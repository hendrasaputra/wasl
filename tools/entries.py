# -*- coding: utf-8 -*-
# SPDX-License-Identifier: GPL-3.0-or-later
# Wasl - a verifiable nasab. Copyright (C) 2026 Hendra Saputra.
"""The biographical entry each Who's who person is read from.

A genealogy gives edges; a life is prose, and these books keep it in a named entry - a
numbered notice in the two sahaba dictionaries, a `dhikr X` chapter in Ibn Sa'd's first
volume for the men who died before Islam. This module locates those entries and nothing
else. What may be SAID about them is Phase 8c; this phase only proves where they are.

Pinned by hand, not matched. An earlier draft resolved entries from recorded aliases and
returned Zayd b. Haritha for Qusayy - whose given name is Zayd - and 'Amr b. al-'As for
Hashim, whose given name is 'Amr. The heading text below is copied out of the corpus and
`validate.py` re-reads it at the page it claims, exactly as it does every Arabic quote.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import nasab

# `### |` NESTS: `### || - dhikr Abd al-Muttalib's vow` belongs to `### | - dhikr Abd
# al-Muttalib`, so an entry runs to the next heading at the same depth or shallower and
# takes its subsections with it.
#
# `### $` does NOT nest. In Usd al-Ghaba `$` heads a man's notice and `$$` a woman's, and
# the women are a block at the END of the book - so reading `$$` as a child of `$` makes the
# last man's entry swallow all 1,351 women. Every `$` heading is depth 1, whatever its
# length, and terminates and is terminated by any other entry or chapter.
HEAD = re.compile(r'^###\s+([|$]+)\s*(?:\(\d+\))?\s*(\d+)?\s*-?\s*(.*)$')
NOISE = re.compile(r'PageV\d{2}P\d+[AB]?|\bms\d+\b|%~%|\[\d+\]')
_cache = {}


def headings(work):
    """[(line_no, depth, heading_text)] for every entry heading in a work."""
    if work in _cache:
        return _cache[work]
    path = os.path.join(nasab.CORPUS, work + '.txt')
    if not os.path.exists(path):
        raise FileNotFoundError(f'{path} missing - run ./fetch.sh')
    lines = open(path, encoding='utf-8').read().split('\n')
    out = []
    for i, ln in enumerate(lines):
        m = HEAD.match(ln)
        if m and m.group(3).strip():
            depth = 1 if set(m.group(1)) == {'$'} else len(m.group(1))
            out.append((i, depth, NOISE.sub(' ', m.group(3)).strip()))
    _cache[work] = (lines, out)
    return _cache[work]


def body(work, line_no, depth):
    """Raw lines of the entry that opens at line_no, up to the next heading of equal or
    shallower depth. A deeper heading is a subsection and stays inside."""
    lines, heads = headings(work)
    end = len(lines)
    for i, d, _ in heads:
        if i > line_no and d <= depth:
            end = i
            break
    return lines[line_no + 1:end]


_marks = {}


def marks(work):
    """[(line_no, vol, page)] for every page milestone, in file order."""
    if work not in _marks:
        lines, _ = headings(work)
        _marks[work] = [(i, int(m.group(1)), int(m.group(2)))
                        for i, ln in enumerate(lines)
                        for m in [nasab.PAGE_RE.search(ln)] if m]
    return _marks[work]


def page_span(work, line_no, depth):
    """(vol, first_page, last_page) for the entry opening at line_no.

    Derived from the milestone positions in the file, NOT by searching for the heading text.
    `locate()` is sound for a claim, whose quote is long and distinctive, and unsound here:
    'Umar b. al-Khattab' as a string occurs on hundreds of pages of Usd al-Ghaba, so
    searching for it returned page 13 and made his 10,748-word entry appear to span 665
    pages. A milestone closes the page it ends, so the first milestone at or after a line is
    the page that line sits on."""
    lines, heads = headings(work)
    stop = next((i for i, d, _ in heads if i > line_no and d <= depth), len(lines))
    ms = marks(work)
    def at(i):
        """The first milestone at or after line i - that is, the page line i sits on."""
        return next((m for m in ms if m[0] >= i), ms[-1])
    a, b = at(line_no), at(max(stop - 1, line_no))
    return a[1], a[2], (b[2] if b[1] == a[1] else a[2])


def find(work, pin):
    """The one entry a pin names, or (None, n) saying how many it matched.

    Pin syntax, because a heading is not always a unique key:
      "prefix"    heading starts with this
      "=exact"    heading IS this, normalised - needed where the wife's notice is headed
                  bare `Hafsa` and four other Hafsas are headed `Hafsa bint ...`
      "...#2"     the 2nd match in document order - Ibn Sa'd files one man once per tabaqa,
                  so 'Anas b. Malik' heads three notices of the same Companion

    Ambiguity returns nothing. `find` quietly taking the longest match is precisely how the
    wrong man gets a biography, and the longest is not even a good guess: in Ibn Sa'd 'Sa'id
    b. Zayd' heads two entries of 1,922 and 113 words and both are him."""
    _, heads = headings(work)
    ordinal, explicit = 1, False
    if '#' in pin:
        pin, _, n = pin.rpartition('#')
        ordinal, explicit = int(n), True
    exact = pin.startswith('=')
    p = nasab.normalise(pin[1:] if exact else pin)
    hits = [(i, d, h) for i, d, h in heads
            if (nasab.normalise(h) == p if exact else nasab.normalise(h).startswith(p))]
    if len(hits) < ordinal:
        return None, len(hits)
    if not explicit and len(hits) > 1:
        return None, len(hits)          # unqualified pin, several matches: say so, do not pick
    return hits[ordinal - 1], 1


def words(raw):
    """Word count of an entry body, with the mARkdown scaffolding stripped out.

    Used as a sanity measure: a printed page holds a few hundred words, so an entry claiming
    thousands per page means the page numbers are wrong even though every quote on them
    verifies. test_wasl.py fails anything over 700.
    """
    return len(NOISE.sub(' ', ' '.join(raw)).replace('#', ' ').replace('~', ' ').split())


# Keyed by the Who's who label in tools/directory.py, so the join is one lookup and the two
# lists cannot drift. Each value is (work, heading prefix) in preference order: the fullest
# life first. A prefix must select exactly ONE heading; `resolve.py --report` fails loudly
# rather than picking.
PINS = {
 "Abū Bakr al-Ṣiddīq":      [("IbnSad","أبو بكر الصديق"),("IbnAlAthir","عبد الله بن عثمان أبو بكر الصديق"),("IbnAbdAlBarr","عبد الله ب أبي قحافة")],
 "ʿUmar b. al-Khaṭṭāb":     [("IbnAlAthir","=عمر بن الخطاب"),("IbnAbdAlBarr","عمر بن الخطاب")],
 "ʿUthmān b. ʿAffān":       [("IbnSad","عثمان بن عفان"),("IbnAlAthir","=عثمان بن عفان"),("IbnAbdAlBarr","عثمان بن عفان")],
 "ʿAlī b. Abī Ṭālib":       [("IbnAlAthir","على بن أبى طالب"),("IbnAbdAlBarr","علي بن أبي طالب رضى الله عنه بن عبد المطلب"),("IbnSad","علي بن أبي طالب#2")],
 "Muḥammad ﷺ":              [("IbnAbdAlBarr","=محمد رسول الله")],
 "Khadīja":                 [("IbnSad","ذكر خديجة بنت خويلد"),("IbnAlAthir","خديجة بنت خويلد"),("IbnAbdAlBarr","خديجة بنت خويلد")],
 "Fāṭima":                  [("IbnAlAthir","فاطمة بنت رسول الله"),("IbnSad","فاطمة بنت رسول الله"),("IbnAbdAlBarr","فاطمة بنت رسول الله")],
 "al-Ḥasan":                [("IbnSad","الحسن بن علي، عليهما السلام"),("IbnAlAthir","الحسن بن على"),("IbnAbdAlBarr","الحسن بن علي")],
 "al-Ḥusayn":               [("IbnSad","الحسين بن علي، رضي الله عنهما"),("IbnAlAthir","الحسين بن على"),("IbnAbdAlBarr","الحسين بن علي")],
 "Ḥamza":                   [("IbnSad","حمزة بن عبد المطلب"),("IbnAlAthir","حمزة بن عبد المطلب"),("IbnAbdAlBarr","حمزة بن عبد المطلب")],
 # Usd al-Ghaba and al-Isti'ab carry only his SONS as headings. Both were searched by name,
 # by chain and by kunya: OpenITI's markup never opens an entry for him, though the printed
 # books certainly do. Reported, not guessed at.
 "al-ʿAbbās":               [("IbnSad","العباس بن عبد المطلب")],
 "Jaʿfar b. Abī Ṭālib":     [("IbnSad","جعفر بن أبي طالب"),("IbnAlAthir","جعفر بن أبى طالب"),("IbnAbdAlBarr","جعفر بن أبي طالب")],
 "Zaynab bt. Muḥammad":     [("IbnSad","زينب بنت رسول الله"),("IbnAlAthir","زينب بنت رسول الله"),("IbnAbdAlBarr","زينب بنت رسول الله")],
 "Ibrāhīm b. Muḥammad":     [("IbnSad","ذكر إبراهيم ابن رسول الله"),("IbnAbdAlBarr","باب حرف الألف إبراهيم بن النبي")],
 "Khadīja bt. Khuwaylid":   [("IbnSad","ذكر خديجة بنت خويلد"),("IbnAlAthir","خديجة بنت خويلد"),("IbnAbdAlBarr","خديجة بنت خويلد")],
 "Sawda bt. Zamʿa":         [("IbnSad","سودة بنت زمعة"),("IbnAlAthir","سودة بنت زمعة"),("IbnAbdAlBarr","سودة بنت زمعة")],
 "ʿĀʾisha bt. Abī Bakr":    [("IbnSad","عائشة زوج النبي"),("IbnAlAthir","عائشة بنت أبى بكر الصديق"),("IbnAbdAlBarr","عائشة بنت أبي بكر")],
 "Ḥafṣa bt. ʿUmar":         [("IbnSad","=حفصة#1"),("IbnAlAthir","حفصة بنت عمر"),("IbnAbdAlBarr","حفصة بنت عمر")],
 "Umm Salama (Hind)":       [("IbnSad","=أم سلمة#1"),("IbnAlAthir","أم سلمة بنت أبي أمية"),("IbnAbdAlBarr","أم سلمة زوج النبي")],
 "Umm Ḥabība (Ramla)":      [("IbnSad","=أم حبيبة"),("IbnAlAthir","رملة بنت أبى سفيان"),("IbnAbdAlBarr","رملة بنت أبي سفيان")],
 "Zaynab bt. Jaḥsh":        [("IbnSad","زينب بنت جحش"),("IbnAlAthir","زينب بنت جحش"),("IbnAbdAlBarr","زينب بنت جحش")],
 "Zaynab bt. Khuzayma":     [("IbnSad","زينب بنت خزيمة"),("IbnAlAthir","زينب بنت خزيمة"),("IbnAbdAlBarr","زينب بنت خزيمة")],
 "Juwayriya bt. al-Ḥārith": [("IbnSad","جويرية بنت الحارث"),("IbnAlAthir","جويرية بنت الحارث"),("IbnAbdAlBarr","جويرية بنت الحارث")],
 "Ṣafiyya bt. Ḥuyayy":      [("IbnSad","صفية بنت حيي"),("IbnAlAthir","صفية بنت حيي"),("IbnAbdAlBarr","صفية بنت حيي")],
 "Rayḥāna bt. Zayd":        [("IbnSad","ريحانة بنت زيد"),("IbnAlAthir","ريحانة")],
 "Maymūna bt. al-Ḥārith":   [("IbnSad","ميمونة بنت الحارث"),("IbnAlAthir","ميمونة بنت الحارث"),("IbnAbdAlBarr","ميمونة بنت الحارث")],
 "Ṭalḥa b. ʿUbayd Allāh":   [("IbnSad","طلحة بن عبيد الله بن عثمان"),("IbnAlAthir","طلحة بن عبيد الله القرشي"),("IbnAbdAlBarr","طلحة بن عبيد الله")],
 "al-Zubayr b. al-ʿAwwām":  [("IbnSad","الزبير بن العوام"),("IbnAlAthir","الزبير بن العوام"),("IbnAbdAlBarr","الزبير بن العوام")],
 "ʿAbd al-Raḥmān b. ʿAwf":  [("IbnSad","=عبد الرحمن بن عوف"),("IbnAlAthir","عبد الرحمن بن عوف"),("IbnAbdAlBarr","عبد الرحمن بن عوف")],
 "Saʿīd b. Zayd":           [("IbnSad","=سعيد بن زيد#1"),("IbnSad","=سعيد بن زيد#2"),("IbnAlAthir","سعيد بن زيد القرشي"),("IbnAbdAlBarr","سعيد بن زيد")],
 "Abū ʿUbayda b. al-Jarrāḥ":[("IbnSad","=أبو عبيدة بن الجراح"),("IbnAlAthir","عامر بن عبد الله بن الجراح"),("IbnAbdAlBarr","عامر بن عبد الله بن الجراح")],
 "Saʿd b. Muʿādh":          [("IbnSad","سعد بن معاذ"),("IbnAlAthir","سعد بن معاذ"),("IbnAbdAlBarr","سعد بن معاذ")],
 "Muʿādh b. Jabal":         [("IbnSad","=معاذ بن جبل"),("IbnAlAthir","معاذ بن جبل"),("IbnAbdAlBarr","معاذ بن جبل")],
 "Ubayy b. Kaʿb":           [("IbnSad","=أبي بن كعب"),("IbnAlAthir","أبى بن كعب بن قيس"),("IbnAbdAlBarr","أبي بن كعب")],
 "Usayd b. Ḥuḍayr":         [("IbnSad","أسيد بن الحضير"),("IbnAlAthir","أسيد بن حضير"),("IbnAbdAlBarr","أسيد بن حضير")],
 "Anas b. Mālik":           [("IbnSad","=أنس بن مالك#1"),("IbnSad","=أنس بن مالك#2"),("IbnAlAthir","أنس بن مالك بن النضر"),("IbnAbdAlBarr","أنس بن مالك بن النضر")],
 # the men above Islam: chapters in Ibn Sa'd's first volume, not notices in a dictionary
 "Ādam":                    [("IbnSad","ذكر حواء")],
 "Nūḥ":                     [("IbnSad","ذكر نوح النبي")],
 "Ibrāhīm (khalīl Allāh)":  [("IbnSad","ذكر إبراهيم خليل")],
 "Ismāʿīl":                 [("IbnSad","ذكر إسماعيل عليه")],
 "ʿAdnān":                  [("IbnSad","ذكر نسب رسول الله")],
 "Quraysh (Fihr)":          [("IbnSad","ذكر نسب رسول الله")],
 "Quṣayy":                  [("IbnSad","ذكر قصي بن كلاب")],
 "Hāshim":                  [("IbnSad","ذكر هاشم بن عبد مناف")],
 "ʿAbd al-Muṭṭalib":        [("IbnSad","ذكر عبد المطلب بن هاشم")],
}
