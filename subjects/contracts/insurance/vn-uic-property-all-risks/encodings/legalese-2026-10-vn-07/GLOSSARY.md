# GLOSSARY — UIC Property All Risks wording, row `legalese-2026-10-vn-07`

The bilingual key to the encoding.
Every Vietnamese cell is a verbatim run of `../../source/raw/uic-par.txt` (checked by `tools/vnsrc.py check`); "src:N" is line N of that file.
"Defined" marks the three terms the document itself defines; every other row is a type, field, constructor or constant the encoding declares to render a Vietnamese concept, in the order of `uic-par-nouns.l4`.
Where the encoding names a provision rather than a concept (`exclusion A1(a) applies to`), the identifier is not listed: the coverage table in NOTES.md maps those.

## Terms the document defines, and the parties

| Vietnamese term (verbatim) | English identifier in the L4 | English meaning, one line | where defined or used (Điều / clause, src line) | translation risk |
| --- | --- | --- | --- | --- |
| `Công ty Bảo hiểm` (Defined: "Công ty Bảo hiểm Liên hiệp ... gọi tắt là Công ty Bảo hiểm") | `the Insurer` (constructor of `A party`) | UIC, the insurer | opening words, src:3 | Low. The document defines it with a capital "B" and then writes "Công ty bảo hiểm" throughout; read as the same term. |
| `Tổn thất` (Defined) | `the occurrence is a Loss as the wording defines it`; "Loss" in every identifier | accidental, sudden and unforeseen physical loss, destruction or damage | insuring clause, src:17-19 | Medium. The definition adds `không lường trước được` (not foreseeable), which the insuring words at src:9 lack (fork F3). Elsewhere the document uses the lower-case `mất mát hoặc tổn thất`, `thiệt hại hoặc tổn thất` (General Conditions 9-12), not the defined term; read as the same loss. |
| `hành động khủng bố` (Defined, for A3(c) only) | `an act of terrorism` | use or threat of force by a person or group for political, religious, ideological "or similar" ends | Exclusion A3(c), src:134-140 | High. The definition is open: `bao gồm nhưng không bị giới hạn` (including but not limited to), so it fixes no boundary (finding 6). |
| `Người được bảo hiểm` | `the Insured` (constructor of `A party`) | the insured | throughout; never defined | Low. The document never mentions the policyholder, whom the Law on Insurance Business distinguishes from the insured; it treats the Insured as the one who pays. |
| `Hợp đồng bảo hiểm` | "the Policy" in identifiers | the insurance contract | throughout | Low. Rendered "Policy" (the English market term). `Đơn bảo hiểm` (src:148) is used once for the same thing. |
| `Bản tóm tắt Hợp đồng bảo hiểm` | "the Schedule"; the record `The Policy` | the schedule (literally "summary of the insurance contract") | src:11, 25, 28, 218, 263, 276 | Medium. "Summary" suggests a non-binding digest; General Condition 1 (src:276-277) makes it part of the contract. |

## The Schedule and the Policy (`The Policy`, `An item in the Schedule`, `A renewal`, `A termination of the Policy`)

| Vietnamese term (verbatim) | English identifier in the L4 | English meaning, one line | where defined or used (Điều / clause, src line) | translation risk |
| --- | --- | --- | --- | --- |
| `Thời hạn bảo hiểm` | `the first day of the Period of Insurance`, `the last day of the Period of Insurance` | the period of insurance | insuring clause, src:10; never defined | Medium. Capitalised as a defined term but defined only by the Schedule; its first day is not named in the insuring clause (fork F1, finding 11). |
| `12 giờ đêm của ngày cuối cùng` | (the test `AT MOST` the last day) | midnight at the end of the last day | src:10 | Medium. "12 giờ đêm" can be read as the midnight that begins the day; taken as the end (fork F2). |
| `khoản phí đầu tiên` | `the date the first premium was paid` | the first premium | src:8 | Low. Paid `bởi` the Insured, literally (finding 21). |
| `tái tục` | `A renewal`, `the renewals` | renewal for a later period | src:12-13 | Low. |
| `Công ty bảo hiểm đã chấp nhận việc thanh toán thêm đó` | `the Insurer accepted that payment` | the insurer accepted the renewal premium | src:12 | Low. |
| `hạng mục` | `An item in the Schedule`, `the item` | an item (a heading of insured property) | proviso (i), src:25-26; Under-insurance, src:256 | Low. |
| `số tiền bảo hiểm` | `the sum insured for the item` | sum insured | proviso (i), src:25 | Low. |
| `tổng số tiền bảo hiểm của tất cả các hạng mục` | `the total sum insured of all the items of` | total sum insured | proviso (i), src:25-26 | Low. |
| `giới hạn trách nhiệm` | `the limit of liability` | limit of liability | proviso (ii), src:28 | Low. |
| `mức miễn thường` | `the deductible for each loss` | deductible (excess) | src:261-263 | Low. "Miễn thường" is the Vietnamese market term for a deductible. |
| `phí bảo hiểm` | `the premium for the Period of Insurance` | premium | src:12, 293 | Low. |
| `theo yêu cầu bằng văn bản của Người được bảo hiểm` | `terminated at the Insured's written request, with effect from` | termination at the Insured's written request | General Condition 3, src:292-293 | Low. When it takes effect is not said (fork F28). |
| `gửi thông báo trước 30 ngày` | `terminated by the Insurer, by written notice sent on` | termination by the insurer on 30 days' notice | General Condition 3, src:295-296 | Low. "Gửi" (send) anchors the 30 days at sending, not receipt (fork F27). |
| `tỷ lệ phí ngắn hạn theo thông lệ` | `the customary short-period rates ... are not stated in the wording` (a named refusal) | customary short-period rates | General Condition 3, src:293-294 | Medium. "Theo thông lệ" (by custom) points outside the document (finding 14). |

## Causes (`A cause`)

| Vietnamese term (verbatim) | English identifier in the L4 | English meaning, one line | where defined or used (Điều / clause, src line) | translation risk |
| --- | --- | --- | --- | --- |
| `nguyên vật liệu thiết kế sai hỏng hay khiếm khuyết` | `faulty or defective design or materials` | faulty or defective design or materials | A1(a)(i), src:43 | Medium. Literally "faulty or defective design-materials"; whether design faults alone are excluded is unclear. Rendered as both. |
| `tay nghề sai hỏng hoặc khiếm` | `faulty or defective workmanship` | faulty workmanship | A1(a)(i), src:43-44 | Low. |
| `thuộc tính cố hữu` | `inherent vice` | inherent vice | A1(a)(i), src:44 | Low. |
| `khuyết tật ẩn` | `latent defect` | latent defect | A1(a)(i), src:44 | Low. |
| `quá trình xuống cấp dần dần` | `gradual deterioration` | gradual deterioration | A1(a)(i), src:44 | Low. |
| `sự méo mó` / `biến dạng` | `deformation or distortion` | deformation, distortion | A1(a)(i), src:44-45 | Low. |
| `hao mòn` | `wear and tear` | wear and tear | A1(a)(i), src:45 | Low. |
| `sự gián đoạn hoạt động của các hệ thống cung cấp nước` / `khí đốt` / `điện hay nhiên liệu` | `interruption of the water, gas, electricity or fuel supply` | supply interruption | A1(a)(ii), src:47 | Low. |
| `sự hư hỏng của các hệ thống thải chất thải dẫn vào trong hoặc dẫn ra khỏi các Địa điểm được bảo hiểm` | `failure of a system carrying waste into or out of the Insured Premises` | drainage/sewerage failure | A1(a)(ii), src:48-49 | Low. |
| `sụp đổ hoặc nứt các tòa nhà` | `collapse or cracking of buildings` | collapse or cracking of buildings | A1(b)(i), src:55 | Low. |
| `sự ăn mòn` / `rỉ sét` | `corrosion or rust` | corrosion, rust | A1(b)(ii), src:57 | Low. |
| `sự khắc nghiệt hoặc sự thay đổi của nhiệt độ` / `độ ẩm` / `độ khô` | `extremes or changes of temperature, humidity or dryness` | extremes or changes of temperature, humidity, dryness | A1(b)(ii), src:57 | Low. |
| `mục ruỗng ở trạng thái ướt hoặc khô` | `wet or dry rot` | wet or dry rot | A1(b)(ii), src:57-58 | Low. |
| `nấm mốc` | `fungus or mould` | fungus, mould | A1(b)(ii), src:58 | Low. |
| `co ngót` / `bay hơi` / `giảm trọng lượng` | `shrinkage, evaporation or loss of weight` | shrinkage, evaporation, loss of weight | A1(b)(ii), src:58 | Low. |
| `sự thay đổi về màu sắc mùi vị kết cấu hoặc bề mặt` | `change in colour, flavour, texture or finish` | change of colour, flavour, texture, finish | A1(b)(ii), src:58-59 | Low. |
| `hoạt động của ánh sáng` | `action of light` | action of light | A1(b)(ii), src:59 | Medium. Printed without commas, `hoạt động của ánh sáng sâu mọt côn trùng`; split into "light" and "vermin, insects". |
| `sâu mọt côn trùng` | `vermin or insects` | vermin, insects | A1(b)(ii), src:59 | As above. |
| `xây sát hoặc trầy xước` | `scratching or marring` | scratching, marring | A1(b)(ii), src:60 | Low. |
| `trộm cắp` | `theft` | theft | A1(c)(i), src:69 | Low. |
| `các hành động lừa đảo hoặc không trung thực` | `fraudulent or dishonest acts` | fraud or dishonesty | A1(c)(ii), src:72 | Low. Whose acts is not said (anyone's). |
| `tài sản bị biến mất` / `thiếu hụt không rõ nguyên nhân hoặc thiếu hụt phát hiện khi kiểm kê` | `disappearance, unexplained shortage, or shortage found at stocktaking` | disappearance, unexplained or inventory shortage | A1(c)(iii), src:74 | Low. |
| `lưu trữ hay để thông tin sai lạc` | `misfiling or misplacement of information` | misfiling | A1(c)(iii), src:75 | Low. |
| `thiếu hụt trong việc cung ứng hoặc phân phối nguyên vật liệu` | `shortage in the supply or distribution of materials` | supply shortage | A1(c)(iii), src:75-76 | Low. |
| `thiếu hụt do sai sót trong kế toán hoặc trong các công việc thống kê ghi chép` | `shortage due to an error in accounting or record-keeping` | clerical or accounting shortage | A1(c)(iii), src:76 | Low. |
| `nứt` / `gãy` / `sụp đổ hoặc quá nhiệt của nồi hơi` | `cracking, fracture, collapse or overheating of boilers, economisers, vessels or pipes containing liquid or gas` | boiler and vessel failure | A1(c)(iv), src:78-79 | Medium. "Gãy" (fracture) overlaps B5's `đứt gãy` (rupture); the caller chooses which cause describes the event. |
| `rò rỉ ở các mối nối hoặc hư hỏng các mối hàn ở nồi hơi` | `leakage at joints or failure of welds of boilers` | joint leaks, weld failure | A1(c)(iv), src:79-80 | Low. |
| `hỏng hóc về cơ khí hoặc về điện hay trục trặc của máy móc thiết bị` | `mechanical or electrical breakdown or derangement of machinery or equipment` | mechanical or electrical breakdown | A1(c)(v), src:82 | Low. |
| `vỡ` / `tràn` / `tháo ra hoặc rò rỉ nước từ các két nuớc` / `thiết bị hoặc đường ống` | `bursting, overflowing, discharge or leakage of water from tanks, apparatus or pipes` | escape of water | A1(c)(vi), src:84; B1 carve-back, src:206-207 | Low. The source misspells `két nuớc` (sic). |
| `xói lở sông hoặc biển` | `river or sea erosion` | erosion | A1(d)(i), src:97 | Low. |
| `lún` / `sự dịch chuyển hay sạt lở của đất` | `subsidence, ground movement or landslip` | subsidence, ground heave, landslip | A1(d)(ii), src:99 | Low. |
| `hiện tượng lún thông thường của các kết cấu mới` | `normal settlement of new structures` | settlement of new structures | A1(d)(iii), src:101 | Low. |
| `gió` | `wind` | wind | A1(d)(iv), src:103 | Medium. A storm is wind and rain, yet `bão tố` (storm) is a separate word, named in B1's carve-back and absent from A1(d)(iv) (fork F9). |
| `mưa` | `rain` | rain | A1(d)(iv), src:103 | As above. |
| `mưa đá` | `hail` | hail | A1(d)(iv), src:103 | Low. |
| `sương giá` | `frost` | frost | A1(d)(iv), src:103 | Low. |
| `tuyết` | `snow` | snow | A1(d)(iv), src:103 | Low. |
| `lụt lội` / `lụt` | `flood` | flood | A1(d)(iv), src:103; B1 carve-back, src:206 | Low. Two spellings, one constructor. |
| `cát hoặc bụi` | `sand or dust` | sand, dust | A1(d)(iv), src:103 | Low. |
| `đông lạnh` / `đông đặc` / `của nguyên liệu nấu chảy` | `freezing or solidification of molten material` | freezing or solidification of molten material | A1(d)(v), src:107 | Medium. `đông lạnh` (freezing) could stand alone (freezing of anything, burst pipes included); read as qualified by `nguyên liệu nấu chảy`. |
| `thoát ra ngẫu nhiên của nguyên liệu nấu chảy` | `accidental discharge of molten material` | escape of molten material | A1(d)(v), src:107 | Low. |
| `hành động có chủ ý hoặc sự cẩu thả cố ý của Người được bảo hiểm` | `a wilful act or wilful negligence of the Insured or of anyone acting on their behalf` | wilful act or wilful negligence | A2(a), src:111-112 | Low. |
| `sự đình trệ của công việc` | `cessation of work` | cessation of work | A2(b), src:114 | Low. |
| `chậm trễ` | `delay` | delay | A2(b), src:114 | Low. |
| `mất thị trường` | `loss of market` | loss of market | A2(b), src:114 | Low. |
| `bất cứ tổn thất hậu quả hoặc tổn thất gián tiếp nào khác` | `another consequential or indirect loss` | consequential or indirect loss | A2(b), src:114-115 | Low. |
| `chiến tranh` | `war` | war | A3(a), src:120 | Low. |
| `xâm lược` | `invasion` | invasion | A3(a), src:120 | Low. |
| `hành động thù địch nước ngoài` | `act of a foreign enemy` | act of foreign enemy | A3(a), src:120 | Low. |
| `hành động gây hấn hay hoặc các hoạt động có tính chất chiến tranh` | `hostilities or warlike operations, whether war be declared or not` | hostilities | A3(a), src:120-121 | Low. "hay hoặc" (or or) is a slip in the source. |
| `nội chiến` | `civil war` | civil war | A3(a), src:121 | Low. |
| `nổi dậy` | `uprising` | uprising | A3(b), src:123 | Medium. The English model's list (mutiny, popular rising, insurrection, rebellion) does not map one to one onto the Vietnamese; each Vietnamese word has its own constructor. |
| `bạo động dân sự có tính chất hoặc dẫn đến nổi dậy quần chúng` | `civil commotion assuming the proportions of, or leading to, a popular rising` | civil commotion at the scale of a popular rising | A3(b), src:123 | Medium. "Dẫn đến" (leading to) is broader than "amounting to". |
| `binh biến` | `mutiny or military rising` | mutiny, military rising | A3(b), src:123-124 | Low. |
| `khởi nghĩa` | `insurrection` | insurrection | A3(b), src:124 | Low. |
| `nổi loạn` | `riot or rebellion` | riot; rebellion | A3(b), src:124; B1 carve-back, src:203 | **High.** One word for the peril A3(b) excludes and the peril B1's carve-back saves; read as one meaning, the carve-back is idle (fork F7, finding 1). |
| `cách mạng` | `revolution` | revolution | A3(b), src:124 | Low. |
| `hành động quân sự hoặc tiếm quyền` | `military action or usurped power` | military or usurped power | A3(b), src:124 | Low. |
| `hành động nào đã được thực hiện trong việc kiểm soát` / `ngăn chặn` / `đàn áp` | `action taken in controlling, preventing or suppressing an act of terrorism` | counter-terrorism action | A3(c), src:143-145 | Low. |
| `bị tịch thu` / `quốc hữu hóa` / `trưng dụng cho mục đích quân sự` / `trưng thu bởi cơ quan quyền lực được thành lập hợp pháp` | `confiscation, nationalisation, requisition for military purposes or expropriation by a lawfully constituted authority` | dispossession by authority | A3(d)(i), src:155-156 | Medium. `mất quyền sở hữu` is "loss of ownership", narrower than "dispossession" (loss of possession). |
| `sự xâm chiếm bất hợp pháp của bất cứ người nào đối với tòa nhà đó` | `unlawful occupation of a building by any person` | unlawful occupation | A3(d)(ii), src:158-159 | **High.** The limb excludes `mất quyền sở hữu` (loss of ownership) by unlawful occupation; on its words that may never happen, since occupation does not transfer ownership (outside knowledge, unverified). |
| `tài sản bị phá hủy theo lệnh của chính quyền` | `destruction by order of a public authority` | destruction by order | A3(e), src:166 | Low. |
| `nguyên liệu vũ khí hạt nhân` | `nuclear weapons material` | nuclear weapons material | A4(a), src:176 | Low. |
| `phóng xạ ion hóa hay nhiễm xạ từ nhiên liệu hạt nhân hoặc từ chất thải hạt nhân` | `ionising radiation or radioactive contamination from nuclear fuel or nuclear waste` | radioactive contamination | A4(b), src:178 | Low. |
| `cháy` | `fire` | fire | B1 carve-back, src:203 | Low. |
| `sét đánh` | `lightning` | lightning | B1 carve-back, src:203 | Low. |
| `nổ` | `explosion` | explosion | B1 carve-back, src:203 | Low. |
| `máy bay rơi` | `falling aircraft` | aircraft (falling) | B1 carve-back, src:203 | Low. Literally "aircraft falling"; narrower than the market's "aircraft or articles dropped therefrom". |
| `bãi công` | `strike` | strike | B1 carve-back, src:203-204 | Low. |
| `công nhân bế xưởng` | `locked-out workers` | locked-out workers | B1 carve-back, src:204 | Low. |
| `những người tham dự vào các cuộc gây rối lao động` | `persons taking part in labour disturbances` | labour disturbances | B1 carve-back, src:204 | Low. |
| `những người có ác ý` | `malicious persons` | malicious persons | B1 carve-back, src:204-205 | Medium. Overlaps the open definition of terrorism (finding 6). |
| `va chạm với phương tiện lưu thông dùng trên đường bộ` | `impact by a road vehicle` | road vehicle impact | B1 carve-back, src:205 | Low. |
| `va chạm với súc vật` | `impact by an animal` | animal impact | B1 carve-back, src:205 | Low. |
| `động đất` | `earthquake` | earthquake | B1 carve-back, src:205-206 | Low. |
| `bão tố` | `storm` | storm | B1 carve-back, src:206 | Medium. See `gió` (fork F9). |
| `tài sản bị hư hỏng do quá trình xử lý` | `a process the property was undergoing` | damage by processing | B3(f), src:229 | Medium. The English market wording limits this to processes "necessarily involving heat"; the Vietnamese has no such limit. |
| `máy móc hoặc thiết bị trong quá trình lắp đặt di chuyển hoặc định vị lại` | `installation, moving or relocation of machinery or equipment, including dismantling and re-erection` | installation or relocation | B3(g), src:231-232 | Low. |
| `tài sản đang được tu chỉnh` / `sửa chữa` / `kiểm tra` / `lắp đặt hoặc bảo dưỡng` | `work on the property: refurbishing, repair, testing, installation or servicing` | work on the property | B3(h), src:234 | Low. |
| `do việc nổ hay đứt gãy các thiết bị trên` | `explosion or rupture of a boiler, economiser, turbine, or other vessel, machinery or apparatus in which pressure is used` | explosion or rupture of pressure apparatus | B5, src:248-249 | Medium. "Các thiết bị trên" (the above apparatus): the class, or the damaged apparatus itself (fork F11). |
| (no source words: the encoding's own) | `a cause this wording does not name` | any cause not named | all-risks basis, src:9 | — |

## Kinds of property (`A kind of property`)

| Vietnamese term (verbatim) | English identifier in the L4 | English meaning, one line | where defined or used (Điều / clause, src line) | translation risk |
| --- | --- | --- | --- | --- |
| `tiền` / `séc` / `tem` / `trái phiếu` / `thẻ tín dụng` / `chứng khoán dưới mọi hình thức` | `money, cheques, stamps, bonds, credit cards or securities of any description` | money and securities | B1(a), src:187 | Low. |
| `đồ trang sức` / `đá quí` / `kim loại quí` / `vàng bạc` | `jewellery, precious stones, precious metals, gold or silver` | jewellery and precious metals | B1(a), src:187-188 | Low. `vàng bạc` (gold and silver) renders "bullion". |
| `lông thú` | `furs` | furs | B1(a), src:188 | Low. |
| `các đồ vật quí hiếm` / `sách hiếm hoặc các tác phẩm nghệ thuật` | `curiosities, rare books or works of art` | curiosities, rare books, art | B1(a), src:188-189 | Low. |
| `kính cố định` | `fixed glass` | fixed glass | B1(b), src:195 | Low. |
| `đồ thủy tinh` / `đồ sứ` / `đồ làm bằng đất nung` / `đá cẩm thạch hoặc bất kỳ đồ vật nào dễ vỡ hoặc dễ gãy` | `glassware other than fixed glass, china, earthenware, marble, or another fragile or brittle article` | fragile articles | B1(c), src:197-198 | Low. |
| `các hệ thống điện tử` / `máy tính và thiết bị xử lý dữ liệu` | `electronic systems, computers or data processing equipment` | electronics | B1(d), src:200 | Low. |
| `hàng ký gửi hay ủy thác` | `goods held on consignment or in trust` | goods held in trust or on commission | B2, src:209 | Low. |
| `tài liệu` / `bản thảo` / `sổ sách kinh doanh` | `documents, manuscripts or business books` | documents | B2, src:209 | Low. |
| `dữ liệu lưu trữ của hệ thống vi tính` | `data stored in computer systems` | computer records | B2, src:209-210 | Low. |
| `mẫu mã` / `mô hình` / `khuôn mẫu` / `sơ đồ` / `bản thiết kế` | `patterns, models, moulds, plans or designs` | patterns and designs | B2, src:210 | Low. |
| `chất nổ` | `explosives` | explosives | B2, src:210 | Low. |
| `phương tiện có giấy phép lưu thông trên đường bộ` / `xe moóc nhà lưu động` / `toa moóc` / `đầu máy xe lửa hoặc xe lăn` / `tàu thủy` / `máy bay` / `tàu vũ trụ` | `a road-licensed vehicle, caravan, trailer, locomotive, rolling stock, watercraft, aircraft, spacecraft or the like` | vehicles and craft | B3(a), src:213-215 | **High.** `xe lăn` means "wheelchair"; the English model has "rolling stock" here. Rendered "rolling stock" (fork F10); on the words, wheelchairs are excluded property. |
| `đất` / `đường lái xe vào nhà` / `vỉa hè` / `đường xá` / `đường băng` / `đường sắt` / `đê đập` | `land, driveways, pavements, roads, runways, railway lines, dams, reservoirs, canals, rigs, wells, pipelines, tunnels, bridges, docks, piers, jetties, excavations, wharves, mines, or underground or offshore works` | land and civil works | B3(d), src:223-226 | Low. One constructor for the whole limb. |
| `súc vật nuôi` / `mùa màng hoặc cây trồng` | `livestock, crops or trees` | livestock, crops | B3(e), src:227 | Low. |
| `tường rào hoặc cổng` | `fences or gates` | fences, gates | A1(d)(iv), src:104-105 | Low. |
| `nồi hơi` / `các thiết bị tiết kiệm` / `tuốc bin hoặc các loại bình chứa` / `máy móc hoặc thiết bị sử dụng áp lực` | `a boiler, economiser, turbine, or other vessel, machinery or apparatus in which pressure is used, or its contents` | pressure apparatus | B5, src:247-248 | Low. |
| `tòa nhà` | `a building` | building | A1(b)(i), General Condition 8 | Low. |
| `máy móc hoặc thiết bị` | `machinery or equipment` | machinery or equipment | B3(g), src:231 | Low. Read to include electronics and pressure apparatus (fork F34). |

## Circumstances, what happened, alterations, other insurance

| Vietnamese term (verbatim) | English identifier in the L4 | English meaning, one line | where defined or used (Điều / clause, src line) | translation risk |
| --- | --- | --- | --- | --- |
| `tại tòa nhà có kèm theo các hành động vũ lực để xâm nhập hoặc đào thoát ra khỏi tòa nhà đó` | `stolen at a building with force and violence used to enter it or to escape from it` | forcible entry or exit | A1(c)(i), src:69-70 | Low. |
| `trong khi các căn nhà bị bỏ trống hoặc không sử dụng` | `in a building that was empty or not in use` | building unoccupied | A1(c)(vi), src:84-85 | Medium. `căn nhà` is "house, dwelling", where the rest of the document says `tòa nhà` (building); read as any building (fork F35). |
| `động sản để ngoài trời hoặc trong các tòa nhà không được che chắn ở các phía` | `movable property in the open, or in a building not enclosed on all sides` | property in the open | A1(d)(iv), src:103-104 | Low. |
| `xảy ra trước khi mất quyền sở hữu hoặc trong khi tạm thời mất quyền sở hữu` | `lost or damaged before a dispossession, or during one that was temporary` | proviso to A3(d) | A3(d), src:162-163 | Medium. See `mất quyền sở hữu` above. |
| `tài sản đang trong quá trình vận chuyển ngoài phạm vi các khu vực được bảo hiểm` | `in transit outside the Insured Premises named in the Schedule` | in transit | B3(b), src:217 | Low. `khu vực được bảo hiểm` (insured areas) is read as the same place as `Địa điểm được bảo hiểm` (Insured Premises). |
| `tài sản hoặc các kết cấu đang trong quá trình phá dỡ` / `xây dựng hay lắp đặt` | `in the course of demolition, construction or erection, or materials or supplies for that work` | works in progress | B3(c), src:220 | Low. |
| `tài sản đã được bảo hiểm riêng dưới đơn bảo hiểm riêng biệt khác` | `insured separately under another, separate policy` | more specifically insured elsewhere | B3(i), src:240 | **High.** `riêng` (separately) may render "more specifically"; whether this differs from B4's "insured by other policies" decides which of three regimes applies (fork F13, finding 2). |
| `giá trị của tài sản đó tại thời điểm xảy ra tổn thất hay phá hủy` | `lost or destroyed, its value at the time of the Loss being` | value at the time of loss | insuring clause, src:15-16 | Medium. "Giá trị" (value) is undefined: market value or indemnity value (fork F14). |
| `số tiền của thiệt hại` | `damaged, the amount of the damage being` | amount of the damage | insuring clause, src:16 | Medium. Repair cost or loss of value is not said (fork F14). |
| `việc kinh doanh hay sản xuất đang tiến hành bị thay đổi` | `the trade or manufacture carried on was altered` | change of trade | General Condition 8(a), src:365 | Medium. No "increase of risk" qualifier on this limb (fork F21, finding 8). |
| `làm tăng rủi ro mất mát hay tổn thất` | `the use of the building, or other circumstances affecting it, changed so as to increase the risk` | change of use increasing risk | General Condition 8(a), src:365-367 | Low. |
| `bị bỏ trống và tình trạng này kéo dài hơn 30 ngày` | `the building had been unoccupied, for this many days, when the loss happened` | unoccupied more than 30 days | General Condition 8(b), src:369-370 | Low. "Hơn" is strictly more (fork F22). |
| `được di chuyển đến tòa nhà khác hay nơi khác ngoài địa điểm được bảo hiểm` | `the property was removed to a building or place other than the Insured Premises` | removal | General Condition 8(c), src:372-373 | Low. |
| `chuyển giao khỏi Người được bảo hiểm không do di chúc hay do hoạt động của luật pháp` | `the Insured's interest in the property passed to another`, `by will or by operation of law` | passing of interest | General Condition 8(d), src:375-376 | Low. |
| `sự đồng ý của Công ty bảo hiểm thể hiện bằng sửa đổi bổ sung` | `the Insurer's consent was endorsed on the Policy before the loss` | consent by endorsement | General Condition 8, src:361-363 | Low. |
| `được bảo hiểm hoặc đáng lẽ được bảo hiểm bởi các đơn bảo hiểm khác` | `insured by other policies in force at the time of the Loss`; `not insured elsewhere, but it would have been, were it not for this Policy` | insured elsewhere, or would be | B4, src:242-243 | **High.** The sentence is garbled: read literally it excludes the very excess the English model saves (fork F12, finding 2). |
| `số tiền lẽ ra có thể được được bồi thường dưới các đơn bảo hiểm đó` | `what those policies would have paid had this Policy not been in force` | the other policies' hypothetical payment | B4, src:244-245 | Medium. "Được được" (sic) in the source. |
| `một hay các đơn bảo hiểm khác đang có hiệu lực` | (the first constructor of `Other insurance of the property`) | other insurance in force | General Condition 6, src:332 | Low. |
| `phần đóng góp tính theo tỉ lệ` | `General Condition 6 does not say how the rateable proportion is measured` (a named refusal) | rateable proportion | General Condition 6, src:335 | **High.** The basis of the proportion is not stated (fork F20). |

## The Loss and the claim (`The Loss`, `A loss under an item`, `The claim`, `An act`, `A bearer of the burden of proof`)

| Vietnamese term (verbatim) | English identifier in the L4 | English meaning, one line | where defined or used (Điều / clause, src line) | translation risk |
| --- | --- | --- | --- | --- |
| `mỗi vụ tổn thất` | `The Loss` | one occurrence | proviso, src:22; deductible, src:264 | Low. |
| `vật chất` | `physical` | physical | src:9, 16 | Low. |
| `ngẫu nhiên` | `accidental` | accidental | src:9, 16 | Low. |
| `bất ngờ` | `sudden` | sudden | src:9, 16 | Low. |
| `không lường trước được` | `unforeseen` | not foreseeable | src:16-18 | Medium. Only in the definition, not in the insuring words (fork F3, finding 18). |
| `có tổng giá trị lớn hơn số tiền bảo hiểm của chúng` | `the value of all the property under the item at the time of the Loss` | value against sum insured, for average | Under-insurance, src:253-254 | Low. |
| `nhận biết được sự kiện làm phát sinh hoặc có khả năng làm phát sinh khiếu nại` | `the date the Insured became aware of the event` | awareness of a claim-giving event | General Condition 9, src:380-381 | Low. |
| `ngay lập tức` | `... at once` (fields of `The claim`) | immediately | General Condition 9(a), src:383 | Medium. An open standard with no figure (fork F24). |
| `thực hiện các biện pháp để giảm thiểu mất mát hay tổn thất và để thu hồi tài sản bị mất` | `take steps to minimise the loss and recover lost property` | mitigation | General Condition 9(a)(i), src:385-386 | Low. |
| `thông báo bằng văn bản cho Công ty bảo hiểm` | `notify the Insurer in writing` | written notice | General Condition 9(a)(ii), src:392 | Low. |
| `thông báo cho Công an nếu có xảy ra trộm hoặc nghi ngờ là có trộm cắp hoặc có hành động cố ý hoặc ác ý` | `notify the police`; `theft, suspected theft, or a wilful or malicious act was involved` | police report | General Condition 9(a)(iii), src:394-395 | Low. |
| `khiếu nại bằng văn bản` | `deliver the written claim and particulars of other insurances` | written claim | General Condition 9(b)(i), src:400 | Low. |
| `chi tiết về các hợp đồng bảo hiểm khác nếu có` | (same act) | particulars of other insurances | General Condition 9(b)(ii), src:405 | Low. |
| `trong thời gian tiếp theo nếu Công ty bảo hiểm chấp nhận bằng văn bản` | `the date to which the Insurer extended the time in writing` | written extension | General Condition 9(b), src:397-398 | Low. |
| `một bản cam kết hoặc văn bản khác theo mẫu quy định của pháp luật khẳng định tính trung thực của khiếu nại` | `produce the further particulars, documents and declaration of truth` | statutory declaration | General Condition 9, src:412-413 | Low. |
| `gian trá` | `any claim under the Policy was fraudulent, ...` | fraudulent | General Condition 4(a), src:304 | Low. |
| `đã bị từ chối` | `the date the claim was rejected` | rejection | General Condition 4(b), src:309 | Low. |
| `tiến hành kiện tụng` | `the date an action was commenced` | suit | General Condition 4(b), src:309-310 | Low. |
| `Trọng tài đã đưa ra phán quyết` | `the date of the arbitration award` | award | General Condition 4(b), src:311-312 | Low. |
| `đã chuyển cho trọng tài nhưng chưa được phân xử xong` | `the date the dispute was referred to arbitration` | in arbitration | General Condition 12, src:483 | Low. |
| `đang chờ giải quyết` | `General Condition 12: the claim was pending or in arbitration on` | pending | General Condition 12, src:482-483 | Medium. Broader than "subject of a pending action"; read as made and not rejected, or sued on (fork F25). |
| `không tuân thủ những yêu cầu của Công ty bảo hiểm hoặc ngăn cản hay gây khó khăn` | `the Insured, or anyone for them, failed to comply with the Insurer's requirements under General Condition 10, or obstructed it`; `obstruct the Insurer in exercising its powers under General Condition 10` | non-compliance or obstruction | General Condition 10, src:442-444 | Low. |
| `không có quyền từ bỏ bất cứ tài sản nào cho Công ty bảo hiểm` | `General Condition 10: the Insured may abandon property to the Insurer` | no abandonment | General Condition 10, src:447-448 | Low. |
| `thực hiện` / `cùng thực hiện và cho phép thực hiện mọi hành động và công việc` | `do and permit the acts the Insurer reasonably requires to enforce its rights against others` | subrogation assistance | General Condition 5, src:317-318 | Low. |
| `Trọng tài` | `appoint an arbitrator` | arbitrator | General Condition 7, src:341-347 | Low. |
| `toàn quyền chỉ định một Trọng tài duy nhất` | `appoint a sole arbitrator` | sole arbitrator | General Condition 7, src:347 | Low. |
| `Trọng tài trung gian` | (not computed) | umpire | General Condition 7, src:348-350 | Low. |
| `tháng dương lịch` | (two calendar months, `add months`) | calendar month | General Condition 7, src:344, 346 | Low. The document says "dương lịch" (solar calendar) here and plain `tháng` in General Conditions 4 and 12; all read as calendar months (fork F26). |
| `các bản sơ đồ` / `đặc điểm kỹ thuật` / `kích thước` / `số lượng và các chi tiết khác` | `furnish plans, specifications, measurements, quantities and particulars for reinstatement` | reinstatement particulars | General Condition 11, src:466-467 | Low. |
| `duy trì tài sản trong tình trạng được bảo dưỡng thích đáng` | `maintain the property and take all reasonable precautions to prevent Loss` | maintenance and precautions | General Condition 13, src:487-488 | Low. |
| `thu xếp việc bảo hiểm đối với các khoản được quy định là mức miễn thường` | `insure the deductible`; `the Insured insured the deductible elsewhere` | insuring the deductible | deductible undertaking, src:268-269 | Low. |
| `hoàn trả theo yêu cầu một phần phí bảo hiểm` | `demand the refund of premium`; `refund premium in proportion to the unexpired period` | refund on demand | General Condition 3, src:297 | Low. |
| `trách nhiệm chứng minh` / `việc chứng minh` | `A bearer of the burden of proof`, `the Insured bears it` | burden of proof | A3(c), src:148; A3, src:170 | Low. |
