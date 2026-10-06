# GLOSSARY — Manulife CSTD (row `legalese-2026-10-vn-12`)

Every term the document defines, and every type, field or constant the encoding declares that renders a Vietnamese concept.
The Vietnamese column is verbatim from `../../source/raw/manulife-cstd.txt` (checked by `tools/vnsrc.py check`); the English is the identifier the L4 uses.
"Translation risk" says where the Vietnamese has more than one plausible English rendering, or where the English word carries a sense the Vietnamese does not.

## Defined terms and the contract's vocabulary

| Vietnamese term (verbatim) | English identifier in the L4 | English meaning, one line | where defined or used (Điều / clause, src line) | translation risk |
| --- | --- | --- | --- | --- |
| Công Ty | `the Company` | Manulife (Vietnam) Ltd, the insurer | 1.1, src:19 | — |
| Bên Mua Bảo Hiểm | `A policyholder`, `policyholder`, `the Policyholder` | the organisation or individual who applies, signs and holds the contract | 1.2, src:23 | Literally "the buyer of insurance"; "policyholder" adds the sense of the holder of rights, which the definition also gives. Not the insured. |
| tổ chức; cá nhân | `an organisation`; `an individual` | the two kinds of policyholder | 1.2, src:23-24 | — |
| năng lực hành vi dân sự đầy đủ | `of full civil act capacity` | full legal capacity | 1.2, src:26 | A civil-law term; "full legal capacity" is the looser common-law equivalent. |
| Người Được Bảo Hiểm | `The insured`, `insured`, `the insured person` | the person whose life and health are covered | 1.3, src:31 | — |
| mối quan hệ được bảo hiểm; quan hệ bảo hiểm | `an insurable relationship between the policyholder and the insured` | the relationship that lets the policyholder insure this person | 1.3(i), src:40; 2.3.2, src:258 | "Insurable interest" is the common-law term; the Vietnamese speaks of a relationship, and the encoding keeps that. |
| đang hiện diện tại Việt Nam | `the insured present in Vietnam` | physically present in Vietnam at the application | 1.3(ii), src:43 | Presence, not residence. |
| Người Thụ Hưởng | `A beneficiary` | the person or organisation named to receive the death benefit | 1.4, src:46 | — |
| Số Tiền Bảo Hiểm | `sum insured at the date of diagnosis` (and of death, at maturity) | the sum insured on the schedule or endorsement | 1.5, src:51 | "Sum assured" in UK usage; same thing. It can change (7.1, 27, 28.1), so it is taken at each event. |
| Tuổi | `the Tuổi on the anchor day`, `the insured's Tuổi under` | the insured's age at the last birthday before the effective date or the latest anniversary | 1.6, src:62 | **High.** English "age" means current age; the defined Tuổi is fixed for a whole policy year. The identifier keeps the Vietnamese word to mark the defined term. 1.2 uses it for the policyholder (finding X-10). |
| Ngày Cấp Hợp Đồng | `issue date` | the day the Company accepts and issues the contract | 1.7.1, src:67 | "Issue" not "effective": the waiting period and incontestability count from it. |
| Ngày Hiệu Lực Hợp Đồng | `effective date` | the day the contract starts | 1.7.2, src:73 | — |
| Ngày Kỷ Niệm Hợp Đồng | `the policy anniversary` | the yearly date of the effective date; the month's last day where it does not exist | 1.7.3, src:77 | — |
| Năm Hợp Đồng | `the policy year of` | one calendar year from the effective date or an anniversary | 1.7.4, src:82 | "năm dương lịch" is a calendar (solar) year, not 1 January to 31 December. |
| Ngày Đáo Hạn Hợp Đồng | `the maturity date of` | the last day of the term | 1.7.5, src:85 | — |
| Ngày Đến Hạn Đóng Phí | `due date` | the day a premium falls due | 1.7.6, src:88 | — |
| Thời Hạn Hợp Đồng | `the maturity date of` (its end) | the term, to the anniversary at 99 Tuổi | 1.8, src:91 | — |
| Thời Hạn Đóng Phí | `A premium term`, `the end of the premium term of` | to the 12th, 15th or 20th anniversary | 1.9, src:97 | — |
| Phí Bảo Hiểm | `premium paid`, `total premiums paid` | the premium | 1.10, src:110 | — |
| Trang Hợp Đồng (Giấy Chứng Nhận Bảo Hiểm) | (comments: "the policy schedule") | the contract page showing its particulars | 1.11, src:116 | Literally "contract page (insurance certificate)"; "schedule" is the common-law name for it. |
| Xác Nhận Thay Đổi Hợp Đồng | `endorsement issued` | the Company's written confirmation of a change | 1.12, src:119 | Literally "confirmation of contract change"; "endorsement" is the insurance term. |
| Sản Phẩm Bảo Hiểm Bổ Trợ | (comments: "rider") | a supplementary product attached to the main one | 1.13, src:122 | Literally "supplementary insurance product". |
| Nợ | `the debt`, `debt` | every premium or sum owed to the Company, loans included, with interest | 1.14, src:127 | **Medium.** English "debt" is broader; the defined Nợ is a contract account (unpaid premiums, loans, interest), deducted before any benefit. Capitalised as "Debt" in the notes. |
| Giá Trị Tiền Mặt | `cash value`, `1.15 — the cash value on` | the value in the schedule's cash value table | 1.15, src:136 | — |
| Giá Trị Hoàn Lại | `1.16 — the surrender value from` | what the policyholder receives on early termination | 1.16, src:149 | Literally "refund value"; "surrender value" is the term of art. |
| Quyền lợi tiền mặt đặc biệt tích lũy | `accumulated special cash benefit` | an amount added to the surrender value, defined nowhere | 1.16, src:165 | Undefined in the source (finding X-11). |
| Bảo tức tích lũy; lãi tích lũy | `accumulated dividends`; `accumulated interest` | dividends left with the Company, and interest on them | 1.16, src:166; 12.2, src:694-695 | See "Bảo tức". |
| Tai Nạn | `An accident`, `1.17 — an Accident:` | a sudden external event that is the sole direct cause of injury or death within 90 days | 1.17, src:168 | **Medium.** English "accident" is broader; the defined Tai Nạn requires a sole, direct cause and injury within 90 days. |
| Bệnh Lý Nghiêm Trọng | `A listed condition` | a disease, condition or operation listed in Annexes 1-3 | 1.18, src:178 | "Critical illness" is the market term; literally "serious pathology", and it includes operations and procedures. |
| Bệnh Có Sẵn | `1.19 — a pre-existing condition under` | a condition a doctor examined, diagnosed or treated before the issue or reinstatement date | 1.19, src:181 | — |
| Hợp Đồng Bảo Hiểm Giảm | (Article 27 rules) | the reduced paid-up contract | 1.20, src:190 | Literally "reduced insurance contract". |
| Lần Thăm Khám | `the visit` | one medical visit at which tests, diagnosis and prescription are made | 1.21, src:196 | — |
| Quy Trình Nghiệp Vụ | `the funeral cap fixed by the Business Procedures` | the Company's operating rules, changeable at any time by website notice | 1.22, src:200 | Literally "business process"; it binds the contract (X-12). |
| Hồ Sơ Yêu Cầu Bảo Hiểm | `An application` | the application file | 2.2, src:236 | — |
| người chưa thành niên | `the insured a minor` | a minor | 2.3.1, src:251 | Not defined in the source. |
| cha/mẹ hoặc người giám hộ hợp pháp | `a parent or lawful guardian of the insured` | who consents for a minor | 2.3.1, src:249-250 | — |
| bảo hiểm tạm thời | `An answer under Article 3`, `A death during temporary cover` | cover between application and issue | 3, src:276 | — |
| phí bảo hiểm tạm tính | (temporary cover record) | the provisional premium | 3.1, src:302 | — |
| THỜI GIAN CÂN NHẮC | `4 — the policyholder's right to refuse the contract` | the free-look period | 4, src:318 | Literally "consideration period". |
| MIỄN TRUY XÉT | `8 — on … the contract can no longer be voided` | incontestability | 8, src:470 | Literally "exemption from investigation". |
| kê khai sai tuổi và/hoặc giới tính | `7.1 — the adjustment for` | misstatement of age or sex | 7, src:432 | — |
| giới tính | `A sex`, `male`, `female` | sex | 7, src:432; Annex 2, src:3147, 3175 | "nam giới" / "nữ giới" read as male and female. |
| Quyền lợi trợ cấp mai táng | `12.1 — the funeral benefit advanced on` | the funeral benefit, paid in advance of the death benefit | 12.1, src:668 | Literally "funeral allowance benefit". |
| Quyền lợi tử vong | `12.2 — the death benefit on` | the death benefit | 12.2, src:683 | — |
| giai đoạn sớm; giai đoạn giữa; giai đoạn cuối | `the early-stage benefit (13.1)`; `the middle-stage benefit (13.2)`; `the late-stage benefit (13.3)` | the three stages | 13.1-13.3, src:724-725, 766-767, 808-809 | "giữa" is middle; two middle-stage headings say "giai đoạn trung gian" (intermediate stage) instead. |
| Quyền lợi Bệnh Lý Nghiêm Trọng bổ sung | `the additional benefit (13.4)` | the additional 25% for Annexes 2 and 3 | 13.4, src:846 | — |
| cơ quan cặp | `A paired organ` | an organ the body has two of | 13.1(b)(iii), src:761-762 | — |
| tay; chân; vú; tai; mắt; ống dẫn trứng; thận; phổi; buồng trứng; tinh hoàn | `the arms`; `the legs`; `the breasts`; `the ears`; `the eyes`; `the fallopian tubes`; `the kidneys`; `the lungs`; `the ovaries`; `the testes` | the ten paired organs | 13.1(b)(iii), src:762-763 | "tay" covers arm and hand, "chân" leg and foot. |
| Phiếu tiền mặt an nhàn | `13.5 — the comfort cash coupon date of`, `13.5 — the coupon` | a one-off payment at 75 Tuổi or the 20th anniversary | 13.5, src:871 | **Medium.** Literally "cash voucher of ease"; it is a single lump sum, not a recurring coupon. |
| trẻ em | `14 — the percentage of the sum insured at Tuổi` | a child, here under 4 Tuổi | 14, src:892-896 | — |
| Bảo tức | `a dividend`, `15(a) …`, `15(b) …` | a participating-fund dividend, not guaranteed | 15, src:916-923 | **Medium.** English "dividend" suggests a shareholder dividend; this is a policyholder bonus. |
| Bảo tức định kỳ; Bảo tức tri ân | `15(a) — a periodic dividend …`; `15(b) — … a loyalty dividend …` | periodic and loyalty dividends | 15(a)-(b), src:924, 931 | "tri ân" is gratitude; "loyalty" is a gloss. |
| Để lại Công Ty và hưởng lãi; Nhận ngay bằng tiền mặt | `left with the Company at interest`; `paid in cash at once` | payment methods | 16.1, src:971, 980 | — |
| Quyền lợi đáo hạn | `17 — the maturity benefit on` | the maturity benefit | 10.2(e)(i), src:589-590; 17, src:953 | — |
| THỜI GIAN CHỜ; THỜI GIAN CÒN SỐNG | `18(a) — …`; `18(b) — …` | waiting period; survival period | 18, src:1001-1002 | — |
| Tự tử | `19.1(a) suicide within two years`, `suicide, an act of suicide or a self-inflicted injury` | suicide | 19.1(a), src:1027; 19.2(b), src:1052 | — |
| tự ý gây ra tổn thương | (same field) | self-inflicted injury | 19.2(b), src:1052-1053 | — |
| hành vi vi phạm pháp luật hình sự; hành vi vô ý | `A criminal act`, `unintentional` | a criminal act; an unintentional one | 19.1(b), src:1032-1033 | — |
| Người Được Bảo Hiểm 2 | `the second insured` | a second insured, undefined | 19.1(b), src:1033-1034 | Undefined in the source (finding X-9). |
| Nổ hoặc phóng xạ từ vũ khí hạt nhân | `nuclear, chemical or radioactive cause` | nuclear, chemical or radioactive cause | 19.2(c), src:1055 | — |
| gia hạn đóng phí bảo hiểm | `20.2 — the last day of the grace period for a premium due on` | the grace period | 20.2, src:1072 | — |
| THANH TOÁN PHÍ BẢO HIỂM TỰ ĐỘNG | `21 — the outcome of` | automatic premium payment, by a loan from the cash value | 21, src:1083 | Literally "automatic premium payment"; the mechanism is a loan ("tạm ứng"), so "automatic premium loan". |
| mất hiệu lực | `the contract lapses at the end of the grace period` | lapse | 21.2, src:1106; 26.5, src:1207 | Distinct from "chấm dứt" (termination): finding X-6. |
| KHẤU TRỪ; cấn trừ | `22 — the payment of` | deduction; set-off | 22, src:1111, 1120 | — |
| KHÔI PHỤC HIỆU LỰC HỢP ĐỒNG | `23 — under …` | reinstatement | 23, src:1128 | — |
| CHẤM DỨT HỢP ĐỒNG TRƯỚC THỜI HẠN | `25 — the payment on early termination` | early termination, for the surrender value | 25, src:1172-1173 | — |
| TẠM ỨNG TỪ GIÁ TRỊ TIỀN MẶT | `26.1 — a loan …` | a loan from the cash value | 26, src:1182 | Literally "advance". |
| sự kiện bảo hiểm | `29.1 — the last day to claim for an insured event on` | the insured event | 29.1, src:1283 | Undefined for a critical illness (fork F-29b, finding X-2). |
| Thời hiệu khởi kiện | `30.3 — the last day to sue on a dispute arising on` | limitation period for suit | 30.3, src:1349 | — |
| Chức Năng Sinh Hoạt Hàng Ngày | `An activity of daily living` | the six activities of daily living | Annex 1 late, src:2410 | — |
| Tắm rửa; Thay quần áo; Chuyển chỗ; Di chuyển; Vệ sinh; Ăn uống | `washing`; `dressing`; `transferring`; `moving about`; `toileting`; `feeding` | the six activities, (a)-(f) | Annex 1 late, src:2412-2430 | "Di chuyển" is moving about indoors, room to room; "Chuyển chỗ" is bed to chair. |

## Measured quantities and excluded causes (the annex data)

| Vietnamese term (verbatim) | English identifier in the L4 | English meaning, one line | where defined or used (Điều / clause, src line) | translation risk |
| --- | --- | --- | --- | --- |
| Không đáp ứng với kích thích bên ngoài | `hours without response to external stimuli` | duration of coma | Annex 1, src:1485, 2030, 2538 | — |
| Trắc nghiệm trạng thái tâm thần tối thiểu | `MMSE score out of 30` | Mini-Mental State Examination score | Annex 1, src:1457-1458, 1960-1961 | — |
| Hẹp tối thiểu 60% lòng mạch | `number of named coronary arteries narrowed by at least 60%`; `… 75%` | coronary stenosis counts | Annex 1, src:1541, 2097, 2640 | "động mạch vành" lists four named arteries (src:1544-1546). |
| bảng phân loại suy tim của Hiệp hội Tim mạch New York | `NYHA class` | New York Heart Association class | Annex 1, src:1590-1591 | — |
| bỏng độ II; bỏng độ III | `percentage of body surface with second-degree burns`; `… third-degree …` | burn degree and extent | Annex 1, src:1853, 2367, 3067 | — |
| thị lực; thị trường | `visual acuity as a Snellen fraction`; `visual field in degrees` | eyesight measures (6/60 read as 0.1) | Annex 1, src:1836-1838 | — |
| thở máy | `hours of continuous mechanical ventilation` | ventilation | Annex 1, src:2188-2189, 2274 | — |
| Chỉ số mật độ xương | `bone density T-score` | WHO T-score | Annex 1, src:2889 | "nhỏ hơn – 2.5" read as below -2.5 (fork F-CI-2). |
| yếu tố đông máu VIII hoặc IX | `clotting factor VIII or IX as a percentage` | clotting factor level | Annex 3, src:3307-3308 | — |
| Thai chết lưu | `completed weeks of pregnancy at the fetal death` | stillbirth after week 28 | Annex 2 women, src:3235-3236 | — |
| Tử vong sơ sinh | `days from the birth to the death of the child` | neonatal death within 30 days | Annex 2 women, src:3261-3262 | — |
| rượu bia | `alcohol` | an excluded cause | e.g. src:1505 | — |
| thuốc | `medicines or drugs` | an excluded cause | e.g. src:1473, 1505 | **Medium.** "thuốc" is medicine generally; read as drug-induced, beside "chất gây nghiện" (fork F-CI-5). |
| chất gây nghiện | `addictive substances` | an excluded cause | e.g. src:1505-1506 | — |
| độc chất | `toxins` | an excluded cause | src:1473 | — |
| nhiễm HIV | `HIV infection` | an excluded cause | e.g. src:1694 | — |
| tự gây ra thương tật | `a self-inflicted injury` | an excluded cause | src:1906 | — |
| nguyên nhân tâm lý; nguyên nhân tâm thần | `a psychological or psychiatric cause without organic damage` | an excluded cause | src:1482, 2365 | — |
| đái tháo đường; sốt bại liệt | `diabetes`; `poliomyelitis` | excluded causes of neuropathy | src:1516-1517 | — |
| Lupus ban đỏ hệ thống | `systemic lupus erythematosus` | an excluded cause for multiple sclerosis | src:1526 | — |
| sỏi túi mật hoặc viêm túi mật | `gallstones or cholecystitis` | an excluded cause | src:1656-1657 | — |
| hiến thận | `kidney donation` | an excluded cause | src:1672 | — |
| điều trị bằng hormon tăng trưởng | `growth hormone treatment` | an excluded cause | src:3134-3135 | — |
| tai nạn | `an accident or injury` | an excluded cause for brain surgery and stroke | src:2590, 2716 | Lower-case: not the defined Tai Nạn. |

## The 147 listed conditions

Generated from `tools/conditions.py`; the Vietnamese is the heading at the line given.

| Vietnamese term (verbatim) | English identifier in the L4 | English meaning, one line | where defined or used (Điều / clause, src line) | translation risk |
| --- | --- | --- | --- | --- |
| Ung thư biểu mô tại chỗ | `carcinoma in situ` | a listed condition: carcinoma in situ | Annex 1 early, item 1, src:1398 | Item 1 also heads five early cancers, each its own constructor (fork F-CI-1). |
| Ung thư tiền liệt tuyến giai đoạn sớm | `early prostate cancer` | a listed condition: early prostate cancer | Annex 1 early, item 1, src:1415 | — |
| Ung thư tuyến giáp giai đoạn sớm | `early thyroid cancer` | a listed condition: early thyroid cancer | Annex 1 early, item 1, src:1419 | — |
| Ung thư bàng quang giai đoạn sớm | `early bladder cancer` | a listed condition: early bladder cancer | Annex 1 early, item 1, src:1423 | — |
| Ung thư máu dòng lympho mạn tính giai đoạn sớm | `early chronic lymphocytic leukaemia` | a listed condition: early chronic lymphocytic leukaemia | Annex 1 early, item 1, src:1425 | — |
| Ung thư hắc tố giai đoạn sớm | `early melanoma` | a listed condition: early melanoma | Annex 1 early, item 1, src:1430 | — |
| Phẫu thuật cắt bỏ u tuyến yên thông qua đường xuyên xoang bướm hoặc đường mũi | `transsphenoidal or transnasal removal of a pituitary tumour` | a listed condition: transsphenoidal or transnasal removal of a pituitary tumour | Annex 1 early, item 2, src:1435 | — |
| Chẩn đoán bệnh Sa sút trí tuệ bao gồm Bệnh Alzheimer | `diagnosed dementia including Alzheimer's disease` | a listed condition: diagnosed dementia including Alzheimer's disease | Annex 1 early, item 3, src:1454 | — |
| Bệnh Parkinson nhẹ | `mild Parkinson's disease` | a listed condition: mild Parkinson's disease | Annex 1 early, item 4, src:1466 | — |
| Câm bất động (Akinetic Mutism) | `akinetic mutism` | a listed condition: akinetic mutism | Annex 1 early, item 5, src:1474 | "Câm bất động" is literally "mute and immobile"; the English clinical term is used. |
| Hôn mê kéo dài ít nhất 48 giờ | `coma of at least 48 hours` | a listed condition: coma of at least 48 hours | Annex 1 early, item 6, src:1483 | — |
| Bệnh thần kinh ngoại biên | `peripheral neuropathy` | a listed condition: peripheral neuropathy | Annex 1 early, item 7, src:1507 | — |
| Bệnh xơ cứng rải rác giai đoạn sớm | `early multiple sclerosis` | a listed condition: early multiple sclerosis | Annex 1 early, item 8, src:1518 | — |
| Bệnh hoặc tổn thương tủy sống gây rối loạn chức năng của ruột và bàng quang | `spinal cord disease or injury causing bowel and bladder dysfunction` | a listed condition: spinal cord disease or injury causing bowel and bladder dysfunction | Annex 1 early, item 9, src:1527 | — |
| Phương pháp điều trị truyền cơ tim bằng tia Laser | `transmyocardial laser revascularisation` | a listed condition: transmyocardial laser revascularisation | Annex 1 early, item 10, src:1534 | — |
| Bệnh động mạch vành nhẹ | `mild coronary artery disease` | a listed condition: mild coronary artery disease | Annex 1 early, item 11, src:1540 | — |
| Đặt máy điều hòa nhịp tim | `pacemaker insertion` | a listed condition: pacemaker insertion | Annex 1 early, item 12, src:1560 | — |
| Đặt máy khử rung tim | `defibrillator insertion` | a listed condition: defibrillator insertion | Annex 1 early, item 12, src:1566 | — |
| Thủ thuật tạo hình van tim, tách van tim qua da | `percutaneous heart valve repair or valvotomy` | a listed condition: percutaneous heart valve repair or valvotomy | Annex 1 early, item 13, src:1572 | — |
| Thủ thuật thay thế van tim hay chỉnh sửa thiết bị qua da | `percutaneous heart valve replacement or device repair` | a listed condition: percutaneous heart valve replacement or device repair | Annex 1 early, item 13, src:1577 | — |
| Tăng áp lực động mạch phổi giai đoạn sớm | `early pulmonary arterial hypertension` | a listed condition: early pulmonary arterial hypertension | Annex 1 early, item 14, src:1586 | — |
| Phẫu thuật phình động mạch ở não | `cerebral aneurysm surgery` | a listed condition: cerebral aneurysm surgery | Annex 1 early, item 15, src:1618 | — |
| Dẫn lưu não thất | `ventricular drainage` | a listed condition: ventricular drainage | Annex 1 early, item 15, src:1625 | — |
| Phình động mạch chủ lớn không triệu chứng | `large asymptomatic aortic aneurysm` | a listed condition: large asymptomatic aortic aneurysm | Annex 1 early, item 16, src:1630 | — |
| Phẫu thuật cắt bỏ 1 bên phổi | `removal of one lung` | a listed condition: removal of one lung | Annex 1 early, item 17, src:1636 | — |
| Đặt lưới lọc tĩnh mạch chủ | `vena cava filter insertion` | a listed condition: vena cava filter insertion | Annex 1 early, item 17, src:1640 | — |
| Phẫu thuật gan | `liver surgery` | a listed condition: liver surgery | Annex 1 early, item 18, src:1645 | — |
| Phẫu thuật tái cấu trúc đường mật | `biliary tract reconstruction surgery` | a listed condition: biliary tract reconstruction surgery | Annex 1 early, item 19, src:1650 | — |
| Phẫu thuật cắt bỏ một thận | `removal of one kidney` | a listed condition: removal of one kidney | Annex 1 early, item 20, src:1658 | — |
| Tổn thương thận mạn tính | `chronic kidney damage` | a listed condition: chronic kidney damage | Annex 1 early, item 20, src:1673 | — |
| Mất khả năng sống độc lập (giai đoạn sớm) | `loss of independent existence, early stage` | a listed condition: loss of independent existence, early stage | Annex 1 early, item 21, src:1680 | The early stage is loss of all fingers of one hand, which the English "loss of independent existence" does not suggest; the heading is kept because the three stages share it. |
| Viêm màng não nhiễm khuẩn phục hồi hoàn toàn | `bacterial meningitis with full recovery` | a listed condition: bacterial meningitis with full recovery | Annex 1 early, item 22, src:1686 | — |
| HIV mắc phải do bị tấn công hoặc do nghề nghiệp | `HIV infection from an assault or at work` | a listed condition: HIV infection from an assault or at work | Annex 1 early, item 23, src:1695 | — |
| Viêm não do virus phục hồi hoàn toàn | `viral encephalitis with full recovery` | a listed condition: viral encephalitis with full recovery | Annex 1 early, item 24, src:1754 | — |
| Sốt bại liệt (giai đoạn sớm) | `poliomyelitis, early stage` | a listed condition: poliomyelitis, early stage | Annex 1 early, item 25, src:1761 | — |
| Bệnh xơ cứng bì tiến triển giai đoạn sớm | `early progressive scleroderma` | a listed condition: early progressive scleroderma | Annex 1 early, item 26, src:1776 | — |
| Bệnh Lupus ban đỏ hệ thống dạng nhẹ | `mild systemic lupus erythematosus` | a listed condition: mild systemic lupus erythematosus | Annex 1 early, item 27, src:1786 | — |
| Thiếu máu bất sản có khả năng hồi phục | `reversible aplastic anaemia` | a listed condition: reversible aplastic anaemia | Annex 1 early, item 28, src:1809 | — |
| Mù 1 (một) mắt | `blindness of one eye` | a listed condition: blindness of one eye | Annex 1 early, item 29, src:1832 | — |
| Mở khí quản vĩnh viễn (hoặc tạm thời) | `permanent or temporary tracheostomy` | a listed condition: permanent or temporary tracheostomy | Annex 1 early, item 30, src:1841 | "vĩnh viễn (hoặc tạm thời)": permanent or temporary; the definition needs 3 months' continuous need. |
| Bỏng mức độ nhẹ | `minor burns` | a listed condition: minor burns | Annex 1 early, item 31, src:1852 | — |
| Điếc cục bộ | `partial deafness` | a listed condition: partial deafness | Annex 1 early, item 32, src:1856 | — |
| Phẫu thuật huyết khối xoang hang | `cavernous sinus thrombosis surgery` | a listed condition: cavernous sinus thrombosis surgery | Annex 1 early, item 32, src:1862 | — |
| Chấn thương đầu mặt cổ cần phẫu thuật phục hồi | `reconstructive surgery above the neck after an accident` | a listed condition: reconstructive surgery above the neck after an accident | Annex 1 early, item 33, limb 1), src:1866 | — |
| Chấn thương tủy sống cổ do tai nạn | `cervical spinal cord injury from an accident` | a listed condition: cervical spinal cord injury from an accident | Annex 1 early, item 33, limb 2), src:1883 | — |
| Phẫu thuật máu tụ dưới màng cứng | `subdural haematoma surgery` | a listed condition: subdural haematoma surgery | Annex 1 early, item 33, src:1890 | — |
| Ghép ruột non | `small bowel transplant` | a listed condition: small bowel transplant | Annex 1 early, item 34, limb first half of the heading, src:1895 | — |
| Ghép giác mạc | `corneal transplant` | a listed condition: corneal transplant | Annex 1 early, item 34, limb second half of the heading, src:1895 | — |
| Mất khả năng sử dụng của 1 (một) chi | `loss of use of one limb` | a listed condition: loss of use of one limb | Annex 1 early, item 35, src:1901 | — |
| Ung thư biểu mô tại chỗ của các cơ quan cụ thể được điều trị bằng phẫu thuật triệt để | `carcinoma in situ of specified organs treated by radical surgery` | a listed condition: carcinoma in situ of specified organs treated by radical surgery | Annex 1 middle, item 1, src:1920 | — |
| Phẫu thuật mở hộp sọ để cắt bỏ toàn bộ u tuyến yên. | `craniotomy for complete removal of a pituitary tumour` | a listed condition: craniotomy for complete removal of a pituitary tumour | Annex 1 middle, item 2, src:1946 | — |
| Bệnh Alzheimer mức độ trung bình | `moderate Alzheimer's disease` | a listed condition: moderate Alzheimer's disease | Annex 1 middle, item 3, src:1956 | — |
| Bệnh Parkinson trung bình | `moderate Parkinson's disease` | a listed condition: moderate Parkinson's disease | Annex 1 middle, item 4, src:1980 | — |
| Hội chứng khóa trong (Locked in syndrome) | `locked-in syndrome` | a listed condition: locked-in syndrome | Annex 1 middle, item 5, src:1992 | — |
| Động kinh nặng | `severe epilepsy` | a listed condition: severe epilepsy | Annex 1 middle, item 6, src:2004 | — |
| Hôn mê kéo dài ít nhất 72 giờ liên tục | `coma of at least 72 continuous hours` | a listed condition: coma of at least 72 continuous hours | Annex 1 middle, item 6, src:2028 | — |
| Bệnh tế bào thần kinh vận động nhẹ | `mild motor neurone disease` | a listed condition: mild motor neurone disease | Annex 1 middle, item 7, src:2037 | — |
| Bệnh xơ cứng rải rác mức độ nhẹ | `mild multiple sclerosis` | a listed condition: mild multiple sclerosis | Annex 1 middle, item 8, src:2045 | — |
| Loạn dưỡng cơ mức độ trung bình | `moderate muscular dystrophy` | a listed condition: moderate muscular dystrophy | Annex 1 middle, item 9, src:2057 | — |
| Phẫu thuật nội soi tim mạch | `endoscopic coronary surgery` | a listed condition: endoscopic coronary surgery | Annex 1 middle, item 10, src:2075 | "Phẫu thuật nội soi tim mạch" is literally endoscopic cardiovascular surgery; the definition is coronary bypass or atherectomy by endoscope, hence "coronary". |
| Bệnh động mạch vành trung bình | `moderate coronary artery disease` | a listed condition: moderate coronary artery disease | Annex 1 middle, item 11, src:2096 | — |
| Phẫu thuật cắt bỏ màng ngoài tim | `pericardiectomy` | a listed condition: pericardiectomy | Annex 1 middle, item 12, src:2109 | — |
| Phẫu thuật nội soi van tim | `endoscopic heart valve surgery` | a listed condition: endoscopic heart valve surgery | Annex 1 middle, item 13, src:2116 | — |
| Tăng áp lực động mạch phổi thứ phát mức độ nặng | `severe secondary pulmonary hypertension` | a listed condition: severe secondary pulmonary hypertension | Annex 1 middle, item 14, src:2135 | — |
| Phẫu thuật động mạch cảnh | `carotid artery surgery` | a listed condition: carotid artery surgery | Annex 1 middle, item 15, src:2153 | — |
| Phẫu thuật xâm lấn tối thiểu động mạch chủ | `minimally invasive aortic surgery` | a listed condition: minimally invasive aortic surgery | Annex 1 middle, item 16, src:2161 | — |
| Hen suyễn nặng | `severe asthma` | a listed condition: severe asthma | Annex 1 middle, item 17, src:2174 | — |
| Xơ gan | `liver cirrhosis` | a listed condition: liver cirrhosis | Annex 1 middle, item 18, src:2190 | — |
| Bệnh viêm xơ chai đường mật nguyên phát mãn tính | `chronic primary sclerosing cholangitis` | a listed condition: chronic primary sclerosing cholangitis | Annex 1 middle, item 19, src:2198 | — |
| Bệnh thận mạn tính | `chronic kidney disease` | a listed condition: chronic kidney disease | Annex 1 middle, item 20, src:2210 | — |
| Mất khả năng sống độc lập (giai đoạn trung gian) | `loss of independent existence, intermediate stage` | a listed condition: loss of independent existence, intermediate stage | Annex 1 middle, item 21, src:2217 | — |
| Viêm màng não nhiễm khuẩn với di chứng thần kinh có khả năng hồi phục | `bacterial meningitis with reversible neurological deficit` | a listed condition: bacterial meningitis with reversible neurological deficit | Annex 1 middle, item 22, src:2225 | — |
| HIV do cấy ghép cơ quan | `HIV infection from an organ transplant` | a listed condition: HIV infection from an organ transplant | Annex 1 middle, item 23, src:2246 | — |
| Viêm não do virus mức độ nhẹ | `mild viral encephalitis` | a listed condition: mild viral encephalitis | Annex 1 middle, item 24, src:2260 | — |
| Sốt bại liệt (giai đoạn trung gian) | `poliomyelitis, intermediate stage` | a listed condition: poliomyelitis, intermediate stage | Annex 1 middle, item 25, src:2269 | — |
| Bệnh xơ cứng bì tiến triển với hội chứng CREST | `progressive scleroderma with CREST syndrome` | a listed condition: progressive scleroderma with CREST syndrome | Annex 1 middle, item 26, src:2276 | — |
| Bệnh Lupus ban đỏ hệ thống dạng trung bình có kèm viêm thận do Lupus | `moderate systemic lupus erythematosus with lupus nephritis` | a listed condition: moderate systemic lupus erythematosus with lupus nephritis | Annex 1 middle, item 27, src:2300 | — |
| Hội chứng rối loạn sinh tủy hoặc xơ tủy | `myelodysplastic syndrome or myelofibrosis` | a listed condition: myelodysplastic syndrome or myelofibrosis | Annex 1 middle, item 28, src:2328 | — |
| Teo thần kinh thị giác gây khiếm thị | `optic atrophy causing visual impairment` | a listed condition: optic atrophy causing visual impairment | Annex 1 middle, item 29, src:2333 | — |
| Câm do liệt dây thanh | `loss of speech from vocal cord paralysis` | a listed condition: loss of speech from vocal cord paralysis | Annex 1 middle, item 30, src:2355 | — |
| Bỏng khuôn mặt mức độ trung bình | `moderate facial burns` | a listed condition: moderate facial burns | Annex 1 middle, item 31, src:2366 | — |
| Phẫu thuật cấy ghép ốc tai | `cochlear implant surgery` | a listed condition: cochlear implant surgery | Annex 1 middle, item 32, src:2370 | — |
| Chấn thương sọ não cần phẫu thuật mở hộp sọ | `head injury requiring craniotomy` | a listed condition: head injury requiring craniotomy | Annex 1 middle, item 33, src:2375 | — |
| Cấy ghép tủy xương hoặc các cơ quan chính (trong danh sách chờ phẫu thuật) | `bone marrow or major organ transplant waiting list` | a listed condition: bone marrow or major organ transplant waiting list | Annex 1 middle, item 34, src:2386 | The condition is being on the waiting list, not the transplant (contrast L45). |
| Mất khả năng sử dụng của 1 (một) chi cần phải có bộ phận giả | `loss of use of one limb requiring a prosthesis` | a listed condition: loss of use of one limb requiring a prosthesis | Annex 1 middle, item 35, src:2397 | — |
| Ung thư nghiêm trọng | `major cancer` | a listed condition: major cancer | Annex 1 late, item 1, src:2432 | — |
| U não lành tính | `benign brain tumour` | a listed condition: benign brain tumour | Annex 1 late, item 2, src:2475 | — |
| Bệnh Alzheimer / Sa sút trí tuệ trầm trọng | `severe Alzheimer's disease or dementia` | a listed condition: severe Alzheimer's disease or dementia | Annex 1 late, item 3, src:2490 | — |
| Bệnh Parkinson nặng | `severe Parkinson's disease` | a listed condition: severe Parkinson's disease | Annex 1 late, item 4, src:2518 | — |
| Hội chứng Apallic | `apallic syndrome` | a listed condition: apallic syndrome | Annex 1 late, item 5, src:2529 | — |
| Hôn mê kéo dài ít nhất 96 giờ | `coma of at least 96 hours` | a listed condition: coma of at least 96 hours | Annex 1 late, item 6, src:2536 | — |
| Bệnh tế bào thần kinh vận động nặng | `severe motor neurone disease` | a listed condition: severe motor neurone disease | Annex 1 late, item 7, src:2546 | — |
| Bệnh xơ cứng rải rác mức độ nặng | `severe multiple sclerosis` | a listed condition: severe multiple sclerosis | Annex 1 late, item 8, src:2554 | — |
| Loạn dưỡng cơ | `muscular dystrophy` | a listed condition: muscular dystrophy | Annex 1 late, item 9, src:2574 | — |
| Phẫu thuật não | `brain surgery` | a listed condition: brain surgery | Annex 1 late, item 10, src:2582 | — |
| Bệnh xơ cứng cột bên teo cơ | `amyotrophic lateral sclerosis` | a listed condition: amyotrophic lateral sclerosis | Annex 1 late, item 11, src:2591 | — |
| Bệnh nhược cơ (Myasthenia Gravis) | `myasthenia gravis` | a listed condition: myasthenia gravis | Annex 1 late, item 12, src:2599 | — |
| Phẫu thuật nối tắt động mạch vành | `coronary artery bypass surgery` | a listed condition: coronary artery bypass surgery | Annex 1 late, item 13, src:2629 | — |
| Bệnh động mạch vành nghiêm trọng khác | `other serious coronary artery disease` | a listed condition: other serious coronary artery disease | Annex 1 late, item 14, src:2639 | — |
| Bệnh nhồi máu cơ tim được xác định là nghiêm trọng | `serious heart attack` | a listed condition: serious heart attack | Annex 1 late, item 15, src:2647 | — |
| Phẫu thuật thay thế van tim | `heart valve replacement surgery` | a listed condition: heart valve replacement surgery | Annex 1 late, item 16, src:2668 | — |
| Tăng áp lực động mạch phổi nguyên phát mức độ nặng | `severe primary pulmonary arterial hypertension` | a listed condition: severe primary pulmonary arterial hypertension | Annex 1 late, item 17, src:2681 | — |
| Đột quỵ | `stroke` | a listed condition: stroke | Annex 1 late, item 18, src:2700 | — |
| Phẫu thuật động mạch chủ | `aortic surgery` | a listed condition: aortic surgery | Annex 1 late, item 19, src:2739 | — |
| Bệnh cơ tim | `cardiomyopathy` | a listed condition: cardiomyopathy | Annex 1 late, item 20, src:2749 | — |
| Hội chứng Eisenmenger | `Eisenmenger syndrome` | a listed condition: Eisenmenger syndrome | Annex 1 late, item 21, src:2763 | — |
| Bệnh phổi giai đoạn cuối | `end-stage lung disease` | a listed condition: end-stage lung disease | Annex 1 late, item 22, src:2768 | — |
| Bệnh suy gan giai đoạn cuối | `end-stage liver failure` | a listed condition: end-stage liver failure | Annex 1 late, item 23, src:2794 | — |
| Viêm gan siêu vi tối cấp | `fulminant viral hepatitis` | a listed condition: fulminant viral hepatitis | Annex 1 late, item 24, src:2801 | — |
| Bệnh viêm tụy mãn tái phát | `chronic relapsing pancreatitis` | a listed condition: chronic relapsing pancreatitis | Annex 1 late, item 25, src:2812 | — |
| Bệnh Crohn mức độ nặng | `severe Crohn's disease` | a listed condition: severe Crohn's disease | Annex 1 late, item 26, src:2820 | — |
| Suy thận | `kidney failure` | a listed condition: kidney failure | Annex 1 late, item 27, src:2831 | — |
| Bệnh nang tủy thận | `medullary cystic kidney disease` | a listed condition: medullary cystic kidney disease | Annex 1 late, item 28, src:2835 | — |
| Mất khả năng sống độc lập (giai đoạn cuối) | `loss of independent existence, final stage` | a listed condition: loss of independent existence, final stage | Annex 1 late, item 29, src:2853 | — |
| Bệnh viêm cân cơ hoại tử (Necrotising fasciitis) | `necrotising fasciitis` | a listed condition: necrotising fasciitis | Annex 1 late, item 30, src:2861 | — |
| Bệnh viêm đa khớp dạng thấp nặng | `severe rheumatoid arthritis` | a listed condition: severe rheumatoid arthritis | Annex 1 late, item 31, src:2871 | — |
| Loãng xương nặng | `severe osteoporosis` | a listed condition: severe osteoporosis | Annex 1 late, item 32, src:2885 | — |
| Viêm màng não nhiễm khuẩn với di chứng thần kinh vĩnh viễn | `bacterial meningitis with permanent neurological deficit` | a listed condition: bacterial meningitis with permanent neurological deficit | Annex 1 late, item 33, src:2904 | — |
| HIV mắc phải do truyền máu hoặc do nghề nghiệp | `HIV infection from a blood transfusion or at work` | a listed condition: HIV infection from a blood transfusion or at work | Annex 1 late, item 34, src:2915 | — |
| Viêm não do virus mức độ nặng | `severe viral encephalitis` | a listed condition: severe viral encephalitis | Annex 1 late, item 35, src:2975 | — |
| Bệnh sốt bại liệt | `poliomyelitis` | a listed condition: poliomyelitis | Annex 1 late, item 36, src:2983 | — |
| Bệnh xơ cứng bì tiến triển mức độ nặng | `severe progressive scleroderma` | a listed condition: severe progressive scleroderma | Annex 1 late, item 37, src:2990 | — |
| Bệnh Lupus ban đỏ hệ thống dạng nặng có kèm viêm thận do Lupus | `severe systemic lupus erythematosus with lupus nephritis` | a listed condition: severe systemic lupus erythematosus with lupus nephritis | Annex 1 late, item 38, src:3001 | — |
| Thiếu máu bất sản | `aplastic anaemia` | a listed condition: aplastic anaemia | Annex 1 late, item 39, src:3028 | — |
| Mù 2 (hai) mắt | `blindness of both eyes` | a listed condition: blindness of both eyes | Annex 1 late, item 40, src:3038 | — |
| Câm | `loss of speech` | a listed condition: loss of speech | Annex 1 late, item 41, src:3047 | — |
| Bỏng nặng | `major burns` | a listed condition: major burns | Annex 1 late, item 42, src:3066 | — |
| Điếc | `deafness` | a listed condition: deafness | Annex 1 late, item 43, src:3069 | — |
| Chấn thương sọ não nghiêm trọng | `serious head injury` | a listed condition: serious head injury | Annex 1 late, item 44, src:3077 | — |
| Cấy ghép tủy xương hoặc các cơ quan chính | `bone marrow or major organ transplant` | a listed condition: bone marrow or major organ transplant | Annex 1 late, item 45, src:3097 | — |
| Liệt | `paralysis` | a listed condition: paralysis | Annex 1 late, item 46, src:3116 | — |
| Bệnh hiểm nghèo giai đoạn cuối | `terminal illness` | a listed condition: terminal illness | Annex 1 late, item 47, src:3123 | "Bệnh hiểm nghèo" (dangerous illness) is the usual Vietnamese for critical illness at large; here it is a terminal illness expected to cause death within 6 months. |
| Bệnh Creutzfeld – Jacob | `Creutzfeldt-Jakob disease` | a listed condition: Creutzfeldt-Jakob disease | Annex 1 late, item 48, src:3128 | — |
| Bệnh suy tuyến thượng thận mãn tính | `chronic adrenal insufficiency` | a listed condition: chronic adrenal insufficiency | Annex 1 late, item 49, src:3136 | — |
| Ung thư tuyến tiền liệt, ung thư phổi hoặc ung thư gan | `prostate, lung or liver cancer` | a listed condition: prostate, lung or liver cancer | Annex 2 men, item 1, src:3148 | — |
| Ung thư biểu mô tại chỗ của vú, cổ tử cung, tử cung, buồng trứng, ống dẫn trứng hoặc âm đạo | `carcinoma in situ of the breast, cervix, uterus, ovary, fallopian tube or vagina` | a listed condition: carcinoma in situ of the breast, cervix, uterus, ovary, fallopian tube or vagina | Annex 2 women, item 1, src:3180 | — |
| Những biến chứng của thai sản | `complications of pregnancy` | a listed condition: complications of pregnancy | Annex 2 women, item 2, src:3212 | One heading for four limbs (a)-(d), including stillbirth. |
| Dị tật bẩm sinh | `congenital defects` | a listed condition: congenital defects | Annex 2 women, item 3, src:3237 | One heading for six limbs (a)-(f), including neonatal death, which is not a defect. |
| Phẫu thuật phục hồi | `reconstructive surgery` | a listed condition: reconstructive surgery | Annex 2 women, item 4, src:3263 | — |
| Bệnh teo cơ tủy sống type 1 ở trẻ em | `spinal muscular atrophy type 1` | a listed condition: spinal muscular atrophy type 1 | Annex 3, item 1, src:3283 | — |
| Viêm khớp dạng thấp nặng ở trẻ em | `severe juvenile rheumatoid arthritis` | a listed condition: severe juvenile rheumatoid arthritis | Annex 3, item 2, src:3292 | — |
| Hemophilia nặng | `severe haemophilia` | a listed condition: severe haemophilia | Annex 3, item 3, src:3305 | — |
| Bệnh thấp có tổn thương van tim | `rheumatic fever with heart valve damage` | a listed condition: rheumatic fever with heart valve damage | Annex 3, item 4, src:3311 | — |
| Bệnh xương thủy tinh | `osteogenesis imperfecta` | a listed condition: osteogenesis imperfecta | Annex 3, item 5, src:3320 | — |
| Đái tháo đường phụ thuộc insulin | `insulin-dependent diabetes` | a listed condition: insulin-dependent diabetes | Annex 3, item 6, src:3343 | — |
| Bệnh Kawasaki | `Kawasaki disease` | a listed condition: Kawasaki disease | Annex 3, item 7, src:3352 | — |
| Viêm cầu thận với hội chứng thận hư | `glomerulonephritis with nephrotic syndrome` | a listed condition: glomerulonephritis with nephrotic syndrome | Annex 3, item 8, src:3359 | — |
