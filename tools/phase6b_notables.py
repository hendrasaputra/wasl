# -*- coding: utf-8 -*-
# SPDX-License-Identifier: GPL-3.0-or-later
# Wasl - a verifiable nasab. Copyright (C) 2026 Hendra Saputra.
"""Seed the companions a reader will actually look for.

The generic parser reaches a companion only when his entry opens with a plain 'X b. Y b. Z'.
The most famous ones are exactly the ones it misses, because they are introduced by kunya or
by title - 'Abu Bakr al-Siddiq', 'Sa'd b. Abi Waqqas' - and a kunya is not a chain. So the
marquee names are seeded from a chain that is quoted verbatim from the corpus, the same way
Phase 1 and Phase 3 were.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ingest, nasab
from extract_walad import BN, norm_name
from translit import translit

# (chain as it stands in the text, work, note for the leaf)
NOTABLES = [
 ("عبد الله بن عثمان بن عامر بن عمرو بن كعب بن سعد بن تيم بن مرة", "IbnAlAthir", "Abū Bakr al-Ṣiddīq, first caliph"),
 ("عثمان بن عفان بن أبي العاص بن أمية بن عبد شمس", "IbnAbdAlBarr", "third caliph"),
 ("عبد الرحمن بن عوف بن عبد عوف بن عبد بن الحارث بن زهرة", "IbnAbdAlBarr", "of the ten"),
 ("سعيد بن زيد بن عمرو بن نفيل", "IbnAbdAlBarr", "of the ten"),
 ("عامر بن عبد الله بن الجراح بن هلال بن أهيب بن ضبة بن الحارث ابن فهر بن مالك", "IbnAbdAlBarr",
  "Abū ʿUbayda b. al-Jarrāḥ, of the ten"),
 ("مالك بن أهيب بن عبد مناف بن زهرة", "IbnAlAthir", "Abū Waqqāṣ, father of Saʿd"),
 ("خالد بن الوليد بن المغيرة", "IbnAbdAlBarr", "Sayf Allāh"),
 ("معاذ بن جبل بن عمرو بن أوس", "IbnAbdAlBarr", None),
 ("زيد بن ثابت بن الضحاك بن زيد", "IbnAbdAlBarr", None),
 ("أبي بن كعب بن قيس بن عبيد بن زيد بن معاوية", "IbnAbdAlBarr", None),
 ("عبادة بن الصامت بن قيس", "IbnAbdAlBarr", None),
 ("أسيد بن حضير بن سماك", "IbnAbdAlBarr", None),
 ("سعد بن معاذ بن النعمان بن امرئ القيس بن زيد بن عبد الأشهل", "IbnAbdAlBarr", "chief of al-Aws"),
]


def attach(st, chain_s, work, note=None, quiet=False):
    """Hang a quoted chain onto the deepest ancestor already in the tree."""
    names = [norm_name(x) for x in BN.split(chain_s) if norm_name(x)]
    if nasab.locate(work, chain_s) is None:
        print(f"  ! not in {work}: {chain_s[:40]}")
        return 0
    anchor = idx = None
    for k in range(len(names) - 1, 0, -1):
        hit = st.find_by_chain(names[k:])
        if hit:
            anchor, idx = hit, k
            break
    if anchor is None:
        print(f"  ! no anchor for {chain_s[:50]}")
        return 0
    cur, made = anchor, 0
    for i in range(idx - 1, -1, -1):
        pair = f"{names[i]} بن {names[i+1]}"
        q = pair if nasab.locate(work, pair) else chain_s
        kid = st.person(names[i], father=cur,
                        sahabi=True if i == 0 else None,
                        note=note if (i == 0 and note) else None)
        if st.add("father_of", cur, q,
                  f"{translit(names[i])[0]} son of {translit(names[i+1])[0]}",
                  object=kid, work=work, source_pattern="notable"):
            made += 1
        cur = kid
    if not quiet:
        print(f"  {'+' if made else '='} {' b. '.join(translit(n)[0] for n in names[:idx+1])}")
    return made


if __name__ == "__main__":
    st = ingest.Store()
    p0 = len(st.people)
    for ch, w, note in NOTABLES:
        attach(st, ch, w, note)
    print(f"\nnew: {len(st.people)-p0} people, {len(st.claims)} claims total")
    if "--write" in sys.argv:
        st.save()
        print("written")
