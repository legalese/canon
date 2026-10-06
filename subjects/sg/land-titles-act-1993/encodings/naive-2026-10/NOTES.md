# Land Titles Act 1993, Part 17 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation in force from
23 September 2026.

**Checks:** `l4 run lta-cases.l4` — 113 assertions satisfied, 0 errors,
0 warnings.

## Why this Act

The shortlist that produced this row named "LTA s 155". The Land Transport
Authority of Singapore Act 1995 has only 44 sections and no s 155; the Act
meant is the **Land Titles Act 1993** — `LTA1993` in the corpus — whose s 155 is
"Actions for recovery of damages", the claim against the assurance fund. That is
what is encoded here.

## Scope

**Part 17 only** — ss 151 to 159 — plus the two sections outside it that Part 17
cannot be read without:

- **s 46**, indefeasibility, which does the barring that s 155(1) requires; and
- **s 51A(4)**, electronic lodgment, which relieves the Registrar of the duty to
  inquire and so narrows what can count as a mistake of the Registrar.

That is one Part of nineteen, out of an Act of about **325,000 characters**.
Nothing here touches registration, caveats, easements, leases, mortgages,
charges, strata, or the court's rectification power in s 160. No rules under the
Act were retrieved, including the rules that fix what proportion of the
Registrar's fees constitutes the fund under s 151(1).

## What the Act turns out to say

### 1. The assurance fund does not insure the register. It insures the Registrar.

This is the thing a layperson will get wrong, and it is the first element of
s 155(1):

> any person who is deprived of land or sustains loss or damage **through any
> omission, mistake or misfeasance of the Registrar**, or any member of the
> Registrar's staff, in the bringing of the land under the provisions of this Act
> or in the registration of any instrument, **and who is barred by this Act from
> bringing any action for the recovery** of land, proceeds of the sale of land,
> moneys secured by a registered mortgage or interests protected by a caveat
> notified on a folio, may bring an action for the recovery of damages against
> the assurance fund.

A clean forgery that the Registry handled correctly on its face gives **no claim
at all**, however complete the owner's loss. The register has taken their land —
s 46(1) protects the proprietor "despite any lack of good faith on the part of
the person through whom that person claims", and s 157(1) adds that no such
purchaser "may be subject to action for the recovery of land **or of money**" —
and the fund does not answer for that. It answers for the Registry's own
mistakes.

Asserted: the clean-forgery fixture has `the claimant was deprived of land or
sustained loss or damage` true and `an action against the assurance fund lies`
false.

### 2. Section 51A(4) shrank the fund without amending Part 17

s 51A(4), on an instrument lodged in electronic form:

> (a) it is the duty of the person who certifies the correctness of the
> instrument under section 59 to ensure that all particulars entered therein are
> complete and accurate; and (b) **the Registrar need not be concerned to inquire
> into the completeness or accuracy** of the particulars as entered in the
> instrument and **must**, on acceptance of the instrument so lodged, **register
> the instrument in accordance with those particulars**.

s 155(1) needs an omission or mistake **of the Registrar**. Where the Registrar
had no duty to look and was obliged to register what was lodged, it is hard to
see what the omission or mistake is.

So the same inaccuracy produces a different answer depending only on the form of
lodgment. Asserted as that pair:

| | duty to inquire? | mistake of the Registrar? | fund claim? |
|---|---|---|---|
| paper lodgment, wrong particulars | **yes** | **yes** | **yes** |
| electronic lodgment, wrong particulars | no | no | **no** |

The modernisation of conveyancing moved the duty of accuracy onto the certifying
solicitor and left Part 17 asking about the Registrar. Nobody amended s 155.

### 3. Section 155(4) is a deeming, not a priority rule

> For the purposes of this section, any person who **may bring** an action for the
> recovery of land, proceeds of sale of land or moneys secured by a registered
> mortgage or charge, or interests protected by a caveat notified on a folio **is
> deemed not to have been deprived** of the land or suffered any loss or damage.

It does not merely withhold the fund claim from a person who has another remedy.
It deems them to have suffered **no loss at all**.

So the owner whose land was taken by a forger and sold on, and who can still sue
the forger for the proceeds of sale, has for the purposes of s 155 lost nothing
— whatever the forger's whereabouts or means. Asserted: identical facts, with
and without an available action against the forger, and only the second gives a
fund claim.

### 4. And the extension in section 158(2) names only one of the ways that action can fail

> **s 158(1)** No action under section 155 shall lie unless such action is
> commenced **within 12 years from the date on which the deprivation occurred or
> the loss or damage was sustained**.
>
> **s 158(2)** Where an action for deprivation, loss or damage has been commenced
> against any person within the period of 12 years …, an action against the
> assurance fund for the same cause may be commenced **within one year after the
> discontinuance of the former action**, even though the period of 12 years may
> have expired.

Put findings 3 and 4 together and the structure is this. s 155(4) obliges the
claimant to exhaust the action against the fraudster before the fund claim exists
at all. s 158(2) then gives them a fresh year only if that action is
**discontinued**. A claimant who fights it to judgment and loses, or whose action
is dismissed, or whose defendant is wound up with nothing in it, gets no extra
year — and the twelve years will usually have gone.

Asserted: discontinuance last year (in time), discontinuance three years ago
(out), and losing the action against the forger at year thirteen (out).

The twelve years also run **from the deprivation, not from discovery**. A register
error can sit undetected for a generation, and the clock runs from the error.

### 5. The fund never pays for a boundary error — unless the Registrar corrects it

s 155(3): "**No compensation is to be paid** out of the assurance fund **under any
circumstances**" for loss occasioned by —

- (a) the issue of a **qualified folio**;
- (b) any **incorrect description of the parcels, the boundaries or dimensions
  (including area)** provided by the Chief Surveyor, or incorrect particulars of
  the alienation forwarded by the Collector;
- (c) any incorrect or absent description of parcels or dimensions **where no
  survey has been carried out**.

Limbs (b) and (c) exclude the commonest practical error in a land register:
getting the boundaries or the area wrong. "Under any circumstances" — so no degree
of fault in the Registrar brings it back. Asserted on fixtures that each have a
proved Registry error and still fail.

s 151(5) adds that the fund is never liable for loss "occasioned by the **breach
by a proprietor of any trust**".

**But s 159(5) is a separate route and it is not subject to any of that:**

> Any person who, **having dealt on the faith of an erroneous registration**, has
> suffered loss or damage **by the exercise of the power conferred on the Registrar
> by this section** is, subject to section 158, entitled to be compensated from
> the assurance fund for the land of which the person has been deprived and for
> any improvement made thereon …

It asks for **none** of the three things s 155 asks for: no omission, mistake or
misfeasance of the Registrar; no requirement of being barred from an action for
recovery; and the s 155(4) deeming does not reach it. It is subject only to the
s 158 limitation period, and it is narrower in measure — the land and the
improvements, where s 155 speaks of damages generally.

And s 159(2)(a) expressly empowers the Registrar to correct "the **wrong
description of parcels or of the boundaries or dimensions (including the area)**
of the land" — the very subject matter s 155(3)(b) excludes.

So the route to compensation for a mis-described boundary runs **through the
Registrar choosing to correct the register**, and not otherwise. Asserted as that
triple: s 155(3) excludes it, the s 155 action fails on it, and s 159(5)
compensates it once the correction is made.

### 6. Where two titles are involved, the Registrar picks the loser by what it costs the fund

s 159(4): in correcting the register the Registrar must have regard to
improvements made since the error, "and, **where 2 or more titles are involved, he
or she may correct that folio, entry or endorsement which in his or her opinion
involves the least loss to the assurance fund**."

Two innocent proprietors, one error, and the tie-breaker is the fund's exposure
rather than anything about their positions. Asserted.

### 7. The claimant must beat the Registrar's tender by more than a fifth

s 156(2): the Registrar may tender the amount claimed or any lesser amount, "and
if the claimant rejects that tender and **fails later to recover damages exceeding
the amount tendered by 20% of that amount**, the claimant must pay, **in addition
to the claimant's own costs**, the costs of the Registrar in defending the
action."

The claimant must beat the tender by **more than a fifth**, not merely beat it:

| tender | recovered | beat it? | beat it by enough? | who pays the Registrar's costs |
|---|---|---|---|---|
| $100,000 | $90,000 | no | no | **claimant** |
| $100,000 | $115,000 | **yes** | no | **claimant** |
| $100,000 | $120,000 | yes | no — "exceeding … by 20%" | **claimant** |
| $100,000 | $130,000 | yes | **yes** | the fund |

All four asserted, including the exact-20% boundary.

And s 156(3) gives the claimant costs only on recovering **final judgment**,
"except as provided in subsection (2)"; s 156(4) says "**in all other cases**, the
Registrar's costs are payable by the claimant". So the only cost-free outcome is
a final judgment that also beats the tender by more than a fifth. Accepting the
tender bears the Registrar's costs. Settling bears them. Asserted.

### 8. An offer, not an acceptance, ends the liability fight

s 155(6): on receipt of notice the Registrar "is entitled to appear in any such
action and **may offer to compensate** any party to the action out of the
assurance fund."

s 155(7): "**On any such offer being made**, further action is limited to
determination of the compensation to be paid."

The consequence attaches to the **making** of the offer. Nothing requires the
claimant to accept it, or the amount to be adequate. Asserted as
`NOT the claimant must accept the offer for section 155(7) to bite`.

### 9. Smaller things worth recording

**A volunteer takes no better title.** s 46(3): "Nothing in this section confers
on a proprietor claiming **otherwise than as a purchaser** any better title than
was held by the proprietor's immediate predecessor." So the forger's gift to a
relative is reachable where the forger's sale to a buyer is not — and s 154(1)(d)
says the same thing from the other end, allowing an action against "any person
claiming through that proprietor **otherwise than as a purchaser**". Asserted on
both.

**The buyer's own agent is not a predecessor.** s 46(2)(a) defeats the title of a
proprietor where the fraud or forgery was one "to which that proprietor **or that
proprietor's agent** was a party or in which that proprietor or that proprietor's
agent colluded". A buyer whose solicitor was in on it is outside the protection.
Asserted.

**An unlawful statutory acquisition is deemed fraudulent.** s 154(5): "any
unlawful acquisition of land, **whether by a person purporting to act under
statutory authority** or otherwise, is deemed to be fraudulent." So an
acquisition under a power that turned out to be invalid falls within s 154(1)(d)
without anyone proving dishonesty. Asserted, including that the fixture's own
`deprived of land by fraud` field is false.

**Contributory fault can defeat the claim entirely.** s 155(2): the court "may
**withhold** or abate damages or compensation accordingly" for the claimant's own
"neglect, default or incaution". Not merely reduce. Asserted as a pair where the
action lies and nothing is recovered.

**Section 157(2) protects the official and not the fund.** It makes the
Authority, the Registrar and their officers not "**personally** liable" for
anything in good faith done or omitted. s 155 asks about omission, mistake or
misfeasance and not about good faith, so the official's good faith is no answer to
the fund. Asserted as
`NOT the Registrar's good faith is an answer to a claim against the fund`.

**$1,000 is the whole of the simplified route.** s 156(5): a person "deprived of
land to a value of **not more than $1,000**, or sustaining loss or damage of not
more than that amount, may claim against the assurance fund **in the first
instance**" — and the words "despite anything to the contrary in section 155"
switch off the s 155(4) deeming and the barred-from-recovery requirement for such
a claim. s 151(2) matches it: the Registrar may authorise payment of a claim "not
exceeding $1,000" alone, and anything above needs the Minister in writing or a
court determination. Asserted at $1,000 and $1,001.

**The fund running dry is not the claimant's problem.** s 151(4): "If the amount
to the credit of the assurance fund is inadequate to meet any claim, the
deficiency is charged on and paid out of the **Consolidated Fund**." Asserted.

**The fund also pays the costs of litigating against the Registrar's refusals.**
s 152(4): costs the court orders the Registrar to pay on a summons under s 152
"are to be paid out of the assurance fund"; s 153(2) does the same for a stated
case certified to involve a question of public importance. s 151(1)(b) makes room
for both. So compensation under s 155 shares an account with the costs of
proceedings against the Registry — though s 151(4) means the competition is about
the fund's accounts rather than about whether a claimant is paid. Asserted.

## What would need doing before this is worth anything

- **No case law was searched**, and this is an area with a settled body of it.
  Findings 1, 2, 3 and 5 are readings of the words. Finding 2 in particular — that
  s 51A(4) narrows s 155 — is an inference from two provisions that do not
  mention each other, and it may well have been argued and decided.
- **s 160 (the court's power to rectify the land-register) is not encoded**, and
  s 46(1)(g) makes indefeasibility subject to it. A claimant's real options
  include an application under s 160, and this row is silent about it.
- No rules under the Act were retrieved, including those fixing the proportion of
  fees that constitutes the fund under s 151(1).
- The onward references are not followed: s 59 (certification of correctness),
  s 142 (statutory obligations), the State Lands Act 1920, the Residential
  Property Act 1976 s 24, and the Chief Surveyor's and Collector's functions.
- **One Part of nineteen.** Any question about registration, caveats, priority,
  easements, leases, mortgages or strata is outside this row entirely.
