# GLOSSARY — VN-13, Manulife regular-premium unit-linked contract terms

Every Vietnamese term below is copied from `../../source/raw/manulife-maxx.txt` and is checked verbatim by `tools/vnsrc.py check`.
"src" is a line of that file.
The first block is every term Article 1 defines, in the order it defines them; the second, every other type, field or constant in the L4 that renders a Vietnamese concept.
Identifiers are given as they appear in the modules (backticks dropped).

## Terms Article 1 defines

| Vietnamese term (verbatim) | English identifier in the L4 | English meaning, one line | where defined or used (Điều / clause, src line) | translation risk |
| --- | --- | --- | --- | --- |
| Công ty | the Company (`A party`) | Manulife (Vietnam) Ltd, the insurer | Điều 1, src 15-17 | none |
| Bên mua bảo hiểm | the Policyholder | the person named as policyholder in the Policy Schedule | Điều 1, src 18-21 | "buyer of insurance" is literal; "Policyholder" adds the common-law sense of owner of the policy, which the text supports (it holds every right) |
| Người được bảo hiểm | The Life Insured | the person whose life and health the contract covers; here the Policyholder | Điều 1, src 22-27 | "the insured" in English can mean the policyholder; "Life Insured" keeps the two roles apart, though the text makes them one person |
| Tuổi | the Age of a person born on … on … | age at the last birthday | Điều 1, src 28-29 | none; capitalised in the source as a defined term, as here |
| Giá trị hoàn lại | the surrender value on | the funds' account value less the premium debt, at any time | Điều 1, src 30-32; Điều 3, 6, 7, 8, 9.4, 12, 20 | literally "value returned"; "surrender value" is the trade term, but here it is defined net of debt, which the English term usually is not |
| Giá trị tài khoản | the account value of; the total account value of | units held times the bid price on the Valuation Date, per fund | Điều 1, src 33-35 | "account value" can mean the whole policy account; here it is per fund and summed by the rule |
| Nợ phí | premium debt (field of `A valuation of the account`); the premium debt of … with interest of | unpaid premiums plus interest if any | Điều 1, src 36-37; Điều 3.1 v, 3.2 ii | "premium debt" may suggest a loan; it is arrears. Distinct from "Nợ vay" (below) |
| Ngày hiệu lực Hợp đồng | effective date | the day the contract begins to be in force, as the Schedule records | Điều 1, src 38-41 | "effective date" also names a transaction's date ("Ngày giao dịch có hiệu lực"); kept apart by name |
| Tháng kỷ niệm Hợp đồng | the monthly anniversary number … | the monthly anniversary of the Effective Date | Điều 1, src 42-43; Điều 13.6 | "kỷ niệm" is "commemoration"; "monthiversary" would be closer but is not standard English |
| Năm kỷ niệm Hợp đồng | the policy anniversary number … | the yearly anniversary of the Effective Date | Điều 1, src 44-45; Điều 3.3 | the source defines it as a POINT in time ("thời điểm"), yet 3.3 speaks of "the end of" one: fork |
| Năm Hợp đồng | the policy year in which … falls | one year from the Effective Date, then from each anniversary | Điều 1, src 48-49 | "contract year" equally good; "policy year" chosen |
| Ngày chấm dứt Hợp đồng | expiry date | the end date in the Schedule or an endorsement | Điều 1, src 50-52 | "termination date" would collide with Điều 20 termination; "expiry" is used for the scheduled end |
| Ngày cấp Hợp đồng | issue date | the day the contract is issued, per the Schedule | Điều 1, src 53-55; Điều 7, 8 | none |
| Ngày đã được trả phí | paid-to date | defined as "the last point premium was paid"; used in Annex 2 F as if a paid-to date | Điều 1, src 56-57; Phụ lục 2 F | HIGH: the definition reads as the date of the last payment; the English trade term "paid-to date" is the date premiums cover up to. The two differ; fork |
| Ngày yêu cầu giải quyết quyền lợi bảo hiểm | date the Company received the complete and valid claim | the day the Company receives the claim complete and valid | Điều 1, src 58-61; Điều 3.1 ii, 18 | "claim date" is shorter but loses "complete and valid", which governs when the date occurs |
| Ngày nhận yêu cầu giao dịch | Annex 2 A — the transaction receipt date of | the day a valid, complete written fund-transaction request is received | Điều 1, src 62-66; Phụ lục 2 A | none |
| Ngày giao dịch có hiệu lực | the effective date / the transaction effective (arguments) | the day a premium takes effect, or a fund request is received | Điều 1, src 67-70; Điều 9.1, 9.2, 11.5 | collides in English with the contract's effective date; context separates them |
| Ngày định giá | valuation date | a day the Company prices the units | Điều 1, src 71-73; Điều 11.2 | none |
| Ngày định giá kế tiếp | the valuation on the next Valuation Date after | the Valuation Date immediately after a transaction's effective date | Điều 1, src 74-75 | "ngay sau" (immediately after) read as strictly after; fork |
| Quỹ liên kết đơn vị | A unit-linked fund | a fund formed from premiums, part of the Company's policyholder fund | Điều 1, src 76-80; Điều 11 | "unit-linked fund" is standard; the source's "quỹ chủ hợp đồng" (policyholders' fund) is not rendered |
| Đơn vị quỹ | units held, units in issue | an equal share of a fund's assets | Điều 1, src 81-82 | none |
| Giá mua của đơn vị quỹ (Giá mua) | bid price | the price at which the Company BUYS a unit from the Policyholder | Điều 1, src 83-84; Điều 11.2 | HIGH: "giá mua" is literally "buying price"; seen from the Policyholder it is the selling price. "Bid" is the Company's side, as the source defines it |
| Giá bán của đơn vị quỹ (Giá bán) | the offer price for a bid price of … | the price at which the Company SELLS a unit to the Policyholder | Điều 1, src 85, 91; Điều 11.2 | HIGH, as above: literally "selling price"; it is the higher price, the one premiums buy at |
| Phí bảo hiểm cơ bản định kỳ | regular basic premium | the main contract's periodic premium in the Schedule | Điều 1, src 92-94; Điều 9.1 | "basic" may suggest a minimum; it is the base contract's premium as against riders |
| Tổng phí bảo hiểm định kỳ | the total regular premium in | basic premium plus rider premiums | Điều 1, src 95-96 | none |
| Phí bảo hiểm đóng thêm | A top-up premium | an extra premium paid on top of the basic premium | Điều 1, src 97-98; Điều 9.2; Phụ lục 2 B | literally "premium paid in addition"; "top-up" is the market term |
| Phí bảo hiểm cơ bản được phân bổ | the allocated basic premium of | the basic premium less the initial charge | Điều 1, src 99-100 | none |
| Phí bảo hiểm đóng thêm được phân bổ | the allocated top-up premium of | the top-up less the initial charge | Điều 1, src 101-102 | none |
| Thưởng duy trì hợp đồng | the loyalty bonus for | 360% of the basic premium annualised at issue, paid at the 15th anniversary | Điều 1, src 103-105; Điều 3.3 | literally "contract-maintenance reward"; "loyalty bonus" is the market term but may suggest discretion; the text makes it conditional, not discretionary |
| qui về năm | the annualised regular basic premium at issue, in | a premium converted to a yearly amount | Điều 1, src 104; Phụ lục 2 B src 966 | method of conversion not stated; read as instalment times instalments a year (fork) |
| Tỷ lệ phân bổ quỹ | fund allocation, An allocation to a fund, share | the split of premiums among funds | Điều 1, src 106-108; Điều 17.2 | none |

## Other terms the L4 renders

| Vietnamese term (verbatim) | English identifier in the L4 | English meaning, one line | where defined or used (Điều / clause, src line) | translation risk |
| --- | --- | --- | --- | --- |
| Trang hợp đồng | The Policy Schedule | the contract page recording the particulars | throughout, e.g. src 19, 140 | "Schedule" is the common-law term; the source's is "contract page" |
| Xác nhận thay đổi hợp đồng | (endorsement; no type) | written confirmation of an accepted change, or a Company notice changing the terms | Điều 2, src 116-119 | "endorsement" in English implies agreement; the source includes the Company's unilateral notices |
| Đơn yêu cầu bảo hiểm | (application; no type) | the application with medical forms and answers | Điều 2, src 113-115 | none |
| Tổng giám đốc; Phó Tổng giám đốc | signed by the General Director or a Deputy General Director | the officers who must sign a change | Điều 2, src 122-123 | "General Director" is the Vietnamese corporate office; not "CEO" |
| Số tiền bảo hiểm | sum assured | the amount assured in the Schedule | Điều 3.1 i, src 140; Điều 13.3 | "sum insured" in non-life usage; "sum assured" is the life term |
| Quyền lợi bảo hiểm tử vong | Article 3.1 — the death benefit on | the death benefit | Điều 3.1, src 132-154 | none |
| Phạm tội hoặc cố tình phạm tội hình sự | caused directly or indirectly by an offence of the Life Insured / of another person | committing, or intentionally committing, a criminal offence | Điều 3.2 (i), src 158 | HIGH: no subject in the Vietnamese; the English "of the Life Insured" supplies one. "Phạm tội" may reach any offence, not only a criminal one with intent |
| Hội chứng suy giảm miễn dịch mắc phải (AIDS) | related to AIDS, ARC or HIV infection | AIDS, AIDS-related conditions, HIV infection | Điều 3.2 (ii), src 159-162 | "liên quan" (related) is wide; the English "related to" keeps the width |
| trực tiếp hay gián tiếp | caused directly or indirectly | the causal link for the exclusions | Điều 3.2, src 156 | none |
| THỜI HẠN TỰ DO XEM XÉT | free-look period (Article 4 rules) | 21 days to cancel after receiving the policy | Điều 4, src 195-204; Phụ lục 2 F | literally "period of free consideration"; "free-look" is the market term (the Law, Article 35, uses another name) |
| chi phí y tế/kiểm tra sức khỏe | medical and health-check expenses | costs deducted from the free-look refund | Điều 4, src 204 | none |
| khai báo sai | A misstatement of age or sex; A non-disclosure or misstatement | a false declaration | Điều 6, 7 | "misstatement" carries no intent; nor does the Vietnamese |
| nhóm tuổi được bảo hiểm | puts the true Age outside the insurable ages | the insurable age range; undefined | Điều 6, src 215, 227-228 | undefined in the source; read as Article 1's 18 to 65 (fork) |
| MIỄN TRUY XÉT | Article 7 — the Company may no longer contest | incontestability | Điều 7, src 233-262 | literally "exemption from investigation"; "incontestability" is the common-law doctrine and fits |
| trục lợi bảo hiểm | insurance fraud | profiteering from insurance; insurance fraud | Điều 7, src 254 | "trục lợi" is "to profit improperly"; "fraud" may import intent and deceit that the Vietnamese does not require |
| phần bổ sung | in a supplementary part of the contract | any supplementary part of the contract; undefined | Điều 7, src 261-262 | undefined; could mean riders, endorsements or later applications |
| TỰ TỬ | suicide | suicide, sane or insane | Điều 8, src 264-275 | none |
| tạm ngưng đóng phí | premium holiday; ever on a premium holiday | a suspension of regular premiums | Điều 9.3, src 317-350; Phụ lục 2 C | "premium holiday" is the market term; the Vietnamese "suspension" is plainer |
| thời gian gia hạn | grace period | the 60 days of grace | Điều 9.4, src 351-381 | none |
| Mất hiệu lực | the contract lapses on; date of the latest lapse or termination | lapse | Điều 9.4, 9.5, 20 | "lose effect" in Vietnamese; English "lapse" fits; whether a year-2 automatic ending ("tự động chấm dứt") is a lapse is a fork |
| Khôi phục hiệu lực | A reinstatement request | reinstatement | Điều 9.5, src 382-397 | literally "restoration of effect" |
| đồng Việt Nam | Vietnamese dong (`A currency`) | the currency of every payment | Điều 10, src 400-401 | none |
| Giá trị tài sản thuần | net asset value | a fund's net assets | Điều 11.2, src 420-439 | "ròng" is used for the same idea in Phụ lục 1 ("giá trị tài sản ròng"); both rendered "net asset value" |
| chênh lệch giá mua và giá bán | bid-offer spread | the gap between the two unit prices | Điều 11.2, 13.7, 13.9 g | the formula sets the spread on the OFFER price (bid = offer × (1 − spread)), not on the bid |
| Thành lập hoặc đóng (các) Quỹ | a fund established later under Article 11.4; closing or renaming a fund under Article 11.4 | the Company's power to open, close or rename funds | Điều 11.4, src 467-487 | none |
| Rút từng phần | partial withdrawal | withdrawing part of a fund's account value | Điều 11.5; Phụ lục 2 D | none |
| Chuyển đổi Quỹ | fund switch | moving value between funds at the bid price | Điều 11.6; Phụ lục 2 E | none |
| Ngừng định giá | suspending valuation and transactions while the exchange is suspended | suspension of pricing | Điều 11.7 d, src 523-527 | none |
| HỦY HỢP ĐỒNG | Article 12 — the surrender payment … | surrender of the contract for its surrender value | Điều 12, src 548-554 | "hủy" is "cancel"; "surrender" is the life-insurance term; Điều 7 uses the same word "huỷ" for the Company's avoidance |
| Phí ban đầu | initial charge | the charge on premiums at allocation | Điều 13.1, 13.9 a | "initial" suggests a one-off; it runs three years |
| Phí quản lý hợp đồng | monthly policy fee | the monthly contract administration fee | Điều 13.2 | "policy fee" vs "administration charge": either |
| Phí bảo hiểm rủi ro | risk premium; risk premium rate | the cost of insurance, sum assured times rate | Điều 13.3 | HIGH for a reader from English markets: this is the "cost of insurance" charge, not a premium the Policyholder pays separately |
| Phí chuyển đổi quỹ | switching fee | the fee for a switch | Điều 13.4, 13.9 e | none |
| Phí rút tiền mặt từng phần | partial withdrawal fee | the fee on a partial withdrawal | Điều 13.5, 13.9 f | literally "partial cash withdrawal fee" |
| Khấu trừ hàng tháng | Article 13.6 — the monthly deduction on … | policy fee plus risk premium, taken monthly in units | Điều 13.6 | none |
| Phí quản lý Quỹ | fund management fee rate per year | the fund management fee, inside the unit price | Điều 13.8, 13.9 h | none |
| Mức phí tối đa đảm bảo | the guaranteed maximum …; A row of the Article 13.9(a) table | guaranteed maximum charges | Điều 13.9, src 615-681 | none |
| bảng tỷ lệ tử vong tiêu chuẩn | against a standard mortality rate of | the Company's standard mortality table for this product | Điều 13.9 d, src 668-669 | the table is the one the Company "is using", not a fixed published table |
| Hợp đồng đóng phí năm; Hợp đồng đóng phí nửa năm; Hợp đồng đóng phí quý; Hợp đồng đóng phí tháng | annual / half-yearly / quarterly / monthly premiums (`A premium frequency`) | premium frequencies | Điều 13.9 a, src 619-652 | none |
| Phí BHCBĐK lần | instalment number | the number of the regular basic premium instalment | Điều 13.9 a, src 620 | "lần" (time, occurrence) read as the instalment's ordinal from the first |
| trở lên | last instalment = NOTHING | "and above" in the table | Điều 13.9 a, src 628 | none |
| Người thụ hưởng | a Beneficiary | the person who takes the death benefit | Điều 16, src 693-711 | none |
| bất khả kháng hoặc trở ngại khách quan | days of force majeure or other objective obstacle | time not counted against the claim limit | Điều 18, src 755-757 | "trở ngại khách quan" is a Vietnamese civil-law notion wider than force majeure |
| Nợ vay | the amount … less unpaid loans of | unpaid loans; never defined, and the contract has no loans | Điều 18, src 762 | undefined; "loan" assumes a policy-loan facility the document does not contain |
| Thời hiệu khởi kiện | Article 19 — the last day to sue on a dispute that arose on | limitation period for suing | Điều 19, src 783-784 | none |
| Quỹ Tăng Trưởng; Quỹ Phát Triển; Quỹ Cân Bằng | the Growth Fund / the Development Fund / the Balanced Fund | the three funds | Phụ lục 1, src 813, 835-837 | "Phát Triển" (development) and "Tăng Trưởng" (growth) are near-synonyms in English; the Development Fund is the middle-risk fund, which neither name says |
| cổ phiếu | equity share | shares in companies operating in Vietnam | Phụ lục 1, src 850, 868, 893 | none |
| tổ chức tín dụng trong nước; tổ chức tín dụng ngoài nước | domestic / foreign credit institution | banks and similar lenders | Phụ lục 1, src 913-916 | none |
| nhóm công ty có quan hệ sở hữu với nhau | one group of related companies | companies linked by ownership | Phụ lục 1, src 918-919 | none |
| ngày làm việc | on a working day; next working day | a business day; undefined | Phụ lục 2 A, src 949-952 | undefined; the Company's calendar |
| mức tối thiểu; số tối thiểu; số dư tài khoản tối thiểu | minimum top-up, minimum withdrawal, minimum switch, minimum balance, minimum difference | minimums the document never states | Phụ lục 2 B, D, E, F | none in translation; the figures are missing from the document |
| thời gian thanh toán tối thiểu | (Annex 2 C refusal) | a minimum payment period; never stated | Phụ lục 2 C, src 985-986 | undefined |
