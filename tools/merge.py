# -*- coding: utf-8 -*-
"""Merge people the sources spell two ways.

Editions differ on a letter and the parsers, quite correctly, refuse to assume: 'Rawah b. Adi'
and 'Rizah b. Adi' become two sons of Adi, and the whole branch beneath - Qurt, Abd Allah,
Riyah, Abd al-Uzza, Nufayl - duplicates with them. Worse, the duplicate then makes every chain
through it AMBIGUOUS, so find_by_chain refuses to resolve and Umar b. al-Khattab can never
attach. One spelling variant high in the tree silently costs hundreds of companions.

The merge rule needs to be tight, because 'Amr' and 'Umar' are also one letter apart and are
not the same man. So: merge two siblings only when their names differ by at most one letter AND
they have a child name in common. Shared issue is the evidence; near-spelling alone is not.
Exact-duplicate siblings merge outright.

Merging is recursive - once the parents are one, their same-named children are duplicate
siblings too - and runs to a fixpoint.
"""
import json, os, sys, collections
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path[:0] = [ROOT, os.path.dirname(os.path.abspath(__file__))]
import nasab


def dist1(a, b):
    """True if a and b are within one substitution/insertion/deletion."""
    if a == b:
        return True
    la, lb = len(a), len(b)
    if abs(la - lb) > 1:
        return False
    if la == lb:
        return sum(x != y for x, y in zip(a, b)) == 1
    if la > lb:
        a, b, la, lb = b, a, lb, la
    for i in range(lb):                       # b with one char removed
        if b[:i] + b[i + 1:] == a:
            return True
    return False


def main(write=False):
    people = [json.loads(l) for l in open(f"{ROOT}/people.jsonl", encoding="utf-8") if l.strip()]
    claims = [json.loads(l) for l in open(f"{ROOT}/claims.jsonl", encoding="utf-8") if l.strip()]
    by = {p["id"]: p for p in people}
    alias = {}                                # loser -> winner

    def root(x):
        while x in alias:
            x = alias[x]
        return x

    merges, rounds = [], 0
    while True:
        rounds += 1
        kids = collections.defaultdict(list)
        for c in claims:
            if c["type"] == "father_of":
                kids[root(c["subject"])].append(root(c["object"]))
        for k in kids:
            kids[k] = list(dict.fromkeys(kids[k]))
        # 'al-Abbas' and 'Abbas' under one father are one man written two ways; the article is
        # not a distinguishing letter, and edit distance alone treats it as two
        def key(x):
            n = nasab.normalise(by[x]["name_ar"])
            return n[2:] if n.startswith("ال") and len(n) > 3 else n
        nm = {p: key(p) for p in by}
        freq = collections.Counter(nm[p] for p in by if p not in alias)
        found = 0
        for f, ch in list(kids.items()):
            for i in range(len(ch)):
                for j in range(i + 1, len(ch)):
                    a, b = root(ch[i]), root(ch[j])
                    if a == b:
                        continue
                    na, nb = nm[a], nm[b]
                    if na == nb:
                        pass                                   # same name, same father
                    elif dist1(na, nb):
                        ca = {nm[x] for x in kids.get(a, ())}
                        cb = {nm[x] for x in kids.get(b, ())}
                        shared = ca & cb
                        # One shared child is weak when the name is Abd Allah or Muhammad, and
                        # 'Amr' and 'Umar' are one letter apart without being one man. Ask for
                        # two children in common, or one that is rare enough to mean something.
                        if not (len(shared) >= 2 or
                                (len(shared) == 1 and freq[next(iter(shared))] <= 4)):
                            continue
                    else:
                        continue
                    # keep the better-attested spelling: more works citing it, then more issue
                    score = lambda x: (len({c["work"] for c in claims
                                            if c["type"] == "father_of" and root(c.get("object") or "") == x}),
                                       len(kids.get(x, ())))
                    win, lose = (a, b) if score(a) >= score(b) else (b, a)
                    alias[lose] = win
                    merges.append((by[lose]["name_ar"], by[win]["name_ar"], by[f]["name_lat"]))
                    found += 1
        if not found or rounds > 40:
            break

    print(f"{len(alias)} merged in {rounds} rounds")
    for lo, wi, f in merges[:14]:
        print(f"   {lo} -> {wi}   (under {f})")
    if len(merges) > 14:
        print(f"   ... and {len(merges)-14} more")

    people = [p for p in people if p["id"] not in alias]
    seen, out = set(), []
    for c in claims:
        c["subject"] = root(c["subject"])
        if c.get("object"):
            c["object"] = root(c["object"])
        if c["type"] == "father_of" and c["subject"] == c["object"]:
            continue
        k = (c["type"], c["subject"], c.get("object"), c["work"], nasab.normalise(c["ar"]))
        if k in seen:
            continue
        seen.add(k)
        out.append(c)
    print(f"claims {len(claims)} -> {len(out)}, people -> {len(people)}")
    if write:
        with open(f"{ROOT}/people.jsonl", "w", encoding="utf-8") as f:
            for p in people:
                f.write(json.dumps(p, ensure_ascii=False) + "\n")
        with open(f"{ROOT}/claims.jsonl", "w", encoding="utf-8") as f:
            for c in out:
                f.write(json.dumps(c, ensure_ascii=False) + "\n")
        print("written")


if __name__ == "__main__":
    main(write="--write" in sys.argv)
