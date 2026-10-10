# United Nations Act 2001 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation (version in force from
28/4/2023), with amendments to Act 18 of 2022 (wef 28/04/2023) shown.

**Checks:** one case file, 51 assertions satisfied, 0 errors.

## Why this Act, and why scoped

**11 of the 527 Singapore Acts** deposited here cite it. The Act has seven
sections, so this row encodes all of the operative ones (ss 2 to 7). It leaves out
only the short title, the list of things regulations may provide for (s 2(1)(a),
(b)), laying regulations before Parliament (s 2(6)), expenses (s 2(7)) and the
Frustrated Contracts Act saving (s 3(2)). The Act itself prohibits nothing: every
actual sanction lives in regulations made under s 2, and none was retrieved.

## What the Act turns out to say

### 1. Banks and VCCs are outside the UN Act measures if MAS merely could direct them

s 2(2): the measures "do not apply to any financial institution ... to the extent
that [it] is or may be subject to" MAS directions under s 15 of the Financial
Services and Markets Act 2022 (wording from Act 18 of 2022). s 2(3) does the same for
VCCs under s 83 of the Variable Capital Companies Act 2018. "Or may be" means the
carve-out does not wait for MAS to act: sanctions for these institutions run through
MAS, not this Act. Asserted.

### 2. s 2(1) is "subject to subsection (2)" only, yet s 2(3) carves out VCCs too

The opening words of s 2(1) name only subsection (2). The VCC carve-out added in
2018 (s 2(3)) is phrased as a flat exclusion of "the measures to be applied under
subsection (1)", and is given full effect here. The cross-reference was apparently
not updated (an inference from the text, not something it says).

### 3. Every form of participation carries the full penalty, and a company cannot be imprisoned

s 5(1): commits, attempts, an act with intent, counsels, procures, aids, abets,
incites, or conspires "(whether in Singapore or elsewhere)" — all liable to the same
maximum: for an individual $500,000 or 10 years or both; "in any other case" a fine
up to $1 million and no imprisonment. Asserted.

### 4. Regulations beat any other written law except the Constitution

s 2(5): no regulation is invalid because it deals with a matter covered by other
written law, or is inconsistent with "any written law other than the Constitution".
That inconsistency with the Constitution can invalidate is read from the exception,
not stated. Asserted.

### 5. Non-performance caused solely by sanctions cannot be sued on

s 3(1): no proceedings lie against a contracting party, or anyone under a written law,
for failing to act where the failure is "solely attributable to" the Act or
regulations. The encoding treats a tort duty as outside both limbs (an inference: the
section names only contracts and written law). The Frustrated Contracts Act 1959 is
unaffected (s 3(2)). Asserted.

### 6. Citizens are reached abroad, and a s 6 trial blocks extradition

s 6(1): a citizen offending outside Singapore may be dealt with as if the offence were
committed here. s 6(2): proceedings that would bar later proceedings at home also bar
extradition for the same offence. s 7: a District Court may impose the full penalty
despite the Criminal Procedure Code. s 5(2): prosecution under other law is not
barred, but "no person shall be punished twice for the same offence". Asserted.

## What would need doing before this is worth anything

- The regulations made under s 2 (the actual prohibitions) were not retrieved; without
  them the encoding says who is liable and for how much, but not for what.
- "To the extent that" in s 2(2), (3) is reduced to a yes/no for the matter in hand.
- Whether the Act reaches a non-citizen acting outside Singapore (beyond conspiracy
  "elsewhere") is not decided; the encoding answers only what s 6 or territoriality
  gives.
- s 4 honest belief and s 3 "solely attributable" are taken as given facts.
- No case law was searched.
