# Glossary — Decree 67/2023/NĐ-CP, compulsory motor insurance (row VN-10)

Vietnamese in the first column is copied from the gazette text and checked by `tools/vnsrc.py` to occur verbatim in one of the three raw sources.
"src line N" means line N of `../../source/raw/nd67-congbao-1017-1018.txt` unless the line says `1019-1020` (`../../source/raw/nd67-congbao-1019-1020.txt`) or `220` (`../../source/raw/nd220-2026-congbao-367.txt`).
The three sources this glossary draws on, one line from each:

> -- src:84 | 5. Người thứ ba
>
> -- src:nd67-congbao-1019-1020:591 | Phụ lục VI
>
> -- src:nd220-2026-congbao-367:173 | 1. Thay thế cụm từ “người thứ ba” bằng cụm từ “bên thứ ba” tại khoản 5
>
> -- src:nd220-2026-congbao-367:174 | Điều 3, Điều 5, điểm a khoản 1 Điều 7, điểm đ khoản 2 Điều 10, khoản 2 và

Identifiers are those of the `.l4` modules; "—" in the second column means the term is quoted but no identifier renders it.

## The terms Article 3 defines

| Vietnamese term (verbatim) | English identifier in the L4 | English meaning, one line | where defined or used (Điều / clause, src line) | translation risk |
| --- | --- | --- | --- | --- |
| Chủ xe cơ giới | `Article 3(1) — a vehicle owner`; field `the owner of the vehicle` | the owner of a motor vehicle, or a person the owner has entrusted with its lawful possession and use | Điều 3(1), src lines 76-77 | high: English "owner" means title; the Vietnamese term also covers a lawful possessor and user, so a lessee or an employee driver given the car can be the "chủ xe" |
| Xe cơ giới hoạt động | `Article 3(2) — the vehicle was operating` | a vehicle that is moving, stopped or parked under the control of its owner or a driver | Điều 3(2), src lines 78-79 | medium: "hoạt động" is "operating" or "active"; English "operating" can suggest the engine running, which the definition does not require (fork F4 on what "có sự điều khiển" governs) |
| Xe cơ giới tham gia giao thông | `Article 3(3) — the vehicle was participating in traffic` | the owner or a driver driving the vehicle in road traffic | Điều 3(3), src lines 80-81 | low |
| Nhà thầu tư vấn | — | a consultant contractor (construction) | Điều 3(4), src line 82 | not used by this row |
| Người thứ ba | `Article 3(5)(a) — a third party`; `the term for the third party in` | a person whose health, life or property the vehicle damaged, other than the driver, the persons on the vehicle, its passengers, and the owner who has not handed the vehicle to another | Điều 3(5)(a), src lines 84-89; Điều 5, 7(1)(a), 10(2)(đ), 12(2), 12(6)(a), 13(5) | high: "third party" in English insurance usage is anyone not a party to the contract and often includes passengers; here passengers and every person on the vehicle are carved out. "người" is literally "person" |
| bên thứ ba | same identifiers, second vintage | the same, as Decree 220/2026 Article 9(1) renames it | Decree 220 Điều 9(1), 220 src lines 172-178 | medium: "bên" is "party" or "side" and reads more naturally of an organisation than "người" does; the definition's words are otherwise unchanged (fork F2) |
| Mức khấu trừ bảo hiểm | — | the deductible: the amount the buyer bears in each insured event | Điều 3(6), src lines 95-96 | not used by the motor chapter, which has no deductible |
| Đưa vào sử dụng | — | putting a construction work into use | Điều 3(7), src line 97 | not used by this row |
| Bệnh nghề nghiệp; Người lao động; Tai nạn lao động | — | occupational disease; employee; work accident (defined by reference to other laws) | Điều 3(8)-(10), src lines 99-101 | not used by this row |

## Terms of the motor chapter

| Vietnamese term (verbatim) | English identifier in the L4 | English meaning, one line | where defined or used (Điều / clause, src line) | translation risk |
| --- | --- | --- | --- | --- |
| bảo hiểm bắt buộc trách nhiệm dân sự của chủ xe cơ giới | module headings; `A contract of compulsory motor insurance` | compulsory insurance of the motor vehicle owner's civil liability | title, Điều 1, 4, Chương II; src lines 19-20, 175-177 | low |
| bên mua bảo hiểm | `the insurance buyer or the insured` | the insurance buyer: the persons Điều 2(1)-(3) name | Điều 4(1), src line 104 | medium: "buyer" not "policyholder"; the L4 merges the buyer with the insured (next row) |
| người được bảo hiểm | `the insurance buyer or the insured` | the insured | Điều 12, src lines 295, 341-345 | medium: merged with the buyer in one party, since every duty of Article 12 binds both together; Article 12(5) pays the insured |
| doanh nghiệp bảo hiểm | `the insurer` | the insurer (a non-life insurer or a foreign non-life insurer's branch) | Điều 2(4), src lines 65-66 | low |
| người bị thiệt hại | `the injured person`; `A person harmed in the accident` | the person who suffered the damage | Điều 7(2)(a), 12(5)-(6); src lines 209-210, 343-346 | low |
| Đối tượng bảo hiểm | `Article 5 — the owner's insured liability is owed to` | the object of the insurance: the owner's civil liability to third parties and passengers | Điều 5, src lines 183-186 | medium: "đối tượng" is the subject-matter, not the persons insured |
| Giới hạn trách nhiệm bảo hiểm | `Article 6(1) — the limit for health and life, per person per accident`; `Article 6(2) — the limit for property, per accident, for a vehicle of class` | the limit of liability | Điều 6, src lines 187-196 | low |
| một vụ tai nạn | (the per-accident limit) | one accident | Điều 6, src lines 189, 193, 196 | low |
| Phạm vi bảo hiểm | `Article 7(1) — the harm to the person's health and life is within the scope` | the scope of the cover | Điều 7(1), src lines 198-203 | low |
| Thiệt hại ngoài hợp đồng | (not a separate fact; fork F36) | non-contractual damage | Điều 7(1)(a), src line 200 | medium: the encoding treats every third party's damage as non-contractual |
| hành khách | field `a passenger on the vehicle` | a passenger | Điều 3(5)(a), 7(1)(b); src lines 87, 202 | high: undefined in the sources; whether a person riding free (a pillion rider) is a "hành khách" decides cover (finding R1, fork F25) |
| người trên xe | field `on the vehicle` | a person on the vehicle | Điều 3(5)(a), src line 87 | medium: wider than "passenger" |
| Người lái xe | field `driving the vehicle`; accident fields `the driver ...` | the driver | Điều 3(5)(a), 7(2)(b)-(c) | low |
| loại trừ trách nhiệm bảo hiểm | `The answer on cover` (`excluded: ...`) | the exclusions | Điều 7(2), src lines 204-231 | low |
| Hành động cố ý gây thiệt hại | `excluded: an intentional act of the owner or the driver`; `... of the injured person` | an intentional act causing the damage | Điều 7(2)(a), src line 209 | low |
| cố ý bỏ chạy | `the driver who caused it deliberately fled` | deliberately fled the scene | Điều 7(2)(b), src line 211 | low |
| Giấy phép lái xe | accident fields on the licence; `a driving licence is required to drive it` | the driving licence | Điều 7(2)(c), 13(2)(b); src lines 215-222, 416 | medium: which vehicles need one is the Road Traffic Law's question (fork F5) |
| hậu quả gián tiếp | `an indirect consequence: loss of commercial value, or loss tied to the use and exploitation of the damaged property` | indirect (consequential) loss | Điều 7(2)(d), src lines 223-224 | low |
| nồng độ cồn vượt quá mức trị số bình thường theo hướng dẫn của Bộ Y tế | `the driver's blood or breath alcohol exceeded the normal level in the Ministry of Health guidance` | alcohol above the normal level in the Ministry of Health's guidance | Điều 7(2)(đ), src line 226 | medium: the level is set outside the sources (an input) |
| ma túy và chất kích thích bị cấm | `the driver had used drugs or banned stimulants` | drugs and banned stimulants | Điều 7(2)(đ), src line 227 | low |
| tài sản đặc biệt | `special property: gold, silver, precious stones, valuable papers such as money, antiques, rare paintings, a body or remains` | special property | Điều 7(2)(g), src lines 229-230 | medium: "thi hài, hài cốt" (a body, remains) are listed as property |
| chiến tranh, khủng bố, động đất | `caused by war, terrorism or an earthquake` | war, terrorism, earthquake | Điều 7(2)(h), src line 231 | low |
| Mức phí bảo hiểm | `Annex I section A — the premium for a 1-year term, VAT not included, for` | the premium | Điều 8, Phụ lục I; src lines 232-238, 2041-2139 | low |
| chưa bao gồm thuế giá trị gia tăng | (comment; no VAT is added) | value added tax not included | Phụ lục I, src lines 2048-2049 | low |
| lịch sử bồi thường bảo hiểm; lịch sử gây tai nạn | `Article 8(2) — the premium after an adjustment of` | claims history; accident history | Điều 8(2), src lines 235-236 | low |
| Mô tô 2 bánh | `a two-wheeled motorcycle` | two-wheeled motorcycle | Phụ lục I A.I, src line 2051 | high: the Road Traffic Law (outside the sources) calls a two-wheeler under 50 cc a moped ("xe gắn máy"), so row I.1 and row III.2 may overlap (fork F3) |
| Mô tô 3 bánh | `a three-wheeled motorcycle` | three-wheeled motorcycle | Phụ lục I A.II, src line 2054 | low |
| Xe gắn máy | `an electric moped`; `another moped or similar motor vehicle` | moped | Phụ lục I A.III, src lines 2055-2059; Điều 6(2)(a) | medium: see Mô tô 2 bánh |
| Xe máy điện | `an electric moped` | electric moped | Phụ lục I A.III.1, src line 2058 | low |
| Xe ô tô không kinh doanh vận tải | `a car not used for transport business` | a car not used for transport business | Phụ lục I A.IV, src line 2060 | low |
| Xe ô tô kinh doanh vận tải | `a car used for transport business` | a car used for transport business | Phụ lục I A.V, src line 2066 | low |
| theo đăng ký | `number of registered seats` | as registered | Phụ lục I A.V, src lines 2067-2090 | low |
| Xe vừa chở người vừa chở hàng | `a pickup or minivan ...` | a vehicle carrying both people and goods (pickup, minivan) | Phụ lục I A.IV.5, A.V.23 | low |
| Xe ô tô chở hàng (xe tải) | `a goods vehicle (truck)` | goods vehicle | Phụ lục I A.VI, src line 2095 | low |
| trọng tải thiết kế | `designed payload in tonnes` | designed payload | Phụ lục I A.VII.3(c), src lines 2114-2117 | low |
| Xe tập lái | `a driving-school vehicle` | driving-school vehicle | Phụ lục I A.VII.1, src line 2101 | low |
| Xe Taxi | `a taxi` | taxi | Phụ lục I A.VII.2, src line 2104 | low |
| xe cứu thương | `an ambulance` | ambulance | Phụ lục I A.VII.3(a), src line 2110 | low |
| xe chở tiền | `a cash-in-transit vehicle` | cash-in-transit vehicle | Phụ lục I A.VII.3(b), src line 2112 | low |
| Xe ô tô chuyên dùng | `another special-purpose car` | special-purpose car | Phụ lục I A.VII.3, src line 2109 | low |
| Đầu kéo rơ-moóc | `a tractor unit with its trailer` | tractor unit (and trailer) | Phụ lục I A.VII.4, src line 2118 | low |
| Máy kéo | `a tractor with its trailer` | tractor | Phụ lục I A.VII.5, Điều 6(2)(b) | medium: an agricultural or road tractor, not a tractor unit |
| Xe buýt | `a bus` | bus | Phụ lục I A.VII.6, src line 2125 | low |
| Thời hạn bảo hiểm | `Article 9 — the term is permitted for`; `insurance begins on`, `insurance ends on` | the term of the insurance | Điều 9, src lines 241-256 | low |
| niên hạn sử dụng | `beyond its service life under the law`; `remaining service life under the law of less than 1 year` | the lawful service life of a vehicle | Điều 4(5)(a), 9(1)(b); src lines 128, 247 | medium: fork F32 reads 9(1)(b) as the REMAINING life |
| đăng ký tạm thời | `subject to temporary registration` | temporary registration | Điều 9(1)(c), src line 248 | low |
| Giấy chứng nhận bảo hiểm | `A certificate of insurance` | the certificate of insurance | Điều 10, src lines 260-284 | low |
| Giấy chứng nhận đăng ký xe, biển số xe | `Article 11 — the refund on the revocation of the registration on` | the vehicle registration certificate and number plates | Điều 11, src lines 287-289 | low |
| hoàn phí bảo hiểm | (refund) | refund of premium | Điều 11, 12(9); src lines 289-291, 391-392 | low |
| tạm ứng bồi thường | `Article 12(3) — the advance for`; `The advance under Article 12(3)` | an advance on compensation | Điều 12(3), src lines 317-334 | low |
| ước tính | `The harm, as estimated for the advance`; `the estimated compensation for the person` | estimated | Điều 12(3), src lines 321-330 | low |
| tỷ lệ tổn thương | `estimated injury rate`; `assessed rate`; `Annex VI rate` | the injury rate (body impairment percentage) | Điều 12(3), Phụ lục VI; src line 328, 1019-1020 src line 602 | low |
| tổn thương bộ phận | `a partial injury` | a partial injury (Part B of Annex VI) | Điều 12(3)(a), src line 324; 1019-1020 src line 601 | medium: fork F16 on whether a vegetative state is one |
| tử vong | `death`; field `died` | death | Điều 12(3), src lines 322, 328 | low |
| sống kiểu thực vật | `a brain injury leaving a persistent vegetative state` | a persistent vegetative state | Phụ lục VI A.2 and B.I 4.1; 1019-1020 src lines 600, 650 | low |
| ngày làm việc | `A working-day calendar`; `a working day under` | working day | Điều 12(3)-(4), src lines 317, 335 | high: undefined in the sources (fork F14) |
| bất khả kháng hoặc trở ngại khách quan | `force majeure or an objective obstacle` | force majeure or an objective obstacle | Điều 12(4), src lines 335-336 | low |
| mức độ lỗi | `the owner's share of the fault` | the degree of fault | Điều 12(6)(a)-(b), src lines 363, 377 | medium: the decree says "degree"; the L4 takes a fraction, which is the encoder's (fork F17) |
| lỗi hoàn toàn của người thứ ba | `an authority found it caused entirely by the fault of a third party` | caused entirely by the fault of a third party | Điều 12(6)(a), src lines 365-366 | high: whose fault halves whose compensation (finding R4) |
| giảm trừ | `Article 12(7) — the compensation for property after a reduction of` | deduction, reduction | Điều 12(7), src line 379 | low |
| hợp đồng bảo hiểm tự nguyện | (Article 12(8) exception; not encoded) | voluntary insurance | Điều 12(8), src line 388 | low |
| hợp đồng bảo hiểm giao kết đầu tiên | `Article 12(9) — what becomes of` | the contract concluded first | Điều 12(9), src lines 389-391 | low |
| Hồ sơ bồi thường bảo hiểm | `A claim file`; `Article 13 — the documents ...` | the claim file | Điều 13, src lines 401-450 | low |
| Văn bản yêu cầu bồi thường | `(1) the written request for compensation` | the written claim | Điều 13(1), src line 404 | low |
| Giấy chứng nhận đăng ký xe | `(2)(a) the vehicle registration certificate, or a document Article 13(2)(a) accepts instead` | the vehicle registration certificate | Điều 13(2)(a), src lines 410-415 | low |
| Giấy chứng minh nhân dân hoặc thẻ Căn cước công dân hoặc Hộ chiếu | `(2)(c) the driver's identity card, citizen identity card, passport or other identity paper` | identity card, citizen identity card or passport | Điều 13(2)(c), src lines 417-418 | low |
| Giấy chứng nhận thương tích | `(3)(a) the injury certificate` | the injury certificate | Điều 13(3)(a), src line 424 | low |
| Hồ sơ bệnh án | `(3)(b) the medical record` | the medical record | Điều 13(3)(b), src line 425 | low |
| Trích lục khai tử hoặc Giấy báo tử | `(3)(c) the death extract, death notice, police confirmation or forensic result` | the death certificate extract or death notice | Điều 13(3)(c), src line 426 | low |
| Hóa đơn, chứng từ hợp lệ | `(4)(a) invoices, vouchers or evidence of the repair or replacement` | valid invoices and vouchers | Điều 13(4)(a), src line 430 | low |
| Thông báo kết quả điều tra, xác minh, giải quyết vụ tai nạn | `(5) the police documents on the accident` | the police's notice of the result of the investigation of the accident | Điều 13(5), src lines 440-441 | low |
| Biên bản giám định | `(6) the insurer's assessment record` | the assessment (survey) record | Điều 13(6), src line 444 | low |
| Quyết định của Tòa án | `(7) the court decision`; `amount fixed by a court decision for health and life` | a court decision | Điều 12(6)(a), 13(7); src lines 359, 446 | low |
| Mã số, mã vạch | `(i) a registered code and barcode identifying the insurer and the product` | the registered code and barcode | Điều 10(2)(i), src line 278 | low |
| giám định tổn thất | `organise the loss assessment` | loss assessment (adjustment) | Điều 12(2), src lines 314-315 | low |
| đường dây nóng | `notify the insurer's hotline at once` | hotline | Điều 12(1)(a), src line 296 | low |
| Thời hạn thanh toán phí bảo hiểm | `Article 4(7) — the premium payment deadline is within the term` | the deadline for paying the premium | Điều 4(7), src line 151 | low |
| gian lận bảo hiểm | `Article 4(8) — the compensation without what fraud added` | insurance fraud | Điều 4(8), src line 161 | low |
| Quỹ bảo hiểm xe cơ giới | `Article 12(3) — the insurer may ask the Fund to repay the advance` | the Motor Vehicle Insurance Fund | Điều 12(3), 14-22; src lines 332, 457 | low (not encoded beyond the right to ask) |
| Luật Giao thông đường bộ | (inputs that defer to it) | the Road Traffic Law (of 13 November 2008, by the preamble) | preamble src line 29; Điều 6(2), 7(2)(c) | high: whether it is still in force is outside the sources (fork F3) |

## Terms of Annex VI and its structure

| Vietnamese term (verbatim) | English identifier in the L4 | English meaning, one line | where defined or used (Điều / clause, src line) | translation risk |
| --- | --- | --- | --- | --- |
| Phụ lục | "Annex" in every identifier | annex | throughout | low ("appendix" is also used in English translations) |
| Điều; khoản; điểm | "Article", clause "(1)", point "(a)" | article; clause; point | throughout | low |
| Bảng quy định trả tiền bồi thường thiệt hại về sức khỏe, tính mạng | `the payment band in Annex VI for`; `the Annex VI amount for` | the table of payments for damage to health and life | Điều 12(6)(a), src lines 352-353; 1019-1020 src lines 591-593 | low |
| CÁC TRƯỜNG HỢP ĐƯỢC GIẢI QUYẾT BỒI THƯỜNG 100% | part "A" | the cases paid at 100% of the limit | 1019-1020 src lines 597-598 | low |
| Số tiền bồi thường = Tỷ lệ tổn thương x Giới hạn trách nhiệm bảo hiểm | `Annex VI — the payment for an injury rate of` | payment = injury rate × limit | 1019-1020 src line 602 | low |
| Ghi chú | (quoted as NOTE in `nd67-annex6-table.l4`) | note | 17 notes in Annex VI | low |
| cộng lùi | `an addition the row describes applies`; refusal `the addition this row of Annex VI directs ...` | "regressive addition", a way of combining rates; undefined in the sources | Annex VI, many rows (finding R7) | high: undefined; a translation as "added" would suggest plain addition, which special case 4 uses and "cộng lùi" evidently does not |
| Thị lực | `A visual acuity class`; `the acuity table rate for` | visual acuity | Annex VI section VIII table, 1019-1020 src lines 1990-2010 | low |
| sáng - tối (ST) âm tính | `no light perception` | no light perception (light-dark perception negative) | 1019-1020 src lines 1996, 2010 | medium: "ST (-)" is literally "light-dark negative" |
| Những trường hợp đặc biệt | the special cases, `special case 1` ... `special case 5` in `An injury` | the special cases | 1019-1020 src lines 2177-2195 | low |
| Hội đồng giám định y khoa | `rate fixed by comparison or by the Medical Assessment Council` | the Medical Assessment Council | special case 5, 1019-1020 src line 2191 | low |
| dính các khớp ngón tay | `stiffness of the joints of a digit, special case 1` | ankylosis (fusion) of the finger joints | special case 1, 1019-1020 src line 2178 | high: "dính khớp" (ankylosis) and the table's "cứng khớp" (stiffness) may be different conditions; the L4 field says "stiffness" (finding R14) |
| Liệt chi trên; liệt chi dưới | `an upper limb`; `a lower limb` | paralysis of an upper or a lower limb | note to B.I 4.2.9-4.2.16, 1019-1020 src lines 670-671 | low |
| Nữ; Nam | `female`; `male` | woman; man | note to B.I 6.3.7-6.3.8, 1019-1020 src line 763 | low |
