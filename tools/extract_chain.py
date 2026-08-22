"""Propose person + father_of rows from a nasab chain in the corpus.

Not a source of truth: it drafts JSONL that a human reviews and validate.py proves.
Usage: python3 tools/extract_chain.py WORK VOL PAGE "<exact arabic chain substring>"
"""
import json, re, sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import nasab

SEP = re.compile(r"\s*\b(?:ابن|بن|بنت)\s+")
ALIAS = re.compile(r"واسم\s+(.+?)\s*[:،]\s*(.+)")


def main(work, vol, page, chain):
    hit = nasab.quote_on_page(work, vol, page, chain)
    if hit is None:
        sys.exit(f"FAIL: chain not found on {work} {vol}:{page}")
    print(f"# verified on {work} v{vol} p{hit}", file=sys.stderr)
    parts = [p.strip(" ،.()") for p in SEP.split(chain) if p.strip(" ،.()")]
    rows = []
    for i, p in enumerate(parts):
        m = ALIAS.search(p)
        name, alias = (m.group(2).strip(), m.group(1).strip()) if m else (p, None)
        rows.append({"seq": i, "name_ar": name, "alias_ar": alias, "raw": p})
    for i, r in enumerate(rows):
        r["father_ar"] = rows[i + 1]["name_ar"] if i + 1 < len(rows) else None
        print(json.dumps(r, ensure_ascii=False))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
