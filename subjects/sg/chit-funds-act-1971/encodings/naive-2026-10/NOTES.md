# Chit Funds Act 1971 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, incorporating amendments
up to and including 1 December 2021. The latest amendment annotated in the body is
[40/2018] (ss 53, 54). SSO metadata: "Current version as at 01 Oct 2026".

**Checks:** one case file, 50 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**4 of the 527 Singapore Acts** deposited here cite it. This row takes who may run a
chit fund and use the word "chit" (ss 4, 5, 9, 18-20), the arithmetic of a sale
(ss 2, 24, 39), the subscribers' voting thresholds (ss 28, 33, 41), guarantors,
refunds and default (ss 30, 31, 34), recovery on termination (s 40(2)), the lending
limit (s 43), the reserve fund (s 44), the revocation clock (s 14), directors and
holding out (ss 59, 60), and the maximum fines and terms (with ss 7, 10, 49, 56, 61).
Licence applications and fees, branches, mergers, constitution changes, meeting and
minute procedure, books, transfers, financial limits left to regulations,
inspection, winding up and the regulations themselves are not encoded.

In the .txt deposit the arrangement of sections is column-shifted for ss 44-48: the
headings "Maintenance of reserve funds" and "Bad and doubtful debts" print without
numbers, so the numbers 44-46 sit against the next three headings. The body's
numbering is followed (s 44 is the reserve fund).

## What the Act turns out to say

### 1. A look-alike scheme is an offence for everyone, licensed or not

s 20(1) deems a scheme not based wholly on the s 24 terms, or inconsistent with them,
"only to partake of the nature of a chit fund". s 20(3) makes it an offence for any
person to promote, conduct or take part in one ($5,000 or 3 years or both), with no
carve-out for a licensed company, and s 20(4) makes rights under it unenforceable in
court. A genuine chit fund run otherwise than in accordance with the Act is caught
by s 18 at the same penalty. Asserted.

### 2. "Hwei", "kutu" and "tontine" count as "chit"

s 5(2) deems these, and like words in any language, derivatives of "chit". Only a
licensed chit fund company, someone with the Authority's written consent, or an
association of chit fund companies may use them in a business name ($1,000 or one
year or both). Asserted.

### 3. Failing to find guarantors costs the purchaser nothing; defaulting after buying costs everything

A purchaser must produce at least 2 guarantors before the prize is paid (s 30). One
who cannot within 2 weeks gets back earlier contributions "without any deduction
whatsoever", within 3 weeks of the auction (s 31(2), (3)), and the company must act
within 7 days (next highest bidder) or 2 weeks (fresh sale) after those 2 weeks. A
subscriber who has already purchased and then defaults, with the guarantors, owes
all contributions to the end of the fund immediately (s 34(1)). Asserted.

### 4. On a failed fund, only those who have not yet purchased get their money back

s 40(2): when a fund terminates otherwise than by expiry or a voluntary reduction
under s 33 (that is, by the company's failure, liquidation, winding-up steps or
revocation), every subscriber "who has not purchased" may recover actual
contributions from the company, or seek a court order that prize-takers keep paying
into court. Asserted.

### 5. Votes count heads and money

ss 28, 33 and 41 each require "a majority" whose contributions reach a fraction of
the chit fund amount: three-quarters to alter the agreement or adopt sealed tenders
(the latter before the first sale), two-thirds to reduce membership instead of
substituting a defaulter. INFERENCE: "majority" is read as more than half of those
voting, and "representing three-quarters" as at least three-quarters; the Act says
neither. Asserted.

### 6. The company may lend, but only to its own non-purchasing subscribers

s 43: no lending to anyone else, and no more than 75% of the subscriber's paid
contributions (or a percentage set by regulations, not retrieved). Such lending is
outside the Moneylenders Act 2008. The reserve fund takes at least 5%, 15% or 30% of
net profits according to whether it stands at 200% or more, 100% to under 200%, or
under 100% of paid-up capital (s 44(3)). Asserted.

## What would need doing before this is worth anything

- The Chit Funds Regulations (security, financial limits, the lending percentage,
  default penalties under s 32(2)) were not retrieved.
- s 5's catch-all "any other word indicating that it transacts chit fund business"
  and s 19's "all the attributes and incidents" limb are not modelled separately.
- Continuing-offence daily fines (ss 4, 5, 7, 10, 13, 48, 49) are not encoded.
- No case law was searched.
