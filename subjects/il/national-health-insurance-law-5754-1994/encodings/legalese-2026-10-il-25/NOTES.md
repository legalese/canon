# NOTES: il/national-health-insurance-law-5754-1994, encoding row `legalese-2026-10-il-25`

Version 0.1.0, 2026-10-09, run IL-25-20261008, agent enc-il-25.
Status: draft.
No domain expert has read this against the Hebrew (gate HG1 not sought).

## 1. What is encoded, and what the Law says

The Law makes every resident insured and makes the insured pay a health insurance contribution to the National Insurance Institute, which collects it as it collects National Insurance contributions (s 15(a), (b)).
Section 14 says who pays and how much:

- **An employee** (s 14(b)(1)): the employer, for every insured employee for whom it is liable for National Insurance contributions, pays 5.17% of the employee's income, and deducts it from his wage.
- **An employee who pays National Insurance for himself** (s 14(b)(2)), **a self-employed person** (s 14(c)(1)): pays 5.17% of his income himself.
- **One who is neither** (s 14(c)(2)): 5.17% of his income, and not less than the minimum amount (123 NIS a month in 2026).
- **The reduced rate** (s 14(f1), for contributions for January 2025 on): for an employer, an employee liable for himself and a self-employed person, 3.23% on the part of the income up to "the reduced amount determined under section 341 of the National Insurance Law", and 5.17% on the rest.
- **A National Insurance benefit** (s 14(d)): the recipient of injury, accident, maternity, unemployment, wages-owed or reserve-duty benefits pays on the benefit "at the rates at which an employer is liable for his employee".
- **An old-age pensioner** (s 14(e)): a fixed amount (123, or 237, or 340 NIS in 2026) in place of (b) to (d) and (f1).
- **Early pension, retirement grant, adjustment allowance** (s 14(e1)): the employee's rates.
- **Anyone else** for whom nothing is payable under the above (s 14(f)): the minimum amount.
- **Exempt** (s 14(g), (g1)): under 18, a housewife, a student or recruit and others exempt from National Insurance by its s 351, a living organ donor for a period the Minister sets.
- **Temporary** (s 14(g2), 1.1.2026 to 31.12.2035): income exempt under s 350A(a) of the National Insurance Law (a new immigrant's income on which he pays social insurance abroad) is added to the income for (b) and (c).

The encoding answers one question: `the health insurance contribution for` a person's month `with` the figures for the year `under` the readings.
It also answers who is liable to pay (`who is liable to pay the contribution of the kind`), and the contribution on a benefit (`the contribution on a benefit, for`).
Months from January 2026 only; earlier months are declined by name (section 4, T3).
Amounts are before rounding (assumption A3).

Modules: `nhi-il25-nouns.l4` (DECLARE only), `nhi-s14-income.l4` (s 2, s 14(b), (c), (f1), (g2)), `nhi-s14-fixed-and-benefits.l4` ((d), (e), (e1), (g), (g1)), `nhi-s14-month.l4` (s 14 as a whole), `nhi-il25-published-figures.l4` (the 2026 figures, marked not law), `nhi-il25-tests.l4`.
No module imports another row's module, so nothing is vendored.

## 2. Coverage table

| provision | source lines | disposition | where / reason |
| --- | --- | --- | --- |
| s 2 "income" | 52 | encoded | the income is a field of the person's month (`income`); its ceiling and floor are forks F1, F2 |
| s 2 "National Insurance contributions", "the Institute", "employee", "employer", "self-employed" | 50, 53 | inert | definitions by reference to the National Insurance Law; the kind of person is an input (`A kind of insured person under section 14`) |
| s 14(a) "minimum amount" | 291 | encoded as an input | the 2026 figure 123 is the consolidation's note, in the published-figures module; the Law prints 47 NIS "as of 1995" and an updating rule (fork T5) |
| s 14(a) "old-age pension", "special old-age benefit", "housewife", "special adjustment allowance" etc. | 292-295 | inputs | defined by the National Insurance Law and the Disengagement Plan Implementation Law; whether the person is paid one is a fact the caller states |
| s 14(b)(1) | 296 | encoded | `the contribution under section 14(b) or (c) for`; payer: `who is liable to pay the contribution of the kind` |
| s 14(b)(2) | 297 | encoded | same |
| s 14(c)(1) | 298 | encoded | same |
| s 14(c)(2) | 299 | encoded | same, with the floor at the minimum amount |
| s 14(d)(1), (2), (3) | 300-307 | encoded | `the contribution on a benefit, for`; forks F3, F6; (d)(3) says an employer-paid benefit is (b)(1) income, so it is not this function's |
| s 14(d)(4) | 308 | out of scope | the State pays for those paid special adjustment allowances under the Disengagement Plan Implementation Law, which is not deposited; also the (f1) interplay is not stated |
| s 14(e)(1) | 309 | encoded | the minimum amount |
| s 14(e)(2), (3) | 310-311 | encoded | 237 or 340 NIS in 2026; the class (3) adds is the caller's input |
| s 14(e)(4) | 312 | encoded | fork F4 (the employer's duty under (b)(1)) |
| s 14(e1) | 313 | encoded | fork F3 |
| s 14(f) | 314 | encoded | the minimum amount; fork F5 for a computed nothing |
| s 14(f1) | 315-316 | encoded | 3.23% up to the reduced amount; the three payers it names (T2); the reduced amount is the National Insurance Law's reduced collection threshold (T1) |
| s 14(g) | 317 | encoded | `section 14(g) or (g1) exempts the person`; the conclusions of National Insurance Law ss 238 and 351 are inputs |
| s 14(g1) | 318 | encoded | the Minister's period is an input (`a living organ donor in a month the Minister of Health has set for the donor`); no order is deposited |
| s 14(g2) | 319 | encoded | years 2026 to 2035; for kinds (b) and (c) only |
| s 14(h) | 320-322 | out of scope | power to set other rates and amounts by regulation, with the approval of the Finance Committee; none deposited |
| s 14(i) | 323-331 | out of scope | power to set rules, exemptions and reduced rates by regulation; the four regulations the Law notes (Exemption 5755-1995, Special Provisions 5755-1995, Reduced Rates 5755-1995, Household Worker 5755-1995) are not deposited: needs a source |
| s 14(j)(1), (2) | 332-336 | out of scope | the Institute's power to deduct health contributions from any benefit it pays, and a payer's duty to transfer: collection, not liability or amount |
| s 15(a), (b) | 338-339 | inert, and the reason for F1, F2 | applies the National Insurance Law, with the necessary changes, "as if they were National Insurance contributions": the only text that could carry that Law's maximum and minimum income over, and it does not say so |
| s 15(c), 15A, 16, 17, 18, 19, 20, 20A | 340-421 | out of scope | the Institute's expenses, the report to the Knesset, the transfer and allocation of the money, and its use: financing, not the contribution |
| s 1 | 43-47 | out of scope | the state health insurance principle: a purpose clause |
| ss 3 to 13 | 79-288 | out of scope | the right to services, membership of a sick fund, the basket of services (the Second Schedule), changes in services and payments, the cost of the basket, the sources of funding (s 13(b)(1): a sick fund may not collect health contributions) |
| ss 21 to 46B | 424-807 | out of scope | the sick funds, their rules, supervision, information, complaints: regulation of services |
| s 47 (offences) | 810-834 | out of scope | the employer who does not pay under s 14(b)(1) and the insured who does not pay under s 14(b)(2) to (f) commit an offence (lines 815, 828); penal, not the amount |
| ss 48 to 54 | 837-909 | out of scope | the Health Council; s 52(a) (line 884) has it advise on "the rates of health insurance contributions", which is advice and not a rule; s 54(b) (line 907) gives the Labour Court exclusive jurisdiction over disputes between the Institute and one liable to pay: procedure |
| s 55(d), (e) | 910-917 | out of scope | rates for a soldier (the rate for one in regular service under a commitment to permanent service is the s 14(b)(1) rate): the arrangements are the Minister's regulations, not deposited |
| s 56 | 918-931 | out of scope | special arrangements for registration and services; no contribution |
| s 57 | 932-938 | out of scope | special rates and exemptions by regulation (one living in an institution): not deposited |
| s 58 | 939-972 | out of scope | the waiting period for a returning resident and its "special payment" (the contribution on the average wage, times thirty, lines 950, 962, 970): residence, and the average wage is another Law's |
| ss 59 to 66, 67 to 69A | 973-1035 | out of scope | insured from abroad, execution, savings, transitional provisions for sick funds and the State's funding; no line states a contribution |
| the Schedules | 1036-3434 | out of scope | the basket of services and its details |

Needs a source (refused by name or taken as an input, never guessed): the four regulations under s 14(i); the Minister's orders under s 14(g1) and s 55; the Disengagement Plan Implementation Law (s 14(d)(4), (a)); the Amendments 69 and 72 (the text of s 14 before 2025); National Insurance Law ss 238, 351 (inputs).

## 3. Fork register

Every row below is "ruled by Meng 2026-10-08 (SHRUG)": one named switch, default `decline where the readings differ`, the other readings kept by name and tested.
A switch declines only where its readings give different contributions; where they agree it answers.

| id | the question | readings (switch values) | where the readings differ | tested |
| --- | --- | --- | --- | --- |
| F1 | Does the maximum income of National Insurance Law Schedule K item 1 (5 times the basic amount: 51,910 NIS a month in 2026) cap the income the health contribution is taken on? | (i) it caps; (ii) nothing caps | income above 51,910; at or below it they agree and the default answers | `nhi-il25-tests.l4`, "The ceiling" |
| F2 | Does that Law's s 348(b) raise an income below Schedule K's minimum income to it, for the health contribution? | (i) the income is what is paid; (ii) it is raised to the minimum | an income below the minimum income the caller supplies; if the caller supplies none (NOTHING) the income stands | "The minimum income" |
| F3 | Do the reduced rate of (f1) and the rates "at which an employer is liable" reach a benefit under (d) and an early pension under (e1), whose recipient is none of the three payers (f1) names? | (i) 3.23% up to the reduced amount, 5.17% above; (ii) 5.17% throughout | any positive amount | "(e1)", "(d)" |
| F4 | For an old-age pensioner who is an employee for whom the employer is liable and has an income: (e)(4) frees "the insured" of (b) to (d), but (b)(1) is the employer's duty. Does it stand? | (i) only the fixed amount; (ii) the fixed amount and the employer's (b)(1) amount | income above nothing; for every other kind of pensioner the (b) to (d) liability is the person's own, (e)(4) frees it, and the fixed amount alone is payable | "Fork F4" |
| F5 | Is an insured person whose computed amount under (b), (c) or (e1) is nothing "one for whom no contribution is payable" within (f), who pays the minimum amount? | (i) a computed nothing is an amount payable: 0; (ii) it is not: the minimum amount | an income of nothing | "Fork F5" |
| F6 | Where one person has an income and a benefit in the month, is the reduced amount used once across the two or once for each? | (i) once across; (ii) once for each | a month with an income and a benefit, where the income is not so large that all the benefit is above the reduced amount in both readings | "(d)" |

Readings the text decides, so not switches (each is an assumption a reader can contest, and each is tested at both ends):

- **T1. The "reduced amount determined under section 341" of (f1) is the reduced collection threshold of that Law's s 334(a).**
  The text of s 341 as deposited (line 3655, last clause) turns a "half of the average wage" in any order made before 2006 into the reduced collection threshold, and the deposited order, the Reduced Rates Order 5759-1999 s 1, is such an order ("half the average wage").
  The Order's own editorial note says 60% of the average wage, which is the older text of s 341 (row IL-04, fork F3: the 2025 budget-year Law s 19(6) replaced it from 1 January 2026).
  For 2026 the Institute's rates pages print 3.23% up to 7,703, which is the s 334(a) threshold.
  The figure is an argument (`the reduced amount`), not a constant of the rules.
- **T2. (f1) reaches the three payers it names, not "one who is neither" under (c)(2).**
  Its operative words are "an employer liable for an employee, an employee liable for himself and a self-employed person liable under those subsections".
  The Institute's worked example for one who is neither prints 12.09% on the part up to 7,703 and 12.17% above: 6.92% and 7% of National Insurance plus 5.17% health on all of it.
  Text and page agree.
- **T3. Months from January 2026.**
  The deposited text prints 5.17% with an editorial note ("until 2024, 5%; January 2025, 5.16%") and states (f1) for contributions "for January 2025 on" with the earlier 3.1% a regulation (not deposited).
  The reduced amount is the National Insurance Law's s 341 as amended in 2025, which that Law has from 1 January 2026 (IL-04, F3).
  So earlier months are refused by name ("this row answers contribution months from January 2026 ...").
- **T4. The start of 5.17%.**
  Not needed for 2026; the editorial note implies February 2025, and the encoding does not use it.
- **T5. The updating of the minimum amount and the pension amounts.**
  (a) updates the minimum amount "at the dates and rates at which benefits are updated, by s 2 of the National Insurance Law"; (c)(2) says it is updated "at the dates when the minimum income in Schedule K item 4 is updated".
  The two may differ in the dates of a year.
  The encoding takes the amounts for the year as input; the 2026 figures (123, 237, 340) are the consolidation's own notes to lines 291 and 310 and are marked not law.

Assumptions (read, but not stated in the text):

- **A1. A month.** The self-employed and "neither" have annual income in the National Insurance Law with monthly advances (IL-04 F8).
  The contribution is computed on the income of the month, as an equal share; the rules do not take an annual figure.
- **A2. A benefit under (d) is not capped.** F1 is applied to income, not to a benefit; a benefit above 51,910 a month is not a case this row meets.
- **A3. No rounding.** The National Insurance rounding regulations are deposited, but whether they apply to the health contribution through s 15(b) is not read here (open question 4).
- **A4. The kind of person is an input.** Whether the employer is liable for National Insurance for the employee, whether one is a self-employed person, an "old-age pension", a "housewife", the exemptions of that Law's s 351, are conclusions of the National Insurance Law; the caller states them.
- **A5. The class of (e)(2).** (e)(3) extends (e)(2) to two classes; the caller places a person in (e)(2) or (e)(1).
  The 340 amount applies if either the pensioner is paid a spouse's supplement or his spouse is paid an old-age pension (the Hebrew "וכן", "and also", read as a union).
- **A6. (g2) and the ceiling.** The exempt income is added to the income before the F1 test, so with a ceiling the sum is capped.
  The text does not say; it matters only for a new immigrant with a very high income.

## 4. Agreement with row IL-04 and the capstone

**Schedule J (row IL-04) does not contain the health rates.**
Its column D is the employee's National Insurance deduction: 1.04% up to the threshold and 7% above in 2026.
The combined rates (National Insurance plus health) appear only in the Institute's pages, which IL-04's NOTES.md transcribes (section 7, and the evidence for its fork F21 at lines 248-262).
So the check is arithmetic against Schedule J and against those pages:

| case | Schedule J / the Institute | this row | agree |
| --- | --- | --- | --- |
| threshold | the same 7,703 (s 334(a) note; Institute pages) | `the reduced amount` 7,703 | yes |
| employee up to the threshold | NI 1.04% + health 3.23% = 4.27% | 3.23% | yes |
| employee above it | NI 7% + health 5.17% = 12.17% | 5.17% | yes |
| one who is neither, January 2026 example, 8,558 | the Institute: 931.29 + 104.05 = 1,035 in total, NI alone 592.8976 (IL-04) | health 442.4486; 592.8976 + 442.4486 = 1,035.3462 | yes |
| controlling shareholder, 67 to 70, women past retirement age (IL-04 F21) | the Institute's form 102 sets all carry health at 3.23% / 5.17% (IL-04 NOTES.md line 253-258) | the same rates | yes |
| the capstone's test figures (IL-07 tests): salary 20,000, salary 51,910 | health 884.5618 and 2,534.3088 | the same | yes |

Disagreements: none for the cases above.
Not checked against the Institute: the self-employed rates (IL-04 records only the National Insurance composites for that page, 4.47% / 12.83%, which exclude health); the maximum income above which the Institute stops (51,910 is IL-07's figure, which IL-07 records from the Institute's employees page, fetched 2026-10-06T23:39:00Z, sha256 `f5bd019cf26adb815f5e84108933c7e86885114a84db4766b546080a41227f03`, DECIDED-ANSWERS.md line 28).

## 5. Answer table, March 2026, default readings

All amounts NIS, before rounding; arithmetic in `nhi-il25-tests.l4`.

| person | income | contribution | provision |
| --- | --- | --- | --- |
| employee, employer liable | 5,000 | 161.5 | 14(b)(1), (f1) |
| same | 7,703 | 248.8069 | |
| same | 7,704 | 248.8586 | |
| same | 20,000 | 884.5618 | |
| same | 51,910 | 2,534.3088 | |
| same | 51,911 and above | refused (F1) | |
| employee liable for himself; self-employed | 20,000 | 884.5618 | 14(b)(2), (c)(1) |
| neither | 8,558 | 442.4486 | 14(c)(2) |
| neither | 0 to 2,379 | 123 | |
| neither | 2,380 | 123.046 | |
| nothing payable under (b) to (e1) | any | 123 | 14(f) |
| old-age pensioner, income supplement | | 123 | 14(e)(1) |
| old-age pensioner, no supplement | | 237 (340 with a spouse's supplement or a pensioner spouse) | 14(e)(2), (3) |
| under 18, housewife, exempt student, 351(7a)/(11)(2c), donor | | 0 | 14(g), (g1) |
| employee with 10,000 exempt income, 20,000 paid, 2026 to 2035 | | 1,401.5618 | 14(g2) |
| the same in 2036 | | 884.5618 | |
| early pension 10,000; maternity allowance 10,000 | | refused (F3) | 14(e1), (d) |
| employee paid nothing | | refused (F5) | |

## 6. What the capstone would need (for IL-55)

Today the capstone (IL-07) takes `the health insurance contribution the caller says is deducted for the month` as an input.
To call this row instead it must supply, for the earner's month, a `A person's month under section 14`: year, month, kind (`an employee for whom the employer is liable for National Insurance contributions`), income (the salary), exempt income under s 350A(a) (0), minimum income (NOTHING), old-age pension (`no old-age pension`), the spouse flag (FALSE), and the exemption facts (age, housewife, student or recruit, s 351(7a)/(11)(2c), donor), plus `the figures for 2026` and the readings (`the default readings` in the tests; built in `nhi-il25-tests.l4`, a `The readings section 14 is applied under` record with every switch at `decline where the readings differ`).
Inputs this row takes that the capstone does not supply today: the age and the exemption facts of the earner and (for the spouse's branch) the earner's kind; the pension status; whether the employer is liable for National Insurance (the capstone assumes it).
What changes in the capstone's answers: none for salaries up to 51,910 (the capstone's own tests supply the same health figure there).
**Above 51,910 the default readings decline** where the capstone caps; the ceiling is fork F1.
That is the one fork that touches an ordinary employee, and the Institute's practice and the capstone's assumption both cap.
A ruling that sets F1 to "caps" would make the capstone's present figure the row's answer.

## 7. What `check.sh` prints

Run on 2026-10-09 with `l4` jl4-0.1-6df1397b.
The l4 sha256 before the run was `f0759b2ef2f1d1b2a577c68f059c54f487de9d913553fc9f0d9bf0f7f5dab0d8` and after it `f0759b2ef2f1d1b2a577c68f059c54f487de9d913553fc9f0d9bf0f7f5dab0d8` (unchanged).

```
module                                    errors satisfied  failed  refused  expected
nhi-il25-nouns.l4                              0         0       0        0         0
nhi-il25-published-figures.l4                  0         0       0        0         0
nhi-il25-tests.l4                              0        78       0        0         0
nhi-s14-fixed-and-benefits.l4                  0         0       0        0         0
nhi-s14-income.l4                              0         0       0        0         0
nhi-s14-month.l4                               0         0       0        0         0
TOTAL (6 modules)                              0        78       0        0
(a failed assertion is also an error; any other error, or a refused assertion a module is not expected to have, makes the run red; "expected" is failed/refused where a module may refuse)
exit status 0
```

Every assertion is satisfied; none fails and none is refused as an assertion.
The `#ASSERT REFUSED ... BECAUSE` assertions (12 of the 78) assert that the declined case is declined, in the words of the fork it turns on; they count as satisfied.
The tests module reads the diagnostics line after each `Message:`, as `check.sh` does.
A mutation check (an expected value and a BECAUSE text changed in a scratch copy) made 7 assertions fail, so the assertions can fail.


## 8. What was not done

- **The independent test pass** is for a later session; the answers above were worked from the Hebrew before the run, not by a second reader.
- **HG1**, a human who knows Israeli social insurance reading the modules against the Hebrew.
- **The sources the table calls "needs a source"**, not fetched (the brief forbids it).
- **Semi-cleanroom:** nothing from the Axiom Foundation was read, searched or fetched.

## 9. Open questions

1. F1: does the National Insurance Law's maximum income apply to the health contribution?
   Text for: s 2 ("the income from which he is liable for National Insurance contributions", which is capped); s 15(b).
   Text against: s 348(a) names "insurance contributions payable under s 335", and s 335 does not list health.
2. F2: do employees' health contributions rise to Schedule K's minimum income?
   The Institute's practice is not recorded in the sources here.
3. F3 and F6: at what rates does a benefit recipient pay, and how do a benefit and a wage share the reduced amount?
   The Institute's own treatment (the employer-paid maternity allowance, for instance) would settle it.
4. Rounding: do the National Insurance rounding regulations (deposited under that Law) round a health contribution?
5. T5: which dates update the minimum amount, and are 123, 237 and 340 the figures the Institute collects in 2026?
6. T1: is the Institute's reduced amount for the health rate the same figure as the National Insurance threshold in every year, or can the orders under s 341 diverge?
7. F4: what does the Institute collect from an employed old-age pensioner?
