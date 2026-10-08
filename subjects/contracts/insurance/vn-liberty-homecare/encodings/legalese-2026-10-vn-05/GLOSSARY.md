# GLOSSARY — Liberty HomeCare (UW-RPP-W-001-06-V), row `legalese-2026-10-vn-05`

The bilingual key between the source's Vietnamese and the encoding's English.
Every Vietnamese cell is verbatim from `../../source/raw/liberty-homecare.txt` (checked by `tools/vnsrc.py check`); source line numbers are `src:N`.
One row for every term the document defines, and for every type, field or constant declared in `homecare-nouns.l4` (and the few declared in rule modules) that renders a Vietnamese concept.
The two tick-box enumerations, `A description of property` and `A circumstance of a loss` (and `A circumstance of a liability`), have one member per phrase of the source; their members are listed here only where the English choice carries a risk, and every member is quoted at the rule that uses it.

## Defined terms (CÁC ĐỊNH NGHĨA and the Part 2 additional definitions)

| Vietnamese term (verbatim) | English identifier in the L4 | English meaning, one line | where defined or used (Điều / clause, src line) | translation risk |
| --- | --- | --- | --- | --- |
| Hợp Đồng Bảo Hiểm | `the documents that make up the Insurance Contract`; "Insurance Contract" in comments | the contract: Proposal Form, these Rules, Summary or Certificate, Endorsements | Definitions, src:34-43 | "contract" and "policy" both fit; English wordings say "policy". Kept "Insurance Contract" because the Law uses the same words for the contract |
| Điều Khoản Sửa Đổi Bổ Sung | "Endorsement" (comments) | an amending or supplementing clause | Definitions, src:49-51 | literally "amending and supplementing clause"; "endorsement" is the English trade term |
| Giới Hạn Trách Nhiệm | `the Part 1 Limit of Liability`, `the Part 2 Limit of Liability for any one Occurrence`, `... for the Period` | the Insurer's maximum for claims under a Part, as the Summary states | Definitions, src:52-54 | Part 3 uses "Giới hạn Bồi thường" (limit of indemnity) for its own limits; treated as the same concept |
| Người Được Bảo Hiểm | `the Insured` (`A party`), `The Insured person` | the person or persons named in the Summary | Definitions, src:55-56; Part 2 redefines, src:490-497 | Vietnamese law distinguishes the insured person from the policyholder ("Bên Mua Bảo Hiểm"); this document uses one term for both roles |
| Công Ty Bảo Hiểm | `the Insurer` | Liberty Insurance Vietnam | Definitions, src:57-58 | literally "the insurance company"; "Insurer" is the role |
| Thời Hạn Bảo Hiểm | `the Period of Insurance begins` / `ends`; `within the Period of Insurance of` | the period stated in the Summary | Definitions, src:59-61 | "thời hạn" is both "term" and "time limit"; the document also uses it for the 72-hour period (src:395) |
| Bản Tóm Tắt Hợp Đồng Bảo Hiểm | `The Policy Summary` | the schedule: insureds, period, items, sums insured, limits, conditions | Definitions, src:62-65 | literally "summary of the insurance contract"; it works as the schedule, and is a binding part of the contract (src:63) |
| Giấy Yêu Cầu Bảo Hiểm | "Proposal Form" (comments; GC1 grounds) | the insurer's application form | Definitions, src:66-68 | literally "insurance request form" |
| Địa Điểm Bảo Hiểm | `the premises are the Insured Location` | the Insured's principal residence at the place in the Summary | Definitions, src:69-72 | literally "insurance location"; the definition requires the Insured's own residence, which matters for Part 3 rent (finding X-rent) |
| Ngôi Nhà | `the Home`; `the premises are a Home under`; `the property is part of the Home` | the house or apartment, owned or managed by the Insured, used as residence | Definitions, src:73-105 | "ngôi nhà" ordinarily means a house; the definition admits apartments ("căn hộ chung cư"), and exclusion (c) then names "các loại nhà và căn hộ" (finding X-home-c) |
| Chi Phí Tân Trang/Cải Tạo | `the Renovation Costs` | a tenant-Insured's improvements, fittings, built-ins | Definitions, src:106-110 | literally "renovation/improvement COSTS", but the definition is of the improvements themselves (property); the identifier keeps the source's name |
| Tài Sản Bên Trong Nhà | `the Contents`; `the property is Contents` | household goods, personal effects, antennas, office equipment, tools, at the Insured Location | Definitions, src:111-159 | literally "property inside the house", yet it includes antennas and garden appliances outside; "Contents" is the trade term |
| Tài sản cá nhân | `personal effects, normally carried or worn on the person` | personal items normally carried or worn | Contents (a), src:118-119 | "mang" is both "carry" and "wear"; the same verb in (j) "thường được mang ra ngoài" makes the overlap (finding X-personal-effects) |
| Tài sản quý | the four valuables members of `A description of property` | jewellery, precious metals and stones, art, furs, glass, crystal, antiques, special-value items | Contents excl. (i), src:152-154 | "đồ mỹ nghệ" may be "fine art" or "handicrafts" |
| Tài sản xách tay | `a laptop computer, mobile phone or camera`; `an item normally carried away from the Insured Location` | portable property | Contents excl. (j), src:155-157 | "xách tay" is "hand-carried"; read as portable (F-contents-j) |
| Các tài sản có thể chuyển giao thông qua việc xác nhận | `a negotiable instrument` | treasury notes, savings certificates, money orders, gift certificates, other transferable documents | Contents excl. (h), src:143-146 | literally "assets transferable by confirmation"; "negotiable instruments" is the English sense |
| Gia Đình Người Được Bảo Hiểm | `a relative is in the Insured's Family, being`; `A relation` | spouse, children and relatives regularly living with the Insured | Definitions, src:160-162 | whether "regularly living with" governs spouse and children (F-family) |
| Rủi Ro Được Bảo Hiểm | `A cause of loss`; `A ground under the Insured Perils` | the nine Insured Perils | Definitions, src:163-283 | literally "insured risks"; "peril" is the English term for a named cause |
| Mức Miễn Thường | `GC13: the Deductible stated in`; Summary fields `the Part 1 Deductible` etc. | the part of a claim the Insured bears | Definitions, src:284-285; GC13, src:972-978 | literally "exempt level"; "deductible" and "excess" both fit |
| Giá Trị Thực Tế | `the Actual Value` | new cost less depreciation and wear for age and condition | Definitions, src:286-289 | "actual value" can be heard as market value; the definition is an indemnity (new-less-wear) value |
| Sự Cố | "Occurrence"; `unexpected and unintended by the Insured` | an event the Insured neither expects nor intends, causing injury or damage | Part 2 definitions, src:476-481 | literally "incident"; the definition adds repeated exposure |
| Thương Tật Thân Thể | `A kind of harm` (`death`, `bodily injury, illness or disability`, `fright, shock, mental anguish or nervous injury`) | Bodily Injury, including death, illness, shock, mental anguish | Part 2 definitions, src:482-484 | wider than the ordinary "thương tật" (wound, injury) |
| Thiệt Hại về Tài sản | `A kind of harm` (`physical damage to or destruction of tangible property`, `loss of use of tangible property that is not physically damaged`) | Property Damage, including loss of use | Part 2 definitions, src:485-489 | none noted |
| Dữ Liệu Điện Tử | `loss, distortion, erasure or alteration of Electronic Data` | Electronic Data | GE 7(a), src:760-764 | none noted |
| Vi Rút Máy Tính | (within the Electronic Data circumstance) | Computer Virus | GE 7(a), src:765-769 | none noted |
| Rủi Ro Xác Định | `a Defined Peril (fire or explosion) resulting from it caused physical loss` | Defined Perils: Fire, Explosion | GE 7(a)(ii), src:770-775 | none noted |
| hành động khủng bố | `an act of terrorism` | act of terrorism, as GE1 defines it | GE 1, src:704-709 | none noted; but see "luật hôn nhân" below |
| Ngoài trời | `in the open` | at the Insured Location, outdoors, in unlockable parts, or in a vehicle | Peril 5, src:237-239 | none noted |
| Lũ lụt | `flood` | overflow of watercourses or the public main, water from outside the Home | Peril 5, src:218-220 | the heading says "lụt", the definition "Lũ lụt"; same peril |
| Rò rỉ từ hệ thống vòi phun tự động | `sprinkler leakage` | sudden discharge from an automatic sprinkler system | Peril 7, src:245-247 | none noted |

## Terms used but not defined

| Vietnamese term (verbatim) | English identifier in the L4 | English meaning, one line | where defined or used (Điều / clause, src line) | translation risk |
| --- | --- | --- | --- | --- |
| Sự Kiện Bảo Hiểm | "Insured Event" (comments; `the date of the event`) | the event that gives rise to a claim | Peril 4(iii), src:213; GC4, src:833 (lower case in GC9, src:933) | capitalised as a defined term, never defined (finding X-undefined) |
| Bên Mua Bảo Hiểm | none | the policyholder | Endorsement definition, src:51 | used once, never defined |
| Tài sản được Bảo hiểm | "insured property" (comments) | the insured property | src:426, 773, 897 | capitalised, never defined |
| Bảo hiểm Tai nạn Con người | `the Insured also has Personal Accident cover` | an additional Personal Accident section | Part 3 death benefit, src:665-666; GC8, GC9 | the section it names is not in the document |

## The Parts, perils and clauses

| Vietnamese term (verbatim) | English identifier in the L4 | English meaning, one line | where defined or used (Điều / clause, src line) | translation risk |
| --- | --- | --- | --- | --- |
| THIỆT HẠI VẬT CHẤT | `Part 1` (`A Part`) | Part 1, Material Damage | src:291 | none noted |
| TRÁCH NHIỆM CÁ NHÂN VÀ GIA ĐÌNH | `Part 2` | Part 2, Personal and Family Liability | src:431 | none noted |
| QUYỀN LỢI BỔ SUNG | `Part 3` | Part 3, Additional Benefits, free of charge | src:628 | none noted |
| Cháy | `fire` | Peril 1 | src:166 | none noted |
| Nổ | `explosion` | Peril 2 | src:174 | none noted |
| Sét đánh | `lightning` | Peril 3 | src:177 | none noted |
| Bạo động | `riot or civil disturbance` and the other limbs of Peril 4 | Peril 4, riot, strike, lockout, malicious act | src:179-192 | "Bạo động" is also used for "civil commotion" in 4(i)(b) |
| giông lốc | `storm` | Peril 5 | src:217 | "giông lốc" (thunder-squall), "gió xoáy" (whirlwind), "bão" (typhoon) overlap; 5(g) and Ext 7 say "bão hoặc giông tố" and "lốc xoáy, giông bão" |
| gió xoáy | `whirlwind` | Peril 5 | src:217 | as above |
| bão | `typhoon` | Peril 5 | src:217 | "bão" is any tropical storm; "typhoon" is the usual regional rendering |
| Thiệt hại do đâm va bởi | `impact by aircraft or articles dropped from it`; `impact by a vehicle or animal` | Peril 8 | src:260-262 | none noted |
| Việc trộm cắp hoặc toan tính trộm cắp | `theft or attempted theft` | Peril 9 | src:263-264 | none noted |
| tường rào | `enclosed by walls or fences` | perimeter wall or fence | Peril 9, src:263 | may mean "secured premises" in the source wording; read literally (finding X-fence) |
| bạo lực hoặc vũ lực | `force or violence used to enter`; `... to leave` | force or violence | Peril 9, src:264 | none noted |
| bỏ trống | `the Home was vacant or unoccupied when the loss occurred`; `consecutive days the Home had been vacant` | vacant | Peril 6(b), src:243; GC3(d), src:828 | different from "bỏ mặc hoặc không ai trông coi" (left unattended), Peril 9(d), src:275; both kept (finding X-vacancy) |
| Cặp và Bộ | `A pair or set`; `Pairs and Sets: the cap on` | Pairs and Sets | Part 1, src:324-328 | none noted |
| CƠ SỞ THỰC HIỆN BỒI THƯỜNG | `the cost of reinstatement`; `Part 1: the cost after Provisions 1 to 3, for` | basis of settlement | Part 1, src:301-312 | none noted |
| GIỚI HẠN TRÁCH NHIỆM - TỔNG QUÁT | `General Limit: what remains for` | General Limit of Liability | Part 1, src:330-336 | none noted |
| BẰNG CHỨNG GIÁ TRỊ | `kept receipts or proof of value`; `Part 1: the Insured keeps proof of value` | proof of value | Part 1, src:338-341 | none noted |
| Định giá | `Extension 2: ...` | valuation (no inventory of undamaged property) | Ext 2, src:348-354 | literally "valuation"; its content is a waiver of inventory for an average calculation the document lacks |
| Điều chỉnh Thời gian | `Extension 7: ...` | the 72-hour clause | Ext 7, src:393-401 | literally "time adjustment" |
| QUYỀN PHÁN QUYẾT | `the Jurisdiction clause excludes`; `A forum` | jurisdiction | Part 2, src:464-469 | literally "right of judgment" |
| phán quyết sơ thẩm | `a first-instance judgment of a competent Vietnamese court` | first-instance judgment | Part 2, src:466-467 | likely a rendering of "judgment of a court in Vietnam"; read literally (finding X-appeal) |
| chểnh mảng | `a negligent act of the Insured or a Family member` | negligent, careless | Part 2 excl. 1, src:533 | the likely source is "wilful" or "malicious"; "chểnh mảng" means careless (finding X-negligence) |
| thường sống chung | `the person injured is Family or usually resides with the Insured` | usually residing with | Part 2 excl. 3, src:539-547 | none noted; but see F-excl3 on "đã sử dụng Ngôi Nhà" |
| Trách nhiệm của người thuê nhà | `the tenant's liability Extension applies to` | tenant's liability | Part 2 Extension, src:514-523 | none noted |
| CHI PHÍ PHÁT SINH THÊM CHO CHỖ Ở TẠM THỜI | `A temporary accommodation claim`; `Part 3: the accommodation or rent payable, under` | additional cost of temporary accommodation | Part 3, src:630-654 | the heading also covers loss of rent (limb 1) |
| Tiền cho thuê | `rent lost` | rent | Part 3 limb 1, src:632-638 | none noted |
| BỒI THƯỜNG TỬ VONG CHO NGƯỜI ĐƯỢC BẢO HIỂM | `A death benefit claim`; `Part 3: the death benefit payable, under` | death benefit | Part 3, src:656-666 | "bồi thường" is "compensation"; the amount is not stated (F-death-amount) |
| người giúp việc | `a domestic helper`; `A domestic helper claim` | domestic helper | Part 3, src:668-682 | none noted |
| luật hôn nhân | in `mutiny, popular rising, insurrection, rebellion, usurped power, martial law or siege` | literally "marriage law"; read as martial law | GE 1(c), src:696-697 | a mistranslation; the identifier says "martial law" (finding X-translation) |
| hàng hóa | `some part is used to manufacture, deposit or store goods` | goods, merchandise | GE 8, src:791 | merchandise, not household belongings |
| Tuân thủ thích đáng | GC1 grounds | due observance, conditions precedent | GC1, src:802-807 | none noted |
| Mô tả Sai | `GC2: the Insurer avoided the policy for misdescription` | misdescription | GC2, src:808-810 | "có thể bị mất hiệu lực" (may become void) read as voidable (F-gc2) |
| Thủ tục Yêu cầu Bồi thường | GC4 grounds; `GC4: the Insured's notice and claim, with days allowed` | claims procedure | GC4, src:832-852 | none noted |
| Mất Quyền Lợi | GC7 grounds | forfeiture | GC7, src:903-915 | none noted |
| kháng nghị | `the date the rejection was challenged`; `the date the award was challenged` | challenge, objection | GC7(b), src:910, 914 | in court procedure "kháng nghị" is a procuracy protest; here the Insured's objection or appeal |
| Thế quyền | `GC8: the claimant does what subrogation requires` | subrogation | GC8, src:916-926 | none noted |
| Đóng Góp Bồi Thường | `GC9: the rateable proportion of` | contribution | GC9, src:932-938 | none noted |
| Trọng tài | `GC10: either party may refer a dispute to VIAC` | arbitration | GC10, src:939-946 | none noted |
| Hủy bỏ Hợp đồng | GC11 rules | cancellation | GC11, src:947-956 | "hủy bỏ" in the Law is rescission with retroactive effect; here prospective cancellation with refund |
| Biểu Phí Ngắn Hạn | `the short-period scale`; `A row of the short-period scale` | short-period scale | GC11, src:957-962 | none noted |
| Phí Bảo hiểm năm | `the annual premium` | annual premium | GC11, src:959-962 | none noted |
| Các Biện pháp Đề phòng Hợp lý | `GC12: the Insured takes reasonable precautions` | reasonable precautions | GC12, src:963-971 | none noted |
| Luật và Tập quán | `GC14: the governing law` | law and practice | GC14, src:979-980 | the heading names "practice" (tập quán); the text names only the law |

## Types and fields that render a source concept

| Vietnamese term (verbatim) | English identifier in the L4 | English meaning, one line | where defined or used (Điều / clause, src line) | translation risk |
| --- | --- | --- | --- | --- |
| căn nhà | `a house` (`A kind of building`) | a house | Home, src:74 | none noted |
| căn hộ chung cư | `an apartment in an apartment building` | an apartment in a block | Home, src:74 | overlaps "căn hộ có chủ quyền theo tầng" |
| căn hộ có chủ quyền theo tầng | `a strata-title apartment` | an apartment held under strata title | Home excl. (c), src:93 | in Vietnam most owned apartments are strata-titled (outside knowledge, unverified), so the excluded kind may swallow the included one |
| khách sạn | `a hotel` | hotel | Home excl. (c), src:93 | none noted |
| nhà nghỉ | `a motel or guest house` | guest house | Home excl. (c), src:93 | none noted |
| bệnh xá | `an infirmary` | infirmary | Home excl. (c), src:93 | none noted |
| nhà trọ | `a boarding house` | boarding house, rented rooms | Home excl. (c), src:93 | none noted |
| nhà lưu động | `a mobile home` | mobile home, caravan | Home excl. (c), src:94; Contents excl. (c), src:133 | in Contents (c) and (f) it sits beside "xe moóc" (trailer) |
| máy bay không lái được | `an aircraft that cannot be piloted` | literally "aircraft that cannot be flown or steered" | Contents excl. (e), src:135 | probably meant unmanned or model aircraft; kept literal |
| vợ/chồng | `a spouse` (`A relation`) | spouse | Family, src:161 | none noted |
| con cái | `a child` | children | Family, src:161 | none noted |
| thân nhân | `another relative` | relatives | Family, src:161 | none noted |
| số tiền bảo hiểm | `the sum insured on the Home`, `... the Renovation Costs`, `... the Contents` | sum insured | Part 1, src:298, 332 | none noted |
| Tổng Số tiền Bảo hiểm của Phần 1 | `the total sum insured under Part 1 of` | total Part 1 sum insured | Part 3, src:653 | not defined; taken as the sum of the item sums insured (F-total-si) |
| tổn thất, phá hủy hoặc thiệt hại | `An extent of loss` (`lost or destroyed`, `damaged`) | loss, destruction or damage | Part 1 scope, src:294; basis (a)-(b), src:302, 311 | none noted |
| bất ngờ không lường trước được | `sudden and unforeseen` | sudden and unforeseen | Part 1 scope, src:294 | none noted |
| tại hoặc gần Địa Điểm Bảo Hiểm | `at or near the Insured Location` | at or near the Insured Location | Part 2 scope, src:439 | none noted |
| quyền sở hữu hoặc sử dụng Ngôi Nhà | `connected with the ownership or use of the Home` | ownership or use of the Home | Part 2 scope, src:440 | none noted |
| với tư cách là chủ nhà | `landlord not occupying the Insured Location` (`A capacity`) | as landlord | Part 3 limb 1, src:632 | none noted |
| Người sử dụng kiêm Chủ sở hữu | `owner-occupier` | owner-occupier | Part 3 limb 2, src:639-640 | none noted |
| độ tuổi | `age in completed years, born on` | age | Part 3 death benefit, src:663 | completed years on the day of injury (F-age) |
| bằng thư đảm bảo | `send written notice of cancellation by registered post` | by registered post | GC11, src:948-949 | none noted |
| công ty | `issued to a company` | a company | Part 3 death benefit, src:664 | none noted |
