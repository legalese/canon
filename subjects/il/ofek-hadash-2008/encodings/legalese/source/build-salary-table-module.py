"""Generate ofek-salary-table.l4 — the two combined-salary tables, as L4.

The 648 amounts come from source/tables.py, which parses the follow-up
committee's corrected agorot appendices of 14 January 2025. The layout comes
from source/_tablefmt.py, which build-catala-module.py also uses, so the two
renderings of the same grid cannot drift in layout.

The prose around the tables lives in this file rather than beside the L4,
because a generated file that is half hand-edited is a file nobody dares
regenerate.

Run:  OFEK_CORPUS=<checkout> python3 source/build-salary-table-module.py > ofek-salary-table.l4
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _tablefmt  # noqa: E402
import tables  # noqa: E402

ROOT = tables.corpus_root(sys.argv)
D = tables.load(ROOT)
MARGINS, RANK_STEP = tables.margins_from_shekel_printing(ROOT)
N = tables.l4num
OUT = []


def w(s=''):
    OUT.append(s)


w('''IMPORT prelude
IMPORT `ofek-domain`

§ `The combined salary tables`

-- ===========================================================================
-- GENERATED FILE — do not edit by hand.
--   source/build-salary-table-module.py, from the grids parsed by
--   source/tables.py and laid out by source/_tablefmt.py. Regenerate with
--     OFEK_CORPUS=<checkout> python3 source/build-salary-table-module.py > ofek-salary-table.l4
--
-- THE COMBINED SALARY TABLE (tavlat ha-sachar ha-meshulav), § 35 of the 2008
-- agreement as replaced from 1 September 2022 by § 4.1 of the collective
-- agreement of 19 October 2022.
--
-- WHICH PRINTING IS AUTHORITATIVE. The 2022 agreement attached its tables
-- rounded to the SHEKEL. A decision of the joint follow-up committee (vaadat
-- maakav) of 14 January 2025 corrected a scribal error in that agreement and
-- REPLACED appendices alef-1 and alef-2 with tables to the AGORA, effective
-- from the same 1 September 2022. The agorot tables are therefore the text in
-- force for the whole period, and they are what this module encodes:
--   /agreements/ofek-hadash/2025-01-14_ofek-hadash_vaadat-maakev_taut-sofer-correction_agorot-salary-tables.html
-- The shekel printing at /tables/2022-09-01_ofek-hadash_salary-table_BA.html
-- and its MA sibling round these figures and are otherwise identical; they are
-- what a reader is most likely to find first, which is why the difference is
-- stated here.
--
-- WHAT THE TABLE IS. Rows are SENIORITY (vetek, § 37), 1 to 36. Columns are
-- RANK (darga, §§ 36 and 38), 1 to 9. A cell is the monthly combined salary in
-- new shekels for a FULL post; § 33 and the 2022 agreement § 5.3 pro-rate it
-- for a part post.
--
-- THE MERGED CELLS. The table does not give 324 distinct numbers. It gives
-- 224, and the shekel printing spreads each across the ranks to its right as a
-- merged cell: at seniority 3 it prints one figure under rank 1 and another
-- spanning ranks 2 to 9. This module reproduces that — the last defined value
-- is repeated into each rank beyond it — and records the frontier separately
-- below, because the frontier is the part a reader can check against § 38.
-- The agorot printing and the 1.1.2015 tables leave the very same positions
-- BLANK instead of merging them, which is why NOTES.md § 5 treats "what a
-- merged cell means" as an open question of construction rather than a settled
-- reading.
--
-- HOW TO READ THE TWO TABLES BELOW. Each is a decision table, one row per
-- seniority. The record is built positionally with `OF`, so the rank is
-- carried by the column rather than by a repeated field name, and the ruler
-- comment above each table names those columns once. The guard subject, THEN,
-- the constructor and OF are written on the first row and dittoed with `^`
-- after it — a caret is the token at that column on the line above. What is
-- left on a row is what varies: the seniority, and nine amounts.
-- ===========================================================================

§§ `A row of the table`

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
    -- Ranks run 1 to 9 (§ 38). A rank below 1 reads the first column and a
    -- rank above 9 the last; neither is reachable through § 38, and the
    -- placement module refuses such a rank before this is ever called.
    -- A backtick identifier is ONE token, so the field names cannot be
    -- dittoed away; the record and its genitive can.
    BRANCH IF `the rank` AT MOST 1 THEN `the row`'s `at rank 1`
           IF ^          EQUALS  2 ^    ^        ^  `at rank 2`
           IF ^          EQUALS  3 ^    ^        ^  `at rank 3`
           IF ^          EQUALS  4 ^    ^        ^  `at rank 4`
           IF ^          EQUALS  5 ^    ^        ^  `at rank 5`
           IF ^          EQUALS  6 ^    ^        ^  `at rank 6`
           IF ^          EQUALS  7 ^    ^        ^  `at rank 7`
           IF ^          EQUALS  8 ^    ^        ^  `at rank 8`
           OTHERWISE                    ^        ^  `at rank 9`

§§ `Appendix alef-1 — the BA table, rating code 101`
''')

for line in _tablefmt.signature('the BA table row at seniority', 'BA (rating code 101)'):
    w(line)
for line in _tablefmt.rows(D['BA'], N):
    w(line)

w()
w('§§ `Appendix alef-2 — the MA table, rating code 102`')
w()
for line in _tablefmt.signature('the MA table row at seniority', 'MA (rating code 102)'):
    w(line)
for line in _tablefmt.rows(D['MA'], N):
    w(line)

w(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '_salary-table-tail.l4'),
       encoding='utf8').read().rstrip('\n'))

sys.stdout.write('\n'.join(OUT) + '\n')
