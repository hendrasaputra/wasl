# -*- coding: utf-8 -*-
# SPDX-License-Identifier: GPL-3.0-or-later
# Wasl - a verifiable nasab. Copyright (C) 2026 Hendra Saputra.
"""Hand-written summaries of the pinned biographical entries.

Everything else in this repository is quoted. A summary is not: it is the one place where
prose is composed rather than cited, which makes it the one place a plausible sentence could
pass unchecked. So a summary is not a paragraph here. It is an ordered list of lines, and an
`anchored` line carries the Arabic phrase from its own entry that it rests on. `validate.py`
re-reads that phrase out of the corpus and fails if it is not inside the pages the entry
claims - the same check every claim gets, applied sentence by sentence.

What that proves and what it does not: it proves each statement points at text that exists
where it says. It cannot prove the English is a fair rendering of the Arabic. That is a human
judgement, and Rule 6 is honest about it - the model drafts, the script decides what is real,
the human approves.

The rules the drafting follows:

* ANCHOR FIRST, SENTENCE SECOND. The dangerous failure is writing from memory: these lives
  are well known, and a fluent invented detail would read perfectly and anchor to nothing.
  Pull the phrase, then write to it.
* An `editorial` line rests on nothing quotable and is pure connective tissue. It may carry no
  number and no name, it is counted, and it is capped as a share of the whole.
* WHERE THE ENTRY DISAGREES WITH ITSELF, THE SUMMARY SAYS SO. Rule 3 applied to prose. Ibn
  Sa'd gives Safiyya's death as 50 and, in the same chapter, as 52; Ibn al-Athir reports five
  different counts of who preceded 'Umar into Islam. Smoothing that is editing the source.
* Nothing enters that is not in THIS entry, however well attested elsewhere.
"""

# who -> (work of the entry the summary reads, [(english, arabic anchor or None)])
SUMMARIES = {

 "Ṣafiyya bt. Ḥuyayy": ("IbnSad", [
  ("Ibn Saʿd opens on her descent: of the Children of Israel, of the line of Hārūn b. ʿImrān.",
   "من بني إسرائيل من سبط هارون بن عمران"),
  ("She had been married twice before — to Sallām b. Mishkam, who left her, then to Kināna b. "
   "al-Rabīʿ b. Abī al-Ḥuqayq, killed at Khaybar.",
   "وكانت صفية تزوجها سلام بن مشكم القرظي ثم فارقها، فتزوجها كنانة بن الربيع بن أبي الحقيق النضري فقتل عنها يوم خيبر"),
  ("How she came to the Prophet is told two ways in this one chapter, and neither is set aside.",
   None),
  ("In one she fell to Diḥya al-Kalbī in the division of the spoils,",
   "أن صفية بنت حيي وقعت في سهم دحية الكلبي"),
  ("and the Prophet bought her from him.",
   "فاشتراها رسول الله صلى الله عليه وسلم بسبعة آرس"),
  ("In the other she was simply among what he chose for himself at Khaybar.",
   "فكانت صفية مما اصطفى يوم خيبر"),
  ("He freed her and married her, and made her freedom her dower.",
   "فأعتقها وتزوجها وجعل عتقها مهرها"),
  ("Those present could not tell whether he had married her or taken her as a concubine,",
   "فقال الناس: والله ما ندري أتزوجها رسول الله صلى الله عليه وسلم أم تسرى بها"),
  ("until he veiled her and mounted her behind him — and then they knew.",
   "فلما حملها سترها وأردفها خلفه فعرف الناس أنه قد تزوجها"),
  ("She had dreamt of a moon coming from Yathrib until it fell into her lap.",
   "رأيت في المنام قمرا أقبل من يثرب حتى وقع في حجري"),
  ("Kināna struck her face for telling it, and the mark was still there when the Prophet asked.",
   "فقال: تحبين أن تكوني تحت هذا الملك الذي يأتي من المدينة؟ فضرب وجهي"),
  ("He told her that her father had been among the bitterest of the Jews against him.",
   "لم يزل أبوك من أشد يهود لي عداوة حتى قتله الله"),
  ("She answered him out of the Qurʾān: no bearer of burdens bears the burden of another.",
   "إن الله يقول في كتابه: {ولا تزر وازرة وزر أخرى}"),
  ("He put the choice to her — Islam and himself, or Judaism and her freedom —",
   "اختاري فإن اخترت الإسلام أمسكتك لنفسي وإن اخترت اليهودية فعسى أن أعتقك"),
  ("and she said God and His Messenger were dearer to her than being freed and going back.",
   "فالله ورسوله أحب إلي من العتق وأن أرجع إلى قومي"),
  ("His other wives called her the Jewess.",
   "وأزواج رسول الله صلى الله عليه وسلم ينظرن فقلن: أبعد الله اليهودية"),
  ("When ʿĀʾisha boasted over her, he told her what to answer: my father is Hārūn, my uncle Mūsā.",
   "ألا قلت أبي هارون وعمي موسى؟ وذلك أن عائشة فخرت عليها"),
  ("On one question the chapter contradicts itself outright, and both readings are left standing.",
   None),
  ("ʿAṭāʾ: the Messenger of God did not allot her a turn.",
   "كان رسول الله صلى الله عليه وسلم لا يقسم لصفية بنت حيي"),
  ("al-Zuhrī: she was one of his wives, and he allotted to her as he allotted to them.",
   "كانت صفية من أزواجه، وكان يقسم لها كما يقسم لنسائه"),
  ("She left a third of her estate to her sister's son, a Jew.",
   "أوصت لابن أختها، وهو يهودي بثلثها"),
  ("Her death is given here as the year fifty,",
   "وماتت صفية بنت حيي سنة خمسين في خلافة معاوية بن أبي سفيان"),
  ("and, in the closing line of the same chapter, as fifty-two — buried at al-Baqīʿ.",
   "وتوفيت صفية سنة اثنتين وخمسين في خلافة معاوية بن أبي سفيان وقبرت بالبقيع"),
 ]),

 "ʿUmar b. al-Khaṭṭāb": ("IbnAlAthir", [
  ("Ibn al-Athīr heads the entry with the full line and the kunya Abū Ḥafṣ.",
   "عمر بن الخطاب بن نفيل بن عبد العزي بن رياح بن عبد الله بن قرط بن رزاح ابن عدي بن كعب بن لؤي القرشي العدوي، أبو حفص"),
  ("His mother's name turns on one letter, and the entry sets the quarrel out rather than settling it.",
   None),
  ("Ḥantama daughter of Hāshim b. al-Mughīra —",
   "وأمه حنتمة بنت هاشم [1] بن المغيرة بن عبد الله بن عمر بن مخزوم"),
  ("or of Hishām, which would make her Abū Jahl's sister rather than his cousin.",
   "وقيل: حنتمة بنت هشام بن المغيرة، فعلى هذا تكون أخت أبي جهل، وعلى الأول تكون ابنة عمه"),
  ("Ibn ʿAbd al-Barr calls that reading a mistake;",
   "قال أبو عمر: ومن قال ذلك- يعني بنت هشام- فقد أخطأ"),
  ("Ibn Manda holds it, and makes Abū Jahl his uncle.",
   "وقال ابن منده: أم عمر أخت أبي جهل"),
  ("He was born thirteen years after the Elephant,",
   "ولد بعد الفيل بثلاث عشرة سنة"),
  ("though he reckoned it himself from the Fijār war instead.",
   "روي عن عمر أنه قال: ولدت بعد الفجار الأعظم بأربع سنين"),
  ("Before Islam he was Quraysh's envoy, sent when they had a quarrel to settle.",
   "وكان من أشرف قريش وإليه كانت السفارة في الجاهلية"),
  ("When Muḥammad was sent, ʿUmar was hard on him and on the Muslims.",
   "لما بعث الله محمدا صلى الله عليه وسلم، كان عمر شديدا عليه وعلى المسلمين"),
  ("How many had entered Islam before him is reported several ways on the same page.",
   None),
  ("Hilāl b. Yasāf: after forty men and eleven women.",
   "قال هلال بن يساف: أسلم عمر بعد أربعين رجلا وإحدى عشرة امرأة"),
  ("Or after thirty-nine men and twenty women, he completing the forty.",
   "وقيل: أسلم بعد تسعة وثلاثين رجلا وعشرين امرأة، فكمل الرجال به أربعين رجلا"),
  ("Saʿīd b. al-Musayyab: after forty men and ten women — and once he entered, Islam showed itself in Mecca.",
   "وقال سعيد بن المسيب: أسلم عمر بعد أربعين رجلا وعشر نسوة، فما هو إلا أن أسلم عمر فظهر الإسلام بمكة"),
  ("The Prophet had prayed: strengthen Islam with whichever of the two men You love better, ʿUmar or ʿAmr b. Hishām.",
   "اللهم أعز الإسلام بأحب الرجلين إليك: عمر بن الخطاب أو عمرو بن هشام"),
  ("By his own account he stood behind him in the mosque, heard him open Sūrat al-Ḥāqqa, and marvelled at how the Qurʾān was put together.",
   "فاستفتح سورة «الحاقة» فجعلت أعجب من تأليف القرآن"),
  ("He was the first to carry the whip, the first to gather people for the night prayer in Ramaḍān, the first to be called Commander of the Faithful.",
   "وهو أول من اتخذ الدرة، وأول من جمع الناس على قيام رمضان، وهو أول من سمي «أمير المؤمنين»"),
  ("His colour changed in the Year of Ashes because he forbade himself fat and milk until the people had plenty.",
   "وإنما تغير لونه عام الرمادة [5] لأنه أكثر أكل الزيت، لأنه حرم على نفسه السمن واللبن حتى يخصب الناس"),
  ("He was stabbed on a Wednesday, four nights left of Dhū al-Ḥijja, in the year twenty-three.",
   "طعن عمر يوم الأربعاء لأربع ليال بقين من ذي الحجة، سنة ثلاث وعشرين"),
  ("ʿUthmān b. Muḥammad al-Akhnasī answers flatly that this is a mistake.",
   "وقال عثمان بن محمد الأخنسي [5] : هذا وهم"),
  ("Ibn Qutayba has Abū Luʾluʾa strike him on a Monday; he lingered three days.",
   "وقال ابن قتيبة: ضربه أبو لؤلؤة يوم الأثنين لأربع بقين من ذي الحجة، ومكث ثلاثا، وتوفي"),
  ("He died at sixty-three, or at fifty-five — the entry prefers the first.",
   "وتوفي وهو ابن ثلاث وستين سنة، وقيل: كان عمره خمسا وخمسين سنة، والأول أصح"),
  ("Ṣuhayb prayed over him, and he was buried beside the Prophet and Abū Bakr.",
   "فصلى عليه صهيب، وقبر مع رسول الله صلى الله عليه وسلم وأبى بكر"),
 ]),

 "Quṣayy": ("IbnSad", [
  ("Fāṭima bt. Saʿd bore Kilāb b. Murra a son, Zuhra, and long after him a second, named Zayd.",
   "فولدت فاطمة بنت سعد لكلاب بن مرة زهرة بن كلاب، ثم مكثت دهرا، ثم ولدت قصيا فسمي زيدا"),
  ("Kilāb died, and Rabīʿa b. Ḥarām carried her off to his own country in Syria.",
   "وتوفي كلاب بن مرة، وقدم ربيعة بن حرام بن ضنة بن عبد بن كبير بن عذرة"),
  ("The child went with her, and was called Quṣayy for the distance she took him.",
   "وحملت قصيا معها لصغره وهو يومئذ فطيم، فسمي قصيا لتقصيها به إلى الشام"),
  ("A Quḍāʿī he had beaten at archery told him to go back where he belonged: you are not one of us.",
   "فقال رقيع: ألا تلحق ببلدك وقومك؟ فإنك لست منا"),
  ("His mother told him who his father was, and that his people were at Mecca beside the Sacred House.",
   "أبوك كلاب بن مرة بن كعب بن لؤي بن غالب بن فهر بن مالك بن النضر بن كنانة القرشي، وقومك بمكة عند البيت الحرام"),
  ("At Mecca he married Ḥubbā, daughter of Ḥulayl, who then held the keys of the House.",
   "خطب إلى حليل بن حبشية بن سلول بن كعب بن عمرو بن ربيعة، وهو لحي الخزاعي ابنته حبى"),
  ("How the House passed to him is given three ways, laid side by side without a choice between them.",
   None),
  ("He bought it from Ḥulayl's son for provisions — or, it is said, for a skin of wine.",
   "ثم اشترى منه البيت بأزواد، ويقال: بزق خمر"),
  ("Ḥulayl willed it to him, saying Quṣayy's children were his own daughter's.",
   "فأوصى بولاية البيت والقيام بأمر مكة إلى قصي، وقال: أنت أحق به"),
  ("Or he judged himself more entitled to it than Khuzāʿa and Bakr, and put it to the men of Quraysh.",
   "رأى أنه أولى بالبيت وأمر مكة من خزاعة وبني بكر"),
  ("He wrote to Rizāḥ, his brother by the same mother, to come and fight for him.",
   "وكتب قصي إلى أخيه ابن أمه رزاح بن ربيعة بن حرام العذري يدعوه إلى نصرته"),
  ("The arbitrator gave him the House and the rule of Mecca over Khuzāʿa,",
   "فقضى بينهم بأن قصي بن كلاب أولى بالبيت وأمر مكة من خزاعة"),
  ("and was named the Crusher, for the blood-claims he crushed underfoot.",
   "فسمي يومئذ يعمر الشداخ، لما شدخ من الدماء"),
  ("Quraysh, the entry says, were named that day for gathering to him.",
   "تجمعت إليه قريش، فسميت يومئذ قريشا لحال تجمعها، والتقرش: التجمع"),
  ("A second account in the same chapter derives the name quite differently, from the sons of Fihr.",
   "إنما سموا قريشا؛ لأن بني فهر الثلاثة كان اثنان منهم لأم"),
  ("He built the House of Assembly with its door facing the Kaʿba.",
   "فابتنى دار الندوة، وجعل بابها إلى البيت"),
  ("The doorkeeping, the watering, the provisioning, the war banner, the assembly and the judging of Mecca were all his.",
   "وكانت إليه الحجابة، والسقاية، والرفادة، واللواء، والندوة، وحكم مكة كله"),
  ("They called him the Gatherer for what he had gathered of their affairs.",
   "وسمته مجمعا لما جمع من أمرها"),
  ("All his children were Ḥubbā's: ʿAbd al-Dār his first-born, and ʿAbd Manāf, whose name was al-Mughīra.",
   "ولد لقصي بن كلاب ولده كلهم من حبى بنت حليل: عبد الدار بن قصي، وكان بكره، وعبد مناف بن قصي، واسمه المغيرة"),
  ("He said of them: four sons — two I named for my god, one for my house, one for myself.",
   "كان قصي يقول: ولد لي أربعة رجال، فسميت اثنين بإلهي، وواحدا بداري، وواحدا بنفسي"),
 ]),

}
