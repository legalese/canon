# Independent expectations — Carbon Pricing Act 2018 (SG)

Written from `../source/CPA2018.txt`, `../source/PROVENANCE.md` and `BRIEF.md` only, before any `.l4`, `NOTES.md` or tests file was opened.
Readings taken where the Act is open are marked **reading**. "REFUSE" means the Act (or the brief's vintage rule) gives no answer and the encoding should refuse rather than return FALSE/0.

Day counting per the brief: "within N days after D" = D + N days; "N years after D" = same date N years later; "at least N days before D" = D − N days at the latest.

## A. First Schedule — GWP and carbon dioxide equivalence (s 2(1) "carbon dioxide equivalence", Sch 1)

| # | facts | expected | provision |
|---|---|---|---|
| A1 | GWP carbon dioxide | 1 | Sch 1 item 1 |
| A2 | GWP methane | 28 | Sch 1 item 2 |
| A3 | GWP nitrous oxide | 265 | Sch 1 item 3 |
| A4 | GWP nitrogen trifluoride | 16,100 | Sch 1 item 4 |
| A5 | GWP sulphur hexafluoride | 23,500 | Sch 1 item 5 |
| A6 | GWP HFC-23 (first HFC, highest) | 12,400 | Sch 1 item 6(a) |
| A7 | GWP HFC-161 | 4 | Sch 1 item 6(k) |
| A8 | GWP HFC-134a | 1,300 | Sch 1 item 6(f) |
| A9 | GWP HFC-1132a | 1 | Sch 1 item 6(za) |
| A10 | GWP (Z)-HFC-1336 | 2 | Sch 1 item 6(zh) |
| A11 | GWP heptadecafluorodec-1-ene (last HFC) | 1 | Sch 1 item 6(zm) |
| A12 | GWP PFC-14 (first PFC) | 6,630 | Sch 1 item 7(a) |
| A13 | GWP PFC-116 (highest PFC) | 11,100 | Sch 1 item 7(b) |
| A14 | GWP perfluorocyclopentene | 2 | Sch 1 item 7(g) |
| A15 | GWP perfluorodecalin (trans) | 6,290 | Sch 1 item 7(n) |
| A16 | GWP perfluorobut-2-ene (last PFC) | 2 | Sch 1 item 7(s) |
| A17 | CO2e of 10 t methane | 280 | s 2(1), Sch 1 |
| A18 | CO2e of 2 t SF6 | 47,000 | s 2(1), Sch 1 |
| A19 | CO2e of 0.5 t HFC-23 | 6,200 | s 2(1), Sch 1 |

## B. Second Schedule — thresholds, non-reckonable, excluded

| # | facts | expected | provision |
|---|---|---|---|
| B1 | first emissions threshold | 2,000 tCO2e | Sch 2 Pt 1 item 1 |
| B2 | second emissions threshold | 25,000 tCO2e | Sch 2 Pt 1 item 2 |
| B3 | SF6 from electrical equipment | non-reckonable | Sch 2 Pt 2 item 2 |
| B4 | SF6 from a manufacturing process (not electrical equipment, no item 6 circumstance) | reckonable | Sch 2 Pt 2 item 2 |
| B5 | CO2 used and emitted in purging | non-reckonable | item 3(a) |
| B6 | CO2 used and emitted in blasting | non-reckonable | item 3(b) |
| B7 | CO2 from using lubricant / paraffin wax | non-reckonable | item 3(c) |
| B8 | CO2 from combustion of charcoal (a listed biomass) | non-reckonable | item 3(d)(iii) |
| B9 | CO2 from combustion of natural gas (not listed) | reckonable | item 3(d) |
| B10 | Methane from purging (item 3 is CO2 only) | reckonable | item 3 |
| B11 | HFC-134a from refrigeration/air-con for non-manufacturing purposes | non-reckonable | item 4 |
| B12 | HFC-134a from refrigeration used for manufacturing purposes | reckonable | item 4 |
| B13 | HFC-1234yf emitted in any circumstance (process) | non-reckonable | item 4A(m) |
| B14 | HFC-23 emitted in a process (not 4A-listed) | reckonable | item 4A |
| B15 | PFC-14 from refrigeration for non-manufacturing purposes | non-reckonable | item 5 |
| B16 | PFC-14 from a process | reckonable | item 5 / 5A |
| B17 | PFC-1114 in any circumstance | non-reckonable | item 5A(h) |
| B18 | any gas from fire protection equipment | non-reckonable | item 6(a) |
| B19 | methane as fugitive emission (not flaring/venting) | non-reckonable | item 6(b) |
| B20 | methane from flaring | reckonable | item 6(b) "excluding flaring and venting" |
| B21 | CO2 from a vehicle transporting goods | non-reckonable (and excluded) | item 6(c); Pt 3 1(a) |
| B22 | CO2 from fuel on which excise duty payable | non-reckonable | item 6(d) |
| B23 | gas from AFOLU activities | non-reckonable (and excluded) | item 6(e); Pt 3 1(b) |
| B24 | vehicle emission — excluded? | excluded | Sch 2 Pt 3 1(a) |
| B25 | AFOLU emission — excluded? | excluded | Sch 2 Pt 3 1(b) |
| B26 | fugitive emission — excluded? | not excluded | Sch 2 Pt 3 |
| B27 | fire-protection emission — excluded? | not excluded (but non-reckonable) | Sch 2 Pt 3 |
| B28 | process CO2 — non-reckonable? | no (reckonable) | s 2(1) |
| B29 | Total reckonable: 20,000 t CO2 (combustion of natural gas) + 200 t methane (process) + 1 t SF6 (electrical equipment) + 5,000 t CO2 (vehicle) | 20,000 + 5,600 = 25,600 tCO2e | s 2(1), s 7(1), Sch 1-2 |

## C. ss 3-5 — business facility, operational control, application

| # | facts | expected | provision |
|---|---|---|---|
| C1 | two parcels contiguous, same controller | single site | s 3(3)(a) |
| C2 | two parcels separated only by a road, same controller | single site | s 3(3)(a) |
| C3 | not contiguous, dependency between activities, same controller | single site | s 3(3)(b) |
| C4 | not contiguous, no dependency, same controller | not a single site | s 3(3) |
| C5 | contiguous but different controllers | not a single site | s 3(3) "same person" |
| C6 | person has authority over environmental policies only | has operational control | s 4(1)(c) |
| C7 | person has authority over none of the three policies | no operational control | s 4(1) |
| C8 | two persons satisfy s 4(1); A has greater authority | A, not B | s 4(3) |
| C9 | two persons satisfy s 4(1) with equal authority | REFUSE (Act silent; s 4(2) says only one) | s 4(2)-(3) |
| C10 | industry sector prescribed? | input (regulations) | s 5(1) |
| C11 | Government charged with an offence | not liable to prosecution | s 5(3) |
| C12 | contractor to Government charged | not immune | s 5(4) |

## D. ss 7-8 — registration (trigger year 2024 or later)

| # | facts | expected | provision |
|---|---|---|---|
| D1 | 2025 reckonable 1,999.9 tCO2e, not registered | no obligation | s 7(1) |
| D2 | 2025 reckonable exactly 2,000, not registered | must apply: registered person + reportable; not taxable | s 7(1)(a)-(b) |
| D3 | 2025 reckonable 24,999 | reportable only, not taxable | s 7(1)(c) |
| D4 | 2025 reckonable exactly 25,000 | registered person + reportable + taxable | s 7(1)(c) |
| D5 | D4 but person already a registered person | no (1)(a); still (b),(c) | s 7(2)(a) |
| D6 | D4, facility already reportable facility of the person | (a) and (c) only | s 7(3) |
| D7 | D4, facility already taxable (and reportable), person registered | no application needed | s 7(2)-(4) |
| D8 | D4, facility will cease to be under person's control by the s 8 deadline | (1)(a) disapplied; (b),(c) still apply as written | s 7(2)(b) |
| D9 | who must apply | person with operational control on 31 Dec of trigger year | s 7(1A) |
| D10 | deadline, trigger year 2025 | 2026-06-30 | s 8(1)(a)(i) |
| D11 | registration in force from (trigger year 2025) | 2026-01-01 | s 8(4)(a) |
| D12 | transfer X→Y; Y not registered | Y must apply as registered person and register facility | s 7(5) |
| D13 | transfer X→Y; Y already registered | (5)(c) disapplied, (5)(d) still applies | s 7(6) |
| D14 | transfer 2025-03-10; 2024 reckonable 10,000 (< 25,000) | deadline 2026-06-30 | s 8(1)(a)(ii)(A) |
| D15 | transfer 2025-03-10; X not taxable; 2024 reckonable 30,000 | later of 2025-06-30 and 2025-04-09 → 2025-06-30 | s 8(1)(a)(ii)(B) |
| D16 | transfer 2025-06-15; X not taxable; 2024 reckonable 30,000 | later of 2025-06-30 and 2025-07-15 → 2025-07-15 | s 8(1)(a)(ii)(B) |
| D17 | transfer 2025-06-15; X's facility is taxable | 2025-07-15 | s 8(1)(a)(ii)(C) |
| D18 | transfer 2025-12-20, X taxable | 2026-01-19 | s 8(1)(a)(ii)(C) |
| D19 | registration under s 7(5) in force from | the transfer date | s 8(4)(b) |
| D20 | facility may be reportable of more than one registered person | yes | s 7(7) |
| D21 | trigger year 2023 | REFUSE (vintage) | brief |
| D22 | transfer in 2023 | REFUSE (vintage) | brief |

## E. ss 9-10 — deregistration

| # | facts | expected | provision |
|---|---|---|---|
| E1 | taxable: person ceases operational control | may apply | s 9(1)(a) |
| E2 | taxable: ceased operating, no intention to resume within 36 months | may apply | s 9(1)(aa) |
| E3 | taxable: ceased operating but intends to resume within 36 months | not on (aa) | s 9(1)(aa) |
| E4 | taxable: below 25,000 each of 3 consecutive years | may apply | s 9(1)(b) |
| E5 | taxable: below 25,000 for only 2 years | may not (no other ground) | s 9(1)(b) |
| E6 | taxable: modification completed, completion year < 25,000, unlikely ≥ 25,000 in next 2 years | may apply | s 9(1)(c) |
| E7 | taxable: modification completed, completion year < 25,000 but likely ≥ 25,000 next year | may not | s 9(1)(c)(ii) |
| E8 | reportable: below 2,000 each of 3 consecutive years | may apply | s 9(3)(b) |
| E9 | reportable: 3 years at 1,500, 2,100, 1,500 | may not | s 9(3)(b) |
| E10 | reportable: below 25,000 but above 2,000 for 3 years | may not (reportable) | s 9(3)(b) |
| E11 | reportable: modification ground with first threshold | may apply | s 9(3)(c) |
| E12 | control to cease 2025-03-01: advance notice due by | 2025-01-15 (45 days before) | s 9(2) |
| E13 | control to cease 2025-12-31 | 2025-11-16 | s 9(2) |
| E14 | registered person, no reportable facility left | may apply to deregister as person | s 9(4) |
| E15 | registered person still has a reportable facility | may not | s 9(4) |
| E16 | person wound up | Agency may deregister on own volition | s 9(5) |
| E17 | person has undischarged liabilities, not wound up | Agency must not deregister person | s 10(4) |
| E18 | undischarged liabilities but wound up (s 9(5)) | may deregister | s 10(4) "except where 9(5) applies" |

## F. ss 11-15 — reporting

| # | facts | expected | provision |
|---|---|---|---|
| F1 | registered person controls reportable facility all of 2025 | must report; reporting period whole year 2025 (2025-01-01 to 2025-12-31) | s 11(1), (2A) |
| F2 | control from 2025-04-01 to year end | reporting period 2025-04-01 to 2025-12-31 | s 11(2A) |
| F3 | report covers excluded GHG emissions? | no | s 11(2) |
| F4 | obligation to submit arises | end of reporting period | s 11(3) |
| F5 | taxable facility report — verification required | yes | s 12(1)(b) |
| F6 | reportable-only facility | no verification required | s 12(1) |
| F7 | non-reckonable part of a taxable facility's report | need not be verified | s 12(2) |
| F8 | part of period before monitoring plan approval | need not be verified | s 12(3)(a) |
| F9 | part of period after deregistration as taxable | need not be verified | s 12(3)(b) |
| F10 | error discovered Monday 2025-03-03, no public holidays supplied (reading: working day = Mon-Fri) | notify by 2025-03-12 | s 15(1) |

## G. s 16, Third Schedule, Division 1A

| # | facts | expected | provision |
|---|---|---|---|
| G1 | carbon tax rate, 2023 emissions year (table as printed) | $5 | Sch 3 Pt 1 1(a) |
| G2 | rate 2024 | $25 | 1(b) |
| G3 | rate 2025 | $25 | 1(b) |
| G4 | rate 2026 | $45 | 1(c) |
| G5 | rate 2030 | $45 | 1(c) |
| G6 | carbon price, credit purchased 2024 | $5 | Sch 3 Pt 2 1(a) |
| G7 | carbon price 2025 | $25 | 1(b) |
| G8 | carbon price 2026 | $25 | 1(b) |
| G9 | carbon price 2027 | $45 | 1(c) |
| G10 | carbon price 2020 | $5 | 1(a) |
| G11 | tax, 2024, 30,000.4 tCO2e | 30,001 × 25 = $750,025 | s 16(3) rounding up |
| G12 | tax, 2026, exactly 25,000 | $1,125,000 | s 16(2)-(3) |
| G13 | tax, 2026, 24,999.9 | no tax (0 / not charged) | s 16(2) |
| G14 | tax, 2025, 40,000 exactly | $1,000,000 | s 16(3) |
| G15 | tax, emissions year 2023 | REFUSE | brief |
| G16 | allowance: 2024, A from 30,000.4 → 30,001, C = 10,000.5 | (A−C)=20,000.5 → 20,001 × 25 = $500,025 | s 20C |
| G17 | allowance 2026, A=50,000, C=20,000 | 30,000 × 45 = $1,350,000 | s 20C |
| G18 | Division 1A applies to 2023 | no | s 20B |
| G19 | Division 1A applies to 2024 | yes | s 20B |
| G20 | Division 1A applies to a late year (end date prescribed) | input / REFUSE without the prescribed date | s 20B, 20F |
| G21 | tax accrues as liability of | registered person with control at end of last reporting period of the year | s 16(4) |

## H. s 17 payment, credits, penalties; s 19, 24, 29, 31A, 32, 33, 33B-C

| # | facts | expected | provision |
|---|---|---|---|
| H1 | 2025 emissions; s 21(1) assessment served 2026-08-01 | due 2026-09-30 (later of 30 Sep and 2026-08-31) | s 17(1)(a) |
| H2 | 2025 emissions; s 21(1) served 2026-09-15 | due 2026-10-15 | s 17(1)(a)(ii) |
| H3 | 2025 emissions; s 21(1) served exactly 2026-08-31 | 30 days = 2026-09-30, = 30 Sep → 2026-09-30 | s 17(1)(a) |
| H4 | s 21(2) best-judgment assessment, 2025 emissions, served 2026-10-01 | 2026-10-31 | s 17(1)(a) |
| H5 | advance assessment (s 22) served 2026-03-01 | 2026-03-31 | s 17(1)(b) |
| H6 | revised assessment (s 23) served 2026-08-01 | 2026-08-31 (no 30-Sep floor) | s 17(1)(b) |
| H7 | tax $750,025 paid in 2025 at $25 | 30,001 credits | s 17(3) |
| H8 | tax $1,125,000 (2026 emissions) paid in 2027 at $45 | 25,000 credits | s 17(3) |
| H9 | revised assessment tax $100 paid in 2027 at $45 | 2.22 → 2 credits (rounded down) | s 17(3B)(a) |
| H10 | revised assessment tax $1,000 paid in 2026 at $25 | 40 credits | s 17(3B)(a) |
| H11 | ICC limit | prescribed → input / REFUSE | s 17(3A), 33B(1) |
| H12 | ICC within limit (limit 10 input, surrendered 8) | all 8 count, each = one FPCC at carbon price | s 33B(3) |
| H13 | ICC above limit (limit 10, surrendered 15), no Ministerial permission | 10 count; 5 excess not counted, no value | s 33B(1), 33C |
| H14 | ICC above limit with Minister's permission | all 15 count | s 33B(2) |
| H15 | 5% penalty, $100,000 unpaid at due date | $5,000 | s 17(4)(a) |
| H16 | paid in full by due date | no penalty | s 17(4) |
| H17 | additional penalty, $100,000 still unpaid, 5 completed months after the 60-day point | $5,000 (1% × 5) | s 17(4)(c) |
| H18 | still unpaid at 59 days after 5% imposed | no additional | s 17(4)(c) |
| H19 | additional penalty, 400 completed months | capped at $300,000 (triple unpaid tax) | s 17(4)(c) |
| H20 | 300 completed months | exactly $300,000 | s 17(4)(c) |
| H21 | refund application deadline, revision made 2025-03-10 | 2029-03-10 | s 19(3) |
| H22 | refund by crediting: reduction $1,000, refund in 2027 ($45), account held, error not Agency's | 22 credits (22.2 rounded down) | s 19(2)-(2B) |
| H23 | reduction $1,000 credited in 2026 ($25) | 40 credits | s 19(2A) |
| H24 | error was the Agency's | not by crediting under (2) (refund otherwise) | s 19(2)(b) |
| H25 | erroneous refund made 2025-05-01 → demand window ends | 2029-05-01 | s 19(4) |
| H26 | waiver: 2025 tax $125 (5 × 2026 price $25) | may waive | s 24 |
| H27 | waiver: 2025 tax $126 | may not | s 24 |
| H28 | waiver: 2026 tax $225 (5 × 2027 price $45) | may waive | s 24 |
| H29 | waiver: 2024 tax $125 (5 × 2025 price $25) | may waive; $126 not | s 24 |
| H30 | failed to pay; has FPCCs in the account | Agency may cancel | s 29(1) |
| H31 | failed to pay; no credits | may not | s 29(1)(b) |
| H32 | conversion in 2025: 100 credits bought at 2024 price $5 | 100 × 5 / 25 = 20 | s 31A |
| H33 | conversion 2025: 7 credits at $5 | 1.4 → 1 | s 31A(2) |
| H34 | conversion 2027: 100 credits at 2026 price $25 | 100 × 25 / 45 = 55.5 → 55 | s 31A |
| H35 | year 2026: credits at 2025 price ($25 = $25) | no conversion (stay 100) | s 31A(1)(b) |
| H36 | suspension period | ≤ 1 year; each extension ≤ 1 year | s 32(1), (3) |
| H37 | closure for inactivity: 5 years since last transaction | ground met; 4 years not | s 33(1)(c) |
| H38 | closure notice required for (c) or (d) | yes; not for (a) or (b) | s 33(2) |
| H39 | notice served 2025-02-01; objection date must be on/after | 2025-03-03 | s 33(3)(b) |
| H40 | objection received in time, not frivolous / withdrawn | must not close | s 33(4) |
| H41 | no objection received | may close | s 33(5) |
| H42 | closure refund: 100 credits at $25 | $2,500 | s 33(6)(b) |
| H43 | closure under (1)(b) | no refund | s 33(7) |

## I. Assessments, objections, appeals (ss 21-23, 34-38)

| # | facts | expected | provision |
|---|---|---|---|
| I1 | VER not submitted, liable | best-judgment assessment available | s 21(2)(a) |
| I2 | VER submitted but cannot be approved before 15 Aug of following year | available | s 21(2)(b) |
| I3 | VER approved in time | s 21(1), not (2) | s 21 |
| I4 | person will cease control of taxable facility, year not yet assessed | advance assessment possible | s 22(1) |
| I5 | year already assessed under 21 | no advance assessment for that year | s 22(1) |
| I6 | revision under 23(1)(a): served 2025-09-01 → last day | 2029-09-01 | s 23(2) |
| I7 | objection deadline, notice served 2025-09-01 | 2025-10-01 | s 23(3)(a) |
| I8 | objection late, extension granted by Agency | valid in time | s 23(4) |
| I9 | objection only to the allowance amount | may not object | s 23(1A) |
| I10 | appeal deadline, decision served 2025-05-10 | 2025-06-09 | s 34(2) |
| I11 | refusal to deregister taxable facility | appealable | s 34(1)(a) |
| I12 | refusal to deregister reportable facility | not appealable under s 34 | s 34(1) |
| I13 | refusal to approve VER / MP | appealable | s 34(1)(b) |
| I14 | refusal to refund under 19(1) or credit under 19(2) | appealable | s 34(1)(c) |
| I15 | refusal to revise assessment under 23 | appealable | s 34(1)(d) |
| I16 | High Court: 2026 rate $45, change $11,249 | no appeal | s 37(2) (250 × 45 = 11,250) |
| I17 | change $11,250 | appeal lies | s 37(2) |
| I18 | 2024 rate $25: change $6,250 | appeal lies; $6,249 not | s 37(2) |
| I19 | Appeal Panel of 3, one specialist | valid; 2 members or no specialist invalid | s 38(1) |

## J. Records, service, extensions (ss 44, 67, 75)

| # | facts | expected | provision |
|---|---|---|---|
| J1 | change in particulars 2025-01-10 | notify by 2025-01-24 | s 44(2)(c) |
| J2 | registered post 2025-03-03 | served 2025-03-05 | s 67(5)(c) |
| J3 | fax with success notification, transmitted 2025-03-03 | served 2025-03-03 | s 67(5)(a) |
| J4 | email without prior written consent | not good service | s 67(6) |
| J5 | email with consent | when retrievable | s 67(5)(b) |
| J6 | extension applied before expiry, decided after expiry | may grant | s 75(3) |
| J7 | extension applied after expiry | may not grant | s 75(3) |

## K. Offences — maximum penalties

| # | facts | expected | provision |
|---|---|---|---|
| K1 | s 47(2) | fine ≤ $10,000, ≤ 12 months, or both | s 47(2) |
| K2 | s 48(3) | $10,000 / 12 months; + $100/day continuing | s 48(3) |
| K3 | s 49(4) | $10,000 / 12 months; + $100/day continuing | s 49(4) |
| K4 | s 51(2) | $2,000 | s 51(2) |
| K5 | s 52 | $10,000 / 12 months | s 52 |
| K6 | s 53 | $5,000 / 6 months | s 53 |
| K7 | s 54(1) | $5,000 | s 54(1) |
| K8 | s 54(2) | $5,000 | s 54(2) |
| K9 | s 54(3), tax that would have been $1,000,000 | 10% + ≤ $10,000 = $110,000 max; + $50/day continuing | s 54(3) |
| K10 | s 54(4) | $5,000 / 6 months | s 54(4) |
| K11 | s 54(5) | $10,000 | s 54(5) |
| K12 | s 55(1) | $1,000 + $50/day | s 55(1) |
| K13 | s 55(2) first | $10,000 | s 55(2)(a) |
| K14 | s 55(2) second | $20,000 | s 55(2)(b) |
| K15 | s 55(2) inaccuracy notified under 15(1) | no offence | s 55(3) |
| K16 | s 56(1) | $1,000 + $50/day | s 56(1) |
| K17 | s 56(2), undercharged $20,000 | fine = $20,000 | s 56(2) |
| K18 | s 56(3) negligence, $20,000 | $40,000 + ≤ $5,000 = $45,000; ≤ 3 years | s 56(3) |
| K19 | s 56(4) wilful, $20,000 | $60,000 + ≤ $10,000 = $70,000; ≤ 3 years | s 56(4) |
| K20 | s 56(5) fraud + wilful, $20,000 | $80,000 + ≤ $50,000 = $130,000; ≤ 5 years | s 56(5) |
| K21 | s 56 inaccuracy notified under 15(1) | no s 56(2) offence | s 56(6) |
| K22 | s 57(1) | $1,000 | s 57(1) |
| K23 | s 57(2) | $50,000 | s 57(2) |
| K24 | s 57(2) notified | no offence | s 57(3) |
| K25 | s 58 | $5,000 | s 58 |
| K26 | s 59, demand note $100,000 outstanding | $300,000 | s 59 |
| K27 | s 60 | $10,000 / 3 years | s 60 |
| K28 | s 61(1), 61(2) | $10,000 each | s 61 |
| K29 | s 62(1) first | $5,000 | s 62(1) |
| K30 | s 62(1) second | $10,000 / 3 years | s 62(1) |
| K31 | s 62(2) | $5,000 | s 62(2) |
| K32 | s 70(3), 10 days non-compliance | $10,000 ($1,000/day) | s 70(3) |
| K33 | s 76(4) regulation offence ceiling | $50,000 / 2 years | s 76(4) |
| K34 | composition of s 54(1) (prescribed compoundable) | ≤ $2,500 | s 71(1)(a) |
| K35 | composition of s 52 (max $10,000) | ≤ $5,000 | s 71(1) |
| K36 | composition of s 57(2) (max $50,000) | ≤ $5,000 | s 71(1)(b) |
| K37 | composition of s 51(2) (max $2,000) | ≤ $1,000 | s 71(1)(a) |
| K38 | offence not prescribed as compoundable | cannot compound | s 71(1) |
| K39 | officer who consented to corporation's offence | guilty of same offence | s 68(2) |
| K40 | officer with no (b) state | not liable under s 68(2) | s 68(2) |
| K41 | partner knowingly concerned in partnership offence | guilty | s 69(2) |

## L. s 79 saving

| # | facts | expected | provision |
|---|---|---|---|
| L1 | ECA-registered corp on 31 Dec 2018, submitted MP in 2018 | registered person; facility reportable and taxable from 2019-01-01 | s 79(1) |
| L2 | 2017 emissions ≥ 2,000, control and ECA registration on 31 Dec 2018 | registered person; reportable only | s 79(2) |
| L3 | 2017 emissions 1,999 | s 79(2) not met | s 79(2)(a) |
| L4 | first reporting period for these | 2019 | s 79(3) |

Note: s 79 events are pre-2024; the brief's vintage rule says earlier events refuse, but s 79 is listed among the goal-1 provisions. Expected: either the source answer above, or REFUSE (both defensible); flagged rather than treated as a finding.
