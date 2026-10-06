# Work Injury Compensation Act 2019 — notes for a reviewer

## 1. What is encoded

**The whole Act**, ss 1-83 with the Part 3A platform-worker provisions (ss 34A-34P), ss 11A, 35A, 35B and Division 2A of Part 4 (ss 47A-47I), and the First to Sixth Schedules, as printed in SSO's PDF "Current version as at 06 Oct 2026" (`../source/WICA2019.txt`).

The law is stated for **accidents on or after 1 January 2025**, the day the Platform Workers Act 2024 amendments came into force. An accident before 1 September 2020 is under the repealed Act (s 83(1)); one between 1 September 2020 and 31 December 2024 is under this Act as it stood before those amendments. Neither text is in the source, so both refuse (`the law is encoded for an accident on`). Inside the encoded period the First and Fifth Schedules carry two sets of floors and caps, for accidents before and from 1 November 2025, and both are encoded.

Provisions that confer a power, describe a procedure, or define a word the caller applies are **inert**: they are listed in `provisions carried as text` (`wica-administration.l4`) and in the coverage table below. The outcome of a discretion — the Commissioner's, the Minister's or a court's — is an input, never a guess. Subsidiary legislation is not in the source: the prescribed interest rate, minimum insurance, compulsory policy terms, funeral cap, time limits, compoundable offences and the s 11A(b) apportionment are inputs or refusals.

The earlier row `naive-2026-10/` (s 7 and First Schedule paras 1-3 only) is untouched; this row stands beside it.

## 2. The goals

The user asked for provisions to be combined into goal-level conclusions rather than one per subsection. These are the eight goals, and the conclusions that answer each.

| # | Goal | Main conclusions | Module |
|---|------|------------------|--------|
| 1 | **Is the person covered by the Act?** — employee or platform worker, Third Schedule exclusions, Government employees, accidents abroad (s 9), seafarers (s 65), illegal contracts (ss 3(3), 34J), and the date gate (s 83) | `the coverage of` c `for the accident` a | `wica-liability.l4` |
| 2 | **Is someone liable to pay compensation?** — (a) the accident arose out of and in the course of the work (ss 7, 8, 34D, 34F); (b) the exclusions (s 7(2), s 34D(2), Sixth Schedule); (c) which platform operators, and their shares (s 34E); (d) the principal (s 13); (e) occupational and other diseases (ss 10-12, 34G-34I, Second Schedule), with the s 11 dates and s 11A apportionment | `the liability for` c `in the accident` a; `the liable platform operators and their shares for` a; `the principal is liable under s 13, …`; `the liability for the disease of a worker` cap `:` d | `wica-liability.l4` |
| 3 | **How much compensation?** — earnings (AME, ADE, lookback), the kind of incapacity (s 4), death, total and partial incapacity with the Fourth Schedule, temporary incapacity, medical expenses, commutation and payment deadlines, seafarers (s 67), refusal of treatment (s 38) | `the lump sum for an AME of` … `, outcome` o; `the temporary incapacity payments for …`; `the platform worker's temporary incapacity payments for …`; `the medical compensation for …`; `the employee's AME from` e; `the platform worker's AME from` e | `wica-compensation.l4`, `wica-schedules.l4` |
| 4 | **To whom, and is the payment good?** — payees (ss 18-21), discharge (s 22), no contracting out (s 23), interest (s 59), refunds (ss 16(5)-(7), 17(5)-(6), 34M, 34N, 54(4)) | `whom the insurer pays, under s 18:` f; `whom the employer pays, under s 19:` f; `paying` p `discharges the compensation, …`; `the interest payable, …`; `the Commissioner may order a refund …` | `wica-payment.l4` |
| 5 | **Where does the claim stand, and what deadlines apply?** — notice and deemed withdrawal (s 35), withdrawal and resumption (ss 41-42), the s 39 claim, the medical examination (s 37), notices becoming orders and objections (ss 44-49, 47B-47E), settlement (s 51), appeal (s 58), concurrent work (s 35A), who processes (s 36), several platform operators' insurers (ss 47A-47G) | `the status on` d `of the claim in` h; `the day the notice takes effect as an order, if it does:` n; `an objection on … is in time, …`; `an appeal lies against` o …; `the relevant platform operator, …` | `wica-process.l4`, `wica-administration.l4` |
| 6 | **Damages instead of, or as well as, compensation?** — ss 63, 64 | `s 63(1) bars compensation, given` h; `s 63(2) bars an action for damages against the employer, given` h; `the court assesses compensation under s 63(6), …`; `the indemnity from the third party, …` | `wica-process.l4` |
| 7 | **Is the insurance in order?** — the duty to insure (ss 24, 34O, 67(4)), approved policies (s 26), double insurance (s 27), insolvency (ss 28-29), who may provide it (s 30), designated insurers (ss 31, 34), the insured amount (ss 18(1), 47, 47F), the employer's duty to cooperate (s 40) | `the insurance duty is met:` i; `what the insurer of a purported policy must pay, …`; `the employer's rights against the insurer pass to the worker:` f; `providing it is an offence under s 30, …` | `wica-insurance-offences.l4`, `wica-administration.l4` |
| 8 | **Is an offence committed, and what is the most it can cost?** — every offence, the repeat-offender rules, maximum penalties, composition (s 76), officers (ss 72-73), the Government (s 77) | `the s 25(1) / 34P(1) offence is made out on` i …; `a repeat offender for` o `, with earlier convictions` e; `the maximum penalty for` o `, a repeat offender:` r; `the composition limit for …` | `wica-insurance-offences.l4` |

## 3. Modules

| module | what it holds |
|---|---|
| `wica-types.l4` | the nouns: claimant, accident, disease, earnings, leave days, payees, the claim history, notices, damages history, insurance, offences |
| `wica-schedules.l4` | Tables A and B (both Schedules print the same tables), the age on the next birthday, the Second Schedule (38 items and periods), the Fourth Schedule (26 items, Notes 1-2), the Sixth Schedule |
| `wica-liability.l4` | Goals 1 and 2, and the date gate |
| `wica-compensation.l4` | Goal 3 |
| `wica-payment.l4` | Goal 4 |
| `wica-process.l4` | Goals 5 and 6 |
| `wica-insurance-offences.l4` | Goals 7 and 8 |
| `wica-administration.l4` | the insured amount, s 40, ss 47A-47G, s 21(2)(b)(i), s 60(2), s 70, and the list of provisions carried as text |
| `wica-tests-liability.l4`, `wica-tests-compensation.l4`, `wica-tests-payment-process.l4`, `wica-tests-insurance-offences.l4` | the encoder's tests, expected values worked from the source |
| `tests-independent.l4` | the independent test author's assertions (section 8) |

## 4. Coverage

Every section and Schedule. *encoded*: a rule decides it. *input*: the fact, or the outcome of a discretion, comes from the caller. *inert*: nothing to compute; carried as text.

| provision | heading | disposition |
|---|---|---|
| s 1 | Short title | inert |
| s 2 | General interpretation | encoded where a definition decides something ("work", "platform worker" as input, "AME"/"ADE" via the Schedules); the rest applied by the caller |
| s 3 | "employee" and "employer" | encoded: s 3(1)(a)-(b), Third Schedule; s 3(3) illegal contract reported as not covered, the saving discretion being the Commissioner's or court's |
| s 4 | Meaning of incapacity | encoded: s 4(5) total/partial; s 4(2)(b) via the Fourth Schedule; s 4(4) in the s 15 rule |
| s 5 | Purpose | inert |
| s 6 | Assistant Commissioners, officers | inert |
| s 7 | Employer's liability | encoded: (1), (2)(a)-(c) with both fight exceptions, (4) |
| s 8 | Accidents deemed in course of employment | encoded: (1), (2), (3) |
| s 9 | Accidents outside Singapore | encoded |
| s 10 | Liability for diseases | encoded: (1)(a)-(c), (3)(a)-(b), (4), (5) |
| s 11 | Date of accident (disease) | encoded: (1), (2); fork F3 |
| s 11A | Apportionment for disease | encoded: (a); (b) refuses (regulations) |
| s 12 | Disease limited to work injuries | encoded |
| s 13 | Liability of principal | encoded: (1), (2), (5); (3)-(4) indemnity and recourse noted |
| s 14 | Computation of compensation | encoded via the First Schedule |
| s 15 | Assessment of permanent or current incapacity | encoded: (1)(b), (2) |
| s 16 | Medical treatment | encoded: (1), (2), (5)-(7); (3)-(4), (8) noted |
| s 17 | Temporary incapacity | encoded: (1)(b) interval, (4) commutation, (5)-(6) refund; (2)-(3) review power inert |
| s 18 | Payment or deposit by employer's insurer | encoded: (1) insured amount, (2), (3) |
| s 19 | Payment or deposit by employer | encoded |
| s 20 | Direction to pay relative | input (the direction); (2)-(3) inert |
| s 21 | Deposit with Commissioner | input (the direction); (2)(b)(i) funeral cap encoded with the cap as input; rest inert |
| s 22 | Discharge | encoded |
| s 23 | No contracting out | encoded |
| s 24 | Employer must be insured | encoded |
| s 25 | Offences, employer insurance | encoded: (1)-(5) |
| s 26 | Approved policy | encoded: (1), (3)-(4A) |
| s 27 | Double insurance | encoded |
| s 28 | Employer bankrupt | encoded: (1), (2)(b), (3), (5) |
| s 29 | Contract void or voidable | encoded |
| s 30 | Provision of insurance | encoded: (1)-(3A), (5) |
| s 31 | Designation | encoded: (6); rest inert |
| s 32 | Obligations of designated insurer | inert |
| s 33 | Information | inert |
| s 34 | Cancellation, suspension, penalty | encoded: (1)(b) ceiling; rest inert |
| s 34A | Interpretation (Part 3A) | inert (work stage is an input) |
| s 34B | Application of Part 2 | encoded: rules written once for both; s 34B(c) excludes s 13 |
| s 34C | Application of Part 3 | encoded the same way |
| s 34D | Platform operator's liability | encoded: (1), (2) with Sixth Schedule limbs, (4) |
| s 34E | Several platform operators | encoded: (2)(a)-(b), (3) |
| s 34F | Deemed in course of platform service | encoded |
| s 34G | Platform operator, diseases | encoded (cut-off 1 January 2025) |
| s 34H | Date of accident (platform disease) | encoded with s 11 |
| s 34I | Disease limited to work injuries | encoded with s 12 |
| s 34J | Illegal agreements | encoded as s 3(3) |
| s 34K | Computation (platform) | encoded via the Fifth Schedule |
| s 34L | Assessment (platform) | encoded with s 15 |
| s 34M | Medical treatment (platform) | encoded with s 16 |
| s 34N | Temporary incapacity (platform) | encoded: (1), (2), (5), (6)-(7) |
| s 34O | Platform operator must be insured | encoded with s 24 |
| s 34P | Offences, platform operator insurance | encoded |
| s 35 | Deemed claim | encoded: (5); (6)-(7) excuse; (8)-(9) offence; (2)-(4A) inert |
| s 35A | Directions on processing | encoded: (4), (5); rest inert |
| s 35B | Application of Part 4 | encoded the same way as s 34B |
| s 36 | Processing by insurer or Commissioner | encoded: (2); (1) inert |
| s 37 | Medical examinations | encoded: (1), (7); (2)-(6) inert |
| s 38 | Refusal of medical treatment | encoded (the trigger; the direction is a discretion) |
| s 39 | Claim for permanent or current incapacity | encoded (two subsections (2) printed; section 7) |
| s 40 | Employer must cooperate with insurer | encoded |
| s 41 | Withdrawal and resumption | encoded: (1), (2), (3)-(4) |
| s 42 | No compensation if withdrawn | encoded in the claim status |
| s 43 | Representatives | inert |
| s 44 | Employer's insurer's process | encoded: (5), (6); (1)-(4) inert |
| s 45 | Directions on denial of liability | inert |
| s 46 | Objection to notice of computation | encoded: (2), (3) noted |
| s 47 | Payment by employer's insurer | encoded (insured amount) |
| s 47A | Relevant platform operator | encoded |
| s 47B | Platform operator's insurer's process | encoded: (5) with s 44(5); rest inert |
| s 47C | Other platform operators liable | encoded: (4)-(7) |
| s 47D | Objection (s 47B) | encoded with s 46(2) |
| s 47E | Objection (s 47C) | encoded: (2), (3), (5); rest inert |
| s 47F | Payment by platform operator's insurer | encoded with s 47 |
| s 47G | Recovery under s 47C(6)-(7) | encoded: (3), with the prescribed period's end as input |
| s 47H | Directions on denial | inert |
| s 47I | Information | inert |
| s 48 | Assessment or reassessment | encoded: (3), (4); rest inert |
| s 49 | Objection to notice of assessment | encoded with s 46(2) |
| s 50 | Directions | encoded: (4) offence; (1)-(3) inert |
| s 51 | Settlement | encoded: (3); (1)-(2) inert; s 23(1) |
| s 52 | Pre-hearing conference | inert; s 23(1), s 58(5) |
| s 53 | Failure to appear | inert |
| s 54 | Powers of Commissioner | encoded: (4); rest inert |
| s 55 | Hearing | inert |
| s 56 | Experts | inert |
| s 57 | Medical Board | inert |
| s 58 | Appeal | encoded: (1), (5); (2)-(4) inert |
| s 59 | Interest | encoded: (2) cap, the rate as input |
| s 60 | Enforcement | encoded: (2) |
| s 61 | Failing to pay or deposit | encoded |
| s 62 | False or misleading information | encoded |
| s 63 | Limitation of action for damages | encoded: (1), (2), (3), (5), (6); (4), (7)-(8) inert |
| s 64 | Remedies against employer and third party | encoded |
| s 65 | Seafarers | encoded: (2) in coverage |
| s 66 | Depositions | inert |
| s 67 | Other shipping laws | encoded: (1)-(4) |
| s 68 | Powers of Commissioner and officers | encoded: (6)-(7) offence; (1)-(5) inert |
| s 69 | Reciprocal arrangements | inert |
| s 70 | Ex gratia payments | encoded |
| s 71 | Protection from liability | inert |
| s 72 | Offences by corporations | encoded: (2) |
| s 73 | Offences by unincorporated associations | encoded: (2) |
| s 74 | Magistrate | inert |
| s 75 | Jurisdiction | inert |
| s 76 | Composition | encoded: (1) |
| s 77 | Government not liable to prosecution | encoded |
| s 78 | Immunity for disclosure | inert |
| s 79 | Exemptions | inert |
| s 80 | Service | inert |
| s 81 | Amendment of Schedules | inert |
| s 82 | Regulations | encoded: (3) ceiling; (1)-(2) inert |
| s 83 | Repeal, saving, transitional | encoded: (1) date gate; (2)-(4) inert (before the encoded period) |
| First Schedule | Compensation for employees | encoded: paras 1-6; para 6(3), (6) discretions are inputs |
| Second Schedule | Occupational diseases | encoded: 38 items, condition and period; the occupation column is an input |
| Third Schedule | Classes not covered | encoded |
| Fourth Schedule | Injuries deemed permanent | encoded: items 1-26, Notes 1-3 |
| Fifth Schedule | Compensation for platform workers | encoded: Part 3 paras 1-7; Parts 1-2 (locations, work stages) inert, the stage an input |
| Sixth Schedule | Laws for s 34D(2) | encoded as lists; whether a contravention is proven is an input |

No row is deferred.

## 5. Fork register

| fork | text | readings | taken |
|---|---|---|---|
| F1 | s 9 extends the Act to an employee "employed by an employer in Singapore" working abroad; s 34B maps Part 2 onto platform workers but s 9 has no platform equivalent | (a) the Act does not reach a platform worker's accident abroad; (b) s 9 applies by analogy | **REFUSE**: the text does not say |
| F2 | s 10(5): the limitation period is the Second Schedule's months "starting on the day after" the worker ceased in the occupation | its last day is (a) the same calendar date N months after ceasing; (b) N months counted from the day after | (a): starting the day after and running N months ends on the same date |
| F3 | s 11(2): "(a) the earlier of (i) the incapacity ... or (ii) the certification ...; or (b) if there has been no previous period of incapacity — the date of death" | with no incapacity but both a certification and a death: (a)(ii) or (b) | (b), death, as the paragraph addressed to "no previous period of incapacity"; certification alone when there is no death; REFUSE when there is neither |
| F4 | First Schedule para 4(1) pays, per day, an amount "based on" AME, a monthly figure | the daily rate is AME/30, AME×12/365, AME/working days... | **input**: the daily rate is given by the caller |
| F5 | para 4(1)(c): "the first 14 days of medical leave and light duties" | (a) one count shared by both kinds of day; (b) 14 of each | (a), in the order the days fall |
| F6 | deadlines that fall on a Sunday or public holiday | (a) the Interpretation Act 1965 s 50 shift; (b) the raw date | (b): no holiday calendar is encoded; a caller applying s 50 adjusts the date |
| F7 | Fourth Schedule Note 2: the parts of "the hand" not to exceed "the loss of the whole hand" | parts listed may be on one hand or two | all parts in one call are one hand (70% cap); item 2 (both hands) is not a hand part; losses on two hands are two calls |
| F8 | s 18(2)(c)-(e) carry no order among themselves | which wins when two apply | a Commissioner's direction (e) prevails; then death (c); then incapacity (d) |
| F9 | s 35A(4) speaks of one AME being "higher" | equal AMEs | fall to (c), the Commissioner's processing |
| F10 | Fifth Schedule para 5(1)(b) caps medical expenses "per accident per employee" | a drafting carry-over for platform workers, or a cap that does not apply | per platform worker |
| F12 | s 83(1): the repealed Act applies to a disease "if the date of the accident ... is before 1 September 2020" | which date, when no s 11(2) date exists yet | the s 11(2) date of accident; with no incapacity, death or certification yet, the date the disease was contracted |
| F11 | s 3(3), s 34J: the Commissioner or court "may" treat an illegal contract as valid | — | reported as not covered, with the reason; the saving is a discretion outside the encoding |

The PDF prints **two subsections (2) in s 39**: the newer (notification of assessment) contains the older text; the encoding reads them together as one s 39(2).

## 6. Answer tables

### Floors and caps (First Schedule paras 1, 2, 5; Fifth Schedule Part 3 the same)

| | accident before 1 Nov 2025 | on or after 1 Nov 2025 |
|---|---|---|
| death, floor / cap | $76,000 / $225,000 | $91,000 / $269,000 |
| C, floor / cap (total = 1.25C) | $97,000 / $289,000 | $116,000 / $346,000 |
| most for total incapacity | $361,250 | $432,500 |
| medical expenses, per accident | $45,000 | $53,000 |

### Temporary incapacity, per day within one year of the accident (para 4)

| | employee | platform worker |
|---|---|---|
| hospitalisation, first 60 days | AME (daily rate, F4) | ADE |
| hospitalisation, later days | 2/3 | 2/3 ADE |
| medical leave, first 14 days (shared with light duties, F5) | AME | ADE |
| medical leave, later days | 2/3 | 2/3 ADE |
| light duties | shortfall of actual wages below AME (first 14) or 2/3 AME | not a head |
| ADE unavailable | — | $27 per day |

### Maximum penalties

| offence | first | repeat |
|---|---|---|
| s 25(1), s 34P(1) not insured | $10,000 / 12 months | $20,000 / 12 months |
| s 25(4), s 34P(4) deducting insurance cost | $5,000 / 6 months | $10,000 / 6 months |
| s 30(1), (2A), (3) insurance providers | $80,000 per policy | $160,000 per policy |
| s 35(8) no notice to the Commissioner | $5,000 | $10,000 / 6 months |
| s 50(4) direction | $5,000 / 6 months | $10,000 / 6 months |
| s 61(1), (3), (5) failing to pay or deposit | $15,000 / 12 months | $30,000 / 12 months |
| s 62(1) false information | $5,000 / 6 months | $10,000 / 6 months |
| s 62(3)(a), (b) dishonesty | $15,000 / 12 months | $30,000 / 12 months |
| s 68(6) obstruction | $5,000 / 6 months | $10,000 / 6 months |
| s 82(3) regulations (ceiling) | $10,000 / 6 months | — |

Composition (s 76(1)): the lower of half the maximum fine and $5,000.

## 7. Notes on the text

- **Tables A and B** are printed identically in the First and Fifth Schedules; each has 53 rows ("14 and below" to "66 and above"). Encoded once.
- **Formulas printed as images** (First Schedule para 6(1) A/P, para 6(2) (D×W×52)/12; Fifth Schedule Part 3 para 6(1)(c) E/P) are transcribed in `../source/PROVENANCE.md`; SSO's grant excludes images.
- **Second Schedule** is as amended by S 751/2025 (wef 1 December 2025). The earlier list is not in the source, so a disease contracted between 1 January and 30 November 2025 is decided against the current list.
- **Bugs found while writing the tests** (and see section 9 for those found by the independent pass), fixed before the independent pass: s 34N(2)(b) built an invalid month 13 for a certificate received late in December; Fourth Schedule Note 2 capped "both hands" (item 2) with a thumb at 70% as if it were a part of one hand.

## 8. Checks

`L4=~/.local/bin/l4 ./check.sh`, run 2026-10-06 after the fixes in section 9:

| module | errors | satisfied | failed |
|---|---|---|---|
| `wica-tests-liability.l4` | 0 | 89 | 0 |
| `wica-tests-compensation.l4` | 0 | 95 | 0 |
| `wica-tests-payment-process.l4` | 0 | 111 | 0 |
| `wica-tests-insurance-offences.l4` | 0 | 116 | 0 |
| `tests-independent.l4` | 0 | 426 | 0 |
| the eight rule modules | 0 | — | — |
| **total, 13 modules** | **0** | **837** | **0** |

No assertion is expected to fail. `#ASSERT REFUSED` lines count as satisfied when the rule refuses.

## 9. The independent test pass

A fresh session wrote 426 expectations from the brief and the source before opening any module (`independent-expectations.md`), then `tests-independent.l4`; its report is `INDEPENDENT-TEST-REPORT.md`. First run: **421 satisfied, 5 failed**. All 419 scenarios written before the modules were read agreed; the five failures were in supplementary scenarios, and all five were **encoding errors**:

- **S1, S2** — the disease rule had no date gate, so a disease dated 2019 or 2023 was answered from this text. Fixed (fork F12).
- **S3** — temporary incapacity had no date gate. Fixed.
- **S4, S5** — the partial-incapacity function priced an aggregate of 100% or more at C × percentage instead of C + 0.25C (s 4(5)(b)). Fixed.

One encoder assertion was wrong for the S1 reason (a 2011 disease asserted "not compensable"; s 83(1) sends it to the repealed Act) and now asserts a refusal; the 2024 platform-worker disease scenario was given a 2025 incapacity date so that it still tests the s 34G cut-off. No independent assertion was changed.

What the independent author could not express, and why:

- **inputs by design**: the work stage (Fifth Schedule Parts 1-2), the relevant platform service (para 7), the daily rate (F4), deemed hospitalisation (para 4(4)), whether a medical cost fell within the year;
- **carried as text**: s 3(2) (a lent employee), s 13(2)-(3) indemnity, s 47C(4), which offences are compoundable, the prescribed time to pay;
- **facts the records do not state**: an order date for s 41(1)'s "before any order"; s 46(3) (a Medical Board change is not an "error"), which the caller applies in deciding `objection delayed by another's error or fraud`; a policy void for unpaid premiums (s 29(1) covers only other grounds); s 34D(3)'s definition of "drug", applied by the caller to `proven the injury is directly attributable to alcohol or a drug`. Fifth Schedule para 6(2)(b)'s B is all the leave days in the period, where there was a run of 7 or more; the field's comment says so.

## 10. Open questions for a domain expert

1. F1: does the Act reach a platform worker's accident outside Singapore?
2. F4: how is AME turned into a daily rate for temporary incapacity — does MOM use AME/30, or working days?
3. F5: is the 14-day limit shared between medical leave and light duties?
4. F7: Note 2 for losses on both hands.
5. Accidents between 1 September 2020 and 31 December 2024: the pre-2025 text would let this encoding answer them.
