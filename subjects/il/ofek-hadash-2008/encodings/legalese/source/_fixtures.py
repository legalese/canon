# The worked cases, emitted into the generated module.
#
# WHY EVERY FIXTURE IS INLINED into the helper its directive names, instead of
# being written once and reused. `l4 catala` collects helpers in a SINGLE pass
# outward from the @export-annotated decision: a helper that calls another
# helper which is not itself in that closure is dropped, and its directive
# never becomes a Catala `#[test]` scope. The diagnostic names the head of the
# application rather than the dependency that was missed, which is why this
# took a bisect to find. Inlining the record keeps each question helper's only
# callee inside the exported closure, and every directive lowers.
# Measured; NOTES.md section 7 carries the minimal repro.
#
# Imported by build-catala-module.py, which supplies `w` (the line emitter).

FIXTURES = [
    ('Yael', dict(
        qual='academic — holds a recognised first degree', seniority=11, rank=4,
        stage='a junior high school', post='1',
        first='JUST `homeroom teacher of a class other than the first grade`',
        second='NOTHING', classes=0, units=0,
        gloss='a junior-high homeroom teacher, eleven years in, on a full post')),
    ('Dvora', dict(
        qual='academic — holds a recognised second degree', seniority=30, rank=8,
        stage='a primary school', post='1',
        first='JUST `homeroom teacher of a first-grade class`',
        second='JUST `subject coordinator`', classes=0, units=3,
        gloss='a primary-school teacher at the top of the table, holding two '
              'role supplements and three school-role units')),
    ('Noa', dict(
        qual='academic — holds a doctorate', seniority=6, rank=3,
        stage='a junior high school', post='50%',
        first='NOTHING', second='NOTHING', classes=0, units=0,
        gloss='a doctorate holder on half a post')),
    ('Yael on half a post', dict(
        qual='academic — holds a recognised first degree', seniority=11, rank=4,
        stage='a junior high school', post='50%',
        first='JUST `homeroom teacher of a class other than the first grade`',
        second='NOTHING', classes=0, units=0,
        gloss='Yael again, with one field changed: half a post')),
]

# (helper prefix, the function in the exported closure it calls, trailing args)
# Every question goes through the ONE exported decision, and does so because
# it must: `l4 catala` collects a directive's helper only when that helper
# calls the FIRST @export-annotated decision directly. Adding a second @export
# does not widen the closure — it emits a scope call inside a toplevel
# definition, which `catala typecheck` rejects outright with "Scope calls are
# not allowed outside of a scope". Both were measured; NOTES.md section 7 has
# the repros.
QUESTIONS = [
    ('the pay of', '`the monthly pay of`', ' 0'),
    ('the pay having advanced of', '`the monthly pay of`', ' 130'),
]

ASSERTIONS = """-- The reduction of section 9 is nil outside its two windows, so the September
-- 2024 figures below are the GROSS pay — the same figures ofek-cases.l4
-- asserts against the eight-module encoding.
#ASSERT `the pay of Yael on` (YMD 2024 9 1) EQUALS 11_008.03
#ASSERT `the pay of Dvora on` (YMD 2024 9 1) EQUALS 18_300.49575
#ASSERT `the pay of Noa on` (YMD 2024 9 1) EQUALS 5_000.9875

-- The 0.95% of section 9(a) and the 1.2% of section 9(b), on Yael.
#ASSERT `the pay of Yael on` (YMD 2025 11 1) EQUALS 10_903.453715
#ASSERT `the pay of Yael on` (YMD 2026 3 1) EQUALS 10_875.93364

-- Section 16 stacks a withheld seniority step on top of section 9 for four
-- months, and then stops: from January 2026 the step is hers to keep.
#ASSERT `the pay having advanced of Yael on` (YMD 2025 11 1) EQUALS 10_773.453715
#ASSERT `the pay having advanced of Yael on` (YMD 2026 3 1) EQUALS 10_875.93364

-- Dvora: the section 22 school-role supplement is worth 600 from 1.9.2026 and
-- nothing before it, having been postponed a year by section 19 of the 2026
-- agreement. 18,900.50 gross becomes 18,673.69 after the 1.2%.
#ASSERT `the pay of Dvora on` (YMD 2026 10 1) EQUALS 18_673.689801

-- And the result the whole encoding exists to make visible: half a post is
-- not half the pay, because section 39(b) pays the role supplement whole.
#ASSERT `the pay of Yael on half a post on` (YMD 2024 9 1) EQUALS 6_004.38"""


def record(f):
    """The teacher, as ONE line.

    A record spread over several lines does parse as a definition's body, but
    not as a parenthesised ARGUMENT: the layout parser stops at the opening
    bracket. Since this file is generated, a long line costs nothing.
    """
    fields = ', '.join([
        f"`qualification` IS `{f['qual']}`",
        f"`seniority in years` IS {f['seniority']}",
        f"`rank` IS {f['rank']}",
        f"`stage of education` IS `{f['stage']}`",
        f"`fraction of a full post` IS {f['post']}",
        f"`first role` IS {f['first']}",
        f"`second role` IS {f['second']}",
        f"`classes in the coordinated grade level` IS {f['classes']}",
        f"`units of the school-role supplement` IS {f['units']}",
    ])
    return f'(`a teacher` WITH {fields})'


def emit(w):
    w('-- These are the fixtures of ofek-cases.l4 and the figures it asserts.')
    w('-- They tie this generated module to the eight-module encoding: the two')
    w('-- were derived independently from the corpus, and they must agree here.')
    w('--')
    w('-- Each fixture is written out once per question rather than named and')
    w('-- reused. That is not redundancy for its own sake: `l4 catala` collects')
    w('-- helpers in a single pass out from the exported decision, so a helper')
    w('-- that calls an uncollected helper is dropped along with its directive.')
    w('-- Inlining keeps every callee inside the exported closure. See')
    w('-- NOTES.md section 7.')
    w()
    for name, f in FIXTURES:
        w(f"-- {name} — {f['gloss']}.")
        for prefix, callee, extra in QUESTIONS:
            w('GIVEN `the date` IS A DATE')
            w('GIVETH A NUMBER')
            w(f'`{prefix} {name} on` `the date`')
            w(f'    MEANS {callee} {record(f)} `the date`{extra}')
            w()
    w(ASSERTIONS)
