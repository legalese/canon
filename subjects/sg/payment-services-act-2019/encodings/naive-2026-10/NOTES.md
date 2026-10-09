# Payment Services Act 2019 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation (amendments to Act 1 of
2021, in force 4 April 2024).

**Checks:** one case file, 23 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**16 of the 527 Singapore Acts** deposited here cite it. This row takes only the
licensing perimeter: who needs a licence, which one, and what is outside the Act.
Conduct and safeguarding duties, control of licensees, audit, Part 3 onwards and all
prescribed amounts (in regulations, not retrieved) are not encoded.

## What the Act turns out to say

### 1. "It's only a sideline" is no defence

s 5(2): a person providing a payment service while carrying on any business is
presumed to carry on a payment-service business "regardless whether" it is related or
incidental to the main business. Under s 5(2)(b) that presumption "is not rebutted" by
proving it is incidental. A shop that remits money for its customers needs a licence.
The fine is up to $125,000 or 3 years for an individual, $250,000 for others (s 5(3)).
Asserted.

### 2. The step from standard to major licence

s 6(5): a major payment institution licence is needed when either:
- the monthly average over a calendar year exceeds $3 million for any one service, or
  $6 million across two or more services; or
- the daily average e-money float exceeds $5 million.

A two-service firm at $2.5 million each stays standard. At $2.9 and $3.2 million it is
major on both limbs. Asserted.

### 3. What the Act does not reach

First Schedule Part 2 and s 13 take these out:
- commercial agents
- intra-group payments
- cash-in-transit firms
- free charitable carrying of cash
- technical providers that never hold the money
- limited-purpose e-money such as single-mall gift cards
- banks, finance companies and card issuers (exempt)

Asserted.

## What would need doing before this is worth anything

- **Retrieve the regulations.** The e-money account caps in s 24 and the exempt-provider
  classes in s 13(1)(e) are prescribed elsewhere.
- "Limited purpose e-money" and "technical service provider" turn on Part 3 definitions
  that are only paraphrased here.
- No MAS guidance or case law was retrieved.
