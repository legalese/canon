"""Generate ofek-catala.l4 — the single-module rendering that `l4 catala` compiles.

WHY THIS EXISTS. `l4 catala` compiles ONE module: a reference into an imported
module is rejected as unbound, and a type declared in an imported module is
reported as outside the v1 fragment. The eight-module encoding beside this
script is therefore not compilable as it stands, and flattening it by hand
would create a second copy of every number, drifting from the first the moment
either is corrected.

So the flattened module is GENERATED, and generated from the SAME corpus parse
that produced the tables in ofek-salary-table.l4 — source/tables.py, reading the
follow-up committee's corrected appendices of 14 January 2025. Neither file is
copied from the other; both are derived from the source documents. The two are
then tied together by assertions: the worked figures at the foot of the emitted
module are the figures ofek-cases.l4 asserts, so if the two encodings ever
diverge, one of them goes red.

Run:  OFEK_CORPUS=<checkout> python3 source/build-catala-module.py > ofek-catala.l4
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tables  # noqa: E402
import _fixtures  # noqa: E402

ROOT = tables.corpus_root(sys.argv)
D = tables.load(ROOT)
N = tables.l4num
OUT = []


def w(s=''):
    OUT.append(s)


def branch_over_rank(values, indent, fmt=N):
    """A nine-armed BRANCH on `the rank`, ranks 1..9."""
    pad = ' ' * indent
    for i, v in enumerate(values, start=1):
        head = 'BRANCH ' if i == 1 else '       '
        if i == 1:
            w(f'{pad}{head}IF `the rank` AT MOST 1 THEN {fmt(v)}')
        elif i < 9:
            w(f'{pad}{head}IF `the rank` EQUALS {i}  THEN {fmt(v)}')
        else:
            w(f'{pad}{head}OTHERWISE                    {fmt(v)}')


def table_rows(grid, name, label):
    w('GIVEN `the seniority` IS A NUMBER')
    w('GIVETH A `a row of the combined salary table`')
    w(f'`{name}` `the seniority`')
    w(f'    @nlg the row of the {label} table at the given seniority')
    w('    MEANS')
    for v in range(1, 37):
        lit = ', '.join(f'`at rank {d}` IS {N(grid[(v, d)])}' for d in range(1, 10))
        lead = '    BRANCH ' if v == 1 else '           '
        if v == 1:
            cond = 'IF `the seniority` AT MOST 1  THEN'
        elif v < 36:
            cond = f'IF `the seniority` EQUALS {v:<2}   THEN'
        else:
            cond = 'OTHERWISE                         '
        w(f'{lead}{cond} `a row of the combined salary table` WITH {lit}')


w('''IMPORT prelude
IMPORT daydate

§ `Ofek Hadash — the pay computation, in one module`

-- ===========================================================================
-- GENERATED FILE — do not edit by hand.
--   source/build-catala-module.py, from the corpus grids parsed by
--   source/tables.py. Regenerate with
--     OFEK_CORPUS=<checkout> python3 source/build-catala-module.py > ofek-catala.l4
--
-- WHAT IT IS FOR. `l4 catala` compiles a SINGLE module: a reference into an
-- imported module is rejected as unbound, and a type declared elsewhere is
-- reported as outside the v1 fragment. The eight-module encoding beside this
-- file is therefore not compilable as it stands. This module is that encoding
-- flattened to the Catala v1 fragment, and it is what catala/ was compiled
-- from.
--
-- IT IS NOT A COPY. It is generated from the same corpus parse that produced
-- ofek-salary-table.l4 — the follow-up committee's corrected appendices of
-- 14 January 2025 — so neither file is derived from the other and a number
-- cannot drift between them without drifting from the source document. The
-- worked figures asserted at the foot of this module are the same figures
-- ofek-cases.l4 asserts against the eight-module encoding, so if the two ever
-- disagree, one of them goes red.
--
-- WHAT IT LEAVES OUT, and why. The Catala v1 fragment takes constitutive
-- rules — records, enums, first-order functions, CONSIDER/BRANCH/IF/WHERE
-- over booleans, numbers, dates and lists. It does not take deontic or
-- regulative material, and it is a decision core rather than the whole
-- encoding. So this module carries the COMPUTATION of pay and omits:
--   * the § 38 promotion machinery, whose quota rule is a fact about the
--     national establishment rather than about a teacher (ofek-placement.l4);
--   * the §§ 14-33 working-week patterns, other than the § 31 hourly value,
--     which is what pay actually reads (ofek-worktime.l4);
--   * the § 39(c) two-supplement cap, which is a constraint on the input and
--     not a step in the arithmetic.
-- Those live in the eight-module encoding and are checked there. NOTES.md § 7
-- carries the full account.
--
-- ONE MODELLING DIFFERENCE, stated plainly. The eight-module encoding gives a
-- teacher a LIST of roles and sums over it. Here a teacher has a first and a
-- second role, each a MAYBE. That is not a workaround: § 39(c) caps a teacher
-- at two role supplements without the district director\'s approval, so two
-- slots is the shape of the section. It also keeps the module inside the
-- fragment without a list fold. A teacher holding a third approved supplement
-- cannot be expressed here, and NOTES.md § 7 records that as the cost.
-- ===========================================================================

§§ `Who the teacher is`

DECLARE `a teaching qualification` IS ONE OF
    `academic — holds a recognised first degree`
    `academic — holds a recognised second degree`
    `academic — holds a doctorate`
    `certified but not academic`
    `senior certified but not academic`
    `unqualified`

DECLARE `a salary table` IS ONE OF
    `the BA table — rating code 101`
    `the MA table — rating code 102`

DECLARE `a stage of education` IS ONE OF
    `a primary school`
    `a junior high school`

DECLARE `a role carrying a supplement` IS ONE OF
    `homeroom teacher of a class other than the first grade`
    `homeroom teacher of a first-grade class`
    `subject coordinator`
    `road-safety coordinator`
    `security coordinator`
    `social-education coordinator`
    `grade-level coordinator`
    `laboratory coordinator`
    `assessment and measurement coordinator`

DECLARE `a teacher` HAS
    `qualification`             IS A `a teaching qualification`
    `seniority in years`        IS A NUMBER
    `rank`                      IS A NUMBER
    `stage of education`        IS A `a stage of education`
    `fraction of a full post`   IS A NUMBER
    `first role`                IS A MAYBE `a role carrying a supplement`
    `second role`               IS A MAYBE `a role carrying a supplement`
    `classes in the coordinated grade level` IS A NUMBER
    `units of the school-role supplement`    IS A NUMBER

-- § 36(c)-(d) of the 2008 agreement: a first degree to the first-degree table,
-- a second degree or a doctorate to the second-degree table.
GIVEN `the teacher` IS A `a teacher`
GIVETH A `a salary table`
`the table the teacher is placed in` `the teacher`
    @nlg the salary table the teacher is placed in
    MEANS
    CONSIDER `the teacher`\'s `qualification`
    WHEN `academic — holds a recognised first degree`  THEN `the BA table — rating code 101`
    WHEN `academic — holds a recognised second degree` THEN `the MA table — rating code 102`
    WHEN `academic — holds a doctorate`                THEN `the MA table — rating code 102`
    OTHERWISE                                          `the BA table — rating code 101`

GIVEN `the teacher` IS A `a teacher`
GIVETH A BOOLEAN
DECIDE `the teacher holds a doctorate` IF
    CONSIDER `the teacher`\'s `qualification`
    WHEN `academic — holds a doctorate` THEN TRUE
    OTHERWISE                           FALSE

§§ `The combined salary table`

-- §§ 35 of the 2008 agreement, as replaced from 1.9.2022 by § 4.1 of the 2022
-- wage agreement and reissued to the agora on 14.1.2025. Rows are seniority
-- 1..36, columns rank 1..9; beyond the frontier the last printed value
-- repeats, exactly as the shekel printing renders it with merged cells.

DECLARE `a row of the combined salary table` HAS
    `at rank 1` IS A NUMBER
    `at rank 2` IS A NUMBER
    `at rank 3` IS A NUMBER
    `at rank 4` IS A NUMBER
    `at rank 5` IS A NUMBER
    `at rank 6` IS A NUMBER
    `at rank 7` IS A NUMBER
    `at rank 8` IS A NUMBER
    `at rank 9` IS A NUMBER

GIVEN `the row` IS A `a row of the combined salary table`
      `the rank` IS A NUMBER
GIVETH A NUMBER
`the amount in the row at rank` `the row` `the rank`
    @nlg the amount in the row at the given rank
    MEANS
    BRANCH IF `the rank` AT MOST 1 THEN `the row`\'s `at rank 1`
           IF `the rank` EQUALS 2  THEN `the row`\'s `at rank 2`
           IF `the rank` EQUALS 3  THEN `the row`\'s `at rank 3`
           IF `the rank` EQUALS 4  THEN `the row`\'s `at rank 4`
           IF `the rank` EQUALS 5  THEN `the row`\'s `at rank 5`
           IF `the rank` EQUALS 6  THEN `the row`\'s `at rank 6`
           IF `the rank` EQUALS 7  THEN `the row`\'s `at rank 7`
           IF `the rank` EQUALS 8  THEN `the row`\'s `at rank 8`
           OTHERWISE                    `the row`\'s `at rank 9`
''')

w('§§ `Appendix alef-1 — the BA table, rating code 101`')
w()
table_rows(D['BA'], 'the BA table row at seniority', 'BA (rating code 101)')
w()
w('§§ `Appendix alef-2 — the MA table, rating code 102`')
w()
table_rows(D['MA'], 'the MA table row at seniority', 'MA (rating code 102)')
w('''
§§ `Reading a cell`

GIVEN `the table` IS A `a salary table`
      `the seniority` IS A NUMBER
      `the rank` IS A NUMBER
GIVETH A NUMBER
`the combined salary for a full post` `the table` `the seniority` `the rank`
    @nlg the combined salary for a full post at the given seniority and rank
    MEANS
    CONSIDER `the table`
    WHEN `the BA table — rating code 101` THEN
        `the amount in the row at rank` (`the BA table row at seniority` `the seniority`) `the rank`
    WHEN `the MA table — rating code 102` THEN
        `the amount in the row at rank` (`the MA table row at seniority` `the seniority`) `the rank`

§§ `Tosefet Ofek 2022`

-- § 5 of the 2022 wage agreement: a flat shekel amount by rank, falling as the
-- rank rises and nil at rank 9. Appendix bet ran from 1.9.2022; appendix
-- gimel doubled it from 1.9.2023 — the date the 2022 agreement misprinted as
-- 1.1.23 and the 14.1.2025 decision corrected.
GIVETH A DATE
`the date tosefet ofek 2022 takes effect` MEANS YMD 2022 9 1
GIVETH A DATE
`the date tosefet ofek 2022 is increased` MEANS YMD 2023 9 1
''')

for era, dlabel in ((2022, 'september 2022'), (2023, 'september 2023')):
    w('GIVEN `the table` IS A `a salary table`')
    w('      `the rank` IS A NUMBER')
    w('GIVETH A NUMBER')
    w(f'`tosefet ofek 2022 from {dlabel} in` `the table` `the rank`')
    w(f'    @nlg Tosefet Ofek 2022 as it stood from {dlabel}, at the given rank')
    w('    MEANS')
    w('    CONSIDER `the table`')
    w('    WHEN `the BA table — rating code 101` THEN')
    branch_over_rank(D['tosefet'][('BA', era)], 8)
    w('    WHEN `the MA table — rating code 102` THEN')
    branch_over_rank(D['tosefet'][('MA', era)], 8)
    w()

w('''GIVEN `the table` IS A `a salary table`
      `the rank` IS A NUMBER
      `the fraction of a full post` IS A NUMBER
      `the date` IS A DATE
GIVETH A NUMBER
`tosefet ofek 2022 for` `the table` `the rank` `the fraction of a full post` `the date`
    @nlg Tosefet Ofek 2022 payable at the given rank
    MEANS
    -- § 5.3 pro-rates it, unlike a § 39 role supplement.
    IF `the date` LESS THAN `the date tosefet ofek 2022 takes effect`
        THEN 0
        ELSE `the amount at the date` TIMES `the fraction of a full post`
    WHERE
        `the amount at the date` MEANS
            IF `the date` LESS THAN `the date tosefet ofek 2022 is increased`
                THEN `tosefet ofek 2022 from september 2022 in` `the table` `the rank`
                ELSE `tosefet ofek 2022 from september 2023 in` `the table` `the rank`

§§ `The role supplements`

-- § 39(a) of the 2008 agreement as percentages, with the shekel floors § 10
-- of the 2022 agreement put under two of them from 1.9.2023.
GIVETH A DATE
`the date the shekel floors take effect` MEANS YMD 2023 9 1
GIVETH A NUMBER
`the floor under the homeroom supplement` MEANS 1_000
GIVETH A NUMBER
`the floor under the grade coordinator supplement` MEANS 1_100
GIVETH A NUMBER
`the smallest post that carries a role supplement` MEANS 1 DIVIDED BY 3

GIVEN `the role` IS A `a role carrying a supplement`
      `the stage` IS A `a stage of education`
      `the classes in the grade` IS A NUMBER
GIVETH A NUMBER
`the section 39 rate for` `the role` `the stage` `the classes in the grade`
    @nlg the section 39 rate for the given role
    MEANS
    CONSIDER `the role`
    WHEN `homeroom teacher of a class other than the first grade` THEN 10%
    WHEN `homeroom teacher of a first-grade class`                THEN 11.5%
    WHEN `subject coordinator` THEN
        CONSIDER `the stage`
        WHEN `a primary school`     THEN 6%
        WHEN `a junior high school` THEN 8%
    WHEN `road-safety coordinator`  THEN 6%
    WHEN `security coordinator`     THEN 6%
    WHEN `social-education coordinator` THEN
        CONSIDER `the stage`
        WHEN `a primary school`     THEN 6%
        WHEN `a junior high school` THEN 10%
    WHEN `grade-level coordinator` THEN
        IF `the classes in the grade` AT MOST 4 THEN 7% ELSE 6%
    WHEN `laboratory coordinator`                 THEN 3%
    WHEN `assessment and measurement coordinator` THEN 6%

GIVEN `the role` IS A `a role carrying a supplement`
GIVETH A NUMBER
`the shekel floor under` `the role`
    @nlg the shekel floor under the given role
    MEANS
    CONSIDER `the role`
    WHEN `homeroom teacher of a class other than the first grade` THEN `the floor under the homeroom supplement`
    WHEN `homeroom teacher of a first-grade class`                THEN `the floor under the homeroom supplement`
    WHEN `grade-level coordinator`                                THEN `the floor under the grade coordinator supplement`
    OTHERWISE                                                          0

GIVEN `the role` IS A `a role carrying a supplement`
      `the stage` IS A `a stage of education`
      `the classes in the grade` IS A NUMBER
      `the base` IS A NUMBER
      `the date` IS A DATE
GIVETH A NUMBER
`the role supplement for` `the role` `the stage` `the classes in the grade` `the base` `the date`
    @nlg the supplement payable for the given role
    MEANS
    IF `the date` LESS THAN `the date the shekel floors take effect`
        THEN `the percentage amount`
        ELSE max `the percentage amount` (`the shekel floor under` `the role`)
    WHERE
        `the percentage amount` MEANS
            `the base` TIMES (`the section 39 rate for` `the role` `the stage` `the classes in the grade`)

§§ `The school-role supplement`

-- § 22 of the 2022 agreement, as postponed to the 2026/27 school year by § 19
-- of the approved agreement of 29.6.2026. Two to five whole units at 200 a
-- month, paid flat to any post of a third or more.
GIVETH A NUMBER
`the value of one school-role unit` MEANS 200
GIVETH A DATE
`the date section 22 takes effect as postponed` MEANS YMD 2026 9 1

GIVEN `the units` IS A NUMBER
      `the fraction of a full post` IS A NUMBER
      `the date` IS A DATE
GIVETH A NUMBER
`the school-role supplement for` `the units` `the fraction of a full post` `the date`
    @nlg the school-role supplement for the given units
    MEANS
    IF      `the date` LESS THAN `the date section 22 takes effect as postponed`
         OR `the units` BELOW 2
         OR `the units` ABOVE 5
         OR `the fraction of a full post` BELOW `the smallest post that carries a role supplement`
        THEN 0
        ELSE `the units` TIMES `the value of one school-role unit`

§§ `The 2025-2026 wage reduction`

-- §§ 9 and 16 of the approved collective agreement of 29 June 2026, made
-- under Chapter 9 of the Budget Objectives Act 5785-2025.
GIVETH A DATE
`the first day of the first reduction period` MEANS YMD 2025 5 1
GIVETH A DATE
`the last day of the first reduction period` MEANS YMD 2025 12 31
GIVETH A DATE
`the last day of the second reduction period` MEANS YMD 2026 12 31
GIVETH A DATE
`the first month the seniority step is withheld` MEANS YMD 2025 9 1
GIVETH A DATE
`the last month the seniority step is withheld` MEANS YMD 2025 12 31

GIVEN `the date` IS A DATE
GIVETH A NUMBER
`the reduction rate on` `the date`
    @nlg the wage reduction rate applying on the given date
    MEANS
    BRANCH IF `the date` LESS THAN `the first day of the first reduction period` THEN 0
           IF `the date` AT MOST `the last day of the first reduction period` THEN 0.95%
           IF `the date` AT MOST `the last day of the second reduction period` THEN 1.2%
           OTHERWISE                                                               0

GIVEN `the value of the seniority step` IS A NUMBER
      `the date` IS A DATE
GIVETH A NUMBER
`the section 16 withholding on` `the value of the seniority step` `the date`
    @nlg the section 16 withholding of the given seniority step
    MEANS
    IF      NOT (`the date` LESS THAN `the first month the seniority step is withheld`)
        AND `the date` AT MOST `the last month the seniority step is withheld`
        THEN `the value of the seniority step`
        ELSE 0

§§ `The month`

-- § 39(b) read with 2022 § 5.4: the base for a percentage supplement is the
-- FULL-POST combined salary plus the FULL-POST Tosefet Ofek 2022.
GIVEN `the teacher` IS A `a teacher`
      `the date` IS A DATE
GIVETH A NUMBER
`the full-post percentage base for` `the teacher` `the date`
    @nlg the full-post base on which percentage supplements are computed
    MEANS
          `the combined salary for a full post` `the table` (`the teacher`\'s `seniority in years`) (`the teacher`\'s `rank`)
    PLUS  `tosefet ofek 2022 for` `the table` (`the teacher`\'s `rank`) 1 `the date`
    WHERE
        `the table` MEANS `the table the teacher is placed in` `the teacher`

GIVEN `the teacher` IS A `a teacher`
      `the date` IS A DATE
GIVETH A NUMBER
`the combined salary payable to` `the teacher` `the date`
    @nlg the combined salary payable to the teacher
    MEANS
    `the combined salary for a full post`
        (`the table the teacher is placed in` `the teacher`)
        (`the teacher`\'s `seniority in years`)
        (`the teacher`\'s `rank`)
    TIMES `the teacher`\'s `fraction of a full post`

-- One role slot, or nothing if the slot is empty or the post is too small for
-- § 39(b) to carry a supplement at all.
GIVEN `the teacher` IS A `a teacher`
      `the slot` IS A MAYBE `a role carrying a supplement`
      `the date` IS A DATE
GIVETH A NUMBER
`the supplement for one slot of` `the teacher` `the slot` `the date`
    @nlg the supplement payable for one role slot
    MEANS
    IF `the teacher`\'s `fraction of a full post` BELOW `the smallest post that carries a role supplement`
        THEN 0
        ELSE CONSIDER `the slot`
             WHEN NOTHING THEN 0
             WHEN JUST `the role` THEN
                 `the role supplement for`
                     `the role`
                     (`the teacher`\'s `stage of education`)
                     (`the teacher`\'s `classes in the coordinated grade level`)
                     (`the full-post percentage base for` `the teacher` `the date`)
                     `the date`

GIVEN `the teacher` IS A `a teacher`
      `the date` IS A DATE
GIVETH A NUMBER
`the monthly pay before the reduction for` `the teacher` `the date`
    @nlg the monthly pay of the teacher before the 2025-2026 reduction
    MEANS
          `the combined salary payable to` `the teacher` `the date`
    PLUS  (`tosefet ofek 2022 for`
              (`the table the teacher is placed in` `the teacher`)
              (`the teacher`\'s `rank`)
              (`the teacher`\'s `fraction of a full post`)
              `the date`)
    PLUS  (IF `the teacher holds a doctorate` `the teacher`
              THEN (`the combined salary payable to` `the teacher` `the date`) TIMES 5%
              ELSE 0)
    PLUS  `the supplement for one slot of` `the teacher` (`the teacher`\'s `first role`) `the date`
    PLUS  `the supplement for one slot of` `the teacher` (`the teacher`\'s `second role`) `the date`
    PLUS  `the school-role supplement for`
              (`the teacher`\'s `units of the school-role supplement`)
              (`the teacher`\'s `fraction of a full post`)
              `the date`

@export Compute the monthly pay of an Israeli teacher employed on Ofek Hadash terms — the combined salary from the 2022 table, Tosefet Ofek 2022, the doctorate and role supplements and the school-role supplement, net of the 2025-2026 wage reduction
GIVEN `the teacher` IS A `a teacher`
      @desc The teacher: qualification, seniority in years, rank 1 to 9, primary or junior high, the fraction of a full post (1 for a whole post), up to two role supplements, the classes in any grade they coordinate, and the units of school-role supplement allotted to them
      `the date` IS A DATE
      @desc The month being computed. The 2025-2026 reduction, the Tosefet Ofek increase of 1.9.2023, the shekel floors of 1.9.2023 and the school-role supplement start of 1.9.2026 all turn on it
      `the value of any seniority step taken in september 2025` IS A NUMBER
      @desc The monthly value of the seniority advancement this teacher became entitled to in the September 2025 salary, which section 16 of the 2026 agreement withholds from September to December 2025. Zero if they did not advance
GIVETH A NUMBER
`the monthly pay of` `the teacher` `the date` `the value of any seniority step taken in september 2025`
    @nlg the monthly pay of the teacher
    MEANS
          `the monthly pay before the reduction for` `the teacher` `the date`
    MINUS (`the monthly pay before the reduction for` `the teacher` `the date` TIMES (`the reduction rate on` `the date`))
    MINUS (`the section 16 withholding on` `the value of any seniority step taken in september 2025` `the date`)

§§ `The same three teachers, and the same answers`
''')

_fixtures.emit(w)

sys.stdout.write('\n'.join(OUT) + '\n')
