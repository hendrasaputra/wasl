# CLAUDE.md — working rules for this repository

## What this is
A verifiable genealogy (nasab) explorer. Source of truth is two JSONL files; the HTML is
generated output. Everything asserted must be traceable to an Arabic primary text.

## Non-negotiable rules

1. **No uncited assertion.** Every parent edge, name, alias, kunya and date lives in
   `claims.jsonl` with `work`, `ed`, `vol`, `page`, `loc`, `ar` and `en`. A person row in
   `people.jsonl` carries identity only — no relationships, no dates.
2. **Quotes must be verbatim from `corpus/`.** `validate.py` re-reads the cited page in the
   pinned OpenITI text and fails if the Arabic string is not there. Never hand-type Arabic
   from memory; copy it out of the corpus file.
3. **Never resolve a disagreement by deleting one side.** If sources differ, add every
   reading as its own claim and link them with `variant_of`. The UI shows all of them.
4. **Never invent a date.** Every date claim carries `date_basis`:
   `attested` | `derived_from_age_at_death` | `generation_estimate` | `unknown`.
   If the source gives no year, the field stays empty. A blank is correct; a guess is not.
5. **New source ⇒ new row in `sources.tsv`** with version URI, URL, editor and edition, and a
   re-run of `fetch.sh`. No claim may cite a work absent from `sources.tsv`.
6. **Model proposes, script verifies, human approves.** An LLM may draft rows. `validate.py`
   decides whether they are real. Never let a draft land without a passing validate.

## Workflow
```
./fetch.sh          # pull pinned corpus into corpus/ (gitignored, checksummed)
python3 validate.py # MUST pass before every commit
python3 build.py    # regenerate nasab.html
```
`nasab.html` is generated and committed so the repo is browsable without a toolchain. Never
hand-edit it — edit `build.py` or the JSONL.

## Conventions
- Person ids: `p.` + lowercase ALA-LC-ish slug, hyphens (`p.abd-al-muttalib`).
- Claim ids: `c` + 5 digits, never reused after deletion.
- Transliteration: ALA-LC with diacritics (`ʿAbd al-Muṭṭalib`, `Muḥammad`).
- Arabic strings in JSONL are stored exactly as they appear in the corpus, minus mARkdown
  markers (`#`, `~~`, `PageV..`, `ms\d+`) and with newlines collapsed to single spaces.
- Commit at every stage. Message body states what was verified, not just what changed.

## Corpus gotchas
- OpenITI mARkdown: `#` starts a paragraph, `~~` continues it, `### |` is a heading,
  `PageV01P002` is a milestone placed at the **end** of the page it closes, `ms0031` is a
  Shamela milestone and is noise for our purposes.
- Text quality varies between versions of the same edition. `IbnAbdAlBarr` deliberately uses
  `Shamela0012288` rather than `JK000778`: same Bajawi edition, same pagination, far fewer
  OCR errors. Check quality before adding a version.
- Ibn Isḥāq's own recension in the corpus (Zakkār's *Siyar wa-Maghāzī*) does **not** contain
  the opening nasab. Ibn Isḥāq's chain survives through Ibn Hishām, who names his isnād for
  it explicitly. Cite it as Ibn Hishām transmitting from al-Bakkāʾī from Ibn Isḥāq.
