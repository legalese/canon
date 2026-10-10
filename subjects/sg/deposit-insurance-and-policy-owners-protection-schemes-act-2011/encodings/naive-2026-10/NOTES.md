# Deposit Insurance and Policy Owners' Protection Schemes Act 2011 — naive encoding

**Method: naive.** Straight from the deposited text, following the `writing-l4-rules`
conventions of the example rows (the skill itself was not loaded in this session).
No pipeline, no coverage table, no independent test pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, headed "version in force
from 9/3/2025", as deposited at `../../registers/source-bundle/DIPOPSA2011.txt`. The
latest amendment annotated is Act 5 of 2025 (wef 9 March 2025, to s 82). The $100,000
Maximum DI Coverage is annotated S 706/2023 wef 1 April 2024.

**Checks:** one case file, 52 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Chosen for its **everyday-life relevance**: nearly everyone in Singapore has a bank
account or an insurance policy, and this Act sets how much of it is protected if the
bank or insurer fails. (An automated count found 4 of the 527 deposited Singapore Acts
citing it by its slug title; that undercounts, and is not a measure of importance.)

This row takes what a depositor or policy owner meets: who is a DI Scheme member (s 5),
what is an insured deposit and who an insured depositor (s 2, First Schedule), when
compensation may be paid (s 21), the depositor's entitlement (ss 22, 23, 26), what is
an insured policy (s 2), life-policy categories and protection ratios (s 47, Second and
Fourth Schedules), deductions and refunds (ss 47(6), 48, 48A, 48B), joint holders
(ss 23(3), 49), settlement options (s 50A) and false statements about cover (ss 67, 70,
71). Not encoded: exemptions, the funds, premium contributions and levies, prescribed
products under s 22(5), Part 5A resolution withdrawals, subrogation and recovery,
transfer and run-off (s 54), liquidators, the Agency, the Third Schedule levy formulas,
and other offences.

## What the Act turns out to say

### 1. A depositor's debts to the bank are ignored; a policy owner's are deducted

s 22(6): in computing deposit compensation "the liabilities (if any) that are owing
from the insured depositor to the failed DI Scheme member are disregarded". A depositor
with $85,000 in deposits and a $200,000 loan from the same bank still gets $85,000. But
s 47(6) requires outstanding policy loans and premiums to be deducted from life-policy
compensation where a claim event or termination happened on or before the
quantification date, and s 48A(6) deducts outstanding premiums on general policies.
Asserted.

### 2. Nothing is paid automatically when a bank fails

s 21(1): on a winding-up order, a voluntary winding up, or MAS's opinion that the
member is insolvent, "the Authority **may** determine that compensation be paid". The
duty to pay follows a determination, not the failure. Asserted.

### 3. $100,000 is one cap across most accounts, but there are separate caps

s 22(1) aggregates deposits in the depositor's own name, their share of joint
accounts, their sole-proprietorship's accounts and SRS moneys under one $100,000 cap.
CPFIS and CPFRS moneys get a separate cap (s 22(4)); each trust or client account gets
its own cap, split equally among joint trustees (s 22(2), (3)); and after a merger, a
depositor in both banks keeps two caps if the merged bank fails within one year
(s 26). Joint accounts are split equally unless the bank's books say otherwise
(s 23(3)). Asserted.

### 4. What is insured is narrow, and pledging does not remove cover

The First Schedule covers Singapore-dollar savings, fixed and current accounts at a
Singapore branch, and Singapore-dollar CPFIS, CPFRS and SRS moneys, "regardless of
whether such a deposit is pledged". Foreign-currency deposits are not covered and
structured deposits are expressly excluded. A bank is an "excluded person" and cannot
be an insured depositor (s 2). Paragraph (b) (CPFIS, CPFRS, SRS) names no
Singapore-branch requirement; the encoding follows the words, and whether that is
meant is an open question. Asserted.

### 5. Life policies are scaled by a ratio, not simply capped

Fourth Schedule: Category 2 sum assured is protected at the ratio of $500,000 to the
aggregate sum assured on that life across all such policies, applied to each policy:
a $400,000 policy on a life insured for $1,000,000 in total yields $200,000. Surrender
values use $100,000, annuities use $100,000 against the commuted value (so a $1,000
annuity payment on a $200,000 commuted value becomes $500), group policies $100,000
per policy. Category 1 (health and accident) is protected in full. Asserted.

### 6. Personal-line general policies count only if issued to a person

s 2: life, accident and health and compulsory (motor third-party, work injury) policies
are insured policies whoever holds them; personal motor, travel, property and maid
policies count only when "issued to a natural person" and a Singapore policy. Taking a
settlement option before the quantification date ends PPF Life Fund cover (s 50A).
Asserted.

### 7. Telling a customer something is insured when it is not is a serious offence

s 67: knowingly or recklessly making a false or misleading statement whether a deposit
is insured or a policy is an insured policy (or about membership) is an offence "even
though a contract does not come into being": up to $125,000 or 3 years, doubled fine
for a corporation (s 71(1)). Whether s 71 also doubles the $12,500 daily fine is not
modelled. Asserted.

## What would need doing before this is worth anything

- The general-business maximum compensation (s 48A(2)) and payment rules are in
  regulations and Agency Rules, which were not retrieved.
- Riders and benefit-by-benefit classification under the Second Schedule are
  simplified to whole policies.
- The Third Schedule's 30-day window for general-business protected liabilities was
  not encoded.
- No MAS or SDIC guidance, and no case law, was consulted.
