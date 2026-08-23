#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
# Wasl - a verifiable nasab. Copyright (C) 2026 Hendra Saputra.
"""Re-derive vol/page/page_end for claims whose page was truncated.

nasab.PAGE_RE read only three digits of a page milestone, so al-Isti'ab - which paginates
1..1969 in one continuous sequence across its four volumes - had every page from 1000 up
recorded shorn of its last digit: 1819 stored as 181. The Arabic was always right and always
verified; it was the number a reader would use to check it that was wrong.

This is not a replay. No parser misread anything and no claim changes its meaning: vol, page
and page_end are DERIVED fields, and this recomputes them with the corrected index. Anything
that disagrees for another reason is reported and left alone.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import nasab

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    """Recompute vol/page/page_end for claims whose stored page was truncated.

    A one-off migration, kept as the record of the fix. It only touches rows where the stored
    page is a strict PREFIX of the true one, which is what the truncation looked like;
    anything disagreeing for another reason is reported and left alone.
    """
    path = os.path.join(ROOT, "claims.jsonl")
    claims = [json.loads(l) for l in open(path, encoding="utf-8") if l.strip()]
    fixed, odd = [], []
    for c in claims:
        span = nasab.locate(c["work"], c["ar"])
        if span is None:
            odd.append(f"{c['cid']}: quote not in {c['work']} at all")
            continue
        v, p1, p2 = span
        if (c["vol"], c["page"]) == (v, p1) and c.get("page_end", p2) == p2:
            continue
        # a truncated page is a strict prefix of the true one - anything else is not this bug
        if c["vol"] == v and str(p1).startswith(str(c["page"])):
            fixed.append((c["cid"], c["work"], c["vol"], c["page"], p1, p2))
            c["page"], c["page_end"] = p1, p2
        else:
            odd.append(f"{c['cid']}: cites {c['work']} {c['vol']}:{c['page']}, "
                       f"text at {v}:{p1}-{p2} - not a truncation, left alone")
    print(f"{len(fixed)} page numbers re-derived, {len(odd)} left alone")
    for cid, w, v, was, now, end in fixed[:6]:
        print(f"   {cid}  {w} {v}:{was} -> {v}:{now}" + (f"-{end}" if end != now else ""))
    if len(fixed) > 6:
        print(f"   ... and {len(fixed)-6} more")
    for o in odd[:10]:
        print("   !", o)
    if "--write" in sys.argv and fixed:
        with open(path, "w", encoding="utf-8") as f:
            for c in claims:
                f.write(json.dumps(c, ensure_ascii=False) + "\n")
        print("written claims.jsonl")
    return 0


if __name__ == "__main__":
    sys.exit(main())
