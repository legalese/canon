# GLOSSARY — UIC voluntary motor vehicle insurance rules (row `legalese-2026-10-vn-02`)

The bilingual record of this encoding: every term the document defines, and every type, field or constant the L4 declares that renders a Vietnamese concept.
Vietnamese is quoted verbatim from `../../source/raw/uic-autojoy.txt` (the source's own spelling, typos included); `src:N` is line N of that file.
Checked by `python3 -I tools/vnsrc.py check ../../source/raw/uic-autojoy.txt GLOSSARY.md`.
Identifiers are those of the `.l4` modules; "(no DECLARE)" means the concept is carried by another name, which the row gives.
Where a name is the encoding's own and not a rendering of source words (the supplementary clauses, the result types), the row says so.

## 1. Terms the document defines

| Vietnamese term (verbatim) | English identifier in the L4 | English meaning, one line | where defined or used (Điều / clause, src line) | translation risk |
| --- | --- | --- | --- | --- |
| "Doanh Nghiệp Bảo Hiểm" | `UIC` (in `A party`) | the insurer, United Insurance Company | Part I def 1, src:36 | "doanh nghiệp bảo hiểm" is generic ("insurance enterprise"); the definition fixes it to UIC, so the L4 uses the name. |
| "Bên Mua Bảo Hiểm" | (no DECLARE; folded into `the policyholder`) | the person who concludes the contract and pays the premium | def 2, src:38-39 | English "policyholder" usually means this person; here that word is reserved for def 9, which is wider. |
| "Người Được Bảo Hiểm" | (no DECLARE; folded into `the policyholder`) | the person whose car is insured and who receives compensation | def 3, src:40-41 | Part 2 Art 1 reuses "Người được bảo hiểm" for the persons carried (src:557): the same words name a different class there. |
| "Chủ xe" | (no DECLARE) | the owner of the car, or one the owner lets possess and use it lawfully | def 4, src:42-43 | wider than English "owner": a lawful user counts. |
| "Xe ô tô" | `definition 5 — a car`; `A kind of vehicle` | car, including pickups, trucks, coaches, buses and drawn trailers; not two- or three-wheelers | def 5, src:44-46 | "car" in English suggests a passenger car; the definition includes trucks and trailers, and its list ends in "....", so it is open. |
| "Giá thị trường của xe" | `the market value of the vehicle when the contract was concluded`; `market value of the vehicle at the time of the loss` | the price a vehicle of the same type, year, make, model, mileage or age and use fetches | def 6, src:47-49; Art 12.2, 13.2.1, 13.2.3 | the document also says "giá trị thực tế" (actual value, src:421, 424), undefined; read as the market value (fork F18). |
| "Thời gian sử dụng xe" | `definition 7 — the time in use in months, under` | months from first registration in Vietnam (or January of the year made, for a used import) to the month the contract was concluded | def 7, src:50-52 | "time in use" is not "age": it stops at conclusion, not at the loss; the depreciation table speaks of "Xe dưới 3 năm" without naming it (fork F19). |
| "Phí bảo hiểm" | `the premium` | the premium payable to UIC on the agreed terms | def 8, src:53-54 | none. |
| "Chủ Hợp Đồng Bảo Hiểm" | `the policyholder` (in `A party`) | the buyer and/or the insured and/or the owner, or their legal representative | def 9, src:58-59; throughout | literally "master of the insurance contract"; "policyholder" is the nearest English, but the Vietnamese is a union of three roles, so who acted and who is paid can differ (finding V15). |
| "Bên thứ ba" | `involving a third party` (field of `A loss`) | anyone related to the damage other than UIC, the driver and the policyholder | def 10, src:60 | in English "third party" usually includes the other driver only; here the insured's own driver is expressly not one. |
| "Hợp Đồng Bảo Hiểm" | `A policy` | the agreement under which the buyer pays and UIC compensates; made of the documents of Art 1 | Art 1, src:72-85 | "contract" and "policy" are used for the same thing in English; the L4 calls the schedule's facts `A policy`. |
| "Thời hạn bảo hiểm" | `An insurance period` | the period between the start and end the contract states | Art 2.1, src:89 | "thời hạn" is both "term" and "deadline" (Art 9's "Thời hạn yêu cầu bồi thường" is a deadline). |
| "Thời hạn thanh toán phí bảo hiểm" | `due date` (of `A premium instalment`) | the time for paying the premium the contract states | Art 16.1, src:523-526 | defined as a period ("thời hạn"), read as its last day (fork F6). |
| "Hợp đồng bảo hiểm trùng" | `Art 8.1 — UIC's share, with the other sums insured`; `sums insured by other insurers for the same vehicle, conditions and events` | the policyholder's contracts with two or more insurers for the same object, conditions and events | Art 8, src:294-296 | English "double insurance" and the Law's own definition (Art 49.1, line 965-968 of the aid) require the sums to exceed the value; this one does not (finding V27). |
| "Số tiền bảo hiểm" | `the sum insured` | the sum the policyholder asks UIC to insure, written in the contract, not above the market value | Art 12.1, src:397-398 | none. |
| "Mức khấu trừ" | `A deductible`; `a deductible per loss of` | the sum stated in the contract the policyholder bears on each and every loss | Art 14.1, src:467-469 | "khấu trừ" also means set-off (Art 16.2, src:535: "khấu trừ bất kỳ khoản Phí bảo hiểm chưa thanh toán nào") and is close to "khấu hao" (depreciation); three different things in English. |
| "Mức khấu trừ theo bậc thang" | `the tiered deductible`; `Art 14.2 — the steps of the tiered deductible` | a deductible rising with the number of losses | Art 14.2, src:470-473 | "bậc thang" (staircase) is rendered "tiered". |
| "miễn thường" | (no DECLARE; the same `deductible`) | used beside "mức khấu trừ" in Art 13.4.3 | src:461 | often a franchise (nothing below, everything above) rather than a deductible; the document uses it as a synonym. |
| "Vu tổn thất" | (no DECLARE; one `A claim under Part 1` is one loss) | one sudden accident at one place, one time, one course and one cause | after Art 14.2, src:475-476 | the source misspells "Vụ"; the definition names only an accident, so fire, a calamity or a theft has no defined unit (finding V26). |
| "Người được bảo hiểm" (Part 2) | `A role on the vehicle`; `P2 Art 1 — a person insured` | the driver, the assistant and the others carried, called together the insured persons | Part 2 Art 1, src:557 | same words as def 3, different persons. |

## 2. Types, fields and constants the L4 declares

### The parties, the acts, the forum

| Vietnamese term (verbatim) | English identifier in the L4 | English meaning, one line | where defined or used (Điều / clause, src line) | translation risk |
| --- | --- | --- | --- | --- |
| "Công ty Bảo Hiểm Liên Hiệp" | `UIC` | the insurer | heading, src:4; def 1, src:36 | none. |
| "thông báo bằng văn bản cho bên kia trước thời điểm chấm dứt" | `give written notice of termination` | the notice that ends the contract early | Art 3.2, src:113-114 | none. |
| "hoàn lại" | `refund the premium` | refund premium for the time remaining | Art 3.2, src:116, 118 | none. |
| "Trả tiền bồi thường bảo hiểm" | `pay the compensation` | pay the claim | Art 4.2.3, src:141 | "bồi thường" is both "indemnify" and "compensate"; "compensation" is used throughout. |
| "giải thích bằng văn bản lý do từ chối bồi thường" | `explain the refusal in writing` | the written reasons for refusing a claim | Art 4.2.4, src:149 | none. |
| "đánh giá lại rủi ro và định phí bảo hiểm" | `reassess the risk and set the premium` | re-rate after a change in risk | Art 4.2.7, src:156 | none. |
| "văn bản trả lời" | `reply in writing to the request to reduce the premium` | UIC's written answer to a request for a lower premium | Art 5.2.4.1, src:184 | none. |
| "thông báo cho UIC trong vòng 15 ngày" | `notify UIC of the change in risk` | the policyholder's notice of a change in risk | Art 5.2.4, src:177 | none. |
| "gửi thông báo tổn thất bằng hình thức văn bản" | `send written notice of the loss` | the written notice within 05 days | Art 5.2.6.3, src:208 | none. |
| "Thời hạn yêu cầu bồi thường" | `make a claim` | the act Art 9.1 times | Art 9.1, src:305 | "yêu cầu bồi thường" is "request compensation"; "claim" is the insurance word. |
| "khiếu nại" | `complain about the settlement decision` | a complaint against UIC's settlement decision | Art 9.2, src:307 | "khiếu nại" is an administrative-style complaint, not a lawsuit ("khởi kiện"). |
| "Toà án nơi xảy ra tổn thất" | `the court where the loss occurred` | a court that may appoint an independent assessor | Art 6.2, src:231-232 | none. |
| "nơi cư trú của Chủ Hợp Đồng Bảo Hiểm" | `the court where the policyholder resides` | the other such court | Art 6.2, src:232 | none. |
| "Tòa án tại Việt Nam" | `a court in Vietnam` | the forum for a dispute negotiation does not settle | Art 9.4, src:315 | none. |

### The vehicle

| Vietnamese term (verbatim) | English identifier in the L4 | English meaning, one line | where defined or used (Điều / clause, src line) | translation risk |
| --- | --- | --- | --- | --- |
| "xe ô tô con" | `a passenger car` | a car for passengers | def 5, src:44 | "con" (small) has no English equivalent; "passenger car" is the usual rendering. |
| "xe bán tải" | `a pickup` | pickup truck | def 5, src:44 | none. |
| "xe tải" | `a truck` | goods truck | def 5, src:44 | none. |
| "xe khách" | `a coach` | passenger coach | def 5, src:44 | "xe khách" covers any passenger vehicle for hire; "coach" is narrower. |
| "xe buýt" | `a bus` | bus | def 5, src:44 | none. |
| "rơ moóc hoặc sơ mi rơ moóc được kéo bởi ô tô đầu kéo" | `a trailer or semi-trailer drawn by a tractor unit` | trailers drawn by a tractor | def 5, src:44-45 | whether the tractor unit itself is named is unclear; the L4 treats it as unnamed (fork F3). |
| "xe mô tô hai bánh" | `a two-wheeled motorcycle` | excluded kind | def 5, src:45 | none. |
| "xe mô tô ba bánh" | `a three-wheeled motorcycle` | excluded kind | def 5, src:45 | none. |
| "xe gắn máy" | `a moped` | excluded kind | def 5, src:45 | "xe gắn máy" is a low-powered motorbike; "moped" is approximate. |
| "xe đạp điện" | `an electric bicycle` | excluded kind | def 5, src:45 | none. |
| "xe máy điện" | `an electric motorbike` | excluded kind | def 5, src:45 | none. |
| "các loại xe tương tự" | `a vehicle similar to those excluded` | excluded kind | def 5, src:45-46 | open-ended. |
| (none: the "...." of def 5) | `another kind of motor vehicle` | a kind def 5 names on neither side | def 5, src:45 | the encoding's own; answered by a named refusal. |
| "bắt buộc phải có Giấy phép lái xe" | `requiring a driving licence` | the vehicle needs a licence to drive | Art 11.3, src:347; P2 3.6, src:577 | none. |
| "không kinh doanh" | `not for business` | non-business use | Art 5.2.4, src:175-176 | none. |
| "kinh doanh vận tải" | `for commercial transport` | use in the transport business | Art 5.2.4, src:176 | none. |
| "xe chở hàng" | `goods` (in `What the vehicle carries`) | a goods vehicle, measured by load | Art 11.16, src:381-382 | none. |
| "xe chở người" | `persons` | a passenger vehicle, measured by persons | Art 11.16, src:382 | none. |
| "xe vừa chở người vừa chở hàng" | `goods and persons` | a mixed vehicle, measured by load or persons | Art 11.16, src:382-383 | "hoặc" (or) between the two measures: read as either (fork F15). |
| "tháng đăng ký lần đầu tại Việt Nam" | `month of first registration in Vietnam` | start of the time in use | def 7, src:50 | none. |
| "xe nhập khẩu đã qua sử dụng ở nước ngoài" | `imported after use abroad` | a used import | def 7, src:51 | none. |
| "năm sản xuất" | `year of manufacture` | the model year | def 7, src:52 | none. |
| "tải trọng" | `permitted load on the inspection certificate`; `load carried` | the load allowed and the load carried | Art 11.16, src:380; 15.1.4, src:504 | none. |
| "số lượng người" | `permitted number of persons on the inspection certificate`; `persons carried` | persons allowed and carried | Art 11.16, src:380; 15.1.4, src:504 | none. |
| "Giấy chứng nhận kiểm định an toàn kỹ thuật và bảo vệ môi trường phương tiện giao thông cơ giới đường bộ" | `without a valid inspection certificate`; the two `permitted` fields | the technical safety and environmental inspection certificate | Art 11.2, src:343-344; 7.1.2.4, src:255-256 | "inspection certificate" abbreviates a long official name. |

### The contract

| Vietnamese term (verbatim) | English identifier in the L4 | English meaning, one line | where defined or used (Điều / clause, src line) | translation risk |
| --- | --- | --- | --- | --- |
| "Các điều khoản sửa đổi, các điều khoản bổ sung" | `the amending and supplementary clauses` | first in priority | Art 1, src:76 | none. |
| "Giấy chứng nhận bảo hiểm" | `the insurance certificate` | second | Art 1, src:77 | none. |
| "Bản Hợp Đồng Bảo Hiểm hoặc Đơn bảo hiểm hoặc Bản tóm tắt Hợp Đồng Bảo Hiểm" | `the contract, the policy or the contract summary` | third | Art 1, src:79 | "Đơn bảo hiểm" is a policy document; "policy" in English can mean the whole contract. |
| "Quy Tắc bảo hiểm này" | `these Rules` | fourth | Art 1, src:81 | "Quy tắc" is "rules" (as in a set of standard terms), not "regulations". |
| "Giấy yêu cầu bảo hiểm" | `the proposal form` | fifth | Art 1, src:83 | "request for insurance"; "proposal form" is the insurance term. |
| "Tài liệu hoặc văn bản khác" | `another document` | sixth | Art 1, src:85 | none. |
| "Thứ tự ưu tiên" | `Art 1 — the rank in priority of`; `Art 1 —` a `prevails over` b | the order of priority | Art 1, src:87 | the source writes "nên trên" for "nêu trên" (above). |
| "điều khoản bổ sung" | `A supplementary clause` (eight members, the encoding's names) | an add-on clause bought with extra premium | Art 11.2, 11.8, 11.11-11.14, 11.17; Part IV, src:541-544 | the document names none and states none's terms; every member name is the encoding's (e.g. `cover outside Vietnam`). |
| "bồi thường không áp dụng khấu hao thay mới" | `no deduction for depreciation on new parts` | the add-on waiving depreciation | Art 13.1.2.2, src:427 | none. |
| "thời điểm bắt đầu và thời điểm kết thúc" | `start date`, `end date` | the period's ends | Art 2.1, src:89 | none. |
| "giờ bắt đầu và giờ kết thúc" | `start time`, `end time` (MAYBE) | the hours, if the contract states them | Art 2, src:93 | none. |
| "0 giờ 1 phút" | `Art 2 — the default start time` | 00:01 | Art 2, src:94 | none. |
| "23 giờ 59 phút" | `Art 2 — the default end time` | 23:59 | Art 2, src:94 | whether 23:59 is the last covered minute or the instant cover ends (fork F5). |
| "Đơn phương chấm dứt Hợp Đồng Bảo Hiểm trước thời hạn" | `A unilateral termination` | ending the contract early on notice | Art 3.2, src:110 | none. |
| "Tự động chấm dứt Hợp Đồng Bảo Hiểm trước thời hạn" | `Art 3.1 — the day the contract ends by itself, under` | automatic termination for unpaid premium | Art 3.1, src:97 | none. |
| "chuyển quyền sở hữu xe" | `A transfer of ownership` | a change of owner | Art 2.2, src:90 | none. |
| "văn bản chấp thuận" | `approved by UIC in writing` | UIC's written approval of the transfer | Art 2.2, src:91-92 | none. |
| "thoả thuận cho Chủ hợp đồng bảo hiểm nợ phí" | `an agreement by UIC that the premium may be owed` | UIC's agreement to let premium be owed | Art 3.1, src:99-100 | "nợ phí" is "owe the premium"; the agreement's terms are not stated (finding V6). |
| "tháng giao kết hợp đồng bảo hiểm" | `the month the contract was concluded` | end of the time in use | def 7, src:50-51 | "giao kết" is "conclude" (enter into). |
| "phần trách nhiệm vượt mức bảo hiểm bắt buộc" | `the cover under Part 3 taken` | the voluntary liability layer above compulsory insurance | Part 3, src:620-621 | none. |
| "số người được bảo hiểm" | `number of persons insured` | persons insured under Part 2 | P2 Art 4.3, src:603 | none. |
| "số tiền bảo hiểm ghi trong Hợp đồng bảo hiểm/Giấy chứng nhận bảo hiểm" | `sum insured per person` | the Part 2 sum insured | P2 Art 4.1, src:582-583 | the text does not say "per person"; read so because a death pays "the whole sum insured" (fork F29). |

### The loss and its circumstances

| Vietnamese term (verbatim) | English identifier in the L4 | English meaning, one line | where defined or used (Điều / clause, src line) | translation risk |
| --- | --- | --- | --- | --- |
| "Đâm, va" | `a collision or impact, including with an object other than a car` | collision | Art 10.1.1, src:323 | "đâm" (strike into) and "va" (bump) are both rendered by one constructor. |
| "lật" | `overturning` | overturning | Art 10.1.1, src:323 | none. |
| "đổ" | `toppling over` | falling over on its side | Art 10.1.1, src:323 | "đổ" vs "lật" is a fine distinction (topple vs roll over). |
| "chìm" | `sinking` | sinking | Art 10.1.1, src:323 | none. |
| "rơi toàn bộ xe" | `the whole vehicle falling` | the vehicle falling (off a height) | Art 10.1.1, src:323 | none. |
| "bị các vật thể khác rơi vào" | `being struck by a falling object` | struck by things falling on it | Art 10.1.1, src:323-324 | none. |
| "Hỏa hoạn" | `a conflagration` | fire (as a disaster) | Art 10.1.2, src:325 | "hỏa hoạn" and "cháy" both translate as "fire"; kept apart as two members. |
| "cháy" | `burning` | burning | Art 10.1.2, src:325 | see above. |
| "nổ" | `an explosion` | explosion | Art 10.1.2, src:325 | none. |
| "Những tai họa bất khả kháng do thiên nhiên gây ra" | `a natural calamity beyond anyone's control` | natural calamity of force majeure | Art 10.1.3, src:327 | "bất khả kháng" is the legal term "force majeure". |
| "Mất toàn bộ xe do trộm, cướp" | `theft or robbery of the whole vehicle` | loss of the whole car by theft or robbery | Art 10.1.4, src:328 | "trộm" (stealth) vs "cướp" (force) are distinct crimes, kept as one event. |
| "Mất bộ phận của xe do bị trộm hoặc bị cướp" | `theft or robbery of a part of the vehicle` | theft of parts | Art 11.13, src:373 | none. |
| "lừa đảo hoặc lạm dụng tín nhiệm chiếm đoạt xe" | `loss of the whole vehicle by fraud or abuse of trust` | appropriation by fraud or breach of trust | Art 11.14, src:375 | criminal-law terms with no exact English equivalents. |
| "thiên tai" | `a natural disaster` | natural disaster | Art 10.1, src:321-322 | none. |
| "tai nạn bất ngờ, không lường trước được" | `an accident` + `sudden and unforeseeable` | a sudden, unforeseeable accident | Art 10.1, src:322 | whether the adjectives qualify "thiên tai" too (fork F1). |
| "lãnh thổ nước CHXHCN Việt Nam" | `in Vietnam` | the territory of Vietnam | Art 11.8, src:358 | none. |
| "Hành động cố ý gây thiệt hại" | `a deliberate act to cause the damage, by the policyholder or ...` | deliberate damage | Art 11.1, src:341-342 | "những người có quyền lợi liên quan" is wide: anyone with an interest in owning, operating or using the car. |
| "xe lưu hành tạm thời có văn bản chấp thuận của cơ quan có thẩm quyền" | `in temporary circulation approved in writing by the authorities` | temporary circulation permit | Art 7.1.2.4, src:256-257 | none. |
| "kiểm định lần đầu tiên tại Việt Nam" | `within the first registration and inspection in Vietnam` | first registration and inspection | Art 7.1.2.4, src:257-258 | none. |
| "đi vào đường cấm hoặc khu vực cấm" | `entering a prohibited road or area` | traffic offence | Art 11.5, src:352 | none. |
| "đường ngược chiều" | `driving against the direction of traffic` | wrong way | Art 11.5, src:352 | none. |
| "rẽ hoặc quay đầu tại nơi bị cấm" | `turning or making a U-turn where prohibited` | prohibited turn | Art 11.5, src:352-353 | none. |
| "vượt đèn đỏ" | `running a red light` | red light | Art 11.5, src:353 | none. |
| "không chấp hành theo hiệu lệnh của người điều khiển giao thông" | `disobeying the person directing traffic` | ignoring a traffic controller | Art 11.5, src:353 | none. |
| "đi đêm không có thiết bị chiếu sáng theo quy định" | `driving at night without the required lights` | no lights at night | Art 11.5, src:353-354 | none. |
| "Đua xe" | `racing, lawful or not` | racing | Art 11.6, src:355 | none. |
| "dùng để kéo xe khác không tuân thủ quy định của pháp luật" | `towing another vehicle in breach of the law` | unlawful towing | Art 11.6, src:355 | none. |
| "vượt quá tốc độ cho phép từ 50% trở lên" | `the speed over the limit, as a share of the limit, at`; `speed`, `speed limit` | speeding by 50% or more | Art 11.6, src:356 | "từ ... trở lên" is inclusive ("50% or more"). |
| "chở hàng trái phép theo quy định của pháp luật" | `carrying goods unlawfully` | illegal cargo | Art 11.7, src:357 | none. |
| "Chiến tranh, khủng bố" | `war`, `terrorism` | war, terrorism | Art 11.9, src:361 | none. |
| "người điều khiển xe" | `A driver`; `driver` (MAYBE) | the person driving | Art 11.3-11.4, src:346, 350 | "điều khiển" is "control/operate", the usual word for driving. |
| "không có Giấy phép lái xe" | `no licence` | no licence | Art 11.3, src:346 | none. |
| "Giấy phép lái xe không phù hợp" | `a licence not appropriate to this kind of vehicle` | wrong class | Art 11.3, src:346-347 | none. |
| "hết hạn" | `an expired licence` | expired | Art 11.3, src:347 | none. |
| "bị tước quyền sử dụng Giấy phép lái xe có thời hạn hoặc không thời hạn" | `a licence whose use has been withdrawn, for a time or indefinitely` | suspended or revoked | Art 11.3, src:348 | "tước quyền sử dụng" is "deprive of the right to use", covering suspension and revocation. |
| "nồng độ cồn trong máu hoặc khí thở" | `alcohol in blood or breath` | any alcohol concentration | Art 11.4, src:350 | "có nồng độ cồn" has no threshold: any trace (finding V2). |
| "sử dụng ma túy hoặc chất kích thích bị cấm" | `using narcotics or banned stimulants` | drugs | Art 11.4, src:350-351 | Part 2 Art 3.5 writes "và" (and) (fork F31). |
| "thiệt hại ước tính" | `estimated damage` | the estimate Art 15.1.1.2 compares with 10 million đồng | Art 15.1.1.2, src:487 | estimated by whom is not said. |
| "liên quan đến bên thứ ba" | `involving a third party` | a third party is involved | Art 15.1.1.2, src:486 | none. |

### The damaged parts

| Vietnamese term (verbatim) | English identifier in the L4 | English meaning, one line | where defined or used (Điều / clause, src line) | translation risk |
| --- | --- | --- | --- | --- |
| "bộ phận" | `A damaged part`; `an ordinary part` | a part of the vehicle | Art 13.1, src:412-413 | none. |
| "động cơ" | `the engine` | the engine | Art 11.11, src:365 | none. |
| "săm lốp" | `a tyre or inner tube` | tyres and tubes | Art 11.12, src:370 | none. |
| "bạt" | `the tarpaulin` | tarpaulin cover | Art 11.12, src:370 | none. |
| "thùng xe" | `the cargo body` | the cargo body of a truck | Art 11.12, src:370 | could be read as the vehicle's body; read as the cargo body (finding V13). |
| "nhãn mác" | `a label or badge` | labels and badges | Art 11.12, src:370-372 | none. |
| "máy móc, dụng cụ điện hay các bộ phận của thiết bị điện" | `electrical machinery, an electrical tool or a part of electrical equipment` | electrical equipment | Art 11.15, src:378 | whether "máy móc" (machinery) is qualified by "điện" (electrical) (fork F14). |
| "thiết bị lắp thêm" | `equipment added to the vehicle`; `the added equipment` | after-market equipment | Art 11.17, src:385-386 | none. |
| "thiết bị của nhà sản xuất đã lắp ráp" | `fitted by the manufacturer` | factory-fitted | Art 11.17, src:385; 11.12, src:372 | none. |
| "hao mòn tự nhiên" | `natural wear and tear` | wear and tear | Art 11.10, src:362 | none. |
| "bản chất vốn có của tài sản" | `the inherent nature of the part` | inherent vice | Art 11.10, src:362 | "inherent vice" is the English insurance term; "inherent nature" is literal. |
| "giảm giá trị thương mại" | `a fall in commercial value` | depreciation in market value | Art 11.10, src:362 | none. |
| "khuyết tật vật liệu" | `a defect in the material` | material defect | Art 11.10, src:363 | none. |
| "hỏng hóc thêm do sửa chữa, trong quá trình sửa chữa (bao gồm chạy thử)" | `further damage from repair or during repair, test runs included` | repair damage | Art 11.10, src:363 | none. |
| "chạy quá tải, quá áp lực, đoản mạch, tự đốt nóng, hồ quang điện hay rò điện" | `overload, over-pressure, short circuit, self-heating, arcing or leakage of current` | electrical causes | Art 11.15, src:378-379 | "quá áp lực" (over-pressure) is mechanical, not electrical. |
| "Khi xe hoạt động trong khu vực ngập nước" | `water, while the vehicle was operating in a flooded area` | 11.11(a) | Art 11.11, src:367 | none. |
| "nước vào khoang máy gây kích nổ phá hỏng động cơ (thủy kích)" | `water entering the engine compartment and hydro-locking the engine` | 11.11(b) | Art 11.11, src:368 | "thủy kích" (water strike) is hydrolock. |
| "cố tình khởi động lại động cơ đã ngưng hoạt động" | `water, after the driver deliberately restarted the engine that had stopped in a flooded area` | 11.11(c) | Art 11.11, src:369 | none. |
| "chi phí hợp lý để sửa chữa" | `reasonable repair cost` | the reasonable cost to repair | Art 13.1.1, src:414 | none. |
| "giá trị thay mới hạng mục" | `replacement cost` | the value of a new part | Art 13.1.1, src:417 | none. |
| "không thể khắc phục được theo đánh giá và đề xuất kỹ thuật từ bên chuyên môn" | `beyond repair on the technical assessment` | irreparable on expert assessment | Art 13.1.1, src:415-416 | none. |

### After the loss

| Vietnamese term (verbatim) | English identifier in the L4 | English meaning, one line | where defined or used (Điều / clause, src line) | translation risk |
| --- | --- | --- | --- | --- |
| "không thông báo ngay đến Tổng Đài" | `not notifying the UIC hotline immediately` | 15.1.1.1 | Art 5.2.6.1, src:200; 15.1.1.1, src:481 | "ngay" (at once) has no number of days. |
| "Không thông báo ngay cho cơ quan công an" | `not notifying the police or the local authority immediately` | 15.1.1.2 | Art 5.2.6.1, src:201-202; 15.1.1.2, src:484 | none. |
| "không thực hiện đầy đủ các biện pháp cứu chữa" | `not fully rescuing, limiting the damage and protecting the scene` | 15.1.1.3 | Art 15.1.1.3, src:489 | none. |
| "tự ý tháo gỡ hoặc sửa chữa xe bị thiệt hại khi chưa có ý kiến chấp thuận của UIC" | `dismantling or repairing the vehicle without UIC's approval` | 15.1.2.1 | Art 5.2.6.2, src:204; 15.1.2.1, src:495-496 | 5.2.6.2 also forbids moving ("di chuyển"); 15.1.2.1 sanctions only dismantling or repairing. |
| "từ chối chuyển quyền cho UIC" | `refusing to transfer, not preserving, or waiving the right to claim from the third party` | 15.1.3 | Art 15.1.3, src:500-501 | none. |
| "kê khai giấy yêu cầu bảo hiểm sai" | `declaring the vehicle's use wrongly, so that too little premium was charged` | 15.1.5.1 | Art 15.1.5.1, src:509 | none. |
| "không thông báo cho UIC trong trường hợp có sự gia tăng mức độ rủi ro bảo hiểm" | `not notifying UIC of an increase in risk` | 15.1.5.2 | Art 15.1.5.2, src:511-512 | none. |
| "không trung thực trong việc cung cấp các thông tin" | `dishonesty in the claim documents` | 11.18 | Art 11.18, src:392 | none. |
| "không tạo điều kiện thuận lợi cho UIC trong quá trình xác minh" | `not facilitating UIC's verification of the claim documents` | 11.18 | Art 11.18, src:393 | none. |
| "bất khả kháng" | `force majeure` | force majeure | Art 5.2.6.1, src:202; 5.2.6.3, src:207 | none. |
| "bất khả kháng và được UIC xác nhận" | `force majeure, confirmed by UIC` | the 15.1.1.2 excuse | Art 15.1.1.2, src:485 | the confirmation is UIC's (fork F36). |
| "di chuyển để đảm bảo an toàn" | `the vehicle was moved for safety` | 15.1.1.3 excuse | src:490 | none. |
| "phải thi hành theo yêu cầu của cơ quan chức năng" | `an authority required it` | 15.1.1.3 and 15.1.2.1 excuse | src:491, 497 | none. |
| "cần thiết để đảm bảo an toàn, đề phòng hạn chế thiệt hại về người và tài sản" | `it was necessary for safety or to prevent harm to persons or property` | 15.1.2.1 excuse | src:496-497 | none. |
| "làm gia tăng mức độ thiệt hại" | `the failures increased the damage` | 15.1.1.4 | src:492 | none. |
| "Giảm trừ đến 30%" | `the rate UIC sets under Article 15.1.1.4` | UIC's chosen rate, up to 30% | src:492 | none. |
| "tùy theo mức độ lỗi" | `the rate UIC sets under Article 15.1.3` | UIC's chosen rate | src:499 | none. |
| "số phí phải nộp theo quy định" | `the premium that should have been charged` | the premium for the true risk | Art 15.1.5, src:507 | none. |

### The assessment and the claim

| Vietnamese term (verbatim) | English identifier in the L4 | English meaning, one line | where defined or used (Điều / clause, src line) | translation risk |
| --- | --- | --- | --- | --- |
| "xe bị thiệt hại trên 75% theo đánh giá và đề xuất kỹ thuật từ bên chuyên môn" | `extent of damage on the technical assessment` | the expert's percentage | Art 13.2.1, src:435-436 | none. |
| "giá thị trường của xe được bảo hiểm tại thời điểm tổn thất" | `market value of the vehicle at the time of the loss` | value at the loss | Art 13.2.1, src:436-437 | none. |
| "Chi phí ngăn ngừa hạn chế tổn thất phát sinh thêm" | `cost of preventing further loss` | 10.2.1 | src:331 | none. |
| "Chi phí cứu hộ và vận chuyển xe bị thiệt hại tới nơi sửa chữa gần nhất" | `cost of rescue and transport to the nearest repair place` | 10.2.2 | src:333 | none. |
| "theo yêu cầu và chỉ dẫn của UIC" | `those costs incurred at UIC's request and on its instructions` | the 10.2 condition | src:330 | none. |
| "nguyên nhân được điều tra và kết luận bởi cơ quan công an có thẩm quyền" | `police concluded the theft` | 13.2.2 | src:438-439 | none. |
| "yêu cầu nhận lại chiếc xe bị tổn thất toàn bộ" | `the policyholder asks to keep the wreck` | 13.3.2 | src:450-451 | none. |
| "định giá của UIC" | `UIC's valuation of the wreck` | 13.3.2 | src:452 | none. |
| "tổng số tiền bồi thường trong toàn bộ thời hạn bảo hiểm" | `compensation already paid in the insurance period` | 12.1 aggregate | src:398-399 | none. |
| "số lần tổn thất" | `earlier losses in the insurance period` | 14.2 count | src:471 | "the losses counted" — within what period is not said (fork F23). |
| "khấu trừ bất kỳ khoản Phí bảo hiểm chưa thanh toán nào" | `UIC sets off unpaid premium` | 16.2 set-off | src:535 | see "Mức khấu trừ". |
| "sự kiện bất khả kháng hoặc trở ngại khách quan khác" | `days of force majeure or other objective obstacle` | days not counted in 9.1 | src:305-306 | none. |
| "Hồ sơ bồi thường" | `A claim document`; `Art 7 — the documents listed for` | the claim file | Art 7, src:244 | none. |
| "(nếu có)" | `only if there is one` | "if any" | Art 7, src:253, 264, 272-279, 285-290 | none. |
| "phụ thuộc vào yêu cầu của từng trường hợp cụ thể" | `The kind of case for Article 7` | depends on the case | src:244-245 | none. |
| "Thông báo tổn thất và yêu cầu bồi thường" | `notice of the loss and request for compensation` | 7.1.1 | src:247 | none. |
| "Giấy đăng ký xe, Giấy phép lái xe hợp lệ của người điều khiển xe bị tổn thất" | `the vehicle registration and the driver's valid licence` | 7.1.2.2 | src:252 | none. |
| "Biên bản ghi nhận thiệt hạ, báo giá, hóa đơn, chứng từ hợp lệ" | `the record of damage, quotes, invoices and receipts for repair or replacement` | 7.1.3.1 | src:260 | source typo "thiệt hạ" (for "thiệt hại"). |
| "Bản án hoặc Quyết định có hiệu lực của Tòa án" | `the court's judgment or decision in force` | 7.1.4 | src:264 | none. |
| "Biên bản khám nghiệm hiện trường vụ tai nạn" | `the record of the scene examination` | 7.2.1.1 | src:272 | none. |
| "Biên bản giám định thiệt hại được các bên thống nhất" | `the damage assessment record agreed by the parties` | 7.2.3 | src:281 | none. |
| "Đơn trình báo mất trộm, mất cướp với cơ quan công an có xác nhận của cơ quan công an" | `the theft or robbery report certified by the police` | 7.3.1 | src:284 | none. |

### Part 2

| Vietnamese term (verbatim) | English identifier in the L4 | English meaning, one line | where defined or used (Điều / clause, src line) | translation risk |
| --- | --- | --- | --- | --- |
| "Người điều khiển xe" | `the driver` | the driver | P2 Art 1, src:557 | none. |
| "phụ xe" | `the driver's assistant` | the driver's assistant (conductor, loader) | P2 Art 1, src:557 | "phụ xe" is a crew role with no single English word. |
| "những người khác được chở trên xe cơ giới" | `another person carried` | passengers | P2 Art 1, src:557 | "xe cơ giới" (motor vehicle) is undefined in the document (fork F27). |
| "đang ở trên xe, lên xuống xe" | `on the vehicle or getting on or off` | P2 scope | P2 Art 2, src:561 | none. |
| "trong quá trình xe đang tham gia giao thông" | `while the vehicle was in traffic` | P2 scope | P2 Art 2, src:561-562 | does it qualify both limbs (fork F28)? |
| "trừ khi có thỏa thuận khác" | `outside Vietnam under another agreement` | P2 3.1 carve-out | src:566 | none. |
| "có hành động cố ý gây thiệt hại" | `a deliberate act of the insured person to cause the harm` | P2 3.3 | src:570 | none. |
| "tham gia đánh nhau" | `the insured person taking part in a fight` | P2 3.4 | src:571 | none. |
| "hành động tự vệ" | `confirmed to be self-defence` | P2 3.4 carve-out | src:571 | who confirms is not said. |
| "tập lái" | `the vehicle used for driving practice` | P2 3.7 | src:578 | none. |
| "đua thể thao, đua xe" | `the vehicle used for sport racing or racing, lawful or not` | P2 3.7 | src:578 | none. |
| "gây tử vong hoặc thương tật thân thể cho Người được bảo hiểm" | `goods carried unlawfully or loading rules broken, causing the death or injury` | P2 3.8 (causal) | src:580 | none. |
| "bị chết" | `death` | P2 4.1 | src:582 | none. |
| "Thương tật vĩnh viễn" | `permanent injury` | P2 4.2(a) | src:585 | none. |
| "Thương tật tạm thời" | `temporary injury` | P2 4.2(b) | src:588 | none. |
| "Bảng tỷ lệ trả tiền bảo hiểm" | `percentage in the payout table` | the Ministry's payout table (Decision 05/TC-BH, 1993), not in the source | src:585-587, 591-593 | read as a percentage of the sum insured per person (fork F29). |
| "Chi phí y tế thực tế" | `actual medical costs` | medical costs | src:590 | none. |
| "chi phí bồi dưỡng" | `nutrition costs claimed` | allowance for nourishment during treatment | src:590 | "bồi dưỡng" is nourishment/convalescent care; no exact English. |
| "0,1% số tiền bảo hiểm/ngày" | the cap in `P2 Art 4.2(b) — the benefit for a temporary injury in` | 0.1% of the sum insured a day | src:590 | decimal comma: 0,1% is 0.001 (fork F33 on what it caps). |
| "180 ngày/vụ" | `P2 Art 4.2(b) — the days of treatment of` | 180 days an accident | src:595 | none. |
| "Số ngày điều trị nội trú trong bệnh viện và điều trị sau khi xuất viện" | `days in hospital and after discharge as the doctor prescribed` | count (1) | src:596-597 | none. |
| "Số ngày nghỉ không đi làm do hậu quả của tai nạn được xác định theo xác nhận của nơi công tác" | `days off work confirmed by the workplace` (MAYBE) | count (2) | src:598 | none (finding V19). |
| "số người thực tế trên xe" | `persons actually on the vehicle` | P2 4.3 | src:604 | none. |
| "số tiền bảo hiểm đã trả trước đó" | `amounts already paid for this accident` | P2 4.4 | src:606-607 | none. |
| "trong thời hạn của hợp đồng bảo hiểm" | `death within the contract term` | P2 4.4 | src:605 | none (fork F34). |
| "bệnh tật hoặc sự tàn tật có sẵn" | `made worse by an existing illness or disability, or by late or improper treatment` | P2 4.5 | src:608-609 | none. |
| "người có sức khỏe bình thường được điều trị một cách hợp lý" | `percentage for the same injury in a healthy person properly treated` | P2 4.5 | src:610-611 | none. |

### What the rules answer

| Vietnamese term (verbatim) | English identifier in the L4 | English meaning, one line | where defined or used (Điều / clause, src line) | translation risk |
| --- | --- | --- | --- | --- |
| "Loại Trừ Trách Nhiệm Bảo Hiểm" | `An exclusion in Article 11` (18 members, named by number and gist) | the exclusions | Art 11, src:338 | member names are the encoding's summaries. |
| "Không thuộc phạm vi bảo hiểm" | `An exclusion in Part 2 Article 3` (8 members) | the Part 2 exclusions | P2 Art 3, src:563 | "not within the cover" is a heading, rendered "exclusions". |
| "Từ chối bồi thường" | `A reason there is no cover`; `not covered` | refusal of a claim | Art 4.1.3, src:129 | the reasons are the encoding's list. |
| "Bồi thường tổn thất bộ phận" | `a partial loss` | partial loss | Art 13.1, src:411 | none. |
| "Bồi thường tổn thất toàn bộ" | `a total loss` | total loss | Art 13.2, src:434 | "tổn thất toàn bộ" includes constructive total loss (75%). |
| "tổn thất toàn bộ do xe bị mất trộm, mất cướp" | `a total loss by theft` | theft as total loss | Art 13.2.2, src:438 | none. |
| "chi phí cần thiết và hợp lý để sửa chữa xe" | `cost of repair and replacement` | 13.4.1 | src:457 | none. |
| "khấu hao thay mới bộ phận" | `depreciation`; `Art 13.1.2.2 — the depreciation table` | 13.4.2 first | src:459; 429-433 | "khấu hao" (depreciation) vs "khấu trừ" (deductible). |
| "giảm trừ do bảo hiểm dưới giá trị" | `insured proportion` | 13.4.2 second | src:459-460 | none. |
| "giảm trừ do chế tài" | `sanction rate` | 13.4.2 third; Article 15 | src:460 | "chế tài" is "sanction (penalty)"; Article 15 calls the same thing "Giảm trừ bồi thường". |
| "Trừ mức khấu trừ" | `deductible` | 13.4.3 | src:461 | see "miễn thường". |
| "Trừ bán thanh lý tài sản" | `wreck deduction` | 13.4.4 | src:462 | literally "less the sale of salvage"; applied only where the policyholder keeps the wreck (fork F22). |
| "Áp dụng bảo hiểm trùng" | `UIC's share under Article 8` | 13.4.5 | src:463 | none. |
| "mức khấu trừ bắt buộc và tối thiểu 500.000 (năm trăm nghìn) Đồng/vụ tổn thất" | `Art 14 — the compulsory minimum deductible` | 500.000 đồng a loss | src:469, 473 | "500.000" is five hundred thousand (the dot groups thousands). |
| "khấu hao" (the five rows) | `Art 13.1.2.2 — the depreciation table`; `A row of the depreciation table` | 0%, 15%, 25%, 35%, 50% by years in use | src:429-433 | "Xe dưới 3 năm" (vehicles under 3 years): age measured as definition 7's time in use (fork F19). |
