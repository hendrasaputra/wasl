#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Small regressions for parser failures that previously reached the dataset."""
import re
import sys
import tempfile

sys.path.insert(0, "tools")
import extract_entry
import extract_kunya
import extract_walad
import ingest
import nasab
import phase7_wives
import validate


assert nasab.strip_noise("أمية </span>بن خلف PageV03P1132") == "أمية  بن خلف  "
assert extract_entry.chain_of(nasab.strip_noise(
    "أمية </span>بن خلف بن وهب PageV03P1132")) == ["أمية", "خلف", "وهب"]
assert extract_entry.chain_of("مالك بن ابن حسل بن عامر") == ["مالك", "حسل", "عامر"]
assert extract_entry.chain_of("معاذ بن ما عض بن قيس") == ["معاذ", "ماعض", "قيس"]
assert extract_entry.chain_of("خالد بن مدلج أبي الحشر بن خالد") == ["خالد", "مدلج", "خالد"]
assert extract_entry.chain_of("بنت صفوان بن أمية") == []
assert extract_entry.chain_of(
    "عباد بن الأبجر- والأبجر هو خدرة بن عوف") == ["عباد", "الأبجر", "عوف"]
assert extract_entry.chain_of(
    "عمارة بن أبي معيط بن أبى عمرو- ذكوان- ابن أمية") == \
       ["عمارة", "أبو معيط", "أبو عمرو", "أمية"]
usd = ("### $ 3786- علي بن عبيد الله بن الحارث\n# علي بن عبيد الله بن الحارث\n# بن رحضة\n"
       "### $ 3787- مروان بن الجدع\n# مروان بن الجذع")
assert list(extract_entry.entries("IbnAlAthir", usd)) == \
       [" علي بن عبيد الله بن الحارث # بن رحضة ", " مروان بن الجذع"]
assert extract_walad.children("IbnHazm", "خالد، سيف الله، عمارة") == [("خالد", None)]
assert extract_walad.children(
    "IbnHazm", "خالد؛ وهو صاحب القصة؛ سليمان") == [("خالد", None)]
assert extract_walad.children(
    "IbnHazm", "خالد، فولد خالد: سليمان، عبد الله") == [("خالد", None)]
assert extract_walad.children("IbnHazm", "ابن، خالد") == []
assert extract_walad.children("IbnHazm", "كلدة درج، محمد بنو جعفر") == \
       [("كلدة", None), ("محمد", None)]
assert extract_walad.children("Baladhuri", "مات في أول خلافة، الحكم") == []
assert re.search(r"تكنى\s+" + extract_kunya.quote_stem("أم سليم"), "تكنى أم سليم")

store = ingest.Store()
assert store.person("لفظاختباري") is None
pid = store.person("لفظاختباري", force=True)
assert pid and store.people[pid]["name_ar"] == "لفظاختباري"

fake = type("FakeStore", (), {})()
fake.people = {str(i): {"name_ar": name} for i, name in enumerate("ابجدابجد", 1)}
fake.claims = [{"type": "father_of", "subject": str(i + 1), "object": str(i)}
               for i in range(1, 8)]
fake.copied_line = ingest.Store.copied_line.__get__(fake)
assert fake.copied_line("1")

with tempfile.NamedTemporaryFile("w", encoding="utf-8") as f:
    f.write('{"ok": true}\nnot json\n[]\n')
    f.flush()
    errors = []
    rows = validate.jsonl(f.name, errors)
assert rows == [{"ok": True}] and len(errors) == 2

print("20 parser and validation checks passed.")
