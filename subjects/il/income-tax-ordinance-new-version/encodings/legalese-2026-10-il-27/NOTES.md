# NOTES — row IL-27 (version 0.1.1)

Income Tax Ordinance ss 39A, 39B, 40A to 40F, 41, 44, 45, 46 to 46C, 47A; s 35(e) with the rules of 5738-1977; s 47(d) with the Regulations of 5740-1980; the Retirement Age Law 5764-2004.
Run `IL-27-20261008`, agent `enc-il-27`, 2026-10-08 to 2026-10-09, one session, no sub-agents.
Status: draft. No domain expert has read this encoding against the source (HG1 not sought). No independent test pass has been run yet. Every expected value in the tests was worked by hand from the Hebrew by the session that wrote the rules.

## 0. Conventions

Identifiers are English backtick names (`@lang en`).
Hebrew appears only in `-- src:N |` comments (line N of the Ordinance), `-- ext:[TAG:N] |` comments (line N of the rules of 5738-1977 `reg35`, the Regulations of 5740-1980 `reg47`, or the Retirement Age Law `ral`), and short runs in other comments.
`tools/srcquote.py` generates the first two kinds from the deposited files and `tools/sq.sh --check` verifies them, and every other run of Hebrew, against the union of the four sources (exit 0 on 2026-10-08T23:13Z for every module of this row's own; the vendored modules of rows IL-01 and IL-08 are checked in those rows, where their `ext:[a262]` lines are verified against the amending Law's PDF).
Money is NIS, a bare NUMBER, for a whole tax year.
A credit's answer is credit points (a NUMBER, fractions exact); the section's credit in NIS is points times the value of a credit point, which is an input (IL-01 s 33A).
Every top-level rule opens with `for tax year Y, row IL-27 answers`, which refuses a tax year before 2024 (assumption A1).

## 1. What is encoded and what is not

**Encoded.**
s 39A: a sixth of a point (23 full months of regular service for a man, 22 for a woman) or a twelfth for each month of the 36 after the month of discharge.
s 39B: points for reserve service as a fighter in the previous tax year, under paragraphs (1) and (2) or the temporary provision for 2026 and 2027.
s 40A: one point for a divorcee who has married again.
s 40B: one point for an individual or spouse who has completed 16 years but not 18.
s 40C: a point for a first degree and half a point for a second, in as many tax years as the years of study (3 and 2), with the second text for studies that ended 2014 to 2022, the internship election, the third degree in medicine or dentistry and the direct track.
s 40D: a point for vocational studies of 1,700 hours, with its second text for studies that ended 2018 to 2022.
s 40E: the election between the two; s 40F is repealed.
s 41: a spouse (not registered) married for part of the year.
s 44: a 35% credit for keeping a relative in an institution above 12.5% of taxable income.
s 45: two points for a paralysed, blind or disabled child.
s 46: the credit for donations, with the minimum, the ceiling and the carry-in; s 46A the overall ceiling with research and development; s 46B the base for advance payments; s 46C is repealed.
s 47A: the deduction of 52% of National Insurance contributions, with the refund rule from 2025.
s 35(e): rule 2 (who is treated as an immigrant) and rule 3 (periods left out of the count), composed with row IL-08's fractions of a point.
s 47(d): regulations 1 and 2 (the enlarged deduction at 50 years of age), composed with row IL-08's s 47 and its order with s 45A.
The Retirement Age Law: ss 3 and 6 and the Schedule's Parts A and B, the retirement age in months by sex and birth month, and "reached in or before a tax year".

**Not encoded, each with its reason:** the coverage table (section 2).

## 2. Coverage table

| source | provision | disposition | where |
| --- | --- | --- | --- |
| ITO line 1609 | s 39A | encoded | `ito-s39a-discharged-soldier.l4`, tests `ito-il27-tests-s39a.l4` (28) |
| ITO line 1617 | s 39A, the definitions "discharged soldier" and "regular service" (Discharged Soldiers Absorption Law 5754-1994) | out-of-scope: the Law is not in the source bundle; whether one is a discharged soldier, and his full months of service, are facts the caller states | `A discharged soldier in a tax year, for section 39A` |
| ITO line 1619 | s 39B(a)(1), (2) | encoded | `ito-s39b-combat-reservist.l4`, tests `ito-il27-tests-s39b.l4` (37) |
| ITO lines 1622, 1624-1626 | s 39B, the lines marked "temporary provision in 2026 and 2027" | encoded under a switch, default declined (fork F2) | same |
| ITO line 1619 | s 39B, commencement (the amending Law of 5786) | needs a source: refuses a tax year before 2026 | same |
| ITO lines 1627-1629 | s 39B(b), "fighter" and "reserve service" (Military Jurisdiction Law 5715-1955, Reserve Service Law 5768-2008) | out-of-scope: the Laws are not in the source bundle; the days of reserve service as a fighter are a fact the caller states | `A combat reservist in a tax year, for section 39B` |
| ITO line 1648 | s 40A | encoded | `ito-s40a-divorcee-remarried.l4`, tests `ito-il27-tests-s40a.l4` (17) |
| ITO line 1651 | s 40B | encoded | `ito-s40b-youth.l4`, tests `ito-il27-tests-s40b.l4` (26) |
| ITO line 1654 | s 40C(a) to (e) | encoded, both texts | `ito-s40c-academic-degree.l4`, tests `ito-il27-tests-s40c.l4` (72) |
| ITO line 1654 | s 40C(f), the definitions "Council Law", "higher education institution", "academic degree" (Council for Higher Education Law 5718-1958) | out-of-scope: the Law is not in the source bundle; entitlement to a degree from a recognised institution is a fact the caller states | `entitled to the degree from a higher education institution` |
| ITO line 1654 | s 40C, studies that ended before 2014 | needs a source: refused | same |
| ITO line 1673 | s 40D(a) to (d) | encoded, both texts | `ito-s40d-professional-studies.l4`, tests `ito-il27-tests-s40d-s40e.l4` (29, with s 40E) |
| ITO line 1673 | s 40D, studies that ended before 2018 | needs a source: refused | same |
| ITO line 1683 | s 40E | encoded | `ito-s40e-no-double-credit.l4`, same tests |
| ITO line 1686 | s 40F | inert: repealed ("פקע") | quoted in `ito-s40e-no-double-credit.l4` |
| ITO line 1689 | s 41(1), (2) | encoded | `ito-s41-spouse-married-part-year.l4`, tests `ito-il27-tests-s41.l4` (16) |
| ITO line 1694 | s 41A (the Director-General's report to the Finance Committee, by 30 June 2019) | inert: an expired reporting duty; no tax computation turns on it | not quoted |
| ITO lines 1697, 1700 | ss 42, 43 | inert: repealed ("בוטל") | not quoted |
| ITO line 1703 | s 44 | encoded | `ito-s44-relative-in-institution.l4`, tests `ito-il27-tests-s44-s45.l4` (36, with s 45) |
| ITO lines 1704-1705 | s 44, the regulations of 5756-1996 and the income ceilings in the consolidation's note | needs a source (the regulations): the caller states whether their conditions are met; the note's figures are recorded, used by no rule | `ito-il27-published-figures.l4` |
| ITO line 1707 | s 45(a), (c) | encoded | `ito-s45-disabled-child.l4`, same tests |
| ITO lines 1709, 1711-1712 | s 45(b) repealed (inert); s 45(d) the Minister's conditions and the regulations of 5756-1996 | (b) inert; (d) needs a source, as s 44 | same |
| ITO line 1744 | s 46(a), (c) | encoded | `ito-s46-donations.l4`, tests `ito-il27-tests-s46.l4` (29) |
| ITO lines 1746-1747, 1750-1751 | s 46(a1), (a2), (d): the Minister's cancelling and renewing a determination of an institution | inert: administrative powers over an institution; whether an institution is one the Minister determined is a fact the caller states by listing only donations to such bodies | not encoded |
| ITO line 1748 | s 46(b) | inert: repealed | not quoted |
| ITO line 1753 | s 46A | encoded | `ito-s46a-overall-ceiling.l4`, tests `ito-il27-tests-s46a-s46b.l4` (23, with s 46B) |
| ITO line 1754 | s 46A, s 20A and the Law of 5744-1983 (the research and development deduction) | out-of-scope: the deduction is an input | `sums deducted for participating in research and development` |
| ITO line 1756 | s 46B, the addition | encoded | `ito-s46b-advance-base.l4`, same tests |
| ITO line 1758 | s 46B, the editorial note on commemorating a fallen soldier (s 4 of the Amendment (No. 2) Law of 5722-1962) | out-of-scope: a summary of another Law that is not in the source bundle | not encoded |
| ITO line 1760 | s 46C | inert: repealed | quoted in `ito-s46b-advance-base.l4` |
| ITO line 1791 | s 47A(a), (b), (b1), (c), (d) | encoded; (c) under a switch (fork F9) | `ito-s47a-national-insurance-deduction.l4`, tests `ito-il27-tests-s47a.l4` (26) |
| ITO line 1795 | s 47A(c), the regulations of 5751-1991 (the bodies) | needs a source: (c) is declined where medical insurance sums were paid | same |
| ITO lines 1585-1588 | s 35(e)(1), (2) | encoded through the rules | `ito-s35e-rules-5738-1977.l4`, tests `ito-il27-tests-s35e.l4` (40) |
| the rules of 5738-1977, line 16 | rule 1, "minor" | encoded | same |
| the rules, lines 19-22 | rule 2 | encoded (fork F10 on the day from which he counts) | same |
| the rules, line 25 | rule 3 | encoded (fork F11 on the 42 and 54 months) | same |
| the rules, lines 28, 31 | rules 4 and 5 | inert: the rules apply from tax year 1975; the name | quoted |
| ITO lines 1788-1789 | s 47(d) | encoded through the Regulations | `ito-s47d-regulations-5740-1980.l4`, tests `ito-il27-tests-s47d.l4` (30) |
| the Regulations of 5740-1980, line 16 | regulation 1, "ceiling of the deduction" | encoded (fork F12) | same |
| the Regulations, lines 19-22 | regulation 2 | encoded (forks F13 considered and found none, F14; the order with s 45A is row IL-08's F35) | same |
| the Regulations, line 25 | regulation 3 | inert: from the 1979 tax year | quoted |
| ITO line 115 | s 1, "retirement age" | encoded by the Law | `retirement-age-law.l4` |
| the Retirement Age Law, line 42 | s 3 | encoded | `retirement-age-law.l4`, tests `ito-il27-tests-retirement-age.l4` (54) |
| the Law, lines 53-55 | s 6(1), (2) and the Schedule's Parts A and B | encoded | same |
| the Law, line 56 | s 6(3) | inert: deleted | not quoted |
| the Law, lines 199-211 | Part B, a woman born before May 1947 | needs a source: the deposited table has no row for her; refused | same |
| the Law, lines 24-25, 27-40 | ss 1, 2 (purpose; "benefit", "agreement", "the Minister") | inert | not quoted |
| the Law, lines 44-48, 58-62, 213-229 | ss 4, 5, 7, 8 and Part C (compulsory and early retirement ages) | out-of-scope: no section of the Ordinance in scope turns on them | not encoded |
| the Law, lines 71-76, 84-85 | ss 10, 12 (the Law prevails over agreements, with exceptions; an age agreed before the Law for a woman, "for her entitlement to retire and to receive a benefit from her employer, and for that purpose only") | out-of-scope: they do not change "the retirement age" the Ordinance means | not encoded |
| the Law, lines 66-67, 78-82, 87-165 | ss 9, 11, 13 to 31 (notices, state aid, budgets, report to the Knesset, indirect amendments) | inert or out-of-scope: administrative, or amendments of other Laws | not encoded |
| the Law, lines 169-177 | ss 32 to 34 (commencement 1 April 2004; National Insurance and health insurance transitional rules) | out-of-scope | not encoded |
| the lead's brief | "Retirement Age Law (s 1 'retirement age', s 37)" | read as ITO s 1 "retirement age" and ITO s 37, which take the Law's retirement age; the Law has 34 sections | `a person has reached the retirement age in or before tax year` |

No row is left "deferred".

## 3. Vendored modules (never edited)

Imports in l4 resolve only beside the importing file, so the minimum of two earlier rows is copied here, byte for byte, and its sha256 is recorded.

| file | from | sha256 |
| --- | --- | --- |
| `ito-credit-points-published-figures.l4` | row IL-01 | `edde7287fffe0bfbf67503771e44c46bed58678e56f3fa8e81c16cc194bf09f8` |
| `ito-il08-nouns.l4` | row IL-08 v0.5.0 | `945359683dab7195eaff9b207f6e75ab47e6cfad481eb8417e3304cfeeb7a0f2` |
| `ito-il08-tax-years.l4` | row IL-08 | `9e686a4dfed2f85b90c4d87c1fa177517d496f1661047d7983f85e10453b2494` |
| `ito-s47a-definitions.l4` | row IL-08 | `4e23063c356b6adbe35c7c6e60a827aa4c266ca98d4b109c46ac1e2d1f94af1d` |
| `ito-s45a-insurance-and-pension-credit.l4` | row IL-08 | `da504d771a1ee880a21575a69b78f0fac0a78befe4717deccc297ba67cb2a70c` |
| `ito-s47-deduction.l4` | row IL-08 | `a6228d39eaaa51eccdf71eebb1bdd9ae765c95cdcdbe11c5bb65196fd5ec9e02` |
| `ito-s35-new-immigrant.l4` | row IL-08 | `6d02395ef64734f3f94e3da74b79f1bd4ad5e824d9b9d25edcf1ce26f2a16b6e` |

IL-08's s 47 and s 45A are used by `ito-s47d-regulations-5740-1980.l4` (the ordinary deduction, the sums the deduction can take, the pension sums s 45A credits, the order reading); IL-08's s 35 fractions of a point by `ito-s35e-rules-5738-1977.l4`; IL-01's published figures by the tests of ss 39A and 39B (the value of a credit point, 2,904 for 2025, the Authority's `itc135-2025` p. 4).
The IL-08 files were copied on 2026-10-08 at the hashes above, which match the originals under `../legalese-2026-10-il-08/` and `../legalese-2026-10-il-01/` at the time of copying.

## 4. Fork register

Every fork is "ruled by Meng 2026-10-08 (SHRUG)": one named switch, default declined (a refusal by name saying the text does not decide) where the readings give different answers, the answer given where they agree, every reading kept by name and tested.
The refusals' wording is the string a test asserts.

| fork | provision | the question | readings (by name) | the default declines when |
| --- | --- | --- | --- | --- |
| F1 | ss 39A, 39B, 40A, 40B | these four sections, unlike ss 34, 40(a), 40(b), 40C, 40D, 44 and 45, name no residence condition. Does a non-resident have the points? | `no residence condition`; `an Israeli resident only`; default `declined where residence decides` | the individual is not an Israeli resident and the points would be positive |
| F2 | s 39B | the lines "temporary provision in 2026 and 2027" sit among paragraphs (1) and (2). Do they replace (1) and (2) in those years, or do (1) and (2) govern throughout? | `the temporary provision replaces paragraphs (1) and (2) in tax years 2026 and 2027`; `paragraphs (1) and (2) govern in every tax year`; default `declined where the readings differ` | the tax year is 2026 or 2027 and the days are 20 or more (they differ at every such number) |
| F3 | s 40A | "גרוש" is masculine and the heading says "another woman", but the body says "בן־זוג" (spouse) of both. Is a divorced woman within it? | `a divorced man only`; `a divorced person of either sex`; default `declined where the individual is a woman` | the individual is a woman who meets the other conditions |
| F4 | s 40B | at what time in the tax year is "has completed 16 years but not 18" measured? | `on the last day of the tax year`; `on some day of the tax year`; `on every day of the tax year`; default `declined where the readings differ` | the three give different answers (one who turns 16 or 18 in the year) |
| F5 | s 40C(d)(1) | a point "in three tax years" and half a point "in two", both "starting" in the year after the studies. Do the runs overlap or does the half point follow? | `the two runs start together`; `the half point follows the point`; default `declined where the readings differ` | the tax year asked about has a different answer under the two |
| F6 | s 41 | a month in which he was married for part is on its face in neither of "the months in which he was not married" and "the months in which he was married" | `a month in which he was married`; `a month in which he was not married`; `a month of neither`; default `declined where the readings differ` | the three give different points (they agree when there is no such month, or when the points are nil) |
| F7 | s 46(a) | "donated a sum exceeding 207": the year's donations together, or each donation? | `the donations of the year together`; `each donation on its own`; default `declined where the readings differ` | some donation does not exceed the minimum and the readings differ |
| F8 | s 46A | when the total passes 50% of taxable income, is the credit's base or the deduction cut? | `the credit is cut first`; `the deduction is cut first`; default `declined where the total passes the ceiling` | the total passes the ceiling |
| F9 | s 47A(c) | (c) is about the Parallel Tax Law, which (d) confines to periods ending 31 December 1996. Does (c) survive for a later year? | `subsection (c) lapses with the Parallel Tax Law` (0); `subsection (c) survives` (refused: its cap, the parallel tax that would have applied, does not exist); default `declined where medical insurance sums were paid` | medical insurance sums were paid |
| F9a | s 47A(b1) | (b1) opens "notwithstanding (a) and (b)": does (a)'s cap, the taxable income before the deduction, survive? | `the cap of subsection (a) applies`; `the cap of subsection (a) does not apply`; default `declined where the cap decides` | a refund was received and 52% of the net contributions exceeds the taxable income |
| F10 | the rules of 5738-1977, rule 2 | one "treated as an immigrant": from which day does the credit period count? | `the day he returned to Israel`; `the day he first became an immigrant` (only where he was one); default `declined` | always |
| F11 | the rules, rule 3 | rule 3 leaves out periods from "the 42 months"; s 35(c) now says 54 for one who first became an immigrant from 2022. Does rule 3 reach the 54? | `rule 3 reaches the 54 months as well`; `rule 3 reaches only the 42 months`; default `declined where the readings differ` | the text of Amendment 262 governs (the day he counts from is 1 January 2022 or later) and a period left out changes the points |
| F12 | the Regulations, regulation 1 | "the ceiling of the deduction" is the product of "the rates fixed as a deduction in s 47(b)(1) or (b)(2)" and the qualifying-income ceiling. For (b)(1) are those the first rate (7%) or every rate (7% and the further 4%, so 11%)? | `the first rate of the paragraph`; `every rate of the paragraph`; default `declined where the readings differ` | the enlarged deduction under (b)(1) passes 7% of the paragraph (2) amount (11,508 for 2026) |
| F13 | the Regulations, regulation 2(b) | "7.5% of the qualifying income to which s 47(b)(2) applies": does the 7.5% replace the 5% in both limbs of (b)(2), or in the first only? | considered, no switch: on row IL-08's definitions (insured income taken into the qualifying work income first, its fork F6) the second limb's income is never the lower, so the readings never differ | never |
| F14 | the Regulations, regulation 2 | "the rate of deduction under s 47(b) shall be …": does the rate replace s 47(b)'s, or has the individual the higher of the two ("enlarged deduction")? | `the regulation replaces the rate of section 47(b)`; `the individual has the higher of the two`; default `declined where the readings differ` | the enlarged deduction is lower than s 47(b)'s (an individual who paid more than 12% and not for a pension only) |
| F15 | s 45(a) | the points are "in his computation or his spouse's": how are they divided? | the record says whose computation takes them: `the individual's`, `the spouse's`, `not stated` | `not stated`, he has a spouse, and the points are positive |
| F16 | s 46(a) | the year's ceiling and the sums carried in from the three earlier years: which does it take first? | not a switch: the credit for the year does not depend on it (it is the lesser of everything available and the ceiling), so it is answered; what remains to carry is answered only where nothing can lapse | a sum carried in from three tax years earlier remains after the ceiling |

Texts that license each reading are quoted on the `src:` lines beside each rule.
IL-08's forks F6 (insured income first), F35 (the order of the s 47 deduction and the s 45A credit) and F1 (s 45A) are used unchanged: where they decide, the rule declines in IL-08's words.

## 5. Assumptions (assumed, not ruled)

- A1. A tax year before 2024 is refused, as in rows IL-01 to IL-08: the text of these sections before the amendments the consolidation shows is not verified. The last amendment each section shows is in `ito-il27-tax-years.l4`.
- A2. A tax year after 2026 is answered on the text as it stood on 2026-10-06, a projection.
- A3. "In the years 2026 and 2027" (s 39B) are the tax years, since the section speaks "לשנת המס".
- A4. "For each five additional days" (s 39B) is each complete block of five days.
- A5. The s 40E election is carried in each tax year's computation ("בחישוב המס שלו"); nothing keeps it the same from year to year.
- A6. In regulation 1 "as the case may be" pairs s 47(b)(1) with the s 47(a)(1) paragraph (2) amount (the ceiling for income that is not work income) and s 47(b)(2) with the paragraph (1) amount.
- A7. "שמלאו לו בתחילת שנת המס 50 שנה" is 50 completed years on 1 January of the tax year; a birthday on 1 January counts.
- A8. The first text of s 40C is read for studies that ended in 2023 or later, the second for 2014 to 2022, and nothing for earlier years; s 40D: 2023 or later, 2018 to 2022, nothing earlier. The consolidation's notes say to whom the second text applies; that the first applies to the rest is an inference.
- A9. A month is a calendar month. s 39A: the month of discharge is not among the 36 months and a tax year is the calendar year.
- A10. s 40A: "pays maintenance" is read as in the tax year; the facts (divorcee, maintenance, married to another spouse) are the caller's.
- A11. ss 44 and 45: the sums and the children are totals the caller has already restricted to qualifying relatives ("totally paralysed, permanently bedridden, blind or insane", child with an intellectual-developmental disability); the points of s 45 are whole-year points, no proration by month.
- A12. s 46: the body-of-persons rate is the s 126(a) rate (23% in the text retrieved), an input. The institution being one the Minister determined is a fact the caller states by listing only such donations.
- A13. s 47A: the Parallel Tax Law applies to no tax year from 1997 (s 47A(d)), so for the years this row answers (a) and (b) are about National Insurance contributions alone; (b1) applies from tax year 2025 ("יחול ... החל משנת המס 2025"), and in 2024 a refund is not looked at.
- A14. s 35(e): periods left out under rule 3 do not overlap, and a period that began before the month he counts from is clipped to it. The s 35(c) absence of row IL-08 is entered as a period too.
- A15. The Regulations' "sum he paid" in (a)(2) is the total paid under s 47(b); a beneficiary member is under s 47(b1), which the Regulations do not touch. The flag `within a class for which regulations under section 47(d) set higher deductions` of row IL-08's record is not read; the date of birth decides.
- A16. The Retirement Age Law: a person born in calendar month b reaches an age of n months in month b + n; "reached in or before a tax year" means reached in a month not after December of it (row IL-08 F20).

## 6. Answer table

Each cell is a test (module in parentheses); the arithmetic is in the comment beside it.

| question | answer | where |
| --- | --- | --- |
| s 39A: a man, 24 months of service, discharged March 2025, tax year 2026 | 12 months x 1/6 = 2 points | `ito-il27-tests-s39a.l4` |
| the same, tax year 2025 / 2028 | April to December 9 x 1/6 = 1.5 / January to March 3 x 1/6 = 0.5 | same |
| s 39A: a man who served 22 months; a woman who served 22; a woman who served 21 | 1/12 a month (1 point in a full year); 1/6 (2); 1/12 (1) | same |
| s 39B: 40 days, tax year 2028 | 3/4 + 4/4 = 7/4 | `ito-il27-tests-s39b.l4` |
| s 39B: 85 days; 100 days | 4 (3/4 + 13/4); 4 (held to 4) | same |
| s 39B: 40 days in 2026 | declined (replace reading 3/4; paragraphs (1)-(2) 7/4) | same |
| s 40A: a divorced man meeting all three conditions | 1 | `ito-il27-tests-s40a.l4` |
| s 40B: born 15 June 2009, tax year 2026 | 1 (all three readings) | `ito-il27-tests-s40b.l4` |
| s 40B: born 15 June 2010, tax year 2026 | declined (last day 1, some day 1, every day 0) | same |
| s 40C: a first degree of 3 years, ended 2023 | 1 point in 2024, 2025, 2026; 0 in 2027 | `ito-il27-tests-s40c.l4` |
| s 40C: a second degree of 2 years, ended 2023 | 1/2 in 2024 and 2025 | same |
| s 40C: a third degree in medicine, ended 2023, 2026 | 1 (the readings agree); 2024 and 2025 declined (3/2 or 1) | same |
| s 40D: 1,700 hours, 3 years, ended 2023 | 1 in 2024 to 2026 | `ito-il27-tests-s40d-s40e.l4` |
| s 40E: a second degree (1/2) and vocational studies (1), no choice | declined | same |
| s 41: 5 months not married, 7 married, points 3 and 6 | (5 x 3 + 7 x 6)/12 = 19/4 | `ito-il27-tests-s41.l4` |
| s 44: paid 60,000, taxable income 200,000, conditions met | 35% x (60,000 - 25,000) = 12,250 | `ito-il27-tests-s44-s45.l4` |
| s 45: one paralysed child | 2 points | same |
| s 46: an individual donating 1,000, income 200,000 | 35% x 1,000 = 350 | `ito-il27-tests-s46.l4` |
| s 46: donating 20,000,000, income 100,000,000 | 35% x 10,354,816 = 3,624,185.6 | same |
| s 46A: credit sums 60,000 and deduction 50,000, income 200,000 | total 110,000 over 100,000: declined | `ito-il27-tests-s46a-s46b.l4` |
| s 46B: base 10,000, relief 3,500 | 13,500 | same |
| s 47A: 20,000 contributions on other income, income 300,000 | 52% x 20,000 = 10,400 | `ito-il27-tests-s47a.l4` |
| s 47A: 2026, 20,000 paid, 4,000 refunded | 52% x 16,000 = 8,320 | same |
| s 47A: 2026, 3,000 paid, 5,000 refunded | 0 deducted; 52% x 2,000 = 1,040 business income | same |
| s 35(e) rule 3: counting from 15 July 2021, a year of service in 2022, tax year 2024 | 12 months at places 19 to 30, 1/6 each = 2 | `ito-il27-tests-s35e.l4` |
| rule 2(3): left at 17, returned exactly five years later | treated as an immigrant | same |
| s 47(d): 100,000 non-work income, 14,000 paid for a pension only, aged 56 | 10,500 | `ito-il27-tests-s47d.l4` |
| s 47(d): the same, 20,000 paid | declined (F12: 11,508 or 15,000) | same |
| s 47(d): an employee on 100,000, none insured, 6,000 paid, aged 56 | 5,820 (7.5% x 100,000 = 7,500 held to 5% x 116,400) | same |
| Retirement Age Law: a man born June 1990 / a woman born June 1990 | 804 / 780 months | `ito-il27-tests-retirement-age.l4` |
| a woman born December 1969 / January 1970 | 777 / 780 months; reaches it September 2034 / January 2035 | same |
| a woman born April 1947 | refused: Part B has no row for her | same |

## 7. Published figures and provenance

`ito-il27-published-figures.l4` carries, from the consolidation's own square-bracket notes (the deposited Ordinance, sha256 `b87f2cf4…94b81b6`, an aid and not law): the amounts of s 46(a) for 2024 to 2027 (207 and 10,354,816; line 1745) and the income ceilings the note gives for the regulations of 5756-1996 (182,000 and 291,000 for 2023; 188,000 and 301,000 for 2024 to 2027; lines 1705 and 1712).
The s 46 amounts are used by the tests as the amounts in force; nothing used the income ceilings, which belong to regulations that are not in the source bundle.
No other source for the s 46 amounts was fetched (the brief forbids fetching), and rows IL-01 and IL-03 do not carry them.
The value of a credit point is row IL-01's published figure (2,904 for 2025, `itc135-2025` p. 4); the tests use it for 2025 only and the rule takes the value as an argument.

## 8. What `check.sh` prints

See section 14, written from the run.

## 9. Needs a source (refused by name, not guessed)

- The commencement of s 39B, in an amending Law of 5786 (the Economic Efficiency Law of 5786, Sefer HaChukim 3511, deposited, does not touch s 39B). Needed: the Law, to answer a tax year before 2026 and to settle fork F2.
- The text of s 40C for studies that ended before 2014 and of s 40D for studies that ended before 2018.
- The Income Tax (Credit for a Disabled Person and Credit for Expenses of Keeping a Relative in an Institution) Regulations, 5756-1996 (the title the consolidation's note gives), for ss 44 and 45.
- The Income Tax (Determination of Bodies for s 47A) Regulations, 5751-1991 (the title the consolidation's note gives), for s 47A(c).
- Part B of the Retirement Age Law's Schedule for a woman born before May 1947: the Knesset text (Sefer HaChukim 5764 p. 150). Part B as deposited has no row for her.
- The Discharged Soldiers Absorption Law of 5754-1994, the Military Jurisdiction Law of 5715-1955, the Reserve Service Law of 5768-2008 and the Council for Higher Education Law of 5718-1958, whose definitions the caller states as facts.
- The foreign-worker regulations of 5775-2014 are deposited but not encoded by any row; this row, like rows IL-01 and IL-08, refuses the credits a foreign worker would have (s 48A).

## 10. Inputs the capstone does not supply today (for IL-55)

Row IL-07 does not call any of this row's rules.
To call them it would have to supply, per section:

- ss 39A, 39B, 40A, 40B: the sex; whether the individual is an Israeli resident in the tax year; for s 39A, whether he is a discharged soldier within the Law, his full months of regular service and the calendar month and year he ended it; for s 39B, the days of reserve service as a fighter in the previous tax year; for s 40A, whether he is a divorcee, whether he or his spouse paid maintenance to the former spouse in the year, and whether he is married to a spouse other than the former one; for s 40B, dates of birth of the individual and of the spouse.
- ss 40C, 40D, 40E: for each set of studies, the kind, entitlement, the years of study, the tax year the studies ended, proof given to the assessing officer, any internship (years it began and ended), the elections, the 40E choice, the hours of vocational study.
- s 41: months married, not married and married for part of the year; the whole-year points under ss 34, 36, 40(b), 40B (rows IL-01, IL-08 and this row) and under s 66 (row IL-02).
- ss 44, 45: the sums paid to keep qualifying relatives in an institution, the taxable income, the children with their conditions, whose computation takes the points, and whether the conditions of the regulations of 5756-1996 are met.
- ss 46, 46A, 46B: the donations (a list), the sums carried in, the taxable income, the s 126(a) rate for a body of persons, the sums deducted for research and development, the tax relieved, the base for advance payments; the amounts of s 46 for the year.
- s 47A: the contributions paid, the s 179(a) addition they include, any refund received, the taxable income before the deduction, any medical insurance sums.
- s 35(e): the facts of rule 2 (dates of birth, of becoming an immigrant, of leaving and returning, the months stayed, exemptions received), the periods of service and study to leave out, and the readings.
- s 47(d): the date of birth and whether the sums were paid for a pension only, with row IL-08's record.
- The Retirement Age Law: sex and the calendar year and month of birth.
- For every credit, the value of a credit point for the tax year (row IL-01; row IL-03 for later years).

## 11. What the capstone would need

- To call `a person has reached the retirement age in or before tax year` in place of the input row IL-08 takes for s 37 (its fork F20).
- Row IL-08's s 35 to call `the credit points under section 35 with rule 3 for` where the immigrant has periods left out, or has been treated as an immigrant under rule 2; row IL-08's s 35 still refuses both.
- Row IL-08's s 47 to call `the deduction under section 47 with the Regulations of 5740-1980 for` for one aged 50 or more; row IL-08's still refuses `within a class for which regulations under section 47(d) set higher deductions`.
- The credits of this row to be summed with the credits of rows IL-01, IL-02 and IL-08 under s 120B's value of a credit point, and each credit's own tax base respected (s 39A's and s 40(b)(1A)'s credits are set against the tax on income from personal exertion).

## 12. Nouns to reconcile with other rows

- `tax year`, `an Israeli resident in the tax year` and `a foreign worker` are spelled as rows IL-01 and IL-08 spell them.
- `A person's sex, for these sections` (a man, a woman) is new to this row; row IL-01 has a `Sex`-like type under its own names (not vendored).
- `A discharged soldier`, `A combat reservist`, `A divorced individual`, `An individual and a spouse, for section 40B` and the others are new; none redeclares a type of another row.
- `A run of credit points` (points, first tax year, number of tax years) is this row's and could serve any credit that runs over several years.

## 13. Open questions for a domain expert

1. s 39B: how do the lines marked "temporary provision in 2026 and 2027" relate to paragraphs (1) and (2), and when does the section commence? As printed, the temporary lines give less than (1) and (2) at every number of days.
2. s 40A: is a divorced woman within it?
3. s 40B: at what time of the tax year is the age measured?
4. s 40C(d)(1): do the point and the half point run together?
5. s 44, s 45: what do the regulations of 5756-1996 require, and what does the income ceiling in the consolidation's note limit?
6. s 46: is the minimum on the year's donations together or on each? Which sums does the ceiling take first?
7. s 47A(c): does it survive 1996? s 47A(b1): does the cap survive?
8. Regulation 1 of 5740-1980: is the ceiling the first rate or every rate? Does the regulation replace s 47(b) or add to it?
9. Rule 2 of 5738-1977: from which day does one treated as an immigrant count, and which text of s 35(a) governs him?

## 14. `check.sh`

Run from 2026-10-08T23:12:20Z to 23:13:05Z as `L4=/Users/mengwong/.local/bin/l4 ./check.sh`, `JL4_LIBRARY_PATH` unset.
The binary `~/.local/bin/l4` is the cabal store's `jl4-0.1-6df1397b`, 233,724,416 bytes, sha256 `f0759b2ef2f1d1b2a577c68f059c54f487de9d913553fc9f0d9bf0f7f5dab0d8` before and after; no module changed during the run.
The first run (2026-10-08T23:07:45Z to 23:08:20Z, the same sha256 before and after, before the editorial changes to fork numbers and the NOTES) gave the same 463 satisfied.
Each satisfied assertion logs "assertion satisfied" twice; `check.sh` counts assertions.

```
module                                    errors satisfied  failed  refused  expected
ito-credit-points-published-figures.l4         0         0       0        0         0
ito-il08-nouns.l4                              0         0       0        0         0
ito-il08-tax-years.l4                          0         0       0        0         0
ito-il27-nouns.l4                              0         0       0        0         0
ito-il27-published-figures.l4                  0         0       0        0         0
ito-il27-tax-years.l4                          0         0       0        0         0
ito-il27-tests-retirement-age.l4               0        54       0        0         0
ito-il27-tests-s35e.l4                         0        40       0        0         0
ito-il27-tests-s39a.l4                         0        28       0        0         0
ito-il27-tests-s39b.l4                         0        37       0        0         0
ito-il27-tests-s40a.l4                         0        17       0        0         0
ito-il27-tests-s40b.l4                         0        26       0        0         0
ito-il27-tests-s40c.l4                         0        72       0        0         0
ito-il27-tests-s40d-s40e.l4                    0        29       0        0         0
ito-il27-tests-s41.l4                          0        16       0        0         0
ito-il27-tests-s44-s45.l4                      0        36       0        0         0
ito-il27-tests-s46.l4                          0        29       0        0         0
ito-il27-tests-s46a-s46b.l4                    0        23       0        0         0
ito-il27-tests-s47a.l4                         0        26       0        0         0
ito-il27-tests-s47d.l4                         0        30       0        0         0
ito-s35-new-immigrant.l4                       0         0       0        0         0
ito-s35e-rules-5738-1977.l4                    0         0       0        0         0
ito-s39a-discharged-soldier.l4                 0         0       0        0         0
ito-s39b-combat-reservist.l4                   0         0       0        0         0
ito-s40a-divorcee-remarried.l4                 0         0       0        0         0
ito-s40b-youth.l4                              0         0       0        0         0
ito-s40c-academic-degree.l4                    0         0       0        0         0
ito-s40d-professional-studies.l4               0         0       0        0         0
ito-s40e-no-double-credit.l4                   0         0       0        0         0
ito-s41-spouse-married-part-year.l4            0         0       0        0         0
ito-s44-relative-in-institution.l4             0         0       0        0         0
ito-s45-disabled-child.l4                      0         0       0        0         0
ito-s45a-insurance-and-pension-credit.l4       0         0       0        0         0
ito-s46-donations.l4                           0         0       0        0         0
ito-s46a-overall-ceiling.l4                    0         0       0        0         0
ito-s46b-advance-base.l4                       0         0       0        0         0
ito-s47-deduction.l4                           0         0       0        0         0
ito-s47a-definitions.l4                        0         0       0        0         0
ito-s47a-national-insurance-deduction.l4       0         0       0        0         0
ito-s47d-regulations-5740-1980.l4              0         0       0        0         0
retirement-age-law.l4                          0         0       0        0         0
TOTAL (41 modules)                             0       463       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

`check.sh` exit 0.
There are no expected failures and no expected refusals: this row declares none.
The row's own fourteen test modules hold 463 assertions, all satisfied, 78 of them `#ASSERT REFUSED … BECAUSE "…"` (a refusal by name, with the exact string asserted).
Per module: retirement age 54 (3 refused), s 35(e) 40 (5), s 39A 28 (3), s 39B 37 (8), s 40A 17 (4), s 40B 26 (8), s 40C 72 (10), ss 40D and 40E 29 (5), s 41 16 (6), ss 44 and 45 36 (8), s 46 29 (5), ss 46A and 46B 23 (4), s 47A 26 (4), s 47(d) 30 (5).
No expected value was changed after a run. Every one was worked by hand before the run, and no assertion failed once its module compiled; several test modules first needed syntax repairs (an argument order that did not match the mixfix name, a date written without the parentheses l4 needs, a copy of a record built with `WITH`, which l4 does not support), none of which touched an expected value.

## 15. Version 0.1.1 (2026-10-09): the independent pass, and the over-declines repaired

The independent test author (fid-il-27) wrote `DECIDED-ANSWERS.md` from the Hebrew alone, then `tests-independent.l4` (237 cases), and `INDEPENDENT-FINDINGS.md`.
Its three OURS-WRONG findings were one defect: a default that declined where the readings agree, against the SHRUG rule that a default declines only where they differ.
Repaired, each default now computes the answer under every reading (or every choice) and declines only if they differ:

- E20, s 39B: the default for tax years 2026 and 2027 compares paragraphs (1) and (2) with the temporary provision from 30 days; 200 days (and 110 days) give 4 under both and are answered; 109 and 100 days still differ and decline; 20 to 29 days still decline (the temporary provision is silent).
- F39, s 40C(e): for each of the first and second degrees every choice of "the one" is tried; the same points under all choices is the answer (two identical first degrees give 1 in 2026), different points decline as before.
- F52, s 40E: one who meets both and states no election has the points if the two elections give the same (1 and 1: 1; 0 and 0 in 2027: 0); different points (1/2 against 1) still decline.

I searched the rest of the defaults for a refusal fired without comparing readings and found one more, repaired the same way:

- s 46A, fork F8: the default declined whenever the total passed the ceiling. Both cuts give the same credit base and deduction when only one of the two is present (a credit of 130,000 alone: 100,000 and 0; a deduction of 120,000 alone: 0 and 100,000); these are now answered, and the mixed case (60,000 and 50,000) still declines.

Checked and already comparing: F1, F3 (a woman with nil points answers), F4, F5, F6, F7, F9a, F11, F12, F14, F15, F16.
Not comparing by design: F2's temporary provision for 20 to 29 days; F9 (the two readings give 0 and a refusal); F10 (the rule gives no day).
New assertions: 4 in the s 39B tests, 4 in s 40C, 2 in ss 40D/40E, 4 in ss 46A/46B (14); every expected value was worked by hand first.
`check.sh`: `tests-independent.l4` now has 226 satisfied, 3 failed, 8 refused; its declared refusals dropped from 11 to 8 (the three repaired cases now pass), commented in `check.sh`; exit 0. l4 sha256 before and after `f0759b2ef2f1d1b2a577c68f059c54f487de9d913553fc9f0d9bf0f7f5dab0d8`.

The tester's other findings, as they stand:

- I07 TESTER-WRONG: 25,000 donated and 10,000 carried in against a 30,000 ceiling is 10,500, whichever is taken first (F16); the declared failure stands.
- Declared failures H07 (SCOPE: the ceiling of the regulations of 5756-1996 is a caller input) and J11 (AMBIGUITY: 16% of 165,228 is 26,436.48, while the note prints 26,436) stand.
- Ambiguities: E12 (s 39B reading T, 29 days: the encoding's refusal is the better answer); F23 (s 40B born 15 June 2010 at the default declines, F4); G07 (s 41 registered spouse: a refusal where the tester expected 0, same substance); J11 above.
- Scope, not encoded by this row: s 39 (the helping spouse) and s 40(b) (single-parent child points) have no module here (rows IL-08 and the capstone take them); s 35(b), the returning-resident definition and the "first time only" rule of s 35(c); s 41(2)'s s 66 points (an input); the couple/single ceilings and relatives of ss 44 and 45 (inputs); s 46's recognition of institutions and the company rate (inputs); s 47A(c), (d); the Retirement Age Law's compulsory and early ages (ss 4, 5, 7, 8, 10, 12, Part C); tax years before 2024 (A17, A18, F47, F48, refused by A1).
- Thinly covered by the independent pass: ss 40A (4 cases, none for a woman), 40E, 45, 46A/46B, rules 2 and 3; not at all: ss 39 and 40(b).
