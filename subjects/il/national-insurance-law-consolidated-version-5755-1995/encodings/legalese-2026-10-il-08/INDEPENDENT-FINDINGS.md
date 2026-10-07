# Independent findings, IL-08 National Insurance half (`fid-il-08b`)

These are independent tests of row IL-08's encoding of National Insurance Law [Consolidated Version], 5755-1995: s 72, s 335 and Schedule A1 Part D.
Every expected value comes from `DECIDED-ANSWERS.md`, which was written from the Hebrew source and the deposited amending Laws before any module of the encoding was opened.
Status: evidence for the encoder to weigh, as `skills/encoding-a-subject/references/second-pass.md` describes. These findings are not rulings.

## How the work was done, and in what order

1. A first `fid-il-08b` session wrote `DECIDED-ANSWERS.md` and finished it at 00:42:39 UTC (its own header; the lead verified this against the transcript).
   It then drafted `tests-independent.l4` and ran it twice.
   The first run (`run1.txt`) stopped on two compile errors (a `NOT` that reached to the end of its line). The second run (`run2.txt`) evaluated the file.
   A usage limit cut that session off before it wrote any findings.
2. A second session (the author of this file) did the following:
   - read `DECIDED-ANSWERS.md`;
   - read the four rule modules (`nii-il08-nouns.l4`, `nii-s72-period-of-allowance.l4`, `nii-s335-branches.l4` and `nii-schedule-a1-part-d.l4`) to check the names in the interface;
   - checked the draft against `DECIDED-ANSWERS.md` line by line, revised it and ran it.

   It did not open the encoder's two tests modules or `encoding.json`.
   The tests were final at 01:35:19 UTC (`date -u`), with `tests-independent.l4` at sha256 `bd929543…14efda2`.
   Only after that did this session read `NOTES.md`, all 182 lines of it. It has no section headed "Comparison with Axiom", and the word "Axiom" does not appear in it.
3. **Reused, then revised.** The draft's expected values were all found to match `DECIDED-ANSWERS.md`, and none was changed. The second session changed three things:
   - It gave every assertion a comment with its scenario id.
   - It replaced the partial checks for 335-10, 335-16, 335-17, 335-18, 335-19 and 335-20 with assertions on the full branch list decided for each. The draft had checked only two branches per scenario, which proves less than the decided answer says.
   - It added an assertion that the unexported first-month rule puts 72-14 in October 1995.

## The run

Command: `/Users/mengwong/.local/bin/l4 run tests-independent.l4`, run in a scratch copy of the encoding directory, with `JL4_LIBRARY_PATH` unset.
Counted from the diagnostics in the way `check.sh` counts them. The exit code was not used, because it is 0 even when assertions fail.

| `#ASSERT` lines | errors | satisfied | failed | refused |
| ---: | ---: | ---: | ---: | ---: |
| 143 | 5 | 136 | 5 | 2 |

143 = 136 + 5 + 2, and each assertion is reported once.
The 5 errors are the 5 failed assertions; there is no other error.
The only other diagnostics are the usual two Warnings that `prelude` and `daydate` have more than one copy on disk.

## Failing and refused assertions

### 1 and 2. 72-57 (lines 247 and 248): failed

- **Scenario.** A child was born on 20 February 2026, left hospital, and died on 25 February 2026. Is the allowance paid for March 2026?
- **Provisions.**
  - s 72(א): "נוצרה הזכאות אחרי 15 בחודש פלוני, תשולם הקצבה החל ב־1 בחודש שלאחריו; תשלום הקצבה יסתיים ביום האחרון של החודש שבו נפסקה הזכאות". Under this limb payment would start on 1 March and end on 28 February, so no month falls inside the window.
  - s 72(ג): "נפטר ילד שבעדו שולמה קצבת ילדים, ימשיכו בתשלום הקצבה שלושה חודשים מתום החודש שבו נפטר".
- **Expected.** REFUSE: the sources do not say whether (ג) runs for a child whose payment window was empty.
- **Answered.** The answer depends on the caller's input "a child allowance was paid for the child":
  - With FALSE (line 247), the answer is FALSE: neither February nor March is paid.
  - With TRUE (line 248), the answer is TRUE: March, April and May 2026 are paid, and June is not (from a scratch probe).
- **Classification.** Genuine ambiguity, recorded by the encoder as fork N2 and as open question 2 in `NOTES.md` §9. The encoder took "no" rather than refusing.
  On reflection I now lean to N2. "ימשיכו" (they shall continue) presupposes a payment already under way.
  N2's answer is reached only when the caller supplies FALSE. With TRUE, the encoding pays three months for a child whose own s 72(א) window was empty, and it gives no diagnostic (see "Silent paths" below).

### 3, 4 and 5. D-46, D-47 and D-48 (lines 733, 735 and 737): failed

- **Scenario.** The day a woman reaches the age that Part D fixes for her, when her date of birth moved on by that age lands on a day that does not exist.
- **Provision.** Part D, "גיל הזכאות לקצבת אזרח ותיק לנשים לפי חודש לידתן":
  - D-46: born 31 October 1945, row "ספטמבר 1945 עד אפריל 1946 / 67 ו־8 חודשים" (line 4446). The age lands on 31 June 2013.
  - D-47: born 29 February 1944, row "מאי 1942 עד דצמבר 1944 / 67" (line 4444). The age lands on 29 February 2011.
  - D-48: born 31 July 1945, row "ינואר עד אוגוסט 1945 / 67 ו־4 חודשים" (line 4445). The age lands on 31 November 2012.
- **Expected.** REFUSE. The Law does not say whether the day is the last day of the shorter month or the first day of the next.
- **Answered.** 30 June 2013, 28 February 2011 and 30 November 2012 respectively. `add months` moves the day back to the end of the shorter month.
- **Classification.** Genuine ambiguity, recorded by the encoder as fork N4. It took the last day so that it agrees with row IL-05's F19.
  The month counts themselves (D-01 to D-39c) are not affected.
  The rule that computes this day carries no `@export`, so only a composing row that calls it (such as IL-05 for s 342(ג)(2)) inherits the choice.

### 6. 72-14 (line 120): refused

- **Scenario.** Entitlement arose on 1 October 1995, the day the consolidation commenced (s 402: "תחילתו של נוסח משולב זה היא ביום ז׳ בתשרי התשנ״ו (1 באוקטובר 1995)"). Is October 1995 paid?
- **Provision.** s 72(א), first limb ("עד 15 בחודש פלוני, תשולם הקצבה החל ב־1 באותו חודש").
- **Expected.** Paid from October 1995.
- **Answered.** REFUSE: "this row answers months of the child allowance from May 2015, the period row IL-06 answers".
  The unexported first-month rule does compute October 1995 (the assertion that follows line 120 is satisfied).
- **Classification.** A choice about scope, recorded by the encoder as assumption A2: the row composes with IL-06's period.
  This is not a misreading of s 72. The encoder and I agree that s 72 carries no amendment tag, so its own text answers this month.
  It is a refusal where the source does answer, which a downstream reader should know about.

### 7. 72-30, the export asked about May 2008 (line 171): refused

- **Scenario.** A child born on 1 May 2008: is May 2008 paid?
- **Provision.** s 72(א), first limb.
- **Expected.** Paid.
- **Answered.** REFUSE, for the same reason as item 6.
- **Classification.** The same scope choice (A2).
  The same cause puts every start month in 72-30 to 72-39 (2008 and 2010) out of reach of the export. Those start months were therefore asserted through the unexported s 72(a) rule, and all of them are satisfied.

## The right answer for a different reason

72-60 (entitlement arising in January 1995) and 335-R2 (a 1990 contribution period) are both refused, as decided, and both assertions are satisfied.
The encoding refuses them because of its May 2015 and January 2026 gates, not because they fall before s 402's commencement on 1 October 1995.
No test can tell those two reasons apart. The refusal messages name the period the encoding chose to compose with, not the commencement of the Law.

## Expectations that could not be expressed (8)

| id | expected | why it cannot be expressed |
| --- | --- | --- |
| 72-39 (end) | REFUSE: does a child born on 29 February turn 18 on 28 February or 1 March 2026? | The day entitlement ceases is an input, so the caller has to choose one. The 18th birthday is row IL-06's question (`NOTES.md` §7). |
| 72-42 | REFUSE: is six days elapsed (seven calendar days counting both ends) "שבעה ימים"? | s 72(ב) is a single boolean input (A4), and the encoding answers whichever way the caller sets it (probe: TRUE pays March, FALSE does not). It is not recorded as a fork. |
| 72-44 | No, on the literal words, for a child born at home and never in hospital | The same boolean input. The question is the caller's, and it is not recorded as a fork. |
| 335-13 | The same answer as 335-06 | There is no Chapter 3 field, which is (ט)'s own rule ("בין שהוא מבוטח גם לפי פרק ג׳ ובין שאינו מבוטח לפיו"). It is consistent by construction. |
| 335-R1 | REFUSE: the rate of contributions | No rule answers it (s 337 and Schedule J are out of scope), so nothing is answered that should have been refused. |
| 335-R4 | REFUSE: who pays | No rule answers it (s 342 is out of scope). |
| D-R1 | REFUSE: Part D's age for a man | The rules take no sex. Their names say "a woman", which limits the risk. |
| D-R2 | REFUSE: Part D as in force on 1 January 2003 | No rule takes a date (assumption A1). |

335-R3 needs no assertion. The export is labelled as s 335 alone ("under National Insurance Law s 335"), and RD-6 accepts that; 335-07 asserts the answer s 335 gives on its own.

## Expressed only because the caller answers the scenario's own question

These assertions are satisfied, but each one tests only how the encoding maps its inputs to an answer. None tests the reading the scenario was written to check:

- 72-30 to 72-38: the "turns 18 on" column (RD-3). The 18th birthday is supplied as the day entitlement ceased.
- 72-29: s 1 "ילד", excluding a married minor. The day of the marriage is supplied as the day entitlement ceased.
- 72-40, 72-41 and 72-43: s 72(ב). The caller supplies TRUE or FALSE.
- 335-16, 335-17 and 335-19 (s 238, housewife), and 335-18 and 335-20 (s 238, housewife and widow pensioner). The s 238 statuses are inputs.
- 335-11, 335-12, 335-14 and 335-15: the age limits, the police exclusion and the long-term-care route for an immigrant. All of them reach s 335 only through the Chapter statuses the caller supplies.
- The "last day paid" columns (72-20 to 72-29 and 72-50 to 72-56). The encoding answers by month, so these are asserted as "that month is paid and the next is not". The leap-day last days (72-25, 72-26 and 72-53) are therefore tested only at month granularity.

## Silent paths (no failure, exit 0, no diagnostic)

- **s 72's "was paid" input is never checked against s 72(א).** If a child dies before the encoding's own first month, a caller's TRUE still produces three months under (ג) (72-57, line 248). The encoding has what it needs to detect that the window is empty.
- **Part D's day rule moves a non-existent day without saying so.** The fork is recorded in N4, but the caller gets no sign that the day was moved.
- **s 72's May 2015 gate sits only on the export.** The unexported first-month and last-month rules for s 72 take no gate. A composing row that calls them directly gets answers before May 2015 that the export would refuse (for example, October 1995 for 72-14). Part D has no period gate anywhere (A1), so it has nothing to bypass.

## Errors of my own

- **RD-9 in `DECIDED-ANSWERS.md` is incomplete.** It says s 335 and Part D carry no date of their own. In fact the heading of s 335 carries "תיקון: תשנ״ו, תשס״ג־8, תשע״ז־12, תשע״ח־5" (line 3610), and Part D carries "תיקון: תש״ף" and "תיקון: תשע״ז־12" (lines 4432 and 4433).
  No expected value depends on it. The appended section "Revised after seeing the encoding" in `DECIDED-ANSWERS.md` says so.
  I found this by reading the encoding's quotation of line 3610.
- **72-57.** On reflection, REFUSE is probably more cautious than the source requires (see item 1). I have left the assertion failing, as decided.
- **The draft I inherited checked six s 335 scenarios too weakly.** This is fixed in the delivered file.
- **The encoder's `tools/hebcheck.py` flags six quotations in the frozen part of `DECIDED-ANSWERS.md`** (lines 16, 33, 115, 129, 132 and 133). Run as `python3 -I tools/hebcheck.py SOURCE FILE`, it exits 1 on that file.
  Each of the six is either an elision marked "..." or a definition whose quote marks were dropped. I checked each one against source lines 807, 854, 3611, 2428 and 2429, and none adds words the source lacks.
  They are left as they are because that part of the file is frozen. This file, the appended section and `tests-independent.l4` pass the check.
- I withdraw none of the five failing assertions.

## What I read, and what I perhaps should not have

The second session read these files:
- `DECIDED-ANSWERS.md`;
- `run1.txt` and `run2.txt` (diagnostics for the draft only);
- the draft `tests-independent.l4`;
- `BRIEF.md` and `check.sh`;
- the four rule modules;
- a copy of `second-pass.md` (from the worktree `l4wt/shrug`);
- lines 853–856, 3610, 4315, 4367–4369, 4431–4433, 4437 and 4444–4446 of the deposited Law;
- `NOTES.md`, only after the tests were final.

The comments in the rule modules name the encoder's forks and assumptions ("fork N1", "IL-05's fork F19", the May 2015 and January 2026 periods). So part of the encoder's reasoning reached me before `NOTES.md` did. That was after `DECIDED-ANSWERS.md` was frozen, and it changed no expected value.
I opened nothing under `/Volumes/transcend/src/Axiom/`, no `rulespec-*` directory, nothing from the Axiom Foundation, no `ENCODING-GAPS.md`, no `.axiom/`, no `tax-benefit-source-map.json`, nothing named `composed/`, and no other row's `NOTES.md`.
I cannot vouch for anything the first session read beyond what its own header in `DECIDED-ANSWERS.md` records.
