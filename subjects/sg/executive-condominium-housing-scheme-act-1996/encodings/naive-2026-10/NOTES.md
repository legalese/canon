# Executive Condominium Housing Scheme Act 1996 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation in force from
1 December 2025.

**Checks:** `l4 run ec-cases.l4` — 41 assertions satisfied, 0 errors,
0 warnings.

## What is encoded

ss 5, 6, 7 and 9 — who may not buy, what the developer must do when someone
disqualified has bought, the two windows in which the home may not be
transferred, and the nine grounds for compulsory acquisition.

Two things the Act leaves elsewhere and this encoding therefore takes as facts:
the **minimum occupation period**, which is prescribed rather than stated, and
the **regulations under s 3(2)**, which s 5(1)(d) makes a disqualifying ground
in their own right. Neither was retrieved.

## Three observations

**1. s 5(1)(c) has neither a time window nor a mental element.** Limbs (a), (b)
and (d) are each confined to a stated period — between application and the
temporary occupation permit, or the 30 months before application. Limb (c) is
not:

> has at any time … made any misrepresentation of a material fact or false
> statement in a material particular, **whether innocently or otherwise**,
> relating to the purchase of the housing accommodation

So an honest mistake, made at any time, disqualifies — and unlike the other
limbs there is no window after which it stops mattering. The words are
deliberate enough ("whether innocently or otherwise") that this is plainly
intended as to the mental element. Whether the absence of a window is equally
deliberate is less clear, and it is the only limb drafted that way. Asserted on
the applicant whose only true fact is an innocent misstatement.

**2. The same saving is written out twice.** s 5(9) saves a purchaser from
s 5(1); s 9(10) saves them from s 9(1)(b). The two are word for word the same
test — commercial property, acquired with the Minister's prior written consent,
not exceeding $250,000 "or such higher value as the Minister may allow". Both
are encoded, separately, because the Act states them separately; they are
asserted at the same boundary ($250,000 in, $250,001 out) in both places.

Two copies of one rule is a maintenance hazard rather than a defect: if a future
amendment moves one figure and not the other, a person could be eligible to buy
and liable to have the home compulsorily acquired for the same holding. Nothing
in the current text produces that, and the encoding would catch it if it
appeared, because the two caps are asserted independently.

**3. A contravention of s 7(1) has two consequences at once.** The transfer is
**void** under s 7(2) — not voidable, so it never happened — **and** the person
commits an offence under s 7(3). Both follow from the same contravention. A
reader who stopped at s 7(3) would think the transfer stood and a fine was the
price of it. Asserted as a pair on the same transfer.

## Also worth noting, not a finding

The appeal in s 5(4) runs to **the Minister**, "whose decision is final and
shall not be called in question in any court", and must be brought within
14 days of service. Fourteen days and no judicial review, against a notice whose
effect is to vest a person's home in the developer and forfeit the money they
have paid (s 5(7)). The encoding records the window and the freeze on lodging
while an appeal is pending (s 5(5)); it takes no view on the ouster.

## What would need doing before this is worth anything

- The minimum occupation period and the s 3(2) regulations carry a large part of
  the operative content and were not retrieved.
- s 8, transmission on death within 10 years of the permit, is not encoded and
  interacts with s 7.
- No case law was searched.
