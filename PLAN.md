# Wasl · وصل — Plan

Living document. Phase status is updated as each stage lands; the record of what was decided and
why stays, so nothing has to be re-argued.

---

## Goal

A visual, searchable, indefinitely expandable genealogy of the Prophet Muḥammad ﷺ and the
Ṣaḥāba, where every assertion is traceable to a page of a printed critical edition of a primary
Arabic source, and the trace is verified by machine.

## Requirements, and how each is met

| # | Requirement | How |
|---|---|---|
| 1 | Every reference validated to the original Arabic, quoted with translation | Claim-based data model + `validate.py` re-reads the cited page in the pinned corpus text. A quote that cannot be found cannot be committed. |
| 2 | Any change or addition must carry full references | The citation is not metadata on the fact — it *is* the row. There is no schema position in which an uncited assertion can be written. |
| 3 | Expandable to unlimited depth | Nested `<details>`; depth is bounded by the data, not the renderer. |
| 4 | Easy to explore by search or by clicking | Diacritic-folding search across Arabic and transliteration; click any node for its full citation panel. |
| 5 | Node = name, kunya, birth year AD + Hijrī, M/F | Name, kunya, laqab, sex, tribe: yes. Birth year: the sources do not give one — see **On dates** below. Never faked. |

## Decisions

**Claim-based, not fact-based.** A person row holds identity only. Every edge, alias, kunya and
date is a separate claim carrying `work`, `vol`, `page`, `ar`, `en`. This is what makes
requirements 1 and 2 structural rather than a matter of discipline, and it is the only model that
can hold *ikhtilāf* without picking a winner.

**The validator re-reads the source.** Because the corpus files are pinned and downloadable,
`validate.py` proves every Arabic quotation is really at the cited page. This is the difference
between a citation and a claim to have one. It has already rejected three quotes drafted from a
noisier copy of al-Istīʿāb.

**Nested `<details>`, no framework.** Native expansion at any depth, works with browser Ctrl-F,
prints, needs no server. Indentation only at real branch points — a lineage is mostly one line,
and 50 levels of staircase is unreadable.

**Two JSONL files in git, generated HTML committed.** Human-diffable source of truth; the
artefact is browsable with no toolchain. No database server, no build tooling, no dependencies —
Python standard library only.

## Phases

### Phase 0 — corpus ✅
`sources.tsv` pins 8 OpenITI texts by version URI, URL, author, editor and edition. `fetch.sh`
downloads and checksums them. Verified the nasab passage is locatable in each.

### Phase 1 — Muḥammad → Ādam ✅
**52 persons · 177 claims · 7 works · 51 links · every quote machine-verified.**

Delivered: `nasab.py` (corpus index resolving a quote to its true page span, including quotes
that straddle a page break), `validate.py`, `build.py` + `template.html`, `index.html`,
`tools/extract_chain.py` and `tools/seed_phase1.py`.

Corroboration as measured, not as hoped:

| Independent works | Links | Stretch |
|---|---|---|
| 5 | 5 | Muḥammad → ʿAbd Manāf |
| 4 | 16 | Quṣayy → ʿAdnān |
| 2 | 10 | Nūḥ → Ādam; Mudrika → ʿAdnān in Ibn Ḥazm |
| 1 | 20 | ʿAdnān → Ibrāhīm → Ādam, Ibn Hishām only |

Ikhtilāf captured rather than flattened: 9 dissent claims (including *kadhaba al-nassābūn* from
Ibn Saʿd, Ibn al-Kalbī and al-Balādhurī — who places the stop one step higher, at Udad; plus Ibn
ʿAbd al-Barr and Ibn al-Athīr each declining the chain above ʿAdnān), 9 competing chains
(including Ibn Saʿd's four incompatible ʿAdnān→Ismāʿīl chains of 3, 40, 18 and 8 generations, and
al-Balādhurī's al-Zuhrī variant for Nūḥ→Ādam), and 17 alias claims (Mudrika as ʿĀmir in Ibn
Hishām against ʿAmr in Ibn Saʿd and Ibn al-Kalbī; ʿAbd al-Muṭṭalib as Shayba, Shaybat al-Ḥamd,
and ʿĀmir — the last reported by Ibn ʿAbd al-Barr and rejected by him in the same sentence).

Two printing errors in the editions are flagged in `text_note` rather than silently corrected.

### Phase 2 — Quraysh ✅
**+116 persons.** Everything the books hang under Fihr b. Mālik, which Ibn Ḥazm defines as
exactly the set of people called Qurashī. Built the extraction engine: `tools/translit.py`,
`tools/ingest.py`, `tools/extract_walad.py` for the `fa-walada X: A, B, C` shape.

The engine's three precision rules were each added because a fifteen-line sample caught the
draft failing — see **Precision** below. The loose resolver produced 2,056 people under Fihr;
the strict one produces 116, and a large share of the other 1,940 would have been wrong.

### Phase 3 — Banū Hāshim and the household ✅
**+24 persons, 16 women now in the tree.** Hand-authored, not parsed: `fa-walada Muḥammad b.
ʿAbd Allāh` names a different man on nearly every page, so the extractor is right to refuse it
and the Prophet's own children have to come from passages that name him unmistakably.

ʿAbd al-Muṭṭalib's ten sons and six daughters (Ibn Hishām 1:108); the Prophet's seven children
(Ibn Saʿd 1:110); Ibrāhīm by Māriya (al-Istīʿāb 1:53); Abū Ṭālib's four sons (al-Balādhurī);
al-Ḥasan, al-Ḥusayn, al-Muḥsin, Zaynab and Umm Kulthūm by Fāṭima (Ibn Ḥazm 1:15); Khadīja bt.
Khuwaylid, joining the household back into the Quraysh trunk.

The birth order of the Prophet's children is recorded twice and the two disagree; both are kept.
`build.py` now hangs a child on its mother where the books name no father, badged *via mother*.

### Phase 4 — the Ṣaḥāba ✅
**+653 persons.** `tools/extract_entry.py` reads the shape both companion dictionaries share:
an entry opens with a full nasab chain, which is a ladder down from someone the tree already
holds. 11,805 entries scanned, 335 anchored over four rounds.

The attach rate is low for a reason worth stating: most Ṣaḥāba are Anṣār, and Qaḥṭān was not in
the tree yet.

### Phase 5 — Qaḥṭān and the tribes ✅
**+812 persons; 1,657 total.** Qaḥṭān is seeded as a **root**, not hung under Sām or Ismāʿīl:
al-Balādhurī gives three incompatible origins for him and Ibn Ḥazm says outright that nothing
above him is sound. All three are stored as claims; none becomes a tree edge. It is the Yemeni
counterpart of the ceiling at ʿAdnān.

The spine from Qaḥṭān down to al-Aws and al-Khazraj is hand-seeded from two sentences in Ibn
Hishām, for the same reason Phase 1 was: without a correct backbone the parser anchors onto the
wrong man. An earlier run hung al-Aws on a `al-Ḥārith b. Qaḥṭān` — visible in a sample, never in
the totals.

Three engine fixes: an O(people × claims) alias scan that turned a run into a ten-minute hang
(now indexed, 0.7 s per pass); one-name chains resolving on uniqueness *within the declared
trunk*; entry anchors requiring four names rather than three.

## Precision

Recall is sacrificed to precision deliberately. The rules that do it:

1. **A chain resolves only if the whole chain matches one path in the tree.** A suffix match is
   a wrong answer, so it must be no answer.
2. **Ask the corpus how ambiguous its own phrase is.** `Quṣayy b. Kilāb` has one continuation;
   `Muḥammad b. ʿAbd Allāh` has 32 in Ibn Saʿd alone. Correctly refuses `Hāshim b. ʿAbd Manāf`,
   since Ibn Ḥazm records two of them.
3. **A one-name chain resolves on uniqueness inside the declared trunk**, so a disputed eponym
   is not mistaken for a common name.
4. **Spines are hand-seeded**; parsers grow outward from them, never inward to them.
5. **Always sample before writing.** Every bug above was invisible in the totals and obvious in
   fifteen sampled lines.

### What remains uncertain
A parser-placed node is badged `auto` and carries `source_pattern`. Its quotation is verified —
the Arabic really is on that page. Its *placement* rests on the anchor being the right man,
which the machine cannot prove. 2,065 of 2,312 claims are parser-placed. The badge is the
boundary between what is proven and what is inferred, and it is in the page, not just the docs.

### Next
Not a Phase 6 so much as more of Phase 4: each hand-seeded trunk unlocks a further tranche of
companion entries that previously had nothing to anchor to. Additive — nothing already in the
file has to change.

## On dates

The requirement asks for a birth year in AD and Hijrī on every node. **These seven works do not
supply one.** They date by event, not by year, and no ancestor above the Prophet carries an
attested birth year in any of them. Rather than print a computed number that reads as sourced,
every date claim carries `date_basis`: `attested`, `attested_relative`,
`derived_from_age_at_death`, `generation_estimate`, or `unknown`. The Prophet's birth is
`attested_relative` — *ʿĀm al-Fīl* — with the conventional 570 CE / 53 BH equation stored and
explicitly labelled a modern equation. Every other node reads *"born · no year in these
sources"*.

This is the one requirement the sources refuse, and the refusal is itself worth displaying.

## Ceilings, and when they bind

- `index.html` is 1.8 MB at 1,657 nodes: one paint, 4 ms search, 22 ms to open a citation
  panel. It holds to roughly 5–10k nodes. Past that, render children on click from the JSONL
  instead of baking them into the page.
- Transliteration of unvocalised Arabic cannot be solved, only widened: 715 of 1,657 names fall
  back to a consonant skeleton and are flagged `translit_provisional`. Each name added to the
  dictionary in `tools/translit.py` reduces the count. The Arabic is always authoritative.
- Arabic renders in whatever naskh face the reader's OS provides. Embedding Amiri would cost
  ~300 KB and make the file certain rather than likely. Worth doing when the project is shared.
- `validate.py` re-reads all 2,312 quotes in a few seconds. Quote lookups are cached; if a
  later phase makes it slow, the index is the thing to reuse across works.

## Deliberately not built

GEDCOM export (~40 lines, worth it once there is breadth to export). SQLite (add when a question
arrives that the tree cannot answer — "all Ṣaḥāba descended from ʿAbd Manāf who died before 40
AH"). Any server, framework, or dependency.
