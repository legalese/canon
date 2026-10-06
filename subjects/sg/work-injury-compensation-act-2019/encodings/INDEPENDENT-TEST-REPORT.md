# Independent test report — WICA 2019 encoding

- Expectations: `independent-expectations.md`. Sections A to N were written from `BRIEF.md`, `../source/WICA2019.txt` and `../source/PROVENANCE.md` before any `.l4` file was opened. Section S was added after the module interfaces were read; its expected values still come from the source.
- Tests: `tests-independent.l4`, run with `~/.local/bin/l4 run`. Diagnostics were read; the exit code was ignored.
- Sanity check: a deliberately wrong assertion (`Table A factor for age 30 = 999`), run in a scratch copy, was reported as `assertion failed`, so failures are detected.

## Numbers

| | count |
|---|---|
| `#ASSERT` directives | 426 |
| assertion satisfied | **421** |
| assertion failed | **5** (3 `expected a refusal, but the expression produced a value`, 2 `assertion failed`) |
| other `DiagnosticSeverity_Error` | **0** |

Every scenario in sections A to N that the interface can express agrees with the encoding: 419 of 419. All 5 failures are supplementary scenarios S1 to S5.

## Failing assertions

### 1. [S1] A disease whose date of accident is before 1 September 2020 is not refused (line 1096)
- **Scenario**: an employee contracts a disease not in the Second Schedule on 2019-06-01. It is directly attributable to chemical exposure at work, and incapacity begins on 2019-07-01. Under s 11(2) the date of the accident is 2019-07-01.
- **Expected**: REFUSE.
- **Encoding gives**: `compensable as if a work injury OF "s 10(1)(c) / 34G(1)(c): a disease from a chemical or biological exposure at work"`.
- **Source**: s 83(1): "the repealed Act continues to apply ... to any personal injury caused by an accident to an employee, **or disease contracted by an employee, if the date of the accident for that personal injury or disease is before 1 September 2020**". The brief also requires a refusal.
- **Cause**: `the liability for the disease of a worker` in `wica-liability.l4` never calls `the law is encoded for an accident on`. The accident route does call it (through `the coverage of`), but the disease route does not.

### 2. [S2] A disease dated in the 2020-2024 window is not refused (line 1098)
- **Scenario**: as S1, but contracted on 2023-03-01 with incapacity from 2023-04-01.
- **Expected**: REFUSE. The brief says the text before 1 January 2025 was not supplied.
- **Encoding gives**: `compensable as if a work injury OF "s 10(1)(c) / 34G(1)(c): ..."`.
- **Source**: BRIEF.md, Vintages. The cause is the same as finding 1.

### 3. [S3] Temporary incapacity payments for a 2019 accident are not refused (line 1100)
- **Scenario**: an accident on 2019-06-01, 20 days of medical leave, daily rate 90.
- **Expected**: REFUSE.
- **Encoding gives**: `1620`.
- **Source**: s 83(1) and the brief. The encoding's own death, C, total, partial and medical functions do refuse this date. `the temporary incapacity payments for an accident on ...` has no date gate, and neither does the platform-worker version, which calls it.

### 4. [S4] An aggregate loss of 110% from one accident is priced as 1.1C, not as total incapacity (line 1102)
- **Scenario**: two injuries in one accident at 60% and 50%. AME 2,000, age 30 on next birthday, accident 2025-11-01, so C = 2,000 × 164 = 328,000.
- **Expected**: 410,000 (C + 0.25C).
- **Encoding gives**: `360800` (1.10 × C) from `the partial incapacity compensation for an AME of ... losses in percent (LIST 60, 50)`.
- **Source**: s 4(5)(b): total incapacity where "(ii) the aggregate percentage of the loss of earning capacity in respect of such injury **or combination of injuries is 100% or more**". s 4(5)(a) confines partial incapacity to an aggregate "less than 100%". First Sch para 3 prices partial incapacity only; para 2 prices total incapacity at C + 0.25C.
- **Note**: the reading is arguable. Para 3(2)'s cap ("not so as to exceed ... permanent total incapacity") could be read as allowing aggregates between 100% and 125% to be priced at C × aggregate. The partial function's cap shows the encoder took that reading. If the caller goes through `the s 4(5) outcome for a loss of earning capacity of 110` and then `the lump sum ...`, the encoding gives 410,000, and a supplementary assertion confirms it. So the result depends on which entry point the caller uses. The aggregating function is the only one that takes several injuries, and it does not apply s 4(5) itself.

### 5. [S5] A single 100% Fourth Schedule injury through the partial function gives C, not 1.25C (line 1104)
- **Scenario**: loss of 2 limbs (Fourth Sch item 1, 100%), same worker as S4.
- **Expected**: 410,000.
- **Encoding gives**: `328000`. `the lump sum ... outcome (permanent or current partial incapacity 100)` gives the same.
- **Source**: s 4(2)(b), s 4(5)(b), Fourth Sch item 1, First Sch para 2. Same cause as finding 4: neither the partial function nor the dispatcher's partial branch checks for 100% or more.

## Scenarios the interface cannot express (not tested)

| ID | Scenario | Why |
|---|---|---|
| A19 | s 3(2): an employee lent or hired out stays the lender's employee | no rule; it is inert in the encoding |
| C11-C16, G4 | which work stage a delivery or ride-hail worker is at, including the gap at an interim location before stage 2 begins (Fifth Sch Pt 2 item 1 col 3(b)) | the work stage is an input (`Work stage`); the Part 2 table is not encoded as a rule |
| G16 | "relevant platform service" = the service with the highest lookback earnings (Pt 3 para 7) | an input |
| D3, D4 | s 13(2)-(3): the principal is indemnified, and compensation is based on earnings under the contractor | carried as text, no function |
| F30 | turning a monthly AME into a daily amount for para 4 | the encoding takes the daily rate as an input (fork F4). This matches my "REFUSE / input" expectation |
| F31 | para 4(4): treated as hospitalised when certified but not admitted | the caller chooses the kind of day |
| F35 | medical cost incurred more than one year after the accident | the caller supplies the cost within the year |
| J7 | s 41(1): withdrawal is allowed only before an order is made or takes effect | `Claim history` has no order date |
| J23 | s 46(3): a Medical Board change is not an "error" | folded into the error/fraud boolean |
| L4 | s 26(3): insurer liable as if the compulsory terms were included; derogating terms void | only s 26(1) and s 26(4) have rules (both tested) |
| L12 | a contract void for non-payment of premium (s 29 not engaged, so arguably nothing passes under s 28) | one boolean "void other than for premiums"; a premium-void contract cannot be stated, and the rule then lets the rights pass |
| M18 | whether an offence is prescribed as compoundable | regulations; no function |
| N3 | s 47C(4): the relevant PO's insurer pays in full, even beyond the insured amount | carried as text, no function |
| N11 | the prescribed time to pay (s 18(2), s 19(1)) | no function, so nothing is wrongly computed |
| — | s 34D(3): a platform worker's "drug" excludes s 7(3)(b)(ii) (foreign prescription law) | a single "alcohol or a drug" boolean |
| — | Fifth Sch Pt 3 para 6(2)(b): B is *all* hospitalisation/medical leave days in the lookback period, once there is a run of 7 or more | the field holds the leave days "in a run of 7 or more", so other leave days cannot be added to B |

## What agrees (for the record)

- **Coverage**: every Third Schedule class, Government declared and undeclared, s 9 each limb, s 65(2), all four vintage boundaries, platform workers.
- **Liability**: every s 7(2) exclusion and each fight exception, s 7(4), s 8(1)-(3); s 34D(2) including both Sixth Schedule limbs with and without causation, s 34F, s 34E shares.
- **Principal and disease**: s 13; s 10(1)(a)-(c), s 10(3)(a)-(b) including the exactly-one-year boundary, s 10(4), s 12, s 34G(1)(c), s 11(1)-(2), s 11A.
- **First and Fifth Schedule amounts**: every Table A/B factor tested including both ends; floors and caps on both sides of 1 Nov 2025 including 31 Oct; the AME and ADE formulas; the lookback period; the para 4 counters (60-day, shared 14-day, light-duties shortfall, rest days, one-year window); the $27 × D rule; the medical caps.
- **Timing**: s 15, s 17(1)(b), s 17(4), s 34N(2) including December and February certificates.
- **Payment and process**: all payees under s 18 and s 19; s 22, s 23, s 59(2) and refunds; every Part 4 date (s 35(5), s 37, s 39, s 41, s 44(5)/48(3), s 46(2), s 47E, s 48(4)), s 51(3), s 58.
- **Damages, insurance, offences**: s 63 and s 64; s 24 to s 34; every maximum penalty and repeat-offender rule, including the asymmetric s 62(4) and the s 35(8) first offence without imprisonment; s 76 composition; s 72 and s 73; s 77.
- **Administration**: s 18(1)/47, s 40, s 47A, s 47C, s 47G, s 60(2), s 70.

## Triage by the encoder (2026-10-06)

All five findings were checked against the source and are **encoding errors**. The encoding was fixed; every independent assertion was kept unchanged and now passes (426 of 426).

| finding | fix |
|---|---|
| S1, S2 | `the liability for the disease of a worker` now refuses unless the law is encoded for the disease's s 83 date: the s 11(2) date of accident, or the date contracted where there is no incapacity, death or certification yet (fork F12) |
| S3 | `the temporary incapacity payments for an accident on …` now refuses outside the encoded period; the platform version inherits it |
| S4, S5 | `the partial incapacity compensation …` now pays C + 0.25C when the aggregate is 100% or more (s 4(5)(b), First Schedule para 2) |

One of the encoder's own assertions was wrong for the same reason as S1 (a disease contracted in 2011 asserted "not compensable", when s 83(1) sends it to the repealed Act); it now asserts a refusal. See NOTES.md section 9.
