# Independent expectations: Child Development Co-Savings Act 2001

Written from `BRIEF.md` and `../source/CDCSA2001.txt` alone, before any `.l4` file was opened.
These values are fixed. `tests-independent.l4` asserts them, and the expected values are never
changed to match the encoding.

Conventions:
- "WI" is the weekly index.
- "per-period cap" means "$X for every period equal to k x WI or 6k days, whichever is lower".
- Money is in dollars. Pay is gross pay per week of WI work days unless stated otherwise.
- Where the Act is open to doubt, the expectation is marked **(doubt)** and the reason is given.

## Goal 1: common measures (s 2, First Schedule)

### April 2025 Scheme child (s 2(1))
- E1. Born alive, confinement 2025-04-01, EDD 2025-04-01: **is** an April 2025 Scheme child (para (a)).
- E2. Born alive, confinement 2025-03-31, EDD 2025-03-31: **not** an April 2025 Scheme child.
- E3. Born alive, confinement 2025-03-20, EDD 2025-04-01: **is** one (confinement before, EDD on or after).
- E4. Born alive, confinement 2025-03-20, EDD 2025-03-31: **not** one.
- E5. Stillborn, confinement 2025-05-01: **not** one, because para (a) needs "a child born alive".
- E6. Adoption, eligibility date 2025-04-01: **is** one (para (b)). Eligibility date 2025-03-31: **not** one.

### January 2024 Scheme child (s 2(1))
- E7. Born alive, confinement 2024-01-01: **is** one.
- E8. Born alive, confinement 2023-12-31, EDD 2023-12-31: **not** one.
- E9. Born alive, confinement 2023-12-20, EDD 2024-01-05: **is** one.
- E10. Adoption, eligibility date 2023-12-31: **not** one. Eligibility date 2024-01-01: **is** one.

### Eligibility date (s 2(1))
- E11. Child is a citizen or PR; application made 2025-05-10; pass issued 2025-06-01: the eligibility date is **2025-05-10**.
- E12. Child is neither a citizen nor a PR; application made 2025-05-10; pass issued 2025-06-01: the eligibility date is **2025-06-01**.

### Specified event number (s 2(2))
- E13. Relevant event 2021-10-31. One previous confinement, whose only child is dead. The previous event is disregarded, so this is the **1st** specified event (s 2(2)(a)(i)).
- E14. Relevant event 2021-11-01. One previous confinement, whose only child is dead. Under (aa) only adoption by another person disregards an event, so this is the **2nd** specified event.
- E15. Relevant event 2022-03-01. One previous event, whose only child has been adopted by another person (not jointly): disregarded, so this is the **1st** (s 2(2)(aa)).
- E16. Relevant event 2020-05-01. One previous confinement of a stillborn child: disregarded, so this is the **1st** (s 2(2)(a)(i)).
- E17. Relevant event 2020-05-01. One previous confinement of twins, one dead and one alive. "Each child" is not dead, so the event counts and this is the **2nd**.
- E18. Any date. A previous adoption application that was withdrawn or refused is disregarded (s 2(2)(b)). With that as the only previous event, this is the **1st**.
- E19. Two previous events, both counted: this is the **3rd** (the third-or-subsequent tier).

### Age (s 2(2A))
- E20. Born 2020-02-29: the person attains 1 year on **2021-02-28**, so they are below 1 on 2021-02-27 and not below 1 on 2021-02-28.
- E21. Born 2018-06-15: they are below 7 on 2025-06-14 and not below 7 on 2025-06-15.

### Weekly index (First Schedule)
- E22. Same number of work days every week (5): WI = **5** (item 1).
- E23. Five full days plus one day of 5 hours or less: WI = **5.5** (note 3 makes that day a half day).
- E24. A regular pattern with T = 11 over W = 2 weeks: WI = **5.5** (item 2, T/W).
- E25. No regular pattern, with T = 16 over the 3 preceding weeks: WI = **16/3, about 5.333** (item 3, T/3).
- E26. Seven work days every week: WI = **6** (note 3A caps it at 6).
- E27. No regular pattern, with T = 21 over 3 weeks: WI = **6** (7 is capped to 6).

### Durations of k x WI or 6k days (note 5)
- E28. 4 x WI with WI = 16/3: 21.333 is rounded down to **21** (the nearest half or whole day below), lower than 24, so **21**.
- E29. 4 x WI with WI = 17/3: 22.667 is rounded down to **22.5**, so **22.5**.
- E30. 8 x WI with WI = 5.5: **44** (lower than 48).
- E31. 4 x WI with WI = 6: **24**.
- E32. 2 x WI with WI = 5: **10** (lower than 12).

## Goal 2: the Co-Savings Scheme (Part 2)
- E33. Co-savings arrangement (s 3(3)): when a parent contributes $3,000, the Government contribution is **equal: $3,000**.
- E34. The maximum penalty under the scheme regulations (s 3(2)(j)) is a **fine of $20,000** and **12 months**.
- E35. On a member's death (s 6(1)), the moneys go to the Public Trustee. For a non-Muslim they are disposed of under the **Intestate Succession Act 1967**. For a Muslim they are disposed of under **s 112 of the Administration of Muslim Law Act 1966**.
- E36. Trustee substitution (s 4(1)(e)): when the trustee is dead, they are replaced by the **personal representative**. If the member has a legal guardian, the replacement is the **legal guardian** instead (s 4(1)(da)).
- E37. Recovery under s 8(1)(h), from a parent who is not in default, is available **only if** the Government cannot recover under (d) or (g) and cannot deduct under (e) or (f).

## Goal 3: maternity (ss 9, 9A, 10)

### Eligibility under s 9A(1)
- E38. Child is a citizen, confinement 2016-12-31, EDD 2016-12-31: **not eligible**.
- E39. Child is a citizen, confinement 2017-01-01: **eligible**, given the 3 months' service.
- E40. Confinement 2016-12-20, EDD 2017-01-03: **eligible** (the EDD is on or after 1 January 2017).
- E41. Stillborn child, confinement 2021-10-31, EDD 2021-10-31: **not eligible**.
- E42. Stillborn child, confinement 2021-11-01: **eligible**.
- E43. Stillborn child, confinement 2021-10-20, EDD 2021-11-05: **eligible** (the EDD is on or after 1 November 2021).
- E44. Child is not a citizen at birth: **not eligible** under 9A(1).
- E45. The employee has served 2 months before confinement: **not eligible** under 9A(1)(c).

### Eligibility under s 9A(1A)
- E46. Child is not a citizen at birth (born 2024-05-01) and becomes a citizen on 2025-04-30: **eligible**. Becoming a citizen on 2025-05-01 is **outside** the 12 months that start on the date of birth, so **not eligible**.

### Government-paid benefit, s 9A(2)
- E47. Employed for 90 days in the aggregate in the 12 months before confinement: **eligible**. 89 days: **not eligible**.
- E48. Stillborn child, confinement 2021-10-31: **not eligible** (for a stillborn child the date must be on or after 1 November 2021).

### Leave length (s 9(1))
- E49. Total maternity leave is **16 weeks** (4 + 12, or 16, or 8 plus 8 x WI/48 days). The flexible part, at WI 5, is **40 days**.

### Employer payment caps, s 9A(4) (pay $3,000 a week, WI 5, 16 weeks taken)
- E50. 1st or 2nd event: weeks 1 to 8 are uncapped ($24,000). Weeks 9 to 16 are two 20-day periods of $12,000 each, each capped at $10,000. Total employer payment **$44,000**.
- E51. 3rd or later event: every 20-day period is capped at $10,000, so four periods give **$40,000** (the total cap is also $40,000).
- E52. 1st event at $1,000 a week: **$16,000** (no cap bites).

### Reimbursement, s 10(1)-(2)
- E53. 1st or 2nd event, $3,000 a week, 16 weeks: the reimbursement covers only the period after the first 8 weeks and is capped at **$20,000**.
- E54. 3rd event, $3,000 a week, 16 weeks: **$40,000**.
- E55. 1st event, $1,000 a week: **$8,000** (8 weeks x $1,000).
- E56. A payment the employer was directed to make on or after 2017-01-01 (by the MOM, the Commissioner or a court) is **not reimbursable**, unless the direction was withdrawn or reversed (s 10(3)).
- E57. Discretionary reimbursement (s 10(2A)-(2B)) is available for a confinement on or after 2021-11-01 where the employee lacks the 3 months' service. Confinement 2021-10-31 (EDD same day): **not available**.

### Self-employed, ss 9(5), 9A(5) (lost income $3,000 a week, WI 5, 16 weeks)
- E58. 1st or 2nd event: the Government pays only after the first 8 weeks, capped at **$20,000**.
- E59. 3rd event: the Government pays for the whole period, capped at **$40,000**.

### Government-paid maternity benefit, ss 9(5A), 9A(5A)
- E60. 1st or 2nd event at $200 a day: 56 x 200 = **$11,200** (the cap of $10,000 per 28 days does not bite, since 28 x 200 = 5,600).
- E61. 1st event at $500 a day: 56 days, with 28 x 500 = 14,000 capped at 10,000, so **$20,000**.
- E62. 3rd event at $500 a day: 112 days, so **$40,000**.
- E63. 3rd event at $200 a day: **$22,400**.

### Disqualification, s 9(6)-(6B)
- E64. Also entitled to employer-paid leave under s 9(1) for the same confinement: **disqualified**, even if she has forfeited it.
- E65. As E64, but on no-pay leave at her own request for a continuous period ending at least 12 months after delivery: **not disqualified** (s 9(6A)).
- E66. Would have been entitled under 9(1) but her contract of service was completed, or she was made redundant: **not disqualified** (s 9(6B)).
- E67. Entitled under 9(1) and resigned (so forfeited under 9(2A)): **still disqualified** (6B covers only contract completion and redundancy).
- E68. A self-employed woman entitled to lost income under 9(4): **disqualified** (9(6)(b)).

### s 9(1A) outcomes (child becomes a citizen after birth)
The specified period is the 12-week period under EA s 76(1)(a)(ii), counted from day 1.
- E69. EA 76(1)(a), 1st event, child a citizen on day 20 of the specified period (within its first 4 weeks): paid for the **last 4 weeks** of the specified period plus a **further 4 weeks** (i)(A).
- E70. As E69, but a citizen on day 29 (after the first 4 weeks, within the period): paid **from the citizenship day to the end** of the period plus a **further 4 weeks** (i)(B).
- E71. As E69, but a citizen within 4 weeks after the period ends: a **further 4 weeks from the citizenship day** (i)(C).
- E72. 3rd event, EA 76(1)(a), citizen within the specified period: **from citizenship to the end** plus a **further 4 weeks** ((ii)(A)). The first-4-weeks split of the 1st and 2nd tier does **not** apply.
- E73. A citizen after the 16 weeks but within 12 months of confinement: a **further 4 weeks** (iva).

### Once per confinement (s 9A(5B))
- E74. Twins: **one** entitlement (16 weeks, not 32).

## Goal 4: adoption (ss 12A-12AD)
- E75. 12AC(1): eligibility date 2016-12-31: **not eligible**. 2017-01-01: **eligible**.
- E76. Child born 2024-03-01, eligibility date 2025-02-28: the child is below 12 months, so **eligible**. Eligibility date 2025-03-01: **not** below 12 months, so **not eligible**.
- E77. The adoptive mother is the child's natural mother: **not eligible** (12AC(1)(f)).
- E78. The child is a PR and the application is in her sole name: she must be a citizen on the application date, otherwise **not eligible**. Joint application where only the husband is a citizen: **eligible** (12AC(1)(da)).
- E79. Adoption leave is **12 weeks** (12AA(1)(a)).
- E80. 12AA(5), $3,000 a week, WI 5, 12 weeks, 1st event: first 4 weeks uncapped ($12,000), then two periods capped at $10,000 each, so employer payment **$32,000**.
- E81. 12AA(5), 3rd event, same facts: three periods of $12,000, each capped at $10,000, so **$30,000** (the total cap is $30,000).
- E82. 12AD reimbursement, 1st event: **$20,000**. 3rd event: **$30,000**.
- E83. 12AD reimbursement, 1st event, $1,000 a week: 8 weeks after the first 4, so **$8,000**.
- E84. 12AB self-employed, 1st event, $3,000 a week: **$20,000**. 3rd: **$30,000**.
- E85. 12A amount, 1st or 2nd event at $500 a day: 56 days capped at $10,000 per 28, so **$20,000**. 3rd at $500: 84 days, so **$30,000**. 1st at $100: **$5,600**.
- E86. 12AC(2): eligibility date 2020-12-31: **not eligible**. 2021-01-01 with 90 days' work: **eligible**. 89 days: **not**.
- E87. 12A(5): also entitled to 12AA leave: **disqualified**. Contract completion (12A(7)): **not disqualified**.
- E88. 12AD(4) discretionary: eligibility date 2021-10-31: **not available**. 2021-11-01: **available**.

## Goal 5: fathers (ss 12H-12JA)
- E89. Employee father of an April 2025 Scheme child: **4 weeks** of paternity leave (12H(1)(a)(i)). Father of any other child: **2 weeks**.
- E90. Flexible paternity leave, WI 5: April 2025 child **20 days** (4 x 5, lower than 24). Other child: **10 days**.
- E91. Self-employed father (12H(4)) of a January 2024 Scheme child born 2024-06-01 (not an April 2025 child), WI 5: **20 days**. The employee father of the same child gets the 2-week tier, **10 days**.
- E92. 12I(3) employer payment cap: April 2025 child, $3,000 a week, 4 weeks: each week capped at $2,500, so **$10,000**. Other child, 2 weeks: **$5,000**.
- E93. 12I(3), April 2025 child, $1,500 a week, 4 weeks: **$6,000**.
- E94. 12I(4) self-employed: January 2024 child: **$10,000** total cap. Other child: **$5,000**.
- E95. 12J reimbursement: as E92, **$10,000** / **$5,000**.
- E96. 12I(1)(a): confinement 2016-12-31 (EDD same day): **not eligible**. Stillborn child 2021-10-31: **not eligible**. Stillborn 2021-11-01: **eligible**.
- E97. 12I(1)(c)(iii): married within 12 months from birth: **eligible**. Married 13 months after birth: **not eligible**.
- E98. 12I(1)(d): 2 months' service before the birth: **not eligible**.
- E99. 12HA amount: $200 a day, not a January 2024 child: 14 x 200 = **$2,800**. $500 a day, January 2024 child: 28 days, capped at $2,500 per 7, so **$10,000**. $500 a day, other child: **$5,000**.
- E100. 12HA(10): father of a stillborn child (confinement 2024-06-01): 14 days, not 28.
- E101. 12I(4A)(a): confinement 2020-12-31 (EDD same day): **not eligible** for 12HA. 2021-01-01: **eligible**.
- E102. 12JA(1): confinement 2023-12-31 with EDD 2024-01-02: **applies**. Confinement 2024-06-01 with EDD 2024-06-01: **applies**. Confinement 2025-03-31 with EDD 2025-04-01: **does not apply** (it is an April 2025 Scheme child). Confinement 2023-12-31 with EDD 2023-12-31: **does not apply**.
- E103. 12JA adoptive father: eligibility date 2025-03-31: **applies**. 2025-04-01: **does not**.
- E104. 12JA(2)(d) P/W minimum, with P = 2500 and W = min(WI, 6): WI 5 gives **$500** a day. WI 6 gives **$416.67**. Weekly pay $3,000 at WI 5 is more than $2,500, so the employer may pay $500 a day instead of $600. Weekly pay $2,000 at WI 5 means gross pay must be paid ($400 a day).
- E105. 12JA(4) reimbursement: at most $2,500 per WI/6 days, total **$5,000**.

## Goal 6: shared parental leave
### Second Schedule para 5 (M)
- E106. Born 2025-04-01, EDD 2025-04-01: **M = 6**.
- E107. Born 2026-03-31, EDD 2026-03-31: **M = 6**.
- E108. Born 2026-04-01, EDD 2026-04-01: **M = 10**.
- E109. Born 2026-03-31, EDD 2026-04-02: **M = 10** (para 5(a)(ii) needs the EDD to be before 1 April 2026).
- E110. Born 2025-03-28, EDD 2025-04-03: **M = 6** (5(a)(i)).
- E111. Adoption, eligibility date 2026-03-31: **M = 6**. 2026-04-01: **M = 10**.
### Default units (paras 6-7)
- E112. Sharing arrangement for a para 5(a) child: **3 and 3**. Other child: **5 and 5**.
- E113. Sole parent: **6** for a para 5(a) child. Otherwise **10**.
### Reallocation (para 8, 12DD)
- E114. M = 10, variation to 4 + 6: **valid**. 5 + 6: **invalid** (exceeds M). 4.5 + 5.5: **invalid** (not whole numbers).
- E115. Illustration: the father's N is 5 and he has consumed 3.5 x WI. The unconsumed balance is 1.5, so at most **1** unit can be reallocated and the 0.5 cannot.
- E116. Sole parent with M = 6: a variation to 7 is **invalid**.
### Specified variation period (paras 1, 14-16)
- E117. Born 2026-05-01: the period runs 2026-05-01 to **2026-05-28**. A notice on 2026-05-28 needs **no** employer agreement. A notice on 2026-05-29 **needs** employer agreement.
- E118. A notice inside the period, but the parent is under investigation for a s 16 offence connected with the arrangement: the Director **may require** employer agreement (para 16).
- E119. Adoption: the period runs from the eligibility date (2026-07-10 to 2026-08-06).
### Pay caps, s 12DB
- E120. N = 5, $3,000 a week, WI 5, 5 weeks: each week capped at $2,500, so **$12,500**. Reimbursement **$12,500**.
- E121. N = 3, $2,000 a week, 3 weeks: **$6,000**.
### s 12DC
- E122. N = 5: 35 days. At $300 a day: **$10,500**. At $500 a day: **$12,500**.
- E123. A 12DC claim submitted after the child's death: **disqualified** (12DC(5)(c)).
### Elected shared parental leave, ss 12E-12G
- E124. Born alive, confinement 2017-06-30, EDD 2017-06-30: **not eligible** (12F(1)(a)(i)). Confinement 2017-06-20 with EDD 2017-07-02: **eligible**.
- E125. Born alive, confinement 2025-03-31, EDD 2025-03-31: **eligible**. Confinement 2025-03-31, EDD 2025-04-01: **not eligible**.
- E126. Stillborn, confinement 2025-03-20, EDD 2025-04-10: **eligible** (12F(1)(a)(ii)(B) has no EDD condition).
- E127. Stillborn, confinement 2021-10-31, EDD 2021-10-31: **not eligible**. Stillborn, confinement 2021-10-25, EDD 2021-11-02: **eligible**.
- E128. Adoptive father, eligibility date 2017-06-30: **not eligible**. 2025-03-31: **eligible**. 2025-04-01: **not eligible**.
- E129. 12F(2): N = 4, $3,000 a week: **$10,000**. N = 2, $2,000 a week: **$4,000**.
- E130. 12E(7): when the mother elects N = 4, her 16 weeks are **reduced to 12**.
- E131. 12E(8)(b): a deceased mother had 6 whole weeks unconsumed, so N = **4** (capped).

## Goal 7: childcare and infant care leave (ss 12B-12D)
- E132. 12B(1), served 3+ months: less than 5 months in the period gives **2 days**. 5 months: **3**. 7: **4**. 9: **5**. 10: **5**. 11: **6**.
- E133. Served less than 3 months: **0** days (not entitled).
- E134. Child aged 7 (below 13): **2 days** of extended childcare leave. Child aged 13: **0**.
- E135. Child not a citizen: **not a qualifying child**, so 0.
- E136. 12B(2)(a): the combined cap is **6 days** per relevant period. The per-child caps are **42** childcare and **12** extended.
- E137. 12B(10): daily pay $800, 6 childcare days: 3 x 800 + 3 x 500 = **$3,900**. Daily pay $400, 6 days: **$2,400**.
- E138. 12B(10A): extended leave, daily pay $800, 2 days: **$1,000**.
- E139. 12C(1): 3 days granted: **0** reimbursable days. 4: **1**. 5: **2**. 6: **3**.
- E140. 12C(2): reimbursement for 3 days at $800 pay (paid $500 on those days): **$1,500**. At $300 pay: **$900**.
- E141. 12CA: extended, 2 days at $800: **$1,000**.
- E142. 12B(16) self-employed: ceased for 3 days: **0**. 4: **1**. 5: **2**. 6 or more: **3**. Each day is capped at $500: 3 days at $800 a day gives **$1,500**.
- E143. 12B(18B): at most **3 days** a calendar year across (16) and (16A).
- E144. 12D: a child below 2 gives **12** days of unpaid infant care leave per relevant period, capped at **24** per child. A child aged 2: **0**.
- E145. 12B(5) fallback: no 12B leave taken gives **2** days under EA 87A. 1 taken: **1**. 2 or more taken: **0**.
- E146. 12B(1B): a natural father married to another person when the child was conceived: **not entitled**. 12B(1C): the parents later marry each other before the birth: **entitled from the birth date**. They marry after the birth: **entitled from the marriage date**.

## Goal 8: general rules, recovery, disputes, offences
- E147. 12MA: two employers both pay 1st-event maternity at $3,000 a week. The aggregate reimbursement across both employers is capped at **$20,000** (the single-employer limit). Each employer may still pay in full (12MA(2)).
- E148. 12MA applies only to a relevant child, that is one whose confinement or eligibility date is on or after 2025-04-01. A confinement on 2025-03-31 is **not** covered.
- E149. 12N(4)(a): recovered 2025-03-10, reimbursed 2025-02-01: refund by **2025-04-10**. Recovered 2025-01-31, reimbursed 2025-03-31: **2025-04-30**.
- E150. 12N(4)(a) month-end: the later date is 2025-01-31, so the deadline is **2025-02-28** **(doubt: "within one month after" at month-end)**.
- E151. 12N(5): contravening 12N(4)(a) carries a fine of up to **$20,000** and **no** imprisonment.
- E152. 12N(9)(e): the child is not adopted within 12 months of the eligibility date: **defaulting event**. The child is not a citizen within 6 months of the adoption: **defaulting event**.
- E153. 12O(1): 1st event, total period 57 days: **recoverable**. 56 days: **not** (only "exceeds" triggers recovery). 3rd event, 112 days: **not**. 113 days: **recoverable**.
- E154. 12O(2): adoption, 1st event, 57 days: recoverable. 3rd event threshold: **84** days.
- E155. 12O(3): father threshold **14** days, or **28** if 12HA(2)(b) applies.
- E156. 12O(2A): shared, N = 5, threshold **35** days.
- E157. s 14: the dispute arises 2025-05-10, so refer by **2025-06-10** (or a later time the Minister allows).
- E158. 12AA(8) failure to grant: **$5,000 / 6 months**. Repeat offender: **$10,000 / 12 months**.
- E159. s 16: **$20,000 / 12 months**. s 18: **$20,000 / 12 months**.
- E160. s 17(1): **$5,000 / 6 months**. Repeat: **$10,000 / 12 months**. A prior conviction only before 2013-05-01 does **not** make the employer a repeat offender (17(1AA)).
- E161. 12D(7): first offence **$5,000 / 6 months**. Subsequent offence **$10,000 / 12 months**.
- E162. s 19(1): offences under 12N, 16 and 18 (and the regulations) are compoundable by the Minister up to **$5,000**. s 19(2): offences under 12AA, 12B, 12D, 12DA, 12E, 12H and 17 are compoundable by the Commissioner up to **$1,000**. An offence under s 16 is **not** compoundable under 19(2).
- E163. s 20(3), offences under the regulations: up to **$20,000 / 12 months**.
