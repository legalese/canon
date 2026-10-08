# GLOSSARY — Vietnamese terms and their English identifiers (row VN-01)

Every Vietnamese term below is copied from ../../source/raw/baoviet-vcx-2021.txt and checked verbatim by `tools/vnsrc.py check`.
"src" is the line of that file where the term is defined or first used.
Identifiers are those in the `.l4` modules; `bvvcx-nouns.l4` declares the facts, the rule modules declare the outcomes.

## The terms Part I defines

| Vietnamese term (verbatim) | English identifier in the L4 | English meaning, one line | where defined or used (Điều / clause, src line) | translation risk |
| --- | --- | --- | --- | --- |
| BẢO VIỆT | `the insurer` | Bao Viet Insurance Corporation, the insurer | def 1, src 50 | The Rules name one company; "the insurer" generalises it, which is what the later cross-insurer comparison wants. |
| Bên mua bảo hiểm | `the purchaser`, `The purchaser`, `a purchaser within definition 2` | who concludes the contract and pays the premium | def 2, src 52 | Often rendered "policyholder"; that English word suggests the person who owns the policy, while the definition makes standing depend on owning or lawfully holding the vehicle AND having paid in full. "Purchaser" keeps the literal sense. |
| Cháy | `a fire`, `a fire within definition 3` | a chemical reaction of combustion with oxygen, giving heat and light | def 3, src 56 | English "fire" has no such technical limit; smouldering without flame is not "Cháy". |
| Giá thị trường | `market value when the contract was concluded`, `market value at the time and place of the loss` | the price at which a like vehicle is offered at the time | def 4, src 58 | The Rules also write "Giá trị thị trường" (market value, 12.2, 13.2.1, 13.2.2), which is not defined; read as this term (fork F2). |
| Giấy chứng nhận kiểm định | `The inspection status at the time of the loss`, `a valid inspection certificate` | the road-worthiness and emissions inspection certificate | def 5, src 61; 11.2, src 449 | "Inspection certificate" loses the statutory name ("technical safety and environmental protection"); harmless here. |
| Giấy yêu cầu bảo hiểm | `the request form was signed or confirmed electronically` | the insurer's request form, paper or electronic | def 6, src 63 | "Proposal form" is the British term; "request form" is literal. |
| mã xác thực (OTP) | `the request form was signed or confirmed electronically` | a one-time password counting as a signature | def 6, src 67-68 | None. |
| Hợp đồng bảo hiểm | `A document making up the contract`, `The policy` | the insurance contract, as Article 1 composes it | def 7, src 69; Art 1, src 99 | The English "policy" names the document; the Vietnamese names the agreement. The L4 uses `The policy` for the certificate's facts. |
| Người điều khiển xe | `the driver`, `the driver within definition 8` | the person driving the insured vehicle with the purchaser's or the insured's consent | def 8, src 71 | HIGH. English "the driver" is whoever drives; the defined term requires consent, so a thief is not "the driver" (finding X1). The definition's own words "Người lái xe được bảo hiểm" can also be read "the insured driver" (fork F1). |
| Người được bảo hiểm | `the insured`, `The claimant` | the person or body whose details are on the certificate | def 9, src 73 | "The insured" in English can mean the vehicle; here it is a person. |
| Người thụ hưởng | (not declared) | beneficiary | used in def 2, src 55 | Capitalised as if defined, and never defined (finding X13). |
| Nổ | `an explosion`, `an explosion within definition 10` | rapid combustion making surrounding gas expand suddenly | def 10, src 75 | English "explosion" includes a tyre or tank bursting; the definition excludes it. |
| nổ lý học | `a physical explosion from excess pressure` | a burst from internal pressure | def 10, src 76 | "Physical explosion" is a calque; "burst" is the plain English. |
| Phí bảo hiểm | `the premium` | the premium | def 11, src 78 | None. |
| Thời gian sử dụng xe | `the time in use, in months, of …` | months from first registration (or June of the year made) to the month cover begins | def 12, src 80 | "Age of the vehicle" would suggest a date of manufacture; the definition counts from registration. |
| Trọng tải | `permitted load` | the permitted carrying or towing mass on the inspection certificate | def 13, src 84 | "Tonnage" or "payload" would each lose half the definition (towed mass is included). |
| Xe ô tô/Xe | `a car within definition 14`, `A kind of road motor vehicle`, `The insured vehicle` | a self-propelled road motor vehicle, not a motorcycle, moped, e-bike or e-motorbike | def 14, src 92 | "Car" is narrower in English than "xe ô tô" (which includes trucks and buses); the identifier keeps "car" with the definition's meaning. |

## Terms defined or fixed in the body

| Vietnamese term (verbatim) | English identifier in the L4 | English meaning, one line | where defined or used (Điều / clause, src line) | translation risk |
| --- | --- | --- | --- | --- |
| Giấy chứng nhận bảo hiểm/Đơn bảo hiểm | `The policy` | the certificate or policy schedule | 1.3, src 110 | Two documents named as alternatives; the L4 treats them as one source of facts. |
| Thời hạn bảo hiểm | `the start of the period of insurance`, `the end of the period of insurance` | the period of insurance on the certificate | 2.1, src 118 | "Term" and "period" are both used in English; "thời hạn" also means "time limit" elsewhere in the Rules. |
| chuyển quyền sở hữu xe | `A transfer of ownership` | transfer of the vehicle's ownership | 2.4, src 126 | None. |
| đơn phương chấm dứt thực hiện Hợp đồng bảo hiểm | `A notice of unilateral termination` | unilateral termination of performance of the contract | 3.2.1, src 153 | Vietnamese law distinguishes ending performance from rescission (hủy bỏ); "termination" is the closer English. |
| nhóm xe | `A vehicle under a group contract` | a fleet or group of vehicles under one contract | 3.2.3, src 167 | "Fleet" implies one owner; the text does not. |
| nợ phí | `an agreement allowing the purchaser to owe the premium` | to owe the premium (premium credit) | 3.1.1, src 140 | Read as a written agreement on the time for payment (fork F10). |
| Tổng đài dịch vụ chăm sóc khách hàng | `notify the insurer's customer-care hotline` | the insurer's customer-care call centre | 5.2.6(a), src 276 | None. |
| bất khả kháng | `force majeure prevented the written notice` | force majeure | 5.2.6, src 279; 9.1, src 408 | Civil-law concept; English "act of God" is narrower. |
| trở ngại khách quan | `days lost to force majeure or other objective obstacles` | objective obstacles | 9.1, src 409 | A term of Vietnamese civil law with no exact English counterpart. |
| giám định độc lập | `The independent assessment` | independent loss assessment | 6.2, src 314 | "Loss adjusting" is the trade term; "assessment" is literal. |
| Hồ sơ bồi thường | `The claim file`, `A claim document` | the claim file | Art 7, src 331 | None. |
| Hợp đồng bảo hiểm trùng | `Another insurance of the vehicle`, `8.1 — this insurer's share of a loss …` | double insurance | Art 8, src 390 | English "double insurance" usually implies over-insurance; the Rules' definition does not (finding X4). |
| sự kiện bảo hiểm | `date of the insured event` | the insured event | 9.1, src 408 | None. |
| thời hiệu khởi kiện | `9.3 — the last day to sue` | limitation period for suit | 9.3, src 417 | "Thời hiệu" is a limitation period; 9.2 uses it and "thời hạn" for the same complaint period (finding X11). |
| Phạm vi bảo hiểm | `A head of cover` | scope of cover | Art 10, src 423 | None. |
| thiên tai | `a natural catastrophe beyond human control` | natural disaster | 10.1, src 425 | Whether ordinary flooding of a street is "thiên tai" is left to the caller (fork F11). |
| tai nạn | (the accident in 15.1.1 and 5.2.6) | accident; read as any loss event | 10.1, src 425; 15.1.1, src 600 | English "accident" excludes theft; the Rules use "tai nạn" for every loss (6.1, 7.1.1), and the encoding follows them (fork F36, finding X3). |
| Đâm va | `a collision` | collision | 10.1.1, src 427 | None. |
| lệch trọng tâm | `a shift of the centre of gravity` | loss of balance | 10.1.1, src 427 | Literal; the event is a vehicle tipping from a shifted load. |
| Hỏa hoạn | `a conflagration` | fire as a disaster | 10.1.2, src 429 | Overlaps "Cháy" in English; both map to 10.1.2. |
| trộm, cướp | `theft of the whole vehicle`, `robbery of the whole vehicle` | theft; robbery (taking by force) | 10.1.4, src 431 | Distinct offences in Vietnamese law (outside knowledge, unverified); fraud is a third (fork F25). |
| Loại trừ trách nhiệm bảo hiểm | `An exclusion of Article 11` | exclusion | Art 11, src 440 | None. |
| Giấy phép lái xe | `held a driving licence` and the licence fields | driving licence | 11.3, src 452 | None. |
| bị tước quyền sử dụng Giấy phép lái xe | `the right to use the licence had been withdrawn` | licence suspended or revoked | 11.3, src 454-455 | "Có thời hạn hoặc không thời hạn": both suspension and revocation. |
| nồng độ cồn | `blood alcohol, milligrams per 100 millilitres`, `breath alcohol, milligrams per litre` | alcohol concentration | 11.4, src 459 | "0,25" uses a decimal comma: 0.25. |
| ma túy và chất kích thích | `had used narcotics or stimulants the law prohibits` | narcotics and stimulants | 11.4, src 460 | "và" (and) is read as a list of substances, either of which suffices. |
| Đua xe | `racing, lawful or unlawful` | racing | 11.6, src 467 | None. |
| hàng hóa nguy hiểm | `carrying dangerous goods without the permit the law requires` | dangerous goods | 11.7, src 469 | None. |
| hao mòn tự nhiên | `natural wear and tear` | wear and tear | 11.10, src 473 | None. |
| bản chất vốn có | `the inherent nature of the part` | inherent vice | 11.10, src 473 | "Inherent vice" is the marine-insurance term of art; the identifier stays literal. |
| giảm giá trị thương mại | `a loss of commercial value` | depreciation in market value | 11.10, src 473-474 | Not physical damage at all. |
| đoản mạch | `overload, overpressure, short circuit, self-heating, electric arc or current leakage` | short circuit (with the other electrical causes) | 11.11, src 477 | One identifier groups six causes the text lists in one breath. |
| ngập nước | `water, while the vehicle was operating in a flooded area` | flooded | 11.12, src 479 | "Hoạt động" (operating) is the hinge between base cover and BVVC03 (fork F11, finding X18). |
| săm lốp | `a tyre or inner tube` | tyres and tubes | 11.13, src 481 | None. |
| bạt thùng xe | `the tarpaulin of the cargo body` | cargo-body tarpaulin | 11.13, src 481 | None. |
| nhãn mác | `a label or badge` | labels and badges | 11.13, src 481 | "Nhãn mác" may also mean trade marks or emblems. |
| lừa đảo hoặc lạm dụng tín nhiệm | `the whole vehicle taken by fraud or abuse of trust` | fraud or criminal breach of trust | 11.15, src 485 | "Abuse of trust" is literal; the Penal Code offence is usually rendered "abusing trust to appropriate property" (outside knowledge, unverified). |
| thiết bị lắp thêm | `added equipment …` kinds and causes | equipment fitted beyond the maker's | 11.17, src 496 | "Theo quy định" (as the regulations provide) has no named regulation (finding X13). |
| Số tiền bảo hiểm | `the sum insured` | the sum insured | 12.1, src 502 | None. |
| giá trị bảo hiểm | `12.3 — the value of` | insurable value | Art 12 heading, src 501 | The heading equates it with market value. |
| dưới giá trị; bằng giá trị | `12.2 — insured below value` | under-insured; insured at value | 13.1.2, src 526, 529 | None. |
| khấu hao | `13.1.2(b) — the depreciation scale`, `the depreciation rate for` | depreciation (new for old) | 13.1.2(b), src 532 | None. |
| Bồi thường thiệt hại bộ phận | `a partial loss (13.1)` | partial loss | 13.1, src 516 | Literally "damage to parts". |
| Bồi thường thiệt hại toàn bộ | `a total loss by the cost of repair (13.2.1(a))`, `a total loss by theft or robbery (13.2.1(b))` | total loss | 13.2, src 550 | Includes a constructive total loss (over 75%). |
| Thu hồi tài sản | `13.3.2 — the deduction for a wreck the insured keeps:` | salvage | 13.3, src 560 | None. |
| Mức khấu trừ | `14 — the deductible per partial loss under`, `14.3 — the minimum deductible per loss` | deductible (excess) | 14.1, src 584 | "Excess" in British English. |
| Giảm trừ bồi thường | `A reduction`, `A ground of reduction` | reduction of compensation | Art 15, src 596 | Not a deductible: a percentage cut. |
| Điều khoản bổ sung | `A supplementary clause` | supplementary clause (endorsement) | Part IV, src 656 | "Endorsement" or "rider" are the trade terms. |
| garage chính hãng | `BVVC02 (repair at an authorised garage)` | the maker's authorised garage | Art 17, src 682 | None. |
| giới hạn trách nhiệm | `BVVC06 (settlement up to the limit of liability)` | limit of liability | Art 21, src 740 | In English a "limit of liability" is a cap; the clause also lifts pro-rating (fork F39). |
| chi phí thuê xe | `BVVC05 (car hire during repair)`, `The car hire during repair` | car-hire costs | Art 20, src 726 | None. |
| ngày làm việc | `the working day … working days after …` | working day | 4.2.7, src 224; 5.2.4, src 251 | Undefined; Saturdays read as non-working (fork F15). |
| đình chỉ điều tra | `the police suspended the investigation or the prosecution` | suspension of the investigation | 13.2.1(b), src 555 | None. |
| Chi phí cứu hộ | `cost of rescue and of transport to the nearest repairer` | rescue (recovery) cost | 10.2.2, src 436 | "Salvage" would be wrong here. |
