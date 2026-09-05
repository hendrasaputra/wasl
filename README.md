# Wasl · وصل

**A verifiable, expandable genealogy (nasab) built directly on the primary Arabic sources.**

*waṣl* — "the link, the joining". Every link in this tree is joined to a page of a printed
critical edition, and the join is checked by machine, not by trust.

**2,502 persons · 4,074 sourced claims · 2,499 links · 7 primary works** — the lineage of the
Prophet Muḥammad ﷺ back to Ādam, his household, 443 Ṣaḥāba, and the Arab tribes down to
al-Aws and al-Khazraj on the Qaḥṭānī side. Every Arabic quotation is re-read out of the source
text at the cited page before the page is written.

**Live at [wasl.hensap.id](https://wasl.hensap.id)** — or open [`index.html`](index.html) in any
browser. No server, no build step, no network.

[![verify](https://github.com/hendrasaputra/wasl/actions/workflows/verify.yml/badge.svg)](https://github.com/hendrasaputra/wasl/actions/workflows/verify.yml)

Every push re-fetches the pinned texts, re-proves all 4,074 quotations against them, runs 79
independent checks plus 22 parser regressions, checks four responsive viewports, and fails if
the published page is stale. See [DEPLOY.md](DEPLOY.md).

---

## What makes it verifiable

Most genealogy projects store facts. Wasl stores **claims**. A person record holds identity
only — name, sex, tribe. Every relationship, second name, kunya and date is a separate row
carrying its own citation:

```json
{"cid":"c00003","type":"father_of","subject":"p.abd-al-muttalib","object":"p.abd-allah",
 "work":"IbnHisham","vol":1,"page":1,"page_end":1,
 "ar":"عبد الله ابن عبد المطلب، واسم عبد المطلب: شيبة",
 "en":"ʿAbd Allāh son of ʿAbd al-Muṭṭalib","grade":"explicit"}
```

Then `validate.py` **re-reads the cited page in the pinned source file and fails if the Arabic
string is not there.** A quote that cannot be found cannot be committed.

Two consequences fall out for free:

- **Disagreement is data.** Wasl never resolves a disagreement by deleting one side. Mudrika is
  `ʿĀmir` in Ibn Hishām and `ʿAmr` in Ibn Saʿd and Ibn al-Kalbī; the tree shows `= ʿĀmir / ʿAmr`
  and the panel gives all three quotations. Zayd b. Thābit is reported as Abū Saʿīd, Abū Khārija
  *and* Abū ʿAbd al-Raḥmān — all three kept.
- **Corroboration is measurable.** `validate.py` reports how many independent works attest each
  link, unprompted.

## The sources

Eight machine-readable texts from the [OpenITI corpus](https://github.com/OpenITI), each pinned
to a named printed edition with real volume and page numbers. Seven are cited.

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

Ibn al-Kalbī and Ibn Ḥazm were added because they are books *about* genealogy, where the others
mention it in passing. Ibn Isḥāq is pinned for completeness, but Zakkār's surviving recension
does **not** carry the opening nasab: Ibn Isḥāq's chain reaches us through Ibn Hishām, whose
isnād for it is stored as its own claim rather than assumed.

## How the tree was built

Phase 1 and the household were typed by hand. The rest could not be — the books hold tens of
thousands of names — so two parsers do most of the work: `fa-walada X: A, B, C` (Ibn Ḥazm and
Ibn al-Kalbī are built almost entirely of it) and the nasab chain that opens every entry in the
two companion dictionaries.

| Phase | Scope | Method |
|---|---|---|
| 1 | Muḥammad ﷺ → Ādam, 50 generations | hand |
| 2 | Quraysh, under Fihr b. Mālik | parser |
| 3 | Banū Hāshim and the household | hand |
| 4–6 | Ṣaḥāba, Qaḥṭān and the tribes, the Anṣār clans | parser |
| — | Marquee companions introduced by kunya | hand |

Parsing genealogy is mostly the problem of **not inventing relatives**. Every guard below was
added because a sample of fifteen lines caught the draft failing:

- **A chain resolves only if the whole chain matches one path already in the tree.** Suffix
  matching hung Qaḥṭānī clans under Quraysh off a stray `Zayd`.
- **Ask the corpus how ambiguous its own phrase is.** `Quṣayy b. Kilāb` has one continuation;
  `Muḥammad b. ʿAbd Allāh` has 32 in Ibn Saʿd alone, so a bare mention identifies nobody.
  Without this, three other men's sons were attached to the Prophet.
- **A one-name chain resolves on uniqueness inside the declared trunk**, so a disputed eponym
  is not mistaken for a common name.
- **Honorifics are not names.** `rasūl Allāh wa-sayyid walad Ādam` is one man under two
  epithets; splitting it on the *wa-* invented a son called Sayyid for the Prophet's father.
- **`bint` is a link in a chain exactly as `bn` is.** Leaving it out of the splitter hung
  granddaughters on their grandfathers.
- **Spines are seeded by hand**; parsers grow outward from them, never inward to them.

**What this costs.** Ibn Ḥazm alone yielded 2,056 people under Fihr with a loose resolver and
116 with the strict one. Recall is sacrificed to precision on purpose; rejected statements are
counted and reported, never guessed at.

## What is proven, and what is not

**Machine-checked on every run:** that each Arabic quotation appears in the pinned text at the
volume and page cited; that no claim references an unknown person or undeclared work; that the
parent graph has no cycles and no double fathers; that no date carries an unrecognised basis.
`test_wasl.py` re-derives page boundaries from the raw files *without* sharing code with the
indexer, and confirms the checker actually rejects a fabricated quote and a wrong page.

**Not proven:** that a parser-placed node sits under the right man. Its quotation is verified —
the Arabic really is on that page — but the **placement rests on the anchor**, which the machine
cannot confirm. 3,846 of 4,074 claims are parser-placed; their nodes are badged **`auto`** in
the page itself, not only here. Hand-seeded spines, Phase 1, Phase 3 and the notables carry no
badge. **Treat the badge as the boundary between proven and inferred.**

Also not claimable: that the digitised text matches the paper edition character for character.
Page numbers are those of the OpenITI/Shamela transcription of the named print edition. Evident
printing or transcription errors met so far are flagged in `text_note` rather than silently
corrected. Translations are ours and are not machine-checkable; the Arabic sits beside every one.

### The core family is checked name by name

A parser error anywhere is bad; one in the Prophet's own family is the project failing at the
thing it exists for. `test_wasl.py` asserts:

| | Children | |
|---|---|---|
| ʿAbd Allāh b. ʿAbd al-Muṭṭalib | **1** | Muḥammad, and nothing else — as Ibn Ḥazm says outright, *lam yakun li-ʿAbd Allāh walad ghayruhu* |
| ʿAbd al-Muṭṭalib | **16** | the ten sons and six daughters Ibn Hishām names — 10 male, 6 female |
| The Prophet ﷺ | **7** | al-Qāsim, Zaynab, Ruqayya, Fāṭima, Umm Kulthūm, ʿAbd Allāh, Ibrāhīm |
| Abū Ṭālib | **4** | Ṭālib, ʿAqīl, Jaʿfar, ʿAlī |

plus: no person's name may contain an honorific, and none may be an unsplit chain. Every one of
these was written because the data had broken it.

## What the sources say about themselves

`validate.py` counts how many independent works attest each link:

| Independent works | Links |
|---|---|
| 7 | 1 |
| 6 | 3 |
| 5 | 19 |
| 4 | 35 |
| 3 | 131 |
| 2 | 658 |
| 1 | 3,013 |

The deepest corroboration sits on the Prophet's own line. The twenty links from ʿAdnān up to
Ādam rest on Ibn Hishām alone — **and that is the finding, not a gap.** Wasl records eleven
objections, including:

> كذب النسابون — *the genealogists have lied*
> — the Prophet, on going beyond Maʿadd b. ʿAdnān. Ibn Saʿd 1:38, Ibn al-Kalbī 1:1;
> al-Balādhurī 1:12 places the stop one step higher, at Udad.

Ibn ʿAbd al-Barr and Ibn al-Athīr both decline the chain above ʿAdnān. Ibn Saʿd gives **four
mutually incompatible chains** from ʿAdnān to Ismāʿīl — of 3, 40, 18 and 8 generations — then
concludes one should stop at ʿAdnān. All four are stored in full with their isnāds.

## On dates

The requirement was a birth year on every node. **These seven works do not supply one.** They
date by event, not by year, and no ancestor above the Prophet carries an attested birth year in
any of them. Rather than print a computed number that reads as sourced, every date claim carries
a `date_basis`: `attested`, `attested_relative`, `derived_from_age_at_death`,
`generation_estimate`, or `unknown`.

The Prophet's birth is `attested_relative` — *ʿĀm al-Fīl* — with the conventional 570 CE / 53 BH
equation stored and explicitly labelled a modern equation. Every other node reads
*"born · no year in these sources"*, which is the truthful answer.

## Why bands and not centuries

A natural request is to cut the tree into eras — Ādam to Ibrāhīm, Ibrāhīm to Mūsā, and so on.
Three things rule it out:

1. **No attested years above the Prophet**, so a band would be computed by us and would read as
   though it came from the sources.
2. **Mūsā and ʿĪsā are not in this tree.** The line runs Ibrāhīm → **Ismāʿīl**; Moses and Jesus
   descend through Isḥāq, a branch these works do not carry.
3. **Depth is not date across branches.** Generation 47 on the ʿAbbāsid line is the 8th century
   CE; generation 47 on a Tamīmī line is not.

So the bands are four things the sources themselves state or do — **a filter, not a period**:

| Band | Count | Basis |
|---|---|---|
| beyond the attested chain | 29 | At or above ʿAdnān and Qaḥṭān — where these books decline to vouch |
| the Arab genealogy | 2,206 | Below ʿAdnān or Qaḥṭān, no companion recorded above |
| companions | 459 | Carries an entry in al-Istīʿāb or Usd al-Ghāba |
| recorded below a companion | 1,171 | Largely the Umayyad, ʿAbbāsid and ʿAlid lines |

## The interface

The data is **deep and narrow** — 53 generations, only ten nodes with more than eight children.
A full dendrogram or 53-ring radial layout would be impractical. So the
problem was never seeing breadth, it was **reaching** a name fifty levels down, and the work
went into navigation.

- **Two views.** *Tree* (nested `<details>` — unlimited depth, browser Ctrl-F, prints) and
  *Columns* (Miller columns: one column per generation, but only a five-wide window around the
  selection, with the generations above folded into a back-column). Bounded by the viewport
  rather than by the data.
- **Indentation diminishes with depth.** 25 forks at a flat 28px put the deepest name 570px
  from the margin — most of a phone screen, a third of a desktop column. The step now shrinks in
  bands (13 → 10 → 9 → 7px), which cuts the deepest indent from 570px to 267px and takes the
  tree's own horizontal scroll from 335px to nothing at 1440px. Every level still steps right of
  its parent, so the tree never becomes ambiguous about who descends from whom — asserted,
  362/362 pairs. On a phone the whole tree is additionally scaled (`zoom: .86`), which reflows
  rather than merely painting smaller, so names, rules and indent come down together and a name
  keeps 52% of the width even at the deepest node.
- **Linear runs are ribbons.** Any chain of single-child links folds to one line: 209 ribbons
  absorb ~950 rows. Lossless — a run of one child has no branching to lose. A fork of two or
  three does, so forks always keep a branching layout.
- **Search returns a list, not a count.** Ninety-one men here are called ʿAbd Allāh; each hit
  carries its own line of descent, so they are told apart at a glance. Enter jumps, opening only
  the line to the hit.
- **Search by kunya.** 253 sourced kunyas on 161 people. `abu hafs` returns ʿUmar b. al-Khaṭṭāb
  alone; `أبا حفص`, `أبي حفص` and `أبو حفص` all reach him.
- **Who's who** — 48 people a reader actually arrives looking for, resolved at build time.
- **A breadcrumb** showing the full line, compressed to first five and last five with an
  expandable middle.
- **Counts on the `+`**, so you know whether it opens two names or 1,200.
- Search folds Latin diacritics, Arabic ḥarakāt and the alif/hamza families.

**On a phone** the citation panel becomes a bottom sheet — tap a name and it slides up over the
tree, dismissed by the close button, the backdrop, a downward swipe or Escape. The header prose
and the filter rows fold behind disclosures, bringing the chrome above the first name from 855px
to 198px on an iPhone 17 and from 989px to 198px on a Galaxy S24. Miller columns show one column
at a time, as they do natively on a phone. Every control clears a 44px target, the search input
is 16px so iOS does not zoom on focus, and safe-area insets keep the notch and home indicator off
the content. `tools/check_responsive.js` asserts all of it rather than trusting the eye.

## Languages

English, **Bahasa Indonesia** and **Bahasa Melayu**, chosen from the header and remembered
between visits. Everything moves: chrome, panel headings, band labels and their explanations,
filter chips, node badges, the footer, and the gloss under every quotation.

Two rules govern the translations:

- **The Arabic is never translated away.** It is the evidence, and it sits beside every gloss in
  whatever language is chosen. Switching language changes only the reading aids.
- **Templated glosses are generated from structure, not translated from the English.** 3,718
  descent glosses and 253 kunyas are of the form "X, son of Y" — a relation between two named
  people, which every language can state directly. Rendering them through English first would
  let a translation of a translation drift for no reason. Only the 33 bespoke prose lines — the
  objections, the competing chains, the birth notices — are hand-translated, and those from the
  Arabic. Coverage is 4,074 of 4,074; the generator exits nonzero and refuses to write if a
  translation is missing.

Indonesian and Malay differ where they genuinely differ (*putra/putri* against *putera/puteri*,
*Pohon* against *Pokok*, *tsabit* against *sabit*) and coincide where they do.

## The Ummahāt al-Muʾminīn

A tree of fathers cannot reach a wife: marriage is not descent, and no *fa-walada* line leads
to one. Ibn Saʿd and Ibn Hishām both set the wives out in a dedicated chapter with each
woman's full paternal nasab, so `tools/phase7_wives.py` quotes those chapters by hand rather
than parsing them. Twelve women, each anchored by the chain her book prints, each carrying a
`married_to` claim quoted from the marriage sentence itself.

`married_to` is deliberately not a tree edge. Placing a wife under her husband would make the
page assert that she descends from him, so it is indexed separately and shown as its own row
on both panels.

Their fathers mostly lie outside what the parsers built — Banū Asad b. Khuzayma, ʿĀmir b.
Ṣaʿṣaʿa, Khuzāʿa and the Jewish Banū al-Naḍīr are neither Quraysh nor Anṣār — so where a
chain finds nothing to hang on, its own top name becomes a root. That is the honest outcome:
an early draft matched Ṣafiyya bt. Ḥuyayy's chain on the single name *al-Naḍīr* and hung the
Prophet's Jewish wife inside Quraysh, because the al-Naḍīr in the tree is al-Naḍīr b.
al-Ḥārith of ʿAbd al-Dār. Below three names the corpus decides how ambiguous its own phrase
is; the tree does not get a vote.

**The count is disputed and stays disputed.** Ibn Hishām: nine survived him, thirteen in all.
Ibn Saʿd, in one chapter, reports thirteen (his informants leaving Rayḥāna out), fourteen and
fifteen. All five readings are recorded as claims against the Prophet; none is chosen. Ibn
Saʿd's own chapter divisions are followed — the women he places among those married but not
brought together, and those proposed to but never married, are not here.

## The biographical entries

The tree gives edges. A life is prose, and these books keep it in a named entry — a numbered
notice in Usd al-Ghāba and al-Istīʿāb, a `dhikr X` chapter in Ibn Saʿd's first volume for the
men who died before Islam. [`entries.jsonl`](entries.jsonl) pins **112 entries for 45 of the
48 Who's who people — 255,220 words**, and each Who's who row opens onto the entry itself at
the pages cited.

Arabic only. Nothing on those pages is translated or summarised; the reading aids are page
anchors and a dimmed isnād, and names in the running text are deliberately **not** linked into
the tree, because matching a name in prose to a person is the one thing this project has got
wrong most often.

They are **built in CI and deployed from the artifact, never committed**. A quarter of a
million words of OpenITI's Arabic in the repository would vendor the corpus by the back door,
and [LICENSING.md](LICENSING.md) says Wasl does not. The staging step deletes `corpus/` and
`refs/` and fails if either survives.

Three people have no entry and say so: Qaḥṭān, al-Aws and al-Khazraj are eponyms, not men
with a life. al-ʿAbbās b. ʿAbd al-Muṭṭalib has none in Usd al-Ghāba or al-Istīʿāb either —
OpenITI's markup never opens one for him, though the printed books do.

## The summaries

All 44 biography pages open with a brief written from the entry below them — and nowhere else.
**7,476 words, 412 sentences, 398 of them anchored.**
It is the only composed prose on the site, so it carries its evidence with it: **every
sentence but the marked editorial ones is anchored to the Arabic phrase it rests on**, and
"show what each sentence rests on" puts that phrase under the sentence. `validate.py` re-reads
each anchor at the pages cited; `test_wasl.py` re-reads it again independently and checks that
a real phrase from a *different* entry is rejected.

That proves each statement points at text that is really there. It does not prove the English
renders the Arabic fairly — that is a human judgement, and the anchors are shown so it can be
checked by eye.

Where an entry contradicts itself, the summary says so rather than choosing. Ibn Saʿd gives
Ṣafiyya's death as the year 50 and, in the closing line of the same chapter, as 52; ʿAlī says
Abū Bakr was the first to gather the Qurʾān and Ibn Sīrīn says he died without gathering it;
Anas served the Prophet ten years, nine years, and from the age of eight. Ibn al-Athīr carries
two readings of ʿUmar's mother's name that turn on one letter — and decide whether she was
Abū Jahl's sister or his cousin.

The summaries are also the one place where Indonesian and Malay are **translated from the
English**, because here the English is the original rather than a gloss of Arabic. Everywhere
else a gloss is generated per language from the structured fields; see
[CLAUDE.md](CLAUDE.md).

## Taking this over

If you are picking the project up — human or agent — start with
[HANDOFF.md](HANDOFF.md): where things stand, how to run it, the traps that keep recurring,
and what is worth doing next. [CLAUDE.md](CLAUDE.md) holds the rules.

## Reading these books in English

There is no complete English translation of **Usd al-Ghāba** or **al-Istīʿāb**, which carry
most of the entries above. What exists covers the other two:

- A. Guillaume, *The Life of Muhammad* (Oxford, 1955) — Ibn Hishām, complete.
- S. Moinul Haq and H. K. Ghazanfar, *Kitāb al-Ṭabaqāt al-Kabīr* I–II — Ibn Saʿd on the
  Prophet and his forefathers.
- Aisha Bewley, *The Women of Madina* — Ibn Saʿd's volume of women, abridged.
- Ella Landau-Tasseron, *The History of al-Ṭabarī* vol. 39 (SUNY, 1998) — a different work,
  but a biographical dictionary of the same people.

Wasl deliberately cites **none of these per person**. Each translates a different edition, so
no volume or page number transfers to the ones cited here, and `validate.py` cannot open a
printed book to check a claim about one. An unverifiable citation is the thing this project
exists to avoid, so the list stays general. [LICENSING.md](LICENSING.md) records the attempt
that was made and withdrawn.

## Layout

```
sources.tsv      the eight texts: version URI, URL, author, editor, edition
fetch.sh         downloads them into corpus/ and verifies the committed SHA256SUMS
corpus/          the pinned texts (gitignored; SHA256SUMS is committed)
people.jsonl     source of truth — identity only
claims.jsonl     source of truth — every relationship, name, kunya and date, each cited
nasab.py         corpus index: resolves a quote to its true volume and page span
validate.py      the proof. Must pass before every commit
test_wasl.py     79 independent checks, sharing no code with the indexer
test_parsers.py  22 focused parser regressions
build.py         renders index.html (front door) and tree.html (whole tree)
template.html    the page shell: palette, layout, views, search
tools/           extraction and maintenance; the replay pipeline is in CLAUDE.md
index.html       generated, committed, self-contained — one person, their thread, the books
tree.html        generated, committed — the whole tree as an explorer
```

## Use

```bash
./fetch.sh                      # once; needs the network
python3 validate.py             # the gate
python3 test_wasl.py            # independent checks
python3 build.py                # regenerate index.html and tree.html
```

## Licence

Source code is **GPL-3.0-or-later** ([LICENSE](LICENSE)). The Arabic quotations belong to
authors dead between 151 and 630 AH and are public domain; the corpus texts are OpenITI's and
are fetched, not vendored. See [LICENSING.md](LICENSING.md) — the distinction matters if you
redistribute.

## Contributing

Read [CLAUDE.md](CLAUDE.md) first — it holds the rules that keep the data trustworthy: never
assert without a citation, never hand-type Arabic, never delete one side of a disagreement,
never invent a date, always sample the output before writing, and never commit without
`validate.py` and `test_wasl.py` passing.
