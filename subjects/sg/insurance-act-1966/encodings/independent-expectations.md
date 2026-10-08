# Independent expectations: Insurance Act 1966 (Singapore)

Written from `../source/IA1966.txt` and `BRIEF.md` only, before any `.l4` module was opened.
These values are fixed. They are not changed after the encoding is read, whatever it says.

Conventions: amounts are S$; imprisonment in years (12 months = 1 year). "corp" = a corporation
(any person other than an individual); "ind" = an individual. "REFUSE" means the Act does not
answer the question and the right output is a refusal, not a value. Where the reading is
genuinely open, the note says so and the expectation records the reading I think is right.

## A. Licensing and authorisation (ss 3, 4)

| # | Scenario | Expected | Provision |
|---|---|---|---|
| E001 | Unlicensed company carries on general business in Singapore as insurer | contravenes s 4(1) | s 4(1) |
| E002 | Company licensed for general business only carries on life business | contravenes s 4(1) (licence is per class) | s 4(1) |
| E003 | Company licensed for life business carries on short-term A&H business with no general licence | permitted; treated as life business | s 4(3)(a),(b) |
| E004 | Company licensed for life business carries on general business other than short-term A&H (e.g. motor) | contravenes s 4(1) | s 4(1), 4(3) |
| E005 | Offshore reinsurer: all reinsurance activities outside Singapore, no commercial/physical presence, only collects premiums in Singapore | not carrying on insurance business in Singapore | s 3(6) |
| E006 | Offshore reinsurer, not authorised, reinsures Singapore persons under an arrangement it solicited | contravenes s 4(2) | s 4(2) |
| E007 | Same, but authorised under s 42 | permitted | s 4(2)(a) |
| E008 | Same, unauthorised, arrangement not solicited and initiated by a licensed insurer | permitted | s 4(2)(b)(i) |
| E009 | Same, initiated by a registered insurance broker | permitted | s 4(2)(b)(ii) |
| E010 | Same, initiated by an exempt broker under s 92(1)(a)-(f) that has notified the Authority | permitted | s 4(2)(b)(iii) |
| E011 | Same, initiated by an exempt broker under s 92(1)(a)-(f) that has NOT notified the Authority | contravenes s 4(2) | s 4(2)(b)(iii) |
| E012 | Same, initiated by a s 92(1)(g) prescribed exempt broker | contravenes s 4(2) ((g) is not listed) | s 4(2)(b)(iii) |
| E013 | Licensed insurer providing reinsurance to persons in Singapore | outside s 4(2) (excepted) | s 4(2) opening words |
| E014 | Long-term A&H business is life business | TRUE | s 3(1)(a) |

## B. Holding out, "insurance", co-branding, solicitation, representative offices (ss 5-9)

| # | Scenario | Expected | Provision |
|---|---|---|---|
| E015 | Unlicensed person holds itself out as licensed insurer for life business | offence | s 5(1)(a) |
| E016 | Director of that corporation, who cannot prove lack of knowledge/consent | also guilty | s 5(1)(b) |
| E017 | Director who proves offence committed without his knowledge or consent | not guilty | s 5(1)(b) |
| E018 | Non-insurer uses "insurance" in its business name, no written consent | contravenes s 6(1) | s 6(1) |
| E019 | Same, with Authority's written consent | permitted | s 6(1) |
| E020 | Registered representative office (s 9(9) registered person) uses "insurance" | s 6(1) does not apply | s 6(3) |
| E021 | Association of insurers uses "insurance" in its name | permitted | s 6(6) |
| E022 | Licensed insurer uses "insurance" | permitted (excluded from s 6(1)) | s 6(1) |
| E023 | Registered insurance broker uses "insurance" in name indicating intermediary business, indicates it is an intermediary | permitted | s 6(4)(a), 6(5) |
| E024 | Insurance agent operating under a s 64 written agreement uses intermediary name | permitted | s 6(4)(d) |
| E025 | Unregistered, non-exempt person uses "insurance" indicating intermediary business, no consent | contravenes s 6(2) | s 6(2) |
| E026 | Licensed insurer co-brands with a foreign insurer that is not licensed/authorised/scheme, no prior written consent | contravenes s 7(1); max fine $100,000, $10,000/day | s 7 |
| E027 | Same with prior written consent | permitted | s 7(1) |
| E028 | Person solicits in Singapore for an insurer not licensed, authorised, under scheme, or otherwise entitled | contravenes s 8(1) | s 8(1) |
| E029 | Person solicits for a licensed insurer's branch outside Singapore | contravenes s 8(2)(b)(i) | s 8(2) |
| E030 | Person solicits for the head office of a foreign-incorporated licensed insurer | contravenes s 8(2)(b)(ii) | s 8(2) |
| E031 | Advertising publisher who received ad in ordinary course, did not devise it, had no reason to believe offence | not guilty | s 8(4) |
| E032 | Person operates unregistered representative office | offence: ind $50,000 / 2 years / $5,000 per day; corp $100,000 / $10,000 per day | s 9(1), 9(8) |
| E033 | Authority registers a representative office for an applicant that is an individual | must refuse (applicant must be a company) | s 9(3)(a) |

## C. Intermediaries and brokers (ss 64, 66, 70, 75, 83-86, 90-92)

| # | Scenario | Expected | Provision |
|---|---|---|---|
| E034 | Insurance agent arranges a contract for a licensed insurer without written agreement | contravenes s 64(1) | s 64(1) |
| E035 | Agent with written agreement covering a class including that contract | permitted | s 64(1)(c) |
| E036 | Employee of the licensed insurer arranging in course of duties, no agreement | s 64(1)/(2) do not apply | s 64(3) |
| E037 | Licensed financial adviser arranges a life policy (not reinsurance) for a licensed insurer, no agreement | s 64(1) does not apply | s 64(4)(a) |
| E038 | Licensed financial adviser arranges a general (motor) policy, no agreement | contravenes s 64(1) | s 64(4) limited to life policies |
| E039 | Licensed insurer arranges a life reinsurance contract as agent for another licensed insurer, no agreement | contravenes s 64(1) (reinsurance excluded from s 64(5)) | s 64(5) |
| E040 | Licensed insurer arranges a (direct) life policy as agent for another licensed insurer, no agreement | s 64(1) does not apply | s 64(5) |
| E041 | s 64 offence max: ind $25,000 / 12 months / $2,500 per day; corp fine doubled to $50,000 | as stated | s 64(7), 143(1) |
| E042 | Insured pays premium to the intermediary that arranged the contract | discharges insured's liability to that extent | s 66(1) |
| E043 | Insurer pays claim moneys to the intermediary | does NOT discharge insurer's liability to insured | s 66(3) |
| E044 | Agreement purporting to make insurer's payment to intermediary a discharge | void | s 66(4) |
| E045 | Person acts as agent for an insurer for business the insurer is not entitled to carry on in Singapore, no approval | offence: $25,000 or 3 years or both; corp $50,000 | s 70, 143(1) |
| E046 | Same with Authority's approval | permitted | s 70(1) |
| E047 | Unregistered, non-exempt person carries on business as insurance broker | offence: $75,000 / 3 years / $7,500 per day; corp fine $150,000 | s 75, 143(1) |
| E048 | Bank licensed under Banking Act carries on broking business, unregistered | permitted (exempt) | s 75(1)(b), 92(1)(a) |
| E049 | Registered broker negotiates direct (non-reinsurance) Singapore risk with unlicensed insurer, no permission | contravenes s 83(1) | s 83 |
| E050 | Same but the contract is reinsurance | not caught | s 83(2)(a) |
| E051 | Same but the risk is outside Singapore | not caught | s 83(2)(b) |
| E052 | Same with Authority's s 84 permission | permitted | s 84 |
| E053 | Same, insurer is a foreign insurer under a scheme, broker holds s 85 licence | permitted | s 85(1) |
| E054 | Broker remuneration varied solely by number of contracts | prohibited | s 86(1)(a) |
| E055 | Profit commission | permitted | s 86(2) |
| E056 | s 86 offence max: ind $50,000 / 12 months / $5,000 per day | as stated | s 86(3) |
| E057 | Person holds itself out as registered direct insurance broker when not | offence: $50,000 / 12 months / $5,000 per day | s 90 |
| E058 | Non-broker uses "life insurance broking" | s 91 does not apply | s 91(3) |
| E059 | Non-broker uses "insurance broking" | contravenes s 91(1); $12,500 + $1,250/day | s 91 |

## D. Ownership and control (ss 26, 27, 34, 35, 36, 37, 87, 89)

| # | Scenario | Expected | Provision |
|---|---|---|---|
| E060 | Person with associates holds exactly 20% of issued shares of a Singapore-incorporated licensed insurer | effective control | s 26(7)(a)(i)(A) |
| E061 | Holds 19% of shares and 19% of votes, no other indicia | not effective control | s 26(7)(a) |
| E062 | Controls 20% of voting power, 5% of shares | effective control | s 26(7)(a)(i)(B) |
| E063 | Holds 0% but directors accustomed to act on its wishes | effective control | s 26(7)(a)(ii) |
| E064 | Directors act on its wishes only because it gives professional advice | not effective control | s 26(7)(b)(ii) |
| E065 | Person is an approved director of the insurer | not regarded as obtaining effective control | s 26(7)(b)(i) |
| E066 | Obtains effective control without prior approval: penalty | ind $125,000 / 3 years / $12,500 per day; corp $250,000 / $25,000 per day | s 26(6) |
| E067 | Agreement to act together over 5% of votes, no approval | contravenes s 27(2) | s 27(2) |
| E068 | Same over 4.9% | not caught | s 27(2) |
| E069 | s 27(7) penalty for individual | fine $125,000, NO imprisonment; $12,500 per day | s 27(7)(a) |
| E070 | s 27(8) (breach of approval condition) individual | $125,000 or 3 years or both | s 27(8)(a) |
| E071 | Whether a person is a substantial shareholder | input (Companies Act), not computed | s 27(9), BRIEF |
| E072 | Singapore-incorporated insurer holds exactly 10% of a corporation's shares | not a major stake | s 34(9)(a)(i) |
| E073 | Holds 10.01% | major stake; needs prior approval | s 34(1), (9) |
| E074 | Controls 11% of voting power | major stake | s 34(9)(a)(ii) |
| E075 | Interest held by way of security in ordinary course | s 34 does not apply | s 34(6)(a) |
| E076 | Foreign-incorporated insurer holds 15% not as insurance-fund assets | not caught by s 34(2) | s 34(2) |
| E077 | s 34 contravention max fine | $250,000 + $25,000/day | s 34(8) |
| E078 | Agreement under which person would hold 20% of a registered broker's capital, no approval | contravenes s 87(2); $25,000 / 2 years; corp $50,000 | s 87 |
| E079 | Same at 19% | not caught | s 87(3)(a) |
| E080 | Licensed insurer appoints chief executive without approval | contravenes s 35(4); $100,000 + $10,000/day | s 35(4),(16) |
| E081 | Re-appointment of approved key executive immediately on expiry, no fresh approval | permitted | s 35(8) |
| E082 | Foreign-incorporated insurer appoints a director without approval | s 35(5) does not apply | s 35(5) |
| E083 | Failure to comply with s 35(10) removal direction | $250,000, no daily fine | s 35(17) |
| E084 | Singapore-incorporated insurer lets an undischarged bankrupt act as director, no consent | contravenes s 36(1)(b) | s 36(1)(d) |
| E085 | Same with Authority's prior written consent | permitted | s 36(1) |
| E086 | Foreign-incorporated insurer lets undischarged bankrupt act as director (not executive officer) | not caught | s 36(1)(b) |
| E087 | Person convicted of an offence not involving fraud/dishonesty and not in Third Schedule, no other ground | not disqualified | s 36(1)(c) |
| E088 | Unsecured loan to insurer's director of $5,000 | permitted | s 37(1)(a) |
| E089 | Unsecured loan to insurer's director of $5,001 | prohibited | s 37(1)(a) |
| E090 | $6,000 unsecured loan to a director's wife | prohibited (wife is a "director") | s 37(2) |
| E091 | Unsecured loan to employee equal to one year's emolument | permitted | s 37(1)(b) |
| E092 | Unsecured loan to employee exceeding one year's emolument | prohibited | s 37(1)(b) |
| E093 | s 37 breach by corporate insurer: max fine (no own penalty) | default s 142(3): $100,000 + $10,000/day | s 142(3) |
| E094 | Broker: unsecured loan of $1,000 to a non-employee director | prohibited (no $3,000 allowance for (a)) | s 89(1)(a) |
| E095 | Broker: unsecured loan of $3,000 to an employee | permitted | s 89(1)(b) |
| E096 | Broker: unsecured loan of $3,001 to an employee | prohibited | s 89(1)(b) |
| E097 | s 89 offence max | $12,500 + $1,250/day | s 89(3) |

## E. Funds and premiums (ss 16, 22)

| # | Scenario | Expected | Provision |
|---|---|---|---|
| E098 | Bonus allocation $900,000; allocation to surplus account $100,000 (directors approved on actuary's recommendation, solvency met) | permitted (= 1/9th) | s 16(7)(c)(iv) |
| E099 | Same but $100,001 | not permitted | s 16(7)(c)(iv) |
| E100 | Cap computed: 1/9 of $900,000 | $100,000 | s 16(7)(c)(iv) |
| E101 | Withdrawal not exceeding surplus over FSR, no instrument disallows, latest accounts show surplus | permitted | s 16(10) |
| E102 | Same but an instrument binding the insurer disallows it | not permitted | s 16(10)(a) |
| E103 | Withdrawal exceeding the surplus over FSR | not permitted | s 16(10) |
| E104 | Life policy issued at a premium not per actuary-approved rates | offence; $25,000 per occasion | s 22(1),(4) |
| E105 | Premium at actuary-approved rates | permitted | s 22(1) |

## F. Penalties general (ss 142-145)

| # | Scenario | Expected | Provision |
|---|---|---|---|
| E106 | s 4(5) individual max | $125,000 / 3 years / $12,500 per day | s 4(5)(a) |
| E107 | s 4(5) corporation max | $250,000 / $25,000 per day; s 143 doubling does NOT apply (split penalty) | s 4(5)(b), 143(2)(b) |
| E108 | s 6(7) individual / corp | $12,500 / 12 months / $1,250; corp $25,000 / $2,500 | s 6(7) |
| E109 | s 142(1) false document, individual / corp | $125,000 / 3 years; corp $250,000, no daily | s 142(2) |
| E110 | s 142(3) default, individual | $50,000 / 2 years / $5,000 per day | s 142(3)(a) |
| E111 | s 124(2) corp | $250,000 (2 x $125,000) | s 124(2), 143(1) |
| E112 | s 143 doubling not for offences of duty imposed only on corporations (e.g. registered broker s 88(8), brokers must be companies) | $150,000, not doubled | s 143(2)(a), 77(1)(a) |
| E113 | Director convicted under s 142(4) of a corporations-only-duty offence (s 88(8)) | fine $150,000 + imprisonment up to 2 years | s 142(5), 143(3) |
| E114 | Composition of a compoundable offence: s 4(5) corp | at most $125,000 | s 142(7) |
| E115 | Composition: s 6(7) individual | at most $6,250 | s 142(7) |
| E116 | Composition of an offence not prescribed as compoundable | not available | s 142(7) |
| E117 | District/Magistrate's Court jurisdiction and full penalty for any IA offence (e.g. s 4) | TRUE | s 144 |
| E118 | Act wholly outside Singapore, substantial foreseeable effect in Singapore, would be s 75 offence | guilty as if in Singapore | s 145(2) |
| E119 | Same but the offence would be s 6 | s 145(2) does not reach it | s 145(2)(b) |
| E120 | Act partly in, partly outside Singapore, would be s 6 offence | guilty | s 145(1) |

## G. Supervision timing (ss 13, 44, 80, 19, 30, 96, 97, 107, 117-119, 127)

| # | Scenario | Expected | Provision |
|---|---|---|---|
| E121 | Authority informs insurer of cancellation (not at its request) on 2026-03-02; on 2026-03-20, no appeal | not yet in effect | s 13(6) |
| E122 | Same, on 2026-04-15, no appeal | in effect | s 13(6) |
| E123 | Appeal lodged 2026-03-25 | in time | s 13(7) |
| E124 | Appeal lodged 2026-04-10 | out of time | s 13(7) |
| E125 | In-time appeal pending, on 2026-05-01 | not in effect | s 13(8) |
| E126 | Licensed 2025-01-01, not commenced by 2026-03-01 | ground under s 13(3)(a) | s 13(3)(a) |
| E127 | Licensed 2025-01-01, not commenced at 2025-10-01 | not a ground | s 13(3)(a) |
| E128 | Broker registered 2025-01-01, not commenced by 2025-08-01 | ground under s 80(2)(a) | s 80(2)(a) |
| E129 | Broker registered 2025-01-01, not commenced at 2025-05-01 | not a ground | s 80(2)(a) |
| E130 | Person with associates holds 20% of insurer shares | "control" for s 13(3)(g) | s 13(10) |
| E131 | 19% shares, 19% votes | not control | s 13(10) |
| E132 | Person holds 50% of reinsurer capital | control for s 44(2)(f) | s 44(9) |
| E133 | Person holds 49% / 49% votes | not control | s 44(9) |
| E134 | s 19(3) notice of 10 days | not a valid notice (at least 14) | s 19(3) |
| E135 | s 30 defence: aware 2026-02-01, notified 2026-02-10 | within 14 days | s 30(1)(b) |
| E136 | s 30: aware 2026-02-01, notified 2026-02-20 | not within 14 days | s 30(1)(b) |
| E137 | s 96(1) notice giving 10 days for explanations | invalid (at least 14 days) | s 96(1) |
| E138 | s 97(1): application received 2026-02-01, copies despatched 2026-02-20 | late (14 days) | s 97(1) |
| E139 | s 97(4): document lodged 11 years ago | no inspection right | s 97(4) |
| E140 | s 107 order made 2026-01-10; on 2026-08-01 | cannot still be valid (max 6 months) | s 107(3) |
| E141 | s 107 order made 2026-01-10; on 2026-06-01 | can still be valid | s 107(3) |
| E142 | s 118(1)(b): scheme lodged 2026-01-05, Gazette notice 2026-01-20 | too early (not earlier than one month) | s 118(1)(b) |
| E143 | Gazette notice 2026-02-10 | compliant | s 118(1)(b) |
| E144 | s 118(3): transmitted 2026-03-01, application 2026-03-10 | non-compliant (at least 15 days) | s 118(3) |
| E145 | s 119(1): scheme effective 2026-04-01, lodged 2026-05-15 | late (one month) | s 119(1) |
| E146 | s 127(2): appeal received 2026-03-02; AAC constituted 2026-04-05 | late (28 days) | s 127(2) |
| E147 | s 127(2): appeal under s 11(7) | no AAC requirement | s 127(2) |
| E148 | s 111: all of (a)-(i) satisfied | may assist | s 111(1) |
| E149 | s 111: request received before 8 Jan 2002, rest satisfied | may not | s 111(1)(a) |
| E150 | s 111: no written undertaking under (d) | may not | s 111(1)(d) |

## H. s 123 winding-up priority

| # | Scenario | Expected | Provision |
|---|---|---|---|
| E151 | Ranks: levy 1, protected liabilities 2, unprotected direct-policy liabilities 3, reinsurance 4, resolution-fund claims 5 | as stated | s 123(3) |
| E152 | Assets $100 for a class whose claims total $200: claim of $50 | paid $25 (equal abatement) | s 123(4)(b) |
| E153 | Assets sufficient: claim paid in full | full | s 123(4)(b) |
| E154 | Preferential debts under IRDA s 203(1) | rank ahead of the s 123(3) liabilities | s 123(2) |

## I. Policies: First Schedule, ss 66, 146-151

| # | Scenario | Expected | Provision |
|---|---|---|---|
| E155 | Singapore citizen, resided outside continuously 6 years before proposal, not currently residing | not ordinarily resident | FS 2(4)(a)(i) |
| E156 | Singapore citizen, abroad 6 years but currently residing in Singapore | ordinarily resident | FS 2(4)(a)(i) |
| E157 | Citizen abroad 3 years | ordinarily resident | FS 2(4)(a)(i) |
| E158 | PR, 150 days in Singapore in preceding 12 months | not ordinarily resident | FS 2(4)(a)(ii) |
| E159 | PR, 183 days | ordinarily resident | FS 2(4)(a)(ii) |
| E160 | Work pass holder, 182 days | not ordinarily resident | FS 2(4)(a)(iii) |
| E161 | Work pass holder, 200 days | ordinarily resident | FS 2(4)(a)(iii) |
| E162 | Immigration pass of 180-day duration, 90 continuous days | ordinarily resident | FS 2(4)(a)(iv) |
| E163 | Same, 89 continuous days | not ordinarily resident | FS 2(4)(a)(iv) |
| E164 | Pass of exactly 90 days' duration, 90 continuous days | not ordinarily resident ("longer than 90 days") | FS 2(4)(a)(iv) |
| E165 | Individual-owned life policy, owner not OR but insured is OR | Singapore policy | FS 2(1)(a)(i) |
| E166 | Individual-owned life policy, neither OR | offshore policy | FS 2(1)(a), 2(3) |
| E167 | Treaty general reinsurance, 25% of gross premiums from Singapore risks | not Singapore policy | FS 2(1)(c) |
| E168 | Treaty general reinsurance, 26% | Singapore policy | FS 2(1)(c) |
| E169 | Treaty life reinsurance, 30% | Singapore policy | FS 2(1)(d) |
| E170 | Direct general, risk arises in Singapore, insured non-resident company | Singapore policy | FS 2(1)(b) |
| E171 | Cargo from outside to outside Singapore, resident individual insured | not Singapore policy | FS 2(2) |
| E172 | A&H policy can run >5 years, insurer may terminate only for fraud/non-disclosure | long-term A&H | FS 9(1) |
| E173 | A&H policy can run >5 years but insurer may terminate unilaterally at will | short-term A&H | FS 9(1)(b), 10 |
| E174 | A&H policy of 3 years only because of insured's age, no unilateral termination | long-term | FS 9(2) |
| E175 | A&H policy 2 years with insured's option to extend to 8 years | long-term (option assumed exercised) | FS 9(3) |
| E176 | A&H policy 2 years, no option, not due to age | short-term | FS 9, 10 |
| E177 | Life policy on own life | not void | s 146(1)(b)(i) |
| E178 | Life policy on spouse | not void | s 146(1)(b)(ii) |
| E179 | Life policy on own child aged 16 | not void | s 146(1)(b)(iii) |
| E180 | Life policy on adult sibling, no insurable interest, not dependant, not trust | void | s 146(1) |
| E181 | Insurable interest $100,000 (s 146(1)(a)), sum assured $150,000 | moneys capped at $100,000 | s 146(2) |
| E182 | Trust: life of settlor, trustee effects, beneficiary is settlor's spouse, settlor consented in writing | not void | s 146(3) |
| E183 | Same without settlor's written consent, no other basis | void | s 146(3)(d), 146(1) |
| E184 | Insurance on event in which beneficiary has no interest (non-indemnity) | void | s 151(1) |
| E185 | Age 12, no parental consent | lacks capacity | s 147(1) |
| E186 | Age 12 with written parental consent | has capacity | s 147(1) |
| E187 | Age 17 | has capacity (age no bar) | s 147(1) |
| E188 | Age 8 | Act does not answer: REFUSE | s 147(1) silent below 10 |
| E189 | Life policy in force 3 years: surrender right | TRUE | s 149(1) |
| E190 | In force 2 years 11 months | no statutory surrender right | s 149(1) |
| E191 | Replacement policy, earlier policy began 4 years ago | treated as in force 4 years: right exists | s 149(4) |
| E192 | Annuity for a term dependent on human life, in force 5 years | s 149(1)-(3) do not apply | s 149(5)(a) |
| E193 | Deduction from life policy moneys for sums not due, no consent | not permitted | s 148(1) |

## J. Nominations and payout (ss 131-133, 150)

| # | Scenario | Expected | Provision |
|---|---|---|---|
| E194 | Owner aged 30 nominates spouse and children, expresses trust intention, prescribed manner, all policy moneys | valid trust nomination | s 132(2),(3) |
| E195 | Owner aged 17 | not valid | s 132(2) |
| E196 | Trust nomination of a sibling | not a s 132 trust nomination | s 132(2)(a) |
| E197 | Trust nomination disposing of 80% of policy moneys | not valid | s 132(3) |
| E198 | Revocation: trustee other than owner consents; nominees do not | valid revocation (if prescribed requirements met) | s 132(7)(a)(i) |
| E199 | Revocation: no outside trustee, two adult nominees, only one consents | void | s 132(7)(b), (10) |
| E200 | Revocation: no outside trustee, all adult nominees consent | valid | s 132(7)(b) |
| E201 | Minor nominee: consent given by the policy owner as parent | not sufficient | s 132(7)(b)(ii) |
| E202 | Revocable nomination, owner 18, all death benefits | valid | s 133(2),(3) |
| E203 | Revocable nomination for 90% of death benefits | invalid | s 133(3) |
| E204 | Nominees A 50, B 30, C 20; C predeceases; A's new portion | 62.5 (50 + 50/80 x 20) | s 133(5)(c) |
| E205 | B's new portion | 37.5 | s 133(5)(c) |
| E206 | Nominees A 60, B 40; B predeceases | A takes 100 | s 133(5)(b) |
| E207 | All nominees predecease | nomination deemed revoked | s 133(5)(a) |
| E208 | Owner (60) and nominee (30) die together, order uncertain | nominee deemed to survive owner | s 133(6) |
| E209 | Owner assigns the policy | nomination deemed revoked | s 133(7)(a) |
| E210 | Later will disposing of all death benefits and specifying prescribed particulars | nomination deemed revoked | s 133(7)(b) |
| E211 | Later will NOT specifying policy particulars | nomination not revoked | s 133(7)(b)(ii) |
| E212 | Last nomination unrevoked, a will exists | per nomination | s 133(8)(a) |
| E213 | Nomination revoked, last will unrevoked | per will | s 133(8)(b) |
| E214 | Nomination revoked, will revoked | Intestate Succession Act | s 133(8)(c) |
| E215 | Intestate, nomination revoked | Intestate Succession Act | s 133(9)(b) |
| E216 | Unrevoked trust nomination exists | s 133 does not apply | s 133(1) |
| E217 | s 150(11): claims 60,000 and 40,000, prescribed C = 50,000: first claim | 30,000 | s 150(11)(b) |
| E218 | Second claim | 20,000 | s 150(11)(b) |
| E219 | Nephew of the deceased | proper claimant | s 150(12) |
| E220 | Cousin of the deceased (not executor) | not proper claimant | s 150(12) |
| E221 | s 150(8): payment to personal representatives of a nominee who died after the owner | permitted | s 150(8)(f) |
