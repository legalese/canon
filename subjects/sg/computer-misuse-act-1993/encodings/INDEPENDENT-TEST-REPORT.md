# Independent test report: Computer Misuse Act 1993 encoding

- Expectations: `independent-expectations.md`. They were written from `BRIEF.md` and `../source/CMA1993.txt` before any `.l4` module was opened, and have not been changed since.
- Tests: `tests-independent.l4`. It imports prelude, daydate and all seven `cma-*` modules except `cma-tests`.
- Run: `L4=~/.local/bin/l4 ./check.sh` (toolchain `~/.local/bin/l4`).

## Counts

| | |
|---|---|
| Assertions in `tests-independent.l4` | 134 |
| Satisfied | 133 |
| Failed | 1 |
| Other errors (syntax, type, plumbing) | 0 |

The other modules were unaffected by this run. `cma-tests.l4` has 92 satisfied assertions and no errors, and the remaining modules have none of either.

The assertions cover every scenario group in the expectations file:
- A: definitions, s 2
- B: offences, ss 3-10 and 12, including both s 9 Examples
- C: punishment, s 11 and caning
- D: reach and procedure, ss 13-17 and 19
- E: the vintage gate

Each scenario was checked by at least one assertion, except two that the encoding's types cannot express. Both are noted below.

## The failing assertion

### D11: s 14(1)(c) amalgamation at exactly 12 months

- **Scenario.** Two acts, each an offence under s 3, on the same computer. One was committed on 1 January 2026 and the other on 1 January 2027.
- **Expected:** they may be amalgamated. Under s 14(1)(c) the acts must be "committed in a period that does not exceed 12 months". The span from 1 January 2026 to 1 January 2027 is a period of exactly 12 calendar months. A period equal to 12 months does not *exceed* 12 months.
- **Encoding:** FALSE. `the acts may be charged as one offence` (in `cma-scope-procedure.l4`, fork F2) requires the last act to fall strictly before `add months first 12`. It counts both the first and the last day, so it treats 1 January 2026 to 1 January 2027 as 12 months and a day.
- **My view.** The source does not say how the period is counted, so both readings can be defended. I prefer mine for two reasons:
  - The usual way to count time excludes the day of the first event. Section 50(a) of Singapore's Interpretation Act 1965 does this, but that Act is outside the source and is cited here from general knowledge. On that basis the period is exactly 12 months.
  - "Does not exceed" is the language of an inclusive ceiling.

  The encoding's inclusive count gives the narrower reading, which is the one that favours the accused. That is a legitimate choice, but it should be argued in NOTES fork F2 rather than assumed. At minimum, F2 should name the date-arithmetic convention it uses and say why that convention was preferred. The two readings differ on only one day, the anniversary itself.

## Where the encoding's types could not express a scenario

1. **A25: loss accruing more than a year after the offence (s 2(1) "damage" (a)).** `Impairment facts` accepts only `loss caused, in dollars, within one year after the offence`. The caller has to apply the one-year exclusion and the aggregation before passing the figure in. My test passes $6,000, which is the result of applying the exclusion by hand, and it passes. The proviso itself, though, is not a computed rule. Taking dated loss items and letting the rule sum and filter them would encode the limb faithfully.
2. **B33: personal information obtained by a s 7 contravention (s 9(1)).** The s 9 constructor takes one boolean, `knew or had reason to believe it was obtained in contravention of s 3, 4, 5 or 6`. The rule therefore never sees which section the contravention was under, and "3, 4, 5 or 6" does no work in the code. The same applies to s 10(1) and its "3, 4, 5, 6 or 7". These tests pass only because the caller answers the question.

## Other observations (not assertion failures)

- **The vintage gate is only at the top.** Only `the computer misuse position for` refuses conduct before 30 December 2025. The goal functions take no date, so they answer for 2020 conduct without refusing: `the elements are made out`, `the maximum punishment for`, `the caning strokes for` and `the Act reaches the conduct`. That matters most for caning and s 8A(1), both of which Act 21 of 2025 introduced or recast. A caller who calls the goal functions directly gets answers the brief says should refuse.
- **Arrest and composition in the top-level goal.** These are keyed to `the offence is made out`. Section 19 (arrest without warrant) and s 16(1) (composition from "a person reasonably suspected") turn on reasonable suspicion, not on the elements being proved. The goal's `arrestable without warrant` and `most that may be collected to compound` are therefore narrower than the Act.
- **Section 12(2)** ("immaterial where the act in question took place") plays no part in the s 13 territorial test. The participation field is ignored throughout. This is probably harmless, but it means s 12(2) is not encoded.
- **Section 14(4)** (the charge must give further particulars if needed) and **s 17(3)** (compensation is recoverable as a civil debt) are not computed. Neither has much to compute.
- **Section 8A(2) and s 9(6)** are evidential and are rightly not treated as elements.

## Where my readings agreed with the encoding

These are the contested points where the encoding and my source-only expectations matched:
- **$10,000 damage edge:** "at least", so $10,000 counts and $9,999.99 does not.
- **s 4(2):** "not less than 2 years" read as a maximum term of at least 2 years.
- **No repeat-conviction limb** in s 4 or s 8A.
- **Damage limbs:** only ss 3, 5, 6 and 7 have one, and it applies whether or not the conviction is a repeat.
- **s 11:** covers ss 3, 5, 6 and 7 only, not s 4 or s 8, and applies "in lieu" even with damage or a repeat conviction.
- **s 11(3) presumption:** whether it stands, and whether it is rebutted.
- **Caning:** limited to individuals, with the reasonable-steps answer in s 8A(5)(b)(ii) and s 8B(5B)(b)(ii).
- **s 8B(5A):** applies only to the (1)(a) limb.
- **s 8B(3) and s 9(3):** both conditions must hold for the exception to apply.
- **s 8B(4) and s 9(4):** the mere-conduit exception.
- **Both s 9 Examples.**
- **s 13(3)(b):** excludes ss 8A, 8B, 9 and 10, while (d) always reaches ss 8A and 8B.
- **s 16:** the $3,000 ceiling.
- **s 17(2):** the remaining balance, with a floor of zero.
- **Vintage gate:** 29 December 2025 and earlier refuse, and 30 December 2025 is answered.
