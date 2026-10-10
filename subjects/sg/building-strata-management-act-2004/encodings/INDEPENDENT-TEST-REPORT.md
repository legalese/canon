# Independent test report: BSMA 2004 encoding

The expected values come from `independent-expectations.md` (E01-E203). They were written from `../source/BSMA2004.txt` before any `.l4` file was read, and none was changed after the encoding was read. The assertions are in `tests-independent.l4`, and each carries its E-number.

## Counts

Run with `L4=~/.local/bin/l4 ./check.sh` and `l4 run tests-independent.l4`:

| | |
|---|---|
| Assertions in `tests-independent.l4` | 288 |
| Satisfied | 286 |
| **Failed** | **2** (E132, E137) |
| Refused | 0 (no `#ASSERT REFUSED` was applicable; see the gaps below) |
| Other errors or warnings | 0 |

None of the `bsma-*.l4` modules has any errors. `bsma-tests.l4` has 249 assertions satisfied and none failed.

Expectations covered by at least one assertion: 186 of 203. Inexpressible: 17 (listed below).

## Disagreements

### E132: when interest starts (s 40(6)(b))

- **The facts:** the contribution was due on 1 Mar 2026 and paid on 1 Apr 2026.
- **My expectation:** interest accrues from **31 Mar 2026**.
- **The encoding:** interest accrues from **1 Apr 2026** (`due on PLUS 31`).

**My view: the encoding is right and my expectation is off by one day.**

Section 40(6)(b) says interest accrues "from the expiry of 30 days after the date when the contribution becomes due". The same paragraph lets the proprietor pay "on or before the 30th day" (31 Mar) without interest. So the 30-day period runs to the end of 31 Mar, which agrees with Interpretation Act s 50(a): a period "after" a day excludes that day. Interest therefore runs from 1 Apr. Accruing interest on 31 Mar would contradict the interest-free window that ends that same day.

### E137: when a charge may be lodged (s 43(1))

- **The facts:** the demand was served on 1 Mar 2026 and the amount is unpaid.
- **My expectation:** a charge may be lodged from **31 Mar 2026**.
- **The encoding:** a charge may be lodged only after 31 Mar, i.e. from **1 Apr 2026** (`as at > d PLUS 30`). The negative test (not on 30 Mar) agrees with both readings.

**My view: the encoding is right, for the same reason as E132.** The amount must remain unpaid "on the expiry of a period of 30 days after" service. That period ends at the end of 31 Mar.

Both failures are therefore errors in my expectations, not defects in the encoding. They are left failing in the test file, because the rules say expected values are never edited.

## Inexpressible expectations

| E | Why |
|---|---|
| E26 | There is no date function for the end of the 12-week period in ss 2(6)-(7). The encoding takes `weeks since the meeting` as an input instead. |
| E38 | The written consent of the proprietor to an exclusive use by-law (s 33(1) opening words) is not modelled. |
| E49 (part) | There is no Matter for an appearance improvement, so "which resolution?" cannot be put. I expected REFUSE. The s 37(4)(a)-(b) limbs *are* asserted, and pass. |
| E83 | The para 2(3) rule that the joint proprietor named first on the roll prevails is not modelled. |
| E84 | The s 65(10) notice naming a company's representative is not modelled. |
| E91 | A proxy instrument is void if the appointer is present (para 17(4)). Not modelled. |
| E95 | Council elections: one vote per lot, and no poll (para 8(4)-(5)). Not modelled. |
| E102 | Uncontested candidates are declared elected (para 8(3)). Not modelled. |
| E155 (part) | A council of 15 is not rejected: the encoding clamps 15 seats to 14. I asserted only that the result is not 15, which passes. |
| E170 | No function for a council majority decision (Second Sch para 2(3)). |
| E171 | No function for the 3 days' notice of a council meeting (Second Sch para 4(1)). |
| E177 | No function for the managing agent's term under s 66(2). |
| E202 | "Reasonable time" in s 31(1)(f) is a boolean input, so there is nothing to refuse. This is acceptable. |
| E203 | The minimum cover prescribed under s 71(2) is not modelled. |

Two further expectations are asserted only partially, through a nearby function:

- **E78:** there is no function for the notice of a resumed meeting under para 3A(3). It is asserted through the general 14-day notice rule in para 1A(1), with 13 days' notice failing.
- **E90:** the void 3rd proxy instrument is shown only as "the limit for 100 lots is less than 3".

## What the encoding misses or simplifies

1. **Valid votes are filtered by the caller.** Section 2(8) excludes votes that are both for and against, unmarked, void, or cast by someone not entitled to vote. The `Motion` record expects the caller to remove these before filling it in. E10, E11, E17 and E27 therefore test only that arithmetic, not the s 2(8) exclusions themselves. Separately, `the proprietor's vote counts` covers entitlement to vote.
2. **The exclusive use term is a single number.** Section 33(1)(b) depends on whether the term *with renewal options* can exceed an aggregate of 3 years (E37). The caller must pass that aggregate. A 2-year term with a 2-year option, entered as 2, would wrongly get a special resolution.
3. **The council size cap is silent.** Asking for 15 seats returns 14, where s 53(1) makes 15 impermissible. Returning a REFUSE or a validity flag would be more faithful.
4. **The 12-week clock is an input.** There is no date computation for the end of the period in ss 2(6)-(7), and there is no AGM-to-AGM managing agent term (s 66(2)).
5. **Several First and Second Schedule meeting mechanics are not modelled.** These are paras 2(3), 8(3)-(5), 17(4), 3A(3), and Second Sch paras 2(3) and 4(1). Nor is s 65(10) (see the inexpressible table).
6. **The encoding has only two REFUSEs, both in the developer module (s 16(1)).** Every other gap is either an input or absent. In particular, E49 (no resolution named for an appearance improvement) has no Matter at all, rather than a REFUSE.
7. **Points of reading where the encoding agrees with me:**
   - E80: a proprietor in arrears may still vote on a unanimous or consensus resolution. This follows the para 1A(2)(e)(ii) carve-out over para 2(1).
   - E134: under s 40(10), payment on the 14th day after the demand is late (fork F3).
   - E46: an EV charger lease of 11 years needs a 90% resolution.
   - E147: the Commissioner cannot authorise alterations to common property during the initial period.

## Triage by the encoder (2026-10-10)

- **E132 and E137:** the encoding is kept (NOTES.md, fork F4). These are expected failures, and their expected values are unchanged.
- **Fixed in the encoding:** the term inputs for exclusive-use by-laws and leases now include every renewal option (ss 33(1)(b), 34(2)). The input was renamed; the values are unchanged, and no test was edited.
- **The other simplifications are kept and listed in NOTES.md §4.**
