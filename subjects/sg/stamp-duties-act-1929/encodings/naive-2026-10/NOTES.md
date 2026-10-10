# Stamp Duties Act 1929 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2021 Revised Edition, informal consolidation (version in force from 1 October 2025), with amendments to 2025
shown (including the 4 July 2025 change to seller's duty).

**Checks:** two case files, 73 assertions satisfied (35 at first encoding; 11 added on 11 Oct 2026 for REQ-0008; 27 for REQ-0009 in `sda-absd-spouses-cases.l4`), 0 errors, 0 warnings.

## Why this Act, and why scoped

**13 of the 527 Singapore Acts** deposited here cite it. This row takes First Schedule
Article 3:
- buyer's stamp duty
- additional buyer's stamp duty (ABSD) on residential property
- seller's stamp duty
- duty on share transfers
- and, added for REQ-0008, Article 8 duty on leases and who pays it (Third Schedule)
- and, added for REQ-0009, the **Stamp Duties (Spouses) (Remission of ABSD) Rules 2013** (S 217/2013), in their own module `sda-absd-spouses.l4`

The charging and procedural sections, mortgages, settlements, the
property-holding-entity rules, ABSD remission other than for spouses, and the two-property elections are not
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

### 6. ABSD remission for spouses: two routes, and the six months is a refund deadline (added for REQ-0009)

Source: the Rules as current on 10 October 2026, saved by hand from SSO and deposited at
`../../registers/source-bundle/SDA1929-S217-2013.txt`. They are subsidiary legislation, so they sit in this row
beside the Act instead of in a row of their own (one encoder slug per subject).

- **Rule 3, remission at the outset.** It applies where a married couple, exactly two joint buyers, are a citizen
  owning no property and a PR or foreigner owning none. ABSD (5% or 60% under Article 3(bi)) is remitted in full.
- **Rule 4, remission by refund.** It applies where one or both own one property and at least one is a citizen
  (rule 4(2)(a)–(c)). A PR with a foreigner never qualifies. Owning two never qualifies. Every condition in rule 4(3)
  must hold:
  - ABSD is paid first.
  - The old property (or both, if each owned one) is disposed of within **6 months** of execution.
  - For a property with no TOP or CSC at execution, the 6 months run from the earlier of TOP and CSC.
  - Nothing else is bought in between.
  - On the disposal date the couple own the new home together, with no one else, and are still married.
  - The refund is claimed within 6 months of the disposal. The Commissioner may allow longer.
- **Rule 4(3A)** gives 12 months where execution was on or before 1 June 2020 and the 6-month deadline fell on or
  after 1 February 2020. These are the COVID cases.

REQ-0009's couple are two citizens jointly owning their first flat; each is "a Singapore citizen owning one
property" under rule 4(2)(c). They buy a completed EC on 28 April 2040, paying 20% ABSD, so the deadline for selling
the flat is **28 October 2040**. Selling on that day gets the remission; selling on 29 October does not. Asserted.

**The encoder's reading:** "within 6 months after" a date means on or before the same day six months later. Where
that month is shorter, it means the month's last day. The Rules do not say this. Who counts as owning a property
(rule 2(5)–(6)) is an input, not computed.

## What would need doing before this is worth anything

- Check the encoded rates against the PDF First Schedule (see the warning above).
- ABSD remission other than for spouses (for example, for developers) and the two-property elections are not modelled.
- No IRAS guidance or case law was retrieved.
