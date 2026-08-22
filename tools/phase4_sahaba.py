# -*- coding: utf-8 -*-
# SPDX-License-Identifier: GPL-3.0-or-later
# Wasl - a verifiable nasab. Copyright (C) 2026 Hendra Saputra.
"""Phase 4 - the Sahaba, from the two dedicated companion dictionaries.

Each entry opens with a nasab chain, so the work is to attach that chain to the deepest
ancestor the tree already holds. Repeated until nothing new attaches: each round puts more
rungs in place, which lets the next round reach entries it could not anchor before.
"""
import os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ingest, extract_entry, extract_walad

WORKS = ["IbnAbdAlBarr", "IbnAlAthir"]

if __name__ == "__main__":
    st = ingest.Store()
    p0, c0 = len(st.people), len(st.claims)
    t = time.time()
    for rnd in range(1, 7):
        n = sum(extract_entry.run(w, st) for w in WORKS)
        print(f"== round {rnd}: {n} entries attached | {len(st.people)} people, "
              f"{len(st.claims)} claims  [{time.time()-t:.0f}s]")
        if not n:
            break
    st.report("phase 4")
    print(f"new: {len(st.people)-p0} people, {len(st.claims)-c0} claims")
    if "--write" in sys.argv:
        st.save()
        print("written")
