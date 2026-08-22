#!/usr/bin/env python3
"""Wasl - generate index.html from people.jsonl + claims.jsonl. Run validate.py first."""
import json, math, os, sys, html, collections
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
    spine = set()
    n = "p.muhammad"
    while n:
        spine.add(n)
        n = father.get(n)

    def node(pid, depth=0, gen=1):
        p = people[pid]
        cs = by_person[pid]
        srcs = sorted({c["work"] for c in cs})
        edge_srcs = sorted({c["work"] for c in cs if c["type"] == "father_of" and c["object"] == pid})
        disputed = any(c["type"] in ("dissent", "variant_chain") and c["subject"] == pid for c in cs)
        children = kids.get(pid, [])
        badges = []
        if p.get("prophet"):
            badges.append('<b class="bp">nabī</b>')
        if p["sex"] == "F":
            badges.append('<b class="bf">f</b>')
        if pid in via_mother:
            badges.append('<b class="bm">via mother</b>')
        auto = {c.get("source_pattern") for c in cs
                if c["type"] == "father_of" and c["object"] == pid}
        if auto and not (auto & {None, "spine"}):
            badges.append('<b class="ba" title="attached by the chain parser: the quote is '
                          'verified, the placement rests on the anchor being right">auto</b>')
        if disputed:
            badges.append('<b class="bd">ikhtilāf</b>')
        if edge_srcs:
            badges.append(f'<b class="bs" title="{" ".join(edge_srcs)}">{len(edge_srcs)}&#8239;src</b>')
        if p.get("sahabi"):
            badges.append('<b class="bc">ṣaḥābī</b>')
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
        summary = (f'<summary data-id="{pid}" data-gen="{gen}" data-search="{html.escape((p["name_lat"]+" "+p["name_ar"]+" "+p.get("kunya_lat","")+" "+p.get("kunya_ar","")+" "+" ".join(a.get("value_lat","")+" "+a.get("value_ar","") for a in alias)).lower())}">'
                   f'<span class="tw{"" if children else " leaf"}" data-n="{below.get(pid,0)}"></span>'
                   f'<span class="gen">{gen}</span>'
                   f'<span class="ar" dir="rtl" lang="ar">{html.escape(p["name_ar"])}</span>'
                   f'<span class="lat">{html.escape(p["name_lat"])}{al}</span>'
                   f'<span class="badges">{"".join(badges)}</span></summary>')
        open_attr = " open" if pid in spine else ""
        inner = "".join(node(k, depth + 1, gen + 1) for k in children)
        # a lineage is mostly a single line; indent only where it actually forks
        cls = "kids linear" if len(children) == 1 else "kids"
        return f'<details{open_attr} id="{pid}">{summary}{f'<div class="{cls}">{inner}</div>' if inner else ""}</details>'

    tree = "".join(node(r) for r in sorted(roots, key=lambda x: (x != "p.adam", x)))

    data = {
        "people": people,
        "claims": claims,
        "works": {k: {kk: v[kk] for kk in ("author_lat", "title_lat", "title_ar", "author_ar", "edition", "death_ah", "version_uri")} for k, v in works.items()},
        "father": father, "mother": mother,
        "below": {k: v for k, v in below.items() if v},
        "kids": {k: v for k, v in kids.items() if v},
    }
    stats = {
        "people": len(people), "claims": len(claims), "works": len({c["work"] for c in claims}),
        "edges": len({(c["subject"], c["object"]) for c in claims if c["type"] in ("father_of", "mother_of")}),
    }

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
