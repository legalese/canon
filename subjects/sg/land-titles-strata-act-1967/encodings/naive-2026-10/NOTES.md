# Land Titles (Strata) Act 1967 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation.

**Checks:** one case file, 45 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**24 of the 527 Singapore Acts** deposited here cite it. A strata owner meets it
chiefly through a collective ("en bloc") sale, which this row takes. Subdivision,
easements, termination of schemes and the procedural Schedules are not encoded.

## What the Act turns out to say

### 1. The objector has two grounds, and neither is "not enough money"

s 84A(7): the High Court is to approve the sale "unless" an objecting owner "will
incur a financial loss" or the proceeds cannot redeem a mortgage. s 84A(8): financial
loss means proceeds, after allowed deductions, **less than the price paid**. It is
expressly **not** a loss that one's gain is less than one's neighbours' (8)(b).
Receiving less than market value is not a ground at all. Asserted.

### 2. A buyer after the committee signs has no loss ground

s 84A(8)(c): an owner who "purchased the lot **after** a collective sale committee had
signed a sale and purchase agreement" is not taken to incur a financial loss, even if
they get less than they paid. Asserted.

### 3. One standing objection sends the case to court, with 14 days to get there

s 84A(6): with no objection, the Strata Titles Board **must** approve. s 84A(6A): with
objections, it must mediate; if any objection stands after 60 days, it **must** issue a
stop order. s 84A(2A), (2B): the majority may then apply to the High Court -- but only
after a stop order and **within 14 days** of it. Asserted.

### 4. "Good faith" is judged on three factors only

s 84A(9)(a)(i): the sale is refused if not in good faith "after taking into account
**only**" the sale price, the method of distribution, and the purchaser's relationship to
any owner. The committee's conduct of the process, as such, is not on the list.
Asserted.

### 5. The majority: 90% or 80%, by share value and area both

s 84A(1): 90% of share values **and** 90% of area if under 10 years from the latest TOP
(or CSC); 80% of each from 10 years. Asserted at the boundaries.

### 6. Top-ups for objectors are capped, and the committee holds a veto

s 84A(7A), (7B): the Court may increase an objector's proceeds if just and equitable,
paid out of everyone's proceeds, capped at the aggregate of the higher of 0.25% or
$2,000 per lot. The text can be read with "whichever is the higher" applied lot by lot
or to the two aggregates; the per-lot reading is encoded. And s 84A(9)(b): if the
committee does not consent to such an order, the sale **cannot** be approved.

### 7. No adverse possession of common property

s 28: no claim to common property or accessory lots by adverse possession, however long
the use. Asserted.

## What would need doing before this is worth anything

- **The First to Fourth Schedules** -- notice, meetings, the committee and deductions --
  are not encoded, and they decide most contested applications.
- **No case law was searched.** The good-faith test under s 84A(9) has a large body of
  Strata Titles Board and High Court decisions.
- The other collective-sale routes (ss 84D to 84FB) are not encoded.
