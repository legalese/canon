# Independent findings for row IL-30 (BACKLOG IL-56)

Author: fid-il-30, an independent test author, 2026-10-09.
The expected answers in `DECIDED-ANSWERS.md` (sha256 `01c7fcfbf20e44abbe8f3717507b89d1fe2cd059d177f594dc67dd2005e6bd58`) were written from the Hebrew sources alone before the encoding's contents were opened.
Before freezing it I had listed this directory's file names (the module names) and had not opened any of them; the encoding's `not-encoded.txt` path named in the brief does not exist, so I did not use it.
The tests are in `tests-independent.l4` (sha256 `2778d70caca08dcfbebfec37a691124af8a201b2e79fb5f33009928d8f9967e2`).

## 1. Result

500 cases decided.
394 of them are asserted in `tests-independent.l4` through 433 assertions; the other 106 have no entry point and are listed in section 6 as SCOPE.
`check.sh` exits 0 with the declared counts: 35 modules, `tests-independent.l4` 405 satisfied, 11 failed (declared), 17 refused (declared), every other module unchanged (579 satisfied).
The l4 binary was `jl4-0.1-6df1397b`, sha256 `f0759b2ef2f1d1b2a577c68f059c54f487de9d913553fc9f0d9bf0f7f5dab0d8`, the same before and after.
Nothing was changed to make an expected value fit: the 11 failures and 17 refusals below are all kept and declared by line, id and class in `check.sh`.

Of the 11 failures, 1 is TESTER-WRONG (BT10, in part), 10 are AMBIGUITY, and none is OURS-WRONG.
Of the 17 refusals, 1 is AMBIGUITY (the encoding is right to decline), 16 are SCOPE.

## 2. Failed assertions

| line | id | class | what |
| ---: | --- | --- | --- |
| 702 | T49 | AMBIGUITY | a right bought and sold in the same tax year: 1 year spreading decided, 0 returned |
| 781 | DV12 | AMBIGUITY | s 125B(3) with a holding 18 months earlier: the decided refusal, a value returned |
| 1305 | BT09 | AMBIGUITY | RE s 47 day counts at the Starting Day |
| 1307 | BT10 | TESTER-WRONG, then AMBIGUITY | middle part for a material shareholder, then the Starting Day |
| 1309 | BT11 | AMBIGUITY | the Starting Day count |
| 1311 | BT12 | AMBIGUITY | the Starting Day count (purchase on the Starting Day) |
| 1325 | BT19 | AMBIGUITY | the Transition Day count in the exempt part of (b2) |
| 1327 | BT20 | AMBIGUITY | the Transition Day count |
| 1331 | BT22 | AMBIGUITY | the Transition Day count |
| 1333 | BT23 | AMBIGUITY | the Transition Day count |
| 1342 | BT27 | AMBIGUITY | s 48A(b4) with a 2005 purchase |

### T49 (AMBIGUITY)

The case: a right bought in 2026 and sold in 2026; how many tax years does s 91(e) spread over.
Hebrew: `תקופת הבעלות בנכס – תקופה שתחילתה בתחילת שנת המס שלאחר שנת המס שבה הגיע הנכס לידי הנישום וסיומה בתום שנת המס שבה יצא הנכס מידיו`.
The period would begin on 1 January 2027 and end on 31 December 2026, which is empty.
I decided 1 year (no real spreading) and flagged the case L; the encoding returns 0, which is also a defensible reading of an empty period.
The text does not say which; neither is wrong.

### DV12 (AMBIGUITY)

The case: a family company's s 64A assessee held 10% of the paying company 18 months before the dividend and holds 3% at receipt.
Hebrew: `ואולם אם היה הנישום כמשמעותו בסעיף 64א בעל מניות מהותי, במישרין או בעקיפין, בחברה ששילמה את הדיבידנד – 30%`.
The text names no time.
I decided that three readings are open (at receipt, at receipt or in the 12 months before, at any time) and asked for a refusal.
The encoding's fork D1 offers the first two, and both give 25% for a holding that ended 18 months earlier, so it answers 25% by default.
Its register of forks omits the third reading (any time, which gives 30%).
The omission only matters for a holding older than 12 months.

### BT09, BT11, BT12 (AMBIGUITY, and a possible double count)

The case: the three-part split of the real betterment of s 48A(b1) by days (s 47: `שבח ריאלי עד יום התחילה`, `שבח ריאלי לאחר יום התחילה ועד למועד השינוי`).
Hebrew for the first part: the ratio of `התקופה שמיום הרכישה ועד יום התחילה` to `התקופה שמיום הרכישה ועד ליום המכירה`.
Hebrew for the second part: the ratio of `התקופה שמיום התחילה או מיום הרכישה, לפי המאוחר, ועד ליום שקדם למועד השינוי` to the same denominator.
I decided that part one stops before the Starting Day (7 November 2001), so that the Starting Day belongs to part two alone and the three parts add exactly to the whole.
The encoding's reading `both the first and the last day are counted` puts the Starting Day in part one as well as in part two.
Arithmetic for BT11 (purchase 6 November 2001, sale 1 July 2026, real betterment 1,000,000): part one 2 days, part two 3,707 days, together 3,709; the interval from the purchase day to 31 December 2011 is 3,708 days, so one day is counted twice and the remainder (part three) is one day short.
Decided 229,439.14, returned 229,463.57.
The sentence for part one says `עד יום התחילה`, not `עד ליום שקדם`, so the text allows the encoder's reading; the overlap it produces is a consequence the text does not address.
I class this AMBIGUITY, with a note for the encoder: under the `both counted` reading the parts overlap by one day.
For BT12 (purchase on the Starting Day) the decided part one is 0 and the encoding's is 1 day, for the same reason.

### BT10 (TESTER-WRONG, then AMBIGUITY)

The case: the same split for a material shareholder selling an association operation.
I decided that the middle part is taxed at up to 25% for a material shareholder, copying the ITO s 91(b1)(1)(a)(2).
Hebrew of the Real Estate Taxation Law s 48A(b1)(1)(ב): `על השבח הריאלי לאחר יום התחילה ועד למועד השינוי – בשיעור כאמור בסעיף 121 עד 20%`, with no proviso for a material shareholder.
Only the third part has the 30% for an association operation (s 48A(b1)(1)(ג) refers to (b)(1) or (1א)).
So the middle part stays at 20% and my expected value is wrong; the encoding is right.
Removing the 5 points on the middle part (326,492.87 x 5% = 16,324.64) from my 318,876.17 gives 302,551.53; the encoding returns 302,566.50, the remaining 15 being the Starting Day count above.

### BT19, BT20, BT22, BT23 (AMBIGUITY)

The case: the exempt part of (b2): `שבח ריאלי עד יום המעבר`, the ratio of `התקופה שמיום הרכישה ועד ליום המעבר` to `התקופה שמיום הרכישה ועד ליום המכירה`.
I decided that the Transition Day (1 January 2014) is not in the exempt part; the encoding counts it.
Arithmetic for BT23 (purchase 1 June 2013, sale 1 June 2014, real betterment 300,000): decided 214 days of 366, tax 31,147.54; the encoding counts 215 days of 366, tax 30,942.62; the difference is one day: 300,000 / 366 x 25% = 204.92.
The text does not say whether `עד יום המעבר` includes the day; AMBIGUITY.
BT21 (purchase on the Transition Day) passed once I set the (b2) flag to false for it, since the field is `it is a qualifying residential apartment that section 48A(b2) governs`, and (b2) needs a purchase `לפני יום המעבר`.

### BT27 (AMBIGUITY)

The case: a qualifying apartment bought in 2005 to which the conditions of (b4) apply.
I decided plain (b)(1) at 25% on the whole real betterment; the encoding keeps it in (b1) (its assumption A14), giving 93,807.85 for a real betterment of 400,000.
Hebrew of (b4): `על אף האמור בסעיפים קטנים (ב2) ו־(ב3), במכירת דירת מגורים מזכה בידי יחיד שיום רכישתה היה לפני יום המעבר, ומתקיימים לגביה שני אלה, יחולו הוראות סעיף קטן (ב)(1) ולא יחולו הוראות סעיפים קטנים (ב2) ו־(ב3)`.
Hebrew of (b1): `על אף האמור בסעיף קטן (ב)(1), במכירת זכות במקרקעין, למעט במכירת דירת מגורים מזכה שחלות לגבי מכירתה הוראות סעיפים קטנים (ב2) ו־(ב3)`.
(b4) says in terms that (b)(1) applies, which is my reading.
(b1) opens `notwithstanding (b)(1)` and its only exception is a sale to which (b2) and (b3) apply, and (b4) makes them not apply, which is the encoder's reading.
Two `על אף` clauses collide and the text does not rank them.
AMBIGUITY, the encoder's own Q6; the encoder's choice is textual, mine purposive.
The sibling case with a 2013 purchase (where (b1) does not apply) passed.

## 3. Refused assertions

Each of these is an `#ASSERT value` that the encoding declines.
The encoding gives a reason for each; the class is mine.

| lines | ids | class | what |
| --- | --- | --- | --- |
| 543, 545, 553 | CG20, CG22 | SCOPE | the s 88 parts of the real gain for a sale before the change date or the fixed date; the definitions in s 88 have no date limit, and the encoding's guards are wider than its assumption A6 needs; impact is low because the rate sections decline those dates anyway |
| 680, 1319, 1321 | T30, BT16, BT17 | SCOPE | a sale before 1 January 2012, declined by name (assumption A6); expected by the lead |
| 799 | DV21 | AMBIGUITY | a dividend on 29 February 2024 and a holding on 28 February 2023: whether the 12 months begin on 29 February 2023 (which does not exist) or 1 March 2023; the encoding is right to decline, and my value 25% assumed the later reading |
| 1443, 1455, 1457, 1459, 1463 | PT37, PT43, PT44, PT45, PT47 | SCOPE | purchase tax for a single dwelling between 16 January 2022 and 15 January 2025: the table in the source prints the 2022, 2023 and 2024 columns, so these were answerable from the text; the encoding encodes the 2025-2027 amounts only (its assumption A15) |
| 1465, 1467, 1471 | PT48, PT49, PT51 | SCOPE | the 2013 nominal column of the same table and the (c1b)(2) scale, printed in the source, not encoded |
| 1475, 1477 | PT53, PT54 | SCOPE | the windows of (c1b)(1) and (c1a)(1) before July 2013; the printed amounts are indexed and the encoding leaves them out |

## 4. Refusals that matched the decided refusals

These are asserted with `#ASSERT REFUSED` and counted as satisfied: T08 (the boundary day of the 12 months), DV04 and DV16 (the same boundary), T38 (the order of the three parts across a bracket line), DV22 and DV23 (dividends before 2012), IN22 (interest before 2012), T55 (spreading of a listed security), S802 (no request), S804 (a difference older than six years), RT03 and RT04 (rent that is business income, or abroad), TC01 (the regulations of s 64A1 are not shown), KB08, KB09, KB10 (a separate computation without its three conditions), PT42, PT46, PT50, PT52, PT55 and PT60 (purchase tax figures not in the sources).
The date and figure refusals are what the lead expected for dates before 2012 and before 2025 and for the 2028 indexation.

## 5. Where the encoding and the decided answers agree, and the tester's readings that the encoding confirmed

- The Rounding Order: all 56 grid cases and the s 15 base rule agree, including every tie; the encoder's argument that the floor reading and the nearest-multiple readings give the same figure is right (my RO notes say the same).
- Section 88: relatives, the s 97 proviso, material shareholder alone or with a relative, the chargeable inflationary amount, and the three-part day count under the `both counted` reading (the pairing I decided) agree exactly.
- Sections 91, 125B, 125C and 122: every rate, cap and boundary asserted agrees, including the (f) year counts under the readings I chose, the (b1) three-part tax with the first part at the layered rate, and the s 122(f) deduction up to 90,000.
- Section 8(c), 64A1, 64A2, 57, 55(b), 60A(b)(2): all asserted cases agree.
- Real Estate Taxation Law s 9: every 2025-2027 band and the 28 November 2021 to 31 December 2026 and 1 January 2027 switch agree, including 105,342 on 2,000,000 from 1 January 2027.
- Real Estate Taxation Law s 48A(d): all 18 ceiling rates agree under the readings I chose.

## 6. Decided cases with no assertion (SCOPE or no entry point)

The cases listed here have an `-- id: reason` comment in `tests-independent.l4` and no assertion.

- RO62 to RO70: s 120B(a), (b) and (e) indexation and the 2028 base; the encoding takes the Order's join only (indexation is row IL-03).
- K12 to K15, K18 to K20, MS09, MS10: ties the text omits (cousin, uncle's spouse, in-laws), additive holdings inside the 25% test, and indirect holdings through a chain; the encoding takes the largest fraction as given (its assumption A3) and has no constructor for a tie that is not a relative.
- CG10, CG11: a gift or an inheritance as a sale (inert).
- T22, T35 to T37, T39 to T44, T56: the missing 1993 index, purchase days at the change date (covered by the split cases), the s 94B reduction, the s 91(d) reports, and the filing condition on spreading.
- IN23: the Minister's order under s 125C(c)(2).
- RT05, RT06, RT14, RT17, RT18: deductions and credits lost under s 122(c), the household total, advances, and the exemption ceiling of the 1990 law.
- S806, S812, S818 to S822: a classification of allowances, fractions of a year, the Director's period, the s 8(d) death or winding-up provision (declared 'not finished'), advances paid, and patents.
- TC04, TC05, TC11, TC15, TC16, TC19, TC21, TC23, TC30, TC31: the count of shareholders as one, the single class of shares, the 60-day notice, the distribution consequences and the buyer's price; the encoding takes these as Booleans or inputs.
- RF09, RF15 to RF28: the kind of an item of income, passing breaks, `מקרקעין`, long-term lease, the purchase windows, sale to a lessor, issue assets and the defining period; inert definitions in the encoding.
- KB06, KB14, KB17, KB19 to KB24: the surtax of s 121B, a part-transferred or part-reported income, and who is a member of a kibbutz.
- RL06 to RL10: the adjusted remaining value and the later expenses of s 47 (the real betterment is an input), and the tax year of s 47.
- BT07, BT26, BT46 to BT55: the Director's permission, s 48A(b3), the (d)(4) exclusions, a sale in February 2013, the ordinary-tax comparison before 2012, and the spreading of s 48A(e) (declared 'not finished' in the encoding).
- PT27, PT28, PT32 to PT36, PT56 to PT59: residence within two years of purchase, the exact 24-month day, contractor delivery timing, the couple as one buyer, the 20% share, commercial land, and association operations; Booleans the caller supplies or not encoded.

## 7. What I got wrong, after re-reading the Hebrew

- BT10: the 25% for a material shareholder in the middle part belongs to ITO s 91(b1)(1)(a)(2), not to the Real Estate Taxation Law (section 2, BT10).
- In `DECIDED-ANSWERS.md` section M I called the base index date of s 9(c1c) (`15 בינואר 2027`) garbled.
  It is not: after the freeze of the amounts for 2025 to 2027, the first adjustment on 16 January 2028 compares the latest index with the index of 15 January 2027, which is a deliberate reset.
  The same date appears in s 121B(e).
  The encoding read it correctly and uses it as the base index.
- In the same section I wrote that the answers for 15 January 2025 and the 2022 to 2024 columns were decidable; they are decidable from the table, but the encoding was entitled to scope them out, hence SCOPE and not OURS-WRONG.

## 8. What the encoder read from the source, checked line by line

- All 435 `-- src:N |` quotation lines in the 18 rules and nouns modules were compared token by token with line N of the source file they name (the Ordinance, the Order, and the Real Estate Taxation Law); none differs.
- The dates and figures I compared against the source agree: the fixed date 1 January 2003, the change date 1 January 2012, the Starting Day 7 November 2001, the Transition Day 1 January 2014, the (c1f) start of 28 November 2021, the 2025 purchase-tax bands (1,978,745; 2,347,040; 6,055,070; 20,183,565; and for (c1c)(1) 1,465,800 and 4,397,380), the 90,000 of s 122(f), the 12%/15%/20%/25%/30% rates, the 60 and 90 days of s 64A1, and the 4-year ceiling and 70% test of s 64A2.
- One slip in naming: the module and fork register for s 9(c2) call the unit `5 shillings` ("nearest multiple of 5 shillings"); the Hebrew is `מכפלה של 5 ש״ח`, five shekels.
  The arithmetic uses 5, so no value is affected.
- No wrong figure, date or Hebrew quotation was found.

## 9. Covered thinly

- The day-count apportionments (sections B, C and L) rest on one pairing of end days; a different pairing moves values by a few shekels, and the encoding's fork covers both.
- The kibbutz tax in s 57(a) was tested with credit points of 2.25 and 2.75 points at 2,904 NIS and the 121(a) scale; the tester's reading that a kibbutz's business income is not personal-effort income is untested against the encoding because the scale is an input.
- Sections 8(c)(d), 48A(e) and 91(d) have no entry point, as expected.
- Section 120B(a), (b) and (e) (indexation and the 2025 to 2027 freeze) are row IL-03's and were tested only through the Order's rounding.
- The surtax of s 121B was kept out of every case.
