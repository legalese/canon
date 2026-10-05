# Work Injury Compensation Act 2019 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation in force from
1 December 2025 — so it carries the S 694/2025 uplift to the compensation
figures, in force 1 November 2025.

**Checks:** `l4 run wica-cases.l4` — 32 assertions satisfied, 0 errors,
0 warnings.

## Scope

s 7 and First Schedule paragraphs 1–3, out of 8 Parts and about 333,000
characters. That is liability and quantum: whether the employer must pay, and
how much. Part 3A (platform workers), the insurance Parts, the claims procedure
and appeals are **not encoded**.

## A defect in our own deposit, not in the Act

**Tables A and B of the First Schedule cannot be read from the deposited text.**
The PDF-to-text extraction has lost or shifted values at page boundaries. Three
places where it is visible:

- Table A runs `… 31 → 122`, then a page break, then a bare `32` with no factor
  and `33 → 121`. One row has lost its number.
- Near the end: `65 → 58`, then a bare `53` with no age, then `66 and above →
  48`. Here the *age* is missing instead.
- Table B shows the same pattern at its own page breaks.

So the deposit cannot be used to compute a compensation figure, because the
factor for a given age is not reliably recoverable from it. The encoding
therefore takes the factor as a **supplied fact** and encodes everything built
on it — the formula, the floors, the caps, the partial-incapacity percentage —
exactly as the Schedule states them. Those are all in running prose and extract
cleanly.

This is a finding about the corpus, not about the law. Fixing it means going
back to `WICA2019.pdf` and extracting the two tables properly.

## Two observations on the Act

**1. The cap is not the most that can be paid — the final figure exceeds it by a
quarter.** First Schedule paragraph 2 defines compensation for total incapacity
as `C + 0.25C`, and defines C as the product of AME and the Table B factor,
*then clamped* to the floor and cap. The clamp bites on C, and the uplift is
applied afterwards. So with the post-November 2025 cap of $346,000, the amount
actually payable at or above the cap is **$432,500**.

The structure is plain once laid out, and it is almost certainly deliberate —
the uplift reflects the need for constant care, and capping after it would
defeat that. But a reader who takes "$346,000" as the maximum payout will be
wrong by $86,500. Asserted at both the cap and the floor.

**2. Partial incapacity at 100% loss of earning capacity pays less than total
incapacity.** Paragraph 3 multiplies **C** by the percentage of loss of earning
capacity. Paragraph 2 pays **C + 0.25C**. So an employee assessed at 100% loss
of earning capacity under paragraph 3 receives C, and an employee with total
incapacity receives C plus a quarter — a 20% difference on identical C.

There is a coherent reading: "permanent total incapacity" and "100% loss of
earning capacity" are different findings, and the quarter is for care rather
than for lost earnings. But the two sit adjacent in one Schedule and the
difference is not explained anywhere in it. Asserted as the pair at the end of
the cases.

## Also worth noting

s 7(4) deems an accident arising **in the course of** employment to have arisen
**out of** it, "in the absence of evidence to the contrary". So the two limbs of
s 7(1) are not independent in practice: an employee proves the second and the
first follows unless the employer displaces it. The encoding models the
rebuttal as its own fact so that the burden is visible.

## What would need doing before this is worth anything

- **Re-extract Tables A and B from the PDF.** Until that is done this cannot
  produce a number without being told the factor.
- The AME computation has six sub-paragraphs of its own, several of them
  Commissioner discretions, and is not encoded.
- The Fourth Schedule, which fixes the percentage for listed injuries, is not
  encoded.
- Part 3A applies a parallel scheme to platform workers and is not encoded.
- No case law was searched.
