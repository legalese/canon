# Residential Property Act 1976 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation. The edition says it
"incorporates all amendments up to and including 1 December 2021"; the body also
carries S 26/2022 (wef 13 January 2022, s 4(4)) and Act 25 of 2021 (wef 1 April
2022, s 24(8)). The arrangement of sections at the head of the deposit is out of
step with the body from s 14B on; section numbers here follow the body.

**Checks:** one case file, 51 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**6 of the 527 Singapore Acts** deposited here cite it. This row takes what a
buyer, seller, heir, mortgagee or conveyancer meets: who is a foreign person, what
is residential and non-restricted property, the prohibition and its carve-outs,
the foreign heir, former citizens and PRs, foreign mortgagees, nominees, the s 25(5)
own-home approval, breaches of approval conditions, foreign governments and
religious groups, and the general penalty and composition. The 1973 foreign-company
regime and the Controller's attach-and-sell machinery (ss 5-8, 6A), conversion and
vesting of Singapore entities (ss 9-18, 26, 27), Registrar powers (ss 19, 20, 24),
confiscation (ss 4A, 23A), sale directions and change of use (ss 28, 28A), housing
developers (s 31), appeals (s 31A), exemptions (s 32) and rulings (s 34) are not
encoded. The Minister's discretions are inputs.

## What the Act turns out to say

### 1. A permanent resident is a "foreign person"

s 2 defines "foreign person" as anyone who is not a citizen, a Singapore company, a
Singapore LLP or a Singapore society. A permanent resident is not on the list, so a
PR buying a landed house needs approval like any other foreign person; s 25(5)(a)
then names being a PR as one ground on which the Minister may approve a natural
person buying a home for own and family occupation. Asserted.

### 2. Flats and condominium units are outside the Act, but not a whole development

s 4(1) disapplies the Act to a foreign person's acquisition of a non-landed flat in a
residential development, any unit in a development titled "condominium", and an
executive condominium unit. s 4(2) brings it back for "all the flats" or "all the
units" in a development, and s 4(3) makes that an offence with a fine of up to
$100,000 (no imprisonment is provided). Asserted. Reading s 4(1)(b) with the s 4(10)
definition of "unit" (which "includes a flat or dwelling house"), a strata landed
house inside a condominium development falls within s 4(1); that is this encoding's
reading of the words, and s 34 lets the Minister rule conclusively. Asserted.

### 3. A prohibited acquisition is void, and leases up to 7 years and mortgages are not caught

s 3(2): a purchase or acquisition in breach of s 3(1)(c) "is void". A mortgage,
charge or reconveyance is excepted (ss 3(1)(c), 33(b)), as is a lease or agreement
whose term, counting renewal options, does not exceed 7 years (s 33(d); s 4(7) for
whole developments; s 30(3) for foreign governments and religious groups). A 10-year
lease of a landed house is prohibited. Asserted.

### 4. A foreign heir does not inherit; the personal representatives have 5 years to sell

s 3(3): residential property "passes" to no foreign person by will or intestacy. s 3(4)
binds the personal representatives to sell to a citizen or approved purchaser within
5 years of the death (or an extension under s 3(12)) and pay the net proceeds to the
heir. s 3(13) exempts a surviving joint tenant. s 3(3) is not itself limited to
restricted property; this encoding lets s 4(1) exclude non-restricted property, which
is an inference. Asserted.

### 5. Former citizens and PRs must sell within 2 years

s 3A: an individual who bought restricted property as a citizen or PR and then loses
citizenship, or gives up PR other than to become a citizen, on or after 17 January
2011, must sell within 2 years (or a longer period the Minister allows before the 2
years end). Breach: $20,000 or 3 years or both. Asserted.

### 6. A breach of the own-occupation condition can cost three times the rent

s 25B: letting approved property against an occupation condition exposes the approved
purchaser to a Controller-imposed financial penalty up to the highest of $10,000,
three times the rent collected, or three times the assessed market rental. Breaching
any other condition is an offence under s 25C: up to $200,000 or 3 years or both, plus
$2,000 a day after conviction. Asserted.

### 7. Nominees, mortgagees, officers

A citizen buying restricted property as a foreign person's nominee commits an offence
($100,000 or 3 years or both), and the trust is void with "no resulting trust in favour
of the foreign person" (s 23). A foreign mortgagee that forecloses must sell within 3
years; s 22(4) confines that duty to foreign mortgagees. Where a body offends, its
officers are deemed guilty unless they prove both absence of consent or connivance and
due diligence (s 36(3), (4)). The Controller may compound prescribed offences for up to
$10,000 (s 36A). Asserted.

## What would need doing before this is worth anything

- The regulations prescribing compoundable offences (s 36A(2)) and any s 32 exemption
  notifications were not retrieved.
- The "Singapore company" chain test (s 2) is collapsed into three facts.
- The pre-17 January 2011 rule for counting rent under s 25B is not encoded.
- No Ministerial rulings under s 34 or case law were searched.
