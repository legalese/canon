# IL-04 independent test findings

Author: fid-il-04, independent test author (one session, no sub-agents), 2026-10-06.
Files: `DECIDED-ANSWERS.md` (the answers, decided from the Hebrew source and finished at 14:53:53 UTC before any `.l4` file, `NOTES.md`, `encoding.json`, `check.sh` or `tools/` of this encoding was opened), `tests-independent.l4` (those answers, asserted through the encoding's interface).

## What `check.sh` prints

Run in a scratch copy of this directory with `L4=/Users/mengwong/.local/bin/l4`, `JL4_LIBRARY_PATH` unset, after `tests-independent.l4` was added:

```
module                                    errors satisfied  failed  refused  expected
nii-il04-tests-expected-red.l4                14        26      14        0        14
nii-il04-tests.l4                              0       120       0        0         0
tests-independent.l4                           1       645       1        0         0
TOTAL (10 modules)                            15       791      15        0
```

(Modules with no assertions omitted; each printed 0 everywhere.)
`tests-independent.l4` has 646 assertions: 645 satisfied, 1 failed, 0 refused, and its one error is the failed assertion.
Read from the diagnostics, not the exit code: the one Error-severity diagnostic is at line 787, `assertion failed: expected a refusal, but the expression produced a value`; the only other non-Information diagnostics are the two Warnings about shadowed copies of `prelude` and `daydate`.
**`check.sh` exits 1 with this module present**, because its `expected_failed` table gives `tests-independent.l4` an expected count of 0. I did not edit `check.sh`; whoever weighs the finding below decides whether to list the module with a count of 1 or to change the encoding.

Breakdown of the 646: 279 cell assertions (all 270 cells of section 2 of DECIDED-ANSWERS, plus item 4 again for 2035), 54 on the printed totals and the sums of rows, 6 on combined rates (section 3), 216 reading every cell branch by branch as a person who pays the branch (dashes asserted as refusals), and 91 hand-written scenarios.

## Failing assertions

| # | scenario | provision and Hebrew words | expected (decided before the encoding) | the encoding answered | classification |
| --- | --- | --- | --- | --- | --- |
| T7 | the reduced collection threshold for 2027, updated from 7,703 when the index last published before 1 January FELL from 102 to 101 | s 334(a)(1), source line 3606: `בשנים 2026 עד 2028 – לפי שיעור עליית המדד שפורסם לאחרונה לפני 1 בינואר, לעומת המדד …` ("by the rate of the RISE of the index") | `REFUSE`: the text provides for a rise and says nothing of a fall, unlike laws that say so expressly | 7,703 × 101/102 = 778003/102 ≈ 7,627.4804 (the fall applied) | **Genuine ambiguity, recorded by the encoder** as fork F6, which lists (i) apply the fall and (ii) count only rises, and takes (i). My reading, that the model should decline, is not among F6's listed readings. On reflection I keep it: "עליית" makes (ii) at least as strong as (i), and choosing either silently gives a number for a case the text does not cover. Left failing. |

No other assertion fails.
I found no assertion that I now think I got wrong; the closest is noted under "Passing, but" item 2 below.

## Expectations that could not be expressed through the encoding's interface

Not expressible at all (2):

- **K15** — which column a person falls in (someone insured who is neither employee nor self-employed). The encoding has no rule mapping a person to a Schedule J column: the column is an input (`column` in `Another insured person's year of contributions`; implicit for an employee). The s 1 predicates exist (`s 1 — a self-employed person in the period:` …, `s 334(b) — the person is an employee for Chapter 15`), and I tested them (K1-K14), but the step from them to a column is not encoded. NOTES says why (it needs s 335, out of scope); still, nothing joins the two.
- **K17** — a person who is an employee and self-employed in the same month. There is no entry point that takes both incomes, so the encoding cannot answer it wrongly either. My expectation was REFUSE.

Expressible only in part (4):

- **V1** — March 2011 against the Schedule's heading "בעד אפריל שנת 2011 ואילך". The encoding selects by calendar year, so only "2011" can be asked; it refuses, which is right for March and also for April-December 2011 (which the BRIEF's scope declines anyway).
- **E13 and N6 (item 1 for one who is neither)** — the encoding folds items 1 and 2 into one maternity branch (its F15), so "item 2 for an employee" or "item 1 for one who is neither" cannot be asked at the person level; I asserted them at cell level, where they are `NOTHING`.
- **T8** — I decided that a year whose index or wage readings are missing is "an input, not a refusal and not a default". The encoding's year-only entry refuses for 2027 on, and a second entry takes the threshold as an argument (P1-P8 use it). That is an input in substance and no default is supplied, so I asserted the refusal and count the pair as meeting the expectation, but it is not the shape I wrote down.

## Passing, but worth a second look

1. **Totals (my section 3; the encoder's F4).** I took the rows as the law before opening the encoding, for the reasons the encoder also gives (s 335 levies branch by branch; s 337(a) applies "rates under s 335"), and both of us note the cost: an employee in 2026 is charged 14.49% above the threshold where the National Insurance Institute charges 14.60%, and the deduction on the upper part sums to 4.67% where the Institute deducts 7%. Two independent readers agreeing on this is not evidence that it is right; it is evidence that the text alone points there. Only the Reshumot text can settle whether the consolidation mistranscribes a row.
2. **The average wage (encoder's F5).** My D1 (8,139.6) and the boundary in K8-K9 used the s 1 figure, 13,566. I did not consider that s 2(b) applies a differently calculated figure (13,769) "for benefits and contributions". The tests pass because I supplied the same figure the encoder's tests do. See the appended section of DECIDED-ANSWERS.
3. **2025.** I expected REFUSE because the BRIEF says so, and wrote that the source "arguably" answers 2025. The encoder's A1 cites the Law for the 2025 budget year, s 21, commencing the National Insurance chapter on 1 January 2026; I have not verified it. Separately, the btl.gov.il employees' page I fetched before writing my answers (a WebFetch summary, not bytes I hashed) dates the 1.04% and 4.51% reduced rates "from 01.01.2025", so some of the temporary table's figures were in force during 2025 even if the deposited text as a whole was not. Neither point changes an answer here, since 2025 is declined; both matter to whoever extends the row backwards.
4. **K16, the controlling shareholder.** My 746.4608 (rows, without items 6 and 7) passes. The Institute's composite above the threshold for this person is 14.17% against 14.12% from the rows (encoder's open question 2).
5. **The column D gap in 2026 (encoder's F3).** We agree: a wage above 7,703 in 2026 is declined for the deduction, at 7,703.01, 8,000 and 10,000. The Institute in practice deducts 7% from the threshold, which is the "stale heading" reading.

## How independent this was

- Before finishing DECIDED-ANSWERS I read: the second-pass reference, the writing-l4-rules skill and its phrasebook chapter 11, the encoding's `BRIEF.md`, a plain `ls` of this directory, the source at lines 115-234, 3590-3639 and 4695-4759, and one btl.gov.il page. Nothing else from this directory.
- Two of my decisions follow the BRIEF's stated rules rather than my own reading of the source: the 2025 refusal and "a dash is not a zero". My agreement with the encoding there is not independent.
- After DECIDED-ANSWERS was stamped, I read the `.l4` modules, `check.sh`, the first 60 lines of `nii-il04-tests.l4` (its branch-list fixtures, to see how inputs are supplied; no expected values were taken), and then `NOTES.md`. No expected value in DECIDED-ANSWERS or `tests-independent.l4` was changed after any run; the only edits after the first run added one boundary I had decided but not asserted (D3 at 7,703.01, satisfied) and corrected a section heading's count.
- Semi-cleanroom: I opened nothing from the Axiom Foundation or any RuleSpec source, and searched for none.
