#!/usr/bin/env python3
"""Cross-check cpi-il35-tests.l4 against the Bureau's JSON, in Python and independently of any L4.

1. Every assertion of the form  `the value of the reading for` Y `month` M EQUALS V   and
   `the base year of the reading for` Y `month` M EQUALS B   must equal the JSON's reading.
2. Every rise the tests assert (the table below, worked by hand in the test comments) is recomputed here
   from the JSON with exact fractions, and its  a / b  must occur in the test file.
Exit 1 on any disagreement.
"""
import json, os, re, sys
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "..", "..", "registers", "source-bundle", "data")
J = json.load(open(os.path.join(DATA, "cbs-cpi-general-120010-2000-01-to-2026-08.json"), encoding="utf-8"))["month"][0]["date"]
JC = json.load(open(os.path.join(DATA, "cbs-cpi-general-120010-2000-01-to-2026-08-with-linkage-coefficients.json"), encoding="utf-8"))["month"][0]["date"]
R = {(r["year"], r["month"]): r for r in J}
RC = {(r["year"], r["month"]): r for r in JC}
T = open(os.path.join(HERE, "..", "cpi-il35-tests.l4"), encoding="utf-8").read()
bad = 0

n_val = n_base = 0
for m in re.finditer(r"#ASSERT `the value of the reading for` (\d+) `month` (\d+) EQUALS ([0-9.]+)", T):
    y, mo, v = int(m[1]), int(m[2]), m[3]
    if F(v) != F(str(R[(y, mo)]["currBase"]["value"])):
        print("VALUE MISMATCH", y, mo, v, R[(y, mo)]["currBase"]["value"]); bad += 1
    n_val += 1
for m in re.finditer(r"#ASSERT `the base year of the reading for` (\d+) `month` (\d+) EQUALS (\d+)", T):
    y, mo, b = int(m[1]), int(m[2]), int(m[3])
    if b != int(R[(y, mo)]["currBase"]["baseDesc"].split()[0]):
        print("BASE MISMATCH", y, mo, b); bad += 1
    n_base += 1

def v(y, m): return F(str(R[(y, m)]["currBase"]["value"]))
def rise(a, b): return (b - a) / a
def step(vv, coefs):
    for c in coefs: vv *= F(str(c))
    return vv
def ratio(f): return "%d / %d" % (f.numerator, f.denominator)
def neg(f): return "0 MINUS " + ratio(-f)

# (label, expected fraction) recomputed from the JSON; the coefficient is read from the linkage file's prevBase, not typed.
def coef(y, m, base):
    return [p["coeff"] for p in RC[(y, m)]["prevBase"] if int(p["baseDesc"].split()[0]) == base][0]
checks = [
    ("TY2024 same base", rise(v(2023, 11), v(2024, 11))),
    ("TY2022 same base", rise(v(2021, 11), v(2022, 11))),
    ("TY2020 fall", rise(v(2019, 11), v(2020, 11))),
    ("TY2006 fall", rise(v(2005, 11), v(2006, 11))),
    ("TY2004", rise(v(2003, 11), v(2004, 11))),
    ("TY2002", rise(v(2001, 11), v(2002, 11))),
    ("120B(b) Jan", rise(v(2025, 11), v(2025, 12))),
    ("120B(b) Feb", rise(v(2025, 11), v(2026, 1))),
    ("120B(b) Mar", rise(v(2025, 11), v(2026, 2))),
    ("120B(b) Apr", rise(v(2025, 11), v(2026, 3))),
    ("120B(b) Sep", rise(v(2025, 11), v(2026, 8))),
    ("TY2000 Jan 2001", rise(v(2000, 11), v(2000, 12))),
    # across a base change, linked into the older base with the coefficient the linkage file prints for the newer row
    ("NII 2026 L", rise(v(2024, 11), v(2025, 11) * F(str(coef(2025, 11, 2022))))),
    ("TY2023 L", rise(v(2022, 11), v(2023, 11) * F(str(coef(2023, 11, 2020))))),
    ("TY2001 L", rise(v(2000, 11), v(2001, 11) * F(str(coef(2001, 11, 1998))))),
    ("Dec2000->Jan2001 L", rise(v(2000, 12), v(2001, 1) * F(str(coef(2001, 1, 1998))))),
    ("Nov2022->Nov2025 L", rise(v(2022, 11), v(2025, 11) * F(str(coef(2025, 11, 2022))) * F(str(coef(2025, 11, 2020))))),  # two steps: the file lists each step's coefficient
    ("NII 2026 P", F(str(R[(2025, 11)]["percentYear"])) / 100),
    ("TY2023 P", F(str(R[(2023, 11)]["percentYear"])) / 100),
    ("TY2001 P", F(str(R[(2001, 11)]["percentYear"])) / 100),
]
for label, f in checks:
    s = neg(f) if f < 0 else ratio(f)
    if f == 0:
        s = "EQUALS 0"
    pat = (" EQUALS " + s) if f != 0 else "EQUALS 0"
    ok = pat in T
    print("%-22s %-28s %s" % (label, s, "found" if ok else "NOT FOUND IN TESTS"))
    bad += 0 if ok else 1
# the values the linkage file prints for the restated readings (section C)
for (y, mo, base, expect) in [(2025, 11, 2022, F(1112664, 10000)), (2024, 11, 2020, F(1151133, 10000)), (2001, 1, 1998, F(66234, 625))]:
    printed = [p["value"] for p in RC[(y, mo)]["prevBase"] if int(p["baseDesc"].split()[0]) == base][0]
    if abs(float(expect) - printed) > 1e-6:
        print("LINKAGE VALUE MISMATCH", y, mo, base, float(expect), printed); bad += 1

# 3. DATA CONSISTENCY (not an assertion of the tests): for every month that has the same month a year earlier in the series (308 pairs),
#    the rise of the index over the twelve months, taken from the readings restated in the older base with the linkage file's own values,
#    and rounded half-up to one decimal place of a percent, equals the percentYear the Bureau published for that month. This is the evidence that
#    the Bureau's percentage is a rounded rise of the same readings, and that linking is how the Bureau itself compares readings across a base.
import math
def basey(x): return int(x["currBase"]["baseDesc"].split()[0])
def restated(x, base):
    if basey(x) == base:
        return F(str(x["currBase"]["value"]))
    return F(str([q for q in x["prevBase"] if int(q["baseDesc"].split()[0]) == base][0]["value"]))
pairs = mism = cross = 0
for (y, mo), r in sorted(RC.items()):
    o = RC.get((y - 1, mo))
    if not o:
        continue
    base = min(basey(r), basey(o))
    L = (restated(r, base) - restated(o, base)) / restated(o, base) * 100
    pct = F(math.floor(L * 10 + F(1, 2)), 10)
    pairs += 1
    cross += basey(r) != basey(o)
    if pct != F(str(r["percentYear"])):
        mism += 1
        print("PERCENT MISMATCH", y, mo, float(L), r["percentYear"])
print("twelve-month pairs: %d (%d across a change of base); linked rise rounded to 0.1%% differs from the Bureau's percentYear in %d" % (pairs, cross, mism))
bad += mism
print("value assertions checked: %d, base assertions checked: %d, rise checks: %d" % (n_val, n_base, len(checks)))
print("spotcheck:", "OK" if not bad else "%d PROBLEM(S)" % bad)
sys.exit(1 if bad else 0)
