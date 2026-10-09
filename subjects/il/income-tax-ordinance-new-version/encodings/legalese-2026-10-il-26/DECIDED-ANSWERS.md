# IL-26 decided answers: withholding on salary (ITO s 164; Deduction from Salary and Wages Regulations 5753-1993)

Written by fid-il-26 from the Hebrew sources alone, before opening the encoding directory.
Sources read: the regulations (`registers/source-bundle/regulations/income-tax-deduction-from-salary-and-wages-regulations-5753-1993.he.wiki.txt`) and the ITO text (`income-tax-ordinance-new-version.he.wiki.txt`: s 33A line 1563, ss 34, 36, 36A, 37, 39A, 40, 40B, 40C, 40D, s 66(c), s 120B line 4337, s 121 line 4349 with the 2019-2027 table, s 121B line 4455, s 164 line 5322).
Arithmetic was done with a script (`calc.py` in this scratch dir) and every figure was checked against the rules below.
"Reg" means the 1993 regulations; "Sch A/B/C" the three Schedules; "item n" the numbered item of the Schedule.

## The figures I take from the ITO text (tax year 2026, same as 2027)

- Rates for a salaried individual (personal-effort income, s 121(b)(1); the (b)(2) bookkeeping carve-out does not touch salary): to 84,120 at 10%; to 120,720 at 14%; to 228,000 at 20%; to 301,200 at 31%; to 560,280 at 35%; above that 47% (the table row headed 2027-2026, ITO line 4440 area).
- Additional tax: 3% of annual taxable income above 721,560 (s 121B(a), note "2024-2027, 721,560"); the 2% on capital income does not reach salary (s 121B(e), "income from personal effort" is excluded from capital source).
- Credit point: 2,904 per year for 2024-2027 (s 33A note); 2,820 for 2023.
- Tax year 2024-2025 brackets: 84,120; 120,720; 193,800; 269,280; 560,280; 721,560.
- Tax year 2023 brackets: 81,480; 116,760; 187,440; 260,520; 542,160; 698,280 (the table has typos in two lower bounds, "116,711" and "187,481"; I take the upper bounds, which are consistent).
- Section 120B(e)(1) freezes the figures for 2025-2027 at their 1 Jan 2024 values, so 2025, 2026 and 2027 use the same credit point; the 2025 brackets differ from 2026 only in the 20% and 31% bands.
- Tax years 2028 and later, and 2022 and earlier credit-point values: not in the sources, so "needs the published figure".
- Standard credit points: s 34 gives 2; s 36 gives 1/4; so a resident man has 2.25 and a woman has 2.75 (s 36A adds 1/2).
- s 37 adds 1 for an eligible individual whose spouse depends on them (retirement age or blind or disabled).
- s 40(b)(1) for a single parent and s 66(c)(4)/(5) for a married working parent: for a child in the tax year after the year of birth until the year the child turns two, 4.5 points to a woman (2.5 in the birth year, 3.5 in the year the child turns three, 2.5 in the years the child turns four and five, and 2 from the year turning six).
- s 39A, 40B, 40C, 40D give the other points Item 3 lists.

## The method (Schedule A items 1 to 5) and the readings I take

Item 1: monthly salary x 12.
Item 2: tax on that sum by ss 121 and 121B with the s 120B adjustments.
Item 3: subtract the credit points the employee is entitled to under ss 34, 36, 36A, 37, 39A, 40, 40B, 40C, 40D, 66(c), as declared on the employee card (Form 0101).
Item 4: divide the tax after credits by 12; that quotient is deducted from the month's salary.
Item 5: a fraction of a shekel exceeding 49 agorot of the salary or of the tax counts as a shekel; a fraction of 49 agorot or less is disregarded.
Item 6: the Director will publish a table; once he has, the employer deducts by that table.

- R1 (table not held, the question put to me): the table in item 6 is a published aid to items 1-5, not a separate rule.
  Reg 3(a) tells the employer to deduct "tax as set out in Schedule A", and items 1-5 are that tax.
  So an employer who does not hold the Director's table computes by items 1-5, and the answer is the figure in this document.
  Confidence M.
  The alternative reading (no table, no lawful figure, the employer must obtain the table) would make the encoding refuse; I count that an AMBIGUITY if the encoding does so.
  If the table is held, I take it to prevail, but its figures are not in the sources, so any case that depends on table values "needs the published figure".
- R2 (floor): if the credit points exceed the annual tax the monthly deduction is zero, not negative (s 33A: the point is "set off against the tax").
  Confidence M.
- R3 (rounding): item 5 is applied to the final monthly tax and to the salary.
  I round the monthly tax once, at the end of item 4, and in bonus cases I round each monthly-tax figure before taking the difference, because reg 4 speaks of "the tax to be deducted from the monthly salary", which is the rounded Schedule A figure.
  Rounding of the salary before item 1 changes nothing in any case below, so I use whole-shekel salaries.
  The 49-agorot test is read as: fraction above 0.49 goes up (so 155.50 goes to 156).
- R4 (maximal rate): "השיעור המרבי" is the highest rate in s 121, which is 47% (reg 1).
  Reg 6(k) adds the s 121B additional tax only to reg 6 deductions, so the reg 5(a)/(b) flat 47% is just 47%, not 50% even for a very large salary.
  Confidence M.
- R5 (no rounding rule outside the Schedules): flat-rate deductions (47%, 35%, 25%, 40%) are exact, with no item 5 rounding; the Schedules' item 5 covers only the Schedules.
  Confidence L; I use whole-shekel results wherever possible.
- R6 (which year): the tax year of the payment date, with the 1 Jan to 13 Jan reporting rule (regs 12(b), 13(c)) left to reporting only.
  2026 and 2027 use identical figures, so the boundary is immaterial for the payment amounts below.

## Cases

Unless stated: tax year 2026, an employee resident in Israel, who is a man, with a filled Form 0101, a single employer, a full month of ordinary salary, and 2.25 credit points; amounts in new shekels.
Basis column: the regulation or section and the Hebrew words the answer rests on.
Confidence: H, M or L.

### A. Schedule A, the ordinary monthly salary (2.25 points)

| ID | Facts | Decided answer | Basis | Conf |
|---|---|---|---|---|
| A01 | salary 3,000 | 0 (annual 36,000 x 10% = 3,600 less 6,534, floored) | Sch A items 1-5, R2 | H |
| A02 | salary 5,445 | 0 (annual 65,340 x 10% = 6,534, less 6,534 = 0) | items 2-4 | H |
| A03 | salary 5,446 | 0 (tax after credits 1.20 a year, 0.10 a month, disregarded under item 5) | item 5 "שאינו עולה על 49 אגורות" | H |
| A04 | salary 6,000 | 56 (annual 7,200 less 6,534 = 666; 666/12 = 55.5 rounds up) | items 3-5 | H |
| A05 | salary 7,000 | 156 (8,400 less 6,534 = 1,866; 155.5 rounds up) | item 5 | H |
| A06 | salary 7,010 (annual exactly 84,120, top of the 10% band) | 157 | s 121(b)(1)(a) | H |
| A07 | salary 7,011 (first shekel in the 14% band) | 157 | s 121(b)(1)(b) | H |
| A08 | salary 8,000 | 295 | items 1-4 | H |
| A09 | salary 10,000 | 575 (annual 120,000: 8,412 + 14% x 35,880 = 13,435.20 less 6,534 = 6,901.20; /12 = 575.1) | items 1-5 | H |
| A10 | salary 10,060 (annual 120,720, top of 14%) | 584 | s 121(b)(1)(b) | H |
| A11 | salary 10,061 | 584 | s 121(b)(1)(c) | H |
| A12 | salary 12,000 | 972 | items 1-5 | H |
| A13 | salary 15,000 | 1,572 | items 1-5 | H |
| A14 | salary 19,000 (annual 228,000, top of 20%) | 2,372 | s 121(b)(1)(c) | H |
| A15 | salary 19,001 | 2,372 | s 121(b)(1)(d) | H |
| A16 | salary 25,100 (annual 301,200, top of 31%) | 4,263 | s 121(a)(1), (b)(1)(d) | H |
| A17 | salary 25,101 (35% begins) | 4,263 | s 121(a)(2) | H |
| A18 | salary 40,000 | 9,478 | items 1-5 | H |
| A19 | salary 46,690 (annual 560,280, top of 35%) | 11,819 | s 121(a)(2) | H |
| A20 | salary 46,691 (47% begins) | 11,819 | s 121(a)(3) | H |
| A21 | salary 60,130 (annual 721,560, the 121B threshold) | 18,136 | s 121B(a) "עלתה על 640,000" (note: 721,560) | H |
| A22 | salary 60,200 (annual above the threshold, 3% on 840) | 18,171 | s 121B(a) | H |
| A23 | salary 61,000 | 18,571 | s 121B(a) via item 2 "121 ו־121ב" | H |
| A24 | salary 100,000 | 38,071 (annual 1,200,000: 148,362 + 47% x 639,720 + 3% x 478,440 less 6,534, /12) | item 2 | H |
| A25 | same facts as A09, tax year 2025 | 575 | s 120B(e)(1) freeze; 2025 band 14% to 120,720 | M |
| A26 | salary 20,000, tax year 2025 (31% band starts at 193,800 annual, not 228,000) | 2,995 (2026 gives 2,682) | 2024-2025 table row | M |
| A27 | salary 25,000, tax year 2025 | 4,647 | 2024-2025 table row | M |
| A28 | salary 10,000, tax year 2023, 2.25 points at 2,820 | 616 | 2023 table row and s 33A note | M |
| A29 | salary 10,000, tax year 2028 | needs the published figure (2028 indexation, s 120B(e)(2)) | s 120B(e)(2) | H |
| A30 | salary 10,000, tax year 2022 | needs the published figure (credit-point value for 2022 is not in the sources) | s 33A note | H |

### B. Schedule A item 3, the credit points

| ID | Facts | Decided answer | Basis | Conf |
|---|---|---|---|---|
| B01 | salary 12,000, woman (2.75 points) | 851 (2.25 points gives 972) | s 36A "1/2 נקודת זיכוי" | H |
| B02 | salary 12,000, man whose spouse depends on him and one of them is of retirement age (3.25 points) | 730 | s 37 | M |
| B03 | salary 12,000, man discharged soldier, 23+ months service, all twelve months within the 36 months (adds 12 x 1/6 = 2 points; 4.25 points) | 488 | s 39A(1); item 3 lists 39A; monthly translation M | M |
| B04 | salary 12,000, first academic degree, tax year after the degree ends (3.25 points) | 730 | s 40C(a) | M |
| B05 | salary 15,000, woman who is a single parent of one child born in 2024, tax year 2026 (turns two: 4.5 points; 2.75 + 4.5 = 7.25) | 362 | s 40(b)(1) "עד לשנת המס שבה מלאו לו שנתיים" | M |
| B06 | salary 15,000, married working mother of one child born 2024, tax year 2026, 7.25 points | 362 | s 66(c)(4)(a), item 3 "66(ג)" | M |
| B07 | B05 facts, salary 5,000 | 0 | R2 | H |
| B08 | B05 facts, salary 20,000 | 1,472 | items 1-5 | M |
| B09 | new immigrant entitled to s 35 points, salary 10,000 | s 35 is not in the item 3 list, so the employer credits only listed points (575) unless the assessing officer directs otherwise under reg 9(a)(4); the reduced figure needs the assessing officer's direction | item 3 list; reg 9(a)(4) | M |
| B10 | combat reservist with 45 service days, salary 10,000 | s 39B is not in the item 3 list, so no automatic credit (575); a credit needs a direction under reg 9(a) | item 3 list; reg 9(a) opening | M |

### C. The Director's table (item 6)

| ID | Facts | Decided answer | Basis | Conf |
|---|---|---|---|---|
| C01 | table not held, salary 10,000 | compute by items 1-5: 575 | R1; reg 3(a) "מס כמפורט בתוספת א׳" | M |
| C02 | table not held, salary 7,000 | 156 | R1 | M |
| C03 | table held, any salary | the table's figure; its values are not in the sources, so "needs the published figure" | item 6 "ינכה המעביד את המס של עובדיו לפי אותו לוח" | H |
| C04 | table not held and the employer treats that as "no deduction possible" | wrong on R1; if the encoding refuses here, AMBIGUITY | item 6 "יפרסם" | M |

### D. No card, incomplete card, additional position (reg 5(a))

| ID | Facts | Decided answer | Basis | Conf |
|---|---|---|---|---|
| D01 | no Form 0101, salary 10,000 | 4,700 (47%) | reg 5(a) "או שלא מילא טופס 0101"; reg 1 "השיעור המרבי" | H |
| D02 | Form 0101 filled but the "other income" section left blank, salary 10,000 | 4,700 | reg 5(a) "שלא מילא את הסעיף העוסק בפרטים על הכנסות אחרות" | H |
| D03 | employee started 1 Oct 2026, card handed in 5 Oct, first pay 31 Oct, salary 10,000 | 575 (the card is held at payment) | reg 5(a), reg 2(a)(1) | M |
| D04 | employee declared on Form 0101 an additional position with the employer, salary 10,000 | 4,700 | reg 5(a) "משכורת בעד משרה נוספת שעליה הצהיר העובד" | H |
| D05 | no Form 0101, salary 100,000 | 47,000 (47%, not 50%) | R4 | M |
| D06 | no card, salary 3,333 | 1,566.51 (exact, R5) | reg 5(a), R5 | L |
| D07 | additional position, with an assessing-officer direction to deduct 30% | 3,000 | reg 5(e)(1) | M |
| D08 | additional position, assessing officer's lower rate not supplied | needs the assessing officer's direction (reg 5(e)(1)); the default is 4,700 | reg 5(e)(1) | M |

### E. Partial salary, pension, Form 0130 (reg 5)

| ID | Facts | Decided answer | Basis | Conf |
|---|---|---|---|---|
| E01 | partial salary 3,000, no Form 0130 | 1,410 | reg 5(a) | H |
| E02 | partial salary 3,000, Form 0130 filed (no other taxable income) | 0 (Sch A) | reg 5(c) | H |
| E03 | partial salary 7,000, Form 0130 filed | 156 | reg 5(c) | H |
| E04 | pension 9,000, no Form 0130 | 4,230 | reg 5(b) | H |
| E05 | pension 9,000, Form 0130 filed | 435 | reg 5(c) | H |
| E06 | pension 10,000 of which 5,700 is exempt, no Form 0130 | 2,021 (47% x 4,300) | reg 9(c) "לא ינכה מס מהחלק הפטור" | M |
| E07 | partial salary 7,000, Form 0130 filed, then the employee reports other taxable income | 3,290 (47%) | reg 5(d) | H |
| E08 | additional-position salary 10,000, Form 0130 filed | 4,700 (Form 0130 covers partial salary, pension and day wage only) | reg 5(c) "ההכנסה היחידה" | M |
| E09 | works 5 hours a day, 22 days a month, salary 3,000 | partial salary: 1,410 | reg 1 "חמש שעות ליום או פחות" | H |
| E10 | works 6 hours a day, 20 days a month, salary 10,000 | ordinary monthly salary: 575 | reg 1 "משכורת חלקית"; "משכורת חודש" | H |
| E11 | works 6 hours on one day a week (6 hours a week), salary 1,000 | partial salary: 470 | reg 1 "יותר מחמש שעות ליום, אולם פחות משמונה שעות בשבוע" | H |
| E12 | 18 days of 8 hours in the month, salary 10,000 | monthly salary: 575 | reg 1 "למעט עבודה של פחות מ־18 ימים" | H |
| E13 | 17 days of 8 hours in the month, one employer, wage 500 a day | day worker: Schedule B (see J) | reg 1 "עובד יומי" | H |
| E14 | 12 days of 4 hours a month (about 11 hours a week), one employer, wage 300 a day | AMBIGUITY: both "partial salary" (5 hours or fewer a day) and "day worker" (under 18 days, at least 8 hours a week) fit; I take partial salary (47%, 1,410 on 3,000 for a month of 12 days) because reg 5(a) names it and reg 5(a) does not name day wages; the alternative is Schedule B | reg 1; reg 5(a) | L |

### F. Part payments (reg 3(b))

| ID | Facts | Decided answer | Basis | Conf |
|---|---|---|---|---|
| F01 | monthly salary 10,000 paid as 6,000 and 4,000 | 345 and 230 (575 x 6/10 and x 4/10) | reg 3(b) "חלק יחסי מהמס שיש לנכות ממשכורת החודש" | H |
| F02 | monthly salary 10,000, 5,000 paid now | 287.50 exact (R5), or 288 | reg 3(b) | L |

### G. Bonuses, unfixed salary and retirement grants (regs 4, 7)

Reg 4(a) formula: tax = 12 x (T(S + B/12) - T(S)), where T is the Sch A monthly tax (rounded).

| ID | Facts | Decided answer | Basis | Conf |
|---|---|---|---|---|
| G01 | monthly salary 10,000, bonus 12,000 | 2,364 (T(11,000) = 772, T(10,000) = 575, x 12) | reg 4(a) | M |
| G02 | salary 10,000, bonus 60,000 | 11,964 (T(15,000) = 1,572) | reg 4(a) | M |
| G03 | salary 20,000, bonus 100,000 | 32,544 | reg 4(a) | M |
| G04 | salary 5,000, bonus 6,000 | 72 (T(5,500) = 6; T(5,000) = 0) | reg 4(a) | M |
| G05 | salary 10,000, bonus 1,000 | 156 (T(10,083) = 588, difference 13, x 12) | reg 4(a) | L |
| G06 | salary 59,000, bonus 24,000 (crosses the 121B line) | 11,592 | reg 4(a); item 2 | M |
| G07 | unrounded variant of G01 (no item 5 rounding inside the difference) | 2,356.80; AMBIGUITY between G01 and this; I take G01 | reg 4(a) "המס שיש לנכות" | M |
| G08 | bonus 6,000 to an employee of a bankrupt company, salary 10,000 (formula 1,164, which is under 25%) | 1,500 (25% floor) | reg 4(a) "בשיעור שלא יפחת מ־25%" | H |
| G09 | bonus 100,000 to such an employee, salary 10,000 (formula 19,956) | 25,000 | reg 4(a) | H |
| G10 | day worker, wage 500 a day, bonus 3,000 | 600 (300 x (T_day(510) - T_day(500)) = 300 x (45 - 43)), points 2.25 assumed | reg 4(b) | L |
| G11 | retirement grant, taxable portion 100,000, last salary 20,000, employee not a day worker | 32,544 (as bonus G03) | reg 7(a)(1) | M |
| G12 | retirement grant, taxable 60,000, last pay was for half a month (8,000) but a full month would be 16,000 | 14,640 (S = 16,000, as bonus) | reg 7(a)(1) "המשכורת האחרונה שהיתה משתלמת... בעד חודש שלם" | M |
| G13 | grant wholly exempt under s 9(7A) | 0 | reg 7(a)(1) "מהחלק שאינו פטור" | H |
| G14 | grant for a day worker | the rate the assessing officer directs; needs the assessing officer's direction | reg 7(a)(2) | H |
| G15 | bonus 120,000 to an employee who was paid no salary in that month | literal formula gives 6,900 (T(10,000) x 12 with S = 0); AMBIGUITY, the text has no clause for it; L | reg 4(a) | L |
| G16 | retirement grant paid by an employer that is not a provident fund while the fund also pays, taxable total 100,000, last salary 20,000 | 32,544 on the whole grant the employer pays, unless the assessing officer directs otherwise | reg 7(b)(1) | M |
| G17 | retirement grant of 80,000 (taxable part) paid in kind, cost to the employer 70,000, market price 80,000; last salary 20,000 | valued at the higher figure, 80,000; tax 25,548 | reg 7(c), reg 8(a) | M |

### H. Payment in kind (reg 8)

| ID | Facts | Decided answer | Basis | Conf |
|---|---|---|---|---|
| H01 | cash salary 10,000 plus goods cost to employer 800, market price 1,000 | goods valued at 1,000; salary for withholding 11,000; tax 772 | reg 8(a) "לפי הגבוה" | H |
| H02 | goods cost 1,200, market 1,000, cash 10,000 | 1,200; salary 11,200; tax 812 | reg 8(a) | H |
| H03 | use of a car | value by the vehicle-use regulations; needs the published figure | reg 8(b) | H |

### I. Foreign workers in a private household (reg 3(d), Schedule C)

| ID | Facts | Decided answer | Basis | Conf |
|---|---|---|---|---|
| I01 | non-resident man, salary 6,000 | 600 (no credit points) | Sch C items 1-4 | H |
| I02 | non-resident woman, salary 6,000 | 479 (half point, 1,452 a year) | Sch C item 3 "חצי נקודת זיכוי" | H |
| I03 | non-resident man 3,000 | 300 | Sch C | H |
| I04 | non-resident woman 3,000 | 179 | Sch C | H |
| I05 | non-resident man 12,000 | 1,516 | Sch C | H |
| I06 | non-resident woman 12,000 | 1,395 | Sch C | H |
| I07 | foreign worker who is an Israeli resident, private household | by Schedule A or B as appropriate; the points are not declared on a card (reg 2(a) excludes foreign workers), so I cannot fix the figure; AMBIGUITY | reg 3(d)(2); reg 2(a) | L |
| I08 | foreign national employed by a company, not by a household | ordinary rules (not "משכורת לעובד זר"); card required | reg 1 "משכורת לעובד זר" | M |

### J. Day workers (reg 3(c), Schedule B; points assumed 2.25 as input because day workers have no card)

| ID | Facts | Decided answer | Basis | Conf |
|---|---|---|---|---|
| J01 | wage 200 a day | 0 | Sch B items 1-5 | M |
| J02 | wage 300 a day | 9 (annual 90,000: 9,235.20 less 6,534 = 2,701.20; /300 = 9.0) | Sch B | M |
| J03 | wage 400 a day | 23 | Sch B | M |
| J04 | wage 500 a day | 43 | Sch B | M |
| J05 | wage 1,000 a day | 169 | Sch B | M |
| J06 | day worker, points not given | AMBIGUITY (no card, item 3 refers to "הנקודות המגיעות לכל עובד"); needs the points | Sch B item 3 | L |
| J07 | lump sum 10,000 paid to several day workers, individual shares unknown | 3,500 (35%) | reg 6(i) | H |
| J08 | lump sum to day workers, one worker also takes wages from another employer for 18 days or more | still 35% | reg 6(i) "לרבות יחיד המקבל שכר עבודה ממעביד אחר" | M |

### K. Special routes (reg 6)

| ID | Facts | Decided answer | Basis | Conf |
|---|---|---|---|---|
| K01 | a provident fund pays holiday/sick/vacation pay 4,000 | 1,000 (25%) | reg 6(d) | H |
| K02 | sabbatical payment 20,000 | 7,000 (35%) | reg 6(g) | H |
| K03 | disabled person pays an escort 8,000 | ordinary tax 295, which is under the 25% ceiling | reg 6(h) "בשיעור שלא יעלה על 25%" | M |
| K04 | disabled person pays an escort 100,000 | 25,000 (ceiling; Sch A would give 38,071) | reg 6(h) | L |
| K05 | monthly pay 12,000 including 2,000 shift pay; Form 0105 notice sent within a week | 672 (972 less 15% x 2,000 = 300; the annual cap 12,540 is not reached) | reg 6(f)(1); ITO s 10 note | M |
| K06 | same, but no Form 0105 notice | 972 (the shift credit does not apply) | reg 6(f)(2) | M |
| K07 | shift credit with annual cap | needs year-to-date credit allowed; cap 12,540 for 2024-2026 | ITO s 10 note | L |
| K08 | survivors of a deceased employee paid 200,000 | AMBIGUITY: lower of 40% (80,000) and "the rate that would have applied to the employee"; the second needs the deceased's rate and the basis (month vs bonus); I take 80,000 | reg 6(a) | L |
| K09 | survivors paid 20,000 | 2,682 (the Sch A rate 13.4% is below 40%) under the same reading | reg 6(a) | L |
| K10 | payment under s 18(b) / controlling shareholder when no monthly salary was paid, 50,000 | 23,500 (47%); the added 121B tax: AMBIGUITY, cannot compute (needs year income) | reg 6(b), 6(k) | L |
| K11 | non-resident employee who is not a household foreign worker | tax per the assessing officer's instructions; needs the assessing officer's direction | reg 6(c) | H |
| K12 | provident fund pays capitalisation of a recognised pension | 15% of the relative profit component; needs that component | reg 6(j) | H |
| K13 | employer gives a deduction/credit outside the item 3 list (donations, s 46) | no automatic deduction; needs the assessing officer's direction | reg 9(a)(8) | H |

### L. Dates and what the employer must file (regs 2, 11, 12, 13)

| ID | Facts | Decided answer | Basis | Conf |
|---|---|---|---|---|
| L01 | tax deducted from a payment on 13 Oct 2026 | report on Form 0102 and pay by 16 Oct 2026 | reg 11(a) | H |
| L02 | payment on 14 Oct 2026 | report and pay by 16 Nov 2026 | reg 11(a) "מה־14 בחודש הקודם" | H |
| L03 | household foreign worker paid on 20 Oct 2026 | Form 0102 foreign by 16 Nov 2026 (period 14 Sep to 13 Nov) | reg 11(d) | M |
| L04 | foreign worker paid on 13 Sep 2026 | by 16 Sep 2026 | reg 11(d) | M |
| L05 | foreign worker paid on 14 Nov 2026 | by 16 Jan 2027 | reg 11(d) | M |
| L06 | employer's annual report (Form 0126) for 2026 | by 31 Mar 2027 | reg 12(b) | H |
| L07 | employer stops employing on 10 Jun 2026 | Form 0126 within 14 days: by 24 Jun 2026 | reg 12(c) | H |
| L08 | employee starts on 1 Oct 2026 | card due by 8 Oct 2026 (a week from the start, or from first pay if earlier) | reg 2(a)(1) | H |
| L09 | change in card details on 3 Mar 2026 | employee notifies by 10 Mar 2026 | reg 2(d) | H |
| L10 | Form 0106 certificate | by 31 Mar of the next year, or the day employment ends | reg 13(a) | H |
| L11 | reporting of foreign-worker pay on Form 0126 | not required | reg 12(e) | H |

### M. Other

| ID | Facts | Decided answer | Basis | Conf |
|---|---|---|---|---|
| M01 | payment on 10 Jan 2027 of December 2026 salary 10,000 | 575 (the 2027 figures equal 2026); the year assignment is an AMBIGUITY but immaterial | regs 12(b), 13(c) | M |
| M02 | pension fund as employer, pension paid | an employer includes a provident fund | reg 1 "מעביד" | H |
| M03 | the registered spouse not yet confirmed in writing | treat the husband as the registered spouse | reg 1 "בן זוג רשום" | H |

## Ambiguities flagged

1. R1: the Director's table not held (C01, C04).
2. R3: rounding inside a bonus difference (G07).
3. Partial salary vs day worker overlap (E14).
4. Day worker credit points with no card (J06) and resident foreign worker points (I07).
5. Whether 121B is added to the reg 5 flat rate (D05) and to reg 6 flat rates (K10).
6. Survivors' rate (K08, K09); the escort ceiling reading (K03, K04).
7. Part-payment fractions (F02) and flat-rate rounding (D06).
8. A bonus when no salary was paid in the month (G15).
9. Shift credit conversion and cap (K05 to K07).
10. Section 39B and s 35 are not in item 3 (B09, B10).
