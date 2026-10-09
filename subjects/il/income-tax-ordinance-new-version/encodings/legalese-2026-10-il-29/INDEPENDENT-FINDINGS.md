# Independent findings for IL-29 (BACKLOG IL-56), by fid-il-29

DECIDED-ANSWERS.md (269 rows) was frozen at sha256 `7dbd3c084d900fcb6505b67fef75f7e1408a051184ed44b65a5d786addf3130d` before this directory was opened.
`tests-independent.l4` asserts those answers through the encoding's public entry points: 216 assertions, 200 satisfied, 8 failed by design, 8 refused by design.
`check.sh` is red only for the declared reasons: it declares 8 expected failures and 8 expected refusals for `tests-independent.l4`, each named by line in a comment, and exits 0.
`l4` is `jl4-0.1-6df1397b`, sha256 `f0759b2ef2f1d1b2a577c68f059c54f487de9d913553fc9f0d9bf0f7f5dab0d8`, the same before and after.
No expected value was changed after the encoding was read.
Where I had flagged an ambiguity the encoding also forks, I asserted the refusal; where I decided one reading, I asserted it by default and again under the named reading.

## Result in one paragraph

No arithmetic or threshold disagreement was found: the day counts (182/183/184, 30 and 425, part days from stays), reg 2, reg 3 (each class, the five-year condition, the hospital test), the body-of-persons tests, the second limb of "foreign resident", s 14(b) day-90 boundaries, the ten rate bands including the gap, the adjusted-price formula (the 1% proviso at exactly 1%, negative difference, exchange ratio, daily-price average), rounding, the phone formula and s 2A all agree with my hand work.
Every one of the 16 non-satisfied assertions (14 rows below) is a fork the encoder had already named (class AMBIGUITY), a figure policy (note-only figures), a scope or granularity difference, or an error of mine.

## Disagreements

| # | IDs | line(s) of tests-independent.l4 | class | what |
|---|---|---|---|---|
| 1 | A34 | 128 | AMBIGUITY (fork C2) | I read a rebuttal as showing the centre of life is abroad, so "rebutted, no finding" is not resident; the encoding declines. |
| 2 | A35 | 131 | AMBIGUITY (fork C1) | I answered resident for five ties all in Israel; the encoding declines. |
| 3 | A36 | 134 | AMBIGUITY (fork C1), and my confidence was too high | I answered not resident for five ties all abroad (H); the list is "בין השאר" (non-exhaustive), so unanimity of the five listed ties is not conclusive. |
| 4 | B06 | 175 | AMBIGUITY (assumption A3) | On the fifth anniversary I flagged the day-count convention; the encoding fixes "ends the day before the anniversary" (not forked) and answers. |
| 5 | C34, C35 | 288 | TESTER-WRONG | I took the foreign journalist and athlete as inputs; s 75A defines both as "תושב חוץ" (ITO line 2640 and 2642), so the class is circular for a resident; the encoder's fork JA is right. Under the named reading my answer holds (line 287). |
| 6 | G02 | 462 | AMBIGUITY (fork N90) | Notice on day 90: I answered in time (day of arrival excluded); the encoding declines. Under reading A it agrees (line 463). |
| 7 | J08 | 664 | AMBIGUITY (policy on note-only figures) | The 2024 cap is only in a Wikisource note; I expect "needs the published figure"; the encoding answers from its marked published-figures module. |
| 8 | J31 | 668 | same | 2026 L3 motorcycle amount (1,070, note only). |
| 9 | J32 | 666 | AMBIGUITY (assumption A11) | A motorcycle not of class L3: reg 2(א) excludes only "אופנוע כאמור בתקנת משנה (ב)"; I flagged it, the encoding treats it as an ordinary vehicle. |
| 10 | K07-K09 | 681-683 | same as 7 | 2026 plug-in, hybrid and electric reductions (1,150 / 580 / 1,380, notes only). |
| 11 | K13 | 687 | SCOPE (conservative) | Tax year 2029, hybrid, price 200,000: no reduction applies (the period ends 2028-12-31) and the price is below any cap, so 4,960 is determinable; the encoding refuses because it holds no cap for 2029. |
| 12 | L07 | 724 | AMBIGUITY | A phone from which only the workplace can be called: I said value 0; the Regulations only exclude it from their rule (TEL reg 2) and say nothing about its value, so the encoding's refusal is defensible. |
| 13 | L12 | 726 | same as 7 | 2025 ceiling of the phone value (115, note only). |
| 14 | L15 | 721 | AMBIGUITY (fork XD) | The employee pays the whole expense: I said 0 (M); the encoding declines. Under reading "nil" it agrees (line 722). |

The numbering counts the 16 expected non-satisfied lines as 14 rows because C34/C35 share a line and K07-K09 are three lines.

## SCOPE differences (no assertion could be written, or none written)

- Tax years before 2024: the encoding answers 2024 onwards only (assumption A1). My cases for 2002, 2010, 2015 to 2022 (J05 to J07, K01 to K06, K10, K11, K14, K20, K22, K23, L13, L14, G16 to G18) cannot be put to it. The 2022 reduction amounts (500, 1,000, 1,200) and the 2015 amounts are text of the Regulations, not notes, so a historical encoding could answer them.
- Granularity: residence is a status of a tax year, so my date-level answers (F10 and F11 at 2025-02-28 and 2025-03-02, B04 and B05 on named dates, G01 to G07 within a straddling year, G14) were restated at tax-year grain with the tax year wholly inside or wholly outside the window, where all four window readings agree and the default answers. The straddling years are declined by the encoding's fork W and I asserted that refusal (F12, G15, G19, C21).
- The ten source categories of s 2, the exemption of s 14(a) and the periods of s 14(b)(2)(a), (c) to (h) are not encoded (H09 to H19, G16 to G18); NOTES section 1 says so.
- Plug-in, hybrid and electric classification (green score at most 100, battery over 3 kWh, spark ignition) is the caller's classification (K15 to K18).
- Whether control and management are "conjunctive" (F16) and "run by such an individual" exclusively (F15) are single boolean inputs; the encoding cannot express the question.
- The proof of the form of notice (G05) and the career-army exclusion (C13) are not representable.
- Personal-import depreciation (J19) was not tested; the encoding forks it (DEP, PMD).

## Matches worth recording

- The rate-band gap (J27): unindexed 123,500 with Nov 2008 / Nov 2009 = 0.99 gives no band; the encoding refuses, as I did. Tier (1) tests the unindexed figure and tiers (2) to (10) the indexed one, exactly as the Hebrew prints them.
- Reg 3(7) hospital test at 182 / 183 non-hospital days and the limb (b) variant (C31 to C33): agree.
- Reg 2(1) is not subject to the proof clause (B15): the encoder punctuated it as I did.
- Both statuses (D12): both flagged ambiguous, both refuse for income produced abroad.
- s 2A set-off (I10): both read "למעט לענין קיזוז הפסדים" as "s 2A does not itself treat the winnings as income for the set-off of losses".

## What the encoder read wrongly in the source

Nothing found.
I checked, against the deposited Hebrew, every figure of `ito-il29-published-figures.l4` (563,790 / 583,100 / 596,860 caps; 1,010 / 1,040 / 1,070 L3; 105 for 2019-2022 and 115 for 2023-2027 phones; 540, 580, 1,150, 1,380 reductions), the ten rate bands and their bounds, the 450,000 base, the 90-day and 10-year, 5-year and 3-year windows, and the eight reg 3 classes.
All match the text.
Points I would put to a domain expert rather than call errors: the note that fixes the commencement day of the 2009 amendment Regulations as 1 January 2010 is a note (the encoding relies on it for "registered before 2010"); the 2007-2009 "five years" parenthetical for a veteran returning resident sits in a Wikisource note.

## Faults in my own frozen file (not edited, reported here)

- The section headings of DECIDED-ANSWERS.md use the letter K twice (the hybrid sub-heading and the phone heading are both "K"; the phone rows are L01 to L15 and the hybrid rows K01 to K24).
- C38 and C40 carry the same facts; C38 is flagged as the "every year" reading (M) and C40 states the same outcome; the test asserts the refusal by default and the answer under the named reading.
- I missed the s 75A circularity (item 5 above).
- A36 was over-confident (item 3 above).
