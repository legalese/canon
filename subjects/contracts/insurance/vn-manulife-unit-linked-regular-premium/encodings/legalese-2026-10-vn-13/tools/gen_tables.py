#!/usr/bin/env python3
"""Generate the L4 for the two tables in the source, from the raw text, so no figure is retyped.

  python3 -I tools/gen_tables.py RAW.txt charge-table   the Article 13.9(a) table as L4 data
  python3 -I tools/gen_tables.py RAW.txt charge-tests   #ASSERTs: both edges of every row
  python3 -I tools/gen_tables.py RAW.txt equity-bands   the Annex 1 equity bands as L4 data
  python3 -I tools/gen_tables.py RAW.txt equity-tests   #ASSERTs: both edges of every band

RAW.txt is ../../source/raw/manulife-maxx.txt. Every row carries `-- src:N |` comments made the
same way as `vnsrc.py quote` makes them (NFC, whitespace collapsed), so `vnsrc.py check` verifies
them. The script fails loudly if the layout it expects is not there.
"""
import re
import sys
import unicodedata

FREQ = [
    ("Hợp đồng đóng phí năm", "`annual premiums`"),
    ("Hợp đồng đóng phí nửa năm", "`half-yearly premiums`"),
    ("Hợp đồng đóng phí quý", "`quarterly premiums`"),
    ("Hợp đồng đóng phí tháng", "`monthly premiums`"),
]
FUNDS = [
    ("2.1. Quỹ Tăng Trưởng:", "`the Growth Fund`"),
    ("2.2. Quỹ Phát Triển:", "`the Development Fund`"),
    ("2.3. Quỹ Cân Bằng:", "`the Balanced Fund`"),
]


def load(path):
    with open(path, encoding="utf-8") as f:
        return [unicodedata.normalize("NFC", x) for x in f.read().split("\n")]


def q(lines, n):
    return "-- src:%d | %s" % (n, re.sub(r"\s+", " ", lines[n - 1]).strip())


def charge_rows(lines):
    """[(freq_l4, header_line, [(range_line, rate_line, first, last_or_None, pct)])]"""
    out = []
    for label, l4 in FREQ:
        hits = [i for i, x in enumerate(lines, 1) if x.strip() == label]
        if len(hits) != 1:
            sys.exit("expected one heading %r, found %d" % (label, len(hits)))
        h = hits[0]
        if lines[h].strip() != "Phí BHCBĐK lần" or lines[h + 1].strip() != "Tỷ lệ Phí Ban đầu":
            sys.exit("column headings not where expected after line %d" % h)
        rows, n = [], h + 3
        while len(rows) < 4:
            rng, rate = lines[n - 1].strip(), lines[n].strip()
            m = re.fullmatch(r"(\d+)(?:-(\d+))?( trở lên)?", rng)
            r = re.fullmatch(r"(\d+)%", rate)
            if not m or not r:
                sys.exit("unexpected row at lines %d-%d: %r %r" % (n, n + 1, rng, rate))
            first = int(m.group(1))
            last = None if m.group(3) else int(m.group(2) or m.group(1))
            rows.append((n, n + 1, first, last, int(r.group(1))))
            n += 2
        out.append((l4, h, rows))
    return out


def equity_bands(lines):
    out = []
    for label, l4 in FUNDS:
        hits = [i for i, x in enumerate(lines, 1) if x.strip() == label]
        if len(hits) != 1:
            sys.exit("expected one heading %r" % label)
        n = hits[0]
        while not lines[n - 1].strip().startswith("• Đầu tư từ"):
            n += 1
            if n > hits[0] + 40:
                sys.exit("no equity band after %r" % label)
        m = re.match(r"• Đầu tư từ (\d+)% đến (\d+)% vào cổ phiếu", lines[n - 1].strip())
        if not m:
            sys.exit("unexpected band line %d" % n)
        out.append((l4, hits[0], n, int(m.group(1)), int(m.group(2))))
    return out


def lastval(last):
    return "NOTHING" if last is None else "JUST %d" % last


def main():
    lines = load(sys.argv[1])
    what = sys.argv[2]
    if what == "charge-table":
        print("    --  frequency               first  last       maximum rate")
        body = []
        for l4, h, rows in charge_rows(lines):
            body.append("    " + q(lines, h))
            for a, b, first, last, pct in rows:
                body.append("    " + q(lines, a))
                body.append("    " + q(lines, b))
                body.append("    (`A row of the Article 13.9(a) table` OF %-22s, %3d, %-8s, %d%%)"
                            % (l4, first, lastval(last), pct))
        # join rows with commas: the list literal is LIST r1, r2, ...
        out, seen = [], 0
        for x in body:
            if x.lstrip().startswith("(`A row"):
                out.append(("    " if seen == 0 else "  , ") + x.lstrip())
                seen += 1
            else:
                out.append(x)
        print("\n".join(out))
    elif what == "charge-tests":
        for l4, h, rows in charge_rows(lines):
            for a, b, first, last, pct in rows:
                probes = [first, last] if last is not None else [first, first + 12]
                for p in dict.fromkeys(probes):
                    print("#ASSERT `the guaranteed maximum initial charge rate for instalment` %d `paid as` %s EQUALS %d%%   -- src:%d-%d"
                          % (p, l4, pct, a, b))
    elif what == "equity-bands":
        for l4, h, n, lo, hi in equity_bands(lines):
            print("    " + q(lines, h))
            print("    " + q(lines, n))
            print("    WHEN %-24s THEN `An equity band` OF %d%%, %d%%" % (l4, lo, hi))
    elif what == "equity-tests":
        for l4, h, n, lo, hi in equity_bands(lines):
            print("#ASSERT `Annex 1 — the equity share is within the band for` %s `:` (%d%%)   -- src:%d" % (l4, lo, n))
            print("#ASSERT `Annex 1 — the equity share is within the band for` %s `:` (%d%%)   -- src:%d" % (l4, hi, n))
            if lo > 0:
                print("#ASSERT NOT (`Annex 1 — the equity share is within the band for` %s `:` (%d%%))   -- src:%d" % (l4, lo - 1, n))
            if hi < 100:
                print("#ASSERT NOT (`Annex 1 — the equity share is within the band for` %s `:` (%d%%))   -- src:%d" % (l4, hi + 1, n))
    else:
        print(__doc__)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
