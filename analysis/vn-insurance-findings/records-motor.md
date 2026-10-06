# Policy defect records: motor rows (VN-01, VN-02, VN-15, VN-17, VN-18, VN-10)

Extracted read-only from each row's `NOTES.md` Findings section and its findings or tests module.
Line numbers in "Evidence" are lines of the named `.l4` file; `src:N` are the encoder's citations into the source text.
Paths are relative to each row's encoding directory under `commonswt/vn-insurance/subjects/`.

---

## VN-01 Bảo Việt motor physical damage 2021

Encoding: `contracts/insurance/vn-baoviet-motor-physical-damage-2021/encodings/legalese-2026-10-vn-01`.
Findings: `NOTES.md` §4 (X1-X24). Findings module: `bvvcx-tests-findings.l4`.

### VN-01 X1 — Driver exclusions miss a thief, because "driver" requires consent
- **Class**: T5 / T7
- **Scenario**: An unlicensed driver at 80 mg alcohol per 100 ml crashes. With the owner's consent, 11.3 and 11.4 exclude the loss; a thief is not def 8's "driver", so the 16,000,000 loss is paid in full.
- **Who bears it**: insurer. **Money direction**: against the insurer.
- **Standing**: CONTESTED (rests on F1 and F5; an insurer's lawyer "would read 'Người điều khiển xe' loosely").
- **Evidence**: `bvvcx-tests-findings.l4:31` (consent: `excluded by (LIST 11.3, 11.4)`), `:32` (no consent: `EQUALS 16_000_000`). src:71-72, 442-466, 636-637.
- **Plain-English test of surprise**: One expects a drunk joyrider to fare no better than a drunk friend; the joyrider's crash is paid, the friend's is not.

### VN-01 X2 — Exclusions apply without any causal link to loss
- **Class**: T2
- **Scenario**: Hail damages a parked car whose inspection certificate lapsed last week. The lapse has nothing to do with the hail, yet 11.2 excludes the whole loss and nothing is paid; the same holds for a lapsed licence on a driver rear-ended at a red light (11.3).
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `bvvcx-tests-findings.l4:44` (`excluded by (LIST 11.2 …)`), `:45` (`EQUALS 0`). src:441, 449-451.
- **Plain-English test of surprise**: A customer expects a paperwork lapse to matter only if it caused the accident; the wording voids hail cover for an expired inspection sticker.

### VN-01 X3 — Theft reported within 24 hours still loses 10%
- **Class**: T1 / T12
- **Scenario**: The car is stolen; the owner tells police and insurer 20 hours later. 5.2.10's 24-hour duty is met (trace FULFILLED), but 15.1.1(a)'s six-hour rule cuts the payout from 580,000,000 to 522,000,000. Both clocks run from the event, not its discovery.
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: CONTESTED (rests on F36; under LAW Article 24 the other reading "is arguable; it would remove finding X3").
- **Evidence**: `bvvcx-tests-findings.l4:60-61` (`#TRACE` 5.2.10 at hour 20), `:62` (`EQUALS 522_000_000`). src:301-304, 599-602, 720-722.
- **Plain-English test of surprise**: A customer meeting the policy's 24-hour theft deadline expects no penalty; a six-hour clock takes 10%.

### VN-01 X4 — Double insurance and under-insurance cut the same loss twice
- **Class**: T4 / T3
- **Scenario**: A car worth 600,000,000 is insured for 300,000,000 with each of two insurers. Each pro-rates by 0.5 for under-insurance, then pays half as its Article 8 share: a 16,500,000 loss yields 3,875,000 from each, 7,750,000 in all. Under the Law's Article 49(1), insuring exactly the value is not double insurance.
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: LAW (Article 49(1), aid 965-968; fork F19 encodes the Rules as written).
- **Evidence**: `bvvcx-tests-findings.l4:76` (`EQUALS 3_875_000`). src:389-400, 526-528.
- **Plain-English test of surprise**: A customer whose two policies together exactly cover the car's value expects the full loss less deductibles; the wording pays under half of it.

### VN-01 X5 — Claim-file rule and exclusion disagree on inspection certificates
- **Class**: T7
- **Scenario**: A vehicle circulating temporarily with written approval is damaged without an inspection certificate. 7.1.2(d) says the claim file need not include one; 11.2 (which excuses only a new vehicle within 30 days) excludes the loss for want of one.
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `bvvcx-tests-findings.l4:102` (certificate not required in the file), `:103` (`excluded by (LIST 11.2 …)`). src:345-348, 449-451.
- **Plain-English test of surprise**: A customer told no certificate is needed for the claim expects the claim to proceed; the exclusion refuses it for the missing certificate.

### VN-01 X6 — "Complete and valid file" starts insurer's clocks, undefined
- **Class**: T5 / T11
- **Scenario**: The 15-day payment and 15-day refusal clocks run from receipt of a "complete and valid" file, but Article 7 lists "one or more" documents and ends with "other relevant documents, if any". The insurer decides when its own clock starts.
- **Who bears it**: policyholder. **Money direction**: against the claimant (timing).
- **Standing**: LITERAL ("Reading only"; fork F49 leaves it undecided).
- **Evidence**: No assertion; the encoding takes the file-complete date as an input (`The claim file`). src:202-215, 332-333, 378.
- **Plain-English test of surprise**: A customer expects a definite payment deadline; the wording lets the insurer postpone it by deeming the file incomplete.

### VN-01 X7 — No payment deadline after 90 days without police conclusion
- **Class**: T1 / T11
- **Scenario**: If the authorities have not concluded within 90 days, the insurer must "proceed to consider" the claim, but 4.2.3 sets no time by which to pay.
- **Who bears it**: policyholder. **Money direction**: against the claimant (timing).
- **Standing**: LITERAL.
- **Evidence**: `bvvcx-tests-contract.l4:187` (`#ASSERT REFUSED` … "4.2.3 sets no time for paying a claim the competent authority has not concluded on"). src:206-212.
- **Plain-English test of surprise**: A customer expects every claim to have a payment deadline; this route has none.

### VN-01 X8 — One risk-change notice, two "5-day" clocks, different units
- **Class**: T1 / T7
- **Scenario**: A notice received Thursday 8 October 2026: the answer on a premium reduction is due 13 October (5 calendar days, 5.2.4(a)) but the re-rating is due 15 October (5 working days, 4.2.7). The insurer may have to answer on the premium before it has re-rated the risk.
- **Who bears it**: insurer. **Money direction**: no money.
- **Standing**: LITERAL (calendar vs working days per forks F6, F15).
- **Evidence**: `bvvcx-tests-findings.l4:109` (`EQUALS YMD 2026 10 13`), `:110` (`EQUALS YMD 2026 10 15`). src:223-224, 254-257.
- **Plain-English test of surprise**: One would expect the decision on the premium to follow the risk assessment; the wording makes it due first.

### VN-01 X9 — Premium charged for a period with no cover
- **Class**: T7
- **Scenario**: With no written agreement on payment time and nothing paid, 2.2 says the contract has no effect, yet 3.1.2 asks premium from the start of cover to the end: ended 2 January unpaid, 10,000. 3.1 also mis-points at 2.3.
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `bvvcx-tests-contract.l4:106` (standing on 1 January `not in effect, the premium not having been paid (2.2)`), `:165` (`3.1.2 — the premium the insurer asks for …` `EQUALS 10_000`). src:120-125, 132-148.
- **Plain-English test of surprise**: A customer expects not to pay for days when the policy had no effect; the wording bills them.

### VN-01 X10 — "Purchaser" defined by full payment contradicts deferred payment
- **Class**: T7 / T5
- **Scenario**: A person who agreed in writing to pay by 31 January holds a contract in effect on 20 January but is not "the purchaser" of def 2, which requires full payment. Every duty and right given to "the purchaser" is, on a literal reading, unowned until payment.
- **Who bears it**: policyholder. **Money direction**: unclear.
- **Standing**: LITERAL.
- **Evidence**: `bvvcx-tests-findings.l4:124` (standing `EQUALS in effect`), `:125` (`NOT a purchaser within definition 2`). src:52-55, 120-122.
- **Plain-English test of surprise**: A customer paying in instalments expects to hold the policy's rights meanwhile; the definition says there is no purchaser yet.

### VN-01 X11 — Limitation clock runs from undefined "dispute arises"
- **Class**: T1 / T5
- **Scenario**: The three-year bar to sue runs from when a dispute "arises", which is undefined; the complaint period is called both a time limit and a limitation period.
- **Who bears it**: policyholder. **Money direction**: unclear.
- **Standing**: LITERAL ("Otherwise reading only").
- **Evidence**: `bvvcx-tests-contract.l4:287` (`#ASSERT REFUSED 9.3 — the last day to sue` … "the record does not say when the dispute arose"). src:411-418.
- **Plain-English test of surprise**: A customer expects to know the last day to sue; the wording gives no starting point.

### VN-01 X12 — Signature recital stands in for proof of understanding
- **Class**: T3
- **Scenario**: The notice makes a signature on the request form evidence that the purchaser understood every term, exclusions included. LAW Article 19(2) requires the insurer to explain exclusions and hold evidence the purchaser understood; a form recital is weaker evidence.
- **Who bears it**: policyholder. **Money direction**: unclear.
- **Standing**: LAW (Article 19(2), aid 435-440); fork F3 says whether the recital satisfies it "is not decided". Reading only.
- **Evidence**: No assertion. src:7-12, 63-68.
- **Plain-English test of surprise**: A customer expects exclusions to be explained; the form treats a signature as proof they were.

### VN-01 X13 — Insurer discretion and undefined standards with weight on them
- **Class**: T11 / T5
- **Scenario**: 15.1.3 allows a reduction "up to 100%" by degree of fault with no scale; 13.3.2 values a kept wreck at the insurer's own figure; "serious" accidents, "special cases", "as the regulations provide" and "Người thụ hưởng" are undefined.
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: LITERAL (evidence for the first; "the rest reading only").
- **Evidence**: `bvvcx-tests-settlement.l4:117` (`#ASSERT REFUSED` … "a ground of 15.1.3 applies and the insurer has fixed no rate for it"). src:628-630, 569-571, 216, 326, 499-500, 55.
- **Plain-English test of surprise**: A customer expects a stated rule for the cut; the insurer may take up to the whole claim.

### VN-01 X14 — Driver, not a party, made to pay assessment cost
- **Class**: T13 (obligation imposed on a non-party)
- **Scenario**: Where the independent assessment agrees with the insurer's, 6.3 makes "the insured and the driver" pay its cost. The driver (def 8) is not a party to the contract.
- **Who bears it**: insured / third party (the driver). **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `bvvcx-tests-contract.l4:221` (`6.3 — who pays …` `EQUALS LIST the insured, the driver`). src:322-325.
- **Plain-English test of surprise**: A person who merely drove with consent would not expect to owe costs under someone else's policy; the wording names that person as a payer.

### VN-01 X15 — Add-on BVVC01 literally cancels the repair-at-value rule
- **Class**: T6 / T7
- **Scenario**: Article 16 (BVVC01, new-for-old) cancels "the partial-loss provision in sub-point b of 13.1.2" wholesale, then restores only new parts at actual cost. Repairs survive under 13.1.1's general promise, but a literal reader could argue the add-on removes repair cover.
- **Who bears it**: policyholder. **Money direction**: against the claimant (on the literal reading).
- **Standing**: CONTESTED. "Reading only; the encoding keeps repairs paid."
- **Evidence**: No assertion. src (Article 16) 677-680.
- **Plain-English test of surprise**: A customer buying a new-for-old add-on expects more cover; the literal wording could take repair cover away.

### VN-01 X16 — Car-hire add-on literally capped at one day's benefit
- **Class**: T5 / T6
- **Scenario**: BVVC05 says total compensation "does not exceed the sum insured per day and … per event". With 800,000 a day and 8,000,000 an event, ten days at 1,000,000 pay 800,000 on the literal reading against 5,600,000 on the reading taken.
- **Who bears it**: policyholder. **Money direction**: against the claimant (on the literal reading).
- **Standing**: CONTESTED (fork F38 takes the per-day reading; the literal one is shown).
- **Evidence**: `bvvcx-tests-findings.l4:138` (literal `EQUALS 800_000`), `:139` (taken `EQUALS 5_600_000`). src:735-738.
- **Plain-English test of surprise**: A customer buying ten days of hire-car cover expects ten days' benefit; the literal cap pays one.

### VN-01 X17 — Six-hour notice rule has no force-majeure exception
- **Class**: T12 / T3
- **Scenario**: The insurer is told 10 hours after a collision because of force majeure; 15.1.1(a) still takes 10% (payout 14,350,000). 15.1.1(b) excuses late written notice for force majeure, but (a) does not, and the cut is not tied to any prejudice to the insurer.
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: LAW (Articles 19(3) and 46(1), aid 441-444, 917-927; fork F48 encodes as written).
- **Evidence**: `bvvcx-tests-findings.l4:145` (`force majeure TRUE` … `EQUALS 14_350_000`). src:601-602, 604-605.
- **Plain-English test of surprise**: A customer prevented by force majeure from calling expects no penalty; the wording deducts 10% anyway.

### VN-01 X18 — Same drowned engine paid fully or not, by "operating"
- **Class**: T5 / T7
- **Scenario**: A flood reaches a parked car: 10.1.3 pays the 40,000,000 engine repair less the base deductible (39,500,000) without BVVC03. Driven into the same water: 11.12 excludes it (0) unless BVVC03, which pays 35,500,000 after its own 10% deductible. "Operating" is undefined.
- **Who bears it**: policyholder. **Money direction**: unclear (depends on the undefined term).
- **Standing**: CONTESTED (rests on F11: a parked car is not "operating").
- **Evidence**: `bvvcx-tests-settlement.l4:259` (parked, no clause, `EQUALS 39_500_000`), `:257` (driving, BVVC03, `EQUALS 35_500_000`). src:430, 479-480, 690-699.
- **Plain-English test of surprise**: A customer expects flood damage treated alike parked or moving; the flood add-on pays less than base cover pays a parked car.

### VN-01 X19 — Either party may end the contract with immediate effect
- **Class**: T1 / T3
- **Scenario**: A notice stating no time ends the contract on its own date, with no notice period: the purchaser may be uninsured from the date of the insurer's letter, before receiving it. LAW Article 26 permits unilateral termination only on listed grounds.
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: LITERAL (the encoding does not test grounds; LAW Article 26 is noted).
- **Evidence**: `bvvcx-tests-contract.l4:136` (notice of 20 June, no date stated: on 20 June `EQUALS ended by a notice of unilateral termination (3.2.1)`). src:153-158.
- **Plain-English test of surprise**: A customer expects some warning before cover ends; the wording ends it the day the letter is dated.

### VN-01 X20 — Total-loss add-on pays above market value
- **Class**: T13 (indemnity above actual loss)
- **Scenario**: Insured at 600,000,000; market value at the loss 580,000,000. Without BVVC06 the total loss pays 580,000,000; with it, 600,000,000. LAW Article 16(3) allows paying above actual loss only by agreement, "which this is".
- **Who bears it**: insurer. **Money direction**: against the insurer.
- **Standing**: CONTESTED (rests on F39: "pay it" rather than "up to it").
- **Evidence**: `bvvcx-tests-findings.l4:158` (`EQUALS 580_000_000`), `:159` (`EQUALS 600_000_000`). src:745-751, 557-559.
- **Plain-English test of surprise**: An insurer expects indemnity never to exceed the car's value; this add-on pays the higher sum insured.

### VN-01 X21 — Fraud exclusion 11.15 has nothing to exclude
- **Class**: T6 / T7
- **Scenario**: If taking by fraud or abuse of trust is not theft or robbery (F25), such a loss is outside 10.1 anyway and 11.15 is declaratory. If it is, 11.15's parenthesis leaves fraud on a vehicle not hired, lent or disputed covered. The drafting suggests a broader 10.1.4 than its words.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: CONTESTED (rests on F25 and F26).
- **Evidence**: `bvvcx-tests-cover.l4:28` (fraud `EQUALS outside the cover of Article 10`), `:196` (11.15 true for a hired vehicle). src:431, 485-486.
- **Plain-English test of surprise**: A reader expects an exclusion to remove something the cover would otherwise pay; on the reading taken it removes nothing.

### VN-01 X22 — Leaving after refused premium cut costs 30%
- **Class**: T6 / T13 (penalty for exercising a granted right)
- **Scenario**: 5.2.4(a) lets the purchaser end the contract if the insurer refuses to cut the premium for a lower risk, but 3.2.2 refunds only 70% of the unexpired premium: ended 2 July, 1,281,000 of the 1,830,000 unearned. LAW Article 27(2) refunds "as agreed in the contract".
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: LITERAL ("Reading only").
- **Evidence**: `bvvcx-tests-contract.l4:157` (`3.2.2 — the refund …` `EQUALS 1_281_000`). src:258-261, 159-163.
- **Plain-English test of surprise**: A customer leaving because the insurer would not lower the premium for a lower risk expects a full pro-rata refund; the wording keeps 30%.

### VN-01 X23 — Termination notice may name a date already past
- **Class**: T1
- **Scenario**: An insurer's notice dated 20 June names 1 June as the end date. A loss on 15 June then finds the contract already ended, and the claim fails.
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: LITERAL (fork F47: "nothing forbids it"; LAW Article 26 limits grounds, not tested).
- **Evidence**: `bvvcx-tests-findings.l4:174` (`EQUALS the contract was not in effect … ended by a notice of unilateral termination (3.2.1)`). src:153-156.
- **Plain-English test of surprise**: A customer expects termination to work only forwards; the wording lets a notice reach back past a loss.

### VN-01 X24 — Risk change penalised inside its own reporting window
- **Class**: T1 / T12
- **Scenario**: The car is converted on Wednesday 10 June 2026; 5.2.4 allows until 1 July to report it. A loss on 15 June is cut by the premium shortfall (3,650,000 of 4,380,000), to 13,250,000, though no deadline was missed.
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: CONTESTED (rests on F46; (ii) "no" is the alternative).
- **Evidence**: `bvvcx-tests-findings.l4:181` (`EQUALS YMD 2026 7 1`), `:182` (`EQUALS 13_250_000`). src:248-251, 647-650.
- **Plain-English test of surprise**: A customer still within the time allowed to report a change expects no penalty; the wording applies one.

#### VN-01 row summary
- Findings in §4: **24** (X1-X24); 24 records.
- Most counterintuitive: X3 (meets the 24-hour theft deadline, still loses 10% under a six-hour clock: 580m to 522m); X4 (two policies exactly covering value pay 7.75m of a 16.5m loss); X1 (a drunk joyrider's crash is paid while the drunk friend's is excluded).
- The encoder's own top three: X3, X2, X6 with X7.
- Cross-row matches: X2 = VN-02 V2, VN-15 X29, VN-17 X-07 (no causal link); X4 = VN-02 V27, VN-15 X22 (double insurance stacked on under-insurance, wider than LAW Art 49(1)); X5 = VN-02 V3 (claim file excuses the inspection certificate, the exclusion does not); X6 + X7 = VN-02 V8, VN-15 X20, VN-17 X-01 + X-02, VN-18 X10, VN-10 R13 (insurer controls when the payment clock starts; no long-stop); X13 ≈ VN-02 V10/V11/V12, VN-15 X14, VN-17 X-06, VN-18 X15, VN-10 R6/R12 (discretion without criteria); X13's undefined beneficiary = VN-02 V15, VN-15 X12; X17 ≈ VN-17 X-04 (late-notice cut with no excuse, LAW Art 46.1); X3 and X8 ≈ VN-15 X3 (two clocks with different units for one act); X11 ≈ VN-17 X-05, VN-18 X11 (claim or complaint clock badly anchored); X14 ≈ VN-15 X23 (who pays the independent assessment); X18 ≈ VN-15 X9, VN-18 X21 (flood add-on and base exclusions interact badly); X21 ≈ VN-02 V21, VN-18 X18 (a provision with nothing to do); X22 = VN-15 X21, ≈ VN-17 X-12 (30% exit after a refused premium cut or on the policyholder's termination).

---

## VN-02 UIC AutoJoy voluntary motor

Encoding: `contracts/insurance/vn-uic-autojoy-motor-2018/encodings/legalese-2026-10-vn-02`.
Findings: `NOTES.md` §4 table (V1-V27). Findings module: `uic-autojoy-findings.l4`.

### VN-02 V1 — Total-loss costs break the "in every case" cap
- **Class**: T7 / T4
- **Scenario**: Sum insured equals market value, 500,000,000; total loss; costs of 25,000,000 and 25,000,000 on UIC's instructions. Art 10.2.3 adds the costs to the total-loss compensation: 549,500,000, though Art 12.1 says compensation "in every case" never exceeds the sum insured.
- **Who bears it**: insurer. **Money direction**: against the insurer.
- **Standing**: CONTESTED (on fork F16; under reading (ii) the cap cuts the costs and "Art 10.2.3 would be dead letter"; LAW Art 51.3 supports F16).
- **Evidence**: `uic-autojoy-findings.l4:29` (`amount payable` `EQUALS 549_500_000`). src:335-337, 398-399.
- **Plain-English test of surprise**: A reader expects a cap stated "in every case" to hold; another clause pays above it.

### VN-02 V2 — Exclusions apply without causal link to the loss
- **Class**: T2
- **Scenario**: A parked car with a lapsed inspection certificate is struck by a tree falling in a storm: excluded by 11.2. A driver with any trace of alcohol, stopped at a red light and hit from behind, is excluded by 11.4. 11.3, 11.5, 11.7 and 11.16 work the same way.
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `uic-autojoy-findings.l4:38` (`excluded by 11.2 …`), `:43` (`excluded by 11.4 …`). src:343-357, 380.
- **Plain-English test of surprise**: A customer expects an exclusion to bite only if the circumstance contributed to the loss; here it bites regardless.

### VN-02 V3 — New car excused from certificate, then excluded for lacking it
- **Class**: T7 / T2
- **Scenario**: A new car within its first registration and inspection has no certificate yet. Art 7.1.2.4 does not ask for one in the claim file, but Art 11.2 excludes every loss without one unless the add-on is bought.
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `uic-autojoy-findings.l4:53` (`excluded by 11.2 …`); `uic-autojoy-tests-general.l4:212` (Art 7 lists 8 documents for this case, not 9). src:255-258, 343-345.
- **Plain-English test of surprise**: A buyer of a brand-new car expects cover on the drive to registration; the wording excludes it.

### VN-02 V4 — Unclear whether excluded damage counts toward 75% total-loss test
- **Class**: T5 / T4
- **Scenario**: A flood hydro-locks the engine (excluded; 300,000,000 new) and damages the body (80,000,000); value 480,000,000. Counting covered damage only, the loss is partial and pays 79,000,000. Counting all damage (380,000,000, above 75% of 480,000,000) makes it a total loss paying about 400,000,000 more.
- **Who bears it**: insurer. **Money direction**: against the insurer (on the alternative reading).
- **Standing**: CONTESTED (fork F21 takes covered parts only).
- **Evidence**: `uic-autojoy-findings.l4:71` (`EQUALS 79_000_000`), `:72` (all-damage sum `AT LEAST 75% TIMES 480_000_000`). src:365-369, 435-437.
- **Plain-English test of surprise**: Excluded damage should not raise a payout; on one reading it turns a 79m claim into a total loss.

### VN-02 V5 — Overloading by exactly 50% escapes every penalty
- **Class**: T4 / T7
- **Scenario**: A truck permitted 10,000 carries 14,999 (49.99% over) and is cut by 49.99%, paying 6,001,400. At exactly 15,000 (50%) neither 11.16 ("more than 50%") nor 15.1.4 ("less than 50%") applies, so 13,000,000 is paid in full. At 15,001 the loss is excluded.
- **Who bears it**: unclear. **Money direction**: unclear (a cliff in both directions).
- **Standing**: LITERAL.
- **Evidence**: `uic-autojoy-findings.l4:85` (`EQUALS 6_001_400`), `:86` (`EQUALS 13_000_000`), `:87` (`excluded by 11.16 …`). src:380, 504.
- **Plain-English test of surprise**: A customer expects more overloading to cost more; exactly 50% over costs nothing, one unit less costs half.

### VN-02 V6 — Premium kept collectable while cover is refused
- **Class**: T6 / T7
- **Scenario**: UIC agrees the July instalment may be owed (Art 3.1), so the contract does not end and the whole premium (5,475,000) stays collectable (Art 16.2). Yet Art 16.1 refuses every loss after the missed due date "whether or not the contract has ended": an August collision is refused.
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `uic-autojoy-findings.l4:103` (end day `EQUALS NOTHING`), `:104` (`EQUALS 5_475_000`), `:105` (`the premium had not been paid in full and on time`). src:98-100, 527-530, 533-536.
- **Plain-English test of surprise**: A customer allowed to pay late expects to stay covered; the wording keeps charging but pays nothing.

### VN-02 V7 — Refusal found after verification cannot be given in time
- **Class**: T1
- **Scenario**: Where UIC verifies, it has up to 30 days to pay (Art 4.2.3) but must explain a refusal within 15 days of the complete file (Art 4.2.4). A ground to refuse found on day 20 is too late for 4.2.4 and is not a payment under 4.2.3.
- **Who bears it**: insurer. **Money direction**: unclear.
- **Standing**: LITERAL.
- **Evidence**: `uic-autojoy-tests-duties.l4:72-74` (refusal `AT 20`, `WAIT UNTIL 31`; comment at `:64-67`: "BREACH BY UIC on both sides"). src:141-150.
- **Plain-English test of surprise**: One expects the time to refuse to cover the time to investigate; here the refusal window closes first.

### VN-02 V8 — No settlement deadline if police never conclude
- **Class**: T1 / T11
- **Scenario**: When the authority never concludes, the file never counts as complete; after 90 days UIC must verify on its own, with no time set to settle. There is no long-stop.
- **Who bears it**: policyholder. **Money direction**: against the claimant (timing).
- **Standing**: LITERAL.
- **Evidence**: `uic-autojoy-tests-duties.l4:85` (`#ASSERT REFUSED` … "Art 4.2.3 sets no time for UIC to settle on its own verification after the 90 days"). src:143-147.
- **Plain-English test of surprise**: A customer expects every claim to have an outside payment date; this route has none.

### VN-02 V9 — Five-day written-notice duty has no consequence
- **Class**: T13 (duty without sanction)
- **Scenario**: The policyholder sends written notice on day 9 instead of within 5 days (Art 5.2.6.3). The breach is recorded but nothing in the Rules reduces or refuses the claim for it; the rate applied is 0. LAW Art 46.2 bars inventing a sanction.
- **Who bears it**: insurer. **Money direction**: no money.
- **Standing**: LITERAL (consistent with LAW Art 46.2, aid 928-932).
- **Evidence**: `uic-autojoy-findings.l4:114` (`Art 15.2 — the one rate applied …` `EQUALS 0`); `uic-autojoy-tests-duties.l4:155-156` (bare breach trace). src:207-209.
- **Plain-English test of surprise**: A reader expects a stated duty to carry a consequence; this one carries none.

### VN-02 V10 — "The 2 duties above" when three are listed
- **Class**: T7 / T11
- **Scenario**: The hotline and police are not told, and the damage increases. Art 15.1.1.4 raises the reduction "up to 30%" for breaching "the 2 duties above", but three are listed, and nothing guides the rate between 10% and 30%.
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: CONTESTED (fork F24 reads "any two of the three"; alternatives: any one, or the two notice duties).
- **Evidence**: `uic-autojoy-tests-settlement.l4:209` (`#ASSERT REFUSED` … "Art 15.1.1.4 leaves the rate to UIC, and none was supplied"). src:480-492.
- **Plain-English test of surprise**: A customer expects to know which breaches trigger the heavier cut, and how heavy; the wording miscounts and leaves it open.

### VN-02 V11 — Insurer may cut 50-100% with no criteria
- **Class**: T11 / T3
- **Scenario**: The policyholder settles with the third party without UIC. Art 15.1.3 lets UIC deduct "50% to 100%" or "according to the degree of fault", with no criteria. LAW Art 54.1(b) allows only a fault-based deduction.
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: LAW (Art 54.1(b), aid 1034-1037; fork F25 reads any rate 0-100%). Reading only.
- **Evidence**: `uic-autojoy-tests-settlement.l4:233` (`#ASSERT REFUSED` … "Art 15.1.3 leaves the rate to UIC, and none was supplied"). src:499-503.
- **Plain-English test of surprise**: A customer expects a cut proportioned to fault; the wording lets the insurer take at least half regardless.

### VN-02 V12 — Kept wreck at insurer's own valuation can zero payout
- **Class**: T11 / T4
- **Scenario**: A total loss with market value 480,000,000; the policyholder keeps the wreck, which UIC values at 479,000,000. 480,000,000 − 1,000,000 deductible − 479,000,000 = 0: nothing is paid, on a valuation with no criteria.
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `uic-autojoy-findings.l4:124` (`EQUALS 0`). src:450-452.
- **Plain-English test of surprise**: A customer keeping a wrecked car expects its scrap value deducted; the insurer's own valuation can absorb the whole payout.

### VN-02 V13 — Truck cargo body excluded "whatever the cause"
- **Class**: T2
- **Scenario**: An insured collision damages only a truck's maker-fitted cargo body (repair 30,000,000). Tyres, tarpaulins, the cargo body and labels are excluded "whatever the cause", and the saving for maker-fitted items covers labels only, so nothing is covered without the add-on.
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: LITERAL (fork F13 reads the saving as labels only).
- **Evidence**: `uic-autojoy-findings.l4:132` (`every damaged part is excluded`). src:370-372.
- **Plain-English test of surprise**: A truck owner expects collision damage to the truck's body to be covered; the cargo body never is.

### VN-02 V14 — Sum insured above value buys nothing, no premium returned
- **Class**: T7 / T6
- **Scenario**: A 500,000,000 car is insured for 600,000,000. Art 12.1 forbids this, Art 13.1.2.2 provides for it, and nothing returns the premium on the excess. A total loss pays 499,000,000; no loss can reach the sum insured. "Giá trị thực tế" is undefined beside the defined "giá thị trường".
- **Who bears it**: policyholder. **Money direction**: against the claimant (premium on the excess).
- **Standing**: LITERAL (NOTES §3 notes LAW Art 47.2 requires a refund for over-insurance by mistake; "the document is silent").
- **Evidence**: `uic-autojoy-findings.l4:142` (`EQUALS 499_000_000`). src:397-398, 421-424.
- **Plain-English test of surprise**: A customer paying premium on 600m expects either 600m of cover or a refund; the wording gives neither.

### VN-02 V15 — Who is paid, and who the policyholder is, shifts
- **Class**: T5 / T7
- **Scenario**: Art 1 says UIC compensates "Người Được Bảo Hiểm/chủ xe", def 3 the insured, Art 10.1 "Chủ Hợp Đồng Bảo Hiểm", and Art 5.1.2 names a beneficiary the definitions never define. A financed car whose bank is named beneficiary has no clear payee.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL (reading only).
- **Evidence**: No assertion. src:40-41, 72-73, 163, 321.
- **Plain-English test of surprise**: A customer and a lending bank expect the policy to say who receives the money; it names four different people.

### VN-02 V16 — "Suspension" of performance granted but never explained
- **Class**: T5
- **Scenario**: Art 5.2.4.1 and 5.2.4.2 let either side "đơn phương đình chỉ thực hiện" (suspend performance of) the contract, for example after UIC refuses a premium reduction. What a suspension does to cover and premium is said nowhere.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL (reading only).
- **Evidence**: No assertion. src:186-193.
- **Plain-English test of surprise**: A customer who suspends the contract expects to know whether cover and premium pause; the wording is silent.

### VN-02 V17 — Published rules may be a later, incomplete revision
- **Class**: T8 / T13 (document provenance)
- **Scenario**: The heading cites a 2018 decision, but Part 3 applies a Circular of 15 January 2021; the PDF was made from Excel on 4 August 2021; every page is numbered "N/21" though the file has 11 pages. Pages 12-21 may be missing.
- **Who bears it**: unclear. **Money direction**: no money.
- **Standing**: CONTESTED (the encoder hedges: the file "may be a later revision, and may be incomplete").
- **Evidence**: No assertion; `pdfinfo uic-autojoy.pdf` (CreationDate 2021-08-04, Creator Microsoft Excel 2016, Pages 11). src:1-4, 57-629 (footers), 623-624.
- **Plain-English test of surprise**: A customer expects the published wording to be complete and current; this file shows signs of neither.

### VN-02 V18 — 10% cap on costs can never bind
- **Class**: T6 / T7
- **Scenario**: Art 10.2.3 caps costs on a total loss at 10% of the sum insured, but its two heads are each already capped at 5%. Costs of 100,000,000 each pay 25,000,000 each: 50,000,000, exactly the 10% cap.
- **Who bears it**: unclear. **Money direction**: no money.
- **Standing**: LITERAL.
- **Evidence**: `uic-autojoy-findings.l4:154` (`EQUALS 2 TIMES 5% TIMES 500_000_000`). src:331-337.
- **Plain-English test of surprise**: A reader expects a cap to limit something; this one is redundant.

### VN-02 V19 — Passenger with no workplace may get zero days
- **Class**: T5 / T2
- **Scenario**: Part 2 Art 4.2(b) counts the shorter of the days of treatment and the days off work confirmed by a workplace. An unemployed passenger with 30 days of treatment has no second count, and "a literal insurer could say zero days".
- **Who bears it**: insured. **Money direction**: against the claimant (on the literal reading).
- **Standing**: CONTESTED (the encoding refuses to decide).
- **Evidence**: `uic-autojoy-tests-p2-p3.l4:178` (`#ASSERT REFUSED` … "the person has no workplace to confirm the second"). src:594-598.
- **Plain-English test of surprise**: A child, retiree or unemployed passenger expects treatment days to count; the wording can reduce them to nothing.

### VN-02 V20 — Death after the term pays more than death within it
- **Class**: T7 / T10
- **Scenario**: 30,000,000 was paid for an injury; the person dies of it after the term. Art 4.4 deducts earlier payments only for a death "within the contract term", so Art 4.1 pays the whole 100,000,000 (or, on the insurer's reading, nothing).
- **Who bears it**: insurer. **Money direction**: against the insurer (on the reading taken).
- **Standing**: CONTESTED (fork F34 takes the literal text; alternatives: no cover after the term, or pay the difference).
- **Evidence**: `uic-autojoy-tests-p2-p3.l4:194` (`death in term FALSE`, `paid 30_000_000` → `payable under Part 2 100_000_000`). src:582-583, 605-607.
- **Plain-English test of surprise**: One expects the same net payment whenever death occurs; this pays 30m more, or nothing.

### VN-02 V21 — Theft cover literally requires a disaster or accident cause
- **Class**: T6 / T7
- **Scenario**: Read as written, Art 10.1's chapeau requires every covered loss, theft (1.4) included, to be "caused by a natural disaster or a sudden, unforeseeable accident", which no theft is. On that reading theft cover is empty.
- **Who bears it**: policyholder. **Money direction**: against the claimant (on the literal reading).
- **Standing**: CONTESTED (fork F2 takes 1.4 as standing alone; reading only).
- **Evidence**: No assertion. src:321-328.
- **Plain-English test of surprise**: A customer buying theft cover expects it to pay for theft; the literal chapeau makes that impossible.

### VN-02 V22 — Renewals leave a two-minute gap each year
- **Class**: T1 / T10
- **Scenario**: With the default hours, a policy ends at 23:59 on 31 December and the next starts at 00:01 on 1 January. A loss at 00:00 on 1 January 2027 falls in neither period.
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: LITERAL (fork F5, at the minute).
- **Evidence**: `uic-autojoy-findings.l4:162` (`NOT … within the 2026 period … at 0h0 on 2027-01-01`), `:163` (`NOT` within the 2027 period). src:93-94.
- **Plain-English test of surprise**: A customer renewing without a break expects continuous cover; the default hours leave a gap at midnight.

### VN-02 V23 — Any insured event forfeits the refund, even one unpaid
- **Class**: T6 / T12
- **Scenario**: A 400,000 scratch, below the 1,000,000 deductible, pays nothing. The policyholder then ends the contract with 100 days left and gets no refund either, because an insured event "has occurred".
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `uic-autojoy-findings.l4:171` (`EQUALS 0`), `:172` (refund `EQUALS 0`). src:115-117.
- **Plain-English test of surprise**: A customer whose claim paid nothing expects the usual 70% refund; the wording withholds it.

### VN-02 V24 — Mitigation is required but paid only if instructed
- **Class**: T6 / T3
- **Scenario**: A policyholder spends 12,000,000 on rescue before calling UIC. Art 10.2 reimburses costs only if incurred on UIC's request and instructions, so 0 is paid; a policyholder who does not mitigate is cut 10% (Art 15.1.1.3).
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: LAW (Art 51.3, aid 991-996, "does not attach that condition to prevention costs").
- **Evidence**: `uic-autojoy-findings.l4:183` (costs `EQUALS 0`), `:184` (rate `EQUALS 10%`). src:200-202, 329-331, 489-491.
- **Plain-English test of surprise**: A customer told to limit the damage expects to be repaid for doing so; prompt action before instructions is at the customer's cost.

### VN-02 V25 — Two Parts treat the same driver differently
- **Class**: T7
- **Scenario**: A driver's licence has expired. Part 1 (vehicle damage) excludes the loss under 11.3; Part 2 (persons carried) names only "no licence" and "not appropriate", so the same accident is covered there. Learner driving and illegal goods differ the other way.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL (fork F32).
- **Evidence**: `uic-autojoy-findings.l4:194` (Part 1 `excluded by 11.3 …`), `:195` (`NOT P2 Art 3.6 …`). src:346-349, 357, 576-580.
- **Plain-English test of surprise**: A customer expects one accident by one driver to be judged the same way across one policy; the Parts disagree.

### VN-02 V26 — "One loss" undefined for fire, storm or theft
- **Class**: T5
- **Scenario**: "Vu tổn thất" (one loss), the unit of the deductible and of Part 2's "180 ngày/vụ", is defined only as an accident. A storm that damages the car twice in one night has no defined count, so the tiered deductible is undefined.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL (reading only).
- **Evidence**: No assertion. src:467-476, 595.
- **Plain-English test of surprise**: A customer expects to know how many deductibles one storm costs; the wording does not say.

### VN-02 V27 — Two policies covering full value pay under half
- **Class**: T4 / T3
- **Scenario**: A 500,000,000 car is insured for 250,000,000 with UIC and 250,000,000 with another insurer. Article 8 calls this double insurance. On a 14,000,000 loss UIC pro-rates for under-insurance, deducts 1,000,000, then takes its 50% share: 3,000,000. Both together pay 6,000,000.
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: LAW (Art 49.1, aid 965-968: double insurance only where sums exceed the value; fork F41 follows the document).
- **Evidence**: `uic-autojoy-findings.l4:210` (`EQUALS 3_000_000`). src:294-299.
- **Plain-English test of surprise**: A customer whose two policies exactly cover the car expects the loss paid less deductibles; the wording pays well under half.

#### VN-02 row summary
- Findings in §4: **27** (V1-V27); 27 records.
- Most counterintuitive: V5 (overloading by 49.99% halves the payout, by exactly 50% costs nothing, by 50.01% loses everything); V6 (instalment allowed, premium still collectable, every claim refused); V12 (insurer's own wreck valuation of 479m zeroes a 480m total loss).
- Cross-row matches within VN-01: V2 = X2 (no causal link); V3 = X5 (claim file excuses the inspection certificate, exclusion does not); V8 = X7 (no deadline after 90 days without police conclusion); V27 = X4 (double insurance stacked on under-insurance, wider than LAW Art 49.1); V11, V10, V12 ≈ X13 (insurer discretion on rate and wreck); V15 ≈ X13 (undefined beneficiary); V23 ≈ X22 (refund penalised on termination).

---

## VN-15 OPES O-Car motor physical damage

Encoding: `contracts/insurance/vn-opes-ocar-motor-physical-damage/encodings/legalese-2026-10-vn-15`.
Findings: `NOTES.md` §4 table (X1-X29). Findings module: `ocar-tests-findings.l4`.

### VN-15 X1 — Exercising a data-protection right ends cover at 30% loss
- **Class**: T13 (sanction for exercising a statutory right) / T6
- **Scenario**: Premium 12,000,000 for 2026. On 1 July the Insured exercises a right under Decree 13/2023 Art 9 clause 5. Data clause 10 ends the contract as the Policyholder's own termination: refund 70% × 12,000,000 × 183/365, or nothing after a loss.
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `ocar-tests-findings.l4:38` (contract ends), `:39` (`EQUALS JUST ((70% TIMES 12_000_000 TIMES 183) DIVIDED BY 365)`), `:40` (after a loss `EQUALS JUST 0`). src:1242-1249, 184-190.
- **Plain-English test of surprise**: A customer exercising a data right expects no effect on cover; the policy ends and at least 30% is kept.

### VN-15 X2 — Battery both exempt from and subject to depreciation
- **Class**: T7
- **Scenario**: With the no-depreciation clause BS01, a battery is replaced new for 10,000,000. 14.1.2(c) and BS01 list what is still depreciated and omit the battery; 14.1.2(d) depreciates the battery "in every case". The encoding pays 5,000,000.
- **Who bears it**: policyholder. **Money direction**: against the claimant (on the reading taken).
- **Standing**: CONTESTED (fork F29 takes (d); reading (ii), not depreciated, is listed).
- **Evidence**: `ocar-tests-findings.l4:47-48` (neither list contains a battery), `:49` (`EQUALS 5_000_000`). src:823-833, 1017-1023.
- **Plain-English test of surprise**: A customer who paid for no-depreciation cover expects a new battery paid in full; it is paid at half.

### VN-15 X3 — Notice on time under 5.2 is late under 16.1.1
- **Class**: T1 / T12
- **Scenario**: Loss on Wednesday 10 June 2026, notice on Wednesday 17 June. 5.2 allows five working days, so notice is on time; 16.1.1 cuts 5-10% for notice not sent within five days. The least payable falls to 8,550,000 of 9,500,000.
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: LITERAL (fork F39: "five days" are calendar days, the words differing from 5.2's).
- **Evidence**: `ocar-tests-findings.l4:56` (5.2 met), `:57` (16.1.1 applies), `:58` (`EQUALS 8_550_000`). src:330-332, 917-923.
- **Plain-English test of surprise**: A customer who meets the policy's notice deadline expects no penalty; another clause with a shorter count takes up to 10%.

### VN-15 X4 — Adding a child passenger removes the overload reduction
- **Class**: T4 / T7
- **Scenario**: Seven adults in a five-seat car: 40% over, no exclusion, a 40% reduction, so a 10,000,000 repair pays 5,700,000. Add a child under 7: 12.18 (not counting children) still sees 40%, 16.1.5 (counting children) sees 60%, not "under 50%", so no reduction: 9,500,000.
- **Who bears it**: insurer. **Money direction**: against the insurer.
- **Standing**: LITERAL (fork F27: children counted under 16.1.5).
- **Evidence**: `ocar-tests-findings.l4:68` (`EQUALS 5_700_000`), `:69` (`EQUALS 9_500_000`). src:683-688, 962-964.
- **Plain-English test of surprise**: One expects a more overloaded car to be treated worse; it is paid in full.

### VN-15 X5 — Termination takes effect on receipt, or five working days later
- **Class**: T1 / T7
- **Scenario**: A termination notice is received Monday 5 October 2026. 3.2.1 requires at least five working days' notice, so the earliest end is 12 October; 3.2.2 ends the contract when the Insurer receives the notice, 5 October.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL.
- **Evidence**: `ocar-tests-findings.l4:75` (`EQUALS YMD 2026 10 12`), `:76` (`EQUALS YMD 2026 10 5`). src:179-183, 190-192.
- **Plain-English test of surprise**: A customer expects one end date for one notice; the wording gives two a week apart.

### VN-15 X6 — Untruthful documents: lose everything, or at most 30%
- **Class**: T7 / T11
- **Scenario**: For a 10,000,000 repair, 12.22 excludes the whole loss where the Insurer proves the information untruthful (0 paid); 16.1.4 reduces up to 30% where the Owner was untruthful, with no proof required (at least 6,650,000). The Insurer chooses its burden.
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `ocar-tests-findings.l4:82` (`EQUALS 0`), `:83` (`EQUALS 6_650_000`). src:698-701, 950-951.
- **Plain-English test of surprise**: A customer expects one consequence for one act; the insurer may pick the harsher route.

### VN-15 X7 — Sub-limit add-on BS04 leaves a hole past its limit
- **Class**: T13 (no rule for the case) / T6
- **Scenario**: BS04 settles at full value "until" its sub-limit and cancels the under-insurance rule without condition. With a 100,000,000 sub-limit, 90,000,000 already paid and a 20,000,000 new loss, nothing says how the excess, or later partial losses, are settled.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL.
- **Evidence**: `ocar-tests-findings.l4:91` (`#ASSERT REFUSED` … "BS04 does not say how a partial loss is settled beyond the sub-limit"). src:1063-1076.
- **Plain-English test of surprise**: A customer expects the add-on to say what happens once its limit is reached; it does not.

### VN-15 X8 — Parts-loss add-on has no limit for short contracts
- **Class**: T13 (no rule for the case) / T10
- **Scenario**: BS05 allows 2 parts losses for contracts of 12-18 months and 3 for over 18 months, and says nothing for a contract under 12 months, such as a six-month contract.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL.
- **Evidence**: `ocar-tests-findings.l4:95` (`#ASSERT REFUSED` … "BS05 states no limit for a contract shorter than 12 months"). src:1097-1099.
- **Plain-English test of surprise**: A customer buying the add-on on a short policy expects some number of covered losses; none is stated.

### VN-15 X9 — Flood electrical add-on collides with short-circuit exclusion
- **Class**: T6 / T2
- **Scenario**: BS03 covers electrical damage from driving into flood water but cancels only 12.12; 12.13 excludes short-circuit damage "by any cause", so read literally the extension is largely empty. Without BS03, a natural-catastrophe flood that shorts the electrics (8,000,000) is excluded though flood is an insured peril.
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: CONTESTED (fork F21 lets BS03 prevail, specific over general and LAW Art 24).
- **Evidence**: `ocar-tests-findings.l4:102` (plain policy: `12.13 electrical or mechanical breakdown`), `:104` (with BS03: `EQUALS EMPTY`). src:652-656, 1049-1053.
- **Plain-English test of surprise**: A buyer of flood-electrics cover expects it to pay; another exclusion literally cancels it.

### VN-15 X10 — No valuation rule for a car imported new
- **Class**: T13 (no rule for the case) / T5
- **Scenario**: 13.2 values a used Vietnamese-made car and one imported after use abroad. A car imported new and used in Vietnam since, whose market value cannot be determined, has no valuation rule.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL (fork F23).
- **Evidence**: `ocar-tests-findings.l4:108` (`#ASSERT REFUSED` … "13.2 gives no value for a new vehicle, or one imported new, whose market value cannot be determined"). src:736-744.
- **Plain-English test of surprise**: A customer expects the policy to say how the car is valued; for this car it does not.

### VN-15 X11 — Defined "time in use" unused; age fixed at inception
- **Class**: T5 / T10
- **Scenario**: 1.15 defines time in use to the contract month, but 13.2 and 14.1.2(b) use other words. Read as 1.15, depreciation on an 18-month BS05 contract, or on a loss late in the year, uses the car's age at inception.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: CONTESTED (fork F10; reading (ii) measures to the loss). Reading only.
- **Evidence**: No assertion. src:126-129, 747, 795.
- **Plain-English test of surprise**: A customer expects depreciation to reflect the car's age when damaged; on the reading taken it is frozen at the start.

### VN-15 X12 — "Người Thụ Hưởng" used as defined but never defined
- **Class**: T5
- **Scenario**: "Người Thụ Hưởng" (beneficiary) is capitalised as a defined term and never defined, so who may receive payment is left open.
- **Who bears it**: beneficiary. **Money direction**: unclear.
- **Standing**: LITERAL (reading only).
- **Evidence**: No assertion. src:111, 1146.
- **Plain-English test of surprise**: A lender or family member named as beneficiary expects the term to be defined; it is not.

### VN-15 X13 — Ownership-transfer clause is misheaded and contradicts itself
- **Class**: T7 / T5
- **Scenario**: 2.3 is headed "declaring information when applying" but deals with transfer of ownership. It says benefits pass "mặc nhiên" (automatically), then that the Policyholder may decline to pass them.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: CONTESTED (fork F12 reads automatic transfer unless the Policyholder asks for a refund). Reading only.
- **Evidence**: No assertion. src:139-148.
- **Plain-English test of surprise**: A buyer of a used car expects to know whether the insurance came with it; the clause says both yes and maybe.

### VN-15 X14 — Reductions are ranges with no criteria
- **Class**: T11
- **Scenario**: A 10,000,000 collision repaired without approval: 16.1.3 allows any cut up to 80%, so the same claim may pay 9,500,000 or 1,900,000 at the Insurer's choice. Every Article 16 ground gives a range with no guide.
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `ocar-tests-findings.l4:115` (`EQUALS 9_500_000`), `:116` (`EQUALS 1_900_000`). src:913-976.
- **Plain-English test of surprise**: A customer expects a stated penalty; the insurer picks anywhere in a fivefold range.

### VN-15 X15 — Deductible on every loss, or partial losses only
- **Class**: T7 / T4
- **Scenario**: 1.8 and 15.2 apply the deductible to each loss; 15.1 to each partial loss. Whether a total loss bears a deductible depends on which clause governs.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: CONTESTED (fork F25 takes partial losses only, citing LAW Art 24). Reading only.
- **Evidence**: No assertion. src:87-91, 894-900.
- **Plain-English test of surprise**: A customer expects to know whether a write-off is reduced by the deductible; the clauses disagree.

### VN-15 X16 — Comparative in 16.1 chapeau lost its adjective
- **Class**: T5
- **Scenario**: 16.1 lets the Insurer state a reduction level "hơn" (more …) in the contract, without saying higher or lower than what. A contract stating a 10% level cannot be applied.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL.
- **Evidence**: `ocar-tests-findings.l4:120` (`#ASSERT REFUSED` … "16.1 lets the contract state a reduction level, but its comparative is incomplete"). src:913-915.
- **Plain-English test of surprise**: A reader expects a sentence to finish its comparison; this one does not.

### VN-15 X17 — Repair permitted by silence, then cut for lacking approval
- **Class**: T7 / T12
- **Scenario**: 5.2 lets the Policyholder repair after five working days of the Insurer's silence; 16.1.3 reduces up to 80% for repairing "without the Insurer's approval", and does not mention 5.2's deemed consent.
- **Who bears it**: policyholder. **Money direction**: against the claimant (on the literal reading).
- **Standing**: CONTESTED (fork F26 counts silence as approval). Reading only.
- **Evidence**: No assertion. src:326-329, 936-940.
- **Plain-English test of surprise**: A customer allowed to repair after the insurer stays silent expects no penalty; another clause penalises it.

### VN-15 X18 — Two total-loss limbs draw the 75% line differently
- **Class**: T7
- **Scenario**: Total loss is damage "trên 75%" (over 75%) on one limb and repair cost "bằng hoặc trên 75%" (75% or more) on the other, so a loss at exactly 75% qualifies on one and not the other.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL (reading only).
- **Evidence**: No findings assertion; both edges tested in `ocar-tests-amounts.l4` (comment at `:278`). src:849-852.
- **Plain-English test of surprise**: One expects one threshold for a write-off; the two limbs use two.

### VN-15 X19 — Amount paid out called the "sum insured"
- **Class**: T5 / T7
- **Scenario**: 4.1 calls the amount paid out the "Số Tiền Bảo Hiểm", which is the defined term for the sum insured.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL (reading only).
- **Evidence**: No assertion. src:228-230.
- **Plain-English test of surprise**: A customer reading "sum insured" expects the policy limit; here it means the payout.

### VN-15 X20 — Insurer's payment period may never start
- **Class**: T1 / T11
- **Scenario**: The Insurer pays within 15 or 30 working days of a "complete and valid" file; the file's contents are open-ended. Where the Insurer cannot verify, the file is complete only on the authority's conclusion; after 90 days the Insurer "may consider" settling. A theft is payable only on a judgment, with no time for it.
- **Who bears it**: policyholder. **Money direction**: against the claimant (timing).
- **Standing**: LITERAL.
- **Evidence**: `ocar-tests-findings.l4:126` (date the file counts as complete `EQUALS NOTHING`). src:238-252, 427-429, 488, 853-856.
- **Plain-English test of surprise**: A customer expects the payment clock to start when the claim is filed; it may never start.

### VN-15 X21 — Refused premium cut leaves a 30% exit
- **Class**: T6 / T13 (penalty for exercising a granted right)
- **Scenario**: The risk falls and the Insurer refuses to cut the premium (Article 6). The Policyholder's only remedy is termination under 3.2.2 on 1 July: 70% × 12,000,000 × 183/365, or nothing after an insured event.
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `ocar-tests-findings.l4:132` (may terminate), `:133` (refund `EQUALS (70% TIMES 12_000_000 TIMES 183) DIVIDED BY 365`). src:376-385, 184-190.
- **Plain-English test of surprise**: A customer whose risk fell expects a lower premium or a full refund; the wording keeps 30%.

### VN-15 X22 — Double insurance stacked on under-insurance halves twice
- **Class**: T4 / T3
- **Scenario**: A 600,000,000 car is insured twice at 300,000,000. Article 9 shares the loss though the total equals the value; 14.1.2(a) halves the loss for under-insurance, Article 9 halves it again: of a 10,000,000 loss OPES pays 2,000,000 after the deductible.
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: LAW (Art 49(1), aid 964-968; L6, encoded as the rules say; fork F4 applies both).
- **Evidence**: `ocar-tests-findings.l4:166` (`EQUALS 2_000_000`). src:503-523.
- **Plain-English test of surprise**: A customer whose two policies exactly cover the car expects the loss paid; each insurer pays a quarter, less deductibles.

### VN-15 X23 — One dong decides who pays the independent assessment
- **Class**: T13 (cliff-edge cost allocation) / T5
- **Scenario**: The Insurer assesses a collision at 10,000,000. An independent assessment of 10,000,000 leaves the Policyholder paying its cost and court fees; one of 10,000,001 "differs", so the Insurer pays.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL (fork F38: any difference counts; (ii) a material one).
- **Evidence**: `ocar-tests-findings.l4:170` (`EQUALS the Policyholder`), `:171` (`EQUALS the Insurer`). src:410-424.
- **Plain-English test of surprise**: One expects costs to follow who was substantially right; one dong flips them.

### VN-15 X24 — Complaint clause names different parties for one complaint
- **Class**: T7
- **Scenario**: Article 10 runs the complaint period from the Owner's receipt of the notice, but extends it where the Policyholder could not complain.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL (reading only).
- **Evidence**: No assertion. src:536-542.
- **Plain-English test of surprise**: A customer expects one person's clock and one person's excuse; the clause mixes two parties.

### VN-15 X25 — Unpaid claim below deductible forfeits the refund
- **Class**: T6 / T12
- **Scenario**: A scrape repaired for 400,000, below the 500,000 deductible, pays nothing. It is still an insured event, so the Policyholder who terminates on 1 July gets 0 instead of 70% × 12,000,000 × 183/365.
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: CONTESTED (rests on fork F6; reading (ii) counts only an event giving rise to payment).
- **Evidence**: `ocar-tests-findings.l4:178` (claim `EQUALS 0`), `:179` (refund after event `EQUALS 0`), `:180` (refund without event). src:176-177, 188-190, 694-695.
- **Plain-English test of surprise**: A customer whose claim paid nothing expects the normal refund; the wording withholds it.

### VN-15 X26 — Short-circuit exclusion reaches insured collisions and fires
- **Class**: T2
- **Scenario**: 12.13 excludes electrical damage from a short circuit "by any cause", including one caused by a collision or fire the policy insures. A collision that shorts the wiring is excluded for that item.
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `ocar-tests-cover.l4:226` (`item short circuit` → `12.13 electrical or mechanical breakdown`). src:652-656.
- **Plain-English test of surprise**: A customer expects wiring burnt in an insured crash to be covered; it is excluded.

### VN-15 X27 — Over-insurance forbidden by definition, then provided for
- **Class**: T7
- **Scenario**: 1.10 defines the sum insured so that it cannot exceed value, yet 13.2 and 14.1.2(b) set rules for a car insured above value.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL (reading only).
- **Evidence**: No assertion. src:96-98, 754-756, 788.
- **Plain-English test of surprise**: A reader expects a forbidden case not to need rules; the policy writes rules for it.

### VN-15 X28 — No grace period for late premium
- **Class**: T1 / T3
- **Scenario**: 3.1.1 ends the contract the moment the payment period ends; the Law contemplates termination only after a grace period for paying.
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: LAW (L8: Art 26(1), aid 627-628, "contemplates" a grace period; recorded, not encoded). Reading only.
- **Evidence**: No assertion. src:162-166.
- **Plain-English test of surprise**: A customer a day late with the premium expects a reminder and a few days' grace; cover ends at once.

### VN-15 X29 — Exclusions apply "while", without causal link
- **Class**: T2
- **Scenario**: 12.4 and 12.5 exclude a loss "khi" (while) the driver is over the limit or making a prohibited turn. A tree falling on the car during a prohibited U-turn is excluded.
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: LITERAL (fork F16; reading only).
- **Evidence**: No assertion. src:587-592, 622-629.
- **Plain-English test of surprise**: A customer expects an exclusion only where the conduct caused the loss; a falling tree is excluded.

#### VN-15 row summary
- Findings in §4: **29** (X1-X29); 29 records.
- Most counterintuitive: X1 (exercising a data-protection right cancels the policy and keeps 30% of premium, or all of it); X4 (adding a child to an overloaded car removes the reduction: 5.7m becomes 9.5m); X23 (a one-dong difference shifts the whole assessment cost).
- The encoder's own top three: X3, X25, X1.
- Cross-row matches: X22 = VN-01 X4 = VN-02 V27 (double insurance on under-insurance); X25 = VN-02 V23 (sub-deductible event forfeits refund); X21 = VN-01 X22 (30% exit after refused premium cut); X29, X26 ≈ VN-01 X2, VN-02 V2 (no causal link / overbroad); X20 = VN-01 X6 + X7, VN-02 V8 (payment clock may never start); X14 ≈ VN-01 X13, VN-02 V10, V11 (discretionary ranges); X12 = VN-01 X13 (undefined beneficiary), VN-02 V15; X27 ≈ VN-02 V14 (over-insurance forbidden and provided for); X4 ≈ VN-02 V5 (overload thresholds produce a non-monotone payout); X3 ≈ VN-01 X3 and X8 (two clocks for one act); X9 ≈ VN-01 X18 (flood add-on interacts badly with base exclusions); X23 ≈ VN-01 X14 (assessment cost allocation).

---

## VN-17 Tasco voluntary motor (Decision 168/2024)

Encoding: `contracts/insurance/vn-tasco-voluntary-motor-2024/encodings/legalese-2026-10-vn-17`.
Findings: `NOTES.md` §4 (X-01 to X-19, printed in the encoder's order of importance to a policyholder, kept here). No separate findings module: evidence is in `tasco-tests-*.l4`.

### VN-17 X-04 — Objective obstacle excuses the notice, not the penalty
- **Class**: T12 / T3
- **Scenario**: An objective obstacle keeps the owner from giving written notice within 5 days. Art. 5.2.7(c) excuses that; Art. 14.1.1(b) excuses only force majeure or a loss Tasco already assessed, so the collision pays 26,950,000 instead of 30,000,000. Art. 24.1.1(b) repeats it for goods.
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: LAW (F-30: Art 46.1, aid 917-927, excuses both and limits the cut to the insurer's loss; encoded "as written; flagged").
- **Evidence**: `tasco-tests-general.l4:111` (duty met); `tasco-tests-own-damage.l4:162` (`EQUALS 26950000`). src 402-405, 815-820, 1147-1153.
- **Plain-English test of surprise**: A customer excused from the notice duty expects no penalty; the penalty clause ignores the excuse.

### VN-17 X-19 — General exclusions defeat passengers and third parties
- **Class**: T2 / T13 (exclusion binds people who control none of it)
- **Scenario**: A passenger is killed in a collision; because the inspection certificate had expired, or the driver ran a red light, the passenger accident cover pays nothing. A third party's claim fails likewise where the driver had blood alcohol of 51.
- **Who bears it**: third party / beneficiary. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `tasco-tests-liability-and-accident.l4:232` (`accident not covered` … `10.4 no valid inspection certificate`), `:234` (`10.8 traffic offences`), `:226` (third party: `10.7 alcohol or drugs`). src 617-680, 1009, 1258.
- **Plain-English test of surprise**: A passenger's family expects accident cover to pay; the driver's paperwork defeats it.

### VN-17 X-07 — Exclusions apply with no causal link to loss
- **Class**: T2
- **Scenario**: A car parked where parking is prohibited burns from an electrical fault. The parking did not cause the fire, yet 10.8 (traffic offences) excludes it; the same fire in clean circumstances pays 30,000,000. Items 4-11 of Article 10 carry no causal words.
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `tasco-tests-own-damage.l4:332` (`own damage not covered` … `10.8 traffic offences`), `:333` (`EQUALS 30000000`). src 621-680.
- **Plain-English test of surprise**: A customer expects a parking ticket to be irrelevant to an electrical fire; it voids the claim.

### VN-17 X-17 — Parts-theft add-on on a short policy can never pay
- **Class**: T6 / T10
- **Scenario**: BS04 allows "0 vụ" (zero thefts) for a contract under 12 months. A buyer who adds BS04 to an 11-month policy pays its premium for no possible claim; a policy one day longer allows 2.
- **Who bears it**: policyholder. **Money direction**: against the claimant (premium).
- **Standing**: LITERAL (confirmed on PDF page 25).
- **Evidence**: `tasco-tests-own-damage.l4:257` (policy to 8 January 2026 `EQUALS 0`), `:256` (to 9 January `EQUALS 2`). src 1330-1333.
- **Plain-English test of surprise**: A customer who pays for an add-on expects it to be capable of paying; on a short policy it cannot.

### VN-17 X-13 — Stolen car awaits police; one-year bar keeps running
- **Class**: T1 / T10
- **Scenario**: A stolen car is a total loss only when the police conclude or suspend the investigation (15.2.1(b)); every claim is barred a year after the loss (9.1). An investigation running past a year leaves the owner arguing the wait was an "objective obstacle".
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: LITERAL (the time-bar is reading only).
- **Evidence**: `tasco-tests-own-damage.l4:142` (`#ASSERT REFUSED` … "a theft of the whole car is not a total loss until the investigation is concluded or suspended"). src 970-971, 598-601, 510-523.
- **Plain-English test of surprise**: A theft victim expects the deadline to wait for the police; it does not.

### VN-17 X-06 — Reduction bands leave the rate to Tasco
- **Class**: T11
- **Scenario**: The car was moved before Tasco consented, putting the loss in the "20% to 50%" band. With no rate recorded the claim is declined; at 30% it pays 20,850,000; at 60% it is declined as outside the band. The rules give no factor for choosing.
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `tasco-tests-own-damage.l4:172` (`REFUSED` … "Tasco has not determined a rate within the band of Article 14.1.2"), `:173` (`EQUALS 20850000`), `:175` (60%: outside the band). src 824, 842, 1157, 1175.
- **Plain-English test of surprise**: A customer expects a stated penalty; the insurer chooses anywhere from 20% to 50%, or from half to all.

### VN-17 X-03 — Undefined "business car" decides the depreciation rate
- **Class**: T5
- **Scenario**: "Xe kinh doanh" (business car) decides the depreciation column and is never defined: a car 1-3 years old is depreciated 0% if private and 10% if business. The same collision pays 30,000,000 for a private car and 28,500,000 for a business car.
- **Who bears it**: policyholder. **Money direction**: unclear.
- **Standing**: LITERAL.
- **Evidence**: `tasco-tests-own-damage.l4:166` (business car `EQUALS 28500000`; private 30,000,000 per NOTES). src 907, 932.
- **Plain-English test of surprise**: A customer who sometimes uses the car for work expects to know which column applies; the term is undefined.

### VN-17 X-15 — Excess-liability formula ignores what compulsory cover pays
- **Class**: T7 / T4
- **Scenario**: A third party dies; the owner, fully at fault, paid 200,000,000; the compulsory limit is 150,000,000. Art. 29's formula alone gives 100,000,000; Art. 28 confines the cover to the excess above the compulsory limit, 50,000,000. The encoding pays the lesser.
- **Who bears it**: insured. **Money direction**: against the claimant (relative to Art. 29 alone).
- **Standing**: CONTESTED (fork F-25 takes the lesser, flagged as favouring Tasco; "a reader of Art. 29 alone expects twice as much").
- **Evidence**: `tasco-tests-liability-and-accident.l4:214` (`EQUALS 50000000`). src 1222-1242.
- **Plain-English test of surprise**: An owner reading the payout formula expects 100m; the cover pays half.

### VN-17 X-16 — Table footnote cuts the death benefit
- **Class**: T7 / T6
- **Scenario**: Art. 20.1 pays the whole sum insured, 100,000,000, on death. The injury table's special case 6 pays only burial and identification costs (here 30,000,000) where the victim is unidentified or has no lawful heir. Art. 20 does not refer to it.
- **Who bears it**: beneficiary. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `tasco-tests-liability-and-accident.l4:74` (`EQUALS 100000000`), `:75` (no heir `EQUALS 30000000`). src 1023-1024, 4128-4130.
- **Plain-English test of surprise**: A reader of the death benefit expects the full sum; a footnote in an appendix reduces it.

### VN-17 X-12 — Termination refunds differ by who ends the contract
- **Class**: T7 / T6
- **Scenario**: With half a year left, Tasco's own termination refunds 6,000,000 (100% of pre-tax premium for the time left, with no insured-event exception). The policyholder's termination refunds 4,200,000 (70%), or nothing once an insured event has happened.
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `tasco-tests-general.l4:67` (`EQUALS 4200000`), `:70` (`EQUALS 6000000`). src 227-228, 269-276.
- **Plain-English test of surprise**: A customer expects the same refund whoever ends the contract; leaving costs 30%, or all of it after a claim.

### VN-17 X-05 — Claim bar runs from the loss, even for liability
- **Class**: T1 / T3
- **Scenario**: Art. 9.1 bars claims a year after the loss. A third party may claim against the owner more than a year after the accident (Chapters IV and V), by which time the owner's claim against Tasco is already barred.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LAW (F-10: Art 30, aid 706-717, counts from the third party's demand). Reading only.
- **Evidence**: No assertion for the finding (the date rule is tested in `tasco-tests-general.l4`). src 598-601.
- **Plain-English test of surprise**: An owner sued late by a victim expects the liability cover to respond; it may already be time-barred.

### VN-17 X-01 — No deadline for Tasco's own verification
- **Class**: T1 / T11
- **Scenario**: Where Tasco cannot verify, the file is complete only when the authority concludes. After 90 days Tasco must verify itself "và xem xét giải quyết bồi thường", with no period. The 15 or 30 days to pay run only from a complete file, so the clock can stop indefinitely.
- **Who bears it**: policyholder. **Money direction**: against the claimant (timing).
- **Standing**: LITERAL (reading only).
- **Evidence**: `tasco-tests-general.l4:102` (start: file received 1 July 2025 → `EQUALS YMD 2025 9 29`); nothing gives the end. src 304-312.
- **Plain-English test of surprise**: A customer expects an outside date for payment; there is none.

### VN-17 X-02 — Claim file is "one or more" documents Tasco chooses
- **Class**: T11 / T5
- **Scenario**: Art. 7 says the file "bao gồm một hoặc nhiều loại tài liệu sau" (comprises one or more of the following). With X-01, whether the file is complete, and so whether the payment period has begun, is Tasco's call.
- **Who bears it**: policyholder. **Money direction**: against the claimant (timing).
- **Standing**: LITERAL (reading only).
- **Evidence**: No assertion (`Article 7 — the documents the items name for` lists only what each item names). src 471-473.
- **Plain-English test of surprise**: A customer expects a checklist that, once complete, starts the clock; the insurer decides what is complete.

### VN-17 X-11 — Battery depreciation table stops at 15 years
- **Class**: T13 (missing table row) / T4
- **Scenario**: The traction-battery depreciation table's last row is "từ 10 năm đến dưới 15 năm"; the parts table runs on to "15 years or more". A battery 15 years old has no rate.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL.
- **Evidence**: `tasco-tests-own-damage.l4:108` (`#ASSERT REFUSED` … "no row for a traction battery 15 years old or more"). src 938.
- **Plain-English test of surprise**: A customer expects every age to have a rate; the oldest batteries have none.

### VN-17 X-14 — Recovered stolen car goes wholly to Tasco
- **Class**: T7 / T4
- **Scenario**: A car worth 800,000,000 is insured for 600,000,000. After an ordinary total loss Tasco takes 0.75 of the wreck (16.2.1); if the car was stolen and later found, Tasco takes the whole car (16.2.3), though it paid only the insured proportion.
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `tasco-tests-own-damage.l4:337` (`EQUALS 0.75`), `:338` (theft `EQUALS 1`). src 984-985, 991-992.
- **Plain-English test of surprise**: An under-insured owner expects to keep the uninsured share of a recovered car; the insurer takes it all.

### VN-17 X-08 — No overload measure for special-purpose vehicles
- **Class**: T13 (no rule for the case) / T5
- **Scenario**: Art. 10.10 measures overload by load for goods vehicles and persons for passenger cars; a special-purpose car of Art. 1.7.4, such as a crane truck carrying 12 tonnes, is neither, so the exclusion cannot be applied.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL.
- **Evidence**: `tasco-tests-general.l4:205` (`#ASSERT REFUSED` … "Article 10.10 names no basis for measuring the overload of a special-purpose car"). src 674-678.
- **Plain-English test of surprise**: An owner of a crane truck expects to know when it counts as overloaded; the clause does not say.

### VN-17 X-09 — Speeding reduction and exclusion overlap at 50%
- **Class**: T7 / T4
- **Scenario**: Art. 14.1.2(c) reduces for speeding "từ trên 20% đến 50%"; Art. 10.11 excludes "50% … trở lên". At 90 km/h in a 60 zone, exactly 50%, the loss is excluded and the reduction band can never apply at its top edge.
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: CONTESTED (fork F-21 takes the exclusion, flagged as favouring Tasco).
- **Evidence**: `tasco-tests-own-damage.l4:187` (`NOT covered:` at 90 in a 60 zone); `tasco-tests-general.l4:211` (`10.11 speeding by half or more`). src 834-835, 680.
- **Plain-English test of surprise**: A customer reading "reduced up to 50%" expects 50% to be reduced; it is excluded.

### VN-17 X-10 — Riot add-on BS12 adds nothing to base cover
- **Class**: T6
- **Scenario**: Art. 11.1.5 already covers malicious damage by anyone but the insured parties. BS12 covers vandalism in riots and excludes bombs, which the base cover (11.1.2, fire and explosion) does not. Riot damage pays 30,000,000 without BS12.
- **Who bears it**: policyholder. **Money direction**: against the claimant (premium).
- **Standing**: CONTESTED (rests on F-14 reading (a); "on a literal reading").
- **Evidence**: `tasco-tests-own-damage.l4:303` (no BS12 `EQUALS 30000000`), `:304` (BS12 also covers it). src 693-696, 1478-1486.
- **Plain-English test of surprise**: A customer buying riot cover expects to gain something; the base policy already pays.

### VN-17 X-18 — Injury table has three names; one points elsewhere
- **Class**: T5 / T7
- **Scenario**: Art. 20, the table's own title (PDF page 30) and special case 5 name the injury table three ways; special case 5 uses the name of the compulsory scheme's table, which Art. 29.1 uses for that other table. Read literally, special case 5 points at the wrong table.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL (reading only).
- **Evidence**: No assertion. src 1029, 4124-4125, 1229-1232; PDF p.30.
- **Plain-English test of surprise**: A reader expects a cross-reference to name the table in hand; this one names a different scheme's table.

#### VN-17 row summary
- Findings in §4: **19** (X-01 to X-19); 19 records.
- Most counterintuitive: X-19 (a passenger's death is unpaid because the driver ran a red light or the inspection certificate expired); X-17 (a parts-theft add-on bought on an 11-month policy allows zero claims); X-14 (an under-insured stolen car, when found, goes wholly to the insurer).
- Cross-row matches: X-07 = VN-01 X2, VN-02 V2, VN-15 X29 (no causal link); X-04 ≈ VN-01 X17 (late-notice cut ignores excuse, LAW Art 46.1) and VN-15 X3; X-01 + X-02 = VN-01 X6 + X7, VN-02 V8, VN-15 X20 (insurer controls when the payment clock starts, no long-stop); X-06 ≈ VN-01 X13, VN-02 V10/V11, VN-15 X14 (discretionary reduction bands); X-12 ≈ VN-01 X22, VN-02 V23, VN-15 X21/X25 (70% refund, nothing after an insured event); X-17 ≈ VN-15 X8 (parts-theft add-on on a contract under 12 months); X-09 ≈ VN-02 V5, VN-15 X4 (threshold edges at 50%); X-13 ≈ VN-15 X20 (theft payable only on a police decision with no time limit); X-05 ≈ VN-01 X11 (claim or limitation clock badly anchored); X-10 ≈ VN-01 X21 (a provision with nothing to do).

---

## VN-18 Tasco combined motor (Decision 53/2024)

Encoding: `contracts/insurance/vn-tasco-combined-motor-2024/encodings/legalese-2026-10-vn-18`.
Findings: `NOTES.md` "## Findings" (X1-X25; X12 withdrawn by the encoder). No separate findings module: evidence is in `tasco-tests-*.l4`.

### VN-18 X1 — Drink-driving exclusion covers only property damage
- **Class**: T7 / T13 (exclusion narrower than its apparent purpose)
- **Scenario**: Điều 11.4 begins "Thiệt hại đối với tài sản" (damage to property). A drunk driver killed in a crash is paid the full Chương III accident benefit, 100,000,000, while the same drunkenness excludes goods and physical-damage claims.
- **Who bears it**: insurer. **Money direction**: against the insurer.
- **Standing**: LITERAL (fork F16 reads the drug limb as governed by the same words).
- **Evidence**: `tasco-tests-ch3-5.l4:721` (`a drunk driver killed` → `payable 100_000_000`); contrast `:747` (goods: `excluded` `art 11.4`). src:640-644.
- **Plain-English test of surprise**: An insurer expects a drink-driving exclusion to reach the driver's own death benefit; it does not.

### VN-18 X2 — "Chủ xe" defined two different ways
- **Class**: T5 / T7
- **Scenario**: The opening paragraph calls the buyer "chủ xe"; definition 5 defines "Chủ xe" as the owner or lawful possessor. Refunds go to "chủ xe" while premiums are paid by the buyer, so who receives a refund is unclear when they differ.
- **Who bears it**: policyholder. **Money direction**: unclear.
- **Standing**: LITERAL (reading only).
- **Evidence**: No assertion. src:48, 67-69, 197, 202.
- **Plain-English test of surprise**: A buyer who is not the registered owner expects the refund back; the wording may send it to the owner.

### VN-18 X3 — "Loss" defined as sudden, yet wear excluded as loss
- **Class**: T5 / T7
- **Scenario**: Definition 18 makes "tổn thất" (loss) sudden damage; Điều 15.1 then excludes wear and tear as a "tổn thất", which by definition it cannot be.
- **Who bears it**: unclear. **Money direction**: no money.
- **Standing**: LITERAL (reading only).
- **Evidence**: No assertion. src:132-133, 779.
- **Plain-English test of surprise**: A reader expects defined terms to be used consistently; the exclusion contradicts the definition.

### VN-18 X4 — Definition of traffic accident is circular
- **Class**: T5
- **Scenario**: Definition 19 says "Tai nạn giao thông gồm: Va chạm giao thông và tai nạn giao thông" (a traffic accident comprises a traffic collision and a traffic accident).
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL (reading only).
- **Evidence**: No assertion. src:140-141.
- **Plain-English test of surprise**: A reader expects a definition to define; this one repeats its own term.

### VN-18 X5 — Insurer's termination refunds premium even after a claim
- **Class**: T7
- **Scenario**: Điều 3.1 and the second paragraph of 3.2 refund nothing once an insured event has happened; 3.2's third paragraph, for Tasco's own termination, has no such exception. A 3,650,000 premium contract ended by Tasco on 2 July refunds 1,830,000 regardless of claims.
- **Who bears it**: insurer. **Money direction**: against the insurer.
- **Standing**: LITERAL.
- **Evidence**: `tasco-tests-ch1.l4:1040` (`art 3.2 — the refund when Tasco terminates …` `EQUALS 1_830_000`; the rule takes no insured-event fact). src:201-203.
- **Plain-English test of surprise**: One expects the same claims rule whoever terminates; only the policyholder loses the refund after a claim.

### VN-18 X6 — Two transfer-of-ownership clauses conflict, leaving a gap
- **Class**: T7 / T1
- **Scenario**: A car is sold; notice is late but the old owner agreed to pass the contract on, triggering both 6.1 and 6.2. Taking 6.2, the contract ends at the transfer, so a loss in the gap is unpaid though the new owner was to be covered "from the transfer".
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: CONTESTED (fork F10 takes 6.2; "LAW: Art 24 … points to 6.1").
- **Evidence**: `tasco-tests-ch1.l4:1060` (`EQUALS it ends at the moment of the transfer`). src:423-429.
- **Plain-English test of surprise**: A buyer promised cover from purchase expects it; the contract ends then instead.

### VN-18 X7 — Transfer clause silent in the ordinary case
- **Class**: T13 (no rule for the case) / T5
- **Scenario**: Notice of the sale was in time, and the old owner neither passed the contract on nor asked to end it. Điều 6 says nothing about what then happens to the contract.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL.
- **Evidence**: `tasco-tests-ch1.l4:1062` (`#ASSERT REFUSED art 6 — what the transfer does … FALSE FALSE`). src:423-429 (inferred from X6).
- **Plain-English test of surprise**: A seller expects the policy to say whether the insurance ends or continues; it does not.

### VN-18 X8 — Reduction points at a clause with no duty
- **Class**: T7 / T5
- **Scenario**: Điều 4.1.6 reduces compensation for breaches of "khoản 2, Điều 6", but Điều 6 is the transfer of ownership and its point 2 sets no duty; the duties are in Điều 5, point 2.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL (reading only).
- **Evidence**: No assertion. src:257-258.
- **Plain-English test of surprise**: A reader expects a penalty to point at the duty it punishes; this one points at nothing.

### VN-18 X9 — Claim-file cross-reference points to the wrong article
- **Class**: T7
- **Scenario**: Điều 4.2.6 refers to "Điều 7" for the claim file; the claim file is Điều 8.
- **Who bears it**: unclear. **Money direction**: no money.
- **Standing**: LITERAL (reading only).
- **Evidence**: No assertion. src:330-331.
- **Plain-English test of surprise**: A claimant following the reference finds the wrong article.

### VN-18 X10 — Claim file is whatever Tasco asks for
- **Class**: T11 / T5
- **Scenario**: Điều 8 says the file is "một hoặc nhiều loại tài liệu sau" (one or more of the following), and the payment clock of 4.2.3 runs only from a complete file. The claimant cannot tell when the file is complete; for a plain collision the file may contain 11 documents, none marked required.
- **Who bears it**: policyholder. **Money direction**: against the claimant (timing).
- **Standing**: LITERAL (reading only).
- **Evidence**: `tasco-tests-ch1.l4:1095` (`count (art 8 — the documents the claim file may contain …) EQUALS 11`). src:470, 277-278.
- **Plain-English test of surprise**: A customer expects a checklist whose completion starts the payment clock; the insurer decides.

### VN-18 X11 — Complaint on time under 10.2, barred under 10.1
- **Class**: T1 / T7
- **Scenario**: Event 1 June 2024; Tasco's decision received 1 July 2025; complaint 1 August 2025. It is within 10.2's 90 days of the decision, yet after 10.1's one year from the event, which voids "mọi khiếu nại" (every complaint).
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: LITERAL (fork F15 notes LAW Art 30.2-30.3 counts from knowledge or a third party's demand; not encoded).
- **Evidence**: `tasco-tests-ch1.l4:1215` (in time under 10.2), `:1216` (`NOT art 10.1 — still in time …`). src:596-598, 600-602.
- **Plain-English test of surprise**: A customer given 90 days to challenge a decision expects them; a slow decision has already used them up.

### VN-18 X13 — Tasco's three-day deadline has no consequence
- **Class**: T1 / T12
- **Scenario**: Điều 13.1.2(a) gives Tasco at most 3 working days to give its opinion on dismantling, and says nothing of what follows if it is late. An owner who dismantles after Tasco's deadline passes still faces the 20%-50% reduction; Tasco chose 20%.
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `tasco-tests-ch1.l4:1219` (`dismantled after Tasco's opinion was overdue, Tasco chose 20%` … `EQUALS 20%`). src:699-700.
- **Plain-English test of surprise**: A customer who waits out the insurer's deadline expects to be free to proceed; the penalty still applies.

### VN-18 X14 — Two exclusions printed under one number
- **Class**: T7
- **Scenario**: Điều 11.1 prints the intentional-act exclusion and the inspection-certificate exclusion together under "1.".
- **Who bears it**: unclear. **Money direction**: no money.
- **Standing**: LITERAL (reading only).
- **Evidence**: No assertion. src:614-623 (page 10).
- **Plain-English test of surprise**: A reader citing "exclusion 1" expects one rule; there are two.

### VN-18 X15 — Reductions up to 100% at Tasco's discretion
- **Class**: T11
- **Scenario**: Điều 13.1.2 and 13.1.3 reduce by 20%-50% and 50%-100% "tùy theo mức độ lỗi" (according to degree of fault) with no criteria; 13.1.3(b) reaches any untruthful document. A car repaired without consent cannot be priced until Tasco picks a rate.
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `tasco-tests-ch1.l4:1189` (`#ASSERT REFUSED art 13.2 — the rate applied … repaired without consent, no rate chosen …`). src:693, 705.
- **Plain-English test of surprise**: A customer expects the penalty for a breach to be stated; it can be anything up to the whole claim.

### VN-18 X16 — Total-loss threshold differs at exactly 75%
- **Class**: T7
- **Scenario**: Điều 18.2.1 says "trên 75%" (over) for damage and "bằng hoặc trên 75%" (75% or more) for repair cost. Repairs of 337,500,000 on a car worth 450,000,000 are a total loss by repair cost but not damage "more than 75%"; 337,000,000 is neither.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL.
- **Evidence**: `tasco-tests-ch2.l4:647` (total loss), `:648` (`NOT … more than 75%`), `:649` (337m: `NOT` a total loss). src:931-934.
- **Plain-English test of surprise**: One expects one write-off threshold; the two limbs disagree at the edge.

### VN-18 X17 — No benefit for permanent partial disability
- **Class**: T13 (benefit gap) / T6
- **Scenario**: Điều 24 pays for death or permanent total disability (24.1) and temporary injury (24.2). A passenger who is permanently but partially disabled falls between the two and has no benefit.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `tasco-tests-ch3-5.l4:708` (`#ASSERT REFUSED` … "art 24 names death, permanent total disability and temporary injury, and not permanent partial disability"). src:1002-1008.
- **Plain-English test of surprise**: A passenger who loses a hand expects accident cover to pay; the benefit list skips that case.

### VN-18 X18 — Theft exception for goods grants nothing
- **Class**: T6
- **Scenario**: Điều 27.2 excludes theft of goods "trừ trường hợp toàn bộ xe và hàng hóa cùng bị mất cắp" (except where the whole vehicle and goods are stolen together), but theft is not a peril of Điều 26. Goods stolen with the whole lorry are outside the cover.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `tasco-tests-ch3-5.l4:738` (`goods stolen with the whole lorry` → `outside the cover` "art 26: the loss to the goods was not caused by a peril it names"). src:1022-1024, 1042.
- **Plain-English test of surprise**: A carrier reading the exception expects goods stolen with the lorry to be covered; they are not.

### VN-18 X19 — Excess-liability formula and layer rule disagree
- **Class**: T7 / T4
- **Scenario**: A pedestrian is killed; the owner, 60% at fault, paid 100,000,000 against a (hypothetical) compulsory limit of 150,000,000. Điều 34.1's formula alone gives 60,000,000; Điều 32 pays only the part above the compulsory limit, so the combined reading pays 0.
- **Who bears it**: insured. **Money direction**: against the claimant (relative to 34.1 alone).
- **Standing**: CONTESTED (fork F31 takes the lesser of the two).
- **Evidence**: `tasco-tests-ch3-5.l4:758` (`payable 0`), `:760` (`art 34.1` alone `EQUALS 60_000_000`). src:1095-1099, 1133.
- **Plain-English test of surprise**: An owner reading the payout formula expects 60m; the cover pays nothing.

### VN-18 X20 — Add-on clauses point to other rule books
- **Class**: T7 / T8
- **Scenario**: Chương VI's clauses say they are "quy định trong Quy tắc bảo hiểm vật chất xe ô tô"; BS14 follows "Quy tắc bảo hiểm tự nguyện xe ôtô"; BS15 "quy tắc bảo hiểm xe cơ giới". None is this document by its own title. The encoding reads them as Chương II.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL (reading only; "Read as Chương II").
- **Evidence**: No assertion. src:1155-1157, 1378, 1409.
- **Plain-English test of surprise**: A customer expects add-ons to modify the policy bought; they cite other rule books.

### VN-18 X21 — Flood add-on does not cover an electric car's motor
- **Class**: T6 / T2
- **Scenario**: Điều 15.2 excludes both water hammer and damage to an electric car's electric motor in flood water. BS03 buys back only "hiện tượng thủy kích" (water hammer), so an electric car's flooded motor stays excluded with BS03.
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `tasco-tests-ch6-claims.l4:1077` (`NOT BS03 — buys back the flood-water exclusion` … `a flooded electric motor`), `:1197` (`excluded` `art 15.2 engine damage in flood water`). src:784-785, 1190-1192.
- **Plain-English test of surprise**: An electric-car owner buying flood cover expects the motor protected; it is not.

### VN-18 X22 — Parts-theft add-on sets no limit under 12 months
- **Class**: T13 (no rule for the case) / T10
- **Scenario**: BS04 allows 2 thefts for 12-18 months and 3 above 18, and states nothing for a contract under 12 months, such as an 11-month contract.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL.
- **Evidence**: `tasco-tests-ch6-claims.l4:1082` (`#ASSERT REFUSED` … "BS04 sets no limit on the number of thefts for a contract of under 12 months"). src:1208-1209.
- **Plain-English test of surprise**: A customer on a short policy expects to know how many thefts are covered; it is unsaid.

### VN-18 X23 — Machinery add-on qualifies eight sites, pays at five
- **Class**: T7 / T6
- **Scenario**: BS09 lets a vehicle hold the clause if it works at airports, industrial zones, mining areas and five other kinds of site, but the benefit names only five. A forklift at an airport may hold the clause, yet a loss there is not at a site the benefit names.
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `tasco-tests-ch6-claims.l4:1111` (may hold the clause), `:1112` (`NOT BS09 — the loss is at a site the benefit names`). src:1300-1302, 1305-1307.
- **Plain-English test of surprise**: An airport operator sold the add-on expects cover at the airport; the benefit omits it.

### VN-18 X24 — Battery add-on adds a deductible 42 times larger
- **Class**: T6 / T4
- **Scenario**: Chương II already pays a traction battery. On a 37-month electric car with a 300,000,000 battery, Chương II pays 226,500,000 for battery and bumper after a 500,000 deductible; BS15 computed alone pays 189,000,000 for the battery after a 21,000,000 deductible. How the two combine is unsaid.
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: CONTESTED (fork F35: BS15 computed alone; the combination is unsaid).
- **Evidence**: `tasco-tests-ch6-claims.l4:1149` (without BS15 `payable 226_500_000`), `:1142` (BS15 `payable 189_000_000`). src:875, 1410.
- **Plain-English test of surprise**: A customer buying battery cover expects better battery cover; the add-on brings a much larger deductible.

### VN-18 X25 — Liability exclusion for inspection stricter than damage exclusion
- **Class**: T7 / T2
- **Scenario**: Điều 33.3 repeats Điều 11.1's inspection-certificate exclusion without its three spared causes. A certificate lapsed only by fitting a roof rack excludes a third-party claim but not a physical-damage claim.
- **Who bears it**: insured / third party. **Money direction**: against the claimant.
- **Standing**: LITERAL (fork F33).
- **Evidence**: `tasco-tests-ch3-5.l4:768` (`excluded` `art 33.3 no valid inspection certificate`); `tasco-tests-ch1.l4:1130` (`NOT art 11.1 …` for the same certificate). src:1110-1112.
- **Plain-English test of surprise**: An owner expects one roof rack to be judged the same way across one policy; liability cover is lost while damage cover is not.

#### VN-18 row summary
- Findings in "## Findings": **24** (X1-X25 with X12 withdrawn by the encoder: "rested on assumptions about criminal procedure outside the sources"); 24 records.
- Most counterintuitive: X19 (the excess-liability formula promises 60m and the layer rule pays 0); X1 (a drunk driver's death is paid in full while the same drunkenness voids property claims); X24 (a battery add-on cuts the battery payout by charging a 21m deductible against the base cover's 0.5m).
- Cross-row matches: X19 = VN-17 X-15 (same insurer, excess layer vs formula); X5 ≈ VN-17 X-12 (insurer's own termination refunds without the insured-event exception); X22 = VN-15 X8 and ≈ VN-17 X-17 (parts-theft add-on on a contract under 12 months: VN-15 and VN-18 set no limit, VN-17 sets zero); X16 = VN-15 X18 (75% "over" vs "equal or over"); X10 = VN-17 X-02, VN-01 X6, VN-15 X20 (open-ended claim file); X15 ≈ VN-17 X-06, VN-15 X14, VN-02 V10/V11, VN-01 X13 (discretionary reduction bands); X11 ≈ VN-01 X11, VN-17 X-05 (claim and complaint clocks); X21 ≈ VN-15 X9, VN-01 X18 (flood add-on narrower than it looks); X18 ≈ VN-01 X21, VN-02 V21 (a provision that does nothing); X6 ≈ VN-15 X13 (contradictory ownership-transfer clause); X13 ≈ VN-15 X17 (insurer silence vs reduction for acting without consent); X25 ≈ VN-17 X-19 (inspection exclusions reaching liability claims); X2 ≈ VN-02 V15 (who is the owner or payee shifts).

---

## VN-10 Decree 67/2023/NĐ-CP, compulsory motor third-party liability insurance (legislation)

Encoding: `vn/decree-67-2023/encodings/legalese-2026-10-vn-10`.
Findings: `NOTES.md` §4 (R1-R16). Findings module: `nd67-findings.l4`; further evidence in `nd67-tests.l4`.
Roles here: the vehicle owner (the insured), the third party or passenger (the victim), the insurer.

### VN-10 R1 — Rider who is not a "passenger" falls between both covers
- **Class**: T5 / T13 (cover gap between two categories)
- **Scenario**: Art 3(5)(a) excludes everyone on the vehicle from "third parties"; Art 7(1)(b) covers only undefined "hành khách" (passengers). A family member killed riding pillion, if not a "passenger", receives nothing, under both vintages.
- **Who bears it**: third party. **Money direction**: against the claimant.
- **Standing**: CONTESTED (rests on F25; reading (i), anyone carried, closes the gap).
- **Evidence**: `nd67-findings.l4:89-90` (both vintages: `outside the scope: the person is neither a third party nor a passenger`). src 86-87, 202.
- **Plain-English test of surprise**: A family expects compulsory insurance to cover a pillion rider's death; the rider may be neither third party nor passenger.

### VN-10 R2 — Parked car with nobody at controls is uninsured
- **Class**: T13 (cover gap) / T5
- **Scenario**: A parked car's handbrake fails and it rolls into a pedestrian. Art 3(2) requires "sự điều khiển" (someone in control) and Art 3(3) driving in road traffic, so the damage is outside the cover; with its driver at the wheel it is covered.
- **Who bears it**: third party. **Money direction**: against the claimant.
- **Standing**: LITERAL (fork F4: "under control" governs moving, stopping and parking).
- **Evidence**: `nd67-findings.l4:97` (`outside the scope: the vehicle was neither in road traffic nor operating`); `nd67-tests.l4:248` (driver at the wheel: covered). src 78-81.
- **Plain-English test of surprise**: A pedestrian hit by a runaway parked car expects compulsory insurance to pay; it does not.

### VN-10 R3 — Licence exclusion literally voids cover for licence-free vehicles
- **Class**: T6 / T5
- **Scenario**: An electric moped needing no licence, ridden by its unlicensed owner, injures a pedestrian. On the grammatical (last-antecedent) reading of Art 7(2)(c) the cover is excluded, making cover for every licence-free vehicle illusory; on the reading encoded it is not.
- **Who bears it**: third party / insured. **Money direction**: against the claimant (on the literal reading).
- **Standing**: CONTESTED (fork F5 takes reading (ii); the encoder calls (i) "the grammatical reading").
- **Evidence**: `nd67-findings.l4:104` (`NOT … excludes the cover`, encoded reading), `:105` (last-antecedent reading excludes). src 215-222.
- **Plain-English test of surprise**: An owner of a licence-free vehicle expects it to be insurable; the literal wording excludes every unlicensed rider.

### VN-10 R4 — Third party's fault halves an innocent victim's award
- **Class**: T5 / T4
- **Scenario**: A cyclist swerves and wholly causes an accident; a pedestrian is killed. Art 12(6)(a) halves compensation to "third parties" where the accident was entirely "a third party's" fault, whoever was at fault: the pedestrian's family receives 75,000,000 instead of 150,000,000; the car's passenger killed in the same accident receives 150,000,000.
- **Who bears it**: third party. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `nd67-findings.l4:113` (pedestrian `EQUALS RIGHT 75000000`), `:114` (passenger `EQUALS RIGHT 150000000`). src 365-373.
- **Plain-English test of surprise**: One expects the halving to punish a victim at fault; it halves an innocent pedestrian because someone else was at fault.

### VN-10 R5 — A 16-seat vehicle's premium exceeds a 17-seat one's
- **Class**: T4 / T7
- **Scenario**: Annex I section V charges a 16-seat business vehicle 3,054,000 and a 17-seat one 2,718,000, though every other step rises. The gazette PDF (page 65) prints the same figures.
- **Who bears it**: policyholder. **Money direction**: against the claimant (premium).
- **Standing**: LITERAL.
- **Evidence**: `nd67-findings.l4:122` (16 `GREATER THAN` 17), `:123` (15 `LESS THAN` 16). src 2081-2082.
- **Plain-English test of surprise**: An operator expects a larger vehicle to cost more to insure; the 16-seater costs more than the 17-seater.

### VN-10 R6 — Injury bands are money ranges with no picker
- **Class**: T11 / T5
- **Scenario**: 650 of Annex VI's rows give a band; 589 of them span 4 points, 6,000,000 on the 150,000,000 limit. Art 12(6)(a) names no assessor or criterion. Injury B.I 1.1 pays anything from 9,000,000 to 15,000,000.
- **Who bears it**: third party. **Money direction**: unclear.
- **Standing**: LITERAL.
- **Evidence**: `nd67-findings.l4:129` (`EQUALS RIGHT (A payment band OF 9000000, 15000000)`); `nd67-tests.l4:433` (`#ASSERT REFUSED` with no assessed rate). src 350-361.
- **Plain-English test of surprise**: A victim expects the table to fix the payment; it gives a range and no one is named to choose.

### VN-10 R7 — "Cộng lùi" undefined; two ways to combine injuries
- **Class**: T5 / T7
- **Scenario**: "Cộng lùi" (a method of adding injury rates) appears on 28 lines of Annex VI and is never defined. Special case 4 adds several injuries' payments plainly, capped at the limit, so two combination methods coexist with no rule for which governs.
- **Who bears it**: third party. **Money direction**: unclear.
- **Standing**: LITERAL (reading only).
- **Evidence**: `nd67-tests.l4:447` (a row whose addition applies: `#ASSERT REFUSED`). src (Decree 1019-1020 lines) 2086-2088, 2103-2104, 1774-1776, 2185-2187.
- **Plain-English test of surprise**: A victim with several injuries expects one rule for totalling them; there are two, one undefined.

### VN-10 R8 — Injury table has gaps and overlaps at boundaries
- **Class**: T7 / T13 (boundary gaps and overlaps)
- **Scenario**: A victim aged exactly 50 is in neither "over 50" nor "under 50"; a limb shortened by exactly 3, 4 or 5 cm fits no row; 8 lost teeth fit both "2 to 8" and "8 to 19"; a boy fits two rows; two stiff joints pay more than three.
- **Who bears it**: third party. **Money direction**: unclear.
- **Standing**: LITERAL (reading only; the 8-teeth overlap checked on gazette page 63).
- **Evidence**: No assertion. src 1222-1223, 1525-1527, 1540-1541, 1321-1322, 1582-1583, 2040, 2043, 1311, 1314, 1729-1731, 1561-1562.
- **Plain-English test of surprise**: A victim expects each injury to fit one row; some fit none, some two.

### VN-10 R9 — Seller sent to an article with no refund rule
- **Class**: T13 (no rule for the case) / T7
- **Scenario**: The vehicle is sold mid-term and the seller terminates. Art 9(3) points to Art 11, which covers only revocation of registration certificate and plates, so the decree states no refund.
- **Who bears it**: policyholder. **Money direction**: unclear.
- **Standing**: LITERAL.
- **Evidence**: `nd67-findings.l4:133` (`#ASSERT REFUSED` … "Article 11 states no refund for a termination on a change of owner"). src 257-259, 285-291.
- **Plain-English test of surprise**: A seller expects the unused premium back; the cross-reference leads nowhere.

### VN-10 R10 — Fund need not repay advances the insurer may claim
- **Class**: T7
- **Scenario**: Art 12(3) lets the insurer ask the Fund to repay any advance; Art 17(1)(a) binds the Fund to repay only advances under point (b). An advance under point (a) for an accident later found excluded gives a right to ask with no duty to pay.
- **Who bears it**: insurer. **Money direction**: against the insurer (inferred).
- **Standing**: LITERAL (reading only; Article 17 is out of scope).
- **Evidence**: No assertion. src 331-334, 503-507.
- **Plain-English test of surprise**: An insurer making a mandated advance expects to recover it if the accident proves excluded; the Fund need not pay.

### VN-10 R11 — Short-term premium cites the wrong rule-maker
- **Class**: T7 / T5
- **Scenario**: Annex I section B prices a short term on the premium "do Bộ Tài chính quy định" (set by the Ministry of Finance), though Annex I is set by this Government decree. The encoding applies section B to the Annex I premium.
- **Who bears it**: unclear. **Money direction**: no money.
- **Standing**: LITERAL (reading only).
- **Evidence**: No assertion. src 2130-2132.
- **Plain-English test of surprise**: A reader expects the premium source to be this annex; the text names another authority.

### VN-10 R12 — Premium and compensation adjustments: ceilings without criteria
- **Class**: T11 / T7
- **Scenario**: Art 8(2) lets the insurer raise or lower the premium by up to 15% on claims history: an annual 437,000 can become 371,450 or 502,550 on the same facts. Art 12(7) lets it cut property compensation up to 5%. Neither says how much, and a 15% reduction sits uneasily with Art 75(1)'s ban on discounts "in any form".
- **Who bears it**: policyholder. **Money direction**: unclear.
- **Standing**: LITERAL.
- **Evidence**: `nd67-findings.l4:139` (`EQUALS RIGHT 371450`), `:140` (`EQUALS RIGHT 502550`). src 235-238, 379-385, 1909-1910.
- **Plain-English test of surprise**: An owner expects compulsory premiums to be fixed by law; the insurer may move them 15% either way at will.

### VN-10 R13 — No deadline to pay compensation, no time-bar
- **Class**: T1
- **Scenario**: Art 12(11) requires the insurer to notify and pay compensation with no period, and Art 13 sets no claims deadline.
- **Who bears it**: third party. **Money direction**: against the claimant (timing).
- **Standing**: LITERAL (reading only; LAW L1, Art 31(1), 15 days, and L2, Art 30(1), 1 year, fill both silences).
- **Evidence**: No assertion. src 397-400.
- **Plain-English test of surprise**: A victim expects a compulsory scheme to say when it pays; the decree does not.

### VN-10 R14 — Special case halves what the table's own row pays
- **Class**: T7 / T4
- **Scenario**: Special case 1 pays ankylosis of finger joints (not thumb or index) at 50% of losing the finger: for the middle finger, 4-5%. The table's own stiffness row for those joints, B.VI 4.5.3.3, pays 7-9% (10,500,000 to 13,500,000).
- **Who bears it**: third party. **Money direction**: against the claimant (if special case 1 governs).
- **Standing**: CONTESTED (whether "dính khớp" and "cứng khớp" are the same condition "is the open question").
- **Evidence**: `nd67-findings.l4:147` (`EQUALS RIGHT (A payment band OF 10500000, 13500000)`), `:148` (special case 1 `EQUALS RIGHT 5`). src 2178-2180, 1448, 1451.
- **Plain-English test of surprise**: A victim expects a special rule to clarify the table, not halve it.

### VN-10 R15 — Short-term premium arithmetic overcharges short and leap terms
- **Class**: T4
- **Scenario**: Section B charges a 1-day contract a twelfth of the annual premium, the same as a 30-day one. A two-year term spanning 29 February costs 731/365 of a year: 875,197.26 against 874,000 for two years at 437,000.
- **Who bears it**: policyholder. **Money direction**: against the claimant (premium).
- **Standing**: LITERAL.
- **Evidence**: `nd67-findings.l4:155` (1 day `EQUALS` 30 days), `:156` (731 days `GREATER THAN 874000`). src 2138-2139.
- **Plain-English test of surprise**: An owner expects a one-day policy to cost a day's premium and two years to cost two years'; neither holds.

### VN-10 R16 — Injury rates vary by sex, age, marriage, occupation
- **Class**: T13 (outcome varies with personal status)
- **Scenario**: A note in Annex VI gives women the top of the band and men the bottom: for B.I 6.3.7 a woman is paid 9%, a man 5%. Another note adds 5-10% for unmarried young men and women; others add for singers, teachers and perfumers.
- **Who bears it**: third party. **Money direction**: unclear.
- **Standing**: LITERAL (sex note encoded and tested; the rest reading only).
- **Evidence**: `nd67-tests.l4:444` (female `EQUALS RIGHT 9`), `:445` (male `EQUALS RIGHT 5`). src 763, 1816-1818, 2123-2124, 2169-2171.
- **Plain-English test of surprise**: A victim expects the same injury to pay the same; it pays differently by sex, marriage and job.

#### VN-10 row summary
- Findings in §4: **16** (R1-R16); 16 records.
- Most counterintuitive: R4 (a pedestrian gets half because a different third party caused the accident, while a passenger in the same crash gets full); R2 (a runaway parked car's victim is outside compulsory cover); R5 (the 16-seat premium exceeds the 17-seat premium).
- Cross-row matches: R13 ≈ VN-01 X7, VN-02 V8, VN-15 X20, VN-17 X-01 (no outside date for paying); R6 and R12 ≈ VN-01 X13, VN-15 X14, VN-17 X-06, VN-18 X15 (discretion with a ceiling and no criterion); R8 ≈ VN-02 V5, VN-15 X18, VN-17 X-09, VN-18 X16 (threshold edges in or out of both rows); R9 ≈ VN-18 X7 (silence on what happens at a change of owner); R7 and R6 ≈ VN-17 X-18 (the voluntary policies borrow this decree's injury table, and VN-17 notes the cross-reference to it is confused).

---
