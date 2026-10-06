# GLOSSARY — Vietnamese source, English encoding

One row for every term the document defines (1.1 to 1.33) and for every type, field or constant of the L4 that renders a Vietnamese concept.
The Vietnamese column is copied from `../../source/raw/aia-an-phuc.txt` and checked by `tools/vnsrc.py`.
`src` is the line of that file.
Identifiers are those of the modules `aptduv-*.l4`.

## The defined terms (Article 1)

| Vietnamese term (verbatim) | English identifier in the L4 | English meaning, one line | where defined or used (Điều / clause, src line) | translation risk |
| --- | --- | --- | --- | --- |
| Công ty | `the Company` (a constructor of `A party`) | AIA Vietnam Life Insurance Co. Ltd, the insurer | 1.1, src 233 | low; the document also says "chúng tôi" (we) in 7.5, 27.1 and 29 without defining it |
| Bên mua bảo hiểm | `the policyholder`; `A policyholder` | the person or organisation that applies, signs and pays | 1.2, src 236-238 | "bên mua" is literally "buying party"; "policyholder" is the usual English, but the Vietnamese can mean the contracting party who is not the insured |
| Người được bảo hiểm | `the insured`; `An insured person` | the life insured | 1.3, src 240-242 | low |
| Người thụ hưởng | `a beneficiary`; `A beneficiary` | the person named to receive the death benefit | 1.4, src 244, 250 | low |
| Giấy chứng nhận bảo hiểm | (input source; no identifier) | the certificate, part of the contract | 1.5, src 256-263 | "certificate" in English can suggest a mere evidence document; here it is part of the contract (Article 3) |
| Ngày có hiệu lực của hợp đồng | `effective date`; `1.6 — the effective date for` | the day the application is complete and the first basic premium paid, if accepted | 1.6, src 267-271 | "hiệu lực" is both "effect" and "validity"; 16.1 and 16.2 write "Ngày hiệu lực hợp đồng" without "có ... của", read as the same date |
| Ngày kỷ niệm hợp đồng | `1.7 — contract anniversary number` | the yearly recurrence of the effective date | 1.7, src 275 | "kỷ niệm" is "commemoration"; "anniversary" is the right term of art |
| Ngày kỷ niệm tháng | `1.8 — monthiversary number` | the monthly recurrence of the effective date, falling to the month's last day | 1.8, src 280-281 | "monthiversary" is a coinage; "monthly anniversary" is the plain rendering |
| Ngày đáo hạn | `1.9 — the maturity date of` | the anniversary after the insured reaches 100 | 1.9, src 287-288 | "đáo hạn" is maturity; which anniversary is a fork (F1, FD1) |
| Ngày đến hạn đóng phí | `due date of a basic premium not paid in full, in the first four contract years` (field) | the day a basic premium instalment is due | 1.10, src 295-297 | low |
| Năm hợp đồng | `1.11 — the contract year in which` | a year from the effective date or an anniversary | 1.11, src 304-305 | "policy year" is the usual English; "contract year" keeps the Vietnamese "hợp đồng" |
| Năm đóng phí | `premium year of the basic premiums paid` (field) | a 12-month period whose basic premium has been paid in full | 1.12, src 307-308 | the definition ties a premium year to payment in full, so a premium year and a contract year can drift apart; the allocation and charge tables key on it (fork F28) |
| Số tiền bảo hiểm | `current sum insured` (field), `new sum insured` | the sum insured, a multiple of the annual basic premium | 1.13, src 310-312 | "số tiền bảo hiểm" is literally "insurance amount"; "sum insured" (not "sum assured") is used throughout |
| Số tiền bảo hiểm hiện tại | `current sum insured` | the sum insured at a moment in the current contract year | 1.14, src 318-319 | the encoding uses one field for 1.13 and 1.14, the current figure being the one every benefit uses |
| Phí bảo hiểm cơ bản | `basic premium due`, `annualised basic premium of the first contract year` | the regular premium the policyholder chooses | 1.15, src 328, 339-340 | "basic" for "cơ bản" can be confused with the "basic benefit" option ("Quyền lợi bảo hiểm cơ bản"); they are unrelated |
| Phí tích lũy | `counted as accumulation premium`; `1.16 — the most accumulation premium the contract may take in one contract year` | the top-up premium, capped at five times the first year's annualised basic premium | 1.16, src 350-365 | "tích lũy" is "accumulate"; "top-up" would be the market term but loses the link to the accumulation account |
| Phí dự tính | `1.17 — the planned premium of` | basic premium plus accumulation premium | 1.17, src 367 | "dự tính" is "estimated" or "planned"; "planned premium" is the universal-life term of art |
| Chi phí ban đầu | `17 — the initial charge on the basic premium in premium year` | the charge deducted from each premium before allocation | 1.18, src 369-370; Art. 17 | "initial" suggests a one-off; it recurs every year at 1.5% from year 5 |
| Chi phí bảo hiểm rủi ro | `cost of insurance for the month` | the monthly risk charge, by age and sex | 1.19, src 372-373; Art. 18 | "chi phí bảo hiểm rủi ro" is literally "risk insurance charge"; "cost of insurance" is the universal-life term |
| Chi phí quản lý hợp đồng | `contract administration charge for the month`; `19 — the contract administration charge as printed` | 30,000 dong a month, at most 60,000 | 1.20, src 379-385; Art. 19 | "policy fee" is the market term |
| Khoản khấu trừ hàng tháng | `1.21 — the monthly deduction of` | cost of insurance plus administration charge | 1.21, src 391-398 | low |
| Chi phí quản lý quỹ | `20 — the maximum fund management charge as printed` | the fund charge, at most 2% a year | 1.22, src 401-402; Art. 20 | low |
| Giá trị tài khoản cơ bản | `basic account value` | the account built from basic premiums | 1.23, src 407-408 | "basic" again collides with the "basic benefit" option |
| Giá trị tài khoản tích lũy | `accumulation account value` | the account built from accumulation premiums | 1.24, src 414-415 | low |
| Giá trị tài khoản | `1.25 — the account value of` | the sum of the two accounts | 1.25, src 422 | "account value" is the universal-life term; not a surrender value, though 25.1 pays it as one |
| Lãi suất tích lũy | `7.6 — the rate credited, on a declared rate of`; `32 — the accumulation interest rate, from a yield of` | the rate credited to the account value, net of the fund charge, never below the minimum | 1.26, src 428-435; Art. 32 | "accumulation interest rate" is literal; "crediting rate" is the market term. The document never says whether it is a yearly or a monthly rate (fork F18) |
| Quỹ liên kết chung | (Chapter 8; no identifier) | the universal-life fund | 1.27, src 437-438 | "liên kết chung" is "universal link" (universal life); not a unit-linked fund |
| Khoản nợ | `outstanding debts` | premiums and charges due and unpaid, and other sums owed | 1.28, src 440-441 | "nợ" is plain "debt"; the term is wider than a policy loan, which this product does not have |
| Tàn tật toàn bộ và vĩnh viễn | `1.29 — the disability is total and permanent`; `A disability` | the listed losses, or a certified rate of 81% or more | 1.29, src 443-463 | "tàn tật" is "disability" in the medical sense; "mất sức lao động" in (b) is "loss of working capacity", a different, occupational measure, rendered separately |
| Ung thư | `1.30 — the illness is a Cancer`; `A cancer` | a histologically confirmed invasive malignant tumour, less five exclusions | 1.30, src 465-537 | "phát sinh" (arise) is defined by first symptoms, which English "onset" or "diagnosis" would not convey (finding FD7) |
| Tai nạn | `1.31 — the death was caused by an Accident`; `An accident` | a sudden, external, unintended event that is the sole cause of death within 180 days | 1.31, src 539-544 | 5.1 writes "tai nạn" in lower case; read as the defined term (fork F33) |
| Tuổi bảo hiểm | `1.32 — the insurance age on` | age last birthday on the effective date or the last anniversary | 1.32, src 546-548 | "insurance age" is literal; "age next birthday" or plain "age" in English would give other numbers. The clause makes every "tuổi" in the document mean this, including the policyholder's (finding FD2) |
| Hành vi gian lận bảo hiểm | `an act of insurance fraud` (field) | forging documents, falsifying claim information, or self-harm of the insured to claim, as the Criminal Code defines | 1.33, src 558-567 | "gian lận" is "fraud" in the criminal sense; the definition sends the reader to the Criminal Code, not encoded |

## Types, fields and constants

| Vietnamese term (verbatim) | English identifier in the L4 | English meaning, one line | where defined or used (Điều / clause, src line) | translation risk |
| --- | --- | --- | --- | --- |
| Quyền lợi bảo hiểm cơ bản | `the basic benefit` (`A benefit option`) | death or disability pays the greater of sum insured and account value | 7.2.1, src 894 | "basic" collides with "basic premium" and "basic account" |
| Quyền lợi bảo hiểm nâng cao | `the enhanced benefit` | death or disability pays sum insured plus account value | 7.2.1, src 907 | "nâng cao" is "raised" or "advanced"; "enhanced" is a choice |
| hàng năm, hàng nửa năm, hàng quý | `annual`, `semi-annual`, `quarterly`, `monthly` (`A premium mode`) | the premium modes | 14.2, src 1455-1456 | low |
| hoặc tổ chức | `an organisation` (field of `A policyholder`) | the policyholder is a body, not an individual | 1.2, src 237 | "tổ chức" is any organisation, not only a company |
| năng lực hành vi dân sự | `full civil act capacity` | legal capacity to act under the Civil Code | 1.2, src 236 | "civil act capacity" is the literal civil-law term; English "legal capacity" is wider |
| hiện đang sinh sống tại Việt Nam | `living in Vietnam when the application was submitted` | residence condition of the insured | 1.3, src 240 | "sinh sống" is "living", not legal "residence"; 22.3 uses "cư trú" (reside), a different word |
| quyền lợi có thể được bảo hiểm | `2.2 — the policyholder has an insurable interest in the insured, who is` | insurable interest | 2.2, src 577-579 | "insurable interest" is the term of art |
| Cha mẹ ruột, vợ hoặc chồng hợp pháp, con ruột hoặc con nuôi hợp pháp | `a natural parent, lawful spouse, or natural or lawfully adopted child` | the close-family bullet | 2.2, src 592 | "ruột" (of the same blood) is rendered "natural" |
| Anh chị em ruột | `a natural sibling` | full siblings | 2.2, src 598 | "ruột" may exclude half-siblings; the encoding does not decide |
| Cháu ruột nếu Bên mua bảo hiểm là ông nội, bà nội, ông ngoại, bà ngoại | `a natural grandchild, the policyholder being a grandparent` | grandchildren of a grandparent policyholder | 2.2, src 602 | "cháu" is grandchild or nephew/niece; the condition fixes grandchild |
| Người có quan hệ nuôi dưỡng, cấp dưỡng | `a person in a relationship of nurture or support` | dependency relationship | 2.2, src 603 | "nuôi dưỡng" (raising) and "cấp dưỡng" (maintenance) are distinct legal relations, merged in one constructor as the bullet merges them |
| Người giám hộ hợp pháp | `a lawful guardian` | a guardian | 2.2, src 605 | does not say whose guardian: the policyholder's, or one the policyholder is guardian of |
| Người khác | `another person` | anyone else the Law allows | 2.2, src 606-607 | declined by name: needs the Law on Insurance Business |
| bảo hiểm tạm thời | `A death during temporary insurance`; `5.1 — the temporary insurance benefit` | cover while the application is pending | Art. 5, src 655-679 | low |
| 100.000.000 đồng | `5.1 — the temporary insurance amount` (100_000_000) | one hundred million dong | 5.1, src 656 | the dots group thousands; read as a decimal point it would be 100 dong |
| cố ý cung cấp thông tin không trung thực hoặc không đầy đủ | `A misstatement`, `intentional` | intentional misstatement | 6.2, src 709-710 | "cố ý" is "intentional", stronger than "knowing" |
| Miễn truy xét | `6.3 — the information behind` … `may still be contested on` | incontestability | 6.3, src 754 | "truy xét" is "investigate" or "pursue"; "incontestable" is the English term of art, slightly narrower |
| Khấu trừ | `6.4 — the amount paid on a benefit of` | set-off of debts against benefits | 6.4, src 769 | "khấu trừ" is used for both "deduct" (charges) and "set off" (6.4) |
| không hút thuốc lá | `determined to be a non-smoker` | the non-smoker condition of 7.3 | 7.3, src 964 | "thuốc lá" is tobacco; e-cigarettes are not addressed |
| Thưởng duy trì hợp đồng | `7.7 — the loyalty bonus under` | the persistency bonus | 7.7, src 1034 | "duy trì" is "maintain"; "loyalty" or "persistency" bonus |
| Tổng Số tiền tính Thưởng | `7.7 — the total bonus base under` | the base the bonus is a percentage of | 7.7, src 1076 | low |
| Số tiền tính Thưởng | `7.7 — the bonus base recorded under` | the base recorded on each of anniversaries 6 to 10 | 7.7, src 1095 | low |
| chiến tranh | `war` (field) | war, 8.1 | 8.1, src 1146 | 8.2 lists "xung đột vũ trang" (armed conflict) separately; 8.1 has war only |
| rượu bia quá nồng độ | `alcohol above the legal limit, or the effect of medication not prescribed` | alcohol above the legal concentration | 8.2, src 1207 | "rượu bia" is "spirits and beer"; the limit is set by other law |
| hoạt động giải trí nguy hiểm | `another recreational activity said to be dangerous` and the named activities | dangerous recreation, listed after "như" | 8.2, src 1217 | "như" (such as) makes the list open |
| hạn mức tối thiểu do Công ty quy định tại từng thời điểm | `minimum set by the Company at the time` | the Company's minimum withdrawal | 9.1, src 1254 | low |
| số tiền bảo hiểm tối đa do Công ty quy định | `maximum set by the Company at the time` | the Company's maximum sum insured | 10.1, src 1286 | low |
| kết hôn hoặc sinh con | `date of the marriage or the birth` | the 11.1 events | 11.1, src 1322 | "sinh con" is "give birth" or "have a child"; read as either parent's event |
| điều kiện chuẩn | `accepted on standard terms at issue or at the last reinstatement` | standard underwriting terms | 11.1, src 1325 | undefined in the document (finding FD17) |
| sản phẩm bảo hiểm bổ sung | `A request to add a supplementary product`; `rider premiums due` | riders | Art. 13, 14.5 | "supplementary product" is literal; "rider" is the market word |
| thời gian gia hạn đóng phí | `15.1 — the last day of the grace period, by` | the 60-day grace period | 15.1, src 1661 | "gia hạn" is "extension"; "grace period" is the term of art |
| Mất hiệu lực | `15.3 — the first day the contract is lapsed, by` | lapse | 15.3, src 1678 | "mất hiệu lực" is "lose effect"; "lapse" is the term of art, not "termination" (25.2(d) ends a lapsed contract after 24 months) |
| Tỷ lệ phân bổ | `14.5.3 — the allocation rate of the basic premium in premium year` | allocation rate | 14.5.3, src 1594 | low |
| 98,5% | `98.5%` in the allocation table | ninety-eight and a half per cent | 14.5.3, src 1608 | the comma is a decimal point |
| 1,5% | `1.5%` in the initial-charge table | one and a half per cent | Art. 17, src 1803 | the comma is a decimal point |
| 30.000 (ba mươi ngàn) đồng/tháng | `19 — the contract administration charge as printed` (30_000) | thirty thousand dong a month | Art. 19, src 1846 | the dot groups thousands |
| Bộ Tài chính | `approved by the Ministry of Finance` (parameter) | the Ministry of Finance | Art. 18-20, src 1824 | low |
| Từ chối tham gia bảo hiểm | `21 — the refusal is in time`; `21 — the free-look right` | the free look | Art. 21, src 1887 | "từ chối" is "refuse"; Article 35 of the Law on Insurance Business frames the same right as a cooling-off period (aid, line 760) |
| Chuyển nhượng hợp đồng bảo hiểm | `22.4 — the assignment takes effect, at` | assignment | 22.4, src 1966 | "chuyển nhượng" is "transfer for value"; the Law uses "chuyển giao" |
| nhầm lẫn khi kê khai tuổi và/hoặc giới tính | `A misstatement of age or sex` | misstated age or sex | Art. 23, src 2004 | "giới tính" is "sex" or "gender"; "sex" is used for the actuarial factor |
| Khôi phục hiệu lực hợp đồng | `24 — the policyholder may ask to reinstate, by` | reinstatement | Art. 24, src 2053 | low |
| thời gian đóng phí bắt buộc | `all overdue basic premiums of the compulsory payment period paid` | the compulsory payment period | 24(i), src 2087 | undefined in the document (finding FD17); read as the first four contract years |
| Chấm dứt Hợp đồng bảo hiểm | `An event that ends the contract`; `25.1 — the amount paid on surrender, at` | termination and surrender | Art. 25, src 2104 | the document has no word for "surrender value"; 25.1 pays the account value less debts |
| người thừa kế hợp pháp | `the policyholder's lawful heirs` (`A payee`) | the policyholder's lawful heirs | 26.2, src 2180; 22.1, src 1923 | "thừa kế" is inheritance; 22.1 applies it to an organisation (finding FD20) |
| Phiếu Yêu cầu giải quyết quyền lợi bảo hiểm | `claim form completed fully and accurately` | the claim form | 27.1, src 2208 | low |
| Trích lục chứng tử | `extract of the death record` | the civil-status extract of the death | 27.1, src 2214 | "trích lục" is an official extract, not a certificate |
| Hội Đồng Giám Định Y Khoa cấp tỉnh, thành phố trực thuộc trung ương | `a provincial or centrally-run city medical assessment council` | the official disability-rating council | 1.29(b), src 460-461; 27.1, src 2215-2221 | "giám định y khoa" is "medical assessment", not "medical examination" |
| tổ chức y tế độc lập được Công ty chấp thuận | `an independent medical organisation approved by the Company` | the alternative certifier of 1.29(b) | 1.29(b), src 461-462 | 27.1 names a different body (finding FD28) |
| tổ chức y tế hợp pháp ở nước ngoài | `a lawful foreign medical organisation approved by the Company` | the certifier 27.1 names | 27.1, src 2221-2222 | not accepted by 1.29(b) |
| Thời hạn yêu cầu giải quyết quyền lợi bảo hiểm | `28 — the last day to claim` | the claim time-bar | Art. 28, src 2279-2280 | "thời hạn" is both "deadline" and "period" |
| khoản tạm ứng từ giá trị hợp đồng | (reason string of `29 — the interest on`) | advances against the contract value | Art. 29, src 2308 | refers to a facility this product does not offer (finding FD16) |
| Lãi suất cam kết tối thiểu | `32 — the minimum guaranteed interest rate in contract year` | the minimum guaranteed rate | Art. 32, src 2355 | "cam kết" is "committed"; "guaranteed" is the term of art |
| trái phiếu chính phủ, trái phiếu đô thị, trái phiếu doanh nghiệp | `government bonds`, `municipal bonds`, `corporate bonds`, `bank deposits` (`An investment asset`) | the asset classes of Art. 31 | Art. 31, src 2351-2352 | "đô thị" is "urban"; "municipal bonds" is the closest English |
| Thời hiệu khởi kiện | `33 — the last day to bring an action on a dispute that arose on` | limitation period for suit | Art. 33, src 2430 | "thời hiệu" is the civil-law limitation period |
| Bên mua được bảo hiểm | (parameter `where the policyholder or the insured resides`) | an undefined fusion of "Bên mua bảo hiểm" and "Người được bảo hiểm" | Art. 33, src 2429 | undefined (finding FD17); read as reaching either |
