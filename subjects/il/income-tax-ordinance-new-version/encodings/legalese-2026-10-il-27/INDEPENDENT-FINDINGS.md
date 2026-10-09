# INDEPENDENT-FINDINGS, row IL-27 (test author fid-il-27, 2026-10-09)

## What was done

DECIDED-ANSWERS.md was written from the Hebrew sources alone and frozen before the encoding's .l4 modules, NOTES.md, check.sh or tests were opened (only `ls` of the directory was seen before).
It holds 267 decided cases (A to K), sha256 `6957cca315024fbe8d1a465b6f1ecb2d4da14fe4ce416dd6308663a277ecfcda`.
`tests-independent.l4` asserts 237 of them through the encoding's public entry points: 223 satisfied, 11 declared refusals, 3 declared failures.
`check.sh` was changed only to add the module's declared counts (3 failed, 11 refused, each named by line, case id and class in comments) and a matching `expected_refused` hook.
`l4` sha256 before and after: `f0759b2ef2f1d1b2a577c68f059c54f487de9d913553fc9f0d9bf0f7f5dab0d8` (unchanged).
`check.sh` exit 0 with the declared counts; `tools/sq.sh --check` (the encoder's quotation checker) also exits 0.
No expected value was changed after a run.
Two edits after the first runs were to my own test data, not to expected values: rule-2(2) test persons had `stayed 0` months, which satisfied rule 2(1) and so made a FALSE case TRUE (my data error); three guessed refusal strings were replaced by the encoding's real strings (the asserted outcome, a refusal, is unchanged).

## Disagreements

| line | case | class | what |
| --- | --- | --- | --- |
| 294, 295 | A17, A18 | SCOPE | Pre-2022 oleh credit for tax years 2022 and 2023: the encoding refuses any tax year before 2024 (NOTES A1). My expected 3 and 2 points stand on the Hebrew (ITO:1574, 1577). Years 2024 and 2025 of the same oleh (A19, A20) agree (1 and 0). |
| 437, 438, 439 | F47, F48 | SCOPE | Old-text 40D cases for tax years 2023, 2019, 2020: refused by the same A1 gate. |
| 356 | E12 | AMBIGUITY | s 39B reading T, 29 days: I decided 0; the encoding refuses "the temporary provision says nothing of 20 to 29 days". The text gives no tier for 20 to 29 days under T, so 0 was an over-reading of silence; the refusal is the better answer. |
| 371 | E20 | OURS-WRONG | s 39B, 200 days in tax year 2027: both readings give 4 (P caps at 85 days, T at 110), yet the default refuses. NOTES section 4 says the default "declines where the readings differ"; here they agree. Code: `declined where the readings differ` refuses whenever days are 20 or more, without comparing. |
| 389 | F23 | AMBIGUITY | s 40B, born 15 June 2010, tax year 2026 at the default: I decided 1 (H), the encoding declines. The "every day" reading gives 0, so my H was overconfident (tester error of confidence, not of reading); with the reading `on the last day of the tax year` named the encoding gives 1 as I decided. F25 (born 2008) agrees: refusal. |
| 416 | F39 | OURS-WRONG (minor over-decline) | s 40C(e), two identical first-degree studies: I decided one point (3 years ended 2023, 2026 gives 1); the encoding refuses "does not say which of several is the one". With identical studies every choice gives 1, so no readings differ. |
| 451 | F52 | OURS-WRONG (minor over-decline) | s 40E, first degree and vocational studies both worth 1 point, no election made: I decided 1; the encoding refuses until an election is made. Both elections give 1. A52-type cases where the points differ (F53) agree: the encoding gives 1/2 or 1 by election. |
| 465 | G07 | AMBIGUITY (presentation) | s 41, registered spouse: I expected 0 ("outside s 41"); the encoding refuses, saying the spouse's tax is under ss 64B and 65. Same substance, different form. |
| 476 | H07 | SCOPE | s 44, income 188,001 against the single ceiling 188,000 of the consolidation's note: I expected 0; the encoding gives 12,774.95625 because it takes the regulations' conditions (which carry the ceiling) as a caller input and the note's figures are recorded but not used. The note is not law, so the encoder's reading is defensible. I could not test the couple ceiling because the input has no marital status. |
| 499 | I07 | TESTER-WRONG | s 46, 25,000 new plus 10,000 carried against a 30,000 ceiling: I demanded a refusal (order of use unstated). The credit is 35% of the lesser of everything available and the ceiling, whichever is taken first, so 10,500 is right (NOTES fork F16). |
| 526 | J11 | AMBIGUITY | s 47(b1), a self-employed person paying exactly 26,436: I expected 12,804, relying on the note's printed figure of 26,436 for 16% of the average wage. The encoding uses 13,769 x 12 = 165,228 and 16% of that is 26,436.48, so 26,436 is "less than 16%" and the person is not a beneficial member; it gives 0. The note itself (ITO:1769) prints both 26,436 and a monthly wage of 13,769, which are inconsistent by 48 agorot; the statute says "not less than 16%". |

Disagreements that were my errors in the decided answers (frozen, so recorded here and not corrected there): E12 (silence), F23 (confidence), I07, J11 (rounded note figure), the missing flag on whether a divorced woman is within s 40A (the encoding's fork F3 is right to decline; I decided nothing for her).

## Agreements worth stating

Every point-fraction schedule I worked by hand matches: s 35 for aliyah dates from 2022-01-01 to 2026-07-01 over tax years 2026 to 2031 (A01 to A16; the pre-2022 and 2022 boundary A12 and A13), s 39A (all D cases), s 39B in 2028 and under both named readings in 2026 and 2027 (E01 to E19), s 40B, s 40C including the internship election, direct track and third degree under the named reading, s 40D, s 41, s 44 and s 45 amounts, s 46 including the carry and the 10,354,816 ceiling, s 46A, s 46B, s 47A including the refund rule, the Regulations of 5740-1980 at age 50 (J16 to J23), the Retirement Age Law tables (all 48 month boundaries) and rule 2 of the 1977 rules.
The encoding's refusals match my flagged ambiguities AMB-3 (s 39B temporary provision), AMB-4 (s 40B age moment), AMB-5 (regulation 1 ceiling), AMB-8 (s 46A cut), AMB-10 (s 40C(d)(1)) and the Part B gap for a woman born before May 1947 (K24).

## Things the encoder read or recorded, checked against the source

Quoted Hebrew passes `tools/sq.sh --check` (exit 0).
Figures checked by hand against the deposited Ordinance: the point value (2,904, ITO:1563), 207 and 10,354,816 (ITO:1745), 188,000 and 301,000 (ITO:1705), 116,400 and 164,400 (ITO:1766 to 1771), 12.5% and 35% (s 44), 52% (s 47A), 1,700 hours (s 40D), 23 and 22 full months (s 39A), 30 to 39, 40 to 49, 50+ days (s 39B temporary lines), and Part A and Part B month boundaries.
I found no mis-read figure or date.
The encoder's own observation that the temporary s 39B lines are less generous than paragraphs (1) and (2) at every number of days is correct.

## SCOPE (decided by me, not encoded by this row; I tested none of these, so these are the thin spots of the independent pass)

- Section 39, the helping spouse (C01 to C10): no module.
- Section 40(b) child points for a single-parent family, para (1), (1a), (1a1), (1b), (2) (F01 to F17): no module (only the whole-year points are an input of s 41).
- Section 35(b), registered spouse of an oleh (B22), the returning-resident definition (B17 to B21), and the s 35(c) "first time only" rule (B07): not encoded by this row.
- Section 41(2) (G08): the s 66 points are an input.
- Sections 44 and 45 relatives, institutions and the couple/single ceilings (H10 to H14): inputs.
- Section 46 recognition of institutions, the memorial note, the company rate (I09, I10, I12, I16 to I18): out of scope or inputs.
- Section 47A(c), (d) and 47(b) fund-type conditions (J31 to J34): refused or inputs.
- Retirement Age Law ss 4, 5, 7, 8, 10, 12 and Part C (K03, K04, K25 to K39): not encoded (NOTES section 2 gives the reason).
- Section 39A on passive income only (D14): the credit's tax base is the composer's.
- Section 39B, tax years before 2026 (commencement): refused by name, and my case says "needs the commencement date", so they agree.

## Coverage of the independent pass (which sections were covered thinly)

Thickly: ss 35 (via rule 3), 39A, 39B, 40C, 40D, 41, 44, 46, 47 with the Regulations, 47A, the Retirement Age Law.
Thinly: s 40A (4 cases, none for a woman), s 40E (4), s 45 (7), ss 46A and 46B (4), rule 2 and rule 3 of the 1977 rules (about 14).
Not at all: s 39 and s 40(b) (no module).
