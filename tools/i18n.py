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
    "married_to":  {"en": "the Messenger of God married {a}",
                    "id": "Rasulullah ﷺ menikahi {a}", "ms": "Rasulullah ﷺ mengahwini {a}"},
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
 "bio_read":    {"en": "Read the entry", "id": "Baca entri", "ms": "Baca entri"},
 "bio_from":    {"en": "{n} entries, in the books' own words",
                 "id": "{n} entri, dalam kata-kata kitab itu sendiri",
                 "ms": "{n} entri, dalam kata-kata kitab itu sendiri"},
 "g_married":   {"en": "marriage", "id": "pernikahan", "ms": "perkahwinan"},
 "g_spouses":   {"en": "Wives", "id": "Istri", "ms": "Isteri"},
 "g_husband":   {"en": "Married to", "id": "Menikah dengan", "ms": "Berkahwin dengan"},
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
 "howto":        {"en": "Search reaches any name in the tree and jumps to it; the trail under "
                        "the toolbar shows where you have landed in up to {n} generations. A "
                        "number beside + is how many lie beneath it. Nodes badged auto were "
                        "placed by the chain parser — the quotation is verified, the placement "
                        "rests on the anchor being the right man.",
                  "id": "Pencarian menjangkau setiap nama dalam pohon dan melompat ke sana; "
                        "jejak di bawah bilah alat menunjukkan posisi Anda dalam hingga {n} "
                        "generasi. Angka di samping + adalah jumlah yang ada di bawahnya. Simpul "
                        "bertanda otomatis ditempatkan oleh pengurai rantai — kutipannya "
                        "terverifikasi, penempatannya bergantung pada ketepatan titik sambung.",
                  "ms": "Carian menjangkau setiap nama dalam pokok dan melompat ke sana; jejak "
                        "di bawah bar alat menunjukkan kedudukan anda dalam sehingga {n} "
                        "generasi. Nombor di sebelah + ialah bilangan yang ada di bawahnya. Nod "
                        "bertanda automatik diletakkan oleh penghurai rantaian — petikannya "
                        "disahkan, penempatannya bergantung pada ketepatan titik sauh."},
 "sources_head": {"en": "Sources", "id": "Sumber", "ms": "Sumber"},
 "footer_note":  {"en": "Texts are the pinned OpenITI machine-readable editions; page numbers "
                        "are those of the printed edition named. Every quotation on this page "
                        "was re-read out of the source file at the cited page by validate.py "
                        "before this file was generated.",
                  "id": "Teks adalah edisi terbaca-mesin OpenITI yang dipatok; nomor halaman "
                        "mengikuti edisi cetak yang disebutkan. Setiap kutipan di halaman ini "
                        "dibaca ulang dari berkas sumber pada halaman yang dirujuk oleh "
                        "validate.py sebelum berkas ini dihasilkan.",
                  "ms": "Teks ialah edisi boleh-baca-mesin OpenITI yang dipasak; nombor halaman "
                        "mengikut edisi cetak yang dinamakan. Setiap petikan di halaman ini "
                        "dibaca semula daripada fail sumber pada halaman yang dirujuk oleh "
                        "validate.py sebelum fail ini dihasilkan."},
 "died_ah":      {"en": "d. {n} AH", "id": "w. {n} H", "ms": "w. {n} H"},
}


# ---- data strings ----------------------------------------------------------
# Tribes, notes and editorial verdicts live in the data rather than the interface, but a reader
# in Indonesian should not meet them in English. There are few enough to translate by hand.
DATA = {
 # Who's who group headings. These were printed straight from directory.py, so an Indonesian
 # reader met 'The four caliphs' between two translated panels.
 "The four caliphs":       {"id": "Empat khalifah", "ms": "Empat khalifah"},
 "The Prophet's household":{"id": "Keluarga Nabi ﷺ", "ms": "Keluarga Nabi ﷺ"},
 "Ummahāt al-Muʾminīn":    {"id": "Ummahātul Muʾminīn (para istri Nabi ﷺ)",
                            "ms": "Ummahātul Muʾminīn (para isteri Nabi ﷺ)"},
 "Among the ten":          {"id": "Sepuluh yang dijamin surga", "ms": "Sepuluh yang dijamin syurga"},
 "Anṣār":                  {"id": "Kaum Anṣār", "ms": "Kaum Anṣār"},
 "of Banū al-Naḍīr, of the Children of Israel, of the line of Hārūn":
   {"id": "dari Banū al-Naḍīr, dari Bani Israil, dari keturunan Hārūn",
    "ms": "dari Banū al-Naḍīr, dari Bani Israil, dari keturunan Hārūn"},
 "of Banū al-Naḍīr; the lists that count thirteen wives are the lists that leave her out":
   {"id": "dari Banū al-Naḍīr; daftar yang menghitung tiga belas istri adalah daftar yang tidak memasukkannya",
    "ms": "dari Banū al-Naḍīr; senarai yang mengira tiga belas isteri ialah senarai yang tidak memasukkannya"},
 "Landmarks of the chain": {"id": "Penanda dalam rantai nasab",
                            "ms": "Penanda dalam rantaian nasab"},

 # tribes
 "Quraysh": {"id": "Quraisy", "ms": "Quraisy"},
 "Quraysh / Banū Hāshim": {"id": "Quraisy / Banū Hāsyim", "ms": "Quraisy / Banū Hāsyim"},
 "Quraysh / Banū Zuhra": {"id": "Quraisy / Banū Zuhrah", "ms": "Quraisy / Banū Zuhrah"},
 "Kināna": {"id": "Kinānah", "ms": "Kinānah"},
 "Khazraj / Banū ʿAdī b. al-Najjār": {"id": "Khazraj / Banū ʿAdī bin al-Najjār",
                                      "ms": "Khazraj / Banū ʿAdī bin al-Najjār"},
 "Qaḥṭān / the Yemeni Arabs": {"id": "Qaḥṭān / bangsa Arab Yaman",
                               "ms": "Qaḥṭān / bangsa Arab Yaman"},
 # person notes
 "Eponym of Banū Hāshim.": {"id": "Moyang yang menamai Banū Hāsyim.",
                            "ms": "Moyang yang menamakan Banū Hāsyim."},
 "Ibn Saʿd: jimāʿ Quraysh - no one above Fihr is called Qurashī.":
   {"id": "Ibnu Saʿd: jimāʿ Quraisy — tidak ada di atas Fihr yang disebut Qurasyi.",
    "ms": "Ibnu Saʿd: jimāʿ Quraisy — tiada di atas Fihr yang disebut Qurasyi."},
 "Ceiling of the attested nasab: several sources stop here.":
   {"id": "Batas nasab yang tsabit: beberapa sumber berhenti di sini.",
    "ms": "Had nasab yang sabit: beberapa sumber berhenti di sini."},
 "Distinct from Nāḥūr father of Tāriḥ.": {"id": "Berbeda dari Nāḥūr ayah Tāriḥ.",
                                          "ms": "Berbeza daripada Nāḥūr bapa Tāriḥ."},
 "Distinct from Nāḥūr son of Muqawwam.": {"id": "Berbeda dari Nāḥūr putra Muqawwam.",
                                          "ms": "Berbeza daripada Nāḥūr putera Muqawwam."},
 "Identified with the prophet Idrīs.": {"id": "Diidentifikasi dengan Nabi Idrīs.",
                                        "ms": "Dikenal pasti sebagai Nabi Idrīs."},
 "First man; the root of the chain.": {"id": "Manusia pertama; pangkal rantai nasab.",
                                       "ms": "Manusia pertama; pangkal rantaian nasab."},
 "Mother of the Prophet. Her own line rejoins the spine at Kilāb.":
   {"id": "Ibu Nabi. Garis nasabnya bertemu kembali dengan tulang punggung pada Kilāb.",
    "ms": "Ibu Nabi. Salasilahnya bertemu semula dengan tulang belakang pada Kilāb."},
 "Mother of ʿAbd al-Muṭṭalib.": {"id": "Ibu ʿAbd al-Muṭṭalib.", "ms": "Ibu ʿAbd al-Muṭṭalib."},
 "Root of the Yemeni (Qaḥṭānī) Arabs. Left unattached on purpose: the sources give incompatible "
 "origins and Ibn Hazm holds that none of them is sound.":
   {"id": "Pangkal bangsa Arab Yaman (Qaḥṭānī). Sengaja dibiarkan tidak tersambung: sumber-"
          "sumber memberi asal-usul yang saling bertentangan dan Ibnu Ḥazm berpendapat tidak "
          "satu pun sahih.",
    "ms": "Pangkal bangsa Arab Yaman (Qaḥṭānī). Sengaja dibiarkan tidak bersambung: sumber-"
          "sumber memberi asal usul yang bercanggah dan Ibnu Ḥazm berpendapat tiada satu pun "
          "yang sahih."},
 "Abū Bakr al-Ṣiddīq, first caliph": {"id": "Abū Bakr al-Ṣiddīq, khalifah pertama",
                                      "ms": "Abū Bakr al-Ṣiddīq, khalifah pertama"},
 "third caliph": {"id": "khalifah ketiga", "ms": "khalifah ketiga"},
 "of the ten": {"id": "termasuk sepuluh yang dijamin surga", "ms": "termasuk sepuluh yang dijamin syurga"},
 "Abū ʿUbayda b. al-Jarrāḥ, of the ten": {"id": "Abū ʿUbayda bin al-Jarrāḥ, termasuk sepuluh",
                                          "ms": "Abū ʿUbayda bin al-Jarrāḥ, termasuk sepuluh"},
 "Abū Waqqāṣ, father of Saʿd": {"id": "Abū Waqqāṣ, ayah Saʿd", "ms": "Abū Waqqāṣ, bapa Saʿd"},
 "Sayf Allāh": {"id": "Sayf Allāh (Pedang Allah)", "ms": "Sayf Allāh (Pedang Allah)"},
 "chief of al-Aws": {"id": "pemimpin al-Aws", "ms": "ketua al-Aws"},
 # claim notes and verdicts
 "The Yemeni counterpart of the ceiling at Adnan on the Northern side.":
   {"id": "Padanan Yaman bagi batas pada ʿAdnān di sisi utara.",
    "ms": "Padanan Yaman bagi had pada ʿAdnān di sebelah utara."},
 "Ibrāhīm left no offspring: he did not reach two years of age.":
   {"id": "Ibrāhīm tidak meninggalkan keturunan: ia tidak mencapai usia dua tahun.",
    "ms": "Ibrāhīm tidak meninggalkan keturunan: baginda tidak mencapai usia dua tahun."},
 "Recorded because a chain parser once hung six descendants on him; the sources leave no room "
 "for any.":
   {"id": "Dicatat karena pengurai rantai pernah menggantungkan enam keturunan padanya; "
          "sumber-sumber tidak menyisakan ruang untuk itu.",
    "ms": "Dicatat kerana penghurai rantaian pernah menggantungkan enam keturunan padanya; "
          "sumber-sumber tidak meninggalkan ruang untuk itu."},
 "rejected by Ibn ʿAbd al-Barr": {"id": "ditolak oleh Ibnu ʿAbd al-Barr",
                                  "ms": "ditolak oleh Ibnu ʿAbd al-Barr"},
 "Ibn 'Abd al-Barr declines to give the chain above Adnan":
   {"id": "Ibnu ʿAbd al-Barr enggan menyebut rantai di atas ʿAdnān",
    "ms": "Ibnu ʿAbd al-Barr enggan menyebut rantaian di atas ʿAdnān"},
 "Ibn al-Athir declines to give the chain above Adnan":
   {"id": "Ibnu al-Athīr enggan menyebut rantai di atas ʿAdnān",
    "ms": "Ibnu al-Athīr enggan menyebut rantaian di atas ʿAdnān"},
 "Ibn Sa'd's own conclusion": {"id": "kesimpulan Ibnu Saʿd sendiri",
                               "ms": "kesimpulan Ibnu Saʿd sendiri"},
 "Ibn Hazm: the chain above Qahtan is not established":
   {"id": "Ibnu Ḥazm: rantai di atas Qaḥṭān tidak tsabit",
    "ms": "Ibnu Ḥazm: rantaian di atas Qaḥṭān tidak sabit"},
 "Ibn Hazm on the Prophet's male line": {"id": "Ibnu Ḥazm tentang garis laki-laki Nabi",
                                         "ms": "Ibnu Ḥazm tentang salasilah lelaki Nabi"},
 "ʿĀm al-Fīl": {"id": "ʿĀm al-Fīl (Tahun Gajah)", "ms": "ʿĀm al-Fīl (Tahun Gajah)"},
 "ʿĀm al-Fīl (the Year of the Elephant)": {"id": "ʿĀm al-Fīl (Tahun Gajah)",
                                           "ms": "ʿĀm al-Fīl (Tahun Gajah)"},
 # chain labels
 "Ibn Ishaq's chain as Ibn Sa'd received it":
   {"id": "rantai Ibnu Isḥāq sebagaimana diterima Ibnu Saʿd",
    "ms": "rantaian Ibnu Isḥāq sebagaimana diterima Ibnu Saʿd"},
 "Ibn Ishaq's second chain": {"id": "rantai kedua Ibnu Isḥāq", "ms": "rantaian kedua Ibnu Isḥāq"},
 "Ma'add to A'raq al-Thara": {"id": "Maʿadd hingga Aʿrāq al-Tharā",
                              "ms": "Maʿadd hingga Aʿrāq al-Tharā"},
 "Qahtan identified with the biblical Yaqtan":
   {"id": "Qaḥṭān disamakan dengan Yaqṭān dalam Alkitab",
    "ms": "Qaḥṭān disamakan dengan Yaqṭān dalam Bible"},
 "Qahtan traced to Isma'il through Qaydar":
   {"id": "Qaḥṭān dinasabkan kepada Ismāʿīl melalui Qaydar",
    "ms": "Qaḥṭān dinasabkan kepada Ismāʿīl melalui Qaydar"},
 "Qahtan traced to Sam b. Nuh through Hud":
   {"id": "Qaḥṭān dinasabkan kepada Sām bin Nūḥ melalui Hūd",
    "ms": "Qaḥṭān dinasabkan kepada Sām bin Nūḥ melalui Hūd"},
 "Udad son of Zayd": {"id": "Udad putra Zayd", "ms": "Udad putera Zayd"},
 "al-Kalbi on Udad": {"id": "riwayat al-Kalbī tentang Udad", "ms": "riwayat al-Kalbī tentang Udad"},
 "the Medinan / al-Zuhri chain from Nuh to Adam":
   {"id": "rantai penduduk Madinah / al-Zuhrī dari Nūḥ hingga Ādam",
    "ms": "rantaian penduduk Madinah / al-Zuhrī daripada Nūḥ hingga Ādam"},
 "the Medinan account of Udad": {"id": "riwayat penduduk Madinah tentang Udad",
                                 "ms": "riwayat penduduk Madinah tentang Udad"},
 "the eighteen-generation chain to Ibrahim":
   {"id": "rantai delapan belas generasi hingga Ibrāhīm",
    "ms": "rantaian lapan belas generasi hingga Ibrāhīm"},
 "the forty-generation Kalbi chain to Ibrahim":
   {"id": "rantai al-Kalbī empat puluh generasi hingga Ibrāhīm",
    "ms": "rantaian al-Kalbī empat puluh generasi hingga Ibrāhīm"},
 "the sound account, per al-Jurjani": {"id": "riwayat yang sahih menurut al-Jurjānī",
                                       "ms": "riwayat yang sahih menurut al-Jurjānī"},
 "weaker of the two, per al-Baladhuri": {"id": "yang lebih lemah dari keduanya menurut al-Balādhurī",
                                         "ms": "yang lebih lemah antara keduanya menurut al-Balādhurī"},
}


def data(s, lang):
    """Translate a data string if we have it; otherwise leave it as written."""
    if lang == "en" or not s:
        return s
    hit = DATA.get(s.strip())
    if hit:
        return hit.get(lang, s)
    # An isnad is a chain of transmitters: the names stay, the joining words move.
    ISNAD = {
      "id": [(" from ", " dari "), ("his father", "ayahnya"), ("his grandfather", "kakeknya"),
             ("and others", "dan lainnya"), ("said it, claiming it", "mengatakannya, menisbatkannya"),
             ("some of the people of Medina", "sebagian penduduk Madinah"),
             ("in another transmission from him", "dalam riwayat lain darinya"),
             ("the genealogist", "sang ahli nasab"), ("per ", "menurut "),
             ("ten years between each of them", "sepuluh tahun antara masing-masing mereka")],
      "ms": [(" from ", " daripada "), ("his father", "bapanya"), ("his grandfather", "datuknya"),
             ("and others", "dan lain-lain"), ("said it, claiming it", "mengatakannya, menisbahkannya"),
             ("some of the people of Medina", "sebahagian penduduk Madinah"),
             ("in another transmission from him", "dalam riwayat lain daripadanya"),
             ("the genealogist", "ahli nasab"), ("per ", "menurut "),
             ("ten years between each of them", "sepuluh tahun antara setiap seorang mereka")],
    }
    out = s
    for a, b in ISNAD.get(lang, []):
        out = out.replace(a, b)
    return out


def strings(lang):
    """Every interface string in one language, falling back to English per key."""
    return {k: v.get(lang, v["en"]) for k, v in UI.items()}


def gloss(kind, lang, **kw):
    """Fill one gloss template in one language: gloss('son_of', 'id', a=..., b=...).

    GENERATED per language from the structured fields, never translated from the English -
    see the module docstring for why. The summaries are the one deliberate exception.
    """
    return GLOSS[kind].get(lang, GLOSS[kind]["en"]).format(**kw)
