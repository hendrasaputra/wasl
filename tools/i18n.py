# SPDX-License-Identifier: GPL-3.0-or-later
# Wasl - a verifiable nasab. Copyright (C) 2026 Hendra Saputra.
"""Interface strings and gloss templates for English, Indonesian and Malay.

Two rules here:

  * The Arabic is always primary and is never translated away. A gloss is a reading aid; the
    quotation beside it is the evidence.
  * Templated glosses are GENERATED from the structured fields in each language, not translated
    from the English. A translation of a translation drifts, and there is no reason to accept
    that when the underlying fact is 'X, son of Y' and every language can say it directly.

Indonesian and Malay are close but not identical - putra/putri against putera/puteri, and
Malay prefers 'keturunan' where Indonesian takes 'keturunan' too but 'sumber' differs in
register. Where they genuinely coincide the strings are simply the same.
"""

LANGS = {"en": "English", "id": "Bahasa Indonesia", "ms": "Bahasa Melayu"}

# ---- gloss templates -------------------------------------------------------
GLOSS = {
    "son_of":      {"en": "{a} son of {b}",       "id": "{a}, putra {b}",   "ms": "{a}, putera {b}"},
    "daughter_of": {"en": "{a} daughter of {b}",  "id": "{a}, putri {b}",   "ms": "{a}, puteri {b}"},
    "mother_of":   {"en": "{a}, mother of {b}",   "id": "{a}, ibu dari {b}","ms": "{a}, ibu kepada {b}"},
    "kunya":       {"en": "is given the kunya {k}",
                    "id": "diberi kunyah {k}", "ms": "diberi kunyah {k}"},
    "alias":       {"en": "{a}, also called {k}",
                    "id": "{a}, disebut juga {k}", "ms": "{a}, disebut juga {k}"},
    "chain":       {"en": "Full chain as given: {a} back to {b}.",
                    "id": "Rantai lengkap sebagaimana disebutkan: {a} hingga {b}.",
                    "ms": "Rantaian lengkap sebagaimana disebut: {a} hingga {b}."},
}

# ---- interface -------------------------------------------------------------
UI = {
 "search_ph":   {"en": "Search {n} names — Arabic or transliteration",
                 "id": "Cari {n} nama — Arab atau transliterasi",
                 "ms": "Cari {n} nama — Arab atau transliterasi"},
 "tree":        {"en": "Tree", "id": "Pohon", "ms": "Pokok"},
 "columns":     {"en": "Columns", "id": "Kolom", "ms": "Lajur"},
 "collapse":    {"en": "Collapse", "id": "Tutup", "ms": "Tutup"},
 "filter":      {"en": "Filter", "id": "Saring", "ms": "Tapis"},
 "filter_to":   {"en": "Filter to", "id": "Saring ke", "ms": "Tapis kepada"},
 "clear":       {"en": "clear", "id": "hapus", "ms": "kosongkan"},
 "whoswho":     {"en": "Who's who", "id": "Tokoh utama", "ms": "Tokoh utama"},
 "about":       {"en": "About this", "id": "Tentang ini", "ms": "Mengenai ini"},
 "close":       {"en": "Close", "id": "Tutup", "ms": "Tutup"},
 "matches":     {"en": "{n} matches", "id": "{n} hasil", "ms": "{n} padanan"},
 "match_1":     {"en": "1 match", "id": "1 hasil", "ms": "1 padanan"},
 "nomatch":     {"en": "no match", "id": "tidak ada hasil", "ms": "tiada padanan"},
 "more_narrow": {"en": "{n} more — narrow the search",
                 "id": "{n} lagi — persempit pencarian", "ms": "{n} lagi — perincikan carian"},
 "noname":      {"en": "No name matches.", "id": "Tidak ada nama yang cocok.",
                 "ms": "Tiada nama yang sepadan."},
 "pick":        {"en": "Select a name to see every source that attests it.",
                 "id": "Pilih sebuah nama untuk melihat semua sumber yang menyebutkannya.",
                 "ms": "Pilih satu nama untuk melihat semua sumber yang menyebutnya."},
 "above":       {"en": "{n} above", "id": "{n} di atas", "ms": "{n} di atas"},
 "roots":       {"en": "roots · {n}", "id": "akar · {n}", "ms": "akar · {n}"},
 "gen_short":   {"en": "{n} gen", "id": "{n} gen", "ms": "{n} gen"},
 "nobranch":    {"en": "{n} generations, no branching",
                 "id": "{n} generasi, tanpa percabangan", "ms": "{n} generasi, tanpa cabang"},
 # node badges
 "b_nabi":      {"en": "nabī", "id": "nabi", "ms": "nabi"},
 "b_ikhtilaf":  {"en": "ikhtilāf", "id": "ikhtilāf", "ms": "ikhtilāf"},
 "b_f":         {"en": "f", "id": "p", "ms": "p"},
 "b_viamother": {"en": "via mother", "id": "lewat ibu", "ms": "melalui ibu"},
 "b_auto":      {"en": "auto", "id": "otomatis", "ms": "automatik"},
 "b_sahabi":    {"en": "ṣaḥābī", "id": "sahabat", "ms": "sahabat"},
 "b_src":       {"en": "src", "id": "sbr", "ms": "sbr"},
 "b_auto_t":    {"en": "attached by the chain parser: the quote is verified, the placement "
                       "rests on the anchor being right",
                 "id": "dipasang oleh pengurai rantai: kutipannya terverifikasi, penempatannya "
                       "bergantung pada ketepatan titik sambung",
                 "ms": "dipasang oleh penghurai rantaian: petikannya disahkan, penempatannya "
                       "bergantung pada ketepatan titik sauh"},
 # panel
 "g_father_of": {"en": "Descent", "id": "Keturunan", "ms": "Keturunan"},
 "g_mother_of": {"en": "Mother", "id": "Ibu", "ms": "Ibu"},
 "g_chain":     {"en": "Full chain as given", "id": "Rantai lengkap", "ms": "Rantaian lengkap"},
 "g_kunya":     {"en": "Kunya", "id": "Kunyah", "ms": "Kunyah"},
 "g_alias":     {"en": "Second names and epithets", "id": "Nama lain dan julukan",
                 "ms": "Nama lain dan gelaran"},
 "g_dissent":   {"en": "Where the sources object", "id": "Di mana sumber berkeberatan",
                 "ms": "Di mana sumber membantah"},
 "g_variant":   {"en": "Competing chains", "id": "Rantai yang berbeda", "ms": "Rantaian berbeza"},
 "g_isnad":     {"en": "Transmission", "id": "Periwayatan", "ms": "Periwayatan"},
 "g_birth":     {"en": "Birth", "id": "Kelahiran", "ms": "Kelahiran"},
 "g_age":       {"en": "Age at death", "id": "Usia saat wafat", "ms": "Usia ketika wafat"},
 "g_children":  {"en": "Children", "id": "Anak", "ms": "Anak"},
 "g_siblings":  {"en": "Brothers and sisters", "id": "Saudara", "ms": "Adik-beradik"},
 "m_kunya":     {"en": "kunya", "id": "kunyah", "ms": "kunyah"},
 "m_laqab":     {"en": "laqab", "id": "laqab", "ms": "laqab"},
 "m_male":      {"en": "male", "id": "laki-laki", "ms": "lelaki"},
 "m_female":    {"en": "female", "id": "perempuan", "ms": "perempuan"},
 "m_father":    {"en": "father", "id": "ayah", "ms": "bapa"},
 "m_mother":    {"en": "mother", "id": "ibu", "ms": "ibu"},
 "m_noyear":    {"en": "born · no year in these sources",
                 "id": "lahir · tidak ada tahun dalam sumber-sumber ini",
                 "ms": "lahir · tiada tahun dalam sumber-sumber ini"},
 "m_born":      {"en": "born", "id": "lahir", "ms": "lahir"},
 "m_desc":      {"en": "{n} descendants recorded", "id": "{n} keturunan tercatat",
                 "ms": "{n} keturunan tercatat"},
 "m_gen":       {"en": "generation {n}", "id": "generasi {n}", "ms": "generasi {n}"},
 "isnad_label": {"en": "isnād", "id": "isnād", "ms": "isnād"},
 "ednote":      {"en": "Edition note", "id": "Catatan edisi", "ms": "Catatan edisi"},
 "claim":       {"en": "claim", "id": "klaim", "ms": "tuntutan"},
 "vol":         {"en": "vol.", "id": "jil.", "ms": "jil."},
 "p":           {"en": "p.", "id": "hlm.", "ms": "hlm."},
 # stats
 "s_names":     {"en": "{n} names", "id": "{n} nama", "ms": "{n} nama"},
 "s_claims":    {"en": "{n} sourced claims", "id": "{n} klaim bersumber",
                 "ms": "{n} tuntutan bersumber"},
 "s_links":     {"en": "{n} links", "id": "{n} tautan", "ms": "{n} pautan"},
 "s_works":     {"en": "{n} primary works", "id": "{n} kitab utama", "ms": "{n} kitab utama"},
 "s_gens":      {"en": "{n} generations", "id": "{n} generasi", "ms": "{n} generasi"},
 # bands
 "band_beyond":  {"en": "beyond the attested chain", "id": "di luar rantai yang tsabit",
                  "ms": "di luar rantaian yang sabit"},
 "band_arabia":  {"en": "the Arab genealogy", "id": "nasab Arab", "ms": "nasab Arab"},
 "band_comp":    {"en": "companions", "id": "sahabat", "ms": "sahabat"},
 "band_desc":    {"en": "recorded below a companion", "id": "tercatat di bawah sahabat",
                  "ms": "tercatat di bawah sahabat"},
 "band_beyond_w":{"en": "At or above ʿAdnān and Qaḥṭān — the stretch these books themselves "
                        "decline to vouch for (kadhaba al-nassābūn; Ibn Ḥazm: nothing above "
                        "Qaḥṭān is sound).",
                  "id": "Pada atau di atas ʿAdnān dan Qaḥṭān — bagian yang kitab-kitab ini "
                        "sendiri enggan menjamin (kadhaba al-nassābūn; Ibnu Ḥazm: tidak ada "
                        "yang sahih di atas Qaḥṭān).",
                  "ms": "Pada atau di atas ʿAdnān dan Qaḥṭān — bahagian yang kitab-kitab ini "
                        "sendiri enggan menjamin (kadhaba al-nassābūn; Ibnu Ḥazm: tiada yang "
                        "sahih di atas Qaḥṭān)."},
 "band_arabia_w":{"en": "Below ʿAdnān or Qaḥṭān, with no companion recorded above them — the "
                        "tribal genealogy the books treat as established.",
                  "id": "Di bawah ʿAdnān atau Qaḥṭān, tanpa sahabat yang tercatat di atasnya — "
                        "nasab kabilah yang dianggap tsabit oleh kitab-kitab ini.",
                  "ms": "Di bawah ʿAdnān atau Qaḥṭān, tanpa sahabat yang tercatat di atasnya — "
                        "nasab kabilah yang dianggap sabit oleh kitab-kitab ini."},
 "band_comp_w":  {"en": "Carries an entry in al-Istīʿāb or Usd al-Ghāba. That is a fact about "
                        "the sources, not a judgement about the person.",
                  "id": "Memiliki entri dalam al-Istīʿāb atau Usd al-Ghāba. Itu fakta tentang "
                        "sumbernya, bukan penilaian atas orangnya.",
                  "ms": "Mempunyai entri dalam al-Istīʿāb atau Usd al-Ghāba. Itu fakta tentang "
                        "sumbernya, bukan penilaian terhadap orangnya."},
 "band_desc_w":  {"en": "Placed under someone with a companion entry — largely the Umayyad, "
                        "ʿAbbāsid and ʿAlid lines Ibn Ḥazm carries forward.",
                  "id": "Ditempatkan di bawah seseorang yang memiliki entri sahabat — sebagian "
                        "besar garis Umayyah, ʿAbbāsiyah dan ʿAlawiyah yang diteruskan Ibnu Ḥazm.",
                  "ms": "Diletakkan di bawah seseorang yang mempunyai entri sahabat — sebahagian "
                        "besar salasilah Umayyah, ʿAbbāsiyah dan ʿAlawiyah yang diteruskan Ibnu Ḥazm."},
 "band_note":    {"en": "These are not centuries. These books give no birth years above the "
                        "Prophet, so any date band would be computed by us and would read as "
                        "though it came from the sources. Each band above is instead something "
                        "the sources themselves state or do — a filter, not a period. Turning "
                        "one on dims everything outside it.",
                  "id": "Ini bukan pembagian abad. Kitab-kitab ini tidak memberi tahun kelahiran "
                        "di atas Nabi, sehingga pembagian berdasarkan tanggal akan kami hitung "
                        "sendiri dan akan terbaca seolah-olah berasal dari sumber. Setiap "
                        "kategori di atas justru sesuatu yang dinyatakan atau dilakukan sumber "
                        "itu sendiri — sebuah saringan, bukan periode. Mengaktifkan satu akan "
                        "meredupkan segala yang di luarnya.",
                  "ms": "Ini bukan pembahagian abad. Kitab-kitab ini tidak memberi tahun "
                        "kelahiran di atas Nabi, jadi sebarang pembahagian tarikh akan kami "
                        "kira sendiri dan akan terbaca seolah-olah datang daripada sumber. "
                        "Setiap kategori di atas sebaliknya ialah sesuatu yang dinyatakan atau "
                        "dilakukan oleh sumber itu sendiri — satu tapisan, bukan tempoh. "
                        "Menghidupkan satu akan malapkan segala yang di luarnya."},
 # filter chips
 "f_sahaba":     {"en": "ṣaḥāba", "id": "sahabat", "ms": "sahabat"},
 "f_women":      {"en": "women", "id": "perempuan", "ms": "perempuan"},
 "f_ikhtilaf":   {"en": "ikhtilāf", "id": "ikhtilāf", "ms": "ikhtilāf"},
 "f_2src":       {"en": "2+ sources", "id": "2+ sumber", "ms": "2+ sumber"},
 "f_hand":       {"en": "hand-checked", "id": "diperiksa manual", "ms": "disemak manual"},
 # header
 "title_sub":    {"en": "The lineage of the Prophet Muḥammad ﷺ, his household, the Ṣaḥāba and "
                        "the Arab tribes — back to Ādam on one side and to Qaḥṭān on the other. "
                        "Every name, link and second name carries a quotation from a named "
                        "critical edition, machine-checked against the page it cites before "
                        "this file was written. Where the sources disagree, every reading is kept.",
                  "id": "Nasab Nabi Muhammad ﷺ, keluarganya, para sahabat dan kabilah-kabilah "
                        "Arab — hingga Ādam di satu sisi dan Qaḥṭān di sisi lain. Setiap nama, "
                        "pertalian dan nama kedua disertai kutipan dari edisi kritis yang "
                        "disebutkan namanya, diperiksa mesin terhadap halaman yang dirujuk "
                        "sebelum berkas ini dibuat. Bila sumber berbeda, semua bacaan disimpan.",
                  "ms": "Nasab Nabi Muhammad ﷺ, ahli keluarganya, para sahabat dan kabilah-"
                        "kabilah Arab — hingga Ādam di satu pihak dan Qaḥṭān di pihak lain. "
                        "Setiap nama, pertalian dan nama kedua disertai petikan daripada edisi "
                        "kritis yang dinamakan, disemak mesin terhadap halaman yang dirujuk "
                        "sebelum fail ini ditulis. Apabila sumber berbeza, setiap bacaan "
                        "disimpan."},
 "lang_label":   {"en": "Language", "id": "Bahasa", "ms": "Bahasa"},
}


def strings(lang):
    return {k: v.get(lang, v["en"]) for k, v in UI.items()}


def gloss(kind, lang, **kw):
    return GLOSS[kind].get(lang, GLOSS[kind]["en"]).format(**kw)
