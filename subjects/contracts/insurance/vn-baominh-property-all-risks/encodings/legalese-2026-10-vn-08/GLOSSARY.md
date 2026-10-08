# Glossary — Bảo Minh property all risks rules (row `legalese-2026-10-vn-08`)

The bilingual deliverable: every term the document defines, and every type, field, constructor or constant the L4 `DECLARE`s that renders a Vietnamese concept, with the source words beside the English identifier.
The Vietnamese column is copied from `../../source/raw/baominh-par.txt` and checked by `tools/vnsrc.py check`; a phrase that spans a line break of the rendering is given whole, and where a long phrase is shortened the src line says where the rest is.
"none: literal" in the last column means the English is the ordinary rendering and carries no legal sense the Vietnamese lacks.
Identifiers the encoder coined with no Vietnamese behind them (`stock`, `other property`, `a cause not named in this document`, the test fixtures) have no row.

283 rows.

| Vietnamese term (verbatim) | English identifier in the L4 | English meaning, one line | where defined or used (Điều / clause, src line) | translation risk |
| --- | --- | --- | --- | --- |
| Tổn hại | `the loss is Damage as defined`; the capitalised word Damage throughout | the defined term: physical loss and damage, or destruction, that is sudden and unforeseen | insuring clause, src:17-18 | The everyday word means harm or damage; the document defines it wider (loss, damage and destruction) and narrower (only if "bất ngờ"). The encoding writes Damage, capitalised, for the defined term only; the document itself also uses lower-case "tổn hại" and "thiệt hại" (Finding 12). |
| có tính bất ngờ | `sudden and unforeseen` | the quality the definition of Damage requires | insuring clause, src:18 | "bất ngờ" is sudden and also unexpected; the English PAR pair "sudden and unforeseen" names two tests (time, foresight) where the Vietnamese has one word. Gradual but unforeseen damage is the case the choice decides (fork F1). |
| tổn thất và thiệt hại vật chất hoặc bị phá hủy | `physical loss, destruction or damage` | the physical element of Damage | insuring clause, src:18 | none: literal |
| Bảo Minh | `the Insurer` | Bao Minh Insurance Corporation, the document's short name for itself | src:8-9 and throughout | A proper name; the identifier uses the role so that sibling encodings can share it. |
| Người bảo hiểm | `the Insurer` | the insurer, used three times and never defined | GC 10 heading src:361; src:420, 453 | Read as Bảo Minh; the document does not say so (Finding 12). |
| Người được bảo hiểm | `the Insured` | the person insured, named in the Schedule | src:7 and throughout | none: literal |
| Bản tóm lược hợp đồng bảo hiểm | `The Schedule` | the policy schedule: the particulars of this policy | src:7, 14, 23, 24; GC 1 src:256 | Literally "summary of the insurance contract"; it does the work of an English Schedule or declarations page, and GC 1 makes it part of the contract. Also written "Bản tóm lược bảo hiểm" (src:152-153) and "Bản tóm lược hợp đồng" (src:256, 411). |
| Hợp đồng bảo hiểm số | `policy number` | the policy number, a blank in the form | src:4 | none: literal |
| Thời hạn bảo hiểm | `the period of insurance`; `A period` | the period stated in the Schedule | insuring clause src:13; proviso src:20 | none: literal |
| chấp nhận tái tục | `renewal periods paid for and accepted` | a later period the Insured pays for and the Insurer accepts | insuring clause src:15 | none: literal |
| hạng mục tài sản được bảo hiểm | `An item in the Schedule` | an item of insured property with its own sum insured | proviso (i) src:22-23 | "hạng mục" is an item or category; an item may be a class of property ("stock"), not one object. |
| số tiền bảo hiểm | `sum insured` | the sum insured of an item | proviso src:22; GC 11 src:389; GC 14 src:413 | none: literal |
| tổng số tiền bảo hiểm | `the total sum insured` | the total sum insured under the policy | proviso (i) src:22 | none: literal |
| giới hạn trách nhiệm | `A limit of liability` | a limit of liability stated in the Schedule | proviso (ii) src:24 | none: literal |
| tổng trách nhiệm của Bảo Minh trong Thời hạn bảo hiểm | `already paid on this item in the period of insurance`; `already paid under this policy in the period` | the Insurer's aggregate liability in the period, which these fields count down | proviso src:20 | The proviso is an aggregate cap; the fields record what has already been paid against it. |
| các khoản miễn thường được kê khai | `the deductible for each loss` | the deductible stated in the Schedule | GC 13 src:404 | "miễn thường" is the deductible or excess; "đối với mỗi tổn thất" makes it per loss, and "tổn thất" is undefined (fork F31). |
| phí bảo hiểm năm | `the annual premium` | the annual premium, the base of the short-period scale | GC 3 src:278-281 | none: literal |
| phí bảo hiểm | `the premium for the period` | the premium for the period, the base of a pro rata refund | GC 3 src:272 | none: literal |
| đã trả phí bảo hiểm hoặc đồng ý trả phí bảo hiểm | `the Insured has paid or agreed to pay the premium` | the recital's premium condition | insuring clause src:7-8 | none: literal |
| khủng bố | `the act is terrorism as exclusion 3(c) defines it`; `An act of force or violence` | terrorism, as exclusion 3(c) defines it for that exclusion only | excl. 3(c) src:84-89 | Defined "theo loại trừ 3 (c) này" only; the definition's purposes (political, religious, ideological or similar) are the test, not criminal law's. |
| việc sử dụng bạo lực hoặc vũ lực | `use of force or violence, or a threat of it, by a person or a group of persons`; cause `an act of force or violence, or a threat of it` | the act element of the definition | excl. 3(c) src:85-86 | "bạo lực" (violence) and "vũ lực" (force) are near synonyms; both are kept. |
| các mục đích chính trị, tôn giáo, hệ tư tưởng hoặc các mục đích tương tự | `for a political, religious, ideological or similar purpose` | the purpose element of the definition | excl. 3(c) src:87-88 | none: literal |
| đốt cháy | folded into cause `ionising radiation or radioactive contamination from nuclear fuel or nuclear waste` | combustion, defined to include any self-sustaining process of nuclear fission | excl. 4(b)(i) src:115-117 | Literally burning; the definition makes it a term of art, which the cause carries. |
| DỮ LIỆU ĐIỆN TỬ | kind `electronic data`; cause `loss, damage, destruction, distortion, erasure, corruption or alteration of electronic data` | electronic data, as the second exclusion 10 defines it, including programs and software | second excl. 10(a)(i) src:186-190 | none: literal |
| VIRUS MÁY ĐIỆN TOÁN | `a computer virus` | computer virus, as defined | second excl. 10(a)(i) src:191-194 | "máy điện toán" is an older word for computer; the definition is wider than viruses (any harmful or unauthorised instructions or code). |
| điều kiện tiên quyết | `why the general conditions defeat the claim` | condition precedent: the insuring clause makes every rule, condition and exclusion one | insuring clause src:10-11; GC 15 src:420 | The English term of art implies a breach defeats the claim outright; the Vietnamese says the same ("tiên quyết", decisive beforehand), and the Law softens it for late notice (fork F28). |
| BẢO MINH SẼ BỒI THƯỜNG | `the Insurer must pay` | the Insurer will indemnify | insuring clause src:16 | "bồi thường" is to indemnify or compensate; the constructor names the result, an amount. |
| Bảo Minh sẽ không chịu trách nhiệm bồi thường | `nothing is payable because` | the Insurer is not liable to indemnify | GC 2 src:266-267 | none: literal |
| LOẠI TRỪ | `The effect of the exclusions on an item`; `excluded by` | exclusions | src:27 | none: literal |
| chỉ có trách nhiệm bồi thường phần Tổn hại phát sinh từ nguyên nhân đó | `excluded except for the part arising from a cause not excluded` | liable only for the part of the Damage from that cause | excl. 1(c) src:60-61; cf. 1(a) src:35-36, 8(h) src:166-167 | none: literal |
| một nguyên nhân không bị hợp đồng bảo hiểm loại trừ | `the cause is excluded for the item` (negated); `a cause not excluded directly caused the Damage to` | a cause not excluded by the policy | excl. 1 src:34, 42-43, 60; excl. 8(h) src:166 | Which exclusions make a cause "excluded" is fork F10. |
| trực tiếp hoặc gián tiếp | `direct` (in `A link in the chain of causation`) | directly or indirectly | excl. 3 src:76; 4 src:111; 11 src:218 | The document's contrast between this phrase and plain "gây ra bởi" (caused by) is how the encoding reads causation (fork F3). |
| gây ra bởi | `A link in the chain of causation`; `a direct cause of the Damage to` | caused by | excl. 1 src:29; 6 src:135; 8(h) src:166 | Read as the direct cause (fork F3); English "caused by" carries proximate-cause doctrine the Vietnamese does not name. |
| do có Tổn hại cho tài sản được bảo hiểm | `resulting from earlier Damage by` | following earlier Damage to the insured property | excl. 1(b) src:41-42; 1(c) src:62 | none: literal |
| thiết kế sai | `faulty design` | faulty design | excl. 1(a)(i) src:30 | none: literal |
| khuyết tật của nguyên vật liệu | `defective material` | defective material | excl. 1(a)(i) src:30 | none: literal |
| tay nghề kém | `defective workmanship` | poor workmanship | excl. 1(a)(i) src:30 | Literally "poor skill"; English "defective workmanship" is the PAR term. |
| khuyết tật ẩn tỳ | `latent defect` | latent defect | excl. 1(a)(i) src:30 | none: literal |
| hư hỏng dần | `gradual deterioration` | gradual deterioration | excl. 1(a)(i) src:30-31 | none: literal |
| biến dạng | `deformation` | deformation | excl. 1(a)(i) src:31 | Whether "do quá trình sử dụng" (from use) also qualifies it is fork F6. |
| hao mòn do quá trình sử dụng | `wear and tear from use` | wear and tear from use | excl. 1(a)(i) src:31 | none: literal |
| ngừng cung cấp nước | `interruption of the water supply to or from the insured premises` | interruption of the water supply | excl. 1(a)(ii) src:32 | none: literal |
| khí đốt | `interruption of the gas supply to or from the insured premises` | gas | excl. 1(a)(ii) src:32 | none: literal |
| điện | `interruption of the electricity supply to or from the insured premises` | electricity | excl. 1(a)(ii) src:32 | none: literal |
| hệ thống nhiên liệu | `interruption of the fuel system to or from the insured premises` | the fuel system | excl. 1(a)(ii) src:32 | none: literal |
| hư hỏng của hệ thống thải rác tới hoặc từ Địa điểm được bảo hiểm | `failure of the waste disposal system to or from the insured premises` | failure of the waste disposal system | excl. 1(a)(ii) src:32-33 | "thải rác" is refuse or waste; the English PAR clause says sewerage. The encoding keeps "waste disposal". |
| sụp đổ | `collapse of an insured building` | collapse | excl. 1(b)(i) src:37 | none: literal |
| rạn nứt các ngôi nhà được bảo hiểm | `cracking of an insured building` | cracking of insured buildings | excl. 1(b)(i) src:37 | none: literal |
| ăn mòn | `corrosion` | corrosion | excl. 1(b)(ii) src:38 | none: literal |
| gỉ | `rust` | rust | excl. 1(b)(ii) src:38 | none: literal |
| điều kiện cực đoan hoặc sự thay đổi của nhiệt độ, độ ẩm, khô của thời tiết | `extreme or changing temperature, humidity or dryness of the weather` | extremes or changes of temperature, humidity or dryness of the weather | excl. 1(b)(ii) src:38 | none: literal |
| mục nát | `rot` | rot | excl. 1(b)(ii) src:39 | none: literal |
| nấm mốc | `mould` | mould | excl. 1(b)(ii) src:39 | none: literal |
| hao hụt | `shrinkage` | shrinkage | excl. 1(b)(ii) src:39 | Also "wastage" or "loss in quantity"; PAR wording says shrinkage. |
| bốc hơi | `evaporation` | evaporation | excl. 1(b)(ii) src:39 | none: literal |
| mất trọng lượng | `loss of weight` | loss of weight | excl. 1(b)(ii) src:39 | none: literal |
| thay đổi màu sắc, mùi vị, chất liệu hoặc bề mặt | `change of colour, flavour, texture or finish` | change of colour, flavour, texture or finish | excl. 1(b)(ii) src:39-40 | "chất liệu" is material or substance; "texture" is the PAR word. |
| hư hại do tác động của ánh sáng | `the action of light` | damage by the action of light | excl. 1(b)(ii) src:40 | none: literal |
| sâu bọ | `vermin` | vermin | excl. 1(b)(ii) src:40 | Literally worms and bugs; PAR says vermin. |
| côn trùng | `insects` | insects | excl. 1(b)(ii) src:40 | none: literal |
| trầy sướt | `scratching` | scratching | excl. 1(b)(ii) src:40 | none: literal |
| trộm cắp | `theft` | theft | excl. 1(c)(i) src:48; GC 9(a)(iii) src:341 | none: literal |
| các hành vi lừa đảo hoặc không trung thực | `a fraudulent or dishonest act` | fraudulent or dishonest acts | excl. 1(c)(ii) src:50 | none: literal |
| biến mất không giải thích được | `unexplained disappearance` | unexplained disappearance | excl. 1(c)(iii) src:51 | none: literal |
| thiếu hụt khi kiểm kê | `inventory shortage` | shortage found at stocktaking | excl. 1(c)(iii) src:51 | none: literal |
| không rõ nguyên nhân | `an unknown cause` | an unknown cause | excl. 1(c)(iii) src:51 | Read as a separate item ("biến mất không giải thích được, thiếu hụt khi kiểm kê hoặc không rõ nguyên nhân"); it may instead qualify the shortage ("shortage of unknown cause"), which would narrow it (Finding 19). |
| khiếm khuyết khi ghi chép thông tin | `an error in recording information` | an error in recording information | excl. 1(c)(iii) src:52 | none: literal |
| thiếu hụt khi cung cấp hoặc giao nhận nguyên vật liệu | `a shortage in the supply or delivery of materials` | a shortage in supplying or delivering materials | excl. 1(c)(iii) src:52-53 | none: literal |
| thiếu hụt do lỗi hành chính, kế toán | `an administrative or accounting error` | a shortage from an administrative or accounting error | excl. 1(c)(iii) src:53 | none: literal |
| tình trạng quá nóng của nồi hơi, bình tiết kiệm, bình hoặc ống nối | `cracking, fracture, collapse or overheating of a boiler, economiser, vessel or pipe` | cracking, fracture, collapse or overheating of boilers, economisers, vessels or pipes | excl. 1(c)(iv) src:54-55 | "bình tiết kiệm" (economiser) here; the first exclusion 10 says "bình áp suất tiết kiệm" (pressure economiser) for the same thing. |
| rò rỉ các mối hàn của nồi hơi | `leakage of a boiler weld` | leaking boiler welds | excl. 1(c)(iv) src:55 | none: literal |
| hư hỏng hoặc đổ vỡ về cơ hoặc điện của máy móc hoặc thiết bị | `mechanical or electrical breakdown or derangement of machinery or equipment` | mechanical or electrical breakdown of machinery or equipment | excl. 1(c)(v) src:56 | none: literal |
| vỡ, tràn hoặc rò rỉ các bể nước, đường ống hoặc thiết bị chứa nước | `bursting, overflowing or leaking of water tanks, pipes or apparatus` | bursting, overflowing or leaking of water tanks, pipes or apparatus | excl. 1(c)(vi) src:57; excl. 6 src:138-139 | Exclusion 6 words the same peril "vỡ tràn nước hoặc rò rỉ nước từ các bể chứa, đường ống, thiết bị nước"; one constructor serves both. |
| sự sói mòn của sông, biển | `erosion by river or sea` | erosion by river or sea | excl. 1(d)(i) src:64 | none: literal |
| sụt, nâng hoặc lở đất | `subsidence`; `heave`; `landslip` | subsidence, heave or landslip | excl. 1(d)(ii) src:65 | "sụt" (sinking) and "nâng" (rising) take "đất" (ground) by sharing; three constructors. |
| sự lún đất thông thường hoặc lún ổn định của các kiến trúc mới xây dựng | `normal settlement or bedding down of new structures` | normal settlement or bedding down of new structures | excl. 1(d)(iii) src:66 | none: literal |
| gió, mưa, mưa đá, sương, tuyết, lụt, cát | `wind`; `rain`; `hail`; `frost`; `snow`; `flood`; `sand` | the weather perils of 1(d)(iv) | excl. 1(d)(iv) src:68 | "sương" is dew or mist as well as frost; PAR says frost. "lụt" (flood) differs from exclusion 6's "bão lụt" (storm flood). |
| bụi | `dust` | dust | excl. 1(d)(iv) src:69 | none: literal |
| sự đông rắn lại do lạnh | `solidification by cold` | solidification by cold | excl. 1(d)(v) src:70 | PAR speaks of the solidification of molten material; "do lạnh" (by cold) is the Vietnamese text's own. |
| việc tràn ra bên ngoài của các kim loại bị nóng chảy | `escape of molten metal` | escape of molten metal | excl. 1(d)(v) src:70 | none: literal |
| hành động ác ý | `a malicious act of the Insured or of anyone acting for the Insured` | a malicious act of the Insured or its representative | excl. 2(a) src:72 | "bất kỳ ai đại diện cho" is anyone acting for, or representing, the Insured: whether an employee's act counts is not stated. |
| cố tình bất cẩn | `wilful negligence of the Insured or of anyone acting for the Insured` | wilful negligence | excl. 2(a) src:72 | An oxymoron in both languages (deliberate carelessness); English "wilful negligence" is the PAR term. |
| ngừng công việc | `cessation of work` | cessation of work | excl. 2(b) src:74 | none: literal |
| chậm trễ | `delay` | delay | excl. 2(b) src:74 | none: literal |
| mất thị trường | `loss of market` | loss of market | excl. 2(b) src:74 | none: literal |
| bất kỳ loại tổn thất hậu quả | `consequential loss of any other kind` | any other consequential loss | excl. 2(b) src:74-75 | none: literal |
| chiến tranh | `war` | war | excl. 3(a) src:79 | none: literal |
| xâm lược | `invasion` | invasion | excl. 3(a) src:79 | none: literal |
| hành động của ngoại thù | `act of a foreign enemy` | act of foreign enemies | excl. 3(a) src:79 | none: literal |
| hành động thù địch | `hostilities` | hostilities | excl. 3(a) src:79 | none: literal |
| hoạt động tương tự chiến tranh | `warlike operations` | warlike operations | excl. 3(a) src:79-80 | none: literal |
| nội chiến | `civil war` | civil war | excl. 3(a) src:80 | none: literal |
| binh biến | `mutiny` | mutiny | excl. 3(b) src:81 | none: literal |
| xung đột là một phần của hoặc dẫn đến sự nổi dậy của công chúng | `civil commotion amounting to or forming part of a popular rising` | civil commotion amounting to a popular rising | excl. 3(b) src:81-82 | "xung đột" is conflict; PAR says civil commotion. |
| nổi dậy của quân đội | `military rising` | military rising | excl. 3(b) src:81-82 | none: literal |
| khởi nghĩa | `insurrection` | insurrection | excl. 3(b) src:82 | none: literal |
| nổi loạn | `rebellion` | rebellion | excl. 3(b) src:82 | none: literal |
| cách mạng | `revolution` | revolution | excl. 3(b) src:82 | none: literal |
| lực lượng quân sự tiếm quyền | `military or usurped power` | military or usurped power | excl. 3(b) src:82 | none: literal |
| tịch thu tài sản, quốc hữu hóa, trưng dụng theo lệnh của cơ quan công quyền hợp pháp | `confiscation, nationalisation or requisition by order of a lawful public authority` | confiscation, nationalisation or requisition by lawful authority | excl. 3 d)(i) src:90-91 | none: literal |
| việc chiếm hữu bất hợp pháp của bất kỳ người nào | `unlawful occupation of a building by any person` | unlawful occupation by any person | excl. 3 d)(ii) src:92-93 | none: literal |
| phá hủy tài sản được bảo hiểm do lệnh của nhà cầm quyền | `destruction by order of a public authority` | destruction by order of the authorities | excl. 3(e) src:101 | none: literal |
| nhằm khống chế, ngăn chặn, trấn áp | `action taken to control, prevent or suppress an event in exclusion 3(a) to (c)` | action to control, prevent or suppress | excl. 3, extension src:103 | none: literal |
| nguyên liệu vũ khí hạt nhân | `nuclear weapons material` | nuclear weapons material | excl. 4(a) src:113 | none: literal |
| phóng xạ ion hóa hoặc ô nhiễm phóng xạ từ nhiên liệu hạt nhân | `ionising radiation or radioactive contamination from nuclear fuel or nuclear waste` | ionising radiation or radioactive contamination | excl. 4(b)(i) src:114 | none: literal |
| chất phóng xạ, chất nổ hoặc các thành phần nguy hiểm khác | `the radioactive, explosive or other hazardous properties of a nuclear explosive device` | radioactive, explosive or other hazardous components of a nuclear explosive device | excl. 4(b)(ii) src:118-119 | "chất" is substance and "thành phần" component; PAR says "properties". A component reading is narrower. |
| ô nhiễm hoặc nhiễm bẩn | `pollution or contamination` | pollution or contamination | excl. 5 src:120-123 | none: literal |
| cháy | `fire` | fire | excl. 6 src:135; second 10 src:195; 11 src:234 | none: literal |
| nổ | `explosion` | explosion | excl. 6 src:135; second 10 src:195; 11 src:234 | none: literal |
| sét đánh | `lightning` | lightning | excl. 6 src:135-136; 11 src:234 | none: literal |
| máy bay rơi | `falling aircraft` | aircraft falling | excl. 6 src:136; 11 src:234 | none: literal |
| đình công | `strike` | strike | excl. 6 src:136; 11 src:235 | none: literal |
| biểu tình | `demonstration` | demonstration, protest | excl. 6 src:136 | PAR's list has "riot" here; "biểu tình" is a demonstration and is not "bạo loạn" (riot) of exclusion 11. Kept apart (Finding 9). |
| công nhân tham gia bế xưởng | `workers taking part in a lockout` | locked-out workers | excl. 6 src:136 | none: literal |
| người tham gia tranh chấp lao động | `persons taking part in a labour dispute` | persons taking part in labour disturbances | excl. 6 src:136-137 | none: literal |
| người có hành động ác ý | `a malicious act of another person` | malicious persons | excl. 6 src:137 | Distinguished from exclusion 2(a)'s malicious act of the Insured. |
| đâm va với các phương tiện giao thông hoặc súc vật trên đường | `impact by road vehicles or animals` | impact by road vehicles or animals | excl. 6 src:137-138 | Exclusion 11 says "xe cộ đâm va" (vehicle impact) without animals; kept apart (Finding 9). |
| động đất | `earthquake` | earthquake | excl. 6 src:138; 11 src:236 | none: literal |
| bão biển | `sea storm` | storm (literally sea storm, typhoon) | excl. 6 src:138 | PAR says "storm"; "bão" is a typhoon-scale storm and "biển" is sea. Exclusion 11 says "giông bão". |
| bão lụt | `storm flood` | storm flood, tempest | excl. 6 src:138 | PAR says "tempest" or "flood"; 1(d)(iv) says "lụt" (flood). |
| quá trình xấy khô hoặc xử lý có sử dụng nhiệt | `a drying process or a process using heat` | a drying or heat process | excl. 8(f) src:161 | none: literal |
| quá trình tháo dỡ và lắp đặt lại | `installing or moving the machinery or equipment, including dismantling and re-erecting it` | installation or removal, including dismantling and re-erection | excl. 8(g) src:162-163 | none: literal |
| sửa chữa, kiểm tra, lắp đặt hoặc bảo dưỡng | `the repair, inspection, installation or maintenance work`; `undergoing repair, inspection, installation or maintenance` | repair, inspection, installation or maintenance | excl. 8(h) src:164 | none: literal |
| khi phát nổ hoặc gãy vỡ | `explosion or rupture of the boiler, vessel, machine or apparatus itself` | their own explosion or rupture | first excl. 10 src:176 | none: literal |
| tổn thất, tổn hại, phá hủy, biến dạng, tẩy xóa, hư hỏng hoặc thay đổi các DỮ LIỆU ĐIỆN TỬ | `loss, damage, destruction, distortion, erasure, corruption or alteration of electronic data` | loss of or damage to electronic data | second excl. 10(a)(i) src:181-182 | none: literal |
| xử lý dữ liệu có liên quan đến việc thay đổi ngày tháng | `processing of data involving a change of date, by a computer system or chip` | processing of data involving a date change | excl. 11 Part 1 a. src:220-221 | "mạch tích hợp điện tử, mạch điện hợp nhất" (microchip, integrated circuit) are folded into "chip". |
| bất kỳ thay đổi, bổ sung có liên quan đến thay đổi ngày tháng | `a change or modification involving a change of date, to a computer system or chip` | a change or modification involving a date change | excl. 11 Part 1 b. src:226 | none: literal |
| xe cộ đâm va | `impact by vehicles` | vehicle impact | excl. 11 src:234-235 | See "đâm va với các phương tiện giao thông" above. |
| vật thể lạ rơi | `falling objects` | falling objects | excl. 11 src:235 | Literally "strange objects falling"; PAR says falling objects. |
| giông bão | `windstorm` | windstorm, thunderstorm | excl. 11 src:235 | "giông" is a thunderstorm; PAR says windstorm. |
| mưa đá | `hail` | hail | excl. 1(d)(iv) src:68; 11 src:235 | none: literal |
| lốc xóay | `whirlwind` | whirlwind, tornado | excl. 11 src:235 | PAR says cyclone or tornado; "lốc" is a whirlwind. |
| bạo loạn | `riot` | riot | excl. 11 src:235 | See "biểu tình". |
| dân biến | `civil commotion` | civil commotion | excl. 11 src:235 | Compare exclusion 3(b)'s civil commotion amounting to a rising. |
| hành vi côn đồ | `hooliganism` | hooliganism | excl. 11 src:235 | PAR says malicious damage; "côn đồ" is thuggery. |
| hành động phá hoại | `acts of sabotage` | sabotage, vandalism | excl. 11 src:236 | Could equally be vandalism. |
| núi lửa phun | `volcanic eruption` | volcanic eruption | excl. 11 src:236 | none: literal |
| sóng thần | `tsunami` | tsunami | excl. 11 src:236 | none: literal |
| đóng băng | `freezing` | freezing | excl. 11 src:236 | none: literal |
| sức nặng của băng tuyết | `the weight of ice and snow` | the weight of ice and snow | excl. 11 src:236-237 | none: literal |
| tiền | `money` | money | excl. 6(a) src:127 | none: literal |
| séc | `cheques` | cheques | excl. 6(a) src:127 | none: literal |
| tem phiếu | `stamps` | stamps and coupons | excl. 6(a) src:127 | "phiếu" adds coupons or vouchers. |
| chứng khóan các loại | `securities of any kind` | securities of any kind | excl. 6(a) src:127 | none: literal |
| khế ước | `deeds` | deeds, bonds | excl. 6(a) src:127 | "khế ước" is any written contract or deed. |
| thẻ tín dụng | `credit cards` | credit cards | excl. 6(a) src:127 | none: literal |
| các loại trang sức quý | `precious jewellery` | precious jewellery | excl. 6(a) src:127 | none: literal |
| đá quý | `precious stones` | precious stones | excl. 6(a) src:127-128 | none: literal |
| kim loại quý | `precious metals` | precious metals | excl. 6(a) src:128 | none: literal |
| vàng nén | `bullion` | bullion (literally gold bars) | excl. 6(a) src:128 | Gold only, literally; bullion includes silver. |
| lông thú | `furs` | furs | excl. 6(a) src:128 | none: literal |
| đồ cổ | `antiques` | antiques | excl. 6(a) src:128 | PAR says curiosities. |
| tác phẩm nghệ thuật | `works of art` | works of art | excl. 6(a) src:128 | none: literal |
| kính lắp cố định | `fixed glass` | fixed glass | excl. 6(b) src:131 | none: literal |
| không phải là kính lắp cố định | `glass other than fixed glass` | glass that is not fixed | excl. 6(c) src:132 | none: literal |
| đồ sứ | `china` | china, porcelain | excl. 6(c) src:132 | none: literal |
| đất nung | `earthenware` | earthenware | excl. 6(c) src:132 | none: literal |
| đá cẩm thạch | `marble` | marble | excl. 6(c) src:132 | none: literal |
| các đồ dễ đổ vỡ khác | `other fragile articles` | other fragile articles | excl. 6(c) src:132-133 | none: literal |
| thiết bị điện tử | `electronic equipment` | electronic equipment | excl. 6(d) src:134 | none: literal |
| máy điện toán | `computers` | computers | excl. 6(d) src:134 | none: literal |
| thiết bị xử lý dữ liệu | `data processing equipment` | data processing equipment | excl. 6(d) src:134 | none: literal |
| Hàng hóa ký gởi | `goods on consignment` | goods on consignment | excl. 7 src:141 | none: literal |
| ủy thác | `goods held in trust` | goods held in trust | excl. 7 src:141 | none: literal |
| tài liệu | `documents` | documents | excl. 7 src:141 | none: literal |
| bản thảo | `manuscripts` | manuscripts | excl. 7 src:141 | none: literal |
| sổ sách kinh doanh | `business books` | business books | excl. 7 src:141 | none: literal |
| hệ thống dữ liệu máy tính | `computer data systems` | computer system records | excl. 7 src:141 | Literally "computer data systems"; PAR says computer system records. |
| vật mẫu | `samples` | samples | excl. 7 src:141-142 | none: literal |
| khuôn mẫu | `moulds` | moulds, patterns, models | excl. 7 src:142 | One word for PAR's "patterns, models, moulds". |
| bản vẽ thiết kế | `design drawings` | plans, designs | excl. 7 src:142 | none: literal |
| thuốc nổ | `explosives` | explosives | excl. 7 src:142 | none: literal |
| xe cơ giới được phép lưu thông trên đường công | `motor vehicles licensed for public roads, with their equipment and accessories` | motor vehicles licensed for road use | excl. 8(a) src:149 | none: literal |
| các xe kéo | `tractor vehicles` | tractors, towing vehicles | excl. 8(a) src:149-150 | none: literal |
| moóc | `trailers` | trailers | excl. 8(a) src:150 | none: literal |
| xe lửa | `trains` | trains | excl. 8(a) src:150 | none: literal |
| đầu máy xe lửa | `locomotives` | locomotives | excl. 8(a) src:150 | none: literal |
| phương tiện lăn trên đường ray | `rolling stock` | rolling stock | excl. 8(a) src:150 | none: literal |
| tàu thủy | `ships` | watercraft | excl. 8(a) src:150 | none: literal |
| máy bay | `aircraft` | aircraft | excl. 8(a) src:150 | none: literal |
| tàu không gian | `spacecraft` | spacecraft | excl. 8(a) src:151 | none: literal |
| các phương tiện tương tự | `similar conveyances` | similar conveyances | excl. 8(a) src:151 | none: literal |
| đất đai | `land, including topsoil, fill, drainage and culverts` | land, with topsoil, fill, drainage and culverts | excl. 8(d) src:156 | "nền đường" in the bracket is roadbed; PAR says fill. |
| đường lái xe vào các tòa nhà | `driveways to buildings` | driveways | excl. 8(d) src:156-157 | none: literal |
| vỉa hè | `pavements` | pavements | excl. 8(d) src:157 | none: literal |
| đường băng | `runways` | runways | excl. 8(d) src:157 | none: literal |
| đường sắt | `railway lines` | railway lines | excl. 8(d) src:157 | none: literal |
| đập | `dams` | dams | excl. 8(d) src:157 | none: literal |
| bể chứa | `reservoirs` | reservoirs; also tanks | excl. 8(d) src:157; excl. 6 src:138 | The same word is "tanks" in exclusion 6's write-back: read here as reservoirs, it still catches any tank (Finding 16). |
| kênh | `canals` | canals | excl. 8(d) src:157 | none: literal |
| giàn khoan | `rigs` | rigs | excl. 8(d) src:157 | none: literal |
| giếng | `wells` | wells | excl. 8(d) src:157 | none: literal |
| đường ống | `pipelines` | pipelines; also pipes | excl. 8(d) src:157-158; 1(c)(vi) src:57; 6 src:139 | The same word is "pipes" in 1(c)(vi) and exclusion 6 (Finding 16). |
| đường hầm | `tunnels` | tunnels | excl. 8(d) src:158 | none: literal |
| cầu | `bridges` | bridges | excl. 8(d) src:158 | none: literal |
| ụ tàu | `docks` | docks | excl. 8(d) src:158 | none: literal |
| cầu chắn sóng | `breakwaters` | breakwaters | excl. 8(d) src:158 | none: literal |
| cầu tàu | `piers` | piers, jetties | excl. 8(d) src:158 | none: literal |
| hố đào | `excavations` | excavations | excl. 8(d) src:158 | none: literal |
| bến tàu | `wharves` | wharves | excl. 8(d) src:158 | none: literal |
| mỏ | `mines` | mines | excl. 8(d) src:158 | none: literal |
| các tài sản dưới lòng đất | `underground property` | property underground | excl. 8(d) src:158-159 | none: literal |
| các tài sản ngoài khơi | `offshore property` | offshore property | excl. 8(d) src:159 | none: literal |
| gia súc | `livestock` | livestock | excl. 8(e) src:160 | none: literal |
| mùa màng | `crops` | growing crops | excl. 8(e) src:160 | none: literal |
| cây cối | `trees` | trees | excl. 8(e) src:160 | none: literal |
| nồi hơi | `boilers` | boilers | first excl. 10 src:174 | none: literal |
| bình áp suất tiết kiệm | `pressure economisers` | economisers | first excl. 10 src:174 | Literally "pressure saving vessel"; see "bình tiết kiệm" in 1(c)(iv). |
| tua-bin | `turbines` | turbines | first excl. 10 src:174 | none: literal |
| các bình chứa, máy móc, thiết bị khác có sử dụng áp lực | `other vessels, machinery or apparatus using pressure` | other vessels, machinery or apparatus in which pressure is used | first excl. 10 src:174-175 | "các bộ phận cấu thành bên trong" (internal components) at src:175 is PAR's "contents"; the kind covers both. |
| phương tiện xử lý dữ liệu điện tử | `electronic data processing media` | electronic data processing media | second excl. 10(b) src:201, 205 | "phương tiện" is means, media or vehicle; "các đĩa" (the disks) in the clause fixes media. |
| cổng, rào | `gates`; `fences` | gates and fences | excl. 1(d)(iv) src:68 | none: literal |
| ngôi nhà | `buildings` | buildings | excl. 1(b)(i) src:37 and throughout | The document also says "tòa nhà" (src:48, 264, 325, 328) for the insured building; both are read as one. |
| máy móc hoặc thiết bị | `machinery and equipment` | machinery or equipment | excl. 1(c)(v) src:56 | none: literal |
| tài sản được bảo hiểm | `A damaged item` | insured property, one item damaged in the loss | insuring clause src:11-12 | none: literal |
| tại địa điểm được bảo hiểm | `at the insured premises` | at the insured premises | insuring clause src:12 | "địa điểm" is a place or site; English "premises" carries buildings and land. |
| tài sản có thể di chuyển được | `movable` | movable property | excl. 1(d)(iv) src:67 | none: literal |
| để ngoài trời hoặc trong nhà không có vách chắn | `in the open or in a building without walls` | in the open or in open-sided buildings | excl. 1(d)(iv) src:67-68 | none: literal |
| được xác nhận là được bảo hiểm | `stated as insured in this policy` | confirmed as insured in this policy | excl. 6(a) src:128-129; excl. 7 "được ghi là được bảo hiểm" src:142 | 6(a) says "xác nhận" (confirmed), 7 says "ghi" (written); one field serves both. |
| trong quá trình di chuyển ngoài phạm vi địa điểm được bảo hiểm | `in transit outside the insured premises` | in transit outside the insured premises | excl. 8(b) src:152 | none: literal |
| đang bị phá dỡ, xây dựng hoặc lắp đặt | `in the course of demolition, construction or erection, or materials supplied for it` | under demolition, construction or erection | excl. 8(c) src:154 | none: literal |
| đang được lắp đặt, di chuyển | `being installed or moved` | being installed or moved | excl. 8(g) src:162 | none: literal |
| đã được thu xếp bảo hiểm theo cách khác | `insured in some other way` | otherwise insured | excl. 8(i) src:168 | Literally "arranged to be insured in another way" (Finding 1). |
| hợp đồng bảo hiểm hàng hải | `insured, or such that it would have to be insured, under a marine policy` | under a marine policy | excl. 9 src:171 | "có thể đã phải được bảo hiểm" is "would have had to be insured"; PAR says "would but for this policy be insured". |
| chi phí các đĩa lưu trữ trống | `the cost of blank media` | the cost of blank media | second excl. 10(b) src:206-207 | none: literal |
| chi phí sao chép dữ liệu điện tử từ nguồn dự phòng | `the cost of copying the data from back-up or from the originals` | the cost of copying data from back-up or from originals of a previous generation | second excl. 10(b) src:207-208 | none: literal |
| được sửa chữa, thay thế hoặc phục hồi | `the media are repaired, replaced or restored` | repaired, replaced or restored | second excl. 10(b) src:210 | none: literal |
| giá trị của tài sản tại thời điểm xảy ra tổn thất | `the Damage, valued at the time of the loss` | the value of the property at the time of the loss, or of the part damaged | insuring clause src:16-17 | "giá trị" (value) is unqualified: market value, actual cash value or replacement cost (fork F33). |
| phần Tổn hại phát sinh từ các nguyên nhân đó | `the part of the Damage arising from a cause not excluded` | the part of the Damage from a cause not excluded | excl. 1(a) src:35-36 | none: literal |
| giá trị thực tế | `the actual value of the item at the time of the loss` | actual value | GC 14 src:413 | "Actual value" in English may suggest actual cash value (after depreciation); the Vietnamese says only "real value". |
| các hợp đồng bảo hiểm khác | `sums insured by other insurances of the same property or loss` | other insurances | GC 6 src:300-301; GC 9(b)(ii) src:348 | none: literal |
| trách nhiệm có thể được bồi thường theo hợp đồng bảo hiểm hàng hải nếu như không có hợp đồng bảo hiểm này | `the amount the marine policy would pay if this policy did not exist` | what the marine policy would pay but for this policy | excl. 9 src:171-172 | none: literal |
| thông tin sai lệch | `false information about the property, the building, the business or the premises` | false information | GC 2 src:263 | none: literal |
| khai báo sai lệch các thông tin quan trọng | `a misstatement of a material fact` | misstatement of material information | GC 2 src:265 | none: literal |
| quên khai báo các thông tin mà dựa vào đó Bảo Minh đánh giá rủi ro | `an omission of a fact on which the Insurer assessed the risk` | omission of information on which the Insurer assessed the risk | GC 2 src:266 | "quên" is to forget: the omission is innocent on its face, and still operative (Finding 17). |
| THAY ĐỔI VÀ CHUYỂN DỜI | `A change under General Condition 8`; `A change affecting the item` | alteration and removal | GC 8 src:320 | none: literal |
| công việc kinh doanh, sản xuất của Người được bảo hiểm bị thay đổi | `a change of the Insured's business or manufacture` | the Insured's business or manufacture changed | GC 8(a) src:324 | none: literal |
| tính chất ngành nghề hoặc các hoàn cảnh khác thay đổi | `a change of occupation or other circumstances that increases the likelihood of loss` | the nature of the occupation or other circumstances changed so as to increase the likelihood of loss | GC 8(a) src:324-327 | none: literal |
| không có người trông coi | `the building or premises left unattended` | unattended | GC 8(b) src:328-329 | "trông coi" is to watch over; differs from 1(c)(vi)'s "bỏ trống hoặc không được sử dụng" (Finding 6). |
| trong thời hạn từ 30 ngày trở lên | `for days` | for 30 days or more | GC 8(b) src:329 | none: literal |
| bị di chuyển đến một địa điểm khác không được hợp đồng bảo hiểm này bảo hiểm | `removal to a place this policy does not cover` | removed to a place not covered | GC 8(c) src:330-331 | none: literal |
| quyền lợi của Người được bảo hiểm trong tài sản được bảo hiểm bị dịch chuyển sang cho người khác | `a transfer of the Insured's interest` | the Insured's interest passes to another | GC 8(d) src:332-333 | none: literal |
| bằng di chúc hoặc do hoạt động của pháp luật | `by will or by operation of law` | by will or operation of law | GC 8(d) src:333 | none: literal |
| chấp nhận cấp sửa đổi bổ sung | `accepted by endorsement before the loss` | accepted by endorsement | GC 8 src:322-323 | none: literal |
| các khoản chi phí | `claimed as a cost of changing or adding to a computer system, programme, software or chip` | costs | excl. 11 Part 2 src:239 | none: literal |
| thời điểm xảy ra tổn thất | `date of the loss` | the time of the loss | insuring clause src:16-17; GC 6 src:299 | Only the date is recorded; the document never needs the hour. |
| bỏ trống hoặc không được sử dụng | `the insured building was empty or not in use` | empty or not in use | excl. 1(c)(vi) src:58 | none: literal |
| cho là đã xảy ra trộm cắp hoặc các hành động ác ý | `theft or a malicious act was suspected` | theft or malicious acts suspected | GC 9(a)(iii) src:341-342 | none: literal |
| xảy ra trong tòa nhà được bảo hiểm | `in the insured building` | in the insured building | excl. 1(c)(i) src:48 | none: literal |
| sử dụng vũ lực hoặc bạo lực để đột nhập hoặc tẩu thóat | `with force or violence to break in or to get out` | forcible and violent entry or exit | excl. 1(c)(i) src:49 | none: literal |
| trước khi có sự truất hữu này | `before the dispossession` | before the dispossession | excl. 3 d) proviso src:99 | none: literal |
| trong khi bị truất hữu tạm thời | `during a temporary dispossession` | during temporary dispossession | excl. 3 d) proviso src:99 | none: literal |
| truất hữu tạm thời hay vĩnh viễn | `during or after a permanent dispossession`; `When the Damage happened, relative to a dispossession` | temporary or permanent dispossession | excl. 3 d)(ii) src:92 | none: literal |
| THỦ TỤC YÊU CẦU BỒI THƯỜNG | `The claims procedure as performed` | claims procedure | GC 9 src:334 | none: literal |
| ngay lập tức | `measures to minimise the loss were taken immediately`; `written notice was given to the Insurer immediately`; `the police were notified immediately` | immediately | GC 9(a) src:337 | Unquantified in both languages; a judgement on the facts here (fork F17). |
| thực hiện tất cả các biện pháp cần thiết để giảm thiểu tổn thất và thu hồi các tài sản bị mất mát | `take all necessary measures to minimise the loss and recover lost property` | take all necessary steps to minimise the loss and recover lost property | GC 9(a)(i) src:338-339 | none: literal |
| thông báo bằng văn bản cho Bảo Minh | `notify the Insurer in writing` | notify the Insurer in writing | GC 9(a)(ii) src:340 | none: literal |
| thông báo cho công an | `notify the police` | notify the police | GC 9(a)(iii) src:341 | none: literal |
| khiếu nại đòi bồi thường tài sản bị tổn thất hoặc tổn hại | `submit a written claim listing the items and amounts`; `days from awareness to the written claim` | a claim for the property lost or damaged, itemised, with amounts | GC 9(b)(i) src:345-347 | none: literal |
| hoặc lâu hơn tùy theo sự đồng ý bằng văn bản của Bảo Minh | `a longer period agreed in writing by the Insurer, in days` | or longer as the Insurer agrees in writing | GC 9(b) src:343 | none: literal |
| thông tin chi tiết về các hợp đồng bảo hiểm khác | `give particulars of other insurances`; `particulars of other insurances were given` | particulars of other insurances | GC 9(b)(ii) src:348 | none: literal |
| bản cam kế́t hoặc văn bản dưới hình thức pháp lý khác xác nhận tính trung thực của khiếu nại | `the information and documents the Insurer reasonably required were provided, with a declaration of truth` | a declaration of the truth of the claim | GC 9 src:357-358 | The source word is an undertaking (and carries a stray combining mark at src:357); PAR says statutory declaration. |
| man trá | `the claim is fraudulent in some respect` | fraudulent | GC 4(a) src:284 | none: literal |
| thủ đoạn gian lận nhằm trục lợi | `fraudulent means or devices were used to obtain a benefit` | fraudulent means or devices to obtain a benefit | GC 4(a) src:286 | none: literal |
| THẾ QUYỀN ĐÒI BỒI THƯỜNG | `refused an act the Insurer required to enforce its rights against others` | subrogation | GC 5 src:291 | none: literal |
| không tuân thủ các yêu cầu của Bảo Minh | `did not comply with a requirement of the Insurer under General Condition 10` | did not comply with the Insurer's requirements | GC 10 src:377-378 | none: literal |
| cản trở Bảo Minh trong việc thực thi quyền hạn | `hindered the Insurer in exercising its powers under General Condition 10` | obstructed the Insurer | GC 10 src:378 | none: literal |
| các bản vẽ, các tài liệu, phương án kỹ thuật, số lượng máy móc | `did not provide the plans and information required for a reinstatement` | plans, documents, specifications, quantities | GC 11 src:391-392 | none: literal |
| bảo dưỡng tài sản một cách phù hợp | `maintained the property properly` | maintain the property properly | GC 12 src:401 | none: literal |
| mọi biện pháp đề phòng tổn thất | `took every precaution to prevent loss` | every precaution to prevent loss | GC 12 src:402 | "mọi" is every, all: there is no "reasonable" in the operative words, only in the heading "CẨN TRỌNG HỢP LÝ" (Finding 2). |
| sẽ không mua bảo hiểm cho số tiền miễn thường | `insured the deductible elsewhere` | not to insure the deductible | GC 13 src:410-411 | "đoan kết" is to warrant, the English term of art. |
| thanh toán phí bảo hiểm thành nhiều kỳ | `the Insurer accepted payment by instalments` | payment by instalments | GC 15 1(b) src:434 | none: literal |
| ngày chấp nhận bảo hiểm | `date the cover was accepted` | the date the insurance was accepted | GC 15 1(a)(i) src:424; 1(b)(i) src:436 | English PPW clauses say inception date, which may differ from the date of acceptance. |
| thanh toán đầy đủ phí bảo hiểm | `date the premium was paid in full` | payment of the premium in full | GC 15 src:421-422 | none: literal |
| các kỳ thanh toán còn lại sẽ được trả vào đúng ngày thỏa thuận | `agreed date of the first later instalment not paid on time` | the later instalments on their agreed dates | GC 15 1(b) src:437-438 | none: literal |
| Sửa đổi bổ sung | `An endorsement` | endorsement | GC 15 src:421, 426 | none: literal |
| ngày có hiệu lực của phạm vi bảo hiểm | `date the cover in it takes effect` | the effective date of the cover in the endorsement | GC 15 1(a)(ii) src:426 | none: literal |
| ngày cấp | `date it was issued` | the date of issue | GC 15 1(a)(ii)-(iii) src:428-430 | none: literal |
| thời hạn cam kết thanh toán phí | `General Condition 15: the last day to pay the premium` | the premium payment warranty period | GC 15 2 src:446 | none: literal |
| BIỂU PHÍ NGẮN HẠN | `A row of the short-period scale`; `the short-period scale` | short-period scale | GC 3 src:276 | none: literal |
| Thời hạn | `the period, as printed`; `months, from more than`; `months, up to and including` | the period column | GC 3 src:277 | The printed rows overlap at their edges (fork F20). |
| Phí bảo hiểm | `the percentage of the annual premium kept` | the premium column, as a percentage of the annual premium | GC 3 src:277-281 | none: literal |
| trọng tài | `appoint an arbitrator in writing` | arbitrator | GC 7 src:310-318 | none: literal |
