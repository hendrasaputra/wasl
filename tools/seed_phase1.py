# -*- coding: utf-8 -*-
"""One-shot seed for Phase 1 (Muhammad -> Adam).

Emits people.jsonl and claims.jsonl. Every Arabic string here was copied out of a file in
corpus/ ; the script refuses to emit an edge whose quote it cannot re-find in the corpus, so
running it is itself a verification pass. After the first run the JSONL files are the source
of truth - edit those, not this. Kept in tools/ as a record of how Phase 1 was built.
"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import nasab

SEP = re.compile(r"\s*\b(?:ابن|بن|بنت)\s+")

# ---------------------------------------------------------------- people
# id, arabic, ALA-LC transliteration, sex, extra fields
SPINE = [
 ("p.muhammad","محمد","Muḥammad","M",{"kunya_ar":"أبو القاسم","kunya_lat":"Abū al-Qāsim","laqab_ar":"رسول الله","laqab_lat":"Rasūl Allāh","tribe":"Quraysh / Banū Hāshim","prophet":True}),
 ("p.abd-allah","عبد الله","ʿAbd Allāh","M",{"tribe":"Quraysh / Banū Hāshim"}),
 ("p.abd-al-muttalib","عبد المطلب","ʿAbd al-Muṭṭalib","M",{"kunya_ar":"أبو الحارث","kunya_lat":"Abū al-Ḥārith","tribe":"Quraysh / Banū Hāshim"}),
 ("p.hashim","هاشم","Hāshim","M",{"tribe":"Quraysh / Banū Hāshim","note":"Eponym of Banū Hāshim."}),
 ("p.abd-manaf","عبد مناف","ʿAbd Manāf","M",{"kunya_ar":"أبو عبد شمس","kunya_lat":"Abū ʿAbd Shams","tribe":"Quraysh"}),
 ("p.qusayy","قصي","Quṣayy","M",{"laqab_ar":"مجمع","laqab_lat":"Mujammiʿ","tribe":"Quraysh"}),
 ("p.kilab","كلاب","Kilāb","M",{"tribe":"Quraysh"}),
 ("p.murra","مرة","Murra","M",{"tribe":"Quraysh"}),
 ("p.kab","كعب","Kaʿb","M",{"tribe":"Quraysh"}),
 ("p.luayy","لؤي","Luʾayy","M",{"tribe":"Quraysh"}),
 ("p.ghalib","غالب","Ghālib","M",{"tribe":"Quraysh"}),
 ("p.fihr","فهر","Fihr","M",{"tribe":"Quraysh","note":"Ibn Saʿd: jimāʿ Quraysh - no one above Fihr is called Qurashī."}),
 ("p.malik","مالك","Mālik","M",{"tribe":"Kināna"}),
 ("p.al-nadr","النضر","al-Naḍr","M",{"tribe":"Kināna"}),
 ("p.kinana","كنانة","Kināna","M",{"tribe":"Kināna"}),
 ("p.khuzayma","خزيمة","Khuzayma","M",{"kunya_ar":"أبو الأسد","kunya_lat":"Abū al-Asad"}),
 ("p.mudrika","مدركة","Mudrika","M",{}),
 ("p.ilyas","إلياس","Ilyās","M",{}),
 ("p.mudar","مضر","Muḍar","M",{}),
 ("p.nizar","نزار","Nizār","M",{}),
 ("p.maadd","معد","Maʿadd","M",{}),
 ("p.adnan","عدنان","ʿAdnān","M",{"note":"Ceiling of the attested nasab: several sources stop here."}),
 ("p.udad","أدد","Udad","M",{}),
 ("p.muqawwam","مقوم","Muqawwam","M",{}),
 ("p.nahur-1","ناحور","Nāḥūr","M",{"note":"Distinct from Nāḥūr father of Tāriḥ."}),
 ("p.tayrah","تيرح","Tayraḥ","M",{}),
 ("p.yarub","يعرب","Yaʿrub","M",{}),
 ("p.yashjub","يشجب","Yashjub","M",{}),
 ("p.nabit","نابت","Nābit","M",{}),
 ("p.ismail","إسماعيل","Ismāʿīl","M",{"prophet":True}),
 ("p.ibrahim","إبراهيم","Ibrāhīm","M",{"laqab_ar":"خليل الرحمن","laqab_lat":"Khalīl al-Raḥmān","prophet":True}),
 ("p.tarih","تارح","Tāriḥ","M",{}),
 ("p.nahur-2","ناحور","Nāḥūr","M",{"note":"Distinct from Nāḥūr son of Muqawwam."}),
 ("p.sarugh","ساروغ","Sārūgh","M",{}),
 ("p.rau","راعو","Rāʿū","M",{}),
 ("p.falikh","فالخ","Fālikh","M",{}),
 ("p.aybar","عيبر","ʿAybar","M",{}),
 ("p.shalikh","شالخ","Shālikh","M",{}),
 ("p.arfakhshadh","أرفخشذ","Arfakhshadh","M",{}),
 ("p.sam","سام","Sām","M",{}),
 ("p.nuh","نوح","Nūḥ","M",{"prophet":True}),
 ("p.lamk","لمك","Lamk","M",{}),
 ("p.mattushalakh","متوشلخ","Mattūshalakh","M",{}),
 ("p.akhnukh","أخنوخ","Akhnūkh","M",{"prophet":True,"note":"Identified with the prophet Idrīs."}),
 ("p.yard","يرد","Yard","M",{}),
 ("p.mahlil","مهليل","Mahlīl","M",{}),
 ("p.qaynan","قينن","Qaynan","M",{}),
 ("p.yanish","يانش","Yānish","M",{}),
 ("p.shith","شيث","Shīth","M",{}),
 ("p.adam","آدم","Ādam","M",{"prophet":True,"note":"First man; the root of the chain."}),
]
LAT = {i: l for i, _, l, _, _ in SPINE}

# ---------------------------------------------------------------- chains
# (work, arabic chain verbatim from corpus, [person ids in order son->father])
IDS = [i for i, *_ in SPINE]
CHAINS = [
 ("IbnHisham",
  "محمد بن عبد الله ابن عبد المطلب، واسم عبد المطلب: شيبة بن هاشم، واسم هاشم: عمرو بن عبد مناف، واسم عبد مناف: المغيرة بن قصي، (واسم قصي: زيد) بن كلاب بن مرة بن كعب بن لؤي بن غالب بن فهر بن مالك بن النضر ابن كنانة بن خزيمة بن مدركة، واسم مدركة: عامر بن إلياس بن مضر بن نزار بن معد بن عدنان بن (أد، ويقال) : أدد بن مقوم بن ناحور بن تيرح بن يعرب بن يشجب بن نابت بن إسماعيل بن إبراهيم- خليل الرحمن- بن تارح ، وهو آزر بن ناحور بن ساروغ بن راعو بن فالخ ابن عيبر بن شالخ بن أرفخشذ بن سام بن نوح بن لمك بن متوشلخ ابن أخنوخ، وهو إدريس النبي- فيما يزعمون، والله أعلم، وكان أول بني آدم أعطى النبوة، وخط بالقلم- ابن يرد بن مهليل بن قينن بن يانش بن شيث بن آدم",
  IDS),
 ("IbnSad",
  "محمد الطيب المبارك ابن عبد الله بن عبد المطلب، واسمه شيبة الحمد بن هاشم، واسمه عمرو بن عبد مناف، واسمه المغيرة بن قصي، واسمه زيد بن كلاب بن مرة بن كعب بن لؤي بن غالب بن فهر",
  IDS[:12]),
 ("IbnSad",
  "فهر بن مالك بن النضر، واسمه قيس بن كنانة بن خزيمة بن مدركة، واسمه عمرو بن إلياس بن مضر بن نزار بن معد بن عدنان",
  IDS[11:22]),
 ("IbnAbdAlBarr",
  "محمد بن عبد الله بن عبد المطلب بن هاشم ابن عبد مناف بن قصي بن كلاب بن مرة بن كعب بن لؤي بن غالب بن فهر ابن مالك بن النضر بن كنانة بن خزيمة بن مدركة بن إلياس بن مضر بن نزار بن معد بن عدنان",
  IDS[:22]),
 ("IbnAlAthir",
  "هو محمد بن عبد الله بن عبد المطلب بن هاشم بن عبد مناف بن قصي بن كلاب بن مرة بن كعب ابن لؤي بن غالب بن فهر بن مالك بن النضر بن كنانة بن خزيمة بن مدركة بن إلياس بن مضر بن نزار ابن معد بن عدنان",
  IDS[:22]),
 ("Baladhuri",
  "نوح عليه السلام بن لامك بن متوشلخ بن أخنوخ- وهو إدريس عليه السلام- بن يارد بن مهلائيل بن قينان بن أنوش بن شيث بن آدم",
  IDS[40:]),
 ("IbnHazm",
  "مدركة بن الياس بن مضر بن نزار بن معد بن عدنان",
  IDS[16:22]),
]

# --------------------------------------------------- hand-authored claims
# (type, subject, object, work, arabic, english, extra) - page is resolved from the corpus
EXTRA = [
 # --- aliases / second names, each with its own citation
 ("alias","p.abd-al-muttalib",None,"IbnHisham","واسم عبد المطلب: شيبة",
  "the name of ʿAbd al-Muṭṭalib is Shayba",{"value_ar":"شيبة","value_lat":"Shayba"}),
 ("alias","p.abd-al-muttalib",None,"IbnSad","عبد المطلب، واسمه شيبة الحمد",
  "ʿAbd al-Muṭṭalib, whose name is Shaybat al-Ḥamd",{"value_ar":"شيبة الحمد","value_lat":"Shaybat al-Ḥamd"}),
 ("alias","p.abd-al-muttalib",None,"IbnAbdAlBarr","وأما عبد المطلب فقيل اسمه عامر ولا يصح",
  "as for ʿAbd al-Muṭṭalib, it is said his name was ʿĀmir, but that is not sound",
  {"value_ar":"عامر","value_lat":"ʿĀmir","grade":"dissent","author_verdict":"rejected by Ibn ʿAbd al-Barr"}),
 ("alias","p.hashim",None,"IbnHisham","واسم هاشم: عمرو","the name of Hāshim is ʿAmr",
  {"value_ar":"عمرو","value_lat":"ʿAmr"}),
 ("alias","p.hashim",None,"IbnAbdAlBarr","واسم هاشم عمرو وإنما قيل له هاشم لأنه أول من هشم الثريد لقومه",
  "the name of Hāshim is ʿAmr; he was called Hāshim only because he was the first to crumble bread into broth for his people",
  {"value_ar":"عمرو","value_lat":"ʿAmr"}),
 ("alias","p.abd-manaf",None,"IbnHisham","واسم عبد مناف: المغيرة","the name of ʿAbd Manāf is al-Mughīra",
  {"value_ar":"المغيرة","value_lat":"al-Mughīra"}),
 ("alias","p.qusayy",None,"IbnHisham","واسم قصي: زيد","the name of Quṣayy is Zayd",
  {"value_ar":"زيد","value_lat":"Zayd"}),
 ("alias","p.al-nadr",None,"IbnSad","النضر، واسمه قيس","al-Naḍr, whose name is Qays",
  {"value_ar":"قيس","value_lat":"Qays"}),
 ("alias","p.mudrika",None,"IbnHisham","واسم مدركة: عامر","the name of Mudrika is ʿĀmir",
  {"value_ar":"عامر","value_lat":"ʿĀmir"}),
 ("alias","p.mudrika",None,"IbnSad","مدركة، واسمه عمرو","Mudrika, whose name is ʿAmr",
  {"value_ar":"عمرو","value_lat":"ʿAmr","variant_of":"alias:p.mudrika:IbnHisham"}),
 ("alias","p.mudrika",None,"IbnKalbi","فولد إلياس بن مضر: عمرا وهو مدركة",
  "Ilyās b. Muḍar begot ʿAmr, who is Mudrika",{"value_ar":"عمرو","value_lat":"ʿAmr"}),
 ("alias","p.ibrahim",None,"IbnHisham","إبراهيم- خليل الرحمن-","Ibrāhīm, the Friend of the Merciful",
  {"value_ar":"خليل الرحمن","value_lat":"Khalīl al-Raḥmān"}),
 ("alias","p.tarih",None,"IbnHisham","تارح ، وهو آزر","Tāriḥ, who is Āzar",
  {"value_ar":"آزر","value_lat":"Āzar"}),
 ("alias","p.akhnukh",None,"IbnHisham","أخنوخ، وهو إدريس النبي","Akhnūkh, who is the prophet Idrīs",
  {"value_ar":"إدريس","value_lat":"Idrīs"}),
 ("alias","p.akhnukh",None,"Baladhuri","أخنوخ- وهو إدريس عليه السلام-","Akhnūkh, who is Idrīs, peace be upon him",
  {"value_ar":"إدريس","value_lat":"Idrīs"}),
 ("alias","p.udad",None,"IbnHisham","عدنان بن (أد، ويقال) : أدد","ʿAdnān son of Udd - and it is also said Udad",
  {"value_ar":"أد","value_lat":"Udd","grade":"dissent"}),
 ("alias","p.mudrika",None,"IbnKalbi","فنفرت إبله من أرنب، فخرج إليها عمرو فأدركها، فسمي مدركة",
  "his camels bolted at a hare; ʿAmr went out after them and caught them up (adraka), so he was named Mudrika",
  {"value_ar":"مدركة","value_lat":"Mudrika","kind":"etymology"}),

 # --- how Ibn Hisham received the chain (Ibn Ishaq's own recension lacks it)
 ("isnad","p.muhammad",None,"IbnHisham",
  "قال أبو محمد عبد الملك بن هشام: حدثنا زياد بن عبد الله البكائي، عن محمد بن إسحاق المطلبي بهذا الذي ذكرت من نسب محمد رسول الله صلى الله عليه وآله وسلم إلى آدم عليه السلام",
  "Abū Muḥammad ʿAbd al-Malik b. Hishām said: Ziyād b. ʿAbd Allāh al-Bakkāʾī related to us, from Muḥammad b. Isḥāq al-Muṭṭalibī, this that I have set out of the lineage of Muḥammad the Messenger of God, God bless him and his family and grant peace, up to Ādam, peace be upon him",
  {"note":"The chain above is Ibn Ishaq's, transmitted by al-Bakka'i. Ibn Ishaq's own surviving recension in the corpus (Zakkar's Siyar wa-Maghazi) does not carry it."}),

 # --- dissent: the nasab is only certain as far as Adnan / Maadd
 ("dissent","p.adnan",None,"IbnSad",
  "أن النبي صلى الله عليه وسلم كان إذا انتسب لم يجاوز في نسبه معد بن عدنان بن أدد ثم يمسك، ويقول: كذب النسابون",
  "that when the Prophet, God bless him and grant him peace, traced his lineage he did not go beyond Maʿadd b. ʿAdnān b. Udad, then he would stop and say: the genealogists have lied",
  {"isnad_ar":"هشام بن محمد الكلبي، عن أبيه، عن أبي صالح، عن ابن عباس","isnad_lat":"Hishām b. Muḥammad al-Kalbī, from his father, from Abū Ṣāliḥ, from Ibn ʿAbbās"}),
 ("dissent","p.adnan",None,"IbnKalbi",
  "كان رسول الله صلى الله عليه وسلم إذا انتهى في النسب إلى معد بن عدنان أمسك، ثم قال: كذب الناسبون",
  "when the Messenger of God, God bless him and grant him peace, reached Maʿadd b. ʿAdnān in the lineage he would stop, then say: the genealogists have lied",
  {"isnad_ar":"هشام بن محمد بن السائب، عن أبيه، عن أبى صالح، عن ابن عباس","isnad_lat":"Hishām b. Muḥammad b. al-Sāʾib, from his father, from Abū Ṣāliḥ, from Ibn ʿAbbās"}),
 ("dissent","p.udad",None,"Baladhuri",
  "كان رسول الله صلى الله عليه وسلم إذا بلغ في النسب إلى أدد، قال: كذب النسابون، كذب النسابون",
  "when the Messenger of God, God bless him and grant him peace, reached Udad in the lineage he said: the genealogists have lied, the genealogists have lied",
  {"note":"al-Baladhuri places the stopping point at Udad, one step above Adnan."}),
 ("dissent","p.adnan",None,"IbnSad",
  "فالأمر عندنا على الانتهاء إلى معد بن عدنان، ثم الإمساك عما وراء ذلك إلى إسماعيل بن إبراهيم",
  "so in our view the matter rests on stopping at Maʿadd b. ʿAdnān, and then withholding from what lies beyond that up to Ismāʿīl b. Ibrāhīm",
  {"author_verdict":"Ibn Sa'd's own conclusion"}),
 ("dissent","p.adnan",None,"IbnAbdAlBarr",
  "واختلفوا فيما بين عدنان وإسماعيل بن إبراهيم عليهما السلام، وفيما بين إبراهيم وسام بن نوح بما لم أر لذكره هاهنا وجها",
  "they differed over what lies between ʿAdnān and Ismāʿīl b. Ibrāhīm, peace be upon them both, and over what lies between Ibrāhīm and Sām b. Nūḥ, to a degree in which I saw no point in reporting here",
  {"author_verdict":"Ibn 'Abd al-Barr declines to give the chain above Adnan"}),
 ("dissent","p.adnan",None,"IbnAlAthir",
  "فأما ما بعد عدنان من آبائه إلى إسماعيل بن إبراهيم الخليل صلى الله عليهما وسلم، ففيه اختلاف كثير في العدد والأسماء، لا ينضبط ولا يحصل منه غرض فتركناه لذلك",
  "as for his forefathers beyond ʿAdnān up to Ismāʿīl b. Ibrāhīm the Friend, God bless them both and grant peace, there is much disagreement in it as to number and names; it cannot be pinned down and no purpose is served by it, so we have left it aside",
  {"author_verdict":"Ibn al-Athir declines to give the chain above Adnan"}),
 ("dissent","p.adnan",None,"IbnAbdAlBarr",
  "قال عمر بن الخطاب رضى الله عنه: إنما ننتسب إلى معد، وما بعد معد لا ندري ما هو",
  "ʿUmar b. al-Khaṭṭāb, may God be pleased with him, said: we trace our lineage only as far as Maʿadd; what lies beyond Maʿadd we do not know",
  {"isnad_ar":"أبو الأسود محمد بن عبد الرحمن، عن عروة بن الزبير","isnad_lat":"Abū al-Aswad Muḥammad b. ʿAbd al-Raḥmān, from ʿUrwa b. al-Zubayr"}),
 ("dissent","p.adnan",None,"IbnAbdAlBarr",
  "بين معد بن عدنان إلى إسماعيل ثلاثون أبا",
  "between Maʿadd b. ʿAdnān and Ismāʿīl there are thirty forefathers",
  {"isnad_ar":"خليفة بن خياط عن ابن الكلبي عن أبيه عن أبي صالح عن ابن عباس","isnad_lat":"Khalīfa b. Khayyāṭ from Ibn al-Kalbī from his father from Abū Ṣāliḥ from Ibn ʿAbbās",
   "note":"Thirty generations, against the seven Ibn Hisham names between Ma'add and Isma'il."}),
 ("dissent","p.adnan",None,"IbnSad",
  "بين معد وإسماعيل صلى الله عليه وسلم نيف وثلاثون أبا، وكان لا يسميهم ولا ينفذهم",
  "between Maʿadd and Ismāʿīl, God bless him and grant him peace, there are thirty-odd forefathers, and he would not name them nor run them through",
  {"isnad_ar":"هشام بن محمد، عن أبيه","isnad_lat":"Hishām b. Muḥammad, from his father"}),

 # --- competing chains above Adnan, given in full, each as its own claim
 ("variant_chain","p.adnan",None,"IbnSad",
  "معد بن عدنان بن أدد بن يرى بن أعراق الثرى",
  "Maʿadd b. ʿAdnān b. Udad b. Yarā b. Aʿrāq al-Tharā",
  {"isnad_ar":"كريمة بنت المقداد بن الأسود البهراني، عن النبي صلى الله عليه وسلم","isnad_lat":"Karīma bt. al-Miqdād b. al-Aswad al-Bahrānī, from the Prophet","chain_label":"Ma'add to A'raq al-Thara"}),
 ("variant_chain","p.adnan",None,"IbnSad",
  "معد بن عدنان بن أدد بن الهميسع بن سلامان بن عوص بن يوز بن قموال بن أبي بن العوام بن ناشد بن حزا بن بلداس بن تدلاف بن طابخ بن جاحم بن ناحش بن ماخي بن عبقى بن عبقر بن عبيد بن الدعا بن حمدان بن سنبر بن يثربي بن نحزن بن يلحن بن أرعوي بن عيفى بن ديشان بن عيصر بن أقناد بن أبهام بن مقصي بن ناحث بن زارح بن شمي بن مزى بن عوص بن عرام بن قيذر بن إسماعيل بن إبراهيم",
  "Maʿadd b. ʿAdnān b. Udad b. al-Humaysaʿ b. Salāmān b. ʿAwṣ b. Yawz b. Qamwāl b. Ubayy b. al-ʿAwwām b. Nāshid b. Ḥazā b. Bildās b. Tadlāf b. Ṭābikh b. Jāḥim b. Nāḥish b. Mākhī b. ʿAbqā b. ʿAbqar b. ʿUbayd b. al-Duʿā b. Ḥamdān b. Sanbar b. Yathribī b. Naḥzan b. Yalḥan b. Arʿawī b. ʿĪfā b. Dīshān b. ʿAyṣar b. Aqnād b. Abhām b. Miqṣī b. Nāḥith b. Zāriḥ b. Shammī b. Mazzī b. ʿAwṣ b. ʿIrām b. Qaydhar b. Ismāʿīl b. Ibrāhīm",
  {"isnad_ar":"هشام بن محمد الكلبي، عن أبيه","isnad_lat":"Hishām b. Muḥammad al-Kalbī, from his father","chain_label":"the forty-generation Kalbi chain to Ibrahim",
   "note":"Ibn Sa'd transmits it with the caveat 'wa-akhbarani mukhbir ... wa-lam asma'hu minhu'."}),
 ("variant_chain","p.adnan",None,"IbnSad",
  "معد بن عدنان بن أدد بن زيد بن يقدر بن يقدم بن أمين بن منحر بن صابوح بن الهميسع بن يشجب بن يعرب بن العوام بن نبت بن سلمان بن حمل بن قيذر بن إسماعيل بن إبراهيم",
  "Maʿadd b. ʿAdnān b. Udad b. Zayd b. Yaqdur b. Yaqdum b. Amīn b. Munḥir b. Ṣābūḥ b. al-Humaysaʿ b. Yashjub b. Yaʿrub b. al-ʿAwwām b. Nabt b. Salmān b. Ḥaml b. Qaydhar b. Ismāʿīl b. Ibrāhīm",
  {"isnad_ar":"هشام بن محمد","isnad_lat":"Hishām b. Muḥammad","chain_label":"the eighteen-generation chain to Ibrahim"}),
 ("variant_chain","p.adnan",None,"IbnSad",
  "معد بن عدنان بن مقوم بن ناحور بن تيرح بن يعرب بن يشجب بن نابت بن إسماعيل",
  "Maʿadd b. ʿAdnān b. Muqawwam b. Nāḥūr b. Tayraḥ b. Yaʿrub b. Yashjub b. Nābit b. Ismāʿīl",
  {"isnad_ar":"رويم بن يزيد المقرئ، عن هارون بن أبي عيسى الشآمي، عن محمد بن إسحاق","isnad_lat":"Ruwaym b. Yazīd al-Muqriʾ, from Hārūn b. Abī ʿĪsā al-Shaʾāmī, from Muḥammad b. Isḥāq",
   "chain_label":"Ibn Ishaq's chain as Ibn Sa'd received it",
   "note":"Corroborates the Ibn Hisham spine from Adnan to Isma'il, minus Udad."}),
 ("variant_chain","p.adnan",None,"IbnSad",
  "معد بن عدنان بن أدد بن أيتحب بن أيوب بن قيذر بن إسماعيل بن إبراهيم",
  "Maʿadd b. ʿAdnān b. Udad b. Aytaḥab b. Ayyūb b. Qaydhar b. Ismāʿīl b. Ibrāhīm",
  {"isnad_ar":"محمد بن إسحاق، في رواية أخرى له","isnad_lat":"Muḥammad b. Isḥāq, in another transmission from him",
   "chain_label":"Ibn Ishaq's second chain"}),
 ("variant_chain","p.udad",None,"Baladhuri",
  "فأدد من ولد نابت بن الهميسع بن تيمن بن نبت بن قيدر بن إسماعيل",
  "Udad is of the offspring of Nābit b. al-Humaysaʿ b. Tayman b. Nabt b. Qaydar b. Ismāʿīl",
  {"isnad_ar":"الكلبي","isnad_lat":"al-Kalbī","author_verdict":"وقول الكلبي أثبت - al-Baladhuri: al-Kalbi's account is the better established","chain_label":"al-Kalbi on Udad"}),
 ("variant_chain","p.udad",None,"Baladhuri",
  "وقال بعض المدنيين: أدد من ولد الهميسع بن أشجب بن نبت بن قيدر بن إسماعيل",
  "some of the Medinans said: Udad is of the offspring of al-Humaysaʿ b. Ashjab b. Nabt b. Qaydar b. Ismāʿīl",
  {"author_verdict":"weaker of the two, per al-Baladhuri","chain_label":"the Medinan account of Udad"}),
 ("variant_chain","p.nuh",None,"Baladhuri",
  "هو نوح بن سلكان بن مثوبة بن إدريس عليه السلام بن الزائد بن مهلهل بن قنان بن الطاهر بن هبة الله بن آدم",
  "he is Nūḥ b. Salkān b. Mathūba b. Idrīs, peace be upon him, b. al-Zāʾid b. Muhalhil b. Qinān b. al-Ṭāhir b. Hibat Allāh b. Ādam",
  {"isnad_ar":"وقال بعض أهل المدينة، وزعم أن ذلك عن الزهري","isnad_lat":"some of the people of Medina said it, claiming it from al-Zuhrī",
   "author_verdict":"والأول أثبت وأشهر - al-Baladhuri: the first account is better established and better known",
   "chain_label":"the Medinan / al-Zuhri chain from Nuh to Adam"}),
 ("variant_chain","p.udad",None,"IbnKalbi",
  "ولد أ دد بن زيد: عدنان، ونبتا",
  "Udad b. Zayd begot ʿAdnān and Nabt",
  {"isnad_ar":"هشام، عن أبيه محمد بن السائب","isnad_lat":"Hishām, from his father Muḥammad b. al-Sāʾib",
   "note":"Ibn al-Kalbi gives Udad a father, Zayd, whom the Ibn Hisham chain does not name.",
   "chain_label":"Udad son of Zayd"}),

 # --- dates. These four books date by event, not by year: no ancestor above the
 # Prophet has an attested birth year anywhere in them. Recorded as given.
 ("birth","p.muhammad",None,"IbnSad",
  "ولد رسول الله صلى الله عليه وسلم عام الفيل",
  "the Messenger of God, God bless him and grant him peace, was born in the Year of the Elephant",
  {"date_basis":"attested_relative","event_ar":"عام الفيل","event_lat":"ʿĀm al-Fīl (the Year of the Elephant)",
   "born_ad_conventional":570,"born_ah":-53,
   "note":"The source dates by event only. 570 CE / 53 BH is the conventional modern equation, not a figure in the text."}),
 ("birth","p.muhammad",None,"IbnAbdAlBarr",
  "ولا خلاف أنه ولد عام الفيل",
  "there is no disagreement that he was born in the Year of the Elephant",
  {"date_basis":"attested_relative","event_ar":"عام الفيل","event_lat":"ʿĀm al-Fīl"}),
 ("birth","p.muhammad",None,"IbnAbdAlBarr",
  "وقيل. إنه ولد أول اثنين من ربيع الأول، وقيل: لاثنتي عشرة ليلة خلت منه عام الفيل",
  "it is said he was born on the first Monday of Rabīʿ al-Awwal, and it is said on the twelfth night elapsed of it, in the Year of the Elephant",
  {"date_basis":"attested_relative","event_ar":"ربيع الأول","grade":"dissent",
   "note":"Two readings of the day within the month, both reported."}),
 ("birth","p.muhammad",None,"IbnAbdAlBarr",
  "وقيل: ولد رسول الله صلى الله عليه وآله وسلم بعد قدوم الفيل بشهر. وقيل: بأربعين يوما. وقيل بخمسين",
  "and it is said the Messenger of God, God bless him and his family and grant peace, was born a month after the coming of the Elephant; and it is said forty days; and it is said fifty",
  {"date_basis":"attested_relative","grade":"dissent","note":"Three further readings of the interval."}),
 ("age_at_death","p.muhammad",None,"IbnSad",
  "وتوفي صلوات الله عليه، وهو ابن ثلاث وستين سنة",
  "and he died, God's blessings upon him, at sixty-three years of age",
  {"date_basis":"attested","age_years":63}),

 # --- names of the mother, the one female link Phase 1 can source
 ("mother_of","p.amina","p.muhammad","IbnAbdAlBarr",
  "أم رسول الله صلى الله عليه وآله وسلم آمنة بنت وهب ابن عبد مناف بن زهرة بن كلاب بن مرة، قرشية زهرية",
  "the mother of the Messenger of God, God bless him and his family and grant peace, is Āmina bt. Wahb b. ʿAbd Manāf b. Zuhra b. Kilāb b. Murra, of Quraysh, of Zuhra",{}),
 ("mother_of","p.amina","p.muhammad","IbnAlAthir",
  "وأم رسول الله صلى الله عليه وسلم آمنة بنت وهب بن عبد مناف بن زهرة بن كلاب بن مرة القرشية الزهرية، تجتمع هي وعبد الله الله في كلاب",
  "the mother of the Messenger of God, God bless him and grant him peace, is Āmina bt. Wahb b. ʿAbd Manāf b. Zuhra b. Kilāb b. Murra, of Quraysh, of Zuhra; she and ʿAbd Allāh meet at Kilāb",
  {"text_note":"The printed text repeats 'Allah' (wa-'Abd Allah Allah); read wa-'Abd Allah."}),
 ("mother_of","p.salma","p.abd-al-muttalib","IbnAbdAlBarr",
  "وأمه سلمى بنت زيد، وقبل بنت عمرو بن زيد من بنى عدي بن النجار",
  "his mother is Salmā bt. Zayd - and it is said bt. ʿAmr b. Zayd - of the Banū ʿAdī b. al-Najjār",
  {"text_note":"The printed text has wa-qabla; read wa-qila ('and it is said')."}),
]

EXTRA_PEOPLE = [
 ("p.amina","آمنة","Āmina","F",{"tribe":"Quraysh / Banū Zuhra","note":"Mother of the Prophet. Her own line rejoins the spine at Kilāb."}),
 ("p.salma","سلمى","Salmā","F",{"tribe":"Khazraj / Banū ʿAdī b. al-Najjār","note":"Mother of ʿAbd al-Muṭṭalib."}),
]

# ---------------------------------------------------------------- emit
def tokens(chain):
    out, last = [], 0
    for m in SEP.finditer(chain):
        out.append((last, m.start()))
        last = m.end()
    out.append((last, len(chain)))
    return [(a, b) for a, b in out if chain[a:b].strip(" ،.():")]


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    people, claims, n, fails = [], [], 0, 0

    for pid, ar, lat, sex, extra in SPINE + EXTRA_PEOPLE:
        people.append({"id": pid, "name_ar": ar, "name_lat": lat, "sex": sex, **extra})

    def add(**kw):
        nonlocal n
        n += 1
        claims.append({"cid": f"c{n:05d}", **kw})

    for work, chain, ids in CHAINS:
        span = nasab.locate(work, chain)
        if span is None:
            print(f"FAIL chain not in corpus: {work} {chain[:40]}...", file=sys.stderr)
            fails += 1
            continue
        toks = tokens(chain)
        if len(toks) != len(ids):
            print(f"FAIL {work}: {len(toks)} tokens vs {len(ids)} ids", file=sys.stderr)
            fails += 1
            continue
        # the chain itself, as one quotable statement
        add(type="chain", subject=ids[0], object=ids[-1], work=work,
            vol=span[0], page=span[1], page_end=span[2], ar=chain,
            en=f"Full chain as given: {LAT[ids[0]]} back to {LAT[ids[-1]]}.",
            grade="explicit", n_generations=len(ids))
        for i in range(len(ids) - 1):
            frag = chain[toks[i][0]:toks[i + 1][1]].strip(" ،.")
            fspan = nasab.locate(work, frag)
            if fspan is None:
                print(f"FAIL fragment not in corpus: {work} {frag[:40]}", file=sys.stderr)
                fails += 1
                continue
            add(type="father_of", subject=ids[i + 1], object=ids[i], work=work,
                vol=fspan[0], page=fspan[1], page_end=fspan[2], ar=frag,
                en=f"{LAT[ids[i]]} son of {LAT[ids[i+1]]}", grade="explicit")

    for typ, subj, obj, work, ar, en, extra in EXTRA:
        span = nasab.locate(work, ar)
        if span is None:
            print(f"FAIL extra not in corpus: {work} {ar[:40]}", file=sys.stderr)
            fails += 1
            continue
        add(type=typ, subject=subj, object=obj, work=work, vol=span[0], page=span[1],
            page_end=span[2], ar=ar, en=en, grade=extra.pop("grade", "explicit"), **extra)

    if fails:
        sys.exit(f"\n{fails} failures - nothing written")
    for name, rows in (("people.jsonl", people), ("claims.jsonl", claims)):
        with open(os.path.join(root, name), "w", encoding="utf-8") as f:
            for r in rows:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        print(f"wrote {name}: {len(rows)} rows")


if __name__ == "__main__":
    main()
