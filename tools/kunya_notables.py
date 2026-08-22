# -*- coding: utf-8 -*-
# SPDX-License-Identifier: GPL-3.0-or-later
# Wasl - a verifiable nasab. Copyright (C) 2026 Hendra Saputra.
"""Give the people in the directory the kunya the sources give them.

Not by supplying the kunya and looking for it - that would be deciding the answer first. We
locate the man by his own chain, then read whatever kunya the text states within the next few
hundred characters, so the quote names him and the reading comes from the page.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ingest, nasab
from extract_kunya import KUNYA, canon
from translit import translit

WORKS = ["IbnAbdAlBarr", "IbnAlAthir", "IbnSad"]


def chain_of(store, pid, n=4):
    out, c = [], pid
    while c and len(out) < n:
        out.append(store.people[c]["name_ar"])
        c = next((x["subject"] for x in store.claims
                  if x["type"] == "father_of" and x.get("object") == c), None)
    return out


def find_kunya(store, pid, quiet=False):
    names = chain_of(store, pid)
    if len(names) < 2:
        return 0
    added = 0
    for work in WORKS:
        txt = nasab.clean(work)
        for depth in (4, 3):
            # the chain is often broken by an honorific - 'Umar b. al-Khattab, radiya Allahu
            # anhu, ibn Nufayl' - so allow a short interjection between the links
            probe = r"(?:\s+|\s*[^.]{0,45}?\s+)ا?بن\s+".join(
                re.escape(n) for n in names[:depth])
            for m in re.finditer(probe, txt):
                # the probe must BEGIN a chain. 'Fihr b. Malik' occurs inside a hundred longer
                # chains, and reading the kunya that follows one of those gives Fihr the kunya
                # of whoever the entry was really about.
                before = txt[max(0, m.start() - 6):m.start()]
                if re.search(r"(?:^|\s)ا?بن\s$", before):
                    continue
                win = txt[m.start():m.start() + 340]
                # and the kunya must belong to this man, not to someone named further along
                head = win[:win.find("يكنى") if "يكنى" in win else len(win)]
                if head.count(" بن ") > len(names) + 4:
                    continue
                k = KUNYA.search(win)
                if not k:
                    continue
                quote = win[:k.end()]
                if len(quote) > 300 or nasab.locate(work, quote) is None:
                    continue
                val = canon(k.group(1))
                if store.add("kunya", pid, quote,
                             f"{store.people[pid]['name_lat']} is given the kunya {translit(val)[0]}",
                             work=work, value_ar=val, value_lat=translit(val)[0],
                             source_pattern="kunya-notable"):
                    added += 1
                    if not quiet:
                        print(f"  {store.people[pid]['name_lat']:24} = {translit(val)[0]:22} {work} {quote[-46:]!r}"[:150])
                break
            if added:
                break
        if added:
            break
    return added


if __name__ == "__main__":
    st = ingest.Store()
    import json
    # everyone the directory names, plus every companion the parser flagged. The directory
    # must be included explicitly: Umar was attached as a middle rung of his son's chain, so
    # nothing ever marked him a companion, and he would have been skipped.
    from directory import DIRECTORY
    ids = []
    for _, rows in DIRECTORY:
        for _, chain in rows:
            hit = st.find_by_chain(chain) if chain[-1] != "__root__" else None
            if hit:
                ids.append(hit)
                st.people[hit].setdefault("sahabi", None)
    ids += [pid for pid, p in st.people.items() if p.get("sahabi") or p.get("note")]
    ids = list(dict.fromkeys(ids))
    print(f"probing {len(ids)} people")
    tot = sum(find_kunya(st, p, quiet="-v" not in sys.argv) for p in ids)
    print(f"{tot} kunyas added")
    st.report("kunya notables")
    if "--write" in sys.argv:
        st.save()
        print("written")
