"""Shared corpus access: prove that a cited Arabic quote really is on the cited page.

OpenITI mARkdown puts a PageV##P### milestone at the END of the page it closes, so page N's
text runs from page N-1's milestone up to and including N's. Quotes routinely straddle a page
break, so we index the whole work as one normalised string and report the page span a quote
covers; a citation is valid when the page it names falls inside that span.
"""
import csv, os, re, unicodedata

ROOT = os.path.dirname(os.path.abspath(__file__))
CORPUS = os.path.join(ROOT, "corpus")

PAGE_RE = re.compile(r"PageV(\d{2})P(\d{3})[AB]?")
NOISE_RE = re.compile(r"PageV\d{2}P\d{3}[AB]?|\bms\d+\b|%~%|\[\d+\]")
DIACRITICS = re.compile(r"[ؐ-ًؚ-ٰٟۖ-ۭـ]")


def sources():
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
            buf.append(NOISE_RE.sub(" ", line))
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
    _, marks = index(work)
    lo, hi, out = 0, len(marks) - 1, marks[0][1:]
    while lo <= hi:
        mid = (lo + hi) // 2
        if marks[mid][0] <= offset:
            out, lo = marks[mid][1:], mid + 1
        else:
            hi = mid - 1
    return out


def locate(work, arabic):
    """Page span a quote covers: (vol, first_page, last_page), or None if absent."""
    text, _ = index(work)
    needle = normalise(arabic)
    if not needle:
        return None
    i = text.find(needle)
    if i < 0:
        return None
    v1, p1 = page_of(work, i)
    v2, p2 = page_of(work, i + len(needle) - 1)
    return (v1, p1, p2) if v1 == v2 else (v1, p1, p2)


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
