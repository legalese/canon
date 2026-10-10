# Consumer Protection (Trade Descriptions and Safety Requirements) Act 1975 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation ("version in force from
1/7/2025"), as deposited at `../../registers/source-bundle/CPTDSRA1975.txt`. The
latest amendment annotated in the body is Act 13 of 2025 (wef 1 July 2025); the
Schedule is annotated S 796/2023 (wef 8 December 2023).

**Checks:** one case file, 57 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Chosen for its **everyday-life relevance** to ordinary people in Singapore: it is
the law behind a weight on a label, an expiry date, a gold-fineness stamp, an
odometer reading on a used car, a "government approved" claim, and the safety
rules for consumer goods. (An automated count found none of the 527 deposited
Singapore Acts citing it by this title; that count undercounts older and short
titles and says nothing about importance.)

The Act is short, so most of it is encoded: ss 2, 4, 5, 11(3), 13, 14 to 17,
19 to 21, 24, 26(3) and 31. Not encoded: s 3 (appointments), s 6 (what
"applying" a description means, taken as one input), s 7 (advertisements
referring to a class of goods), s 8 (pre-1975 trade marks), ss 9, 10, 12
(marking and advertisement regulations, whose content is in subsidiary
legislation not retrieved), s 18, the enforcement powers and procedure
(ss 22, 23, 25, 27, 28, 30), s 29 (noted only) and s 32.

## What the Act turns out to say

### 1. Price is not a trade description

The eleven matters in the s 2(1) definition cover quantity, manufacture,
composition, fitness (including expiry date), gold and silver fineness,
physical characteristics, testing, approval, place and date of manufacture,
maker, and history including previous ownership or use. **Price is not among
them**, and neither are the seller's own terms. On this reading (an inference
from the list, not words in the text), a false "was $99, now $49" is not an
offence under s 4 of this Act. Asserted.

### 2. Compliance with a Schedule law is an exemption under Part 2, but under Part 3 being regulated is enough

s 2(2) switches the Act off for a description subject to a Schedule law (Sale of
Food Act 1973, Health Products Act 2007, Electric Vehicles Charging Act 2022)
only where it is "applied in accordance with the requirements of that written
law". s 13 takes goods "subject to and regulated by" a Schedule law out of
Part 3 altogether, compliant or not, so the s 11(3) civil action for breach of
safety regulations is not available for them. Asserted.

### 3. Anyone hurt by unsafe goods can sue, but compensation in the criminal case is capped at $1,000

s 11(3) deems a trade supplier's breach of safety regulations "a breach of a
statutory duty for which action may be brought by any other person who may be
affected". Separately, a convicting court may order compensation of at most
$1,000 (s 31(1)), and that order does not affect a civil action for damages
beyond what was paid (s 31(2)). s 29: a contract is not void "by reason only"
of a contravention. Asserted (s 29 not modelled).

### 4. Newspapers and broadcasts are outside unless it is an advertisement; a private seller is always outside

s 2(4): a description published in a newspaper, book, periodical, film or
broadcast is not applied in the course of a trade or business "unless it is or
forms part of an advertisement". The offences in ss 4, 9(2), 11(2) and 14 each require the
course of a trade or business, so a private person selling her own phone
commits no s 4 offence even if the description is false. Asserted.

### 5. Penalties are modest and the officer provision reads "consent and connivance"

The general penalty is $10,000 or 2 years (s 15), which also covers the
unpenalised s 23(4) offence of disclosing trade secrets; obstruction and false
statements to officers carry $2,000 or one year (s 24). Offences may be
compounded for up to $2,000 (s 21) and are time-barred after 3 years (s 16).
s 17 makes a company officer liable where the offence was committed "with the
consent and connivance of" the officer, conjunctively, or is attributable to
their neglect; encoded as written, so consent without connivance is not
enough unless neglect is shown. Asserted.

### 6. The due diligence defence has a notice trap

s 19(1) needs both a cause beyond the accused's control (mistake, reliance on
information, another's act, accident) and all reasonable precautions. If the
defence blames another person, it cannot be run without the court's
permission unless written notice was served "within a period ending 7 clear
days before the hearing" (s 19(2)). An innocent supplier (s 19(3)) and an
innocent publisher of advertisements (s 20) have their own defences. Asserted.

### 7. Seized goods are lost after a month unless claimed

With no prosecution, seized goods are "deemed to be forfeited at the end of
one month from the date of the seizure unless a claim ... is made before then"
by written notice to the Director (s 26(3), (4)). Asserted.

## What would need doing before this is worth anything

- The regulations under ss 9, 10 and 11 were not retrieved; the safety regime
  is empty without them.
- Whether "consent and connivance" in s 17 is read disjunctively by the courts
  was not checked; no case law was searched.
- The relationship with the Consumer Protection (Fair Trading) Act 2003, which
  is where false price claims are more likely to be dealt with (an inference),
  was not examined.
- s 6 (applying a description, including oral statements and requests) and
  s 7 (class advertisements) are inputs here, not rules.
