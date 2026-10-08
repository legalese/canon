# NOTES — contracts/insurance/vn-liberty-homecare, encoding row `legalese-2026-10-vn-05`

Liberty's home insurance wording, "QUY TẮC BẢO HIỂM NHÀ CỬA" (document code UW-RPP-W-001-06-V, the HomeCare product), encoded in L4 by one agent in one session (run `VN-05-20261006`, encoder `enc-vn-05`, 2026-10-06 to 2026-10-07), from `BRIEF.md`.
Status: **draft**.
No domain expert has read it against the source; HG1 has not been sought.

Line numbers (`src:N`) are lines of `../../source/raw/liberty-homecare.txt`, the `pdftotext -layout` rendering of the PDF (sha256 `f8c92ddb9394902a4a2b95005ea60144da59c93df850b922ecd74aba5da27969`, 18 pages, retrieved from libertyinsurance.com.vn).
Identifiers are English; the Vietnamese appears only in generated `-- src:N |` lines and in short verbatim runs, both checked by `tools/vnsrc.py`.

## 0. Build and run

- `l4`: `/Users/mengwong/.local/bin/l4`, a symlink to `~/.cabal/bin/l4`, sha256 `64bbcb157dbef2ef1020a6a75589313bba0a2aeeb807c921c5e65e62e9eca118`. It has no `--version`; no record beside it names its commit. `JL4_LIBRARY_PATH` unset.
- Command: `L4=/Users/mengwong/.local/bin/l4 ./check.sh` from this directory. A full run takes several minutes (the test modules evaluate a few hundred whole-policy questions each).
- Totals (2026-10-07, copied from the run; the full table is in §6):

```
TOTAL (14 modules)                             0       522       0        0
```
- Generated files: `homecare-tests-figures.l4` is written by `python3 -I tools/gen_figure_tests.py ../../source/raw/liberty-homecare.txt > homecare-tests-figures.l4`; every expected value in it is parsed from the quoted source line above it.
- The `-- src:N |` lines in every other module were inserted by a small template expander that calls `python3 -I tools/vnsrc.py quote ../../source/raw/liberty-homecare.txt N M` for each marker; none was typed. The expander and the templates lived in the session scratchpad and are not deposited; the modules here are complete without them, and §7 checks every quotation.

Modules:

| module | what |
| --- | --- |
| `homecare-nouns.l4` | `DECLARE` only: parties, acts, the Policy Summary, the Insured, the premises, the policy, property descriptions, causes, circumstances, losses, claims, conduct |
| `homecare-definitions.l4` | Introduction (when cover attaches); the Definitions, except the Perils, the Deductible and Actual Value; a grounds helper |
| `homecare-perils.l4` | the nine Insured Perils, each with its own exclusions and conditions |
| `homecare-general-exclusions.l4` | General Exclusions 1-9 |
| `homecare-general-conditions.l4` | General Conditions 1-14, the Deductible, the short-period scale, refunds, time-bars, and the duties as regulative rules |
| `homecare-part1.l4` | Part 1: cover, settlement, Provisions, Pairs and Sets, General Limit, Extensions 1-7, Exclusions 1-8 |
| `homecare-part2.l4` | Part 2: cover, costs, Limits, Jurisdiction, Additional Definitions, tenant's Extension, Exclusions 1-17, Conditions 1-3 |
| `homecare-part3.l4` | Part 3: temporary accommodation and rent, death benefit, domestic helper's effects |
| `homecare-test-fixtures.l4` | named cases; every Policy Summary figure in it is hypothetical |
| `homecare-tests-part1.l4` | Definitions, Perils, Part 1, General Exclusions |
| `homecare-tests-part2.l4` | Part 2 |
| `homecare-tests-part3-conditions.l4` | Part 3, General Conditions, traces of the duties |
| `homecare-tests-figures.l4` | generated: every figure the document prints, and the short-period scale row by row |
| `homecare-findings.l4` | one demonstration per finding of §4 that the encoding can show |

## 1. What is encoded and what is not

**The whole document is in scope** (brief), and every provision has a row in §2.
The encoding answers three questions about a case:

1. **Is it covered?** For each Part, a function returns the list of grounds, in source order, on which the claim fails: cover not attached, item not insured, outside a definition, outside the Period, not an Insured Peril or excluded within it, a Part exclusion, a General Exclusion, a General Condition (including the conditions precedent and time-bars). An empty list means covered, and a non-empty one names every clause that bites.
2. **How much?** Part 1: the reinstatement basis, Provisions 1-3, GC6, Pairs and Sets, the General Limit, Extensions 2-6 inside the General Limit, GC9 contribution and, last, the GC13 Deductible; Extension 7's grouping of catastrophe losses. Part 2: the per-Occurrence and Period limits, the food and drink limit, the tenant's sub-limit, costs and the proportional-costs proviso, the Deductible. Part 3: the accommodation and rent formula, the death benefit, the helper limit. GC11: the short-period scale and both refunds.
3. **Who must do what, by when?** GC4 (notice; the written claim within 30 days; the Insurer's payment, with no deadline in the document), GC4(c) and Part 2 Condition 2 (no admission), GC5, GC6, GC8, GC10, GC11, GC12, Part 1 proof of value, Part 2 Conditions 2-3, as regulative rules exercised with `#TRACE`; the 30-day and 12-month periods also as date functions.

**Input conventions** (stated in the nouns header):

- Everything the document leaves to the Policy Summary (Bản Tóm Tắt Hợp Đồng Bảo Hiểm) is a field of `The Policy Summary` with no default; a figure the Summary may omit is a `MAYBE`, and a rule that needs a missing one refuses by name (Provision 2's comparator, the Part 2 Period limit, the food and drink limit, the General Limit's sum insured).
- The facts the exclusions and carve-backs turn on are **tick-box lists** (`the property` descriptions; `the circumstances` of a loss or liability): every description or circumstance established for the case is listed, and one not listed is established not to apply. One enumeration member per phrase of the source, so a case reads as the adjuster's findings. The alternative, a record with some 120 booleans, was rejected as unreviewable; the convention is stated where the types are declared.
- Figures an adjuster states (cost of reinstatement, Actual Value, the cost had reinstatement been lawful) are inputs: the document gives no method for them (no depreciation rate, no measure of "reasonable dispatch").
- Days are calendar days (F-days). Time of day is not modelled (F-period).

**Not encoded, beyond §2's out-of-scope row:** the Law on Insurance Business is not encoded; where it fills or overrides the document it is a `LAW` note in §3.
Average (underinsurance) is not in the document and is not supplied.
Nothing was fetched; no source outside `source/raw/` and the Law aid was read.

## 2. Coverage table

Totals: **117 rows; 104 encoded, 12 inert, 1 out-of-scope, 0 reached-and-refused, 0 deferred.**
"Encoded" includes clauses whose only operative effect is a refusal or a regulative rule.

| src | heading as written | English | disposition | where |
| --- | --- | --- | --- | --- |
| 1-11 | QUY TẮC BẢO HIỂM NHÀ CỬA; Mục lục | title and contents | inert | headings of the modules |
| 15-17 | GIỚI THIỆU | what the document contains | inert | `the Introduction, as a description of the document` |
| 18-20 | GIỚI THIỆU | the Insured's duty to read the documents (no consequence stated) | inert | same |
| 21-24 | GIỚI THIỆU | when the Insurer's liability begins | encoded | `cover has attached under` |
| 25-27 | GIỚI THIỆU | whom to ask | inert | same |
| 31-32 | CÁC ĐỊNH NGHĨA | "unless the context otherwise requires" | inert | definitions module header |
| 34-43 | Hợp Đồng Bảo Hiểm | the contract and its documents (i)-(iv) | inert | `the documents that make up the Insurance Contract` |
| 49-51 | Điều Khoản Sửa Đổi Bổ Sung | endorsements | inert | definitions, comment |
| 52-54 | Giới Hạn Trách Nhiệm | Limit of Liability, per Part, in the Summary | encoded | `The Policy Summary` fields; General Limit; Part 2 limits |
| 55-56 | Người Được Bảo Hiểm | the Insured, named in the Summary | encoded | `A party`; `The Insured person` |
| 57-58 | Công Ty Bảo Hiểm | the Insurer | encoded | `the Insurer's name` |
| 59-61 | Thời Hạn Bảo Hiểm | Period of Insurance | encoded | `within the Period of Insurance of` |
| 62-65 | Bản Tóm Tắt Hợp Đồng Bảo Hiểm | Policy Summary | encoded | `The Policy Summary` |
| 66-68 | Giấy Yêu Cầu Bảo Hiểm | Proposal Form | inert | definitions, comment (its truth is GC1) |
| 69-72 | Địa Điểm Bảo Hiểm | Insured Location | encoded | `the premises are the Insured Location` |
| 73-80 | Ngôi Nhà | the Home: kind, ownership, residence, construction | encoded | `the premises are a Home under` |
| 81-89 | Ngôi Nhà bao gồm | the Home includes (a)-(d) | encoded | `the property is part of the Home` |
| 90-92, 104-105 | Ngôi Nhà không bao gồm | excludes (a), (b), (h) | encoded | same |
| 93-103 | Ngôi Nhà không bao gồm | excludes (c)-(g) | encoded | `the Home definition's exclusions (c) to (g) apply to` (F-home-c) |
| 106-110 | Chi Phí Tân Trang/Cải Tạo | Renovation Costs | encoded | `the property is Renovation Costs under` |
| 111-128 | Tài Sản Bên Trong Nhà | Contents include (a)-(e); personal effects | encoded | `the property is Contents`, `a kind of property Contents includes` |
| 129-159 | Tài Sản Bên Trong Nhà không bao gồm | Contents exclude (a)-(l) | encoded | `a kind of property Contents does not include` (F-contents-j) |
| 160-162 | Gia Đình Người Được Bảo Hiểm | the Insured's Family | encoded | `a relative is in the Insured's Family, being` (F-family) |
| 163-165 | Rủi Ro Được Bảo Hiểm | Insured Perils, chapeau | encoded | `the grounds under the Insured Perils that defeat` |
| 166-173 | Cháy | Peril 1, fire, exclusions (a)-(e) | encoded | `Peril 1, fire` |
| 174-176 | Nổ | Peril 2, explosion | encoded | `Peril 2, explosion` |
| 177-178 | Sét đánh | Peril 3, lightning | encoded | `Peril 3, lightning` |
| 179-192 | Bạo động, Đình công, Công nhân Bế xưởng, Hành động Ác ý của bất kỳ một người nào | Peril 4, limbs (a)-(e) | encoded | cause constructors; `Peril 4, riot, strike and malicious act` |
| 193-216 | nhưng loại trừ | Peril 4 exclusions (i)-(iii) | encoded | same |
| 217-220 | Động đất, núi lửa phun, giông lốc, gió xoáy, bão và lụt | Peril 5 and the flood definition | encoded | `Peril 5, earthquake, volcano, storm and flood` (F-flood) |
| 221-236 | Nhưng loại trừ tổn thất hoặc thiệt hại | Peril 5 exclusions (a)-(i) | encoded | same |
| 237-239 | Ngoài trời | "in the open" | encoded | `in the open` |
| 240-244 | Tràn nước từ bể chứa, thiết bị chứa nước hoặc đường ống dẫn nước | Peril 6, escape of water | encoded | `Peril 6, escape of water` |
| 245-259 | Rò rỉ từ hệ thống vòi phun tự động | Peril 7, sprinkler leakage | encoded | `Peril 7, sprinkler leakage` |
| 260-262 | Thiệt hại do đâm va bởi | Peril 8, impact | encoded | cause constructors; no exclusions |
| 263-268 | Việc trộm cắp hoặc toan tính trộm cắp | Peril 9, theft, forcible entry | encoded | `Peril 9, theft`, `force was used to enter or leave` |
| 269-283 | Nhưng loại trừ trộm cắp | Peril 9 exclusions (a)-(h) | encoded | `Peril 9, theft` (F-theft-c) |
| 284-285 | Mức Miễn Thường | Deductible | encoded | GC13 functions |
| 286-289 | Giá Trị Thực Tế | Actual Value | encoded | input; Provisions 1 and 3 |
| 291-299 | PHẠM VI BẢO HIỂM | Part 1 cover | encoded | `the grounds on which a Part 1 claim fails, under` |
| 301-312 | CƠ SỞ THỰC HIỆN BỒI THƯỜNG | basis of settlement (a)-(b) | encoded | input `the cost of reinstatement`; `Part 1: the cost after Provisions 1 to 3, for` |
| 313-319 | Các Quy định | Provision 1, reasonable dispatch | encoded | same |
| 320-321 | Các Quy định | Provision 2, partial loss | encoded | same; refusal without the comparator |
| 322-323 | Các Quy định | Provision 3, Actual Value until incurred | encoded | same |
| 324-328 | Cặp và Bộ | Pairs and Sets | encoded | `Pairs and Sets: the cap on` (F-pairs) |
| 330-336 | GIỚI HẠN TRÁCH NHIỆM - TỔNG QUÁT | General Limit (a)-(b) | encoded | `General Limit: what remains for` |
| 338-341 | BẰNG CHỨNG GIÁ TRỊ | proof of value | encoded | GC grounds; `Part 1: the Insured keeps proof of value` |
| 344-347 | Thay đổi và Sửa chữa | Ext 1, alterations and repairs | encoded | `Extension 1: ...` (a constant, with the input convention it implies) |
| 348-354 | Định giá | Ext 2, no inventory below 40,000,000 or 5% | encoded | `Extension 2: no inventory of undamaged property is needed for a claim of` |
| 355-367 | Phí trả cho Kiến trúc sư, Giám sát viên và Kỹ sư Tư vấn | Ext 3, professional fees, 10% of the Home | encoded | `Extension 3: ...` |
| 368-375 | Chi phí chữa cháy | Ext 4, fire fighting, 10% | encoded | `Extension 4: ...` (F-ext-base) |
| 376-386 | Dọn dẹp hiện trường sau tổn thất | Ext 5, debris removal, 10% per item | encoded | `Extension 5: ...` |
| 387-392 | Chi phí Bảo vệ Tạm thời | Ext 6, temporary protection, 10% | encoded | `Extension 6: ...` |
| 393-401 | Điều chỉnh Thời gian | Ext 7, 72 hours | encoded | `Extension 7: the number of events, for losses at hours` (F-72h) |
| 402-404 | Điều chỉnh Thời gian | no liability outside the Period | encoded | Part 1 grounds |
| 406-429 | CÁC TRƯỜNG HỢP BỊ LOẠI TRỪ | Part 1 exclusions 1-8 | encoded | `Part 1 exclusions 1 to 8 that apply to` |
| 433-442 | PHẦN 2 - TRÁCH NHIỆM CÁ NHÂN VÀ GIA ĐÌNH | Part 2 cover | encoded | `the grounds on which a Part 2 claim fails, under` |
| 443-448 | PHẦN 2 - TRÁCH NHIỆM CÁ NHÂN VÀ GIA ĐÌNH | costs and expenses | encoded | `Part 2: the amount payable, under` (F-p2-costs) |
| 450-458 | GIỚI HẠN TRÁCH NHIỆM | Part 2 limits (a)-(b) | encoded | `Part 2: the limit that binds, under` |
| 459-462 | GIỚI HẠN TRÁCH NHIỆM | proportional costs proviso | encoded | `Part 2: the amount payable, under` (F-p2-limit) |
| 464-469 | QUYỀN PHÁN QUYẾT | jurisdiction | encoded | `the Jurisdiction clause excludes` (F-jurisdiction) |
| 476-481 | Sự Cố | Occurrence | encoded | scope ground; input `unexpected and unintended by the Insured` |
| 482-484 | Thương Tật Thân Thể | Bodily Injury | encoded | `A kind of harm` |
| 485-489 | Thiệt Hại về Tài sản | Property Damage | encoded | `A kind of harm` |
| 490-497 | Người Được Bảo Hiểm | the Insured in Part 2, (a)-(c) | encoded | `an Insured under Part 2` (F-p2-relative) |
| 498-500 | Người Được Bảo Hiểm | cross liability | out-of-scope | see below |
| 501-509 | Người Được Bảo Hiểm | waiver of subrogation | encoded | `the Insurer has waived subrogation against` |
| 510-511 | Người Được Bảo Hiểm | maximum payable | encoded | `Part 2: the limit that binds, under` |
| 513-523 | CÁC ĐIỀU KHOẢN MỞ RỘNG | tenant's liability, 160,000,000 | encoded | `the tenant's liability Extension applies to` (F-tenant) |
| 525-606 | ĐIỀU KHỎAN LOẠI TRỪ | Part 2 exclusions 1-17 | encoded | `Part 2 exclusions 1 to 17 that apply to` (F-excl3) |
| 609-612 | CÁC ĐIỀU KIỆN | Part 2 Condition 1, notice and forwarding | encoded | GC4(a)-(b) grounds and the GC4 rule |
| 613-621 | CÁC ĐIỀU KIỆN | Condition 2, no admission; the Insurer may take over | encoded | `GC4(c): no admission or offer without written consent`; Part 2 powers |
| 622-626 | CÁC ĐIỀU KIỆN | Condition 3, the Insurer may pay the limit or less | encoded | `Part 2: the Insurer may take over the claim, or pay ...` |
| 628 | PHẦN 3 – QUYỀN LỢI BỔ SUNG – KHÔNG TÍNH PHÍ | Part 3 heading | inert | module header |
| 630-638 | CHI PHÍ PHÁT SINH THÊM CHO CHỖ Ở TẠM THỜI | limb 1, rent | encoded | `Part 3: the accommodation or rent payable, under` (F-p3-rent) |
| 639-652 | CHI PHÍ PHÁT SINH THÊM CHO CHỖ Ở TẠM THỜI | limb 2, accommodation | encoded | same (F-p3-trigger) |
| 653-654 | CHI PHÍ PHÁT SINH THÊM CHO CHỖ Ở TẠM THỜI | limit 10%; at most 6 months | encoded | same (F-p3-shared, F-p3-months) |
| 656-660 | BỒI THƯỜNG TỬ VONG CHO NGƯỜI ĐƯỢC BẢO HIỂM | death benefit, trigger | encoded | `the grounds on which a death benefit claim fails, under` |
| 661-662 | BỒI THƯỜNG TỬ VONG CHO NGƯỜI ĐƯỢC BẢO HIỂM | limit, lesser of 160,000,000 and 50% | encoded | `Part 3: the death benefit limit under` (F-death-amount) |
| 663 | BỒI THƯỜNG TỬ VONG CHO NGƯỜI ĐƯỢC BẢO HIỂM | ages 5-65 | encoded | grounds (F-age) |
| 664-666 | BỒI THƯỜNG TỬ VONG CHO NGƯỜI ĐƯỢC BẢO HIỂM | not for a company or with Personal Accident cover | encoded | grounds |
| 668-678 | TỔN THẤT HOẶC THIỆT HẠI ĐỐI VỚI TÀI SẢN CÁ NHÂN CỦA NGƯỜI GIÚP VIỆC | helper's effects, proviso 1 | encoded | `the grounds on which a domestic helper claim fails, under` |
| 679-681 | TỔN THẤT HOẶC THIỆT HẠI ĐỐI VỚI TÀI SẢN CÁ NHÂN CỦA NGƯỜI GIÚP VIỆC | proviso 2 | encoded | same (F-helper-2) |
| 682 | TỔN THẤT HOẶC THIỆT HẠI ĐỐI VỚI TÀI SẢN CÁ NHÂN CỦA NGƯỜI GIÚP VIỆC | limit 4,000,000 | encoded | `Part 3: the domestic helper amount payable, under` |
| 684-698, 703 | CÁC ĐIỀU KHOẢN LOẠI TRỪ CHUNG | GE 1(a)-(d) | encoded | `General Exclusion 1 applies to` (F-ge1) |
| 704-709 | CÁC ĐIỀU KHOẢN LOẠI TRỪ CHUNG | "hành động khủng bố" defined | encoded | input circumstance; comment |
| 710-713 | CÁC ĐIỀU KHOẢN LOẠI TRỪ CHUNG | suppression of (a)-(c) | encoded | `General Exclusion 1 applies to` |
| 714-717 | CÁC ĐIỀU KHOẢN LOẠI TRỪ CHUNG | burden of proof on the Insured | inert | procedural; comment |
| 718-719 | CÁC ĐIỀU KHOẢN LOẠI TRỪ CHUNG | severability | inert | comment |
| 720-724 | CÁC ĐIỀU KHOẢN LOẠI TRỪ CHUNG | GE 2, confiscation | encoded | `General Exclusions 2 to 6 apply to` |
| 725-732 | CÁC ĐIỀU KHOẢN LOẠI TRỪ CHUNG | GE 3, nuclear | encoded | same |
| 733-736 | CÁC ĐIỀU KHOẢN LOẠI TRỪ CHUNG | GE 4, asbestos | encoded | same |
| 737-741 | CÁC ĐIỀU KHOẢN LOẠI TRỪ CHUNG | GE 5, DES, dioxin, SARS, AIDS | encoded | same |
| 742-745 | CÁC ĐIỀU KHOẢN LOẠI TRỪ CHUNG | GE 6, wilful act | encoded | same |
| 746-775 | Dữ Liệu Điện Tử | GE 7(a), electronic data, write-back for fire and explosion | encoded | `General Exclusion 7(a) applies to` |
| 776-789 | Giá trị các phương tiện lưu trữ thông tin điện tử | GE 7(b), valuing data media | encoded | `General Exclusion 7(b): the value of a data medium, blank at` |
| 790-791 | CÁC ĐIỀU KHOẢN LOẠI TRỪ CHUNG | GE 8, storing goods | encoded | `General Exclusions 8 and 9 apply to` |
| 792-798 | Điều Khoản Loại Trừ Liên Quan Giới Hạn Cấm Vận | GE 9, sanctions | encoded | same |
| 802-807 | Tuân thủ thích đáng | GC1, conditions precedent | encoded | GC grounds |
| 808-810 | Mô tả Sai | GC2, misdescription | encoded | GC grounds (F-gc2) |
| 811-831 | Thay đổi | GC3, alterations (a)-(e) | encoded | GC grounds |
| 832-852 | Thủ tục Yêu cầu Bồi thường | GC4, claims procedure (a)-(g) | encoded | GC grounds; `GC4: the Insured's notice and claim, with days allowed`; `GC4(g): the last day ...` (F-gc4g) |
| 853-869, 874-875 | Quyền Của Công Ty Bảo Hiểm | GC5, the Insurer's powers | encoded | `GC5: the Insurer may take possession; ...` |
| 876-882 | Quyền Của Công Ty Bảo Hiểm | GC5, forfeiture for obstruction; no abandonment | encoded | GC grounds; same rule |
| 883-896 | Sửa Chữa và Thay Thế | GC6, reinstatement option; plans | encoded | `GC6: once the Insurer elects to reinstate, ...`; GL caps |
| 897-902 | Sửa Chữa và Thay Thế | GC6, reinstatement unlawful | encoded | input; Part 1 settlement |
| 903-908 | Mất Quyền Lợi | GC7(a), fraud, wilful act | encoded | GC grounds |
| 909-915 | Mất Quyền Lợi | GC7(b), 12 months to challenge | encoded | `GC7(b): forfeited, decided on` (F-gc7b) |
| 916-926 | Thế quyền | GC8, subrogation | encoded | `GC8: the claimant does what subrogation requires` |
| 932-938 | Đóng Góp Bồi Thường | GC9, contribution | encoded | `GC9: the rateable proportion of` (F-gc9) |
| 939-946 | Trọng tài | GC10, arbitration at VIAC | encoded | `GC10: either party may refer a dispute to VIAC`; constant (F-gc10) |
| 947-952 | Hủy bỏ Hợp đồng | GC11, cancellation by the Insurer | encoded | `GC11: the refund when the Insurer cancels, under`; effective date (F-gc11-notice, F-gc11-pro-rata) |
| 953-962 | Biểu Phí Ngắn Hạn | GC11, cancellation by the Insured; short-period scale | encoded | `the short-period scale` (data, 4 rows); refund (F-short-period, F-gc11-refund) |
| 963-971 | Các Biện pháp Đề phòng Hợp lý | GC12, reasonable precautions (a)-(e) | encoded | GC grounds; `GC12: ...` |
| 972-978 | Mức Miễn Thường | GC13, Deductible | encoded | `GC13: ...` (F-deductible) |
| 979-980 | Luật và Tập quán | GC14, Vietnamese law | encoded | `GC14: the governing law` |
| 48, 101, ... 985 | page footers | document code and page numbers | inert | not quoted |

**Out of scope, with the reason: Part 2 cross liability (src:498-500).**
Where the Insured comprises several parties, each is treated as if separately insured.
It changes an answer only for a claim made by one Insured against another, and the case model has one Insured held liable and a person injured described by facts, not by identity, so it cannot say that the injured person is a co-insured.
Encoding it needs a second Insured record and an identity comparison (phrasebook 6.6); recorded as open question 6 in §8.

## 3. Fork register

Each fork is an ambiguity the encoding had to resolve. "LAW" marks a place where the Law on Insurance Business 08/2022/QH15 (aid `.aids/law-08-2022-qh15.txt`, lines cited) fills or conflicts with the document; the Law is not encoded and no conflict is resolved silently.
Where the text read literally contradicts another clause of the same document, the reading taken is the one that gives both clauses work, and the literal reading is kept as a predicate so §4 can show it.

| ID | where | question | readings | taken, and why |
| --- | --- | --- | --- | --- |
| F-attach | Intro, 21-24 | Does either limb attach cover? | (i) the Certificate or Summary agreed, OR proposal accepted and premium paid in time; (ii) all three | (i): "trừ khi" (unless) makes the second limb apply only where the first is absent |
| F-period | 59-61, 402-404 | The Period's edges, and the hour | (i) dates, both inclusive; (ii) date and hour as Extension 7 says | (i): no hour is in any input; a loss dated on either edge is in |
| F-days | GC3, GC4, GC11, Peril 9, Part 2 excl 3 | Calendar or working days? | calendar; working | calendar: the document never says "working"; every WITHIN is in calendar days |
| F-family | 160-162 | Does "regularly living with the Insured" govern spouse and children too? | (i) all three; (ii) relatives only | (i): Part 2 limb (b) must add "whether or not living with the Insured" to reach a non-resident relative, which presupposes (i). Under Law art 24 (lines 588-591) the favourable reading differs by clause (wider Family widens Contents but also Part 2 exclusion 3), so art 24 does not settle it |
| F-home-c | 93-94 | Home exclusion (c): "các loại nhà và căn hộ" (the kinds of houses and apartments) | (i) literal: every house and apartment; (ii) establishments of those kinds | (ii): (i) empties the definition it qualifies; finding X-home-c |
| F-contents-j | 115-117, 155-157 | (a) includes "photographic/sports equipment"; (j) excludes "video/photographic/sports equipment" | (i) (j) reaches all such equipment; (ii) (j) reaches the portable kind | (ii): (j) is headed "Tài sản xách tay" (portable property); gives (a)'s words work. Finding X-personal-effects |
| F-total-si | 653, 661, Ext 4, 6 | "Total sum insured of Part 1" | the sum of the item sums insured the Summary states; a separate Summary figure | the sum; none is otherwise defined. 0 if nothing is insured |
| F-ext-base | Ext 4 (374-375), Ext 6 (391-392) | "the sum insured under this Part" | total Part 1; the affected item's | total Part 1: Ext 3 and 5 name the item where they mean it |
| F-ext-within | 330-336 with Ext 3-6 | Are Extension costs inside the sums insured? | inside; in addition | inside: the General Limit binds "Trong mọi trường hợp" (in all cases) |
| F-order | Part 1 settlement, GC9, GC13 | Order of caps, contribution and Deductible | Deductible first; caps first | caps, then GC9, then the Deductible: GC13 says "sau khi áp dụng tất cả các điều khoản và điều kiện khác" (after all other terms) |
| F-pairs | 324-328 | "a proportionate part of the sum insured on the pair or set" | parts lost over parts in set; value-weighted | parts lost over parts; no weights are given. Applies only where the Summary insures the pair or set as such |
| F-72h | 393-401 | The 72-hour period's edges; how periods are placed | closed or half-open; the Insured's choice | closed, and periods placed from the earliest uncovered loss, which gives the fewest Deductibles the Insured could choose |
| F-flood | 217-234 | Do Peril 5(g) "water or rain" and (h) "escape from any pipe" reach flood water? | (i) literally yes; (ii) no, for water that is the flood as defined | (ii): (i) withdraws the grant in the same clause; finding X-flood |
| F-theft-c | 274 | "(c) any part of the Home lent, let or sublet" | (i) theft from such a part; (ii) any theft while any part is let | (i): the limb names a part, not the Home |
| F-ge1 | 687-713 | GE1's chapeau names "any act of terrorism" before listing war, terrorism, rebellion | (i) only terrorism-connected loss is excluded; (ii) each of (a)-(c) and their suppression is excluded | (ii): the clause later speaks of "mục (a) đến (c)" (items (a) to (c)) as heads; (i) is open to the Insured under LAW art 24 (588-591); finding X-war. Limb (d) "an excluded risk" adds nothing |
| F-gc1 | 802-807 | Is every duty a condition precedent? | yes; only those GC1 names | yes, as written. LAW: art 46(1)-(2) (917-932) limits the effect of late notice to the loss it caused; art 19(3) (441-444) bars a late-notice exclusion after force majeure. Finding X-precedent |
| F-gc2 | 808-810 | "có thể bị mất hiệu lực" (may become void) | void; voidable at the Insurer's election | voidable; the election is an input. LAW: art 22(2) (543-553) requires intent; GC2 does not |
| F-gc4g | 848-852 | Counting the 30 days | day 0 the event, day 30 in time; or the event as day 1 | day 0 the event. LAW: art 30(1) (706-710) gives one year to submit; art 30(3) runs a liability claim from the third party's demand. Finding X-claim-time |
| F-gc7b | 909-915 | 12 months | calendar months by `add months` (31 May to 31 May; 29 Feb to 28 Feb) | as stated; a challenge on the last day is in time |
| F-gc9 | 932-938 | "rateable proportion" | by sums insured; by independent liability | by sums insured; the only figures the document makes available |
| F-gc10 | 939-946 | "có quyền" (has the right) to go to VIAC | optional; exclusive forum | optional. LAW: art 32 (730-734) allows arbitration by agreement |
| F-gc11-notice | 947-950 | When the Insurer's 30 days run | from sending; from receipt | from sending: "gửi ... trước 30 ngày" |
| F-gc11-pro-rata | 950-952 | Day count for the pro rata refund | days in force over days in the Period | as stated; the Period has last day minus first day plus one days |
| F-short-period | 957-962 | "Đến 3 tháng" and "Từ 3 tháng đến 6 tháng" both contain 3 months; likewise 6 | first printed row wins (30% at 3, 60% at 6); later row | first row: the reading LAW art 24 favours; "Trên 9 tháng" is strict |
| F-gc11-refund | 953-956 | Premium paid below the short-period premium | refund 0; the Insured owes more | refund 0: GC11 gives no claim for more |
| F-deductible | 972-978 | A Part with no Deductible in the Summary | none; refuse | none: the Summary is where it would be stated |
| F-p2-relative | 494-495 | Limb (b) reaches relatives not living with the Insured, though the Family is defined as those who do | relative of the Insured, resident or not; Family only | the former; otherwise its last words do nothing |
| F-jurisdiction | 464-469 | What "not first-instance judgments of a competent Vietnamese court" qualifies | judgments only; claims and actions too | judgments only: a claim settled without judgment is not reached. Finding X-appeal |
| F-excl3 | 541-547 | "đã sử dụng Ngôi Nhà" (has used the Home) | (i) any use; (ii) use as a place to live | (ii): the limb defines "usually residing". "In 60 days" read as 60 or more; "more than 90" strict. Finding X-visitors |
| F-tenant | 513-523 | Does exclusion 2 still bar liability under the tenancy agreement the Extension names? | yes; no | no, where the agreement was sent to the Insurer: the Extension names that agreement as the one it reaches |
| F-p2-costs | 443-448 | Costs inside or on top of the limit? | on top ("thêm"); inside | on top, cut by the proviso |
| F-p2-limit | 459-462 | Which limit the proviso's ratio uses | the limit that binds this claim; the per-Occurrence figure | the limit that binds (the lower of the per-Occurrence limit, what remains of the Period limit, any sub-limit) |
| F-p3-trigger | 634-636, 646-648 | "fire or another peril insured hereunder" | the Peril test and General Exclusions; a full Part 1 claim | the Peril test and General Exclusions; the Home need not be insured under Part 1 |
| F-p3-shared | 653 | One 10% limit or one per limb | one, shared | one: one limit is printed under the heading |
| F-p3-months | 654 | "Months insured: at most 6" | the denominator is 6; a Summary figure up to 6 | 6; fractions of a month allowed in the numerator, which counts up to 6 |
| F-p3-rent | 632-633 with 69-77 | Limb 1 is for a landlord not occupying the Insured Location, which is defined as the Insured's residence | (i) literal: never; (ii) the residence requirements not applied to limb 1 | (ii); finding X-rent |
| F-death-amount | 656-662 | The death benefit's amount (only a limit is printed) | the limit, as a fixed sum; an indemnity up to it, amount unknown | the limit: the clause states no measure of indemnity for a death, and LAW art 24 favours the payment |
| F-age | 663 | Age 5-65 | completed years on the day of injury, both ends in | as stated |
| F-3-months | 659-660 | "within 3 months" | calendar months from the injury, last day in | as stated, by `add months` (30 November to 28 February) |
| F-theft-death | 658 | "trộm cắp" (theft) for the death benefit | ordinary meaning; Peril 9's forcible theft | ordinary: lower case, not the defined Peril |
| F-helper-2 | 679-681 | Proviso 2: "if the property lost is part of the Contents" | as written; "had it been Contents" | as written; a helper's own effects are not Contents, so it bites only on the Insured's or Family's property |
| LAW-48 | Ext 2, 348-354 | Average (underinsurance) | not in the document | not supplied. art 48 (955-963) applies pro rata reduction where the sum insured is below market value; Extension 2 presupposes such a clause |
| LAW-31 | GC4, payment | The Insurer's time to pay | not stated | not supplied. art 31(1) (718-724): 15 days from a complete valid claim file where the contract states none |
| LAW-26 | GC11 | Cancellation without cause | as written | as written. art 26 (623-635) lists the grounds for unilateral termination |
| LAW-54 | GC8; Part 2 waiver | Subrogation against family | as written | as written. art 54(3) (1043-1049) bars recovery from the Insured's parents, spouse and children unless they caused the loss intentionally |

## 4. Findings

Defects in the instrument as written, from a hostile reading for each side. Evidence is an assertion in `homecare-findings.l4` (it passes, stating the surprising answer) or "reading only".
Ordered by how much they matter to a policyholder.

1. **X-negligence. Part 2 excludes negligence.** Exclusion 1 excludes liability "do hành động cố ý hoặc chểnh mảng" (from an intentional or negligent act) of the Insured or Family whose consequences were reasonably foreseeable (src:532-535). Foreseeable harm from carelessness is what personal liability insurance is bought for; read as written, Part 2 pays for little beyond liability without fault. Scenario: a guest trips on a rug the Insured left loose. Evidence: `homecare-findings.l4`, the claim fails on exclusion 1 alone and pays 0.
2. **X-visitors. Exclusion 3, read literally, excludes injury to every visitor.** A person "usually resides with the Insured" if that person "đã sử dụng Ngôi Nhà" (has used the Home) (src:541-543); every injured guest has. Encoded on F-excl3 reading (ii); evidence: `on its literal words, exclusion 3 treats as usually residing` `a visitor` is TRUE.
3. **X-home-c. The definition of the Home excludes houses and apartments.** "Ngôi Nhà không bao gồm (c) ... các loại nhà và căn hộ" (the kinds of houses and apartments) (src:93-94) against "căn nhà hoặc căn hộ chung cư" in the definition (src:74). Read literally, no Home is ever insured. It also excludes "căn hộ có chủ quyền theo tầng" (strata-title apartments) while admitting "căn hộ chung cư": in Vietnam most owned apartments are both (outside knowledge, unverified). Evidence: both literal predicates TRUE.
4. **X-flood. Peril 5 grants flood and takes it back.** Flood includes overflow of the public water main (src:218-220); exclusion (g) removes loss "do nước hoặc mưa gây ra" (by water or rain) unless through a storm-made opening, and (h) loss from escape of water from any pipe (src:232-234). Evidence: a flood from a burst main is excluded on the literal words, covered on F-flood.
5. **X-claim-time. A liability claim can be time-barred before it exists.** GC4(g) requires the written claim within 30 days "từ ngày xảy ra sự kiện" (from the day of the event) (src:851), and GC1 makes it a condition precedent; a third party may first claim months later. Law art 30(1) allows one year and art 30(3) runs it from the third party's demand. Evidence: a dog-bite claim whose written claim is delivered 46 days after the bite fails on GC4(g); the trace in `homecare-tests-part3-conditions.l4` shows the breach on day 31.
6. **X-precedent. Any breach of any duty defeats every claim.** GC1 (src:802-807) makes observance of every term a condition precedent; the duties include keeping purchase receipts for all insured property (src:339-341). Evidence: a fire claim on the house itself, whose value no receipt is needed to prove, pays 0 because no receipts were kept. Law art 46 and art 19(3) narrow this for late notice only.
7. **X-award. Winning at arbitration forfeits the claim after a year.** GC10: the award "có giá trị chung thẩm" (is final) (src:945-946). GC7(b)(ii): benefit is lost for claims decided by arbitration "mà không có kháng nghị" (without the Insured's challenge) within 12 months (src:913-915). A final award cannot be challenged by appeal, so every arbitrated claim, won or lost, is forfeited a year after the award. Evidence: an award of 1 August 2026, asked on 2 August 2027, is a GC7(b)(ii) ground.
8. **X-war. The war exclusion's chapeau names terrorism.** GE1 excludes loss connected with "bất kỳ hành động khủng bố nào" (any act of terrorism) and then lists war, terrorism and rebellion (src:687-697). On reading (i), open to the Insured under Law art 24, war damage with no terrorism is not excluded by GE1, and fire covers fire "dù do sự cố nổ hoặc nguyên nhân khác" (whatever the cause) (src:166). Evidence: `on reading (i), General Exclusion 1 excludes` war is FALSE.
9. **X-debris. Demolition and shoring cover is deleted for almost everyone.** Extension 5 deletes (b) and (c) "khi Ngôi Nhà hoặc các Chi Phí Tân trang/Cải tạo hoặc Tài Sản Bên Trong Nhà không được bảo hiểm" (when the Home OR the Renovation Costs OR the Contents is not insured) (src:383-384). Renovation Costs exist only for a tenant (src:106-108), so the usual owner (Home and Contents) and the usual tenant (Renovation Costs and Contents) both lose them. Evidence: TRUE for both fixture Summaries.
10. **X-rent. The rent benefit pays a landlord the definitions exclude.** Part 3 limb 1 is for rent "với tư cách là chủ nhà nhưng không sử dụng Địa Điểm Bảo Hiểm" (as landlord not occupying the Insured Location) (src:632-633), but the Insured Location is the Insured's own principal residence (src:69-72) and the Home must be used by the Insured as a residence (src:76). Evidence: on the literal words the limb cannot apply to a let house; encoded on F-p3-rent.
11. **X-personal-effects. Contents include personal effects and then exclude them.** Personal effects are things "thường được mang hoặc đeo theo người" (normally carried or worn on the person) (src:118-119); exclusion (j) removes things "thường được mang ra ngoài khỏi địa điểm bảo hiểm" (normally carried out of the insured location) (src:156-157). A handbag or a watch is both. Read literally (j) also removes all the photographic and sports equipment (a) admits (F-contents-j). Evidence: two assertions.
12. **X-vacancy. Three vacancy rules.** Escape of water is excluded for a Home "đang bỏ trống hoặc không được sử dụng" (vacant or unused) with no period (src:243); theft only after "quá 30 ngày liên tiếp" unattended (src:275); GC3(d) ends cover after "hơn 30 ngày" vacant (src:829). A family away for a weekend loses water cover only. Evidence: a three-day vacancy defeats an escape-of-water claim on Peril 6(b) and nothing else.
13. **X-atmosphere. Part 1 exclusion 2 has no storm exception.** Peril 5(i) excludes atmospheric conditions "ngoại trừ ... bão, giông bão, gió xoáy và lũ lụt" (src:235-236); Part 1 exclusion 2 excludes "tác động của ánh sáng hoặc các điều kiện về khí quyển" (src:410-411) with no exception, which an insurer can read onto any storm loss. Evidence: a typhoon loss recorded with atmospheric conditions fails on Part 1 exclusion 2.
14. **X-appeal. An appeal judgment is outside Part 2.** The indemnity does not apply to judgments "không phải là phán quyết sơ thẩm" (that are not first-instance judgments) of a competent Vietnamese court (src:465-467). A judgment on appeal is not a first-instance judgment. Evidence: an appellate judgment is a Jurisdiction ground.
15. **X-fence. Theft cover needs a walled or fenced Home.** Peril 9 covers theft "tại Ngôi Nhà có tường rào" (at a Home with a perimeter wall or fence) (src:263). An apartment in a block usually has none of its own, so the apartments the Home definition admits may have no theft cover. Evidence: an apartment not enclosed fails on Peril 9.
16. **X-sublimit. A printed sub-limit above the schedule limit.** The tenant's Extension prints "Giới hạn 160.000.000 Đồng cho mỗi Sự Cố" (src:514); the Part 2 limit is the Summary's. With a Summary limit below 160,000,000 the printed figure can never bind and tells the tenant nothing. Evidence: a hypothetical 100,000,000 limit pays 100,000,000 on a 200,000,000 claim.
17. **X-discretion. Discretion without criteria.** GC2 "có thể bị mất hiệu lực" (may become void) with no decider or test (src:809-810); GC12(e) "tất cả các đề nghị hợp lý của Công Ty Bảo Hiểm" (all reasonable recommendations of the Insurer) as a condition precedent (src:971); Actual Value's depreciation "dựa trên số năm sử dụng và tình trạng" with no rate (src:288); "tiến độ hợp lý" (reasonable dispatch) (src:317); "thương tật trầm trọng" (seriously injured) undefined (src:658); the death benefit states a limit and no amount (src:661). Reading only.
18. **X-translation. Defects of translation that change meaning.** "luật hôn nhân" (marriage law) where martial law is meant, twice (src:696-697); GE8 is a prohibition placed under "the Insurer shall not be liable for:" (src:790-791); "máy bay không lái được" (aircraft that cannot be piloted) as the Contents carve-back, where a drone or model is likely meant (src:135); GE1(d) "một rủi ro đã bị loại trừ" (an excluded risk) is circular (src:703); the helper's proviso 2 reads "if the property is part of the Contents" where "had it been" is likely meant, which makes it inert (src:679-681). Reading only.
19. **X-undefined. Capitalised terms never defined.** "Sự Kiện Bảo Hiểm" (Insured Event) is capitalised and carries Peril 4(iii) and GC4 (src:213, 833) but is defined nowhere; "Bên Mua Bảo Hiểm" (the policyholder) appears once (src:51) and the contract is otherwise between the Insured and the Insurer; "Tài sản được Bảo hiểm" (src:426, 773, 897), "Giới hạn Bồi thường" beside "Giới Hạn Trách Nhiệm" (src:636, 653), and "Bảo hiểm Tai nạn Con người" (Personal Accident), whose existence removes the death benefit (src:665), are used and not defined. Reading only.
20. **X-payment-time. The Insurer's own deadlines are missing.** The document gives the Insured 30 days to claim and 12 months to challenge, and gives the Insurer no time to assess or pay (Comparables). Law art 31(1) supplies 15 days. Evidence: the GC4 trace with the claim in on day 10 shows the Insurer's duty still standing on day 400.
21. **X-cancel. The Insurer may cancel without cause on 30 days' notice** (src:948-949); Law art 26 lists the grounds for unilateral termination. Reading only.

## 5. Answer table

The figures the document prints, where, and the rule that uses each. Everything else (sums insured, Part 1 and Part 2 limits, Deductibles, premium, Period) is the Policy Summary's and is an input.

| figure | as printed | src | rule |
| --- | --- | --- | --- |
| no inventory below | 40.000.000 Đồng or 5% of the item's sum insured, whichever is less | 349-350 | `Extension 2: ...` |
| professional fees cap | 10% of the total sum insured on the Home | 367 | `Extension 3: ...` |
| fire fighting cap | 10% of the sum insured under Part 1 | 374-375 | `Extension 4: ...` |
| debris removal cap | 10% of the sum insured on each affected item | 385-386 | `Extension 5: ...` |
| temporary protection cap | 10% of the sum insured under Part 1 | 391-392 | `Extension 6: ...` |
| one catastrophe event | 72 consecutive hours | 395 | `Extension 7: ...` |
| theft, unattended | more than 30 consecutive days | 275 | `Peril 9, theft` |
| tenant's liability | 160.000.000 Đồng each Occurrence | 514 | `the tenant's liability limit for each Occurrence, in dong` |
| usually residing | 60 days intended; more than 90 consecutive days | 545-546 | exclusion 3 |
| accommodation and rent | 10% of the total Part 1 sum insured; at most 6 months | 653-654 | `Part 3: the accommodation or rent payable, under` |
| death benefit | lesser of 160.000.000 Đồng and 50% of the Part 1 sum insured; ages 5-65; death within 3 months | 660-663 | `Part 3: the death benefit ...` |
| helper's effects | 4.000.000 Đồng in the Period | 682 | `Part 3: the domestic helper amount payable, under` |
| alterations: vacancy | more than 30 days | 829 | GC3(d) |
| written claim | 30 days from the event | 851 | GC4(g) |
| challenge a rejection or award | 12 months | 910, 914 | GC7(b) |
| Insurer's notice of cancellation | 30 days | 949 | GC11 |
| short-period scale | up to 3 months 30%; 3-6 months 60%; 6-9 months 90%; over 9 months 100% of the annual premium | 959-962 | `the short-period scale` |

Worked answers the tests assert, on the hypothetical Summary (Home 2,000,000,000; Contents 500,000,000; Part 1 Deductible 2,000,000; Part 2 limits 1,000,000,000 and 2,000,000,000; Part 2 Deductible 1,000,000; no Part 3 Deductible):

| case | answer |
| --- | --- |
| house fire, reinstatement 300,000,000, reinstated | 298,000,000 |
| the same, not reinstated, Actual Value 200,000,000 | 198,000,000 |
| partial loss, total-loss cost 250,000,000 | 248,000,000 |
| 1,900,000,000 already paid on the Home this Period | 98,000,000 |
| another policy of 2,000,000,000 on the same Home | 148,000,000 |
| layered: 2,600,000,000 cost, AV 1,200,000,000, 1,000,000,000 paid, another policy | 498,000,000 |
| fire with professional fees, debris and fire fighting | 388,000,000 |
| dog bite, damages 300,000,000, costs 70,000,000 | 369,000,000 |
| damages 1,400,000,000, costs 70,000,000 (proviso) | 1,049,000,000 |
| owner-occupier, 3 months of 6, extra cost 150,000,000 | 125,000,000 |
| death by fire within 3 months | 160,000,000 |
| Insured cancels at exactly 3 months, premium 4,000,000 | refund 2,800,000 |
| Insurer cancels after 182 of 365 days, premium 3,650,000 | refund 1,830,000 |

## 6. What `check.sh` prints

Run on 2026-10-07 with `/Users/mengwong/.local/bin/l4`, `JL4_LIBRARY_PATH` unset:

```
module                                    errors satisfied  failed  refused  expected
homecare-definitions.l4                        0         0       0        0         0
homecare-findings.l4                           0        22       0        0         0
homecare-general-conditions.l4                 0         0       0        0         0
homecare-general-exclusions.l4                 0         0       0        0         0
homecare-nouns.l4                              0         0       0        0         0
homecare-part1.l4                              0         0       0        0         0
homecare-part2.l4                              0         0       0        0         0
homecare-part3.l4                              0         0       0        0         0
homecare-perils.l4                             0         0       0        0         0
homecare-test-fixtures.l4                      0         0       0        0         0
homecare-tests-figures.l4                      0        43       0        0         0
homecare-tests-part1.l4                        0       266       0        0         0
homecare-tests-part2.l4                        0        82       0        0         0
homecare-tests-part3-conditions.l4             0       109       0        0         0
TOTAL (14 modules)                             0       522       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
exit 0
```

No failed or refused assertion is expected, and none is listed in `check.sh`'s `expected_failed`.
The rule modules, the nouns and the fixtures carry no assertions; the traces in the tests module print results (fulfilled, a breach naming its clause, or the standing duty) that `check.sh` does not count.
Every run also prints two Warnings that differing copies of `prelude` and `daydate` exist under `~/.local/share/jl4/libraries/`; the binary uses its embedded copies, and the warnings are not errors.
One test failed during development and was fixed in the test, not in the expected value: the shared fixture delivered the written claim on 20 March, which GC4(g) makes late for a loss on 1 January; the Period tests now deliver it five days after each loss.

## 7. The quote check

The gate (every `.l4` and every `.md` here except the lead's `BRIEF.md`):

```
vnsrc check: 1025 src: lines, 473 Vietnamese runs, 0 problems
```

The brief's literal command, `python3 -I tools/vnsrc.py check ../../source/raw/liberty-homecare.txt *.l4 *.md` (which also reads `BRIEF.md`), printed:

```
vnsrc check: 1025 src: lines, 487 Vietnamese runs, 0 problems
```

The first line is the gate.

## 8. Open questions for a domain expert

1. Part 2 exclusion 1: is "chểnh mảng" (negligent) a translation of "wilful" or "malicious" in the source wording, and how would a Vietnamese court treat an exclusion that removes negligence from a liability cover?
2. Home exclusion (c): which buildings does Liberty mean by "các loại nhà và căn hộ, căn hộ có chủ quyền theo tầng"; is an owned condominium apartment insurable as a Home?
3. Does Law 08/2022/QH15 art 30 (one year to submit a claim) override GC4(g)'s 30 days, and does art 46 confine the effect of a breach of GC4 to the loss the Insurer suffered?
4. GC7(b)(ii) with GC10: what is a "kháng nghị" (challenge) of a final VIAC award: a petition to set it aside?
5. The death benefit: is the amount the limit (a fixed sum), and what is "thương tật trầm trọng" (serious injury)?
6. Part 2 cross liability (src:498-500): which claims between co-insureds does Liberty pay, given exclusions 3 and 6?
7. Theft "tại Ngôi Nhà có tường rào": does an apartment in a block qualify?
8. Extension 5: was Tài Sản Bên Trong Nhà meant to be in the list of items whose absence deletes demolition and shoring?
9. Is there an average clause in the Policy Summary or an endorsement, which Extension 2 presupposes?
