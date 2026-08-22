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

### Phase 2 — Quraysh — next
Descendants of Quṣayy and ʿAbd Manāf, from Ibn Hishām, Ibn Saʿd vol. 1, and Ibn Ḥazm (whose
*Jamhara* is organised exactly this way). ~300 nodes. This is the trunk every Ṣaḥābī hangs off,
and the first phase where the tree actually branches — the renderer already handles it.

### Phase 3 — Ṣaḥāba
al-Istīʿāb and Usd al-Ghāba, whose entries each open with a nasab chain in a formulaic
`X بن Y بن Z` shape. `tools/extract_chain.py` already parses that shape; the loop is
propose → `validate.py` proves the quote → human approves the diff. 5–10k nodes.

### Phase 4 — tribal breadth
al-Balādhurī and Ibn al-Kalbī beyond Quraysh.

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

- `index.html` as one self-contained file holds to roughly 5–10k nodes. Past that, render
  children on click from the JSONL instead of baking them into the page. Bites in Phase 3.
- Arabic renders in whatever naskh face the reader's OS provides. Embedding Amiri would cost
  ~300 KB and make the file certain rather than likely. Worth doing when the project is shared.
- `validate.py` scans each work linearly. Fine at 177 claims; index once and reuse if Phase 3
  makes it slow.

## Deliberately not built

GEDCOM export (~40 lines, worth it once there is breadth to export). SQLite (add when a question
arrives that the tree cannot answer — "all Ṣaḥāba descended from ʿAbd Manāf who died before 40
AH"). Any server, framework, or dependency.
