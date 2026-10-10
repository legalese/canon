# Stamp Duties Act 1929 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2021 Revised Edition, informal consolidation (version in force from 1 October 2025), with amendments to 2025
shown (including the 4 July 2025 change to seller's duty).

**Checks:** one case file, 46 assertions satisfied (35 at first encoding; 11 added on 11 Oct 2026 for REQ-0008), 0 errors, 0 warnings.

## Why this Act, and why scoped

**13 of the 527 Singapore Acts** deposited here cite it. This row takes First Schedule
Article 3:
- buyer's stamp duty
- additional buyer's stamp duty (ABSD) on residential property
- seller's stamp duty
- duty on share transfers
- and, added for REQ-0008, Article 8 duty on leases and who pays it (Third Schedule)

The charging and procedural sections, mortgages, settlements, the
property-holding-entity rules, ABSD remission and the two-property elections are not
encoded.

**Warning about the source.** The First Schedule tables are **column-shifted** in the
`.txt` deposit. The percentages appear in a block beside the wrong bands. They were
matched to bands by order of appearance:
- residential: 1, 2, 3, 4, 5, 6%
- non-residential: 1, 2, 3, 4, 5%

The resulting duties agree with the standard worked figures (residential $1m →
$24,600). Anyone re-encoding from the `.txt` should check against the PDF.

## What the Act turns out to say

### 1. Buyer's stamp duty has a 6% top band for homes and stops at 5% for everything else

Para (a)(iv), from 15 February 2023: residential bands are 1/2/3/4/5/6% across
$180k / $180k / $640k / $500k / $1.5m / above $3m. Non-residential stops at 5% above
$1.5m. On $1m, both come to $24,600. On $4m, residential is $179,600 and
non-residential $169,600. Asserted.

### 2. ABSD: the highest-rate buyer governs a joint purchase

Para (bi), from 27 April 2023:

| Buyer | ABSD |
|---|---|
| Citizen buying a first property | 0% (no paragraph applies) |
| Citizen owning one | 20% |
| Citizen owning two or more | 30% |
| PR owning none | 5% |
| PR owning one | 30% |
| PR owning two or more | 35% |
| Housing developer | 40% |
| Foreigner | 60% |
| Entity or trustee | 65% |

Each paragraph applies only where "none of the other" joint buyers falls in a
higher-rate profile. A first-time citizen buying with a foreigner therefore pays 60%
on the whole price. Asserted.

### 3. Seller's stamp duty was raised and lengthened for purchases from 4 July 2025

Para (bj): 16/12/8/4% for sales within 1/2/3/4 years. Under para (bg), for purchases
between 11 March 2017 and 3 July 2025, it is 12/8/4% within 3 years. Asserted.

### 4. Smaller things worth recording

- **Head-note:** duty is rounded down to the dollar, with a $1 minimum. Rounding is not
  modelled, so the cases use prices that give whole dollars.
- **Para (c):** 0.2% on share transfers.

### 5. Leases: 0.4% of the rent, paid by the tenant (added for REQ-0008)

Article 8(aa), for leases without a premium executed on or after 22 February 2014:
- For a lease of up to 4 years, the duty is 0.4% of the total rent for the term.
- For a longer or indefinite lease, it is 0.4% × 4 × the average annual rent.

Exempt are leases whose average annual rent is $1,000 or less, and direct HDB public
rentals. Duty is rounded down to the dollar, with a $1 minimum. The Third Schedule makes
**the lessee** liable. REQ-0008's two-year tenancy at $2,400 a month comes to $57,600 in
rent; 0.4% is $230.40, so the duty is **$230**, paid by the couple as lessees. Asserted.

The Article 8 table is column-shifted in the `.txt` deposit, like Article 3's; the
formulas were read from their cells.

## What would need doing before this is worth anything

- Check the encoded rates against the PDF First Schedule (see the warning above).
- ABSD remission for married couples and the two-property elections are not modelled.
  Remission is often decisive in practice.
- No IRAS guidance or case law was retrieved.
