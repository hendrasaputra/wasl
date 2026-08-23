#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
# Wasl - a verifiable nasab. Copyright (C) 2026 Hendra Saputra.
"""Wasl - generate index.html from people.jsonl + claims.jsonl. Run validate.py first."""
import json, math, os, re, sys, html, collections
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "tools"))
import nasab

ROOT = os.path.dirname(os.path.abspath(__file__))

PALETTE = {  # from the project palette: brass golds into deepening greens
    "gold":   "#A98B42", "gold-lt": "#C9A55F",
    "grn-1":  "#3B7A5C", "grn-2":   "#17513A",
    "grn-3":  "#0C4A31", "grn-4":   "#08301F",
}


def rosette(n=10, steps=(3, 4), r=100):
    """A 10-fold girih rosette: decagonal frame, interlaced star polygons, central star."""
    def pts(count, radius, phase=0.0):
        return [(radius * math.cos(2 * math.pi * i / count - math.pi / 2 + phase),
                 radius * math.sin(2 * math.pi * i / count - math.pi / 2 + phase))
                for i in range(count)]

    def star(count, step, radius, phase=0.0):
        p, order, i = pts(count, radius, phase), [], 0
        for _ in range(count):
            order.append(p[i]); i = (i + step) % count
        return "M" + "L".join(f"{x:.2f},{y:.2f}" for x, y in order) + "Z"

    d = ["M" + "L".join(f"{x:.2f},{y:.2f}" for x, y in pts(n, r)) + "Z"]
    for s in steps:
        d.append(star(n, s, r * 0.97))
        d.append(star(n, s, r * 0.62, math.pi / n))
    d.append(star(n, 3, r * 0.30))
    d.append("M" + "L".join(f"{x:.2f},{y:.2f}" for x, y in pts(n, r * 0.62)) + "Z")
    box = f"{-r-4} {-r-4} {2*r+8} {2*r+8}"
    return (f'<svg viewBox="{box}" xmlns="http://www.w3.org/2000/svg" fill="none" '
            f'stroke="currentColor" stroke-width="1.4" stroke-linejoin="round">'
            + "".join(f'<path d="{p}"/>' for p in d) + "</svg>")


def main():
    people = {p["id"]: p for p in (json.loads(l) for l in open(f"{ROOT}/people.jsonl", encoding="utf-8") if l.strip())}
    claims = [json.loads(l) for l in open(f"{ROOT}/claims.jsonl", encoding="utf-8") if l.strip()]
    works = nasab.sources()

    kids = collections.defaultdict(list)
    father = {}
    mother = {}
    by_person = collections.defaultdict(list)
    for c in claims:
        by_person[c["subject"]].append(c)
        if c.get("object"):
            by_person[c["object"]].append(c)
        if c["type"] == "father_of":
            father[c["object"]] = c["subject"]
            if c["object"] not in kids[c["subject"]]:
                kids[c["subject"]].append(c["object"])
        if c["type"] == "mother_of":
            mother[c["object"]] = c["subject"]
    # a child whose father these books never name still belongs in the tree - hang it on the
    # mother rather than leaving it floating at the root
    for child, mum in mother.items():
        if child not in father and child not in kids[mum]:
            kids[mum].append(child)

    roots = [p for p in people if p not in father and p not in mother]
    via_mother = {c for c in mother if c not in father}

    # how many sit beneath each node - shown on the [+] so you know what it opens
    below = {}

    def count(pid):
        if pid not in below:
            below[pid] = sum(1 + count(k) for k in kids.get(pid, ()))
        return below[pid]

    sys.setrecursionlimit(10000)
    for r in roots:
        count(r)

    # ---- bands. Not centuries: these books give no years, and a band label that looked like
    # a date would read as sourced when it was computed. These four are things the sources
    # either state or do, so each is defensible in one sentence.
    def ancestors(pid):
        out, c = set(), father.get(pid)
        while c:
            out.add(c)
            c = father.get(c)
        return out

    unattested = ancestors("p.adnan") | {"p.qahtan"}     # the sources' own declared ceiling
    band = {}
    for pid in people:
        if pid in unattested:
            band[pid] = "beyond"
        elif people[pid].get("sahabi"):
            band[pid] = "companion"
        else:
            band[pid] = "descendant" if any(people[a].get("sahabi") for a in ancestors(pid)) \
                        else "arabia"
    BAND_KEY = {"beyond": "band_beyond", "arabia": "band_arabia",
                "companion": "band_comp", "descendant": "band_desc"}
    BANDS = {
      "beyond":     ("beyond the attested chain",
                     "At or above ʿAdnān and Qaḥṭān — the stretch these books themselves "
                     "decline to vouch for (kadhaba al-nassābūn; Ibn Ḥazm: nothing above "
                     "Qaḥṭān is sound)."),
      "arabia":     ("the Arab genealogy",
                     "Below ʿAdnān or Qaḥṭān, with no companion recorded above them — the "
                     "tribal genealogy the books treat as established."),
      "companion":  ("companions",
                     "Carries an entry in al-Istīʿāb or Usd al-Ghāba. That is a fact about "
                     "the sources, not a judgement about the person."),
      "descendant": ("recorded below a companion",
                     "Placed under someone with a companion entry — largely the Umayyad, "
                     "ʿAbbāsid and ʿAlid lines Ibn Ḥazm carries forward."),
    }
    spine = set()
    n = "p.muhammad"
    while n:
        spine.add(n)
        n = father.get(n)

    def node(pid, depth=0, gen=1, ind=0):
        p = people[pid]
        cs = by_person[pid]
        srcs = sorted({c["work"] for c in cs})
        edge_srcs = sorted({c["work"] for c in cs if c["type"] == "father_of" and c["object"] == pid})
        disputed = any(c["type"] in ("dissent", "variant_chain") and c["subject"] == pid for c in cs)
        children = kids.get(pid, [])
        badges = []
        if p.get("prophet"):
            badges.append('<b class="bp" data-k="b_nabi">nabī</b>')
        if p["sex"] == "F":
            badges.append('<b class="bf" data-k="b_f">f</b>')
        if pid in via_mother:
            badges.append('<b class="bm" data-k="b_viamother">via mother</b>')
        auto = {c.get("source_pattern") for c in cs
                if c["type"] == "father_of" and c["object"] == pid}
        if auto and not (auto & {None, "spine"}):
            badges.append('<b class="ba" data-k="b_auto" data-tk="b_auto_t">auto</b>')
        if disputed:
            badges.append('<b class="bd" data-k="b_ikhtilaf">ikhtilāf</b>')
        if edge_srcs:
            badges.append(f'<b class="bs" data-k="b_src" data-n="{len(edge_srcs)}" '
                          f'title="{" ".join(edge_srcs)}">{len(edge_srcs)}&#8239;src</b>')
        if p.get("sahabi"):
            badges.append('<b class="bc" data-k="b_sahabi">ṣaḥābī</b>')
        kun = []
        for c in cs:
            if c["type"] == "kunya" and c["subject"] == pid and c.get("value_lat") \
               and c["value_lat"] not in kun:
                kun.append(c["value_lat"])
        alias = [c for c in cs if c["type"] == "alias" and c["subject"] == pid]
        al = ""
        if alias:
            uniq = []
            for a in alias:
                v = a.get("value_lat") or ""
                if v and v not in uniq and v != p["name_lat"]:
                    uniq.append(v)
            if uniq:
                al = f'<i class="alias">= {" / ".join(html.escape(u) for u in uniq)}</i>'
        if kun:
            al += f'<i class="kunya">{html.escape(" · ".join(kun[:2]))}</i>'
        summary = (f'<summary data-id="{pid}" data-gen="{gen}" data-band="{band.get(pid,"")}" data-search="{html.escape((p["name_lat"]+" "+p["name_ar"]+" "+p.get("kunya_lat","")+" "+p.get("kunya_ar","")+" "+" ".join(kun)+" "
                   +" ".join(c.get("value_ar","") for c in cs if c["type"]=="kunya")+" "+" ".join(a.get("value_lat","")+" "+a.get("value_ar","") for a in alias)).lower())}">'
                   f'<span class="tw{"" if children else " leaf"}" data-n="{below.get(pid,0)}"></span>'
                   f'<span class="gen">{gen}</span>'
                   f'<span class="ar" dir="rtl" lang="ar">{html.escape(p["name_ar"])}</span>'
                   f'<span class="lat">{html.escape(p["name_lat"])}{al}</span>'
                   f'<span class="badges">{"".join(badges)}</span></summary>')
        open_attr = " open" if pid in spine else ""
        # `ind` counts only the levels that actually indent - a fork. It drives a diminishing
        # scale: 25 forks at a flat 28px put the deepest name 570px from the margin, which is
        # most of a phone screen and a third of a desktop column. Every level still steps
        # right, so nothing is ever ambiguous; the steps just get smaller as they go.
        nxt = ind + (1 if len(children) > 1 else 0)
        inner = subtree(children, depth + 1, gen + 1, nxt)
        cls = "kids linear" if len(children) == 1 else f"kids kd{min(nxt // 5, 3)}"
        return f'<details{open_attr} id="{pid}">{summary}{f'<div class="{cls}">{inner}</div>' if inner else ""}</details>'

    RUN_MIN = 3   # a run shorter than this is cheaper to read as rows than as a ribbon

    def run_from(pid):
        """The maximal chain of single-child links starting at pid."""
        run = [pid]
        while len(kids.get(run[-1], ())) == 1:
            run.append(kids[run[-1]][0])
        return run

    def ribbon(run, gen):
        """A chain of names on one line. Lossless: every node here has exactly one child, so
        there is no branching to lose - only rows to save."""
        links = "".join(
            f'<b data-go="{i}">{html.escape(people[i]["name_lat"])}</b>' for i in run)
        return (f'<div class="ribbon inline">'
                f'<span class="rl" data-n="{len(run)}">{len(run)}&nbsp;gen</span>'
                f'{links}</div>')

    def subtree(children, depth, gen, ind=0):
        """Render a set of children, folding any single-child chain among them into a ribbon."""
        out = []
        for c in children:
            run = run_from(c)
            if len(run) - 1 >= RUN_MIN:
                # ribbon the chain, then resume the tree at the node that forks
                out.append(ribbon(run[:-1], gen) + node(run[-1], depth, gen + len(run) - 1, ind))
            else:
                out.append(node(c, depth, gen, ind))
        return "".join(out)

    # ---- the unbranching prologue. Adam to Udad is 28 links with exactly one child each: a
    # sequence, not a tree, and it currently eats half the scroll depth carrying no branching
    # information at all. Render it as a ribbon and start the tree where the tree begins.
    ordered = sorted(roots, key=lambda x: (x != "p.adam", x))
    tree = subtree(ordered, 0, 1, 0)
    prologue = {r: run_from(r) for r in ordered if len(run_from(r)) - 1 >= RUN_MIN}
    starts = [run_from(r)[-1] if r in prologue else r for r in ordered]

    data = {
        "people": people,
        "claims": claims,
        "works": {k: {kk: v[kk] for kk in ("author_lat", "title_lat", "title_ar", "author_ar", "edition", "death_ah", "version_uri")} for k, v in works.items()},
        "father": father, "mother": mother,
        "below": {k: v for k, v in below.items() if v},
        "prologue": prologue, "starts": starts,
        "band": band, "bands": BANDS, "band_key": BAND_KEY, "roots": sorted(roots, key=lambda x: (x != "p.adam", x)),
        "kids": {k: v for k, v in kids.items() if v},
    }
    stats = {
        "people": len(people), "claims": len(claims), "works": len({c["work"] for c in claims}),
        "edges": len({(c["subject"], c["object"]) for c in claims if c["type"] in ("father_of", "mother_of")}),
    }

    # ---- a directory of the people a reader actually comes looking for. Resolved here, at
    # build time, from the chain that identifies each one, so a link can never point nowhere.
    import unicodedata as _u

    def _n(x):
        x = _u.normalize("NFKC", x)
        for a, b in (("أ","ا"),("إ","ا"),("آ","ا"),("ة","ه"),("ى","ي"),("ئ","ي"),("ؤ","و")):
            x = x.replace(a, b)
        return re.sub(r"\s+", " ", x).strip()

    byname = collections.defaultdict(list)
    for pid, pr in people.items():
        byname[_n(pr["name_ar"])].append(pid)

    def find(chain):
        """Walk down a name chain given deepest-last; return the id only if it is unambiguous."""
        if chain[-1] == "__root__":       # a root has no father to anchor on
            c = [p for p in roots if _n(people[p]["name_ar"]) == _n(chain[0])]
            return c[0] if len(c) == 1 else None
        hits = []
        for a in byname.get(_n(chain[-1]), ()):
            cur = a
            for nm in reversed(chain[:-1]):
                nxt = next((k for k in kids.get(cur, ()) if _n(people[k]["name_ar"]) == _n(nm)), None)
                cur = nxt
                if cur is None:
                    break
            if cur:
                hits.append(cur)
        return hits[0] if len(set(hits)) == 1 else None

    from directory import DIRECTORY
    from i18n import LANGS, UI, DATA

    directory = []
    missing = []
    for group, items in DIRECTORY:
        rows = []
        for label, chain in items:
            pid = find(chain)
            (rows.append([label, pid]) if pid else missing.append(label))
        if rows:
            directory.append([group, rows])
    if missing:
        print("  directory entries unresolved: " + ", ".join(missing))

    data["directory"] = directory
    data["langs"] = LANGS
    data["ui"] = {lang: {k: v.get(lang, v["en"]) for k, v in UI.items()} for lang in LANGS}
    # every data string the page shows in prose - tribes, notes, verdicts, chain labels, isnads
    import i18n as _i18n
    seen = set()
    for pr in people.values():
        seen |= {pr.get("tribe"), pr.get("note")}
    for c in claims:
        seen |= {c.get(k) for k in ("note", "author_verdict", "chain_label", "text_note",
                                    "event_lat", "isnad_lat")}
    # the Who's who headings are prose the page prints, so they translate like any other
    seen |= {g for g, _ in directory}
    seen.discard(None)
    # sorted, not set order: Python randomises string hashing per process, so iterating the
    # set gave a different key order on every build and index.html was never twice the same
    data["dtr"] = {lang: {s: _i18n.data(s, lang) for s in sorted(seen)
                          if _i18n.data(s, lang) != s} for lang in ("id", "ms")}

    tpl = open(f"{ROOT}/template.html", encoding="utf-8").read()
    out = (tpl.replace("{{TREE}}", tree)
              .replace("{{DATA}}", json.dumps(data, ensure_ascii=False))
              .replace("{{ROSETTE}}", rosette())
              .replace("{{STATS}}", json.dumps(stats))
              .replace("{{CSSVARS}}", "".join(f"--{k}:{v};" for k, v in PALETTE.items())))
    open(f"{ROOT}/index.html", "w", encoding="utf-8").write(out)
    print(f"wrote index.html  {os.path.getsize(f'{ROOT}/index.html')//1024} KB  "
          f"{stats['people']} people, {stats['claims']} claims")


if __name__ == "__main__":
    main()
