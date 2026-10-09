# Land Acquisition Act 1966 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation.

**Checks:** one case file, 17 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**13 of the 527 Singapore Acts** deposited here cite it. This row takes only the
compensation rules (ss 33, 34). Notification and declaration, the Collector's inquiry
and award, the Appeals Board procedure, possession and temporary occupation are not
encoded.

## What the Act turns out to say

### 1. A low value declared for tax caps the compensation

s 33(5)(d): if the owner stated a value for tax or duty within 2 years before the
declaration, and it was accepted, the market value "is deemed not to exceed" it. An
owner who under-declared to save stamp duty is held to that figure. Asserted.

### 2. No hope value

s 33(5)(e): market value is capped at what a buyer would pay under the current zoning,
and "no account is to be taken of any potential value" for a more intensive use. Any
uplift from an unlawful use is also ignored (s 33(5)(b)). Asserted.

### 3. Betterment offsets only the damage heads

s 33(2): any increase in the value of the owner's other land "is to be set off only
against" severance and injurious-affection damages. It never reduces the market value,
relocation costs or title costs. If betterment exceeds the damage, the damage head is
nil, not negative. Asserted.

### 4. The Board's closed list

s 33(1) says "the following matters and no others". s 34 excludes:
- urgency
- the owner's reluctance to sell
- value the project will add
- renovations after the notification, unless they were necessary repairs approved by
  the Commissioner of Lands
- unregistered transactions
- comparable sales, unless the **appellant** proves they were bona fide and not
  speculative

Asserted.

### 5. The valuation date

s 33(1)(a): the date of the s 3 notification, if a s 5 declaration follows within
6 months; otherwise the date of the declaration. Asserted.

## What would need doing before this is worth anything

- The Appeals Board procedure and the time limits for appeal were not encoded.
- "Market value" itself is a valuation question, taken here as an input.
- No case law was searched. Appeals Board and High Court decisions on s 33(5)(e) are the
  real content.
