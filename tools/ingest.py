# -*- coding: utf-8 -*-
"""Shared ingest layer: mint people, add claims, refuse anything the corpus does not support.

Every add_claim call verifies the quote against the pinned text before the claim exists, so an
unverifiable row can never reach the JSONL. Person identity is (normalised name, father) - the
same name under a different father is a different person, which is how these books work.
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path[:0] = [ROOT, HERE]
import nasab
from translit import translit, slug


class Store:
    def __init__(self):
        self.people = {}
        self.order = []
        self.claims = []
        self._byfather = {}
        self._ids = set()
        self._seen = set()
        self._byname = {}
        self.rejected = []
        self.load()

    # ---------------------------------------------------------------- io
    def load(self):
        for l in open(f"{ROOT}/people.jsonl", encoding="utf-8"):
            if l.strip():
                p = json.loads(l)
                self.people[p["id"]] = p
                self.order.append(p["id"])
                self._ids.add(p["id"])
                self._byname.setdefault(nasab.normalise(p["name_ar"]), []).append(p["id"])
        for l in open(f"{ROOT}/claims.jsonl", encoding="utf-8"):
            if l.strip():
                self.claims.append(json.loads(l))
        for c in self.claims:
            self._seen.add((c["type"], c["subject"], c.get("object"), c["work"],
                            nasab.normalise(c["ar"])))
            if c["type"] == "father_of":
                self._byfather[(c["subject"], nasab.normalise(self.people[c["object"]]["name_ar"]))] = c["object"]
        self._n = max((int(c["cid"][1:]) for c in self.claims), default=0)

    def save(self):
        with open(f"{ROOT}/people.jsonl", "w", encoding="utf-8") as f:
            for pid in self.order:
                f.write(json.dumps(self.people[pid], ensure_ascii=False) + "\n")
        with open(f"{ROOT}/claims.jsonl", "w", encoding="utf-8") as f:
            for c in self.claims:
                f.write(json.dumps(c, ensure_ascii=False) + "\n")

    # ------------------------------------------------------------ people
    def find_by_chain(self, chain, scope=None):
        """chain = [name, father, grandfather, ...] as the text gives it. Resolves ONLY if the
        whole chain matches a path already in the tree, and only if it matches one path.

        Matching a suffix is not good enough: 'Sa'd Hudhaym b. Zayd' would otherwise latch onto
        any Zayd in the tree and hang a Qahtani clan under Quraysh. A partial match is a wrong
        answer, so it must be no answer."""
        if not chain:
            return None
        names = [nasab.normalise(n) for n in chain]
        anchors = list(self._byname.get(names[-1], ()))
        if len(anchors) < 8:                       # aliases are worth the scan only when rare
            anchors += [p for p in self.people if names[-1] in self.aliases_of(p)]
        if scope is not None:
            anchors = [a for a in anchors if a in scope]
        hits = []
        for a in anchors:
            cur = a
            for nm in reversed(names[:-1]):
                cur = self.child_of(cur, [nm]) if cur else None
                if cur is None:
                    break
            if cur is not None and (scope is None or cur in scope):
                hits.append(cur)
        return hits[0] if len(set(hits)) == 1 else None

    def aliases_of(self, pid):
        return {nasab.normalise(c["value_ar"]) for c in self.claims
                if c["type"] == "alias" and c["subject"] == pid and c.get("value_ar")}

    def child_of(self, fid, names):
        """names may be raw Arabic or already normalised."""
        """An existing child of fid answering to any of these names - its own or a recorded
        alias. 'Amir wa-huwa Mudrika' is one man under two readings, not two men."""
        keys = {nasab.normalise(n) for n in names if n} | {n for n in names if n}
        for (f, nm), cid in self._byfather.items():
            if f == fid and (nm in keys or self.aliases_of(cid) & keys):
                return cid
        return None

    def descendants(self, root):
        seen, stack = {root}, [root]
        kids = {}
        for c in self.claims:
            if c["type"] == "father_of":
                kids.setdefault(c["subject"], set()).add(c["object"])
        while stack:
            for k in kids.get(stack.pop(), ()):
                if k not in seen:
                    seen.add(k)
                    stack.append(k)
        return seen

    def person(self, name_ar, father=None, **extra):
        """Get or mint. Identity is (name, father); a bare name with no father is ambiguous
        and must already exist."""
        name_ar = re.sub(r"\s+", " ", name_ar).strip()
        key = nasab.normalise(name_ar)
        alias = extra.pop("_alias", None)
        if father:
            hit = self.child_of(father, [name_ar, alias])
            if hit:
                return hit
        else:
            hits = [pid for pid, p in self.people.items() if nasab.normalise(p["name_ar"]) == key]
            if len(hits) == 1:
                return hits[0]
            if len(hits) > 1:
                return None
        lat, prov = translit(name_ar)
        base = "p." + slug(lat)
        pid, n = base, 1
        while pid in self._ids:
            n += 1
            pid = f"{base}-{n}"
        row = {"id": pid, "name_ar": name_ar, "name_lat": lat,
               "sex": extra.pop("sex", "M")}
        if prov:
            row["translit_provisional"] = True
        row.update(extra)
        self.people[pid] = row
        self.order.append(pid)
        self._ids.add(pid)
        self._byname.setdefault(key, []).append(pid)
        return pid

    # ------------------------------------------------------------ claims
    def add(self, type, subject, ar, en, object=None, work=None, **extra):
        """Add a claim, but only if the corpus backs the quote. Returns cid or None."""
        key = (type, subject, object, work, nasab.normalise(ar))
        if key in self._seen:
            return None                      # same statement, same work - already recorded
        span = nasab.locate(work, ar)
        if span is None:
            self.rejected.append((work, ar[:60]))
            return None
        self._seen.add(key)
        if type == "father_of":
            if subject == object:
                return None                  # a self-edge is always a parse error
            self._byfather[(subject, nasab.normalise(self.people[object]["name_ar"]))] = object
        self._n += 1
        cid = f"c{self._n:05d}"
        c = {"cid": cid, "type": type, "subject": subject, "object": object, "work": work,
             "vol": span[0], "page": span[1], "page_end": span[2], "ar": ar, "en": en,
             "grade": extra.pop("grade", "explicit"), **extra}
        if object is None:
            del c["object"]
        self.claims.append(c)
        return cid

    def has_edge(self, father, child):
        return any(c["type"] == "father_of" and c["subject"] == father and c["object"] == child
                   for c in self.claims)

    def report(self, label):
        print(f"{label}: {len(self.people)} people, {len(self.claims)} claims"
              + (f", {len(self.rejected)} quotes rejected" if self.rejected else ""))
        for w, q in self.rejected[:5]:
            print(f"   rejected {w}: {q}")
