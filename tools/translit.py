# -*- coding: utf-8 -*-
"""Arabic -> ALA-LC transliteration.

Unvocalised Arabic does not carry the vowels transliteration needs: عمرو is ʿAmr, but the
letters alone say only ʿ-m-r-w. So: a dictionary for the names that actually recur in this
material, and a consonant-skeleton fallback for the rest, flagged so the page can say the
reading is provisional. The Arabic is always the authority; the Latin is a finding aid.
"""
import re

# names that carry the tree - hand-checked readings
NAMES = {
 "محمد":"Muḥammad","عبد الله":"ʿAbd Allāh","عبد المطلب":"ʿAbd al-Muṭṭalib","هاشم":"Hāshim",
 "عبد مناف":"ʿAbd Manāf","قصي":"Quṣayy","كلاب":"Kilāb","مرة":"Murra","كعب":"Kaʿb","لؤي":"Luʾayy",
 "غالب":"Ghālib","فهر":"Fihr","مالك":"Mālik","النضر":"al-Naḍr","كنانة":"Kināna","خزيمة":"Khuzayma",
 "مدركة":"Mudrika","إلياس":"Ilyās","الياس":"Ilyās","مضر":"Muḍar","نزار":"Nizār","معد":"Maʿadd",
 "عدنان":"ʿAdnān","أدد":"Udad","أد":"Udd","مقوم":"Muqawwam","ناحور":"Nāḥūr","تيرح":"Tayraḥ",
 "يعرب":"Yaʿrub","يشجب":"Yashjub","نابت":"Nābit","إسماعيل":"Ismāʿīl","اسماعيل":"Ismāʿīl",
 "إبراهيم":"Ibrāhīm","ابراهيم":"Ibrāhīm","تارح":"Tāriḥ","ساروغ":"Sārūgh","راعو":"Rāʿū",
 "فالخ":"Fālikh","عيبر":"ʿAybar","عابر":"ʿĀbir","شالخ":"Shālikh","أرفخشذ":"Arfakhshadh",
 "سام":"Sām","نوح":"Nūḥ","لمك":"Lamk","لامك":"Lāmak","متوشلخ":"Mattūshalakh","أخنوخ":"Akhnūkh",
 "إدريس":"Idrīs","يرد":"Yard","يارد":"Yārid","مهليل":"Mahlīl","مهلائيل":"Mahlāʾīl","قينن":"Qaynan",
 "قينان":"Qaynān","يانش":"Yānish","أنوش":"Anūsh","شيث":"Shīth","آدم":"Ādam",
 # Quraysh and the clans
 "عبد شمس":"ʿAbd Shams","المطلب":"al-Muṭṭalib","نوفل":"Nawfal","عبد العزى":"ʿAbd al-ʿUzzā",
 "عبد الدار":"ʿAbd al-Dār","زهرة":"Zuhra","تيم":"Taym","يقظة":"Yaqaẓa","مخزوم":"Makhzūm",
 "عدي":"ʿAdī","عدى":"ʿAdī","هصيص":"Huṣayṣ","سهم":"Sahm","جمح":"Jumaḥ","عامر":"ʿĀmir",
 "الحارث":"al-Ḥārith","محارب":"Muḥārib","أمية":"Umayya","امية":"Umayya","حبيب":"Ḥabīb",
 "ربيعة":"Rabīʿa","أسد":"Asad","اسد":"Asad","خويلد":"Khuwaylid","العوام":"al-ʿAwwām",
 "أسيد":"Usayd","عثمان":"ʿUthmān","عفان":"ʿAffān","أبو العاص":"Abū al-ʿĀṣ","العاص":"al-ʿĀṣ",
 "حرب":"Ḥarb","أبو سفيان":"Abū Sufyān","صخر":"Ṣakhr","معاوية":"Muʿāwiya","عتبة":"ʿUtba",
 "شيبة":"Shayba","الوليد":"al-Walīd","المغيرة":"al-Mughīra","هشام":"Hishām","خالد":"Khālid",
 "عمرو":"ʿAmr","عمر":"ʿUmar","الخطاب":"al-Khaṭṭāb","نفيل":"Nufayl","زيد":"Zayd","سعيد":"Saʿīd",
 "طلحة":"Ṭalḥa","عبيد الله":"ʿUbayd Allāh","أبو بكر":"Abū Bakr","أبو قحافة":"Abū Quḥāfa",
 "عثمان بن عامر":"ʿUthmān b. ʿĀmir","سعد":"Saʿd","أبو وقاص":"Abū Waqqāṣ","مالك بن أهيب":"Mālik b. Uhayb",
 "عبد الرحمن":"ʿAbd al-Raḥmān","عوف":"ʿAwf","الزبير":"al-Zubayr","حكيم":"Ḥakīm","حزام":"Ḥizām",
 "أبو طالب":"Abū Ṭālib","أبو لهب":"Abū Lahab","العباس":"al-ʿAbbās","حمزة":"Ḥamza",
 "أبو الفضل":"Abū al-Faḍl","الحسن":"al-Ḥasan","الحسين":"al-Ḥusayn","علي":"ʿAlī","على":"ʿAlī",
 "جعفر":"Jaʿfar","عقيل":"ʿAqīl","طالب":"Ṭālib","فاطمة":"Fāṭima","زينب":"Zaynab","رقية":"Ruqayya",
 "أم كلثوم":"Umm Kulthūm","خديجة":"Khadīja","آمنة":"Āmina","سلمى":"Salmā","وهب":"Wahb",
 "عبد يغوث":"ʿAbd Yaghūth","هالة":"Hāla","صفية":"Ṣafiyya","عاتكة":"ʿĀtika","برة":"Barra",
 "أميمة":"Umayma","أروى":"Arwā","القاسم":"al-Qāsim","إبراهيم بن محمد":"Ibrāhīm b. Muḥammad",
 "الطاهر":"al-Ṭāhir","الطيب":"al-Ṭayyib","عبد الكعبة":"ʿAbd al-Kaʿba","المقوم":"al-Muqawwim",
 "ضرار":"Ḍirār","الغيداق":"al-Ghaydāq","حجل":"Ḥajl","قثم":"Quthham","الفضل":"al-Faḍl",
 "معبد":"Maʿbad","عبيد":"ʿUbayd","تمام":"Tammām","كثير":"Kathīr","عون":"ʿAwn",
 "يزيد":"Yazīd","سليمان":"Sulaymān","إسحاق":"Isḥāq","يعقوب":"Yaʿqūb","يوسف":"Yūsuf",
 "موسى":"Mūsā","هارون":"Hārūn","داود":"Dāwūd","إياد":"Iyād","أنمار":"Anmār","قنص":"Qanṣ",
 "قيس":"Qays","عيلان":"ʿAylān","هذيل":"Hudhayl","أسلم":"Aslam","الهون":"al-Hūn","مليح":"Mulayḥ",
 "النضر بن كنانة":"al-Naḍr b. Kināna","عبد مناة":"ʿAbd Manāt","بكر":"Bakr","الديل":"al-Dīl",
 "ضمرة":"Ḍamra","ليث":"Layth","غفار":"Ghifār","تغلب":"Taghlib","وائل":"Wāʾil","أنس":"Anas",
 "جشم":"Jusham","النمر":"al-Namir","عنزة":"ʿAnaza","عبد القيس":"ʿAbd al-Qays","أفصى":"Afṣā",
 "هوازن":"Hawāzin","سليم":"Sulaym","غطفان":"Ghaṭafān","أشجع":"Ashjaʿ","عبس":"ʿAbs","ذبيان":"Dhubyān",
 "تميم":"Tamīm","ضبة":"Ḍabba","الرباب":"al-Ribāb","مزينة":"Muzayna","طابخة":"Ṭābikha",
 "قمعة":"Qamʿa","خندف":"Khindif","الياس بن مضر":"Ilyās b. Muḍar","قحطان":"Qaḥṭān","يقطان":"Yaqṭān",
 "سبأ":"Sabaʾ","حمير":"Ḥimyar","كهلان":"Kahlān","الأزد":"al-Azd","همدان":"Hamdān","مذحج":"Madhḥij",
 "كندة":"Kinda","لخم":"Lakhm","جذام":"Judhām","طيء":"Ṭayyiʾ","الأوس":"al-Aws","الخزرج":"al-Khazraj",
 "حارثة":"Ḥāritha","ثعلبة":"Thaʿlaba","عوص":"ʿAwṣ","إرم":"Iram","لوذ":"Lūdh","عاد":"ʿĀd",
 "ثمود":"Thamūd","جرهم":"Jurhum","قيدر":"Qaydar","قيذر":"Qaydhar","الهميسع":"al-Humaysaʿ",
 "نبت":"Nabt","تيمن":"Tayman","أشجب":"Ashjab","الأسود":"al-Aswad","جندب":"Jundab",
 "المقداد":"al-Miqdād","بلال":"Bilāl","سلمان":"Salmān","صهيب":"Ṣuhayb","أبو ذر":"Abū Dharr",
 "أبو هريرة":"Abū Hurayra","أبو أيوب":"Abū Ayyūb","أبي":"Ubayy","معاذ":"Muʿādh","جبل":"Jabal",
 "أنس بن مالك":"Anas b. Mālik","النعمان":"al-Nuʿmān","بشير":"Bashīr","الأرقم":"al-Arqam",
 "مصعب":"Muṣʿab","عمير":"ʿUmayr","عمار":"ʿAmmār","ياسر":"Yāsir","سمية":"Sumayya",
 "خباب":"Khabbāb","الأرت":"al-Aratt","سهيل":"Suhayl","حاطب":"Ḥāṭib","أبي بلتعة":"Abī Baltaʿa",
 "أسامة":"Usāma","حارثة بن شراحيل":"Ḥāritha b. Sharāḥīl","جبير":"Jubayr","مطعم":"Muṭʿim",
 "قتادة":"Qatāda","النعمان بن بشير":"al-Nuʿmān b. Bashīr","سمرة":"Samura","جندب بن سفيان":"Jundab b. Sufyān",
 "سفيان":"Sufyān","صفوان":"Ṣafwān","عكرمة":"ʿIkrima","أبو جهل":"Abū Jahl","هند":"Hind",
 "سودة":"Sawda","عائشة":"ʿĀʾisha","حفصة":"Ḥafṣa","أم سلمة":"Umm Salama","زينب بنت جحش":"Zaynab bt. Jaḥsh",
 "جويرية":"Juwayriya","أم حبيبة":"Umm Ḥabība","ميمونة":"Maymūna","مارية":"Māriya",
 "جحش":"Jaḥsh","أم حكيم البيضاء":"Umm Ḥakīm al-Bayḍāʾ","البيضاء":"al-Bayḍāʾ",
 "المحسن":"al-Muḥsin","مارية القبطية":"Māriya al-Qibṭiyya","القبطية":"al-Qibṭiyya",
 "أم حكيم":"Umm Ḥakīm","خويلد":"Khuwaylid","أمامة":"Umāma","المطلب بن عبد مناف":"al-Muṭṭalib",
 "عبد الكعبة":"ʿAbd al-Kaʿba","الغيداق":"al-Ghaydāq","نضلة":"Naḍla","أبو صيفي":"Abū Ṣayfī",
 "أسماء":"Asmāʾ","أم هانئ":"Umm Hāniʾ","جمانة":"Jumāna","ريطة":"Rayṭa","لبابة":"Lubāba",
 "أم الفضل":"Umm al-Faḍl","سلمة":"Salama","عبد الله بن عثمان":"ʿAbd Allāh b. ʿUthmān","الحارث بن أبي ضرار":"al-Ḥārith b. Abī Ḍirār","حيي":"Ḥuyayy","أخطب":"Akhṭab",
}


# --- added after Phase 5: the readings that recur across Quraysh, Mudar and the Yemen
EXTRA = {
 "عبد":"ʿAbd","جابر":"Jābir","هلال":"Hilāl","نافع":"Nāfiʿ","عبد الملك":"ʿAbd al-Malik",
 "جذيمة":"Judhayma","حذافة":"Ḥudhāfa","شداد":"Shaddād","زهير":"Zuhayr","عيسى":"ʿĪsā",
 "نصر":"Naṣr","معمر":"Maʿmar","السائب":"al-Sāʾib","خلف":"Khalaf","حفص":"Ḥafṣ","أنيس":"Unays",
 "الحصين":"al-Ḥuṣayn","سليط":"Sulayṭ","عائذ":"ʿĀʾidh","رياح":"Riyāḥ","أبان":"Abān",
 "عاصم":"ʿĀṣim","مسلم":"Muslim","محصن":"Miḥṣan","علقمة":"ʿAlqama","جنادة":"Junāda",
 "زمعة":"Zamʿa","صبرة":"Ṣabra","يعمر":"Yaʿmar","محرز":"Muḥriz","طريف":"Ṭarīf","بكير":"Bukayr",
 "قرط":"Qurṭ","حرام":"Ḥarām","أسعد":"Asʿad","مسعود":"Masʿūd","بدر":"Badr","منصور":"Manṣūr",
 "أبو أمية":"Abū Umayya","سيار":"Sayyār","عمارة":"ʿUmāra","فراس":"Firās","مازن":"Māzin",
 "رهم":"Ruhm","عتيق":"ʿAtīq","منقر":"Minqar","ثور":"Thawr","قرة":"Qurra","مخرمة":"Makhrama",
 "عباد":"ʿAbbād","حسل":"Ḥisl","عبد عوف":"ʿAbd ʿAwf","الصلت":"al-Ṣalt","عبد ود":"ʿAbd Wudd",
 "عبدود":"ʿAbd Wudd","جبيلة":"Jubayla","أزهر":"Azhar","شهاب":"Shihāb",
 "عبد الأسد":"ʿAbd al-Asad","الخيار":"al-Khiyār","عبيدة":"ʿUbayda","حريث":"Ḥurayth",
 "لقيط":"Laqīṭ","أبو حذيفة":"Abū Ḥudhayfa","غنم":"Ghanm","أهيب":"Uhayb","كلدة":"Kalada",
 "هبار":"Habbār","الفاكه":"al-Fākih","قعين":"Quʿayn","فقعس":"Faqʿas","حجوان":"Ḥajwān",
 "الأشتر":"al-Ashtar","أكثم":"Akthum","رزاح":"Rizāḥ","كبير":"Kabīr","شبيب":"Shabīb",
 "أوس":"Aws","غانم":"Ghānim","حذيفة":"Ḥudhayfa","واثلة":"Wāthila","حرثان":"Ḥarthān",
 "سويد":"Suwayd","خنيس":"Khunays","الحكم":"al-Ḥakam","خارجة":"Khārija","أبو سلمة":"Abū Salama",
 "أبو ربيعة":"Abū Rabīʿa","المعتمر":"al-Muʿtamir","سراقة":"Surāqa","نبيه":"Nabīh",
 "الغوث":"al-Ghawth","عنبسة":"ʿAnbasa","لأى":"Laʾy","محلم":"Muḥallim","كراثة":"Kurātha",
 "جلان":"Jullān","بلبلة":"Balbala","حمار":"Ḥimār","ماوية":"Māwiyya","أبو بردة":"Abū Burda",
 "أبو قيس":"Abū Qays","أبو عبيدة":"Abū ʿUbayda","عبد العزيز":"ʿAbd al-ʿAzīz",
 "سلامان":"Salāmān","رواحة":"Rawāḥa","خلاوة":"Khalāwa","سنان":"Sinān","سامة":"Sāma",
 "أبو سعيد":"Abū Saʿīd","أبو عمر":"Abū ʿUmar","كريز":"Kurayz","الربيع":"al-Rabīʿ",
 "أبو العاص":"Abū al-ʿĀṣ","أبو العاصى":"Abū al-ʿĀṣ","أبا العاص":"Abū al-ʿĀṣ",
 "خويلدا":"Khuwaylid","عبد الحارث":"ʿAbd al-Ḥārith","شريح":"Shurayḥ","أبو سعد":"Abū Saʿd",
 "العقيم":"al-ʿAqīm","شرحبيل":"Shuraḥbīl","جهم":"Jahm","جهيم":"Juhaym","صبيحة":"Ṣubayḥa",
 "طليق":"Ṭalīq","عقبة":"ʿUqba","عبد يزيد":"ʿAbd Yazīd","عجير":"ʿUjayr","دودان":"Dūdān",
 "رياب":"Riyāb","أبو السائب":"Abū al-Sāʾib","أثاثة":"Uthātha","مسطح":"Misṭaḥ",
 "ظريب":"Ẓarib","النضير":"al-Naḍīr","هريم":"Huraym","غيرة":"Ghīra","ناشب":"Nāshib",
 "عبد ياليل":"ʿAbd Yālīl","البكير":"al-Bukayr","وايلة":"Wāʾila","وائلة":"Wāʾila",
 "عرنة":"ʿUrana","نقير":"Nuqayr","خيشنة":"Khayshana","شجع":"Shajʿ","عويرة":"ʿUwayra",
 "عوذ":"ʿAwdh","شيبان":"Shaybān","عرفطة":"ʿArfaṭa","سخبرة":"Sakhbara","الهدير":"al-Hudayr",
 "جدعان":"Judʿān","رواح":"Rawāḥ","محمية":"Maḥmiya","زنيم":"Zunaym","ثابت":"Thābit",
 "رقيش":"Ruqaysh","مهان":"Mahān","الأحب":"al-Aḥabb","مرداس":"Mirdās","عياض":"ʿIyāḍ",
 "مسافع":"Musāfiʿ","نفاثة":"Nufātha","حلبس":"Ḥalbas","جندل":"Jandal","وديعة":"Wadīʿa",
 "عويج":"ʿUwayj","الجراح":"al-Jarrāḥ","حدي":"Ḥiddī","خميس":"Khumays","العاصي":"al-ʿĀṣī",
 "العاصى":"al-ʿĀṣī","عباس":"ʿAbbās","بجرة":"Bajra","كاهل":"Kāhil","صاهلة":"Ṣāhila",
 "شمخ":"Shamkh","غافل":"Ghāfil","مطيع":"Muṭīʿ","نضر":"Naḍr","وقدان":"Waqdān",
 "مظعون":"Maẓʿūn","جدي":"Judayy","جدى":"Judayy","ناشرة":"Nāshira","إياس":"Iyās",
 "رويبة":"Ruwayba","شأس":"Shaʾs","الملوح":"al-Mulawwiḥ","أشيم":"Ashyam","مليل":"Mulayl",
 "أحيمس":"Uḥaymis","أبو جهم":"Abū Jahm","عابد":"ʿĀbid","صبيرة":"Ṣubayra","سلامة":"Salāma",
 "قنفذ":"Qunfudh","مساحق":"Masāḥiq","كلب":"Kalb","حزن":"Ḥazn","صبابة":"Ṣubāba",
 "الأسقع":"al-Asqaʿ","سحيم":"Suḥaym","بشر":"Bishr","جميل":"Jamīl","مؤمل":"Muʾammal",
 "مسلمة":"Maslama","حطاب":"Ḥaṭṭāb","الضحاك":"al-Ḍaḥḥāk","أهبان":"Ahbān","عكاشة":"ʿUkkāsha",
 "عبد الأسود":"ʿAbd al-Aswad","أداة":"Adāt","عاقل":"ʿĀqil","قدامة":"Qudāma","صيفي":"Ṣayfī",
 "فضلة":"Faḍla","ضبيرة":"Ḍubayra","واقعة":"Wāqiʿa","شريق":"Shurayq","معشر":"Maʿshar",
 "زبيد":"Zubayd","حنطب":"Ḥanṭab","الزبعري":"al-Zibaʿrā","أمري القيس":"Imruʾ al-Qays",
 "امرئ القيس":"Imruʾ al-Qays","عمران":"ʿImrān","أيوب":"Ayyūb","سابط":"Sābiṭ","سهل":"Sahl",
 "السكران":"al-Sakrān","المتلمس":"al-Mutalammis","منيع":"Manīʿ","القطامى":"al-Quṭāmī",
 "ظالم":"Ẓālim","نباتة":"Nubāta","حيدان":"Ḥaydān","عريب":"ʿArīb","ذهل":"Dhuhl",
 "سواد":"Sawād","خنساء":"Khansāʾ","أوسلة":"Awsala","ألهان":"Alhān","حوشب":"Ḥawshab",
 "جلد":"Jald","يحابر":"Yuḥābir","الصعب":"al-Ṣaʿb","نمرة":"Namira","جعفى":"Juʿfī",
 "الحر":"al-Ḥurr","أشرس":"Ashras","الدئل":"al-Dīl","مران":"Murrān","علة":"ʿIlla",
 "جسر":"Jasr","مسلية":"Masliya","أحمد":"Aḥmad","البختري":"al-Bakhtarī","حصن":"Ḥiṣn",
 "شريف":"Sharīf","حبال":"Ḥibāl","زفر":"Zufar","المسور":"al-Miswar","العجلان":"al-ʿAjlān",
 "خشين":"Khushayn","عطية":"ʿAṭiyya","شكم":"Shukm","بغيض":"Baghīḍ","غزية":"Ghaziyya",
 "خبيب":"Khubayb","سلم":"Salm","عبد المجيد":"ʿAbd al-Majīd","شعيب":"Shuʿayb",
 "مهشم":"Muhashshim","أبو الحكم":"Abū al-Ḥakam","أبو هاشم":"Abū Hāshim","عروة":"ʿUrwa",
 "أبو سليمان":"Abū Sulaymān","المنصور":"al-Manṣūr","حميد":"Ḥumayd","تويت":"Tuwayt",
 "المرتفع":"al-Murtafiʿ","قاسط":"Qāsiṭ","عياش":"ʿAyyāsh","جامع":"Jāmiʿ","مكرز":"Mikraz",
 "جندع":"Jundaʿ","عتوارة":"ʿUtwāra","حميس":"Ḥumays","غفار":"Ghifār","مدلج":"Mudlij",
 "مبذول":"Mabdhūl","غاضرة":"Ghāḍira","مر":"Murr","يعفر":"Yaʿfur","مقاعس":"Muqāʿis",
 "زهر":"Zuhr","دعمى":"Duʿmī","نمارة":"Numāra","عميرة":"ʿUmayra","عامرة":"ʿĀmira",
 "الأصبغ":"al-Aṣbagh","ورقة":"Waraqa","رزق":"Rizq","الشداخ":"al-Shaddākh","غضبان":"Ghaḍbān",
 "زيد مناة":"Zayd Manāt","زيد منا":"Zayd Manāt","مخاشن":"Mukhāshin","عصية":"ʿUṣayya",
 "دهمان":"Dahmān","حنظلة":"Ḥanẓala","يعلى":"Yaʿlā","رافع":"Rāfiʿ","صريم":"Ṣuraym",
 "خصفة":"Khaṣafa","أدى":"Udayy","هانئ":"Hāniʾ","هبيرة":"Hubayra","عفير":"ʿUfayr",
 "المؤمل":"al-Muʾammal","المجزم":"al-Mujazzam","كلوب":"Kulūb","دحية":"Diḥya",
 "عبد الواحد":"ʿAbd al-Wāḥid","عوافة":"ʿAwāfa","عبشمس":"ʿAbd Shams","طارق":"Ṭāriq",
 "خوات":"Khawwāt","فقيم":"Fuqaym","جرول":"Jarwal","لوذان":"Lawdhān","عطارد":"ʿUṭārid",
 "عيص":"ʿĪṣ","منقذ":"Munqidh","جوية":"Juwayya","مروان":"Marwān","يحيى":"Yaḥyā",
 "أبو مالك":"Abū Mālik","حلمة":"Ḥalma","معير":"Muʿayr","حنين":"Ḥunayn","بهدلة":"Bahdala",
 "لاطم":"Lāṭim","هدمة":"Hadma","حراق":"Ḥarrāq","معبر":"Muʿabbir","يسار":"Yasār",
 "معقل":"Maʿqil","شراحيل":"Shurāḥīl","النزال":"al-Nazzāl","عبادة":"ʿUbāda","سريع":"Sarīʿ",
 "عصم":"ʿIṣam","جمان":"Jumān","قنان":"Qunān","جعشم":"Juʿsham","هذمة":"Hadhma",
 "حبشية":"Ḥabashiyya","هجير":"Hujayr","مقرن":"Muqarrin","تور":"Tawr","زبينة":"Zubayna",
 "زياد":"Ziyād","قطن":"Qaṭan","سمي":"Sumayy","الأهتم":"al-Ahtam","الديان":"al-Dayyān",
 "حارثة الغطريف":"Ḥāritha al-Ghiṭrīf","عامر ماء السماء":"ʿĀmir Māʾ al-Samāʾ",
 "عمرو مزيقياء":"ʿAmr Muzayqiyāʾ","عمران الكاهن":"ʿImrān al-Kāhin","سعد العشيرة":"Saʿd al-ʿAshīra",
 "أوس الله":"Aws Allāh","زيد الله":"Zayd Allāh","أنس الله":"Anas Allāh","الأسد":"al-Asd",
 "الأزد":"al-Azd","كهلان":"Kahlān","سبأ":"Sabaʾ","أمامة":"Umāma","سودة":"Sawda",
 "قتيلة":"Qutayla","رملة":"Ramla","ليلى":"Laylā","خالد الأكبر":"Khālid al-Akbar",
 "مالك الأكبر":"Mālik al-Akbar","أبو رهم":"Abū Ruhm","أبو أحيحة":"Abū Uḥayḥa",
 "أبو الأخنس":"Abū al-Akhnas","أبو الواثق":"Abū al-Wāthiq","أبو زهير":"Abū Zuhayr",
 "أبو عمرو":"Abū ʿAmr","أبو حنين":"Abū Ḥunayn","أبو المطاع":"Abū al-Miṭāʿ",
 "أبو البختري":"Abū al-Bakhtarī","نعيم":"Nuʿaym","النحام":"al-Naḥḥām","الأزور":"al-Azwar",
 "جثامة":"Juthāma","العبلات":"al-ʿAbalāt","خلف عبد":"Khalaf",
}
NAMES.update(EXTRA)

# connectives and epithets: they belong to a name without being one, so a name built from
# dictionary words plus these should not be flagged provisional
NAMES.update({
 "بنت":"bt.","بن":"b.","ابن":"b.","أبي":"Abī","أبو":"Abū","أبا":"Abū","أم":"Umm",
 "الأكبر":"al-Akbar","الأصغر":"al-Aṣghar","الشاعر":"al-Shāʿir","الجواد":"al-Jawād",
 "جذل":"Jidhl","الطعان":"al-Ṭiʿān","حبيش":"Ḥubaysh","حثمة":"Ḥathma","الحشر":"al-Ḥashr",
 "ذكوان":"Dhakwān","العزي":"al-ʿUzzā","العاس":"al-ʿĀṣ","غرازة":"Gharāza","شاكر":"Shākir",
 "قحافة":"Quḥāfa","أحيحة":"Uḥayḥa","عرار":"ʿArār","جديلة":"Jadīla","كندي":"Kindī",
 "المختار":"al-Mukhtār","الواثق":"al-Wāthiq","البختري":"al-Bakhtarī","الشداخ":"al-Shaddākh",
})

CONS = {"ا":"a","أ":"a","إ":"i","آ":"ā","ء":"ʾ","ب":"b","ت":"t","ث":"th","ج":"j","ح":"ḥ",
        "خ":"kh","د":"d","ذ":"dh","ر":"r","ز":"z","س":"s","ش":"sh","ص":"ṣ","ض":"ḍ","ط":"ṭ",
        "ظ":"ẓ","ع":"ʿ","غ":"gh","ف":"f","ق":"q","ك":"k","ل":"l","م":"m","ن":"n","ه":"h",
        "ة":"a","و":"ū","ؤ":"ʾ","ي":"ī","ى":"ā","ئ":"ʾ"}
DIA = re.compile(r"[ؐ-ًؚ-ٰٟـ]")


VARIANTS = str.maketrans({"ى":"ي","ٱ":"ا"})


def _look(w):
    """Dictionary hit tolerant of the spellings that vary between printings."""
    for cand in (w, w.translate(VARIANTS),
                 w.replace("أ","ا").replace("إ","ا"),
                 w.translate(VARIANTS).replace("ؤ","ئ"),
                 w.replace("ا","أ", 1)):
        if cand in NAMES:
            return NAMES[cand]
    for k, v in NAMES.items():
        if k.translate(VARIANTS).replace("أ","ا").replace("إ","ا") == \
           w.translate(VARIANTS).replace("أ","ا").replace("إ","ا"):
            return v
    return None


def translit(ar):
    """(latin, is_provisional). Dictionary first; otherwise a consonant skeleton."""
    ar = DIA.sub("", ar).strip()
    hit = _look(ar)
    if hit:
        return hit, False
    bare = ar[2:] if ar.startswith("ال") and ar[2:] in NAMES else None
    if bare:
        return "al-" + NAMES[bare], False
    parts, prov = [], False
    for word in ar.split():
        # look the whole word up FIRST: 'al-Walid' is in the dictionary as one entry, and
        # stripping the article before looking made it miss and fall back to a skeleton
        hw = _look(word)
        if hw:
            parts.append(hw)
            continue
        w, pre = word, ""
        if w.startswith("ال") and len(w) > 2:
            pre, w = "al-", w[2:]
        hw = _look(w)
        if hw:
            parts.append(pre + hw)
            continue
        prov = True
        out = "".join(CONS.get(ch, "") for ch in w)
        parts.append(pre + (out[:1].upper() + out[1:] if out else word))
    return " ".join(parts), prov


def slug(latin):
    s = latin.lower()
    for a, b in (("ā","a"),("ī","i"),("ū","u"),("ḥ","h"),("ḍ","d"),("ṣ","s"),("ṭ","t"),
                 ("ẓ","z"),("ʿ",""),("ʾ",""),("ġ","gh"),("š","sh"),("ḏ","dh"),("ṯ","th")):
        s = s.replace(a, b)
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s or "x"


if __name__ == "__main__":
    for t in ["عمرو","عبد المطلب","الحارث","بلداس","أبو طالب","زهرة"]:
        print(t, "->", translit(t))
