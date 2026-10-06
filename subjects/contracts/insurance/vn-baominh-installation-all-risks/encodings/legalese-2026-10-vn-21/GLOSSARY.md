# GLOSSARY — Bảo Minh erection all risks rules, row `legalese-2026-10-vn-21`

Vietnamese source, English encoding.
Every Vietnamese term below is copied from `../../source/raw/baominh-ear.txt` and checked verbatim by `tools/vnsrc.py check`.
`src:N` is line N of that file.
The document defines exactly one term (the short name of the insurer, src:5-6) and says in General Condition 2 that the policy's defined words keep their meaning throughout, but it defines no other word; every other row is a term the document uses and the encoding names.
Identifiers are in `bm-ear-nouns.l4` unless another module is named.

| Vietnamese term (verbatim) | English identifier in the L4 | English meaning, one line | where defined or used (Điều / clause, src line) | translation risk |
| --- | --- | --- | --- | --- |
| "Bảo Minh" (defined: "sau đây gọi tắt là") | `Bao Minh` (constructor of `A party to the policy`) | the insurer, by its short name | preamble, src:5-6 (the only definition in the document) | Diacritics dropped in the identifier only; the Vietnamese name is used in comments. |
| "Tổng Công Ty Cổ Phần Bảo Minh" | (comment only) | Bao Minh Insurance Corporation, the issuer | preamble, src:5-6 | "Tổng Công Ty" is a corporation (group parent company), not a "general company". |
| "Người được bảo hiểm" | `the Insured` | the insured named in the schedule | throughout; src:5 | The Law on Insurance Business places the disclosure duty on the purchaser of insurance (Law line 541), a party this document never names; "the Insured" here does both jobs (fork F01). |
| "Phụ lục", "phụ lục kèm theo" | `The schedule` | the attached schedule holding the items, sums, limits, deductibles and dates | src:5, 11, 43, 56, 156; GC2 src:67 | Literally "annex/appendix". Rendered "schedule" for the insurance sense; it is not in the document, so all its figures are inputs. |
| "Giấy yêu cầu bảo hiểm", "giấy yêu cầu bảo hiểm" | (record) `The answers in the questionnaire and the proposal form` | the proposal form | preamble src:6; GC1 src:64 | "Yêu cầu" is "request"; "proposal" carries the common-law offer sense, which the Vietnamese does not stress. |
| "Bản câu hỏi" | (record) `The answers in the questionnaire and the proposal form` | the questionnaire completed to make the proposal | preamble src:6-7; GC1 src:64 | None material. Its questions are not in the document. |
| "bản kê khai khác" | (comment) | the Insured's other declarations, also part of the policy | preamble src:7 | "Kê khai" is "declare/list"; not "warranty". |
| "Đơn bảo hiểm này" | (comment) | this Policy, which GC2 says includes the schedule and later parts | src:8, 10; GC2 src:67-69 | "Đơn" is the policy document; the Law speaks of the insurance contract, a word this document does not use for itself. |
| "phí bảo hiểm" | `the premium stated in the schedule has been paid` | the premium | preamble src:10-11; GC4(b) src:84 | None material. |
| "các Điều khoản, Điều kiện và các Điểm loại" ... "trừ" | (section headings) | the terms, conditions and exclusions | preamble src:11-12 | "Điểm loại trừ" is "point of exclusion"; rendered "exclusion". |
| "CÁC ĐIỂM LOẠI TRỪ CHUNG" | § `General exclusions` | the general exclusions | src:16 | None material. |
| "trực tiếp hay gián tiếp gây nên bởi" | `was caused, directly or indirectly, by one of` (bm-ear-general-exclusions.l4) | caused directly or indirectly by | GE chapeau src:19 | Encoded as "among the recorded causes", with no weighing of causes (fork F17). |
| "Chiến tranh, xâm lược, hành động thù địch của nước ngoài" | `war`, `invasion`, `an act of a foreign enemy` (`A cause of loss`) | war, invasion, act of foreign enemy | GE (a) src:21 | None material. |
| "chiến sự" | `hostilities, whether war is declared or not` | hostilities | GE (a) src:21 | "Chiến sự" is "fighting"; the parenthesis "dù tuyên chiến hay" ... "không tuyên chiến" carries "whether declared or not". |
| "đình công, bãi công" | `strike` | strike | GE (a) src:22-23 | Two words, one concept here; "bãi công" may also mean a walk-out. Placing strikes inside the war exclusion is the source's choice. |
| "bế xưởng" | `lockout` | lockout | GE (a) src:23 | "Close the workshop"; rendered as the labour-law term. |
| "khởi nghiã" | `insurrection` | insurrection | GE (a) src:22 | Misspelt in the source (the usual spelling has the tilde on the i); copied as written. |
| "binh biến", "nổi loạn" | `mutiny`, `rebellion` | mutiny; rebellion | GE (a) src:22 | "Binh biến" is a military uprising, nearer "mutiny" than "military rising". |
| "bạo động của quần chúng" | `civil commotion` | civil commotion | GE (a) src:23 | Literally "violence of the masses". |
| "hành động quân sự hay lực lượng" ... "tiếm quyền" | `military action or usurped power` | military or usurped power | GE (a) src:23-24 | "Lực lượng tiếm quyền" is "usurping force". |
| "tịch biên, tịch thu hay phá huỷ theo lệnh của chính phủ" | `confiscation, commandeering or destruction by order of a government, de jure or de facto, or of any public authority` | confiscation, requisition or destruction by state order | GE (a) src:25-26 | "Tịch biên" is sequestration, "tịch thu" confiscation; "theo lệnh" read as qualifying all three. |
| "Phản ứng hạt nhân, phóng xạ hạt nhân hay nhiễm phóng xạ" | `nuclear reaction`, `nuclear radiation`, `radioactive contamination` | nuclear risks | GE (b) src:28 | None material. |
| "Hành động cố ý hay cố tình sơ xuất" | `a wilful act of the Insured or its representative`, `wilful negligence of the Insured or its representative` | wilful act or wilful negligence | GE (c) src:30 | "Cố tình sơ xuất" (deliberate carelessness) is an oxymoron in English too; it is the source's rendering of "wilful negligence". |
| "đại diện" | `... or its representative` | representative of the Insured | GE (c) src:30; Part II cond 1 src:301 | Undefined (Finding 12): could mean agent, manager, or any employee. |
| "Ngừng công việc dù là toàn bộ hay một phần" | `cessation of work, whole or partial` | cessation of work, total or partial | GE (d) src:32 | "Ngừng" (stop) carries no minimum duration (Finding 13). |
| "Người được bảo hiểm cho là" | `the burden of proof where exclusion (a) is alleged by` (bm-ear-general-exclusions.l4) | where the Insured contends | burden clause src:34 | The clause names the Insured as the party alleging exclusion (a), which inverts the evident purpose (fork F03, Finding 5). |
| "THỜI HẠN BẢO HIỂM" | § `The period of insurance` (bm-ear-period.l4) | the period of insurance | src:40 | None material. |
| "khởi công công trình" | `date the works commenced` | commencement of the works | src:42 | "Khởi công" is ground-breaking/start of construction. |
| "công trình" | `The works` | the works (the project as a whole) | src:42, 44, 238 | Could mean the building, the project or the site; read as the project. |
| "công trường" | `on or near the site` | the site | src:43, 237-238, 256 | None material. |
| "dỡ xong các hạng" ... "mục" | `date unloaded at the site` | unloading completed | src:42-43 | "Dỡ xong" is "finished unloading"; the cover starts after it, not during it (fork F07). |
| "bàn giao công trình" | `date the works were handed over` | handover of the works | src:44 | "Bàn giao" is "hand over"; not necessarily "taking-over certificate". |
| "chạy thử" | `date testing began`, `date its testing began` | testing (test run) | src:44, 46, 54 | One word for "test", "test run" and "commissioning test". |
| "vận hành hay chạy thử" ... "có tải đầu tiên" | `date the first test operation or test loading was completed` | the first test operation or test loading | src:44-45 | "Có tải" (under load) may govern both nouns or only the second. |
| "4 tuần" | `four weeks, in days` (bm-ear-period.l4) = 28 | four weeks | src:45 | None; fork F08 on counting. |
| "hạng mục sử dụng lại" | `second-hand` | second-hand items | src:53 | The source adds "(second-hand items)" in English; "sử dụng lại" is literally "re-used". |
| "kéo dài thời hạn (gia hạn)" | `an extension agreed in advance in writing by Bao Minh, to` | extension of the period | src:56-57 | None material. |
| "ĐIỀU KIỆN CHUNG" | § `General conditions` | the general conditions | src:60 | None material. |
| "điều kiện tiên quyết" | GC1 rules; `GC1: a duty of the Insured was not complied with` | condition precedent | GC1 src:64; GC7 src:138 | "Condition precedent" carries a common-law consequence (no liability at all on breach) that Vietnamese law does not attach to the phrase as such; the encoding applies the words literally (fork F02). |
| "khai báo" ... "trả lời các câu hỏi" | `A reading of the questionnaire limb of General Condition 1` | declaring answers to the questions | GC1 src:63-64 | Whether "đúng" (correctly) reaches the answers decides fork F04. |
| "thay đổi quan trọng" | `GC4(b): notify Bao Minh immediately, by telegram and in writing, of a material change` | material change | GC4(b) src:82, 87 | "Quan trọng" is "important"; "material" adds the insurance-law test of relevance to the risk, which the text does not state. |
| "bằng điện tín và bằng văn" ... "bản" | (duty labels) | by telegram and in writing | GC4(b) src:81-82 | "Điện tín" is a telegram; the encoding does not decide whether e-mail or another channel satisfies it (Finding 14). |
| "Lập tức thông báo ngay" | `GC5(a): notify Bao Minh immediately ...` | notify immediately | GC5(a) src:94 | No number of days. |
| "trong vòng 14 ngày kể từ ngày xảy ra sự cố" | `the days General Condition 5 allows for Bao Minh to receive notice` = 14 | within 14 days from the day of the occurrence | GC5 src:110 | "Ngày" does not say calendar or working days (fork F13). |
| "sự cố" | `An occurrence` | occurrence (incident) | GC5 src:91, 110; Part I src:161; Part II src:310 | "Incident" or "occurrence"; undefined, yet deductibles and limits count by it (Finding 12). |
| "tổn thất" | `A loss under Part I` | loss (including damage) | throughout | Covers both "loss" and "damage"; also used for "liability" losses in GE. |
| "hư hỏng nhỏ" | `minor` | minor damage | GC5 src:114 | Undefined (Finding 12). |
| "giám định viên" | (comment) | surveyor / loss adjuster | GC5(c) src:100 | None material. |
| "một thời gian được xem là hợp lý" | `a reasonable time for inspection, in days` (bm-ear-duties.l4) | a reasonable time | GC5 src:116 | Undefined; an input. |
| "kịp thời chu đáo" | `the item had earlier been damaged and not repaired promptly and properly` | promptly and properly | GC5 src:120 | Two qualities in one phrase; neither defined. |
| "thế quyền" | `GC6: do and permit what Bao Minh requires to enforce rights against third parties` | subrogation | GC6 src:126 | None material. |
| "Trọng tài" | `appoint an arbitrator in writing` | arbitrator (also arbitration) | GC7 src:132-137 | The same word names the person and the process; "Trọng tài viên" (src:144) is the person only. |
| "trách nhiệm được chấp nhận" ... "theo cách khác" | `liability admitted and the amount disputed` | liability being otherwise admitted | GC7 src:131-132 | A calque of the English proviso; "theo cách khác" (in another way) is unidiomatic. |
| "trong" ... "vòng một tháng" | `General Condition 7: the last day to appoint an arbitrator after a written request sent on` | within one month | GC7 src:134-135 | Calendar month assumed (fork F18). |
| "phán quyết" | `date of the arbitral award` | award | GC7 src:138; GC8 src:145 | None material. |
| "khiếu nại gian lận hay khai báo sai" | `a claim under the policy was fraudulent`, `a false declaration was made or used in support of a claim` | fraudulent claim or false declaration | GC8 src:141 | "Khai báo sai" (wrong declaration) does not by itself require dishonesty; read with "gian lận" (fraud). |
| "bị khước từ" | `rejected` | rejected | GC8 src:143 | Whole or partial rejection not distinguished. |
| "tiến hành tố tụng" | `date proceedings were commenced` | commence proceedings | GC8 src:144 | None material. |
| "ba tháng" | `General Condition 8: the last day to commence proceedings after an award made on` | three months | GC8 src:144 | Calendar months assumed (fork F18). |
| "không có trị giá" | `GC8: all benefit is forfeited for fraud or a false declaration` | of no value (forfeited) | GC8 src:146 | "Have no value" rather than the legal term "forfeited". |
| "tỷ lệ của họ" | `Bao Minh's ratable proportion, as determined` | its (rateable) proportion | GC9 src:150 | "Họ" (they) is ambiguous between Bao Minh and the other insurers; the basis of the proportion is not stated (fork F20). |
| "PHẦN I - TỔN THẤT VẬT CHẤT" | § `Part I — material damage` | Part I, material damage | src:153 | "Tổn thất vật chất" is "physical loss"; "material damage" is the trade term. |
| "bất ngờ và không lường trước được" | `sudden and unforeseen` | sudden and unforeseen | Part I src:157 | None material. |
| "với mức độ cần thiết phải sửa chữa hoặc thay thế" | `repair or replacement necessary` | to an extent that repair or replacement is necessary | Part I src:158 | None material. |
| "tùy Bảo Minh lựa chọn" | (comment; fork F16) | at Bao Minh's option | Part I src:160 | None material. |
| "hạng mục" | `An item in Part I of the schedule` | item | Part I src:156; Art 1 src:194 | "Hạng mục" is a line or category of work, not a single object. |
| "hạn mức trách nhiệm bồi thường đó" | `the Part I limit of indemnity for any one occurrence` | "that" limit of indemnity | Part I src:162 | "Đó" (that) has no antecedent (fork F14). |
| "tổng số tiền được bảo hiểm ở phần này" | `the total sum insured under Part I` | total sum insured under Part I | Part I src:163 | None material. |
| "chi phí dọn dẹp hiện trường" | `the sum stated separately for clearance of debris`; `the cost of clearing debris from the site` | clearance of debris | Part I src:168 | "Hiện trường" is "the scene"; rendered as site. |
| "Mức khấu trừ" | `the Part I deductible for each occurrence` | deductible (Part I) | Part I excl 1 src:176 | A different word from Part II's (Finding 12). |
| "tổn thất có tính chất hậu quả" | `the consequential losses claimed` | consequential loss | Part I excl 2 src:178 | None material. |
| "thiết kế sai", "khuyết tật của nguyên vật liệu hay khuôn mẫu", "tay nghề" ... "kém" | `faulty design`, `defective material`, `a defective casting or mould`, `bad workmanship other than a fault in erection` | design, material, casting and workmanship defects | Part I excl 3 src:181-182 | "Khuôn mẫu" is "mould/pattern", nearer the English "casting" only by context. |
| "lỗi trong lắp đặt" | `a fault in erection` | fault in erection | Part I excl 3 src:182 | Scope of the carve-back is fork F22. |
| "Ăn mòn, mài mòn, ô xy hoá, kết tạo vẩy cứng" | `corrosion`, `wear`, `oxidation`, `scaling` | corrosion, wear (abrasion), oxidation, scale formation | Part I excl 4 src:184 | "Mài mòn" is abrasion; "kết tạo vẩy cứng" (hard scale) is incrustation. |
| "hồ sơ, sơ đồ, chứng từ kế toán, hóa đơn, tiền mặt, tem phiếu, văn" ... "bản, chứng thư nợ nần, cổ phiếu, séc" | `files`, `drawings`, `accounts`, `bills`, `currency`, `stamps`, `deeds`, `evidences of debt`, `share certificates`, `cheques` | documents, money and securities | Part I excl 5 src:186-187 | "Sơ đồ" is a diagram; "văn bản" any written document (rendered "deeds"); "hóa đơn" invoices. |
| "bao gói như hòm, thùng, hộp" | `packaging materials such as cases, crates and boxes` | packaging | Part I excl 5 src:187 | The source repeats "vật liệu" twice. |
| "kiểm kê" | `discovered only when an inventory was taken` | inventory | Part I excl 6 src:189 | None material. |
| "Số tiền bảo hiểm" | `sum insured` | sum insured | Art 1 src:193 | None material. |
| "trị giá đầy đủ" | `full value` | full value (at completion of erection) | Art 1 src:194 | Includes freight, duties, taxes, erection costs, by the text. |
| "số tiền lẽ ra phải yêu" ... "cầu bảo hiểm" | `Article 1: the proportion of the loss recoverable on` (bm-ear-part1-material-damage.l4) | the amount that ought to have been insured | Art 1 src:200-201 | Stated only for items 1 and 2 (Finding 8). |
| "Cơ sở giải quyết bồi thường" | § `Article 2 — the basis of settlement` | basis of settlement | Art 2 src:205 | None material. |
| "phần thu hồi", "phần trị giá thu hồi" | `the salvage value` | salvage | Art 2 src:209, 212 | Two phrasings for one concept. |
| "trị giá thực tế" | `the actual value of the item immediately before the occurrence` | actual value | Art 2 src:211 | "Actual" may mean market or depreciated value; not defined. |
| "thực tế phải gánh chịu" | `the costs actually incurred by the Insured` | actually incurred | Art 2 src:214 | Drives Finding 9. |
| "Chi phí sửa chữa tạm thời" | `the cost of temporary repairs` | temporary repairs | Art 2 src:227 | None material. |
| "sửa đổi, bổ sung và/hoặc hoàn thiện thêm" | `the cost of alterations, additions or improvements` | alterations, additions, improvements | Art 2 src:230 | None material. |
| "Mở rộng phạm vi bảo hiểm" | § `Article 3 — extra charges` | extension of cover | Art 3 src:233 | The heading says "extension" but the clause restricts. |
| "làm thêm giờ, làm việc ban đêm, làm việc" ... "trong ngày lễ, cước phí vận chuyển hoả tốc" | `the extra charges for overtime, night work, work on public holidays and express freight` | overtime, night work, holiday work, express freight | Art 3 src:233-234 | None material. |
| "Tài sản xung quanh" | `surrounding property` | surrounding property | Art 4 src:237 | None material. |
| "Chủ Đầu tư", "Chủ" ... "thầu" | `owned by, or in the care, custody or control of, the principal or a contractor` | the principal (owner/investor); the contractor | Art 4 src:238-239; Part II src:280, 288 | "Chủ Đầu tư" is literally "investor-owner"; "principal" is the FIDIC/insurance term. |
| "máy móc và trang thiết bị xây dựng/lắp đặt" | `construction or erection plant, machinery or equipment` | construction/erection plant | Art 4 src:242 | None material. |
| "PHẦN II – TRÁCH NHIỆM ĐỐI VỚI BÊN THỨ BA" | § `Part II — third-party liability` | Part II, third-party liability | src:245 | None material. |
| "bên thứ ba" | (the third party of `A liability under Part II`) | third party | Part II src:251, 253 | Undefined (Finding 12); "Người thứ ba" is used for the same idea in GC6 (src:125). |
| "trách nhiệm pháp lý bồi thường" | `the damages the Insured is legally liable to pay` | legal liability to pay damages | Part II src:248 | None material. |
| "thương tật hay ốm đau bất ngờ" | `bodily injury or illness, fatal or not`; `accidental` | accidental bodily injury or illness | Part II src:251 | "Bất ngờ" is "sudden/unexpected", rendered "accidental"; the English word imports a fortuity test the Vietnamese states only as surprise. |
| "chi phí kiện tụng" | `the claimant's costs of litigation recovered from the Insured` | litigation costs | Part II src:261 | None material. |
| "sự đồng ý bằng văn bản" | `the costs and expenses incurred with Bao Minh's written consent`; `with Bao Minh's written consent` | written consent | Part II src:263, 302-303 | None material. |
| "mức miễn thường" | `the Part II deductible for each occurrence` | deductible / excess (Part II) | Part II excl 1 src:272 | Literally "exemption level"; a different word from Part I's "mức khấu trừ" for what reads as the same device. |
| "người làm thuê hay công nhân" | `injury or illness of an employee or worker ...` | employees or workers | Part II excl 3(a) src:279 | None material. |
| "xe cơ giới được phép lưu hành trên đường công cộng" | `a motor vehicle licensed for use on public roads` | licensed road vehicles | Part II excl 3(c) src:292 | None material. |
| "tàu" ... "thuyền, xà lan hay máy bay" | `a waterborne vessel or barge`, `an aircraft` | vessels, barges, aircraft | Part II excl 3(c) src:292-293 | None material. |
| "thoả thuận nào của Người được bảo hiểm" | `under an agreement of the Insured, and would not have attached without it` | an agreement of the Insured | Part II excl 3(d) src:295 | None material. |
| "sự thừa nhận, một đề xuất, một hứa hẹn thanh toán hay bồi thường" | `make an admission, offer, promise, payment or indemnity` | admission, offer, promise of payment or indemnity | Part II cond 1 src:301-302 | None material. |
| "khiếu nại" | `A claim` | claim | GC8 src:141; Part II src:258, 304 | Also "complaint"; "khiếu tố" (src:34) is closer to a formal complaint or prosecution. |
