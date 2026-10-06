# GLOSSARY — row VN-14 (Manulife group universal-linked, flexible premium)

One row for every term the document defines (Article 1, and terms defined where they are used), and for every type, field or constant declared in `vn14-nouns.l4` that renders a Vietnamese concept.
The first column is verbatim from `../../source/raw/manulife-group-linked.txt` (checked by `tools/vnsrc.py check`); `src:N` is line N of that file.
Identifiers in backticks are the L4 names; a capitalised English term without backticks is the gloss used in comments and rule names.

| Vietnamese term (verbatim) | English identifier in the L4 | English meaning, one line | where defined or used (Điều / clause, src line) | translation risk |
| --- | --- | --- | --- | --- |
| Công Ty | `the Company` | Manulife (Vietnam) Ltd, the life insurer | Điều 1.1, src:22 | low |
| Bên Mua Bảo Hiểm | `the Policyholder`; `The Policyholder's particulars` | the organisation that applies, signs and holds the group contract | Điều 1.2, src:25 | "policyholder" in English suggests the person insured; here it is the employer or other organisation, never the member. Every right the document gives the Policyholder is the employer's |
| Danh Sách Người Được Bảo Hiểm | `the List of Insured Members` | the Policyholder's signed list of the persons covered | Điều 1.3, src:32 | low |
| Người Được Bảo Hiểm | `the Insured Member` | a person whose life is the subject of the cover | Điều 1.4, src:37 | literally "the insured person"; "member" is added to mark the group role and does not imply membership of a scheme the document defines |
| Đơn Đăng Ký Người Được Bảo Hiểm | `an Enrolment Form` | each member's form, in which the Beneficiary is named | Điều 1.5, src:48 | "registration form" is the literal rendering; "enrolment" is the group-insurance term |
| Người Thụ Hưởng | `the Beneficiary` | the person or organisation named by the member to receive the death benefits | Điều 1.6, src:52 | low; may be an organisation ("tổ chức") |
| người thừa kế hợp pháp | `the legal heirs of the Insured Member` | the member's lawful heirs | Điều 9.3, src:521 | "heirs" carries succession law the document does not set out |
| người yêu cầu giải quyết quyền lợi bảo hiểm | `the claimant` | the person submitting a claim | Điều 26.1, src:1364 | low |
| Tổ Chức Mới | `the New Organisation` | the organisation formed by the Policyholder's division, merger or consolidation | Điều 29.2(b), src:1483 | low |
| Số Tiền Bảo Hiểm | `sum insured` | the amount the Company accepts to insure | Điều 1.7, src:65 | "sum assured" is the British life-insurance term; same meaning |
| Tuổi | `the Age, as at … , of a person born on …` | age at the last birthday before the start date or anniversary | Điều 1.8, src:69 | "Tuổi" is also the ordinary word for age; the document capitalises the defined term but uses it in 12.3 for age at death (fork F12) |
| Ngày Cấp Hợp Đồng | Contract Issue Date (`date the temporary cover period ended`) | the date the Contract is approved and issued | Điều 1.9.1, src:73 | low |
| Ngày Hiệu Lực Hợp Đồng | Contract Effective Date | the date the Contract takes effect | Điều 1.9.2, src:78 | low |
| Ngày Kỷ Niệm Tháng Hợp Đồng | Contract Monthly Anniversary (`the Monthly Anniversary number … of …`) | the monthly date matching the Contract Effective Date | Điều 1.9.3, src:82 | "kỷ niệm" is literally "commemoration"; "anniversary" is the trade term |
| Ngày Bắt Đầu Bảo Hiểm | `coverage start date` | the date one member's cover starts | Điều 1.9.4, src:86 | low |
| Ngày Kỷ Niệm Tháng | Monthly Anniversary (`the Monthly Anniversary number … of …`) | the monthly date matching the Coverage Start Date | Điều 1.9.5, src:92 | easily confused with the Contract Monthly Anniversary (finding X17) |
| Ngày Kỷ Niệm Năm | Policy Anniversary (`the Policy Anniversary number … of …`) | the yearly date matching the Coverage Start Date | Điều 1.9.6, src:96 | it is the member's anniversary, not the Contract's, though "Policy" suggests the latter |
| Năm Bảo Hiểm | `insurance year` | a year from the Coverage Start Date or a Policy Anniversary | Điều 1.9.7, src:103 | "policy year" is the usual English; "insurance year" keeps it per member |
| Năm Phí Bảo Hiểm | Premium Year (`1.9.8 — the insurance year is a Premium Year`) | an insurance year in which every Basic Premium due was paid | Điều 1.9.8, src:109 | low |
| Ngày Đáo Hạn | `maturity date` | the end of a member's term; the part ends that day | Điều 1.9.9, src:113 | low |
| Ngày Đến Hạn Đóng Phí | `Premium Due Date` | the date the Basic Premium must be paid in full | Điều 1.9.10, src:119 | low |
| Thời Hạn Bảo Hiểm | policy term | the period a member is covered | Điều 1.10, src:122 | low |
| Giấy Chứng Nhận Bảo Hiểm | `a Certificate of Insurance` | the certificate issued to each member | Điều 1.11, src:126 | low |
| Phí Bảo Hiểm Định Kỳ | Periodic Premium; `instalment` | Basic plus Rider Premium, paid by period | Điều 1.12, src:130 | "định kỳ" is "periodic" or "regular"; not "recurring" in any statutory sense |
| Phí Bảo Hiểm Cơ Bản | Basic Premium; `basic premium …` fields | premium for the main product | Điều 1.12, src:131 | "cơ bản" is "basic"; not "base premium" of a tariff |
| Phí Bảo Hiểm Bổ Trợ | Rider Premium; `rider premium …` fields | premium for riders | Điều 1.12, src:132 | "bổ trợ" is "supplementary"; "rider" is the trade term |
| Phí Bảo Hiểm Đóng Thêm | Top-up Premium; `top-up premium` | premium paid beyond the Basic Premium | Điều 1.13, src:138 | low |
| Phí Bảo Hiểm Được Phân Bổ | Allocated Premium (`1.14 — the Allocated Premium, of …`) | premium after the Initial Charge, credited to the accounts | Điều 1.14, src:142 | low |
| Phí Ban Đầu | Initial Charge (`25.1 — the Initial Charge on …`) | charge deducted before allocation | Điều 1.15, src:145; 25.1 | "premium allocation charge" in some markets; same function |
| Phí Bảo Hiểm Rủi Ro | Cost of Insurance | the monthly charge for the risk cover | Điều 1.16, src:172; 25.3 | literally "risk premium"; called a charge here because it is deducted, not paid |
| Phí Quản Lý Hợp Đồng | Policy Administration Charge | the monthly administration charge per part | Điều 1.17, src:176; 25.2 | low |
| Khoản Khấu Trừ Hàng Tháng | `Monthly Deduction` | Cost of Insurance plus Policy Administration Charge | Điều 1.18, src:183 | low |
| Phí Chấm Dứt | Termination Charge; `termination charge` | charge on early termination of a part | Điều 1.19, src:187; 25.4 | "surrender charge" is the usual English; the document's trigger differs between 1.19 and 25.4 (finding X18) |
| Phí Rút Giá Trị Tài Khoản | Withdrawal Charge; `withdrawal charge` | charge on a partial withdrawal | Điều 1.20, src:191; 25.5 | low |
| Nợ | `debt` | any sum owed to the Company, deducted before any benefit | Điều 1.21, src:195 | "Nợ" is the ordinary word "debt"; here a defined term that includes unpaid premium and charges, not a loan |
| Giá Trị Tài Khoản | Account Value (`1.22 — the Account Value of`) | the Policyholder's plus the member's account values | Điều 1.22, src:203 | low |
| Giá Trị Tài Khoản Của Bên Mua Bảo Hiểm | `the Policyholder's account value` | the account built from the Policyholder's share of Allocated Premium | Điều 1.22, src:206 | low |
| Giá Trị Tài Khoản Của Người Được Bảo Hiểm | `the Insured Member's account value` | the account built from the member's share | Điều 1.22, src:209 | low |
| Giá Trị Hoàn Lại | Surrender Value (`1.23 — the Surrender Value of …`) | Account Value less Termination Charge | Điều 1.23, src:212 | in the Law, "giá trị hoàn lại" is a statutory term (Law Art 40(3)); the document's definition may not match the Law's |
| Giá Trị Tiền Mặt Thực Trả | Net Cash Value (`1.24 — the Net Cash Value of …`) | Surrender Value less Debt | Điều 1.24, src:214 | literally "actual cash value paid"; "net cash value" chosen to avoid the property-insurance sense of "actual cash value" |
| Giá Trị Tài Khoản Đã Trao Quyền Cho Người Được Bảo Hiểm | Vested Account Value (`1.25 — the Vested Account Value of`) | the part of the Policyholder's account vested in the member | Điều 1.25, src:216 | "trao quyền" is "grant rights"; "vest" imports a pension-law sense of irrevocability the document does not state (it can be changed under 17.3) |
| tỷ lệ trao quyền | `the vesting ratio` | the ratio of the Policyholder's account vested in the member | Điều 6.2(b), src:456; 1.25 | the document never says the ratio is a fraction of the account rather than of contributions (fork F10) |
| tỷ lệ đóng góp | contribution ratio | each party's share of the premium | Điều 1.22, src:207; 16.2.1, src:904 | low |
| Kế Hoạch Bảo Hiểm | `A Plan` | the benefit plan chosen | Điều 1.26, src:223 | low |
| Kế Hoạch Bảo Hiểm Cơ Bản | `the Basic Plan` | death benefit is the greater of Sum Insured and Account Value | Điều 1.26, src:223; 12.2 | low |
| Kế Hoạch Bảo Hiểm Nâng Cao | `the Enhanced Plan` | death benefit is Sum Insured plus Account Value | Điều 1.26, src:224; 12.2 | "nâng cao" is "advanced" or "enhanced" |
| Hợp đồng bảo hiểm | the Contract | the written agreement and its eight documents | Điều 2.1, src:236 | low |
| Hồ Sơ Yêu Cầu Bảo Hiểm | `the Application` | the Policyholder's application form | Điều 2.2, src:251 | "hồ sơ" is "file" or "dossier"; Article 3 uses the same words in lower case for pending applications, which in this product are the Policyholder's (finding X3) |
| Trang Hợp Đồng | `the Contract Page` | the schedule page of the Contract | Điều 2.1(iv), src:244 | it holds most figures (charges, vesting) and is not in the document |
| Xác Nhận Thay Đổi Hợp Đồng | `an Endorsement` | the Company's written confirmation of a change | Điều 2.1(vii), src:249; 2.3 | literally "confirmation of change of contract" |
| phần Hợp Đồng của Người Được Bảo Hiểm | `An Insured Member's part` | the part of the group contract covering one member | passim, e.g. Điều 18.1, src:1006 | "part" is literal; a member's "certificate cover" in group-insurance English |
| bảo hiểm tạm thời | temporary cover; `A death during temporary cover` | cover while an application is pending | Điều 3, src:267 | low |
| Tai Nạn | Accident (`3.1 — the death was caused by an Accident`) | a sudden external event, the direct and sole cause of death | Điều 3.1, src:296 | defined only inside Article 3; Article 26.2 uses "tai nạn" again without a definition |
| sản phẩm bảo hiểm chính | main product; `cover applied for under the main product` | the base product, as against riders | Điều 3.1, src:285 | low |
| mức tiêu chuẩn | standard rate (`3.2 — the standard-rate condition is met`) | acceptance without loading | Điều 3.2, src:306 | low |
| quy định thẩm định | underwriting rules | the Company's rules for assessing risk, not in the document | Điều 3.2, src:307; 10.2 | low |
| kê khai trung thực | declare truthfully; `A breach of the duty to declare` | the duty of disclosure | Điều 5.1, src:376-377 | Vietnamese law frames this as a duty to "provide information"; English "utmost good faith" doctrine is not imported |
| cố ý | `deliberate` | intentional | Điều 5.2, src:388 | "cố ý" is the Civil Code's "intentional fault"; "deliberate" is narrower than "reckless" |
| bất khả kháng | force majeure; `the delay was the result of force majeure` | an unforeseeable, unavoidable event | Điều 26.1, src:1371 | its meaning comes from the Civil Code, outside the document |
| Quyền lợi trợ cấp mai táng | funeral benefit | an advance on the death benefit for funeral costs | Điều 12.1, src:700 | "trợ cấp" is "allowance" or "subsidy"; it is not an extra benefit (fork F15) |
| Quyền lợi tử vong | death benefit | the main death benefit by Plan | Điều 12.2, src:716 | low |
| Quyền Lợi Đáo Hạn | maturity benefit | the account split at maturity | Điều 13, src:730 | low |
| Quyền Lợi Đặc Biệt Khi Duy Trì Bảo Hiểm | loyalty bonus; `A loyalty bonus review` | 5% of the average Account Value every five years | Điều 14, src:744-745 | literally "special benefit for maintaining the insurance"; "loyalty bonus" is the trade term |
| thời hạn xem xét | review period | each five-year period for the loyalty bonus | Điều 14.2, src:768 | low |
| Loại trừ | exclusion (`15 — the death is excluded, …`) | causes on which the death benefit is not paid | Điều 15, src:780 | low |
| hành vi vi phạm pháp luật hình sự | criminal act; `a criminal act of …` fields | an act in breach of the criminal law | Điều 15(b), src:790 | "vi phạm pháp luật hình sự" covers any criminal-law breach, not only a conviction; the document does not say whether a conviction is needed |
| Phí Treo | `suspense premium` | premium held by the Company that is too little for an instalment | Điều 16.2.1(a), src:831 | literally "hanging premium" |
| phí bổ sung | `supplementary premium` | further premium paid in the grace period | Điều 16.2.1(a)(i), src:834 | not the defined "Phí Bảo Hiểm Bổ Trợ" (rider premium), despite the similar word |
| gia hạn đóng phí | grace period | 60 days to pay before lapse | Điều 18.1, src:995 | literally "extension of premium payment" |
| mất hiệu lực | `lapsed` | the part is out of force | Điều 18.2, src:1008 | low |
| khôi phục hiệu lực | reinstatement; `A request for reinstatement` | restoring a lapsed part | Điều 19, src:1028 | low |
| Tạm Đóng Tài Khoản | account suspension; `suspended` | a premium holiday with all cover suspended | Điều 20, src:1057 | literally "temporary closing of the account"; it suspends the death benefit too (finding X7), which "premium holiday" would hide |
| Rút Giá Trị Tài Khoản | withdrawal; `A withdrawal request` | a partial withdrawal from the member's account | Điều 21, src:1088 | low |
| hợp đồng bảo hiểm cá nhân | individual policy | the policy a member may convert to | Điều 11.2(a), src:617 | low |
| Quỹ Liên Kết Chung | the universal-linked fund | the fund backing all universal-linked contracts | Điều 24.1, src:1193-1195 | "liên kết chung" is "universal linked" (universal life, one pooled fund with a declared rate), not "unit linked", a different product class |
| Lãi suất công bố | declared rate | the monthly rate the Company announces | Điều 24.2(b), src:1221-1222 | low |
| Lãi suất cam kết | guaranteed rate (`24.2(e) — the guaranteed rate in insurance year`) | the minimum rate by insurance year | Điều 24.2(e), src:1240 | "cam kết" is "commit"; read as a floor (fork F21) |
| Phí Quản Lý Quỹ | Fund Management Charge | deducted before the rate is declared | Điều 25.6, src:1339 | low |
| mối quan hệ lao động | employment relationship; `full years of employment with the Policyholder` | the member's employment by the Policyholder | Điều 29.3(a), src:1519 | the document never requires a member to be an employee (fork F27) |
| Thời hiệu khởi kiện | limitation of suit (`27.3 — the last day to sue, …`) | the period to sue | Điều 27.3, src:1419 | low |

Types and fields that render no single Vietnamese term (`A party`, `An act under the Contract`, the outcome types, the case records) are named in English for what the document makes of them; each carries its `src:` citation in `vn14-nouns.l4`.
