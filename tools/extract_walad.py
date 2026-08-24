# -*- coding: utf-8 -*-
# SPDX-License-Identifier: GPL-3.0-or-later
# Wasl - a verifiable nasab. Copyright (C) 2026 Hendra Saputra.
"""Parse 'fa-walada X: A, B, C' statements - the standard shape of a genealogy book.

Ibn Hazm and Ibn al-Kalbi are built almost entirely out of these, so one parser opens both.
Prints candidates for review; --write commits them through the ingest layer, which refuses any
quote the corpus does not carry.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ingest, nasab
from translit import translit

# the father/children separator is usually ':' but Ibn Hazm's Yemeni sections often use ';'
WALAD = re.compile(r"(?:ف|و)?ولد\s+(?P<f>[^:؛.]{2,120}?)\s*[:؛]\s*(?P<k>[^.]{2,600}?)(?=\.|$)")
# 'bint' and 'ibna' are links in a chain exactly as 'bn' is. Leaving them out meant every
# "X bint Y b. Z" was read as one long name and hung on Z instead of Y - which is why the tree
# held 16 women when the sources name hundreds.
BN = re.compile(r"\s+(?:ابنة|بنت|ابن|بن)\s+")
FEM_LINK = re.compile(r"\s+(?:ابنة|بنت)\s+")

# honorifics are not names. 'rasul Allah wa-sayyid walad Adam' is one man under two epithets,
# and splitting it on the 'wa-' invented a son called Sayyid for the Prophet's father.
HONORIFIC = re.compile(
    r"رسول\s+الله|سيد\s+ولد\s+آدم|صلى\s+الله\s+عليه\s+و[آله\s]*سلم|"
    r"عليه\s+السلام|عليهما\s+السلام|رضي\s+الله\s+عنه[ما]?|رضى\s+الله\s+عنه[ما]?|"
    r"خليل\s+الله|كليم\s+الله|أمير\s+المؤمنين|عز\s+وجل|تبارك\s+وتعالى|جل\s+ثناؤه")

# a child is often given with his kunya: 'al-Hasan Aba Muhammad'. The name is the head.
KUNYA_TAIL = re.compile(r"\s+(?:أب[اوي]|أم)\s+[ء-ي].*$")
# clauses that comment on a name rather than name a person
STOP = re.compile(r"^(?:و?في|و?هو|و?هم|و?هي|و?كان|و?قد|و?قيل|و?ذكر|أم|و?أم|لا |ثم |أ?لهم|"
                  r"و?ليس|و?منهم|و?من\b|و?إلي|و?به|و?لم|درج|و?الله|و?أما|و?قال|و?يقال|"
                  r"و?هؤلاء|و?هذ|و?بنو|و?بني|[وف]?ولد|و?إخوت|و?سائر|و?جميع|و?رهط|و?عقب|"
                  r"و?انقرض|و?له|و?لها|و?لهم|و?عدد|و?بطن|و?فيهم|ابن(?:ه|اه)?\b|بن\b|"
                  r"بنت\b|ابنة\b|زوج\b|سيف\s+الله|أسلم\b|قتل\b|هاجر\b|مات\b|فأما\b|لي\b)")
CHILD_TAIL = re.compile(r"\s+(?:درج|بنو|لأم|مبايعة|الجواد)\b.*$")
ACC = re.compile(r"ا$")
HUWA = re.compile(r"^\s*و?ه[وي]\s+(?P<alias>[ء-ي][^،؛.]{1,22})")

_namelex = {}


def namelex(work):
    """Every token the work itself uses as a personal name - i.e. seen in the frame 'bn X'.
    A stray verb swept up by the splitter will not be in it; a real name will."""
    if work not in _namelex:
        txt = nasab.clean(work)
        toks = set()
        for m in re.finditer(r"\b(?:ابن|بن|بنت)\s+([ء-ي]{2,})", txt):
            toks.add(nasab.normalise(m.group(1)))
        for m in re.finditer(r"([ء-ي]{2,})\s+(?:ابن|بن)\s", txt):
            toks.add(nasab.normalise(m.group(1)))
        _namelex[work] = toks
    return _namelex[work]


def is_name(work, s):
    """Accept a candidate only if the corpus uses it as a name, or we know the reading."""
    from translit import _look
    head = s.split()[-1] if s.startswith(("عبد", "أبو", "أم", "بنت")) else s.split()[0]
    return _look(s) is not None or nasab.normalise(head) in namelex(work) \
        or nasab.normalise(s) in namelex(work)


TAIL = re.compile(r"\s*(?:ولد|كان\b|منهم|رضي الله|وهم|فمن|وفيه|وهو|ولده|أعقب|عقبه|"
                  r"لصلبه|ثمانية|سبعة|ستة|خمسة|أربعة|ثلاثة|رجال|ذكرا|اثنا|فولد).*$")


def father_of_stmt(raw):
    """clean() joins the heading line onto the body, so a statement often reads
    'walada al-Zubayr b. Abd al-Muttalib walada al-Zubayr b. Abd al-Muttalib:'. Take the text
    after the LAST 'walada', then cut the commentary that trails the name."""
    raw = re.split(r"\bولد\s+", " " + raw)[-1]
    return norm_name(TAIL.sub("", raw))


PARTICLE = re.compile(r"\s+(?:لم|له|لها|لهم|لا|قد|ثم|من|في|هو|هي|هم|إلا|غير|أن|إن|بن|ابن|"
                      r"على|عن|مع|بعد|قبل|أبو|أم)$")


def norm_name(w):
    """Undo the accusative these lists are written in: nizaran -> nizar, aba talib -> abu talib."""
    w = w.replace("ما عض", "ماعض")
    # kunya only when a name follows: bare 'Ubayy' is a name in its own right, and turning it
    # into a bare 'Abu' made it look like a stray particle and got it pruned
    w = re.sub(r"^أبا\s+", "أبو ", w.strip())
    w = re.sub(r"^أب[يى]\s+", "أبو ", w)
    w = re.sub(r"\bابنة\b", "بنت", w)
    w = re.sub(r"[#~*]+", " ", w).strip(" ،؛.()[]«»-")
    prev = None
    while prev != w:                       # a name never ends in a particle
        prev = w
        w = PARTICLE.sub("", w).strip()
    return w


def dealef(w):
    """Candidate readings of a word that may carry an accusative alif."""
    out = [w]
    if len(w) > 3 and w.endswith("ا"):
        out.append(w[:-1])
    if len(w) > 4 and w.endswith("ان") is False and w.endswith("ا"):
        pass
    return out


def children(work, blob):
    """Split a child list into names, dropping the commentary that follows each.
    'X, wa-huwa Y' is one person under two readings, not two people - carry Y as an alias."""
    blob = HONORIFIC.sub(" ", blob)      # before any splitting
    out = []
    for piece in re.split(r"؛", blob):
        # 'wa-' is the ordinary separator too: 'Mu'awiya wa-Wa'il' is two sons, not one name
        piece = re.sub(r"([ء-ي])\s+و(?=[ء-ي])", r"\1، و", piece)
        parts = re.split(r"،", piece)
        for i, sub in enumerate(parts):
            raw = norm_name(CHILD_TAIL.sub("", re.sub(r"^\s*و", "", sub.strip())))
            if not raw:
                continue
            if STOP.match(raw):
                return out        # commentary has begun; nothing after it is a child name
            s = BN.split(raw)[0].strip()        # a child named "X bn Y" restates the father
            s = re.sub(r"\s*\(.*", "", s).strip()
            kun = None
            m2 = KUNYA_TAIL.search(s)
            if m2 and len(s) > len(m2.group(0)):
                kun = norm_name(m2.group(0))
                s = s[:m2.start()].strip()      # 'al-Hasan Aba Muhammad' -> al-Hasan
            if not (2 <= len(s) <= 24 and re.match(r"^[ء-ي]", s) and is_name(work, s)):
                return out
            alias = None
            if i + 1 < len(parts):
                h = HUWA.match(parts[i + 1].strip())
                if h:
                    a = norm_name(h.group("alias"))
                    if a and is_name(work, a):
                        alias = a
            out.append((s, alias or kun))
            # keep going: 'walada al-Khazraj: Amr, Awf, Jusham, Ka'b, al-Harith' is five sons,
            # and taking only the first cost the whole Ansar clan structure
    return out


_conts = {}


def continuations(work, chain):
    """How many different grandfathers the book itself gives this chain.

    'Qusayy b. Kilab' is only ever continued '... b. Murra' - one man. 'Muhammad b. Abd Allah'
    is continued a hundred different ways, so a bare mention of it identifies nobody. This is
    the test that keeps other men's sons from being hung on the Prophet: ask the corpus how
    ambiguous its own phrase is, rather than guessing from the small tree we have built."""
    key = (work, tuple(chain))
    if key in _conts:
        return _conts[key]
    text = nasab.index(work)[0]
    pat = r"\s+(?:ا?بن)\s+".join(re.escape(nasab.normalise(c)) for c in chain)
    outs = set()
    for m in re.finditer(pat + r"(?:\s+(?:ا?بن)\s+([ء-ي]+))?", text):
        if m.group(1):
            outs.add(m.group(1))
    _conts[key] = outs
    return outs


def identifies(work, chain, store, scope=None):
    """Does this chain, as the book uses it, pick out one man?

    A bare eponym needs different treatment from a bare name. 'Qahtan' is continued a dozen
    ways in al-Baladhuri, but those are rival accounts of ONE man's ancestry, not a dozen men.
    'Muhammad' is a dozen men. The tree can tell them apart: an eponym has exactly one bearer,
    a common name has many. So a one-name chain resolves only when the whole tree holds a
    single person of that name."""
    if len(chain) == 1:
        if store is None:
            return False
        # The corpus decides first. A bare 'walada Ibrahim:' identifies nobody - Ibn Hazm
        # continues that name 55 different ways - and trusting tree-uniqueness alone made the
        # answer depend on how many Ibrahims happened to be in the tree when the pass ran.
        # Tribal eponyms sit at 1-6 continuations, personal names in the dozens or hundreds.
        if len(continuations(work, chain)) > 3:
            return False
        bearers = store._byname.get(nasab.normalise(chain[0]), ())
        if scope is not None:
            bearers = [b for b in bearers if b in scope]
        # then uniqueness inside the declared trunk: Qahtan's Ya'rub and Isma'il's are two
        # different men, and neither should block the other from growing its own side
        return len(bearers) == 1
    if len(chain) >= 4:
        return True
    cont = continuations(work, chain)
    if len(cont) <= 1:
        return True
    # several continuations exist: accept only if the tree's candidate matches one of them
    # AND the chain is long enough that the coincidence is unlikely
    if len(chain) >= 3 and len(cont) <= 3:
        return True
    return False


def run(work, store, limit=None, quiet=False, under=None):
    """under: only take statements whose father already sits beneath this person, so a pass
    grows the tree outward from a chosen trunk instead of sprawling across every tribe."""
    text = nasab.clean(work)
    scope = store.descendants(under) if under else None
    added = edges = skipped = 0
    for m in WALAD.finditer(text):
        father_raw = father_of_stmt(m.group("f"))
        chain = [norm_name(x) for x in BN.split(father_raw) if norm_name(x)]
        if not chain:
            continue
        # resolve inside the scope: 'fa-walada Khalaf' is unambiguous among Quraysh even
        # when a dozen men named Khalaf exist elsewhere in the book
        fid = store.find_by_chain(chain, scope=scope)
        if fid is None or not identifies(work, chain, store, scope):
            skipped += 1
            continue
        stmt = m.group(0)
        kids = children(work, m.group("k"))
        if not kids:
            continue
        for kid, alias in kids:
            # quote: from "walada" up to and including this child, contiguous in the text
            hits = [mm for w in dealef(kid) for mm in re.finditer(re.escape(w), stmt)]
            if not hits:
                continue
            quote = stmt[:max(h.end() for h in hits)]
            if nasab.locate(work, quote) is None:
                continue
            cid_before = len(store.claims)
            kid_id = store.person(kid, father=fid, _alias=alias)
            if kid_id is None:
                continue
            if scope is not None:
                scope.add(kid_id)          # a new child widens the trunk, incrementally

            flat = translit(kid)[0]
            store.add("father_of", fid, quote,
                      f"{flat} son of {store.people[fid]['name_lat']} — from: “{store.people[fid]['name_lat']} begot …”",
                      object=kid_id, work=work, grade="explicit", source_pattern="walada")
            if len(store.claims) > cid_before:
                edges += 1
                if alias:
                    aq = stmt[:stmt.index(alias) + len(alias)] if alias in stmt else None
                    if aq:
                        store.add("alias", kid_id, aq,
                                  f"{flat}, who is {translit(alias)[0]}", work=work,
                                  value_ar=alias, value_lat=translit(alias)[0],
                                  source_pattern="wa-huwa")
                if not quiet:
                    print(f"  {store.people[fid]['name_lat']:22} -> {flat}"
                          + (f"  (= {translit(alias)[0]})" if alias else ""))
        added += 1
        if limit and added >= limit:
            break
    print(f"{work}: {added} statements used, {edges} edges, {skipped} fathers not yet in tree")
    return edges


if __name__ == "__main__":
    st = ingest.Store()
    work = sys.argv[1]
    lim = int(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2].isdigit() else None
    run(work, st, limit=lim, quiet="-q" in sys.argv)
    st.report("result (not written)")
