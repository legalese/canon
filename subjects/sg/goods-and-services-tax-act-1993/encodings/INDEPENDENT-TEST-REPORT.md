# Independent test report: GST Act 1993 encoding

## Method

I wrote the expectations from BRIEF.md and `../source/GSTA1993.txt` before opening any module. There are 195 of them (E01-E195), in `independent-expectations.md`.

Only then did I read the `gst-*.l4` modules, for their names and input shapes. I did not read `gst-tests.l4`.

The assertions are in `tests-independent.l4`, and each carries its E-number. I changed no expected value after reading the encoding.

## Counts

| | |
|---|---|
| `#ASSERT` lines in `tests-independent.l4` | 243 (includes 1 `#ASSERT REFUSED`) |
| Satisfied | 241 |
| Failed | 2 (E38, E166) |
| Refused where a value was expected ("assertion refused" warnings) | 0 |
| `#ASSERT REFUSED` that produced a value | 0 (E22/E193, s 16 before 2003, refuses as expected) |
| Compile or other errors | 0 |
| Expectations asserted, wholly or in part | 174 of 195 (E20 and E105 by approximation) |
| Expectations not expressible at all | 21; a further 5 are only partly expressible (E123, E126, E160, E189, E112's agreed-date variants). All are listed below |

Without my file, `check.sh` reports 0 errors, 177 satisfied and 0 failed across the encoding's own modules.

`l4 run tests-independent.l4 | grep -i warning` prints nothing.

## Disagreements

### E38: the reverse charge carries no tax at the top-level goal (encoding wrong)

**Scenario.** A supplier belonging abroad supplies $10,000 of services on 1 Mar 2025. The recipient is a partly exempt Singapore business that is registered.

**What the encoding gives.** `the GST position for` reports:
- treatment `outside the scope of the tax`;
- `tax on the supply` = JUST 0;
- `the recipient accounts under the reverse charge` = TRUE.

**Why that is wrong.** Section 14(2) says that "all the same consequences follow ... as if the recipient had himself, herself or itself supplied the goods or services in Singapore ... and that supply were a taxable supply". Section 17(3A) makes the value equal to the consideration, and s 17(2A)(a) disapplies the tax-fraction rule. So the tax should be 9% on top of $10,000, which is $900.

The goal module has two problems:
- It never computes the reverse charge tax.
- Even for an in-scope supply, it always extracts tax with the s 17(2) fraction, which would give $743.12 here instead of $900.

No function anywhere in the encoding gives the value of a reverse charge supply.

### E166: when an advance ruling ends (both sides off)

**What the encoding gives.** `an advance ruling applies until, made` 1 Mar 2025 = 1 Mar 2028, which is `add years` 3.

**What I expected.** 28 Feb 2028. That was my own arithmetic slip: 2028 is a leap year.

**The correct answer.** The 3-year period "beginning on the date the ruling is made" (Fifth Schedule Part 1 para 6(b)) runs from 1 Mar 2025 to 29 Feb 2028 inclusive.

**Why I left my value in place.** I kept 28 Feb 2028 as written, under the rule against editing expectations.

**What the encoding should change.** The encoding's 1 Mar 2028 is the first day *outside* the period, yet the function is named "applies until". It should either return 29 Feb 2028 or be renamed to say the date is exclusive.

The same exclusive-versus-inclusive question does not arise for the other `add years` deadlines I checked, all of which are correct:
- s 45(5) assessments;
- s 46(2) records;
- s 90(1B) refunds;
- Third Schedule para 1(2) directions.

The difference is that their wording is "not more than N years after" or "within N years after", where the anniversary itself is the last good day.

## Expectations I could not express

The encoding has no name for these, or has the fact only as an input that makes the test trivial.

### Belonging and place

- **E19.** Section 15(4) and (5): where a *recipient* belongs, including an individual's usual residence. Only the supplier test in s 15(3) exists. E20 is asserted by approximation, through the supplier enum.

### Value

- **E37.** Section 17(3): the open market value for non-money consideration. There is no path for it. `the tax treatment of` sends any supply with `for a consideration` = FALSE outside the scope. That also sends Second Schedule para 5(1) and (3) deemed supplies ("whether or not for a consideration") outside the scope, which is wrong.

### Reverse charge and the Seventh Schedule

- **E65.** Section 14(3A): no reverse charge to the extent that tax was already paid to the overseas vendor. There is no field for it.
- **E70, E71, E75.** Whether a supply is a Seventh Schedule supply (para 3(2) and (3A)). This is a boolean input on `Supply`, never derived.
- **E74.** A pure ISP is not an operator (para 1(2)). The marketplace function takes only a count of conditions.

### Second and Third Schedules

- **E78.** Second Schedule para 5(4): a gift is not a supply where no input tax credit was allowed. The gift function has no parameter for this, so it treats a $500 gift as a supply even where no credit was ever allowed.
- **E82.** Second Schedule para 7(2): the same carve-out for deregistration. It is missing from the deregistration function.
- **E84.** Third Schedule para 14 excludes the s 23 margin scheme. The special-value enum cannot express a margin-scheme vehicle.
- **E86.** Para 10(2): employees who pay money. The enum only has "no money paid".
- **E90.** The conditions for an open market value direction (Third Schedule para 1(1), (1A)). Only the time limit is encoded.

### Rate changes

- **E97.** Section 39B(4): no election for a para 6 supply.
- **E98.** Section 39A(5): Division 1 does not apply to a change on or before registration.

The s 39B and s 39C functions also never check their own triggers. E94 (fully paid and performed before the change) returns the right number only by coincidence.

### Registration and special persons

- **E105.** The capital-asset exclusion in para 1C(2) is left to the caller. I asserted only the threshold.
- **E112.** I asserted this, and the encoding agrees with my day X + 31 reading. Note that para 5(3) and (4) (the Comptroller may register from day X) and the "earlier date agreed" in paras 4(2)(b) and 5(2)(b) have no parameter.
- **E119.** The effective date on a going-concern transfer (para 6(2)) has no function. The notification deadline is asserted.
- **E123.** The date nuance of s 31(3): the deeming stops on the notification date. The function is boolean only.
- **E126 (second half), E127.** The s 33(1B)(b) and (c) deadlines (30 days after appointment; 30 days before a change) have no function.

### Assessment, refunds and collection

- **E148.** The s 47(2A) 5-year limit on adjustments has no function of its own. It is only mentioned in the records function's `@ref`.
- **E158.** Section 90(1A) covers only periods ending on or after 1 Jan 2007. `the last day to claim a refund` adds 5 years to any date and never signals the cut-off.
- **E160 (partial).** The 14-day notice, 28-day objection and 7-day relay steps in s 79(4) have no functions. The 42-day step is asserted.
- **E161.** Section 83E arrest powers (who may arrest for which offence) are not encoded. Only s 83E(7) detention hours exist.

### Offences and discretions

- **E189 (partial).** The s 6 secrecy offence is not in the `GST offence` enum, so the encoding cannot be asked about Public Prosecutor consent for s 6.
- **E194.** The composition amount below the $5,000 cap is a discretion; there is nothing to assert.
- **E195.** The Fourth Schedule classification is an input.

## Simplifications and gaps I noticed (not asserted as failures)

1. **The s 14 election flag is shared.** The encoding uses one boolean, `recipient elected under s 14(5) or (6)`, to override both the full-credit condition and the Eighth Schedule exclusion. But the two elections are separate:
   - s 14(5) overrides only the full-credit condition;
   - s 14(6) overrides only the exclusions, and is open only to a registered recipient.

   A fully-creditable recipient that made only an s 14(6) election would wrongly be caught.
2. **Partial coverage is lost in time of supply.** Sections 11(2), 11(3)-(4), 11B(3) and 11A(6) all apply "to the extent covered" by an invoice or payment. The encoding returns a single date, so partial coverage (part invoiced, part not) cannot be represented.
3. **The s 73A test reads only the imprisonment field.** It asks whether imprisonment is 12 months or less. As a result:
   - s 59(1), which carries a penalty but no fine or imprisonment, counts as eligible;
   - the s 58 "imprisonment in default" of 6 months is stored as an ordinary prison term.

   Both are arguable, but the field conflates the two kinds of imprisonment.
4. **Fines are recorded as penalties.** The fines in s 62A ("fine of an amount equal to the tax") and s 62B ("fine equal to 3 times") go into `penalty as a multiple of the tax`, alongside true penalties. The label is misleading, though the numbers are right.
5. **Prospective registration totals omit some supplies.** For a Singapore-belonging person, para 1(1)(b)(ii) adds Seventh Schedule para 3(2)(b)(ii)/(3A) supplies. That is left to the caller's total and not mentioned in the input name.
6. **The tax treatment ignores the reverse charge.** `the tax treatment of` cannot express a reverse charge supply as standard-rated (see E38).
7. **The s 60(1)(b) inputs are a fork.** The additional late-payment penalty needs both "days after the 5% penalty" and "completed months since due" as separate inputs (FORK F3). This matches my reading of the text, which counts months "commencing from the date on which the tax became payable".

## Agreement worth recording

The encoding matched every threshold and date edge I set where it has a function:
- the s 16 rate boundaries;
- $400 / $400.01 for distantly taxable goods;
- $200 for business gifts;
- $10,000 for deemed supplies on deregistration;
- $1m and $100k "exceeded" limits;
- the 1 July 2025 change to the registration effective date, including the 31-to-28 Feb and 30-to-29 Feb (2028) clamps;
- the s 41(7) $5 de minimis, both ways;
- the 5- and 7-year assessment and record limits;
- the s 54 $500 limit;
- the s 50(6)/(6A) Board constitution;
- the advance ruling fees, including part hours and the 3x expedited cap;
- all 25 offence maxima.

## Triage by the encoder (2026-10-10)

- **E38: fixed.** The top-level goal now treats a reverse-charged supply as standard-rated, with the tax on top of the consideration. E38 passes.
- **E166:** the encoding was corrected to return the last day (29 Feb 2028). E166's expected 28 Feb 2028 is the report's own leap-year slip, so it stays as an expected failure, unchanged.
- **Also fixed:** s 73A eligibility; deemed supplies in scope; s 90 refunds before 2007 refuse.
- **Plumbing:** the renamed field `for a consideration, or deemed a supply by the Second Schedule` in this file's supply builders. No expected value was changed.
- **The other simplifications are listed in NOTES.md §4.**
