# NOTES — Income Tax Ordinance s 66 (separate calculation), row IL-02

Encoder: one Claude session (Opus 5.5), run IL-02-20261006, 2026-10-06, working alone from `BRIEF.md`.
Status: **draft**, version 0.3.0 (fork F19 ruled and made a switch, 2026-10-08, BACKLOG IL-38; see the next section). (0.3.0; version 0.2.0 was the repairs of BACKLOG IL-15, in the section after it.)
No domain expert has read this against the source; HG1 has not been sought.
No independent test pass was run (the run was instructed to work alone, without sub-agents); see section 8.
(0.2.0, 02-W1: true of the encoding run, stale since. An independent test pass was run after deposit by fid-il-02, commit 240a478: `DECIDED-ANSWERS.md`, `tests-independent.l4`, `INDEPENDENT-FINDINGS.md`. Its V-4 is repaired in 0.2.0 and its E-4 is recorded as fork F19; from 0.3.0, with F19 ruled, all 103 of its assertions hold.)

## Version 0.3.0 (2026-10-08): fork F19 as a switch (BACKLOG IL-38, SHRUG)

Agent shrug-il-38 (the repair session of IL-15, one Claude session, Opus 5.5), 2026-10-08, under the lead's repair brief of that day and its addendum.
Meng ruled on 2026-10-08 (SHRUG, BACKLOG IL-24 and IL-38) that fork F19, inventory 02-E4, becomes one named switch, default DECLINE, the other reading kept by name and tested.
F19: a child born before 2024 (in practice in 2023), the mother's (c)(4)(a1) election set, asked of tax year 2024, where the point moved is one she had "בשנת הלידה", a year whose text this row does not hold (A1).

**What changed** (all in `ito66-c-credit-points.l4`):

- A new type, `A reading of section 66(c)(4)(a1) for a child born before 2024`, with two readings: (i) `an election for a child born before 2024 is carried by the text of the year of the calculation`, the behaviour of 0.1.0 and 0.2.0 (4½ + 1 = 5½); (ii) `an election for a child born before 2024 is declined`.
- The switch: `section 66(c)(4)(a1) — the reading this row takes for an election for a child born before 2024` names (ii).
- The refusal, by name and in these words: "the text of section 66 this encoding holds does not decide a birth-year credit point elected for a child born before 2024".
- Three rules gain a form that takes the reading, named with the suffix `, reading an election for a child born before 2024 as` r: `s 66(c)(4)(a)-(a1) — the mother's credit points for … in tax year …`, `s 66(c)(4)-(6) — the credit points of the … in … for …`, and `s 66(c) — the credit points it gives the … in …`.
  Each rule of the old name keeps its signature and passes the switch, as IL-04's F6 switch does.
- The fork is reached only where the election is set, the child turns 1 in the tax year, and the child's tax year of birth is before `the first tax year the deposited text of section 66 governs` (2024); everywhere else both readings answer alike, and the tax-year gate still refuses a year before 2024 before the reading is asked.
- The man's points are never reached: the election is the mother's ("אמו של ילד").

**Tests.**
None of this row's own tests rested on reading (i): every election test before 0.3.0 has a child born in 2024 or later, which the fork does not reach, so none needed re-pointing.
Fourteen assertions were added to `ito66-tests.l4`, every expected value worked out from lines 2466-2467 and 2475 in the comment beside it before the module was run; all passed on their first run.
A control copy with three of them made wrong reported two failures and one refusal.
The independent tester's E-4 (`tests-independent.l4:385`), which expected a refusal, now holds; its file was not edited for this change, and `check.sh` no longer lists it in `expected_failed`.

**Answers changed** (old is 0.2.0's answer; "declined" is the F19 sentence above):

| where | case | old | new | why |
| --- | --- | --- | --- | --- |
| `s 66(c)(4)(a)-(a1) — the mother's credit points for` | a child born 2023, the election set, tax year 2024 | 5½ | declined | F19 ruled, default (ii) |
| `s 66(c)(4)-(6) — the credit points of the` | the woman, the same child, 2024 | 5½ | declined | the same, through (a1) |
| `s 66(c) — the credit points it gives the` | the woman of a couple with that child, 2024 | ½, 0, 5½ | declined | the same, through the children's points |
| `tests-independent.l4:385` (E-4) | the same as the row above, the tester's | answered (failed) | refused (satisfied) | expected value unchanged |

No other answer moved: a child born from 2024 on, a child without the election, the year after next, and the man's points answer as before.

**Assertions added** (`ito66-tests.l4`; none existed before, so "old" is none):

| line | case | new | why (source) |
| --- | --- | --- | --- |
| 644 | the switch | `an election for a child born before 2024 is declined` | SHRUG |
| 647 | mother's points, born 2023, elected, 2024, default | declined | SHRUG; line 2467 "בשנת הלידה" |
| 649 | the same, reading (ii) by name | declined | SHRUG |
| 651 | the same, reading (i) by name | 5.5 | line 2466, 4½ "החל בשנת המס שלאחר שנת לידתו"; line 2467, one point moved |
| 653 | the same in 2023, reading (i) by name | refused, A1's sentence | the year gate comes first |
| 658 | born 2023, no election, 2024, default | 4.5 | line 2466 |
| 660 | born 2023, elected, 2025, default | 4.5 | line 2466, age 2; the election moves nothing then |
| 662 | born 2024, elected, 2025, default | 5.5 | lines 2466-2467; the year of birth is held |
| 665 | (c)(4)-(6), the woman, that child, 2024, default | declined | through (a1) |
| 667 | the same, reading (i) by name | 5.5 | through (a1) |
| 673 | (c), the woman, 2024, default | declined | through the children's points |
| 675 | the same, reading (ii) by name | declined | the same |
| 677 | the same, reading (i) by name | ½, 0, 5½ | line 2465 (s 36A ½); no s 37 point; 5½ as at 651 |
| 678 | (c), the man, 2024, default | 0, 0, 4½ | line 2475, 4½ "החל בשנת המס שלאחר לידתו"; the election is the mother's |

### What `check.sh` prints, version 0.3.0

Run from 2026-10-08T15:56:54Z to 15:57:08Z as `./check.sh`, with `l4` on PATH: `/Users/mengwong/.local/bin/l4` -> `~/.cabal/bin/l4` -> the cabal-store build `jl4-0.1-d4290e25`, sha256 `f4f2bd2558f02f828f0deced5f74313a33670f08cc3275ff95b83f2cde71e448`, the same before and after the run.
`JL4_LIBRARY_PATH` unset.

```
module                                    errors satisfied  failed  refused  expected
ito66-a-separate-calculation.l4                0         0       0        0         0
ito66-ab-taxable-income.l4                     0         0       0        0         0
ito66-b-property-income.l4                     0         0       0        0         0
ito66-c-credit-points.l4                       0         0       0        0         0
ito66-d-common-source.l4                       0         0       0        0         0
ito66-fixtures.l4                              0         0       0        0         0
ito66-nouns.l4                                 0         0       0        0         0
ito66-tax-years.l4                             0         3       0        0         0
ito66-tests-ita.l4                             0        23       0        0         0
ito66-tests.l4                                 0       193       0        0         0
tests-independent.l4                           0       103       0        0         0
TOTAL (11 modules)                             0       322       0        0
```

Exit 0.
No module is expected to fail or refuse; `expected_red` in `encoding.json` is empty.

## Version 0.2.0 (2026-10-08): repairs (BACKLOG IL-15)

Repair agent rep-il-15 (one Claude session, Opus 5.5), 2026-10-08, job B of `l4-pipeline/findings/il-2026-10-08/jobs.txt`, under the lead's repair brief of that day.
Each item below is an id in `l4-pipeline/findings/il-2026-10-08/inventory.tsv`.
Each finding was read where it was recorded (`INDEPENDENT-FINDINGS.md`, the Axiom comparison at the end of this file, and IL-07's `RECONCILE.md` N3, N7 and R2) before it was repaired.
Every new expected value was worked out from the source, in a comment beside its assertion, before the module was run; all passed on their first run.
A control copy in a scratch directory, with four of the new expectations made wrong, reported three failures and one refusal, so the new assertions can fail.

### Items

**02-V4 (OURS-WRONG): rules answered tax years before 2024.**
The year gate `in tax year … , the answer is` (`ito66-tax-years.l4`) now wraps every rule that takes the couple, and so carries the tax year, and the one rule that takes a tax year directly:

- `s 66(d) — subsection (a) applies to` (`ito66-d-common-source.l4`);
- `s 66(a)(1) — the spouse who is not the registered spouse may claim a separate calculation, for` and `s 66(a)(1) — a separate calculation is made, for`;
- `s 66(a)(2) — the spouse to whose taxable income the income not from personal exertion is added, for`;
- `s 66(a)(3) — for … , the income of this child is the registered spouse's:` and `s 66(a)(3) — the children's income deemed the registered spouse's, for`;
- `s 66(b) — for … , the spouse has other income for which a separate calculation is made:` and `s 66(b) — for … , the property income goes:`;
- `s 66(c)(1A) — a separate calculation of income from personal exertion is requested by the`, `s 66(c) — governs the calculation of the`, `s 66(c)(4A), (6) — a child of the widowed partner of the` and `s 66(c)(4)-(6) — the credit points of the … for`;
- `s 66(c)(4)(a)-(a1) — the mother's credit points for … in tax year`, which takes the year itself.

The three rules gated in 0.1.0 keep their gate.
Not wrapped, and why: the rules that take one spouse, one item, a child's age or a provision carry no year, and state the deposited text; `the particulars of the …` and `the particulars of the partner of the …` are plumbing; `a woman and a man:` is a fact about the couple, not a provision.
The three parts of the (a)-(b) assembly in `ito66-ab-taxable-income.l4`, which is not among job B's files, are not wrapped; each sums a gated rule and refuses through it, as three new assertions show.
The independent tests' V-4 (`tests-independent.l4:204`) now passes.
No answer for a tax year from 2024 moved.

**02-R2 (OURS-WRONG; assumed, not ruled: the lead's choice).**
Row IL-01 declines s 36A for a woman who is a foreign worker, because s 48A (line 1811) lets regulations take the credits of Part C, Chapter Three from a foreign worker, and s 48A is not encoded.
This row gave every woman in a separate calculation the half point that s 66(c)(4) gives "לפי סעיף 36א", with no foreign-worker input.
Of the two options in the inventory (drop the half point and leave s 36A to IL-01, or add the fact and decline in IL-01's words) the lead chose the second.

- New field on `A spouse`: `a foreign worker within the meaning of section 48A` (BOOLEAN), named apart from IL-01's `a foreign worker` so the two cannot collide (section 9).
- New rule `s 66(c)(4) — the half point under section 36A, for`: a woman who is a foreign worker is declined with "section 48A and the regulations made under it are not encoded in this model", IL-01's words (`ito-s34-s36-s36a-credits.l4:103` at commons HEAD `3f7d673`, and `:115-116` in IL-01's v0.2.0 working tree of 2026-10-08, where rep-il-14 confirmed the string is unchanged and is applied from tax year 2002, so in every year this row answers; not edited); any other woman ½; a man 0, a foreign worker or not, as in IL-01, where s 36A does not reach a man and so s 48A cannot change the answer.
- The decline is a rule named `row IL-02, section 66(c)(4): section 48A and the regulations made under it are not encoded in this model`, prefixed as row IL-08 prefixes its own, so it cannot collide with IL-01's rule of the same words where both rows are imported.
- `s 66(c) — the credit points it gives the` takes its first field from the new rule. For a foreign-worker woman that field refuses and the other two answer, because L4 evaluates a field of a record only when it is read; asked as a whole, the record refuses.
- `s 66(c) — in a separate calculation, the … has the entitlement under` `section 36A` declines alike.
- The children's points of (c)(4)-(6) still answer for a foreign worker (A6, section 3).
- The half point under s 37 in (c)(2) reads the caller's s 37 answer, which carries s 48A (row IL-08 declines s 37 for a foreign worker in its own words); nothing is added here.
- The (c)(1) arms still answer "each of the spouses has the entitlement" for ss 34 and 36: they say who holds the entitlement in a separate calculation, and IL-01's counts decline those sections for a foreign worker.

`ito66-fixtures.l4`, the row's own test builders, gains `a spouse, with the foreign-worker fact:`; the builder `a spouse:` keeps its call site and sets the fact FALSE, so `tests-independent.l4` needs no change for 02-R2.

**02-X2 (WORDING).**
Section 1 now says that s 66's own date edges are the caller's: the five-year window of the (a)(1) proviso, "בחמש השנים האחרונות שלפני תחילת תשלום הקיצבה", and the two conditions of (b), "שהיה בבעלותו שנה לפני נישואיו" and "שקיבל בירושה בתקופת נישואיו".
Section 2 marks the two rows, and the headers of the (a) and (b) modules say it too.
The optional computation of the window from the pension's start was not taken: it would change the interface (dates for the start of the pension and for each earlier entitlement), and AX-2 below records that the text fixes no whole-year convention at the edge, so computing it would itself take a reading.

**02-W1 (WORDING).**
The status lines at the head of this file and the recommendation at the end of section 8 said that no independent test pass had been run; one was, commit 240a478.
Both are marked in place.

**CHK-02 (housekeeping).**
`check.sh` declares the tester's one remaining failure, `tests-independent.l4` line 385 (E-4, inventory 02-E4, class AMBIGUITY), as `expected_failed` 1, and gains `expected_refused`, 0 for every module, as IL-04's `check.sh` has.
It exits 0.
(0.3.0: the entry is gone; E-4 holds once F19 is ruled.)

**02-E4 (fork; waits on Meng, BACKLOG IL-24).** (0.3.0: ruled by Meng, SHRUG; see the section above.)
Recorded as fork F19 in section 4, with both readings and who holds each.
The behaviour of 0.1.0, reading (i), 5½, is kept as the default until the ruling.

**02-N3 (WORDING), IL-02's half.**
The type `A child` is now `A child, for section 66` (IL-07 `RECONCILE.md` N3), so that one module can name it beside row IL-06's child.
The rename touches `ito66-nouns.l4` (the DECLARE and the `children` field of `Spouses in a tax year`), `ito66-a-separate-calculation.l4` (2), `ito66-c-credit-points.l4` (5), `ito66-fixtures.l4` (4) and `ito66-tests.l4` (2); no field, constructor of another type, or rule was renamed.
The tester's `tests-independent.l4` names the type at lines 141, 143 (the record constructor), 158, 171 and 190; the lead authorised on 2026-10-08 replacing those five in place, on the precedent of IL-04 v0.3.1, and they were, with no line inserted and no expected value or input changed, and a dated "NOTE BY THE LEAD, 2026-10-08" appended at the end of that file.
Its comment at line 293 still says `A child`; it is prose and needs no change to compile.
No answer moved.

### Assertions added or changed

No expected value of 0.1.0 changed.
One assertion of the independent tests changed outcome with its expected value untouched: `tests-independent.l4:204` (V-4), expected a refusal, answered `TRUE` (failed) in 0.1.0, refuses (satisfied) in 0.2.0.
Added, all in `ito66-tests.l4` (none existed before, so "old" is none; "refused" is A1's sentence, "this encoding does not hold the text of section 66 for a tax year before 2024", unless another is named):

| line | rule, case | new | why (source) |
| --- | --- | --- | --- |
| 492 | (d) applies, 2023 | refused | A1; line 2454 |
| 494 | (a)(1) may claim, 2023 | refused | A1 |
| 496 | (a)(1) made, 2023 | refused | A1 |
| 498 | (a)(2) destination, 2023 | refused | A1 |
| 500 | (a)(3), the child born 2015, 2023 | refused | A1 |
| 502 | (a)(3) children's income, 2023 | refused | A1 |
| 504 | (b) other separate calculation, registered spouse, 2023 | refused | A1 (it answered FALSE before) |
| 506 | (b) where it goes, the woman, 2023 | refused | A1 |
| 508 | (c)(1A) request, registered spouse, 2023 | refused | A1 |
| 510 | (c) governs, the woman, 2023 | refused | A1 |
| 512 | (4A), (6) child of the widowed partner, 2023 | refused | A1 |
| 514 | (c)(4)-(6) the woman's points for the child, 2023 | refused | A1 (the tester's probe had 2) |
| 518 | (a1) a child born 2023, deferring, in 2023 | refused | A1 (it answered 1½ before) |
| 522 | (a)(2) pooled income, 2023 | refused | through line 506's rule |
| 524 | (a) registered apart from the pool, 2023 | refused | through line 502's rule |
| 526 | (a) separate apart from the pool, 2023 | refused | through line 506's rule |
| 531 | (d) applies, 2024 | TRUE | (d)(1) chapeau, line 2479: no common source |
| 533 | (a)(1) may claim, 2024 | TRUE | line 2456: 120,000 of salary |
| 534 | (a)(1) made, 2024 | TRUE | line 2456: she claims |
| 536 | (a)(2) destination, 2024 | `registered spouse` | line 2457: 200,000 > 120,000 |
| 538 | (a)(3), the child, 2024 | TRUE | line 2458: 2024 − 2015 = 9 < 18, his child |
| 539 | (a)(3) children's income, 2024 | 4000 | line 2458: the child's interest |
| 541 | (b) other separate calculation, registered spouse, 2024 | FALSE | fork F7 |
| 543 | (b) where it goes, the woman, 2024 | `it is not calculated separately` | line 2459: no (b) income, no claim |
| 545 | (c)(1A) request, registered spouse, 2024 | FALSE | line 2462: he does not request |
| 547 | (c) governs, the woman, 2024 | TRUE | line 2460, (a)(1) made |
| 549 | (4A), (6), the child, 2024 | FALSE | line 2472: the child is hers |
| 551 | (c)(4)-(6) the woman's points for the child, 2024 | 2 | line 2466: age 9, "החל בשנת המס שבה מלאו לו שש שנים" |
| 593 | half point, a foreign-worker woman | refused, "section 48A and the regulations made under it are not encoded in this model" | 02-R2; line 1811; IL-01 |
| 595 | half point, a woman not a foreign worker | 0.5 | line 2465 |
| 597 | half point, a foreign-worker man | 0 | line 2465 ("האשה"); IL-01 alike |
| 603 | (c)'s record for the foreign-worker woman, whole | refused, s 48A sentence | it holds the declined half point |
| 605 | its half point under s 36A | refused, s 48A sentence | 02-R2 |
| 607 | its children's points | 2 | line 2466: the child turns 10; A6 |
| 608 | its half point under s 37 | 0 | line 2463: no s 37 point |
| 611 | entitlement under s 36A, the foreign-worker woman | refused, s 48A sentence | 02-R2 |
| 613 | entitlement under s 34, the foreign-worker woman | TRUE | line 2461, "יהיו לכל אחד מבני הזוג" |
| 618 | (c)'s record for a foreign-worker man, registered | 0, 0, 1 | line 2465 ("האשה"); line 2476: (5)(c), age 10 |
| 619 | (c)'s record for the woman married to him | 0.5, 0, 2 | lines 2465-2466 |
| 620 | entitlement under s 36A, the foreign-worker man | FALSE | line 2465 ("האשה") |

### What `check.sh` prints, version 0.2.0

Run from 2026-10-08T07:13:30Z to 07:13:50Z as `./check.sh`, after every repair including 02-N3 and a comment-only update of IL-01's line citation (the same counts as runs at 06:59:43Z, before the rename, and 07:02:05Z), with `l4` on PATH: `/Users/mengwong/.local/bin/l4` -> `~/.cabal/bin/l4` -> the cabal-store build `jl4-0.1-d4290e25`, sha256 `f4f2bd2558f02f828f0deced5f74313a33670f08cc3275ff95b83f2cde71e448`, the same before and after the run.
`JL4_LIBRARY_PATH` unset.
Before any edit, the same binary reproduced 0.1.0's figures: 2 errors, 266 satisfied, 2 failed (both in `tests-independent.l4`), 0 refused.

```
module                                    errors satisfied  failed  refused  expected
ito66-a-separate-calculation.l4                0         0       0        0         0
ito66-ab-taxable-income.l4                     0         0       0        0         0
ito66-b-property-income.l4                     0         0       0        0         0
ito66-c-credit-points.l4                       0         0       0        0         0
ito66-d-common-source.l4                       0         0       0        0         0
ito66-fixtures.l4                              0         0       0        0         0
ito66-nouns.l4                                 0         0       0        0         0
ito66-tax-years.l4                             0         3       0        0         0
ito66-tests-ita.l4                             0        23       0        0         0
ito66-tests.l4                                 0       179       0        0         0
tests-independent.l4                           1       102       1        0         1
TOTAL (11 modules)                             1       307       1        0
```

Exit 0.
The one error is the one expected failure, `tests-independent.l4` line 385 (E-4, fork F19).
`ito66-tests.l4` grew from 139 to 179 satisfied: the 40 assertions in the table above.

## 1. What is encoded, and what is not

Section 66 of the Income Tax Ordinance [New Version], every subsection and paragraph, from the Hebrew text at lines 2454-2484 of `registers/source-bundle/income-tax-ordinance-new-version.he.wiki.txt` (Hebrew Wikisource, retrieved 2026-10-06, sha256 `b87f2cf437ccfed35c3164681f4fc7ee015a111633454622751930c8894b81b6`).
That file is an unofficial consolidation of the law as amended at retrieval; Hebrew is authoritative.

What the modules answer, for a married couple in a tax year from 2024:

- whether subsection (a) applies at all, given a common source of income (s 66(d));
- whether the spouse who is not the registered spouse may claim, and has made, a separate calculation, and which of that spouse's income from personal exertion it covers, with the pension proviso (s 66(a)(1));
- which spouse takes the pooled income not from personal exertion (s 66(a)(2)), and which children's income is the registered spouse's (s 66(a)(3));
- whether each spouse's pre-marriage or inherited property income is calculated separately, joined to another separate calculation, or left in the pool (s 66(b));
- the taxable income in each calculation, assembled from the above (`ito66-ab-taxable-income.l4`);
- what s 66(c) does with each provision it names, whether (c) governs each spouse's calculation (including a (c)(1A) request), and the credit points (c) itself gives: ½ under s 36A for the woman, ½ under s 37, and the children's points under (c)(4), (4A), (5), (6) with the mother's (a1) election;
- the children's credit as set against the tax on income from personal exertion, given the value of a credit point and that tax.

What is not encoded, and is taken as an input or left to its owner:
s 65 itself (the consolidated calculation is named as an outcome, not computed); the credit-point counts under ss 34, 35, 36 (IL-01 for 34 and 36); s 37's conditions (a GIVEN per spouse); the value of a credit point (s 33A, IL-01) and the tax on income from personal exertion (ss 121 ff., IL-03), both GIVENs of the one rule that needs them, with no default; the classification of income as personal exertion, transparent-company, REIT, interest or capital gain (the caller's); the determination of the registered spouse under s 64B (an input).

(0.2.0, 02-X2) Nor are three date edges that s 66 itself sets; the caller decides each, and the encoding takes the conclusion:
the five-year window of the (a)(1) proviso, "בחמש השנים האחרונות שלפני תחילת תשלום הקיצבה", is the BOOLEAN `the spouse was entitled to a separate calculation, in the five years before the pension began, …` on each item;
and the two conditions of (b), "שהיה בבעלותו שנה לפני נישואיו" and "שקיבל בירושה בתקופת נישואיו", are decided by sorting the income into the two (b) fields of `A spouse`.
"Encoded" in section 2 means the paragraph's consequences are computed from those conclusions, not that the edges are.

(0.2.0, 02-R2) s 48A and the Income Tax (Credits for a Foreign Worker) Regulations 5775-2014 are not encoded; where they reach the ½ under s 36A that (c)(4) gives, a woman who is a foreign worker is declined in row IL-01's words (A6).

## 2. Coverage table

### s 66 itself

| provision | source line | gist | disposition | where |
| --- | --- | --- | --- | --- |
| 66 heading | 2454 | חישוב נפרד | inert | module headers |
| 66(a) chapeau | 2455 | notwithstanding s 65 | encoded | arm order, `s 66(a)-(b) — the calculations, for` |
| 66(a)(1) | 2456 | the other spouse may claim; the pension proviso | encoded; the five-year window is the caller's (0.2.0, 02-X2) | `ito66-a-separate-calculation.l4` |
| 66(a)(2) | 2457 | non-personal-exertion income to the spouse with higher personal-exertion income; none → registered | encoded | same |
| 66(a)(3) | 2458 | a child's transparent-company, REIT, interest, capital-gain income is the registered spouse's | encoded | same |
| 66(b) | 2459 | pre-marriage or inherited property income; the proviso | encoded; whether the property qualifies is the caller's (0.2.0, 02-X2) | `ito66-b-property-income.l4` |
| 66(c) chapeau | 2460 | the provisions applying to the separate calculation | encoded | `s 66(c) — governs the calculation of the` |
| 66(c)(1) | 2461 | ss 34, 35, 36, 45A, 47, 47A, 121A, 10, 11 for each spouse | encoded | `s 66(c) — in a separate calculation, as to` |
| 66(c)(1A) | 2462 | a separate calculation even if the other has no personal-exertion income | encoded | `s 66(c)(1A) — …` |
| 66(c)(2) | 2463 | s 37 ½ only; no ss 38, 39 | encoded | `ito66-c-credit-points.l4` |
| 66(c)(3) | 2464 | s 40(a) pension points to the registered spouse only | encoded | same |
| 66(c)(4) chapeau | 2465 | the woman: ½ under s 36A; children's points against tax on personal-exertion income | encoded | same |
| 66(c)(4)(a) | 2466 | the woman's table; definitions by reference to s 40(b)(3) | encoded | `s 66(c)(4)(a) — the woman's credit points …` |
| 66(c)(4)(a1) | 2467 | the mother may count one birth-year point in the next year | encoded | `s 66(c)(4)(a)-(a1) — …` |
| 66(c)(4)(b) | 2468 | (נמחקה) | inert | stub |
| 66(c)(4)(c) | 2469 | (נמחקה) | inert | stub |
| 66(c)(4)(d) | 2470 | (פקעה) | inert | stub |
| 66(c)(4), unnumbered tail | 2471 | year of birth / year of majority as in s 40(b)(3), repeated | encoded | `the age the child … turns in tax year` |
| 66(c)(4A) | 2472 | a woman married to a widower: his children | encoded | `s 66(c)(4A), (6) — …` |
| 66(c)(5) chapeau | 2473 | the man: children's points against tax on personal-exertion income | encoded | `ito66-c-credit-points.l4` |
| 66(c)(5)(a) | 2474 | 2½ in the year of birth | encoded | `s 66(c)(5) — the man's credit points …` |
| 66(c)(5)(b) | 2475 | 4½ (1-2), 3½ (3), 2½ (4-5) | encoded | same |
| 66(c)(5)(c) | 2476 | 1 from 6 to the year before majority | encoded | same |
| 66(c)(5A) | 2477 | (פקעה) | inert | stub |
| 66(c)(6) | 2478 | a man married to a widow: her children | encoded | `s 66(c)(4A), (6) — …` |
| 66(d)(1)(a)-(c) | 2479-2482 | (a) applies to spouses with a common source only if all three | encoded | `ito66-d-common-source.l4` |
| 66(d)(2) | 2483 | definition of common source | encoded, as an input | the MAYBE `common source of income` |
| 66(e) | 2484 | (בוטל) | inert | stub |

**Totals for s 66: 22 encoded, 6 inert, 0 out-of-scope, 0 deferred.**

### Provisions s 66 points at

| provision | what s 66 needs from it | disposition |
| --- | --- | --- |
| s 1, "הכנסה מיגיעה אישית", paras (1)-(7), lines 170-178 | which kinds of income are in (a)(1), and which are pensions | encoded, as the `Kind of income from personal exertion` enumeration |
| s 40(b)(3), lines 1644-1645 | year of birth, year of majority | encoded where (c)(4)(a) uses it |
| s 65, line 2448 | the rule (a) and (b) displace; the meaning of "ריבית" | out-of-scope: named as an outcome, not computed; interest classified by the caller |
| s 64B, lines 2440-2445 | who is the registered spouse | out-of-scope: an input |
| ss 64A1, 64A2 | transparent company, real estate investment trust | out-of-scope: the caller classifies the income |
| ss 34, 35, 36, 45A, 47, 47A, 121A, 10, 11 | their own deductions, credits, benefits | out-of-scope: (c)(1) is encoded as "each spouse"; the amounts are those sections' |
| s 36A, line 1597 | ½ point for a woman | out-of-scope: the ½ is stated in (c)(4) itself and encoded there; (0.2.0) declined for a woman who is a foreign worker, as IL-01 declines s 36A |
| s 48A, lines 1810-1812 | whether the ½ under s 36A survives for a foreign worker | out-of-scope: declined by name where it reaches that ½ (0.2.0, 02-R2; A6) |
| s 37, line 1600 | whether the spouse would have a point | out-of-scope: a GIVEN per spouse |
| ss 38, 39 | nothing: (c)(2) excludes them | out-of-scope |
| s 40(a) | pension points | out-of-scope: (c)(3) is encoded as "registered spouse only" |
| s 33A, line 1563 | the value of a credit point | out-of-scope: a GIVEN, no default (IL-01) |
| ss 121 ff. | the tax on income from personal exertion | out-of-scope: a GIVEN, no default (IL-03) |

**Totals for cross-references: 2 encoded, 10 out-of-scope.**
(0.2.0: 2 encoded, 11 out-of-scope, with the s 48A row.)

## 3. Tax years, and assumptions

**A1 — the text governs tax years from 2024.**
The amendment list for s 66 (line 2454) ends at תשפ״ג־6 and תשפ״ד־3.
The page header (line 5) resolves them to ס״ח תשפ״ג, 400 (חוק הגדלת נקודות זיכוי להורים במס הכנסה והרחבת מענק עבודה) and ס״ח תשפ״ד, 630 (חוק סיוע להורים לילדים עד גיל שלוש (תיקוני חקיקה)), counting each `ח:תיבה` entry including the three pages 163, 171, 177 of the 5783 Economic Efficiency Law as three.
The amending Acts could not be fetched: `fs.knesset.gov.il` redirected to a geographic maintenance page (2026-10-06).
The commencement is taken from two Israel Tax Authority circulars (section 7), which say both changes to s 66 apply from tax year 2024, the second "רטרואקטיבית החל מיום 1.1.2024".
For a tax year before 2024 every top-level rule refuses: `this encoding does not hold the text of section 66 for a tax year before 2024`.
(0.2.0, 02-V4: in 0.1.0 only three rules did, and the independent tests found others answering 2023 (V-4). From 0.2.0 every rule that takes the couple, or a tax year, refuses; the rules that take no year state the deposited text. The list is in the version section at the top.)
That is deliberate: the circulars print different 2023 figures for the children's table, so the earlier text certainly differed, and which other paragraphs differed is not known.

**A2 — a tax year after 2026** is answered on the text as it stood on 2026-10-06; that is a projection, not a statement of what was enacted for that year.

**A3 — (c)(1A) moves no income.** It is encoded for its stated consequence, the requesting spouse's entitlement to the (4) or (5) credit points against tax on that spouse's personal-exertion income. It does not create a separate income calculation for the registered spouse in `ito66-ab-taxable-income.l4`.

**A4 — ages are by tax year.** A child's "age in the tax year" is the tax year less the tax year of birth, as s 40(b)(3)'s definitions make every band of (c)(4)(a) and (c)(5).

**A5 — the amounts are the caller's.** Every amount is taxable income in shekels, already classified by the caller.

**A6 — s 48A reaches the ½ under s 36A in (c)(4), not s 66's own points (0.2.0, 02-R2; the decline is assumed, not ruled: the lead's choice).**
s 48A, line 1811, lets the Minister provide that "הוראות פרק זה לענין זיכויים ... לא יחולו על עובד זר"; "פרק זה" is Part C, Chapter Three, "ניכויים, זיכויים וקיצבאות ילדים" (heading at line 1559), which holds s 36A.
(c)(4) gives the woman ½ "לפי סעיף 36א", a credit under that Chapter, so for a woman who is a foreign worker the ½ is declined, in row IL-01's words, because s 48A and its Regulations (noted at line 1812) are not encoded.
The children's points of (c)(4)-(6) are given by s 66 itself, which is in Part D, Chapter Three, "הכנסת בני־זוג" (heading at line 2437), outside "פרק זה"; on its words s 48A does not reach them, and they are answered.
The ½ under s 37 in (c)(2) follows the caller's s 37 answer, in which s 48A is the caller's (row IL-08 declines s 37 for a foreign worker).

## 4. Fork register

Each fork: the readings, the one taken, and the text that licenses each.
None has been settled by a court or the Tax Authority to my knowledge; I did not search case law.

| id | where | readings | taken | why |
| --- | --- | --- | --- | --- |
| F1 | (d)(1), line 2479 | (i) the gate is on the COUPLE: where conditions fail, (a) does not apply to them at all; (ii) it is on the INCOME from the common source only | (i) | "הוראות סעיף קטן (א) יחולו לגבי בני זוג שיש להם מקור הכנסה משותף, רק אם …" names spouses, not income. For (ii): s 64B(b), line 2441, speaks of "הכנסה ממקור הכנסה משותף לפי סעיף 66(ד) שלא מתקיימות לגביה הוראות אותו סעיף", and s 67(a) applies (d) to farm income. |
| F2 | (a)(1) proviso, line 2456 | is a sum received on commuting a pension (s 1 def. para (6)) a "קיצבה" for the proviso? | no | para (6) calls it "סכום המתקבל עקב היוון קיצבה", distinguishing it from the pensions of paras (1)-(4); (5) and (7) are a grant and rent. |
| F3 | (a)(2), line 2457 | spouses with EQUAL non-zero income from personal exertion: neither sentence answers | refuse | "גבוהה יותר" presupposes one is higher; the second sentence covers only "no income". Not filled with a guess. |
| F4 | (a)(2) | is the comparison on the spouse's whole personal-exertion income, or only what is calculated separately? | whole | "הכנסתו החייבת מיגיעה אישית" is not qualified. The other reading would exclude a pension the (a)(1) proviso keeps on the registered spouse. |
| F5 | (a)(3), line 2458 | "ילדו": the registered spouse's own child only, or any child of the couple? | own child | the possessive is singular and attached to "בן הזוג הרשום". A child of the other spouse alone is not reached. |
| F6 | (a)(3) | does s 65's exception (assets from inheritance, or compensation or insurance for bodily injury) apply? | no | (a)(3) restates s 65's child rule without the exception and imports only s 65's meaning of "ריבית". The opposite reading: (a)(3) is s 65's rule under s 66, and the exception travels with it. |
| F7 | (b) proviso, line 2459 | "הכנסה אחרת לגביה נערך חישוב מס נפרד": only the (a)(1) calculation of the other spouse; or also the registered spouse's income once (a) applies, or a (1A) request | (a)(1) only | the registered spouse's income is assessed on him under s 65 as modified, and s 66 calls only the other spouse's calculation "חישוב נפרד". So a registered spouse's claimed (b) income is always calculated on its own. |
| F8 | (c)(1A), line 2462 | is a (1A) request shut by the (d) gate? | no | (d) gates "סעיף קטן (א)"; (1A) is in (c). The opposite reading: (c) states provisions for "the separate calculation", which (a) creates, so (d) reaches it indirectly. |
| F9 | (c)(4)-(6) | a couple of the same sex: who is "האשה", who is "הגבר"? | refuse | the definite articles presuppose one of each; the text does not say. (c)(3), which does not turn on sex, still answers. |
| F10 | (c)(1)-(4) | a provision (c) does not name (ss 39A, 39B, 40A-40D, 44, 45, 46, …) | refuse | s 66 is silent; the provision's own wording decides, outside this slice. |
| F11 | (c)(4)(a1), line 2467 | does the election reach a step-mother's points under (4A)? | no | "אמו של ילד": the child's mother. |
| F12 | (c)(4A), (6), lines 2472, 2478 | a partner's children from an earlier marriage that ended other than by death | not counted | the paragraphs say "לאלמן" / "לאלמנה". |
| F13 | (c)(1A), (4), (5) | "כנגד המס החל על הכנסתה מיגיעה אישית": a cap on the children's credit, or only an ordering? | a cap: the credit is the lesser of points × value and that tax | a credit point is "המקוזז כנגד המס" (s 33A); naming one tax confines the set-off to it. The ½ under s 36A precedes "ובנוסף" and is not confined. |
| F14 | (a)(2) with (a)(3) | does the children's (a)(3) income, once deemed the registered spouse's, join the (a)(2) pool and move with it? | no: it stays on the registered spouse | (a)(3) says whose income it is, specifically; reading it into the pool would let (a)(2) send it to the other spouse, contradicting "בן הזוג הרשום". |
| F15 | (a)(3) | "שטרם מלאו לו בשנת המס 18 שנים": a child who turns 18 during the year | excluded | read as "has not turned 18 by the end of the tax year"; age in the year at most 17. |
| F16 | (c) chapeau with (c)(4), (5) | once (a)(1) gives a separate calculation, does (c) govern the registered spouse's calculation too? | yes | (c)(1) says "לכל אחד מבני הזוג", and (c)(4)/(5) speak of the woman and the man, one of whom is the registered spouse. |
| F17 | (c)(4), (5) | must the child be maintained by, or live with, the spouse (as s 40(b)(1) requires)? | no condition | (c)(4) and (5) say only "ילדיה" / "ילדיו". |
| F18 | (c)(1A) | does "בן זוג" include the registered spouse? | yes | the paragraph says "בן זוג", not "בן זוג שאיננו בן זוג רשום" as (a)(1) does, and it would otherwise add nothing to (a)(1). |
| F19 (0.2.0, 02-E4) | (c)(4)(a1), line 2467, at the vintage boundary of A1 | a child born in 2023, the mother's election set, asked of tax year 2024: (i) the 2024 text governs the 2024 calculation and says where the point lands, 4½ + 1 = 5½; (ii) the point moved is one "מתוך נקודות הזיכוי שלהן היא זכאית כאמור באותה פסקה, בשנת הלידה", the year of birth is 2023, and whether a 2023 mother could elect and had a point to move is 2023 law, which is not held: refuse | (i), kept as the default in 0.2.0; **(0.3.0) RULED by Meng on 2026-10-08 (SHRUG): one named switch, default (ii), a refusal by name; (i) kept by name and tested** (BACKLOG IL-38; switch `section 66(c)(4)(a1) — the reading this row takes for an election for a child born before 2024`) | (i) is the encoder's, taken by construction in 0.1.0 and unrecorded until 0.2.0. (ii) is the independent tester's (E-4, `tests-independent.l4:385`, confidence L; "on reflection I would not call the encoding wrong"), left failing and declared in `check.sh`. Axiom is silent: it does not apply (a1) (AX-14). The input `the mother elects to count one birth-year credit point in the following tax year` carries no year, so the encoding cannot tell an election of 2023 from one of 2024. Under the lead's recommendation for IL-24 (a named switch, default decline), (ii) would become the default. (0.3.0: it has; the tester's E-4 now holds.) |

**A consolidation oddity, not a fork.**
The definitions of "שנת לידה" and "שנת בגרות" appear twice: inside (c)(4)(a) at line 2466 ("לעניין זה ולעניין פסקה (5) …") and again as an unnumbered line after (c)(4)(d) at line 2471 ("לענין זה …").
Both refer to s 40(b)(3) and say the same thing, so nothing turns on it; the second is probably a survivor of an earlier layout of the paragraph.

## 5. Answer table: the children's credit points under s 66(c), tax years from 2024

Age = the tax year less the child's tax year of birth.

| age in the tax year | the woman, (c)(4)(a), line 2466 | the man, (c)(5), lines 2474-2476 | ITA circulars (section 7) |
| --- | --- | --- | --- |
| 0 (year of birth) | 2½ — or 1½ if she elects under (a1), line 2467 | 2½ — (5)(a) | 2.5, each parent |
| 1 | 4½ — or 5½ after the (a1) election | 4½ — (5)(b) | 4.5 |
| 2 | 4½ | 4½ — (5)(b) | 4.5 |
| 3 | 3½ | 3½ — (5)(b) | 3.5 |
| 4, 5 | 2½ | 2½ — (5)(b) | not printed |
| 6 to 17 | 2 | 1 — (5)(c) | woman 2, man 1 |
| 18 (year of majority) | ½ | 0 — no row | not printed |
| 19 and over | 0 | 0 | — |

Through (4A) a woman married to a widower has the woman's column, without the (a1) election, for each of his children; through (6) a man married to a widow has the man's column for each of hers.
Beside the children's points, (c)(4) gives the woman ½ under s 36A, and (c)(2) gives ½ (not 1) to a spouse whom s 37 would give a point.

## 6. What `check.sh` prints

(0.2.0: this section is version 0.1.0's run, before the independent tests were added; the current table is in the version section at the top.)

Run on 2026-10-06 as `L4=/Users/mengwong/.local/bin/l4 ./check.sh`.
The binary has no `--version`; it resolves to a cabal-store build `jl4-0.1-0ee0100b`, sha256 `64bbcb157dbef2ef1020a6a75589313bba0a2aeeb807c921c5e65e62e9eca118`.
`JL4_LIBRARY_PATH` unset; the embedded standard library was used.

```
module                                    errors satisfied  failed  refused  expected
ito66-a-separate-calculation.l4                0         0       0        0         0
ito66-ab-taxable-income.l4                     0         0       0        0         0
ito66-b-property-income.l4                     0         0       0        0         0
ito66-c-credit-points.l4                       0         0       0        0         0
ito66-d-common-source.l4                       0         0       0        0         0
ito66-fixtures.l4                              0         0       0        0         0
ito66-nouns.l4                                 0         0       0        0         0
ito66-tax-years.l4                             0         3       0        0         0
ito66-tests-ita.l4                             0        23       0        0         0
ito66-tests.l4                                 0       139       0        0         0
TOTAL (10 modules)                             0       165       0        0
```

No assertion is expected to fail; no module is listed in `expected_red`.
"refused 0" counts plain `#ASSERT`s that refused; the 11 `#ASSERT REFUSED` directives that test a refusal (1 in `ito66-tax-years.l4`, 8 in `ito66-tests.l4`, 2 in `ito66-tests-ita.l4`) are among the 165 satisfied.
Every expected value was written from the source text before the rule was run; all passed on their first run, which is evidence that the tests and the code share one reader, not that both are right (section 8).
As a control that the harness can fail, a scratch copy outside this directory asserted three wrong values and a refusal of a value-producing rule: all four were reported as failures.

## 7. Aids consulted, with provenance

Neither is a source of law; both were used only to date the text (A1) and as a second test oracle (`ito66-tests-ita.l4`).
`curl` received a Cloudflare challenge page, so both were fetched in a browser session; the sha256 is of the bytes that session received, and the text was extracted in the page with pdf.js 4.0.379.

| document | URL | retrieved (UTC) | bytes | sha256 |
| --- | --- | --- | --- | --- |
| ITA circular 2024-000012, 3 January 2024, "חוק הגדלת נקודות זיכוי להורים במס הכנסה, התשפ״ג–2023" | https://www.gov.il/BlobFolder/dynamiccollectorresultitem/employers-info-030124/he/IncomeTax_employers-info-030124.pdf | 2026-10-06T13:16:27Z | 134,504 | `88f871fb8677de7aa673b03d8ff5aeeeb2525301c7fcbf81c4ac9183530e7290` |
| ITA circular 2024-001090, 26 March 2024, "חוק סיוע להורים לילדים עד גיל שלוש (תיקוני חקיקה), התשפ״ד-2024" | https://www.gov.il/BlobFolder/dynamiccollectorresultitem/employers-info-260324/he/IncomeTax_employers-info-260324.pdf | 2026-10-06T13:16:55Z | 106,995 | `71cf63a3539ab500df36d9dbaaa2216958178d28bf5faf68c28f0170ecef361a` |

Copies are not deposited (the browser session could not hand the bytes to the file system); re-fetch and compare the sha256.
pdf.js returned the Hebrew with most word spaces dropped (`חוק זה יחולרטרואקטיביתהחלמיום1.1.2024`); the few words quoted from the circulars here and in `ito66-tests-ita.l4` have their spaces restored and are otherwise as extracted.

Every Hebrew string quoted from the Ordinance in the modules, `NOTES.md` and `BRIEF.md` was checked mechanically against the deposited file (templates resolved to their display text, each piece between elisions searched for): all are present, apart from labels such as "(ד)(1)" whose spacing differs and citations assembled from the page header (`ס״ח תשפ״ג, 400` plus the title).
Not fetched: the amending Acts at `fs.knesset.gov.il/24/law/24_lsr_624898.pdf`, `25/law/25_lsr_2301411.pdf`, `25/law/25_lsr_2656507.pdf`, `25/law/25_lsr_4239836.pdf` (geographic block).

## 8. Open questions for a domain expert

1. F1: is the (d) gate on the couple or on the common-source income? It decides whether a couple with a failing common source loses the separate calculation of unrelated salary too.
2. F3: what does the Tax Authority do with equal incomes from personal exertion under (a)(2)?
3. F6 and F14: does s 65's inheritance / bodily-injury exception apply under (a)(3), and does a child's income move with the (a)(2) pool?
4. F7: may a registered spouse's (b) income be joined to anything, or is it always alone?
5. F8 and F18: is (c)(1A) a route for the registered spouse, and does (d) reach it?
6. F9: how are (c)(4)-(6) applied to a same-sex couple in practice?
7. F13: is the children's credit capped at the tax on personal-exertion income, or may the excess be set against tax on other income?
8. F10: which unnamed credit provisions (ss 39A, 39B, 40A-40D, 44, 45, 46) apply to each spouse in a separate calculation?
9. The text before 2024: encoding the earlier vintages needs the amending Acts (ס״ח 3048 and 3184, and earlier), which this run could not fetch.

10. (0.2.0) F19: may a birth-year point elected in 2023 be carried into a 2024 calculation, when the 2023 text is not held? Waits on Meng (BACKLOG IL-24). (0.3.0: ruled by Meng on 2026-10-08, SHRUG: declined by default, the carrying reading kept by name. A domain expert could still say what the Tax Authority does.)

Recommended next step: the independent test pass of the encoding skill (`references/second-pass.md`), in a fresh session given only `BRIEF.md` and the source, then a refuter on the (a)/(b) assembly, where the forks concentrate.
(0.2.0, 02-W1: the independent test pass was done after deposit, commit 240a478, by fid-il-02; its findings are in `INDEPENDENT-FINDINGS.md`, and V-4 and E-4 are dealt with in the version section at the top. The refuter on the (a)/(b) assembly has not been run.)

## 9. Nouns to reconcile at IL-07

Read from the sibling directories on 2026-10-06, read-only; nothing imported.

- **The person.** IL-01 declares `Individual` (`ito-credit-points-nouns.l4`) with `a woman` as a BOOLEAN; this row declares `A spouse` with `sex` IS A `Sex` (`a woman` | `a man`). Same person, two shapes; the constructor `a woman` here and IL-01's field `a woman` will also collide by name if both modules are imported together.
- **Residence.** IL-01 declares `an Israeli resident in the tax year` on `Individual`; this row does not declare residence at all, because s 66 does not test it.
- **The child** (0.2.0, 02-N3). This row's `A child` is now `A child, for section 66`, so it no longer shares a name with row IL-06's.
- **Foreign worker** (0.2.0, 02-R2). IL-01 declares `a foreign worker` on `Individual`; this row now declares `a foreign worker within the meaning of section 48A` on `A spouse`, named apart so the two fields cannot collide, and read only for the ½ under s 36A (A6). IL-07 must pass the same fact to both rows.
- **Income items.** IL-03 declares `An item of income` (`amount`, `from personal exertion` BOOLEAN, …) inside `An individual in a tax year`; this row declares `An item of income from personal exertion` (`kind`, `taxable amount`) and keeps income not from personal exertion as one NUMBER on `A spouse`. Same items, different granularity: this row needs the s 1 paragraph of each item for the (a)(1) pension proviso.
- **The tax year.** IL-03's `An individual in a tax year` and this row's `Spouses in a tax year` both have a field `tax year` (NUMBER); two record fields of one name in one import scope are ambiguous in L4.
- **The credit point and the tax.** The value of a credit point is a GIVEN here; IL-01's `ito-s33a-credit-point.l4` is where it is computed. The tax on income from personal exertion is a GIVEN here; IL-03's s 121 module computes tax, and whether it yields the tax on income from personal exertion alone, the figure (c)(4)-(5) needs, is for IL-07 to check.
- **Pension points** (s 40(a), "נקודת קיצבה"): IL-03 declares `A pension-point amount in a tax year`; this row only records that (c)(3) gives them to the registered spouse alone.

## 10. Semi-cleanroom

Nothing under `/Volumes/transcend/src/Axiom/`, no `rulespec-*`, no Axiom Foundation repository or encoding, no `ENCODING-GAPS.md`, no `.axiom/`, no `tax-benefit-source-map.json`, and no `specs/research/AXIOM-*` was read, searched or fetched.
The one web search was restricted to gov.il, knesset.gov.il and taxes.gov.il and asked for the commencement of the 5784 amending Act.

## Comparison with Axiom's RuleSpec (2026-10-06)

Comparison author lad-il-02 (one Claude session, Opus 5.5), 2026-10-06, working alone, after this encoding and its independent test pass were deposited.
Meng's semi-cleanroom ruling of 2026-10-06 held Axiom's encoding back until ours was deposited, and released it for this row only.
Section 10 describes the encoding run and stays true of it: nothing below informed the modules, and no module was changed.
Each divergence is a finding, not a fix.
Source lines are those of the deposited Hebrew file (sha256 `b87f2cf4…94b81b6`, re-verified).

### What was read

Axiom Foundation `rulespec-il`, a local read-only clone at `/Volumes/transcend/src/Axiom/rulespec-il`, commit `95c6f32c87c75e318631cbd77c14b840bc536c15` (2026-10-03).
`git diff HEAD` on the two §66 files was empty.

| file | read | note |
| --- | --- | --- |
| `il/statutes/income-tax-ordinance/section-66.yaml` | whole, 738 lines | sha256 `823dc4426b84e51fb56c4eff876c9ebbac94c86b225d2dca05537ab571a75cb0`; imports `section-34#tax_credit_points_for_israeli_resident` and `section-36#tax_credit_points_for_travel`, which were not opened |
| `il/statutes/income-tax-ordinance/section-66.test.yaml` | whole, 714 lines, 25 cases | sha256 `96a11abaaea4ee0ef829c3c33ba8c5f92eaa09cb0bc1a4713a9ea4aa62ee3bca` |
| `.axiom/encoding-manifests/il/statutes/income-tax-ordinance/section-66.json` | whole | model `gpt-6-astra`, run `565292ca`, 2026-09-06; its applied sha256 for the YAML is `e77b52bc…`, not the file's, because commit `4bb1177` (2026-09-10) re-quoted proof excerpts afterwards; `git diff 66e45b6 4bb1177` on the YAML touches excerpt lines only |
| `docs/ENCODING-GAPS.md` | lines 101-103 (ITO §66 bullet of `encoder-model-mix`), 314-339 (`section-66-proof-excerpts-quote-the-earlier-corpus-render`), 395-424 (`ito-section-66-what-is-and-is-not-executable`, `…-birth-and-maturity-year-come-from-section-40`, `…-c-4-a1-election-not-applied`), 20-26 (a sentence naming the build that made §66) | the 314-339 entry still describes the excerpts as the glued "21⁄2" spelling, which the YAML no longer has |
| `known-validation-gaps.yaml`, `known-missing-money-atoms.yaml` | whole (10 and 3 lines) | no §66 entry: `validate_failures: {}`, `total_allowed: 0` |
| `data/coverage/tax-benefit-source-map.json` | the one entry naming ITO §66 (`instruments[0].applied_without_a_module[2]`) | the composition quotes s 40's "שנת בגרות" to place a child on §66's ladders |
| `NOTICE`, `LICENSE`, `LICENSE-CODE` | `NOTICE` whole; the other two, their headings | licence, below |
| `git log` of the two §66 files | subjects and dates | — |

**Read outside the list I was given**, recorded so the exposure is on file:
the heading list of `docs/ENCODING-GAPS.md`, used to locate the §66 entries (titles only, including titles of entries on other sections and instruments);
lines 104-106, the ITO §121ב bullet next to the §66 one (encoder process, no figures);
and lines 695-706 (`no-executable-oracle`), opened for its sentence on §66's ladders, which in the same bullets states figures for ss 34, 36, 36A and 121 (rows IL-01 and IL-03).
Nothing below uses those lines except the §66 sentence, cited where used.
The §66 test cases themselves carry s 34 and s 36 expected outputs (2 and 0.25); they are named in the case table and not compared.
Not read: any other section's module or cases, anything under `national-insurance-law-1995/` or `composed/`, the body of the general ENCODING-GAPS entry on `effective_from` (only its title, `effective-from-is-not-commencement`, was seen), any other Axiom repository, and `l4-ide/specs/research/AXIOM-*`.

### Licence

`NOTICE` at that commit: "Encodings, companion test cases, parameter values, and provenance metadata in this repository are licensed under the Creative Commons Attribution 4.0 International license (CC BY 4.0) — see LICENSE", and "Incidental tooling and scripts … are licensed under the Apache License 2.0 — see LICENSE-CODE".
So both §66 YAML files are **CC BY 4.0**; `LICENSE-CODE` (Apache 2.0) does not apply to them.
The keys, values and formula fragments quoted below are short identifying snippets, attributed: *Axiom Foundation RuleSpec corpus (CC BY 4.0), https://github.com/TheAxiomFoundation*.
Nothing of theirs is copied into our modules, which are Apache-2.0 (`encoding.json`).

### Axiom's module, in brief

36 rules (26 parameters, 10 derived), 10 `deferred_outputs` each carrying a reason, 25 companion cases, every case in tax year 2024, every rule `effective_from: '0001-01-01'`.
It executes: the two children's ladders, per child, from caller-supplied birth-year and maturity-year facts; the (a)(3) age test; the (d)(1) conditions; an (a)(1) judgment for one income of one person, including the pension proviso with a computed five-year window; the s 34 and s 36 points in a separate calculation, imported from those sections; and "no ss 38, 39".
It defers, with reasons in the module: (a)(2); the (a)(3) amount; (b); the rest of (c)(1); the application of the ½ points in (c)(2) and (c)(4); (c)(3); the birth-year and maturity-year classification; (a1); and parent totals, (4A), (6) and the set-off against the tax on income from personal exertion.
It omits without recording it: (c)(1A), line 2462 (not in `deferred_outputs`, not in the ENCODING-GAPS §66 entries).

### Divergences

| id | provision | ours | theirs | source lines | classification | proposed repair to ours |
| --- | --- | --- | --- | --- | --- | --- |
| AX-1 | the tax years s 66 answers | refuses before 2024 at three rules; seven couple-level rules answer 2023 (independent finding V-4) | every rule `effective_from: '0001-01-01'`; no case outside 2024; a 2023 period gets the current text | 2454 (amendment list ending תשפ״ג־6, תשפ״ד־3); the text states no commencement | **theirs wrong** for years before 2024, on the ITA circulars, an aid, which print other figures "עד שנת 2023" (`ito66-tests-ita.l4:30-32`; not re-fetched here); the Hebrew text alone does not decide; ours is internally inconsistent (V-4, already recorded) | the V-4 repair: wrap the seven rules in `in tax year … , the answer is`, or name one entry point and call the rest helpers |
| AX-2 | (a)(1) proviso, the five-year window | Boolean input; the edge is the caller's | `qualifying_separate_calculation_years_before_pension_started >= 1 and … <= pension_separate_calculation_lookback_years` (5); case 22 (5) holds, case 23 (6) does not; 0 is the value for "no history" | 2456 "בחמש השנים האחרונות שלפני תחילת תשלום הקיצבה" | **scope difference**: Axiom computes an edge s 66 itself sets, which ours leaves to the caller; at the edge, a genuine ambiguity the text leaves open: it counts back from the start of payment and fixes no whole-year convention, and Axiom's whole-year count cannot express an entitlement earlier in the same tax year as the start | not wrong; recommended (as INDEPENDENT-FINDINGS already does): take the pension's start and the last entitlement as inputs and compute the window, or say in §1 that the caller decides it |
| AX-3 | (d)(1)(b) | two inputs, both required | one input, `each_spouse_shared_income_directly_proportional_to_contribution`, named for the second limb only | 2481 "התואמת את תרומתו … ועומדת ביחס ישיר לתרומתו" | representational: same answer when the caller folds both limbs into the one input; probes show ours fails if either limb fails | none |
| AX-4 | (a)(1), the unit decided and the claim | per spouse: may claim if any item within (a)(1) is above 0; made only if the spouse claims | per person and one income: "available"; no claim input; whether a calculation is made is the input `spouse_tax_is_calculated_separately` | 2456 "רשאי … לתבוע" | representational | none |
| AX-5 | (a)(2) | encoded; a tie of non-zero incomes refuses (F3) | deferred; its reason: "The source supplies no tie-breaker for equal positive personal-exertion incomes" | 2457 | scope; agree on F3's premise | none |
| AX-6 | (a)(3) | the amount, with F5, F6, F14, F15 | only `child_income_attribution_age_condition`: `child_age_attained_in_tax_year < 18`; the amount deferred | 2458 | scope; agree on F15 | none |
| AX-7 | (b) | the routing and the proviso (F7); whether property qualifies is pre-sorted by the caller | deferred; `premarital_property_ownership_years: 1` declared, not applied | 2459 | scope; neither computes "שנה לפני נישואיו" or "בירושה בתקופת נישואיו" | none new; INDEPENDENT-FINDINGS' note stands |
| AX-8 | (c)(1) | names the entitlement per provision; the counts are IL-01's | composes the s 34 and s 36 point counts, 0 when `spouse_tax_is_calculated_separately` is false; ss 35, 45A, 47, 47A, 121A, 10, 11 deferred | 2461 | scope (Axiom composes more) | none |
| AX-9 | (c)(1A) | encoded, F8, F18 | absent, and not recorded as deferred | 2462 | scope, unrecorded on Axiom's side; F18 within it is a genuine ambiguity | none |
| AX-10 | (c)(2) | ½ applied from the s 37 GIVEN; no ss 38, 39 | `favored_individual_separate_calculation_points: 1 / 2`, unapplied; ss 38, 39 `false` (agree) | 2463 | scope | none |
| AX-11 | (c)(3) | the registered spouse only | deferred | 2464 | scope | none |
| AX-12 | (c)(4), ½ under s 36A | 0.5 to the woman | `woman_separate_calculation_additional_points: 1 / 2`, unapplied | 2465 | scope | none |
| AX-13 | (c)(4)(a), (5), the ladders | age = tax year − tax year of birth (A4, s 40(b)(3)) | the band is chosen from caller-supplied `child_is_in_birth_year`, `child_is_in_maturity_year`, `child_is_before_maturity_year`, `child_age_attained_in_tax_year` | 2466, 2474-2476; s 40(b)(3), 1644-1645 | representational; the figures agree at every age 0-19 for both ladders | none |
| AX-14 | (c)(4)(a1) | applied: 1½ in the year of birth, 5½ the next | deferred; the output is named `woman_child_credit_points_before_birth_year_election` | 2467 | scope | none |
| AX-15 | (c)(4A), (6) | encoded (F12) | deferred; the reason glosses them as "children of a deceased spouse", where the text says the widower's and the widow's own children ("ילדיו", "ילדיה") | 2472, 2478 | scope; the gloss is imprecise (documentation only) | none |
| AX-16 | totals per spouse, and the set-off | summed; capped at the tax on income from personal exertion (F13) | deferred | 2465, 2473 | scope | none |
| AX-17 | "האשה", "הגבר" | sex on each spouse; a same-sex couple refuses (F9) | no sex input; both ladders are computed for any person and the caller picks | 2465, 2473 | genuine ambiguity: the text names a woman and a man and does not say more; ours refuses, theirs leaves it to the caller | none |
| AX-18 | labels of the (d) conditions | (d)(1)(a)-(c) | the module cites "§66(d)(1)" correctly, but ENCODING-GAPS line 398 calls them "the §66(א)(1)(א)–(ג) conditions on a shared income source" | 2479-2482 | **theirs wrong**, documentation only | none |
| AX-19 | spent text | stubs for (c)(4)(b)-(d), (5A), (e) | nothing | 2468-2470, 2477, 2484 | scope, cosmetic | none |

**By class:** theirs wrong 2 (AX-1 on the aid, AX-18 in documentation); ours wrong 0 new (AX-1 also carries the already-recorded V-4); genuine ambiguity 1 (AX-17, plus the edge inside AX-2 and F18 inside AX-9); scope 13; representational 3.

### Our forks against Axiom

| fork | Axiom | how |
| --- | --- | --- |
| F1 | silent | `spouses_income_sources_are_dependent` is one couple-named Boolean evaluated beside one income; like ours (DECIDED-ANSWERS D-8), it cannot tie an income to the common source |
| F2 | silent | `income_is_pension` is the caller's |
| F3 | agree on the premise, not executable | the (a)(2) deferral reason quoted at AX-5 |
| F4 | silent | (a)(2) deferred |
| F5 | silent | the (a)(3) amount is deferred; its reason speaks of "the registered spouse to that spouse's children", consistent with F5 |
| F6 | silent | deferred |
| F7 | silent | (b) deferred; its reason mentions "coordination with the same spouse's other separately calculated income" |
| F8 | silent | (1A) absent |
| F9 | silent | no sex input (AX-17) |
| F10 | silent | the named rest of (c)(1) is deferred; unnamed provisions are not mentioned |
| F11 | silent | (a1) deferred; the gap entry (lines 417-424) speaks of "the mother" |
| F12 | silent | (4A), (6) deferred (AX-15) |
| F13 | silent | deferred; the reason names "application against the recipient's personal-exertion income tax" and says neither cap nor ordering |
| F14 | silent | deferred |
| F15 | agree | `< 18` on the age attained in the tax year; case 9 (age 18) `not_holds` |
| F16 | silent | `spouse_tax_is_calculated_separately` is a per-person input |
| F17 | agree, by construction | the ladders take no maintenance or residence input; the parent-child relation is deferred |
| F18 | silent | (1A) absent; Axiom's (a)(1) judgment is `not_holds` for a registered spouse (case 18), which is right for (a)(1) and says nothing about (1A) |

Agree 3 (F3 on the premise, F15, F17 by construction); disagree 0; silent 15.

### Numbers

Axiom states every figure from `effective_from: '0001-01-01'`; ours applies them from tax year 2024 (at the three gated rules; see AX-1).

| figure | line | ours | Axiom |
| --- | --- | --- | --- |
| 5 years, (a)(1) proviso | 2456 | none: a Boolean input | `pension_separate_calculation_lookback_years: 5`, applied as 1..5 |
| 18, (a)(3) | 2458 | `tax year − tax year of birth` < 18 | `child_income_attribution_age_limit: 18`, applied to the caller's age |
| 1 year, (b) | 2459 | none: pre-sorted input | `premarital_property_ownership_years: 1`, unapplied |
| ½ under s 37, (c)(2) | 2463 | 0.5 | `1 / 2`, unapplied |
| ½ under s 36A, (c)(4) | 2465 | 0.5 | `1 / 2`, unapplied |
| the woman: 2½ (birth), 4½ (1-2), 3½ (3), 2½ (4-5), 2 (6 to the year before majority), ½ (majority) | 2466 | same | same, in `woman_child_credit_point_schedule` and again as named parameters |
| one point moved, (a1) | 2467 | applied | `mother_birth_year_deferrable_points: 1`, unapplied |
| the man: 2½, 4½, 3½, 2½, 1, none at majority | 2474-2476 | same | same, in `man_child_credit_point_schedule` and again as named parameters |
| band edges 1, 2, 3, 4, 5, 6 | 2466, 2475-2476 | literals | named parameters (`toddler_credit_band_maximum_age: 2`, …) |
| ss 38, 39 | 2463 | `there is no entitlement` | `false` |

Axiom reports a hand comparison against the OECD TaxBEN description that agrees on "every rung of both §66(ג) child ladders" (ENCODING-GAPS lines 695-703); not verified here.

**A silent hazard in Axiom's module.**
Each child figure is stated twice: as a named parameter (`woman_credit_points_year_turning_three`, formula `3 + 1 / 2`) and as a literal in the indexed schedule (`woman_child_credit_point_schedule`, `2: 3.5`).
The schedule does not reference the named parameters, and the entry at lines 314-339 says the composed pipeline consumes the named `*_credit_points_*` rules.
An amendment entered in one place and not the other would change one consumer's answer with no error.
Our ladders state each figure once.

### Interface

**Ours.** The caller supplies one `Spouses in a tax year`: the tax year; for each spouse, sex, items of income from personal exertion by s 1 kind with the two proviso facts, other income, the two kinds of (b) property income already classified, the two claims, widowhood and the s 37 entitlement; for each child, tax year of birth, parentage, the (a1) election and the four kinds of (a)(3) income; and a MAYBE common source with the six (d) facts.
It gets back, rule by rule: (a)(1) may claim and made; the (a)(2) destination; the (a)(3) amount; the (b) destination; the assembled taxable income of each calculation; (c)'s entitlement per provision; (c)'s credit points per spouse; and the capped children's credit, given the value of a point and the tax as GIVENs.

**Axiom.** The caller supplies flat facts for one person and one tax-year period: four facts classifying one child; the five (d) facts; whether the person is the non-registered spouse; whether one income is personal-exertion income of the kinds (a)(1) names; whether it is a pension; limb 1 as a Boolean; limb 2 as a whole number of years; whether the spouses' sources are dependent; whether the person's tax is calculated separately; and residence for ss 34 and 36.
It gets back ten outputs: two band indices, the woman's and the man's points for that child before the election, the (a)(3) age condition, the (d) conditions, the (a)(1) judgment, the s 34 and s 36 points in a separate calculation, and the ss 38-39 judgment.

**On the two conditions our tester found we take as inputs:** Axiom computes the (a)(1) five-year window itself, from a whole-year count (AX-2); it does not compute the (b) property conditions either, since (b) is deferred and its one-year parameter is unapplied (AX-7).

### The independent-test findings, in Axiom

**V-4, tax year 2023 answered instead of refused.**
Axiom has no year gate: every rule is `effective_from: '0001-01-01'`, so a 2023 period, or a 1990 one, is answered by the current text in all ten outputs.
What our tester classified as our error in seven rules is Axiom's behaviour throughout.
For the children's ladders the circulars, as transcribed in `ito66-tests-ita.l4:30-32`, print other figures "עד שנת 2023", so Axiom's 2023 ladder answers are the 2024 figures.
A probe on the scratch copy repeats V-4 unchanged: our per-child rule `s 66(c)(4)-(6) — the credit points of the … for` answers 2.5 for a 2023 couple with a child born 2023, while `s 66(c) — the credit points it gives the` refuses.

**E-4, a birth-year point moved out of 2023 into 2024.**
Axiom does not apply (a1) at all (AX-14), and ENCODING-GAPS lines 422-423 say its composed pipeline "allots the birth-year points in the birth year".
For a 2024 calculation of a child born in 2023 it gives 4½, neither refusing nor adding the point; it is silent on the fork and is evidence for neither reading.

### Axiom's 25 cases, run through this encoding

Each case's inputs were mapped onto our interface in a scratch module, `tests-axiom-cases.l4`, in a copy of this directory in the comparison session's scratchpad (not deposited), with every expected output asserted as Axiom states it.
Mapping: the person is the non-registered woman of a 2024 couple with a salaried registered man; a child turning *n* is a child of both born in 2024 − *n*; Axiom's single (d)(1)(b) input is given to both of our limbs; `spouses_income_sources_are_dependent: false` is `common source of income` = NOTHING; the band indices have no counterpart, so the points they select are compared instead.
`l4 run` (`/Users/mengwong/.local/bin/l4`, `JL4_LIBRARY_PATH` unset): 0 errors, **47 of 47 assertions satisfied**, counted as `check.sh` counts (the raw output logs each satisfied assertion twice, 94 lines).
A control copy asserting four wrong values reported four failures.
`check.sh` over the scratch copy also reproduced the deposited figures for every other module (`tests-independent.l4`: 101 satisfied, 2 failed).

| # | case | Axiom expects | result |
| --- | --- | --- | --- |
| 1 | `birth_year_selects_zero_band_and_mixed_number_points` | woman 2.5, man 2.5, (a)(3) age test holds (bands 0, 0) | match |
| 2 | `year_after_birth` | 4.5, 4.5 | match |
| 3 | `year_turning_two` | 4.5, 4.5 | match |
| 4 | `year_turning_three` | 3.5, 3.5 | match |
| 5 | `year_turning_four` | 2.5, 2.5 | match |
| 6 | `year_turning_five` | 2.5, 2.5 | match |
| 7 | `ladders_diverge_when_child_turns_six` | woman 2, man 1 | match |
| 8 | `child_below_attribution_age_limit` | age 17: age test holds; 2, 1 | match |
| 9 | `externally_classified_maturity_year` | age 18: woman 0.5, man 0, age test fails | match |
| 10 | `after_final_bounded_child_credit_row` | age 19: 0, 0 | match |
| 11 | `all_shared_source_conditions_satisfied` | (d) conditions hold; (a)(1) holds; s 34 points 2; s 36 points 0.25; ss 38, 39 not allowed | match on 3 of 5 outputs; the s 34 and s 36 counts not run (IL-01's) |
| 12 | `required_personal_exertion_missing` | (d) fails; (a)(1) fails | match |
| 13 | `shared_income_not_proportional_to_contribution` | (d) fails; (a)(1) fails | match |
| 14 | `home_not_regularly_used_for_shared_source` | (d) fails; (a)(1) fails | match |
| 15 | `most_activity_not_at_home` | (d) fails; (a)(1) fails | match |
| 16 | `home_qualifications_do_not_apply_to_income_produced_elsewhere` | (d) holds; (a)(1) holds | match |
| 17 | `independent_sources_do_not_require_shared_source_contribution_test` | (d) conditions fail, but no dependency: (a)(1) holds | match |
| 18 | `nonregistered_spouse_condition_missing` | (a)(1) fails for the registered spouse | match on (a)(1); a probe shows ours lets the same spouse request under (c)(1A) (F18), which Axiom does not encode |
| 19 | `income_outside_personal_exertion_categories` | (a)(1) fails | match |
| 20 | `pension_without_either_qualifying_history` | (a)(1) fails | match |
| 21 | `pension_based_on_qualifying_employment` | (a)(1) holds | match |
| 22 | `pension_history_in_fifth_preceding_year` (5) | (a)(1) holds | match, with limb 2 set TRUE by hand: ours does not compute the window (AX-2) |
| 23 | `pension_history_outside_five_preceding_years` (6) | (a)(1) fails | match, with limb 2 set FALSE by hand (AX-2) |
| 24 | `separate_calculation_credit_outputs_inoperative_without_separate_calculation` | s 34 and s 36 points 0 | not run: the counts are IL-01's |
| 25 | `imported_residence_conditions_remain_required` | s 34 and s 36 points 0 for a non-resident | not run: the counts and residence are not in this row |

**Matched 20; matched with the window supplied by hand 2; matched in part 1; diverged 0; could not be run 2.**

### What each covers that the other does not

**Axiom, not ours:** the (a)(1) five-year window, computed; the s 34 and s 36 point counts composed into the separate calculation; a proof atom quoting the Hebrew for each figure; each deferral recorded with its reason inside the module.

**Ours, not Axiom:** (a)(2), with the tie refused; the (a)(3) amount; (b) and its proviso; the assembled taxable income of each calculation; (c)(1A); the application of (c)(2), (c)(3) and the ½ under s 36A; (a1); (4A) and (6); per-spouse totals and the cap against the tax on income from personal exertion; refusals where the text is silent (pre-2024 years, the tie, a same-sex couple, an unnamed provision); stubs for the spent text; the ITA circular tests; and an independent test pass.

### Bottom line

On every value both encodings compute, they agree: both ladders at every age, the (a)(3) age test, the (d) conditions, the (a)(1) judgment with its pension proviso, and the exclusion of ss 38 and 39.
None of Axiom's 25 cases diverges from ours; 2 rest on the five-year window, which ours takes as given, and 3 test s 34 and s 36 counts this row does not hold.
Axiom's module is narrower than ours: it defers most of (a)(2), (a)(3), (b) and (c), and omits (c)(1A) without saying so.
It is broader in two places: it computes the five-year window and composes the s 34 and s 36 points.
The one substantive disagreement is the tax year: Axiom answers every year with the current text, which the ITA circulars contradict for the children's figures before 2024; ours refuses at three rules and, per V-4, not at seven.
This comparison found nothing in our encoding that Axiom shows to be wrong.
The agreement is evidence about the ladders and the gates, not about the forks: Axiom is silent on 15 of F1-F18 and contradicts none.
