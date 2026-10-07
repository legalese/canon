#!/usr/bin/env python3
"""Generate nd67-vn27-art17-tests.l4: the answer table of Article 17 as tests, from the raw text.

usage (from the encoding directory):
  python3 -I tools/art17.py ../../source/raw/nd67-congbao-1017-1018.txt > nd67-vn27-art17-tests.l4

The expected values are computed here from figures EXTRACTED FROM THE RAW TEXT by regular
expressions (Article 6(1)'s limit, Article 12(3)(b)'s and Article 17(1)(a)'s percentages and
thresholds, the eight ceilings of Article 17(1)(a)-(h) and their bases, the points of 17(1)(i)),
not copied from the L4 modules. The script stops if any extraction does not find exactly what
it expects. Only the mapping from a point letter to this row's L4 names is written by hand.
It reads the raw text as data and never executes it.
"""
import re
import subprocess
import sys

RAW = sys.argv[1]
LINES = open(RAW, encoding="utf-8").read().split("\n")


def joined(a, b):
    """Lines a..b (1-based, inclusive), running headers dropped, whitespace collapsed."""
    t = " ".join(l.strip() for l in LINES[a - 1 : b] if "CÔNG BÁO" not in l)
    return re.sub(r"\s+", " ", t)


def quote(a, b):
    r = subprocess.run(["python3", "-I", "tools/vnsrc.py", "quote", RAW, str(a), str(b)],
                       capture_output=True, text=True, check=True)
    return [q for q in r.stdout.splitlines() if "CÔNG BÁO/Số" not in q]


def die(msg):
    sys.exit("art17.py: " + msg)


# Article 6(1): the limit per person per accident.
m = re.search(r"là (\d+) triệu đồng cho một người trong một vụ tai nạn", joined(188, 189))
if not m:
    die("Article 6(1) limit not found")
LIMIT = int(m.group(1)) * 1_000_000

# Article 17(1)(a): two support rates and their thresholds.
SUP = re.compile(
    r"(\d+)% giới hạn trách nhiệm bảo hiểm theo quy định cho một người trong một vụ tai nạn "
    r"đối với trường hợp (?:(tử vong và )?(?:ước tính )?tỷ lệ tổn thương từ (\d+)% (trở lên|đến dưới (\d+)%))")


def bands(a, b, label):
    found = SUP.findall(joined(a, b))
    if len(found) != 2:
        die(f"{label}: expected 2 bands, found {found}")
    (hi_pct, hi_death, hi_from, hi_kind, _), (lo_pct, lo_death, lo_from, lo_kind, lo_to) = found
    if not hi_death or hi_kind != "trở lên" or lo_death or not lo_to:
        die(f"{label}: unexpected shape {found}")
    if int(lo_to) != int(hi_from):
        die(f"{label}: the bands do not meet: {found}")
    return int(hi_pct), int(hi_from), int(lo_pct), int(lo_from)


S_HI, S_HI_FROM, S_LO, S_LO_FROM = bands(494, 502, "Article 17(1)(a)")
A_HI, A_HI_FROM, A_LO, A_LO_FROM = bands(325, 330, "Article 12(3)(b)")

# Article 17(1)(a)-(h): the ceilings and their bases.
CEIL = re.compile(
    r"(?:^| )([a-hđ])\) .*?Mức chi không vượt quá (\d+)% tổng số tiền đóng vào Quỹ bảo hiểm xe cơ "
    r"giới hàng năm( và số dư Quỹ bảo hiểm xe cơ giới các năm trước \(nếu có\))?")
ceilings = [(p, int(n), bool(b)) for p, n, b in CEIL.findall(joined(492, 550))]
if [c[0] for c in ceilings] != ["a", "b", "c", "d", "đ", "e", "g", "h"]:
    die(f"ceilings: unexpected points {ceilings}")

# Article 17(1)(i): which points, and the 1%.
mi = re.search(r"tổng mức chi không vượt quá tỷ lệ quy định tại điểm (d), điểm (đ), điểm (e), "
               r"điểm (g), điểm (h) khoản 1 Điều này tương ứng với mức đóng góp tối đa (\d+)%",
               joined(551, 559))
if not mi:
    die("Article 17(1)(i) not found")
EMERGENCY_POINTS = list(mi.groups()[:5])
EMERGENCY_RATE = int(mi.group(6))

# Hand-written: this row's L4 names for the point letters.
HEAD = {
    "a": "(a) humanitarian support, and repaying advances",
    "b": "(b) works and equipment to prevent and limit losses and road accidents",
    "c": "(c) propaganda and education on road safety and the compulsory motor insurance",
    "d": "(d) support for the police",
    "đ": "(dd) rewards for achievement",
    "e": "(e) the database of the compulsory motor insurance",
    "g": "(g) the ASEAN compulsory motor insurance programme",
    "h": "(h) managing the Fund",
}
VINTAGES = ["the decree as made", "the decree as amended by Decree 220/2026"]
EXCL = [
    "Article 7(2)(a): an intentional act of the owner or the driver",
    "Article 7(2)(b): the driver fled without performing the owner's civil liability",
    "Article 7(2)(c): the driver's age or driving licence",
    "Article 7(2)(d): an indirect consequence",
    "Article 7(2)(dd): alcohol or drugs, for damage to property",
    "Article 7(2)(e): property stolen or robbed in the accident",
    "Article 7(2)(g): special property",
    "Article 7(2)(h): war, terrorism or an earthquake",
]
SITUATIONS = (
    [("`a vehicle that was not identified`", "the vehicle that caused the accident was not identified"),
     ("`an identified vehicle with no compulsory insurance in force`", "the vehicle was not insured"),
     ("(`an identified, insured vehicle, whose insurer answers` `the harm is outside the scope of Article 7(1)`)",
      "the harm is outside the scope of the insurance")]
    + [(f"(`an identified, insured vehicle, whose insurer answers` `{e}`)",
        "an exclusion of Article 7(2) applies, other than the injured person's own intentional act") for e in EXCL]
    + [("(`an identified, insured vehicle, whose insurer answers` `Article 7(2)(a): an intentional act of the injured person`)", None),
       ("(`an identified, insured vehicle, whose insurer answers` `the insurer covers the harm`)", None)]
)


def harms(hi_from, lo_from):
    """Both sides of each threshold, a death, and the ends of the scale."""
    return [None, 100, hi_from, hi_from - 0.5, hi_from - 1, lo_from, lo_from - 0.5, lo_from - 1, 0]


def harm_l4(h):
    return "`death`" if h is None else f"(`an injury assessed at a rate of` {fmt(h)})"


def fmt(x):
    return str(int(x)) if float(x).is_integer() else str(x)


def support(h):
    if h is None or h >= S_HI_FROM:
        return LIMIT * S_HI // 100
    if h >= S_LO_FROM:
        return LIMIT * S_LO // 100
    return None


def prescribed_advance(h):
    if h is None or h >= A_HI_FROM:
        return LIMIT * A_HI // 100
    if h >= A_LO_FROM:
        return LIMIT * A_LO // 100
    return 0


out = []
w = out.append
w("@lang en")
w("IMPORT `nd67-vn27-art75`")
w("")
w("-- GENERATED by tools/art17.py from ../../source/raw/nd67-congbao-1017-1018.txt; do not edit.")
w("-- The answer table of Article 17 (with Article 6(1) and 12(3)(b)) as tests, in both vintages.")
w("-- Expected values come from figures the script extracted from the raw text:")
w(f"--   Article 6(1) limit {LIMIT}; Article 17(1)(a) {S_HI}% from {S_HI_FROM}% (and a death), {S_LO}% from {S_LO_FROM}%;")
w(f"--   Article 12(3)(b) {A_HI}% from {A_HI_FROM}% (and a death), {A_LO}% from {A_LO_FROM}%;")
w("--   ceilings " + ", ".join(f"({p}) {n}%{' with the balance' if b else ''}" for p, n, b in ceilings).replace("(đ)", "(dd)") + ";")
w(f"--   Article 17(1)(i): points {', '.join(EMERGENCY_POINTS).replace('đ', 'dd')} at a {EMERGENCY_RATE}% contribution.")
w("")
w("§ `Article 17 — generated tests`")
w("")
w("GIVEN h IS A `The harm to the person`")
w("      x IS A `A vehicle that caused the harm`")
w("GIVETH A `A person harmed in a road accident`")
w("`a person with` h `harmed by` x MEANS")
w("    `A person harmed in a road accident` WITH")
w("        `the accident happened on`          IS YMD 2026 7 1")
w("        `the harm`                          IS h")
w("        `the vehicles that caused the harm` IS LIST x")
w("")
w("§§ `Article 6(1) — the limit`")
w("")
w(from_q := "\n".join(quote(188, 189)))
w(f"#ASSERT `Article 6(1) — the limit per person per accident, for health and life` EQUALS {LIMIT}")
w("")
w("§§ `Article 17(1)(a) — humanitarian support, every case, both sides of each threshold`")
w("")
w("\n".join(quote(494, 502)))
n_sup = 0
for v in VINTAGES:
    for x, case in SITUATIONS:
        for h in harms(S_HI_FROM, S_LO_FROM):
            if case is None:
                exp = "RIGHT `no support: none of the cases of Article 17(1)(a)`"
            elif support(h) is None:
                exp = "RIGHT `no support: an injury rate under 31%`"
            else:
                exp = f"RIGHT (`support of` {support(h)} `{case}`)"
            w(f"#ASSERT `Article 17(1)(a) — under` `{v}` `, the humanitarian support for` (`a person with` {harm_l4(h)} `harmed by` {x}) EQUALS {exp}")
            n_sup += 1
w("")
w("§§ `Article 17(1)(a), second paragraph — repaying an advance under Article 12(3)(b)`")
w("")
w("-- Each advance is the amount Article 12(3)(b) prescribes for the harm plus 1,000,000; the Fund")
w("-- repays at most the prescribed amount (fork V11), and nothing where the accident was later")
w("-- found within the scope.")
w("\n".join(quote(325, 330)))
w("\n".join(quote(503, 507)))
LATER = [("`excluded under Article 7(2)`", True), ("`outside the scope of the insurance`", True),
         ("`within the scope and not excluded`", False)]
n_rep = 0
for v in VINTAGES:
    for later, owed in LATER:
        for h in harms(A_HI_FROM, A_LO_FROM):
            amt = prescribed_advance(h) + 1_000_000
            adv = (f"(`An advance an insurer paid` WITH `the point under which it was paid` IS "
                   f"`point (b): the accident had not yet been found within the scope of compensation`, "
                   f"`the harm, as estimated when the advance was paid` IS {harm_l4(h)}, "
                   f"`the amount advanced` IS {amt}, `what was later found of the accident` IS {later})")
            exp = (f"RIGHT (`the Fund must repay` {min(amt, prescribed_advance(h))})" if owed
                   else "RIGHT `no duty: the accident was later found within the scope and not excluded`")
            w(f"#ASSERT `Article 17(1)(a) — under` `{v}` `, what the Fund owes the insurer for` {adv} EQUALS {exp}")
            n_rep += 1
w("")
w("§§ `Article 17(1)(a)-(h) — the ceilings, on contributions of 100,000,000,000 and a balance of 20,000,000,000`")
w("")
w("\n".join(quote(510, 550)))
C, B = 100_000_000_000, 20_000_000_000
rows = ", ".join(f"(`A ceiling of Article 17(1)` OF `{HEAD[p]}`, {n}, {'TRUE' if b else 'FALSE'})" for p, n, b in ceilings)
w(f"#ASSERT `Article 17(1) — the ceilings` EQUALS LIST {rows}")
w(f"#ASSERT sum (map (GIVEN r YIELD r's percent) `Article 17(1) — the ceilings`) EQUALS {sum(n for _, n, _ in ceilings)}")
n_ceil = 2
for p, n, b in ceilings:
    cap = (C + B) * n // 100 if b else C * n // 100
    w(f"#ASSERT `Article 17(1) — the most the Fund may spend in a year under` `{HEAD[p]}` `, on contributions of` {C} `and a balance of earlier years of` {B} EQUALS {cap}")
    w(f"#ASSERT `Article 17(1) — the heads overspent by` (LIST `A year's spending under a head` OF `{HEAD[p]}`, {cap}) `, on contributions of` {C} `and a balance of earlier years of` {B} EQUALS EMPTY")
    w(f"#ASSERT `Article 17(1) — the heads overspent by` (LIST `A year's spending under a head` OF `{HEAD[p]}`, {cap + 1}) `, on contributions of` {C} `and a balance of earlier years of` {B} EQUALS LIST `{HEAD[p]}`")
    n_ceil += 3
w("")
w("§§ `Article 17(1)(i) — the emergency ceiling, on premiums of 10,000,000,000,000`")
w("")
w("\n".join(quote(551, 559)))
P = 10_000_000_000_000
rate_sum = sum(n for p, n, _ in ceilings if p in EMERGENCY_POINTS)
w(f"#ASSERT `Article 17(1)(i) — the most that may be spent from the balance of earlier years on points (d) to (h), on premiums of` {P} EQUALS {P * EMERGENCY_RATE // 100 * rate_sum // 100}")
n_em = 1
w("")
w(f"-- {1 + n_sup + n_rep + n_ceil + n_em} assertions: 1 limit, {n_sup} support, {n_rep} repayment, {n_ceil} ceilings, {n_em} emergency.")
print("\n".join(out))
