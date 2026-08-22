# -*- coding: utf-8 -*-
"""The people a reader arrives looking for.

Shared by build.py (which renders the Who's who and resolves each to an id) and by the kunya
pass (which must probe them whether or not the parser happened to flag them as companions).
Kept in one place so the two can never drift apart.
"""

DIRECTORY = [
  ("The four caliphs", [
    ("Abū Bakr al-Ṣiddīq", ["عبد الله","عثمان","عامر","عمرو","كعب"]),
    ("ʿUmar b. al-Khaṭṭāb", ["عمر","الخطاب","نفيل"]),
    ("ʿUthmān b. ʿAffān", ["عثمان","عفان","أبو العاص"]),
    ("ʿAlī b. Abī Ṭālib", ["علي","أبو طالب","عبد المطلب"])]),
  ("The Prophet's household", [
    ("Muḥammad ﷺ", ["محمد","عبد الله","عبد المطلب"]),
    ("Khadīja", ["خديجة","خويلد","أسد"]),
    ("Fāṭima", ["فاطمة","محمد","عبد الله"]),
    ("al-Ḥasan", ["الحسن","علي","أبو طالب"]),
    ("al-Ḥusayn", ["الحسين","علي","أبو طالب"]),
    ("Ḥamza", ["حمزة","عبد المطلب","هاشم"]),
    ("al-ʿAbbās", ["العباس","عبد المطلب","هاشم"]),
    ("Jaʿfar b. Abī Ṭālib", ["جعفر","أبو طالب","عبد المطلب"]),
    ("Zaynab", ["زينب","محمد","عبد الله"]),
    ("Ibrāhīm", ["إبراهيم","محمد","عبد الله"])]),
  ("Among the ten", [
    ("Ṭalḥa b. ʿUbayd Allāh", ["طلحة","عبيد الله","عثمان"]),
    ("al-Zubayr b. al-ʿAwwām", ["الزبير","العوام","خويلد"]),
    ("ʿAbd al-Raḥmān b. ʿAwf", ["عبد الرحمن","عوف","عبد عوف"]),
    ("Saʿīd b. Zayd", ["سعيد","زيد","عمرو","نفيل"]),
    ("Abū ʿUbayda b. al-Jarrāḥ", ["عامر","عبد الله","الجراح"])]),
  ("Anṣār", [
    ("Saʿd b. Muʿādh", ["سعد","معاذ","النعمان"]),
    ("Muʿādh b. Jabal", ["معاذ","جبل","عمرو"]),
    ("Ubayy b. Kaʿb", ["أبي","كعب","قيس","عبيد"]),
    ("Usayd b. Ḥuḍayr", ["أسيد","حضير","سماك"]),
    ("Anas b. Mālik", ["أنس","مالك","النضر"]),
    ("al-Aws", ["الأوس","حارثة","ثعلبة"]),
    ("al-Khazraj", ["الخزرج","حارثة","ثعلبة"])]),
  ("Landmarks of the chain", [
    ("Ādam", ["آدم","__root__"]), ("Nūḥ", ["نوح","لمك"]), ("Ibrāhīm", ["إبراهيم","تارح"]),
    ("Ismāʿīl", ["إسماعيل","إبراهيم"]), ("ʿAdnān", ["عدنان","أدد"]),
    ("Qaḥṭān", ["قحطان"]), ("Quraysh (Fihr)", ["فهر","مالك","النضر"]),
    ("Quṣayy", ["قصي","كلاب","مرة"]), ("Hāshim", ["هاشم","عبد مناف","قصي"]),
    ("ʿAbd al-Muṭṭalib", ["عبد المطلب","هاشم","عبد مناف"])]),
]
