# -*- coding: utf-8 -*-
"""Phase 6 - the companions that could not anchor before.

Three things had been blocking them, all now fixed upstream:
  * a blunt anchor gate of four names, which meant a four-name chain could never anchor at all;
  * duplicate branches from one-letter spelling variants, which made every chain through them
    ambiguous - one 'Rawah/Rizah' cost the whole line of Umar b. al-Khattab;
  * the Ansar trunk being absent, so most Sahaba had nothing to hang from.

So this is not a new parser, it is the old one finally able to reach. Alternates walada passes
(which widen the Ansar clans) with entry passes (which hang companions off them) until neither
finds anything new.
"""
import os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ingest, extract_walad, extract_entry

WALAD = ["IbnHazm", "IbnKalbi", "Baladhuri", "IbnSad", "IbnHisham"]
ENTRY = ["IbnAbdAlBarr", "IbnAlAthir"]
TRUNKS = ["p.qahtan", "p.adnan"]

if __name__ == "__main__":
    st = ingest.Store()
    p0, c0 = len(st.people), len(st.claims)
    t = time.time()
    for rnd in range(1, 10):
        w = sum(extract_walad.run(x, st, quiet=True, under=tr) for tr in TRUNKS for x in WALAD)
        e = sum(extract_entry.run(x, st) for x in ENTRY)
        print(f"== round {rnd}: +{w} walada, {e} entries | {len(st.people)} people  [{time.time()-t:.0f}s]")
        if not (w or e):
            break
    st.report("phase 6")
    print(f"new: {len(st.people)-p0} people, {len(st.claims)-c0} claims")
    if "--write" in sys.argv:
        st.save()
        print("written")
