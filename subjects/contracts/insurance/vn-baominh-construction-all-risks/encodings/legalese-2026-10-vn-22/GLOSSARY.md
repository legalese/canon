# GLOSSARY — Vietnamese source, English encoding (row `legalese-2026-10-vn-22`)

Every Vietnamese run below is copied from `../../source/raw/baominh-car.txt` and checked verbatim by `tools/vnsrc.py check`.
"Line N" is line N of that file.
The document defines almost nothing (General Condition 2 presupposes definitions it never gives; finding X20), so most rows are the encoder's rendering of an undefined term, and the `translation risk` column is where that choice is argued.
Identifiers are the names declared in `bmcar-nouns.l4` unless another module is named.
Encoder bookkeeping with no Vietnamese counterpart (`description`, `as at`, `item number` as a bare number, the fixture names) has no row.

## The parties and the instrument

| Vietnamese term (verbatim) | English identifier in the L4 | English meaning, one line | where defined or used (Điều / clause, src line) | translation risk |
| --- | --- | --- | --- | --- |
| "Bảo Minh" ("Tổng Công ty Cổ Phần Bảo Minh") | `Bao Minh` (of `A party to the policy`) | the insurer | recital, lines 5-6 (defined: "sau đây gọi tắt là") | a proper name; written without diacritics in identifiers only |
| "Người được bảo hiểm" | `the Insured` | the insured named in the Schedule | recital, line 5; passim | The Law distinguishes the policyholder from the person insured; this document names only "Người được bảo hiểm" and puts every duty on it, the premium included, so `the Insured` here also bears the policyholder's duties. |
| "Đơn bảo hiểm này" | none: "the Policy" in comments | this Policy, including the Schedule and the following parts | General Condition 2, lines 62-64 | "Đơn bảo hiểm" is both the policy document and the contract; General Condition 2 fixes only its extent. |
| "Phụ lục" | `The Schedule`, `the Schedule` | the schedule of the Insured, items, sums, limits, deductibles, dates and premium | lines 5, 12, 45, 51, 62 | Usually "appendix"; "Schedule" is the insurance term for what it does here. Its contents are not in the document, so every figure in it is an input. |
| "giấy yêu cầu bảo hiểm", "Bản câu hỏi" | `the answers in the questionnaire and the proposal were true` | the proposal form, completed by answering the questionnaire | recital, lines 6-7; General Condition 1, line 59 | The recital's deeming of the proposal is never completed (finding X1). |
| "điều kiện tiên quyết" | `General Condition 1 — the conditions precedent to liability are met`; `General Condition 7 — an action against Bao Minh is barred for want of an award` | condition precedent | General Condition 1, line 59; General Condition 7, line 133 | Literally "prerequisite". "Condition precedent" imports the common-law consequence (any breach defeats liability without prejudice); how strictly Vietnamese law applies it is a question of that law (forks F9, F38). |
| "phí bảo hiểm" | `the premium stated in the Schedule`; `the premium has been paid` | the premium | insuring agreement, line 12 | none |
| "sự cố" | `the date of the occurrence` (and "occurrence" throughout) | the event a claim arises from; the unit of the deductible and of the limits | lines 86, 103, 159, 163, 174, 285, 321 | "Incident" or "occurrence". English "occurrence" carries a body of aggregation law (one event or many) that the undefined Vietnamese does not (X20). |
| "tổn thất" | "loss" in identifiers | loss or damage | passim | covers both loss and damage; the English uses "loss" for the pair |

## The period of insurance

| Vietnamese term (verbatim) | English identifier in the L4 | English meaning, one line | where defined or used (Điều / clause, src line) | translation risk |
| --- | --- | --- | --- | --- |
| "thời hạn bảo hiểm" | `the occurrence on … falls within the period of insurance of …` | the period of insurance | heading, line 42; lines 153, 267 | "thời hạn" is both a period and a deadline; here a period |
| "khởi công công trình" | `the date work on the site commenced` | the commencement of the works | period, line 44 | "khởi công" is the formal start of construction, often a dated milestone; "work commenced" could be read as any preparatory work. |
| "dỡ xong các hạng mục có tên trong Phụ lục xuống công trường" | `the date the items entered in the Schedule were unloaded at the site` | completion of unloading of the scheduled items at the site | period, lines 44-45 | "dỡ xong" is completion of unloading, not its start (fork F5) |
| "ngày quy định trong phụ lục" | `the date the Schedule states the insurance begins` | the start date the Schedule states | period, line 45 | Declared, never read: the clause says it does not govern (F6, X3). |
| "bàn giao" | `the damaged part had been handed over before the occurrence` | handed over | period, line 47 | the market's English is "taken over"; same act |
| "đưa vào sử dụng" | `the damaged part had been put into use before the occurrence` | put into use | period, lines 47-48 | joined to "bàn giao" by "và" (F7) |
| "Chậm nhất thì bảo hiểm này sẽ chấm dứt hiệu lực vào ngày quy định ghi trong Phụ lục" | `the date the Schedule states the insurance ends`; `the date the insurance ends at the latest` | the end of the period | period, line 51 | inclusive (F8) |
| "sự gia hạn" | `the end date of an extension agreed by Bao Minh in writing` | an extension of the period | period, line 52 | none |

## The Schedule's figures

| Vietnamese term (verbatim) | English identifier in the L4 | English meaning, one line | where defined or used (Điều / clause, src line) | translation risk |
| --- | --- | --- | --- | --- |
| "hạng mục" | `An item entered in the Schedule`; `the item` | an item of the Schedule (item 1 the works; items 2 and 3 plant and machinery) | Section I, line 153; Article I, lines 206, 210 | **High.** Also used for components of the works (exclusion (d), line 182, and line 114); the insuring clause uses "bộ phận" for parts (line 153). Fork F22, finding X14. |
| "số tiền bảo hiểm" | `sum insured` | the sum set against the item | Section I, line 158; Article I, line 204 | none |
| "tổng số tiền được bảo hiểm ở phần này" | `the total sum insured under Section I` | the Section's total sum insured | Section I, line 160 | none |
| "hạn mức trách nhiệm bồi thường đó" | `the limit of indemnity for any one occurrence under Section I` | a per-occurrence limit, where the Schedule stipulates one | Section I, line 159 | "đó" (that) has no antecedent (X13); taken as optional (F18) |
| "chi phí dọn dẹp hiện trường" | `the cost of clearance of debris`; `the separate sum for clearance of debris` | clearance of debris; the separate sum for it | Section I, lines 162-164 | Literally "clearing the scene"; "debris removal" is the term of art and may be read more narrowly. |
| "Mức khấu trừ" | `the deductible under Section I for each occurrence`; `the deductible under Section II for each occurrence` | the deductible | Section I exclusion (a), line 173; Section II exclusion 1, line 285 | "deductible" and "excess" are used interchangeably in the market; none |
| "hạn mức bồi thường ghi trong Phụ lục" | `the limit of indemnity under Section II` | the Section II limit | Section II, lines 278-279 | per occurrence or aggregate is not said (F30) |

## Article 3 and the policy in force

| Vietnamese term (verbatim) | English identifier in the L4 | English meaning, one line | where defined or used (Điều / clause, src line) | translation risk |
| --- | --- | --- | --- | --- |
| "Chi phí cho việc làm thêm giờ, làm việc ban đêm, làm việc trong ngày lễ, cước phí vận chuyển hoả tốc" | `overtime, night work, holiday work and express freight were agreed in writing in advance`; `of which, overtime, night work, holiday work or express freight` | overtime, night work, holiday work, express freight | Article 3, lines 252-253 | "ngày lễ" is a public holiday, not any day off |
| "thoả thuận riêng trước bằng văn bản" | same | specially agreed in writing in advance | Article 3, line 253 | none |

## The Insured's conduct (General Conditions 1, 3, 4, 6)

| Vietnamese term (verbatim) | English identifier in the L4 | English meaning, one line | where defined or used (Điều / clause, src line) | translation risk |
| --- | --- | --- | --- | --- |
| "mọi biện pháp đề phòng hợp lý", "mọi kiến nghị hợp lý của Bảo Minh" | `took every reasonable precaution and followed Bao Minh's reasonable recommendations` | reasonable precautions and recommendations | General Condition 3, lines 68-69 | none |
| "mọi quy chế, kiến nghị của người sản xuất" | `complied with the regulations and the manufacturer's recommendations` | regulations and the manufacturer's recommendations | General Condition 3, line 70 | Ambiguous: "the manufacturer's regulations and recommendations", or "regulations, and the manufacturer's recommendations"; "quy chế" is rules or regulations, not necessarily statutory. |
| "mọi chi tiết, thông tin cần thiết để đánh giá rủi ro được bảo hiểm" | `gave Bao Minh's representatives the details and information needed to assess the risk` | information to assess the risk | General Condition 4(a), line 74 | none |
| "sự thay đổi quan trọng" | `there was a material change in the risk` | a material change | General Condition 4(b), line 77 | "quan trọng" is "important" or "significant"; "material" carries the insurance-law sense of what would influence a prudent insurer, which the Vietnamese does not define. |
| "bằng điện tín và bằng văn bản" | `notified the material change immediately, by telegram and in writing` | by telegram and in writing | General Condition 4(b), lines 76-77 | "điện tín" is a telegram, not telex or e-mail; read literally (F10, X6) |
| "các biện pháp phòng ngừa cần thiết mà hoàn cảnh yêu cầu" | `took the additional precautions the change required` | precautions the circumstances require | General Condition 4(b), line 78 | "additional" is the encoder's, from context |
| "không được tự ý tiến hành hay chấp nhận bất cứ sự thay đổi quan trọng nào làm tăng mức độ rủi ro" | `made or admitted a material change increasing the risk without Bao Minh's written approval` | no unapproved risk-increasing change | General Condition 4, lines 82-83 | "chấp nhận" (accept) rendered "admit" |
| "mọi hành động và mọi công việc xét thấy cần thiết hay theo yêu cầu của Bảo Minh" | `did and permitted the acts Bao Minh required to enforce rights against third parties` | subrogation assistance | General Condition 6, lines 117-119 | none |
| "với chi phí do Bảo Minh chịu" | `General Condition 6 — the party who bears the cost of the acts subrogation requires` | at Bảo Minh's expense | General Condition 6, line 117 | none |
| "bằng chi phí của riêng mình" | `General Condition 3 — the party who bears the cost of the precautions` | at the Insured's own expense | General Condition 3, line 68 | none |

## The notice and the Insured's conduct after an occurrence (General Condition 5; Section II Condition 1)

| Vietnamese term (verbatim) | English identifier in the L4 | English meaning, one line | where defined or used (Điều / clause, src line) | translation risk |
| --- | --- | --- | --- | --- |
| "Lập tức thông báo ngay" | `given immediately` | notify immediately | General Condition 5(a), line 89 | "lập tức" and "ngay" both mean "immediately"; no period is given (F11) |
| "bằng điện thoại hay điện tín" | `by telephone or telegram` | by telephone or telegram | General Condition 5(a), line 89 | none |
| "cũng như bằng văn bản" | `in writing` | as well as in writing | General Condition 5(a), lines 89-90 | "cũng như" is conjunctive: both media |
| "nêu rõ tính chất và mức độ tổn thất" | `stating the nature and extent of the loss` | stating nature and extent | General Condition 5(a), line 90 | none |
| "Bảo Minh không nhận được thông báo tổn thất" | `the date Bao Minh received the notice` | receipt of the notice | General Condition 5, lines 103-104 | "nhận được" is receipt, not dispatch |
| "trong vòng 14 ngày kể từ ngày xảy ra sự cố" | `the number of days from the occurrence within which Bao Minh must receive notice` (14) | 14 days from the day of the occurrence | General Condition 5, line 103 | "ngày" is not said to be calendar or working days (F12) |
| "hạn chế tổn thất ở mức thấp nhất" | `took all steps within its power to minimise the loss` | minimise the loss | General Condition 5(b), lines 92-93 | none |
| "Bảo quản các bộ phận bị tổn thất" | `preserved the damaged parts and made them available for inspection` | preserve the damaged parts | General Condition 5(c), line 95 | none |
| "Cung cấp mọi thông tin và chứng từ, văn bản theo yêu cầu của Bảo Minh" | `furnished the information and documents Bao Minh required` | furnish information and documents | General Condition 5(d), line 98 | none |
| "Thông báo cho cơ quan Công an" | `informed the police` | inform the police | General Condition 5(e), line 100 | "Công an" is the public-security police |
| "hư hỏng nhỏ" | `repaired, before an inspection, damage that was not minor` | minor damage | General Condition 5, line 107 | undefined (F13, X20) |
| "một thời gian được xem là hợp lý xét theo tình hình thực tế" | `the period reasonable in the circumstances, in days` (`bmcar-general-conditions.l4`) | a reasonable period for inspection | General Condition 5, lines 111-112 | no criteria (X7) |
| "không được sửa chữa kịp thời chu đáo" | `damaged in an earlier occurrence and not then repaired properly without delay` | not repaired promptly and properly | General Condition 5, line 115 | "kịp thời" is "in good time"; "chu đáo" "thoroughly" |
| "một sự thừa nhận, một đề xuất, một hứa hẹn thanh toán hay bồi thường" | `made an admission, offer, promise or payment without Bao Minh's written consent` | an admission, offer, promise or payment | Section II Condition 1, lines 312-313 | none |

## Causes (General Exclusions; Section I exclusions (c), (d), (e), (f); Section II exclusions 3, 4(c))

| Vietnamese term (verbatim) | English identifier in the L4 | English meaning, one line | where defined or used (Điều / clause, src line) | translation risk |
| --- | --- | --- | --- | --- |
| "trực tiếp hay gián tiếp gây nên bởi" | `the causes` (a list) | directly or indirectly caused by | General Exclusions, lines 19-20 | how remote a cause counts is not said (F3) |
| "Chiến tranh, xâm lược, hành động thù địch của nước ngoài, chiến sự" | `war, invasion, act of foreign enemies or hostilities, whether war be declared or not` | war and hostilities | General Exclusion (a), line 22 | none |
| "nội chiến, bạo loạn, cách mạng, khởi nghiã, binh biến, nổi loạn" | `civil war, rebellion, revolution, insurrection or mutiny` | civil war and rebellion | General Exclusion (a), lines 23-24 | "bạo loạn" can be riot or rebellion; grouped here with rebellion, and "bạo động của quần chúng" with riot. The grouping does not change the answer: all six groups are in (a). |
| "đình công, bãi công, bế xưởng, bạo động của quần chúng" | `riot, strike, lock-out or civil commotion` | strike, lock-out, riot | General Exclusion (a), line 24 | "đình công" and "bãi công" both mean strike |
| "hành động quân sự hay lực lượng tiếm quyền" | `military or usurped power` | military or usurped power | General Exclusion (a), lines 24-25 | "hành động quân sự" is literally "military action" |
| "hành động của nhóm người hay những người thù địch" | `the acts of hostile persons acting for or in connection with a political organisation` | political violence | General Exclusion (a), lines 25-26 | none |
| "tịch biên, tịch thu hay phá huỷ theo lệnh của chính phủ thực tế tồn tại" | `confiscation, requisition or destruction by order of a government de jure or de facto or of any public authority` | confiscation by government order | General Exclusion (a), lines 26-28 | "tịch biên" is distraint rather than requisition; "chính phủ thực tế tồn tại" (a government that actually exists) is the de facto limb, with the English "(de jure or de facto)" left in the source. |
| "Phản ứng hạt nhân, phóng xạ hạt nhân hay nhiễm phóng xạ" | `nuclear reaction, nuclear radiation or radioactive contamination` | nuclear | General Exclusion (b), line 30 | none |
| "Hành động cố ý hay cố tình sơ xuất của Người được bảo hiểm hay đại diện của họ" | `a wilful act or wilful negligence of the Insured or its representatives` | wilful act or wilful negligence | General Exclusion (c), line 32 | "đại diện" may be a legal representative or any agent: whose acts count is open |
| "Ngừng công việc dù là toàn bộ hay một phần" | `cessation of work, whole or partial` | cessation of work | General Exclusion (d), line 34 | none (X24) |
| "thiết kế sai" | `faulty design` | faulty design | Section I exclusion (c), line 179 | "sai" is "wrong": an error, which may be narrower than an inadequate design |
| "khuyết tật của vật liệu hoặc tay nghề" | `defective material or workmanship in the item itself`; `of which, replacing, repairing or rectifying defective material or workmanship` | defective material or workmanship | Section I exclusion (d), line 181 | see "hạng mục" |
| "Ăn mòn, mài mòn, ô xy hoá, mục rữa do ít sử dụng hay do điều kiện áp suất, nhiệt độ bình thường" | `corrosion, wear, oxidation or deterioration due to lack of use or normal pressure and temperature` | wear, corrosion, deterioration | Section I exclusion (e), line 186 | "normal pressure and temperature" is narrower than "normal atmospheric conditions" (humidity is not named); qualifier scope F23 |
| "Đổ vỡ cơ học và/hoặc do điện hay do sự trục trặc của các trang thiết bị và máy móc xây dựng" | `mechanical or electrical breakdown or derangement of construction plant, equipment or machinery` | breakdown of plant | Section I exclusion (f), lines 189-190 | "đổ vỡ" is breakage or collapse, "trục trặc" malfunction (F24) |
| "chấn động hay do bộ phận chống đỡ bị chuyển dịch hay suy yếu" | `vibration or the removal or weakening of support` | vibration, removal or weakening of support | Section II exclusion 3, line 290 | "chuyển dịch" is shifting rather than removal |
| "Thiệt hại đối với tài sản hay đất đai hay nhà cửa do chấn động" | `damage to property, land or buildings caused by vibration or by the removal or weakening of support` | damage by vibration, as a cause of further harm | Section II exclusion 3, lines 290-292 | second limb, F32 |
| "tai nạn gây ra bởi xe cơ giới được phép lưu hành trên đường công cộng hay bởi tàu thuyền, xà lan hay máy bay" | `an accident caused by a vehicle licensed for public roads, or by a ship, barge or aircraft` | vehicles, vessels, aircraft | Section II exclusion 4(c), lines 304-305 | none |
| "trộm cắp" | `theft` | theft | General Condition 5(e), line 100 | none |

## Kinds of property (Section I exclusions (f), (g), (h))

| Vietnamese term (verbatim) | English identifier in the L4 | English meaning, one line | where defined or used (Điều / clause, src line) | translation risk |
| --- | --- | --- | --- | --- |
| "trang thiết bị và máy móc xây dựng" | `construction plant, equipment or machinery` | construction plant and machinery | Section I exclusion (f), lines 189-190; Article I, line 210 | none |
| "xe cơ giới được phép sử dụng trên đường công cộng" | `a motor vehicle licensed for use on public roads` | licensed road vehicle | Section I exclusion (g), line 192 | Section II 4(c) says "được phép lưu hành" for the same idea |
| "tàu thuỷ" | `a ship` | ship | Section I exclusion (g), line 193 | any powered vessel |
| "xà lan" | `a barge` | barge | Section I exclusion (g), line 193 | none |
| "hồ sơ" | `files` | files | Section I exclusion (h), line 195 | dossier or records |
| "sơ đồ" | `drawings` | drawings, plans | line 195 | "diagram"; plans and drawings |
| "chứng từ kế toán" | `accounting records` | accounting records | line 195 | none |
| "hoá đơn" | `bills or invoices` | bills, invoices | line 195 | none |
| "tiền mặt" | `cash` | cash | line 195 | none |
| "tem phiếu" | `stamps or coupons` | stamps, coupons | line 195 | none |
| "văn bản" | `documents` | documents | line 196 | overlaps "hồ sơ" |
| "chứng thư nợ nần" | `evidences of debt` | evidences of debt | line 196 | none |
| "cổ phiếu" | `share certificates` | shares | line 196 | none |
| "thư bảo lãnh" | `letters of guarantee` | letters of guarantee | line 196 | none |
| "séc" | `cheques` | cheques | line 196 | none |

## A loss to an item, and its valuation (Section I; Articles I and 2)

| Vietnamese term (verbatim) | English identifier in the L4 | English meaning, one line | where defined or used (Điều / clause, src line) | translation risk |
| --- | --- | --- | --- | --- |
| "tổn thất vật chất" | `physical loss or damage` | physical loss or damage | Section I, line 154 | none |
| "bất ngờ và không lường trước được" | `sudden and unforeseen` | sudden and unforeseen | Section I, line 154 | the two words overlap; one field for both |
| "với mức độ cần thiết phải sửa chữa hoặc thay thế" | `to an extent that requires repair or replacement` | requiring repair or replacement | Section I, line 155 | none |
| "chỉ phát hiện được vào thời điểm kiểm kê" | `discovered only when an inventory was taken` | inventory losses | Section I exclusion (i), line 198 | none |
| "tổn thất có thể sửa chữa được" | `repairable, at a necessary cost of` | a repairable loss | Article 2(a), line 227 | none |
| "chi phí cần thiết để phục hồi các hạng mục bị tổn thất trở lại trạng thái như trước khi xảy ra tổn thất" | `the cost necessary to restore the item to its condition immediately before the occurrence` | the necessary cost of restoring | Article 2(a), lines 227-228 | none |
| "tổn thất toàn bộ" | `a total loss` | total loss | Article 2(b), line 231 | the constructive case is lines 240-242 |
| "trị giá thực tế của hạng mục đó ngay trước khi xảy ra sự cố" | `the actual value immediately before the occurrence` | actual value before the occurrence | Article 2(b), lines 231-232 | "trị giá thực tế" is not defined: market value, or replacement cost less depreciation; the gap between it and Article I's replacement value is finding X15 |
| "phần thu hồi", "phần trị giá thu hồi" | `the value of salvage` | salvage | Article 2, lines 228, 232 | none |
| "chi phí mà Người được bảo hiểm thực tế phải gánh chịu" | `the cost the Insured has actually incurred in repairing or replacing it` | cost actually incurred | Article 2, line 234 | "gánh chịu" is "borne"; F27 |
| "được tính chung trong số tiền bảo hiểm" | `the part of the loss not included in the sum insured` | what the sum insured includes | Article 2, line 235 | none |
| "các hoá đơn, chứng từ cần thiết" | `the invoices and documents showing the repair or replacement were produced` | invoices proving repair or replacement | Article 2, line 238 | none |
| "Chi phí sửa chữa tạm thời" | `of which, provisional repairs not part of the final repairs or increasing their cost` | provisional repairs | Article 2, lines 244-245 | none |
| "sửa đổi, bổ sung và/hoặc hoàn thiện thêm" | `of which, alterations, additions or improvements` | alterations, additions, improvements | Article 2, line 247 | none |
| "Trị giá đầy đủ của công trình theo hợp đồng tại thời điểm hoàn thành việc xây" | `The full contract value of the works at completion`; `the contract value at completion, with all materials, wages, freight, customs duties and other taxes` | full contract value at completion | Article I, lines 206-207 | "theo hợp đồng" (under the contract) may mean the contract price only (F25) |
| "nguyên vật liệu hay các hạng mục do chủ công trình (bên A) cung cấp" | `the value of materials or items supplied by the principal` | the principal's materials | Article I, line 208 | "chủ công trình" is the owner or employer, "bên A" the contract's Party A; "principal" is the market term |
| "Trị giá thay thế của trang thiết bị và máy móc xây dựng" | `the replacement value by a new item of the same kind and capacity` | replacement value new | Article I, lines 210-211 | "cùng tính năng" is "the same function or performance", rendered "capacity" |
| "số tiền lẽ ra phải yêu cầu bảo hiểm" | `Article I — the sum for which the item should have been insured` (`bmcar-section-1.l4`) | the sum that should have been insured | Article I, lines 218-219 | none |
| "tổn thất có tính chất hậu quả" | `the consequential losses claimed` | consequential loss | Section I exclusion (b), line 176 | the examples (penalties, delay, failure to perform, loss of contract) are inclusive |

## Claims, arbitration and forfeiture (General Conditions 7, 8, 9)

| Vietnamese term (verbatim) | English identifier in the L4 | English meaning, one line | where defined or used (Điều / clause, src line) | translation risk |
| --- | --- | --- | --- | --- |
| "tranh chấp về số tiền bồi thường" | `General Condition 7 — the difference must be referred to arbitration` | a dispute about the amount | General Condition 7, line 126 | none |
| "Trọng tài chung" (line 128) | `a single arbitrator appointed by both parties` | the single arbitrator | General Condition 7, line 128 | **High.** The same words name the umpire at lines 131-132 (X9). |
| "hai Trọng tài" | `the two arbitrators` | the two party-appointed arbitrators | General Condition 7, line 129 | none |
| "trọng tài chung" (lines 131-132) | `the umpire appointed by the two arbitrators` | the umpire | General Condition 7, lines 131-132 | see line 128 |
| "Phán quyết" | `An arbitral award`; `the date of the award` | the award | General Condition 7, line 133; General Condition 8, line 140 | none |
| "trong vòng một tháng" | `the last day to appoint an arbitrator after a written request sent on` (`bmcar-general-conditions.l4`) | within one month | General Condition 7, lines 129-130 | calendar month assumed (F15) |
| "khiếu nại gian lận" | `the claim is fraudulent` | a fraudulent claim | General Condition 8, line 136 | none |
| "khai báo sai" | `a false declaration was made or used in support of the claim` | a false declaration | General Condition 8, line 136 | "sai" is "incorrect", with no implication of intent; English "false" suggests untruth (X18, F46) |
| "phương tiện hay thủ đoạn gian lận" | `fraudulent means or devices were used by or for the Insured to obtain a benefit` | fraudulent means or devices | General Condition 8, lines 137-138 | none |
| "khiếu nại đòi bồi thường bị khước từ" | `the claim was rejected` | the claim is rejected | General Condition 8, line 138 | whether a rejection of the amount counts is F16 |
| "tiến hành tố tụng" | `the date proceedings were commenced`; `commence proceedings against Bao Minh` | commence proceedings | General Condition 8, line 139 | "tố tụng" is court proceedings; whether arbitration counts is open |
| "trong vòng ba tháng" | `the last day to commence proceedings after an award made on` (`bmcar-general-conditions.l4`) | within three months | General Condition 8, line 139 | calendar months assumed (F16) |
| "tất cả các quyền lợi theo đơn bảo hiểm này sẽ không có giá trị" | `General Condition 8 — all benefit under the Policy is forfeited` | all benefit forfeited | General Condition 8, line 141 | none |
| "Đơn bảo hiểm nào khác cũng bảo hiểm tổn thất vật chất hay trách nhiệm đó" | `another insurance covers the same loss`; `another insurance covers the same liability` | other insurance | General Condition 9, lines 143-145 | none |
| "tỷ lệ của họ" | `General Condition 9 limits Bao Minh to a rateable proportion that the policy does not define` | rateable proportion | General Condition 9, line 145 | "of them" (họ) for Bảo Minh is odd; the basis is not stated (F17) |

## Section II

| Vietnamese term (verbatim) | English identifier in the L4 | English meaning, one line | where defined or used (Điều / clause, src line) | translation risk |
| --- | --- | --- | --- | --- |
| "bên thứ ba" | `A claim under Section II` | the third party | Section II, lines 262, 264 | undefined (F29) |
| "thương tật hay ốm đau bất ngờ cho bên thứ ba (dù chết hay không)" | `bodily injury or illness, fatal or not` | bodily injury or illness | Section II, line 262 | none |
| "tổn thất bất ngờ đối với tài sản thuộc bên thứ ba" | `loss of or damage to property belonging to the third party` | third-party property damage | Section II, line 264 | none |
| "bất ngờ" | `accidental` | accidental | Section II, lines 262, 264 | "sudden" or "unexpected"; "accidental" is wider than "sudden" |
| "có liên quan trực tiếp đến việc xây dựng hay lắp đặt các hạng mục được bảo hiểm theo Phần" | `in direct connection with the construction or erection of the items insured under Section I` | in direct connection with the works | Section II, line 266 | "lắp đặt" is erection or installation (X22) |
| "tại khu vực công trường hay phụ cận với công trường" | `on or in the immediate vicinity of the site` | on or near the site | Section II, line 267 | "phụ cận" is "vicinity"; "immediate" is the encoder's |
| "trách nhiệm pháp lý bồi thường" | `the Insured is legally liable to pay damages`; `the damages the Insured is legally liable to pay` | legal liability to pay damages | Section II, line 259 | none |
| "chi phí kiện tụng mà bên nguyên đơn đòi được từ Người được bảo hiểm" | `the claimant's costs and expenses of litigation recovered from the Insured` | the claimant's costs | Section II, line 272 | none |
| "chi phí đã được thực hiện với sự đồng ý bằng văn bản của Bảo Minh" | `costs and expenses incurred with the written consent of Bao Minh` | consented costs | Section II, line 273 | none |
| "Chi phí phát sinh trong việc làm, làm lại, làm hoàn thiện hơn, sửa chữa hay thay thế" | `of which, expenditure on doing, redoing, making good, repairing or replacing anything insured or insurable under Section I` | Section I work | Section II exclusion 2, line 287 | none |
| "điều khoản sửa đổi bổ sung" | `the vibration and support exclusion has been varied by endorsement` | an endorsement | Section II exclusion 3, line 292 | none |
| "người làm thuê hay công nhân của chủ thầu hay chủ công trình" | `the injured person is an employee or worker of the contractor, the principal or a firm connected with the works, or of their family` | the contractors' and principal's people | Section II exclusion 4(a), lines 296-299 | "chủ thầu" is the contractor, "chủ công trình" the owner |
| "sự chăm nom, coi sóc hay kiểm soát" | `the property belongs to or is in the care, custody or control of the contractor, the principal, a firm connected with the works, or an employee or worker of one of them` | care, custody or control | Section II exclusion 4(b), lines 300-301 | the qualifier at line 302 is garbled (X21) |
| "bất kỳ thoả thận nào của Người được bảo hiểm về trả bất kỳ một khoản nào dưới hình thức đền bù" | `the liability arises from an agreement of the Insured to pay by way of indemnity or otherwise` | contractual liability | Section II exclusion 4(d), lines 306-307 | "thoả thận" is the source's misprint for "thoả thuận" (X21) |
| "trừ khi trách nhiệm đó thuộc trách nhiệm bồi thường của Bảo Minh cho dù không có thoả thuận đó" | `the liability would have attached in the absence of that agreement` | liability without the agreement | Section II exclusion 4(d), lines 307-308 | none |
| "toàn bộ hạn mức bồi thường với mỗi sự cố" | `the limit for the occurrence` (`bmcar-section-2.l4`) | the full limit for the occurrence | Section II Condition 2, lines 321-322 | none |
| "khoản tiền đền bù cho sự cố đó" | `the sums already paid as compensation for it` (`bmcar-section-2.l4`) | sums already paid for the occurrence | Section II Condition 2, lines 322-323 | none |
| "số tiền mà khiếu nại hay các khiếu nại phát sinh từ sự cố trên có thể được giải quyết" | `the sum for which the claims can be settled` (`bmcar-section-2.l4`) | the settlement sum | Section II Condition 2, lines 323-324 | whose estimate is not said (F33) |
| "toàn quyền" | `Section II Condition 1 — Bao Minh's option to take over the claim` | full discretion | Section II Condition 1, line 317 | none |

## Acts and outcomes

| Vietnamese term (verbatim) | English identifier in the L4 | English meaning, one line | where defined or used (Điều / clause, src line) | translation risk |
| --- | --- | --- | --- | --- |
| "thông báo" | `give notice of the occurrence that Bao Minh receives` | give notice | General Condition 5, line 89 | none |
| "giám định" | `inspect the loss` | inspect, survey | General Condition 5, lines 96, 110-111 | "giám định" is a survey or assessment, more than an inspection |
| "sửa chữa hay thay thế" | `repair or replace the damaged item` | repair or replace | General Condition 5, line 107 | none |
| "chỉ định một Trọng tài bằng văn bản" | `appoint an arbitrator in writing` | appoint an arbitrator | General Condition 7, line 129 | none |
| "tiến hành và chỉ đạo dưới danh nghĩa Người được bảo hiểm việc bảo vệ hay giải quyết một khiếu nại" | `take over and conduct the defence or settlement of the claim in the Insured's name` | take over the defence | Section II Condition 1, lines 314-316 | none |
| "sẽ không bồi thường" | `no loss claimed is within the cover` (of `A reason nothing is payable`) | no cover | General Exclusions, line 19; Section II exclusions, line 283 | none |
| "bồi thường" | `payable` (of `The outcome of a claim`) | indemnity | passim | "bồi thường" is both indemnity and compensation (damages) |
