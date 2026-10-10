# Skills Development Levy Act 1979 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation (version in force from 1 July
2026; s 3 as amended by Act 4 of 2023, in force 15 June 2023).

**Checks:** one case file, 25 assertions satisfied, 0 errors. The first case is
requirement REQ-0004's own: monthly remuneration $4,200 gives a levy of **$10.50**.

## Why this Act, and why scoped

Requirement **REQ-0004** in `subjects/sg/requirements.jsonl`, raised by the
`cradle-to-grave-simone` scenario (event e041), asked what levy an employer pays for one
employee on $4,200 a month. This row takes who pays and how much (ss 2, 3), and the
penalties for false returns and their composition (ss 11, 17). The exemption orders, the
Fund, enforcement powers and the regulations on returns are not encoded.

## What the Act turns out to say

### 1. The figures are in the Act, not in regulations

REQ-0004 expected the rate, floor and cap to be in subsidiary legislation. As
deposited, s 3 states all three, as amended in 2023:
- **0.25% of the month's wages** (s 3(1)(a))
- **at least $2** (s 3(1)(b): "the greater of" the two)
- **no levy on wages above $4,500** a month (s 3(2))

So the levy runs from $2 to $11.25 a month per employee. Each figure applies "or such
[other] rate/amount as the Minister may, by notification in the Gazette, prescribe". No
notification was retrieved, so the encoding assumes the figures in s 3 are the ones in
force. Asserted.

### 2. Household staff are outside the levy

s 2: "employee" excludes "any domestic servant, gardener or chauffeur, wholly and
exclusively employed by an individual otherwise than in connection with his or her
trade, business, profession or vocation". A privately employed domestic helper attracts
no levy; a chauffeur employed for the individual's business does. Asserted.

### 3. False returns: one times or double the levy, plus a fine or prison

s 11(1), negligent or without reasonable excuse: a penalty equal to the unpaid levy, plus
up to $2,500 or 6 months. s 11(2), wilful with intent to evade: double the unpaid levy,
plus up to $5,000 or 3 years. The Agency may compound for up to $1,000 (s 17). The
deposit's arrangement numbers that section 15A; the body numbers it 17, and the body
was followed. Asserted.

## What would need doing before this is worth anything

- **Check the Gazette** for any notification under s 3(1)(a) or (2) changing the rate or
  the $4,500 ceiling. The encoding assumes none. *Partly checked on 11 Oct 2026:* the CPF
  Board's employer page on SDL (https://www.cpf.gov.sg/employer/employer-obligations/skills-development-levy,
  read 10 Oct 2026) gives the same figures. Those are 0.25% of total wages, $2 for wages under
  $800, and at most $11.25 above $4,500, so no change by notification is in force. The page
  adds a step the row does not model: the levy is computed for each employee, the amounts are
  added, and the **total is rounded down to the dollar**. Its example totals $40.75 and pays $40.
  The Act's source for that rounding was not found.
- The s 4 exemption orders and the wages excluded by notification under s 2 were not
  retrieved.
- No case law was searched.
