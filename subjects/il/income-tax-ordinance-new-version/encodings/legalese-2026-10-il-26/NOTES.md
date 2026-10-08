# NOTES: ITO s 164 and the Deduction from Salary and Wages Regulations 5753-1993 (withholding), row IL-26

Version 0.1.0, 2026-10-08, encoder `enc-il-26`, status `draft`.
No domain expert has read this against the source.
An independent test pass has not yet been run.
Every expected value in `ito-il26-tests.l4` was worked by hand from the text before it was run.

## 0. Toolchain

`l4` is `~/.local/bin/l4`, the cabal store build `jl4-0.1-6df1397b`, sha256 `f0759b2ef2f1d1b2a577c68f059c54f487de9d913553fc9f0d9bf0f7f5dab0d8`, the same before and after the final `check.sh` run (2026-10-08T22:49:59Z).
`JL4_LIBRARY_PATH` is unset.
The four IL-03 modules are vendored beside this row's own (`VENDORED.txt`, with sha256); none is edited.

## 1. What is encoded, and what it says

Section 164 of the Ordinance makes the payer of listed kinds of income, employment income first, deduct tax at the time of payment "in the manner and at the rates prescribed" (line 5323).
For a salary the manner and rates are the Regulations (the editorial note at line 5338 says so).
Regulation 3(a) has the employer deduct, from each monthly salary, the tax Schedule A gives.
Schedule A is five steps and a table: (1) multiply the month's salary by 12; (2) compute the tax on that under ss 121 and 121B with the adjustments of s 120B; (3) take the employee's credit points into account against that tax; (4) divide by 12; (5) round, a fraction of a shekel over 49 agorot counting as a shekel and any smaller fraction as nothing; (6) the Director publishes a table, and the employer deducts by it.
Regulation 3(b) splits the tax in proportion when a month's salary is paid in parts.
Regulation 5 sends a partial salary, a pension, a salary for an additional position that the employee declared, and any salary where the employee gave no card or left the other-income section empty, to the maximal rate (the top rate of s 121, 47%), unless the employee has declared on form 0130 that the partial salary or pension is their only taxable income, in which case Schedule A applies.
Regulation 4(a) taxes a non-regular salary (a bonus) at twelve times the extra monthly tax that a twelfth of it would bring.
Regulations 9 and 10 let the assessing officer reduce, avoid or change the deduction on the employee's request; regulation 9(a) lists the grounds.

How it is encoded: `ito-il26-schedule-a.l4` is items (1) to (5) as one calculation, with IL-03's `the tax under section 121 for` and `the additional tax under section 121B for` doing step (2).
`ito-il26-regulations.l4` is regulations 1 to 5 and 10 and item (6).
`ito-il26-s164.l4` and `ito-il26-claims.l4` are s 164 and regulations 2 and 9.
`ito-il26-published-figures.l4` carries the Tax Authority's credit point (2,904 a year) and s 121B(a) amount (721,560), marked not law, through s 120B(e)(1) to 2026 and 2027.

What the answer is called.
`Schedule A - the tax on a month's salary of ...` is "the tax items (1) to (5) give", not "the tax the employer must deduct".
Item (6) says the employer deducts by the Director's table, which is not in the deposited sources, so `the employer deducts, given the Director's table` takes the table's figure as an input and refuses by name without it.
Whether the Authority's table equals the computation at every salary is not knowable from the sources.

## 2. Coverage table

Every provision in scope has a disposition; none is deferred.

| provision | disposition | where, or why not |
| --- | --- | --- |
| ITO s 164, the duty and the kinds of payment | encoded | `ito-il26-s164.l4`: ten kinds; the duty; the State as payer |
| ITO s 164, "the manner and rates" for employment income | encoded as a pointer | the Regulations; the instrument is named by `the instrument prescribing the manner and rates of deduction from` |
| ITO s 164, the manner and rates for the other nine kinds | refused: needs a source | the orders and regulations listed in the notes at lines 5324-5347 are not deposited |
| ITO s 164, the Minister may set a different time or base of deduction for gambling and prizes | inert | no rule here reads it; the Minister's order is not deposited |
| Reg 1 definitions: employee, day employee, salary, month's salary, partial salary, additional position, maximal rate | encoded | `ito-il26-regulations.l4`; the facts are the payment's days and hours |
| Reg 1, the other definitions (foreign worker, non-regular salary, shift work, sabbatical, registered spouse, child, and the rest) | inert, or an input | foreign worker is a flag; non-regular salary is regulation 4(a)'s input; shift work, sabbatical and the rest belong to regulation 6; registered spouse and child belong to the credit points (rows IL-01, IL-08) |
| Reg 2(a), (c) the card | encoded for who must give it | `the employer must demand an employee's card for`; the card's contents are `The employee's declarations` |
| Reg 2(a)(1)-(2), (b), (d) the deadlines and the duty to declare a second position | inert | they set when the employee must act, not the amount; no date input exists |
| Reg 2(e) computerised employers | inert | the Director's alternative procedure, not a figure |
| Reg 3(a) monthly salary | encoded | `regulations 3 and 5 treat` sends it to Schedule A |
| Reg 3(b) a month's salary paid in parts | encoded | `the share of ... on a part`; fork F3 |
| Reg 3(c), Schedule B (day employees) | refused by name | `wages of a day employee ...`; out of scope: wages of a day worker, not a monthly salary |
| Reg 3(d), Schedule C (foreign workers) | refused by name | `a salary to a foreign worker ...`; out of scope for the same reason |
| Reg 4(a) non-regular salary | encoded | `regulation 4(a) - the tax on`, with the 25% floor for a bankrupt's or liquidated company's employees |
| Reg 4(b) non-regular salary of a day employee | out of scope | a day employee's (Schedule B) |
| Reg 4(c) the officer may change the rate | encoded as an input | `A direction of the assessing officer` |
| Reg 5(a) maximal rate | encoded | for a partial salary, an additional position, no card, no other-income section |
| Reg 5(b) pension | encoded | maximal rate, or Schedule A on the 5(c) declaration |
| Reg 5(c)-(d) the form 0130 declaration and its withdrawal | encoded | `the sole-income declaration is in force` |
| Reg 5(e)(1) the officer reduces the rate; 5(e)(2) the Director may let employers adjust without the officer | encoded as an input | `A direction of the assessing officer`; the Director's general permission is an instruction, not a figure |
| Reg 5(f) the employer's notice of the partial salary | inert | a duty to notify, not an amount |
| Reg 6 special cases (survivors, no monthly salary, non-residents, provident fund leave pay, shift work, sabbatical, a disabled person's companion, a lump sum to day workers, annuity capitalisation, the s 121B surtax) | out of scope | kinds of payment other than a resident employee's monthly salary; each has its own flat rate or rule and none is needed to answer a monthly salary |
| Reg 7 retirement grants | out of scope | a grant is not a monthly salary; it is taxed "as if a non-regular salary" by reference to regulation 4, which is encoded, but the pairing needs the grant's exempt part under s 9(7A), not deposited |
| Reg 8 payments in kind | out of scope | a market-value rule for benefits in kind, not for a monthly cash salary |
| Reg 9(a) grounds of a request | encoded | 18 grounds (paragraph 2 is repealed), `the paragraph of regulation 9(a) for`; the officer's direction is the input |
| Reg 9(b) | inert | repealed |
| Reg 9(c) pension partly exempt | encoded | `the part of a pension of ... from which tax is deducted` |
| Reg 10 coordination | encoded as an input | the officer may reduce or increase; the employer must comply; same input |
| Regs 11-13 reporting, records, certificates | out of scope | duties after the deduction; no amount of tax |
| Reg 14 forms; reg 15 commencement | inert | forms; the Regulations apply from the January 1993 salary |
| Schedule A items (1)-(5) | encoded | `ito-il26-schedule-a.l4` |
| Schedule A item (6) the Director's table | refused by name without an input | table not deposited |
| Schedules B and C | refused by name | as regulations 3(c), 3(d) |
| a cumulative method | refused by name | the Regulations print none |

## 3. Fork register

All forks were ruled by Meng on 2026-10-08 (SHRUG): one named switch, the default a refusal by name where the readings give different answers, every other reading kept and tested.
Where only one reading is arguable on the words, the fork is classed (b), not a switch, and says so.
The switch values are fields of `The readings of the withholding rules`; `the readings of the withholding rules, by default` has them all declined.

| # | where | the question | readings | taken |
| --- | --- | --- | --- | --- |
| F1 | Schedule A items (2)-(3) | Are the credit points set off against the s 121B additional tax? | (i) against the whole of the tax under ss 121 and 121B (the words of items (2)-(3): "the tax so computed"); (ii) against the s 121 tax only, never below nil, with the additional tax added after (s 33A sets a credit point off against the tax for the year; the capstone's K3) | switch, default declined where they part; they part only when the credits exceed the s 121 tax and the income is above the s 121B amount (tested: 70,000 a month with 100 points gives 0 or 296) |
| F2 | Schedule A item (5) | Is the salary rounded before item (1) multiplies it, or only the tax? | (i) the salary is rounded first; (ii) the salary is multiplied as it stands | switch, default declined where they part; they part only for a salary with agorot (1,234.90 gives 124 or 123); they agree for 1,234.40 and 1,234.95 |
| F3 | reg 3(b) | Is the share of the tax on a part rounded? | (i) rounded as item (5) rounds a tax; (ii) exact | switch, default declined where they part (12,000 of 20,000 gives 1,609 or 1,609.2); agree where the share is whole (10,000 of 20,000: 1,341) |
| F4 | Schedule A item (2) | A salary paid in one tax year for another (December pay in January): whose year's amounts? | (i) the year of the payment; (ii) the year of the work | switch, default declined where they part; they agree in 2026 and 2027 (the amounts are frozen by s 120B(e)(1)) and part when one of the two is a year the sources do not answer (2026 for 2025: 575 or a refusal). Regulation 12(b) treats a payment made 1-13 January for an earlier year as paid in that year, but only for the report. |
| F5 | reg 4(a) | How is the "difference of tax" read? | (i) tax(S plus B/12) less tax(S), each the rounded Schedule A figure, times 12; (ii) the same with unrounded tax | (b), no switch: "the tax to be deducted from the month's salary" is the figure item (5) gives, and the "plus a twelfth" attaches to the salary, not the tax. The readings differ by at most 6 shekels in 12 x the rounding. Flagged for the independent tester. |
| F6 | reg 5(a) | Is the maximal rate 47%, or 47% with the s 121B surtax? | (i) 47%, "the highest rate fixed in section 121"; (ii) 50% (47% plus 3%) | (b), no switch: the definition names s 121 alone, and reg 6(k) adds s 121B to deductions under reg 6 only. |
| F7 | reg 5(a), no rounding | Is a deduction at the maximal rate rounded under item (5)? | (i) not rounded; (ii) rounded | (b), no switch: item (5) is a step of Schedule A; reg 5(a) applies a rate, not the Schedule. Assumption A2. |
| F8 | reg 1 "משכורת חלקית" and "עובד יומי" | A person who is both | the definitions overlap (a person on 4 hours a day for 15 days) | (b): reg 5 (partial salary, maximal rate) is tested before regulation 3(c); the exception in reg 3(a) points to reg 5. |
| F9 | reg 5(c) with an additional position | Does a form 0130 declaration lift the maximal rate on a salary for a declared additional position? | (i) no (5(c) names only the partial salary, pension, wages); (ii) yes | (b): reg 5(c)'s "sole income" is a partial salary, pension or wages. A declared additional position goes to the maximal rate, and the test order puts partial salary first. |

## 4. Assumptions (made, not read)

- A1. A credit point is set off against tax and never below nil: the tax to deduct is never negative.
  The Regulations say "taken into account" and do not say it floors at nil; s 33A sets a credit point off against tax.
  No one reads the schedule as a payment to the employee.
- A2. A deduction at the maximal rate, and a deduction an officer fixes, is not rounded (F7).
- A3. The credit points are a number the employee claims on the card (item (3): "in accordance with his declaration on the employee's card").
  Which points an employee is entitled to is ss 34 to 40D and 66(c), rows IL-01, IL-02, IL-08.
- A4. The form of an assessing officer's direction is assumed (nothing, a rate, an amount).
  The Regulations say the officer may "direct the employer to reduce the deduction" and do not say in what form.
  A direction takes precedence over every other rule, a foreign worker's and a day employee's included, because the employer "shall comply" (reg 10).
- A5. The payment, not the month, has a single tax year in the readings of F4; `tax year` is the year of payment.
- A6. Hours worked in a day and a week and days worked in the month are inputs; the definitions in regulation 1 are applied to them.
  The 18-day test is "at least 18" (reg 1: "less than 18 days" is not a month's work).
- A7. Schedule A treats the whole salary as income from personal exertion charged at the s 121 rates and the employee as having no other income: that is what the Schedule computes.
- A8. The credit point of tax year 2027 is 2,904 and the s 121B(a) amount 721,560, by s 120B(e)(1) from the Authority's 2025 credit point and 2026 s 121B amount.
  Those two published figures were carried from rows IL-01 and IL-03; this row did not re-read the PDFs (no fetching was allowed).

## 5. Findings

- W1. My first expectation for the year-of-work reading of F4 named the wrong refusal.
  I expected the figures module's "no annual figures published ... for this tax year" for a salary for 2025; the refusal is section 121's ("section 121 as it stood before tax year 2026 is not in the deposited text"), because Schedule A reaches s 121 before s 121B reads the amount.
  The outcome I expected (a refusal) was right; only its name was not.
  I edited the expected message and left a dated comment in the test file.
- W2. The Regulations and Schedule A call the credit points "taken into account" and the Ordinance (s 33A) calls them a set-off against tax; neither says whether the additional tax of s 121B is reduced.
  Fork F1.
- W3. The text of regulation 4(a) is garbled ("the difference between the tax to be deducted from the month's salary for the month in which the non-regular salary was paid, and the tax to be deducted from the month's salary for that month, plus a twelfth of the non-regular salary").
  Read as tax(S plus B/12) less tax(S), the bonus falls in the marginal band: a 24,000 bonus on a 20,000 salary is taxed at 31% (7,440).
  F5.

## 6. How this differs from the annual tax that row IL-03 computes

IL-03 computes the tax on the year's actual taxable income.
Schedule A computes, month by month, the tax on twelve times that month's salary, as if the month were the whole year, less the credit points the employee declared.
Where the salary is the same every month and the declarations do not change, the two agree up to item (5)'s rounding: 20,000 a month with 2.25 points is 2,681.50 a month from the annual figure and 2,682 withheld, so twelve withholdings are 32,184 against an annual 32,178 (asserted: 12 x 2,682 less (38,712 less 6,534) is 6).
Where the salary varies, or there is other income, or the employee started mid-year, the withholding is not the annual tax; the annual assessment settles the difference.
Schedule A cannot know the year's income; regulations 5 (the maximal rate for a second job) and 10 (the officer's adjustment) are the Regulations' own tools for the gap.
Regulation 4(a) taxes a bonus at the marginal rate of the month it falls in, so a large bonus is withheld at a higher rate than the year's average.

## 7. Answer table (tax year 2026, an employee born in 1990 with 2.25 credit points = 6,534 a year, readings by default)

| monthly salary | annual | tax on the annual (ss 121, 121B) | less credits | / 12 | withheld |
| --- | --- | --- | --- | --- | --- |
| 4,000 | 48,000 | 4,800 | nil (credits exceed tax) | 0 | 0 |
| 5,445 | 65,340 | 6,534 | 0 | 0 | 0 |
| 5,449 | 65,388 | 6,538.80 | 4.80 | 0.40 | 0 |
| 5,450 | 65,400 | 6,540 | 6 | 0.50 | 1 |
| 10,000 | 120,000 | 13,435.20 | 6,901.20 | 575.10 | 575 |
| 20,000 | 240,000 | 38,712 | 32,178 | 2,681.50 | 2,682 |
| 50,000 | 600,000 | 167,030.40 | 160,496.40 | 13,374.70 | 13,375 |
| 60,130 | 721,560 | 224,163.60 | 217,629.60 | 18,135.80 | 18,136 |
| 61,000 | 732,000 | 229,070.40 plus 313.20 | 222,849.60 | 18,570.80 | 18,571 |
| 70,000 | 840,000 | 279,830.40 plus 3,553.20 | 276,849.60 | 23,070.80 | 23,071 |

Every cell is cited to Schedule A items (1)-(5) and ss 121, 121B; the arithmetic is in the comment beside each assertion.
The same salaries in 2027 give the same (s 120B(e)(1) freezes the amounts for 2025-2027, and IL-03 prints s 121 for 2026-2027).
Other routes: a partial salary of 3,000 with no declaration is 1,410 (47%); a pension of 8,000 on the form 0130 declaration is 295; a 20,000 salary with no card is 9,400.
A 24,000 non-regular salary on a 20,000 salary is 7,440; with a 5,000 salary and a 12,000 bonus, 672, or 3,000 where the 25% floor for a bankrupt's employees binds.

## 8. What check.sh prints

```
module                                    errors satisfied  failed  refused  expected
ito-120b-indexation.l4                         0         0       0        0         0
ito-121-individual-rates.l4                    0         0       0        0         0
ito-121b-additional-tax.l4                     0         0       0        0         0
ito-il03-nouns.l4                              0         0       0        0         0
ito-il26-claims.l4                             0         0       0        0         0
ito-il26-nouns.l4                              0         0       0        0         0
ito-il26-published-figures.l4                  0         0       0        0         0
ito-il26-regulations.l4                        0         0       0        0         0
ito-il26-s164.l4                               0         0       0        0         0
ito-il26-schedule-a.l4                         0         0       0        0         0
ito-il26-tests.l4                              0       115       0        0         0
TOTAL (11 modules)                             0       115       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
exit=0
```

The l4 sha256 was `f0759b2e...dab0d8` before and after.
No assertion is expected to fail or to be refused: the 18 refusals the tests exercise are `#ASSERT REFUSED` assertions, counted as satisfied.
Mutation check: changing two expected values (575 to 576, 18,571 to 18,545) in a scratch copy produced two failed assertions, so the harness can fail.

## 9. What the capstone would need (for IL-55)

The capstone (row IL-07) answers "one twelfth of the income tax for the tax year" (its K1 reading (i)) and declines the Regulations as not in its sources.
To answer "the tax withheld from the salary" it would add an adapter taking:
- the earner's `The employee's declarations` (the card: given, the other-income section filled, a declared additional position, form 0130 and its withdrawal, the credit points claimed, the date of birth); the credit points are the sum its IL-01 and IL-08 adapters already compute;
- a `A payment of salary` (the year of payment and of the work, the month's salary, the part paid, days and hours, pension, foreign worker, works elsewhere);
- `The annual figures for the tax year` (the s 121B(a) amount and the credit point value), which `the annual figures published for tax year` supplies for 2026 and 2027;
- the readings (the capstone's default is `the readings of the withholding rules, by default`) and the assessing officer's direction (`no direction`).
The tax year has to be 2026 or 2027, the years IL-03 answers.
The answer differs from K1 (i) by the rounding of item (5) and, for a partial salary, a pension or a second job, by the maximal rate.

## 10. Open questions for a domain expert

- Does the Tax Authority's published table (the monthly booklet) equal Schedule A items (1)-(5) at every salary, or does it differ (it is built for whole shekels of salary, and the Director may "publish" a table that departs from the arithmetic)?
  Item (6) makes the table, not the arithmetic, what the employer deducts.
- Is a credit point set off against the s 121B additional tax in withholding? (F1)
- Is a salary paid in January for December deducted by the amounts of the year of payment? (F4)
- Is a bonus (reg 4(a)) computed on the rounded Schedule A figures or the exact ones? (F5)
- The cumulative method of withholding, which the Authority may prescribe by practice, is not in the Regulations as deposited; where is it?
- Do regulation 4(a)'s "difference of tax" and regulation 7(a)'s grant-as-bonus pair need the s 9(7A) exemption for a grant, which is not deposited?

## 11. Needs a source

- The Director's table (Schedule A item (6)), the Tax Authority's monthly booklet: not deposited (recorded by pointer in `../../registers/source-bundle/amending-laws/SOURCES.json`).
- The orders and regulations made under s 164 for every kind of payment other than employment income (the notes at ITO lines 5324-5347 name them): not deposited.
- Any cumulative method: none in the Regulations.
- The Employers' Tax Law 5735-1975 and the Income Tax (Rules for Rounding Amounts) Order 5746-1986 are named by the Regulations' preamble and s 120B(d); the Order is deposited under `regulations/` but IL-03 does not encode it, so the credit point and s 121B amount stay published inputs.
