# -*- coding: utf-8 -*-
# SPDX-License-Identifier: GPL-3.0-or-later
# Wasl - a verifiable nasab. Copyright (C) 2026 Hendra Saputra.
"""Phase 3 - Banu Hashim and the Prophet's household.

Hand-authored, not parsed: 'fa-walada Muhammad b. Abd Allah' names a different man on nearly
every page, so the extractor is right to refuse it and his own children must be taken from the
passages that name him unmistakably. This is also the first phase with women in quantity - the
daughters are in the sources, and they are here.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ingest, extract_walad
from translit import translit

# (father, work, quote, english, [(child_ar, sex, alias_ar)], extra)
FAMILIES = [
 ("p.muhammad", "IbnSad",
  "كان أول من ولد لرسول الله صلى الله عليه وسلم بمكة قبل النبوة القاسم، وبه كان يكنى، ثم ولد له زينب، ثم رقية، ثم فاطمة، ثم أم كلثوم، ثم ولد له في الإسلام عبد الله، فسمي الطيب والطاهر، وأمهم جميعا خديجة بنت خويلد بن أسد بن عبد العزى بن قصي",
  "the first born to the Messenger of God at Mecca before the prophethood was al-Qāsim, and he was named Abū al-Qāsim after him; then Zaynab was born to him, then Ruqayya, then Fāṭima, then Umm Kulthūm; then in Islam ʿAbd Allāh was born to him, who was called al-Ṭayyib and al-Ṭāhir; and the mother of all of them was Khadīja bt. Khuwaylid b. Asad b. ʿAbd al-ʿUzzā b. Quṣayy",
  [("القاسم","M",None),("زينب","F",None),("رقية","F",None),("فاطمة","F",None),
   ("أم كلثوم","F",None),("عبد الله","M","الطيب")],
  {"isnad_ar":"هشام بن محمد بن السائب الكلبي، عن أبيه، عن أبي صالح، عن ابن عباس",
   "isnad_lat":"Hishām b. Muḥammad b. al-Sāʾib al-Kalbī, from his father, from Abū Ṣāliḥ, from Ibn ʿAbbās"}),

 ("p.abd-al-muttalib", "IbnHisham",
  "فولد عبد المطلب بن هاشم عشرة نفر وست نسوة: العباس وحمزة، وعبد الله، وأبا طالب- واسمه عبد مناف- والزبير ، والحارث، وحجلا ، والمقوم، وضرارا، وأبا لهب- واسمه عبد العزى- وصفية، وأم حكيم البيضاء، وعاتكة، وأميمة، وأروى، وبرة",
  "ʿAbd al-Muṭṭalib b. Hāshim begot ten men and six women: al-ʿAbbās and Ḥamza, ʿAbd Allāh, Abū Ṭālib — whose name is ʿAbd Manāf — al-Zubayr, al-Ḥārith, Ḥajl, al-Muqawwim, Ḍirār, Abū Lahab — whose name is ʿAbd al-ʿUzzā — Ṣafiyya, Umm Ḥakīm al-Bayḍāʾ, ʿĀtika, Umayma, Arwā and Barra",
  [("العباس","M",None),("حمزة","M",None),("عبد الله","M",None),("أبو طالب","M","عبد مناف"),
   ("الزبير","M",None),("الحارث","M",None),("حجل","M",None),("المقوم","M",None),
   ("ضرار","M",None),("أبو لهب","M","عبد العزى"),("صفية","F",None),("أم حكيم البيضاء","F",None),
   ("عاتكة","F",None),("أميمة","F",None),("أروى","F",None),("برة","F",None)], {}),

 ("p.abd-al-muttalib", "Baladhuri",
  "فولد عبد المطلب- ويكنى أبا الحارث-: عبد الله، والزبير، وعبد مناف وهو أبو طالب",
  "ʿAbd al-Muṭṭalib — whose kunya is Abū al-Ḥārith — begot ʿAbd Allāh, al-Zubayr, and ʿAbd Manāf, who is Abū Ṭālib",
  [("عبد الله","M",None),("الزبير","M",None)], {}),

 (["أبو طالب","عبد المطلب","هاشم"], "Baladhuri",
  "فولد أبو طالب طالبا- وكان مضعوفا لا عقب له- وعقيلا وجعفرا وعليا",
  "Abū Ṭālib begot Ṭālib — who was weak and left no offspring — ʿAqīl, Jaʿfar and ʿAlī",
  [("طالب","M",None),("عقيل","M",None),("جعفر","M",None),("علي","M",None)],
  {"isnad_lat":"per Hishām b. al-Kalbī, ten years between each of them"}),

 (["علي","أبو طالب","عبد المطلب"], "IbnHazm",
  "وتزوج فاطمة علي بن أبي طالب؛ فولدت له الحسن: والحسين؛ والمحسن مات المحسن صغيرا؛ وزينب؛ وأم كلثوم رضي الله عنهم",
  "ʿAlī b. Abī Ṭālib married Fāṭima, and she bore him al-Ḥasan, al-Ḥusayn and al-Muḥsin — al-Muḥsin died young — and Zaynab and Umm Kulthūm, may God be pleased with them",
  [("الحسن","M",None),("الحسين","M",None),("المحسن","M",None),("زينب","F",None),("أم كلثوم","F",None)],
  {}),
]

# (mother, child, work, quote, english)
# (mother chain, child chain, work, quote, english)
MOTHERS = [
 (["خديجة","خويلد","أسد"], ["القاسم","محمد","عبد الله"], "IbnSad",
  "وأمهم جميعا خديجة بنت خويلد بن أسد بن عبد العزى بن قصي",
  "and the mother of all of them was Khadīja bt. Khuwaylid b. Asad b. ʿAbd al-ʿUzzā b. Quṣayy"),
 (["خديجة","خويلد","أسد"], ["فاطمة","محمد","عبد الله"], "IbnSad",
  "وأمهم جميعا خديجة بنت خويلد بن أسد بن عبد العزى بن قصي",
  "and the mother of all of them was Khadīja bt. Khuwaylid"),
 (["فاطمة","محمد","عبد الله"], ["الحسن","علي","أبو طالب"], "IbnHazm",
  "وتزوج فاطمة علي بن أبي طالب؛ فولدت له الحسن: والحسين",
  "ʿAlī b. Abī Ṭālib married Fāṭima, and she bore him al-Ḥasan and al-Ḥusayn"),
 (["فاطمة","محمد","عبد الله"], ["الحسين","علي","أبو طالب"], "IbnHazm",
  "وتزوج فاطمة علي بن أبي طالب؛ فولدت له الحسن: والحسين",
  "ʿAlī b. Abī Ṭālib married Fāṭima, and she bore him al-Ḥasan and al-Ḥusayn"),
]

# standalone claims: births, aliases, dissent
SINGLE = [
 ("birth",["إبراهيم","محمد","عبد الله"],None,"IbnAbdAlBarr",
  "إبراهيم بن النبي صلى الله عليه وآله وسلم، ولدته أمه مارية القبطية في ذي الحجة سنة ثمان من الهجرة",
  "Ibrāhīm son of the Prophet, God bless him and his family and grant peace: his mother Māriya the Copt bore him in Dhū al-Ḥijja of year eight of the Hijra",
  {"date_basis":"attested","born_ah":8,"born_ad_conventional":630,"month_ar":"ذو الحجة"}),
 ("dissent",["محمد","عبد الله","عبد المطلب"],None,"IbnAbdAlBarr",
  "أولاد رسول الله صلى الله عليه وسلم: القاسم وهو أكبر أولاده، ثم زينب، قال: وقال ابن الكلبي. زينب، ثم القاسم ، ثم أم كلثوم، ثم فاطمة، ثم رقية، ثم عبد الله وكان يقال له الطيب والطاهر. قال: وهذا وهو الصحيح، وغيره تخليط",
  "the children of the Messenger of God: al-Qāsim, who is the eldest of his children, then Zaynab — he said: and Ibn al-Kalbī said, Zaynab then al-Qāsim — then Umm Kulthūm, then Fāṭima, then Ruqayya, then ʿAbd Allāh, who was called al-Ṭayyib and al-Ṭāhir. He said: this is the sound account, and anything else is confusion",
  {"isnad_lat":"ʿAlī b. ʿAbd al-ʿAzīz al-Jurjānī the genealogist",
   "author_verdict":"al-Jurjani: this order is the sound one; Ibn al-Kalbi puts Zaynab first",
   "note":"A different birth order from Ibn Sa'd's, and a disagreement inside the passage itself."}),
]


def main(write=False):
    """Seed the Prophet's household by hand from quoted chains.

    Hand-seeded, like Phase 1, and for the same reason: a parser grows outward from a correct
    backbone but cannot find one. This is the commit the replay pipeline resets to.
    """
    st = ingest.Store()
    p0, c0 = len(st.people), len(st.claims)

    # people the household hangs on, created before the families that need them
    asad = st.find_by_chain(["أسد", "عبد العزى", "قصي"])
    if asad is None:
        raise RuntimeError("required household anchor Asad b. Abd al-Uzza b. Qusayy is missing")
    khuwaylid = st.person("خويلد", father=asad)
    st.add("father_of", asad,
           "خديجة بنت خويلد بن أسد بن عبد العزى بن قصي",
           "Khuwaylid son of Asad b. ʿAbd al-ʿUzzā b. Quṣayy", object=khuwaylid, work="IbnSad")
    kh = st.person("خديجة", father=khuwaylid, sex="F")
    st.add("father_of", khuwaylid, "خديجة بنت خويلد بن أسد بن عبد العزى بن قصي",
           "Khadīja daughter of Khuwaylid", object=kh, work="IbnSad")
    st.people[kh]["id_alias"] = "p.khadija"

    def rid(spec):
        """Accept either a person id or a name chain, and return the id."""
        return spec if isinstance(spec, str) and spec in st.people else st.find_by_chain(spec)

    for father, work, quote, en, kids, extra in FAMILIES:
        fid = rid(father)
        if fid is None:
            raise RuntimeError(f"required household father is missing: {father}")
        for name, sex, alias in kids:
            kid = st.person(name, father=fid, sex=sex, _alias=alias)
            lat = st.people[kid]["name_lat"]
            st.add("father_of", fid, quote,
                   f"{lat} {'daughter' if sex=='F' else 'son'} of {st.people[fid]['name_lat']} — from: {en}",
                   object=kid, work=work, **extra)
            if alias:
                st.add("alias", kid, quote, f"{lat}, whose name is {translit(alias)[0]}",
                       work=work, value_ar=alias, value_lat=translit(alias)[0])

    # Ibrahim's mother is not Khadija, so he is not in the family list above
    mu = rid(["محمد", "عبد الله", "عبد المطلب"])
    ib = st.person("إبراهيم", father=mu)
    st.add("father_of", mu,
           "إبراهيم بن النبي صلى الله عليه وآله وسلم، ولدته أمه مارية القبطية",
           "Ibrāhīm son of the Prophet; his mother Māriya the Copt bore him",
           object=ib, work="IbnAbdAlBarr")
    mar = rid("p.mariya-al-qibtiyya") or st.person("مارية القبطية", sex="F", force=True)
    st.add("mother_of", mar,
           "إبراهيم بن النبي صلى الله عليه وآله وسلم، ولدته أمه مارية القبطية",
           "Māriya the Copt, mother of Ibrāhīm son of the Prophet",
           object=ib, work="IbnAbdAlBarr")

    for m, c, work, q, en in MOTHERS:
        mid, cid = rid(m), rid(c)
        if mid and cid:
            st.add("mother_of", mid, q, en, object=cid, work=work)
        else:
            raise RuntimeError(f"required mother link is unresolved: {m} -> {c}")

    for typ, subj, obj, work, q, en, extra in SINGLE:
        sid = rid(subj)
        if sid:
            st.add(typ, sid, q, en, object=rid(obj) if obj else None, work=work, **extra)
        else:
            raise RuntimeError(f"required household claim subject is unresolved: {subj}")

    # now let the parser widen Banu Hashim from the household it can now see
    for _ in range(4):
        if not sum(extract_walad.run(w, st, quiet=True, under="p.abd-al-muttalib")
                   for w in ["IbnHazm", "IbnKalbi", "Baladhuri", "IbnSad", "IbnHisham"]):
            break
    return st, p0, c0


if __name__ == "__main__":
    st, p0, c0 = main()
    st.report("phase 3")
    print(f"new: {len(st.people)-p0} people, {len(st.claims)-c0} claims")
    if "--write" in sys.argv:
        st.save()
        print("written")
