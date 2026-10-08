# Independent test report: Child Development Co-Savings Act 2001 encoding

## How the tests were made

1. I read `BRIEF.md` and `../source/CDCSA2001.txt` (Parts 1-4 and both Schedules) first. From them I wrote 163 numbered expectations (E1-E163) to `independent-expectations.md`, each with its provision. I wrote these before opening any `.l4` file and have not changed them since.
2. Then I read `cdcsa-types`, `-common`, `-scheme`, `-maternity-adoption`, `-fathers-shared`, `-childcare`, `-general-offences` and `-goal`. I looked at `cdcsa-tests.l4` only for its helper-record syntax.
3. I wrote `tests-independent.l4`. It imports prelude, daydate and the eight modules listed above. It does not import `cdcsa-tests`.

## Result

`l4 run tests-independent.l4` (toolchain `~/.local/bin/l4`) gives:

| | count |
|---|---|
| `#ASSERT` lines | **268** |
| satisfied | **267** |
| failed | **0** |
| refused (warning, not satisfied) | **1** |
| other errors | **0** |

`L4=~/.local/bin/l4 ./check.sh` reports `tests-independent.l4` with 0 errors, 267 satisfied and 0 failed. The other modules show 0 errors, and `cdcsa-tests` 218 satisfied. `check.sh` does **not** count the refused assertion: l4 reports a refusal as a Warning, and the script greps only for Error, satisfied and failed. A refused `#ASSERT` therefore passes `check.sh` silently, which is worth fixing in the script.

## Disagreements

### D1. E33: s 3(3) co-savings match with no regulatory cap given (refused)

- **Scenario.** The child is eligible and a parent contributes $3,000. No cap from the regulations is supplied.
- **Expected.** The Government contributes **$3,000**. Section 3(3) defines a co-savings arrangement as Government contributions "equal to the contributions made by or on behalf of any parent".
- **Encoding.** It answers `REFUSE "the matching cap is set by regulations under s 3, which are not in the source"`. With a cap supplied (E33a, cap $1,000,000) it gives $3,000, which agrees.
- **My view.** The encoding's reading is defensible. The Act defines the matching ratio, and the regulations (s 3(2)(a), (c)-(d)) set the eligibility and the maximum, so a refusal when the cap is unknown follows the brief's "REFUSE where the source does not answer" rule. Section 3(3) itself still answers "equal". A function that gave the 1:1 ratio, and refused only on the ceiling, would fit the Act more closely. This is a minor point.

There are no other disagreements. Every date edge I tested agrees with my reading:
- April 2025 and January 2024 child definitions, including the born-alive limb;
- the s 2(2) before/after 1 November 2021 rule;
- 9A(1) and stillbirth dates; the 12-month citizenship window; the 90/89-day test;
- 12F(1)(a) for born-alive and stillborn children, including the stillborn limb with no EDD condition;
- 12JA(1), para 5 M, the specified variation period, 12N(4) month-end, and 12N(9)(e).

All the cap arithmetic I tested also agrees: ss 9A(4), 10(2), 9A(5), 9A(5A), 12AA(5), 12AD, 12AB, 12A, 12I(3)-(4), 12J, 12HA, 12JA, 12DB, 12DC, 12F(2), 12B(10)-(10A), 12C, 12CA, 12B(16)-(19) and 12D. So do the penalty and composition values.

## A finding from a probe (not in the expectation file)

I ran a scratch probe of the top-level goal. It is not counted above, because the scenario is not in `independent-expectations.md`.

- **Scenario.** A natural mother whose status is `neither` (she *was* an employee, s 9(5A) "is or was"). She has 12 months of past service, 200 working days in the prior 12 months, $500 a day, 1st event.
- **Result.** `the parental position for` gives **Government-paid benefit NOTHING**. The same case with months = 0 gives `JUST 20000`.
- **Cause.** `cdcsa-goal.l4` computes `own eligible` from `eligible under s 9A(1)` without looking at `status`. A woman with no current employer, but with past months of service in the record, is treated as having her own leave. She is then refused the s 9(5A) benefit, yet gets no leave either, because `own paid leave` needs `employee`. The same pattern applies to fathers (s 12HA) and adoptive mothers (s 12A).
- **Fix.** Either gate `own eligible` on `status` being an employee or a self-employed person, or document that `months of service` must be 0 when there is no current employer.

## Expectations I could not express against the encoding

| E | Provision | Why |
|---|---|---|
| E74 | s 9A(5B) once per confinement | `Birth` has no child count; one confinement is one record by construction |
| E87 (second half) | s 12A(7) contract-completion exception | There is no 12A disqualification function. The goal uses "not own-eligible" as a proxy, so the exception cannot be reached |
| E88 | s 12AD(3)-(4) discretionary adoption reimbursement | Carried as text only |
| E91 (days) | s 12H(4)(b)(i) self-employed father's days for a January 2024 child | The only days function is for employees (April 2025). I tested the self-employed $10,000 cap instead, which agrees |
| E97 | s 12I(1)(c)(iii) marriage within 12 months | `married in time` is a boolean input |
| E118 | Second Schedule para 16 ("the Director **may** require") | The encoding treats a s 16 event as making agreement required, not discretionary. I asserted only that the variation is not "permitted without agreement" |
| E123 | s 12DC(5)(c) claim after the child's death | Not encoded |
| E131 | s 12E(8)(b) N from a deceased mother's unconsumed weeks | Not computed. Only the 1-4 validity check exists |
| E135 | s 12B(21) qualifying child = citizen | The caller decides it |
| E148 | s 12MA(9) "relevant child" (1 April 2025 gate) | The aggregation function takes no date, so the gate is not encoded |
| E160 (part) | s 17(1AA), 12B(14C) prior conviction on or after 1 May 2013 | `repeat` is a boolean input |

## Parts of the Act the encoding misses or simplifies

1. **Government-paid benefit at goal level** (see the probe above). Eligibility for own leave ignores work status. The s 9(6A)/(6B), 12A(6)/(7), 12HA(5)/(6) and 12DC(6)/(7) exceptions are reachable only through the standalone maternity disqualification function, not through the goal.
2. **Discretionary reimbursements** for an employee without 3 months' service are carried as text only: ss 12AD(3)-(4), 12DB(6)-(9), 12DD(2), 12J(3)-(5) and 12JA(6). Only s 10(2A) is encoded.
3. **s 12MA.** The aggregate limit is a plain min(sum, limit). The relevant-child date gate, the 12MA(5) treatment of all employers, and the 12MA(8) employer recovery are not modelled.
4. **s 12B(16)-(18A) self-employed childcare.** The lifetime per-child caps (21 days under (16), 12 under (16A)), the 3 months of carrying on, and the 17 August 2008 / 1 January 2013 gates are not in the function. Only the calendar-year logic and the $500 a day cap are.
5. **Timing windows.** These are not checked anywhere:
   - the 26-week window for one-block shared parental leave (12DA(2)(a)(i)) and the 12-month window (12DA(2)(a)(ii), 12DA(6)(d));
   - the 16-week window for one-block paternity leave (12H(1)(a));
   - the start date of an adoptive father's leave (12H(5), 12DA(7), 12E(4));
   - 12DA(8), where entitlement ends the day after the child's death;
   - 12E(5A)(b), the election window.
6. **s 9(1A) and (1B).** The outcome is given as a label, with the EA s 76 "specified period" as an input. The goal refuses a non-citizen-at-birth case rather than computing pay for it. The amounts under 9A(4)(a)(i)(C)-(G) for these mothers are not computed.
7. **Second Schedule paras 2-4 and 11-13, 17-18.** These cover:
   - one arrangement per confinement or adoption;
   - conversion after a later marriage or adoption;
   - reallocation on termination or death, including employer agreement under para 12(2);
   - notice procedure and refusal.

   They are text only. Para 8 is covered by the whole-number and floor functions.
8. **s 12O.** The amount test needs the caller to give "the benefit amount". The "extra absence period" definition (12O(5)) is left to the caller's day count.
9. **s 2(2) specified-event counting.** The record carries "each child is dead or was stillborn" as one boolean. The caller must apply "each child" across multiple births, as in my E17 twins case.
10. **Parent-case model.** A single `weekly index` and `gross pay per week` is used throughout. Partial-week caps (blocks of 4 x WI) are modelled as 4 calendar weeks of pay. The note 5 half-day rounding is applied only in the days functions, not in money blocks. This agrees with my arithmetic for whole-week cases but is untested for odd periods.
11. **Childcare reimbursement.** The 12C(2A)/12CA(2A) cross-year treatment and the multi-employer s 12C(3) refusal are input-driven: the caller passes the days already reimbursed.
