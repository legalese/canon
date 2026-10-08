# IL-25 independent findings (BACKLOG IL-56), fid-il-25

DECIDED-ANSWERS.md was written from the Hebrew sources alone and frozen before the encoding was opened; sha256 `ca4fee908677c7fd0720382e967d8ce9dd1482180d060c54a64176fcad1434a5`.
The tests are in `tests-independent.l4` (74 assertions for 80 decided cases; ids C01 to C80 as in DECIDED-ANSWERS.md).
`check.sh` result: tests-independent.l4 0 errors, 67 satisfied, 0 failed, 7 refused (declared in check.sh), exit 0; l4 sha256 `f0759b2ef2f1d1b2a577c68f059c54f487de9d913553fc9f0d9bf0f7f5dab0d8` before and after.

## Summary

Every one of the tester's 2026 values (rates, tier edges at 7,702, 7,703 and 7,704, the cap, the minimum amount, the pensioner amounts, benefits, early pension, exemptions, the temporary provision for exempt income) matches the encoding to four decimals when the encoding is run under the tester's reading of each fork.
There is no OURS-WRONG finding and no TESTER-WRONG finding.
The only disagreements are SCOPE (months before 2026) and AMBIGUITY (the encoding declines by default where the tester took a reading).

## Disagreements

- SCOPE, C66 to C71 and C73 (assertions at lines 248, 250, 252, 254, 256, 258, 260): the tester asserted values for January, February and December 2025, the 7,522 edge, a capped 2025 wage and a 2024 wage at 3.1%; the encoding refuses every month before January 2026 ("this row answers contribution months from January 2026").
  The Hebrew supports the tester's 2025 arithmetic: 3.23% on the first 7,522 (note to NIL s 334(a)), 5.16% in January 2025 and 5.17% after (notes to s 14(b), (c)), cap 5 x 10,139 = 50,695 (note to NIL s 1 "basic amount" para (3)).
  Example: 2025-06, wage 10,000: 242.9606 + 2,478 x 5.17% = 371.0732.
  The encoder's reason is that the pre-2026 rate history is only in editorial notes; the tester accepts that as a scope choice but notes that the 2025 figures are deposited in the NIL text.
- SCOPE, C40, C72, C74, C75: the tester expected a refusal (published figure needed), and the encoding refuses; the assertions are satisfied.
- AMBIGUITY, A1 (cap), A3 (reduced tier for benefits and early pension), A4 (pensioner with wages): the tester took a reading; the encoding's default declines and offers the same readings by name.
  All three agree numerically with the tester when the named reading is chosen (C09 to C12, C21, C28, C41 to C44, C47, C48, C39).
  A2 (the reduced tier does not reach a non-worker) is a text decision in the encoding (T2) and agrees with the tester (C27, C28, C79).
- SCOPE, not tested because not encoded: C46 (the State's payment on special adaptation allowance, (d)(4), flat 5.17% by the literal text), C60 (organ donor: the period set by the Minister, taken as an input), C76 (the 1995 exemption regulations of (h)/(i)), C77 (an employee who is also self-employed, A5), C78 and A9 (rounding, the encoder's open question 4).
  The conclusions of NIL ss 238 and 351 (agunah, month three after discharge, a student's income test; C53, C54, C56 to C59) are inputs to the encoding, so the tester passed the flags that follow from the Hebrew and the test checks only s 14's use of them.

## What the encoder read in the source

The quoted Hebrew and the figures were checked against the deposited files: the reduced amount 7,703 (NIL s 334(a) note), the maximum 5 x 10,382 = 51,910 (NIL s 1 note, Schedule 11 items 1, 2), the minimum 123 and the pension amounts 237 and 340 (notes to s 14(a), (e)(2)), the rates 5.17% and 3.23%, the (g2) period 1.1.2026 to 31.12.2035, and the exemption list of (g) and (g1).
No misreading found.
One observation, not an error: the encoding's department of the "neither" class puts a computed amount of nothing through the minimum automatically, which agrees with (c)(2)'s proviso (C23 to C26).
