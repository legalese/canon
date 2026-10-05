# Independent expectations — Apportionment Act 1928 (2020 RevEd)

Written from `BRIEF.md` and `../source/AA1928.txt` only, before any `.l4`, `NOTES.md` or
`encoding.json` was opened. Each answer cites the provision it comes from.

## Readings taken where the text is silent or ambiguous

- **R1 Day counting (s 3, s 2 "dividends").** The Act says only "accruing from day to day" and,
  for dividends, "equal daily increment during and within the period". It does not say whether
  the start day and the day of determination are both counted. My expected reading: the accrued
  part is `entire portion × (days accrued ÷ days in the period)`, i.e. linear in days. Tests are
  written so that the number of days is an input or so that the day-count convention is the only
  thing in doubt; where a date-based test depends on the convention, I say which convention I
  assumed (period start counted, determination date not counted: days = determination − start;
  period length = end − start, where `end` is the date the entire portion falls due).
  Genuinely ambiguous.
- **R2 "Payments in the nature of income" (s 3).** A lump sum or a payment of capital is not
  apportionable. A return or reimbursement of capital is expressly not a "dividend" (s 2).
- **R3 s 4 "and not before".** The apportioned part is payable on the due date itself and any day
  after, not on any day before.
- **R4 s 6 and s 7 override s 3.** An annual sum payable under a policy of assurance of any
  description is never apportionable; a case where it is expressly stipulated that no
  apportionment shall take place is outside the Act.
- **R5 s 5(2) applies only to rent reserved out of or charged on lands or tenements.** For such
  rent the tenant / land cannot be resorted to for the apportioned part specifically; the entire
  rent is received by the person who would have been entitled to the entire rent, and the
  executors (or other parties entitled) recover the apportioned part from that person by suit.
  For any other payment (annuity, dividend) s 5(1) gives the same remedies as for the entire
  portion.

## Scenarios

### s 2 / s 3 — what is apportionable

| # | scenario | expected | provision |
|---|---|---|---|
| A1 | rent (written lease) | apportionable | s 3; s 2 "rents" |
| A2 | rent reserved orally (not in writing) | apportionable ("or otherwise") | s 3 |
| A3 | periodical payment in lieu of / in the nature of rent | apportionable | s 2 "rents" |
| A4 | annuity | apportionable | s 3 |
| A5 | salary | apportionable (annuity includes salaries) | s 2, s 3 |
| A6 | pension | apportionable | s 2, s 3 |
| A7 | dividend strictly so called | apportionable | s 2, s 3 |
| A8 | bonus paid out of revenue of a trading/public company, divisible among members | apportionable (a dividend) | s 2 |
| A9 | dividend not paid at fixed times | apportionable ("whether ... at any fixed times or otherwise") | s 2 |
| A10 | payment in the nature of a return / reimbursement of capital | NOT a dividend; NOT apportionable | s 2, s 3 |
| A11 | other periodical payment in the nature of income (e.g. interest-like royalty) | apportionable | s 3 |
| A12 | a one-off, non-periodical payment | NOT apportionable | s 3 (R2) |
| A13 | annual sum payable under a policy of assurance (any description) | NOT apportionable | s 6 |
| A14 | rent with express stipulation that no apportionment shall take place | NOT apportionable (Act does not extend) | s 7 |
| A15 | rent with stipulation that does not exclude apportionment | apportionable | s 7 converse |

### s 3 / s 2 — arithmetic (R1, linear)

| # | scenario | expected | provision |
|---|---|---|---|
| B1 | annual rent 36,500, period 365 days, 100 days accrued | 10,000 | s 3 |
| B2 | quarterly rent 900, period 90 days, 30 days accrued | 300 | s 3 |
| B3 | 0 days accrued | 0 | s 3 |
| B4 | all days of the period accrued (365/365) | the whole 36,500 | s 3 |
| B5 | dividend 3,650 declared for a 365-day period, 100 days within | 1,000 (equal daily increment) | s 2 |
| B6 | monthly salary 3,100 for a 31-day month, 15 days accrued | 1,500 | s 2, s 3 |
| B7 | leap year: annual 36,600 over a 366-day period, 183 days | 18,300 | s 3 (R1) |
| B8 | date-based: period 1 Jan 2025 → 1 Jan 2026 (365 days), determination 11 Apr 2025 (100 days after start), annual 36,500 | 10,000 (convention R1) | s 3 |
| B9 | policy-of-assurance annual sum, any day count | not apportionable → no apportioned part (encoding should refuse or yield nothing, not compute) | s 6 |

### s 4 — when payable

| # | scenario | expected | provision |
|---|---|---|---|
| C1 | continuing rent, entire portion due 30 Jun 2025, asking 29 Jun 2025 | NOT yet payable | s 4(a) "and not before" |
| C2 | continuing rent, asking 30 Jun 2025 (due date) | payable | s 4(a) |
| C3 | continuing rent, asking 1 Jul 2025 | payable | s 4(a) |
| C4 | rent determined by death, next entire portion would have been payable 30 Jun 2025, asking 29 Jun | NOT payable | s 4(b) |
| C5 | same, asking 30 Jun 2025 | payable | s 4(b) |
| C6 | determined by re-entry, same dates | same as C4/C5 | s 4(b) |
| C7 | determined "otherwise" (e.g. sale / surrender) | same as C4/C5 | s 4(b) "or otherwise" |
| C8 | the payable date under s 4(a) is the date the entire portion becomes due; under s 4(b) the date the next entire portion would have been payable | identity | s 4 |

### s 5 — who may recover and how

| # | scenario | expected | provision |
|---|---|---|---|
| D1 | the person entitled themselves | has remedies (same as for entire portion) | s 5(1) |
| D2 | executor / administrator / assign of a person | has remedies | s 5(1) |
| D3 | executor of a person whose interest determines with own death (e.g. life tenant) | has remedies | s 5(1) |
| D4 | rent charged on land: may the apportioned part be sought from the tenant / the land specifically? | NO | s 5(2) |
| D5 | rent charged on land: who receives the entire rent? | the person who would have been entitled to the entire rent had it not been apportionable | s 5(2) |
| D6 | rent charged on land: how do the executors get the apportioned part? | from that person, by suit | s 5(2) |
| D7 | annuity (not land rent): may the apportioned part be sought from the payer? | yes, same remedies as for the entire portion when payable (s 5(2) does not apply) | s 5(1) (R5) |
| D8 | remedies are only "when payable": asking before the s 4 date | no remedy yet | s 5(1) + s 4 |

### s 1 — inert. s 6, s 7 — see A13, A14.
