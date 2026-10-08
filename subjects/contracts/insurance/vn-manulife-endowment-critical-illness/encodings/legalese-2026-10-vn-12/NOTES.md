# NOTES — vn-manulife-endowment-critical-illness, encoding row `legalese-2026-10-vn-12`

Manulife Việt Nam's terms for an endowment with a critical illness benefit paid in three stages ("CSTD", from the product name in the document's URL path, `cuoc-song-tuoi-dep`; approved by Ministry of Finance letter 1997/BTC-QLBH of 20 February 2019), encoded in L4 by one agent in one session (run `VN-12-20261006`, 6-7 October 2026) from `BRIEF.md`.
Status: **draft**.
No domain expert has read it against the source; HG1 has not been sought.

## 0. Build and run

- `l4`: `/Users/mengwong/.local/bin/l4`, sha256 `64bbcb157dbef2ef1020a6a75589313bba0a2aeeb807c921c5e65e62e9eca118`; it has no `--version`. `JL4_LIBRARY_PATH` unset. Every run prints two Warnings that differing copies of `prelude` and `daydate` exist under `~/.local/share/jl4/libraries/`; the binary uses its embedded copies, and the warnings are not errors.
- Command, from this directory: `L4=/Users/mengwong/.local/bin/l4 ./check.sh`.
- Totals: see §6, copied from the run.
- Source: `../../source/raw/manulife-cstd.txt` (sha256 `432165cb6277f734b148cd3b4c91b302a35a36453b97f71a8d453b1e032b7536`), the `pdftotext` reading-order rendering of `manulife-cstd.pdf` (sha256 `fdf3c7f0ca507f8f2f1c0c9d743fa4ca285b2a8f1b63ffb8fdbc7555ee0b8141`, 34 pages). The brief gives the PDF's sha256 for both; the `.txt` has its own, above. A `src:N` is line N of the `.txt`.
- Generated files. `cstd-annex-tables.l4`, `cstd-tests-annex.l4` and the three enumerations between the `BEGIN/END GENERATED` markers of `cstd-nouns.l4` are written by `python3 -I tools/gen_annex.py ../../source/raw/manulife-cstd.txt .` from `tools/conditions.py` (the encoder's hand-written reading of Annexes 1-3) and the raw text; the script says how its tests get expected values independently of the table it writes. Every `-- src:N |` line was produced by `tools/vnsrc.py quote` (through a placeholder expander), never typed.

Modules (ASCII names, each `@lang en`):

| module | what it holds |
| --- | --- |
| `cstd-nouns.l4` | DECLARE only: parties, contract, application, accident, the 147 listed conditions, measured quantities, causes, diagnosis, claims, records the later articles read |
| `cstd-annex-tables.l4` | generated: where each listed condition is listed, the thresholds its definition states, the causes it excludes, and the bars between conditions |
| `cstd-annex-rules.l4` | reading a diagnosis against the annex data |
| `cstd-ch1-general.l4` | Chapter 1, Articles 1-11 |
| `cstd-ch2-conditions.l4` | Articles 18-19 (waiting and survival periods, exclusions) |
| `cstd-ch2-benefits.l4` | Chapter 2 preamble, Articles 12-17, and the two claim decisions |
| `cstd-ch3-premiums.l4` | Chapter 3, Articles 20-28 |
| `cstd-ch4-claims.l4` | Chapter 4, Articles 29-32 |
| `cstd-tests-fixtures.l4` | builders for named cases; no assertions |
| `cstd-tests-ch1.l4`, `cstd-tests-ch2.l4`, `cstd-tests-ch3-ch4.l4` | hand-worked tests |
| `cstd-tests-annex.l4` | generated boundary tests of every annex threshold |
| `cstd-tests-findings.l4` | each demonstrable finding of §4, asserted as the instrument is written |

## 1. What is encoded and what is not

**Encoded: the whole document.** Articles 1 to 32 and Annexes 1 to 3, every provision with a disposition in §2.
Operative: the definitions the articles read (ages and Tuổi, dates, the term, the premium term, cash value and surrender value, Accident, pre-existing condition); formation and voidness (2.3); temporary cover; the free-look period; the duties to inform, keep confidential and disclose; misstated age or sex; incontestability; currency; the beneficiaries' shares and payees; changes of occupation or residence; the minimum benefit of Chapter 2; the funeral, death, three-stage critical illness, additional and comfort-cash-coupon benefits; the adjustment for a child under 4; when dividends fall due; payment methods; maturity; the waiting and survival periods; the exclusions; grace, the automatic premium loan and lapse; deductions; reinstatement; cash value; early termination; loans; the reduced paid-up option; adding riders; claim deadlines, documents and payment; disputes; and the ending of the critical illness benefit and of the contract.
Annexes 1-3: all 147 separately headed conditions (49 early-stage, 36 middle-stage, 49 late-stage, 1 for men, 4 for women, 8 for children), each with its list and item number, every number its definition states (118 thresholds), the causes its own definition excludes, and the three bars one condition puts on another.

**Not computed, by design, each said where it arises:**
- The qualitative part of each annex definition (which specialist, which test, the clinical picture, TNM categories, any exclusion that is not a cause) is one certified fact of the diagnosis, `the rest of the definition certified as met`. So the in-definition exclusions that are not causes (e.g. CIN-1 to CIN-3 for carcinoma in situ) are not tested individually.
- Amounts the Company sets and the document does not state: dividends (Article 15), the cash value table and values between year ends (24), the reduced paid-up sum insured (27, a named refusal), loan and late-payment interest rates (26, 29.4).
- The riders' own terms (1.13, 28.3): not in the source.

**Inputs, never defaults.** The sum insured at each event, the premiums, Debt, dividends and interest, the cash value from the schedule, what the Company's records show of earlier payments: all inputs. A number appears in the rules only where the document states it.

**Gaps answer with a named `REFUSE`.** Eleven: a threshold the diagnosis does not report; the 30-day survival period not yet run; Article 3 on a death by illness; Article 4 where deductions exceed the premium; Article 6 on an innocent but material misstatement; Article 10.2 with shares stated for some beneficiaries only; Article 13.2, 13.3 and 13.5 where earlier payments exceed the benefit; Article 21's uncovered case; Article 27's reduced sum insured.

## 2. Coverage table

Totals: **Articles: 104 rows: 84 encoded, 20 inert, 0 out-of-scope, 0 deferred. Annexes: 153 rows (6 list headings and preambles plus 147 conditions): all encoded.**
Headings are quoted as the document writes them; where a clause has no heading, its opening words are given.

### 2.1 Chapters 1 to 4

| provision | heading as written | gloss | src | disposition | where |
| --- | --- | --- | --- | --- | --- |
| title | QUY TẮC, ĐIỀU KHOẢN SẢN PHẨM BẢO HIỂM HỖN HỢP | the product's rules and terms | 1-3 | inert: names the product and the approval letter | nouns header |
| Ch 1 | CHƯƠNG 1 NHỮNG QUY ĐỊNH CHUNG | general provisions | 5 | inert: heading | `§ Chapter 1` |
| 1.1 | Công Ty | the Company | 19-22 | inert: names a party | `A party` |
| 1.2 | Bên Mua Bảo Hiểm | the policyholder | 23-30 | encoded | `1.2 — may be the policyholder on` |
| 1.3 | Người Được Bảo Hiểm | the insured, and who may be insured | 31-45 | encoded | `1.3 — the insured may be insured under` |
| 1.4 | Người Thụ Hưởng | the beneficiary | 46-50 | encoded (as the beneficiary record; its rights in 10.2) | `A beneficiary` |
| 1.5 | Số Tiền Bảo Hiểm | the sum insured | 51-61 | encoded as an input at each event | claim records |
| 1.6 | Tuổi | age, as the terms count it | 62-65 | encoded | `the Tuổi on the anchor day`, `the insured's Tuổi under` |
| 1.7.1-1.7.2 | Ngày Cấp Hợp Đồng; Ngày Hiệu Lực Hợp Đồng | issue date; effective date | 67-76 | encoded (inputs) | `The contract` |
| 1.7.3 | Ngày Kỷ Niệm Hợp Đồng | policy anniversary | 77-81 | encoded | `the policy anniversary` |
| 1.7.4 | Năm Hợp Đồng | policy year | 82-84 | encoded | `the policy year of` |
| 1.7.5 | Ngày Đáo Hạn Hợp Đồng | maturity date | 85-87 | encoded | `the maturity date of` |
| 1.7.6 | Ngày Đến Hạn Đóng Phí | premium due date | 88-90 | encoded (input to 20.2) | `20.2 — the last day of the grace period` |
| 1.8 | Thời Hạn Hợp Đồng | contract term, to 99 Tuổi | 91-96 | encoded | `the maturity date of` |
| 1.9 | Thời Hạn Đóng Phí | premium term, 12, 15 or 20 years | 97-109 | encoded | `the end of the premium term of` |
| 1.10 | Phí Bảo Hiểm | premium | 110-115 | inert: an input wherever used | claim records |
| 1.11 | Trang Hợp Đồng (Giấy Chứng Nhận Bảo Hiểm) | policy schedule | 116-118 | inert: the document inputs come from | nouns header |
| 1.12 | Xác Nhận Thay Đổi Hợp Đồng | endorsement | 119-121 | encoded through 2.4 | `2.4 — the requested change has effect` |
| 1.13 | Sản Phẩm Bảo Hiểm Bổ Trợ | riders | 122-126 | inert: the riders' terms are not in the source | 28.2 |
| 1.14 | Nợ | Debt | 127-135 | encoded as an input, deducted under 12.3, 17, 22 | `22 — the payment of` |
| 1.15 | Giá Trị Tiền Mặt | cash value, halved after a late-stage approval | 136-148 | encoded | `1.15 — the cash value on` |
| 1.16 | Giá Trị Hoàn Lại | surrender value | 149-167 | encoded | `1.16 — the surrender value from` |
| 1.17 | Tai Nạn | Accident | 168-177 | encoded | `1.17 — an Accident:` |
| 1.18 | Bệnh Lý Nghiêm Trọng | critical illness, by the annexes | 178-180 | encoded | `cstd-annex-tables.l4` |
| 1.19 | Bệnh Có Sẵn | pre-existing condition | 181-189 | encoded | `1.19 — a pre-existing condition under` |
| 1.20 | Hợp Đồng Bảo Hiểm Giảm | reduced paid-up contract | 190-195 | encoded through Article 27 | `cstd-ch3-premiums.l4` |
| 1.21 | Lần Thăm Khám | a medical visit | 196-199 | encoded (the visit number of a diagnosis) | `13(b) — the limits that stop` |
| 1.22 | Quy Trình Nghiệp Vụ | the Business Procedures | 200-206 | inert: read only by 12.1's cap (finding X-12) | `12.1 — the funeral benefit advanced on` |
| 2.1 | Hợp đồng bảo hiểm là thỏa thuận bằng văn bản | the contract and its documents | 211-235 | inert: a list of documents | — |
| 2.2 | Hồ Sơ Yêu Cầu Bảo Hiểm | the application file | 236-244 | inert: a definition no rule reads | — |
| 2.3 | Công Ty sẽ không bảo hiểm cho Người Được Bảo Hiểm | no consent or no insurable relationship: void, refund | 245-269 | encoded | `2.3 — the contract has no effect`, `2.3 — the refund of` |
| 2.4 | Nếu Hợp Đồng được thay đổi hoặc được sửa đổi | changes take effect on endorsement | 270-274 | encoded | `2.4 — the requested change has effect` |
| 3.1 | Trong thời hạn bảo hiểm tạm thời | temporary cover benefit and period | 281-304 | encoded | `Article 3 — the answer on` |
| 3.2 | Quyền lợi bảo hiểm tạm thời nêu trên sẽ không có hiệu lực | temporary cover exclusions | 305-316 | encoded | `3.2 — the temporary cover is void` |
| 4 | ĐIỀU 4 THỜI GIAN CÂN NHẮC | free-look period | 318-331 | encoded | `4 — the last day to refuse`, `4 — the refund of`, deontic |
| 5.1 | Khi giao kết Hợp Đồng, Công Ty có trách nhiệm cung cấp đầy đủ thông tin | the Company's duty to inform | 341-348 | encoded | `5.1 — the return on termination` |
| 5.2 | Công Ty không được chuyển giao thông tin cá nhân | confidentiality | 349-371 | encoded | `5.2 — the transfer is permitted`, deontic |
| 6.1 | Bên Mua Bảo Hiểm và/hoặc Người Được Bảo Hiểm có nghĩa vụ phải kê khai trung thực | duty to disclose | 381-390 | encoded (deontic, no period) | `6.1 — the duty to disclose` |
| 6.2 | Công Ty sẽ đơn phương chấm dứt | intentional non-disclosure; fraud | 391-415 | encoded | `Article 6 — the consequence of`, `6.2 — what remains payable` |
| 6.3 | việc vi phạm này không làm ảnh hưởng | an immaterial breach | 416-426 | encoded | `Article 6 — the consequence of` |
| 7.1 | Trong trường hợp kê khai sai tuổi và/hoặc giới tính | misstated age or sex, within range | 432-449 | encoded | `7.1 — the adjustment for` |
| 7.2 | Tuổi thực của Người Được Bảo Hiểm không nằm trong nhóm tuổi | outside the insurable range | 450-468 | encoded | `the greater of the surrender value` |
| 8.1-8.2 | ĐIỀU 8 MIỄN TRUY XÉT | incontestability | 470-492 | encoded | `8 — on … the contract can no longer be voided` |
| 9 | ĐIỀU 9 TIỀN TỆ VÀ NƠI THANH TOÁN | currency and place | 494-499 | encoded | `9 — a payment by the Company conforms` |
| 10.1(a), (d) | Bên Mua Bảo Hiểm sẽ thực hiện mọi quyền và nghĩa vụ | the policyholder's rights; no liability for successions | 504-505, 539-540 | inert: no case turns on them | — |
| 10.1(b)-(c) | Bên Mua Bảo Hiểm là cá nhân bị tử vong | succession of the policyholder | 506-538 | encoded | `10.1 — the successor to the policyholder of` |
| 10.2(a) | Người Thụ Hưởng được Bên Mua Bảo Hiểm chỉ định | naming and changing beneficiaries | 547-553 | encoded (whether consent is needed) | `10.2 — changing the beneficiary needs the insured's consent` |
| 10.2(b), (e)(i) | Người Thụ Hưởng được hưởng các quyền lợi | who is paid what | 554-561, 583-596 | encoded | `10.2 — the payee` |
| 10.2(c)-(d), (e)(ii) | Nếu không có Người Thụ Hưởng nào được chỉ định | shares; no beneficiary | 562-582, 597-600 | encoded | `10.2 — the recipients of the death benefit` |
| 10.2(e)(iii) | việc thay đổi Người Thụ Hưởng phải được Người Được Bảo Hiểm đồng ý | change needs the insured's consent | 601-602 | encoded | as 10.2(a) |
| 10.2(f) | Công Ty sẽ không chịu trách nhiệm về tính hợp pháp | no liability for disputes | 603-606 | inert | — |
| 11, 11.1(a) | ĐIỀU 11 CÁC THAY ĐỔI LIÊN QUAN ĐẾN HỢP ĐỒNG | changes of details | 608-619 | inert: changes of address and identity decide nothing here | — |
| 11.1(b) | Thay đổi nghề nghiệp/tính chất công việc | occupation change, 90 days abroad | 620-648 | encoded | `11.1(b) — the Company's options on`; termination refund as 7.2 |
| 11.2 | Chuyển nhượng Hợp Đồng | assignment | 649-658 | inert: the Company only records it | — |
| Ch 2 preamble | Trong mọi trường hợp tổng quyền lợi chi trả | benefit on death or maturity not below premiums | 662-664 | encoded | `Chapter 2 — the benefit` |
| 12.1 | Quyền lợi trợ cấp mai táng | funeral benefit | 668-682 | encoded | `12.1 — the funeral benefit advanced on` |
| 12.2 | Quyền lợi tử vong | death benefit, 200% or 100% | 683-707 | encoded | `12.2 — the death benefit on` |
| 12.3 | Trước khi thanh toán Quyền lợi bảo hiểm tử vong | settlement on death | 708-719 | encoded | `12.3 — the death benefit settled on`, `the answer on the death claim` |
| 13 preamble | ĐIỀU 13 QUYỀN LỢI BỆNH LÝ NGHIÊM TRỌNG | while in force | 721-723 | encoded (in force at diagnosis) | `the answer on the critical illness claim` |
| 13.1(a) | Quyền lợi bảo hiểm Bệnh Lý Nghiêm Trọng giai đoạn sớm | early stage: lesser of 25% and 500 million | 724-745 | encoded | `13.1(a) — the early-stage benefit` |
| 13.1(b) | Các điều kiện sau sẽ được Công Ty áp dụng | four payments, one per condition, same day or visit, paired organs | 746-765 | encoded | `13(b) — the limits that stop` |
| 13.2(a) | Quyền lợi bảo hiểm Bệnh Lý Nghiêm Trọng giai đoạn giữa | middle stage: lesser of 50% and 1 billion, less early for the same illness | 766-785 | encoded | `13.2(a) — the middle-stage benefit` |
| 13.2(b) | Các điều kiện sau sẽ được Công Ty áp dụng | two payments, and the rest | 788-807 | encoded | `13(b) — the limits that stop` |
| 13.3(a) | Quyền lợi bảo hiểm Bệnh Lý Nghiêm Trọng giai đoạn cuối | late stage: 100%, less earlier for the same illness | 808-822 | encoded | `13.3(a) — the late-stage benefit` |
| 13.3(b) | Công Ty chỉ chi trả một (01) lần | one payment, and the rest | 823-842 | encoded | `13(b) — the limits that stop` |
| 13.3, last | Quyền lợi bảo hiểm nêu tại Điều 13.1, 13.2 và 13.3 sẽ chấm dứt | 13.1-13.3 end on approving "this benefit" | 843-845 | encoded through 31.3 (fork F-13a) | `31 — under` |
| 13.4 | Quyền lợi Bệnh Lý Nghiêm Trọng bổ sung | additional 25% for Annexes 2 and 3 | 846-870 | encoded | `13.4 — under … the additional benefit covers`, `13.4 — the additional benefit` |
| 13.5 | Phiếu tiền mặt an nhàn | comfort cash coupon | 871-890 | encoded | `13.5 — the comfort cash coupon date of`, `13.5 — the coupon` |
| 14 | ĐIỀU 14 MỨC ĐIỀU CHỈNH TRONG TRƯỜNG HỢP NGƯỜI ĐƯỢC BẢO HIỂM LÀ TRẺ EM | a child under 4: 20-80% | 892-914 | encoded (table, one arm per row) | `14 — the percentage of the sum insured at Tuổi` |
| 15 preamble | ĐIỀU 15 QUYỀN LỢI BẢO TỨC | participating; amounts the Company's | 916-923 | inert: the amounts are discretionary | — |
| 15(a) | Bảo tức định kỳ | periodic dividend | 924-930 | encoded (when it may be declared) | `15(a) — a periodic dividend may be declared` |
| 15(b) | Bảo tức tri ân | loyalty dividend | 931-946 | encoded (when it falls due) | `15(b) — under … a loyalty dividend falls due` |
| 15, last | Bảo tức định kỳ và Bảo tức tri ân được tính dựa trên Số Tiền Bảo Hiểm | basis; paid with death, surrender, maturity | 947-951 | encoded through 12.2 and 17 | — |
| 16.1-16.3 | Đối với Phiếu tiền mặt an nhàn | payment methods, default | 965-992 | encoded | `16.1 — the coupon remaining`, `16 — the method for a payment` |
| 16.4 | Phiếu tiền mặt an nhàn, Bảo tức tích lũy và lãi tích lũy | paid on death, surrender, maturity | 993-997 | encoded | `16.4 — the coupons and interest also paid` |
| 17 | ĐIỀU 17 QUYỀN LỢI ĐÁO HẠN HỢP ĐỒNG | maturity benefit | 953-961 | encoded | `17 — the maturity benefit on` |
| 18 | ĐIỀU 18 THỜI GIAN CHỜ VÀ THỜI GIAN CÒN SỐNG | 90-day waiting, 30-day survival | 1001-1018 | encoded | `18 — under … the waiting and survival periods allow` |
| 19.1 | Công ty sẽ không thanh toán Quyền lợi bảo hiểm tử vong | death exclusions, and what is paid instead | 1023-1047 | encoded | `19.1 — under`, `19.1 — the payment on an excluded death` |
| 19.2 | Công Ty sẽ không thanh toán Quyền lợi Bệnh lý Nghiêm Trọng | critical illness exclusions | 1048-1062 | encoded | `19.2 — under` |
| Ch 3 | CHƯƠNG 3 PHÍ BẢO HIỂM, TÀI KHOẢN, SỐ TIỀN BẢO HIỂM | premiums, accounts, sum insured | 1064-1065 | inert: heading | — |
| 20.1-20.3 | ĐIỀU 20 PHÍ BẢO HIỂM VÀ GIA HẠN ĐÓNG PHÍ BẢO HIỂM | premiums and grace | 1066-1081 | encoded | `20.2 — the last day of the grace period`, `20.1 — the duty to pay the premium due` |
| 21.1-21.2 | ĐIỀU 21 THANH TOÁN PHÍ BẢO HIỂM TỰ ĐỘNG VÀ HỢP ĐỒNG MẤT HIỆU LỰC | automatic premium loan; lapse | 1083-1107 | encoded | `21 — the outcome of` |
| 21.3 | Trong suốt thời gian Hợp Đồng mất hiệu lực | no benefit while lapsed | 1108-1109 | encoded (in force at the event) | claim decisions |
| 22.1-22.2 | ĐIỀU 22 KHẤU TRỪ | deductions | 1111-1126 | encoded | `22 — the payment of` |
| 23 | ĐIỀU 23 KHÔI PHỤC HIỆU LỰC HỢP ĐỒNG | reinstatement | 1128-1151 | encoded | `23 — under …` (time, conditions, deontic) |
| 24 | ĐIỀU 24 BẢNG GIÁ TRỊ TIỀN MẶT | cash value | 1153-1170 | encoded (when there is one; the values are the schedule's) | `24 — the contract has a cash value` |
| 25 | ĐIỀU 25 CHẤM DỨT HỢP ĐỒNG TRƯỚC THỜI HẠN | early termination | 1172-1178 | encoded | `25 — the payment on early termination` |
| 26.1, 26.5 | ĐIỀU 26 : TẠM ỨNG TỪ GIÁ TRỊ TIỀN MẶT | loans: 80% limit; lapse | 1182-1191, 1204-1207 | encoded | `26.1 — a loan …`, `26.5 — the contract lapses` |
| 26.2-26.4 | Mức lãi suất cho các khoản tạm ứng | loan interest and repayment | 1192-1203 | inert: rates and minimums are the Company's to publish | — |
| 27 | ĐIỀU 27 HỢP ĐỒNG BẢO HIỂM GIẢM | reduced paid-up | 1209-1225 | encoded (when open; the new sum insured is a named refusal) | `27 — …` |
| 28.1 | Giảm Số Tiền Bảo Hiểm | reducing the sum insured | 1231-1243 | inert: at the Company's discretion, no criteria (finding X-12) | — |
| 28.2 | Tham gia thêm (các) Sản Phẩm Bảo Hiểm Bổ Trợ | adding riders within 6 months | 1244-1254 | encoded | `28.2 — under …` |
| 28.3-28.4 | Hiệu lực của (các) Sản Phẩm Bảo Hiểm Bổ Trợ | riders' dates; cancelling riders | 1255-1270 | inert: riders' own terms | — |
| Ch 4 | CHƯƠNG 4 GIẢI QUYẾT QUYỀN LỢI BẢO HIỂM | claims, disputes, termination | 1272-1276 | inert: heading | — |
| 29.1 | Thời hạn nộp yêu cầu giải quyết quyền lợi bảo hiểm | notice; one year to claim | 1279-1291 | encoded | `29.1 — …` (deontic, date, in time) |
| 29.2 | Chứng từ yêu cầu giải quyết quyền lợi bảo hiểm tử vong | death claim documents | 1292-1309 | encoded | `29.2 — the death claim documents are complete` |
| 29.3 | Chứng từ yêu cầu giải quyết quyền lợi Bệnh Lý Nghiêm Trọng | critical illness documents | 1310-1328 | encoded | `29.3 — …` |
| 29.4 | Thời gian giải quyết quyền lợi bảo hiểm | 30 days to pay; interest | 1329-1340 | encoded | `29.4 — …` (deontic, dates) |
| 30.1 | Hợp Đồng được điều chỉnh và giải thích theo pháp luật | Vietnamese law | 1343-1344 | inert | — |
| 30.2 | Nếu có bất kỳ tranh chấp nào không thể giải quyết | forum | 1345-1348 | encoded | `30.2 — the forums open` |
| 30.3 | Thời hiệu khởi kiện | 3 years to sue | 1349-1352 | encoded | `30.3 — the last day to sue` |
| 31 | ĐIỀU 31 CHẤM DỨT QUYỀN LỢI BỆNH LÝ NGHIÊM TRỌNG | end of the critical illness benefit | 1356-1368 | encoded | `31 — under` |
| 32.1-32.3, 32.5-32.8 | ĐIỀU 32 CHẤM DỨT HỢP ĐỒNG | end of the contract | 1370-1388 | encoded | `32 — the grounds on which` |
| 32.4 | Người Được Bảo Hiểm liên quan không còn đáp ứng các điều kiện | insured no longer meets 1.3 | 1379-1381 | encoded on the application-time reading; the literal reading separately (finding X-1) | `32 — …`, `32.4, read literally` |

### 2.2 Annexes: headings and preambles

| provision | heading as written | gloss | src | disposition | where |
| --- | --- | --- | --- | --- | --- |
| Annex 1, early | PHỤ LỤC 1 DANH SÁCH CÁC BỆNH LÝ NGHIÊM TRỌNG GIAI ĐOẠN SỚM | early-stage list, paid several times | 1392-1393 | encoded | `A list of conditions` |
| Annex 1, middle | DANH SÁCH CÁC BỆNH LÝ NGHIÊM TRỌNG GIAI ĐOẠN GIỮA THANH TOÁN NHIỀU LẦN | middle-stage list | 1910-1911 | encoded | same |
| Annex 1, late | GIAI ĐOẠN CUỐI | late-stage list | 2408-2409 | encoded | same |
| Annex 1, late (a)-(f) | Chức Năng Sinh Hoạt Hàng Ngày | the six activities of daily living | 2410-2430 | encoded | `An activity of daily living`, `the number of activities of daily living in` |
| Annex 2 | DANH SÁCH CÁC BỆNH LÝ NGHIÊM TRỌNG CHO NAM GIỚI; CHO NỮ GIỚI | lists for men and for women | 3147, 3175 | encoded | same; 13.4 |
| Annex 3 | DANH SÁCH CÁC BỆNH LÝ NGHIÊM TRỌNG CHO TRẺ EM | list for children, and its preamble on cover to 18 | 3277-3281 | encoded | same; `13.4 — under … the additional benefit covers` |

### 2.3 Annexes: every listed condition

Generated from `tools/conditions.py`; the heading is the raw text at the lines given. Every row is **encoded**: its listing (list and item number) in `the listing of`, its stated thresholds in `the measured criteria of`, its excluded causes in `the causes excluded by the definition of`, all in `cstd-annex-tables.l4`.

| id | heading as written | English (the L4 constructor) | list, item | src | disposition |
| --- | --- | --- | --- | --- | --- |
| E1 | Ung thư biểu mô tại chỗ | `carcinoma in situ` | Annex 1, early, 1 | 1398 | encoded: listing; no number stated, the specialist's certificate carries it |
| E1a | Ung thư tiền liệt tuyến giai đoạn sớm | `early prostate cancer` | Annex 1, early, 1 | 1415 | encoded: listing; no number stated, the specialist's certificate carries it |
| E1b | Ung thư tuyến giáp giai đoạn sớm | `early thyroid cancer` | Annex 1, early, 1 | 1419 | encoded: listing; 1 threshold (thyroid tumour diameter in cm); a qualitative alternative |
| E1c | Ung thư bàng quang giai đoạn sớm | `early bladder cancer` | Annex 1, early, 1 | 1423 | encoded: listing; no number stated, the specialist's certificate carries it |
| E1d | Ung thư máu dòng lympho mạn tính giai đoạn sớm | `early chronic lymphocytic leukaemia` | Annex 1, early, 1 | 1425-1426 | encoded: listing; 2 thresholds (RAI stage) |
| E1e | Ung thư hắc tố giai đoạn sớm | `early melanoma` | Annex 1, early, 1 | 1430 | encoded: listing; 2 thresholds (Breslow thickness in mm, Clark level); a qualitative alternative |
| E2 | Phẫu thuật cắt bỏ u tuyến yên thông qua đường xuyên xoang bướm hoặc đường mũi | `transsphenoidal or transnasal removal of a pituitary tumour` | Annex 1, early, 2 | 1435-1436 | encoded: listing; no number stated, the specialist's certificate carries it |
| E3 | Chẩn đoán bệnh Sa sút trí tuệ bao gồm Bệnh Alzheimer | `diagnosed dementia including Alzheimer's disease` | Annex 1, early, 3 | 1454-1455 | encoded: listing; 1 threshold (MMSE score out of 30); a qualitative alternative |
| E4 | Bệnh Parkinson nhẹ | `mild Parkinson's disease` | Annex 1, early, 4 | 1466 | encoded: listing; no number stated, the specialist's certificate carries it; excluded causes: medicines or drugs, toxins |
| E5 | Câm bất động (Akinetic Mutism) | `akinetic mutism` | Annex 1, early, 5 | 1474 | encoded: listing; 1 threshold (months the qualifying state has lasted); excluded causes: a psychological or psychiatric cause without organic damage |
| E6 | Hôn mê kéo dài ít nhất 48 giờ | `coma of at least 48 hours` | Annex 1, early, 6 | 1483 | encoded: listing; 2 thresholds (days after the coma at which the permanent neurological deficit is assessed, hours without response to external stimuli); excluded causes: alcohol, medicines or drugs, addictive substances |
| E7 | Bệnh thần kinh ngoại biên | `peripheral neuropathy` | Annex 1, early, 7 | 1507 | encoded: listing; no number stated, the specialist's certificate carries it; excluded causes: diabetes, alcohol, poliomyelitis |
| E8 | Bệnh xơ cứng rải rác giai đoạn sớm | `early multiple sclerosis` | Annex 1, early, 8 | 1518 | encoded: listing; no number stated, the specialist's certificate carries it; excluded causes: systemic lupus erythematosus, HIV infection |
| E9 | Bệnh hoặc tổn thương tủy sống gây rối loạn chức năng của ruột và bàng quang | `spinal cord disease or injury causing bowel and bladder dysfunction` | Annex 1, early, 9 | 1527-1528 | encoded: listing; 1 threshold (months the qualifying state has lasted) |
| E10 | Phương pháp điều trị truyền cơ tim bằng tia Laser | `transmyocardial laser revascularisation` | Annex 1, early, 10 | 1534-1535 | encoded: listing; no number stated, the specialist's certificate carries it |
| E11 | Bệnh động mạch vành nhẹ | `mild coronary artery disease` | Annex 1, early, 11 | 1540 | encoded: listing; 1 threshold (number of named coronary arteries narrowed by at least 60%) |
| E12 | Đặt máy điều hòa nhịp tim | `pacemaker insertion` | Annex 1, early, 12 | 1560 | encoded: listing; no number stated, the specialist's certificate carries it |
| E12b | Đặt máy khử rung tim | `defibrillator insertion` | Annex 1, early, 12 | 1566 | encoded: listing; no number stated, the specialist's certificate carries it |
| E13 | Thủ thuật tạo hình van tim, tách van tim qua da | `percutaneous heart valve repair or valvotomy` | Annex 1, early, 13 | 1572 | encoded: listing; no number stated, the specialist's certificate carries it |
| E13b | Thủ thuật thay thế van tim hay chỉnh sửa thiết bị qua da | `percutaneous heart valve replacement or device repair` | Annex 1, early, 13 | 1577-1578 | encoded: listing; no number stated, the specialist's certificate carries it |
| E14 | Tăng áp lực động mạch phổi giai đoạn sớm | `early pulmonary arterial hypertension` | Annex 1, early, 14 | 1586 | encoded: listing; 2 thresholds (NYHA class) |
| E15 | Phẫu thuật phình động mạch ở não | `cerebral aneurysm surgery` | Annex 1, early, 15 | 1618 | encoded: listing; no number stated, the specialist's certificate carries it |
| E15b | Dẫn lưu não thất | `ventricular drainage` | Annex 1, early, 15 | 1625 | encoded: listing; no number stated, the specialist's certificate carries it |
| E16 | Phình động mạch chủ lớn không triệu chứng | `large asymptomatic aortic aneurysm` | Annex 1, early, 16 | 1630 | encoded: listing; 1 threshold (aortic diameter in mm) |
| E17 | Phẫu thuật cắt bỏ 1 bên phổi | `removal of one lung` | Annex 1, early, 17 | 1636 | encoded: listing; no number stated, the specialist's certificate carries it |
| E17b | Đặt lưới lọc tĩnh mạch chủ | `vena cava filter insertion` | Annex 1, early, 17 | 1640 | encoded: listing; no number stated, the specialist's certificate carries it |
| E18 | Phẫu thuật gan | `liver surgery` | Annex 1, early, 18 | 1645 | encoded: listing; 1 threshold (whole liver lobes removed); excluded causes: alcohol, addictive substances |
| E19 | Phẫu thuật tái cấu trúc đường mật | `biliary tract reconstruction surgery` | Annex 1, early, 19 | 1650 | encoded: listing; no number stated, the specialist's certificate carries it; excluded causes: gallstones or cholecystitis |
| E20 | Phẫu thuật cắt bỏ một thận | `removal of one kidney` | Annex 1, early, 20 | 1658 | encoded: listing; no number stated, the specialist's certificate carries it; excluded causes: kidney donation |
| E20b | Tổn thương thận mạn tính | `chronic kidney damage` | Annex 1, early, 20 | 1673 | encoded: listing; 2 thresholds (days the qualifying state has lasted, eGFR in ml per minute per 1.73 square metres of body surface) |
| E21 | Mất khả năng sống độc lập (giai đoạn sớm) | `loss of independent existence, early stage` | Annex 1, early, 21 | 1680 | encoded: listing; no number stated, the specialist's certificate carries it; excluded causes: a self-inflicted injury |
| E22 | Viêm màng não nhiễm khuẩn phục hồi hoàn toàn | `bacterial meningitis with full recovery` | Annex 1, early, 22 | 1686 | encoded: listing; no number stated, the specialist's certificate carries it; excluded causes: HIV infection |
| E23 | HIV mắc phải do bị tấn công hoặc do nghề nghiệp | `HIV infection from an assault or at work` | Annex 1, early, 23 | 1695 | encoded: listing; 3 thresholds (days from the incident to notice to the Company, days from the incident to seroconversion, days from the incident to the negative HIV antibody test) |
| E24 | Viêm não do virus phục hồi hoàn toàn | `viral encephalitis with full recovery` | Annex 1, early, 24 | 1754 | encoded: listing; no number stated, the specialist's certificate carries it; excluded causes: HIV infection |
| E25 | Sốt bại liệt (giai đoạn sớm) | `poliomyelitis, early stage` | Annex 1, early, 25 | 1761 | encoded: listing; no number stated, the specialist's certificate carries it |
| E26 | Bệnh xơ cứng bì tiến triển giai đoạn sớm | `early progressive scleroderma` | Annex 1, early, 26 | 1776 | encoded: listing; no number stated, the specialist's certificate carries it |
| E27 | Bệnh Lupus ban đỏ hệ thống dạng nhẹ | `mild systemic lupus erythematosus` | Annex 1, early, 27 | 1786 | encoded: listing; 2 thresholds (number of the listed clinical signs present, number of the listed laboratory tests positive) |
| E28 | Thiếu máu bất sản có khả năng hồi phục | `reversible aplastic anaemia` | Annex 1, early, 28 | 1809 | encoded: listing; no number stated, the specialist's certificate carries it |
| E29 | Mù 1 (một) mắt | `blindness of one eye` | Annex 1, early, 29 | 1832 | encoded: listing; 2 thresholds (visual acuity as a Snellen fraction, visual field in degrees); excluded causes: alcohol, medicines or drugs |
| E30 | Mở khí quản vĩnh viễn (hoặc tạm thời) | `permanent or temporary tracheostomy` | Annex 1, early, 30 | 1841 | encoded: listing; 1 threshold (months the qualifying state has lasted) |
| E31 | Bỏng mức độ nhẹ | `minor burns` | Annex 1, early, 31 | 1852 | encoded: listing; 1 threshold (percentage of body surface with second-degree burns) |
| E32 | Điếc cục bộ | `partial deafness` | Annex 1, early, 32 | 1856 | encoded: listing; 1 threshold (hearing loss in decibels at all frequencies) |
| E32b | Phẫu thuật huyết khối xoang hang | `cavernous sinus thrombosis surgery` | Annex 1, early, 32 | 1862 | encoded: listing; no number stated, the specialist's certificate carries it |
| E33 | Chấn thương đầu mặt cổ cần phẫu thuật phục hồi | `reconstructive surgery above the neck after an accident` | Annex 1, early, 33 1) | 1866 | encoded: listing; no number stated, the specialist's certificate carries it |
| E33x | Chấn thương tủy sống cổ do tai nạn | `cervical spinal cord injury from an accident` | Annex 1, early, 33 2) | 1883 | encoded: listing; 2 thresholds (limbs whose use is entirely lost, weeks the qualifying state has lasted) |
| E33b | Phẫu thuật máu tụ dưới màng cứng | `subdural haematoma surgery` | Annex 1, early, 33 | 1890 | encoded: listing; no number stated, the specialist's certificate carries it |
| E34 | Ghép ruột non | `small bowel transplant` | Annex 1, early, 34 first half of the heading | 1895 | encoded: listing; 1 threshold (metres of small bowel transplanted) |
| E34b | Ghép giác mạc | `corneal transplant` | Annex 1, early, 34 second half of the heading | 1895 | encoded: listing; no number stated, the specialist's certificate carries it |
| E35 | Mất khả năng sử dụng của 1 (một) chi | `loss of use of one limb` | Annex 1, early, 35 | 1901 | encoded: listing; 1 threshold (weeks the qualifying state has lasted); excluded causes: a self-inflicted injury |
| M1 | Ung thư biểu mô tại chỗ của các cơ quan cụ thể được điều trị bằng phẫu thuật triệt để | `carcinoma in situ of specified organs treated by radical surgery` | Annex 1, middle, 1 | 1920-1921 | encoded: listing; no number stated, the specialist's certificate carries it |
| M2 | Phẫu thuật mở hộp sọ để cắt bỏ toàn bộ u tuyến yên. | `craniotomy for complete removal of a pituitary tumour` | Annex 1, middle, 2 | 1946-1947 | encoded: listing; no number stated, the specialist's certificate carries it |
| M3 | Bệnh Alzheimer mức độ trung bình | `moderate Alzheimer's disease` | Annex 1, middle, 3 | 1956 | encoded: listing; 1 threshold (MMSE score out of 30); a qualitative alternative; excluded causes: a psychological or psychiatric cause without organic damage, alcohol, addictive substances |
| M4 | Bệnh Parkinson trung bình | `moderate Parkinson's disease` | Annex 1, middle, 4 | 1980 | encoded: listing; 2 thresholds (months the qualifying state has lasted, number of activities of daily living the insured cannot perform); excluded causes: medicines or drugs, toxins |
| M5 | Hội chứng khóa trong (Locked in syndrome) | `locked-in syndrome` | Annex 1, middle, 5 | 1992 | encoded: listing; 1 threshold (months the qualifying state has lasted) |
| M6 | Động kinh nặng | `severe epilepsy` | Annex 1, middle, 6 | 2004 | encoded: listing; 3 thresholds (grand mal seizures per week, months the qualifying state has lasted, number of anti-epileptic drugs prescribed); a qualitative alternative |
| M6b | Hôn mê kéo dài ít nhất 72 giờ liên tục | `coma of at least 72 continuous hours` | Annex 1, middle, 6 | 2028 | encoded: listing; 2 thresholds (days after the coma at which the permanent neurological deficit is assessed, hours without response to external stimuli); excluded causes: alcohol, medicines or drugs, addictive substances |
| M7 | Bệnh tế bào thần kinh vận động nhẹ | `mild motor neurone disease` | Annex 1, middle, 7 | 2037 | encoded: listing; no number stated, the specialist's certificate carries it |
| M8 | Bệnh xơ cứng rải rác mức độ nhẹ | `mild multiple sclerosis` | Annex 1, middle, 8 | 2045 | encoded: listing; 1 threshold (months the qualifying state has lasted); excluded causes: systemic lupus erythematosus, HIV infection |
| M9 | Loạn dưỡng cơ mức độ trung bình | `moderate muscular dystrophy` | Annex 1, middle, 9 | 2057 | encoded: listing; 2 thresholds (months the qualifying state has lasted, number of activities of daily living the insured cannot perform) |
| M10 | Phẫu thuật nội soi tim mạch | `endoscopic coronary surgery` | Annex 1, middle, 10 | 2075 | encoded: listing; no number stated, the specialist's certificate carries it |
| M11 | Bệnh động mạch vành trung bình | `moderate coronary artery disease` | Annex 1, middle, 11 | 2096 | encoded: listing; 1 threshold (number of named coronary arteries narrowed by at least 60%) |
| M12 | Phẫu thuật cắt bỏ màng ngoài tim | `pericardiectomy` | Annex 1, middle, 12 | 2109 | encoded: listing; no number stated, the specialist's certificate carries it |
| M13 | Phẫu thuật nội soi van tim | `endoscopic heart valve surgery` | Annex 1, middle, 13 | 2116 | encoded: listing; no number stated, the specialist's certificate carries it |
| M14 | Tăng áp lực động mạch phổi thứ phát mức độ nặng | `severe secondary pulmonary hypertension` | Annex 1, middle, 14 | 2135-2136 | encoded: listing; 1 threshold (NYHA class) |
| M15 | Phẫu thuật động mạch cảnh | `carotid artery surgery` | Annex 1, middle, 15 | 2153 | encoded: listing; 1 threshold (percentage narrowing of the carotid artery) |
| M16 | Phẫu thuật xâm lấn tối thiểu động mạch chủ | `minimally invasive aortic surgery` | Annex 1, middle, 16 | 2161 | encoded: listing; no number stated, the specialist's certificate carries it |
| M17 | Hen suyễn nặng | `severe asthma` | Annex 1, middle, 17 | 2174 | encoded: listing; 1 threshold (hours of continuous mechanical ventilation) |
| M18 | Xơ gan | `liver cirrhosis` | Annex 1, middle, 18 | 2190 | encoded: listing; 3 thresholds (Child-Pugh score, HAI-Knodell fibrosis score); excluded causes: alcohol, addictive substances |
| M19 | Bệnh viêm xơ chai đường mật nguyên phát mãn tính | `chronic primary sclerosing cholangitis` | Annex 1, middle, 19 | 2198-2199 | encoded: listing; no number stated, the specialist's certificate carries it |
| M20 | Bệnh thận mạn tính | `chronic kidney disease` | Annex 1, middle, 20 | 2210 | encoded: listing; 2 thresholds (eGFR in ml per minute per 1.73 square metres of body surface, months the qualifying state has lasted) |
| M21 | Mất khả năng sống độc lập (giai đoạn trung gian) | `loss of independent existence, intermediate stage` | Annex 1, middle, 21 | 2217 | encoded: listing; 2 thresholds (months the qualifying state has lasted, number of activities of daily living the insured cannot perform); excluded causes: a psychological or psychiatric cause without organic damage |
| M22 | Viêm màng não nhiễm khuẩn với di chứng thần kinh có khả năng hồi phục | `bacterial meningitis with reversible neurological deficit` | Annex 1, middle, 22 | 2225-2226 | encoded: listing; no number stated, the specialist's certificate carries it; excluded causes: HIV infection |
| M23 | HIV do cấy ghép cơ quan | `HIV infection from an organ transplant` | Annex 1, middle, 23 | 2246 | encoded: listing; no number stated, the specialist's certificate carries it |
| M24 | Viêm não do virus mức độ nhẹ | `mild viral encephalitis` | Annex 1, middle, 24 | 2260 | encoded: listing; 2 thresholds (weeks of inpatient treatment, weeks the qualifying state has lasted); excluded causes: HIV infection |
| M25 | Sốt bại liệt (giai đoạn trung gian) | `poliomyelitis, intermediate stage` | Annex 1, middle, 25 | 2269 | encoded: listing; 1 threshold (hours of continuous mechanical ventilation) |
| M26 | Bệnh xơ cứng bì tiến triển với hội chứng CREST | `progressive scleroderma with CREST syndrome` | Annex 1, middle, 26 | 2276 | encoded: listing; no number stated, the specialist's certificate carries it |
| M27 | Bệnh Lupus ban đỏ hệ thống dạng trung bình có kèm viêm thận do Lupus | `moderate systemic lupus erythematosus with lupus nephritis` | Annex 1, middle, 27 | 2300-2301 | encoded: listing; 3 thresholds (creatinine clearance per minute, number of the listed clinical signs present, number of the listed laboratory tests positive) |
| M28 | Hội chứng rối loạn sinh tủy hoặc xơ tủy | `myelodysplastic syndrome or myelofibrosis` | Annex 1, middle, 28 | 2328 | encoded: listing; no number stated, the specialist's certificate carries it |
| M29 | Teo thần kinh thị giác gây khiếm thị | `optic atrophy causing visual impairment` | Annex 1, middle, 29 | 2333 | encoded: listing; 2 thresholds (visual acuity as a Snellen fraction, visual field in degrees); excluded causes: alcohol, medicines or drugs |
| M30 | Câm do liệt dây thanh | `loss of speech from vocal cord paralysis` | Annex 1, middle, 30 | 2355 | encoded: listing; 1 threshold (months the qualifying state has lasted); excluded causes: a psychological or psychiatric cause without organic damage |
| M31 | Bỏng khuôn mặt mức độ trung bình | `moderate facial burns` | Annex 1, middle, 31 | 2366 | encoded: listing; 1 threshold (percentage of the face with third-degree burns) |
| M32 | Phẫu thuật cấy ghép ốc tai | `cochlear implant surgery` | Annex 1, middle, 32 | 2370 | encoded: listing; no number stated, the specialist's certificate carries it |
| M33 | Chấn thương sọ não cần phẫu thuật mở hộp sọ | `head injury requiring craniotomy` | Annex 1, middle, 33 | 2375 | encoded: listing; no number stated, the specialist's certificate carries it |
| M34 | Cấy ghép tủy xương hoặc các cơ quan chính (trong danh sách chờ phẫu thuật) | `bone marrow or major organ transplant waiting list` | Annex 1, middle, 34 | 2386-2387 | encoded: listing; no number stated, the specialist's certificate carries it |
| M35 | Mất khả năng sử dụng của 1 (một) chi cần phải có bộ phận giả | `loss of use of one limb requiring a prosthesis` | Annex 1, middle, 35 | 2397-2398 | encoded: listing; no number stated, the specialist's certificate carries it; excluded causes: a self-inflicted injury |
| L1 | Ung thư nghiêm trọng | `major cancer` | Annex 1, late, 1 | 2432 | encoded: listing; no number stated, the specialist's certificate carries it; excluded causes: HIV infection |
| L2 | U não lành tính | `benign brain tumour` | Annex 1, late, 2 | 2475 | encoded: listing; no number stated, the specialist's certificate carries it |
| L3 | Bệnh Alzheimer / Sa sút trí tuệ trầm trọng | `severe Alzheimer's disease or dementia` | Annex 1, late, 3 | 2490 | encoded: listing; no number stated, the specialist's certificate carries it; excluded causes: a psychological or psychiatric cause without organic damage, alcohol, addictive substances |
| L4 | Bệnh Parkinson nặng | `severe Parkinson's disease` | Annex 1, late, 4 | 2518 | encoded: listing; 2 thresholds (months the qualifying state has lasted, number of activities of daily living the insured cannot perform); excluded causes: medicines or drugs, toxins |
| L5 | Hội chứng Apallic | `apallic syndrome` | Annex 1, late, 5 | 2529 | encoded: listing; 1 threshold (months the qualifying state has lasted) |
| L6 | Hôn mê kéo dài ít nhất 96 giờ | `coma of at least 96 hours` | Annex 1, late, 6 | 2536 | encoded: listing; 2 thresholds (days after the coma at which the permanent neurological deficit is assessed, hours without response to external stimuli); excluded causes: alcohol, medicines or drugs, addictive substances |
| L7 | Bệnh tế bào thần kinh vận động nặng | `severe motor neurone disease` | Annex 1, late, 7 | 2546 | encoded: listing; no number stated, the specialist's certificate carries it |
| L8 | Bệnh xơ cứng rải rác mức độ nặng | `severe multiple sclerosis` | Annex 1, late, 8 | 2554 | encoded: listing; 1 threshold (months the qualifying state has lasted); excluded causes: systemic lupus erythematosus, HIV infection |
| L9 | Loạn dưỡng cơ | `muscular dystrophy` | Annex 1, late, 9 | 2574 | encoded: listing; 2 thresholds (months the qualifying state has lasted, number of activities of daily living the insured cannot perform) |
| L10 | Phẫu thuật não | `brain surgery` | Annex 1, late, 10 | 2582 | encoded: listing; no number stated, the specialist's certificate carries it; excluded causes: an accident or injury |
| L11 | Bệnh xơ cứng cột bên teo cơ | `amyotrophic lateral sclerosis` | Annex 1, late, 11 | 2591 | encoded: listing; no number stated, the specialist's certificate carries it |
| L12 | Bệnh nhược cơ (Myasthenia Gravis) | `myasthenia gravis` | Annex 1, late, 12 | 2599 | encoded: listing; 1 threshold (myasthenia gravis clinical class) |
| L13 | Phẫu thuật nối tắt động mạch vành | `coronary artery bypass surgery` | Annex 1, late, 13 | 2629 | encoded: listing; no number stated, the specialist's certificate carries it |
| L14 | Bệnh động mạch vành nghiêm trọng khác | `other serious coronary artery disease` | Annex 1, late, 14 | 2639 | encoded: listing; 2 thresholds (number of named coronary arteries narrowed by at least 60%, number of named coronary arteries narrowed by at least 75%) |
| L15 | Bệnh nhồi máu cơ tim được xác định là nghiêm trọng | `serious heart attack` | Annex 1, late, 15 | 2647 | encoded: listing; 1 threshold (number of the four heart attack criteria met) |
| L16 | Phẫu thuật thay thế van tim | `heart valve replacement surgery` | Annex 1, late, 16 | 2668 | encoded: listing; no number stated, the specialist's certificate carries it |
| L17 | Tăng áp lực động mạch phổi nguyên phát mức độ nặng | `severe primary pulmonary arterial hypertension` | Annex 1, late, 17 | 2681-2682 | encoded: listing; 1 threshold (NYHA class) |
| L18 | Đột quỵ | `stroke` | Annex 1, late, 18 | 2700 | encoded: listing; 1 threshold (weeks the qualifying state has lasted); excluded causes: an accident or injury |
| L19 | Phẫu thuật động mạch chủ | `aortic surgery` | Annex 1, late, 19 | 2739 | encoded: listing; no number stated, the specialist's certificate carries it |
| L20 | Bệnh cơ tim | `cardiomyopathy` | Annex 1, late, 20 | 2749 | encoded: listing; 1 threshold (NYHA class); excluded causes: alcohol |
| L21 | Hội chứng Eisenmenger | `Eisenmenger syndrome` | Annex 1, late, 21 | 2763 | encoded: listing; no number stated, the specialist's certificate carries it |
| L22 | Bệnh phổi giai đoạn cuối | `end-stage lung disease` | Annex 1, late, 22 | 2768 | encoded: listing; 2 thresholds (FEV1 in litres, resting PaO2 in mmHg) |
| L23 | Bệnh suy gan giai đoạn cuối | `end-stage liver failure` | Annex 1, late, 23 | 2794 | encoded: listing; no number stated, the specialist's certificate carries it; excluded causes: alcohol, addictive substances |
| L24 | Viêm gan siêu vi tối cấp | `fulminant viral hepatitis` | Annex 1, late, 24 | 2801 | encoded: listing; no number stated, the specialist's certificate carries it |
| L25 | Bệnh viêm tụy mãn tái phát | `chronic relapsing pancreatitis` | Annex 1, late, 25 | 2812 | encoded: listing; 1 threshold (episodes of pancreatitis); excluded causes: alcohol |
| L26 | Bệnh Crohn mức độ nặng | `severe Crohn's disease` | Annex 1, late, 26 | 2820 | encoded: listing; 1 threshold (bowel segments resected) |
| L27 | Suy thận | `kidney failure` | Annex 1, late, 27 | 2831 | encoded: listing; no number stated, the specialist's certificate carries it |
| L28 | Bệnh nang tủy thận | `medullary cystic kidney disease` | Annex 1, late, 28 | 2835 | encoded: listing; no number stated, the specialist's certificate carries it |
| L29 | Mất khả năng sống độc lập (giai đoạn cuối) | `loss of independent existence, final stage` | Annex 1, late, 29 | 2853 | encoded: listing; 2 thresholds (months the qualifying state has lasted, number of activities of daily living the insured cannot perform); excluded causes: a psychological or psychiatric cause without organic damage |
| L30 | Bệnh viêm cân cơ hoại tử (Necrotising fasciitis) | `necrotising fasciitis` | Annex 1, late, 30 | 2861 | encoded: listing; no number stated, the specialist's certificate carries it |
| L31 | Bệnh viêm đa khớp dạng thấp nặng | `severe rheumatoid arthritis` | Annex 1, late, 31 | 2871 | encoded: listing; 1 threshold (major joints affected) |
| L32 | Loãng xương nặng | `severe osteoporosis` | Annex 1, late, 32 | 2885 | encoded: listing; 3 thresholds (bone density T-score, number of activities of daily living the insured cannot perform, osteoporotic fractures of the femur, wrist or spine) |
| L33 | Viêm màng não nhiễm khuẩn với di chứng thần kinh vĩnh viễn | `bacterial meningitis with permanent neurological deficit` | Annex 1, late, 33 | 2904-2905 | encoded: listing; 1 threshold (days the qualifying state has lasted); excluded causes: HIV infection |
| L34 | HIV mắc phải do truyền máu hoặc do nghề nghiệp | `HIV infection from a blood transfusion or at work` | Annex 1, late, 34 | 2915 | encoded: listing; 3 thresholds (days from the incident to notice to the Company, days from the incident to seroconversion, days from the incident to the negative HIV antibody test); a qualitative alternative |
| L35 | Viêm não do virus mức độ nặng | `severe viral encephalitis` | Annex 1, late, 35 | 2975 | encoded: listing; 1 threshold (weeks the qualifying state has lasted); excluded causes: HIV infection |
| L36 | Bệnh sốt bại liệt | `poliomyelitis` | Annex 1, late, 36 | 2983 | encoded: listing; 1 threshold (months the qualifying state has lasted) |
| L37 | Bệnh xơ cứng bì tiến triển mức độ nặng | `severe progressive scleroderma` | Annex 1, late, 37 | 2990 | encoded: listing; no number stated, the specialist's certificate carries it |
| L38 | Bệnh Lupus ban đỏ hệ thống dạng nặng có kèm viêm thận do Lupus | `severe systemic lupus erythematosus with lupus nephritis` | Annex 1, late, 38 | 3001-3002 | encoded: listing; 2 thresholds (WHO lupus nephritis class) |
| L39 | Thiếu máu bất sản | `aplastic anaemia` | Annex 1, late, 39 | 3028 | encoded: listing; no number stated, the specialist's certificate carries it |
| L40 | Mù 2 (hai) mắt | `blindness of both eyes` | Annex 1, late, 40 | 3038 | encoded: listing; 2 thresholds (visual acuity as a Snellen fraction, visual field in degrees); excluded causes: alcohol, medicines or drugs |
| L41 | Câm | `loss of speech` | Annex 1, late, 41 | 3047 | encoded: listing; 1 threshold (months the qualifying state has lasted); excluded causes: a psychological or psychiatric cause without organic damage |
| L42 | Bỏng nặng | `major burns` | Annex 1, late, 42 | 3066 | encoded: listing; 1 threshold (percentage of body surface with third-degree burns) |
| L43 | Điếc | `deafness` | Annex 1, late, 43 | 3069 | encoded: listing; 1 threshold (hearing loss in decibels at all frequencies) |
| L44 | Chấn thương sọ não nghiêm trọng | `serious head injury` | Annex 1, late, 44 | 3077 | encoded: listing; 1 threshold (weeks the qualifying state has lasted) |
| L45 | Cấy ghép tủy xương hoặc các cơ quan chính | `bone marrow or major organ transplant` | Annex 1, late, 45 | 3097 | encoded: listing; no number stated, the specialist's certificate carries it |
| L46 | Liệt | `paralysis` | Annex 1, late, 46 | 3116 | encoded: listing; 2 thresholds (limbs whose use is entirely lost, weeks the qualifying state has lasted); excluded causes: a self-inflicted injury |
| L47 | Bệnh hiểm nghèo giai đoạn cuối | `terminal illness` | Annex 1, late, 47 | 3123 | encoded: listing; 1 threshold (months within which the illness is expected to cause death); excluded causes: HIV infection |
| L48 | Bệnh Creutzfeld – Jacob | `Creutzfeldt-Jakob disease` | Annex 1, late, 48 | 3128 | encoded: listing; 1 threshold (number of activities of daily living the insured cannot perform); excluded causes: growth hormone treatment |
| L49 | Bệnh suy tuyến thượng thận mãn tính | `chronic adrenal insufficiency` | Annex 1, late, 49 | 3136 | encoded: listing; no number stated, the specialist's certificate carries it |
| X1 | Ung thư tuyến tiền liệt, ung thư phổi hoặc ung thư gan | `prostate, lung or liver cancer` | Annex 2, men, 1 | 3148 | encoded: listing; no number stated, the specialist's certificate carries it |
| F1 | Ung thư biểu mô tại chỗ của vú, cổ tử cung, tử cung, buồng trứng, ống dẫn trứng hoặc âm đạo | `carcinoma in situ of the breast, cervix, uterus, ovary, fallopian tube or vagina` | Annex 2, women, 1 | 3180-3181 | encoded: listing; no number stated, the specialist's certificate carries it |
| F2 | Những biến chứng của thai sản | `complications of pregnancy` | Annex 2, women, 2 | 3212 | encoded: listing; 1 threshold (completed weeks of pregnancy at the fetal death); a qualitative alternative |
| F3 | Dị tật bẩm sinh | `congenital defects` | Annex 2, women, 3 | 3237 | encoded: listing; 1 threshold (days from the birth to the death of the child); a qualitative alternative |
| F4 | Phẫu thuật phục hồi | `reconstructive surgery` | Annex 2, women, 4 | 3263 | encoded: listing; 1 threshold (percentage of body surface with skin grafts after burns); a qualitative alternative |
| C1 | Bệnh teo cơ tủy sống type 1 ở trẻ em | `spinal muscular atrophy type 1` | Annex 3, 1 | 3283 | encoded: listing; no number stated, the specialist's certificate carries it |
| C2 | Viêm khớp dạng thấp nặng ở trẻ em | `severe juvenile rheumatoid arthritis` | Annex 3, 2 | 3292 | encoded: listing; 1 threshold (months the qualifying state has lasted) |
| C3 | Hemophilia nặng | `severe haemophilia` | Annex 3, 3 | 3305 | encoded: listing; 1 threshold (clotting factor VIII or IX as a percentage) |
| C4 | Bệnh thấp có tổn thương van tim | `rheumatic fever with heart valve damage` | Annex 3, 4 | 3311 | encoded: listing; 1 threshold (months the qualifying state has lasted) |
| C5 | Bệnh xương thủy tinh | `osteogenesis imperfecta` | Annex 3, 5 | 3320 | encoded: listing; no number stated, the specialist's certificate carries it |
| C6 | Đái tháo đường phụ thuộc insulin | `insulin-dependent diabetes` | Annex 3, 6 | 3343 | encoded: listing; 1 threshold (months the qualifying state has lasted) |
| C7 | Bệnh Kawasaki | `Kawasaki disease` | Annex 3, 7 | 3352 | encoded: listing; 2 thresholds (coronary artery dilation or aneurysm in mm, months the qualifying state has lasted) |
| C8 | Viêm cầu thận với hội chứng thận hư | `glomerulonephritis with nephrotic syndrome` | Annex 3, 8 | 3359 | encoded: listing; 2 thresholds (months the qualifying state has lasted, proteinuria in grams per day) |

## 3. Fork register

Each fork: the question, the readings, the one taken and why. LAW: forks name the line of the Law on Insurance Business 08/2022/QH15 aid (`../../../../../../.aids/law-08-2022-qh15.txt`). Whether that 2022 Law governs a contract under terms approved in 2019 is outside knowledge, unverified: the aid stops at Article 130 and contains no commencement or transitional article.

| # | where | question | readings | taken, and why |
| --- | --- | --- | --- | --- |
| F-T1 | throughout | What kind of day, month, year? | calendar; working days | **calendar** days, months and years: the document defines only "Năm Hợp Đồng" (one calendar year, src:82-84) and nowhere mentions working days. |
| F-1.6a | 1.6, src:62-65 | "sinh nhật vừa qua trước" the effective date or anniversary: does a birthday ON that day count? | (i) strictly before; (ii) on or before | **(i)**, the words "trước" (before); tested both sides. |
| F-1.3 | 1.3, src:36-45 | When is the 1 month to 65 Tuổi range tested? | (i) on the application day; (ii) at the effective date | **(i)**: "Vào thời điểm yêu cầu bảo hiểm". Tuổi's method (1.6) applied with the application day as anchor. |
| F-1.2 | 1.2, src:23-26 | "18 Tuổi" for the policyholder, where Tuổi is defined as the insured's age | (i) the policyholder's own completed years; (ii) the insured's Tuổi | **(i)**; (ii) is absurd (finding X-10). |
| F-3a | 3.1, src:302-304 | Is a death on the day cover "chấm dứt vào" (ends on) inside the period? | (i) no; (ii) yes | **(i)**: the period ends on that day, and the contract's cover begins. |
| F-4 | 4, src:319 | "Trong vòng hai mươi mốt (21) ngày kể từ ngày nhận Hợp Đồng" | (i) to the 21st day after receipt; (ii) to the 20th | **(i)**, day 1 being the day after receipt. |
| F-7a | 7.1(a), src:442-446 | "điều chỉnh giảm Số Tiền Bảo Hiểm phù hợp với khoản phí bảo hiểm đã đóng" | (i) in proportion to premium paid / premium due; (ii) the tariff sum the paid premium buys | **(i)**: the same as (ii) for a premium linear in the sum insured; the document states no method. |
| F-12a | 12.1, src:675-677 | "sau một (01) năm kể từ" | (i) after the first anniversary of the later date; (ii) on it | **(i)**, "sau" (after); both sides tested. |
| F-12b | 12.2, src:687-707 | When has the Company "ra quyết định chi trả" the late-stage benefit for 12.2? | (i) a decision on or before the death; (ii) by the time of the death claim | **(i)**: the cases describe the state at the death. |
| F-13a | 13.3, src:843-845 | "chấm dứt ngay khi Công Ty chấp thuận thanh toán quyền lợi này": which benefit? | (i) the late-stage benefit; (ii) each of 13.1-13.3 on its own first payment | **(i)**: (ii) contradicts the four- and two-payment limits; 31.3 says (i). |
| F-13.4a | 13.4, src:863-866; Annex 3, src:3279-3281; 14, src:896-897 | "Tuổi, được xác định vào ngày được chẩn đoán": which Tuổi? | (i) the defined Tuổi as fixed for the policy year containing the day; (ii) the age at the last birthday before that day | **(i)**: it is the defined term, and only (i) agrees with Annex 3's preamble (cover until the day before the anniversary after the 18th birthday). The same reading for Article 14. |
| F-13.4b | 13.4(b)(ii), src:859-862 | Must the mother be 18 Tuổi for her child's congenital defect? | (i) no age; (ii) 18 | **(i)**: the age is stated in limb (i) only. |
| F-13.4c | 13.4(b)(i), Annex 2 | Does the list for men cover a woman's lung or liver cancer? | (i) no, the list is "cho nam giới"; (ii) yes, "bệnh lý theo giới tính" read loosely | **(i)**. |
| F-13.5a | 13.5(a), src:879-882 | "Tuổi tại Ngày Cấp Hợp Đồng" | (i) Tuổi with the issue date as anchor; (ii) Tuổi at the effective date | **(i)**, the words. |
| F-13.5b | 13.5(b), src:883-887 | "Ngày Kỷ Niệm Hợp Đồng Năm Hợp Đồng thứ 20" | (i) the 20th anniversary, ending year 20; (ii) the 19th, starting it | **(i)**: an insured of 55 at issue reaches 75 at the 20th; (i) keeps the over-55s no earlier. Tested. |
| F-15a | 15(b)(i), src:935-936 | "Ngày Kỷ Niệm Hợp Đồng của năm cuối cùng của Thời Hạn Đóng Phí" | (i) the anniversary ending the premium term (12th/15th/20th); (ii) the one starting its last year | **(i)**: 1.9 ends the premium term at that anniversary. |
| F-15b | 15(b)(ii), src:937-946 | "nhỏ hơn 65 (sáu mươi lăm) trừ thời hạn đóng phí" | (i) issue Tuổi < 65 - premium term; (ii) under 65, except during the premium term | **(i)**; the two give the same anniversaries (after the term, up to 65); "until 65" includes the anniversary at 65. |
| F-16.4 | 16.4 and 12.2 | Are accumulated dividends paid twice on death? | (i) no: 12.2 includes them, 16.4 restates; coupons held are paid in addition; (ii) both | **(i)**. |
| F-18a | 18(a), src:1012-1014 | "sau chín mươi (90) ngày kể từ Ngày Cấp" | (i) from the 91st day after; (ii) from the 90th | **(i)**; tested on both sides. |
| F-18b | 18(b), src:1015-1018 | "vẫn còn sống ít nhất là ba mươi (30) ngày kể từ" | (i) death on the 30th day after diagnosis or later passes; (ii) the 31st | **(i)**. |
| F-18c | 18, src:1003-1005 | Does "trừ trường hợp do Tai Nạn" excuse (a) only, or (a) and (b)? | (i) both; (ii) the waiting period only | **(i)**: it stands before both limbs; Law Art 24 (LAW, line 588-591) also favours the policyholder where two readings are open. Finding X-17 shows its effect. |
| F-19a | 19.1(a), src:1027-1031 | Is the second anniversary "trong thời gian 02 (hai) năm"? | (i) no; (ii) yes | **(i)**; both sides tested. |
| F-20 | 20.2, src:1072-1073 | "sáu mươi (60) ngày sẽ được bắt đầu kể từ Ngày Đến Hạn" | (i) to the 60th day after the due date; (ii) the 59th | **(i)**. |
| F-21 | 21.1-21.2, src:1085-1107 | Which sum and which premium do the 21.2 tests compare? | as written: cash value against a period's premium, then cash value less Debt against a month's | **as written**; the case between them is a named refusal (finding X-15). |
| F-28 | 28.2, src:1245-1246 | "Trong vòng 06 (sáu) tháng đầu tiên kể từ" | (i) before the 6-month anniversary; (ii) on it too | **(i)**: "đầu tiên" (the first six months). |
| F-29a | 29.1, src:1287-1291 | The last day of "tối đa là một (01) năm, kể từ ngày xảy ra" | (i) the day one year after; (ii) the day before | **(i)**. |
| F-29b | 29.1 and Article 13 | What is "ngày xảy ra sự kiện bảo hiểm" for a critical illness? | (i) the diagnosis; (ii) the day the definition is first wholly met; (iii) the approval | **(i)**, the date the waiting and survival periods also count from. Finding X-2 shows what turns on it. |
| F-29c | 29, src:1277-1278 | The article is headed "death benefit claims procedure" | (i) 29.1 and 29.4 apply to every claim; (ii) to death claims only | **(i)**: 29.3 sits in it and is about critical illness. |
| F-29d | 29.4(i), src:1330-1334 | When must a refusal be given? | (i) within the same 30 days; (ii) no period | **(i)**: "xem xét và chi trả … chậm nhất là 30 (ba mươi) ngày". |
| F-31a | 31.3 and 13.4, src:1364-1365, 867-870 | Does approval of the late-stage benefit end the additional benefit? | (i) yes: 31 ends "Quyền lợi Bệnh lý Nghiêm trọng", and 13.5 names 13.4 among those benefits; (ii) no: 13.4 is paid "độc lập" | **(i)**, the termination clause being specific; finding X-16. |
| F-32.4 | 32.4, src:1379-1381 | Are 1.3's conditions continuing? | (i) application-time conditions; (ii) continuing | **(i)** for the operative rule; (ii) encoded separately for finding X-1. |
| F-C2 | Ch 2 preamble, src:662-664 | Where does the floor bite? | (i) on the 12.2 or 17 benefit before Debt and settlement; (ii) on the net payment | **(i)**: 12.3 and 17(d) settle accounts, they are not benefits. |
| F-CI-1 | 13.1(b)(i) etc.; Annex 1 layout | Is each separately headed condition a "Bệnh Lý Nghiêm Trọng", or each numbered item? (Item 1 of the early list groups carcinoma in situ and five early cancers.) | (i) each heading; (ii) each number | **(i)**: 1.18 defines critical illness as the illnesses, conditions or operations the annexes specify, and each heading specifies one with its own definition. Under (ii), early thyroid then early prostate cancer would be paid once. The table carries both, so (ii) is a one-line change. |
| F-CI-2 | annex numbers, e.g. src:1431, 3362 | "1.5 mm", "3.5g", "– 2.5", "1,73m2" | Vietnamese format reads a dot before three digits as grouping thousands | Dot or comma before **one or two** digits is a decimal point (1.5, 3.5, -2.5, 1.73): a thousands group always has three digits, and 1,500 mm is not a melanoma. Tested at 1.49/1.5, 3.5/3.51, -2.5/-2.51. |
| F-CI-3 | early PAH, src:1589-1590 | "tương ứng với nhóm 3" | (i) NYHA class 3 exactly; (ii) at least 3 | **(i)**, the words; class 4 is the middle and late stages'. |
| F-CI-4 | late CAD, src:2640-2642 | "Hẹp tối thiểu 75% lòng mạch của 1 (một) động mạch vành và 60% lòng mạch của 2 (hai) động mạch vành khác" | (i) one at 75% and two others at 60%: three at 60% or more, one of them at 75%; (ii) otherwise | **(i)**. |
| F-CI-5 | Annexes, excluded causes | Is "thuốc" medicine (drug-induced) or narcotics? | (i) medicines or drugs; (ii) narcotics only | **(i)**; "chất gây nghiện" (addictive substances) is listed separately in the same sentences. |
| F-CI-6 | CLL early, src:1427-1429 | RAI stage 1 or 2 | — | 1 to 2 inclusive (hand-read; marked so in the tests). |
| LAW-1 | 19.1(a) | The 2 years run from the effective date or reinstatement; Law Art 40(1)(a), line 818-820, from the first premium payment or reinstatement | — | **the document's anchor is encoded**; the conflict is not resolved. |
| LAW-2 | 29.1 | Law Art 30(2), line 711-714: time runs from knowledge where the claimant proves ignorance of the event; the document has no such rule | — | **not encoded** (the Law is not encoded); recorded. |
| LAW-3 | 6.2 | The document returns the surrender value; Law Art 22(2), line 543-553, returns the premiums less reasonable costs | — | **the document's rule is encoded**; the conflict is not resolved. |
| LAW-4 | 5.1 | The document deducts Debt; Law Art 22(3), line 554-559, returns the premiums paid, with damages | — | **the document's rule is encoded**. |
| LAW-5 | 21 | Law Art 37(4), line 787-791: no deduction of premium from the surrender value without the policyholder's consent; Article 21 makes the loan automatic | — | **the document's rule is encoded**; whether signing the terms is that consent is for a lawyer. |
| LAW-6 | 4, 20.2, 23, 29.4 | Law Art 35 (line 760-769), Art 37(2)-(3) (line 780-786) and Art 31(1) (line 719-724) give the same 21 days, 60 days, 2 years, and let an agreed payment term govern | — | consistent; nothing to resolve. |

## 4. Findings

A finding is a defect of the instrument as written. "Evidence" names the assertion in `cstd-tests-findings.l4` (or another test module) that passes on the surprising answer, or says **reading only**.

**X-1. Read literally, 32.4 ends every contract when the insured turns 66 Tuổi, or travels.** src:1379-1381 ends the contract when the insured "không còn đáp ứng các điều kiện để trở thành Người Được Bảo Hiểm như được quy định tại Điều 1.3"; 1.3 (src:36-45) requires presence in Vietnam and 1 month to 65 Tuổi. The term runs to 99 Tuổi (1.8) and the coupon falls at 75 (13.5): on the literal reading neither can be reached. Scenario: C1, 34 Tuổi in 2020; on 1 January 2052 she is 66 Tuổi. Evidence: `32.4, read literally` is TRUE on 1 January 2052 and on any day she is abroad (§`X-1`).

**X-2. A twelve-month definition meets a one-year time bar on the same day.** Kawasaki disease (src:3356-3358) requires dilation lasting 12 months from the first acute episode; loss of speech (src:3050-3051) and loss of speech from vocal cord paralysis (src:2362-2363) 12 months' continuous loss. 29.1 (src:1287-1291) allows one year from "the insured event", which the document never defines for a critical illness (F-29b). If it is the diagnosis, the definition is first met on the last day to claim. Evidence: `add months` of the diagnosis by 12 equals the 29.1 last day; 11 months does not meet the definition; a claim the next day is out of time (§`X-2`).

**X-3. Two bars block each other, so a claim for both conditions pays neither.** src:1556-1559 (mild coronary artery disease is not paid "khi phẫu thuật nội soi tim mạch … được yêu cầu quyền lợi bảo hiểm") and src:2090-2095 (endoscopic coronary surgery is not paid if "có yêu cầu quyền lợi bảo hiểm liên quan đến bệnh Động mạch vành nhẹ … hay … trung bình"); src:2105-2108 the same between moderate disease and the surgery. The bars turn on a claim being made, not paid. Evidence: both answers `not payable … barred by a claim for another condition` (§`X-3`).

**X-4. "The same illness", which sets the middle- and late-stage amounts, is defined nowhere.** src:782-785, 816-822 deduct earlier payments "cho cùng một bệnh" / "của cùng một Bệnh Lý Nghiêm Trọng"; the three lists (49, 36 and 49 conditions) are not aligned and no rule maps one stage to another. The encoding takes it as a fact the claim record states. Evidence: the same late-stage coma claim pays 250 million or 1 billion on that one input (§`X-4`).

**X-5. The comfort cash coupon can come to less than nothing.** 13.1(b)(i) allows four early payments of 25% and 13.2(b)(i) two middle payments of 50%, on different illnesses with no deduction: up to 200% of the sum insured. 13.5 (src:875-878) pays 100% of the sum insured less those benefits, with no floor. Evidence: a second middle-stage payment is still due after four early and one middle; the coupon on 2 billion received against 1 billion insured is a named refusal (§`X-5`).

**X-6. One shortfall, two consequences.** src:1206-1207: Debt with interest above the cash value lapses the contract ("mất hiệu lực", reinstatable for two years under 23); src:1386-1387: the cash value not enough for the Debt ends it ("chấm dứt"). Evidence: both TRUE on the same facts (§`X-6`).

**X-7. Any invasive melanoma is an early-stage melanoma.** src:1431-1432: "xâm lấn hoặc dưới 1.5 mm … hoặc dưới mức 3 theo Clark" joins invasive, thin and shallow by "or"; read as written the thresholds add nothing to "invasive", and a thick invasive melanoma is early-stage as well as late-stage cancer (src:2453-2454 excludes only melanoma not beyond the epidermis). Evidence: a 4 mm, Clark 5 invasive melanoma meets the early definition (§`X-7`).

**X-8. Under temporary cover an accidental death can pay less than a suicide.** src:281-298 pays the lesser of the pending sum insured and 200 million on an accidental death and returns no premium; src:305-310 returns the premiums less costs on a suicide. Evidence: sum insured 100 million and premiums 150 million: 100 million against 149 million (§`X-8`).

**X-9. An exclusion for a person the product does not have.** src:1033-1034 excludes the crimes of "Người Được Bảo Hiểm 2"; nothing in the document provides for a second insured. Evidence: applied as written, such a crime excludes the death benefit (§`X-9`).

**X-10. "Tuổi" is defined as the insured's age and used for the policyholder's.** src:62 defines Tuổi as "tuổi của Người Được Bảo Hiểm"; src:24-25 requires the individual policyholder to be "từ đủ mười tám (18) Tuổi". Reading only (fork F-1.2).

**X-11. A component of the surrender value is defined nowhere.** src:165-166 adds "Quyền lợi tiền mặt đặc biệt tích lũy (nếu có)"; no other line mentions a special cash benefit. Reading only; the encoding takes it as an input.

**X-12. Discretion without criteria.** The funeral cap may be changed through the Business Procedures (src:680-682), which the Company may change at any time with effect from notice on its website (src:203-206); reducing the sum insured is approved or refused "tùy từng thời điểm" (src:1239-1241); the occupation-change consequences are the Company's choice (src:625-632). Evidence for the first: a cap set to 0 takes the funeral benefit to 0 (§`X-12`).

**X-13. Temporary cover is silent on death by illness.** src:281-316 provide for an accidental death and for excluded causes only. Evidence: named refusal (`cstd-tests-ch1.l4`, Article 3).

**X-14. Article 6 does not provide for an innocent but material misstatement.** 6.2 (src:391-397) needs intent; 6.3 (src:416-421) needs no effect on the decision. Article 8 implies the contract can be voided for such a statement within 24 months (src:483-487) but says with what refund nowhere. Evidence: named refusal (`cstd-tests-ch1.l4`, Articles 5 and 6).

**X-15. The automatic premium loan has a case neither branch covers.** 21.1 advances the shortfall from the cash value less Debt; 21.2 tests the cash value (not less Debt) against a full period's premium (not the shortfall), then the cash value less Debt against a month's premium. Cash value 12, Debt 10, premium 10, monthly 1: no shortening, no lapse, and too little to advance. Evidence: named refusal (`cstd-tests-ch3-ch4.l4`, Article 21).

**X-16. The additional benefit is "independent", yet ends with the late-stage benefit.** src:867-870 against src:1364-1365 and 888-890 (F-31a). Evidence: a stillbirth after a late-stage approval is not paid (§`X-16`).

**X-17. An accidental critical illness need not be survived.** src:1003-1005 puts the Accident exception before both the waiting and the survival period. Evidence: death two days after an accidental coma, early-stage benefit payable (§`X-17`).

**X-18. Three anchors for "two years" or "since the start".** The waiting period, pre-existing conditions and incontestability count from the issue date (src:1012-1013, 183-184, 484-486); the suicide exclusion and the funeral benefit from the effective date (src:1028-1029, 675-676); the Law from the first premium (LAW-1). On a backdated contract they differ. Reading only.

**X-19. The tracheostomy bar is unreachable after the approval it depends on.** src:1849-1851 bars a tracheostomy already paid for under four late-stage conditions, but approving any late-stage benefit ends the critical illness benefit (src:1364-1365). It bites only when the late-stage approval comes after the tracheostomy's diagnosis. Evidence: §`X-19`, and the payment-bar test in `cstd-tests-ch2.l4`. The bar also names "chấn thương sọ não nặng" where the late list says "nghiêm trọng" (src:3077).

**X-20. Labels that disagree.** The list for women is headed "PHỤ LỤC 2" (src:3175) and footed "Phụ lục 3" (src:3225); Article 29 is headed for death claims (src:1277-1278) and governs critical illness claims (src:1310-1311); the HIV-by-transfusion definition speaks of "sản phẩm bổ trợ này" (this rider, src:2923-2924) in a main product; in the raw text Article 17 precedes Article 16 (the PDF's two-column order, src:953, 963). Reading only.

**X-21. Inconsistent severities between and within ladders.** Creutzfeldt-Jakob disease is late-stage at 2 of 6 activities of daily living (src:3131-3132), the severity of the middle-stage loss of independent existence (src:2221); every other late-stage activities test asks for 3. The middle-stage coma must be "liên tục" (continuous, src:2028) and the late-stage one need not (src:2536). Carcinoma in situ excludes CIN-3 at the early stage (src:1408) and the list for women covers it (src:3192-3194). Evidence for the first: §`X-27`.

**X-22. The free-look and early-stage refunds have no floor or no deadline.** Article 4 (src:328-331) states no period for the Company's refund and no rule where deductions exceed the premium (named refusal in the tests); 13.2 and 13.3 state none where the deduction exceeds the benefit (named refusals). Evidence: `cstd-tests-ch1.l4` and `cstd-tests-ch2.l4`.

**X-24. A change of occupation takes effect from the day it happened.** src:620-635: notified or not, the Company may terminate or exclude, effective from the change; no time limit binds its decision, so it can follow a claim. Evidence: §`X-24`.

## 5. Answer table

The benefits, as the terms state them (SA = the sum insured at the event, adjusted under Article 14 for a child under 4 where Article 14 says so).

| benefit | amount | limits | clause |
| --- | --- | --- | --- |
| temporary cover, accidental death | lesser of pending SA and 200,000,000; premiums returned instead if they exceed 200,000,000 | — | 3.1, src:281-298 |
| funeral (advance) | lesser of 10% SA and 30,000,000 (cap changeable, X-12) | death after 1 year from effective or reinstatement date | 12.1, src:668-682 |
| death, before coupon or late-stage decision | 200% SA + accumulated dividends and interest | not below premiums paid | 12.2(a)(i), src:690-695 |
| death, after coupon or late-stage decision | 100% SA + the same | not below premiums paid | 12.2(a)(ii), (b) |
| early stage | lesser of 25% SA and 500,000,000 (500,000,000 across contracts per payment) | 4 payments, 1 per condition | 13.1 |
| middle stage | lesser of 50% SA and 1,000,000,000 (same across contracts), less early for the same illness | 2 payments | 13.2 |
| late stage | 100% SA, less early and middle for the same illness | 1 payment; ends the critical illness benefit | 13.3, 31.3 |
| additional (Annexes 2, 3) | 25% SA | 1 payment | 13.4 |
| comfort cash coupon | 100% SA less early and middle received | at 75 Tuổi (issue Tuổi ≤ 55) or the 20th anniversary | 13.5 |
| maturity | SA + coupons + dividends + interest - Debt | not below premiums paid | 17 |

Article 14: Tuổi 0: 20%; 1: 40%; 2: 60%; 3: 80%; 4 and over: 100% (src:903-914).

Periods: free-look 21 days from receipt (4); grace 60 days from due date (20.2); waiting 90 days from issue or reinstatement (18(a)); survival 30 days from diagnosis (18(b)); suicide 2 years from effective date or reinstatement (19.1(a)); incontestability 24 months from issue or reinstatement (8); reinstatement within 2 years of lapse, not after maturity (23); riders within 6 months of the effective date (28.2); claim within 1 year of the event (29.1); payment within 30 days of complete documents (29.4); suit within 3 years of the dispute (30.3); critical illness cover to the anniversary at 75 Tuổi (31.2); term to the anniversary at 99 Tuổi (1.8).

## 6. What check.sh prints

Run on 2026-10-07 after the last rebuild, with `/Users/mengwong/.local/bin/l4`, `JL4_LIBRARY_PATH` unset:

```
module                                    errors satisfied  failed  refused  expected
cstd-annex-rules.l4                            0         0       0        0         0
cstd-annex-tables.l4                           0         0       0        0         0
cstd-ch1-general.l4                            0         0       0        0         0
cstd-ch2-benefits.l4                           0         0       0        0         0
cstd-ch2-conditions.l4                         0         0       0        0         0
cstd-ch3-premiums.l4                           0         0       0        0         0
cstd-ch4-claims.l4                             0         0       0        0         0
cstd-nouns.l4                                  0         0       0        0         0
cstd-tests-annex.l4                            0       245       0        0         0
cstd-tests-ch1.l4                              0        99       0        0         0
cstd-tests-ch2.l4                              0       127       0        0         0
cstd-tests-ch3-ch4.l4                          0        58       0        0         0
cstd-tests-findings.l4                         0        28       0        0         0
cstd-tests-fixtures.l4                         0         0       0        0         0
TOTAL (14 modules)                             0       557       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

`check.sh` exit 0.
557 assertions: 245 generated annex boundary tests, 99 for Chapter 1, 127 for Chapter 2, 58 for Chapters 3 and 4, 28 findings demonstrations; all satisfied.

No module is expected to fail; `check.sh`'s `expected_failed` table is unchanged (all zero).
The 10 `#TRACE` directives print residual obligations, fulfilments and breaches but are not counted; there are no `#EVAL`s.
Every named refusal the tests reach is asserted with `#ASSERT REFUSED … BECAUSE`, so it counts as satisfied, not refused.

## 7. The quote check

The gate, run from this directory over every `.l4` and `.md` file except `BRIEF.md` (the lead's file), on 2026-10-07 after this file was completed:

`python3 -I tools/vnsrc.py check ../../source/raw/manulife-cstd.txt $(ls *.l4 *.md | grep -v '^BRIEF.md$')`

```
vnsrc check: 1711 src: lines, 1190 Vietnamese runs, 0 problems
```

The brief's literal command (`*.l4 *.md`, which includes `BRIEF.md`) reports two problems, both in `BRIEF.md` (lines 1 and 23): the product's marketing name, taken from the URL path, which the raw text never prints. Nothing else:

```
vnsrc check: 1711 src: lines, 1202 Vietnamese runs, 2 problems
```

## 8. Open questions for a domain expert

1. F-CI-1: does Manulife treat each numbered item of Annex 1, or each separately headed condition, as one "Bệnh Lý Nghiêm Trọng" for the one-payment-per-condition limit?
2. X-4: how does the Company decide that an early- or middle-stage payment was "for the same illness" as a later claim? Is there a published mapping between the three lists?
3. F-29b and X-2: what date does the Company treat as "ngày xảy ra sự kiện bảo hiểm" for a critical illness, and does it accept a claim for a 12-month condition after one year from diagnosis?
4. X-1: is 32.4 ever applied after issue?
5. X-5: what is paid as the coupon when early and middle benefits received exceed the sum insured?
6. F-18c: does the Company waive the 30-day survival period for an accidental critical illness?
7. LAW-1, LAW-3, LAW-5: does the 2022 Law govern contracts under these 2019-approved terms, and if so which rule does the Company apply?
8. X-9, X-11: what are "Người Được Bảo Hiểm 2" and the "special cash benefit" in this product?

## 9. What was not done

- **The independent test pass** was not run: the brief is one session with no sub-agents. Every expected value was worked by hand from the text before it was asserted, or (the 245 annex boundary tests) derived by script from the Vietnamese words of the threshold phrases, independently of the comparator typed in the table; the same session wrote both.
- **HG1** has not been sought; no domain expert has read the encoding against the source.
- The qualitative part of the 147 annex definitions is one certified fact (§1).
- No source was fetched; nothing outside `source/raw/` and the Law aid was read.
