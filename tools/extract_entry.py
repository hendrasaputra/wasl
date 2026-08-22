# -*- coding: utf-8 -*-
"""Attach a Sahabi's entry-heading chain to the deepest ancestor already in the tree.

al-Isti'ab puts the full nasab in the entry heading; Usd al-Ghaba puts it in the first lines of
the entry. Either way the shape is 'X b. Y b. Z ... al-Qurashi al-Umawi', which is a ladder
down from someone we already hold. We climb to the deepest rung the tree recognises and build
the rungs between - never guessing at the anchor, and never accepting a short tail.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ingest, nasab
from extract_walad import norm_name, identifies, BN
from translit import translit

# nisbas and the clauses that end a chain
TAIL = re.compile(r"\s*(?:القرشي|الأنصاري|الأموي|الهاشمي|المخزومي|الزهري|التيمي|العدوي|السهمي|"
                  r"الجمحي|الأسدي|الخزرجي|الأوسي|الكناني|الثقفي|التميمي|الكلبي|الفهري|النوفلي|"
                  r"المطلبي|العامري|الحارثي|الدوسي|المزني|السلمي|الغفاري|الجهني|البكري|"
                  r"وأمه|وأمها|أمه|أمها|يجتمع|أسلم|شهد|روى|قال|وكان|كان|له صحبة|رضي الله|"
                  r"وهو|وهي|ويقال|قيل|توفي|مات|استشهد|يكنى|أبو |[(\[]).*$", re.S)
NUM = re.compile(r"^\s*[(\[]?\d+[)\]]?\s*[-.]?\s*")
ISTIAB = re.compile(r"^###\s*\|\s*(.+)$", re.M)
USD = re.compile(r"^###\s*\$\s*(.+)$", re.M)


def chain_of(raw):
    s = NUM.sub("", raw.strip())
    s = TAIL.sub("", s)
    parts = [norm_name(x) for x in BN.split(s)]
    parts = [p for p in parts if p and re.match(r"^[ء-ي]", p) and len(p) <= 26]
    return parts


def entries(work, text):
    """(display chain, raw text the quote must come from)."""
    if work == "IbnAbdAlBarr":
        for m in ISTIAB.finditer(text):
            yield m.group(1).strip()
    else:
        for m in USD.finditer(text):
            body = text[m.end():m.end() + 400].replace("\n", " ")
            body = re.sub(r"^\s*[#~]+\s*|\(\s*[بدعس\s]+\s*\)", " ", body)
            head = NUM.sub("", m.group(1).strip())
            yield (head + " " + body) if head else body


def run(work, store, limit=None, quiet=True, min_anchor=2):
    # The length gate defers to identifies(), which asks the corpus how ambiguous the phrase is.
    # A blunt gate of 4 meant a four-name chain could never anchor - the longest tail excluding
    # the entry's own name is three - so 'Abd Allah b. Umar b. al-Khattab b. Nufayl' was
    # silently skipped, and with it most of the companion dictionary.
    raw = open(f"{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/corpus/{work}.txt",
               encoding="utf-8").read()
    txt_lines = [l for l in raw.split("\n") if not l.startswith("#META#")]
    text = "\n".join(txt_lines)
    flat = nasab.clean(work)
    attached = seen = 0
    for ent in entries(work, text):
        seen += 1
        ent = re.sub(r"PageV\d{2}P\d{3}[AB]?|\bms\d+\b|[#~]+|\[\d+\]|%~%", " ", ent)
        ent = re.sub(r"\s+", " ", ent).strip()
        chain = chain_of(ent)
        if len(chain) < min_anchor + 1:
            continue
        # deepest suffix the tree already knows
        anchor = idx = None
        for k in range(len(chain) - 1, min_anchor - 2, -1):
            tail = chain[k:]
            if len(tail) < min_anchor or not identifies(work, tail, store, None):
                continue
            hit = store.find_by_chain(tail)
            if hit:
                anchor, idx = hit, k
                break
        if anchor is None:
            continue
        # build downward from the anchor
        cur = anchor
        made = False
        for i in range(idx - 1, -1, -1):
            name = chain[i]
            pair = f"{name} بن {chain[i+1]}"
            quote = pair if nasab.locate(work, pair) else None
            if quote is None:
                break
            kid = store.person(name, father=cur,
                               sahabi=(i == 0 and work in ("IbnAbdAlBarr", "IbnAlAthir")) or None)
            if kid is None:
                break
            if store.add("father_of", cur, quote,
                         f"{translit(name)[0]} son of {translit(chain[i+1])[0]}",
                         object=kid, work=work, source_pattern="entry-chain"):
                made = True
            cur = kid
        if made:
            attached += 1
            if not quiet:
                print("  " + " b. ".join(translit(c)[0] for c in chain[:idx + 1]))
        if limit and attached >= limit:
            break
    print(f"{work}: {seen} entries scanned, {attached} attached")
    return attached


if __name__ == "__main__":
    st = ingest.Store()
    run(sys.argv[1], st, limit=int(sys.argv[2]) if len(sys.argv) > 2 else None, quiet=False)
    st.report("entry pass (not written)")
