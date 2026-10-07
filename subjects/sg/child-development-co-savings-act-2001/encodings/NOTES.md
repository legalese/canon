# Child Development Co-Savings Act 2001 (Singapore) — encoding notes

Read this first. `BRIEF.md` is the specification; `../source/PROVENANCE.md` says where the text came from and transcribes the four formulas the PDF prints as images.

## 1. What is encoded

**The whole Act** (Parts 1–4 and the First and Second Schedules), as printed by SSO, "Current version as at 07 Oct 2026". That is the 2020 Revised Edition, amended up to Act 46 of 2024, which came into force on 1 April 2025.

**Dates.** The Act states its own cohorts and windows by date, and each is encoded as printed:
- "April 2025 Scheme child" and "January 2024 Scheme child" (s 2);
- the 2017 and November 2021 (stillbirth) gates in ss 9A, 12I and 10(2B);
- the July 2017–March 2025 window for elected shared parental leave (s 12F);
- the January 2024–March 2025 window for extra paternity leave (s 12JA);
- the maximum units M (Second Schedule, para 5).

A case outside these dates is answered as the Act answers it: not eligible. Nothing is refused for its date alone. The source is a consolidation of the law now in force; where an amendment changed an earlier rule, the earlier text is not encoded.

**Amounts.**
- Pay is an input: the parent's gross rate of pay, or lost income, per week of work days. A "4 times the weekly index or 24 days" period is 4 weeks of work days, and a "weekly index or 6 days" period is one week of them.
- The Government-paid benefits take total income per day over the prescribed period. The period is prescribed by regulations, so the daily figure is an input.
- What the encoding computes is the most the Act allows: each cap applied per period and in total.

**Inputs.** The following are taken as inputs:
- the Employment Act 1968 periods that s 9(1A) refers to;
- regulations, the Scheme's caps, and reductions by regulation;
- the Minister's and a Director's decisions;
- the specified event number. The caller can compute it with `the specified event number on`.

**The existing `sg/child-support` subject** also encodes childcare leave under this Act, as part of the 2026 child support package. This is a separate row on a separate subject; the two have not been reconciled.

### The goals

Top level: `the parental position for` a `Parent case` (`cdcsa-goal.l4`). The question is: *for this parent and this child, what paid leave or Government payment does the Act give, how much may be paid, and how much may the employer claim back?* For one parent, it answers:
- the child's scheme;
- the parent's own paid leave (maternity, adoption or paternity), or the self-employed claim, or, failing both, the Government-paid benefit;
- shared parental units, and the leave or claim they carry.

| goal | question | main functions | provisions | module |
| --- | --- | --- | --- | --- |
| 1 | Which scheme is the child in? What is the eligibility date and the event number? What is the weekly index, and how long are its multiples? | `an April 2025 Scheme child`, `the eligibility date of`, `the specified event number on`, `the weekly index for`, `the lower of … times the weekly index … or`, `at most … per block and … in all` | s 2, First Schedule | `cdcsa-common.l4` |
| 2 | How much does the Government match? Who becomes trustee? What happens on death? How is a wrong payment recovered? | `the Government's matching contribution…`, `the substitute trustee for`, `the means of recovery open to the Government…` | ss 3–8 | `cdcsa-scheme.l4` |
| 3 | Is a mother eligible for maternity leave or benefit? How much is paid, and how much claimed back? | `eligible under s 9A(1)…`, `maternity leave payments…`, `the s 9(1A) outcome under s 76(1)`, `the Government-paid maternity benefit at most…` | ss 9, 9A, 10, 12 | `cdcsa-maternity-adoption.l4` |
| 4 | The same for adoption | `eligible for adoption leave under s 12AC(1)…`, `adoption leave payments…`, `the Government-paid adoption benefit at most…` | ss 12A–12AD | `cdcsa-maternity-adoption.l4` |
| 5 | Paternity leave, pay, benefit and extra leave | `paternity leave payments…`, `the Government-paid paternity benefit at most…`, `s 12JA applies to the child`, `the least an employer may pay per day of extra paternity leave…` | ss 12H–12JA | `cdcsa-fathers-shared.l4` |
| 6 | Shared parental leave units, pay and benefit | `M, the maximum number of units for`, `the default units for a parent of`, `a valid allocation of`, `shared parental leave payments for`, `the shared parental benefit at most for`, `elected shared parental leave payments for` | ss 12DA–12DD, 12E–12G, Second Schedule | `cdcsa-fathers-shared.l4` |
| 7 | Childcare, extended childcare and unpaid infant care leave | `childcare leave days…`, `the employer pays at most for…`, `the Government reimburses childcare leave at most…`, `unpaid infant care leave days…` | ss 12B–12D | `cdcsa-childcare.l4` |
| 8 | Paid days, several employers, recovery, disputes, offences, composition | `the Government pays across all employers…`, `the employer must refund by…`, `the Government may recover under s 12O…`, `the maximum penalty for`, `the most that may be collected to compound` | ss 12L–22 | `cdcsa-general-offences.l4` |

## 2. Coverage table

| provision | heading | disposition |
| --- | --- | --- |
| long title, 1 | | inert |
| 2(1) | Interpretation | Goal 1: the Scheme children, the eligibility date and the weekly index. Specified events are via (2). The other definitions are read into the facts: confinement, gross rate of pay, self-employed, employer and so on |
| 2(1A), (2B), (2C) | platform workers; day of death; s 12MA | read into the facts; (2C) is via Goal 8's s 12MA |
| 2(2) | first, second or later specified event | Goal 1 |
| 2(2A) | age | Goal 1 |
| 2(3)–(4) | amending Schedules | inert |
| 3 | Scheme | (3) co-savings: Goal 2. (1)–(2) are a regulation-making power, inert |
| 4 | Substitution of trustee | Goal 2, (1)(a)–(j). (2)–(3) noted |
| 5 | Protection of benefits | Goal 2 (as text) |
| 6 | Death of member | Goal 2 |
| 7 | Approved persons | inert (regulation power) |
| 8 | Recovery of payment | Goal 2, (1)–(2). (3) inert |
| 9 | Maternity benefit period | Goal 3: (1), (1A) limb selection, (1B) options, (2), (2A)–(3A) forfeiture, (4)–(5) self-employed, (5A)–(8) the Government-paid benefit and disqualification |
| 9A | Eligibility and caps | Goal 3: (1), (1A), (2), (4), (5), (5A)(a). (2A) day counting is left to the caller. (3)–(3A), (5B)–(8) read into the facts. (5A)(b) reductions are by regulation |
| 10 | Reimbursement | Goal 3: (1)–(2), (2A)–(2C) and (3) |
| 10A, 11 | repealed | — |
| 12 | Employment Act provisions | carried as text |
| 12A | Adoption benefits | Goal 4: (2)–(3)(a). (4) reductions and (5)–(7) disqualification are carried as text. Disqualification is applied in the top-level goal |
| 12AA | Adoption leave (employee) | Goal 4: (1), (2), (4)–(6). (1A), (7)–(13) notice and offences: Goal 8 penalties |
| 12AB | Adoption leave (self-employed) | Goal 4 |
| 12AC | Eligibility | Goal 4, (1)–(3) |
| 12AD | Reimbursement | Goal 4, (1)–(2). (3)–(4) carried as text |
| 12B | Childcare leave | Goal 7: (1)–(2)(a), (1B)–(1C), (5), (9)–(10A), (16)–(19). (2)(b), (3), (7), (8), (11), (11A) carried as text. (12)–(14C) are offences, in Goal 8 |
| 12C, 12CA | Reimbursement for childcare leave | Goal 7; (2A) carried as text |
| 12D | Unpaid infant care leave | Goal 7, (1)–(2)(a), (1A)–(1B). (7) is in Goal 8. The rest carried as text |
| 12DA–12DD | Shared parental leave, April 2025 Scheme | Goal 6: M, default units, valid allocation, pay and benefit caps. The remaining limbs are carried as text |
| 12E–12G | Elected shared parental leave | Goal 6: 12F(1), (1A), (2)–(3); 12E(7), (8); 12G. The rest carried as text |
| 12H, 12HA, 12I, 12J, 12JA | Paternity | Goal 5. The remaining limbs are carried as text |
| 12K–12KC | repealed | — |
| 12L, 12M | Holidays; unpaid leave | Goal 8 |
| 12MA | Concurrent employment | Goal 8: (2)–(4). (5)–(8) noted |
| 12MB | Sequence of leave | Goal 8 |
| 12N | Recovery due to defaulting event | Goal 8: (4)–(5), (9)(e). (1)–(3), (6)–(8) are powers, inert |
| 12O | Recovery in other circumstances | Goal 8 |
| 13 | Exclusion of classes | carried as text |
| 14 | Disputes | Goal 8 |
| 15, 15A | Change of residence; verification | carried as text |
| 16–19 | Offences and composition | Goal 8 |
| 20–22 | Regulations; exemptions | carried as text |
| First Schedule | Weekly index | Goal 1: Part 1 items 1–3 and notes 3, 3A, 5. Parts 2–3 (applicable dates) are read into the caller's choice of work pattern |
| Second Schedule | Arrangements | Goal 6: paras 1, 5–10, 14–16. Paras 2–4, 11–13, 17–18 carried as text |

Nothing is left `deferred`.

## 3. Fork register

| id | provision | question | reading taken | why |
| --- | --- | --- | --- | --- |
| F1 | s 9A(4), 10(2), 12AA(5), 12AD(2) | Is the first 8 weeks of maternity pay (4 weeks for adoption) capped for a first or second event? | No. The employer pays the gross rate, uncapped and not reimbursed. Only the later weeks carry the $10,000-a-period cap | The caps are stated "after the first 8 weeks" |
| F2 | s 9(1A)(i)(A), (iii)(A) "within the first 4 [8] weeks of the specified period" | Where is the edge? | Before the specified period's start date plus 28 [56] days | Counting whole weeks from its first day |
| F3 | s 9(1A)(iva) "after the period of 16 weeks, which commences on the first day …" | When does the period end? | Citizenship on or after the first day of absence plus 112 days | 16 × 7 days |
| F4 | ss 12H(4), 12I(4) "January 2024 Scheme child" | A self-employed father's 4 weeks follow the January 2024 cohort, but an employee's follow April 2025 (s 12H(1)(a)(i)). Is that a slip? | Encoded as printed | The two provisions name different cohorts; the encoding does not correct either. Whether the difference is intended is an open question for a domain expert (§6) |
| F5 | Second Schedule para 5(a)(ii) | A child born on 31 March 2026 whose estimated delivery date was in April 2026 | M = 10 | (a)(ii) requires the estimated delivery date to be before 1 April 2026, and (a)(i) covers only births before 1 April 2025 |
| F6 | s 12E(7) "reduced by N weeks, taken from the last N weeks" | Which pay do the weeks come out of? | The capped (reimbursed) weeks first | They are the last weeks |
| F7 | s 12B(2)(a)(iii) and (1)/(1A) | How do the 6-day combined cap and the per-child caps combine? | Each kind is capped by its per-child remainder first, then the sum by 6 | The text |
| F9 | s 3(3) co-savings "equal to the contributions" | Is the match computed with no cap given? | No: the encoding refuses without the cap remaining under the regulations | The Scheme's caps are made by regulations under s 3, which are not in the source. The independent pass expected a full match (D1); both readings are recorded |
| F8 | Top-level goal | A mother whose child became a citizen after birth (s 9(1A)/(1B)) | The goal refuses and names the rules to ask | Those limbs turn on Employment Act periods outside the source |

## 4. Tests

`cdcsa-tests.l4` has 218 assertions. Expected values are worked from the source, with the arithmetic shown. They include:
- every Scheme-date edge;
- s 2(2) counting either side of 1 November 2021;
- the First Schedule formulas and note 5 rounding;
- the maternity, adoption, paternity and shared caps for first, second and later events;
- the s 9(1A) limbs at their edges;
- the Second Schedule para 8 illustration;
- childcare days by months served;
- the reimbursement caps, the s 12N(4) and s 14 deadlines, the penalties and composition sums;
- seven whole cases through `the parental position for`;
- the s 12B(16)–(18A) limits, added after the independent pass.

`tests-independent.l4` has 268 assertions; with it are `independent-expectations.md` and `INDEPENDENT-TEST-REPORT.md`. A separate session wrote its 163 expectations from the source before reading the encoding:
- **267 were satisfied and none failed.**
- **One refuses: D1, line 162.** It is the co-savings match with no regulation cap given (fork F9). `check.sh` counts satisfied and failed assertions only, so it does not report this refusal. That is a gap in the shared script: it reads l4's refusal warnings as neither.
- **Fixed after the pass:**
  - the top-level goal now sends a parent with no current employer or trade to the Government-paid benefit, which a probe found it did not;
  - Second Schedule para 16 is now an input ("a Director has required"), not automatic;
  - the s 12B(16)–(18A) 3-month condition and per-child limits were added.
- **Plumbing change in the independent file:** the para 16 parameter was renamed, five uses. No expected value changed.
- **Simplifications the report lists, and kept as they are:**
  - timing windows (26 weeks, 16 weeks, 12 months, start dates, the child's death) are the caller's to respect;
  - s 9(1A) answers with a limb, not an amount;
  - discretionary reimbursement, other than s 10(2A), is carried as text;
  - s 12MA is the lesser of the claims and the limit;
  - the Second Schedule beyond paras 1 and 5–10 and 14–16 is carried as text;
  - once-per-confinement, repeat-offender dating and s 12E(8)(b) are inputs or carried as text.

## 5. Checks

See `encoding.json` → `checks`.

## 6. Open questions

- F4: is the January 2024 cohort for self-employed fathers (ss 12H(4), 12I(4)) intended, against April 2025 for employees?
- Regulations: the prescribed periods for total income, and the reductions in ss 9A(5A)(b), 12A(3)(b), 12DC(4)(b), 12HA(3)(b), would let the Government-paid benefits be computed rather than capped.
