# Notes: National Insurance Law statuses and the surroundings of the child allowance (row IL-33)

Status: **draft, version 0.1.1** (0.1.0 plus the Retirement Age Law, section 13).
Row IL-33, run id `IL-33-20261008`, encoder `enc-il-33`, one session, no sub-agents.
No domain expert has read this against the source, and no independent test pass has been run yet (BACKLOG chain: encode, independent tests, lead re-run).
Every expected value in the tests was worked by hand from the Hebrew before the run; a failing assertion would have been a finding.
None failed.

## 1. What is encoded and what is not

The row exists because the capstone `employed-parent-monthly-net` (version 0.4.0) and rows IL-06 and IL-08 take as inputs the statuses s 335 and ss 65-66 read, and a set of surrounding provisions.
Capstone `GAPS.md` item 9 (the statuses s 335 reads) and item 13 (residence, s 238) record the first; IL-06's `NOTES.md` (the "Not encoded" paragraph) records s 69, s 69A, s 71, s 238, s 381 and the rounding regulations, the updating clause of s 1, the Income Support Law, the Maintenance (Assurance of Payment) Law and the Family Allowance Regulations.

**Encoded, in the lead's priority order.**

1. *The statuses, derived from facts.*
   Who is insured under Chapter 5 (ss 75-76), Chapter 6 (s 150), s 158 paragraphs (1), (2) and (3) of Chapter 7 with s 6B, Chapter 8 (ss 180-181), Chapter 9 (s 195), Chapter 10 (s 223) and Chapter 11 (ss 240, 243), on a day, from the person's date of birth, sex, residence, work and service; with the ages of Schedule A1 (Parts A, B, C, E) and s 1 "גיל הפרישה", which for a woman born in 1956 or later is the Retirement Age Law's (row IL-27's module, vendored).
2. *Residence and the housewife.*
   s 2A (who is not an Israeli resident) and the residence words of s 65(a); s 238 "עקרת בית" (housewife), "אלמנה" (widow), "אלמנה בת קצבה" (widow pensioner).
3. *ss 69, 69A, 71.*
   To whom the child allowance is paid; in whose count the children of a man with children by several women come; by virtue of whom the allowance is paid when a parent died or ceased to be insured.
4. *s 381 and the Rounding Regulations 5746-1985.*
5. *The rest of the row.*
   The updating clause of s 1 "הסכום הבסיסי" for the child allowance, 2015 to 2026, over the CBS index; the Family Allowance Regulations 5720-1960 (regulations 1 and 11, the only ones left); the gate of the Income Support Law 5741-1980 and of the Maintenance (Assurance of Payment) Law 5732-1972, as far as "is a benefit/payment made for this month" goes.

**Composition.**
`nii-s335-adapter.l4` builds row IL-08's record `A person in a contribution period, for section 335` from these derived statuses and calls IL-08's s 335 (IL-08's two modules are vendored unchanged, `VENDORED.sha256`).
So the capstone's thirteen hand-filled fields can come from one person record.

**Not encoded** (reasons in the coverage table): ss 132 and 252 (the widow's pension itself), s 246 (qualifying period), the Second Schedule of the Income Support Law and its Chapter 4 (income), the regulations under ss 75, 243 and under the Maintenance Law, the Entry to Israel Law and Regulations, the Security Service Law.

## 2. Coverage table

Every row is `encoded`, `inert`, `input` (the Law leaves it to another text or to a determination, which the case supplies) or `out-of-scope` with a reason.
No row is left `deferred`.
Line numbers are those of the deposited text of the provision's own Law (NII lines unless said).

| provision | lines | disposition | where / reason |
| --- | --- | --- | --- |
| s 2A(a) "שנה" (twelve consecutive months) | 244 | encoded | `nii-s2a-residence.l4` |
| s 2A(b)(1) unlawful presence; (2) Area permit; (3) visitor B/1-B/4; (3A) reg 5A; (5) A/3, A/4 | 246-249, 253 | encoded | the stay excludes residence; the visa types are taken as named (the Entry Law and Regulations are not deposited) |
| s 2A(b)(4) A/1 and (c) another visa: the two limbs and the determining year | 250-256 | encoded | fork R4 (exactly 183 days) |
| s 2A(d) the Institute may regard an A/1 holder as resident | 257 | input | `the Institute regards the holder as a resident from the day it was granted` |
| positive test of residence | — | input | the Law has none (fork R1): `lives in Israel` |
| s 65(a) "מבוטח" (2) the words "יושב בישראל", "העדר ארעי שהוא סביר" | 803 | encoded | forks R3; the opinion of the authorised employee is an input |
| s 238 "עקרת בית" | 2428 | encoded | `nii-s238-housewife.l4`; fork H1 |
| s 1 "עגונה" | 203 | encoded | inside the housewife rule |
| s 238 "אלמנה" (1), (2) | 2403-2405 | encoded | forks W1, W2 |
| s 238 "אלמנה בת קצבה" | 2429 | encoded | the entitlement to a pension under ss 132(1)-(5) or 252 is an input |
| ss 132, 252 (the widow's pension) | 1276-1290, 2545-2565 | out-of-scope | a pension model of its own (ages, children, earnings); the row needs only the fact that one is paid |
| s 238 "אלמן", "ילד", "הכנסה", "עובד מבוטח" | 2406-2430 | out-of-scope | not read by ss 65, 335, 69-71; "ילד" is read only by ss 247 and by the Income Support Law's definition, which the gate takes as an input |
| s 240(a) | 2439 | encoded | `nii-statuses-chapters.l4`; Part C for a man, the retirement age for a woman |
| s 240(b) (a woman not exempt from the qualifying period: Mark C only) | 2440 | out-of-scope | it narrows which Marks she is insured under, not whether she is insured under Chapter 11; s 335(i) has one branch for both; reads s 246's qualifying period |
| s 243 classes the Minister excluded | 2449 | input | regulations not deposited (fork C2) |
| s 246 qualifying period | 2481-2493 | out-of-scope | not read by ss 65, 335 (it is read by s 240(b) only) |
| s 75(a)(1), (2), (3)-(8) | 944-952 | encoded | the regulations that name the approved places, ordinary prison services and excluded classes are inputs |
| s 75(b) who is the employer of (3)-(8) | 953 | out-of-scope | contributions, not insurance |
| s 76 a worker abroad | 956-957 | encoded | fork C4 (class (b)) |
| s 77 registration; s 78 special provisions | 959-973 | out-of-scope | a condition of a benefit (s 77) and regulations (s 78), not of being insured |
| s 150 "מבוטח" (Chapter 6) | 1405 | encoded | |
| s 158 "מבוטח" (1) | 1444 | encoded | "תושב ארעי" undefined (fork R2) |
| s 158 "מבוטח" (2) a released soldier | 1445 | encoded | |
| s 158 "מבוטח" (3) a national-service volunteer | 1446-1447 | encoded | the temporary provision (24 months); the permanent text needs the Security Service Law s 16(1), refused by name (fork C1) |
| s 158 "מבוטח מיוחד", "תאריך קובע", s 159 | 1448-1459 | out-of-scope | the benefit's mechanics, and regulations extending the insured |
| s 6B controlling shareholder | 289-290 | encoded | |
| ss 180-181 (Chapter 8) | 1820, 1830 | encoded | a provident fund is not a person of this model |
| s 195 "מבוטח" (Chapter 9) | 1929 | encoded | |
| s 223 "מבוטח" (1), (4) (Chapter 10) | 2175, 2178 | encoded | |
| Schedule A1 Parts A, B, C, E | 4369-4428, 4456-4475 | encoded | Part D is row IL-08's |
| s 1 "גיל הפרישה" | 130-132 | encoded | a man, and a woman born up to 1955: Part A; a woman born in 1956 or later: the Retirement Age Law, ss 3, 6 and Part B, through `nii-s1-retirement-age-law.l4` over row IL-27's `retirement-age-law.l4` (section 13) |
| s 1 "עובד", "עובד עצמאי" | 204-211 | input | row IL-04's definitions; the Institute records which a person is |
| s 335 (a)-(j) | 3610-3620 | composed | row IL-08's, fed by the adapter |
| s 69 (a)-(d) | 836-840 | encoded | `nii-ss69-69a-71.l4`; forks P1, P2 |
| s 70 a parent absent from Israel directs payment | 847-848 | out-of-scope | not named by the row; the capstone's households are in Israel |
| s 69A | 842-845 | encoded | fork A1 |
| s 71 | 850-851 | encoded | fork S1 |
| s 381 | 4168-4170 | encoded | `nii-s381-rounding.l4`; fork R6 (class (b)) |
| Rounding Regulations reg 1 (definition), 2, 3, 4, 5, 6, 7 | regs 16-44 | encoded | `nii-rounding-regulations.l4`; fork R5 |
| Rounding Regulations reg 8 (repeal), 9 (transition of 1986), 10 (commencement) | regs 46-60 | inert | historic |
| s 1 "הסכום הבסיסי" (2), the updating paragraph (3), for the child allowance | 186-189, 197 | encoded | `nii-s1-updating-clause.l4`, 1 January 2015 to 2026 over the CBS data; fork U1 |
| s 1 "הסכום הבסיסי" (1), the updating paragraphs (1), (2), (4), the other benefits | 176-185, 193-196, 198-202 | out-of-scope | not the child allowance (row IL-35 reads s 334) |
| Family Allowance Regulations reg 1 | regs 19 | encoded | `nii-family-allowance-regulations.l4` |
| Family Allowance Regulations regs 2-10 | regs 21-46 | inert | each is marked cancelled in the deposited text |
| Family Allowance Regulations reg 11 | regs 49 | encoded | |
| Family Allowance Regulations regs 12, 13 | regs 52-55 | inert | commencement, name |
| Income Support Law ss 2(a), (b), (2A) | 78-96 | encoded | `isl-benefit-gate.l4`; the grounds the regulations define are inputs |
| Income Support Law s 3 (1)-(4), s 3C | 105-123 | encoded | as facts |
| Income Support Law s 3A, 3B | 114-118 | out-of-scope | a refused job offer and a repealed section |
| Income Support Law s 4(a) | 126 | encoded | s 4(b) (regulations) is not |
| Income Support Law s 5(b), s 7(b), (c), s 8 | 138, 163-167 | encoded | the benefit for a person without income and the income are inputs |
| Income Support Law s 5(a) and the Second Schedule (the rates) | 132-137, 503-521 | out-of-scope | the rate tables and the child-related deductions need the Chapter 4 income and the basic amount of the Law; the gate takes the result as an input |
| Income Support Law s 6, s 7(a), ss 9-12 (income and deductions), ss 13, 15-32 | 153-157, 161-162, 171-259, 260, 298-397 | out-of-scope | the income computation is a model of its own and needs regulations (s 7(a), s 9(b)); no household of the capstone is near it |
| Income Support Law s 14(a) | 267 | encoded | |
| Income Support Law s 14A(a) | 273 | encoded | (b)-(g): out-of-scope (counting departures and days); the Maintenance Law's s 9A is encoded, with the counts as inputs |
| Income Support Law s 23(a) | 353 | encoded | s 2A of the Insurance Law applies to "resident" |
| Maintenance Law s 1 "זוכה" | 27 | encoded | `ml-payment-gate.l4` |
| Maintenance Law s 2(a), (b) | 36-39 | encoded | "resident" is the Insurance Law's |
| Maintenance Law s 3 | 42 | encoded | the regulations' rate is an input; refused by name if absent |
| Maintenance Law s 6(a) | 52 | encoded | fork M1 |
| Maintenance Law s 9 | 66-69 | encoded | |
| Maintenance Law s 9A(b), (c), (d) | 73-83 | encoded | (c)(2) refused by name (the Minister's rules are not deposited) |
| Maintenance Law ss 4, 5, 6(b), 7, 8, 8A, 10-23, the Schedule | 44-153 | out-of-scope | procedure, collection, penalties |

## 3. Fork register

Every row is **ruled by Meng 2026-10-08 (SHRUG)**: where the text is silent or two readings are arguable and give different answers to a question someone would ask, one named switch, default decline, the other readings kept by name and tested, the default declining only where the readings differ.
`rd` is the record `The readings this row takes where the text does not decide` (`nii-il33-nouns.l4`), with `the readings this row takes` as the default and a setter per field (`nii-il33-readings.l4`).
"Class" follows IL-08's convention: (a) a switch; (b) only one reading is arguable, no switch; (c) an input convention; (d) not made a switch for a stated reason.

| id | provision, lines | the readings | default | class |
| --- | --- | --- | --- | --- |
| R1 | s 2A, 241-257: the Law gives no positive test of residence | none: a person is a resident if section 2A does not exclude the stay and the case says he lives in Israel | `lives in Israel` is an input | (c) |
| R2 | s 158 "מבוטח" (1), 1444: "תושב ארעי" is not defined in the deposited text | none | an input flag, the residence test not applied | (c) |
| R3 | s 65(a) "מבוטח" (2), 803, with s 2A: is "יושב בישראל" the "תושב ישראל" of s 2A? | (i) yes, so s 2A's exclusions apply; (ii) a matter of fact, whatever s 2A says | declined only for a person s 2A excludes who in fact lives in Israel | (a), `rd`'s `the words sits in Israel in section 65(a)` |
| R4 | s 2A(b)(4), (c), 251-256: "fewer than 183" and "more than 183"; exactly 183 | (i) with fewer; (ii) with more; (iii) neither limb applies, as the words read | declined only where the three give different answers on the day asked | (a), `exactly 183 days in section 2A` |
| DATE | Schedule A1, "an age in years and months": the day it is reached when the later month lacks the day of birth (born 29 February, 31st) | (i) the last day of the shorter month; (ii) the 1st of the next month | declined only on the days the two differ (the same ruling as IL-08 N4, IL-05 F19, IL-06 F2) | (a), `the day an age is reached` |
| Q1 | s 1 "גיל הפרישה" (2), 132: a woman born in 1956 or later, "the age fixed under the Retirement Age Law 5764-2004" | **no longer a fork** (0.1.1): the Law is deposited and decides, by s 3 (65 for a woman) and Part B (born May 1947 to December 1969); 0.1.0's switch and its floor reading were removed | the Law's age | resolved |
| C1 | s 158 "מבוטח" (3), 1446-1447: two texts of the paragraph (permanent; temporary provision to 31 August 2026) | the temporary provision (24 months, and civil-national service) for a service begun before 31 August 2026; the permanent text measures against s 16(1) of the Security Service Law, not deposited | a service begun on or after that day is refused by name unless the woman's proviso decides | (d) a source is missing, so a refusal, no switch |
| C2 | s 243, 2449: classes the Minister excluded; the Institute may insure one on request | none | two inputs | (c) |
| C3 | s 75(a)(2), 946, with s 76, 956: does the insurance of the self-employed reach work outside Israel? | (i) wherever the work is done; (ii) only in Israel | declined where the person works outside Israel | (a), `a self-employed person who works outside Israel` |
| C4 | s 76(a), 956: "even if the contract was not made in Israel and ..." dispenses with the place of the contract only, or with the residence of both parties too | the first is the only arguable reading: the other insures two foreign parties on a foreign contract under this Law | the first | (b) |
| C5 | s 75(a)(1) with s 76: an employee abroad who does not meet s 76(a) | s 76 is the only way in; reading s 75(a)(1) as covering every employee wherever he works would leave s 76(a) with nothing to say | not insured | (b) |
| H1 | s 238 "עקרת בית", 2428, with s 1 "אשתו", 129: "אשה נשואה" (a married woman) or also a woman known in public as the wife and living with him | (i) married only; (ii) also the woman known in public | declined only where the answer depends on it (she is otherwise a housewife) | (a), `the word married in the definition of a housewife` |
| W1 | s 238 "אלמנה" (2), 2405: the "or" between "not entitled to maintenance" and "the insured did not in fact bear her maintenance" | (i) inside the condition of separation; (ii) an alternative to the whole | declined only where they differ (not separated and he bore no maintenance) | (a), `the maintenance limb of the definition of a widow` |
| W2 | s 238 "אלמנה" (1), 2404: the age of 55 is at the death, at the marriage, or now | at the death ("בשעת פטירתו" opens the definition and the condition is in the present tense) | at the death | (b) |
| P1 | s 69(a), 837: a child whose two parents are of one sex | none | refused by name | (d) no arguable reading |
| P2 | s 69(b) "ישלם" (shall pay) and (d) "רשאי" (may) both in the case | (i) the request prevails; (ii) the decision prevails | declined where they differ | (a), `a request under section 69(b) and a decision under section 69(d)` |
| P3 | s 69(a): is the mother paid only if she is herself entitled? | no: that would leave an entitled father and a mother who is not entitled with nobody to pay but a guardian | the mother is paid whether or not she is entitled | (b) |
| A1 | s 69A(1), 844: "a child as in s 68(b)", the fourth or later in the count of the parent's children, born before 1 June 2003: whose count | (i) all the man's children; (ii) each woman's | declined where they differ | (a), `a child as in section 68(b), for section 69A(1)` |
| A2 | s 68(b), s 69A(1): how the count is ordered | eldest first by date of birth (IL-06's F4); one of the children born before 1 June 2003 is the fourth or later exactly when four or more were born before that day | eldest first | (d) |
| S1 | s 71, 851: both parents died or ceased to be insured | (i) the parent s 67(b) would choose if both were alive and insured; (ii) the parent who died or ceased first | declined where they differ | (a), `section 71 where both parents died or ceased to be insured` |
| R5 | Rounding Regulations reg 3, with s 68(c), 826: is the supplement rounded with the allowance as one amount or on its own | (i) one amount; (ii) on its own | declined where the child's total differs (2025 figures, a fourth child born before 2003: 489 against 490) | (a), `the child allowance and the supplement of section 68(c), for rounding` |
| R6 | s 381, 4169: "if it has no other provision" attaches to "any other law" (its "בו" is singular), not to "this Law" | the first | the Regulations govern amounts under this Law whatever another law says | (b) |
| U1 | s 1 "הסכום הבסיסי" (3), 197: "the rate of RISE of the index"; when the index published last fell | (i) a fall leaves the amount as it was; (ii) a fall lowers it | declined where the rounded amounts differ (every update from 1 January 2016, so every year after 2015) | (a), `a fall in the index, in the updating clause of the basic amount` |
| U2 | the rise from the index values or from the CBS twelve-month percentage | none arguable: the two give the same amount in every year 2015 to 2026 (tested) | the index values | (b) |
| U3 | is the updated amount rounded each year, and the next update taken from the rounded amount | yes: Rounding Regulations reg 4 rounds "an amount computed under the Law and used to fix the rate" of the payments of regs 2 and 3 | rounded to whole shekels each year | (b) |
| FA1 | Family Allowance Regs reg 11, 49: "not more than ninety days after the doubt arose" | the 90th day after is within the limit; the clearing day ends the suspension | inclusive | (b) |
| M1 | Maintenance Law s 6(a), 52: a month in which the period of payment begins or ends partway | (i) paid in full; (ii) not paid | declined | (a), `a month in which the period of payment begins or ends partway` |

**What the default declines, in practice.**
With the Retirement Age Law in, no status declines for want of a retirement age.
The defaults decline only the cases of the forks above (a visitor who lives in Israel, exactly 183 days, a day an age falls on that the month lacks, and so on).

## 4. Answer tables

All on 15 January 2026, from the tests, at the default readings.

### 4.1 Statuses of the two ordinary persons

| status | Avi (a man born 10 March 1988, employee in Israel) | Batya (a woman born 20 June 1990, not working) |
| --- | --- | --- |
| Chapter 5 | insured | not |
| Chapter 6 | insured | insured |
| s 158(1) | insured | not |
| Chapter 7 with s 6B | insured | not |
| Chapter 8 | insured | not |
| Chapter 9 | insured | insured |
| Chapter 10 | insured | insured |
| Chapter 11 | insured | insured |
| housewife (married to Avi) | not | **yes** |
| s 335 branches | all nine | accident injury, disability, long-term care |

### 4.2 s 335 for other persons

| person | branches in which contributions are payable |
| --- | --- |
| a visitor on a B/2 visa, working in Israel as an employee | maternity, work injury, employees' rights in insolvency |
| a widow pensioner (born 1990, widowed, with a pension) | children, accident injury, disability, long-term care |
| the same widow without the pension | maternity, children, accident injury, disability, long-term care, senior citizens and survivors |
| Avi as a controlling shareholder | all but unemployment and insolvency |

### 4.3 The basic amount of the child allowance on 1 January (reading U1 (i), rounded each year)

| year | (2)(a) first and fifth and later child | (2)(b) second to fourth | (2)(c) Income Support / s 68(c) |
| --- | ---: | ---: | ---: |
| 2015 (denominated) | 150 | 188 | 140 |
| 2016, 2017 (the index fell) | 150 | 188 | 140 |
| 2018 | 150 | 189 | 140 |
| 2019 | 152 | 191 | 142 |
| 2020, 2021 | 152 | 192 | 142 |
| 2022 | 156 | 197 | 145 |
| 2023 | 164 | 207 | 153 |
| 2024 | **169** | **214** | **158** |
| 2025 (frozen as on 1 January 2024) | 169 | 214 | 158 |
| 2026 | **173** | **219** | **162** |

The bold figures are the ones the deposited text prints in its notes (lines 187-189: "בשנים 2024–2025, 169 / 214 / 158; בשנת 2026, 173 / 219 / 162").
Reading U1 (ii) (a fall lowers the amount) gives 167 / 210 / 156 for 2024 and 171 / 215 / 160 for 2026: it does not reproduce the printed figures.
By default every year after 2015 is declined, because the readings differ from 2016.

### 4.4 Rounding (regulation 3, each child)

| child | before rounding | rounded |
| --- | ---: | ---: |
| a fourth child born before 1 June 2003, 2026, with the s 68(c) supplement | 173 x 2.24 + 162 x 0.7 = 387.52 + 113.4 = 500.92 | 501 (also 388 + 113 = 501) |
| a third child, 2026, with the supplement | 219 + 113.4 = 332.4 | 332 |
| the same, 2025 figures (169, 158) | 378.56 + 110.6 = 489.16 | declined: 489 as one amount, 490 on its own |
| four children, 2026 (173, 219, 219 + 113.4, 219 + 113.4) | 1056.8 | 1056 (each child rounded; the total rounded would be 1057) |

## 5. `check.sh`

`L4=/Users/mengwong/.local/bin/l4 ./check.sh`, `JL4_LIBRARY_PATH` unset.
Run from 2026-10-08T23:32:32Z to 23:33:09Z, after the last edit to any module.
Binary: `~/.local/bin/l4` resolving to the cabal store's `jl4-0.1-6df1397b/bin/l4`, sha256 `f0759b2ef2f1d1b2a577c68f059c54f487de9d913553fc9f0d9bf0f7f5dab0d8`, the same before and after the run.

```
module                                    errors satisfied  failed  refused  expected
isl-benefit-gate.l4                            0         0       0        0         0
ito-il27-nouns.l4                              0         0       0        0         0
ito-il27-tax-years.l4                          0         0       0        0         0
ml-payment-gate.l4                             0         0       0        0         0
nii-family-allowance-regulations.l4            0         0       0        0         0
nii-il08-nouns.l4                              0         0       0        0         0
nii-il33-fixtures.l4                           0         0       0        0         0
nii-il33-nouns.l4                              0         0       0        0         0
nii-il33-published-figures.l4                  0         0       0        0         0
nii-il33-readings.l4                           0         0       0        0         0
nii-il33-tests-ages.l4                         0       129       0        0         0
nii-il33-tests-fa-regs.l4                      0        14       0        0         0
nii-il33-tests-isl.l4                          0        35       0        0         0
nii-il33-tests-ml.l4                           0        38       0        0         0
nii-il33-tests-residence.l4                    0        41       0        0         0
nii-il33-tests-rounding.l4                     0        40       0        0         0
nii-il33-tests-s238.l4                         0        37       0        0         0
nii-il33-tests-s335.l4                         0        21       0        0         0
nii-il33-tests-ss69-71.l4                      0        43       0        0         0
nii-il33-tests-statuses.l4                     0        96       0        0         0
nii-il33-tests-updating.l4                     0       117       0        0         0
nii-rounding-regulations.l4                    0         0       0        0         0
nii-s1-retirement-age-law.l4                   0         0       0        0         0
nii-s1-updating-clause.l4                      0         0       0        0         0
nii-s238-housewife.l4                          0         0       0        0         0
nii-s2a-residence.l4                           0         0       0        0         0
nii-s335-adapter.l4                            0         0       0        0         0
nii-s335-branches.l4                           0         0       0        0         0
nii-s381-rounding.l4                           0         0       0        0         0
nii-schedule-a1-ages.l4                        0         0       0        0         0
nii-ss69-69a-71.l4                             0         0       0        0         0
nii-statuses-chapters.l4                       0         0       0        0         0
retirement-age-law.l4                          0         0       0        0         0
TOTAL (33 modules)                             0       611       0        0
```

Exit 0.
Many of the 611 assertions are `#ASSERT REFUSED` (declining by name is the expected answer there); `check.sh` counts them as satisfied, and no assertion fails or refuses unexpectedly.
A deliberately wrong assertion in a scratch copy failed (`assertion failed`), so the harness can fail.

`tools/hebcheck.py` (copied unchanged from IL-06) found every Hebrew run in the modules, outside the `src:` quotations, in the source file that module cites: the Law, or the regulations, or the Income Support Law, or the Maintenance Law.
The `src:` lines were generated by `tools/srcquote.py` from the line numbers in the `--@SRC` markers; no Hebrew in the quotations was typed.

## 6. Findings worth the lead's attention

1. **A derived Chapter 11 status makes a resident housewife insured under Chapter 11, and that is not what IL-06's fork F18 presupposes.**
   s 240(a) insures every resident of 18 or over; s 238's definition of a housewife asks that her *spouse* be insured under the Chapter and says nothing against her own insurance.
   So this row derives `insured under Chapter 11` = TRUE for a resident housewife, and the capstone's fixture "a resident s 238 housewife not insured under Chapter 11" is an input convention, not a reading of s 240.
   s 65(a)(1) and s 335 do not care: both carve her out by name ("למעט עקרת בית"), so IL-08's s 335 gives the same branches either way (tested: the adapter feeds the derived TRUE).
   **IL-06's limb (2) does care.**
   Its code requires `NOT insured under Chapter 11` as a conjunct before it reads the housewife's exception (`nii-s65-interpretation.l4:40-44`), so if IL-55 feeds IL-06 the derived TRUE, a resident housewife is in neither limb on every reading of F18, reading (B) included, and the fork stops being reached.
   Reading (B) as IL-06 describes it ("not [insured under Chapter 11, other than a housewife]", the noun phrase of limb (1) negated) would still make her insured under limb (2), because not (Chapter 11 and not a housewife) is true of a housewife however Chapter 11 stands; the conjunct in IL-06's code is what stops it.
   This row does not rule on F18 and does not edit IL-06.
   **Open item for IL-55** (recorded so that IL-55 sees it): this finding is unresolved.
   IL-55 has two clean choices: keep passing IL-06 `insured under Chapter 11` FALSE for a housewife (the convention, so F18 stays as IL-06 has it), or ask Meng to re-point IL-06's limb (2) to `NOT (insured under Chapter 11 AND NOT housewife)` for reading (B).
2. **(0.1.0 said women born in 1956 or later decline by default for want of the Retirement Age Law; 0.1.1 retires that finding.)**
   The Law is deposited and row IL-27 encodes it; see section 13.
3. **The deposited notes settle the CPI fork on the evidence, but not on the text.**
   Reading U1 (i) with the rounding of reg 4 reproduces all six printed figures (169 / 214 / 158 and 173 / 219 / 162); reading U1 (ii) reproduces none.
   The ruling is that the default is a decline where readings differ, so the default declines.
   Meng can turn the default to reading (i) by changing one field of `the readings this row takes`; the tests would then answer 2016 to 2026.
4. **Regulation 3 rounds each child.**
   A family of four children at the 2026 figures is 1056 when each child is rounded and 1057 when the total is rounded.
   IL-06 states its totals "before rounding" (`the family's total, before rounding`); the capstone should round per child with `reg 3 — the allowance for one child, rounded` (its fork R5 aside).
5. **The Law has no positive definition of a resident.**
   s 2A lists, "among others", who is not one.
   This row answers "is the stay excluded" exactly, and "is he a resident" only with the case's own `lives in Israel`.
6. **s 71 and s 69A now have answers, and the capstone's refusals for them can be replaced.**
   The answer says by virtue of whom, or in whose count; the amount for the deceased or non-insured parent still has to be asked of IL-06 in that parent's name (section 8).

## 7. Inputs this row takes that the capstone does not supply today (for IL-55)

The capstone's household holds the earner's sex, date of birth, salary, residence, Chapter 11 status, the earner's seven Chapter statuses (`IL-07 the earner's insurance statuses, for section 335`) and the spouse's sex, Chapter 11 status, housewife status and residence.
To derive those, the person record `A person for the statuses of the Law` needs:

| for | input | note |
| --- | --- | --- |
| everyone | date of birth; sex | the capstone has the earner's; the spouse has no date of birth in `IL-07 spouse` |
| residence | `lives in Israel`; `permission to stay` (the s 2A categories, with the visa's day and the lawful days); `absent from Israel beyond a reasonable temporary absence`; `a temporary resident` | a citizen is `no permission that section 2A names` |
| Chapter 11 | `the day the person first became an Israeli resident` | a person resident since birth: the birth date; if absent, Chapter 11 is declined by name |
| work | `an employee`; `a self-employed person`; the s 75(a) flags; `entitled to wages on which the employer must pay insurance contributions`; `a controlling shareholder` | the capstone's earner is an employee in Israel |
| housewife, widow | `A woman's marriage` (status, the two facts of an agunah); the spouse's record; `A widowing`; `A widow's pension fact` | the spouse needs the same person record |
| service | `released from regular service`, `completed national or community service` | none for the capstone's households |
| long-term care | `The absorption facts of a person`; | none for most |
| Chapter 11 classes | `The Chapter 11 facts of a person` (s 243 inputs) | none for most |

The mapping to IL-06's `A person`: `insured under Chapter 11` = `s 240 — insured under Chapter 11:`; `a housewife as defined in section 238` = `s 238 — a housewife:`; `resident in Israel` = `s 65(a) — sits in Israel:`; `absent from Israel beyond a reasonable temporary absence` = the residence facts' field; `formerly insured`, `income chargeable to additional tax` and the two payments are not derived here (the first needs a history; the second is IL-03's; the two payments are `isl-benefit-gate.l4` and `ml-payment-gate.l4`).

## 8. What the capstone would need (IL-55)

1. Vendor the modules (it resolves imports only beside the importing file): `nii-il33-nouns`, `nii-il33-readings`, `nii-schedule-a1-ages`, `nii-s1-retirement-age-law`, `retirement-age-law`, `ito-il27-nouns`, `ito-il27-tax-years`, `nii-s2a-residence`, `nii-statuses-chapters`, `nii-s238-housewife`, `nii-s335-adapter`, `nii-ss69-69a-71`, `nii-rounding-regulations`, `nii-s381-rounding`, `nii-il33-published-figures`, `nii-s1-updating-clause`, `nii-family-allowance-regulations`, `isl-benefit-gate`, `ml-payment-gate`; the vendored IL-08 modules `nii-il08-nouns` and `nii-s335-branches` it already holds are the same files (sha256 in `VENDORED.sha256`).
2. An adapter from `IL-07 earner`, `IL-07 spouse` and the further facts to `A person for the statuses of the Law`, a `A woman's marriage` and the rest, then `s 335 — the branches in which contributions are payable, from the facts of` ... in place of the hand-filled thirteen fields.
3. Per-child rounding of IL-06's amounts with `reg 3 — the allowance for one child, rounded:`, and the updating clause (`s 1 — the basic amounts of the child allowance on 1 January of`) in place of the published basic amounts only if Meng turns fork U1 to reading (i); the published figures module stays the source of the amounts until then.
4. For s 71 and s 69A: IL-06 declines by name when "section 71 may apply" or "section 69A may apply". The capstone can ask this row who the payee or count is, and then ask IL-06 for the allowance in that parent's name. IL-06's functions that take the family on a day would need the dead or uninsured parent in the family record, which this row does not edit.
5. The ISL and Maintenance gates replace IL-06's two payment flags only for a household that has such a payment; the capstone's employed parents do not.

## 9. What was assumed rather than read

- That the Rounding Regulations 5746-1985 are in force under the 1995 Law (the Law's note at line 4170 lists them).
- That the Family Allowance Regulations 1 and 11 survive: the deposited text marks regs 2-10 cancelled and says the whole is "mostly cancelled" in favour of regulations of 5758-1998 that are not deposited (line 14).
- That the temporary provision of s 158(3) covers every service begun before 31 August 2026 (the start of the provision is not in the text).
- That the index published last before a 1 January is the November index of the year before (the CBS publishes about 15 December); that the CBS twelve-month figures are the rise of one November over the last; and that the linkage values in the CBS coefficient file convert between bases.
- That `lives in Israel` means a life centred in Israel; the Law does not say.
- That the 90-day limit of reg 11 includes the 90th day after the doubt arose, and that the clearing day ends the suspension (fork FA1).
- For the Income Support Law: that a person's pension under Chapter 5 or 11 of the Insurance Law is the one flag for both s 2(b) and s 7(c); that s 7(c)'s "5(a)(2)(a)" is a person under 55 who is paid no pension.
- For the Maintenance Law: that a creditor treated as abroad under s 9A(d) is paid nothing for the month.
- That the allowance of a child is in a parent's count in order of birth, eldest first (as IL-06's F4).

## 10. Needs a source (refused by name, never guessed)

- The Security Service Law s 16(1) (the permanent text of s 158(3)).
- The Entry to Israel Law and Regulations (the visa types of s 2A; "שוהה שלא כדין").
- The regulations under s 75 (approved places of training, ordinary services of prisons and hostels, excluded classes of the self-employed), under s 243 (classes not insured) and under s 159.
- The regulations under the Maintenance Law (the rates of s 3; the Minister of Justice's exceptions under ss 9(d), 9A(c)(2)), and under the Income Support Law (the determining sums of s 7(a), the grounds of s 2(a)(1)-(3), (7), the Second Schedule's application to income).

## 11. Open questions

1. (Retired in 0.1.1: the Retirement Age Law decides.)
2. Should the default of fork U1 be reading (i), on the evidence of the printed notes?
3. Is "יושב בישראל" in s 65(a) "מבוטח" the "תושב ישראל" of s 2A (fork R3)?
4. Does s 238's "נשואה" reach a woman known in public as a wife (fork H1)?
5. s 69A(1): is "a child as in s 68(b)" measured in the count of all the man's children or of each woman's (fork A1)?
6. Is the supplement of s 68(c) rounded with the allowance or on its own (fork R5)? It matters at the 2025 figures, not at 2026's.
7. Does the Institute pay the mother whether or not she is entitled (fork P3, class (b))? Our reading follows the usual practice and the section's structure.

## 12. Files

`BRIEF.md`; `NOTES.md`; `check.sh`; `encoding.json`; `SOURCE-LICENSE.md`; `VENDORED.sha256`; `tools/srcquote.py`, `tools/hebcheck.py` (copies of IL-06's, unchanged).
Modules: `nii-il33-nouns.l4` (the nouns), `nii-il33-readings.l4` (the switches), `nii-schedule-a1-ages.l4`, `nii-s1-retirement-age-law.l4`, `nii-s2a-residence.l4`, `nii-statuses-chapters.l4`, `nii-s238-housewife.l4`, `nii-s335-adapter.l4`, `nii-ss69-69a-71.l4`, `nii-s381-rounding.l4`, `nii-rounding-regulations.l4`, `nii-il33-published-figures.l4` (CBS data, not law), `nii-s1-updating-clause.l4`, `nii-family-allowance-regulations.l4`, `isl-benefit-gate.l4`, `ml-payment-gate.l4`; the vendored `nii-il08-nouns.l4` and `nii-s335-branches.l4` (row IL-08) and `retirement-age-law.l4`, `ito-il27-nouns.l4`, `ito-il27-tax-years.l4` (row IL-27).
Tests: `nii-il33-fixtures.l4` (builders, no assertions) and `nii-il33-tests-{ages,residence,statuses,s238,ss69-71,s335,rounding,updating,fa-regs,isl,ml}.l4`.

## 13. Version 0.1.1: the Retirement Age Law (lead's instruction, 2026-10-08)

0.1.0 took the retirement age of a woman born in 1956 or later as an input because the Retirement Age Law was not deposited.
It is deposited now (`../../../retirement-age-law-5764-2004/registers/source-bundle/retirement-age-law-5764-2004.he.wiki.txt`, sha256 `633aa70f0cd151e65bccc91c1341e0784a13d93311d79b65e5a4ecedb1dfa1bd`) and row IL-27 encodes it.
**Folded into the same directory as 0.1.1** (the 0.1.0 text was never committed).

**Vendored, unedited** (`VENDORED.sha256`, byte-identical to IL-27's, checked with `cmp`): `retirement-age-law.l4`, `ito-il27-nouns.l4`, `ito-il27-tax-years.l4`, from IL-27 at commit `91142a46`.
Only `retirement-age-law.l4` is called, through `nii-s1-retirement-age-law.l4`, a short wrapper that takes the month and year of birth as numbers.
The wrapper exists because IL-27's nouns declare a sex type whose constructors are `a man` and `a woman`, and two types with one constructor name in one scope is an error (`There are multiple definitions for the identifier`).
This row's own sex constructors are therefore renamed `male` and `female` (a mechanical rename in this row's files; no vendored file changed).

**Source check (the lead's point 3).**
s 1 "גיל הפרישה" (2) (NII line 132): a woman's age is Part A of Schedule A1 by her month of birth, "and if she was born in 1956 or later, the age fixed for her in accordance with the Retirement Age Law, 5764-2004".
The Law is the one IL-27 encodes: title and year match (חוק גיל פרישה, התשס״ד–2004).
Read in the Hebrew: s 3 (line 42) 67 for a man and 65 for a woman; s 6(2) (line 55) a woman born up to December 1969 has the age of Part B by month of birth; Part B (lines 200-210) May 1947 to December 1959 is 62, then 62 and 4 months for 1960, 62 and 8 for 1961, 63, 63 and 3, 63 and 6, 63 and 9, 64, 64 and 3, 64 and 6, and 64 and 9 for 1969.
A woman born in 1970 or later: s 3, 65.

**Is there a gap?**
No, for this row.
The Law decides every woman born in 1956 or later (Part B to December 1969, s 3 after).
IL-27's module declines for a woman born before May 1947 because Part B has no row for her; this row never asks it about her, since s 1 (2) sends only those born in 1956 or later to the Law and gives the earlier ones Part A of Schedule A1.
So fork Q1 stops being a fork: its switch, its floor reading and the `the age in months the Retirement Age Law fixes` field are removed, and no status declines for want of a retirement age.

**One disagreement between the two texts, noted, not acted on.**
For a man born April to June 1939, Part A of Schedule A1 says 65 years (up to June 1939; NII line 4376) and the Law's Part A says 65 years and 4 months (April to August 1939; Law line 188).
s 1 (1) sends a man to Part A of Schedule A1, which this row uses.
The difference touches no one under 87.

**Tests re-pointed, values re-worked from the Hebrew** (not from the output): a woman born 20 June 1990 (780 months, reached 20 June 2055); born 10 January 1956 (744, reached 10 January 2018); born 10 May 1964 (762, reached 10 November 2027); born 15 January 1966 (768, reached 15 January 2030); the bands of Part B and the open band (15 assertions on the wrapper); a man born after April 1942 (804, equal to the Law's s 3: 67 years).
Removed: the assertions that Batya's statuses were declined by default, that a supplied age was used, and the floor-reading assertions; the s 335 assertion that her branches decline.
The Income Support Law test for a woman born in 1990 now answers 2000 (it declined by default in 0.1.0).
Counts: 598 assertions in 0.1.0, 611 in 0.1.1.
