#!/usr/bin/env python3
"""Generate the Annex I (Phụ lục I) premium tests from the raw source text.

  python3 -I tools/annex1.py ../../source/raw/nd67-congbao-1017-1018.txt

Run from the encoding directory. Writes nd67-annex1-tests.l4: for every row of Annex I section
A, one #ASSERT per vehicle the row covers (both edges of every band), and one per special case
of section VII, whose expected premium is the percentage the raw text prints times the figure
of the row it names. Every figure and percentage is read from the raw text here, not from the
L4 module, so a mistyped constant in nd67-art8-premium.l4 fails a test. Prints the answer table
NOTES.md §5 copies. Reads the raw text as data; never executes it.
"""
import os
import re
import sys
from fractions import Fraction

FIRST, LAST = 2050, 2127
ROW = re.compile(r"^\s*(\d+|[IVX]+)\s+(.*?)\s{2,}(\d{1,3}(?:\.\d{3})+)\s*$")
HEAD = re.compile(r"^\s*([IVX]+)\s+(\S.*?)\s*$")


def vnd(s):
    return int(s.replace(".", ""))


def parse(raw):
    rows, sec = {}, None
    for n in range(FIRST, LAST + 1):
        t = raw[n - 1]
        m = ROW.match(t)
        if m:
            tt, label, fig = m.group(1), m.group(2).strip(), vnd(m.group(3))
            if re.fullmatch(r"[IVX]+", tt):
                sec = tt
                rows[(sec, "")] = (n, label, fig)
            else:
                rows[(sec, tt)] = (n, label, fig)
            continue
        h = HEAD.match(t)
        if h and re.fullmatch(r"[IVX]+", h.group(1)):
            sec = h.group(1)
        elif t.strip() == "III":
            sec = "III"
    return rows


def pct(raw, n):
    """The single percentage printed on line n (VII special cases)."""
    found = re.findall(r"(\d+)%", raw[n - 1])
    assert len(found) == 1, (n, raw[n - 1])
    return Fraction(int(found[0]), 100)


def lit(x):
    x = Fraction(x)
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator / x.denominator}"


def main():
    raw = open(sys.argv[1], encoding="utf-8").read().split("\n")
    here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    r = parse(raw)
    f = lambda s, t="": r[(s, t)][2]
    line = lambda s, t="": r[(s, t)][0]
    # V.22: "[4.813.000 + 30.000 x (số chỗ - 25 chỗ)]", read from its three raw lines
    v22 = " ".join(raw[n - 1] for n in range(2091, 2094))
    base, step = [vnd(x) for x in re.findall(r"\d{1,3}(?:\.\d{3})+", v22)]
    k25 = int(re.search(r"số chỗ - (\d+) chỗ", v22).group(1))

    cases = []   # (source line, L4 class, expected VND, label)
    add = lambda n, cls, exp, lab: cases.append((n, cls, exp, lab))
    add(line("I", "1"), "`a two-wheeled motorcycle` 49", f("I", "1"), "I.1 under 50 cc (49 cc)")
    add(line("I", "2"), "`a two-wheeled motorcycle` 50", f("I", "2"), "I.2 50 cc or more (50 cc)")
    add(line("II"), "`a three-wheeled motorcycle`", f("II"), "II three-wheeled motorcycle")
    add(line("III", "1"), "`an electric moped`", f("III", "1"), "III.1 electric moped")
    add(line("III", "2"), "`another moped or similar motor vehicle`", f("III", "2"), "III.2 other mopeds")
    for tt, seats in (("1", 5), ("2", 6), ("2", 11), ("3", 12), ("3", 24), ("4", 25), ("4", 45)):
        add(line("IV", tt), f"`a car not used for transport business` {seats}", f("IV", tt), f"IV.{tt} non-business car, {seats} seats")
    add(line("IV", "5"), "`a pickup or minivan not used for transport business`", f("IV", "5"), "IV.5 pickup or minivan, non-business")
    add(line("V", "1"), "`a car used for transport business` 5", f("V", "1"), "V.1 business car, under 6 seats (5)")
    for tt in range(2, 22):
        seats = int(re.match(r"(\d+) chỗ", r[("V", str(tt))][1]).group(1))
        add(line("V", str(tt)), f"`a car used for transport business` {seats}", f("V", str(tt)), f"V.{tt} business car, {seats} seats")
    for seats in (26, 45):
        add(2092, f"`a car used for transport business` {seats}", base + step * (seats - k25), f"V.22 business car, {seats} seats")
    add(line("V", "23"), "`a pickup or minivan used for transport business`", f("V", "23"), "V.23 pickup or minivan, business")
    for tt, tonnes in (("1", "2.9"), ("2", "3"), ("2", "8"), ("3", "8.1"), ("3", "15"), ("4", "15.1")):
        add(line("VI", tt), f"`a goods vehicle (truck)` {tonnes}", f("VI", tt), f"VI.{tt} truck, {tonnes} t")
    # VII
    add(2102, "`a driving-school vehicle` (`a car not used for transport business` 5)", pct(raw, 2102) * f("IV", "1"), "VII.1 driving-school car (IV.1)")
    add(2102, "`a driving-school vehicle` (`a goods vehicle (truck)` 5)", pct(raw, 2102) * f("VI", "2"), "VII.1 driving-school truck (VI.2)")
    add(2105, "`a taxi` 5", pct(raw, 2105) * f("V", "1"), "VII.2 taxi, 5 seats (V.1)")
    add(2105, "`a taxi` 7", pct(raw, 2105) * f("V", "3"), "VII.2 taxi, 7 seats (V.3)")
    add(2110, "`an ambulance`", pct(raw, 2110) * f("V", "23"), "VII.3(a) ambulance (V.23)")
    add(2112, "`a cash-in-transit vehicle`", pct(raw, 2112) * f("IV", "1"), "VII.3(b) cash-in-transit (IV.1)")
    add(2115, "`another special-purpose car` (JUST 10)", pct(raw, 2115) * f("VI", "3"), "VII.3(c) special-purpose, 10 t (VI.3)")
    add(2117, "`another special-purpose car` NOTHING", pct(raw, 2117) * f("VI", "1"), "VII.3(c) special-purpose, no payload (VI.1)")
    add(2119, "`a tractor unit with its trailer`", pct(raw, 2119) * f("VI", "4"), "VII.4 tractor unit and trailer (VI.4)")
    add(2123, "`a tractor with its trailer`", pct(raw, 2123) * f("VI", "1"), "VII.5 tractor and trailer (VI.1)")
    add(2126, "`a bus` 16", f("IV", "3"), "VII.6 bus, 16 seats (IV.3)")
    add(2126, "`a bus` 30", f("IV", "4"), "VII.6 bus, 30 seats (IV.4)")

    out = ["@lang en", "IMPORT prelude", "IMPORT `nd67-vn10-nouns`", "IMPORT `nd67-art8-premium`", "",
           "-- GENERATED by tools/annex1.py from ../../source/raw/nd67-congbao-1017-1018.txt, lines",
           f"-- {FIRST}-{LAST}. Do not edit by hand. One test per vehicle class of Annex I section A, at",
           "-- both edges of every band of seats and payload, and one per special case of section VII.",
           "-- The expected premium is the figure (or the percentage times the figure) the raw text",
           "-- prints, read by the script; VAT not included, as the Annex says. A failing assertion here",
           "-- is a finding, never an edit.", "",
           "§ `Annex I — one test per row and per band edge`", ""]
    for n, cls, exp, lab in cases:
        out.append(f"-- source line {n}: {lab}")
        out.append(f"#ASSERT `Annex I section A — the premium for a 1-year term, VAT not included, for` ({cls}) EQUALS RIGHT {lit(exp)}")
    with open(os.path.join(here, "nd67-annex1-tests.l4"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(out) + "\n")
    print(f"annex1: {len(r)} rows read; {len(cases)} tests written")
    print("| Annex I row | vehicle tested | premium, VND, VAT not included | src line |")
    print("| --- | --- | --- | --- |")
    for n, cls, exp, lab in cases:
        e = Fraction(exp)
        s = f"{int(e):,}" if e.denominator == 1 else f"{float(e):,.2f}"
        print(f"| {lab.split(' ')[0]} | {lab.split(' ', 1)[1]} | {s} | {n} |")
    return 0


if __name__ == "__main__":
    sys.exit(main())
