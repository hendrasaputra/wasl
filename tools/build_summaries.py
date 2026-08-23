#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
# Wasl - a verifiable nasab. Copyright (C) 2026 Hendra Saputra.
"""Check the hand-written summaries against their entries and write summaries.jsonl."""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, ROOT)
import nasab
from summaries import SUMMARIES

MIN_ANCHOR = 25      # normalised characters
MAX_WORDS = 400
MAX_LINES = 30
MAX_EDITORIAL = 0.20


def main():
    entries = {}
    for l in open(f"{ROOT}/entries.jsonl", encoding="utf-8"):
        if l.strip():
            e = json.loads(l)
            entries[(e["who"], e["work"])] = e
    rows, err = [], []
    for who, (work, lines) in SUMMARIES.items():
        e = entries.get((who, work))
        if not e:
            err.append(f"{who}: no pinned entry in {work}")
            continue
        out, edit = [], 0
        for en, ar in lines:
            if ar is None:
                edit += 1
                if any(c.isdigit() for c in en):
                    err.append(f"{who}: editorial line carries a number - {en[:60]}")
                out.append({"en": en, "basis": "editorial"})
                continue
            if len(nasab.normalise(ar)) < MIN_ANCHOR:
                err.append(f"{who}: anchor too short to identify a passage - {ar[:40]}")
                continue
            span = nasab.locate(work, ar)
            if span is None:
                err.append(f"{who}: anchor NOT in {work} - {ar[:50]}")
                continue
            v, p1, p2 = span
            # the anchor must sit inside the entry this summary claims to read. locate() finds
            # the FIRST occurrence in the work, so a phrase common enough to appear earlier
            # fails here - which is the point: it was not distinctive enough to cite.
            if v != e["vol"] or not (e["page"] <= p1 and p2 <= e["page_end"]):
                err.append(f"{who}: anchor at {v}:{p1}-{p2}, outside the entry "
                           f"({e['vol']}:{e['page']}-{e['page_end']}) - {ar[:44]}")
                continue
            out.append({"en": en, "ar": ar, "basis": "anchored",
                        "vol": v, "page": p1, "page_end": p2})
        words = sum(len(l["en"].split()) for l in out)
        if words > MAX_WORDS:
            err.append(f"{who}: {words} words, cap is {MAX_WORDS}")
        if len(out) > MAX_LINES:
            err.append(f"{who}: {len(out)} lines, cap is {MAX_LINES}")
        if out and edit / len(out) > MAX_EDITORIAL:
            err.append(f"{who}: {edit}/{len(out)} lines editorial, cap is "
                       f"{int(MAX_EDITORIAL*100)}%")
        rows.append({"who": who, "work": work, "eid": e["eid"],
                     "n_words": words, "n_editorial": edit, "lines": out})
        print(f"  {who:26} {len(out):>2} lines  {words:>3} words  {edit} editorial")
    if err:
        print(f"\nFAIL - {len(err)} problem(s):", file=sys.stderr)
        for x in err:
            print("  x", x, file=sys.stderr)
        return 1
    print(f"\n{len(rows)} summaries, {sum(r['n_words'] for r in rows)} words, "
          f"{sum(len(r['lines']) for r in rows)} lines")
    if "--write" in sys.argv:
        with open(f"{ROOT}/summaries.jsonl", "w", encoding="utf-8") as f:
            for r in rows:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        print("written summaries.jsonl")
    return 0


if __name__ == "__main__":
    sys.exit(main())
