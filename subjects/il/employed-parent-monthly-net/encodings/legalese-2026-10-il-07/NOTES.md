# NOTES — il/employed-parent-monthly-net, encoding row `legalese-2026-10-il-07`

The capstone: the monthly net income, in a month of 2026, of a household in Israel with one employed parent, composed from six deposited rows encoding the Income Tax Ordinance (IL-01, IL-02, IL-03) and the National Insurance Law (IL-04, IL-05, IL-06).
One agent, one session, no sub-agents (run `IL-07-20261006`, encoder `enc-il-07`, 2026-10-07), from the brief in `BRIEF.md`.
Status: **draft**.
No domain expert has read it; HG1 has not been sought.

Read with it: `RECONCILE.md` (how the rows' nouns were reconciled, and the changes proposed to the rows) and `GAPS.md` (the provisions no row encodes, in IL-08's work order).

## 0. What `check.sh` prints

Run from 2026-10-06T22:53:25Z to 23:06:50Z (13 min 25 s wall clock on a busy machine) as `L4=/Users/mengwong/.local/bin/l4 ./check.sh`, `JL4_LIBRARY_PATH` unset.
The binary is `~/.local/bin/l4` → `~/.cabal/bin/l4`, cabal store `jl4-0.1-0ee0100b`, sha256 `64bbcb157dbef2ef1020a6a75589313bba0a2aeeb807c921c5e65e62e9eca118`, the build all six rows used; it has no `--version`.
No module of this row and no vendored copy changed during the run (checked against hashes taken before it).

```
vendor.sh: 36 vendored modules match their sources and VENDORED.sha256
module                                    errors satisfied  failed  refused  expected
il07-adapter-il01.l4                           0         0       0        0         0
il07-adapter-il02.l4                           0         0       0        0         0
il07-adapter-il03.l4                           0         0       0        0         0
il07-adapter-il04.l4                           0         0       0        0         0
il07-adapter-il05.l4                           0         0       0        0         0
il07-adapter-il06.l4                           0         0       0        0         0
il07-nouns.l4                                  0         0       0        0         0
il07-pipeline.l4                               0         0       0        0         0
il07-published-figures.l4                      0         0       0        0         0
il07-refusals.l4                               0         0       0        0         0
il07-tests-expected-red.l4                     3         0       3        0         3
il07-tests.l4                                  0       113       0        0         0
TOTAL (12 modules)                             3       113       3        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

`check.sh` exit 0.
The 3 errors are the 3 failed assertions of `il07-tests-expected-red.l4`, which `check.sh`'s `expected_failed` table and `encoding.json`'s `expected_red` both name with that count; read from the diagnostics, they are the module's only three assertions, at lines 68 and 69 (`assertion failed`, finding R1) and 123 (`assertion failed: expected a refusal, but the expression produced a value`, finding R2), each predicted before the module was first run.
`il07-tests.l4`: 113 assertions, 113 satisfied, of which 27 are `#ASSERT REFUSED … BECAUSE "…"` pinning a refusal's wording; none refused.
The rule modules carry no assertions.
Every run also prints two Warnings that differing copies of `prelude` and `daydate` exist under `~/.local/share/jl4/libraries/`; the binary uses its embedded copies.

The harness can fail: `il07-tests-expected-red.l4` is the proof, and its three failures are counted, not hidden.
An earlier full run (22:40:08Z-22:52:56Z) printed the same table; a comment in `il07-published-figures.l4` was edited during it, so the run above, made after, is the one recorded.

## 1. What is composed, and what is not

**The question.** For a household in a month of 2026: the income tax for tax year 2026 and one twelfth of it; the national insurance contributions the employer deducts from the salary for the month; the health insurance contribution (an input); the child allowance for the month; and the net, salary less the tax's twelfth, the national insurance and the health contribution, plus the allowance.

**The household** (`BRIEF.md`, "The household"): one employed resident parent, paid the same gross salary by one employer every month of 2026; possibly a spouse with no income; children who are the earner's (and the spouse's) own, unmarried, living with them, in Israel; no Income Support, no maintenance payments, no absences, no other income; and no credit or deduction beyond those the rows encode (an input: FALSE declines the tax).

**How each figure is made.** No rule of law is the capstone's own; every one is a row's, called through that row's adapter.

| figure | made by | through |
| --- | --- | --- |
| the year's taxable income | 12 × the monthly salary (fork K1) | the IL-02 and IL-03 adapters build their income records from it |
| the s 121 tax | IL-03 `the tax under section 121 for` | `IL-03: the tax under section 121 on the earner's salary, in` |
| the s 121B additional tax | IL-03 `the additional tax under section 121B for`, with the 2026 amount the Tax Authority published | `IL-03: the additional tax under section 121B …`; `il07-published-figures.l4` |
| the value of a credit point | IL-03 `s 120B — the amount in force in the tax year`, given IL-01's published 2025 value as the 1 January 2024 figure (fork K2) | `IL-03: the credit-point amount in force in tax year …`; `IL-01: the value of one credit point …` |
| the personal credit points | IL-01 `the credit points under sections 34, 36 and 36A for` | `IL-01: the credit points under sections 34, 36 and 36A for the earner` |
| whether s 66(c) governs, and the points it gives (s 37's half, the children's) | IL-02 `s 66(c) — governs the calculation of the`, `s 66(c) — the credit points it gives the` | `IL-02: section 66(c) governs …`, `IL-02: the credit points section 66(c) gives the earner, in` |
| the children's credit, capped at the tax on income from personal exertion | IL-02 `s 66(c)(4)-(5) — the credit for children, …` (its fork F13) | `IL-02: the credit for … children's points …` |
| points to money, and the set-off | IL-01 s 33A: `the amount of … credit points …`, `the tax for the year after setting off …` (its fork F5) | `IL-01: the amount of …`, `IL-01: the tax after setting off …` |
| the income for contributions | IL-05 `s 348 — the income on which contributions are computed, for` (Schedule K's maximum and minimum) | `IL-05: the income on which the earner's contributions are computed, in` |
| column D per branch on that income | IL-04 `the column D deduction under …`, the 2026 version of Schedule J, the 2026 threshold | `IL-04: the column D amounts in a month of …` |
| the employer's deduction | IL-05 `s 342(c) — the amount the employer deducts from the wage, for` | `IL-05: the amount the employer deducts from the earner's wage, …` |
| additional-tax income for the allowance | IL-03's s 121B for the month's tax year, above nil (fork K5) | `IL-07: the earner has income chargeable to additional tax …` |
| the child allowance | IL-06 `the child allowance of each person, at the basic amounts the Institute published for the day, in`, on the first day of the month (fork K6) | `IL-06: the household's child allowance for the month, in` |

**Modules** (this row's own; line counts at deposit):

| module | lines | holds |
| --- | ---: | --- |
| `il07-nouns.l4` | 168 | the household, the records that pass between rows, the answer; `DECLARE` only |
| `il07-refusals.l4` | 125 | the 13 refusals the capstone itself owns |
| `il07-published-figures.l4` | 54 | the s 121B(a) amount for 2026, as the Tax Authority published it; not law |
| `il07-adapter-il01.l4` | 81 | IL-01: the earner as a `Person`, the points, s 33A, IL-01's published figures |
| `il07-adapter-il02.l4` | 176 | IL-02: the couple as `Spouses in a tax year`, whether s 66(c) governs, its points, the children's credit |
| `il07-adapter-il03.l4` | 103 | IL-03: the earner as `An individual in a tax year`, s 121, s 121B, s 120B |
| `il07-adapter-il04.l4` | 105 | IL-04: the threshold, column D per branch |
| `il07-adapter-il05.l4` | 124 | IL-05: s 348's income, s 342(c)'s deduction |
| `il07-adapter-il06.l4` | 209 | IL-06: the family on the first day of the month, the allowance, the s 72 check |
| `il07-pipeline.l4` | 257 | the composition, the period gate, the `@export` |
| `il07-tests.l4` | 445 | 23 households (H1-H20, H3b, and H3 in June 2025 and June 2027) and 113 assertions (27 of them `#ASSERT REFUSED`) |
| `il07-tests-expected-red.l4` | 123 | 3 assertions expected to fail (section 6) |

Plus `vendor.sh` (100 lines), `check.sh` (71), `VENDORED.sha256` and `.gitignore`; and 36 vendored modules of the six rows, not committed.

## 2. Coverage table

What the capstone uses of each row, and what it does not.
"Composed" means a household's answer runs through it; "reached" means a test reaches it (often as the row's own refusal); "not needed" means the household of the brief never reaches it.

| row | provision | disposition | where |
| --- | --- | --- | --- |
| IL-01 | s 33A "נקודת זיכוי" limbs (1)-(2), points to money | composed | `IL-01: the amount of …` |
| IL-01 | s 33A limb (3), the set-off, never below nil (IL-01 F5) | composed | `IL-01: the tax after setting off …` |
| IL-01 | s 33A "נקודת קיצבה" | not needed | — |
| IL-01 | ss 34, 36, 36A | composed | H1-H10 |
| IL-01 | s 48A refusal (foreign worker) | reached | H18 |
| IL-01 | s 48 refusal (Area resident not a citizen) | not reached by a test | — |
| IL-01 | published: 2025 annual value 2,904; monthly 242 for 2024-2026 | composed (fork K2); cross-checked | figures tests |
| IL-02 | s 66(a)(1) the claim, with (d)'s gate (no common source) | composed | H3b, H4 |
| IL-02 | s 66(c)(1A) the request | composed | H3, H5, H6, H7, H8, H10 |
| IL-02 | s 66(c) chapeau, whether (c) governs | composed; "does not govern" declined as s 65 | H11 |
| IL-02 | s 66(c)(2), s 37's half point | composed (the input is FALSE in every test, so always 0) | — |
| IL-02 | s 66(c)(4)(a) and (a1), the woman's table and the election | composed | H4 (with the election), H6, H8 |
| IL-02 | s 66(c)(5), the man's table | composed | H3, H5, H7, H10 |
| IL-02 | s 66(c)(4), the half point under s 36A | not counted (fork K7); compared with IL-01 | figures tests; red R2 |
| IL-02 | s 66(c)(4A), (6), a widowed partner's children | not needed: every child is both spouses' | — |
| IL-02 | s 66(a)(2), (a)(3), (b), the income assembly | reached as a cross-check only (fork K4) | H3b |
| IL-02 | tax years from 2024 | reached: answers 2025 | `H3 in 2025` |
| IL-03 | s 121(a), (b)(1) reduced rates on personal exertion | composed | H1-H10 |
| IL-03 | s 121(b)(2), age 60 | not needed (salary is personal exertion; earners under 60) | — |
| IL-03 | s 121 for 2025 (declined) and 2027 (answered) | reached | `H13`, `H3 in 2027` |
| IL-03 | s 121B(a) | composed | H7, H8 |
| IL-03 | s 121B(a1), (e) residential | not needed (salary is not capital-source income; no real estate) | — |
| IL-03 | s 120B(e)(1), the 2025-2027 freeze | composed | the credit-point value |
| IL-03 | s 120B(a), (e)(2), (d) | reached as IL-03's refusals | 2024, 2028 |
| IL-04 | s 334(a), the 2026 threshold; 2025 and 2027 declined | composed; reached | all; year tests |
| IL-04 | Schedule J, the version for 2026, column D | composed | all |
| IL-04 | s 337 (column C, the contributions in total) | not needed: the employee's net turns on the deduction (column D, s 342(c)), not on the total | — |
| IL-04 | s 1 "employee", "self-employed person", "the average wage" | not needed: the earner is an employee by the brief; column D for 2026 reads no average wage (fork K9) | — |
| IL-05 | s 348(a), (b) with Schedule K item 1 | composed | H7 (maximum), H9 (minimum) |
| IL-05 | s 348(a1), (d), (e) | reached with nil (no non-work income, no status) | all |
| IL-05 | s 342(c)(1), (c)(2) | composed; (c)(2)'s age limb takes the Part D input | all; H19 |
| IL-05 | s 342(a)-(b), (d), (e1), (f) | not needed (one employer, not also self-employed) | — |
| IL-05 | 2025 and 2027 declined | reached | year tests |
| IL-06 | ss 65, 66, 67(a)-(b), 68(a) | composed | H1-H12 |
| IL-06 | s 66's additional-tax exclusion, s 67(b) first limb with an excluded father (IL-06 F6) | composed | H7, H8 |
| IL-06 | s 68(b), (c) | not needed (no child born before June 2003; no Income Support) | — |
| IL-06 | 2025 answered; 2027 declined | reached | `H3 in 2025`, `H3 in 2027` |

**The gaps** (provisions no row encodes) are in `GAPS.md`, each with its disposition: a named input, a named refusal, or an input convention of the brief.
None is left silent.

## 3. The period

| row | answers | source of the limit |
| --- | --- | --- |
| IL-01 | any tax year for which the credit-point value is supplied | IL-01 NOTES.md section 1 |
| IL-02 | tax years from 2024 | IL-02 NOTES.md A1 |
| IL-03 | s 121: 2026 and 2027; s 121B: from 2026, with the amount supplied; s 120B: from 2025 | IL-03 NOTES.md A1 |
| IL-04 | contribution months from January 2026; 2027 only on a threshold the caller supplies | IL-04 NOTES.md section 1 and Repair 2026-10-07 |
| IL-05 | contribution periods from January 2026; 2027 only on figures the caller supplies | IL-05 NOTES.md A1 |
| IL-06 | days from 1 May 2015 to 31 December 2026 (the published basic amounts end there) | IL-06 NOTES.md A1, A3 |

2026 is the only year all six answer on their own figures, so the capstone answers months of 2026 and refuses every other by name ("IL-07 answers months of 2026 only, the one period all six composed rows answer").
The tests show the rows' own answers for 2025 and 2027, adapter by adapter (H13, `H3 in 2025`, `H3 in 2027`): in 2025 IL-03, IL-04 and IL-05 decline while IL-02 and IL-06 answer; in 2027 IL-03's s 121 answers while IL-04, IL-05, IL-06 and the s 121B figure decline.

## 4. Fork register

None of these has been settled by a court or a regulator to my knowledge.

| # | where | the question | readings | taken, and why |
| --- | --- | --- | --- | --- |
| K1 | the year's tax against a month | How does tax for a year become a month's figure? | (i) one twelfth of the year's tax, for a salary the same every month; (ii) the withholding the Income Tax (Deduction from Salary and Wages) Regulations 5753-1993 prescribe; (iii) decline | **(i), and decline otherwise.** The Ordinance charges tax for a year: s 121(a) "המס על הכנסתו החייבת של יחיד בשנת המס" (ITO line 4350); a credit point is an amount "לשנת מס" (s 33A, line 1563). Withholding is s 164 (line 5323), "באופן ובשיעורים שנקבעו", by Regulations not in the source bundle (noted at line 5338), so (ii) is not available. The answer is named "one twelfth of the income tax for the tax year", not "the tax withheld". A salary that varies is declined, because the year's income is then not twelve times the month's. Consistent with it: the Tax Authority's booklet prints the credit point at 242 a month for 2026 (IL-01), which is 2,904 / 12. |
| K2 | the credit-point value for 2026 | Where does the capstone get it? | (i) IL-03's s 120B for 2026, from the 1 January 2024 amount after rounding, which is IL-01's published 2025 value; (ii) twelve times the booklet's monthly 242 | **(i)**: s 120B(e)(1) (line 4344) fixes the amounts of 2025, 2026 and 2027 at their 1 January 2024 figure after rounding, so the Tax Authority's 2025 value (2,904, [itc135-2025] p. 4, IL-01) is that figure, and IL-03's rule gives 2026 the same. (ii) agrees and is asserted. |
| K3 | the set-off, and s 121B | Are credit points set off against the s 121B additional tax? In what order are several credits set off? | (i) against the s 121 tax only, never below nil, the additional tax added after; (ii) against the total | **(i), and declined where it matters.** s 33A sets a credit point off "כנגד המס לאותה שנה"; s 121B is a further tax computed separately (IL-03 A6: the s 121 result is the tax before credit points). Where the credits exceed the s 121 tax and there is additional tax, the two readings part, and the capstone declines; no household of the brief's shape reaches it (at the s 121B threshold the s 121 tax is about 224,000). The order of several credits does not matter here: all the earner's income is from personal exertion, so IL-02's cap on the children's credit (the tax on that income, its F13) is the whole s 121 tax, and every order gives max(0, tax − credits). |
| K4 | the couple's income | Whose income is in the earner's calculation? | — | **The year's salary, in every case answered.** The spouse has no income (a household with two earners is declined: s 66(a)(2) would move income between them). Where the earner is the spouse who is not registered and claims under s 66(a)(1), IL-02 places the salary in the separate calculation (asserted, H3b: 180,000). Where the earner is the registered spouse and requests under s 66(c)(1A), IL-02 says (1A) moves no income and s 65 governs (its A3); under s 65 the couple's income is "כהכנסת בן הזוג הרשום" (line 2448), which, with the spouse at nil, is the earner's salary. Where no separate calculation governs at all, s 66(c)'s points do not apply and the capstone declines, naming s 65. |
| K5 | IL-06's additional-tax input | Which tax year's "income chargeable to additional tax" excludes a parent from the allowance for a month? (IL-06 F5) | (i) the tax year in which the month falls; (ii) the last assessed year | **(i)**: the capstone has the 2026 liability and no other; the parent is excluded iff IL-03's s 121B tax for 2026 is above nil. |
| K6 | the day IL-06 is asked about | IL-06 answers a day; s 72 (months paid) is not encoded. | (i) the first day of the month, declining a month in which a child is born or turns 18 after it; (ii) the last day; (iii) any day | **(i)**: for a household of the brief's shape nothing IL-06 reads changes within a month except a birth or an 18th birthday (the basic amounts change on 1 January), so (i) answers every other month exactly and declines, naming s 72, the months where a choice of day would decide the answer. A child born after the day is not yet in the family. |
| K7 | s 36A, twice | IL-01 encodes s 36A; IL-02 restates its half point in s 66(c)(4). Count it once or twice? | — | **Once, from IL-01**: s 66(c)(4) gives the half point "לפי סעיף 36א", s 36A's own. IL-01's is preferred because it carries s 48A's reach (red finding R2 shows IL-02's does not). |
| K8 | the base of the employee's deduction | Is the s 342(c) deduction a percentage of the wage paid, or of the s 348 income? | (i) the s 348 income (maximum and minimum applied); (ii) the wage | **(i)**: s 342(c)(1) "ינכה המעביד משכרו של העובד אחוזים מההכנסה שלפיה משתלמים דמי הביטוח" (NII line 3661), percentages of the income on which contributions are paid. So a salary of 5,000 in February is deducted on 6,247.67 (H9) and one of 70,000 on 51,910 (H7). |
| K9 | IL-04's average-wage argument | Which average wage does column D read for 2026? | — | **None**: every version IL-04 reads for 2026 starts column D's upper part at the threshold (its F3, repaired), so the argument is not read; the adapter passes a named refusal rather than choose between IL-04's two figures (its open F5). |
| K10 | the tests' health figure | What health contribution do the tests supply? | — | **Not a fork of the capstone, which takes it as an input.** The tests apply the Institute's published employee health rates, 3.23% up to 7,703 and 5.17% above (IL-04 NOTES.md section 7), to the salary up to 51,910; that the National Health Insurance Law's maximum is Schedule K's is an assumption of the test author, unsourced (GAPS.md item 4). |
| K11 | the s 37 input | Does the earner in a separate calculation have a s 37 point to halve? | — | An input, as in IL-02; FALSE in every test. s 37 (line 1600) needs a "יחיד מוטב" (past retirement age, blind or disabled) who proves the spouse's maintenance. |

## 5. Answer table: the worked households

All for tax year 2026 and the month named; amounts in NIS; every figure worked by hand from the figures below, then checked with exact fractions in a scratch calculator (`expected.py`, kept in the session scratchpad, which reads no L4).
The check caught one slip of mine before any run: the health input for H7 and H8 is 248.8069 + 44,207 × 5.17% (2,285.5019) = 2,534.3088, which I had first written as 2,534.2088.
One expected value was also corrected before any run, when I worked it: IL-02's children's points for `H3 in 2025` are 4.5 + 1 = 5.5 (ages 2 and 6 in 2025), not the 6 first typed.

**The figures.**
Credit point 2,904 a year (K2).
s 121 for 2026 (ITO lines 4351-4358; enacted by the 5786 Law s 5, from 1 January 2026): on income from personal exertion 10% to 84,120, 14% to 120,720, 20% to 228,000, 31% to 301,200, 35% to 560,280, 47% above; so 8,412 at 84,120; 13,536 at 120,720; 34,992 at 228,000; 57,684 at 301,200; 148,362 at 560,280.
s 121B: 3% above 721,560 ([booklet-2026] p. 8).
Personal points: 2.25 for a man, 2.75 for a woman (ss 34, 36, 36A; IL-01).
Children's points (s 66(c)(4) the woman / (5) the man), by age in the tax year: 0 → 2.5 / 2.5; 1-2 → 4.5 / 4.5; 3 → 3.5 / 3.5; 4-5 → 2.5 / 2.5; 6-17 → 2 / 1; 18 → 0.5 / 0; the mother's (a1) election moves one point from age 0 to age 1 (IL-02 NOTES.md section 5).
Threshold 7,703; column D 1.04% / 4.67% (IL-04 NOTES.md section 5); Schedule K maximum 51,910 a month, minimum the minimum wage of the quarter's first month, 6,247.67 (January) and 6,443.85 (April on) (IL-05 NOTES.md section 5).
Child allowance on 1 January 2026 on: 173 for the first child and the fifth on, 219 for the second to fourth (IL-06 NOTES.md section 5); the count is with the insured father where both parents are insured, and with the one insured parent otherwise.
Health input: 3.23% × min(salary, 7,703) + 5.17% × (min(salary, 51,910) − 7,703) where positive (K10).

**The hand arithmetic.**

- **H1**, single man, 10,000, March. Year 120,000: 8,412 + 35,880 × 14% (5,023.2) = 13,435.2. Credits 2.25 × 2,904 = 6,534. Tax 6,901.2; a twelfth 575.1. Deduction 7,703 × 1.04% (80.1112) + 2,297 × 4.67% (107.2699) = 187.3811. Health 248.8069 + 118.7549 = 367.5618. Allowance 0. Net 10,000 − 575.1 − 187.3811 − 367.5618 = **8,869.9571**.
- **H2**, single woman, 10,000, March. Credits 2.75 × 2,904 = 7,986. Tax 5,449.2; a twelfth 454.1. Net **8,990.9571**.
- **H3**, father 15,000, registered, requests under (1A); wife a housewife; children aged 3 and 7; June. Year 180,000: 13,536 + 59,280 × 20% (11,856) = 25,392. Children's points 3.5 + 1 = 4.5, worth 13,068 (below the cap of 25,392). Credits 6,534 + 13,068 = 19,602. Tax 5,790; a twelfth 482.5. Deduction 80.1112 + 7,297 × 4.67% (340.7699) = 420.8811. Health 248.8069 + 377.2549 = 626.0618. Allowance: the wife is not insured (s 238 housewife), so both children are in the father's count: 173 + 219 = 392. Net 15,000 − 482.5 − 420.8811 − 626.0618 + 392 = **13,862.5571**.
- **H3b**, the same with the father not registered, claiming under (a)(1): the same tax, 5,790, and net **13,862.5571**.
- **H4**, mother 12,000, not registered, claims under (a)(1); husband at home, insured; a child born 2025 (she elects under (a1)) and one aged 5; January. Year 144,000: 13,536 + 23,280 × 20% (4,656) = 18,192. Children's points 5.5 + 2.5 = 8, worth 23,232, capped at 18,192. Credits 7,986 + 18,192 = 26,178 > 18,192: tax 0. Deduction 80.1112 + 4,297 × 4.67% (200.6699) = 280.7811. Health 248.8069 + 222.1549 = 470.9618. Allowance: both parents insured, children with both: the father's count, and he has no additional-tax income: 173 + 219 = 392. Net 12,000 − 0 − 280.7811 − 470.9618 + 392 = **11,640.2571**.
- **H5**, father 12,000, (1A); wife a housewife; four children aged 16, 13, 10, 6; April. s 121 18,192. Children's points 4 × 1 = 4, worth 11,616. Credits 6,534 + 11,616 = 18,150. Tax 42; a twelfth 3.5. Deduction 280.7811 (April's minimum, 6,443.85, is below the salary). Allowance 173 + 3 × 219 = 830. Net 12,000 − 3.5 − 280.7811 − 470.9618 + 830 = **12,074.7571**.
- **H6**, mother 25,000, registered, (1A); husband at home; children aged 14, 9, 2; July. Year 300,000: 34,992 + 72,000 × 31% (22,320) = 57,312. Children's points 2 + 2 + 4.5 = 8.5, worth 24,684. Credits 7,986 + 24,684 = 32,670. Tax 24,642; a twelfth 2,053.5. Deduction 80.1112 + 17,297 × 4.67% (807.7699) = 887.8811. Health 248.8069 + 894.2549 = 1,143.0618. Allowance (the father's count) 173 + 219 + 219 = 611. Net 25,000 − 2,053.5 − 887.8811 − 1,143.0618 + 611 = **21,526.5571**.
- **H7**, father 70,000, (1A); wife a housewife; children aged 8 and 4; October. Year 840,000: 148,362 + 279,720 × 47% (131,468.4) = 279,830.4. s 121B: 118,440 × 3% = 3,553.2. Children's points 1 + 2.5 = 3.5, worth 10,164. Credits 16,698. Tax 279,830.4 − 16,698 + 3,553.2 = 266,685.6; a twelfth 22,223.8. Income for contributions 51,910 (the maximum): deduction 80.1112 + 44,207 × 4.67% (2,064.4669) = 2,144.5781. Health 2,534.3088. Allowance: the children are in the father's count and he has income chargeable to additional tax: none. Net 70,000 − 22,223.8 − 2,144.5781 − 2,534.3088 = **43,097.3131**.
- **H8**, the same children and salary, the mother earning; husband at home, insured. Children's points 2 + 2.5 = 4.5, worth 13,068. Credits 7,986 + 13,068 = 21,054. Tax 279,830.4 − 21,054 + 3,553.2 = 262,329.6; a twelfth 21,860.8. Allowance: the father's count, and he has no such income: 392. Net 70,000 − 21,860.8 − 2,144.5781 − 2,534.3088 + 392 = **43,852.3131**.
- **H9**, single woman, 5,000, February. Year 60,000: 6,000 < 7,986: tax 0. Income for contributions: the minimum, 6,247.67; deduction 6,247.67 × 1.04% = 64.975768. Health 5,000 × 3.23% = 161.5. Net 5,000 − 64.975768 − 161.5 = **4,773.524232**.
- **H10**, father 7,703 (the threshold), (1A); wife a housewife; a child aged 10; May. Year 92,436: 8,412 + 8,316 × 14% (1,164.24) = 9,576.24. Credits 6,534 + 2,904 = 9,438. Tax 138.24; a twelfth 11.52. Deduction 7,703 × 1.04% = 80.1112 (and at 7,704, 80.1579). Health 248.8069. Allowance 173. Net 7,703 − 11.52 − 80.1112 − 248.8069 + 173 = **7,535.5619**.

**Declined by name** (each asserted with `#ASSERT REFUSED … BECAUSE "…"`):

| household | declined | because | still answered |
| --- | --- | --- | --- |
| H11, as H3 without a separate calculation | the tax, the net | s 65 not encoded | deduction 420.8811; allowance 392 |
| H12, a single father, children 11 and 7 | the tax, the net, the household's month | s 40(b) not encoded | allowance 392 |
| H13, H14, March 2025 and 2027 | everything | the period gate | — |
| H15, a salary not the same each month | the tax, the allowance | fork K1; s 164 not encoded | deduction 187.3811 |
| H16, as H3 with a child turning 18 on 15 June 2026 | the allowance | s 72 not encoded | — |
| H17, as H3 with a wife who has income | everything | one earner only | — |
| H18, a resident foreign-worker woman | the tax | IL-01's s 48A refusal | — |
| H19, a woman whose Part D age is not given | the deduction | Schedule A1 Part D not encoded | — |
| H20, an earner with a credit no row encodes | the tax, the net | ss 35, 45A, 47 and the rest not encoded | deduction 187.3811 |

## 6. Findings

Each is an assertion in `il07-tests-expected-red.l4`, expected to fail; `RECONCILE.md` section 3 has them in full with the proposed row changes.

- **R1 (two assertions; IL-04's open fork F4).** The Institute deducts 7% from an employee above the threshold; Schedule J's column D items sum to 4.67%. On H3's 15,000 that is 590.9012 against IL-04's 420.8811, and a net of 13,692.537 against 13,862.5571: 170.0201 a month.
- **R2 (one assertion; IL-02 against IL-01).** For a resident foreign-worker woman in a separate calculation, IL-01 declines s 36A (s 48A) and IL-02's s 66(c)(4) half point "under s 36A" is 0.5.

Observations, no assertion failing: the enacted 5786 Law confirms IL-03's 2026 brackets from 1 January 2026; the Tax Authority's February 2026 booklet prints the superseded brackets; and IL-06's fork F6 makes the allowance turn on which parent earns (H7: none; H8: 392).

All 113 assertions of `il07-tests.l4` were satisfied on the first run that evaluated them (110 on the first; the three for H20 were added afterwards, with the input they test, and satisfied on their first run).
That shows the composition does what its author worked by hand from the rows' readings; it does not show the rows' readings are right, and an independent test pass (section 10) is the check that could.

## 7. Sources: what was read, fetched and not

**Read**: each row's `BRIEF.md`, `encoding.json`, rule and noun modules, and `NOTES.md` up to and **not including** any section headed "Comparison with Axiom's RuleSpec" (IL-01 stopped before line 249, IL-02 before 220, IL-03 before 227, IL-04 before 447; IL-05 and IL-06 have none); the rows' test modules only for how inputs are supplied (IL-02's `ito66-fixtures.l4`); the two deposited sources, by line, for citation.
**Not read**: any row's `INDEPENDENT-FINDINGS.md`, `DECIDED-ANSWERS.md` or `tests-independent.l4`; anything of the Axiom Foundation or under any path the brief forbids. No web search was made.

**Fetched**, both directly from the Internet Archive (no proxy), into the session scratchpad, not deposited:

| what | URL | retrieved (UTC) | bytes | sha256 | used for |
| --- | --- | --- | --- | --- | --- |
| [booklet-2026] Israel Tax Authority, "לוח עזר לחישוב מס הכנסה ממשכורת ושכר עבודה" for 2026, 36 pp. | `https://web.archive.org/web/20260207101513id_/https://www.gov.il/BlobFolder/generalpage/income-tax-monthly-deductions-booklet/he/generalInformation_income-tax-monthly-deductions-booklet_monthly-deductions-booklet-2026.pdf` | 2026-10-06T22:02:54Z | 610,829 | `282bb886ccae1cc718840127af378fce88ca37ee3b2b9f00ed2cd44467e86285` (row IL-01 recorded the same) | PDF p. 8: the s 121B threshold 721,560 (60,130 a month). PDF p. 7: the superseded bracket table (observation only). |
| Economic Efficiency Law (Legislative Amendments for Achieving the Budget Targets for Budget Year 2026), 5786-2026, Sefer HaChukim 3511 (31 March 2026), 40 pp. | `https://web.archive.org/web/20260718005658id_/https://fs.knesset.gov.il/25/law/25_lsr_12235101.pdf` | 2026-10-06T22:03:38Z (the file's time) | 519,764 | `72244dba261c44d2818f80708fa2dece5d8b99f75e788f48e290942ff4734155` | PDF p. 4 (SH p. 415): ch. C, ss 5-7, the s 121 brackets from 1 January 2026 (evidence for IL-03; RECONCILE.md section 3). |

Text was extracted with `pdftotext -layout`, bidi controls removed; the booklet quotation in `il07-published-figures.l4` has the extractor's spacing.
The Israeli fetch proxy was not used.
Internet Archive availability queries for the 5786 Law and the 5785 freezing Law (`25_lsr_5396578.pdf`) both answered 429; the 5786 Law was then fetched by a capture URL, and the 5785 Law was not tried again (nothing here needs it).

**Unsourced, and so inputs**: the health insurance contribution (the National Health Insurance Law is not deposited); and, in the tests only, the maximum income for the health contribution (K10).

## 8. Open questions for a domain expert

1. K1: for a salary that is the same every month, does the withholding under the 5753-1993 Regulations equal one twelfth of the year's tax, credit points and all?
2. K3: are credit points ever set off against the s 121B additional tax?
3. K5 (IL-06 F5): which tax year's additional-tax liability excludes a parent from the allowance for a given month?
4. K8: is the employee's deduction under s 342(c) taken on the s 348 income (the minimum wage for a low earner, the maximum for a high one), as the capstone reads it?
5. R1 (IL-04 F4): the 7% or the 4.67% above the threshold?
6. H7/H8 (IL-06 F6): does the Institute really deny the allowance when the insured father has additional-tax income, and pay it when the earning mother does?
7. K4: under s 66(c)(1A), is the registered spouse's separate calculation of income from personal exertion a calculation of its own (IL-02 reads that it moves no income)?

## 9. How the composition is built

`RECONCILE.md` section 1 has the design and the measurements behind it: cross-directory IMPORT fails; the rows' 36 modules are vendored and hash-pinned; imports are transitive, so adapters make each reference unambiguous rather than hide names; and how each kind of clash behaves.
`vendor.sh --check` runs first in `check.sh`, and fails if a row has changed since `VENDORED.sha256` was written: a change to a row must be read, re-vendored with `vendor.sh --record`, and the numbers here re-earned.
The vendored copies were taken at commons commits recorded per file in `VENDORED.sha256`; row IL-04's are its v0.2.0, repaired 2026-10-07.

## 10. What was not done

- **No independent test pass** (skill step 8): one session without sub-agents, as briefed. It is the first thing to add; a test author given `BRIEF.md`, `GAPS.md` and the two sources could work the households without reading the pipeline.
- **HG1** not sought.
- **The two fetched PDFs are not deposited**: they sit in the session scratchpad; whether the 5786 Law belongs in the Income Tax Ordinance subject's registers is the lead's call.
- **Not committed**, and `subjects/README.md` and `NOTICE` not updated: the brief forbids any git change and any edit outside this subject.

## Comparison with Axiom's RuleSpec (2026-10-07)

Written by `lad-il-07` (one session, no sub-agents) after this capstone and its independent test pass (`INDEPENDENT-FINDINGS.md`) were deposited, under the semi-cleanroom ruling of 2026-10-06, which held Axiom's encoding back until then.
Nothing above this heading was changed and no `.l4` file was edited: a divergence here is a finding, not a fix.

### What was read

Axiom's side is the local clone `/Volumes/transcend/src/Axiom/rulespec-il` at commit `95c6f32c87c75e318631cbd77c14b840bc536c15` (2026-10-03), read only, not pulled; `git rev-parse HEAD`, `git status --short` and `git log --oneline -3` on the pipeline's path were run, and changed no tracked file.

- In full: `il/statutes/composed/worker-with-children-monthly-net-pipeline.yaml` (761 lines) and its `.test.yaml` (881 lines, 15 cases).
- The modules it imports, to the depth needed for the values it reads: ITO `section-121b.yaml` (whole: the 640,000 parameter and every formula); NII `section-1.yaml` and `section-66.yaml` (whole); ITO `section-34.yaml`, `section-36.yaml`, `section-36a.yaml` (rules and formulas); ITO `section-66.yaml` lines 148-392 (the two ladders' point values); ITO `section-121.yaml`, its rule list and band formulas only, because row IL-03's comparison already ran Axiom's s 121 cases through IL-03 and found all four tax figures equal.
- `.axiom/encoding-manifests/` for those eight modules, provenance fields only (models `gpt-6-astra` for ITO ss 121, 121B, 66 and NII s 66; `gpt-5.6-terra` for ITO ss 34, 36, 36A and NII s 1; all generated 2026-09-06). The pipeline has no manifest, as Axiom says (`docs/ENCODING-GAPS.md:504-515`).
- `docs/ENCODING-GAPS.md`: its heading list, then lines 1-8, 192-250, 253-288, 356-392, 395-430, 462-569 and 666-714.
- `known-missing-money-atoms.yaml` and `known-validation-gaps.yaml` (whole; neither has an entry for the pipeline); `data/coverage/tax-benefit-source-map.json` lines 1-20, 55-80 and 110-145.
- `NOTICE`, and the opening lines of `LICENSE` and `LICENSE-CODE`.

On our side: everything the brief lists, and the "Comparison with Axiom's RuleSpec" sections of the six rows (IL-03's in full; the divergence table of IL-06's; IL-01's, IL-02's, IL-04's and IL-05's by search for the rows bearing on this capstone).

**Read outside that list, said so that a reviewer can weigh it.**
`ls` of `il/statutes/` showed the names of modules the pipeline does not import (ITO ss 120B, 33A; NII ss 67, 68, 334, 337, 342, 348, Schedule J, Schedule K); none was opened.
The heading list of `docs/ENCODING-GAPS.md` showed titles of entries on Schedule J, Schedule K and s 334, among them `schedule-j-rows-do-not-sum-to-printed-totals` (line 598); their bodies were not read, except that a line search of the file for "composed" and "pipeline" printed single lines from outside the ranges above (43, 137, 317, 330, 422, 443, 612, 614), two of them (612, 614) from that Schedule J entry.
`oracle-coverage-pending.yaml` (not on the brief's list) was read at lines 1-11 and searched: it lists the pipeline's outputs among 151 outputs awaiting classification in oracle mappings, consistent with `ENCODING-GAPS.md:687-690`, which says nothing is machine-compared against an external model.

### Licence

`NOTICE` puts the encodings, companion test cases, parameter values and provenance metadata under **CC BY 4.0** (`LICENSE` opens "Attribution 4.0 International") and tooling under Apache 2.0 (`LICENSE-CODE`), as earlier rows found; so the two pipeline files are CC BY 4.0.
Attribution as `NOTICE` suggests it: "Axiom Foundation RuleSpec corpus (CC BY 4.0), https://github.com/TheAxiomFoundation".
They are quoted below only in short snippets that identify a point; nothing of theirs is copied into this encoding.

### Method

Axiom's 15 cases were restated as IL-07 households in the scratch module `axiom-cases.l4` (sha256 `aa884546…43cc`, not deposited), in a scratch copy of this directory whose 36 vendored copies were checked against `VENDORED.sha256` and against their rows' sources (36 of 36 equal), and whose 12 own modules, hashed when copied, still equalled the deposited ones after the run.
It was run once, 2026-10-07T05:59:45Z-05:59:55Z, `JL4_LIBRARY_PATH` unset: 35 `#EVAL`, 0 errors.
**The binary was not the build section 0 records.** `~/.local/bin/l4` now resolves to a file rebuilt at 2026-10-07T05:35:45Z, sha256 `6015a4c3…4a6`, not `64bbcb15…e118`; `check.sh` was not re-run on it.
Every figure it gave equals my hand arithmetic from section 5's figures, worked before the run; its contributions equal what `il07-tests.l4` asserts for the same incomes (420.8811 at 15,000, line 317; 2,144.5781 at the maximum, line 354) and what `INDEPENDENT-FINDINGS.md` reports the capstone giving (654.3811 at 20,000; 67.01604 on June's minimum).

How a case was restated:
Axiom's period is `period_kind: month` from 2026-01-01 to 2026-12-31 and no fixture names a month, so every case is put in **June 2026**.
Axiom supplies two ages per child (reached in the tax year; at the month) and birth-year and maturity-year flags; each was turned into a date of birth giving those ages on 1 June 2026 and in tax year 2026.
Axiom's bound is "separate calculation (חישוב נפרד) assumed elected", and it models no spouse (pipeline lines 137-139), so the earner is married, registered, and requests under ITO s 66(c)(1A), as in H3, H6 and H8: a working mother's husband is at home and insured, a working father's wife is a housewife.
The health input is 0.
Axiom's net is "net of income tax and inclusive of child allowance only" (pipeline lines 178-181), that is salary − tax/12 + allowance, so ours is compared on the same sum, which is our net plus the national insurance and the health input.
The Axiom engine was not run; its expected values are its fixtures' own.

### The two pipelines

| | IL-07 | Axiom's composed pipeline |
| --- | --- | --- |
| question | the monthly net income, in a month of 2026, of a household with one employed resident parent | "Composed monthly net income for an employed parent with children" (pipeline line 28) |
| period | months of 2026; 2025 and 2027 refused by name (section 3) | every rule `effective_from: '2026-01-01'` with no end (lines 125-135); a later month is answered on the caller's figures |
| household | one earner; a spouse with no income, or none; any number of children; a single parent with children declined (s 40(b)) | one earner; at most two children; separate calculation assumed; no spouse fact (lines 137-146; `ENCODING-GAPS.md:522-534`) |
| income tax | IL-03 s 121 and s 121B, less IL-01 ss 34, 36, 36A, IL-02 s 66(c) and the s 37 half point, set off to nil, s 121B added after (K3) | the same order: `max(0, income_tax - annual_credit_amount_ils) + total_additional_tax` (line 615) |
| s 121B(a) amount | 721,560, the Tax Authority's 2026 figure (`il07-published-figures.l4:51-53`) | 640,000, the printed figure, in every year (`section-121b.yaml:33-50`; pipeline lines 120-122) |
| credit point | 2,904, IL-03's s 120B(e)(1) from IL-01's published 2025 value (K2) | 2,904, a supplied input, taken from OECD TaxBEN 2025 (`ENCODING-GAPS.md:368`) |
| the month's tax | one twelfth of the year's, declined if the salary varies (K1) | one twelfth, "for presentation" (line 178) |
| national insurance | IL-05 s 348 with Schedule K, IL-04 Schedule J column D, IL-05 s 342(c) | none (`ENCODING-GAPS.md:666-684`) |
| health | a caller's figure | none (the National Health Insurance Law is not in Axiom's corpus, same entry) |
| child allowance | IL-06 ss 65-68 on the first of the month, s 67 across both parents, s 66's exclusion joined to the same year's s 121B (K5), birth and 18th-birthday months declined (K6) | s 66 with s 65(a)'s proviso per child (age at the month, presence in Israel) and s 68(a), every child in the earner's count (lines 616-711); basic amounts supplied, and the printed 150 / 188 reported beside them |
| refusals | 13 of its own and the rows' | none; what is out of scope is bounded in prose, not refused |

What each takes as an input, beyond the salary and the children: IL-07 takes sex, date of birth, the ITO and NII residences, Chapter 11 insurance, foreign-worker and Area status, the full-adult minimum wage, the Part D age, the "no unencoded credit" flag, the spouse's facts, which spouse is registered (s 64B), the s 66 claim or request, the s 37 entitlement, the (a1) election and the health figure.
Axiom takes sex, ITO residence, "insured parent", age 60, books of account, the credit-point value, the two basic amounts, and per child two ages, two year flags and presence in Israel.

### Divergences

Classes: ours wrong, theirs wrong, genuine ambiguity (the text supports both), scope difference, representational difference (same answer, different shape).
`ITO` and `NII` line numbers are lines of the deposited sources, as in `GAPS.md`; "pipeline" is Axiom's YAML.

| id | topic | IL-07 | Axiom | source | class | repair to ours |
| --- | --- | --- | --- | --- | --- | --- |
| X1 | the s 121B(a) amount for 2026 | 721,560 | 640,000; its fixtures' additional tax is 3% above it | ITO 4335 makes "הכנסה החייבת במס נוסף, כמשמעותה בסעיף 121ב" an income ceiling; 4338 adjusts income ceilings every 1 January; 4344 fixes 2025-2027 at the 1 January 2024 figure after rounding; the note at 4456 gives 640,000 as "נקוב לשנת 2017" and 721,560 for 2024-2027 | **theirs wrong**, conceded: "a household between the nominal and the indexed threshold is shown as liable here when it would not be in the year" (`ENCODING-GAPS.md:276-288`). Its `no-executable-oracle` entry still calls the same difference "a fact about the statute" (line 710); on 4335, 4338 and 4344 it is not | none |
| X2 | NII s 66's exclusion between 640,000 and 721,560 | not excluded | excluded: case 5 (720,000 a year) withholds 392 | NII 814 excludes a parent "שיש לו הכנסה החייבת במס נוסף כמשמעותה בסעיף 121ב"; with X1, a parent at 720,000 has none in 2026 | **theirs wrong**, by X1. Case 5 (`high_earner_mother_…`) is the one fixture that asserts the allowance withheld, and Axiom's gap file says "the composed pipeline's high-earner fixture turns on it" (`ENCODING-GAPS.md:269-272`); on the text the exclusion does not reach that household in 2026 | none |
| X3 | what "net" deducts | income tax, national insurance, health (an input) | income tax only; "It is not take-home pay" (line 181) | NII 3661 (s 342(c)(1), the employer's deduction); the health law is outside both bundles | **scope difference**, stated by both | none |
| X4 | whose count a child is in (NII s 67) | IL-06's s 67: with an insured husband at home, an earning mother's children are in his count | not applied; every child in the earner's count (lines 172-176; `ENCODING-GAPS.md:536-541`) | NII 818 "יבוא במנין האב המבוטח זולת אם הוא נמצא עם האם בלבד"; 814 attaches s 66's exclusion to the parent | **scope difference**. It shows only where a parent has additional-tax income: case 15's mother at 74,000 gets 392 here (her husband's count) and 0 by Axiom's formula (not asserted). Ours is the literal reading, which IL-06 F6 and section 8 Q6 leave open | none |
| X5 | a single parent with children | declined, naming s 40(b) | no spouse fact, so a single parent is computed with s 66(c)'s points; s 40 is listed as not encoded and single parents as outside the pilot (`ENCODING-GAPS.md:425-429`) | ITO 2460-2476 (s 66(c), spouses in a separate calculation); 1632-1647 (s 40(b)) | **scope difference**: neither encodes s 40(b); Axiom answers where it says it cannot | none |
| X6 | the separate calculation | the (a)(1) claim or the (c)(1A) request is an input; without one, declined as s 65 (H11) | assumed elected; Axiom's s 66 module has no (c)(1A) (row IL-02, AX-9) | ITO 2456, 2462, 2448 | **scope difference** | none |
| X7 | credits no row encodes (ss 35, 45A, 47 and the rest) | an input; FALSE declines the tax | none; the tax is computed as if there were none (coverage map lines 55-56; `ENCODING-GAPS.md:682-683`) | ITO 1714-1805 (ss 45A, 47) | **scope difference**: both leave them; Axiom's tax is too high for an employee who contributes to a pension, with no sign of it | none |
| X8 | the mother's (a1) election | applied (IL-02; H4) | not applied: birth-year points always in the birth year (`ENCODING-GAPS.md:417-423`) | ITO 2467 | **scope difference** | none |
| X9 | a month in which a child is born or turns 18 | declined, naming s 72 (K6), except an 18th birthday on the 1st, answered as excluded (independent finding F3, recorded) | answered on the caller's whole-number `child_N_age_at_month_years` (lines 632-635); no date, no s 72 | NII 853-856; 854 "עד 15 בחודש … החל ב־1 באותו חודש … יסתיים ביום האחרון של החודש שבו נפסקה הזכאות" | **scope difference**: neither encodes s 72. The text decides these months; Axiom's answer is right only if the caller has applied s 72(a) in choosing the age and the children (see below) | none new (F3's repair stands) |
| X10 | months after 2026 | refused | answered on supplied figures | ITO 4344 freezes the s 121 amounts for 2027, 4345 adjusts them from 2028 | **scope difference**; Axiom's s 121 is right for 2027 and wrong from 2028 (row IL-03, X04), and X1 applies throughout | none |
| X11 | a child's age | dates of birth; IL-02 takes the tax year of birth (ITO 1645, 2471) | two ages and two year flags supplied per child | ITO 2466, 2471 | **representational**. Axiom's inputs can disagree without a diagnostic: a mother's child of 18 without the maturity flag falls to `else: 0` (lines 496-506), 0 points where ITO 2466 gives ½ | none |
| X12 | the credit-point value | derived through s 120B(e)(1) from the Tax Authority's 2025 figure | supplied, from OECD TaxBEN | ITO 1563, 4344 | **representational**: the same 2,904 | none |
| X13 | the insured parent | from Chapter 11 insurance, NII residence and s 238 (IL-06) | an input, `taxpayer_is_an_insured_parent` | NII 801-803 | **representational** | none |
| X14 | a child abroad | every child in Israel (`BRIEF.md`; `il07-adapter-il06.l4:120-121`) | `child_N_is_present_in_israel`, per child | NII 807, 809 | **scope difference**: Axiom covers what this capstone pins (case 10) | none |
| X15 | a foreign worker (ITO s 48A) | IL-01's refusal (H18) | no input; full points | ITO 1810-1812 | **scope difference** (row IL-01, X02) | none |
| X16 | number of children | any | at most two | — | **scope difference** | none |

**Totals: 16. Ours wrong 0; theirs wrong 2 (X1, X2, one cause); genuine ambiguity 0; scope difference 11; representational 3.**

Where both answer, they read the text the same way: the 2026 s 121 figures (ITO 4350-4358); 2 points under s 34, ¼ under s 36, ½ under s 36A; every rung of both ladders, including ½ for the mother and nothing for the father in the year of majority (ITO 2466, 2474-2476); the credits set off against the s 121 tax only and never below nil, s 121B added after (K3); one twelfth of the year's tax (K1); s 66's exclusion turning on the s 121B liability of the tax year in which the month falls (K5, IL-06 F5); and a child counted for the allowance while under 18 and in Israel (NII 807).
K3 and K5 were reached separately by both, which is evidence for those readings, not proof.

### Axiom's 15 cases through IL-07

All in June 2026; IL-07's "Axiom's sum" is salary − one twelfth + allowance.
Every child's points agree: in each case where Axiom asserts them (all but 14 and 15), its two per-child figures add up to IL-07's children's points.

| # | Axiom case | the household here | Axiom: tax for the year; allowance; net | IL-07: tax for the year; twelfth; allowance; NI | IL-07, Axiom's sum | result |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | `working_mother_two_children_aged_two_and_eight_fifteen_thousand_a_month` | mother, 15,000; children born 2024-03-10, 2018-02-20 | 0; 392; 15,392 | 0; 0; 392; 420.8811 | 15,392 | match |
| 2 | `working_father_two_children_aged_two_and_eight_fifteen_thousand_a_month` | father, 15,000; the same children | 2,886; 392; 15,151.5 | 2,886; 240.5; 392; 420.8811 | 15,151.5 | match |
| 3 | `minimum_wage_working_mother_two_children_aged_two_and_eight` | mother, 5,880.02 | 0; 392; 6,272.02 | 0; 0; 392; 67.01604 | 6,272.02 | match (see below) |
| 4 | `woman_with_no_children_fifteen_thousand_a_month` | single woman, 15,000 | 17,406; 0; 13,549.5 | 17,406; 1,450.5; 0; 420.8811 | 13,549.5 | match |
| 5 | `high_earner_mother_two_children_sixty_thousand_a_month` | mother, 60,000 | s 121B 2,400; 198,968.4; 0; 43,419.3 | s 121B 0; 196,568.4; 16,380.7; 392; 2,144.5781 | 44,011.3 | **diverge**, by 592 a month: X1 (200) and X2 (392). With 640,000 put into IL-03's s 121B, IL-07 gives Axiom's 2,400; with a husband who is not insured, the children are in her count (2) and the allowance is still 392, so s 67 plays no part |
| 6 | `working_mother_child_in_its_birth_year_and_child_in_its_maturity_year` | mother, 15,000; born 2026-02-10 and 2008-03-10 | 8,694; 173; 14,448.5 | 8,694; 724.5; 173; 420.8811 | 14,448.5 | match |
| 7 | `working_father_child_in_its_birth_year_and_child_in_its_maturity_year` | father, 15,000; the same children | 11,598; 173; 14,206.5 | 11,598; 966.5; 173; 420.8811 | 14,206.5 | match |
| 8 | `working_mother_children_aged_three_and_five_twenty_thousand_a_month` | mother, 20,000; born 2023-02-10, 2021-01-15 | 13,302; 392; 19,283.5 | 13,302; 1,108.5; 392; 654.3811 | 19,283.5 | match |
| 9 | `working_mother_child_past_its_maturity_year_and_child_aged_eight` | mother, 15,000; born 2007-03-10, 2018-02-20 | 11,598; 173; 14,206.5 | 11,598; 966.5; 173; 420.8811 | 14,206.5 | match |
| 10 | `working_mother_two_children_the_elder_one_outside_israel` | — | 0; 173; 15,173 | — | — | **could not be run**: IL-07 has no input for a child abroad (X14). Its tax is case 1's |
| 11 | `working_mother_two_children_aged_seventeen_and_eight` | mother, 15,000; born 2009-02-10, 2018-02-20 | 5,790; 392; 14,909.5 | 5,790; 482.5; 392; 420.8811 | 14,909.5 | match |
| 12 | `working_mother_child_turning_three_this_year_and_child_aged_eight` | mother, 15,000; born 2023-09-10 (2 in June, 3 in the tax year), 2018-02-20 | 1,434; 392; 15,272.5 | 1,434; 119.5; 392; 420.8811 | 15,272.5 | match |
| 13 | `working_mother_maturity_year_child_before_its_eighteenth_birthday` | mother, 15,000; born 2026-02-10 and 2008-09-10 (17 in June) | 8,694; 392; 14,667.5 | 8,694; 724.5; 392; 420.8811 | 14,667.5 | match |
| 14 | `woman_aged_sixty_with_no_children_fifteen_thousand_a_month` | single woman born 1966-01-15, 15,000 | asserts only the taxable income (180,000) and judgments (60 reached; not an insured parent; no additional tax) | 17,406; 1,450.5; 0; 420.8811 | 13,549.5 | match on what Axiom asserts; the age changes nothing for a salary (ITO 4354) |
| 15 | `mother_above_the_additional_tax_threshold` | mother, 74,000 | asserts only the taxable income (888,000), both children under s 65, and additional-tax income "holds" | s 121B 4,993.2; 280,521.6; 23,376.8; 392 (her husband's count; 0 with a husband who is not insured); 2,144.5781 | 51,015.2 | match on what Axiom asserts; X1 sits underneath (Axiom's formula would charge 7,440) and X4 decides the allowance |

**Matched 13 (11 on every comparable figure, 2 on the few Axiom asserts), diverged 1, could not be run 1.**
No case is dated outside 2026, so none was a question of the period.

Case 3 calls 5,880.02 the minimum wage; it is below the full adult minimum wage row IL-05 sourced for every month of 2026 (6,247.67 from 1 April 2025, 6,443.85 from 1 April 2026; `nii-il05-published-figures.l4:70-72`), and the test file records no source for it.
It changes nothing Axiom computes; here s 348(b) (NII 3765) takes the contributions on June's 6,443.85, not on the 5,880.02 paid.

### Our independent findings, on Axiom's side

| finding (`INDEPENDENT-FINDINGS.md`) | Axiom's pipeline |
| --- | --- |
| F1, Schedule J column D above the threshold, 7.00 printed against 4.67 summed | not reached: no contributions are deducted. Axiom's own s 337 and Schedule J modules (not read here) take the printed totals, by row IL-04's comparison (its D5), which is the independent tester's and the Institute's reading; Axiom records the mismatch as `unexplained` (`ENCODING-GAPS.md:598`, heading only read) |
| F2, a child born, or turning 18, after the 1st | answered without s 72 (X9). In H25's shape (18 on 10 June) a caller who enters 18 gets 173 and one who enters 17 gets 392, which is s 72(a)'s answer; in H28's (born 16 September) a caller who lists the newborn gets 392 where s 72(a) gives 173 |
| F3, an 18th birthday on the 1st | the same answer as IL-07's if the caller enters 18 for the month (0 where the independent tester reads s 72(a) as paying 173); Axiom shares the defect through its input |
| F4, a non-resident | answers the tax as IL-07 does: s 34 and s 36 turn on `taxpayer_is_israeli_resident`, s 36A does not (`section-34.yaml`, `section-36.yaml`, `section-36a.yaml`); computes no contributions, so never meets s 335(a) (NII 3611) |
| F5, s 348(b)'s minimum | not reached: no contributions; the coverage map lists s 348(b), (d) and (e) as not encoded (`tax-benefit-source-map.json:124`). Case 3 is the one fixture it would touch |
| M1, children's names must be unique | no counterpart: Axiom's children are two numbered slots |

### Our gaps (`GAPS.md`), on Axiom's side

Axiom encodes none of them, and where IL-07 declines, Axiom mostly answers on an assumption it states in prose.

| `GAPS.md` | provision | Axiom |
| --- | --- | --- |
| 1 | ITO ss 45A, 47 | not encoded (coverage map line 56; `ENCODING-GAPS.md:682`); no input; the tax is computed as if there were none (X7) |
| 2 | ITO s 40(b) | not encoded; single parents "cannot be computed by this pilot" (`ENCODING-GAPS.md:428`), but nothing refuses one (X5) |
| 3 | ITO ss 64B, 65 | a separate calculation is assumed (X6) |
| 4 | the health contribution | not deducted; the Law is not in Axiom's corpus (`ENCODING-GAPS.md:666-680`) |
| 5 | ITO s 164 and the 5753-1993 Regulations | the same one twelfth, "for presentation" (`ENCODING-GAPS.md:533`); no condition that the salary is the same every month |
| 6 | NII s 72 | not encoded (X9) |
| 7 | ITO ss 37-39 | s 66(c)(2)'s half point deferred (`ENCODING-GAPS.md:406-407`); no input |
| 8 | ITO s 35 and the other status credits | not encoded; silent (X7) |
| 9 | NII s 335 | not reached (no contributions) |
| 10 | NII Schedule A1 Part D | not reached; listed as not encoded (coverage map line 125) |
| 11 | the Minimum Wage Law | not reached; see case 3 |
| 12 | ITO ss 48, 48A | no input; full points (X15) |
| 13 | residence and status | inputs in both |

### What Axiom covers that IL-07 does not, and the reverse

**Axiom, not IL-07:** a child abroad (per-child presence, case 10); the printed 150 / 188 allowance reported beside the amount paid; months after 2026 on supplied figures (right for 2027 on s 121, X10); the s 121(b)(1) age of 60 and the (b)(2) books exception as inputs (neither matters for a salary); a verbatim source excerpt on every rule.
**IL-07, not Axiom:** national insurance deducted and the health contribution taken, so a net nearer take-home pay; s 67 across both parents, which surfaces IL-06 F6 (H7 against H8); the s 121B amount in force in 2026; the credit-point value from the regulator through s 120B(e)(1); any number of children; dates of birth in place of ages the caller works out; the (a1) election; both routes into a separate calculation; named refusals for s 65, s 40(b), the unencoded credits, s 48A, a varying salary, the s 72 months, a spouse with income and every other year; and an independent test pass, which found F1-F4 against this capstone.

One note on Axiom's own records, not a divergence: `ENCODING-GAPS.md:564-566` says a child's age is "one number for the case", but the pipeline at this commit carries two ages per child and reads the one at the month for s 65 (pipeline lines 72-81, 632-635); the gap entry lags the file it describes.

### Bottom line

Where both pipelines answer the same household they compute the same income tax, the same points for every child and the same allowance: in eleven of the twelve cases where Axiom states a tax and an allowance and IL-07 could run the household, and on every figure Axiom asserts for cases 14 and 15, which state neither.
They also made the same reading at each fork they share (K1, K3, K5).
The one case that differs, case 5, is Axiom's error and Axiom concedes it: it applies the 2017 figure of 640,000, which ss 120A and 120B (ITO 4335, 4338, 4344) put at 721,560 for 2026.
That case is also the fixture Axiom's gap file points to for NII s 66's exclusion of a high earner, and on the text the exclusion does not reach it in 2026: the household at 720,000 keeps its 392, whichever parent counts the children.
The two answer different questions: Axiom's "net" leaves out national insurance and health by design and says so; IL-07 deducts the first and takes the second as an input.
Beyond that, Axiom answers across facts IL-07 declines (single parents, pension credits, s 65, s 48A, the s 72 months), bounding them in prose rather than refusing them.
Nothing Axiom's pipeline does shows IL-07 wrong on the Hebrew, and nothing here proposes a repair.
The open items stay those already recorded: the independent pass's F1-F4, which Axiom's pipeline does not reach except that it shares F3's shape; and section 8's questions, three of which (K1, K3, K5) it answers the same way without settling them.
