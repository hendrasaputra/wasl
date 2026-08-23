#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
# Wasl - a verifiable nasab. Copyright (C) 2026 Hendra Saputra.
"""Independent checks. validate.py trusts nasab.py's page mapping; these do not - they
re-derive page boundaries straight from the raw corpus file with plain string operations,
and confirm the checker actually rejects bad data rather than waving it through.

    python3 test_wasl.py
"""
import json, os, re, sys, collections
import nasab

ROOT = os.path.dirname(os.path.abspath(__file__))
ok = 0


def check(label, cond, detail=""):
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
    any_mark = re.compile(r"PageV\d{2}P\d{3}")
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

print("\nno honorific or unsplit chain ever became a person")
HON = ("رسول الله", "صلى الله", "سيد ولد", "عليه السلام", "رضي الله", "أمير المؤمنين")
bad = [p["name_ar"] for p in byid.values() if any(h in p["name_ar"] for h in HON)]
check("no name contains an honorific", not bad, "; ".join(bad[:4]))
unsplit = [p["name_ar"] for p in byid.values()
           if re.search(r"\s+(?:ابنة|بنت|ابن|بن)\s+", p["name_ar"])]
check("no name is an unsplit chain", not unsplit, "; ".join(unsplit[:4]))

print("\nnormalisation folds printings, not readings")
check("hamza forms fold", nasab.normalise("إلياس") == nasab.normalise("الياس"))
check("ta marbuta folds", nasab.normalise("خزيمة") == nasab.normalise("خزيمه"))
check("distinct names stay distinct", nasab.normalise("عمرو") != nasab.normalise("عامر"))

print(f"\n{ok} checks passed.")
