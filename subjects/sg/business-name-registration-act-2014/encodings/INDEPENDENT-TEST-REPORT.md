# Independent test pass: Business Names Registration Act 2014

File: `tests-independent.l4` (imports `bnra-types`, `bnra-part1`, `bnra-part2-registration`, `bnra-part2-names`, `bnra-part2-register`, `bnra-part3`).

Method: expected answers were decided from `source/BNRA2014.txt` before any rule module was opened; the encoding was then read for names and signatures only.

## Result

`l4 run tests-independent.l4`: 599 `#ASSERT` written, 599 satisfied, 0 failed, 0 error diagnostics.
(One `#ASSERT` against a deliberately wrong value, in a scratch copy outside the repository, did report `assertion failed`, so the harness does detect failures.)
Eight `#TRACE` runs (deadline edges of ss 11(4), 11(7), 17(4), 22(1)) were read by hand: act on the last day gives FULFILLED, waiting one day past gives BREACH. They are not counted as assertions.

## Findings

None: no assertion failed.

## Edges covered

30 days (ss 8(7), 11(4), 11(11), 12(3), 12(4), 14(2), 16(5), 23, 27(2)), 14 days (ss 11(7), 11(9), 19, 20, 22, 39), 42 days (s 17(4)), 60 and 120 days (s 16(4)), 12 months (ss 17(7), 24(2)), 1, 2 and 6 years (s 17(2)), 3 months, 6 years, 1 year (s 17(3)), age 17/18 (s 11(2)), $1,000 / $5,000 / $10,000 and 12/24 months (all penalty provisions), the composition cap at half-maximum below and above $10,000, 3 January 2016 + 30 days (s 45(5)), every s 2(3) activity, every s 4(1) exemption and the s 4(3) choose-to-register carve-out.

## Not tested, or tested only partly

- Provisions that are inert or pure allocations of power with no condition (ss 1, 3, 26(4), 27(6), 29(1) and (4), 33(2), 44, 45(1), (3), (6), (7), (10) to (14)).
- Discretion actually exercised ("may" provisions are tested as availability only, as the brief requires).
- Regulative rules for ss 11(9), 11(11), 19(1), 20(1) and 20(3): the deadline is a bare `WITHIN 14/30` and was not traced; only the four traces listed above were run. No `#TRACE` result can be `#ASSERT`ed.
- The `Kind of Registrant` route for a limited liability partnership under s 11(1) (the section does not name it, so `FALSE` was asserted for a company only).
- s 2(1) "business" for a trade not carried on for gain (the relative clause "that is carried on for the purposes of gain" may attach to "any other activity" only): left untested as ambiguous.
- s 40(5) "officer" of a body corporate includes a "partner": the `Role in Body` list has no such role, so it was not tested.
- s 11(12) fixes a fine for failures under 11(1), (7), (9) only. A failure under s 11(11) has no offence in s 11(12); `Representative Offence Facts` has no field for it, so the negative could not be asserted.
- Leap-day anniversaries for `add months` (for example a dissolution on 29 February).
- Anything depending on regulations (prescribed particulars, fees, compoundable offences, exemptions under s 43); asserted only as `#ASSERT REFUSED` for ss 37/43(2)(j), 40(6) and 43.
