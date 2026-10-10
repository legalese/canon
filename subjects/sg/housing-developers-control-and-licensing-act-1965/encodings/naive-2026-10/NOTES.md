# Housing Developers (Control and Licensing) Act 1965 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition (amendments up to 1 December 2021, in operation
31 December 2021), informal consolidation "version in force from 1/7/2025", as
deposited at `../../registers/source-bundle/HDCLA1965.txt`. The latest amendment
annotated is Act 15 of 2025 (wef 1 July 2025).

**Checks:** one case file, 52 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Chosen for its **everyday-life relevance**: anyone who buys a new private home from
a developer in Singapore is a "purchaser" under this Act, and the licence, the
Project Account and the published audited accounts are what stand between the
buyer's money and a failed developer. (An automated count found 4 of the 527
deposited Singapore Acts citing it by this title; that undercounts and is not a
measure of importance.)

This row takes what a buyer meets: what counts as housing development and needs a
licence (ss 2, 4), suspension and appeal periods (ss 4(10), 7, 12(3)), the Project
Account (s 9), audited accounts (s 10), the secrecy of buyers' particulars (s 11(4)),
who may not run a licensed developer (s 25), and the maximum penalties and
composition sums. Not encoded: the application paperwork, the s 5 licence bars, the
Part 3A anti-money-laundering programme duties (only the s 12A penalty), auditors,
investigation and the Minister's rescue powers (ss 14-21), immunity, officer
liability, exemptions and the Public Prosecutor's consent.

## What the Act turns out to say

### 1. The buyer protections that matter most are not in the Act

Deposit limits, the progressive payment schedule, the conditions before a developer
may demand an instalment, the amount withheld until the certificate of statutory
completion, the standard form contract, void contract terms, show-unit accuracy and
the Project Account withdrawal rules are all things the Minister **may** prescribe by
rules (s 22(2)(c)-(m)). The Act itself fixes none of them. No rules made under s 22
were retrieved, so nothing here says what a buyer actually pays when. Not
asserted (nothing to assert).

### 2. Buyers' money is ring-fenced if the developer fails

s 9(5): Project Account moneys are "deemed not to form part of the property of the
licensed housing developer" if it compounds with creditors, has a receiving or
adjudication order, or goes into voluntary or compulsory liquidation, "despite any
other written law to the contrary". They vest in the official receiver, trustee or
liquidator to be applied for the authorised purposes, and only the balance after the
sale and purchase obligations are discharged goes to the general creditors (s 9(6)).
Asserted.

### 3. A developer can opt out of the Project Account

s 9(10): no Project Account is needed if no unit is offered for sale before
completion, or if the developer furnishes security of "not less than 140%" of the
total construction cost as certified by the architect. 139% does not do. Asserted.

### 4. Five units is the line, and lenders are outside it

"Housing development" is the business of developing, or financing the development or
purchase of, "more than 4 units" (s 2). Building four needs no licence; five does.
A licensed bank or insurer is not a housing developer "so long as" it only lends.
Developing without a licence carries up to $100,000 "and" up to 5 years (s 4(8)),
the heaviest term in the Act; breaching a licence condition or calling oneself a
"housing developer" without a licence carries 3 years (ss 4(9), 6(2)). Asserted.

### 5. Every buyer can read the developer's audited accounts, free

s 10(1): within 6 months of the financial year end, a licensed developer must send
its audited accounts and auditor's report to the Controller and make them available
"for inspection by the public without charge" at its office or on its website for
"at least 24 months". The Controller may extend the time "not more than once" and
by no more than 6 months (s 10(2)). Asserted.

### 6. Fraud bars a director for 5 years from the later of conviction and release

s 25(1)(a): the 5 years run from "the later of" the conviction date and the release
date. A director convicted six years ago but released three years ago is still
barred. An undischarged bankrupt is barred outright, as is anyone convicted of a
money laundering, proliferation financing or terrorism financing offence (no time
limit stated). Someone who held a responsible position in a developer wound up by the
court needs the Minister's written approval to hold one in "any other" developer
(s 25(2)). Reading "until the expiry of 5 years" as permitting the position once 5
full years have passed is an inference. Asserted.

### 7. Not every appeal to the Minister has the same words

Appeals run 10 days (licence grant, refusal or conditions, s 4(10)), 30 days
(revocation or suspension, s 7(3)) and 14 days (sale or reconstruction of the
business, s 12(3)). Sections 7(3) and 12(3) say the Minister's decision "shall not be
questioned in any court"; s 4(10) says only that it is "final". The encoding records
the wording, not its effect in court. A suspension may not exceed 12 months and must
be preceded by notice and a chance to explain (s 7(1), (2)). Asserted.

### 8. Buyers' particulars are secret

s 11(4): particulars of purchasers, intending purchasers and assignees obtained under
s 11 may be disclosed only with the Minister's prior approval for s 11 purposes, as
non-identifying statistics, to the Chief Statistician, if already public, or for
prosecutions. Up to $10,000 or 12 months (s 11(5)). Asserted.

### 9. Composition is capped at half the maximum fine

s 27A(1): a prescribed compoundable offence may be compounded for "not exceeding one
half" of the maximum fine. Which offences are prescribed is in rules not retrieved.
Asserted for the arithmetic only.

## What would need doing before this is worth anything

- Retrieve and encode the rules made under s 22 (their titles are not given in the
  deposit; that they are called the Housing Developers Rules is an inference): the payment schedule, deposit limits,
  standard form contract and withdrawal rules are where the buyer's rights live.
- The s 5 licence bars and the Part 3A anti-money-laundering duties are not encoded.
- s 4(8) says "and shall also be liable to imprisonment"; whether both are imposed
  together is a sentencing question not examined. The encoding records the maxima.
- No case law was searched, including on the effect of the differing finality wording.
