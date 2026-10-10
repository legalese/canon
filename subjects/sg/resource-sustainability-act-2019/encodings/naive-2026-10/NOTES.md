# Resource Sustainability Act 2019 — naive encoding

**Method: naive.** Straight from the deposited text, following the conventions of
the example rows (the `writing-l4-rules` skill was not available in the session).
No pipeline, no coverage table, no independent test pass, no human gate. Not for
public use.

**Edition:** 2020 Revised Edition (incorporating amendments up to 1 December 2021,
in operation 31 December 2021), informal consolidation, deposited as
`../../registers/source-bundle/RSA2019.txt` (SSO "Current version as at 01 Oct
2026"). The latest amendments annotated are by Act 14 of 2023 (wef 26/05/2023,
08/03/2024 and 12/07/2024) and S 582/2024 (the Schedule, wef 12/07/2024).

**Checks:** one module (`rsa-retail.l4`), one case file (`rsa-cases-retail.l4`),
50 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is **REQ-0066** in `subjects/sg/requirements.jsonl`: Tier 2 of the remaining
Singapore Acts, ordered by everyday-life relevance. It asks what the Act decides for
a person or business it applies to; no scenario has asked a sharper question yet.

The Act is mostly about producers, scheme operators and large premises. This row
takes what a shopper or a shop meets: free take-back of old electrical goods (ss 14,
15), the disposable carrier bag charge with registration and deregistration (ss 23A
to 23D, 23F to 23H), the beverage container deposit and its refund (ss 23Q, 23U),
the maximum penalties for those offences (including s 23X, misuse of the deposit
mark, which is in the table but not separately asserted) and the composition cap
(s 49). Not encoded: producer registration and producers' e-waste duties (ss 8 to
13, 16, 17); packaging reporting (Part 4); bag-charge reports, records and
publication (ss 23I to 23L); producers' and operators' other beverage-scheme duties
(ss 23O, 23P, 23R to 23T, 23V, 23W); food waste (Part 5); scheme licensing (Part 6);
enforcement and appeals (Parts 7, 8).

Almost every threshold is left to subsidiary legislation, none of which was read:
which products are regulated or designated, which retailers are regulated, the
prescribed annual turnover, the deposit amount, and exempt bags, persons and
circumstances. They are flags or parameters here.

## What the Act turns out to say

### 1. A paper bag with handles is a disposable carrier bag

s 23A defines a disposable carrier bag as a bag with handles "other than a reusable
bag", and a reusable bag only by washable woven fabric, plastic of a prescribed
thickness or density, a prescribed carrying weight, or prescription. No material is
named for the disposable kind, so a paper bag with handles that meets none of those
tests attracts the charge. A bag without handles is outside the definition
altogether. Asserted.

### 2. The $0.05 is a floor, it cannot be refunded, and the offences are strict

s 23F(1): a registered retailer must charge "no less than the prescribed amount"
($0.05 unless substituted) per disposable bag to a customer who buys goods. s 23G
forbids reimbursing the charge "in money or in kind", and s 23H requires it on the
receipt "as a separate item". Each offence carries up to $10,000 or 3 months and "is
a strict liability offence" — none is worded "without reasonable excuse". Asserted.

### 3. The bag charge reaches a retailer two years after its turnover crosses the line

s 23B: a regulated retailer whose annual turnover for a trigger year "exceeds" the
prescribed figure must apply to register; for trigger year T from 2022, before 30
June of T + 1 (s 23C(1)(a)(ii)), and registration begins on 1 January of T + 2 (s
23C(3)(b)). Turnover equal to the threshold does not trigger the duty. A retailer may
apply to deregister after three consecutive years not exceeding the threshold, or on
ceasing to be a regulated retailer (s 23D). Asserted.

### 4. Large stores must take e-waste back with no purchase

s 15: a retailer with premises "of or more than 300 sqm" supplying a designated
product must accept one of the same class brought in for disposal. Nothing in the
section requires the person to buy anything. By contrast s 14's take-back on
delivery is one-for-one: only a consumer (an individual buying for household use, s
2), only on delivery to premises the consumer names, only for the same class, and
free of "any consideration ... (such as the cost of any labour or transport)".
Asserted.

### 5. A deposit may be waived only when the beverage is given away

s 23Q(5): the supplier "must not waive" the deposit "if X receives any consideration
in money for the supply". If it was waived and the recipient later collects the
deposit from its own customer, it must pass it back up (s 23Q(6)). The deposit is
not part of the price (s 23Q(8)). Asserted (except (8)).

### 6. The refund has four exits

s 23U: a return point operator must accept an empty marked and barcoded container
and refund the deposit, unless the mark or barcode cannot be read or scanned, it is
outside the operating hours specified at the return point, the operator "reasonably
believes" no deposit was paid or it was already refunded, or a prescribed exception
applies. Refusal without reasonable excuse carries up to $10,000 or 3 months.
Asserted.

### 7. Composition is capped at the lower of half the maximum fine and $5,000

s 49(1), for offences prescribed as compoundable (which ones was not read). So a
$10,000 offence compounds for at most $5,000, a $5,000 one for $2,500. Asserted.

## What would need doing before this is worth anything

- The regulations: which products are regulated consumer products and designated
  products, which retailers are regulated for the bag charge and at what turnover,
  the deposit amount, the bag exceptions, and which offences are compoundable.
- The 2021 trigger year (both dates prescribed) is not encoded.
- Second-conviction penalties (ss 23Q(7)(b), 23I to 23L, 23V, 23W) are not encoded.
- No case law or NEA guidance was searched.
