# Income Tax Act 1947 — notes for a reviewer

## 1. What is encoded

The **Income Tax Act 1947** as printed in SSO's PDF "Current version as at 06 Oct 2026" (`../source/ITA1947.txt`, 1,118 pages, 354 sections in the arrangement), organised under one top-level goal and ten goals, with every section given a disposition in the coverage table (section 4).

The **computation of tax is stated for YA 2024 onwards** (fork I1); an earlier YA refuses. Where the Act itself keeps YA-specific figures (the three Second Schedule tables, relief thresholds by YA, reliefs ending at YA 2026, the YA 2024 and YA 2025 company remissions), they are encoded as printed.

The Act is very large and much of it is made of regimes that turn on an approval or a prescription by the Minister or an authorised body (the exemptions of ss 13A-13X, the further deductions of ss 14A-14ZJ, the concessionary rates of ss 43A-43X). Those are encoded at the goal: the approval, and where the section offers a choice the awarded rate, are inputs; the computation they feed is encoded. The special ascertainment rules of Part 7 (insurers, financial instruments, amalgamations, redomiciled companies) produce an adjusted income figure that is an input. Schemes tied to YAs before 2024 (the Productivity and Innovation Credit, the YA 2011-2020 remissions) are out of the encoded period. The Multinational Enterprise (Minimum Tax) Act 2024 (DTT, MTT) is a separate Act and out of scope. Subsidiary legislation is not in the source: prescribed figures are inputs.

## 2. The goals

**Top-level goal** (`ita-goal.l4`): *how much income tax does this person owe for this year of assessment, and by when?* — `the income tax position for` a `Taxpayer year`: residence; income charged and exempt; statutory, assessable and chargeable income; personal reliefs; tax before rebates; rebates and remissions; credits; tax payable; the last day to pay; the late-payment penalty. It runs through the Act in order, s 2 to s 87.

Under it, ten goals — the questions one can ask, each answered by rules that can be called on their own:

| # | Goal — the question | Main conclusions | Module |
|---|---|---|---|
| 1 | **Is the person resident, and who is chargeable?** (s 2, Part 15) | `resident in Singapore:` …; `who is charged, …` | `ita-rates`, `ita-withholding-credits` |
| 2 | **Is this income charged, and is it derived from Singapore?** (Part 3: ss 2A, 10-12) | `within the charge to tax, being` …; `a payment of` … `is deemed derived from Singapore:` …; `the housing benefit …`; `the gain from an employee share right …`; `the annuity income …`; `the SRS withdrawal of …`; `the foreign asset gains chargeable under s 10L:` … | `ita-charge` |
| 3 | **Is this income exempt?** (Part 4, First Schedule) | `the income is exempt under` … `:` …; `the share disposal gain is exempt under s 13W:` … | `ita-exemptions` |
| 4 | **What may be deducted, and what capital allowances are made?** (Parts 5, 6, Sixth Schedule) | `deductible, an outgoing of kind` …; `the R&D deductions for YA` …; `the maximum allowable medical expenses for` …; `the s 19 annual allowance on` …; `the s 19A allowance by` …; `the balancing adjustment …` | `ita-deductions`, `ita-capital-allowances` |
| 5 | **What are the statutory, assessable and chargeable income?** (Parts 7-10, Fifth Schedule) | `the statutory income …`; `the assessable income from statutory income …`; `the personal reliefs for YA` …; `the chargeable income from assessable income …` | `ita-assessable`, `ita-reliefs` |
| 6 | **At what rate is it taxed, and what rebates, remissions and credits apply?** (Part 11, Second and Twelfth Schedules, ss 42A, 46, 50-50C, 92J, 92L) | `the resident individual rates for YA` …; `the basis of charge for YA` …; `the chargeable income taxed, after the s 43(6) exemptions …`; `the tax with the non-resident relief …`; `the parenthood rebate for a` …; `the company remission for YA` …; `the concessionary tax under` …; `the foreign tax credit …` | `ita-rates`, `ita-concessions`, `ita-withholding-credits` |
| 7 | **What must be withheld from a payment to a non-resident, and when paid over?** (Part 12) | `the withholding rate on` …; `the last day to pay over tax withheld …`; `the late withholding penalty on` … | `ita-withholding-credits` |
| 8 | **What must be filed, when may the Comptroller assess, and how is an assessment disputed?** (Parts 16-18) | `the last day to notify chargeability for YA` …; `the Comptroller may still assess YA` …; `the last day to object …`; `the appeal deadlines …` | `ita-process` |
| 9 | **When is tax due, what is added if it is late, and when is it refunded?** (Part 19) | `the last day to pay tax assessed …`; `the late payment penalty on tax of` …; `a repayment claim for YA` … `is in time` | `ita-process` |
| 10 | **Is an offence committed, and what is the most it can cost?** (Part 20 and elsewhere) | `the penalty for` (culpability) …; `the penalty for failing to file …`; `the maximum penalty for` … | `ita-offences` |

## 3. Modules

| module | what it holds |
|---|---|
| `ita-types.l4` | persons, residence facts, heads and sources of income |
| `ita-rates.l4` | the vintage gate; residence; Second Schedule; s 43 rates and exemptions; gross-income rates; ss 40A-40C; s 42A; ss 92J, 92L |
| `ita-reliefs.l4` | Part 10: s 38, s 39, s 39A, Fifth Schedule |
| `ita-charge.l4` | Part 3 |
| `ita-exemptions.l4` | Part 4, First Schedule |
| `ita-deductions.l4` | Part 5 |
| `ita-capital-allowances.l4` | Part 6, Sixth Schedule |
| `ita-assessable.l4` | Parts 7-9 |
| `ita-withholding-credits.l4` | Parts 12-15 |
| `ita-process.l4` | Parts 16-19, s 8 |
| `ita-offences.l4` | Part 20 and the offences elsewhere |
| `ita-concessions.l4` | ss 43A-43X, s 34K and the Twelfth Schedule |
| `ita-administration.l4` | s 101, s 105, s 108 and the Seventh Schedule |
| `ita-goal.l4` | the top-level goal |
| `ita-tests-*.l4` | the encoder's tests (rates and reliefs, income, process, goal) |
| `tests-independent.l4` | the independent test author's (section 8) |

## 4. Coverage

Every section in the Act's arrangement. *encoded*: a rule decides it. *input*: the figure or approval it yields comes from the caller. *inert*: a power, procedure or information duty with nothing to compute. *out of period*: tied to YAs before 2024. Schedules follow the table.

| section | heading | disposition |
|---|---|---|
| s 1 | Short title | inert |
| s 2 | Interpretation | encoded (residence, `ita-rates`); other definitions applied by the caller |
| s 2A | Purpose of Act | encoded (`ita-charge`); (2)-(6) DTT/MTT out of scope (MMT Act) |
| s 3 | Appointment of Comptroller and other officers | inert: a power, a procedure or an information duty |
| s 3A | Assignment of function or power to public body | inert: a power, a procedure or an information duty |
| s 4 | Powers of Comptroller | inert: a power, a procedure or an information duty |
| s 5 | Approved pension or provident fund or society | inert: a power, a procedure or an information duty |
| s 6 | Official secrecy | inert: a power, a procedure or an information duty |
| s 7 | Rules | inert: a power, a procedure or an information duty |
| s 8 | Service and signature of notices, etc. | encoded: (2) (`ita-process`); rest inert |
| s 8A | Use of electronic service | inert: a power, a procedure or an information duty |
| s 9 | Free postage | inert: a power, a procedure or an information duty |
| s 10 | Charge of income tax | encoded: (1), (2)(cb), (6), (7)-(7AC), (9), (10), (13), (14)-(15), (25) (`ita-charge`); unit-trust and other deeming rules (19)-(24), (26)-(28): inputs |
| s 10A | Profits of unit trusts | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 10B | Excess provident fund contributions, etc., from employer deemed to be income | encoded (`ita-charge`) |
| s 10BA | Voluntary contributions by platform operator deemed to be income | encoded (`ita-charge`) |
| s 10C | Income from finance or operating lease | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 10D | Ascertainment of income from business of making investments | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 10E | Ascertainment of income from certain public-private partnership arrangements | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 10F | Ascertainment of income from business of hiring out motor cars or providing driving instruction or chauffeur services | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 10G | Withdrawals from Supplementary Retirement Scheme | encoded: (1)-(3) (`ita-charge`); rest inert |
| s 10H | Securities lending or repurchase arrangement | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 10I | Additional Tier 1 capital instruments | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 10J | Tax treatment for trading stock appropriated for non-trade or capital purpose | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 10K | Tax treatment for covered bond transactions | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 10L | Gains from the sale of foreign assets | encoded: (1)-(3), (8), (9), (12) (`ita-charge`) |
| s 11 | Ascertainment of income of clubs, trade associations, etc. | encoded: (1) (`ita-charge`); (2)-(4) input |
| s 12 | Sources of income | encoded: (4)-(7AB) (`ita-charge`); (1)-(3), (8) input |
| s 13 | Exempt income | encoded: (1)(d), (e), (i), (j), (jd), (m), (ma), (t), (w), (za), (zb), (zd), (ze)-(zj), (zm), (6)-(10) (`ita-exemptions`); other paragraphs: conditions an input |
| s 13A | Exemption of shipping profits | input: the exemption turns on an approval or prescription (`an approved or prescribed regime`) |
| s 13B | Assessment of income not entitled to exemption under section 43A, 43C, 43D or 43H | input: the exemption turns on an approval or prescription (`an approved or prescribed regime`) |
| s 13C | Exemption of income of trustee of trust fund arising from funds managed by fund manager in Singapore | input: the exemption turns on an approval or prescription (`an approved or prescribed regime`) |
| s 13D | Exemption of income of prescribed persons arising from funds managed by fund manager in Singapore | input: the exemption turns on an approval or prescription (`an approved or prescribed regime`) |
| s 13E | Exemption of international shipping profits | input: the exemption turns on an approval or prescription (`an approved or prescribed regime`) |
| s 13F | Exemption of income of foreign trust | input: the exemption turns on an approval or prescription (`an approved or prescribed regime`) |
| s 13G | Exemption of income of venture company | input: the exemption turns on an approval or prescription (`an approved or prescribed regime`) |
| s 13H | Exemption of tax on gains or profits from equity remuneration incentive scheme (SMEs) | out of period: tied to years of assessment before 2024 (the PIC and earlier schemes) |
| s 13I | Exemption of tax on gains or profits from equity remuneration incentive scheme | out of period: tied to years of assessment before 2024 (the PIC and earlier schemes) |
| s 13J | Exemption of tax on gains or profits from equity remuneration incentive scheme (start-ups) | out of period: tied to years of assessment before 2024 (the PIC and earlier schemes) |
| s 13K | Exemption of tax on income derived by non-ordinarily resident individual | input: the exemption turns on an approval or prescription (`an approved or prescribed regime`) |
| s 13L | Exemption of income of foreign account of philanthropic purpose trust | input: the exemption turns on an approval or prescription (`an approved or prescribed regime`) |
| s 13M | Exemption of income derived from asset securitisation transaction | input: the exemption turns on an approval or prescription (`an approved or prescribed regime`) |
| s 13N | Exemption of relevant income of prescribed locally-administered trust | input: the exemption turns on an approval or prescription (`an approved or prescribed regime`) |
| s 13O | Exemption of income of company incorporated and resident in Singapore arising from funds managed by fund manager in Singapore | input: the exemption turns on an approval or prescription (`an approved or prescribed regime`) |
| s 13OA | Exemption of income of partners of limited partnership arising from funds managed by fund manager in Singapore | input: the exemption turns on an approval or prescription (`an approved or prescribed regime`) |
| s 13P | Exemption of income of shipping investment enterprise | input: the exemption turns on an approval or prescription (`an approved or prescribed regime`) |
| s 13Q | Exemption of trust income to which beneficiary is entitled | encoded (`ita-exemptions`) |
| s 13QA | Exemption of estate income received by beneficiary, etc. | encoded (`ita-exemptions`) |
| s 13R | Exemption of income of not-for-profit organisation | input: the exemption turns on an approval or prescription (`an approved or prescribed regime`) |
| s 13S | Exemption of income derived by law practice from international arbitration held in Singapore | input: the exemption turns on an approval or prescription (`an approved or prescribed regime`) |
| s 13T | Exemption of relevant income of eligible family-owned investment holding company | input: the exemption turns on an approval or prescription (`an approved or prescribed regime`) |
| s 13U | Exemption of income arising from funds managed by fund manager in Singapore | input: the exemption turns on an approval or prescription (`an approved or prescribed regime`) |
| s 13V | Exemption of certain income of prescribed sovereign fund entity, approved foreign government-owned entity, and prescribed or approved international organisation | input: the exemption turns on an approval or prescription (`an approved or prescribed regime`) |
| s 13W | Exemption of gains or profits from disposal of ordinary shares or preference shares | encoded: (1)-(1B) (`ita-exemptions`); exclusions an input |
| s 13X | Exemption of certain payments received in connection with COVID-19 events | input: the exemption turns on an approval or prescription (`an approved or prescribed regime`) |
| s 14 | Deductions allowed | encoded: (1), (1)(e), (fb), (fc), (3), (3A), (5)-(6B) (`ita-deductions`); (2) reasonableness an input |
| s 14A | Deduction for costs for protecting intellectual property | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 14B | Further deduction for expenses relating to approved trade fairs, exhibitions or trade missions, maintenance of overseas trade office, or electronic commerce | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 14C | Expenditure on research and development | encoded (`ita-deductions`) |
| s 14D | Enhanced deduction for qualifying expenditure on research and development | encoded: (1), (1A) (`ita-deductions`); (2) YA 2011-2018 out of period |
| s 14E | Further deduction for expenditure on research and development project | out of period: tied to years of assessment before 2024 (the PIC and earlier schemes) |
| s 14EA | Deduction for expenditure incurred on qualifying innovation projects | encoded (`ita-deductions`) |
| s 14EB | Deduction for payment under innovation cost-sharing agreement | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 14F | Expenditure on building modifications for benefit of disabled employees | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 14G | Provisions by banks and qualifying finance companies for impairment losses, etc., from non-credit-impaired loans and securities | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 14H | Further or double deduction for overseas investment development expenditure | out of period: tied to years of assessment before 2024 (the PIC and earlier schemes) |
| s 14I | Further or double deduction for salary expenditure for employees posted overseas | out of period: tied to years of assessment before 2024 (the PIC and earlier schemes) |
| s 14J | Deduction for upfront land premium | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 14K | Deduction for special reserve of approved general insurer | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 14L | Deduction for treasury shares transferred under employee equity-based remuneration scheme | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 14M | Deduction for shares transferred by special purpose vehicle under employee equity-based remuneration scheme | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 14MA | Deduction for new shares issued by holding company under employee equity-based remuneration scheme | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 14N | Deduction for renovation or refurbishment expenditure | encoded: (3), (3A), (7)(f) (`ita-deductions`) |
| s 14O | Deduction for qualifying training expenditure for years of assessment 2011 to 2018 | out of period: tied to years of assessment before 2024 (the PIC and earlier schemes) |
| s 14P | Deduction for qualifying design expenditure | out of period: tied to years of assessment before 2024 (the PIC and earlier schemes) |
| s 14Q | Deduction for expenditure on leasing of PIC automation equipment under qualifying lease | out of period: tied to years of assessment before 2024 (the PIC and earlier schemes) |
| s 14R | Deduction for expenses incurred before first dollar of income from trade, business, profession or vocation | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 14S | Deduction for amortisation of intangible asset created under public-private partnership arrangement | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 14T | Deduction for expenditure on licensing intellectual property rights | out of period: tied to years of assessment before 2024 (the PIC and earlier schemes) |
| s 14U | Enhanced deduction for expenditure on licensing intellectual property rights | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 14V | Deduction for expenditure incurred to comply with statutory and regulatory requirements | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 14W | Deduction for expenditure incurred by individual in deriving passive rental income in Singapore | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 14X | Attribution of deductible expenses incurred before commencement of trade, etc. | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 14Y | Further or double deduction for qualifying expenditure on issue of debentures and making available debentures for secondary trading | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 14Z | Deduction for expenditure for services or secondment to institutions of a public character | encoded (`ita-deductions`) |
| s 14ZA | Deduction for expenditure incurred in deriving income from driving chauffeured private hire car or taxi | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 14ZB | Deduction for expenditure incurred by individual in deriving commission | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 14ZC | Deduction for payments made to drivers of chauffeured private hire cars and taxis | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 14ZD | Deduction for payments made to lessees or licensees to mitigate impact of COVID-19 event | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 14ZE | Deduction for expenditure incurred in obtaining or granting, etc., leases of immovable properties | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 14ZF | Deduction for expenditure incurred on immovable property while vacant | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 14ZG | Deduction for qualifying training expenditure for years of assessment 2024 to 2028 | encoded (`ita-deductions`) |
| s 14ZH | Deduction for expenditure incurred in deriving income from providing delivery services | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 14ZI | Deduction for real estate investment trust units held by managers of real estate investment trusts | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 14ZJ | Deduction for expenditure on green certificates and green credits | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 15 | Deductions not allowed | encoded: (1) (`ita-deductions`) |
| s 15A | Limit on deduction allowed for leasing or licensing expenditure in 2020 | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 15B | Limit on deduction allowed for leasing or licensing expenditure in 2021 | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 16 | Initial and annual allowances for industrial buildings and structures | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 17 | Balancing allowances and charges for industrial buildings and structures | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 18 | Definitions for sections 16, 17 and 18B | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 18A | (Repealed) | repealed |
| s 18B | Transitional provisions for capital expenditure incurred on industrial buildings or structures on or after 23 Febuary 2010 | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 18C | Initial and annual allowances for certain buildings and structures | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 19 | Initial and annual allowances for machinery or plant | encoded: (1), (2)(a), (bb) (`ita-capital-allowances`) |
| s 19A | Allowances of 3 years or 2 years write-off for machinery and plant, and 100% write-off for computer, prescribed automation equipment and robot, etc. | encoded: (1), (1A), (1E), (2), (10A)-(10C) (`ita-capital-allowances`); PIC (2A)-(2B) out of period |
| s 19B | Writing-down allowances for intellectual property rights | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 19C | Writing-down allowances for approved cost-sharing agreement for research and development activities | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 19D | Writing-down allowance for IRU | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 19E | Use of open-market price for making allowances under sections 19, 19A and 19D | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 20 | Balancing allowances and charges for machinery or plant | encoded: (2A)-(4) (`ita-capital-allowances`) |
| s 21 | Replacement of machinery or plant | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 22 | Expenditure on machinery or plant | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 22A | Order of set-off of allowances | encoded (`ita-capital-allowances`) |
| s 23 | Carry forward of allowances | encoded (`ita-capital-allowances`) |
| s 24 | Special provisions as to certain sales | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 25 | Special provisions as to certain transfers | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 26 | Profits of insurers | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 26A | Ascertainment of income of member of Lloyd’s syndicate | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 27 | Profits of non-resident shipowner or charterer | encoded: (2) (`ita-assessable`) |
| s 28 | Profits of non-resident air transport and cable undertakings | encoded via s 27 (`ita-assessable`) |
| s 29 | (Repealed) | repealed |
| s 30 | (Repealed) | repealed |
| s 31 | Income arising from settlements | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 32 | Valuation of trading stock on discontinuance or transfer of trade or business | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 32A | Valuation of cost of trading stock converted from non-trade or capital asset | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 33 | Comptroller to disregard certain transactions and dispositions | input (the Comptroller's adjustment) |
| s 33A | Surcharge on adjustments under section 33 | encoded (`ita-assessable`) |
| s 34 | Decision of Comptroller no bar to appeal | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 34A | Adjustment on change of basis of computing profits of financial instruments resulting from FRS 39 or SFRS for Small Entities | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 34AA | Adjustment on change of basis of computing profits of financial instruments resulting from FRS 109 or SFRS(I) 9 | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 34AAA | Change of basis for computing profits from financial instruments for insurers | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 34AB | Chargeability of profit or loss from foreign exchange differences | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 34B | Islamic financing arrangements | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 34C | Amalgamation of companies | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 34CA | Transfer of businesses by insurer | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 34D | Transactions not at arm’s length | input (the arm's length adjustment) |
| s 34E | Surcharge on transfer pricing adjustments | encoded (`ita-assessable`) |
| s 34F | Transfer pricing documentation | encoded: (1)-(3), (8) (`ita-assessable`, `ita-offences`) |
| s 34G | Modification of provisions for companies redomiciled in Singapore | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 34H | Tax credits for approved redomiciled companies | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 34I | Adjustments arising from adoption of FRS 115 or SFRS(I) 15 | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 34J | Tax treatment arising from adoption of FRS 116 or SFRS(I) 16 | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 34K | Net tonnage basis of taxation | encoded: Twelfth Schedule rates (`ita-concessions`); election an input |
| s 35 | Basis for computing statutory income | encoded: (1)-(2A) (`ita-assessable`); (4)-(9) inert |
| s 35A | Cessation of source of income commenced before 1 January 1969 | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 36 | Partnership | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 36A | Limited liability partnership | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 36B | Registered business trusts | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 36C | Limited partnership | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 37 | Assessable income | encoded: (1), (3)(a), (3)(c), (3A), (7), (8), (12), (14) (`ita-assessable`) |
| s 37A | Adjustment of capital allowances, losses or donations between income subject to tax at different rates | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 37AA | Deduction for donation of money by person related to or connected with company approved under section 13O, limited partnership approved under section 13OA or person, master fund, etc., approved under section 13U | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 37AB | Deduction for donation of money for overseas emergency humanitarian assistance | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 37B | Group relief for Singapore companies | encoded: (2)-(5) (`ita-assessable`) |
| s 37C | Transfer of qualifying deduction between spouses | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 37D | Carry-back of capital allowances and losses | encoded: (1), (3), (5) (`ita-assessable`) |
| s 37E | Carry-back of capital allowances and losses between spouses | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 37F | Deduction for incremental expenditure on research and development | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 37G | Cash payout under Productivity and Innovation Credit Scheme | out of period: tied to years of assessment before 2024 (the PIC and earlier schemes) |
| s 37H | Productivity and Innovation Credit bonus | out of period: tied to years of assessment before 2024 (the PIC and earlier schemes) |
| s 37I | Modification of sections 37G and 37H in their application to partnership | out of period: tied to years of assessment before 2024 (the PIC and earlier schemes) |
| s 37J | Enhanced deduction or allowance under Productivity and Innovation Credit Plus Scheme | out of period: tied to years of assessment before 2024 (the PIC and earlier schemes) |
| s 37K | Abusive PIC arrangements | out of period: tied to years of assessment before 2024 (the PIC and earlier schemes) |
| s 37L | Promoters of abusive PIC arrangements | out of period: tied to years of assessment before 2024 (the PIC and earlier schemes) |
| s 37M | Penalties for false information, etc., resulting in payment under section 37G or 37H | out of period: tied to years of assessment before 2024 (the PIC and earlier schemes) |
| s 37N | Deduction for qualifying investments in qualifying start-up companies | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 37O | Deduction for acquisition of shares of companies | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 37P | Treatment of unabsorbed donations attributable to exempt income | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 37Q | Exclusion of expenditure or payment subsidised by capital grant | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 37R | Cash payout under Enterprise Innovation Scheme | encoded: (1), (4) (`ita-assessable`) |
| s 37S | Penalties for false information, etc., resulting in payment under section 37R | encoded: the penalty ladder (`ita-offences`) |
| s 38 | Chargeable income | encoded (`ita-reliefs`) |
| s 39 | Relief and deduction for resident individual | encoded (`ita-reliefs`) |
| s 39A | Limit on total deduction under section 39 | encoded (`ita-reliefs`) |
| s 40 | (Repealed) | repealed |
| s 40A | Relief for non-resident public entertainers | encoded (`ita-rates`) |
| s 40B | Relief for non-resident employees | encoded (`ita-rates`, `ita-goal`) |
| s 40C | Relief for non-resident SRS members | encoded (`ita-rates`) |
| s 40D | Relief for non-resident deriving income from activity as public entertainer and employee, etc. | inert: applies the ss 40A-40C rates source by source |
| s 41 | Proof of claims for deduction or relief | inert |
| s 42 | Rates of tax upon individuals | encoded (`ita-rates`) |
| s 42A | Rebate for children of family | encoded: (1)-(3), (10A), (11) (`ita-rates`) |
| s 43 | Rate of tax upon companies and others | encoded: (1), (3)-(6D), (8), (10)-(13) (`ita-rates`); (2) trustee rate an input; (9) prescribed |
| s 43A | Concessionary rate of tax for Asian Currency Unit, Fund Manager and securities company | encoded: the rates the section allows (`ita-concessions`); approval and awarded rate inputs |
| s 43B | Special rate of tax for non-resident shipowner or charterer or air transport undertaking | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 43C | Exemption and concessionary rate of tax for insurance and reinsurance business | encoded: the rates the section allows (`ita-concessions`); approval and awarded rate inputs |
| s 43D | Concessionary rate of tax for headquarters company | encoded: the rates the section allows (`ita-concessions`); approval and awarded rate inputs |
| s 43E | Concessionary rate of tax for Finance and Treasury Centre | encoded: the rates the section allows (`ita-concessions`); approval and awarded rate inputs |
| s 43F | Concessionary rate of tax for offshore leasing of machinery and plant | encoded: the rates the section allows (`ita-concessions`); approval and awarded rate inputs |
| s 43G | Concessionary rate of tax for trustee company | encoded: the rates the section allows (`ita-concessions`); approval and awarded rate inputs |
| s 43H | Concessionary rate of tax for income derived from debt securities | encoded: the rates the section allows (`ita-concessions`); approval and awarded rate inputs |
| s 43I | Concessionary rate of tax for global trading company and qualifying company | encoded: the rates the section allows (`ita-concessions`); approval and awarded rate inputs |
| s 43J | Concessionary rate of tax for financial sector incentive company | encoded: the rates the section allows (`ita-concessions`); approval and awarded rate inputs |
| s 43K | Concessionary rate of tax for provision of processing services to financial institutions | encoded: the rates the section allows (`ita-concessions`); approval and awarded rate inputs |
| s 43L | Concessionary rate of tax for shipping investment manager | encoded: the rates the section allows (`ita-concessions`); approval and awarded rate inputs |
| s 43M | Concessionary rate of tax for trust income to which beneficiary is entitled | input: the concessionary rate the beneficiary's share bears |
| s 43MA | Concessionary rate of tax for estate income received by beneficiary, etc. | input: the concessionary rate the beneficiary's share bears |
| s 43N | Concessionary rate of tax for leasing of aircraft and aircraft engines | encoded: the rates the section allows (`ita-concessions`); approval and awarded rate inputs |
| s 43O | Concessionary rate of tax for aircraft investment manager | encoded: the rates the section allows (`ita-concessions`); approval and awarded rate inputs |
| s 43P | Concessionary rate of tax for container investment enterprise | encoded: the rates the section allows (`ita-concessions`); approval and awarded rate inputs |
| s 43Q | Concessionary rate of tax for container investment manager | encoded: the rates the section allows (`ita-concessions`); approval and awarded rate inputs |
| s 43R | Concessionary rate of tax for approved insurance brokers | encoded: the rates the section allows (`ita-concessions`); approval and awarded rate inputs |
| s 43S | Concessionary rate of tax for income derived from managing qualifying registered business trust or company | encoded: the rates the section allows (`ita-concessions`); approval and awarded rate inputs |
| s 43T | Concessionary rate of tax for ship broking and forward freight agreement trading | encoded: the rates the section allows (`ita-concessions`); approval and awarded rate inputs |
| s 43U | Concessionary rate of tax for shipping-related support services | encoded: the rates the section allows (`ita-concessions`); approval and awarded rate inputs |
| s 43V | Concessionary rate of tax for income derived from managing approved venture company | encoded: the rates the section allows (`ita-concessions`); approval and awarded rate inputs |
| s 43W | Concessionary rate of tax for international growth company | encoded: the rates the section allows (`ita-concessions`); approval and awarded rate inputs |
| s 43X | Concessionary rate of tax for intellectual property income | encoded: the rates the section allows (`ita-concessions`); approval and awarded rate inputs |
| s 44 | (Repealed) | repealed |
| s 44A | (Repealed) | repealed |
| s 45 | Withholding of tax in respect of interest paid to non-resident persons | encoded: (1), (4), (5), (6), (9) (`ita-withholding-credits`) |
| s 45A | Application of section 45 to royalties, management fees, etc. | encoded via s 45 |
| s 45AA | Tax deemed withheld and recoverable from person in breach of condition imposed under section 13(4) | inert: withholding procedure; the rate is s 45's |
| s 45B | Application of section 45 to non-resident director’s remuneration | encoded via s 45 |
| s 45C | Application of section 45 to distribution by unit trust | inert: withholding procedure; the rate is s 45's |
| s 45D | Application of section 45 to gains from real property transaction | encoded via s 45 |
| s 45E | Application of section 45 to withdrawals by non-citizen SRS members, etc. | inert: withholding procedure; the rate is s 45's |
| s 45EA | Approval of deduction of investment from SRS account of non-citizen | inert: withholding procedure; the rate is s 45's |
| s 45F | Application of section 45 to income from profession or vocation carried on by non-resident individual, etc. | encoded via s 45 |
| s 45G | Application of section 45 to distribution from any real estate investment trust | inert: withholding procedure; the rate is s 45's |
| s 45GA | Application of section 45 to income derived as public entertainer | encoded via s 45 |
| s 45H | Application of section 45 to commission or other payment of licensed international market agent | encoded via s 45 |
| s 45I | Sections 45 and 45A not applicable to certain payments | inert: withholding procedure; the rate is s 45's |
| s 45J | Application of section 45, etc., to Government | inert: withholding procedure; the rate is s 45's |
| s 46 | Tax deducted from interests, etc. | encoded (`ita-goal`: tax deducted is a credit) |
| s 47 | (Repealed) | repealed |
| s 48 | (Repealed) | repealed |
| s 49 | Avoidance of double taxation arrangements | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 50 | Tax credits | encoded: (2)-(4) (`ita-withholding-credits`) |
| s 50A | Unilateral tax credits | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 50B | Tax credits for trust income to which beneficiary is entitled | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 50BA | Tax credits for estate income received by beneficiary, etc. | input: the figure the section ascertains (a deduction, allowance, adjusted income or credit) is computed by the caller and enters the goal |
| s 50C | Pooling of credits | encoded (`ita-withholding-credits`) |
| s 51 | Income of wife Trustees, agents and curators | encoded (`ita-withholding-credits`) |
| s 52 | Chargeability of trustees, etc. | encoded (`ita-withholding-credits`) |
| s 53 | Chargeability of agent of person residing out of Singapore | encoded (`ita-withholding-credits`) |
| s 54 | Liability of person chargeable in respect of incapacitated person | inert: a power, a procedure or an information duty |
| s 55 | Liability of managers of companies or bodies of persons | inert: a power, a procedure or an information duty |
| s 56 | Indemnification of representative | inert: a power, a procedure or an information duty |
| s 57 | Power to appoint agent, etc., for recovery of tax | inert: a power, a procedure or an information duty |
| s 58 | Deceased persons | encoded (`ita-withholding-credits`) |
| s 59 | Duty of liquidator on winding up of company or limited liability partnership | inert: a power, a procedure or an information duty |
| s 60 | Chargeability of joint trustees | encoded (`ita-withholding-credits`) |
| s 61 | (Repealed) | repealed |
| s 62 | Notice of chargeability and returns | encoded: (4), (5) (`ita-process`); rest inert |
| s 62A | The basic rule: Singapore dollar to be used | inert: a power, a procedure or an information duty |
| s 62B | Currency other than Singapore dollar to be used in certain circumstances | inert: a power, a procedure or an information duty |
| s 63 | Furnishing of estimate of chargeable income if no return is made under section 62 | encoded: (1), (1A), (1B) (`ita-process`) |
| s 64 | Comptroller may call for further returns | inert: a power, a procedure or an information duty |
| s 65 | Power to call for returns | inert: a power, a procedure or an information duty |
| s 65A | Statement of bank accounts, assets, etc. | inert: a power, a procedure or an information duty |
| s 65B | Power of Comptroller to obtain information | inert: a power, a procedure or an information duty |
| s 65C | Failure to comply with section 64, 65, 65A or 65B | encoded: penalties (`ita-offences`) |
| s 65D | Section 65B notice applies despite duty of secrecy under Banking Act 1970 or Trust Companies Act 2005 | inert: a power, a procedure or an information duty |
| s 65E | Section 65B notice may be subject to confidentiality duty | encoded: penalty (`ita-offences`) |
| s 65F | Arrest of person | inert: a power, a procedure or an information duty |
| s 65G | No unnecessary restraint | inert: a power, a procedure or an information duty |
| s 65H | Arresting officer to be armed | inert: a power, a procedure or an information duty |
| s 65I | Search of place entered by person sought to be arrested | inert: a power, a procedure or an information duty |
| s 65J | Arrested person may be orally examined | encoded: penalty (`ita-offences`) |
| s 65K | Disposal of item furnished or seized | inert: a power, a procedure or an information duty |
| s 66 | Returns to be deemed to be furnished by due authority | inert: a power, a procedure or an information duty |
| s 67 | Keeping of books of account and giving of receipts | encoded: (1) (`ita-process`) |
| s 68 | Official information and secrecy, and returns by employer | inert: a power, a procedure or an information duty |
| s 68A | Duty to collect and retain information of certain persons, etc. | inert: a power, a procedure or an information duty |
| s 69 | Lists to be prepared by representative or agent | inert: a power, a procedure or an information duty |
| s 70 | Occupiers to furnish return of rent payable | inert: a power, a procedure or an information duty |
| s 71 | Return to be made by partnership | inert: a power, a procedure or an information duty |
| s 71A | (Repealed) | repealed |
| s 72 | Comptroller to make assessments | inert: a power, a procedure or an information duty |
| s 73 | Advance assessments | inert: a power, a procedure or an information duty |
| s 74 | Additional assessments | encoded: (1), (2), (2A) (`ita-process`) |
| s 74A | Revised assessments as relief for late GST registration | inert: a power, a procedure or an information duty |
| s 75 | Waiver of small assessments | encoded (`ita-process`) |
| s 76 | Service of notices of assessment and revision of assessment | encoded: (3), (4) (`ita-process`); rest inert |
| s 77 | Errors and defects in assessment and notice | inert: a power, a procedure or an information duty |
| s 78 | Board of Review | inert: a power, a procedure or an information duty |
| s 79 | Right of appeal | encoded: (1), (3) (`ita-process`) |
| s 80 | Hearing and disposal of appeals | inert: a power, a procedure or an information duty |
| s 80A | Hearing of appeal by committee where member becomes unavailable | inert: a power, a procedure or an information duty |
| s 80B | Hearing of appeal by single member where member becomes unavailable | inert: a power, a procedure or an information duty |
| s 81 | Appeals to General Division of High Court | encoded: (1), (2) (`ita-process`) |
| s 82 | Cases stated for General Division of High Court | inert: a power, a procedure or an information duty |
| s 83 | Proceedings before Board | inert: a power, a procedure or an information duty |
| s 84 | Assessments to be final and conclusive | inert: a power, a procedure or an information duty |
| s 85 | Time within which payment is to be made | encoded: (1) (`ita-process`) |
| s 86 | Recovery of tax from persons leaving Singapore | inert: a power, a procedure or an information duty |
| s 87 | Penalty for non-payment of tax and enforcement of payment | encoded (`ita-process`) |
| s 88 | Change of address | inert: a power, a procedure or an information duty |
| s 89 | Suit for tax by Comptroller | inert: a power, a procedure or an information duty |
| s 90 | Statement of Comptroller sufficient | inert: a power, a procedure or an information duty |
| s 91 | Deduction of tax from emoluments and pensions | inert: a power, a procedure or an information duty |
| s 92 | Remission, reduction or refund of tax | inert: a power, a procedure or an information duty |
| s 92A | Remission of tax of companies for year of assessment 2011 | out of period: tied to years of assessment before 2024 (the PIC and earlier schemes) |
| s 92B | Cash grant for companies for year of assessment 2011 | out of period: tied to years of assessment before 2024 (the PIC and earlier schemes) |
| s 92C | Cash grant for companies for year of assessment 2012 | out of period: tied to years of assessment before 2024 (the PIC and earlier schemes) |
| s 92D | Remission of tax of companies for years of assessment 2013, 2014 and 2015 | out of period: tied to years of assessment before 2024 (the PIC and earlier schemes) |
| s 92E | Remission of tax of companies for year of assessment 2016 | out of period: tied to years of assessment before 2024 (the PIC and earlier schemes) |
| s 92F | Remission of tax of companies for year of assessment 2017 | out of period: tied to years of assessment before 2024 (the PIC and earlier schemes) |
| s 92G | Remission of tax of companies for year of assessment 2018 | out of period: tied to years of assessment before 2024 (the PIC and earlier schemes) |
| s 92H | Remission of tax of companies for year of assessment 2019 | out of period: tied to years of assessment before 2024 (the PIC and earlier schemes) |
| s 92I | Remission of tax of companies for year of assessment 2020 | out of period: tied to years of assessment before 2024 (the PIC and earlier schemes) |
| s 92J | Remission of tax for companies for year of assessment 2024 and cash grant for companies | encoded (`ita-rates`) |
| s 92K | Rebate for company for listing shares on stock exchange in Singapore | inert: a power, a procedure or an information duty |
| s 92L | Remission of tax for companies for year of assessment 2025 and cash grant for companies | encoded (`ita-rates`) |
| s 93 | Repayment of tax | encoded: (2) (`ita-process`) |
| s 93AA | Modification of section 93 for repayment of tax for training allowance under Workfare Training Support scheme | inert: a power, a procedure or an information duty |
| s 93A | Relief in respect of error or mistake | encoded: (1), (1A) (`ita-process`) |
| s 93B | Refundable investment credits | inert: a power, a procedure or an information duty |
| s 93C | Recovery of cash grant from companies | inert: a power, a procedure or an information duty |
| s 94 | General penalties | encoded (`ita-offences`) |
| s 94A | Penalty for failure to make return | encoded (`ita-offences`) |
| s 95 | Penalty for incorrect return, etc. | encoded (`ita-offences`) |
| s 96 | Tax evasion and wilful action to obtain PIC bonus | encoded (`ita-offences`) |
| s 96A | Serious fraudulent tax evasion and action to obtain PIC bonus | encoded (`ita-offences`) |
| s 97 | Penalties for offences by authorised and unauthorised persons | encoded (`ita-offences`) |
| s 98 | Penalty for obstructing Comptroller or officers | encoded (`ita-offences`) |
| s 99 | Tax to be payable despite any proceedings for penalties | encoded (`ita-offences`) |
| s 100 | Provisions relating to penalty | inert: a power, a procedure or an information duty |
| s 101 | Consent for prosecution | encoded (`ita-administration`) |
| s 102 | Service of summons | inert: a power, a procedure or an information duty |
| s 102A | Notice to attend court | inert: a power, a procedure or an information duty |
| s 103 | Saving for criminal proceedings | inert: a power, a procedure or an information duty |
| s 104 | Admissibility of certain statements and documents as evidence | inert: a power, a procedure or an information duty |
| s 104A | Protection of informers | inert: a power, a procedure or an information duty |
| s 105 | Jurisdiction of court | encoded (`ita-administration`) |
| s 105A | Interpretation of this Part | inert: a power, a procedure or an information duty |
| s 105B | Purpose of this Part | inert: a power, a procedure or an information duty |
| s 105BA | Exchange of information arrangement | inert: a power, a procedure or an information duty |
| s 105C | (Repealed) | repealed |
| s 105D | Request for information | inert: a power, a procedure or an information duty |
| s 105E | Comptroller to serve notice of request on certain persons | inert: a power, a procedure or an information duty |
| s 105F | Power of Comptroller to obtain information | inert: a power, a procedure or an information duty |
| s 105G | Power of Comptroller to obtain information from other authorities | inert: a power, a procedure or an information duty |
| s 105GA | Information may be used for administration of Act | inert: a power, a procedure or an information duty |
| s 105H | Rules for purposes of this Part | inert: a power, a procedure or an information duty |
| s 105HA | Confidentiality requirements for judicial review proceedings | inert: a power, a procedure or an information duty |
| s 105I | Interpretation of this Part | inert: a power, a procedure or an information duty |
| s 105J | Purpose of this Part | inert: a power, a procedure or an information duty |
| s 105K | International tax compliance agreements | inert: a power, a procedure or an information duty |
| s 105L | Provision of information to Comptroller | inert: a power, a procedure or an information duty |
| s 105M | Offences | encoded: penalties (`ita-offences`) |
| s 105MA | Anti-avoidance | inert: a power, a procedure or an information duty |
| s 105N | Power of Comptroller to obtain information | inert: a power, a procedure or an information duty |
| s 105O | Information may be used for administration of Act | inert: a power, a procedure or an information duty |
| s 105P | Regulations to implement international tax compliance agreements, etc. | inert: a power, a procedure or an information duty |
| s 105PA | Duty to provide information under regulations prevails over duty of secrecy, etc. | inert: a power, a procedure or an information duty |
| s 105Q | Confidentiality requirements for judicial review proceedings | inert: a power, a procedure or an information duty |
| s 105R | Revocation of approval | inert: a power, a procedure or an information duty |
| s 105S | Conditions for application of tax incentive treated as conditions of approval | inert: a power, a procedure or an information duty |
| s 106 | Powers to amend Schedules | inert: a power, a procedure or an information duty |
| s 107 | Variable capital companies or VCCs | inert: a power, a procedure or an information duty |
| s 108 | Advance rulings | encoded: Seventh Schedule fees (`ita-administration`) |

| Schedule | disposition |
|---|---|
| First (exempt bodies) | encoded (`ita-exemptions`) |
| Second (rates) | encoded: all three tables (`ita-rates`) |
| Third (VCC substitutions for ss 13W, 34G-34H, 50-50C) | inert: applied to VCCs under s 107 |
| Fourth (prescribed sections, s 45AA, 105R) | inert |
| Fifth (child relief) | encoded (`ita-reliefs`) |
| Sixth (working life) | encoded (`ita-capital-allowances`) |
| Seventh (advance rulings) | Part 2 fees encoded (`ita-administration`); Part 1 inert |
| Eighth (exchange of information requests) | inert |
| Ninth (specified public schemes) | inert |
| Tenth (Tenth Schedule entities) | inert: an input to ss 13X, 14ZC |
| Eleventh (prescribed information) | inert |
| Twelfth (net tonnage) | encoded (`ita-concessions`) |

No row is deferred.

## 5. Fork register

| fork | text | readings | taken |
|---|---|---|---|
| I1 | the Act is stated by YA; earlier versions of most provisions are not in the text | answer earlier YAs from this text | refuse YAs before 2024; printed YA tables still answer |
| I2 | ss 40B(3), 40C(3): relief limited so that the tax "in respect of such income" is not less than a resident's "in the same circumstances" | what the resident comparison is | the tax at resident rates on chargeable income less the reliefs a resident would have, apportioned to the employment share; compared with 15% on that share |
| I3 | s 39(1)(c)-(d): "at any time ... above 55 ... above 60"; (b) "without affecting" (c), (d) | age band; how (b) combines | the band reached by 31 December of the preceding year; (b) added to (c) or (d) |
| I4 | s 39(2)(h), (ha): "37% ... or such other rate as may be prescribed", "$37,740 ... or such other amount" | prescribed alternatives | the printed figures |
| I5 | s 10(2)(cb)(i): the employer's rent, without "less any rent paid by the employee" (which (ii) has) | deduct the employee's rent under (i) too | not deducted under (i), as printed |
| I6 | s 45(4)(b): 1% per completed month "within 30 days after the time specified" | when months start | counted from 30 days after the due date |
| I7 | s 87(1)(c): 5% then 1% per completed month after 60 days | when the 5% is imposed | the day after the last day to pay; months from 60 days after; amount constant |
| I8 | s 62(4): notice "within 14 days after the end of" 3 months from the start of the YA | the end of the period | 31 March; so 14 April |
| I9 | Fifth Schedule para 5(1AB) "if Y is the eligible child" | the first child | read as the first eligible child ($8,000) |

## 6. Answer tables

**Resident individuals, YA 2024 on** (Second Schedule Table 3): first $20,000 nil; next $10,000 2%; $10,000 3.5%; $40,000 7%; $40,000 11.5%; $40,000 15%; $40,000 18%; $40,000 19%; $40,000 19.5%; $40,000 20%; $180,000 22%; $500,000 23%; above $1,000,000 24%. Tax at $80,000: $3,350; $120,000: $7,950; $320,000: $44,550; $1,000,000: $199,150.

**Companies**: 17% (s 43(1)(a)). YA 2020 on: 75% of the first $10,000 and 50% of the next $190,000 exempt (s 43(6B)); a qualifying start-up in its first 3 YAs: 75% of the first $100,000 and 50% of the next $100,000 (s 43(6D)(b)). Remission YA 2024 and YA 2025: lower of 50% of tax less the $2,000 grant and $40,000 less the grant (ss 92J, 92L).

**Non-residents**: individuals 24% (YA 2024 on); employment income at 15% or the resident amount, whichever is more (s 40B); interest 15%, royalties 10% on the gross (s 43(3), (3A)); withholding 24% / 17% / 15% / 10% (s 45).

**Penalties**: late payment 5% + 1% a month to 12% (s 87); late withholding 5% + 1% a month to 15% (s 45(4)); incorrect return 1x / 2x / 3x / 4x the tax undercharged by culpability (ss 95, 96, 96A); failure to file 2 years or more: 2x the tax assessed (s 94A(3)).

## 7. Known limits

- The deductions and allowances under the approval-based sections of Parts 5 and 6, and the Part 7 adjustments, are computed by the caller and enter the goal as figures; the encoding does not test their conditions.
- `the income tax position for` takes one figure for all capital allowances and gives no s 37B group relief or s 37D carry-back inside the goal: those are separate rules.
- The trustee rate (s 43(2)) and the REIT and unit trust regimes are inputs.
- Concessionary rates: the approval date is not an input, so a rate allowed only for approvals from 17 February 2024 (s 43I 15%, s 43E, s 43N, the s 43X 15% base) is accepted at any date.
- s 40A(2A): the 10% rate for a public entertainer's income derived from 22 February 2010 to 31 March 2022 is outside the encoded period and not applied.
- Not encoded: s 19(3) ($35,000 base for a car's allowances), s 50C(2)(b) (the 15% headline-rate condition is the caller's), s 93A(5) ($250 deposit), s 33A(4) (one month to pay the surcharge); s 40B(1)'s SRS exclusion, the 7% capital-sum cap on premiums and s 13W's 20% holding are the caller's facts.
- In the top-level goal an exempt item is exempt in full; the partial s 13(1)(jd) exemption is the separate rule.

## 8. The independent test pass

A fresh session wrote its expectations from the brief and the source before opening any module (`independent-expectations.md`), then `tests-independent.l4` (320 assertions). First run: **316 satisfied, 2 failed, 2 refused where an answer was expected**: four findings, all **encoding errors**, all fixed:

- **s 10L(2)(b)** — gains that would otherwise be exempt are caught; the encoding had one input for "chargeable or exempt" and excluded both.
- **s 13(1)(jd)** — the exemption reaches the first $2,730 of a larger contribution.
- **s 43X(5)** — the rate is a base of 5%, 10% or 15% plus any increases; only 5% had been allowed.

The independent tests needed two plumbing edits (a split field, a mislabelled constructor renamed); no expected value changed. s 27(4) and (6), which the pass listed as not expressible, were added. See `INDEPENDENT-TEST-REPORT.md`.

## 9. Checks

`L4=~/.local/bin/l4 ./check.sh`, 2026-10-06: **19 modules, 0 errors, 721 assertions satisfied, 0 failed** (401 encoder, 320 independent). No assertion is expected to fail.

## 10. Open questions for a domain expert

1. I2: how IRAS computes "the tax ... payable by a resident of Singapore in the same circumstances" for a non-resident employee with other income.
2. I3: the age band for an individual whose 55th or 60th birthday falls during the preceding year.
3. I5: whether the employee's rent is deducted from the employer-paid rent under s 10(2)(cb)(i).
4. The prescribed figures the encoding takes as inputs (SRS caps, CPF top-up limits, withholding substitutions under s 45(1C)).
