#!/usr/bin/env python3
"""Generate the L4 data rows and the tests for the short-period premium scale of Part 4
clause 4 (source lines 582-589) from the raw text, so that no figure is retyped.

  python3 -I tools/gen_shortrate.py ../../source/raw/pti-phuc-an-sinh.txt rows
  python3 -I tools/gen_shortrate.py ../../source/raw/pti-phuc-an-sinh.txt tests

`rows` prints the body of `the short-period scale` (one `A row of the short-period scale`
per source row, in source order). `tests` prints #ASSERT lines: for each row with a month
bound N, a cancellation exactly N calendar months after the first day of cover (inside the
row) and one day later (inside the next row); for the open last row, a cancellation 11
months in. The first day of cover in the tests is 2026-01-15, so no month end is involved.
"""
import re
import sys
import unicodedata

ROW = re.compile(r"^\s*([a-g])\.\s+Đối với thời hạn (đến đủ|trên) (\d+) tháng:\s+(\d+)(?:/(\d+)|%)")


def rows(raw):
    out = []
    for n in range(582, 590):
        line = unicodedata.normalize("NFC", raw[n - 1])
        m = ROW.match(line)
        if not m:
            continue
        letter, kind, months, num, den = m.groups()
        if den is None:  # "100%"
            num, den = num, "100"
        bound = int(months) if kind == "đến đủ" else None
        out.append((n, letter, bound, int(months), int(num), int(den)))
    if len(out) != 7:
        sys.exit(f"expected 7 rows in lines 582-589, found {len(out)}")
    return out


def add_months(y, m, d, k):
    m0 = m - 1 + k
    return y + m0 // 12, m0 % 12 + 1, d


def main():
    raw = open(sys.argv[1], encoding="utf-8").read().split("\n")
    rs = rows(raw)
    if sys.argv[2] == "rows":
        print("    --                                                   row  up to and including, months  fraction of the annual premium")
        for i, (n, letter, bound, months, num, den) in enumerate(rs):
            lead = "LIST" if i == 0 else "   ,"
            b = f"JUST {bound}" if bound is not None else "NOTHING"
            print(f"    {lead} (`A row of the short-period scale` OF \"{letter}\", {b:<8}, {num} / {den})   -- src:{n}")
    elif sys.argv[2] == "tests":
        y, m, d = 2026, 1, 15
        for i, (n, letter, bound, months, num, den) in enumerate(rs):
            if bound is not None:
                ey, em, ed = add_months(y, m, d, bound)
                print(f"#ASSERT `the fraction of the annual premium the short-period scale keeps, for cover from` (YMD {y} {m} {d}) `to` (YMD {ey} {em} {ed}) EQUALS {num} / {den}")
                nxt = rs[i + 1]
                print(f"#ASSERT `the fraction of the annual premium the short-period scale keeps, for cover from` (YMD {y} {m} {d}) `to` ((YMD {ey} {em} {ed}) PLUS 1) EQUALS {nxt[4]} / {nxt[5]}")
            else:
                ey, em, ed = add_months(y, m, d, 11)
                print(f"#ASSERT `the fraction of the annual premium the short-period scale keeps, for cover from` (YMD {y} {m} {d}) `to` (YMD {ey} {em} {ed}) EQUALS {num} / {den}")
    else:
        sys.exit("second argument: rows or tests")


if __name__ == "__main__":
    main()
