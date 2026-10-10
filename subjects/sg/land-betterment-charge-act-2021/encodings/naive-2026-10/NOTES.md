# Land Betterment Charge Act 2021 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. NOT for public use.

**Edition:** informal consolidation, "version in force from 18/12/2023", as deposited
at `../../registers/source-bundle/LBCA2021.txt` (retrieved 1 October 2026). The latest
amendment annotated in the text is Act 23 of 2023 wef 18/12/2023 (to s 2 and the
provisional-permission dates in ss 8(3) and 26(2)).

**Checks:** one case file, 55 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0069** in `subjects/sg/requirements.jsonl`: Tier 2 of the remaining
Singapore Acts, ordered by everyday-life relevance. It asks what the Act decides for a
person or business it applies to; no scenario has asked a sharper question yet.

The Act taxes the increase in land value from a planning permission or a variation of
a title covenant. The money figures — the prescribed percentages and the Table of
Rates — are in Regulations, which were not deposited. So this row takes what the Act
itself decides for an owner, co-owner, tenant, charity or developer: who counts as an
owner (s 4), which method applies and when the charge is nil (ss 8(2), 9, 10(3), 11(1),
(2)), who pays (ss 15, 16), charity deferment (ss 20, 22(4)), the 24-month window
(ss 25(4), 27(2)), short levies (s 30), insolvency priority (s 33), contribution and the
first charge on land (ss 34 to 36), refunds (s 37), penalty tax (ss 41 to 43), offences
(ss 40(7), 45, 54) and appeal deadlines (s 47).

Not encoded: the definition of chargeable consent and the ordering of several events
(s 3), the relevant point in time (s 8(3), (4)), what the pre- and post-chargeable
valuations must take into account (s 11(3) to (6)), exemption, concessionary relief and
remission (ss 12 to 14), transfer of deferred liability (s 23), interest (s 38, prescribed
rate), the administration and enforcement powers (Part 8 apart from s 54), and Part 10.

## What the Act turns out to say

### 1. Unauthorised development costs the charge plus 30%, or 6%, 24% or 50%

s 41(1): penalty tax on a rectification order is the charge that would have been
payable plus "30% of the amount". The Authority may use 6% if the tax payer discloses
in writing before being told of an investigation, 24% if after being told but "before
the investigation is begun" (s 42), and 50% if the tax payer "hinders or obstructs" an
officer or valuer (s 43). A disclosure once the investigation has begun earns no reduction (encoded, not separately asserted).
None is payable if the tax payer proves it happened "solely because of circumstances
beyond the tax payer's control" short of "financial incapacity" (s 41(2), (3)). The
lower and higher rates are discretionary ("may"); the encoding gives the rate where the
power is used. Asserted.

### 2. A buyer of an uncompleted strata unit is not an owner; a tenant usually is not either

s 4(1): only someone with a "material interest" is an owner, and only an owner when the
consent is given is liable (s 15(1)(a)). A buyer of a lot from the developer "before that
completion" does not get a material interest by reason only of the purchase (s 4(4)). A
landlord receiving rent counts only if the letting is "for more than 10 years", counting
a lessee's option to extend (s 4(2)(d), (3)(a)): 10 years is not enough, 7 plus a 5-year
option is. A mortgagee in possession counts. A tenant under a private lease is not in the
list at all (an inference: s 4(2)(c) covers only leases "under a State title"). Asserted.

### 3. Selling the land does not end the liability, but a tenant can be made to pay from the rent

s 15(2): liability "continues despite the taxable person disposing of the land". On
default a lessee or occupier is responsible as if the defaulter, but only up to "any rent
or payments due" to the taxable person at the time of demand (s 35). The charge is "a
first charge on that land in priority over all other encumbrances whatever" (s 36(1));
when a portion is sold, it carries the charge in proportion to its area (s 36(2)).
Asserted.

### 4. Who must use a valuation, and who may choose one

The Table of Rates is the default (s 9(1)). Varying a special condition with a material
change of use, a covenant in a concessional title, a controlled activity covenant or a
subdivision control covenant must go by Valuation, and the same list attracts a higher
prescribed percentage (ss 8(2), 9(2)). Anyone else may elect Valuation, but only if "all
taxable persons concerned elect" before the liability order, and the election "is
irrevocable" (s 9(3), (5)). Either way, no charge if the value does not rise (ss 10(3),
11(2)). Asserted.

### 5. Deadlines are short for the taxpayer and long for the State

An appeal against a liability order must be made within 30 days; against any other
appealable decision, including a rectification order, within 14 (s 47(2)), and an appeal
does not suspend payment (s 48). The Authority may revise a liability order on its own
initiative for 24 months (s 27(2)), may demand a short levy within 2 years — without limit
for fraud or evasion (s 30(2), (3)) — and may recover the charge "at any time" (s 32).
A refund claim must be made within 6 years of the order becoming final (s 37(3)). At
exactly 24 months an estimated order is both final (s 25(4)) and still revisable
(s 27(2)) on the wording; this overlap is an inference; the cases assert revision still open at
24 months and the estimate final at 25. Asserted.

### 6. Charities may defer, unless they share ownership

s 20(2)(a): a charitable institution using the land wholly or mainly for charitable
purposes may get a deferment, and leaving the land unoccupied counts as charitable use
(s 20(4)). But not if the material interest is owned "jointly with a person who is not a
charitable institution" (s 20(3)). Asserted.

### 7. Evasion costs four times the tax

s 45(1): wilful evasion carries "a penalty of 4 times the amount of land betterment charge
which has been underpaid", plus a fine up to $50,000 or 5 years' imprisonment or both; a
false entry is presumed made with intent to evade (s 45(2)). Failing to restore land under
a rectification order: up to $200,000 or 12 months, plus $10,000 a day after conviction
(s 40(7)). Asserted.

## What would need doing before this is worth anything

- The Land Betterment Charge Regulations (prescribed percentages, Table of Rates, election
  period, interest rate, deferment criteria) were not deposited or read; without them no
  charge can be computed.
- s 3 (what counts as a chargeable consent, and which of several events counts) and s 8(3),
  (4) (the relevant point in time) decide the date and rate, and were not encoded.
- Exemption, concessionary relief and remission orders (ss 12 to 14) were not searched.
- No case law or SLA guidance was consulted.
