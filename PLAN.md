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
| 2 ✅ | Quraysh, under Fihr b. Mālik | ~760 | parser |
| 3 ✅ | Banū Hāshim and the household | 24 | hand |
| 4 ✅ | The Ṣaḥāba, from the two companion dictionaries | — | parser |
| 5 ✅ | Qaḥṭān and the tribes, to al-Aws and al-Khazraj | ~2,600 | parser + hand-seeded spine |
| 6 ✅ | The Anṣār clans and the companions that could not anchor | ~500 | parser |
| — ✅ | Marquee companions introduced by kunya | 13 | hand |

**Current: 3,865 persons · 5,407 claims · 3,867 links · 459 Ṣaḥāba · 7 works.**

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

- `index.html` is ~4 MB at 3,865 nodes and renders in one paint. It holds to roughly 10k. Past
  that, render children on click from the JSONL instead of baking them into the page.
- Transliteration of unvocalised Arabic cannot be solved, only widened: **379 of 3,865** names
  still fall back to a consonant skeleton, flagged `translit_provisional`. Each reading added to
  `tools/translit.py` reduces the count.
- `tools/prune.py` recognises misparses by shape, which is a heuristic and always will be. It
  repairs before it prunes and protects hand-seeded spines; an early draft's length rule would
  have deleted Udd and Murr with 203 descendants.
- Only **20 women** are in the tree. The `bint` fix removed the structural cause; the remaining
  limit is that most women in the companion dictionaries have fathers not yet anchored.

## What remains

Not a Phase 7 so much as more of Phase 6: each hand-seeded trunk unlocks a further tranche of
companion entries that previously had nothing to anchor to. Purely additive — nothing already in
the file has to change. Beyond that: GEDCOM export (~40 lines), and more transliteration
readings.
