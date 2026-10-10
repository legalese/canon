# Independent expectations: Goods and Services Tax Act 1993 (SSO consolidation in force 11 Sep 2026)

Written from `../source/GSTA1993.txt` alone, before opening any `.l4` file.
Every expectation states a scenario, the answer the Act gives, and the provision.
"REFUSE" means I think the Act gives no answer and an encoding should refuse.
Dates are written as day month year. "Interpretive" marks expectations where the
text is open to more than one reading; I give my reading and the reason.

## A. Scope (s 8)

- **E01.** A taxable person makes a supply of goods in Singapore, in the course of business, and the supply is not exempt. Expected: tax is charged (s 8(1), (2A)(a)).
- **E02.** Same as E01, but the supply is an exempt supply under s 22 and the Fourth Schedule. Expected: no tax is charged, because it is not a taxable supply (s 8(2A)(a)).
- **E03.** Same as E01, but the supplier is neither registered nor required to be registered. Expected: no tax is charged; the supplier is not a taxable person (s 8(1), (2)).
- **E04.** Same as E01, but the supply is not made in the course or furtherance of a business. Expected: no tax is charged (s 8(1)).
- **E05.** Same as E01, but the supply is made outside Singapore. Expected: no tax is charged under s 8(1).
- **E06.** A person who is required to be registered, but has not registered, makes a supply like E01. Expected: that person is a taxable person, so tax is charged (s 8(2): "is or is required to be registered").
- **E07.** A Seventh Schedule supply made by a taxable person in the course of business, whether or not in Singapore. Expected: tax is charged (s 8(1A), (2A)(b)).

## B. Place of supply (s 13)

- **E08.** Goods whose supply does not involve removal from or to Singapore, located in Singapore. Expected: supplied in Singapore (s 13(2)).
- **E09.** Goods whose supply does not involve removal, located outside Singapore. Expected: supplied outside Singapore (s 13(2)).
- **E10.** Goods whose supply involves their removal from Singapore (an export). Expected: supplied in Singapore (s 13(3)).
- **E11.** Goods whose supply involves their removal to Singapore. Expected: supplied outside Singapore (s 13(3)).
- **E12.** Services whose supplier belongs in Singapore. Expected: made in Singapore (s 13(4)(a)).
- **E13.** Services whose supplier belongs in another country. Expected: made outside Singapore (s 13(4)(b)).

## C. Belonging (s 15)

- **E14.** The supplier has a business establishment in Singapore and none elsewhere. Expected: belongs in Singapore (s 15(3)(a)).
- **E15.** The supplier has no establishment anywhere and its usual place of residence is Singapore. Expected: belongs in Singapore (s 15(3)(b)).
- **E16.** The supplier has no establishment anywhere and its usual place of residence is abroad. Expected: does not belong in Singapore (s 15(3)(b)).
- **E17.** The supplier has establishments in Singapore and elsewhere, and the establishment most directly concerned with the supply is in Singapore. Expected: belongs in Singapore (s 15(3)(c)).
- **E18.** Same as E17, but the most directly concerned establishment is abroad. Expected: does not belong in Singapore.
- **E19.** The recipient is an individual receiving services otherwise than for a business, with usual residence in Singapore. Expected: belongs in Singapore (s 15(4)).
- **E20.** The recipient has establishments in Singapore and elsewhere, and the services are most directly used at the overseas establishment. Expected: does not belong in Singapore (s 15(5)(b)).
- **E21.** A body corporate is incorporated in Singapore and has no establishment anywhere. Expected: belongs in Singapore, because its usual place of residence is its place of incorporation (s 15(6)(b), (3)(b)).

## D. Rate (s 16)

- **E22.** Supply on 31 Dec 2002. Expected: s 16 states no rate for this date. REFUSE.
- **E23.** Supply on 1 Jan 2003. Expected: 4% (s 16(a)).
- **E24.** Supply on 31 Dec 2003. Expected: 4%.
- **E25.** Supply on 1 Jan 2004. Expected: 5% (s 16(b)).
- **E26.** Supply on 30 Jun 2007. Expected: 5%.
- **E27.** Supply on 1 Jul 2007. Expected: 7% (s 16(c)).
- **E28.** Supply on 31 Dec 2022. Expected: 7%.
- **E29.** Supply on 1 Jan 2023. Expected: 8% (s 16(ca)).
- **E30.** Supply on 31 Dec 2023. Expected: 8%.
- **E31.** Supply on 1 Jan 2024. Expected: 9% (s 16(cb)).
- **E32.** Supply on 10 Oct 2026. Expected: 9%.

## E. Value and tax fraction (s 17)

- **E33.** Money consideration of $109 at 9%. Expected: value $100 and tax $9 (s 17(2)).
- **E34.** Money consideration of $108 at 8%. Expected: value $100 and tax $8.
- **E35.** Money consideration of $1,070 at 7%. Expected: tax $70.
- **E36.** The tax fraction at 9%. Expected: 9/109 (s 17(2)).
- **E37.** A supply that is not for money consideration. Expected: the value is the open market value (s 17(3)).
- **E38.** A reverse charge supply with consideration of $10,000. Expected: value $10,000, with tax added on top and not extracted (s 17(2A)(a), (3A)); at 9% the tax is $900.

## F. Time of supply (ss 11, 11A, 11B)

- **E39.** Invoice issued on 5 Mar 2025, payment received on 10 Mar 2025. Expected: the time of supply is 5 Mar 2025, the earlier event (s 11(2)(b)).
- **E40.** Payment received on 1 Mar 2025, invoice issued on 20 Mar 2025. Expected: 1 Mar 2025.
- **E41.** Invoice issued on 5 Mar 2025, no payment yet. Expected: 5 Mar 2025 (s 11(2)(a)).
- **E42.** A grant of an interest in land (not a periodic lease): goods made available on 1 Jun 2025, and the first invoice or payment comes on 15 Jun 2025. Expected: the time of supply is 1 Jun 2025 (s 11(3)(a), (d)(ii)).
- **E43.** Same as E42, but an invoice is issued on 20 May 2025, before the goods are made available. Expected: 20 May 2025 (s 11(4)).
- **E44.** Goods sent on sale or return, removed on 1 Mar 2025, with no invoice or payment ever made. Expected: the supply takes place 12 months after removal, on 1 Mar 2026 (s 11A(6)).
- **E45.** Same as E44, but an invoice is issued on 15 Feb 2026, before the 12 months expire. Expected: 15 Feb 2026.
- **E46.** Same as E44, but the first invoice is issued on 15 Mar 2026, after the 12 months expire. Expected: 1 Mar 2026.
- **E47.** Supply to a connected person: goods removed on 1 Apr 2025, with no invoice or consideration. Expected: the supply takes place 12 months after removal, on 1 Apr 2026 (s 11B(3)).
- **E48.** Same as E47, but an invoice covering the whole supply is issued on 1 May 2025. Expected: s 11(2) gives 1 May 2025, and s 11B(3) applies only "to the extent not covered", so the time of supply is 1 May 2025.

## G. Distantly taxable goods (s 2(1), (1A))

- **E49.** Goods with an entry value of $400, non-dutiable, not exempt, located outside the customs territory at the point of sale, and delivered by post. Expected: distantly taxable goods, because $400 does not exceed the threshold.
- **E50.** Same as E49, with an entry value of $400.01. Expected: not distantly taxable goods.
- **E51.** Same as E49, but delivered following an importation by sea. Expected: not distantly taxable goods, unless approved under para 4C of the Seventh Schedule.
- **E52.** Same as E49, but delivered by air. Expected: distantly taxable goods.
- **E53.** Same as E49, but the goods are located in Singapore at the point of sale. Expected: not distantly taxable goods.
- **E54.** Same as E49, but the goods are dutiable and the duty is not waived. Expected: not distantly taxable goods.
- **E55.** Same as E54, but the whole duty is waived under s 11 of the Customs Act. Expected: distantly taxable goods.
- **E56.** Same as E49, but the supply would be exempt. Expected: not distantly taxable goods.

## H. Reverse charge (s 14) and the Eighth Schedule

- **E57.** Services supplied by an overseas supplier to a Singapore-belonging, registered business recipient that is not entitled to full input tax credit (partially exempt). The services are not excluded. Expected: s 14(2) applies; the recipient accounts for tax.
- **E58.** Same as E57, but the recipient is entitled to full input tax credit and makes no election. Expected: s 14 does not apply (s 14(1)).
- **E59.** Same as E58, but the recipient elects under s 14(5). Expected: s 14(2) applies.
- **E60.** Same as E57, but the recipient is an individual receiving the services in a private capacity. Expected: s 14 does not apply (s 14(1)(b)(i)(C)).
- **E61.** Same as E57, but the recipient is neither registered nor liable to be registered under para 1 or 1B. Expected: s 14 does not apply (s 14(1)(b)(i)(B)).
- **E62.** Same as E57, but the services would be exempt if supplied in Singapore. Expected: excluded under Eighth Schedule para 1(a) of the services part; no reverse charge.
- **E63.** Same as E57, but the services would be zero-rated international services. Expected: excluded under Eighth Schedule para 1(b) of the services part.
- **E64.** Same as E57, but the supplier belongs in Singapore. Expected: s 14(1)(b)(i) does not apply.
- **E65.** Same as E57, but the recipient has already paid an amount as tax to the overseas vendor under s 8(1A). Expected: s 14(2) does not apply to that extent (s 14(3A)).

## I. Seventh Schedule: customers, remote services, marketplaces

- **E66.** A Seventh Schedule supply to a person who is registered and receives it in the course of business. Expected: not a customer (para 2(1)).
- **E67.** A Seventh Schedule supply to a registered person who receives it privately. Expected: a customer.
- **E68.** A Seventh Schedule supply to an unregistered business. Expected: a customer.
- **E69.** The recipient does not give the supplier a GST registration number. Expected: the supplier must treat the recipient as not registered (para 3(4)), so the recipient is a customer.
- **E70.** Remote services from an overseas supplier to a customer who belongs in Singapore. Expected: a Seventh Schedule supply (para 3(2)(a)).
- **E71.** Remote services from an overseas supplier to a customer who does not belong in Singapore. Expected: not a Seventh Schedule supply under para 3(2)(a).
- **E72.** A marketplace operator only sets the terms and conditions of the supply (para 4(1)(c)), and no other para 4(1) condition is met. Expected: the operator is treated as the supplier.
- **E73.** A marketplace operator meets none of the para 4(1)(a)-(e) conditions. Expected: the operator is not treated as the supplier.
- **E74.** An operator that is only the Internet service provider for the marketplace. Expected: not an operator (para 1(2)).
- **E75.** Distantly taxable goods supplied to a customer, where the supplier arranges delivery to Singapore. Expected: a Seventh Schedule supply (para 3(3A)(a)).

## J. Second Schedule

- **E76.** A business gift of goods costing the donor $200. Expected: not a supply (para 5(2)(a): "not more than $200").
- **E77.** Same as E76, costing $200.01. Expected: a supply (para 5(1)).
- **E78.** A gift of goods costing $500, where no input tax credit was allowed on the goods and they were not acquired through a going concern transfer. Expected: not treated as a supply (para 5(4)).
- **E79.** On ceasing to be a taxable person, the business assets have a deemed-supply value of $10,000. Expected: no deemed supply (para 7(1)(c): "not more than $10,000").
- **E80.** Same as E79, with a value of $10,000.01. Expected: a deemed supply.
- **E81.** Same as E80, but the business is transferred as a going concern to another taxable person. Expected: no deemed supply (para 7(1)(a)).
- **E82.** Same as E80, but no input tax credit was allowed on the goods and they were not acquired as part of a going concern. Expected: para 7 does not apply (para 7(2)).

## K. Third Schedule

- **E83.** A taxable person supplies a used motor vehicle, previously registered under the Road Traffic Act, for $50,000; not under the margin scheme. Expected: value reduced by 50% (para 14). The value before reduction is $50,000 × 100/109 ≈ $45,871.56, so the reduced value is about $22,935.78. An encoding that applies the 50% to a pre-computed value should give half of its input.
- **E84.** Same as E83, under the margin scheme (s 23). Expected: no 50% reduction.
- **E85.** An employer provides catering food to employees for no consideration. Expected: value nil (para 10).
- **E86.** Same as E85, but employees pay $3 in money. Expected: the value is determined by reference to the money only (para 10(2)).
- **E87.** Hotel accommodation provided to employees free. Expected: value nil.
- **E88.** An open market value direction given 3 years after the time of supply, to the day (supply 1 Mar 2023, direction 1 Mar 2026). Expected: permitted ("not more than 3 years").
- **E89.** Same as E88, but the direction is given on 2 Mar 2026. Expected: not permitted.
- **E90.** Para 1(1) open market value direction: value below open market value, connected persons, and a recipient not entitled to full credit. Expected: a direction is possible. If the recipient is entitled to full credit, no direction is possible.

## L. Supplies spanning a rate change (ss 39A-39F), with 8% to 9% on 1 Jan 2024 and value $10,000

- **E91.** s 39C: invoice for $10,000 issued before 1 Jan 2024, nothing paid and nothing performed before. Expected: new rate (9%) on $10,000; old rate on $0.
- **E92.** s 39C: invoice issued before, $4,000 paid before, $3,000 performed before. Expected: new rate on the lower of $6,000 (paid after) and $7,000 (performed after), which is $6,000 at 9%. The old rate applies to $4,000 at 8%.
- **E93.** s 39C: invoice issued before and consideration paid in full before, but nothing performed before. Expected: new-rate base is the lower of $0 and $10,000, which is $0, so the whole $10,000 is at the old rate.
- **E94.** s 39C: invoice issued before, fully paid and fully performed before. Expected: s 39C does not apply, because condition (b) fails; the supply does not span the change (s 39(3)).
- **E95.** s 39B election: $6,000 performed before the change, $0 paid before, and the invoice and payment come after. Expected: old rate on the higher of $0 and $6,000, which is $6,000; new rate on $4,000.
- **E96.** s 39B election: $6,000 performed before and $7,000 paid before. Note that s 39B needs the invoice or a payment on or after the change; here the invoice is issued after. Expected: old rate on $7,000, the higher value; new rate on $3,000.
- **E97.** s 39B: a supply to which para 6 of the Second Schedule applies. Expected: no election allowed (s 39B(4)).
- **E98.** s 39A(5): the specified change occurs on or before the date the person is required to be registered. Expected: Division 1 does not apply.
- **E99.** s 39D(2): a new tax invoice is required within 14 days after the change. Expected: the deadline is 15 Jan 2024 for a change on 1 Jan 2024.

## M. Section 40

- **E100.** A contract is made before a rate increase, the supply is after, and the contract is silent. Expected: the supplier may add the tax increase to the agreed price (s 40(1)(a)).
- **E101.** Same as E100, but the contract expressly excludes adjustment. Expected: no adjustment.
- **E102.** A rate decrease, or the supply becomes exempt. Expected: the supplier may deduct the reduction (s 40(1)(b)).

## N. First Schedule registration

- **E103.** Taxable supplies in calendar year 2025 of $1,000,000 exactly. Expected: not liable under para 1(1)(a)(ii), which requires the value to have "exceeded".
- **E104.** Taxable supplies in calendar year 2025 of $1,000,001. Expected: liable at the end of 2025.
- **E105.** Same as E104, but $200,000 of the total is sales of capital assets. Expected: not liable, because capital assets are disregarded (para 1C(2)) and $800,001 does not exceed $1m.
- **E106.** Same as E104, but the Comptroller is satisfied that 2026 supplies will not exceed $1m. Expected: not liable (para 1(3)(b)).
- **E107.** Retrospective liability at the end of 2025. Expected: notify within 30 days, so by 30 Jan 2026 (para 4(1A)). The effective date of registration is the day after the end of the month following the month of the 30th day: the 30th day is 30 Jan 2026, the following month is February, so registration is effective 1 Mar 2026 (para 4(2)(a)).
- **E108.** Prospective liability under para 1(1)(b): there are reasonable grounds on 15 Aug 2025 (day X) to expect more than $1m in the next 12 months. Expected: notify within 30 days after day X, so by 14 Sep 2025. Registration is effective 15 Oct 2025 (para 5(2)(a)(ii)(A)).
- **E109.** Prospective, day X on 31 Dec 2025. Expected: month M+2 is February 2026, which has no 31st, so registration is effective on the last day of Feb 2026, 28 Feb 2026 (para 5(2)(a)(ii)(B)).
- **E110.** Prospective, day X on 30 Dec 2027. Expected: February 2028 has 29 days and no 30th, so registration is effective 29 Feb 2028.
- **E111.** Prospective, day X on 1 Jul 2025 (on the change date). Expected: the new rule applies, and registration is effective 1 Sep 2025.
- **E112.** Prospective, day X on 30 Jun 2025 (before the change). Expected: the old rule applies: registration is effective the day after the end of the 30 days after day X. Interpretive: the 30 days after 30 Jun run to 30 Jul, so the effective date is 31 Jul 2025 (day X plus 31 days).
- **E113.** Overseas vendor (para 1A): global turnover $1,500,000 and Seventh Schedule supplies $100,000 in 2025. Expected: not liable, because $100k does not exceed $100k.
- **E114.** Same as E113, with Seventh Schedule supplies of $100,001. Expected: liable.
- **E115.** Same as E113, with global turnover of $1,000,000 and Seventh Schedule supplies of $500,000. Expected: not liable, because the global limb is not exceeded.
- **E116.** Reverse charge recipient (para 1B): supplies received of $1,200,000 in 2025, not entitled to full input credit. Expected: liable.
- **E117.** Same as E116, but entitled to full input credit. Expected: not liable.
- **E118.** Voluntary registration (para 8(2)). Expected: the person remains registered for not less than 2 years.
- **E119.** A going concern transfer: the transferee is liable at the time of transfer, and must notify within 30 days after the transfer. Expected: registration is effective on the day of transfer (para 6(2)).
- **E120.** A person registered under para 4(4)/5(2B) after a refusal. Expected: the effective date is not earlier than 30 days after the Comptroller notifies the person (para 4(5)(b)).

## O. Special persons (ss 30-33)

- **E121.** A supply between members of a GST group. Expected: disregarded (s 30(1)(a)).
- **E122.** A supply between group members that would give rise to a reverse charge supply. Expected: not disregarded (s 30(1A)).
- **E123.** A partner leaves a partnership on 1 Mar 2025, and the change is notified to the Comptroller in writing on 1 May 2025. Is the person still treated as a partner on 15 Apr 2025? Expected: yes (s 31(3)). On 1 May 2025 itself: no, because "until the date on which" the change is notified means the deeming ends on that date.
- **E124.** A person carrying on the business of a deceased taxable person starts on 1 Jun 2025. Expected: must inform the Comptroller within 21 days, by 22 Jun 2025 (s 32(6)).
- **E125.** An overseas registrant that is not a pay-only person. Expected: must appoint a s 33(1) agent (s 33(1)(a)).
- **E126.** A registered (Seventh Schedule — pay only) person. Expected: may, but need not, appoint an agent (s 33(1)(b)). If it appoints one on 1 Mar 2025, it must notify within 30 days, by 31 Mar 2025 (s 33(1B)(b)).
- **E127.** A change of agent on 1 Jun 2025. Expected: must be notified not less than 30 days before, by 2 May 2025 (s 33(1B)(c)).

## P. Input tax (ss 19, 20, 41(7))

- **E128.** Goods bought for business use only. Expected: the tax counts as input tax (s 19(3)).
- **E129.** Goods bought 60% for business and 40% for private use, with $900 tax. Expected: input tax $540 (s 19(4)).
- **E130.** Consideration is due on 1 Mar 2025 and remains unpaid. Expected: the initial specified period ends 12 months after the due date, on 1 Mar 2026, and the input tax must be repaid in the accounting period in which that date falls (s 19(12), (15)).
- **E131.** Input tax is first credited in a period ending 31 Mar 2025. Expected: the subsequent specified period ends 5 years after the end of that period, on 31 Mar 2030 (s 19(15)(b)). For a period ending 31 Dec 2006 the end is 6 years after.
- **E132.** s 20(2A): the person knew the supply was part of a fraud arrangement. Expected: input tax is denied.
- **E133.** s 20(2D)(b)(i): reasonable risk, and no reasonable steps taken. Expected: "should have known", so credit is denied, even if a reasonable person would have concluded otherwise (s 20(2E)(a)).
- **E134.** s 20(2F): the person took reasonable steps, concluded "not part", and the conclusion is reasonable. Expected: not "should have known"; credit is allowed (absent actual knowledge).
- **E135.** The person took reasonable steps but was unable to conclude. Expected: should have known (s 20(2D)(b)(ii)(B)).
- **E136.** No reasonable risk in the circumstances. Expected: not "should have known" (s 20(2D)(a)).
- **E137.** Net tax due of $4.99. Expected: zero (s 41(7)).
- **E138.** Net tax due of $5.00. Expected: $5, because only "less than $5" is zeroed.
- **E139.** A net refund due under s 19(5) of $4.99. Expected: zero.

## Q. Assessment, records, surcharges (ss 45-48)

- **E140.** An assessment for a period ending 31 Dec 2020, made on 31 Dec 2025. Expected: allowed; it is "not more than 5 years after" the end (s 45(5)(b)).
- **E141.** Same as E140, but made on 1 Jan 2026. Expected: time-barred, unless fraud or wilful default (s 45(5A)).
- **E142.** Same as E141, but with fraud or wilful default. Expected: allowed at any time.
- **E143.** A period ending 31 Dec 2006: an assessment made 7 years after the end is allowed; one made 7 years and 1 day after is barred (s 45(5)(a)).
- **E144.** A s 45A surcharge on input tax of $50,000. Expected: $5,000 (10%).
- **E145.** Records for a period ending 31 Dec 2025 must be kept until at least 31 Dec 2030 (s 46(2)(b)); for a period ending before 2007, 7 years.
- **E146.** A s 47A surcharge on additional tax of $20,000 for a period starting 1 Jan 2021. Expected: $10,000 (50%).
- **E147.** Same as E146, for a period starting 1 Oct 2020. Expected: s 47A does not apply.
- **E148.** A s 47 adjustment more than 5 years after the end of the period. Expected: not allowed (s 47(2A)).
- **E149.** s 48 penal tax where the undercharged tax is $10,000. Expected: a maximum of $30,000.

## R. Objections and appeals (ss 49-57)

- **E150.** Notified of a decision on 1 Mar 2025. Expected: the objection deadline is 31 Mar 2025, 30 days after (s 49(2)).
- **E151.** The Comptroller's decision on review is dated 1 Apr 2025. Expected: notice of appeal by 1 May 2025 (s 51(1)(a)). The petition is due 30 days after the notice is lodged: a notice lodged on 20 Apr 2025 gives a petition deadline of 20 May 2025 (s 51(1)(b)).
- **E152.** An appeal against a s 49(1)(j) assessment, where the tax is not paid and no hardship agreement or decision has been made. Expected: the appeal must not be heard (s 51(8)). If the tax is paid or deposited, it may be heard, provided all returns are made and paid (s 51(7)).
- **E153.** An appellant has outstanding returns. Expected: the appeal must not be heard (s 51(7)).
- **E154.** A Board decision where the tax payable is $499. Expected: no appeal to the High Court (s 54(2)). At $500, an appeal on law or mixed law and fact is allowed.
- **E155.** A Board committee of 3 members, one of whom is a Deputy Chairperson. Expected: validly constituted (s 50(6)). A committee of 2: invalid. A committee of 3 with no Chair or Deputy: invalid.
- **E156.** A single member who is a Deputy Chairperson, appointed by the Chairperson. Expected: valid (s 50(6A)). A single ordinary member: invalid.

## S. Collection, refunds, rulings, service

- **E157.** A refund claim for a period ending 31 Mar 2021, made on 31 Mar 2026. Expected: in time ("within 5 years after the end", s 90(1B)(b)(ii)). Made on 1 Apr 2026: out of time.
- **E158.** A refund for a period ending before 1 Jan 2007. Expected: s 90(1A) does not cover it, so no refund under s 90.
- **E159.** A s 79 agent notice received on 1 Mar 2025. Expected: moneys held up to 90 days later (30 May 2025) are caught; moneys first held on 31 May 2025 are not.
- **E160.** A s 79(4) joint account: the agent must notify the owners within 14 days and pay over within 42 days; an objection must be made within 28 days.
- **E161.** s 83E: the Comptroller may arrest without warrant a person reasonably believed to have committed a s 62 offence (s 83E(2)(a)). A specially authorised customs officer may arrest only in connection with a s 25 refund (s 83E(1)), and not for a general s 62 offence.
- **E162.** Advance ruling fee when 4 hours are spent. Expected: $660.
- **E163.** Same as E162, 4.5 hours. Expected: $660 + $165 = $825, because "any part of an hour" counts.
- **E164.** Same as E162, 6 hours. Expected: $990.
- **E165.** Same as E164, with priority. Expected: a maximum of 3 × $990 = $2,970, because the additional fee is up to 2× the aggregate.
- **E166.** A ruling made on 1 Mar 2025. Expected: it applies for 3 years by default, to 28 Feb 2028 (Fifth Sch para 6(b)), unless the Comptroller determines otherwise.
- **E167.** s 87 service by ordinary post. Expected: a valid method; deemed served when it would be received in the ordinary course of post. Service through the electronic service: served when the record enters the account (s 87(3A)).

## T. Penalties (ss 59-66 etc.)

- **E168.** Late payment of $10,000 tax. Expected: a 5% penalty of $500 (s 60(1)(a)).
- **E169.** Same as E168, paid within 60 days after the 5% penalty. Expected: no additional penalty.
- **E170.** Same as E168, unpaid 3 completed months, after the 60-day window has passed. Expected: additional 2% × 3 = $600. Interpretive: months are counted from the date the tax became payable.
- **E171.** Same as E168, unpaid 40 completed months. Expected: the additional penalty is capped at 50%, so $5,000 (with a total of $5,500 including the 5%).
- **E172.** A late return, filed 0 completed months late. Expected: $200 (s 60(2)).
- **E173.** A late return, 3 completed months late. Expected: $200 + $600 = $800.
- **E174.** A late return, 60 completed months late. Expected: capped at $10,000.
- **E175.** s 61 failure to register: tax due of $50,000 in respect of 1 year. Expected: a penalty of 10% = $5,000, a fine up to $10,000, and $50 per day after conviction.
- **E176.** s 59(1) incorrect return, undercharged $8,000. Expected: a penalty of $8,000. s 59(2) negligence: a penalty of $16,000 plus a fine up to $5,000 or 3 years' imprisonment.
- **E177.** s 62: penalty 3× undercharged tax, fine up to $10,000, imprisonment up to 7 years.
- **E178.** s 63 improper refund of $4,000 excess. Expected: penalty $12,000; fine up to $10,000 or 3 years.
- **E179.** s 64: fine up to $5,000 and a penalty of 3× the tax.
- **E180.** s 64A(1): 3× the amount collected, plus a fine up to $10,000 (no imprisonment). s 64A(2) and (4): plus up to 3 years' imprisonment.
- **E181.** s 62A: fine equal to the undercharged tax, plus a further fine up to $10,000 (no imprisonment). s 62B: fine of 3× plus a further fine up to $10,000 or 7 years.
- **E182.** s 62C(1): fine up to $500,000 or 10 years. s 62C(4): $50,000 or 12 months.
- **E183.** s 65: $10,000 or 3 years. s 66: $10,000 or 12 months.
- **E184.** s 44(4): $5,000. s 81(4): $5,000. s 58 general: $5,000, with imprisonment in default of up to 6 months.
- **E185.** s 46(6) first conviction: $5,000 or 6 months. Second or subsequent conviction: $10,000 or 3 years.
- **E186.** s 83I(4): $10,000 or 12 months. s 83I(9): $10,000 or 2 years.
- **E187.** s 84(2D): $10,000 or 12 months, plus $100 per day continuing. s 84(2E): $10,000 or 2 years.
- **E188.** s 86(1) contravention of regulations: up to $10,000 or 2 years.

## U. Proceedings (ss 69, 73A, 74, 75)

- **E189.** Public Prosecutor consent is required for ss 6, 62, 62C, 63, 65 and 66, and not for s 59 or s 64 (s 69).
- **E190.** s 73A notice to attend court: available for s 66 (12 months) and s 44(4) (fine only); not available for s 62 (7 years) or s 62C(1) (10 years).
- **E191.** s 74: a director is deemed guilty unless the director proves both no consent or connivance and due diligence. Proving only one is not enough.
- **E192.** s 75: composition of a prescribed compoundable offence for $5,000 is allowed; for $5,001 it is not allowed; an offence that is not prescribed cannot be compounded.

## V. Matters I expect the Act not to answer (REFUSE)

- **E193.** The rate for a supply before 1 Jan 2003 (s 16 is silent; see E22). REFUSE.
- **E194.** The amount of the composition sum below the $5,000 cap. This is the Comptroller's discretion, and the Act gives no figure. REFUSE or a discretion input.
- **E195.** Whether a supply is exempt, as a classification under the Fourth Schedule. This is an input and cannot be derived.
