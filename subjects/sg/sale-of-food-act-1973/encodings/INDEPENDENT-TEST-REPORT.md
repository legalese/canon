# Independent test report: Sale of Food Act 1973 encoding

## Method

1. I read `BRIEF.md` and `../source/SFA1973.txt` in full and fixed 129 numbered expectations (E1-E129, several with sub-cases) in `independent-expectations.md`, before opening any `.l4` file. They have not been changed since.
2. I then read `sfa-types`, `sfa-definitions`, `sfa-offences`, `sfa-procedure` and `sfa-goal` for names and inputs, and wrote `tests-independent.l4`. I looked at `sfa-tests.l4` only for syntax.
3. I ran `L4=~/.local/bin/l4 ./check.sh` and searched `l4 run tests-independent.l4` for warnings and refusals.

## Counts

| | |
|---|---|
| Assertions in `tests-independent.l4` | 139 |
| Passing | 139 |
| Failing | 0 |
| Refusing (warnings / REFUSE) | 0 |
| Error diagnostics | 0 |
| Expectations that cannot be expressed against the encoding's inputs (wholly or partly) | 23 (listed below) |

`check.sh` total across the encoding: 0 errors, 226 satisfied, 0 failed. That is 87 from `sfa-tests.l4` and 139 from this file.

## Disagreements in asserted values

None. Every expectation that could be stated against the encoding's functions came out as I expected.

## Disagreements that can't be asserted because the encoding has no input for the distinction

In these cases the encoding answers the coarser question, and that answer differs from mine:

| E | Provision | My expected value | What the encoding gives | View |
|---|---|---|---|---|
| E69 | s 10K(1) "without reasonable excuse" | Failing to comply with a direction **with** a reasonable excuse is not an offence | `failing to comply with a food safety direction` always contravenes (`OTHERWISE TRUE`); there is no reasonable-excuse input | Gap. Add a `reasonable excuse` field. |
| E70 | s 10K(3) "while that direction remains in force" | Removing the affixed copy after the direction has ended is not an offence | `removing a direction affixed to food premises` always contravenes; it is not linked to the s 10B(5) in-force rule | Gap. Add an in-force flag, or a date checked with `the direction is in force on`. |
| E76 | s 41(2) "without authority" | Breaking a seal **with** authority is not an offence | `obstructing an officer, or interfering with an official mark` always contravenes | Gap. Add an authority flag. |
| E79 | s 6(3) | A retailer who refuses to sell less than a whole unopened retail package commits no offence | `refusing to give a sample` always contravenes | Gap. The s 6(3) limit on the demand is not modelled. |
| E81 | s 7(1)(b) | For food other than milk, a refusal is no offence without the purchaser's request or consent, because no power arises | `refusing to give a sample` always contravenes; milk and other food are not distinguished | Gap. |
| E54 (second half) | s 18 "to the prejudice of the purchaser" | No offence where the purchaser is not prejudiced | The conduct only exists as "... to the purchaser's prejudice", so prejudice is assumed | Acceptable as an input, but the negative case cannot be stated. |
| E22 | s 2E(3)(b) | Food donated for a charitable purpose is not "given away for advertisement", so it is not a sale | `Kind of supply` has no value for this case. The s 2E(1) classification is wholly an input. | Simplification. All of s 2E(1) and (3) is left to the caller. |
| E84 (second half) | s 46(6) "any licence granted is void" | The licence is void | Only the offence is modelled | Gap. |
| E90 | s 56(1)(r) "every day or part of a day" | 2 days and part of a third day count as 3 days: $6,500 | Only the per-day rate ($500) is returned. There is no day-counting function, and part-day rounding is not encoded. | Gap. E89 (whole days) passes when the test does the arithmetic. |
| E116 / E117 (suspend/cancel limb) | s 46(12)(c) | The Director-General may suspend or cancel for either limb | Only the financial-penalty cap is computed | Gap. The penalty limb is right. |

## Expectations that cannot be expressed, or only trivially

- **E9, E10** (s 2A(4), (5)): no input for fitness or for being alive. These pass only because "for human consumption" is the input.
- **E20, E21, E24, E25** (s 2E(1)): the caller supplies `a sale or other dealing listed in s 2E(1)`, so these tests are tautologies.
- **E28, E29, E30** (s 2B): commercial/charitable nature, one occasion, intermediary and furniture hire all collapse into two input flags.
- **E56**: trivial.
- **E94** (s 31): there is no input for "bought for analysis", so the defence can never be raised. The encoding is correct by omission, but this can't be tested.
- **E103** (s 27(a)): the principal-liability function returns its input unchanged.
- **E122** (s 10J): the period is "prescribed". The encoding returns NOTHING, which is right, but nothing more can be checked.
- **s 33(4)** (an employee or agent relying on the employer's warranty): not encoded, so not tested.

## What the encoding misses or simplifies

1. **s 2F "but includes".** The field is called `has a non-retail component`, but the Act's wording is "a food business a component of which is [a retail purpose]". The rule `NOT retail OR non-retail component` gives the right answer for a mixed business (E35 passes). However:
   - the label inverts the Act's wording;
   - the primary-production exclusion (b) is kept even for a mixed business that the "but includes" clause might capture.
2. **s 2A.**
   - (2)(b), seeds for planting, has no input.
   - (4), fitness, has no input.
   - Exclusions are a single enum, so an article cannot be both, say, declared food and excluded. That is fine, because exclusions win.
3. **s 2C(2) and s 2D(2).** Each subsection is a single "only because of ..." flag. s 2D(2)(b)'s rider, "so long as it does not contain the chemical ... in an amount that contravenes any food regulations", cannot be expressed.
4. **s 2E(3)(a)-(e).** The deeming rules (display for prizes, mixing, human-consumption presumption) and the s 28 presumptions are carried only as text.
5. **s 16A(4)-(5).** The presumption that an advertisement is false is not encoded. s 16A(7)(a)-(c) are merged into one flag, which is fine for outcomes.
6. **s 32 scope.**
   - All s 40 conduct counts as "a prosecution for selling" (`OTHERWISE TRUE`), but s 40 also covers importing and advertising.
   - s 16A advertisement prosecutions are excluded from s 32, although s 16A(6) says "Without affecting section 32". This is arguable both ways.
7. **s 56(1)(r).** This sets a ceiling for what regulations may provide. The encoding reports it as the maximum penalty for "contravening food regulations", whereas the actual penalty is whatever the regulation fixes (up to that cap).
8. **s 46(9).**
   - The caller has to convert days to fractional months; the encoding only applies `CEILING`.
   - The proportionate fee is discretionary ("may"), but the encoding computes it as if it is always charged.
9. **s 4(2).** The caller supplies elapsed hours; there are no date/time inputs.
10. **s 10I(7)** (the bar on late applications) is not encoded.
11. **s 5(6)** (the purposes that limit the information power) and **s 6(3), s 7(1)(b)** (the limits on the sampling powers) are not encoded. As a result, refusals are always offences.
12. **s 22(6).** Grounds (a)-(d) are correct. The input "knowingly employs" puts the knowledge finding on the caller.
13. **No REFUSE anywhere.** The brief asks for `REFUSE` where the source does not answer, for example s 10J's prescribed period or the District Court limit. The encoding uses NOTHING or input parameters instead. None of my tests needed a refusal.
