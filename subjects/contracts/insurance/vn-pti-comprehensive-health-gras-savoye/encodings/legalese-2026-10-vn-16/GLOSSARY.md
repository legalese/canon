# GLOSSARY — Vietnamese terms and their English identifiers

Row VN-16, PTI comprehensive health care rules through Gras Savoye (Decision 268/QĐ-PTI-BHCN).
Every Vietnamese term below is copied from the source text (`../../source/raw/pti-gras-savoye.txt`) and checked to occur there verbatim by `tools/vnsrc.py check`.
"src" is the line of that file.
The English identifiers are those of the `.l4` modules (`pti268-*.l4`); "(nouns)" means `pti268-nouns.l4`.

## Part I — the 69 defined terms

| Vietnamese term (verbatim) | English identifier in the L4 | English meaning, one line | where defined or used (Điều / clause, src line) | translation risk |
| --- | --- | --- | --- | --- |
| Bác sỹ | `A doctor`; `counts as a doctor` | a licensed, lawfully practising doctor who is not the insured or a close relative | def 1, src 34 | The source spells it both "bác sỹ" and "bác sĩ"; both mean the same. "Doctor" is the person, not the title. |
| Bệnh đặc biệt | `a special disease`; `A diagnosis` | the listed diseases (cancer, tumours, blood pressure, heart disease, ...) | def 2, src 39 | "Special" is a literal rendering; in English insurance usage the closest term is "specified conditions". "huyết áp" (blood pressure) names no particular disease; rendered "a blood pressure disease". |
| Bệnh mãn tính | none (inert) | a disease with any of five chronic characteristics | def 3, src 47 | "Chronic" carries no special legal sense; the term is never used operatively. |
| Bệnh viện | `counts as a hospital` | a lawful facility recognised as a hospital, not mainly for convalescence, rehabilitation, the elderly, addiction, mental disorder or leprosy | def 4, src 54 | "Hospital" may suggest any inpatient facility in English; the definition is narrower. |
| Biến chứng thai sản | `a complication of pregnancy` | a pregnancy condition needing treatment on a doctor's indication | def 5, src 61 | "thai sản" covers pregnancy and childbirth together; "maternity" or "pregnancy" each loses half. |
| Bộ Hợp đồng bảo hiểm | (convention: contract terms are inputs) | the contract, these rules and the endorsements, read together; special terms replace the rules | def 6, src 64 | "Contract set" is literal; "policy documents" is the usual English. |
| Bộ phận giả | `a prosthesis implanted to sustain life`; `another prosthesis` | any artificial part fitted or implanted to sustain life or a bodily function | def 7, src 73 | "Prosthesis" in English often means a limb only; the definition is wider (implants). |
| Vật tư tiêu hao | `consumables` | materials used once or more to support treatment, not permanently implanted | def 8, src 77 | "Consumables" is the industry term; the exception for absorbable materials is lost in one word. |
| Vật tư thay thế | `replacement materials that sustain life` | medical materials replacing or supporting a body part when implanted | def 9, src 83 | "Replacement" vs "substitute" materials; Benefit 2 qualifies them "nhằm duy trì sự sống" (to sustain life), which the identifier carries. |
| Duy trì sự sống | (inside the identifiers above) | sustaining circulation and breathing | def 10, src 86 | "Life support" in English suggests machines; the definition is functional. |
| Cấy ghép nội tạng | `an organ transplant`; `excluded by definition 11` | transplant of heart, lung, liver, pancreas, kidney or marrow; donor costs not insured | def 11, src 88 | none significant. |
| Chăm sóc thai sản | `maternity` | care for childbirth, miscarriage or abortion on indication, and complications | def 12, src 94 | "Maternity care" vs "pregnancy care"; the definition includes miscarriage and abortion. |
| Chăm sóc trẻ mới sinh | `newborn care` (a head of expense; declined) | hospital care of the baby right after birth while the mother is still in | def 13, src 98 | none; but no benefit grants it (finding X7). |
| Chi phí cấp cứu khẩn cấp bằng taxi | `an emergency taxi` (declined) | a one-way taxi fare to emergency care | def 14, src 102 | none; no benefit grants it (X7). |
| Chi phí nằm viện | (def 15, used in `a stay in hospital`) | room, surgery and other related medical costs during the stay | def 15, src 105 | "Hospitalisation costs" is wider in English than room charges. |
| Chi phí Phòng bệnh hay Buồng bệnh | `room and board`; `the room and board allowed under` | the room charge, within the contract's limit per day | def 16, src 113 | "Room and board" adds "board" (meals), which the Vietnamese does not name. |
| Chi phí y tế hợp lệ | `on the indication of a doctor` | reasonable medical costs on a doctor's indication | def 17, src 118 | "Hợp lệ" is "valid/eligible", not "lawful". |
| Chi phí y tế thực tế | (same) | reasonable and necessary actual medical costs | def 18, src 121 | "Actual" vs "incurred". |
| Chủ hợp đồng bảo hiểm | `the policyholder` | the organisation that signs the contract with PTI | def 19, src 125 | English "policyholder" can mean the insured person; here it is the employer. |
| Công ty bảo hiểm | `PTI` | PTI and its member companies | def 20, src 128 | none. |
| Cơ sở y tế | `counts as a medical facility` | a lawful facility licensed for inpatient or outpatient treatment, not a rest home, elderly home or addiction centre | def 21, src 130 | "Medical facility" vs "clinic"; wider than "hospital" (def 4). |
| Dịch vụ xe cứu thương | `an ambulance` (declined) | use of an ambulance or the 115 service in a critical condition | def 22, src 135 | none; no benefit grants it (X7). |
| Dị tật bẩm sinh | (circumstance under IV.A.27) | abnormal development from the womb, in a doctor's opinion | def 23, src 141 | "Congenital defect"; the Vietnamese "dị tật" includes deformity. |
| Điều trị ngoại trú | `outpatient treatment`; `counts as outpatient treatment` | treatment at a facility without admission, not inpatient, not day treatment | def 24, src 145 | none. |
| Điều trị nội trú | `inpatient treatment`; `counts as inpatient treatment` | treatment with admission formalities and an overnight stay | def 25, src 149 | English "inpatient" does not require an overnight stay; this definition does. |
| Điều trị sau khi xuất viện | `treatment in the 45 days after discharge`; `within the 45 days after discharge` | treatment within 45 days after discharge, directly related to the stay | def 26, src 157 | "Post-hospitalisation". |
| Điều trị trong ngày | `day treatment`; `counts as day treatment` | admitted and treated on a bed, without staying overnight | def 27, src 162 | "Day treatment" vs "day case". |
| Điều trị trước khi nhập viện | `tests in the 30 days before admission`; `within the 30 days before admission` | tests in the 30 days before, or on the day of, admission | def 28, src 166 | The Vietnamese names "costs", the English names tests; the definition lists only tests and imaging. |
| Điều trị y tế | (shape: `on a doctor's indication`) | surgery or treatment on a doctor's indication, solely to cure or relieve | def 29, src 171 | none. |
| Đơn bảo hiểm nhóm | `a group policy for a number of persons` | a policy for ten or more people working at one organisation | def 30, src 174 | "Đơn" is "policy" (the document); never used operatively. |
| Khám sức khỏe định kỳ | `a periodic health check, or a check before travel or work` | tests and imaging without symptoms, for early detection | def 31, src 178 | "Periodic" vs "routine". |
| Lần khám/điều trị trong Điều trị ngoại trú do bệnh | `the visits counted for` | one visit to one specialty; a follow-up counts as a new visit | def 32, src 182 | "Visit" vs "consultation". |
| Mạng lưới thanh toán trực tiếp | `in the direct billing network`; `through the direct billing network` | PTI's or Gras Savoye Willis's direct billing facilities | def 33, src 188 | "Direct billing" vs "cashless network"; "bảo lãnh" (guarantee) is the act. |
| Mất tích | `What is known of the last news`; `the earliest day a court may declare the person missing, given`; `disappearance` | a court's declaration after two years without reliable news | def 34, src 194 | English "missing" is everyday; the Vietnamese defined term is a court status (Civil Code). |
| Nằm viện | `counts as a hospital stay` | inpatient treatment over 24 continuous hours, and day treatment | def 35, src 205 | "Hospital stay"; the "và" (and) is read as union (fork F6). |
| Ngày bắt đầu bảo hiểm | `the start date under definition 36 alone for` | the first day of each period of cover | def 36, src 208 | "Start date" vs "inception date"; conflicts with def 38 (finding X1). |
| Ngày tái tục bảo hiểm | (renewal date in III.13 test) | the effective date of the next year's contract | def 37, src 210 | none. |
| Ngày tham gia bảo hiểm | `date first insured with PTI`; `the start date for` | the day the insured first joined a contract | def 38, src 212 | "Joining date" vs "entry date". |
| Người được bảo hiểm | `An insured person`; `named as an insured person` | a person PTI accepted and named in the list | def 39, src 217 | none. |
| Người phụ thuộc | `counts as a dependant`; `a spouse`; `a child` | a spouse under 65, or a child from 12 months to 18 (24 if studying, unmarried) | def 40, src 219 | "Dependant" in English implies financial dependence; here it is a family relation with age limits. |
| Nhân viên | `an employee`; `counts as an employee` | a member of an organisation under a labour or probation contract | def 41, src 226 | "Employee" vs "staff member". |
| Ốm đau, bệnh tật | `an illness` | an abnormal condition of one or more organs, with symptoms | def 42, src 229 | "Sickness, disease"; the pair is a set phrase. |
| Phạm vi lãnh thổ | `within the territory` | Vietnam, unless the contract says otherwise | def 43, src 232 | none. |
| Phẫu thuật | `surgery` | a scientific method of treating injury or illness by operation | def 44, src 236 | none. |
| Phẫu thuật trong ngày | (surgery head, day setting) | surgery not requiring an overnight stay | def 45, src 244 | "Day surgery". |
| Phòng chăm sóc đặc biệt | none (inert) | ICU, HDU, CCU | def 46, src 247 | "Special care room"; never used operatively. |
| Quyền lợi bảo hiểm | `A benefit` | the benefits of the rules, as extended or limited by the contract | def 47, src 253 | "Benefit" vs "cover". |
| Tai nạn | `meets the definition of accident`; `counts as an accident under` | a sudden, unforeseen event outside the insured's control, by a visible external force | def 48, src 256 | English "accident" is broader; the visible external force is a narrowing condition. |
| Thương tật toàn bộ vĩnh viễn do ốm đau bệnh tật | `counts as total permanent injury` | a listed total injury, or a complete change lasting 52 weeks | def 49, src 261 | "Thương tật" is injury, used here for illness too; "disability" would be the natural English. |
| Thời gian chờ | `a waiting period bars` | a time from the start during which a benefit is not paid | def 50, src 268 | none. |
| Thời hạn bảo hiểm | `last day of the period of cover` | the period stated in the contract, usually 12 months | def 51, src 274 | "Period of insurance" vs "term". |
| Thuốc kê đơn của bác sỹ | `the vitamins payable on` | medicine on a doctor's prescription; vitamins capped | def 52, src 278 | none. |
| Thương tật bộ phận vĩnh viễn | `partial permanent injury` | loss, or total loss of function, of part of the body | def 53, src 289 | "Partial permanent disability" is the usual English. |
| Thương tật tạm thời | none (inert) | an accidental injury preventing work during treatment | def 54, src 292 | "Temporary disability"; never used operatively. |
| Thương tật thân thể | (the event's facts) | a physical injury caused by accident, as its first result | def 55, src 295 | "Bodily injury". |
| Thương tật toàn bộ vĩnh viễn | `total permanent injury`; `counts as total permanent injury` | total loss of ability to work, 52 continuous weeks, no hope of improvement | def 56, src 301 | "Total permanent disability" (TPD) is the usual English. |
| Tổn thương thân thể | (the event's facts) | harm in the period caused solely by accident | def 57, src 305 | "Bodily harm"; close to def 55. |
| Tình trạng có sẵn | `a pre-existing condition, judged at` | a condition existing before the start date, treated in the last 3 years or known | def 58, src 308 | "Pre-existing condition"; "có sẵn" is literally "already there". |
| Tình trạng nguy kịch | `in a critical condition` | a condition needing emergency treatment to avoid death | def 59, src 315 | none. |
| Giới hạn chi tiết | (schedule input) | the maximum per item within a benefit | def 60, src 317 | "Sub-limit". |
| Hoạt động thể thao chuyên nghiệp | `a professional sport` | sport that is the insured's main and regular income | def 61, src 320 | English "professional" suggests status; the test here is income. |
| Hoạt động thể thao nguy hiểm | `a dangerous sport` | the listed hazardous activities | def 62, src 323 | "Hazardous sports"; the carve-outs are part of the term. |
| Trợ cấp hàng ngày | `daily allowance`; `the amount Benefit 5 pays in` | a daily cash allowance beyond medical costs | defs 63-64, src 332, 336 | "Trợ cấp lương" (salary allowance) in Benefit 5's heading; "allowance" vs "hospital cash". |
| Trợ cấp mai táng | `the funeral allowance under definition 65` | the funeral allowance written in the contract | def 65, src 339 | "Funeral" vs "burial" allowance. |
| Trường hợp khẩn cấp | (Annex facts) | an emergency needing immediate care | def 66, src 342 | none. |
| Vận chuyển cấp cứu | `emergency medical transport to the nearest suitable hospital` | transport by ambulance in a critical condition | def 67, src 346 | "Emergency evacuation" in assistance usage. |
| Vật lý trị liệu | `radiation, heat or light therapy` (Benefit 6.3) | physical methods to relieve pain and restore function | def 68, src 349 | "Physiotherapy"; Benefit 6.3 names related therapies separately. |
| Y tá chăm sóc tại nhà | `a home care nurse`; `the home nursing days payable after` | a licensed nurse's care at home after discharge, at most 15 days a year | def 69, src 353 | none; no benefit grants the money (X7). |

## Types, constructors and fields that render other Vietnamese concepts

| Vietnamese term (verbatim) | English identifier in the L4 | English meaning, one line | where defined or used (Điều / clause, src line) | translation risk |
| --- | --- | --- | --- | --- |
| Hợp đồng bảo hiểm | `The contract` (nouns) | the insurance contract and its schedule | I chapeau, src 30 | "Contract" vs "policy"; the rules call the document "Đơn bảo hiểm" too. |
| Sửa đổi bổ sung | (inputs; III.2, III.3) | an endorsement | I chapeau, src 30 | "Amendment" vs "endorsement"; the latter is the insurance term. |
| Giấy chứng nhận bảo hiểm | (inputs) | the certificate of insurance | I chapeau, src 30 | none. |
| Bảng tóm tắt quyền lợi bảo hiểm | (schedule input) | the summary of benefits | def 50, src 271 | "Schedule of benefits". |
| Số tiền bảo hiểm | `sum insured under Benefit 1`, `sum insured under Benefit 3` | the sum insured | II, src 369 | "Sum insured" vs "limit"; Benefits 2, 4 and 6 speak of a "giới hạn" (limit). |
| Các quyền lợi chính | `Benefit 1` to `Benefit 4` | the main benefits | II.A, src 366 | none. |
| Các quyền lợi lựa chọn | `Benefit 5` to `Benefit 7` | the optional benefits | II.B, src 408 | "Optional" vs "elective". |
| Tử vong hoặc thương tật vĩnh viễn do tai nạn | `Benefit 1` | death or permanent injury from an accident | Benefit 1, src 367 | none. |
| Chi phí y tế do tai nạn | `Benefit 2` | medical expenses from an accident | Benefit 2, src 372; III.13, src 574 | III.13 attaches this description to the number 3 (X8). |
| Tử vong, tàn tật vĩnh viễn do ốm đau, bệnh tật, thai sản | `Benefit 3` | death or permanent disability from illness or maternity | Benefit 3, src 381 | "tàn tật" (disability) here, "thương tật" (injury) elsewhere. |
| Chi phí nằm viện và phẫu thuật do ốm đau, bệnh tật, thai sản | `Benefit 4` | hospital and surgery costs from illness or maternity | Benefit 4, src 390 | none. |
| Trợ cấp ngày | `Benefit 5` | daily allowance | Benefit 5, src 409 | "(trợ cấp lương)" is a salary allowance; the identifier keeps "daily allowance". |
| Điều trị ngoại trú do ốm đau, bệnh tật | `Benefit 6` | outpatient treatment of illness | Benefit 6, src 429 | none. |
| Vận chuyển y tế cấp cứu trong lãnh thổ Việt Nam | `Benefit 7`; the Annex module | emergency medical transport in Vietnam | Benefit 7, src 442; Annex, src 1232 | none. |
| thủ thuật điều trị | `a therapeutic procedure` | a treatment procedure, paid within 50% of the surgery limit | Benefit 4, src 401 | "Procedure" vs "minor surgery". |
| thủ thuật chẩn đoán | `a diagnostic procedure` | a diagnostic procedure (gastroscopy, biopsy), not a surgery cost | Benefit 4, src 399 | none. |
| bọc mão sứ | `dental crowns or false teeth of ordinary material` | porcelain crowns | Benefit 2, src 376 | "Mão sứ" is a porcelain crown. |
| trồng răng giả | (same) | fitting false teeth | Benefit 2, src 376 | none. |
| Lương tháng đã thông báo | `the notified monthly salary`; `monthly salary notified` | the declared monthly salary | Benefit 5, src 424 | "Notified" vs "declared". |
| Trợ cấp cố định theo ngày | `a fixed daily allowance` | a fixed daily allowance written in the contract | Benefit 5, src 426 | none. |
| Đối tượng bảo hiểm | `A role`; `insurable under III.1` | who may be insured | III.1, src 456 | In the Law, "đối tượng bảo hiểm" means the subject-matter insured (health); here it means eligible persons. |
| Phí bảo hiểm ngắn hạn | `the short-period rate for a term in months of` | short-period premium | III.7, src 515 | none. |
| Đảm bảo tái tục hợp đồng | `renewed under III.3` | guaranteed renewal | III.3, src 479 | "Guaranteed" overstates: the premium may change at PTI's discretion (X20). |
| Hủy toàn bộ hợp đồng bảo hiểm | `A cancelling party`; `the refund when` | cancelling the whole contract | III.4, src 489 | none. |
| Chấm dứt quyền lợi bảo hiểm | `the day cover ends under` | termination of benefits | III.6, src 505 | none. |
| Hiệu lực hợp đồng và thời gian chờ | `a waiting period bars` | effect of the contract and waiting periods | III.8, src 523 | none. |
| Tiền tệ & Tỉ giá | `in VND` | currency and rate of exchange | III.9, src 546 | none. |
| Khiếu nại bồi thường gian lận | `fraud bars` | fraudulent claims | III.10, src 554 | none. |
| Đồng bảo hiểm | `what III.11 leaves PTI to pay of` | other insurance (literally "co-insurance") | III.11, src 561 | "Đồng bảo hiểm" is literally co-insurance, which in English means a shared risk or a co-payment; the clause is about other insurance (contribution). |
| Trường hợp đặc biệt | `the special cases clause bars` | special cases (hazardous activities) | III.12, src 566 | none. |
| Thay đổi quyền lợi | `a change to the limit of` | changes of benefits | III.13, src 573 | none. |
| Tranh chấp | `A forum`; `the forum for a dispute, if` | disputes | III.14, src 578 | none. |
| NHỮNG ĐIỂM LOẠI TRỪ | `A general exclusion`; `the general exclusions engaged by` | the exclusions | IV, src 587 | none. |
| người thừa kế hợp pháp | `an intentional act of the insured's lawful heir` | the lawful heir | IV.A.1, src 592 | none. |
| năm bảo hiểm đầu tiên | `the second exclusion 32 is engaged by` | the first policy year | IV.A second 32, src 674 | From first joining (fork F1), not each year. |
| Người thân trong gia đình | (role `a spouse`, `a child`) | family members | IV.A second 32, src 678 | none. |
| BẢNG TỈ LỆ THƯƠNG TẬT | `the table of injury rates`; `A row of the table` | the table of injury rates | V, src 686 | "Thương tật" (injury) vs "disability". |
| NGUYÊN TẮC XÉT TRẢ TIỀN BẢO HIỂM | `the rate for`; `the total rate for`; `the amount under the table on` | the principles for paying under the table | V, src 858 | none. |
| ĐIỀU KHOẢN MỞ RỘNG | `An extension clause` | extension clauses | VI, src 888 | none. |
| ĐIỀU KHOẢN CAM KẾT THANH TOÁN PHÍ | `the premium payment warranty` | premium payment warranty | VI.2, src 911 | "Cam kết" is "undertaking"; "warranty" is the London-market term this clause translates. |
| ĐÔNG Y | `the traditional medicine extension`; `traditional medicine` | traditional (Sino-Vietnamese) medicine | VI.3, src 926 | "Traditional medicine" loses "Đông" (Eastern). |
| NGỘ ĐỘC THỰC PHẨM HOẶC ĐỒ UỐNG | `the food or drink poisoning extension` | food or drink poisoning | VI.4, src 937 | none. |
| ĐÌNH CÔNG, NỔI LOẠN VÀ BẠO ĐỘNG DÂN SỰ | `the strike, riot and civil commotion extension` | strikes, riots and civil commotion | VI.5, src 941 | none. |
| NGHẸT THỞ DO KHÓI, HƠI ĐỘC, KHÍ GAS VÀ NGẠT NƯỚC | `the suffocation and drowning extension` | suffocation by smoke, fumes, gas, and drowning | VI.6, src 956 | none. |
| ĐIỀU KHOẢN CƯỚP | `the hijacking extension` | hijacking ("cướp" is robbery/seizure) | VI.7, src 961 | "Cướp" alone is "robbery"; the clause is about seizure of a carrier. |
| BỆNH NGHỀ NGHIỆP | `the occupational disease extension`; `An occupational disease` | occupational disease | VI.8, src 968 | none. |
| CHUYẾN ĐI NGOÀI LỊCH TRÌNH | `the unscheduled flights extension` | unscheduled trips (by air) | VI.9, src 998 | The heading says "trips"; the clause speaks of flights. |
| SÁT HẠI VÀ TẤN CÔNG VÔ CỚ | `the murder and assault extension` | murder and unprovoked assault | VI.10, src 1002 | none. |
| KHÁM THAI ĐỊNH KỲ | `the routine prenatal check extension`; `a routine prenatal check` | routine prenatal checks | VI.12, src 1014; IV.A.16, src 636 | none. |
| THỦ TỤC YÊU CẦU BỒI THƯỜNG | the claims module | claims procedure | VII, src 1025 | none. |
| Thời hạn nộp hồ sơ yêu cầu bồi thường | `the day the claim file is due in` | the time limit for the claim file | VII, src 1072 | none. |
| bất khả kháng | `force majeure` | force majeure | VII, src 1081 | none. |
| Hồ sơ bồi thường | `A claim document`; `the documents Part VII asks for in` | the claim file and its documents | VII, src 1094 | none. |
| ngày làm việc | `a working day`; `the working day` | working days | VII, src 1092 | The document does not say which days are working days (fork F46). |
| hóa đơn VAT | `with a VAT invoice`; `lacks the VAT invoice it needs` | a VAT (financial) invoice | VII, src 1144 | none. |
| thẻ bảo hiểm PTI Care | (direct billing) | the PTI Care card | VII, src 1046 | none. |
| Nơi cư trú | `consecutive days away from the declared residence` | the declared city or province of residence | Annex I, src 1239 | "Residence" vs "domicile". |
| Công ty cứu trợ | `the assistance company` | the assistance company | Annex II, src 1245 | "Cứu trợ" is "relief/rescue"; "assistance" is the industry word. |
| Mức A | `Level A` | level A of transport cover | Annex VI, src 1340 | none. |
| Mức B | `Level B` | level B of transport cover | Annex VI, src 1341 | none. |
