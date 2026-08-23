# -*- coding: utf-8 -*-
# SPDX-License-Identifier: GPL-3.0-or-later
# Wasl - a verifiable nasab. Copyright (C) 2026 Hendra Saputra.
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
    """The whole dataset in memory, plus the indexes that make lookups O(1).

    Every extraction pass follows the same shape: build a Store, call person() and add() as
    the corpus is read, then save(). Nothing is written until save(), so a pass that fails
    part-way leaves the files untouched.

    The indexes are not an optimisation detail, they are what makes a pass finish at all.
    `aliases_of` once walked every claim for every person, making chain resolution
    O(people x claims) - a ten-minute hang that became 0.7s once these were added. Anything
    called per-statement has to be O(1).
    """

    def __init__(self):
        """Load the dataset from disk and build every index over it."""
        self.people = {}          # id -> person row
        self.order = []           # ids in file order, so save() does not reshuffle the file
        self.claims = []
        self._byfather = {}       # (father id, normalised child name) -> child id
        self._ids = set()         # every id in use, for minting a fresh one
        self._seen = set()        # claims already recorded, so a re-run adds nothing twice
        self._byname = {}         # normalised name -> [person]
        self._alias = {}          # person -> set of normalised alias values
        self._byalias = {}        # normalised alias value -> [person]
        self.rejected = []        # quotes the corpus did not carry, reported by report()
        self.load()

    # ---------------------------------------------------------------- io
    def load(self):
        """Read people.jsonl and claims.jsonl and build every index from them.

        A pass therefore starts from whatever the previous pass wrote, which is what lets the
        replay pipeline in CLAUDE.md run phase after phase over one growing tree.
        """
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
            if c["type"] == "alias" and c.get("value_ar"):
                self._note_alias(c["subject"], c["value_ar"])
            if c["type"] == "father_of":
                self._byfather[(c["subject"], nasab.normalise(self.people[c["object"]]["name_ar"]))] = c["object"]
        self._n = max((int(c["cid"][1:]) for c in self.claims), default=0)

    def save(self):
        """Write both files back. Called once, at the end of a pass, and only with --write."""
        for c in self.claims:
            span = nasab.locate(c["work"], c["ar"])
            if span is None:
                raise RuntimeError(f"{c['cid']} quote vanished from {c['work']}: {c['ar'][:60]}")
            c["vol"], c["page"], c["page_end"] = span
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
        anchors = list(self._byname.get(names[-1], ())) + list(self._byalias.get(names[-1], ()))
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

    def _note_alias(self, pid, value_ar):
        """Record an alias in both directions, so child_of can match a man under either name."""
        v = nasab.normalise(value_ar)
        self._alias.setdefault(pid, set()).add(v)
        self._byalias.setdefault(v, []).append(pid)

    def aliases_of(self, pid):
        """Indexed. Scanning every claim per person made chain resolution O(people x claims),
        which is what turned a Phase-5 run into a ten-minute hang."""
        return self._alias.get(pid, frozenset())

    def child_of(self, fid, names):
        """An existing child of `fid` answering to any of these names - its own or a recorded
        alias. Names may be raw Arabic or already normalised.

        The alias half matters: 'Amir wa-huwa Mudrika' is one man under two readings, and
        without it the second reading mints a twin brother.
        """
        keys = {nasab.normalise(n) for n in names if n} | {n for n in names if n}
        for (f, nm), cid in self._byfather.items():
            if f == fid and (nm in keys or self.aliases_of(cid) & keys):
                return cid
        return None

    def descendants(self, root):
        """Every person below `root`, used to scope a pass - Phase 2 runs under Fihr, which
        Ibn Hazm defines as exactly the set of people called Qurashi.

        Rebuilds the child map on each call, so hoist it out of a loop if one is ever needed
        per statement rather than once per pass.
        """
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

    def copied_line(self, pid):
        """Whether this person's ancestry repeats a four-name parser-copied run."""
        father = {c["object"]: c["subject"] for c in self.claims if c["type"] == "father_of"}
        seq = []
        while pid:
            seq.append(nasab.normalise(self.people[pid]["name_ar"]))
            pid = father.get(pid)
        return any(seq[i:i + 4] == seq[j:j + 4]
                   for i in range(len(seq) - 4) for j in range(i + 4, len(seq) - 3))

    def person(self, name_ar, father=None, force=False, **extra):
        """Get or mint. Identity is (name, father); a bare name with no father is ambiguous
        and must already exist - unless force=True, which mints a fresh root. Only a
        hand-quoted pass may force: it means 'the book gives this chain and its top name is
        nobody we already hold', which a parser is in no position to assert."""
        name_ar = re.sub(r"\s+", " ", name_ar).strip()
        key = nasab.normalise(name_ar)
        alias = extra.pop("_alias", None)
        if force:
            pass
        elif father:
            hit = self.child_of(father, [name_ar, alias])
            if hit:
                return hit
        else:
            hits = [pid for pid, p in self.people.items() if nasab.normalise(p["name_ar"]) == key]
            if len(hits) == 1:
                return hits[0]
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
        if type == "alias" and extra.get("value_ar"):
            self._note_alias(subject, extra["value_ar"])
        self.claims.append(c)
        return cid

    def has_edge(self, father, child):
        """Is this exact parent edge already recorded, from any work?"""
        return any(c["type"] == "father_of" and c["subject"] == father and c["object"] == child
                   for c in self.claims)

    def report(self, label):
        """Print what the pass did, including what it REFUSED. A rejected quote is a finding -
        the corpus did not carry it - so it is counted and shown, never dropped silently."""
        print(f"{label}: {len(self.people)} people, {len(self.claims)} claims"
              + (f", {len(self.rejected)} quotes rejected" if self.rejected else ""))
        for w, q in self.rejected[:5]:
            print(f"   rejected {w}: {q}")
