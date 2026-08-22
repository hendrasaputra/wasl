# Wasl · وصل

**A verifiable, expandable genealogy (nasab) explorer built directly on the primary Arabic sources.**

*waṣl* — "the link, the joining". Every link in this tree is joined to a page of a printed
critical edition, and the join is checked by machine, not by trust.

**Phase 1 is complete: the lineage of the Prophet Muḥammad ﷺ back to Ādam — 50 generations,
52 persons, 177 sourced claims drawn from 7 primary works, every Arabic quotation re-read out of
the source text at the cited page.**

Open [`index.html`](index.html) in any browser. No server, no build step, no network.

---

## What makes it verifiable

Most genealogy projects store facts. Wasl stores **claims**. A person record holds identity
only — name, sex, tribe. Every relationship, every second name, every date is a separate row that
carries its own citation:

```json
{"cid":"c00003","type":"father_of","subject":"p.abd-al-muttalib","object":"p.abd-allah",
 "work":"IbnHisham","vol":1,"page":1,"page_end":1,
 "ar":"عبد الله ابن عبد المطلب، واسم عبد المطلب: شيبة",
 "en":"ʿAbd Allāh son of ʿAbd al-Muṭṭalib","grade":"explicit"}
```

Then `validate.py` **re-reads the cited page in the pinned source file and fails if the Arabic
string is not there.** A quote that cannot be found is not a citation, so it cannot be committed.
This has already caught three quotes drafted from a noisier copy of al-Istīʿāb; they were
re-taken from the pinned text.

Two consequences fall out for free:

- **Disagreement is data, not a problem.** Sources differ constantly. Wasl never resolves a
  disagreement by deleting one side — every reading becomes its own claim, and the interface
  shows them together. Mudrika is `ʿĀmir` in Ibn Hishām and `ʿAmr` in Ibn Saʿd and Ibn al-Kalbī;
  the tree shows `= ʿĀmir / ʿAmr` and the panel gives you all three quotations.
- **Corroboration is measurable.** `validate.py` reports how many independent works attest each
  link. See "What the data says" below — the answer is interesting.

## The sources

Eight machine-readable texts from the [OpenITI corpus](https://github.com/OpenITI), each pinned
to a named printed edition with real volume and page numbers. Seven are cited in Phase 1.

| Key | Work | Author (d. AH) | Edition |
|---|---|---|---|
| `IbnHisham` | al-Sīra al-Nabawiyya | ʿAbd al-Malik b. Hishām (213) | al-Saqqā, al-Abyārī & al-Shalabī — al-Ḥalabī, Cairo |
| `IbnIshaq` | al-Siyar wa-l-Maghāzī | Muḥammad b. Isḥāq (151) | Suhayl Zakkār — Dār al-Fikr, Beirut 1398/1978 |
| `IbnKalbi` | Jamharat al-Nasab | Hishām b. Muḥammad al-Kalbī (204) | Shamela |
| `IbnSad` | al-Ṭabaqāt al-Kubrā | Muḥammad b. Saʿd (230) | ʿAlī Muḥammad ʿUmar — al-Khānjī, Cairo 1421/2001 |
| `Baladhuri` | Ansāb al-Ashrāf | Aḥmad b. Yaḥyā al-Balādhurī (279) | Zakkār & al-Ziriklī — Dār al-Fikr, Beirut |
| `IbnHazm` | Jamharat Ansāb al-ʿArab | ʿAlī b. Aḥmad b. Ḥazm (456) | Dār al-Kutub al-ʿIlmiyya, Beirut |
| `IbnAbdAlBarr` | al-Istīʿāb fī Maʿrifat al-Aṣḥāb | Yūsuf b. ʿAbd al-Barr (463) | al-Bajāwī — Dār al-Jīl, Beirut 1412 |
| `IbnAlAthir` | Usd al-Ghāba fī Maʿrifat al-Ṣaḥāba | ʿAlī b. Muḥammad b. al-Athīr (630) | Dār al-Fikr, Beirut 1409/1989 |

The four you named are all here. Three were added and are worth saying why:

- **Ibn al-Kalbī, *Jamharat al-Nasab* (d. 204)** and **Ibn Ḥazm, *Jamharat Ansāb al-ʿArab*
  (d. 456)** are books *about* genealogy, where the other five mention it in passing. Ibn
  al-Kalbī is the earliest systematic Arab genealogist and the source Ibn Saʿd cites by name for
  the Prophet's nasab; leaving him out would mean citing him at second hand.
- **Ibn Isḥāq (d. 151)** is included for completeness, but note: Zakkār's recension in the corpus
  does **not** carry the opening nasab. Ibn Isḥāq's chain survives through Ibn Hishām, who names
  his isnād for it — `IbnHisham` 1:3 — and that quotation is stored as an `isnad` claim so the
  transmission is visible rather than assumed.

## What the data says

`validate.py` counts, without being asked to, how many works independently attest each link:

| Independent works | Links | Which part of the chain |
|---|---|---|
| 5 | 5 | Muḥammad → ʿAbd Manāf |
| 4 | 16 | Quṣayy → ʿAdnān |
| 2 | 10 | Nūḥ → Ādam, and Mudrika → ʿAdnān in Ibn Ḥazm |
| 1 | 20 | **ʿAdnān → Ibrāhīm → Ādam — Ibn Hishām only** |

That is not a gap in the collection. It is the finding, and the sources say so themselves. Wasl
records eight separate objections, including:

> كذب النسابون — *the genealogists have lied*
> — the Prophet, on going beyond Maʿadd b. ʿAdnān. Ibn Saʿd 1:38, Ibn al-Kalbī 1:1;
> al-Balādhurī 1:12 places the stopping point one step higher, at Udad.

Ibn ʿAbd al-Barr and Ibn al-Athīr both decline to give the chain above ʿAdnān at all. Ibn Saʿd
gives **four mutually incompatible chains** from ʿAdnān to Ismāʿīl — of 3, 40, 18 and 8
generations — then concludes one should stop at ʿAdnān. All four are stored in full, each with
its isnād. Ibn ʿAbd al-Barr and Ibn Saʿd both transmit "thirty forefathers between Maʿadd and
Ismāʿīl", against the seven Ibn Hishām names.

So the page shows the Ibn Hishām chain to Ādam, because that is what the text says, and marks
every step of it above ʿAdnān as single-source with the objections attached. Nothing is smoothed.

## On dates

Requirement: each node carries a birth year in AD and Hijrī. **These books do not supply one.**
They date by event, not by year, and no ancestor above the Prophet has an attested birth year
anywhere in the seven works. Wasl will not print a number that looks sourced when it is not, so
every date claim carries a `date_basis`:

| `date_basis` | Meaning |
|---|---|
| `attested` | a year stated in the text |
| `attested_relative` | dated to an event, not a year (`ʿĀm al-Fīl`) |
| `derived_from_age_at_death` | back-computed from a stated age |
| `generation_estimate` | computed from generation count — not from any text |
| `unknown` | the sources are silent |

The Prophet's birth is `attested_relative` — *ʿĀm al-Fīl*, the Year of the Elephant (Ibn Saʿd
1:81; Ibn ʿAbd al-Barr "there is no disagreement" 1:30, alongside four competing readings of the
day and interval, all recorded). The conventional 570 CE / 53 BH equation is stored explicitly
labelled as a modern equation, not as something the text says. Every other node reads
*"born · no year in these sources"*, which is the truthful answer.

## What is and is not verified

**Verified by machine, on every run:** that each Arabic quotation appears in the pinned source
text at the volume and page the claim cites; that no claim references an unknown person or an
undeclared work; that the parent graph has no cycles and no person has two different fathers;
that no date carries an unrecognised basis. `test_wasl.py` re-derives page boundaries from the
raw file *without* sharing code with the indexer, and confirms the checker actually rejects a
fabricated quote and a wrong page number.

**Not verified, and not claimable:** that the digitised text matches the paper edition
character for character. Page numbers are those recorded in the OpenITI/Shamela transcription of
the named print edition. Two evident printing or transcription errors met so far are flagged in
`text_note` rather than silently corrected. Translations are ours and are not machine-checkable;
the Arabic sits beside every one of them so the reader can judge.

## Layout

```
sources.tsv      the eight texts: version URI, download URL, author, editor, edition
fetch.sh         downloads them into corpus/ and writes SHA256SUMS
corpus/          the pinned texts (gitignored; SHA256SUMS is committed)
people.jsonl     source of truth - identity only
claims.jsonl     source of truth - every relationship, name and date, each with its citation
nasab.py         corpus index: resolves a quote to its true volume and page span
validate.py      the proof. Must pass before every commit
build.py         renders index.html
template.html    the page shell: palette, layout, tree and citation-panel behaviour
tools/           one-shot helpers used to draft Phase 1 (not sources of truth)
index.html       generated, committed, self-contained
```

## Use

```bash
./fetch.sh && python3 validate.py && python3 build.py
```

`fetch.sh` needs the network once; nothing else ever does. `validate.py` is the gate — if it
fails, the data is wrong, not the checker.

## The interface

- **The tree is nested `<details>`** — native HTML, so it expands to unlimited depth, survives
  browser Ctrl-F, and prints. Indentation appears only where the line actually forks, because a
  lineage is mostly a single file and a 50-level staircase is unreadable.
- **Search** folds Latin diacritics, Arabic ḥarakāt and the alif/hamza families, so `mughira`,
  `Mughīra`, `قصى` and `قصي` all find their man.
- **Click any name** for every claim about them, grouped: descent, second names, birth, the full
  chain as each source gives it, competing chains, and where the sources object — each with the
  Arabic, an English translation, the isnād where one is given, the editor, the volume and page,
  and the OpenITI version URI.

## Where this goes next

Phase 1 is the spine. The structure carries straight into breadth:

| Phase | Scope | Est. nodes |
|---|---|---|
| 1 ✅ | Muḥammad → Ādam | 52 |
| 2 | Quraysh: descendants of Quṣayy and ʿAbd Manāf — Ibn Hishām, Ibn Saʿd, Ibn Ḥazm | ~300 |
| 3 | Ṣaḥāba from al-Istīʿāb and Usd al-Ghāba — each entry opens with a nasab chain | 5–10k |
| 4 | Tribal breadth beyond Quraysh — al-Balādhurī, Ibn al-Kalbī | + |

`index.html` holds comfortably to roughly 5–10k nodes as one file. Past that, children render on
click from the JSONL rather than being baked into the page.

## Adding to it

Read [CLAUDE.md](CLAUDE.md) first — it holds the rules that keep the data trustworthy. In short:
never assert without a citation, never hand-type Arabic, never delete one side of a
disagreement, never invent a date, and never commit without `validate.py` passing.
