# GLOSSARY — OPES O-Car rules (row `legalese-2026-10-vn-15`)

Vietnamese source, English encoding. Every Vietnamese term in the first column is quoted verbatim from `../../source/raw/opes-ocar.txt` (checked by `tools/vnsrc.py check`). One row for each term Article 1 defines, then one for each type, field, enumeration member or constant the modules declare that renders a Vietnamese concept, in the order of the document.

## Terms Article 1 defines

| Vietnamese term (verbatim) | English identifier in the L4 | English meaning, one line | where defined or used (Điều / clause, src line) | translation risk |
| --- | --- | --- | --- | --- |
| Xe Ô Tô | `The vehicle`; `1.1 — a motor car within the definition` | a road motor vehicle with four or more wheels, not on rails, not a motorcycle | 1.1, src:64-70 | "motor car" is narrower in ordinary English than the definition, which takes in trucks, coaches, buses and special-purpose vehicles; "motor vehicle" is wider, since it would include the motorcycles 1.1 excludes. The identifier follows the definition, not either English word. |
| Chủ Xe | `the Vehicle Owner` | the owner, or a person the owner lets possess, use or lease the car, or a buyer not yet registered | 1.2, src:71-75 | High. English "owner" means title; the Vietnamese defined term covers lessees and possessors. Read the identifier as the defined term, not as "owner". |
| Bên Mua Bảo Hiểm | `the Policyholder` | the party who makes the contract with the Insurer and pays the premium | 1.3, src:76-78 | Literally "the party buying insurance". "Policyholder" is the usual English, but in Vietnamese law the buyer and the insured (next row) may differ. |
| Người Được Bảo Hiểm | `the Insured` | the owner whose car the contract insures | 1.4, src:79-80 | Low; note that it is defined by reference to Chủ Xe, so it inherits that term's width. |
| Lái Xe | `the Driver` | the person driving the insured vehicle at the time of the loss | 1.5, src:81 | Low. Defined at the moment of loss only. |
| Xe Được Bảo Hiểm | `vehicle` (field of `The policy`) | the car or cars named in the certificate or the contract | 1.6, src:82-83 | Low. |
| Phí Bảo Hiểm | `premium`, `premium paid` | the money the Policyholder pays the Insurer | 1.7, src:84-86 | Low. The rules use the defined term for the amount payable; `premium paid` is what was in fact paid. |
| Mức khấu trừ | `15 — the deductible on`, `deductible stated in the contract` | the amount the Insured bears on each loss, taken off the indemnity | 1.8, src:87-91; 15, src:893-900 | "khấu trừ" is "deduct". "Deductible" (US) and "excess" (UK) are both right; 12.20 calls it "mức miễn thường có khấu trừ", a deductible franchise, which is the same mechanism. 1.8 says "every loss", 15.1 "every partial loss" (finding X15). |
| Giá Thị Trường | `market value when insured`, `market value immediately before the loss` | the average sale price of similar vehicles at the time the value is fixed | 1.9, src:92-95 | The definition does not fix the time; each rule does, so the encoding carries two fields. 13.1 also writes "Giá Trị Thị Trường" (src:727), read as the same term. |
| Số Tiền Bảo Hiểm | `sum insured` | the amount the Policyholder asks to insure for, not more than the market value when insured | 1.10, src:96-98 | 4.1 uses the term for the amount the Insurer has paid out (src:228), which is not this (finding X19). |
| Hợp Đồng Bảo Hiểm | `The policy` | the insurance contract between the Policyholder and the Insurer | 1.11, src:109-115 | The encoding's record is called "policy" and holds what the contract and the certificate record; "policy" in English can mean the certificate. |
| Người Thụ Hưởng | not declared | a beneficiary, to whom the Insurer may pay | used 1.11, src:111; personal data clause, src:1146 | Used as a capitalised defined term and never defined (finding X12). Nothing in the encoding turns on it. |
| Giấy Chứng Nhận Bảo Hiểm | `The policy` (the inputs it records) | the certificate summarising the contract | 1.12, src:116-120 | "Certificate" in English can suggest a document of title; here it is evidence of the contract. |
| Điều Khoản Bảo Hiểm Bổ Sung | `A supplementary clause`, `A supplementary clause on the policy` | a clause that adjusts the scope of cover, in the certificate or the contract | 1.13, src:121-123; 17; BS01-BS07 | "Supplementary clause" is literal; in English market usage these are endorsements or riders. Note that the heading of the document (src:6) uses the same words for the amending instrument of 2022. |
| Công Ty Bảo Hiểm | `the Insurer` | OPES Insurance Joint Stock Company | 1.14, src:124-125 | Low. |
| Thời Gian Sử Dụng Xe Ô Tô | `1.15 — the time in use of the vehicle, in months` | months from first registration in Vietnam (or January of the year of manufacture, if imported after use abroad) to the month the contract was concluded | 1.15, src:126-129 | High in effect: the term is never used again; 13.2 says "Thời gian đã sử dụng" and 14.1.2(b) "Xe sử dụng" (fork F10, finding X11). "Age" would suggest the age at the loss, which this is not. |

## Types, fields, members and constants the modules declare

| Vietnamese term (verbatim) | English identifier in the L4 | English meaning, one line | where defined or used (Điều / clause, src line) | translation risk |
| --- | --- | --- | --- | --- |
| Quyết định số 124/2019/QĐ-TGĐ ngày | `the rules as made by Decision 124/2019`, `the date of Decision 124/2019` | the instrument that issued the rules, dated 31/12/2019 | heading, src:5-6 | The date is the decision's; the file gives no separate commencement date (fork F2). |
| Quyết định số 17/2022/QĐ-TGĐ ngày 28/03/2022 | `the rules as amended by the supplementary clauses of Decision 17/2022`, `the date of Decision 17/2022` | the instrument that issued the supplementary clauses | heading, src:6-7 | Same as above. |
| Thời hạn bảo hiểm | `start of the insurance period`, `last day of the insurance period` | the period of cover, as the certificate records it | 2.1, src:135-136 | "thời hạn" is both "period" and "deadline"; here a period. The encoding takes the last day as covered. |
| thời hạn thanh toán | `last day for paying the premium` | the agreed time for paying the premium | 3.1.1, src:162-163 | The text speaks of the end of the payment period; the encoding records its last day. |
| nợ phí | `the Insurer agreed that the premium may be owed` | an agreement letting the premium be paid later | 3.1.1, src:164 | Literally "owe the premium"; read as an agreed deferral. |
| đơn phương chấm dứt | `3.2.2 — the refund on the Policyholder's termination`, `3.2.3 — the refund on the Insurer's termination` | ending the contract by one party's notice | 3.2, src:178-197 | "Unilateral termination" is literal; "cancellation" is the usual English insurance word and carries no different sense here. |
| sự kiện bảo hiểm | `an insured event has happened`, `an insured event happened before termination, or liability to pay has arisen` | an event the cover responds to | 3.1.3, src:176; 3.2.2, src:189; 10, src:534 | Not defined in the rules. Read as any event within the scope of cover, whether or not anything is payable (fork F6, finding X25). "Claim" would be wrong. |
| ngày làm việc | `the non-working days` (input), `the end of ... working days counted from ... skipping ...` | a working day | 3.1.3, 3.2.1, 4.2, 5.2, 6 (src:170, 183, 238, 330, 379) | Not defined; which days are not working days is an input (fork F8). |
| giờ | `5.2 — the duty to notify the Insurer of a theft or a disaster loss within 24 hours` (clock in hours) | hour | 5.2, src:354 | Low. |
| thiên tai | `a natural catastrophe` | a disaster of nature (storm, flood, lightning, earthquake, landslide, tsunami ...) | 11.1, src:554, 569-570 | 11.1 bullet 3 says "tai họa bất khả kháng do thiên nhiên" (an irresistible calamity of nature). "Force majeure" (bất khả kháng) is a wider legal concept used elsewhere (5.2, 10) for an excuse, not a peril. |
| tai nạn bất ngờ, không lường trước được | `sudden and unforeseeable` (field of `The loss`) | a sudden accident that could not be foreseen | 11.1, src:554 | Low; whether it qualifies every listed peril is fork F17. |
| Đâm, va | `collision or impact, including with another object` | collision | 11.1, src:566 | "va" also covers grazing contact. |
| lật | `overturning` | overturning | 11.1, src:566 | Low. |
| đổ | `tipping over` | falling onto its side | 11.1, src:566 | Overlaps "lật"; the encoding keeps both. |
| chìm | `sinking` | sinking | 11.1, src:566 | Low. |
| rơi toàn bộ xe | `the whole vehicle falling` | the whole vehicle falling (from a height) | 11.1, src:566 | Low. |
| bị các vật thể khác rơi vào | `being struck by a falling object` | struck by other objects falling on it | 11.1, src:566-567 | Low. |
| Hỏa hoạn, cháy, nổ | `conflagration, fire or explosion` | conflagration, fire, explosion | 11.1, src:568 | "Hỏa hoạn" is a fire as an event (a conflagration), "cháy" burning; English "fire" covers both. |
| trộm, cướp | `theft or robbery of the whole vehicle` | theft (stealth) or robbery (force) | 11.1, src:571 | Two Vietnamese offences; the English pair keeps them apart. |
| Hành động ác ý, cố tình phá hoại | `a malicious act or deliberate destruction` | a malicious act, deliberate sabotage | 11.1, src:572 | Low. |
| vùng ngập nước | `driving into flood water` | a waterlogged area | BS03, src:1052 | "Flood water" may suggest a natural flood; the Vietnamese is any waterlogged area, including a flooded street, which is why the encoding keeps it apart from `a natural catastrophe`. |
| mất cắp, mất cướp | `theft or robbery of parts` | parts lost by theft or robbery | BS05, src:1085 | Low. |
| chi phí cần thiết và hợp lý | `11.2 — the costs payable besides the indemnity, for` | necessary and reasonable costs | 11.2, src:576 | Low. |
| Chi phí cứu hộ và vận chuyển | `cost of rescue and transport to the nearest repair shop` | rescue (towing) and transport to the nearest repair shop | 11.2, src:581 | "cứu hộ" is roadside rescue, not salvage at sea. |
| Loại trừ trách nhiệm bảo hiểm | `An exclusion in Article 12` | exclusion | 12, src:587 | Low. |
| Giấy chứng nhận kiểm định an toàn kỹ thuật và bảo vệ môi trường phương tiện giao thông cơ giới đường bộ | `The inspection certificate` | the roadworthiness and emissions inspection certificate (đăng kiểm) | 12.2, src:596-598 | "Registration" would be wrong: registration is "đăng ký"; this is the periodic inspection. |
| giấy phép lái xe | `The driving licence` | driving licence | 12.3, src:616-621 | Low. "bị tước quyền sử dụng" is the withdrawal of the right to use the licence, not its cancellation. |
| nồng độ cồn | `the Driver was over the legal alcohol limit` | blood or breath alcohol above the legal limit | 12.4, src:622-623 | The limit is the law's, not the rules' (an input). |
| tập lái | `used for driving practice` | driving practice | 12.7, src:632 | Low. |
| đua xe | `used for racing` | racing, lawful or not | 12.7, src:632 | Low. |
| hao mòn tự nhiên | `wear and tear, inherent nature, defect, or damage in repair` | natural wear | 12.11, src:643 | Low. |
| thủy kích | `engine damage from water: flood water or hydrolock` | hydrolock | 12.12, src:649 | A technical term; "water hammer" is a less precise rendering. |
| đoản mạch | `electrical damage from overload, overpressure, short circuit, self-heating, arcing or leakage` | short circuit | 12.13, src:655 | Low. |
| săm lốp | `a tyre or an inner tube` | tyres and inner tubes | 12.14, src:667; 14.1.2(d), src:834 | Low. |
| bạt thùng | `a truck-bed canvas` | the canvas cover of a cargo bed | 12.14, src:667; 14.1.2(d), src:831 | Low. |
| biểu tượng của nhà sản xuất | `the maker's emblem` | the maker's badge | 12.14, src:667-668 | Low. |
| tem chữ, nhãn mác | `a label or a sticker` | lettering stickers, labels | 12.14, src:668; 14.1.2(d) "tem nhãn mác", src:834 | The two clauses spell it differently; read as one kind. |
| ốp chụp la-zăng | `a hubcap` | hubcap | 12.14, src:668 | Low. |
| chìa khóa cơ/chìa khóa điện/điều khiển điện | `a key or a remote` | mechanical key, electronic key, remote | 12.14, src:668-669; BS05, src:1084 | Low. |
| tấm lót gầm | `an underbody shield` | underbody plate | 12.14, src:669 | Low. |
| Mất các bộ phận | `lost` (field of `A damaged item`) | loss of parts | 12.15, src:672 | "Mất" is to lose or to have stolen; the field records only that the part is gone. |
| lừa đảo hoặc lạm dụng tín nhiệm | `total loss by fraud or abuse of trust` | fraud, or abuse of trust to appropriate the car | 12.16, src:675-676 | "Lạm dụng tín nhiệm" is a named offence (criminal breach of trust); "abuse of trust" is literal. |
| thiết bị chuyên dùng | `caused by the vehicle's own special-purpose equipment` | the vehicle's own special-purpose equipment (pump, crane, tipper) | 12.17, src:678 | Low. |
| tải trọng | `load carried`, `permitted load in the inspection certificate` | load | 12.18, src:683 | Low. |
| trẻ em dưới 7 tuổi | `persons carried, not counting children under 7` | children under seven | 12.18, src:684 | 16.1.5 does not use the phrase (finding X4). |
| thiết bị/phụ kiện lắp thêm | `other added equipment or accessory` | equipment or accessories added beyond the maker's | 12.19, src:689 | Low. |
| thiết bị mang tính chất bảo vệ cho xe | `added protective equipment` | protective fittings: alarm, front and rear bumper guards | 12.19, src:690-691 | Low. |
| tốc độ cho phép | `speed above the limit, by an authority's written conclusion` | the permitted speed | 12.21, src:696; 16.1.2, src:933-935 | The field is the excess as a share of the limit, as the authority finds it. |
| tổn thất mang tính hậu quả | `a consequential loss, as 12.23 defines it` | consequential loss as 12.23 defines it | 12.23, src:703-704 | 12.23's definition ties it to a failure to notify; English "consequential loss" has its own common-law sense, which this is not. |
| trung đại tu, cải tạo, hoán cải | `overhauled, modified or converted and not yet re-inspected` | major overhaul, modification, conversion | 12.24, src:721 | Low. |
| Giá Trị Thị Trường | `market value when insured` | market value | 13.1, src:727 | A variant spelling of the defined term "Giá Thị Trường". |
| Xe Ô Tô mới (100%) | `new (100%) when insured` | a new vehicle | 13.1, src:730 | Low. |
| sản xuất trong nước | `manufactured in Vietnam` | domestically produced | 13.2(i), src:739 | Includes assembled in Vietnam, on the usual reading; not stated. |
| nhập khẩu đã qua sử dụng ở nước ngoài | `imported after use abroad` | imported having been used abroad | 1.15, src:127-128; 13.2(ii) | 13.2(ii) says only "nhập khẩu đã qua sử dụng", which could also mean imported and since used (fork F23). |
| giá xe nhập khẩu | `imported new` | an imported vehicle (new) | 13.1, src:731 | The text says "imported"; "new" is the encoder's, from 13.1's first bullet (new vehicles). |
| giá xe mới (100%) | `price of the vehicle new (100%)` | the price of the vehicle new | 13.2, src:740 | Low. |
| tỷ lệ (%) tối thiểu chất lượng còn lại | `13.2 — the minimum remaining-quality rate for a time in use, in months, of`; `minimum remaining-quality rate in the import customs declaration` | the minimum remaining-quality percentage | 13.2, src:740-751 | "Remaining value" would be shorter but wrong: it is a quality rate applied to the new price. |
| tờ khai hải quan nhập khẩu | `minimum remaining-quality rate in the import customs declaration` | the import customs declaration | 13.2(ii), src:744 | Low. |
| bảo hiểm dưới giá trị | `13 — insured below value, on` | insurance below value | 13.2, src:754; 14.1.2(a), src:785 | "Under-insurance" is the usual English. |
| bảo hiểm trên giá trị | `13 — insured above value, on` | insurance above value | 13.2, src:755 | "Over-insurance"; 1.10 forbids it by definition (finding X27). |
| tổn thất bộ phận | `14.1 — the reasonable cost of putting the partial loss right, on` | partial loss | 14.1, src:769; 15.1, src:896 | Low. |
| khấu hao | `14.1.2 — the depreciation rate, on` | depreciation | 14.1.2(b), src:792-802 | "Khấu hao" is accounting depreciation; here a deduction for new-for-old. |
| xe buýt | `a bus` | bus | 14.1.2(b), src:803 | Low. |
| xe kinh doanh vận tải hành khách chạy tuyến cố định/ nội tỉnh/ liên tỉnh | `a passenger transport business vehicle on a fixed, intra-provincial or inter-provincial route` | passenger transport on fixed or provincial routes | 14.1.2(b), src:803-804 | Low. |
| xe cho thuê tự lái | `a self-drive rental vehicle` | self-drive rental car | 14.1.2(b), src:804 | Low. |
| xe taxi | `a taxi` | taxi | 14.1.2(b), src:804 | Low. |
| phụ tùng cũ tương đương | `replaced with an equivalent used part, as the shop, the Policyholder and the Insurer agreed` | an equivalent used part | 14.1.2(b), src:821-822 | Low. |
| gas của hệ thống điều hòa nhiệt độ | `air-conditioning gas` | refrigerant | 14.1.2(c)-(d), src:826, 830 | Low. |
| nước mát | `coolant` | coolant | 14.1.2(c)-(d), src:827, 830 | Literally "cool water". |
| dầu bôi trơn | `lubricating oil` | lubricating oil | 14.1.2(c)-(d), src:827, 831 | Low. |
| ắc quy | `a battery` | battery | 14.1.2(d), src:831 | Low. |
| năm sử dụng đầu tiên | `14.1.2(d) — the rate in the first year of use` | the first year of use | 14.1.2(d), src:832-833 | A calendar year or twelve months (fork F28). |
| kính, mặt gương | `glass or a mirror` | glass, mirror faces | 14.1.2(d) note, src:839 | "mặt gương" is the mirror glass; the mirror housing is an ordinary part. |
| diện tích sơn | `share of the painted area damaged` | painted area | 14.1.4, src:845-846 | Low. |
| tổn thất toàn bộ | `14.2 — a total loss, for` | total loss | 14.2, src:848 | Includes a theft of the whole vehicle (14.2.2). |
| Thu hồi tài sản sau bồi thường | `14.3.2 — the share of the wreck the Insurer takes, on` | taking the property after paying | 14.3, src:872 | "Salvage" in English; here also the replaced parts. |
| Mức Khấu Trừ tối thiểu và bắt buộc | `15.2 — the minimum deductible` (500,000) | the minimum, mandatory deductible | 15.2, src:897 | Low. |
| Giảm trừ bồi thường | `A ground of reduction in Article 16`, `A reduction the Insurer may make` | reduction of the indemnity | 16, src:912 | Not a deductible: a percentage cut at the Insurer's choice. |
| Hợp Đồng Bảo Hiểm trùng | `9 — the Insurer's share under double insurance, on` | double insurance | 9, src:502-506 | The Law's definition is narrower (LAW fork L6, finding X22). |
| đang tham gia giao thông | `in traffic` | in traffic (on the road), not parked off it | 12.2, src:596; 12.3, src:616 | "Tham gia giao thông" (taking part in traffic) may or may not include a car parked on the street; an input. |
| sử dụng ma túy | `the Driver had used drugs or prohibited stimulants` | drug use, or prohibited stimulants | 12.4, src:623-624 | Low. |
| đi vào đường cấm | `a prohibited manoeuvre listed in 12.5` | entering a prohibited road, wrong way, prohibited turn, red light, ignoring a controller, no lights at night | 12.5, src:625-629 | One field for the whole list; a caller decides whether the manoeuvre is on it. |
| cấm dừng, cấm đỗ | `stopped or parked where prohibited, leading to the damage` | stopping or parking where prohibited | 12.6, src:630-631 | Low; 12.6 does ask for causation ("dẫn đến thiệt hại"). |
| chở hàng trái phép | `carrying goods unlawfully or without the loading safety rules` | carrying goods unlawfully, or unsafely | 12.8, src:635-637 | Low. |
| lãnh thổ nước CHXHCN Việt Nam | `in Vietnam` | the territory of the Socialist Republic of Vietnam | 12.9, src:640 | Low. |
| Chiến tranh, khủng bố, nội chiến, đình công, bạo động | `war, terrorism, civil war, strike or riot` | war, terrorism, civil war, strike, riot | 12.10, src:641-642 | "Bạo động" is a violent disturbance; "riot" is the nearest English. |
| không trung thực hoặc giả mạo | `claim information proven by the Insurer untruthful or forged` | untruthful or forged | 12.22, src:700-701 | Low; note the burden: "được Công Ty Bảo Hiểm chứng minh" (proven by the Insurer). |
| việc bỏ sót là do vô ý | `the omission was inadvertent` | the omission was inadvertent | 12.22, src:701 | Low. |
| độ/chế | `the loss was caused by the added equipment or the modification` | aftermarket modification | 12.19, src:692 | Colloquial ("độ xe"); "modification" is the sense. |
| Thông báo tổn thất | `date the Insurer was notified of the loss` | notice of the loss | 16.1.1, src:917-918; 5.2, src:331-332 | 16.1.1 asks for it "bằng văn bản" (in writing) or as the contract agrees; the field records only its date. |
| cứu chữa, hạn chế thiệt hại | `rescue and mitigation measures were not fully taken` | rescue and loss limitation | 16.1.1, src:925; 5.2, src:320-321 | Low. |
| địa hình dốc | `parked on a slope without brakes or chocks, so it rolled` | sloping ground | 16.1.1, src:929-930 | Low. |
| tự ý tháo gỡ hoặc sửa | `dismantled or repaired without the Insurer's approval` | dismantling or repairing on one's own initiative | 16.1.3, src:937 | Low. |
| bảo vệ hiện trường | `the scene was not protected or the vehicle was moved from it` | protecting the scene | 16.1.4, src:942 | Low. |
| bảo lưu quyền khiếu nại | `the Owner did not preserve and transfer the claim against the third party` | preserving the right to claim | 16.1.4, src:945 | "Khiếu nại" here is a claim against the third party, not a complaint to the Insurer (Article 10). |
| kê khai sai | `the use of the vehicle was misdeclared, so less premium was charged` | a wrong declaration | 16.1.6, src:967 | Low. |
| gia tăng mức độ rủi ro bảo hiểm | `an increase in risk was not notified` | an increase in the insured risk | 16.1.6, src:970 | Low. |
| số phí phải nộp | `premium that should have been paid` | the premium payable on the true facts | 16.1.6, src:965 | Low. |
| chuyển quyền sở hữu | `2.3 — the benefits pass to the transferee` | transfer of ownership | 2.3, src:140; 5.1, src:291 | Low. |
| chi phí sơn lại toàn bộ xe | `cost of repainting the whole vehicle` | the cost of repainting the whole vehicle | 14.1.4, src:845 | Low. |
| thay thế mới | `replaced with a new part` | replacement with a new part | 14.1.3, src:842 | Low. |
| giá trị thu hồi | `value of the wreck, as valued` | the recovery value of the wreck | 14.3.2, src:885 | The text values it by an authority the Insurer appoints, or by agreement; the field takes the figure. |
| bản án của tòa án có thẩm quyền | `a court judgment, or a decision to suspend the investigation or not to prosecute` | a judgment of a competent court | 14.2.2, src:854 | The decisions named are criminal-procedure decisions (đình chỉ điều tra, không khởi tố). |
| kết luận chính thức của cơ quan chức năng có thẩm quyền | `4.2 — the date the file counts as complete` | the competent authority's official conclusion | 4.2, src:245 | Low. |
| xác minh | `4.2 — the working days to pay`, `the Insurer must verify the file` | verification | 4.2, src:240 | Low. |
| Giám định tổn thất | `7 — the party who pays for the Insurer's assessment` | loss assessment | 7, src:395 | "Survey" or "loss adjustment" in English market usage. |
| đơn vị giám định độc lập | `7 — the party who pays for the independent assessment and the court fees` | independent assessor | 7, src:404 | Low. |
| Hồ sơ bồi thường | `A claim document`, `8 — the documents the claim file may include, for` | claim file | 8, src:427 | Low. |
| hệ thống bảo lãnh | `invoices for repair or replacement outside the Insurer's guarantee network` | the Insurer's network of repairers it guarantees payment to | 8.1, src:453 | "Guarantee network" is literal; "approved repairers" is the market meaning. |
| Thời hạn yêu cầu bồi thường | `10 — the last day to claim, for an event on` | the time limit for claiming | 10, src:533 | A contractual period, not a statutory limitation period. |
| khiếu nại | `10 — the last day to complain, notice received on` | complaint against the Insurer's decision | 10, src:536 | Low. |
| Thời hiệu khởi kiện | `10 — the last day to sue, the dispute having arisen on` | the limitation period for suit | 10, src:543 | "Thời hiệu" is a statutory concept; the contract restates it. |
| cơ sở sửa chữa | `BS02 — the Insured may choose the repair shop`, `BS02 — the repair cost OPES accepts` | repair shop | BS02, src:1027 | Low. |
| Mức giới hạn phụ | `sub-limit in the contract` | sub-limit | BS04, src:1074-1076 | BS04 defines it as the maximum total paid in the period. |
| Giới hạn trách nhiệm | `BS05 — the number of parts losses covered on` | limit of liability, as a number of losses | BS05, src:1097 | Here a count of losses ("02 lần"), not an amount. |
| hạn mức quyền lợi | `benefit limit in the contract` | benefit limit | BS06, src:1111 | Low. |
| nghỉ qua đêm | `cost of overnight stay and transport to the destination for the driver and occupants` | an overnight stay | BS06, src:1109 | Low. |
| hóa đơn tài chính hợp lệ | `valid financial invoices were supplied` | a valid VAT invoice | BS06, src:1113 | "Hóa đơn tài chính" is the official tax invoice; "receipt" would be too loose. |
| Cơ quan Đăng kiểm | `approved by the registry and within the inspection's validity` | the vehicle inspection authority | BS07, src:1126 | "Registry" is the encoder's word for the inspection authority, not the registration office. |
| Chủ thể dữ liệu | `a data subject` | a data subject (Policyholder, Insured or beneficiary) | personal data clause, src:1146 | Low; note it is wider than the Policyholder (finding X1). |
| Nghị định số 13/2023/NĐ-CP | `the date of Decree 13/2023` | the Decree on personal data protection of 17/04/2023 | personal data clause 8, src:1234-1235 | The Decree is not in the sources; what its Article 9 rights are is outside knowledge, unverified. |
| bất khả kháng | `force majeure prevented notice` | force majeure | 5.2, src:331; 16.1.1, src:920 | A legal excuse; not the natural-catastrophe peril. |
| đường dây nóng | `the hotline was told at the time of the accident` | the Insurer's hotline | 12.23, src:707; 16.1.1, src:922 | Low. |
