# Nasab Explorer — Plan

## 0. Finding: the sources are already machine-readable (verified today)

All four kitab are in the [OpenITI corpus](https://github.com/OpenITI/RELEASE) as plain-text
Arabic with `PageV##P###` milestones tied to a named critical edition. Verified by pulling the
metadata index and downloading Ibn Hisham:

| Work | OpenITI version URI | Edition | tokens |
|---|---|---|---|
| Sira (Ibn Hisham) | `0213IbnHisham.SiraNabawiyya.Shamela0023833-ara1` | al-Saqqa / al-Abyari / al-Shalabi, Halabi, Cairo | 278,907 |
| Sira (Ibn Ishaq, Zakkar recension) | `0151IbnIshaq.Sira.Shamela0009862-ara2` | Suhayl Zakkar, Dar al-Fikr, Beirut 1978 | 70,453 |
| Tabaqat al-Kubra (Ibn Sa'd) | `0230IbnSacd.TabaqatKubra.ShamAY0035884-ara1` | Ali Muhammad Umar, al-Khanji, Cairo 2001 | 1,167,652 |
| Ansab al-Ashraf (al-Baladhuri) | `0279Baladhuri.AnsabAshraf.Shamela0009773-ara1` | Zakkar & al-Zirikli, Dar al-Fikr, Beirut | 1,104,613 |
| al-Isti'ab (Ibn Abd al-Barr) | `0463IbnCabdBarr.IsticabFiMacrifatAshab.JK000778-ara1` | al-Bajawi, Dar al-Jil, Beirut 1412 | 395,221 |
| Usd al-Ghaba (Ibn al-Athir) | `0630IbnAthirCizzDin.UsdGhaba.Shamela0023700-ara1` | Dar al-Fikr, Beirut 1989 | 934,287 |

Proof the pipeline works — first lines of the Sira, page anchors intact:

```
### | ذكر سرد النسب الزكي من محمد صلى الله عليه وآله وسلم، إلى آدم عليه السلام
# هذا كتاب سيرة رسول الله ... قال: محمد بن عبد الله
~~ابن عبد المطلب، واسم عبد المطلب: شيبة بن هاشم، واسم هاشم: عمرو بن
~~عبد مناف، واسم عبد مناف: المغيرة بن قصي، (واسم قصي: زيد) بن كلاب بن
~~مرة بن كعب بن لؤي بن غالب بن فهر بن مالك بن النضر PageV01P001
```

That single passage already yields ~42 nodes, the alias equations
(`عبد المطلب = شيبة`, `هاشم = عمرو`, `عبد مناف = المغيرة`, `قصي = زيد`), and
exact vol/page citations. **Requirement 1 is mechanically satisfiable, not honor-system.**

## 1. Data model — claim-based, not fact-based

A person node stores **no relationships and no dates**. Every edge, name, and date is a
*claim* carrying its citation. This is what makes rules 1 and 2 automatic instead of a
discipline problem, and it is the only way to represent ikhtilaf without picking a winner.

Two git-tracked JSONL files. Human-diffable, no database server.

**`people.jsonl`** — identity only
```json
{"id":"p.abd-al-muttalib","ism_ar":"عبد المطلب","ism_lat":"ʿAbd al-Muṭṭalib","sex":"M","tribe":"Quraysh/Hashim","sahabi":false}
```

**`claims.jsonl`** — everything else, one line per sourced assertion
```json
{"cid":"c0007","type":"father_of","subject":"p.hashim","object":"p.abd-al-muttalib",
 "work":"IbnHisham.Sira","ed":"al-Saqqa/al-Abyari/al-Shalabi, Halabi, Cairo","vol":1,"page":1,
 "loc":"0213IbnHisham.SiraNabawiyya.Shamela0023833-ara1@PageV01P001",
 "ar":"واسم عبد المطلب: شيبة بن هاشم",
 "en":"the name of ʿAbd al-Muṭṭalib is Shayba son of Hāshim",
 "grade":"explicit"}
```

`type`: `father_of | mother_of | name | kunya | laqab | alias | birth | death | age_at_death | tribe | dissent`
`grade`: `explicit` (text states it) | `inferred` (chain position implies it) | `dissent` (source contradicts another)

Dates get an extra field, and this is the part that must not be fudged:

`date_basis`: `attested` | `derived_from_age_at_death` | `generation_estimate` | `unknown`

## 2. `validate.py` — the check that makes the whole thing trustworthy

Because the corpus files are downloadable and pinned by commit SHA, the validator can
**re-read the cited page and confirm the Arabic quote actually appears there**. Run it in
CI or as a pre-commit hook.

1. every person has ≥1 `name` claim
2. every `father_of`/`mother_of` edge has ≥1 claim with non-empty `ar`, `en`, `vol`, `page`, `loc`
3. **every `ar` string is found in the corpus file at the cited page milestone** ← the real guarantee
4. no cycles in the parent graph; no orphan claim ids
5. `work` is one of the whitelisted version URIs

Rule 2 ("any addition must carry full references") becomes a failing test, not a policy.

## 3. Platform: one Python script → one static HTML file

```
corpus/          pinned .txt from OpenITI (fetch.sh, ~15 MB, gitignored)
people.jsonl     source of truth
claims.jsonl     source of truth
validate.py      the check above
build.py         reads the two JSONL, writes nasab.html
nasab.html       self-contained, open in a browser or drop on GitHub Pages
```

- **Tree** = nested `<details>` elements. Native HTML, unlimited depth, zero JS to expand, works with browser Ctrl-F, and prints. No tree library.
- **Search** = ~20 lines of JS filtering a name index (Arabic + transliteration + kunya), auto-opening ancestors of hits.
- **Citations** = click a node, a side panel lists every claim about them with Arabic (`dir="rtl"`), English, work, editor, vol:page, and the OpenITI locator.
- **Disputed edges** render dashed with the competing claims side by side (needed immediately: `عدنان بن أدد` vs `عدنان بن أد` appears on page 2).

No server, no framework, no build tooling, no SQLite. Add SQLite only when you want queries the
tree can't answer ("all sahabah descended from Abd Manaf who died before 40 AH").

`ponytail:` single-file HTML holds to ~5–10k nodes; past that, ship the JSONL alongside and
lazy-render children on click.

## 4. Phases

| # | Scope | Nodes | Why |
|---|---|---|---|
| 0 | `fetch.sh` + `validate.py` + 3 hand-entered nodes | 3 | prove the quote-verification loop |
| 1 | Muhammad → Adnan → Adam, Ibn Hisham vol 1 pp. 1–2 | ~42 | already extracted above; ships a real explorer in a day |
| 2 | Quraysh: Qusayy / Abd Manaf descendants, Ibn Hisham + Ibn Sa'd vol 1 | ~300 | the trunk every sahabi hangs off |
| 3 | Sahabah from al-Isti'ab + Usd al-Ghaba (each entry opens with a nasab chain) | 5–10k | the long tail |
| 4 | Baladhuri for tribal breadth beyond Quraysh | + | widest coverage |

**Extraction method.** Nasab chains are formulaic — `X بن Y بن Z`. A ~50-line regex splitter on
`بن / ابن / بنت / واسم` gets most chains mechanically. Use a script to *propose* rows, `validate.py`
to *prove the quote exists*, and a human to *approve the diff*. Never let a model be the final
authority on a citation.

## 5. Honest conflicts with the requirements

1. **Birth years barely exist in these four books.** Death years are common; birth is almost always
   back-computed from "he died aged 63". Requirement 5 will be mostly *derived*, not sourced —
   hence `date_basis`. For pre-Adnan ancestors, nothing is attested; either leave blank or show a
   generation estimate (~25–30 yrs) clearly marked as computed. Do not print a number that looks sourced.
2. **Adnan → Ibrahim is contested.** Ibn Hisham gives the chain, but there is a well-known position
   (and a report from the Prophet himself) to stop at Adnan. Model as `dissent`, render dashed, never flatten.
3. **Women are sparsely recorded.** Mothers appear selectively. Expect a lopsided tree; do not infer a
   mother who isn't named.
4. **Same person, many names.** `عبد المطلب = شيبة`. Canonical id + `alias` claims, each cited.
5. **Hijri↔Gregorian**: tabular Islamic calendar, ±1 day. Fine at year granularity. Label pre-Hijra as BH.

## 6. Suggestions beyond the ask

- **Add two dedicated genealogy books.** Your four are sira/tabaqat/rijal works where nasab is
  incidental. Both of these are *about* nasab and far denser — and both are already in the corpus:
  - `0204IbnKalbi.JamharatAnsab` — Ibn al-Kalbi, d. 204 AH, the foundational Arab genealogy
  - `0456IbnHazm.JamharatAnsab` — Ibn Hazm, d. 456 AH, systematic and well-indexed
- **GEDCOM export** — ~40 lines, gives you free interop with every existing genealogy tool.
- **Pin the corpus by git commit SHA** so a citation can never silently drift.
- **Amiri or Scheherazade for Arabic** — embed the font rather than a CDN link, keeps the file offline-capable.
- **Publish `nasab.html` as an Artifact** for a shareable private link, no hosting setup.

## 7. Open question

Phase 1 (Muhammad → Adam, 42 nodes, fully cited, working HTML explorer) is about a day's work and
proves every requirement end to end. Start there, or go straight to Phase 2 breadth?
