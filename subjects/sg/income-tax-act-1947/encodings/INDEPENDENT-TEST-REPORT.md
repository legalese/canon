# Independent test report: Income Tax Act 1947 (SG)

**Method.** I read `BRIEF.md`, `../source/PROVENANCE.md` and the listed provisions of `../source/ITA1947.txt`. I wrote `independent-expectations.md` (about 300 scenarios in sections A to S) before opening any `.l4`, `NOTES.md` or tests file. Only then did I read the module interfaces and write `tests-independent.l4`. I glanced at `ita-tests-goal.l4` and `ita-tests-process.l4` only to see how records are built. No expected value was changed after the run.

**Run.** `~/.local/bin/l4 run tests-independent.l4` with `JL4_LIBRARY_PATH` unset.

| | count |
|---|---|
| `#ASSERT` directives | 320 |
| assertion satisfied | **316** |
| assertion failed | **2** |
| assertion refused where an answer was expected (Warning: "assertion refused") | **2** |
| other `DiagnosticSeverity_Error` (beyond the 2 failures) | 0 |

`l4 check` is clean. The 2 Error diagnostics in the run are the 2 failed assertions.

## Failing assertions (4 findings, 3 provisions)

### 1. s 10L(2)(b): gains that would otherwise be exempt are wrongly let off (line 379)

- **Scenario J17b.** An entity in a relevant group sells a foreign asset on 1 June 2024. It remits $1,000,000 of gains, nothing is excluded under (8), and the gains would otherwise be exempt from tax.
- **Expected:** 1,000,000 chargeable.
- **Encoding gives:** 0.
- **Source:** s 10L(2): "Subsection (1) only applies if — (a) the gains would not otherwise be chargeable to tax as income under section 10(1); **or** (b) the gains would otherwise be exempt from tax under this Act."
- **Cause:** the encoding has one input, `otherwise chargeable or exempt as income`, and switches s 10L off when it is TRUE. Under (2)(b), "otherwise exempt" is a reason s 10L applies, not a reason it does not. The input needs splitting into two: chargeable switches s 10L off, exempt does not.

### 2. s 13(1)(jd): a medisave contribution above $2,730 gets no exemption at all (line 395)

- **Scenario K6.** A person of the prescribed description makes a voluntary $3,000 medisave contribution in 2025 for a self-employed individual.
- **Expected:** the exemption applies, up to $2,730.
- **Encoding gives:** FALSE, because it tests `amount AT MOST 2730`, so the whole $3,000 is treated as not exempt.
- **Source:** s 13(1)(jd): "any voluntary contribution … to the medisave account … of a self-employed individual, **up to** — … (ii) $2,730 per year (for contributions made in 2018 and in each subsequent year), less any previous contribution …"
- **Cause:** the provision caps the exempt amount. It is not a condition on the whole contribution. The rule should return the exempt amount, min(contribution, 2,730 less the earlier employer contribution), as s 14(1)(fb) is already encoded.

### 3. s 43X(5): only 5% is allowed (lines 558 and 559, refused)

- **Scenario R10a.** An approved IP company has a 10% base rate. Expected: 10,000 on 100,000. The encoding refuses: "the awarded rate is not one the section allows".
- **Scenario R10b.** Base 10% plus a 2% rate increase, so 12%. Expected: 12,000. The encoding refuses the same way.
- **What the encoding has:** `the rates allowed under` `s 43X intellectual property income` = `LIST 0.05`.
- **Source:** s 43X(5): the rate "determined in accordance with the formula A + B, where — (a) if the company is approved before 17 February 2024 — A is a base rate of 5% or 10% …; (b) if … approved on or after 17 February 2024 — A is a base rate of 5%, 10% or 15% …; … (d) B is the sum of every rate increase specified by the Minister or authorised body … in accordance with subsection (6)."
- **Cause:** the list should allow base rates of 5%, 10% and 15%, gated by approval date, plus an input B.

## Scenarios I could not express with the interface

| id | scenario | why |
|---|---|---|
| E3 (note) | NR rent for movable property, s 12(7)(d) | It passed, at 15%. But the constructor is labelled `s 12(7)(d) management or technical service fee`. Management fees fall under s 12(7)(c), which is not in s 43(3)(b). Technical-service fees are excluded from s 43(3)(b) by s 43(7)(b). So the label invites a caller to apply 15% to income that should bear the s 43(1) rate. |
| F3 | s 40B does not apply where income includes an SRS withdrawal (s 40B(1)(a)) | The caller chooses the relief; there is no input for it. |
| F5 | NR public entertainer, income derived in 2021, at 10% (s 40A(2A)) | The function takes a YA, not the date the income was derived, so 10% is never applied. |
| G10 | No s 42A rebate for a non-resident | Reachable only through the goal; not tested separately. |
| I26 | 7% of capital sum cap on premiums (s 39(2)(g)(i)) | The input is already capped by the caller. |
| I39, I42 | SRS cap and CPF top-up limits | Prescribed by regulations, so these are inputs, as expected. |
| K16 | s 13W with a 19% holding | The interface takes only "months the 20% holding was held". The percentage test is the caller's. |
| M19 | s 19(3) $35,000 base for allowances on a car | There is no function. The s 14(3) deduction cap is encoded and passes. |
| N18 | s 27(4): no certificate, so profits are 5% of the receipts from carriage shipped in SG | Only the s 27(2) certificate ratio is encoded. |
| O17 | s 50C(2)(b): pooled credit not available where the foreign headline rate is below 15% | The function has no condition input. |
| P6 | s 67(1)(a) records kept 5 years | I left this out: whether "5 years from the YA" means YA + 5 is ambiguous. |
| P26 | s 93A(5) $250 deposit | There is no function. |
| P28 | s 33A(4) surcharge payable within one month | There is no function. |
| R2, R5, R8, R11 | Approval-date gating of concessionary rates. s 43E: 10% for approvals on or before 24 Mar 2016, 8% up to 16 Feb 2024. s 43N: 8% for approvals 1 Apr 2017 to 16 Feb 2024. s 43I: 15% only for a GTC approved on or after 17 Feb 2024. s 43X: 15% base only after 17 Feb 2024. | `the concessionary tax under` takes no approval date, so it accepts any listed rate whatever the approval date. For example, s 43I at 15% passes for any company. |

## Notes on what passed

Everything else matched the source. That covers:
- the Second Schedule tables at every band edge tested, with a refusal before YA 2012, and YA 2023 answering;
- s 43(1), (6A), (6B), (6C)/(6D), (8) and (10)-(11);
- the gross-income rates and the s 43(5) deadline;
- ss 40A and 40B, including the resident floor and the proportional case;
- s 42A;
- ss 92J and 92L, including (2) and the (4) bar;
- every s 39 relief tested, the Fifth Schedule caps (5(3), 6(2)) and s 39A;
- s 10 housing, shares, annuities and author royalties (YA 2026-2029);
- s 10G, s 11 and s 12;
- the Part 4 exemptions tested;
- ss 14, 14C/14D, 14EA, 14N, 14Z and 14ZG;
- ss 19, 19A and 20, and the s 23/37(12) 50% test;
- s 35(2A), the s 37 donation multiples and carry-forward, ss 37B, 37D, 37R, 33A, 34E and 34F;
- s 45 rates, deadline and penalties, s 45(5)-(6), (9), ss 50 and 50C;
- ss 62-93A and 8(2);
- ss 94-96A, including the minimum-imprisonment rules;
- the Twelfth Schedule and the Seventh Schedule fees;
- three whole-taxpayer cases: a resident employee with tax of 3,000; a company paying 18,787.50 after the s 92L remission; and a non-resident employee paying 15,000 under s 40B. Both whole-computation cases at YA 2023 refuse.

The encoding's actual values for the failures were taken with `#EVAL` in `/tmp/claude-1001/-home-aswathy/60ab0213-e32e-44b6-b10d-b771e4c3f054/scratchpad/indep-ita/evals.l4`.

## Triage by the encoder (2026-10-06)

All four findings were checked against the source and are **encoding errors**; the encoding was fixed and every independent assertion now passes (320 of 320).

| finding | fix |
|---|---|
| s 10L(2)(b) | the one input `otherwise chargeable or exempt as income` is split into `otherwise chargeable as income under s 10(1)` and `otherwise exempt from tax`; s 10L applies if the gains are not otherwise chargeable **or** would otherwise be exempt |
| s 13(1)(jd) | the exemption applies to any contribution, "up to" $2,730; a new rule `the exempt part of a voluntary medisave contribution of` … gives the amount |
| s 43X(5) | the rate is A + B: the base rates 5%, 10%, 15% are allowed, and any rate above 5% as a base plus increases |

**Plumbing edits to `tests-independent.l4`, no expected value changed:** the `sale` helper now sets the two split fields (its flag, which the scenarios use to mean "would otherwise be exempt", goes to `otherwise exempt from tax`); and the constructor `s 12(7)(d) management or technical service fee` was renamed `s 12(7)(d) rent or payment for the use of movable property`, as the report pointed out it was mislabelled (s 12(7)(d) is rent for movable property; management fees are (7)(c)).

**Not expressible, now added:** s 27(4) (5% deemed profit without a certificate) and s 27(6) (casual calls). The rest of that list is recorded in NOTES.md section 7 as known limits.

One encoder assertion was wrong for the s 13(1)(jd) reason (a $2,731 contribution asserted not exempt); it now asserts the exemption and the exempt part.
