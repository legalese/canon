# NOTES — il/national-insurance-law-consolidated-version-5755-1995, encoding row `legalese-2026-10-il-06`

National Insurance Law [Consolidated Version], 5755-1995, **ss 66, 67 and 68** (the child allowance: the right to it, the count of children, the amount), with **s 65** and the parts of **s 1** they read, encoded in L4 by one agent in one session (run `IL-06-20261006`, 2026-10-06), from the brief in `BRIEF.md`.
Status: **draft, version 0.2.0** (repairs of 2026-10-08, BACKLOG IL-18; the section below).
An independent test pass was run on 2026-10-06 (`INDEPENDENT-FINDINGS.md`); after 0.2.0 its five remaining failures are recorded forks that wait on rulings.
No domain expert has read it against the source; HG1 has not been sought.

## Version 0.2.0 (2026-10-08): repairs (BACKLOG IL-18)

Made by `rep-il-18` from the repair brief of 2026-10-08 and the inventory `l4-pipeline/findings/il-2026-10-08/inventory.tsv`.
One answer moves (06-F5); one question is added (06-S72); the rest is forks recorded, tests labelled, `check.sh` and wording.
Changed: `nii-il06-nouns.l4`, `nii-s65-interpretation.l4`, `nii-s67-count-of-children.l4`, `nii-s68-amount.l4`, `nii-il06-family-on-a-day.l4`, `nii-il06-tests.l4`, `check.sh`, `encoding.json` and this file (the lead widened the file list to s 65, s 67 and s 68 on 2026-10-08).
No expected value of an existing assertion changed, in either test module.

### Items

- **06-F5, a finished absence (`INDEPENDENT-FINDINGS.md`, finding 5).**
  A child's `absence from Israel` is the absence in progress on the day, but an absence that had ended before the day was accepted and measured, so a child who had come back was treated as abroad (total 0) with no diagnostic.
  `A problem with the facts` gains `an absence from Israel ended before the day`, and the family's answer returns it as a LEFT, as it already did for an absence that begins after the day.
  The return day itself is not "before the day": an absence that ends on the day asked about is in progress on it, as the code has always read it (fork F3, now stated; assumed, not ruled).
  The check is in `nii-il06-family-on-a-day.l4`, where the checks shared by the day and the month questions now sit in one rule, `the first problem with the facts of … , the check on births being …`; the day question's `a problem with the facts of` is unchanged in name, type and order of checks.
  Rejecting rather than treating the absence as none was chosen because the validator already rejects an absence that begins after the day; both keep the field meaning "in progress on the day".
- **06-S72, this row's half (IL-07 `RECONCILE.md` section 3; IL-07 independent finding F3).**
  s 72(a) (line 854) pays the allowance to the last day of the month in which entitlement ceased, so a child who turns 18 on the 1st of a month is paid for that month; this row answered a day, and on every day of that month the child is 18.
  A second question now answers a **month**, for the children the caller says s 72 pays for in it (row IL-08 encodes s 72; this row still does not).
  It takes a new record, `A family in a month`, and changes exactly one thing against the day question: s 65's age limb, and the need to be born by the day, are met for the month by a listed child whose 18th birthday is on or after the month's first day and who is born by its last day.
  A listed child outside that is a problem with the facts (two new constructors), not a child silently left out.
  Every other fact is as on a day of the month the record names.
  There is no second composition: the rules of ss 65-68 that take a family on a day (s 65's "child"; s 67's answer, in whose count, with the count and s 67(a); s 68's answer for a person; the family's answer and its check of the facts) are now asked a question, a new enumeration `The question asked of a family on a day` (`the allowance on the family's day`, or `the allowance for the month of the family's day, for the children section 72 pays for in it`), and the month is put as a family on its day.
  Only s 65's age limb and the fourth check on the facts consult the question; every other rule answers both alike, so the day and the month cannot drift apart.
  The day's forms keep their names and types as thin wrappers, and the month's forms sit beside them in the same modules (the lead's preference, 2026-10-08, over a first draft that restated the composition in `nii-il06-family-on-a-day.l4`).
  The lines of `nii-s67-count-of-children.l4` and `nii-s68-amount.l4` that this file's Axiom comparison cites (s 67: 169, 223-227; s 68: 43-49, 156-159) and the s 65 lines the inventory cites (40-44) hold the same rules on the same lines; the new code is at the end of each module.
  The count for the month is the listed children placed with the parent, eldest first; a child paid for in the month of its 18th birthday keeps its place and counts for s 68(c)'s "three or more" (fork F19, new; assumed, not ruled).
  The day question is unchanged, and the tests assert that the two agree where every listed child is born and under 18 on the record's day.
  The guard against drift between the two questions is `nii-il06-tests.l4` lines 695-696, which assert that the month answer equals the day answer (173, 219, 219, 219, 173, 173; 1176) where both answer; since the first draft's restated s 67/s 68 composition was replaced by one composition asked a question, there is no second copy for them to guard, and they guard the month's age limb and check on births instead.
- **06-HW, a resident s 238 housewife under s 65(a) "מבוטח" limb (2) (`INDEPENDENT-FINDINGS.md`, finding 4).**
  Recorded as fork **F18**, with both readings and who holds each; the current reading (A) is kept as the default until Meng rules (BACKLOG IL-24).
  Every test of the encoder's that rests on reading (A) is labelled: `nii-il06-tests.l4` lines 379 ("Batya"), 415, 444 and 465, and the `a housewife` fixture (lines 89-95).
  `nii-s65-interpretation.l4` is not changed.
- **DATE, 29 February and other days a later month lacks (`INDEPENDENT-FINDINGS.md`, finding 2).**
  Fork F2's row now names its three readings and who holds each; the clamp is kept as the default until Meng rules (BACKLOG IL-24).
  The tests that rest on it are labelled (lines 391-392, 403-404), and the month question's two tests of a 29 February birthday (lines 702-703) show the clamp reaching s 72.
- **CHK-06.** `check.sh` now declares the tester's five remaining failures (lines 594, 608, 613, 615, 619: 06-F7, DATE, 06-F3 twice, 06-HW), each named in a comment, and gains `expected_refused` as row IL-04's has (0 for every module).
  It exits 0.
- **06-W1.** Assumption A3 and the answer table no longer say that every day from 1 January 2027 is declined: it is declined wherever an amount is needed.
- **06-W2.** Axiom's readings under F7 and F9-F11 are recorded in the fork register and open questions 2 and 3; section 9's "the independent test pass was not run" is marked stale.
- **06-W3.** Section 6 and fork F5 record that the s 66 additional-tax input is joined to row IL-03's s 121B at IL-07, and how (IL-07 `RECONCILE.md` N12, its fork K5).
- **02-N3 and 03-N4 (this row's halves): resolved from the other side; IL-06 keeps its names.**
  The lead ruled on 2026-10-08 that IL-06 does not rename: row IL-02 renames its `A child` to `A child, for section 66` (job IL-15) and row IL-03 renames its `A problem with the facts` to `A problem with the facts, for sections 121 and 121B` (job IL-16), so each clash (IL-07 `RECONCILE.md` N3, N4) is gone without touching IL-06's names.
  Renaming here would also have meant 30 edits to the tester's `tests-independent.l4`; none was made.

### Assertions added (none changed)

All 39 in `nii-il06-tests.l4`; every value worked from the source before the run.
2026 amounts are [nii-basic]'s: (2)(a) 173, (2)(b) 219, (2)(c) 162, so the s 68(c) supplement is 70% × 162 = 113.4.

| line(s) | scenario | old | new | why |
| --- | --- | --- | --- | --- |
| 606 | Noa away 10 Jan-10 Jun 2026, asked 1 Sep 2026 | — (0.1.0 gave total 0) | `LEFT an absence from Israel ended before the day` | 06-F5; line 807 and the noun's contract |
| 607 | the same, asked 11 Jun 2026 | — | the same LEFT | 06-F5 |
| 611-612 | the same, asked 10 Jun 2026, the return day | — | not in Israel; total 0 | F3: the return day is a day of the absence (more than three months: 10 Jan to 10 Jun, the three months ending 10 Apr) |
| 647-648 | Keren, 18 on 1 Nov 2026, alone, month November | — | 173; total 173 | 06-S72: line 854, entitlement ceased in November, paid to its last day; first child, (2)(a) |
| 650 | the same, as at 30 Nov | — | 173 | any day names the month |
| 653 | the day question, 1 Nov | — | 0 | Keren is 18 on the day (line 807): the day answer is unchanged |
| 658-660 | Keren, Gil, Hila, November | — | Keren, Gil, Hila; 173, 219, 219; 611 | F19: eldest first, places 1-3 |
| 661 | the day question, 1 Nov | — | 392 (Gil 173, Hila 219) | the day answer counts two |
| 663 | Gil, Hila, December | — | 392 | s 72 no longer pays for Keren |
| 665 | Keren listed for December | — | `LEFT … reached 18 before the month began` | her entitlement ceased in November |
| 672-673 | Avi paid Income Support; Keren, Gil, Hila, Ido; November | — | supplements 0, 0, 113.4, 113.4; total 830 + 226.8 = 1056.8 | F19 and line 826, on the month's count of four |
| 674 | the day question, 1 Nov | — | 173 + 219 + 219 + 113.4 = 724.4 | three children; the supplement for the third only |
| 678-679 | Ella, Gil, Gal (born 10 Sep 2026), September, as at 1 Sep | — | 173, 219, 219; 611 | line 854: born by the 15th, paid from the 1st |
| 681 | Gal born 2 Oct, listed for September | — | `LEFT … born after the month` | no reading of s 72 pays a month before the birth |
| 688-690 | Tal (18 on 10 Sep 2026), Gil, Hila, Gal (born 12 Sep 2026), September | — | Tal, Gil, Hila, Gal; 173 + 219 × 3 = 830; s 67(a) holds | F19; no day of September counts all four |
| 695-696 | the six children, June 2026, as at 15 June and 1 June | — | 173, 219, 219, 219, 173, 173; 1176 | the month question agrees with the day question (line 493) |
| 702 | born 29 Feb 2008, February 2026 | — | 173 | paid on every reading of F2 |
| 703 | the same, March 2026 | — | `LEFT … reached 18 before the month began` | F2 reading (i): 18 on 28 February |
| 707 | the eldest two, April 2015 | — | refused (the period) | A1 |
| 708 | the eldest two, May 2015, as at 20 May | — | 150, 188 | [nii-basic] from 1 May 2015 |
| 709 | the eldest two, January 2027 | — | refused (no published figures) | A3 |
| 713-716 | the month's age limb alone | — | Keren in November TRUE, December FALSE; Gal (born 12 Sep 2026) in September TRUE, August FALSE | line 854 with line 807 |
| 723-727 | Keren, Gil, Hila, November 2026, through the month's forms in s 65, s 67 and s 68 | — | Keren a child for the month (TRUE) but not on 1 November (FALSE); in Avi's count (`JUST "Avi"`); Avi's count Keren, Gil, Hila; Batya's allowance with no lines | the same reading as lines 658-660, asked rule by rule |

The independent tester's file is unchanged.
Its assertion X2 (line 638, finding 5) now passes: the answer is a rejected fact, which its expectation allows.

### What changed in the interface (for job IL-22, the capstone)

New in `nii-il06-nouns.l4`, after every existing declaration so that the lines `RECONCILE.md` cites (88, 123, 188) still hold:

```
DECLARE `A family in a month` HAS                                                    -- line 225
    `a day in the month, on which the facts stand`     IS A DATE
    `the persons`                                      IS A LIST OF `A person`
    `the children section 72 pays for in the month`    IS A LIST OF `A child`

DECLARE `The question asked of a family on a day` IS ONE OF                          -- line 235
    `the allowance on the family's day`
    `the allowance for the month of the family's day, for the children section 72 pays for in it`
```

New constructors of `A problem with the facts`: `an absence from Israel ended before the day`, `a child said to be paid for in the month is born after the month`, `a child said to be paid for in the month reached 18 before the month began`.

**Entry points for a month** (each takes `A family in a month`):

- `nii-il06-family-on-a-day.l4`: `the child allowance of each person for the month, for the children section 72 pays for, at the basic amounts the Institute published for the month, in` …, the one the capstone needs (the counterpart of the day question at published amounts); and `the child allowance of each person for the month, for the children section 72 pays for, in` … `, at` …, at amounts the caller gives.
- `nii-s68-amount.l4`: `s 68 — the child allowance for the month, in` … `, at` … `, of` ….
- `nii-s67-count-of-children.l4`: `s 67 — the insured parent in whose count, for the month, in` … `, is` …; `s 67 — the count of children, for the month, in` … `, of` …; `s 67(a) — no child is counted with more than one insured parent, for the month, in` ….
- `nii-s65-interpretation.l4`: `s 65 — a child for this Chapter, for the month section 72 pays, in` … `:` …; `s 65, read with s 72(a) — not 18 before the month of` … `began, and born by its end:` …; `the family in a month, on its day:` …; `the first day of the month of` …; `the last day of the month of` ….

**Rules asked of a question** (the forms both questions share; each day's form calls one with `the allowance on the family's day`):
`s 65 — a child for this Chapter, asked` … `, in` … `:` …; `s 65 — the age limb, asked` … `, on` … `:` …; `s 67 — the insured parent in whose count, asked` … `, in` … `, is` …; `s 67(a) — no child is counted with more than one insured parent, asked` … `, in` …; `s 67 — the count of children, asked` … `, in` … `, of` …; `s 68 — the child allowance, asked` … `, in` … `, at` … `, of` …; `the child allowance of each person, asked` … `, in` … `, at` …; `a problem with the facts, asked` … `, of` …; and `the first problem with the facts of` … `, the check on births being` … (the three checks both questions make first).

**Nothing was renamed.** Every rule a caller used before 0.2.0 keeps its name and type: the day's forms are now one-line wrappers.
The capstone's IL-06 adapter calls the day answer at published amounts, `the family's total, before rounding, of`, `s 67 — the count of children, in`, `s 66 — an insured parent with income chargeable to additional tax`, `s 65 — under 18 on`, `the 18th anniversary of the birth of` and the published figures; all keep their names and types, so it needs no change once the five changed modules (nouns, s 65, s 67, s 68, family-on-a-day) are re-vendored together.

**For the capstone (IL-22):** build `A family in a month` with the first day of the month (or any day of it), the two persons, and the children IL-08's s 72 pays for, and call the published-amounts month entry point.
K15's choice of a day and its decline for "no day of the month counts them all" (`il07-pipeline.l4`, the rule `IL-07: the child allowance for the month, in`) are then no longer needed.
By this row's arithmetic, the declined months should then be answered: H44n (one child, 18 on 1 November 2026) 173; N21's November (Keren and two younger children) 611; N22 (four children, one of them 18 on 10 September and one born on 12 September) 830. The capstone has to verify these values against its own households.
The capstone's `IL-06: the refusal for` has an `OTHERWISE` arm, so the three new constructors reach it as its general refusal unless it names them.

### `check.sh` after the repairs

Run on 2026-10-08, 07:10:46Z to 07:11:08Z, in place with `L4=/Users/mengwong/.local/bin/l4 ./check.sh`, `JL4_LIBRARY_PATH` unset.
Binary `~/.cabal/bin/l4` -> cabal store `jl4-0.1-d4290e25`, sha256 `f4f2bd2558f02f828f0deced5f74313a33670f08cc3275ff95b83f2cde71e448`, the same before and after the run.

```
module                                    errors satisfied  failed  refused  expected
nii-il06-family-on-a-day.l4                    0         0       0        0         0
nii-il06-nouns.l4                              0         0       0        0         0
nii-il06-period.l4                             0         0       0        0         0
nii-il06-published-figures.l4                  0         0       0        0         0
nii-il06-tests.l4                              0       156       0        0         0
nii-s1-basic-amount.l4                         0         0       0        0         0
nii-s65-interpretation.l4                      0         0       0        0         0
nii-s66-entitlement.l4                         0         0       0        0         0
nii-s67-count-of-children.l4                   0         0       0        0         0
nii-s68-amount.l4                              0         0       0        0         0
tests-independent.l4                           5       141       5        0         5
TOTAL (11 modules)                             5       297       5        0
```

`check.sh` exit 0.
Before the repairs, on the same binary: `nii-il06-tests.l4` 117 satisfied; `tests-independent.l4` 6 errors, 140 satisfied, 6 failed, 0 refused, against 0 expected, so exit 1.
`tools/srcquote.py` regenerates every module byte-identical, and `tools/hebcheck.py` passes on the six changed modules and on this file.

## 0. What `check.sh` prints

(0.2.0) This is version 0.1.0's run, kept; 0.2.0's is at the end of the section "Version 0.2.0" above.

Run on 2026-10-06 with `/Users/mengwong/.local/bin/l4`, `JL4_LIBRARY_PATH` unset.
That path is a symlink to `~/.cabal/bin/l4`, which resolves to cabal store entry `jl4-0.1-0ee0100b`, sha256 `64bbcb157dbef2ef1020a6a75589313bba0a2aeeb807c921c5e65e62e9eca118`.
The binary has no `--version`, and no record beside it names the commit it was built from.

```
module                                    errors satisfied  failed  refused  expected
nii-il06-family-on-a-day.l4                    0         0       0        0         0
nii-il06-nouns.l4                              0         0       0        0         0
nii-il06-period.l4                             0         0       0        0         0
nii-il06-published-figures.l4                  0         0       0        0         0
nii-il06-tests.l4                              0       117       0        0         0
nii-s1-basic-amount.l4                         0         0       0        0         0
nii-s65-interpretation.l4                      0         0       0        0         0
nii-s66-entitlement.l4                         0         0       0        0         0
nii-s67-count-of-children.l4                   0         0       0        0         0
nii-s68-amount.l4                              0         0       0        0         0
TOTAL (10 modules)                             0       117       0        0
```

`check.sh` exit 0.
The tests module has 117 `#ASSERT` directives, of which 11 are `#ASSERT REFUSED`; all 117 are satisfied, and no failure or refusal is expected.
(`l4 run` prints each result twice, so a raw grep finds 234 `assertion satisfied` lines; `check.sh` counts only the diagnostic half.)
The rule modules carry no assertions of their own.
The tests module takes about 40 seconds to run: every child's count is recomputed for every person who is asked about.

To show the harness can fail, a scratch copy of the tests with four planted defects (three expected values altered, one assertion pointed at a day before 1 May 2015) reported 113 satisfied, 3 failed, 1 refused.
Every run also prints two Warnings that differing copies of `prelude` and `daydate` exist under `~/.local/share/jl4/libraries/`; the binary uses its embedded copies, and the warnings are not errors.

Mechanical checks over every file, with the scripts in `tools/` (run them with `python3 -I`):
`tools/srcquote.py SOURCE FILE.l4…` regenerates every `-- src:N | …` comment from line N of the source file (regenerating left all ten modules byte-identical); `tools/hebcheck.py SOURCE FILE…` checks that every other run of Hebrew in the modules and the Markdown files occurs verbatim in the source.
Both pass.
Both scripts are copied from row IL-03; `hebcheck.py` has one change, stated in its header: it also skips lines tagged `-- ext:[TAG] |`, which quote a source other than the Law.
Those quotations were checked separately (section 7).

## 1. What is encoded and what is not

**Encoded:** s 66 in full; s 67(a) and (b) in full for the shapes of family the text describes, with a named refusal for each shape it does not; s 68(a), (b)(2), (b)(3) and (c) in full.
The definitions they read are encoded as far as they need: s 65(a) "מבוטח" (insured, both limbs), s 65(a) "ילד" (child, both limbs and the proviso), s 65(b) (a child out of Israel), s 1 "ילד" (stepchild, adopted child, married minors), and s 1 "הסכום הבסיסי" paragraph (2)(a)-(c) (which basic amount fixes the allowance for a child at each place in the count).

**Not encoded:** s 1's updating clause for the basic amount (row IL-04's s 1); s 69 (to whom paid), s 69A (several women), s 71 (a parent who died or ceased to be insured), s 72 (which months are paid; (0.2.0) its answer for a month is taken from the caller by the month question), s 238 ("housewife"), s 381 and the rounding regulations; the Income Tax Ordinance s 121B (row IL-03); the Income Support Law; the Maintenance (Assurance of Payment) Law; the Family Allowance Regulations under s 65.
Each of these that feeds a provision in scope enters as an **input**, with its citation in the nouns module; s 69A and s 71, which displace or decide cases this row would otherwise answer, are **named refusals** consulted before s 67 answers.

**The figures.** The text prints the basic amounts only as their 2015 base (150, 188, 140).
The amounts in force on a day are an input to the rules; the National Insurance Institute's published table of them, 1 May 2015 to 2026, is a separate module (`nii-il06-published-figures.l4`) that says on its face it is not encoded law.
Figures that appear only in the consolidation's editorial notes are not encoded.

**The question answered.** For a family on a day: which persons are insured, which children are "children", in whose count each child is, and each person's monthly allowance and s 68(c) supplement at the basic amounts in force that day, **before rounding**.

**(0.2.0) A second question.** For a family in a month: the same answer for each person, for the children the caller says s 72 pays for in the month, with s 65's age limb met for the month by a child whose 18th birthday is on or after the month's first day and who is born by its last (section "Version 0.2.0", 06-S72; fork F19).

## 2. Coverage table

Line numbers are lines of `../../registers/source-bundle/national-insurance-law-consolidated-version-5755-1995.he.wiki.txt`.
Totals: **26 encoded, 4 inert, 10 out-of-scope, 0 deferred** (40 rows).

| provision | line | gist | disposition | where |
| --- | --- | --- | --- | --- |
| s 65(a) chapeau | 800 | "in this Chapter" | encoded | scope of `nii-s65-interpretation.l4` (Chapter 4 only) |
| s 65(a) "מבוטח" (1) | 801-802 | insured under Chapter 11, except a s 238 housewife | encoded | `s 65 "insured" (1) — …` |
| s 65(a) "מבוטח" (2) | 803 | resident individual, not absent beyond a reasonable temporary absence, not insured under Chapter 11, except a s 238 housewife | encoded | `s 65 "insured" (2) — …`, `s 65 — insured` |
| s 65(a) "ילד" (1) | 804-805 | the child of an insured or formerly insured person | encoded | `s 65 "child" (1) — …`, `s 65 — one who was insured` |
| s 65(a) "ילד" (2) | 806 | a child the insured supported, as proven | encoded | `s 65 "child" (2) — …` |
| s 65(a) "ילד" proviso | 807 | in Israel and under 18; "father", "mother", "parent" construed accordingly | encoded | `s 65 — in Israel on`, `s 65 — under 18 on`, `s 65 — a parent for this Chapter, …` |
| s 65(a) note | 808 | Family Allowance Regulations 5720-1960 published | inert | comment; the regulations' period for (2) is not in the sources, and the proof under (2) is an input |
| s 65(b) | 809 | out of Israel for no more than three months is not abroad; the Institute may deem otherwise | encoded | `s 65(b) — the absence, as at …`, `s 65 — in Israel on` |
| s 66 | 813-814 | insured parent entitled for each child, except one with income chargeable to additional tax | encoded | `s 66 — entitled …`, `s 66 — an insured parent with income chargeable to additional tax` |
| s 67(a) | 817 | one count only | encoded (by construction, and as a rule the family answer consults) | `s 67(a) — no child is counted with more than one insured parent, in` |
| s 67(b) first limb | 818 | two parents: the insured father, unless the child is with the mother only | encoded | `s 67(b), first limb — …` |
| s 67(b) second limb | 818 | a natural parent and another parent, both insured: the one the child is with | encoded | `s 67(b), second limb — …` |
| s 67(b), the cases it does not answer | 818 | two parents of one sex; natural and other parent with both or neither; neither limb; three or more | encoded (as four named refusals) | `section 67(b) does not say …` |
| s 67, order of the count | — | "the first child", "the fourth child" (used by s 68 and s 1) | encoded (assumption, fork F4) | `s 67 — the count of children, in` |
| s 68 chapeau | 820 | the amount of the allowance | encoded | `nii-s68-amount.l4` |
| s 68(a) | 821 | the basic amount fixed for the child | encoded | `s 68 — the provision that fixes …`, `s 68 — the monthly allowance, before rounding, under` |
| s 68(b) chapeau | 822 | children born before 1 June 2003, fourth and later | encoded | `born before 1 June 2003:` |
| s 68(b)(1) | 823 | (deleted) | inert | comment |
| s 68(b)(2) | 824 | fourth child: (2)(a) amount × 2.24 | encoded | `section 68(b)(2), …` |
| s 68(b)(3) | 825 | fifth and later: (2)(a) amount × 2.36 | encoded | `section 68(b)(3), …` |
| s 68(c) | 826 | Income Support or maintenance payment, three or more children: 70% of (2)(c) for the third and the fourth | encoded | `s 68(c) applies to …`, `s 68(c) — the supplement, …` |
| s 68(d)-(יא) | 827-834 | (repealed) | inert | comment |
| s 68, a person's allowance | 813-826 | ss 66-68 composed for one person | encoded | `s 68 — the child allowance, in … of` |
| s 1 "ילד" | 170 | includes a stepchild and an adopted child; excludes a married boy or girl | encoded (as s 65 reads it, fork F1) | `the child is the person's child`, `s 1 — not a married boy or girl` |
| s 1 "הסכום הבסיסי" (2) chapeau | 186 | for the child allowance under Chapter 4 Mark B | encoded | `nii-s1-basic-amount.l4` |
| s 1 "הסכום הבסיסי" (2)(a) | 187 | first and fifth and later child: 150 | encoded | `paragraph (2)(a) fixes …`, `the amount printed in paragraph (2)(a)` |
| s 1 "הסכום הבסיסי" (2)(b) | 188 | second, third and fourth: 188 | encoded | same, and `the amount printed in paragraph (2)(b)` |
| s 1 "הסכום הבסיסי" (2)(c) | 189 | Income Support Law benefit or s 68(c) supplement: 140 | encoded (the s 68(c) use) | `the basic amount for a supplement under section 68(c), under` |
| s 1 "הסכום הבסיסי", the base figures | 187-189 | 150, 188, 140 | encoded (as the printed base; not used as the figure in force) | `the basic amounts printed in paragraph (2)` |
| s 1 "המוסד", "המינהלה" | 123, 125 | the Institute; its Administration | inert | used only to name whose determinations are inputs |
| s 1 "הסכום הבסיסי", updating clause chapeau and (3) | 192, 197 | child-allowance amounts updated each 1 January from 2015 by the index; not on 1 January 2025 | out-of-scope | s 1 is row IL-04's, and the update needs index readings this row does not hold; the Institute's published result is used instead, in a module marked not-law. Touched to say so, and to check that the 2025 row equals 2024's. |
| s 1 "הסכום הבסיסי" (1), (2א), (3); updating (1), (2), (4) | 176-185, 190-191, 193-196, 198-202 | basic amounts and updates for other benefits | out-of-scope | not read by ss 65-68; row IL-04 (s 1) and the benefit rows |
| s 69 | 836-840 | to whom the allowance is paid | out-of-scope | it says who receives the payment, not whether or how much; no rule here reaches it. Its default, payment to the mother, differs from s 67's count, which goes with the father: a reader should not take the count for the payee. |
| s 69A | 842-845 | an insured man with children by more than one woman | out-of-scope (declined by name where reached) | it applies "notwithstanding anything elsewhere in this Mark" and recasts the count; encoding it needs each woman's count and a proof by the mother, which are a unit of their own |
| s 71 | 850-851 | a parent who died or ceased to be insured | out-of-scope (declined by name where reached) | it pays "by virtue of" a parent who is no longer an insured parent, which this row's per-person answer cannot express |
| s 72 | 853-856 | the months for which the allowance is paid; seven days alive; three months after death | out-of-scope | this row answers a day; mapping days to paid months is s 72's job, and a reader asking about a month must apply it. (0.2.0) Still not encoded (row IL-08 encodes it), but the month question takes its answer, the children it pays for in the month, from the caller, and reads s 72(a) (line 854) only to check that a listed child's birth and 18th birthday allow it |
| s 238 "עקרת בית" | 2401 ff. | housewife (Chapter 11) | out-of-scope (input) | a status the Institute records under Chapter 11, outside this row |
| s 381 | 4168-4170 | rounding of amounts, by rules the Minister makes | out-of-scope | the rounding regulations of 5746-1985 are not in the sources; every amount here is before rounding, and the tests compare with the Institute's rounded figures only to within one shekel |
| Income Tax Ordinance s 121B | (ITO) | income chargeable to additional tax | out-of-scope (input) | decided under the Ordinance; row IL-03 encodes it; fork F5 on which tax year |
| Income Support Law; Maintenance (Assurance of Payment) Law 5732-1972 | — | the payments s 68(c) turns on | out-of-scope (inputs) | whether a person is paid either for the month is recorded by the Institute |

## 3. Assumptions

**A1. The period answered: days from 1 May 2015.**
s 29(a) of the Economic Efficiency Law (Legislative Amendments for Achieving the Budget Targets for Budget Years 2015 and 2016), 5776-2015 (Sefer HaChukim 2511, 30.11.2015, p. 247) commences ss 1 and 68 "as worded in this Mark" on 1 May 2015.
That Law's s 28 substituted s 1 "הסכום הבסיסי" paragraph (2) and amended s 68(b) and (c); its paragraph (2) matches the deposited lines 186-189 word for word (checked by script, section 7).
The latest amendment tag on any of ss 65-68 in the deposited text is that Law's (תשע״ו־3, on s 68); s 65's last is תשס״ט־4 and s 66's תשע״ג־3; s 67 has none.
So the deposited text is the text in force from 1 May 2015, and a day before it is declined by name.
The identification of תשע״ו־3 with that Law is by counting the entries of the file's own list of amending Laws (line 7), confirmed by the Law's own contents (it amends ss 1, 68 and adds s 74B, as the deposited text's tags show).
Nothing in the sources ends the period; the figures are bounded separately (A3).

**A2. The day is an explicit input; `RULES EFFECTIVE DATE` is not used.**
For a monthly benefit the day asked about fixes, at once, the child's age, the facts about absence and payments, the text in force and the figures in force.
Taking it as a field of the case (`A family on a day`) keeps those together, and every dated arm (the period gate, the figures table) selects on it with its citation.

**A3. The Institute's table: each row applies from its date to the next row's.**
The table's date column is headed "from the day" and has rows for 1.05.2015 and then 1.01.2018-1.01.2026, with none for 2016 or 2017; 1 May 2015 to 31 December 2017 is therefore read as 150 / 188 / 140.
The table has no row from 1 January 2027, and the updating clause requires one, so days from 1 January 2027 are declined.
(0.2.0, 06-W1) More exactly: a day from 1 January 2027 is declined **wherever an amount is needed**.
A family none of whose persons has a child in the count needs no figure, and is answered (an allowance with no lines, or no allowance), as the Axiom comparison's incidental finding observed.

**A4. Figures found only in the consolidation's editorial notes are not encoded.**
The notes at lines 187-189 give the 2024-2026 amounts; they agree with the Institute's table, which is what the encoding cites.

**A5. Classifications outside the slice are inputs.**
Chapter 11 insurance; the s 238 housewife; residence, and the authorised employee's view of an absence; formerly insured (died or ceased); income chargeable to additional tax; payment of an Income Support benefit or a maintenance payment for the month; children by more than one woman (for the s 69A gate); how a person stands to a child, and whether the child is with them; the authorised person's satisfaction that an insured person supported a child; a child's marriage, absence from Israel, and the Institute's decision under s 65(b).

**A6. Amounts are before rounding, per month.**
s 381 leaves rounding to rules the Minister makes, which are not in the sources.

**A7. A person's answer is for the count s 67 gives that person.**
Each person in the family gets one answer; a person with no child in the count and entitled under s 66 gets an allowance with no lines (0 shekels).

## 4. Fork register

| # | where | the question | readings | taken, and why |
| --- | --- | --- | --- | --- |
| F1 | s 65(a) "ילד" (1), line 805; s 1 "ילד", line 170 | Does "his child" in s 65 carry s 1's extension (stepchild, adopted child) and exclusion (married boy or girl)? | (i) yes: s 65 defines which children count for the Chapter but uses "child" within its own definition, which can only mean the Law's general sense; (ii) no: s 65 displaces s 1, so a stepchild counts only under (2) on proof of support, and a married minor is a child | **(i)**. Reading (ii) makes s 65's own definition circular, and the extension to stepchildren is in the Law's own general definition. A test asserts the married-minor exclusion. |
| F2 | s 65(a) proviso, line 807; s 65(b), line 809 | Date arithmetic where the calendar has no corresponding day: an 18th birthday for a 29 February birth; three months from 30 November. | (i) clamp to the last day of the shorter month (28 February); (ii) roll into the next month (1 March, 2 March) | **(i)**, `add years` / `add months`. The text says nothing; the clamp is the conservative choice for both (the child stops being a child, and an absence stops being short, no later than the rolled date). Each changes the answer on one or two days. Tests sit on both. **(0.2.0, inventory DATE; waits on Meng, BACKLOG IL-24.)** Three readings, and who holds each: (i) clamp to the last day of the shorter month: this row, and rows IL-05 (its F19) and IL-08's National Insurance half (its N4), which took it to agree; (ii) roll to the 1st of the next month: no row or tester; (iii) refuse, the Law not saying: the independent tester (finding 2, `tests-independent.l4:608`) and IL-08's (its D-46 to D-48). Axiom: silent (no date arithmetic). The lead's recommendation (IL-24) is a named switch with decline as default; until a ruling, (i) stays the default. The tests that rest on (i) are labelled (`nii-il06-tests.l4:391-392`, `:403-404`, `:702-703`), and the month question carries the clamp into s 72: on (i) a 29 February child is not paid for March of her 18th year. |
| F3 | s 65(b), line 809 | "left Israel for a period not exceeding three months", for an absence that has not ended on the day asked. | (i) measure from the day of leaving to the day asked; (ii) the intended length of the trip; (iii) the actual length, known only afterwards | **(i)** where no return day is supplied; a caller who knows the return day (past or planned) supplies it and the full period is measured. **(0.2.0, 06-F5)** "past" meant past when the question is asked, not before the day asked about: an absence that ended before the day is not in progress on it, and is now reported as a problem with the facts. The return day itself is a day of the absence (an absence over three months leaves the child abroad on the day of return), as this row has always read it; stated in 0.2.0, assumed, not ruled (`nii-il06-tests.l4:611-612`). |
| F4 | s 68(a)-(c), s 1 (2), lines 187-188, 821-826 | How is the count ordered: which child is "the first", "the fourth"? | (i) by date of birth, eldest first; (ii) by the order children entered the count | **(i)**, children born the same day keeping the order of the family's list. The Institute's page computes the allowance "according to the number of children in the family, the children's dates of birth" and lists amounts by the child's "place in the family"; that supports (i) but is practice, not text. Only s 68(b) and the s 68(c) supplement's attribution depend on it; totals without (b) do not. |
| F5 | s 66, line 814 | "has income chargeable to additional tax": for which tax year? | (i) the tax year in which the month falls; (ii) the last assessed year | **not decided**: the input is the caller's answer for the day asked. **(0.2.0, 06-W3)** The capstone, row IL-07, joins this input to row IL-03's s 121B: chargeable if and only if IL-03's additional tax for the tax year in which the month falls is above nil (IL-07 `RECONCILE.md` N12, its fork K5, which takes reading (i) for the capstone). This row's F5 stays open. |
| F6 | ss 66 and 67(b), lines 814, 818 | Is a child whose insured father has income chargeable to additional tax still in the father's count? | (i) yes: s 66 keeps him "an insured parent", and s 67(b) counts with "the insured father", so the child is in his count and no allowance is paid for it; (ii) no: a parent excluded from the allowance is not a candidate, and the child goes to the other insured parent | **(i)**, the literal reading; it can deny a family the allowance although the mother has no such income. Tests assert it, labelled. Open question 1. |
| F7 | s 67(b), line 818 | Only one of the child's parents is insured. | (i) that parent's count, wherever the child is; (ii) the first limb literally: with "the insured father" unless with the mother only, so a child with an uninsured mother only is in no count | **(i)**: s 67 chooses among insured parents, and with one there is nothing to choose. **(0.2.0, 06-W2)** Who holds (ii): the independent tester, as a refusal (finding 1); and Axiom's RuleSpec, which answers it as "not counted" and extends it to a sole parent and to a natural parent with an uninsured step-parent (Comparison section, D1-D3), where this row finds no support for it in lines 814 and 818. |
| F8 | s 67(b), line 818 | What are "two parents" (first limb) and "a natural parent and another parent" (second limb)? | (i) first limb: the child's own parents, natural or adoptive; second: a natural parent and a step-parent or a person who supported the child; (ii) second limb: a natural parent and any parent who is not natural, adoptive included | **(i)**: an adopter is the child's parent in every respect, and reading adoption into the second limb would send a child of a stepparent adoption to whichever parent it is "with", which it is with both. |
| F9 | s 67(b) second limb, line 818 | A natural parent and another parent, both insured, and the child is with both of them (or with neither). | (i) the text does not say: declined; (ii) fall back on the first limb (the father, unless with the mother only) | **(i)**, a named refusal. This is the common blended family, so the refusal is reached often. Open question 3. **(0.2.0, 06-W2)** Axiom's RuleSpec answers instead: both counts when the child is with both, no count when with neither (D4, D5). |
| F10 | s 67(b) first limb, line 818 | Two insured parents who are both fathers or both mothers. | (i) the text, which names "the father" and "the mother", does not say: declined; (ii) the Institute's practice, stated on its page "to whom is the allowance paid?", that a same-sex couple living together may receive one allowance for all their common children | **(i)**, a named refusal. The Institute's practice is noted, not encoded. **(0.2.0, 06-W2)** Axiom's RuleSpec answers instead, by its formula: two mothers with the child, no count; two fathers, both counts (D6). |
| F11 | s 67(b), line 818 | Three or more insured parents; or two who fit neither limb (a step-parent and a supporter, an adopter and a step-parent). | — | **declined**, two named refusals. **(0.2.0, 06-W2)** Axiom's RuleSpec answers two insured parents who fit neither limb as "not counted" (D7), and cannot state three. |
| F12 | s 67(b) first limb, line 818 | "unless he is with the mother only". | — | with the mother and not with the father; a third person the child is also with (a step-parent, say) does not matter. |
| F13 | s 69A, line 843 | "ילדים ממספר נשים": children by more than one woman, or by more than one wife? | (i) women; (ii) wives | **(i) for the refusal gate only**: s 69A is not encoded, and the wider reading declines every case it might reach. |
| F14 | s 68(c), line 826 | The parent paid Income Support is not the parent in whose count the children are. | (i) no supplement: (c) speaks of a parent paid the benefit "and entitled … for three or more children"; (ii) the supplement attaches to the family | **(i)**, literal. A test asserts it, labelled. |
| F15 | s 65(a) "ילד" (2), line 806 | Must the supporter be insured, or may they have been insured? | — | insured: "the insured supported him". A person who is a parent only under (2) is therefore always an insured parent. |
| F16 | s 65(a) "מבוטח" (2), line 803 | The absence limb has three parts: temporary, reasonable in the authorised employee's opinion, and not contradicting the claim of residence. | — | one input, `absent from Israel beyond a reasonable temporary absence`, which is the authorised employee's determination on all three. |
| F17 | s 68(c), line 826 | "entitled … for three or more children": counted how? | — | the number of children in the parent's count, children under s 68(b) included. |
| F18 (0.2.0, 06-HW) | s 65(a) "מבוטח" (2), line 803 | Is a resident s 238 housewife, not insured under Chapter 11, insured under limb (2)? Limb (2) ends "ואינו מבוטח לפי פרק י״א, למעט עקרת בית כהגדרתה בסעיף 238". | (A) "and is not insured under Chapter 11; excluding a housewife": she is excluded from both limbs; (B) "and is not [insured under Chapter 11, other than a housewife]": the phrase repeats limb (1) verbatim and limb (2) negates it, so the limbs partition residents and she is insured under limb (2) | **(A)**, the reading `nii-s65-interpretation.l4:40-44` encodes, unrecorded until 0.2.0. Held by: (A) the encoder; (B) the independent tester (finding 4, who on reflection thinks (A) the weaker parse). Axiom: silent ("insured" is an input). It decides a child living with the mother only, or whose other parent is uninsured; the capstone's households are not affected (their children are with both parents). **Waits on Meng (BACKLOG IL-24)**; the lead recommends a named switch with decline as default. Until then (A) stays the default. The tests resting on (A) are labelled: `nii-il06-tests.l4:379`, `:415`, `:444`, `:465`. |
| F19 (0.2.0, 06-S72) | s 72(a), line 854, with s 68(a)-(c), lines 821-826 | In a month s 72 pays for a child after its entitlement ceased (the month of its 18th birthday) or before it arose (the month of a birth by the 15th), is the child in the parent's count for that month, at what place, and does it count for s 68(c)'s "three or more children"? | (i) yes: the count for the month is the children paid for, eldest first, so the child keeps its place and counts for s 68(c); (ii) s 72 continues the child's payment at the amount it had, and the count for the other children is made without it | **(i)**, assumed, not ruled. s 68(a) is the allowance "for each child in the parent's count" for the month, and s 68(c) asks for which children the parent is entitled "for that month"; s 72 pays the allowance, not a separate sum. It agrees with the capstone's fork K15 wherever K15 found a day to ask about. It changes an answer only in such a month: Keren, Gil and Hila in November 2026 are 611 on (i) (`nii-il06-tests.l4:660`), 173 + 173 + 219 = 565 on (ii). IL-07 open question 9 asks the Institute the same. |

Places where no fork was found, read for one and listed so a reviewer can disagree: s 68(b)'s "born before 1 June 2003" (strict: a child born on 1 June is not before it; the Institute's own heading "born until 31 May 2003" agrees, and a test sits on both days); "has not reached 18" (a child on the day before the 18th birthday, not on it); s 68(c)'s "the third child and the fourth child" (a parent with three children gets one supplement, with four or more two).

## 5. Answer table

Basic amounts from the Institute's table [nii-basic]; the amounts by place are s 68 applied to them, before rounding.
"(b)" columns are for a child born before 1 June 2003; every such child reached 18 by 31 May 2021, so they cannot arise later.
In brackets, the Institute's own per-child page where one was fetched [nii-rates-YYYY].

| from | (2)(a) | (2)(b) | (2)(c) | 1st | 2nd-4th | 5th+ | 4th, (b)(2) | 5th+, (b)(3) | s 68(c) supplement |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 May 2015 | 150 | 188 | 140 | 150 | 188 | 150 | 336 | 354 | 98 |
| 1 Jan 2018 | 150 | 189 | 140 | 150 [150] | 189 [189] | 150 [150] | 336 [336] | 354 [354] | 98 [98] |
| 1 Jan 2019 | 152 | 191 | 142 | 152 | 191 | 152 | 340.48 | 358.72 | 99.4 |
| 1 Jan 2020 | 152 | 192 | 142 | 152 [152] | 192 [192] | 152 [152] | 340.48 [340] | 358.72 [359] | 99.4 [99] |
| 1 Jan 2021 | 152 | 192 | 142 | 152 | 192 | 152 | 340.48 (to 30 May) | 358.72 (to 30 May) | 99.4 |
| 1 Jan 2022 | 156 | 197 | 145 | 156 | 197 | 156 | — | — | 101.5 |
| 1 Jan 2023 | 164 | 207 | 153 | 164 | 207 | 164 | — | — | 107.1 |
| 1 Jan 2024 | 169 | 214 | 158 | 169 [169] | 214 [214] | 169 [169] | — | — | 110.6 [111] |
| 1 Jan 2025 | 169 | 214 | 158 | 169 [169] | 214 [214] | 169 [169] | — | — | 110.6 [111] |
| 1 Jan 2026 | 173 | 219 | 162 | 173 [173] | 219 [219] | 173 [173] | — | — | 113.4 [113] |
| 1 Jan 2027 | declined where an amount is needed (0.2.0, 06-W1) | declined | declined | | | | | | |
| before 1 May 2015 | declined | | | | | | | | |

A family's monthly total in 2026, with no child under s 68(b) and no supplement: 1 child 173; 2 children 392; 3 children 611; 4 children 830; 5 children 1,003; 6 children 1,176; each further child 173.
With the s 68(c) supplement: 3 children 724.4; 4 or more, 226.8 above the figure without it.

## 6. Nouns to reconcile at IL-07

Read from the sibling deposits (read-only) near the end of this session; nothing here depends on them and nothing in them was changed.

- **The person.** This row: `A person` (Chapter 11 insurance, s 238 housewife, residence and absence, formerly insured, additional-tax income, Income Support and maintenance payments, children by more than one woman). IL-04: `A person who works` (employment relationship, the family-member limb of "employee", wage fixed by Law) and `A person's occupation in a period` (the self-employed limbs). One insured-person record could carry both. IL-04's own notes record that its s 335(b) and (i) turn on s 65(a)(1) "insured", which this row encodes as `s 65 "insured" (1) — insured under Chapter 11, other than a housewife`.
- **s 1.** IL-04 encodes several s 1 definitions (`nii-s1-definitions.l4`: "employee", "self-employed person", "the average wage"); this row encodes "ילד" and "הסכום הבסיסי" paragraph (2) (`nii-s1-basic-amount.l4`). They should become one s 1 module; IL-04's notes leave both definitions to this row.
- **Published figures.** Both rows keep a module of figures the Institute publishes (`nii-il04-published-figures.l4`, `nii-il06-published-figures.l4`). They cite different pages; one module, one provenance format.
- **Income chargeable to additional tax.** This row takes it as a BOOLEAN input; row IL-03 (Income Tax Ordinance) computes s 121B's additional tax for a tax year. IL-07 can join them as "chargeable iff the IL-03 additional tax for the tax year is above 0", once fork F5 (which tax year) is settled.
  **(0.2.0, 06-W3) Done at IL-07, without settling F5.** IL-07 (`il07-pipeline.l4`, `IL-07: the earner has income chargeable to additional tax in the tax year of the month, in`) passes TRUE exactly when IL-03's s 121B additional tax on the earner's salary for the tax year in which the month falls is above nil; its fork K5 takes F5's reading (i) for the capstone (IL-07 `RECONCILE.md` N12). The spouse, who has no income in the capstone, is given FALSE.
- **The tax year / the day.** IL-03 selects on the tax year; this row on a day. A day falls in exactly one tax year, so the join is mechanical.

## 7. Sources: what was fetched, and how quotations were checked

The deposited Law (sha256 `78bf47ee…552a97`) was verified on 2026-10-06 before use.
Fetched on 2026-10-06 (all fetched bytes were kept only in the session's scratch directory, and are cited here by sha256):

- **[nii-basic]** The Institute's page "the basic amount for computing benefits", fetched directly at 14:10 UTC: `https://www.btl.gov.il/Mediniyut/GeneralData/Pages/%D7%94%D7%A1%D7%9B%D7%95%D7%9D%20%D7%94%D7%91%D7%A1%D7%99%D7%A1%D7%99%20%D7%9C%D7%97%D7%99%D7%A9%D7%95%D7%91%20%D7%A7%D7%A6%D7%91%D7%90%D7%95%D7%AA.aspx`, 193,110 bytes, sha256 `d19985509135d947b3c34c0c1c462913adeddf5c9c86509ff4fccf2810994139`.
- **[nii-rates-2026]** The Institute's page of child-allowance amounts, fetched directly at 14:08 UTC: `https://www.btl.gov.il/benefits/children/Pages/%d7%a9%d7%99%d7%a2%d7%95%d7%a8%d7%99%20%d7%94%d7%a7%d7%a6%d7%91%d7%94.aspx`, sha256 `0bf54039e27ec719e1ec190d00e20012d26f88290e9ed2f5a6a4f503c1b4359c`.
- **[nii-rates-2025, -2024, -2020, -2018]** The same page as captured by the Internet Archive, fetched in the raw (`id_`) form: capture `20250420005113`, sha256 `3985123f0d5dfc54d3bd5ef971b23f9ecd59a6f47dd79990ac383ed70b024e64`; `20240806061702`, sha256 `0c7083ccd45f7eb327c3eda843c83b69f8431a5782262a7a8b6aa0fa798632f6`; `20200821105458`, sha256 `36b09fd990aec92110dc64e174edca48fbada24bcb895307d13bec84fc65d93c`; `20181003161656`, sha256 `3a7c5f6f347e48cebd7e199d94d987c0b34419021e4d59c1f1267a81dc5cdb09`.
- **[sh-5776-247]** The Economic Efficiency Law 5776-2015, Sefer HaChukim 2511: a direct fetch of `fs.knesset.gov.il/20/law/20_lsr_316719.pdf` returned a 131,618-byte HTML "Unavailable" page, so the PDF was fetched as Internet Archive capture `20151217003808` (raw form): 44 pp., sha256 `6c99d23c7d2521bd8691d5cc7b62c43eca6d76fec27f8ee0d2958dfee9c50797`.
  Later the same day (14:50 UTC) the same URL, `https://fs.knesset.gov.il/20/law/20_lsr_316719.pdf`, was fetched directly from the Knesset **through the lead's Israeli-IP SOCKS proxy** (an ssh tunnel to an EC2 instance): HTTP 200, `application/pdf`, 434,026 bytes, the same sha256. The Internet Archive copy is byte-identical to the Knesset's.
- Two further Institute pages were read for context and are not relied on for any figure: "eligibility conditions" (`…/benefits/children/Pages/%d7%aa%d7%a0%d7%90%d7%99%20%d7%96%d7%9b%d7%90%d7%95%d7%aa.aspx`, sha256 `bc15afbc4958c3d58e2c679d02067e1f661ed1ec359de4a105292974a98f7966`) and "to whom is the allowance paid?" (`…/benefits/children/Pages/%d7%9c%d7%9e%d7%99%20%d7%9e%d7%a9%d7%95%d7%9c%d7%9e%d7%aa%20%d7%94%d7%a7%d7%a6%d7%91%d7%94.aspx`, sha256 `fc7e745bcb94b1606edbb6fb30d8d6398d86124760ef94670956f6bcab245760`), the second for the same-sex practice noted at F10.

**Quotations from sources other than the Law** are on lines tagged `-- ext:[TAG] |`.
Each `[nii-…]` quotation was checked by script to occur in the text extracted from the page it cites (whitespace and direction marks normalised): ten quotations, all found.
The one `[sh-5776-247]` quotation (s 29(a) of the 5776 Law) was rebuilt from the PDF's text layer, whose lines are stored in visual order, by reversing each line's word order; its 19 Hebrew words were checked by script to occur contiguously in that layer, and its digits and punctuation by eye against page 31 rendered as an image.
The claim in A1 that s 1 paragraph (2) is word for word the 5776 Law's was checked the same way: the Hebrew words of each of lines 186-189 (editorial notes removed) occur contiguously in pages 28-31 of the PDF's text layer.

**Not read, under the semi-cleanroom ruling of 2026-10-06:** nothing from the Axiom Foundation, any RuleSpec repository, `.axiom/` directory or the other paths the brief lists was read, searched or fetched in this session, and no web search was made for encodings of Israeli social-insurance law.

## 8. Open questions for a domain expert

1. F6: when an insured father has income chargeable to additional tax, does the Institute count the children with him (so no allowance is paid for them), or with an insured mother who has no such income?
2. F7: with one insured parent and a child who lives only with the other, uninsured, parent, is the child in the insured parent's count? (0.2.0) Two other readers take the literal reading: the independent tester, as a refusal, and Axiom's RuleSpec, as "not counted", which it extends to a sole parent.
3. F9: for a child living with a natural parent and an insured step-parent together, in whose count is the child? Does the Institute apply the first limb (the father) by default? (0.2.0) Axiom's RuleSpec counts the child with both (and, for F10 and F11, with both or neither), where this row declines.
4. F10: what is the legal basis of the Institute's practice for same-sex parents, and in whose count are the children?
5. F4: does the Institute order the count by date of birth, eldest first, and does the order change when the eldest reaches 18?
6. F5: which tax year's additional-tax liability excludes a parent in a given month?
7. F14: when one parent is paid Income Support and the children are counted with the other, is the s 68(c) supplement paid?
8. The Institute's page lists old-age and survivors' pensioners with an income supplement among those who receive the s 68(c) supplement. Is that supplement "a benefit under the Income Support Law" within s 68(c)?
9. F2: how are a 29 February birthday and a three-month period from the 30th or 31st of a month computed?
10. F13: in s 69A, is "נשים" women or wives?
11. (0.2.0) F18: is a resident housewife within s 238, not insured under Chapter 11, insured under s 65(a) "מבוטח" limb (2)?
12. (0.2.0) F19: for the month in which a child turns 18 (or is born by the 15th), is that child in the parent's count for the month, at its place by date of birth, and does it count towards s 68(c)'s three children?

## 9. What was not done

- **The independent test pass** (skill step 8) was not run: the brief for this row is one session with no sub-agents. Every expected value was worked by hand from the text or from an Institute page before it was asserted, but no second reader has derived them.
  **(0.2.0, 06-W2) Stale.** An independent pass was run afterwards, on 2026-10-06, by `fid-il-06` (`DECIDED-ANSWERS.md`, `tests-independent.l4`, `INDEPENDENT-FINDINGS.md`): 146 assertions, 6 failed from 5 findings. After 0.2.0, finding 5 is repaired (06-F5) and four remain, each a recorded fork (F7, F2, F3, F18) that `check.sh` declares.
- **HG1**, a human who knows Israeli social-security law reading the modules against the Hebrew, has not been sought.
- **s 69A and s 71** are reachable and declined; encoding them is the obvious next unit, and the refusals mark exactly where they would plug in.
- **Performance.** The tests module takes about 40 seconds; the count of every child is recomputed for each person. Nothing here depends on that, but a deployment would want the counts computed once.
  (0.2.0) On the binary of 2026-10-08 (`jl4-0.1-d4290e25`) the tests module, with 156 assertions, ran in about 9 seconds.

## Comparison with Axiom's RuleSpec (2026-10-06)

Written by `lad-il-06` on 2026-10-07, after this row's encoding and its independent test pass were deposited, under the semi-cleanroom ruling of 2026-10-06, which allows the Axiom encoding to be read for this row once ours is deposited.
Line numbers are lines of `../../registers/source-bundle/national-insurance-law-consolidated-version-5755-1995.he.wiki.txt` (sha256 `78bf47ee…552a97`, re-hashed before use and matching).
A divergence is recorded as a finding, not a fix: nothing in this encoding was changed.

### What was read

**Commit.** A local clone of `TheAxiomFoundation/rulespec-il` at `95c6f32c87c75e318631cbd77c14b840bc536c15` (2026-10-03, "Merge pull request #8 … encode/il-nii-contributions"), read in place, not pulled or modified.

**Files read in full** (sha256 of each matches the one its encoding manifest records):

| file | sha256 |
| --- | --- |
| `il/statutes/national-insurance-law-1995/section-66.yaml` | `3720f4f2…5f49` |
| `il/statutes/national-insurance-law-1995/section-66.test.yaml` | `b323aaf8…650d` |
| `il/statutes/national-insurance-law-1995/section-67.yaml` | `f179fe16…efed7` |
| `il/statutes/national-insurance-law-1995/section-67.test.yaml` | `136ee4a0…8dec` |
| `il/statutes/national-insurance-law-1995/section-68.yaml` | `a9f74b43…309d` |
| `il/statutes/national-insurance-law-1995/section-68.test.yaml` | `0c0da31c…984d` |
| `il/statutes/national-insurance-law-1995/section-1.yaml` | `ec1a280a…ddec1` |
| `il/statutes/national-insurance-law-1995/section-1.test.yaml` | `37517e5f…b570` (the empty list `[]`) |
| `.axiom/encoding-manifests/il/statutes/national-insurance-law-1995/section-{1,66,67,68}.json` | — |

`section-68.yaml` imports three rules from `section-1.yaml`, and those three rules are the whole of that file, so it was read in full.
There is no `section-65.yaml` (a directory listing shows none; Axiom's own gaps file says so).
The manifests name the generating runner for each file (`codex-gpt-5.6-terra` for ss 1 and 68, `codex-gpt-6-astra` for ss 66 and 67) and a chain of three to six superseded earlier runs.

**Entries read from the gap and coverage files:** `docs/ENCODING-GAPS.md` entries `child-allowance-surtax-exclusion-vs-oecd` (line 253), `nii-68c-increment-not-reconcilable-with-the-published-figure` (340), `nii-section-1-paragraphs-1-and-3` (462), `nii-section-68-repealed-and-unencoded-subsections` (467), `nii-section-67-relations-are-facts` (471), `nii-section-67a-is-audited-not-enforced` (482), `nii-section-67a-proof-atom-has-no-excerpt` (494), `nii-section-65-child-definition-partial` (543), and the two rows for the child-allowance basic amounts in its table "Amounts supplied rather than encoded" (lines 369-370).
`known-missing-money-atoms.yaml` and `known-validation-gaps.yaml` have no entry for the National Insurance Law (counted with `grep -c`).
From `data/coverage/tax-benefit-source-map.json`, only the National Insurance Law instrument's entries for ss 1 and 65-68: `temporal_coverage: current_expression_only`, expression date 2026-06-15 (Hebrew Wikisource), `encoded_sections` including 1, 66, 67, 68, and s 65 listed as not encoded as a module.

**Read outside the allowed list, said plainly.** A line range I printed from `ENCODING-GAPS.md` (253-339) ran past the s 66 entry and printed three entries that are not this row's: `additional-tax-threshold-is-the-statute-s-nominal-figure` and `section-121b-a1-capital-charge-not-dated-from-2025` (both on Income Tax Ordinance s 121B), and `section-66-proof-excerpts-quote-the-earlier-corpus-render` (on Income Tax Ordinance s 66, credit points, which I had expected to be NII s 66).
Those three entries, the s 65 and s 66 entries and lines 372-373 (printed by a filter) mention Axiom's composed pipeline in passing.
Nothing from them about the composition or about another provision is used below, and no file under `composed/` was opened.
The entry `composed-capstone-does-not-apply-nii-67-or-68b-c` (line 536) was not read beyond its heading.

**Licence.** `NOTICE` at that commit: encodings, companion test cases, parameter values and provenance metadata are CC BY 4.0 (`LICENSE` is the CC BY 4.0 legal code); incidental tooling is Apache 2.0 (`LICENSE-CODE`); the statutes are public domain.
This agrees with what earlier comparison agents found.
Snippets below are short and attributed: "Axiom Foundation RuleSpec corpus (CC BY 4.0), https://github.com/TheAxiomFoundation".
No Axiom file was copied into this directory.

**Same text.** Each of Axiom's 19 proof excerpts for these provisions occurs verbatim in the deposited source once the wiki markup is stripped (checked by script), so the two encodings read the same Hebrew for ss 1(2), 66, 67 and 68 (Axiom's corpus expression is dated 2026-06-15; ours was retrieved 2026-10-06).

### How each is built, in one paragraph each

**Axiom.** Four modules, one per section, with no Child entity.
s 66 is one Judgment over two Boolean inputs (`person_is_insured_parent`, `insured_parent_has_income_subject_to_additional_tax_under_section_121b`).
s 67 is two Judgments for one child and one "current" insured parent, over six Boolean inputs (`child_has_two_parents`, `current_insured_parent_is_father`, `child_is_with_mother_alone`, `child_has_natural_and_other_parent`, `child_other_parent_is_insured`, `child_is_with_current_insured_parent`) and a caller-supplied count for s 67(a).
s 68 is two Money values for one child, over its position in the count, the parent's count, a Boolean "born before the statutory cutoff date", entitlement for that child, and the two payment flags.
s 1 is three parameters: 150, 188, 140.
Every rule has `effective_from: '0001-01-01'` and `period: Month`.

**Ours.** One question, a family on a day, through s 65 (both limbs of "insured", both limbs of "child", the proviso, s 65(b)), s 1 "ילד", s 66, s 67 (count computed for every child, ordered eldest first), s 68, a period gate from 1 May 2015, and the Institute's published amounts by year in a module marked not-law; named refusals where the text is silent and for s 69A and s 71.

### Divergence table

Classes: **ours wrong**, **theirs wrong**, **genuine ambiguity** (the text supports both), **scope difference**, **representational difference**.
"No count" means Axiom's `child_counted_with_insured_parent` is `not_holds` for every parent of the child.

| id | provision | ours | theirs | source lines | class | proposed repair to ours |
| --- | --- | --- | --- | --- | --- | --- |
| D1 | s 67(b), a child with one parent only | that parent's count (`nii-s67-count-of-children.l4:169`, one candidate) | no count: the case `father_default_requires_two_parents` asserts `not_holds` for the child's only, insured, parent | 814 "בעד כל ילד"; 818 | **theirs wrong.** s 66 entitles the insured parent for each child; s 67(b)'s two limbs only choose between two parents, and neither they nor s 67(a) say that a child no limb reaches is in no count. Axiom's reading treats s 67(b) as the exhaustive list of ways into a count, which leaves every sole parent without an allowance. | none |
| D2 | s 67(b) first limb, two parents and only one insured (our F7) | the insured parent's count, wherever the child is | (a) father insured, mother not, child with the mother only: no count; (b) mother insured, father not, child not with the mother only: no count | 818 "יבוא במנין האב המבוטח זולת אם הוא נמצא עם האם בלבד" | **genuine ambiguity**, recorded as our F7. Axiom takes our reading (ii), as the independent tester did for (a) (INDEPENDENT-FINDINGS, finding 1). (b) leans our way: no word of the limb excludes the mother there; the child is sent to an "insured father" who does not exist. | none; add Axiom as a second reading under F7 and open question 2 |
| D3 | s 67(b), a natural parent and another parent, only one of them insured | the insured one's count | no count (cases `natural_and_other_parent_limb_requires_other_parent_insured`, `overlapping_parent_facts_require_other_parent_insured`, `natural_and_other_parent_situation_displaces_father_default`) | 818 "והם מבוטחים" | **theirs wrong.** The second limb applies by its own words only when both are insured, so it cannot be what excludes the child; and in the two "overlapping" cases the first limb, which Axiom switches off whenever the natural-and-other flag holds, gives the insured father, since the child is not with the mother only. The first case (natural mother insured, step-father not, no second natural parent) is D1's shape. | none |
| D4 | s 67(a) with s 67(b): the same child in two counts | impossible by construction, and asserted (`nii-s67-count-of-children.l4:223-227`) | a natural parent and another parent, both insured, child with both: `holds` for each (by the formula; the case `natural_and_other_insured_parents_child_counts_where_present` does not say whether the child is also with the other); two insured fathers: `holds` for each. Axiom's s 67(a) judgment checks a caller-supplied number against 1 and does not constrain the s 67(b) judgment (its own entry `nii-section-67a-is-audited-not-enforced`) | 817 "לא יבוא ילד, בפרק זמן אחד, במנין ילדים של יותר מהורה מבוטח אחד" | **theirs wrong** (recorded by Axiom). Which parent the child goes to in these shapes is D5/D6. | none |
| D5 | s 67(b) second limb, both insured, child with both or with neither (our F9) | named refusal | with both: both counts (D4); with neither: no count | 818 "אותו הורה אשר עמו הוא נמצא" | **genuine ambiguity**: the limb names one parent "with whom he is" and the facts give two or none. Ours declines; theirs defaults. | none |
| D6 | s 67(b) first limb, two fathers or two mothers (our F10) | named refusal | two mothers, child with both: no count; two fathers: both counts (D4). No Axiom case covers it; read off the formula | 818 "האב … האם" | **genuine ambiguity**. | none |
| D7 | s 67(b), two insured parents fitting neither limb (our F11) | named refusal | no count (case `presence_alone_does_not_establish_natural_and_other_parent_limb`) | 818 | **genuine ambiguity**: the text does not say. | none |
| D8 | s 67(b), which limb applies when a family fits both, and where an adopter falls (our F8) | by the standing of the two insured candidates: the child's own parents (natural or adoptive) take the first limb, a natural parent with a step-parent or supporter the second | the caller sets both flags; when both hold, the second limb displaces the first; adoption is not addressed | 818; 170 "וילד מאומץ" | **representational difference**, with F8's ambiguity on adopters left to Axiom's caller. Its consequence for one-insured families is D3. | none |
| D9 | s 1 "הסכום הבסיסי" (2) and its updating clause: the amount in force | the 2015 base kept as the printed figure (`nii-s1-basic-amount.l4:34-52`); the amount in force on a day from the Institute's table [nii-basic] (`nii-il06-published-figures.l4:58-72`) | 150 / 188 / 140 for every period. Its own s 68 cases, dated 2024-01, assert 188, 98, 336 and 354, which are the 2015 base; at the amounts in force in January 2024 (169 / 214 / 158) the same inputs give 214, 110.6, 378.56 and 398.84 | 187-189; 192; 197 "ב־1 בינואר של כל שנה, לפי שיעור עליית המדד" | **theirs wrong** for any period from 1 January 2018 ((2)(b) became 189) and for all three amounts from 1 January 2019; right for 1 May 2015 to 31 December 2017. Recorded by Axiom: the update mechanism is not encoded (`nii-section-1-paragraphs-1-and-3`), and the current figures are not carried in its repository. | none |
| D10 | s 68(c), the Institute's published supplement | 70% of the (2)(c) amount in force: 110.6 in 2024-2025, 113.4 in 2026, which the Institute publishes rounded as 111 and 113 (NOTES section 5) | `nii-68c-increment-not-reconcilable-with-the-published-figure` calls 111 and 113 `unexplained`, because only the nominal 140 was captured; it also says the OECD's "0.7*153" cannot reach 111 | 189; 197; 826 "70% מן הסכום הבסיסי הקבוע בפסקה (2)(ג)" | **theirs wrong** (a recorded gap that the updating clause and [nii-basic] close): the figure is 70% of the indexed (2)(c) amount. The 153 Axiom quotes is the Institute's (2)(c) amount from 1 January 2023 (`nii-il06-published-figures.l4:34`), so it is a 2023 figure compared with a 2025 one. | none |
| D11 | the period answered | days from 1 May 2015 (`nii-il06-period.l4:55-56`, on s 29(a) of the 5776 Law [sh-5776-247]); a day from 1 January 2027 is declined where an amount is needed | every period (`effective_from: '0001-01-01'`; coverage map `current_expression_only`), at the 2015 base | 820 (latest tag תשע״ו־3); the date itself is from [sh-5776-247], not the deposited text | **scope difference.** The deposited source alone does not date the text; on [sh-5776-247] Axiom answers days before 1 May 2015 with a text not then in force. | none (but see "incidental finding" below on our 2027 wording) |
| D12 | s 65 and s 1 "ילד" | encoded: both limbs of "insured", both limbs of "child", the proviso (in Israel, under 18 by the day), s 65(b), s 1's stepchild, adopted child and married-minor rules | not encoded as a module: `person_is_insured_parent` and the relation flags are inputs; Axiom's gaps entry says the supporter limb (806) and s 65(b) (809) are not modelled and age and presence in Israel are supplied, not computed | 170; 801-809 | **scope difference.** | none |
| D13 | s 69A and s 71 | named refusals consulted before s 67 answers | not encoded and not gated: s 67 answers for a family s 69A or s 71 governs | 843 "על אף האמור בכל מקום אחר בסימן זה"; 845 (the children in the father's count unless the mother proves a separate household); 851 | **scope difference**, with the consequence that Axiom's s 67 answer for an insured man with children by several women is the one s 69A displaces. | none |
| D14 | s 68(b) "born before 1 June 2003" | computed from the date of birth, strictly before (`nii-s68-amount.l4:43-49`) | a Boolean input, `child_was_born_before_statutory_cutoff_date` | 822 "לפני יום א׳ בסיון התשס״ג (1 ביוני 2003)" | **representational difference**: the caller decides "before" against "on". | none |
| D15 | the order of the count (our F4) | eldest first by date of birth, same-day births in list order | a caller-supplied position | 187-188, 821-826 | **representational difference** (Axiom silent on F4). | none |
| D16 | s 66 with s 68: an insured parent who is not entitled | no allowance lines at all (`nii-s68-amount.l4:156-159`) | the per-child amount is still computed (case `third_child_when_parent_is_not_entitled`: 188), only the supplement is gated | 814 | **representational difference**: Axiom's per-child amount is "the amount if paid"; entitlement is gated elsewhere. | none |
| D17 | the unit asked about | a day; s 72 (the months paid) is not encoded | a Month | 814 "חודשית"; 821 "לחודש"; 826 "בעד חודש מסוים" | **representational difference**; neither encodes s 72. | none |
| D18 | Axiom's s 68 companion cases | — | two cases put a child at place 4 in a count of 3 (`pre_cutoff_fourth_child_with_income_support`, `post_cutoff_fourth_child_with_maintenance_payment`); two put a child born before 1 June 2003 in a count in January 2024, when every such child had reached 18 (by 31 May 2021) | 807 "ולא מלאו לו 18 שנים"; 822 | **theirs wrong** (inconsistent fixtures, not a legal reading). Our interface cannot state these facts, because the place is derived from the count. | none |

**Totals: 18 divergences. Ours wrong 0; theirs wrong 6 (D1, D3, D4, D9, D10, D18); genuine ambiguity 4 (D2, D5, D6, D7); scope difference 3 (D11, D12, D13); representational difference 5 (D8, D14, D15, D16, D17).**

**Where the two agree.** Every number the text prints: 150, 188, 140 as the base (187-189); places 1 and 5-onward at (2)(a), 2-4 at (2)(b); the multipliers 2.24 and 2.36 applied to (2)(a) (824-825); 70% of (2)(c), for the third and fourth child, when entitled for three or more and paid an Income Support benefit or a maintenance payment (826).
s 66 in full (814), including that the exception is of an insured parent.
The plain first-limb cases: father insured, child not with the mother only, the father's count; child with the mother only, the mother's count, when she is insured (818).
Neither encodes s 381 rounding; both give 70% × (2)(c) unrounded.

### Our 17 forks against Axiom

| fork | Axiom |
| --- | --- |
| F1 s 1 "ילד" read into s 65 | silent: s 1 "ילד" and s 65 are not encoded; the relation flags are inputs |
| F2 29 February, three months from the 30th | silent: no date arithmetic in these files |
| F3 an absence not yet ended | silent: s 65(b) not modelled |
| F4 the order of the count | silent: the position is an input (D15) |
| F5 which tax year for s 66's exception | silent: the exception is an input. Axiom records a different question, `unexplained`: whether the exception is applied at all, since the OECD TaxBEN description calls the allowance "not means-tested" |
| F6 the excluded father keeps the count | agrees, implicitly: its s 67 does not consult s 66, so a father with additional-tax income is still the "current insured parent" and the child stays with him; not recorded |
| F7 one insured parent | disagrees: reading (ii), extended to a sole parent (D1, D2, D3) |
| F8 what "two parents" and "a natural parent and another parent" are | different structure: caller-set flags, second limb first (D8) |
| F9 natural and other parent, with both or neither | disagrees: both counts or no count, never a refusal (D4, D5) |
| F10 two fathers or two mothers | disagrees: no count or both counts (D6) |
| F11 three parents, or neither limb | disagrees: no count (D7); three parents cannot be stated |
| F12 "with the mother only" | silent: `child_is_with_mother_alone` is an input |
| F13 s 69A "נשים" | not reached: s 69A is not encoded (D13) |
| F14 Income Support paid to the other parent | agrees, implicitly: the s 68(c) inputs are those of the parent whose count is priced |
| F15 the supporter must be insured | silent: s 65 "child" (2) not modelled |
| F16 the absence limb as one input | silent: "insured" is an input |
| F17 the count for s 68(c) includes (b) children | silent: `parent_child_count` is an input |

Agree 2 (F6, F14), disagree 5 (F7, F9, F10, F11, and F8 by structure), silent or not reached 10.
Axiom records none of F1-F17 as a fork; its gap entries on s 67's relations, on s 67(a) and on s 65 touch F8-F12, F1-F3 and F15 only to say that the caller supplies the fact or that the limb is not modelled.

### Axiom's own cases, put through our encoding

Run on 2026-10-07 in a scratch copy of our ten modules plus one scratch module (`lad-il-06/run/axiom-cases.l4`), with `/Users/mengwong/.local/bin/l4 run`, `JL4_LIBRARY_PATH` unset: type-check succeeded, every `#EVAL` produced a value or a named refusal.
Axiom's expected values were checked against Axiom's formulas by hand (its runner was not run); all 20 are what its formulas give.
Each Axiom case was realised as a family; where Axiom's inputs leave open a fact ours needs (is the other parent insured? is the child also with the other parent?), each realisation is shown.
s 67 cases are asked on 15 September 2026 (Axiom period 2026-09); "Avi", "Batya" natural father and mother, "Gadi" step-father, "Dina" step-mother, "Ezra" a supporter whose support is proven.

| # | Axiom case | Axiom expects | our realisation and answer | result |
| --- | --- | --- | --- | --- |
| 66-1 | `insured_parent_without_additional_tax_income_is_eligible` | holds | insured, no additional tax: entitled TRUE | match |
| 66-2 | `insured_parent_with_additional_tax_income_is_excluded` | not_holds | FALSE | match |
| 66-3 | `person_who_is_not_an_insured_parent_is_not_eligible` | not_holds | FALSE | match |
| 67-1 | `insured_father_counts_child_not_with_mother_alone` | father: holds; s 67(a) holds | Avi insured, child with both: `JUST "Avi"`, with Batya insured or not; s 67(a) TRUE | match |
| 67-2 | `mother_alone_exception_blocks_insured_father` | father: not_holds | child with Batya only: Batya insured, `JUST "Batya"`; Batya not insured, `JUST "Avi"` | match / **diverge** (D2, F7) |
| 67-3 | `insured_mother_counts_child_with_mother_alone` | mother: holds | child with Batya only: `JUST "Batya"`, with Avi insured or not | match |
| 67-4 | `insured_mother_does_not_count_child_when_not_with_mother_alone` | mother: not_holds | child with both: Avi insured, `JUST "Avi"`; Avi not insured, `JUST "Batya"` | match / **diverge** (D2, F7) |
| 67-5 | `natural_and_other_insured_parents_child_counts_where_present` | current (Batya): holds | Batya and Gadi insured: child with Batya only, `JUST "Batya"`; child with both, refusal (F9) | match / **diverge** (D4, D5) |
| 67-6 | `natural_and_other_parent_limb_requires_other_parent_insured` | not_holds | Batya insured, Gadi not, child with Batya: `JUST "Batya"` | **diverge** (D1/D3) |
| 67-7 | `natural_and_other_parent_limb_requires_child_present` | current (Batya): not_holds | child with Gadi only, `JUST "Gadi"`; with neither, refusal (F9) | match / **diverge** (D5) |
| 67-8 | `presence_alone_does_not_establish_natural_and_other_parent_limb` | not_holds; s 67(a) not_holds (caller says 2) | Gadi and Ezra insured, child with Gadi: refusal (F11); our s 67(a) refuses with it, and a caller's count cannot be supplied | **diverge** (D7); s 67(a) could not be run (our s 67(a) is computed, not supplied) |
| 67-9 | `overlapping_parent_facts_require_other_parent_insured` | not_holds | Avi insured, Dina not, child with both: `JUST "Avi"` | **diverge** (D3) |
| 67-10 | `overlapping_parent_facts_require_child_with_current_parent` | not_holds | Avi and Dina insured, child with neither: refusal (F9). (A child with Dina only would make `child_is_with_mother_alone` arguably true, against Axiom's input) | **diverge** (D5) |
| 67-11 | `overlapping_parent_facts_count_child_with_current_insured_parent` | holds | Avi and Dina insured, child with Avi: `JUST "Avi"` | match |
| 67-12 | `natural_and_other_parent_situation_displaces_father_default` | not_holds | Avi insured, Dina not, child with neither: `JUST "Avi"` | **diverge** (D3) |
| 67-13 | `father_default_requires_two_parents` | not_holds | Avi insured, the child's only parent: `JUST "Avi"`; s 67(a) TRUE | **diverge** (D1) |
| 68-1 | `pre_cutoff_fourth_child_with_income_support` | 336; supplement 98 | as given (place 4 in a count of 3, a pre-2003 child in 2024): could not be run at family level (D18). Function level, at the printed amounts: 336, 98; at the amounts in force in January 2024: 378.56, 110.6. Nearest consistent family (four children, the fourth born 10 Feb 2003, father paid Income Support, 15 Jan 2016): fourth line 336 + 98 | match at the 2015 amounts; **diverge** for the stated period (D9) |
| 68-2 | `pre_cutoff_fifth_child_without_supplement_conditions` | 354; 0 | as given: impossible in 2024 (D18). Function level: 354, 0 printed; 398.84, 0 in January 2024. Five pre-2003 children on 15 Jan 2016: fifth line 354, 0 | match at the 2015 amounts; **diverge** for the stated period (D9) |
| 68-3 | `post_cutoff_fourth_child_with_maintenance_payment` | 188; 98 | place 4 in a count of 3 cannot be stated (D18). Function level: 188, 98 printed; 214, 110.6 in January 2024. Four children, father paid maintenance, 15 Jan 2024: fourth line 214 + 110.6; the same on 15 Jan 2016: 188 + 98 | match at the 2015 amounts; **diverge** for the stated period (D9) |
| 68-4 | `third_child_when_parent_is_not_entitled` | 188; 0 | father with additional-tax income, paid Income Support, three children, 15 Jan 2024: "no child allowance, being an insured parent with income chargeable to additional tax", no lines | supplement: match (0). Allowance: not comparable (D16); our s 68(a) amount at (2)(b) is 188 printed, 214 in January 2024 |

**Results: 6 match outright (66-1 to 66-3, 67-1, 67-3, 67-11); 4 match or diverge on a fact Axiom does not take (67-2, 67-4, 67-5, 67-7); 6 diverge (67-6, 67-8, 67-9, 67-10, 67-12, 67-13); the 4 s 68 cases match at the 2015 base and diverge at the amounts in force in their stated period, 2024-01, and three of them cannot be run at family level as given because their facts are inconsistent.**
Every s 67 divergence is one where Axiom answers "not counted" and ours either counts the child with its only insured parent or declines by name.

### Our independent-test findings against Axiom

| finding (INDEPENDENT-FINDINGS.md) | Axiom |
| --- | --- |
| 1. Father insured, mother not, child with the mother only | no count (case 67-2 with the mother uninsured): the tester's literal reading, delivered as an answer, not a refusal or a recorded fork |
| 2. Born 29 February, day 28 February | silent: no date arithmetic in these files; its gaps entry says age is supplied, not computed |
| 3. Six-month trip, with and without a return day | silent: s 65(b) not modelled; presence in Israel is supplied as a conclusion |
| 4. The s 238 housewife under s 65(a)(2) | silent: "insured" is an input; s 65 "מבוטח" not encoded |
| 5. A finished absence still leaving the child abroad | silent: no absence facts |

Axiom gives no evidence on findings 2 to 5, so the repairs the independent tester proposed for 4 (open a fork) and 5 (reject or ignore a finished absence) stand as they were.

### What Axiom covers that we do not, and the reverse

**Axiom, not us.**
Proof atoms tying each formula to a verbatim excerpt, and a manifest chain recording the generating run.
Each multiplier and threshold as a named parameter rule.
A per-child amount callable for one child without building a family.
An s 67(a) judgment over a caller-supplied number (an audit; see D4).
A recorded open question on whether s 66's exception is applied, given the OECD TaxBEN description (`child-allowance-surtax-exclusion-vs-oecd`); our NOTES do not raise it.

**Us, not Axiom.**
s 65 in full and s 1 "ילד" (D12).
The dates the text turns on: the 18th birthday, 1 June 2003, three months abroad (D14, findings 2-3).
The order of the count (D15) and the attribution of s 68(b) and (c) by a computed place.
s 67(a) by construction (D4).
The amounts in force by year with provenance (D9, D10).
The period gate (D11).
Named refusals where the text is silent (D5-D7) and for s 69A and s 71 (D13).
Validation of facts that cannot describe a case.
An independent test pass.

### Incidental finding about our own notes (not an Axiom divergence)

NOTES assumption A3 and the answer table say days from 1 January 2027 "are declined".
In the scratch run, a family on 15 January 2027 whose only child had turned 18 on 10 January 2027 got `RIGHT`, an allowance with no lines, not a refusal; the same family with a child of 11 was refused ("the basic amounts … from 1 January 2027 had not been published …").
The refusal is reached only where an amount is needed.
That answer is right (it needs no figure), but the sentence overstates.
**Proposed repair:** reword A3 and the table row to "a day from 1 January 2027 is declined wherever an amount is needed".

### Proposed repairs to our encoding

None is required by the Hebrew: no divergence found ours wrong.
To NOTES only:
(1) under F7 and open question 2, record that a second encoding (Axiom) takes reading (ii) and extends it to sole parents (D1-D3);
(2) under F9-F11, record that Axiom defaults to "not counted" or counts twice where ours declines (D4-D7);
(3) add an open question: is s 66's exception for additional-tax income applied by the Institute (Axiom's `unexplained` entry against the OECD description)?
(4) the A3 wording above.

### Bottom line

The two encodings read the same Hebrew and agree on every printed number, on s 66, on the s 68 arithmetic and on the plain first-limb cases.
They part where the text does not plainly decide s 67: Axiom answers every such shape "not counted" (or counts a child twice), while ours counts the child with its only insured parent or declines by name.
In two of those places (a sole parent, D1; a natural-and-other family with one insured parent, D3) Axiom's answer has no support in lines 814 and 818; in the others the text supports both, and ours already records the fork.
Axiom's amounts are the 2015 base for every period, and its own 2024-dated cases assert them; our use of the Institute's table also explains the published 111 and 113 supplements that Axiom records as unexplained.
The comparison found nothing in the Hebrew that shows our encoding wrong.
It does add weight to open question 2: two independent readers (the tester and Axiom) now take the literal reading of F7, though the count of readers is not the text.
