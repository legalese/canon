# IL-06 independent findings (fid-il-06)

Independent test author's report on `legalese-2026-10-il-06` (National Insurance Law ss 65-68, the child allowance).
The expected values come from `DECIDED-ANSWERS.md`, finished at 2026-10-06 15:03:48 UTC before any `.l4` file or `NOTES.md` was opened.
The assertions are in `tests-independent.l4`.
`NOTES.md` was read only after the module had been written and run.

## The run

`/Users/mengwong/.local/bin/l4 run tests-independent.l4` in a scratch copy of the encoding directory, `JL4_LIBRARY_PATH` unset, on the delivered bytes (sha256 `aca1bfc1af17e24e7c0e4b15512d1acb09818a32acd7b1038bd58bc73c5f83da`), counted with `check.sh`'s own greps (the full `check.sh` was not run, because the machine was busy):

| module | errors | satisfied | failed | refused |
| --- | --- | --- | --- | --- |
| tests-independent.l4 | 6 | 140 | 6 | 0 |

146 `#ASSERT` directives: 140 + 6.
The 6 errors are the 6 failed assertions; there is no other error.
`l4 run` exited 0, which is why the diagnostics, not the exit code, are what count.
Of the 146, 144 assert values decided in DECIDED-ANSWERS.md (82 scenarios) and 2 (section X) were added after reading the interface, licensed by the same source text.

Each refusal that passed was also probed with `#EVAL` in a scratch module, to confirm it refuses for the right reason (a bare `#ASSERT REFUSED` accepts any refusal).
Each one did:

| scenario | the encoding's refusal |
| --- | --- |
| F1 two mothers | "section 67(b) does not say in whose count a child is counted whose two insured parents are both its fathers or both its mothers" |
| F2, F3 natural parent and step-parent, with both / neither | "section 67(b) does not say in whose count a child is counted who has a natural parent and another insured parent and is with both of them, or with neither" |
| F5 children by several women | "section 69A, for an insured man with children by more than one woman, displaces sections 67 and 68 and is not encoded in this model" |
| F6 the only parent ceased to be insured | "section 71, on the allowance paid by virtue of a parent who died or ceased to be insured, is not encoded in this model" |
| F11 three insured parents | "section 67(b) does not say in whose count a child with more than two insured parents is counted" |
| E1 30 April 2015 | "this model answers days from 1 May 2015, when sections 1 and 68 took their present wording; …" |
| E4 1 January 2027 | "the basic amounts for the child allowance from 1 January 2027 had not been published when this model's sources were fetched" |

## Failing assertions

Six assertions fail, from five findings.
None is my own error on reflection; four are genuine ambiguities (three of which the encoder recorded as forks), one is a minor encoding error.

### Finding 1 — one insured parent, child with the uninsured mother only (scenario F4)

- **Scenario.** Natural father F insured, natural mother M not insured; the child is with M only.
- **Provision.** s 67(b), line 818: "ילד שיש לו שני הורים, יבוא במנין האב המבוטח זולת אם הוא נמצא עם האם בלבד".
- **Expected.** A refusal. Read literally the child is *not* in the insured father's count ("unless he is with the mother only"), and the mother has no count, so the child is in no count; read structurally, s 67(b) arbitrates only between two insured parents, so with one there is nothing to arbitrate and the child is the father's. The text does not choose.
- **The encoding answered.** `JUST "F"`: the child is in the father's count (so 150 a month at the 2015 amounts).
- **Classification.** Genuine ambiguity, **recorded** by the encoder as fork F7 (its reading (ii) is exactly my literal reading) and as open question 2. The encoder's choice is defensible; mine is that a model should not pay in a case the text arguably sends to nobody without saying so at the point of the answer.

### Finding 2 — a 29 February birthday in a common year (scenario F8)

- **Scenario.** Child born 2008-02-29; day 2026-02-28.
- **Provision.** s 65(a) "ילד", proviso, line 807: "ולא מלאו לו 18 שנים".
- **Expected.** A refusal or a recorded fork: the Law does not say when a 29 February child completes 18 years in a common year. Both certain edges pass (a child on 2026-02-27, not on 2026-03-01).
- **The encoding answered.** Not a child on 2026-02-28 (the anniversary clamps to 28 February), total 0.
- **Classification.** Genuine ambiguity, **recorded** as fork F2 (clamp chosen as conservative) and open question 9. My assertion asked for a refusal; the recorded fork is the other outcome my decided answer allowed.

### Finding 3 — a six-month trip, a day in its first month (scenario F9; two assertions)

- **Scenario.** Child left Israel 2026-01-10 for a trip ending 2026-07-10; day 2026-02-01; no Institute decision.
- **Provision.** s 65(b), line 809: "לא יראו ילד כנמצא בחוץ לארץ אם יצא מישראל לתקופה שאינה עולה על שלושה חודשים; אולם המוסד רשאי לראותו כאילו הוא בישראל גם אם יצא מישראל לתקופה העולה על שלושה חודשים".
- **Expected.** A refusal or a recorded fork. The statute's "left Israel for a period exceeding three months" reads as the whole trip, so the child is abroad from the first day; the Institute's own page (`https://www.btl.gov.il/benefits/children/Pages/שהות בחוץ לארץ.aspx`, fetched 2026-10-06, sha256 `b86cea0a…679d`) applies it as "the first three months of the stay count" ("למשך 3 החודשים הראשונים לשהותו בחוץ לארץ", lost "החל בחודש הרביעי").
- **The encoding answered.** It depends on what the caller supplies. With the return day supplied: abroad, not counted, total 0 (the statute's reading). With the return day not supplied: in Israel, counted, total 150 (the Institute's reading).
- **Classification.** Genuine ambiguity, **recorded** as fork F3. Worth a reader's attention: the same child on the same day gets opposite answers depending on whether the question is asked before or after the return date is known. Fork F3 says so in its own terms; the answer table does not.

### Finding 4 — a resident "housewife" within s 238 (scenario F10)

- **Scenario.** A resident mother who is a housewife as defined in s 238 and is not insured under Chapter 11; one child with her.
- **Provision.** s 65(a) "מבוטח", lines 802-803: (1) "מבוטח לפי פרק י״א, למעט עקרת בית כהגדרתה בסעיף 238"; (2) "יחיד היושב בישראל, … ואינו מבוטח לפי פרק י״א, למעט עקרת בית כהגדרתה בסעיף 238".
- **Expected.** A refusal (or an explicit input that is not given a reading silently). Limb (2) has two parses: "and is not [insured under Chapter 11 other than a housewife]", which lets a resident housewife in through limb (2); or "and is not insured under Chapter 11; excluding a housewife", which keeps her out of both limbs.
- **The encoding answered.** "no child allowance, not being an insured parent": the second parse, in `nii-s65-interpretation.l4` (`… AND NOT the person's a housewife as defined in section 238` in limb (2)).
- **Classification.** Genuine ambiguity, **not recorded**: the fork register (F1-F17) has no entry, the coverage table states the exclusion as the meaning of limb (2), and the encoder's own test asserts it unlabelled (`#ASSERT NOT s 65 — insured (a housewife "Batya")`).
  On reflection (DECIDED-ANSWERS, "Revised after seeing the encoding", item 1) I think the encoding's parse is the weaker one: the phrase "מבוטח לפי פרק י״א, למעט עקרת בית כהגדרתה בסעיף 238" is one noun phrase repeated verbatim, limb (2) negates it, and the two limbs then partition residents, so a resident housewife is insured under limb (2). The practical reach is narrow (the s 238 housewife is a married woman, and with both parents insured and the child with both, the child is the father's anyway), but it decides cases where the child lives with the mother only.
  Recommendation: open a fork, keep the current reading if the encoder prefers it, and label the test.

### Finding 5 — an absence that ended before the day (added assertion X2)

- **Scenario.** Child left 2026-01-10, came back 2026-06-10; day 2026-09-01; the caller supplies that finished absence.
- **Provision.** s 65(a) "ילד", proviso, line 807: "ובלבד שהילד נמצא בישראל"; s 65(b), line 809.
- **Expected.** On 2026-09-01 the child is in Israel and is counted (150), or the facts are rejected as a problem the caller can fix; never a silent "abroad".
- **The encoding answered.** Facts accepted, child treated as abroad, total 0.
- **Classification.** Encoding error, minor, **not recorded**. `nii-il06-nouns.l4` (the `A child` comment) says the field is "the absence in progress on the day, if any (NOTHING when the child is in Israel)", and `a problem with the facts of` rejects an absence that begins after the day or ends before it begins, but not one that ended before the day. So a contract violation the validator could catch returns a wrong answer with no diagnostic. NOTES fork F3 also says a caller may supply a return day that is "past", which reads as inviting exactly this input. Fix: add "an absence from Israel ended before the day" to `A problem with the facts`, or treat a return before the day as no absence.

## Expectations that could not be expressed through the interface

One.
F7 (the child has been abroad more than three months and whether the Institute exercises its s 65(b) power is not known): the interface takes the decision as a required BOOLEAN with no "unknown". That meets the alternative my decided answer allowed (a required input with no default), so it is not a defect; it has no assertion.

## Agreements worth recording

These were my low- or moderate-confidence readings, decided before I saw the encoding, and the encoding reached the same answer independently:

- B15 (an insured father with income chargeable to additional tax keeps the child in his count; nobody is paid): encoder's fork F6, open question 1.
- B4 (both parents insured, child with neither: the father's count).
- B6, B7 (only the mother insured: her count wherever the child is): encoder's fork F7.
- C8 (the count is ordered eldest first by date of birth): encoder's fork F4.
- C26 (Income Support paid to the parent whose count is empty: no supplement): encoder's fork F14.
- A7, A8 (a married minor is not a child, through s 1): encoder's fork F1.
- D2 (18 years are completed on the 18th birthday).
- All 21 published-figure lookups (E3) and all per-year per-child amounts (E5) agree with the NII table I fetched myself (2026-10-06 14:59:55 UTC, sha256 `f873d1ef…1aec`). My bytes differ from the encoder's (`d1998550…4139`); the figures do not.

## What I read, and what I should not have

- Before finishing DECIDED-ANSWERS.md: the source's s 1 (lines 120-229) and ss 65-68 (799-835); also lines 840-859 (s 69(d) to s 73), read to check the brief's claim that s 69A and s 71 displace ss 67-68 rather than to borrow it; `BRIEF.md`; a plain `ls` of the encoding directory; the NII pages cited above.
- I did **not** open `NOTES.md` or any `.l4` file before finishing DECIDED-ANSWERS.md.
- After it, in this order: the eight rule and noun modules; the first ninety lines of the encoder's `nii-il06-tests.l4` (fixture helpers) and its destructuring lines, for syntax only; `check.sh`; then, after the run, `NOTES.md`, and a grep of the encoder's tests for "housewife" to see whether its reading was labelled.
- `BRIEF.md` states some readings in its summary (for instance that s 68(a)'s amount is "the basic amount fixed for that child"). I read it as permitted; it agrees with the source on every point I relied on, and none of my expected values is taken from it rather than from the Hebrew.
- Nothing from the Axiom Foundation, any `rulespec-*` repository, or any of the other banned paths was read, searched or fetched.
