# Insurance Act 1966 (Singapore) — encoding notes

Read this first. `BRIEF.md` is the specification; `../source/PROVENANCE.md` says where the text came from and transcribes the two formulas the PDF prints as images.

## 1. What is encoded

**The whole Act**, as printed by SSO as the "Current version as at 07 Oct 2026": Parts 1 to 4 and both Schedules.

**What is computed:**
- what the Act fixes: permission, thresholds, limits, periods, priorities, maxima and classifications;
- every penalty in the Act, in one table, with ss 142, 143 and 145 applied on top.

**What is an input:** the Act's many powers turn on the Authority's or the Minister's opinion, approval or consent. Each of those is an input. So are prescribed figures (financial requirements, fund solvency and capital adequacy, fees, the s 150 amount) and figures defined in other Acts.

**What is carried as text:** provisions that only confer a power or describe a procedure. Each module lists them.

### The two top-level goals

The Act speaks to a regulated person and to a policy owner, so it has two questions.

**A. `the regulatory position for` a `Regulatory case`** (`ia-goal.l4`). *For this person and what it does, does the Act reach it, does it permit it, and if not, what offence is it and what is the most it can cost?* The answer gives:
- reach (s 145);
- permission;
- the offence;
- the maximum fine, imprisonment and daily fine, for an individual, a corporation (doubled by s 143 where that applies) or another person;
- the most that may be collected to compound the offence (s 142(7));
- the courts (s 144).

**B. `the policy position for` a `Policy case` and its `Estate facts`** (`ia-goal.l4`). *For this policy and its owner, what kind of policy is it, is it valid and for how much, what rights does the owner have, and who receives the death benefits?* The answer gives:
- Singapore or offshore policy;
- class of business;
- the capacity to insure;
- validity for insurable interest, and the most recoverable;
- the s 148 and s 149 rights;
- who takes the death benefits;
- whom the insurer may pay without probate.

### The goals under them

| goal | question | main functions | provisions | module |
| --- | --- | --- | --- | --- |
| 1 | May this person carry on insurance business, solicit, act as agent, broke, place risk, or use these names? | `the activity is permitted`, `the offence for` | ss 3-10, 64-75, 83-92 | `ia-permission.l4` |
| 2 | Does this holding, stake, appointment or loan need approval, or exceed a limit? | `effective control of an insurer`, `a major stake…`, `effective control of a broker…`, `the activity is permitted` | ss 26-37, 87-89 | `ia-permission.l4` |
| 3 | May this allocation, withdrawal or premium be made? | `the most that may be allocated to the surplus account`, `the most that may be withdrawn from a fund…` | ss 16, 22 | `ia-permission.l4` |
| 4 | For this offence and this offender, what is the maximum penalty, and the composition sum? | `the maximum penalty for`, `the most that may be collected to compound`, `the Act reaches an act` | every penalty limb; ss 142-145 | `ia-penalties.l4` |
| 5 | When does a cancellation take effect, and by when must an appeal be made? What periods apply to returns and transfers? How are an insolvent insurer's assets shared? | `a cancellation takes effect…`, `the last day to appeal…`, `what each s 123 class receives…`, and the dated rules | ss 11-14, 19, 30, 42-45, 59, 80, 94-130 | `ia-supervision.l4` |
| 6 | Is this a Singapore policy? What class is it? Is it valid, and for how much? What are the owner's rights? | `the policy is`, `ordinarily resident in Singapore`, `the class of business of`, `the policy is valid for insurable interest`, `the most that may be recovered under`, `has capacity to insure…`, `the owner's statutory rights under` | s 3; First Schedule; ss 66, 68, 146-151 | `ia-policies.l4` |
| 7 | Is the nomination valid? Who takes the death benefits? Whom may the insurer pay, and how much? | `the nomination is valid`, `the nominees after deaths before the owner`, `the death benefits go`, `the insurer may pay without probate`, `a proper claimant's payment…` | ss 131-136, 150 | `ia-policies.l4` |

## 2. How to ask: the questions, and the rule each one invokes

Give the facts named in each row; the answer comes back as the field shown.

| ask | invoke | give |
| --- | --- | --- |
| "Is company X, licensed only for general business, allowed to write life policies? If not, what is the most it could be fined?" | `the regulatory position for` → `permitted`, `maximum penalty` | a `Standing`, the `Activity` (`carrying on a class of insurance business…` with the class), and the `place` |
| "We are an overseas reinsurer. May we reinsure a Singapore insurer that approached us?" | `the activity is permitted` with `providing reinsurance from outside Singapore to persons in Singapore` | whether the arrangement was unsolicited and initiated by a licensed insurer or broker |
| "A person holds 18% of shares and has an arrangement over another 6% of the votes. Is approval needed?" | `obtaining control of a licensed insurer incorporated in Singapore` | shareholding percentages, substantial-shareholder status, the arrangement's percentage, and any approval |
| "May the insurer take 12% of a fintech company?" | `a licensed insurer acquiring or holding a stake in a corporation` | percentages, control, any s 34(6) exception, and any approval |
| "How much can an insurer lend unsecured to a director, or to an employee earning $X?" | `granting an unsecured loan or advance` | the lender (insurer or broker), the borrower's role, and the amount outstanding |
| "Bonus to participating policies is $900k. How much may go to the surplus account?" | `the most that may be allocated to the surplus account` | the `Fund facts` |
| "What is the most a corporation, or an individual, faces for offence Y? What may be paid to compound it?" | `the maximum penalty for`, `the most that may be collected to compound` | the `IA offence`, and whether the offender is an individual or a corporation |
| "The Authority informed us of a cancellation on D. When does it take effect, and when must we appeal?" | `a cancellation takes effect…`, `the last day to appeal to the Minister…` | D, whether it was at the insurer's request, and whether an appeal was lodged |
| "An insolvent insurer has $A after preferential debts. What does each class of claim receive?" | `what each s 123 class receives from assets`, then `a claim's payment…` | the five class totals, in s 123(3) order |
| "Is this policy a Singapore policy? Is it life or general business?" | `the policy position for` → `Singapore or offshore`, `class of business` | the `Policy case`, including the owner's `Residence facts` |
| "Is a life policy on my business partner valid, and for how much?" | `the policy position for` → `valid for insurable interest`, `most that may be recovered` | the life insured, the insurable interest and the sum insured |
| "Can a 14-year-old buy a policy?" | `has capacity to insure, aged … with a parent's written consent` | the age, and whether a parent consented in writing |
| "My policy is 3 years old. Can I surrender it, or stop paying and keep cover?" | `the owner's statutory rights under` | the years in force; whether the policy is an annuity |
| "I nominated my wife and son. Is that a valid trust nomination, and who gets paid when I die?" | `the nomination is valid`, `the death benefits go`, `the insurer may pay without probate` | the `Estate facts`: kind, nominees and portions, age, trust intent, revocation, will, notice |
| "One of three nominees died before me. How are the shares redistributed?" | `the nominees after deaths before the owner` | the nominees with their portions, and who is alive |
| "Several relatives claim without probate. What does each get under the cap?" | `a proper claimant's payment…` | each claim, the total of the claims, and the prescribed amount |

## 3. Coverage table

| provision | heading | disposition |
| --- | --- | --- |
| long title, 1, 2 | Short title; interpretation | Inert, except where a definition is computed: "insurance business in Singapore" via s 3(6), and "major stake" etc. in their sections |
| 3 | Classification | Goal 6, (1); (6) in Goal 1; (2)-(5), (7)-(10) read into the facts |
| 4-9 | Unlicensed business, holding out, names, co-branding, solicitation, representative offices | Goal 1, with their penalties in Goal 4 |
| 10 | Examination of suspects | penalty in Goal 4; the power is inert |
| 11-14 | Licensing, fees, cancellation, effects | Goal 5 (cancellation timing, grounds (3)(a) and (g)/(10), appeals); penalties in Goal 4; the rest carried as text |
| 15 | Register of policies | carried as text |
| 16 | Insurance funds | Goal 3, (7)(c), (9), (10); the rest carried as text |
| 17-21 | Solvency, assets, documents, custody | penalties in Goal 4; s 19(3) notice in Goal 5; requirements are prescribed (inputs) |
| 22 | Premiums | Goal 3 |
| 23, 24 | Forms; financial advisers' remuneration | penalties in Goal 4; the rest carried as text |
| 25-33A | Control of insurers | Goal 2 (ss 26(7), 27); the s 30 defence period in Goal 5; penalties in Goal 4 |
| 34 | Investment in corporations | Goal 2 |
| 35, 36 | Officers; disqualification | Goal 2, as approval and consent inputs; penalties in Goal 4 |
| 37 | Unsecured loans | Goal 2 |
| 38-41 | Information, web aggregator, product direction | penalties in Goal 4; the rest carried as text |
| 42-50 | Authorised reinsurers | Goal 5 (control at 50%, cancellation timing); penalties in Goal 4; the rest carried as text |
| 51 | Saving for validity | carried as text: no policy is invalidated by Parts 2-2B |
| 52-63 | Foreign insurer schemes | Goal 1 (standing); Goal 5 (s 59 timing); penalties in Goal 4; the rest carried as text |
| 64-74 | Intermediaries | Goal 1 (s 64, s 70); Goal 6 (ss 66, 68); penalties for ss 67, 69, 71 in Goal 4; the rest carried as text |
| 75-93 | Broking | Goal 1 (ss 75, 83-86, 90-92); Goal 2 (ss 87, 89); Goal 5 (s 80); penalties in Goal 4 |
| 94-101U | Returns, inspection, investigation, evidence | Goal 5 (ss 96, 97 periods); penalties in Goal 4 |
| 102-108 | Failing insurers | Goal 5 (s 102 grounds, s 107(3)); penalties in Goal 4 |
| 109-115 | Foreign regulators | Goal 5 (s 111); penalties in Goal 4 |
| 116-126 | Transfers, winding up | Goal 5 (ss 117-119 periods, s 121, s 123); penalties in Goal 4 |
| 127-130 | Appeals | Goal 5 (s 127(2)); the rest carried as text |
| 131-136 | Nominations | Goal 7 |
| 137-141 | Administration | carried as text |
| 142-145 | Offences | Goal 4 |
| 146-152 | Insurable interest, capacity, deductions, surrender, payment, gaming, fire | Goals 6-7; s 152 carried as text |
| 153-155 | Supplementary | carried as text |
| First Schedule | Definitions | Goal 6: paras 2, 9, 10, 13. The others are read into the facts |
| Second Schedule | Specified provisions | carried as text (s 137(2)) |

No row is left `deferred`.

## 4. Fork register

| id | provision | question | reading taken | why |
| --- | --- | --- | --- | --- |
| F1 | s 143(2)(a) "a duty imposed only on corporations" | Which single-penalty offences are duties only on corporations? | Duties of a licensed insurer, an authorised reinsurer, a registered broker or a transferee. Each must be a body corporate (ss 11(3), 42, 77(1)). | Their penalties are therefore not doubled. Offences open to "any person" are doubled for a corporation |
| F2 | s 143(1) "a fine not exceeding 2 times the maximum amount" | Is the continuing daily fine doubled too? | Yes | It is "a fine for that offence" |
| F3 | s 142(7) "one half of the amount of the maximum fine that is prescribed for that offence" | Which fine? | The fine prescribed for the kind of offender, before any s 143 doubling | Doubling is what "the court may impose", not what is "prescribed" |
| F4 | ss 13(6), 44(5), 59(3) "until the expiration of a period of 30 days after" | Effective date | Informed on D: effective on D + 31 | The period of 30 days after D ends at the end of D + 30 |
| F5 | s 146(2) "Where subsection (1)(a) applies" | Is recovery capped when the life insured is the policy owner's own life or a spouse's? | No. The cap applies only where the policy stands on insurable interest alone | (1)(b) and (1)(c) save the policy independently of (a) |
| F6 | s 27(1) "substantial shareholder" | Where is the threshold? | An input, defined by s 81 of the Companies Act 1967 | The threshold is not in the source. s 27(2)'s 5% arrangement threshold is in the source, and is computed |
| F8 | s 147(1) "a person over the age of 10 years" | What of a person aged 10 or under? | The encoding refuses | The section says nothing about them; the general law of capacity decides. First read as "no capacity"; revised after the independent pass |
| F9 | s 132(7)(b) "so long as no nominee has died before the revocation" | With no outside trustee and a nominee dead, whose consent is needed? | None named; only the prescribed requirements in (c), which are the caller's | The text. Revised after the independent pass |
| F7 | ss 37, 89 | Is a loan exactly at the limit allowed? | Yes ("exceed" means more than) | The text |

## 5. Tests

`ia-tests.l4` has 157 assertions. Expected values are worked from the source. They cover:
- every activity in Goals 1-3, on both sides of each threshold: 20% control, 5% arrangement, more than 10% for a major stake, $5,000, $3,000, the 1/9th surplus allocation, surplus less the solvency requirement;
- the penalty table: individual against corporation, split penalties, doubling, corporate-only duties, s 142(3), s 142(5) and composition;
- s 145;
- the Goal 5 periods and the s 123 distribution;
- ordinary residence at 183 days and at 90 days, and the 25% treaty test;
- insurable interest and its cap, capacity at 10 and at 16, the 3-year rights;
- nominations, including the s 133(5) A/B × C redistribution and the s 150(11) pro rata payment;
- whole cases through both top-level goals.

**The independent pass.** `tests-independent.l4` (213 assertions), `independent-expectations.md` and `INDEPENDENT-TEST-REPORT.md` are the independent pass. A separate session wrote 221 expectations from the source before reading the encoding; 201 of them could be asserted.
- 212 passed and one failed: s 147 at age 8. I agreed with the independent reader on it and revised it as fork F8.
- The report also pointed out s 132(7)(b), which I revised as fork F9. My own two assertions on these points changed with the forks.
- All 213 now pass, and none refuse.

**Simplifications the report lists, kept as they are:**
- **No input for incorporation in Singapore.** So s 34(1) and (2) are not told apart, and neither are the director limbs of ss 35 and 36. The s 26/27 activity is named for insurers incorporated in Singapore.
- **s 35:** the duties in (1)-(2), (8) and (9) are carried as text.
- **Defences and exceptions not computed:** officer liability under s 5(1)(b); the defences in s 8(4) and most of s 30; s 66(4)-(5); s 89(2); s 34(3); s 145(3).
- **Folded into single yes/no inputs** the caller must decide: First Schedule para 2 for non-individuals and para 9(2)-(3); s 4(2)(b)(iii); s 64(4)-(5); and several conditions in Part 3C.
- **s 150's payees exist only as text.**

**The shared `check.sh`:** a failing `#ASSERT REFUSED` shows up only as an error, not as a failed assertion, and an assertion that refuses is not counted at all. Each run here was also checked by hand for refusal warnings, and none were found.

## 6. Checks

See `encoding.json` → `checks`.
