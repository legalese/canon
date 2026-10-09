# Building Control Act 1989 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation (amendments to Act 12 of
2020 and Act 15 of 2026).

**Checks:** one case file, 46 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**33 of the 527 Singapore Acts** deposited here cite it (s 2 by 11). Most of its
377,000 characters regulate the building industry and building performance. This
row takes what a home owner, occupier or small builder meets: building without
approval, moving in, falling windows, and unlicensed building. **The building
regulations** -- which say what an "exterior feature" and "insignificant building
works" are -- **were not retrieved.**

## What the Act turns out to say

### 1. A falling window: presumed fault, and a seven-day window to name the contractor

s 25H: the "person responsible" for an exterior feature -- for a private flat, the
**owner** (s 22A) -- commits an offence ($20,000 or 12 months) by failing without
reasonable excuse to keep it secure. If it falls and there is disrepair not caused
by accident or nature, failure is **presumed** (s 25H(2)). The owner escapes by
showing another's faulty materials or work (s 25H(3)), or by naming their contractor
by statutory declaration "**not later than the 7th day** after a notice" and showing
good-faith reliance (s 25H(4)). Day 8 is too late. Asserted at days 5 and 10.

### 2. Deviating from plans is an offence without knowledge

s 20(3), (4): anyone "directly concerned" who deviates materially from approved plans
commits an offence ($100,000 or 2 years), and "it is not necessary for the
prosecution to prove that an accused knew". The defence is to prove the accused did
not know and **could not reasonably have known**. Building without approval at all
is $200,000 or 2 years (s 20(1)). Asserted.

### 3. A TOP is not evidence of compliance

s 12(4): a temporary occupation permit "is only prima facie evidence that a building
is suitable for occupation and is **not** to be taken to be evidence of compliance with
the provisions of this Act, the building regulations or any other written law". A
buyer who moves in on a TOP has no statutory comfort that the building complies.
Asserted.

### 4. Occupying "any building where any building works have been carried out"

s 12(1): no occupation without a certificate of statutory completion (or a TOP), of
"any building where any building works have been carried out". Read literally that
reaches an existing home after approved works, not only new buildings. The encoding
follows the text; the question is flagged, not answered.

### 5. Smaller things worth recording

- **s 22A:** for HDB common property the Town Council (or its contractor) is the person
  responsible; for condominium common property, the owner of the common property or
  its managing agent.
- **s 4(1)(d):** works prescribed as "insignificant" are outside Part 2 entirely.
- **s 29B:** carrying on a builder's business, or holding out as licensed, without a
  licence.

## What would need doing before this is worth anything

- **Retrieve the Building Control Regulations**, especially the list of exterior
  features and insignificant building works.
- **No case law was searched.**
- Periodic façade inspection (Part 5) and the maintenance notices (Part 4A) are not
  encoded.
