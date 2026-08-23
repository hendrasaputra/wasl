#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
# Wasl - a verifiable nasab. Copyright (C) 2026 Hendra Saputra.
"""Resolve the pinned biographical entries into entries.jsonl.

Keyed by the Who's who label, not by person id: build.py already resolves each label to a
person, and duplicating that resolution here would let the two drift. The row records where
the entry IS - work, heading, volume, page span, length. It records nothing about what the
entry SAYS; that is Phase 8c.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import nasab, entries
from directory import DIRECTORY

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Eponyms, not men with a life. Recorded here so 'no entry' is a stated finding rather than
# an absence nobody noticed.
NO_ENTRY = {
 "Qaḥṭān":     "an eponym: the books trace lines to him, none tells his life",
 "al-Aws":     "a tribe, not a person",
 "al-Khazraj": "a tribe, not a person",
}


def main():
    labels = [l for _, items in DIRECTORY for l, _ in items]
    missing = [l for l in labels if l not in entries.PINS and l not in NO_ENTRY]
    extra = [k for k in entries.PINS if k not in labels]
    if missing or extra:
        print(f"FAIL - pins and directory disagree: missing {missing}, extra {extra}",
              file=sys.stderr)
        return 1

    rows, n, bad = [], 0, []
    for who in labels:
        if who in NO_ENTRY:
            continue
        for work, pin in entries.PINS[who]:
            hit, count = entries.find(work, pin)
            if not hit:
                bad.append(f"{who} / {work} / {pin}: "
                           + ("no heading matches" if not count else f"{count} headings match"))
                continue
            line_no, depth, heading = hit
            raw = entries.body(work, line_no, depth)
            vol, page, page_end = entries.page_span(work, line_no, depth)
            n += 1
            rows.append({"eid": f"e{n:03d}", "who": who, "work": work, "pin": pin,
                         "heading_ar": heading, "vol": vol, "page": page,
                         "page_end": page_end, "n_words": entries.words(raw)})
    if bad:
        print("FAIL - unresolved pins:", file=sys.stderr)
        for b in bad:
            print("  x", b, file=sys.stderr)
        return 1

    per = {}
    for r in rows:
        per.setdefault(r["who"], []).append(r)
    print(f"{len(rows)} entries for {len(per)} people, "
          f"{sum(r['n_words'] for r in rows):,} words")
    print(f"no entry by design: {', '.join(sorted(NO_ENTRY))}")
    thin = sorted((sum(x['n_words'] for x in v), k) for k, v in per.items())[:5]
    print("thinnest: " + "; ".join(f"{k} {w}w" for w, k in thin))
    if "--write" in sys.argv:
        with open(os.path.join(ROOT, "entries.jsonl"), "w", encoding="utf-8") as f:
            for r in rows:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        print("written entries.jsonl")
    return 0


if __name__ == "__main__":
    sys.exit(main())
