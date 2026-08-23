# -*- coding: utf-8 -*-
# SPDX-License-Identifier: GPL-3.0-or-later
# Wasl - a verifiable nasab. Copyright (C) 2026 Hendra Saputra.
"""Seed the Ummahat al-Mu'minin - the wives of the Prophet.

The tree the parsers built is a tree of FATHERS, so it cannot reach a wife: a marriage is not
a parent edge, and no 'fa-walada' line leads to one. Both Ibn Sa'd and Ibn Hisham set the
wives out in a dedicated chapter, each with her full paternal nasab, so this pass is
hand-quoted from those two chapters rather than parsed.

Two things here are deliberate and easy to get wrong:

* Their fathers are mostly NOT in our tree. Quraysh and the Ansar are; Banu Asad b. Khuzayma,
  'Amir b. Sa'sa'a, Khuza'a and the Jewish Banu al-Nadir are not. Where a chain does not
  anchor, its own top name becomes a root - the book states the chain, so the chain is what we
  record. What we must never do is force it: an early draft anchored Safiyya bt. Huyayy on
  'p.al-nadir', which is al-Nadir b. al-Harith of 'Abd al-Dar - a Qurashi - and would have hung
  the Prophet's Jewish wife inside Quraysh off a one-name suffix match.

* The count is genuinely disputed and the books say so in the same breath. Ibn Hisham: nine
  survived him, thirteen in all. Ibn Sa'd reports thirteen (excluding Rayhana), fourteen, and
  fifteen from different informants. Every reading is recorded; none is picked.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ingest, nasab
from extract_walad import BN, norm_name, identifies
from translit import translit

S, H = "IbnSad", "IbnHisham"

# Each wife, in the order Ibn Sa'd gives them (Tabaqat, "dhikr azwaj rasul Allah").
#   chain    - her paternal nasab, verbatim, as the chapter prints it
#   father   - an explicit chain into the tree we already have, when the book names her father
#              by kunya ('bint Abi Bakr al-Siddiq') and no chain match is possible
#   marry    - (work, quote) that states the marriage itself
#   also     - (name_ar, name_lat, quote) when the chapter gives her name behind a kunya
WIVES = [
 dict(chain="خديجة بنت خويلد بن أسد بن عبد العزى بن قصي", work=S,
      marry=(S, "خديجة بنت خويلد بن أسد بن عبد العزى بن قصي، وهي أول امرأة تزوجها"),
      en="Khadīja bt. Khuwaylid, the first woman the Messenger of God married",
      kunya=("أم هند", "Umm Hind", S, "وكانت تكنى أم هند بولدها")),
 dict(chain="سودة بنت زمعة بن قيس بن عبد شمس بن ود بن نصر بن مالك بن حسل بن عامر بن لؤي", work=S,
      marry=(H, "وتزوج رسول الله صلى الله عليه وسلم سودة بنت زمعة بن قيس"),
      en="the Messenger of God married Sawda bt. Zamʿa b. Qays"),
 dict(chain="عائشة بنت أبي بكر الصديق", work=S,
      father=["عبد الله", "عثمان", "عامر", "عمرو", "كعب", "سعد", "تيم", "مرة"],
      marry=(H, "وتزوج رسول الله صلى الله عليه وسلم عائشة بنت أبي بكر الصديق بمكة"),
      en="the Messenger of God married ʿĀʾisha bt. Abī Bakr al-Ṣiddīq at Mecca"),
 dict(chain="حفصة بنت عمر بن الخطاب بن نفيل بن عبد العزى بن رياح بن عبد الله بن قرط بن رزاح بن عدي بن كعب بن لؤي",
      work=S,
      marry=(H, "وتزوج رسول الله صلى الله عليه وسلم حفصة بنت عمر بن الخطاب"),
      en="the Messenger of God married Ḥafṣa bt. ʿUmar b. al-Khaṭṭāb"),
 dict(chain="هند بنت أبي أمية", work=S,
      father=["أبو أمية", "المغيرة", "عبد الله", "عمر", "مخزوم"],
      marry=(H, "وتزوج رسول الله صلى الله عليه وسلم أم سلمة بنت أبي أمية بن المغيرة المخزومية، واسمها هند"),
      en="the Messenger of God married Umm Salama bt. Abī Umayya b. al-Mughīra al-Makhzūmiyya, whose name is Hind",
      kunya=("أم سلمة", "Umm Salama", S, "أم سلمة واسمها هند بنت أبي أمية")),
 dict(chain="رملة بنت أبي سفيان بن حرب بن أمية بن عبد شمس", work=S,
      marry=(H, "وتزوج رسول الله صلى الله عليه وسلم أم حبيبة، واسمها رملة بنت أبي سفيان"),
      en="the Messenger of God married Umm Ḥabība, whose name is Ramla bt. Abī Sufyān",
      kunya=("أم حبيبة", "Umm Ḥabība", S, "أم حبيبة واسمها رملة بنت أبي سفيان بن حرب")),
 dict(chain="زينب بنت جحش بن رياب بن يعمر بن صبرة بن مرة بن كبير بن غنم بن دودان بن أسد بن خزيمة", work=S,
      marry=(H, "وتزوج رسول الله صلى الله عليه وسلم زينب بنت جحش بن رئاب الأسدية"),
      en="the Messenger of God married Zaynab bt. Jaḥsh b. Riʾāb, of Banū Asad"),
 dict(chain="زينب بنت خزيمة بن الحارث بن عبد الله بن عمرو بن عبد مناف بن هلال بن عامر بن صعصعة", work=S,
      marry=(H, "وتزوج رسول الله صلى الله عليه وسلم زينب بنت خزيمة بن الحارث بن عبد الله"),
      en="the Messenger of God married Zaynab bt. Khuzayma b. al-Ḥārith b. ʿAbd Allāh",
      alias=("أم المساكين", "Umm al-Masākīn", S, "وهي أم المساكين كانت تسمى بذلك في الجاهلية")),
 dict(chain="جويرية بنت الحارث بن أبي ضرار بن حبيب بن عائذ بن مالك بن جذيمة", work=S,
      marry=(H, "وتزوج رسول الله صلى الله عليه وسلم جويرية بنت الحارث بن أبي ضرار الخزاعية"),
      en="the Messenger of God married Juwayriya bt. al-Ḥārith b. Abī Ḍirār, of Khuzāʿa"),
 dict(chain="صفية بنت حيي بن أخطب بن سعية بن عامر بن عبيد بن كعب بن الخزرج بن أبي حبيب بن النضير بن النحام بن ينحوم",
      work=S,
      marry=(H, "وتزوج رسول الله صلى الله عليه وسلم صفية بنت حيي بن أخطب، سباها من خيبر"),
      en="the Messenger of God married Ṣafiyya bt. Ḥuyayy b. Akhṭab, taken captive at Khaybar",
      note="of Banū al-Naḍīr, of the Children of Israel, of the line of Hārūn"),
 dict(chain="ريحانة بنت زيد بن عمرو بن خنافة بن شمعون بن زيد", work=S,
      marry=(S, "سباها رسول الله صلى الله عليه وسلم فأعتقها وتزوجها وماتت عنده"),
      en="the Messenger of God took her captive, freed her, married her, and she died with him",
      note="of Banū al-Naḍīr; the lists that count thirteen wives are the lists that leave her out"),
 dict(chain="ميمونة بنت الحارث بن حزن بن بجير بن الهزم بن رويبة بن عبد الله بن هلال بن عامر بن صعصعة", work=S,
      marry=(H, "وتزوج رسول الله صلى الله عليه وسلم ميمونة بنت الحارث بن حزن بن بحير"),
      en="the Messenger of God married Maymūna bt. al-Ḥārith b. Ḥazn b. Buḥayr"),
]

# The books disagree with each other and with themselves, in the same chapter. Rule 3: record
# every reading, resolve none of them.
COUNTS = [
 (H, "قال ابن هشام: وكن تسعا: عائشة بنت أبي بكر، وحفصة بنت عمر بن الخطاب",
  "Ibn Hishām: they were nine - and he names them"),
 (H, "وكان جميع من تزوج رسول الله صلى الله عليه وسلم ثلاث عشرة",
  "all whom the Messenger of God married were thirteen"),
 (S, "تزوج رسول الله صلى الله عليه وسلم ثلاث عشرة امرأة ثم سموا جميع من سمينا في الحديث الأول من أزواج رسول الله صلى الله عليه وسلم إلا ريحانة بنت زيد",
  "he married thirteen women - the same list as before, but without Rayḥāna bt. Zayd"),
 (S, "إنما تزوج رسول الله صلى الله عليه وسلم أربع عشرة امرأة، ست منهن قرشيات لا شك فيهن",
  "he married fourteen women, six of them Qurashī beyond doubt"),
 (S, "تزوج رسول الله صلى الله عليه وسلم خمس عشرة امرأة", "he married fifteen women"),
]


def anchor(st, names, work):
    """Deepest suffix of the chain that already stands in the tree.

    Three names is the floor for a plain match. Below that the corpus decides, not the tree:
    'Asad b. Khuzayma' is continued exactly one way in these books, so it is one man, while a
    bare 'al-Nadir' is several - and the several include a Qurashi who is not this woman's
    ancestor at all."""
    for k in range(len(names) - 1, 0, -1):
        suffix = names[k:]
        if len(suffix) < 3 and not identifies(work, suffix, st):
            continue
        hit = st.find_by_chain(suffix)
        if hit and not st.copied_line(hit):
            return hit, k
    return None, len(names) - 1


def seed(st, w):
    """Put one wife into the tree from her quoted paternal chain, and record the marriage.

    Returns her id, or None if the chain is not in the work or her father cannot be resolved.
    Where the chain anchors on nothing - her tribe is simply not in our tree - its own top
    name becomes a root, which is the honest outcome: the book states the chain, so the chain
    is what we record.
    """
    chain, work = w["chain"], w["work"]
    if nasab.locate(work, chain) is None:
        print(f"  ! chain not in {work}: {chain[:40]}")
        return None
    names = [norm_name(x) for x in BN.split(chain) if norm_name(x)]
    if "father" in w:                       # named by kunya in the book - resolve by hand
        cur = st.find_by_chain(w["father"])
        if cur is None:
            print(f"  ! father not in tree: {' b. '.join(w['father'])}")
            return None
        idx, rooted = 1, False
    else:
        cur, idx = anchor(st, names, work)
        rooted = cur is None
        if rooted:                          # her tribe is not in our tree; the chain is a stem
            cur = st.person(names[-1], force=True)
            idx = len(names) - 1
    for i in range(idx - 1, -1, -1):
        leaf = i == 0
        kid = st.person(names[i], father=cur, sex="F" if leaf else "M",
                        sahabi=True if leaf else None,
                        note=w.get("note") if leaf else None)
        pair = f"{names[i]} {'بنت' if leaf else 'بن'} {names[i+1]}"
        q = pair if nasab.locate(work, pair) else chain
        # name the father as the TREE holds him, not as this line of text spells him. Ibn Sa'd
        # writes 'A'isha bint Abi Bakr al-Siddiq' - a kunya and a title - and transliterating
        # that raw put 'Abu Bakr al-Sdiq' in the gloss for a man the tree already calls
        # 'Abd Allah b. 'Uthman.
        st.add("father_of", cur, q,
               f"{st.people[kid]['name_lat']} {'daughter' if leaf else 'son'} of "
               f"{st.people[cur]['name_lat']}",
               object=kid, work=work, source_pattern="wives")
        cur = kid
    mw, mq = w["marry"]
    st.add("married_to", "p.muhammad", mq, w["en"], object=cur, work=mw, source_pattern="wives")
    for key, typ in (("kunya", "kunya"), ("alias", "alias")):
        if key in w:
            v_ar, v_lat, kw, kq = w[key]
            st.add(typ, cur, kq, f"{'is given the kunya' if key=='kunya' else 'also called'} {v_lat}",
                   work=kw, value_ar=v_ar, value_lat=v_lat, source_pattern="wives")
    print(f"  {'^' if rooted else '+'} {' b. '.join(translit(n)[0] for n in names)}")
    return cur


if __name__ == "__main__":
    st = ingest.Store()
    p0, c0 = len(st.people), len(st.claims)
    got = [seed(st, w) for w in WIVES]
    n_got = sum(1 for g in got if g)
    print(f"\nwives seeded: {n_got}/{len(WIVES)}")
    if n_got != len(WIVES):
        missing = [w["chain"] for w, pid in zip(WIVES, got) if pid is None]
        raise RuntimeError("wives unresolved: " + "; ".join(missing))
    for work, ar, en in COUNTS:
        st.add("dissent", "p.muhammad", ar, en, work=work, source_pattern="wives")
    print(f"new: {len(st.people)-p0} people, {len(st.claims)-c0} claims")
    st.report("phase7")
    if "--write" in sys.argv:
        st.save()
        print("written")
