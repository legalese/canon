#!/usr/bin/env python3
"""Put one `@ref` source locator under every quote run of this row's modules.

  python3 -I tools/switch_to_ref_locators.py             add the `@ref` lines to ../*.l4 and to ../templates/*.l4.in
  python3 -I tools/switch_to_ref_locators.py --dry-run   report what would change; write nothing
  python3 -I tools/switch_to_ref_locators.py --no-templates
                                                         leave templates/*.l4.in alone (then `tools/expand.py` removes the lines again)
  python3 -I tools/switch_to_ref_locators.py --line-map FILE
                                                         also write FILE: one line `module<TAB>N` for every inserted line, N being the
                                                         line of the OLD module it was inserted after (see below)

A quote run is what `tools/srcrefs.py check` calls a run: consecutive `-- src:N | text` lines, blank lines allowed between,
anything else ends it. Runs that are separated only by blank lines and plain comments are placed together, as one unit,
because the gate puts them in one block. Under each unit the script inserts ONE line

    @ref Dieu N (src:A-B)                          a unit in the main raw file, the lines A to B
    @ref Dieu N (src:A-B; src:ID:C-D)              a unit that also quotes the raw file ID.txt (two locators, one line)
    @ref Law 139/2025/QH15 Dieu 1 (src:ID:C-D)     a unit that quotes only another law's text
    @ref src:A-B                                   no article could be found

Placement (convention C4): immediately after the last quote line of the unit, which must be directly above (blank lines and
plain `--` comments may sit between) the first declaration the unit supports. A declaration here is a DECLARE, a GIVEN- or
GIVETH-led rule, a DECIDE, an ASSUME, a definition that starts with a backtick-quoted name, or an `@desc` / `@export` block.
(GIVETH-led rules and backtick definitions are what this row writes; the convention's list is shorter.) A unit followed by
anything else (a `§` / `§§` heading, a `#ASSERT` / `#EVAL` / `#CHECK`, the end of the file) gets no `@ref`; the script lists
it as unplaced, by file and line, says whether the gate exempts it (it does for those three), and leaves it alone.

Locator A-B: per raw file, the lowest first line and the highest last line the unit quotes. Where the unit skips a raw line
that is neither blank nor page furniture (a gazette header such as `CÔNG BÁO/Số ...`, a bare page number), or goes backwards,
within one raw file, each stretch gets its own locator, so that a locator never claims a clause the unit leaves out.

The label is `Dieu N`, in ASCII like the rule names of this row (the encoding keeps Vietnamese to quote lines; `tools/vnsrc.py`
counts any other Vietnamese). N comes from the raw file itself: the `Điều N.` headings of the raw text say which article each
raw line lies in, so the label names every article the unit's quoted lines lie in (`Dieu 91-93`, `Dieu 5, 9`), and nothing the
quotation does not reach; the name of the declaration below is not consulted. Quotations from Law 08/2022/QH15 (the main
raw file and the second gazette issue, `law08-2022-qh15-577-578`) are labelled by Law 08 articles, bare. A unit that quotes
only another law gets that law's name in front: `Law 139/2025/QH15 Dieu 1`. A line before the first `Điều N.` has no article.

The script is deterministic and idempotent: a unit whose next non-blank, non-comment line is already an `@ref` is left alone,
so a second run changes nothing. It only ever adds lines, and every added line begins with `@ref `: it checks that, for each
file, before it writes anything, and writes nothing at all if any file fails (exit 1).

Modules are generated from templates/NAME.l4.in by tools/expand.py. So the same lines are added to the template, after the
`@@q` / `@@qa` / `@@qb` marker that emits the last quote line, and the script checks that the new template expands to exactly
the new module (and that the old one expanded to exactly the old module, or it refuses).

Inserting lines moves every line below them. `--line-map` records where, so that a citation of the form `module.l4:LINE`
written against the old modules can be rewritten: NEW = OLD + the number of recorded N below OLD.

Exit status: 0 done (unplaced units are reported, not an error), 1 refused, 2 usage.
"""
import bisect
import glob
import importlib.util
import os
import re
import sys
import unicodedata

sys.dont_write_bytecode = True  # importing the sibling tools must not leave .pyc files behind

HERE = os.path.dirname(os.path.abspath(__file__))
ROW = os.path.dirname(HERE)
RAW_DIR = os.path.normpath(os.path.join(ROW, "..", "..", "source", "raw"))
MAIN_RAW = "law08-2022-qh15"

# Raw lines a quote run may skip without the locator claiming a clause it leaves out: the gazette's running header
# (`CÔNG BÁO/Số 575 + 576/Ngày 17-7-2022`, with the page number before or after it) and a bare page number.
FURNITURE = re.compile(r"\s*(?:(?:\d+\s+)?CÔNG BÁO/Số [\d +]+/Ngày \d+-\d+-\d+(?:\s+\d+)?|\d+)\s*$")
# "Điều" precomposed (NFC), the form the quote lines are in; a heading may be preceded by the page number.
ARTICLE = re.compile(r"\s*(?:\d+\s+)?Điều\s+(\d+)\.")
STRUCTURE = re.compile(r"\s*(?:Chương|Mục|Phần)\s+[IVXLC0-9]+\s*$")
LAW_ID = re.compile(r"law(\d+)-(\d{4})-(qh\d+)$")
DECL_START = re.compile(r"(?:DECLARE|GIVEN|GIVETH|DECIDE|ASSUME)\b|`|@(?:desc|export)\b")


def load_sibling(name):
    spec = importlib.util.spec_from_file_location(name[:-3], os.path.join(HERE, name))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


srcrefs = load_sibling("srcrefs.py")


def nfc(s):
    return unicodedata.normalize("NFC", s)


def read_lines(path):
    with open(path, encoding="utf-8", newline="") as f:
        text = f.read()
    if "\r" in text:
        raise ValueError("carriage return in file; the script does not rewrite line endings")
    return text.split("\n")


def write_lines(path, lines):
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write("\n".join(lines))


def is_ref(line):
    """True if the line is nothing but an `@ref` annotation, as srcrefs.py reads it."""
    code, refs = srcrefs.scan_line(line, [])
    return bool(refs) and not code


def is_quote(line):
    return not is_ref(line) and bool(srcrefs.SRC_LINE.search(line))


def is_plain_comment(line):
    return line.lstrip().startswith("--") and not is_quote(line)


class Raws:
    """The raw files beside the main one: their lines, and which article each line lies in."""

    def __init__(self, raw_dir=RAW_DIR):
        self.dir = raw_dir
        self.lines = {}
        self.heads = {}

    def get(self, ident):
        key = ident or MAIN_RAW
        if key not in self.lines:
            self.lines[key] = read_lines(os.path.join(self.dir, key + ".txt"))
        return self.lines[key]

    def headings(self, ident):
        """[(line number, article number or None)] for every `Điều N.` heading and every Chương / Mục / Phần heading, in order."""
        key = ident or MAIN_RAW
        if key not in self.heads:
            out = []
            for n, line in enumerate(self.get(ident), 1):
                m = ARTICLE.match(nfc(line))
                if m:
                    out.append((n, int(m.group(1))))
                elif STRUCTURE.match(nfc(line)):
                    out.append((n, None))
            self.heads[key] = out
        return self.heads[key]

    def articles_in(self, ident, a, b):
        """The article numbers the raw lines a..b lie in, in order. A chapter or section heading is in no article."""
        hs = self.headings(ident)
        i = bisect.bisect_right([n for n, _ in hs], a) - 1
        found = [hs[i][1]] if i >= 0 and hs[i][1] is not None else []
        for n, num in hs[i + 1:]:
            if n > b:
                break
            if num is not None:
                found.append(num)
        return found

    def skips_text(self, ident, lo, hi):
        """True if raw lines lo..hi (1-based, inclusive) hold a line that is neither blank nor page furniture."""
        return any(s.strip() and not FURNITURE.match(s) for s in self.get(ident)[lo - 1 : hi])


def law_key(ident):
    """`law08-2022-qh15-577-578` (the second gazette issue of a law) is part of `law08-2022-qh15`."""
    return re.sub(r"(?:-\d+)+$", "", ident) if ident else MAIN_RAW


def law_name(ident):
    m = LAW_ID.match(law_key(ident))
    return f"Law {m.group(1)}/{m.group(2)}/{m.group(3).upper()}" if m else law_key(ident)


def article_label(numbers):
    """'Dieu 91-93' for 91, 92, 93; 'Dieu 5, 9' for 5, 9; 'Dieu 7' for 7. The numbers are sorted: a unit may quote out of order."""
    seen = sorted(set(numbers))
    parts, i = [], 0
    while i < len(seen):
        j = i
        while j + 1 < len(seen) and seen[j + 1] == seen[j] + 1:
            j += 1
        parts.append(str(seen[i]) if i == j else f"{seen[i]}-{seen[j]}")
        i = j + 1
    return "Dieu " + ", ".join(parts)


def label_for(quotes, raws):
    """The label of one unit, from the raw articles its quoted lines lie in; None if there is none."""
    own = [(i, a, b) for i, a, b in quotes if law_key(i) == MAIN_RAW]
    if own:
        nums = [n for i, a, b in own for n in raws.articles_in(i, a, b)]
        return article_label(nums) if nums else None
    first = law_key(quotes[0][0])
    nums = [n for i, a, b in quotes if law_key(i) == first for n in raws.articles_in(i, a, b)]
    return f"{law_name(quotes[0][0])} {article_label(nums)}" if nums else None


def locators(quotes, raws):
    """The locator texts for one unit: quotes is [(ident, a, b)] in file order."""
    stretches = []  # (first position in the unit, text)
    by_id = {}
    for pos, (ident, a, b) in enumerate(quotes):
        by_id.setdefault(ident, []).append((pos, a, b))
    for ident, items in by_id.items():
        tag = f"{ident}:" if ident else ""
        groups, cur = [], [items[0]]
        for prev, nxt in zip(items, items[1:]):
            if nxt[1] < prev[1] or (nxt[1] > prev[2] + 1 and raws.skips_text(ident, prev[2] + 1, nxt[1] - 1)):
                groups.append(cur)
                cur = []
            cur.append(nxt)
        groups.append(cur)
        for g in groups:
            lo, hi = min(a for _, a, _ in g), max(b for _, _, b in g)
            stretches.append((g[0][0], f"src:{tag}{lo}" if lo == hi else f"src:{tag}{lo}-{hi}"))
    return [text for _, text in sorted(stretches)]


def plan(lines, raws):
    """Decide what to insert into one module.

    Returns (inserts, unplaced, stats): inserts maps the index of the last quote line of a unit to the @ref line to add after
    it; unplaced is [(first line number, last line number, why, exempt)] (1-based); stats counts runs, units and label sources.
    """
    inserts, unplaced = {}, []
    stats = dict(runs=0, units=0, inserted=0, already=0, unplaced=0, mixed=0, split=0, labelled=0, unlabelled=0)
    n = len(lines)
    i = 0
    while i < n:
        if not is_quote(lines[i]):
            i += 1
            continue
        first, last, quotes, j = i, i, [], i
        while True:
            # one run, exactly as srcrefs.Scan reads it
            while j < n:
                s = lines[j]
                m = None if is_ref(s) else srcrefs.SRC_LINE.search(s)
                if m:
                    a = int(m.group(2))
                    quotes.append((m.group(1), a, int(m.group(3) or a)))
                    last = j
                elif s.strip():
                    break
                j += 1
            stats["runs"] += 1
            k = last + 1
            while k < n and (not lines[k].strip() or is_plain_comment(lines[k])):
                k += 1
            if k < n and is_quote(lines[k]):
                j = k  # separated from the next run by plain comments only: one unit
                continue
            break
        i = last + 1
        stats["units"] += 1
        if k < n and is_ref(lines[k]):
            stats["already"] += 1
            continue
        if k >= n or not DECL_START.match(lines[k]):
            why = "end of file" if k >= n else "next is " + lines[k].split()[0]
            exempt = k >= n or bool(srcrefs.UNREFERENCED_TERMINATOR.match(lines[k]))
            unplaced.append((first + 1, last + 1, why, exempt))
            stats["unplaced"] += 1
            continue
        locs = locators(quotes, raws)
        if len({q[0] for q in quotes}) > 1:
            stats["mixed"] += 1
        if len(locs) > len({q[0] for q in quotes}):
            stats["split"] += 1
        label = label_for(quotes, raws)
        stats["labelled" if label else "unlabelled"] += 1
        indent = re.match(r"\s*", lines[last]).group(0)
        body = "; ".join(locs)
        inserts[last] = f"{indent}@ref {label} ({body})" if label else f"{indent}@ref {body}"
        stats["inserted"] += 1
    return inserts, unplaced, stats


def apply_inserts(lines, inserts):
    out = []
    for idx, line in enumerate(lines):
        out.append(line)
        if idx in inserts:
            out.append(inserts[idx])
    return out


def pure_addition(old, new):
    """True if `new` is `old` plus lines that begin with '@ref ' (old is a subsequence of new, nothing else differs)."""
    i = 0
    added = 0
    for line in new:
        if i < len(old) and line == old[i]:
            i += 1
        elif line.lstrip().startswith("@ref "):
            added += 1
        else:
            return False
    return i == len(old) and len(new) - len(old) == added


def expand_lines(expand, tlines, path):
    """The module lines a template yields, and for each the index of the template line that emitted it (tools/expand.py's own rules)."""
    out, origin = [], []
    for t, line in enumerate(tlines):
        fx = expand.FX.match(line)
        if fx:
            got = expand.fixture(fx, path, t + 1)
        else:
            m = expand.MARK.match(line)
            if m:
                got = [m.group(1) + g for g in expand.quote(m.group(2), m.group(3), m.group(4))]
                if not got:
                    raise ValueError(f"{path}:{t + 1}: marker quotes no non-blank line")
            else:
                got = [line]
        out.extend(got)
        origin.extend([t] * len(got))
    return out, origin


def main(argv):
    argv = list(argv)
    dry = "--dry-run" in argv
    use_templates = "--no-templates" not in argv
    line_map = None
    if "--line-map" in argv:
        at = argv.index("--line-map")
        if at + 1 >= len(argv):
            print(__doc__, file=sys.stderr)
            return 2
        line_map = argv[at + 1]
        del argv[at : at + 2]
    bad = [a for a in argv if a not in ("--dry-run", "--no-templates")]
    if bad:
        print(__doc__, file=sys.stderr)
        return 2
    modules = sorted(glob.glob(os.path.join(ROW, "*.l4")))
    if not modules:
        print(f"switch_to_ref_locators: no .l4 modules in {ROW}", file=sys.stderr)
        return 2
    expand = load_sibling("expand.py") if use_templates else None
    raws = Raws()

    writes, refusals, reports, total, moved = [], [], [], {}, []
    for path in modules:
        name = os.path.basename(path)
        try:
            old = read_lines(path)
            inserts, unplaced, stats = plan(old, raws)
        except (OSError, UnicodeDecodeError, ValueError) as e:
            refusals.append(f"{name}: {e}")
            continue
        new = apply_inserts(old, inserts)
        if not pure_addition(old, new):
            refusals.append(f"{name}: the result is not the old file plus '@ref ' lines")
            continue
        for key, v in stats.items():
            total[key] = total.get(key, 0) + v
        reports.append((name, stats, unplaced))
        moved.extend((name, last + 1) for last in sorted(inserts))
        if new != old:
            writes.append((path, new))

        tpath = os.path.join(ROW, "templates", name + ".in")
        if use_templates and os.path.isfile(tpath):
            try:
                told = read_lines(tpath)
                got, origin = expand_lines(expand, told, tpath)
                if got != old:
                    refusals.append(f"templates/{name}.in does not expand to {name}: regenerate with tools/expand.py first, or pass --no-templates")
                    continue
                tins = {}
                for last, text in inserts.items():
                    t = origin[last]
                    if last + 1 < len(origin) and origin[last + 1] == t:
                        raise ValueError(f"line {last + 1} is not the last line its template line emits")
                    tins[t] = text
                tnew = apply_inserts(told, tins)
                if not pure_addition(told, tnew):
                    refusals.append(f"templates/{name}.in: the result is not the old file plus '@ref ' lines")
                    continue
                if expand_lines(expand, tnew, tpath)[0] != new:
                    refusals.append(f"templates/{name}.in: the new template does not expand to the new {name}")
                    continue
            except (OSError, UnicodeDecodeError, ValueError, SystemExit) as e:
                refusals.append(f"templates/{name}.in: {e}")
                continue
            if tnew != told:
                writes.append((tpath, tnew))

    if refusals:
        print("refused, nothing written:", file=sys.stderr)
        for r in refusals:
            print("  " + r, file=sys.stderr)
        return 1

    for name, s, unplaced in reports:
        print(f"{name}: {s['runs']} runs in {s['units']} units; {s['inserted']} @ref added, {s['already']} already had one, {s['unplaced']} unplaced")
    t = total
    print(f"TOTAL: {t['runs']} runs in {t['units']} units; {t['inserted']} @ref added, {t['already']} already had one, {t['unplaced']} unplaced")
    print(f"labels on the added lines: {t['labelled']} from the raw articles, {t['unlabelled']} none")
    print(f"added lines carrying locators for two raw files: {t['mixed']}; carrying more than one locator for one raw file: {t['split']}")
    if t["unplaced"]:
        print(f"unplaced units ({t['unplaced']}): no @ref directly above a declaration is allowed, so none was added")
        for name, _, unplaced in reports:
            for first, last, why, exempt in unplaced:
                print(f"  {name}:{first}-{last}: {why}; " + ("the gate exempts it" if exempt else "the gate will report it as an orphan quotation"))
    if dry:
        print("dry run: nothing written")
        return 0
    for path, lines in writes:
        write_lines(path, lines)
    if line_map:
        with open(line_map, "w", encoding="utf-8", newline="") as f:
            f.write("".join(f"{name}\t{after}\n" for name, after in moved))
    print(f"wrote {len(writes)} files" + (f" and the line map {line_map}" if line_map else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
