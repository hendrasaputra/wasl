# -*- coding: utf-8 -*-
# SPDX-License-Identifier: GPL-3.0-or-later
# Wasl - a verifiable nasab. Copyright (C) 2026 Hendra Saputra.
"""Remove nodes the parsers created out of prose rather than out of names.

A splitter that cuts a child list on punctuation will occasionally cut a clause instead: 'qutila
yawm al-Jamal' (he was killed at the Battle of the Camel) is not a person, and neither is 'ammuhu
Urwa' (his uncle Urwa). validate.py cannot catch these - the Arabic really is on the page - so
they have to be recognised by shape and removed with their claims.

A pruned node takes its descendants with it: they were reached only through a misparse.
Run with --write after reading the sample.
"""
import json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path[:0] = [ROOT, os.path.dirname(os.path.abspath(__file__))]
import nasab

# --- step 1: repair what is a name with prose stuck to it -------------------
# 'his son al-Aswad' really is his son, so the edge is right and only the label is wrong.
SON = re.compile(r"^(?:ابنه|ابنته|ابنا)\s+")
# a clause boundary: everything after it comments on the name rather than continuing it
CLAUSE = re.compile(r"\s*(?:[،,؛:\.]|-\s*واسم|واسمه|وبه كان|</?span[^>]*>|\s+بن\s).*$")


def repair(name):
    """The name with its trailing commentary cut off, or None if nothing survives."""
    n = re.sub(r"</?span[^>]*>", " ", name)
    n = re.sub(r"\s+", " ", n).strip()
    n = SON.sub("", n)
    n = CLAUSE.sub("", n).strip(" ،؛.:-()[]«»")
    return n or None


# --- step 2: prune what was never a name -----------------------------------
# a verb, a relative clause, or a kinship pointer to someone who is NOT the child
JUNK = re.compile(
    r"قتل|تزوج|هاجر|سكن|يسمى|سميت|خلف علي|فولد|"
    r"^عمه|^عمة|^ابن عم|^أخت|^أخو|^بنو|^بني|^فهم|^أن |^أنت|^لعمر|"
    r"^الناس$|محدث|الفقيه|^بطن|ثقة|الترجمان|^أبو$|^أبا$|لا بقية|"   # not ^أبي$: that is Ubayy
    
    r"منا فأما|^فمن$|^اسمه|أحق به|^معهم$|^فقتله$|^هر$|^لغن$|^غضيا$|^الأغوز$|"
    r"زوجة|ابنا |بطن ضخم|^رسول الله$|\sبه\s|^أمة بنت")
# one character cannot be a name; two can - 'Udd' and 'Murr' are ancestors of Tamim
SHORT = re.compile(r"^.$")


def is_junk(name):
    """Does this "name" look like a clause the splitter cut in the wrong place?

    Two shapes: a phrase carrying a verb or a relationship word (JUNK), and something too
    short to be a name at all (SHORT). Both are judged on shape alone, because the Arabic is
    genuinely on the page and validate.py will happily pass it.
    """
    n = re.sub(r"\s+", " ", name).strip()
    return bool(JUNK.search(n)) or bool(SHORT.match(n))


def main(write=False):
    """Repair names first, then drop what was never a name.

    ORDER MATTERS, AND SO DOES THE ORDER AGAINST merge.py. Repair turns 'Umar ammuhu
    al-Shayba' into 'Umar', and a repair can turn two differently-named siblings into
    duplicates - which merge.py must then see. Run prune BEFORE merge; the other way round,
    Ali ends up with two sons called Umar.
    """
    people = [json.loads(l) for l in open(f"{ROOT}/people.jsonl", encoding="utf-8") if l.strip()]
    claims = [json.loads(l) for l in open(f"{ROOT}/claims.jsonl", encoding="utf-8") if l.strip()]
    by_id = {p["id"]: p for p in people}
    kids = {}
    for c in claims:
        if c["type"] == "father_of":
            kids.setdefault(c["subject"], []).append(c["object"])

    # repair first: a node that cleans up to a real name keeps its place and its children
    from translit import translit
    fixed = 0
    for p in people:
        r = repair(p["name_ar"])
        if r and r != p["name_ar"] and not is_junk(r):
            p["name_ar"] = r
            p["name_lat"], prov = translit(r)
            p.pop("translit_provisional", None)
            if prov:
                p["translit_provisional"] = True
            fixed += 1
    print(f"repaired {fixed} names")

    bad = {p["id"] for p in people if is_junk(p["name_ar"])}
    # a bad node takes its descendants: they were reached only through the misparse
    stack = list(bad)
    while stack:
        for k in kids.get(stack.pop(), ()):
            if k not in bad:
                bad.add(k)
                stack.append(k)
    bad.discard("p.muhammad")          # never prune a hand-seeded spine member
    seeded = {c["subject"] for c in claims if c.get("source_pattern") == "spine"} | \
             {c["object"] for c in claims if c.get("source_pattern") == "spine" and c.get("object")}
    protected = bad & seeded
    bad -= seeded

    print(f"pruning {len(bad)} of {len(people)} nodes"
          + (f" ({len(protected)} protected as hand-seeded)" if protected else ""))
    for pid in sorted(bad)[:25]:
        print(f"   {by_id[pid]['name_ar']}")
    if len(bad) > 25:
        print(f"   ... and {len(bad)-25} more")

    people = [p for p in people if p["id"] not in bad]
    claims = [c for c in claims
              if c["subject"] not in bad and (not c.get("object") or c["object"] not in bad)]
    if write:
        with open(f"{ROOT}/people.jsonl", "w", encoding="utf-8") as f:
            for p in people:
                f.write(json.dumps(p, ensure_ascii=False) + "\n")
        with open(f"{ROOT}/claims.jsonl", "w", encoding="utf-8") as f:
            for c in claims:
                f.write(json.dumps(c, ensure_ascii=False) + "\n")
        print(f"written: {len(people)} people, {len(claims)} claims")
    return bad


if __name__ == "__main__":
    main(write="--write" in sys.argv)
