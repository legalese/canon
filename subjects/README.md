# subjects/

One directory per body of law. **Nineteen subjects are listed as at 2026-09-26**; the first sixteen are described in this paragraph, and the last three, which arrived with the bulk ingestion, below it. Ten are enacted
law, or announced as law: four Singapore subjects, three pieces of Israeli legislation, one
US federal regulation, one Act of the UK Parliament and one Law of Jersey. Of the other six, one is a synthetic insurance
policy, two are commercial standard forms, one is eight private issuers' card T&Cs bundled as
one comparison subject, one is a judge-made doctrine encoded across four jurisdictions, and one
is a body of Israeli **collective agreements** rather than enacted law at all. Each of those six
is flagged below. One subject, `contracts/investment/yc-safe-premoney`, holds source text and no
encoding at all, which the `what it encodes` column says plainly.

| subject | what it encodes | status |
| --- | --- | --- |
| [`sg/succession`](sg/succession) | Wills Act 1838, Intestate Succession Act 1967, Probate and Administration Act 1934 — three Acts against one ontology | `draft` |
| [`sg/child-support`](sg/child-support) | the SG Child Support Package announced at the National Day Rally on 23 August 2026, and childcare leave under the Child Development Co-Savings Act 2001 | `draft` |
| [`sg/pdpa-2012`](sg/pdpa-2012) | Personal Data Protection Act 2012, Part VIA (data breach notification) | `draft` |
| [`sg/penal-code-1871`](sg/penal-code-1871) | Penal Code 1871 — cheating, theft, extortion, robbery, criminal breach of trust, criminal intimidation, hurt (ss 22–25, 321, 323A, 378–384, 390–394, 405–406, 415–420, 503–506) with the form of a charge under CPC 2010 ss 123–126, and s 301 (transferred malice) | `draft` |
| [`us/chubb-hospital-cash`](us/chubb-hospital-cash) | a **synthetic** supplemental hospitalization cash policy — never law, never in force — encoded twice, independently, as evidence in a replication study | `experimental` |
| [`us/regcf`](us/regcf) | SEC Regulation Crowdfunding, 17 CFR Part 227, encoded twice and independently: the eight requirement groups one wiki page presents, with a rule-version axis back to commencement in 2016, and all 22 sections de novo from the eCFR | `draft` |
| [`uk/bna-1981`](uk/bna-1981) | British Nationality Act 1981, section 1 — British citizenship by birth or adoption in the United Kingdom, as in force on 4 July 2026; the demo pipeline's smoke-test subject, "as is traditional" (Sergot et al., 1986) | `draft` |
| [`je/charities-2014`](je/charities-2014) | Charities (Jersey) Law 2014 — the charity test (Articles 5-7, with the definitions it needs), encoded de novo as a cleanroom smoke test, with its DMN/BPMN projections and a three-way comparison against an earlier encoding of the whole Law | `draft` |
| [`contracts/investment/yc-safe-postmoney`](contracts/investment/yc-safe-postmoney) | the Y Combinator post-money SAFE — six instruments plus four Pro Rata Side Letters, with their User Guide — deposited verbatim, with one encoding row | `draft` |
| [`contracts/investment/yc-safe-premoney`](contracts/investment/yc-safe-premoney) | nothing, and none planned in this repository — **sources only**: the 2013–2018 "original safe", four US variants, recovered from the Internet Archive | `draft` |
| [`contracts/payments/sg-miles-card`](contracts/payments/sg-miles-card) | eight Singapore card issuers' reward-programme T&Cs — DBS yuu, DBS Woman's World, Citi Rewards, HSBC Revolution, UOB Lady's Solitaire, POSB PAssion, plus two flat-rate cards with no held T&C — against one shared ontology, so "which card earns the most on this purchase" can be asked across all eight at once | `draft` |
| [`il/ofek-hadash-2008`](il/ofek-hadash-2008) | the Ofek Hadash reform — the collective agreements, and one budget-law chapter, that determine an Israeli teacher's pay | `draft` |
| [`il/hvac-work-licensing-2025`](il/hvac-work-licensing-2025) | the Refrigeration or Air-Conditioning Systems Work Licensing Law 5785-2025 (licence grades, eligibility with the Second Schedule, validity, foreign experts, commencement) and its Fees Regulations in THREE vintages — the SimpLEX draft shown in Schwartz, Bar-Siman-Tov & Gelbard (2025), as made, as amended — with the paper's own test table run against all three | `draft` |
| [`il/income-tax-ordinance-new-version`](il/income-tax-ordinance-new-version) | Income Tax Ordinance [New Version] — three rows, one per slice, each against its own nouns: `legalese-2026-10-il-01` (credit points, ss 33A, 34, 36, 36A), `legalese-2026-10-il-02` (s 66, separate calculation for spouses) and `legalese-2026-10-il-03` (ss 120B indexation, 121 individual rates, 121B additional tax); the rest of the Ordinance is not encoded, and the three slices' nouns are not yet reconciled | `draft` |
| [`il/national-insurance-law-consolidated-version-5755-1995`](il/national-insurance-law-consolidated-version-5755-1995) | National Insurance Law [Consolidated Version], 5755-1995 — three rows, one per slice: `legalese-2026-10-il-04` (s 1 definitions, s 334, Schedule J contribution rates, s 337; v0.2.0, repaired against the enacted amending Laws), `legalese-2026-10-il-05` (Schedule K income bounds, s 342 who pays and the employer's deduction, s 348 maximum and minimum) and `legalese-2026-10-il-06` (ss 65 to 68, the child allowance); the rest of the Law is not encoded, the enacted amending Laws are deposited beside the Hebrew text, and each row declares findings about the source's own inconsistencies as expected failures | `draft` |
| [`il/employed-parent-monthly-net`](il/employed-parent-monthly-net) | a **composed** subject, not a statute: one row, `legalese-2026-10-il-07`, that composes the six income-tax and national-insurance rows above into the monthly net income of an employed resident parent with children in a month of 2026, through adapters because this `l4` cannot import across directories; every provision no row encodes is a named input or a named refusal, listed in its GAPS.md | `draft` |
| [`il/penal-law-1977`](il/penal-law-1977) | Penal Law 5737-1977 — theft and robbery (ss 383, 384, 402, 403, 404), encoded in Hebrew with English renderings beside every rule | `draft` |
| [`il/traffic-ordinance-bac`](il/traffic-ordinance-bac) | Traffic Ordinance [New Version] 5721-1961, s 64B(a) "intoxicated" — the drink-driving alcohol thresholds, with reg. 169A of the Traffic Regulations — on the rule-effective axis either side of the 2010 amendment that lowered the threshold for new, young and professional drivers | `draft` |
| [`doctrine/contract/unilateral-mistake`](doctrine/contract/unilateral-mistake) | the Singapore doctrine of unilateral mistake in contract — *Chwee Kin Keong v Digilandmall.com* [2005] SGCA 2 — encoded beside three comparators (English common law, *Taylor v Johnson*, Restatement (Second) § 153) against one ontology | `draft` |
| [`comparative/ai-content-labelling`](comparative/ai-content-labelling) | AI-content labelling across three authorities — EU AI Act Art. 50(2) and (4) with the Code of Practice's Measure 1.1, Washington E2SHB 1170 (2026), California Bus. & Prof. Code 22757 as amended by SB 1000 (2026) — encoded against one domain module, run over real and test-signed C2PA files, with a census of where the three disagree; first row under a **proposed** `comparative/` grammar (see its README) | `draft` |
| [`eu/FinMont-demo`](eu/FinMont-demo) | PSD2 strong customer authentication (Commission Delegated Regulation (EU) 2018/389) and refunds and liability under Directive (EU) 2015/2366, orchestrated for one firm — row `legalese-aswathy` | `draft` |
| [`nz/online-safety-minimum-age-bill-2026`](nz/online-safety-minimum-age-bill-2026) | the Online Safety (Minimum Age and Child Safety Risk Assessment) Bill — row `legalese-michael` | `draft` |
| [`au/wa/residential-tenancies-act`](au/wa/residential-tenancies-act) | Residential Tenancies Act 1987 (Western Australia) — row `legalese-michael` | `draft` |
| [`au/wa/cat-act-2011`](au/wa/cat-act-2011) | Cat Act 2011 (Western Australia) and Cat Regulations 2012 — row `legalese-michael`: Part 1, Part 2 Divs 1–3, regs 9, 10, 12 and s 79 in two versions; row `legalese-aswathy`: the whole Act (ss 1–88) and the whole Regulations (regs 1–30, Schedules 1–3), as in force from 25 September 2025, an independent reading with a 16-entry fork register | `draft` |
| [`sg/consumer-protection-fair-trading-act-2003`](sg/consumer-protection-fair-trading-act-2003) | Consumer Protection (Fair Trading) Act 2003 — the whole Act (ss 1–44, First, Second, Fourth and Fifth Schedules), every delegation to regulations a named refusal — row `legalese-aswathy` | `draft` |
| [`sg/business-name-registration-act-2014`](sg/business-name-registration-act-2014) | Business Names Registration Act 2014 — the whole Act (ss 1–45), notice duties as regulative rules, every delegation to regulations an input fact or a named refusal — row `legalese-aswathy` | `draft` |
| [`sg/carriage-by-air-act-1988`](sg/carriage-by-air-act-1988) | Carriage by Air Act 1988 (ss 1–13) and the three texts of the Warsaw Convention in its Schedules — the original, as amended by the Hague Protocol, and as further amended by Montreal Protocol No. 4 — each its own answer, the limits in francs and SDRs, the conversion a named refusal — row `legalese-aswathy` | `draft` |
| [`sg/criminal-procedure-code-2010`](sg/criminal-procedure-code-2010) | Criminal Procedure Code 2010 — the First Schedule (tabular statement of offences under the Penal Code 1871: 478 rows plus the four other-law bands, each with arrest, warrant or summons, bail, court) with ss 2(1) and 7 to 9, and the Second Schedule (laws to which criminal case disclosure procedures apply) with ss 159 and 211A; and the treatment of an offence under the Prevention of Corruption Act 1960 and the Misuse of Drugs Act 1973, read with what each Act says about its own offences (a statement carried in an interface module shared by the three subjects); the rest of the Code and Schedules 3 to 7 are not encoded — row `legalese-aswathy` | `draft` |
| [`sg/evidence-act-1893`](sg/evidence-act-1893) | Evidence Act 1893 — Parts 1 to 4 and both Schedules organised by evidentiary question (relevancy, hearsay, documents, presumptions and burden, witnesses and privilege, examination), ss 117 to 119 not encoded, with an interface module shared with the Criminal Procedure Code subject — row `legalese-aswathy` | `draft` |
| [`sg/prevention-of-corruption-act-1960`](sg/prevention-of-corruption-act-1960) | Prevention of Corruption Act 1960 — Parts 1, 3, 4, 5, 6 and ss 3 and 4: the offences, the s 8 presumption and s 9 deeming, the penalty rules, the powers of arrest, investigation and search, the evidence rules, and a statement to the Criminal Procedure Code subject (ss 32(1), 34); ss 4A to 4F (CPIB superannuation) not encoded — row `legalese-aswathy` | `draft` |
| [`sg/misuse-of-drugs-act-1973`](sg/misuse-of-drugs-act-1973) | Misuse of Drugs Act 1973 — the offences (controlled drugs and psychoactive substances), the presumptions and certificates, the powers of search, arrest and specimen, forfeiture, jurisdiction, and every punishment (the Second Schedule's table in full, 86 rows, with ss 33, 33A, 33B); the substance lists of the First, Third and Fifth Schedules and ss 34 to 52 are not encoded — row `legalese-aswathy` | `draft` |
| [`sg/apportionment-act-1928`](sg/apportionment-act-1928) | Apportionment Act 1928 — the whole Act (ss 1–7): what is apportionable, the day-by-day accrued part, when it is payable and how it is recovered | `draft` |
| [`sg/metrication-act-1970`](sg/metrication-act-1970) | Metrication Act 1970 — the whole Act (ss 1–7) and all four Schedules: SI membership, every unit row, every Third Schedule conversion, the s 7 saving | `draft` |
| [`sg/notaries-public-act-1959`](sg/notaries-public-act-1959) | Notaries Public Act 1959 — the whole Act (ss 1–8): appointment and temporary appointment, when an appointment has effect, oath powers under s 4, revocation, the s 7 offence, rules; refuses before 1 June 2007 | `draft` |
| [`sg/work-injury-compensation-act-2019`](sg/work-injury-compensation-act-2019) | Work Injury Compensation Act 2019 — the whole Act (ss 1–83 with Part 3A, ss 34A–34P, platform workers) and the First to Sixth Schedules, as eight goal-level conclusions: coverage, liability (accidents, platform operators' shares, principals, disease), amount, payment, the claim process, damages, insurance, offences; refuses accidents before 1 January 2025; beside the `naive-2026-10` row (s 7 and First Schedule paras 1–3) | `draft` |
| [`sg/carbon-pricing-act-2018`](sg/carbon-pricing-act-2018) | Carbon Pricing Act 2018 — the whole Act (ss 1–79, First to Fifth Schedules) under one top-level goal (what a facility's operator must do and owe for an emissions year) and seven goals: registration, reporting, the carbon tax, payment and credits, assessments and appeals, records, offences; refuses years before 2024 | `draft` |
| [`sg/income-tax-act-1947`](sg/income-tax-act-1947) | Income Tax Act 1947 — every section given a disposition, under one top-level goal (how much income tax a person owes for a year of assessment, and by when) and ten goals: residence, the charge, exemptions, deductions and allowances, statutory to chargeable income and reliefs, rates, rebates and credits, withholding, filing and disputes, payment, offences; approval-based incentives take the approval as input; YA 2024 onwards | `draft` |
| [`sg/computer-misuse-act-1993`](sg/computer-misuse-act-1993) | Computer Misuse Act 1993 — the whole Act (ss 1–20, both Schedules) under one top-level goal (is the conduct reached, is the offence made out, the most it can cost) and four goals: definitions, offences, punishment, reach and procedure; refuses conduct before 30 December 2025 | `draft` |
| [`sg/child-development-co-savings-act-2001`](sg/child-development-co-savings-act-2001) | Child Development Co-Savings Act 2001 — the whole Act (Parts 1–4, First and Second Schedules) under one top-level goal (what paid leave or Government payment a parent gets for a child, capped how, and what the employer claims back) and eight goals: common measures, the Co-Savings Scheme, maternity, adoption, fathers, shared parental leave, childcare leave, recovery and offences | `draft` |
| [`sg/insurance-act-1966`](sg/insurance-act-1966) | Insurance Act 1966 — the whole Act under two top-level goals: a regulated person (does the Act reach and permit the activity; the offence and its maximum penalty, every penalty in the Act tabled) and a policy (Singapore or offshore, class, validity and recoverable amount, the owner's rights, nominations and who is paid without probate); supervision, appeals, transfers and the s 123 winding-up priority as a fifth goal | `draft` |
| [`vn/decree-67-2023`](vn/decree-67-2023) | Decree 67/2023/NĐ-CP on compulsory motor vehicle owners' civil liability insurance, compulsory fire and explosion insurance, and compulsory insurance in construction investment — encoded in L4 with the Vietnamese quoted line by line from the source (VN-10: the compulsory motor insurance, Articles 5-13, with Annexes I and VI; VN-27: the Motor Vehicle Insurance Fund, Articles 14-22, and the insurer's duties, Article 75); a draft that no Vietnamese-qualified reader has checked, with a fork register and findings in its `NOTES.md` | `draft` |
| [`vn/road-traffic-order-safety-law-36-2024`](vn/road-traffic-order-safety-law-36-2024) | Law 36/2024/QH15 on Road Traffic Order and Safety, from 1 January 2025 — the parts that bear on motor insurance (driving licence classes and validity, alcohol and drugs, vehicle registration and service life), encoded in L4 with the Vietnamese quoted line by line from the source (VN-28); a draft that no Vietnamese-qualified reader has checked, with a fork register and findings in its `NOTES.md` | `draft` |
| [`contracts/insurance/vn-aia-an-phuc-tron-doi-uu-viet`](contracts/insurance/vn-aia-an-phuc-tron-doi-uu-viet) | AIA An Phúc Trọn Đời Ưu Việt whole life product rules and terms (V082021, with three amending MoF letters) — encoded in L4 with the Vietnamese quoted line by line from the source (VN-25); a draft that no Vietnamese-qualified reader has checked, with a fork register and findings in its `NOTES.md` | `draft` |
| [`contracts/insurance/vn-aia-khoe-tron-ven`](contracts/insurance/vn-aia-khoe-tron-ven) | AIA Khỏe Trọn Vẹn product rules and terms (MoF letter 14632/BTC-QLBH, 23 December 2021) — encoded in L4 with the Vietnamese quoted line by line from the source (VN-24); a draft that no Vietnamese-qualified reader has checked, with a fork register and findings in its `NOTES.md` | `draft` |
| [`contracts/insurance/vn-baominh-construction-all-risks`](contracts/insurance/vn-baominh-construction-all-risks) | Bảo Minh construction all risks insurance rules (Quy tắc bảo hiểm mọi rủi ro xây dựng) — encoded in L4 with the Vietnamese quoted line by line from the source (VN-22); a draft that no Vietnamese-qualified reader has checked, with a fork register and findings in its `NOTES.md` | `draft` |
| [`contracts/insurance/vn-baominh-fire-special-perils`](contracts/insurance/vn-baominh-fire-special-perils) | Bảo Minh fire and special perils insurance rules (Quy tắc bảo hiểm hỏa hoạn và các rủi ro đặc biệt) — encoded in L4 with the Vietnamese quoted line by line from the source (VN-20); a draft that no Vietnamese-qualified reader has checked, with a fork register and findings in its `NOTES.md` | `draft` |
| [`contracts/insurance/vn-baominh-installation-all-risks`](contracts/insurance/vn-baominh-installation-all-risks) | Bảo Minh installation all risks insurance rules (Quy tắc bảo hiểm mọi rủi ro lắp đặt) — encoded in L4 with the Vietnamese quoted line by line from the source (VN-21); a draft that no Vietnamese-qualified reader has checked, with a fork register and findings in its `NOTES.md` | `draft` |
| [`contracts/insurance/vn-baominh-property-all-risks`](contracts/insurance/vn-baominh-property-all-risks) | Bảo Minh property all risks insurance rules (Quy tắc bảo hiểm mọi rủi ro cho tài sản) — encoded in L4 with the Vietnamese quoted line by line from the source (VN-08); a draft that no Vietnamese-qualified reader has checked, with a fork register and findings in its `NOTES.md` | `draft` |
| [`contracts/insurance/vn-baoviet-motor-physical-damage-2021`](contracts/insurance/vn-baoviet-motor-physical-damage-2021) | Bảo Việt motor vehicle physical damage insurance rules (Decision 5688/QĐ-BHBV, 9 December 2021) — encoded in L4 with the Vietnamese quoted line by line from the source (VN-01); a draft that no Vietnamese-qualified reader has checked, with a fork register and findings in its `NOTES.md` | `draft` |
| [`contracts/insurance/vn-liberty-homecare`](contracts/insurance/vn-liberty-homecare) | Liberty HomeCare home insurance rules (Quy tắc bảo hiểm nhà cửa, UW-RPP-W-001-06-V) — encoded in L4 with the Vietnamese quoted line by line from the source (VN-05); a draft that no Vietnamese-qualified reader has checked, with a fork register and findings in its `NOTES.md` | `draft` |
| [`contracts/insurance/vn-liberty-personal-accident`](contracts/insurance/vn-liberty-personal-accident) | Liberty personal accident insurance rules (Quy tắc bảo hiểm tai nạn con người, UW-PAG-W-001-10-V) — encoded in L4 with the Vietnamese quoted line by line from the source (VN-23); a draft that no Vietnamese-qualified reader has checked, with a fork register and findings in its `NOTES.md` | `draft` |
| [`contracts/insurance/vn-manulife-endowment-critical-illness`](contracts/insurance/vn-manulife-endowment-critical-illness) | Manulife endowment insurance with critical illness benefit, three-stage extended payout (Cuộc Sống Tươi Đẹp; MoF letter 1997/BTC-QLBH, 20 February 2019) — encoded in L4 with the Vietnamese quoted line by line from the source (VN-12); a draft that no Vietnamese-qualified reader has checked, with a fork register and findings in its `NOTES.md` | `draft` |
| [`contracts/insurance/vn-manulife-group-linked-flexible-premium`](contracts/insurance/vn-manulife-group-linked-flexible-premium) | Manulife group universal-linked insurance, flexible premium (MoF letter 14548/BTC-QLBH, 27 October 2017) — encoded in L4 with the Vietnamese quoted line by line from the source (VN-14); a draft that no Vietnamese-qualified reader has checked, with a fork register and findings in its `NOTES.md` | `draft` |
| [`contracts/insurance/vn-manulife-term-life`](contracts/insurance/vn-manulife-term-life) | Manulife term life insurance product terms (Điều khoản sản phẩm bảo hiểm tử kỳ có thời hạn) — encoded in L4 with the Vietnamese quoted line by line from the source (VN-11); a draft that no Vietnamese-qualified reader has checked, with a fork register and findings in its `NOTES.md` | `draft` |
| [`contracts/insurance/vn-manulife-unit-linked-regular-premium`](contracts/insurance/vn-manulife-unit-linked-regular-premium) | Manulife unit-linked life insurance, regular premium (Maxx Phúc Lộc Thịnh Vượng; MoF letter 5485/BTC-BH, 13 May 2008) — encoded in L4 with the Vietnamese quoted line by line from the source (VN-13); a draft that no Vietnamese-qualified reader has checked, with a fork register and findings in its `NOTES.md` | `draft` |
| [`contracts/insurance/vn-msig-general-liability-2015`](contracts/insurance/vn-msig-general-liability-2015) | MSIG Vietnam general liability insurance policy (Revised CGL Policy Form, 12 January 2015) — encoded in L4 with the Vietnamese quoted line by line from the source (VN-09); a draft that no Vietnamese-qualified reader has checked, with a fork register and findings in its `NOTES.md` | `draft` |
| [`contracts/insurance/vn-opes-ocar-motor-physical-damage`](contracts/insurance/vn-opes-ocar-motor-physical-damage) | OPES O-Car motor vehicle physical damage insurance product rules (Decision 124/2019/QĐ-TGĐ, amended by supplementary clauses under Decision 17/2022/QĐ-TGĐ) — encoded in L4 with the Vietnamese quoted line by line from the source (VN-15); a draft that no Vietnamese-qualified reader has checked, with a fork register and findings in its `NOTES.md` | `draft` |
| [`contracts/insurance/vn-pacific-cross-travel-2023`](contracts/insurance/vn-pacific-cross-travel-2023) | Pacific Cross Vietnam travel insurance policy wording (English and Vietnamese) — encoded in L4 with the Vietnamese quoted line by line from the source (VN-06); a draft that no Vietnamese-qualified reader has checked, with a fork register and findings in its `NOTES.md` | `draft` |
| [`contracts/insurance/vn-prudential-term-life-pa-notes`](contracts/insurance/vn-prudential-term-life-pa-notes) | Prudential term insurance with personal accident benefit: two pages of notes followed by the full rules and terms (one PDF) — encoded in L4 with the Vietnamese quoted line by line from the source (VN-26); a draft that no Vietnamese-qualified reader has checked, with a fork register and findings in its `NOTES.md` | `draft` |
| [`contracts/insurance/vn-pti-phuc-an-sinh-health`](contracts/insurance/vn-pti-phuc-an-sinh-health) | PTI Phúc An Sinh health care insurance rules (Decision 267/QĐ-PTI-BHCN, 26 September 2012) — encoded in L4 with the Vietnamese quoted line by line from the source (VN-03); a draft that no Vietnamese-qualified reader has checked, with a fork register and findings in its `NOTES.md` | `draft` |
| [`contracts/insurance/vn-pti-comprehensive-health-gras-savoye`](contracts/insurance/vn-pti-comprehensive-health-gras-savoye) | PTI comprehensive health care insurance through Gras Savoye (Decision 268/QĐ-PTI-BHCN, 26 September 2012) — encoded in L4 with the Vietnamese quoted line by line from the source (VN-16); a draft that no Vietnamese-qualified reader has checked, with a fork register and findings in its `NOTES.md` | `draft` |
| [`contracts/insurance/vn-pvi-comprehensive-health-care`](contracts/insurance/vn-pvi-comprehensive-health-care) | PVI comprehensive health care insurance rules (Quy tắc bảo hiểm chăm sóc sức khỏe toàn diện) — encoded in L4 with the Vietnamese quoted line by line from the source (VN-04); a draft that no Vietnamese-qualified reader has checked, with a fork register and findings in its `NOTES.md` | `draft` |
| [`contracts/insurance/vn-tasco-combined-health`](contracts/insurance/vn-tasco-combined-health) | Tasco Insurance combined health insurance rules, with the guarantee-hospital and excluded-facility lists — encoded in L4 with the Vietnamese quoted line by line from the source (VN-19); a draft that no Vietnamese-qualified reader has checked, with a fork register and findings in its `NOTES.md` | `draft` |
| [`contracts/insurance/vn-tasco-combined-motor-2024`](contracts/insurance/vn-tasco-combined-motor-2024) | Tasco Insurance combined motor vehicle insurance rules (Decision 53/2024/QĐ-BH Tasco, 22 May 2024) — encoded in L4 with the Vietnamese quoted line by line from the source (VN-18); a draft that no Vietnamese-qualified reader has checked, with a fork register and findings in its `NOTES.md` | `draft` |
| [`contracts/insurance/vn-tasco-voluntary-motor-2024`](contracts/insurance/vn-tasco-voluntary-motor-2024) | Tasco Insurance voluntary motor vehicle insurance rules (Decision 168/2024/QĐ-BH Tasco) — encoded in L4 with the Vietnamese quoted line by line from the source (VN-17); a draft that no Vietnamese-qualified reader has checked, with a fork register and findings in its `NOTES.md` | `draft` |
| [`contracts/insurance/vn-uic-autojoy-motor-2018`](contracts/insurance/vn-uic-autojoy-motor-2018) | UIC AutoJoy voluntary motor vehicle insurance rules (Decision 271/2018/UIC-QĐ, 18 December 2018) — encoded in L4 with the Vietnamese quoted line by line from the source (VN-02); a draft that no Vietnamese-qualified reader has checked, with a fork register and findings in its `NOTES.md` | `draft` |
| [`contracts/insurance/vn-uic-property-all-risks`](contracts/insurance/vn-uic-property-all-risks) | UIC property all risks insurance rules (Quy tắc bảo hiểm mọi rủi ro tài sản) — encoded in L4 with the Vietnamese quoted line by line from the source (VN-07); a draft that no Vietnamese-qualified reader has checked, with a fork register and findings in its `NOTES.md` | `draft` |

Two subjects above carry a second, independent row from the bulk ingestion: `sg/penal-code-1871/encodings/legalese-aswathy/` (the whole Code, Chapters 1–23) beside the `legalese` row, and `il/hvac-work-licensing-2025/encodings/legalese-michael/` (the whole Law, in Hebrew-commented English L4) beside `legalese` and `legalese-he`. Rows are equal; neither is primary.
`sg/penal-code-1871` also has a third row, `encodings/legalese-whole-code/` (2026-09-26): the whole Code again, made in one run of nine agents to the charge generator's contract, with 443 sections encoded and 42 deferred for time.

`sg/child-support` is the odd one and worth knowing about before you read it: its primary
source is an **announcement, not an enactment**. No Bill has been introduced, so its
rule-version axis carries *administered today* against *announced*, and the statute the
announcement would amend is recorded as the source bundle's `instrument`.

`sg/penal-code-1871` grew on 2026-09-17 from one section to ten modules, encoded in inert style
for the charge-generator demo, with a seven-case bench of reported judgments asserted inside the
modules rather than a `cases/` directory; it gained section 393 and a `projections/` directory on
2026-09-21, and still has no `registers/`, `report/` or `gates/`. The projections are the
repository's **first generated ladder figures** — six robbery decisions read out of the module
through `jl4-lsp` in four carriers each, one of them prose, so the section's elements can be laid
beside a textbook's list without anyone transcribing them. It is filed as a
subject rather than an l4-ide example because it is a body of law, and this is where bodies
of law live; its `NOTES.md` states what the sidecar does not carry. It is also the row whose
**source terms bite hardest**: inert style works by quoting the statute inline, so unlike
`sg/pdpa-2012` it reproduces its section verbatim rather than paraphrasing it. See that
row's `SOURCE-LICENSE.md`.

`us/chubb-hospital-cash` is the row that most needs its label read. It is the first `experimental`
row, and the status is not a weaker `draft` — it marks a different kind of thing. **The instrument is
synthetic: fictional parties, never issued, never in force, never construed.** It was invented by
researchers as a benchmarking target, and it is filed here because it is a body of contractual rules
that has been encoded, not because anyone is subject to it. It is also the first row whose source
terms are **determined** rather than undetermined — the policy originates in a CC BY 4.0 article, so
attribution is required and is recorded in `NOTICE`. Two independent encodings sit side by side under
`encodings/`, written blind to each other and to the benchmark's answer key, because the comparison
between them is the evidence. Read its `NOTES.md` before drawing any conclusion from it: the source
text was modified before publication in a way that removed the operative insuring clause.

`doctrine/contract/unilateral-mistake` is the first row under a **third grammar**, and the first
whose subject is **judge-made law**. Everything else here is a text somebody enacted or drafted;
this is a rule that exists only as a line of holdings, and the encoding's point is comparative —
Singapore's equitable limb requires constructive knowledge **plus** an additional element of
impropriety, and that formula is visible as distinctive only when England's, Australia's and the
American rule are computed on the same facts beside it. Filing it under `sg/` would have made
three of its four modules trespassers; filing four sibling subjects would have left the comparison
homeless. So it seeds `doctrine/<area>/<leaf>/`, with a controlled area vocabulary in
[`doctrine/AREAS.md`](doctrine/AREAS.md) on the model of `contracts/GENRES.md`. **That grammar is a
proposal, not a ruling** — `docs/directory-conventions.md` §12 owns the rewrite and this row has
not amended it; the argument is set out in the row's `NOTES.md` §1 so a reviewer can disagree with
it rather than reconstruct it.

Two things about that row need reading before it is relied on. Its **comparators are read at second
hand**: the English and Australian authorities were never fetched from their own reports, only from
*Chwee Kin Keong*'s account of them, and the American column states the Restatement rule rather than
the law of any State. And it is the first row whose registers had to be **bent to fit** — a judgment
has no in-force banner and no amendment markers, so the source bundle declares no annotations and
the sweep register has nothing to dispose of; both say so in their own notes, and both record the
schema vocabulary gaps as upstream candidates rather than papering over them.

`contracts/payments/sg-miles-card` is the first subject under a **new genre**, `payments/`,
seeded in the same change (`contracts/GENRES.md` records why). It is also the first `contracts/`
row that is a **bundle**: eight instruments by five different issuers, filed as one leaf against
one shared domain module and composer, because the point of the encoding is a comparison across
all eight (Meng ruled this shape on 2026-09-21, the day it was deposited) — the same reason
`sg/succession` bundles four Acts and `il/ofek-hadash-2008` bundles several collective agreements.
Its `subject.json.encodings_note` and its row's `NOTES.md` §0 both state the argument in full.
**HG1 was waived, not signed** — `status: draft` is not a weaker claim about the encoding's
correctness than usual; it specifically reflects that nobody has checked its isomorphism to the
eight source texts yet, notwithstanding that every machine gate (848 scenario assertions, a
Catala projection with zero refusals) passed. See `encodings/legalese/gates/HG1.waiver.md`.

The two `contracts/` rows are the first entries under a **second grammar**. Everything above them
is enacted law, filed by the authority that enacted it — `sg/`, `us/`, an ISO 3166-1 code. A
commercial instrument has no promulgating authority and often no jurisdiction at all until a
governing-law clause supplies one, so it is filed by **genre** instead:
`contracts/<genre>/<leaf>/`, with `governing_law` as a `subject.json` field rather than a
directory. The genre vocabulary is controlled — insurance, investment, leasing, lending — and
lives in [`contracts/GENRES.md`](contracts/GENRES.md), which these rows seed. See
`docs/directory-conventions.md` §3, and §8.4 of that document, which names
`yc-safe-postmoney` as its worked example of a standard form. **That document is not on this
branch**: it lives on `docs/directory-conventions` and is unlinked here for that reason, so
read it with `git show docs/directory-conventions:docs/directory-conventions.md`.

Both SAFE rows carry the publisher's text byte-exact, a Markdown rendering of it, the header and
footer strings pandoc throws away (which is where the licence and the version stamp live), digests
for everything, and a validated source bundle. **`yc-safe-premoney` stops there** — no `encodings/`
directory, and none planned in this repository; its `NOTES.md` says why. `yc-safe-postmoney` adds
one encoding row and a fork register, and neither row has `projections/`, `report/` or `gates/`, so
no human review has been sought for either. They also differ from each other in the way that matters
most for a corpus: `yc-safe-postmoney` is the second row
here whose source terms are **determined** — CC BY-ND 4.0, printed in the form's own footer, so
attribution is a condition and is recorded in `NOTICE` — while `yc-safe-premoney` carries **no
terms at all**, because the licence footer was added in 2018 and those captures are from 2014.
Read each row's `SOURCE-LICENSE.md` before deriving anything from it. `yc-safe-postmoney`'s also
records an unresolved question: whether an L4 formalisation of a form is an "adaptation" under a
NoDerivatives licence.

`il/penal-law-1977` is the second Israeli row and the first that is enacted law. Its source --
the consolidated text of the Penal Law, 651 sections, deposited 2026-09-16 -- had sat in the tree
with no encoding beside it until 2026-09-21, when five of those sections were encoded: theft, and
the robbery sub-chapter that builds on it. The row exists to be read **beside**
`sg/penal-code-1871`, whose robbery module encodes the same crime from the other colonial code,
and its `NOTES.md` carries an element-by-element comparison of the two. Two things about it are
unlike every other row here. It is written in **Hebrew** -- identifiers, section titles and the
default natural-language rendering of every rule -- with an English rendering tagged beside each
one, so the same source produces a whole document in either language. And it carries the same two
open source-terms questions as `il/ofek-hadash-2008`, for the same reason: the consolidated text
was read from a Wikisource volunteer project rather than from *Reshumot*, which is geo-blocked and
publishes no consolidation. Its `SOURCE-LICENSE.md` sits beside `source/` at the subject level
rather than inside the encoding row.

`il/ofek-hadash-2008` is the first row whose subject is **not enacted law**, and the label
should be read before the row is. Ofek Hadash is a **collective agreement** between the State
of Israel and the Teachers' Union, layered with later agreements, binding decisions of a joint
bipartite follow-up committee, and ministry circulars. The one Act in the picture — Chapter 9
of the 2025 budget law — works by referring back to an *approved collective agreement* rather
than setting a rate itself, so even the statutory layer routes through the agreements. It is
filed under `il/` because the State is one of the two parties and the Knesset is the authority
for the fiscal chapter; `contracts/` would have been wrong, because this is not a commercial
instrument and it governs a whole profession.

It is also the first row read **entirely from a third-party corpus** rather than from an
official publisher, and the first whose `SOURCE-LICENSE.md` therefore carries **two** open
questions instead of one: what may be done with the instruments, and what may be done with the
compilation that transcribed them. Nothing was fetched from the Ministry of Education or from
*Reshumot*; the digests are over the corpus's published HTML. Its `/akn/il/…` identifiers,
which appear throughout that row's document register, are a convention of that corpus and are
**not citable outside it** — the corpus says so itself, and the row repeats it rather than
letting the identifiers pass as citations. Two further things distinguish it: all 282 documents
of the source corpus were read and are deposited as a per-document register, which is what
surfaced a January 2025 committee decision as the authoritative source for salary tables
otherwise attributed to an October 2022 agreement; and it is the first row to carry an
**executed** foreign-notation projection — six worked cases run through `catala interpret`
against the emitted Catala module, reproducing the figures the L4 asserts.

`us/regcf` was encoded in `legalese/l4-ide` and deposited here on 2026-09-23, byte-identical, with
its history left in l4-ide, which vendors it back into its regression corpus once its
`etc/canon-pin.json` names a commit that contains it. Its `README.md`, `PROJECTIONS.md`
and ladder figures stayed in l4-ide, because they describe l4-ide's own projections of the
corpus, and each row's `NOTES.md` says where they are. `uk/bna-1981` and `je/charities-2014` were
deposited from l4-ide the same day, in the same way, and nothing of either stayed behind.
`je/charities-2014` is the first row under a Crown Dependency. Its code, `je`, is Jersey's own
ISO 3166-1 alpha-2 code: Jersey legislates for itself, so the Law is filed under Jersey and not
under `uk/`.

*(This paragraph read "Empty at this writing" until 2026-08-25, by which point three
subjects had landed; a fourth landed on 2026-08-27, a fifth on 2026-08-31, the two
`contracts/` rows on 2026-09-04, and the first `doctrine/` row and the first `il/` row on
2026-09-07. A README that
describes a directory it no longer matches is worse than none, because it is believed.)*

## The bulk ingestion, by jurisdiction

Every jurisdiction directory uses its ISO 3166 code (`docs/directory-conventions.md` §2): countries and the EU at the top (`sg`, `il`, `nz`, `eu`), subdivisions nested beneath them (`au/wa`, `us/ca`, `ca/on`).
Most subjects below hold source text and metadata only; where one had already been encoded, the encoding is a row under its `encodings/`, as above.

One directory per jurisdiction, then one directory per body of law inside it.

| jurisdiction | contents |
| ------------ | -------- |
| [`au/wa/`](au/wa/) | Western Australian Acts |
| [`eu/`](eu/) | European Union Regulations and Directives |
| [`sg/`](sg/) | Singapore Acts |
| [`sg/sale-of-food-act-1973`](sg/sale-of-food-act-1973) | Sale of Food Act 1973 — the whole Act under one top-level goal (does the Act reach the article, is an offence committed, does a defence answer it, the most it can cost) and four goals: what the Act reaches (food, unsafe, unsuitable, adulterated, non-retail business), offences and penalties, defences and liability, enforcement and procedure | `draft` |
| [`sg/housing-and-development-act-1959`](sg/housing-and-development-act-1959) | Housing and Development Act 1959 — the whole Act under one top-level goal (may the person buy the flat, is the dealing lawful, is it safe from creditors, may the Board re-enter, acquire or penalise instead) and six goals: buying, dealings, the Board's remedies and periods, upgrading, the Board, offences and service | `draft` |
| [`sg/building-strata-management-act-2004`](sg/building-strata-management-act-2004) | Building (Strata Management) Act 2004 — the whole Act under one top-level goal (is the matter validly decided, may this person sit on the council, what does a proprietor in arrears face) and six goals: resolutions and meetings, the owner developer, the management corporation, the council, Strata Titles Boards, offences and service | `draft` |
| [`au/`](au/) | Commonwealth of Australia Acts |
| [`au/nsw/`](au/nsw/) | New South Wales Acts |
| [`au/vic/`](au/vic/) | Victorian Acts -- **not openly licensed; metadata only** until permission is obtained |
| [`au/qld/`](au/qld/) | Queensland Acts |
| [`au/sa/`](au/sa/) | South Australian Acts |
| [`au/tas/`](au/tas/) | Tasmanian Acts |
| [`nz/`](nz/) | New Zealand Acts and Bills |
| [`uk/`](uk/) | United Kingdom Acts (Westminster) |
| [`au/act/`](au/act/) | Australian Capital Territory Acts |
| [`au/nt/`](au/nt/) | Northern Territory Acts -- conditional permission; confirm before quoting text |
| [`us/`](us/) | United States federal Acts (public domain) |
| [`us/ca/`](us/ca/) | California code divisions (public domain) |
| [`us/ny/`](us/ny/) | New York Consolidated Laws articles |
| [`us/tx/`](us/tx/) | Texas code chapters |
| [`ca/`](ca/) | Canadian federal Acts -- English and French equally authoritative; conditional permission |
| [`ca/on/`](ca/on/) | Ontario statutes -- English and French equally authoritative; conditional permission |
| [`ca/bc/`](ca/bc/) | British Columbia statutes (King's Printer Licence) |
| [`in/`](in/) | Indian central Acts -- no reuse licence; not independently spot-checked |
| [`ie/`](ie/) | Irish Acts (Oireachtas PSI Licence, CC BY 4.0) |
| [`za/`](za/) | South African Acts -- **licence unclear; metadata only** until resolved |
| [`hk/`](hk/) | Hong Kong ordinances -- **not openly licensed; metadata only**; English and Chinese equally authentic |
| [`il/`](il/) | Israeli Laws (no copyright in statutes, Copyright Act 2007 s 6) -- Hebrew authoritative |
| [`us/al/`](us/al/) | Alabama (US state) -- **metadata only**; licence decision pending |
| [`us/ak/`](us/ak/) | Alaska (US state) -- **metadata only**; licence decision pending |
| [`us/az/`](us/az/) | Arizona (US state) -- **metadata only**; licence decision pending |
| [`us/ar/`](us/ar/) | Arkansas (US state) -- **metadata only**; licence decision pending |
| [`us/co/`](us/co/) | Colorado (US state) -- **metadata only**; licence decision pending |
| [`us/ct/`](us/ct/) | Connecticut (US state) -- **metadata only**; licence decision pending |
| [`us/de/`](us/de/) | Delaware (US state) -- **metadata only**; licence decision pending |
| [`us/dc/`](us/dc/) | District of Columbia (US federal district) -- **metadata only**; licence decision pending |
| [`us/fl/`](us/fl/) | Florida (US state) -- **metadata only**; licence decision pending |
| [`us/ga/`](us/ga/) | Georgia (US state) -- **metadata only**; licence decision pending |
| [`us/hi/`](us/hi/) | Hawaii (US state) -- **metadata only**; licence decision pending |
| [`us/in/`](us/in/) | Indiana (US state) -- **metadata only**; licence decision pending |
| [`us/ia/`](us/ia/) | Iowa (US state) -- **metadata only**; licence decision pending |
| [`us/ks/`](us/ks/) | Kansas (US state) -- **metadata only**; licence decision pending |
| [`us/ky/`](us/ky/) | Kentucky (US state) -- **metadata only**; licence decision pending |
| [`us/me/`](us/me/) | Maine (US state) -- **metadata only**; licence decision pending |
| [`us/md/`](us/md/) | Maryland (US state) -- **metadata only**; licence decision pending |
| [`us/mn/`](us/mn/) | Minnesota (US state) -- **metadata only**; licence decision pending |
| [`us/ms/`](us/ms/) | Mississippi (US state) -- **metadata only**; licence decision pending |
| [`us/mt/`](us/mt/) | Montana (US state) -- **metadata only**; licence decision pending |
| [`us/nm/`](us/nm/) | New Mexico (US state) -- **metadata only**; licence decision pending |
| [`us/nd/`](us/nd/) | North Dakota (US state) -- **metadata only**; licence decision pending |
| [`us/ok/`](us/ok/) | Oklahoma (US state) -- **metadata only**; licence decision pending |
| [`us/sc/`](us/sc/) | South Carolina (US state) -- **metadata only**; licence decision pending |
| [`us/sd/`](us/sd/) | South Dakota (US state) -- **metadata only**; licence decision pending |
| [`us/tn/`](us/tn/) | Tennessee (US state) -- **metadata only**; licence decision pending |
| [`us/vt/`](us/vt/) | Vermont (US state) -- **metadata only**; licence decision pending |
| [`us/va/`](us/va/) | Virginia (US state) -- **metadata only**; licence decision pending |
| [`us/wa/`](us/wa/) | Washington (US state) -- **metadata only**; licence decision pending |
| [`us/wy/`](us/wy/) | Wyoming (US state) -- **metadata only**; licence decision pending |
| [`ca/ab/`](ca/ab/) | Alberta (Canadian province or territory) -- **metadata only**; licence decision pending |
| [`ca/mb/`](ca/mb/) | Manitoba (Canadian province or territory) -- **metadata only**; licence decision pending |
| [`ca/nl/`](ca/nl/) | Newfoundland and Labrador (Canadian province or territory) -- **metadata only**; licence decision pending |
| [`ca/nt/`](ca/nt/) | Northwest Territories (Canadian province or territory) -- **metadata only**; licence decision pending |
| [`ca/ns/`](ca/ns/) | Nova Scotia (Canadian province or territory) -- **metadata only**; licence decision pending |
| [`ca/nu/`](ca/nu/) | Nunavut (Canadian province or territory) -- **metadata only**; licence decision pending |
| [`ca/qc/`](ca/qc/) | Quebec (Canadian province or territory) -- **metadata only**; licence decision pending |
| [`ca/sk/`](ca/sk/) | Saskatchewan (Canadian province or territory) -- **metadata only**; licence decision pending |

The directory contract (the "class" — see the repository README for the class/instance
design) is the subject-sidecar shape defined by the l4-ide orchestrator:

| file                | role                                                                                                                                                 |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `subject.json`      | machine-readable descriptor: id, display name, citation, source URL, corpus modules, per-leg projection declarations, encoding version, status       |
| `NOTES.md`          | this subject's idiosyncrasies, in prose, for humans — no script reads it                                                                             |
| `SOURCE-LICENSE.md` | the terms the quoted legal text carries, and the attribution NOTICE requires                                                                         |
| `*.l4`              | the encoding, in inert style, with `@ref` citations on dated arms                                                                                    |
| `cases/`            | dated scenario cases; expected values machine-evaluated, never hand-typed                                                                            |
| `projections/`      | emitted DMN/BPMN/other artifacts + fidelity reports declaring every loss                                                                             |
| `registers/`        | fork register, external-modification register, source bundle — validated against the schemas in l4-ide `specs/todo/single-instruction-demo/schemas/` |
| `report/`           | the conversion report                                                                                                                                |
| `gates/`            | HG1/HG2 grant artifacts: payloads, signatures, waivers, `allowed_signers`                                                                            |

An instance is expected to veer from the class; its divergences are recorded in its own
`NOTES.md`, never by forking the template.

Two amendments to that table are already in force and are not yet written into it, because
`docs/directory-conventions.md` supersedes it and its own §12
owns the rewrite. First, the sidecar shape above now describes a **vendored encoding row** under
`encodings/<encoder>/`, one level below the subject, and the descriptor splits in two:
`subject.json` at the subject level carries facts about the law, `encoding.json` in each row
carries facts about the encoding (§4.2). All seven subjects already do this. Second, `source/` and
`registers/` sit at the **subject** level, because the source text is a fact about the law and is
shared by every row (§6). That one is not yet uniform, and the tree is the honest record: both
`contracts/` rows put `source/` and `registers/` at the subject level, `us/chubb-hospital-cash`
puts `registers/` there, and the `sg/` rows keep both inside the encoding row. Do not read the
table above as contradicting the conventions document.

The stages an encoding passes through, and what the HG1 and HG2 gates certify, are in
[`PIPELINE.md`](../PIPELINE.md).
