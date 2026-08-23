#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
# Wasl - a verifiable nasab. Copyright (C) 2026 Hendra Saputra.
"""Prove the dataset against the primary texts. Must pass before every commit.

The load-bearing check is #4: every Arabic quote is re-read out of the pinned corpus file at
the page the claim cites. A claim whose quote is not there is not a citation, it is a guess.

WHAT THIS PROVES AND WHAT IT DOES NOT. It proves the QUOTE: the Arabic really is on the page
named. It cannot prove the PLACEMENT - that the man a parser anchored a chain to is the man
the text meant. Parser-placed claims carry `source_pattern` and are badged `auto` in the page
for exactly that reason. Never describe an `auto` node as verified without the distinction.

This file shares nasab.py with the extraction code, so it can agree with its own bug. That is
not hypothetical: it is how the repeated-page-marker bug in Ibn Sa'd survived, and how a page
milestone truncated to three digits put 286 claims on the wrong page while every quote still
"verified". test_wasl.py exists to disagree - it re-derives page boundaries from the raw file
with plain string operations and shares no code with the indexer. Run both.

Exit code 0 means every check passed. Anything else is a failure and the commit must not
happen.
"""
import json, os, sys, collections
import nasab

ROOT = os.path.dirname(os.path.abspath(__file__))
REQUIRED = ("cid", "type", "subject", "work", "vol", "page", "ar", "en")
EDGE = ("father_of", "mother_of")
CLAIM_TYPES = {"age_at_death", "alias", "birth", "chain", "dissent", "father_of",
               "isnad", "kunya", "married_to", "mother_of", "variant_chain"}
DATE_BASIS = {"attested", "attested_relative", "derived_from_age_at_death",
              "generation_estimate", "unknown"}


def jsonl(name, errors=None):
    """Read JSON objects without letting one malformed row hide later validation errors."""
    rows = []
    with open(os.path.join(ROOT, name), encoding="utf-8") as f:
        for line_no, line in enumerate(f, 1):
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError as e:
                msg = f"{name}:{line_no}: invalid JSON: {e.msg}"
                if errors is None:
                    raise ValueError(msg) from e
                errors.append(msg)
                continue
            if not isinstance(row, dict):
                msg = f"{name}:{line_no}: row must be a JSON object"
                if errors is None:
                    raise ValueError(msg)
                errors.append(msg)
                continue
            rows.append(row)
    return rows


def main():
    """Run every check, print a summary, and exit non-zero if anything failed.

    The checks are numbered in the order they run, and each is cheap enough that all of them
    run every time - nothing is sampled. Errors are collected rather than raised so one bad
    row does not hide the next fifty.
    """
    err, warn = [], []
    E = err.append               # errors fail the run; warnings are printed and tolerated
    people_rows = jsonl("people.jsonl", err)
    claims = jsonl("claims.jsonl", err)
    works = nasab.sources()
    people = {}

    # 1. people well-formed and unique
    for row_no, p in enumerate(people_rows, 1):
        pid = p.get("id")
        if not isinstance(pid, str) or not pid:
            E(f"people.jsonl row {row_no}: missing id")
            continue
        if pid in people:
            E(f"{pid}: duplicate person id")
            continue
        people[pid] = p
        if not pid.startswith("p."):
            E(f"{pid}: id must start with 'p.'")
        for f in ("name_ar", "name_lat", "sex"):
            if not isinstance(p.get(f), str) or not p[f]:
                E(f"{pid}: missing {f}")
        if p.get("sex") not in ("M", "F"):
            E(f"{pid}: sex must be M or F")

    # 2. claims well-formed, ids unique, references resolve, work is declared
    seen, usable = set(), []
    for row_no, c in enumerate(claims, 1):
        cid = c.get("cid")
        if not isinstance(cid, str) or not cid:
            E(f"claims.jsonl row {row_no}: cid must be a string")
            cid = f"row {row_no}"
        typ, subject, obj, work = (c.get(k) for k in ("type", "subject", "object", "work"))
        for f in REQUIRED:
            if c.get(f) in (None, ""):
                E(f"{cid}: missing {f}")
        if cid in seen:
            E(f"{cid}: duplicate claim id")
        seen.add(cid)
        if not isinstance(typ, str) or typ not in CLAIM_TYPES:
            E(f"{cid}: unknown claim type '{typ}'")
        for f, value in (("subject", subject), ("object", obj)):
            if value and (not isinstance(value, str) or value not in people):
                E(f"{cid}: {f} '{value}' is not in people.jsonl")
        if not isinstance(work, str) or work not in works:
            E(f"{cid}: work '{work}' is not in sources.tsv")
        basis = c.get("date_basis")
        if basis and (not isinstance(basis, str) or basis not in DATE_BASIS):
            E(f"{cid}: date_basis '{basis}' not one of {sorted(DATE_BASIS)}")
        if typ in {"birth", "age_at_death"} and not basis:
            E(f"{cid}: {typ} needs date_basis")
        if typ in {*EDGE, "married_to"} and not obj:
            E(f"{cid}: {typ} needs both subject and object")
        if not all(c.get(f) not in (None, "") for f in REQUIRED):
            continue
        if (not isinstance(typ, str) or typ not in CLAIM_TYPES
                or not isinstance(work, str) or work not in works
                or not isinstance(subject, str) or subject not in people
                or (obj and (not isinstance(obj, str) or obj not in people))):
            continue
        if not isinstance(c["ar"], str) or not isinstance(c["en"], str):
            E(f"{cid}: ar and en must be strings")
            continue
        if not all(isinstance(c.get(f), int) and c[f] > 0 for f in ("vol", "page")):
            E(f"{cid}: vol and page must be positive integers")
            continue
        page_end = c.get("page_end", c["page"])
        if not isinstance(page_end, int) or page_end < c["page"]:
            E(f"{cid}: page_end must be an integer at or after page")
            continue
        if typ in {*EDGE, "married_to"} and not obj:
            continue
        usable.append(c)

    # 3. every person carries at least one name, every edge at least one citation
    named = {c["subject"] for c in usable} | {c["object"] for c in usable if c.get("object")}
    for pid in people:
        if pid not in named:
            E(f"{pid}: no claim mentions this person")
    edges = collections.defaultdict(list)
    for c in usable:
        if c["type"] in EDGE:
            edges[(c["subject"], c["object"], c["type"])].append(c)

    # 4. THE check - every quote is really on the cited page of the pinned text.
    #    locate() returns the page SPAN a quote covers, because quotes routinely straddle a
    #    page break; a citation is valid when the page it names falls inside that span.
    checked = 0
    for c in usable:
        try:
            span = nasab.locate(c["work"], c["ar"])
        except FileNotFoundError as e:
            E(str(e))
            break
        if span is None:
            E(f"{c['cid']}: quote NOT FOUND in {c['work']} - {c['ar'][:50]}")
            continue
        v, p1, p2 = span
        if c["vol"] != v or not (p1 <= c["page"] <= p2):
            E(f"{c['cid']}: cites {c['work']} {c['vol']}:{c['page']} but text is at {v}:{p1}-{p2}")
        checked += 1

    # 5. the parent graph is a forest - no cycles, no two fathers for one child. Two fathers
    #    is nearly always a merge that should have happened or a chain that anchored wrongly;
    #    where the sources genuinely disagree, model it as a variant_chain claim instead.
    father, mother = {}, {}
    for (par, chi, typ), cs in edges.items():
        if typ == "father_of":
            father.setdefault(chi, set()).add(par)
        elif typ == "mother_of":
            mother.setdefault(chi, set()).add(par)
    for chi, pars in father.items():
        if len(pars) > 1:
            E(f"{chi}: two different fathers claimed - {sorted(pars)} (model as variant_chain)")
    for chi, pars in mother.items():
        if len(pars) > 1:
            E(f"{chi}: two different mothers claimed - {sorted(pars)}")
    parents = collections.defaultdict(set)
    for child, pars in list(father.items()) + list(mother.items()):
        parents[child].update(pars)
    visiting, done = set(), set()

    def visit(node):
        if node in visiting:
            return True
        if node in done:
            return False
        visiting.add(node)
        cycle = any(visit(parent) for parent in parents.get(node, ()))
        visiting.remove(node)
        done.add(node)
        return cycle

    for start in list(parents):
        if visit(start):
            E(f"cycle in the parent graph at {start}")
            break

    # 6. advisory only, and never a failure: an edge only one book carries is still an edge.
    #    The count is printed so the shape of the corroboration is visible at a glance.
    for (par, chi, typ), cs in sorted(edges.items()):
        if len({c["work"] for c in cs}) == 1:
            warn.append(f"{chi} <- {par}: attested by {cs[0]['work']} only")

    # 7. the summaries. Every anchored sentence must point at text that really is inside the
    # entry it claims to read. This does not prove the English is a fair rendering - that is
    # a human judgement - but it does prove nothing was written about a passage that is not
    # there, which is the failure a fluent draft would otherwise slip past.
    spath = os.path.join(ROOT, "summaries.jsonl")
    n_anchor = n_edit = 0
    if os.path.exists(spath):
        ent = {}
        for e in jsonl("entries.jsonl"):        # several entries per work is normal
            ent.setdefault((e["who"], e["work"]), []).append(e)
        for srow in jsonl("summaries.jsonl"):
            es = ent.get((srow["who"], srow["work"]))
            if not es:
                E(f"summary {srow['who']}: no pinned entry in {srow['work']}")
                continue
            for i, line in enumerate(srow["lines"]):
                if line["basis"] == "editorial":
                    n_edit += 1
                    continue
                span = nasab.locate(srow["work"], line["ar"])
                if span is None:
                    E(f"summary {srow['who']} line {i}: anchor NOT in {srow['work']}")
                    continue
                v, p1, p2 = span
                if not any(v == x["vol"] and x["page"] <= p1 and p2 <= x["page_end"]
                           for x in es):
                    E(f"summary {srow['who']} line {i}: anchor at {v}:{p1}-{p2} is outside "
                      + " or ".join(f"{x['vol']}:{x['page']}-{x['page_end']}" for x in es))
                    continue
                n_anchor += 1

    print(f"people   {len(people)}")
    print(f"claims   {len(claims)}  ({checked} quotes re-read from corpus)")
    print(f"edges    {len(edges)}   works cited: {len({c['work'] for c in usable})}")
    if n_anchor or n_edit:
        print(f"summary  {n_anchor} anchored sentences re-read from the entries they read"
              f", {n_edit} editorial")
    corr = collections.Counter(len({c['work'] for c in cs}) for cs in edges.values())
    print("corrob.  " + "  ".join(f"{n} work(s): {k} edges" for n, k in sorted(corr.items())))
    if warn:
        print(f"\n{len(warn)} single-source edge(s):")
        for w in warn[:8]:
            print("  -", w)
        if len(warn) > 8:
            print(f"  ... and {len(warn)-8} more")
    if err:
        print(f"\nFAIL - {len(err)} error(s):", file=sys.stderr)
        for e in err[:40]:
            print("  x", e, file=sys.stderr)
        sys.exit(1)
    print("\nOK - every quote verified against the pinned primary texts.")


if __name__ == "__main__":
    main()
