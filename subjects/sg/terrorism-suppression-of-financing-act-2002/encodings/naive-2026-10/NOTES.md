# Terrorism (Suppression of Financing) Act 2002 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, with amendments to Act 17
of 2022 (in force 1 July 2022) and First Schedule changes to S 568/2026 (in force
26 August 2026) shown.

**Checks:** one case file, 87 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**10 of the 527 Singapore Acts** deposited here cite it. This row takes what a
"terrorist act" is, the four financing offences and their penalty, the Minister's
exemptions, the two duties to tell the police, tipping-off, reach outside Singapore
and officers' liability: ss 2(2) to (5), 3 to 8, 9(4), 10, 10B, 14, 34 and 35. The
names in the First Schedule, the seizure and forfeiture procedure of Part 4 (beyond
the s 14 offence), mutual assistance and extradition, informer protection (s 10A),
the content of audit orders, and ss 36 and 37 are not encoded.

## What the Act turns out to say

### 1. A foreigner abroad who funds terrorism is caught; one who handles a terrorist's property is not

s 34(1) deems **every** person who does abroad what would be an offence under s 3, 4
or 5 to have done it in Singapore. But s 6 (dealing with terrorist property) and s 8
(duty to disclose) reach only persons in Singapore and Singapore citizens abroad
(s 6(1), s 8(1), s 34(2)), and s 10 (information about terrorism financing) reaches
only persons **in Singapore** — not even citizens abroad. Asserted.

### 2. The Minister cannot exempt support to a terrorist entity under s 4, but can under s 6

s 7(1) lets the Minister exempt a person from s 4(1)(b) or s 6. s 7(2) bars an
exemption from s 4(1)(b) where the property or services "will be used by or will
benefit a terrorist entity". No such bar applies to an exemption from s 6, so an
exempted bank may deal with a terrorist entity's property. An exemption never reaches
s 4(1)(a) (funding a terrorist act), s 3 or s 5. That an exemption fails when its
conditions are unmet is an inference from s 7(3) and (4). Asserted.

### 3. On the words, the exempted person still has to report; the people helping it do not

s 7(4) frees "any other person involved in carrying out" an exempted activity from
s 4(1)(b), s 6 "and section 8" if the exemption's conditions are met. s 7(1) frees
the named person only from s 4(1)(b) and s 6. Read literally, the named person keeps
the s 8 duty to tell the police while its counterparties lose it. This is a literal
reading and may not be what was intended. Asserted.

### 4. A company's fine can scale with the money; tipping-off cannot

For a non-individual, the s 6A maximum is the higher of $1 million or twice the value
of the property, services or transaction. The same formula applies to a company's
failure to disclose under s 8(1) and to s 10 where a financing offence was in fact
committed; otherwise $1 million. Tipping-off (s 10B) is capped at $250,000 or 5 years
for "any person", company or not. Individuals: s 6A $500,000 or 10 years; ss 8 and 10
$250,000 if the knowledge came at work, $50,000 otherwise. Asserted.

### 5. A terrorist act needs both a harm and a purpose — unless it is in the Second Schedule

s 2(2) needs one of nine harms and an intention (or reasonable appearance of one) to
influence a government or international organisation or to intimidate the public. A
violent robbery for gain is not a terrorist act; a peaceful petition is not either.
Second Schedule offences (hijacking, maritime, bombing and others) count without the
purpose limb. Official military activity governed by international law is excluded
"despite anything in subsection (2)", read here as covering the Schedule too. Asserted.

### 6. Funding a terrorist act needs wilfulness; supplying a terrorist does not

s 3 requires that the person act "wilfully and without lawful excuse". s 4 has no such
words: having reasonable grounds to believe the property or services will benefit a
terrorist or terrorist entity is enough. Civil immunity for reasonable measures
(ss 3(2), 4(2), 5(2)) is harder to get under s 6(3), which also requires all
reasonable steps to confirm the property was a terrorist's. Asserted.

### 7. Lawyers may tell clients, but not to further an illegal purpose

s 10B(3), (4) exclude disclosures by advocates and solicitors and in-house counsel to
clients for advice or for legal proceedings; s 10B(7) withdraws that if the disclosure
furthers an illegal purpose. A person who proves no reason to suspect prejudice has a
defence (s 10B(8)). Officers of a body that offends are guilty unless they prove
**both** no consent or connivance **and** due diligence (s 35). Asserted.

## What would need doing before this is worth anything

- Ministerial exemption orders under s 7 (one is annotated S 759/2022) and any
  audit orders under s 9 were not retrieved.
- The s 4(3) travel-financing extension and the s 2(1) definitions of "terrorist" and
  "terrorist entity" are folded into boolean inputs, not modelled.
- Imprisonment for a non-individual is encoded as 0 years; the text simply gives a
  fine only, and 0 is a modelling choice.
- No case law was searched.
