# Work Injury Compensation Act 2019 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation in force from
1 December 2025 — so it carries the S 694/2025 uplift to the compensation
figures, in force 1 November 2025.

**Checks:** `l4 run wica-cases.l4` and `l4 run wica-liability-cases.l4` —
102 assertions satisfied, 0 errors, 0 warnings.

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


---

# Added with the table recovery and sections 8 to 16, 24 and 34B

## The deposit defect was not a one-off, and the second instance changes the law

The first pass recorded that Tables A and B could not be read from
`WICA2019.txt`. Both are now **recovered from the PDF with pypdf** and encoded;
the deposited extract shifts the factors one row against the ages at every page
break, so row 32 of Table A appeared blank and every later row on that page
carried its neighbour's figure.

Then the **same defect turned up again**, in the s 34B substitution table that
decides which provisions apply to a **platform worker**:

| | deposited `WICA2019.txt` | the PDF |
|---|---|---|
| s 7 | *(no entry)* | **34D** |
| s 8 | 34D | **34F** |
| s 10 | 34F | **34G** |
| s 11 | 34G | **34H** |

Anyone reading the deposited text would conclude that s 8 (the deeming rules) is
replaced by s 34D for platform workers. It is not: s 34D replaces **s 7**, the
liability section, and s 8 is replaced by s 34F. The mapping encoded here is
from the PDF, and every row is asserted.

So this is a **systemic extraction defect**, not a one-off: any table in this
deposit that crosses a page break should be treated as unreliable until checked
against the PDF. That is now a method note, not a single finding.

## Five observations on the sections added

**1. The public bus is excluded, however the employer arranged it.** s 8(1)
deems a commuting accident to be in the course of employment only if the
transport is operated by or for the employer **and** "is **not** operated in the
ordinary course of a public transport service". An employer who buys season
tickets rather than running a shuttle leaves its staff outside the deeming rule.

**2. Disobedience does not defeat a claim; being off the employer's business
does.** s 8(3) preserves the claim even where the employee broke the law, the
regulations or the employer's own orders, provided the act "was done for the
purposes of and in connection with the employer's trade or business". That last
limb, not the disobedience, is what decides it.

**3. s 10(1)(c) is much narrower than it reads.** The open-ended limb for
unscheduled diseases requires the disease to be "directly attributable to an
exposure to a **chemical or biological agent**". A disease caused by noise,
vibration, radiation or repetitive strain is outside it, however clearly the
work caused it, unless the Second Schedule happens to list it.

**4. The principal owes nothing until the Commissioner says so.** Under s 13 the
Commissioner **may direct** a principal to fulfil the employer's obligations.
Every condition can be satisfied and no liability arises until that direction is
made. Compare s 65 of the Motor Vehicles (Third-Party Risks and Compensation)
Act 1960, where the principal and contractor are jointly and severally liable
**by operation of law**, with no official decision in the way. Two Acts, the
same commercial situation, opposite defaults.

**5. Medical treatment has two ceilings and the temporal one bites hardest.**
First Schedule paragraph 5 pays the **lower** of the cost incurred "within a
period of one year after the date of the accident" and $53,000 ($45,000 before
1 November 2025). An employee who spends $2,000 inside the year and $40,000
after it recovers **$2,000** — nowhere near the money cap. Asserted directly.

## What would still need doing

- Part 4, the claims procedure, with its own time limits.
- The AME computation in the First Schedule, six sub-paragraphs with several
  Commissioner discretions.
- The Second Schedule of occupational diseases and their limitation periods, and
  the Fourth Schedule of loss-of-earning-capacity percentages. **Both are tables
  that cross page breaks** and must be recovered from the PDF, not read from the
  deposited text.
- ss 34D to 34N individually.
- No case law was searched, and no human gate has been sought.
