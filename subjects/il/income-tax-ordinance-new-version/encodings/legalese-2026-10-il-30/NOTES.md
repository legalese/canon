# Notes: Income Tax Ordinance special rates and other regimes, and the Rounding Order 5746-1986 (row IL-30)

Run `IL-30-20261008`, encoder `enc-il-30`, one session, 2026-10-08 to 2026-10-09, version 0.1.1 (the repair after the independent pass; section 11 says what changed), status `draft`.
This file is what a reviewer reads first.
It was written after the modules and their tests were green, and every number in it is copied from the `check.sh` output in section 6 or from a test named here.
Claims about the sources cite the source line in the deposited file; a line number with no file name is a line of the Ordinance file, and the Order and RE Tax Law files are named where they are meant.

## 1. What is encoded and what is not

Encoded, in L4, from the Hebrew text:

- The Rounding Order 5746-1986, ss 1 to 13 and 15 and 17, with s 120B(d) as the join (`ito-rounding-order-5746.l4`, `ito-120b-d-rounding-power.l4`): the multiple and the direction for each of the thirteen kinds of amount, the rule that rounding does not change the base of the next adjustment, and the Order's commencement.
- Ordinance s 88: the definitions of Part 5 that the rate sections use (`ito-88-definitions.l4`): who is a relative, who is a material shareholder (alone or together with another), what is an asset, the six ways an asset comes to the taxpayer and the purchase day, consideration, capital gain and loss, the adjusted remaining original price, the inflationary amount, the real capital gain, the chargeable inflationary amount, and the three parts of the real gain around the fixed date (1 January 2003) and the change date (1 January 2012).
- Ordinance ss 125B (dividends), 125C (interest), 122 (rent of a residential apartment), 91 (capital gains: (a), (b)(1) to (3), (b1), (c), (e), (f), (g), and (b2) for a body of persons), 8(c) (spreading), 64A1 (the transparent company), 64A2 (three of the fund definitions), 57, 55(b) and 60A(b)(2) (the kibbutz).
- The RE Tax Law: s 6(b), s 48A (the betterment tax) and s 9 (the purchase tax on a residential apartment, as printed for 2025) (`retl-48a-betterment-tax.l4`, `retl-9-purchase-tax.l4`).
- One shared module of arithmetic, the "highest layer" sentence that ss 91 and 125C and the RE Tax Law use (`ito-top-layer.l4`).

Not encoded (the reason for each is in the coverage table): the report and advance procedure of s 91(d); the Minister's powers; the rest of s 60A; s 64A1(b)(3)(b), (6), (7), (10) and (d)(2); the RE Tax Law's s 48A(e), 48A1, 48B and 48C, its purchase-tax windows before 16 January 2025 and its s 9(a) and (b); 125D and 125E, 122A and 126 (not named by the row).

Ss 91, 125B, 125C and the RE Tax Law's s 48A are answered for dates on or after the text's own change date (1 January 2012), and the purchase tax from 16 January 2025; an earlier date is declined by name (assumption A6).
Every figure that is only published is an input with no default.

## 2. Coverage table

Dispositions: `encoded`; `input` (the rule takes the fact or figure as an input, with the citation); `inert` (quoted, not operative as a rule here); `out-of-scope` (with a reason); `not finished` (could be encoded, was not finished in this session).
No row is left `deferred`.

### 2.1 The Rounding Order 5746-1986 (Order file lines) and s 120B(d) (Ordinance lines 4341-4342)

| provision | what it is | disposition | where, or why not |
| --- | --- | --- | --- |
| Order intro (line 11) | the power: s 120B(d)(3) | inert | quoted in `ito-rounding-order-5746.l4` |
| Order s 1 (14-16) | income ceilings, step 120 | encoded | `Order s 1 — round an income ceiling` |
| Order s 2 (18-20) | credit points, step 12 | encoded | `Order s 2 — round the amount of credit points` |
| Order s 3 (22-24) | allowance points, nearest whole shekel | encoded | `Order s 3 — round the amount of allowance points` |
| Order s 4 (26-28) | the exemption of s 9(5)(a), step 1,200 | encoded | `Order s 4 — …` |
| Order s 5 (30-32) | the exemption of s 9(5)(b), step 120 | encoded | `Order s 5 — …` |
| Order s 6 (34-36) | retirement and death grants, ss 9(7A) and 32(9)(a)(1), step 10 | encoded | `Order s 6 — …` |
| Order s 7 (38-40) | employee discounts, s 9(20), step 12 | encoded | `Order s 7 — …` |
| Order s 8 (42-44) | qualifying annuity, s 9A(a) and (c), step 10 | encoded | `Order s 8 — …` |
| Order s 9 (46-48) | the exempt amount, s 9A(b), nearest whole shekel | encoded | `Order s 9 — …` |
| Order s 10 (50-52) | the medical-expenses ceiling, s 44(a)(1), step 120 | encoded | `Order s 10 — …` |
| Order s 11 (54-56) | the amount for credit, s 45A(d), step 12 | encoded | `Order s 11 — …` |
| Order s 12 (58-60) | qualifying income, s 47, step 1,200 | encoded | `Order s 12 — …` |
| Order s 13 (62-64) | the fine of s 188, step 10 | encoded | `Order s 13 — …` |
| Order s 14 (66-67) | summing and rounding the amounts of 1 April to 31 December 1985 | inert | a 1985 transition, in old units; no current question reaches it |
| Order s 15 (69-70) | rounding does not change the base of the next adjustment | encoded | `Order s 15 — the amount the next adjustment under section 120B starts from` |
| Order s 16 (72-73) | repeal of the 1980 Order | inert | quoted |
| Order s 17 (75-76) | commencement, 1 January 1986 | encoded | `Order s 17 — the Order is in force on` |
| s 120B(d) (4341-4342) | the power and the note that the Order was published | encoded | `s 120B(d) — the amount after rounding`, with the kinds the Order names and, for the rest, fork R1 |

### 2.2 Ordinance s 122 (lines 4467-4478)

| provision | disposition | where, or why not |
| --- | --- | --- |
| (a) the 10% election | encoded | `s 122(a) — the election is open for`, `s 122 — the tax at 10% on` |
| (a1) payment within 30 days | encoded | `s 122(a1) — the last day for payment for the tax year` (A7) |
| (b), (d), (e) | inert | repealed |
| (c) no deductions; the sale value is increased for betterment tax | encoded | the tax is 10% of the rent less only the (f) deduction; `s 122(c) — the sale value for betterment tax, being …` |
| (f) deduction of qualifying rent, up to the rent or 90,000 | encoded | `s 122(f)(1) — the payment is qualifying rent`, `s 122(f) — the deduction for qualifying rent, of` |
| (f)(1) qualifying rent | encoded | rent or care fees; not to a relative of s 88 paragraphs (1) or (2); the payer within the household; not claimed elsewhere |
| (f)(2) "only apartment", RE Tax Law s 9(c1c)(4) | input | a Boolean; the definition needs RE Tax Law ss 16A and 49C (lines 228-231, 748-753 of that file) and a list of the owner's apartments, which the row does not encode |
| (f)(3) the household as one owner | input | the rental income and payments of the individual, the cohabiting spouse and children under 18 are supplied together |
| the note after (f) (line 4478) | out-of-scope | the exemption on rent of a residential apartment, Law 5750-1990: not deposited and not part of s 122 |

### 2.3 Ordinance s 125B (lines 4512-4518)

| provision | disposition | where |
| --- | --- | --- |
| lead-in (notwithstanding ss 121, 126) | encoded | the rates below |
| (1) an individual, 25% | encoded | `s 125B — the rate of tax on a dividend received on` |
| (2) a material shareholder at receipt or in the 12 months before, 30% | encoded | forks S1, S4 |
| (3) a family company, 25%; 30% if the s 64A assessee is a material shareholder | encoded | fork D1 (no time is named) |
| (4) a public institution or provident fund, dividend not exempt, 25% | encoded | an exempt dividend has no rate here and is declined |
| (5) a non-resident body of persons, 25%; 30% for a material shareholder | encoded | forks S1, S4 |
| any other recipient | out-of-scope | no paragraph; declined by name |

### 2.4 Ordinance s 125C (lines 4525-4540)

| provision | disposition | where |
| --- | --- | --- |
| (a) definitions: material shareholder, index, interest | encoded (material shareholder, via s 88); input (the index: how the property is linked is given as one of four values; interest: the caller supplies the amount) | |
| (b) an individual, at most 25%, as the highest layer | encoded | `ito-top-layer.l4`, fork T1 |
| (c)(1) not linked, partly linked, or not linked until redemption: 15% | encoded | |
| (c)(2) the Minister may change the 15% by order | input | no order is deposited; 15% is the figure as printed (Q3) |
| (d)(1) to (6) the rate of s 121 if a condition holds | encoded | the answer is a treatment, not a figure: "taxed at the rates of section 121 with the rest of the income" (the tax is row IL-03's) |
| (e) outside the section | encoded | `outside section 125C`, except interest treated under s 3(h4)(3) |

### 2.5 Ordinance s 8(c) (lines 531-538)

| provision | disposition | where, or why not |
| --- | --- | --- |
| (a) premiums and key money | out-of-scope | the Director's discretion; no rule, no figure |
| (b) patents and copyrights | out-of-scope | the Director's discretion |
| (c)(1) wage and annuity differences, in the years they relate to, at most six tax years | encoded | fork E1 |
| (c)(2) vacation pay, equal parts, at most six years and the years of work | encoded | |
| (c)(3) grants of s 1 "personal exertion" (5) and (6), equal parts, at most six years | encoded | fork E2; the Director's other period is an input |
| (d) death or winding-up before the period ends | not finished | arithmetic (the rest of the income is added to the year of death) and a choice by the heirs; left for want of session time |

### 2.6 Ordinance s 88 (lines 3247-3322)

| definition | disposition | where, or why not |
| --- | --- | --- |
| "means of control" (3249-3255) | encoded | five fractions held, each an input (direct and indirect holding is outside the row) |
| "material shareholder" (3256) | encoded | 10% of any one kind, forks S1, S4 |
| "together with another" (3257) | encoded | a relative, or regular cooperation by agreement |
| "asset" (3258-3262) | encoded | the four exclusions are inputs |
| "depreciable asset" (3263) | inert | not used by ss 91, 125B, 125C |
| "business inventory" (3264) | input | s 85 |
| "index" (3265-3266) | input | the readings are supplied |
| "fixed date" (3267) | encoded | 1 January 2003 |
| "adjusted depreciation", "adjusted original price" (3268, 3282, 3287) | inert | repealed |
| "original price" (3269-3281) | encoded | six ways and the closing additions |
| "purchase day" (3283-3285) | encoded | |
| "depreciation" (3286), "remaining original price" (3288) | input | the caller supplies the remaining original price |
| "adjusted remaining original price" (3289) | encoded | fork S3 |
| "sale" (3290) | inert | open-ended; the caller says a sale occurred |
| "security", "commercial security", "future transaction", "oil and film units" (3291-3294) | inert | classifications the caller makes |
| "consideration" (3295) | encoded | |
| "relative" (3296-3301) | encoded | including the s 97 proviso |
| "capital gain" (3302) | encoded | |
| "inflationary amount" (3303-3306) | encoded | A4 |
| "chargeable inflationary amount" (3307-3309) | encoded | A5 |
| "real capital gain" (3310) | encoded | |
| "real gain up to the fixed date", "from it to the change date", "the remainder", "the change date" (3311-3314) | encoded | fork S2 |
| "regulated market" (3315) | inert | repealed |
| "capital loss" (3316) | encoded | |
| "real-estate investment fund", the mutual-fund definitions (3317-3322) | inert | cross-references and classifications |
| s 88A (3324-3327) | out-of-scope | not named by the row |

### 2.7 Ordinance s 91 (lines 3345-3391)

| provision | disposition | where, or why not |
| --- | --- | --- |
| (a) a body of persons, the rate of s 126(a) | encoded | the s 126(a) rate is an input (s 126 is not encoded) |
| (b)(1) an individual, at most 25%, highest layer | encoded | fork T1 |
| (b)(2) a security in a body of persons, material shareholder, at most 30% | encoded | forks S1, S4 |
| (b)(3) a bond and the like not linked to the index, at most 15%, 20% for a material shareholder; all gain is real | encoded | fork D2; A10 |
| (b)(3)(b) the Minister may change the rate | inert | a power; no order deposited |
| (b)(3)(c) "not linked" | input | the caller chooses the kind |
| (b1) the three parts for an asset bought before the change date | encoded | forks S2, T1, T2 |
| (b1)(1A) a security bought before the fixed date: distributable profits of s 94B | encoded | the s 94B profits are an input; fork V3 |
| (b1)(1B) listed securities and exempt fund units | encoded | |
| (b1)(2) the highest layer | encoded | |
| (b2) oil and film partnership units | encoded for a body of persons (no effect); an individual with such a part is declined by name | Q2 |
| (c) 10% on the chargeable inflationary amount | encoded | A10 |
| (d)(1) to (6) the report and the advance | out-of-scope | procedure, no rate; the 30-day day is the sale day plus 30 |
| (e)(1), (e)(2) spreading | encoded | A8; combined with (f), (g), (b2) it is declined by name (Q7) |
| (e)(3) not for exchange-listed securities | encoded | |
| (f) old assets: 12%, 1% a year | encoded | forks V1, V2 |
| (g) expropriation: half | encoded | |
| (h) the Minister's power over transfers between controlling shareholders | inert | a power |

### 2.8 Ordinance s 64A1 (lines 2105-2156), s 64A2 (lines 2160-2209)

| provision | disposition | where, or why not |
| --- | --- | --- |
| 64A1 note: applies from the entry into force of regulations | input | a Boolean with no default; declined if not shown (Q4) |
| 64A1(a) the eight conditions | encoded | |
| (b) attribution to the shareholders | encoded | |
| (b)(1) profits distributed are not income | inert | the consequence; the arithmetic of "profits distributed" is (b)(2) |
| (b)(2) profits distributed | encoded | |
| (b)(3)(a) losses first against the income from the company | encoded | |
| (b)(3)(b) earlier years' losses only against the shareholder's income | out-of-scope | a restriction on which income, no figure |
| (b)(4) the source follows the company's; active role | encoded | |
| (b)(5) foreign tax | encoded | |
| (b)(6) advances | out-of-scope | adds the share to the turnover for advances; no figure beyond the attribution |
| (b)(7) collection from the company or the shareholders | out-of-scope | |
| (b)(8)(a) sale of a share: the reduction | encoded | |
| (b)(8)(b) s 94B does not apply for the benefit years | out-of-scope | a disapplication |
| (b)(8)(c) the seller's adjusted price is reduced by losses | encoded | |
| (b)(9) notify within 90 days | encoded | |
| (b)(10) Part 5-2 does not apply | out-of-scope | |
| (b)(11)(a) winding-up: no tax; 0.5% purchase tax | encoded | |
| (b)(11)(b), (c)(1), (e) | inert | powers of the Minister |
| (c)(2) a company that ceased to be transparent may ask to be wound up within a year | out-of-scope | an administrative request with the Director's approval |
| (d)(1) the last day to assess | encoded | |
| (d)(2) objection and appeal | out-of-scope | |
| 64A2(a): "yielding land" | encoded | |
| 64A2(a): "exceptional income" | encoded | fork Q1 |
| 64A2(a): "land held for a short period" | encoded | A11 |
| 64A2(a): the other definitions (request for additional rights, long-term rental, the Government rental-housing company, the planning law, land for rental housing and its yielding form, assets of issue and consideration, the fund, the defining period, tax, land under construction, plan, plan for rental housing, asset, sale to a landlord) | inert | conditions that are facts the caller supplies, or cross-references; the fund's tax regime, ss 64A3 onward, is not part of the row |
| 64A2(b) | inert | a general cross-reference |

### 2.9 Ordinance ss 57, 55, 60A

| provision | disposition | where, or why not |
| --- | --- | --- |
| 57(a) the kibbutz pays the total of its members' taxes on equal shares | encoded | the scale is a function the caller supplies; the credit points and s 47 deductions of each member are inputs |
| 57(b)(1) the separate computation: three conditions; the base | encoded | |
| 57(b)(2), (2a), (3) | out-of-scope | point to s 66(c) (row IL-02), ss 38 and 39, and a power |
| 57(c) report online | out-of-scope | a duty |
| "qualifying work", "kibbutz" | inert | conditions that are facts |
| 55(a) assessed under the sub-chapter | encoded | `s 55 — the member's income is assessed` |
| 55(b) income not transferred: assessed apart; the rates, credit points and losses of the kibbutz's assessment left out | encoded | Q5 |
| 60A(b)(1), (2) the renewed kibbutz | encoded | `ito-60a2-renewed-kibbutz-member.l4` |
| 60A(a), (b)(3), (4), (c), (d) | out-of-scope | not named by the row |

### 2.10 The RE Tax Law (RE Tax Law file lines)

| provision | disposition | where, or why not |
| --- | --- | --- |
| s 6(a) the imposition of the tax | inert | |
| s 6(b) the betterment | encoded | `s 6(b) — the betterment on a sale value of …` |
| s 7 the action in a land association | inert | the imposition; the rate is s 48A |
| s 9(a) rates fixed by the Minister | out-of-scope | the regulations are not deposited |
| s 9(b) an action in a land association | out-of-scope | the proportional part, no rate |
| s 9(c), (c1), (c1a) the windows from 1995 to 5 May 2013 | out-of-scope | the printed amounts were indexed on every 16 January while the windows ran and the indices are not supplied (the independent tester's PT54, PT60) |
| s 9(c1b)(1), (2) the sales of 6 May to 31 July 2013 | encoded (0.1.1) | the bands as printed |
| s 9(c1c)(3) the table: the 2013, 2022, 2023 and 2024 columns | encoded (0.1.1) | for a buyer under (c1c)(2); 2014 to 2021 are not printed; a buyer outside (c1c)(2) before 16 January 2025 is declined, since the amounts of (c1c)(1) are printed for 2025 only |
| s 9(c1c)(1) bands | encoded | as printed for 2025 |
| s 9(c1c)(2), (3), (4) | encoded | the conditions are inputs |
| s 9(c1f) 8% and 10% | encoded | fork P1 |
| s 9(c2) indexation from 16 January 2028 | encoded | forks R2; the index readings are an input |
| s 9(c3), (c4), (d), (e) | inert | publication, powers |
| s 9A, 9B, 9C, 9D | out-of-scope | repealed or temporary provisions of 2001 to 2003 |
| s 48A(a) a body of persons | encoded | |
| s 48A(b)(1), (1A), (2) | encoded | |
| s 48A(b1) | encoded | forks S2, T1, T2 |
| s 48A(b2) | encoded | |
| s 48A(b3) | encoded as a refusal | needs the amounts of s 49Z |
| s 48A(b4) | encoded | fork 30-F20 (0.1.1) |
| s 48A(c) | encoded | |
| s 48A(d) | encoded | forks L1, V1, V2 |
| s 48A(e) spreading | not finished | the same machinery as ITO s 91(e) with the Law's periods |
| s 48A1 | out-of-scope | a temporary provision for sales from 2001 to 2003 |
| s 48B the betterment as part of taxable income | out-of-scope | an assessment rule; the layering is s 91's |
| s 48C expropriation | out-of-scope | a credit table in pounds (liras), a historic currency |

## 3. The fork register

Every fork below was ruled by Meng on 2026-10-08 (SHRUG): one named switch, declined by default, the other readings kept by name.
The default declines only where the readings give different answers to the question asked; where they agree the rule answers.
Each is tested in the module named, with the default, each reading by name, and a case where the readings agree.

| id | provision | the readings | default | tested in |
| --- | --- | --- | --- | --- |
| 30-F1 (R1) | s 120B(d), an amount the Order names no rule for (the donation amounts of s 46(a) and several of the social deductions) | declined; stays as adjusted | declined | `tests-rounding-order.l4` |
| 30-F2 (S1) | s 88 "alone or together with another" | any number of others added; one other only | declined where they differ | `tests-88-definitions.l4`, `tests-125b-dividends.l4` |
| 30-F3 (S2) | s 88 and RE Tax Law s 47 how the days of "the period from A to B" are counted, and where a boundary day (the commencement day, the transition day) falls (0.1.1) | both ends with the boundary day in the part after it; the days between; both ends with the boundary day in the part before it | declined where they differ | `tests-88-definitions.l4`, `tests-91-capital-gains.l4` |
| 30-F4 (S3) | s 88 half of the holding expenses, which the adjusted price leaves out | lost; added back unindexed | declined where there are holding expenses | `tests-88-definitions.l4` |
| 30-F5 (S4) | s 88 and ss 91, 125B, 125C the twelve months before a day | from the day twelve months before; from the day after | declined where they differ | `tests-88-definitions.l4`, `tests-125b-dividends.l4`, `tests-125c-interest.l4` |
| 30-F6 (D1) | s 125B(3) names no time for the shareholding | at receipt only; at receipt or in the twelve months; at any time up to receipt (0.1.1) | declined where they differ | `tests-125b-dividends.l4` |
| 30-F7 (D2) | s 91(b)(3) names no time for the shareholding | at the sale only; at the sale or in the twelve months; at any time up to the sale (0.1.1) | declined where they differ | `tests-91-capital-gains.l4` |
| 30-F8 (T1) | a cap "not exceeding 25%" where the gain stands in several bands | each band's rate capped; the average rate capped | declined where they differ | `tests-top-layer.l4` and every module that uses it |
| 30-F9 (T2) | where the three parts of a gain stand in the top layer | each alone on the other income; earliest lowest; earliest highest | declined where they differ | `tests-top-layer.l4` (three parts); the RE Tax Law's flat-part-and-two-parts variant is tested only on a flat scale, where the places do not matter |
| 30-F10 (V1) | s 91(f)(1) and RE Tax Law s 48A(d)(1): "1% for each year from 1949 until the year of acquisition" | both ends counted; the year of acquisition not counted | declined where they differ | `tests-91-capital-gains.l4` (the RE Tax Law's s 48A(d) uses the same fork; its tests acquire in 1940, before the 1949 years begin, so only V2 is exercised there) |
| 30-F11 (V2) | s 91(f)(2): "from tax year 2005, 1% for each tax year or part" | 2005 and the sale year both counted; 2005 not counted | declined where they differ | `tests-91-capital-gains.l4` |
| 30-F12 (V3) | s 91(b1)(1A): is the middle part also reduced by the distributable profits | all three parts reduced; the middle part unreduced | declined where they differ | `tests-91-capital-gains.l4` |
| 30-F13 (E1) | s 8(c)(1) a difference older than six tax years | placed in the year of receipt; in the earliest of the six | declined | `tests-8c-spreading.l4` |
| 30-F14 (E2) | s 8(c)(3) working years that end before the year of receipt | only those inside the six years; the last six working years | declined where they differ | `tests-8c-spreading.l4` |
| 30-F15 (Q1) | s 64A2 "exceptional income" (2): "whose total rate exceeds 5%" | all the other income once it is more than 5%; only the part above 5% | declined where they differ | `tests-64a2-fund-definitions.l4` |
| 30-F16 (L1) | RE Tax Law s 47 "tax year" begins on 1 April; which calendar year names it | the year it begins in; the year it ends in | declined where they differ | `tests-retl-48a-betterment-tax.l4` |
| 30-F17 (P1) | RE Tax Law s 9(c1f): printed to end on 31 December 2024, the consolidation's note says extended to 31 December 2026 | ends 2024; ends 2026 | declined where they differ | `tests-retl-9-purchase-tax.l4` |
| 30-F19 (T3) | s 91(e)(1) a right bought and sold in the same tax year: the period of ownership is empty (0.1.1) | an empty period gives no tax year (spreading not open); it gives one tax year | declined | `tests-91-capital-gains.l4` |
| 30-F20 (B4) | RE Tax Law s 48A(b4) against s 48A(b1) for a qualifying apartment bought before the change date with the (b4) conditions (0.1.1) | (b4) restores plain (b)(1); (b1) still applies | declined where the amounts differ | `tests-retl-48a-betterment-tax.l4` |
| 30-F18 (R2) | RE Tax Law s 9(c2): "the nearest multiple of 5 shekels", where a half goes | up; down | declined where they differ | `tests-retl-9-purchase-tax.l4` |

Not forks, with the argument (so a reviewer can disagree):

- **Limb (a) "nearest" and limb (b) of the Order.**
  If the round amount is the multiple not above the adjusted amount, limb (b) does all the work; if it is the nearest multiple, the excess is negative whenever the nearest multiple is above and limb (b) adds nothing, and at the tie (an excess of exactly half a step) limb (b) says to go up either way.
  Every reading therefore gives the same figure for every amount; `tests-rounding-order.l4` asserts that the floor reading and both nearest readings agree on a grid of ten amounts including every tie.
- **The commencement day in two parts (0.1.1).**
  At 0.1.0 the reading "both the first and the last day are counted" put the commencement day (7 November 2001) in the first part and in the second, so the parts overlapped by a day (the independent tester's BT09, BT11, BT12).
  That is not arguable as a partition of the period, so it is gone: under every reading the parts now add to the whole.
  The text says the second part runs "from the commencement day" and the first "until" it; the only reading in which no day is counted twice puts the commencement day in the second part (the default "both" reading) or, as a named alternative, in the first part with the second beginning the day after.
  The transition day (the exempt part of (b2) runs "until" it; the rest is "after" it) can lie in either part without any overlap, because the rest is the whole less the exempt part; both readings are named (fork 30-F3), and the tester's (the transition day in the rest) is the default "both" reading.
- **"Part of the capital gain" in the inflationary amount.**
  A part cannot exceed the whole, so the inflationary amount is capped at the gain (A4).

## 4. Assumptions: what was assumed rather than read

| id | the assumption | the text that licenses it, or its absence |
| --- | --- | --- |
| A1 | The Order's limb (a) and (b) are read together as the floor reading; see section 3. | the Order, ss 1 to 13 |
| A2 | The Order is in force: nothing in the deposited sources repeals or replaces it. | the Order file is the 2025 consolidation; the Ordinance's note after s 120B(d) (line 4342) records it |
| A3 | In "relative" paragraph (3), the 25% holding is the largest fraction the person holds of any kind, already counting what he holds directly or indirectly; the "together with another" aggregation of s 88 is not applied again inside it. | line 3299 says "alone or together with another", and this encoding takes the caller's figure as the whole |
| A4 | The inflationary amount is at most the capital gain. | "the part of the capital gain equal to the amount" (line 3304) |
| A5 | The chargeable inflationary amount is nought for an asset bought on or after 1 January 1994, and for a bond sold under s 91(b)(3). | "had the asset been sold on 31 December 1993" (line 3309); (b)(3) "all the gain is regarded as real" (line 3349) |
| A6 | A date before the text's own change date (1 January 2012) is declined for ss 91, 125B, 125C and the RE Tax Law's s 48A. The deposited texts are as amended at retrieval; the last amendment tags in the section headings are 5772 (2012) for ss 125B and 125C, 5777 (2017) for s 91, 5783 for the RE Tax Law's s 48A. The effective dates of those amendments are in Sefer HaChukim, which is not deposited. | needs a source; for sales from 2012 to 2017 a rate may be that of the text as amended later than the sale |
| A7 | The last day for payment under s 122(a1) is 31 December plus 30 days (30 January). | "within 30 days from the end of the tax year" (line 4469) |
| A8 | Section 91(e)(2) is read as: the three parts of (b1) are computed on the whole gain as if no request were made, each part is divided into equal annual parts, and each year taxes its shares above that year's other income, less the credit points left unused. | line 3382-3385; the text says the parts are "computed as they would have been but for the request" and that the tax takes account of the rates of (b1), the rates on the total income and the credit points |
| A9 | In s 91(f)(2) and RE Tax Law s 48A(d)(2), (3), the "rate of (a) or (b)(1) or (2)" with which the (f) rate is compared is the rate of the body of persons, or 25% (30% for a security sold by a material shareholder); for a bond under (b)(3) it is 25%. | the paragraphs name (a), (b)(1), (b)(2) and not (b)(3) |
| A10 | Under s 91(b)(3) there is no inflationary amount and so no chargeable inflationary amount. | "all the capital gain is regarded as real capital gain" |
| A11 | In s 64A2 "land held for a short period", a sale on the fourth anniversary is not within "less than four years". | "less than four years passed" (line 2184); "before four years passed" (line 2185) |
| A12 | "Left out of the member's assessment" in ss 55(b) and 60A(b)(2) is a Boolean that is TRUE for income not transferred (or not reported). Where that income stands on the scale is not decided. | lines 1864 and 1916 say what is not counted, not what is |
| A13 | Section 91(b)(2) and (b)(3), which say "at a rate not exceeding", share the layering sentence of (b)(1) ("regarded as the highest layer"). | (b)(2) and (b)(3) are exceptions to (b)(1) and a rate "as in s 121" needs a place on the scale |
| A14 | Withdrawn at 0.1.1: the collision of s 48A(b4) with (b1) is fork 30-F20, declined by default where the amounts differ. | lines 624 and 641 of the RE Tax Law file |
| A15 | (0.1.1: the 2022 to 2024 and 2013 columns of the table are encoded too, for a buyer under (c1c)(2).) The purchase-tax bands printed for 2025 hold for sales from 16 January 2025 to 15 January 2028. | the table note after (c1c)(3) (line 219) gives the tax year as 16 January to 15 January; (c2) skips the tax years 2025 to 2027 |
| A16 | A kibbutz member's family composition gives his credit points and s 47 deductions as inputs, and his tax on an equal share is the scale applied to the share less the s 47 deductions, less the credit points, not below nought. | s 57(a), lines 1870 |
| A17 | A tax year of the Ordinance is the calendar year. | s 1 "tax year" (line 202) |
| A18 | The fine of s 188, which the Order's s 13 covers, is not an amount that s 120B(a) adjusts, and s 9A(b), which the Order's s 9 covers, is not in the s 120A list of social deductions. The Order's thirteen rules are encoded as it states them. | line 4332 (the list); the Order's ss 9 and 13 |
| A19 | A dividend exempt in the hands of a public institution or provident fund has no rate under s 125B(4) and is declined. | (4) fixes a rate "for a dividend that is not exempt" |
| A20 | Under s 125C(d) the interest is on the s 121 scale with the rest of the income; this encoding does not place it. | (d) gives no place |
| A21 | The count of the employee's years of work in s 8(c)(2) is a whole number of years, supplied. | "the years of his work" (line 536) |

## 5. Answer table

A sample of the answers `check.sh` proves, each from a test named here and worked by hand before it was run.
The scales in these tests are fixtures (the s 121 bands as printed, or one flat band); which scale applies is row IL-03's.

| question | answer | provision | test |
| --- | --- | --- | --- |
| an income ceiling of 301,259 after the index adjustment, rounded | 301,200 | Order s 1 | `tests-rounding-order.l4` |
| the same at 301,260 | 301,320 | Order s 1 | same |
| a credit-point amount of 125, and of 126 | 120, and 132 | Order s 2 | same |
| an allowance-point amount of 235.5 | 236 | Order s 3 | same |
| the unrounded base of the next adjustment, 1,139.9, when rounded to 1,080 | 1,139.9 | Order s 15 | same |
| a donation amount of 1,139.9 (the Order has no rule) | declined by default; 1,139.9 at the other reading | 120B(d) | same |
| a dividend of 40,000 to an individual with no 10% holding | tax 10,000 (25%) | 125B(1) | `tests-125b-dividends.l4` |
| the same, the individual holding 10% on the day | 12,000 (30%) | 125B(2) | same |
| the same, a record of 10% exactly twelve months before | declined (the readings of the twelve months part) | 125B(2), S4 | same |
| interest of 100,000, wholly index-linked, top of the 31% band | 25,000 | 125C(b) | `tests-125c-interest.l4` |
| the same, not index-linked | 15,000 | 125C(c)(1) | same |
| the same, with books kept | taxed at the rates of s 121 with the rest | 125C(d)(1) | same |
| rent 120,000 from the only apartment, 100,000 of qualifying rent paid | tax 3,000 | 122(a), (f) | `tests-122-residential-rent.l4` |
| a gain of 200,000, bought 2013, no other income, scale (a) | 50,000 | 91(b)(1) | `tests-91-capital-gains.l4` |
| the same security sold by a material shareholder | 60,000 | 91(b)(2) | same |
| a non-indexed bond, gain 100,000 | 15,000; 20,000 for a material shareholder | 91(b)(3) | same |
| a body of persons at 23%, gain 200,000 | 46,000 | 91(a) | same |
| an asset bought 1 January 2000, sold 1 January 2020, flat scale, real gain 53,370,330 | 13,902,222.1 (days between), 13,903,387.35 (both ends), declined by default | 91(b1), S2 | same |
| four-year spreading of 400,000 with credit points left unused of 5,000 and 30,000 in the first two years | 70,000 | 91(e)(1) | same |
| wage differences related to 2020 and received in 2026 | declined by default (older than the six tax years) | 8(c)(1), E1 | `tests-8c-spreading.l4` |
| vacation pay of 60,000 over 3 years, received in 2026 | 20,000 in each of 2024, 2025, 2026 | 8(c)(2) | same |
| a company with 51 shareholders and the Director's approval up to 60 | transparent (if the other conditions hold and the regulations are in force) | 64A1(a) | `tests-64a1-transparent-company.l4` |
| a kibbutz with taxable income 1,000,000 and four members | 65,000 (fixture scale) | 57(a) | `tests-57-kibbutz-tax.l4` |
| betterment on a sale value of 1,000,000 over 700,000 | 300,000 | RE Tax Law s 6(b) | `tests-retl-48a-betterment-tax.l4` |
| betterment tax, real betterment 200,000, bought 2013, scale (a) | 50,000 | 48A(b)(1) | same |
| purchase tax on 2,000,000, the buyer's only apartment, 30 June 2026 | 743.925 | 9(c1c)(3) | `tests-retl-9-purchase-tax.l4` |
| the same for an investor | declined (the end of the (c1f) period is given two ways); 105,342 from 1 January 2027 | 9(c1f), P1 | same |

## 6. What `check.sh` prints

The l4 binary is `jl4-0.1-6df1397b`, sha256 `f0759b2ef2f1d1b2a577c68f059c54f487de9d913553fc9f0d9bf0f7f5dab0d8`, the same before and after the 0.1.1 run (the 0.1.0 run is in section 11).
Exit code 0, 35 modules, 1 error (the one declared failure of the independent module), 1040 assertions satisfied, 1 failed, 10 refused.
This encoding's own test modules have no failure and no refusal: every refusal they make is asserted with `#ASSERT REFUSED … BECAUSE "…"` and counts as satisfied.
The independent module `tests-independent.l4` (fid-il-30, frozen, sha256 `2778d70caca08dcfbebfec37a691124af8a201b2e79fb5f33009928d8f9967e2`) has 422 satisfied, 1 failed and 10 refused, all declared line by line in `check.sh`:
the failure is BT10 (TESTER-WRONG, section 11); the refusals are CG20, CG22 (3 assertions), T30, BT16, BT17 (a date before 2012), T49 and BT27 (forks 30-F19 and 30-F20, new), DV21 and PT54.

| module | satisfied |
| --- | ---: |
| `tests-rounding-order.l4` | 109 |
| `tests-120b-d.l4` | 13 |
| `tests-88-definitions.l4` | 119 |
| `tests-top-layer.l4` | 23 |
| `tests-125b-dividends.l4` | 31 |
| `tests-125c-interest.l4` | 24 |
| `tests-122-residential-rent.l4` | 29 |
| `tests-91-capital-gains.l4` | 80 |
| `tests-8c-spreading.l4` | 21 |
| `tests-64a1-transparent-company.l4` | 35 |
| `tests-64a2-fund-definitions.l4` | 19 |
| `tests-55b-kibbutz-member.l4` | 8 |
| `tests-60a2-renewed-kibbutz-member.l4` | 8 |
| `tests-57-kibbutz-tax.l4` | 11 |
| `tests-retl-48a-betterment-tax.l4` | 46 |
| `tests-retl-9-purchase-tax.l4` | 42 |
| own tests, total | 618 |
| `tests-independent.l4` | 422 |
| all | 1040 |

The Hebrew check (`tools/hebcheck.py`) passes: every run of Hebrew outside a `-- src:N |` quotation occurs verbatim in the source file the module names.
The quotations are generated by `tools/srcquote.py`, never typed.

## 7. Findings during the work

- **A default declined at the component level where the answer did not part.**
  The first version of the three parts of s 88 declined as soon as the way of counting days changed the denominator, even for an asset bought on the fixed date, where the first part is nought on either counting.
  `tests-88-definitions.l4` caught it (a refused assertion where an answer was meant).
  The rules now compute the final figure under each counting and compare, which is what the SHRUG policy asks.
- **A hand value corrected, with the reason.**
  My hand value for the (b4) test of the RE Tax Law assumed (b4) displaces (b1) for an apartment bought in 2010; the code gave the (b1) figure, and the text says (b4) disapplies (b2) and (b3) only (assumption A14).
  I did not edit the expected value to fit: I re-read the text, moved that test's purchase date to 2013 (so that it tests (b4) alone), and added a second test for the 2010 purchase whose value (3,252,037.15) I worked out by hand first.
- **Evidence on fork R1 from the consolidation's notes (not law).**
  The figures the notes after s 125D print for 2024 to 2027 are multiples of 120, as the Order's s 1 would round them; the s 58A(c) figures (283,905 for 2023 and 293,397 for 2024 to 2027) are multiples of neither 12 nor 120.
  The Order names no rule for s 58A(c) or s 125D, so the notes cannot settle what the Order leaves open, but the 58A(c) figures are what an unrounded amount looks like.
- **The Order covers fewer amounts than s 120B adjusts.**
  Of the fourteen "social deductions" that s 120A lists (line 4332), the Order names ss 9(5), 9(7A), 9(20), 9A(a), 44(a)(1), 45A(d), 47, and 32(9)(a)(1); it names no rule for 9(16A), (16B), (18A), 17(5A), the rest of 32(9) and of 45A, 58A(c) and 125D, nor for the recognised donation amounts of s 46(a).
  Its s 9 (9A(b)) and s 13 (the fine of s 188) cover amounts that the s 120A list does not name.
- **Tooling notes for the next encoder.**
  A mixfix name may not end in a keyword (`` `a holding of` f `in the right to profits` `` is not read as one call); a percent literal that is an argument and is followed by a keyword must be in parentheses; a keyword called `and` is read as the operator; `REFUSE` takes a string literal only, not a variable; a lambda takes one argument.
  Two sum types in this row both have a constructor `an individual`, so a test that builds one names it through a one-line wrapper.

## 8. For IL-03 (not edited) and IL-55

**Rounding for IL-03.**
IL-03's `ito-120b-indexation.l4` declines `the rounding rules made under section 120B(d) are not encoded in this model`.
To call the rule, a row vendors three files from this directory beside its own modules, recording these hashes, and never edits the originals:

| file | sha256 |
| --- | --- |
| `ito-rounding-order-nouns.l4` | `8ffa2a650a11e8b97bee8a2a459b3af2d1770524f2efb0bacba2c860c24f426a` |
| `ito-rounding-order-5746.l4` | `eb9bd4676e306773adb43b78aff2a2b3919bb7d054ea241a9f104635ddb9c1d0` |
| `ito-120b-d-rounding-power.l4` | `3a7b7111cb4ff5b9cad1945f38d964365b7db9ad7d402aeb20a829399265a33f` |

The call is `s 120B(d) — the amount after rounding` amount `, of the kind` kind, with the kind `an income ceiling`, `the amount of a credit point` or `the amount of an allowance point` for the three groups IL-03 uses.
Section 15 of the Order says the base of the next adjustment is the unrounded figure; that is the reading IL-03's fork F6 takes for 2029 onward, and this row finds nothing against it.

**Inputs this row takes that the capstone does not supply today (for IL-55):**

- the s 126(a) rate of tax on a body of persons (s 91(a), 48A(a));
- the highest rate in s 121 (RE Tax Law s 48A(b1)(1)(a));
- the scale of s 121 as a list of bands, and the individual's other taxable income, for the layered rates (ss 91, 125C, 48A);
- the credit points left unused in each year of a spreading (s 91(e));
- the individual's holdings, direct and indirect, by kind of means of control, on each day that they changed (the material shareholder tests);
- the real capital gain, the capital gain and the chargeable inflationary amount (from s 88's rules, which this row encodes), the s 94B distributable profits, and the index readings;
- the credit-point values and s 47 deductions of each kibbutz member, and the scale as a function (s 57);
- for the purchase tax: whether the buyer qualifies under (c1c)(2), and from 16 January 2028 the housing-services index readings;
- whether the regulations under s 64A1 are in force.

**What the capstone would need.**
The capstone's earner has a salary only, and none of these regimes touches salary.
To reach them it would need a second kind of income item with its rate section, and the choices above as inputs; it would call IL-03's scale for the layered rates (as `A band of a marginal scale` values) rather than a number.

## 9. Sources, and what needs a source we do not have

Deposited and read: the three files named in `BRIEF.md`.
Needed and not deposited, so declined by name or taken as an input:

- the amendments' effective dates (Sefer HaChukim) for ss 91, 125B, 125C and the RE Tax Law's s 48A, so that a sale before the 5772 round is declined (A6);
- the regulations under s 64A1 and the order, if any, under s 125C(c)(2);
- the order (Kovetz HaTakanot 5785, p 626) that the consolidation's note says extended s 9(c1f) to 31 December 2026;
- the publications of the housing-services index (for the purchase tax from 16 January 2028);
- the Income Tax (Exemption on Income from the Rent of a Residential Apartment) Law 5750-1990 (the note after s 122(f));
- the Companies Law, the Value Added Tax Law, the Inflation Adjustments Law (named in the conditions of s 64A1 and s 64A2);
- ss 49Z, 16A, 49C and 49E of the RE Tax Law are in the deposited file but are not encoded by this row (the Law's rates only).

## 10. Open questions for a domain expert

1. **Q1.** Does s 125B(3) test the s 64A assessee's shareholding at receipt only, or at receipt and in the twelve months before, as (2) and (5) say? (30-F6)
2. **Q2.** Where does the part of an individual's real gain equal to depletion deductions stand in the scale under s 91(b2)? (declined by name)
3. **Q3.** Has the Minister changed the 15% of s 125C(c)(1) by an order under (c)(2)? (none is deposited)
4. **Q4.** Are the regulations under s 64A1 in force? (the note at the head of the section makes the section depend on them)
5. **Q5.** In ss 55(b) and 60A(b)(2), when "the rates counted in the kibbutz's assessment are not counted", does the member's own income stand on the scale above the share the kibbutz's assessment gave him?
6. **Q6.** Does RE Tax Law s 48A(b4) restore plain (b)(1) for a pre-2012 purchase, or does (b1) still apply? (fork 30-F20)
7. **Q7.** How does s 91(e) combine with (f), (g) and (b2)? (declined by name)
8. **Q8.** What were the rates in ss 91, 125B, 125C and 48A for a sale between 2012 and the later amendments? (A6)
9. **Q9.** For RE Tax Law s 48A(b1)(1)(a), is "the highest rate in s 121" the 47% marginal rate, or includes the 3% and 2% additional tax of s 121B? (taken as an input)

## 11. Version 0.1.1: the repair after the independent pass

The independent pass (fid-il-30; `INDEPENDENT-FINDINGS.md`, `tests-independent.l4`, `DECIDED-ANSWERS.md`, all frozen) decided 500 cases; none was OURS-WRONG and all 435 quotations matched.
At 0.1.0 `check.sh` printed, for the 35 modules, 984 satisfied, 11 failed, 17 refused; l4 `jl4-0.1-6df1397b`, sha256 `f0759b2e…dab0d8`, unchanged.
At 0.1.1: 1040 satisfied, 1 failed, 10 refused, exit 0, the same binary before and after.
What changed, in the order the lead set:

1. **DV12 (forks D1 and D2).**
   The tester's third reading, that "was" has no limit of time, is added to both forks (`at any time up to the receiving of the dividend`, `at any time up to the sale`), named and tested; the default declines where it differs from the other two, so a holding 18 months before a family company's dividend is now declined (the tester's expectation) and gives 25%, 25%, 30% under the three named readings.
2. **BT09, BT11, BT12, BT19, BT20, BT22, BT23 (the day counts, fork 30-F3).**
   I re-read s 47.
   The reading "both the first and the last day are counted" did double count the commencement day (once as the end of the first part, once as the start of the second), so it was not an arguable reading and is replaced: the parts now partition the days under every reading (section 3).
   The transition day is arguable either way and is a named reading.
   The partition is tested: the first two parts add to the days from the purchase day to 31 December 2011 for purchases on 6, 7 and 8 November 2001, under each reading.
   The tester's seven assertions now pass as written, with their expected values unchanged.
3. **T49 (fork 30-F19).**
   I re-read s 91(e): "the shorter of four tax years or the period of ownership", the period beginning after the year the right reached the seller and ending in the year it left his hands.
   The text does not say what that is when the period is empty, so it is a switch with no default answer: the number of tax years, and the tax, are declined unless a reading is named.
   The tester's assertion (1 year) is now a declared refusal, and the one-year reading is tested (200,000 over scale (a), tax 50,000).
4. **BT27 (fork 30-F20).**
   The collision of (b4) with (b1) is a named switch (assumption A14 is withdrawn); the default declines where the readings give different amounts.
   For a 2010 purchase with the (b4) conditions the readings give 3,252,037.15 and 3,385,189 (flat scale, days between).
   The tester's assertion is now a declared refusal.
   For a 2013 purchase the clauses do not collide and every reading gives 3,385,189.
5. **Cosmetic.**
   "5 shillings" is now "5 shekels" in the modules, the fork register and `encoding.json` (the Hebrew is `5 ש״ח`); no value moved.
6. **The records the lead asked for.**
   - BT10 is TESTER-WRONG: the 25% middle-part rate for a material shareholder is in ITO s 91(b1)(1)(a)(2), not in the RE Tax Law's s 48A(b1)(1)(b), which prints "up to 20%" with no proviso; the assertion stays failing, its expected value unchanged, and is the one declared failure.
   - DV21 (a dividend on 29 February 2024 with a holding on 28 February 2023): the encoding is right to decline, because the first day of "the twelve months before" is either a day that does not exist (29 February 2023) or 1 March 2023; the tester's 25% assumed the later reading.
   - The 16 SCOPE refusals at 0.1.0: PT37, PT43, PT44, PT45, PT47 were answerable from the table in the text (the 2022, 2023 and 2024 columns), and PT48, PT49, PT51, PT53 from the 2013 column and the (c1b) scales; all nine are now encoded and pass (`retl-9-purchase-tax.l4`).
     PT54 stays declined: the (c1a)(1) amounts were indexed on every 16 January while that window ran, so the single printed figure cannot be applied to a given date in the 14 years without the indices.
     CG20, CG22 (three assertions): the s 88 parts for a sale before the fixed date or the change date are declined by the guards of `ito-88-definitions.l4`; the definitions have no date limit but a ratio over a period that has not ended has no meaning, and the rate sections decline those dates anyway (A6).
     T30, BT16, BT17: a sale before 1 January 2012 (A6).
   - Thin coverage the tester lists, taken as true: the day-count apportionments rest on one pairing of end days (the fork now covers three); the kibbutz tax is tested with a fixture scale; ss 8(c)(d), 48A(e) and 91(d) have no entry point; s 120B(a), (b) and (e) belong to IL-03; the surtax of s 121B is out.
   - Unfinished, as before: ITO s 8(c)(d) (death or winding-up before the period ends) and RE Tax Law s 48A(e) (spreading of land betterment).
