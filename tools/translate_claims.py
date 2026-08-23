# SPDX-License-Identifier: GPL-3.0-or-later
# Wasl - a verifiable nasab. Copyright (C) 2026 Hendra Saputra.
"""Add Indonesian and Malay glosses to every claim.

The templated ones - 'X son of Y', 'is given the kunya Z' - are REGENERATED from the structured
fields in each language, never translated from the English. A translation of a translation
drifts, and there is no reason to accept that when the underlying fact is a relation between two
named people and every language can state it directly.

The bespoke prose - the objections, the competing chains, the birth notices - is hand-translated
from the Arabic in PROSE below, because those carry argument rather than structure. Anything
without a hand translation keeps the English and is reported, so a gap is visible rather than
silently machine-filled.
"""
import json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path[:0] = [ROOT, os.path.dirname(os.path.abspath(__file__))]
import i18n

# hand translations for the prose claims, keyed by the English gloss
PROSE = {
 "the first born to the Messenger of God at Mecca before the prophethood was al-Qāsim, and he was named Abū al-Qāsim after him; then Zaynab was born to him, then Ruqayya, then Fāṭima, then Umm Kulthūm; then in Islam ʿAbd Allāh was born to him, who was called al-Ṭayyib and al-Ṭāhir; and the mother of all of them was Khadīja bt. Khuwaylid b. Asad b. ʿAbd al-ʿUzzā b. Quṣayy": {
  "id": "yang pertama lahir bagi Rasulullah di Makkah sebelum kenabian adalah al-Qāsim, dan beliau dijuluki Abū al-Qāsim karenanya; kemudian lahir Zaynab, lalu Ruqayya, lalu Fāṭima, lalu Umm Kulthūm; kemudian pada masa Islam lahir ʿAbd Allāh yang disebut al-Ṭayyib dan al-Ṭāhir; dan ibu mereka semua adalah Khadīja binti Khuwaylid bin Asad bin ʿAbd al-ʿUzzā bin Quṣayy",
  "ms": "yang pertama lahir bagi Rasulullah di Makkah sebelum kenabian ialah al-Qāsim, dan baginda digelar Abū al-Qāsim kerananya; kemudian lahir Zaynab, lalu Ruqayya, lalu Fāṭima, lalu Umm Kulthūm; kemudian pada zaman Islam lahir ʿAbd Allāh yang disebut al-Ṭayyib dan al-Ṭāhir; dan ibu mereka semua ialah Khadīja binti Khuwaylid bin Asad bin ʿAbd al-ʿUzzā bin Quṣayy"},
 "that when the Prophet, God bless him and grant him peace, traced his lineage he did not go beyond Maʿadd b. ʿAdnān b. Udad, then he would stop and say: the genealogists have lied": {
  "id": "bahwa Nabi ﷺ apabila menyebut nasabnya tidak melampaui Maʿadd bin ʿAdnān bin Udad, lalu beliau berhenti dan berkata: para ahli nasab telah berdusta",
  "ms": "bahawa Nabi ﷺ apabila menyebut nasabnya tidak melampaui Maʿadd bin ʿAdnān bin Udad, lalu baginda berhenti dan bersabda: para ahli nasab telah berdusta"},
 "when the Messenger of God, God bless him and grant him peace, reached Maʿadd b. ʿAdnān in the lineage he would stop, then say: the genealogists have lied": {
  "id": "apabila Rasulullah ﷺ sampai kepada Maʿadd bin ʿAdnān dalam nasab, beliau berhenti lalu bersabda: para ahli nasab telah berdusta",
  "ms": "apabila Rasulullah ﷺ sampai kepada Maʿadd bin ʿAdnān dalam nasab, baginda berhenti lalu bersabda: para ahli nasab telah berdusta"},
 "when the Messenger of God, God bless him and grant him peace, reached Udad in the lineage he said: the genealogists have lied, the genealogists have lied": {
  "id": "apabila Rasulullah ﷺ sampai kepada Udad dalam nasab, beliau bersabda: para ahli nasab telah berdusta, para ahli nasab telah berdusta",
  "ms": "apabila Rasulullah ﷺ sampai kepada Udad dalam nasab, baginda bersabda: para ahli nasab telah berdusta, para ahli nasab telah berdusta"},
 "so in our view the matter rests on stopping at Maʿadd b. ʿAdnān, and then withholding from what lies beyond that up to Ismāʿīl b. Ibrāhīm": {
  "id": "maka menurut kami perkaranya adalah berhenti pada Maʿadd bin ʿAdnān, lalu menahan diri dari apa yang di baliknya hingga Ismāʿīl bin Ibrāhīm",
  "ms": "maka pada pandangan kami perkaranya ialah berhenti pada Maʿadd bin ʿAdnān, lalu menahan diri daripada apa yang di sebaliknya hingga Ismāʿīl bin Ibrāhīm"},
 "they differed over what lies between ʿAdnān and Ismāʿīl b. Ibrāhīm, peace be upon them both, and over what lies between Ibrāhīm and Sām b. Nūḥ, to a degree in which I saw no point in reporting here": {
  "id": "mereka berselisih tentang apa yang ada antara ʿAdnān dan Ismāʿīl bin Ibrāhīm, dan tentang apa yang ada antara Ibrāhīm dan Sām bin Nūḥ, sedemikian rupa sehingga aku tidak melihat gunanya menyebutkannya di sini",
  "ms": "mereka berselisih tentang apa yang ada antara ʿAdnān dan Ismāʿīl bin Ibrāhīm, dan tentang apa yang ada antara Ibrāhīm dan Sām bin Nūḥ, sedemikian rupa sehingga aku tidak melihat gunanya menyebutnya di sini"},
 "as for his forefathers beyond ʿAdnān up to Ismāʿīl b. Ibrāhīm the Friend, God bless them both and grant peace, there is much disagreement in it as to number and names; it cannot be pinned down and no purpose is served by it, so we have left it aside": {
  "id": "adapun leluhurnya di atas ʿAdnān hingga Ismāʿīl bin Ibrāhīm al-Khalīl, padanya banyak perselisihan dalam jumlah dan nama; tidak dapat dipastikan dan tidak ada gunanya, maka kami meninggalkannya",
  "ms": "adapun nenek moyangnya di atas ʿAdnān hingga Ismāʿīl bin Ibrāhīm al-Khalīl, padanya banyak perselisihan dalam bilangan dan nama; tidak dapat dipastikan dan tiada gunanya, maka kami meninggalkannya"},
 "he died young, not completing two years, during the lifetime of the Prophet, peace be upon him": {
  "id": "beliau wafat masih kecil, belum genap dua tahun, pada masa hidup Nabi ﷺ",
  "ms": "baginda wafat ketika kecil, belum genap dua tahun, pada zaman hidup Nabi ﷺ"},
 "Ibrāhīm died four months before the death of the Prophet, God bless him and grant him peace, and was buried at al-Baqīʿ": {
  "id": "Ibrāhīm wafat empat bulan sebelum wafatnya Nabi ﷺ, dan dimakamkan di al-Baqīʿ",
  "ms": "Ibrāhīm wafat empat bulan sebelum kewafatan Nabi ﷺ, dan dikebumikan di al-Baqīʿ"},
 "and he, peace be upon him, left no surviving male offspring except Ibrāhīm son of the Messenger of God": {
  "id": "dan beliau ﷺ tidak meninggalkan keturunan laki-laki kecuali Ibrāhīm putra Rasulullah",
  "ms": "dan baginda ﷺ tidak meninggalkan keturunan lelaki kecuali Ibrāhīm putera Rasulullah"},
 "the Messenger of God, God bless him and grant him peace, was born in the Year of the Elephant": {
  "id": "Rasulullah ﷺ dilahirkan pada Tahun Gajah",
  "ms": "Rasulullah ﷺ dilahirkan pada Tahun Gajah"},
 "there is no disagreement that he was born in the Year of the Elephant": {
  "id": "tidak ada perselisihan bahwa beliau lahir pada Tahun Gajah",
  "ms": "tiada perselisihan bahawa baginda lahir pada Tahun Gajah"},
 "and he died, God's blessings upon him, at sixty-three years of age": {
  "id": "dan beliau wafat, selawat Allah atasnya, pada usia enam puluh tiga tahun",
  "ms": "dan baginda wafat, selawat Allah ke atasnya, pada usia enam puluh tiga tahun"},
 "the Yemenis all go back to the offspring of Qaḥṭān; and nothing beyond Qaḥṭān is sound": {
  "id": "seluruh orang Yaman kembali kepada keturunan Qaḥṭān; dan tidak ada yang sahih di atas Qaḥṭān",
  "ms": "seluruh orang Yaman kembali kepada keturunan Qaḥṭān; dan tiada yang sahih di atas Qaḥṭān"},
 "ʿUmar b. al-Khaṭṭāb, may God be pleased with him, said: we trace our lineage only as far as Maʿadd; what lies beyond Maʿadd we do not know": {
  "id": "ʿUmar bin al-Khaṭṭāb berkata: kami hanya menasabkan diri sampai Maʿadd; apa yang di balik Maʿadd kami tidak tahu",
  "ms": "ʿUmar bin al-Khaṭṭāb berkata: kami hanya menasabkan diri sehingga Maʿadd; apa yang di sebalik Maʿadd kami tidak tahu"},
 "between Maʿadd b. ʿAdnān and Ismāʿīl there are thirty forefathers": {
  "id": "antara Maʿadd bin ʿAdnān dan Ismāʿīl terdapat tiga puluh leluhur",
  "ms": "antara Maʿadd bin ʿAdnān dan Ismāʿīl terdapat tiga puluh nenek moyang"},
 "between Maʿadd and Ismāʿīl, God bless him and grant him peace, there are thirty-odd forefathers, and he would not name them nor run them through": {
  "id": "antara Maʿadd dan Ismāʿīl terdapat tiga puluh sekian leluhur, dan ia tidak menyebut nama-nama mereka",
  "ms": "antara Maʿadd dan Ismāʿīl terdapat tiga puluh sekian nenek moyang, dan beliau tidak menyebut nama-nama mereka"},
 "it is said he was born on the first Monday of Rabīʿ al-Awwal, and it is said on the twelfth night elapsed of it, in the Year of the Elephant": {
  "id": "dikatakan beliau lahir pada Senin pertama bulan Rabīʿ al-Awwal, dan dikatakan pada malam kedua belas bulan itu, pada Tahun Gajah",
  "ms": "dikatakan baginda lahir pada Isnin pertama bulan Rabīʿ al-Awwal, dan dikatakan pada malam kedua belas bulan itu, pada Tahun Gajah"},
 "and it is said the Messenger of God, God bless him and his family and grant peace, was born a month after the coming of the Elephant; and it is said forty days; and it is said fifty": {
  "id": "dan dikatakan Rasulullah ﷺ lahir sebulan setelah datangnya Gajah; dan dikatakan empat puluh hari; dan dikatakan lima puluh",
  "ms": "dan dikatakan Rasulullah ﷺ lahir sebulan selepas kedatangan Gajah; dan dikatakan empat puluh hari; dan dikatakan lima puluh"},
 "Ibrāhīm son of the Prophet, God bless him and his family and grant peace: his mother Māriya the Copt bore him in Dhū al-Ḥijja of year eight of the Hijra": {
  "id": "Ibrāhīm putra Nabi ﷺ: ibunya Māriya al-Qibṭiyya melahirkannya pada Dzulhijjah tahun kedelapan Hijriah",
  "ms": "Ibrāhīm putera Nabi ﷺ: ibunya Māriya al-Qibṭiyya melahirkannya pada Zulhijjah tahun kelapan Hijrah"},
 "the children of the Messenger of God: al-Qāsim, who is the eldest of his children, then Zaynab — he said: and Ibn al-Kalbī said, Zaynab then al-Qāsim — then Umm Kulthūm, then Fāṭima, then Ruqayya, then ʿAbd Allāh, who was called al-Ṭayyib and al-Ṭāhir. He said: this is the sound account, and anything else is confusion": {
  "id": "anak-anak Rasulullah: al-Qāsim yang tertua, lalu Zaynab — ia berkata: dan Ibnu al-Kalbī berkata, Zaynab lalu al-Qāsim — lalu Umm Kulthūm, lalu Fāṭima, lalu Ruqayya, lalu ʿAbd Allāh yang disebut al-Ṭayyib dan al-Ṭāhir. Ia berkata: inilah yang sahih, selainnya kacau",
  "ms": "anak-anak Rasulullah: al-Qāsim yang tertua, lalu Zaynab — katanya: dan Ibnu al-Kalbī berkata, Zaynab lalu al-Qāsim — lalu Umm Kulthūm, lalu Fāṭima, lalu Ruqayya, lalu ʿAbd Allāh yang disebut al-Ṭayyib dan al-Ṭāhir. Katanya: inilah yang sahih, selainnya kacau"},
 "Abū Muḥammad ʿAbd al-Malik b. Hishām said: Ziyād b. ʿAbd Allāh al-Bakkāʾī related to us, from Muḥammad b. Isḥāq al-Muṭṭalibī, this that I have set out of the lineage of Muḥammad the Messenger of God, God bless him and his family and grant peace, up to Ādam, peace be upon him": {
  "id": "Abū Muḥammad ʿAbd al-Malik bin Hishām berkata: Ziyād bin ʿAbd Allāh al-Bakkāʾī meriwayatkan kepada kami, dari Muḥammad bin Isḥāq al-Muṭṭalibī, apa yang telah aku sebutkan dari nasab Muhammad Rasulullah ﷺ hingga Ādam",
  "ms": "Abū Muḥammad ʿAbd al-Malik bin Hishām berkata: Ziyād bin ʿAbd Allāh al-Bakkāʾī meriwayatkan kepada kami, daripada Muḥammad bin Isḥāq al-Muṭṭalibī, apa yang telah aku sebutkan daripada nasab Muhammad Rasulullah ﷺ hingga Ādam"},
 "Udad is of the offspring of Nābit b. al-Humaysaʿ b. Tayman b. Nabt b. Qaydar b. Ismāʿīl": {
  "id": "Udad termasuk keturunan Nābit bin al-Humaysaʿ bin Tayman bin Nabt bin Qaydar bin Ismāʿīl",
  "ms": "Udad termasuk keturunan Nābit bin al-Humaysaʿ bin Tayman bin Nabt bin Qaydar bin Ismāʿīl"},
 "some of the Medinans said: Udad is of the offspring of al-Humaysaʿ b. Ashjab b. Nabt b. Qaydar b. Ismāʿīl": {
  "id": "sebagian penduduk Madinah berkata: Udad termasuk keturunan al-Humaysaʿ bin Ashjab bin Nabt bin Qaydar bin Ismāʿīl",
  "ms": "sebahagian penduduk Madinah berkata: Udad termasuk keturunan al-Humaysaʿ bin Ashjab bin Nabt bin Qaydar bin Ismāʿīl"},
 "Udad b. Zayd begot ʿAdnān and Nabt": {
  "id": "Udad bin Zayd melahirkan ʿAdnān dan Nabt",
  "ms": "Udad bin Zayd melahirkan ʿAdnān dan Nabt"},
 "he is Qaḥṭān b. Hūd, peace be upon him, b. ʿAbd Allāh b. al-Khulūd b. ʿĀd b. ʿAwṣ b. Iram b. Sām b. Nūḥ — and he is not Yaqṭān": {
  "id": "dia adalah Qaḥṭān bin Hūd bin ʿAbd Allāh bin al-Khulūd bin ʿĀd bin ʿAwṣ bin Iram bin Sām bin Nūḥ — dan dia bukan Yaqṭān",
  "ms": "dia ialah Qaḥṭān bin Hūd bin ʿAbd Allāh bin al-Khulūd bin ʿĀd bin ʿAwṣ bin Iram bin Sām bin Nūḥ — dan dia bukan Yaqṭān"},
 "some said: Qaḥṭān is the very Yaqṭān named in the Torah, except that the Arabs arabised it and said Qaḥṭān": {
  "id": "sebagian berkata: Qaḥṭān adalah Yaqṭān yang disebut dalam Taurat, hanya saja orang Arab mengarabkannya menjadi Qaḥṭān",
  "ms": "sebahagian berkata: Qaḥṭān ialah Yaqṭān yang disebut dalam Taurat, cuma orang Arab mengarabkannya menjadi Qaḥṭān"},
 "he is Nūḥ b. Salkān b. Mathūba b. Idrīs, peace be upon him, b. al-Zāʾid b. Muhalhil b. Qinān b. al-Ṭāhir b. Hibat Allāh b. Ādam": {
  "id": "dia adalah Nūḥ bin Salkān bin Mathūba bin Idrīs bin al-Zāʾid bin Muhalhil bin Qinān bin al-Ṭāhir bin Hibat Allāh bin Ādam",
  "ms": "dia ialah Nūḥ bin Salkān bin Mathūba bin Idrīs bin al-Zāʾid bin Muhalhil bin Qinān bin al-Ṭāhir bin Hibat Allāh bin Ādam"},
}

# A gloss that is only a chain of names needs no translating, only the connector: 'b.' is
# written 'bin' in both Indonesian and Malay.
# a segment may be more than one word - 'A'raq al-Thara' is a single name
_SEG = r"[^\s]+(?: (?!b\. )[^\s]+)*"
CHAIN_ONLY = re.compile(rf"^{_SEG}(?: b\. {_SEG})+$")


def chain_gloss(en):
    return en.replace(" b. ", " bin ") if CHAIN_ONLY.match(en.strip()) else None


def main(write=False):
    path = f"{ROOT}/claims.jsonl"
    rows = [json.loads(l) for l in open(path, encoding="utf-8") if l.strip()]
    people = {json.loads(l)["id"]: json.loads(l)
              for l in open(f"{ROOT}/people.jsonl", encoding="utf-8") if l.strip()}
    made = {"id": 0, "ms": 0}
    missing = 0
    for c in rows:
        for lang in ("id", "ms"):
            g = None
            subj = people.get(c["subject"], {})
            obj = people.get(c.get("object"), {}) if c.get("object") else {}
            if c["type"] == "father_of" and obj:
                kind = "daughter_of" if obj.get("sex") == "F" else "son_of"
                g = i18n.gloss(kind, lang, a=obj["name_lat"], b=subj.get("name_lat", ""))
            elif c["type"] == "mother_of" and obj:
                g = i18n.gloss("mother_of", lang, a=subj.get("name_lat", ""), b=obj["name_lat"])
            elif c["type"] == "kunya" and c.get("value_lat"):
                g = i18n.gloss("kunya", lang, k=c["value_lat"])
            elif c["type"] == "alias" and c.get("value_lat"):
                g = i18n.gloss("alias", lang, a=subj.get("name_lat", ""), k=c["value_lat"])
            elif c["type"] == "chain":
                m = re.match(r"Full chain as given: (.+?) back to (.+?)\.", c["en"])
                if m:
                    g = i18n.gloss("chain", lang, a=m.group(1), b=m.group(2))
            if g is None:
                hit = PROSE.get(c["en"].strip())
                g = hit[lang] if hit else chain_gloss(c["en"])
            if g:
                c[lang] = g
                made[lang] += 1
    for c in rows:
        if "id" not in c:
            missing += 1
    print(f"glossed: id={made['id']} ms={made['ms']} of {len(rows)} claims")
    print(f"still English-only: {missing}"
          + ("  (prose without a hand translation - they keep the English)" if missing else ""))
    if write:
        with open(path, "w", encoding="utf-8") as f:
            for c in rows:
                f.write(json.dumps(c, ensure_ascii=False) + "\n")
        print("written")


if __name__ == "__main__":
    main(write="--write" in sys.argv)
