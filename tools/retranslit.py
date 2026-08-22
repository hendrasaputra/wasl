# -*- coding: utf-8 -*-
"""Re-read every person's Latin form against the current dictionary, in place.

Ids are never touched: they are referenced by thousands of claims, and a name is a label, not
an identity. Run after adding readings to translit.py.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from translit import translit

rows = [json.loads(l) for l in open(f"{ROOT}/people.jsonl", encoding="utf-8") if l.strip()]
before = sum(1 for r in rows if r.get("translit_provisional"))
changed = 0
for r in rows:
    lat, prov = translit(r["name_ar"])
    if lat != r["name_lat"] or bool(prov) != bool(r.get("translit_provisional")):
        changed += 1
    r["name_lat"] = lat
    r["translit_provisional"] = True if prov else None
    if r["translit_provisional"] is None:
        del r["translit_provisional"]
after = sum(1 for r in rows if r.get("translit_provisional"))
if "--write" in sys.argv:
    with open(f"{ROOT}/people.jsonl", "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
print(f"provisional {before} -> {after}  ({changed} rows updated)")
