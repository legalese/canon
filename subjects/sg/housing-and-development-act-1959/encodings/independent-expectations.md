# Independent expectations: Housing and Development Act 1959

Written from `../source/HDA1959.txt` and `BRIEF.md` alone, before any `.l4` file was opened.
Each expectation names its provision. These values are fixed and are not to be changed after the encoding is read.

Conventions: "A" = application date, "C" = completion date. Ages are whole years. Where the source is genuinely ambiguous, the expectation records the reading chosen and is marked (interpretive).

## Buying a flat: s 50(1), (10), s 57, s 92(1)

- E01 s 50(1): applicant, spouse and authorised occupiers own nothing and have sold nothing → entitled to purchase.
- E02 s 50(1)(a): applicant owns another flat → not entitled.
- E03 s 50(1)(a): applicant's spouse has an interest in other land → not entitled.
- E04 s 50(1)(a): an authorised occupier owns a house → not entitled.
- E05 s 50(1)(b): A = 1 Jan 2026; applicant sold a flat on 2 Jul 2023 (inside 30 months before A) → not entitled.
- E06 s 50(1)(b): A = 1 Jan 2026; sale on 30 Jun 2023 (more than 30 months before A) → entitled.
- E07 s 50(1)(b): A = 1 Jan 2026; sale on 1 Jul 2023 (exactly 30 months before A) → not entitled (interpretive: the window includes its first day).
- E08 s 50(1)(b): sale on 31 Dec 2025, the day before A → not entitled.
- E09 s 50(1)(b): A = 1 Jan 2026, C = 1 Jan 2029, sale on 1 Jun 2027 (between A and C) → not entitled.
- E10 s 50(1)(b): sale on 2 Jan 2029, after C (1 Jan 2029), nothing owned → entitled.
- E11 s 50(1)(b): spouse divested an interest in land 12 months before A → not entitled.
- E12 s 50(10): applicant owns another flat, but the Board has exempted the applicant → entitled.
- E13 s 57(1): a body corporate declared by Minister's order in the Gazette → entitled despite s 50.
- E14 s 57 / s 50: a body corporate with no order → not entitled under s 57 (no declaration).
- E15 s 92(1)(a): applicant entitled under Part 4 and spouse entitled → eligible to buy from approved developer.
- E16 s 92(1)(a): spouse not entitled under Part 4, Minister has not allowed → not eligible.
- E17 s 92(1): spouse not entitled, but Minister allows → eligible.

## Cancellation of application: s 50(12)

- E18 s 50(12)(a): innocent misrepresentation of a material fact in the application → Board may cancel.
- E19 s 50(12)(b): listed occupier aged 15 convicted under s 336 Penal Code for throwing things from Board property → Board may cancel.
- E20 s 50(12)(b): listed occupier aged 14 so convicted → no ground under (b) ("above the age of 14 years"; interpretive with whole years).
- E21 s 50(12)(b): applicant convicted under a Penal Code section not listed (e.g. s 323) → no ground under (b).
- E22 s 50(12)(c): CPF cash grant used and applicant refuses to return it when required → may cancel.
- E23 s 50(12)(d): spouse convicted of harbouring an immigration offender → may cancel.
- E24 s 50(12): none of (a)-(d) → no ground to cancel.

## Dealings: s 55, s 56, s 52(3)

- E25 s 55(1): sale agreed within MOP without the Board's prior written consent → prohibited.
- E26 s 55(1): sale within MOP with the Board's prior written consent → not prohibited by s 55(1).
- E27 s 55(1): sale agreed after MOP has ended, prescribed form used → not prohibited.
- E28 s 55(2): contract with a non-Board purchaser not in prescribed form and not authorised → contravenes s 55(2).
- E29 s 55(3): contravening contract made on 20 Nov 1998 → void.
- E30 s 55(3): contravening contract made on 19 Nov 1998 → not void under s 55(3).
- E31 s 55(2): purchaser is the Board, form not prescribed → no contravention of s 55(2).
- E32 s 56(1): sold flat mortgaged without prior written consent → not permitted.
- E33 s 56(1): leased with the Board's prior written consent → permitted.
- E34 s 52(3): lessee uses flat for a purpose not permitted by lease without prior written approval → prohibited.
- E35 s 52(3): same use with prior written approval → permitted.

## Protected property: s 58

- E36 s 58(1): agreement to use the flat as collateral for a private lender → void.
- E37 s 58(4)(b): security in favour of an approved financial institution (licensed bank) → not void.
- E38 s 58(4)(a): security in favour of the Board → not void.
- E39 s 58(1),(12): collateral over the proceeds of sale of the flat for a private lender → void.
- E40 s 58(6): sole owner is a citizen and becomes bankrupt → flat does not vest in Official Assignee.
- E41 s 58(8): sole owner is not a citizen → s 58(6) does not apply (flat can vest in the Official Assignee).
- E42 s 58(8): two joint owners, one citizen and one non-citizen → s 58(6) protection still applies.
- E43 s 58(8): two joint owners, both non-citizens → s 58(6),(7) do not apply.
- E44 s 58(7): judgment creditor (unsecured) seeks attachment, citizen owner → not attachable.
- E45 s 58(7)(a): mortgagee under mortgage made with the Board's prior written consent → attachable.
- E46 s 58(9),(10): trust created without the Board's prior written approval → void.
- E47 s 58(9): trust created with prior written approval → not void.
- E48 s 58(11): claim under a resulting trust → no entitlement.

## Death of owner: s 59

- E49 s 59(1): transmission registration without the Board's written consent → not permitted.
- E50 s 59(3)(a): no representation 13 months after death → Board may vest.
- E51 s 59(3)(a): no representation 11 months after death → not under (a).
- E52 s 59(3)(b): representation taken; PRs haven't applied for consent 7 months after representation → Board may vest.
- E53 s 59(3)(b): 5 months after representation, no application → not under (b).
- E54 s 59(3)(c): consent given; sale not completed 13 months after consent → Board may vest.
- E55 s 59(3)(c): 11 months after consent, not completed → not under (c).
- E56 s 59(4)(a): owner's lease unregistered at death → Board may rescind agreement for lease.

## Re-entry: s 62(1)

- E57 s 62(1)(a): rent unpaid 3 calendar months after payable, demand sent by registered post → may re-enter.
- E58 s 62(1)(a): rent unpaid 2 months (less than 3 calendar months), demand sent → not under (a).
- E59 s 62(1)(a): rent unpaid 4 months but no registered-post demand → not under (a).
- E60 s 62(1)(c): remediable breach not remedied 2 weeks (14 days) after notice → may re-enter.
- E61 s 62(1)(c): only 13 days after notice → not under (c).
- E62 s 62(1)(b): breach of condition against underletting and notice sent by registered post → may re-enter.
- E63 s 62(1)(d): false statement in application form → may re-enter.
- E64 s 62(1)(f): unauthorised use without prior written approval → may re-enter.
- E65 s 62(1)(e): in the Board's opinion a breach of s 74(1)(g) rules → may re-enter.

## Compulsory acquisition: s 63

- E66 s 63(1)(a): owner and spouse have, in the Board's opinion, ceased to occupy → may acquire.
- E67 s 63(1)(b): spouse acquires another flat → may acquire.
- E68 s 63(2): owner bought commercial property worth $250,000, with prior written consent, used for business → (1)(b) does not apply.
- E69 s 63(2): same but worth $250,001 and Minister has not allowed a higher value → (1)(b) applies → may acquire.
- E70 s 63(2): commercial property worth $200,000 but bought without prior written consent → (1)(b) applies.
- E71 s 63(2): $200,000, consent, but not used or intended for business → (1)(b) applies.
- E72 s 63(1)(d): owner lets a person who is not an authorised occupier stay → may acquire.
- E73 s 63(1)(j): owner ceased to be a citizen → may acquire.
- E74 s 63(1)(k): mortgage instalment unpaid 3 calendar months after due and notice of demand sent → may acquire.
- E75 s 63(1)(k): unpaid only 2 months → not under (k).
- E76 s 63(1)(m): authorised occupier aged 15 convicted on 1 Jun 2020 of s 336 throwing from Board property → may acquire.
- E77 s 63(1)(m): authorised occupier aged 14 so convicted → not under (m) (interpretive, whole years).
- E78 s 63(1)(m): owner convicted on 28 Feb 1984 (before 1 Mar 1984) → not under (m).
- E79 s 63(1)(n): owner's spouse convicted of harbouring immigration offenders → may acquire.
- E80 s 63(1)(o): owner convicted after the appointed date of an abatement offence and previously convicted of an exclusion offence → may acquire.
- E81 s 63(1)(o): owner convicted of one abatement offence only, no other offence convicted, TIC or compounded → not under (o).
- E82 s 63(1)(o)(iii): owner convicted, and one other offence compounded under s 13U CDRA → may acquire.
- E83 s 63(1)(o): conviction before the appointed date → not under (o).
- E84 s 63(1): no ground at all → may not acquire.

## Financial penalty instead: s 74(1)(i)-(k)

- E85 s 74(1)(k): breach of s 63 on 20 Jul 2015, penalty $50,000 → within power.
- E86 s 74(1)(k): breach on 19 Jul 2015 → no power.
- E87 s 74(1)(k): penalty $50,001 → exceeds power.
- E88 s 74(1)(i): breach of s 50 on 1 Jan 2020, Board does not proceed under s 50, penalty $30,000 → within power.
- E89 s 74(1)(i): Board does proceed under s 50 → no power under (i).
- E90 s 74(1)(j): breach of s 62 on 1 Jan 2020, Board does not proceed under s 62, $50,000 → within power.

## Periods

- E91 s 50(3A): notice served 1 Mar 2026 → earliest vesting/termination after 14 days, i.e. 15 Mar 2026; not on 14 Mar.
- E92 s 50(4): appeal to Minister within 14 days after service (deadline 15 Mar 2026 for service 1 Mar 2026).
- E93 s 59(5A): 28 days after service of notice before lodging/rescinding.
- E94 s 59(6): appeal within 28 days.
- E95 s 63(5): objection within 28 days after service of notice.
- E96 s 63(7): appeal within 28 days after service of the Board's decision.
- E97 s 66(1)(a)(i): vesting on expiry of 28 days after service of s 63(3) notice where no objection.
- E98 s 68(1): possession on expiry of 30 days after service of notice.
- E99 s 69(2): delivery period at least 30 days; a 29-day notice period is non-compliant, 30 days compliant.
- E100 s 15(1): one month's notice to vary mortgage interest rate.
- E101 s 28(14): owner pays within one month after the date of the written notice unless the Board specifies another period.

## Upgrading: s 77, 80, 82, 84

- E102 s 77(4): 75% of total value in votes in favour → Board may (with approval) carry out general upgrading.
- E103 s 77(4): 74.99% → may not.
- E104 s 77(4): measured on total value in votes of all prescribed owners, not votes cast: 70 of 100 value votes in favour, 10 against, 20 not cast → 70% → may not.
- E105 s 77(5)(a): wholly residential building, 80% in favour of specified works, general works approved → may carry out specified works.
- E106 s 77(5)(a): general works not approved → may not carry out specified works under (5).
- E107 s 77(5)(b): mixed building, residential 80%, non-residential 76% → specified works in the whole building.
- E108 s 77(6): mixed building, residential 80%, non-residential 50% → only the residential part.
- E109 s 77(7): mixed building, residential 60% → the non-residential poll must not be conducted; no specified works.
- E110 s 77(8): special works, building poll 80% and, as proposed with general works, precinct poll 76% → may.
- E111 s 77(8)(b): building poll 80%, together with general works, precinct poll 70% → may not.
- E112 s 77(8)(a): stand-alone special works (no general works), building poll 75% → may.
- E113 s 80(1): improvement contribution payable not later than one month from demand.
- E114 s 82(1): unpaid 3 months after demand → charge on the flat arises on expiry.
- E115 s 82(1): unpaid only 2 months after demand → no charge yet.
- E116 s 82(4): sale only on expiry of 3 months from the notice of sale and if still unpaid.
- E117 s 82(5): owner has movable property on the flat sufficient (Board's estimate) to satisfy the debt → Board may not sell.
- E118 s 82(8): application order: (a) sale costs, (b) improvement contribution, (c) Town Council charges, (d) subsequent mortgages, (e) residue to owner.
- E119 s 84(8): after Minister's approval under s 77(4) or (5) → Board may compulsorily acquire a flat for the works; not on approval under s 77(9) alone.

## The Board

- E120 s 6(1): Chairperson + 4 other members → validly constituted; + 3 → not; + 14 → valid; + 15 → not.
- E121 s 6(4): appointment term of 3 years → permitted; 4 years → not.
- E122 s 7(1)(a): undischarged bankrupt → not eligible.
- E123 s 7(1)(b): convicted in Singapore, sentenced to 6 months, no pardon → not eligible; 5 months → eligible; 6 months with free pardon → eligible; convicted abroad → not disqualified by (b).
- E124 s 7(2)(b): misses 3 consecutive meetings without acceptable cause → office vacant; 2 meetings → not.
- E125 s 9(1): 12 members in office, 4 present including the Chairperson → quorum; 3 present → no quorum; 4 present but neither Chair nor Deputy → no quorum; 13 in office, 5 present incl. Deputy → quorum (one-third of 13 is 4.33, so 5 needed; 4 not enough).
- E126 s 98(1): budget forwarded by 15 Nov → in time; 16 Nov → late.
- E127 s 98(2): financial year ends 31 March.
- E128 s 45(4): CEO temporary appointment of 2 months → permitted; 3 months → not.

## Offences and penalties

- E129 s 13(2): max fine $2,000, max imprisonment 6 months, both allowed.
- E130 s 14(3): $2,000, 6 months, both.
- E131 s 70: $5,000, 6 months, both.
- E132 s 72(2): $2,000; continuing offence $100 per day after conviction; no imprisonment.
- E133 s 84(7): $5,000; continuing $100 per day; no imprisonment.
- E134 s 107: $5,000 or imprisonment up to 6 months; the wording omits "or to both" so both together are not authorised.
- E135 s 108(3) and (5): $2,000, 3 months, both.
- E136 s 31(2)(f): offence under general rules (not renovation rules) max fine $5,000.
- E137 s 31(3)(g): offence under renovation rules (s 31(2)(c)) max fine $20,000, imprisonment 12 months, both.

## Composition: s 32

- E138 s 32(1): max fine $2,000 → composition cap $1,000.
- E139 s 32(1): max fine $5,000 → $2,500.
- E140 s 32(1): max fine $10,000 → $5,000.
- E141 s 32(1): max fine $20,000 → $5,000.
- E142 s 32(1): offence not prescribed as compoundable → cannot be compounded.

## Financial penalties

- E143 s 31(2)(h): lessee penalty up to $5,000; $5,001 exceeds.
- E144 s 31(3)(f): renovation licensee penalty up to $10,000; $10,001 exceeds.
- E145 s 30(4): contravention that is an offence → no financial penalty; not an offence → penalty power exercisable.

## Parking: s 33

- E146 s 33(1): owner of the vehicle at the time → guilty as if actual offender.
- E147 s 33(1): vehicle stolen at the relevant time → owner not guilty.
- E148 s 33(3)(a): statutory declaration naming the driver within 7 days after service → owner not guilty (day 7 counts).
- E149 s 33(3)(a): declaration on day 8 → owner guilty (unless (b)/(c)).
- E150 s 33(5): one declaration covering two parking offences → does not count; owner guilty.
- E151 s 33(3)(b): owner satisfies the Board he could not ascertain the driver → not guilty.
- E152 s 33(2): penalty already recovered from the actual offender → no further penalty on the owner.

## Service: s 111

- E153 s 111(8)(c): registered post on 1 Mar 2026 → service effective 3 Mar 2026.
- E154 s 111(8)(a): fax with successful transmission notice → effective on day of transmission.
- E155 s 111(5),(7): email to an individual without prior consent → not valid service.
- E156 s 111(5),(7): email with consent, document under s 62 → valid.
- E157 s 111(6): email with consent, s 63 notice → not permitted.
- E158 s 111(6): email of a summons → not permitted.
- E159 s 111(6): s 82(4) notice by email → not permitted; s 80 demand by email with consent → permitted.

## Entry: ss 28, 29, 84

- E160 s 28(1): 24 hours' notice → may enter; 23 hours → may not (without warrant).
- E161 s 29(1): reasonable grounds of imminent danger to public safety → may enter without notice or warrant.
- E162 s 84(1): 48 hours' notice to occupier → may enter; 24 hours → may not.
- E163 s 84(3): warrant needs notice of intention to apply, or premises unoccupied/occupier absent and urgency.
