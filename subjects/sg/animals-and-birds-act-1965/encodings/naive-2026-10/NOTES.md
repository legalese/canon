# Animals and Birds Act 1965 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation ("version in force from
1/3/2022"), with amendments to Act 23 of 2021 (s 42(1)(c), in force 1 March 2022)
shown.

**Checks:** one case file, 100 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**10 of the 527 Singapore Acts** deposited here cite it. Most of the Act is
import, export and disease-control machinery run by officers. This row takes what
a pet owner or an animal-related business meets: the meaning of "animal-related
business" (s 41), the duty of care (ss 41B, 41C), cruelty (s 42), the penalties
for those and the nearby offences (ss 30, 39, 43, 43A, 48), disqualification and
loss of the animal (ss 43B, 44(3)-(4)), notice before a destruction direction
(s 45(2)), compensation for destroyed animals (ss 19(3), 21, 40(12), 46) and
composition (s 69). Import and export licensing, Part 3 disease powers, rabies
orders, livestock control, enforcement powers, veterinary licensing and
quarantine are not encoded, and no code of animal welfare or rule made under the
Act was retrieved.

## What the Act turns out to say

### 1. Ignoring a code of animal welfare is a duty breached but not an offence

s 41C(1)(d) requires every owner to take reasonable steps to ensure the animal
is cared for in accordance with the codes of animal welfare. But s 41C(2) makes
only a failure under "subsection (1)(a), (b) or (c)" an offence, and s 41B(1) says
no one is liable "by reason only" of failing to observe a code. The code still
matters in court: s 41B(2) lets either side rely on compliance or non-compliance
"as tending to establish or negate any liability". The encoding has two rules,
one for the offence and one for falling short of s 41C(1) at all; an owner who
ignores only the code is caught by the second and not the first. Asserted.

### 2. Doing it in a business multiplies the maximum, and the repeat tier is $100,000

For breach of the duty of care (s 41C(3)) and for cruelty (s 42(4)), an offence
"in the course of carrying on, or employment or purported employment with, an
animal-related business" carries up to $40,000 or 2 years, and $100,000 or 3
years for a second or subsequent offence. Outside a business the duty-of-care
maxima are $10,000 / 12 months and $20,000 / 2 years; cruelty's are $15,000 /
18 months and $30,000 / 3 years. Asserted.

### 3. "Repeat offender" is defined and then never used

s 41C(4) says "a person is a repeat offender if" convicted under s 41C(2) after an
earlier conviction under s 42(1)(f) as in force before 16 January 2015. But
s 41C(3) speaks only of a "second or subsequent offence"; the words "repeat
offender" appear nowhere else in what was read. The encoding reads (4) as making
an old s 42(1)(f) conviction count as the first offence for s 41C(3) -- an
inference -- and gives cruelty no such carry-over. Asserted.

### 4. An owner is deemed to permit cruelty by failing to supervise

s 42(2): "an owner is deemed to have permitted cruelty to an animal, if the owner
has failed to exercise reasonable care and supervision". So an owner whose
carer beats the dog commits the s 42(1)(b) offence without knowing of it; a
bystander who is not the owner does not. Slaughter for food is outside s 42
"unless ... accompanied by the infliction of unnecessary suffering" (s 42(3)).
Asserted.

### 5. A food business is never an "animal-related business"; an unpaid breeder may be

s 41 excludes "any business in respect of animals intended for consumption", so
a poultry farm or a live-seafood tank is outside the higher business penalties.
"For reward" is written into the care and service limbs, not into "using or
holding animals for display, sport, entertainment, sale, breeding or
conservation", nor the rescue limb. Reading it that way (an inference), an
unpaid hobby breeder and a volunteer shelter are animal-related businesses, and a
neighbour minding a dog for nothing is not. Asserted.

### 6. Disqualification reaches only three offences, for at most 12 months

s 43B(1): only on conviction under "section 41C(2), 42(1) or 43(3)", and "for a
period not exceeding 12 months". Failing a Director-General's welfare direction
(s 43A) does not qualify. A business offender is barred from the business or from
being in charge of animals in one; anyone else may be barred "from owning any
animal". Separately, s 44(3)-(4) lets the court take the animal from an owner
convicted of any Part 4 offence, but only if satisfied it "is likely to be
exposed to cruelty" if left. Asserted.

### 7. Compensation for a destroyed animal is almost never payable

None for an animal destroyed for examination (s 19(3)), under the anti-rabies
provisions (s 40(12)), by court order, on an officer's welfare directions or at
the request of a professed owner (s 46: "No compensation is in any case
payable"). For a diseased animal destroyed under s 20, s 21(1) says none, but
s 21(2) lets the Minister authorise a sum. The encoding confines s 21(2) to s 20
destructions -- an inference from its place in the Act. Asserted.

### 8. Smaller rules

Failing to produce a dog that has bitten someone is fine-only, up to $2,000
(s 39(3)). Burying a carcase is not an offence once 24 hours pass after the
report with no instructions (s 30(3)); exactly 24 hours is not asserted. An
officer cannot direct destruction of an animal in its own enclosure off public
places until the known owner has been notified (s 45(2)). Composition is capped
at $1,000 and only for offences "prescribed as a compoundable offence" (s 69).
Asserted.

## What would need doing before this is worth anything

- No code of animal welfare, and no rule or order under the Act, was retrieved:
  which businesses are "prescribed" under s 43, which offences are compoundable
  under s 69, and what animals are prescribed under s 2 are all unknown.
- The "repeat offender" reading of s 41C(4) and the scope of s 21(2) are
  inferences and should be checked against case law or the amending Act's
  debates.
- s 41's "animal" (Part 4) differs from s 2's (rest of the Act); the encoding does
  not decide whether a creature is an animal.
- Import and export licensing (ss 8, 16) and the remaining disease and rabies
  powers are not encoded.
