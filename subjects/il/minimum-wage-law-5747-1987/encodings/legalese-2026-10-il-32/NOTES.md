# Notes: Minimum Wage Law 5747-1987 (row IL-32, run IL-32-20261008, agent enc-il-32)

Status: draft.
No domain expert has read this against the source.
The text is the unofficial Wikisource consolidation deposited at `../../registers/source-bundle/minimum-wage-law-5747-1987.he.wiki.txt` (sha256 `d74633b3e230f83e486642c2815a81fe98b3259450ee85f01bc6f1b972ef78f5`, amendments to 5778).

## 1. What is encoded and what is not

Encoded, from the Hebrew text: the three minimum wages of s 1 (monthly as 47.5 percent of the average wage, daily as a 25th or a 21 2/3rd, hourly as a 186th), the right of s 2(a) by pay basis, the part-time proportion of s 2(b), the reduction for absence of s 2(c), the pay components that count in s 3, the non-reduction rule of s 5, and the two amounts printed in s 21 (reached by the dated lookup since v0.1.1).
Taken as published inputs, in their own clearly marked module (`mw-il32-published-figures.l4`): the shekel amounts since 1 April 2025 (6,247.67 and 6,443.85) and the average wage of 13,566, all reused from row IL-05 with its provenance; nothing was fetched by this row.
Refused by name: the rate for an employee under 18 (s 16 regulations), for an employee in a class covered by s 17 regulations, any daily or hourly part-time proportion, any date before 1 April 2025 and any date from 1 April 2027.

The Law itself contains no youth rate, no apprentice rate and no age band expressed as a fraction.
Section 16 delegates all of that to regulations, which are not deposited, so the brief's "youth and apprentice rates and the age bands the Law sets as fractions" has nothing to encode: the Law sets none.
The only shekel amounts the Law prints are 525 and 551 of s 21 (1987).

## 2. Coverage table

Source lines are in the deposited file.

| Provision | Heading | Disposition | Where |
|---|---|---|---|
| s 1 (lines 11-22) | definitions of bodies of law, the Minister | out-of-scope | cross-references to other Laws, with no operative content for the minimum |
| s 1 "היום הקובע", "המדד" (21-22) | repealed definitions | inert | the text says "(נמחקה)" |
| s 1 "שכר מינימום" (23) | monthly minimum wage | encoded | `mw-s1-definitions.l4`; the average wage is an input; the increases under s 4 arrive through the published figure |
| s 1 "שכר מינימום יומי" (24) | daily | encoded | `mw-s1-definitions.l4` |
| s 1 "שכר מינימום לשעה" (25) | hourly | encoded | `mw-s1-definitions.l4` |
| s 2(a) (28) | the right, full position, age 18 | encoded | `mw-s2-the-right.l4` |
| s 2(b) (29) | part-time proportion | encoded (monthly basis; others refused) | `mw-s2-the-right.l4`, forks F1, F10 |
| s 2(c) (30) | absence | encoded | `mw-s2-the-right.l4`, fork F5 |
| s 3(a) (33) | the pay for a regular working day | encoded | `mw-s3-pay-that-counts.l4` |
| s 3(b)(1)-(3), proviso (35-37, 40) | components that count and do not | encoded | same |
| s 3(b)(4), (5), (c), (e), (f) | repealed | inert | "(פקעה)", "(בוטל)" |
| s 3(d) (42) | pay not by components (1), (2) | encoded | same, fork F2 |
| s 4 (47) | increase by collective-agreement rates | out-of-scope as a rule; carried by the published figure | the increases are the Minister's notices (s 6(3)), not held except through the 2025 and 2026 figures |
| s 5 (50) | no reduction on update | encoded | `mw-s1-definitions.l4` |
| s 6 (54-58) | publication by the Minister | inert; it is why the figures are published inputs | `mw-il32-published-figures.l4` |
| s 6A (60-65) | the actual employer | out-of-scope | liability of a second person, not the amount |
| s 6B (67-75) | notice at the workplace | out-of-scope | a duty to post a notice; no amount |
| s 7 (77) | right to sue | out-of-scope | procedure |
| s 7A (80) | protection of a complainant | out-of-scope | not about the amount |
| s 7B (83-89) | presumptions | out-of-scope | evidentiary presumptions in proceedings against an employer; they decide who proves non-payment, not what is owed |
| s 8, 8A (91, 94) | enlarged compensation; injunction | out-of-scope | remedies |
| s 9 (97) | limit on a claim | out-of-scope | no claim to a raise above the minimum merely because it rose |
| s 10 (100) | average wage | out-of-scope | adjustments of wages tied to the average wage |
| s 11 (104) | saving of rights | inert | the Law adds to other rights; the encoding computes only the statutory floor |
| s 12 (107) | no waiver or contracting out | inert | the floor is computed from the Law whatever a contract says |
| s 13 (110) | the State as employer | inert | no separate rule: the State is an employer like any other |
| s 14, 14A (113-118) | penalties | out-of-scope | punishments, under Penal Law s 61, not deposited |
| s 15-15D (120-144) | managers' liability, limitation, inspectors, obstruction, public authorities | out-of-scope | enforcement |
| s 16 (146-148) | working youth | refused by name | regulations not held |
| s 17 (150-153) | sheltered workshops, people with limitations | refused by name | regulations not held |
| s 18(a)-(c) (155-162) | regulations | refused by name where they would change an amount | s 18(b)(1), (2) pay not by month, day or hour: not held; s 18(c) supplementary daily and hourly rules: not held |
| s 18A (164) | jurisdiction | out-of-scope | labour court |
| s 19 (167) | merged text | inert | editorial |
| s 20 (170) | commencement 1 April 1987 | inert | the encoding answers dates from 2025 |
| s 21 (173-177) | transitional amounts | encoded; the dated lookup `the full monthly minimum wage ... on` DAY reaches them (v0.1.1): 525 from 1 April 1987, 551 from 1 October 1987 to 31 March 1988 (F6, assumed; s 21(a)(2) does not detract from s 4) | `mw-s1-definitions.l4`, `mw-il32-published-figures.l4` |

No row is left deferred.

## 3. Fork register

All forks below are "ruled by Meng 2026-10-08 (SHRUG)" as a policy: one named switch, default decline, other readings kept and tested, the default answering where the readings agree.
Forks marked "assumed, not ruled" are choices of this row, to be reverted alone if wrong.

| Fork | Question | Readings | Default |
|---|---|---|---|
| F1 | How is "the fraction of his position" (s 2(b), line 29) measured by hours? | A: hours worked over the hours of a full position customary at the workplace (s 2(a): "כנהוג במקום עבודתו"); B: hours worked over the 186 hours of a month that s 1's hourly definition implies | decline where they differ; they agree when the full position is 186 hours; the fraction is capped at 1 |
| F2 | When does s 3(d) (line 42) apply? | P: only a pay with neither a basic or combined wage nor a cost-of-living supplement; L: a pay lacking either of them | decline where the two amounts differ (a basic wage plus a fixed supplement and no cost-of-living supplement differ: 5,800 against 5,000) |
| F3 | Does a component the text neither lists nor excludes count (line 34 lists a closed set)? | it counts; it does not count | decline where counting changes the amount |
| F4 | Is a daily wage defined for a week of other than five or six days? | the text defines only those two | no fork: the working week is a two-valued input, so the question cannot be asked |
| F5 | In what unit is the time of absence measured (s 2(c), line 30)? | days; hours; working time | the caller supplies the fraction; the unit is the caller's (assumed, not ruled) |
| F6 | How long does a published figure hold? | until the next 1 April; until a notice | assumed, not ruled: a figure published for 1 April holds to 31 March 1 year later, as IL-05 recorded no change in between; the dates from 1 April 2027 decline |
| F7 | Rounding of the daily and hourly figures | the Law prints none | no rounding: the encoding returns the exact quotient; the Institute prints rounded cents |
| F8 | May a pay for a day that is below the minimum be met by a pay for a month? | not asked | no comparison across periods; the caller supplies the figure of the same period |
| F9 | "שמלאו לו 18 שנים" (line 28): at 18 or from the day after? | 18 completed years or more | assumed, not ruled: age 18 is an adult |
| F11 | Does the s 5 floor apply in the dated lookup? | yes where two adjacent figures are held (525 to 551; 6,247.67 to 6,443.85) | applied (v0.1.1; changes nothing on these figures) |
| F12 | A position of 0% (independent finding 3) | a position or not | the text does not say; refused; not a gating choice |
| F10 | What does a fraction of a position do to a daily or an hourly minimum wage? | the same fraction; none (an hourly wage is already per hour) | decline by name (only the monthly basis is answered) |

## 4. Answer table

The only dated answers are published figures, not law.
Monthly figure for an employee aged 18 or over, full position (the monthly basis).

| Day | Monthly | Six-day daily (a 25th) | Five-day daily (3/65 of the month) | Hourly (a 186th) |
|---|---|---|---|---|
| before 1 April 1987 | declined (the Law had not commenced; the refusal text is the generic no-source one) | | | |
| 1 April 1987 to 30 September 1987 | 525 (s 21(a)(1)) | | | |
| 1 October 1987 to 31 March 1988 | 551 (s 21(a)(2); F6) | | | |
| 1 April 1988 to 31 March 2025 | declined, no source (including 1 April 2023, the editorial note) | | | |
| 1 April 2025 to 31 March 2026 | 6,247.67 | 249.9068 | 288.354 | 33.58962... |
| 1 April 2026 to 31 March 2027 | 6,443.85 | 257.754 | 297.4084... | 34.64435... |
| 1 April 2027 and after | declined, not yet published | | | |

The daily and hourly cells are quotients worked here from the monthly figure by the Law's fractions, not figures the Institute printed.
Part-time, 1 April 2026, 93 of 186 hours: 3,221.925 on either reading.
Part-time, 1 April 2026, 93 hours of a 200-hour position: reading A 2,996.39025, reading B 3,221.925, default declines.

## 5. check.sh output

l4 sha256 before and after: `f0759b2ef2f1d1b2a577c68f059c54f487de9d913553fc9f0d9bf0f7f5dab0d8` (jl4-0.1-6df1397b), unchanged.

```
module                                    errors satisfied  failed  refused  expected
mw-il32-answers.l4                             0         0       0        0         0
mw-il32-nouns.l4                               0         0       0        0         0
mw-il32-published-figures.l4                   0         0       0        0         0
mw-il32-tests.l4                               0        68       0        0         0
mw-s1-definitions.l4                           0         0       0        0         0
mw-s2-the-right.l4                             0         0       0        0         0
mw-s3-pay-that-counts.l4                       0         0       0        0         0
TOTAL (7 modules)                              0        68       0        0
```

Exit 0.
The 68 are all the `#ASSERT` lines in the tests module (`grep -c '^#ASSERT'` is 68), sixteen of which are `#ASSERT REFUSED ... BECAUSE` and satisfied by the refusal text named.
A canary `#ASSERT` with a wrong value fails (`assertion failed`), so the harness can fail.
`tools/hebcheck.py` finds every run of Hebrew in the modules inside the source (exit 0).
No assertion fails and none is expected to.

## 6. Cross-checks of the Law against the published figure

47.5 percent of the Institute's average wage of 13,566 is 6,443.85, which is the figure published from 1 April 2026 (13,566 / 2 = 6,783; 13,566 x 0.025 = 339.15; 6,783 - 339.15 = 6,443.85): tested.
The Law's editorial note prints 5,571.75 from April 2023; 5,571.75 / 0.475 = 11,730, an average wage this row holds no source for, so it is arithmetic only and not a used figure.
6,247.67 / 0.475 is 13,152.99, again an implied average wage, not held.
The average wage the Law names is that of s 1 of the National Insurance Law [Consolidated Version] 5728-1968, which is not deposited; the match of 13,566 with the 1995 Law's average wage is an empirical match (it reproduces the published figure to the agora), not a reading of the 1968 text.

## 6a. Version 0.1.1 (independent pass, finding 1)

The dated lookup refused every date before 1 April 2025, so s 21 was claimed encoded but unreachable by date.
It now answers 525 and 551 as above and applies s 5 between adjacent held figures.
check.sh: 8 modules, 0 errors, 141 satisfied (75 in the row's tests, 66 in tests-independent), 0 failed, 2 refused (tests-independent cases 6 and 45, declared), exit 0; l4 sha256 `f0759b2e…` before and after.
The tester's cases 1, 3, 4 now pass.
Independent finding 8 (open): the tester recalls official hourly rates matching a 182nd, the deposited text says a 186th.
The deposited consolidation may be stale on this, and every hourly answer and F1 reading B rests on the deposited 186.

## 7. Open questions and what needs a source

- Needs a source: the regulations under s 16 (youth and apprentices) and under s 17, including the Minimum Wage (Adjusted Wage for an Employee with a Disability of Reduced Work Capacity) Regulations 5762-2002; the regulations under s 18(b) for pay not by month, day or hour; the supplementary regulations for the daily minimum wage 5759-1998; the Minister's notices under s 6 for each year before 2025 and any s 4 increase; the National Insurance Law [Consolidated Version] 5728-1968 s 1 for the average wage; Penal Law s 61 for the fines.
- Is a part-time employee's "fraction of a position" measured against the workplace's customary full position (reading A) or against 186 hours (reading B)?
- Does s 3(d) reach an employee paid a combined wage plus a fixed supplement?
- Is a figure in the Institute's table between two 1 April dates ever different (fork F6)?

## 8. Inputs the capstone does not supply today (for IL-55)

The capstone takes the Schedule K employee minimum as `the full monthly minimum wage of an employee aged 18 or over applies to the earner` and IL-05's two published figures.
This row would need it to supply: the earner's completed age; whether the pay is fixed by the month, the day or the hour; the working week (five or six days) for a daily wage; whether the earner is in a class covered by s 17 regulations; the hours worked in the month and, if known, the hours of a full position customary at the workplace; and the F1 switch.
It replaces the boolean with `the full-time minimum wage in the unit of pay for ... on` DAY and, for a part-time earner, `the monthly minimum wage of a part-time employee ... on` DAY.
The capstone's second tester's finding F3 (a part-time Schedule K refusal broader than its gap) is answered for a monthly-paid earner by the part-time function: the minimum for 93 of 186 hours is half the figure.
The capstone's premise (K21: a partial or young worker's minimum is at most the full adult figure) holds for the part-time case (the fraction is capped at 1) and is not decided for a young worker, whose rate is fixed by regulations not held.

## 9. What was assumed rather than read

F5, F6, F9 and the cap of the fraction at 1; that the figures of 6,247.67 and 6,443.85 hold between their dates; that the average wage of 13,566 is the Law's average wage on 1 April 2026; that the pay components are classified by the caller.
