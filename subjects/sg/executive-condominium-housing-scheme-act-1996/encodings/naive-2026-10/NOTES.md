# Executive Condominium Housing Scheme Act 1996 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation in force from
1 December 2025.

**Checks:** `l4 run ec-cases.l4` and `l4 run ec-death-and-transfer-cases.l4`
— 83 assertions satisfied, 0 errors, 0 warnings.

## What is encoded

**ss 3 to 13 — the whole Act** except s 1 (short title), s 2 (interpretation)
and s 14 (the Minister's general power). `ec-act.l4` covers who may not buy,
the developer's duties, the transfer prohibition and compulsory acquisition;
`ec-death-and-transfer.l4` covers the regulation power, developers, death of
the owner, the resale premium, service, immunity and transfer to a non-citizen.

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
- No case law was searched.

*(Superseded in part — see the section added with ss 3, 4, 8 and 10 to 13 below.)*


---

# Added with sections 3, 4, 8 and 10 to 13

## s 8: three clocks, and a family can lose the home by meeting only two

When the owner dies **within 10 years** of the temporary occupation permit, the
transmission cannot be registered without the Minister's **prior written
consent** — testate or intestate alike, so a will makes no difference. s 8(3)
then gives the Minister three independent grounds to vest the home in the Board:

- **(a)** no representation taken out within **12 months** of the death;
- **(b)** representation taken out, but no application for consent within
  **6 months** of the date of representation;
- **(c)** consent obtained, but the transfer not effected within the period the
  Minister specified.

These do not reinforce each other — they stack. A family that probates promptly,
satisfying (a), and then takes seven months to write to the Minister loses the
home on (b). Asserted as exactly that case: `limb (a)` not made out, `limb (b)`
made out, home vested.

And on registration the title vests **"free from all encumbrances"**, with the
Registrar required to cancel any mortgage or charge overreached. The lender's
security goes with the family's title.

The only procedural protection is s 8(4): written notice, stating the
compensation and a lodging date **not earlier than 28 days** after service. Read
that against s 11(1), which deems service effected by **affixing the notice to a
conspicuous part of the accommodation**, and s 11(2), which lets it be addressed
to "the owner" **without further name or description**. The 28 days can begin on
a notice pinned to the door of a house whose owner has died, addressed to
nobody.

## s 12 protects good faith alone

"No suit ... shall lie ... for or on account of ... anything which is **in good
faith** done or intended to be done" by the Government, the Board, a public
officer or a person acting under the Minister's direction.

There is **no reasonable-care limb**. Compare s 19(1) of the Silver Support
Scheme Act 2015 and s 19(1) of the Advance Medical Directive Act 1996, both of
which require good faith **and** reasonable care. Here an honest but negligent
decision to vest someone's home in the Board attracts no suit at all. Whether
that difference is deliberate is not something the text settles; it is visible
only when the three Acts are put side by side.

## Two smaller points

**Almost none of the eligibility test is in the Act.** s 3(2)(b) leaves to
regulations "the qualifications as to income, the minimum size of the family,
citizenship of and ownership of any other properties". s 5(1)(d) then makes a
breach of those regulations a disqualifying ground in its own right, which is
how they bind. The Act supplies the enforcement and the regulations supply the
rules. Asserted as a list of what is left out.

**s 10 creates a duty with no amount.** A purchaser who previously bought public
housing from the Board "must pay to the Board a premium of **such amount as the
Board may determine**" — no formula, no ceiling, no appeal. The trigger is
encodable; the quantum is not in the Act at all.

## What would still need doing

- s 14, and the s 13(1) excepting circumstances, which the deposited text sets
  out in a list this encoding carried as one supplied fact.
- The minimum occupation period and the s 3(2) regulations.
- The compensation and High Court deposit machinery in s 8(6).
- No case law was searched, and no human gate has been sought.
