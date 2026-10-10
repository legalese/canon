# Encoding brief: the Goods and Services Tax Act 1993 (Singapore), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Goods and Services Tax Act 1993**: Singapore, 2020 Revised Edition, the informal consolidation printed by Singapore Statutes Online, version in force from 11 September 2026.

What the Act covers:
- **Part 1**: definitions.
- **Part 2**: the Comptroller and official secrecy.
- **Part 3**: the charge, covering:
  - scope;
  - supply;
  - time and place of supply;
  - reverse charge;
  - belonging;
  - rate;
  - value.
- **Part 4**: input tax.
- **Part 5**: zero-rating, exemption and reliefs.
- **Part 6**: special cases, including groups, partnerships, agents, VCCs, going concerns, vouchers, customs control and customer accounting.
- **Part 6A**: supplies spanning a rate change.
- **Part 7**: accounting, assessments, records, anti-avoidance and penal tax.
- **Part 8**: the Board of Review and appeals.
- **Part 9**: offences and penalties.
- **Part 10**: proceedings.
- **Part 11**: collection and enforcement.
- **Part 12**: general provisions, covering service, remission, refunds, advance rulings and transitional rules.
- **Schedules**:
  - First: registration.
  - Second: what counts as a supply.
  - Third: valuation.
  - Fourth: exempt supplies and imports.
  - Fifth: advance rulings.
  - Sixth: public schemes.
  - Seventh: overseas vendors and electronic marketplaces.
  - Eighth: reverse charge exclusions.
  - Ninth: fraud illustrations.
  - Tenth: prescribed information.

The source is `../source/GSTA1993.txt`, a copy of the text deposited in this repository; `../source/PROVENANCE.md` gives its origin. It is SSO's unofficial consolidation. In the deposited text, the s 39(4) table has its columns interleaved.

## The top-level goal, and the goals under it

Top level: *for this supply, is GST charged on it, and how — standard-rated, zero-rated, exempt or outside the scope; when does it take place; at what rate; how much tax is in the price; and who accounts for it?*

1. **The charge**: scope, place, belonging, rate, value, time of supply, distantly taxable goods, reverse charge, Seventh Schedule customers, rate changes (ss 39B, 39C, 40).
2. **Registration**: the First Schedule tests and dates, plus ss 30-33.
3. **Input tax and the net amount**: ss 19, 20, 34A, 41(7), 45A.
4. **Assessment, records, review and appeal**: ss 45-57.
5. **Collection, refunds, rulings and service**: ss 79, 83E, 87, 90, and the Fifth Schedule.
6. **Penalties and offences**: Part 9, ss 44(4), 46(6), 69, 73A, 74, 75, 81(4), 83I, 84, 86(1).

Inputs: the Comptroller's, the Minister's and the Board's discretions and satisfactions; prescribed matters and regulations; the classification of a supply under the Fourth Schedule and s 21(3); and facts.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's words beside each limb.
- Where the source does not answer, use `REFUSE "…"`; never `FALSE` or `0`.
- A failing assertion is a finding. Never edit an expected value to match the code.
- Read the diagnostics, not the exit code.

## Deliverables (in this `encodings/` directory)

`gst-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
