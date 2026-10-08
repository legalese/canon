#!/usr/bin/env python3
"""Generate cpi-il35-published-figures.l4 mechanically from the deposited CBS JSON.

Usage:  gen_published_figures.py [--check]
  (no flag)  write ../cpi-il35-published-figures.l4
  --check    regenerate in memory and diff against the file on disk; exit 1 on any difference.
             Also checks both JSON files against SOURCES.json (sha256, byte count, 320 rows),
             and that the step coefficients below reproduce every cumulative `value` the
             linkage-coefficients file prints (to 1e-9 relative).

Nothing is typed by hand: the readings, the bases and the step factors all come from the JSON.
The step factors are derived from the linkage file and verified against it; a base pair whose
coefficient is not constant across rows stops the run.
"""
import hashlib, json, os, sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "cpi-il35-published-figures.l4")
DATA = os.path.join(HERE, "..", "..", "..", "registers", "source-bundle", "data")
F1 = "cbs-cpi-general-120010-2000-01-to-2026-08.json"
F2 = "cbs-cpi-general-120010-2000-01-to-2026-08-with-linkage-coefficients.json"


def load(name):
    raw = open(os.path.join(DATA, name), "rb").read()
    return raw, json.loads(raw.decode("utf-8"))


def base_year(desc):
    # "2024 ממוצע" -> 2000-style year; "1959 ינואר" / "1951 ספטמבר" are not in this series' own bases
    return int(desc.split()[0])


def numlit(x):
    s = repr(x)
    if s.endswith(".0"):
        s = s[:-2]
    return s


def build():
    raw1, d1 = load(F1)
    raw2, d2 = load(F2)
    src = json.load(open(os.path.join(DATA, "SOURCES.json"), encoding="utf-8"))
    meta = {f["file"]: f for f in src["files"]}
    for name, raw in ((F1, raw1), (F2, raw2)):
        m = meta[name]
        assert hashlib.sha256(raw).hexdigest() == m["sha256"], name + " sha256"
        assert len(raw) == m["bytes"], name + " bytes"
    rows1 = d1["month"][0]["date"]
    rows2 = d2["month"][0]["date"]
    assert len(rows1) == 320 and len(rows2) == 320
    key = lambda r: (r["year"], r["month"])
    assert sorted(map(key, rows1)) == sorted(map(key, rows2))
    assert len(set(map(key, rows1))) == 320
    rows1 = sorted(rows1, key=key)
    r2 = {key(r): r for r in rows2}
    # the two files must agree on every reading
    for r in rows1:
        o = r2[key(r)]
        assert r["currBase"] == o["currBase"] and r["percent"] == o["percent"] and r["percentYear"] == o["percentYear"]
    # complete months, no gaps
    ms = [y * 12 + m - 1 for (y, m) in map(key, rows1)]
    assert ms == list(range(ms[0], ms[0] + 320)), "gap in the series"
    # bases in order of first appearance
    bases = []
    for r in rows1:
        b = base_year(r["currBase"]["baseDesc"])
        if b not in bases:
            bases.append(b)
    assert bases == sorted(bases)
    desc = {}
    for r in rows1:
        desc[base_year(r["currBase"]["baseDesc"])] = r["currBase"]["baseDesc"]
    # step factors: factor[older] converts a reading of the next newer base into base `older`
    factor = {}
    for r in rows2:
        nb = base_year(r["currBase"]["baseDesc"])
        pb = r["prevBase"] or []
        i = bases.index(nb)
        for p in pb:
            ob = base_year(p["baseDesc"])
            if ob in bases and bases.index(ob) < i:
                pass
        # the immediate predecessor in this series
        if i > 0:
            first = [p for p in pb if base_year(p["baseDesc"]) == bases[i - 1]]
            assert len(first) == 1, (key(r), "no link to predecessor base")
            c = first[0]["coeff"]
            assert factor.setdefault(bases[i - 1], c) == c, ("coefficient not constant", bases[i - 1])
    # the other coefficients in prevBase of newer rows must be the same step factors (cumulative values check)
    for r in rows2:
        nb = base_year(r["currBase"]["baseDesc"])
        i = bases.index(nb)
        v = Fraction(str(r["currBase"]["value"]))
        for j in range(i - 1, -1, -1):
            v *= Fraction(str(factor[bases[j]]))
            hit = [p for p in (r["prevBase"] or []) if base_year(p["baseDesc"]) == bases[j]]
            assert len(hit) == 1, (key(r), bases[j])
            assert abs(float(v) - hit[0]["value"]) <= 1e-9 * abs(hit[0]["value"]), (key(r), bases[j], float(v), hit[0]["value"])
            assert hit[0]["coeff"] == factor[bases[j]], (key(r), bases[j], "coefficient")
    assert set(factor) == set(bases[:-1])

    L = []
    w = L.append
    m1 = meta[F1]; m2 = meta[F2]
    w("@lang en")
    w("IMPORT prelude")
    w("IMPORT `cpi-il35-nouns`")
    w("")
    w("-- ===========================================================================")
    w("-- PUBLISHED DATA, NOT LAW. Generated; do not edit by hand.")
    w("-- Regenerate and diff:  python3 tools/gen_published_figures.py --check")
    w("--")
    w("-- The general consumer price index (code 120010, 'מדד המחירים לצרכן - כללי') as the")
    w("-- Central Bureau of Statistics publishes it through its public index API: every month from")
    w("-- January 2000 to August 2026, 320 readings, each in the base in force when it was published.")
    w("-- The Laws that use the index (Income Tax Ordinance s 1 'מדד', s 120B; National Insurance Law")
    w("-- s 1 'מדד', s 334(a)(1)) say only 'the consumer price index the Bureau publishes'; the numbers are the")
    w("-- Bureau's, not the Knesset's, and they are not law.")
    w("--")
    w("-- [cbs-cpi] " + m1["file"])
    w("--   url:        " + m1["url"])
    w("--   retrieved:  " + m1["retrieved_at"] + " (" + m1["retrieved_via"].split(";")[0] + ")")
    w("--   sha256:     " + m1["sha256"] + "   (" + str(m1["bytes"]) + " bytes)")
    w("-- [cbs-cpi-coef] " + m2["file"])
    w("--   url:        " + m2["url"])
    w("--   retrieved:  " + m2["retrieved_at"])
    w("--   sha256:     " + m2["sha256"] + "   (" + str(m2["bytes"]) + " bytes)")
    w("--   Both sit in ../../registers/source-bundle/data/ beside SOURCES.json, which records the above.")
    w("--   The two files give the same 320 readings and percentages; the second adds the Bureau's linkage")
    w("--   coefficients (prevBase), which this module carries as the step factors below.")
    w("--")
    w("-- THE BASES. The Bureau re-bases the index from time to time (the index of the base period is 100).")
    w("-- A reading is published in the base in force that month and is never restated here. In this series:")
    for b in bases:
        n = sum(1 for r in rows1 if base_year(r["currBase"]["baseDesc"]) == b)
        first = [key(r) for r in rows1 if base_year(r["currBase"]["baseDesc"]) == b]
        w("--   base " + str(b) + " ('" + desc[b] + "'): " + str(n) + " readings, %d-%02d to %d-%02d" % (first[0] + first[-1]))
    w("-- Within a base, readings compare directly. Across a change of base they do not, until one is")
    w("-- restated in the other's base: the Bureau's linkage coefficient links the two bases (a reading in the newer")
    w("-- base times the coefficient is the same index in the older base). The coefficients are constant for a")
    w("-- pair of bases across all rows of both files, and the cumulative products reproduce every `value` in")
    w("-- the linkage file (checked by the generator on every run).")
    w("--")
    w("-- WHEN A READING IS PUBLISHED. The Laws speak of 'the index published last before' a day. The files carry no")
    w("-- publication date. SOURCES.json ('latest_reading') records: '" + m1["latest_reading"] + "'. So a month's reading is published in the")
    w("-- following month. That each reading is published after the first and before the last day of the following month")
    w("-- (in practice on the 15th) is ASSUMED, NOT READ from any deposited source; it is the only fact about publication the")
    w("-- encoding uses (NOTES.md, assumption A1).")
    w("-- ===========================================================================")
    w("")
    w("§ `Consumer price index readings published by the Central Bureau of Statistics — published data, not law`")
    w("")
    w("@ref [cbs-cpi] sha256 " + m1["sha256"][:8] + "...; SOURCES.json 'latest_reading'; assumption A1")
    w("`the number of months from the month a reading is of to the month it is published in` MEANS 1")
    w("")
    w("@ref [cbs-cpi] first row, " + "%d-%02d" % key(rows1[0]))
    w("`the first month of the published series` MEANS `A calendar month` WITH `year of the month` IS %d, `number of the month in the year` IS %d" % key(rows1[0]))
    w("")
    w("@ref [cbs-cpi] last row, " + "%d-%02d" % key(rows1[-1]))
    w("`the last month of the published series` MEANS `A calendar month` WITH `year of the month` IS %d, `number of the month in the year` IS %d" % key(rows1[-1]))
    w("")
    w("-- The base years of the series, oldest first.")
    w("@ref [cbs-cpi] currBase.baseDesc of each row")
    w("`the base years of the published series, oldest first` MEANS LIST " + ", ".join(str(b) for b in bases))
    w("")
    w("-- The Bureau's linkage coefficient from the next newer base into the base named: a reading in that next newer")
    w("-- base, times this factor, is the same index in the base named. (A newer base's step to its predecessor.)")
    w("@ref [cbs-cpi-coef] prevBase.coeff; constant across rows (generator-checked)")
    w("GIVEN `the base year` IS A NUMBER")
    w("GIVETH A MAYBE NUMBER")
    w("`the step factor into base` `the base year` MEANS")
    lines = []
    for b in bases[:-1]:
        lines.append("    IF `the base year` EQUALS %d THEN JUST %s  -- %s from %s" % (b, numlit(factor[b]), desc[b], desc[bases[bases.index(b) + 1]]))
    for ln in lines:
        w(ln.replace("    IF ", "    BRANCH IF " if ln is lines[0] else "           IF ", 1))
    w("           OTHERWISE NOTHING")
    w("")
    w("-- THE READINGS, oldest first. Fields: year, month, base year, value, percent published for the month,")
    w("-- percent published for the twelve months. One line per row of [cbs-cpi].")
    w("@ref [cbs-cpi] month[0].date[], all 320 rows")
    w("`the readings the Central Bureau of Statistics published, January 2000 to August 2026` MEANS LIST")
    for i, r in enumerate(rows1):
        b = base_year(r["currBase"]["baseDesc"])
        lead = "    " if i == 0 else "  , "
        w("%s(`A published reading` WITH `the year the reading is of` IS %d, `the month the reading is of` IS %d, `the base year of the reading` IS %d, `the value of the reading` IS %s, `the percent the Bureau published for the month` IS %s, `the percent the Bureau published for the twelve months` IS %s)"
          % (lead, r["year"], r["month"], b, numlit(r["currBase"]["value"]), numlit(r["percent"]), numlit(r["percentYear"])))
    w("")
    return "\n".join(L) + "\n"


def main():
    text = build()
    if "--check" in sys.argv:
        on_disk = open(OUT, encoding="utf-8").read() if os.path.exists(OUT) else ""
        if on_disk != text:
            import difflib
            sys.stdout.writelines(list(difflib.unified_diff(on_disk.splitlines(True), text.splitlines(True), "on disk", "regenerated"))[:60])
            print("gen_published_figures: DIFFERS")
            sys.exit(1)
        print("gen_published_figures: regenerated file is byte-identical to cpi-il35-published-figures.l4; JSON hashes and coefficients verified")
    else:
        open(OUT, "w", encoding="utf-8").write(text)
        print("wrote", OUT)


main()
