# -*- coding: utf-8 -*-
"""Phase 5 - the Arabs beyond Quraysh: Qahtan, and Adnan's other branches.

Qahtan is seeded as a root, not hung under Sam or Isma'il, because the sources do not agree
where he belongs and Ibn Hazm says outright that nothing above him is sound. Both competing
origins are recorded as claims; neither is made into a tree edge. Once the root exists, the
same walada parser that opened Quraysh opens the whole Yemeni half of the genealogy - which
in turn lets the Phase 4 entry parser anchor the Ansar, who are most of the Sahaba.
"""
import os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ingest, extract_walad, extract_entry

SEED = [
 ("dissent", "IbnHazm",
  "اليمانية كلها راجعة إلى ولد قحطان؛ ولا يصح ما بعد قحطان",
  "the Yemenis all go back to the offspring of Qaḥṭān; and nothing beyond Qaḥṭān is sound",
  {"author_verdict": "Ibn Hazm: the chain above Qahtan is not established",
   "note": "The Yemeni counterpart of the ceiling at Adnan on the Northern side."}),
 ("variant_chain", "Baladhuri",
  "قحطان بن الهميسع بن تيمن بن نبت بن قيذار",
  "Qaḥṭān b. al-Humaysaʿ b. Tayman b. Nabt b. Qaydhār",
  {"isnad_ar": "كان أبى، والشرقى بن القطامي يقولان",
   "isnad_lat": "my father and al-Sharqī b. al-Quṭāmī used to say — Hishām b. al-Kalbī",
   "chain_label": "Qahtan traced to Isma'il through Qaydar"}),
 ("variant_chain", "Baladhuri",
  "هو قحطان ابن هود عليه السلام بن عبد الله بن الخلود بن عاد بن عوص بن إرم بن سام ابن نوح، وهو غير يقطان",
  "he is Qaḥṭān b. Hūd, peace be upon him, b. ʿAbd Allāh b. al-Khulūd b. ʿĀd b. ʿAwṣ b. Iram b. Sām b. Nūḥ — and he is not Yaqṭān",
  {"chain_label": "Qahtan traced to Sam b. Nuh through Hud",
   "note": "Incompatible with the Qaydar chain: the two put Qahtan on different sides of the Arab genealogy."}),
 ("variant_chain", "Baladhuri",
  "فقال بعضهم: قحطان هو يقطان المذكور في التوراة بعينه، إلا أن العرب أعربته فقالت قحطان",
  "some said: Qaḥṭān is the very Yaqṭān named in the Torah, except that the Arabs arabised it and said Qaḥṭān",
  {"chain_label": "Qahtan identified with the biblical Yaqtan"}),
]

# The Qahtani backbone, seeded by hand for the same reason Phase 1 was: without a correct
# spine the parsers anchor onto the wrong man. An earlier run hung al-Aws on a al-Harith b.
# Qahtan because the real path from Qahtan down to the Ansar was not yet in the tree.
# (chain closest-first, work, quote it is cut from)
SPINE = [
 ("مازن بن الأسد ابن الغوث بن نبت بن مالك بن زيد بن كهلان بن سبأ بن يشجب بن يعرب ابن قحطان",
  "IbnHisham",
  "قبائل من ولد مازن بن الأسد ابن الغوث بن نبت بن مالك بن زيد بن كهلان بن سبأ بن يشجب بن يعرب ابن قحطان",
  "tribes of the offspring of Māzin b. al-Asd b. al-Ghawth b. Nabt b. Mālik b. Zayd b. Kahlān b. Sabaʾ b. Yashjub b. Yaʿrub b. Qaḥṭān"),
 ("حارثة بن ثعلبة بن عمرو بن عامر بن حارثة بن أمري القيس بن ثعلبة بن مازن",
  "IbnHisham",
  "والأنصار بنو الأوس والخزرج، ابني حارثة بن ثعلبة بن عمرو بن عامر بن حارثة بن أمري القيس بن ثعلبة بن مازن بن الأسد بن الغوث",
  "the Anṣār are the sons of al-Aws and al-Khazraj, the two sons of Ḥāritha b. Thaʿlaba b. ʿAmr b. ʿĀmir b. Ḥāritha b. Imriʾ al-Qays b. Thaʿlaba b. Māzin b. al-Asd b. al-Ghawth"),
]

ANSAR = ("والأنصار بنو الأوس والخزرج، ابني حارثة بن ثعلبة بن عمرو بن عامر بن حارثة بن أمري القيس بن ثعلبة بن مازن بن الأسد بن الغوث",
         "the Anṣār are the sons of al-Aws and al-Khazraj, the two sons of Ḥāritha b. Thaʿlaba b. ʿAmr b. ʿĀmir …")

TRUNKS = ["p.qahtan", "p.adnan"]
WALAD_WORKS = ["IbnHazm", "IbnKalbi", "Baladhuri", "IbnSad", "IbnHisham"]


def main(write=False):
    st = ingest.Store()
    p0, c0 = len(st.people), len(st.claims)

    if "p.qahtan" not in st.people:
        st.people["p.qahtan"] = {"id": "p.qahtan", "name_ar": "قحطان", "name_lat": "Qaḥṭān",
                                 "sex": "M", "tribe": "Qaḥṭān / the Yemeni Arabs",
                                 "note": "Root of the Yemeni (Qaḥṭānī) Arabs. Left unattached "
                                         "on purpose: the sources give incompatible origins and "
                                         "Ibn Hazm holds that none of them is sound."}
        st.order.append("p.qahtan")
        st._ids.add("p.qahtan")
        st._byname.setdefault("قحطان", []).append("p.qahtan")
    for typ, work, ar, en, extra in SEED:
        st.add(typ, "p.qahtan", ar, en, work=work, **extra)

    # spine first
    import re
    from extract_walad import BN, norm_name
    for chain_s, work, quote, en in SPINE:
        names = [norm_name(x) for x in BN.split(chain_s) if norm_name(x)]
        cur = st.find_by_chain([names[-1]])
        if cur is None:
            print(f"  ! spine anchor {names[-1]} missing")
            continue
        for i in range(len(names) - 2, -1, -1):
            kid = st.person(names[i], father=cur)
            st.add("father_of", cur, quote,
                   f"{names[i]} son of {names[i+1]} — from: {en}", object=kid, work=work,
                   source_pattern="spine")
            cur = kid
    # al-Asd in Ibn Hisham is al-Azd elsewhere; record it so both spellings resolve to one man
    azd = st.find_by_chain(["الأسد", "الغوث", "نبت"])
    if azd:
        st.add("alias", azd, "الأزد بن الغوث بن نبت بن مالك بن زيد بن كهلان بن سبأ",
               "al-Azd b. al-Ghawth b. Nabt b. Mālik b. Zayd b. Kahlān b. Sabaʾ",
               work="IbnHazm", value_ar="الأزد", value_lat="al-Azd")
    har = st.find_by_chain(["حارثة", "ثعلبة", "عمرو", "عامر"])
    if har:
        for nm in ("الأوس", "الخزرج"):
            kid = st.person(nm, father=har)
            st.add("father_of", har, ANSAR[0], f"{nm} son of Ḥāritha — {ANSAR[1]}",
                   object=kid, work="IbnHisham", source_pattern="spine")

    t = time.time()
    for rnd in range(1, 9):
        n = 0
        for trunk in TRUNKS:
            for w in WALAD_WORKS:
                n += extract_walad.run(w, st, quiet=True, under=trunk)
        print(f"== walada round {rnd}: +{n} edges | {len(st.people)} people  [{time.time()-t:.0f}s]")
        if not n:
            break

    for rnd in range(1, 5):
        n = sum(extract_entry.run(w, st) for w in ["IbnAbdAlBarr", "IbnAlAthir"])
        print(f"== entry round {rnd}: {n} attached | {len(st.people)} people  [{time.time()-t:.0f}s]")
        if not n:
            break

    st.report("phase 5")
    print(f"new: {len(st.people)-p0} people, {len(st.claims)-c0} claims")
    if write:
        st.save()
        print("written")
    return st


if __name__ == "__main__":
    main(write="--write" in sys.argv)
