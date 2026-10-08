#!/usr/bin/env python3
"""Generate the Annex 1-3 tables of the CSTD encoding, and their threshold tests.

  python3 -I tools/gen_annex.py ../../source/raw/manulife-cstd.txt .

Reads tools/conditions.py (the encoder's hand-written reading of the annexes) and the raw
text. Writes, in the deposit directory:

  cstd-annex-tables.l4     the listing, the stated thresholds and the excluded causes of
                           every listed condition, as data (one CONSIDER arm per condition)
  cstd-tests-annex.l4      two boundary tests for every stated threshold
  and splices the three generated enumerations into cstd-nouns.l4 between the markers
  `-- BEGIN GENERATED` and `-- END GENERATED`.

Checks, and stops on failure: every heading line and every `phrase` is verbatim in the raw
text at the lines given; the comparator the Vietnamese words of each phrase imply agrees
with the comparator typed in conditions.py (unless the phrase is marked 'hand'); the
threshold typed there is among the numbers the phrase contains (same exception).

Where the two come from, so that a test can fail: the L4 table is written from the
comparator and threshold TYPED in conditions.py; the expected value of each generated test
is computed from the comparator DERIVED from the phrase's Vietnamese words by the rules in
`cmp_of`, and from the numbers parsed out of the phrase by `numbers_of`.
"""
import os, re, runpy, sys, unicodedata
from decimal import Decimal

HERE = os.path.dirname(os.path.abspath(__file__))
RAW, OUT = sys.argv[1], sys.argv[2]
D = runpy.run_path(os.path.join(HERE, "conditions.py"))
CONDS, Q, CAUSE, BARS, PAID_BARS = D["CONDS"], D["Q"], D["CAUSE"], D["BARS"], D["PAID_BARS"]
raw = open(RAW, encoding="utf-8").read().split("\n")


def nfc(s): return unicodedata.normalize("NFC", s)
def ws(s): return re.sub(r"\s+", " ", nfc(s)).strip()
def line(n): return ws(raw[n - 1])
def window(a, b): return " ".join(line(k) for k in range(a, b + 1) if line(k))
def quote(a, b=None):
    b = b or a
    return [f"-- src:{k} | {line(k)}" for k in range(a, b + 1) if line(k)]

def die(msg):
    print("gen_annex: " + msg, file=sys.stderr); sys.exit(1)

# ---------------------------------------------------------------- reading the phrases
def cmp_of(phrase):
    """The comparator the Vietnamese words of a phrase imply (None if no rule fires)."""
    p = phrase.lower()
    if re.search(r"trở xuống|ít hơn hoặc bằng|≤", p): return "le"
    if re.search(r"trở lên|ít nhất|tối thiểu|kéo dài|liên tục trong", p): return "ge"
    if re.search(r"dưới|ít hơn|nhỏ hơn|<", p): return "lt"
    if re.search(r"lớn hơn|trên|hơn|sau tuần thứ|>", p): return "gt"
    if re.search(r"trong vòng|vòng|trong thời gian", p): return "le"
    return None

NUM = re.compile(r"–\s*\d+(?:[.,]\d+)?|\d+/\d+|\d+(?:[.,]\d+)*")
def num(tok):
    """Vietnamese format: a dot followed by exactly three digits groups thousands; a dot or a
    comma followed by one or two digits is a decimal point (the annexes write both 1.5 and
    1,73). a/b is a fraction (Snellen 6/60). An en dash before a number is a minus sign."""
    neg = tok.startswith("–")
    t = re.sub(r"^–\s*", "", tok)
    if "/" in t:
        a, b = t.split("/"); v = Decimal(a) / Decimal(b)
    elif re.fullmatch(r"\d{1,3}(\.\d{3})+", t):
        v = Decimal(t.replace(".", ""))
    elif re.fullmatch(r"\d+[.,]\d{1,2}", t):
        v = Decimal(t.replace(",", "."))
    else:
        v = Decimal(t.replace(".", "").replace(",", ""))
    return -v if neg else v
def numbers_of(phrase):
    return [num(m.group(0)) for m in NUM.finditer(phrase)]

def fmt(v):
    v = Decimal(v).normalize()
    s = format(v, "f")
    return s

# ---------------------------------------------------------------- checks
def leaves(c):
    if c is None: return []
    if c[0] in ("all", "any"): return [l for k in c[1] for l in leaves(k)]
    if c[0] == "alt": return []
    return [c]

problems = []
for c in CONDS:
    a, b = c["head"]
    if not window(a, b): problems.append(f"{c['code']}: empty heading at {a}-{b}")
    if c.get("vi") and ws(c["vi"]) not in window(a, b + 3):
        problems.append(f"{c['code']}: term {c['vi']!r} not at {a}")
    for l in leaves(c["crit"]):
        cmp, q, thr, (x, y), phrase = l[:5]
        hand = len(l) > 5 and l[5] == "hand"
        if q not in Q: problems.append(f"{c['code']}: unknown quantity {q}")
        if ws(phrase) not in window(x, y):
            problems.append(f"{c['code']}: phrase {phrase!r} not verbatim in src {x}-{y}")
        if not hand:
            d = cmp_of(phrase)
            if d != cmp: problems.append(f"{c['code']}: typed {cmp}, phrase {phrase!r} reads {d}")
            if Decimal(str(thr)) not in numbers_of(phrase):
                problems.append(f"{c['code']}: threshold {thr} not among {numbers_of(phrase)} in {phrase!r}")
if problems:
    die("\n".join(problems))

# definition ranges: from a condition's heading to the line before the next heading
heads = sorted(set(c["head"][0] for c in CONDS))
ANNEX_END = {1906, 2404, 3143, 3171, 3274, 3368}
def def_end(a):
    nxt = [h for h in heads if h > a]
    stop = min([e for e in ANNEX_END if e >= a])
    return min(nxt[0] - 1, stop) if nxt else stop

def cause_lines(c):
    if c["code"] == "L1": return (2474, 2474)
    a, e = c["head"][0], def_end(c["head"][0])
    for n in range(a, e + 1):
        if "Loại trừ" in raw[n - 1]:
            m = n
            while m < e and m - n < 7 and not line(m).endswith("."):
                m += 1
            return (n, m)
    die(f"{c['code']}: no exclusion sentence found for causes {c['causes']}")

SCHED = {
    "early":    ("Annex 1, the early-stage list", 1393, 1393),
    "middle":   ("Annex 1, the middle-stage list", 1911, 1911),
    "late":     ("Annex 1, the late-stage list", 2408, 2409),
    "men":      ("Annex 2, the list for men", 3147, 3147),
    "women":    ("Annex 2, the list for women", 3175, 3175),
    "children": ("Annex 3, the list for children", 3277, 3278),
}
def bt(s): return "`" + s + "`"
NAME = {c["code"]: c["name"] for c in CONDS}
if len(set(NAME.values())) != len(NAME): die("duplicate condition names")

# ---------------------------------------------------------------- nouns splice
nouns = []
nouns.append("-- The conditions Annexes 1 to 3 list: one constructor for each condition the annexes")
nouns.append("-- head and define separately (NOTES.md, fork F-CI-1, on why a sub-heading under one")
nouns.append("-- number is its own condition). The quoted line is the condition's heading.")
nouns.append("DECLARE `A listed condition` IS ONE OF")
cur = None
for c in CONDS:
    if c["sched"] != cur:
        cur = c["sched"]
        nouns.append(f"    -- {SCHED[cur][0]}")
    lab = f"item {c['item']}" + (f", limb {c['limb']}" if c["limb"] else "")
    nouns.append(f"    -- {c['code']}, {lab}")
    nouns += ["    " + q for q in quote(*c["head"])]
    nouns.append(f"    {bt(c['name'])}")
nouns.append("")
nouns.append("-- The quantities the definitions in Annexes 1 to 3 state a threshold for. A witness of")
nouns.append("-- ordinary competence (the treating specialist, a laboratory report) states each one.")
nouns.append("DECLARE `A measured quantity` IS ONE OF")
used = {l[1] for c in CONDS for l in leaves(c["crit"])}
for k, (name, step) in Q.items():
    if k in used: nouns.append(f"    {bt(name)}")
nouns.append("")
nouns.append("-- The causes the definitions in Annex 1 exclude, each named in at least one \"Loại trừ\"")
nouns.append("-- sentence (the cause table in cstd-annex-tables.l4 quotes each sentence).")
nouns.append("DECLARE `A cause` IS ONE OF")
usedc = {x for c in CONDS for x in c["causes"]}
for k, name in CAUSE.items():
    if k in usedc: nouns.append(f"    {bt(name)}")

np = os.path.join(OUT, "cstd-nouns.l4")
src = open(np, encoding="utf-8").read()
m = re.search(r"(-- BEGIN GENERATED[^\n]*\n)(.*?)(-- END GENERATED)", src, re.S)
if not m: die("cstd-nouns.l4 has no BEGIN/END GENERATED markers")
src = src[: m.start(2)] + "\n".join(nouns) + "\n" + src[m.end(2):]
open(np, "w", encoding="utf-8").write(src)

# ---------------------------------------------------------------- tables module
def crit_l4(cr):
    if cr is None: return "`all of` EMPTY"
    if cr[0] == "alt": return "`the stated qualitative alternative`"
    if cr[0] in ("all", "any"):
        inner = ", ".join("(" + crit_l4(k) + ")" for k in cr[1])
        return f"`{cr[0]} of` (LIST {inner})"
    cmp, q, thr = cr[:3]
    word = {"ge": "at least", "le": "at most", "gt": "more than", "lt": "less than"}[cmp]
    t = fmt(Decimal(str(thr)))
    if t.startswith("-"): t = "(0 MINUS " + t[1:] + ")"
    return f"{bt(word)} {bt(Q[q][0])} {t}"

def crit_lines(cr):
    if cr is None: return []
    if cr[0] in ("all", "any"): return [x for k in cr[1] for x in crit_lines(k)]
    if cr[0] == "alt": return []
    return [cr[3]]

T = []
T.append("@lang en")
T.append("IMPORT prelude")
T.append("IMPORT `cstd-nouns`")
T.append("")
T.append("-- Manulife CSTD terms, Annexes 1 to 3: the lists of critical illnesses, as DATA.")
T.append("-- GENERATED by tools/gen_annex.py from tools/conditions.py and the raw text. Do not edit by")
T.append("-- hand: change conditions.py and run, from this directory,")
T.append("--     python3 -I tools/gen_annex.py ../../source/raw/manulife-cstd.txt .")
T.append("-- Three tables, each one CONSIDER arm per listed condition, each arm under the source lines")
T.append("-- it encodes: where the condition is listed (annex and item number); the thresholds its")
T.append("-- definition states, as a criterion over measured quantities; and the causes its own")
T.append("-- definition excludes. What the rules do with them is cstd-annex-rules.l4.")
T.append("")
T.append("§ `Annexes 1 to 3 — the lists of critical illnesses`")
T.append("")
T.append("-- src:178 | Bệnh Lý Nghiêm Trọng: là các bệnh, tình trạng y tế")
T.append("-- src:179 | hoặc phẫu thuật được quy định cụ thể tại Phụ Lục 1, Phụ")
T.append("-- src:180 | Lục 2, Phụ Lục 3 của Hợp Đồng này.")
T.append("DECLARE `A list of conditions` IS ONE OF")
for k, (name, a, b) in SCHED.items():
    T += ["    " + q for q in quote(a, b)]
    T.append(f"    {bt(name)}")
T.append("")
T.append("DECLARE `A listing` HAS")
T.append("    `the list`        IS A `A list of conditions`")
T.append("    `the item number` IS A NUMBER")
T.append("")
T.append("-- A threshold a definition states, over one measured quantity; `all of` and `any of` join")
T.append("-- them as the definition joins them (\"và\" / \"hoặc\"); `the stated qualitative")
T.append("-- alternative` stands for a limb the definition offers IN PLACE OF a number (e.g. \"ung thư")
T.append("-- hắc tố xâm lấn hoặc dưới 1.5 mm\"), which the specialist certifies or not.")
T.append("DECLARE `A criterion` IS ONE OF")
T.append("    `at least`  HAS `the quantity` IS A `A measured quantity`")
T.append("                    `the threshold` IS A NUMBER")
T.append("    `at most`   HAS `the quantity` IS A `A measured quantity`")
T.append("                    `the threshold` IS A NUMBER")
T.append("    `more than` HAS `the quantity` IS A `A measured quantity`")
T.append("                    `the threshold` IS A NUMBER")
T.append("    `less than` HAS `the quantity` IS A `A measured quantity`")
T.append("                    `the threshold` IS A NUMBER")
T.append("    `all of`    HAS `the parts` IS A LIST OF `A criterion`")
T.append("    `any of`    HAS `the parts` IS A LIST OF `A criterion`")
T.append("    `the stated qualitative alternative`")
T.append("")
# listing table
T.append("§§ `Where each condition is listed`")
T.append("")
T.append("-- The item numbers are printed beside the headings in the PDF's two-column layout; in the")
T.append("-- raw text they are separated from them (e.g. src:1394-1396), so each number here was read")
T.append("-- against the PDF page. A sub-heading under one number carries that number.")
T.append("GIVEN c IS A `A listed condition`")
T.append("GIVETH A `A listing`")
T.append("`the listing of` c MEANS")
T.append("    CONSIDER c")
w = max(len(bt(c["name"])) for c in CONDS)
for c in CONDS:
    T.append(f"    WHEN {bt(c['name']).ljust(w)} THEN `A listing` OF {bt(SCHED[c['sched']][0])}, {c['item']}")
T.append("")
# criteria table
T.append("§§ `The thresholds each definition states`")
T.append("")
T.append("-- A condition whose definition states no number answers `all of` EMPTY, which every")
T.append("-- diagnosis meets: its definition is wholly qualitative, and the specialist's certificate")
T.append("-- (cstd-annex-rules.l4) carries it. Each arm is under the lines that state its numbers.")
T.append("GIVEN c IS A `A listed condition`")
T.append("GIVETH A `A criterion`")
T.append("`the measured criteria of` c MEANS")
T.append("    CONSIDER c")
for c in CONDS:
    if c["crit"] is None: continue
    ls = []
    for (x, y) in crit_lines(c["crit"]):
        for k in range(x, y + 1):
            if line(k) and k not in ls: ls.append(k)
    T.append(f"    -- {c['code']}")
    for k in sorted(ls):
        T += ["    " + q for q in quote(k)]
    T.append(f"    WHEN {bt(c['name'])} THEN")
    T.append(f"        {crit_l4(c['crit'])}")
T.append("    OTHERWISE `all of` EMPTY")
T.append("")
# causes table
T.append("§§ `The causes each definition excludes`")
T.append("")
T.append("GIVEN c IS A `A listed condition`")
T.append("GIVETH A LIST OF `A cause`")
T.append("`the causes excluded by the definition of` c MEANS")
T.append("    CONSIDER c")
for c in CONDS:
    if not c["causes"]: continue
    a, b = cause_lines(c)
    T.append(f"    -- {c['code']}")
    T += ["    " + q for q in quote(a, b)]
    T.append(f"    WHEN {bt(c['name'])} THEN LIST " + ", ".join(bt(CAUSE[x]) for x in c["causes"]))
T.append("    OTHERWISE EMPTY")
T.append("")
# bars
T.append("§§ `The bars one listed condition puts on another`")
T.append("")
T.append("-- Three definitions bar payment when ANOTHER condition is claimed (\"được yêu cầu quyền lợi")
T.append("-- bảo hiểm\"), whether or not that claim is paid; NOTES.md finding X-3 shows that the bars")
T.append("-- are mutual, so a claim for both conditions leaves neither payable.")
T.append("GIVEN c IS A `A listed condition`")
T.append("GIVETH A LIST OF `A listed condition`")
T.append("`the conditions whose claim bars` c MEANS")
T.append("    CONSIDER c")
for (who, by, (a, b), words) in BARS:
    T += ["    " + q for q in quote(a, b)]
    T.append(f"    WHEN {bt(NAME[who])} THEN LIST " + ", ".join(bt(NAME[x]) for x in by))
T.append("    OTHERWISE EMPTY")
T.append("")
T.append("-- One definition bars payment when ANOTHER condition has already been PAID.")
T.append("GIVEN c IS A `A listed condition`")
T.append("GIVETH A LIST OF `A listed condition`")
T.append("`the conditions whose payment bars` c MEANS")
T.append("    CONSIDER c")
for (who, by, (a, b)) in PAID_BARS:
    T += ["    " + q for q in quote(a, b)]
    T.append(f"    WHEN {bt(NAME[who])} THEN LIST " + ", ".join(bt(NAME[x]) for x in by))
T.append("    OTHERWISE EMPTY")
open(os.path.join(OUT, "cstd-annex-tables.l4"), "w", encoding="utf-8").write("\n".join(T) + "\n")

# ---------------------------------------------------------------- tests
OPS = {"ge": lambda v, t: v >= t, "le": lambda v, t: v <= t,
       "gt": lambda v, t: v > t, "lt": lambda v, t: v < t}

def reading(l):
    """(cmp, threshold) as the PHRASE reads them; for a 'hand' leaf, as typed."""
    cmp, q, thr, rng, phrase = l[:5]
    if len(l) > 5 and l[5] == "hand":
        return cmp, Decimal(str(thr)), True
    nums = numbers_of(phrase)
    t = Decimal(str(thr)) if Decimal(str(thr)) in nums else nums[0]
    return cmp_of(phrase), t, False

def passing(l):
    cmp, t, _ = reading(l); s = Decimal(str(Q[l[1]][1]))
    return {"ge": t, "le": t, "gt": t + s, "lt": t - s}[cmp]
def failing(l):
    cmp, t, _ = reading(l); s = Decimal(str(Q[l[1]][1]))
    return {"ge": t - s, "le": t + s, "gt": t, "lt": t}[cmp]

def contains(node, target):
    return node is target or (node[0] in ("all", "any") and any(contains(k, target) for k in node[1]))

def assign(node, focus, a, mode):
    """Fill assignment `a` (quantity -> value, plus 'ALT') so that `node` is true ('pass'),
    false ('fail'), or follows the focus leaf ('focus')."""
    kind = node[0]
    if kind == "alt":
        a.setdefault("ALT", mode == "pass")
        if mode == "fail": a["ALT"] = False
        return
    if kind in ("all", "any"):
        for k in node[1]:
            if mode == "focus" and contains(k, focus):
                assign(k, focus, a, "focus")
            elif mode == "focus":
                assign(k, focus, a, "pass" if kind == "all" else "fail")
            elif mode == "pass" and kind == "all":
                assign(k, focus, a, "pass")
            elif mode == "pass" and kind == "any":
                nums = [x for x in node[1] if x[0] != "alt"]
                assign(nums[0] if nums else node[1][0], focus, a, "pass"); break
            elif mode == "fail" and kind == "any":
                assign(k, focus, a, "fail")
            elif mode == "fail" and kind == "all":
                assign(k, focus, a, "fail"); break
        return
    if node is focus: return
    v = passing(node) if mode == "pass" else failing(node)
    q = node[1]
    if q in a and mode == "pass":
        cmp, t, _ = reading(node)
        if OPS[cmp](a[q], t): return
    a[q] = v

def evaluate(node, a):
    kind = node[0]
    if kind == "alt": return a.get("ALT", False)
    if kind == "all": return all(evaluate(k, a) for k in node[1])
    if kind == "any": return any(evaluate(k, a) for k in node[1])
    cmp, t, _ = reading(node)
    return OPS[cmp](a[node[1]], t)

def l4list(a):
    items = [f"(`A measurement` OF {bt(Q[q][0])}, {fmtv(v)})" for q, v in a.items() if q != "ALT"]
    return "(LIST " + ", ".join(items) + ")"
def fmtv(v):
    s = fmt(v)
    return f"(0 MINUS {s[1:]})" if s.startswith("-") else s

X = []
X.append("@lang en")
X.append("IMPORT prelude")
X.append("IMPORT `cstd-nouns`")
X.append("IMPORT `cstd-annex-tables`")
X.append("IMPORT `cstd-annex-rules`")
X.append("")
X.append("-- Boundary tests for every threshold Annexes 1 to 3 state. GENERATED by tools/gen_annex.py;")
X.append("-- do not edit by hand.")
X.append("--")
X.append("-- WHERE THE EXPECTED VALUES COME FROM. Not from the L4 table. For each threshold the")
X.append("-- generator takes the verbatim Vietnamese phrase that states it (checked against the raw")
X.append("-- text at the lines cited), reads the comparator from its words (\"ít nhất\", \"tối thiểu\",")
X.append("-- \"trở lên\", \"kéo dài\" = at least; \"trở xuống\" = at most; \"dưới\", \"ít hơn\", \"nhỏ hơn\" = less")
X.append("-- than; \"lớn hơn\", \"hơn\", \"trên\", \"sau tuần thứ\" = more than; \"trong vòng\", \"trong thời")
X.append("-- gian\" = at most) and the number from its digits (Vietnamese format: a dot before three")
X.append("-- digits groups thousands, a dot or comma before one or two digits is a decimal point), and")
X.append("-- computes the expected answer from that reading. A phrase with no comparator word is marked")
X.append("-- HAND-READ below, and for it the expectation is the encoder's reading. Two values per")
X.append("-- threshold: on it, and one step past it. Every other threshold of the condition is set to")
X.append("-- a passing value (or, inside an \"or\", to a failing one), so the answer turns on this one.")
X.append("")
X.append("§ `Annexes 1 to 3 — boundary tests of the stated thresholds`")
X.append("")
ntests = 0
for c in CONDS:
    if c["crit"] is None: continue
    X.append(f"-- {c['code']} {c['name']}")
    for l in leaves(c["crit"]):
        cmp, t, hand = reading(l)
        s = Decimal(str(Q[l[1]][1]))
        vals = {"ge": [t, t - s], "le": [t, t + s], "gt": [t, t + s], "lt": [t, t - s]}[cmp]
        x, y = l[3]
        X.append(f"--   src:{x}" + (f"-{y}" if y != x else "") + f", \"{ws(l[4])}\": {cmp} {fmt(t)}" + (" (HAND-READ)" if hand else ""))
        for v in vals:
            a = {}
            assign(c["crit"], l, a, "focus")
            a[l[1]] = v
            exp = evaluate(c["crit"], a)
            alt = "TRUE" if a.get("ALT") else "FALSE"
            call = f"`the thresholds of` {bt(c['name'])} `are met by` {l4list(a)} `with the qualitative alternative` {alt}"
            X.append(("#ASSERT " + call) if exp else ("#ASSERT NOT (" + call + ")"))
            ntests += 1
    # the qualitative alternative, where there is one: alone it suffices
    if any(True for _ in [1]) and "('alt',)" in repr(c["crit"]):
        a = {}
        for l in leaves(c["crit"]):
            a[l[1]] = failing(l)
        a["ALT"] = True
        exp = evaluate(c["crit"], a)
        call = f"`the thresholds of` {bt(c['name'])} `are met by` {l4list(a)} `with the qualitative alternative` TRUE"
        X.append("--   the qualitative alternative alone, every number failing:")
        X.append(("#ASSERT " + call) if exp else ("#ASSERT NOT (" + call + ")"))
        ntests += 1
    X.append("")
open(os.path.join(OUT, "cstd-tests-annex.l4"), "w", encoding="utf-8").write("\n".join(X) + "\n")
print(f"gen_annex: {len(CONDS)} conditions, {sum(1 for c in CONDS if c['crit'])} with thresholds, "
      f"{sum(len(leaves(c['crit'])) for c in CONDS)} thresholds, {ntests} tests")
