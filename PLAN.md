# Wasl · وصل — Plan and record

Living document. What was decided and why stays here, so nothing is re-argued.

---

## Goal

A visual, searchable, indefinitely expandable genealogy of the Prophet Muḥammad ﷺ and the
Ṣaḥāba, where every assertion is traceable to a page of a printed critical edition of a primary
Arabic source, and the trace is verified by machine.

## Requirements, and how each is met

| # | Requirement | Status |
|---|---|---|
| 1 | Every reference validated to the original Arabic, quoted with translation | ✅ `validate.py` re-reads the cited page; a quote that cannot be found cannot be committed |
| 2 | Any change or addition must carry full references | ✅ the citation *is* the row; there is no schema position for an uncited assertion |
| 3 | Expandable to unlimited depth | ✅ 56 generations; bounded by the data, not the renderer |
| 4 | Easy to explore by search or clicking | ✅ diacritic-folding search over names, kunyas and aliases; results list with lineage; two views |
| 5 | Node = name, kunya, birth year AD + Hijrī, M/F | ⚠️ name, kunya, laqab, sex, tribe: yes. **Birth year: the sources do not give one** — see *On dates* |

## Decisions that carried the project

**Claim-based, not fact-based.** A person row holds identity only. Every edge, alias, kunya and
date is a separate claim carrying `work`, `vol`, `page`, `ar`, `en`. This makes requirements 1
and 2 structural rather than a matter of discipline, and it is the only model that holds
*ikhtilāf* without picking a winner.

**The validator re-reads the source.** Because the corpus is pinned and downloadable,
`validate.py` proves every quotation is really at the cited page. This is the difference between
a citation and a claim to have one.

**`test_wasl.py` shares no code with the indexer.** `validate.py` could otherwise agree with its
own bug — which is exactly how the repeated-page-marker bug in Ibn Saʿd was found.

**Two JSONL files in git; the HTML is generated and committed.** Human-diffable source of truth,
browsable artefact, Python standard library only, no dependencies.

**Precision over recall, deliberately.** Guards are listed in CLAUDE.md. Ibn Ḥazm alone yielded
2,056 people under Fihr with a loose resolver and 116 with the strict one; most of the
difference would have been wrong.

## Phases

| # | Scope | Added | Method |
|---|---|---|---|
| 1 ✅ | Muḥammad ﷺ → Ādam, 50 generations | 52 | hand |
| 2 ✅ | Quraysh, under Fihr b. Mālik | ~400 | parser |
| 3 ✅ | Banū Hāshim and the household | 24 | hand |
| 4 ✅ | The Ṣaḥāba, from the two companion dictionaries | — | parser |
| 5 ✅ | Qaḥṭān and the tribes, to al-Aws and al-Khazraj | ~1,200 | parser + hand-seeded spine |
| 6 ✅ | The Anṣār clans and the companions that could not anchor | ~260 | parser |
| — ✅ | Marquee companions introduced by kunya | 13 | hand |

**Current: 1,957 persons · 2,986 claims · 1,959 links · 219 Ṣaḥāba · 7 works.**

## The bugs worth not relearning

Each of these was invisible in the totals and obvious in fifteen sampled lines.

1. **Suffix chain matching** hung Qaḥṭānī clans under Quraysh off a stray `Zayd`. A chain now
   resolves only if the *whole* chain matches one path.
2. **`Muḥammad b. ʿAbd Allāh` identifies nobody** — 32 continuations in Ibn Saʿd alone. Three
   other men's sons had been attached to the Prophet. Fixed by asking the corpus how ambiguous
   its own phrase is.
3. **`aliases_of` was O(people × claims)**, turning a run into a ten-minute hang. Indexed.
4. **A four-name anchor gate** meant a four-name chain could never anchor at all, silently
   skipping most of the companion dictionary.
5. **One spelling variant duplicated a whole branch.** `Rawāḥ`/`Rizāḥ` b. ʿAdī made every chain
   through them ambiguous, so ʿUmar b. al-Khaṭṭāb could never attach. `tools/merge.py` collapses
   these on evidence — one letter apart *and* two children in common.
6. **The child splitter took only the first name per clause**, so `walada al-Khazraj: ʿAmr,
   ʿAwf, Jusham, Kaʿb, al-Ḥārith` yielded one son instead of five — and with it the Anṣār clan
   structure most Ṣaḥāba hang from.
7. **Honorifics were split for names.** `rasūl Allāh wa-sayyid walad Ādam` invented a son
   called Sayyid for the Prophet's father; `ṣallā Allāhu ʿalayhi wa-sallam` gave ʿAlī a son
   called Salm.
8. **`bint` was missing from the chain splitter**, so every `X bint Y b. Z` was read as one long
   name and hung on Z instead of Y — granddaughters sitting under their grandfathers, sexed
   male. This also kept the tree at 16 women when the sources name far more.
9. **A probe must begin a chain.** `Fihr b. Mālik` occurs inside a hundred longer chains;
   reading the kunya after one of them gave Fihr someone else's kunya.

Bugs 7 and 8 corrupted the Prophet's immediate family, were reported by the user, and were
fixed at the parser followed by a full replay from the hand-seeded base — not patched in the
output. `test_wasl.py` now asserts the core family name by name.

## On dates

The requirement asks for a birth year in AD and Hijrī. **These seven works do not supply one.**
They date by event, not year, and no ancestor above the Prophet carries an attested birth year
in any of them. Every date claim therefore carries a `date_basis`, and every other node reads
*"born · no year in these sources"*. This is the one requirement the sources refuse, and the
refusal is itself worth displaying.

## Interface decisions

The data is deep and narrow — 56 generations, only ten nodes with more than eight children. A
left-to-right dendrogram would be 8,400px wide and a radial layout would need 56 rings, so both
were rejected **on the shape of the data, not on taste**. The work went into reaching a name,
not into drawing the whole shape: a results list carrying each hit's lineage, a compressed
breadcrumb, ribbons for linear runs, Miller columns as a bounded horizontal view, subtree counts,
a Who's who, and source-grounded bands rather than invented centuries.

## Ceilings, and when they bind

- `index.html` is ~2 MB at 1,957 nodes and renders in one paint. It holds to roughly 10k. Past
  that, render children on click from the JSONL instead of baking them into the page.
- Transliteration of unvocalised Arabic cannot be solved, only widened: **175 of 1,957** names
  still fall back to a consonant skeleton, flagged `translit_provisional`. Each reading added to
  `tools/translit.py` reduces the count.
- `tools/prune.py` recognises misparses by shape, which is a heuristic and always will be. It
  repairs before it prunes and protects hand-seeded spines; an early draft's length rule would
  have deleted Udd and Murr with 203 descendants.
- Only **17 women** are in the tree. The `bint` fix removed the structural cause; the remaining
  limit is that most women in the companion dictionaries have fathers not yet anchored.

## Responsive: built

Measured, not guessed, on iPhone 17 (393×852) and Galaxy S24 (360×780).

| | iPhone 17 | Galaxy S24 |
|---|---|---|
| Chrome above the first name | 855px — **100% of the screen** | 989px — **127%** |
| Filter chips wrap into | 6 rows | 7 rows |
| Citation panel starts at | y = 6,811px | worse |
| Tree horizontal scroll | 641px | ~670px |
| Deepest row indent | 514px on a 393px screen | 514px |
| Miller columns visible at once | 1.8 | 1.6 |
| Smallest tap target | 34px (WCAG wants 44) | 34px |

The desktop layout does not degrade on a phone, it inverts: **you scroll a full screen of
chrome before seeing a single name, and the citation panel — the entire point of the project —
sits below a 3,500px tree, so in practice it cannot be reached at all.**

### 1. The panel must stop being a second grid row  *(the one structural change)*

At ≤760px the panel becomes a **bottom sheet**: hidden until a name is tapped, then sliding up
over the tree to about 70% height, with a grab handle, a close control, and dismissal by swipe
or backdrop tap. The tree stays where it was, scroll position intact.

Rejected alternatives: a full-screen overlay loses the tree and makes comparing siblings a
round trip; Tree/Details tabs put the citations behind a mode switch, and the citations are the
product. A sheet keeps both on one screen and is what a phone user already expects.

### 2. Collapse the chrome from ~900px to ~120px

- **Header** → a compact bar: title, the live counts, and an **About** disclosure holding the
  three explanatory paragraphs. They are worth reading once, not on every visit.
- **Filters** → one `Filter` button opening a sheet, instead of six rows of chips. The active
  filter shows as a count on the button.
- **Keep visible**: search (full width), the Tree/Columns toggle, the breadcrumb.
- Breadcrumb compresses harder on narrow screens: first 2 and last 2 rather than 5 and 5.

### 3. Tree and columns

- Indent 12px → 8px per level, and cap total indent; ribbons already absorb the long runs.
  `#tree` keeps `overflow-x:auto` so the page itself never scrolls sideways.
- **Columns view shows one column at a time** on a phone — which is the native Miller-column
  behaviour on iOS Files — with the breadcrumb as the back affordance.

### 4. Touch, safe areas, and iOS quirks

- Every control to a 44×44px minimum hit area; rows to 40px.
- `viewport-fit=cover` plus `env(safe-area-inset-*)` padding, so the notch and the home
  indicator do not sit on top of content.
- Search input font-size ≥16px, otherwise iOS Safari zooms the page on focus and never zooms
  back.
- `-webkit-overflow-scrolling` and `overscroll-behavior: contain` on the sheet so its scroll
  does not chain to the page.
- Replace the hardcoded `top:110px` sticky offsets with a CSS variable set per breakpoint;
  they currently assume the desktop toolbar height and will mis-stick on any other.

### 5. Verification — `tools/check_responsive.js`

Same discipline as the data: measure, do not eyeball. Load it in the page and call
`waslResponsiveCheck()` at each width.

| Viewport | Chrome above the first name | Result |
|---|---|---|
| iPhone 17 · 393×852 | 855px → **198px** | 11/11 |
| Galaxy S24 · 360×780 | 989px → **198px** | 11/11 |
| iPad portrait · 768×1024 | — | 5/5 |
| Desktop · 1440×900 | unchanged | 3/3 |

Indentation was measured separately and cut afterwards: 25 fork levels at a flat 28px reached
570px, halved to 305px by a diminishing scale, with the tree's horizontal scroll going from
335px to 0 at 1440px. The check asserts both the bound and that every child still indents right
of its parent — a diminishing scale is only safe while it stays strictly monotonic.

Two things the check caught that inspection had not:

- **A dead zone at 768px.** The grid collapses to one column at 1100px but the sheet only
  began at 760px, so an iPad in portrait put the panel back under the tree at y=5592 —
  the original unreachable-panel bug, in a narrower window. The sheet breakpoint now *is* the
  grid breakpoint; any gap between them reintroduces it.
- **A race in the check itself.** The sheet animates over 280ms, so measuring straight after
  the click read a mid-transition position and reported a failure that was not there. The
  check now disables the transition while measuring.

## Phase 7 — the Ummahāt al-Muʾminīn

Twelve wives, hand-quoted from Ibn Saʿd's *dhikr azwāj rasūl Allāh* and Ibn Hishām's chapter,
each with the paternal nasab her book gives and a `married_to` claim taken from the marriage
sentence. A new claim type that is not a tree edge, a `force=True` root for the chains whose
tribes the parsers never reached, and 16 new checks in `test_wasl.py` asserting each woman by
name, by sex, and by the fact that no marriage became descent. See README for why Ṣafiyya bt.
Ḥuyayy must not resolve inside Quraysh.

The books disagree on the count in the same breath — nine, thirteen, fourteen, fifteen — and
every reading is recorded rather than reconciled.

## Phase 8a — where the biographies are

112 entries pinned by hand for 45 people, 255,221 words, spans derived from milestone
positions rather than text search. Bio pages built in CI, deployed from the artifact, never
committed. `references.tsv` pins Guillaume — fetched to locate a page, never quoted.

Found on the way: `PAGE_RE` read three digits of a page milestone, so 286 published claims
named a page a tenth of the true one. Fixed and re-derived; `test_wasl.py` guards it.

Next: 8b hand-verifies Guillaume page ranges per person; 8c writes the anchored summaries.

## Phase 8c — the summaries

44 briefs, 7,476 words, 412 sentences of which 398 carry the Arabic phrase they rest on.
Every anchor re-read from its own entry by `validate.py` and again, independently, by
`test_wasl.py`. Indonesian and Malay complete: 412/412.

## What remains

Not a Phase 8 so much as more of Phase 6: each hand-seeded trunk unlocks a further tranche of
companion entries that previously had nothing to anchor to. Purely additive — nothing already in
the file has to change. Beyond that: GEDCOM export (~40 lines), and more transliteration
readings.
