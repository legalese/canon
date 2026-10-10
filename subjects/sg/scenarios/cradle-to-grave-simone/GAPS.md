# Gap register for the cradle-to-grave scenario

What [`SCENARIO.md`](SCENARIO.md) needs that this repository does not hold on 10 October 2026. Six sections: Acts with no encoding row, ranked by how hard the scenario leans on them; encoded Acts whose row stops short of the question asked; subsidiary legislation that no row retrieved; policy that has no legislative instrument; the common-law doctrines a case register would have to carry; and seams between rows that a runnable scenario will trip over.

The first eighteen of these gaps are written up as briefs in the requirement ledger at [`subjects/sg/requirements.jsonl`](../../requirements.jsonl), in the shape described in [`tools/society-sim/LEDGER.md`](../../../../tools/society-sim/LEDGER.md); the simulation will raise the rest.

Status of every subject was read from `subjects/sg/*/encodings/*/encoding.json` on 2026-10-10; "no row" means the source is deposited under `registers/source-bundle/` and nothing has been encoded from it.

## A. Acts the scenario touches that have no encoding row

Ranked by weight in the story. While this register was being written, rows landed for fifteen subjects that had been on this list — the Women's Charter, the Constitution, the Retirement and Re-employment Act, the Hire-Purchase Act, the Estate Agents Act, the Estate Duty Act, the Guardianship of Infants Act, the Compulsory Education Act, the Early Childhood Development Centres Act, the Holidays Act, the CareShield Life and Long-Term Care Act, the Deposit Insurance and Policy Owners' Protection Schemes Act, the National Servicemen (Employment) Act, the Education Endowment and Savings Schemes Act and the Skills Development Levy Act — so those whose new row stops short of a scenario question appear in section B, and none appears here. Re-run `check-status.py` before trusting this list.

| rank | Act | where the scenario needs it | what to encode first |
| --- | --- | --- | --- |
| 1 | **Conveyancing and Law of Property Act 1886** | Ch 8 (option, sale and purchase of the EC) | ss 3-7 (conveyances, covenants); the rest is largely obsolete and should be marked inert. |
| 2 | **Census Act 1973** and the Interpretation Act | Ch 7 (the 2030 census; every age computation) | Census Act ss 4-12 (the duty to answer, secrecy). The **Interpretation Act 1965** is used silently on every page of the scenario: when a person "attains" an age, how days are counted, what "month" means. It has no row either, and the Women's Charter's own worked example (a person born 21 July 2021 attains 18 on the anniversary) shows why one is needed. |
| 3 | **Singapore Examinations and Assessment Board Act 2003**; **NUS (Corporatisation) Act 2005**; **Singapore Institute of Technology Act 2014**; the polytechnic Acts | Ch 1-3 | Constitutive Acts with few citizen-facing rules; a row would mostly be inert sections. Low priority; record them as touched. |
| 4 | **Skills and Workforce Development Agency Act 2026**; **Lifelong Learning Endowment Fund Act 2001** | Ch 8 (SkillsFuture at 40) | Constitutive; the credit itself is policy. Low priority. |
| 5 | **Pioneer Generation and Merdeka Generation Funds Act 2014** | Ch 9 | A negative answer only: she was born too late. A row of two or three sections would let the assistant say "no, because" with a citation, as the Estate Duty row now does for s 2A. |
| 6 | **Minors' Contracts Act 1987** | Ch 1-2 (bank accounts, the part-time job before 21) | s 2 (guarantees) is all the Act does; the capacity of a minor to contract is common law (section E). |

Not touched because the scenario is sunny, but adjacent and also without a row: Maintenance of Parents Act 1995, Community Disputes Resolution Act 2015, Legitimacy Act 1934, Status of Children (Assisted Reproduction Technology) Act 2013, Termination of Pregnancy Act 1974, Voluntary Sterilisation Act 1974, Debt Collection Act 2022, Protection from Scams Act 2025, Inheritance (Family Provision) Act 1966, Policies of Assurance Act 1867, Sale of Goods Act 1979 and Supply of Goods Act 1982 (the CPFTA row treats their answers as facts in its records).

## B. Encoded Acts where the scenario's question falls outside the row's scope

| Act and row | what the scenario asks | what the row says it does not cover |
| --- | --- | --- |
| **Central Provident Fund Act 1953** `naive-2026-10` | contribution rates and allocation on every payslip (Ch 4); the housing withdrawal and the Board's charge (Ch 5, 7); Home Protection Scheme (Ch 7); Dependants' Protection Scheme (Ch 4); CPF LIFE at 65 (Ch 7, 9); Medisave withdrawal limits for confinement (Ch 6); the Education Scheme (Ch 3) | "NOT ENCODED: the First Schedule contribution rates, s 13 (crediting into the three accounts), s 15AA, s 15(4), the housing and investment charges, the rest of s 25, and everything from Part 3A onwards." That excludes Part 3A (Lifelong Income Scheme, ss 27K ff), Part 4A (Home Protection, ss 29 ff) and Part 5 (Dependants' Protection, ss 41 ff). This is the second-largest hole after the Women's Charter: the Act the assistant is asked about most often answers least. |
| **Women's Charter 1961** `naive-2026-10` (landed 2026-10-10) | notice of marriage and its lapse (Ch 5); solemnisation (Ch 5); what marriage does to the spouses' property (Ch 5) | the row takes void marriages (ss 9, 11-13), remarriage (s 6A), consents for a minor (ss 17(2), 21A), maintenance (s 69), protection orders and divorce grounds; "not encoded: ... solemnisation procedure and caveats". ss 14-15 (notice), s 22 (solemnisation) and ss 46-52 (rights, duties and property of spouses) are the next cut for this scenario. |
| **Retirement and Re-employment Act 1993** `naive-2026-10` (landed 2026-10-10) | the actual retirement and re-employment ages (Ch 7, 9) | the row's own first finding: "the Act does not say what the retirement or re-employment age is". ss 4(1) and 7A(11) give the Minister a range; the gazetted ages (63 and 68 in 2026) enter as facts. |
| **Hire-Purchase Act 1969** `naive-2026-10` (landed 2026-10-10) | the copies of documents the owner must serve (Ch 7) | s 4 is not in the row's list (ss 2, 5, 8, 11, 14-17, 21, 29, 32(5), 33, 35-37, 39, 48); the hirer's rights and repossession are. |
| **Education Endowment and Savings Schemes Act 1992** `naive-2026-10` (landed 2026-10-11) | the Edusave account and what is paid into it (Ch 1) | the row is scoped to the Post-Secondary Education Scheme (ss 20-24); Parts 2-4 (Edusave Endowment Fund, Pupils Fund, withdrawals) are the next cut. |
| **CareShield Life and Long-Term Care Act 2019** `naive-2026-10` (landed 2026-10-10) | the premium at 30 and the years it is payable (Ch 5, 7, 9) | s 6(1)(a) (who is insured) is in the row; the premium amounts and the age at which premiums stop are in regulations (section C). |
| **Employment Act 1968** `naive-2026-10` | childcare leave (Ch 6-7); any replay of a confinement before 22 Aug 2015 | ss 84-87A are not encoded (the CDCSA row carries childcare leave instead); Part 9 encodes only confinements after 22 Aug 2015. |
| **Stamp Duties Act 1929** `naive-2026-10` | the PPHS lease (Ch 5); ABSD remission had they bought the EC before selling the flat (Ch 8) | Art 8 (leases), s 15 and the remission rules are not encoded. |
| **Road Traffic Act 1961** `naive-2026-10` | Marcus's driving licence at 18 (Ch 2); registration, road tax and the certificate of entitlement for the car (Ch 7) | only the driving offences are encoded; Part 1 (vehicles) and the licensing provisions beyond the s 35 offence are not. |
| **Town Councils Act 1988** `naive-2026-10` | the monthly conservancy charge (Ch 7) | s 51 (levying) is not encoded; s 66 (arrears) is. |
| **Property Tax Act 1960** `naive-2026-10` | the owner-occupier rate (Ch 7) | the rate orders under s 9(2) were not retrieved; the statutory 36% in s 9(1) is never what an owner-occupier pays. |
| **Infectious Diseases Act 1976** `naive-2026-10` | compulsory childhood vaccination (Ch 0, 6) | ss 47-48 and the Third Schedule are outside the row. |
| **Animals and Birds Act 1965** `naive-2026-10` | dog licensing and rabies vaccination (Ch 7) | s 40 and the licensing rules are outside the row; Part 4 (welfare) is in. |
| **Land Titles Act 1993** `naive-2026-10` | joint tenancy and survivorship of the flat (Ch 8, 9) | Part 17 and s 46 only. The co-ownership provisions (s 53) are not encoded. |
| **Environmental Public Health Act 1987** `naive-2026-10` | cremation (Ch 8) | public-cleansing offences only. |
| **Electricity Act 2001, Public Utilities Act 2001, Gas Act 2001** `naive-2026-10` | opening and paying a utilities account (Ch 7) | offence and penalty sections only. |
| **Banking Act 1970** `naive-2026-10` | the credit card at 23 (Ch 4) | s 57 is encoded; the income and age conditions are in regulations (section C). |
| **MediShield Life Scheme Act 2015** `naive-2026-10` | the premium at each age and the subsidy at 65 (Ch 9) | s 4 is in the row but the premium table is in regulations. |
| **Customs Act 1960** `naive-2026-10` | the duty-free allowance on the way home (Ch 1, 6) | the offences and presumptions are encoded; "no duty rates, allowances or the fuel order were retrieved". |
| **Public Trustee Act 1915** `naive-2026-10` and the **succession** rows | whether Siew Lan's estate can go through the Public Trustee (Ch 8) | the value limits are prescribed; the rows take them as facts. |
| **Silver Support Scheme Act 2015** `naive-2026-10` | Boon Keng's and Simone's eligibility (Ch 7, 9) | the row is complete for ss 6-19, but the flat-type, income and lifetime-contribution thresholds are "eligibility criteria that may be prescribed" (s 6(1)(c)) and are facts supplied. |

## C. Subsidiary legislation the scenario needs and no row has retrieved

Named instruments, each with the chapter that needs it. Where the title is from memory and not from a deposited text it is marked (†) and should be confirmed against SSO before anything is encoded from it.

**Work and pay**
- CPF Act First Schedule (contribution rates by age band and wage) — Ch 4 and every payslip after. The Schedule is part of the Act, so it is a row-scope gap, not a retrieval gap.
- Central Provident Fund (Allocation of Contributions)† regulations or the Board's allocation rates — Ch 4.
- The CPF exemption for students in approved internships — Ch 3.
- Skills Development Levy Regulations (the 0.25% rate, $2 floor, $11.25 cap) — Ch 4.
- Employment (Part IV) Regulations† and the salary thresholds that move Part 4's reach — Ch 2, 4.
- Child Development Co-Savings Regulations and the Child Development Co-Savings (Government-Paid Maternity/Paternity/Shared Parental Benefits) regulations† — Ch 6: the CDCSA row's own open question is that "the prescribed periods for total income ... would let the Government-paid benefits be computed rather than capped".
- Banking (Credit and Charge Card) Regulations 2013 (minimum age 21, minimum annual income) — Ch 4.
- The Gazette notifications under Retirement and Re-employment Act ss 4(1) and 7A(11) that fix the retirement and re-employment ages — Ch 7, 9. The row encodes the ranges; the ages themselves are facts.

**Housing**
- CPF (Approved Housing Schemes) Regulations — Ch 5, 7, 9 (using Ordinary Account savings; the Board's charge; the valuation limit).
- CPF (Home Protection Insurance Scheme) Regulations† — Ch 7.
- The rules prescribing the minimum occupation period under HDA s 55 — Ch 7, 8.
- Executive Condominium Housing Scheme Regulations (the income ceiling, family nucleus, minimum occupation period for an EC) — Ch 8.
- Stamp Duties (Spouses) (Remission of ABSD) Rules† — Ch 8.
- Property Tax (Rate for Owner-Occupied Residential Premises) Order — Ch 7.
- Town Councils by-laws and the conservancy and service charge rates of the Tampines town council — Ch 7.
- MAS Notice 632 (loan-to-value) and Notice 645 (total debt servicing ratio) — Ch 8. These are notices, not subsidiary legislation, but they bind the bank.
- Building Control Regulations (what is an insignificant building work) — Ch 7.
- Public Utilities (Water Supply) Regulations (water conservation tax) — Ch 7.

**Health and old age**
- MediShield Life Scheme Regulations (premiums by age, subsidies, the Additional Premium Support) — Ch 0, 9.
- CareShield Life and Long-Term Care (Premiums)† regulations — Ch 5, 7, 9.
- CPF (Medisave Account Withdrawals) Regulations (the Medisave Maternity Package limits, the outpatient and inpatient caps) — Ch 6, 9.
- CPF (Lifelong Income Scheme) Regulations (the CPF LIFE plans, payout ages, deferral) — Ch 7, 9.
- The retirement sums prescribed under the CPF Act's definition of "retirement sum" — Ch 8, 9.
- Silver Support Scheme Regulations (the prescribed thresholds) — Ch 7, 9.
- Infectious Diseases (Vaccination)† regulations and the National Childhood Immunisation Schedule — Ch 0, 6.
- Human Organ Transplant (Registration of Objection)† regulations — Ch 2.
- Mental Capacity Regulations (the LPA forms, the certificate issuer) — Ch 9.
- Advance Medical Directive Regulations (the form, the register) — Ch 9.

**Civil status and the State**
- Registration of Births and Deaths Regulations (forms, fees, late-registration penalties) — Ch 0, 6, 8, 9.
- National Registration Regulations (the re-registration age, fees, the Multi-Purpose card) — Ch 2, 7.
- Passports Regulations (validity, fees, a child's passport) — Ch 1, 6.
- Parliamentary Elections (Registration of Electors) Regulations; Presidential Elections (Registration of Electors)† — Ch 2, 5.
- Compulsory Education (Exemption) Regulations — Ch 1.
- Census Order† for the 2030 census (made under the Census Act s 4) — Ch 7.
- Enlistment Regulations (exit permits for a full-time serviceman) — Ch 8.

**Travel, vehicles, animals**
- Customs (Duties) Order and the Customs (Duties) (Exemption) Order (duty-free allowance) — Ch 1, 6.
- Goods and Services Tax (Imports Relief) Order (the $500 relief after 48 hours away) — Ch 1, 6.
- Road Traffic (Motor Vehicles, Driving Licences) Rules (minimum age, classes, the probationary plate) — Ch 2.
- Road Traffic (Motor Vehicles, Quota System) Rules (the certificate of entitlement) — Ch 7.
- Road Traffic (Motor Vehicles, Registration and Licensing) Rules (registration, road tax) — Ch 7.
- Animals and Birds (Dog Licensing and Control) Rules — Ch 7.

**Death and estates**
- Family Justice Rules (probate practice; the schedule of assets; the small-estate procedure) — Ch 8, 9.
- Public Trustee (Fees)† rules and the value limits for the Public Trustee's summary administration — Ch 8.
- CPF (Nominations) Rules† (the form, witnesses, the Minister's maximum nomination amount) — Ch 8, 9.
- Insurance (Nomination of Beneficiaries) Regulations 2009 — Ch 4, 8.

## D. Policy with legal effect and no instrument

These decide outcomes in the scenario and are nowhere in legislation. The child-support row is the model for encoding them: a dated, cited, "as published" row that says on its face it is policy, not law.

| area | the policy | chapter |
| --- | --- | --- |
| HDB | eligibility schemes (fiancé/fiancée, family nucleus), citizenship and age conditions, the income ceilings ($14,000 BTO, $16,000 EC), the HDB Flat Eligibility letter, the Enhanced CPF Housing Grant table, HDB loan terms (2.6%, 75% LTV), the Standard/Plus/Prime classification, the resale levy, the Parenthood Provisional Housing Scheme, renovation permits, the fire insurance requirement, approved dog breeds, 2-room Flexi lease lengths and the refund of an unexpired short lease, the Silver Housing Bonus | 5, 7, 8, 9 |
| CPF Board | the retirement sums each year, the Ordinary Wage ceiling, the Medisave Grant for Newborns, the Matched Retirement Savings Scheme, CPF LIFE plan choice | 4, 6, 7, 8, 9 |
| MOE | Primary 1 registration phases and the distance rule, Edusave awards, the Tuition Grant, the Tuition Fee Loan, PSLE scoring bands | 1, 3, 7 |
| ECDA | infant care and childcare Basic and Additional Subsidies | 6, 7 |
| MOH | MediShield Life premium subsidies, Medisave use caps, Healthier SG | 0, 9 |
| IRAS | the filing requirement and the No-Filing Service, Budget-year personal income tax rebates | 2, 4 |
| MINDEF | make-up pay during in-camp training, the NS HOME award, exit permit practice | 5, 8 |
| SkillsFuture Singapore | SkillsFuture Credit, the Level-Up Programme at 40 | 8 |
| MOF | GST Vouchers, Assurance Package, CDC vouchers; the Majulah Package by birth year | 4, 9 |
| MAS | LTV and TDSR notices; the credit card income rule is in regulations but the "unsecured credit" caps are notices | 4, 8 |
| MOM | the Tripartite Guidelines on Flexible Work Arrangement Requests, probation practice | 4 |

## E. Common law and case law the scenario depends on

A sunny day avoids litigation, but it still stands on doctrines no statute states. A case register would need, at least:

| doctrine | where the scenario stands on it | note |
| --- | --- | --- |
| the contract of employment: implied terms, probation, confirmation, the meaning of "notice" when the contract and s 10 differ | Ch 4, 7 | the Employment Act is a floor; everything above it is contract |
| a minor's capacity to contract (necessaries; beneficial contracts of service) | Ch 1 (the savings account), Ch 2 (the part-time job at 18) | the Minors' Contracts Act 1987 speaks only to guarantees |
| residential tenancy: the lease, the deposit, quiet enjoyment, repair | Ch 5 (the PPHS flat) | Singapore has no residential tenancies statute; the HDB's standard terms and the common law do the work |
| the option to purchase and the sale and purchase agreement for the EC; time of the essence; completion | Ch 8 | the Conveyancing and Law of Property Act has no row and does little here anyway |
| joint tenancy and survivorship; severance | Ch 5, 8, 9 (every home they own) | Land Titles Act s 53 is outside the row; survivorship on each death is common law applied to a registered title |
| CPF monies do not form part of the estate and pass by nomination, not by will | Ch 8, 9 | the usual citation is *Saniah bte Ali v Abdullah bin Ali* [1990] (Singapore High Court); verify before relying on it |
| trust nominations under the Insurance Act create a trust in favour of the nominee; revocable nominations do not | Ch 4, 8, 9 | the Act is encoded; what the trust does on the policyholder's insolvency or divorce is case law |
| construction of wills (the armchair principle; lapse; "everything to my husband, then to my children") | Ch 8, 9 | the succession rows encode formal validity and the intestacy rules, not construction |
| "issue" and per stirpes distribution under ISA s 7 | Ch 8 (Siew Lan's estate) | the rows encode it; the edge cases (a predeceased child leaving children) are rule 3 read with s 7's final paragraph and the cases on it |
| "ordinarily resident" for the register of electors | Ch 2, 5 | an input to the Parliamentary Elections Act row |
| judicial review of HDB and CPF decisions (the limits of the Board's discretion) | Ch 5, 7 | the HDA row treats every discretion as an input; the cases say when a refusal can be challenged |
| the "lemon law" presumption and what a "reasonable" time to repair is | Ch 7 | the CPFTA row is complete; reasonableness is for a tribunal |
| when a person "attains" an age; computing "days" and "months" | every chapter | Interpretation Act 1965 (no row) and the Women's Charter's own worked example |

## F. Seams between rows that a runnable scenario will trip over

1. **No cross-subject import.** `l4` cannot import across subjects, so every Act is its own file with the facts repeated; the Public Prosecutor v Tan scenario's `build.py` is the pattern. `facts.json` is written to be that build's single input.
2. **Two rows for the same child.** The `child-development-co-savings-act-2001` row (the Act as printed, cohorts included) and the `child-support/legalese` row (the Package as announced, plus childcare leave under ss 12B-12CA) overlap on childcare leave and "have not been reconciled", in the CDCSA row's own words. Chapter 6 asks both; the demo must pick one for each question and say which.
3. **Two rows for succession.** `succession/legalese` and `succession/cleanroom-2026-08` were written independently so that they can be compared. Chapters 8 and 9 should be run against both, and a disagreement is a finding, not a bug in the scenario.
4. **No rule-version axis.** Nearly every row states today's law. The 2003 birth, the 2010 Primary 1 entry, Marcus's 2018 enlistment and Boon Keng's 2025 withdrawal at 55 are replayed under 2026 law. The Income Tax row refuses any year of assessment before 2024; the Employment Act row refuses a confinement before 22 Aug 2015; the child-support row refuses a Cash Gift question for a birth before 2015. Those refusals are correct and the demo should show them.
5. **Facts the rows take as supplied.** The CPF rates and retirement sums, the HDB income ceilings, the MediShield premiums, the stamp duty bands' inputs, the Silver Support thresholds, the Minister's maximum nomination amount and the Public Trustee's limits all enter as facts. `facts.json` carries each one with its date and source so that a demo answer can show where the number came from.
6. **An "announced, not enacted" row inside a life.** Kai En's and Kai Xin's money comes from the Child Support Package, which the child-support row encodes from a National Day Rally announcement with an implementation date of 1 April 2027. If a Bill is introduced the row changes; the scenario's figures for Chapter 6 should be re-run when it does.
7. **The tree is moving under the scenario.** Thirteen subjects changed from "no row" to "row" during the afternoon this register was written, one of them passing through an empty row directory on the way. `facts.json` records a status for every Act an event touches; [`check-status.py`](check-status.py) compares those statuses with the tree and reports every `NONE` that now has a row and every `ENC` or `PART` whose row has gone. Run it before a demo and update the three files together.
