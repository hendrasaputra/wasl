#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
# Wasl - a verifiable nasab. Copyright (C) 2026 Hendra Saputra.
"""Render one biography page per Who's who person, into bio/.

Built in CI and deployed from the artifact, never committed. The pages carry several hundred
thousand words of OpenITI's Arabic, and LICENSING.md says plainly that Wasl fetches the
corpus and does not vendor it. Generating at deploy time keeps that true: the repository
holds pins and checksums, the published site holds the text, and both are built from
OpenITI's own file.

This phase shows the entry and says where it is. It does not summarise, gloss or translate
it - that is 8c - and it deliberately does not link names in the prose into the tree, because
matching a name in running text to a person is the single thing this project has got wrong
most often.
"""
import html, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, ROOT)
import nasab, entries, i18n
from directory import DIRECTORY
from build import PALETTE

PAGE = re.compile(r'PageV(\d+)P(\d+)[AB]?')
DROP = re.compile(r'\bms\d+\b|%~%')
# Ibn Sa'd and al-Isti'ab open most reports with a chain of transmission. It is a fixed shape,
# so it can be set apart without parsing it: dim the isnad, leave the report at full weight.
ISNAD = re.compile(r'^(?:\d+\s*-\s*)?((?:أخبرنا|حدثنا|أنبأنا|أخبرني|حدثني|نا)\b.{0,600}?(?:قال[^:]{0,25}|قالت)\s*:)')
UI = {"back": {"en": "Back to the tree", "id": "Kembali ke pohon", "ms": "Kembali ke pokok"},
      "sum":  {"en": "In brief", "id": "Ringkasnya", "ms": "Ringkasnya"},
      "show": {"en": "show what each sentence rests on",
               "id": "tampilkan dasar setiap kalimat",
               "ms": "tunjukkan asas setiap ayat"},
      "edit": {"en": "editorial — rests on no single passage",
               "id": "redaksional — tidak bersandar pada satu nas",
               "ms": "editorial — tidak bersandar pada satu nas"},
      "sumnote": {"en": "Written from the entry below, not from anywhere else. Every sentence "
                        "but the marked ones carries the Arabic phrase it rests on, and "
                        "validate.py re-reads that phrase at the pages cited.",
                  "id": "Ditulis dari entri di bawah, bukan dari sumber lain. Setiap kalimat "
                        "kecuali yang ditandai membawa frasa Arab yang menjadi dasarnya, dan "
                        "validate.py membaca ulang frasa itu pada halaman yang disebutkan.",
                  "ms": "Ditulis daripada entri di bawah, bukan dari mana-mana sumber lain. "
                        "Setiap ayat kecuali yang ditanda membawa frasa Arab yang menjadi "
                        "asasnya, dan validate.py membaca semula frasa itu pada halaman "
                        "yang dinyatakan."},
      "src":  {"en": "the entry as the book prints it",
               "id": "entri sebagaimana tercetak dalam kitab",
               "ms": "entri sebagaimana tercetak dalam kitab"},
      "vol":  {"en": "vol.", "id": "jil.", "ms": "jil."},
      "pp":   {"en": "pp.", "id": "hlm.", "ms": "hlm."},
      "words":{"en": "words", "id": "kata", "ms": "perkataan"},
      "note": {"en": "The entry itself, at the pages named. It is not translated — only the "
                     "brief above it is written in English, and every sentence of that is "
                     "anchored to a phrase below.",
               "id": "Entri itu sendiri, pada halaman yang disebutkan. Tidak diterjemahkan — "
                     "hanya ringkasan di atasnya yang ditulis dalam bahasa Inggris, dan "
                     "setiap kalimatnya bersandar pada frasa di bawah.",
               "ms": "Entri itu sendiri, pada halaman yang dinyatakan. Tidak diterjemah — "
                     "hanya ringkasan di atasnya yang ditulis dalam bahasa Inggeris, dan "
                     "setiap ayatnya bersandar pada frasa di bawah."},
      "note0":{"en": "Arabic only. Nothing here is translated or summarised: what the page "
                     "shows is the entry itself, at the pages named.",
               "id": "Hanya bahasa Arab. Tidak ada yang diterjemahkan atau diringkas di sini: "
                     "yang ditampilkan adalah entri itu sendiri, pada halaman yang disebutkan.",
               "ms": "Bahasa Arab sahaja. Tiada apa-apa di sini yang diterjemah atau "
                     "diringkaskan: yang dipaparkan ialah entri itu sendiri, pada halaman "
                     "yang dinyatakan."}}


def paragraphs(work, line_no, depth):
    """The entry as (kind, text, page) blocks. mARkdown: '#' opens a paragraph, '~~'
    continues it, '###' is a subheading, and a page milestone CLOSES the page it ends."""
    raw = entries.body(work, line_no, depth)
    out, buf = [], []
    page = entries.page_span(work, line_no, depth)[1]

    def flush():
        """Close the paragraph being accumulated and push it, if it has any text."""
        if buf:
            t = DROP.sub(' ', ' '.join(buf))
            t = re.sub(r'\s+', ' ', PAGE.sub(' ', t)).strip()
            if t:
                out.append(('p', t, page))
            buf.clear()

    for ln in raw:
        if ln.startswith('###'):
            flush()
            h = re.sub(r'^###\s*[|$]*\s*(?:\(\d+\))?\s*\d*\s*-?\s*', '', ln).strip()
            if h:
                out.append(('h', DROP.sub(' ', PAGE.sub(' ', h)).strip(), page))
        else:
            if ln.startswith('~~'):
                buf.append(ln[2:])
            else:
                flush()
                buf.append(ln.lstrip('# '))
            m = PAGE.search(ln)
            if m:                       # this line ends a page; what follows is the next
                flush()
                page = int(m.group(2)) + 1
    flush()
    return out


def block_html(kind, text, page, seen):
    """One paragraph or subheading of an entry, as HTML.

    `seen` carries the pages already marked, so the margin number appears once per page
    rather than once per paragraph.
    """
    if kind == 'h':
        return f'<h3 dir="rtl" lang="ar">{html.escape(text)}</h3>'
    mark = ''
    if page not in seen:
        seen.add(page)
        mark = f'<a class="pg" id="p{page}" href="#p{page}">{page}</a>'
    m = ISNAD.match(text)
    if m:
        body = (html.escape(text[:m.start(1)])
                + f'<span class="isnad">{html.escape(m.group(1))}</span>'
                + html.escape(text[m.end():]))
    else:
        body = html.escape(text)
    return f'<p dir="rtl" lang="ar">{mark}{body}</p>'


def main():
    """Write one page per Who's who person into bio/.

    Joins three things by person: the pinned entries (entries.jsonl), the summary if one
    exists (summaries.jsonl), and bio/_ids.json, which build.py writes so that the label to
    id resolution happens once rather than twice.
    """
    works = nasab.sources()
    people = {p["id"]: p for p in (json.loads(l) for l in
              open(f"{ROOT}/people.jsonl", encoding="utf-8") if l.strip())}
    rows = [json.loads(l) for l in open(f"{ROOT}/entries.jsonl", encoding="utf-8") if l.strip()]
    pid_of = json.load(open(f"{ROOT}/bio/_ids.json", encoding="utf-8")) \
        if os.path.exists(f"{ROOT}/bio/_ids.json") else {}
    if not pid_of:
        print("FAIL - run build.py first: it writes bio/_ids.json mapping labels to ids",
              file=sys.stderr)
        return 1
    summaries = {}
    if os.path.exists(f"{ROOT}/summaries.jsonl"):
        for l in open(f"{ROOT}/summaries.jsonl", encoding="utf-8"):
            if l.strip():
                r = json.loads(l)
                summaries[r["who"]] = r
    # Khadija stands in the Who's who twice - under the household and under the wives - and
    # both rows resolve to one person. Key the lookup by id so whichever label carries the
    # summary reaches the page.
    by_pid = {}
    shell = open(f"{HERE}/bio_template.html", encoding="utf-8").read()
    os.makedirs(f"{ROOT}/bio", exist_ok=True)

    by_who = {}
    for r in rows:
        by_who.setdefault(r["who"], []).append(r)
    made = 0
    for who, rs in by_who.items():
        pid = pid_of.get(who)
        if not pid:
            print(f"  ! no person for {who}")
            continue
        p = people[pid]
        for _lbl, _r in summaries.items():
            if pid_of.get(_lbl) == pid:
                by_pid[pid] = _r
        secs = []
        for r in rs:
            hit, _ = entries.find(r["work"], r["pin"])
            seen = set()
            blocks = "\n".join(block_html(k, t, pg, seen)
                               for k, t, pg in paragraphs(r["work"], hit[0], hit[1]))
            w = works[r["work"]]
            pages = r["page"] if r["page"] == r["page_end"] else f'{r["page"]}–{r["page_end"]}'
            secs.append(
                f'<section><div class="src"><b>{html.escape(w["title_lat"])}</b> — '
                f'{html.escape(w["author_lat"])}, <span data-k="vol"></span> {r["vol"]}, '
                f'<span data-k="pp"></span> {pages} · {r["n_words"]:,} <span data-k="words"></span>'
                f'<i>{html.escape(w["edition"])}</i><i>{html.escape(w["version_uri"])}</i></div>'
                f'<div class="ar-head" dir="rtl" lang="ar">{html.escape(r["heading_ar"])}</div>'
                f'{blocks}</section>')
        srow = summaries.get(who) or by_pid.get(pid)
        if srow:
            bits, last_pg = [], None
            for ln in srow["lines"]:
                # the sentence carries its own id/ms, swapped in by the picker. The English is
                # the original here, so these are translated FROM it - see tools/i18n.py for
                # why that is the exception rather than the rule.
                tr = "".join(f' data-{k}="{html.escape(ln[k], quote=True)}"'
                             for k in ("id", "ms") if ln.get(k))
                txt = f'<i class="t"{tr}>{html.escape(ln["en"])}</i>'
                if ln["basis"] == "editorial":
                    bits.append(f'<span class="sl ed" data-k-t="edit">{txt}</span>')
                else:
                    pg = ln["page"] if ln["page"] == ln["page_end"] else f'{ln["page"]}–{ln["page_end"]}'
                    # 12 of Safiyya's 21 marks repeated the one before them: a page number
                    # that has not changed is noise in running prose, and the sentence above
                    # already carries the link
                    mark = ("" if pg == last_pg else
                            f'<a class="sp" href="#p{ln["page"]}">{pg}</a>')
                    last_pg = pg
                    bits.append(
                        f'<span class="sl">{txt}{mark}'
                        f'<q dir="rtl" lang="ar">{html.escape(ln["ar"])}</q></span>')
            summary = ('<div id="sum"><h2 data-k="sum"></h2>'
                       '<p class="sumnote" data-k="sumnote"></p>'
                       '<button id="anch" data-k="show"></button>'
                       '<div class="prose">' + " ".join(bits) + "</div></div>")
        else:
            summary = ""
        # the standing note must not claim nothing is summarised on a page that summarises
        # with a brief present the note sits above the Arabic, where it applies; without one
        # it stays at the top, because then it describes the whole page
        note = f'<p class="note" data-k="{"note" if srow else "note0"}"></p>'
        secs = ([note] + secs) if srow else secs
        out = (shell.replace("{{NOTE}}", "" if srow else note)
                    .replace("{{SUMMARY}}", summary)
                    .replace("{{NAME_AR}}", html.escape(p["name_ar"]))
                    .replace("{{NAME_LAT}}", html.escape(p["name_lat"]))
                    .replace("{{WHO}}", "" if who.startswith(p["name_lat"])
                             else " · " + html.escape(who))
                    .replace("{{PID}}", html.escape(pid))
                    .replace("{{BODY}}", "\n".join(secs))
                    .replace("{{UI}}", json.dumps(UI, ensure_ascii=False))
                    .replace("{{PALETTE}}", "\n".join(f"  --{k}: {v};" for k, v in PALETTE.items())))
        open(f"{ROOT}/bio/{pid}.html", "w", encoding="utf-8").write(out)
        made += 1
    total = sum(os.path.getsize(f"{ROOT}/bio/{f}") for f in os.listdir(f"{ROOT}/bio")
                if f.endswith(".html"))
    print(f"wrote {made} biography pages, {total//1024:,} KB "
          f"({sum(r['n_words'] for r in rows):,} words of Arabic)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
