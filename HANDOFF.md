<!-- SPDX-License-Identifier: GPL-3.0-or-later
     Wasl - a verifiable nasab. Copyright (C) 2026 Hendra Saputra. -->

# HANDOFF

You are picking up **Wasl** (وصل, "the link") — a genealogy of the Prophet Muḥammad ﷺ, his
household, the Ṣaḥāba and the Arab tribes, in which **every single assertion is traceable to a
page of a pinned Arabic primary text, and a script re-reads that page to prove it.**

That last clause is the whole project. A genealogy site is easy; one where a stranger can
check any line against the book is not. If you change nothing else, keep that.

**Live:** <https://wasl.hensap.id> · **Repo:** <https://github.com/hendrasaputra/wasl>

---

## 1. Where things stand

| | |
|---|---|
| People | 2,502 |
| Claims | 4,074 — every one re-read from the corpus |
| Parent edges | 2,499 |
| Ṣaḥāba | 443 |
| Biographical entries pinned | 112, for 45 of the 48 Who's who people |
| Summaries | 44, 7,476 words, 398 anchored sentences |
| Languages | English, Indonesian, Malay — complete |
| Data checks | 79 independent + 22 parser regressions |
| Responsive checks | CI: tree phone/tablet/desktop + biography phone |
| Interface | index.html is person-first: search, then one person with their thread of descent (sources on every link), brief, family and the books. tree.html keeps the whole-tree explorer (Sept 2026) |
| Sources | 8 OpenITI texts, pinned by version URI |

Phases 1–8c are done. CI gates every push; `main` deploys after verification.

---

## 2. Running it, from nothing

```bash
git clone https://github.com/hendrasaputra/wasl && cd wasl
./fetch.sh              # ~38MB of Arabic into corpus/ (gitignored, checksummed)
python3 validate.py     # proves every quote. MUST pass before any commit
python3 test_wasl.py    # independent checks. Also must pass
python3 build.py        # regenerates index.html (front door) and tree.html (whole tree)
```

No dependencies beyond Python 3. `python3 -m http.server` and open `index.html` to look at it.

To regenerate the biography pages locally (CI does this on every deploy):

```bash
python3 tools/build_entries.py --write     # re-pin the entries
python3 tools/build_summaries.py --write   # re-check every summary anchor
python3 tools/build_bios.py                # writes bio/*.html
```

---

## 3. The four documents, and what each is for

Keep them apart or they drift.

- **README.md** — what the project is, for a visitor. Public-facing.
- **CLAUDE.md** — the **rules**. Non-negotiables, conventions, the replay pipeline, and every
  hard-won lesson about the parsers. Read this before touching `tools/`.
- **PLAN.md** — the record of what each phase did and why.
- **HANDOFF.md** — this file. Orientation, current state, traps, open threads.

---

## 4. The map

**Source of truth is two files.** Everything else is derived.

```
people.jsonl      identity only - name, sex, kunya, tribe. NO relationships, NO dates
claims.jsonl      every relationship, name, kunya and date, each with work/vol/page/ar/en
```

Everything downstream:

```
sources.tsv       the 8 pinned texts. A claim may only cite a key that appears here
fetch.sh          downloads into corpus/ and verifies the committed SHA256SUMS
nasab.py          corpus access: index / clean / locate / page_text. Shared by everything
validate.py       THE GATE. Re-reads every quote at its cited page
test_wasl.py      the second opinion. Shares no code with the indexer
build.py          people + claims -> index.html and tree.html (committed, so CI can prove them current)
template.html     the front door: one person, their line of descent with the sources on every
                  link, the brief, the family, what the books say. Routes on the hash.
tools/tree_template.html  the whole tree as an explorer, with columns and filters
template.html     the page shell: palette, layout, tree, columns, search, i18n
entries.jsonl     where each Who's who person's biography sits in which book
summaries.jsonl   the hand-written briefs, each sentence anchored to an Arabic phrase
```

`tools/` holds extraction and maintenance. The ones you are most likely to touch:

```
ingest.py         the Store: mint people, add claims, refuse what the corpus lacks
extract_walad.py  the 'fa-walada X: A, B, C' parser that built most of the tree
entries.py        pins each biographical entry, and derives its page span
summaries.py      the summaries themselves (data). summaries_i18n.py holds id/ms
directory.py      the Who's who list, shared by build.py and the kunya passes
i18n.py           interface strings and gloss templates
merge.py          collapse duplicates, cut copied spines, unweld broken chains
prune.py          repair mis-cut names, then drop what was never a name
```

---

## 5. Rules you cannot break

The full list is in CLAUDE.md. The four that matter most:

1. **No uncited assertion.** Every edge, name, kunya and date is a claim with a work, volume,
   page and verbatim Arabic.
2. **Quotes are verbatim from `corpus/`.** Never hand-type Arabic from memory. Copy it out of
   the file. `validate.py` will catch you, but the point is not to need it to.
3. **Never resolve a disagreement by deleting one side.** If the sources differ, record every
   reading. The interface shows all of them.
4. **Never invent a date.** Every date carries a `date_basis`. A blank is correct; a guess is
   not.

And the meta-rule: **model proposes, script verifies, human approves.** A draft that has not
passed `validate.py` is not data.

---

## 6. Traps — read this section twice

Every one of these has already happened here, most of them more than once.

**A plausible name attached to the wrong man is invisible in totals.** It is the recurring
failure of this project. `validate.py` cannot catch it, because the quote genuinely is on the
page. Only reading the output catches it. **Always sample fifteen lines before writing.**

**`nasab.locate()` returns the FIRST occurrence in a work.** Load-bearing in
`build_summaries.py` — an anchor not distinctive enough to sit only in its own entry resolves
elsewhere and fails the span check, which is the point. It also makes `locate()` unsound for
short strings: `عمر بن الخطاب` occurs on hundreds of pages, so `entries.py` derives entry spans
from milestone positions in the file instead, never from a text search.

**The checker can share the bug.** `validate.py` imports `nasab.py`. Twice it has reported a
clean run over wrong data — the repeated page marker in Ibn Saʿd, and `PAGE_RE` reading three
digits of a four-digit milestone, which put **286 claims on a page a tenth of the true one**
while every quote still "verified". Both were found by `test_wasl.py`, which slices the raw
file by hand. **A new check must not import the thing it checks.**

**A one-name chain identifies nobody.** Ask the corpus how ambiguous its own phrase is
(`continuations()`), never the tree. A bare `ولد إبراهيم:` gave the Prophet's infant son six
descendants; Ibn Ḥazm continues that name 55 different ways.

**A partial chain match is a wrong answer, so it must be no answer.** Matching a suffix hung
Qaḥṭānī clans under Quraysh off a stray `Zayd`.

**Order in the pipeline is load-bearing.** `prune` before `merge`: prune *repairs* names, and a
repair can create the duplicate merge exists to see. Run it the other way and ʿAlī ends up with
two sons called ʿUmar.

**A cleanup that deletes the real thing is worse than the mess.** The first `uncopy()` was off
by one and flagged Kināna, Mudrika and al-Naḍr themselves. It was reverted, not trusted.

**The build must be deterministic.** Iterating a `set` made `index.html` different on every
build, because Python randomises string hashing per process — and CI could no longer tell a
stale page from a fresh one. Sort anything unordered before it reaches the page.

**When a parser is wrong, fix the parser and REPLAY.** Patching the output leaves the same
class of error in the thousands of nodes you did not look at. The replay recipe is in
CLAUDE.md and takes about ten minutes.

---

## 7. How to know you have not broken anything

```bash
python3 validate.py && python3 test_wasl.py && python3 build.py
git diff --exit-code index.html tree.html   # must be clean, or you forgot to rebuild
```

For anything touching `build.py` or `template.html`, **prove the output is unchanged** when it
should be:

```bash
cp index.html /tmp/before.html && python3 build.py && diff /tmp/before.html index.html
```

That is not ceremony. A comment-only refactor of the search-index line silently changed 5.6KB
of output; the diff is what caught it.

For an ad-hoc responsive check, add `?responsive-check=1` to a tree or biography URL. The
page records the result on `<html>` as `data-responsive-failed`; CI checks phone, tablet and
desktop tree views plus a phone biography view in headless Chrome.

CI runs all of this on every push, verifies that fetching cannot rewrite the corpus pin, and
refuses to deploy if any data, parser, generated-page or responsive check fails.

---

## 8. Open threads

Nothing here is broken. These are the things worth doing next, with the method for each.

**The biggest untapped seam: mothers.** The corpus carries roughly **6,548 `wa-ummuhu X bint
Y…` formulas** against the 8 `mother_of` claims we hold — 3,645 in Ibn Saʿd alone. The shape is
the same one `extract_walad.py` already parses (a name followed by a chain), so the parser
mostly exists. This would put women into a tree that is male almost by construction.

**One companion still cannot anchor.** `عبادة بن الصامت بن قيس` is reported by
`phase6b_notables.py`, not guessed at. He needs a hand-quoted chain, like the other marquee
names. Zayd b. Thābit and the seven incorrectly male women were resolved by the parser replay.

**al-ʿAbbās b. ʿAbd al-Muṭṭalib has no entry heading** in Usd al-Ghāba or al-Istīʿāb — searched
by name, chain and kunya. The printed books certainly have one; OpenITI's markup never opens
it. He is pinned to Ibn Saʿd alone. If a better version of either text appears, revisit.

**English references were tried and withdrawn.** Guillaume's translation of Ibn Hishām was
pinned and removed; the reasoning is in CLAUDE.md and LICENSING.md §4. **Do not repeat the
attempt on the same archive.org scans.** The short version: 431 leaves for 813 pages means page
boundaries cannot be recovered, the index OCR loses ~40% of entries including nearly everything
under ʿayn, and pinning the headword `Husayn` returned *a poet* while every automated test
passed. If English references are added later they go in as **bibliography**, entered from a
copy in hand and marked unverifiable by script.

**196 transliterations are provisional** — the consonant-skeleton fallback, flagged in the data
and badged in the page. Adding readings to `tools/translit.py` and re-running
`tools/retranslit.py --write` reduces the count.

**`build.py:main()` is 371 lines** and stays that way by decision. It is eight banner-marked
stages, listed in the module docstring. If you ever split it, prove `index.html` is
byte-identical.

---

## 9. What was proven, and what was not

Say this accurately, in commits and to users alike.

`validate.py` proves the **quote**: the Arabic really is on the page cited. It cannot prove the
**placement** — that the man a parser anchored a chain to is the man the text meant.
Parser-placed claims carry `source_pattern` and their nodes are badged `auto` in the page.
**Never describe an `auto` node as verified without that distinction.**

The summaries prove that every sentence points at text that exists where it says. They do not
prove the English renders the Arabic fairly. That is a human judgement, which is why the page
shows every anchor.
