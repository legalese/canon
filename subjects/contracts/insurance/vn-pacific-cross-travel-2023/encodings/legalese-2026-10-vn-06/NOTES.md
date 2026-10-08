# NOTES — vn-pacific-cross-travel-2023, encoding row `legalese-2026-10-vn-06`

Pacific Cross Vietnam's travel insurance wording, **Travel Insurance Policy** / **Quy tắc bảo hiểm du lịch**, encoded in L4 by one agent in one session (`enc-vn-06`, run `VN-06-20261006`, 2026-10-06), from `BRIEF.md`.
Status: **draft**.
No domain expert has read it against the source; HG1 has not been sought; no independent test pass has been run; every expected value was written by the same session that wrote the rules.

## 0. Build and run

`l4` is `/Users/mengwong/.local/bin/l4`, sha256 `64bbcb157dbef2ef1020a6a75589313bba0a2aeeb807c921c5e65e62e9eca118`, run with `JL4_LIBRARY_PATH` unset.
The binary has no `--version`.
Every run prints two Warnings that differing copies of `prelude` and `daydate` exist under `~/.local/share/jl4/libraries/`; the binary uses its embedded copies, and the warnings are not errors.

```
cd subjects/contracts/insurance/vn-pacific-cross-travel-2023/encodings/legalese-2026-10-vn-06
L4=/Users/mengwong/.local/bin/l4 ./check.sh
```

Final run, 2026-10-07:

```
module                                    errors satisfied  failed  refused  expected
pc-travel-claims.l4                            0         0       0        0         0
pc-travel-definitions.l4                       0         0       0        0         0
pc-travel-general.l4                           0         0       0        0         0
pc-travel-nouns.l4                             0         0       0        0         0
pc-travel-part1-medical.l4                     0         0       0        0         0
pc-travel-part2-accident.l4                    0         0       0        0         0
pc-travel-part3-property.l4                    0         0       0        0         0
pc-travel-part3-trip-liability.l4              0         0       0        0         0
pc-travel-part4-rental-car.l4                  0         0       0        0         0
pc-travel-tests-en-vi.l4                       0        82       0        0         0
pc-travel-tests-fixtures.l4                    0         0       0        0         0
pc-travel-tests-tables.l4                      0        71       0        0         0
pc-travel-tests.l4                             0       338       0        0         0
TOTAL (13 modules)                             0       491       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

`check.sh exit 0`.

The modules, in reading order:

| module | what it holds |
| --- | --- |
| `pc-travel-nouns.l4` | `DECLARE` only: the Certificate, the Insured Person, the trip, the case, the clause 5 circumstances (the 22 named Disabilities and 13 named activities), and one claim record per section |
| `pc-travel-definitions.l4` | the 28 definitions, in the order printed; the Short Period Rate table |
| `pc-travel-general.l4` | the preamble; clauses 1-17; Travel Flex; Annual Travel 1-6; the limits the sections share; the general gate `the general terms let a claim proceed` |
| `pc-travel-part1-medical.l4` | Part I: sections 1A and 1B |
| `pc-travel-part2-accident.l4` | Part II: section 2 |
| `pc-travel-part3-property.l4` | Part III, sections 3-6 |
| `pc-travel-part3-trip-liability.l4` | Part III, sections 7-11 |
| `pc-travel-part4-rental-car.l4` | Part IV, section 12; other insurance |
| `pc-travel-claims.l4` | the Claims Procedure, with three regulative rules; the version marker |
| `pc-travel-tests-fixtures.l4` | named facts and builders for the tests; no rules, no assertions |
| `pc-travel-tests-tables.l4` | **generated** from the raw text: one assertion per plan in every plan table, the Personal Accident table and the Short Period Rate table |
| `pc-travel-tests.l4` | scenario tests read against the English text |
| `pc-travel-tests-en-vi.l4` | every place the two texts give different answers, asserted against each |

Every `-- src:N |` line in the modules was written by a build script that calls `tools/vnsrc.py quote`; none was typed.
The plan-table tests were written by a second script that parses the English figures (comma groups thousands) and the Vietnamese figures (dot groups thousands) from the raw text and checks they agree before writing an assertion (§5).
The coverage table in §2 was generated the same way: each Vietnamese cell is cut from the raw text.

## 1. What is encoded, and what is not

**The whole document is in scope and every provision has a row in §2**: the preamble, the 17 general terms, the Travel Flex and Annual Travel terms, sections 1A to 12, the other-insurance clause, the 28 definitions, the Claims Procedure, and the version marker.
184 rows are encoded and 37 are inert (headings, a recital, a rule of construction, a choice of law, definitions no operative clause uses, the version marker); none is out of scope and none deferred.
The insurer's contact block (src 2210-2217) and the page footers and numbers are not provisions.

**What the encoding answers.**
For each insuring section: whether an event is covered (the general terms, the cover window, the section's own conditions and exclusions) and how much is payable (limits, sub-limits, daily caps, deductible, the Certificate's limit).
For the conditions: ages, periods, cancellation and refunds, extension, Travel Flex, the Annual Travel terms, arbitration, the time-bars.
For the Claims Procedure: the deadlines as dates, three duties as regulative rules (`#TRACE`d), and the documents each section's claim needs.
What the wording leaves to the Insurance Certificate (plan, product, dates, the per-section limits, premiums) is an input with no default; a limit the Certificate does not state is refused by name, never assumed.

**The two texts.**
The English text is src 1-1077, the Vietnamese src 1079-2208.
Each operative rule cites both, an English `src:` block then the Vietnamese one.
Where the two give different answers the rule exists twice, `… reading the English` and `… reading the Vietnamese`, and a third name takes a `Text version` and picks; every such pair is tested in `pc-travel-tests-en-vi.l4`.
The rules that agree take the `Text version` too and ignore it, so a caller asks one question of one text at a time.

**Which text prevails: no clause found.**
Searched both halves of the raw text for: prevail, conflict, inconsistent, discrepancy, precedence, language, English, Vietnamese, translation, ưu tiên, ngôn ngữ, tiếng, bản dịch, and the brief's "khác biệt" and "mâu thuẫn" (the Vietnamese words on this line are search terms, not quotations [translator]).
Nothing matched but the page footers ("EN G LISH", "TIẾNG VIỆT") and "tiếng" meaning "hours" (6 tiếng, src 1668, 1749, 1764).
`tools/vnsrc.py check` confirms it independently: run over `BRIEF.md` it reports "ưu tiên", "khác biệt" and "mâu thuẫn" as not occurring anywhere in the source (§7) (search terms [translator]).
The Law aid was searched too (tiếng, bản dịch, song ngữ, ngôn ngữ; search terms [translator]): its only provision on language is Art. 87(2)(b) (Law line 1765-1767), that terms be precise and defined; it says nothing of precedence between language versions.
The nearest rule is Art. 24 (Law line 588-591): an unclear term that admits different understandings is to be interpreted in the way that favours the insurance buyer — fork LAW-CONTRA.

**Which version of the wording.**
Both texts end with the same version marker, "Vs. 022014" (src 1077) and "Vs.022014" (src 2208); the file name says 042023 and the upload path 2025/08.
The encoding takes the document as published at its URL on 2026-10-06 and makes no claim about which marker is current.

**The tag.**
The brief asks for findings tagged with EN, the not-equal sign and VI, written without spaces (BRIEF.md line 56).
In this deposit the tag is written `EN ≠ VI`, with spaces, because `tools/vnsrc.py` decomposes "≠" (U+2260) into "=" and a combining overlay, counts the overlay as a Vietnamese diacritic, and reports the unspaced tag as a Vietnamese run missing from the source; the spaced form is the same tag and passes.
The findings are also numbered `VN-F1` to `VN-F27`, which grep reliably.

**What was read.**
The deposited raw text, in full, both halves; the Law aid (Arts. 15-32, 43-54, 87; §3's LAW forks cite its lines); the skills and references the brief names; IL-03's NOTES, nouns module and `encoding.json` for shape; the Chubb encoding for house style.
No other row's directory was opened.
No network was used.

## 2. Coverage table

Line numbers are lines of `../../source/raw/pacificcross-travel.txt`.
The third column is cut mechanically from the Vietnamese text (the heading, or the provision's first words); the fourth is an English gloss.

| # | provision | heading or opening words as the Vietnamese writes them | English gloss | EN src | VI src | disposition | where, or why |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Title | QUY TẮC BẢO HIỂM DU LỊCH TOÀN CẦU | Travel Insurance Policy (VI adds TOÀN CẦU, global) | 1-2 | 1079-1081 | inert | a title; finding VN-F21 |
| 2 | Preamble | Theo đề nghị của Chủ hợp đồng được nêu | recital: the Company accepts the Application and the risks | 5-10 | 1082-1088 | inert | a recital; no rule turns on it (phrasebook 9.2) |
| 3 | General heading | CÁC ĐIỀU KHOẢN VÀ ĐIỀU KIỆN ÁP DỤNG CHUNG CHO TẤT CẢ CÁC KHOẢN | Terms and conditions applying to all sections | 11 | 1090-1091 | inert | a heading |
| 4 | Clause 1 | Việc tuân thủ và thực hiện đúng các điều | observance of terms and true statements are conditions precedent | 13-19 | 1093-1099 | encoded | general: `clause 1 — the conditions precedent to liability are met` |
| 5 | Clause 2 | Trong Hợp đồng bảo hiểm này | singular/plural, gender | 20-23 | 1100-1103 | inert | a rule of construction; it decides nothing alone |
| 6 | Clause 3 | Hợp đồng bảo hiểm này được chi phối và | governed by the laws of Vietnam | 24-27 | 1104-1107 | inert | a choice of law; it adds or removes no condition of payment; it is why the Law aid is read for LAW forks |
| 7 | Clause 4 | Nếu có bất kỳ yêu cầu bồi thường nào | a disclaimed claim not referred within 6 calendar months is abandoned | 28,33-36 | 1108-1112 | encoded | general: `clause 4 — …` |
| 8 | Clause 5 chapeau | Hợp đồng bảo hiểm này không bồi thường cho | the Policy does not cover losses arising from | 37 | 1113-1114 | encoded | general: `clause 5 excludes a loss arising from …` |
| 9 | Clause 5.1 | Các bệnh hoặc thương tích đã có trước | pre-existing illness or injury, congenital conditions | 38-39 | 1120-1121 | encoded | general; part1-medical `the circumstances the Disability arose from` (fork F-PEC) |
| 10 | Clause 5.2 | Những bệnh tật sau đây cho dù xảy ra | 22 named Disabilities, before or during the Period | 40-54 | 1123-1137 | encoded | nouns `A Disability named in clause 5.2`; general |
| 11 | Clause 5.3 | Chiến tranh | war and warlike events; riot amounting to a popular rising | 55,57-61 | 1139-1145 | encoded | general (two readings, VN-F2) |
| 12 | Clause 5.4 | Các hành động khủng bố hoặc hành động được | terrorism | 62-76 | 1147-1163 | encoded | general |
| 13 | Clause 5.5 | Tự tử | suicide, mental disorders, childbirth, alcohol and drugs, dental | 77-83 | 1165-1171 | encoded | general |
| 14 | Clause 5.6 | Phản ứng phân rã hạt nhân | nuclear | 84-85 | 1173-1174 | encoded | general |
| 15 | Clause 5.7 | Các tai nạn xảy ra trong khi tham gia | accidents in named sports, flying, manual or hazardous work | 86-101 | 1176-1192 | encoded | general (two readings, VN-F1, VN-F3) |
| 16 | Clause 5.8 | Ði tìm hiểu thiên nhiên ở độ cao trên | trekking above 5,000 m, scuba below 20 m | 102-104 | 1194-1196 | encoded | general (VN-F22 reading only) |
| 17 | Clause 5.9 | Những tổn thất mang tính chất gián tiếp và | indirect and consequential losses | 105 | 1198 | encoded | general |
| 18 | Clause 6 | Hợp đồng bảo hiểm này chỉ có giá trị | leisure or administrative business travel only | 106-107 | 1200-1202 | encoded | general: `clause 6 — …` |
| 19 | Clause 7 | Công ty hoặc Chủ Hợp Đồng không thể hủy | non-cancelable save Annual Travel or unpaid premium; no refund | 111-114 | 1203-1207 | encoded | general: `clause 7 — …` |
| 20 | Clause 8 | Việc gia hạn bảo hiểm khi hết thời gian | extension of cover, up to 180 days | 115-119 | 1208-1213 | encoded | general (two readings, VN-F4) |
| 21 | Clause 9 | Trong trường hợp Công ty đã thực hiện bất | subrogation | 120-123 | 1214-1218 | encoded | general: `clause 9 — …` (fork LAW-SUBRO) |
| 22 | Clause 10 | Không thanh toán trực tiếp các chi phí y | direct billing only above VND 50,000,000 | 124-127 | 1219-1222 | encoded | general: `clause 10 — …` |
| 23 | Clause 11 | Chủ hợp đồng và Người được bảo hiểm có | joint liability for costs not covered | 128-132 | 1223-1228 | encoded | general: `clause 11 — …` |
| 24 | Clause 12 | Công ty và (các) | strikes and conditions beyond control | 133-137,141 | 1229-1235 | encoded | general: `clause 12 — …` |
| 25 | Clause 13 | Việc bảo hiểm cho tất cả các mục ngoại | when cover commences and ceases; Cancellation Charges window | 142-157 | 1236,1242-1255 | encoded | general: `clause 13 — …`, `clause 13 and AT 5 — …` |
| 26 | Clause 14 | Thời gian bảo hiểm tối đa của Hợp đồng | at most 180 consecutive calendar days | 158-159 | 1256-1257 | encoded | general: `clause 14 — …` (fork F-C14) |
| 27 | Clause 15 | Giới hạn tuổi cho (những) | ages 6 weeks to 75; under 7 accompanied; none from 76 | 160-164 | 1258,1260-1263 | encoded | general: three `clause 15 — …` rules |
| 28 | Clause 16 | Nếu Người được bảo hiểm không tuân theo các | claims procedure; fraud voids the Policy | 167-172 | 1264-1270 | encoded | general: `clause 16 — …` |
| 29 | Clause 17 | Bất cứ bất đồng nào phát sinh giữa Người | arbitration; an award is a condition precedent | 173-186 | 1271-1282 | encoded | general (two readings of the right of action, VN-F15) |
| 30 | Travel Flex / Annual heading | CÁC ĐIỀU KHOẢN VÀ ĐIỀU KIỆN ÁP DỤNG RIÊNG CHO BẢO HIỂM DU LỊCH | Terms and conditions for Travel Flex and Annual Travel only | 188-189 | 1284-1285 | inert | a heading |
| 31 | Travel Flex | Phần áp dụng riêng cho Travel Flex | free extension of up to 5 days for a delay beyond control | 191-201 | 1287-1298 | encoded | general: `Travel Flex — the days of free extension` |
| 32 | Annual Travel heading | Phần áp dụng riêng cho Annual Travel: | Annual Travel sections | 202 | 1299 | inert | a heading |
| 33 | AT 1 | Nếu có bất kỳ sự thay đổi nào về | notice of an alteration within 30 days | 203-205 | 1300-1303 | encoded | general: `AT 1 — …` (deontic; VN-F14) |
| 34 | AT 2 | Mỗi Người được bảo hiểm sẽ được cấp một | the coverage card | 206-210 | 1304-1309 | encoded | general: `AT 2 — …` |
| 35 | AT 3 | Công ty có thể hủy Hợp đồng bảo hiểm | cancellation by either side on 7 days' notice; refunds | 211-217,219-223 | 1310-1313,1316-1326 | encoded | general: `AT 3 — …` |
| 36 | AT 4 | Bất kỳ việc tái tục nào của Hợp đồng | renewal at the Company's option | 224-225 | 1327-1328 | encoded | general: `AT 4 — renewal` (MAY) |
| 37 | AT 5 | Việc bảo hiểm cho tất cả các mục ngoại | when Annual Travel cover commences and ceases | 226-242 | 1329-1344 | encoded | general: `clause 13 and AT 5 — …` |
| 38 | AT 6 | Số ngày tối đa cho mỗi chuyến đi theo | at most 90 consecutive calendar days a trip | 243-244 | 1345-1346 | encoded | general: `AT 6 — …` |
| 39 | Insuring sections heading | CÁC MỤC BẢO HIỂM | Insuring sections | 246 | 1348 | inert | a heading |
| 40 | Part I heading | I. CHI PHÍ Y TẾ VÀ TRỢ GIÚP KHẨN CẤP | I. Medical expenses and emergency assistance | 251 | 1349 | inert | a heading |
| 41 | 1A heading | MỤC 1A — “CHI PHÍ Y TẾ” | Section 1A, Medical Expenses | 253-255 | 1351-1352 | inert | a heading |
| 42 | 1A.1 chapeau | Công ty đồng ý thanh toán các chi phí | eligible inpatient and outpatient expenses abroad, only those listed | 256-261 | 1353,1359-1361 | encoded | part1-medical: `1A.1(a) names the kind of expense`, `the Disability is covered under section` |
| 43 | 1A.1(a) | Viện phí | the expenses; room and board 6,000,000 a day; 20,000,000 a day without breakdown | 263-270 | 1362-1370 | encoded | part1-medical: `1A.1(a) — the daily cap applied to … of …` |
| 44 | 1A.1(b) | Chi phí y tế hợp lệ được định nghĩa | follow-up within 90 days of return, at most 130,000,000 | 271-275 | 1371-1374 | encoded | part1-medical: `1A.1(b) — …`, `1A — the amount payable` |
| 45 | 1A.1 proviso | Với điều kiện là tất cả các chi phí | normal, customary, reasonable; breakdown, receipts, reports; incurred abroad | 277-282 | 1375,1377-1380 | encoded | part1-medical: `1A.1 proviso — …` (finding F-MED-BREAKDOWN) |
| 46 | 1A.2 chapeau | Quyền lợi “Chi phí y tế” | Medical Expenses does not cover | 283 | 1381 | encoded | part1-medical: `1A.2 — the expense is excluded` |
| 47 | 1A.2(a) | Các chi phí y tá điều dưỡng đặc biệt | special or private nursing | 285 | 1382-1383 | encoded | part1-medical `1A.2 — …` |
| 48 | 1A.2(b) | Chi phí vật lý trị liệu | physiotherapy, chiropractic, acupuncture | 286 | 1384 | encoded | part1-medical |
| 49 | 1A.2(c) | Phẫu thuật thẩm mỹ | cosmetic surgery, eyeglasses, hearing aids, save after an accidental Injury | 287-290 | 1385-1388 | encoded | part1-medical (finding F-MED-CLOSED) |
| 50 | 1A.2(d) | Các chi phí y tế được trả bởi bất | expenses payable by other insurance or a third party | 291-295 | 1389-1392 | encoded | part1-medical (VN-F24 reading only) |
| 51 | 1A.2(e) | Các rối loạn về tâm thần | psychiatric and mental disorders | 296-297 | 1393-1394 | encoded | part1-medical |
| 52 | 1A.2(f) | Bất kỳ chi phí nào phát sinh từ các | birth control and infertility | 298-300 | 1395-1397 | encoded | part1-medical |
| 53 | 1A.2(g) | Bất kỳ chi phí nào phát sinh do Ốm | pregnancy-related Illness or Injury | 301-302 | 1398-1399 | encoded | part1-medical |
| 54 | 1A.2(h) | Điều trị hoặc sử dụng dịch vụ mà không | treatment without a Physician's recommendation; routine check-ups | 303-306 | 1400-1403 | encoded | part1-medical (fork F-CHECKUP) |
| 55 | 1A.2(i) | Các chi phí y tế phát sinh sau 30 | expenses more than 30 days after the end of cover when unable to return | 307-312 | 1404-1409 | encoded | part1-medical: `1A.2(i) — …` (refuses the case it does not provide for) |
| 56 | 1B heading | MỤC 1B — “TRỢ GIÚP KHẨN CẤP” | Section 1B, Emergency Assistance | 314-316 | 1411-1413 | inert | a heading |
| 57 | 1B preamble | Trợ giúp y tế khẩn cấp Công ty đã | assistance companies; what the caller must identify | 317-332 | 1414-1427 | encoded | part1-medical: `1B preamble — …` |
| 58 | 1B.1 | Sơ tán khẩn cấp (không giới hạn) | Emergency Evacuation (unlimited) | 333-340 | 1428-1430,1432-1435 | encoded | part1-medical: `1B.1 — …` (VN-F28 reading only) |
| 59 | 1B.2 | Hồi hương (không giới hạn) | Repatriation (unlimited) | 341-350 | 1436-1446 | encoded | part1-medical: `1B.2 — …` |
| 60 | 1B.3 | Bảo lãnh viện phí | Hospital Expenses Guarantee above 50,000,000 | 351-354 | 1447-1450 | encoded | part1-medical: `1B.3 — …` |
| 61 | 1B.4 | Trợ cấp nằm viện | Hospital Cash Allowance 1,000,000 a day | 355,360-375 | 1451-1466 | encoded | part1-medical (two readings, VN-F5, VN-F10) |
| 62 | 1B.5 | Chi phí bổ sung cho việc đi lại và | additional costs of travel and accommodation | 376-387 | 1467-1468,1474-1482 | encoded | part1-medical: `1B.5 — …` |
| 63 | 1B.6 | Thăm viếng của người thân trong gia đình | Family Member Visit | 388-393 | 1483-1489 | encoded | part1-medical: `1B.6 — …` |
| 64 | 1B.7 | Đưa trẻ em trở về nước | Return of Children | 394-403 | 1490,1493-1500 | encoded | part1-medical (two readings, VN-F7) |
| 65 | 1B.8 | Hồi hương thi hài | Repatriation of Mortal Remains | 404-411 | 1501-1507 | encoded | part1-medical: `1B.8 — …` |
| 66 | 1B.9 | Các dịch vụ thông tin trợ giúp | Referral Services; no liability for fees | 412-416 | 1508-1513 | encoded | part1-medical (two deontic readings, VN-F9) |
| 67 | 1B Note | Chú ý | prior approval for (1), (2) and (3) | 417-420 | 1514-1517 | encoded | part1-medical: `1B Note — …` |
| 68 | Part II heading | II. TAI NẠN CÁ NHÂN | II. Personal accident | 422 | 1519 | inert | a heading |
| 69 | 2 heading | MỤC 2 — “TAI NẠN CÁ NHÂN’’ | Section 2, Personal Accident | 424-426 | 1521-1523 | inert | a heading |
| 70 | 2.1 | Các quyền lợi được mô tả ở đây sẽ | death or disablement within 12 calendar months, cause within the Period | 427-430 | 1524-1528 | encoded | part2-accident: `2.1 — …` |
| 71 | 2.2 | Mức chi trả bồi thường tối đa cho mỗi | the limit in the Certificate; nothing more once a benefit is payable | 431-435 | 1529-1532 | encoded | part2-accident: `2 — the amount payable` (finding F-PA-ONCE) |
| 72 | 2.3 | Các quyền lợi được biểu thị theo tỷ lệ | benefits as a percentage of the sum insured | 438-440 | 1533-1535 | encoded | part2-accident: `2.3 — …` |
| 73 | 2.3 table | Tử vong do tai nạn 100% Mất hoàn toàn | six rows: 100% x 5, 50% for loss of use of one limb | 442-452 | 1537-1548 | encoded | part2-accident; tests-tables (generated) |
| 74 | 2.4 | Số tiền bảo hiểm cho trẻ em dưới 18 | a child's sum insured at most 400,000,000 | 454-455 | 1550-1551 | encoded | part2-accident: `2.4 — …` |
| 75 | 2.5 | Số tiền tối đa phải trả cho bất kỳ | at most 100% of the sum insured for all events, save 2.7 | 456-459 | 1552-1556 | encoded | part2-accident: `2 — the amount payable` |
| 76 | 2.6 | Trong trường hợp Người được bảo hiểm tử vong | the beneficiary on death | 460-464 | 1557-1562 | encoded | part2-accident: `2.6 — the beneficiary` (VN-F16 reading only) |
| 77 | 2.7 | Quyền lợi về Tai nạn cá nhân bổ sung | Common Carrier: double, Bon Voyage only, not children | 465-466,471-475 | 1563-1570 | encoded | part2-accident: `2.7 — …` |
| 78 | Part III heading | III. BẢO HIỂM SỰ CỐ BẤT NGỜ | III. Incidental cover | 477 | 1572 | inert | a heading |
| 79 | 3 heading | MỤC 3 — “HÀNH LÝ VÀ ĐỒ DÙNG CÁ NHÂN” | Section 3, Baggage and Personal Effects | 479-481 | 1574-1576 | inert | a heading |
| 80 | 3 insuring clause | Mục này cung cấp sự bồi thường cho hành | loss or damage by theft, robbery, burglary, Accident, carriers | 482-486 | 1577-1581 | encoded | part3-property: `3 — the cause is one the section names` |
| 81 | 3.1 | Tổn thất phải được thông báo cho cảnh sát | report within 24 hours | 488-490 | 1584-1586 | encoded | part3-property: `3.1 and 3.2 — …` |
| 82 | 3.2 | Người được bảo hiểm phải giữ gìn cẩn thận | ordinary care; immediate notice to police or carriers | 491-494,496-505 | 1587,1593-1604 | encoded | part3-property: `3.1 and 3.2 — …` |
| 83 | 3.3 | Mức bồi thường tối đa là 5.000.000 VND cho | 5,000,000 an item, 10,000,000 a pair or set, laptop, camera as a set | 506-510 | 1605-1609 | encoded | part3-property: `3 — the amount payable` (finding F-LAPTOP) |
| 84 | 3.4 | Công ty sẽ bồi thường cho Người được bảo | payment, replacement or repair at the Company's option, up to the Certificate | 511-515 | 1611-1615 | encoded | part3-property: `3 — the amount payable` |
| 85 | 3.5 | Đối với những yêu cầu bồi thường về bể | damaged property produced for inspection | 516-518 | 1616-1619 | encoded | part3-property: `3.5 — …` |
| 86 | 3.6 chapeau | Quyền lợi “Hành lý và Đồ dùng cá nhân” | Baggage and Personal Effects does not cover | 519 | 1620-1621 | encoded | part3-property: `3.6 — the article is excluded` |
| 87 | 3.6(a) | Mất mát hoặc hư hại do hậu quả của | delay, confiscation, customs | 521-523 | 1622-1624 | encoded | part3-property |
| 88 | 3.6(b) | Mất mát hoặc hư hại đối với tiền mặt | cash, instruments, documents, tickets | 524-528 | 1625-1629 | encoded | part3-property |
| 89 | 3.6(c) | Mất mát hoặc hư hại đối với máy nhắn | phones, portable electronics, computer equipment | 529-533 | 1630-1635 | encoded | part3-property (finding F-LAPTOP) |
| 90 | 3.6(d) | Mất mát hoặc hư hại đối với các món | fragile articles, gemstones, eyeglasses, foodstuff | 534-537 | 1636-1639 | encoded | part3-property |
| 91 | 3.6(e) | Mòn rách | wear and tear; depreciation at the Company's discretion | 538-542 | 1640-1644 | encoded | part3-property (finding F-DISCRETION) |
| 92 | 3.6(f) | Hàng hóa kinh doanh hoặc hàng mẫu | business merchandise or samples | 543-545 | 1645-1647 | encoded | part3-property |
| 93 | 3.6(g) | Mất mát hoặc hư hại đối với hành lý | left unattended in a Public Conveyance or Public Place | 548-550 | 1648-1650 | encoded | part3-property |
| 94 | 3.6(h) | Mất mát hoặc hư hại đối với hành lý | baggage mailed or shipped separately | 551 | 1651-1652 | encoded | part3-property |
| 95 | 3.6(i) | Bất kỳ tài sản hoặc đồ dùng cá nhân | insured elsewhere or recovered | 552-553 | 1653-1655 | encoded | part3-property |
| 96 | 3.6(j) | Mất nữ trang | jewelry, save armed robbery or hotel-safe burglary | 554-555 | 1656-1657 | encoded | part3-property |
| 97 | 3.6(k) | Hư hại đồ đựng hành lý. | damage to luggage | 556 | 1658 | encoded | part3-property (two readings, VN-F8) |
| 98 | 4 heading | MỤC 4 — “HÀNH LÝ ĐẾN CHẬM” | Section 4, Baggage Delay | 557-559 | 1660-1662 | inert | a heading |
| 99 | 4 insuring clause | Công ty sẽ chi trả | emergency purchases after 6 hours without baggage | 560-565 | 1663-1664,1667-1669 | encoded | part3-property: `4 — the baggage delay is covered` |
| 100 | 4.1 | Mức bồi thường tối đa là 1.300.000 VND cho | at most 1,300,000 an article | 567-568 | 1672 | encoded | part3-property: `4 — the amount payable` |
| 101 | 4.2 | Việc chậm trễ phải được xác nhận bằng “Biên | certified by a Baggage Irregularity Report | 569-571 | 1673-1675 | encoded | part3-property |
| 102 | 4.3 | Việc chậm trễ không phải do bị hải quan | not customs detention | 575-576 | 1676-1677 | encoded | part3-property |
| 103 | 4.4 | Người được bảo hiểm phải cung cấp chứng từ | purchase bills | 577-578 | 1678-1679 | encoded | part3-property |
| 104 | 4.5 | Nếu một tổn thất đã được yêu cầu bồi | not claimed under section 3 as well | 579-581 | 1680-1682 | encoded | part3-property |
| 105 | 4.6 | Không bồi thường hành lý đến chậm sau khi | no cover after return or the final destination | 582-583 | 1683-1684 | encoded | part3-property (fork F-FINAL) |
| 106 | 5 heading | MỤC 5 — “MẤT GIẤY TỜ DU LỊCH” | Section 5, Loss of Travel Document | 585-587 | 1686-1688 | inert | a heading |
| 107 | 5 insuring clause | Nếu Người được bảo hiểm bị mất hộ chiếu | replacing lost passports and tickets, and the costs | 588-596 | 1689-1697 | encoded | part3-property (two readings, VN-F11) |
| 108 | 5.1 | Công ty sẽ không chịu trách nhiệm theo mục | police report within 24 hours (EN: or as soon as practicable) | 600-604 | 1700-1703 | encoded | part3-property (two readings, VN-F11) |
| 109 | 5.2 | Công ty sẽ không chịu trách nhiệm theo mục | not if left unattended in a public place | 605-607 | 1709-1711 | encoded | part3-property |
| 110 | 5.3 | Mức bồi thường tối đa mỗi ngày cho các | daily limit 4,000,000 / 3,000,000 / 2,000,000 | 608-611 | 1712-1714 | encoded | part3-property: `5.3 — …` |
| 111 | 5.4 | Mức bồi thường cho vé máy bay là hạng | economy class only | 612-613 | 1715 | encoded | part3-property: `5 — the amount payable` |
| 112 | 6 heading | MỤC 6 — “TIỀN CÁ NHÂN” | Section 6, Personal Money | 615-617 | 1717-1718 | inert | a heading |
| 113 | 6 insuring clause | Công ty sẽ bồi thường cho Người được bảo | money lost by theft, robbery or burglary | 618-621 | 1719-1722 | encoded | part3-property: `6 — the loss is covered` |
| 114 | 6.1 | Nếu Người được bảo hiểm bị mất tiền mặt | report within 24 hours | 623-626 | 1726-1729 | encoded | part3-property |
| 115 | 6.2 | Công ty sẽ không chịu trách nhiệm đối với | not error, omission, exchange | 627-629 | 1730-1732 | encoded | part3-property |
| 116 | 6.3 | Tiền cá nhân phải được mang theo người và | carried on the person | 630-632 | 1733-1735 | encoded | part3-property |
| 117 | 6.4 | Quyền lợi này không áp dụng cho trẻ em | not children under 18 | 633 | 1736 | encoded | part3-property |
| 118 | 7 heading | MỤC 7 — “CHUYẾN ĐI BỊ TRÌ HOÃN” | Section 7, Travel Delay | 635-636 | 1738-1740 | inert | a heading |
| 119 | 7 insuring clause | Trong trường hợp chuyến bay hoặc phương tiện vận | a delay abroad for weather, strike, hijack, breakdown | 637-643 | 1741-1747 | encoded | part3-trip-liability: `7 — the delay is covered` |
| 120 | 7(a) | Người được bảo hiểm có thể yêu cầu bồi | 500,000 for each full 6 hours, capped by plan | 645-648 | 1748-1752 | encoded | part3-trip-liability (VN-F19 reading only) |
| 121 | 7(b) | Mức bồi thường tối đa là 16.000.000 VND cho | re-routing fares, capped by plan | 649,651-655 | 1753-1759 | encoded | part3-trip-liability (VN-F20: EN misprint) |
| 122 | 7, one paragraph | Chỉ có thể yêu cầu bồi thường theo (a) | a claim under (a) or (b) only | 656 | 1761 | encoded | part3-trip-liability: `7 — the amount payable` |
| 123 | 7.1 | Thời gian bị trễ phải kéo dài trên 6 | more than 6 hours | 658-661 | 1764-1767 | encoded | part3-trip-liability: `7.1 to 7.5 — …` |
| 124 | 7.2 | Việc chậm trễ không phải do Người được bảo | not a failure to reconfirm or check in | 662-664 | 1768-1770 | encoded | part3-trip-liability |
| 125 | 7.3 | Việc đặt chỗ trước đã được xác nhận phải | booking confirmed before the industrial action | 665-666 | 1771-1772 | encoded | part3-trip-liability |
| 126 | 7.4 | Chứng từ chính thức của hãng hàng không/nhà vận | official documentation | 667-669 | 1773-1776 | encoded | part3-trip-liability |
| 127 | 7.5 | Không chi trả cho yêu cầu bồi thường phát | no strike existing at the effective date or (Annual) commencement | 670-674 | 1777-1779,1781-1783 | encoded | part3-trip-liability |
| 128 | 8 heading | MỤC 8 — “RÚT NGẮN CHUYẾN ĐI” hoặc “HỦY BỎ CHUYẾN ĐI” | Section 8, Curtailment of Trip or Cancellation Charges | 676-677,682 | 1785-1787 | inert | a heading |
| 129 | 8 insuring clause | Người được bảo hiểm sẽ được bồi thường cho | prepaid deposits or extra travel, capped by plan | 683-689 | 1788-1795 | encoded | part3-trip-liability: `8 — the amount payable` |
| 130 | 8 cause 1 | Người được bảo hiểm bị tử vong | death or Serious Injury or Illness of the Insured Person | 690 | 1796-1797 | encoded | part3-trip-liability: `8 — the cause is one the section names, as the provisos shape it` |
| 131 | 8 cause 2 | Người thân gia đình trực hệ | the same of family, Close Business Partner, insured companion | 691-694 | 1798-1802 | encoded | part3-trip-liability (finding F-CBP; VN-F6) |
| 132 | 8 cause 3 | Người được bảo hiểm được mời làm chứng | witness summons, jury service, quarantine | 695-696 | 1803-1804 | encoded | part3-trip-liability |
| 133 | 8 cause 4 | Thiên tai (động đất | natural disaster at the destination | 697-698 | 1805-1806 | encoded | part3-trip-liability (finding F-S8-CANCEL) |
| 134 | 8 cause 5 | Nơi cư trú chính ở Nước xuất phát của | destruction of the principal residence | 699-700 | 1807-1808 | encoded | part3-trip-liability (finding F-S8-CANCEL) |
| 135 | 8 proviso 1 | Người được bảo hiểm phải hủy bỏ chuyến đi | the trip abandoned or cut short | 702-705 | 1811-1813 | encoded | part3-trip-liability: `8 — the provisos are met` |
| 136 | 8 proviso 2 | Việc bồi thường sẽ được tính theo tỷ lệ | pro rata for the unused portion | 706-708 | 1814-1816 | encoded | part3-trip-liability: `8 — the amount payable` |
| 137 | 8 proviso 3 | Công ty sẽ không chi trả quyền lợi cho | not pregnancy, childbirth, gynecological disease | 709-711 | 1822-1824 | encoded | part3-trip-liability |
| 138 | 8 proviso 4 | Những nguyên nhân đó không phát sinh từ các | not known at issue; (Annual) not within 14 days before departure | 712-717 | 1825-1832 | encoded | part3-trip-liability (fork F-S8P4; finding F-S8-ANNUAL) |
| 139 | 8 proviso 5 | Thiên tai xảy ra đột ngột tại nơi đến | natural disaster after commencement of travel | 718-720 | 1833-1835 | encoded | part3-trip-liability |
| 140 | 8 proviso 6 | Nơi cư trú chính ở Nước xuất phát của | residence destroyed after commencement of travel | 721-726 | 1836-1837,1840-1843 | encoded | part3-trip-liability |
| 141 | 9 heading | MỤC 9 — “TRÁCH NHIỆM CÁ NHÂN” | Section 9, Personal Liability | 728-730 | 1845-1847 | inert | a heading |
| 142 | 9 insuring clause | Công ty sẽ bồi thường cho Người được bảo | legal liability to a third party, capped by plan | 731-737 | 1848-1853 | encoded | part3-trip-liability: `9 — the amount payable` |
| 143 | 9 causes | Với điều kiện trách nhiệm đó là do | accidental bodily injury or property damage | 738-740 | 1855-1857 | encoded | part3-trip-liability: `9 — the liability is covered` |
| 144 | 9 exclusions chapeau, (i) | Quyền lợi “Trách nhiệm cá nhân” | not payable by other insurance or a third party | 741-743 | 1858-1861 | encoded | part3-trip-liability |
| 145 | 9(ii) chapeau | phát sinh trực tiếp hoặc gián tiếp từ | arising directly or indirectly from | 745 | 1863 | encoded | part3-trip-liability: `9(ii) — the circumstance is excluded` |
| 146 | 9(ii)(a) | Trách nhiệm của người sử dụng lao động | employer's, contractual, family liability | 747-748 | 1864-1866 | encoded | part3-trip-liability (VN-F6) |
| 147 | 9(ii)(b) | Tài sản hoặc vật nuôi do Người được bảo | property or animals in the Insured Person's care | 749-750 | 1867-1868 | encoded | part3-trip-liability |
| 148 | 9(ii)(c) | Bất kỳ hành động cố ý | willful, malicious, unlawful or deliberate acts | 751 | 1869-1870 | encoded | part3-trip-liability (finding F-PL-UNLAWFUL, reading only) |
| 149 | 9(ii)(d) | Theo đuổi công việc kinh doanh thương mại hoặc | a trade, business or profession | 752 | 1871-1872 | encoded | part3-trip-liability |
| 150 | 9(ii)(e) | Việc sở hữu hay chiếm hữu đất đai hoặc | land or buildings, save a temporary residence | 755-756 | 1873-1874 | encoded | part3-trip-liability |
| 151 | 9(ii)(f) | Việc sở hữu | motor vehicles, aircraft, watercraft | 757-759 | 1875-1877 | encoded | part3-trip-liability |
| 152 | 9(ii)(g) | Các chi phí pháp lý do bất kỳ vụ | legal costs of criminal proceedings | 760 | 1878 | encoded | part3-trip-liability |
| 153 | 9(ii)(h) | Mất trí | insanity, drugs, liquor, firearms | 761-763 | 1879-1881 | encoded | part3-trip-liability (two readings, VN-F13) |
| 154 | 9(ii)(i) | Sự ký gửi hàng hóa | bailments, contractual licences, conveyances | 764-765 | 1882-1883 | encoded | part3-trip-liability |
| 155 | 9 judgements | VIỆC BỒI THƯỜNG NÀY SẼ KHÔNG ÁP DỤNG ĐỐI | no indemnity for a judgement outside the Country of Origin | 766-770 | 1884-1886 | encoded | part3-trip-liability: `9 — the judgement clause …` (finding F-PL-FORUM) |
| 156 | 10 heading | MỤC 10 — “TRỞ VỀ NƯỚC ĐỘT XUẤT” | Section 10, Incidental Home Country | 772-774 | 1888-1890 | inert | a heading |
| 157 | 10 insuring clause | Trong suốt Thời gian bảo hiểm | a return home of up to 14 consecutive days | 775-777 | 1891-1892,1894 | encoded | part3-trip-liability (two readings, VN-F17) |
| 158 | 10.1 | Người được bảo hiểm đã rời khỏi Nước xuất | had departed | 779 | 1897 | encoded | part3-trip-liability |
| 159 | 10.2 | Thời gian bảo hiểm tối thiểu là 31 ngày | Period of Insurance at least 31 days | 780 | 1898 | encoded | part3-trip-liability |
| 160 | 10.3 | Nguyên nhân của việc trở về nước không phát | cause not known before the effective date | 785-787 | 1899-1901 | encoded | part3-trip-liability |
| 161 | 10.4 | Việc trở về Nước xuất phát không nhằm mục | not to seek medical treatment | 788-789 | 1902-1903 | encoded | part3-trip-liability |
| 162 | 10.5 | Việc bảo hiểm sẽ tạm ngưng khi trở về | cover ceases (VI: is suspended) on return | 790 | 1904 | encoded | part3-trip-liability (two readings, VN-F17) |
| 163 | 10.6 | Công ty sẽ không chịu trách nhiệm cho những | no expenses of the return | 791-792 | 1905-1906 | encoded | part3-trip-liability: `10.6 — …` |
| 164 | 11 heading | MỤC 11 — “BỒI HOÀN MỨC MIỄN THƯỜNG BẢO HIỂM CHO XE Ô TÔ THUÊ” | Section 11, Rental Car Excess Cover | 794-796 | 1908-1910 | inert | a heading (VN-F29) |
| 165 | 11 insuring clause | Công ty sẽ bồi hoàn cho mức miễn thường | the excess on a valid car policy, capped by plan; the Insured Person drives | 797-803 | 1911-1918 | encoded | part3-trip-liability: `11 — the excess is covered` |
| 166 | 11.1 | Chiếc xe ô tô phải được thuê từ một | a recognized licensed rental company (VI: licensed) | 805 | 1920-1921 | encoded | part3-trip-liability (two readings, VN-F18) |
| 167 | 11.2 | Như là một phần của hợp đồng thuê xe | comprehensive car insurance bought with the rental | 806,808-809 | 1922-1925 | encoded | part3-trip-liability |
| 168 | 11.3 | Người được bảo hiểm phải tuân thủ tất cả | compliance with the contract, policy and local law | 810-812 | 1926-1928 | encoded | part3-trip-liability |
| 169 | 11.4 chapeau, (a)-(c) | Quyền lợi “Bồi hoàn mức miễn thường bảo hiểm | breach, off-road, wear and tear | 813,815-820 | 1934-1942 | encoded | part3-trip-liability |
| 170 | Part IV heading | BẢO HIỂM XE Ô TÔ THUÊ | IV. Rental car protection | 821 | 1944 | inert | a heading (VI has no IV.) |
| 171 | 12 heading | MỤC 12 — “BẢO HIỂM XE Ô TÔ THUÊ” | Section 12, Optional Rental Car Protection | 823-825 | 1946-1948 | inert | a heading |
| 172 | 12 eligibility | Bảo hiểm xe ô tô thuê chỉ áp dụng | only if applied for and paid | 826-829 | 1949,1951-1953 | encoded | part4-rental-car: `12 — the Insured Person bought Rental Car Protection` |
| 173 | 12 insuring clause | Công ty sẽ chi trả | up to 500,000,000 for fire, theft, collision, vandalism; repairs after an Accident | 830-837 | 1954-1961 | encoded | part4-rental-car (VN-F18) |
| 174 | 12 documents, cooperation | cho chiếc xe ô tô thuê. | police report, repairs; the right to refuse | 838-844 | 1961-1968 | encoded | part4-rental-car: `12 — the Company may refuse protection for the Accident` |
| 175 | 12 exclusions (a)-(f) | Quyền lợi lựa chọn “Bảo hiểm xe ô tô | intoxication, intent, assumed obligations, misuse, vehicle kinds, liability | 845,847-855,859-861 | 1970-1983 | encoded | part4-rental-car: `12(a)-(f) — the claim is excluded` |
| 176 | 12 deductible | Mức miễn thường | the first 5,000,000 | 862-863 | 1985-1986 | encoded | part4-rental-car (fork F-DEDUCT) |
| 177 | Other insurance | TRÁCH NHIỆM TỐI ĐA CỦA CÔNG TY ĐỐI VỚI | the ratable proportion, save Personal Accident | 865-872 | 1987-1994 | encoded | part4-rental-car: `the most payable where other insurance would cover the claim` (fork F-RATABLE) |
| 178 | Definitions heading | ĐỊNH NGHĨA | Definitions | 874 | 1995 | inert | a heading |
| 179 | Def. Accident | “Tai nạn” | beyond control, violent, external, visible | 876-877 | 1996-1998 | encoded | definitions |
| 180 | Def. Cash | “Tiền” | cash, notes, coins, negotiable instruments | 879 | 1999-2000 | inert | defined and used by no operative clause (finding F-UNUSED) |
| 181 | Def. Close Business Partner | “Cộng sự làm ăn thân thiết” | an associate with a share in the business | 881-882 | 2001-2002 | encoded | definitions |
| 182 | Def. Company | “Công ty” | Hung Vuong Insurance Corporation | 884 | 2003 | encoded | definitions: `the Company, reading the English` (a constant) |
| 183 | Def. Country of Origin | “Nước xuất phát” | the country of the first stage; same as Country of Residence | 885-889,893-897 | 2006-2014 | encoded | definitions |
| 184 | Def. Disability | “Bệnh tật” | an Illness or Injury and its sequelae | 898-901 | 2015-2018 | encoded | definitions |
| 185 | Def. Eligible Expenses | “Các chi phí hợp lệ” | medically necessary, recommended, at most customary | 902-907 | 2019-2024 | encoded | definitions (two readings, VN-F12) |
| 186 | Def. Emergency | “Tình trạng khẩn cấp” | a sudden change needing urgent intervention | 908-910 | 2025-2028 | inert | defined and used by no operative clause (finding F-UNUSED) |
| 187 | Def. Hospital | “Bệnh viện” | licensed hospital, not a spa or home, a resident Physician | 911-917,920 | 2029-2037 | encoded | definitions |
| 188 | Def. Illness | “Ốm đau” | a pathological deviation needing treatment | 921-923 | 2038-2040 | encoded | definitions |
| 189 | Def. Immediate Family Members | “Người thân gia đình trực hệ” | spouse, children, siblings, parents and so on | 924-927 | 2041-2043,2049-2050 | encoded | definitions (two readings, VN-F6) |
| 190 | Def. Injury | “Thương tích” | bodily, from an Accident; death in 12 months or treatment | 928-932 | 2051-2056 | encoded | definitions |
| 191 | Def. Insured Person | “Người được bảo hiểm” | named in the Certificate | 933-934 | 2057-2059 | encoded | definitions |
| 192 | Def. Loss of Limb | “Mất chi” | severance at or above wrist or ankle | 935-936 | 2060-2061 | encoded | definitions |
| 193 | Def. Loss of sight | “Mất thị lực” | entire and irrecoverable | 937 | 2062 | encoded | definitions |
| 194 | Def. Medicines and Drugs | “Thuốc và Dược phẩm” | prescribed medicines | 938-940 | 2065-2067 | inert | defined and used by no operative clause (finding F-UNUSED) |
| 195 | Def. Pair and Set | “Đôi và Bộ” | a fair share of the set's value | 941-944 | 2068-2071 | encoded | part3-property: `3 — the amount payable` (sets) |
| 196 | Def. Period of Insurance | “Thời gian bảo hiểm” | the period in the Certificate | 945-946 | 2072-2073 | encoded | nouns: the Certificate's first and last days |
| 197 | Def. Permanent Total Disablement | “Thương tật toàn bộ vĩnh viễn” | no work of any kind for 52 weeks, beyond hope | 947-951 | 2074-2077 | encoded | definitions |
| 198 | Def. Personal Effects | “Đồ dùng cá nhân” | articles worn or carried | 952-954 | 2078-2080 | inert | used only in the name of section 3 |
| 199 | Def. Physician / Surgeon | “Bác sĩ”/“Bác sĩ phẫu thuật” | qualified and licensed | 955-957 | 2081-2084 | inert | a qualification of the certifier; the findings are inputs |
| 200 | Def. Policy | “Hợp Đồng bảo hiểm” | the policy with Application, Certificate, endorsements | 958-961 | 2085-2088 | inert | says which documents make the contract; no rule turns on it (VN-F27) |
| 201 | Def. Pre-Existing Condition | “Tình trạng tồn tại trước” | before the effective date, with known symptoms | 962-966 | 2089-2093 | encoded | definitions (fork F-PEC) |
| 202 | Def. Public Conveyance | “Phương tiện vận chuyển công cộng” | public common carriers and travel-agency coaches | 967-970,972 | 2094-2099 | encoded | definitions (fork F-PC) |
| 203 | Def. Public Place | “Nơi công cộng” | publicly accessible places | 973-976 | 2100-2104 | inert | a question of fact; claims carry it as a BOOLEAN |
| 204 | Def. Serious Injury or Illness | “Thương tích nghiêm trọng hoặc ốm đau nặng” | certified dangerous to life and unfit; for family, dangerous and the trip ends | 977-984 | 2105-2113 | encoded | definitions |
| 205 | Def. Short Period Rate | “Mức phí bảo hiểm ngắn hạn” | the rate for the period in force | 985-987 | 2114-2117 | encoded | definitions: `the Short Period Rate, …` |
| 206 | Short Period Rate table | Khoảng thời gian trước khi hủy bỏ Mức phí | 20%, then 10% a month, 100% after 8 months | 989-994 | 2119-2123 | encoded | definitions; tests-tables (generated) |
| 207 | Def. Specialist | “Chuyên gia” | a Physician in one area | 996-997 | 2124-2125 | inert | used only inside the definition of Illness |
| 208 | Claims Procedure heading | THỦ TỤC YÊU CẦU BỒI THƯỜNG | Claims procedure | 999 | 2127 | inert | a heading |
| 209 | CP 1, notice | Phải nộp thông báo yêu cầu bồi thường cho | notice within 30 days of expiry (Annual: end of trip) | 1003-1006 | 2128-2131 | encoded | claims: `CP 1 — …` (deontic) |
| 210 | CP 1, Personal Liability | hiểm này (áp dụng đối với bảo hiểm du | written notice within 15 days of the incident | 1006-1009 | 2131-2135 | encoded | claims: `CP 1 — …` (deontic) |
| 211 | CP 1, information | muộn hơn 15 ngày kể từ khi xảy ra | information within 60 days of a written request | 1009-1013 | 2135-2140 | encoded | claims: `CP 1 — …` (deontic) |
| 212 | CP 1, proof | từ bỏ. | proof satisfactory to the Company, at the claimant's expense | 1013-1017 | 2140-2143 | inert | a judgement with no criteria a rule can apply (VN-F10; finding F-DISCRETION) |
| 213 | CP 2 chapeau | Tất cả mọi yêu cầu bồi thường phải được | a claims form and supporting information | 1018-1020 | 2144-2145 | encoded | claims: `CP 2 — the documents a claim under the section needs` |
| 214 | CP 2(a) | Trong trường hợp Tai nạn cá nhân | Personal Accident documents | 1022-1026 | 2146-2150 | encoded | claims |
| 215 | CP 2(b) | Trong trường hợp Chi phí y tế | medical, assistance, cancellation documents | 1027-1029,1031-1037 | 2151-2154,2160-2164 | encoded | claims |
| 216 | CP 2(c) | Trong trường hợp mất mát | baggage, documents, money; reports within 24 hours | 1038-1050 | 2165-2176,2179-2180 | encoded | claims (VN-F25) |
| 217 | CP 2(d) | Trong trường hợp Chuyến đi bị trì hoãn | travel delay documentation | 1051-1053 | 2181-2183 | encoded | claims |
| 218 | CP 2(e) | Đối với Trách nhiệm cá nhân | liability notification and court papers | 1054-1063 | 2184-2193 | encoded | claims |
| 219 | CP 2(f) | Trong trường hợp Bồi hoàn mức miễn thường bảo | rental car excess documents | 1064-1069 | 2194-2199 | encoded | claims |
| 220 | CP 2(g) | Trong trường hợp lựa chọn Bảo hiểm xe ô | rental car protection documents | 1070-1072 | 2200-2203 | encoded | claims |
| 221 | Version marker | Vs.022014 | Vs. 022014 (both texts) | 1077 | 2208 | inert | a version label; NOTES.md §1 |

Totals: **184 encoded**, **37 inert**, **0 out-of-scope, 0 deferred** (221 rows).

## 3. Fork register

Every ambiguity met, the readings seen, the one taken and the text that licenses it.
A fork resolved by nothing in the sources says so.
`LAW-` forks record where the Law on Insurance Business (the aid, cited by its line) fills or may override the wording; none is encoded and none is silently resolved.

| # | where | the question | readings | taken, and why |
| --- | --- | --- | --- | --- |
| F-DAYS | CP 1, AT 1, AT 5, 1A.1(b), 1A.2(i), 8 proviso 4, 10 | Are the unqualified "days" calendar days? | (i) calendar days; (ii) working days | **(i)**. Clause 14 and AT 6 say "consecutive calendar days"; the wording has no notion of a working day anywhere. |
| F-MONTHS | clause 4 (src 34, 1110); 2.1 (src 428, 1525) | How is "6 calendar months" counted from 31 August? | (i) to the same day number, clamped to the month's end (28 February); (ii) to 1 March | **(i)**, `add months`. Nothing in the text decides it; a test sits on 31 August. |
| F-START | clause 13 (src 142-153) | Cover "commences on the date and time of departure": what if the departure precedes the Certificate's first day? | (i) at departure regardless; (ii) at the later of departure and the first day of the Period of Insurance | **(ii)**: the Period of Insurance is "the period of insurance specified in the Insurance Certificate" (src 945); clause 13 governs within it. |
| F-C7 | clause 7 (src 111-114, 1203-1207) | Does "(unless it is Annual Travel Policy)" except Annual Travel from the whole clause, or only from the Policyholder's bar? | (i) the whole clause, AT 3 governing Annual Travel; (ii) only "or by the Policyholder" | **(i)**: AT 3 lets both sides cancel an Annual Travel policy and gives refunds, which (ii) would contradict. |
| F-C14 | clause 14 (src 158-159) | Does the 180-day maximum bind Annual Travel? | (i) yes, literally ("this Policy"); (ii) no: AT 6 limits each trip to 90 days instead | **(ii)**. Under (i) no annual policy can exist, while AT 3 speaks of an "annual premium" and the Short Period Rate runs past eight months. Finding F-C14 records (i). |
| F-AGE | clause 15 (src 160-164, 1260-1263) | When are the age limits tested? | (i) 6 weeks to 75 on the first day of the Period of Insurance, and the 76 bar on the date of the event; (ii) both at issue; (iii) both at the event | **(i)**: "the age limit for person(s) insured" speaks of becoming insured; "once the Insured Person reaches the age of 76" speaks of the moment a benefit is claimed. So read, "75 years" runs to the day before the 76th birthday and the two sentences agree. |
| F-ACCOMP | clause 15, second sentence | A child under 7 "must be accompanied by an adult who is also insured": what follows if not? | (i) a condition precedent, through clause 1; (ii) no consequence | **(i)**: clause 1 makes "the due observance and fulfillment of the terms" a condition precedent to any liability. |
| F-AGE18 | 2.4, 2.7, 6.4 | "children under 18 years of age": at what date? | (i) the date of the Accident or loss; (ii) the start of the Period | **(i)**: the benefit is measured at the event. |
| F-AT3 | AT 3 (src 217-223, 1320-1326) | A Policyholder who cancels after a claim, or without returning the card: what refund? | (i) none; (ii) pro rata; (iii) not provided for | **(i)**: "Provided that … the Policyholder shall be entitled to a refund"; the proviso is the only source of the entitlement. |
| F-AT3N | AT 3 | A cancellation on less than 7 days' notice by registered letter. | (i) refused as not provided for; (ii) effective on the seventh day | **(i)**, `REFUSE`; the text states only the 7-day route. |
| F-AT5 | AT 5 (src 240-242, 1342-1344) | "commences on 14 days before the scheduled commencement date": which day? | (i) the 14th day before, inclusive; (ii) the 13th | **(i)**. |
| F-AT6 | AT 6 | Is the day of departure day 1 of the 90? | (i) yes; (ii) day 0 | **(i)**: "90 consecutive calendar days" counts the days of the trip. |
| F-PRORATA | AT 3 (src 213-215) | "the premium less the pro-rata portion thereof for the period the Policy has been in force": pro rata by what? | (i) days of the Period of Insurance; (ii) months | **(i)**. |
| F-SPR | Short Period Rate table (src 989-994, 2119-2123) | "For each successive month after the first month": a month begun, or a month completed? | (i) begun; (ii) completed | **(i)**. Under (i), 20% + 8 × 10% = 100% exactly when the ninth month begins, which is the table's third row, "More than eight (8) months": the arithmetic closes. A cancellation on the same day of the next month is still in the first month. |
| F-PEC | 5.1 (src 38, 1120); Pre-Existing Condition (src 962, 2089) | 5.1 excludes "Pre-existing Illness or Injury", a phrase no definition has. | (i) read through the definition of Pre-Existing Condition; (ii) any condition that existed before | **(i)**: the definition is the wording's only account of "pre-existing". |
| F-EXCL | 1B.4(c) (src 374-375, 1465-1466) | "Excluded Conditions" is used and never defined. | (i) the conditions clause 5 excludes; (ii) those and the section exclusions; (iii) not determinable | **(i)**, which `the Disability is covered under section` already tests. Recorded as finding F-UNDEF. |
| F-5DAYS | 1B.6 (src 393, 1489) | "confined in a hospital for more than 5 days". | (i) more than 120 hours; (ii) more than 5 calendar days | **(i)**, matching the English "complete day" counting of 1B.4. |
| F-VIDAY | 1B.4, Vietnamese (src 1451) | "1.000.000 VND/ngày": what is a day? | (i) each calendar day as an inpatient; (ii) part days pro rata | **(i)**. Either reading pays more than the English for a stay of 25-47 hours (VN-F5). |
| F-CHECKUP | 1A.2(h) (src 303-306) | A check-up "incidental to the treatment or diagnosis of a covered Disability" is excepted from (h); 1A.1(a) does not name check-ups. | (i) not payable: 1A.1 includes "only the following expenses"; (ii) it is a diagnostic test or consultation | **(i)** for an expense of that kind; a caller who classes it as a diagnostic test gets (ii). Finding F-MED-CLOSED. |
| F-1A-AFTER | 1A.2(i) (src 307-312) | An expense abroad after cover ended, by an Insured Person who could return. | (i) not covered; (ii) covered; (iii) not provided for | **(iii)**, `REFUSE`: (i) speaks only of the Insured Person "unable to return". |
| F-LAPTOP | 3.3 (src 507-509), 3.6(c) (src 529-533), 3.4 "Subject to paragraph (6)" | Does 3.6(c) ("computer equipment", "portable electronic devices") exclude the laptop 3.3 gives a limit to? | (i) yes, literally, and 3.4 makes the indemnity subject to 3.6; (ii) the specific laptop limit prevails over the general exclusion | **(i)**. Reading (ii) is what Art. 24 would likely favour. Finding F-LAPTOP. |
| F-3PARTY | 3.2(a) (src 501-503) | "the police in case of theft, loss or willful damage by a third party". | (i) the perils theft, robbery, burglary; (ii) any loss | **(i)**: "by a third party" qualifies the list. |
| F-LUGGAGE | 3.6(k), English (src 556) | "Damage to luggage": the bags, or the bags and their contents? | (i) bags and contents (luggage = baggage); (ii) the containers only | **(i)** for the English, the dictionary sense; (ii) is the Vietnamese "đồ đựng hành lý" (VN-F8). |
| F-SET | 3.3 | Is the camera set one set however the claim names it? | (i) yes; (ii) only if the claim groups it | **(i)**: "will be treated as a set". |
| F-FINAL | 4.6 (src 582-583) | "No cover … after the Insured Person … reaches the final destination." | (i) the end of a journey that does not return home, as 1A.2(i) uses the words; (ii) the destination abroad | **(i)**. Under (ii) the cover would end at the moment the 6 hours begin (finding F-BAGDELAY, reading only). |
| F-RIOT | 5.3, English (src 59-61) | Does "assuming the proportions of or amounting to a popular rising" govern mutiny and riot, or only civil commotion? | (i) all three; (ii) civil commotion only | **(i)**, the usual reading of this standard clause (outside knowledge, unverified). The Vietnamese drops the qualifier (VN-F2). |
| F-DRUGS | 5.5 (src 80-81) | "the use of alcohol, drugs or solvents other than those prescribed": does "other than prescribed" reach alcohol? | (i) drugs and solvents only; (ii) all three | **(i)**: a physician does not prescribe alcohol. |
| F-VIAIR | 5.7, Vietnamese (src 1184-1186) | "máy bay không được cấp giấy phép hợp lệ của một hãng hàng không không được công nhận". | (i) an aircraft not validly licensed AND of an airline not recognized; (ii) either | **(i)**: one noun phrase with two negated modifiers. Under either, the Vietnamese excludes only fare-paying passengers (VN-F1). |
| F-PC | Public Conveyance (src 967-972) | Is the list "such as multi-engined aircrafts, buses …" closed? | (i) illustrative; (ii) closed | **(i)**: "such as". |
| F-PAROWS | 2.3 table | The rows are not all defined terms. | (i) a row that is a defined term is tested against its definition ("Total loss of … limbs" against Loss of Limb); the "loss of use" rows are taken as claimed; (ii) all as claimed | **(i)**. |
| F-S7P5 | 7.5 (src 670-674) | "(applicable for Annual Travel)": all of 7.5, or the scheduled-commencement limb? | (i) that limb; (ii) the whole proviso | **(i)**, matching the same parenthesis in 8 proviso 4 (F-S8P4). |
| F-S8WIN | clause 13 and AT 5 with section 8 | Is the Cancellation Charges cover tested on the date the cause arose or on the date of cancelling? | (i) the cause; (ii) the cancellation | **(i)**: the insured perils are the causes 1-5. Under (ii) an Annual Travel cancellation for a cause arising more than 14 days out would be covered; finding F-S8-ANNUAL holds under (i). |
| F-S8P4 | 8 proviso 4 (src 712-717, 1825-1832) | Does "(applicable for Annual Travel)" govern the whole proviso or only the 14-day limb? | (i) the 14-day limb; (ii) the whole | **(i)**: the "known to exist on the date of issue" limb applies to every product, as it must for a single trip. |
| F-DEDUCT | 12 (src 830-831, 862-863) | Deductible before or after the 500,000,000 maximum? | (i) before: "the first VND 5,000,000 of eligible expenses"; (ii) after | **(i)**. They differ only above 505,000,000; tests sit on 504 and 600 million. |
| F-RATABLE | other insurance (src 868-872) | "its ratable proportion" is not defined. | (i) by limits; (ii) by amounts payable | **(i)**, the Law's rule for double insurance (Art. 49(2), Law line 969-973). |
| F-PLASAP | CP 1 (src 1006-1009) | "as soon as possible and in any event not later than 15 days". | — | Only the 15-day bound is encoded; "as soon as possible" has no measure. |
| F-AT1 | AT 1, English (src 203-205) | "the Policyholder shall be given written notice to the Company". | (i) the Policyholder must give notice (the Vietnamese); (ii) as written, the Policyholder receives notice | **(i)** (VN-F14). |
| F-12REF | 12 (src 842-844) | "the Company reserves the right to refuse any protection". | (i) a power the Company may use; (ii) a bar | **(i)**: the encoding says when the power is open and pays "unless the Company refuses" (phrasebook 8.5). |
| F-C17VI | 17, Vietnamese (src 1281-1282) | The Vietnamese makes the award a condition of liability and does not mention a right of action. | — | Refused by name in the Vietnamese reading (VN-F15). |
| LAW-CONTRA | Law Art. 24 (line 588-591) | Where the two texts differ, does the unclear-term rule pick the reading favourable to the buyer? | (i) yes, clause by clause; (ii) no: two language versions are not "an unclear term" | **Not resolved**; both readings are encoded. Under (i) a policyholder takes the better text clause by clause: the Vietnamese for VN-F1, F5, F8, F9, F10, F17 (resumption), F18; the English for VN-F2, F6, F7, F11, F13, F17 (purpose); either for F3, F4, F12, depending on the facts. |
| LAW-SUBRO | clause 9; Law Art. 16(4) (line 402-406), Art. 38 (line 792-799), Art. 54(3) (line 1043-1049) | Clause 9 subrogates the Company after "any payment". The Law withholds subrogation from health insurance (whose definition, line 130-131, covers injury, accident and illness) and from recovery against parents, spouse or children. | — | **Not resolved**: sections 1A, 1B and 2 look like health insurance; whether clause 9 is void there is for an expert. |
| LAW-TERM | AT 3; Law Art. 26 (line 623-635) | AT 3 lets the Company cancel an Annual Travel policy on 7 days' notice for any reason; Art. 26 lists the cases in which a party may terminate unilaterally. | — | **Not resolved**. |
| LAW-NOTICE | CP 1; 3.1, 5.1, 6.1; Law Art. 19(3) (line 441-444), Art. 46 (line 917-931; (2) at 928-931) | Late notice for force majeure may not trigger an exclusion; a reduction for late notice is limited to the insurer's loss and needs an agreed sanction. CP 1 states no sanction; clause 1 makes all terms conditions precedent. | — | **Not resolved**. |
| LAW-CLAIM | CP 1; clause 4; Law Art. 30 (line 706-717) | The Law gives one year from the insured event to file a claim dossier; CP 1 wants notice within 30 days of expiry, and clause 4 ends a disclaimed claim after 6 months. | — | **Not resolved**. |
| LAW-PAY | (silent); Law Art. 31 (line 718-729) | The wording sets no deadline for the Company to pay; the Law supplies 15 days from a complete dossier, with interest after. | — | Not encoded; COMPARABLES.md says "not stated". |
| LAW-FRAUD | clauses 7, 16; Law Art. 22(2) (line 543-553) | On intentional misstatement the insurer may rescind but must return the premium less reasonable costs; clauses 7 and 16 refund nothing. | — | **Not resolved**. |
| LAW-UNDEF | Law Art. 87(2)(b) (line 1765-1767) | Terms of art must be defined in the rules; finding F-UNDEF lists those that are not. | — | **Not resolved**. |
| LAW-EXCL | Law Art. 19(2) (line 435-440) | An exclusion binds only if explained and the buyer's understanding evidenced. | — | A fact about the sale, outside the wording; not encoded. |

## 4. Findings

The hostile reading, as a policyholder's lawyer and as the insurer's.
A finding is a defect in the instrument as written, not an ambiguity I resolved (those are §3).
Each has its source lines, a minimal scenario, and the evidence: an assertion in a named test module, or "reading only".

### 4.1 Where the English and the Vietnamese differ (EN ≠ VI)

| # | where | English (src) | Vietnamese (src) | scenario | changes an answer? | evidence |
| --- | --- | --- | --- | --- | --- | --- |
| VN-F1 | 5.7, flying | "entering/descending or flying in any aircraft other than a properly licensed aircraft operated by a recognized airline in which the Insured Person is traveling as a fare-paying passenger" (93-96) | "lên/xuống hoặc đi trên máy bay như là một hành khách có mua vé trên máy bay không được cấp giấy phép hợp lệ của một hãng hàng không không được công nhận" (1183-1186): a fare-paying passenger on an aircraft not validly licensed, of an airline not recognized | injured as a non-paying passenger in a licensed private plane | **yes**: English excluded, Vietnamese covered (VND 18,000,000 of medical expenses) | `pc-travel-tests-en-vi.l4`, `VN-F1` |
| VN-F2 | 5.3, riot | "mutiny or riot or civil commotion assuming the proportions of or amounting to a popular rising" (59-61) | "nổi dậy chống đối hay dấy loạn hoặc bạo động dân sự do các bộ phận trong nhân dân hoặc một số dân chúng gây nên" (1143-1145): caused by sections of the people, no popular-rising test | hurt in a street riot that is no popular rising | **yes**: English covered (18,000,000), Vietnamese excluded | `VN-F2` |
| VN-F3 | 5.7, climbing | "rock or mountain climbing normally involving the use of ropes or other equipment" (90-91) | "leo đá hoặc leo núi có sử dụng dây thừng hoặc thiết bị khác" (1181-1182): climbing using ropes | an unroped climb of a route that normally needs ropes; an easy scramble done roped | **yes**, both ways | `VN-F3` |
| VN-F4 | clause 8, extension | "the total length of the trip does not exceed 180 days" (119) | "tổng thời gian được bảo hiểm không vượt quá 180 ngày" (1212-1213): the total time insured | a 200-day trip insured for 170 days asks to extend | **yes**: English refuses, Vietnamese grants | `VN-F4` |
| VN-F5 | 1B.4, the day | "VND 1,000,000 for each complete day" (355, 360) | "1.000.000 VND/ngày" (1451): per day | 36 hours as an inpatient over two calendar days | **yes**: 1,000,000 against 2,000,000 | `VN-F5 and VN-F10` |
| VN-F6 | Immediate Family Members | "parents", beside "children (natural or adopted)" (925-926) | "cha mẹ ruột" (natural parents), beside "con ruột hoặc con nuôi" (2042-2043) | the Insured Person's adoptive mother dies and the trip is cut short; she is hurt by the Insured Person; she visits the Insured Person in hospital | **yes**: section 8 pays 25,000,000 or 0; section 9(ii)(a) excludes or pays 370,000,000; 1B.6 pays 35,000,000 or 0 | `VN-F6` |
| VN-F7 | 1B.7 | "as a result of Serious Injury, Illness, or hospitalization, or death" (396-398) | "do Người được bảo hiểm bị Thương tích nghiêm trọng hoặc Ốm đau nặng, nằm viện hay tử vong" (1494-1496): serious Illness only | the Insured Person's ordinary illness leaves the children unattended | **yes**: 40,000,000 or 0 | `VN-F7` |
| VN-F8 | 3.6(k) | "Damage to luggage" (556) | "Hư hại đồ đựng hành lý" (1658): damage to luggage containers | clothes damaged in a bag the carrier mishandled | **yes**: 0 or 3,000,000 | `VN-F8` |
| VN-F9 | 1B.9 | referral services "may be provided" (413-415) | "sẽ cung cấp" (will provide) (1509-1511) | a requested referral service is never provided | **yes**: a permission unused (FULFILLED) or a duty breached (BREACH BY the Company) | `VN-F9` (`#TRACE`) |
| VN-F10 | 1B.4(b) | "Documentation satisfactory to the Company" (367) | "Chứng từ thích hợp" (appropriate documents) (1459) | documents produced that the Company says do not satisfy it | **yes**: 0 or 3,000,000 | `VN-F5 and VN-F10`; CP 1 "proof satisfactory to the Company" (1014) against "bằng chứng thỏa đáng" (2141) is the same difference, reading only |
| VN-F11 | 5, perils and report | "theft, robbery, burglary and accidental loss" (589-590); report "within 24 hours or as soon as practicable" (600-601) | "trộm cắp, cướp hoặc tai nạn" (1690); "trong vòng 24 giờ" (1700-1701) | a passport mislaid; a theft reported after 30 hours, as soon as practicable | **yes**: 15,000,000 or 0 in each | `VN-F11` |
| VN-F12 | Eligible Expenses | "not to exceed normal and customary charges for the same in the country in which they are incurred" (905-907) | "không vượt quá chi phí bình thường theo thông lệ cho cùng Bệnh tật ở nước mà họ trả chi phí điều trị" (2022-2024): where they pay | treated abroad (customary 12,000,000), paid at home (customary 8,000,000) | **yes**: 12,000,000 or 8,000,000 | `VN-F12` |
| VN-F13 | 9(ii)(h) | "the use of firearms" (763) | "sử dụng vũ khí" (the use of weapons) (1881) | a liability arising from the use of a knife | **yes**: 370,000,000 or 0 | `VN-F13` |
| VN-F14 | AT 1 | "the Policyholder shall be given written notice to the Company" (204-205) | "Chủ hợp đồng phải thông báo bằng văn bản cho Công ty" (1301-1302) | — | reading only: the English as written gives the Policyholder no duty; encoded on the Vietnamese (F-AT1) | reading only |
| VN-F15 | clause 17 | an award is a condition precedent "to any liability or right of action against the Company" (184-186) | a condition of "trách nhiệm bồi thường của Công ty" (the Company's liability to pay) (1281-1282) | a suit before any award | **yes**: the English bars it; the Vietnamese does not speak of it (refused) | `VN-F15` |
| VN-F16 | 2.6 | "unless a selected beneficiary has been advised to the Company in writing" (463-464) | "trừ khi Người được bảo hiểm đã có văn bản chỉ định Người thụ hưởng" (1560-1561): designated by the Insured Person | a Policyholder (not the insured) names a beneficiary | possibly; reading only (the encoding takes the designation as given) | reading only |
| VN-F17 | 10 | "may return to the Country of Origin for incidental visits"; 10.5 "Coverage ceases on return" (775-777, 790) | "có thể trở về Nước xuất phát vì lý do đột xuất … cho mỗi lần"; "Việc bảo hiểm sẽ tạm ngưng" (1891-1894, 1904) | a 7-day home visit, then back abroad; a planned visit | **yes**: after resuming, English not covered, Vietnamese covered; a planned visit is allowed in English only | `VN-F17` |
| VN-F18 | 11.1, 12 | "a recognized licensed car rental company" (805, 834-835) | "công ty cho thuê xe ô tô có giấy phép" (1920-1921, 1958-1959): licensed | a licensed company no one has "recognized" | **yes**: 0 or 8,000,000 (11); 0 or 45,000,000 (12) | `VN-F18` |
| VN-F19 | 7(a) | "for each full 6 hours delay" (645-646) | "cho mỗi 6 tiếng đồng hồ bị trễ" (1749): no "full" | a 13-hour delay | reading only: on the natural reading both count two periods; a buyer-favourable reading of the Vietnamese (LAW-CONTRA) counts three | reading only |
| VN-F20 | 7(b) | "VND f10,000,000 or Plan B and Executive Plan" (651): a misprint | "10.000.000 VND cho Hạng B và Hạng phổ thông" (1754-1755) | — | no: the Vietnamese settles the English misprint as 10,000,000; the table generator parses both and they agree | `pc-travel-tests-tables.l4` |
| VN-F21 | title | "TRAVEL INSURANCE POLICY" (1) | "QUY TẮC BẢO HIỂM DU LỊCH TOÀN CẦU" (1079-1080): global | — | no: the cover's territory is set by the Country of Origin definition in both | reading only |
| VN-F22 | 5.8 | "Trekking at an altitude limit greater than 5,000 meters" (102) | "Ði tìm hiểu thiên nhiên ở độ cao trên 5.000 mét" (1194): going out to explore nature | a visitor driven to a 5,200 m viewpoint | possibly: not trekking, arguably exploring nature; reading only | reading only |
| VN-F23 | clause 6 | "leisure travel or business travel (limited to administrative and non manual works only)" (106-107) | "du lịch hoặc đi công tác nước ngoài" (1200-1201): business travel abroad | — | no, on this wording: cover is outside the Country of Origin anyway | reading only |
| VN-F24 | 1A.2(d) | expenses "for which a third party may be liable" (291-292) | "do một bên thứ ba có trách nhiệm chi trả" (1390): a third party that is liable | a third party is possibly, not certainly, liable | possibly; reading only | reading only |
| VN-F25 | CP 2(c), (f), (g) | "certified written copy" of police reports (1045, 1066, 1071) | "bản sao có công chứng" (a notarised copy) (2173, 2196, 2201) | a copy certified by the police station, not notarised | possibly; reading only (documents are not tested for form) | reading only |
| VN-F26 | CP 2 | "a completed Travel Insurance Claims Form" (1018-1019); (a) "the relevant coroner's report" (1026) | "đơn Thông báo tổn thất" (a loss notification form) (2144-2145); "biên bản của nhân viên điều tra" (an investigator's report) (2150) | — | reading only | reading only |
| VN-F27 | Policy; 1B.1; 11-12 headings; 17 | "approved by an executive officer" (960-961); "the most economical form of conveyance" (339); "(if applicable as per Insurance Certificate)" (796, 825); "the arbitrators at the discretion of the Company may be a Surgeon or Physician" (181-182) | "nhân viên có thẩm quyền" (an authorised employee) (2087-2088); adds "với đầy đủ phương tiện y tế cần thiết" (with the necessary medical equipment) (1435); "(căn cứ vào Bảng liệt kê quyền lợi)" (1910, 1948); "các trọng tài do Công ty chỉ định" (the arbitrators the Company appoints) (1278-1279) | — | reading only, each | reading only |

**List checks.**
Clause 5.2 lists the same 22 Disabilities in the same order in both texts (the Vietnamese writes "cao huyết áp, các bệnh tim mạch" with a comma where the English joins "hypertension or cardiovascular diseases" with "or"); clause 5.7 the same 13 activities; 1A.2 nine exclusions (a)-(i) in both; 3.6 eleven (a)-(k) in both; 9(ii) nine (a)-(i) in both; 11.4 three; 12 six; section 8 five causes and six provisos; the definitions 28 terms in the same order; the Personal Accident table six rows with the same percentages; the Short Period Rate table three rows with the same rates.
Every money figure in the plan tables and every single figure the sections print agree between the texts (§5, 0 mismatches).

### 4.2 Defects in the instrument (both texts)

| # | defect | source | minimal scenario | evidence |
| --- | --- | --- | --- | --- |
| F-HEART | Clause 5.2 excludes 22 named Disabilities "whether occurring prior to or during the Period of Insurance": a heart attack, a stroke, a cancer, a kidney stone, an ulcer or diabetes that first strikes during the trip is excluded from every section, emergency evacuation included. The commonest travel emergencies are not covered. | 40-54, 1123-1137 | a traveller with no history has a heart attack on day 5 | `pc-travel-tests.l4`: medical expenses 0 for a Disability arising from "hypertension or cardiovascular diseases" |
| F-MED-BREAKDOWN | 1A.1(a) caps at VND 20,000,000 a day the charges "if no detailed breakdown of charges is provided"; the proviso requires every expense to "be supported by a detailed breakdown of charges". The no-breakdown cap can never be reached: an unitemised hospital day pays nothing, not 20,000,000. | 266-270, 277-279; 1367-1370, 1377-1378 | a day of all-in hospital charges of 15,000,000, unitemised | `pc-travel-tests.l4`: 0 |
| F-MED-CLOSED | 1A.1 includes "only the following expenses", which do not name eyeglasses, hearing aids or check-ups; 1A.2(c) and (h) then except such items after an accidental Injury or when incidental to a covered Disability. The exceptions take back an exclusion from items the cover never included. | 256-270, 287-290, 303-306 | eyeglasses needed after an accident abroad | `pc-travel-tests.l4`: 0 |
| F-LAPTOP | 3.3 prints a laptop limit (20,000,000 Premier, 10,000,000 others); 3.6(c) excludes "computer equipment" and "portable electronic devices", and 3.4 makes the indemnity "Subject to paragraph (6)". A stolen laptop pays nothing; the limit is dead text. 3.3 is also the one table that pairs Premier alone, without Plan A. | 507-509, 511, 529-533; 1606-1608, 1611, 1630-1635 | a Premier traveller's laptop is stolen | `pc-travel-tests.l4`: 0, beside the limit of 20,000,000 |
| F-S8-ANNUAL | For Annual Travel the Cancellation Charges cover runs from 14 days before the scheduled commencement date (AT 5); proviso 4 excludes a cause arising "within 14 days prior to the scheduled departure date". Every cause arising while the cover is in force is excluded; a cause arising earlier arose before the cover began (fork F-S8WIN). | 240-242, 712-717; 1342-1344, 1825-1832 | an Annual Travel traveller falls seriously ill 7 days, or 22 days, before departure | `pc-travel-tests.l4`: 0 both, against 30,000,000 for the same illness under a single-trip policy |
| F-S8-CANCEL | Causes 4 (natural disaster) and 5 (destruction of the residence) are bound by provisos 5 and 6 to events "after commencement of travel", so they can never found a cancellation, which happens before travel; the Cancellation Charges cover (clause 13) ends on the departure date. | 697-700, 718-726; 1805-1808, 1833-1843 | a typhoon hits the destination a week before departure | `pc-travel-tests.l4`: 0; the same typhoon after commencement founds a curtailment, 25,000,000 |
| F-CBP | Cause 2 needs "Serious Injury or Illness" of a Close Business Partner; the definition gives the term a meaning for the Insured Person and for an Immediate Family Member only. | 691-694, 977-984; 1798-1802, 2105-2113 | the insured's business partner is gravely ill | `pc-travel-tests.l4`: `#ASSERT REFUSED` |
| F-PA-NOTICE | CP 1 wants notice "within 30 days of the expiry of this Policy"; section 2 pays for death or disablement "within 12 calendar months of the Accident", and Permanent Total Disablement needs 52 consecutive weeks. On a 20-day trip the notice period closes on day 50; a death on day 188 is covered and cannot have been notified in time. 1A.1(b) does the same for follow-up expenses up to 90 days after return. A time-bar shorter than the time the same document allows for the loss. | 1003-1005, 427-430, 947-951, 271-275; 2128-2131, 1524-1528, 2074-2077, 1371-1374 | Accident on 5 April, death on 5 October; follow-up treatment on 14 July | `pc-travel-tests.l4`, "The hostile reading": the deadline is 138 days before the death; 52 weeks ends after the deadline; the 14 July follow-up pays 40,000,000 after a 20 May deadline |
| F-PA-ONCE | 2.2: "upon any benefit … becoming payable no further liability shall be attached"; 2.5 caps "any and all events" at 100% of the sum insured. After a 50% benefit for the loss of use of one limb, a later death pays nothing; 2.5 never binds. | 431-435, 456-459; 1529-1532, 1552-1556 | a 50% claim, then death | `pc-travel-tests.l4`: 0 when a benefit has already become payable |
| F-PL-FORUM | Personal Liability covers events abroad but "SHALL NOT APPLY IN RESPECT OF JUDGEMENTS WHICH ARE NOT IN THE FIRST INSTANCE DELIVERED BY OR OBTAINED FROM A COURT OF COMPETENT JURISDICTION WITHIN THE COUNTRY OF ORIGIN"; the injured third party will ordinarily sue where the accident happened. | 766-770; 1884-1886 | a tourist injures a pedestrian in Bangkok and is sued there | `pc-travel-tests.l4`: 0 under a foreign judgement, 370,000,000 under none |
| F-C14 | Read literally, clause 14 caps "this Policy" at 180 days, which no annual policy can meet, while AT 3 and the Short Period Rate presuppose policies in force more than eight months. | 158-159, 211-223, 985-994 | an Annual Travel certificate for 2026 | `pc-travel-tests.l4`: `clause 14, read literally` FALSE |
| F-S10-EN | Read literally, the English section 10 ends the cover ("Coverage ceases on return") that it exists to preserve across a home visit; it confers nothing. The Vietnamese suspends it. | 775-792; 1891-1906 | a 7-day visit home | `pc-travel-tests-en-vi.l4`, `VN-F17` |
| F-24H | 5.1 counts 24 hours from when the Insured Person "is aware of the loss"; CP 2(c), which lists Loss of Travel Documents, wants reports "within 24 hours of the occurrence". A theft discovered two days late meets the one and fails the other. | 600-604, 1046-1047; 1700-1703, 2174-2175 | a passport stolen on 6 April, missed until 8 April | `pc-travel-tests.l4`: section 5 pays 15,000,000; CP 2(c) fails at 58 hours |
| F-UNDEF | Terms that carry weight and are never defined: "Excluded Conditions" (1B.4(c)); "Pre-existing Illness or Injury" (5.1, not the defined Pre-Existing Condition); "Insurance Certificate", "Schedule of Benefit(s)"/"Benefit Schedule" (three spellings, and AT 5 has the Schedule specify the Country of Residence where the definition has the Certificate do it); "Application"; "Policyholder"; "Annual Travel", "Travel Flex", "Bon Voyage"; the five plans; "Car Insurance Policy"; "registered medical practitioner"; "recognized" (airline, rental company); "the Insured". | 374-375, 38, 229-231, 893-894, 960, 1019 | — | reading only; LAW-UNDEF |
| F-UNUSED | Defined and used by no operative clause: Cash, Emergency, Medicines and Drugs; Personal Effects appears only in a heading; Specialist only inside another definition. | 879, 908-910, 938-940, 952-954 | — | reading only |
| F-DISCRETION | Discretion given to the Company with no criteria: depreciation "applied wholly at the discretion of the Company" (3.6(e)); payment or "at its option by replacement or repair" (3.4); documentation and proof "satisfactory to the Company" (1B.4(b), CP 1); "may result in denial" (16); "reserves the right to refuse" (12); renewal "at the option of the Company" (AT 4); repatriation decided "jointly and exclusively" with the Company (1B.2); the arbitrators "at the discretion of the Company" (17); prior approval for emergency evacuation (1B Note), which an unconscious traveller cannot seek. | 538-542, 511-515, 367-368, 1014, 168-169, 842-844, 224-225, 348-350, 181-182, 417-420 | — | reading only; where it is encoded, the rule says when the power is open (`clause 16 — the Company may deny the claim`, `12 — the Company may refuse protection for the Accident`) |
| F-PL-UNLAWFUL | 9(ii)(c) excludes liability arising from "any willful, malicious, unlawful or deliberate act". Legal liability to a third party ordinarily arises from a wrongful act; read widely, "unlawful" swallows the cover. | 751; 1869-1870 | a careless (negligent, hence unlawful?) act injures a passer-by | reading only (the encoding takes the classification as an input) |
| F-ALCOHOL | 5.5 excludes losses "arising from … the use of alcohol" with no threshold of intoxication. | 80; 1167-1168 | a fall after one glass of wine | reading only (causation is an input) |
| F-BAGDELAY | Under fork F-FINAL (ii), 4.6 removes Baggage Delay cover at the moment it starts to run; under (i) it does not. The insurer has the ambiguity to argue. | 562-565, 582-583 | a delayed bag on arrival at a single-destination holiday | reading only |
| F-CANCEL-REFUND | A single-trip policy is "non-cancelable" and "no refund of premium will be made once this Policy has been issued", even for a trip cancelled for a reason section 8 covers. | 111-114; 1203-1207 | — | `pc-travel-tests.l4`: refund 0; LAW-FRAUD, LAW-TERM |
| F-7-ORIGIN | Travel Delay covers only a delay "outside the Insured's Country of Origin", so the outbound flight delayed at the home airport (before clause 13's cover begins) is never covered. | 637-639; 1741-1743 | — | reading only |
| F-COMPANY | The insurer is Hung Vuong Insurance Corporation; Pacific Cross Vietnam, which publishes the document, is not a party the wording names. | 884, 2210-2217 | — | reading only |

Checked and found sound: the age limits (75, then no benefit from 76) agree once tested at different dates (F-AGE); the Short Period Rate closes at 100% (F-SPR); the Personal Accident percentages never exceed 100% of the sum insured; the child cap (400,000,000) and the Common Carrier doubling (not for children) agree; clause 10 and 1B.3 use the same VND 50,000,000 threshold.

## 5. Answer table

From the raw text by `gen_tables.py` (enc-vn-06's scratch script); each English figure was parsed and compared with the Vietnamese figure for the same plan, and all agree (0 mismatches).
VND.

| benefit (clause) | Plan A, Premier | Plan B, Executive | Plan C | EN src | VI src |
| --- | --- | --- | --- | --- | --- |
| 1B.5 additional travel and accommodation | 100,000,000 | 70,000,000 | 40,000,000 | 384-387 | 1479-1482 |
| 1B.6 family member visit | 100,000,000 | 70,000,000 | 40,000,000 | 389-391 | 1484-1487 |
| 1B.7 return of children | 100,000,000 | 70,000,000 | 40,000,000 | 400-403 | 1498-1500 |
| 1B.8 repatriation of mortal remains | 60,000,000 | 40,000,000 | 20,000,000 | 408-411 | 1505-1507 |
| 5.3 travel documents, a day | 4,000,000 | 3,000,000 | 2,000,000 | 608-611 | 1712-1714 |
| 7(a) travel delay (500,000 per full 6 hours), at most | 3,500,000 | 2,500,000 | 1,500,000 | 645-648 | 1748-1752 |
| 7(b) re-routing | 16,000,000 | 10,000,000 | 6,000,000 | 649, 651-652 | 1753-1755 |
| 8 curtailment or cancellation | 130,000,000 | 90,000,000 | 70,000,000 | 687-689 | 1792-1794 |
| 9 personal liability | 2,000,000,000 | 1,300,000,000 | 700,000,000 | 731-734 | 1848-1851 |
| 11 rental car excess | 10,000,000 | 6,000,000 | 4,000,000 | 799-801 | 1914-1916 |
| 3.3 laptop (excluded by 3.6(c), F-LAPTOP) | 20,000,000 Premier; 10,000,000 Plan A | 10,000,000 | 10,000,000 | 507-509 | 1606-1608 |

Figures printed once, for every plan:

| figure | value | EN src | VI src |
| --- | --- | --- | --- |
| direct billing threshold (clause 10); hospital guarantee threshold (1B.3) | above 50,000,000 | 126, 354 | 1221, 1450 |
| room and board a day; all-in day without breakdown (1A.1(a)) | 6,000,000; 20,000,000 | 266, 269 | 1366, 1370 |
| follow-up after return, within 90 days (1A.1(b)) | 130,000,000 | 271 | 1374 |
| hospital cash, a day (1B.4) | 1,000,000 | 355, 360 | 1451 |
| emergency evacuation; repatriation (1B.1, 1B.2) | unlimited | 333, 341 | 1428, 1436 |
| a child's Personal Accident sum insured (2.4) | at most 400,000,000 | 455 | 1551 |
| Personal Accident table (2.3) | 100% five rows; 50% loss of use of one limb | 442-452 | 1537-1548 |
| baggage: an item; a pair or set (3.3) | 5,000,000; 10,000,000 | 506-507 | 1605-1606 |
| baggage delay, an article (4.1) | 1,300,000 | 568 | 1672 |
| rental car protection, most; deductible (12) | 500,000,000; first 5,000,000 | 831, 863 | 1954, 1985 |
| Short Period Rate | 20% under one month; +10% each further month begun; 100% after eight months | 989-994 | 2119-2123 |

Worked scenarios the tests assert (English text; Plan A unless said; the Certificate's limits as in `pc-travel-tests-fixtures.l4`):

| facts | payable |
| --- | --- |
| hospitalisation 10,000,000, room and board 8,000,000, consultation 2,000,000 (1A) | 18,000,000 |
| room and board 8,000,000 (→ 6,000,000), surgery 12,000,000 at a customary 10,000,000, follow-up 140,000,000 (→ 130,000,000), Certificate limit 120,000,000 (1A, every layer) | 120,000,000 |
| 72 hours in hospital (1B.4) | 3,000,000 |
| economy fare 30,000,000 and accommodation 50,000,000 + 40,000,000 (1B.5) | 100,000,000 (Plan C 40,000,000) |
| accidental death, sum insured 1,000,000,000 (2); Bon Voyage on a bus | 1,000,000,000; 2,000,000,000 |
| a child's accidental death, sum insured 1,000,000,000 (2.4) | 400,000,000 |
| camera body 8,000,000 + lens 6,000,000 + jacket 7,000,000 (3) | 15,000,000 |
| passport: replacement 3,000,000, days 5,000,000 and 2,000,000, fare 10,000,000 at economy 8,000,000 (5) | 17,000,000 (Plan C 15,000,000) |
| a 13-hour delay; a 48-hour delay (7(a)) | 1,000,000; 3,500,000 (Plan C 1,500,000) |
| father dies, trip cut short: 20,000,000 prepaid, half unused, 15,000,000 extra (8) | 25,000,000 |
| injury liability 300,000,000 + 50,000,000 + 20,000,000 (9); Plan C, 900,000,000 damages | 370,000,000; 700,000,000 |
| rental car collision 50,000,000; 600,000,000 (12) | 45,000,000; 500,000,000 |
| Annual Travel, the Company cancels on 15 March (73 of 365 days), premium 2,000,000 (AT 3) | 1,600,000 |
| Annual Travel, the Policyholder cancels on 14 February (second month, 30%) | 1,400,000 |

## 6. What `check.sh` prints

See §0 for the table.
No module is expected to fail, so `check.sh`'s `expected_failed` table is unchanged (`check.sh` was not edited), and `encoding.json` has no `expected_red`.

One test-authoring error was caught by the harness during the session and is recorded here: the first assertion of the section 10 tests used the 20-day base case, which section 10 proviso 2 ("The Period of Insurance is not less than 31 days") rules out, and it failed.
The expected value (TRUE, a permitted return) was right for the facts intended; the scenario was wrong.
The fix was to give those tests a 31-day Certificate (`the 31-day case`), and the near misses with it, so each fails for its own reason; no expected value was changed.

The regulative rules are exercised with `#TRACE`, whose results are printed but are not assertions (check.sh does not count them).
Results, from the runs of 2026-10-06:

| trace | events | result |
| --- | --- | --- |
| `AT 1 — the duty to notify an alteration` | notice on day 30 | FULFILLED |
| same | none by day 31 | `BREACH BY the Policyholder BECAUSE "AT 1: no written notice of the alteration within 30 days from the date of alteration"` |
| `AT 4 — renewal` | none by day 400 | the permission stands: `PARTY the Company MAY renew the Policy` (no deadline is stated) |
| `CP 1 — the duty to give notice of a claim` | notice on day 30 | FULFILLED |
| same | none by day 31 | `BREACH BY the Insured Person BECAUSE "CP 1: notice of the claim was not given within 30 days …; clause 1 makes compliance a condition precedent to liability"` |
| `CP 1 — the duty to give written notice of a possible Personal Liability claim` | none by day 16 | `BREACH BY the Insured Person` |
| `CP 1 — the duty to provide the further information requested` | information on day 60 | FULFILLED |
| `1B.9 — referral services on request, reading the English` | none | FULFILLED (a permission unused) |
| `1B.9 — referral services on request, reading the Vietnamese` | none | `BREACH BY the Company BECAUSE "1B.9 (Vietnamese): the designated assistance company did not provide the referral services requested"` |
| same | provided at 1 | FULFILLED |


## 7. `vnsrc check`

Run from DEPOSIT, the brief's command, verbatim:

```
python3 -I tools/vnsrc.py check ../../source/raw/pacificcross-travel.txt *.l4 *.md
```

The gate (the same command over every `.l4` and `.md` in the deposit except `BRIEF.md`, as the lead ruled on 2026-10-07):

```
vnsrc check: 2478 src: lines, 640 Vietnamese runs, 0 problems
```

The brief's command as written, which also reads `BRIEF.md`:

```
vnsrc check: 2478 src: lines, 649 Vietnamese runs, 4 problems
```

Its four problems are all in `BRIEF.md` (lines 55-56): the brief's three Vietnamese search words, which occur nowhere in the source (§1), and the brief's tag, written without spaces. `BRIEF.md` was not edited.

## 8. Open questions for a domain expert

1. Which text does Pacific Cross, or a Vietnamese court or arbitrator, treat as governing where the two differ? Does Law Art. 24 (unclear terms read for the buyer) reach a difference between language versions (LAW-CONTRA)?
2. Does "cha mẹ ruột" exclude adoptive parents in practice, and does "anh chị em ruột" include half-siblings (VN-F6)?
3. Section 10: is cover suspended during a home visit (the Vietnamese) or ended (the English)? Is a planned visit home within section 10 (VN-F17)?
4. Is a laptop paid under 3.3 despite 3.6(c) (F-LAPTOP)?
5. How is an unitemised hospital day paid, given the proviso's breakdown requirement (F-MED-BREAKDOWN)?
6. Under Annual Travel, does any cancellation claim ever succeed, given AT 5 and section 8 proviso 4 (F-S8-ANNUAL)?
7. Does clause 14's 180-day maximum apply to Annual Travel policies (F-C14)?
8. Is a Personal Liability claim ever paid on a judgement given abroad (F-PL-FORUM)?
9. Does the Company accept notice of a Personal Accident claim after CP 1's 30 days when the death or disablement comes later (F-PA-NOTICE)? Does Law Art. 30's one year apply (LAW-CLAIM)?
10. What are "Excluded Conditions" (1B.4(c)), a "recognized" airline or rental company, and a "registered medical practitioner"?
11. How is a Close Business Partner's "Serious Injury or Illness" judged (F-CBP)?
12. Do the clause 9 subrogation and the AT 3 cancellation-at-will survive Law Arts. 16(4), 38 and 26 (LAW-SUBRO, LAW-TERM)?
13. The document is marked "Vs. 022014" in both halves while its file name says 042023: is this the wording in force for policies sold in 2026?
14. The `src:` lines quote 964 of the English lines and 1,005 of the Vietnamese: nearly the whole document. The subject-level `SOURCE-LICENSE.md` says the encodings "do not reproduce the document wholesale". This followed from the brief (the whole document, both texts cited on every operative clause); whether to thin the quotations is the lead's call (see `SOURCE-LICENSE.md` here).
