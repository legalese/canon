# GLOSSARY — Vietnamese terms and their English identifiers (row `legalese-2026-10-vn-17`)

One row for every term Article 1 defines, and for every type, field and constant the modules declare that renders a Vietnamese concept. The Vietnamese is copied from the OCR text (`../../source/raw/tasco-voluntary-motor.txt`); "src" is its line. Where the OCR misspells a term, the row quotes another occurrence that is spelled right, or says so. Fields and constants that are the encoder's own bookkeeping (a date a file records, a flag for "the owner keeps the car") are listed with the Vietnamese clause they serve.

## Defined terms (Article 1)

| Vietnamese term (verbatim) | English identifier in the L4 | English meaning, one line | where defined or used (Điều / clause, src line) | translation risk |
| --- | --- | --- | --- | --- |
| Bảo hiểm Tasco | `Tasco Insurance` | the insurer, Tasco Insurance Co. Ltd. | Art. 1.1, src 84 | none |
| Bên mua bảo hiểm | `the policyholder` | the party who concludes the contract and pays the premium | Art. 1.2, src 87 | literally "the insurance buyer". English "policyholder" can suggest the insured; here buyer and insured (1.3) may be different persons |
| Người được bảo hiểm | `the insured person` | whoever has the property, liability, health or life insured | Art. 1.3, src 90; Art. 17, src 999 | covers organisations ("tổ chức") as well as people, which English "person" hides; Art. 17 reuses the term for the driver and passengers only |
| Người thụ hưởng | `the beneficiary` | the person named to receive the benefit, or the heirs | Art. 1.4, src 94 | none |
| Chủ xe | `the vehicle owner` | owner, or one given possession or use, or a buyer not yet registered | Art. 1.5, src 97 | wider than English "owner": it includes possessors, users and unregistered buyers |
| Lái xe | `the driver` | the person driving the insured vehicle at the loss | Art. 1.6, src 101 (OCR "Láixe") | the same two words also mean "to drive" |
| Xe ô tô | `a car` (`A kind of motor vehicle`) | a road motor vehicle with four wheels or more, incl. trailers and special functions | Art. 1.7, src 103 (OCR "Xeô tô") | English "car" is narrower: the term takes in trucks, tractor units and trailers |
| Xe chở người | `a passenger car` | buses, coaches and cars carrying persons | Art. 1.7.1, src 107 | "car" again narrower than the term |
| Xe chở hàng | `a goods vehicle` | trucks, trailers, semi-trailers, tractor units | Art. 1.7.2, src 110 | none |
| Xe vừa chở người vừa chở hàng | `a vehicle carrying both passengers and goods` | pickups and panel vans | Art. 1.7.3, src 113 | none |
| Xe ô tô chuyên dùng | `a special-purpose car` | a car built for one function (crane, mixer, ambulance) | Art. 1.7.4, src 117 | none |
| Xe ô tô điện | `electric, from the traction battery alone` | a car driven only by electric motors from its traction battery | Art. 1.7.5, src 123 | none |
| Xe ô tô lai sạc điện | `a plug-in hybrid` | a car using a combustion engine and an electric motor together | Art. 1.7.6, src 127 | "lai sạc điện" reads as plug-in hybrid, but the definition covers any combustion-electric hybrid; "plug-in" narrows it |
| Xe điện | `a low-speed electric vehicle` | an electric vehicle of at most 15 seats and 30 km/h, for restricted areas | Art. 1.7.7, src 130 | literally "electric vehicle", which in English would include electric cars (1.7.5) |
| Bộ pin điện động cơ | `the traction battery` | the battery that powers the motor | Art. 1.7.8, src 137 | none |
| Xe máy chuyên dùng | `a special-purpose machine` | construction, farm and defence machines that use roads | Art. 1.7.9, src 140 | "xe máy" alone means a motorcycle; here it is a machine |
| Thiết bị chuyên dùng | `special equipment` | equipment mounted on the vehicle for a special function | Art. 1.8, src 144; 10.6, 13.11, BS13 | none |
| Xe đang hoạt động | `vehicle in operation` | engine or motor running or the driver in control, moving or stopped | Art. 1.9, src 147; 10.5, 10.7 | "hoạt động" also means "active"; the definition includes a parked car with its engine running |
| Xe tham gia giao thông | `vehicle in traffic` | the driver driving the vehicle on the road | Art. 1.10, src 151; Art. 18 | none |
| Thời gian sử dụng xe | `Article 1.11 — the months of use of the vehicle insured by` | months from first registration (or January of the year made) to the contract | Art. 1.11, src 154 | "sử dụng" is use; it is counted from registration, not from actual use |
| Giấy yêu cầu bảo hiểm | `application signed` | the application the buyer declares and confirms | Art. 1.12, src 159 | none |
| Hợp đồng bảo hiểm | `A policy` | the insurance contract | Art. 1.13, src 165 | none |
| Giấy chứng nhận bảo hiểm | `A policy` | the certificate evidencing the contract (GCNBH) | Art. 1.14, src 171 | the encoding uses one record for contract and certificate |
| Số tiền bảo hiểm | `sum insured` (each section) | the amount the buyer asks to insure, written on the policy | Art. 1.15, src 176 | one Vietnamese term covers both a sum insured and a limit of liability ("mức trách nhiệm bảo hiểm") |
| Phí bảo hiểm | `premium before tax`, `premium paid in full and on time` | the premium | Art. 1.16, src 179 (OCR "lố.") | none |
| Mức khấu trừ | `deductible stated on the policy`, `An additional deductible` | the amount, before VAT, the insured bears in each loss | Art. 1.17, src 183, 185 | none |
| Bảo lưu quyền khiếu nại | `right of recourse not preserved or transferred, or a settlement made with the third party` | not settling with the third party without Tasco's consent | Art. 1.18, src 200; 14.1.3(a) | literally "reserving the right to complain"; it is a duty not to settle, not a right |
| Chuyển quyền/ Thế quyền | same field | authorising Tasco to recover from the wrongdoer | Art. 1.19, src 204 | "thế quyền" is subrogation; "chuyển quyền" transfer of rights |

## Types, fields and constants

| Vietnamese term (verbatim) | English identifier in the L4 | English meaning, one line | where defined or used (Điều / clause, src line) | translation risk |
| --- | --- | --- | --- | --- |
| Hiệu lực bảo hiểm | `Article 2.1 — Tasco is liable under` | when the insurance is in force | Art. 2, src 208 | none |
| đóng phí bảo hiểm đầy đủ và đúng hạn | `premium paid in full and on time` | premium paid in full and on time | Art. 2.1, src 212 | none |
| chuyển quyền sở hữu xe | `the ownership has been transferred` | transfer of ownership of the vehicle | Art. 2.2, src 215 | none |
| đơn phương chấm dứt | `Article 3.2.1 — a party may end the contract unilaterally` | unilateral termination | Art. 3.2, src 230 | the Law uses the same words for termination on stated grounds only (F-08) |
| phí bảo hiểm trước thuế | `premium before tax` | premium net of tax, the base of refunds | Art. 3.2.2, src 269 | none |
| Giám định tổn thất | `Who bears the independent assessor's fee` | loss assessment | Art. 6, src 423 | "giám định" is assessment or survey, not "expert opinion" |
| giám định độc lập | `the independent conclusion is the same as Tasco's assessment` | an independent assessor | Art. 6.2-6.3, src 445-452 | none |
| Hồ sơ bồi thường | `A claim document`, `The kind of claim`, `A claim file` | the claim file | Art. 7, src 460 | none |
| đầy đủ, hợp lệ | `date the complete and valid file was received` | complete and valid (of a file) | Art. 4.2.4, src 302 | who decides is not said (X-02) |
| Bảo hiểm trùng | `Article 8 — the contracts are double insurance` | double insurance | Art. 8, src 580 (OCR "Điền8.") | none |
| Thời hạn yêu cầu bồi thường | `Article 9.1 — the last day to claim for the loss in` | time limit to claim | Art. 9.1, src 598 | none |
| Thời hạn khiếu nại | `Article 9.2 — the last day to complain about the settlement, for` | time limit to complain | Art. 9.2, src 603 | "khiếu nại" is an internal complaint, not a lawsuit |
| Thời hiệu khởi kiện | `Article 9.3 — the last day to sue on the contract, for` | limitation period for suing | Art. 9.3, src 607 | "thời hiệu" (limitation) is a legal term distinct from "thời hạn" (time limit) |
| bất khả kháng | `force majeure prevented the written notice`, `force majeure or objective obstacle, in days` | force majeure | Art. 5.2.7(c), 9.1, 14.1.1(b) | none |
| trở ngại khách quan | `objective obstacle prevented the written notice` | objective obstacle | Art. 5.2.7(c), src 403; 9.1, src 600 | a civil-law term with no exact English equivalent |
| Các điểm loại trừ chung | `A general exclusion` | the general exclusions | Art. 10, src 617 | none |
| lãnh thổ nước Cộng hoà xã hội chủ nghĩa Việt Nam | `in Vietnam`, `10.1 outside Vietnam` | Vietnamese territory | Art. 10.1, src 621 | none |
| chiến tranh, khủng bố | `war or terrorism` | war, terrorism | Art. 10.2, src 623 | none |
| Hành vi ác ý, cố tình phá hoại | `deliberate destruction by the policyholder, owner, driver or another interested person`, `a malicious act by someone else` | malicious, deliberate destruction | Art. 10.3, src 625; 11.1.5, src 693 | "ác ý" is malice; the same words serve as an exclusion (insured parties) and a cover (others) |
| giấy chứng nhận kiểm định an toàn kỹ thuật và bảo vệ môi trường | `valid inspection certificate` | the technical safety and environmental inspection certificate | Art. 10.4, src 628 | none |
| thông số lốp và/hoặc đường kính la-zăng | `tyres or rims changed within the manufacturer's specification` | tyre size or rim diameter | Art. 10.4.1, src 632 | none |
| giấy phép lái xe | `A driving licence` | driving licence | Art. 10.5, src 642 | none |
| bị tước quyền sử dụng giấy phép lái xe | `a licence suspended or revoked` | licence withdrawn for a time | Art. 10.5, src 646 | none |
| nồng độ cồn | `blood alcohol, mg per 100 ml`, `breath alcohol, mg per litre` | alcohol concentration | Art. 10.7, src 654 | none |
| ma túy, chất kích thích | `drugs or prohibited stimulants used` | drugs and banned stimulants | Art. 10.7, src 655 | none |
| đường cấm | `A traffic offence` | prohibited roads and the other offences of 10.8 | Art. 10.8, src 658 | none |
| Đuaxe (the OCR joins the two words) | `racing` (`A prohibited use`) | racing, lawful or not | Art. 10.9, src 665 | none |
| quá tải trọng | `load carried in tonnes`, `permitted load in tonnes` | overloaded | Art. 10.10, src 674 | none |
| trẻ em dưới 07 tuổi | `persons carried, not counting children under 7`, `under 7` | children under 7 | Art. 10.10, src 674; 20.3, src 1041 | none |
| tốc độ cho phép | `speed`, `speed limit` | the speed limit | Art. 10.11, src 680; 14.1.2(c) | none |
| BẢO HIỂM VẬT CHẮT XE Ô TÔ | `An own-damage section`, `An own-damage loss` | own damage to the car (Chapter II) | src 683 (OCR "CHẮT" for "CHẤT") | literally "material damage of the car" |
| tai nạn bất ngờ, không lường trước được | `sudden and unforeseen` | sudden and unforeseen | Art. 11.1, src 687 | none |
| Hỏa hoạn, cháy, nổ | `fire or explosion` | fire, burning, explosion | Art. 11.1.2, src 689 | none |
| tai họa bất khả kháng do thiên nhiên | `a natural catastrophe beyond control` | natural catastrophes | Art. 11.1.3, src 690 | none |
| Mất toàn bộ xe do trộm, cướp | `theft or robbery of the whole vehicle` | theft of the whole car | Art. 11.1.4, src 691 | "cướp" is robbery (with force), "trộm" theft |
| Chi phí ngăn ngừa hạn chế tổn thất phát sinh thêm | `cost of preventing further loss` | cost of preventing further loss | Art. 11.2.1, src 702 | none |
| Chi phí cứu hộ và vận chuyển xe | `cost of rescue and towing to the nearest repairer` | rescue and towing | Art. 11.2.2, src 704 | none |
| Giá trị thị trường của xe | `market value when the contract was concluded`, `market value immediately before the loss` | the car's market value | Art. 12, src 711; 15.2 | the same term is used at two times (conclusion, and just before the loss) |
| hao mòn tự nhiên | `wear and tear, inherent vice, loss of value, defect or faulty repair` | wear and tear | Art. 13.5, src 755 | none |
| khu vực bị ngập nước | `vehicle operating in a flooded area` | a flooded area | Art. 13.6, src 760 | none |
| săm lốp | `a tyre or inner tube` | tyres and inner tubes | Art. 13.7, src 762; 15.1.3(e) | none |
| bạt thùng xe | `a goods-body canvas` | the canvas cover of a goods body | Art. 13.7, src 762 | none |
| thiết bị lắp thêm | `equipment added after manufacture`, `A listed item of added equipment` | equipment added after manufacture | Art. 13.10, src 781; BS10 | none |
| Giảm trừ bồi thường | `A reduction ground`, `Article 14.2.1 — the highest rate among` | reductions of the payment | Art. 14, src 791; Art. 24 | "giảm trừ" is a reduction, not a "deductible" ("mức khấu trừ") |
| Tổn thất bộ phận | `a partial loss` | a partial loss | Art. 15.1, src 887 | none |
| khấu hao | `A depreciation row`, `Article 15.1.3 — the depreciation rate, at` | depreciation | Art. 15.1.3, src 895 | none |
| Xe kinh doanh | `used for business` | a business vehicle | Art. 15.1.3, src 907 | undefined in the rules (X-03): commercial registration, use or tariff class |
| Tổn thất toàn bộ | `a total loss` | a total loss | Art. 15.2, src 963 | a constructive total loss at over 75% is included |
| Thu hồi tài sản sau bồi thường | `Article 16.2 — the share of the car Tasco takes after a total loss, under` | salvage | Art. 16, src 979 | none |
| giá trị thu hồi | `salvage value of a vehicle the owner keeps` | salvage value | Art. 16.2.2, src 988 | none |
| BẢO HIỂM TẠI NẠN LÁI XE | `An accident section`, `An accident to a person on board` | accident cover for the driver and passengers (Chapter III) | src 995 (OCR "TẠI" for "TAI") | none |
| đang ở trên xe, lên xuống xe | `on the vehicle, or getting on or off it` | on board, or getting on or off | Art. 18, src 1002 | none |
| tham gia đánh nhau | `fighting, not in self-defence` | taking part in a fight | Art. 19.3, src 1010 | none |
| cảm đột ngột, trúng gió, bệnh tật | `sudden illness, stroke or disease` | sudden illness, "wind stroke", disease | Art. 19.4, src 1012 | "trúng gió" is a folk diagnosis with no clinical English equivalent |
| thương tật thân thể | `bodily injury` | bodily injury | Art. 20.2, src 1026 | none |
| Thương tật tạm thời | `permanent` = FALSE | temporary injury | Art. 20.2.2(a), src 1033 | none |
| Thương tật vĩnh viễn | `permanent` = TRUE | permanent injury | Art. 20.2.2(b), src 1038 | none |
| tử vong | `death` | death | Art. 20.1, src 1023 | none |
| TRÁCH NHIỆM DÂN SỰ CỦA CHỦ XE | `A goods section`, `A loss of goods` | the owner's civil liability for goods carried (Chapter IV) | src 1050 | none |
| hợp đồng vận chuyển giữa Chủ xe và Chủ hàng | `carried under a contract of carriage between owner and cargo owner` | contract of carriage | Art. 21.1, src 1064 | none |
| Giá trị hàng hóa | `actual damage` | value of the goods | Art. 22, src 1088 | none |
| số tiền bảo hiểm tham gia/ tấn | `sum insured per tonne` | sum insured per tonne | Art. 25, src 1204 | none |
| tổng mức trách nhiệm bảo hiểm | `total limit of liability` | total limit | Art. 26, src 1209 | none |
| người thứ ba | `A third-party claim`, `A head of third-party loss` | third party | Art. 28, src 1223 | none |
| bảo hiểm bắt buộc trách nhiệm dân sự của chủ xe cơ giới | `compulsory insurance in force`, `compulsory limit for this head`, `excluded under the compulsory scheme` | compulsory third-party motor insurance | Art. 27, src 1218; 28, 30 | none |
| Tỷ lệ trả tiền | `rate under the compulsory table` | the payment rate in the compulsory scheme's table | Art. 29.1, src 1235 | none |
| Mức trách nhiệm tự nguyện | `voluntary limit for bodily injury per person per accident` | the voluntary limit | Art. 29.1, src 1235 | none |
| Tỷ lệ lỗi | `fault ratio of the owner or driver` | share of fault | Art. 29.3, src 1244 (OCR "lỷ lệ lỗi"; "Tỷ lệ lỗi" at src 1235) | none |
| Điều khoản bảo hiểm bổ sung | `An additional clause`, `An additional clause on the policy` | additional clause | Art. 31, src 1269 | none |
| không khẩu hao khi thay thế mới | `BS01 new for old` | no depreciation on replacement | BS01, src 1290 | none |
| lựa chọn cơ sở sửa chữa | `BS02 choice of repairer` | choice of repairer | BS02, src 1296 | none |
| khi xe hoạt động trong khu vực bị ngập nước | `BS03 water damage to engine and electrics` | engine and electrics damaged in a flooded area | BS03, src 1307-1309 | none |
| mất bộ phận của xe do bị trộm, cướp | `BS04 theft of parts` | theft of parts | BS04, src 1320 | none |
| Bảo hiểm vật chất xe ngoài lãnh thổ Việt Nam | `BS05 own damage outside Vietnam`, `countries named for BS05` | own damage abroad | BS05, src 1336 | none |
| xe miễn thuế, tạm nhập, tái | `BS06 duty-free or temporarily imported vehicle` | duty-free or temporarily imported vehicles | BS06, src 1354 | none |
| Bảo hiểm thuê xe trong thời gian sửa chữa | `BS07 hire car during repair`, `BS07 — the hire paid, for` | hire car during repair | BS07, src 1376 | none |
| Bảo hiểm vật chất xe lưu hành tạm thời | `BS08 temporary circulation` | temporary circulation | BS08, src 1391 | none |
| Bảo hiểm vật chất xe hoạt động trong khu vực nội bộ | `BS09 vehicle used only inside a closed site` | vehicles used only within a site | BS09, src 1413 | "nội bộ" is internal; the clause lists the sites |
| liên quan đến thiết bị lắp thêm | `BS10 added equipment` | added equipment | BS10, src 1429 | none |
| xe tập lái | `BS11 driving-school vehicle` | driving-school vehicles | BS11, src 1442 | none |
| các hành động đập phá, phá hoại | `BS12 vandalism in riots`, `vandalism in a demonstration, riot or public disorder` | vandalism | BS12, src 1478 | none |
| liên quan đến thiết bị chuyên dùng | `BS13 special equipment` | special equipment | BS13, src 1488 | none |
| Bảo hiểm hàng hóa trên xe cùng chủ | `BS14 the owner's own goods` | the owner's own goods | BS14, src 1509 | none |
| cải tạo/ hoán cải | `BS15 converted goods vehicle` | converted vehicles | BS15, src 1521 | none |
| Điều khoần bảo hiểm bố sung khác (as the OCR has it) | `BS16 another clause agreed in writing` | other additional clauses | Chapter VI item 16, src 1538 | the code BS16 is the encoder's; the text has no code |
| Bảng tỷ lệ trả tiền bảo hiểm thương tật | `An injury table row`, `the injury table` | the table of injury rates | Art. 20.2, src 1029; appendix | the table has three names (X-18) |
| CÁC TRƯỜNG HỢP ĐƯỢC GIẢI QUYẾT BÒI THƯỜNG 100% | section "A" | the cases paid at 100% | appendix, src 1555 (OCR "BÒI") | none |
| CÁC TRƯỜNG HỢP TỔN THƯƠNG BỘ PHẬN | sections "B.I" to "B.X" | partial injuries | appendix, src 1562 | none |
| Ghi chú | quoted notes in `tasco-injury-table.l4` | a note in the table | appendix, src 1590 and others | none |
| cộng lùi | (not computed) | the table's method for adding a further rate | appendix, src 1626 and others | a term of art of Vietnamese disability assessment; the encoding does not compute it, since the rows give the assessor the result (`assessed rate`) |
| Thị lực | `A level of corrected sight`, `the table of rates for reduced sight` | corrected visual acuity | appendix, src 3749-3754 | none |
| Hội đồng giám định y khoa | section "unlisted" with the recorded `assessed rate` | the medical assessment council | appendix special case 5, src 4126 | none |
| Nạn nhân bị chết nhưng không xác định được tung tích | `identified, with a lawful heir` = FALSE | an unidentified deceased victim | appendix special case 6, src 4128 | none |
| chi phí thực tế cần thiết để mai táng | `cost of burial and of keeping the remains for identification` | burial costs | appendix special case 6, src 4129 (OCR "chỉ phí") | none |
