# NOTES — vn-pti-comprehensive-health-gras-savoye, encoding row `legalese-2026-10-vn-16`

PTI's comprehensive health care rules through Gras Savoye ("BẢO HIỂM CHĂM SÓC SỨC KHỎE TOÀN DIỆN QUA GRAS SAVOYE"), issued under Decision 268/QĐ-PTI-BHCN of 26 September 2012, encoded in L4 by one agent in one session (run `VN-16-20261006`, agent `enc-vn-16`), from `BRIEF.md`.
Status: **draft**.
No domain expert has read it against the source; HG1 has not been sought.

## 0. Build and run

- `l4`: `/Users/mengwong/.local/bin/l4`, a symlink to a local cabal build (store entry `jl4-0.1-0ee0100b`, modified 2026-10-06 21:20), sha256 `64bbcb157dbef2ef1020a6a75589313bba0a2aeeb807c921c5e65e62e9eca118`. The binary has no `--version`. `JL4_LIBRARY_PATH` unset.
- Command, from this directory: `L4=/Users/mengwong/.local/bin/l4 ./check.sh` (run 2026-10-07; 7 min 28 s wall, one `l4` process at a time).
- Totals: **0 errors, 563 assertions satisfied, 0 failed, 0 refused**, exit 0. The full table is in section 6.
- The `.l4` files in this directory are generated: the drafts carry `--@src N M` markers that a script expands into `-- src:N |` lines with `tools/vnsrc.py quote`, and the Part V table and its 126 per-row tests are generated from the text (section 6). The scripts were kept in the encoder's scratch directory and are not part of the deposit; the generated files are the deliverable.
- Every run also prints two Warnings that differing copies of `prelude` and `daydate` exist under `~/.local/share/jl4/libraries/`; the binary uses its embedded copies, and the warnings are not errors.
- Import structure: each test module imports the rule modules it uses directly, not a chain. The whole run finished in 7.5 minutes, so the chain-of-imports remedy suggested for a sibling PTI row (each module importing only its predecessor) was not applied; it would not change any answer.

## 1. What is encoded and what is not

**The whole document is in scope and every provision has a row in section 2.**
Encoded: the 69 definitions of Part I as far as a later clause uses them; the seven benefits of Part II, each as "which event and outcome it answers" and "how much it pays"; the fourteen general conditions of Part III; the 32 general exclusions of Part IV and the second "32"; the table of injury rates of Part V (126 printed rows, generated from the text) and its six principles; the twelve extension clauses of Part VI; the claims procedure of Part VII (time limits, payment, documents); and the Annex on emergency medical transport (Benefit 7).
The three questions are put together in `pti268-decision.l4`: `the claim is covered`, `the amount payable on`, and `the amount PTI must pay on` (after Part VII's time limits).

**Inputs, never defaults.**
The document is PTI's standard rules; the contract and its schedule (`Hợp đồng bảo hiểm`, the benefit summary) are not in the sources.
Every sum insured, limit, per-day room limit, daily allowance, number of allowance days, transport level, funeral allowance, premium, rate of exchange, the benefits and extension clauses chosen, the group's size and the dates of the period are inputs (`The contract`, `The limits in the schedule`) with no default.
The only figures written in the rules are those the document states (30, 45, 60, 120, 210 and 365 days; 12 months; 24 hours; 10%, 20%, 50%, 80%, 100%; VND 500.000 and 200.000; USD 100, 50 000 and 20 000; the table's rates).
The fixtures module's figures are scenario values, labelled as such.

**Not encoded:** nothing is left out deliberately.
Some provisions are **inert**: they state no rule a fact could trigger (the title and table of contents; definitions no clause uses; the Annex's messaging and information services; the contact details of the assistance centres; the signature block; the blank claim form).
Each has a row in section 2 with the reason.
Where the document points to something it does not contain (the schedule's benefit-specific waiting periods, the territory a contract extends to, the benefit that pays prenatal checks), the encoding declines by a named `REFUSE`.

**Provenance.** The source is a mirror on a university website (hcmiu.edu.vn), not PTI's own site; its sha256 (`d2a2a62b…d72f2971`, 34 pages) pins the bytes, and nothing here says the document is PTI's current wording.
The vintage is the document as published at that URL on 2026-10-06.
The Law on Insurance Business 08/2022/QH15, read as an aid, post-dates the 2012 decision; where it bears on a clause the conflict is recorded as a `LAW:` fork and not resolved.

## 2. Coverage table

Line numbers are lines of `../../source/raw/pti-gras-savoye.txt`.
Dispositions: `encoded`, `inert` (quoted or noted, not operative), `out-of-scope`, `reached-and-refused` (encoded as a named refusal because the document, not the encoder, leaves the answer open).
Totals: **144 rows: 128 encoded, 13 inert, 3 reached-and-refused, 0 out-of-scope, 0 deferred**; 8 of the encoded rows are partly reached-and-refused (the part named in the row).

| provision (as written) | English gloss | lines | disposition | where in the L4 |
| --- | --- | --- | --- | --- |
| QUI TẮC BẢO HIỂM; Quyết định số 268 | title, issuing decision | 1-9 | inert: identification, no rule | nouns header |
| Nội dung | table of contents | 10-22 | inert: navigation | — |
| I. ĐỊNH NGHĨA (chapeau) | defined terms carry their meaning throughout | 28-33 | encoded: as the convention that identifiers carry the definitions | definitions header |
| 1. Bác sỹ | doctor | 34-38 | encoded | `counts as a doctor` |
| 2. Bệnh đặc biệt | special disease | 39-46 | encoded | `a special disease`, `A diagnosis` |
| 3. Bệnh mãn tính | chronic disease | 47-53 | inert: no clause uses the term (X6) | definitions, comment |
| 4. Bệnh viện | hospital | 54-60 | encoded | `counts as a hospital` |
| 5. Biến chứng thai sản | complication of pregnancy | 61-63 | encoded | `a complication of pregnancy`, `maternity` |
| 6. Bộ Hợp đồng bảo hiểm | the contract documents; special terms prevail | 64-72 | encoded: as the input convention (contract terms are inputs; a varied rule is declined) | definitions §6; `waiting periods varied by the contract`, `territory extended by the contract` |
| 7. Bộ phận giả | prosthesis | 73-76 | encoded: as heads of expense | `a prosthesis implanted to sustain life`, `another prosthesis` |
| 8. Vật tư tiêu hao | consumables | 77-82 | encoded: as a head of expense | `consumables` |
| 9. Vật tư thay thế | replacement materials | 83-85 | encoded: as a head of expense | `replacement materials that sustain life` |
| 10. Duy trì sự sống | sustaining life | 86-87 | encoded: in the heads of 7 and 9 | nouns |
| 11. Cấy ghép nội tạng | organ transplant; donor costs not insured | 88-93 | encoded | `excluded by definition 11`, Benefits 2, 4 |
| 12. Chăm sóc thai sản | maternity care | 94-97 | encoded | `maternity` |
| 13. Chăm sóc trẻ mới sinh | newborn care | 98-101 | reached-and-refused: no benefit grants it, the schedule is not in the sources (X7) | `Part II grants no benefit for this head of expense, ...` |
| 14. Chi phí cấp cứu khẩn cấp bằng taxi | emergency taxi | 102-104 | reached-and-refused: as 13 | same |
| 15. Chi phí nằm viện | hospitalisation costs | 105-107 | encoded | `a stay in hospital`, Benefits 2, 4 |
| 16. Chi phí Phòng bệnh hay Buồng bệnh | room charges within the daily limit | 113-117 | encoded | `the room and board allowed under` |
| 17. Chi phí y tế hợp lệ | valid medical costs | 118-120 | encoded | `on the indication of a doctor` |
| 18. Chi phí y tế thực tế | actual medical costs | 121-124 | encoded: with 17 | same |
| 19. Chủ hợp đồng bảo hiểm | policyholder | 125-127 | encoded: as a party | `the policyholder` |
| 20. Công ty bảo hiểm | the insurer | 128-129 | encoded: as a party | `PTI` |
| 21. Cơ sở y tế | medical facility | 130-134 | encoded | `counts as a medical facility` |
| 22. Dịch vụ xe cứu thương | ambulance service | 135-140 | reached-and-refused: as 13 | `an ambulance` |
| 23. Dị tật bẩm sinh | congenital defect | 141-144 | encoded: as the fact IV.A.27 turns on | circumstance |
| 24. Điều trị ngoại trú | outpatient treatment | 145-148 | encoded | `counts as outpatient treatment` |
| 25. Điều trị nội trú | inpatient treatment | 149-151 | encoded | `counts as inpatient treatment` |
| 26. Điều trị sau khi xuất viện | treatment within 45 days after discharge | 157-161 | encoded | `within the 45 days after discharge` |
| 27. Điều trị trong ngày | day treatment | 162-165 | encoded | `counts as day treatment` |
| 28. Điều trị trước khi nhập viện | tests within 30 days before admission | 166-170 | encoded | `within the 30 days before admission` |
| 29. Điều trị y tế | medical treatment | 171-173 | encoded: as `on a doctor's indication` | nouns |
| 30. Đơn bảo hiểm nhóm | group policy, ten or more | 174-177 | encoded (no clause makes it a condition) | `a group policy for a number of persons` |
| 31. Khám sức khỏe định kỳ | periodic health check | 178-181 | encoded: as the fact IV.A.16 turns on | circumstance |
| 32. Lần khám/điều trị ... | an outpatient visit; follow-ups count anew | 182-187 | encoded | `the visits counted for` |
| 33. Mạng lưới thanh toán trực tiếp | direct billing network | 188-193 | encoded | `in the direct billing network`; VII direct billing |
| 34. Mất tích | missing (court declaration after two years) | 194-204 | encoded | `the earliest day a court may declare the person missing, given` |
| 35. Nằm viện | hospital stay | 205-207 | encoded | `counts as a hospital stay` (fork F6) |
| 36. Ngày bắt đầu bảo hiểm | start date (each period) | 208-209 | encoded (fork F1; X1) | `the start date under definition 36 alone for` |
| 37. Ngày tái tục bảo hiểm | renewal date | 210-211 | encoded: in III.13 | `a change to the limit of` |
| 38. Ngày tham gia bảo hiểm | date of first joining | 212-216 | encoded | `the start date for` |
| 39. Người được bảo hiểm | insured person | 217-218 | encoded | `named as an insured person` |
| 40. Người phụ thuộc | dependant | 219-225 | encoded (forks F2-F4) | `counts as a dependant` |
| 41. Nhân viên | employee | 226-228 | encoded | `counts as an employee` |
| 42. Ốm đau, bệnh tật | illness | 229-231 | encoded: as the kind of event | `an illness` |
| 43. Phạm vi lãnh thổ | territory | 232-235 | encoded | `within the territory` |
| 44. Phẫu thuật | surgery | 236-240 | encoded: as a head of expense | `surgery` |
| 45. Phẫu thuật trong ngày | day surgery | 244-246 | encoded: surgery in a day setting | Benefit 4 |
| 46. Phòng chăm sóc đặc biệt | intensive care room | 247-252 | inert: no clause uses it (X6) | — |
| 47. Quyền lợi bảo hiểm | benefit | 253-255 | encoded: as `A benefit` | nouns |
| 48. Tai nạn | accident | 256-260 | encoded | `meets the definition of accident` |
| 49. Thương tật toàn bộ vĩnh viễn do ốm đau bệnh tật | total permanent injury from illness | 261-267 | encoded (fork F7) | `counts as total permanent injury` |
| 50. Thời gian chờ | waiting period | 268-273 | encoded: in III.8 (X30) | `a waiting period bars` |
| 51. Thời hạn bảo hiểm | period of cover | 274-277 | encoded: as input | `last day of the period of cover` |
| 52. Thuốc kê đơn của bác sỹ | prescribed medicine; vitamins capped | 278-283 | encoded | `the vitamins payable on` |
| 53. Thương tật bộ phận vĩnh viễn | partial permanent injury | 289-291 | encoded | `partial permanent injury` |
| 54. Thương tật tạm thời | temporary injury | 292-294 | inert: no clause uses it (X6) | — |
| 55. Thương tật thân thể | bodily injury | 295-300 | encoded: as the facts of the event | `An event` |
| 56. Thương tật toàn bộ vĩnh viễn | total permanent injury | 301-304 | encoded | `counts as total permanent injury` |
| 57. Tổn thương thân thể | bodily harm | 305-307 | encoded: with 55 | `An event` |
| 58. Tình trạng có sẵn/Bệnh có sẵn | pre-existing condition | 308-314 | encoded (fork F8) | `a pre-existing condition, judged at` |
| 59. Tình trạng nguy kịch | critical condition | 315-316 | encoded: Annex input | `in a critical condition` |
| 60. Giới hạn chi tiết | detailed limit | 317-319 | encoded: as schedule inputs | `The limits in the schedule` |
| 61. Hoạt động thể thao chuyên nghiệp | professional sport | 320-322 | encoded | `a professional sport` |
| 62. Hoạt động thể thao nguy hiểm | dangerous sport | 323-328 | encoded | `a dangerous sport` |
| 63. Trợ cấp hàng ngày (mở rộng - Điều kiện 5) | daily allowance (extensions) | 332-335 | encoded: in Benefit 5 (X8) | `the amount Benefit 5 pays in` |
| 64. Trợ cấp hàng ngày (chính - Điều kiện 4) | daily allowance (main) | 336-338 | encoded: in Benefit 5 (X8) | same |
| 65. Trợ cấp mai táng | funeral allowance | 339-341 | encoded | `the funeral allowance under definition 65` |
| 66. Trường hợp khẩn cấp | emergency | 342-345 | encoded: Annex input | Annex |
| 67. Vận chuyển cấp cứu | emergency transport | 346-348 | encoded: Annex | `emergency medical transport to the nearest suitable hospital` |
| 68. Vật lý trị liệu | physiotherapy | 349-352 | encoded: Benefit 6.3 | `radiation, heat or light therapy` |
| 69. Y tá chăm sóc tại nhà | home care nurse | 353-358 | encoded (days) and reached-and-refused (money; X7) | `the home nursing days payable after`; `a home care nurse` |
| II. PHẠM VI BẢO HIỂM; A- Các quyền lợi chính | scope; main benefits | 364-366 | encoded | benefits module |
| Quyền lợi 1 | death or permanent injury from accident | 367-371 | encoded | `Benefit 1`, `the amount Benefit 1 pays in` |
| Quyền lợi 2 | accident medical expenses; dental 10%, prostheses 10% | 372-380 | encoded (fork F40) | `the amount Benefit 2 allows for`, `the medical costs Benefit 2 allows in` |
| Quyền lợi 3 | death or permanent disability from illness or maternity | 381-389 | encoded | `the amount Benefit 3 pays in` |
| Quyền lợi 4 | hospital and surgery; procedures 50% | 390-402 | encoded (forks F41, F42) | `the amount Benefit 4 allows for`, `the medical costs Benefit 4 allows in` |
| B- Các quyền lợi lựa chọn; Quyền lợi 5 | optional benefits; daily allowance | 408-426 | encoded (forks F38, F43) | `the amount Benefit 5 pays in` |
| Quyền lợi 6 (1-4) | outpatient treatment of illness | 429-441 | encoded | `the amount Benefit 6 allows for` |
| Quyền lợi 7 | emergency transport, see the Annex | 442-444 | encoded | Annex module |
| III. ĐIỀU KIỆN BẢO HIỂM CHUNG (heading) | general conditions | 450-455 | inert: heading (garbled in the text rendering) | — |
| 1. Đối tượng bảo hiểm | who may be insured; ages; exclusions (a), (b) | 456-466 | encoded (fork F5) | `insurable under III.1` |
| 2. a, b | effect and period per the contract | 467-471 | encoded: as inputs | `The contract` |
| 2. c | premium within 30 days; endorsements; extraordinary payment | 472-475 | encoded | `III.2(c) the duty to pay the premium`; `an extraordinary payment is due for endorsements of` |
| 2. d | rate fixed during the period | 476-478 | inert: declaratory, nothing computes a rate | — |
| 3. Đảm bảo tái tục hợp đồng | guaranteed renewal; 15-day window | 479-488 | encoded | `renewed under III.3`, `III.3 allows payment for a loss in the 15 days after expiry` |
| 4. Hủy toàn bộ hợp đồng bảo hiểm | cancellation; 100% / 80% refunds | 489-500 | encoded (forks F17, F25) | `notice given at least 30 days before`, `the refund when` |
| 5. Hoàn phí ... giữa năm | mid-year cancellation of persons | 501-504 | encoded | `the refund of` |
| 6. Chấm dứt quyền lợi bảo hiểm | when benefits end; Benefit 1's two years | 505-514 | encoded (fork F21) | `the day cover ends under`, `Benefit 1 continues for two years after an injury in the period in` |
| 7. Phí bảo hiểm ngắn hạn | short-period premium | 515-522 | encoded; 5, 7 and 8 months reached-and-refused (X5) | `the short-period rate for a term in months of` |
| 8. Hiệu lực hợp đồng và thời gian chờ | effect; risks before cover; waiting periods; maternity proviso | 523-545 | encoded (forks F9, F10, F11, F18, F35) | `III.8 bars a condition that existed before cover in`, `a waiting period bars`, `the share paid under the maternity proviso in` |
| 9. Tiền tệ & Tỉ giá | VND; USD at the agreed rate | 546-553 | encoded | `in VND` |
| 10. Khiếu nại bồi thường gian lận | fraud | 554-560 | encoded (LAW fork L2) | `fraud bars`, `III.10 the duty to refund benefits paid on a fraud` |
| 11. Đồng bảo hiểm | other insurance | 561-565 | encoded (fork F20) | `what III.11 leaves PTI to pay of` |
| 12. Trường hợp đặc biệt | hazardous activities | 566-572 | encoded (fork F36); "v.v…" reached-and-refused | `the special cases clause bars` |
| 13. Thay đổi quyền lợi | no mid-term change of limits | 573-577 | encoded (fork F19); Benefits 1, 3, 5, 7 reached-and-refused | `a change to the limit of` |
| 14. Tranh chấp | disputes | 578-581 | encoded (LAW fork L3) | `the forum for a dispute, if` |
| IV. A. (chapeau) | exclusions apply to all conditions and extensions | 587-591 | encoded | `the general exclusions engaged by` |
| IV.A.1 to IV.A.12 | intentional acts ... mental illness | 592-620 | encoded (forks F14, F16) | `the general exclusion engaged by` |
| IV.A.13 | indicated or injured before the start date | 621-623 | encoded | `exclusion 13 is engaged by` |
| IV.A.14 to IV.A.32 | reproduction ... epidemics | 624-668 | encoded (fork F15) | `the general exclusion engaged by` |
| IV.A.32 (the second) and its table | special or pre-existing disease in the first year | 674-680 | encoded (forks F11, F12, F33) | `the second exclusion 32 is engaged by` |
| V. BẢNG TỈ LỆ THƯƠNG TẬT, items 0 (I) to 93 | the table: 126 printed rows | 686-853 | encoded (generated; X11, X14) | `the table of injury rates` |
| NGUYÊN TẮC 1) | loss of function counts as loss | 861-862 | encoded: as the input convention (the claim names the row) | injury-table comment |
| NGUYÊN TẮC 2) | unlisted injuries by comparison | 863-864 | encoded: the assessed rate is an input (X13) | `an injury not listed in the table` |
| NGUYÊN TẮC 3), 4) | lowest rate; up to highest | 865-870 | encoded | `the rate under principles 2 to 4 for` |
| NGUYÊN TẮC 5) | several injuries; same limb | 871-875 | encoded (fork F23) | `the total rate for`, `the amount under the table on` |
| NGUYÊN TẮC 6) | re-operation, 50% of the lowest | 876-878 | encoded; unlisted case reached-and-refused (F22) | `the rate for` |
| VI. ĐIỀU KHOẢN MỞ RỘNG (chapeau) | only if named in the contract | 884-890 | encoded | `the contract carries` |
| VI.1 | automatic additions and deletions | 891-910 | encoded (forks F24, F25) | `the date VI.1 gives effect to`, `the pro rata premium VI.1 charges or refunds for` |
| VI.2 | premium payment warranty | 911-925 | encoded (fork F26) | `the day cover ends under the warranty, for`, `the premium PTI earns when the warranty terminates` |
| VI.3 | traditional medicine, 20% | 926-936 | encoded (fork F28) | `traditional medicine VI.3 covers`, `the traditional medicine cap under` |
| VI.4 | food or drink poisoning | 937-940 | encoded | `poisoning deemed an accident by VI.4` |
| VI.5 | strikes, riots, civil commotion | 941-955 | encoded (fork F29; X17, X18) | `VI.5 lifts the strike exclusion under` |
| VI.6 | suffocation, drowning | 956-960 | encoded (fork F30) | `suffocation covered by VI.6` |
| VI.7 | hijacking | 961-967 | encoded (X18) | `hijacking covered by VI.7` |
| VI.8 | occupational disease, 21 listed | 968-997 | encoded (fork F31; X10) | `an occupational disease within VI.8` |
| VI.9 | unscheduled flights | 998-1001 | inert: declaratory, IV.A.6 already spares a ticketed passenger (X18) | extensions comment |
| VI.10 | murder and assault | 1002-1006 | encoded (X18) | `an assault covered by VI.10` |
| VI.11 | disappearance | 1007-1013 | encoded (fork F32; X4) | `a death deemed by VI.11`, `VI.11 the payees' undertaking ...` |
| VI.12 | routine prenatal checks, groups of 50+ | 1014-1020 | encoded; amount reached-and-refused (X19) | `VI.12 covers routine prenatal checks under` |
| VII. general information | documents free, at the insured's cost, originals | 1028-1042 | inert: procedural, no consequence stated | claims comment |
| VII. direct billing: services, TPA duties | the network and its guarantee | 1043-1055, 1065-1067 | encoded | `what the insured pays the hospital of` |
| VII. direct billing: the insured's duties | card and ID; under 14; sign; pay the excess | 1056-1064 | encoded | `a copy of the birth certificate stands for ...`, `VII the insured's duty to pay what direct billing does not cover` |
| VII. Thời hạn nộp hồ sơ | 120 days; supplements 120; one year; refusal | 1072-1082 | encoded (forks F44, F49; LAW L5) | `the claim file is in time in`, `VII the duty to submit the claim file` |
| VII. accident notice | written notice within 120 days | 1083-1087 | encoded (LAW fork L4) | `the accident was notified in time in` |
| VII. documents within 12 months | accident documents; part or all refused | 1088-1091 | encoded (fork F45); amount reached-and-refused | `the accident documents were sent in time in` |
| VII. Thời gian thanh toán | payment in 10-15 working days | 1092-1093 | encoded (fork F46) | `the last day for PTI to pay a file complete on`, `VII PTI's duty to pay ...` |
| VII. Hồ sơ bồi thường I, II, III | the documents | 1094-1143 | encoded (fork F50) | `the documents Part VII asks for in` |
| VII. Chú ý (VAT invoice) | VAT invoice from VND 200.000 | 1144 | encoded | `lacks the VAT invoice it needs` |
| signature block | deputy general director | 1145-1151 | inert: execution | claims comment |
| GIẤY YÊU CẦU BỒI THƯỜNG | the claim form | 1155-1225 | inert: a blank form; its fields are this encoding's inputs | claims comment |
| PHỤ LỤC (intro) | transport cover; 90 days; US$50.000 | 1231-1237 | encoded (fork F47) | `Benefit 7 responds to`, `the Annex's limit for a period of cover, in US dollars` |
| Annex I. ĐỊNH NGHĨA | residence | 1238-1241 | encoded: as the reference of an input | `consecutive days away from the declared residence` |
| Annex II.1, II.2 | messages; information | 1243-1253 | inert: services, no money | annex comment |
| Annex II.3 | guarantee of hospital costs | 1254-1262 | encoded (fork F51) | `the assistance company may guarantee hospital costs under` |
| Annex II.4 | emergency transport and its conditions | 1263-1282 | encoded (fork F48; X2) | `the conditions of the service are met for` |
| Annex II.5 | transport home | 1283-1289 | encoded | same |
| Annex II.6 | remains or burial | 1290-1294 | encoded | same |
| Annex III.1 | call at once, with information | 1295-1309 | encoded (the information); centres' details inert | `the call gives what III.1 asks` |
| Annex III.2 | life threatened | 1310-1314 | inert: "as soon as possible", no measurable duty | annex comment |
| Annex III.3 | notify within 24 hours | 1315-1323 | encoded; the insured's share reached-and-refused | `Annex III.3 the duty to notify an admission` |
| Annex III.4 | information; access; no assistance | 1324-1334 | encoded | `III.4 leaves assistance open after` |
| Annex VI. table | Level A, Level B | 1335-1341 | encoded | `the yearly limit in US dollars at` etc. |

## 3. Fork register

Each row: where, the question, the readings, the one taken and why. Forks tagged `LAW:` cite `/Users/mengwong/src/legalese/commonswt/vn-insurance/.aids/law-08-2022-qh15.txt` by line; that Law (2022) post-dates the document (2012) and is read as an aid, not encoded.

| # | where (lines) | the question | readings | taken, and why |
| --- | --- | --- | --- | --- |
| F1 | defs 36, 38 (208-216) | Is the start date the first day of each period, or the date of first joining? | (i) def 36: each period; (ii) def 38: first joining while continuously renewed | **(ii)**: def 38's second sentence only makes sense if continuous contracts run from first joining; (i) would make every condition from year 1 pre-existing in year 2 (X1). |
| F2 | def 40 (219-225) | "đến 70 tuổi", "đến 18 tuổi", "24 tuổi": inclusive? | (i) up to and including that age; (ii) until that birthday | **(i)**, in completed years; III.1's "bắt đầu tuổi 71" agrees for 70. |
| F3 | def 40 (222-223) | Does "chưa kết hôn" (unmarried) qualify the 18 limb too? | (i) the 24 limb only; (ii) both | **(i)**: it follows "khóa học dài hạn" in the 24 limb. |
| F4 | III.1, def 40 | How are ages counted? | completed years and months; age attained in the year | **completed years and months**, measured at the date cover began in the period. |
| F5 | III.1 (461-463) | "bắt đầu tuổi 66" | (i) having reached 66; (ii) entering the 66th year (65 completed) | **(i)**. |
| F6 | def 35 (205-207) | "quá 24 giờ liên tục và điều trị trong ngày" joined by "và" | (i) union; (ii) conjunction (impossible) | **(i)**; X23. |
| F7 | defs 49, 56; V.II | Does a listed total-injury row (items 1-7) need def 56's 52 weeks? | (i) no; (ii) yes | **(i)**: def 49 makes listing sufficient, and the table prints 100% either way. |
| F8 | def 58(a) (311) | "3 năm gần đây": the 3 years before what? | (i) before the start date; (ii) before the claim | **(i)**. |
| F9 | III.8 ¶2 (526-529) | What is a risk arising before cover? | (i) only a pre-existing condition as def 58 defines it; (ii) any condition whose onset precedes the start | **(i)**: def 58 is the document's own test; (ii) bars latent conditions the insured never knew of. |
| F10 | III.8 (530-541) | How is "30 ngày tính từ" counted? | (i) the start date is day 1; (ii) from the next day | **(i)**: the reading more favourable to the insured (LAW: line 588-591, art 24). |
| F11 | III.8 (534), IV.A second 32 (674-680) | Special and pre-existing disease: 365 days, or the group table? | (i) the table governs Benefits 4 and 6 in groups of 30+; (ii) both apply | **(i)**: specific over general; under (ii) the table would never shorten anything (X3). |
| F12 | IV.A second 32 | A group under 30 | (i) the sentence's "first policy year"; (ii) no exclusion | **(i)**. |
| F14 | IV.A | Ambiguous exclusions | narrow; wide | **narrow** (LAW: line 588-591, art 24). |
| F15 | IV.A.28 (661-662) | Does "Tham gia tập luyện hoặc tham gia thi đấu" govern all three objects? | (i) yes: training or competing only; (ii) only professional sport | **(i)**, the grammatical reading and F14; a leisure parachute jump is not excluded. |
| F16 | IV.A.2 (593-595) | A traffic offence by a child under 14 | (i) not excluded; (ii) excluded by the general "law" limb | **(i)**: otherwise the age limit is empty. |
| F17 | III.4 (490-491) | "trong vòng 30 ngày trước ngày hủy" | (i) at least 30 days' notice; (ii) any time within the 30 days before | **(i)**; X21. |
| F18 | III.8 proviso (542-545) | Days insured | start date as day 1; the next day | **start as day 1**, as F10. |
| F19 | III.13 (574) | "quyền lợi 3 (Chi phí y tế do tai nạn)" | (i) Benefit 2 by description; (ii) Benefit 3 by number | **(i)**: III.13's other two items are medical-expense benefits too; X8. |
| F20 | III.11 (563-565) | Excess or proportion: who chooses? | larger; smaller; refuse | **the larger** (LAW: line 588-591, art 24); X22. |
| F21 | III.6 (510-514) | "thương tât toàn phần"; two years from when? | def 56 TPD, from the injury | as stated. |
| F22 | V principle 6 (876-878) | Re-operation of an unlisted injury | no scale; use the assessed rate | **declined** by name. |
| F23 | V principle 5 (874-875) | "tỉ lệ mất chi đó": lowest or highest rate of items 8 and 27? | lowest; highest | **highest** (70%). |
| F24 | VI.1 (896-898) | Is monthly notice a condition of the automatic cover? | condition; separate duty | **condition** ("với điều kiện"). |
| F25 | III.4, III.5, VI.1 | Pro rata how? | days; months; the short-period scale | **days**. |
| F26 | VI.2 (912-924) | "điều kiện tiên quyết" vs "không phương hại tới bất kỳ trách nhiệm nào đã phát sinh trước" | (i) no liability before payment; (ii) liability before termination preserved | **(ii)**: the clause's specific consequence; X16. |
| F27 | II "theo giới hạn đã lựa chọn" | Limit per event or per period? | aggregate per period; per event | **aggregate per period**; amounts paid before are an input. |
| F28 | VI.3 (930-936) | The 20% cap; Đông y without VI.3 | (i) cap on all traditional medicine, none without VI.3; (ii) cap on outpatient only | **(i)**. |
| F29 | VI.5, IV.A.8 | Does VI.5 lift the strike exclusion? | yes ("dù có bất kể điều gì trái ngược"); no ("Chiểu theo ... các loại trừ") | **yes**; X17. |
| F30 | VI.6 | Suffocation without a visible external force | counts as accident under VI.6; not | **counts**. |
| F31 | VI.8 | Does VI.8 deem occupational disease an accident? | no (contrast VI.4); yes | **no**. |
| F32 | VI.11 (1007-1010) | "bị mất tích" | def 34's court declaration; ordinary sense | **def 34**; X4. |
| F33 | IV.A second 32 table | A group over 50 is also "30 or more" | the "trên 50" row | **the "trên 50" row**. |
| F34 | III.7 (515-522) | Rows as exact terms or bands | exact; bands | **exact**; others declined (X5). |
| F35 | III.8 | Which day the wait tests | the day of the loss; the onset | **the day of the loss**. |
| F36 | III.12 (567-569) | Are climbing and surfing caught only as professional competitions? | no, in their own right; yes | **in their own right**: "và quyền anh" closes the example list. |
| F37 | VI.12 | Under which benefit? | Benefit 6 for cover; amount declined | as stated; X19. |
| F38 | Benefit 5 (411-412) | "bảo hiểm tai nạn" | Benefit 1 or 2 | as stated. |
| F39 | defs 26, 28; VII I.2, I.4 | Are pre- and post-hospital costs paid? | with the stay's benefit; not at all | **with the stay**, as Part VII's documents presume. |
| F40 | Benefit 2 (373-375) | Closed list? | closed outside a stay; open | **closed**; X24. |
| F41 | Benefit 4 (399-400) | A diagnostic procedure | paid as a test; not paid | **as a test**. |
| F42 | Benefit 4 | Consumables outside surgery | surgery costs | as stated. |
| F43 | Benefit 5 | Days chosen: per claim or per year | per claim | as stated. |
| F44 | VII (1073-1077) | Last day of treatment for a claim with no treatment | the day of the loss | as stated. |
| F45 | VII (1088-1091) | The 12-month limit | accident claims only | as stated. |
| F46 | VII (1092) | 10 or 15 working days; which days | 15; Mon-Fri, holidays an input | as stated. |
| F47 | Annex (1234-1235) | 90 days | days away at the event; length of the trip | **days away at the event**. |
| F48 | Annex II.4 (1279-1282) | "nơi xảy ra tai nạn" for an illness | where the illness struck; never | **where it struck**; X2. |
| F49 | VII heading (1070-1071) | Do the time limits bind a direct-billing claim? | no; yes | **no**. |
| F50 | VII III.3 (1140-1143) | Leave and death papers under "traffic accident" | any accident; traffic only | **any**. |
| F51 | Annex II.3 | "đơn chính bảo hiểm chi phí y tế" | Benefit 4 or 2 | as stated. |
| L2 | III.10 (554-560) | Premium refund on fraud | LAW: line 543-553 (art 22(2)) requires a refund less costs | **as written** (no refund); conflict recorded. |
| L3 | III.14 (578-581) | Forum | LAW: line 730-734 (art 32) also allows mediation or arbitration | **as written** (court). |
| L4 | VII (1083-1087) | Late accident notice with force majeure | LAW: line 441-444 (art 19(3)) forbids applying a late-notice exclusion then | **as written** (no exception); conflict recorded. |
| L5 | VII (1072-1080) | 120 days to submit | LAW: line 706-710 (art 30) sets one year from the insured event | **as written** (120 days); conflict recorded. |

**54 forks**: F1-F51 (F13 unused, merged into F30) and the four LAW forks L2-L5 (there is no L1).

## 4. Findings

The hostile reading. Each finding gives the lines, a minimal scenario and the evidence: an assertion in `pti268-findings.l4` (or another tests module), or "reading only".
**31 findings**: 20 shown by assertions (X1-X5, X7, X9-X11, X16, X18, X19, X22-X29), 11 reading only (X6, X8, X12-X15, X17, X20, X21, X30, X31).

| # | lines | finding | minimal scenario | evidence |
| --- | --- | --- | --- | --- |
| X1 | 208-216, 308-314, 526-529 | Def 36 makes the start date the first day of EACH period; read alone, every condition first appearing in year 1 is "pre-existing" at the year-2 renewal and barred by III.8 unless pre-existing cover was bought. Def 38 implies the opposite. | Joined 1 January 2025; condition June 2025; claim June 2026. | findings §X1: pre-existing at def 36's date, not at def 38's; covered on F1. |
| X2 | 1234, 1279-1282 | The Annex covers accident or illness, but its transport condition requires the treatment to be unavailable "where the accident happened": on its words no illness ever qualifies. | A stroke 200 km from home. | findings §X2: the literal rule answers FALSE for the illness, TRUE for an accident. |
| X3 | 534, 674-680 | III.8 waits 365 days for special and pre-existing disease; IV's second 32 gives 6 months (or none) by group size. Applied together, the table never relieves anyone. | Hepatitis, employee in a group of 40, stay in month 8. | findings §X3: covered on F11; 212 days < 365 under III.8. |
| X4 | 194-204, 1007-1013, 1072-1091 | A disappearance can be claimed only after a court declaration two years after the last news (def 34), but accident documents are due within 12 months and any file within a year. | Vanished 1 March 2026. | findings §X4: earliest declaration 1 March 2028, after 1 March 2027. |
| X5 | 515-522 | The short-period scale gives 8 months twice (7/8 and 100%) and nothing for 5 or 7 months. | An 8-month contract. | tests-parts: REFUSED at 8, 5 and 7. |
| X6 | 47-53, 247-252, 292-294 | Defs 3 (chronic disease), 46 (intensive care) and 54 (temporary injury) are never used. | — | reading only. |
| X7 | 98-104, 135-140, 353-358, 443, 602 | Newborn care, emergency taxi, ambulance and home nursing are defined (home nursing with a 15-day limit), Benefit 7 calls itself "independent of the ambulance service in Benefit 4", and exclusion 5 spares vaccinations "under the newborn care benefit" — but no benefit grants any of them. | A taxi fare to hospital. | tests-claims §Scenario 3: REFUSED. |
| X8 | 332-338, 574 | III.13 calls accident medical expenses "quyền lợi 3"; defs 63-64 number the benefits as "Điều kiện 4" and "Điều kiện 5", a third numbering. | — | reading only (F19). |
| X9 | 323-328, 661-662 | Def 62 spares charity and company races from "dangerous sports"; exclusion 28's "bất kỳ hoạt động đua nào" (any race) takes them back. | A company charity run. | findings §X9: not dangerous, still excluded. |
| X10 | 609, 607, 974-997 | VI.8 lists occupational tuberculosis (13) and radiation sickness (7) and is "subject to the exclusions", which exclude pulmonary tuberculosis (IV.9) and radioactive contamination (IV.7); occupational hepatitis (14) is a special disease with a year's wait. Those items are illusory. | Occupational TB under VI.8. | findings §X10: not covered. |
| X11 | 697-699, 747 | Table item 5 pays 100% for "mất một cánh tay hoặc một bàn chân" (an arm OR a foot); item 30 pays 40-50% for a foot. The same loss is worth 100% or 40%. | Loss of one foot, sum insured 100.000.000. | findings §X11: 100.000.000 against 40.000.000. |
| X12 | 261-267, 301-304, 691-702 | Two definitions of total permanent injury (49 with a listed-row limb, 56 without) and a table section listing TPD at 100% without the 52 weeks. | — | reading only (F7). |
| X13 | 863-870, 1008-1010, 1270-1278, 1321-1323, 482-483, 898, 1090 | The insurer's discretion without criteria: rates within a range and for unlisted injuries; whether a disappearance shows a fatal injury; the assistance company on criticality, destination and means, and on how much of the late-notice costs the insured bears; renewal premium "on other factors"; PTI's confirmation of membership changes; refusing late accident documents "in part or in whole". | — | reading only; each enters as an input or a named refusal. |
| X14 | 709, 769-771, 784-785, 808-820 | Table gaps and overlaps: "Dưới 55 tuổi" and "Trên 55 tuổi" leave 55 unplaced, likewise 45; "Ít nhất 5 cm" and "Từ 3 đến 5 cm" both take 5 cm; items 57 and 58 print the same range for overlapping descriptions; typos ("đống thời", "hang", "bang quang"). | An insured aged exactly 55. | reading only (the claim names the row). |
| X15 | 896-898 | VI.1's automatic cover depends on PTI confirming the monthly notice; no criteria. | — | reading only (part of X13). |
| X16 | 912-924 | VI.2 makes payment a condition precedent to liability and preserves liability arising before termination. | Accident on day 41, premium never paid. | findings §X16: covered on F26. |
| X17 | 942, 955, 608 | VI.5 extends cover "notwithstanding anything to the contrary" and ends "subject to the exclusions", one of which excludes strikes. | Injury in a strike. | reading only (F29). |
| X18 | 941-1006 | VI.5 for riots, VI.7, VI.9 and VI.10 add nothing the base cover lacks. | An unprovoked assault without VI.10. | findings §X18: covered. |
| X19 | 1014-1020 | VI.12 covers prenatal checks but names no benefit or limit to pay them from. | A prenatal ultrasound. | findings §X19: REFUSED. |
| X20 | 482-483 | "Guaranteed renewal" allows the premium to be recalculated on factors PTI chooses. | — | reading only. |
| X21 | 490-491 | Cancellation "trong vòng 30 ngày trước ngày hủy" can be read as requiring no minimum notice at all. | Notice the day before. | reading only (F17). |
| X22 | 563-565 | Other insurance: two methods joined by "or", no chooser. | Costs 10M, other policies pay 6M, limits 20M of 40M: 4M or 5M. | tests-parts §III.11: 4.000.000 and 5.000.000. |
| X23 | 149-151, 205-207 | An overnight admission of under 24 hours is inpatient treatment (def 25) but not a hospital stay (def 35) nor day treatment, so its room charge is not paid. | Admitted 8 pm, out 7 am. | findings §X23: covered, 0 paid. |
| X24 | 373-375 | Benefit 2 lists no consultation fee: an accident treated as an outpatient gets nothing for the consultation. | A sprain seen in clinic. | findings §X24: 0. |
| X25 | 510-514, 1088-1091 | Benefit 1 pays a death within two years of the accident, but accident documents (the death certificate among them) are due within 12 months. | Death 23 months after the accident. | findings §X25: payable 100.000.000; REFUSED once Part VII applies. |
| X26 | 472-473, 916-917 | Two premium deadlines: 30 days from the effective date (III.2(c), no consequence) and 60 days from issue (VI.2, termination). | Premium paid on day 45. | tests-parts: III.2(c) breached at 31, VI.2 satisfied. |
| X27 | 566-572, 661-662 | III.12 lets the insured buy back professional matches; exclusion 28 excludes them anyway, with no buy-back. | A professional footballer, risk accepted and paid for. | findings §X27: not covered. |
| X28 | 461-463, 219-221 | III.1 admits first entry up to 65; def 40 admits a spouse only under 65. | A spouse of 65. | findings §X28. |
| X29 | 542, 678-680, 1016 | Thresholds at 50 disagree: VI.12 "từ 50 nhân viên trở lên" (50+), III.8 "trên 50 nhân viên" (51+), IV's table "Số người bảo hiểm" (persons, not employees). | Exactly 50 employees. | findings §X29. |
| X30 | 268-273, 530-532 | Def 50 says a waiting period applies to a benefit only if shown on the benefit summary; III.8 imposes waiting periods by default. | — | reading only (III.8 is encoded as written). |
| X31 | 1072-1087, 554-560 | Conflicts with the Law (L2, L4, L5). | — | reading only. |

The three most likely to matter to a policyholder: X1 (a condition from the first year barred at every renewal on def 36's words, src 208-209, 526-529), X25 (a death within Benefit 1's two years defeated by the 12-month document limit, src 510-514, 1088-1091), and X11 (the loss of one foot at 100% or 40%, src 697-699, 747).

## 5. Answer table

The figures the document states, by benefit (the schedule's figures are inputs).

| benefit | what it pays | document's figures | src |
| --- | --- | --- | --- |
| 1 | death or total permanent injury: 100% of the sum insured; partial: table rate x sum insured; death within 2 years of an injury in the period | 100%; table 126 rows | 368-371, 510-514 |
| 2 | accident medical expenses up to the limit | dental 10%, other prostheses 10% of the limit | 373-380 |
| 3 | death or permanent disability from illness or maternity | 100%; table; funeral allowance (contract figure) | 382-389, 339-341 |
| 4 | hospital and surgery for illness or maternity, up to the limit | therapeutic procedures within 50% of the surgery limit; pre-admission 30 days; post-discharge 45 days; vitamins VND 500.000 a prescription | 391-402, 157-170, 278-283 |
| 5 | salary / 30 x days, or fixed x days, up to the days chosen | / 30 | 420-426 |
| 6 | outpatient: consultations, tests, medicine, devices, therapy, listed dental | traditional medicine within 20% (VI.3) | 431-441, 930-931 |
| 7 | emergency transport in Vietnam | Level A USD 50 000, Level B USD 20 000; 90 days away | 1235-1236, 1338-1341 |

Worked results asserted in the tests (scenario schedule: Benefit 2 limit 20.000.000; Benefit 4 limit 40.000.000, surgery 20.000.000; room 1.000.000 a day; Benefit 6 10.000.000; allowance 200.000 a day; 60 days):

| scenario | result |
| --- | --- |
| accident, 3 nights: surgery 5M, room 3.6M, crown 3M, medicine 1M, precious crown 2M, consultation 0.2M | 11.200.000 (room cut to 3M, crown to 2M, precious 0) |
| the same, 15M paid before | 5.000.000 |
| the same, other policies pay 6M of limits totalling 40M | 5.600.000 |
| illness, 5 nights: surgery 15M, procedure 12M, room 7.5M, tests 2M, pre-admission 1M, post-discharge (day 49) 0.5M | 28.000.000 |
| outpatient: consultation 0.3M, medicine 0.5M, filling 0.4M, cosmetic dental 1M | 1.200.000 |
| allowance: accident 10 days; salary 9M basis; 70 days | 2.000.000; 3.000.000; 12.000.000 |
| cancer death in hospital, insured since 2025 | 55.000.000 (50M + funeral 5M) |
| childbirth day 104, 51 employees, costs 7M | 3.500.000 (105/210) |
| transport USD 10.000, Level A, 25.000 VND per USD | 250.000.000 |

## 6. What check.sh prints

```
module                                    errors satisfied  failed  refused  expected
pti268-annex-transport.l4                      0         0       0        0         0
pti268-benefits.l4                             0         0       0        0         0
pti268-claims.l4                               0         0       0        0         0
pti268-conditions.l4                           0         0       0        0         0
pti268-decision.l4                             0         0       0        0         0
pti268-definitions.l4                          0         0       0        0         0
pti268-exclusions.l4                           0         0       0        0         0
pti268-extensions.l4                           0         0       0        0         0
pti268-findings.l4                             0        34       0        0         0
pti268-fixtures.l4                             0         0       0        0         0
pti268-injury-table.l4                         0         0       0        0         0
pti268-nouns.l4                                0         0       0        0         0
pti268-tests-claims.l4                         0       168       0        0         0
pti268-tests-parts.l4                          0       218       0        0         0
pti268-tests-table.l4                          0       143       0        0         0
TOTAL (15 modules)                             0       563       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

`check.sh` exit 0.
No failing or refused assertion is expected, and none occurs; `expected_failed` is 0 for every module and `check.sh` was not edited.
The rule modules, the nouns and the fixtures carry no assertions of their own.
Assertions by module: `pti268-tests-table.l4` 143 (126 generated per-row tests of Part V, each reading the row's printed line by a second method independent of the data generator, plus 17 on the six principles); `pti268-tests-parts.l4` 218 (Parts I, III, VI, VII and the Annex, provision by provision, both sides of every threshold); `pti268-tests-claims.l4` 168 (every general exclusion with its near misses, and ten whole-claim scenarios through cover, sub-limits, limits and time limits); `pti268-findings.l4` 34 (the findings of section 4 that the encoding can show; each asserts the surprising answer the text gives).
`pti268-tests-parts.l4` also runs six `#TRACE`s of regulative rules: three end FULFILLED (premium paid on day 30; PTI pays a complete file on calendar day 21, the 15th working day; the insured notifies the assistance company at hour 24) and three end in the BREACH they were written to show (premium unpaid at day 31; PTI unpaid at day 22; claim file unsubmitted at day 121). Traces are not assertions and `check.sh` does not count them.
To see that the harness can fail, a scratch run during development failed loudly on a misnamed function (276 errors) before it was fixed; no expected value was edited to make a test pass.

## 7. The vnsrc check

The gate (every `.l4` and every `.md` in this directory except `BRIEF.md`, which is the lead's):

```
python3 -I tools/vnsrc.py check ../../source/raw/pti-gras-savoye.txt $(ls *.l4 *.md | grep -v '^BRIEF.md$')
vnsrc check: 1019 src: lines, 459 Vietnamese runs, 0 problems
```

The literal command of the brief, `python3 -I tools/vnsrc.py check ../../source/raw/pti-gras-savoye.txt *.l4 *.md`, also reads `BRIEF.md` and reports problems only there: two at `BRIEF.md:23` and one at `BRIEF.md:31`, where the brief quotes the title across a line break and names a sibling PTI product whose name is not in this source. Its last line:

```
vnsrc check: 1019 src: lines, 470 Vietnamese runs, 3 problems
```

The three problem lines are not reproduced here because they quote Vietnamese that is not in the source, which would make this file fail the gate.

## 8. Open questions for a domain expert

1. Is def 36 or def 38 the start date in practice at renewal (F1, X1)? Does PTI apply the 365-day wait again after each renewal?
2. Does IV's second 32 table replace III.8's 365 days for Benefits 4 and 6, or add to it (F11, X3)?
3. Which row does PTI use for the loss of one foot, item 5 or item 30 (X11)?
4. Which benefit and limit pay VI.12's prenatal checks, and def 13/14/22/69's newborn care, taxi, ambulance and home nursing (X7, X19)? Are they usually in the benefit summary?
5. Is the 12-month limit for accident documents applied to deaths within Benefit 1's two-year tail (X25)?
6. Under III.11, does PTI pay the excess or the proportion, and who chooses (F20)?
7. Does the Law on Insurance Business 08/2022/QH15 override the 120-day submission limit (art 30), the no-refund rule on fraud (art 22(2)) and the absence of a force majeure exception to the accident notice (art 19(3)) for contracts made after 2023 under these 2012 rules (L2, L4, L5)?
8. Is the document still in use (the mirror was uploaded in May 2023) and does PTI publish a later wording?
