# Regulation of Imports and Exports Act 1995 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, with amendments to Act 16
of 2026 (in force 30 September 2026) shown. Part 3 (trade information certificates)
is as inserted by Act 26 of 2025, in force 29 September 2026.

**Checks:** one case file, 88 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**10 of the 527 Singapore Acts** deposited here cite it. The Act is mostly a shell:
the actual import and export controls are made by regulations under s 3, and none
were retrieved. This row takes what the Act itself decides. That covers what counts
as an import, an export and "goods" (s 2), and the penalty ceilings for every offence
in the Act (ss 3(3), 7, 10A, 10E-10H, 11, 16, 17, 19, 27-31). It also covers who may
issue a certificate (ss 10A(4), (5), 10H), surrender of cancelled permits (s 7),
action against authorised issuers (s 10D), reporting seizures (s 13(2)), examination
costs (s 20(3)), false declarations (s 28), incorrect trade descriptions (s 28A),
liability for agents (s 36(4)), composition (s 39) and appeals (s 39A). Search,
seizure, arrest and computer-inspection powers, the computer service, the disclosure
gateways in s 31(1), informers and cross-border railway preclearance are not encoded.

## What the Act turns out to say

### 1. An authorised issuer who issues a false certificate faces a tenth of the fine a self-certifier does

s 10E: an authorised certificate issuer who issues a trade information certificate it
"knows or ought reasonably to know is false or misleading" faces at most **$10,000** or
2 years, with no higher tier for a repeat offence. s 10H(4), (5): a manufacturer or
exporter who self-issues a false preferential certificate of origin faces
**$100,000** (first offence) or **$200,000** (repeat). Anyone who merely tampers with
an entry in a certificate (s 10F) faces the greater of $100,000 or 3 times the value
of the goods. The 2025 Part 3 is new. The text does not say why the trusted issuer has
the lowest ceiling. Asserted.

### 2. Most fines scale with the value of the goods

For breach of the trade regulations (s 3(3)), posing as an authorised issuer (s 10A(6)),
tampering (s 10F), false representations about certificates (s 10G) and incorrect
trade descriptions (s 28A), the ceiling is "$100,000 or 3 times the value of the
goods ..., whichever is the greater", rising to $200,000 or 4 times on a repeat. On
$1m of goods a first offence reaches $3m. Under s 10G(2), where a certificate is
passed off as covering other goods, the multiplier applies to those other goods
("goods Y"). s 3(3) is a ceiling on what the regulations may provide, not itself an
offence. Asserted.

### 3. Composition is capped at $5,000 however large the offence

s 39(1): a prescribed offence may be compounded for at most $1,000 if its maximum fine
is under $5,000, otherwise $5,000. A value-linked offence on $1m of goods, with a $4m
ceiling on a repeat, compounds for at most $5,000, *if* it is prescribed as
compoundable. Which offences are prescribed is in regulations not retrieved. Asserted
(the ceiling only).

### 4. Transit is neither import nor export

s 2: goods that leave on the same conveyance they arrived on, without being landed or
transhipped, are neither imported nor exported. Landing or transhipping them makes
them both. "Goods" excludes choses in action and money, except collector's pieces,
investment articles and currency notes "in substantial quantities". Asserted.

### 5. Reverse burdens throughout

A false declaration (s 28) is an offence unless the accused proves "all reasonable
steps" to check it. A principal is liable for a partner's, agent's or employee's act
(s 36(4)) unless the principal proves **both** lack of knowledge and all reasonable
precautions. Asserted.

### 6. Electronic permits need not be surrendered, and appeals do not suspend

s 7(3) exempts permits issued by electronic notice from the duty to surrender a
cancelled or suspended permit. s 39A: an appeal must be in writing, with adequate
grounds, within 14 days of service. The decision must be complied with pending the
appeal unless the Minister directs otherwise, and the Minister's decision is final.
Asserted.

## What would need doing before this is worth anything

- The Regulation of Imports and Exports Regulations (the actual controls, permit
  requirements and compoundable-offence list) were not retrieved; without them the Act
  answers almost no "may I import this?" question.
- "One month" in s 13(2) is modelled as a boolean, not a date computation.
- s 3(3) is a ceiling on regulations, so the encoded s 3(3) fine is the most a
  regulation could provide, not what any regulation does provide.
- The s 39 composition rule is read as using the offence's maximum fine as computed
  for the case at hand. For value-linked offences that is never under $5,000. This
  reading is an inference, not something the text says expressly.
- No case law was searched.
