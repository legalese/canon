# Settled Estates Act 1934 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation (version in force from
1 April 2022), as deposited at `../../registers/source-bundle/SEA1934.txt`. The
revised edition incorporates amendments up to 1 December 2021; the latest amendment
annotated in the body is Act 25 of 2021, in force 1 April 2022, against s 15(2).

**Checks:** one case file, 54 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is **REQ-0041** in `subjects/sg/requirements.jsonl`: Tier 2 of the remaining
Singapore Acts, ordered by everyday-life relevance. The requirement asks what the Act
decides for a person or business it applies to; no scenario has asked a sharper
question yet.

The Act is short (32 sections), so most of it is here: what is a settled estate
(s 2, s 3(1)), the court's power to authorise sales and leases and the lease limits
(ss 4 to 6, 8), who may apply (s 7), whose consent is sought and what becomes of
those who do not give it (ss 9 to 13), who may be heard (s 15(2)), who acts for a
minor, a bankrupt or a person lacking capacity (s 16(2)), the married woman's separate
examination (s 17), conditions in leasing orders (s 24), and the uses of sale money
(s 27; s 29(2) in a comment only). Not encoded: the conduct of sales and conveyances,
lease covenants and preliminary contracts, service and newspaper notice (ss 14,
15(1)), who examines a married woman (ss 18, 19), the mechanics of approving leases
and vesting leasing powers (ss 20 to 23, 25, 26), ss 28, 29(1), 30, 31 and costs
(s 32). Every power here is a discretion of the court; the encoding takes the court's
satisfaction as a given fact.

## What the Act turns out to say

### 1. A married woman must be examined apart from her husband

s 17(1): where a married woman applies or consents, "she shall first be examined
apart from her husband" on her knowledge of the application, and it must be
ascertained that she "freely desires" it; s 17(2) makes this so even for her separate
property, and ss 18 and 19 say who certifies it in and outside Singapore. Nothing in
the Act examines a married man. The provision survives in the 2020 Revised Edition.
Asserted.

### 2. Silence is submission

s 10(3): a non-consenting party given notice who does not reply in time "shall be
deemed to have submitted his rights and interests to be dealt with by the court". s 11
does the same for someone who cannot be found, may be dead, or whom it would cost too
much to notify, once the court dispenses with notice. s 12 lets the court make an
order even over a refusal, with effect "as if all such persons had been consenting
parties". Only s 13 lets the court save the rights of those who refused or have not
submitted (or anyone it thinks ought to be excepted). Asserted.

### 3. Leases are capped at 21 years, or 99 for building and repairing

s 5(1): 99 years for building or repairing leases, or for other purposes where the
court thinks 21 years is not enough; otherwise 21. s 5(2) requires the best rent
"without taking any fine" (a premium), s 5(4) a deed with a counterpart, and s 6 bars
anything the settlor could not have authorised. Asserted.

### 4. A minor's land is a settled estate even with no settlement

s 2(b): "settled estates" include any immovable property to which a minor is entitled
in his own right, except a lease of at most 3 years which a minor "who has attained
the age of 18 years" executed as principal. So the Act contemplates a minor of 18 or
more. The Act does not define "minor"; that a minor here means someone under 21 is an
inference from the 18-year carve-out, not something the Act states. Asserted.

### 5. Only those in possession may apply; anyone may ask to be heard

s 7 limits applicants to persons entitled to possession or the rents and profits for
life, for a term ending on death, or a greater estate, their assignees, and trustees
for them. A remainderman waiting for the life tenant to die, or a lessee for a fixed
term, is not one (read from the words of s 7). But s 15(2) lets "any person or body
corporate, whether interested in the estate or not" apply to be heard. Asserted.

### 6. A settlor who keeps a reversion is a party to consent

s 3(1) deems undisposed reversions to come "under or by virtue of the settlement", so
under s 9 the settlor (or a testator's next-of-kin) holding one must concur or be
given notice, alongside every living beneficiary and trustees for unborn children.
Other trustees are served under s 14 rather than asked to consent. Asserted.

### 7. Sale money goes back into the land, not to the life tenant

s 27 lets the judge direct sale money and rents only to clearing incumbrances,
permanent improvements, buying land to be settled the same way, or paying someone
absolutely entitled. s 29(2) gives the life tenant the income of the money while it
waits. Asserted for s 27.

## What would need doing before this is worth anything

- No case law was searched, and the Rules of Court governing these applications were
  not retrieved.
- The relationship with any other statute dealing with trustees' powers of sale and
  leasing was not checked; whether applications under this Act are still made in
  practice is unknown.
- ss 18 to 23 and 25 to 32 are procedural and not encoded.
