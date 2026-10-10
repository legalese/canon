# Free Trade Zones Act 1966 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, as deposited at
`../../registers/source-bundle/FTZA1966.txt`. The cover says it incorporates
amendments "up to and including 1 December 2021", but the body is annotated with
Act 33 of 2023 (in force in two stages, 1 March 2024 and 25 November 2024) and
Act 24 of 2024 (wef 14 November 2024). The latest date annotated is 25/11/2024.

**Checks:** one case file, 55 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**7 of the 527 Singapore Acts** deposited here cite it. This row takes the rules a
trader, zone operator, cargo handler or shipping agent meets: what goods may come
in and be handled (s 5), the Director-General's permission for manufacture and
dutiable manipulation (s 6), retail trade, unpaid-duty goods and entry (ss 8-10)
and their penalties (s 10A), the operator licence (s 14A) and regulatory action
against a licensee (s 14P), disclosure of suspect goods (ss 14J, 14M), obstructing
officers (s 14Z), appeals (s 18(2)), officers of bodies corporate (s 23(1)) and
composition (s 23A). Not encoded: zone declaration (s 3), delegation (s 4), the
duty rate and valuation date (s 7), licence application and conditions
(ss 14B-14E), directions and reports (ss 14F, 14I, 14K, 14L), the shipping and air
cargo agent information duties (ss 14N, 14O), enforcement powers (ss 14Q-14X),
false statements (s 14Y), secrecy (s 16A), service (s 18A), the reverse burden of
proof (s 20) and regulations (s 24).

## What the Act turns out to say

### 1. The Part 2 fine has no fixed ceiling: it tracks the duty

s 10A(1) and (3): failing to obey an operator's direction under s 5(2), manufacturing
or dutiable manipulation without permission (s 6(1)), or using goods knowing duty or
GST is unpaid (s 9) carries a fine not exceeding "the greater of" $10,000 and "the
sum total of the customs duty and tax on the goods", or 12 months, or both. On
$50,000 of duty and tax the ceiling is $50,000. Unauthorised retail trade (s 8) is
a flat $10,000 fine and unauthorised entry (s 10) $5,000, neither with
imprisonment. Asserted.

### 2. A private operator, not Customs, is the first gatekeeper

Entry and residence (s 10(1)), retail trade (s 8(1)) and day-to-day handling of goods
(s 5(2)(b), "unless otherwise directed by the licensed FTZ operator") all turn on the
licensed FTZ operator's permission or direction. The Director-General may still bar a
person "despite any permission" (s 10(2)). Operating a zone without an FTZ operator
licence is itself an offence ($10,000, s 14A). Asserted.

### 3. Suspicions flow up a chain

A cargo handler with reason to suspect a contravention discloses to the licensed
operator (s 14M(3)), unless it is itself the operator, in which case it goes straight
to the Director-General under s 14J(1) (s 14M(2)). Each failure is a $5,000 offence
(ss 14J(2), 14M(4)). Asserted.

### 4. Licence sanctions: 14 days to answer, a $10,000 penalty only for breach

s 14P(3)(c) requires at least 14 days for written representations before any
regulatory action. A financial penalty (cap $10,000) is available only "for any
contravention under subsection (1)(a)" (licence conditions and non-offence
provisions), not for a false application or a conviction. Only a conviction for an
offence "committed during the term of the licence" is a ground. After the licence
ends, only censure and a financial penalty survive (s 14P(8)); the encoding reads
suspension or revocation of a lapsed licence as unavailable, which is an inference
from s 14P(8). Asserted.

### 5. Prescribed goods may only sit, or be surveyed with permission

Goods prescribed under s 5(4) lose the s 5(2)(b) freedoms, save storage for
transhipment, and survey and repacking with "the prior permission of a senior
officer of customs". Asserted.

### 6. A repeat s 14Z offender: "and", not "or"

s 14Z(e) gives a fine of $10,000 "or" 18 months "or both"; (f), for a second or
subsequent conviction, reads "a fine not exceeding $20,000 and to imprisonment for a
term not exceeding 3 years". Whether that makes both limbs mandatory is not decided
here; only the ceilings are asserted. Asserted.

### 7. Composition is capped at the lower of half the maximum fine and $5,000

s 23A(1), and only for offences "prescribed as a compoundable offence". No list of
compoundable offences was retrieved. Asserted.

## What would need doing before this is worth anything

- The Free Trade Zones Regulations (prescribed goods, prescribed periods, compoundable
  offences, fees) were not retrieved.
- The ceilings in s 10A depend on the duty and GST on the goods, which this row takes
  as a given number; the Customs Act 1960 and GST Act 1993 computations are not encoded.
- The s 20 reverse burden of proof and the s 23(2) liability for servants and agents
  are not encoded.
- No case law was searched.
