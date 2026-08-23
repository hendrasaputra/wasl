# SPDX-License-Identifier: GPL-3.0-or-later
# Wasl - a verifiable nasab. Copyright (C) 2026 Hendra Saputra.
"""Shared corpus access: prove that a cited Arabic quote really is on the cited page.

OpenITI mARkdown puts a PageV##P### milestone at the END of the page it closes, so page N's
text runs from page N-1's milestone up to and including N's. Quotes routinely straddle a page
break, so we index the whole work as one normalised string and report the page span a quote
covers; a citation is valid when the page it names falls inside that span.

Three views of the same file, and which one to use matters:

  index(work)   normalised, punctuation stripped, with page positions. For PROVING a quote.
  clean(work)   readable Arabic with punctuation kept. For PARSING - a splitter needs the
                commas. Quotes cut from clean() still verify through locate(), which folds
                punctuation away again.
  page_text()   the text of one page, gathering every segment of a repeated marker.

Everything here caches per work, so the first call pays for the file and the rest are free.

The corpus is fetched, never vendored: corpus/*.txt is gitignored and corpus/SHA256SUMS is
committed, so drift is detectable. If a file is missing the error says to run ./fetch.sh.
"""
import csv, os, re, unicodedata

ROOT = os.path.dirname(os.path.abspath(__file__))
CORPUS = os.path.join(ROOT, "corpus")

# \d{3} truncated every four-digit page: al-Isti'ab runs to 1969 in one sequence, so
# PageV03P1132 was read as page 113 and left a stray "2" in the text. 961 markers in that
# work alone. Page numbers are what a reader checks a citation by, so this was not cosmetic.
PAGE_RE = re.compile(r"PageV(\d{2})P(\d+)[AB]?")
NOISE_RE = re.compile(r"PageV\d{2}P\d+[AB]?|\bms\d+\b|%~%|\[\d+\]")
MARKUP_RE = re.compile(r"</?span\b[^>]*>", re.I)
DIACRITICS = re.compile(r"[ؐ-ًؚ-ٰٟۖ-ۭـ]")


def strip_noise(s):
    """Remove corpus milestones and stray HTML without changing the quoted Arabic."""
    return MARKUP_RE.sub(" ", NOISE_RE.sub(" ", s))


def sources():
    """The pinned works, keyed by the short name a claim cites (`IbnSad`, `IbnHazm`, ...).

    A claim may only cite a key that appears here; validate.py enforces it. Adding a work
    means a new row in sources.tsv with its version URI, URL, editor and edition, and a
    re-run of fetch.sh - see rule 5 in CLAUDE.md.
    """
    with open(os.path.join(ROOT, "sources.tsv"), encoding="utf-8") as f:
        return {r["key"]: r for r in csv.DictReader(f, delimiter="\t")}


def normalise(s):
    """Fold what varies between printings but never between readings."""
    s = unicodedata.normalize("NFKC", s)
    s = DIACRITICS.sub("", s)
    for a, b in (("أ", "ا"), ("إ", "ا"), ("آ", "ا"), ("ٱ", "ا"),
                 ("ة", "ه"), ("ى", "ي"), ("ئ", "ي"), ("ؤ", "و")):
        s = s.replace(a, b)
    s = re.sub(r"[^ء-ي]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


_clean = {}


def clean(work):
    """The work as continuous Arabic with mARkdown scaffolding removed but punctuation kept,
    for parsing. Quotes cut from this still verify through locate(), which folds punctuation."""
    if work in _clean:
        return _clean[work]
    out = []
    with open(os.path.join(CORPUS, work + ".txt"), encoding="utf-8") as f:
        for line in f:
            if line.startswith("#META#"):
                continue
            line = re.sub(r"^###\s*\|+\s*|^#\s*|^~~", " ", line.rstrip("\n"))
            line = strip_noise(line)
            line = re.sub(r"«\d+»|/\s*\d+\s*/", " ", line)
            out.append(line)
    _clean[work] = re.sub(r"[ \t]+", " ", " ".join(out))
    return _clean[work]


_idx = {}


def index(work):
    """(full normalised text, [(char_offset, vol, page)]) for one work."""
    if work in _idx:
        return _idx[work]
    path = os.path.join(CORPUS, work + ".txt")
    if not os.path.exists(path):
        raise FileNotFoundError(f"{path} missing - run ./fetch.sh")
    chunks, marks, buf = [], [], []
    pos = 0
    with open(path, encoding="utf-8") as f:
        for line in f:
            if line.startswith("#META#"):
                continue
            m = PAGE_RE.search(line)
            buf.append(strip_noise(line))
            if m:
                txt = normalise(" ".join(buf))
                if txt:
                    marks.append((pos, int(m.group(1)), int(m.group(2))))
                    chunks.append(txt)
                    pos += len(txt) + 1
                buf = []
    _idx[work] = (" ".join(chunks), marks)
    return _idx[work]


def page_of(work, offset):
    """(volume, page) for a character offset into index(work)'s text.

    Binary search over the milestone table. A milestone CLOSES the page it ends, so the first
    milestone at or after an offset names the page that offset sits on.
    """
    _, marks = index(work)
    lo, hi, out = 0, len(marks) - 1, marks[0][1:]
    while lo <= hi:
        mid = (lo + hi) // 2
        if marks[mid][0] <= offset:
            out, lo = marks[mid][1:], mid + 1
        else:
            hi = mid - 1
    return out


_loc = {}


def locate(work, arabic):
    """Page span a quote covers: (vol, first_page, last_page), or None if absent.

    Finds the FIRST occurrence in the work. That is deliberate and load-bearing elsewhere: a
    phrase common enough to appear earlier resolves to the earlier place, so an anchor that
    is not distinctive enough to sit only in its own entry fails the span check rather than
    passing on the wrong page. See tools/build_summaries.py.

    It also means locate() is unsound for a SHORT string. An entry heading like 'Umar b.
    al-Khattab' occurs on hundreds of pages of Usd al-Ghaba; tools/entries.py derives entry
    spans from milestone positions in the file instead, never from a text search.
    """
    text, _ = index(work)
    needle = normalise(arabic)
    if not needle:
        return None
    ck = (work, needle)
    if ck in _loc:
        return _loc[ck]
    i = text.find(needle)
    if i < 0:
        _loc[ck] = None
        return None
    v1, p1 = page_of(work, i)
    v2, p2 = page_of(work, i + len(needle) - 1)
    _loc[ck] = (v1, p1, p2)
    return _loc[ck]


def page_text(work, vol, page):
    """All text on one page. Some editions repeat a page marker once per report, so a page can
    be several disjoint segments; concatenate them in order."""
    text, marks = index(work)
    out = []
    for n, (off, v, p) in enumerate(marks):
        if (v, p) == (int(vol), int(page)):
            end = marks[n + 1][0] if n + 1 < len(marks) else len(text)
            out.append(text[off:end])
    return " ".join(out)


if __name__ == "__main__":
    import sys
    print(page_text(*sys.argv[1:4]) if len(sys.argv) == 4 else locate(sys.argv[1], sys.argv[2]))
