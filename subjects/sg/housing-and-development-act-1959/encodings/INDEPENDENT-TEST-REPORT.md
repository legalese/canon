# Independent test report: Housing and Development Act 1959

The expectations in `independent-expectations.md` (E01-E163) were written from `../source/HDA1959.txt` and `BRIEF.md` before any `.l4` file was opened. `tests-independent.l4` asserts them against `hda-types`, `hda-flats`, `hda-upgrading-board` and `hda-goal`. No expected value was changed after the encoding was read. No `hda-*.l4` file was edited.

## Counts

| | |
|---|---|
| Assertions in `tests-independent.l4` | 164 |
| Passing | 162 |
| Failing | 2 |
| Refusing (`#ASSERT REFUSED`) | 0. None were written: no expectation called for a refusal, and the encoding contains no `REFUSE`. |
| Other errors or warnings | none |

`check.sh` (L4=~/.local/bin/l4) output: `tests-independent.l4  errors 2  satisfied 162  failed 2`. The 2 errors are the 2 failed assertions. `hda-tests.l4` passes 102 of 102. `l4 run tests-independent.l4 | grep -i warning` prints nothing.

## Disagreements

### 1. E60, s 62(1)(c): a remediable breach still unremedied 14 days after notice

- **Expected:** the Board may re-enter when the condition "is not performed or observed within 2 weeks after a written notice", and I took day 14 as enough.
- **Encoding:** `days since notice ... GREATER THAN 14`, so re-entry is possible only from day 15. Day 14 gives FALSE.
- **My view:** the encoding is probably right. If the day of the notice is excluded, the 2 weeks run to the end of day 14, so the owner is in default only from day 15. My expectation looks off by one. The input name "days since notice" does not say how the days are counted, so a `NOTES.md` line would help.

### 2. E91, s 50(3A): the earliest day the Board may vest or terminate after a notice served on 1 Mar 2026

- **Expected:** 15 Mar 2026.
- **Encoding:** 16 Mar 2026 (`served PLUS 14 PLUS 1`).
- **My view:** the encoding is right. The Board "must not proceed ... until the expiry of a period of 14 days after the service". Excluding the day of service, that period ends at the close of 15 Mar, so the Board may act on 16 Mar. My own E92 sets the purchaser's appeal deadline (s 50(4)) at 15 Mar, which agrees with the encoding: the Board cannot act on the last day an appeal may still be lodged. The error is in my expectation.

All other 162 expectations that could be expressed agree with the encoding. That includes:
- the 30-month window in s 50(1)(b), with the exact-edge reading E07 (a disposal exactly 30 months before is barred), the day before applying, and disposals between application and completion;
- the $250,000 limit in s 63(2), the 3-month limit in (k) and the "above 14" age in (m);
- the 75% thresholds in s 77 and the rules for mixed buildings in s 77(5)-(7);
- the s 107 penalty with no "or both";
- composition under s 32 as the lower of half the fine and $5,000;
- the 7-day statutory declaration and the single-offence rule in s 33(3)(a) and (5);
- the 2-day registered-post rule and the email exclusions in s 111;
- the quorum arithmetic in s 9(1), including 5 of 13;
- the budget date in s 98.

## Expectations that cannot be expressed against the encoding

| Expectation | Why it cannot be tested |
|---|---|
| E14, s 57 (a body corporate with no order) | `Purchase facts` has no input saying the buyer is a body corporate. |
| E19 / E20 / E21, s 50(12)(b) | The cancellation ground is an enum. The "above the age of 14 years" condition and the list of Penal Code sections (304A, 336, 337, 338) are not modelled. E19 is asserted only as "ground (b) made out". |
| E27, s 55(1) after the minimum occupation period ends | The dealing enum has only "within the minimum occupation period". |
| E29 / E30, s 55(3) on 20 Nov 1998 | The date is a boolean input ("made on or after 20 November 1998"), so the edge day itself is not computed. |
| E31, s 55(2) where the purchaser is the Board | No input for this. |
| E56, s 59(4) rescission of an unregistered agreement for a lease | Not encoded. |
| E78, s 63(1)(m) conviction before 1 Mar 1984 | No conviction date is modelled. |
| E83, s 63(1)(o) conviction before the appointed date | No conviction date is modelled. |
| E89, s 74(1)(i) where the Board does proceed under s 50 | The penalty function takes only the breach date. |
| E119, s 84(8) compulsory acquisition for upgrading after approval under s 77(4)/(5) | Not encoded. |
| E140, s 32 for an offence with a $10,000 maximum fine | Composition is computed only for the enumerated offences, and none has a $10,000 fine. |
| E152, s 33(2) no second penalty once one has been imposed | Not encoded. |
| E163, s 84(3) conditions for a warrant | Not encoded. |
| E42 and E44, s 58(8) mixed citizenship and unsecured creditors | These collapse into the boolean inputs "all owners non-citizens" and "consented mortgagee". They are asserted only at that level. |
| E123, s 7(1)(b) pardoned or foreign convictions | These must be entered by hand as 0 unpardoned Singapore months. |

## What the encoding misses or simplifies

1. **s 59(3)(a) once representation exists.** If representation exists, the encoding checks only limbs (b) and (c). Suppose representation is taken out late, say 14 months after death. Limb (a), "no representation ... within 12 months from the death", is still satisfied, and the Board may vest. The encoding says it may not, unless (b) or (c) also applies. This is outside my fixed expectations, so it is not asserted.
2. **s 50(1)(b) records only one disposal.** The encoding keeps only the date of the last disposal. Take an earlier disposal inside the 30-month window followed by a later one after completion. The encoding sees only the later one and wrongly finds the buyer entitled.
3. **s 58(6) and (7) are merged.** One boolean covers both. The consented-mortgagee and chargee exception belongs only to attachment under (7). It should not remove protection from vesting in the Official Assignee under (6). The top-level goal also fixes the mortgagee input at FALSE.
4. **The top-level financial penalty is a constant.** The goal's "most financial penalty instead" is always 50000. It ignores the 20 July 2015 start date and whether the Board has proceeded under s 50, 62 or 63. `the most financial penalty instead of ss 50, 62 or 63` likewise ignores the "does not proceed" condition.
5. **s 63(1)(m) and (o) are simplified.**
   - In (m), the age test is applied to whoever was convicted. The Act attaches "above the age of 14 years" to the authorised occupier, and arguably not to the owner or spouse.
   - The 1 Mar 1984 date in (m) is missing.
   - In (o), the "appointed date" is missing, and so is the condition that the occupier is a related person or above 18.
   - Where the Act does not supply a fact, such as the appointed date, the brief would call for a `REFUSE`. The encoding contains no `REFUSE` anywhere.
6. **s 50(12)** grounds are an enum, so the ages and offence lists in (b) and (d) are not checked.
7. **s 111 service.**
   - Whether a document is excluded is an input. The encoding does not derive it from which section the document is under.
   - The exclusions in s 111(9), such as the s 15(1) and s 69(1) notices, are not modelled.
   - Email service takes effect on the day sent. Under (8)(b) it takes effect when the email becomes retrievable.
8. **s 33** merges limbs (3)(b) and (c) (the Board or the court is satisfied) and omits s 33(2).
9. **Not modelled at all:** the warrant provisions in ss 28(4)-(9), 29(3)-(5) and 84(2)-(6); the compulsory acquisition in s 84(8)-(13); and s 59(4).
10. **Periods are bare day counts.** Interpretive choices such as "within 2 weeks" are left to how the caller counts "days since notice".

## Triage by the encoder (2026-10-09)

- **E60 and E91:** the encoding is kept (NOTES.md, forks F2 and F3). These are expected failures, and their expected values are unchanged.
- **Fixed in the encoding:**
  - s 50(1)(b): every disposal;
  - s 58(6)/(7): split;
  - s 59(3)(a): late representation;
  - s 63(1)(m): the age test applies only to an occupier, with the 1984 date;
  - s 63(1)(o): the related-person-or-above-18 condition and the appointed date;
  - the top-level s 74 penalty now follows the breach date.

  This file's tests were changed only in plumbing: the constructors take the new arguments, each set so the expected value is unchanged. See NOTES.md §4.
