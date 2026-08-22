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
 "جحش":"Jaḥsh","الحارث بن أبي ضرار":"al-Ḥārith b. Abī Ḍirār","حيي":"Ḥuyayy","أخطب":"Akhṭab",
}

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
        w = word
        pre = ""
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
