# Scenario: cradle to grave — Simone Ng

One Singaporean life, 2003 to 2088, told as the sequence of legal decision points, calculations and applications that an ordinary citizen meets, and mapped milestone by milestone onto the Acts in this repository. It is a **sunny-day** scenario: nothing goes wrong, nobody sues, nobody is prosecuted, nobody divorces, and the only deaths are of old age. Its job is to touch as many Acts as a normal life does, so that a life-spanning assistant grounded in these encodings can be demonstrated against it.

Companion files:

- [`ABRIDGED.md`](ABRIDGED.md) — the same life in twenty beats, two a chapter, with Simone's age and look at each, written as the spine for a screenplay. The events it keeps are flagged `"abridged": true` in `facts.json`.
- [`GAPS.md`](GAPS.md) — what the scenario needs that the repository does not yet hold: Acts without an encoding, encoded Acts whose scope stops short of the question, subsidiary legislation never retrieved, policy that is not law, and the common-law doctrines a case register would have to carry.
- [`facts.json`](facts.json) — the cast and every dated event in machine-readable form, each event tagged with the Acts and sections it turns on, for a chat demo or a `build.py` in the shape of [`../public-prosecutor-v-tan/`](../public-prosecutor-v-tan/).

## Design rules

1. **Real dates, one "now".** The demo's present is **10 October 2026**. Everything before that date is backstory the assistant has on file; everything after it is what the assistant handles live. Any later date can be chosen as "now" for a particular demo — the timeline is written so that each year has something in it.
2. **Current law, replayed.** Almost every row in `subjects/sg/` states the law as at its encoding date and has no rule-version axis. Milestones before 2026 are therefore replayed under today's law: Simone's 2003 birth is registered under the Registration of Births and Deaths Act 2021, not the 1937 Act that actually applied. Where that anachronism matters it is flagged in the tables. The two rows that *do* carry dated arms (child-support, and the Act's own cohorts in the Child Development Co-Savings Act) are exercised deliberately.
3. **Statute first, then what the statute leaves out.** Each milestone names the question a citizen would actually ask, the provision that answers it, and whether this repository can answer it today. The status column uses six words:

| status | meaning |
| --- | --- |
| `ENC` | the question is inside the scope of an encoding row that exists |
| `PART` | the Act has a row, but this question falls outside the row's stated scope |
| `NONE` | the subject exists in `subjects/sg/` (source deposited) but has no encoding row |
| `REGS` | the answer is in subsidiary legislation that no row has retrieved |
| `POLICY` | the answer is an administrative scheme with no legislative instrument at all (HDB rules, CPF rates, MOE phases) |
| `CASE` | the answer is common law or depends on decided cases |

   The status column is a snapshot read from `subjects/sg/*/encodings/` on 10 October 2026. Rows are landing daily (fifteen of the subjects first classed `NONE` gained a row while this document was being written), so run [`check-status.py`](check-status.py) to re-derive the column from the tree before a demo.
4. **No cross-subject import.** `l4` cannot import across subjects, so a runnable version of this scenario is one file per Act with the facts duplicated, as `public-prosecutor-v-tan/build.py` does. `facts.json` is the single set of facts such a build would read.
5. **Sunny-day guard-rails.** No divorce, no custody dispute, no maintenance claim, no retrenchment, no workplace injury claim, no insolvency, no offence, no serious illness before old age, no foreign spouse or PR status, no Syariah-law marriage, no en-bloc sale, no inheritance dispute. Each of these is a branch another scenario can take; this one does not.

## The cast

| person | born | role | notes |
| --- | --- | --- | --- |
| **Simone Ng** | 14 Mar 2003, KK Women's and Children's Hospital | the main character | Singapore citizen by birth. First child of her parents. |
| Marcus Lim Wei Jie | 22 Jul 1999 | her husband from 18 May 2029 | Singapore citizen by birth. Mechanical engineer. Did full-time NS Aug 2018 to Aug 2020. |
| Lim Kai En | 5 Sep 2030 | their son | an "April 2025 Scheme child" for leave, a Child Support Package cohort child for the money |
| Lim Kai Xin | 12 Apr 2033 | their daughter | second child |
| Ng Boon Keng | 2 May 1970 | Simone's father | technician, then retired; dies 19 Aug 2052 with a will |
| Teo Siew Lan | 19 Nov 1972 | Simone's mother | clerk, retires 2035; cares for the grandchildren; dies 27 Jan 2060 without a will |
| Ng Jun Hao | 30 Aug 2006 | Simone's brother | full-time NS 2025 to 2027 |
| Lim Ah Huat and Chua Mei Fong | 1968, 1971 | Marcus's parents | 5-room flat in Bedok; mostly off-stage |
| Meridian Logistics Pte Ltd | — | Simone's first employer | management associate from 3 Aug 2026 at $4,200 a month, 13th-month AWS |
| Straits Precision Engineering Pte Ltd | — | Marcus's employer | from Aug 2023; $5,400 a month in 2026 |
| Mochi | 2035 | a dog | adopted from a shelter |

Simone's parents own a 4-room HDB flat in Tampines as joint tenants, bought in 1999. The family is not Muslim, so marriage and succession run under the Women's Charter and the Intestate Succession Act, not the Administration of Muslim Law Act.

---

## Chapter 0 — Born (2003)

Simone is born at KKH on 14 March 2003 to two Singapore citizens. The hospital notifies the birth; her father registers it and names her within the statutory window. She is a citizen by birth. Her first-year vaccinations follow the national schedule, and she is insured from her first day.

This chapter keeps only what is about *her*. Her mother's maternity leave and the Baby Bonus of 2003 are events in her parents' lives, and the same events recur, with current figures, when her own children are born in Chapters 6 and 7. They are told there once.

| date | event | the question | law | status |
| --- | --- | --- | --- | --- |
| 2003-03-14 | birth at KKH | Is she a Singapore citizen? | Constitution Art 121 (citizenship by birth) | `ENC` — the Constitution row carries Arts 121-123 |
| 2003-03-14 | hospital notifies the birth | Who must tell the Registrar-General, and by when? | Registration of Births and Deaths Act 2021 s 7 (24 hours) | `ENC` (replayed; the 1937 Act applied in 2003) |
| 2003-04-02 | father registers the birth and the name | By when must the birth be registered, and who may? | RBDA 2021 s 8 (42 days), s 10 | `ENC` |
| 2003-2004 | vaccinations | Which are compulsory? | Infectious Diseases Act 1976 ss 47-48 and Third Schedule (diphtheria, measles) | `PART` — the IDA row encodes ss 6, 15, 21A, 23-25, 46, 65 only |
| 2003 → | MediShield (later MediShield Life) | Is a newborn covered? | MediShield Life Scheme Act 2015 s 3 (every citizen is an insured person) | `ENC` |

## Chapter 1 — Preschool and primary school (2006–2015)

Kindergarten at six, Primary 1 in January 2010 at a school within a kilometre of home, an Edusave account that pays for enrichment, a first savings account at seven with her mother as trustee, a first passport at eight for a Malaysia holiday, PSLE in 2015.

| date | event | the question | law | status |
| --- | --- | --- | --- | --- |
| 2006-01 | kindergarten | Must the kindergarten be licensed? | Early Childhood Development Centres Act 2017 ss 3, 6 (replayed; in 2006 kindergartens were registered under the Education Act) | `ENC` |
| 2009-07 | P1 registration, Phase 2C | Which phase, and what does distance do? | MOE P1 registration framework | `POLICY` — no instrument |
| 2010-01-04 | Primary 1 | Is attendance compulsory, and from when? | Compulsory Education Act 2000 s 2 ("compulsory school age": above 6 and under 15), s 3 (born after 1 Jan 1996, citizen, resident) | `ENC` |
| 2010-01 | Edusave account | What goes into it each year? | Education Endowment and Savings Schemes Act 1992 ss 7-9 (Edusave Pupils Fund) | `PART` — the row is scoped to the Post-Secondary Education Scheme |
| 2010-03 | child savings account, mother as trustee | Is the bank taking a deposit; what is a deposit? | Banking Act 1970 ss 4A, 4B | `ENC` |
| 2011-06 | first passport | Who may apply for a child under 16? | Passports Act 2007 s 6, s 27 (a parent) | `ENC` |
| 2011-06 | drive to Malacca and back | What may the family bring back duty-free? | Customs Act 1960 ss 93, 128J; GST import relief | `ENC` for the offences and the Green Channel presumption; `REGS` for the allowance amounts (Customs (Duties) Order, GST (Imports Relief) Order) |
| 2015-09 | PSLE | Who sets and scores it? | Singapore Examinations and Assessment Board Act 2003 | `NONE` — and the scoring bands are `POLICY` |

## Chapter 2 — Secondary school, junior college and three birthdays (2016–2024)

Secondary school from 2016, NRIC at fifteen, O-levels in 2019, junior college 2020–2021, a part-time job in the gap after A-levels, then three birthdays that each switch legal capacities on: eighteen, when she could marry without a special licence and learn to drive; twenty-one, when she becomes an elector, a presumed organ donor, and a person who can make a will or a lasting power of attorney.

| date | event | the question | law | status |
| --- | --- | --- | --- | --- |
| 2018-03-14 | turns 15 | Must she register for an NRIC? | National Registration Act 1965 s 6 | `ENC` |
| 2019-10 | O-levels | — | SEAB Act 2003 | `NONE` |
| 2021-03-14 | turns 18 | Could she marry? Could she hold a driving licence? | Women's Charter 1961 s 9 (void under 18 without a special licence); Road Traffic Act 1961 s 35 and the driving-licence rules | `ENC` for s 9; `PART` for the RTA (only the s 35 offence is encoded) and `REGS` for the age rule |
| 2021-12 → 2022-07 | part-time retail job, $1,900 a month | Does the Employment Act apply? Does Part 4? Is CPF payable? | Employment Act 1968 s 2 (employee), s 35 (Part 4: non-workman at or under $2,600); CPF Act 1953 s 7 | `ENC` for the Act's own tests; `REGS` for the contribution rates (First Schedule not encoded) |
| 2022-04 | files nothing | Must she file a tax return on $13,300? | Income Tax Act 1947 s 62 (returns), the Comptroller's filing requirement | `ENC` for the charge; the filing threshold is `POLICY` (IRAS) |
| 2024-03-14 | turns 21 | Is she an elector? | Parliamentary Elections Act 1954 s 5 (citizen, 21, ordinarily resident) | `ENC` |
| 2024-03-14 | turns 21 | Is she now a presumed organ donor, and how would she object? | Human Organ Transplant Act 1987 s 5, s 8 (registering an objection) | `ENC` |
| 2024-03-14 | turns 21 | Could she make a will? An LPA? | Wills Act 1838 s 4 (no will under 21); Mental Capacity Act 2008 s 11 (donor must be 21) | `ENC` — both succession rows carry the Wills Act; the MCA row carries ss 11-12 |

## Chapter 3 — University (2022–2026)

A four-year business degree at NUS from August 2022, paid by a tuition grant, her Post-Secondary Education Account and a tuition fee loan, with her father drawing on his CPF for part of the fees. An internship in 2025. Her first general election on 3 May 2025. She graduates in June 2026.

| date | event | the question | law | status |
| --- | --- | --- | --- | --- |
| 2022-08 | matriculates at NUS | — | National University of Singapore (Corporatisation) Act 2005 | `NONE` |
| 2022-08 | tuition grant; fee loan | Is a citizen's fee subsidised? What bond? | MOE Tuition Grant Scheme; Tuition Fee Loan | `POLICY` |
| 2022-08 | PSEA pays part of the fees | What may the account be used for, and who may withdraw? | Education Endowment and Savings Schemes Act 1992 ss 20, 22 (Post-Secondary Education Scheme: members, withdrawals) | `ENC` |
| 2022-08 | father draws CPF for fees | May a parent's Ordinary Account fund a child's degree, and on what repayment terms? | CPF Act 1953 (Education Scheme withdrawals); CPF (Education) Regulations | `PART` for the Act; `REGS` |
| 2025-05 → 2025-07 | internship, $1,200 a month | Must the employer pay CPF for a student intern? | CPF Act s 7 and the exemption for students in approved programmes | `REGS` — the exemption lives in subsidiary legislation not retrieved |
| 2025-05-03 | General Election | Must she vote? What happens if she does not? | Parliamentary Elections Act 1954 s 43 (name removed from the register; restoration) | `ENC` |
| 2026-06 | graduates | — | — | — |

## Chapter 4 — First job, first payslip, first tax return (2026–2027) — the demo's "now"

On 3 August 2026 Simone starts as a management associate at Meridian Logistics on $4,200 a month with a thirteenth-month payment. On 10 October 2026 she has two payslips and a stack of questions: what is on them, what her leave is, when she can see a doctor on company time, whether she needs to do anything about tax, what to do about the marketing calls that started the day she signed up for a credit card. She buys term life insurance and an Integrated Shield plan.

| date | event | the question | law | status |
| --- | --- | --- | --- | --- |
| 2026-08-03 | contract of service | What must a written contract contain? Can the probation clause do what it says? | Employment Act 1968 Part 2 (contracts of service), key employment terms; probation is contractual | `ENC` for Part 2; `CASE` for probation and implied terms |
| 2026-08-03 | hours and overtime | Does Part 4 apply to her? | Employment Act s 35 — a non-workman above $2,600 is outside Part 4 | `ENC` (the answer is no, and the assistant should say why) |
| 2026-08-31 | first payslip | When must salary be paid, and what must the itemised payslip show? | Employment Act Part 3 (salary) | `ENC` |
| 2026-08-31 | CPF on $4,200 | How much goes in, and where? | CPF Act 1953 s 7 (the duty); First Schedule (rates); s 13 (allocation) | `ENC` for the duty; `REGS` for the rates and allocation. Expected answer with the 2026 figures as supplied facts: employer 17% $714, employee 20% $840, total $1,554; allocated OA $966, SA $252, MA $336 |
| 2026-08-31 | Skills Development Levy | What does her employer pay on top? | Skills Development Levy Act 1979 s 3 (0.25%, floor $2, on wages up to $4,500) | `ENC` — $10.50 on $4,200 |
| 2026-11-03 | three months served | How many days of annual leave has she earned? Sick leave? | Employment Act s 88A (7 days in the first year, rising to 14), s 89 (14 outpatient, 60 hospitalisation) | `ENC` — her contract gives 14 days from day one, which is more than the statute, so the statute is a floor |
| 2026-12-25 | public holiday | Which days are public holidays; what if one falls on a Sunday? | Holidays Act 1998 s 4 and Schedule (11 days), s 6; Employment Act s 88 | `ENC` for both |
| 2026-09 | credit card | Who may be issued a card; what income? | Banking Act 1970 s 57; Banking (Credit and Charge Card) Regulations 2013 (minimum annual income) | `ENC` for s 57; `REGS` for the income threshold |
| 2026-09 | the bank pulls her credit report | What may a credit bureau hold and disclose about her? | Credit Bureau Act 2016 ss 4, 6-8, 11-13 | `ENC` |
| 2026-09 | deposits in two banks | Are her deposits insured, and to what amount? | Deposit Insurance and Policy Owners' Protection Schemes Act 2011 ss 22-23, 26 and First Schedule ($100,000 Maximum DI Coverage) | `ENC` |
| 2026-09 | marketing calls | Can she stop them? | Personal Data Protection Act 2012 ss 43-44 (Do Not Call Registry), ss 13-16 (consent) | `ENC` |
| 2026-09 | spam SMS | — | Spam Control Act 2007 | `ENC` |
| 2026-10 | term life policy and Integrated Shield plan through an adviser | What must the adviser disclose; what is the adviser's duty? | Financial Advisers Act 2001 ss 35-45; Insurance Act 1966 (whole Act encoded) | `ENC` |
| 2026-10 | nominates her parents as beneficiaries | Trust nomination or revocable nomination? | Insurance Act 1966 ss 132-133 | `ENC` |
| 2026-10 | Dependants' Protection Scheme | Is she automatically covered when CPF contributions start? | CPF Act Part 5 (DPS) | `PART` — the CPF row stops before Part 3A |
| 2026-10 | workplace safety briefing | What does her employer owe her? | Workplace Safety and Health Act 2006 | `ENC` |
| 2027-03 | files her first return (YA 2027) | Does she owe tax on Aug–Dec 2026 income of $21,000? | Income Tax Act 1947 ss 10, 39 (earned income relief $1,000, CPF relief), Second Schedule rates | `ENC` — chargeable income $15,800, tax nil |
| 2027-04 | Workfare? | — | Workfare is `POLICY`; not applicable at her income | — |
| 2028-03 | YA 2028 return | Tax on 2027 income of $54,600 (12 × $4,200 plus AWS)? | ITA s 39 reliefs; Part B rates | `ENC` — CPF relief $10,920, earned income relief $1,000, chargeable $42,680, tax $737.60 before any Budget rebate |

## Chapter 5 — Engagement, a BTO application, and a marriage (2028–2029)

Simone and Marcus apply for a four-room Build-To-Order flat in Tampines North in the February 2028 exercise under the fiancé/fiancée scheme, succeed in the ballot, book a flat, sign the agreement for lease in October 2028 and pay the first ten per cent from their Ordinary Accounts. They file notice of marriage and are married at the Registry on 18 May 2029, with a customary dinner in November. While the flat is built they rent under the Parenthood Provisional Housing Scheme. In September 2029 they vote in a presidential election. Marcus does his annual in-camp training.

| date | event | the question | law | status |
| --- | --- | --- | --- | --- |
| 2028-02 | BTO application | Are they eligible: citizenship, age 21, family nucleus, income ceiling, no other property? | HDB eligibility conditions (HFE letter) | `POLICY` — the Act is fully encoded and says nothing about these |
| 2028-02 | the 30-month rule | Does either of them own, or has either sold, property in the last 30 months? | Housing and Development Act 1959 s 50(1) | `ENC` — the answer is no, so they are entitled to purchase |
| 2028-02 | Enhanced CPF Housing Grant | How much grant on a combined income of $9,600? | EHG table | `POLICY` |
| 2028-10 | agreement for lease; 10% downpayment from CPF | May Ordinary Account savings be used, and what charge does the Board take? | CPF Act (Approved Housing Schemes); CPF (Approved Housing Schemes) Regulations | `PART`, `REGS` |
| 2028-10 | HDB loan in principle | What loan-to-value, what interest? | HDB loan terms (2.6%, 75% LTV) | `POLICY` |
| 2029-04-20 | notice of marriage | How long before the wedding, and how long is the notice good for? | Women's Charter 1961 ss 14-15 (notice; lapses after three months) | `PART` — the Charter row (ss 6A, 9, 11-13, 17(2), 21A, 60-63C, 69, 93-95A) stops short of the notice and solemnisation procedure |
| 2029-05-18 | solemnisation at ROM | Who may solemnise; is parental consent needed at 26 and 29? | Women's Charter ss 17(2), 21A (consent needed only for a minor, under 21), s 22 (solemnisation) | `ENC` for consent; `PART` for s 22 |
| 2029-05-18 | monogamy | Is either already married? | Women's Charter s 11 (void by subsisting prior marriage), s 6A (marrying again during a spouse's lifetime) | `ENC` |
| 2029-05-18 | the Registry's certificate; what the marriage does to property | Does marriage change who owns what? | Women's Charter s 51 (married woman's capacity), s 52 (property); the agreement for lease is already in joint names | `PART`; joint tenancy is `CASE` |
| 2029-06 | change of address | Must they tell the NRIC authority? | National Registration Act 1965 s 10 (28 days) | `ENC` |
| 2029-06 → 2031-08 | PPHS rental flat | What governs the tenancy? Is the lease stamped? | HDB PPHS terms; tenancy at common law; Stamp Duties Act First Schedule Art 8 (leases) | `POLICY`; `CASE`; `PART` (the stamp-duty row encodes Art 3 only) |
| 2029-07-22 | Marcus turns 30 | Does CareShield Life start for him? | CareShield Life and Long-Term Care Act 2019 s 6(1)(a) (citizens born on or after 1 Jan 1980, from 30) | `ENC` — the premium amounts are `REGS` |
| 2029-09 | in-camp training | Must his employer release him, and what is he paid? | Enlistment Act 1970 ss 13-15 (operationally ready NS liability), ss 21-23 (employers); National Servicemen (Employment) Act 1970 ss 4-9 (his job is protected while he serves); make-up pay | `ENC` for both Acts; `POLICY` for make-up pay |
| 2029-09 | Presidential Election | Must they vote? | Presidential Elections Act 1991 (compulsory voting) | `ENC` |
| 2030-03 | YA 2030 return | Does marriage change her tax? | ITA s 39(2)(m) NSman wife relief $750; spouse relief not available (Marcus earns more than the limit) | `ENC` |

## Chapter 6 — First child (2030–2031)

Kai En is born at KKH on 5 September 2030. Both parents are citizens, so he is a citizen by birth, an "April 2025 Scheme child" for parental leave, and a child born after 1 April 2027 for the Child Support Package. Simone begins maternity leave two weeks before the due date; Marcus takes four weeks of paternity leave; they split ten weeks of shared parental leave six and four. The Baby Gift arrives, the Child Development Account is opened and co-matched, and the child's first passport is issued for a trip in 2031.

| date | event | the question | law | status |
| --- | --- | --- | --- | --- |
| 2030-06 | the 2030 Census | Must the household answer? | Census Act 1973; Statistics Act 1973 ss 5-6 (duty to answer a requisition) | `NONE`; `ENC` |
| 2030-01 → 2030-09 | antenatal care; the delivery bill | What may Medisave pay for a confinement? | CPF Act 1953 s 16 (Medisave restrictions); CPF (Medisave Account Withdrawals) Regulations (the maternity package limits) | `ENC` for s 16; `REGS` for the limits |
| 2030-08-22 | maternity leave begins | May she start before the birth? How many weeks in all? Who pays which weeks? | Employment Act s 76 (16 weeks; up to 4 before confinement); CDCSA ss 9, 9A, 10 (employer pays the first 8, Government the last 8, capped at $10,000 per 4 weeks) | `ENC` — the CDCSA row's fork F1 is exactly this cap |
| 2030-09-05 | birth | Citizen by birth? | Constitution Art 121 | `ENC` |
| 2030-09-05 | hospital notification; registration within 42 days | — | RBDA 2021 ss 7-8, 10 | `ENC` |
| 2030-09-05 | paternity leave | How many weeks, and within what period? | CDCSA ss 12H-12J (4 weeks for an April 2025 Scheme child) | `ENC` |
| 2030-09 | shared parental leave | How many weeks, how allocated, who is reimbursed? | CDCSA ss 12DA-12DD (10 weeks; default allocation; valid arrangements) | `ENC` |
| 2030-10 | Baby Gift $10,000 | What does the Package give this child? | SG Child Support Package as announced; child-support row | `ENC` (as policy, dated arm from 1 Apr 2027, flagged "announced, not enacted") |
| 2030-10 | CDA First Step Grant $5,000; co-matching cap $5,000 | — | CDCSA Part 2 (the Child Development Account); child-support row | `ENC` |
| 2031 → 2046 | Child Credits $2,000 a year, years he turns 1 to 16 | How much over the whole run? | child-support row | `ENC` — $32,000 |
| 2030-10 | Medisave Grant for Newborns $4,000 | — | CPF Board scheme | `POLICY` (MediShield Life cover from birth is told once, in Chapter 0) |
| 2031-01 | childcare leave begins to accrue | How many days each, and from when? | CDCSA ss 12B-12C (6 days a year per parent), s 12D (unpaid infant care leave) | `ENC` — note the Employment Act row leaves ss 84-87A (its childcare-leave sections) unencoded, so ask the CDCSA row, not the EA row |
| 2031-01 | infant care centre, 7:00 to 19:00 | Must it be licensed; what subsidies? | Early Childhood Development Centres Act 2017 ss 3, 6; ECDA Basic and Additional Subsidy | `ENC`; `POLICY` |
| 2031-03 | YA 2031 return | Qualifying child relief, working mother's child relief, parenthood tax rebate? | ITA s 39(2) (QCR $4,000; WMCR fixed at $8,000 for a first child born in or after 2024), s 42A (rebate $5,000 for a first child, shareable) | `ENC` |
| 2031-06 | child's passport | — | Passports Act 2007 s 27 | `ENC` |

## Chapter 7 — Keys, a second child, a car, a dog, and school (2031–2040)

Keys to the flat in August 2031: stamp duty, a mortgage, Home Protection Scheme cover, property tax, conservancy charges, utilities, a renovation. Kai Xin is born in April 2033, a month after Simone turns thirty and her own CareShield Life premiums begin. Simone changes jobs in 2034. They buy a used car on hire-purchase that year and adopt a dog in 2035. The five-year minimum occupation period ends in August 2036. Kai En starts Primary 1 in 2037, Kai Xin in 2040. Simone's father retires in 2033 and starts CPF LIFE payouts in 2035; her mother retires in 2035 and looks after the children, so Simone claims grandparent caregiver relief and parent relief, and tops up her mother's Retirement Account.

| date | event | the question | law | status |
| --- | --- | --- | --- | --- |
| 2031-08 | lease of the flat, 99 years, joint tenants | What kind of dealing is this; what does the Board's lease restrict? | Housing and Development Act 1959 Part 4 (ss 50-59: dealings, protection from creditors) | `ENC` |
| 2031-08 | buyer's stamp duty on $420,000 | How much? | Stamp Duties Act 1929 First Schedule Art 3(a)(iv) | `ENC` — $1,800 + $3,600 + $1,800 = $7,200 |
| 2031-08 | additional buyer's stamp duty | Any? | SDA First Schedule Art 3(bi) | `ENC` — nil: two citizens, first residential property |
| 2031-08 | HDB loan, 75% LTV, repaid from CPF OA | — | HDB loan terms; CPF (Approved Housing Schemes) Regulations | `POLICY`; `REGS` |
| 2031-08 | Home Protection Scheme | Is it compulsory when the loan is serviced from CPF? | CPF Act 1953 Part 4A (ss 29 ff) | `PART` |
| 2031-08 | fire insurance | — | HDB fire insurance requirement | `POLICY` |
| 2031-08 | title | Is an HDB flat under the Torrens register? What does indefeasibility give them? | Land Titles Act 1993 s 46 | `ENC` (s 46 is in the row as the hinge of Part 17) |
| 2031-09 | change of address | — | National Registration Act s 10 | `ENC` |
| 2031-10 | renovation: hacking a wall, new kitchen | Which works need permission, and whose? | HDB renovation permit; Building Control Act 1989 s 4(1)(d) (insignificant works) | `POLICY`; `ENC` |
| 2032-01 | property tax bill | What is the charge; what is the owner-occupier rate on an annual value of $12,000? | Property Tax Act 1960 s 6, s 9; Property Tax (Rate for Owner-Occupied Residential Premises) Order | `ENC` for the charge; `REGS` for the owner-occupier rates |
| 2032-01 | service and conservancy charges | Who levies them; what if they are late? | Town Councils Act 1988 s 51 (levy), s 66 (arrears) | `PART` for s 51; `ENC` for s 66 |
| 2032-01 | SP account, Open Electricity Market retailer, PUB water | — | Electricity Act 2001; Public Utilities Act 2001; Gas Act 2001 | `ENC` for the offence sections, `PART` for billing |
| 2032-05 | a new laptop fails in month three | What does the retailer owe her? | Consumer Protection (Fair Trading) Act 2003 Part 3 (the "lemon law": defect within 6 months presumed present at delivery; repair or replace) | `ENC` — the retailer repairs it; the Small Claims Tribunals Act 1984 row is there if it had not |
| 2033-03-14 | Simone turns 30 | CareShield Life premiums begin | CareShield Life and Long-Term Care Act 2019 s 6(1)(a) | `ENC` |
| 2033-03-14 | NRIC re-registration at 30 | — | National Registration Act 1965 s 8 | `ENC` |
| 2033-04-12 | Kai Xin born | the whole Chapter 6 cluster again | CDCSA, RBDA, child-support, ITA | `ENC` — WMCR $10,000 and parenthood rebate $10,000 for a second child |
| 2034-02 | Simone resigns, joins a bank at $6,800 | What notice; what happens to unused leave; does the CPF ceiling bite? | Employment Act ss 10-11 (notice), s 88A; CPF Ordinary Wage ceiling ($8,000 from 2026) | `ENC`; the ceiling is `REGS` |
| 2034-06 | used car on hire-purchase | What must the agreement show; what are her rights as hirer? | Hire-Purchase Act 1969 Part 2 (ss 5, 8, 11, 14-17: the written agreement, the hirer's statutory rights, early completion, repossession notice) | `ENC` — the row takes "the provisions a hirer or guarantor meets" |
| 2034-06 | certificate of entitlement; registration; road tax | — | Road Traffic Act 1961 Part 1; Road Traffic (Motor Vehicles, Quota System) Rules | `PART`; `REGS` |
| 2034-06 | motor insurance | Is third-party cover compulsory, and what makes a policy comply? | Motor Vehicles (Third-Party Risks and Compensation) Act 1960 ss 3-4 | `ENC` |
| 2034-06 | season parking | — | Parking Places Act 1974; HDB and Town Council parking | `ENC` for the Act's offences; `POLICY` |
| 2035-03 | Mochi, a mixed-breed dog | Which breeds may live in an HDB flat; must the dog be licensed and vaccinated? | HDB approved-breeds list; Animals and Birds Act 1965 s 40 (rabies vaccination), the Dog Licensing and Control Rules; Part 4 (welfare) | `POLICY`; `PART`; `REGS`; `ENC` for welfare |
| 2035-05 | Boon Keng turns 65 | CPF LIFE payouts begin | CPF Act 1953 Part 3A (Lifelong Income Scheme, ss 27K ff) | `PART` |
| 2035-05 | Boon Keng checks Silver Support | Is he eligible at 65? | Silver Support Scheme Act 2015 ss 6-7 | `ENC` — not eligible on lifetime contributions; the thresholds are prescribed facts |
| 2033-05 | Boon Keng turns 63 | Must his employer offer re-employment, and until what age? | Retirement and Re-employment Act 1993 ss 4, 7, 7A | `ENC` — the two ages are gazetted under ss 4(1) and 7A(11) and enter as facts |
| 2036-03 | YA 2036 return | Grandparent caregiver relief now that Siew Lan has stopped work and minds Kai Xin; parent relief for a parent living with her; relief for topping up her mother's Retirement Account | ITA s 39(2)(p), s 39(2) (parent), s 39(3) (CPF cash top-up, capped) | `ENC` |
| 2036-03 | Matched Retirement Savings Scheme | Does the Government match the top-up? | CPF Board scheme | `POLICY` |
| 2036-08 | minimum occupation period ends | May they now sell without the Board's consent? | Housing and Development Act 1959 s 55 (no sale within the prescribed MOP without consent) | `ENC` for s 55; the length of the MOP is `REGS` |
| 2037-01 | Kai En, Primary 1 (Kai Xin follows in 2040) | — | Compulsory Education Act 2000 s 3; P1 phases | `ENC`; `POLICY` |
| 2030, 2035, 2040 … | general elections | — | Parliamentary Elections Act 1954 ss 5, 43 | `ENC` |

## Chapter 8 — Mid-life: a bigger home, wills, parents, a son in uniform (2040–2060)

In 2040 they sell the Tampines flat and buy a seven-year-old resale executive condominium in Punggol, which is still inside its ten-year window under the EC Act. They make wills and CPF nominations in 2041. Kai En registers for national service at sixteen and a half, enlists in 2049 and completes full-time service in 2051. Boon Keng dies in 2052 leaving a will; Siew Lan dies in 2060 without one. Marcus reaches fifty-five in 2054 and Simone in 2058.

| date | event | the question | law | status |
| --- | --- | --- | --- | --- |
| 2040-03 | sale of the Tampines flat | Is the sale within the MOP? What resale levy? | HDA s 55; HDB resale levy | `ENC`; `POLICY` |
| 2040-03 | seller's stamp duty | Any, after nine years? | SDA Art 3(bg), (bj) | `ENC` — nil |
| 2040-04 | buying a 2033-TOP executive condominium | May a citizen buy within 10 years of TOP; what may the seller do; is a resale premium due? | Executive Condominium Housing Scheme Act 1996 ss 5, 9, 10 | `ENC` |
| 2040-04 | buyer's stamp duty on $1,300,000 | How much? | SDA Art 3(a)(iv) | `ENC` — $36,600 |
| 2040-04 | additional buyer's stamp duty | Any, given they sold first? | SDA Art 3(bi); and the remission rules had they bought first | `ENC` for the charge (nil); `REGS` for the Stamp Duties (Spouses) (Remission of ABSD) Rules |
| 2040-04 | bank mortgage | What LTV and debt-servicing limits? | MAS Notices 632 and 645 | `REGS` |
| 2040-04 | the estate agent | Who may act, and on what commission? | Estate Agents Act 2010 ss 28-29 (licensing), s 44 (no commission without the prescribed agreement) | `ENC` |
| 2040-04 | option and sale and purchase agreement | What law governs the option, the deposit and completion? | Conveyancing and Law of Property Act 1886; common law of contract | `NONE`; `CASE` |
| 2040-06 | the management corporation | What do they owe the MCST, and what may it do? | Building Maintenance and Strata Management Act 2004 ss 37-44 | `ENC` |
| 2041-02 | wills, each leaving everything to the other then to the children | Formalities; witnesses; what a gift to a witness does | Wills Act 1838 ss 4, 6, 10 | `ENC` (both succession rows) |
| 2041-02 | CPF nominations | Who may nominate; what if the nomination exceeds the Minister's maximum? | CPF Act s 25(1) | `ENC` |
| 2041-02 | insurance nominations updated | — | Insurance Act ss 132-133 | `ENC` |
| 2043-03 | SkillsFuture course at 40 | What credit does she have? | Skills and Workforce Development Agency Act 2026; Lifelong Learning Endowment Fund Act 2001; SkillsFuture Credit | `NONE`; `POLICY` |
| 2047-03 | Kai En registers for NS at 16½ | Who is a person subject to the Act? | Enlistment Act 1970 s 2, s 12 | `ENC` |
| 2049-02 → 2051-02 | Kai En's full-time NS | What law governs him in uniform? Exit permits for the family holiday? | Singapore Armed Forces Act 1972; Enlistment Act ss 32-33 (exit permits) | `ENC` |
| 2050-03 | YA 2050 return | Parent-of-NSman relief for both parents | ITA s 39(2)(n), $750 each | `ENC` |
| 2052-08-19 | Boon Keng dies at 82, at home | Who certifies, who registers, by when? | RBDA 2021 ss 19-23 | `ENC` |
| 2052-08 | his will: everything to Siew Lan; Simone is executor | Is the will valid? Which grant? What comes off the estate first? | Wills Act ss 4, 6; Probate and Administration Act 1934 (grant of probate; the order of application) | `ENC` (succession rows) |
| 2052-08 | the Tampines flat, joint tenancy | Does it pass by survivorship, outside the will? | Land Titles Act 1993 (joint tenancy); HDA Part 4 (transmission) | `PART` (Part 17 only); `CASE` |
| 2052-08 | his CPF | To whom, and is it part of the estate? | CPF Act s 25 (nominee: Siew Lan); CPF monies fall outside the estate | `ENC`; `CASE` |
| 2052-08 | cremation at Mandai | — | Environmental Public Health Act 1987 and its cemeteries and crematoria regulations | `PART`; `REGS` |
| 2054-07 | Marcus turns 55 | What may he withdraw; what stays as the retirement sum? | CPF Act s 15(1)-(6) | `ENC` — the retirement sum itself is a fact supplied |
| 2058-03 | Simone turns 55 | same | CPF Act s 15 | `ENC` |
| 2060-01-27 | Siew Lan dies at 87, intestate | Who takes, in what shares? | Intestate Succession Act 1967 s 7 (no spouse: the children, Simone and Jun Hao, equally); PAA (letters of administration) | `ENC` (both rows) |
| 2060-02 | is the estate small enough for the Public Trustee? | — | Public Trustee Act 1915; PAA ss 55, 62 | `ENC` for the sections in the row; the value limits are `REGS` |

## Chapter 9 — Retirement, old age, and two deaths (2062–2088)

Marcus retires at sixty-three in 2062 and is re-employed part-time; his CPF LIFE payouts start in 2064. Simone retires in 2066 and starts payouts in 2068. They make lasting powers of attorney at sixty. In 2070 they sell the condominium, which is by then fully privatised, and buy a short-lease two-room Flexi flat. Simone makes an advance medical directive at seventy. Marcus dies in 2083; Simone in 2088, at eighty-five, leaving a will in favour of her two children.

| date | event | the question | law | status |
| --- | --- | --- | --- | --- |
| 2059-03, 2063-07 | lasting powers of attorney, each the other's donee, Kai Xin as replacement | Who may be a donee; what may a donee never do; how is an LPA revoked? | Mental Capacity Act 2008 ss 11-15 | `ENC` |
| 2062-07-22 | Marcus turns 63 | Retirement age; the re-employment offer | Retirement and Re-employment Act 1993 ss 4, 7A (the Minister's gazetted ages) | `ENC`, the ages as facts |
| 2064-07 | Marcus turns 65 | CPF LIFE payouts; Silver Support check | CPF Act Part 3A; Silver Support Scheme Act ss 6-7 | `PART`; `ENC` (not eligible) |
| 2066-03 | Simone retires | — | RRA 1993 s 4 | `ENC` |
| 2068-03 | Simone turns 65 | CPF LIFE; MediShield Life premium subsidies at 65 | CPF Act Part 3A; MediShield Life Scheme Act s 4 and the premium regulations | `PART`; `REGS` |
| 2068 | Pioneer, Merdeka, Majulah packages | Does she qualify for any of them? | Pioneer Generation and Merdeka Generation Funds Act 2014; the Majulah Package | `NONE` — but the answer is no by birth year, which is the kind of negative a life assistant should give without being asked |
| 2070-05 | sell the EC, buy a 2-room Flexi flat on a 30-year lease | Does the EC Act still restrict the sale? May they buy from the Board having just sold? Silver Housing Bonus? | EC Act s 9 (ten years from TOP have passed); HDA s 50(1) (the sale completes before the application); Silver Housing Bonus | `ENC`; `ENC`; `POLICY` |
| 2070-05 | stamp duty on the 2-room flat | — | SDA Art 3(a)(iv) | `ENC` |
| 2070-06 | change of address | — | National Registration Act s 10 | `ENC` |
| 2073-03 | advance medical directive at 70 | Who may make one; who witnesses; when does it operate? | Advance Medical Directive Act 1996 ss 3-9 | `ENC` |
| 2083-02-09 | Marcus dies at 83 | Registration; his will; his CPF; the flat by survivorship | RBDA ss 19-23; Wills Act; PAA; CPF Act s 25; HDA | `ENC`, `ENC`, `ENC`, `ENC`, `PART` |
| 2083-03 | Simone, widow | Is she now a "wife or widow of an NSman" for relief? Is the 2-room lease hers alone? | ITA s 39(2)(m); HDB lease terms | `ENC`; `POLICY` |
| 2088-11-02 | Simone dies at 85 | Registration; her will (Kai En executor; to the children equally); CPF to the two nominees; insurance nominations; the remaining lease | RBDA ss 19-23; Wills Act; PAA; CPF Act s 25(1) (how a nomination is split); Insurance Act ss 132-133; HDB short-lease refund terms | `ENC` throughout; the lease refund is `POLICY` |
| 2088-11 | estate duty | Any? | Estate Duty Act 1929 s 2A (the Act applies only to deaths before 15 Feb 2008) | `ENC` — a one-line negative, and the row asserts it |

---

## What the scenario touches

Counting by subject, the story above meets **67 Acts and the Constitution**, plus one announcement-based subject:

- **ENC, with the question inside the row's scope** (53 Acts, the Constitution, and the child-support row): the Constitution (Arts 121-123); Education Endowment and Savings Schemes 1992 (PSEA); Skills Development Levy 1979; Women's Charter 1961 (ss 9, 11, 6A, 17(2), 21A); Retirement and Re-employment 1993; Hire-Purchase 1969; Estate Agents 2010; Estate Duty 1929 (s 2A); Compulsory Education 2000; Early Childhood Development Centres 2017; Holidays 1998; CareShield Life and Long-Term Care 2019; Deposit Insurance and Policy Owners' Protection Schemes 2011; National Servicemen (Employment) 1970; Registration of Births and Deaths 2021; MediShield Life Scheme 2015; Banking 1970; Passports 2007; Customs 1960 (offences); National Registration 1965; Parliamentary Elections 1954; Presidential Elections 1991; Human Organ Transplant 1987; Mental Capacity 2008; Employment 1968; Child Development Co-Savings 2001; child-support (announcement row); Income Tax 1947; Credit Bureau 2016; PDPA 2012; Spam Control 2007; Financial Advisers 2001; Insurance 1966; Workplace Safety and Health 2006; Housing and Development 1959; Enlistment 1970; Singapore Armed Forces 1972; Stamp Duties 1929 (Art 3); Land Titles 1993 (s 46); Building Control 1989; Consumer Protection (Fair Trading) 2003; Motor Vehicles (Third-Party Risks) 1960; Parking Places 1974; Silver Support Scheme 2015; Executive Condominium Housing Scheme 1996; Building Maintenance and Strata Management 2004; the three succession Acts (Wills 1838, Intestate Succession 1967, Probate and Administration 1934, via the two `succession` rows); Advance Medical Directive 1996; Statistics 1973; Property Tax 1960 (charge); Town Councils 1988 (s 66); Public Trustee 1915.
- **PART, a row exists but the question is outside it** (8 further Acts, and four from the list above): CPF 1953 (rates, allocation, housing, HPS, DPS, CPF LIFE); Infectious Diseases 1976 (vaccination); Road Traffic 1961 (licensing, registration, COE); Town Councils 1988 (s 51 levy); Animals and Birds 1965 (licensing); Environmental Public Health 1987 (crematoria); Stamp Duties 1929 (leases, remission); Electricity, Public Utilities and Gas (billing); Land Titles 1993 (joint tenancy); Employment Act 1968 (ss 84-87A, pre-2015 confinements); Women's Charter 1961 (notice of marriage, solemnisation, spouses' property); Education Endowment and Savings Schemes 1992 (Edusave).
- **NONE, source deposited, no row** (7): Singapore Examinations and Assessment Board 2003; NUS (Corporatisation) 2005; Conveyancing and Law of Property 1886; Census 1973; Skills and Workforce Development Agency 2026; Lifelong Learning Endowment Fund 2001; Pioneer Generation and Merdeka Generation Funds 2014.

The largest hole is now inside an encoded Act rather than beside one: the CPF Act row stops before the contribution rates, the allocation rules, the housing and education withdrawals, Home Protection, Dependants' Protection and CPF LIFE, which between them are what Simone asks about most often from her first payslip to her last payout. The Women's Charter row, which landed today, settles who may marry but not how the marriage is contracted. [`GAPS.md`](GAPS.md) ranks the rest.

## Sample prompts for the chat demo

Each is something Simone would type, with the row that should answer it.

1. "I started work on 3 August. When can I first take annual leave, and how many days do I have?" — Employment Act s 88A.
2. "My payslip shows $840 CPF. Is that right, and where does it go?" — CPF Act s 7 for the duty; the rates and allocation are supplied facts, and the assistant must say so.
3. "Do I need to file a tax return for 2026?" — Income Tax Act s 39, Second Schedule: chargeable income $15,800, nil tax.
4. "Marcus and I want to apply for a BTO before the wedding. Are we allowed to?" — HDA s 50(1) answers the property test; the fiancé/fiancée scheme and income ceiling are HDB policy, and the assistant must say so.
5. "We filed notice of marriage on 20 April. How soon can we marry, and how long is the notice good for?" — Women's Charter ss 14-15: the row answers the age and consent questions (ss 9, 17(2), 21A) but not the notice period, and the assistant should say so and quote the source text for ss 14-15.
6. "I'm due on 5 September. When can I start maternity leave, and who pays?" — Employment Act s 76; CDCSA ss 9-10.
7. "How many weeks of leave can Marcus take, between paternity and shared parental leave?" — CDCSA ss 12H, 12DA-12DD.
8. "What will Kai En get from the Child Support Package over his childhood?" — child-support row: Baby Gift $10,000, Child Credits $32,000, First Step Grant $5,000, co-matching up to $5,000, PSEA top-up $10,000 — flagged as announced policy.
9. "How much stamp duty on our $420,000 flat?" — SDA Art 3(a)(iv): $7,200, ABSD nil.
10. "Can we sell the flat in 2036?" — HDA s 55 with the prescribed MOP as a fact.
11. "Can we buy a seven-year-old EC?" — EC Act ss 5, 9, 10.
12. "Dad died yesterday. What do I have to do this week?" — RBDA ss 19-23; then the succession row for the will and grant; CPF s 25 for his nomination.
13. "Mum had no will. Who gets her flat?" — ISA s 7.
14. "I'm 55 next month. What can I take out?" — CPF Act s 15.
15. "Do I get the Merdeka Generation Package?" — a negative by birth year; the Act has no row, and the assistant should say the answer is no on the published criteria.
