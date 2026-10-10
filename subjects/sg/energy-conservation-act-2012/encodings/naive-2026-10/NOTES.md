# Energy Conservation Act 2012 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. Not for public use.

**Edition:** 2020 Revised Edition (incorporating amendments up to and including
1 December 2021), informal consolidation, version in force from 1 July 2026, as
deposited at `../../registers/source-bundle/ECA2012.txt`. The latest amendment
annotated is Act 10 of 2026 (wef 1 July 2026).

**Checks:** one case file, 51 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This Act is requirement **REQ-0067**: Tier 2 of the remaining Singapore Acts,
ordered by everyday-life relevance. The requirement asks what the Act decides for
a person or business it applies to; no scenario has asked a sharper question yet.

The row takes what a shop, an importer, a household or a business meets: the
restrictions on supplying and importing regulated goods (ss 12, 12A), how long
registration lasts and the appeal window (ss 15, 17), the maximum fines for the
goods offences (ss 12, 12A, 18 to 20), registering and cancelling as a large energy
user (ss 23, 25), the penalty scale for energy-management offences (s 32), entry
to premises (s 33), obstruction (s 38), fuel economy labels on vehicles for sale
(s 42) and composition (s 74).

Not encoded: which goods are regulated and what they must meet (Gazette orders
and regulations under ss 11, 22 and 78, none retrieved); the content of the
energy-management duties in ss 26A to 31 beyond their penalties; transport
facility operators (Part 4 Division 2) and Part 4 enforcement; type-approval
submissions (s 41); information powers (ss 34 to 37, 64 to 66); disclosure (s 71);
offences by bodies corporate (s 72); the court's remedial order (s 73); exemptions
(ss 61, 77).

## What the Act turns out to say

### 1. Since 1 July 2026 a household can commit an offence by importing a non-complying appliance for its own use

Act 10 of 2026 added s 12(1)(b) and (3A): a "prohibited import" is the import of
regulated goods that do not meet a prescribed requirement, on or after the
effective date, "by the person for the person's own use". There is no trade or
business element. The fine is up to $10,000 (s 12(2)). A waiver may be sought in
advance under s 31B(1). Asserted.

### 2. Selling your old appliance to a dealer is caught; selling it to a neighbour is not

A prohibited supply needs a trade link on either side: the supply is made "in the
course or furtherance of the firstmentioned person's trade or business" or "in
furtherance of the second-mentioned person's trade or business" (s 12(3)(b)). A
household selling a non-complying regulated fridge to a neighbour is outside it; the
same sale to a second-hand dealer, on the words, is a prohibited supply. Whether the
old fridge is "regulated goods" at all turns on the s 11 order, which was not read.
Asserted.

### 3. Developers and self-builders get a "complied when bought" defence; a developer that imported the goods does not

s 12(5) and (6) exempt goods supplied as part of premises by a developer, through a
developer's supply chain, or (for prescribed goods) to a person building premises
to occupy, if the goods complied when the supply agreement was made. The developer
and self-builder limbs fail if that person imported or manufactured the goods
themselves. Asserted.

### 4. A corporation that crossed the energy threshold cannot leave the register for three years

s 25(1)(a) lets a registered corporation that "no longer qualifies" apply to cancel,
but it is "subject to paragraph (b)": a corporation that qualified by reaching an
energy use threshold must have been below it "for a continuous period of at least 3
years immediately preceding the application". Read that way, a corporation dipping
below the threshold for two years stays registered. That (b) displaces (a) entirely
for threshold cases is an inference from "subject to". Asserted.

### 5. The energy-management penalties escalate, and the biggest is for skipping a design-stage assessment

s 32(1): $10,000 on a first conviction, $20,000 on a repeat plus $1,000 a day while
the offence continues after that conviction. s 32(3): $100,000 for failing to
conduct the energy efficiency opportunities assessment for a new venture (s
26A(1)(a)), ten times the first-conviction maximum for failing to submit its report.
s 32(4): $20,000 plus $500 a day for prescribed energy-consuming systems. False
data (s 31) carries $5,000 or 3 months. Asserted.

### 6. Composition is capped at $5,000 whatever the offence

s 74(1): a compoundable offence (outside Part 4) may be compounded for no more than
the lower of half the maximum fine and $5,000, so the $100,000 offence compounds for
at most $5,000. Which offences are compoundable is prescribed and was not read.
Asserted.

### 7. Smaller points

Goods registrations last 3 years, a supplier's registration indefinitely (s 15). An
appeal to the Minister is within 14 days and is final, and a revocation takes effect
on the date the Director-General specifies even while the appeal is pending, unless
the Minister directs otherwise (s 17). An authorised officer may enter during
business hours without notice, otherwise on 6 hours' notice unless the occupier
consents to less (s 33). A dealer offering a specified motor vehicle for sale without
the approved fuel economy label throughout its display commits an offence ($2,000,
s 42); a private seller does not. Asserted.

## What would need doing before this is worth anything

- The s 11 orders (which goods are regulated, and from when) and the regulations
  setting the requirements were not retrieved, so every "regulated" and "unmet
  requirement" is an input.
- The "related provision" rules in s 32(2) for pre-2018 convictions are not modelled.
- Part 4 Division 2 (transport facility operators) and the s 60 composition rule for
  Part 4 were not read.
- No case law or NEA guidance was searched.
