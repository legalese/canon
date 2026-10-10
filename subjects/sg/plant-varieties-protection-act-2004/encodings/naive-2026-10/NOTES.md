# Plant Varieties Protection Act 2004 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition (incorporating amendments up to 1 December 2021),
informal consolidation, version in force from 10 June 2022, as deposited at
`../../registers/source-bundle/PVPA2004.txt`. The latest amendments annotated are
Act 7 of 2022 (wef 26 May 2022) and Act 23 of 2019 (wef 10 June 2022, s 52).

**Checks:** one case file, 53 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

It is requirement **REQ-0084**: Tier 2 of the remaining Singapore Acts, ordered by
everyday-life relevance. The requirement asks what the Act decides for a person or
business it applies to; no scenario has asked a sharper question yet. This row takes
what a breeder, nursery, florist, farmer or home gardener meets: who the breeder is
(s 2), novelty and foreign priority (ss 14, 22), the duty to grant (s 21), term,
cancellation, invalidity (ss 24 to 27), the scope of the right, infringement and its
exceptions (ss 28 to 32), money remedies (s 30), compulsory licences (s 34),
denominations the Registrar must refuse (s 36(3)), offences and composition (ss 10,
11, 44 to 46, 52) and appeals (s 48). Not encoded: administration, application
procedure, publication and objections, provisional protection, competing independent
breeders (s 23), the expired 2014 transitional rule (s 22(4)), assignment and
licences binding successors, notice of protection (s 35), the register. No rules were
retrieved, so prescribed periods, fees and the genera exempt for farm-saved seed are
unknown here.

## What the Act turns out to say

### 1. A home gardener may propagate a protected variety; a nursery may not

s 31(1)(a): it is not an infringement to do "any act privately and for a
non-commercial purpose". The same act -- producing cuttings -- infringes when a
nursery does it without authorisation (ss 28(1)(a), 30(1)(a)). Research (s 31(1)(b))
and breeding another variety (s 31(1)(c)) are also free. Asserted.

### 2. Buying a licensed plant lets you resell it, but not propagate it

s 32(1): acts concerning material "sold or otherwise marketed in Singapore by or with
the grantee's consent" do not infringe, "unless such act involves ... further
propagation" (or export of propagable material to a country not protecting the
genus, except for final consumption). A retailer reselling licensed potted plants is
clear; a buyer propagating them for sale infringes. Asserted.

### 3. A foreign filing can rescue a sale that would otherwise kill novelty

s 22(1)(a)(i): a variety sold in Singapore with the breeder's consent "earlier than
12 months before" the application is not new (abroad, 6 years for trees or vines,
4 years otherwise). But s 14(1) lets a breeder who files here within 12 months of the
earliest UPOV filing have s 22 apply "as if" the application were made on the foreign
date. A Singapore sale 18 months before the Singapore filing destroys novelty -- unless
priority is claimed from a foreign filing 10 months before, which puts the sale
8 months before the effective date. A foreign filing 14 months before gives no
priority. Stock-increase and trial arrangements (s 22(2)) and sales of
non-propagating, non-harvested material (s 22(3)) do not count. Asserted.

### 4. Harvested material is caught only if the grantee could not act earlier

s 28(7): the grantee's rights reach harvested material from unauthorised propagation
"unless the grantee has had a reasonable opportunity" to act against the propagation
first. A florist selling cut flowers from pirated cuttings infringes; if the grantee
could have stopped the pirate earlier, not. s 30(1)(c) separately catches importing
harvested material from a non-UPOV country without consent; reading that limb as
reaching any harvested material (not only the s 2 defined term tied to s 28(7)) is an
inference, since otherwise it would add nothing to s 30(1)(a). Asserted.

### 5. Instability at grant invalidates only a grant made on a foreign report

s 25(2)(b): a grant is invalid for lack of stability or uniformity at the time of
grant only "where the grant of protection was made on the basis of an examination
report by an Examiner lodged under section 18". A grant after the Registrar's own
examination (s 17) is not invalid on that ground, though the Court must cancel it if
the variety "is no longer stable or uniform" (s 26(3)). Lack of novelty or
distinctness invalidates any grant (s 25(2)(a)). Asserted.

### 6. An innocent infringer pays profits, not damages

s 30(4): a defendant who proves he "was not aware and had no reasonable grounds for
supposing that it was an infringement" is not liable in damages; the claimant gets an
account of profits instead. s 35(3) lets the Court weigh whether the breeder labelled
the material (not encoded). Asserted.

### 7. Offences are fine-heavy, and composition is capped at $5,000

Falsifying the register: $50,000 or 5 years or both (s 44). Falsely representing a
variety as protected, and wilful or negligent misuse of a denomination: a fine up to
$10,000, no imprisonment (ss 45, 46). Disobeying a Registrar's summons or refusing
evidence: $2,000 or 3 months (ss 10, 11). Composition (s 52(1)) is capped at the lower
of half the maximum fine and $5,000 -- $1,000 for a summons offence, $5,000 for the
rest -- but only for offences prescribed as compoundable, which were not retrieved.
Asserted.

### 8. Protection lasts 25 years, and an unpaid annual fee forces cancellation

s 24(2): "25 calendar years from the date of the grant". s 26(2)(b): if the annual or
late fee "has not been paid within the prescribed period", the grant "must be
cancelled by the Registrar". Treating a grant removed from the register as no longer
in force is an inference. Only decisions to grant, to decline, and on denominations
are appealable under the Act itself (s 48(2)). Asserted.

## What would need doing before this is worth anything

- The Plant Varieties Protection Rules were not retrieved: fees, prescribed periods,
  the s 31(2) farm-saved-seed genera, compoundable offences and appeals by rules.
- Novelty is tested against one sale at a time; the s 22(1)(a) case of a sale in
  Singapore with exploitation abroad (or the reverse) is not addressed by the text and
  not modelled.
- The essentially-derived test (s 29) is reduced to four yes/no facts; how
  "predominantly derived" is judged is not in the text.
- No case law or IPOS practice directions were searched.
