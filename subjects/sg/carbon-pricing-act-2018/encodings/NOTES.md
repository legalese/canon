# Carbon Pricing Act 2018 — notes for a reviewer

## 1. What is encoded

**The whole Act**, ss 1-79, and all five Schedules, as printed in SSO's PDF "Current version as at 06 Oct 2026" (`../source/CPA2018.txt`): the 2020 Revised Edition with the Carbon Pricing (Amendment) Act 2022 (Act 37 of 2022, in force 1 January 2024) and later orders.

The law is stated for **emissions years and events from 2024**. Act 37 of 2022 rewrote registration, reporting periods, payment and the credits regime, and the earlier text was not supplied, so every rule that takes a year or a date refuses for one before 2024 (fork F1). The Third Schedule prints the carbon tax rate and the carbon price for every year, and those tables answer for any year.

Provisions that confer a power, describe a procedure or define a word the caller applies are **inert**, listed in `provisions carried as text` (`cpa-process-offences.l4`) and in the coverage table. Discretions of the Agency, the Minister or a court are inputs. Regulations are not in the source: prescribed industry sectors (s 5(1)), the ICC criteria and limit (ss 33A, 33B), record-keeping periods (s 40), compoundable offences (s 71) and the end date of Division 1A (s 20B) are inputs.

## 2. The goals

**Top-level goal** (`cpa-goal.l4`): *for this business facility and this emissions year, what does the Act require of the person in operational control, and what does it owe?* — `the carbon pricing position for` a `Facility year`: whether the Act applies, the reckonable emissions, the registration applications due, the reporting duties, the carbon tax, the credits to surrender, the last day to pay and the late-payment penalty.

Under it, seven goals, each of which can be asked on its own:

| # | Goal — the question one can ask | Main conclusions | Module |
|---|---|---|---|
| 1 | **Must this person register this facility, or may it deregister?** (ss 3-10, 79) | `the applications required for the year` …; `the applications Y must make on the transfer` …; `the registered person may apply to deregister the facility` …; `the person with operational control among` …; `carried out at a single site:` … | `cpa-registration-reporting.l4` |
| 2 | **What must it report, verified or not, and by when?** (ss 11-15; First and Second Schedules) | `the reporting duties, controlled:` …; `the reporting period in` …; `the last day to notify an error discovered on` …; `the reckonable tCO2e of` …; `a non-reckonable GHG emission:` … | `cpa-registration-reporting.l4`, `cpa-schedules.l4` |
| 3 | **How much carbon tax is charged for the emissions year?** (ss 16, 20A-20E; Third Schedule Part 1) | `the carbon tax charged for` …; `eligible for allowances, exporting:` … | `cpa-tax-payment.l4` |
| 4 | **How, and by when, is the tax paid, and what is owed if it is late?** (ss 17-20, 24, 26-33D; Third Schedule Part 2) | `the last day to pay the tax for` …; `the fixed-price carbon credits to surrender for tax of` …; `the eligible ICCs that count, of` …; `the late payment penalty on` …; `the credits after conversion, of` …; `the refund of` …; `the Agency may close the account on ground` … | `cpa-tax-payment.l4` |
| 5 | **Can an assessment be made, revised, objected to or appealed, and by when?** (ss 21-25, 34-39) | `the Agency may make a best-judgment assessment on` …; `an objection on` … `is valid` …; `an appeal to the Minister lies against` …; `the change of` … `is large enough for a High Court appeal` | `cpa-process-offences.l4`, `cpa-tax-payment.l4` |
| 6 | **What records and register updates are owed, and when is a document served?** (ss 40-44, 67, 75) | `the last day to notify a change made on` …; `the day service takes effect, sent` …; `an extension may still be granted after expiry` … | `cpa-process-offences.l4` |
| 7 | **Is an offence committed, and what is the most it can cost?** (ss 5(3), 47-62, 68-71, 76(4)) | `the maximum penalty for` …; `the penalty for an inaccurate verified report, culpability` …; `the composition limit for a maximum fine of` …; `the officer is guilty of the same offence:` … | `cpa-process-offences.l4` |

## 3. Modules

| module | what it holds |
|---|---|
| `cpa-types.l4` | nouns: emissions and circumstances, sites and control, registration status, transfers, deregistration facts, assessments, surrenders, decisions, offences |
| `cpa-schedules.l4` | the First Schedule (63 gases, generated from the text), thresholds, non-reckonable and excluded emissions, the tax rate and carbon price tables |
| `cpa-registration-reporting.l4` | Goals 1 and 2, the vintage gate, s 79 |
| `cpa-tax-payment.l4` | Goals 3 and 4, s 37(2) |
| `cpa-process-offences.l4` | Goals 5 to 7, and the provisions carried as text |
| `cpa-goal.l4` | the top-level goal |
| `cpa-tests.l4` | the encoder's tests |
| `tests-independent.l4` | the independent test author's (section 8) |

## 4. Coverage

| provision | disposition |
|---|---|
| Long title, s 1 | inert |
| s 2 | encoded where a definition decides something (carbon dioxide equivalence, excluded, non-reckonable and reckonable emissions, greenhouse gas); the rest applied by the caller |
| s 3 | encoded: (1), (3); (2), (4), (5) inert (a finding) |
| s 4 | encoded: (1)-(3); tie at the greatest authority refuses |
| s 5 | encoded: (1) (prescribed sector an input), (3); (2), (4) inert |
| s 6 | inert |
| s 7 | encoded: (1)-(6); (7) inert |
| s 8 | encoded: (1)(a), (4); (1)(b)-(d), (2), (3) inert |
| s 9 | encoded: (1)-(5) |
| s 10 | encoded: (4); (1)-(3) inert |
| s 11 | encoded: (1), (2), (2A), (3); (2B)-(2D) inert (the caller sets the period) |
| s 12 | encoded: (1), (3)(a); (2), (3)(b) inert |
| s 13 | encoded: (1), (2); (3)-(6) inert |
| s 14 | inert (a direction; failure is s 58) |
| s 15 | encoded: (1) (7 working days, fork F3); (2)-(3) inert |
| s 16 | encoded: (1)-(3); (4) inert |
| s 17 | encoded: (1)-(4); (5) inert |
| s 18 | input (relief or remission is a discretion) |
| s 19 | encoded: (1)-(4); (5) inert |
| s 20 | encoded: (1); (2)-(3) inert |
| ss 20A-20G | encoded: 20B, 20C, 20D(1), 20E(2)(b)(i), 20E(5); the rest inert (the Minister's award and methodology are inputs) |
| s 21 | encoded: (2); (1), (3)-(5) inert |
| s 22 | encoded: (1); (2)-(3) inert |
| s 23 | encoded: (1A), (2)-(4); (1), (5)-(7) inert |
| s 24 | encoded |
| s 25 | encoded |
| s 26 | encoded: (1) via Third Schedule; (2) inert |
| s 27 | inert |
| s 28 | encoded: (2) |
| s 29 | encoded: (1), (3); (2), (4) inert |
| s 30 | inert (no refund except under s 33) |
| s 31 | inert |
| s 31A | encoded (formula transcribed) |
| s 32 | encoded: (1), (3); (2) via s 17(2) |
| s 33 | encoded: (1)-(7) |
| s 33A | input (prescribed criteria, the Agency's acceptance) |
| s 33B | encoded |
| s 33C | encoded |
| s 33D | inert |
| s 34 | encoded: (1), (2); (3)-(5) inert |
| s 35 | encoded |
| s 36 | inert |
| s 37 | encoded: (1), (2); (3)-(5) inert |
| s 38 | encoded: (1); (2)-(4) inert |
| s 39 | inert |
| s 40 | inert (failure is s 62(1)) |
| ss 41-43 | inert |
| s 44 | encoded: (2)(c); rest inert |
| s 45 | inert (definitions) |
| ss 46-50 | inert (powers); offences in ss 47(2), 48(3), 49(4) encoded |
| s 51 | encoded: offence (2); (1) inert |
| ss 52-62 | encoded (offences and penalties) |
| ss 63, 64 | inert |
| s 65 | encoded: (1), (4); (2)-(3) inert |
| s 66, Fourth Schedule | inert |
| s 67 | encoded: (5), (6); (1)-(4), (7)-(8) inert |
| ss 68, 69 | encoded: (2); the rest inert |
| s 70 | encoded: (2), (3); (1) inert |
| s 71 | encoded: (1) (compoundability an input) |
| ss 72-74 | inert (s 74 exemption is an input to s 5) |
| s 75 | encoded: (3)-(4); (1)-(2), (5) inert |
| ss 76-78, Fifth Schedule | encoded: s 76(4); the rest inert |
| s 79 | encoded: (1), (2); (3) inert |
| First Schedule | encoded (63 gases) |
| Second Schedule | encoded (Parts 1-3) |
| Third Schedule | encoded (Parts 1, 2) |

No row is deferred.

## 5. Fork register

| fork | text | readings | taken |
|---|---|---|---|
| F1 | Act 37 of 2022 (wef 1 January 2024) rewrote most of Parts 3 and 5 | earlier years under the old text | refuse every year or event before 2024; the Third Schedule's printed tables still answer |
| F2 | s 7(5)(d): Y registers "as a reportable facility or as both ... (as the case may be)" | which case | taxable where the facility was a taxable facility of X, or attained the second threshold in the year before the transfer (the cases s 8(1)(a)(ii)(B)-(C) provide for) |
| F3 | s 15(1): "7 working days" | no definition | days other than Saturdays, Sundays and public holidays; holidays an input |
| F4 | s 17(3): credits "assessed ... to have a total carbon price equal to the amount of tax" | a fractional credit | the year of purchase's price; rounded up, so the credits cover the tax (s 17(3B) rounds down for revisions) |
| F5 | s 17(4): the 5%, the 60 days, the completed months, "triple ... in total" | when the 5% is imposed; what the cap covers | imposed the day after the last day; months counted from 60 days after; the cap covers the additional 1% penalties; unpaid amount constant |
| F6 | s 4(2)-(3) with two persons of equal greatest authority | — | refuse |
| F7 | s 8(1)(a)(ii): where both (A) and (C) could apply | — | (C) (X's taxable registration) prevails |

## 6. Answer tables

| | 2023 and before | 2024 | 2025 | 2026 | 2027 on |
|---|---|---|---|---|---|
| carbon tax rate (per tCO2e, by emissions year) | $5 | $25 | $25 | $45 | $45 |
| carbon price (per FPCC, by year of purchase) | $5 | $5 | $25 | $25 | $45 |

Thresholds: first 2,000 tCO2e (register, report); second 25,000 tCO2e (taxable, verified reports, monitoring plan).

| offence | maximum |
|---|---|
| s 54(1), (2) not applying to register | $5,000 |
| s 54(3) not registering a taxable facility | 10% of the tax + $10,000; $50 a day |
| s 55(1), 56(1) report not submitted | $1,000; $50 a day |
| s 55(2) inaccurate report | $10,000; $20,000 second offence |
| s 56(2)-(5) inaccurate verified report | 1x / 2x + $5,000 or 3 years / 3x + $10,000 or 3 years / 4x + $50,000 or 5 years the tax undercharged |
| s 57(2) inaccurate monitoring plan | $50,000 |
| s 59 not paying a demand note | 3x the tax |
| s 60 | $10,000 or 3 years |
| s 62(1) records | $5,000; $10,000 or 3 years second offence |
| s 76(4) regulations | $50,000 or 2 years |

## 7. Known limits

- s 12(2), 12(3)(b): partial verification of a report is not an output; the duty is reported for the whole year.
- s 29: the power to cancel credits is not a predicate; its effect on tax paid is.
- s 34: "refusing to deregister a reportable facility" is not among the appealable decisions, as the Act says; it is `some other decision`.
- s 67(5)(b): service by email is taken as effective on the day sent; the Act says when "capable of being retrieved".
- s 70(3) is a daily fine only.

## 8. The independent test pass

A fresh session wrote about 190 expectations from the brief and the source before opening any module, then `tests-independent.l4` (266 assertions). First run: **262 satisfied, 4 failed**, all of one kind: dated rules for ss 9(2), 17(1), 24 and 37(2) answered for 2023 instead of refusing. **Encoding error**: the vintage gate was missing from most dated rules. Fixed for every dated rule; all 266 independent assertions now pass, unchanged. See `INDEPENDENT-TEST-REPORT.md`.

## 9. Checks

`L4=~/.local/bin/l4 ./check.sh`, 2026-10-06: **8 modules, 0 errors, 487 assertions satisfied, 0 failed** (221 encoder, 266 independent). No assertion is expected to fail.

## 10. Open questions for a domain expert

1. F4: how the Agency rounds the credits assessed under s 17(3) when the price and the rate differ.
2. F5: whether the s 17(4)(c) cap ("triple ... in total") includes the 5% penalty.
3. F3: whether NEA counts Singapore public holidays out of the 7 working days.
4. The text before 1 January 2024, to answer emissions years 2019-2023.
