# Notes: ITO residence and sources (s 1, s 2(2)(b), s 2A, s 14(b)) with the residence and value Regulations (row IL-29)

Version 0.1.0, status `draft`; no domain expert has read this against the source, and no independent test pass has been run yet.
Semi-cleanroom: nothing of the Axiom Foundation was read, and this file has no comparison with theirs.
Run `IL-29-20261008`, encoder `enc-il-29`.

## 1. What is encoded, and what is not

**s 1 "Israeli resident", for an individual (paragraph (a)).**
The centre of life is the test.
The text says it is found on "the whole" of his family, economic and social ties, and names five (home; where he and his family live; usual occupation or employment; active and material economic interests; activity in organisations).
That weighing is evaluative, so it is an input here: a recorded finding (in Israel or outside it), or the five ties.
Where no finding is made, two presumptions put the centre of life in Israel: 183 days or more in the tax year; or 30 days or more in the tax year and 425 or more in that year and the two before it.
A part of a day is a day.
Either the individual or the assessing officer may rebut them.
The day counts are encoded exactly, from counts or from a list of stays (arrival day and departure day both count; two stays that share a day are refused rather than counted twice).
The Regulations of 5766-2006 under paragraph (4) are encoded: reg 2 deems some individuals residents (an employee of the State, and one of the other listed employers within five years of beginning to work for it abroad) and reg 3 deems eight classes foreign residents.
s 14(b)'s adjustment year (not regarded as resident for one year from arrival, if he gave notice within 90 days) displaces the definition.

**s 1 "Israeli resident", for a body of persons (paragraph (b)).**
Incorporated in Israel, or control and management of its business exercised in Israel, except where they are exercised by an individual who became a first-time resident or a veteran returning resident within the last ten years (or by someone on his behalf), on the proviso's conditions.
s 14(b)(2)(b) adds the adjustment year to those ten years.

**s 1 "foreign resident".**
One who is not an Israeli resident, and also an individual outside Israel 183 days or more in each of the tax year and the next, whose centre of life (found by paragraph (a)(1)) was not in Israel in the two tax years after those.
The second limb is a fork; the two statuses are answered separately and may both hold (section 5, fork BS).

**s 1 "tax year".**
Twelve months from 1 January, or a special assessment period where one was set.

**s 2(2)(b), with VEH, VTP, TEL.**
The monthly value of the use of a vehicle: the adjusted consumer price times the rate of use value (2.43% to 2.6%, by the 2010 weighted price), rounded to the nearest ten shekels, less the temporary provision's reduction for a hybrid, plug-in or electric vehicle; an L3 motorcycle has a fixed amount.
The monthly value of a mobile telephone: the lower of half the monthly expense and NIS 115 (2023 to 2027), less what the employee paid.
The value for a tax year is the monthly value times the months.

**s 2A.** Winnings are taken into account and deemed income on the territorial terms of s 2, except the three exceptions of (b), and not for the set-off of losses.

**Not encoded (and why).**
s 2(2)(a) and s 2's other nine sources, which IL-08 encodes as the caller's classification of an item.
The ten-year exemption of s 14(a) and the other periods in s 14(b)(2)(a), (c) to (h), which are other sections' business; only the definition of "תושב חוזר ותיק" in s 14(a) is encoded because the proviso of paragraph (b)(2) and s 14(b) use it.
The Vehicle Expenses Deduction Regulations of 5755-1995, whose definition of "רכב" VEH reg 1 adopts: not deposited, so the caller states that the vehicle is one (needs a source).
The Minister's determinations under s 2A(b)(3): not deposited, so the caller states whether one reaches the winnings (needs a source).
Any other regulation under paragraph (4) of the definition: only the 2006 Regulations are deposited (needs a source if there are others).
When a special assessment period is set: the sections that set one are not in this row; the period is an input.
The ordinary ITO sections that read residence (rows IL-01, IL-08).

## 2. Files

| file | lines | what |
| --- | ---: | --- |
| `ito-il29-nouns.l4` | 344 | every record, enumeration and the readings of every fork; `DECLARE`s only |
| `ito-il29-time.l4` | 279 | the tax year; the count of days in Israel from stays; the matching of a window of time with a tax year (four readings); the tax-year gate; the choice of one value among the values the readings allow |
| `ito-s1-israeli-resident-individual.l4` | 450 | s 1 (a)(1) to (3); s 14(a) veteran returning resident; s 14(b); RES regs 2 and 3; the whole of (a) (`@export`) |
| `ito-s1-israeli-resident-body.l4` | 100 | s 1 (b) with the exception and s 14(b)(2)(b) (`@export`) |
| `ito-s1-foreign-resident.l4` | 146 | s 1 "תושב חוץ" with the second limb (`@export`, individual and body) |
| `ito-s2-charge-and-s2a.l4` | 97 | s 2's territorial charge on both statuses, s 2A (`@export`) |
| `ito-il29-published-figures.l4` | 113 | the adjusted caps and reductions the Wikisource notes print; NOT LAW |
| `ito-s2-2b-vehicle-value.l4` | 291 | VEH regs 1 and 2, VTP reg 1 (`@export`) |
| `ito-s2-2b-phone-value.l4` | 112 | TEL regs 1 and 2; the value for a tax year (`@export` twice) |
| `ito-il29-test-people.l4` | 611 | constructors for the people the tests ask about (written by hand), and the readings of the forks one and two at a time (generated by `tools/gen_readings.py`); no assertions |
| `ito-il29-tests-individual.l4`, `ito-il29-tests-body-and-foreign.l4`, `ito-il29-tests-charge-and-s2a.l4`, `ito-il29-tests-vehicle.l4` | 369, 200, 65, 322 | 117, 38, 18, 85 assertions (258 in all) |
| `tools/srcquote.py`, `tools/hebcheck.py` | | generate and check the Hebrew quotations (five sources) |
| `tools/gen_readings.py` | | regenerates the readings section of `ito-il29-test-people.l4` |

Imports in l4 resolve only beside the importing file; this row imports only its own modules, `prelude` and `daydate`.
No module of another row is vendored and none was edited.

## 3. Coverage table

No row is left `deferred`.
Line numbers are those of the deposited files (ITO = the Ordinance; RES, VEH, VTP, TEL as in `SOURCE-LICENSE.md`).

| provision | disposition | where / why |
| --- | --- | --- |
| ITO s 1 "תושב ישראל" (a) chapeau, ITO:143-144 | encoded | centre of life is a finding or five ties (input) |
| (a)(1), ITO:145-150 | encoded as inputs | `The ties of an individual`; weighing not computed; fork C1 |
| (a)(2)(a), (b) and "יום", ITO:151-154 | encoded exactly | `a presumption that the centre of life is in Israel arises on …`; stays count a part of a day as a day |
| (a)(3), ITO:155 | encoded | rebutted by either: one flag; fork C2 for what a rebuttal finds |
| (a)(4)(א)-(ו), ITO:156-162 | encoded through RES | employer classes in `An employer named in paragraph (4) of the definition` |
| note ITO:163 | inert | cites the Regulations |
| (b)(1), (2), ITO:164-166 | encoded | `ito-s1-israeli-resident-body.l4`; forks PY and W |
| "תושב חוץ" first limb, ITO:167 | encoded | not an Israeli resident |
| "תושב חוץ" second limb (א), (ב), ITO:168-169 | encoded | forks YD, PD |
| "שנת מס", ITO:202 | encoded | calendar year, or a special assessment period given |
| "חבר בני אדם", ITO:124 | read | the definition of the body in (b) |
| s 2 chapeau, ITO:210 | encoded | `s 2 — the charge reaches income produced or accrued in Israel`, on both statuses; fork BS |
| s 2(1), (2)(a), (3) to (10), ITO:211-245 | out-of-scope | the sources of income: row IL-08 (the caller classifies the item) |
| s 2(2)(b), ITO:217-220 | encoded through VEH, VTP, TEL | the notes at ITO:218-220 name the three Regulations |
| s 2A (a), (b)(1)-(3), ITO:247-252 | encoded | `ito-s2-charge-and-s2a.l4`; (b)(3) determinations are an input |
| s 14(a) exemption, ITO:1138 | out-of-scope | the ten-year exemption is not in the row |
| s 14(a) "תושב חוזר ותיק", ITO:1140 | encoded | `s 14(a) — a veteran returning resident:` |
| s 14(a) "תושב חוזר", (c), (c1), (d), ITO:1151-1160 | out-of-scope | the five-year exemption of a returning resident, and the Minister's extension: other sections' business |
| s 14(b)(1), ITO:1141 | encoded | election in 90 days, one year; forks N90, W |
| s 14(b)(2)(b), ITO:1144 | encoded | the ten years of s 1 (b)(2) run from the arrival if he elected |
| s 14(b)(2)(a), (c)-(h), ITO:1143, 1145-1150 | out-of-scope | periods in other sections (75B1, 75B, 75D1, 97, 134B, 135); (e), (g), (h) were deleted for those who became resident from 2026 |
| s 14(c1), (d), ITO:1159-1166 | out-of-scope | an expired subsection and the Minister's extension of the periods |
| RES intro, RES:10 | read | the power in (a)(4) |
| RES reg 1, RES:15-18 | encoded | "עולה חדש" is s 35(d) (a flag); "שירות צבאי" excludes career service (the caller's `service ended` date); the foreign athlete and journalist are s 75A's |
| RES reg 2(1), (2), RES:21-23 | encoded | `regulation 2 deems him an Israeli resident …` |
| RES reg 3 and (1) to (8), RES:26-34 | encoded | `regulation 3 deems him a foreign resident …`; forks F5Y, JA, W |
| RES reg 4, RES:37 | inert | commenced 1 January 2006; the row answers tax years from 2024 |
| VEH reg 1, VEH:16-33 | encoded | the adjusted consumer price; the consumer price (list or personal import); "רכב" refers to a regulation not deposited |
| VEH reg 2(a), VEH:36-49 | encoded | the rate of use value (ten bands), rounding to ten shekels; fork MP |
| VEH reg 2(b), VEH:50 | encoded | the L3 motorcycle amount, published adjusted figures |
| VEH reg 3, VEH:53-54 | published figures | adjustment on 1 January and rounding to ten: the indices are not named; the adjusted amounts are in the published module |
| VEH regs 4, 5 and the Schedule, VEH:57-62 | inert | repeal of the 1980 Regulations; application from 1987; the Schedule is repealed |
| VTP reg 1(a), VTP:15-18 | encoded | the three kinds of vehicle (`The drive of a vehicle`) |
| VTP reg 1(b), (c), (d), VTP:19, 21, 23 | out-of-scope | the periods ended on 31 December 2021, before the first tax year the row answers |
| VTP reg 1(b1), (c1), (d1), (d2), VTP:20, 22, 24, 25 | encoded | `the monthly reduction of the temporary provision …`; fork SCH |
| VTP reg 1(e), VTP:26 | encoded | a plug-in vehicle gets (d1) and not also (c1) |
| VTP reg 1(f), VTP:27 | published figures | the adjusted reductions |
| TEL reg 1, TEL:16-17 | encoded | "הוצאה חודשית", "הועמד לרשות העובד" |
| TEL reg 2, TEL:20 | encoded | half the expense or the ceiling, less what the employee paid; the workplace-only telephone excluded |
| TEL reg 3, TEL:23 | published figures | s 120B adjustment and rounding to five |
| TEL reg 4, TEL:26 | inert | from 1 May 2002 |

## 4. Assumptions (not forks): what the encoding assumed rather than read

- **A1.** Every rule answers tax years from 2024 only, as row IL-08 does (its assumption A1: the deposited text is the Ordinance as consolidated on 2026-10-06; the capstone composes the two).
  s 14's last listed amendment is תשפ״ד־4 (Hebrew year 5784, ended 2 October 2024); whether that amendment touched s 14(b) and from when is not checked (needs a source).
  The published figures begin in 2024 too.
- **A2.** A tax year after the ones a note prints (the cap after 2026, the motorcycle amount after 2026, the telephone ceiling after 2027, the reductions outside the year in their note) is REFUSED, "needs a source".
- **A3.** A window of N years that runs from a day ends on the day before the Nth anniversary; the anniversary itself is outside.
  The text says "במשך עשר שנים מהמועד" (s 14(a)) and "טרם חלפו עשר שנים מהמועד" (s 1 (b)(2)), not which.
  Where the tax year's edge falls on that day the readings of fork W might otherwise move; the effect of one day is not forked.
- **A4.** Two stays of one individual that share a day (including the departure day of one and the arrival day of the next) are REFUSED.
- **A5.** Reg 3(7)'s patient must have been hospitalised during the tax year itself (`days of hospitalisation in the tax year` at least 1); the text says "חולה המאושפז" in the present tense.
  Hospital days of the two earlier years still count in the "but for" test of the three-year presumption.
- **A6.** VTP reg 1(b1), (c1), (d1), (d2) print the classes "1M או 1N" where (b), (c), (d) print "M1 או N1".
  The row reads "1M" and "1N" as class M1 and N1 (a transposition in the Wikisource text; the class is that of Traffic Regulations reg 271A(d), not deposited).
  The official Reshumot text is linked in the source's header and not deposited (needs a source).
- **A7.** Readings of different forks are combined independently.
  Where one fork's reading (for example the matching of a window) in fact binds several provisions at once, the encoding is more cautious than the text requires: it may decline where a joint reading would answer.
- **A8.** Regulation 3 is consulted only where the definition makes the individual a resident (paragraphs (1) to (3), by finding or presumption), and regulation 2 only where it does not, as their prefaces say.
  Section 14(b) is consulted first, as it opens "על אף האמור בפסקה (א) להגדרה".
- **A9.** The five years of reg 2(2) run from "היום שהחל היחיד לעבוד אצל אותו מעביד מחוץ לישראל" (the day he began to work for that employer outside Israel); the caller supplies it.
- **A10.** The inputs of the vehicle value (the original price on the later of the day of first registration and 1 January of that year; the sum of the daily prices; the divisor "365 or the number of days since the model's first registration"; the indices known on 1 January; the exchange rates; the weighted price in 2010) are the caller's.
  The text's "לפי העניין" (as the case may be) for the divisor is the caller's choice.
- **A11.** A vehicle that is not of class M1, N1 or L3 takes reg 2(a) (price times rate) with no reduction.
  A plug-in vehicle first registered before 2010 is a hybrid vehicle (VTP:18) and meets (b1)'s fork; an electric vehicle registered before 2010 is reached by no provision.
- **A12.** s 2A(a)'s "למעט לענין קיזוז הפסדים" is read as stating that s 2A itself does not deem the winnings income for the set-off of losses; whether set-off is available is for the set-off sections, which are not in the row.
- **A13.** The Wikisource notes that print the adjusted amounts are not the Minister's.
  They are carried as `ito-il29-published-figures.l4` with their source line and hash and nothing is derived from an index.
  The notes are consistent with a factor of 1.15 on the 2022 amounts (1,150 / 1,000; 1,380 / 1,200; and 500 x 1.15 = 575 printed as 580), which would be half-up rounding of a midpoint at ten shekels.
  That is an inference about practice from three numbers, not law, and it is not used (fork MP still declines).

## 5. Fork register

Every fork is a switch in `The readings of the forks of row IL-29`, passed to the rules.
The first reading of each is the default and declines: **ruled by Meng 2026-10-08 (SHRUG)**, where the readings give different answers to the question asked; where they agree the default answers.
F26 is carried from row IL-08.
The tests set each fork to every reading.

| fork | question | readings (text that licenses each) | default |
| --- | --- | --- | --- |
| F26 (carried from IL-08) | No finding of the centre of life, and no presumption arises: is he a non-resident? | A: the absence of a presumption is not a finding (ITO:151, "חזקה היא … בישראל"); the only basis for FALSE would be a finding. | declines by name (not a switch; the tests assert it) |
| C1 ties | The five ties all lie in Israel (or all outside) and no finding was made: do they find the centre of life? | A: the text lists them among the factors of a weighing of the whole ("מכלול", "בין השאר", ITO:145); B: ties that all lie one way find it there. | declines (A) |
| C2 rebuttal | A presumption arose, was rebutted, and no finding says where the centre of life then is: is he a non-resident? | A: the text says the presumption can be rebutted (ITO:155) and not that a rebuttal places the centre of life abroad; B: it does. | declines (A) |
| W windows | How is a period that runs from a day (one year from arrival, ten years from becoming a resident, five years from beginning work abroad, three or five years of a stay, until the end of service) matched with a tax year it begins or ends inside? | whole: the tax year lies wholly in it; some day; last day (31 December) in it; count: the tax year is among the first N tax years from the tax year of the start (for windows in years). | declines where they differ |
| N90 ninety days | "תוך 90 ימים מיום הגעתו" (ITO:1141): is the 90th day after arrival in time? | A: the day of arrival is not counted, so the 90th day after it is in time; B: the day of arrival is the first day, so the 90th day counting it is in time. | declines at the 90th day only |
| F5Y five years | Reg 3: "בחמש שנות המס הקודמות … היה תושב חוץ" (RES:26): in every one of the five years, or in one? | A: every one; B: at least one. | declines where the list is mixed |
| JA journalist or athlete | Reg 3(8) uses the s 75A terms, which are defined as a "תושב חוץ" (ITO:2640, 2642): can one who is an Israeli resident be one? | A: the terms describe what he came to Israel to do; B: s 75A makes him a foreign resident, so the class is empty for one the definition makes a resident. | declines |
| YD years deemed | For which tax year does the second limb deem a foreign resident (ITO:168 "בשנת המס ובשנת המס שלאחריה")? | A: the first year of the pair (the "tax year" of the definition); B: both years of the pair. | declines where they differ |
| PD partial day | Second limb (א): "שהה מחוץ לישראל 183 ימים": is a day partly in Israel a day outside? The part-day rule is for paragraph (2) only ("לענין פסקה זו", ITO:154). | A: counts as outside; B: does not. | declines where the sum crosses 183 |
| BS both statuses | A person who is an Israeli resident and, by the second limb, also a foreign resident: which status does the charge of s 2 read? | A: the foreign resident status prevails; B: the Israeli resident status prevails (worldwide income). | answers where the item is produced in Israel (charged either way); declines for income from abroad |
| PY part-year connection | A body whose control and management were in Israel for only part of the tax year (and the ten years of the exception that end inside it): resident? | A: any part of the tax year; B: only throughout. | declines |
| MP midpoint | VEH reg 2(a): "מעוגל לסכום הקרוב … 10": a midpoint (… 5 shekels): up or down? | A: up; B: down. | declines at an exact midpoint only |
| XD excess deduction | A reduction (VTP) or the employee's payment (TEL reg 2 "בניכוי") larger than the value: nil or negative? | A: nil; B: negative. | declines where it occurs |
| SCH old schedule | VTP (b1) reduces "the amounts in the Schedule", repealed (VEH:62): for a hybrid registered before 2010, is the reduction taken from the monthly value under reg 2(a), or none? | A: the reduction is taken from reg 2(a)'s value; B: no reduction. | declines |
| DEP depreciation base | VEH reg 1 "פחת שימוש" is 1% a month "בתוספת" the other items: of what? | A: of the sum of the customs value, customs, purchase tax and VAT; B: of the customs value alone. | declines |
| PMD part month of depreciation | The same: a part of a month of depreciation. | A: counts as a month; B: does not. | declines |
| PM part month of use | The Regulations fix a value "לכל חודש": a part of a month of use. | A: counts as a month; B: prorated by days; C: does not count. | declines |

Considered and not forked: the "1M/1N" classes (assumption A6); whether reg 2(1) is subject to the proof "אלא אם כן הוכיח אחרת" (it closes reg 2(2) only, as RES:23 punctuates it; a test asserts it); the 90-day notice dated before arrival (a named refusal, since the text does not say it is within 90 days).

## 6. Answer table

Hand-worked from the Hebrew; every cell is asserted in the tests.
The tests set a tax year of 2026 unless the cell says otherwise.

**Day-count presumptions (no finding, no ties, no rebuttal), defaults.**

| days in the tax year / in the year before / in the one before that | presumption | answer |
| --- | --- | --- |
| 183 / 0 / 0 | arises ((a)(2)(a)) | resident |
| 182 / 0 / 0 | no | declined (F26) |
| 30 / 200 / 195 (sum 425) | arises ((b)) | resident |
| 30 / 200 / 194 (sum 424) | no | declined |
| 29 / 365 / 365 | no (29 < 30) | declined |
| 200, rebutted, no finding | arose, rebutted | declined (C2); not resident on reading B |
| 10, finding "in Israel" | n/a | resident (the finding governs); 200 days with finding "outside" is not resident |

**s 14(b), arrival 1 March 2026, notice 15 April 2026, finding "in Israel".**

| reading of the window | tax year 2026 | tax year 2027 |
| --- | --- | --- |
| whole tax year in the window | resident (the adjustment year does not cover all of 2026) | resident |
| some day of the tax year in the window | not resident | not resident |
| last day of the tax year in the window | not resident | resident |
| count of tax years from the tax year of the start | not resident | resident |
| default | declined | declined |

Tax year 2028 (past every reading): resident.
Notice on 30 May 2026 (the 90th day): in time on reading A of N90, late on B; on 31 May, late on both.

**Regulation 2(2), local authority, began abroad 1 March 2022 (five years to 28 February 2027).** Tax year 2026: deemed resident on every reading; 2027: declined (some day yes, whole and last day no); 2028: not.

**The vehicle, monthly (rate 2.5%, W = 130,000).**

| case | monthly value |
| --- | ---: |
| registered 2024, tax year 2024, listed 200,000 | 5,000 |
| listed 200,500 | 5,010 |
| listed 200,200 (a midpoint, 5,005) | declined; up 5,010; down 5,000 |
| listed 570,000, tax year 2024 (cap 563,790) | 14,090 |
| listed 600,000, tax year 2026 (cap 596,860) | 14,920 |
| registered 1 February 2025, tax year 2026, listed 200,000, index 105/100, ordinary | 5,250 |
| the same, hybrid / plug-in / electric | 4,670 / 4,100 / 3,870 |
| average price 230,000, exchange rates 4.2 and 4.0, index 104/100 | 5,720 |
| average 190,000 / 199,000 / 198,000 | 4,940 / 5,200 / 5,150 |
| L3 motorcycle, tax year 2024 / 2025 / 2026 | 1,010 / 1,040 / 1,070 |
| personal import, 12 months, base the sum / the customs value alone | 5,320 / 5,050 (declined by default) |

**The mobile telephone, tax year 2026.**

| monthly expense / paid by the employee | value |
| --- | ---: |
| 200 / 0 | 100 |
| 300 / 20 | 95 |
| 230 / 0, 232 / 0, 400 / 0 | 115 |
| 200 / 120 | declined (nil or negative: -20); 200 / 100 gives 0 |

## 7. What `check.sh` prints

Run from 2026-10-08T23:48:15Z to 23:48:30Z as `L4=/Users/mengwong/.local/bin/l4 ./check.sh`, `JL4_LIBRARY_PATH` unset.
`l4` is `~/.local/bin/l4` which resolves to `jl4-0.1-6df1397b`, sha256 `f0759b2ef2f1d1b2a577c68f059c54f487de9d913553fc9f0d9bf0f7f5dab0d8`, the same before and after the run.

```text
module                                    errors satisfied  failed  refused  expected
ito-il29-nouns.l4                              0         0       0        0         0
ito-il29-published-figures.l4                  0         0       0        0         0
ito-il29-test-people.l4                        0         0       0        0         0
ito-il29-tests-body-and-foreign.l4             0        38       0        0         0
ito-il29-tests-charge-and-s2a.l4               0        18       0        0         0
ito-il29-tests-individual.l4                   0       117       0        0         0
ito-il29-tests-vehicle.l4                      0        85       0        0         0
ito-il29-time.l4                               0         0       0        0         0
ito-s1-foreign-resident.l4                     0         0       0        0         0
ito-s1-israeli-resident-body.l4                0         0       0        0         0
ito-s1-israeli-resident-individual.l4          0         0       0        0         0
ito-s2-2b-phone-value.l4                       0         0       0        0         0
ito-s2-2b-vehicle-value.l4                     0         0       0        0         0
ito-s2-charge-and-s2a.l4                       0         0       0        0         0
TOTAL (14 modules)                             0       258       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
hebcheck: 109 source quotations verified line by line; 0 problem(s)
```

Exit status 0.

No assertion is expected to fail or to refuse: every refusal is asserted with `#ASSERT REFUSED … BECAUSE`, which counts as satisfied.
Two refusal messages in the vehicle tests were first written from the function's name rather than its text and were corrected to the REFUSE string of the encoding; no expected value was changed.
One expected message in the second-limb tests was mis-pasted (it named the fork refusal where the hand derivation was the missing-finding refusal) and was corrected before any conclusion was drawn from the run.

## 8. Composing this into the capstone (row IL-55): what is needed

The capstone (row IL-07) takes one Boolean per earner, `the earner was an Israeli resident in the tax year, under the Income Tax Ordinance` (adapters `il07-adapter-il01.l4`, `il07-adapter-il02.l4`, `il07-adapter-il08-ito.l4`).
Row IL-08 encodes s 1 (a) and s 2 but its record `An individual's year, for the definition of Israeli resident` is not built by the capstone.
To derive the Boolean from this row instead:

1. **Call** `s 1 "Israeli resident" (a): an Israeli resident in the tax year of` with `An individual in a tax year, for the definition of Israeli resident` and the readings (`the default readings of row IL-29`).
   The answer is a BOOLEAN or a refusal by name; the capstone must carry the refusal (an earner with no finding and fewer than 183 days is declined, as IL-08 declines).
2. **New inputs the capstone does not supply today:**
   - the tax year as `A tax year` (`the calendar tax year`), and the two before it;
   - the days in Israel of **each** of the three tax years (IL-08 took the three-year sum; the presumption needs the sum but the validation and reg 3(7) need the years), or the stays;
   - a finding of the centre of life, or the five ties;
   - whether the presumption was rebutted;
   - for reg 2: the employer, whether employment began while resident, the day he began to work abroad, any proof otherwise;
   - for reg 3: whether he is a new immigrant, the foreign residence of the five preceding years, the class and its facts, the arrival day;
   - for s 14(b): first-time or veteran returning resident, arrival day, day of notice;
   - for the second limb: for the tax year and the three after it, days wholly and partly outside Israel and the finding of the centre of life;
   - for a body: the incorporation, control and management, the exception's facts.
3. **Replace** IL-08's input conventions (`regulations made under paragraph (4) reach the individual`, `section 14(b) reaches the individual in the tax year`) by these facts: they are derived here.
4. **For s 2:** IL-08's `s 2 — the item is within the charge of section 2, for a person who is an Israeli resident:` takes one Boolean; with the second limb a person can be both, so use `s 2 — the item is within the charge, for a person who is an Israeli resident:` … `and a foreign resident:` … (fork BS).
5. **s 2(2)(b):** where the capstone's earner has a company car or a telephone, call `s 2(2)(b) — the monthly value of the use of a vehicle …` and `… a mobile telephone …` and `the value for the tax year …`; the 2010 weighted price and the indices are inputs.
6. **Vendor** the non-test modules beside the capstone's (an l4 import resolves only beside the importing file): `ito-il29-nouns`, `ito-il29-time`, `ito-s1-israeli-resident-individual`, `ito-s1-israeli-resident-body`, `ito-s1-foreign-resident`, `ito-s2-charge-and-s2a`, `ito-il29-published-figures`, `ito-s2-2b-vehicle-value`, `ito-s2-2b-phone-value`.
   Record their sha256 and say so in the capstone's NOTES.
7. The capstone's own gate (tax years from 2024) and this row's agree.
8. **Not edited:** IL-08, the capstone.

## 9. Open questions for a domain expert

1. Does the second limb of "תושב חוץ" deem the individual a foreign resident for the first tax year of the pair only, or for both (fork YD)? Does it displace being an Israeli resident, or may a person be both (fork BS)?
2. Is a rebutted presumption itself a finding that the centre of life is abroad (fork C2)? Do ties that all lie one way find the centre of life (fork C1)?
3. How is a period that runs from a day matched with a tax year (fork W)?
4. Did amendment 5784-4 change s 14(b), and from when (assumption A1)?
5. Has the Minister made other regulations under paragraph (4) of the definition? Are there determinations under s 2A(b)(3)?
6. What are the Vehicle Expenses Deduction Regulations of 5755-1995's definition of "רכב"?
7. By what index are the amounts of VEH reg 3(a) and VTP reg 1(f) adjusted? (VEH reg 3 does not say; TEL reg 3 names s 120B.)
8. What is the 2010 weighted price of VEH reg 2(a), as published?
9. Which Wikisource notes were editorial, and what does the official publication print for the adjusted amounts (the published module)?
10. Which provisions set a special assessment period (s 1 "שנת מס")?
