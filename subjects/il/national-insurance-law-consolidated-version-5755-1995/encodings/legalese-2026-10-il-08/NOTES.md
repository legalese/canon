# NOTES — il/national-insurance-law-consolidated-version-5755-1995, encoding row `legalese-2026-10-il-08`

The National Insurance Law half of row IL-08, the extension of the Israel tier: Schedule A1 Part D, s 72 and s 335, and the dispositions of ss 65 and 67A, taken in the order row IL-07's `GAPS.md` needs them.
One agent, one session, no sub-agents (run `IL-08-20261007`, encoder `enc-il-08`, 2026-10-07).
Status: **draft**, version 0.3.0 (2026-10-08: fork N4 as a switch, Meng's SHRUG ruling, BACKLOG IL-41; below), after 0.2.0 (2026-10-08: repairs of BACKLOG IL-20, below).
No domain expert has read it; HG1 has not been sought; no independent test pass has been run (0.2.0: one has since been run, `fid-il-08b`, `INDEPENDENT-FINDINGS.md`; its file now fails 4 and refuses 22, as declared in `check.sh`; 0.3.0: fails 1 and refuses 22).

The Income Tax Ordinance half, whose `NOTES.md` carries the parts common to both (the binary, the semi-cleanroom record, what was read), is `../../../income-tax-ordinance-new-version/encodings/legalese-2026-10-il-08/`.

## Version 0.3.0 (2026-10-08): SHRUG, fork N4 as a switch (BACKLOG IL-41)

Agent `shrug-il-41` (the session that did IL-20), one session, no sub-agents, on 2026-10-08, from BACKLOG IL-41.
Meng ruled SHRUG on 2026-10-08 for the four forks that gated code (BACKLOG IL-24): one named switch per fork, default DECLINE (a refusal by name saying the text does not decide), every other reading kept by name and tested.
Here that is fork N4, this row's part of inventory item DATE: the day a woman reaches the Part D age when the month she reaches it in lacks her day of birth.
Files changed: `nii-il08-nouns.l4`, `nii-schedule-a1-part-d.l4`, `nii-il08-tests-part-d.l4`, `check.sh`, `encoding.json` and this file.
Not changed: the s 72 and s 335 modules and their tests, the independent tester's three files (`tests-independent.l4` is still sha256 `bd929543…14efda2`), and the section "Comparison with Axiom's RuleSpec".

### What changed

- **The reading** (`nii-il08-nouns.l4`): `A reading of Part D of Schedule A1 where the day she reaches the age does not exist`, one of `Part D: the last day of the shorter month` (the clamp of 0.1.0 to 0.2.0, as row IL-05's F19), `Part D: the 1st of the next month`, `Part D: such a day is declined`.
  The constructors say "Part D" so that they cannot collide with rows IL-05's and IL-06's readings of the same fork in a module that imports two of them (the "multiple definitions" error of section 7).
- **The switch** (`nii-schedule-a1-part-d.l4`): `Schedule A1, Part D — the reading this row takes where the day she reaches the age does not exist`, which gives `Part D: such a day is declined`.
- **The refusal**: "Part D of Schedule A1 fixes an age in years and months, and does not say which day a woman reaches it where the month she reaches it in lacks her day of birth".
- **The rule at a reading**: `Schedule A1, Part D — the day she reaches the age it fixes for her, for a woman born on` D `, reading a day the month lacks as` R.
  Where the later month has her day of the month, all three readings give that day; otherwise the clamp gives the last day of the shorter month, the roll the 1st of the next month, and the default declines.
  The day is missing exactly when `add months`, which clamps, returns a different day of the month from hers.
- **The old rule by its old name**, `Schedule A1, Part D — the day she reaches the age it fixes for her, for a woman born on` D, keeps its name and type and now answers at the switch's reading, so it declines such a day.
  It carries no `@export`, and no other row calls it: row IL-05 computes its own day for s 342(c)(2) (its F19, BACKLOG IL-39), and the capstone reads only the age in months.
- **s 72 takes no reading.** Its rules compute no day: the days they read (the day entitlement arose or ceased, a death) are inputs, so a 29 February 18th birthday (the tester's 72-39) reaches s 72 already decided by whoever supplies it (row IL-06's s 65, fork F2, BACKLOG IL-40, or the capstone).

### Tests

The three tests of the day that existed (`nii-il08-tests-part-d.l4` lines 70, 72, 74) land on days that exist (15 November 2013, 31 May 2018, 30 June 2020), so none rested on the clamp; they stay at the default reading, values unchanged.
No other test of this row computes such a day, so no test was re-pointed.
14 assertions were added (lines 85-105), each worked from the printed rows before the run:

| line | born | months (row) | reaches the age in | default | clamp | roll | declined by name |
| ---: | --- | --- | --- | --- | --- | --- | --- |
| 85-88 | 31 October 1945 | 812 (line 4446, 67 and 8 months) | June 2013, 30 days | REFUSED | 30 June 2013 | 1 July 2013 | REFUSED |
| 91-93 | 29 February 1944 | 804 (line 4444, 67) | February 2011, a common year | REFUSED | 28 February 2011 | 1 March 2011 | — |
| 96-98 | 31 July 1945 | 808 (line 4445, 67 and 4 months) | November 2012, 30 days | REFUSED | 30 November 2012 | 1 December 2012 | — |
| 101-103 | 15 March 1946 | 812 | November 2013, the day exists | — | 15 November 2013 | 15 November 2013 | 15 November 2013 |
| 105 | 30 October 1945 | 812 | June 2013, which has a 30th | 30 June 2013 | — | — | — |

The module had 37 assertions and has 51; no expected value changed.
The tester's D-46, D-47 and D-48 (`tests-independent.l4` lines 733, 735, 737, `#ASSERT REFUSED`) now pass: they were the three DATE failures declared from 0.2.0.
Its D-40 to D-45 (lines 721-731) land on days that exist and are satisfied as before.
That the switch is what passes them: a scratch copy with the switch set to the clamp, and one roll value altered, printed 4 failed in `nii-il08-tests-part-d.l4` (the three default refusals and the altered value) and 4 failed in the tester's file, exit 1.

### The tester's file

| | satisfied | failed | refused |
| --- | ---: | ---: | ---: |
| 0.2.0 | 117 | 4 | 22 |
| 0.3.0 | 120 | 1 | 22 |

Failed: line 247 (08n-N2) only.
Refused: the 22 SCOPE lines of 0.2.0, unchanged.

### `check.sh`, 0.3.0

`expected_failed` for `tests-independent.l4` goes from 4 to 1; `expected_refused` stays 22.
Run from 2026-10-08T15:58:05Z to 15:58:15Z as `L4=/Users/mengwong/.local/bin/l4 ./check.sh`, `JL4_LIBRARY_PATH` unset, after the last edit to any module or to `check.sh`; binary `~/.local/bin/l4` resolving to the cabal store's `jl4-0.1-d4290e25/bin/l4`, sha256 `f4f2bd2558f02f828f0deced5f74313a33670f08cc3275ff95b83f2cde71e448` before and after the run.
The 0.2.0 baseline was re-run on the same binary first (15:51:30Z), with 0.2.0's counts and exit 0.

```
module                                    errors satisfied  failed  refused  expected
nii-il08-nouns.l4                              0         0       0        0         0
nii-il08-tests-part-d.l4                       0        51       0        0         0
nii-il08-tests-s72-s335.l4                     0        54       0        0         0
nii-s335-branches.l4                           0         0       0        0         0
nii-s72-period-of-allowance.l4                 0         0       0        0         0
nii-schedule-a1-part-d.l4                      0         0       0        0         0
tests-independent.l4                           1       120       1       22      1/22
TOTAL (7 modules)                              1       225       1       22
(a failed assertion is also an error; any other error, or a refused assertion a module is not expected to have, makes the run red; "expected" is failed/refused where a module may refuse)
```

`check.sh` exit 0.
`python3 -I tools/srcquote.py SOURCE` leaves the three changed modules byte-identical, and `python3 -I tools/hebcheck.py SOURCE` passes them (exit 0).

### For the capstone (BACKLOG IL-44)

- Re-vendor `nii-il08-nouns.l4` and `nii-schedule-a1-part-d.l4`; nothing else of this row changed.
- No answer the capstone reaches changes: it reads only the Part D age in months, which no reading touches.
  Its modules, with these two vendored in a scratch copy, gave the same counts as with the copies it holds (`il07-tests.l4` 130, `il07-tests-il08.l4` 116, `tests-independent.l4` 260 satisfied and 18 failed, `tests-independent-2.l4` 298 satisfied, 7 failed and 20 refused).
- Names added: the type `A reading of Part D of Schedule A1 where the day she reaches the age does not exist` and its three constructors; the switch `Schedule A1, Part D — the reading this row takes where the day she reaches the age does not exist`; the refusal `Part D of Schedule A1 fixes an age in years and months, and does not say which day a woman reaches it where the month she reaches it in lacks her day of birth`; the rule `Schedule A1, Part D — the day she reaches the age it fixes for her, for a woman born on` D `, reading a day the month lacks as` R.
  Nothing renamed or removed.
- The capstone's own DATE cases (an 18th birthday on 29 February, a woman's day under s 342(c)(2)) come from rows IL-06 and IL-05, not from this row.

## Version 0.2.0 (2026-10-08): repairs (BACKLOG IL-20)

Repair agent `rep-il-20`, one session, no sub-agents, on 2026-10-08, working job G of `l4-pipeline/findings/il-2026-10-08/jobs.txt` from the inventory `inventory.tsv` taken that morning.
Each finding was read where it was recorded (`INDEPENDENT-FINDINGS.md`, this file) before it was fixed.
Files changed: `nii-s72-period-of-allowance.l4`, `nii-il08-nouns.l4` (comments only), `nii-il08-tests-s72-s335.l4`, `check.sh`, `encoding.json` and this file.
Not changed: `nii-schedule-a1-part-d.l4`, `nii-s335-branches.l4`, `nii-il08-tests-part-d.l4`, the independent tester's three files (`tests-independent.l4` is still sha256 `bd929543…14efda2`), and the section "Comparison with Axiom's RuleSpec".

### The items

- **08n-PAID** (OURS-WRONG, silent; `INDEPENDENT-FINDINGS.md` line 122, `tests-independent.l4` line 248).
  "A child allowance was paid for the child" was never read against s 72(a): a child who died before its first paid month still got (c)'s three months when the input said TRUE.
  The input stays: it is the Institute's record of a payment (assumption A4), (c) reads "שבעדו שולמה", and fork N2 turns on whether anything had yet been paid, which (a)'s window cannot tell (a child may die inside a payable month before any payment is made).
  Deriving it from the window would have erased that distinction and removed a field the capstone sets.
  It is now read against (a) and (b): where it says paid, and (b) excludes the child or (a)'s first month comes after the month of the death, the months after the death rest on a payment s 72 did not allow, and (c) does not say whether its three months follow one.
  The rules decline exactly the months that turn on it, by name: "an allowance is recorded as paid for the child, but s 72(a) and (b) make no month payable before the child died; s 72(c) does not say whether its three months follow such a payment".
  A month up to the death is unpaid on the text ((b) fails, or (a) has not begun), a month after the third month is unpaid on either reading of (c), and both are answered; the last-month rule declines.
  The tester's line 248 (expected REFUSE) now passes; line 247 (the same child recorded as not paid) still fails, on fork N2.
- **08n-GATE** (OURS-WRONG, minor; `INDEPENDENT-FINDINGS.md` line 124).
  The May-2015 period was applied only on the export; the first-month and last-month rules gave months before it to any caller (October 1995 for 72-14).
  Now one rule, `s 72(a), (c) — the first and last months for which the allowance is paid, placed against the period this row answers, for`, holds the only encoding of (a) and (c): it computes both months and places each against the period, as `a month before May 2015` or `a month from May 2015, numbered` N.
  The first-month and last-month rules (names and types unchanged) decline a month before May 2015 with the export's refusal; the export answers a month from May 2015 for a child whose payment began or ended before it, without reaching a refusal.
  No rule of the row now gives a month before May 2015; the two month-count helpers (`s 72 — the month count of …`) are calendar arithmetic and take no period.
  Consequence: 20 of the tester's assertions that went through the first-month rule (lines 122 and 167-205) are now refused, as lines 120 and 171 already were.
  The lead classed them on 2026-10-08 as SCOPE (08n-A2), not tester error: the tester's values stand as its reading of s 72 for 1995-2015, and they are the assertions to re-check if the scope is ever widened to the Law's commencement.
- **08n-A2** (AMBIGUITY, scope; the lead's choice, **assumed, not ruled**).
  Months before May 2015 are still declined.
  The refusal is renamed and reworded so that it says May 2015 is this row's scope, chosen to compose with row IL-06, and not the Law's commencement, which s 402 (lines 4314-4315, quoted in the module) fixes on 1 October 1995.
  Before: "this row answers months of the child allowance from May 2015, the period row IL-06 answers".
  After: "this row answers months of the child allowance from May 2015, a scope chosen to compose with row IL-06, not the commencement of the Law (s 402: 1 October 1995)".
  If the gate's date is ruled to be 1 October 1995, `the first month this row answers, as a month count` is the one value to change.
- **08n-72B** (AMBIGUITY, unrecorded).
  Recorded as forks N5 (how "שבעה ימים" are counted) and N6 (a child born at home and never in a hospital), with the tester's 72-42 and 72-44, in the fork register and at the input in `nii-il08-nouns.l4` and the export.
  Dates were not taken: (b) stays one input, which the caller answers; taking the day of birth and of leaving the hospital would still need a reading of N5 and N6, and the capstone answers TRUE for the living children it lists.
- **08n-B2** (WORDING).
  Section 6 now says that s 342(c)(2) makes the women's age "subject to s 245(b2)" (line 3662) and that s 245(b2) reads "(בוטל)" (line 2474): there is nothing to supply.
- **CHK-08n** (WORDING, housekeeping).
  `check.sh` gains `expected_refused`, as row IL-04's, and declares the tester's file: 4 failed and 22 refused, each line named with its inventory id and class in a comment.
  It exits 0.
- **DATE** (AMBIGUITY; BACKLOG IL-24, waits on Meng).
  Recorded under fork N4 with its three readings and who holds it; the behaviour is kept (the clamp).
  The tester's D-46, D-47 and D-48 (lines 733, 735, 737) still fail, as declared.
  s 72's side (72-39: when a child born on 29 February turns 18) is an input, the day entitlement ceased, which row IL-06 or the capstone supplies.

### Expected values changed or added

All worked from lines 854-856 (and 4315 for the message) before the run; none was changed to match what the encoding printed.
`nii-il08-tests-s72-s335.l4`, by line:

| line | assertion | old | new | why |
| ---: | --- | --- | --- | --- |
| 62 (was 61) | export, April 2015, arose 1 January 2010 | REFUSED, "… the period row IL-06 answers" | REFUSED, "… a scope chosen to compose with row IL-06, not the commencement of the Law (s 402: 1 October 1995)" | 08n-A2 wording |
| 68 | first month, arose 10 June 2026 | — | June 2026 (10th, by the 15th) | 08n-GATE: a month of the period is answered |
| 70 | last month, not ended | — | NOTHING | 08n-GATE |
| 73 | first month, arose 20 March 2008 | — | REFUSED (April 2008, before May 2015) | 08n-GATE |
| 75 | export, June 2026, the same child | — | paid (began April 2008, not ended) | 08n-GATE: the export still answers |
| 78, 79 | arose 20 April 2015 (after the 15th) | — | first month May 2015; May 2015 paid | 08n-GATE, the edge |
| 82, 83 | arose 15 April 2015 (by the 15th) | — | first month REFUSED (April 2015); May 2015 paid | 08n-GATE, the edge |
| 87, 88 | ceased 30 April 2015 | — | last month REFUSED (April 2015); May 2015 not paid | 08n-GATE |
| 91-93 | ceased 1 May 2015 | — | last month May 2015; May paid; June not | 08n-GATE |
| 97-99 | died 10 February 2015, paid since 2010 | — | last month May 2015 (February + 3, (c)); May paid; June not | 08n-GATE with (c) |
| 103, 104 | died 10 January 2015, the same | — | last month REFUSED (April 2015); May 2015 not paid | 08n-GATE with (c) |
| 115-120 | 72-57 recorded as paid (born 20 February 2026, died 25 February) | — | February not paid; March and May REFUSED; June not paid; first month March 2026; last month REFUSED | 08n-PAID: (a) pays from March, ends with February, so no month was payable |
| 122, 123 | 72-57 recorded as not paid | — | March not paid; last month February 2026 | fork N2, unchanged reading |
| 128-130 | lived three days, never left the hospital, recorded as paid | — | February and March not paid; last month REFUSED | 08n-PAID with (b) |
| 134-136 | 72-56 recorded as paid (born 10 February 2026, died 20 February) | — | May paid; June not; last month May 2026 | 08n-PAID, a consistent record: (c) applies |

The module had 22 assertions and has 54: one reworded, 32 added.
Answers that changed in the rules: the export for a child recorded as paid whose window was empty (72-57 with TRUE: March to May 2026 were paid, now declined); the first-month and last-month rules for a month before May 2015 (answered, now declined); the export's refusal message.
No answer the capstone reaches changed: its modules, with these two vendored in a scratch copy, gave the counts `red-checks.txt` records (`il07-tests.l4` 114, `il07-tests-il08.l4` 98, `tests-independent.l4` 258 satisfied, 18 failed, 2 refused).

### The tester's file

| | satisfied | failed | refused |
| --- | ---: | ---: | ---: |
| 0.1.0 (2026-10-08 inventory) | 136 | 5 | 2 |
| 0.2.0 | 117 | 4 | 22 |

Failed: line 247 (08n-N2), lines 733, 735, 737 (DATE).
Refused: lines 120 and 171 (the export, October 1995 and May 2008) and lines 122, 167, 169, 173, 175, 177, 179, 181, 183, 185, 187, 189, 191, 193, 195, 197, 199, 201, 203 and 205 (the first-month rule and the months-paid count built on it, for October 1995 and for children born 2007-2010): all 08n-A2, the last twenty surfaced by 08n-GATE.
All 22 are class SCOPE, not tester error (the lead, 2026-10-08): this row answers months from May 2015 by its own choice, and the tester decided that s 72's untagged text answers them.
The tester's values stand as its reading of s 72 for 1995-2015; if the scope is ever widened to the Law's commencement (s 402, 1 October 1995), these 22 are the assertions to re-check (the twenty that reached the first-month rule were satisfied by 0.1.0's ungated rules).
Each of the 22 meets the reworded refusal, "this row answers months of the child allowance from May 2015, a scope chosen to compose with row IL-06, not the commencement of the Law (s 402: 1 October 1995)" (checked in the run's diagnostics: one message, 22 lines).
Line 248 moved from failed to satisfied (08n-PAID).

### `check.sh`, 0.2.0

Run from 2026-10-08T07:08:30Z to 07:08:43Z, after the last edit to any module or to check.sh, as `L4=/Users/mengwong/.local/bin/l4 ./check.sh`, `JL4_LIBRARY_PATH` unset, binary `~/.local/bin/l4` resolving to the cabal store's `jl4-0.1-d4290e25/bin/l4` (sha256 `f4f2bd2558f02f828f0deced5f74313a33670f08cc3275ff95b83f2cde71e448`, unchanged during the run, and the binary of the 2026-10-08 inventory).

```
module                                    errors satisfied  failed  refused  expected
nii-il08-nouns.l4                              0         0       0        0         0
nii-il08-tests-part-d.l4                       0        37       0        0         0
nii-il08-tests-s72-s335.l4                     0        54       0        0         0
nii-s335-branches.l4                           0         0       0        0         0
nii-s72-period-of-allowance.l4                 0         0       0        0         0
nii-schedule-a1-part-d.l4                      0         0       0        0         0
tests-independent.l4                           4       117       4       22      4/22
TOTAL (7 modules)                              4       208       4       22
(a failed assertion is also an error; any other error, or a refused assertion a module is not expected to have, makes the run red; "expected" is failed/refused where a module may refuse)
```

`check.sh` exit 0.
Before the repairs, on the same binary (06:51:30Z), the run was red: the tester's file at 5 failed and 2 refused against 0 and 0.
That the harness can fail: a scratch copy with three of the new assertions altered (one expected value, one negation, one `#ASSERT REFUSED` pointed at an answering expression) printed 2 failed and 1 refused in `nii-il08-tests-s72-s335.l4`, exit 1.
`python3 -I tools/srcquote.py SOURCE` leaves the three changed modules byte-identical, and `python3 -I tools/hebcheck.py SOURCE` passes them (exit 0).

### Names added and renamed (for the capstone, BACKLOG IL-22)

- Renamed: the refusal `this row answers months of the child allowance from May 2015, the period row IL-06 answers` is now `this row answers months of the child allowance from May 2015, a scope chosen to compose with row IL-06, not the commencement of the Law (s 402: 1 October 1995)`.
- Added, in `nii-s72-period-of-allowance.l4`: `the first month this row answers, as a month count`; the type `A month for section 72, placed against the period this row answers` (`a month before May 2015`, `a month from May 2015, numbered` with `the month count`); the record `The first and last months for which section 72 pays the allowance, placed against the period this row answers` (`the first month paid`, `the last month paid`, `the months after the death rest on a payment that s 72(a) and (b) did not allow`); the rule `s 72(a), (c) — the first and last months for which the allowance is paid, placed against the period this row answers, for`; the refusal `an allowance is recorded as paid for the child, but s 72(a) and (b) make no month payable before the child died; s 72(c) does not say whether its three months follow such a payment`.
- Unchanged: the export's name, inputs and type; the first-month and last-month rules' names and types; every noun (the nouns module changed only in comments).
- The capstone calls only the export and sets "was paid" to FALSE, so it needs a re-vendor and no adapter change.

## 0. What `check.sh` prints (0.1.0)

This section is the 0.1.0 run, before the independent tests were deposited; the 0.2.0 run is in "Version 0.2.0" above.

Run from 2026-10-07T00:22:32Z to 00:22:41Z as `L4=/Users/mengwong/.local/bin/l4 ./check.sh`, `JL4_LIBRARY_PATH` unset, with the binary the other half records (`jl4-0.1-ff13a0ea`, sha256 `f6501568…dbfa8bc`).
No module changed during the run.

```
module                                    errors satisfied  failed  refused  expected
nii-il08-nouns.l4                              0         0       0        0         0
nii-il08-tests-part-d.l4                       0        37       0        0         0
nii-il08-tests-s72-s335.l4                     0        22       0        0         0
nii-s335-branches.l4                           0         0       0        0         0
nii-s72-period-of-allowance.l4                 0         0       0        0         0
nii-schedule-a1-part-d.l4                      0         0       0        0         0
TOTAL (6 modules)                              0        59       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

`check.sh` exit 0.
59 assertions, all satisfied; 2 of them are `#ASSERT REFUSED … BECAUSE "…"`.
No assertion is expected to fail; there is no expected-red module.
The two Warnings about differing copies of `prelude` and `daydate` under `~/.local/share/jl4/libraries/` are printed as for every row.

That the harness can fail: a scratch copy of these six modules with one expected value altered (a woman born in January 1930 asserted at 781 months), one `#ASSERT REFUSED` pointed at an expression that answers, and one plain `#ASSERT` on an expression that refuses (s 335 for 2025) printed `2 failed, 1 refused`, exit 1.

Every assertion was satisfied on the first run that evaluated it; before that, the tests modules failed to compile once (a one-argument mixfix name ending in a keyword), which a rename fixed, no expected value changing.
`python3 -I tools/srcquote.py SOURCE *.l4` regenerates every `-- src:N |` line; `python3 -I tools/hebcheck.py SOURCE *.l4 *.md` finds every other run of Hebrew verbatim in the source (exit 0).

## 1. What is encoded, and what is not

| module | lines | holds |
| --- | ---: | --- |
| `nii-il08-nouns.l4` | 93 (0.2.0: 99, comments; 0.3.0: 116, the Part D reading) | the nine branches (as rows IL-04 and IL-05 spell them), the person for s 335, the entitlement for s 72; `DECLARE` only |
| `nii-schedule-a1-part-d.l4` | 96 (0.3.0: 136) | Part D: a woman's age by month of birth, in months, and the day she reaches it (0.3.0: at a reading of fork N4, declined by default where the month lacks her day) |
| `nii-s72-period-of-allowance.l4` | 90 (0.2.0: 218) | s 72(a)-(c): whether the child allowance is paid for a month (0.2.0: the first and last months placed against the period, and "was paid" read against (a) and (b)) |
| `nii-s335-branches.l4` | 131 | s 335(a)-(j): the branches in which a person pays |
| `nii-il08-tests-part-d.l4` | 74 (0.3.0: 105) | 37 assertions: every band of Part D at both its edges (0.3.0: 51, with the three readings of fork N4) |
| `nii-il08-tests-s72-s335.l4` | 85 (0.2.0: 160) | 22 assertions (0.2.0: 54) |

Not encoded: s 65 (encoded in full by row IL-06), s 67A (no such section), the other Parts of Schedule A1, and the statuses s 335 reads (each another Chapter's answer).

## 2. Coverage table

Line numbers are lines of `../../registers/source-bundle/national-insurance-law-consolidated-version-5755-1995.he.wiki.txt`.
"GAPS" is the item of row IL-07's `GAPS.md` the provision discharges.
**Totals: 17 encoded, 1 inert, 8 out-of-scope, 0 deferred** (26 rows, counted by script; "out-of-scope" includes the statuses taken as inputs).

| provision | lines | gist | disposition | where | GAPS |
| --- | --- | --- | --- | --- | --- |
| Schedule A1, Part D, heading and note | 4431-4433 | "the age of entitlement to a senior citizen pension for women by month of birth"; used by ss 245(a), 342(c), 351(b), 406(a)(4)(a) | encoded | `nii-schedule-a1-part-d.l4` | 10 |
| Schedule A1, Part D, the table | 4437-4453 | sixteen bands, 65 to 70 years | encoded | `Schedule A1, Part D — the age in months fixed for a woman born in month` | 10 |
| Schedule A1, Parts A, B, C, E | 4367-4430, 4456-4477 | retirement age, unemployment age, Chapter 11 age, women exempt from a qualifying period | out-of-scope | Not in the ruled scope (only Part D is), and no rule of this row reads them. Observation, not checked further: Part A's table for women (lines 4385-4397) ends at "מאי 1947 עד דצמבר 1955" (line 4396), with no row for a woman born later, where the other tables end with an open row ("ואילך"). | — |
| s 65(a) "מבוטח" (1), (2) | 801-803 | insured for Chapter 4 | out-of-scope | Encoded in full by row IL-06 (its coverage rows for s 65(a) and (b)); not re-encoded, so that one provision has one encoding. s 335(b) reads "insured as defined in s 65(a)(1)" from the two status fields IL-06 uses (`insured under Chapter 11`, `a housewife as defined in section 238`). "יושב בישראל", the residence (2) turns on, is not defined in the Law: a search on 2026-10-07 for a definition of "תושב ישראל" or "יושב בישראל" in it found none, so residence remains a status. | 13 |
| s 65(a) "ילד", s 65(b) | 804-809 | the child, abroad for three months | out-of-scope | Encoded in full by row IL-06. | — |
| s 67A | — | — | inert | There is no s 67A in the deposited consolidation. "67א" occurs only in the table of old and new section numbers (line 5326), mapping the 1968 consolidation's s 67A to the present s 108, which is repealed ("(בוטל)", lines 1162-1163). Row IL-07's GAPS.md records the same. | — |
| s 72(a), first limb | 854 | entitlement arising by the 15th: paid from the 1st of that month; after: from the next | encoded | `s 72(a) — the first month …`; fork N1 | 6 |
| s 72(a), last limb | 854 | payment ends on the last day of the month entitlement ceased | encoded | `s 72(a), (c) — the last month …` | 6 |
| s 72(b) | 855 | only for a child who lived seven days or left the hospital | encoded | `s 72 — the allowance is paid for month`; (0.2.0) forks N5, N6, the caller's | 6 |
| s 72(c) | 856 | three months on after the month a child for whom it was paid died | encoded | `s 72(a), (c) — the last month …`; fork N2; (0.2.0) `s 72(a), (c) — the first and last months … placed against the period …`, which reads "was paid" against (a) and (b) (item 08n-PAID) | 6 |
| s 72, the period answered | 853 | no amendment tag | encoded (a gate from May 2015, row IL-06's period; 0.2.0: applied to every rule that gives a month, item 08n-GATE) | `this row answers months of the child allowance from May 2015 …` (0.2.0: reworded, "… a scope chosen to compose with row IL-06, not the commencement of the Law (s 402: 1 October 1995)") | 6 |
| s 335 heading | 3610 | last tag תשע״ח־5 | encoded (a gate from January 2026, rows IL-04 and IL-05's period) | `this row answers section 335 for contribution periods from January 2026` | 9 |
| s 335(a) | 3611 | a worker who is not a resident: maternity | encoded | `s 335(a) — …` | 9 |
| s 335(b) | 3612 | insured as in s 65(a)(1): children | encoded | `s 335(b) — …` | 9 |
| s 335(c), (d) | 3613-3614 | Chapters 5 and 6: work injury, accident injury | encoded | `s 335(c) — …`, `s 335(d) — …` | 9 |
| s 335(e) | 3615 | s 158(1), not a controlling shareholder: unemployment | encoded | `s 335(e) — …` | 9 |
| s 335(f) | 3616 | an employee under Chapter 8, not a controlling shareholder: insolvency | encoded | `s 335(f) — …` | 9 |
| s 335(g), (h) | 3617-3618 | Chapter 9; long-term care | encoded | `s 335(g) — …`, `s 335(h) — …` | 9 |
| s 335(i) | 3619 | Chapter 11, not a housewife or widow pensioner: senior citizens and survivors, and maternity | encoded | `s 335(i) — …`; fork N3 | 9 |
| s 335(j) | 3620 | none detracts from another | encoded | `s 335 — contributions are payable in the branch` (any subsection imposing it) | 9 |
| s 335, the list | 3610-3620 | the branches, in Schedule J's order | encoded | `s 335 — the branches for which contributions are payable, for` | 9 |
| s 238 "עקרת בית", "אלמנה בת קצבה" | 2401 ff. | housewife, widow pensioner (Chapter 11) | out-of-scope (inputs) | Statuses the Institute records under Chapter 11; outside the ruled scope. | 9 |
| s 158 "מבוטח" (1) | — | unemployment insurance | out-of-scope (input) | Chapter 7's definition; outside the ruled scope. | 9 |
| Chapters 5, 6, 8, 9, 11; long-term care | — | who is insured in each branch | out-of-scope (inputs) | Each is its Chapter's own regime; s 335 only maps the statuses to branches. | 9 |
| s 1 "בעל שליטה", "חברת מעטים" | 122, 139 | controlling shareholder, closely-held company | out-of-scope (input) | Row IL-04 lists them as out-of-scope statuses; one input here. | 9 |
| ss 66-68 | 813-834 | the child allowance itself | out-of-scope | Row IL-06. s 72 says which months are paid; how much, and in whose count, is IL-06's. | 6 |

## 3. Assumptions

**A1 — Part D is stated as the deposited text prints it.** No rule takes a date: the table maps a month of birth to an age, its last row is open ("ואילך"), and its tags (תשע״ז־12 on the heading, תש״ף on the Part) predate every period the consuming rows answer.

**A2 — s 72 answers months from May 2015.** s 72 carries no amendment tag, so its text is not dated by any amendment; the row answers the period row IL-06 answers (its A1), with which it composes, and declines an earlier month by name.
(0.2.0) Assumed, not ruled: the lead's choice (BACKLOG IL-20, inventory 08n-A2), kept against the reading that s 72's own text answers from the Law's commencement, 1 October 1995 (s 402, lines 4314-4315), which the independent tester took (72-14, 72-30).
The refusal now says so, and every rule that gives a month applies it (08n-GATE).
The 22 assertions of the tester's that it refuses ("The tester's file" in "Version 0.2.0") are the ones to re-check if the scope is widened.

**A3 — s 335 answers contribution periods from January 2026.** Its last tag, תשע״ח־5, is by counting the file's list of amending Laws (line 7) the Insolvency and Economic Rehabilitation Law 5778-2018; what that Law changed in s 335, and when it commenced, were not checked. The row answers the period rows IL-04 and IL-05 answer (their A1) and declines an earlier year.

**A4 — the statuses are inputs.** Every fact s 335 reads is another Chapter's answer; every fact s 72 reads (the day entitlement arose or ceased, a death, the seventh day) is the Institute's record.
(0.2.0) The record that an allowance was paid for the child is now read against (a) and (b), and the months that turn on a payment they did not allow are declined (08n-PAID).

## 4. Fork register

| # | where | the question | readings | taken, and why |
| --- | --- | --- | --- | --- |
| N1 | s 72(a) | "עד 15 בחודש": by the 15th inclusive, or before it? | inclusive; exclusive | **inclusive**: the next limb says "אחרי 15", after the 15th, so the 15th itself falls in the first. Tests on the 15th and the 16th. |
| N2 | s 72(a), (c) | A child for whom no allowance had been paid dies: does (c)'s three months apply? | no; yes | **no**: (c) is about "ילד שבעדו שולמה קצבת ילדים"; (a) then ends payment with the month of death. (0.2.0) Inventory 08n-N2, a recorded fork in BACKLOG IL-24's queue, held by Meng; the independent tester expected REFUSE (72-57, line 247, still failing) and now leans to "no" ("ימשיכו" presupposes a payment under way). Its companion, a payment recorded where (a) and (b) made no month payable, is no longer answered either way: the months that turn on it are declined (item 08n-PAID). |
| N3 | s 335(a), (i) | Maternity is imposed by (a) and by (i): one branch or two? | one | **one** (row IL-04's F15): (j) says the subsections do not detract from each other, and Schedule J's two maternity items never both print a figure in one column. |
| N4 | Schedule A1 Part D | The day a woman "reaches" the age, for a 29-31 day of birth and a shorter month | the last day of the shorter month; the first of the next; (0.3.0) declined | (0.1.0-0.2.0) **the last day** (`add months` clamps), row IL-05's fork F19, so the two rows agree. (0.2.0) This is this row's part of inventory item **DATE**, one fork across rows IL-05 (F19), IL-06 (F2) and IL-08: a day the later month lacks (31 June, 29 February in a common year, 31 November). Readings: (i) clamp to the last day of the shorter month (taken in all three rows); (ii) roll to the 1st of the next month; (iii) refuse, as the independent tester expected (D-46, D-47, D-48, lines 733, 735, 737, still failing). Held by Meng (BACKLOG IL-24, one ruling for the three rows; the lead recommends a named switch with decline as the default); the clamp is kept until then. s 72's side of DATE (72-39, a child born on 29 February turning 18) is an input here, the day entitlement ceased, which row IL-06's s 65 or the capstone supplies, so s 72 inherits IL-06's reading. **(0.3.0) RULED by Meng on 2026-10-08 (SHRUG, BACKLOG IL-41): a named switch, default DECLINE.** `Schedule A1, Part D — the reading this row takes where the day she reaches the age does not exist` gives `Part D: such a day is declined`; `Part D: the last day of the shorter month` (the clamp above) and `Part D: the 1st of the next month` are kept by name and tested (`nii-il08-tests-part-d.l4` lines 85-105). The tester's D-46 to D-48 now pass. |
| N5 | s 72(b) | "שחי שבעה ימים לפחות": counted how? (the tester's 72-42: six days elapsed, or seven calendar days counting both ends) | seven full days after the day of birth; seven calendar days counting the day of birth | (0.2.0, item 08n-72B) **none in the rules**: (b) is one input, `the child lived at least seven days or left the hospital`, which the caller answers; the tester expected REFUSE. Recorded so the choice is visible; open question 5. |
| N6 | s 72(b) | "או שיצא מבית החולים": does a child born at home, never in a hospital, satisfy (b) before seven days? (the tester's 72-44) | no, on the literal words; yes, the limb being about a child who was in hospital | (0.2.0, item 08n-72B) **none in the rules**: the same input; the tester expected "no" on the literal words. Open question 6. |

Places read for a fork and none found: Part D's bands (contiguous and disjoint; each tested at both edges); s 335(b)'s cross-reference to s 65(a)(1), which IL-06 encodes as the same two statuses.

## 5. Answer tables

### Schedule A1 Part D

| born | age | in months |
| --- | --- | ---: |
| to June 1939 | 65 | 780 |
| July and August 1939 | 65 and 4 months | 784 |
| September 1939 to April 1940 | 65 and 8 months | 788 |
| May to December 1940 | 66 | 792 |
| January to August 1941 | 66 and 4 months | 796 |
| September 1941 to April 1942 | 66 and 8 months | 800 |
| May 1942 to December 1944 | 67 | 804 |
| January to August 1945 | 67 and 4 months | 808 |
| September 1945 to April 1946 | 67 and 8 months | 812 |
| May to December 1946 | 68 | 816 |
| January to August 1947 | 68 and 4 months | 820 |
| September 1947 to April 1948 | 68 and 8 months | 824 |
| May to December 1948 | 69 | 828 |
| January to August 1949 | 69 and 4 months | 832 |
| September 1949 to April 1950 | 69 and 8 months | 836 |
| May 1950 and after | 70 | 840 |

### s 72

| event | first month paid | last month paid |
| --- | --- | --- |
| born on the 1st-15th of a month | that month | — |
| born on the 16th or later | the next month | — |
| turns 18 (entitlement ceases on the birthday) | — | the month of the 18th birthday |
| entitlement ceases otherwise | — | that month |
| dies, an allowance having been paid | — | the third month after the month of death |
| lived fewer than seven days and never left the hospital | never paid | — |
| (0.2.0) dies, an allowance recorded as paid, but (b) excludes the child or (a)'s first month is after the month of death | as above | declined: the three months after the month of death are refused, later months unpaid (item 08n-PAID) |
| (0.2.0) either month before May 2015 | declined by the first-month rule (the export answers any month from May 2015: paid from it) | declined by the last-month rule (the export answers any month from May 2015: unpaid) |

### s 335

| person | branches |
| --- | --- |
| a resident employee insured in every Chapter | all nine |
| a controlling shareholder in a closely-held company, otherwise the same | all but unemployment and insolvency |
| a non-resident employee insured for work injury only | maternity, work injury |
| a housewife (Chapter 11), insured in Chapters 6, 9 and long-term care | accident injury, disability, long-term care |
| a widow pensioner (Chapter 11), the same | children, accident injury, disability, long-term care |

## 6. What these rows imply for the capstone's adapters

- **GAPS 10, Part D.** The input "the earner's age fixed by Part D … in months, if a woman" becomes `Schedule A1, Part D — the age in months fixed for a woman born on` her date of birth, the unit row IL-05's `The insured person, for the age limb of section 342(c)(2)` takes. H19 can be answered: a woman born in 1980 has 840.
  (0.2.0, item 08n-B2) A note for whoever composes Part D with s 342(c)(2): that paragraph fixes the woman's age "בכפוף להוראות סעיף 245(ב2)" (line 3662), and s 245(b2) reads "(בוטל)" (line 2474), repealed.
  So the cross-reference points at nothing, and there is no second dependency to supply beside Part D (the comparison below, B2, found Axiom naming it as one).
  (0.3.0) The day she reaches the age now declines, by default, where the month she reaches it in lacks her day of birth (fork N4, SHRUG); the age in months, which is what s 342(c)(2) and the capstone read, is unchanged.
- **GAPS 6, s 72.** Fork K6 (ask row IL-06 about the first day of the month, declining a month with a birth or an 18th birthday after it) can give way to: for each child, whether `s 72 — the allowance is paid for month` M; then ask IL-06 about the family of the children paid for. Under s 72 the month of an 18th birthday is paid in full, and a child born after the 15th starts the next month. Which day of the month to put to IL-06 for the count and the amounts is still the adapter's choice; s 72 does not say.
  (0.2.0) The export's name, inputs and type are unchanged; it now declines a month from the death to the third month after it when an allowance is recorded as paid for a child for whom (a) and (b) made no month payable (item 08n-PAID), which the capstone, giving "was paid" as FALSE for living children, never reaches.
- **GAPS 9, s 335.** The input convention "an employee pays in all nine branches" can give way to `s 335 — the branches for which contributions are payable, for`, which returns that list for a resident employee insured in every Chapter, and a shorter one for a controlling shareholder, a non-resident or a housewife. The statuses remain inputs.
- **GAPS 13, NII s 65.** Nothing new: IL-06 already encodes it, and residence ("יושב בישראל") remains an undefined status.

## 7. Nouns to reconcile

- **`A branch of insurance`** is declared here constructor for constructor as in rows IL-04 and IL-05 (row IL-07's RECONCILE.md N1). A module that imports two of the three and names a constructor in a bare `LIST` meets the "multiple definitions" error IL-07 measured; one shared nouns module for the subject would end it.
- **The person.** IL-06 `A person` (with `insured under Chapter 11`, `a housewife as defined in section 238`, which this row's `A person in a contribution period, for section 335` spells the same); IL-04 `A person who works`; IL-05 `An insured person, for section 342(a)-(b)`. s 335 reads statuses from all of them.
- **The branch list.** IL-04's and IL-05's input `branches for which contributions are payable under section 335` is this row's output.
- **The Part D age.** IL-05's `a woman` constructor carries `the age fixed for her by her month of birth in Part D of Schedule A1, in months`; this row computes it from a date of birth.
- **The child and the month.** IL-06's `A child` (date of birth) and `A family on a day`; this row's `An entitlement to the child allowance for a child, for section 72` (the day it arose and how it ended). A child's 18th birthday in IL-06 is the day its entitlement ceases here.
- **Month counts.** Two helpers (`the month count of`, `s 72 — the month count of`) do what row IL-08's ITO half calls `the serial number of month`; one shared date module would serve all three.

## 8. Sources

The deposited Law, at the lines cited; its table of old and new section numbers (lines 5247-5458); the three enacted amending Laws deposited under `../../registers/source-bundle/amending-laws/`, searched only to see whether they touch this half (`BRIEF.md`).
Nothing was fetched for this half.
No officially published table of Part D was fetched to cross-check the tests; the expected values are the printed table, row by row.

## 9. Open questions for a domain expert

1. N1: does the Institute pay a child born on the 15th for that month?
2. N2: is the allowance continued three months after the death of a child for whom no payment had yet been made?
3. Part A's table for women ends at December 1955 in the consolidation: is a row missing (the 2021-2022 changes to women's retirement age), or does Part A not apply to later births? Not in this row's scope; noted for whoever encodes Part A.
4. A3: from when does the present text of s 335 apply?
5. (0.2.0) N5: is a child who died on the seventh calendar day of life, counting the day of birth, one who "lived seven days"?
6. (0.2.0) N6: does s 72(b) pay a child born at home and never in a hospital who dies within seven days?
7. (0.2.0) With N2: does (c) run after a payment made for a child for whom (a) and (b) made no month payable (a payment in error, or a record that is wrong)?

## 10. What was not done

- **No independent test pass**, **HG1 not sought**, **not committed**: as for the other half. (0.2.0: an independent pass has since been run, `INDEPENDENT-FINDINGS.md`, and 0.1.0 was committed; HG1 is still not sought.)
- **No official cross-check of Part D**: the Institute publishes the women's ages by month of birth; a fetched copy would make a second oracle for the 37 assertions. (0.3.0: 51 assertions, the 37 of the table among them.)

## Comparison with Axiom's RuleSpec (2026-10-07)

Written by the comparison author for row IL-08 (`lad-il-08`), one session, no sub-agents, on 2026-10-07, after both halves of the row and both independent passes had been deposited, as the semi-cleanroom ruling of 2026-10-06 requires.
This section covers the National Insurance half only; the Income Tax Ordinance half's `NOTES.md` carries its own, including fork F19 (s 40(a)'s pointer to the old s 109 and the repealed Schedule D).
Nothing else in this row, and nothing in the commons, was edited; nothing was repaired.
A divergence below is a finding, not a fix.

### What was read

**Axiom.** A local clone of the Axiom Foundation's `rulespec-il`, read-only, at commit `95c6f32c87c75e318631cbd77c14b840bc536c15` (the merge of its PR #8, 2026-10-03, "encode/il-nii-contributions"); nothing was pulled.
Read: `NOTICE`; the heads of `LICENSE` and `LICENSE-CODE`; `data/coverage/tax-benefit-source-map.json` (whole); `docs/ENCODING-GAPS.md` (lines 140-714, and its headings above); `docs/encoding-charter.md` lines 40-55; `known-missing-money-atoms.yaml` and `known-validation-gaps.yaml` (whole; neither has any entry); `README.md` by search; `il/statutes/national-insurance-law-1995/section-337.yaml`, `section-342.yaml` and `section-348.yaml` (whole) with their `.test.yaml` files; `schedule-j/sign-1.yaml` (its rule list, lines 1-125 and its total-rate rules); the composed pipeline (lines 1-535, and the child facts and outputs of all 15 cases).
No Axiom module exists for Part D, s 72 or s 335 (`ls il/statutes/national-insurance-law-1995/`: ss 1, 66, 67, 68, 334, 337, 342, 348, Schedules J and K), so there was no module or companion test file of theirs for them.
Nothing of any other Axiom repository was read, and nothing under `l4-ide/specs/research/AXIOM-*`.

**Ours.** This row's `BRIEF.md`, `NOTES.md`, `encoding.json`, the four rule and noun modules, `INDEPENDENT-FINDINGS.md`, `DECIDED-ANSWERS.md` and `tests-independent.l4`, in full; row IL-07's `GAPS.md`.
The deposited Law at the lines cited below (sha256 `78bf47ee…552a97`, checked).

**Licence.** `NOTICE` puts Axiom's encodings, companion test cases, parameter values and provenance metadata under CC BY 4.0 (`LICENSE`) and its tooling under Apache 2.0 (`LICENSE-CODE`); confirmed from the three files.
Axiom material appears here only as short attributed snippets: Axiom Foundation RuleSpec corpus (CC BY 4.0), https://github.com/TheAxiomFoundation.

**Runs.** Axiom's stated conventions and figures for these provisions were put through a scratch copy of this directory (the session scratchpad, `lad-il-08/nii/zz-axiom-cases.l4`) with `/Users/mengwong/.local/bin/l4 run`, `JL4_LIBRARY_PATH` unset, at 2026-10-07T06:01:08Z, under the binary the other half's section records (sha256 `6015a4c3…3b54a6`, not the build section 0 used).
14 assertions, 14 satisfied, 0 errors (a first run failed to compile on `length`, which this binary's prelude does not define; the two assertions were rewritten with list equality, and no expected value changed).

### Coverage: what Axiom did with each provision of this half

Axiom's inventory, `tax-benefit-source-map.json`, lists this Law's encoded sections as ss 1, 66, 67, 68, 334, 337, 342 and 348, with Schedules J and K (lines 88-109).

| provision (ours) | source lines | ours | Axiom | Axiom file, status |
| --- | --- | --- | --- | --- |
| Schedule A1, Part D | 4431-4453 | encoded: the age in months by month of birth, and the day it is reached | **left out**, named, with a reason: "Three encoder attempts were blocked by the numeric-grounding check"; its absence is one of the reasons they give for deferring the employee deduction of s 342(c)(1) and the women's limb of s 342(c)(2) | source map line 125; `ENCODING-GAPS.md` lines 651-664; `section-342.yaml` lines 24-42; `README.md` line 53 |
| s 72 | 853-856 | encoded: whether the allowance is paid for a month | **left out**, not named anywhere; the composition counts a child for "the allowance month" from two per-case inputs, `child_N_age_at_month_years` (below 18) and `child_N_is_present_in_israel` | composed pipeline lines 72-81, 148-170; `ENCODING-GAPS.md` lines 564-566 |
| s 335 | 3610-3620 | encoded: the branches in which contributions are payable | **left out**, "deliberately out of scope"; **an input** to their s 348 (`contributions_payable_under_section_335`, one Boolean); their s 337 applies Schedule J's printed employee totals, so implicitly all nine branches | `encoding-charter.md` lines 51-52; `section-348.yaml` line 69; `section-337.yaml` lines 74-80; `ENCODING-GAPS.md` line 612 |
| s 65 | 799-809 | not re-encoded here (row IL-06 encodes it) | **applied without a module**: the age-and-presence proviso of s 65(a), per child, inside the composition; the maintained-child limb and s 65(b) not modelled | source map lines 119, 127-133; `ENCODING-GAPS.md` lines 543-568 |
| s 67A | — | inert: no such section | no s 67A either; the identifiers `nii-section-67a-*` are s 67(a) (see below) | `ENCODING-GAPS.md` lines 482-502; `README.md` line 49 |

**Counts**, over the three provisions this half encodes: encoded by Axiom as a module, **0**; handled as an input, **1** (s 335, as one Boolean in s 348); left out, **3** (Part D with a stated reason; s 72 unmentioned; s 335 by its charter).
The one stated reason, for Part D, is a limit of their encoder, not a reading of the text.

### Where Axiom applies one of our provisions

Nowhere: it applies none of Part D, s 72 or s 335.
Three things Axiom states about them were put through our rules instead.

**Part D.** `ENCODING-GAPS.md` (lines 652-654) gives the table's range as "65 for the oldest cohorts, rising to 70 for every woman born in May 1950 or later" and quotes the row for September 1939 to April 1940.
Ours: born June 1939, 780 months; May 1950, 840; January 1990, 840; September 1939 and April 1940, 788 (5 assertions, satisfied).
They agree.
Axiom's stated obstacle, that "a month number taken as input is a literal the text does not print", does not arise in ours: the rule takes a date of birth, and the band edges are typed from the rows (lines 4438-4453) and tested edge by edge, here and by the independent pass.

**s 72.** The composition's summary (lines 72-81) says a child who turns 18 later in the year "still counts for the allowance in the months before the birthday and stops counting after it"; its gap entry (lines 564-566) says the age "is one number for the case, so a child that turns 18 mid-year changes state at the start of the modelled month rather than on its birthday".
Ours, for a child born 20 July 2008 whose entitlement ceases on 20 July 2026: paid for June and July 2026, not August (s 72(a), last limb, line 854).
For a child born 20 March 2026: not paid for March, paid from April (s 72(a), second limb).
5 assertions, satisfied.

**s 335.** Their s 337 charges an employee Schedule J's printed totals, which cover all nine branch rows (items 1 and 3-10).
Ours, for a resident employee insured in every Chapter s 335 reads: all nine branches; for the same person as a controlling shareholder in a closely-held company: seven, without unemployment and insolvency (s 335(e), (f), lines 3615-3616).
4 assertions, satisfied.

### Axiom's cases put through our encoding

| Axiom case(s) (file, line) | what the case takes from our provisions | put through ours | result |
| --- | --- | --- | --- |
| `section-337.test.yaml` 1, 12: an employee's contributions on 15,000 and 5,000 for January 2026 | s 335 implicitly: the Schedule J totals, all nine branches | s 335 for a resident employee insured in every Chapter | **consistent**: nine branches; the case does not state the person's statuses, and the rates are outside this row |
| `section-348.test.yaml` 1, 14, 27, 40 | s 335 as one Boolean (`true` three times, `false` once) | — | **could not be run**: the case supplies s 335's conclusion, not the statuses our rule reads |
| `section-342.test.yaml`, all 5 | s 342(a) and (d) only | — | not applicable: none reaches Part D |
| composed pipeline, all 15 | the monthly child count, which s 72 governs at a birth and at 18 | — | **could not be run**: no case gives a date of birth, and each case's period is the whole of 2026 (2026-01-01 to 2026-12-31) |

### Divergences and differences

| id | provision | ours | Axiom | source lines | classification | repair if ours is wrong |
| --- | --- | --- | --- | --- | --- | --- |
| B1 | Part D | encoded | not encoded (encoder failure); its figures as stated agree with ours | 4431-4453 | scope difference | — |
| B2 | s 342(c)(2), the consumer of Part D | not ours; NOTES section 6 offers Part D to the composer of s 342(c)(2) without remark | names "the operative qualification in section 245(b2)" as a second missing dependency beside Part D | s 342(c)(2) line 3662 makes the women's age "subject to s 245(b2)"; s 245(b2) reads "(בוטל)", line 2474 | **theirs wrong** in a stated reason, on the deposited text: the qualification is repealed, so there is nothing to supply (not checked against their corpus expression of 2026-06-15, though every amendment tag on s 245, line 2464, is older than that) | — (a note for whoever composes Part D with s 342(c)(2): the cross-reference points at a repealed subsection) |
| B3 | s 72 | encoded | not encoded; per-month age and presence supplied by the caller; no 15th-day rule, no seven-day rule, no three months after a death | 853-856 | scope difference; the convention their gap entry states (the state changes at the start of the month of the 18th birthday) would lose the month s 72(a) pays, and nothing in their pipeline declines the month of a birth after the 15th | — |
| B4 | s 335 | encoded: the branch list | not encoded; s 337 charges every employee the full employee total, with no input through which s 335's exclusions reach the rate | 3611, 3615-3616 | scope difference, silent on their side: a controlling shareholder in a closely-held company (no unemployment, no insolvency) or a non-resident worker (s 335(a): maternity, with work injury and insolvency if insured under Chapters 5 and 8) is charged the full employee total, including branches s 335 does not impose on them | — |
| B5 | Schedule J's branch rows against its totals | not ours | recorded as `unexplained` (`ENCODING-GAPS.md` lines 598-617) | checked here on the deposited text: in the 2025-2026 table the employee column above the reduced bracket sums over its nine rows (lines 4720, 4722-4729) to 14.39 against the printed 14.50 (line 4730), and to 14.49 against 14.60 at the 2024-2027 work-injury rate | not a divergence in s 335; a caution for composition: a rate built by summing the rows of our branch list will not reproduce the printed total even for a full employee | — |
| B6 | s 67A | no such section | none either | 817; 5326; 1162-1163 | agreement | — |
| B7 | s 65 | row IL-06's | applied in the composition without a module | 799-809 | scope difference (row IL-06's comparison, not this one) | — |

No divergence shows a rule of this half wrong on the text.

### Our independent pass's findings, and Axiom

| finding (`INDEPENDENT-FINDINGS.md`) | Axiom |
| --- | --- |
| 1-2, 72-57: s 72(c) for a child whose payment window was empty (fork N2) | nothing: s 72 not encoded |
| 3-5, D-46 to D-48: the day a woman reaches the Part D age when the day does not exist (fork N4) | nothing: Part D not encoded, and their man's age under s 342(c)(2) is a parameter (70), with no day computed |
| 6-7, 72-14 and 72-30: the May 2015 gate (A2) | nothing to compare |
| silent paths (the unchecked "was paid" input, the moved day, the gate only on the export) | nothing to compare |
| 72-39, 72-42, 72-44: a 29 February birthday, how seven days are counted, a home birth | nothing: their composition leaves the 18th birthday to the caller as ours does, and has no seven-day rule |
| 335-R1, the rate of contributions; 335-R4, who pays | **Axiom encodes both**: the rates in s 337 and Schedule J, the self-payer judgment of s 342(a) and the multiple-employer rules of s 342(d) |
| D-R1, a man's age under Part D | Axiom carries the man's age of s 342(c)(2), 70, as a parameter (`section-342.yaml` lines 89-104; line 3662); Part D is for women only, as both the tester and our rule names say |

### Our forks, and the s 67A observation

N1, N2 and N4 have no Axiom counterpart.
N3 (one maternity branch from s 335(a) and (i)): their Schedule J keys items 1 and 2 separately, item 2 being maternity for one who is neither an employee nor self-employed (line 4721); the employee column prints nothing for item 2, so nothing for an employee turns on the question, and nothing in Axiom conflicts with N3.

**s 67A.** Axiom's record agrees that there is no s 67A.
Its two gap entries whose identifiers read `nii-section-67a-…` (`ENCODING-GAPS.md` lines 482-502) are about s 67(a), the rule that a child is counted with one insured parent at a time, which they quote word for word from the provision at line 817; `README.md` line 49 calls it "§67(א)'s one-parent-at-a-time limit".
Their source map lists s 67, not s 67A, among the encoded sections (lines 88-97).
So the observation in section 2 stands, and Axiom's material supports it.
A guess, not checked (the backlog was not read in this pass): the "s 67A" in row IL-08's ruled list may be a reading of Axiom's identifier `67a` as a section number; the same list's ITO s 121A matches an item of Axiom's `not_encoded` list.

### What Axiom does that this half does not, and the reverse

**Axiom, not us**: the rates (s 337, Schedule J), the reduced bracket (s 334), the ceiling and small non-work income (s 348, Schedule K), who pays (s 342(a), (d)), the man's age in s 342(c)(2); all outside this row's scope, and the natural consumers of our s 335 list and Part D age.
**Us, not Axiom**: Part D, s 72 and s 335, with forks N1-N4 and the refusals for earlier periods.

### Bottom line

Axiom encodes none of the three provisions of this half.
Part D it tried three times and could not encode for a reason in its tooling, and its absence is one of the reasons Axiom gives for deferring the employee's deduction under s 342(c)(1); our Part D module is that missing piece, and the figures Axiom states for the table agree with ours.
s 335 it left out by charter, and its s 337 charges every employee the full employee rate; our branch list is what a composer needs to charge a controlling shareholder in a closely-held company or a non-resident worker correctly, with the caution that Schedule J's branch rows do not add up to its printed totals.
s 72 does not appear in Axiom's material at all; its monthly child count leaves the first and last months to the caller.
On s 67A the two records agree.
No finding of this comparison shows a rule of this half wrong; one stated reason of Axiom's points at a repealed subsection (B2).
