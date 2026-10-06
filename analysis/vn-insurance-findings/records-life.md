# Policy defect records: life, unit-linked and critical illness rows (VN-11, 13, 14, 24, 25, 26)

Extracted read-only from each row's `NOTES.md` section 4 and its findings module.
Class codes are the team lead's T1 to T13; "T13 silent consequence" is used where the document states a condition or event but not what follows, so the encoder had to refuse.
Line numbers in "Evidence" are the line of the `#ASSERT` in the named module at the time of reading (2026-10-07).

## VN-11 Manulife term life

### VN-11 1 — Crime exclusion names no criminal, so murder is excluded
- **Class**: T2 / T5
- **Scenario**: Any death resulting "directly or indirectly" from "Phạm tội" is excluded, with no offender named. On the literal reading an insured killed in a robbery on 10 May 2023 gets nothing; on the reading taken (the insured's own crime) the benefit is paid.
- **Who bears it**: beneficiary. **Money direction**: against the claimant.
- **Standing**: CONTESTED (fork F6 takes the insured's own crime; the Law points the same way "but only if it governs").
- **Evidence**: `vn11-findings.l4:33` (taken: NOT excluded) and `:34` (literal: excluded); src:132-137.
- **Plain-English test of surprise**: A family expects a murdered insured to be covered; the words exclude it.

### VN-11 2 — Crime exclusion reaches crimes of negligence too
- **Class**: T2
- **Scenario**: Only the second limb says "cố tình" (intentionally); the first, "Phạm tội", has no intent requirement and swallows the second. An insured who dies in a crash the insured caused, if that is a crime, is excluded: the family gets 19 million in refunded premium instead of 1 billion.
- **Who bears it**: beneficiary. **Money direction**: against the claimant.
- **Standing**: LITERAL. Whether careless driving is a crime is outside the document.
- **Evidence**: `vn11-findings.l4:42`, outcome EQUALS `no death benefit, and the premium is refunded` "Art 3(c)" 19_000_000; src:137.
- **Plain-English test of surprise**: A customer reads a crime exclusion as aimed at deliberate wrongdoing; the wording also catches a careless accident.

### VN-11 3 — Only a dead policyholder can extend the claim year
- **Class**: T1 / T3
- **Scenario**: The one-year claim period extends only where "Bên mua bảo hiểm chứng minh" (the policyholder proves) ignorance. When the insured is also the policyholder, that person is dead; a beneficiary who learns of the death 19 months later is out of time.
- **Who bears it**: beneficiary. **Money direction**: against the claimant.
- **Standing**: LAW. Law Art 30(2) gives the discovery rule to the beneficiary (fork L3).
- **Evidence**: `vn11-findings.l4:54`, EQUALS `the claim for the death benefit is out of time`; src:364-375.
- **Plain-English test of surprise**: A beneficiary unaware of the death expects the clock to wait; only the deceased could stop it.

### VN-11 4 — Suicide and contest years run from undefined issue date
- **Class**: T1 / T5
- **Scenario**: Both two-year periods count from "ngày cấp Hợp đồng bảo hiểm" (the issue date), undefined and distinct from the effective date. Effective 15 Jan 2020, issued 1 Feb 2020: a suicide on 20 Jan 2020 pays 1 billion; one on 1 Feb 2022, two years and 17 days into cover, is excluded (19 million refunded).
- **Who bears it**: unclear (cuts both ways). **Money direction**: unclear.
- **Standing**: LITERAL (fork F3); LAW as to suicide, which the Law counts from the first premium (L2).
- **Evidence**: `vn11-findings.l4:61-62`; src:271-272, 278-280.
- **Plain-English test of surprise**: A customer expects "two years" to mean two years of cover; it starts from another date.

### VN-11 5 — Avoidance for non-disclosure with no stated refund
- **Class**: T13 silent consequence
- **Scenario**: The Company "có quyền xem Hợp đồng bảo hiểm là vô hiệu" (may treat the contract as void), but the document never says whether premiums are returned in full, less costs, or not at all. The encoding refuses to answer.
- **Who bears it**: policyholder. **Money direction**: unclear.
- **Standing**: LITERAL (the document is silent); the encoder notes the Law has answers (fork L9, Law Arts 22(2), 25(2)).
- **Evidence**: `vn11-findings.l4:66`, `#ASSERT REFUSED … the premium returned when the Company treats the contract as void`; src:257-267.
- **Plain-English test of surprise**: A policyholder whose contract is cancelled for non-disclosure expects to know what comes back; the document says nothing.

### VN-11 6 — No beneficiary named, no payee for the benefit
- **Class**: T13 silent consequence
- **Scenario**: Art 8 says how to split among beneficiaries but not who is paid when none was designated or all have died, nor who receives any refund (fork F23). The encoding refuses.
- **Who bears it**: beneficiary (the insured's estate, inferred). **Money direction**: unclear.
- **Standing**: LITERAL.
- **Evidence**: `vn11-findings.l4:70`, `#ASSERT REFUSED … no beneficiary designated`; also `vn11-tests.l4:521-523` (partial or short shares refused); src:215-227.
- **Plain-English test of surprise**: A customer expects a default payee such as the estate; the wording names none.

### VN-11 7 — Company approvals and costs with no criteria
- **Class**: T11 / T5
- **Scenario**: "Reasonable costs" deducted from every refund are undefined; Company approval of a beneficiary change, assignment and reinstatement ("tùy theo sự xem xét của Công ty") has no standard; reinstatement interest is set by the Company, capped only by the State Bank maximum; "có tầm quan trọng" (material) has no test.
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: LITERAL (reading only; each is an input recording the Company's decision).
- **Evidence**: no assertion (reading only); src:172-173, 230-231, 260, 301, 307-311, 329.
- **Plain-English test of surprise**: A customer expects deductions and approvals to follow stated rules; the wording leaves them to the insurer.

### VN-11 8 — Misstated Age undoes cover after any length of time
- **Class**: T7 / T1
- **Scenario**: Art 10 limits contesting non-disclosure to two years, but Art 9 on misstated Age has no limit. With a true issue Age of 61 (outside 0-60), an insured dying in 2035, fifteen years on, yields only a 19 million premium refund, no death benefit.
- **Who bears it**: beneficiary. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `vn11-findings.l4:77`, outcome EQUALS `no death benefit, and the premium is refunded` "Art 9" 19_000_000; src:249-254 with 268-276.
- **Plain-English test of surprise**: A customer expects a contract unchallenged for years to be safe; an Age error unwinds it at any time.

### VN-11 9 — HIV exclusion reaches any death "related to" infection
- **Class**: T2
- **Scenario**: Deaths "do liên quan đến" HIV infection are excluded under a chapeau reaching "trực tiếp hay gián tiếp" (direct or indirect) causes. An insurer can argue any death of an HIV-positive insured is indirectly related, whatever the proximate cause; there is no carve-out for transfusion or occupational infection.
- **Who bears it**: beneficiary. **Money direction**: against the claimant.
- **Standing**: CONTESTED (the encoder frames it as what "an insurer can argue"; the encoding records the relation as found).
- **Evidence**: no assertion (reading only); src:132-134, 141-145.
- **Plain-English test of surprise**: A customer expects a death in an unrelated accident to be paid; the wording lets the insurer link it to an underlying infection.

### VN-11 10 — A child insured cannot sign as required
- **Class**: T6 / T13 silent consequence
- **Scenario**: Art 1.3 admits an insured of Age 0, but Art 1.5 requires the insured to sign the application and names nobody to sign for a child. On a truthful record the child's claim cannot be answered; residence and issue-Age failures likewise have no stated consequence.
- **Who bears it**: beneficiary. **Money direction**: unclear.
- **Standing**: LITERAL (fork L11 notes Law Art 39(2)(a) wants parental consent).
- **Evidence**: `vn11-findings.l4:90` (`#ASSERT REFUSED`); `vn11-tests.l4:369, 505`; src:26-31, 43-45, 201-203.
- **Plain-English test of surprise**: Parents insuring a baby expect it to work; the baby cannot meet the condition.

### VN-11 11 — Contract ends at death and again at settlement
- **Class**: T7
- **Scenario**: Art 18(ii) ends the contract on the day of death; Art 16 ends it "sau khi đã giải quyết xong quyền lợi bảo hiểm" (once the claim is settled). Between the two it is unclear whether premiums falling due are owed or the Company's other duties survive.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL (reading only).
- **Evidence**: no assertion (reading only); src:383-385, 405.
- **Plain-English test of surprise**: A customer expects one end date; the wording gives two with a gap between them.

### VN-11 12 — Short free look; no receipts means no refund
- **Class**: T3 / T12
- **Scenario**: The free look is 14 days; a cancellation sent on day 20 is late. A timely cancellation without the premium receipts returned gets "không hoàn trả lại bất cứ một khoản tiền nào" (nothing at all), and no deadline for the receipts is set.
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: LAW as to 14 days (Law Art 35: 21, fork L1, precedence unverified); LITERAL as to receipts.
- **Evidence**: `vn11-findings.l4:97` (late) and `:98` (`cancelled, and nothing is refunded`); src:185-195.
- **Plain-English test of surprise**: A customer who cancels in time expects the money back; a lost receipt forfeits it all.

### VN-11 13 — "All unpaid premiums" deducts what the Company waived
- **Class**: T7 / T4
- **Scenario**: Art 3(a)(iii) deducts "Tất cả các khoản phí bảo hiểm chưa đóng"; Art 5 says the Company will not require the rest of the year's premiums on a death claim. A death on 10 May 2023 under a monthly mode pays 1 billion on the reading taken, 992.5 million on the literal one.
- **Who bears it**: beneficiary. **Money direction**: against the claimant (on the literal reading).
- **Standing**: CONTESTED (fork F7 takes "due and unpaid").
- **Evidence**: `vn11-findings.l4:124` (1_000_000_000) and `:125` (992_500_000); src:93 with 162-169.
- **Plain-English test of surprise**: A customer told the rest of the year's premium is not required expects no deduction; the literal formula takes it anyway.

### VN-11 14 — No payment deadline; late interest cannot be computed
- **Class**: T1 / T5
- **Scenario**: "Sẽ cố gắng giải quyết ngay" (will try to settle promptly) binds to nothing; interest at the State Bank overdue rate is owed after two months "vì bất kỳ lý do gì" (for whatever reason), but its period, day count and base are not stated.
- **Who bears it**: beneficiary (no deadline); insurer (interest regardless of fault). **Money direction**: unclear.
- **Standing**: LAW. Law Art 31(1) gives 15 days where none is agreed (fork L4); whether "2 months" is agreed is open.
- **Evidence**: `vn11-tests.l4:676` (`#ASSERT REFUSED … the interest …`); src:376-383.
- **Plain-English test of surprise**: A claimant expects a payment date and a computable late charge; the wording gives neither.

### VN-11 15 — No rule before the first premium is paid
- **Class**: T13 silent consequence / T1
- **Scenario**: Grace and lapse rules apply only "Sau khi đóng phí bảo hiểm lần đầu" (after the first premium), while cover runs from the effective date. A death on 1 Mar 2020, after the effective date but before any premium, is unaddressed; the encoding refuses.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL (fork F25 refused).
- **Evidence**: `vn11-findings.l4:129`, `#ASSERT REFUSED … no premium paid`; src:151.
- **Plain-English test of surprise**: A customer expects to know whether cover starts before paying; the wording does not say.

### VN-11 16 — Death benefit formula can go negative
- **Class**: T4
- **Scenario**: Benefit = (i) plus (ii) less (iii) with no floor. A child of Age 0 at 20% of a 100 million sum insured (20 million) with 25 million overdue yields minus 5 million. The encoder calls it theoretical, since such premiums are unrealistic.
- **Who bears it**: beneficiary. **Money direction**: against the claimant.
- **Standing**: LITERAL ("Theoretical").
- **Evidence**: `vn11-findings.l4:136`, `Art 3(a) — the death benefit` … EQUALS 0 MINUS 5_000_000; src:83-93.
- **Plain-English test of surprise**: A customer expects a death benefit of at least nil; the formula can produce a debt.

#### VN-11 row summary
- **Findings in section 4**: 16 (numbered 1 to 16). Findings 7, 9, 11 and 14 have no block in `vn11-findings.l4` (14 has its evidence in `vn11-tests.l4:676`).
- **Most counterintuitive**: (1) the murdered insured excluded on the literal crime exclusion; (3) the beneficiary out of time because only the dead policyholder could invoke the discovery rule; (12) a timely cancellation refunding nothing for want of receipts.
- **Matches in this group**: 1 = VN-13 2 (crime exclusion with no subject); 3 = VN-13 7 (discovery rule for the policyholder only); 8 = VN-13 9 and relates to VN-25 FD4 (a ground to refuse with no time limit); 9 = VN-13 24 (HIV/AIDS "related to", no carve-out); 6 = VN-13 23 (no beneficiary); 14 = VN-13 15 (no payment deadline, interest that cannot be computed); 16 = VN-14 X10, VN-24 X3, VN-25 FD26 (no floor); 7 = VN-14 X12, VN-25 FD18, VN-26 F-14 (discretion without criteria); 5 relates to VN-13 6, VN-25 FD19, VN-26 F-10 (what is returned on avoidance). See also the group cross-reference at the end of this file.

## VN-13 Manulife unit-linked regular premium

### VN-13 1 — Premium debt deducted twice from the death benefit
- **Class**: T4
- **Scenario**: The surrender value is already the account value less premium debt; Art 3.1 adds that surrender value and then subtracts the debt again (3.2 likewise). With a 2,000,000 debt the death benefit is 757,300,000 instead of 759,300,000; 3.2 pays 207,000,000 against a 209,000,000 surrender value. Art 18's "các khoản phí khác" makes a third deduction arguable (reading only).
- **Who bears it**: beneficiary. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `vn13-findings.l4:38-39` and `:41`; src 30-32, 145-147, 154, 165-168, 761-763.
- **Plain-English test of surprise**: A customer expects an unpaid premium to be deducted once; the formula takes it twice.

### VN-13 2 — Offence exclusion has no subject; murder victim excluded
- **Class**: T2 / T5
- **Scenario**: "Phạm tội" names no offender, so on the literal reading a death caused by anyone's offence (a murder, a drunk driver) pays only the surrender value. For a murdered Life Insured, the reading taken pays 757,300,000; the literal one 207,000,000.
- **Who bears it**: beneficiary. **Money direction**: against the claimant.
- **Standing**: CONTESTED (fork F6 takes the Life Insured's own offence, citing Law Art 24's reading for the buyer).
- **Evidence**: `vn13-findings.l4:55` (literal: excluded) and `:56` (taken: 757_300_000); src 156-158.
- **Plain-English test of surprise**: A family expects a murder victim's death to be covered; the words exclude it.

### VN-13 3 — Grace period restarts monthly and never ends
- **Class**: T1
- **Scenario**: Grace runs 60 days from the day the surrender value was "most recently" found short, and a shortfall is found at every monthly deduction. With shortfalls on the 10th of each month from March 2028, the taken reading ends the contract on 10 May 2028; on the literal reading it has still not ended on 30 June 2029 or ever.
- **Who bears it**: insurer (unbounded exposure; free cover for the policyholder). **Money direction**: against the insurer.
- **Standing**: CONTESTED (fork F15 takes the determination that opened the grace).
- **Evidence**: `vn13-findings.l4:92-94`; src 368-377.
- **Plain-English test of surprise**: Both sides expect a grace period to end; the literal clock resets forever.

### VN-13 4 — No rule for a first-year account shortfall
- **Class**: T13 silent consequence / T1
- **Scenario**: The first-year rule covers only an unpaid premium; the shortfall rule starts from the second policy year. With a 90% initial charge the first-year account is small, so a policyholder can pay every premium and still have a monthly deduction fail (June 2026); the encoding refuses.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL.
- **Evidence**: `vn13-findings.l4:101`, `#ASSERT REFUSED … in the first policy year`; also `vn13-tests-mechanics.l4:93`; src 353-367.
- **Plain-English test of surprise**: A customer paying on time expects cover to be secure; the wording does not say what happens when charges outrun the account.

### VN-13 5 — Death benefit floats with the market until the claim
- **Class**: T4 / T1
- **Scenario**: The surrender value in the death benefit is taken after the claim date, not the death, so the beneficiary carries market moves in between: one death pays 757,300,000 if the claim is complete on 10 Mar 2030, 768,300,000 if on 13 Mar. Only some charges deducted after the death are refunded; the policy fee is not (reading only).
- **Who bears it**: beneficiary. **Money direction**: unclear (market either way; kept charges against the claimant).
- **Standing**: LITERAL.
- **Evidence**: `vn13-findings.l4:116-117`; src 145-151.
- **Plain-English test of surprise**: A family expects the benefit fixed at death; it depends on how fast they file.

### VN-13 6 — Avoidance refunds charges, not premiums, without intent
- **Class**: T3 / T4
- **Scenario**: On avoidance, the Company refunds charges collected plus the surrender value, not premiums; the bid-offer spread, fund fees and investment losses stay with the policyholder, and no intent is needed. With flat prices, 20,000,000 paid returns 19,900,000.
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: LAW. Law Art 22(2) requires intent and refunds the premiums (less reasonable costs); the encoding follows the document.
- **Evidence**: `vn13-findings.l4:127`, EQUALS 19_900_000; src 234-253.
- **Plain-English test of surprise**: A policyholder whose contract is undone for an innocent error expects the premiums back; the wording keeps the spread.

### VN-13 7 — Discovery extension available only to the deceased policyholder
- **Class**: T1 / T3
- **Scenario**: Only the policyholder may prove not knowing of the event to extend the one-year claim limit, and in a death claim the policyholder is the one who died. A beneficiary who learns of the death 18 months on and claims at once gets nothing.
- **Who bears it**: beneficiary. **Money direction**: against the claimant.
- **Standing**: LAW. Law Art 30(2) gives the extension to the beneficiary.
- **Evidence**: `vn13-findings.l4:135`, EQUALS `nothing, because the claim was made after the Article 18 time limit`; src 758-761.
- **Plain-English test of surprise**: A beneficiary unaware of the death expects time to run from learning of it; the extension is given only to the dead.

### VN-13 8 — Cover ends at 99 a year before payout date
- **Class**: T7 / T1
- **Scenario**: For a Life Insured born on the anniversary date (born 10 Jan 1990, effective 10 Jan 2026), the contract ends on the anniversary at Age 99, 10 Jan 2089, while the surrender value is determined "on the anniversary following" the 99th birthday, read strictly 10 Jan 2090.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: CONTESTED (fork F28 takes the two as the same day).
- **Evidence**: `vn13-findings.l4:152` (2089-01-10) and `:153` (2090-01-10); src 798-802.
- **Plain-English test of surprise**: A customer expects the maturity payment when cover ends; the wording can put it a year later.

### VN-13 9 — Misstated age voids cover at any duration
- **Class**: T7 / T1
- **Scenario**: Art 7's two-year contest bar does not reach age, and Art 6 has no time limit. A true age outside the range, discovered 20 years on, pays a 300,000,000 surrender value and no sum assured, and the payment goes to the policyholder, who at a death claim is dead (reading only).
- **Who bears it**: beneficiary. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `vn13-findings.l4:160`, EQUALS 300_000_000; src 216, 223-225, 260-262.
- **Plain-English test of surprise**: A customer expects a 20-year-old contract to be beyond challenge; an age error undoes it.

### VN-13 10 — "20% for each fund" can become unsatisfiable
- **Class**: T5
- **Scenario**: Art 17.2 requires "tối thiểu là 20% cho mỗi Quỹ". If that means every fund that exists, a half-and-half split across two of three funds fails, and once the Company opens six funds (which it may at any time) no allocation can pass, since 6 × 20% is 120%.
- **Who bears it**: policyholder. **Money direction**: no money.
- **Standing**: CONTESTED (fork F25 takes each fund in the allocation).
- **Evidence**: `vn13-findings.l4:174-176`; src 468-469, 729-731.
- **Plain-English test of surprise**: A customer expects to choose a simple allocation; one reading forbids every allocation.

### VN-13 11 — Company may keep part of a refused premium
- **Class**: T11
- **Scenario**: When the Company refuses a premium it refunds "một phần hay toàn bộ" (part or all) with no criteria: on a 19,000,000 refused premium, a refund of 1 dong is one the Article allows.
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `vn13-findings.l4:180`; src 536-538.
- **Plain-English test of surprise**: A customer expects a refused premium back in full; the wording lets the insurer keep almost all of it.

### VN-13 12 — Fund closure points to a procedure that does not exist
- **Class**: T8 / T11
- **Scenario**: Art 11.4 says a closed fund's units are dealt with under an Annex 2 procedure that Annex 2 does not contain; the policyholder's reply window is "do Công ty ấn định" (set by the Company) with no minimum, after a notice that may be only 3 days.
- **Who bears it**: policyholder. **Money direction**: unclear.
- **Standing**: LITERAL.
- **Evidence**: `vn13-tests-mechanics.l4:154`, `#ASSERT REFUSED … what becomes of the units of a closed fund`; src 474-487.
- **Plain-English test of surprise**: An investor expects a stated procedure when a fund closes; the cross-reference leads nowhere.

### VN-13 13 — Switch timing refers to a time never stated
- **Class**: T8
- **Scenario**: Annex 2 E vii says a fund switch takes effect at a time "nêu trong Hợp đồng" (stated in the contract); the contract states none, so the switch date cannot be computed.
- **Who bears it**: policyholder. **Money direction**: unclear.
- **Standing**: LITERAL.
- **Evidence**: `vn13-tests-mechanics.l4:454`, `#ASSERT REFUSED Annex 2 E vii — the day a switch takes effect`; src 1041-1043.
- **Plain-English test of surprise**: An investor expects to know when a switch is priced; the document points to a term it lacks.

### VN-13 14 — Transaction minimums and maximums stated nowhere
- **Class**: T8
- **Scenario**: Annex 2 relies on a minimum top-up, minimum withdrawal, minimum balance, maximum number of withdrawals, minimum switch, minimum sum-assured change and the minimum payment period a premium holiday turns on; none is stated or assigned to the Schedule. Whether a premium holiday may start cannot be answered.
- **Who bears it**: policyholder. **Money direction**: unclear.
- **Standing**: LITERAL.
- **Evidence**: `vn13-tests-mechanics.l4:400`, `#ASSERT REFUSED Annex 2 C …`; the rest are inputs (reading only); src 963-964, 985-986, 998, 1003-1008, 1016-1017, 1030-1032, 1073-1074.
- **Plain-English test of surprise**: A customer expects the limits on using the account to be written down; they are not.

### VN-13 15 — Late-claim interest rate set by the Company
- **Class**: T11 / T1
- **Scenario**: Interest on a late claim is at a rate and method the Company decides, and the Company has no payment deadline ("sẽ cố gắng", will try).
- **Who bears it**: beneficiary. **Money direction**: against the claimant.
- **Standing**: LITERAL. The fork register (F27) notes Law Art 31(1) sets 15 days where none is agreed; not resolved.
- **Evidence**: `vn13-tests-cover.l4:357`, `#ASSERT REFUSED Article 18 leaves the rate and the method of interest to the Company`; src 764, 767-768.
- **Plain-English test of surprise**: A claimant expects a deadline and a set late-payment rate; the insurer controls both.

### VN-13 16 — Loans deducted from payments; no loans exist
- **Class**: T5 / T8
- **Scenario**: Art 18 deducts "nợ vay" (loans) from every payment, but the document provides for no policy loans.
- **Who bears it**: unclear. **Money direction**: against the claimant (inferred, if any amount were deducted).
- **Standing**: LITERAL (reading only).
- **Evidence**: no assertion (reading only); src 762.
- **Plain-English test of surprise**: A customer expects deductions to refer to things the contract creates; this one refers to nothing.

### VN-13 17 — Insurance-charge cap tied to the Company's own table
- **Class**: T6 / T11
- **Scenario**: The guaranteed maximum cost of insurance is set by "bảng tỷ lệ tử vong tiêu chuẩn Công ty đang sử dụng" (the standard mortality table the Company is using), so the cap moves with the Company's own choice and caps nothing the policyholder can check.
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: LITERAL (reading only).
- **Evidence**: no assertion (reading only); src 668-669.
- **Plain-English test of surprise**: A customer reads "maximum" as a fixed ceiling; the insurer can raise it.

### VN-13 18 — Valuation suspension has no end and no notice
- **Class**: T11 / T1
- **Scenario**: Art 11.7(d) lets valuation be suspended with no end date and no notice, and every payment (death benefit, surrender) is priced on "the next Valuation Date", so a suspension postpones payment without limit.
- **Who bears it**: beneficiary / policyholder. **Money direction**: against the claimant.
- **Standing**: LITERAL (reading only).
- **Evidence**: no assertion (reading only); src 523-532.
- **Plain-English test of surprise**: A family expects a death benefit within a bounded time; a suspension can delay it indefinitely.

### VN-13 19 — Company notices count as endorsements changing charges
- **Class**: T11 / T7
- **Scenario**: Art 2 treats the Company's notices as endorsements, and charges are "in the Schedule or an endorsement", while Art 2 ¶3 requires consent to any change. Unless ¶3 is read over the rest, a notice is a route to unilateral change.
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: CONTESTED (fork F32 takes ¶3 as governing every change).
- **Evidence**: no assertion (reading only); src 116-119, 557-558, 568-569.
- **Plain-English test of surprise**: A customer expects charges to change only with consent; one reading lets a notice do it.

### VN-13 20 — Receipt-time rules miss early, holiday and pending submissions
- **Class**: T13 silent consequence / T1
- **Scenario**: Annex 2 A fixes the receipt date only for submissions between 8:30 and 15:00 on working days; a submission at 8:29, one on a non-working day before 15:01, or one made while another transaction is pending, has no receipt date.
- **Who bears it**: policyholder. **Money direction**: unclear.
- **Standing**: LITERAL.
- **Evidence**: `vn13-tests-mechanics.l4:363, 365, 367`, three `#ASSERT REFUSED`; src 946-954.
- **Plain-English test of surprise**: A customer expects any submission to be dated; some fall outside every rule.

### VN-13 21 — Sum-assured change effective date fails twice
- **Class**: T5 / T1
- **Scenario**: Annex 2 F dates a change from "ngày hiệu lực Hợp đồng kế tiếp", which is undefined; an approval on the paid-to date is not provided for; and under the defined meaning of "Ngày đã được trả phí" (the last payment) an approval nearly always comes after it.
- **Who bears it**: policyholder. **Money direction**: unclear.
- **Standing**: LITERAL (fork F3 substitutes the paid-to date as an input).
- **Evidence**: `vn13-tests-mechanics.l4:489-490`, two `#ASSERT REFUSED`; src 1055-1058, 1077-1080.
- **Plain-English test of surprise**: A customer expects a change of cover to have a start date; the wording gives none.

### VN-13 22 — Riders end "after a grace period" that does not exist
- **Class**: T1 / T7
- **Scenario**: From the second year, riders end "ngay sau thời gian gia hạn" (right after the grace period) on an unnotified delay, but from the second year a delay opens no grace period, so a 2027 premium delay gives no rider end date.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL.
- **Evidence**: `vn13-tests-mechanics.l4:59`, `#ASSERT REFUSED Article 9.3 — the day the riders end …`; src 324-327, 364-367.
- **Plain-English test of surprise**: A customer expects rider cover to end on a knowable date; the clock it refers to never starts.

### VN-13 23 — No beneficiary named, no payee for death benefit
- **Class**: T13 silent consequence
- **Scenario**: Art 16 does not say who takes the death benefit when no beneficiary is named; the encoding refuses.
- **Who bears it**: beneficiary (the estate, inferred). **Money direction**: unclear.
- **Standing**: LITERAL.
- **Evidence**: `vn13-tests-cover.l4:290`, `#ASSERT REFUSED Article 16 — who is paid …`; src 694-701.
- **Plain-English test of surprise**: A customer expects a default payee; there is none.

### VN-13 24 — AIDS exclusion lifelong, no transfusion or work exception
- **Class**: T2
- **Scenario**: The AIDS exclusion has no time limit and no exception for infection by transfusion or at work, and reaches "any death … related to" it.
- **Who bears it**: beneficiary. **Money direction**: against the claimant.
- **Standing**: LITERAL (reading only; fork F39 takes the relation as a finding of fact).
- **Evidence**: no assertion (reading only); src 159-162.
- **Plain-English test of surprise**: A customer infected through a hospital transfusion expects cover; the wording makes no exception.

### VN-13 25 — Loyalty bonus lost by using a contractual right
- **Class**: T6
- **Scenario**: The loyalty bonus is forfeited by taking a premium holiday, a right Art 9.3 grants, or by any lapse, even one later reinstated.
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: LITERAL (reading only).
- **Evidence**: no assertion (reading only); src 180-183.
- **Plain-English test of surprise**: A customer expects to use a feature without penalty; using it costs the bonus.

### VN-13 26 — Customer deadlines strict, Company deadlines absent
- **Class**: T1 / T11
- **Scenario**: The policyholder has one year to claim, three to sue, and requests count only at the counter before 15:00; the Company has no deadline to pay a claim, a free-look refund or a surrender, and may close a fund on 3 days' notice with a reply window it sets.
- **Who bears it**: policyholder / beneficiary. **Money direction**: against the claimant.
- **Standing**: LITERAL (reading only).
- **Evidence**: no assertion (reading only); src 202-204, 474-481, 549-554.
- **Plain-English test of surprise**: A customer expects deadlines to bind both sides; only the customer's are fixed.

#### VN-13 row summary
- **Findings in section 4**: 26 (numbered 1 to 26). 1-11 are evidenced in `vn13-findings.l4`; 12-15 and 20-23 in `vn13-tests-mechanics.l4` or `vn13-tests-cover.l4`; 16-19 and 24-26 are reading only.
- **Most counterintuitive**: (3) a grace period that on the literal reading never ends; (2) a murdered Life Insured paid 207,000,000 instead of 757,300,000 on the literal reading; (11) a refused 19,000,000 premium of which the Company may return 1 dong.
- **Matches in this group**: 2 = VN-11 1 (crime exclusion with no subject); 7 = VN-11 3 (discovery rule for the policyholder only); 9 = VN-11 8 (misstated age with no time limit); 23 = VN-11 6 (no beneficiary); 24 = VN-11 9 (HIV/AIDS "related to", no carve-out); 15 = VN-11 14 (no payment deadline, incomputable interest); 6 relates to VN-11 5 (consequence of avoidance).

## VN-14 Manulife group universal-linked flexible premium

### VN-14 X1 — Turning 66 or travelling abroad ends cover
- **Class**: T5 / T6
- **Scenario**: Art 1.4's conditions (age 1 month to 65, presence in Vietnam) are met "vào thời điểm yêu cầu bảo hiểm"; Art 28.4 ends a part "ngay" when the member "no longer meets" them. Read as continuing, a member born 1 Mar 1960 loses cover on 2 Mar 2026, and a member of 40 abroad on business too, whatever the Certificate's Maturity Date.
- **Who bears it**: insured / beneficiary. **Money direction**: against the claimant.
- **Standing**: CONTESTED (fork F24 takes continuing; otherwise the triggers never fire).
- **Evidence**: `vn14-findings.l4:86-88`; src:37-47, 610-620, 1433-1437.
- **Plain-English test of surprise**: An employee expects cover to maturity; a birthday or trip ends it.

### VN-14 X2 — Covered accident pays less than excluded suicide
- **Class**: T6 / T4
- **Scenario**: During temporary cover, a covered accidental death pays the lesser of the pending Sum Insured and 200,000,000 with no premium refund; an excluded suicide refunds premium less costs. With 100,000,000 pending and 150,000,000 paid, the accident pays 100,000,000 and the suicide 148,000,000. A non-accidental death leaves the paid premium unaddressed.
- **Who bears it**: beneficiary. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `vn14-findings.l4:114-115`; `vn14-tests-ch1.l4:365` (`#ASSERT REFUSED Article 3 — the premium refunded`); src:270-289, 308-319.
- **Plain-English test of surprise**: A family expects a covered death to pay at least as much as an excluded one; here it pays less.

### VN-14 X3 — Temporary benefit payee named in the wrong form
- **Class**: T7
- **Scenario**: The temporary benefit goes to "Người Thụ Hưởng có tên trong hồ sơ yêu cầu bảo hiểm" (beneficiaries named in the application), but the application is the employer's and beneficiaries are named in each member's Enrolment Form.
- **Who bears it**: beneficiary. **Money direction**: unclear.
- **Standing**: LITERAL (reading only).
- **Evidence**: no assertion (reading only); src:52-64, 280-281, 502-504.
- **Plain-English test of surprise**: A member expects the beneficiary on the member's own form to be paid; the clause points to a document that names nobody.

### VN-14 X4 — No temporary cover for members added later
- **Class**: T6 / T1
- **Scenario**: Temporary cover ends "vào Ngày Cấp Hợp Đồng" (on the contract's issue date), which for a member added later is already past, so the period is empty: a member added in 2027 to a contract issued in 2026 has no temporary benefit.
- **Who bears it**: insured / beneficiary. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `vn14-findings.l4:140-141`, EQUALS `no temporary benefit is payable`; src:290-295, 598-609.
- **Plain-English test of surprise**: A new employee expects the same interim cover as the original group; the clock has already run out.

### VN-14 X5 — Disclosure breaches outside two types have no consequence
- **Class**: T13 silent consequence
- **Scenario**: Art 5.2 covers a deliberate breach the Company would have declined; 5.3 a breach that did not affect the decision. An honest but material mistake, or a deliberate one that would only have raised the premium (the case Art 7.2 names), has no stated consequence.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL.
- **Evidence**: `vn14-findings.l4:165-166`, both `#ASSERT REFUSED`; `vn14-tests-ch1.l4:426-427`; src:385-414, 487-492.
- **Plain-English test of surprise**: Both sides expect an innocent misstatement to have some defined result; the document has none.

### VN-14 X6 — Misstated-age refund deducts withdrawals twice
- **Class**: T4
- **Scenario**: Art 6.2 refunds the greater of the Account Value and premium paid, "trừ đi … các khoản Rút Giá Trị Tài Khoản" (less withdrawals), though the Account Value is already net of withdrawals. With 10,000,000 withdrawn, an Account Value of 100,000,000 after it and 80,000,000 premium, the refund is 90,000,000, not 100,000,000.
- **Who bears it**: policyholder / insured. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `vn14-findings.l4:189`, EQUALS 90_000_000; src:433-440.
- **Plain-English test of surprise**: A member expects a withdrawal to reduce the refund once; it is taken twice.

### VN-14 X7 — Death during suspension pays nothing, not even the account
- **Class**: T6 / T13 silent consequence
- **Scenario**: While a part is suspended, all remaining benefits "bao gồm cả quyền lợi tử vong" (including the death benefit) "sẽ không được thực hiện". The part ends on death; the employer's account goes back to the employer, but nothing returns the member's own account, over which Art 17.1 gives the member "toàn quyền" (full rights).
- **Who bears it**: beneficiary. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `vn14-findings.l4:193-194`, EQUALS `no benefit: the part was suspended under Article 20`; src:955-957, 984-988, 1072-1077.
- **Plain-English test of surprise**: A family expects at least the member's own savings back; the wording returns nothing.

### VN-14 X8 — One early payment, two allocation rules
- **Class**: T7
- **Scenario**: With nothing overdue, 25,000,000 paid 10 days before the due date is all Top-up Premium under Art 16.2.1, but under 16.2.3 is applied first to the next instalment.
- **Who bears it**: policyholder. **Money direction**: unclear.
- **Standing**: LITERAL.
- **Evidence**: `vn14-findings.l4:213-214`; src:821-825, 914-928.
- **Plain-English test of surprise**: An employer expects one answer to where a payment goes; the document gives two.

### VN-14 X9 — Employer's crime defeats employee's death benefit
- **Class**: T2 / T13 silent consequence
- **Scenario**: Exclusion 15(b) includes criminal acts of the Policyholder, an organisation, so an employer's crime directly related to an employee's death leaves only the account value (100,000,000; the same fixture without the crime pays 1,000,000,000), payable to no named person. One beneficiary's crime defeats all shares; the list ends "Hưởng; hoặc" with nothing after.
- **Who bears it**: beneficiary. **Money direction**: against the claimant.
- **Standing**: LITERAL; LAW as to one beneficiary defeating all (fork F32, Law Art 40(2) keeps others' shares).
- **Evidence**: `vn14-findings.l4:220-222` (payee `REFUSED`), compare `:299`; src:781-798.
- **Plain-English test of surprise**: An employee's family expects cover regardless of the employer's wrongdoing; the employer's crime cancels it.

### VN-14 X10 — Refund formulas have no floor
- **Class**: T4
- **Scenario**: In Arts 3.3, 6.2, 10.2 and 15 deductions can exceed the amount with no floor; only 5.2 says the Company will not claw back. A small part found misstated (Account Value 5,000,000, premium 8,000,000, withdrawals 10,000,000) has no answer.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL.
- **Evidence**: `vn14-findings.l4:242-243`, `#ASSERT REFUSED`; `vn14-tests-ch1.l4:461`, `vn14-tests-ch2.l4:155`; src:308-313, 395-398, 436-440, 570-572, 793-798.
- **Plain-English test of surprise**: A member expects a refund of at least nil; the formula can go below it.

### VN-14 X11 — Employer must report employee's details, without consequence
- **Class**: T13 silent consequence / T7
- **Scenario**: Art 10.2 makes the employer notify, within 30 days, a change of the member's own residence, name or identity card; nothing follows from a late notice.
- **Who bears it**: policyholder (the employer). **Money direction**: no money.
- **Standing**: LITERAL (reading only for the consequence).
- **Evidence**: `vn14-tests-ch1.l4:559-561`, the 10.2 trace breaches; src:554-558.
- **Plain-English test of surprise**: One expects the person whose details change to report them, and a late report to matter; neither holds.

### VN-14 X12 — Repricing, exclusion and approvals with no criteria
- **Class**: T11
- **Scenario**: After any listed change, even a new name or identity card, Art 10.2 lets the Company reprice, exclude benefits or stop cover; 11.1, 11.2 ("xem xét"), 12.2 ("Công Ty sẽ xem xét chi trả", will consider paying), 16.3, 23.1(d) and 24.1 give further discretion with no standard.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `vn14-findings.l4:248` (a change of name engages the 10.2 powers) and `:249`; src:559-566, 718-719, 939-940, 1177-1179, 1203-1209.
- **Plain-English test of surprise**: A member who marries and changes name expects nothing to happen to cover; the insurer may stop it.

### VN-14 X13 — Two clauses refund the same part differently
- **Class**: T7 / T4
- **Scenario**: Art 10.2 copies 6.2's wording, including a notice "về việc kê khai không chính xác đó" (about that inaccurate declaration) where none is in issue, but deducts benefits and withdrawals and not Debt or costs. On one part, 6.2 gives 86,000,000 and 10.2 gives 90,000,000.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL.
- **Evidence**: `vn14-findings.l4:269-270`; src:566-572.
- **Plain-English test of surprise**: A member expects the same refund rule for the same account; the two clauses differ by 4,000,000.

### VN-14 X14 — No rule for a common disaster
- **Class**: T13 silent consequence / T5
- **Scenario**: Art 9.3 provides only for beneficiaries who die "trước khi" (before) the Insured Member, so a beneficiary who dies at the same moment is unprovided for; its two rules are also joined by "hoặc" (or).
- **Who bears it**: beneficiary. **Money direction**: unclear.
- **Standing**: LITERAL.
- **Evidence**: `vn14-findings.l4:274`, `#ASSERT REFUSED`; src:517-534.
- **Plain-English test of surprise**: A family expects a rule for a shared accident; there is none.

### VN-14 X15 — Product limits not stated in the document
- **Class**: T8 / T11
- **Scenario**: The product's minimum and maximum Sum Insured and the Company's withdrawal minimums "tại từng thời điểm" (from time to time) are used but stated nowhere.
- **Who bears it**: policyholder / insured. **Money direction**: unclear.
- **Standing**: LITERAL (reading only; they are inputs).
- **Evidence**: no assertion (reading only); src:1101-1104, 1111-1113, 1157-1159.
- **Plain-English test of surprise**: A member expects the limits on the account to be written down; they are not.

### VN-14 X16 — Death benefit conditioned inconsistently and only "considered"
- **Class**: T7 / T11
- **Scenario**: Art 12.2 conditions the death benefit on the Contract being in force, 12.1 on the member's part; and 12.2 says only that the Company "xem xét" (considers) paying.
- **Who bears it**: beneficiary. **Money direction**: against the claimant (inferred).
- **Standing**: CONTESTED (resolved by fork F30: the part must be in force).
- **Evidence**: no assertion (reading only); src:708-709, 716-719.
- **Plain-English test of surprise**: A family expects a death benefit to be owed, not considered; the wording hedges.

### VN-14 X17 — One monthly deduction taken on two days
- **Class**: T7 / T1
- **Scenario**: The administration charge comes off on the member's Monthly Anniversary, the cost of insurance on the Contract Monthly Anniversary, yet Art 18.1 tests the Account Value against the whole Monthly Deduction.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL (reading only).
- **Evidence**: no assertion (reading only); src:1288-1289, 1310-1311.
- **Plain-English test of surprise**: A member expects one deduction date for one charge; there are two.

### VN-14 X18 — Termination charge applies on conflicting triggers
- **Class**: T7
- **Scenario**: Art 1.19 charges a Termination Charge whenever a part ends early; 25.4 only "khi Bên Mua Bảo Hiểm yêu cầu chấm dứt" (when the policyholder requests); Art 22 needs policyholder and member together; 11.2(b) and 29.2 deduct it "(nếu có)" on ends nobody requested.
- **Who bears it**: insured. **Money direction**: against the claimant (inferred).
- **Standing**: LITERAL (reading only).
- **Evidence**: no assertion (reading only); src:187-190, 1327-1329.
- **Plain-English test of surprise**: A member whose cover ends without asking expects no exit fee; one clause charges it.

### VN-14 X19 — Literal claims clause pays only late, force-majeure claims
- **Class**: T5 / T6
- **Scenario**: Art 26.1 says the Company "sẽ chỉ xem xét và/hoặc có nghĩa vụ chi trả" (will only consider and/or be obliged to pay) where a late claim is due to force majeure; read literally, payment depends on a late claim.
- **Who bears it**: beneficiary. **Money direction**: against the claimant (literal reading).
- **Standing**: CONTESTED (resolved by fork F26 as an exception for late claims).
- **Evidence**: no assertion (reading only); src:1368-1371.
- **Plain-English test of surprise**: A claimant filing promptly expects to be paid; the literal sentence ties payment to force majeure.

### VN-14 X20 — Claim completeness defined by a changeable website list
- **Class**: T11 / T1
- **Scenario**: The 30-day payment clock starts only on "đầy đủ các chứng từ" (all documents), whose list the Company publishes on its website and can change. A claim with every document in the contract but one the website lists is incomplete.
- **Who bears it**: beneficiary. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `vn14-findings.l4:278`, `#ASSERT NOT … the claim documents are complete`; src:1389-1393.
- **Plain-English test of surprise**: A claimant expects the required documents to be fixed in the contract; the insurer can move the target.

### VN-14 X21 — Late-payment interest at a rate that does not exist
- **Class**: T5 / T8
- **Scenario**: Late payment carries interest at the rate for "tạm ứng từ Giá Trị Tài Khoản" (advances from the Account Value), but the document provides no such advance and no such rate. A claim complete on 1 Mar 2026 and paid on 1 Jun 2026 carries no computable interest.
- **Who bears it**: beneficiary. **Money direction**: against the claimant (inferred).
- **Standing**: LITERAL.
- **Evidence**: `vn14-findings.l4:282`, `#ASSERT REFUSED`; `vn14-tests-ch3-ch5.l4:437`; src:1402-1407.
- **Plain-English test of surprise**: A claimant paid three months late expects interest; the rate refers to nothing.

### VN-14 X22 — No forum for the member or beneficiary
- **Class**: T13 forum / T5
- **Scenario**: Disputes go to the court where the Policyholder "cư trú hợp pháp" (lawfully resides), a word for a person when the Policyholder is an organisation, or the Company's head office; the member and the beneficiary get no forum of their own.
- **Who bears it**: insured / beneficiary. **Money direction**: no money.
- **Standing**: LITERAL (reading only).
- **Evidence**: no assertion (reading only); src:1415-1418.
- **Plain-English test of surprise**: An employee expects to sue locally; the clause offers only the employer's or insurer's seat.

### VN-14 X23 — Accelerated vesting skipped when employer simply terminates
- **Class**: T6 / T7
- **Scenario**: Art 29.3 fully vests the employer's contributions when the employer dissolves or merges, but not when it simply asks to end the contract. A member with 20 years' service gets 60,000,000 on a merger and 18,000,000 otherwise.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `vn14-findings.l4:289-292`; src:1509-1531.
- **Plain-English test of surprise**: An employee expects full vesting whenever the scheme ends; the employer can avoid it by choosing how.

### VN-14 X24 — Premium paid between death and claim is kept
- **Class**: T4
- **Scenario**: Art 12.4(a) adds back only premium paid after the claim date. With a 1,000,000,000 Sum Insured, 10,000,000 paid after the death but before the claim raises the Account Value from 100,000,000 to 110,000,000 and the benefit is 1,000,000,000 either way.
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `vn14-findings.l4:299-300`; src:681-683.
- **Plain-English test of surprise**: A payer who keeps paying after a death expects that premium back; it is absorbed.

### VN-14 X25 — Company's own top-up withdrawal forfeits loyalty bonus
- **Class**: T6 / T11
- **Scenario**: At the end of a year-2 grace period the Company itself withdraws 3,000,000 from the Account Value to pay premium; Art 14.1(c) counts any withdrawal "bao gồm cả rút Giá Trị Tài Khoản để đóng Phí Bảo Hiểm", so the 5th-anniversary bonus is 0 though every other condition holds.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `vn14-findings.l4:307` (3_000_000 withdrawn) and `:308` (bonus EQUALS 0); src:762-764, 845-847.
- **Plain-English test of surprise**: A member expects to keep a bonus the member did nothing to lose; the insurer's own action forfeits it.

### VN-14 X26 — Numbering and naming slips
- **Class**: T13 drafting slips
- **Scenario**: Art 1.8 numbers both limbs "(ii)"; two chapters are numbered "CHƯƠNG 4"; the page footer drops "nhóm" (group) from the product name.
- **Who bears it**: unclear. **Money direction**: no money.
- **Standing**: LITERAL (reading only).
- **Evidence**: no assertion (reading only); src:55, 70-71, 1188, 1273.
- **Plain-English test of surprise**: A reader expects unique cross-reference targets; two share a number.

#### VN-14 row summary
- **Findings in section 4**: 26 (X1 to X26). X3, X15-X19, X22 and X26 are reading only; X11's evidence is a trace in `vn14-tests-ch1.l4`.
- **Most counterintuitive**: (X2) a covered accidental death pays 100,000,000 while an excluded suicide refunds 148,000,000; (X9) the employer's crime defeats the employee's death benefit; (X7) a death during suspension returns not even the member's own account.
- **Matches in this group**: X6 = VN-13 1 (same deduction taken twice); X10 = VN-11 16 (no floor); X21 ~ VN-11 14 and VN-13 15 (late-payment interest that cannot be computed); X25 = VN-13 25 (loyalty bonus lost by using a mechanism the contract provides); X15 = VN-13 14 (limits stated nowhere); X12 = VN-11 7 (discretion without criteria); X14 relates to VN-11 6 and VN-13 23 (payee gaps); X9's "no payee" likewise.

## VN-24 AIA Khỏe Trọn Vẹn (unit-linked with critical illness)

### VN-24 X1 — "Customer" means owner and/or insured; rights unassigned
- **Class**: T5
- **Scenario**: "Khách hàng" is the policyowner "và/hoặc" (and/or) the insured, so when they are different people (an employer owning a policy on an employee's life) it is not determined who holds the free-look, withdrawal and change rights; an employee asking to withdraw has no clear answer.
- **Who bears it**: policyholder / insured. **Money direction**: no money.
- **Standing**: CONTESTED (fork F1 takes the policyowner for Part II rights; "Not settled by the text").
- **Evidence**: no assertion (reading only); src 43-45.
- **Plain-English test of surprise**: Parties expect each right to have one holder; the wording names two, either or both.

### VN-24 X2 — Early-stage advances can exceed the sum insured
- **Class**: T4
- **Scenario**: Early-stage advances have no aggregate cap. On a 1 billion sum insured, three 300 million payments leave the contract in force and the fourth is paid in full: 1.2 billion advanced before Art 24(a)(iii) ends the contract, and the termination refund is then paid on top.
- **Who bears it**: insurer. **Money direction**: against the insurer.
- **Standing**: CONTESTED (fork F16 takes it as written; the alternative cuts the last payment to the remainder).
- **Evidence**: `ktv-tests-findings.l4:105-106`; src 71-80, 136-138, 165-170, 779-794.
- **Plain-English test of surprise**: An insurer expects advances to stop at the sum insured; they can pass it.

### VN-24 X3 — Main benefit formula can go below zero
- **Class**: T4
- **Scenario**: Sum insured 1 billion, basic account 50 million, top-up 50 million, 900 million advanced, debts 250 million: 1,000 + 50 − 900 − 250 = −100 million. The document does not say what is paid.
- **Who bears it**: beneficiary / insured. **Money direction**: unclear.
- **Standing**: LITERAL.
- **Evidence**: `ktv-tests-findings.l4:112`, `#ASSERT REFUSED … the main benefit formula gives less than nothing`; src 85-108, 140-152, 307-327, 363-370.
- **Plain-English test of surprise**: A claimant expects a death or TPD benefit of at least nil; the formula can produce a negative.

### VN-24 X4 — Waiting period starts at acceptance, not payment
- **Class**: T10 / T1
- **Scenario**: The 90-day waiting period runs from the Company's acceptance, not the effective date when the premium was paid. Effective 15 Mar 2022, accepted 15 May: cancer diagnosed 10 Aug 2022, 148 days after payment, is still excluded. Slow underwriting stretches the wait.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `ktv-tests-findings.l4:119-120` (within the waiting period; 148 days); src 755-757, 1384-1386.
- **Plain-English test of surprise**: A customer expects 90 days from paying; the insurer's own delay extends it.

### VN-24 X5 — Grace-period cover maintained, then lapsed retroactively
- **Class**: T7 / T1
- **Scenario**: Art 21(b) keeps benefits during the grace period, but 21(c) lapses the contract from the due date, before grace began, if the premium stays unpaid. With a premium due 15 Mar 2023 never paid and a death on 1 Apr 2023, benefits are maintained and the contract is not in force.
- **Who bears it**: beneficiary. **Money direction**: unclear.
- **Standing**: LITERAL. The fork register (L12) notes Law Art 27(1)(b) "points to the policyowner's side".
- **Evidence**: `ktv-tests-findings.l4:132` (maintained) and `:133` (NOT in force); src 600-620.
- **Plain-English test of surprise**: A family expects a death in the grace period to be covered; the wording says both yes and no.

### VN-24 X6 — Lapse backdated months before the grace period starts
- **Class**: T1
- **Scenario**: From contract year 5, grace starts when the account reaches zero, but lapse still dates "từ ngày đến hạn đóng phí" (from the due date), which may be months earlier and which a flexible-premium year does not define. Account dry on 1 Jun 2027: grace from 1 Jun, lapse from 15 Mar 2027.
- **Who bears it**: insured / beneficiary. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `ktv-tests-findings.l4:143-144`; also `ktv-tests-general.l4:305` (no due date, refused); src 594-595, 607-614.
- **Plain-English test of surprise**: A customer expects lapse no earlier than the grace period ends; it reaches back before the grace began.

### VN-24 X7 — No deadline for the free-look refund
- **Class**: T1
- **Scenario**: A policyholder who cancels on day 10 of the free look is owed a refund, but the Company has no time limit to pay it.
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: LITERAL (reading only; the duty has no deadline).
- **Evidence**: no assertion (reading only); src 387-400.
- **Plain-English test of surprise**: A customer who cancels expects the money back within days; no date is set.

### VN-24 X8 — ICU benefit paid where TPD excluded, same crash
- **Class**: T7 / T2
- **Scenario**: The ICU, premium-support, screening, loyalty and maturity benefits have no exclusions. After a drink-driving crash with self-injury, 7 days in ICU pays 300 million while TPD from the same crash is excluded.
- **Who bears it**: insurer. **Money direction**: against the insurer.
- **Standing**: LITERAL.
- **Evidence**: `ktv-tests-findings.l4:169` (ICU `payable` 300 million) and `:170` (TPD excluded); src 190-227, 691-762.
- **Plain-English test of surprise**: One expects the same exclusions across one product's benefits; some benefits have none.

### VN-24 X9 — Cost-of-insurance rate unprinted and changeable
- **Class**: T8 / T11
- **Scenario**: The largest charge, the cost of insurance, has no printed rate or basis beyond "căn cứ theo tuổi, giới tính" (by age and sex), and every charge may be changed with the Ministry's approval and 3 months' notice, so the account values are set by the insurer.
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `ktv-tests-general.l4:200`, `#ASSERT REFUSED the cost-of-insurance rates … are not printed`; src 1719-1720, 1786-1788.
- **Plain-English test of surprise**: A customer expects to see the price of cover; it is not printed and can change.

### VN-24 X10 — Excluded-death account value has no payee
- **Class**: T13 silent consequence / T7
- **Scenario**: Art 23(a)'s last paragraph pays "Giá trị tài khoản hợp đồng" (the account value) on an excluded death without saying to whom, and overlaps (ii)'s payment to innocent beneficiaries; e.g. where a beneficiary forges a document.
- **Who bears it**: beneficiary. **Money direction**: unclear.
- **Standing**: CONTESTED (fork F22 reads (ii)'s shares for the fraud case and the last paragraph for a death not paid at all).
- **Evidence**: no assertion (reading only); src 703-725.
- **Plain-English test of surprise**: A family expects to know who gets the account value; the clause names no one.

### VN-24 X11 — Disability certificate literally required for every claim
- **Class**: T12 / T5
- **Scenario**: Art 26(b) lists an impairment certificate from the Medical Assessment Council with no condition; read literally, a cancer claim or a death claim needs one too.
- **Who bears it**: insured / beneficiary. **Money direction**: against the claimant.
- **Standing**: CONTESTED (fork F23 takes TPD claims only).
- **Evidence**: no assertion (reading only); src 869-884.
- **Plain-English test of surprise**: A cancer claimant expects to file medical records, not a disability assessment; the list demands both.

### VN-24 X12 — Late-payment interest tied to nonexistent advances
- **Class**: T5 / T8
- **Scenario**: Late claim payments (e.g. paid on day 45) earn interest at the rate for "các khoản tạm ứng từ giá trị hợp đồng" (advances from the contract value), but the document offers no such advances.
- **Who bears it**: beneficiary. **Money direction**: against the claimant (inferred).
- **Standing**: LITERAL (reading only).
- **Evidence**: no assertion (reading only); the related accrual gap is `ktv-tests-general.l4:371` (`#ASSERT REFUSED Article 27 does not say how interest on a late payment accrues`); src 909-917.
- **Plain-English test of surprise**: A claimant paid late expects a stated interest rate; the reference points to nothing.

### VN-24 X13 — Occupational HIV cover withheld once treatment exists
- **Class**: T6
- **Scenario**: Annex 7(30) withholds the occupational-HIV benefit "nếu đã có phương pháp điều trị hiệu quả bệnh HIV" (if effective treatment exists). The encoder notes, as outside knowledge, unverified, that effective antiretroviral therapy exists; on that reading a nurse infected by a needle-stick gets nothing.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL, with the encoder's hedge "outside knowledge, unverified" on whether the condition is already met.
- **Evidence**: no assertion (reading only); src 3205-3206.
- **Plain-English test of surprise**: A health worker buying this cover expects it to pay on infection; on that reading it never can.

### VN-24 X14 — One predeceased beneficiary diverts everyone's shares
- **Class**: T13 payee diversion / T5
- **Scenario**: Art 28(b)(ii) sends the death benefit to the policyowner if "bất kỳ" (any) beneficiary died before or with the insured. With two beneficiaries at 50% and one predeceased, the surviving beneficiary's share also goes to the policyowner.
- **Who bears it**: beneficiary. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `ktv-tests-findings.l4:174`, EQUALS `the policyowner, as payee`; src 942-946.
- **Plain-English test of surprise**: A surviving beneficiary expects to keep that share; it is diverted.

### VN-24 X15 — Large first premium turns death benefit into refund
- **Class**: T7 / T6
- **Scenario**: Art 29's three sentences conflict when the first premium exceeds 100 million: refund it, pay the temporary benefit, and no refund if the benefit is paid. As encoded, an accidental death on 5 Mar 2022 with a 101 million first premium gets a refund of 101 million instead of the benefit.
- **Who bears it**: beneficiary. **Money direction**: against the claimant.
- **Standing**: CONTESTED (fork F24 takes "instead", the only reading under which all three sentences hold).
- **Evidence**: `ktv-tests-findings.l4:178`, outcome a refund of 101 million; src 956-975.
- **Plain-English test of surprise**: A customer who pays more expects more interim cover; paying over 100 million removes it.

### VN-24 X16 — Non-disclosure remedies chosen by the Company; one unintelligible
- **Class**: T11 / T5
- **Scenario**: For a non-disclosure that would have meant an exclusion, Art 30(b)(ii) lets the Company choose among three outcomes at its own decision with no criteria; the third, paying "quyền lợi bảo hiểm nằm ngoài giới hạn" (benefits outside the limit), is unintelligible.
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: LITERAL (reading only; the rule returns the three options).
- **Evidence**: no assertion; related `ktv-tests-general.l4:417` (`#ASSERT REFUSED Article 30(b)(i) — the refund`); src 1028-1045.
- **Plain-English test of surprise**: A customer expects a defined consequence; the insurer picks one, and one option has no meaning.

### VN-24 X17 — First premium year and partial-year rates undefined
- **Class**: T5
- **Scenario**: "Năm đóng phí" (premium year) counts 12 months "từ Ngày kỷ niệm hợp đồng" in which the basic premium was paid in full; the first premium year starts on the effective date, not an anniversary, and a partly paid year's allocation rate is undefined.
- **Who bears it**: policyholder. **Money direction**: unclear.
- **Standing**: LITERAL (reading only; premium year is an input).
- **Evidence**: no assertion (reading only); src 556-581, 1411-1413.
- **Plain-English test of surprise**: A customer expects to know how much of each premium is invested; a part-paid year has no rate.

### VN-24 X18 — Claim deadline expires before the illness qualifies
- **Class**: T1
- **Scenario**: Art 25's 12-month bar runs from "ngày được chẩn đoán" (diagnosis), but loss of speech needs 12 continuous months and Kawasaki disease an echo no sooner than 12 months after onset. Onset 10 Jan 2024: last day to claim 10 Jan 2025; a claim on 11 Jan 2025 is late.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: CONTESTED (the encoder notes it holds "unless the diagnosis date is the day the definition is met").
- **Evidence**: `ktv-tests-findings.l4:185-186`; src 860-863, 3236, 3348-3354.
- **Plain-English test of surprise**: A patient expects to claim once the illness qualifies; the deadline can pass first.

### VN-24 X19 — Loyalty bonus gap between valuation and allocation
- **Class**: T1 / T13 silent consequence
- **Scenario**: Art 8 values the loyalty bonus on the last day of the contract year and allocates it on the anniversary; a lapse or claim between the two (e.g. a death on the anniversary) is unprovided for.
- **Who bears it**: beneficiary. **Money direction**: unclear.
- **Standing**: LITERAL (reading only; fork F19 takes the last-day value).
- **Evidence**: no assertion (reading only); src 344-352.
- **Plain-English test of surprise**: A family expects an earned bonus to be paid; the one-day gap leaves it uncertain.

### VN-24 X20 — No-lapse guarantee cannot apply until it ends
- **Class**: T6 / T5
- **Scenario**: Art 9's no-lapse guarantee for years 1-4 requires the premiums "của 4 Năm hợp đồng đầu tiên" (of the first four years) paid in full; read literally, in year 2 it cannot yet be met, so it cannot apply until it has ended.
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: CONTESTED (fork F20 takes "premiums due so far").
- **Evidence**: no assertion (reading only); src 354-358.
- **Plain-English test of surprise**: A customer expects the guarantee during years 1-4; literally it works only after them.

### VN-24 X21 — Exclusion lists differ: race kills, death paid, TPD not
- **Class**: T7 / T2
- **Scenario**: Dangerous sports exclude TPD but not death; medicine without a prescription excludes cancer and CI but not TPD; fighting excludes TPD but not cancer or CI. A fatal motor race in 2030 pays the death benefit, while TPD from the same race would be excluded.
- **Who bears it**: insured. **Money direction**: unclear.
- **Standing**: LITERAL.
- **Evidence**: `ktv-tests-findings.l4:190` (TPD excluded) and `:191` (`the death benefit is paid`); `ktv-tests-exclusions.l4` near misses; src 691-762.
- **Plain-English test of surprise**: One expects a worse outcome to be no less excluded than a better one; surviving disabled is excluded, dying is paid.

### VN-24 X22 — "Dangerous activities" defined only by example
- **Class**: T5 / T2
- **Scenario**: Art 23(b)(vi) names dangerous activities only by example ("như", such as) and never defines "nguy hiểm" (dangerous); whether a TPD in a trail run is excluded cannot be answered.
- **Who bears it**: insured. **Money direction**: unclear.
- **Standing**: LITERAL.
- **Evidence**: `ktv-tests-benefits.l4:231`, `#ASSERT REFUSED Article 23(b) — the TPD benefit is excluded …`; src 743-745.
- **Plain-English test of surprise**: A runner expects to know whether a hobby voids cover; the list is open-ended.

### VN-24 X24 — Withdrawal removes the guarantee, with no grace to replace it
- **Class**: T6 / T13 silent consequence
- **Scenario**: A basic-account withdrawal (allowed from the 2nd anniversary) removes the no-lapse guarantee in years 3-4, and before year 5 there is no grace period for an account that cannot meet the deduction. In year 3 with the account dry on 15 Aug 2024, the document does not say whether the contract lapses; as encoded it stays in force.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL.
- **Evidence**: `ktv-tests-findings.l4:195` (guarantee FALSE) and `:198` (in force); src 354-370, 415, 584-595.
- **Plain-English test of surprise**: A customer expects a withdrawal to have stated consequences; it leaves the contract's status undefined.

### VN-24 X25 — Sum insured cut "correspondingly" with no measure
- **Class**: T5
- **Scenario**: After an 80 million withdrawal the sum insured is reduced "tương ứng" (correspondingly) without saying to what.
- **Who bears it**: insured. **Money direction**: unclear.
- **Standing**: LITERAL (fork F25 left undecided).
- **Evidence**: `ktv-tests-general.l4:252`, `#ASSERT REFUSED … does not say what the sum insured is reduced to`; src 434-437.
- **Plain-English test of surprise**: A customer expects to know the new cover after a withdrawal; no rule gives it.

### VN-24 X26 — Misstated age or sex "adjusted" with no method
- **Class**: T13 silent consequence / T5
- **Scenario**: A misstated age or sex is "adjusted" (sum insured, premium, cost of insurance) with no method stated.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL.
- **Evidence**: `ktv-tests-general.l4:427`, `#ASSERT REFUSED Article 40 does not say how … are adjusted`; src 1265-1268.
- **Plain-English test of surprise**: A customer expects a formula for correcting an error; there is none.

### VN-24 X29 — Termination refund ignores debts; surrender deducts them
- **Class**: T7 / T4
- **Scenario**: When early-stage advances reach 100%, the termination refund (Art 24(a)(iii)) does not deduct debts, while the surrender value on request (24(c)) does. With debts of 10 million, the test gives 50 million for the first and 240 million for the second; the figures differ in base, and the point is the treatment of debts (inferred).
- **Who bears it**: insurer (inferred). **Money direction**: against the insurer (inferred).
- **Standing**: LITERAL.
- **Evidence**: `ktv-tests-findings.l4:202-203`; src 789-794, 843-845.
- **Plain-English test of surprise**: One expects outstanding debts to come off every exit payment; one route skips them.

### VN-24 X30 — ICU tier requirement has no foreign equivalent
- **Class**: T5
- **Scenario**: Art 3(a)(ii) needs an ICU in a hospital "tuyến tỉnh trở lên hoặc tương đương" (provincial tier or above, or equivalent), a Vietnamese tier with no stated foreign equivalent, though Annex 1 covers foreign hospitals; an ICU stay abroad after an accident is uncertain.
- **Who bears it**: insured. **Money direction**: against the claimant (inferred).
- **Standing**: LITERAL (reading only; an input).
- **Evidence**: no assertion (reading only); src 217-219, 1662-1670.
- **Plain-English test of surprise**: A traveller expects foreign ICU care to count, as the hospital definition suggests; the tier test may exclude it.

### VN-24 X31 — Three-year limit runs from an unfixed dispute date
- **Class**: T1 / T5
- **Scenario**: Art 41's three-year limitation period runs from "ngày xảy ra tranh chấp" (the day the dispute arose), which nothing in the document fixes.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL (reading only).
- **Evidence**: no assertion (reading only); src 1277-1278.
- **Plain-English test of surprise**: A claimant expects a definite start for the limitation clock; none is given.

#### VN-24 row summary
- **Findings in section 4**: 28 (X1-X22, X24-X26, X29-X31; the NOTES say X23, X27 and X28 were merged into others while drafting).
- **Most counterintuitive**: (X21) a fatal race pays the death benefit while disability from the same race is excluded; (X15) a first premium over 100 million turns an accidental-death benefit into a 101 million refund; (X18) a 12-month claim bar that expires before illnesses defined by 12 months of symptoms can qualify.
- **Matches in this group**: X3 = VN-11 16 and VN-14 X10 (no floor); X12 = VN-14 X21 (interest at the rate for advances the document does not offer; near-identical wording); X9 = VN-13 17 (insurance-charge cap or rate set by the insurer); X10 relates to VN-14 X9 (account value on an excluded death with no payee); X11 relates to VN-14 X20 (claim documents); X26 relates to VN-11 8 and VN-13 9 (misstated age); X7 relates to VN-13 26 (no Company deadline for the free-look refund); X20 relates to VN-13 22 (a clock that cannot start).

## VN-25 AIA An Phúc Trọn Đời Ưu Việt (whole-life universal life)

### VN-25 FD1 — Two maturity dates a year apart
- **Class**: T7 / T1
- **Scenario**: Art 1.32 makes every "tuổi" the insurance age, reached only on an anniversary, so 1.9's "anniversary after the insured reaches 100" falls a year after Art 4's "anniversary after the 100th birthday". Born 15 Jun 1980, effective 31 Jan 2021: maturity 31 Jan 2081 by Art 4, 31 Jan 2082 by 1.9 with 1.32.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: CONTESTED (fork F1 takes Art 4).
- **Evidence**: `aptduv-findings.l4:95-96`; src 287-288, 546-548, 648-650.
- **Plain-English test of surprise**: A customer expects one maturity date; the contract gives two.

### VN-25 FD2 — Policyholder's minimum age becomes the insured's age
- **Class**: T5 / T7
- **Scenario**: Art 1.32 says every "tuổi" is the insured's insurance age, so read literally the policyholder's 18-year minimum tests the insured: a 16-year-old policyholder insuring a 40-year-old qualifies.
- **Who bears it**: unclear. **Money direction**: no money.
- **Standing**: CONTESTED (fork F2 takes the policyholder's own age and calls the literal reading "absurd").
- **Evidence**: `aptduv-findings.l4:108` (literal: qualifies) and `:109` (taken: does not); src 236, 546-548.
- **Plain-English test of surprise**: One expects an adult-only rule to test the buyer's age; literally it tests someone else's.

### VN-25 FD3 — Incontestability clause protects nothing
- **Class**: T6
- **Scenario**: Art 6.3's exception removes every intentional misstatement, the only kind 6.2 gives a remedy for; what remains (innocent misstatements) had no remedy to bar. An intentional misstatement can be contested ten years on (1 Feb 2031).
- **Who bears it**: beneficiary / policyholder. **Money direction**: against the claimant.
- **Standing**: LITERAL; under the alternative timing in fork F37 it "would never protect a death claim".
- **Evidence**: `aptduv-findings.l4:118-120` (contestable after ten years; innocent misstatement has no remedy, EMPTY); src 709-760.
- **Plain-English test of surprise**: A customer expects a two-year contest bar to give certainty; it bars nothing that was otherwise contestable.

### VN-25 FD4 — Pre-existing-condition exclusion lasts forever
- **Class**: T2 / T1
- **Scenario**: The pre-existing-cause exclusion has no time limit and outlives the incontestability clause. A death in 2060 from a condition existing a month before the effective date pays only the account value, 50,000,000, against 550,000,000 otherwise.
- **Who bears it**: beneficiary. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `aptduv-findings.l4:128-129`; src 1141-1145, 1151-1157.
- **Plain-English test of surprise**: A customer expects an old condition to stop mattering after decades; it never does.

### VN-25 FD5 — Excluded death pays more than covered death
- **Class**: T4 / T7
- **Scenario**: Art 7.5 deducts a cancer advance only from a 7.2 or 7.3 benefit; an 8.1-excluded death pays the account value with nothing deducted. Account value 600,000,000, sum insured 500,000,000, cancer advance 125,000,000: a covered death pays 475,000,000, a death in war 600,000,000.
- **Who bears it**: insurer. **Money direction**: against the insurer.
- **Standing**: LITERAL (fork F10 takes the literal reading).
- **Evidence**: `aptduv-findings.l4:140-141`; src 1017-1018, 1151-1157.
- **Plain-English test of surprise**: One expects an excluded death to pay no more than a covered one; here it pays 125,000,000 more.

### VN-25 FD6 — Accidental-death cap drafted as all-or-nothing condition
- **Class**: T4 / T5
- **Scenario**: The 10 billion accidental-death limit is written as a condition: a 500,000,000 benefit for an insured who already received 9,800,000,000 elsewhere pays 200,000,000 read as a cap, and 0 read as written.
- **Who bears it**: beneficiary. **Money direction**: against the claimant (on the literal reading).
- **Standing**: CONTESTED (fork F6 takes the cap, citing Law Art 24).
- **Evidence**: `aptduv-findings.l4:148-149`; src 969, 977, 984-987.
- **Plain-English test of surprise**: A customer expects a limit to cut the payment to the room left; read as written it cancels the payment.

### VN-25 FD7 — Cancer claim time-barred before diagnosis
- **Class**: T1
- **Scenario**: Art 1.30 dates a cancer from the first signs that would send an ordinary person to a doctor, and Art 28 runs twelve months from that date. Symptoms 1 Mar 2023, diagnosis 1 May 2024: the last day to claim was 1 Mar 2024, so a claim on 2 May 2024 is out of time.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LAW. Law Art 30(2) runs the period from knowledge.
- **Evidence**: `aptduv-findings.l4:177-178`; src 472-474, 2280-2281.
- **Plain-English test of surprise**: A patient expects the clock to start at diagnosis; it can expire before it.

### VN-25 FD8 — Disability certification delay outlasts claim deadline
- **Class**: T1
- **Scenario**: Art 1.29(b) forbids certifying a disability within six months; Art 28 bars the claim twelve months after it. Disability 1 Mar 2023, certificate 2 Mar 2024: a valid total and permanent disability, and a claim out of time.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `aptduv-findings.l4:196-197`; src 462-463, 2280.
- **Plain-English test of surprise**: A claimant expects a valid certificate to support a claim; a slow medical council makes it useless.

### VN-25 FD9 — Bigger first premium, smaller temporary-cover payout
- **Class**: T6 / T4
- **Scenario**: Above 100,000,000 of first premium, the temporary-cover benefit is replaced by a refund less medical costs. An accidental death with 99,000,000 paid yields 100,000,000; with 100,500,000 paid, the benefit is 0 and the refund 98,500,000.
- **Who bears it**: beneficiary. **Money direction**: against the claimant.
- **Standing**: CONTESTED (fork F34 takes "replace" over "add").
- **Evidence**: `aptduv-findings.l4:217-219`; src 655-667, 674-675.
- **Plain-English test of surprise**: A customer expects paying more to buy at least as much cover; it buys less.

### VN-25 FD10 — Withdrawal cap locks up the accumulation account
- **Class**: T6 / T7
- **Scenario**: Art 9.1 caps a withdrawal at 80% of the basic account, though 9.2 takes it from the accumulation account first. With 300,000,000 in accumulation and 10,000,000 basic, 8,000,000 may be withdrawn and 8,000,001 may not.
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `aptduv-findings.l4:234-235`; src 1255, 1257-1259.
- **Plain-English test of surprise**: A saver expects to reach the money in the savings account; the cap is measured on a different account.

### VN-25 FD11 — Almost every withdrawal cuts cover by an unstated amount
- **Class**: T5
- **Scenario**: Art 9.3 reduces the sum insured "tương ứng" (correspondingly) when the basic account falls below the sum insured after a withdrawal, which is the ordinary state of a contract; no measure is given (the 8,000,000 withdrawal of FD10 triggers it).
- **Who bears it**: insured. **Money direction**: unclear.
- **Standing**: LITERAL (fork F19 declined).
- **Evidence**: `aptduv-findings.l4:243` (triggered) and `:244` (`#ASSERT REFUSED` amount); `aptduv-tests.l4:788`; src 1265-1267.
- **Plain-English test of surprise**: A customer expects to know how much cover a withdrawal costs; no rule says.

### VN-25 FD12 — Monthly deduction taken twice when basic account short
- **Class**: T4
- **Scenario**: Read literally, Art 16 takes the monthly deduction from the basic account and again from the accumulation account when the basic one is short. Basic 100,000, deduction 180,000: literal result −80,000 basic and 1,820,000 accumulation; taken reading 0 and 1,920,000.
- **Who bears it**: policyholder. **Money direction**: against the claimant (literal reading).
- **Standing**: CONTESTED (fork F17 takes the shortfall from the accumulation account once).
- **Evidence**: `aptduv-findings.l4:265-266`; src 1733, 1754-1755.
- **Plain-English test of surprise**: A customer expects one charge per month; the literal wording charges twice.

### VN-25 FD13 — Free-look window may run before delivery
- **Class**: T1 / T3
- **Scenario**: The free-look clock's start is ambiguous; counted from issue, delivery time eats the 21 days. Issued 1 Mar, received 15 Mar, refused 30 Mar 2023: in time from receipt, out of time from issue.
- **Who bears it**: policyholder. **Money direction**: against the claimant (on the issue reading).
- **Standing**: CONTESTED (fork F20 takes the later of issue and receipt); the Law (Art 35) counts from receipt.
- **Evidence**: `aptduv-findings.l4:280-281`; src 1888-1889.
- **Plain-English test of surprise**: A buyer expects 21 days to review a contract in hand; one reading counts days before it arrives.

### VN-25 FD14 — Bonus table says "6" in figures, "five" in words
- **Class**: T7
- **Scenario**: The last row of the loyalty-bonus table reads "Năm hợp đồng thứ 6 (năm)": year 6 by the numeral, year 5 by the word. With interest of k × 100,000 in year k, the base recorded on anniversary 10 is 2,000,000 on the reading taken and 2,250,000 if the window starts at year 5.
- **Who bears it**: policyholder. **Money direction**: unclear.
- **Standing**: CONTESTED (fork F26 takes 6).
- **Evidence**: `aptduv-findings.l4:294-296`; src 1111-1113.
- **Plain-English test of surprise**: A customer expects figures and words to agree; they name different years.

### VN-25 FD15 — One beneficiary's crime costs all beneficiaries
- **Class**: T2 / T3
- **Scenario**: A beneficiary killing the insured is insurance fraud under 1.33, and 8.1 then excludes the death benefit for everyone; 8.2 saves innocent beneficiaries only for the accidental benefit. The death pays the account value, 50,000,000, against 550,000,000.
- **Who bears it**: beneficiary (the innocent ones). **Money direction**: against the claimant.
- **Standing**: LAW. Law Art 40(2) requires payment to the other beneficiaries.
- **Evidence**: `aptduv-findings.l4:306`; src 565-567, 1137, 1185-1188.
- **Plain-English test of surprise**: An innocent co-beneficiary expects a share; another's crime wipes it out.

### VN-25 FD16 — Late interest at nonexistent rate, no reparation deadline
- **Class**: T5 / T1
- **Scenario**: Late-payment interest is pegged to "khoản tạm ứng từ giá trị hợp đồng" (advances from the contract value), which this product does not have; Art 29 does not say how it accrues; and if the Company neither settles in 30 days nor with interest later, nothing sets a deadline. A claim settled four days late has no computable interest.
- **Who bears it**: beneficiary. **Money direction**: against the claimant (inferred).
- **Standing**: LITERAL.
- **Evidence**: `aptduv-tests.l4:1128` (`#ASSERT REFUSED`); `aptduv-findings.l4:370` (trace: duty standing after 400 days); src 2305-2309.
- **Plain-English test of surprise**: A claimant paid late expects interest at a stated rate; the rate refers to nothing.

### VN-25 FD17 — Terms used but never defined, or inconsistent
- **Class**: T5
- **Scenario**: "NĐBH", "chúng tôi", "bệnh hiểm nghèo", "điều kiện chuẩn", "thời gian đóng phí bắt buộc", "Bác sĩ" and "Bên mua được bảo hiểm" are undefined; "Ngày hiệu lực hợp đồng" sits beside the defined "Ngày có hiệu lực của hợp đồng"; 6.5's heading names the policyholder's duty for a clause binding the Company.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL (reading only).
- **Evidence**: no assertion (reading only); src 799, 997-1003, 1325, 1708, 2087, 2228, 2429.
- **Plain-English test of surprise**: A reader expects defined terms to be used consistently; several are not defined at all.

### VN-25 FD18 — Company discretion with no criteria
- **Class**: T11
- **Scenario**: Withdrawal approval; minimum withdrawal and min/max sum insured "tại từng thời điểm" (from time to time); the ceiling above which evidence can be demanded despite 11.1; the remedy under 6.2 and 22.3; a premium increase or sum-insured cut under 23.1; further documents and examinations (27.3, 27.4): all at the Company's choice.
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: LITERAL (reading only; the rules return the options open).
- **Evidence**: no assertion (reading only); src 723-749, 1254-1259, 1286, 1300, 1347-1350, 1944-1959, 2011-2012, 2267-2276.
- **Plain-English test of surprise**: A customer expects stated rules; the insurer decides case by case.

### VN-25 FD19 — Company keeps premiums on avoiding the contract
- **Class**: T3
- **Scenario**: Art 6.2 lets the Company keep the premiums when it avoids a contract for intentional misstatement.
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: LAW. Law Art 22(2) requires a refund less reasonable costs.
- **Evidence**: no assertion (reading only); src 715-722.
- **Plain-English test of surprise**: A policyholder expects premiums back, less costs, when a contract is undone; the wording keeps them.

### VN-25 FD20 — Organisation's account value paid to its "heirs"
- **Class**: T5 / T13 silent consequence
- **Scenario**: Art 22.1 pays an organisation policyholder's account value to its "người thừa kế hợp pháp" (lawful heirs); an organisation (e.g. a dissolved company) has none. Civil Code rules on successors to a legal person are outside knowledge, unverified.
- **Who bears it**: policyholder. **Money direction**: unclear.
- **Standing**: LITERAL (reading only).
- **Evidence**: no assertion (reading only); src 1919-1925.
- **Plain-English test of surprise**: A corporate buyer expects a successor to be named; the clause uses a word for persons.

### VN-25 FD21 — Child's cancer advance exceeds the death benefit
- **Class**: T4 / T7
- **Scenario**: The 25% cancer advance is paid without the child's reduction, while a death under age 1 pays 20%. Cancer at insurance age 0 pays 125,000,000; the death benefit it comes off is 100,000,000; what follows on death is not said.
- **Who bears it**: insurer (inferred). **Money direction**: unclear.
- **Standing**: LITERAL (fork F8 takes the literal reading).
- **Evidence**: `aptduv-findings.l4:330-331`, and `:332` `#ASSERT REFUSED` on the total; src 926-940, 993, 1017-1018.
- **Plain-English test of surprise**: One expects an advance to be no larger than the benefit it advances; here it is larger.

### VN-25 FD22 — Overpayments the allocation rules do not place
- **Class**: T13 silent consequence
- **Scenario**: A payment above the instalment due before the year's premiums are paid in full, and accumulation premium above the 1.16 cap, are not placed: a monthly payer paying 20,000,000 against a 12,000,000 instalment has no answer.
- **Who bears it**: policyholder. **Money direction**: unclear.
- **Standing**: LITERAL (fork F16 declined).
- **Evidence**: `aptduv-tests.l4:889, 891`, both `#ASSERT REFUSED`; src 358-365, 1534-1537, 1583-1589.
- **Plain-English test of surprise**: A payer expects extra money to be credited somewhere; no rule says where.

### VN-25 FD23 — Second cancer not addressed
- **Class**: T13 silent consequence
- **Scenario**: The cancer benefit does not say whether a second cancer, after one already paid (125,000,000), is paid again.
- **Who bears it**: insured. **Money direction**: unclear.
- **Standing**: LITERAL (fork F9 declined).
- **Evidence**: `aptduv-tests.l4:655`, `#ASSERT REFUSED 7.5 — the cancer benefit … cancer paid 125000000 …`; src 993-996.
- **Plain-English test of surprise**: A survivor expects to know whether a recurrence is covered; the clause is silent.

### VN-25 FD24 — Amount needed to cure a year-5 grace unstated
- **Class**: T5 / T12
- **Scenario**: From year 5, grace opens on an account shortfall, and Art 15.3 lapses the contract unless "khoản phí bảo hiểm theo yêu cầu" (the premium required) is paid, without saying what is required.
- **Who bears it**: policyholder. **Money direction**: against the claimant (inferred).
- **Standing**: LITERAL (reading only; the payment date is an input).
- **Evidence**: no assertion (reading only); src 1665-1666, 1676-1678.
- **Plain-English test of surprise**: A customer in grace expects to be told what to pay to stay covered; the clause names no sum.

### VN-25 FD25 — Illness death in temporary cover: no benefit, no refund rule
- **Class**: T13 silent consequence / T6
- **Scenario**: A death by illness during temporary cover (10 Mar 2021, 20,000,000 first premium) gets no benefit, and nothing says whether the premium is returned; an accident or suicide is addressed.
- **Who bears it**: beneficiary. **Money direction**: against the claimant (inferred).
- **Standing**: LITERAL.
- **Evidence**: `aptduv-tests.l4:575` (benefit 0) and `:576` (`#ASSERT REFUSED Article 5 — the first premiums refunded`); src 655-679.
- **Plain-English test of surprise**: A family expects premium back at least; the text says nothing.

### VN-25 FD26 — Refund on age correction can be negative
- **Class**: T4
- **Scenario**: The Art 23.3 refund (premiums less debts, medical costs, withdrawals and benefits paid) can go below zero, and nothing says who then owes what.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL (reading only; the rule refuses a negative refund).
- **Evidence**: no assertion in the findings or tests modules (reading only); src 2040-2046.
- **Plain-English test of surprise**: A customer expects a refund of at least nil; the formula can produce a debt.

### VN-25 FD27 — Loyalty bonus counts one year's interest five times
- **Class**: T4 / T7
- **Scenario**: The five bonus windows overlap, so a year's interest is counted up to five times, year 6 five times: interest of 1,000,000 in year 6 only yields a 10th-anniversary bonus of 2,500,000.
- **Who bears it**: insurer. **Money direction**: against the insurer.
- **Standing**: CONTESTED (fork F27 takes the literal sum, as written; the alternative counts each year once).
- **Evidence**: `aptduv-findings.l4:345`; src 1076-1113.
- **Plain-English test of surprise**: One expects each year's interest to count once; it counts five times.

### VN-25 FD28 — Claim form accepts a certificate the definition rejects
- **Class**: T7 / T12
- **Scenario**: Art 27.1 names a lawful foreign medical organisation approved by the Company as a certifier; 1.29(b) accepts only a provincial council or an approved independent organisation. A 90% rating by an approved foreign organisation is not a 1.29 disability.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `aptduv-findings.l4:364`, `#ASSERT NOT 1.29 — the disability is total and permanent` `a disability certified abroad`; src 460-462, 2215-2222.
- **Plain-English test of surprise**: A claimant who follows the claims list expects the certificate to count; the definition refuses it.

#### VN-25 row summary
- **Findings in section 4**: 28 (FD1 to FD28). FD17-FD20, FD24 and FD26 are reading only.
- **Most counterintuitive**: (FD5) a death in war pays 600,000,000 while a covered death pays 475,000,000; (FD9) paying 100,500,000 rather than 99,000,000 of first premium turns a 100,000,000 benefit into a 98,500,000 refund; (FD7) a cancer claim out of time before the cancer is diagnosed.
- **Matches in this group**: FD9 = VN-24 X15 (same AIA temporary-cover cliff above 100 million of first premium); FD25 = VN-14 X2 second limb (illness death in temporary cover, premium unaddressed); FD16 = VN-24 X12 and VN-14 X21 (interest at the rate for advances the product lacks); FD11 = VN-24 X25 (sum insured cut "tương ứng" with no measure); FD7 and FD8 = VN-24 X18 (claim bar against a definition that takes months to meet); FD12 = VN-13 1 and VN-14 X6 (a deduction taken twice); FD15 relates to VN-14 X9 (one beneficiary's crime defeats all); FD26 = VN-11 16, VN-14 X10, VN-24 X3 (no floor); FD3 relates to VN-11 8 and VN-13 9 (incontestability that does not protect); FD4 relates to VN-11 8 (no time limit on a ground to refuse); FD19 relates to VN-11 5 and VN-13 6 (what is returned on avoidance); FD27 relates to VN-24 X19 (loyalty-bonus mechanics); FD18 = VN-11 7, VN-14 X12 (discretion without criteria).

## VN-26 Prudential term life with personal accident benefit (summary notes and Rules and Terms)

Finding ids are the encoder's (`F-01` to `F-22`); the fork register uses the same `F-NN` form for different items, so forks are written "fork F-NN" below.

### VN-26 F-01 — Accidental death after day 180 paid by nothing
- **Class**: T6 / T7
- **Scenario**: Art 8.1 pays a death by Accident within 180 days; 8.7 a death "không do Tai nạn" (not by accident). An Accident on 10 Mar 2027 and death on day 181 is neither: no benefit, no refund. The same death from illness gets 30,000,000 (8.7); the same Accident while drunk, 30,000,000 (11.2, no 180-day limit).
- **Who bears it**: beneficiary. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `pru-tests-findings.l4:26` (nothing), `:29`, `:31`; src 419, 516, 725-730.
- **Plain-English test of surprise**: A family expects a sober accident victim to fare no worse than a drunk one; here it gets nothing.

### VN-26 F-02 — Claiming injury maximum forfeits the death benefit
- **Class**: T6 / T1
- **Scenario**: Paying Art 8.2's maximum ends the contract, and 8.1 needs the death while in force. Lose both legs on 10 Mar 2027, be paid 1,000,000,000 (contract ends 1 Apr 2027), die of the same Accident on day 40: nothing; had the claim waited, 8.1 pays 1,000,000,000 (300% on a scheduled flight).
- **Who bears it**: beneficiary. **Money direction**: against the claimant.
- **Standing**: CONTESTED (fork F-03, labelled "Insurer-favourable"; 8.10 "presupposes the opposite").
- **Evidence**: `pru-tests-findings.l4:37-39`, `:43`, `:44`; src 419-420, 442-443, 535-537, 990-991.
- **Plain-English test of surprise**: A claimant expects an injury payout not to cancel the death benefit; claiming promptly loses it.

### VN-26 F-03 — Accidental blindness or paralysis pays less than illness
- **Class**: T6 / T2
- **Scenario**: Loss of an eye means loss of the eyeball; paralysis appears only in 1.17; 8.8 covers total and permanent disability only "không do Tai nạn". Total blindness with eyeballs intact, or paraplegia, pays the premiums back (30,000,000) if caused by illness, and nothing if caused by an Accident (unless a fracture row applies).
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `pru-tests-findings.l4:49-56`, five assertions; src 201-202, 1033.
- **Plain-English test of surprise**: A buyer of accident cover expects accidental blindness to be covered; it falls between the two benefits.

### VN-26 F-04 — Fingers itemised pay more than the whole hand
- **Class**: T4 / T7
- **Scenario**: Annex 1 gives thumb 15%, each finger 5%, all the fingers of one hand 25%, and 8.2 adds the rates of several injuries. The same loss pays 250,000,000 as one row and 350,000,000 itemised.
- **Who bears it**: insurer. **Money direction**: against the insurer.
- **Standing**: LITERAL.
- **Evidence**: `pru-tests-findings.l4:62-63`; src 438-439, 1028-1030.
- **Plain-English test of surprise**: One expects the whole to be worth at least the sum of its parts; here it is worth less.

### VN-26 F-05 — Youngest child's fracture cap has no ceiling
- **Class**: T4 / T7
- **Scenario**: The fracture and burn cap is 50% of the sum insured under age 6, but the lesser of 100% and 250 million from 6 to 18 and of 100% and 500 million from 18. On a 2 billion sum insured, the caps are 1,000,000,000 for a 5-year-old, 250,000,000 for a 10-year-old and 500,000,000 for an adult.
- **Who bears it**: insurer. **Money direction**: against the insurer.
- **Standing**: LITERAL.
- **Evidence**: `pru-tests-findings.l4:70-72`; src 470-476.
- **Plain-English test of surprise**: One expects the youngest band to have the lowest cap; above 500 million sum insured it has the highest.

### VN-26 F-06 — Ankle fracture fits two table rows
- **Class**: T7 / T5
- **Scenario**: Annex 3 lists "Mắt cá chân" (ankle) at 15% and leg bones including tibia and fibula at 30%; the encoder notes that an ankle fracture is a fracture of the tibia or fibula (outside knowledge, unverified). The same break pays 150,000,000 or 300,000,000. Elbow and arm bones overlap the same way.
- **Who bears it**: insured. **Money direction**: unclear.
- **Standing**: CONTESTED (the document does not say which row governs).
- **Evidence**: `pru-tests-findings.l4:78-79`; src annex 3 (1063-1088).
- **Plain-English test of surprise**: A claimant expects one fracture to have one rate; it has two.

### VN-26 F-07 — Overlapping rows for kidneys and burns
- **Class**: T7 / T4
- **Scenario**: Annex 2 has kidney injury at 5% and both kidneys in one Accident at 10%; with 8.3's addition, both kidneys can be claimed as 20% (200,000,000). Annex 4's burn rows overlap, and a mixed burn (10% third degree, 12% second degree) rates 25% depending on fork F-07, whose literal reading the encoder calls insurer-favourable.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: CONTESTED (forks F-06 and F-07).
- **Evidence**: `pru-tests-findings.l4:85` and `:88` (25%); src 1089-1097.
- **Plain-English test of surprise**: One expects a single injury to be rated once; the table lets it be counted more than once or not reached at all.

### VN-26 F-08 — Document deadline can fall before the event
- **Class**: T1 / T12
- **Scenario**: Art 8.6 pays for an intensive-care stay or transfer with no time limit after the Accident; 10.5 wants documents within 60 days of the Accident. A transfer on day 70 cannot be documented in time; neither 10.4 nor 10.5 says what follows a missed 60 days, while 10.6 allows 12 months to claim.
- **Who bears it**: insured. **Money direction**: against the claimant (inferred).
- **Standing**: LITERAL.
- **Evidence**: `pru-tests-findings.l4:94` (`#ASSERT NOT … the transfer paper can exist before the deadline`) and `:95`; src 508-512, 635.
- **Plain-English test of surprise**: A claimant expects to have time to document an event after it happens; the deadline may pass first.

### VN-26 F-09 — Temporary cover: war gap, refund threshold, illness silence
- **Class**: T7 / T13 silent consequence
- **Scenario**: Art 3 is silent on a non-accidental death during temporary cover, even on the premium. It omits war, so a riot death pays 200,000,000 before the certificate issues and is excluded after (30,000,000 under 11.2). The refund threshold compares premium with 200 million, not the benefit: 150 million paid on a 100 million sum insured returns 100,000,000, no refund.
- **Who bears it**: beneficiary. **Money direction**: unclear (each limb differs).
- **Standing**: LITERAL.
- **Evidence**: `pru-tests-findings.l4:101-105`; `pru-tests.l4:108` (`#ASSERT REFUSED Article 3 …`); src 331-344.
- **Plain-English test of surprise**: A customer expects interim cover to mirror the full contract; it covers some risks better and some not at all.

### VN-26 F-10 — Notes' misdeclaration remedy discretionary; terms keep premium
- **Class**: T7 / T3
- **Scenario**: Notes item 1 gives the insurer one of three outcomes "tùy từng trường hợp" (case by case) with no criterion; Rules and Terms 12.2(a) supplies the criterion and adds that no premium is refunded on cancellation.
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: LAW. Fork LAW-01: Law Art 22(2) allows rescission only for intentional misstatement, with a refund less reasonable costs; "not resolved".
- **Evidence**: `pru-tests-findings.l4:110` (3 options) and `:111` (`… no benefit is paid and no premium is refunded`); src 14-16, 853-864.
- **Plain-English test of surprise**: A policyholder expects premiums back if the contract is cancelled for an error; the terms keep them.

### VN-26 F-11 — Summary notes exclude more than the contract terms
- **Class**: T7 / T2
- **Scenario**: Notes item 3 excludes every benefit for an event "liên quan đến" (related to) a cause, and a crime with no authority's finding; 11.1 excludes only 8.1-8.6, only for a direct cause, and a crime only on an authority's conclusion. A suicide is excluded by the notes and paid 30,000,000 under 8.7; an unproven crime or merely related cause is excluded by the notes and paid under 8.4.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL.
- **Evidence**: `pru-tests-findings.l4:114-121`; src 58-84 (notes), 696-713.
- **Plain-English test of surprise**: A customer reading the summary expects it to match the contract; it excludes cases the contract pays.

### VN-26 F-12 — Summary notes print caps the terms lack
- **Class**: T7
- **Scenario**: The notes cap fractures and burns at the lesser of 100% and 500 million with no age bands; for a 10-year-old on a 1 billion sum insured, the notes say 500,000,000 and the Rules and Terms 250,000,000. Emergency transport is 2 million a year with no 1 million per-Accident limit.
- **Who bears it**: insured (inferred, if relying on the notes). **Money direction**: unclear.
- **Standing**: LITERAL.
- **Evidence**: `pru-tests-findings.l4:124-125`, `:127`, `:130-131`; src 33-42.
- **Plain-English test of surprise**: A parent reading the summary expects 500 million of fracture cover for a child; the contract gives half.

### VN-26 F-13 — Payee list can be empty; insured never paid
- **Class**: T13 silent consequence / T7
- **Scenario**: With a sole beneficiary dead and the policyholder dead, no limb of Art 10.8.2 names a payee. For an organisation policyholder the insured is not on the list: an injured employee's fracture benefit goes to the beneficiary the company named or, with none, to the company, though 8.10 says the insured may claim.
- **Who bears it**: insured / beneficiary. **Money direction**: against the claimant.
- **Standing**: LITERAL (fork F-21).
- **Evidence**: `pru-tests-findings.l4:142` (`#ASSERT REFUSED`), `:145-146` (`the policyholder as recipient`); src 664-693.
- **Plain-English test of surprise**: An injured employee expects the injury benefit; the employer receives it.

### VN-26 F-14 — Late occupation notice lets insurer refuse any claim
- **Class**: T11 / T2
- **Scenario**: Under Art 9, a late notice of a change of occupation lets Prudential decline any later claim, with no causal link and no criterion for its choice among three options; 12.2(d) does the same on leaving Vietnam. Minimums and charges follow "quy định của Prudential tại từng thời điểm"; approvals have no time limit.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL (demonstrated in part; the rest reading only).
- **Evidence**: `pru-tests-findings.l4:152-154`; src 543, 550, 558-559.
- **Plain-English test of surprise**: A customer expects a late notice to matter only if the new job caused the claim; any claim can be refused.

### VN-26 F-15 — Incontestability protects nothing that cancels
- **Class**: T6
- **Scenario**: Art 6's exception covers misstatements that would have led Prudential to decline cover, exactly those 12.2(a) cancels for. What it shuts off after 24 months is a non-material misstatement, which could only bring extra premium. A material misstatement can still be raised in 2034.
- **Who bears it**: beneficiary / policyholder. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `pru-tests-findings.l4:161-162`; src 384-390.
- **Plain-English test of surprise**: A customer expects a contract to become unchallengeable after two years; the clause bars only challenges that could never cancel it.

### VN-26 F-16 — Insurer's slow letter defeats timely reinstatement
- **Class**: T1 / T11
- **Scenario**: Reinstatement must be requested within 24 months of lapse and takes effect on Prudential's confirmation letter, with no time set for the letter; the contract ends after 24 months of lapse. Lapsed 1 Jan 2027, requested 20 Dec 2028 (day 719), letter 5 Jan 2029 (day 735): never effective.
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `pru-tests-findings.l4:168` (request allowed) and `:169` (EQUALS NOTHING); src 817-819, 836-838, 986.
- **Plain-English test of surprise**: A policyholder who applies in time expects reinstatement; the insurer's own delay defeats it.

### VN-26 F-17 — Summary notes not part of the contract
- **Class**: T7
- **Scenario**: Art 2.1 lists the contract's documents; the summary notes are not among them, though the sales illustration is.
- **Who bears it**: policyholder. **Money direction**: unclear.
- **Standing**: LITERAL (reading only).
- **Evidence**: no assertion (reading only); src 297-306.
- **Plain-English test of surprise**: A customer who reads the summary expects it to bind; the contract leaves it out.

### VN-26 F-18 — Ambulance benefit lacks the "in force" words
- **Class**: T13 drafting gap
- **Scenario**: Arts 8.1-8.5, 8.7 and 8.8 each say "trong thời gian Hợp đồng bảo hiểm đang còn hiệu lực" (while the contract is in force); 8.6 does not. The encoding supplies the condition from 12.1(h) and Art 16.
- **Who bears it**: insurer (on the literal reading, inferred). **Money direction**: unclear.
- **Standing**: LITERAL (reading only).
- **Evidence**: no assertion (reading only); src 840-842.
- **Plain-English test of surprise**: One expects every benefit to require cover in force; one is silent.

### VN-26 F-19 — Termination clause cites reinstatement, omits surrender
- **Class**: T7 / T13 drafting slip
- **Scenario**: Art 16's first ground lists "Điều 12.1 d), Điều 12.1 h), Điều 15.1" as early termination; 12.1(h) is reinstatement, which terminates nothing, while 12.1(g), surrender, which does, is not cited.
- **Who bears it**: unclear. **Money direction**: no money.
- **Standing**: LITERAL (reading only).
- **Evidence**: no assertion (reading only); src 827-829, 983-984.
- **Plain-English test of surprise**: A reader expects the termination list to name surrender; it names reinstatement instead.

### VN-26 F-20 — Unclear whether extra document requests stop the clock
- **Class**: T1 / T11
- **Scenario**: Art 10.6 starts its 30-day payment clock from a file complete under 10.1 to 10.5; 10.7's further documents are outside that list, so whether a 10.7 request stops the clock is not said.
- **Who bears it**: beneficiary. **Money direction**: unclear.
- **Standing**: LITERAL (reading only).
- **Evidence**: no assertion (reading only); src 10.6-10.7 (line numbers not given in the finding).
- **Plain-English test of surprise**: A claimant expects to know when the payment deadline runs; a document request leaves it uncertain.

### VN-26 F-21 — Burn degrees, transfer and danger left undefined
- **Class**: T5
- **Scenario**: "Phỏng" (burn) and its degrees, how body-skin area is measured, "Chuyển viện" (transfer), and "hoạt động nguy hiểm" (dangerous activity) beyond its examples are undefined, yet each decides a benefit or exclusion.
- **Who bears it**: insured. **Money direction**: unclear.
- **Standing**: LITERAL (reading only; fork F-32 treats dangerous activity as an input).
- **Evidence**: no assertion (reading only); src annex 4, 8.6, 69-71, 343-344, 705-707.
- **Plain-English test of surprise**: A claimant expects benefit-deciding words to be defined; several are not.

### VN-26 F-22 — Suicide exclusion that can never apply to death
- **Class**: T13 idle clause / T7
- **Scenario**: Art 11.1(c) and Art 3 exclude suicide from benefits for a death "do Tai nạn" (by accident), but 1.16 requires an Accident to be "không chủ động và ngoài ý muốn" (involuntary and unintended), so a suicide is never one; the head matters only for self-injury.
- **Who bears it**: unclear. **Money direction**: no money.
- **Standing**: LITERAL (reading only).
- **Evidence**: no assertion (reading only); src 180-190, 335-344, 696-713.
- **Plain-English test of surprise**: A reader expects an exclusion to exclude something; for death this one cannot.

#### VN-26 row summary
- **Findings in section 4**: 22 (F-01 to F-22). F-17 to F-22 are reading only; F-09's illness limb is evidenced in `pru-tests.l4:108`.
- **Most counterintuitive**: (F-02) claiming the permanent-injury maximum forfeits a 1,000,000,000 death benefit for the same Accident; (F-01) an accidental death on day 181 is paid nothing, while the same death drunk or from illness gets 30,000,000; (F-16) a reinstatement requested in time is defeated by the insurer's own 16-day-late letter.
- **Matches in this group**: F-15 = VN-25 FD3 (incontestability that protects nothing); F-09 refund threshold = VN-24 X15 and VN-25 FD9 (temporary-cover premium threshold), and its illness limb = VN-14 X2 and VN-25 FD25; F-10 = VN-25 FD19 and relates to VN-13 6 (premium kept or not returned on avoidance, against Law Art 22(2)); F-13 relates to VN-11 6, VN-13 23, VN-24 X14 (payee gaps or diversion); F-14 = VN-11 7, VN-14 X12, VN-25 FD18 (discretion without criteria); F-21 = VN-24 X22 (dangerous activities defined only by example); F-08 relates to VN-24 X18 and VN-25 FD8 (deadline against an event's timing); F-16 relates to VN-24 X4 (the insurer's own delay moving a clock against the customer); F-01 and F-03 relate to VN-24 X21 (benefits that disagree on the same event).

## Group cross-reference (patterns recurring in two or more rows)

- **Crime exclusion with no subject (murder victim excluded on the literal reading)**: VN-11 1, VN-13 2.
- **Claim-period discovery rule given only to the (possibly dead) policyholder**: VN-11 3, VN-13 7.
- **Misstated age or a pre-existing ground with no time limit, outliving incontestability**: VN-11 8, VN-13 9, VN-25 FD4; VN-24 X26 (no adjustment method).
- **Incontestability clause that protects nothing**: VN-25 FD3, VN-26 F-15.
- **HIV/AIDS "related to" exclusion with no carve-out, or occupational HIV cover that is illusory**: VN-11 9, VN-13 24, VN-24 X13.
- **No payee, or payee diverted**: VN-11 6, VN-13 23, VN-14 X9 and X14, VN-24 X10 and X14, VN-26 F-13.
- **Avoidance: what is returned (silent, charges not premiums, or premiums kept), against Law Art 22(2)**: VN-11 5, VN-13 6, VN-25 FD19, VN-26 F-10.
- **A deduction taken twice**: VN-13 1, VN-14 X6, VN-25 FD12.
- **No floor on a benefit or refund formula**: VN-11 16, VN-14 X10, VN-24 X3, VN-25 FD26.
- **Late-payment interest at a rate the document does not have ("advances from the account/contract value")**: VN-14 X21, VN-24 X12, VN-25 FD16; incomputable or insurer-set interest: VN-11 14, VN-13 15.
- **Temporary-cover anomalies (premium-threshold cliff; illness death unaddressed; covered death paying less than excluded)**: VN-14 X2 and X4, VN-24 X15, VN-25 FD9 and FD25, VN-26 F-09.
- **Claim time bar running out before the claim can be made**: VN-24 X18, VN-25 FD7 and FD8, VN-26 F-08.
- **Sum insured cut "tương ứng" with no measure**: VN-24 X25, VN-25 FD11.
- **Loyalty bonus lost or miscounted through the contract's own mechanisms**: VN-13 25, VN-14 X25, VN-24 X19, VN-25 FD14 and FD27.
- **Discretion without criteria**: VN-11 7, VN-13 11, 17-19, VN-14 X12, VN-24 X9 and X16, VN-25 FD18, VN-26 F-14.
- **An excluded or worse event pays more than a covered or better one**: VN-14 X2, VN-24 X8 and X21, VN-25 FD5, VN-26 F-01 and F-03.

