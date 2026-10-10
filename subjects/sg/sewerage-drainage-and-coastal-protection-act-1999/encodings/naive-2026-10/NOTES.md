# Sewerage, Drainage and Coastal Protection Act 1999 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions of the example rows and nothing else. No pipeline, no coverage table,
no independent test pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, version in force from
1/7/2026 (`../../registers/source-bundle/SDCPA1999.txt`). The revised edition
incorporates amendments up to 1 December 2021; later amendments are annotated, chiefly
Act 38 of 2024 (wef 01/03/2025) and Act 8 of 2026 (wef 29/05/2026, which added Part 4A
on coastal flooding).

**Checks:** one case file, 51 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0068**: Tier 2 of the remaining Singapore Acts, ordered by
everyday-life relevance. The requirement asks what the Act decides for a person or
business it applies to; no scenario has asked a sharper question yet.

The Act runs to some 5,000 lines of text. This row takes what an owner, occupier,
contractor or discharging business meets: keeping private sewers and drains in order
(ss 10, 22A, 63), enquiring before digging (s 13A), discharges into the public sewers
(ss 16, 16A, 17), damage (ss 20, 30, 67A), drains and drainage reserves (ss 24, 24A),
water intake works (s 31), failing to comply with a notice (s 41), appeals (ss 9, 17,
22, 42, 47) and the penalties those sections set. Not encoded: Part 4A (coastal
flooding, ss 30A–30Q), s 22B flood protection measures, approvals procedure and
qualified persons (ss 32–36), enforcement powers, Part 7A compensation and
owner-initiated acquisition, cost recovery (ss 48–60), composition (s 70), and every
regulation, code or order made under the Act (none was retrieved).

## What the Act turns out to say

### 1. The emergency defence covers ordinary trade effluent, not hazardous discharges

s 16(6): a person is not guilty of discharging trade effluent without approval if the
discharge was "made in an emergency to avoid danger to life or property" and the Board
was told in writing as soon as reasonably practicable. s 16A, which governs dangerous
or hazardous substances (s 16(2) routes them there), has no such defence. An
emergency release of solvent, promptly reported, is still an offence. Asserted.

### 2. An order to stop a hazardous discharge must be obeyed while it is appealed; other notices are suspended

s 17(3): an aggrieved person "must comply with the order pending the outcome of the
appeal". A notice mentioned in s 41 (a repair notice, an obstruction notice) is instead
"suspended and need not be complied with" until the appeal is decided (s 42(1)(b)), and
so is anything appealed under s 47 (s 47(2)). Appeals run 14 days, except 28 days
against a notice of intention to vest a private sewer or drain in the Government
(ss 9(3), 22(3)) or a declaration under s 47. A tree notice under s 24A is in neither
the s 41 list nor the s 47(4) exclusions, so falls under s 47. A coastal protection
notice under s 30E(8) is excluded from both s 42 and s 47; no other appeal for it was
found (an inference from searching the deposit). Asserted.

### 3. A neighbour who uses your sewer or drain shares the duty to keep it in order

s 10(1A) (sewers) and s 22A(2) (drains): where a private system at one premises is
connected to and serves other premises, the owner of the other premises must also keep
it in proper order, at their own cost. Being connected without being served is not
enough. Neither section sets a penalty, so the s 63 general penalty applies: up to
$15,000 or 3 months, plus up to $500 a day after conviction. Asserted.

### 4. Discharge penalties carry minimum fines; damage penalties turn on a 0.9-metre pipe

Trade effluent without approval: at least $4,000 (first) or $10,000 (repeat), up to
$20,000 / $50,000. Hazardous discharge: at least $10,000 / $20,000, up to $50,000 /
$100,000, rising to $40,000–$200,000 / $80,000–$400,000 where it causes injury, death,
an inoperable sewer or severe disruption to treatment (s 16A(6)). Damaging the public
sewers is up to $50,000 (s 20(1)), but damage to "a pipe of 0.9 metres or greater in
diameter" is up to $200,000 or 2 years (s 20(2)). Ignoring an s 17 order carries "a
further fine of $2,000" a day — a fixed sum, not a maximum. Asserted.

### 5. The occupier is presumed to have discharged, and an employer cannot use the s 20 defence

Effluent discharged from premises is presumed the occupier's doing unless the occupier
proves "all reasonable precautions" and due diligence (ss 16(3), (4), 16A(2), (3)).
s 20(3) gives a due-diligence defence to damage, "but this defence is not available to
a person who may be liable by virtue of section 67A" — the employer or principal of
the person who did it, who must instead prove no consent or connivance and no neglect
of its own. Asserted.

### 6. Digging needs three things first, and drainage reserves are off-limits for ordinary uses

s 13A: anyone who breaks ground with "any mechanical equipment, tool or explosive"
without first obtaining the Board's plans, digging trial trenches and complying with the
Board's other requirements commits an offence — up to $50,000 or 3 years. s 24(1A):
parking a vehicle on a drainage reserve, leaving renovation debris in a drain, or
cultivating a reserve needs the Board's prior approval (up to $50,000 first, $100,000
repeat). A tree overhanging a reserve is the occupier's problem, not the landlord's
(s 24A(1)). Asserted.

## What would need doing before this is worth anything

- Part 4A (coastal flooding), added by Act 8 of 2026, is a whole regime for owners of
  prescribed places and is not encoded.
- The trade effluent and sewerage regulations, and the s 32 codes of practice that give
  "proper order" and flood protection measures their content, were not retrieved.
- Which offences are compoundable under s 70 depends on regulations not retrieved.
- No case law or Board practice was searched.
