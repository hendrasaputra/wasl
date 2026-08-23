#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
# Wasl - a verifiable nasab. Copyright (C) 2026 Hendra Saputra.
"""Independent checks. validate.py trusts nasab.py's page mapping; these do not - they
re-derive page boundaries straight from the raw corpus file with plain string operations,
and confirm the checker actually rejects bad data rather than waving it through.

    python3 test_wasl.py

WHY A SECOND CHECKER. validate.py imports nasab.py, so it can agree with its own bug and
report a clean run over wrong data. Twice now it has: the repeated page marker in Ibn Sa'd,
where page_text returned only the first of several disjoint segments; and PAGE_RE reading
three digits of a four-digit milestone, which put 286 claims on a page a tenth of the true
one while every quote still "verified". Both were found here, because raw_page() slices the
file by hand and shares nothing with the indexer.

So a check in this file must not import the thing it is checking. Where that is unavoidable
- the summaries need entries.py to know where an entry is - the check re-reads the raw pages
itself and asserts that the check CAN fail, by feeding it a genuine phrase from a different
entry and requiring rejection.

The assertions on the Prophet's immediate family are named one by one on purpose. Every one
of them was written because the data broke it: an epithet became a son of the Prophet's
father, granddaughters were hung on their grandfathers and sexed male, and a man who died in
infancy acquired six descendants. Totals cannot show that; only naming the family can.

Exits non-zero on the first failure, so the failing line is the last thing printed.
"""
import json, os, re, sys, collections
import nasab

ROOT = os.path.dirname(os.path.abspath(__file__))
ok = 0


def check(label, cond, detail=""):
    """Assert one thing, print it, and stop the run if it is false.

    `detail` is printed only on failure - it carries the measurement that explains it.
    """
    global ok
    print(("  ok   " if cond else "  FAIL ") + label + (f"  {detail}" if detail and not cond else ""))
    if not cond:
        sys.exit(1)
    ok += 1


def raw_page(work, vol, page):
    """Slice page N straight out of the file with plain string ops - deliberately sharing no
    code with nasab.py's index. Some editions (Ibn Sa'd) repeat the same page marker once per
    report, so a page is several disjoint segments; take all of them."""
    txt = open(f"{ROOT}/corpus/{work}.txt", encoding="utf-8").read()
    mark = f"PageV{int(vol):02d}P{int(page):03d}"
    any_mark = re.compile(r"PageV\d{2}P\d+")   # \d+: al-Isti'ab pages run past 999
    out, at = [], 0
    while True:
        end = txt.find(mark, at)
        if end < 0:
            return " ".join(out)
        prev = [m.end() for m in any_mark.finditer(txt, 0, end)]
        out.append(txt[(prev[-1] if prev else 0):end])
        at = end + len(mark)


print("page mapping, re-derived from the raw file")
for work, vol, page, needle in [
    ("IbnHisham", 1, 1, "محمد بن عبد الله"),
    ("IbnHisham", 1, 2, "واسم مدركة: عامر"),
    ("IbnHisham", 1, 3, "بن شيث بن آدم"),
    ("IbnSad", 1, 37, "واسمه شيبة الحمد"),
    ("IbnAbdAlBarr", 1, 25, "لم يختلف أهل العلم بالأنساب"),
    ("IbnAlAthir", 1, 20, "هو محمد بن عبد الله بن عبد المطلب"),
    ("Baladhuri", 1, 3, "بن يارد بن مهلائيل"),
]:
    raw = nasab.normalise(raw_page(work, vol, page))
    check(f"{work} {vol}:{page} contains {needle[:26]}", nasab.normalise(needle) in raw)

print("\nevery committed claim, checked against the raw slice - not the index")
claims = [json.loads(l) for l in open(f"{ROOT}/claims.jsonl", encoding="utf-8") if l.strip()]
bad = []
for c in claims:
    # join with a space: pages abut at a word boundary, never mid-word
    span = " ".join(nasab.normalise(raw_page(c["work"], c["vol"], p))
                    for p in range(c["page"], c.get("page_end", c["page"]) + 1))
    if nasab.normalise(c["ar"]) not in re.sub(r"\s+", " ", span):
        bad.append(f"{c['cid']} {c['work']} {c['vol']}:{c['page']}")
check(f"all {len(claims)} quotes present in their raw page slice", not bad, "; ".join(bad[:5]))

print("\nthe checker rejects bad data")
w, v, p = "IbnHisham", 1, 1
check("a fabricated quote is not found", nasab.locate(w, "محمد بن عبد الرحمن بن أبي بكر الصديق") is None)
real = "محمد بن عبد الله ابن عبد المطلب"
check("a real quote is found", nasab.locate(w, real) == (1, 1, 1))
check("a real quote cited to the wrong page is caught", not (1 <= 99 <= nasab.locate(w, real)[2]))
check("a quote spanning a page break resolves to its true span",
      nasab.locate(w, "بن مالك بن النضر ابن كنانة") == (1, 1, 2))

print("\ndata integrity")
people = {json.loads(l)["id"] for l in open(f"{ROOT}/people.jsonl", encoding="utf-8") if l.strip()}
check("every claim references known persons",
      all(c["subject"] in people and (not c.get("object") or c["object"] in people) for c in claims))
check("no claim carries an empty translation", all(c["en"].strip() for c in claims))
check("no claim carries an empty quote", all(c["ar"].strip() for c in claims))
check("claim ids are unique", len({c["cid"] for c in claims}) == len(claims))
works = set(nasab.sources())
check("every cited work is declared in sources.tsv", all(c["work"] in works for c in claims))
check("both readings of Mudrika's name survive",
      {c.get("value_lat") for c in claims if c["type"] == "alias" and c["subject"] == "p.mudrika"}
      >= {"ʿĀmir", "ʿAmr"})
check("the chain is 50 generations",
      any(c["type"] == "chain" and c.get("n_generations") == 50 for c in claims))
check("no node claims an unsourced birth year",
      all(c.get("date_basis") in (None, *("attested attested_relative derived_from_age_at_death "
          "generation_estimate unknown").split()) for c in claims))

print("\nthe core family, checked name by name")
# A parser error anywhere is bad; a parser error here is the project failing at the one thing
# it exists to get right. Every one of these assertions was written because the data broke it:
# an epithet became a son of the Prophet's father, granddaughters were hung on their
# grandfather, and 'bint' was missing from the chain splitter so every woman was mis-attached.
kids = collections.defaultdict(list)
for c in claims:
    if c["type"] == "father_of":
        kids[c["subject"]].append(c["object"])
byid = {p["id"]: p for p in json.load(open(f"{ROOT}/people.jsonl", encoding="utf-8"))} \
       if False else {json.loads(l)["id"]: json.loads(l)
                      for l in open(f"{ROOT}/people.jsonl", encoding="utf-8") if l.strip()}


def person(chain):
    """Resolve a name chain (shallowest first) to one person id, or None if ambiguous.

    Deliberately a second implementation of what build.py's find() does. If the two ever
    disagree, one of them is wrong, and this file exists to be the one that notices.
    """
    hits = []
    for a in [p for p in byid if nasab.normalise(byid[p]["name_ar"]) == nasab.normalise(chain[-1])]:
        cur = a
        for nm in reversed(chain[:-1]):
            cur = next((k for k in kids.get(cur, ())
                        if nasab.normalise(byid[k]["name_ar"]) == nasab.normalise(nm)), None)
            if cur is None:
                break
        if cur:
            hits.append(cur)
    return hits[0] if len(set(hits)) == 1 else None


def names_of(chain):
    """The transliterated names of one person's children, sorted and de-duplicated."""
    pid = person(chain)
    return sorted({byid[k]["name_lat"] for k in dict.fromkeys(kids.get(pid, []))}) if pid else None


abdallah = names_of(["عبد الله", "عبد المطلب", "هاشم"])
check("the Prophet's father has exactly one child", abdallah == ["Muḥammad"], str(abdallah))
# Ibn Hazm says so outright one sentence after the list the parser misread:
# 'lam yakun li-Abd Allah walad ghayruhu'
check("and the sources say so: lam yakun li-Abd Allah walad ghayruhu",
      nasab.locate("IbnHazm", "لم يكن لعبد الله ولد غيره") is not None)

amuttalib = names_of(["عبد المطلب", "هاشم", "عبد مناف"])
check("Abd al-Muttalib has the ten sons and six daughters Ibn Hisham names",
      len(amuttalib) == 16, str(amuttalib))
sexes = collections.Counter(byid[k]["sex"] for k in
                            dict.fromkeys(kids.get(person(["عبد المطلب", "هاشم", "عبد مناف"]), [])))
check("ten male, six female", sexes["M"] == 10 and sexes["F"] == 6, str(dict(sexes)))

prophet = names_of(["محمد", "عبد الله", "عبد المطلب"])
check("the Prophet's seven children",
      set(prophet) == {"al-Qāsim", "Zaynab", "Ruqayya", "Fāṭima", "Umm Kulthūm",
                       "ʿAbd Allāh", "Ibrāhīm"}, str(prophet))
check("Abu Talib's four sons",
      set(names_of(["أبو طالب", "عبد المطلب", "هاشم"])) == {"Ṭālib", "ʿAqīl", "Jaʿfar", "ʿAlī"},
      str(names_of(["أبو طالب", "عبد المطلب", "هاشم"])))

# The Prophet's sons all died in infancy - Ibn Hazm: Ibrahim 'died young, not completing two
# years'. A chain parser once hung six descendants on him, because 'walada Ibrahim:' is a bare
# one-name chain and Ibn Hazm continues that name 55 different ways.
for son in ("إبراهيم", "القاسم", "عبد الله"):
    pid = person([son, "محمد", "عبد الله"])
    check(f"{son} b. Muhammad has no descendants",
          pid is not None and not kids.get(pid), str(kids.get(pid)))
check("and the sources say so: mata saghiran, lam yastakmil amayn",
      nasab.locate("IbnHazm", "مات صغيرا، لم يستكمل عامين") is not None)

# A missing 'bn' in a printed edition welds two generations into one name - al-Isti'ab 2:614
# prints 'b. Nufayl Abd al-Uzza b. Riyah' - which put Sa'id b. Zayd in the tree twice, once at
# generation 51 and once at 52. Recognisable without guessing: a node 'A B' whose parent has
# another child B, which in turn has a child A.
welded = []
for pid, p in byid.items():
    par = next((c["subject"] for c in claims
                if c["type"] == "father_of" and c.get("object") == pid), None)
    if not par:
        continue
    w = p["name_ar"].split()
    for i in range(1, len(w)):
        A, B = " ".join(w[:i]), " ".join(w[i:])
        sib = next((s for s in kids.get(par, ())
                    if s != pid and nasab.normalise(byid[s]["name_ar"]) == nasab.normalise(B)), None)
        if sib and any(nasab.normalise(byid[g]["name_ar"]) == nasab.normalise(A)
                       for g in kids.get(sib, ())):
            welded.append(p["name_ar"])
            break
check("no chain welded by a missing bn", not welded, "; ".join(welded[:4]))

# and the man that bug produced twice is single
said = [pid for pid, p in byid.items()
        if nasab.normalise(p["name_ar"]) == nasab.normalise("سعيد")
        and any(c["type"] == "father_of" and c.get("object") == pid
                and nasab.normalise(byid[c["subject"]]["name_ar"]) == nasab.normalise("زيد")
                for c in claims)]
check("Sa'id b. Zayd appears once", len(said) == 1, f"{len(said)} nodes")

# no two nodes may share a full lineage - that is the definition of the same man twice
sig = {}
dupsig = []
for pid in byid:
    chain, cur = [], pid
    while cur:
        chain.append(nasab.normalise(byid[cur]["name_ar"]))
        cur = next((c["subject"] for c in claims
                    if c["type"] == "father_of" and c.get("object") == cur), None)
    k = " < ".join(chain)
    if k in sig:
        dupsig.append(byid[pid]["name_lat"])
    sig[k] = pid
check("no two people share a full lineage", not dupsig, "; ".join(dupsig[:4]))

# and no father has two children of the same name, or of the same name in another case
def fold_case(x):
    """Fold the case endings a name picks up in running Arabic, so 'Umar and 'Umara are not
    counted as two sons of the same father when they are one man quoted twice."""
    x = nasab.normalise(x)
    x = re.sub(r"^اب[اوي]\b", "ابو", x)
    return x[:-1] if x.endswith("ا") and len(x) > 3 else x
sibs = collections.defaultdict(list)
for c in claims:
    if c["type"] == "father_of":
        sibs[c["subject"]].append(c["object"])
clash = []
for f, ch in sibs.items():
    seen = {}
    for k in dict.fromkeys(ch):
        key = fold_case(byid[k]["name_ar"])
        if key in seen:
            clash.append(f'{byid[f]["name_lat"]}: {byid[k]["name_ar"]}')
        seen[key] = k
check("no father has the same son twice", not clash, "; ".join(clash[:4]))

# A run of four CONSECUTIVE names repeating inside one line of descent is not a genealogy, it
# is a segment the parser copied. Ibn Hazm's real Nizar b. Mu'ays once collected the whole
# Adnani spine beneath him - 644 duplicate nodes, including a second Fihr and a second Quraysh.
father_of = {}
for c in claims:
    if c["type"] == "father_of":
        father_of.setdefault(c["object"], c["subject"])
copied = []
for pid in byid:
    seq, cur = [], pid
    while cur:
        seq.append(nasab.normalise(byid[cur]["name_ar"]))
        cur = father_of.get(cur)
    for i in range(len(seq) - 4):
        if any(seq[i:i + 4] == seq[j:j + 4] for j in range(i + 4, len(seq) - 3)):
            copied.append(byid[pid]["name_lat"])
            break
check("no lineage repeats a four-name run", not copied,
      f"{len(copied)} lineages, e.g. {'; '.join(copied[:3])}")

print("\nthe Ummahat al-Mu'minin")
# The marquee names again. A wife reaches the tree by her FATHER's chain and by nothing else,
# so every way of getting her there is a way of getting her there wrong: an early draft hung
# Safiyya bt. Huyayy of Banu al-Nadir on p.al-nadir, which is al-Nadir b. al-Harith of 'Abd
# al-Dar, a Qurashi. Assert them one by one, by the chain the books print.
WIVES = [
 ("Khadīja",   ["خديجة", "خويلد", "أسد"]),
 ("Sawda",     ["سودة", "زمعة", "قيس"]),
 ("ʿĀʾisha",   ["عائشة", "عبد الله", "عثمان"]),
 ("Ḥafṣa",     ["حفصة", "عمر", "الخطاب"]),
 ("Hind",      ["هند", "أبو أمية", "المغيرة"]),
 ("Ramla",     ["رملة", "أبو سفيان", "حرب"]),
 ("Zaynab",    ["زينب", "جحش", "رياب"]),
 ("Zaynab",    ["زينب", "خزيمة", "الحارث"]),
 ("Juwayriya", ["جويرية", "الحارث", "أبو ضرار"]),
 ("Ṣafiyya",   ["صفية", "حيي", "أخطب"]),
 ("Rayḥāna",   ["ريحانة", "زيد", "عمرو"]),
 ("Maymūna",   ["ميمونة", "الحارث", "حزن"]),
]
married = {c["object"] for c in claims if c["type"] == "married_to" and c["subject"] == "p.muhammad"}
wids = {}
for lat, chain in WIVES:
    pid = person(chain)
    wids[lat] = pid
    check(f"{lat} b. {chain[1]} stands where the books put her",
          pid is not None and byid[pid]["name_lat"] == lat and byid[pid]["sex"] == "F"
          and pid in married,
          "not found" if pid is None else
          f"{byid[pid]['name_lat']}/{byid[pid]['sex']}/married={pid in married}")
check("twelve wives, no more and no fewer", len(married) == 12, f"{len(married)}")

# A marriage is not descent. If one ever became a father_of, the tree would assert that the
# Prophet's wives descend from him.
fmap = {c["object"]: c["subject"] for c in claims if c["type"] == "father_of"}
line = set()
n = "p.muhammad"
while n:
    line.add(n)
    n = fmap.get(n)
def below(pid):
    """Every descendant of pid, used to assert that a wife never landed inside the tree."""
    out, stack = set(), [pid]
    while stack:
        for k in kids.get(stack.pop(), ()):
            if k not in out:
                out.add(k)
                stack.append(k)
    return out
desc = below("p.muhammad")
check("no wife is placed in the Prophet's own line",
      not (married & (line | desc)),
      ", ".join(byid[x]["name_lat"] for x in (married & (line | desc))))

# The al-Nadir trap, named: Safiyya is of Banu al-Nadir of the Children of Israel, and must not
# have been anchored inside Quraysh.
quraysh = below(person(["فهر", "مالك", "النضر"]) or "p.__none__")
check("Ṣafiyya bt. Ḥuyayy is not inside Quraysh", wids["Ṣafiyya"] not in quraysh)

# Rule 3: the books count the wives differently in the same chapter, so all the counts stand.
counts = [c for c in claims if c["type"] == "dissent" and c["subject"] == "p.muhammad"]
check("the disputed count is recorded, not resolved", len(counts) >= 4, f"{len(counts)} readings")

print("\npage milestones are read whole, and the entries sit where they claim")
# Re-derived with a plain scan that shares nothing with nasab.py. PAGE_RE captured \d{3}, so
# al-Isti'ab - paginated 1..1969 in one run across four volumes - reported page 1819 as 181
# on 286 published claims. The Arabic was right; the number a reader checks it by was not.
import collections as _c
for work in sorted({c["work"] for c in claims}):
    raw = open(f"{ROOT}/corpus/{work}.txt", encoding="utf-8").read()
    plain = _c.defaultdict(set)
    for v, pg in re.findall(r"PageV(\d+)P(\d+)", raw):
        plain[int(v)].add(int(pg))
    idx = _c.defaultdict(set)
    for _, v, pg in nasab.index(work)[1]:
        idx[v].add(pg)
    # only volumes the index actually carries: a stray PageV00P000 ahead of any text is
    # dropped by the indexer on purpose and is not a truncation
    diff = [(v, max(plain[v]), max(idx[v])) for v in sorted(idx) if max(plain[v]) != max(idx[v])]
    check(f"{work}: every milestone read to its last digit", not diff, str(diff))

entries_rows = [json.loads(l) for l in open(f"{ROOT}/entries.jsonl", encoding="utf-8") if l.strip()]
check("every entry names a work in sources.tsv",
      all(e["work"] in works for e in entries_rows))
check("no entry ends before it begins", all(e["page_end"] >= e["page"] for e in entries_rows))
# A printed page holds a few hundred words. A span that implies thousands means the page
# numbers are wrong even though every quote on them verifies - which is exactly what a
# truncated milestone looks like from the inside.
dense = [f'{e["who"]}/{e["work"]} {e["n_words"]}w over {e["page_end"]-e["page"]+1}pp'
         for e in entries_rows if e["n_words"] / (e["page_end"] - e["page"] + 1) > 700]
check("no entry implies an impossible number of words per page", not dense, "; ".join(dense[:4]))

sys.path.insert(0, f"{ROOT}/tools")
import entries as _e
import build_bios as _bio
from directory import DIRECTORY as _D
_labels = [l for _, items in _D for l, _ in items]
check("every Who's who person has an entry or a stated reason for having none",
      all(l in _e.PINS or l in __import__("build_entries").NO_ENTRY for l in _labels),
      ", ".join(l for l in _labels if l not in _e.PINS))
check("the heading recorded is the heading in the file",
      all(_e.headings(e["work"])[0][_e.find(e["work"], e["pin"])[0][0]].strip().endswith(
          e["heading_ar"].split()[-1]) for e in entries_rows))
outside = []
for e in entries_rows:
    hit, _ = _e.find(e["work"], e["pin"])
    pages = {pg for kind, _, pg in _bio.paragraphs(e["work"], hit[0], hit[1]) if kind == "p"}
    if any(not e["page"] <= pg <= e["page_end"] for pg in pages):
        outside.append(f'{e["who"]}/{e["work"]}: {sorted(pages)}')
check("biography page links stay inside their entry span", not outside, "; ".join(outside[:3]))

print("\nthe summaries rest on text that is really there")
# The one place in this repository where prose is composed rather than quoted, so the one
# place a plausible sentence could pass unchecked. Each anchored sentence is re-read here out
# of the raw page slice - plain string operations, no nasab.py index - and must be inside the
# entry the summary claims to be reading.
spath = f"{ROOT}/summaries.jsonl"
if os.path.exists(spath):
    srows = [json.loads(l) for l in open(spath, encoding="utf-8") if l.strip()]
    # a person can have several entries in one work - Ibn Sa'd files one man once per tabaqa -
    # so gather them all. Keying on (who, work) kept the last and failed every anchor in the
    # rest, which is exactly how Sa'id b. Zayd's summary came out empty.
    erows = {}
    for e in (json.loads(l) for l in open(f"{ROOT}/entries.jsonl", encoding="utf-8") if l.strip()):
        erows.setdefault((e["who"], e["work"]), []).append(e)
    missing, outside = [], []
    for sr in srows:
        blob = nasab.normalise(" ".join(
            raw_page(sr["work"], e["vol"], pg)
            for e in erows[(sr["who"], sr["work"])]
            for pg in range(e["page"], e["page_end"] + 1)))
        for ln in sr["lines"]:
            if ln["basis"] != "anchored":
                continue
            if nasab.normalise(ln["ar"]) not in blob:
                outside.append(f'{sr["who"]}: {ln["ar"][:40]}')
    check(f"every anchored sentence is inside its own entry's pages", not outside,
          "; ".join(outside[:3]))
    check("no editorial sentence smuggles in a number",
          not [l for sr in srows for l in sr["lines"]
               if l["basis"] == "editorial" and any(c.isdigit() for c in l["en"])])
    over = [f'{sr["who"]} {sr["n_editorial"]}/{len(sr["lines"])}' for sr in srows
            if sr["n_editorial"] / len(sr["lines"]) > 0.20]
    check("editorial sentences stay under a fifth of each summary", not over, "; ".join(over))
    long = [f'{sr["who"]} {sr["n_words"]}w' for sr in srows if sr["n_words"] > 400]
    check("no summary runs past its word cap", not long, "; ".join(long))
    # the summaries are the one place English is the original, so id/ms are translated from
    # it. A gap keeps the English and is counted; here we assert there is no gap.
    untr = [f'{sr["who"]}: {l["en"][:40]}' for sr in srows for l in sr["lines"]
            if not (l.get("id") and l.get("ms"))]
    check("every summary sentence carries Indonesian and Malay", not untr,
          f"{len(untr)} untranslated, e.g. " + "; ".join(untr[:2]))
    labels = {l for _, items in _D for l, _ in items}
    check("every summary belongs to somebody in the Who's who",
          all(sr["who"] in labels for sr in srows),
          ", ".join(sr["who"] for sr in srows if sr["who"] not in labels))
    # the check must be able to fail: a real phrase from another entry must be rejected
    other = nasab.normalise("فابتنى دار الندوة، وجعل بابها إلى البيت")
    saf = erows.get(("Ṣafiyya bt. Ḥuyayy", "IbnSad"))
    if saf:
        blob = nasab.normalise(" ".join(raw_page("IbnSad", saf[0]["vol"], pg)
                                        for pg in range(saf[0]["page"], saf[0]["page_end"] + 1)))
        check("and a genuine phrase from a DIFFERENT entry is rejected", other not in blob)

print("\nno honorific or unsplit chain ever became a person")
HON = ("رسول الله", "صلى الله", "سيد ولد", "عليه السلام", "رضي الله", "أمير المؤمنين")
bad = [p["name_ar"] for p in byid.values() if any(h in p["name_ar"] for h in HON)]
check("no name contains an honorific", not bad, "; ".join(bad[:4]))
unsplit = [p["name_ar"] for p in byid.values()
           if re.search(r"(?:^|\s)(?:ابنة|بنت|ابن|بن)(?:\s|$)", p["name_ar"])]
check("no name is an unsplit chain", not unsplit, "; ".join(unsplit[:4]))
artifacts = {"سيف الله", "أسلم يوم الفتح", "زوج زينب بنت", "ابن خالتها هالة",
             "الأبجر- والأبجر هو خدرة", "أبى عمرو- ذكوان", "الحارث علي",
             "العنبس يسير", "بنت صفوان", "كلدة درج", "محمد بنو جعفر",
             "مات في أول خلافة", "الحكم الجواد", "فأما زمعة", "لي اليمن لعبد الله",
             "داود لأم", "عميرة مبايعة", "السمين بإسناده عن يونس"}
bad = sorted(p["name_ar"] for p in byid.values() if p["name_ar"] in artifacts)
check("known commentary and title fragments are absent", not bad, "; ".join(bad))
known_women = {"p.hind-2", "p.aisha", "p.fatima-2", "p.maymuna",
               "p.arwa-2", "p.barra-2", "p.hind-3"}
wrong = [pid for pid in sorted(known_women & set(byid)) if byid[pid]["sex"] != "F"]
check("known surviving women are female", not wrong, "; ".join(wrong))

print("\nnormalisation folds printings, not readings")
check("hamza forms fold", nasab.normalise("إلياس") == nasab.normalise("الياس"))
check("ta marbuta folds", nasab.normalise("خزيمة") == nasab.normalise("خزيمه"))
check("distinct names stay distinct", nasab.normalise("عمرو") != nasab.normalise("عامر"))

print(f"\n{ok} checks passed.")
