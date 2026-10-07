> Relayed by the lead, 2026-10-07. The independent test author (fid-il-07, one Opus agent, fresh session) was blocked by its harness from writing this file ("subagents should return findings as text") and returned it in a message; the lead saved the text below as received, with nothing changed except this note. The lead's own checks of it are in the commit message that deposits it.

# IL-07 — independent findings (fid-il-07)

I decided the answers from the Hebrew sources, the amending Laws and BTL/ITA figures in DECIDED-ANSWERS.md, finished 2026-10-06T23:46:05Z. That was before I opened any .l4 file, NOTES, RECONCILE, GAPS, check.sh or vendor.sh, and I never opened a row's directory. I read NOTES, RECONCILE and GAPS only after tests-independent.l4 had been written and run.

## 1. Numbers
I ran the tests in a scratch copy (36 of 36 vendored copies match VENDORED.sha256) and counted the way check.sh counts:
- run 1 (every child named "Child"): 278 assertions; 72 errors, 183 satisfied, 72 failed, 23 refused.
- **run 2, the deposited file: 278 assertions; 80 errors, 192 satisfied, 80 failed, 6 refused.**

Every error is a failed assertion. Between the runs only the children's names changed (M1); no #ASSERT line changed and no expected value was ever changed. check.sh expects 0 failures for this file, so it will now exit red.

## 2. What agreed (192)
- **Income tax, every figure**:
  - the 2026 brackets on both sides of each threshold;
  - the s 121B 3% on both sides of 721,560;
  - the 2,904 credit point, and 2¼ / 2¾ personal points;
  - s 66(c)(4)/(5) children's points at every age;
  - credits greater than the tax giving nil.
  My reading of s 66(c)(1A) (the sole earner, registered, requesting a separate calculation) is the capstone's. NOTES' citation of the 5786-2026 Law ss 5–7 confirms the brackets I chose over the February ITA booklet.
- **The NI deduction** up to and at 7,703 (1.04%), and its cap at the Schedule K maximum.
- **The child allowance wherever answered**:
  - 1–5 children: 173 / 392 / 611 / 830 / 1,003;
  - the s 66 exclusion of an additional-tax father: H30 0; H34 at 60,131 0; H33 at 60,130 173;
  - a high-earning mother whose husband is the counting parent (H31): 392;
  - a single high-earning mother (H32): 0;
  - the month after an 18th birthday (H26 173, H44b 0).
- **Refusals**:
  - 2025 and 2027 by name, for every figure;
  - s 40(b) for single parents with children (H32, H36, H36m);
  - the unencoded-credit flag (H41, H42).
- **The net** is salary − tax/12 − NI − health + allowance, as I guessed.

## 3. Findings
**F1 — the deduction above 7,703: 7.00% (mine) against 4.67% (capstone). 74 assertions fail: 41 NI and 33 net.**
- Provision: NII s 342(c)(1) "ינכה המעביד משכרו של העובד אחוזים מההכנסה שלפיה משתלמים דמי הביטוח כאמור בלוח י׳". Schedule J column D, upper part, prints a total ("סך הכל") of 7.00; BTL publishes 7% (sha256 f5bd019c…).
- The capstone takes the sum of the branch figures, 0.87+0.07+0.21+1.86+0.14+1.52 = 4.67. Example: H35 at 12,000 is 280.7811 against my 380.9012; at the maximum the difference is 1,030.02 a month.
- My own miss: I never added up the items, so I did not see before opening the encoding that the deposited table contradicts itself.
- Classification: genuine ambiguity, already recorded (R1, IL-04 F4, NOTES open question 5). My assertions are independent evidence for the regulator's reading. A stale branch figure in the consolidation is the likely cause.
- Also confirmed: the boundary is 7,703, not 8,139.60. At 7,704 the capstone gives 80.1579, so it reads the s 19(6) heading as I do.

**F2 — the allowance in a month of birth, or of an 18th birthday after the 1st: the capstone declines. 6 refused.**
- H25 (18 on 10 June) 392 expected; H27 (born 15 Sept) 392; H28 (born 16 Sept) 173. Each fails on the allowance and the net.
- Provision: s 72(a) "עד 15 בחודש … החל ב־1 באותו חודש … תשלום הקצבה יסתיים ביום האחרון של החודש שבו נפסקה הזכאות".
- Classification: a provision outside the rows, recorded (GAPS 6, K6). The text decides these three months; whether "עד 15" includes the 15th is the only open point.

**F3 — an 18th birthday ON the 1st: the capstone answers 0 where s 72 pays the month. 2 fail. Not recorded.**
- H44n: a married man, a child born 2008-11-01, 12,000, November 2026. I expected 173; the capstone gives 0 with no refusal.
- The gate in il07-adapter-il06.l4 tests `d GREATER THAN the first`, so a birthday on the 1st passes the gate. IL-06, asked about the 1st, already excludes the child.
- Classification: capstone error. It is a counterexample to K6's claim that the first day "answers every other month exactly". Births on the 1st are fine.
- Proposed fix: use `AT LEAST` for the anniversary limb, or encode s 72.
- I added H44n after seeing the encoding; its expected value comes from my pre-encoding s 72 reading. It is labelled as such in DECIDED-ANSWERS.md.

**F4 — a non-resident (H43): I guessed a refusal; the capstone answers. 2 fail.**
- The capstone gives tax 18,192 a year, NI 280.7811 (all nine branches), allowance 0, net 9,732.2571.
- The tax half is my guess wrong: ss 34 and 36 give no points to a non-resident, and s 121 still applies.
- The NI half is a gap that is recorded (GAPS 9, s 335) but not gated. s 335(a) "עובד … שאינו תושב ישראל ישתלמו בעדו דמי ביטוח אימהות" gives a non-resident different branches, yet the IL-05 adapter passes all nine even when NII residence is FALSE.
- Proposal: decline when NII residence (or Chapter 11 insurance) is FALSE.

**F5 — H45, 5,000 a month: my own error. 2 fail.**
- I expected 52. The capstone gives 67.01604 = 1.04% × 6,443.85 (net 4,771.48396).
- s 348(b) "ישתלמו בעדו דמי הביטוח כאילו הכנסתו היתה הסכום המזערי" applies (fork K8), so the capstone is right.
- With the full-adult-minimum input FALSE, the capstone declines (H45b), as I said I would accept.

**M1 — my input error.** In run 1 every child was named "Child". All 17 allowance and net answers for households with two or more children were then refused with "IL-06 reports that the household's facts cannot describe a family on the day". Distinct names cleared every one of them. Suggestion: neither IL-07 child nor the @export @desc says names must be unique, and the refusal does not say why it refused.

## 4. Inexpressible expectations
None. Two (H41 pension, H42 immigrant) can be expressed only through the caller's no-unencoded-credit flag. Three inputs I had not foreseen were needed: date of birth, the Part D age, and the full-adult-minimum flag.

## 5. Every failing or refused assertion (line, household, figure, mine → capstone, class)
**F1 (NI → net):**

| household | NI: mine → capstone | net: mine → capstone |
| --- | --- | --- |
| H05 | 80.1812 → 80.1579 | 7242.3002 → 7242.3235 |
| H47 | 100.9012 → 93.9811 | 7460.837 → 7467.7571 |
| H06 | 245.1012 → 190.1831 | 8860.735 → 8915.6531 |
| H07 | 245.1712 → 190.2298 | 8861.4133 → 8916.3547 |
| H08 | 870.9012 → 607.6811 | 14924.737 → 15187.9571 |
| H09 | 870.9712 → 607.7278 | 14925.3053 → 15188.5487 |
| H10 | 1297.9012 → 892.5511 | 18391.367 → 18796.7171 |
| H11 | 1297.9712 → 892.5978 | 18391.8953 → 18797.2687 |
| H12 | 2809.2012 → 1900.8041 | 29797.364 → 30705.7611 |
| H13 | 2809.2712 → 1900.8508 | 29797.7723 → 30706.1927 |
| H14 | 3174.6012 → 2144.5781 | 31928.69 → 32958.7131 |
| H15 | 3174.6012 → 2144.5781 | 33566.39 → 34596.4131 |
| H16 | 3174.6012 → 2144.5781 | 36285.29 → 37315.3131 |
| H17 | 3174.6012 → 2144.5781 | 41220.29 → 42250.3131 |
| H35 | 380.9012 → 280.7811 | 10176.637 → 10276.7571 |
| H37 | 380.9012 → 280.7811 | 10297.637 → 10397.7571 |
| H18 | 380.9012 → 280.7811 | 10954.637 → 11054.7571 |
| H19 | 380.9012 → 280.7811 | 10591.637 → 10691.7571 |
| H20 | 590.9012 → 420.8811 | 14175.037 → 14345.0571 |
| H21 | 590.9012 → 420.8811 | 13934.537 → 14104.5571 |
| H22 | 940.9012 → 654.3811 | 17798.037 → 18084.5571 |
| H23 | 170.9012 → 140.6811 | 9343.237 → 9373.4571 |
| H24 | 1640.9012 → 1121.3811 | 23193.037 → 23712.5571 |
| H26 | 380.9012 → 280.7811 | 11075.637 → 11175.7571 |
| H44 | 380.9012 → 280.7811 | 10349.637 → 10449.7571 |
| H44b | 380.9012 → 280.7811 | 10176.637 → 10276.7571 |
| H29 | 380.9012 → 280.7811 | 11196.637 → 11296.7571 |
| H30 | 3174.6012 → 2144.5781 | 41704.29 → 42734.3131 |
| H31 | 3174.6012 → 2144.5781 | 42701.29 → 43731.3131 |
| H33 | 3174.6012 → 2144.5781 | 36700.29 → 37730.3131 |
| H34 | 3174.6012 → 2144.5781 | 36527.79 → 37557.8131 |
| H40a | 380.9012 → 280.7811 | 10176.637 → 10276.7571 |
| H40d | 380.9012 → 280.7811 | 10176.637 → 10276.7571 |

NI only, at 380.9012 → 280.7811: H25, H27, H28, H36, H36m, H41, H42. NI only, at 3174.6012 → 2144.5781: H32.

**F2:** H25 allowance 392 and net 11294.637, refused. H27 allowance 392 and net 11415.637, refused. H28 allowance 173 and net 11196.637, refused.

**F3:** H44n allowance 173 → 0; net 10349.637 → 10276.7571 (F1 and F3 together).

**F4:** H43 tax and net: refusal expected, a value returned.

**F5:** H45 NI 52 → 67.01604; net 4786.5 → 4771.48396.

I checked that every net difference equals the NI difference, except H44n, where the allowance adds −173.
