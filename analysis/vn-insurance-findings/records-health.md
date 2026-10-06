# Policy defect records: health, accident and travel rows (VN-03, VN-04, VN-19, VN-23, VN-06)

Extracted from each row's `NOTES.md` section 4 and its findings or tests modules.
Money marked "(fixture)" is the encoder's hypothetical test money, not a figure from the source.
Line references like `pti-findings.l4:42` are to the encoding directory of the row.

## VN-03 PTI Phúc An Sinh health (Decision 267/2012)

Directory: `vn-pti-phuc-an-sinh-health/encodings/legalese-2026-10-vn-03`.

### VN-03 X0 — Appendices that fix disablement and benefit amounts are missing
- **Class**: T8 published document is incomplete
- **Scenario**: The Rules pay partial disablement by "the table of Appendix 03", list benefits in Appendix 01 and the hospital network in Appendix 04. The published 16-page file contains none of them, so what a lost finger pays cannot be learned.
- **Who bears it**: insured. **Money direction**: unclear.
- **Standing**: LITERAL (reading only; the encoding takes the rates as inputs).
- **Evidence**: reading only, no assertion; src:261, 277, 436, 723.
- **Plain-English test of surprise**: A buyer expects the policy to state what each injury pays; the wording points to tables that are not published.

### VN-03 X1 — Total accident disablement must be shown before it can exist
- **Class**: T1 clocks and deadlines / T6 illusory cover
- **Scenario**: Programme I covers consequences "within 104 weeks" of the accident; an unlisted disablement is total only after lasting 104 weeks. If it must be established inside those weeks, only a same-day onset qualifies: accident 1 March 2026, onset 5 March fails, onset 1 March passes.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: CONTESTED ("read literally"; the encoding takes onset instead, fork F9).
- **Evidence**: `pti-findings.l4:42` (5 March: NOT established), `:43` (1 March: established); src:273-274, 90-94.
- **Plain-English test of surprise**: A customer expects a disablement appearing days after an accident to be covered; read literally, only a same-day onset is.

### VN-03 X19 — Claim deadline expires 18 months before the disablement qualifies
- **Class**: T1 clocks and deadlines (a bar that runs before the right arises)
- **Scenario**: The claim file is due 180 days after the last treatment. Accident 1 March 2026, discharge 10 March: due 6 September 2026, yet a disablement from 5 March meets definition 18 only on 2 March 2028. Partial and illness disablement (52 weeks) fail the same way.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL. LAW note (fork F41): Law art 30(1)'s year "is still shorter than 104 weeks".
- **Evidence**: `pti-findings.l4:61` (due 2026-09-06), `:62` (before onset plus 728 days); src:649-651, 654-655, 90-94.
- **Plain-English test of surprise**: A claimant expects the clock to start once the loss can be proved; it closes long before.

### VN-03 X26 — A death claim has no date for its time limits to run from
- **Class**: T1 clocks and deadlines (a clock with an undefined start)
- **Scenario**: Claim time limits run from "the day of last treatment", which is defined only for a hospital stay (discharge) and outpatient treatment (diagnosis). A death without treatment has neither, so whether a death claim is late cannot be decided.
- **Who bears it**: beneficiary. **Money direction**: unclear.
- **Standing**: LITERAL.
- **Evidence**: `pti-findings.l4:78` `#ASSERT REFUSED the total payable on the claim a death claim BECAUSE "Part 5 clause 1 fixes the day of last treatment only for a hospital stay and for outpatient treatment"`; src:650-651.
- **Plain-English test of surprise**: A bereaved family expects a clear deadline for a death claim; the wording supplies none.

### VN-03 X2 — A late notice may forfeit a claim filed in time
- **Class**: T12 forfeiture by notice / T1 clocks and deadlines
- **Scenario**: Notice is due within 30 days of the last treatment, the claim file within 180; "past the above time limit" the claim is refused in full. If that includes the notice, a claim notified on day 31 and filed on day 38 is lost.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: CONTESTED (fork F40 reads the phrase as the filing limits only; Law art 19(3) on force majeure noted).
- **Evidence**: `pti-findings.l4:108` (literal reading: refused in full), `:109` (reading taken: not); src:646-655.
- **Plain-English test of surprise**: A customer expects a one-day-late notice to cost nothing when the claim is filed early; read literally, it forfeits everything.

### VN-03 X3 — Each renewal resets the start date and re-imposes exclusions
- **Class**: T10 waiting period or term interplay / T5 ambiguous term
- **Scenario**: Read alone, definition 5 makes each period's first day the "start date". On a contract held since 2023, a surgery ordered in 2025 then becomes a pre-start "surgical indication" in 2026 (exclusion 12), and hepatitis in 2026 falls in "the first year" again (exclusion 26).
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: CONTESTED (fork F3 measures from the date of joining).
- **Evidence**: `pti-findings.l4:155`, `:157` (definition 5 alone: exclusions apply), `:156`, `:158` (encoded: not); src:35-36, 483-484, 520.
- **Plain-English test of surprise**: A loyal renewer expects continuity; read this way, every renewal treats the person as a new joiner.

### VN-03 X4 — Benefit 2 pays for a prosthesis that exclusion 18 removes
- **Class**: T7 internal inconsistency / T6 granted then taken back
- **Scenario**: Benefit 2 pays for a life-sustaining prosthesis bought for surgery; exclusion 18 excludes it, and exclusions apply to "the main programmes and the optional benefits alike" (src 460). A pacemaker bought for heart surgery is both granted and excluded.
- **Who bears it**: insured. **Money direction**: against the claimant (literal reading).
- **Standing**: CONTESTED. The encoding pays, the specific grant prevailing over the general exclusion and by Law art 24 (fork F34).
- **Evidence**: `pti-findings.l4:178` `exclusion 18, read literally, applies to a pacemaker bought for surgery`; `:179` encoded outcome `payable 5_000_000` (fixture); src:301, 496-498.
- **Plain-English test of surprise**: A patient expects a benefit that names life-sustaining prostheses to pay for a pacemaker; the exclusion list takes it back.

### VN-03 X5 — Outpatient exclusion swallows emergency and pre-admission cover
- **Class**: T6 granted then taken back / T2 overbroad exclusion
- **Scenario**: Exclusion 27 excludes outpatient treatment unless the outpatient option is held. Read literally, it removes Programme I emergency care without admission (Programme I alone cannot buy the option, src 333), Programme II costs before admission and after discharge, and dental and maternity care outside a stay.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: CONTESTED. The encoding confines exclusion 27 (fork F35) and pays 500,000 and 800,000 (fixture).
- **Evidence**: `pti-findings.l4:222`, `:224` `exclusion 27, read literally, applies to` (TRUE); `:223`, `:225` encoded `payable`; src:521, 278-279, 312-317.
- **Plain-English test of surprise**: A customer expects the emergency and pre-admission benefits printed in the programme to pay; read literally, a general exclusion cancels them.

### VN-03 X6 — "Hospitalisation" and "inpatient treatment" split one stay
- **Class**: T5 ambiguous term / T7 internal inconsistency
- **Scenario**: Benefit 1 needs a "hospitalisation" (24 hours, def 31); the income allowance needs "inpatient treatment" (a night, def 32), yet the text treats them as one. A 20-hour admitted overnight stay pays the allowance (600,000, fixture) but not benefit 1; a 26-hour stay without admission is outpatient, so exclusion 27 removes it without the outpatient option.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `pti-findings.l4:239` (allowance `payable 600_000`), `:240` (benefit 1 `not covered`); `pti-tests-exclusions.l4:201` (26-hour stay, `EQUALS LIST 27`); src:158-163.
- **Plain-English test of surprise**: A patient kept in hospital overnight expects to count as hospitalised for every benefit; the two definitions give different answers for the same stay.

### VN-03 X7 — Exclusion 2's age-14 threshold does nothing
- **Class**: T2 overbroad exclusion / T7 internal inconsistency
- **Scenario**: Limb 1 excludes any breach of the law; limb 2 excludes traffic offences by people aged 14 or more. A 13-year-old's traffic offence is still a breach of the law, so limb 1 excludes it and the age threshold is idle.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: CONTESTED. The encoding reads limb 1 as not reaching traffic offences (fork F31).
- **Evidence**: `pti-findings.l4:260` `exclusion 2, read literally, applies to a 13-year-old's traffic offence` (TRUE); `:261` encoded (NOT); src:463-464.
- **Plain-English test of surprise**: A parent expects the stated age threshold to protect a child under 14; read literally, the broader limb excludes the child anyway.

### VN-03 X8 — Rabies-shot proviso after a bite never applies
- **Class**: T6 granted then taken back / T2 overbroad exclusion
- **Scenario**: Vaccination is excluded. The proviso saving treatment after an accident or animal bite is attached to "preventive medicine", not to vaccination, so a rabies shot after a dog bite stays excluded on the literal reading.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: CONTESTED. The encoding lets the proviso limit the vaccination limb (fork F32).
- **Evidence**: `pti-findings.l4:284` `exclusion 9, read literally, applies to a rabies vaccination after a dog bite` (TRUE); `:285` encoded (NOT); src:473-476.
- **Plain-English test of surprise**: A dog-bite victim expects the post-bite shot the clause appears to save to be paid; read literally, it is not.

### VN-03 X9 — Illness partial disablement paid only if an injury table lists it
- **Class**: T6 illusory cover / T5 term that decides outcomes
- **Scenario**: Benefit 6 pays partial permanent disablement from illness by Appendix 03, but definition 17's descriptive limb requires an accident. An illness disablement that the (unpublished) table does not list is not covered.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `pti-findings.l4:303` benefit 6 partial disablement `EQUALS not covered`; `:305`; src:436-437, 85-89.
- **Plain-English test of surprise**: A buyer of illness disablement cover expects any lasting partial disablement from illness to count; the definition only works for accidents.

### VN-03 X10 — Programme main limit can never be reached
- **Class**: T13 other (a redundant limit) / T4 payout arithmetic
- **Scenario**: Definition 13 says a programme's sub-limits may not add up to more than its maximum. If so, payments inside the sub-limits never reach the maximum, and the main limit does no work.
- **Who bears it**: unclear. **Money direction**: no money.
- **Standing**: LITERAL (reading only).
- **Evidence**: reading only; `pti-findings.l4:383` asserts the fixtures' arithmetic (`the sum of the sub-limits of Programme II ... AT MOST ... the main limit`); src:56-58, 70-72.
- **Plain-English test of surprise**: A reader expects the headline maximum to be a real cap; it is never the binding figure.

### VN-03 X11 — Two extensions referred to but never offered
- **Class**: T8 published document is incomplete / T5 undefined term
- **Scenario**: The Rules mention a "contract extended to cover pre-existing conditions" (src 484) and an extension for special diseases (src 502). No part of the Rules offers, defines or prices either.
- **Who bears it**: insured. **Money direction**: unclear.
- **Standing**: LITERAL (reading only; the encoding treats them as inputs).
- **Evidence**: reading only; src:484, 502.
- **Plain-English test of surprise**: A customer told an exclusion can be lifted by an extension expects to be able to buy it; the document never says how.

### VN-03 X12 — Other insurance: two methods, no rule for choosing
- **Class**: T5 ambiguous term / T4 payout arithmetic
- **Scenario**: Clause 6 gives an excess method and a ratio method joined by "hoặc" (or). On the same facts the excess method pays 7,000,000 and the ratio method 4,000,000 (fixture).
- **Who bears it**: insured. **Money direction**: unclear.
- **Standing**: CONTESTED. The encoding pays the larger, by Law art 24 (fork F21, marked LAW).
- **Evidence**: `pti-tests-conditions.l4:240` (excess `EQUALS 7_000_000`), `:241` (ratio `EQUALS 4_000_000`), `:242` (encoded `EQUALS 7_000_000`); src:598-600.
- **Plain-English test of surprise**: A claimant with two policies expects one answer; the wording supports two that differ by 3,000,000.

### VN-03 X13 — Insurer may order a medical examination without criteria
- **Class**: T11 insurer discretion
- **Scenario**: PTI may have the insured person examined "at any time when necessary" during a claim. No criterion is stated, and no consequence of refusal.
- **Who bears it**: insured. **Money direction**: unclear.
- **Standing**: LITERAL (reading only).
- **Evidence**: reading only; src:604-607.
- **Plain-English test of surprise**: A claimant expects limits on when and why an examination can be demanded; the wording leaves it to the insurer.

### VN-03 X14 — Subrogation clause in a health contract
- **Class**: T3 contract conflicts with the statute
- **Scenario**: Clause 9 passes the insured's recovery rights to PTI after payment. The encoder notes that Law art 16(4) says subrogation does not apply to health insurance and art 38 bars the insurer's recourse.
- **Who bears it**: insured. **Money direction**: against the claimant (if the clause is applied).
- **Standing**: LAW. Encoded as written; "Not resolved" (fork F23).
- **Evidence**: reading only per NOTES; `pti-tests-conditions.l4:250` shows the clause's arithmetic (`clause 9: the rights passed to PTI ... EQUALS 4_000_000`); src:608-611.
- **Plain-English test of surprise**: A health insured expects to keep a recovery from the person at fault; on the literal reading the clause hands it to the insurer.

### VN-03 X15 — Exclusion of "routine treatment as regulated by the Ministry"
- **Class**: T2 overbroad exclusion / T5 undefined term
- **Scenario**: Exclusion 16 excludes "routine treatment as regulated by the Ministry of Health". Read literally, standard-of-care treatment is excluded; an in-hospital medicine line so described (2,000,000, fixture) is excluded, and what the words reach is not said.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `pti-findings.l4:311` (`... routine treatment as regulated by the Ministry of Health of Vietnam ... EQUALS LIST 16`); src:492-494.
- **Plain-English test of surprise**: A patient expects treatment the health ministry approves to be the core of health cover; the exclusion appears to remove it.

### VN-03 X16 — A pedestrian cannot complete a traffic-accident claim
- **Class**: T12 condition precedent / T2 overbroad
- **Scenario**: Every traffic-accident claim requires copies of the driving licence and vehicle registration. A pedestrian who files every other document still has the licence copy missing.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `pti-findings.l4:330` `the documents missing from a pedestrian's claim EQUALS LIST a copy of both sides of the driving licence and the vehicle registration`; src:662-665.
- **Plain-English test of surprise**: A pedestrian hit by a car expects to be able to claim; the document list demands a licence the pedestrian never needed.

### VN-03 X17 — A living disablement claimant must supply a death certificate
- **Class**: T7 internal inconsistency / T12 condition precedent
- **Scenario**: Benefit 6 (death and disablement) has one document list: a death certificate, medical documents and an inheritance certificate. A living claimant for total disablement from illness is asked for all three.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `pti-tests-claims.l4:187` (documents for benefit 6 total disablement `EQUALS LIST the death certificate, the relevant medical documents, the certificate of the right to inherit`); src:442-445.
- **Plain-English test of surprise**: A disabled claimant expects a disablement document list; the wording asks for proof of the claimant's own death.

### VN-03 X18 — No time limit for the insurer to pay
- **Class**: T3 contract worse than the statute / T1 clocks and deadlines
- **Scenario**: Part 5 sets deadlines for the claimant but none for PTI to assess or pay. The encoder notes Law art 31(1) gives 15 days from a complete file; the encoding does not import that figure.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LAW (fork F42, "Refused by name").
- **Evidence**: `pti-findings.l4:343` `#ASSERT REFUSED the last day for PTI to pay ... BECAUSE "Part 5 states no time within which PTI must assess or pay a claim"`; also `pti-tests-claims.l4`.
- **Plain-English test of surprise**: A claimant bound by tight deadlines expects the insurer to have one too; the Rules set none.

### VN-03 X20 — "100% refund" on the insurer's cancellation is three quarters
- **Class**: T4 payout arithmetic / T7 internal inconsistency
- **Scenario**: When PTI cancels, the policyholder gets "100%" of the premium for the unexpired period, but that premium is computed on the short-period scale. PTI cancels after one month of a 12,000,000 premium (fixture): refund 9,000,000, not the 11,000,000 pro rata.
- **Who bears it**: policyholder. **Money direction**: against the claimant (the policyholder).
- **Standing**: LITERAL (fork F20 reading (i); reading (ii) "would refund more than the premium for the time left").
- **Evidence**: `pti-findings.l4:351` `the refund on (cancellation asked for by PTI, notice 2026-01-01, cancellation 2026-02-01) ... LESS THAN 11_000_000` (comment gives 9,000,000); src:570-571, 575, 583.
- **Plain-English test of surprise**: A customer whose cover the insurer ends expects a full pro-rata refund; "100%" yields three quarters.

### VN-03 X21 — Guaranteed renewal undone by a cancel-for-any-reason clause
- **Class**: T6 granted then taken back / T3 conflict with the statute
- **Scenario**: PTI "guarantees" renewal but may cancel on 30 days' notice for any reason, so the guarantee can be ended at will. The encoder notes Law art 26 limits unilateral termination to listed grounds.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LAW (fork F43; encoded as written; reading only).
- **Evidence**: reading only; src:547-550, 568-569.
- **Plain-English test of surprise**: A customer relying on guaranteed renewal expects to keep cover; the cancellation clause lets the insurer end it anyway.

### VN-03 X22 — At 65, a new applicant is accepted and a renewer is dropped
- **Class**: T7 internal inconsistency / T10 term interplay
- **Scenario**: Entry is open up to age 65, but continuous cover ends at the first renewal after the 65th birthday. A person born 1 November 1960 can take out a first policy on 1 January 2026, yet a continuous renewal due that same day ends cover.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL (age read in completed years, fork F4, also by art 24).
- **Evidence**: `pti-findings.l4:359` (accepted as a new applicant); `:360` `NOT (continuous cover ... goes on at renewal 2026-01-01)`; src:537, 554-555.
- **Plain-English test of surprise**: A long-standing customer expects at least the terms a newcomer gets; at 65 the newcomer is accepted and the renewer dropped.

### VN-03 X25 — Day-case surgery falls between two benefits
- **Class**: T13 other (a cover gap between two benefits) / T5 term that decides outcomes
- **Scenario**: Benefit 2 (surgery) needs a 24-hour hospitalisation; the outpatient benefit pays examinations, tests, medicine and therapies but not surgery. A 6-hour surgical stay costing 10,000,000 (fixture) is covered by neither.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `pti-findings.l4:374` (benefit 2 `not covered`), `:375` (outpatient `not covered ... the head of cost is not one the benefit pays`); src:299-302, 351-357.
- **Plain-English test of surprise**: A patient holding surgery and outpatient cover expects a same-day operation to be paid by one of them; neither pays.

### VN-03 X27 — Key terms undefined or defined twice
- **Class**: T5 undefined term
- **Scenario**: "Số tiền bảo hiểm" (sum insured), which sets the death benefit, is never defined; "policyholder" and "policy" are used without definition; definitions 15 and 50 define the same bodily injury twice; definition 16 is never used.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL (reading only).
- **Evidence**: reading only; no src lines cited in the finding.
- **Plain-English test of surprise**: A reader expects the amount the death benefit pays to rest on a defined term; it does not.

### VN-03 X28 — Benefit numbers collide; "before discharge" means "before admission"
- **Class**: T7 internal inconsistency / T13 other (drafting error)
- **Scenario**: Optional benefits are numbered "Quyền lợi bổ sung" 1, 2, 5 but plain "Quyền lợi" 3, 4, 6, so benefit 3 names both organ transplant and dental treatment. The pre-admission documents ask for invoices "trước khi xuất viện" (before discharge) where "before admission" is meant.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL (reading only).
- **Evidence**: reading only; src:697.
- **Plain-English test of surprise**: A reader expects one number to name one benefit; here one number names two.

#### VN-03 row summary
- Findings in section 4: 27 (X0-X22, X25-X28; there is no X23 or X24).
- Most counterintuitive: X19 (the claim file is due 6 September 2026 for a disablement that can qualify only on 2 March 2028); X17 (a living disablement claimant must supply a death certificate); X25 (day-case surgery is paid by neither the surgery nor the outpatient benefit).
- Matches in this group: X1 ~ VN-19 X17 (a disablement must fall inside a window and also last as long as the window); X19 ~ VN-23 D5 and VN-06 F-PA-NOTICE (a claim or notice deadline closes before a covered disablement or death can exist); X2 ~ VN-19 X18, VN-04 X13 and VN-23 D12 (notice and filing clocks that forfeit); X0 ~ VN-04 X18 and VN-19 X2 (injury tables missing from the published document); X6 and X25 ~ VN-04 X5 and VN-19 X8 (a 24-hour hospitalisation test splits an overnight stay); X3 ~ VN-04 X3 and VN-19 X11 (renewal restarts the start date or waiting periods); X4, X5 and X8 ~ VN-04 X2, VN-19 X22, VN-23 D10-D11 and VN-06 F-LAPTOP (a benefit granted, then excluded); X7 ~ VN-19 X7 and VN-23 D14 (a breach-of-law exclusion with no causal link); X12 ~ VN-23 D8 (other insurance: several methods, no rule for choosing); X14 ~ VN-23 D26 (subrogation in health or accident cover); X18 ~ VN-23 D27 (no time for the insurer to pay); X13 and X21 ~ VN-04 X10 and X17, VN-23 D21 and VN-06 F-DISCRETION (discretion and termination at will); X22 ~ VN-19 X5 (age limits and continuous renewal); X27 ~ VN-04 X9, VN-23 D20 and VN-06 F-UNDEF (undefined or unused terms); X28 ~ VN-04 X12 and VN-19 X15 (numbering and cross-reference errors).

## VN-04 PVI comprehensive health care

Directory: `vn-pvi-comprehensive-health-care/encodings/legalese-2026-10-vn-04`.

### VN-04 X1 — Death after the term paid only if a partial payment came first
- **Class**: T7 internal inconsistency / T1 clocks and deadlines
- **Scenario**: Accident 1 November 2026, term ends 31 December, death from the accident 1 February 2027. Clause 10 ends liability after the term; A.1.4 (iv) pays the difference on a death within a year after a Benefit 2 payment. A family already paid 30,000,000 gets 70,000,000 more; one never paid gets nothing (fixture).
- **Who bears it**: beneficiary. **Money direction**: against the claimant.
- **Standing**: CONTESTED (fork F21 takes A.1.4 (iv) as the specific rule; clause 10 alone bars both).
- **Evidence**: `pvi-health-findings.l4:45`, `:50` (70,000,000), `:51` (0); src:176-189, 544-548.
- **Plain-English test of surprise**: Two families who lose someone to the same accident on the same day expect the same answer; the one already paid gets more, the other nothing.

### VN-04 X2 — An exclusion swallows the maternity care that B.3 sells
- **Class**: T6 granted then taken back / T7 internal inconsistency
- **Scenario**: B.3.1 covers "chi phí y tế chăm sóc thai sản và sinh đẻ" (maternity care and childbirth costs). Item 26 excludes care before and after childbirth, with no exception for B.3, under a Part that applies to all benefits; item 20 excludes routine antenatal check-ups. A pre-natal care claim under B.3 is refused; what is left is complications, caesarean and delivery.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `pvi-health-findings.l4:64` (pre-natal care under B.3 `EQUALS LIST (excluded by Part IV item 26)`); src:717-721, 907, 874-877.
- **Plain-English test of surprise**: A buyer of a benefit named maternity care expects antenatal care to be paid; the exclusions remove it.

### VN-04 X3 — Raising benefits at renewal restarts every waiting period
- **Class**: T10 waiting period or term interplay
- **Scenario**: A "continuous renewal" must carry benefits "thấp hơn hoặc bằng" (lower than or equal to) the old ones. A person insured since 2024 who adds a rider in 2026 is not continuously renewed, so the 365-day wait for chronic, special or pre-existing disease under A.2 restarts on 1 January 2026. Hypertension on 1 June 2026 is refused when upgraded, covered when renewed unchanged.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `pvi-health-findings.l4:78` (upgraded: `the event arose in the waiting period`), `:79` (unchanged: covered); `pvi-health-tests-part3.l4:105`; src:487-492, 575-583.
- **Plain-English test of surprise**: A customer buying more cover expects to keep waiting periods already served on unchanged benefits; the upgrade restarts them all.

### VN-04 X4 — Eligibility clause read at claim time refuses every claimant
- **Class**: T6 illusory cover / T5 term that decides outcomes
- **Scenario**: Item 34 excludes costs for a person "không đủ điều kiện tham gia bảo hiểm" (not eligible to join). Part I 2.2(c) makes a person under treatment for illness or injury ineligible. Tested at claim time, every claimant is under treatment, so every claim fails.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: CONTESTED (fork F5 tests 2.2 at enrolment; the claim-time reading, "the insurer's reading", "makes the cover illusory").
- **Evidence**: `pvi-health-findings.l4:88` (2.2 refuses a person under treatment); src:79, 940.
- **Plain-English test of surprise**: A customer expects eligibility to be checked once, at sign-up; read at claim time, being treated disqualifies the claim for that treatment.

### VN-04 X5 — An overnight stay under 24 hours falls between benefits
- **Class**: T13 other (a cover gap between two benefits) / T5 term that decides outcomes
- **Scenario**: Admitted 18:00, discharged 10:00 (16 hours): inpatient treatment (a night in a bed) but not a "hospitalisation" (24 continuous hours), so A.2.3(a) does not pay. Not being a hospitalisation, it is outpatient treatment by definition, which item 31 excludes without supplementary benefit 1.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL (fork F17: "Either way" such a stay is not a hospitalisation).
- **Evidence**: `pvi-health-findings.l4:102`, `:103`, `:104` (grounds: A.2.3 scope and `excluded by Part IV item 31`); src:349-355, 370-372, 587-588, 620-622, 928-929.
- **Plain-English test of surprise**: A patient kept in hospital overnight expects inpatient cover; a 16-hour stay is paid as neither inpatient nor outpatient.

### VN-04 X6 — Eight listed diseases are "pre-existing" whenever they arise
- **Class**: T5 term that decides outcomes / T10 waiting period interplay
- **Scenario**: Asthma, a herniated disc, a vestibular disorder, joint or spinal degeneration and four others are "được hiểu là Bệnh có sẵn" (deemed pre-existing) with no reference to when they arose. Asthma first diagnosed in month 6 of a first certificate waits 365 days, against 30 for an ordinary illness.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL (fork F16(a) takes the deeming as written).
- **Evidence**: `pvi-health-findings.l4:115` (asthma wait `EQUALS 365`), `:116` (refused: waiting period); src:276-285.
- **Plain-English test of surprise**: A customer expects "pre-existing" to mean present before cover began; here a disease first appearing mid-policy is pre-existing by label.

### VN-04 X7 — Partial-injury definition restricts total permanent injury
- **Class**: T7 internal inconsistency / T5 term that decides outcomes
- **Scenario**: A sentence saying "Thương tật toàn bộ vĩnh viễn chỉ bao gồm" (total permanent injury includes only) the annex items sits inside the definition of partial permanent injury. As written, a total permanent injury of 81% or more is paid only if the unpublished annex lists it.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: CONTESTED. The encoding reads it as a slip for "partial" (fork F15). Reading only.
- **Evidence**: reading only; src:251-254.
- **Plain-English test of surprise**: A customer expects a total disablement to be paid as such; a misplaced sentence makes it depend on a missing list.

### VN-04 X8 — No interest on any payment
- **Class**: T3 contract worse than the statute
- **Scenario**: A.1.4 says no amount paid under the Rules bears interest. The encoder notes that Law Art. 31(2) requires interest on a late payment.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LAW (fork F23: "Rules followed"; the conflict itself is reading only).
- **Evidence**: `pvi-health-findings.l4:121` `A.1.4 — the interest PVI pays on any amount under the Rules EQUALS 0`; src:542.
- **Plain-English test of surprise**: A claimant paid late expects interest for the delay; on the literal reading the Rules allow none.

### VN-04 X9 — Defined terms never used; a cited benefit never stated
- **Class**: T5 undefined term / T7 internal inconsistency
- **Scenario**: "Chi phí thông lệ và hợp lý" (customary and reasonable costs), temporary injury, pregnancy term and the pre-admission and post-discharge cost terms are defined and read by no operative clause. Item 29 excepts a home-care main benefit Part III does not contain. "Chủ hợp đồng" and "STBH" are used undefined. The customary-cost definition would cap payments, and nothing applies it.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL (reading only).
- **Evidence**: reading only; src:256, 374, 397, 413, 418, 423, 480, 688, 918-919.
- **Plain-English test of surprise**: A reader expects defined terms and cited benefits to do work; several do nothing, including a payment cap.

### VN-04 X10 — Insurer discretion with no criterion
- **Class**: T11 insurer discretion
- **Scenario**: PVI may refuse renewal or change terms at renewal; end the certificate for any reason on 30 days' notice; refuse "một phần hoặc toàn bộ" (part or all) of a payment for dishonesty "tùy theo mức độ vi phạm" (according to severity); and exclude dental care at facilities on a refusal list the document does not publish.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL (permissions encoded unconditionally; otherwise reading only).
- **Evidence**: `pvi-health-tests-part1.l4:98-128` (clause 5.2 early-termination traces); the refusal list is an input; src:114-116, 140-142, 208-209, 698.
- **Plain-English test of surprise**: A customer expects stated grounds and a published list; each decision is left to the insurer.

### VN-04 X11 — Insured person harmed by a beneficiary is refused
- **Class**: T2 overbroad exclusion
- **Scenario**: The insured person, assaulted by a spouse who is a named beneficiary, claims the hospital costs. Item 2 excludes harm intentionally caused by a beneficiary; its proviso saves only "những người thụ hưởng hợp pháp khác" (other lawful beneficiaries), and the insured person is not a beneficiary.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL (fork F29; Law Art. 40(1)(c), (2) noted as pointing the same way).
- **Evidence**: `pvi-health-findings.l4:132` (excluded by item 2); src:805-809.
- **Plain-English test of surprise**: A victim of an assault expects the victim's own hospital costs to be covered; an exclusion aimed at the wrongdoer refuses the victim.

### VN-04 X12 — Part V has no clause 2
- **Class**: T8 published document is incomplete / T13 other (numbering)
- **Scenario**: The claims part is numbered 1, 3, 4, 5. Whether a clause was dropped, in the mirror or in the original, cannot be told from the copy.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL (reading only).
- **Evidence**: reading only; src:950, 983.
- **Plain-English test of surprise**: A reader expects a complete claims procedure; a clause number is missing and its content unknown.

### VN-04 X13 — Six months or twelve months to claim
- **Class**: T7 internal inconsistency / T1 two clocks for one act
- **Scenario**: Clause 3 requires the dossier within 6 months of the event, on pain of losing the right; clause 5 gives 12 months. Event 15 March 2026, dossier sent 15 November: lost under clause 3, in time under clause 5. Clause 3 also names the "người thừa kế hợp pháp" (lawful heir) where the others name the beneficiary.
- **Who bears it**: insured / beneficiary. **Money direction**: against the claimant.
- **Standing**: LAW (fork F35 takes 12 months: Law Art. 30(1) fixes one year).
- **Evidence**: `pvi-health-findings.l4:143` (clause 3 alone: right lost), `:144` (encoded: survives); src:985-988, 1002-1003.
- **Plain-English test of surprise**: A claimant expects one deadline; the document gives two, six months apart.

### VN-04 X14 — 365-day waiting periods inside a one-year term
- **Class**: T10 waiting period or term interplay / T6 illusory cover
- **Scenario**: Chronic, special and pre-existing diseases (A.2, B.1) and childbirth (B.3) wait 365 days on a one-year term. On a first certificate from 1 January 2026, diabetes or a delivery on 31 December is still waiting; with a 29 February in the term, only the last day is covered. Death from such a disease (B.4) waits 730 days.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL (days counted per fork F22).
- **Evidence**: `pvi-health-findings.l4:155`-`:156` (refused), `:161`-`:162` (29 February covered, 28 February refused), `:165` (730); src:153-154, 573, 644, 761, 782.
- **Plain-English test of surprise**: A first-year buyer expects these benefits' premium to buy some cover; for these diseases it buys none, or a single day.

### VN-04 X15 — Emergency dental care after an accident waits 30 days
- **Class**: T10 waiting period interplay / T6 illusory cover
- **Scenario**: B.2 covers emergency dental care only within 24 hours of an accident, but the whole benefit waits 30 days with no exception for accidents (A.2 and B.1 have one). An accident on 10 January 2026 under a first-year certificate can never be followed by covered emergency dental care.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `pvi-health-findings.l4:177` (refused: `the event arose in the waiting period`); src:683-688, 700-702.
- **Plain-English test of surprise**: A customer expects accident cover to start at once, as it does for the other benefits; emergency dental care cannot be used in the first month.

### VN-04 X16 — The same dental clinic covered in Da Nang, not Hanoi
- **Class**: T13 other (location-dependent eligibility) / T7 internal inconsistency
- **Scenario**: In Hanoi and Ho Chi Minh City, dental care is covered only at state facilities, private and international hospitals, and facilities with a PVI agreement; elsewhere at any licensed facility issuing proper invoices. A licensed private dental clinic in Hanoi without a PVI agreement is outside cover; a clinic in Da Nang is inside.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `pvi-health-findings.l4:190` (NOT, Hanoi private clinic), `:191` (Da Nang clinic); `pvi-health-tests-part3.l4:179`; src:690-698.
- **Plain-English test of surprise**: A customer expects a licensed clinic to qualify wherever it is; in the two largest cities it does not.

### VN-04 X17 — Termination at will cuts off treatment already under way
- **Class**: T11 insurer discretion / T3 conflict with the statute
- **Scenario**: PVI may end the certificate for any reason on 30 days' notice, and liability then ends at once, including costs after termination of an event that began in cover. Admitted 29 June 2026 for four nights under a certificate terminated from 1 July 2026: paid 6,000,000 of 12,000,000 (fixture), two nights of four.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LAW (fork F38: Rules followed; Law Arts. 26 and 27 noted).
- **Evidence**: `pvi-health-findings.l4:209` `EQUALS 6_000_000`; src:114-116, 169-174.
- **Plain-English test of surprise**: A patient admitted while insured expects the whole stay to be covered; the insurer can end cover mid-stay.

### VN-04 X18 — Annex and schedule missing from the published copy
- **Class**: T8 published document is incomplete
- **Scenario**: The annex of injury percentages that Benefit 2 pays by, and the schedule that sets every sum insured and limit and defines the programmes, are absent. Printed pages run 2 to 23, then 27. Benefit 2 cannot be computed from the document.
- **Who bears it**: insured. **Money direction**: unclear.
- **Standing**: LITERAL (reading only).
- **Evidence**: reading only; src:252-253, 460-466, 529-530, 601-602, 1021-1022.
- **Plain-English test of surprise**: A buyer expects the policy to state the sums and percentages it pays; they are not in the published copy.

### VN-04 X19 — Congenital-disease exclusion against the therapeutic-abortion benefit
- **Class**: T7 internal inconsistency / T6 granted then taken back
- **Scenario**: B.3.1(a) covers a therapeutic abortion because of a genetic disease or congenital defect of the foetus. Item 17 excludes congenital and genetic diseases "và mọi biến chứng, hậu quả liên quan" (and all related consequences) for every benefit, so the insurer can argue the abortion is such a consequence.
- **Who bears it**: insured. **Money direction**: against the claimant (on the insurer's reading).
- **Standing**: CONTESTED (read for the insured, fork F41; reading only).
- **Evidence**: reading only; src:744-746, 861-865.
- **Plain-English test of surprise**: A customer expects a benefit that names this procedure to pay for it; the general exclusion gives the insurer an argument to refuse.

### VN-04 X20 — Special diseases that exclusions take back
- **Class**: T7 internal inconsistency / T6 granted then taken back
- **Scenario**: Alzheimer's disease and dementia are covered special diseases, while item 18 excludes mental and behavioural disorders; the Rules do not say whether dementia is one. Diseases of the blood-forming system are special diseases, while item 16 excludes bone marrow failure and leukaemia, which are such diseases.
- **Who bears it**: insured. **Money direction**: against the claimant (on the insurer's reading).
- **Standing**: CONTESTED (reading only; the encoding treats each named condition as named; the dementia classification is "outside knowledge, unverified").
- **Evidence**: reading only; src:287-293, 858-859, 867-868.
- **Plain-English test of surprise**: A customer expects a disease listed as covered to be paid; an exclusion elsewhere arguably removes it.

### VN-04 X21 — Conjunctive exclusions 9 and 33 catch almost nothing
- **Class**: T5 ambiguous term (conjunctive or disjunctive)
- **Scenario**: Item 9 bites only on a breach of the law AND of workplace-safety rules, recorded by an authority, so a road-traffic offence alone is not caught. Item 33's last limb bites only on a facility both unlicensed AND unable to issue invoices. The insurer's disjunctive reading would exclude far more.
- **Who bears it**: insurer. **Money direction**: against the insurer.
- **Standing**: CONTESTED (fork F31: conjunctive as written; Art. 24 points the same way).
- **Evidence**: `pvi-health-tests-exclusions.l4:125` (item 9 near miss: law broken, no safety breach), `:431` (item 33 near miss: unlicensed but invoicing); src:831-838, 934-938.
- **Plain-English test of surprise**: An insurer expects a law-breaking exclusion to catch law-breaking; as written, it also needs a workplace-safety breach.

### VN-04 X22 — Any illness linked to an announced epidemic is excluded
- **Class**: T2 exclusion overbroad
- **Scenario**: Item 7 excludes death, illness or injury arising "trực tiếp hoặc gián tiếp" (directly or indirectly) from an epidemic a central authority has announced, for every benefit. During an announced epidemic, a pneumonia linked to it is excluded however it was treated.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `pvi-health-findings.l4:219` (pneumonia `arising from an epidemic` → `excluded by Part IV item 7`); src:458, 824-826.
- **Plain-English test of surprise**: A customer expects health cover to matter most in an epidemic; that is when this wording withdraws it.

#### VN-04 row summary
- Findings in section 4: 22 (X1-X22).
- Most counterintuitive: X4 (read at claim time, being under treatment makes every claimant ineligible); X1 (a death after the term pays 70,000,000 to a family already paid for partial injury and 0 to one that was not); X14 (365-day waits on a one-year term leave first-year cover for chronic disease and childbirth at nothing or one day).
- Matches in this group: X1 ~ VN-23 D4 and VN-06 F-PA-ONCE (a death after a partial-disablement payment is paid less, or nothing); X5 ~ VN-03 X6 and X25 and VN-19 X8 (a 24-hour hospitalisation test splits an overnight stay); X3 ~ VN-03 X3 and VN-19 X5 and X11 (renewal changes restart waiting periods or end continuity); X14 and X15 ~ VN-19 X24 (a waiting period that runs into or past the term); X18 ~ VN-03 X0 and VN-19 X2 (injury tables missing from the published document); X13 ~ VN-03 X2, VN-19 X18 and VN-23 D9 (two clocks for one act); X20 ~ VN-19 X22 (covered special diseases, including blood-system diseases, excluded elsewhere); X2 and X19 ~ VN-03 X4 and X5 (a benefit granted, then excluded); X4 ~ VN-19 X26 (an eligibility bar on anyone under treatment); X10 and X17 ~ VN-03 X13 and X21, VN-23 D21 and VN-06 F-DISCRETION (discretion and termination at will); X21 ~ VN-03 X7, VN-19 X7 and VN-23 D14 (breach-of-law exclusions; here the conjunctive reading narrows them instead); X9 ~ VN-03 X27 and VN-23 D20 (undefined or unused terms); X12 ~ VN-03 X28 (numbering errors).

## VN-19 Tasco combined health, with the annex lists

Directory: `vn-tasco-combined-health/encodings/legalese-2026-10-vn-19`.
The encoder marks X2, X18 and X22 (★) as the three most likely to matter to a policyholder.
Test-file names below drop the `tasco-vn19-` prefix where unambiguous: `tests-cover.l4` is `tasco-vn19-tests-cover.l4`, and so on.

### VN-19 X2 — Injury and surgery tables are missing from the document (★)
- **Class**: T8 published document is incomplete
- **Scenario**: Partial permanent disability, temporary injury (standard programme) and every surgery pay a percentage of the sum insured "in the table", and the 19 published pages contain no table. With a rate supplied, II.2 at 30% pays 6,000,000 and III.3 at 10% pays 2,000,000 (fixture); without one, no answer can be given.
- **Who bears it**: insured. **Money direction**: unclear.
- **Standing**: LITERAL.
- **Evidence**: `tests-cover.l4:124` (30% → `payable 6000000`), `:125` and `:104` (`#ASSERT REFUSED` with no percentage); src:200, 208, 228-229, 405-420, 451-464.
- **Plain-English test of surprise**: A buyer expects to be able to read what an injury or operation pays; the insurer's unpublished table decides.

### VN-19 X18 — The notice period can outlast the one-year claim bar (★)
- **Class**: T1 two clocks for one act / T12 forfeiture by notice
- **Scenario**: Notice is due within 120 days of discharge, end of treatment or death; documents within a year of the insured event, after which "mọi yêu cầu giải quyết quyền lợi không có giá trị" (every claim is void). Illness from 10 January 2026, death 20 November: notice due 20 March 2027, claim barred after 10 January 2027. Any trigger after day 245 does this.
- **Who bears it**: beneficiary. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `tests-claims.l4:37`-`:39` (notice due 2027-03-20; bar passed), `:44`-`:45` (day 245 FALSE, day 246 TRUE); src:649-651, 653-655.
- **Plain-English test of surprise**: A beneficiary using the full notice period granted expects the claim to survive; it is already barred.

### VN-19 X22 — Special diseases covered from year two are excluded outright (★)
- **Class**: T6 granted then taken back / T7 internal inconsistency
- **Scenario**: 2.11 lists tuberculosis, malaria, dialysis and blood and marrow diseases as special diseases, which 11.17 covers from the second year; 11.9 excludes "suy tủy, bạch cầu, chạy thận nhân tạo; sốt rét, lao" outright, and the exclusions control. A second-year tuberculosis stay is not payable, while another second-year special disease is paid (500,000, fixture). The overlap is partial for the other items.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `tests-cover.l4:290` (tuberculosis: `not payable`, `excluded by Article 11.9`), comment `:287`-`:289`; src:84-92, 600, 630-632.
- **Plain-English test of surprise**: A customer told tuberculosis is covered from year two expects it to be paid then; another clause says never.

### VN-19 X1 — A group of exactly 100 persons falls between two columns
- **Class**: T5 term that decides outcomes / T13 other (boundary gap)
- **Scenario**: The waiting-period table has columns for contracts "dưới 100 người" (under 100) and groups "trên 100 người" (over 100); 10.2 and 11.17 also say "over 100". An employer insuring exactly 100 staff has no column where the two differ (rows 2, 3, 5, 6). 99 and 150 are answered, and so is an accident at 100, where the columns agree.
- **Who bears it**: policyholder / insured. **Money direction**: unclear.
- **Standing**: LITERAL.
- **Evidence**: `tests-cover.l4:189` (`#ASSERT REFUSED` for 100 persons, illness), `:192` (accident at 100: payable), `:193`-`:194` (99 and 150: payable); src:506, 533, 631-632.
- **Plain-English test of surprise**: An employer with 100 staff expects one of the two columns to apply; neither does.

### VN-19 X3 — "Chỉnh hình" excludes orthopaedics
- **Class**: T2 overbroad exclusion / T5 term that decides outcomes
- **Scenario**: 11.11 excludes cosmetic treatment, cosmetic surgery and "chỉnh hình", which is the ordinary word for orthopaedics, so read literally a broken leg set surgically after an accident is excluded. The neighbouring words (cosmetic) suggest corrective cosmetic work was meant; the rules do not say so.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL ("read literally"; whether an operation is "chỉnh hình" is the caller's classification).
- **Evidence**: `tests-cover.l4:286` (accident claim → `not payable`, `excluded by Article 11.11`); src:607.
- **Plain-English test of surprise**: An accident victim expects the setting of a broken bone to be the core of accident cover; one word arguably excludes it.

### VN-19 X4 — Any claim forfeits the cancellation refund
- **Class**: T12 forfeiture by condition
- **Scenario**: On the policyholder's cancellation, 4.2(a) refunds 70% only if no claim ("bất kỳ khiếu nại") arose, even one Tasco refused; otherwise the rules say nothing, so on their face Tasco keeps the whole premium. With 73 of 365 days left on 1,200,000 (fixture): 168,000 without a claim; no answer with one.
- **Who bears it**: policyholder. **Money direction**: against the claimant (the policyholder).
- **Standing**: LITERAL ("on their face"; fork F24 declines the with-claim case by name).
- **Evidence**: `tests-ch1.l4:205` (`EQUALS 168000`), `:206` (`#ASSERT REFUSED` with a claim); src:311-314.
- **Plain-English test of surprise**: A customer who once made a refused claim expects the same refund as anyone else; the wording gives none.

### VN-19 X5 — After 60, cover depends on the insurer renewing and on never lowering it
- **Class**: T11 insurer discretion / T10 term interplay
- **Scenario**: Over 60, a person is insured only on continuous renewal from 60; Tasco may refuse renewal with no criterion, and continuity needs unchanged benefits. An insured aged 61 whose renewal is refused, or who lowers the scope C sum insured from 20 to 10 million to save premium, can never be insured under these rules again.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL (forks F1, F27).
- **Evidence**: `tests-ch1.l4:49` (61, renewing on the same sums: in), `:52` (scope C lowered: out); src:11-12, 342, 348-349.
- **Plain-English test of surprise**: An older customer trimming cover to afford it expects to stay insured on less; the trim ends eligibility for good.

### VN-19 X6 — Climbing with safety gear is excluded; without it, not
- **Class**: T5 term that decides outcomes / T2 exclusion misaligned with risk
- **Scenario**: 2.26 lists climbing "có sử dụng thiết bị hướng dẫn và/hoặc dụng cụ bảo hộ" (using guidance equipment and/or protective gear) as dangerous. So a roped climber who falls is excluded under 11.6 and a free-solo climber is not; deep-sea diving likewise only with a hard helmet and oxygen tank.
- **Who bears it**: insured (the careful climber). **Money direction**: against the claimant (careful climber); against the insurer (free-solo climber).
- **Standing**: LITERAL (fork F18).
- **Evidence**: `tests-ch1.l4:168`-`:169`; `tests-cover.l4:262` (with gear: excluded), `:263` (without: not); src:243-246.
- **Plain-English test of surprise**: Anyone would expect the safer climber to be the one covered; the wording covers the reckless one.

### VN-19 X7 — Exclusions with no link to the insured event
- **Class**: T2 exclusion with no causal link
- **Scenario**: 11.4 (breach of traffic law, or of a local authority's or social organisation's rule) and 11.14 state no link to the insured event; read literally, a traffic ticket excludes an unrelated pneumonia stay. Even on the narrower reading, a ticket issued on the drive to hospital excludes it.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL for the broad version; the narrower reading (fork F33) still fails the drive-to-hospital case.
- **Evidence**: `tests-cover.l4:254`-`:255` (illness stay excluded by 11.4); src:581-583, 617.
- **Plain-English test of surprise**: A patient with pneumonia expects a traffic ticket to be irrelevant; the exclusion has no causal test.

### VN-19 X8 — Two day-count methods count the same stay differently
- **Class**: T5 term that decides outcomes / T7 internal inconsistency
- **Scenario**: At a hospital that records hours, a 23-hour stay over midnight (20:00 1 May to 19:00 2 May) is not a hospitalisation and a 47-hour stay counts 1 day. At one that does not, the date formula makes a 1-2 May stay 2 days and a hospitalisation.
- **Who bears it**: insured. **Money direction**: against the claimant (where hours are recorded).
- **Standing**: LITERAL (forks F11 and F12).
- **Evidence**: `tests-ch1.l4:136` (23 hours: NOT a hospitalisation), `:137` (47 hours `EQUALS 1`), `:141`-`:142` (no hours recorded: 2 days, a hospitalisation); src:154-158.
- **Plain-English test of surprise**: A patient expects the same stay to count the same wherever it happens; the hospital's record-keeping changes the answer.

### VN-19 X9 — Drink-driving limits printed in impossible units
- **Class**: T5 term that decides outcomes / T13 other (unit error)
- **Scenario**: 11.3 sets limits of "0,25% mililit/lít khí thở" and "50 mililit/100 mililit máu". Fifty millilitres of alcohol in 100 ml of blood is half the blood, so read as printed the blood limb never applies; the printed equivalent of 10.9 mmol matches 50 milligrams, so milligrams were meant.
- **Who bears it**: insurer. **Money direction**: against the insurer (as printed).
- **Standing**: CONTESTED. The encoding takes the figures as printed but in mg units, "which 10,9mmol confirms" (fork F34).
- **Evidence**: reading only; the L4 tests both sides of 0.25 and 50; src:577-578.
- **Plain-English test of surprise**: A reader expects a drink-driving limit a driver could exceed; as printed, no living driver can.

### VN-19 X10 — The special-disease list includes things that are not diseases
- **Class**: T5 term that decides outcomes
- **Scenario**: The special-disease list includes blood pressure, coronary surgery, bone marrow and "tái tạo dây chằng" (ligament reconstruction). Read literally, a ligament reconstruction after a first-year sports injury is a special disease, excluded in year one by 11.17.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL (reading only).
- **Evidence**: reading only (the list is carried as data, its count of 46 tested); src:84-92.
- **Plain-English test of surprise**: A sports-injury patient expects knee surgery to be accident treatment; the list labels it a first-year-excluded disease.

### VN-19 X11 — Article 11.8 can take back what 11.17 gives
- **Class**: T6 granted then taken back / T10 term interplay
- **Scenario**: An illness is diagnosed in year 1 with surgery indicated; the surgery is done in year 2 after a continuous renewal. 11.17 covers pre-existing conditions from year 2, but 11.8 excludes an indication "có từ trước ngày bắt đầu bảo hiểm" (existing before the start date), which on fork F9 is this year's start.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL (reading only; depends on fork F9).
- **Evidence**: reading only; src:596-598, 630-632.
- **Plain-English test of surprise**: A renewing customer told pre-existing conditions are covered from year two expects the indicated surgery to be paid; a second exclusion removes it.

### VN-19 X12 — "Medical expenses" is defined for injuries only
- **Class**: T5 term that decides outcomes / T7 internal inconsistency
- **Scenario**: "Chi phí y tế" is defined as costs incurred when the insured "phải điều trị thương tật" (must treat an injury), yet Article 3 uses the term for injury and illness alike. (Inferred) On the definition alone, illness costs would not be medical expenses.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL (reading only).
- **Evidence**: reading only; src:231-236, 282-290.
- **Plain-English test of surprise**: A reader expects "medical expenses" in a health policy to include illness; the definition names injury only.

### VN-19 X13 — Poisoning is defined and never used
- **Class**: T5 term that decides outcomes
- **Scenario**: Poisoning is defined, but no provision uses "ngộ độc", and the rules do not say whether poisoning is an accident (scope B) or an illness (scope C), which decides which benefits apply.
- **Who bears it**: insured. **Money direction**: unclear.
- **Standing**: CONTESTED (fork F5: "not resolved in the L4"; the caller classifies). Reading only.
- **Evidence**: reading only; src:248-254.
- **Plain-English test of surprise**: A food-poisoning victim expects to know which cover applies; the defined term is never connected to either.

### VN-19 X14 — Read literally, exhausting one scope ends the whole contract
- **Class**: T6 illusory cover / T5 term that decides outcomes
- **Scenario**: 4.1(c) ends the contract when "Số tiền chi trả bảo hiểm bằng Số tiền bảo hiểm" (payments equal the sum insured). An insured who uses the whole 20 million scope C sum insured on hospital bills in May and dies in an accident in June: on the literal reading the contract ended in May.
- **Who bears it**: beneficiary. **Money direction**: against the claimant.
- **Standing**: CONTESTED (fork F21 ends only the exhausted scope's cover).
- **Evidence**: `tests-ch1.l4:200` (read literally, the whole contract has ended), `:201`; src:300.
- **Plain-English test of surprise**: A customer who exhausts hospital cover expects accident and death cover to continue; read literally, all of it ends.

### VN-19 X15 — Article 4.4 cites the wrong Article and spares death only
- **Class**: T7 internal inconsistency / T1 clocks and deadlines
- **Scenario**: 4.4's exception for consequences after the contract cites "Điều 8" where the 180-day rule is Article 9, and spares death only. An accident on the last day causing paralysis certified six months later is, read literally, a consequence after the contract; a death on 15 January 2027 from a 1 November 2026 accident is paid.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: CONTESTED (fork F25 dates a consequence from its onset).
- **Evidence**: `tests-cover.l4:134` (the death: paid); otherwise reading only; src:331-332, 476-479.
- **Plain-English test of surprise**: A customer expects a disability from an in-term accident to be covered like a death; the exception names death alone.

### VN-19 X16 — A waiting period for a benefit that does not exist
- **Class**: T7 internal inconsistency / T13 other (phantom benefit)
- **Scenario**: Waiting-period row 4 covers death and total permanent disability from pre-existing disease, special disease and maternity, but scope A pays death from illness only, and no row of Article 8 pays total permanent disability from illness.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL (reading only).
- **Evidence**: reading only; comment at `tasco-vn19-art10-waiting.l4:108`; src:518-520, 373.
- **Plain-English test of surprise**: A reader seeing a waiting period for illness disability expects such a benefit to exist; none does.

### VN-19 X17 — Read literally, a paralysis qualifies on one day only
- **Class**: T1 clocks and deadlines / T6 illusory cover
- **Scenario**: Death or total permanent disability must occur "trong vòng 180 ngày" (within 180 days) of the accident, and paralysis may be certified "không sớm hơn 180 ngày" (no earlier than 180 days). If a disability occurs when certified, only certification on exactly day 180 qualifies.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: CONTESTED. The encoding reads occurrence as onset (fork F17, Art 24) and pays a paralysis certified on day 181.
- **Evidence**: `tests-cover.l4:142` (179: NOT), `:143` (180: TRUE), `:144` (181: NOT); src:476-479, 193-195.
- **Plain-English test of surprise**: A paralysed accident victim expects any paralysis lasting six months to qualify; read literally, the paperwork must land on one exact day.

### VN-19 X19 — Tasco can extend its own deadlines without limit
- **Class**: T11 insurer control over a condition / T1 clocks and deadlines
- **Scenario**: Tasco pays within 15 days of complete documents and gives refusal reasons within 30, "không bao gồm trường hợp phải xác minh Hồ sơ" (except where verification is needed); 13.7 lets Tasco request any other documents. Both clocks wait on completeness, verification removes the refusal deadline, and a refusal may take 30 days where a payment must take 15.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `tests-claims.l4:52` (refusal deadline with verification: REFUSED), `:57`-`:63` (`#TRACE` runs); src:660-661, 663-666, 715-716.
- **Plain-English test of surprise**: A claimant expects the 15-day payment promise to bind; the insurer controls when the clock starts.

### VN-19 X20 — Hospital lists published with the rules but not part of them
- **Class**: T8 published document is incomplete / T5 term that decides outcomes
- **Scenario**: "PHỤ LỤC 5" lists direct-billing hospitals and another list names excluded facilities, said to be updated on Tasco's website; the rules mention neither. Treatment at a listed excluded facility that meets 2.17 has no rule excluding it. Annexes 1 to 4 were not found; one list row has no mark.
- **Who bears it**: insured. **Money direction**: unclear.
- **Standing**: LITERAL (fork F40: "no clause refers to either list").
- **Evidence**: `tests-annexes.l4:392` (row 4 unmarked); lists in `tasco-vn19-annex-*.l4`; sources G1, E1-E2.
- **Plain-English test of surprise**: A customer handed an excluded-facilities list expects it to bind; nothing in the rules says it does, or which version.

### VN-19 X21 — No document rule for a sum insured of exactly 20 million
- **Class**: T5 term that decides outcomes / T13 other (boundary gap)
- **Scenario**: Article 13 sets payment documents for sums insured "trên 20 triệu đồng" (over 20 million) and "dưới 20 triệu đồng" (under 20 million); the standard programme runs up to and including 20 million. Every treatment-cost claim on a standard contract at its maximum has no document rule; 10 and 50 million are answered.
- **Who bears it**: insured. **Money direction**: unclear.
- **Standing**: LITERAL.
- **Evidence**: `tests-claims.l4:84` (`#ASSERT REFUSED` documents at 20 million), `:81`-`:82` (other sums answered); src:686, 690, 392.
- **Plain-English test of surprise**: A customer on the standard plan's top tier expects to know what to file; the rule skips that exact figure.

### VN-19 X23 — Late-found ineligibility: insurer keeps the premium and pays nothing
- **Class**: T13 other (premium retained, cover void) / T3 possible conflict with the statute
- **Scenario**: In month 11 Tasco discovers the insured was under treatment at the start (1.2(c)). It refunds one month's premium and refuses every claim of the eleven months.
- **Who bears it**: insured / policyholder. **Money direction**: against the claimant.
- **Standing**: LITERAL (reading only). LAW note: Art 25.2 makes the parties return what each received where a contract is void; whether ineligibility makes this contract void is "outside knowledge, unverified".
- **Evidence**: reading only; `tests-ch1.l4:204` computes the refund (`EQUALS 240000` on 1,200,000 with 73 days left, fixture); src:302-305.
- **Plain-English test of surprise**: A customer whose cover is voided expects the premium back; the insurer keeps eleven months of it.

### VN-19 X24 — In a leap year, "365 days" and "the second year" differ by a day
- **Class**: T10 waiting period or term interplay
- **Scenario**: Continuous participation from 1 January 2028. A special disease on 31 December 2028 has served the 365-day waiting period, yet is still in the first year, so 11.17 excludes it.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `tests-cover.l4:218` (`Article 10, the waiting period has run`: TRUE), `:219` (`Article 11.17 applies to`: TRUE); src:510-512, 630-632.
- **Plain-English test of surprise**: A customer who has served the waiting period expects cover; a second clock still excludes the claim for one day.

### VN-19 X25 — The rules carry no date or decision number
- **Class**: T8 published document is incomplete
- **Scenario**: The published rules have no date of issue and no decision number. (Inferred) A reader cannot tell which version is in force or when it was approved.
- **Who bears it**: unclear. **Money direction**: no money.
- **Standing**: LITERAL (reading only).
- **Evidence**: reading only; src:1-6, 824.
- **Plain-English test of surprise**: A reader expects an insurer's rules to say when and under which decision they were issued; these do not.

### VN-19 X26 — Several exclusions read literally reach almost everything
- **Class**: T2 overbroad exclusion / T5 undefined term
- **Scenario**: 11.8 excludes treatment "theo yêu cầu của Người được bảo hiểm" (at the insured's request); 1.2(c) refuses anyone under any treatment at the start; 1.2(a) refuses "bệnh thần kinh" (nervous disease), undefined and wide enough for a migraine.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: CONTESTED. The encoding reads 11.8 as treatment without medical indication (fork F35) and 1.2 at the start of the contract (fork F3).
- **Evidence**: reading only; src:598, 17, 15.
- **Plain-English test of surprise**: A patient expects asking for treatment, or having a migraine, to be harmless; read literally, each can exclude the claim.

### VN-19 X27 — A doctor of unstated allegiance settles aggravation
- **Class**: T11 insurer discretion
- **Scenario**: Article 9's second paragraph makes "Kết luận của bác sĩ" (a doctor's conclusion) full and lawful proof that an injury was aggravated, without saying whose doctor.
- **Who bears it**: insured. **Money direction**: against the claimant (inferred: a finding of aggravation reduces the payment).
- **Standing**: LITERAL (reading only).
- **Evidence**: reading only; src:488-489.
- **Plain-English test of surprise**: A claimant expects a disputed medical finding to be open to challenge; the clause makes one doctor's word conclusive.

### VN-19 X28 — An accident victim's hospital days are not paid by the day
- **Class**: T13 other (cover gap between two benefits) / T7 internal inconsistency
- **Scenario**: Scope C (illness, sickness, maternity) does not reach accidents, so a hospital stay after an accident cannot claim III.1's daily benefit. II.3 pays a temporary injury by the table's percentage, whatever the length of the stay.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL (fork F37: "the text").
- **Evidence**: `tests-cover.l4:29` (III.1 for an accident → `not payable`, Article 7.2); src:375, 413-420.
- **Plain-English test of surprise**: A customer expects a long hospital stay after an accident to pay more than a short one; it pays the same table percentage.

### VN-19 X29 — The one-year claim bar is shorter than the Law's
- **Class**: T3 contract worse than the statute / T1 clocks and deadlines
- **Scenario**: Claims are barred one year after the insured event. The encoder notes Law Art 30.2 runs the year from when a claimant who did not know of the event learned of it; the rules make no such allowance.
- **Who bears it**: beneficiary / insured. **Money direction**: against the claimant.
- **Standing**: LAW (fork F42; not encoded).
- **Evidence**: reading only; src:653-655.
- **Plain-English test of surprise**: A beneficiary who learns of a death late expects time to run from that knowledge; the rules run it from the event.

### VN-19 X30 — Complaint and suit are run together
- **Class**: T7 internal inconsistency / T1 clocks and deadlines
- **Scenario**: 16.1 bars complaints about a claims decision after 90 days. 16.2, the clause about suits, says that after 3 years "mọi khiếu nại đều không có giá trị" (every complaint has no validity), using the word for complaint.
- **Who bears it**: insured. **Money direction**: unclear.
- **Standing**: LITERAL (reading only).
- **Evidence**: `tests-claims.l4:101` (complaint limit `EQUALS YMD 2026 8 30`), `:102` (suit limit `EQUALS YMD 2029 6 1`); src:807-810, 812-813.
- **Plain-English test of surprise**: A claimant expects separate, clear limits for complaining and for suing; the wording blurs them.

#### VN-19 row summary
- Findings in section 4: 30 (X1-X30).
- Most counterintuitive: X6 (a climber using safety gear is excluded; one without it is covered); X18 (a beneficiary who gives notice within the 120 days granted can find the claim already barred by the one-year limit); X22 (tuberculosis and malaria are covered "from the second year" by one clause and excluded outright by another).
- Matches in this group: X17 ~ VN-03 X1 (a disablement must fall inside a window and also last as long as the window); X18 ~ VN-03 X2, VN-04 X13 and VN-06 F-24H (two clocks for one act); X29 ~ VN-03 X19 (fork F41) and VN-04 X13 (a claim bar measured against Law art 30); X2 ~ VN-03 X0 and VN-04 X18 (injury or surgery tables missing); X22 ~ VN-04 X20 (covered special diseases excluded elsewhere); X8 ~ VN-03 X6 and VN-04 X5 (how a hospital stay is counted); X6 ~ VN-06 VN-F3 (climbing defined by whether ropes or gear are used); X7 ~ VN-03 X7 and VN-23 D14 (breach-of-law exclusion with no causal link); X11 ~ VN-03 X3, and X5 ~ VN-04 X3 and VN-03 X22 (renewal, continuity and age); X24 ~ VN-04 X14 (waiting period against the term); X1 and X21 ~ VN-23 D6, D16 and D17 (a boundary value in no band, or two); X19 and X27 ~ VN-04 X10 and VN-23 D21 (insurer control and discretion); X28 ~ VN-03 X25 (a cover gap between two benefits); X4 ~ VN-06 F-CANCEL-REFUND (premium refund lost); X15 ~ VN-03 X28 and VN-04 X12 (cross-reference and numbering errors).

## VN-23 Liberty personal accident (group, business)

Directory: `vn-liberty-personal-accident/encodings/legalese-2026-10-vn-23`.
The encoder numbers findings D1-D28 and D31; there is no D29 or D30.

### VN-23 D1 — "Performing work" exclusion removes every injury at work
- **Class**: T2 overbroad exclusion / T5 term that decides outcomes
- **Scenario**: Exclusion 6(d) excludes injury during military drills or combat, or service in the armed forces or police, "hoặc đang thực hiện công việc" (or while performing work). Read literally, the last words exclude any insured performing work: an office employee who falls at a desk is excluded, under a business group accident policy.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: CONTESTED. The encoding confines the words to the forces and police on duty (fork F22, Art 24).
- **Evidence**: `lpa-tests-findings.l4:78` (`general exclusion 6(d) read literally excludes performing work`: TRUE), `:77` (encoded: `EMPTY`); src:785-787.
- **Plain-English test of surprise**: An employer buying group accident cover expects workplace injuries to be covered; read literally, they are excluded.

### VN-23 D2 — Cover ends retroactively on the day the insured left Vietnam
- **Class**: T1 clocks and deadlines / T12 forfeiture by notice
- **Scenario**: 7.1(e) ends cover on the day the employee left Vietnam once an absence passes 180 days without notice or agreement. Leaving 1 March 2026 and injured abroad on 1 April: with a 181-day absence, 1 April was not covered; with 180 days, it was. 3(f) separately caps stays abroad at 180 days.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL ("The day named is the departure (literal)", fork F27).
- **Evidence**: `lpa-tests-findings.l4:85` (181 days: not in force), `:86` (180: in force); src:1189-1191, 1255-1260.
- **Plain-English test of surprise**: An insured hurt in the first month abroad expects that day's cover to be settled; it depends on when the insured later comes home.

### VN-23 D3 — Unpaid premium: nothing, 0.1%, or the full benefit
- **Class**: T7 internal inconsistency / T3 contract worse than the statute
- **Scenario**: If the premium is unpaid, 4(a)(ii) and 4(b) give no liability, while 16B(b) pays prior events at most 0.1% of the limit; the encoder notes Law art 27(1)(b) requires such events to be paid. On a 400,000 daily allowance (fixture), 0.1% is 400 đồng. The employee bears the employer's failure.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LAW (fork F31 takes 16B(b); its cap conflicts with art 27(1)(b)).
- **Evidence**: `lpa-tests-findings.l4:94`-`:95` (0.1% caps); `lpa-tests.l4:904` (`claim D`: allowance 400); src:1199-1214, 1552-1581.
- **Plain-English test of surprise**: An employee expects cover the employer arranged to pay out; an employer's missed premium cuts a day's allowance to 400 đồng.

### VN-23 D4 — Death top-up after a permanent-injury payment is almost unreachable
- **Class**: T1 clocks and deadlines / T4 payout arithmetic
- **Scenario**: Partial permanence exists only from 52 weeks after the accident, but 1(b)'s top-up needs death within 52 weeks of the injury. Right eye lost 10 January 2026, 40% paid (400,000,000 on a 1,000,000,000 limit, fixture); death 10 January 2027: nothing more. The same death with no permanent-injury claim pays 1,000,000,000.
- **Who bears it**: beneficiary. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `lpa-tests-findings.l4:103` (52 weeks end 2027-01-09), `:104` (`EQUALS 0`), `:105` (`EQUALS 1000000000`); src:156-163, 552-558.
- **Plain-English test of surprise**: A family expects an earlier injury payment to be topped up to the death benefit; having claimed it leaves the family 600,000,000 worse off.

### VN-23 D5 — General provision 13's deadlines cannot all be met
- **Class**: T1 a bar that runs before the right arises / T12 forfeiture by notice
- **Scenario**: If "sự kiện bảo hiểm" (the insured event) is the accident, the one-year filing limit expires before a total permanent injury can exist (104 weeks). Forms are due within 30 days and 13(d) voids late claims, so the year does no work: notice on day 31 voids all.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: CONTESTED for the first limb (fork F2); LITERAL for 13(d), "applied as written" (fork F39; Law art 30 noted).
- **Evidence**: `lpa-tests-findings.l4:112`, `:116`-`:117`; `lpa-tests.l4:865` (`claim B`: all void); src:1479-1486, 1515-1516.
- **Plain-English test of surprise**: A claimant told there is a year to claim expects day 31 to be safe; it voids the claim.

### VN-23 D6 — Teeth bands have a gap, an overlap and a dead row
- **Class**: T7 internal inconsistency / T4 payout arithmetic
- **Scenario**: Exactly 8 lost teeth fall in no band; more than 8 that dentures can replace, in none; 3 teeth are in two bands (8% and 3%); and the "1 to 3 teeth, 3%" row sits under the 5% floor, so on its own it never pays: 2 teeth pay 0.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL (fork F7 takes 8% for 3 teeth).
- **Evidence**: `lpa-tests-findings.l4:122`-`:123` (8 and 12 teeth: `NOTHING`), `:124`-`:125` (two rates), `:127` (3 teeth → 8%), `:128` (2 teeth → 0); src:371-374, 467.
- **Plain-English test of surprise**: A claimant expects every number of lost teeth to have a rate; some have none and one row can never pay.

### VN-23 D7 — Many finger and toe combinations have no price
- **Class**: T8 schedule incomplete / T11 insurer discretion
- **Scenario**: 10 of 31 finger sets and 20 of 31 toe sets have no row (for example two fingers without the thumb, all five fingers, two toes) and go to the Company's sole discretion. The 50% ankylosis rule for lesser toes has no amputation amount to halve; ankylosis of the non-dominant middle finger (2.5%) is under the 5% floor.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `lpa-tests-findings.l4:200` (`EQUALS 10`), `:202` (`EQUALS 20`), `:204` (`#ASSERT REFUSED`: "its rate is for the Company to decide by comparison"), `:206` (2.5%); src:403-411, 448-450, 453-454, 459-465.
- **Plain-English test of surprise**: A claimant who loses all five fingers expects a printed rate; the table has none, so the insurer decides.

### VN-23 D8 — Three rules for expenses another contract also covers
- **Class**: T7 internal inconsistency / T4 payout arithmetic
- **Scenario**: Limitation 4 pays the excess; special exclusion 3 pays nothing; general provision 11 pays the excess or a rateable share, with no criterion. Bills of 10,000,000, 4,000,000 met elsewhere, limits 50,000,000 of 100,000,000 (fixture): 6,000,000, 0 or 5,000,000.
- **Who bears it**: insured. **Money direction**: unclear.
- **Standing**: CONTESTED (fork F14 takes limitation 4 for benefit C).
- **Evidence**: `lpa-tests-findings.l4:213` (excess `EQUALS 6000000`), `:214` (rateable `EQUALS 5000000`); src:573-578, 887-889, 1449-1453.
- **Plain-English test of surprise**: A claimant with two policies expects one rule; the wording gives three answers from 0 to 6,000,000.

### VN-23 D9 — 52 weeks or 12 months for medical expenses
- **Class**: T7 internal inconsistency / T1 two clocks for one act
- **Scenario**: The definition of medical expenses runs 12 months from the injury; benefit C runs 52 weeks. Accident 10 March 2026: a bill on 10 March 2027 is outside 52 weeks (ended 9 March) and inside 12 months.
- **Who bears it**: insured. **Money direction**: against the claimant (on the 52-week reading).
- **Standing**: CONTESTED (fork F13 takes the longer 12 months, Art 24; the encoding pays 1,000,000, fixture).
- **Evidence**: `lpa-tests-findings.l4:220` (52 weeks end 2027-03-09), `:221` (`EQUALS 1000000`); src:229-231, 512-513.
- **Plain-English test of surprise**: A claimant expects one window for medical bills; the policy gives two that differ by a day.

### VN-23 D10 — Dental surgery is both included and excluded
- **Class**: T7 internal inconsistency
- **Scenario**: Definition (b) of medical expenses includes "phẫu thuật nha khoa" (dental surgery); general exclusion 12 excludes all treatment "liên quan đến nha khoa" (related to dentistry). Dental surgery after an accident injury is both.
- **Who bears it**: insured. **Money direction**: against the claimant (on the exclusion).
- **Standing**: CONTESTED (fork F15 covers it, Art 24). Reading only.
- **Evidence**: reading only; src:232-233, 829.
- **Plain-English test of surprise**: An accident victim who loses teeth expects the dental surgery the definition names to be paid; the exclusion says otherwise.

### VN-23 D11 — Asphyxiation by fumes: extended and excluded
- **Class**: T7 internal inconsistency / T6 granted then taken back
- **Scenario**: Special provision 5 extends cover to sudden asphyxiation by toxic fumes; general exclusion 5(g), unqualified, excludes "hít phải hơi độc, khí độc, chất độc" (inhaling toxic vapour, gas or poison).
- **Who bears it**: beneficiary / insured. **Money direction**: against the claimant (on the exclusion).
- **Standing**: CONTESTED (fork F21: the specific extension prevails).
- **Evidence**: `lpa-tests-findings.l4:227` (encoded: `EMPTY`); src:616-619, 770-771.
- **Plain-English test of surprise**: A family told fume asphyxiation is specially covered expects payment; a general exclusion names the same event.

### VN-23 D12 — Any injury must be notified "at once", or cover ends
- **Class**: T12 forfeiture by notice / T7 internal inconsistency
- **Scenario**: 7.1(f) ends cover on the day the insured fails to notify "ngay" (at once) a change that increases the risk, including any injury arising in the period; 13(a) allows 30 days to notify an injury. Read literally, the claimed injury itself, notified on day 20, ends cover on the day of the accident.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: CONTESTED (fork F28 notifies the claimed injury under 13(a)).
- **Evidence**: `lpa-tests-findings.l4:233` (not in force on the day of an unnotified change); src:1261-1267, 1291-1297, 1328-1335.
- **Plain-English test of surprise**: A claimant who reports within the 30 days allowed expects to be covered; read literally, the injury ended cover the day it happened.

### VN-23 D13 — The all-benefits cap rests on an optional benefit
- **Class**: T4 payout arithmetic / T6 illusory cover
- **Scenario**: 1(c) caps all benefits at 100% of the death or permanent-injury limit, but benefit A is optional; without it, read literally, the cap is 0. With it, medical expenses count toward a cap set by the death limit: 150,000,000 of allowed medical expenses is cut to 100,000,000 (fixture).
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: CONTESTED (fork F17: no cap without benefit A).
- **Evidence**: `lpa-tests-findings.l4:238` (literal cap `EQUALS 0`), `:239` (encoded `NOTHING`); `lpa-tests.l4:979` (`claim H`: 150,000,000 → 100,000,000); src:311-314, 560-562.
- **Plain-English test of surprise**: A buyer who skips the death benefit expects the other benefits to pay; read literally, everything is capped at zero.

### VN-23 D14 — Any breach of any law, intentional or not, excludes
- **Class**: T2 exclusion with no causal link
- **Scenario**: 6(a) excludes any breach of law or regulation, including "vi phạm luật giao thông" (a traffic violation), with no link to the accident. A rider who breaks a traffic rule unrelated to how the accident happened is excluded.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: CONTESTED (fork F24: the encoding requires the breach to be a circumstance of the accident, and "the literal text does not even require that").
- **Evidence**: `lpa-tests.l4:883`-`:884` (`claim C` → `excluded by general exclusion 6(a)`); src:776-781.
- **Plain-English test of surprise**: A rider hit by another vehicle expects an unrelated minor offence not to matter; the exclusion has no causal test.

### VN-23 D15 — "Any race" swallows the carve-out for foot races
- **Class**: T7 internal inconsistency / T2 overbroad exclusion
- **Scenario**: Exclusion 4(l) excludes racing "khác hơn so với đi bộ" (other than on foot); 4(e) excludes "bất kỳ cuộc đua nào" (any race). A foot race is excluded by 4(e), so the carve-out does nothing.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `lpa-tests-findings.l4:243` (`EQUALS LIST general exclusion 4(e)`); src:727-728, 739-740.
- **Plain-English test of surprise**: A charity-run entrant who reads the foot-race carve-out expects cover; another limb takes it away.

### VN-23 D16 — Short-period refund bands share their edges
- **Class**: T7 internal inconsistency / T4 payout arithmetic
- **Scenario**: "Đến 3 tháng" (up to 3 months) and "Từ 3 tháng đến 6 tháng" (3 to 6 months) both include 3 months; likewise 6. Cover from 1 January to 1 April 2026 is charged at 40%; to 1 July 2026, 70%.
- **Who bears it**: policyholder. **Money direction**: unclear.
- **Standing**: CONTESTED (fork F38 takes the lower band, the larger refund).
- **Evidence**: `lpa-tests-findings.l4:249` (`EQUALS 40%`), `:250` (`EQUALS 70%`); src:1432-1434.
- **Plain-English test of surprise**: A policyholder cancelling at exactly 3 months expects one rate; two bands claim the same day.

### VN-23 D17 — Overlapping and missing measurement bands
- **Class**: T7 internal inconsistency / T5 term that decides outcomes
- **Scenario**: A 5 cm leg shortening is in two bands (30% and 20%); "khoảng" (about) gives no measure; a skull loss under 3 cm² and a shortening under 3 cm have no band (2.9 tested).
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: CONTESTED (fork F8: first band, higher rate, no tolerance).
- **Evidence**: `lpa-tests-findings.l4:254`-`:255` (30% and 20%); `lpa-tests.l4:400`, `:406` (2.9 → `NOTHING`); src:364-365, 445-447.
- **Plain-English test of surprise**: A claimant expects a measured injury to map to one rate; at 5 cm it maps to two, under 3 cm to none.

### VN-23 D18 — The application outranks the endorsements that amend the contract
- **Class**: T7 internal inconsistency
- **Scenario**: General provision 1 ranks the application or quotation above an endorsement, so an endorsement that changes a term cannot prevail over the document it changes.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL.
- **Evidence**: `lpa-tests-findings.l4:259` (the application prevails over an endorsement); src:1124-1130.
- **Plain-English test of surprise**: Parties expect a later amendment to override the original; the precedence clause says the reverse.

### VN-23 D19 — Words and figures for an amount differ
- **Class**: T5 term that decides outcomes / T13 other (words against figures)
- **Scenario**: "một triệu năm trăm (1.500.000)": the words, read literally, are one million five hundred (1,000,500), while two other passages say "một triệu năm trăm ngàn" (1,500,000).
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: CONTESTED. Whether everyday Vietnamese reads the first as 1,500,000 is "outside knowledge, unverified"; the figure is encoded. Reading only.
- **Evidence**: reading only; src:1220, 1226-1227, 1415-1416.
- **Plain-English test of surprise**: A reader expects the words and digits of an amount to agree; literally, they differ by 499,500.

### VN-23 D20 — Defined terms carry no weight; weighty terms are undefined
- **Class**: T5 undefined term
- **Scenario**: Six terms are defined and never used, including "Mất chi" (loss of a limb from wrist or ankle up), while the tables say loss of "an arm", "a hand", "both legs" with nothing tying them to it. "Tử vong", "Thai sản" and two group-policy terms are capitalised but undefined; "Ôm đau" misspells "Ốm đau".
- **Who bears it**: insured. **Money direction**: unclear.
- **Standing**: LITERAL (reading only).
- **Evidence**: reading only; src:153.
- **Plain-English test of surprise**: A claimant expects the table's "loss of a hand" to use the defined meaning of loss; nothing connects them.

### VN-23 D21 — Insurer discretion with no criteria
- **Class**: T11 insurer discretion
- **Scenario**: The Company decides, without criteria: the rate for an injury not in the tables, at its "toàn quyền đơn phương" (sole unilateral discretion); necessary hospital days; the remedy for non-disclosure; terms on a material change; refunds; excess or rateable share; exchange rates; dependants; and "Các tài liệu khác khi Công ty yêu cầu" (other documents on request), whose absence voids a claim under 13(d).
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `lpa-tests-findings.l4:204` (unlisted injury: REFUSED until the Company sets a rate); the rest reading only; src:464-465, 1513 (eight more in NOTES §4 D21).
- **Plain-English test of surprise**: A claimant expects stated rules for these decisions; each is the insurer's call.

### VN-23 D22 — Special provision 6 puts the employer's duty on the employee
- **Class**: T12 condition precedent on the wrong party
- **Scenario**: Special provision 6 applies on condition that "Người được bảo hiểm phải thông báo vào cuối mỗi tháng" (the insured must notify at each month's end). The list of employees is the policyholder's, and the insured cannot know it.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL (reading only).
- **Evidence**: reading only; src:625-627.
- **Plain-English test of surprise**: An employee expects the employer to keep the staff list current; the condition is put on the employee.

### VN-23 D23 — 7(h) ends cover "on" the period's last day
- **Class**: T1 clocks and deadlines / T7 internal inconsistency
- **Scenario**: 7(h) ends cover "on" the last day of the period, while the definitions run the period and the insurance year to the end of that day. Read like 7(a)-(g), which end cover from the start of the named day, the last day would be uncovered.
- **Who bears it**: insured. **Money direction**: against the claimant (on that reading).
- **Standing**: CONTESTED (fork F29 keeps the whole last day). Reading only.
- **Evidence**: reading only; src:1269, 1299, 1327, 88-92, 98-102.
- **Plain-English test of surprise**: A customer expects to be covered through the last day printed; one reading drops it.

### VN-23 D24 — Property and reinsurance clauses in an accident wording
- **Class**: T13 other (irrelevant boilerplate)
- **Scenario**: Special exclusions 4 and 6 (nuclear risks, defined as classes of property and liability insurance), 7 (data and software damage) and 8 (pollution of property, clean-up, fines) concern nothing this contract pays for.
- **Who bears it**: unclear. **Money direction**: no money.
- **Standing**: LITERAL.
- **Evidence**: `lpa-tests-findings.l4:263` (`#ASSERT REFUSED` on the nuclear-property exclusion); src:891-1103.
- **Plain-English test of surprise**: A reader expects every exclusion in an accident policy to bear on accidents; several concern property only.

### VN-23 D25 — Cancellation for non-disclosure without intent
- **Class**: T3 contract worse than the statute
- **Scenario**: 2(a) lets the Company cancel from the effective date for information the policyholder "phải biết hoặc được cho là biết" (must know or is deemed to know). The encoder notes Law art 22(2) requires intentionally incomplete or false information.
- **Who bears it**: policyholder / insured. **Money direction**: against the claimant.
- **Standing**: LAW (fork F33). Reading only.
- **Evidence**: reading only; src:1143-1153.
- **Plain-English test of surprise**: A policyholder expects an honest mistake not to void cover from the start; on the literal reading it can.

### VN-23 D26 — A subrogation clause where the Law forbids subrogation
- **Class**: T3 contract conflicts with the statute
- **Scenario**: The Company may recover from third parties after paying. The encoder notes Law art 16(4) and art 38 exclude subrogation from health insurance, which includes accident cover; the clause's "phù hợp với quy định của pháp luật" (in accordance with law) may save it by giving it nothing to do.
- **Who bears it**: insured. **Money direction**: unclear.
- **Standing**: LAW (fork F34; encoded as inert). Reading only.
- **Evidence**: reading only; src:1457-1463.
- **Plain-English test of surprise**: An accident victim expects to keep a claim against the wrongdoer; the clause purports to pass it to the insurer.

### VN-23 D27 — No time for the Company to pay
- **Class**: T3 contract worse than the statute / T1 clocks and deadlines
- **Scenario**: Only limitation 3 times the permanent-injury instalments; otherwise the wording sets no payment deadline. The encoder notes Law art 31 fills 15 days.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LAW (fork F40; not encoded). Reading only.
- **Evidence**: reading only (silence in the wording).
- **Plain-English test of surprise**: A claimant held to 30-day deadlines expects the insurer to have one; the wording sets none.

### VN-23 D28 — A 30-day period whose premium-payment period ends after it
- **Class**: T1 clocks and deadlines / T5 term that decides outcomes
- **Scenario**: The rule for periods "ít hơn 30 ngày" (under 30 days) does not reach a period of exactly 30 days, which gets 30 days from the effective date to pay; that ends the day after the period. Effective 1 January 2026, period ending 30 January: last payment day 31 January.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL (day counting per fork F35, Art 24).
- **Evidence**: `lpa-tests-findings.l4:269` (`EQUALS YMD 2026 1 31`); src:1542-1544.
- **Plain-English test of surprise**: A reader expects premium for a short cover to fall due within it; here it falls due after cover ends.

### VN-23 D31 — An extension that cuts cover: motorcycles over 150cc
- **Class**: T6 illusory cover / T5 term that decides outcomes
- **Scenario**: Special provision 8 extends cover to motorcycles on condition the machine is "không vượt quá 150cc" (not over 150cc). No exclusion names motorcycles, so a 175cc rider is either covered by the insuring clause or uncovered by an "extension".
- **Who bears it**: insured. **Money direction**: against the claimant (on the reading taken).
- **Standing**: CONTESTED (fork F19 reads the condition as biting; Art 24 favours reading it as an extension only, "recorded, not followed").
- **Evidence**: `lpa-tests-findings.l4:273` (`special provision 8 is not met by riding a motorcycle ... 175`); src:650-653.
- **Plain-English test of surprise**: A rider expects an extension to add cover; this one may remove cover the main clause already gave.

#### VN-23 row summary
- Findings in section 4: 29 (D1-D28 and D31).
- Most counterintuitive: D4 (a family that claimed the permanent-injury benefit receives 600,000,000 less on the same death than one that did not); D1 (read literally, a business group accident policy excludes any injury while performing work); D13 (without the optional death benefit, read literally, every benefit is capped at 0).
- Matches in this group: D4 ~ VN-04 X1 and VN-06 F-PA-ONCE (a death after a partial-disablement payment is paid less, or nothing); D5 ~ VN-03 X19 and VN-06 F-PA-NOTICE (a deadline closes before the disablement can exist), and D5(ii) and D12 ~ VN-03 X2 (late notice forfeits); D8 ~ VN-03 X12 (other insurance: several methods); D9 ~ VN-04 X13 (two windows for one benefit); D10, D11, D15 and D31 ~ VN-03 X4 and X8, and VN-06 F-LAPTOP (a benefit granted, then excluded); D14 ~ VN-03 X7 and VN-19 X7 (breach-of-law exclusion with no causal link); D21 ~ VN-04 X10, VN-19 X27 and VN-06 F-DISCRETION (discretion without criteria); D26 ~ VN-03 X14 (subrogation); D27 ~ VN-03 X18 (no time to pay); D6, D16 and D17 ~ VN-19 X1 and X21 (a boundary value in no band, or two); D7 ~ VN-03 X0 and VN-19 X2 (injuries the published tables do not price); D20 ~ VN-03 X27 and VN-06 F-UNDEF (undefined or unused terms).

## VN-06 Pacific Cross travel 2023 (English and Vietnamese texts)

Directory: `vn-pacific-cross-travel-2023/encodings/legalese-2026-10-vn-06`.
Section 4.1 lists 27 places where the English and Vietnamese differ (VN-F1 to VN-F27); section 4.2 lists 22 defects in both texts.
The encoder does not group the EN ≠ VI items, so each has its own record; those that change no answer get a one-line record.
For every EN ≠ VI record, both texts are encoded as written, and which text governs is the encoder's fork LAW-CONTRA, marked "Not resolved" (whether Law Art. 24 lets the buyer take the better text clause by clause).
Test-file short names: `en-vi.l4` is `pc-travel-tests-en-vi.l4`; `tests.l4` is `pc-travel-tests.l4`.
Money in this row is the encoder's test-case money (fixture) unless the plan table prints it.

### VN-06 VN-F1 — Non-paying passenger in a private plane: English excludes, Vietnamese covers
- **Class**: T9 English and Vietnamese disagree / T2 exclusion scope
- **Scenario**: The English excludes flying in any aircraft other than a licensed aircraft of a recognised airline as a fare-paying passenger. The Vietnamese excludes only a fare-paying passenger on an unlicensed aircraft of an unrecognised airline. Injured as a non-paying passenger in a licensed private plane: English 0, Vietnamese 18,000,000 of medical expenses (fixture).
- **Who bears it**: insured. **Money direction**: against the claimant (English) / against the insurer (Vietnamese).
- **Standing**: LITERAL, both texts; which governs is open (LAW-CONTRA).
- **Evidence**: `en-vi.l4:22`-`:23`, `:40` (English 0), `:41` (Vietnamese 18,000,000); src:93-96, 1183-1186.
- **Plain-English test of surprise**: A traveller expects the two language versions of one policy to give one answer; here they differ by the whole claim.

### VN-06 VN-F2 — Street riot: English covers, Vietnamese excludes
- **Class**: T9 English and Vietnamese disagree / T2 exclusion scope
- **Scenario**: The English excludes a riot "assuming the proportions of or amounting to a popular rising"; the Vietnamese excludes unrest caused by sections of the people, with no popular-rising test. Hurt in a street riot that is no popular rising: English 18,000,000, Vietnamese 0 (fixture).
- **Who bears it**: insured. **Money direction**: against the claimant (Vietnamese) / against the insurer (English).
- **Standing**: LITERAL, both texts (fork F-RIOT reads the English qualifier as governing all three perils); which governs is open (LAW-CONTRA).
- **Evidence**: `en-vi.l4:44`-`:45`, `:50` (`EQUALS 18_000_000`), `:51` (`EQUALS 0`); src:59-61, 1143-1145.
- **Plain-English test of surprise**: A tourist caught in a street disturbance expects one answer; the language chosen decides it.

### VN-06 VN-F3 — Climbing that "normally" needs ropes, or climbing with ropes
- **Class**: T9 English and Vietnamese disagree / T2 exclusion scope
- **Scenario**: The English excludes climbing "normally involving the use of ropes or other equipment"; the Vietnamese excludes climbing "có sử dụng dây thừng" (using ropes). An unroped climb of a route that normally needs ropes is excluded in English only; an easy scramble done roped is excluded in Vietnamese only.
- **Who bears it**: insured. **Money direction**: against the claimant (in each text, for a different climber).
- **Standing**: LITERAL, both texts; which governs is open (LAW-CONTRA).
- **Evidence**: `en-vi.l4:55`-`:58`; src:90-91, 1181-1182.
- **Plain-English test of surprise**: A climber expects one rule; the careful roped scrambler loses in one text, the unroped climber in the other.

### VN-06 VN-F4 — Extension limit: length of the trip, or time insured
- **Class**: T9 English and Vietnamese disagree / T10 term interplay
- **Scenario**: The English grants an extension if "the total length of the trip" stays within 180 days; the Vietnamese, if "tổng thời gian được bảo hiểm" (total time insured) does. A 200-day trip insured for 170 days: English refuses, Vietnamese grants. A 170-day trip insured for 190: the reverse.
- **Who bears it**: insured. **Money direction**: unclear.
- **Standing**: LITERAL, both texts; which governs is open (LAW-CONTRA).
- **Evidence**: `en-vi.l4:72`-`:73`, `:74`-`:75`; src:119, 1212-1213.
- **Plain-English test of surprise**: A traveller asking to extend expects one rule; the texts measure different things.

### VN-06 VN-F5 — Hospital cash per "complete day" or per day
- **Class**: T9 English and Vietnamese disagree / T4 payout arithmetic
- **Scenario**: The English pays VND 1,000,000 "for each complete day"; the Vietnamese "1.000.000 VND/ngày" (per day). A 36-hour inpatient stay over two calendar days: English 1,000,000, Vietnamese 2,000,000.
- **Who bears it**: insured. **Money direction**: against the claimant (English).
- **Standing**: LITERAL, both texts (forks F-5DAYS, F-VIDAY); which governs is open (LAW-CONTRA).
- **Evidence**: `en-vi.l4:81` (English `1_000_000`), `:82` (Vietnamese `2_000_000`); src:355, 360, 1451.
- **Plain-English test of surprise**: A patient expects a day and a half in hospital to pay the same in both texts; one pays double.

### VN-06 VN-F6 — An adoptive parent is family in English, not in Vietnamese
- **Class**: T9 English and Vietnamese disagree / T5 term that decides outcomes
- **Scenario**: The English "parents" sits beside adopted children; the Vietnamese says "cha mẹ ruột" (natural parents). An adoptive mother dies and the trip is cut short: 25,000,000 (English) or 0 (Vietnamese). The insured injures the adoptive mother: liability excluded (English) or 370,000,000 (Vietnamese). The adoptive mother's hospital visit: 35,000,000 or 0.
- **Who bears it**: insured / third party. **Money direction**: unclear (each text favours a different party per benefit).
- **Standing**: LITERAL, both texts; which governs is open (LAW-CONTRA).
- **Evidence**: `en-vi.l4:91`-`:92`, `:101`-`:102`, `:104`-`:105`, `:110`-`:111`; src:925-926, 2042-2043.
- **Plain-English test of surprise**: An adopted traveller expects an adoptive parent to count as a parent; one text says no.

### VN-06 VN-F7 — Return of children after an ordinary illness
- **Class**: T9 English and Vietnamese disagree
- **Scenario**: The English pays for children's return after the insured's "Serious Injury, Illness, or hospitalization, or death"; the Vietnamese needs "Ốm đau nặng" (serious illness). An ordinary illness leaves the children unattended: 40,000,000 (English) or 0 (Vietnamese).
- **Who bears it**: insured. **Money direction**: against the claimant (Vietnamese).
- **Standing**: LITERAL, both texts; which governs is open (LAW-CONTRA).
- **Evidence**: `en-vi.l4:118` (`EQUALS 40_000_000`), `:119` (`EQUALS 0`); src:396-398, 1494-1496.
- **Plain-English test of surprise**: A parent taken ill abroad expects the children's trip home to be covered either way; the Vietnamese demands a serious illness.

### VN-06 VN-F8 — "Damage to luggage", or damage to luggage containers
- **Class**: T9 English and Vietnamese disagree / T2 exclusion scope
- **Scenario**: The English excludes "Damage to luggage", read as bags and contents (fork F-LUGGAGE); the Vietnamese excludes "Hư hại đồ đựng hành lý" (damage to luggage containers). Clothes damaged in a bag the carrier mishandled: 0 (English) or 3,000,000 (Vietnamese).
- **Who bears it**: insured. **Money direction**: against the claimant (English).
- **Standing**: LITERAL, both texts; which governs is open (LAW-CONTRA).
- **Evidence**: `en-vi.l4:128` (`EQUALS 0`), `:129` (`EQUALS 3_000_000`); src:556, 1658.
- **Plain-English test of surprise**: A traveller whose clothes are ruined in transit expects one answer; the English excludes them, the Vietnamese only the suitcase.

### VN-06 VN-F9 — Referral services "may" or "will" be provided
- **Class**: T9 English and Vietnamese disagree / T11 insurer discretion
- **Scenario**: The English says referral services "may be provided"; the Vietnamese "sẽ cung cấp" (will provide). A requested referral that is never provided is a permission unused in English (FULFILLED) and a duty breached by the Company in Vietnamese.
- **Who bears it**: insured. **Money direction**: no money.
- **Standing**: LITERAL, both texts; which governs is open (LAW-CONTRA).
- **Evidence**: `en-vi.l4:134` (`#TRACE`, English), `:136`, `:138` (`#TRACE`, Vietnamese); src:413-415, 1509-1511.
- **Plain-English test of surprise**: A traveller expects promised assistance to be a promise; in English it is optional.

### VN-06 VN-F10 — Documents "satisfactory to the Company", or "appropriate"
- **Class**: T9 English and Vietnamese disagree / T11 insurer discretion
- **Scenario**: The English needs documentation "satisfactory to the Company"; the Vietnamese "Chứng từ thích hợp" (appropriate documents). Documents the Company says do not satisfy it, on a 72-hour stay: 0 (English) or 3,000,000 (Vietnamese). CP 1's "proof satisfactory to the Company" against "bằng chứng thỏa đáng" is the same difference (reading only).
- **Who bears it**: insured. **Money direction**: against the claimant (English).
- **Standing**: LITERAL, both texts; which governs is open (LAW-CONTRA).
- **Evidence**: `en-vi.l4:87` (`EQUALS 0`), `:88` (`3_000_000`); src:367, 1459, 1014, 2141.
- **Plain-English test of surprise**: A claimant expects documents to be judged by an objective standard; the English lets the insurer's satisfaction decide.

### VN-06 VN-F11 — Travel-document perils and the 24-hour report
- **Class**: T9 English and Vietnamese disagree / T12 forfeiture by notice
- **Scenario**: The English covers theft, robbery, burglary "and accidental loss", reported "within 24 hours or as soon as practicable"; the Vietnamese covers theft, robbery or accident, reported "trong vòng 24 giờ" (within 24 hours). A mislaid passport: 15,000,000 (English) or 0. A theft reported after 30 hours, as soon as practicable: 15,000,000 (English) or 0.
- **Who bears it**: insured. **Money direction**: against the claimant (Vietnamese).
- **Standing**: LITERAL, both texts; which governs is open (LAW-CONTRA).
- **Evidence**: `en-vi.l4:143`-`:144` (mislaid: `15_000_000`, `0`), `:146`-`:147` (30 hours: `15_000_000`, `0`); src:589-590, 600-601, 1690, 1700-1701.
- **Plain-English test of surprise**: A traveller who simply loses a passport expects the same cover in both texts; only the English has it.

### VN-06 VN-F12 — Customary charges where treated, or where paid
- **Class**: T9 English and Vietnamese disagree / T4 payout arithmetic
- **Scenario**: The English caps eligible expenses at customary charges "in the country in which they are incurred"; the Vietnamese, in the country where the insured pays. Treated abroad (customary 12,000,000), paid at home (customary 8,000,000): 12,000,000 (English) or 8,000,000 (Vietnamese).
- **Who bears it**: insured. **Money direction**: against the claimant (Vietnamese).
- **Standing**: LITERAL, both texts; which governs is open (LAW-CONTRA).
- **Evidence**: `en-vi.l4:155` (`EQUALS 12_000_000`), `:156` (`EQUALS 8_000_000`), `:157`-`:158`; src:905-907, 2022-2024.
- **Plain-English test of surprise**: A traveller expects foreign bills to be judged by foreign prices; the Vietnamese measures them by home prices.

### VN-06 VN-F13 — Liability exclusion: firearms, or any weapon
- **Class**: T9 English and Vietnamese disagree / T2 exclusion scope
- **Scenario**: Personal liability exclusion 9(ii)(h) reads "the use of firearms" in English and "sử dụng vũ khí" (the use of weapons) in Vietnamese. A liability arising from the use of a knife: 370,000,000 (English) or 0 (Vietnamese).
- **Who bears it**: insured / third party. **Money direction**: against the claimant (Vietnamese).
- **Standing**: LITERAL, both texts; which governs is open (LAW-CONTRA).
- **Evidence**: `en-vi.l4:166` (`EQUALS 370_000_000`), `:167` (`EQUALS 0`); src:763, 1881.
- **Plain-English test of surprise**: A reader expects "firearms" and its translation to cover the same objects; the Vietnamese covers any weapon.

### VN-06 VN-F14 — English notice duty points the wrong way
- **One line** (no change to an answer): T9; the English AT 1 says the Policyholder "shall be given written notice to the Company", which as written imposes no duty, where the Vietnamese requires the Policyholder to notify; encoded on the Vietnamese (fork F-AT1); reading only; src:204-205, 1301-1302.

### VN-06 VN-F15 — Arbitration award: condition of any right of action, or of payment
- **Class**: T9 English and Vietnamese disagree / T12 condition precedent
- **Scenario**: The English makes an award a condition precedent "to any liability or right of action against the Company"; the Vietnamese makes it a condition of the Company's liability to pay and says nothing of a right of action. A suit before any award is barred in English; the Vietnamese is silent.
- **Who bears it**: insured. **Money direction**: unclear.
- **Standing**: LITERAL, both texts; the Vietnamese reading is refused by name (fork F-C17VI).
- **Evidence**: `en-vi.l4:182` (English: NOT), `:183` (Vietnamese: `#ASSERT REFUSED`); src:184-186, 1281-1282.
- **Plain-English test of surprise**: A claimant expects to know whether court is open before arbitration; one text bars it, the other does not say.

### VN-06 VN-F16 — Who may name the death beneficiary
- **Class**: T9 English and Vietnamese disagree
- **Scenario**: The English accepts a beneficiary "advised to the Company in writing"; the Vietnamese requires the Insured Person to designate the beneficiary in writing. A Policyholder who is not the insured names a beneficiary: possibly valid in English only (inferred).
- **Who bears it**: beneficiary. **Money direction**: unclear.
- **Standing**: LITERAL; "possibly" changes an answer; reading only (the encoding takes the designation as given).
- **Evidence**: reading only; src:463-464, 1560-1561.
- **Plain-English test of surprise**: An employer buying cover for staff expects its nomination to stand; the Vietnamese gives that power to the insured alone.

### VN-06 VN-F17 — Home visit: cover "ceases", or is suspended
- **Class**: T9 English and Vietnamese disagree / T6 illusory cover
- **Scenario**: English section 10.5 says "Coverage ceases on return"; the Vietnamese says cover "sẽ tạm ngưng" (is suspended). After a 7-day visit home and a return abroad, cover does not resume in English and does in Vietnamese. A planned (not unexpected) visit is allowed in English only.
- **Who bears it**: insured. **Money direction**: against the claimant (English, after resuming).
- **Standing**: LITERAL, both texts; which governs is open (LAW-CONTRA).
- **Evidence**: `en-vi.l4:193` (English: NOT resumed), `:194` (Vietnamese: resumed), `:196`-`:197` (planned visit); src:775-777, 790, 1891-1894, 1904.
- **Plain-English test of surprise**: A traveller using the home-visit benefit expects cover back on returning abroad; the English ends it.

### VN-06 VN-F18 — A "recognized" licensed rental company, or just licensed
- **Class**: T9 English and Vietnamese disagree / T5 undefined term
- **Scenario**: The English requires "a recognized licensed car rental company"; the Vietnamese only a licensed one. Renting from a licensed company that no one has "recognized": rental excess 0 or 8,000,000; rental-car protection 0 or 45,000,000 (English, Vietnamese).
- **Who bears it**: insured. **Money direction**: against the claimant (English).
- **Standing**: LITERAL, both texts; which governs is open (LAW-CONTRA).
- **Evidence**: `en-vi.l4:202` (`EQUALS 0`), `:203` (`8_000_000`), `:204` (`0`), `:205` (`45_000_000`); src:805, 834-835, 1920-1921, 1958-1959.
- **Plain-English test of surprise**: A renter using a licensed company expects cover; the English adds an undefined test of recognition.

### VN-06 VN-F19 — Delay benefit per "full" 6 hours, or per 6 hours
- **Class**: T9 English and Vietnamese disagree / T4 payout arithmetic
- **Scenario**: The English pays "for each full 6 hours delay"; the Vietnamese omits "full". A 13-hour delay: both count two periods on the natural reading; a buyer-favourable reading of the Vietnamese counts three.
- **Who bears it**: insured. **Money direction**: unclear.
- **Standing**: CONTESTED (reading only; the third period exists only under LAW-CONTRA).
- **Evidence**: reading only; src:645-646, 1749.
- **Plain-English test of surprise**: A delayed passenger expects the hours to be counted one way; the Vietnamese leaves room for one more period.

### VN-06 VN-F20 — English misprint in the delay benefit, settled by the Vietnamese
- **One line** (no change to an answer): T9; the English prints "VND f10,000,000 or Plan B and Executive Plan" (src 651), a misprint; the Vietnamese (src 1754-1755) gives 10,000,000 for Plan B and economy; both parse to the same figure in `pc-travel-tests-tables.l4`.

### VN-06 VN-F21 — Title says "global" in Vietnamese only
- **One line** (no change to an answer): T9; the English title is "TRAVEL INSURANCE POLICY" (src 1), the Vietnamese "QUY TẮC BẢO HIỂM DU LỊCH TOÀN CẦU" (global, src 1079-1080); territory is set by the Country of Origin definition in both; reading only.

### VN-06 VN-F22 — Trekking above 5,000 m, or exploring nature above 5,000 m
- **Class**: T9 English and Vietnamese disagree / T2 exclusion scope
- **Scenario**: The English excludes "Trekking at an altitude limit greater than 5,000 meters"; the Vietnamese excludes "Ði tìm hiểu thiên nhiên" (going out to explore nature) above 5,000 m. A visitor driven to a 5,200 m viewpoint is not trekking but arguably exploring nature.
- **Who bears it**: insured. **Money direction**: against the claimant (Vietnamese, possibly).
- **Standing**: CONTESTED ("possibly"; reading only).
- **Evidence**: reading only; src:102, 1194.
- **Plain-English test of surprise**: A tourist on a sightseeing drive expects no adventure-sport exclusion; the Vietnamese may catch it.

### VN-06 VN-F23 — Business travel: limited in English, "abroad" in Vietnamese
- **One line** (no change to an answer): T9; the English limits business travel to administrative, non-manual work (src 106-107), the Vietnamese says business travel abroad (src 1200-1201); no change on this wording, since cover is outside the Country of Origin anyway; reading only.

### VN-06 VN-F24 — Third party who "may be" liable, or who is liable
- **Class**: T9 English and Vietnamese disagree / T2 exclusion scope
- **Scenario**: 1A.2(d) excludes expenses "for which a third party may be liable" in English; the Vietnamese, those a third party is liable to pay. Where a third party is possibly, not certainly, liable, the English exclusion may bite and the Vietnamese may not.
- **Who bears it**: insured. **Money direction**: against the claimant (English, possibly).
- **Standing**: CONTESTED ("possibly"; reading only).
- **Evidence**: reading only; src:291-292, 1390.
- **Plain-English test of surprise**: An injured traveller expects the insurer to pay first and chase the other party; the English lets a mere possibility of liability exclude.

### VN-06 VN-F25 — Police copy "certified", or "notarised"
- **Class**: T9 English and Vietnamese disagree / T12 condition precedent
- **Scenario**: The claims procedure asks for a "certified written copy" of police reports in English and "bản sao có công chứng" (a notarised copy) in Vietnamese. A copy certified by the police station but not notarised meets the English and possibly not the Vietnamese.
- **Who bears it**: insured. **Money direction**: against the claimant (Vietnamese, possibly).
- **Standing**: CONTESTED ("possibly"; reading only; documents are not tested for form).
- **Evidence**: reading only; src:1045, 1066, 1071, 2173, 2196, 2201.
- **Plain-English test of surprise**: A theft victim abroad expects a police-certified copy to suffice; the Vietnamese asks for notarisation.

### VN-06 VN-F26 — Claim-form and report names differ
- **One line** (no change to an answer): T9; the English asks for "a completed Travel Insurance Claims Form" and "the relevant coroner's report" (src 1018-1019, 1026), the Vietnamese for a loss notification form and an investigator's report (src 2144-2145, 2150); reading only.

### VN-06 VN-F27 — Four smaller wording differences
- **One line** (no change to an answer stated): T9; "executive officer" against an authorised employee (src 960-961, 2087-2088); the Vietnamese adds "with the necessary medical equipment" to the most economical conveyance (src 339, 1435); the plan-dependence parenthesis differs (src 796, 825, 1910, 1948); arbitrators at the Company's discretion against arbitrators the Company appoints (src 181-182, 1278-1279); reading only, each.

### VN-06 F-HEART — Heart attack first striking on the trip is excluded
- **Class**: T2 overbroad exclusion / T6 illusory cover
- **Scenario**: Clause 5.2 excludes 22 named Disabilities "whether occurring prior to or during the Period of Insurance". A heart attack, stroke, cancer, kidney stone, ulcer or diabetes that first strikes during the trip is excluded from every section, emergency evacuation included. A traveller with no history has a heart attack on day 5: medical expenses 0.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `tests.l4:300` (`EQUALS 0` for a Disability arising from hypertension or cardiovascular disease); src:40-54, 1123-1137.
- **Plain-English test of surprise**: A traveller buys medical cover for exactly a sudden heart attack abroad; the commonest travel emergencies are excluded.

### VN-06 F-MED-BREAKDOWN — The no-breakdown daily cap can never be reached
- **Class**: T6 illusory cover / T7 internal inconsistency
- **Scenario**: 1A.1(a) caps at 20,000,000 a day the charges "if no detailed breakdown of charges is provided", but a proviso requires every expense to be supported by a detailed breakdown. An unitemised all-in hospital day of 15,000,000 pays 0, not up to 20,000,000.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `tests.l4:263` (`EQUALS 0`); src:266-270, 277-279, 1367-1370, 1377-1378.
- **Plain-English test of surprise**: A patient whose hospital bills a flat daily rate expects the cap for unitemised bills to apply; it can never apply.

### VN-06 F-MED-CLOSED — Exceptions restore items the cover never included
- **Class**: T6 illusory cover / T7 internal inconsistency
- **Scenario**: 1A.1 covers "only the following expenses", which do not name eyeglasses, hearing aids or check-ups; 1A.2(c) and (h) then except such items from the exclusions after an accident or when incidental to a covered Disability. Eyeglasses needed after an accident abroad (4,000,000, fixture): 0.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL (fork F-CHECKUP (i)).
- **Evidence**: `tests.l4:272` (`EQUALS 0`); src:256-270, 287-290, 303-306.
- **Plain-English test of surprise**: A reader seeing eyeglasses carved out of an exclusion expects them to be paid; the cover never granted them.

### VN-06 F-LAPTOP — A laptop limit is printed, and laptops are excluded
- **Class**: T6 granted then taken back / T7 internal inconsistency
- **Scenario**: 3.3 prints a laptop limit (20,000,000 Premier, 10,000,000 other plans); 3.6(c) excludes "computer equipment" and portable electronic devices, and 3.4 makes the indemnity "Subject to paragraph (6)". A Premier traveller's stolen laptop pays 0.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: CONTESTED. The encoding takes the literal reading (fork F-LAPTOP (i)); "Reading (ii) is what Art. 24 would likely favour".
- **Evidence**: `tests.l4:455` (limit `EQUALS 20_000_000`), `:456` (`EQUALS 0`); src:507-509, 511, 529-533, 1606-1608, 1611, 1630-1635.
- **Plain-English test of surprise**: A buyer shown a laptop limit expects a stolen laptop to be paid up to it; the limit is dead text.

### VN-06 F-S8-ANNUAL — Annual Travel cancellation cover excludes every cause
- **Class**: T6 illusory cover / T1 clocks and deadlines
- **Scenario**: Annual Travel cancellation cover runs from 14 days before scheduled commencement (AT 5); proviso 4 excludes a cause arising "within 14 days prior to the scheduled departure date". Cover 18 March to 1 April: an illness on 25 March is excluded, one on 10 March predates cover. Both pay 0; a single-trip policy pays 30,000,000.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: CONTESTED (holds under fork F-S8WIN (i), dating the cause; not under (ii), dating the cancellation).
- **Evidence**: `tests.l4:583`-`:584` (0), `:586` (single trip 30,000,000); src:240-242, 712-717, 1342-1344, 1825-1832.
- **Plain-English test of surprise**: An annual-policy buyer expects the same cancellation cover as a single-trip buyer; every cause falls outside it.

### VN-06 F-S8-CANCEL — Disaster or home destruction can never found a cancellation
- **Class**: T6 illusory cover
- **Scenario**: Causes 4 (natural disaster) and 5 (destruction of the residence) are tied by provisos 5 and 6 to events "after commencement of travel", but a cancellation happens before travel, and cancellation cover ends on the departure date. A typhoon hitting the destination a week before departure: 0; the same typhoon after commencement founds a curtailment of 25,000,000.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `tests.l4:577` (`EQUALS 0`), `:578` (`EQUALS 25_000_000`); src:697-700, 718-726, 1805-1808, 1833-1843.
- **Plain-English test of surprise**: A traveller who cancels because a typhoon struck the destination expects the named cause to pay; it never can.

### VN-06 F-CBP — A business partner's "serious illness" has no meaning
- **Class**: T5 undefined term that decides outcomes
- **Scenario**: Cancellation cause 2 needs "Serious Injury or Illness" of a Close Business Partner, but the definition gives the term a meaning only for the Insured Person and Immediate Family Members. A gravely ill business partner: no answer.
- **Who bears it**: insured. **Money direction**: unclear.
- **Standing**: LITERAL.
- **Evidence**: `tests.l4:574` (`#ASSERT REFUSED`); src:691-694, 977-984, 1798-1802, 2105-2113.
- **Plain-English test of surprise**: A business traveller expects a partner's grave illness to be a valid cause, as listed; the test it must meet is undefined.

### VN-06 F-PA-NOTICE — Notice deadline closes before a covered death or disablement
- **Class**: T1 a bar that runs before the right arises / T12 forfeiture by notice
- **Scenario**: CP 1 wants notice "within 30 days of the expiry of this Policy"; section 2 pays a death within 12 months of the accident, and Permanent Total Disablement needs 52 weeks. A 20-day trip, accident 5 April, death 5 October: the death pays 1,000,000,000, but notice closed on 20 May, 138 days earlier, and before a covered 14 July follow-up.
- **Who bears it**: beneficiary / insured. **Money direction**: against the claimant.
- **Standing**: LITERAL; LAW-NOTICE and LAW-CLAIM "Not resolved".
- **Evidence**: `tests.l4:712`-`:714` (death paid; deadline 138 days earlier), `:717`, `:720`-`:721`; src:271-275, 427-430, 947-951, 1003-1005.
- **Plain-English test of surprise**: A family expects a covered death to be claimable; the notice window shut before the death.

### VN-06 F-PA-ONCE — A partial disablement payment bars a later death benefit
- **Class**: T4 payout arithmetic / T6 illusory cover
- **Scenario**: 2.2 says once any benefit becomes payable "no further liability shall be attached"; 2.5 caps all events at 100% of the sum insured. After a 50% benefit for loss of use of one limb, a later death pays 0, so the 100% cap never binds.
- **Who bears it**: beneficiary. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `tests.l4:416` (`EQUALS 0` when a benefit has already become payable); src:431-435, 456-459, 1529-1532, 1552-1556.
- **Plain-English test of surprise**: A family expects a death to be topped up to the sum insured after a 50% payment, as the 100% cap implies; it pays nothing.

### VN-06 F-PL-FORUM — Liability cover only for home-country judgments
- **Class**: T6 illusory cover / T2 overbroad exclusion
- **Scenario**: Personal liability covers events abroad but not judgments first given outside a court "WITHIN THE COUNTRY OF ORIGIN", while an injured third party ordinarily sues where the accident happened. A tourist sued in Bangkok for injuring a pedestrian there: 0; with no judgment, 370,000,000 (fixture).
- **Who bears it**: insured / third party. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `tests.l4:600` (another court `EQUALS 0`), `:596` (no judgment `EQUALS 370_000_000`); src:766-770, 1884-1886.
- **Plain-English test of surprise**: A traveller buys liability cover for accidents abroad; it fails when sued abroad.

### VN-06 F-C14 — Read literally, the 180-day cap forbids annual policies
- **Class**: T7 internal inconsistency / T6 illusory cover
- **Scenario**: Clause 14 caps "this Policy" at 180 days, which no annual policy can meet, while AT 3 and the short-period table presuppose policies in force more than eight months. An Annual Travel certificate for 2026 fails clause 14 read literally.
- **Who bears it**: insured. **Money direction**: unclear.
- **Standing**: CONTESTED (fork F-C14 takes reading (ii): AT 6's 90 days per trip governs Annual Travel).
- **Evidence**: `tests.l4:152` (`clause 14, read literally`: NOT within the maximum), `:150` (encoded: within); src:158-159, 211-223, 985-994.
- **Plain-English test of surprise**: A buyer of an annual policy expects it to last a year; one clause, read literally, caps every policy at 180 days.

### VN-06 F-S10-EN — The English home-visit section ends the cover it protects
- **Class**: T6 illusory cover / T9 English and Vietnamese disagree
- **Scenario**: Read literally, English section 10 ("Coverage ceases on return") ends the cover it exists to preserve across a home visit, so it confers nothing; the Vietnamese suspends cover instead. After a 7-day visit home, English cover does not resume.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL ("read literally").
- **Evidence**: `en-vi.l4:193` (English: NOT resumed), `:194` (Vietnamese: resumed); src:775-792, 1891-1906.
- **Plain-English test of surprise**: A traveller using a benefit called "incidental home country" visits expects to stay covered afterwards; the English benefit ends cover.

### VN-06 F-24H — Two 24-hour clocks: from awareness, or from the event
- **Class**: T1 two clocks for one act / T7 internal inconsistency
- **Scenario**: Section 5.1 counts 24 hours from when the insured "is aware of the loss"; CP 2(c) wants reports "within 24 hours of the occurrence". A passport stolen 6 April, missed until 8 April and reported 10 hours after discovery: section 5 pays 15,000,000; CP 2(c) fails at 58 hours.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `tests.l4:726` (`EQUALS 15_000_000`), `:727` (`NOT ... within 24 hours` at 58); src:600-604, 1046-1047, 1700-1703, 2174-2175.
- **Plain-English test of surprise**: A theft victim who reports promptly on discovery expects to have complied; another clause says it was too late.

### VN-06 F-UNDEF — Weight-bearing terms are never defined
- **Class**: T5 undefined term
- **Scenario**: "Excluded Conditions", "Pre-existing Illness or Injury" (not the defined Pre-Existing Condition), "Insurance Certificate", three spellings of the benefit schedule, "Application", "Policyholder", the product and plan names, "registered medical practitioner", "recognized" (airline, rental company) and "the Insured" are used and never defined.
- **Who bears it**: insured. **Money direction**: unclear.
- **Standing**: LITERAL (reading only); fork LAW-UNDEF notes Law Art. 87(2)(b) requires terms of art to be defined, "Not resolved".
- **Evidence**: reading only; src:38, 229-231, 374-375, 893-894, 960, 1019.
- **Plain-English test of surprise**: A reader expects the terms that decide claims to be defined; a dozen are not.

### VN-06 F-UNUSED — Defined terms that no clause uses
- **Class**: T13 other (dead definitions)
- **Scenario**: Cash, Emergency, and Medicines and Drugs are defined and used by no operative clause; Personal Effects appears only in a heading; Specialist only inside another definition.
- **Who bears it**: unclear. **Money direction**: no money.
- **Standing**: LITERAL (reading only).
- **Evidence**: reading only; src:879, 908-910, 938-940, 952-954.
- **Plain-English test of surprise**: A reader expects each definition to matter somewhere; several matter nowhere.

### VN-06 F-DISCRETION — Insurer discretion with no criteria
- **Class**: T11 insurer discretion
- **Scenario**: The Company decides without criteria: depreciation, wholly at its discretion; payment or replacement, at its option; whether documents and proof satisfy it; whether to deny a claim or refuse protection; renewal; repatriation, decided jointly with it; the arbitrators; and prior approval for emergency evacuation, which an unconscious traveller cannot seek.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL (reading only; where encoded, the rule says when the power is open, e.g. `clause 16 — the Company may deny the claim`).
- **Evidence**: reading only; src:168-169, 181-182, 224-225, 348-350, 367-368, 417-420, 511-515, 538-542, 842-844, 1014.
- **Plain-English test of surprise**: An unconscious traveller cannot ask permission to be evacuated; the policy requires it.

### VN-06 F-PL-UNLAWFUL — An "unlawful act" exclusion can swallow liability cover
- **Class**: T2 overbroad exclusion / T6 illusory cover
- **Scenario**: 9(ii)(c) excludes liability from "any willful, malicious, unlawful or deliberate act". Liability to a third party ordinarily arises from a wrongful act, so read widely, a careless act injuring a passer-by is excluded.
- **Who bears it**: insured / third party. **Money direction**: against the claimant.
- **Standing**: CONTESTED ("read widely"; reading only, the encoding takes the classification as an input).
- **Evidence**: reading only; src:751, 1869-1870.
- **Plain-English test of surprise**: A buyer of liability cover expects it to pay for careless harm; read widely, carelessness is "unlawful" and excluded.

### VN-06 F-ALCOHOL — Any alcohol use excludes, with no threshold
- **Class**: T2 exclusion without a threshold
- **Scenario**: 5.5 excludes losses "arising from ... the use of alcohol" with no threshold of intoxication, so a fall after one glass of wine is arguably excluded.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL (reading only; causation is an input).
- **Evidence**: reading only; src:80, 1167-1168.
- **Plain-English test of surprise**: A traveller expects one glass of wine at dinner not to void accident cover; the clause sets no limit.

### VN-06 F-BAGDELAY — Baggage-delay cover may end as it begins
- **Class**: T6 illusory cover / T5 ambiguous term
- **Scenario**: 4.6 gives no cover after the insured "reaches the final destination". If that means the destination abroad (fork F-FINAL reading (ii)), cover for a bag delayed on arrival at a single-destination holiday ends at the moment the 6-hour wait begins.
- **Who bears it**: insured. **Money direction**: against the claimant (on the insurer's reading).
- **Standing**: CONTESTED. The encoding takes reading (i), the end of a journey that does not return home; "The insurer has the ambiguity to argue".
- **Evidence**: reading only; src:562-565, 582-583.
- **Plain-English test of surprise**: A traveller whose bag misses the flight expects baggage-delay cover; one reading ends cover on landing.

### VN-06 F-CANCEL-REFUND — Single-trip premium is never refunded
- **Class**: T13 other (no refund at all) / T3 possible conflict with the statute
- **Scenario**: A single-trip policy is "non-cancelable", and "no refund of premium will be made once this Policy has been issued", even for a trip cancelled for a reason section 8 covers.
- **Who bears it**: policyholder. **Money direction**: against the claimant (the policyholder).
- **Standing**: LITERAL; forks LAW-FRAUD and LAW-TERM are noted, "Not resolved".
- **Evidence**: `tests.l4:102` (refund `EQUALS 0`); src:111-114, 1203-1207.
- **Plain-English test of surprise**: A traveller whose trip is cancelled for a covered reason expects some premium back; none is returned.

### VN-06 F-7-ORIGIN — An outbound delay at the home airport is never covered
- **Class**: T13 other (cover gap) / T6 illusory cover
- **Scenario**: Travel Delay covers only a delay "outside the Insured's Country of Origin", so an outbound flight delayed at the home airport, before clause 13's cover begins, is never covered.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL (reading only).
- **Evidence**: reading only; src:637-639, 1741-1743.
- **Plain-English test of surprise**: A traveller stuck at the departure airport expects the delay benefit to apply; it only works abroad.

### VN-06 F-COMPANY — The publisher is not the insurer the wording names
- **Class**: T13 other (identity of the insurer)
- **Scenario**: The insurer is Hung Vuong Insurance Corporation; Pacific Cross Vietnam, which publishes the document, is not a party the wording names.
- **Who bears it**: unclear. **Money direction**: no money.
- **Standing**: LITERAL (reading only).
- **Evidence**: reading only; src:884, 2210-2217.
- **Plain-English test of surprise**: A buyer expects the brand on the document to be the insurer; it is not named as a party.

#### VN-06 row summary
- Findings in section 4: 49 (27 EN ≠ VI items VN-F1 to VN-F27, of which 6 change no answer and have one-line records; 22 defects in both texts).
- Most counterintuitive: F-HEART (a heart attack first striking on the trip is excluded from every section, evacuation included); F-PA-NOTICE (a covered death 6 months after the accident pays 1,000,000,000, but the notice deadline closed 138 days before it); F-PL-FORUM (liability cover for accidents abroad pays 0 when the traveller is sued abroad).
- Matches in this group: F-PA-NOTICE ~ VN-03 X19 and VN-23 D5 (a deadline closes before the covered loss can exist); F-PA-ONCE ~ VN-04 X1 and VN-23 D4 (a death after a partial payment is paid less, or nothing); VN-F3 ~ VN-19 X6 (climbing defined by ropes or gear); F-LAPTOP and F-MED-CLOSED ~ VN-03 X4 and X8, VN-23 D31 (a benefit granted, then excluded or never granted); F-24H ~ VN-04 X13 and VN-19 X18 (two clocks for one act); F-HEART ~ VN-04 X22 (a broad exclusion applied to every benefit); F-DISCRETION ~ VN-04 X10 and VN-23 D21; F-UNDEF ~ VN-03 X27 and VN-23 D20; F-PL-UNLAWFUL ~ VN-03 X7 and VN-23 D14 (a law-breach exclusion that can reach everything); F-CANCEL-REFUND ~ VN-19 X4 (premium refund lost); VN-F5 ~ VN-03 X6 and VN-19 X8 (how a hospital day is counted).

