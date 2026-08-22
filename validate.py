#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
# Wasl - a verifiable nasab. Copyright (C) 2026 Hendra Saputra.
"""Prove the dataset against the primary texts. Must pass before every commit.

The load-bearing check is #4: every Arabic quote is re-read out of the pinned corpus file at
the page the claim cites. A claim whose quote is not there is not a citation, it is a guess.
"""
import json, os, sys, collections
import nasab

ROOT = os.path.dirname(os.path.abspath(__file__))
REQUIRED = ("cid", "type", "subject", "work", "vol", "page", "ar", "en")
EDGE = ("father_of", "mother_of")
DATE_BASIS = {"attested", "attested_relative", "derived_from_age_at_death",
              "generation_estimate", "unknown"}


def jsonl(name):
    with open(os.path.join(ROOT, name), encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


def main():
    people = {p["id"]: p for p in jsonl("people.jsonl")}
    claims = jsonl("claims.jsonl")
    works = nasab.sources()
    err, warn = [], []
    E = err.append

    # 1. people well-formed and unique
    if len(people) != len(jsonl("people.jsonl")):
        E("duplicate person id")
    for pid, p in people.items():
        if not pid.startswith("p."):
            E(f"{pid}: id must start with 'p.'")
        for f in ("name_ar", "name_lat", "sex"):
            if not p.get(f):
                E(f"{pid}: missing {f}")
        if p.get("sex") not in ("M", "F"):
            E(f"{pid}: sex must be M or F")

    # 2. claims well-formed, ids unique, references resolve, work is declared
    seen = set()
    for c in claims:
        cid = c.get("cid", "?")
        for f in REQUIRED:
            if c.get(f) in (None, ""):
                E(f"{cid}: missing {f}")
        if cid in seen:
            E(f"{cid}: duplicate claim id")
        seen.add(cid)
        for f in ("subject", "object"):
            if c.get(f) and c[f] not in people:
                E(f"{cid}: {f} '{c[f]}' is not in people.jsonl")
        if c.get("work") not in works:
            E(f"{cid}: work '{c.get('work')}' is not in sources.tsv")
        if c.get("date_basis") and c["date_basis"] not in DATE_BASIS:
            E(f"{cid}: date_basis '{c['date_basis']}' not one of {sorted(DATE_BASIS)}")
        if c["type"] in EDGE and not c.get("object"):
            E(f"{cid}: {c['type']} needs both subject (parent) and object (child)")

    # 3. every person carries at least one name, every edge at least one citation
    named = {c["subject"] for c in claims} | {c["object"] for c in claims if c.get("object")}
    for pid in people:
        if pid not in named:
            E(f"{pid}: no claim mentions this person")
    edges = collections.defaultdict(list)
    for c in claims:
        if c["type"] in EDGE:
            edges[(c["subject"], c["object"], c["type"])].append(c)

    # 4. THE check - every quote is really on the cited page of the pinned text
    checked = 0
    for c in claims:
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

    # 5. the parent graph is a forest - no cycles, no two fathers for one child
    father = {}
    for (par, chi, typ), cs in edges.items():
        if typ == "father_of":
            father.setdefault(chi, set()).add(par)
    for chi, pars in father.items():
        if len(pars) > 1:
            E(f"{chi}: two different fathers claimed - {sorted(pars)} (model as variant_chain)")
    for start in father:
        node, hops = start, 0
        while node in father and hops <= len(people):
            node = next(iter(father[node]))
            hops += 1
        if hops > len(people):
            E(f"cycle in the parent graph at {start}")

    # 6. advisory: single-source edges (true, but not yet corroborated)
    for (par, chi, typ), cs in sorted(edges.items()):
        if len({c["work"] for c in cs}) == 1:
            warn.append(f"{chi} <- {par}: attested by {cs[0]['work']} only")

    print(f"people   {len(people)}")
    print(f"claims   {len(claims)}  ({checked} quotes re-read from corpus)")
    print(f"edges    {len(edges)}   works cited: {len({c['work'] for c in claims})}")
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
