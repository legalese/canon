# Independent findings: IL-34 (BACKLOG IL-56), author fid-il-34, 2026-10-09

DECIDED-ANSWERS.md (370 cases) was written from the Hebrew sources alone and frozen before any file of this directory but its listing was opened; sha256 `1d4a5ef8878cb3e1ecb8ce397f62d092c490ad0324a9c940797e524de2e34230`.
`tests-independent.l4` asserts those answers through the encoding's public rules.
Every expected value there is the one decided before the encoding was read; none was changed to fit it.
`l4` sha256 before and after the run: `f0759b2ef2f1d1b2a577c68f059c54f487de9d913553fc9f0d9bf0f7f5dab0d8` (unchanged).
`check.sh` (26 modules, exit 0): `tests-independent.l4` has 149 assertions satisfied, 5 failed (declared), 2 refused (declared); the 25 modules of the row are unchanged at 718 satisfied.
Only `check.sh`'s two `case` lists (expected 5 failed, 2 refused for `tests-independent.l4`) were edited.

## Disagreements

| # | lines of tests-independent.l4 | my case | class | what |
|---|---|---|---|---|
| 1 | 129 (refused) | C013 | OURS-WRONG (minor) | `Order of 5759-1999 s 3 — the Order applies to contributions payable for the day` refuses on 31.12.1998 ("governed by the Order No. 2 of 5747-1987, which is not deposited"). |
| 2 | 326 (refused) | C269 | AMBIGUITY | Began civic service 1.9.2026, for October 2026: I decided "not reached" on the deposited text and said "unless an Act extended the Law". The encoding's default declines (fork C1). My assertion at the named reading (`the deposited expiry, the day itself in force`) passes (line 324). |
| 3 | 220 to 223 and 225 (failed) | C143 to C147 | TESTER-WRONG | I divided each branch rate by the printed total 14.60; the encoding divides by the sum of the cells it is given (14.49). See finding S1. |

### 1. Order s 3 on 31 December 1998 (OURS-WRONG, minor)

Hebrew: "תחילתו של צו זה ביום י״ב בטבת התשנ״ט (1 בינואר 1999) ... והוא יחול על דמי ביטוח המשתלמים בעד יום התחילה ולאחריו" (Order art 3).
The question "does this Order apply to a payment for 31 December 1998" has the plain answer no.
What governed that day (Order No. 2 of 1987) is the reason the encoding gives for refusing, but it is not needed to answer the question asked.
The same applies to `Order of 5759-1999 — the Order's amount applies to ... on the day` for 1998 (not asserted by me).
The refusal for the amount of wage for a month before 1999 is right: there the amount is the repealed Order's.

### 2. Civic Service Law, a start on 1.9.2026 (AMBIGUITY)

The deposited text (Wikisource revision of 2026-04-01) says s 36(a) "עד יום י״ח באלול התשפ״ו (31 באוגוסט 2026)" and s 36(b) keeps the Law for "מי שהחל את שירותו ... לפני מועד הפקיעה".
Nothing deposited says an Act moved the date, and nothing after 2026-04-01 is deposited, so both of us say the answer turns on a later Act; I take "not moved" as my reading, the encoding declines.
The brief's question, "whether the National-Civic Service Law moved s 348(e)'s 31.8.2026 expiry", is answered the same way by both: the text deposited says 31.8.2026, the date in s 348(e)'s editorial note is the Civic Law's own lapse date, and a later amendment cannot be excluded from the sources.
Agreement elsewhere: began 1.3.2026 and serving in October 2026 yes (line 320); began 1.7.2026 and still serving, s 36(b) yes; 30.8.2026 in force; 1.9.2026 not in force at the deposited reading; the start on 31.8.2026 declined at the default (my C270, flagged L; line 328, satisfied).

### 3. Section 28(a) with employee rates (TESTER-WRONG), and a source anomaly (S1)

My frozen answers C143 to C147 used the printed total 14.60 as the denominator.
The employee column C above the tier prints cells 1.40, 2.08, 1.96 (2.06 under the 2024 to 2027 note), 0.13, 0.33, 0.04, 2.28, 0.28, 5.89; they add to 14.39 (14.49 with 2.06) while the printed total is 14.50 (14.60).
s 28(a) credits "לפי יחס שיעורי דמי הביטוח" (by the ratio of the rates), so the ratio of the cells is the more literal reading and the encoding's is the defensible one; I was wrong to use the printed total.
The failures are my expected values (95.89, 142.47, 141.10, 403.42 for each 1,000, and 47.95 for 500) against the encoding's (96.62, 143.55, 142.17, 406.49 and 48.31).

## Source anomalies the encoder should know (not the encoder's errors)

S1. Schedule J, 2025 to 2026 table, employee column C above the tier: cells add to 14.39 (14.49) against the printed total 14.50 (14.60), a gap of 0.11.
S2. Schedule J, col D (employee deduction) above the tier: the cells (0.87, 0.07, 0.21, 1.86, 0.14, 1.52) add to 4.67; the printed total is 7.00; the lower tier cells (0.10, 0.03, 0.02, 0.29, 0.03, 0.57) add to 1.04 as printed.
Any branch-by-branch deduction would not add up to the 7.00 the regulations and s 342(c) rely on; the encoding takes the rates as inputs and is unaffected.
S3. The consolidation keeps "על חלק השכר העולה על 60% מהשכר הממוצע" in col D's heading in the 2025 to 2026 table although the 2025 Budget-year Law s 19(6) replaces "60%" in Schedule J by the reduced collection tier from 1.1.2026.
S4. s 342(e)(3), (4) and reg 1 say "טור ה׳ בלוח י׳" for the deduction rate; the deduction is col D, and col E is the Treasury allocation (the encoder's NOTES section 3 says the same, IL-05 fork F22).
S5. s 369(d) says "הוראות סעיף קטן (ג) לא יחולו אם חויב מעסיק בשל פגיעה בעבודה"; (c) is the right to argue, and the evident target is (a); out of scope here (the encoding stops at (a)).
S6. Two 2026 average wages appear in the file: 13,566 in s 1's note ("השכר הממוצע לפי הגדרה זאת") and 13,769 in s 2(a)'s note ("השכר הממוצע המדוד").
AMBIGUITY (not decided by the text): which one feeds Schedule A, Schedule K1, ss 340(d), (e) and the Schedule K11 minima.
I used 13,566 and tested both figures for Schedule A (2,034.90 and 2,065.35, both satisfied).

## Where the encoder's figures differ from what I derive (OURS-WRONG, minor, fixtures and labels)

M1. The tests and NOTES answer table use 3,442 as "the Schedule K minimum" for s 345B(c)(2) ("A pensioner of 2,000 with no other income: 3,442 counts") and for s 350A(c).
s 345B(c)(2) names "ההכנסה המזערית הקבועה בפרט 3 בלוח י״א"; item 3 is "5% of the average wage ... times 3" a quarter, that is 678.30 a month (2,034.90 a quarter) at 13,566, not 3,442.
3,442 is 25% of 13,769, which is item 2's (self-employed) monthly minimum computed with the s 2 note's wage, so the fixture takes the wrong item (and the other average wage, S6).
The rules take the minimum as an input, so no rule is wrong: with 678.3 my assertions pass (lines 296, 298, 300 and 302).
The same figure for s 345(e): item 2 gives 3,391.50 at 13,566 (lines 293 and 294, satisfied with that input).
For s 350A(c) "the minimum stated for him" depends on his class; the fixture 3,442 is item 2 only.

## What I checked in the encoder's reading of the sources

I compared against the Hebrew, line by line: the 2026 tier 7,703 (s 334 note; also reproduced as 7,522 x CPI Nov 2025 / Nov 2024 = 7,702.5 from data/cbs-cpi), the maximum 51,910 = 5 x 10,382, the Treasury percentages 2018 to 2029 (s 32(a)(1) to (12)) and the extension figures 44.26 and 45.39 (Amendment 252 s 7(b), changed by the Budget-year Law s 20(2)), the s 32(c1) rates 7.10 and 5.65, s 340(d), (e) (0.53 and 0.13, base 0.4 and 0.1), s 340A (7.85, 1.8, 3.6 and 6.25, 1, 2), the Order's dates (1.1.1999, 31.3.2000), s 28A, s 28B (1.1.2000 to 31.12.2014), reg 4(a) 31 July, reg 6(a) seven years, reg 6(b) three months, reg 7(1) the 15th, reg 9 five months, Schedule A 15 percent, Schedule K1 multiples 5, 10, 20, K16 one country, s 350A window 1.1.2026 to 31.12.2035, s 351 subsection letters.
I found no figure or date misread.
Its s 351 matrix (b), (c), (d) second limb, (h) to (j) agrees with my C308 to C341, and its `s 350(a)` reading agrees with C278 to C290 (four kinds are income; unemployment benefit is not).
I did not run `tools/hebcheck.py` (it needs a file argument; the encoder reports it passes).

## SCOPE and what I covered thinly

SCOPE (decided by me, not tested here because the encoding takes the figure as an input or leaves it to another row): C018 to C059 (the employer's s 342(c) deduction and the age/police rules; IL-05), C060 to C061 (columns and tier in the regulations; the rate is an input), C097 to C098 (s 342(f) rates), C225 to C230 (rates on early pension; IL-05's Schedule J), C244 to C262 (s 348 minima and maxima; IL-05), C310 to C341 (the s 351 matrix: covered by the encoding's own 267 assertions, which I read and agree with).
Not decided at all (my gap): s 32(b) to (h) other than (a), (c1) and (c2), including the (g) reimbursement formula the encoding encodes (my reading stopped at (e)), s 32(g)(2) indexation, s 369(a1) to (e) beyond a summary, s 344(a)(1) kibbutz amounts (D1), and the s 342(ה1) kibbutz-member case.
Heavier on my side: the s 342(e) regulations (about 30 cases), s 32 percentages, s 340A, s 348(e) and the civic expiry, and K1.
The Institute's charge on yeshiva students: no text; the encoding refuses it by name (`nii-il34-needs-a-source.l4`) and I agree (C273).

## Counts

370 cases decided; 149 independent assertions satisfied (of which 6 are `REFUSED ... BECAUSE` assertions satisfied); 5 failed (TESTER-WRONG); 2 refused (1 OURS-WRONG minor, 1 AMBIGUITY).
