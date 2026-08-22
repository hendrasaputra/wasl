# -*- coding: utf-8 -*-
# SPDX-License-Identifier: GPL-3.0-or-later
# Wasl - a verifiable nasab. Copyright (C) 2026 Hendra Saputra.
"""Phase 2 - Quraysh: everything the books hang under Fihr b. Malik.

Runs the walada parser over every work, scoped to descendants of Fihr, until no new edge
appears. Scoping to Fihr is not arbitrary: Ibn Hazm states the boundary outright - no one above
Fihr is called Qurashi, and no descendant of Fihr is anything else.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ingest, extract_walad

WORKS = ["IbnHazm", "IbnKalbi", "Baladhuri", "IbnSad", "IbnHisham", "IbnAbdAlBarr", "IbnAlAthir"]

if __name__ == "__main__":
    st = ingest.Store()
    p0, c0 = len(st.people), len(st.claims)
    for rnd in range(1, 7):
        total = 0
        for w in WORKS:
            total += extract_walad.run(w, st, quiet=True, under="p.fihr")
        print(f"== round {rnd}: +{total} edges | {len(st.people)} people, {len(st.claims)} claims")
        if not total:
            break
    st.report("phase 2")
    print(f"new: {len(st.people)-p0} people, {len(st.claims)-c0} claims")
    if "--write" in sys.argv:
        st.save()
        print("written")
