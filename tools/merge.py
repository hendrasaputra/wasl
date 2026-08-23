# -*- coding: utf-8 -*-
# SPDX-License-Identifier: GPL-3.0-or-later
# Wasl - a verifiable nasab. Copyright (C) 2026 Hendra Saputra.
"""Merge people the sources spell two ways.

Editions differ on a letter and the parsers, quite correctly, refuse to assume: 'Rawah b. Adi'
and 'Rizah b. Adi' become two sons of Adi, and the whole branch beneath - Qurt, Abd Allah,
Riyah, Abd al-Uzza, Nufayl - duplicates with them. Worse, the duplicate then makes every chain
through it AMBIGUOUS, so find_by_chain refuses to resolve and Umar b. al-Khattab can never
attach. One spelling variant high in the tree silently costs hundreds of companions.

The merge rule needs to be tight, because 'Amr' and 'Umar' are also one letter apart and are
not the same man. So: merge two siblings only when their names differ by at most one letter AND
they have a child name in common. Shared issue is the evidence; near-spelling alone is not.
Exact-duplicate siblings merge outright.

Merging is recursive - once the parents are one, their same-named children are duplicate
siblings too - and runs to a fixpoint.
"""
import json, os, re, sys, collections
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path[:0] = [ROOT, os.path.dirname(os.path.abspath(__file__))]
import nasab


def case_variant(a, b):
    """Same name, different grammatical case - deterministic morphology, not a guess.

    Arabic lists inflect: 'walada Nizar: Sayyaran' is Sayyar in the accusative, and a kunya is
    Abu / Aba / Abi depending on the sentence. Two siblings differing only that way are one man,
    so this needs no corroborating evidence the way a one-letter spelling difference does.
    """
    if a == b:
        return True
    # trailing accusative alif: Khuwaylidan / Khuwaylid
    if a == b + "ا" or b == a + "ا":
        return True
    # kunya case: Abu / Aba / Abi al-As
    ka = re.sub(r"^اب[اوي]\b", "ابو", a)
    kb = re.sub(r"^اب[اوي]\b", "ابو", b)
    return ka == kb and ka.startswith("ابو")


def dist1(a, b):
    """True if a and b are within one substitution/insertion/deletion."""
    if a == b:
        return True
    la, lb = len(a), len(b)
    if abs(la - lb) > 1:
        return False
    if la == lb:
        return sum(x != y for x, y in zip(a, b)) == 1
    if la > lb:
        a, b, la, lb = b, a, lb, la
    for i in range(lb):                       # b with one char removed
        if b[:i] + b[i + 1:] == a:
            return True
    return False


def uncopy(people, claims):
    """Cut a spine the parser copied into the wrong place.

    Ibn Hazm genuinely records a Nizar b. Mu'ays b. Amir b. Luayy - a Qurashi, and he stays.
    But every later 'fa-walada Nizar ...' statement then resolved onto HIM, and the whole
    Adnani spine was rebuilt underneath: Mudar, Ilyas, Mudrika, Khuzayma, Kinana, al-Nadr,
    Malik, Fihr, and all of Quraysh below that - 644 nodes of duplicate.

    The signature is decisive. Names recur across generations in a real genealogy, but a run of
    four CONSECUTIVE names repeating inside one line of descent means a segment was copied. We
    walk the two sequences up until they diverge; the last name that still agrees is the one the
    source really attests, so it is KEPT, and its children are the copy.
    """
    by = {p["id"]: p for p in people}
    fa, kids = {}, {}
    for c in claims:
        if c["type"] == "father_of":
            fa.setdefault(c["object"], c["subject"])
            kids.setdefault(c["subject"], []).append(c["object"])
    N, RUN = nasab.normalise, 4

    def line(pid):
        out, cur = [], pid
        while cur:
            out.append(cur)
            cur = fa.get(cur)
        return out

    tops = set()
    for pid in list(by):
        ids = line(pid)
        nm = [N(by[x]["name_ar"]) for x in ids]
        for i in range(len(nm) - RUN):
            for j in range(i + RUN, len(nm) - RUN + 1):
                if nm[i:i + RUN] == nm[j:j + RUN]:
                    k = 0
                    while i + k < len(nm) and j + k < len(nm) and nm[i + k] == nm[j + k]:
                        k += 1
                    tops.add(ids[i + k - 1])     # attested; its CHILDREN are the copy
                    break
            else:
                continue
            break
    if not tops:
        return people, claims
    drop = set()
    for t in tops:
        if set(line(t)[1:]) & tops:
            continue                            # an outer one already covers this
        stack = list(kids.get(t, ()))
        while stack:
            x = stack.pop()
            if x in drop:
                continue
            drop.add(x)
            stack.extend(kids.get(x, ()))
        print(f"   uncopy: keeping {by[t]['name_lat']} under "
              f"{by[fa[t]]['name_lat'] if fa.get(t) else '-'}, cutting the copy beneath it")
    people = [p for p in people if p["id"] not in drop]
    claims = [c for c in claims
              if c["subject"] not in drop and (not c.get("object") or c["object"] not in drop)]
    print(f"   {len(drop)} copied nodes removed")
    return people, claims


def unweld(people, claims):
    """Undo a chain welded by a missing 'bn' in the printed edition.

    al-Isti'ab 2:614 prints 'b. Nufayl Abd al-Uzza b. Riyah' where the chain is 'b. Nufayl b.
    Abd al-Uzza b. Riyah'. The splitter did the right thing with wrong input and made one person
    called 'Nufayl Abd al-Uzza', a generation short - so Sa'id b. Zayd appeared twice, once at
    generation 51 and once at 52.

    It is recognisable without guessing: a node X under P whose name is 'A B', where P has
    ANOTHER child named B, and that child has a child named A. The welded node is then the same
    man as that grandchild, reached by a defective route. We move X's children onto the real
    grandchild and drop X - not merge, because merging would keep X's father edge and assert
    that the grandchild descends directly from P, which is exactly the error being removed.
    """
    by = {p["id"]: p for p in people}
    kids, fa = {}, {}
    for c in claims:
        if c["type"] == "father_of":
            fa.setdefault(c["object"], c["subject"])
            kids.setdefault(c["subject"], [])
            if c["object"] not in kids[c["subject"]]:
                kids[c["subject"]].append(c["object"])
    N = nasab.normalise
    redirect, drop = {}, set()
    for x, par in list(fa.items()):
        w = by[x]["name_ar"].split()
        if len(w) < 2:
            continue
        for k in range(1, len(w)):
            A, B = " ".join(w[:k]), " ".join(w[k:])
            sib = next((s for s in kids.get(par, ()) if s != x and N(by[s]["name_ar"]) == N(B)), None)
            if not sib:
                continue
            g = next((q for q in kids.get(sib, ()) if N(by[q]["name_ar"]) == N(A)), None)
            if g and g != x:
                redirect[x] = g
                drop.add(x)
                print(f"   unweld '{by[x]['name_ar']}' -> '{by[g]['name_ar']}' under {by[par]['name_lat']}")
                break
    if not redirect:
        return people, claims
    out = []
    for c in claims:
        if c["type"] == "father_of" and c["object"] in redirect:
            continue                     # the defective edge itself goes
        if c["subject"] in redirect:     # its children move to the real man
            c = dict(c, subject=redirect[c["subject"]])
        if c.get("object") in redirect:
            c = dict(c, object=redirect[c["object"]])
        out.append(c)
    people = [p for p in people if p["id"] not in drop]
    print(f"   {len(drop)} welded node(s) removed")
    return people, out


def main(write=False):
    people = [json.loads(l) for l in open(f"{ROOT}/people.jsonl", encoding="utf-8") if l.strip()]
    claims = [json.loads(l) for l in open(f"{ROOT}/claims.jsonl", encoding="utf-8") if l.strip()]
    print("cutting spines copied into the wrong place")
    people, claims = uncopy(people, claims)
    print("unwelding chains broken by a missing bn in the edition")
    people, claims = unweld(people, claims)

    by = {p["id"]: p for p in people}
    alias = {}                                # loser -> winner

    def root(x):
        while x in alias:
            x = alias[x]
        return x

    merges, rounds = [], 0
    while True:
        rounds += 1
        kids = collections.defaultdict(list)
        for c in claims:
            if c["type"] == "father_of":
                kids[root(c["subject"])].append(root(c["object"]))
        for k in kids:
            kids[k] = list(dict.fromkeys(kids[k]))
        # 'al-Abbas' and 'Abbas' under one father are one man written two ways; the article is
        # not a distinguishing letter, and edit distance alone treats it as two
        def key(x):
            n = nasab.normalise(by[x]["name_ar"])
            return n[2:] if n.startswith("ال") and len(n) > 3 else n
        nm = {p: key(p) for p in by}
        freq = collections.Counter(nm[p] for p in by if p not in alias)
        found = 0
        for f, ch in list(kids.items()):
            for i in range(len(ch)):
                for j in range(i + 1, len(ch)):
                    a, b = root(ch[i]), root(ch[j])
                    if a == b:
                        continue
                    na, nb = nm[a], nm[b]
                    if na == nb or case_variant(na, nb):
                        pass                    # same man, same father - possibly inflected
                    elif dist1(na, nb):
                        ca = {nm[x] for x in kids.get(a, ())}
                        cb = {nm[x] for x in kids.get(b, ())}
                        shared = ca & cb
                        # One shared child is weak when the name is Abd Allah or Muhammad, and
                        # 'Amr' and 'Umar' are one letter apart without being one man. Ask for
                        # two children in common, or one that is rare enough to mean something.
                        if not (len(shared) >= 2 or
                                (len(shared) == 1 and freq[next(iter(shared))] <= 4)):
                            continue
                    else:
                        continue
                    # keep the better-attested spelling: more works citing it, then more issue
                    score = lambda x: (len({c["work"] for c in claims
                                            if c["type"] == "father_of" and root(c.get("object") or "") == x}),
                                       len(kids.get(x, ())))
                    win, lose = (a, b) if score(a) >= score(b) else (b, a)
                    alias[lose] = win
                    merges.append((by[lose]["name_ar"], by[win]["name_ar"], by[f]["name_lat"]))
                    found += 1
        if not found or rounds > 40:
            break

    print(f"{len(alias)} merged in {rounds} rounds")
    for lo, wi, f in merges[:14]:
        print(f"   {lo} -> {wi}   (under {f})")
    if len(merges) > 14:
        print(f"   ... and {len(merges)-14} more")

    people = [p for p in people if p["id"] not in alias]
    seen, out = set(), []
    for c in claims:
        c["subject"] = root(c["subject"])
        if c.get("object"):
            c["object"] = root(c["object"])
        if c["type"] == "father_of" and c["subject"] == c["object"]:
            continue
        k = (c["type"], c["subject"], c.get("object"), c["work"], nasab.normalise(c["ar"]))
        if k in seen:
            continue
        seen.add(k)
        out.append(c)
    print(f"claims {len(claims)} -> {len(out)}, people -> {len(people)}")
    if write:
        with open(f"{ROOT}/people.jsonl", "w", encoding="utf-8") as f:
            for p in people:
                f.write(json.dumps(p, ensure_ascii=False) + "\n")
        with open(f"{ROOT}/claims.jsonl", "w", encoding="utf-8") as f:
            for c in out:
                f.write(json.dumps(c, ensure_ascii=False) + "\n")
        print("written")


if __name__ == "__main__":
    main(write="--write" in sys.argv)
