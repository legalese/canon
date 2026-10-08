# NOTES — il/national-insurance-law-consolidated-version-5755-1995, encoding row `legalese-2026-10-il-05`

National Insurance Law [Consolidated Version], 5755-1995: **s 342** (who is liable to pay insurance contributions, and the employer's deduction), **s 348** (the maximum, the minimum and the disregarded amount) and **Schedule K** (לוח י״א, the maximum and minimum income for contributions), encoded in L4 by one agent in one session (run `IL-05-20261006`, 2026-10-06), from the brief in `BRIEF.md`.
Status: **draft**. Version **0.5.0** (2026-10-08): fork DATE (a day of birth the month of the age lacks, s 342(c)(2)) is a switch, ruled by Meng (SHRUG), declined by default (BACKLOG IL-39); see "Version 0.5.0" below.
Version 0.4.0 (2026-10-08): repairs from the inventory of 2026-10-08 (BACKLOG IL-17): s 342(c), (d) and (e1) on the income s 348(a) takes into account, nine of the independent tester's assertions re-pointed to the printed totals it decided, one call for a person both employee and self-employed; see "Version 0.4.0" below.
Version 0.3.0 (2026-10-07): row IL-04's Schedule J switch reaches s 342(c); see "Version 0.3.0" below.
No domain expert has read it against the source; HG1 has not been sought.
The row depends on row IL-04 (s 1, s 334, s 337, Schedule J), whose modules it could not import (section 8).

## Version 0.5.0 (2026-10-08): fork DATE as a switch (BACKLOG IL-39)

Backlog row IL-39, agent `shrug-il-39`, one session, no sub-agents, on Meng's ruling of 2026-10-08 (SHRUG) as the lead relayed it: fork DATE becomes one named switch with three readings, the last day of the month (this row's reading until now), the first day of the next month, and a refusal by name saying the text does not say what such a day is; declined by default, the other two kept by name and tested.
Nothing in the sections below was deleted; entries this version changes are marked **(0.5.0)** in place.
`tests-independent.l4`, `DECIDED-ANSWERS.md`, `INDEPENDENT-FINDINGS.md`, the section "Comparison with Axiom's RuleSpec" and `check.sh` are unchanged: none of the tester's dates of birth (15 March 1986, 1 January 1956, 1 January 1957) lands on a day a month lacks.

### What changed

1. **The reading** (`nii-il05-nouns.l4`): `A reading of a day of birth the month of the age lacks`, with `the last day of that month`, `the first day of the next month` and `such a day is declined`.
   It is an argument, never a field of the case records.
2. **One switch** (`nii-s342-liability-and-deduction.l4`, s 342(c)(2)): `section 342(c)(2) — the reading this row takes of a day of birth the month of the age lacks`, now `such a day is declined`, with the refusal "section 342(c)(2) does not say on what day the insured reaches the age when the month it falls in lacks the day of the month of birth".
   Either other reading is a one-line change there.
3. **The day.** `s 342(c)(2) — the day the insured reaches the age, for` m `, reading a day the month lacks as` d: where the month the age falls in has the day of the month of birth, that day, under all three readings; where it lacks it, the month's last day (`add months`, fork F19), the first day of the next month, or the refusal.
   The rule under its old name follows the switch, so for a day a month lacks it now declines where it gave the month's last day.
4. **No deduction for the month.** The body before 0.5.0 is now `s 342(c)(2) — no deduction is made for the month, for` m `, the age being reached on` *day*; a form takes the reading; the old name follows the switch.
   Where the day is lacking, the last day of the month (L) and the first day of the next (L + 1) answer every month the same but the one containing L: before it the age is reached after the month under both, and from the next month on, on or before its first day under both.
   In that month they differ only where no senior citizen pension is payable for any of it: at L the age is reached during the month, declined by fork F9; at L + 1 it is reached after it, and the employer deducts.
   So "declined" declines in that month only, and answers every other month as both readings do (fork F26, below).
5. **The deduction.** A new most general form, `s 342(c) — the amount the employer deducts from the wage, for` m `, reading Schedule J as` r `, column D at the printed totals being` x `, reading a day the month lacks as` d; every other s 342(c), (c)(2), (d) and (e1) rule, those of 0.4.0 included, follows the switch.

**What the default changes.** No answer that was a number became a refusal, or the reverse.
In the one month in which the readings differ, the clamp already declined it (fork F9); it is now declined by fork DATE's refusal instead.
The day rule under its old name declines where it gave the month's last day.
The version is minor, not a patch, for those two.

### Fork register (0.5.0)

| # | where | the question | readings | taken, and why |
| --- | --- | --- | --- | --- |
| DATE | s 342(c)(2) (3662); fork F19 | see "Version 0.4.0" below | (i) the last day of the month; (ii) the first day of the next month; (iii) declined | **(iii) by default, ruled by Meng on 2026-10-08 (SHRUG)**; (i) and (ii) kept by name and tested. One ruling for rows IL-05, IL-06 and IL-08 (BACKLOG IL-39 to IL-41). |
| F26 | fork DATE's (iii) | Does "declined" decline every question that reads the day, or only those the reading decides? | (i) only where (i) and (ii) of fork DATE give different answers; (ii) every question that reads the day | **(i)**, assumed by the agent, not ruled. Under (ii), every month's deduction for a woman born on the 31st whose Part D age ends in a month of 30 days would be declined, decades before or after that month, on a question the day cannot change. The day rule itself declines (it has no answer without the day). |

### Assertions re-pointed or added

No expected value changed.
`nii-il05-tests.l4`, section "Fork DATE": **2 re-pointed** to the clamp by name, values unchanged, and **26 added** (210 to 236), in the same section.
The two re-pointed called the rule under its 0.1.0 name; they now call the most general form with `the items govern`, 0 for the printed totals (what the 0.1.0 name passes) and `the last day of that month`.
Every added value was worked out by hand before the first run that evaluated it (a wage of 7,000 at 1.04% is 72.8; the days by the calendar); all 26 were satisfied on that run, and with three of them altered in a scratch copy (a day, a value, a refusal's wording) the module reported each as failed.

| assertion | value | why |
| --- | --- | --- |
| (re-pointed) a man born 29 February 1956, wage 7,000, February 2026, at the last day of the month | declined, fork F9 | 28 February is reached after the month's first day |
| (re-pointed) the same, March 2026 | 0 | reached on or before 1 March |
| the switch | `such a day is declined` | the ruling |
| the day, that man: last day; first day of the next month; declined by name; at the switch | 28 February 2026; 1 March 2026; declined; declined | the readings |
| the day, a man born 15 March 1956, under each of the three readings | 15 March 2026 (three times) | the month has the day |
| February 2026, that man: first day of the next month; declined by name; the 0.1.0 name | 72.8; declined (DATE); declined (DATE) | reached on 1 March, after February; the readings differ |
| January 2026, the 0.1.0 name; March 2026, the 0.1.0 name, the next day's reading, declined by name | 72.8; 0, 0, 0 | the readings agree |
| February 2026 with a senior citizen pension for the whole month; for part of it (0.1.0 name) | 0; declined (the pension's refusal, fork F9) | the readings agree |
| 0.4.0's rule from a wage of 60,000, February 2026, that man | declined (DATE) | it follows the switch, before column D is read |
| SCENARIO: a woman whose Part D age is 836 months, born 31 August 1956: the day at the last day; at the first day of the next month | 30 April 2026; 1 May 2026 | April 2026 has no 31st |
| the same woman, April 2026: last day; first day of the next month; the 0.1.0 name | declined (F9); 72.8; declined (DATE) | the readings differ |
| the same woman, May 2026: the 0.1.0 name; last day; first day of the next month | 0; 0; 0 | the readings agree |

### What `check.sh` prints at 0.5.0

Run from 2026-10-08T16:04:45Z to 16:05:03Z as `L4=/Users/mengwong/.local/bin/l4 ./check.sh`, `JL4_LIBRARY_PATH` unset, on the binary of 0.4.0 (cabal store `jl4-0.1-d4290e25`, sha256 `f4f2bd2558f02f828f0deced5f74313a33670f08cc3275ff95b83f2cde71e448`), the same before and after the run.
On it, a copy of the row as committed at 0.4.0 gave 0.4.0's table (16:05:13Z to 16:06:17Z).

```
module                                    errors satisfied  failed  refused  expected
nii-il05-nouns.l4                              0         0       0        0         0
nii-il05-published-figures.l4                  0         0       0        0         0
nii-il05-tests-expected-red.l4                 3         2       3        0         3
nii-il05-tests.l4                              0       236       0        0         0
nii-s342-liability-and-deduction.l4            0         0       0        0         0
nii-s348-maximum-minimum.l4                    0         0       0        0         0
nii-schedule-k.l4                              0         0       0        0         0
tests-independent.l4                           6       131       6        2       6/2
TOTAL (8 modules)                              9       369       9        2
```

`check.sh` exit 0; every error is a failed assertion, each declared.
**Mechanical checks** (row IL-04's tools, by path): `srcquote.py` over the three changed modules changed nothing; `hebcheck.py` passes on them, on this file and on `encoding.json`.

### For the capstone (row IL-07; BACKLOG IL-44)

- `nii-il05-nouns.l4` and `nii-s342-liability-and-deduction.l4` changed; re-vendor them.
  Nothing the capstone calls was renamed or removed.
- In a scratch copy of the capstone as committed (v0.3.0) with these two modules in place of its vendored copies, every capstone module compiled and gave the counts it gave before: `il07-tests.l4` 130 satisfied, `il07-tests-il08.l4` 116, `tests-independent.l4` 260 satisfied and 18 failed, `tests-independent-2.l4` 298 satisfied, 7 failed and 20 refused.
- New: the reading type, the switch, the refusal, and the forms that take the reading; a capstone that wants the clamp or the next day passes it to the most general s 342(c) form.

### Row IL-37 (TAKEAWAY): nothing is needed here

TAKEAWAY changes row IL-04's column D for fewer than all deduction branches (the printed total less the printed items of the branches not paid, by default for a controlling shareholder, 1.02 and 6.79, and for ages 67 to 70 without an old-age pension, 0.70 and 4.86).
This row needs no change for it, because:

- At the printed totals this row never computes column D: it takes the figure for the deduction branches together from its caller (an argument since 0.3.0, a function of an income since 0.4.0), which is row IL-04's `the column D deduction under` … `in the branches` … for those branches.
  Whatever IL-04 now answers for a partial set reaches s 342(c) unchanged, and so does a decline.
- Its one partial-set computation, fork F23 (a police or prison officer: the printed total less item 6's own amount), is TAKEAWAY's construction on the set of all deduction branches but unemployment.
  That is a controlling shareholder's column D set too: s 335(e) takes unemployment away from "בעל שליטה בחברת מעטים" (line 3615), and s 335(f)'s insolvency branch has no column D figure (line 4726).
  So F23 gives TAKEAWAY's published 1.02 and 6.79 in 2026 (1.04 less 0.02, 7.00 less 0.21; the tester's B9 decided the same), and 0.39 and 6.79 under the permanent table.
  It reaches that set by subtracting item 6 from the six-branch total, so it does not depend on whether IL-04 keys its default to the branch set or to the person's status.
- The tester's re-pointed assertions and this row's own tests at the printed totals pay all six deduction branches, so none of them moves.

At IL-07 the two may be named as one construction; that is a naming question, not a change in any answer.

## Version 0.4.0 (2026-10-08): repairs (BACKLOG IL-17)

Backlog row IL-17, job D of `l4-pipeline/findings/il-2026-10-08/jobs.txt`, repair agent `rep-il-17`, one session, no sub-agents, on the inventory of open findings taken on 2026-10-08 (`findings/il-2026-10-08/inventory.tsv`, the items named below).
Nothing in the sections below was deleted; entries this version changes are marked **(0.4.0)** in place.
The section "Comparison with Axiom's RuleSpec", `DECIDED-ANSWERS.md` and `INDEPENDENT-FINDINGS.md` are untouched; `tests-independent.l4` was edited only as item 05-RC1 says, with a dated note at its end.
No existing entry point's answer changed: what this version adds has new names, and every assertion `nii-il05-tests.l4` had at 0.3.0 gives the value it gave.
The version is minor, not a patch, because the row now answers questions it could not (a capped deduction from a wage; both liabilities in one call).

### The items

- **05-RC2: s 342(c) is uncapped by s 348(a) when called on its own (OURS-WRONG, interface).**
  s 342(c)(1) deducts "percentages of the income on which the contributions are payable" (source line 3661), and s 348(a) says that the insured person's income above the Schedule K maximum "shall not be taken into account" (line 3763).
  The s 342 rules take column D as amounts the caller has computed, so they deducted on whatever income the caller used: column D on a wage of 60,000 in 2026 gave 2,522.3811 at the items, where on the 51,910 s 348(a) takes into account it is 2,144.5781 (the independent tester's root cause 2).
  Those rules are kept and answer as before; the record field `the column D amounts on the wage` and the s 342(c) rule under its 0.1.0 name now say in their `@desc` that the amounts must be on the wage as s 348(a) takes it into account.
  New, in `nii-s342-liability-and-deduction.l4`, section "Version 0.4.0": rules that take the wage (for (d) and (e1), the total monthly income) and column D as Schedule J gives it, a function of an income, by branch and at the printed totals, and apply it to the wage as s 348(a) takes it into account: the wage, or the Schedule K item 1 maximum for a month if that is lower.
  Each comes at a named reading of Schedule J with the Schedule K figures given, and at the switch's reading with the figures for the month's tax year (2026 as published; 2025, and 2027 on, declined by name): `s 342(c) — the amount the employer deducts from a wage of` …, `s 342(d) — "coordinated contributions", on a total monthly income of` …, `s 342(d) — the outcome, for the deductions` … `, on a total monthly income of` …, and `s 342(e1) — the contributions the renewed kibbutz pays for the member, for` … `, on a total monthly income of` ….
  They do not read the month's own column D amounts.
  Column D is a function argument, not computed here, because Schedule J is row IL-04's and this row cannot import it (section 8); row IL-04's `the column D deduction under` on an income is the function a composing row would pass.
  `nii-s342-liability-and-deduction.l4` now imports `nii-s348-maximum-minimum` (for `s 348(a) — the income taken into account, of` and the refusal when the figures are for another year); that module does not import this one.
  The new rules apply s 348(a) and not s 348(b) (fork F25, below).
- **05-RC1: nine of the independent tester's assertions called the items' reading (OURS-WRONG, test wiring).**
  Read before re-pointing: `DECIDED-ANSWERS.md` section 1 decides "col D (employee deduction) total 7.00 above the bracket, 1.04 below"; its B and C tables work every value on 7%; and its "Revised" section, item 1, keeps them on the printed total after finding that the rows sum to 4.67.
  The nine called the s 342(c) and (d) rules under their 0.1.0 names, which read the items, so they failed with values that are right under the ruling of 2026-10-07.
  They were re-pointed, as row IL-04 v0.3.1 re-pointed its tester's, to the reading the tester decided by name, `, reading Schedule J as` `the printed totals govern`, with no expected value changed and no line inserted: lines 220-223, 226, 228, 236, 245 and 248.
  At the printed totals this row takes column D for the deduction branches together as an argument, so each line now carries the tester's own figure for it, 7,703 × 1.04% plus the rest of the wage × 7%, written out as an expression on the wage of the line.
  05-RC2 was done first; line 226 (B8, a wage of 60,000) uses its new rule, with the tester's own `fid 2026 figures` and `fid column D amounts on a wage of` and, at the printed totals, a function applying 1.04 and 7.00 as the tester's `fid banded` applies the rows.
  All nine now pass.
  The note at the end of `tests-independent.l4` gives the details, including that lines 220-223 and 236 now check only that the figure passes through when nothing is left out: the arithmetic is row IL-04's, whose own tests assert two of the values at its default (80.1812 at 7,704 and 240.9012 at 10,000, its `nii-il04-tests.l4` lines 344 and 505).
- **05-P3: a person who is both an employee and self-employed took two calls (OURS-WRONG, optional interface).**
  New record `An insured person who may be both an employee and self-employed, for section 342(a)-(b)` (`nii-il05-nouns.l4`) and rule `s 342(a)-(b) — the persons liable to pay the contributions for`, which returns a list: the employer for the employee under (b), and the person for himself under (a).
  Each status is put to the one-column rule, which is unchanged, so one call answers as the two calls did (the tester's A7; the Axiom comparison's X5 and P3).
- **05-RC5: Amendment 252 s 7(b) (WORDING).**
  Recorded here, as the inventory asks; this row's notes had not mentioned it.
  Amendment 252 s 7(b) (the deposited `amending-laws/25_lsr_5482787.pdf`, PDF page 4, read with `pdftotext -raw`) lets the Minister of Finance, after consulting the Minister of Labour and with the approval of the Knesset Labour and Welfare Committee, extend by order the temporary provision for contributions collected for 2027 and 2028, one year at a time; s 7(c) has the order brought to the Committee at least two months before the year.
  Row IL-04 takes no order by default (its assumption A8) and has entry points that take one.
  This row takes column D from its caller, so whether the temporary or the permanent table applies in 2027 is the caller's: this row's own 2027 scenario (`nii-il05-tests.l4`, section "Section 342(d)") uses the permanent table, which is IL-04's A8 default, not a finding that no order was made.
  The tester's I3 (`tests-independent.l4` line 421) expects a refusal for February 2027; the rules that take amounts answer on what they are given (187.3811), and it stays failing, declared in `check.sh`.
  The new rules of 05-RC2 decline 2027 at the switch, because the Schedule K figures for 2027 were not published, not because of s 7(b).
- **05-X1, its F3 rewording (P1) (WORDING).** Fork F3's reason is restated in place, and open question 2 is extended; the answer is unchanged.
- **05-P2 and 05-P4 (WORDING).** The two presuppositions are stated in assumption A5.
- **05-W1 (WORDING).** Section 11's "independent test pass … was not run" is marked stale in place.
  The comparison section's "the composed answer would use 4.67" (its subsection "Schedule J column D: 4.67 or 7.00") is stale too, and is noted here because that section is not edited: since row IL-11 (IL-04 and this row v0.3.0, the capstone v0.2.1, which follows IL-04's switch), the printed totals govern by default, so the composed deduction above the threshold uses 7.00 (80.1812 at 7,704), and 4.67 only at the items' reading by name.
- **DATE (fork, waits on Meng; BACKLOG IL-24).** Recorded in the fork register below with each reading and who holds it; the current behaviour (fork F19's clamp) is kept, and a test in `nii-il05-tests.l4` (section "Fork DATE") labels it.
  **(0.5.0)** Ruled by Meng on 2026-10-08 (SHRUG): a switch, declined by default, the clamp and the next day kept by name; see "Version 0.5.0".

### Fork register, added (0.4.0)

| # | where | the question | readings | taken, and why |
| --- | --- | --- | --- | --- |
| F25 | s 342(c)(1) (3661); s 348(a) (3763), (b) (3765) | the income the deduction is taken on, in the 0.4.0 rules that take the wage | (i) the wage, less what s 348(a) leaves out; (ii) the whole s 348 income, (b)'s minimum applied too (the capstone's fork K8 (i)); (iii) the wage as paid | **(i)**, assumed by the repair agent, not ruled: the item asked for the cap. Whether (b)'s minimum applies to each employer's wage or to the total, with several employers, is fork F17, not modelled; with one employer a caller who applies (b) gives the minimum as the wage. The rules that take amounts deduct on whatever income the caller used. |
| DATE | s 342(c)(2) (3662); fork F19 | the day an age is reached, when the date of birth moved on by the age falls on a day the month lacks (a man born 29 February 1956 reaches 70 in 2026, which has no 29 February) | (i) clamp to the month's last day (28 February); (ii) roll to the first of the next month (1 March); (iii) decline | **(i), kept as the default until Meng rules (BACKLOG IL-24).** **(0.5.0)** Ruled (SHRUG): (iii) by default, (i) and (ii) by name; see "Version 0.5.0". (i) is held by this row's encoder (F19), row IL-06's (its F2, s 65) and row IL-08's (its N4, Schedule A1 Part D, chosen to agree with F19). (ii) is named as the other reading by IL-06's F2 and IL-08's N4, and held by no one. (iii) is held by the independent testers of IL-06 (its finding 2) and IL-08 (its D-46 to D-48), and is the lead's recommendation for IL-24 (a named switch, default decline). Here it moves one month: February 2026, for that man, is declined under (i) (the age is reached on the 28th, after the month's first day: fork F9) and deducted under (ii); March is 0 under both. |

### Assertions added or re-pointed

No expected value changed anywhere.

`nii-il05-tests.l4`: **29 added** (181 to 210), in its last three sections, every value worked out before the first run that evaluated it, from Schedule J column D (source lines 4720-4730, 4738-4748) and Schedule K item 1 (line 4758), by a script over exact fractions that does not use this encoding (`expected.py`, in the repair agent's scratchpad, not deposited), and each agreeing with the hand working in the comments.
All 29 were satisfied on that first run; with three of them altered in a scratch copy (a value, a refusal's wording, a list's order) the module reported each as failed.

| assertion (Feb 2026 unless marked; "D" = column D as a function) | value | why |
| --- | --- | --- |
| s 342(c) from a wage of 60,000, at the switch | 3,174.6012 | 51,910 taken into account (10,382 × 5): 7,703 × 1.04% + 44,207 × 7% |
| the same at the printed totals by name, figures given | 3,174.6012 | the same |
| the same at the items | 2,144.5781 | 80.1112 + 44,207 × 4.67% (the tester's "capped" figure) |
| s 342(c) under its 0.1.0 name, given column D on 60,000 | 2,522.3811 | the rule that reads amounts is kept: 80.1112 + 52,297 × 4.67% |
| from a wage of 51,910; of 51,911 | 3,174.6012; 3,174.6012 | at and above the maximum |
| from a wage of 10,000, at the switch; at the items | 240.9012; 187.3811 | below the maximum, as the rules that take amounts |
| a police officer, 60,000, at the switch; at the items | 3,080.2259; 2,050.2028 | item 6 on 51,910, 1.5406 + 92.8347 = 94.3753, left out |
| a man who reached 70 on 1 January 2026, 60,000 | 0 | s 342(c)(2); column D not needed |
| December 2025 | declined, "this row answers contribution periods from January 2026 only" | A1 |
| February 2027, at the switch | declined, "the figures Schedule K reads for 2027 and later had not been published when this encoding was made" | Schedule K figures |
| February 2027, scenario figures (basic amount 10,600) and the permanent version (threshold 8,000), at the printed totals; at the items | 3,182; 2,133.5 | 53,000 taken into account: 32 + 45,000 × 7%; 32 + 45,000 × 4.67% |
| February 2026 with the 2027 figures | declined, "the figures given are for another tax year than the case" | — |
| s 342(d) coordinated contributions on a total of 80,000 | 3,174.6012 | the total taken into account at 51,910 |
| (d), two employers deducting 2,340.9012 each, total 80,000, at the switch | a refund of 1,507.2012 | 4,681.8024 − 3,174.6012 (the tester's C2, with the cap now this row's) |
| (d) at the items, each deducting 1,588.3811 | a refund of 1,032.1841 | 3,176.7622 − 2,144.5781 |
| (d) with one employer | does not apply | — |
| (e1), total 80,000, the other employer deducted 2,340.9012; at the items, 1,588.3811 | 833.7; 556.197 | 3,174.6012 − 2,340.9012; 2,144.5781 − 1,588.3811 |
| s 342(a)-(b), one call: both; employee; self-employed; neither; neither, insured under Chapter C only as a wife | [the employer, the person]; [the employer]; [the person]; [the person]; [no one …] | 05-P3 |
| fork DATE: a man born 29 February 1956, wage 7,000, February 2026; March 2026 | declined (fork F9); 0 | reading (i), the current behaviour; **(0.5.0)** re-pointed to (i) by name, values unchanged |

`tests-independent.l4`: **nine re-pointed**, values unchanged (05-RC1).

| line | id | expected | at 0.3.0 | at 0.4.0 |
| ---: | --- | --- | --- | --- |
| 220 | B4, 7,704 | 80.1812 | failed (80.1579) | satisfied |
| 221 | B5, 8,000 | 100.9012 | failed (93.9811) | satisfied |
| 222 | B6, 10,000 | 240.9012 | failed (187.3811) | satisfied |
| 223 | B7, 51,910 | 3,174.6012 | failed (2,144.5781) | satisfied |
| 226 | B8, 60,000 | 3,174.6012 | failed (2,522.3811) | satisfied, through the 05-RC2 rule |
| 228 | B9, police, 10,000 | 234.5369 | failed (181.0168) | satisfied |
| 236 | B12, a man of 69, 10,000 | 240.9012 | failed (187.3811) | satisfied |
| 245 | C1, pays | 375.3012 | failed (228.5811) | satisfied |
| 248 | C2, refund | 1,507.2012 | failed (2,537.2243) | satisfied |

The six failures and two refusals that remain are the tester's E8 (lines 303-306) and H1 (385), inventory 05-RC3, TESTER-WRONG; H2 and H3 (387, 389, refused), 05-RC4, AMBIGUITY; and I3 (421), 05-RC5, WORDING.

### What `check.sh` prints at 0.4.0

Run from 2026-10-08T07:08:54Z to 07:09:08Z as `L4=/Users/mengwong/.local/bin/l4 ./check.sh`, `JL4_LIBRARY_PATH` unset.
`~/.local/bin/l4` resolved to the cabal store build `jl4-0.1-d4290e25` (233,567,184 bytes, modified 2026-10-08T06:07:24Z), sha256 `f4f2bd2558f02f828f0deced5f74313a33670f08cc3275ff95b83f2cde71e448`, the same before and after the run; not the binary of 0.3.0 (`3a1843a0…`).
On it, before any repair (06:50:57Z to 06:51:28Z), the row gave 0.3.0's table exactly, exit 0.

```
module                                    errors satisfied  failed  refused  expected
nii-il05-nouns.l4                              0         0       0        0         0
nii-il05-published-figures.l4                  0         0       0        0         0
nii-il05-tests-expected-red.l4                 3         2       3        0         3
nii-il05-tests.l4                              0       210       0        0         0
nii-s342-liability-and-deduction.l4            0         0       0        0         0
nii-s348-maximum-minimum.l4                    0         0       0        0         0
nii-schedule-k.l4                              0         0       0        0         0
tests-independent.l4                           6       131       6        2       6/2
TOTAL (8 modules)                              9       343       9        2
```

`check.sh` exit 0; every error is a failed assertion.
Re-run from 07:14:05Z to 07:14:27Z, after the last edits (a comment in the note at the end of `tests-independent.l4`, this file, `encoding.json`), on the same binary, unchanged during the run: the same table, exit 0.
**`check.sh` changed**: `tests-independent.l4` is expected to fail 6 (was 15) and refuse 2, each line named in a comment with its inventory id and class.
**Mechanical checks** (row IL-04's tools, by path, read-only): `srcquote.py` over the three changed modules changed nothing; `hebcheck.py` passes on them, on `tests-independent.l4`, this file and `encoding.json`, and fails on a planted string.

### For the capstone (row IL-07; BACKLOG IL-22)

- `nii-il05-nouns.l4` and `nii-s342-liability-and-deduction.l4` changed, so the capstone's pins for them in `VENDORED.sha256` are stale; `nii-s348-maximum-minimum.l4`, `nii-schedule-k.l4` and `nii-il05-published-figures.l4` did not change.
- Nothing the capstone calls was renamed or removed, and no answer of it changed.
  In a scratch copy of the capstone with the two changed modules put in place of its vendored copies, every capstone module compiled and gave the counts it gave before (its `il07-tests.l4` 114 satisfied, `il07-tests-il08.l4` 98, `tests-independent.l4` 258 satisfied, 18 failed, 2 refused, `il07-tests-expected-red.l4` 2 failed), on the binary above.
- New: `nii-s342-liability-and-deduction.l4` imports `nii-s348-maximum-minimum` (both vendored); the record type of 05-P3; the rules of 05-RC2 and 05-P3.
  The capstone already takes column D on the s 348 income (its fork K8), so it need not move to the 05-RC2 rules; if it does, it passes row IL-04's column D as their function arguments, and keeps (b)'s minimum its own (fork F25).

## Version 0.3.0 (2026-10-07): Schedule J's printed totals or its items

Backlog row IL-11, encoder `enc-il-11`, one session, no sub-agents, on Meng's ruling of 2026-10-07 as the lead relayed it: where Schedule J's totals row and its items differ (row IL-04's fork F4), the **printed totals govern by default** and the items' reading is **kept as the alternative**.
The version goes from 0.1.0 to 0.3.0 to match row IL-04's, whose switch this is.
Nothing in the sections below was deleted; the section "Comparison with Axiom's RuleSpec", `tests-independent.l4`, `DECIDED-ANSWERS.md` and `INDEPENDENT-FINDINGS.md` are untouched.

### What changed

1. **The reading is declared again** (`nii-il05-nouns.l4`), constructor for constructor as row IL-04 v0.3.0 declares it, `A reading of Schedule J where its totals row and its items differ` (`the printed totals govern`, `the items govern`), for the reason the branch types are (section 8).
2. **One switch**, `section 342(c) — the reading of Schedule J this row takes where its totals row and its items differ`, now `the printed totals govern` (`nii-s342-liability-and-deduction.l4`, section "Version 0.3.0"); the other reading is a one-line change there.
3. **What a reading changes here.** s 342(c)(1) deducts "percentages … as in Schedule J" (line 3661). At the items, the (c)(1) deduction is the sum of the per-branch column D amounts the case gives, as before. At the printed totals it is one amount for the branches in which the employer deducts, together, which no per-branch list can carry (column D's upper part prints 7.00 where its six items sum to 4.67): so the rules that read it take it as an **argument**, `column D at the printed totals being` x, the figure row IL-04 v0.3.0's `the column D deduction under …` gives at its default reading for those branches (fork F24). It is an argument, not a field of `An employee's month under section 342(c)`, so the records `tests-independent.l4` builds still build.
4. **Which rules.** s 342(c), (c)(1), (c)(2)'s reduction, (d)'s coordinated contributions and outcome, and (e1) each have a form that takes a reading and the argument, and a form "…, column D at the printed totals being" x that follows the switch. **The rules under their 0.1.0 names read the items** (their bodies now call the reading form with `the items govern`; the argument is not read there), so every caller built before 0.3.0 answers as it did.
5. **A police or prison officer** (s 342(c)(2): "the deduction in item 6 of Schedule J" is not deducted): at the printed totals, the total less item 6's own amount from the per-branch list (fork F23).

### Fork register, added

| # | where | the question | readings | taken, and why |
| --- | --- | --- | --- | --- |
| F23 | s 342(c)(2) (3662), at the printed totals | "the deduction in item 6" when the deduction is a total for the branches together | (i) item 6's own amount, from the items; (ii) a share of the total | **(i)**: item 6 is a row of Schedule J with its own printed figures; the total covers it, so the rest is the total less it. |
| F24 | s 342(c)(1) (3661), "as in Schedule J" | row IL-04's fork F4, as it reaches this row | (i) the printed totals; (ii) the items | **(i) by default, ruled 2026-10-07**; (ii) by name. At (i) the amount for the branches together is an argument, computed by row IL-04. |

### Assertions changed, or now asking the items by name

`nii-il05-tests.l4`: the four s 342(d) assertions of the 2027 scenario that turn on column D's upper part (coordinated contributions 218.8, and the three outcomes on it) now ask the items' reading by name (`…, reading Schedule J as` `the items govern` …), values unchanged.
Added (11, its last section, each worked by hand from the source's cells before the run): the switch's value; on a wage of 10,000 in 2026, the per-branch amounts by the items (27.6869, 3.9188, 6.3643, 65.0629, 5.5267, 78.8215), the deduction **187.3811** at the items (by the 0.1.0 name and by name) and **240.9012** at the printed totals (7,703 × 1.04% + 2,297 × 7%); a police officer, **234.5369** at the printed totals and **181.0168** at the items (item 6, 6.3643, left out); 7,000 at the printed totals, 72.8 (the readings agree below the threshold); s 342(d) in the 2027 scenario at the printed totals, coordinated contributions **312** (8,000 × 0.40% + 4,000 × 7%), and the outcomes: the employee pays 264, is refunded 88, pays 93.2.
No other expected value changed.

### What `check.sh` prints at 0.3.0

Run from 2026-10-07T07:20:12Z to 07:20:25Z as `L4=/Users/mengwong/.local/bin/l4 ./check.sh`, `JL4_LIBRARY_PATH` unset, on the binary row IL-04's "Version 0.3.0" records (sha256 `6015a4c3…`, unchanged during the run; not `jl4-0.1-0ee0100b`, which section 0 used). No module changed during the run.

```
module                                    errors satisfied  failed  refused  expected
nii-il05-nouns.l4                              0         0       0        0         0
nii-il05-published-figures.l4                  0         0       0        0         0
nii-il05-tests-expected-red.l4                 3         2       3        0         3
nii-il05-tests.l4                              0       181       0        0         0
nii-s342-liability-and-deduction.l4            0         0       0        0         0
nii-s348-maximum-minimum.l4                    0         0       0        0         0
nii-schedule-k.l4                              0         0       0        0         0
tests-independent.l4                          15       122      15        2      15/2
TOTAL (8 modules)                             18       305      18        2
(a failed assertion is also an error; any other error, or a refused assertion a module is not expected to have, makes the run red; "expected" is failed/refused where a module may refuse)
```

**Re-run on a new binary.** `~/.cabal/bin/l4` was replaced at 2026-10-07T07:25:28Z, after the run above: sha256 3a1843a0e51ce1663cd71b4307e061fa425f2f9f23d78afb8ffa9be6fd20278f (233,039,712 bytes, modified 2026-10-07T07:25:28Z, again a regular file, not a store build). Re-run from 07:28:54Z to 07:29:01Z on it, the binary unchanged during the run and no module changed: the same table, exit 0.
`check.sh` exit 0; every error is a failed assertion. `nii-il05-tests.l4`: 181 of 181, every new value satisfied on the first run that evaluated it.
**`check.sh` changed**: it now lists `tests-independent.l4` (15 failed, 2 refused) and has `expected_refused`. Before 0.3.0, on the same binary, the same modules gave the same counts but `check.sh` exited **1**, because it did not list the independent tester's file, added after section 0 was written.

### The independent tests at 0.3.0

`tests-independent.l4` (not edited), 139 assertions: **122 satisfied, 15 failed, 2 refused**, assertion by assertion the same as before 0.3.0: its calls use the rules' 0.1.0 names, which read the items.

## 0. What `check.sh` prints

Run on 2026-10-06 with `/Users/mengwong/.local/bin/l4`, `JL4_LIBRARY_PATH` unset.
That path is a symlink to `~/.cabal/bin/l4`, which resolves to the cabal store entry `jl4-0.1-0ee0100b`, sha256 `64bbcb157dbef2ef1020a6a75589313bba0a2aeeb807c921c5e65e62e9eca118` (the binary row IL-04 used).
The binary has no `--version`, and no record beside it names the commit it was built from.

```
module                                    errors satisfied  failed  refused  expected
nii-il05-nouns.l4                              0         0       0        0         0
nii-il05-published-figures.l4                  0         0       0        0         0
nii-il05-tests-expected-red.l4                 3         2       3        0         3
nii-il05-tests.l4                              0       170       0        0         0
nii-s342-liability-and-deduction.l4            0         0       0        0         0
nii-s348-maximum-minimum.l4                    0         0       0        0         0
nii-schedule-k.l4                              0         0       0        0         0
TOTAL (7 modules)                              3       172       3        0
```

`check.sh` exit 0.
The 3 errors are the 3 failed assertions of `nii-il05-tests-expected-red.l4`, which `check.sh`'s `expected_failed` table and `encoding.json`'s `expected_red` both name with that count; there is no other error, and no warning in any module.
They were predicted before that module was first run, and the run failed exactly those three, read from the diagnostics by line (45, 46, 61; none "could not be evaluated"):

- **2: s 342(e)(3) and (e)(4) name "column E of Schedule J" for the rates of the employer's deduction** (lines 3669-3670), where Schedule J's column E is "the State Treasury's allocation under s 32(c1)" and the deduction is column D, "the deduction from the employee's wage for s 342(c)" (line 4717). Fork F22.
- **1: s 342(c)(2) is made "subject to s 245(b2)"** (line 3662), and s 245(b2) reads "(בוטל)", repealed (line 2474). Fork F10.

Neither changes an answer the rules give: (e) is a power whose regulations are not in the sources, and a repealed provision qualifies nothing.

`nii-il05-tests.l4`: 170 assertions, 170 satisfied, on the first run that evaluated them.
Before that run, nine fixture names were changed so that no helper shared a name with a record field, a parameter, a global, or another helper's head and arity (made by reading the module, not in answer to a diagnostic); no expected value was changed at any point.
Every expected value was computed before the run, from the source's cells and the Institute's printed figures, without the encoding: by a Python script over exact fractions (`expected.py`, in the session scratchpad, not deposited), or, for a few one-step figures (557.75, 700, 2,100, and the 200 + 18.8 that equals 218.8), by hand.

**The harness can fail.** In a scratch copy, two expected values were altered (51,910 to 51,911; 2,065.35 to 2,065.36): `check.sh` reported 2 failed in the tests module and exited 1.

**Mechanical checks**, using row IL-04's scripts by path (read-only; not copied):

- `../legalese-2026-10-il-04/tools/srcquote.py SOURCE FILE.l4…` generates every `-- src:N | …` comment from line N of the source; re-running it over every module of this row changed nothing.
- `../legalese-2026-10-il-04/tools/hebcheck.py SOURCE FILE…` checks that every run of Hebrew outside a `src:` line occurs verbatim in the source; it passes on every `.l4` module, `BRIEF.md`, this file, `encoding.json` and `SOURCE-LICENSE.md`, and fails on a planted invented string.

## 1. What is encoded and what is not

**Encoded:** s 342(a), (b), (c)(1), (c)(2) in all its limbs, (d) with its two definitions, (e1) and (f)(1)-(2); s 348(a), (a1), (b), (c) (as the test whether an order is within the power, and a decline where one reaches), (d) (where its two readings agree) and (e) in both its permanent and its temporary text; Schedule K in full: all four items, maximum and minimum, per month, quarter and year, with its three definitions.
**Inert:** headings; s 342(e)(1)-(4) and (f)(3), powers to make rules whose regulations are not in the sources (a deduction such a regulation governs is declined by name).
**Out of scope:** Schedule K1 (referred to only by s 369); and every provision outside the slice, each listed in section 2 with how this row takes its result.

**Periods answered:** contribution periods from **January 2026** (assumption A1).
For 2026 the Institute's published figures are used; for 2027 and later a caller supplies the figures, and the rules that would look them up decline by name.

**Figures not in the text** are the Institute's (section 7): the basic amount under paragraph (3) for 2026 (10,382), the average wage for contributions for 2026 (13,769 under s 2, used; 13,566 under s 1, recorded), the monthly minimum wage (6,247.67 from 1.4.2025, 6,443.85 from 1.4.2026), and the reduced collection threshold for 2026 (7,703).

**Composition with IL-04.** IL-04's s 337 takes as an input "the monthly income on which contributions are computed … (s 348 and Schedule K, row IL-05)"; that is this row's `s 348 — the income on which contributions are computed, for`.
This row's s 342(c) takes as an input the column D amount of each branch on the wage, which is IL-04's `the column D deduction under`, per branch.
**(0.4.0)** Or, in the rules that take the wage (05-RC2), column D as a function of an income, which those rules apply to the wage as s 348(a) takes it into account; IL-04's `the column D deduction under` on an income is that function.

## 2. Coverage table

Line numbers are lines of `../../registers/source-bundle/national-insurance-law-consolidated-version-5755-1995.he.wiki.txt`.

**Totals.** s 342, s 348 and Schedule K: **32 encoded, 8 inert, 1 out-of-scope, 0 deferred** (41 rows).
s 1 terms the slice uses: **9 encoded** (of which 8 as inputs or input conventions), **1 inert**, **3 out-of-scope** (13 rows).
Provisions outside the slice that it refers to, or that displace it: **21 out-of-scope** rows, each with its reason.
Altogether **41 encoded, 9 inert, 25 out-of-scope, 0 deferred**.

### s 342

| provision | line | gist | disposition | where |
| --- | --- | --- | --- | --- |
| s 342 heading and tags | 3658 | who is liable to pay contributions; tag תשפ״ה־7 | inert (the tag dates the text, A1) | `src:` heading, `nii-s342-liability-and-deduction.l4` |
| s 342(a) | 3659 | the self-employed and those who are neither pay for themselves; a wife insured only under Chapter C does not | encoded | `s 342(a)-(b) — the person liable to pay the contributions for`; **(0.4.0)** one who is both employee and self-employed in one call, `s 342(a)-(b) — the persons liable to pay the contributions for` (05-P3) |
| s 342(b) | 3660 | the employer pays for the employee; several employers each as if the only one; (d) and (e) apply | encoded | same rule; "as if the only one" is how each employer's (c) is computed; (d) below |
| s 342(c)(1) | 3661 | the employer deducts the Schedule J percentages for s 335(a), (d), (e), (g), (h), (i) | encoded (F12, F13; **(0.4.0)** F25) | `the branches of the subsections of section 335 that section 342(c)(1) names`, `s 342(c)(1) — the deduction it requires, for`; **(0.4.0)** on the wage as s 348(a) takes it into account, `s 342(c) — the amount the employer deducts from a wage of` (05-RC2) |
| s 342(c)(2) | 3662 | no deduction while a senior citizen pension is payable, or after 70 (a man) or the Part D age (a woman); police and prison officers: not item 6; the employer may reduce | encoded (F9, F10, F19, F21) | `s 342(c)(2) — no deduction is made for the month, for`, `s 342(c) — the amount the employer deducts from the wage, for`, `s 342(c)(2) — the amount by which the employer may reduce …` |
| s 342(d) chapeau | 3663 | several employers | encoded | `section 342(d) does not apply: the insured person works for one employer` |
| s 342(d)(1) | 3664 | actual deduction below the coordinated contributions: the employee pays the difference; the two definitions | encoded (F14) | `s 342(d) — "the actual deduction", of`, `s 342(d) — "coordinated contributions", for`, `s 342(d) — the outcome, …` |
| s 342(d)(2) | 3665 | above them: the employee is refunded | encoded | `s 342(d) — the outcome, …` |
| s 342(e) chapeau | 3666 | the Minister may set conditions, rules and dates | inert (a power) | `src:` comment |
| s 342(e)(1)-(4) | 3667-3670 | reporting; payment or refund of the (d) difference; deduction at the full rate where there is another employer; the Institute's approval | inert (powers; the regulations are not in the sources; a deduction they govern is declined; F22) | `the deduction is governed by regulations under section 342(e)(3) or an approval under section 342(e)(4), which are not encoded here` |
| s 342(e) note | 3671 | regulations of 5757-1997 published | inert | `src:` comment |
| s 342(e1) | 3672 | a renewed kibbutz member: the kibbutz pays the coordinated contributions less what the other employer deducted | encoded (F15) | `s 342(e1) — the contributions the renewed kibbutz pays for the member, for` |
| s 342(f)(1) | 3673 | an employee who is also self-employed: no reduced rate on the s 2(1) and (8) income | encoded | `s 342(f)(1) — the part of the self-employed income not at the reduced rate, for` |
| s 342(f)(2) | 3674 | unless the wage is below the threshold: the reduced rate on the difference | encoded (F16) | `s 342(f)(2) — the part of the self-employed income at the reduced rate, for` (two arities) |
| s 342(f)(3) | 3675 | regulations power | inert (a power) | `src:` comment |

### s 348

| provision | line | gist | disposition | where |
| --- | --- | --- | --- | --- |
| s 348 heading and tags | 3762 | maximum, minimum and disregarded amounts; tags into תשפ״ו־7 | inert (the tags dated, section 7) | `src:` heading, `nii-s348-maximum-minimum.l4` |
| s 348(a) | 3763 | income above the Schedule K maximum is not taken into account | encoded | `s 348(a) — the income taken into account, of`, `the Schedule K maximum for`; **(0.4.0)** also inside the s 342(c), (d) and (e1) rules that take the wage, `s 342(c)(1) with s 348(a) — the income the deduction is taken on, from a wage of` (05-RC2, F25) |
| s 348(a1) | 3764 | non-work income not exempt under s 350 and not above 25% of the average wage is not taken into account | encoded (F3, F4; the other reading also encoded, for comparison) | `s 348(a1) — the income not from work that is not taken into account, for`, `s 348(a1), read as all or nothing — …` |
| s 348(b) | 3765 | no income or below the Schedule K minimum: as if the minimum | encoded (F6, F11, F18) | `s 348(b) — no income, or an income that does not reach the minimum: of`, `s 348(a) and (b) — …` |
| s 348(c) | 3766 | the Minister may change the minimum amounts by order | encoded (the power's test; an order that reaches a period is declined) | `s 348(c) — the order is within the Minister's power`, `an order under section 348(c) changed a minimum amount …` |
| s 348(d) | 3767 | unemployment benefit for a full month: as if the item 3 minimum | encoded where its readings agree (F5, F7) | `s 348(d) — the income on which contributions are computed, for` |
| s 348(e), permanent text | 3768 | volunteers, yeshiva students, civil service: as if the item 3 minimum | encoded (F6, F7) | `s 348(e) — the person is of a class both texts name`, `s 348(e) — the income regarded as the item 3 minimum, for` |
| s 348(e), temporary text | 3769 | the same with national-civic service, until 31.8.2026, and after it for those who began before | encoded (a dated arm, F8; A3) | `the expiry of the National-Civic Service Law, which ends the temporary text of section 348(e)`, `s 348(e) — the person serves in national-civic service in a period the temporary text reaches` |

### Schedule K

| provision | line | gist | disposition | where |
| --- | --- | --- | --- | --- |
| heading, references, sub-heading, tags | 4751-4755 | "maximum and minimum income for contributions"; ss 345(e), 348, 349; tags to תשע״ב־2 | inert | `src:` heading, `nii-schedule-k.l4` |
| table header | 4757 | item, for whom, maximum income, minimum income | encoded (the four items) | nouns `An item of Schedule K` |
| item 1, employee, month | 4758 | max the basic amount × 5; min the minimum wage of the quarter's first month | encoded | `Schedule K item 1 — the maximum income for a month, under`, `… the minimum income for a month in` |
| item 1, employee, quarter | 4759 | max month × 3; min month × 3 | encoded | `Schedule K item 1 — the maximum income for a quarter, under`, `… the minimum income for` |
| item 1, employee, year | 4760 | the totals over the quarters | encoded | `Schedule K item 1 — … for a year, under` |
| item 2, self-employed, quarter | 4761 | max 5 × the basic amount × 3; min 25% of the average wage of the quarter's first month × 3 | encoded | `Schedule K item 2 — …` |
| item 2, self-employed, year | 4762 | the totals over the quarters | encoded | `Schedule K item 2 — … for a year, under` |
| item 3, maximum | 4763 | as item 1, for a quarter or a year | encoded | `Schedule K item 3 — the maximum income …` |
| item 3, minimum, quarter | 4763 | 5% of the average wage of January (of October for the fourth quarter) × 3 | encoded | `the average wage items 3 and 4 read for`, `Schedule K item 3 — the minimum income for` |
| item 3, minimum, year | 4764 | the total over the quarters | encoded | `Schedule K item 3 — the minimum income for a year, under` |
| item 4, maximum | 4765 | as item 2 | encoded | `Schedule K item 4 — the maximum income …` |
| item 4, minimum, quarter | 4765 | 15%, the same months as item 3 | encoded | `Schedule K item 4 — the minimum income for` |
| item 4, minimum, year | 4766 | the total over the quarters | encoded | `Schedule K item 4 — the minimum income for a year, under` |
| (no monthly cell for items 2-4) | 4761-4766 | — | encoded as a third of the quarter (F2) | `a month's share of the quarter's figure` |
| definitions chapeau and tag | 4769-4770 | "in this Schedule" | inert | `src:` comment |
| "quarter" | 4771 | three months from 1 January, April, July or October of a tax year | encoded | `the quarter that contains month`, `the first month of`, `the four quarters of a tax year` |
| "minimum wage" | 4772 | the minimum wage applicable to the particular employee under the Minimum Wage Law | encoded (as the employee's input, F11) | nouns `The minimum wage applicable to the employee in the first month of each quarter` |
| "basic amount" | 4773 | as in paragraph (3) of the s 1 definition | encoded (as an input) | `the basic amount, under` |
| Schedule K1 | 4775-4784 | breach periods and maximum charges, referred to by s 369 | out-of-scope | Neither s 342 nor s 348 refers to it; its only reference is s 369 (line 4776), a provision on charging an employer who did not register or pay, which is not in this row. |

(The "no monthly cell" row records a reading, not a provision, and is not counted in the totals.)

### s 1 terms the slice uses

| term | line | disposition | where, or why not |
| --- | --- | --- | --- |
| הסכום הבסיסי, paragraph (3), with its update clause (2) | 191, 192, 196 | encoded (as an input, constant in a tax year) | `The figures Schedule K reads for a tax year`; the 2026 figure published; the update by the index is s 1's and not encoded |
| השכר הממוצע | 222-226 | encoded (as an input) | `the average wage as updated on 1 January`; which figure is fork F1 |
| יום העדכון | 225 | encoded | `the average wage in force in month`: 1 January, and any later update day |
| שנת מס | 227 | encoded (input convention: a calendar year) | nouns |
| משרת בשירות לאומי–אזרחי | 173 | encoded (as an input: the day service began) | s 348(e) temporary text |
| מתנדב בשירות לאומי או בהתנדבות קהילתית | 174 | encoded (as an input) | s 348(e) |
| גמלת אזרח ותיק מיוחדת | 135 | encoded (folded into the pension input, as s 342(c)(2) itself folds it) | `The senior citizen pension in the month` |
| חוק המשטרה / חוק שירות בתי הסוהר | 145, 164 | encoded (as an input: a police or prison officer) | s 342(c)(2) |
| קיבוץ מתחדש / חבר קיבוץ מתחדש | 217, 138 | encoded (as inputs: s 3A met) | s 342(e1) |
| השר | 126 | inert | the Minister of ss 342(e) and 348(c); row IL-04 encodes the definition |
| מעביד / עובד / עובד עצמאי | 172, 204, 206 | out-of-scope (row IL-04 encodes them) | The column of insured person is an input; IL-04's s 1 rules decide it. |
| שירות לאומי / התנדבות קהילתית / שירות אזרחי | 221 | out-of-scope | s 348(e) uses "civil service as defined in s 6(a) of the Deferral of Service for Yeshiva Students Law", not the s 1 definition (which points to the Civil Service Law); "national service" and "community volunteering" reach (e) through the s 1 definition of the volunteer, line 174. |
| מדד | 171 | out-of-scope | Used by the basic amount's update, which this row takes as a published figure. |

### Provisions outside the slice that it refers to, or that displace it

| provision | line | referred to by | disposition | reason, and how this row takes its result |
| --- | --- | --- | --- | --- |
| s 335 | 3610-3620 | s 342(c)(1); s 348(a) | out-of-scope | Which branches a person pays. Its answer is the input `branches for which contributions are payable under section 335` (IL-04's name); its subsections are mapped to branches for (c)(1) (F12). |
| s 337 and Schedule J | 3625-3629, 4709-4749 | s 342(c)(1), (c)(2) item 6, (e), (f) | out-of-scope (row IL-04) | The rates. s 342(c) takes the column D amount per branch as an input; s 342(f) returns the parts of the income each rate applies to. |
| s 334(a) | 3605-3607 | s 342(e)(3), (f) | out-of-scope (row IL-04) | The reduced collection threshold: an argument of (f), with the Institute's 2026 figure for 2026. |
| s 344 | 3684-3697 | s 348 ("his income") | out-of-scope | An employee's monthly income: the input `income from work in the period`. |
| s 345 | 3715-3734 | s 348; Schedule K's heading cites s 345(e) | out-of-scope | The annual income of the self-employed and others; (e) charges advances on the Schedule K minimum when nothing else is known. The income is an input. |
| s 349 | 3771-3772 | (Schedule K's heading) | out-of-scope | The Minister's power to change or replace Schedule K; not exercised in the sources since the 5759 change the consolidation already includes (tag ק״ת תשנ״ט, line 4755). |
| s 350, with (c) | 3774-, 3805 | s 348(a1); s 350(c) disapplies s 348(b) | out-of-scope | What is exempt is subtracted before the input; s 350(c) enters as a flag (F18). |
| s 3A | — | s 342(e1) | out-of-scope | Whether a renewed kibbutz member meets 3A(a) and (b): inputs. |
| s 245(b2) | 2474 | s 342(c)(2) | out-of-scope (repealed) | "(בוטל)". The cross-reference is checked, red (F10). |
| Schedule A1 Part D | 4431-4453 | s 342(c)(2) | out-of-scope | A woman's age by month of birth: an input in months. The tests use its last row (70, for a woman born in May 1950 or later, line 4453). |
| Chapter C | — | s 342(a) | out-of-scope | On what footing a woman is insured: an input. |
| Chapter G | — | s 348(d) | out-of-scope | Whether unemployment benefit was received for a full month: an input. |
| Chapter 15's collection provisions (ss 352-364 and on) | — | (what follows non-payment) | out-of-scope | Why ss 342(a)-(d) are encoded as who and how much, not as obligations (module header). |
| s 2 | 230-239 | s 1 "the average wage" | out-of-scope | Its (b) changes the average wage "for benefits and contributions"; the reason for fork F1. |
| the regulations of 5757-1997 under s 342(e) | 3671 | s 342(e)(3)-(4) | out-of-scope | Not in the sources; a deduction they govern is declined. |
| Income Tax Ordinance s 2 | — | ss 342(f), 348(a1) | out-of-scope | The sources of income: the inputs are split by source. |
| Minimum Wage Law | — | Schedule K "minimum wage" | out-of-scope | The employee's minimum wage is an input; the Institute's 2026 figures for an employee aged 18 or over are published figures. |
| Deferral of Service for Yeshiva Students Law s 6(a) | — | s 348(e) | out-of-scope | Who serves in civil service as it defines: an input. |
| National-Civic Service Law s 36(a) | — | s 348(e) temporary text | out-of-scope | Its expiry date ends the temporary text; read from Amendments 7-9 (section 7). |
| Police Law (Disabled and Fallen), Prison Service Law (Disabled and Fallen) | — | s 342(c)(2) | out-of-scope | Who is a police or prison officer within them: an input. |
| s 369 | — | Schedule K1 | out-of-scope | See Schedule K1 above. |

## 3. Assumptions

**A1. Contribution periods from January 2026 only; earlier periods are declined by name.**
s 342's last tag, תשפ״ה־7, counts to the Law for the 2025 budget year (row IL-04's identification, A1 there).
That Law, read from the Knesset's PDF (section 7), says in its s 19(4) that in s 342 "everywhere, instead of '60% of the average wage' shall come 'the reduced collection threshold', and instead of 'from 60% of the average wage', 'from the reduced collection threshold'", and in its s 21 that its National Insurance chapter commences on 1 January 2026.
So the deposited s 342 is the text from 1 January 2026, and before it (e)(3) and (f) read "60% of the average wage"; that earlier wording is known but not encoded, because its Schedule J is not (IL-04 declines 2025 too).
s 348 and Schedule K were probably the same in 2025 apart from the date in (e)'s editors' note (section 7), but this row answers from 2026 only, with IL-04 and with s 342.

**A2. The year and month of the period are explicit inputs; the dated arms select on them.**
The rule-effective-time axis was not used, as in rows IL-03 and IL-04: Schedule K speaks of "the first month of the quarter" and s 348(e)'s temporary text of a date, both facts of the case.

**A3. The editors' notes are relied on for s 348(e)'s two texts and their date.**
The deposited text prints (e) twice, labelled by the editors "(the permanent text)" and "(temporary provision until the expiry of the National-Civic Service Law … on 31.8.2026 …)".
Without the labels there is no rule choosing between them, so they are used as aids, cited where used.
The date was checked against the National-Civic Service Law's own amendments (section 7); whether a later amendment moved it again was not searched for.

**A4. Published figures.**
Used by the rules: the 2026 basic amount under paragraph (3) (10,382), the 2026 average wage for contributions under s 2 (13,769; fork F1), the monthly minimum wage of an employee aged 18 or over (6,247.67 from 1.4.2025; 6,443.85 from 1.4.2026), and the 2026 threshold (7,703), each with URL, time and sha256 (`nii-il05-published-figures.l4`).
The consolidation's editorial notes give the same basic amount and average wages (lines 191, 226, 233).
No figure for 2027 was published at retrieval.

**A5. Classifications outside the slice are inputs**, each listed in section 2 with its citation: the column of insured person, the branches payable, the income by source and after exemptions, the column D amounts, the employee's minimum wage, receipt of unemployment benefit, the s 348(e) statuses, s 350(c), an order under s 348(c), the senior citizen pension, the Part D age, police or prison service, s 3A, the regulations under s 342(e).
**(0.4.0)** Two presuppositions, stated (the Axiom comparison's P2 and P4): every s 348 rule presupposes contributions payable under s 335, the limb with which (a) and (a1) open (lines 3763-3764), which is not an input, so a caller asks these rules only about such contributions (05-P2); and s 342(a)'s "an insured person" (line 3659) is presupposed by `An insured person, for section 342(a)-(b)` and its 0.4.0 companion, which cannot say "not insured", so a person who is not insured is not put to them (05-P4).

**A6. Nothing is rounded.**
Neither s 342 nor s 348 nor Schedule K says to round; the Institute publishes whole shekels, and the tests compare with `ROUND` where they compare with a printed figure.

**A7. Input conventions not checked:** incomes are not negative; each branch appears once in a list; updates of the average wage are listed in order of month.

## 4. Fork register

| # | where | the question | readings | taken, and why |
| --- | --- | --- | --- | --- |
| F1 | Schedule K items 2-4 (4761-4765); s 348(a1) (3764) | Which "average wage": the s 1 figure (13,566 for 2026) or the figure calculated under s 2 (13,769)? | (i) s 1; (ii) s 2 | **(ii)**: s 2(b) says that "in calculating the average wage, for benefits and contributions, these changes apply" (line 236); and every Institute figure this row checked fits (ii) and not (i): 3,442 (25% of 13,769), 143 (6.92% of 15% of 13,769), 171 (48 + 123), the 2025 table's 3,134, 627 and 1,880 (25%, 5%, 15% of 12,536, the 2025 s 2 figure for contributions). The rules take the figure in the figures record; the 2026 record uses (ii); tests show (i) does not reproduce the Institute's figures. Bears on row IL-04's open fork F5. |
| F2 | Schedule K items 2-4 | They print no figure for a month; what is a month's? | (i) a third of the quarter's; (ii) none (decline monthly periods) | **(i)**: every quarterly figure is written as a monthly amount "× 3"; s 337(a)(2) divides annual income into monthly advance periods (s 336); s 348(d) speaks of a month; the Institute prints monthly figures that are exactly a third (51,910, 3,442). |
| F3 | s 348(a1) (3764) | "the income … which does not exceed 25% of the average wage shall not be taken into account": all of it if it does not exceed, none if it does; or the part up to 25%? | (i) all or nothing; (ii) a deduction of up to the 25% sum | **(ii)**: (a)'s "the amount of the income exceeding the maximum" is read as the part above it, and (a1) is the same construction from below; the Institute's January 2026 example deducts 3,442 from rent of 12,000. (i) is encoded beside it; the readings agree up to the sum and part above it (tests). **(0.4.0, 05-X1 and P1)** The first reason is withdrawn: (a) and (a1) are not the same construction. In (a) the subject is "the amount" of the income, with יבוא (line 3763), and read as all or nothing it would disregard the whole income of anyone above the maximum, which cannot be meant; in (a1) it is "the income" itself, with תובא and a qualifying clause (line 3764), and all or nothing gives a cliff at 3,442.25 in 2026, odd but not absurd. On the words the text reads at least as naturally as (i). (ii) is kept because the Institute's published example applies it (rent of 12,000 charged on 8,558); a second encoder (Axiom) took (i). The answer is unchanged. |
| F4 | s 348(a1) | The 25% sum has no period. | (i) a month's; (ii) scaled to the period | **(i), and other periods declined**: the average wage is a monthly figure, and the Institute applies the sum "per month". A quarter or year with income not from work is declined by name. |
| F5 | s 348(d) (3767) | (d) has no condition "who has no income or whose income does not reach". A deeming (the item 3 minimum whatever the income), or a floor like (e)? | (i) deeming; (ii) floor | **neither; answered only where they agree**: income not above the item 3 minimum gives the minimum under both; above it, declined by name. No source settles it. |
| F6 | Schedule K item 3 (4763) | "an insured person as stated in s 348(d) and (e)": the classes (d) and (e) name, or only those meeting (e)'s income condition? | (i) the classes; (ii) the classes with the condition | **(i)**: (ii) puts a yeshiva student with a little income on item 4's 15% minimum, above the 5% minimum of one with none (a cliff the schedule's own grading does not suggest). A test shows (i)'s answer (1,557.75, not 2,065.35). |
| F7 | items 1-3; s 348(d), (e) | An employee or a self-employed person who is also in a class (d) or (e) names: which item? | (i) item 1 or 2 by the column; (ii) item 3 | **(i), with declines**: items 1 and 2 are named by status. Where it matters, declined: (d) for an employee or self-employed person; (e) for one whose income is below the item 3 minimum (then (e) says the item 3 minimum and (b) says item 1's or 2's). The Institute's yeshiva page charges "one who works … according to the wage". |
| F8 | s 348(e) temporary text (3769) | The date and its edges. | — | The expiry is 31.8.2026 (the editors' note, matching Amendment 9). A month ending by then is within the temporary text; "began before" is strict (one who began on 31.8.2026 is not reached in September); a quarter or year across the date, for one who began on or after it, is declined. |
| F9 | s 342(c)(2) (3662) | "for the time …": a month in which the age is reached after its first day, or the pension is payable for part of it. | (i) apportion the month; (ii) whole month one way | **declined**: the text speaks of time and the wage is monthly; how it is divided is not said. A month whose first day is on or after the day the age is reached is wholly "after". |
| F10 | s 342(c)(2) | "subject to s 245(b2)", which is repealed | — | **no effect**; checked red. |
| F11 | Schedule K "minimum wage" (4772) | Whose minimum wage? | — | **the particular employee's**, as the definition says (partial, daily or hourly as applicable): an input. The tests use the Institute's full monthly figure for an adult, and a scenario partial figure. For an employee with none given, item 1's minimum declines by name. |
| F12 | s 342(c)(1) (3661); s 335 (3611-3619) | Which branches are "contributions payable under s 335(a), (d), (e), (g), (h) or (i)"? | — | maternity ((a), (i)), accident injury ((d)), unemployment ((e)), disability ((g)), long-term care ((h)), senior citizens and survivors ((i)); read from s 335's text. Column D prints figures for exactly these (row IL-04's test). |
| F13 | s 342(c)(1) | A deduction branch with no column D amount in the case | — | **declined by name**, not taken as 0. An amount given for a branch (c)(1) does not name is ignored. |
| F14 | s 342(d) "coordinated contributions" (3664) | Does (c)(2) apply to what one employer "would have had to deduct"? | — | **yes**: one employer would have had to deduct under (c) as a whole. |
| F15 | s 342(e1) (3672) | The other employer deducted more than the coordinated contributions. | — | **declined**: (e1) speaks only of the kibbutz paying the difference. |
| F16 | s 342(f)(2) (3674) | "lower than" the threshold | — | **strict**; at the threshold the difference is nil anyway, so nothing turns on it. |
| F17 | s 342(b) and s 348(b) | With several employers, is (b)'s minimum applied to each employer's wage ("as if he alone were his employer") or to the total? | — | **not modelled**: the caller supplies the income the floor applies to. **(0.4.0)** It is also why the rules that take the wage apply s 348(a) and not (b): fork F25. |
| F18 | s 350(c) (3805) | It disapplies s 348(b); does it reach (d) and (e)? | (i) (b) only; (ii) all minimums | **(i)**: it names (b) alone. A test shows a yeshiva student under s 350(c) still at the item 3 minimum. |
| F19 | s 342(c)(2) | The day a person "reaches" an age | — | the date of birth plus the age in months, keeping the day of the month or the month's last day when it is shorter (`add months`). **(0.4.0)** The shorter month is fork DATE ("Version 0.4.0" above), which waits on Meng (BACKLOG IL-24); this reading is kept until then. **(0.5.0)** Ruled (SHRUG): declined by default; this reading is kept by name, `the last day of that month`. |
| F20 | Schedule K "for a year" | A person in a category for part of a year | — | **not modelled**: the yearly figures are for the whole tax year. |
| F21 | s 342(c)(2) "the deduction in item 6 of Schedule J" | — | — | item 6 is unemployment (line 4725); only that branch's column D amount is left out for a police or prison officer. |
| F22 | s 342(e)(3)-(4) (3669-3670) | "column E of Schedule J" for deduction rates | (i) column D intended; (ii) as written | **not resolved**: (e) is a power and decides nothing here; checked red. |
| F23, F24 | (0.3.0) | see "Version 0.3.0" above | — | — |
| F25, DATE | (0.4.0) | see "Version 0.4.0" above | — | — |

**Where I looked for others and found none:** s 342(a)'s exception (one class, one limb); s 348(c)'s conditions (two facts of the order); Schedule K's yearly sums (the total of four quarters, read as written).

## 5. Answer table

Schedule K for 2026, with the basic amount 10,382, the average wage 13,769 (F1) in every month, and the full monthly minimum wage of an adult employee (6,247.67 in January; 6,443.85 in April, July and October).
"(F2)" marks a monthly figure the schedule does not print.

| item | max, month | max, quarter | max, year | min, month | min, quarter | min, year |
| --- | --- | --- | --- | --- | --- | --- |
| 1, employee | 51,910 | 155,730 | 622,920 | 6,247.67 (first quarter), 6,443.85 (others) | 18,743.01; 19,331.55 | 76,737.66 |
| 2, self-employed | 51,910 (F2) | 155,730 | 622,920 | 3,442.25 (F2) | 10,326.75 | 41,307 |
| 3, s 348(d) and (e) | 51,910 (F2) | 155,730 | 622,920 | 688.45 (F2) | 2,065.35 | 8,261.40 |
| 4, another insured | 51,910 (F2) | 155,730 | 622,920 | 2,065.35 (F2) | 6,196.05 | 24,784.20 |

With the s 1 average wage (13,566) the minimums would be 3,391.50, 678.30 and 2,034.90 a month; the Institute prints figures matching the table above, not these.

Worked figures the tests assert (2026 unless marked):

| facts | answer |
| --- | --- |
| employee, wage 60,000, March | income 51,910 (s 348(a)) |
| employee, wage 5,000, February / May | 6,247.67 / 6,443.85 (s 348(b)) |
| one who is neither, rent 12,000, January | 8,557.75 (the Institute: 8,558; with its composite rates, 1,035 a month) |
| one who is neither, rent 3,000 / no income | 2,065.35 |
| one who is neither, rent 4,000, under s 350(c) | 557.75 |
| unemployment benefit for a full month, income up to 688.45 / above it | 688.45 / declined (F5) |
| yeshiva student, no income / rent 5,000 | 688.45 / 1,557.75 (F6) |
| national-civic service begun 30.8.2026 / 31.8.2026, September 2026 | 688.45 / 2,065.35 (F8) |
| employer's deduction, wage 7,000, all branches (column D, temporary version) | 72.80; police officer 71.40; pension payable all month 0 (employer may reduce by 72.80) |
| man born 15.3.1956: February / March / April 2026 | 72.80 / declined (F9) / 0 |
| two employers at 6,000 each, permanent version, threshold 8,000 (scenario 2027) | each deducts 24; coordinated 218.80; the employee pays 170.80 |
| renewed kibbutz member, same, other employer deducted 24 | the kibbutz pays 194.80 |
| employee also self-employed, wage 5,000, self-employed income 6,000 | 2,703 at the reduced rate, 3,297 above |
| **(0.4.0)** employer's deduction from a wage of 60,000, February 2026, s 348(a) applied (51,910) | 3,174.6012 at the printed totals; 2,144.5781 at the items |

## 6. Nouns to reconcile at IL-07

Read from the sibling deposits `legalese-2026-10-il-04` and `legalese-2026-10-il-06` (read-only); nothing here depends on IL-06 and nothing in either was changed.

- **Declared twice because IMPORT failed (section 8).** `A branch of insurance` and `A column of insured persons in Schedule J` are IL-04's, constructor for constructor; delete this row's copies at IL-07. The same for the three published figures whose names are IL-04's: `the reduced collection threshold for 2026, as published by the National Insurance Institute` and the two `the average wage from 1 January 2026 …` (same figures, different fetches).
- **Schedule J's column D.** This row's input `A branch's column D amount` (a branch and an amount) is IL-04's `the column D deduction under v on a wage of … in the branches …`, taken per branch. At IL-07, compute it there.
- **The case records.** IL-04's `An employee's month of contributions` (`calendar year of the month`, the branches, the monthly income, s 341 and s 343 flags) and this row's `An employee's month under section 342(c)` (`tax year`, `month`, the branches, the column D amounts, pension, age, police) and `An insured person's period under section 348` describe overlapping facts. The year field is `calendar year of the month` there and `tax year` here; a tax year is a calendar year in both (IL-04 F12). IL-04's `monthly income on which contributions are computed` is this row's output.
- **The person.** IL-04 `A person who works`; IL-06 `A person` (insured under Chapter 11, resident, a housewife under s 238 …); this row `An insured person, for section 342(a)-(b)` (column; insured under Chapter C only as a wife) and the age record `The insured person, for the age limb of section 342(c)(2)` (`a man` / `a woman` with her Part D age). IL-06 has `Father or mother`, a second sex distinction. `date of birth` is a field name here and in IL-06's `A child`.
- **The basic amount.** IL-06 `The basic amounts for the child allowance` (paragraph (2), fields `under paragraph (2)(a)` …); this row the paragraph (3) figure as a field of `The figures Schedule K reads for a tax year` and as `the basic amount under paragraph (3) from 1 January 2026, as published by the National Insurance Institute`.
- **(0.5.0) Fork DATE's reading.** `A reading of a day of birth the month of the age lacks` is this row's; the same ruling is to be carried out in rows IL-06 and IL-08 (BACKLOG IL-40 and IL-41, queued when this was written), and any reading types they declare are to be joined with this one at IL-07.
- **(0.4.0) Column D as a function.** The rules of 05-RC2 take column D as functions of an income, by branch and at the printed totals; at IL-07 they are IL-04's `the column D deduction under` with the version, threshold and average wage fixed, the second over the deduction branches.
  The record of 05-P3, `An insured person who may be both an employee and self-employed, for section 342(a)-(b)`, has two booleans where IL-04's `A person who works` and this row's one-column record each have one status.
- **Refusal wording.** For the year boundary: IL-04 per provision ("section 334(a) as it stood before 1 January 2026 is not in the deposited text"); this row once for the row ("this row answers contribution periods from January 2026 only"). For unpublished figures: IL-04 and this row "had not been published when this encoding was made"; IL-06 "had not been published when this model's sources were fetched".

## 7. Sources: what was fetched, and what was not

The deposited source was read and its sha256 verified (`78bf47ee…2a97`) on 2026-10-06 before use.

**National Insurance Institute pages**, fetched 2026-10-06 with curl directly (not through the proxy); bytes not deposited, the site reserving its rights:

| what | URL | UTC | sha256 | what it says that this row uses |
| --- | --- | --- | --- | --- |
| rates, self-employed | `https://www.btl.gov.il/Insurance/Rates/Pages/%d7%9c%d7%a2%d7%a6%d7%9e%d7%90%d7%99%d7%9d.aspx` | 14:49:42 | `5d1e1a490b11bb63f1430677185a977045a173d32cde6fca5317836a34827567` | threshold 7,703; maximum income 51,910 a month; "one whose income is below 3,442 a month pays on the minimum income"; from 01.01.2026 |
| rates, employees | `https://www.btl.gov.il/Insurance/Rates/Pages/%d7%9c%d7%a2%d7%95%d7%91%d7%93%d7%99%d7%9d%20%d7%a9%d7%9b%d7%99%d7%a8%d7%99%d7%9d.aspx` | 14:49:54 | `34ade94d9f315ad684979636e7b3d1e166cb09bf676b1ea1a20f4d82fa242c7b` | threshold 7,703 and maximum 51,910 from 01.01.2026 |
| rates, neither | `https://www.btl.gov.il/Insurance/Rates/Pages/%d7%9e%d7%99%20%d7%a9%d7%90%d7%99%d7%a0%d7%9d%20%d7%a2%d7%95%d7%91%d7%93%d7%99%d7%9d%20%d7%95%d7%91%d7%a2%d7%9c%d7%99%20%d7%94%d7%9b%d7%a0%d7%a1%d7%94%20%d7%a9%d7%9c%d7%90%20%d7%9e%d7%a2%d7%91%d7%95%d7%93%d7%94.aspx` | 14:49:55 | `1c86c85f9a1fe65f5a95a6e0e1e9aa4fdc350aff2b518f75f6e0d633e12c8e92` | no income: 143 National Insurance and 123 health, 266 a month; rent of 12,000 in January 2026: "income up to 3,442 a month is exempt", charged on 8,558, 931.29 + 104.05 = 1,035 |
| yeshiva student, amount | `https://www.btl.gov.il/Insurance/National%20Insurance/type_list/yesivatalmid/Pages/SecomTlmidYesiva.aspx` | 14:51:01 | `39720f8c5ecbcec9ce267cb4a54905a6a9d07520b798e7c8c4c52a0e5da2125a` | 171 a month at the minimum from 01.01.2026; and (open question 3) a student who has not regularised his military status is charged from 1.1.26 "full National Insurance (without discount)", 95 more a month |
| not working, amount | `https://www.btl.gov.il/Insurance/National%20Insurance/type_list/NotWorking/Pages/ScomNotWorking.aspx` | 14:51:08 | `c2692a7d08e18b81a64c9a566e42a0e5727ad36a06b6c737af65aaec9e325efa` | 266 a month at the minimum "except a woman married to an insured resident" (cf. s 342(a)) |
| minimum income, self-employed (table) | `https://www.btl.gov.il/Mediniyut/GeneralData/rates_1954_2007/Hachnasa/Pages/ovedAtzmaii.aspx` | 14:49:44 | `c8f8edf3dfdc58db79ad61f6d32d3ef73dc6bfd1ec35a620a980acdb69d10a16` | from 01/01/2025: minimum 3,134, threshold 7,522, maximum 50,695 a month (no 2026 row) |
| minimum income, neither (table) | `https://www.btl.gov.il/Mediniyut/GeneralData/rates_1954_2007/Hachnasa/Pages/%d7%9c%d7%90%20%d7%a2%d7%95%d7%91%d7%93%20%d7%95%d7%9c%d7%90%20%d7%a2%d7%95%d7%91%d7%93%20%d7%a2%d7%a6%d7%9e%d7%90%d7%99.aspx` | 14:53:32 | `8bc34ff3f3fd636835d14ce7db26a4d904abf826afba1ce8bdce4f787df069be` | from 01/01/2025: 5% 627, 15% 1,880, maximum 50,695 a month |
| minimum income, employee (table) | `https://www.btl.gov.il/Mediniyut/GeneralData/rates_1954_2007/Hachnasa/Pages/Sahir_Maasik.aspx` | 14:53:30 | `3135d61d26977f6c1a4bfc5957f1752af65e266079eae90b40501db56965b9ca` | the employee's minimum is the minimum wage (not used for a figure: its 2025 rows date 6,247.67 from 01/02/2025, where the minimum wage page dates it from 01.04.2025) |
| average wage | `https://www.btl.gov.il/Mediniyut/GeneralData/Pages/%d7%a9%d7%9b%d7%a8%20%d7%9e%d7%9e%d7%95%d7%a6%d7%a2.aspx` | 14:49:57 | `0afd95b65113a99dfc9bb9cd277090a927d26fa0c39b49a75be4ec1931829532` | from 01.01.2026: 13,566 (s 1) and 13,769 (s 2), each for benefits and for contributions; 2025 for contributions 12,379 and 12,536 (0.0% change), for benefits 13,153 and 13,316 |
| basic amount | `https://www.btl.gov.il/Mediniyut/GeneralData/Pages/%d7%94%d7%a1%d7%9b%d7%95%d7%9d%20%d7%94%d7%91%d7%a1%d7%99%d7%a1%d7%99%20%d7%9c%d7%97%d7%99%d7%a9%d7%95%d7%91%20%d7%a7%d7%a6%d7%91%d7%90%d7%95%d7%aa.aspx` | 14:52:50 | `c585c6469d5c358d0230523208b54b6501ad624b06775eed2235f52bdc0a13d9` | basic amount 3, "for … computing the maximum income for collecting contributions": 10,382 from 1.01.2026, 10,139 from 1.01.2025 |
| minimum wage | `https://www.btl.gov.il/Mediniyut/GeneralData/Pages/%d7%a9%d7%9b%d7%a8%20%d7%9e%d7%99%d7%a0%d7%99%d7%9e%d7%95%d7%9d.aspx` | 14:52:49 | `0c7ff9205881f9b13396791c2b058bb511b1ec2e51bd6a9cb9ae20effa5ac743` | age 18 and over, monthly 6,443.85 from 01.04.2026, 6,247.67 from 01.04.2025 |

Also fetched and read, nothing taken: the category pages for self-employed, employees, the not-working, income not from work (with its tab pages), yeshiva students, national service (its amount tab printed no figure), the rates index, the General Data index and the 1954-on rates index. None is cited by a rule or test, and their sha256s are not recorded here (the session's fetch log was deleted with the fetched bytes at the end of the session).
The Institute's pages describe themselves as general information and not the binding text of the Law; they are used as the regulator's published figures and examples, not as law.

**Amending Laws from the Knesset**, fetched 2026-10-06 **through the Israeli-IP proxy** (an ssh tunnel to an EC2 instance; `curl --socks5-hostname localhost:1080`), PDFs, not deposited, text extracted with `pdftotext -raw`:

| Law | URL | UTC | sha256 | what it says that this row uses |
| --- | --- | --- | --- | --- |
| Law for the 2025 budget year (legislative amendments), Sefer HaChukim 3384, p. 395 | `https://fs.knesset.gov.il/25/law/25_lsr_6133485.pdf` | 14:54:06 | `eba7e1fa570a3ece265d87f379543024da038ee51af3f959d4c74162f5edecfa` | Chapter E, s 19(4): in s 342 "60% of the average wage" becomes "the reduced collection threshold"; s 19(6): the same "everywhere" in Schedule J, "as defined in s 334(a)"; s 20: amends s 7 of Amendment 252 (column C 0.17 to 0.16); s 21: the chapter commences 1 January 2026 |
| National Insurance Law (Amendment 252 and temporary provision), 5785-2025 | `https://fs.knesset.gov.il/25/law/25_lsr_5482787.pdf` | 14:55:34 | `d6c450ca0b869d1edb036b0f96bffbd79be6670336d9b5aa888da6cf2ecc8904` | s 6: commences 1 January 2025; s 7 (temporary provision, for contributions for 2025 and 2026, until 31 December 2026): in Schedule J, replaces the sub-column of column C headed "on the part not exceeding 60% of the average wage", and the sub-column of column D headed "on the part of the wage not exceeding 60% of the average wage", with new figures under the same headings |
| National-Civic Service Law (Amendment 7), 5785-2025 | `https://fs.knesset.gov.il/25/law/25_lsr_7458944.pdf` | 14:54:08 | `b0d30c46949e5aac77ae1d87cfb30bdd62a20fa2825a42bbc9e6feb53ee4716f` | s 36(a) expiry: 30.6.2025 becomes 15.11.2025 |
| National-Civic Service Law (Amendment 8), 5786-2025 | `https://fs.knesset.gov.il/25/law/25_lsr_9833371.pdf` | 14:54:10 | `2482417b87a0e0af223e0cbc9bd43fb90bfc1a798d22955dc735a6ce24e795c4` | 15.11.2025 becomes 31.3.2026; commences 16.11.2025 |
| National-Civic Service Law (Amendment 9), 5786-2026 | `https://fs.knesset.gov.il/25/law/25_lsr_12223999.pdf` | 14:54:12 | `cb19f7be69ae6b1b49057171cd00fda46c50e4997e37f51a2f240f7881888100` | 31.3.2026 becomes 31.8.2026 |

**Tags on s 348.** Counting the 5786 list at the head of the source (line 7) as row IL-04 counted 5785's: bare תשפ״ו is Amendment 8 of the National-Civic Service Law (p. 18) and תשפ״ו־7 is its Amendment 9 (p. 470); with IL-04's count, תשפ״ה־11 is its Amendment 7.
Each only moves that Law's expiry date, so these tags record the date in the editors' note on s 348(e)'s temporary text, not a change of s 348's words.

**Attempted and failed:** nothing.
**Not attempted:** the Central Bureau of Statistics (the average wage and the index are taken as published by the Institute); a search for an amendment of the National-Civic Service Law after Amendment 9.

## 8. The cross-directory IMPORT, and what was done instead

The brief asked for IL-04's modules to be imported by relative path.
With this binary, `IMPORT \`../legalese-2026-10-il-04/nii-il04-nouns\`` (and the same for `nii-s334-interpretation` and `nii-schedule-j`) fails with "I could not find a module with this name: nii-il04-nouns": the resolver reduces the path to its bare module name and tries the importing file's own directory, the embedded library, `~/.local/share/jl4/libraries/` and the VS Code bundle (tested 2026-10-06; the probe file was deleted).
The library-resolution reference in l4-ide (`doc/reference/libraries/resolution.md`) says the CLI's project root is the importing file's own directory.
The only other route, `JL4_LIBRARY_PATH`, the brief forbids.

A symlink was also tried, in the scratchpad only: a symlink to IL-04's `nii-schedule-j.l4` resolves, but that module's own imports (`nii-il04-nouns`, `nii-s1-definitions`, `nii-il04-published-figures`) are then looked for beside the symlink and not found, so the whole import closure would have to be linked.
Nothing was linked in the deposit.

So, as the brief directs, this row declares again the IL-04 types it needs with the same names and constructors, takes IL-04's computed results (the column D amounts, the threshold) as inputs, and uses IL-04's published-figure names for the three figures both rows need.
Section 6 lists what to delete or join at IL-07.

## 9. Observations about the source, for whoever maintains it

- **s 342(e)(3)-(4) say "column E" of Schedule J for deduction rates**; the deduction is column D (F22; red).
- **s 342(c)(2) is subject to s 245(b2)**, which is repealed (F10; red).
- **Schedule J's temporary table, column D (row IL-04's fork F3).** The consolidation prints the temporary table's column D upper heading as "above 60% of the average wage" and the lower one as "not above the reduced collection threshold" (line 4718). The enacted texts, as read here: Amendment 252 s 7(a)(3)(b) replaces only column D's lower sub-column, under its own heading "not exceeding 60% of the average wage"; the upper sub-column is the main Law's, whose "60% of the average wage" the 2025 budget-year Law s 19(6) replaced "everywhere" in Schedule J with "the reduced collection threshold" from 1 January 2026, and s 20 of that Law amended s 7's figures but not its headings. On that reading the 2026 upper heading is "above the reduced collection threshold", as in the permanent table, and the "60%" survives in the enacted text only in s 7's lower heading. This is this row's reading of three texts, offered as evidence on IL-04's F3; nothing in this row turns on it, because its s 342(c) takes the column D amounts as inputs.
- **The editors' note dates s 348(e)'s temporary text to 31.8.2026**, which matches Amendment 9; the National-Civic Service Law's expiry was moved three times in 2025-2026, the second time (Amendment 8, passed 18.11.2025) after the date it replaced (15.11.2025), with commencement on 16.11.2025.

## 10. Open questions for a domain expert

1. F1 (and IL-04's F5): is "the average wage" in Schedule K and s 348(a1) the figure calculated under s 2 (the Institute's practice), for every provision of Chapter 15?
2. F3 and F5: does the Institute read s 348(a1) as a deduction because of the text, or by practice; and does it read s 348(d) as a deeming or a floor?
   **(0.4.0)** On (a1) the words lean, if anywhere, to all or nothing (F3, as restated), so the question is whether a rule or ruling outside the Law supports the Institute's deduction.
3. The Institute's yeshiva page says a yeshiva student who has not regularised his military status is charged from 1 January 2026 the full contributions, "95 NIS more each month" (the difference between the item 4 and item 3 minimums). Nothing in the deposited s 348(e) or Schedule K turns on military status. Where is that rule?
4. F6 and F7: which Schedule K item applies to a yeshiva student or a volunteer who also works, and below what income?
5. F9: how does the Institute apportion a month in which an employee reaches 70 (or her Part D age), or in which a pension begins?
6. F22: is "column E" in s 342(e)(3)-(4) a remnant of an earlier numbering of Schedule J's columns?
7. Was the National-Civic Service Law's expiry moved again after 31.8.2026, and if not, does s 348(e)'s temporary text now reach only those who began before?
8. **(0.4.0)** Fork DATE: from what day is a man born on 29 February 70 in a year without one, for s 342(c)(2)?
   One ruling for rows IL-05, IL-06 and IL-08: BACKLOG IL-24.
   **(0.5.0)** Ruled by Meng on 2026-10-08 (SHRUG): declined by default, both other readings kept by name.
9. **(0.4.0)** Was an order under Amendment 252 s 7(b) made extending the temporary Schedule J to 2027 (row IL-04's open question 7)?
   It decides which column D a caller passes for 2027 (05-RC5).

## 11. What was not done

- **The independent test pass** (skill step 8) was not run: the brief for this row is one session with no sub-agents. Every expected value was worked out before it was asserted, by a computation that does not use this encoding; no second reader has derived them.
  **(0.4.0, 05-W1)** Stale: the pass was run after the deposit, by `fid-il-05` (`DECIDED-ANSWERS.md`, `INDEPENDENT-FINDINGS.md`, `tests-independent.l4`), deriving its own expected values without this encoding; the sentences above describe the encoding session only.
- **HG1**, a human who knows Israeli national insurance reading the modules against the Hebrew, has not been sought.
- **Semi-cleanroom** (ruled 2026-10-06): nothing from the Axiom Foundation, any RuleSpec repository, or the paths the brief lists was read, searched or fetched in this session. IL-04's and IL-06's deposits were read for names only, read-only; IL-04's `tests-independent.l4`, `DECIDED-ANSWERS.md` and `INDEPENDENT-FINDINGS.md` were not opened.

## Comparison with Axiom's RuleSpec (2026-10-06)

Written 2026-10-07 by the comparison author (`lad-il-05`), working alone, after this row was deposited and independently tested, under Meng's semi-cleanroom ruling of 2026-10-06 as the lead relayed it for this row.
Nothing in this row's modules, tests or other sections was changed; every divergence below is a finding, and every repair is proposed, not made.

### What was read

**Axiom.** A local clone of `TheAxiomFoundation/rulespec-il` at `/Volumes/transcend/src/Axiom/rulespec-il`, commit `95c6f32c87c75e318631cbd77c14b840bc536c15` ("Merge pull request #8 from TheAxiomFoundation/encode/il-nii-contributions", 2026-10-03), read-only; nothing was pulled or modified.
Files read in full, each sha256 matching the `applied_files` hash in its own encoding manifest:

| file | sha256 |
| --- | --- |
| `il/statutes/national-insurance-law-1995/section-342.yaml` | `689a3057…08de2` |
| `il/statutes/national-insurance-law-1995/section-342.test.yaml` | `fca4179d…3ca87` |
| `il/statutes/national-insurance-law-1995/section-348.yaml` | `57e9af0d…6c66ec` |
| `il/statutes/national-insurance-law-1995/section-348.test.yaml` | `c3ba4ea3…11ba3b` |
| `il/statutes/national-insurance-law-1995/schedule-k/sign-1.yaml` (the only file under `schedule-k/` besides its test) | `139f54a0…a7f29` |
| `il/statutes/national-insurance-law-1995/schedule-k/sign-1.test.yaml` | `85c9b1f2…f102` |

Also read, only the parts about these provisions: `.axiom/encoding-manifests/il/statutes/national-insurance-law-1995/section-342.json`, `section-348.json` and `schedule-k/sign-1.json` (whole; provenance only: model `gpt-6-astra` for s 342 and Schedule K, a deterministic import-hash repair for s 348, all generated 2026-09-29); `docs/ENCODING-GAPS.md` lines 638-650 (`schedule-k-monthly-minimum-and-section-348-b`) and 651-665 (`nii-schedule-a1-part-d-not-encoded`, about s 342(c)(2)); `data/coverage/tax-benefit-source-map.json`, only the values naming s 342, s 348 or Schedule K, and the instrument's `temporal_coverage` (`current_expression_only`) and the file's `validation_year` (2025).
`known-missing-money-atoms.yaml` and `known-validation-gaps.yaml` were searched with a count and contain nothing about these provisions.
The s 348 module imports one value from `schedule-k/sign-1` (read); no other file was needed to understand a value, except Schedule J's column D figures (below, under "Schedule J column D"), for which I stopped short.
What else was seen, outside that list, is set out at the end of this section.

**Ours.** The five rule modules as deposited (sha256 `nii-il05-nouns.l4` `b62351d5…e013`, `nii-il05-published-figures.l4` `05e8472d…09d`, `nii-schedule-k.l4` `d73fd96d…c975`, `nii-s348-maximum-minimum.l4` `45ea8d42…39c2`, `nii-s342-liability-and-deduction.l4` `058282cb…5691`), `nii-il05-tests.l4`, `nii-il05-tests-expected-red.l4`, `tests-independent.l4`, `NOTES.md`, `BRIEF.md`, `DECIDED-ANSWERS.md`, `INDEPENDENT-FINDINGS.md`, `check.sh`.
Row IL-04's `NOTES.md` "Repair 2026-10-07" section only (its lines 1-80), as background.

**Sources.** The consolidation (sha256 `78bf47ee…2a97`, verified): s 1 (lines 186-228), s 2 (230-239), s 245 (2464-2477), s 342 (3658-3675), s 348 (3762-3769), Schedule A1 Part D's last rows (4450-4453), Schedule J (4709-4749), Schedule K (4751-4773).
The deposited amending Laws (`registers/source-bundle/amending-laws/`, sha256 of all three verified against `SOURCES.json`), text by `pdftotext -raw`: Amendment 252 (all four pages) and the 2025 Budget-year Law's Part E, ss 19-21 (PDF pages 11-12).
Neither amends s 348 or Schedule K; the Budget-year Law s 19(4) amends s 342 ("60% of the average wage" becomes the reduced collection threshold, "everywhere"), from 1 January 2026 (s 21); Amendment 252 s 7(a)(3) replaces only the lower sub-columns of Schedule J's columns C and D.
The 2023 Economic Efficiency Law was not opened: nothing in this comparison turns on Schedule J's item 4.
The National Insurance Institute's figures are taken from this row's `NOTES.md` section 7 (the encoder's fetch, 14:49-14:53 UTC on 2026-10-06) and `DECIDED-ANSWERS.md` section 1 (the independent tester's fetch through the Israeli proxy, 21:41-21:43 UTC); they agree, and nothing was re-fetched.

Toolchain: `/Users/mengwong/.local/bin/l4` → `jl4-0.1-0ee0100b`, sha256 `64bbcb15…e118` (the binary of section 0), `JL4_LIBRARY_PATH` unset.

### Licence

`NOTICE` in the clone: "Encodings, companion test cases, parameter values, and provenance metadata in this repository are licensed under the Creative Commons Attribution 4.0 International license (CC BY 4.0)"; "incidental tooling and scripts" under Apache 2.0 (`LICENSE-CODE`); the statutes themselves are not licensed.
`LICENSE` is the CC BY 4.0 legal code, `LICENSE-CODE` the Apache 2.0 text; this confirms what the earlier comparison authors found.
Quotations from Axiom's files below are short and attributed; nothing of theirs is copied into this row.
Suggested attribution, from `NOTICE`: "Axiom Foundation RuleSpec corpus (CC BY 4.0), https://github.com/TheAxiomFoundation".

### What each encoding does, in one paragraph each

**Axiom** executes, for s 342: (a) as a person-level judgment, `liable_for_own_insurance_contributions`, from booleans `person_is_insured`, `person_is_employee`, `person_is_self_employed` and the Chapter C wife flag; (d)(1) and (d)(2) as `multiple_employer_contribution_shortfall` and `…_refund`, from a boolean `insured_employee_has_multiple_employers` and two caller-supplied amounts, `coordinated_contributions` and `actual_total_monthly_deductions`; and the man's age, 70, as a parameter.
It defers, with a reason each, (b), (c)(1), (c)(2) (the age limb, the employer's reduction, the police and prison item 6 limb), the computation of coordinated contributions, (e), (e1) and (f).
For s 348 it executes (a) only as `employee_monthly_income_after_contribution_ceiling` (the employee's monthly wage against item 1's monthly maximum) and (a1) as the excluded amount, each gated by a boolean `contributions_payable_under_section_335`; it defers (b), (d) and (e), and gives (c) as summary text only.
For Schedule K it executes the arithmetic of all four items for a month (item 1 only), a quarter and a year, with the item (`insured_item`, 1 to 4), the basic amount, the minimum wage, the average wages of January, April, July and October and the quarter (`quarter_begins_in_october`) all supplied by the caller.
Every rule is `effective_from: '0001-01-01'`.

**Ours** encodes s 342(a), (b), (c)(1), (c)(2) in all its limbs, (d) with coordinated contributions computed from (c), (e1) and (f)(1)-(2), with (e) inert and a deduction it governs refused; s 348(a), (a1), (b), (c), (d) where its readings agree, (e) in both texts; Schedule K in full, with the item derived from the person's column and the (d)/(e) classes; contribution periods from January 2026, with the Institute's 2026 figures built in (NOTES sections 1-4).

### Divergence table

Lines are lines of the deposited consolidation unless marked.

| id | provision | ours | Axiom's | source | classification | proposed repair (ours) |
| --- | --- | --- | --- | --- | --- | --- |
| X1 | s 348(a1), how much non-work income is disregarded | a deduction: the part up to 25% of the average wage (F3 (ii)); the all-or-nothing reading is encoded beside it, unused | all or nothing: `if nonwork_income… <= nonwork_income_exclusion_threshold: max(0, nonwork_income…) else: 0`; its test `nonwork_income_above_threshold_receives_no_partial_exclusion` asserts 0 on 3,000 against a sum of 2,500 | 3764; 3763 for the comparison F3 relies on | genuine ambiguity: see below | none to the answer; restate F3's reason (P1) |
| X2 | Schedule K, a monthly minimum for items 2-4 | a third of the quarter's (F2): 3,442.25, 688.45, 2,065.35 a month in 2026 | `employee_monthly_minimum_insurable_income` is `if insured_item == 1: applicable_minimum_wage_first_month_of_quarter else: 0`; its test asserts 0 for item 3 | 4761-4766 print no monthly cell for items 2-4 | theirs wrong: 0 has no source, and Axiom's own gap entry says so ("The text sets no monthly minimum for those items, which is not the same as a minimum of zero", `docs/ENCODING-GAPS.md` lines 641-643). Between ours and a refusal (the independent tester's E8), F2 stays a genuine ambiguity, already recorded | none |
| X3 | s 342(c)(2), "subject to s 245(b2)" | repealed, so no effect; checked red (F10) | a live dependency: (c)(1) and (c)(2) are deferred for want of "the operative qualification in section 245(b2)", and the deferral says a "repeal assertion" cannot replace "the required legal dependencies" | 3662 (בכפוף להוראות סעיף 245(ב2)); 2474, where (b2) reads בוטל | theirs wrong on the deposited text. Not checked against Axiom's own copy of s 245, which is out of row. No Axiom output turns on it, because the limbs it blocks are deferred | none |
| X4 | s 342(e)(3)-(4), "column E" for deduction rates | flagged red: the deduction is column D (F22) | not noticed: (e) is deferred as "upper-band withholding and Institute approvals", with no mention of a column | 3669-3670 (טור ה׳); 4717 | representational: neither computes (e); only ours tests the source against itself | none |
| X5 | s 342(a)-(b), an employee who is also self-employed | one column per call, so such a person takes two calls (the independent tester's A7) | one call, two booleans: `person_is_self_employed or not person_is_employee`, so a dual-status person is liable for himself | 3659; 3673 names the dual case | representational, with the interface gap on our side | optional (P3) |
| X6 | s 342(a), "an insured person" | presupposed: the record has no "not insured" | `person_is_insured` is an input, and false gives not liable | 3659 (מבוטח) | scope difference | optional (P4) |
| X7 | s 348(a) and (a1), "for contributions payable under s 335" | presupposed: every s 348 rule is for such contributions; the limb is not an input and not in the coverage table | `contributions_payable_under_section_335` gates both rules; false passes the wage through uncapped and excludes nothing | 3763-3764 | scope difference | state the presupposition (P2) |
| X8 | s 348(a), whose income the maximum caps | the whole income taken into account (income from work plus non-work income after (a1)), for every item and period | the employee's monthly wage only, "solely the effect of subsection (a), not a complete contribution base" (its own deferral note) | 3763: סכום ההכנסה של המבוטח העולה על הסכום המרבי | scope difference | none |
| X9 | Schedule K, the yearly maximum | one basic amount per tax year | four, one per quarter: `5 × 3 × (basic_amount_for_january_quarter… + …october_quarter…)`; its test sums 10,000, 11,000, 12,000 and 13,000 | 4760, 4762 (the sum over quarters); s 1's update clause, 192 and 196, moves the paragraph (3) amount only on 1 January | representational: the same answer for every input the deposited s 1 can produce; Axiom's test case is one it cannot | none |
| X10 | which Schedule K item applies | derived from the column and the (d)/(e) classes (F6, F7) | `insured_item` is a caller input | 4757-4765; 3765-3769 | representational; Axiom is silent on F6 and F7 | none |
| X11 | "quarter" and the average wage of a month | derived from the month (4771) and the update days (225) | caller-supplied: `quarter_begins_in_october`, `average_wage_first_month_of_quarter`, and the four monthly figures, which a caller can make inconsistent with each other | 4771; 222-225 | representational | none |
| X12 | which "average wage" | the figure calculated under s 2, 13,769 for 2026 (F1) | a bare input, `average_wage` in s 348 and `average_wage_<month>` in Schedule K; tests use invented figures (10,000 to 14,000) | 222-226; 236 | scope difference: Axiom leaves F1 to whoever supplies the figure | none |
| X13 | s 342(b), (c), (e1), (f) and coordinated contributions | computed (with refusals where the text is silent) | deferred | 3660-3662, 3664, 3672-3674 | scope difference | none |
| X14 | s 348(b), (c), (d), (e) | encoded | deferred; (c) summary text only. Axiom's own gap entry says the (b) deferral's stated reason ("no applicable monthly minimum") "is no longer true" for an employee (`docs/ENCODING-GAPS.md` lines 644-647) | 3765-3769 | scope difference | none |
| X15 | the periods answered | from January 2026 (A1); earlier periods refused, later ones only on caller figures | `effective_from: '0001-01-01'`, "current_expression_only", tests dated 2024 and January 2026 | tags at 3658, 3762, 4755 | scope difference (see "Periods") | none |
| X16 | s 342(d) with one employer, or none | a named outcome: "does not apply: the insured person works for one employer" | 0 and 0 | 3663 | representational | none |
| X17 | coordinated contributions | (c) applied to the total monthly income as one employer's wage, with (c)(2) (F14) | an input | 3664 | scope difference | none |
| X18 | s 342(c)(2), a woman's age | the Part D age is a caller input in months (F19) | deferred: Part D is not encoded (its gap entry, lines 651-664); both cite 70 for a woman born in May 1950 or later | 3662; 4453 | scope difference | none |
| X19 | the text each carries of s 342(d)(2) | quoted from line 3665 | the module summary ends (d)(2) "…לבין סכום דמי הביטוח המתואמים", one word more than line 3665's "…לבין דמי הביטוח המתואמים"; the longer phrase is (e)(2)'s, line 3668 | 3665, 3668 | theirs wrong, immaterial: no rule reads the summary. Not checked against Axiom's own copy of the consolidation, which may be a different revision | none |

**Counts.** 19 divergences: ours wrong 0; theirs wrong 3 (X2, X3, X19, the last immaterial); genuine ambiguity 1 (X1); scope difference 9 (X6, X7, X8, X12, X13, X14, X15, X17, X18); representational 6 (X4, X5, X9, X10, X11, X16).
Where both encodings compute the same quantity, they agree on every number except X1 and X2.

**X1 in detail.** Line 3764 says the non-work income "which is not exempt … and does not exceed (ואינה עולה על סכום השווה ל־25% מהשכר הממוצע)" a sum equal to 25% of the average wage "shall not be taken into account".
Our F3 reads (a1) as a deduction "because (a)'s 'the amount of the income exceeding the maximum' is read as the part above it, and (a1) is the same construction from below".
The two are not the same construction.
In (a) the subject is "the amount" of the income, masculine, with יבוא (line 3763); in (a1) it is "the income" itself, feminine, with תובא, qualified by a relative clause (line 3764).
Read as all or nothing, (a) would disregard the whole income of anyone above the maximum, which cannot be meant, so (a) must mean the part above; (a1) read as all or nothing gives a cliff at 3,442.25 (2026), which is odd but not absurd.
So on the words alone Axiom's reading is at least as natural as ours, and the text does not decide.
What supports ours is the regulator: the Institute's January 2026 example charges rent of 12,000 on 8,558, "income up to 3,442 a month is exempt" (both fetches agree; NOTES section 7, DECIDED-ANSWERS G5), which is a deduction.
This row's own tests show the readings part exactly where Axiom's case does (`nii-il05-tests.l4` lines 404-406), and our all-or-nothing rule reproduces Axiom's 0 on Axiom's own case (scratch run, below).

### Our 22 forks, and what Axiom does

| fork | ours | Axiom | verdict |
| --- | --- | --- | --- |
| F1 which average wage | s 2's, 13,769 | bare inputs; no figure | silent |
| F2 a month for items 2-4 | a third of the quarter | minimum 0 for items 2-4 (disowned by its gap entry); monthly maximum `basic × 5` whatever the item, which equals ours (51,910 at 10,382); s 348(b), (d), (e) deferred | disagrees |
| F3 (a1) deduction or all or nothing | deduction | all or nothing | disagrees (X1) |
| F4 (a1)'s sum has no period | a month's; other periods refused | the rule is declared `period: Month` and the average wage is a monthly input | agrees in effect |
| F5 (d) deeming or floor | answered only where they agree | deferred; the reason speaks of "deeming income equal to the Schedule XI item 3 minimum", with no floor condition | silent (prose leans to deeming) |
| F6 item 3: the classes, or the classes with the income condition | the classes | `insured_item` is an input | silent |
| F7 an employee or self-employed person also in (d)/(e) | item 1 or 2, with refusals | — | silent |
| F8 the temporary text's date and edges | 31.8.2026; "before" strict; straddling periods refused | deferral prose: "until expiry on 2026-08-31, continuing until completion for persons who began service before expiry" | agrees on the date; edges not executed |
| F9 a month split by the age or the pension | refused | deferred | silent |
| F10 s 245(b2) | repealed, no effect | live and blocking | disagrees (X3) |
| F11 whose minimum wage | the particular employee's, an input | `applicable_minimum_wage_first_month_of_quarter`, an input | agrees |
| F12 the branches of (c)(1) | six branches from s 335 | (c)(1) deferred | silent |
| F13 a branch with no column D amount | refused | — | silent |
| F14 (c)(2) inside coordinated contributions | yes | coordinated contributions is an input | silent |
| F15 kibbutz: the other employer deducted more | refused | deferred; prose: the kibbutz pays "the coordinated contributions less deductions" | silent |
| F16 (f)(2) "lower than" | strict | deferred | silent |
| F17 several employers and (b)'s floor | not modelled | — | silent |
| F18 s 350(c) reaches (b) only | yes | s 350 appears only as (a1)'s "not exempt" input | silent |
| F19 the day an age is reached | `add months` | deferred; the man's age 70 is a parameter | silent |
| F20 part of a year in a category | not modelled | one `insured_item` per call | agrees in effect |
| F21 item 6 of Schedule J | unemployment | names "the Schedule J item 6 deduction for police and prison officers" without the branch | silent, consistent |
| F22 "column E" | not resolved; red | not mentioned | silent |

Agree 4 (F4, F8's date, F11, F20); disagree 3 (F2, F3, F10); silent 15.

### The three places the source contradicts itself

| expected-red check | ours | Axiom |
| --- | --- | --- |
| s 342(e)(3) names column E for a deduction rate (line 3669; column D is the deduction, 4717) | red | not noticed: (e) deferred as "upper-band withholding" |
| s 342(e)(4) the same (line 3670) | red | not noticed |
| s 342(c)(2) is "subject to s 245(b2)" (3662), which is repealed (2474) | red; no effect on any answer | treated as an operative dependency; with Part D's absence, the reason (c)(1) and (c)(2) are deferred |

### Schedule J column D: 4.67 or 7.00

The independent tester found column D's rows above the threshold summing to 4.67 against a printed total of 7.00 (lines 4720-4730, and 4738-4748), with the Institute printing 7%.
Within the files I may read, Axiom uses neither figure: its s 342(c)(1) is deferred, and its gap entry says "the deduction's rates are encoded in `schedule-j/sign-1`" (`docs/ENCODING-GAPS.md` lines 660-661).
That file is out of this row and I did not open it, so I cannot say which figure Axiom's Schedule J carries; I stop short there.
On our side, IL-05 takes column D amounts as inputs; IL-04 as repaired on 2026-10-07 computes them from the rows, so the composed answer would use 4.67 (IL-04's repair asserts 80.1579 at a wage of 7,704: 7,703 × 1.04% + 1 × 4.67%).

### Where the text is silent

Ours refuses by name, case by case (18 named refusals across the three rule modules: 4 in Schedule K, 8 in s 348, 6 in s 342, counted by `grep -c 'REFUSE "'`).
Axiom defers whole outputs, each with a written reason, and inside the rules it executes it fills silence with a value: 0 for the monthly minimum of items 2-4 (X2); 0 and 0 for (d) without several employers (X16); 0 excluded and the wage uncapped when contributions are not under s 335 (X7); and any period at all, by `effective_from: '0001-01-01'` (X15).
Of these, only the first is a value the source does not support, and Axiom's own gap file says so.

### Periods

Ours answers contribution periods from January 2026, because s 342 as deposited is the text from 1 January 2026 (the 2025 Budget-year Law s 19(4) and s 21, verified again from the deposited PDF), and refuses earlier ones.
Axiom answers every period with the current text ("current_expression_only"); its coverage map's `validation_year` is 2025, its Schedule K tests are dated 2024 and its s 342 and s 348 tests January 2026.
For the limbs Axiom executes this makes no difference that I could find: s 342(a) and (d) do not contain the words the 2026 change replaced, and Schedule K's last tag is תשע״ב־2 (line 4755).
Whether every limb of s 348 as deposited, (a1) included, was in force in 2024 was not checked.

### Interface

| | ours | Axiom |
| --- | --- | --- |
| s 342 in | `An insured person, for section 342(a)-(b)` (column, wife flag); `An employee's month under section 342(c)` (year, month, branches, column D amounts, pension, person and age, date of birth, police, regulations flag); a list of each employer's deduction; `A renewed kibbutz member's month…`; `An employee who is also self-employed, in a month` | seven flat inputs: four booleans of status, the several-employers boolean, `coordinated_contributions`, `actual_total_monthly_deductions` |
| s 342 out | who is liable (three-way); the deduction; the employer's permitted reduction; the (d) outcome (four-way, with the amount); the kibbutz's contributions; the two parts of the self-employed income | a judgment (holds / not_holds); shortfall and refund amounts; the parameter 70 |
| s 348 in | `An insured person's period under section 348` (year, period, column, incomes by kind, minimum wage, the (d) and (e) statuses, s 350(c), an order under (c)), optionally the figures for a year | monthly wage, non-work income not exempt under s 350, the average wage, the s 335 boolean; the basic amount through Schedule K |
| s 348 out | the income on which contributions are computed, or a named refusal | the wage after the ceiling; the 25% sum; the amount excluded |
| Schedule K | item and period types; the figures for a tax year; the employee's four minimum wages; the 2026 figures published, with provenance | `insured_item` and every figure, per quarter, as inputs |

### Axiom's test cases through our encoding

Run in a scratch copy (`lad-il-05/run/`, the five rule modules byte-identical to the deposit, plus `axiom-cases.l4`), 2026-10-07, with the binary above: 30 assertions, each carrying **Axiom's** expected value, 28 satisfied and 2 failed, no other diagnostic; 8 `#EVAL`s printing ours.
The two failures were written as expected-to-fail before the run (scratch lines 115 and 161).
Where our interface differs, the adapter is named in the row.

| case | Axiom expects | ours | result |
| --- | --- | --- | --- |
| s342 `insured_dual_status_worker_owes_own_contributions_and_shortfall` | liable for own; shortfall 100; refund 0 | as a self-employed column, "the insured person, for himself"; deductions 200 and 200 against a month whose (c) deduction is 500 (one maternity column D amount of 500): "the employee pays the difference" 100 | match, 3 of 3 (adapted: one column per call, X5; coordinated contributions built, X17) |
| s342 `own_contribution_liability_requires_insurance` | not liable (not insured); 0; 0 | (a): could not be run, no input for an uninsured person (X6); (d) with one employer: "does not apply" | 2 match, 1 could not be run |
| s342 `nonworking_insured_person_owes_own_contributions` | liable for own; 0; 0 | "the insured person, for himself"; (d) with no employer: "does not apply" | match, 3 of 3 |
| s342 `chapter_three_only_wife_exemption` | not liable; 0; 0 | "no one: … is not liable"; (d): "does not apply" | match, 3 of 3 |
| s342 `employee_only_receives_excess_deduction_refund` | not liable for own; shortfall 0; refund 150 | "the employer, for the employee"; deductions 325 and 325 against 500: refund 150 | match, 3 of 3 |
| s348 `employee_income_below_ceiling_and_nonwork_income_below_threshold` (average wage 10,000, basic amount 10,382) | 15,000; 2,500; 2,000 | 15,000; 2,500; 2,000 (the whole of s 348: 15,000) | match, 3 of 3 |
| s348 `employee_income_above_ceiling_and_nonwork_income_at_threshold` | 51,910; 2,500; 2,500 | the same (the whole of s 348: 51,910) | match, 3 of 3 |
| s348 `nonwork_income_above_threshold_receives_no_partial_exclusion` | 51,910; 2,500; **0** | 51,910; 2,500; **2,500** (our all-or-nothing rule: 0; the whole of s 348: 51,910) | 2 match, 1 diverges (X1) |
| s348 `ceiling_and_exclusion_do_not_operate_outside_section_335` | 60,000; 2,500; 0 | the 25% sum 2,500; the other two could not be run, no input for contributions not under s 335 (X7) | 1 match, 2 could not be run |
| schedK `Employee monthly minimum uses the first month of the quarter` (2024) | 50,000; 6,000; 150,000; 18,000 | the same, through the Schedule K rules with figures for 2024; our s 348 entry refuses 2024 ("this row answers contribution periods from January 2026 only", scratch line 189) | match, 4 of 4 |
| schedK `Item three October minimum uses October average wage` (2024) | monthly minimum **0**; 165,000; 2,100 | item 3's monthly minimum **700** (F2); 165,000; 2,100 | 2 match, 1 diverges (X2) |
| schedK `Self-employed annual limits preserve quarterly changes` (2024) | 690,000; 36,750 | maximum: could not be run, four basic amounts in one tax year (X9; with one basic amount of 10,000 ours gives 600,000, which is not Axiom's input); minimum 36,750 | 1 match, 1 could not be run |
| schedK `Other insured annual minimum retains January wage for the first three quarters` (2024) | 690,000; 19,800 | maximum: could not be run (X9); minimum 19,800 | 1 match, 1 could not be run |

**13 cases, 38 expected outputs: 31 match, 2 diverge, 5 could not be run.**
Every Axiom case uses invented figures (an average wage of 10,000, basic amounts of 10,000 to 13,000), except the s 348 cases' basic amount, 10,382, which is the Institute's 2026 figure and gives its 51,910.

### Our independent-test findings, and how Axiom treats each

| finding (INDEPENDENT-FINDINGS.md) | Axiom |
| --- | --- |
| Root cause 1: column D's rows sum to 4.67 above the threshold, the total says 7.00 | (c)(1) deferred; its rates are in `schedule-j/sign-1`, out of row and not opened: cannot say |
| Root cause 2: s 342(c) does not apply the s 348(a) cap | the same gap: its s 348(a) output is an employee wage ceiling not wired to any s 342 output, and its (d) takes coordinated contributions as an input |
| Root cause 3: monthly figures for items 2-4 | 0 for the minimum (X2, disowned by its gap entry); s 348(b), (d), (e) deferred, which is the tester's refusal in effect |
| Root cause 4: s 348(d) for a quarter | deferred; its reason speaks only of a monthly item 3 minimum |
| Root cause 5: the 2027 deduction, and an order under Amendment 252 s 7(b) | (c)(1) deferred; Schedule J out of row: silent |

### What Axiom covers that we do not, and the reverse

**Axiom, not ours:** an uninsured person under s 342(a) (X6); the "contributions payable under s 335" limb of s 348(a) and (a1) as an input (X7); a dual-status person in one call (X5); a basic amount that differs between quarters (X9, which the deposited s 1 does not produce); answers for periods before 2026 (X15).

**Ours, not Axiom:** s 342(b); (c)(1) with its branch mapping; (c)(2) in every limb (pension, the man's and the woman's age, police and prison officers, the employer's reduction); coordinated contributions computed; (e) as a refusal; (e1); (f)(1)-(2); s 348(a) for every item and period on the whole income; (b) with s 350(c); (c)'s power test and refusal; (d) where its readings agree; (e) in both texts with the dated arm; the item derived from the case; the quarter and the average wage of a month derived from the text; a month for items 2-4; the 2026 figures with provenance; the expected-red checks of the source against itself.

### Proposed repairs to our encoding (not made)

- **P1 (X1; NOTES.md only).** Fork F3's reason says (a1) is "the same construction from below" as (a); the constructions differ (line 3763: "the amount" with יבוא; line 3764: "the income" with תובא and a qualifying clause).
  Restate F3: the text reads at least as naturally as all or nothing; the deduction is taken because the Institute's published example applies it; a second encoder (Axiom) took the other reading.
  Keep the answer; add the point to open question 2.
- **P2 (X7; NOTES.md only).** Say in section 1 or assumption A5 that every s 348 rule presupposes contributions payable under s 335, the limb with which (a) and (a1) open (lines 3763-3764), and that the limb is not an input.
- **P3 (X5; optional, interface).** A person who is both employee and self-employed (s 342(f), line 3673) cannot be put to `s 342(a)-(b)` in one call; consider a rule that takes both statuses and returns both liabilities (the independent tester's A7 points the same way).
- **P4 (X6; optional).** Say that s 342(a)'s "insured person" is presupposed by the record.

No expected value in any of our test modules should change on this comparison.

### Bottom line

Axiom executes a much smaller slice of these three provisions: s 342(a), and (d) given the coordinated contributions; s 348(a) for an employee's wage and (a1); and Schedule K's arithmetic with the item and every figure supplied by the caller.
It defers the rest, each with a written reason.
Where both compute, they agree, except on two points.
One is s 348(a1) (X1), where the words lean to Axiom's all-or-nothing reading and the regulator's published practice supports ours; the text does not decide it.
The other is the monthly minimum of items 2-4 (X2), where Axiom returns 0 and its own gap file says that is wrong.
Axiom's deferral treats the repealed s 245(b2) as live (X3), and it does not notice the "column E" slips in s 342(e)(3)-(4).
Nothing in the comparison shows an answer of ours wrong.
One reason in our fork register (F3) is overstated, and two presuppositions should be stated.
Of Axiom's 38 expected outputs, 31 match through our encoding, 2 diverge, and 5 cannot be put to our interface.

### Read outside the allowed list, said plainly

- While locating the `ENCODING-GAPS.md` entries, I printed by `awk` the heading lines of two entries not about these provisions: line 11 (`bootstrap-encoder-ref`, about the encoder build) and line 289 (`section-121b-a1-capital-charge-not-dated-from-2025`, an Income Tax Ordinance entry); heading text only, no body.
- I printed four lines of the `bootstrap-encoder-ref` entry (24, 36, 37, 39), because each mentions s 342 or s 348; they say the encoder was a local build that reached s 342 "twice" and deferred (c)(1) on an unresolved import. That entry is about tooling, not these provisions.
- `ls -R .axiom` printed the file names (not contents) of every encoding manifest, including other NII sections, Schedule J and Income Tax Ordinance sections; `ls` of the clone's top level printed its file names.
- From the coverage map I also printed its top-level key names, the NII instrument's key names, `id` and `official_name`, and one `not_encoded` value that names s 337(a)(2) beside s 342(a).
- In this repository: the headings (not bodies) of IL-04's `NOTES.md`, including the sub-headings of its "Comparison with Axiom's RuleSpec" section; its "Repair 2026-10-07" section, which I was allowed, refers by label to that comparison's items R1, R2, D11 and N3.
- Not opened: Axiom's README, AGENTS.md, any other `docs/` file, any `composed/`, Income Tax Ordinance, s 1, s 334, s 337, Schedule J or ss 65-68 file, and anything under `l4-ide/specs/research/AXIOM-*`. No grep printed lines of any other Axiom file.
