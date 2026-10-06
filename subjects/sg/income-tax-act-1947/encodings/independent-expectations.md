# Independent expectations: Income Tax Act 1947 (SG)

Written from `../source/ITA1947.txt` and `../source/PROVENANCE.md` alone, before any `.l4`, NOTES.md or tests file was opened. Amounts are S$. "REFUSE" means the Act does not answer (left to regulations or to a discretion), so the encoding should refuse or take the figure as an input.

## A. Residence (s 2)

| # | Facts | Expected | Provision |
|---|---|---|---|
| A1 | Individual, present in Singapore 183 days in the year before the YA | resident | s 2 "resident in Singapore" (a) |
| A2 | Individual, present 182 days, not otherwise residing, not employed | not resident | s 2 (a) |
| A3 | Individual employed in Singapore (not as director) for 200 days | resident | s 2 (a) |
| A4 | Individual, director of a company, exercising directorship 200 days, physically present 100 days, not residing | not resident (the employment limb excludes directors) | s 2 (a) |
| A5 | Individual present 30 days but resides in Singapore apart from reasonable temporary absences | resident | s 2 (a) |
| A6 | Company whose control and management is exercised in Singapore | resident | s 2 (b) |
| A7 | Company incorporated in Singapore, control and management abroad | not resident | s 2 (b) |

## B. Second Schedule Part A and s 42 (resident individuals)

| # | Chargeable income | YA | Expected tax | Provision |
|---|---|---|---|---|
| B1 | 20,000 | 2016 | 0 | Table 1 |
| B2 | 30,000 | 2016 | 200 | Table 1 |
| B3 | 80,000 | 2016 | 3,350 | Table 1 |
| B4 | 200,000 | 2016 | 20,750 | Table 1 |
| B5 | 320,000 | 2016 | 42,350 | Table 1 |
| B6 | 500,000 | 2016 | 78,350 | Table 1 |
| B7 | 40,000 | 2023 | 550 | Table 2 |
| B8 | 120,000 | 2023 | 7,950 | Table 2 |
| B9 | 200,000 | 2023 | 21,150 | Table 2 |
| B10 | 320,000 | 2023 | 44,550 | Table 2 |
| B11 | 1,000,000 | 2023 | 194,150 | Table 2 |
| B12 | 20,000 | 2025 | 0 | Table 3 |
| B13 | 30,000 | 2025 | 200 | Table 3 |
| B14 | 160,000 | 2025 | 13,950 | Table 3 |
| B15 | 320,000 | 2025 | 44,550 | Table 3 |
| B16 | 500,000 | 2025 | 84,150 | Table 3 |
| B17 | 1,000,000 | 2025 | 199,150 | Table 3 |
| B18 | 1,200,000 | 2025 | 247,150 | Table 3 |
| B19 | 100,000 | 2011 | REFUSE (no table printed for YA 2011) | Second Schedule |

## C. s 43 rates

| # | Facts | Expected | Provision |
|---|---|---|---|
| C1 | Company, YA 2025 (rate) | 17% | s 43(1)(a) |
| C2 | Non-resident individual, YA 2023 | 22% | s 43(1)(b)(i) |
| C3 | Non-resident individual, YA 2025 | 24% | s 43(1)(b)(ii) |
| C4 | Trustee (not of incapacitated person) or executor | 17% | s 43(1)(c) |
| C5 | Company rate YA 2006 | 20% | s 43(8)(a) |
| C6 | Company rate YA 2009 | 18% | s 43(8)(b) |
| C7 | Company rate YA 2010 | 17% | s 43(1)(a), (8) |
| C8 | Company YA 2025, CI 10,000, partial exemption | tax 425 (2,500 chargeable) | s 43(6B) |
| C9 | Company YA 2025, CI 200,000, partial exemption | tax 16,575 (97,500 chargeable) | s 43(6B) |
| C10 | Company YA 2025, CI 300,000, partial exemption | tax 33,575 (197,500 chargeable) | s 43(6B) |
| C11 | Company YA 2025, CI 1,000,000, partial exemption | tax 152,575 | s 43(6B) |
| C12 | Qualifying company in 1st of its first 3 YAs, YA 2025, CI 100,000 | tax 4,250 | s 43(6C), (6D)(b) |
| C13 | Same, CI 200,000 | tax 12,750 | s 43(6D)(b) |
| C14 | Same, CI 300,000 | tax 29,750 (175,000 chargeable) | s 43(6D)(b) |
| C15 | Qualifying company but in its 4th YA, YA 2025, CI 300,000 | 33,575 (partial exemption only) | s 43(6C), (6B) |
| C16 | Company YA 2019, CI 300,000, partial exemption | 25,075 (147,500 chargeable) | s 43(6A) |
| C17 | Start-up YA 2019, CI 300,000 | 17,000 (first 100,000 exempt, next 200,000 at 50%) | s 43(6D)(a) |

## D. "Qualifying company" (s 43(10)-(11))

| # | Facts | Expected | Provision |
|---|---|---|---|
| D1 | Incorporated and resident in SG, 20 individual shareholders throughout | qualifying | s 43(10) (b)(i)(A) |
| D2 | 21 shareholders, all individuals | not qualifying | s 43(10) |
| D3 | 5 shareholders, one individual holding 10% throughout, others companies | qualifying | s 43(10) (b)(i)(B) |
| D4 | 5 shareholders, best individual holds 9% | not qualifying | s 43(10) |
| D5 | Incorporated 2015, undertakes property development | not qualifying | s 43(11)(a) |
| D6 | Incorporated 2015, only activity holding investments | not qualifying | s 43(11)(c) |
| D7 | Incorporated in SG but not resident | not qualifying | s 43(10)(a) |

## E. Gross-income rates (s 43(3)-(5), s 43(7))

| # | Facts | Expected | Provision |
|---|---|---|---|
| E1 | NR (no PE, not trade) receives interest within s 12(6), 2025 | 15% of gross | s 43(3)(a) |
| E2 | NR receives royalty for use of movable property, s 12(7)(a), 2025 | 10% of gross | s 43(3A) |
| E3 | NR receives rent for movable property, s 12(7)(d) | 15% | s 43(3)(b) |
| E4 | NR professional (individual, principal place of business abroad), 2025 | 15% of gross | s 43(4)(a) |
| E5 | NR individual arbitrator, income derived 2025 | 10% of gross | s 43(4A)(a) |
| E6 | NR arbitrator, income derived 2028 | 15% (4A window ended 31 Dec 2027) | s 43(4), (4A) |
| E7 | s 43(5) option: payment liable to be made in March 2025 | option deadline 15 May 2025 | s 43(5) |
| E8 | Payment liable in December 2025 | deadline 15 Feb 2026 | s 43(5) |

## F. Non-resident reliefs (ss 40A, 40B)

| # | Facts | Expected | Provision |
|---|---|---|---|
| F1 | NR employee, YA 2025, only SG income employment, CI 100,000 | tax 15,000 (15% exceeds resident tax 5,650) | s 40B(2)(a), (3) |
| F2 | NR employee, YA 2025, CI 1,000,000 | 199,150: the resident floor binds (15% = 150,000 < resident 199,150) | s 40B(3) |
| F3 | NR employee with SRS withdrawal income | s 40B does not apply (24% applies) | s 40B(1)(a) |
| F4 | NR public entertainer, income 2025 | 15% | s 40A(2)(a) |
| F5 | NR public entertainer, income derived 2021 | 10% | s 40A(2A) |
| F6 | NR employee, employment statutory income 60,000, other 40,000 (total AI 100,000), CI 100,000 | 15% on 60,000 = 9,000 plus 24% on 40,000 = 9,600 → 18,600 | s 40B(2)(b) |

## G. Parenthood tax rebates (s 42A)

| # | Facts | Expected | Provision |
|---|---|---|---|
| G1 | Resident; first child (citizen, legitimate) born 2010 | 5,000 for YA 2011 | s 42A(2A) |
| G2 | First child born 2007 | none (first-child rebate starts 1 Jan 2008) | s 42A(2A) |
| G3 | Second child born 2004 | 10,000 | s 42A(1) |
| G4 | Second child born 2003 | none | s 42A(1) |
| G5 | Third child born 2015 | 20,000 | s 42A(2) |
| G6 | Fourth child born 2015 | 20,000 | s 42A(2) |
| G7 | Fifth child born 2015 | 20,000 | s 42A(2B) |
| G8 | Fifth child born 2006 | none (2B starts 2008) | s 42A(2B) |
| G9 | Rebate 20,000, tax payable 5,000 | used 5,000, carry forward 15,000 | s 42A(3) |
| G10 | Non-resident parent | no rebate | s 42A(1) |

## H. Company remissions (ss 92J, 92L)

| # | Facts | Expected | Provision |
|---|---|---|---|
| H1 | YA 2025, tax 33,575, cash grant made | remission 14,787.50 (16,787.50 − 2,000) | s 92L(1) |
| H2 | YA 2025, tax 33,575, no grant | 16,787.50 | s 92L(1) |
| H3 | YA 2025, tax 200,000, grant | 38,000 | s 92L(1)(b) |
| H4 | YA 2025, tax 200,000, no grant | 40,000 | s 92L(1)(b) |
| H5 | YA 2025, tax 3,000, grant | 0 (50% = 1,500 < 2,000) | s 92L(2) |
| H6 | YA 2024, tax 100,000, grant | 38,000 | s 92J(1) |
| H7 | YA 2024, tax 3,000, grant | 0 | s 92J(2) |
| H8 | Grant: CPF for a local employee in 2024 | grant 2,000 | s 92L(3) |
| H9 | Grant: company in liquidation at disbursement | no grant (absent Comptroller permission) | s 92L(4)(b) |
| H10 | YA 2025 remission excludes s 43(3) tax | remission computed on tax excluding 43(3)-(3C) | s 92L(1)(a) |

## I. Section 39 reliefs

| # | Facts | Expected | Provision |
|---|---|---|---|
| I1 | Earned income relief, age 40, EI 50,000 | 1,000 | s 39(1)(a) |
| I2 | Age 40, EI 500 | 500 | s 39(1) "whichever is less" |
| I3 | Age 57, EI 50,000 | 6,000 | s 39(1)(c) |
| I4 | Age 65, EI 50,000 | 8,000 | s 39(1)(d) |
| I5 | Age 40, disabled, EI 50,000 | 4,000 | s 39(1)(b) |
| I6 | Spouse relief YA 2024, spouse income 5,000 | 0 | s 39(2)(a) |
| I7 | Spouse relief YA 2025, spouse income 5,000 | 2,000 | s 39(2)(a) |
| I8 | Spouse relief YA 2025, spouse income 9,000 | 0 | s 39(2)(a) |
| I9 | Handicapped spouse | 5,500 | s 39(2)(d)(iv) |
| I10 | QCR, child under 16 | 4,000 | Fifth Sch para 1 |
| I11 | Handicapped child | 7,500 | s 39(2)(e) proviso (v)/(vi) |
| I12 | Child income 6,000, YA 2025 | 4,000 allowed (≤ 8,000) | Fifth Sch para 3B |
| I13 | Child income 6,000, YA 2024 | 0 (> 4,000) | Fifth Sch para 3A |
| I14 | WMCR, child born 2020, 1st child, mother EI 100,000 | 15,000 | Fifth Sch 5(1A)(c) |
| I15 | WMCR, born 2020, 2nd child | 20,000 | 5(1A)(d) |
| I16 | WMCR, born 2020, 3rd child | 25,000 | 5(1A)(e) |
| I17 | WMCR, child born 2024, 1st | 8,000 (YA 2025) | 5(1AB)(c) |
| I18 | WMCR, born 2024, 2nd | 10,000 | 5(1AB)(d) |
| I19 | WMCR, born 2024, 3rd | 12,000 | 5(1AB)(e) |
| I20 | WMCR born 2024, YA 2024 | 0 (1AB starts YA 2025) | 5(1AB) |
| I21 | WMCR total for three pre-2024 children with EI 50,000: 15%+20%+25% = 30,000 | 30,000 (under 100% EI) | 5(3) |
| I22 | Six pre-2024 children (15+20+25×4 = 135%) with EI 10,000 | capped at 10,000 | 5(3) |
| I23 | Per-child cap: QCR 4,000 + WMCR 25% of EI 400,000 (100,000) | total 50,000 (WMCR cut to 46,000) | 6(2), 6(3) |
| I24 | Life insurance/CPF: CPF 3,000 + premiums 4,000, YA 2025 | 5,000 | s 39(2)(g)(ii) |
| I25 | CPF 6,000 + premiums 2,000 | 6,000 | s 39(2)(g)(ii) |
| I26 | Premium 4,000 on capital sum 20,000 | 1,400 (7% cap) | s 39(2)(g)(i) |
| I27 | Self-employed CPF YA 2025: AI from trade 50,000, contributions 20,000 | 18,500 | s 39(2)(h) |
| I28 | Self-employed: AI 200,000, contributions 40,000 | 37,740 | s 39(2)(h) |
| I29 | Parent relief YA 2025, living with, parent 60, income 6,000 | 9,000 | s 39(2)(i)(iv)(A) |
| I30 | Not living with, maintenance 2,000 | 5,500 | (iv)(B) |
| I31 | Incapacitated, living with | 14,000 | (v)(A) |
| I32 | Incapacitated, not living with | 10,000 | (v)(B) |
| I33 | YA 2024, living with, parent income 6,000 | 0 | (iv) $4,000 limit |
| I34 | Three parents each living with (9,000) | 18,000 (max 2) | (vi) |
| I35 | NSman active, not KCS | 3,000 | s 39(2A)(c) |
| I36 | NSman active, KCS | 5,000 | s 39(2A)(d) |
| I37 | NSman not active, not KCS / KCS | 1,500 / 3,500 | s 39(2B) |
| I38 | Wife of NSman / parent of NSman | 750 each | s 39(2)(m), (n) |
| I39 | SRS relief amount | input (cap set by regulations) | s 39(2)(o) |
| I40 | Grandparent caregiver YA 2025, GP income 6,000 | 3,000 | s 39(2)(p)(iii)(C) |
| I41 | GP caregiver YA 2024, GP income 6,000 | 0 | (p)(iii)(B) |
| I42 | CPF top-up relief amount | input / REFUSE (limits by rules) | s 39(3), (3A) |
| I43 | Course fees YA 2025, fees 8,000 | 5,500 | s 39(12B) |
| I44 | Course fees YA 2026 | 0 (ceased) | s 39(12C) |
| I45 | FDWL YA 2024, levy 3,600 | 7,200 | s 39(11) |
| I46 | FDWL YA 2025 | 0 | s 39(11) |
| I47 | Reliefs totalling 90,000 | 80,000 | s 39A |
| I48 | Chargeable income = AI 120,000 − reliefs 20,000 | 100,000 | s 38 |
| I49 | Sibling relief (incapacitated, living with) | 5,500 | s 39(2)(j) |

## J. Income charged (ss 10, 10G, 10L, 11, 12)

| # | Facts | Expected | Provision |
|---|---|---|---|
| J1 | YA 2025, employer pays rent 60,000 for employee housing; employee pays 12,000 | benefit 60,000 (limb (i) deducts nothing) | s 10(2)(cb)(i) |
| J2 | No rent paid by employer; annual value 30,000; employee pays 6,000 | 24,000 | s 10(2)(cb)(ii) |
| J3 | Share option exercised: OMV 50,000, paid 20,000 | gain 30,000 at exercise | s 10(6)(a) |
| J4 | Moratorium share: OMV when restriction lifts 60,000, paid 20,000 | 40,000 at that time | s 10(6)(b) |
| J5 | Foreigner ceases employment 2025-06-30, option granted 2023-01-01 unexercised | deemed derived 2025-05-30 | s 10(7)(c) |
| J6 | Cessation 2025-06-30, granted 2025-06-15 | deemed derived 2025-06-15 (later date) | s 10(7)(c) |
| J7 | Annuity purchased for 100,000 | 3,000 deemed income per year | s 10(9) |
| J8 | Annuity purchased by employer in lieu of pension, payment 8,000 | 8,000 | s 10(9)(b) |
| J9 | Author royalties YA 2026: gross 100,000, expenses 20,000 | 10,000 | s 10(14) |
| J10 | Same YA 2027 | 40,000 | s 10(14A)(a) |
| J11 | Same YA 2028 | 70,000 | s 10(14A)(b) |
| J12 | Same YA 2029 | 80,000 (s 10(14) no longer applies) | s 10(14B) |
| J13 | Royalties for work published in a newspaper | 80,000 (no concession) | s 10(15) |
| J14 | SRS: withdrew 10,000, contributed 0, before retirement age | income 10,000, penalty 500 | s 10G(1), (2) |
| J15 | SRS: withdrew 10,000 after retirement age | income 5,000, no penalty | s 10G(3)(b), (2) |
| J16 | SRS: withdrew 10,000, contributed 4,000 that year, early | income 6,000, penalty 300 | s 10G(1), (2) |
| J17 | 10L: relevant-group entity sells foreign asset 2024-06-01, gains 1,000,000 remitted, not otherwise taxable, not excluded | chargeable | s 10L(1) |
| J18 | Same but sale 2023-12-31 | not chargeable | s 10L(3) |
| J19 | Same but not member of relevant group | not chargeable | s 10L(1), (5) |
| J20 | Club: 60% of revenue receipts from members | not carrying on business | s 11(1) |
| J21 | Club: 40% from members | whole income deemed business receipts | s 11(1) |
| J22 | Employment exercised in SG, paid abroad | derived from Singapore | s 12(4) |
| J23 | Interest on loan borne by SG resident (not for foreign PE) | derived from Singapore | s 12(6)(a)(i) |
| J24 | Royalty borne by SG resident | derived from Singapore | s 12(7) |

## K. Exemptions (Part 4)

| # | Facts | Expected | Provision |
|---|---|---|---|
| K1 | Dividend from SG-resident company paid 2025 | exempt | s 13(1)(za) |
| K2 | Individual's SG bank deposit interest 2025 | exempt | s 13(1)(zd) |
| K3 | Individual's interest from debt securities, not through trade/partnership | exempt | s 13(1)(ze)(i) |
| K4 | Same but derived from carrying on a trade | not exempt | s 13(1)(ze) proviso |
| K5 | NR individual, deposit interest with approved bank | exempt | s 13(1)(t) |
| K6 | Medisave voluntary contribution 3,000 in 2025 | 2,730 exempt | s 13(1)(jd) |
| K7 | NR short-term employee, 60 days | exempt | s 13(6) |
| K8 | NR short-term employee, 61 days | not exempt | s 13(6) |
| K9 | NR director, 30 days | not exempt | s 13(7)(a) |
| K10 | Resident individual, foreign-sourced income received, not through partnership | exempt | s 13(7A)(b) |
| K11 | Resident individual via SG partnership | not exempt under 13(7A) | s 13(7A) |
| K12 | Resident company, foreign dividend, taxed abroad, headline rate 17%, beneficial | exempt | s 13(8)-(9) |
| K13 | Headline rate 14% | not exempt | s 13(9)(b) |
| K14 | 13W: disposal 2025-06-01, 25% held 30 months | exempt | s 13W(1) |
| K15 | Held 25% for 20 months | not exempt | s 13W(1)(b) |
| K16 | Held 19% for 30 months | not exempt | s 13W(1)(b) |
| K17 | Disposal 2012-05-31 | not exempt (window opens 1 June 2012) | s 13W(1)(a) |
| K18 | First Schedule body (e.g. National Library Board) | exempt | s 13(1), First Sch |

## L. Deductions (Part 5)

| # | Facts | Expected | Provision |
|---|---|---|---|
| L1 | Employer CPF 20,000 on remuneration 100,000 (2025) | 17,000 deductible | s 14(1)(e)(i)(D) |
| L2 | Employer medisave 3,000 for one employee, 2025 | 2,730 | s 14(1)(fb) |
| L3 | Car expenses 10,000; car cost 70,000; car within s 14(4) | 5,000 | s 14(3) |
| L4 | Car cost 30,000 | 10,000 (full) | s 14(3) |
| L5 | Medical cap, portable benefits, remuneration 1,000,000 | 20,000 | s 14(6A)(a) |
| L6 | Medical cap, no qualifying insurance: remuneration 1,000,000, medical 30,000 (excluding general contributions), general contributions 5,000 | 15,000 (A 10,000 + B 5,000) | s 14(6B)(a) |
| L7 | R&D YA 2025: U = 100,000 local, direct | 14C 100,000 + 14D(1) 150,000 + 14D(1A) 150,000 = 400,000 | ss 14C, 14D(1), (1A) |
| L8 | R&D YA 2025: U = 1,000,000 | 14D(1A) 600,000 (cap 400,000 × 150%) | s 14D(1A) |
| L9 | R&D YA 2029 | 14D(1) and (1A) not available | s 14D(1) |
| L10 | 14EA YA 2025, qualifying expenditure 80,000 | 200,000 | s 14EA(1) |
| L11 | 14EA, expenditure 30,000 | 120,000 | s 14EA(1) |
| L12 | 14ZG YA 2025, training expenditure 500,000 | 1,200,000 additional | s 14ZG(1) |
| L13 | 14N renovation 90,000 YA 2025, no election | 90,000 in YA 2025 | s 14N(3A) |
| L14 | Same, elected 3-year spread | 30,000 per YA | s 14N(3) |
| L15 | Renovation 400,000 in a specified period | 300,000 cap | s 14N(7)(f) |
| L16 | 14Z: IPC volunteering, salary expenditure endorsed 10,000, deductible under s 14 | further 15,000 | s 14Z(1A)(a) |
| L17 | 14Z: non-salary, not deductible under s 14, 10,000 | 25,000 | s 14Z(1B)(b) |

## M. Capital allowances (Part 6)

| # | Facts | Expected | Provision |
|---|---|---|---|
| M1 | s 19, acquired YA 2022 basis, cost 120,000, Sixth Sch life 8 | IA 24,000; AA 12,000 | s 19(1), (2)(a) |
| M2 | Acquired YA 2025 basis, cost 120,000, elect 6 years | AA 16,000 | s 19(2)(bb) |
| M3 | Same, elect 12 years | AA 8,000 | s 19(2)(bb) |
| M4 | Life 16 (vessels), elect 16 | AA 6,000 | s 19(2)(bb)(i)(B) |
| M5 | Life 8, elect 16 | not available (REFUSE/invalid) | s 19(2)(bb)(i)(A) |
| M6 | Sixth Sch: aircraft 5, electronic equipment 8, vessels 16, taxis 5, office furniture 10 | as stated | Sixth Sch |
| M7 | s 19A(1), cost 90,000 | 30,000 per year | s 19A(1) |
| M8 | s 19A(1E), YA 2024 expenditure 100,000, elected | 75,000 YA 2024, 25,000 YA 2025 | s 19A(1E) |
| M9 | 19A(1E) for YA 2023 expenditure | not available | s 19A(1E) |
| M10 | 19A(1E) for YA 2025 expenditure | not available | s 19A(1E) |
| M11 | Computer 12,000, elected | 12,000 (100%) | s 19A(2) |
| M12 | Low-value items: 10 × 4,000 | 30,000 (cap) | s 19A(10A), (10B) |
| M13 | Item costing 6,000 | not low-value | s 19A(10A) |
| M14 | s 20: unallowed 40,000, sale 30,000 | balancing allowance 10,000 | s 20(2A) |
| M15 | Unallowed 40,000, sale 50,000 | balancing charge 10,000 | s 20(3) |
| M16 | Cost 100,000, allowances 60,000, sale 120,000 | balancing charge 60,000 (capped) | s 20(4) |
| M17 | s 23: 50% of shares held by same persons | substantially the same | s 23(7)(a) |
| M18 | 49% | not the same → balance not carried forward | s 23(4), (7) |
| M19 | s 19(3) car cost 100,000: IA base | 35,000 | s 19(3) |

## N. Statutory/assessable income, losses, donations

| # | Facts | Expected | Provision |
|---|---|---|---|
| N1 | Unabsorbed CA 30,000; trade 20,000, rent 50,000 | CA against trade first: trade 0, rent 40,000 | s 35(2A) |
| N2 | Donation 1,000 to IPC in 2025 | 2,500 | s 37(3)(c), (3A)(a)(ii) |
| N3 | Donation 1,000 in 2015 | 3,000 | s 37(3A)(b) |
| N4 | Donation 1,000 in 2027 | 2,000 (2.5x window ends 2026) | s 37(3)(c), (3A) |
| N5 | Donation 1,000 in 2012 | 2,500 | s 37(3A)(a)(i) |
| N6 | Donation made 2024 (YA 2025 basis): last YA for unabsorbed balance | YA 2030 | s 37(8) |
| N7 | Company, 50% same shareholders | loss/donation allowed | s 37(12), (14) |
| N8 | 40% same shareholders | disregarded | s 37(12) |
| N9 | s 37B: holding 75% | same group | s 37B(3) |
| N10 | 74% | not same group | s 37B(3) |
| N11 | s 37D: QD 150,000, prior-YA AI 200,000 | carry-back 100,000 | s 37D(3), (5) |
| N12 | QD 50,000, prior AI 30,000 | 30,000 | s 37D(3) |
| N13 | s 37R: selected expenditure 500,000, YA 2025 | payout 20,000 | s 37R(4) |
| N14 | Selected 2,000 | 400 | s 37R(4) |
| N15 | Selected 399 | no election (below 400) | s 37R(1) |
| N16 | Selected 400 | payout 80 | s 37R(1), (4) |
| N17 | Selected expenditure YA 2029 | not available | s 37R(1) |
| N18 | s 27: NR shipowner, no certificate, receipts 1,000,000 | profits 50,000 | s 27(4) |
| N19 | s 33A: additional tax 10,000 under s 33, YA 2025 | surcharge 5,000 | s 33A(2) |
| N20 | s 34E: TP adjustment 200,000 | surcharge 10,000 | s 34E(1) |
| N21 | s 34F: gross revenue exactly 10,000,000, no prior documentation | not required | s 34F(2)(a) |
| N22 | Gross revenue 10,000,001 | required | s 34F(2)(a) |
| N23 | s 34F(8) failure | fine up to 10,000 | s 34F(8) |

## O. Withholding and credits (Parts 12-14)

| # | Facts | Expected | Provision |
|---|---|---|---|
| O1 | Interest to NR individual | 24% | s 45(1)(a)(i) |
| O2 | Interest to NR company (no 43(3)) | 17% | s 45(1)(a)(ii) |
| O3 | Interest within s 43(3) | 15% | s 45(1)(a)(iii) |
| O4 | Royalty within s 43(3A) | 10% | s 45(1)(a)(iii), 45A |
| O5 | Interest paid 2025-01-10 | pay by 2025-03-15 | s 45(4)(a) |
| O6 | Interest paid 2025-12-31 | pay by 2026-02-15 | s 45(4)(a) |
| O7 | Late, tax 10,000 | 500 penalty | s 45(4)(a) |
| O8 | Additional penalty cap, tax 10,000, unpaid 20 months | 1,500 | s 45(4)(b) |
| O9 | s 45(5) failure to give notice, tax 10,000 | penalty 30,000, fine ≤ 10,000, ≤ 3 years | s 45(5) |
| O10 | 3 convictions under s 45 | minimum 6 months | s 45(6) |
| O11 | Interest on qualifying debt securities issued 2025 | s 45 does not apply | s 45(9)(a) |
| O12 | Interest to SG branch of foreign company, 2025 | s 45 does not apply | s 45(9)(c) |
| O13 | s 50 credit: foreign income 100,000, foreign tax 20,000, SG tax 170,000 on AI 1,000,000 | credit 17,000 | s 50(3) |
| O14 | Foreign tax 10,000 on same | 10,000 | s 50(3) |
| O15 | Person not resident in YA | no credit | s 50(2) |
| O16 | s 50C pooled: SG tax on elected income 30,000, foreign taxes 25,000 | 25,000 | s 50C(4) |
| O17 | s 50C: foreign headline rate 14% | not eligible | s 50C(2)(b) |

## P. Administration (Parts 16-19, s 8)

| # | Facts | Expected | Provision |
|---|---|---|---|
| P1 | Chargeable, not asked to file in first 3 months of YA 2026 | notify by 2026-04-14 | s 62(4) |
| P2 | Individual arrived 2025-05-10 | notify by 2025-06-10 | s 62(5) |
| P3 | Company ECI, FYE 2024-12-31 | by 2025-03-31 | s 63(1) |
| P4 | Company ECI, FYE 2025-06-30 | by 2025-09-30 | s 63(1) |
| P5 | Sole-proprietor ECI for YA 2027 | not required | s 63(1B) |
| P6 | Records retention | 5 years | s 67(1)(a) |
| P7 | Goods receipts 20,000 previous year | must issue serial receipts | s 67(1)(b) |
| P8 | Services receipts 12,000 | not required (must exceed) | s 67(1)(b) |
| P9 | s 74 time limit, YA 2025 | 2029-12-31 | s 74(1) |
| P10 | YA 2007 | 2013-12-31 | s 74(1) |
| P11 | Fraud | any time | s 74(2) |
| P12 | Tax 15 | may be waived | s 75 |
| P13 | Tax 16 | not waivable | s 75 |
| P14 | Objection, company, NOA served 2025-03-10 | by 2025-05-10 | s 76(3)(a) |
| P15 | Objection, individual, served 2025-03-10 | by 2025-04-09 | s 76(3)(b) |
| P16 | Refusal to amend 2025-06-01 | notice of appeal by 2025-07-01 | s 79(1)(a) |
| P17 | Notice of appeal lodged 2025-06-20 | petition by 2025-07-20 | s 79(1)(b) |
| P18 | Board decision tax 201 | appeal to High Court available | s 81(2) |
| P19 | Tax 200 | not available | s 81(2) |
| P20 | NOA served 2025-04-15 | tax due 2025-05-15 | s 85(1) |
| P21 | Late tax 10,000 | 500 | s 87(1)(a) |
| P22 | Additional penalty cap on 10,000 | 1,200 | s 87(1)(c) |
| P23 | Refund claim YA 2025 | by 2029-12-31 | s 93(2) |
| P24 | Refund claim YA 2007 | by 2013-12-31 | s 93(2) |
| P25 | Error/mistake: assessment made in YA 2026 | by 2030-12-31 | s 93A(1) |
| P26 | 93A appeal deposit | 250 | s 93A(5) |
| P27 | Notice posted, would be received 2025-03-03 | served 2025-03-04 | s 8(2) |
| P28 | 33A surcharge payment | within one month after notice | s 33A(4) |

## Q. Offences (Part 20)

| # | Facts | Expected | Provision |
|---|---|---|---|
| Q1 | General offence | fine ≤ 5,000, default imprisonment ≤ 6 months | s 94(2) |
| Q2 | Failure to file | fine ≤ 5,000 | s 94A(1) |
| Q3 | Second conviction same YA, continuing 10 days | further 1,000 | s 94A(2) |
| Q4 | Failure 2+ years, tax 8,000 | penalty 16,000 + fine ≤ 5,000 | s 94A(3) |
| Q5 | Incorrect return, tax undercharged 10,000 | penalty 10,000 | s 95(1) |
| Q6 | Negligent incorrect return 10,000 | 20,000 + fine ≤ 5,000 / ≤ 3 years | s 95(2) |
| Q7 | Wilful evasion 10,000 | 30,000 + fine ≤ 10,000 / ≤ 3 years | s 96(1) |
| Q8 | Serious fraudulent evasion 10,000 | 40,000 + fine ≤ 50,000 / ≤ 5 years | s 96A(1) |
| Q9 | Individual with 3 s 96 convictions | minimum 6 months | s 96(2)(a) |
| Q10 | Individual with 2 s 96 convictions | no minimum | s 96(2) |
| Q11 | 2 s 96A convictions | minimum 6 months | s 96A(2)(a) |
| Q12 | 1 s 96A + 1 s 96 | minimum 6 months | s 96A(2)(b), 96(2)(b) |
| Q13 | 1 s 96A only | no minimum | s 96A(2) |

## R. Concessionary rates and schedules

| # | Facts | Expected | Provision |
|---|---|---|---|
| R1 | FTC approved 2016-01-01 | 10% | s 43E(1A)(a) |
| R2 | FTC approved 2020-01-01 | 8% | s 43E(1A)(b) |
| R3 | FTC approved 2024-05-01, awarded 10% | 10% | s 43E(1A)(c) |
| R4 | FTC approved 2024-05-01, awarded 9% | invalid / REFUSE | s 43E(1A)(c) |
| R5 | Aircraft leasing approved 2018 | 8% | s 43N(1)(b) |
| R6 | Aircraft leasing approved 2015, awarded 5% | 5% | s 43N(1)(a) |
| R7 | Global trading company approved 2024-03-01 at 15% | 15% | s 43I(1AA)(c) |
| R8 | Global trading company approved 2020 at 15% | not allowed | s 43I(1AA)(c) |
| R9 | FSI award 13.5% | 13.5% | s 43J(1)(a) |
| R10 | IP development: approved 2025, base 10%, increase 2% | 12% | s 43X(5) |
| R11 | IP development approved 2020, base 15% | not allowed | s 43X(5)(a) |
| R12 | Tonnage, non-green ship 25,000 NT, per day | 108 | Twelfth Sch |
| R13 | Green ship 25,000 NT | 78 | Twelfth Sch |
| R14 | Non-green 550 NT | 4.50 (rounded down to 500 NT) | Twelfth Sch |
| R15 | Non-green 1,000 NT | 9 | Twelfth Sch |
| R16 | Ruling fee, 4 hours | 660 | Seventh Sch Pt 2 para 1(1)(a) |
| R17 | 10 hours | 1,650 | para 1(1)(a), (b) |
| R18 | 4.5 hours | 825 (part hour counted) | para 1(1)(b) |
| R19 | Maximum priority fee on 10 hours | 3,300 | para 1(1)(c) |

## S. Whole-taxpayer and YA boundary

| # | Facts | Expected | Provision |
|---|---|---|---|
| S1 | Resident employee age 40, YA 2025, employment 100,000, obligatory CPF 20,000, one QCR child, no other reliefs | reliefs 25,000; CI 75,000; tax 3,000; due one month after NOA | ss 10, 35, 37, 38, 39, 42, Second Sch, s 85 |
| S2 | Company, YA 2025, CI 300,000, not start-up, cash grant | gross 33,575; remission 14,787.50; net 18,787.50 | ss 43(6B), 92L |
| S3 | NR employee YA 2025, employment 100,000 only | 15,000 | ss 40B, 43(1)(b) |
| S4 | Resident employee as S1 but YA 2023 | REFUSE (brief: computation is for YA 2024 on) | brief |
| S5 | Second Schedule Table 2 at YA 2023, CI 80,000 | 3,350 (the printed table still answers) | Second Sch Table 2 |
| S6 | Company YA 2023 whole computation | REFUSE | brief |
