# -*- coding: utf-8 -*-
# SPDX-License-Identifier: GPL-3.0-or-later
# Wasl - a verifiable nasab. Copyright (C) 2026 Hendra Saputra.
"""Harvest kunyas from the companion dictionaries.

A reader looks for 'Abu Bakr', not for 'Abd Allah b. Uthman'. The sources give the kunya
explicitly - 'yukanna Aba Hafs', 'kunyatuhu Abu Ubayda' - roughly 2,200 times across the two
companion dictionaries and Ibn Sa'd. Each becomes a cited claim like any other, so searching a
kunya is searching evidence, not a guess.

The kunya is attributed to the person whose ENTRY it sits in: we resolve the entry's own chain
and attach the kunya to its head. An entry titled by kunya alone is handled too - its nasab is
in the first lines, so the chain resolves and the title becomes the kunya.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ingest, nasab, extract_entry
from extract_walad import BN, norm_name
from translit import translit

# 'yukanna Aba X' / 'kunyatuhu Abu X' / 'wa-kunyatuhu Umm X'
# 'Abu Abd Allah' is three words: take the second only after a construct head like 'Abd',
# otherwise the kunya truncates to a meaningless 'Abu Abd'
_K = r"(?:أب[اوي]|أم)\s+(?:عبد|أمة|ذي|ذو)\s+[ء-ي]{2,14}|(?:أب[اوي]|أم)\s+[ء-ي]{2,16}"
KUNYA = re.compile(r"(?:يكنى|كنيته|ويكنى|وكنيته|تكنى|كنيتها)\s+(" + _K + r")")
LEAD = re.compile(r"^\s*(" + _K + r")\b")


def canon(k):
    """Accusative and genitive forms of the kunya are the same kunya."""
    k = re.sub(r"\s+", " ", k).strip(" ،؛.:()[]«»")
    k = re.sub(r"^أب[اي]\b", "أبو", k)
    return k


def entries_with_body(work, text):
    """Heading plus the first lines of the entry. al-Isti'ab puts the chain in the heading and
    the kunya in the body, so reading only the heading finds almost nothing."""
    pat = extract_entry.ISTIAB if work == "IbnAbdAlBarr" else extract_entry.USD
    for m in pat.finditer(text):
        body = text[m.end():m.end() + 520].replace("\n", " ")
        body = re.sub(r"\(\s*[بدعس\s]+\s*\)", " ", body)
        # Usd repeats the name in its first body line, so heading+body would break the chain in
        # two; al-Isti'ab puts the chain only in the heading and needs it prepended
        yield (m.group(1).strip() + " " + body) if work == "IbnAbdAlBarr" else body


def run(work, store, quiet=True):
    raw = open(f"{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/corpus/{work}.txt",
               encoding="utf-8").read()
    text = "\n".join(l for l in raw.split("\n") if not l.startswith("#META#"))
    added = seen = unresolved = 0
    for ent in entries_with_body(work, text):
        seen += 1
        ent = re.sub(r"PageV\d{2}P\d{3}[AB]?|\bms\d+\b|[#~]+|\[\d+\]|%~%", " ", ent)
        ent = re.sub(r"\s+", " ", ent).strip()
        chain = extract_entry.chain_of(ent)
        if len(chain) < 3:
            continue
        # the person is already in the tree by now, so their own full chain identifies them
        pid = store.find_by_chain(chain)
        if pid is None:
            unresolved += 1
            continue
        found = {canon(m.group(1)) for m in KUNYA.finditer(ent)}
        lead = LEAD.match(ent)
        if lead:
            found.add(canon(lead.group(1)))
        already = {c.get("value_ar") for c in store.claims
                   if c["type"] == "kunya" and c["subject"] == pid}
        for k in sorted(found):
            if k in already:
                continue
            already.add(k)
            # quote the sentence that states it, so the claim carries its own evidence
            stem = re.escape(k)[:-0] if not k.startswith("أبو") else \
                   r"أب[اوي]" + re.escape(k[3:])
            m = re.search(r"[^.]{0,80}(?:يكنى|كنيته|ويكنى|وكنيته|تكنى|كنيتها)\s+" + stem, ent)
            q = m.group(0).strip() if m else None
            if not q or nasab.locate(work, q) is None:
                q = k if nasab.locate(work, k) else None
            if not q:
                continue
            if store.add("kunya", pid, q, f"is given the kunya {translit(k)[0]}",
                         work=work, value_ar=k, value_lat=translit(k)[0],
                         source_pattern="kunya"):
                added += 1
                if not quiet:
                    print(f"  {store.people[pid]['name_lat']:26} = {translit(k)[0]}")
    print(f"{work}: {seen} entries, {added} kunyas, {unresolved} entries unresolved")
    return added


if __name__ == "__main__":
    st = ingest.Store()
    for w in (["IbnAbdAlBarr", "IbnAlAthir"] if len(sys.argv) < 2 or sys.argv[1].startswith("-")
              else [sys.argv[1]]):
        run(w, st, quiet="-v" not in sys.argv)
    st.report("kunya pass")
    if "--write" in sys.argv:
        st.save()
        print("written")
