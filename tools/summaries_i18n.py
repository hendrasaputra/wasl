# -*- coding: utf-8 -*-
# SPDX-License-Identifier: GPL-3.0-or-later
# Wasl - a verifiable nasab. Copyright (C) 2026 Hendra Saputra.
"""Indonesian and Malay for the summaries.

The deliberate exception to the rule in tools/i18n.py. Everywhere else a gloss is GENERATED
per language from the structured fields, never translated from the English, because a
translation of a translation drifts for no reason when the fact is 'X, son of Y'. Here the
English is the original - authored from the Arabic, not derived from a structure - so there
is nothing to generate from, and id/ms are translated from it.

Keyed by the English sentence, so a line that is reworded loses its translation rather than
keeping a stale one. A missing translation keeps the English and is counted in the report.
"""

TR = {
 'Ibn Saʿd opens on her descent: of the Children of Israel, of the line of Hārūn b. ʿImrān.':
  ('Ibn Saʿd membuka dengan nasabnya: dari Bani Israil, dari keturunan Hārūn b. ʿImrān.',
   'Ibn Saʿd membuka dengan nasabnya: daripada Bani Israil, daripada keturunan Hārūn b. ʿImrān.'),
 'She had been married twice before — to Sallām b. Mishkam, who left her, then to Kināna b. al-Rabīʿ b. Abī al-Ḥuqayq, killed at Khaybar.':
  ('Ia telah dua kali menikah sebelumnya — dengan Sallām b. Mishkam, yang menceraikannya, lalu dengan Kināna b. al-Rabīʿ b. Abī al-Ḥuqayq, yang terbunuh di Khaybar.',
   'Dia pernah berkahwin dua kali sebelum itu — dengan Sallām b. Mishkam, yang menceraikannya, kemudian dengan Kināna b. al-Rabīʿ b. Abī al-Ḥuqayq, yang terbunuh di Khaybar.'),
 'How she came to the Prophet is told two ways in this one chapter, and neither is set aside.':
  ('Bagaimana ia sampai kepada Nabi ﷺ diceritakan dua cara dalam satu bab ini, dan tidak satu pun disingkirkan.',
   'Bagaimana dia sampai kepada Nabi ﷺ diceritakan dua cara dalam satu bab ini, dan tiada satu pun diketepikan.'),
 'In one she fell to Diḥya al-Kalbī in the division of the spoils,':
  ('Dalam riwayat pertama ia jatuh kepada Diḥya al-Kalbī dalam pembagian rampasan,',
   'Dalam riwayat pertama dia jatuh kepada Diḥya al-Kalbī dalam pembahagian rampasan,'),
 'and the Prophet bought her from him.':
  ('lalu Rasulullah ﷺ membelinya darinya.',
   'lalu Rasulullah ﷺ membelinya daripadanya.'),
 'In the other she was simply among what he chose for himself at Khaybar.':
  ('Dalam riwayat kedua ia termasuk apa yang beliau pilih untuk diri sendiri di Khaybar.',
   'Dalam riwayat kedua dia termasuk apa yang baginda pilih untuk diri sendiri di Khaybar.'),
 'He freed her and married her, and made her freedom her dower.':
  ('Beliau memerdekakannya dan menikahinya, dan menjadikan kemerdekaannya sebagai maharnya.',
   'Baginda memerdekakannya dan mengahwininya, dan menjadikan kemerdekaannya sebagai maharnya.'),
 'Those present could not tell whether he had married her or taken her as a concubine,':
  ('Orang-orang yang hadir tidak tahu apakah beliau menikahinya atau menjadikannya budak,',
   'Orang yang hadir tidak tahu sama ada baginda mengahwininya atau menjadikannya hamba,'),
 'until he veiled her and mounted her behind him — and then they knew.':
  ('sampai beliau menutupinya dengan hijab dan memboncengnya di belakangnya — barulah mereka tahu.',
   'sehingga baginda menutupinya dengan hijab dan membonceng dia di belakang — barulah mereka tahu.'),
 'She had dreamt of a moon coming from Yathrib until it fell into her lap.':
  ('Ia bermimpi melihat bulan datang dari Yathrib hingga jatuh ke pangkuannya.',
   'Dia bermimpi melihat bulan datang dari Yathrib hingga jatuh ke ribaannya.'),
 'Kināna struck her face for telling it, and the mark was still there when the Prophet asked.':
  ('Kināna memukul wajahnya karena ia menceritakan mimpi itu, dan bekasnya masih ada ketika Nabi ﷺ bertanya.',
   'Kināna menampar wajahnya kerana dia menceritakan mimpi itu, dan kesannya masih ada ketika Nabi ﷺ bertanya.'),
 'He told her that her father had been among the bitterest of the Jews against him.':
  ('Beliau mengatakan kepadanya bahwa ayahnya termasuk orang Yahudi yang paling keras memusuhinya.',
   'Baginda memberitahunya bahawa bapanya termasuk orang Yahudi yang paling keras memusuhi baginda.'),
 'She answered him out of the Qurʾān: no bearer of burdens bears the burden of another.':
  ('Ia menjawab dengan ayat al-Qurʾān: seorang yang berdosa tidak memikul dosa orang lain.',
   'Dia menjawab dengan ayat al-Qurʾān: seorang yang berdosa tidak memikul dosa orang lain.'),
 'He put the choice to her — Islam and himself, or Judaism and her freedom —':
  ('Beliau memberinya pilihan — Islam dan dirinya, atau Yahudi dan kemerdekaannya —',
   'Baginda memberinya pilihan — Islam dan dirinya, atau Yahudi dan kemerdekaannya —'),
 'and she said God and His Messenger were dearer to her than being freed and going back.':
  ('dan ia berkata Allah dan Rasul-Nya lebih ia cintai daripada dimerdekakan dan kembali kepada kaumnya.',
   'dan dia berkata Allah dan Rasul-Nya lebih dia cintai daripada dimerdekakan dan kembali kepada kaumnya.'),
 'His other wives called her the Jewess.':
  ('Istri-istri beliau yang lain menyebutnya perempuan Yahudi itu.',
   'Isteri-isteri baginda yang lain memanggilnya perempuan Yahudi itu.'),
 'When ʿĀʾisha boasted over her, he told her what to answer: my father is Hārūn, my uncle Mūsā.':
  ('Ketika ʿĀʾisha membanggakan diri atasnya, beliau mengajarinya jawaban: ayahku Hārūn, pamanku Mūsā.',
   'Ketika ʿĀʾisha berbangga atasnya, baginda mengajarnya jawapan: bapaku Hārūn, bapa saudaraku Mūsā.'),
 'On one question the chapter contradicts itself outright, and both readings are left standing.':
  ('Dalam satu perkara bab ini bertentangan dengan dirinya sendiri secara terang, dan kedua bacaan dibiarkan berdiri.',
   'Dalam satu perkara bab ini bercanggah dengan dirinya sendiri secara terang, dan kedua-dua bacaan dibiarkan berdiri.'),
 'ʿAṭāʾ: the Messenger of God did not allot her a turn.':
  ('ʿAṭāʾ: Rasulullah ﷺ tidak memberinya giliran.',
   'ʿAṭāʾ: Rasulullah ﷺ tidak memberinya giliran.'),
 'al-Zuhrī: she was one of his wives, and he allotted to her as he allotted to them.':
  ('al-Zuhrī: ia salah seorang istri beliau, dan beliau memberinya giliran seperti kepada yang lain.',
   'al-Zuhrī: dia salah seorang isteri baginda, dan baginda memberinya giliran seperti kepada yang lain.'),
 "She left a third of her estate to her sister's son, a Jew.":
  ('Ia mewasiatkan sepertiga hartanya kepada anak saudarinya, seorang Yahudi.',
   'Dia mewasiatkan satu pertiga hartanya kepada anak saudaranya, seorang Yahudi.'),
 'Her death is given here as the year fifty,':
  ('Wafatnya di sini disebut tahun lima puluh,',
   'Kewafatannya di sini disebut tahun lima puluh,'),
 'and, in the closing line of the same chapter, as fifty-two — buried at al-Baqīʿ.':
  ('dan, pada baris penutup bab yang sama, tahun lima puluh dua — dimakamkan di al-Baqīʿ.',
   'dan, pada baris penutup bab yang sama, tahun lima puluh dua — dimakamkan di al-Baqīʿ.'),
 'Ibn al-Athīr heads the entry with the full line and the kunya Abū Ḥafṣ.':
  ('Ibn al-Athīr membuka entri dengan nasab lengkap dan kunyah Abū Ḥafṣ.',
   'Ibn al-Athīr membuka entri dengan nasab lengkap dan kunyah Abū Ḥafṣ.'),
 "His mother's name turns on one letter, and the entry sets the quarrel out rather than settling it.":
  ('Nama ibunya bergantung pada satu huruf, dan entri ini memaparkan perselisihannya alih-alih memutuskannya.',
   'Nama ibunya bergantung pada satu huruf, dan entri ini memaparkan perselisihannya dan bukan memutuskannya.'),
 'Ḥantama daughter of Hāshim b. al-Mughīra —':
  ('Ḥantama binti Hāshim b. al-Mughīra —',
   'Ḥantama binti Hāshim b. al-Mughīra —'),
 "or of Hishām, which would make her Abū Jahl's sister rather than his cousin.":
  ('atau binti Hishām, yang menjadikannya saudari Abū Jahl, bukan sepupunya.',
   'atau binti Hishām, yang menjadikannya saudara perempuan Abū Jahl, bukan sepupunya.'),
 'Ibn ʿAbd al-Barr calls that reading a mistake;':
  ('Ibn ʿAbd al-Barr menyebut bacaan itu keliru;',
   'Ibn ʿAbd al-Barr menyebut bacaan itu silap;'),
 'Ibn Manda holds it, and makes Abū Jahl his uncle.':
  ('Ibn Manda memegangnya, dan menjadikan Abū Jahl pamannya.',
   'Ibn Manda berpegang dengannya, dan menjadikan Abū Jahl bapa saudaranya.'),
 'He was born thirteen years after the Elephant,':
  ('Ia lahir tiga belas tahun setelah Tahun Gajah,',
   'Dia lahir tiga belas tahun selepas Tahun Gajah,'),
 'though he reckoned it himself from the Fijār war instead.':
  ('meski ia sendiri menghitungnya dari perang Fijār.',
   'walaupun dia sendiri mengiranya dari perang Fijār.'),
 "Before Islam he was Quraysh's envoy, sent when they had a quarrel to settle.":
  ('Sebelum Islam ia menjadi duta Quraisy, diutus bila mereka punya perselisihan untuk diselesaikan.',
   'Sebelum Islam dia menjadi duta Quraisy, diutus apabila mereka mempunyai perselisihan untuk diselesaikan.'),
 'When Muḥammad was sent, ʿUmar was hard on him and on the Muslims.':
  ('Ketika Muḥammad ﷺ diutus, ʿUmar keras terhadapnya dan terhadap kaum Muslimin.',
   'Ketika Muḥammad ﷺ diutus, ʿUmar keras terhadap baginda dan terhadap kaum Muslimin.'),
 'How many had entered Islam before him is reported several ways on the same page.':
  ('Berapa orang yang masuk Islam sebelumnya diriwayatkan beberapa cara pada halaman yang sama.',
   'Berapa orang yang memeluk Islam sebelumnya diriwayatkan beberapa cara pada halaman yang sama.'),
 'Hilāl b. Yasāf: after forty men and eleven women.':
  ('Hilāl b. Yasāf: setelah empat puluh lelaki dan sebelas perempuan.',
   'Hilāl b. Yasāf: selepas empat puluh lelaki dan sebelas perempuan.'),
 'Or after thirty-nine men and twenty women, he completing the forty.':
  ('Atau setelah tiga puluh sembilan lelaki dan dua puluh perempuan, ia menggenapkan yang empat puluh.',
   'Atau selepas tiga puluh sembilan lelaki dan dua puluh perempuan, dia menggenapkan yang empat puluh.'),
 'Saʿīd b. al-Musayyab: after forty men and ten women — and once he entered, Islam showed itself in Mecca.':
  ('Saʿīd b. al-Musayyab: setelah empat puluh lelaki dan sepuluh perempuan — dan begitu ia masuk, Islam tampak di Mekah.',
   'Saʿīd b. al-Musayyab: selepas empat puluh lelaki dan sepuluh perempuan — dan sebaik dia masuk, Islam menampakkan diri di Mekah.'),
 'The Prophet had prayed: strengthen Islam with whichever of the two men You love better, ʿUmar or ʿAmr b. Hishām.':
  ('Nabi ﷺ telah berdoa: kuatkanlah Islam dengan salah satu dari dua orang yang lebih Engkau cintai, ʿUmar atau ʿAmr b. Hishām.',
   'Nabi ﷺ telah berdoa: kuatkanlah Islam dengan salah seorang daripada dua lelaki yang lebih Engkau cintai, ʿUmar atau ʿAmr b. Hishām.'),
 'By his own account he stood behind him in the mosque, heard him open Sūrat al-Ḥāqqa, and marvelled at how the Qurʾān was put together.':
  ('Menurut penuturannya sendiri, ia berdiri di belakang beliau di masjid, mendengar beliau membuka Sūrat al-Ḥāqqa, dan takjub pada susunan al-Qurʾān.',
   'Menurut ceritanya sendiri, dia berdiri di belakang baginda di masjid, mendengar baginda membuka Sūrat al-Ḥāqqa, dan kagum pada susunan al-Qurʾān.'),
 'He was the first to carry the whip, the first to gather people for the night prayer in Ramaḍān, the first to be called Commander of the Faithful.':
  ('Ia orang pertama yang membawa cambuk, pertama yang mengumpulkan orang untuk qiyam Ramadan, pertama yang digelari Amīr al-Muʾminīn.',
   'Dia orang pertama yang membawa cemeti, pertama yang mengumpulkan orang untuk qiyam Ramadan, pertama yang digelar Amīr al-Muʾminīn.'),
 'His colour changed in the Year of Ashes because he forbade himself fat and milk until the people had plenty.':
  ('Warna kulitnya berubah pada Tahun Abu karena ia mengharamkan atas dirinya lemak dan susu sampai orang-orang berkecukupan.',
   'Warna kulitnya berubah pada Tahun Abu kerana dia mengharamkan ke atas dirinya lemak dan susu sehingga orang ramai berkecukupan.'),
 'He was stabbed on a Wednesday, four nights left of Dhū al-Ḥijja, in the year twenty-three.':
  ('Ia ditikam pada hari Rabu, empat malam tersisa dari Dhū al-Ḥijja, tahun dua puluh tiga.',
   'Dia ditikam pada hari Rabu, empat malam berbaki dari Dhū al-Ḥijja, tahun dua puluh tiga.'),
 'ʿUthmān b. Muḥammad al-Akhnasī answers flatly that this is a mistake.':
  ('ʿUthmān b. Muḥammad al-Akhnasī menjawab tegas bahwa ini keliru.',
   'ʿUthmān b. Muḥammad al-Akhnasī menjawab dengan tegas bahawa ini silap.'),
 'Ibn Qutayba has Abū Luʾluʾa strike him on a Monday; he lingered three days.':
  ('Menurut Ibn Qutayba, Abū Luʾluʾa menikamnya pada hari Senin; ia bertahan tiga hari.',
   'Menurut Ibn Qutayba, Abū Luʾluʾa menikamnya pada hari Isnin; dia bertahan tiga hari.'),
 'He died at sixty-three, or at fifty-five — the entry prefers the first.':
  ('Ia wafat pada usia enam puluh tiga, atau lima puluh lima — entri ini memilih yang pertama.',
   'Dia wafat pada usia enam puluh tiga, atau lima puluh lima — entri ini memilih yang pertama.'),
 'Ṣuhayb prayed over him, and he was buried beside the Prophet and Abū Bakr.':
  ('Ṣuhayb menyalatinya, dan ia dimakamkan di samping Nabi ﷺ dan Abū Bakr.',
   'Ṣuhayb menyembahyangkannya, dan dia dimakamkan di sisi Nabi ﷺ dan Abū Bakr.'),
 'Fāṭima bt. Saʿd bore Kilāb b. Murra a son, Zuhra, and long after him a second, named Zayd.':
  ('Fāṭima binti Saʿd melahirkan bagi Kilāb b. Murra seorang putra, Zuhra, dan lama setelahnya seorang lagi, bernama Zayd.',
   'Fāṭima binti Saʿd melahirkan bagi Kilāb b. Murra seorang putera, Zuhra, dan lama selepasnya seorang lagi, bernama Zayd.'),
 'Kilāb died, and Rabīʿa b. Ḥarām carried her off to his own country in Syria.':
  ('Kilāb wafat, dan Rabīʿa b. Ḥarām membawanya ke negerinya di Syam.',
   'Kilāb wafat, dan Rabīʿa b. Ḥarām membawanya ke negerinya di Syam.'),
 'The child went with her, and was called Quṣayy for the distance she took him.':
  ('Anak itu ikut bersamanya, dan dinamai Quṣayy karena jauhnya ia dibawa.',
   'Anak itu ikut bersamanya, dan dinamakan Quṣayy kerana jauhnya dia dibawa.'),
 'A Quḍāʿī he had beaten at archery told him to go back where he belonged: you are not one of us.':
  ('Seorang Quḍāʿī yang ia kalahkan dalam memanah menyuruhnya pulang ke tempat asalnya: engkau bukan dari kami.',
   'Seorang Quḍāʿī yang dia kalahkan dalam memanah menyuruhnya pulang ke tempat asalnya: engkau bukan daripada kami.'),
 'His mother told him who his father was, and that his people were at Mecca beside the Sacred House.':
  ('Ibunya memberitahunya siapa ayahnya, dan bahwa kaumnya di Mekah di sisi Baitullah.',
   'Ibunya memberitahunya siapa bapanya, dan bahawa kaumnya di Mekah di sisi Baitullah.'),
 'At Mecca he married Ḥubbā, daughter of Ḥulayl, who then held the keys of the House.':
  ('Di Mekah ia menikahi Ḥubbā, putri Ḥulayl, yang saat itu memegang kunci Kaʿbah.',
   'Di Mekah dia mengahwini Ḥubbā, puteri Ḥulayl, yang ketika itu memegang kunci Kaʿbah.'),
 'How the House passed to him is given three ways, laid side by side without a choice between them.':
  ('Bagaimana Kaʿbah berpindah kepadanya disebut tiga cara, diletakkan berdampingan tanpa dipilih salah satunya.',
   'Bagaimana Kaʿbah berpindah kepadanya disebut tiga cara, diletakkan bersebelahan tanpa dipilih salah satunya.'),
 "He bought it from Ḥulayl's son for provisions — or, it is said, for a skin of wine.":
  ('Ia membelinya dari putra Ḥulayl dengan bekal — atau, menurut satu riwayat, dengan sekantong khamar.',
   'Dia membelinya daripada putera Ḥulayl dengan bekalan — atau, menurut satu riwayat, dengan sekirbat arak.'),
 "Ḥulayl willed it to him, saying Quṣayy's children were his own daughter's.":
  ('Ḥulayl mewasiatkannya kepadanya, katanya anak-anak Quṣayy adalah anak putrinya sendiri.',
   'Ḥulayl mewasiatkannya kepadanya, katanya anak-anak Quṣayy ialah anak puterinya sendiri.'),
 'Or he judged himself more entitled to it than Khuzāʿa and Bakr, and put it to the men of Quraysh.':
  ('Atau ia memandang dirinya lebih berhak atasnya daripada Khuzāʿa dan Bakr, lalu mengajukannya kepada tokoh-tokoh Quraisy.',
   'Atau dia memandang dirinya lebih berhak ke atasnya daripada Khuzāʿa dan Bakr, lalu mengemukakannya kepada tokoh-tokoh Quraisy.'),
 'He wrote to Rizāḥ, his brother by the same mother, to come and fight for him.':
  ('Ia menulis kepada Rizāḥ, saudaranya seibu, agar datang berperang membelanya.',
   'Dia menulis kepada Rizāḥ, saudaranya seibu, agar datang berperang membelanya.'),
 'The arbitrator gave him the House and the rule of Mecca over Khuzāʿa,':
  ('Hakim itu memutuskan Kaʿbah dan pemerintahan Mekah baginya, mengungguli Khuzāʿa,',
   'Hakim itu memutuskan Kaʿbah dan pemerintahan Mekah baginya, mengatasi Khuzāʿa,'),
 'and was named the Crusher, for the blood-claims he crushed underfoot.':
  ('dan ia digelari al-Shaddākh, karena tuntutan-tuntutan darah yang ia injak dan gugurkan.',
   'dan dia digelar al-Shaddākh, kerana tuntutan-tuntutan darah yang dia pijak dan gugurkan.'),
 'Quraysh, the entry says, were named that day for gathering to him.':
  ('Quraisy, kata entri ini, dinamai pada hari itu karena berkumpulnya mereka kepadanya.',
   'Quraisy, kata entri ini, dinamakan pada hari itu kerana berkumpulnya mereka kepadanya.'),
 'A second account in the same chapter derives the name quite differently, from the sons of Fihr.':
  ('Riwayat kedua dalam bab yang sama menurunkan nama itu dengan cara yang sama sekali lain, dari anak-anak Fihr.',
   'Riwayat kedua dalam bab yang sama menerbitkan nama itu dengan cara yang sama sekali lain, daripada anak-anak Fihr.'),
 'He built the House of Assembly with its door facing the Kaʿba.':
  ('Ia membangun Dār al-Nadwa dengan pintunya menghadap Kaʿbah.',
   'Dia membina Dār al-Nadwa dengan pintunya menghadap Kaʿbah.'),
 'The doorkeeping, the watering, the provisioning, the war banner, the assembly and the judging of Mecca were all his.':
  ('Ḥijābah, siqāyah, rifādah, panji perang, nadwah dan seluruh hukum Mekah ada di tangannya.',
   'Ḥijābah, siqāyah, rifādah, panji perang, nadwah dan seluruh hukum Mekah ada di tangannya.'),
 'They called him the Gatherer for what he had gathered of their affairs.':
  ('Mereka menyebutnya Mujammiʿ karena apa yang ia himpun dari urusan mereka.',
   'Mereka memanggilnya Mujammiʿ kerana apa yang dia himpunkan daripada urusan mereka.'),
 "All his children were Ḥubbā's: ʿAbd al-Dār his first-born, and ʿAbd Manāf, whose name was al-Mughīra.":
  ('Semua anaknya dari Ḥubbā: ʿAbd al-Dār yang sulung, dan ʿAbd Manāf, yang namanya al-Mughīra.',
   'Semua anaknya daripada Ḥubbā: ʿAbd al-Dār yang sulung, dan ʿAbd Manāf, yang namanya al-Mughīra.'),
 'He said of them: four sons — two I named for my god, one for my house, one for myself.':
  ('Ia berkata tentang mereka: empat putra — dua kunamai dengan nama tuhanku, satu dengan rumahku, satu dengan diriku.',
   'Dia berkata tentang mereka: empat putera — dua kunamakan dengan nama tuhanku, satu dengan rumahku, satu dengan diriku.'),
 'His name was ʿAbd Allāh; his father Abū Quḥāfa was ʿUthmān b. ʿĀmir, of Taym.':
  ('Namanya ʿAbd Allāh; ayahnya Abū Quḥāfa adalah ʿUthmān b. ʿĀmir, dari Taym.',
   'Namanya ʿAbd Allāh; bapanya Abū Quḥāfa ialah ʿUthmān b. ʿĀmir, daripada Taym.'),
 'His mother, Umm al-Khayr, was Salmā bt. Ṣakhr — of Taym as well.':
  ('Ibunya, Umm al-Khayr, adalah Salmā binti Ṣakhr — dari Taym juga.',
   'Ibunya, Umm al-Khayr, ialah Salmā binti Ṣakhr — daripada Taym juga.'),
 'Ibn Isḥāq alone says the name ʿAtīq belonged to the father, and Ibn Saʿd notes that nobody else says it.':
  ('Hanya Ibn Isḥāq yang mengatakan nama ʿAtīq milik sang ayah, dan Ibn Saʿd mencatat tak seorang pun selainnya mengatakannya.',
   'Hanya Ibn Isḥāq yang mengatakan nama ʿAtīq milik bapanya, dan Ibn Saʿd mencatat tiada seorang pun selainnya mengatakannya.'),
 'Ibrāhīm: the first to pray was Abū Bakr.':
  ('Ibrāhīm: orang pertama yang salat adalah Abū Bakr.',
   'Ibrāhīm: orang pertama yang bersolat ialah Abū Bakr.'),
 'His daughter Asmāʾ: my father was the first of the Muslims — I never knew him but holding this religion.':
  ('Putrinya Asmāʾ: ayahku orang Islam yang pertama — aku tak pernah mengenalnya kecuali memeluk agama ini.',
   'Puterinya Asmāʾ: bapaku orang Islam yang pertama — aku tidak pernah mengenalnya melainkan memeluk agama ini.'),
 'He entered Islam owning forty thousand dirhams,':
  ('Ia masuk Islam dengan memiliki empat puluh ribu dirham,',
   'Dia memeluk Islam dengan memiliki empat puluh ribu dirham,'),
 'and spent it freeing slaves and strengthening the Muslims until he reached Medina with five thousand.':
  ('dan membelanjakannya untuk memerdekakan budak dan menguatkan kaum Muslimin hingga sampai di Madinah dengan lima ribu.',
   'dan membelanjakannya untuk memerdekakan hamba dan menguatkan kaum Muslimin sehingga sampai di Madinah dengan lima ribu.'),
 'He was at Badr, Uḥud, the Trench and every engagement,':
  ('Ia ikut Badr, Uḥud, Khandaq dan semua peperangan,',
   'Dia menyertai Badr, Uḥud, Khandaq dan semua peperangan,'),
 'and among those who held their ground at Uḥud when the people turned.':
  ('dan termasuk yang bertahan di Uḥud ketika orang-orang berpaling.',
   'dan termasuk yang bertahan di Uḥud ketika orang ramai berpaling.'),
 'He died owing the treasury six thousand dirhams and left his orchard against it.':
  ('Ia wafat dengan utang enam ribu dirham kepada baitulmal dan meninggalkan kebunnya sebagai gantinya.',
   'Dia wafat dengan hutang enam ribu dirham kepada baitulmal dan meninggalkan kebunnya sebagai gantinya.'),
 'To ʿĀʾisha: I have nothing but a milch-camel and a bowl — take them to ʿUmar when I die.':
  ('Kepada ʿĀʾisha: aku tak punya apa-apa selain seekor unta perah dan sebuah mangkuk — bawalah keduanya kepada ʿUmar bila aku mati.',
   'Kepada ʿĀʾisha: aku tiada apa-apa selain seekor unta perah dan sebuah mangkuk — bawalah kedua-duanya kepada ʿUmar apabila aku mati.'),
 'ʿUmar, receiving them: God have mercy on Abū Bakr, he has worn out whoever comes after him.':
  ('ʿUmar, saat menerimanya: semoga Allah merahmati Abū Bakr, ia telah memayahkan siapa pun sesudahnya.',
   'ʿUmar, ketika menerimanya: semoga Allah merahmati Abū Bakr, dia telah memenatkan sesiapa pun selepasnya.'),
 'On one thing the chapter reports two flatly opposed positions and settles neither.':
  ('Dalam satu hal bab ini meriwayatkan dua pendirian yang bertolak belakang dan tidak memutuskan keduanya.',
   'Dalam satu hal bab ini meriwayatkan dua pendirian yang bertentangan dan tidak memutuskan kedua-duanya.'),
 'ʿAlī: God have mercy on Abū Bakr — he was the first to gather the two boards.':
  ('ʿAlī: semoga Allah merahmati Abū Bakr — ia orang pertama yang menghimpun dua papan mushaf.',
   'ʿAlī: semoga Allah merahmati Abū Bakr — dia orang pertama yang menghimpunkan dua papan mushaf.'),
 'Ibn Sīrīn: Abū Bakr died and did not gather the Qurʾān.':
  ('Ibn Sīrīn: Abū Bakr wafat dan tidak menghimpun al-Qurʾān.',
   'Ibn Sīrīn: Abū Bakr wafat dan tidak menghimpunkan al-Qurʾān.'),
 'Saʿīd b. al-Musayyab: he completed in his caliphate the age of the Messenger of God, dying at sixty-three.':
  ('Saʿīd b. al-Musayyab: dalam kekhalifahannya ia menggenapi usia Rasulullah ﷺ, wafat pada enam puluh tiga.',
   'Saʿīd b. al-Musayyab: dalam pemerintahannya dia menggenapi usia Rasulullah ﷺ, wafat pada enam puluh tiga.'),
 'ʿĀʾisha: he died in the night and we buried him before morning.':
  ('ʿĀʾisha: ia wafat pada malam hari dan kami memakamkannya sebelum pagi.',
   'ʿĀʾisha: dia wafat pada waktu malam dan kami mengebumikannya sebelum pagi.'),
 "He had asked to be buried alongside the Prophet, and his head was set at the Prophet's shoulders.":
  ('Ia telah meminta dimakamkan di samping Nabi ﷺ, dan kepalanya diletakkan di bahu Nabi ﷺ.',
   'Dia telah meminta dikebumikan di sisi Nabi ﷺ, dan kepalanya diletakkan di bahu Nabi ﷺ.'),
 'ʿĀʾisha raised the wailing for him and ʿUmar came and forbade it.':
  ('ʿĀʾisha menaikkan ratapan atasnya dan ʿUmar datang melarangnya.',
   'ʿĀʾisha menaikkan ratapan atasnya dan ʿUmar datang melarangnya.'),
 'His father outlived him and inherited a sixth,':
  ('Ayahnya hidup lebih lama darinya dan mewarisi seperenam,',
   'Bapanya hidup lebih lama daripadanya dan mewarisi satu perenam,'),
 'and when told, said only: a heavy loss — who has taken the command after him?':
  ('dan ketika diberitahu, hanya berkata: musibah besar — siapa yang memegang urusan sesudahnya?',
   'dan apabila diberitahu, hanya berkata: musibah besar — siapa yang memegang urusan selepasnya?'),
 'His mother was Arwā bt. Kurayz of ʿAbd Shams,':
  ('Ibunya Arwā binti Kurayz dari ʿAbd Shams,',
   'Ibunya Arwā binti Kurayz daripada ʿAbd Shams,'),
 'and her mother was Umm Ḥakīm al-Bayḍāʾ, daughter of ʿAbd al-Muṭṭalib.':
  ('dan ibunya adalah Umm Ḥakīm al-Bayḍāʾ, putri ʿAbd al-Muṭṭalib.',
   'dan ibunya ialah Umm Ḥakīm al-Bayḍāʾ, puteri ʿAbd al-Muṭṭalib.'),
 'In the Jāhiliyya he was called Abū ʿAmr; the Muslims renamed him for the son Ruqayya bore him.':
  ('Pada masa Jahiliah ia berkunyah Abū ʿAmr; kaum Muslimin menggantinya dengan nama putra yang dilahirkan Ruqayya baginya.',
   'Pada zaman Jahiliah dia berkunyah Abū ʿAmr; kaum Muslimin menggantinya dengan nama putera yang dilahirkan Ruqayya baginya.'),
 'That child died at six, pecked on the eye by a cockerel.':
  ('Anak itu wafat pada usia enam tahun, matanya dipatuk ayam jantan.',
   'Anak itu wafat pada usia enam tahun, matanya dipatuk ayam jantan.'),
 'When he entered Islam his uncle al-Ḥakam bound him: do you turn from the religion of your fathers to a new one?':
  ('Ketika ia masuk Islam, pamannya al-Ḥakam mengikatnya: apakah engkau berpaling dari agama nenek moyangmu kepada agama baru?',
   'Ketika dia memeluk Islam, bapa saudaranya al-Ḥakam mengikatnya: adakah engkau berpaling daripada agama nenek moyangmu kepada agama baharu?'),
 'He made both migrations to Abyssinia with Ruqayya,':
  ('Ia melakukan kedua hijrah ke Habasyah bersama Ruqayya,',
   'Dia melakukan kedua-dua hijrah ke Habsyah bersama Ruqayya,'),
 'of whom the Prophet said: they are the first to migrate to God since Lot.':
  ('yang tentang keduanya Nabi ﷺ bersabda: mereka orang pertama yang berhijrah kepada Allah setelah Lūṭ.',
   'yang tentang kedua-duanya Nabi ﷺ bersabda: mereka orang pertama yang berhijrah kepada Allah selepas Lūṭ.'),
 'At the shūrā ʿAbd al-Raḥmān gave him his hand first, then ʿAlī.':
  ('Pada syura, ʿAbd al-Raḥmān membaiatnya lebih dahulu, lalu ʿAlī.',
   'Pada syura, ʿAbd al-Raḥmān membaiahnya terlebih dahulu, kemudian ʿAlī.'),
 'He sent Ibn ʿAbbās to lead the pilgrimage in the year he was killed, thirty-five.':
  ('Ia mengutus Ibn ʿAbbās memimpin haji pada tahun ia terbunuh, tiga puluh lima.',
   'Dia mengutus Ibn ʿAbbās mengetuai haji pada tahun dia terbunuh, tiga puluh lima.'),
 "Besieged, he answered the charge against him with the three things that make a Muslim's blood lawful, and said he was none of them.":
  ('Dalam pengepungan, ia menjawab tuduhan atasnya dengan tiga hal yang menghalalkan darah seorang Muslim, dan mengatakan dirinya bukan salah satunya.',
   'Dalam kepungan, dia menjawab tuduhan ke atasnya dengan tiga perkara yang menghalalkan darah seorang Muslim, dan berkata dirinya bukan salah satunya.'),
 'On the morning of his death he told a dream: the Messenger of God had said, ʿUthmān, break your fast with us.':
  ('Pada pagi hari kematiannya ia menceritakan mimpi: Rasulullah ﷺ berkata, wahai ʿUthmān, berbukalah bersama kami.',
   'Pada pagi hari kematiannya dia menceritakan mimpi: Rasulullah ﷺ berkata, wahai ʿUthmān, berbukalah bersama kami.'),
 'Kināna b. Bishr struck his forehead with an iron bar and he fell on his side.':
  ('Kināna b. Bishr memukul dahinya dengan batang besi dan ia tersungkur ke sisinya.',
   'Kināna b. Bishr memukul dahinya dengan batang besi dan dia tersungkur ke sisinya.'),
 'al-Zuhrī puts the killing at the time of the afternoon prayer.':
  ('al-Zuhrī menempatkan pembunuhan itu pada waktu salat Asar.',
   'al-Zuhrī meletakkan pembunuhan itu pada waktu solat Asar.'),
 'His wife, after it: you killed him, and he used to keep the whole night alive with the Qurʾān in a single rakʿa.':
  ('Istrinya, sesudah itu: kalian membunuhnya, padahal ia menghidupkan seluruh malam dengan al-Qurʾān dalam satu rakaat.',
   'Isterinya, selepas itu: kamu membunuhnya, padahal dia menghidupkan seluruh malam dengan al-Qurʾān dalam satu rakaat.'),
 'His treasurer held thirty million five hundred thousand dirhams on the day he died; it was plundered.':
  ('Bendaharanya menyimpan tiga puluh juta lima ratus ribu dirham pada hari ia terbunuh; semuanya dijarah.',
   'Bendaharinya menyimpan tiga puluh juta lima ratus ribu dirham pada hari dia terbunuh; semuanya dirampas.'),
 'He was the first to be buried in that ground.':
  ('Ia orang pertama yang dimakamkan di pekuburan itu.',
   'Dia orang pertama yang dikebumikan di perkuburan itu.'),
 "Ibn al-Athīr heads him as the Prophet's paternal cousin.":
  ('Ibn al-Athīr menyebutnya sebagai putra paman Nabi ﷺ.',
   'Ibn al-Athīr menyebutnya sebagai anak bapa saudara Nabi ﷺ.'),
 "Abū Ṭālib's name was ʿAbd Manāf — or, it is said, his kunya was his name.":
  ('Nama Abū Ṭālib adalah ʿAbd Manāf — atau, menurut satu pendapat, kunyahnya itulah namanya.',
   'Nama Abū Ṭālib ialah ʿAbd Manāf — atau, menurut satu pendapat, kunyahnya itulah namanya.'),
 'His mother was Fāṭima bt. Asad b. Hāshim.':
  ('Ibunya Fāṭima binti Asad b. Hāshim.',
   'Ibunya Fāṭima binti Asad b. Hāshim.'),
 'He was the first Hāshimī born of two Hāshimīs, and the first caliph of Banū Hāshim.':
  ('Ia orang Hāshimī pertama yang lahir dari dua orang Hāshimī, dan khalifah pertama dari Banū Hāshim.',
   'Dia orang Hāshimī pertama yang lahir daripada dua orang Hāshimī, dan khalifah pertama daripada Banū Hāshim.'),
 'Who entered Islam first is argued through the entry rather than answered in it.':
  ('Siapa yang pertama masuk Islam diperdebatkan sepanjang entri ini, bukan dijawab di dalamnya.',
   'Siapa yang pertama memeluk Islam diperdebatkan sepanjang entri ini, bukan dijawab di dalamnya.'),
 'Mujāhid: ʿAlī became Muslim at ten.':
  ('Mujāhid: ʿAlī masuk Islam pada usia sepuluh tahun.',
   'Mujāhid: ʿAlī memeluk Islam pada usia sepuluh tahun.'),
 'al-Ḥasan and others: first after Khadīja, and at fifteen.':
  ('al-Ḥasan dan yang lain: pertama setelah Khadīja, dan pada usia lima belas.',
   'al-Ḥasan dan yang lain: pertama selepas Khadīja, dan pada usia lima belas.'),
 'Zayd b. Arqam said ʿAlī was first — and Ibrāhīm al-Nakhaʿī, told of it, denied it: the first was Abū Bakr.':
  ('Zayd b. Arqam mengatakan ʿAlī yang pertama — dan Ibrāhīm al-Nakhaʿī, ketika diberitahu, mengingkarinya: yang pertama adalah Abū Bakr.',
   'Zayd b. Arqam mengatakan ʿAlī yang pertama — dan Ibrāhīm al-Nakhaʿī, apabila diberitahu, mengingkarinya: yang pertama ialah Abū Bakr.'),
 'Abū Dharr, al-Miqdād, Khabbāb, Jābir and Abū Saʿīd all put him first after Khadīja.':
  ('Abū Dharr, al-Miqdād, Khabbāb, Jābir dan Abū Saʿīd semuanya menempatkannya pertama setelah Khadīja.',
   'Abū Dharr, al-Miqdād, Khabbāb, Jābir dan Abū Saʿīd semuanya meletakkannya pertama selepas Khadīja.'),
 "He was at Badr, Uḥud, the Trench and the Pledge, and at every engagement but Tabūk, where he was left over the Prophet's household.":
  ('Ia ikut Badr, Uḥud, Khandaq dan Baiat Ridwan, dan semua peperangan kecuali Tabūk, di mana ia ditinggalkan mengurus keluarga Nabi ﷺ.',
   'Dia menyertai Badr, Uḥud, Khandaq dan Baiah Ridwan, dan semua peperangan kecuali Tabūk, ketika dia ditinggalkan menjaga keluarga Nabi ﷺ.'),
 'His feet were swollen and running with blood; the Prophet wept, spat on his hands and wiped them, and he never complained of them again.':
  ('Kedua kakinya bengkak dan meneteskan darah; Nabi ﷺ menangis, meludah pada kedua tangannya lalu mengusapnya, dan ia tak pernah lagi mengeluhkannya.',
   'Kedua-dua kakinya bengkak dan menitiskan darah; Nabi ﷺ menangis, meludah pada kedua-dua tangannya lalu menyapunya, dan dia tidak pernah lagi mengadu tentangnya.'),
 'His own account of the caliphate: they gave me their hands willingly and unforced, then broke it.':
  ('Penuturannya sendiri tentang kekhalifahan: mereka membaiatku dengan sukarela tanpa paksaan, lalu membatalkannya.',
   'Ceritanya sendiri tentang pemerintahan: mereka membaiahku dengan rela tanpa paksaan, kemudian membatalkannya.'),
 'Ṭalḥa pledged first with his tongue and Saʿd with his hand.':
  ('Ṭalḥa membaiat lebih dulu dengan lisannya dan Saʿd dengan tangannya.',
   'Ṭalḥa membaiah dahulu dengan lidahnya dan Saʿd dengan tangannya.'),
 "Ibn Muljam's price for marrying Quṭām, whose father and brother ʿAlī had killed at Nahrawān, was that he avenge them.":
  ('Syarat Quṭām untuk menikah dengan Ibn Muljam — ayah dan saudaranya dibunuh ʿAlī di Nahrawān — adalah agar ia membalaskan dendam mereka.',
   'Syarat Quṭām untuk berkahwin dengan Ibn Muljam — bapa dan saudaranya dibunuh ʿAlī di Nahrawān — ialah agar dia membalas dendam mereka.'),
 'When ʿAlī was dead and buried, al-Ḥasan had Ibn Muljam brought out of prison to be killed.':
  ('Setelah ʿAlī wafat dan dimakamkan, al-Ḥasan mengeluarkan Ibn Muljam dari penjara untuk dibunuh.',
   'Selepas ʿAlī wafat dan dikebumikan, al-Ḥasan mengeluarkan Ibn Muljam dari penjara untuk dibunuh.'),
 'His age is disputed, and his son Ibn al-Ḥanafiyya reckoned by it that he had outlived his father.':
  ('Usianya diperselisihkan, dan putranya Ibn al-Ḥanafiyya menghitung dengannya bahwa ia telah melampaui usia ayahnya.',
   'Usianya diperselisihkan, dan puteranya Ibn al-Ḥanafiyya mengira dengannya bahawa dia telah melampaui usia bapanya.'),
 'Ibn ʿAbd al-Barr opens on the point this whole site turns on: the scholars of genealogy do not differ over the line up to ʿAdnān.':
  ('Ibn ʿAbd al-Barr membuka dengan titik yang menjadi poros seluruh situs ini: para ahli nasab tidak berselisih tentang jalur sampai ʿAdnān.',
   'Ibn ʿAbd al-Barr membuka dengan titik yang menjadi paksi seluruh laman ini: para ahli nasab tidak berselisih tentang jalur hingga ʿAdnān.'),
 'Above ʿAdnān they do differ, and between Ibrāhīm and Sām b. Nūḥ, and he declines to set any of it down.':
  ('Di atas ʿAdnān mereka memang berselisih, juga antara Ibrāhīm dan Sām b. Nūḥ, dan ia menolak mencatat satu pun darinya.',
   'Di atas ʿAdnān mereka memang berselisih, juga antara Ibrāhīm dan Sām b. Nūḥ, dan dia enggan mencatat satu pun daripadanya.'),
 "For the narrowing he quotes the Prophet: God chose Kināna of Ismāʿīl's children, and Quraysh of Kināna, and Banū Hāshim of Quraysh, and me of Banū Hāshim.":
  ('Untuk penyempitannya ia mengutip Nabi ﷺ: Allah memilih Kināna dari anak Ismāʿīl, memilih Quraisy dari Kināna, memilih Banū Hāshim dari Quraisy, dan memilihku dari Banū Hāshim.',
   'Untuk penyempitannya dia memetik Nabi ﷺ: Allah memilih Kināna daripada anak Ismāʿīl, memilih Quraisy daripada Kināna, memilih Banū Hāshim daripada Quraisy, dan memilihku daripada Banū Hāshim.'),
 'Several names in the line are epithets. Hāshim was ʿAmr, called Hāshim for breaking bread for his people;':
  ('Beberapa nama dalam jalur ini adalah julukan. Hāshim adalah ʿAmr, disebut Hāshim karena ia meremuk roti untuk kaumnya;',
   'Beberapa nama dalam jalur ini ialah gelaran. Hāshim ialah ʿAmr, dipanggil Hāshim kerana dia meremukkan roti untuk kaumnya;'),
 'Quṣayy was Zayd, on the majority reading;':
  ('Quṣayy adalah Zayd, menurut bacaan mayoritas;',
   'Quṣayy ialah Zayd, menurut bacaan majoriti;'),
 'ʿAbd Manāf, it is said, was al-Mughīra.':
  ('ʿAbd Manāf, menurut satu pendapat, adalah al-Mughīra.',
   'ʿAbd Manāf, menurut satu pendapat, ialah al-Mughīra.'),
 'Of ʿAbd al-Muṭṭalib some say his name was ʿĀmir — Ibn ʿAbd al-Barr answers that this is not sound.':
  ('Tentang ʿAbd al-Muṭṭalib sebagian mengatakan namanya ʿĀmir — Ibn ʿAbd al-Barr menjawab bahwa itu tidak sahih.',
   'Tentang ʿAbd al-Muṭṭalib sebahagian mengatakan namanya ʿĀmir — Ibn ʿAbd al-Barr menjawab bahawa itu tidak sahih.'),
 'Others say Shayba, and that he was called ʿAbd al-Muṭṭalib because his father Hāshim, dying, told his brother al-Muṭṭalib to fetch his boy from Yathrib.':
  ('Yang lain mengatakan Shayba, dan bahwa ia disebut ʿAbd al-Muṭṭalib karena ayahnya Hāshim, menjelang wafat, menyuruh saudaranya al-Muṭṭalib menjemput anaknya dari Yathrib.',
   'Yang lain mengatakan Shayba, dan bahawa dia dipanggil ʿAbd al-Muṭṭalib kerana bapanya Hāshim, menjelang wafat, menyuruh saudaranya al-Muṭṭalib menjemput anaknya dari Yathrib.'),
 'His mother was Āmina bt. Wahb, of Zuhra.':
  ('Ibunya Āmina binti Wahb, dari Zuhra.',
   'Ibunya Āmina binti Wahb, daripada Zuhra.'),
 'ʿAbd Allāh married her at thirty, or at twenty-five.':
  ('ʿAbd Allāh menikahinya pada usia tiga puluh, atau dua puluh lima.',
   'ʿAbd Allāh mengahwininya pada usia tiga puluh, atau dua puluh lima.'),
 'There is no disagreement that he was born in the Year of the Elephant,':
  ('Tidak ada perselisihan bahwa beliau lahir pada Tahun Gajah,',
   'Tiada perselisihan bahawa baginda lahir pada Tahun Gajah,'),
 'though one report puts it a month after the Elephant came.':
  ('meski satu riwayat menempatkannya sebulan setelah Gajah datang.',
   'walaupun satu riwayat meletakkannya sebulan selepas Gajah datang.'),
 'The day is not disputed. Ibn ʿAbbās: your Prophet was born on a Monday, left Mecca on a Monday, entered Medina on a Monday, and Badr was a Monday.':
  ('Harinya tidak diperselisihkan. Ibn ʿAbbās: Nabi kalian lahir pada hari Senin, keluar dari Mekah pada hari Senin, masuk Madinah pada hari Senin, dan Badr pun hari Senin.',
   'Harinya tidak diperselisihkan. Ibn ʿAbbās: Nabi kamu lahir pada hari Isnin, keluar dari Mekah pada hari Isnin, masuk Madinah pada hari Isnin, dan Badr pun hari Isnin.'),
 'The month is: two nights into Rabīʿ al-Awwal, or twelve.':
  ('Bulannya: dua malam berlalu dari Rabīʿ al-Awwal, atau dua belas.',
   'Bulannya: dua malam berlalu dari Rabīʿ al-Awwal, atau dua belas.'),
 'His father died while his mother was still carrying him.':
  ('Ayahnya wafat ketika ibunya masih mengandungnya.',
   'Bapanya wafat ketika ibunya masih mengandungnya.'),
 "The first woman he married, and by the agreement of the Muslims the first of God's creation to enter Islam — no man and no woman before her.":
  ('Perempuan pertama yang beliau nikahi, dan menurut kesepakatan kaum Muslimin makhluk Allah yang pertama masuk Islam — tak ada lelaki maupun perempuan sebelumnya.',
   'Perempuan pertama yang baginda kahwini, dan menurut kesepakatan kaum Muslimin makhluk Allah yang pertama memeluk Islam — tiada lelaki mahupun perempuan sebelumnya.'),
 'al-Zubayr: in the Jāhiliyya she was called the Pure.':
  ('al-Zubayr: pada masa Jahiliah ia dipanggil al-Ṭāhira, yang suci.',
   'al-Zubayr: pada zaman Jahiliah dia dipanggil al-Ṭāhira, yang suci.'),
 'Her mother was Fāṭima bt. Zāʾida b. al-Aṣamm.':
  ('Ibunya Fāṭima binti Zāʾida b. al-Aṣamm.',
   'Ibunya Fāṭima binti Zāʾida b. al-Aṣamm.'),
 'She had been married before — to ʿAtīq b. ʿĀbid, who died leaving her a daughter, and then to Abū Hāla.':
  ('Ia pernah menikah sebelumnya — dengan ʿAtīq b. ʿĀbid, yang wafat meninggalkannya seorang putri, lalu dengan Abū Hāla.',
   'Dia pernah berkahwin sebelum itu — dengan ʿAtīq b. ʿĀbid, yang wafat meninggalkannya seorang puteri, kemudian dengan Abū Hāla.'),
 'The Prophet married her before the revelation, at twenty-five — or twenty-one — her uncle ʿAmr b. Asad giving her, her father being dead.':
  ('Nabi ﷺ menikahinya sebelum wahyu, pada usia dua puluh lima — atau dua puluh satu — pamannya ʿAmr b. Asad yang menikahkannya, karena ayahnya telah wafat.',
   'Nabi ﷺ mengahwininya sebelum wahyu, pada usia dua puluh lima — atau dua puluh satu — bapa saudaranya ʿAmr b. Asad yang mengahwinkannya, kerana bapanya telah wafat.'),
 'How many children she bore him is not settled, and Ibn al-Athīr lines the readings up.':
  ('Berapa anak yang ia lahirkan bagi beliau tidak dipastikan, dan Ibn al-Athīr menderetkan riwayat-riwayatnya.',
   'Berapa anak yang dia lahirkan bagi baginda tidak dipastikan, dan Ibn al-Athīr menderetkan riwayat-riwayatnya.'),
 'Some know of none but al-Qāsim and the four daughters.':
  ('Sebagian tidak mengetahui selain al-Qāsim dan empat putri.',
   'Sebahagian tidak mengetahui selain al-Qāsim dan empat orang puteri.'),
 'Qatāda: two boys and four girls.':
  ('Qatāda: dua anak lelaki dan empat anak perempuan.',
   'Qatāda: dua anak lelaki dan empat anak perempuan.'),
 'al-Zubayr: al-Qāsim the eldest, then Zaynab, then ʿAbd Allāh — who is called both al-Ṭayyib and al-Ṭāhir.':
  ('al-Zubayr: al-Qāsim yang sulung, lalu Zaynab, lalu ʿAbd Allāh — yang disebut al-Ṭayyib dan juga al-Ṭāhir.',
   'al-Zubayr: al-Qāsim yang sulung, kemudian Zaynab, kemudian ʿAbd Allāh — yang dipanggil al-Ṭayyib dan juga al-Ṭāhir.'),
 'al-Kalbī has ʿAbd Allāh born in Islam and all the rest before it.':
  ('Menurut al-Kalbī, ʿAbd Allāh lahir dalam Islam dan semua yang lain sebelumnya.',
   'Menurut al-Kalbī, ʿAbd Allāh lahir dalam Islam dan semua yang lain sebelumnya.'),
 'al-Qāsim, al-Ṭayyib and al-Ṭāhir died before Islam; the daughters lived to see it and migrated with him.':
  ('al-Qāsim, al-Ṭayyib dan al-Ṭāhir wafat sebelum Islam; putri-putrinya sempat menyaksikannya dan berhijrah bersama beliau.',
   'al-Qāsim, al-Ṭayyib dan al-Ṭāhir wafat sebelum Islam; puteri-puterinya sempat menyaksikannya dan berhijrah bersama baginda.'),
 'Ibn Isḥāq on what she was to him: she was the first to believe, and God lightened his burden through her — he never met a denial that she did not steady him after.':
  ('Ibn Isḥāq tentang kedudukannya bagi beliau: ia orang pertama yang beriman, dan Allah meringankan beban beliau melaluinya — tak sekali pun beliau menemui pendustaan tanpa ia meneguhkan beliau sesudahnya.',
   'Ibn Isḥāq tentang kedudukannya bagi baginda: dia orang pertama yang beriman, dan Allah meringankan beban baginda melaluinya — tidak sekali pun baginda menemui pendustaan tanpa dia meneguhkan baginda selepasnya.'),
 'She died three days after Abū Ṭālib, in Ramaḍān, and was buried at al-Ḥajūn.':
  ('Ia wafat tiga hari setelah Abū Ṭālib, pada bulan Ramadan, dan dimakamkan di al-Ḥajūn.',
   'Dia wafat tiga hari selepas Abū Ṭālib, pada bulan Ramadan, dan dikebumikan di al-Ḥajūn.'),
 'Her mother was Khadīja, and she was born while Quraysh were rebuilding the House, five years before the prophethood.':
  ('Ibunya Khadīja, dan ia lahir ketika Quraisy membangun kembali Kaʿbah, lima tahun sebelum kenabian.',
   'Ibunya Khadīja, dan dia lahir ketika Quraisy membina semula Kaʿbah, lima tahun sebelum kenabian.'),
 'Abū Bakr asked for her and was told to wait for the decree; ʿUmar asked and was told the same.':
  ('Abū Bakr meminangnya dan disuruh menunggu ketetapan; ʿUmar meminang dan dijawab sama.',
   'Abū Bakr meminangnya dan disuruh menunggu ketetapan; ʿUmar meminang dan dijawab sama.'),
 'Then: she is yours, ʿAlī — I am no liar; he had promised her to him already.':
  ('Lalu: ia untukmu, ʿAlī — aku bukan pendusta; beliau telah menjanjikannya kepadanya sebelum itu.',
   'Kemudian: dia untukmu, ʿAlī — aku bukan pendusta; baginda telah menjanjikannya kepadanya sebelum itu.'),
 'She and ʿAlī argued over which was older, and al-ʿAbbās settled it against her.':
  ('Ia dan ʿAlī berselisih siapa yang lebih tua, dan al-ʿAbbās memutuskannya tidak berpihak kepadanya.',
   'Dia dan ʿAlī berselisih siapa yang lebih tua, dan al-ʿAbbās memutuskannya tidak memihak kepadanya.'),
 'In his last illness he told her she would be the first of his family to follow him and she wept, then asked whether she would not be content to be mistress of the women of this community — and she laughed.':
  ('Dalam sakit terakhirnya beliau memberitahunya bahwa ia yang paling cepat menyusul beliau di antara keluarganya dan ia menangis, lalu beliau bertanya tidakkah ia rela menjadi penghulu kaum perempuan umat ini — dan ia tertawa.',
   'Dalam sakit terakhirnya baginda memberitahunya bahawa dia yang paling cepat menyusul baginda dalam kalangan keluarganya dan dia menangis, kemudian baginda bertanya tidakkah dia rela menjadi penghulu wanita umat ini — dan dia ketawa.'),
 "She asked Abū Bakr for her inheritance and he answered with the Prophet's words — we leave no heir, what we leave is charity — and she was angry.":
  ('Ia meminta warisannya kepada Abū Bakr dan ia menjawab dengan sabda Nabi ﷺ — kami tidak mewariskan, apa yang kami tinggalkan adalah sedekah — dan ia pun marah.',
   'Dia menuntut warisannya daripada Abū Bakr dan dijawab dengan sabda Nabi ﷺ — kami tidak mewariskan, apa yang kami tinggalkan ialah sedekah — dan dia pun marah.'),
 'How long she outlived her father is given two ways in the same chapter: six months,':
  ('Berapa lama ia hidup setelah ayahnya disebut dua cara dalam bab yang sama: enam bulan,',
   'Berapa lama dia hidup selepas bapanya disebut dua cara dalam bab yang sama: enam bulan,'),
 "and, on Abū Jaʿfar's authority, three.":
  ('dan, menurut Abū Jaʿfar, tiga bulan.',
   'dan, menurut Abū Jaʿfar, tiga bulan.'),
 'Hers was the first bier of its kind, made for her by Asmāʾ bt. ʿUmays, who had seen the like in Abyssinia.':
  ('Kerandanya yang pertama dari jenisnya, dibuatkan oleh Asmāʾ binti ʿUmays, yang pernah melihat yang serupa di Habasyah.',
   'Kerandanya yang pertama daripada jenisnya, dibuat oleh Asmāʾ binti ʿUmays, yang pernah melihat yang serupa di Habsyah.'),
 'al-Zuhrī: she was buried at night, and ʿAlī buried her.':
  ('al-Zuhrī: ia dimakamkan pada malam hari, dan ʿAlī yang memakamkannya.',
   'al-Zuhrī: dia dikebumikan pada waktu malam, dan ʿAlī yang mengebumikannya.'),
 'Ibn Saʿd heads him: the Lion of God, the Lion of His Messenger, and his uncle.':
  ('Ibn Saʿd membukanya: Singa Allah, Singa Rasul-Nya, dan pamannya.',
   'Ibn Saʿd membukanya: Singa Allah, Singa Rasul-Nya, dan bapa saudaranya.'),
 "His mother was Hāla bt. Uhayb, of Zuhra — so he and the Prophet's mother were of one clan.":
  ('Ibunya Hāla binti Uhayb, dari Zuhra — jadi ia dan ibu Nabi ﷺ berasal dari satu kabilah.',
   'Ibunya Hāla binti Uhayb, daripada Zuhra — jadi dia dan ibu Nabi ﷺ berasal daripada satu kabilah.'),
 'He entered Islam in anger: hearing Abū Jahl had abused the Prophet, he came into the mosque and split his head with a bow.':
  ('Ia masuk Islam dalam keadaan marah: mendengar Abū Jahl mencaci Nabi ﷺ, ia masuk masjid dan memecahkan kepalanya dengan busur.',
   'Dia memeluk Islam dalam keadaan marah: mendengar Abū Jahl mencaci Nabi ﷺ, dia masuk masjid dan memecahkan kepalanya dengan busur.'),
 'It was the sixth year of the prophethood, and the Prophet and the Muslims were strengthened by him.':
  ('Itu tahun keenam kenabian, dan Nabi ﷺ serta kaum Muslimin menjadi kuat karenanya.',
   'Itu tahun keenam kenabian, dan Nabi ﷺ serta kaum Muslimin menjadi kuat kerananya.'),
 'Waḥshī b. Ḥarb killed him at Uḥud and cut him open; Hind bt. ʿUtba chewed his liver and spat it out,':
  ('Waḥshī b. Ḥarb membunuhnya di Uḥud dan membelah perutnya; Hind binti ʿUtba mengunyah hatinya lalu memuntahkannya,',
   'Waḥshī b. Ḥarb membunuhnya di Uḥud dan membelah perutnya; Hind binti ʿUtba mengunyah hatinya lalu meludahkannya,'),
 'then made bracelets and anklets of what she took, and carried them to Mecca.':
  ('lalu membuat gelang tangan dan gelang kaki dari apa yang ia ambil, dan membawanya ke Mekah.',
   'kemudian membuat gelang tangan dan gelang kaki daripada apa yang dia ambil, dan membawanya ke Mekah.'),
 'His sister Ṣafiyya came looking for him and ʿAlī and al-Zubayr each pressed the other to tell her.':
  ('Saudarinya Ṣafiyya datang mencarinya dan ʿAlī serta al-Zubayr saling mendesak agar yang lain memberitahunya.',
   'Saudaranya Ṣafiyya datang mencarinya dan ʿAlī serta al-Zubayr saling mendesak agar yang lain memberitahunya.'),
 'The Prophet feared for her reason, put his hand on her breast and prayed, and she wept.':
  ('Nabi ﷺ khawatir akan akalnya, meletakkan tangannya di dadanya dan berdoa, lalu ia menangis.',
   'Nabi ﷺ bimbang akan akalnya, meletakkan tangan baginda di dadanya dan berdoa, lalu dia menangis.'),
 "Standing over the mutilated body: were it not for the women's grief I would leave him to be gathered from the crops of birds and the bellies of beasts.":
  ('Berdiri di atas jasad yang dicincang itu: kalau bukan karena kesedihan kaum perempuan, aku akan membiarkannya dihimpun dari tembolok burung dan perut binatang buas.',
   'Berdiri di atas jasad yang dicincang itu: kalau bukan kerana kesedihan kaum wanita, aku akan membiarkannya dihimpunkan dari tembolok burung dan perut binatang buas.'),
 'Abū Bakr, ʿUmar, ʿAlī and al-Zubayr went down into his grave while the Prophet sat at its edge.':
  ('Abū Bakr, ʿUmar, ʿAlī dan al-Zubayr turun ke liang kuburnya sementara Nabi ﷺ duduk di tepinya.',
   'Abū Bakr, ʿUmar, ʿAlī dan al-Zubayr turun ke liang kuburnya sementara Nabi ﷺ duduk di tepinya.'),
 "He said he had seen the angels washing Ḥamza, and Ḥamza was the first of that day's martyrs he prayed over, with four takbīrs.":
  ('Beliau berkata telah melihat malaikat memandikan Ḥamza, dan Ḥamza syuhada pertama hari itu yang beliau salatkan, dengan empat takbir.',
   'Baginda berkata telah melihat malaikat memandikan Ḥamza, dan Ḥamza syuhada pertama hari itu yang baginda solatkan, dengan empat takbir.'),
 "Son of ʿAlī and of Fāṭima, and so grandson of Khadīja on his mother's side.":
  ('Putra ʿAlī dan Fāṭima, jadi cucu Khadīja dari pihak ibunya.',
   'Putera ʿAlī dan Fāṭima, jadi cucu Khadīja daripada pihak ibunya.'),
 'Born in the middle of Ramaḍān, year three.':
  ('Lahir pada pertengahan Ramadan, tahun ketiga.',
   'Lahir pada pertengahan Ramadan, tahun ketiga.'),
 'ʿAlī: I loved war, and meant to name him Ḥarb — the Messenger of God named him al-Ḥasan.':
  ('ʿAlī: aku mencintai perang, dan hendak menamainya Ḥarb — Rasulullah ﷺ menamainya al-Ḥasan.',
   'ʿAlī: aku mencintai perang, dan hendak menamakannya Ḥarb — Rasulullah ﷺ menamakannya al-Ḥasan.'),
 "And of the second: I named these two sons of mine after Hārūn's sons, Shabbar and Shubayr.":
  ('Dan tentang yang kedua: aku menamai dua putraku ini dengan nama dua putra Hārūn, Shabbar dan Shubayr.',
   'Dan tentang yang kedua: aku menamakan dua puteraku ini dengan nama dua putera Hārūn, Shabbar dan Shubayr.'),
 'Abū Saʿīd al-Khudrī reports the Prophet: al-Ḥasan and al-Ḥusayn are the two lords of the youth of Paradise.':
  ('Abū Saʿīd al-Khudrī meriwayatkan sabda Nabi ﷺ: al-Ḥasan dan al-Ḥusayn adalah dua penghulu pemuda ahli surga.',
   'Abū Saʿīd al-Khudrī meriwayatkan sabda Nabi ﷺ: al-Ḥasan dan al-Ḥusayn ialah dua penghulu pemuda ahli syurga.'),
 'ʿAlī: al-Ḥasan was likest the Messenger of God from the chest to the head.':
  ('ʿAlī: al-Ḥasan paling mirip Rasulullah ﷺ dari dada hingga kepala.',
   'ʿAlī: al-Ḥasan paling mirip Rasulullah ﷺ dari dada hingga kepala.'),
 'Dying, he pressed his brother: do not let blood be spilt over me, the people are quick to strife.':
  ('Menjelang wafat ia berpesan kepada saudaranya: jangan sampai darah tertumpah karena aku, orang-orang cepat terseret fitnah.',
   'Menjelang wafat dia berpesan kepada saudaranya: jangan sampai darah tertumpah kerana aku, orang ramai cepat terseret fitnah.'),
 'He asked to be buried with the Prophet — and that if he were prevented, and a cupping-glass of blood were feared over it, he be buried with his mother at al-Baqīʿ instead.':
  ('Ia berwasiat agar dimakamkan bersama Nabi ﷺ — dan jika dihalangi, dan dikhawatirkan tertumpah setetes darah karenanya, agar dimakamkan bersama ibunya di al-Baqīʿ.',
   'Dia berwasiat agar dikebumikan bersama Nabi ﷺ — dan jika dihalang, dan dibimbangi tertumpah setitis darah kerananya, agar dikebumikan bersama ibunya di al-Baqīʿ.'),
 'When he died Medina shook with the cry of it, and you met nobody who was not weeping.':
  ('Ketika ia wafat Madinah berguncang oleh tangisan, dan tak seorang pun yang engkau temui kecuali menangis.',
   'Ketika dia wafat Madinah bergegar dengan tangisan, dan tiada seorang pun yang engkau temui melainkan menangis.'),
 'Son of ʿAlī, called Abū ʿAbd Allāh.':
  ('Putra ʿAlī, berkunyah Abū ʿAbd Allāh.',
   'Putera ʿAlī, berkunyah Abū ʿAbd Allāh.'),
 "His mother was Fāṭima, and hers was Khadīja — the wording is all but identical to al-Ḥasan's entry a few pages earlier.":
  ('Ibunya Fāṭima, dan ibu Fāṭima adalah Khadīja — susunan katanya nyaris sama persis dengan entri al-Ḥasan beberapa halaman sebelumnya.',
   'Ibunya Fāṭima, dan ibu Fāṭima ialah Khadīja — susunan katanya hampir sama dengan entri al-Ḥasan beberapa halaman sebelumnya.'),
 "Ibn Saʿd dates the conception: five nights into Dhū al-Qaʿda of year three, fifty nights after al-Ḥasan's birth, and the birth in Shaʿbān of year four.":
  ('Ibn Saʿd menetapkan waktu mengandungnya: lima malam berlalu dari Dhū al-Qaʿda tahun ketiga, lima puluh malam setelah kelahiran al-Ḥasan, dan kelahirannya pada Shaʿbān tahun keempat.',
   'Ibn Saʿd menetapkan waktu mengandungnya: lima malam berlalu dari Dhū al-Qaʿda tahun ketiga, lima puluh malam selepas kelahiran al-Ḥasan, dan kelahirannya pada Shaʿbān tahun keempat.'),
 "Umm al-Faḍl asked to nurse him, brought him to the Prophet, and he wet his waist-wrapper; he told her a boy's water is poured over and a girl's washed.":
  ('Umm al-Faḍl meminta menyusuinya, membawanya kepada Nabi ﷺ, dan ia mengencingi sarung beliau; beliau berkata air kencing bayi lelaki cukup disiram dan bayi perempuan dicuci.',
   'Umm al-Faḍl meminta menyusukannya, membawanya kepada Nabi ﷺ, dan dia mengencingi kain baginda; baginda berkata air kencing bayi lelaki cukup disiram dan bayi perempuan dibasuh.'),
 'On the road he woke saying he had dreamt of a horseman keeping pace with them: the people travel, and the deaths travel towards them.':
  ('Di perjalanan ia terbangun dan berkata bermimpi melihat penunggang kuda berjalan seiring mereka: kaum itu berjalan, dan ajal berjalan menuju mereka.',
   'Di perjalanan dia terjaga dan berkata bermimpi melihat penunggang kuda berjalan seiring mereka: kaum itu berjalan, dan ajal berjalan menuju mereka.'),
 'He knew it for a death-notice, and rode on until he halted at Karbalāʾ.':
  ('Ia tahu itu berita kematian, dan terus berjalan hingga singgah di Karbalāʾ.',
   'Dia tahu itu berita kematian, dan terus berjalan sehingga singgah di Karbalāʾ.'),
 'His eldest son ʿAlī was killed with him at al-Ṭaff and left no line.':
  ('Putra sulungnya ʿAlī terbunuh bersamanya di al-Ṭaff dan tidak meninggalkan keturunan.',
   'Putera sulungnya ʿAlī terbunuh bersamanya di al-Ṭaff dan tidak meninggalkan keturunan.'),
 'The Prophet: al-Ḥusayn is of me and I am of him — God love whoever loves al-Ḥusayn.':
  ('Nabi ﷺ: al-Ḥusayn dariku dan aku darinya — Allah mencintai siapa yang mencintai al-Ḥusayn.',
   'Nabi ﷺ: al-Ḥusayn daripadaku dan aku daripadanya — Allah mencintai sesiapa yang mencintai al-Ḥusayn.'),
 'ʿAlī counted him the likest of his family to himself, and said al-Ḥasan would step out of the command.':
  ('ʿAlī menganggapnya yang paling mirip dengan dirinya di antara keluarganya, dan berkata al-Ḥasan akan keluar dari urusan kekhalifahan.',
   'ʿAlī menganggapnya yang paling mirip dengan dirinya dalam kalangan keluarganya, dan berkata al-Ḥasan akan keluar daripada urusan pemerintahan.'),
 "When Muʿāwiya took the people's pledge for Yazīd, al-Ḥusayn was among those who did not give it.":
  ('Ketika Muʿāwiya mengambil baiat orang-orang untuk Yazīd, al-Ḥusayn termasuk yang tidak membaiatnya.',
   'Ketika Muʿāwiya mengambil baiah orang ramai untuk Yazīd, al-Ḥusayn termasuk yang tidak membaiahnya.'),
 "The people of Kūfa had been writing to him to come out to them since Muʿāwiya's time, and each time he refused.":
  ('Penduduk Kūfa telah menyurati agar ia keluar kepada mereka sejak zaman Muʿāwiya, dan setiap kali ia menolak.',
   'Penduduk Kūfa telah menyurat agar dia keluar kepada mereka sejak zaman Muʿāwiya, dan setiap kali dia menolak.'),
 "Muslim b. ʿAqīl's last message was to turn him back: the people have deceived him and lied to him.":
  ('Pesan terakhir Muslim b. ʿAqīl adalah agar ia berbalik: kaum itu telah menipunya dan mendustainya.',
   'Pesanan terakhir Muslim b. ʿAqīl ialah agar dia berpatah balik: kaum itu telah menipunya dan mendustainya.'),
 'A man who went to look afterwards found his body, and his companions lying in a ring around him.':
  ('Seseorang yang pergi melihat sesudahnya menemukan jasadnya, dan para sahabatnya terbaring melingkarinya.',
   'Seseorang yang pergi melihat selepas itu menemui jasadnya, dan para sahabatnya terbaring mengelilinginya.'),
 'They found thirty-three wounds on him, and in his garment a hundred and some rents from arrows and blows. He was killed on a Friday, the day of ʿĀshūrāʾ, in Muḥarram of the year sixty-one, aged fifty-six years and five months.':
  ('Mereka mendapati tiga puluh tiga luka padanya, dan pada pakaiannya seratus lebih koyakan dari anak panah dan pukulan. Ia terbunuh pada hari Jumat, hari ʿĀshūrāʾ, bulan Muharram tahun enam puluh satu, dalam usia lima puluh enam tahun lima bulan.',
   'Mereka mendapati tiga puluh tiga luka padanya, dan pada pakaiannya seratus lebih koyakan daripada anak panah dan pukulan. Dia terbunuh pada hari Jumaat, hari ʿĀshūrāʾ, bulan Muharram tahun enam puluh satu, dalam usia lima puluh enam tahun lima bulan.'),
 'His mother was Nutayla bt. Janāb, of al-Namir b. Qāsiṭ — not a Qurashī woman.':
  ('Ibunya Nutayla binti Janāb, dari al-Namir b. Qāsiṭ — bukan perempuan Quraisy.',
   'Ibunya Nutayla binti Janāb, daripada al-Namir b. Qāsiṭ — bukan wanita Quraisy.'),
 'His son Ibn ʿAbbās: my father was born three years before the men of the Elephant came, and was three years older than the Messenger of God.':
  ('Putranya Ibn ʿAbbās: ayahku lahir tiga tahun sebelum pasukan Gajah datang, dan tiga tahun lebih tua dari Rasulullah ﷺ.',
   'Puteranya Ibn ʿAbbās: bapaku lahir tiga tahun sebelum tentera Gajah datang, dan tiga tahun lebih tua daripada Rasulullah ﷺ.'),
 "When al-Aws and al-Khazraj argued over who first struck the Prophet's hand at al-ʿAqaba, they asked al-ʿAbbās, who said nobody knew it better than he did.":
  ('Ketika al-Aws dan al-Khazraj berbantah siapa yang pertama membaiat Nabi ﷺ di al-ʿAqaba, mereka bertanya kepada al-ʿAbbās, yang berkata tak ada yang lebih tahu tentangnya darinya.',
   'Ketika al-Aws dan al-Khazraj berbalah siapa yang pertama membaiah Nabi ﷺ di al-ʿAqaba, mereka bertanya kepada al-ʿAbbās, yang berkata tiada yang lebih tahu tentangnya daripadanya.'),
 'Taken at Badr, he ransomed himself and his nephew ʿAqīl for eighty ounces of gold — or, it is said, a thousand dīnārs.':
  ('Ditawan di Badr, ia menebus dirinya dan keponakannya ʿAqīl dengan delapan puluh uqiyah emas — atau, menurut satu riwayat, seribu dinar.',
   'Ditawan di Badr, dia menebus dirinya dan anak saudaranya ʿAqīl dengan lapan puluh auns emas — atau, menurut satu riwayat, seribu dinar.'),
 "He, Nawfal and ʿAqīl were sent back to Mecca to keep up the watering and the provisioning, which had been Banū Hāshim's since the Jāhiliyya.":
  ('Ia, Nawfal dan ʿAqīl dikembalikan ke Mekah untuk meneruskan siqāyah dan rifādah, yang menjadi milik Banū Hāshim sejak Jahiliah.',
   'Dia, Nawfal dan ʿAqīl dihantar balik ke Mekah untuk meneruskan siqāyah dan rifādah, yang menjadi milik Banū Hāshim sejak Jahiliah.'),
 "The Prophet, pressed about his alms: a man's uncle is his father's twin — al-ʿAbbās paid us this year's zakāt a year early.":
  ('Nabi ﷺ, ketika didesak soal zakatnya: paman seseorang adalah saudara kembar ayahnya — al-ʿAbbās telah membayar zakat tahun ini setahun lebih awal.',
   'Nabi ﷺ, apabila didesak tentang zakatnya: bapa saudara seseorang ialah kembar bapanya — al-ʿAbbās telah membayar zakat tahun ini setahun lebih awal.'),
 "In drought under ʿUmar he was brought out to pray for rain: we used to ask through Your Prophet, and now we ask through Your Prophet's uncle.":
  ('Pada masa kemarau di zaman ʿUmar ia dibawa keluar untuk salat istisqa: dahulu kami bertawasul dengan Nabi-Mu, dan kini kami bertawasul dengan paman Nabi-Mu.',
   'Pada musim kemarau di zaman ʿUmar dia dibawa keluar untuk solat istisqa: dahulu kami bertawassul dengan Nabi-Mu, dan kini kami bertawassul dengan bapa saudara Nabi-Mu.'),
 'He died on a Friday, fourteen nights into Rajab of the year thirty-two, aged eighty-eight, and was buried at al-Baqīʿ in the burial-ground of Banū Hāshim.':
  ('Ia wafat pada hari Jumat, empat belas malam berlalu dari Rajab tahun tiga puluh dua, dalam usia delapan puluh delapan, dan dimakamkan di al-Baqīʿ di pekuburan Banū Hāshim.',
   'Dia wafat pada hari Jumaat, empat belas malam berlalu dari Rejab tahun tiga puluh dua, dalam usia lapan puluh lapan, dan dikebumikan di al-Baqīʿ di perkuburan Banū Hāshim.'),
 'Brother of ʿAlī by the same mother, Fāṭima bt. Asad.':
  ('Saudara ʿAlī seibu, Fāṭima binti Asad.',
   'Saudara ʿAlī seibu, Fāṭima binti Asad.'),
 'His three sons — ʿAbd Allāh, ʿAwn and Muḥammad — were all born to him in Abyssinia during the migration there.':
  ('Ketiga putranya — ʿAbd Allāh, ʿAwn dan Muḥammad — semuanya lahir baginya di Habasyah selama hijrah ke sana.',
   'Ketiga-tiga puteranya — ʿAbd Allāh, ʿAwn dan Muḥammad — semuanya lahir baginya di Habsyah semasa hijrah ke sana.'),
 'Their mother was Asmāʾ bt. ʿUmays, who later married Abū Bakr and then ʿAlī: her sons by the three were half-brothers.':
  ('Ibu mereka Asmāʾ binti ʿUmays, yang kemudian menikah dengan Abū Bakr lalu ʿAlī: putra-putranya dari ketiganya bersaudara seibu.',
   'Ibu mereka Asmāʾ binti ʿUmays, yang kemudian berkahwin dengan Abū Bakr lalu ʿAlī: putera-puteranya daripada ketiga-tiganya bersaudara seibu.'),
 'An eyewitness at Muʾta: I can still see Jaʿfar dismounting from a sorrel mare and hamstringing her, then fighting until he was killed.':
  ('Seorang saksi mata di Muʾta: aku seakan masih melihat Jaʿfar turun dari kuda betina merahnya lalu menyembelihnya, kemudian bertempur sampai terbunuh.',
   'Seorang saksi mata di Muʾta: aku seakan masih melihat Jaʿfar turun daripada kuda betina merahnya lalu menyembelihnya, kemudian bertempur sehingga terbunuh.'),
 "He was killed at al-Balqāʾ on the day of Muʾta, and the Prophet prayed: God, take Jaʿfar's place in his family.":
  ('Ia terbunuh di al-Balqāʾ pada hari Muʾta, dan Nabi ﷺ berdoa: ya Allah, gantikanlah Jaʿfar bagi keluarganya.',
   'Dia terbunuh di al-Balqāʾ pada hari Muʾta, dan Nabi ﷺ berdoa: ya Allah, gantikanlah Jaʿfar bagi keluarganya.'),
 "Khadīja's daughter, and the eldest of the Prophet's daughters.":
  ('Putri Khadīja, dan yang sulung di antara putri-putri Nabi ﷺ.',
   'Puteri Khadīja, dan yang sulung dalam kalangan puteri-puteri Nabi ﷺ.'),
 "She married her mother's sister's son, Abū al-ʿĀṣ b. al-Rabīʿ, before the prophethood — the first of the daughters to marry.":
  ('Ia menikah dengan putra bibinya, Abū al-ʿĀṣ b. al-Rabīʿ, sebelum kenabian — putri pertama yang menikah.',
   'Dia berkahwin dengan anak emak saudaranya, Abū al-ʿĀṣ b. al-Rabīʿ, sebelum kenabian — puteri pertama yang berkahwin.'),
 "His mother Hāla bt. Khuwaylid was Khadīja's sister, and so Zaynab's aunt.":
  ('Ibunya Hāla binti Khuwaylid adalah saudari Khadīja, jadi bibi Zaynab.',
   'Ibunya Hāla binti Khuwaylid ialah saudara Khadīja, jadi emak saudara Zaynab.'),
 'She bore him ʿAlī, who died young, and Umāma.':
  ('Ia melahirkan baginya ʿAlī, yang wafat kecil, dan Umāma.',
   'Dia melahirkan baginya ʿAlī, yang wafat semasa kecil, dan Umāma.'),
 'She entered Islam and migrated with her father while her husband was still in Syria and still a pagan.':
  ('Ia masuk Islam dan berhijrah bersama ayahnya sementara suaminya masih di Syam dan masih musyrik.',
   'Dia memeluk Islam dan berhijrah bersama bapanya sementara suaminya masih di Syam dan masih musyrik.'),
 'Later she gave him protection, and the Prophet upheld it: the believers are one hand against all others, and the least of them may grant protection.':
  ('Kemudian ia memberinya jaminan keamanan, dan Nabi ﷺ mengukuhkannya: kaum mukmin satu tangan atas selain mereka, dan yang paling rendah di antara mereka boleh memberi jaminan.',
   'Kemudian dia memberinya jaminan keselamatan, dan Nabi ﷺ mengesahkannya: kaum mukmin satu tangan atas selain mereka, dan yang paling rendah antara mereka boleh memberi jaminan.'),
 'She asked that what had been taken from him be returned, and he ordered it — but told her he could not come near her while he remained a pagan.':
  ('Ia meminta agar apa yang diambil darinya dikembalikan, dan beliau memerintahkannya — tetapi berkata kepadanya bahwa suaminya tidak halal mendekatinya selama masih musyrik.',
   'Dia meminta agar apa yang diambil daripadanya dipulangkan, dan baginda memerintahkannya — tetapi memberitahunya bahawa suaminya tidak halal mendekatinya selagi masih musyrik.'),
 'Qatāda: she migrated with her father, then her husband became Muslim and migrated after her, and the Prophet returned her to him.':
  ('Qatāda: ia berhijrah bersama ayahnya, lalu suaminya masuk Islam dan berhijrah menyusulnya, dan Nabi ﷺ mengembalikannya kepadanya.',
   'Qatāda: dia berhijrah bersama bapanya, kemudian suaminya memeluk Islam dan berhijrah menyusulnya, dan Nabi ﷺ mengembalikannya kepadanya.'),
 'Ibn Saʿd puts his story where it starts: the letter carried to the Muqawqis of Alexandria after al-Ḥudaybiya, in Dhū al-Qaʿda of year six.':
  ('Ibn Saʿd memulai kisahnya dari awalnya: surat yang dibawa kepada al-Muqawqis di Iskandariyah setelah al-Ḥudaybiya, pada Dhū al-Qaʿda tahun keenam.',
   'Ibn Saʿd memulakan kisahnya dari awalnya: surat yang dibawa kepada al-Muqawqis di Iskandariah selepas al-Ḥudaybiya, pada Dhū al-Qaʿda tahun keenam.'),
 'Anas: when Ibrāhīm was born Jibrīl came and greeted him — peace be upon you, father of Ibrāhīm.':
  ('Anas: ketika Ibrāhīm lahir, Jibrīl datang dan memberi salam — salam sejahtera atasmu, wahai ayah Ibrāhīm.',
   'Anas: ketika Ibrāhīm lahir, Jibrīl datang dan memberi salam — salam sejahtera atasmu, wahai bapa Ibrāhīm.'),
 "He came out in the morning and said: a boy was born to me last night, and I have named him with my father's name, Ibrāhīm.":
  ('Beliau keluar pada pagi hari dan berkata: tadi malam lahir seorang putra bagiku, dan aku menamainya dengan nama ayahku, Ibrāhīm.',
   'Baginda keluar pada waktu pagi dan berkata: malam tadi lahir seorang putera bagiku, dan aku menamakannya dengan nama bapaku, Ibrāhīm.'),
 'He brought him to ʿĀʾisha: look how like me he is. She saw no likeness. He said: do you not see his whiteness and his flesh?':
  ('Beliau membawanya kepada ʿĀʾisha: lihatlah betapa miripnya denganku. ʿĀʾisha tidak melihat kemiripan. Beliau berkata: tidakkah engkau lihat putihnya dan dagingnya?',
   'Baginda membawanya kepada ʿĀʾisha: lihatlah betapa miripnya dengan aku. ʿĀʾisha tidak melihat kemiripan. Baginda berkata: tidakkah engkau lihat putihnya dan dagingnya?'),
 'At his death: the heart will grieve and the eye will weep, and we will not say what angers the Lord.':
  ('Ketika ia wafat: hati bersedih dan mata menangis, dan kami tidak mengucapkan apa yang membuat Tuhan murka.',
   'Ketika dia wafat: hati bersedih dan mata menangis, dan kami tidak mengucapkan apa yang membuat Tuhan murka.'),
 'And: were it not for an appointed term and a known hour, our grief for you would be harder than it is — we are grieved for you, Ibrāhīm.':
  ('Dan: kalau bukan karena ajal yang ditetapkan dan waktu yang diketahui, kesedihan kami atasmu akan lebih berat dari ini — kami bersedih atasmu, wahai Ibrāhīm.',
   'Dan: kalau bukan kerana ajal yang ditetapkan dan waktu yang diketahui, kesedihan kami atasmu akan lebih berat daripada ini — kami bersedih atasmu, wahai Ibrāhīm.'),
 'Qatāda adds the words: the rest of his suckling is in the Garden.':
  ('Qatāda menambahkan sabda: sisa penyusuannya disempurnakan di surga.',
   'Qatāda menambah sabda: baki penyusuannya disempurnakan di syurga.'),
 'And: Ibrāhīm is my son, and he died at the breast, and he has two nurses who will finish his suckling in the Garden.':
  ('Dan: Ibrāhīm adalah putraku, ia wafat saat masih menyusu, dan baginya dua ibu susu yang akan menyempurnakan penyusuannya di surga.',
   'Dan: Ibrāhīm ialah puteraku, dia wafat semasa masih menyusu, dan baginya dua ibu susu yang akan menyempurnakan penyusuannya di syurga.'),
 'Ibn al-Athīr heads her the truthful daughter of the truthful, and the best known of his wives.':
  ('Ibn al-Athīr menyebutnya al-Ṣiddīqa putri al-Ṣiddīq, dan yang paling masyhur di antara istri-istri beliau.',
   'Ibn al-Athīr menyebutnya al-Ṣiddīqa puteri al-Ṣiddīq, dan yang paling masyhur dalam kalangan isteri-isteri baginda.'),
 'Her mother was Umm Rūmān, of Kināna.':
  ('Ibunya Umm Rūmān, dari Kināna.',
   'Ibunya Umm Rūmān, daripada Kināna.'),
 "He married her two years before the Hijra, on Abū ʿUbayda's reckoning — or three.":
  ('Beliau menikahinya dua tahun sebelum Hijrah, menurut perhitungan Abū ʿUbayda — atau tiga tahun.',
   'Baginda mengahwininya dua tahun sebelum Hijrah, menurut kiraan Abū ʿUbayda — atau tiga tahun.'),
 'Her age at the marriage is given as six, and as seven.':
  ('Usianya saat pernikahan disebut enam tahun, dan tujuh tahun.',
   'Usianya ketika perkahwinan disebut enam tahun, dan tujuh tahun.'),
 'When the Prophet died she was eighteen.':
  ('Ketika Nabi ﷺ wafat ia berusia delapan belas tahun.',
   'Ketika Nabi ﷺ wafat dia berusia lapan belas tahun.'),
 'ʿUrwa: I never saw anyone better versed in law, or medicine, or poetry than ʿĀʾisha — and had she nothing but the affair of the slander, that alone would be honour enough, for Qurʾān came down about her that is recited to the Day of Rising.':
  ('ʿUrwa: aku tak pernah melihat seorang pun yang lebih paham fikih, atau kedokteran, atau syair daripada ʿĀʾisha — dan andai ia tak punya keutamaan selain peristiwa al-ifk, itu saja sudah cukup sebagai kemuliaan, sebab turun tentangnya ayat al-Qurʾān yang dibaca sampai Hari Kiamat.',
   'ʿUrwa: aku tidak pernah melihat seorang pun yang lebih memahami fiqh, atau perubatan, atau syair daripada ʿĀʾisha — dan andai dia tiada keutamaan selain peristiwa al-ifk, itu sahaja sudah cukup sebagai kemuliaan, kerana turun tentangnya ayat al-Qurʾān yang dibaca hingga Hari Kiamat.'),
 "Anas reports the Prophet: ʿĀʾisha's excellence over women is that of tharīd over other food.":
  ('Anas meriwayatkan sabda Nabi ﷺ: keutamaan ʿĀʾisha atas kaum perempuan seperti keutamaan tharīd atas makanan lainnya.',
   'Anas meriwayatkan sabda Nabi ﷺ: keutamaan ʿĀʾisha atas kaum wanita seperti keutamaan tharīd atas makanan lain.'),
 'The senior Companions asked her on the law of inheritance, and ʿAṭāʾ called her the soundest of people in public judgement.':
  ('Para sahabat senior bertanya kepadanya tentang ilmu faraid, dan ʿAṭāʾ menyebutnya orang yang paling baik pendapatnya dalam urusan umum.',
   'Para sahabat kanan bertanya kepadanya tentang ilmu faraid, dan ʿAṭāʾ menyebutnya orang yang paling baik pendapatnya dalam urusan awam.'),
 'Masrūq, when he transmitted from her, would say: the truthful daughter of the truthful told me, the innocent, the vindicated.':
  ('Masrūq, bila meriwayatkan darinya, berkata: telah menceritakan kepadaku al-Ṣiddīqa putri al-Ṣiddīq, yang bersih lagi dibersihkan.',
   'Masrūq, apabila meriwayatkan daripadanya, berkata: telah menceritakan kepadaku al-Ṣiddīqa puteri al-Ṣiddīq, yang bersih lagi dibersihkan.'),
 'She was buried at al-Baqīʿ by night as she had asked, Abū Hurayra praying over her and five of her kin going down into the grave.':
  ('Ia dimakamkan di al-Baqīʿ pada malam hari sesuai permintaannya, Abū Hurayra menyalatinya dan lima orang kerabatnya turun ke liang kubur.',
   'Dia dikebumikan di al-Baqīʿ pada waktu malam sesuai permintaannya, Abū Hurayra menyembahyangkannya dan lima orang kerabatnya turun ke liang kubur.'),
 'Her mother, al-Shamūs bt. Qays, was of the Anṣār, of Banū ʿAdī b. al-Najjār.':
  ('Ibunya, al-Shamūs binti Qays, dari kaum Anṣār, dari Banū ʿAdī b. al-Najjār.',
   'Ibunya, al-Shamūs binti Qays, daripada kaum Anṣār, daripada Banū ʿAdī b. al-Najjār.'),
 'She had married al-Sakrān b. ʿAmr; both entered Islam early at Mecca and both went out to Abyssinia in the second migration.':
  ('Ia menikah dengan al-Sakrān b. ʿAmr; keduanya masuk Islam sejak dini di Mekah dan keduanya berangkat ke Habasyah pada hijrah kedua.',
   'Dia berkahwin dengan al-Sakrān b. ʿAmr; kedua-duanya memeluk Islam awal di Mekah dan kedua-duanya berangkat ke Habsyah pada hijrah kedua.'),
 'Widowed at Mecca, she had Ḥāṭib b. ʿAmr marry her to the Prophet: the first woman he married after Khadīja.':
  ('Setelah menjanda di Mekah, ia meminta Ḥāṭib b. ʿAmr menikahkannya dengan Nabi ﷺ: perempuan pertama yang beliau nikahi setelah Khadīja.',
   'Selepas menjanda di Mekah, dia meminta Ḥāṭib b. ʿAmr mengahwinkannya dengan Nabi ﷺ: wanita pertama yang baginda kahwini selepas Khadīja.'),
 'He said to her once: count your waiting-period.':
  ('Beliau pernah berkata kepadanya: berʿiddahlah.',
   'Baginda pernah berkata kepadanya: berʿiddahlah.'),
 "ʿĀʾisha: Sawda gave her day and her night to me, seeking by it the Messenger of God's contentment.":
  ('ʿĀʾisha: Sawda memberikan hari dan malamnya kepadaku, mencari dengan itu keridaan Rasulullah ﷺ.',
   'ʿĀʾisha: Sawda memberikan hari dan malamnya kepadaku, mencari dengan itu keredaan Rasulullah ﷺ.'),
 'Her portion of Khaybar was eighty loads of dates and twenty of barley — or of wheat.':
  ("Bagiannya dari Khaybar delapan puluh wasaq kurma dan dua puluh wasaq gandum sya'ir — atau gandum burr.",
   'Bahagiannya daripada Khaybar lapan puluh wasaq kurma dan dua puluh wasaq barli — atau gandum.'),
 'She died at Medina in Shawwāl of the year fifty-four.':
  ('Ia wafat di Madinah pada Shawwāl tahun lima puluh empat.',
   'Dia wafat di Madinah pada Syawal tahun lima puluh empat.'),
 'Her mother was Zaynab bt. Maẓʿūn, sister of ʿUthmān b. Maẓʿūn.':
  ('Ibunya Zaynab binti Maẓʿūn, saudari ʿUthmān b. Maẓʿūn.',
   'Ibunya Zaynab binti Maẓʿūn, saudara ʿUthmān b. Maẓʿūn.'),
 'ʿUmar: Ḥafṣa was born while Quraysh were building the House, five years before the Prophet was sent.':
  ('ʿUmar: Ḥafṣa lahir ketika Quraisy membangun Kaʿbah, lima tahun sebelum Nabi ﷺ diutus.',
   'ʿUmar: Ḥafṣa lahir ketika Quraisy membina Kaʿbah, lima tahun sebelum Nabi ﷺ diutus.'),
 'She had been married to Khunays b. Ḥudhāfa, migrated with him, and was widowed after Badr.':
  ('Ia pernah menikah dengan Khunays b. Ḥudhāfa, berhijrah bersamanya, dan menjanda setelah Badr.',
   'Dia pernah berkahwin dengan Khunays b. Ḥudhāfa, berhijrah bersamanya, dan menjanda selepas Badr.'),
 'Anas: when the Prophet divorced Ḥafṣa he was commanded to take her back, and he took her back.':
  ('Anas: ketika Nabi ﷺ menceraikan Ḥafṣa, beliau diperintahkan merujuknya, dan beliau merujuknya.',
   'Anas: ketika Nabi ﷺ menceraikan Ḥafṣa, baginda diperintahkan merujuknya, dan baginda merujuknya.'),
 'The reason given: Jibrīl came and said, take Ḥafṣa back, for she fasts much and stands much in prayer, and she is your wife in the Garden.':
  ('Alasan yang disebut: Jibrīl datang dan berkata, rujuklah Ḥafṣa, sebab ia banyak berpuasa dan banyak salat malam, dan ia istrimu di surga.',
   'Sebab yang disebut: Jibrīl datang dan berkata, rujuklah Ḥafṣa, kerana dia banyak berpuasa dan banyak bersolat malam, dan dia isterimu di syurga.'),
 'She was party to the trick of the honey, agreed between the wives to make him think a smell displeased him.':
  ('Ia terlibat dalam siasat madu, yang disepakati para istri agar beliau mengira ada bau yang tidak beliau sukai.',
   'Dia terlibat dalam helah madu, yang dipersetujui para isteri agar baginda menyangka ada bau yang tidak baginda sukai.'),
 'Her portion of Khaybar was eighty loads of barley — or of wheat.':
  ("Bagiannya dari Khaybar delapan puluh wasaq gandum sya'ir — atau gandum burr.",
   'Bahagiannya daripada Khaybar lapan puluh wasaq barli — atau gandum.'),
 'Marwān b. al-Ḥakam, then governor of Medina, prayed over her.':
  ('Marwān b. al-Ḥakam, saat itu gubernur Madinah, menyalatinya.',
   'Marwān b. al-Ḥakam, ketika itu gabenor Madinah, menyembahyangkannya.'),
 'Her name was Hind, daughter of Abū Umayya — whose own name was Suhayl, called Zād al-Rakb — of Makhzūm.':
  ('Namanya Hind, putri Abū Umayya — yang namanya sendiri Suhayl, dijuluki Zād al-Rakb — dari Makhzūm.',
   'Namanya Hind, puteri Abū Umayya — yang namanya sendiri Suhayl, digelar Zād al-Rakb — daripada Makhzūm.'),
 'She had married Abū Salama and gone with him to Abyssinia in both migrations, bearing him children there.':
  ('Ia menikah dengan Abū Salama dan pergi bersamanya ke Habasyah pada kedua hijrah, melahirkan anak-anak baginya di sana.',
   'Dia berkahwin dengan Abū Salama dan pergi bersamanya ke Habsyah pada kedua-dua hijrah, melahirkan anak-anak baginya di sana.'),
 'Abū Salama, dying, told her to marry after him, and prayed: God, grant Umm Salama after me a man better than I am, who will not grieve her or wrong her.':
  ('Abū Salama, menjelang wafat, menyuruhnya menikah sesudahnya, dan berdoa: ya Allah, karuniakan kepada Umm Salama sesudahku seorang lelaki yang lebih baik dariku, yang tidak menyedihkannya dan tidak menyakitinya.',
   'Abū Salama, menjelang wafat, menyuruhnya berkahwin selepasnya, dan berdoa: ya Allah, kurniakan kepada Umm Salama selepasku seorang lelaki yang lebih baik daripadaku, yang tidak menyedihkannya dan tidak menyakitinya.'),
 'She had learnt the words for a calamity from the Prophet himself — God reward me in my affliction and give me better after it —':
  ('Ia telah belajar kalimat musibah dari Nabi ﷺ sendiri — ya Allah, berilah aku pahala dalam musibahku dan gantikanlah dengan yang lebih baik —',
   'Dia telah mempelajari kalimah musibah daripada Nabi ﷺ sendiri — ya Allah, berilah aku pahala dalam musibahku dan gantikanlah dengan yang lebih baik —'),
 'and balked at saying it: who is better than Abū Salama? She said it, and afterwards said God had hurried the answer.':
  ('dan enggan mengucapkannya: siapa yang lebih baik dari Abū Salama? Ia mengucapkannya, dan sesudahnya berkata Allah menyegerakan jawabannya.',
   'dan keberatan mengucapkannya: siapa yang lebih baik daripada Abū Salama? Dia mengucapkannya, dan selepas itu berkata Allah menyegerakan jawapannya.'),
 'When the Prophet asked for her she raised three objections: I am old, I have children, and I am a jealous woman.':
  ('Ketika Nabi ﷺ meminangnya ia mengajukan tiga keberatan: aku sudah tua, aku punya anak-anak, dan aku perempuan pencemburu.',
   'Ketika Nabi ﷺ meminangnya dia mengemukakan tiga keberatan: aku sudah tua, aku ada anak-anak, dan aku wanita pencemburu.'),
 "He answered each: the jealousy we will ask God to take from you, as for age I am older than you, and the children are God's affair and His Messenger's.":
  ('Beliau menjawab satu per satu: cemburu itu akan kita mohonkan kepada Allah agar dihilangkan darimu, adapun usia, aku lebih tua darimu, dan anak-anak itu urusan Allah dan Rasul-Nya.',
   'Baginda menjawab satu persatu: cemburu itu akan kita pohonkan kepada Allah agar dihilangkan daripadamu, adapun usia, aku lebih tua daripadamu, dan anak-anak itu urusan Allah dan Rasul-Nya.'),
 'Abū Jaʿfar: he came to her when Abū Salama died and spoke to her so long, leaning on his hand, that the matting marked it.':
  ('Abū Jaʿfar: beliau mendatanginya ketika Abū Salama wafat dan berbicara begitu lama, bertumpu pada tangannya, sampai tikar membekas padanya.',
   'Abū Jaʿfar: baginda mendatanginya ketika Abū Salama wafat dan berbicara begitu lama, bertekan pada tangannya, sehingga tikar meninggalkan kesan padanya.'),
 'Of Banū Hilāl b. ʿĀmir b. Ṣaʿṣaʿa, and called Mother of the Poor already in the Jāhiliyya.':
  ('Dari Banū Hilāl b. ʿĀmir b. Ṣaʿṣaʿa, dan sudah dipanggil Umm al-Masākīn sejak Jahiliah.',
   'Daripada Banū Hilāl b. ʿĀmir b. Ṣaʿṣaʿa, dan sudah dipanggil Umm al-Masākīn sejak Jahiliah.'),
 'al-Zuhrī: Zaynab bt. Khuzayma al-Hilāliyya was called Mother of the Poor, and had been married to al-Ṭufayl b. al-Ḥārith, who divorced her.':
  ('al-Zuhrī: Zaynab binti Khuzayma al-Hilāliyya dipanggil Umm al-Masākīn, dan pernah menjadi istri al-Ṭufayl b. al-Ḥārith, yang menceraikannya.',
   'al-Zuhrī: Zaynab binti Khuzayma al-Hilāliyya dipanggil Umm al-Masākīn, dan pernah menjadi isteri al-Ṭufayl b. al-Ḥārith, yang menceraikannya.'),
 "Ibn Saʿd's own informant continues: then ʿUbayda married her — the chapter given her is barely a page.":
  ('Perawi Ibn Saʿd meneruskan: lalu ʿUbayda menikahinya — bab yang diberikan kepadanya hanya sekitar satu halaman.',
   'Perawi Ibn Saʿd meneruskan: kemudian ʿUbayda mengahwininya — bab yang diberikan kepadanya hanya sekitar satu muka surat.'),
 "Her name was Ramla, daughter of Abū Sufyān; her mother Ṣafiyya bt. Abī al-ʿĀṣ was ʿUthmān's aunt.":
  ('Namanya Ramla, putri Abū Sufyān; ibunya Ṣafiyya binti Abī al-ʿĀṣ adalah bibi ʿUthmān.',
   'Namanya Ramla, puteri Abū Sufyān; ibunya Ṣafiyya binti Abī al-ʿĀṣ ialah emak saudara ʿUthmān.'),
 'She had married ʿUbayd Allāh b. Jaḥsh and bore him Ḥabība, from whom she took her kunya.':
  ('Ia menikah dengan ʿUbayd Allāh b. Jaḥsh dan melahirkan Ḥabība baginya, dari nama itulah kunyahnya diambil.',
   'Dia berkahwin dengan ʿUbayd Allāh b. Jaḥsh dan melahirkan Ḥabība baginya, daripada nama itulah kunyahnya diambil.'),
 'He took her to Abyssinia in the second migration, became a Christian and left Islam, and died there — she held to her religion and her migration.':
  ('Ia membawanya ke Habasyah pada hijrah kedua, lalu menjadi Nasrani dan murtad dari Islam, dan wafat di sana — sementara ia tetap teguh pada agamanya dan hijrahnya.',
   'Dia membawanya ke Habsyah pada hijrah kedua, lalu menjadi Nasrani dan murtad daripada Islam, dan wafat di sana — sementara dia tetap teguh pada agamanya dan hijrahnya.'),
 'The Prophet sent ʿAmr b. Umayya al-Ḍamrī to the Negus to ask for her; the Negus married her to him and paid her dower himself, four hundred dīnārs.':
  ('Nabi ﷺ mengutus ʿAmr b. Umayya al-Ḍamrī kepada Najashi untuk meminangnya; Najashi menikahkannya dengan beliau dan membayarkan maharnya sendiri, empat ratus dinar.',
   'Nabi ﷺ mengutus ʿAmr b. Umayya al-Ḍamrī kepada Najasyi untuk meminangnya; Najasyi mengahwinkannya dengan baginda dan membayar maharnya sendiri, empat ratus dinar.'),
 'When her father Abū Sufyān died she called for perfume and rubbed it on her arms and cheeks, saying she had no need of it — but she had heard the Prophet forbid a woman to mourn beyond three days.':
  ('Ketika ayahnya Abū Sufyān wafat ia meminta wewangian lalu melumurkannya pada kedua lengan dan pipinya, katanya ia tidak membutuhkannya — tetapi ia mendengar Nabi ﷺ melarang perempuan berkabung lebih dari tiga hari.',
   'Ketika bapanya Abū Sufyān wafat dia meminta minyak wangi lalu menyapunya pada kedua-dua lengan dan pipinya, katanya dia tidak memerlukannya — tetapi dia mendengar Nabi ﷺ melarang wanita berkabung lebih daripada tiga hari.'),
 "Her mother was Umayma bt. ʿAbd al-Muṭṭalib, so she was the Prophet's cousin; she migrated with him to Medina, and was a beautiful woman.":
  ('Ibunya Umayma binti ʿAbd al-Muṭṭalib, jadi ia sepupu Nabi ﷺ; ia berhijrah bersama beliau ke Madinah, dan seorang perempuan yang cantik.',
   'Ibunya Umayma binti ʿAbd al-Muṭṭalib, jadi dia sepupu Nabi ﷺ; dia berhijrah bersama baginda ke Madinah, dan seorang wanita yang cantik.'),
 'The Prophet first asked for her on behalf of Zayd b. Ḥāritha; she refused — I am the unmarried woman of Quraysh, I do not accept him for myself.':
  ('Nabi ﷺ mula-mula meminangnya untuk Zayd b. Ḥāritha; ia menolak — aku perempuan Quraisy yang belum bersuami, aku tidak meridainya untuk diriku.',
   'Nabi ﷺ mula-mula meminangnya untuk Zayd b. Ḥāritha; dia menolak — aku wanita Quraisy yang belum bersuami, aku tidak meredainya untuk diriku.'),
 'He said: I accept him for you. And she married Zayd.':
  ('Beliau berkata: aku meridainya untukmu. Dan ia pun menikah dengan Zayd.',
   'Baginda berkata: aku meredainya untukmu. Dan dia pun berkahwin dengan Zayd.'),
 'The verse of the curtain came down over his own wedding to her, when the guests would not leave.':
  ('Ayat hijab turun pada malam pernikahan beliau dengannya, ketika para tamu tak kunjung pergi.',
   'Ayat hijab turun pada malam perkahwinan baginda dengannya, ketika para tetamu tidak juga beredar.'),
 'The wives asked which of them would follow him soonest. He said: the longest of you in the arm.':
  ('Para istri bertanya siapa di antara mereka yang paling cepat menyusul beliau. Beliau berkata: yang paling panjang tangannya.',
   'Para isteri bertanya siapa antara mereka yang paling cepat menyusul baginda. Baginda berkata: yang paling panjang tangannya.'),
 'ʿĀʾisha: we used to stretch our arms against the wall to measure — until Zaynab died, and she was a short woman, and we understood he had meant giving.':
  ('ʿĀʾisha: kami biasa merentangkan tangan ke dinding untuk mengukur — sampai Zaynab wafat, padahal ia perempuan yang pendek, dan barulah kami paham yang beliau maksud adalah sedekah.',
   'ʿĀʾisha: kami biasa menghulurkan tangan ke dinding untuk mengukur — sehingga Zaynab wafat, padahal dia wanita yang rendah, dan barulah kami faham yang baginda maksudkan ialah sedekah.'),
 'She worked with her hands, and when she died they knew hers had been the longest arm in charity.':
  ('Ia bekerja dengan tangannya, dan ketika ia wafat mereka tahu tangannyalah yang paling panjang dalam sedekah.',
   'Dia bekerja dengan tangannya, dan ketika dia wafat mereka tahu tangannyalah yang paling panjang dalam sedekah.'),
 'Daughter of al-Ḥārith b. Abī Ḍirār, of Banū al-Muṣṭaliq of Khuzāʿa.':
  ('Putri al-Ḥārith b. Abī Ḍirār, dari Banū al-Muṣṭaliq dari Khuzāʿa.',
   'Puteri al-Ḥārith b. Abī Ḍirār, daripada Banū al-Muṣṭaliq daripada Khuzāʿa.'),
 'She had been married to Musāfiʿ b. Ṣafwān, who was killed on the day of al-Muraysīʿ.':
  ('Ia pernah menjadi istri Musāfiʿ b. Ṣafwān, yang terbunuh pada hari al-Muraysīʿ.',
   'Dia pernah menjadi isteri Musāfiʿ b. Ṣafwān, yang terbunuh pada hari al-Muraysīʿ.'),
 "When the Prophet married her the news went out and the people said: the Messenger of God's kin by marriage, held as slaves —":
  ('Ketika Nabi ﷺ menikahinya berita itu tersiar dan orang-orang berkata: besan Rasulullah ﷺ kok dijadikan budak —',
   'Ketika Nabi ﷺ mengahwininya berita itu tersebar dan orang ramai berkata: keluarga mertua Rasulullah ﷺ dijadikan hamba —'),
 'and they freed the captives of Banū al-Muṣṭaliq in their hands, a hundred households.':
  ('dan mereka memerdekakan tawanan Banū al-Muṣṭaliq yang ada di tangan mereka, seratus keluarga.',
   'dan mereka memerdekakan tawanan Banū al-Muṣṭaliq yang ada di tangan mereka, seratus keluarga.'),
 'Ibn Saʿd: I know of no woman who was a greater blessing to her people than she was.':
  ('Ibn Saʿd: aku tak mengetahui perempuan yang lebih besar berkahnya bagi kaumnya daripada dia.',
   'Ibn Saʿd: aku tidak mengetahui wanita yang lebih besar keberkatannya bagi kaumnya daripada dia.'),
 'She died in Rabīʿ al-Awwal of the year fifty-six, and Marwān b. al-Ḥakam, governor of Medina, prayed over her.':
  ('Ia wafat pada Rabīʿ al-Awwal tahun lima puluh enam, dan Marwān b. al-Ḥakam, gubernur Madinah, menyalatinya.',
   'Dia wafat pada Rabīʿ al-Awwal tahun lima puluh enam, dan Marwān b. al-Ḥakam, gabenor Madinah, menyembahyangkannya.'),
 'Sister, by both parents, of Umm al-Faḍl bt. al-Ḥārith, and it was al-ʿAbbās who had charge of her affair.':
  ('Saudari sekandung Umm al-Faḍl binti al-Ḥārith, dan al-ʿAbbās-lah yang mengurus perkaranya.',
   'Saudara sekandung Umm al-Faḍl binti al-Ḥārith, dan al-ʿAbbās-lah yang menguruskan perkaranya.'),
 'He married her at Sarif, ten miles from Mecca, in the year seven, on the ʿumra of the settlement — the last woman he married.':
  ('Beliau menikahinya di Sarif, sepuluh mil dari Mekah, pada tahun ketujuh, dalam umrah qadha — perempuan terakhir yang beliau nikahi.',
   'Baginda mengahwininya di Sarif, sepuluh batu dari Mekah, pada tahun ketujuh, dalam umrah qadha — wanita terakhir yang baginda kahwini.'),
 "She put her affair in his hands, and he went to al-ʿAbbās's house and asked him for her.":
  ('Ia menyerahkan urusannya kepada beliau, lalu beliau datang ke rumah al-ʿAbbās dan meminangnya kepadanya.',
   'Dia menyerahkan urusannya kepada baginda, lalu baginda datang ke rumah al-ʿAbbās dan meminangnya daripadanya.'),
 'Whether he was in iḥrām when he married her is a question the chapter puts directly to a witness.':
  ('Apakah beliau sedang berihram ketika menikahinya adalah pertanyaan yang bab ini ajukan langsung kepada seorang saksi.',
   'Sama ada baginda sedang berihram ketika mengahwininya ialah soalan yang bab ini ajukan terus kepada seorang saksi.'),
 'Maymūn b. Mihrān asked Ṣafiyya bt. Shayba, an old woman by then: did he marry Maymūna while in iḥrām? She said: no, by God — he married her and they were both out of it.':
  ('Maymūn b. Mihrān bertanya kepada Ṣafiyya binti Shayba, yang saat itu telah tua: apakah beliau menikahi Maymūna dalam keadaan berihram? Ia menjawab: tidak, demi Allah — beliau menikahinya dan keduanya dalam keadaan halal.',
   'Maymūn b. Mihrān bertanya kepada Ṣafiyya binti Shayba, yang ketika itu telah tua: adakah baginda mengahwini Maymūna dalam keadaan berihram? Dia menjawab: tidak, demi Allah — baginda mengahwininya dan kedua-duanya dalam keadaan halal.'),
 'She died at Sarif, where she had been married, and Ibn ʿAbbās told them not to shake her bier.':
  ('Ia wafat di Sarif, tempat ia dinikahi, dan Ibn ʿAbbās berpesan agar kerandanya jangan diguncang.',
   'Dia wafat di Sarif, tempat dia dikahwini, dan Ibn ʿAbbās berpesan agar kerandanya jangan digoncang.'),
 'He added a count of his own: the Prophet had nine wives, and allotted turns to eight of them, and to one he did not.':
  ('Ia menambahkan hitungannya sendiri: Nabi ﷺ punya sembilan istri, dan beliau membagi giliran untuk delapan, dan untuk satu tidak.',
   'Dia menambah kiraannya sendiri: Nabi ﷺ mempunyai sembilan isteri, dan baginda membahagi giliran untuk lapan, dan untuk seorang tidak.'),
 'Called Abū Muḥammad; his mother was al-Ṣaʿba bt. ʿAbd Allāh al-Ḥaḍramī.':
  ('Berkunyah Abū Muḥammad; ibunya al-Ṣaʿba binti ʿAbd Allāh al-Ḥaḍramī.',
   'Berkunyah Abū Muḥammad; ibunya al-Ṣaʿba binti ʿAbd Allāh al-Ḥaḍramī.'),
 "Her mother's father, Wahb b. ʿAbd, had held the provisioning of the pilgrims for all Quraysh.":
  ('Kakek dari pihak ibunya, Wahb b. ʿAbd, memegang rifādah jamaah haji bagi seluruh Quraisy.',
   'Datuk sebelah ibunya, Wahb b. ʿAbd, memegang rifādah jemaah haji bagi seluruh Quraisy.'),
 'He came to Islam through what a monk had told him: Abū Bakr took him in to the Prophet, who was gladdened by the report.':
  ('Ia sampai kepada Islam melalui apa yang dikatakan seorang rahib kepadanya: Abū Bakr membawanya menghadap Nabi ﷺ, yang bergembira mendengar kabar itu.',
   'Dia sampai kepada Islam melalui apa yang dikatakan seorang rahib kepadanya: Abū Bakr membawanya mengadap Nabi ﷺ, yang bergembira mendengar berita itu.'),
 'Nawfal b. Khuwaylid bound him and Abū Bakr in a single rope, and Banū Taym did not stop him.':
  ('Nawfal b. Khuwaylid mengikatnya bersama Abū Bakr dalam satu tali, dan Banū Taym tidak mencegahnya.',
   'Nawfal b. Khuwaylid mengikatnya bersama Abū Bakr dalam satu tali, dan Banū Taym tidak menghalangnya.'),
 "Abū Bakr's account of Uḥud: I was among the first to return, and the Messenger of God said to us — see to your companion, meaning Ṭalḥa.":
  ('Penuturan Abū Bakr tentang Uḥud: aku termasuk yang pertama kembali, dan Rasulullah ﷺ berkata kepada kami — uruslah sahabat kalian, maksudnya Ṭalḥa.',
   'Cerita Abū Bakr tentang Uḥud: aku termasuk yang pertama kembali, dan Rasulullah ﷺ berkata kepada kami — uruslah sahabat kamu, maksudnya Ṭalḥa.'),
 'ʿUmar once saw him in iḥrām wearing two garments dyed with red ochre, and asked him what he meant by them.':
  ('ʿUmar pernah melihatnya berihram mengenakan dua kain yang dicelup tanah merah, lalu bertanya apa maksudnya.',
   'ʿUmar pernah melihatnya berihram memakai dua kain yang dicelup tanah merah, lalu bertanya apa maksudnya.'),
 'His son Muḥammad, called al-Sajjād, was killed with him on the day of the Camel.':
  ('Putranya Muḥammad, yang dijuluki al-Sajjād, terbunuh bersamanya pada hari Jamal.',
   'Puteranya Muḥammad, yang digelar al-Sajjād, terbunuh bersamanya pada hari Jamal.'),
 "His mother was Ṣafiyya bt. ʿAbd al-Muṭṭalib, so he was the Prophet's cousin.":
  ('Ibunya Ṣafiyya binti ʿAbd al-Muṭṭalib, jadi ia sepupu Nabi ﷺ.',
   'Ibunya Ṣafiyya binti ʿAbd al-Muṭṭalib, jadi dia sepupu Nabi ﷺ.'),
 'He was called Abū ʿAbd Allāh.':
  ('Ia berkunyah Abū ʿAbd Allāh.',
   'Dia berkunyah Abū ʿAbd Allāh.'),
 'He had eleven sons and nine daughters.':
  ('Ia punya sebelas putra dan sembilan putri.',
   'Dia mempunyai sebelas putera dan sembilan puteri.'),
 "When he broke a boy's hand as a child and they brought the complaint to his mother, she answered in verse — asking how they had found Zubayr.":
  ('Ketika ia mematahkan tangan seorang anak semasa kecil dan pengaduan dibawa kepada ibunya, ia menjawab dengan syair — menanyakan bagaimana mereka mendapati Zubayr.',
   'Ketika dia mematahkan tangan seorang budak semasa kecil dan aduan dibawa kepada ibunya, dia menjawab dengan syair — bertanya bagaimana mereka mendapati Zubayr.'),
 'Hishām b. ʿUrwa: he entered Islam at sixteen, and never stayed behind from a raid the Prophet made.':
  ('Hishām b. ʿUrwa: ia masuk Islam pada usia enam belas, dan tak pernah absen dari satu pun peperangan Nabi ﷺ.',
   'Hishām b. ʿUrwa: dia memeluk Islam pada usia enam belas, dan tidak pernah tertinggal daripada satu pun peperangan Nabi ﷺ.'),
 'At Badr he wore a yellow turban wound about his head — and the angels that day, it is said, wore yellow turbans.':
  ('Di Badr ia mengenakan serban kuning yang dililitkan di kepalanya — dan para malaikat hari itu, konon, bersorban kuning.',
   'Di Badr dia memakai serban kuning yang dililit di kepalanya — dan para malaikat hari itu, katanya, berserban kuning.'),
 'He was at Badr, Uḥud and every engagement, held his ground at Uḥud and pledged himself to death, and carried one of the three Muhājir banners at the Conquest.':
  ('Ia ikut Badr, Uḥud dan semua peperangan, bertahan di Uḥud dan berbaiat sampai mati, serta membawa satu dari tiga panji Muhajirin pada Penaklukan.',
   'Dia menyertai Badr, Uḥud dan semua peperangan, bertahan di Uḥud dan berbaiah sampai mati, serta membawa satu daripada tiga panji Muhajirin pada Pembukaan Mekah.'),
 'In the Jāhiliyya his name was ʿAbd ʿAmr; the Prophet named him ʿAbd al-Raḥmān when he entered Islam. He was called Abū Muḥammad.':
  ('Pada masa Jahiliah namanya ʿAbd ʿAmr; Nabi ﷺ menamainya ʿAbd al-Raḥmān ketika ia masuk Islam. Ia berkunyah Abū Muḥammad.',
   'Pada zaman Jahiliah namanya ʿAbd ʿAmr; Nabi ﷺ menamakannya ʿAbd al-Raḥmān ketika dia memeluk Islam. Dia berkunyah Abū Muḥammad.'),
 "His mother was al-Shifāʾ bt. ʿAwf, of Zuhra — his father's clan as well.":
  ('Ibunya al-Shifāʾ binti ʿAwf, dari Zuhra — kabilah ayahnya juga.',
   'Ibunya al-Shifāʾ binti ʿAwf, daripada Zuhra — kabilah bapanya juga.'),
 'He was born ten years after the Elephant.':
  ('Ia lahir sepuluh tahun setelah Tahun Gajah.',
   'Dia lahir sepuluh tahun selepas Tahun Gajah.'),
 'He entered Islam before the Prophet went into the house of al-Arqam, and before he began calling people there.':
  ('Ia masuk Islam sebelum Nabi ﷺ memasuki rumah al-Arqam, dan sebelum beliau mulai berdakwah di sana.',
   'Dia memeluk Islam sebelum Nabi ﷺ memasuki rumah al-Arqam, dan sebelum baginda mula berdakwah di sana.'),
 'He said the Prophet had marked out land for him in Syria called al-Salīl, and died before writing him any document for it.':
  ('Ia berkata Nabi ﷺ telah memberinya sebidang tanah di Syam bernama al-Salīl, dan wafat sebelum menuliskan surat apa pun untuknya.',
   'Dia berkata Nabi ﷺ telah memberinya sebidang tanah di Syam bernama al-Salīl, dan wafat sebelum menulis sebarang surat untuknya.'),
 'His eldest son, Sālim, died before Islam.':
  ('Putra sulungnya, Sālim, wafat sebelum Islam.',
   'Putera sulungnya, Sālim, wafat sebelum Islam.'),
 'Called Abū al-Aʿwar; his line runs back through Nufayl to ʿAdī b. Kaʿb — the same stock as ʿUmar.':
  ('Berkunyah Abū al-Aʿwar; nasabnya naik melalui Nufayl sampai ʿAdī b. Kaʿb — satu rumpun dengan ʿUmar.',
   'Berkunyah Abū al-Aʿwar; nasabnya naik melalui Nufayl hingga ʿAdī b. Kaʿb — serumpun dengan ʿUmar.'),
 'His mother was Fāṭima bt. Baʿja, of Khuzāʿa.':
  ('Ibunya Fāṭima binti Baʿja, dari Khuzāʿa.',
   'Ibunya Fāṭima binti Baʿja, daripada Khuzāʿa.'),
 'His father Zayd b. ʿAmr went looking for a religion — travelled to Syria and asked the Jews and the Christians, and was not satisfied by what they had.':
  ('Ayahnya Zayd b. ʿAmr pergi mencari agama — berjalan ke Syam dan bertanya kepada orang Yahudi dan Nasrani, dan tidak puas dengan apa yang ada pada mereka.',
   'Bapanya Zayd b. ʿAmr pergi mencari agama — berjalan ke Syam dan bertanya kepada orang Yahudi dan Nasrani, dan tidak berpuas hati dengan apa yang ada pada mereka.'),
 'A Christian told him: what you are after is the religion of Ibrāhīm. And Zayd asked: what is the religion of Ibrāhīm?':
  ('Seorang Nasrani berkata kepadanya: yang engkau cari adalah agama Ibrāhīm. Dan Zayd bertanya: apa itu agama Ibrāhīm?',
   'Seorang Nasrani berkata kepadanya: yang engkau cari ialah agama Ibrāhīm. Dan Zayd bertanya: apakah agama Ibrāhīm?'),
 'Zayd died before the message came, and was buried at the foot of Ḥirāʾ.':
  ('Zayd wafat sebelum risalah datang, dan dimakamkan di kaki Ḥirāʾ.',
   'Zayd wafat sebelum risalah datang, dan dikebumikan di kaki Ḥirāʾ.'),
 'His son entered Islam before the Prophet went into the house of al-Arqam, and before he began calling people there.':
  ('Putranya masuk Islam sebelum Nabi ﷺ memasuki rumah al-Arqam, dan sebelum beliau mulai berdakwah di sana.',
   'Puteranya memeluk Islam sebelum Nabi ﷺ memasuki rumah al-Arqam, dan sebelum baginda mula berdakwah di sana.'),
 'His name was ʿĀmir b. ʿAbd Allāh b. al-Jarrāḥ, of Fihr.':
  ('Namanya ʿĀmir b. ʿAbd Allāh b. al-Jarrāḥ, dari Fihr.',
   'Namanya ʿĀmir b. ʿAbd Allāh b. al-Jarrāḥ, daripada Fihr.'),
 'His two sons died and left nothing, so he has no line.':
  ('Kedua putranya wafat tanpa meninggalkan keturunan, jadi ia tidak berketurunan.',
   'Kedua-dua puteranya wafat tanpa meninggalkan keturunan, jadi dia tidak berketurunan.'),
 'He entered Islam with ʿUthmān b. Maẓʿūn and ʿAbd al-Raḥmān b. ʿAwf, before the Prophet went into the house of al-Arqam.':
  ('Ia masuk Islam bersama ʿUthmān b. Maẓʿūn dan ʿAbd al-Raḥmān b. ʿAwf, sebelum Nabi ﷺ memasuki rumah al-Arqam.',
   'Dia memeluk Islam bersama ʿUthmān b. Maẓʿūn dan ʿAbd al-Raḥmān b. ʿAwf, sebelum Nabi ﷺ memasuki rumah al-Arqam.'),
 'He was at Badr and Uḥud, and held his ground at Uḥud when the people were routed and turned.':
  ('Ia ikut Badr dan Uḥud, dan bertahan di Uḥud ketika orang-orang kalah dan berpaling.',
   'Dia menyertai Badr dan Uḥud, dan bertahan di Uḥud ketika orang ramai tewas dan berpaling.'),
 'He was at the Trench and every engagement, one of the foremost of the Companions, and was sent to Dhū al-Qaṣṣa with forty men.':
  ('Ia ikut Khandaq dan semua peperangan, termasuk sahabat terkemuka, dan diutus ke Dhū al-Qaṣṣa bersama empat puluh orang.',
   'Dia menyertai Khandaq dan semua peperangan, termasuk sahabat terkemuka, dan diutus ke Dhū al-Qaṣṣa bersama empat puluh orang.'),
 'When a man said under his siege that things would not be so hard had it been Khālid b. al-Walīd, Muʿādh answered him sharply.':
  ('Ketika seseorang berkata dalam pengepungannya bahwa keadaan tak akan sesulit ini andai Khālid b. al-Walīd yang memimpin, Muʿādh menjawabnya dengan keras.',
   'Ketika seseorang berkata dalam kepungannya bahawa keadaan tidak akan sesukar ini andai Khālid b. al-Walīd yang memimpin, Muʿādh menjawabnya dengan keras.'),
 'ʿIrbāḍ b. Sāriya went in to him as he was dying, and heard him say: God forgive ʿUmar b. al-Khaṭṭāb for turning back from Sargh.':
  ('ʿIrbāḍ b. Sāriya menjenguknya menjelang wafat, dan mendengarnya berkata: semoga Allah mengampuni ʿUmar b. al-Khaṭṭāb atas kepulangannya dari Sargh.',
   'ʿIrbāḍ b. Sāriya menziarahinya menjelang wafat, dan mendengarnya berkata: semoga Allah mengampuni ʿUmar b. al-Khaṭṭāb atas kepulangannya dari Sargh.'),
 'Of ʿAbd al-Ashhal of al-Aws, and called Abū ʿAmr.':
  ('Dari ʿAbd al-Ashhal dari al-Aws, berkunyah Abū ʿAmr.',
   'Daripada ʿAbd al-Ashhal daripada al-Aws, berkunyah Abū ʿAmr.'),
 'His mother Kabsha bt. Rāfiʿ was of al-Khazraj, and among the women who gave the pledge.':
  ('Ibunya Kabsha binti Rāfiʿ dari al-Khazraj, dan termasuk perempuan yang berbaiat.',
   'Ibunya Kabsha binti Rāfiʿ daripada al-Khazraj, dan termasuk wanita yang berbaiah.'),
 "He married his brother Aws's widow, Hind bt. Simāk — the aunt of Usayd b. Ḥuḍayr.":
  ('Ia menikahi janda saudaranya Aws, Hind binti Simāk — bibi Usayd b. Ḥuḍayr.',
   'Dia mengahwini balu saudaranya Aws, Hind binti Simāk — emak saudara Usayd b. Ḥuḍayr.'),
 'Ibn Isḥāq, alone, pairs him in brotherhood with Abū ʿUbayda; Ibn Saʿd leaves it open.':
  ('Hanya Ibn Isḥāq yang mempersaudarakannya dengan Abū ʿUbayda; Ibn Saʿd membiarkannya terbuka.',
   'Hanya Ibn Isḥāq yang mempersaudarakannya dengan Abū ʿUbayda; Ibn Saʿd membiarkannya terbuka.'),
 'The banner of al-Aws at Badr was his; he was at Uḥud and held his ground when the people turned, and at the Trench.':
  ('Panji al-Aws di Badr ada padanya; ia ikut Uḥud dan bertahan ketika orang-orang berpaling, juga Khandaq.',
   'Panji al-Aws di Badr ada padanya; dia menyertai Uḥud dan bertahan ketika orang ramai berpaling, juga Khandaq.'),
 'The Prophet slept, and an angel — or Jibrīl — came to him as he woke and asked: which man of your community died tonight, whose death the people of heaven rejoiced at?':
  ('Nabi ﷺ tidur, lalu seorang malaikat — atau Jibrīl — datang saat beliau bangun dan bertanya: siapa orang dari umatmu yang wafat malam ini, yang kematiannya disambut gembira penduduk langit?',
   'Nabi ﷺ tidur, lalu seorang malaikat — atau Jibrīl — datang ketika baginda bangun dan bertanya: siapa orang daripada umatmu yang wafat malam ini, yang kematiannya disambut gembira penduduk langit?'),
 'His mother wept over him in verse, and the Prophet said: every wailing woman lies but Umm Saʿd.':
  ('Ibunya menangisinya dengan syair, dan Nabi ﷺ berkata: setiap perempuan yang meratap itu berdusta kecuali Umm Saʿd.',
   'Ibunya menangisinya dengan syair, dan Nabi ﷺ berkata: setiap wanita yang meratap itu berdusta kecuali Umm Saʿd.'),
 'Those carrying him said they had never carried a body lighter; he answered that so many angels had come down for it.':
  ('Mereka yang mengusungnya berkata belum pernah mengusung jenazah seringan itu; beliau menjawab bahwa sekian banyak malaikat telah turun untuknya.',
   'Mereka yang mengusungnya berkata belum pernah mengusung jenazah seringan itu; baginda menjawab bahawa sekian banyak malaikat telah turun untuknya.'),
 'Of Banū Salima of al-Khazraj; his mother Hind bt. Sahl was of Juhayna.':
  ('Dari Banū Salima dari al-Khazraj; ibunya Hind binti Sahl dari Juhayna.',
   'Daripada Banū Salima daripada al-Khazraj; ibunya Hind binti Sahl daripada Juhayna.'),
 'Called Abū ʿAbd al-Raḥmān; he was at al-ʿAqaba with the seventy of the Anṣār,':
  ('Berkunyah Abū ʿAbd al-Raḥmān; ia hadir di al-ʿAqaba bersama tujuh puluh orang Anṣār,',
   'Berkunyah Abū ʿAbd al-Raḥmān; dia hadir di al-ʿAqaba bersama tujuh puluh orang Anṣār,'),
 'and when he entered Islam he went about breaking the idols of Banū Salima with Thaʿlaba b. ʿAnama and ʿAbd Allāh b. Unays.':
  ('dan ketika masuk Islam ia menghancurkan berhala-berhala Banū Salima bersama Thaʿlaba b. ʿAnama dan ʿAbd Allāh b. Unays.',
   'dan ketika memeluk Islam dia memusnahkan berhala-berhala Banū Salima bersama Thaʿlaba b. ʿAnama dan ʿAbd Allāh b. Unays.'),
 'Ibn Saʿd: the pairing with Ibn Masʿūd is not disputed among us — Ibn Isḥāq alone gives another.':
  ('Ibn Saʿd: persaudaraannya dengan Ibn Masʿūd tidak diperselisihkan di kalangan kami — hanya Ibn Isḥāq yang menyebut yang lain.',
   'Ibn Saʿd: persaudaraannya dengan Ibn Masʿūd tidak diperselisihkan dalam kalangan kami — hanya Ibn Isḥāq yang menyebut yang lain.'),
 'He was at Badr at twenty, or twenty-one, and at Uḥud, the Trench and every engagement.':
  ('Ia ikut Badr pada usia dua puluh, atau dua puluh satu, dan ikut Uḥud, Khandaq dan semua peperangan.',
   'Dia menyertai Badr pada usia dua puluh, atau dua puluh satu, dan menyertai Uḥud, Khandaq dan semua peperangan.'),
 'When the Prophet died, Muʿādh was his governor over al-Janad.':
  ('Ketika Nabi ﷺ wafat, Muʿādh menjabat sebagai gubernur beliau atas al-Janad.',
   'Ketika Nabi ﷺ wafat, Muʿādh menjadi gabenor baginda ke atas al-Janad.'),
 'Abū Idrīs al-Khawlānī: I entered the mosque of Damascus and there was a young man with shining teeth, and people around him who referred every disagreement to him and left it at his opinion.':
  ('Abū Idrīs al-Khawlānī: aku masuk masjid Damaskus dan ternyata ada seorang pemuda bergigi putih berkilau, dengan orang-orang di sekelilingnya yang mengembalikan setiap perselisihan kepadanya dan berhenti pada pendapatnya.',
   'Abū Idrīs al-Khawlānī: aku masuk masjid Damsyik dan ternyata ada seorang pemuda bergigi putih berkilau, dengan orang ramai di sekelilingnya yang mengembalikan setiap perselisihan kepadanya dan berhenti pada pendapatnya.'),
 'Of Banū al-Najjār of al-Khazraj, and called Abū al-Mundhir.':
  ('Dari Banū al-Najjār dari al-Khazraj, berkunyah Abū al-Mundhir.',
   'Daripada Banū al-Najjār daripada al-Khazraj, berkunyah Abū al-Mundhir.'),
 'His mother was Ṣuhayla bt. al-Aswad, of Banū Mālik b. al-Najjār.':
  ('Ibunya Ṣuhayla binti al-Aswad, dari Banū Mālik b. al-Najjār.',
   'Ibunya Ṣuhayla binti al-Aswad, daripada Banū Mālik b. al-Najjār.'),
 'Ibn Saʿd gathers several reports of the day of his death, each carrying the same sentence:':
  ('Ibn Saʿd menghimpun beberapa riwayat tentang hari kematiannya, masing-masing membawa kalimat yang sama:',
   'Ibn Saʿd menghimpunkan beberapa riwayat tentang hari kematiannya, masing-masing membawa kalimah yang sama:'),
 'the lord of the Muslims died today, Ubayy b. Kaʿb.':
  ('hari ini telah wafat penghulu kaum Muslimin, Ubayy b. Kaʿb.',
   'hari ini telah wafat penghulu kaum Muslimin, Ubayy b. Kaʿb.'),
 'One who heard it remarked that he had never seen a man so covered over as this man had been.':
  ('Seorang yang mendengarnya berkata ia belum pernah melihat orang yang begitu ditutupi Allah seperti orang ini.',
   'Seorang yang mendengarnya berkata dia belum pernah melihat orang yang begitu ditutupi Allah seperti orang ini.'),
 'Ibn Saʿd weighs the reports himself: these say he died under ʿUmar, and his family put it at twenty-two — but the year thirty, under ʿUthmān, is the soundest of the accounts to us.':
  ('Ibn Saʿd menimbang riwayat-riwayat itu sendiri: yang ini menunjukkan ia wafat pada masa ʿUmar, dan keluarganya menyebut tahun dua puluh dua — tetapi tahun tiga puluh, pada masa ʿUthmān, adalah yang paling kuat menurut kami.',
   'Ibn Saʿd menimbang riwayat-riwayat itu sendiri: yang ini menunjukkan dia wafat pada zaman ʿUmar, dan keluarganya menyebut tahun dua puluh dua — tetapi tahun tiga puluh, pada zaman ʿUthmān, ialah yang paling kuat menurut kami.'),
 'Of ʿAbd al-Ashhal of al-Aws; called Abū Yaḥyā, and also Abū al-Ḥuḍayr.':
  ('Dari ʿAbd al-Ashhal dari al-Aws; berkunyah Abū Yaḥyā, dan juga Abū al-Ḥuḍayr.',
   'Daripada ʿAbd al-Ashhal daripada al-Aws; berkunyah Abū Yaḥyā, dan juga Abū al-Ḥuḍayr.'),
 "His mother's name comes down two ways: Umm Usayd bt. al-Nuʿmān on Muḥammad b. ʿUmar's authority,":
  ('Nama ibunya sampai kepada kita dua cara: Umm Usayd binti al-Nuʿmān menurut riwayat Muḥammad b. ʿUmar,',
   'Nama ibunya sampai kepada kita dua cara: Umm Usayd binti al-Nuʿmān menurut riwayat Muḥammad b. ʿUmar,'),
 "and Umm Usayd bt. Sakan on ʿAbd Allāh b. Muḥammad's.":
  ('dan Umm Usayd binti Sakan menurut riwayat ʿAbd Allāh b. Muḥammad.',
   'dan Umm Usayd binti Sakan menurut riwayat ʿAbd Allāh b. Muḥammad.'),
 'His father Ḥuḍayr of the Squadrons was a chief in the Jāhiliyya and led al-Aws at Buʿāth — the last battle between al-Aws and al-Khazraj — and was killed there.':
  ('Ayahnya Ḥuḍayr al-Katāʾib seorang pemuka pada masa Jahiliah dan memimpin al-Aws pada Buʿāth — pertempuran terakhir antara al-Aws dan al-Khazraj — dan terbunuh di sana.',
   'Bapanya Ḥuḍayr al-Katāʾib seorang pemuka pada zaman Jahiliah dan memimpin al-Aws pada Buʿāth — pertempuran terakhir antara al-Aws dan al-Khazraj — dan terbunuh di sana.'),
 'Ibn Saʿd dates that battle by the Prophet: it happened while he was at Mecca, already prophesying and calling to Islam, and he migrated six years after it.':
  ('Ibn Saʿd menanggali pertempuran itu dengan Nabi ﷺ: peristiwa itu terjadi ketika beliau di Mekah, sudah menjadi nabi dan menyeru kepada Islam, dan beliau berhijrah enam tahun sesudahnya.',
   'Ibn Saʿd menentukan tarikh pertempuran itu dengan Nabi ﷺ: peristiwa itu berlaku ketika baginda di Mekah, sudah menjadi nabi dan menyeru kepada Islam, dan baginda berhijrah enam tahun selepasnya.'),
 'He took seven wounds at Uḥud and held his ground when the people broke, and was at the Trench and every engagement.':
  ('Ia menderita tujuh luka di Uḥud dan bertahan ketika orang-orang berpencar, dan ikut Khandaq serta semua peperangan.',
   'Dia menderita tujuh luka di Uḥud dan bertahan ketika orang ramai berpecah, dan menyertai Khandaq serta semua peperangan.'),
 'He died in Shaʿbān of the year twenty, and ʿUmar himself carried his bier out of Banū ʿAbd al-Ashhal to al-Baqīʿ and prayed over him there.':
  ('Ia wafat pada Shaʿbān tahun dua puluh, dan ʿUmar sendiri memikul kerandanya dari Banū ʿAbd al-Ashhal sampai al-Baqīʿ dan menyalatinya di sana.',
   'Dia wafat pada Syaaban tahun dua puluh, dan ʿUmar sendiri memikul kerandanya dari Banū ʿAbd al-Ashhal hingga al-Baqīʿ dan menyembahyangkannya di sana.'),
 "Ibn ʿAbbās: Hāshim's name was ʿAmr, and he was the man of the Īlāf of Quraysh.":
  ('Ibn ʿAbbās: nama Hāshim adalah ʿAmr, dan dialah pemilik īlāf Quraisy.',
   'Ibn ʿAbbās: nama Hāshim ialah ʿAmr, dan dialah pemilik īlāf Quraisy.'),
 'He was the first to appoint Quraysh their two journeys — one in winter to the Yemen and to the Negus in Abyssinia, and one in summer to Syria.':
  ('Ia orang pertama yang menetapkan dua perjalanan Quraisy — satu pada musim dingin ke Yaman dan kepada Najashi di Habasyah, dan satu pada musim panas ke Syam.',
   'Dia orang pertama yang menetapkan dua perjalanan Quraisy — satu pada musim sejuk ke Yaman dan kepada Najasyi di Habsyah, dan satu pada musim panas ke Syam.'),
 'Ibn Saʿd names his children by their mothers, one of whom, Qayla, was nicknamed the Slaughter-Camel and was of Khuzāʿa.':
  ('Ibn Saʿd menyebut anak-anaknya menurut ibu masing-masing, salah satunya Qayla, yang dijuluki al-Jazūr dan berasal dari Khuzāʿa.',
   'Ibn Saʿd menyebut anak-anaknya menurut ibu masing-masing, salah seorangnya Qayla, yang digelar al-Jazūr dan berasal daripada Khuzāʿa.'),
 'His kunya is disputed: Abū Yazīd, or, some say, after his son Asad.':
  ('Kunyahnya diperselisihkan: Abū Yazīd, atau, menurut sebagian, dengan nama putranya Asad.',
   'Kunyahnya diperselisihkan: Abū Yazīd, atau, menurut sebahagian, dengan nama puteranya Asad.'),
 "When he died his children mourned him in a great deal of verse, and Ibn Saʿd notes that his daughter Khālida's elegy is weak poetry.":
  ('Ketika ia wafat anak-anaknya meratapinya dengan banyak syair, dan Ibn Saʿd mencatat bahwa ratapan putrinya Khālida adalah syair yang lemah.',
   'Ketika dia wafat anak-anaknya meratapinya dengan banyak syair, dan Ibn Saʿd mencatat bahawa ratapan puterinya Khālida ialah syair yang lemah.'),
 'The chapter opens on his uncle: al-Muṭṭalib, whom Quraysh called the Overflowing for his openhandedness, and who held the watering and provisioning after Hāshim.':
  ('Bab ini dibuka dengan pamannya: al-Muṭṭalib, yang Quraisy juluki al-Fayḍ karena kemurahannya, dan yang memegang siqāyah dan rifādah setelah Hāshim.',
   'Bab ini dibuka dengan bapa saudaranya: al-Muṭṭalib, yang digelar Quraisy al-Fayḍ kerana kemurahannya, dan yang memegang siqāyah dan rifādah selepas Hāshim.'),
 'Digging where he was told — by the dung, by the ants, by the sitting-place of Khuzāʿa — he found a gazelle, weapons and gold.':
  ('Menggali di tempat yang ditunjukkan kepadanya — di dekat kotoran, di dekat semut, di dekat majelis Khuzāʿa — ia menemukan patung kijang, senjata dan emas.',
   'Menggali di tempat yang ditunjukkan kepadanya — di dekat najis, di dekat semut, di dekat majlis Khuzāʿa — dia menemui patung kijang, senjata dan emas.'),
 'His people crowded him over the find, and it was then that he vowed that if ten sons were born to him he would sacrifice one.':
  ('Kaumnya mendesaknya karena temuan itu, dan saat itulah ia bernazar jika lahir baginya sepuluh putra ia akan menyembelih salah satunya.',
   'Kaumnya mendesaknya kerana penemuan itu, dan ketika itulah dia bernazar jika lahir baginya sepuluh putera dia akan menyembelih salah seorangnya.'),
 'When ten were born and he meant to slaughter ʿAbd Allāh, Banū Zuhra stopped him and told him to cast lots.':
  ('Ketika sepuluh telah lahir dan ia hendak menyembelih ʿAbd Allāh, Banū Zuhra menghalanginya dan menyuruhnya mengundi.',
   'Ketika sepuluh telah lahir dan dia hendak menyembelih ʿAbd Allāh, Banū Zuhra menghalangnya dan menyuruhnya mengundi.'),
 'Ibn ʿAbbās: the blood-price then was ten camels, and ʿAbd al-Muṭṭalib was the first to set it at a hundred — Quraysh and the Arabs followed him, and the Prophet left it as it stood.':
  ('Ibn ʿAbbās: diat saat itu sepuluh ekor unta, dan ʿAbd al-Muṭṭalib orang pertama yang menetapkannya seratus — Quraisy dan orang Arab mengikutinya, dan Nabi ﷺ membiarkannya sebagaimana adanya.',
   'Ibn ʿAbbās: diat ketika itu sepuluh ekor unta, dan ʿAbd al-Muṭṭalib orang pertama yang menetapkannya seratus — Quraisy dan orang Arab mengikutinya, dan Nabi ﷺ membiarkannya sebagaimana adanya.'),
 'He was the first of Quraysh at Mecca to dye with wasma, after a Ḥimyarī notable asked him whether he would like to be rid of the white and be young again.':
  ('Ia orang Quraisy pertama di Mekah yang menyemir dengan wasma, setelah seorang pembesar Ḥimyar bertanya apakah ia ingin menghilangkan uban itu dan kembali muda.',
   'Dia orang Quraisy pertama di Mekah yang menyemir dengan wasma, selepas seorang pembesar Ḥimyar bertanya adakah dia ingin menghilangkan uban itu dan kembali muda.'),
 "On a journey his water ran out and Thaqīf refused him; a spring broke open under his camel's chest, and when their own water failed he gave them to drink.":
  ('Dalam perjalanan air bekalnya habis dan Thaqīf menolak memberinya; sebuah mata air memancar di bawah dada untanya, dan ketika air mereka sendiri habis ia memberi mereka minum.',
   'Dalam perjalanan air bekalannya habis dan Thaqīf enggan memberinya; sebuah mata air memancar di bawah dada untanya, dan ketika air mereka sendiri habis dia memberi mereka minum.'),
 "He had twelve sons and six daughters; the eldest, al-Ḥārith, whose name gave him his kunya, died in his father's lifetime.":
  ('Ia punya dua belas putra dan enam putri; yang sulung, al-Ḥārith, yang namanya menjadi kunyahnya, wafat semasa ayahnya masih hidup.',
   'Dia mempunyai dua belas putera dan enam puteri; yang sulung, al-Ḥārith, yang namanya menjadi kunyahnya, wafat semasa bapanya masih hidup.'),
 "Ibn Saʿd's chapter here is Ḥawwāʾ's, and it is barely a page. Mujāhid on 'and He created from it its mate': Ḥawwāʾ was created from Ādam's shortest rib while he slept.":
  ("Bab Ibn Saʿd di sini adalah bab Ḥawwāʾ, dan panjangnya hampir satu halaman saja. Mujāhid tentang 'dan Dia menciptakan darinya pasangannya': Ḥawwāʾ diciptakan dari tulang rusuk Ādam yang terpendek ketika ia tidur.",
   "Bab Ibn Saʿd di sini ialah bab Ḥawwāʾ, dan panjangnya hampir satu muka surat sahaja. Mujāhid tentang 'dan Dia menciptakan daripadanya pasangannya': Ḥawwāʾ diciptakan daripada tulang rusuk Ādam yang terpendek ketika dia tidur."),
 'He woke and said athā — woman, in Nabataean.':
  ('Ia terbangun dan berkata athā — perempuan, dalam bahasa Nabath.',
   'Dia terjaga dan berkata athā — perempuan, dalam bahasa Nabti.'),
 'Ibn ʿAbbās: she was called Ḥawwāʾ because she is the mother of every living thing.':
  ('Ibn ʿAbbās: ia dinamai Ḥawwāʾ karena ia ibu setiap yang hidup.',
   'Ibn ʿAbbās: dia dinamakan Ḥawwāʾ kerana dia ibu setiap yang hidup.'),
 'Ibn ʿAbbās gives the ages plainly: Lamak was eighty-two when Nūḥ was born.':
  ('Ibn ʿAbbās menyebut usia-usianya dengan gamblang: Lamak berumur delapan puluh dua ketika Nūḥ lahir.',
   'Ibn ʿAbbās menyebut usia-usianya dengan jelas: Lamak berumur lapan puluh dua ketika Nūḥ lahir.'),
 'Nobody in that age forbade wrong, so God sent Nūḥ to them when he was four hundred and eighty.':
  ('Tak seorang pun pada zaman itu melarang kemungkaran, maka Allah mengutus Nūḥ kepada mereka ketika ia berumur empat ratus delapan puluh.',
   'Tiada seorang pun pada zaman itu melarang kemungkaran, maka Allah mengutus Nūḥ kepada mereka ketika dia berumur empat ratus lapan puluh.'),
 'He called them for a hundred and twenty years, then was ordered to build the ship, and he built it and rode in it at six hundred.':
  ('Ia menyeru mereka selama seratus dua puluh tahun, lalu diperintahkan membuat bahtera, dan ia membuatnya serta menaikinya pada umur enam ratus.',
   'Dia menyeru mereka selama seratus dua puluh tahun, kemudian diperintahkan membuat bahtera, dan dia membinanya serta menaikinya pada umur enam ratus.'),
 'Saʿīd b. al-Musayyab: Nūḥ had three sons — Sām, Ḥām and Yāfith.':
  ('Saʿīd b. al-Musayyab: Nūḥ punya tiga putra — Sām, Ḥām dan Yāfith.',
   'Saʿīd b. al-Musayyab: Nūḥ mempunyai tiga putera — Sām, Ḥām dan Yāfith.'),
 'The chapter is really a table of the nations: the Arabs, the Persians and the Byzantines from Sām, and so on through the rest.':
  ('Bab ini sesungguhnya sebuah daftar bangsa-bangsa: orang Arab, Persia dan Rum dari Sām, dan seterusnya untuk yang lain.',
   'Bab ini sebenarnya sebuah senarai bangsa-bangsa: orang Arab, Parsi dan Rom daripada Sām, dan seterusnya untuk yang lain.'),
 'Ibn ʿAbbās again: the Arabs, the Persians, the Nabateans, the people of India and Sind are of the children of Sām b. Nūḥ.':
  ('Ibn ʿAbbās lagi: orang Arab, Persia, Nabath, penduduk India dan Sind adalah anak keturunan Sām b. Nūḥ.',
   'Ibn ʿAbbās lagi: orang Arab, Parsi, Nabti, penduduk India dan Sind ialah anak keturunan Sām b. Nūḥ.'),
 'It is said ʿImlīq was the first to speak Arabic when they left Babel, and that he and Jurhum were called the Arabising Arabs.':
  ('Dikatakan ʿImlīq orang pertama yang berbicara bahasa Arab ketika mereka meninggalkan Babil, dan bahwa ia bersama Jurhum disebut al-ʿArab al-ʿĀriba.',
   'Dikatakan ʿImlīq orang pertama yang bertutur bahasa Arab ketika mereka meninggalkan Babil, dan bahawa dia bersama Jurhum disebut al-ʿArab al-ʿĀriba.'),
 "al-Kalbī: Ibrāhīm's father was of the people of Ḥarrān, and a year of drought drove him to Hurmuzjird with his wife.":
  ('al-Kalbī: ayah Ibrāhīm berasal dari penduduk Ḥarrān, dan tahun paceklik mendorongnya pindah ke Hurmuzjird bersama istrinya.',
   'al-Kalbī: bapa Ibrāhīm berasal daripada penduduk Ḥarrān, dan tahun kemarau mendorongnya berpindah ke Hurmuzjird bersama isterinya.'),
 'Her name is given as Nūnā bt. Karnabā,':
  ('Namanya disebut Nūnā binti Karnabā,',
   'Namanya disebut Nūnā binti Karnabā,'),
 'and, on other authority, as Abyūnā of the line of Afrāyim.':
  ('dan, menurut riwayat lain, Abyūnā dari keturunan Afrāyim.',
   'dan, menurut riwayat lain, Abyūnā daripada keturunan Afrāyim.'),
 'He was the first to take in a guest, the first to crumble bread into broth, and the first to see grey hair.':
  ('Ia orang pertama yang menjamu tamu, pertama yang meremuk roti ke dalam kuah, dan pertama yang melihat uban.',
   'Dia orang pertama yang menjamu tetamu, pertama yang meremukkan roti ke dalam kuah, dan pertama yang melihat uban.'),
 'ʿIkrima: Ibrāhīm was called the father of guests.':
  ('ʿIkrima: Ibrāhīm berkunyah Abū al-Aḍyāf, bapak para tamu.',
   'ʿIkrima: Ibrāhīm berkunyah Abū al-Aḍyāf, bapa para tetamu.'),
 'Abū Hurayra: he was circumcised with an adze at a hundred and twenty, and lived eighty years after it.':
  ('Abū Hurayra: ia berkhitan dengan kapak pada umur seratus dua puluh, dan hidup delapan puluh tahun sesudahnya.',
   'Abū Hurayra: dia berkhatan dengan kapak pada umur seratus dua puluh, dan hidup lapan puluh tahun selepasnya.'),
 'Ismāʿīl was born to him, and was his eldest.':
  ('Ismāʿīl lahir baginya, dan dialah yang sulung.',
   'Ismāʿīl lahir baginya, dan dialah yang sulung.'),
 'Hājar was a Copt, from a village near what is now the encampment of Egypt, and belonged to a Pharaoh.':
  ('Hājar seorang Qibti, dari sebuah desa dekat tempat yang kini menjadi Fusṭāṭ Mesir, dan milik seorang Firaun.',
   'Hājar seorang Qibti, daripada sebuah kampung berhampiran tempat yang kini menjadi Fusṭāṭ Mesir, dan milik seorang Firaun.'),
 'It was that Pharaoh who reached for Sāra and was struck down — or, it is said, his hand withered to his chest as he went to take hers.':
  ('Firaun itulah yang hendak menjamah Sāra lalu tersungkur — atau, menurut satu riwayat, tangannya mengering sampai ke dadanya ketika hendak meraih tangan Sāra.',
   'Firaun itulah yang hendak menyentuh Sāra lalu tersungkur — atau, menurut satu riwayat, tangannya mengering hingga ke dadanya ketika hendak meraih tangan Sāra.'),
 'God commanded Ibrāhīm to go to His sacred land; he rode al-Burāq with Ismāʿīl, then two years old, before him and Hājar behind.':
  ('Allah memerintahkan Ibrāhīm menuju tanah haram-Nya; ia menunggang al-Burāq dengan Ismāʿīl, yang saat itu berumur dua tahun, di depannya dan Hājar di belakangnya.',
   'Allah memerintahkan Ibrāhīm menuju tanah haram-Nya; dia menunggang al-Burāq dengan Ismāʿīl, yang ketika itu berumur dua tahun, di hadapannya dan Hājar di belakangnya.'),
 'Who first spoke Arabic is asked outright, and answered three ways in three consecutive reports.':
  ('Siapa yang pertama berbicara bahasa Arab ditanyakan terus terang, dan dijawab tiga cara dalam tiga riwayat berturut-turut.',
   'Siapa yang pertama bertutur bahasa Arab ditanya secara terus, dan dijawab tiga cara dalam tiga riwayat berturut-turut.'),
 'Muḥammad b. ʿAlī: Ismāʿīl, at thirteen.':
  ('Muḥammad b. ʿAlī: Ismāʿīl, pada umur tiga belas.',
   'Muḥammad b. ʿAlī: Ismāʿīl, pada umur tiga belas.'),
 "Others: he was inspired with the tongue of the Arabs from the day he was born, and all Ibrāhīm's other children spoke their father's tongue.":
  ('Yang lain: ia diilhami lisan Arab sejak hari ia dilahirkan, dan semua anak Ibrāhīm yang lain berbicara dengan lisan ayah mereka.',
   'Yang lain: dia diilhamkan lidah Arab sejak hari dia dilahirkan, dan semua anak Ibrāhīm yang lain bertutur dengan lidah bapa mereka.'),
 'al-Kalbī, flatly against both: Ismāʿīl did not speak Arabic and would not differ from his father — the first of his descendants to speak it were the sons of Raʿla bt. Yashjub.':
  ('al-Kalbī, bertentangan dengan keduanya: Ismāʿīl tidak berbicara bahasa Arab dan tidak mau menyalahi ayahnya — yang pertama berbicara dengannya dari keturunannya adalah anak-anak Raʿla binti Yashjub.',
   'al-Kalbī, bercanggah dengan kedua-duanya: Ismāʿīl tidak bertutur bahasa Arab dan tidak mahu menyalahi bapanya — yang pertama bertutur dengannya daripada keturunannya ialah anak-anak Raʿla binti Yashjub.'),
 "Hishām al-Kalbī opens: my father taught me the Prophet's lineage when I was a boy — and recites it down through the epithets.":
  ('Hishām al-Kalbī membuka: ayahku mengajariku nasab Nabi ﷺ ketika aku masih kecil — lalu ia menuturkannya turun melalui julukan-julukannya.',
   'Hishām al-Kalbī membuka: bapaku mengajarku nasab Nabi ﷺ ketika aku masih kecil — lalu dia menuturkannya turun melalui gelaran-gelarannya.'),
 "A man of Tadmur who had read the books of the Children of Israel reported that Bārūkh, Jeremiah's scribe, had written down the line of Maʿadd b. ʿAdnān, and that the rabbis knew it.":
  ('Seorang penduduk Tadmur yang membaca kitab-kitab Bani Israil menyebutkan bahwa Bārūkh, juru tulis Irmiyā, telah mencatat nasab Maʿadd b. ʿAdnān, dan bahwa para rabi mengetahuinya.',
   'Seorang penduduk Tadmur yang membaca kitab-kitab Bani Israil menyebut bahawa Bārūkh, jurutulis Irmiyā, telah mencatat nasab Maʿadd b. ʿAdnān, dan bahawa para rabbi mengetahuinya.'),
 'Ibn Saʿd then gives his own verdict, and it is the reason this site stops where it does.':
  ('Ibn Saʿd lalu memberikan keputusannya sendiri, dan itulah sebabnya situs ini berhenti di titik ini.',
   'Ibn Saʿd kemudian memberikan keputusannya sendiri, dan itulah sebabnya laman ini berhenti di titik ini.'),
 'I have seen no disagreement among them that Maʿadd is of the children of Qaydar b. Ismāʿīl. This disagreement about his descent shows that it was not preserved — it was taken from the People of the Book and translated for them, and they differed over it.':
  ('Aku tidak melihat perselisihan di antara mereka bahwa Maʿadd berasal dari anak keturunan Qaydar b. Ismāʿīl. Perselisihan tentang nasabnya ini menunjukkan bahwa ia tidak terpelihara — ia diambil dari Ahli Kitab dan diterjemahkan bagi mereka, lalu mereka berselisih tentangnya.',
   'Aku tidak melihat perselisihan antara mereka bahawa Maʿadd berasal daripada anak keturunan Qaydar b. Ismāʿīl. Perselisihan tentang nasabnya ini menunjukkan bahawa ia tidak terpelihara — ia diambil daripada Ahli Kitab dan diterjemahkan bagi mereka, lalu mereka berselisih tentangnya.'),
 'And had it been sound, the Messenger of God would have known it best of anyone. So the matter with us ends at Maʿadd.':
  ('Dan seandainya itu sahih, Rasulullah ﷺ tentu yang paling mengetahuinya. Maka perkara ini menurut kami berhenti pada Maʿadd.',
   'Dan sekiranya itu sahih, Rasulullah ﷺ tentu yang paling mengetahuinya. Maka perkara ini menurut kami berhenti pada Maʿadd.'),
 'The Prophet, in the same chapter: do not revile Muḍar, for he had submitted.':
  ('Nabi ﷺ, dalam bab yang sama: janganlah kalian mencela Muḍar, sebab ia telah berserah diri.',
   'Nabi ﷺ, dalam bab yang sama: janganlah kamu mencela Muḍar, kerana dia telah berserah diri.'),
 'Hishām al-Kalbī recites the line and stops at the name that defines the tribe.':
  ('Hishām al-Kalbī menuturkan nasab itu dan berhenti pada nama yang menentukan batas kabilah.',
   'Hishām al-Kalbī menuturkan nasab itu dan berhenti pada nama yang menentukan sempadan kabilah.'),
 'Quraysh gather at Fihr — and whoever stands above Fihr is not called Qurashī.':
  ('Quraisy berhimpun pada Fihr — dan siapa yang berada di atas Fihr tidak disebut Qurasyi.',
   'Quraisy berhimpun pada Fihr — dan sesiapa yang berada di atas Fihr tidak disebut Qurasyi.'),
 'Above him the line runs through Mālik, al-Naḍr, Kināna, Khuzayma and Mudrika to Maʿadd b. ʿAdnān, and there Ibn Saʿd stops.':
  ('Di atasnya nasab itu naik melalui Mālik, al-Naḍr, Kināna, Khuzayma dan Mudrika sampai Maʿadd b. ʿAdnān, dan di situlah Ibn Saʿd berhenti.',
   'Di atasnya nasab itu naik melalui Mālik, al-Naḍr, Kināna, Khuzayma dan Mudrika hingga Maʿadd b. ʿAdnān, dan di situlah Ibn Saʿd berhenti.'),
 "Of Maʿadd's sons, Nizār fathered Muḍar and Iyād — his kunya — by Sawda bt. ʿAkk, and Rabīʿa and Anmār by another mother.":
  ('Di antara putra Maʿadd, Nizār memperoleh Muḍar dan Iyād — yang menjadi kunyahnya — dari Sawda binti ʿAkk, dan Rabīʿa serta Anmār dari ibu yang lain.',
   'Antara putera Maʿadd, Nizār memperoleh Muḍar dan Iyād — yang menjadi kunyahnya — daripada Sawda binti ʿAkk, dan Rabīʿa serta Anmār daripada ibu yang lain.'),
 'Muḍar was called the Red, Iyād the Grey-and-Piebald.':
  ('Muḍar dijuluki al-Ḥamrāʾ, si merah, dan Iyād al-Shamṭāʾ wal-Balqāʾ.',
   'Muḍar digelar al-Ḥamrāʾ, si merah, dan Iyād al-Shamṭāʾ wal-Balqāʾ.'),
 'Of Banū al-Najjār of al-Khazraj; his mother was Umm Sulaym bt. Milḥān, of the same clan.':
  ('Dari Banū al-Najjār dari al-Khazraj; ibunya Umm Sulaym binti Milḥān, dari kabilah yang sama.',
   'Daripada Banū al-Najjār daripada al-Khazraj; ibunya Umm Sulaym binti Milḥān, daripada kabilah yang sama.'),
 'Abū Ṭalḥa took his hand when the Prophet reached Medina: Messenger of God, Anas is a clever boy, let him serve you.':
  ('Abū Ṭalḥa memegang tangannya ketika Nabi ﷺ tiba di Madinah: wahai Rasulullah, Anas anak yang cerdas, biarlah ia melayanimu.',
   'Abū Ṭalḥa memegang tangannya ketika Nabi ﷺ tiba di Madinah: wahai Rasulullah, Anas budak yang cerdik, biarlah dia berkhidmat kepadamu.'),
 "His mother's version has her bring him herself: this is my son, and he is a boy who writes.":
  ('Versi ibunya, dialah yang membawanya sendiri: ini putraku, dan ia anak yang bisa menulis.',
   'Versi ibunya, dialah yang membawanya sendiri: ini puteraku, dan dia budak yang boleh menulis.'),
 'How long he served, and from what age, he tells differently in different reports.':
  ('Berapa lama ia melayani, dan sejak usia berapa, ia ceritakan berbeda-beda dalam riwayat yang berbeda.',
   'Berapa lama dia berkhidmat, dan sejak usia berapa, dia ceritakan berbeza-beza dalam riwayat yang berlainan.'),
 'I served the Prophet ten years, and he never once said uff to me.':
  ('Aku melayani Nabi ﷺ sepuluh tahun, dan beliau tak pernah sekali pun berkata ah kepadaku.',
   'Aku berkhidmat kepada Nabi ﷺ sepuluh tahun, dan baginda tidak pernah sekali pun berkata ah kepadaku.'),
 'I served him nine years, and he never said of anything I did: you did badly.':
  ('Aku melayaninya sembilan tahun, dan beliau tak pernah berkata tentang sesuatu yang kukerjakan: engkau berbuat buruk.',
   'Aku berkhidmat kepadanya sembilan tahun, dan baginda tidak pernah berkata tentang sesuatu yang aku lakukan: engkau berbuat buruk.'),
 'I served the Messenger of God when I was eight years old.':
  ('Aku melayani Rasulullah ﷺ ketika aku berumur delapan tahun.',
   'Aku berkhidmat kepada Rasulullah ﷺ ketika aku berumur lapan tahun.'),
 'And if any of the household blamed him, the Prophet would say: leave him — had it been decreed, it would have been.':
  ('Dan bila ada anggota keluarga yang menyalahkannya, Nabi ﷺ berkata: biarkanlah ia — sekiranya ditakdirkan, tentu terjadi.',
   'Dan jika ada ahli keluarga yang menyalahkannya, Nabi ﷺ berkata: biarkanlah dia — sekiranya ditakdirkan, tentu berlaku.'),
 'His mother asked a prayer for him: God, increase his wealth and his children, lengthen his life and forgive his sin.':
  ('Ibunya memohon doa untuknya: ya Allah, perbanyaklah harta dan anaknya, panjangkanlah umurnya dan ampunilah dosanya.',
   'Ibunya memohon doa untuknya: ya Allah, perbanyakkanlah harta dan anaknya, panjangkanlah umurnya dan ampunilah dosanya.'),
 'Anas afterwards: I have buried a hundred of my own children bar two, and my palms bear twice a year.':
  ('Anas sesudahnya: aku telah memakamkan seratus kurang dua dari anak-anak kandungku, dan pohon kurmaku berbuah dua kali setahun.',
   'Anas selepas itu: aku telah mengebumikan seratus kurang dua daripada anak-anak kandungku, dan pokok kurmaku berbuah dua kali setahun.'),
 'He was the last Companion to die at Baṣra.':
  ('Ia sahabat terakhir yang wafat di Basrah.',
   'Dia sahabat terakhir yang wafat di Basrah.'),
 'His age at death is given as ninety-nine,':
  ('Usianya saat wafat disebut sembilan puluh sembilan,',
   'Usianya ketika wafat disebut sembilan puluh sembilan,'),
 'and Ibn Saʿd, asking the qāḍī Muḥammad b. ʿAbd Allāh al-Anṣārī outright, is told a hundred and seven.':
  ('dan Ibn Saʿd, yang bertanya langsung kepada kadi Muḥammad b. ʿAbd Allāh al-Anṣārī, dijawab seratus tujuh.',
   'dan Ibn Saʿd, yang bertanya terus kepada kadi Muḥammad b. ʿAbd Allāh al-Anṣārī, dijawab seratus tujuh.'),
 'Of Banū al-Naḍīr, married to a man of Banū Qurayẓa called al-Ḥakam — which is why some transmitters assign her to Qurayẓa instead.':
  ('Dari Banū al-Naḍīr, menikah dengan seorang lelaki Banū Qurayẓa bernama al-Ḥakam — karena itulah sebagian perawi menisbatkannya kepada Qurayẓa.',
   'Daripada Banū al-Naḍīr, berkahwin dengan seorang lelaki Banū Qurayẓa bernama al-Ḥakam — kerana itulah sebahagian perawi menisbahkannya kepada Qurayẓa.'),
 'Thaʿlaba b. Abī Mālik: when the captives of Qurayẓa fell, the Messenger of God took her, freed her, married her, and she died with him.':
  ('Thaʿlaba b. Abī Mālik: ketika tawanan Qurayẓa jatuh, Rasulullah ﷺ mengambilnya, memerdekakannya, menikahinya, dan ia wafat dalam pemeliharaan beliau.',
   'Thaʿlaba b. Abī Mālik: ketika tawanan Qurayẓa jatuh, Rasulullah ﷺ mengambilnya, memerdekakannya, mengahwininya, dan dia wafat dalam pemeliharaan baginda.'),
 'Her own account: I was among those shown to him, and he had me set aside.':
  ('Penuturannya sendiri: aku termasuk yang ditawarkan kepada beliau, dan beliau menyuruh agar aku dipisahkan.',
   'Ceritanya sendiri: aku termasuk yang ditawarkan kepada baginda, dan baginda menyuruh agar aku diasingkan.'),
 'He said: if you choose God and His Messenger, then the Messenger of God chooses you for himself. And I said I choose God and His Messenger.':
  ('Beliau berkata: jika engkau memilih Allah dan Rasul-Nya, maka Rasulullah ﷺ memilihmu untuk dirinya. Dan aku berkata aku memilih Allah dan Rasul-Nya.',
   'Baginda berkata: jika engkau memilih Allah dan Rasul-Nya, maka Rasulullah ﷺ memilihmu untuk dirinya. Dan aku berkata aku memilih Allah dan Rasul-Nya.'),
 'When I became Muslim he freed me and married me and gave me twelve ounces and a nashsh, as he gave his wives.':
  ('Ketika aku masuk Islam beliau memerdekakanku dan menikahiku dan memberiku mahar dua belas uqiyah dan satu nash, sebagaimana beliau memberi istri-istrinya.',
   'Ketika aku memeluk Islam baginda memerdekakan aku dan mengahwini aku dan memberi aku mahar dua belas auns dan satu nash, sebagaimana baginda memberi isteri-isterinya.'),
 'Muḥammad b. Kaʿb has it differently: she was of the spoil, and he gave her the choice between Islam and her own religion.':
  ('Muḥammad b. Kaʿb meriwayatkannya berbeda: ia termasuk fai, dan beliau memberinya pilihan antara Islam dan agamanya sendiri.',
   'Muḥammad b. Kaʿb meriwayatkannya berbeza: dia termasuk fai, dan baginda memberinya pilihan antara Islam dan agamanya sendiri.'),
 'In that account she grew violently jealous, he divorced her once, she wept, and he took her back.':
  ('Dalam riwayat itu ia menjadi sangat cemburu, beliau menceraikannya sekali, ia menangis, dan beliau merujuknya.',
   'Dalam riwayat itu dia menjadi sangat cemburu, baginda menceraikannya sekali, dia menangis, dan baginda merujuknya.'),
 'Ibn Saʿd puts the marriage in Muḥarram of the year six; she remained with him until she died on his return from the Farewell Pilgrimage, and he buried her at al-Baqīʿ.':
  ('Ibn Saʿd menempatkan pernikahan itu pada Muharram tahun keenam; ia tetap bersama beliau sampai wafat saat beliau kembali dari Haji Wada, dan beliau memakamkannya di al-Baqīʿ.',
   'Ibn Saʿd meletakkan perkahwinan itu pada Muharram tahun keenam; dia kekal bersama baginda sehingga wafat ketika baginda pulang dari Haji Wada, dan baginda mengebumikannya di al-Baqīʿ.'),
 'The lists that count thirteen wives are the lists that leave her out.':
  ('Daftar yang menghitung tiga belas istri adalah daftar yang tidak memasukkannya.',
   'Senarai yang mengira tiga belas isteri ialah senarai yang tidak memasukkannya.'),
}
