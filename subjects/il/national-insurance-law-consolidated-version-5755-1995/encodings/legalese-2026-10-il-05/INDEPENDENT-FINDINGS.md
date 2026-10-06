# IL-05 independent findings (ss 342, 348, Schedule K)

By the independent test author (fid-il-05), 2026-10-06/07 UTC.
Companion files: `DECIDED-ANSWERS.md` (the pre-encoding reading, finished 21:49:13 UTC, with an appended and labelled post-encoding section) and `tests-independent.l4`.

## Numbers

`check.sh` run over a directory holding the five rule modules and `tests-independent.l4` (L4=/Users/mengwong/.local/bin/l4):

| module | errors | satisfied | failed | refused |
|---|---|---|---|---|
| tests-independent.l4 | 15 | 122 | 15 | 2 |

All 15 errors are the 15 failed assertions; there are no parse, type or other evaluation errors.
139 assertions in all.
The rule modules themselves report 0 everywhere.

## Order of work, as it happened

1. Read `second-pass.md` and the `writing-l4-rules` skill (SKILL.md, and phrasebook entry 11.6).
2. Read the Hebrew source (s 1, s 2, s 334, s 335-337, s 342, s 344-345 for context, s 348, Schedule J, Schedule K), both amending Laws as page images, and fetched five National Insurance Institute pages through the Israeli proxy (21:41-21:43 UTC).
   In the encoding directory I read `BRIEF.md` and ran one plain `ls`. Nothing else.
3. Wrote `DECIDED-ANSWERS.md`; finished 21:49:13 UTC; sha256 recorded then, and verified unchanged before the revision section was appended.
4. Only then opened the `.l4` modules, in a scratch copy. I read the encoder's tests module lines 1-80 (its fixture header) to learn how inputs are supplied. That header quotes some Institute figures (3,442; 143; 8,558) that I had already fetched and decided on.
5. Wrote and ran `tests-independent.l4`.
6. Then read `NOTES.md`.

## Failing and refused assertions

Lines are lines of `tests-independent.l4`.
"Recorded" means the encoder's `NOTES.md` already names the point.

### Root cause 1: Schedule J column D's rows do not add up to its printed total (9 failures)

Schedule J column D ("הניכוי משכר העובד לענין סעיף 342(ג)"), sub-column "above" the bracket, temporary table (source lines 4720-4729): 0.87 + 0.07 + 0.21 + 1.86 + 0.14 + 1.52 = **4.67**; printed total (line 4730) **7.00**.
The permanent table (4738-4748) is the same.
Column D "below" the bracket does add up (1.04).
The Institute prints the employee's share above the bracket as "7% (החל ב- 01.01.2006)".
s 342(c)(1) makes the employer deduct "אחוזים מההכנסה שלפיה משתלמים דמי הביטוח כאמור בלוח י׳".
I decided on the printed total, 7.00.
The encoding takes one column D amount per branch as input and sums the six branches s 342(c)(1) names. Fed the source's rows, it therefore deducts at 4.67% above the bracket.
The encoder's own suite relies on 4.67 too: `nii-il05-tests.l4:596` asserts coordinated contributions of 218.8 for "two employers at 6,000 each, permanent version, threshold 8,000 (scenario 2027)", worked at line 591 as 8,000 × 0.40% + 4,000 × 4.67%.

| line | id | expected (decided) | encoding | classification |
|---|---|---|---|---|
| 220 | B4, wage 7,704 | 80.1812 | 80.1579 | source inconsistency, **not recorded** (also my own oversight: I did not check the rows before deciding) |
| 221 | B5, wage 8,000 | 100.9012 | 93.9811 | same |
| 222 | B6, wage 10,000 | 240.9012 | 187.3811 | same |
| 223 | B7, wage 51,910 | 3,174.6012 | 2,144.5781 | same |
| 226 | B8, wage 60,000 | 3,174.6012 | 2,522.3811 | same, **plus root cause 2** |
| 228 | B9, police officer, 10,000 (s 342(c)(2) "לא ינוכה משכרם הניכוי כאמור בפרט 6") | 234.5369 | 181.0168 | same root cause. The police rule itself is right: the supplementary B9' at 7,000 is satisfied (71.40) |
| 236 | B12, man of 69 without pension, 10,000 | 240.9012 | 187.3811 | same root cause. The age rule itself is right (B10, B11, B12' satisfied) |
| 245 | C1, two employers at 7,000; s 342(d)(1) "יהיה העובד חייב בתשלום ההפרש" | pays 375.3012 | pays 228.5811 | same root cause. The (d) comparison itself is right (C3 and A6 satisfied) |
| 248 | C2, two employers at 40,000; s 342(d)(2) "זכאי להחזר ההפרש" | refund 1,507.2012 | refund 2,537.2243 | same root cause (I supplied the coordinated month already capped at 51,910) |

This is Schedule J's arithmetic, so it belongs to row IL-04's table more than to IL-05's logic.
It reaches s 342(c) because IL-05 sums per-branch rows; nothing in IL-05 can see the printed total.
Someone needs to decide whether the deduction above the bracket is the printed total (7.00, as the Institute applies) or the row sum (4.67), and whether a row of column D, most likely item 10 at 1.52, is a transcription error in the consolidation.
3.85 in place of 1.52 would make the column add up; that is a guess, not checked against the Reshumot text.

### Root cause 2: s 342(c) in IL-05 does not apply the s 348(a) maximum (1 failure, B8, shared with root cause 1)

s 342(c)(1) charges "אחוזים מההכנסה שלפיה משתלמים דמי הביטוח", and s 348(a) says "לא יבוא בחשבון סכום ההכנסה … העולה על הסכום המרבי".
IL-05's `An employee's month under section 342(c)` takes "the column D amounts on the wage"; nothing in IL-05 caps them, and its `s 348` result is not connected to its `s 342(c)`.
On a wage of 60,000, given uncapped per-branch amounts, IL-05 deducts on 60,000 (2,522.3811 on the rows; it would be 2,144.5781 capped).
Classification: interface gap, **not recorded** as such. Fork F17 records that the caller supplies the income for the s 348(b) floor, but not the cap.
NOTES section 1 says the per-branch amounts are IL-04's `the column D deduction under`; if that applies the cap, the composition is right and only IL-05's standalone interface is open to misuse.

### Root cause 3: monthly figures for Schedule K items 2-4 (5 failures)

| line | id | expected (decided) | encoding | classification |
|---|---|---|---|---|
| 303 | E8, item 2, monthly maximum | REFUSE | 51,910 | genuine ambiguity, **recorded (F2)**; on reflection I prefer the encoder's reading |
| 304 | E8, item 2, monthly minimum | REFUSE | 3,442.25 | same |
| 305 | E8, item 3, monthly minimum | REFUSE | 688.45 | same |
| 306 | E8, item 4, monthly minimum | REFUSE | 2,065.35 | same |
| 385 | H1, s 348(d) "שקיבל דמי אבטלה לחודש מלא", deemed monthly income | REFUSE (item 3 prints only "לרבעון … ולשנה") | 688.45 | same (F2 with F5) |

Schedule K items 2-4 print no monthly row.
I refused. The encoder takes a third of the quarter, because each quarterly figure is written as a monthly amount "כפול 3" and the Institute prints exactly those monthly figures.
Having read the reason I think the encoder's reading is the better one; the assertions stay failing as decided.

### Root cause 4: s 348(d) for a quarter (2 refused)

| line | id | expected (decided) | encoding | classification |
|---|---|---|---|---|
| 387 | H2, full-month unemployment benefit in every month of Q1 2026, no other income | 2,065.35 (item 3, quarter) | refuses: "section 348(d) is stated for a full month" | genuine ambiguity, **recorded (F5 and the named refusal)**; also partly not expressible: the case has one boolean "for a full month" and cannot say "in every month of the quarter" |
| 389 | H3, as H2 with 5,000 of other income; (d) has no "אינה מגיעה" limb | 2,065.35 (deeming) | refuses (same message) | genuine ambiguity, **recorded (F5: deeming or floor, declined where they differ)** |

### Root cause 5: the 2027 deduction (1 failure)

| line | id | expected (decided) | encoding | classification |
|---|---|---|---|---|
| 421 | I3, s 342(c) for February 2027 | REFUSE: the temporary Schedule J ends on 31.12.2026 (Amendment 252 s 7(a)) unless extended by order for 2027 (s 7(b)), and no source says whether an order was made | 187.3811 (sums the inputs) | genuine ambiguity, **not recorded in IL-05**. NOTES does not mention the s 7(b) extension power, and its own 2027 scenario assumes the permanent table. Low severity for IL-05, because the column D amounts are inputs and the choice falls on IL-04 or the caller |

## Expectations that could not be expressed through the interface: 4

1. **A7**: an employee who is also self-employed, as one person. `An insured person, for section 342(a)-(b)` takes a single column, so this needs two calls. I did not write them.
2. **The bracket banding and the s 348(a) cap inside s 342(c)** (B1-B8, C1-C2): IL-05 does not compute column D from a wage; the caller supplies per-branch amounts. My tests therefore supply amounts computed by my own helper (`fid column D amounts on a wage of`), and the band arithmetic is mine, not IL-05's.
3. **H2, "full-month benefit in every month of the quarter"**: the case's (d) field is a single month-stated boolean.
4. **J2**, the consolidation's stale column D "above 60% of the average wage" heading in the temporary table, which would leave 7,703-8,261.40 in neither band in 2026: not testable in IL-05 for the same reason as 2.
   The encoder's NOTES section 9 reads the three texts exactly as I did (enacted Law: both bands meet at the bracket from 1 January 2026; "60%" survives only in Amendment 252 s 7's lower heading).

Two more are not counted, because the encoding meets them by construction: K6 (a quarter beginning on 1 February cannot be built; the type has only the four Schedule K quarters) and B13 (a woman's Part D age is a required input, so it cannot be missing).
One artefact: the quarterly yeshiva-student cases (H5, H6) put the student's income in "income from work", because s 348(a1) on a quarter refuses (as I decided it should, G9). The noun's convention says that field is employee or self-employed income.

## Where the independent reading and the encoding agree on a contested point

- **Which average wage**: s 1 as modified by s 2(b), 13,769 for 2026 (my section 2; F1). The encoding's published 2026 figures carry 13,769, and item 2's quarterly minimum on them is 10,326.75.
- **s 348(a1) as a deduction**, not a cliff (G3: 0.01 at 3,442.26; G5: 8,557.75 on 12,000; F3).
- **s 348(a1) declined on a quarter or a year** (G9; F4).
- **A yeshiva student with income above the item 3 minimum stays on item 3** (H6; F6).
- **s 348(e) temporary text**: begun 31.8.2026 is not "before" (H10); begun 1.3.2026 is still covered in Q4 (H8); begun 1.9.2026 falls to item 4 (H9) (F8).
- **Periods before 1 January 2026 refused**, never answered on the 2026 bracket (I1; A1).
- **s 342(e)(3)-(4) "טור ה׳"** is not the deduction column (J1; F22), and a deduction governed by those regulations is refused.
- **Moving average wage** (F12): items 3-4 read January's figure for Q2-Q3 and October's for Q4, while item 2 reads each quarter's own first month. All eight figures agree.
- Every Schedule K bound, at, below and above, in month (item 1), quarter and year: all satisfied.

## Other observations

- `registers/source-bundle/amending-laws/SOURCES.json` says `25_lsr_6133485.pdf` has 5 pages; `pdfinfo` reports 40, and the National Insurance part (Part E, ss 19-21) is on PDF pages 11-12 (printed pp 395-396). A reader who trusts the manifest and reads five pages will not find s 19.
- NOTES section 11 says the independent test pass "was not run". This file is that pass.
- `nii-il05-tests.l4:591-596` asserts coordinated contributions of 218.8 for a 2027 scenario, with the working "8,000 × 0.40% + 4,000 × 4.67%" (NOTES line 257 repeats it). So the encoder's own suite carries the column D row sum (root cause 1) as an expected value, unflagged.

## Anything read that should not have been

Nothing under the Axiom Foundation, any `rulespec-*` path, `.axiom/`, `docs/ENCODING-GAPS.md`, `tax-benefit-source-map.json`, or `l4-ide/specs/research/AXIOM-*` was read, searched or fetched.
No sibling row's `NOTES.md` was opened.
The encoder's tests module was opened (lines 1-80 only) after `DECIDED-ANSWERS.md` was fixed, as the instructions allow; its header quotes some Institute figures.
