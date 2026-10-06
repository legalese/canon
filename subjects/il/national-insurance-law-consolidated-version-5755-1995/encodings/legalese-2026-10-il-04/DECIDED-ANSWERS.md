# IL-04 decided answers, written from the Hebrew source before opening the encoding

Finished: Tue Oct  6 14:53:53 UTC 2026 (from `date -u`).
Author: fid-il-04, independent test author (one session, no sub-agents).
Before writing this file I had read only: `l4-ide/skills/encoding-a-subject/references/second-pass.md`, `l4-ide/skills/writing-l4-rules/SKILL.md`, its `references/source-patterns/11-when-the-encoding-cannot-answer.md`, the encoding's `BRIEF.md`, a plain `ls` of the encoding directory, the source file at lines 115-234, 3590-3639 and 4695-4759, and one page of btl.gov.il (cited below).
I had not opened `NOTES.md`, `encoding.json`, any `.l4` file, `check.sh` or `tools/`.

Source: `registers/source-bundle/national-insurance-law-consolidated-version-5755-1995.he.wiki.txt`, sha256 `78bf47ee…2a97`, line numbers below are into that file.
Money is NIS; a rate written `5.89` is a percentage as Schedule J prints it; an amount is the exact rational (the text in scope states no rounding rule, so I round nothing).

## 0. Inputs I choose, and where they come from

| input | value | provenance |
| --- | --- | --- |
| average wage (השכר הממוצע), 2026 | 13,566 | editors' note at line 226, `השכר הממוצע לפי הגדרה זאת: בשנת 2026, 13,566 ש״ח` — an aid, not the Law; taken as an input |
| reduced collection threshold (מדרגת גבייה מופחתת), 2026 | 7,703 | editors' note at line 3605, `בשנת 2026, 7,703 ש״ח`; also printed by the National Insurance Institute, https://www.btl.gov.il/Insurance/Rates/Pages/לעובדים%20שכירים.aspx, fetched 2026-10-06 ~14:50 UTC: "7,703 ש"ח" from 01.01.2026 |
| CPI last published before 1 Jan 2026 / before 1 Jan 2027 | 100 / 102 | invented inputs, so T(2027) = 7,703 × 1.02 = 7,857.06 |
| CPI last published before 1 Jan 2028 | 102 | invented (no change), so T(2028) = 7,857.06 |
| average wage on 1 Jan 2028 / 1 Jan 2029 | 13,566 / 14,000 | invented, for the s 334(a)(2) arm |
| the Schedule A (לוח א׳) amount for limb (3) of "self-employed" | 2,000 | invented; Schedule A is out of scope (BRIEF), so it is an input |

The same btl.gov.il page prints, for salaried employees in 2026: employee 1.04% on the reduced part and 7% on the full part; employer 4.51% and 7.6%.
Composite: 5.55% and 14.60%.
I record this because it bears on the totals question in section 3; it is not where any expected value below comes from.

## 1. Which table governs which contribution month (the vintage selector)

Sources of the dates: the Schedule's heading at line 4711, `שיעור דמי ביטוח בעד אפריל שנת 2011 ואילך`; the editors' notes `(הוראת שעה לשנים 2025–2026)` at line 4714 over the first table and `(הנוסח הקבוע)` at line 4732 over the second; the notes `(הוראת שעה בשנים 2024 עד 2027: …)` inside cells at lines 4723, 4730, 4741, 4748; s 334(a)(1)-(2) at lines 3606-3607.
The dates of the two tables live only in editors' notes, which the BRIEF calls aids; I rely on them because nothing else in the source tells the two tables apart.

| # | contribution month | expected |
| --- | --- | --- |
| V1 | March 2011 | REFUSE. Before the Schedule's own heading, "for April 2011 onward". |
| V2 | December 2024 | REFUSE. Neither table is shown as in force; the text before the 5785 amendments is not in the source. |
| V3 | January 2025, December 2025 | REFUSE, per the BRIEF's rule (answers from January 2026). My own reading: the source arguably *does* answer 2025 (the first table is "for 2025–2026", and 7,522 is the unupdated 2025 figure, since s 334(a)(1) first updates it in 2026), and btl.gov.il dates 1.04%/4.51% from 01.01.2025. But the commencement of the 5785 amending Laws (תשפ״ה־3, ־7, ־8, line 4713) is not in the source. The refusal is the BRIEF's scope choice, not something the text forces. |
| V4 | January 2026, December 2026 | the temporary table (lines 4715-4731), with the 2024-2027 notes applied: called **V2026** below |
| V5 | January 2027, December 2027 | the permanent table (lines 4733-4749), with the 2024-2027 notes applied: **V2027** |
| V6 | January 2028, June 2035 | the permanent table without the notes: **V2028+** |

## 2. Every cell of Schedule J, per vintage

Columns, from the header rows at lines 4716-4719 and 4734-4737:

- C↑e, C↑s, C↑n: column ג׳, "on the part above the reduced collection threshold", for an employee (לעובד), a self-employed person (לעובד עצמאי), an insured who is neither (למבוטח שאינו עובד ואינו עובד עצמאי).
- C↓e, C↓s, C↓n: column ג׳, "on the part not above the threshold", same three.
- D↑: column ד׳, the deduction from the employee's wage for s 342(c), upper band. **In the temporary table the band is `על חלק השכר העולה על 60% מהשכר הממוצע` (above 60% of the average wage, line 4718); in the permanent table it is above the reduced collection threshold (line 4736).**
- D↓: column ד׳, lower band, "not above the reduced collection threshold", in both tables.
- E: column ה׳, the Treasury allocation under s 32(c1).

`–` is the schedule's dash. I read a dash as "the schedule states no rate", not 0. Where a person pays that branch, the answer is REFUSE; where the person does not pay it (the s 335 question, out of scope), there is no contribution and nothing to look up.

### V2026 (contribution months in 2026)

| item | branch | C↑e | C↑s | C↑n | C↓e | C↓s | C↓n | D↑ (>60% AW) | D↓ | E |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | אימהות maternity | 1.40 | 0.94 | – | 0.24 | 0.37 | – | 0.87 | 0.10 | 0.09 |
| 2 | אימהות – neither | – | – | 0.16 | – | – | 0.16 | – | – | – |
| 3 | ילדים children | 2.08 | 2.74 | 1.67 | 1.68 | 0.92 | 1.65 | – | – | 0.08 |
| 4 | נפגעי עבודה work injury | **2.06** (1.96 with note 2024-2027: 2.06) | 0.78 | – | 0.60 | 0.26 | – | – | – | 0.03 |
| 5 | נפגעי תאונות accidents | 0.13 | 0.09 | 0.07 | 0.04 | 0.05 | 0.06 | 0.07 | 0.03 | 0.02 |
| 6 | אבטלה unemployment | 0.33 | – | – | 0.06 | – | – | 0.21 | 0.02 | 0.06 |
| 7 | insolvency | 0.04 | – | – | 0.01 | – | – | – | – | 0.02 |
| 8 | נכות disability | 2.28 | 2.12 | 1.31 | 0.62 | 0.73 | 1.31 | 1.86 | 0.29 | 0.10 |
| 9 | סיעוד long-term care | 0.28 | 0.21 | 0.14 | 0.08 | 0.08 | 0.14 | 0.14 | 0.03 | 0.02 |
| 10 | old age & survivors | 5.89 | 5.95 | 3.65 | 2.22 | 2.06 | 3.60 | 1.52 | 0.57 | 0.25 |
| | printed total | **14.60** (14.50, note 2024-2027: 14.60) | 12.83 | 7.00 | 5.55 | 4.47 | 6.92 | **7.00** | 1.04 | 0.67 |
| | sum of rows (by hand, and checked by script) | **14.49** | 12.83 | 7.00 | 5.55 | 4.47 | 6.92 | **4.67** | 1.04 | 0.67 |

### V2027 (contribution months in 2027)

| item | C↑e | C↑s | C↑n | C↓e | C↓s | C↓n | D↑ (>T) | D↓ | E |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1.40 | 0.94 | – | 0.16 | 0.24 | – | 0.87 | 0.04 | 0.09 |
| 2 | – | – | 0.16 | – | – | 0.11 | – | – | – |
| 3 | 2.08 | 2.74 | 1.67 | 1.47 | 0.59 | 1.10 | – | – | 0.08 |
| 4 | **2.06** | 0.78 | – | **0.47** | 0.17 | – | – | – | 0.03 |
| 5 | 0.13 | 0.09 | 0.07 | 0.02 | 0.03 | 0.04 | 0.07 | 0.01 | 0.02 |
| 6 | 0.33 | – | – | 0.04 | – | – | 0.21 | 0.01 | 0.06 |
| 7 | 0.04 | – | – | 0.01 | – | – | – | – | 0.02 |
| 8 | 2.28 | 2.12 | 1.31 | 0.37 | 0.47 | 0.87 | 1.86 | 0.11 | 0.10 |
| 9 | 0.28 | 0.21 | 0.14 | 0.05 | 0.05 | 0.09 | 0.14 | 0.01 | 0.02 |
| 10 | 5.89 | 5.95 | 3.65 | 1.67 | 1.32 | 2.40 | 1.52 | 0.22 | 0.25 |
| printed total | **14.60** | 12.83 | 7.00 | **3.95** | 2.87 | 4.61 | **7.00** | 0.40 | 0.67 |
| sum of rows | **14.49** | 12.83 | 7.00 | **4.26** | 2.87 | 4.61 | **4.67** | 0.40 | 0.67 |

### V2028+ (contribution months from January 2028)

As V2027 except item 4: C↑e **1.96**, C↓e **0.37**; printed totals C↑e **14.50**, C↓e **3.85**; sums of rows C↑e **14.39**, C↓e **4.16**.

Cell count: 3 vintages × 10 items × 9 columns = 270 cell scenarios (of which 3 × 25 = 75 are dashes, each expected to yield no rate), plus 3 × 9 printed totals.

## 3. The totals: which I take as the law, and why

Three columns do not add up, in this unofficial consolidation:

| column | tables | sum of rows | printed total | difference |
| --- | --- | --- | --- | --- |
| C↑e | both, every vintage | 14.49 (14.39 from 2028) | 14.60 (14.50 from 2028) | rows 0.11 short |
| C↓e | permanent only (V2027, V2028+) | 4.26 (4.16 from 2028) | 3.95 (3.85 from 2028) | rows 0.31 over |
| D↑ | both | 4.67 | 7.00 | rows 2.33 short |

Every other column adds up exactly, in every vintage.

**I take the rows as the law**, for these reasons, all from the text:
s 337(a)(1) gives "שיעורי דמי הביטוח החודשיים לפי סעיף 335" — the rates of the contributions *under s 335* — as the percentages in Schedule J;
s 335 levies contributions branch by branch ("ישתלמו בעדו דמי ביטוח אימהות", "… ילדים", and so on, lines 3611-3619) and (י) makes them cumulative;
so a person's liability is the sum of their branch liabilities, each at its row's rate, and no provision in scope gives the totals row any operative effect.

**The caveat, which I do not hide:** the National Insurance Institute's published 2026 composite rates (5.55% and 14.60% for an employee; 1.04% and 7% for the employee's own part) equal the *printed totals*, not the row sums.
That is evidence that this consolidation's *rows* in C↑e and D↑ carry an error (or that the Law itself does), and only the Reshumot text can settle which.
So the aggregate in those three columns is a genuine ambiguity of the source bundle.
My expected aggregates below use the rows; an encoding that uses the printed totals, or refuses the aggregate, disagrees with me on a recorded ambiguity, not on an obvious error.
Per-branch amounts do not depend on this at all, and I test those heavily.

## 4. The reduced collection threshold, s 334(a)

Text, line 3605-3607: `סכום של 7,522 שקלים חדשים …, כשהוא מעודכן ב־1 בינואר של כל שנה כלהלן: (1) בשנים 2026 עד 2028 – לפי שיעור עליית המדד שפורסם לאחרונה לפני 1 בינואר, לעומת המדד שפורסם לאחרונה לפני 1 בינואר של השנה הקודמת; (2) משנת 2029 ואילך – לפי שיעור עליית השכר הממוצע, המעודכן ב־1 בינואר, לעומת השכר הממוצע ב־1 בינואר של השנה הקודמת.`

| # | scenario | expected |
| --- | --- | --- |
| T1 | 2026 | 7,703 (the published figure, section 0) |
| T2 | 2026 recomputed from the formula, CPI ratio 1.024 | 7,522 × 1.024 = 7,702.528 exactly (the text states no rounding; 7,703 is the regulator's rounding). Only if the encoding computes 2026 rather than taking it as published. |
| T3 | 2027, CPI 100 → 102 | 7,703 × 102/100 = 7,857.06 |
| T4 | 2028, CPI 102 → 102 | 7,857.06 (no change) |
| T5 | 2029, AW 13,566 → 14,000 (and whatever the CPI did) | 7,857.06 × 14,000/13,566 = 154060/19 ≈ 8,108.421053; the CPI is irrelevant from 2029 |
| T6 | 2028 update uses the CPI, not the AW | with CPI unchanged and AW up, T(2028) = T(2027) |
| T7 | 2027 with the CPI *falling* (102 → 101) | REFUSE (genuine ambiguity). The text updates "by the rate of the rise of the index" (שיעור עליית המדד) and does not say what happens on a fall, unlike laws that say so expressly. |
| T8 | A year whose CPI or AW inputs are missing | an input, not a refusal and not a default |

## 5. Employee, s 337(a)(1), V2026, T = 7,703, all the branches an employee pays (items 1, 3-10)

Rule: for each branch, C↓e × min(W, T) + C↑e × max(0, W − T); sum over branches.
Using the rows: 5.55% below and 14.49% above (section 3); the printed-total alternative is given in brackets.

| # | monthly income W | expected (rows) | [printed totals] |
| --- | --- | --- | --- |
| E1 | 0 | 0 | 0 |
| E2 | 7,702 (just below T) | 427.461 | same |
| E3 | 7,703 (at T: "שאינו עולה על" — the whole of it is the reduced part) | 427.5165 | same |
| E4 | 7,704 (just above) | 427.6614 | [427.6625] |
| E5 | 10,000 | 760.3518 | [762.8785] |
| E6 | 60,000 | 8,005.3518 — the maximum insurable income (s 345, Schedule K) is out of scope, so s 337 applies to the income it is given | [8,062.8785] |

Per branch, W = 10,000, V2026 (no totals question arises):

| # | branch | expected |
| --- | --- | --- |
| E7 | 10 old age & survivors | 2.22% × 7,703 + 5.89% × 2,297 = 306.2999 |
| E8 | 4 work injury (2.06 under the 2024-2027 note) | 0.60% × 7,703 + 2.06% × 2,297 = 93.5362 |
| E9 | 6 unemployment | 12.2019 |
| E10 | 1 maternity | 50.6452 |
| E11 | 3 children | 177.188 |
| E12 | 8 disability | 100.1302 |
| E13 | 2 (maternity for the neither-column) asked for an employee | no rate (dash): REFUSE, or not reachable |

## 6. Self-employed, s 337(a)(2), V2026, per monthly period, branches 1, 3, 4, 5, 8, 9, 10

s 337(a)(2): `מהכנסתו השנתית כשהיא מחולקת לתקופות שנקבעו לצורך תשלום מקדמות` — annual income divided into the periods fixed for advances. The periods are fixed outside the scope (regulations; s 336's default is monthly), so the period is an input; I use monthly periods.
Rates: 4.47% below, 12.83% above (rows = printed).

| # | income per monthly period | expected |
| --- | --- | --- |
| S1 | 7,702 | 344.2794 |
| S2 | 7,703 | 344.3241 |
| S3 | 7,704 | 344.4524 |
| S4 | 10,000 | 639.0292 |
| S5 | annual 120,000 in 12 monthly periods | 639.0292 per period; 7,668.3504 for the year |
| S6 | item 10 only, 10,000 | 2.06% × 7,703 + 5.95% × 2,297 = 295.3533 |
| S7 | items 6 or 7 for a self-employed person | dash: no rate; REFUSE if asked as a branch they pay |
| S8 | advance periods other than a month (e.g. a quarter) | REFUSE: T is a monthly sum and nothing in scope says how to scale it to another period |

## 7. Insured who is neither employee nor self-employed, V2026, branches 2, 3, 5, 8, 9, 10

Rates 6.92% below, 7.00% above (rows = printed).

| # | income per monthly period | expected |
| --- | --- | --- |
| N1 | 7,702 | 532.9784 |
| N2 | 7,703 | 533.0476 |
| N3 | 7,704 | 533.1176 |
| N4 | 10,000 | 693.8376 |
| N5 | item 2 only, 10,000 | 0.16% × 10,000 = 16 |
| N6 | items 1 or 4 for a neither-person | dash: no rate |

## 8. V2027 and V2028+, T = 7,857.06 (section 4, T3-T4)

| # | scenario | expected (rows) | [printed totals] |
| --- | --- | --- | --- |
| P1 | 2027 employee, W = 7,857.06 (at T) | 4.26% × W = 334.710756 | [3.95%: 310.35387] |
| P2 | 2027 employee, W = 7,857.07 | 334.712205 | [310.35533] |
| P3 | 2027 employee, W = 10,000 | 645.222762 | [623.22311] |
| P4 | 2027 self-employed, 10,000 | 2.87%/12.83%: 500.436824 | same |
| P5 | 2027 neither, 10,000 | 4.61%/7.00%: 512.216266 | same |
| P6 | 2027 employee item 4, 10,000 | 0.47%/2.06%: 81.072746 | |
| P7 | 2028 employee, 10,000 | 4.16%/14.39%: 635.222762 | [3.85%/14.50%: 613.22311] |
| P8 | 2028 employee item 4, 10,000 | 0.37%/1.96%: 71.072746 | |
| P9 | Dec 2026 vs Jan 2027, employee item 1 below T | 0.24 then 0.16 | |
| P10 | Dec 2027 vs Jan 2028, employee item 4 above T | 2.06 then 1.96 | |

## 9. Who is in which column (s 1, s 334(b))

| # | facts | expected | text |
| --- | --- | --- | --- |
| K1 | works for another in an employment relationship | employee column | s 1 "מעביד" – `מי שמעסיק אדם במסגרת יחסי עבודה` |
| K2 | wage fixed by a Law or a Knesset resolution (e.g. a Knesset member) | employee column; the one liable to pay the wage is the employer | s 334(b), line 3608, `רואים כעובד גם את מי ששכרו נקבע בחוק או בהחלטת הכנסת או על פיה` |
| K3 | a sibling (or parent, child, grandchild) of the owner, no employment relationship, working regularly in work that would otherwise be done by an employee | employee | s 1 "עובד", line 204, `לרבות בן משפחה … ובלבד שהוא עובד במפעל באופן סדיר` |
| K4 | the same sibling, working irregularly | not an employee through this extension | same |
| K5 | the owner's spouse, no employment relationship, working regularly | not an employee through this extension: "בן משפחה" is only `אחד ההורים, ילד, נכד, אח או אחות` | same |
| K6 | a cousin, same facts | not an employee through this extension | same |
| K7 | self-employed: occupation not as employee, 20 h/week average, income 0 | self-employed (limb 1, `לפחות עשרים שעות`, at the bound) | s 1 "עובד עצמאי", lines 206-209 |
| K8 | 19.99 h, average monthly income 6,783 (= 50% of 13,566) | self-employed (limb 2, `לא פחתה מסכום השווה ל־50% מהשכר הממוצע`, at the bound) | same |
| K9 | 19.99 h, income 6,783.01 | self-employed (limb 2) | same |
| K10 | 19.99 h, income 6,782.99, Schedule A amount 2,000 | self-employed (limb 3: ≥ 12 h and ≥ Schedule A amount) | same |
| K11 | 11.99 h, income 6,782.99 | NOT self-employed (no limb) | same |
| K12 | 12 h, income 1,999.99, Schedule A 2,000 | NOT self-employed | same |
| K13 | 12 h, income 2,000, Schedule A 2,000 | self-employed (limb 3 at the bound) | same |
| K14 | 25 h, income 20,000, but works *as an employee* | NOT self-employed (`שלא כעובד` fails) | same |
| K15 | someone insured who is neither (K11, K12) | the neither column | Schedule J header |
| K16 | controlling shareholder (בעל שליטה, s 1 by reference to Income Tax Ordinance s 32 — an input) of a close company, employed by it, W = 10,000 in 2026 | the employee column's rates; branches 6 and 7 are not payable for him (s 335(e)-(f), out of scope, so an input). Total over items 1, 3, 4, 5, 8, 9, 10 by rows: 5.48% × 7,703 + 14.12% × 2,297 = 746.4608. The encoding must not charge him items 6 and 7 by default. | s 1 line 122; s 335(ה)-(ו) |
| K17 | a person who is both an employee and self-employed in one month | REFUSE: how the threshold is shared between the two incomes is not in the provisions in scope | — |

## 10. The average wage, s 1

Line 222-225: the average wage is the 3-month CBS average wage per employee post plus an addition at the compensation rate given since.

| # | facts | expected |
| --- | --- | --- |
| A1 | 3-month average 13,000, compensation rate 0 | 13,000 |
| A2 | 3-month average 13,000, compensation rate 1.5% | 13,195 |

## 11. s 337(b) and (c)

| # | facts | expected |
| --- | --- | --- |
| M1 | no order under s 337(b) in the sources | the printed rates are the law (the section's own default); not a refusal |
| M2 | an order changes item 10's employee rate above T (permanent table) from 5.89 to 6.00 | D↑ item 10 becomes 1.52 × 6.00/5.89 = 48/31 ≈ 1.548387 (`באותה דרך ובאופן יחסי`) |
| M3 | an order changes item 3 (children), where column D is a dash | the deduction stays a dash: nothing to scale |
| M4 | who may make the order | the Minister of Labour and Welfare (s 1 "השר"), with the Knesset Finance Committee's approval; insolvency after consulting, and long-term care with the consent of, the Minister of Finance |

## 12. Column D, the employee's deduction (s 342(c) is out of scope; s 337(c) refers to it)

| # | facts | expected |
| --- | --- | --- |
| D1 | 2026: where does the D↑ band start | 60% of the average wage = 8,139.60, not T = 7,703 (line 4718) |
| D2 | 2026, W = 7,703 | 1.04% × 7,703 = 80.1112 |
| D3 | 2026, W = 8,000 | REFUSE. The slice 7,703-8,000 is in neither band of the temporary table. Literal alternative: no deduction on that slice (80.1112). Purposive alternative: read D↑ as "above T", as the permanent table does. Genuine ambiguity. |
| D4 | 2027, W = 10,000, T = 7,857.06 | 0.40% × T + D↑ × (W − T): rows 4.67% → 131.503538; [printed 7.00% → 181.43404] |

## 13. The refusals, collected

R1 March 2011 (V1); R2 2024 (V2); R3 2025 (V3, BRIEF's scope); R4 a dash cell for a branch the person pays (E13, S7, N6); R5 a falling CPI (T7); R6 the 2026 deduction gap (D3); R7 a non-monthly advance period (S8); R8 employee and self-employed at once (K17).

## 14. Count

270 cell scenarios (section 2) + 27 printed totals + 6 dated arms (V1-V6) + 8 threshold (T1-T8) + 13 employee (E1-E13) + 8 self-employed (S1-S8) + 6 neither (N1-N6) + 10 later-vintage (P1-P10) + 17 classification (K1-K17) + 2 average wage (A1-A2) + 4 s 337(b)-(c) (M1-M4) + 4 deduction (D1-D4) = 375 scenarios: 270 cells, 27 printed totals, and 78 other scenarios.

## Revised after seeing the encoding

Appended after the encoding's `.l4` modules, and then its `NOTES.md`, had been read.
**No expected value above has been changed.** What follows is what reading the encoding taught me about my own answers.

1. **T7 (a falling index) stays REFUSE.** The encoding applies the fall (its fork F6, reading (i)); I still hold that `שיעור עליית המדד` does not say what a fall does, and that "rise" makes reading (ii), no update, at least as strong as (i). The assertion is left failing.
2. **D1, K8 and K9 depend on which average wage is meant, and I did not ask.** I took 13,566, the s 1 figure in the editors' note at line 226. The encoding's fork F5 points out that s 2(b) applies a differently calculated figure (13,769 for 2026, editors' note at line 233) "for benefits and contributions". Under it, 60% is 8,261.4 and 50% is 6,884.5: K8 (19.99 hours, 6,783) and K9 (6,783.01) would no longer meet limb (2), though with my invented Schedule A sum of 2,000 both would still meet limb (3), so the boolean would not change but the limb carrying it would, and K8 and K9 would stop testing the boundary they name. My tests pass because I supplied 13,566; that is my input choice, not a finding that s 1's figure is right.
3. **V3 (2025).** In section 1 I wrote that the source "arguably does answer 2025". The encoding's assumption A1 reports that the Law for the 2025 budget year, s 21, commences its National Insurance chapter on 1 January 2026, which, if right, makes the deposited s 334 and Schedule J text in force only from 2026. I have not verified that Law; it is outside the source bundle. If it is right, my aside was wrong and the refusal is required by the law, not merely by the BRIEF.
4. **Two of my decisions were shaped by the BRIEF rather than derived from the source alone:** the 2025 refusal (V3) and "a dash is not a zero" (section 2). The BRIEF states both as rules. So my agreement with the encoding on those two is not independent evidence.
5. **K16.** The Institute's composite for a controlling shareholder above the threshold is 14.17% (the encoding's NOTES section 0), against 14.12% from the rows without items 6 and 7. My expected 746.4608 uses the rows; the 0.05 is unexplained by anything in scope.
