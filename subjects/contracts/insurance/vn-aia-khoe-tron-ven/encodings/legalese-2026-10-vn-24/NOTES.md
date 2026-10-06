# NOTES — vn-aia-khoe-tron-ven, encoding row `legalese-2026-10-vn-24`

AIA Vietnam's product rules and terms for **Khỏe Trọn Vẹn**, version V012022, approved by Ministry of Finance letter 14632/BTC-QLBH of 23 December 2021: a universal-life ("liên kết chung") contract with cancer, critical-illness, intensive-care, disability and death benefits.
Encoded in L4 by one agent in one session (run `VN-24-20261006`, agent `enc-vn-24`, 6-7 October 2026) from `BRIEF.md`.
Status: **draft**. No domain expert has read it against the source; HG1 has not been sought.

## 0. Build and run

- `l4`: `/Users/mengwong/.local/bin/l4`, a symlink to `~/.cabal/bin/l4` → cabal store `jl4-0.1-0ee0100b`, built 2026-10-06 21:20 local, sha256 `64bbcb157dbef2ef1020a6a75589313bba0a2aeeb807c921c5e65e62e9eca118`. The binary has no `--version`.
- `JL4_LIBRARY_PATH` unset. Each run also prints Warnings that differing copies of `prelude` and `daydate` exist under `~/.local/share/jl4/libraries/`; the binary uses its embedded copies; these are not errors.
- Command, from this directory: `L4=/Users/mengwong/.local/bin/l4 ./check.sh`
- Every `.l4` file here is generated: the templates and the scripts are in the session scratchpad (`scratchpad/vn24/tpl/*.tpl`, `scratchpad/vn24/bin/`), which the lead does not commit. `expand.py` replaces each `@@src N M` line of a template by the output of `tools/vnsrc.py quote` (dropping watermark-only lines); `gen_table_tests.py` writes `ktv-tests-tables.l4` from the raw text; `gen_ci_tests.py` writes `ktv-tests-ci.l4` from a specification written from Annexes 6 and 7; `gen_glossary.py` writes `GLOSSARY.md` Part 2 from the `-- vi:` notes in the nouns. The generated files are the deliverable and can be read and edited by hand.

`check.sh` totals (copied from its output, section 6):

```
module                                    errors satisfied  failed  refused  expected
ktv-annex1-definitions.l4                      0         0       0        0         0
ktv-annex2-charges.l4                          0         0       0        0         0
ktv-annex3-fund.l4                             0         0       0        0         0
ktv-annex4-coefficients.l4                     0         0       0        0         0
ktv-annex5-cancer.l4                           0         0       0        0         0
ktv-annex6-early-ci.l4                         0         0       0        0         0
ktv-annex7-severe-ci.l4                        0         0       0        0         0
ktv-assessment.l4                              0         0       0        0         0
ktv-nouns.l4                                   0         0       0        0         0
ktv-part1-benefits.l4                          0         0       0        0         0
ktv-part2-owner-rights.l4                      0         0       0        0         0
ktv-part3-exclusions-and-termination.l4        0         0       0        0         0
ktv-part3-premiums-and-account.l4              0         0       0        0         0
ktv-part4-claims.l4                            0         0       0        0         0
ktv-part5-general.l4                           0         0       0        0         0
ktv-tests-benefits.l4                          0        80       0        0         0
ktv-tests-cancer.l4                            0        31       0        0         0
ktv-tests-ci.l4                                0       182       0        0         0
ktv-tests-exclusions.l4                        0        17       0        0         0
ktv-tests-findings.l4                          0        21       0        0         0
ktv-tests-general.l4                           0       143       0        0         0
ktv-tests-tables.l4                            0       100       0        0         0
TOTAL (22 modules)                             0       574       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

## 1. What is encoded and what is not

**The whole document is in scope and every provision has a disposition in section 2.** Encoded: Articles 1-41 (Parts I-V) and Annexes 1-7, including every table (the allocation and initial-charge tables, the administration-charge schedule, the guaranteed-rate table, both coverage-coefficient tables) as data with one arm per printed row, and all 4 cancer, 23 early-stage and 45 severe-stage definitions as predicates over a findings record per definition.

The encoding answers three questions for a claim, in `ktv-assessment.l4`: is the event covered (in force, Article 24 termination, the Annex definition, the Article's own conditions, once-only rules, Article 23 exclusions), how much is payable (the Article's formula), and, in `ktv-part4-claims.l4`, by when must it be claimed and paid (Articles 25 and 27).
The account mechanics (Article 22 monthly step, allocation, charges, guaranteed rate, no-lapse guarantee, grace and lapse) are encoded as functions over one month's facts.

**Inputs, not encoded:** what the certificate or the Company's books hold — the sum insured, the premiums, the effective and acceptance dates, the account values on a date, the debts, the premium history; the cost-of-insurance amount for a month (the rate table is not in the document, finding X9); the interest credited in a month (the document names the rate but not how it accrues, fork F14); the minimum withdrawal and minimum sum insured the Company sets from time to time; medical facts, each as the record or certificate states it.

**Declined by a named `REFUSE`**, each a gap in the document, not a default: a premium year before 1 or a calendar year before 2022 (Annex 2, Article 20); an issue age above 65 (Annex 4); the cost-of-insurance rates; a main benefit formula or a refund that goes below zero (findings X3, Articles 30, 37, 40); what the sum insured is reduced to after a withdrawal (Article 12(c)); how a misstated age or sex is adjusted (Article 40); how late-payment interest accrues (Article 27); whether an unlisted activity is "dangerous" (Article 23(b)(vi)); a grace period from contract year 5 when the account value has not reached zero (Article 21(a)(ii)).

**Not computed, by design:** the regulative duties with no stated consequence (Articles 33, 36) are encoded as triggers or as a `MUST` without a clock; the Company's discretions (Articles 13(b), 30(b)(ii), 35, 38) are encoded as the options open, never as a choice.

The vintage is the PDF as published at its URL on 2026-10-06 (sha256 `10008a684833…326a6` of the PDF; the `.txt` rendering the `src:` lines point at has sha256 `050520f4bc747d275621698d5f5dfdbb8bdb7c5847b2828e8ecac5ce2f704a43` — the brief's figure `10008a…` is the PDF's).

## 2. Coverage table

Line numbers are lines of `../../source/raw/aia-khoe-tron-ven.txt`.
Headings are given as the document writes them; the Articles' headings sit in a narrow left column, and where `pdftotext -layout` breaks them across lines the breaks are shown as " … ".
Dispositions: **encoded**, **inert** (quoted, not operative, with the reason), **out-of-scope** (none), **reached-and-refused** (encoded as a named refusal because the text does not answer).
Totals: **164 rows**: 155 encoded (some with a part reached-and-refused or inert, said in the row), 9 inert, 0 out-of-scope, 0 deferred.

| provision | heading as written | English gloss | disposition | where in the L4 / reason |
| --- | --- | --- | --- | --- |
| cover, title | Khỏe Trọn Vẹn; QUY TẮC VÀ ĐIỀU KHOẢN (with a diagonal watermark reading "sample rules and terms") | cover page; "sample rules and terms" | inert | a title page; the "MẪU" (sample) watermark runs across every page and is dropped from quotations |
| preamble, src 34-45 | SẢN PHẨM KHỎE TRỌN VẸN | approval line, purpose, who "Công ty" and "Khách hàng" are | encoded | `ktv-annex1-definitions.l4` § Preamble; `Party` in the nouns; the and/or of "Khách hàng" is fork F1 |
| Part I, src 48 | QUYỀN LỢI BẢO HIỂM | benefits | encoded | `ktv-part1-benefits.l4` |
| Art 1(a), src 54-116 | Quyền lợi … bảo hiểm Bệnh … ung thư | cancer benefit: 30% capped at 500 million for early-stage and in-situ; the main formula for major; +100% sum insured for extended major | encoded | `Article 1(a) — the cancer benefit for`; `the cancer benefit on` (assessment) |
| Art 1(b), src 118-119 | (same) | each cancer benefit once in the term | encoded | `Article 1(b) — the cancer benefit for … has not yet been paid in` |
| Art 1(c), src 120-125 | (same) | values fixed at the accepted diagnosis; later premiums refunded without interest | encoded | the account snapshot is the one at the diagnosis; `the refund of premiums received after the event, without interest:` |
| Art 2(a), src 132-152 | Quyền lợi … bảo hiểm Bệnh … hiểm nghèo | early-stage (1 of 23): 30% capped at 500 million; severe (1 of 45): the main formula | encoded | `Article 2(a)(i) …`, `Article 2(a)(ii) …` |
| Art 2(b), src 158-159 | (same) | each critical illness once | encoded | `Article 2(b) — the early-stage condition …`, `… severe-stage condition …` |
| Art 2(c), src 165-170 | (same) | several different early-stage illnesses "within the corresponding limit" | encoded | by the absence of any other bar; fork F16, finding X2 |
| Art 2(d), src 172-184 | (same) | values fixed at the severe diagnosis; later premiums refunded | encoded | as Art 1(c) |
| Art 3(a), src 190-219 | Quyền lợi … bảo hiểm khi … điều trị tại … Phòng Chăm … sóc đặc biệt | +30% sum insured, at most 500 million across the insured's contracts, for 5+ consecutive days in ICU caused by cancer/CI, or by accident/illness in a provincial-level hospital | encoded | `Article 3(a) — the stay qualifies`, `Article 3(a) — the ICU benefit on … for` |
| Art 3(b), src 220-227 | (same) | before age 85 or the next anniversary; once; not deducted from other benefits | encoded | `Article 3(b) — under …`; not deducted: `a cancer or critical-illness benefit:` |
| Art 4, src 234-252 | Quyền lợi hỗ … trợ duy trì hiệu … lực hợp đồng | 200% of the annualised basic premium on the first early-stage cancer, in-situ or early CI diagnosis; once; not deducted | encoded | `Article 4(a) …`, `Article 4 — the premium-support benefit goes with …` |
| Art 5, src 258-285 | Quyền lợi hỗ … trợ chi phí tầm … soát Bệnh ung … thư | 5 million at the end of each 5-year cycle if sum insured ≥ 1 billion, never lapsed, premiums paid; credited to the top-up account | encoded | `Article 5(a) …`; credited in `Article 22 — the accounts after …` |
| Art 6, src 290-331 | Quyền lợi … bảo hiểm Tàn … tật toàn bộ và … vĩnh viễn … (TTTB&VV) … hoặc tử vong | TPD before 75 (or the next anniversary), or death: the main formula; values at the event | encoded | `Article 6(a)(i) …`, `Article 6(a) — the TPD or death benefit on …`; `the TPD benefit on`, `the death benefit on` |
| Art 7, src 333-337 | Quyền lợi … hưởng lãi từ … kết quả đầu tư … của Quỹ liên … kết chung | the account earns the crediting rate, never below the guarantee | encoded | `Article 7 — the rate the contract account value earns …` (Annex 3) |
| Art 8, src 344-352 | Quyền lợi … thưởng duy trì … đóng phí | 5% of the basic account at the end of years 5, 10, 15, 20, if never lapsed and premiums paid | encoded | `Article 8 — …`; fork F19 |
| Art 9, src 354-370 | Quyền lợi … đảm bảo duy … trì hiệu lực … hợp đồng | no-lapse guarantee in years 1-4; unmet deductions become an interest-free debt | encoded | `Article 9 — the no-lapse guarantee applies …`, `Article 9 — the debts after …`; fork F20 |
| Art 10, src 376-381 | Quyền lợi … đáo hạn | the contract account value at maturity if in force and alive | encoded | `Article 10 — …` |
| Part II, src 383 | QUYỀN CỦA BÊN MUA BẢO HIỂM | the policyowner's rights | encoded | `ktv-part2-owner-rights.l4` |
| Art 11, src 387-400 | Cân nhắc … tham gia bảo … hiểm (21 ngày) | free look: 21 days, refund of premiums less medical costs | encoded | `Article 11 — …` (incl. a `DEONTIC`) |
| Art 12, src 402-437 | Rút tiền từ … Giá trị tài … khoản hợp … đồng | withdrawals: top-up any time, basic from the 2nd anniversary up to 80%; top-up first; sum insured cut if basic falls below it | encoded; (c)'s new figure reached-and-refused | `Article 12 …`; `Article 12(c) does not say what the sum insured is reduced to` (fork F25) |
| Art 13, src 439-461 | Thay đổi Số … tiền bảo hiểm | change of sum insured from the 2nd anniversary; increase before 65; decrease not below the minimum; effective date | encoded; (b) inert | `Article 13(a) …`, `Article 13(c) …`; (b) is a discretion with no criteria to encode |
| Art 14, src 463-485 | Thay đổi … Phí bảo hiểm … cơ bản | change of basic premium from the 2nd anniversary, effective at the next anniversary | encoded | `Article 14 — …` |
| Art 15, src 487-502 | Tham gia … thêm các sản … phẩm bổ sung | riders: conditions; effective at the next monthly anniversary | encoded | `Article 15(a) …`, `Article 15(b) …`; the riders' own terms are not in the document |
| Art 16, src 508-522 | Thay đổi … định kỳ đóng … phí | change of frequency at an anniversary, asked 30 days before | encoded | `Article 16 — …` |
| Part III, src 529 | LƯU Ý KHI THAM GIA BẢO HIỂM | notes on joining | encoded | `ktv-part3-*.l4` |
| Art 17, src 531-533 | Thời hạn … hợp đồng | term: to the anniversary after the 100th birthday | encoded | `Article 17 — the end of the contract term of` |
| Art 18, src 535 | Thời hạn … đóng phí | premium term equals the contract term | inert | restates Article 17 for premiums; nothing turns on it separately |
| Art 19, src 538-554 | Đóng phí … bảo hiểm | premiums: 60 days in years 1-4; flexible later if the account covers the deduction; top-up conditions and 5× cap | encoded | `Article 19(a)-(d) …` |
| Art 20, src 556-581 | Phân bổ … phí bảo hiểm | allocation: basic 15/20/65/100%, top-up 100% | encoded (table) | `Article 20 — the allocation rate of …` |
| Art 21, src 584-620 | Gia hạn … đóng phí và … mất hiệu lực … hợp đồng | 60-day grace; benefits kept in grace; lapse from the due date | encoded | `Article 21(a)-(c) …`; findings X5, X6 |
| Art 22, src 626-689 | Giá trị tài … khoản hợp … đồng | basic and top-up account values at the effective date and each monthly anniversary | encoded | `Article 22 — the accounts after the monthly anniversary for`, `Article 22(a)(i), (b)(i) …` |
| Art 23(a), src 691-725 | Các trường … hợp loại trừ … bảo hiểm | death: suicide within 24 months; fraud (innocent beneficiaries paid); else the account value | encoded | `Article 23(a) …`; fork F22 |
| Art 23(b), src 731-748 | (same) | TPD: seven exclusions | encoded; (vi) for unlisted activities reached-and-refused | `Article 23(b) …` |
| Art 23(c), src 752-762 | (same) | cancer and CI: 90-day waiting period and five more | encoded | `Article 23(c) …` |
| Art 24, src 764-847 | Các trường … hợp chấm dứt … hiệu lực hợp … đồng | termination: request, death, early benefits reaching 100% (with refund), TPD or severe paid, age 100, 24 months lapsed, after major cancer, by law; surrender value | encoded; (a)(viii) inert | `Article 24 …`; (a)(viii) "other cases by law" names no case to encode |
| Part IV, src 853 | GIẢI QUYẾT QUYỀN LỢI BẢO HIỂM | claims | encoded | `ktv-part4-claims.l4` |
| Art 25, src 860-863 | Thời hạn … yêu cầu giải … quyết quyền … lợi bảo hiểm | claim within 12 months of the event | encoded | `Article 25 — …`; finding X18 |
| Art 26, src 865-899 | Hồ sơ yêu … cầu giải quyết … quyền lợi bảo … hiểm | the claim documents | encoded | `Article 26 — for … the claim file is complete:`; fork F23 |
| Art 27, src 903-917 | Thời hạn … giải quyết … quyền lợi bảo … hiểm | pay within 30 days of a complete file; late interest | encoded; the interest amount reached-and-refused | `Article 27 — …` incl. a `DEONTIC`; fork F28 |
| Art 28, src 924-950 | Người … nhận quyền lợi … bảo hiểm | who is paid | encoded | `Article 28(a)`, `Article 28(b)`; finding X14 |
| Part V, src 954 | CHƯƠNG V. CÁC ĐIỀU KHOẢN CHUNG | general terms | encoded | `ktv-part5-general.l4` |
| Art 29, src 956-988 | Bảo hiểm … tạm thời | temporary cover: accidental death, min(100 million, sum insured applied for); premium refunds | encoded | `Article 29 — …`; fork F24, finding X15 |
| Art 30, src 993-1045 | Nghĩa vụ … kê khai thông … tin | disclosure duty; misstatement consequences | encoded; (a) inert | `Article 30(b)(i)`, `Article 30(b)(ii)`; (a) states the duty, whose consequences are (b) |
| Art 31, src 1047-1054 | Nghĩa vụ … cung cấp … thông tin của … AIA Việt Nam | the Company's false information: termination with the larger of premiums and account value, plus damages | encoded | `Article 31 — …` |
| Art 32, src 1057-1083 | Trách … nhiệm bảo mật … thông tin … Khách hàng | confidentiality and its exceptions | encoded | `Article 32 — a transfer to a third party is permitted …` |
| Art 33, src 1089-1100 | Thay đổi … nơi cư trú … hoặc nghề … nghiệp | notify before 2+ months abroad or a change of occupation | encoded | `Article 33 — …` (trigger only; no consequence stated) |
| Art 34, src 1102-1152 | Khôi phục … hiệu lực hợp … đồng | reinstatement within 24 months: premiums, health; effective on approval if alive | encoded; (c) inert | `Article 34(a)`, `(b)`; (c) points back to Article 30 |
| Art 35, src 1159-1180 | Xác minh … các khoản tiền … đã đóng | payments by others; money laundering | inert | disclaims a duty and reserves measures; no rule of cover turns on it |
| Art 36, src 1186-1201 | Thay đổi … thông tin liên … quan đến Đạo … luật tuân thủ … thuế Hoa Kỳ | United States tax status: notify immediately | encoded | `Article 36 — the duty to notify …` (`DEONTIC`, no clock) |
| Art 37, src 1205-1211 | Khấu trừ … các khoản chưa … thanh toán | deduct unpaid deductions and premiums before paying | encoded | `Article 37 — what is paid after deducting …`; LAW fork L5 |
| Art 38, src 1217-1247 | Khám, xét … nghiệm y khoa … và khám … nghiệm pháp y | medical examination and autopsy at the Company's cost | inert | a power of the Company with no criteria and no effect on cover the text states |
| Art 39, src 1249-1250 | Chuyển … nhượng hợp … đồng | the assignee must have an insurable interest | encoded | `Article 39 — the assignee qualifies …`; LAW fork L8 |
| Art 40, src 1258-1272 | Kê khai … nhầm lẫn tuổi … và/ hoặc giới … tính của Người … được bảo hiểm | misstated age or sex: adjust; if uninsurable, cancel and refund | encoded; the adjustment reached-and-refused | `Article 40 — …` |
| Art 41, src 1274-1278 | Giải quyết … tranh chấp | negotiation, then a Vietnamese court; suit within 3 years | encoded | `Article 41 — a suit on …` |
| Annex 1, src 1301-1303 | Phụ lục 1: Giải thích từ ngữ | definitions | encoded | `ktv-annex1-definitions.l4` |
| Annex 1 Người được bảo hiểm, src 1305-1309 | Người được bảo hiểm | the insured: insurable interest, accepted, living in Vietnam, 30 days to 65 years, to 100 | encoded | `Annex 1 — the insured person qualifies …` |
| Annex 1 Bên mua bảo hiểm, src 1311-1312 | Bên mua bảo hiểm | the policyowner: an adult with full capacity or a lawful organisation | encoded | `Annex 1 — the policyowner qualifies` |
| Annex 1 Người thụ hưởng; Hồ sơ yêu cầu bảo hiểm; Hợp đồng bảo hiểm; Giấy chứng nhận bảo hiểm, src 1314-1366 | (each as written) | beneficiary, application, contract, certificate | inert | name documents and roles; nothing turns on more than their existence |
| Annex 1 Số tiền bảo hiểm, src 1372 | Số tiền bảo hiểm | sum insured | encoded | an input: `sum insured` |
| Annex 1 Ngày có hiệu lực của hợp đồng, src 1384-1386 | Ngày có hiệu lực của hợp đồng | effective date, if the customer is alive at acceptance | encoded | `Annex 1 — the effective date stands …` |
| Annex 1 anniversaries, src 1388-1392 | Ngày kỷ niệm hợp đồng; Ngày kỷ niệm tháng | policy and monthly anniversaries | encoded | `policy anniversary number`, `monthly anniversary number`, `the first … anniversary after`; fork F3 |
| Annex 1 due date, maturity, src 1394-1406 | Ngày đến hạn đóng phí; Ngày đáo hạn | due date; maturity date | inert | on the certificate; maturity is computed by Article 17 |
| Annex 1 Năm hợp đồng, src 1408-1409 | Năm hợp đồng | contract year | encoded | `the contract year in which …`, `the last day of contract year …` |
| Annex 1 Năm đóng phí, src 1411-1413 | Năm đóng phí | premium year | encoded | an input on `Premium payment`; finding X17 |
| Annex 1 Định kỳ đóng phí, src 1415-1417 | Định kỳ đóng phí | premium frequency | encoded | `Premium frequency` (an input) |
| Annex 1 premiums, src 1423-1443 | Phí bảo hiểm cơ bản; Phí đóng thêm; Phí dự tính | basic, top-up and planned premium | encoded | `Kind of premium`; `Annex 1 — the planned premium of` |
| Annex 1 account values, src 1447-1473 | Giá trị tài khoản cơ bản; Giá trị tài khoản đóng thêm | the accounts and their sum | encoded | `Annex 1 — the contract account value of` |
| Annex 1 charges, src 1480-1497 | Chi phí ban đầu; Chi phí bảo hiểm rủi ro; Khoản khấu trừ hàng tháng | initial, risk, administration and fund charges; the monthly deduction | encoded | `Annex 1 — the monthly deduction of`; Annex 2 module |
| Annex 1 Lãi suất tích lũy, Quỹ liên kết chung, Khoản nợ, src 1499-1508 | Lãi suất tích lũy; Quỹ liên kết chung; Khoản nợ | crediting rate; the fund; debts | encoded | Annex 3 module; `debts` (input) |
| Annex 1 Hành vi gian lận bảo hiểm, src 1514-1528 | Hành vi gian lận bảo hiểm | insurance fraud: two acts | encoded | `Annex 1 — the act is insurance fraud` |
| Annex 1 Bệnh ung thư, Bệnh hiểm nghèo, src 1530-1547 | Bệnh ung thư; Bệnh hiểm nghèo | cancer; critical illness: first arising, at a Hospital, usual practice | encoded | `Annex 1 — the general conditions of a critical illness hold …`; Annex 5 |
| Annex 1 ICU, src 1553-1581 | Phòng Chăm sóc đặc biệt | intensive care unit | encoded | `Annex 1 — the unit is an intensive care unit` |
| Annex 1 TPD, src 1583-1615 | TTTB&VV | total and permanent disability, (a) limbs and sight, (b) 81% | encoded | `Annex 1 — TPD (a) …`, `(b) …`, `… totally and permanently disabled` |
| Annex 1 Bác sĩ, src 1617-1625 | Bác sĩ | Doctor | encoded | `Annex 1 — the person is a Doctor` |
| Annex 1 Tai nạn, src 1631-1646 | Tai nạn | Accident, within 180 days | encoded | `Annex 1 — the event is an Accident` |
| Annex 1 Bệnh viện, src 1650-1683 | Bệnh viện | Hospital, not for convalescence or rehabilitation | encoded | `Annex 1 — the facility is a Hospital` |
| Annex 2, src 1691-1700 | Phụ lục 2: Các khoản chi phí của hợp đồng — Chi phí ban đầu | initial charge table | encoded (table) | `Annex 2 — the initial charge rate on …`; fork F12 |
| Annex 2, src 1703-1720 | Chi phí bảo hiểm rủi ro | cost of insurance, order of deduction | encoded; rates reached-and-refused | `the cost-of-insurance rates … are not printed …`; order in Article 22 |
| Annex 2, src 1727-1777 | Chi phí quản lý hợp đồng | administration charge schedule 30/40/50/60 thousand a month | encoded (table) | `Annex 2 — the contract administration charge …` |
| Annex 2, src 1779-1781 | Chi phí quản lý quỹ | fund charge at most 2% a year | encoded | `Annex 2 — the fund management charge is within its cap at` |
| Annex 2, src 1783-1784 | (other charges) | no withdrawal or surrender charge | encoded | `Annex 2 — the charge on …` |
| Annex 2, src 1786-1788 | (changes) | charges may change with the Ministry's approval and 3 months' notice | encoded | `Annex 2 — a change of charges may take effect …`; finding X9 |
| Annex 3, src 1792-1806 | Phụ lục 3 : Thông tin về Quỹ liên kết chung | fund policy and assets | inert | a statement of investment policy; no rule turns on it |
| Annex 3, src 1808-1846 | Lãi suất cam kết tối thiểu | guaranteed minimum rate table | encoded (table) | `Annex 3 — the minimum guaranteed crediting rate …`, `… the crediting rate the account earns …` |
| Annex 3, src 1848-1854 | (publication) | the rate is published monthly | inert | publication duty with no effect on cover |
| Annex 4, src 1865-1920 | Phụ lục 4: Bảng hệ số bảo hiểm — Dành cho Nam | coefficient table, men | encoded (table) | `Annex 4 — the limits for a man of issue age` |
| Annex 4, src 1922-1970 | Dành cho Nữ | coefficient table, women | encoded (table) | `Annex 4 — the limits for a woman of issue age`; `Annex 4 — under …` |
| list annex, src 1993-2106 | Phụ lục danh sách Bệnh ung thư và Bệnh hiểm nghèo | summary list of the 72 conditions | inert | repeats the item names of Annexes 5-7 |
| Annex 5(1), src 2118-2129 | Ung thư giai đoạn sớm | early-stage cancer | encoded | `Annex 5(1) — …` |
| Annex 5(2), src 2135-2202 | Ung thư biểu mô tại chỗ | carcinoma in situ | encoded | `Annex 5(2) — …` |
| Annex 5(3), src 2204-2229 | Ung thư nghiêm trọng | major cancer | encoded | `Annex 5(3) — …`, `Annex 5 — the cancer the findings establish` |
| Annex 5(4), src 2235-2287 | Ung thư nghiêm trọng mở rộng | extended major cancer | encoded | `Annex 5(4)(a) …`, `Annex 5(4) — under …` |
| Annex 6, src 2296 | Phụ lục 6: Định nghĩa Bệnh hiểm nghèo giai đoạn sớm | early-stage critical illnesses | encoded | `ktv-annex6-early-ci.l4` |
| Annex 6(1), src 2303 | Phẫu thuật bắc cầu động mạch vành xâm lấn tối thiểu | minimally invasive coronary artery bypass surgery | encoded | `Annex 6(1) — minimally invasive coronary artery bypass surgery` |
| Annex 6(2), src 2308 | Thủ thuật can thiệp mạch vành qua da | percutaneous coronary intervention | encoded | `Annex 6(2) — percutaneous coronary intervention` |
| Annex 6(3), src 2326 | Đặt máy tạo nhịp tim hoặc máy khử rung tim | implantation of a pacemaker or defibrillator | encoded | `Annex 6(3) — implantation of a pacemaker or defibrillator` |
| Annex 6(4), src 2339 | Nong và đặt stent động mạch cảnh | carotid artery angioplasty and stenting | encoded | `Annex 6(4) — carotid artery angioplasty and stenting` |
| Annex 6(5), src 2357 | Điều trị bệnh van tim ít xâm lấn | minimally invasive treatment of heart valve disease | encoded | `Annex 6(5) — minimally invasive treatment of heart valve disease` |
| Annex 6(6), src 2376 | Đặt màng lọc tĩnh mạch chủ | insertion of a vena cava filter | encoded | `Annex 6(6) — insertion of a vena cava filter` |
| Annex 6(7), src 2385 | Hôn mê kéo dài ít nhất 48 giờ | coma lasting at least 48 hours | encoded | `Annex 6(7) — coma lasting at least 48 hours` |
| Annex 6(8), src 2397 | Phẫu thuật dẫn lưu não thất | cerebral ventricular shunt surgery | encoded | `Annex 6(8) — cerebral ventricular shunt surgery` |
| Annex 6(9), src 2401 | Phẫu thuật cắt bỏ u tuyến yên | surgical removal of a pituitary tumour | encoded | `Annex 6(9) — surgical removal of a pituitary tumour` |
| Annex 6(10), src 2408 | Tổn thương não | brain damage | encoded | `Annex 6(10) — brain damage` |
| Annex 6(11), src 2443 | Ghép ruột non | small bowel transplant | encoded | `Annex 6(11) — small bowel transplant` |
| Annex 6(12), src 2461 | Phẫu thuật gan | liver surgery | encoded | `Annex 6(12) — liver surgery` |
| Annex 6(13), src 2480 | Xơ gan do viêm gan siêu vi | cirrhosis due to viral hepatitis | encoded | `Annex 6(13) — cirrhosis due to viral hepatitis` |
| Annex 6(14), src 2485 | Phẫu thuật cắt bỏ một bên phổi | removal of one lung | encoded | `Annex 6(14) — removal of one lung` |
| Annex 6(15), src 2495 | Bệnh thận | kidney disease | encoded | `Annex 6(15) — kidney disease` |
| Annex 6(16), src 2510 | Bệnh Lupus ban đỏ hệ thống ít nghiêm trọng | less severe systemic lupus erythematosus | encoded | `Annex 6(16) — less severe systemic lupus erythematosus` |
| Annex 6(17), src 2538 | Thiếu máu bất sản tạm thời | temporary aplastic anaemia | encoded | `Annex 6(17) — temporary aplastic anaemia` |
| Annex 6(18), src 2563 | Ghép giác mạc | corneal transplant | encoded | `Annex 6(18) — corneal transplant` |
| Annex 6(19), src 2578 | Mất thị lực một mắt | loss of sight in one eye | encoded | `Annex 6(19) — loss of sight in one eye` |
| Annex 6(20), src 2585 | Mất thính lực một tai | loss of hearing in one ear | encoded | `Annex 6(20) — loss of hearing in one ear` |
| Annex 6(21), src 2594 | Bỏng mức độ nhẹ | minor burns | encoded | `Annex 6(21) — minor burns` |
| Annex 6(22), src 2598 | Liệt một chi | paralysis of one limb | encoded | `Annex 6(22) — paralysis of one limb` |
| Annex 6(23), src 2603 | Phẫu thuật phục hồi khuôn mặt bị tổn thương do Tai nạn | reconstructive surgery of a face injured in an Accident | encoded | `Annex 6(23) — reconstructive surgery of a face injured in an Accident` |
| Annex 7, src 2634 | Phụ lục 7: Định nghĩa Bệnh hiểm nghèo giai đoạn nghiêm trọng | severe-stage critical illnesses | encoded | `ktv-annex7-severe-ci.l4` |
| Annex 7(1), src 2641 | Phẫu thuật bắc cầu động mạch vành | coronary artery bypass surgery | encoded | `Annex 7(1) — coronary artery bypass surgery` |
| Annex 7(2), src 2647 | Nhồi máu cơ tim | heart attack | encoded | `Annex 7(2) — heart attack` |
| Annex 7(3), src 2664 | Bệnh cơ tim nặng | severe cardiomyopathy | encoded | `Annex 7(3) — severe cardiomyopathy` |
| Annex 7(4), src 2695 | Phẫu thuật van tim | heart valve surgery | encoded | `Annex 7(4) — heart valve surgery` |
| Annex 7(5), src 2716 | Phẫu thuật động mạch chủ | surgery to the aorta | encoded | `Annex 7(5) — surgery to the aorta` |
| Annex 7(6), src 2724 | Tăng áp lực động mạch phổi nguyên phát | primary pulmonary arterial hypertension | encoded | `Annex 7(6) — primary pulmonary arterial hypertension` |
| Annex 7(7), src 2739 | Hôn mê kéo dài ít nhất 96 giờ | coma lasting at least 96 hours | encoded | `Annex 7(7) — coma lasting at least 96 hours` |
| Annex 7(8), src 2750 | Đột quỵ | stroke | encoded | `Annex 7(8) — stroke` |
| Annex 7(9), src 2776 | U não lành tính | benign brain tumour | encoded | `Annex 7(9) — benign brain tumour` |
| Annex 7(10), src 2801 | Chấn thương đầu nặng | severe head injury | encoded | `Annex 7(10) — severe head injury` |
| Annex 7(11), src 2829 | Phẫu thuật não hở | open brain surgery | encoded | `Annex 7(11) — open brain surgery` |
| Annex 7(12), src 2840 | Bệnh Alzheimer hoặc Sa sút trí tuệ | Alzheimer disease or dementia | encoded | `Annex 7(12) — Alzheimer disease or dementia` |
| Annex 7(13), src 2852 | Bệnh tế bào thần kinh vận động | motor neurone disease | encoded | `Annex 7(13) — motor neurone disease` |
| Annex 7(14), src 2871 | Bệnh xơ cứng rải rác | multiple sclerosis | encoded | `Annex 7(14) — multiple sclerosis` |
| Annex 7(15), src 2896 | Viêm não nặng do vi rút | severe viral encephalitis | encoded | `Annex 7(15) — severe viral encephalitis` |
| Annex 7(16), src 2915 | Viêm màng não do vi khuẩn | bacterial meningitis | encoded | `Annex 7(16) — bacterial meningitis` |
| Annex 7(17), src 2920 | Bệnh Parkinson nặng | severe Parkinson disease | encoded | `Annex 7(17) — severe Parkinson disease` |
| Annex 7(18), src 2942 | Bại liệt | poliomyelitis | encoded | `Annex 7(18) — poliomyelitis` |
| Annex 7(19), src 2961 | Suy gan mạn | chronic liver failure | encoded | `Annex 7(19) — chronic liver failure` |
| Annex 7(20), src 2978 | Viêm gan siêu vi tối cấp | fulminant viral hepatitis | encoded | `Annex 7(20) — fulminant viral hepatitis` |
| Annex 7(21), src 3006 | Viêm tụy mạn tính tái phát | chronic relapsing pancreatitis | encoded | `Annex 7(21) — chronic relapsing pancreatitis` |
| Annex 7(22), src 3022 | Bệnh phổi mạn tính | chronic lung disease | encoded | `Annex 7(22) — chronic lung disease` |
| Annex 7(23), src 3035 | Suy thận | kidney failure | encoded | `Annex 7(23) — kidney failure` |
| Annex 7(24), src 3039 | Bệnh Lupus ban đỏ hệ thống | systemic lupus erythematosus | encoded | `Annex 7(24) — systemic lupus erythematosus` |
| Annex 7(25), src 3073 | Thiếu máu bất sản | aplastic anaemia | encoded | `Annex 7(25) — aplastic anaemia` |
| Annex 7(26), src 3106 | Ghép tủy xương | bone marrow transplant | encoded | `Annex 7(26) — bone marrow transplant` |
| Annex 7(27), src 3111 | Ghép tạng | major organ transplant | encoded | `Annex 7(27) — major organ transplant` |
| Annex 7(28), src 3121 | Bỏng nặng | severe burns | encoded | `Annex 7(28) — severe burns` |
| Annex 7(29), src 3125 | Mất khả năng sống độc lập | loss of independent existence | encoded | `Annex 7(29) — loss of independent existence` |
| Annex 7(30), src 3155 | Nhiễm HIV do tai nạn nghề nghiệp | HIV infection from an occupational accident | encoded | `Annex 7(30) — HIV infection from an occupational accident` |
| Annex 7(31), src 3208 | Loạn dưỡng cơ | muscular dystrophy | encoded | `Annex 7(31) — muscular dystrophy` |
| Annex 7(32), src 3229 | Mất thính lực | loss of hearing | encoded | `Annex 7(32) — loss of hearing` |
| Annex 7(33), src 3235 | Mất khả năng phát âm | loss of speech | encoded | `Annex 7(33) — loss of speech` |
| Annex 7(34), src 3244 | Bệnh giai đoạn cuối | terminal illness | encoded | `Annex 7(34) — terminal illness` |
| Annex 7(35), src 3260 | Bệnh Still | Still disease | encoded | `Annex 7(35) — Still disease` |
| Annex 7(36), src 3274 | Bệnh Hemophilia nặng | severe haemophilia | encoded | `Annex 7(36) — severe haemophilia` |
| Annex 7(37), src 3306 | Bệnh thấp tim | rheumatic heart disease | encoded | `Annex 7(37) — rheumatic heart disease` |
| Annex 7(38), src 3314 | Bệnh xương thủy tinh | osteogenesis imperfecta | encoded | `Annex 7(38) — osteogenesis imperfecta` |
| Annex 7(39), src 3329 | Tiểu đường tuýp 1 | type 1 diabetes | encoded | `Annex 7(39) — type 1 diabetes` |
| Annex 7(40), src 3340 | Bệnh Kawasaki có biến chứng tim | Kawasaki disease with cardiac complications | encoded | `Annex 7(40) — Kawasaki disease with cardiac complications` |
| Annex 7(41), src 3362 | Viêm cầu thận có hội chứng thận hư | glomerulonephritis with nephrotic syndrome | encoded | `Annex 7(41) — glomerulonephritis with nephrotic syndrome` |
| Annex 7(42), src 3380 | Bệnh tay chân miệng nặng | severe hand, foot and mouth disease | encoded | `Annex 7(42) — severe hand, foot and mouth disease` |
| Annex 7(43), src 3410 | Bệnh Wilson | Wilson disease | encoded | `Annex 7(43) — Wilson disease` |
| Annex 7(44), src 3421 | Uốn ván thể toàn thân | generalised tetanus | encoded | `Annex 7(44) — generalised tetanus` |
| Annex 7(45), src 3436 | Trạng thái động kinh | status epilepticus | encoded | `Annex 7(45) — status epilepticus` |

No row is `deferred`. There is no `out-of-scope` row: the brief pins the whole document.

## 3. Fork register

Each fork is an ambiguity this encoding resolved. LAW Art 24 (Law on Insurance Business 08/2022/QH15, aid line 588-591) says an unclear term is read in favour of the policyowner; where the reading taken is not the policyowner's, the fork says so.

| # | where | the question | readings | taken, and why |
| --- | --- | --- | --- | --- |
| F1 | preamble, src 43-45 | "Khách hàng" is the policyowner "và/hoặc" the insured: who holds a right given to "Khách hàng"? | (i) the policyowner; (ii) the insured; (iii) either | (i) for the rights of Part II (its heading names the policyowner); for payment, Article 28 decides. Not settled by the text (finding X1). |
| F2 | Annex 1, src 1305-1309; Annex 4 "Tuổi phát hành"; "đạt 85 tuổi" and the like | How is age counted? | (i) completed years (age last birthday); (ii) age nearest birthday; (iii) insurance age | (i). "đạt 85 tuổi" (and the like) is read as that birthday, and a 29 February birthday is reached on 28 February in a common year (`add years` clamps). The Annex 4 row "65" and the entry age "đến 65 tuổi" agree with (i). |
| F3 | Annex 1 "Ngày kỷ niệm hợp đồng", src 1388 | The anniversary of a 29 February effective date in a common year | (i) 28 February; (ii) 1 March | (i): every anniversary is also a monthly anniversary, whose definition (src 1391-1392) takes the last day of the month. |
| F4 | throughout | Is a "ngày" a calendar or a working day? | calendar; working | calendar: the document never mentions working days. |
| F5 | Arts 11, 19, 21, 23, 25, 27, 34, 41; Annex 5(4) | "trong vòng 90 ngày kể từ ngày" D and the like; "sau 02 năm kể từ ngày" | (i) day D not counted, the period ends at the end of D+N (or the same date N months on), inclusive; (ii) day D counted | (i). Outside knowledge, unverified: the Civil Code does not count the first day of a period. "sau 02 năm" (after 2 years) is strictly after. |
| F6 | Arts 3, 6, 17, 24(a)(v), (b)(iii); Annexes 5(4), 7(35)-(45) | "Ngày kỷ niệm hợp đồng kế tiếp" / "ngay sau" a birthday that falls on an anniversary | (i) the anniversary a year later; (ii) that same day | (i): "kế tiếp" and "ngay sau" are after, and (i) is the policyowner's reading. |
| F7 | Art 3(a), src 192 | "điều trị liên tục từ 5 ngày trở" (5 days or more): how are ICU days counted? | (i) days as the hospital record counts them; (ii) nights; (iii) 24-hour periods | (i): an input, `consecutive days of treatment in the unit`. |
| F8 | Art 6(b), src 328-331 | "tại thời điểm Người được bảo hiểm bị TTTB&VV": the date of the event or of the confirmation 6 months later? | (i) the event; (ii) the confirmation | (i) for the age limb (Article 6(a)(i)); the account snapshot is an input either way. |
| F9 | Art 24(a)(iii), src 789 | "đạt 100%": reaches, or exceeds? | at least; more than | at least (`AT LEAST`). |
| F10 | Annex 4 "Tuổi phát hành" | issue age | completed years on the effective date; another measure | completed years on the effective date (with F2). |
| F11 | Art 23(c)(i), src 755-757 | "đã được chẩn đoán trước hoặc trong vòng 90 ngày" | before or within 90 days of the later of acceptance and reinstatement | as written, with F5: excluded up to and including day 90. |
| F12 | Annex 2, src 1700 | The top-up row prints one "0%" under the table | 0% in every premium year; 0% from year 3 only (where it is printed) | every year, as Article 20 prints one top-up figure (100%) for all years; the two then sum to 100% (tested). |
| F13 | Art 21(a)(ii), src 594-595 | From year 5, with no day on which the account value became zero | (i) no grace period runs and nothing lapses; (ii) a due date starts one | (i): refused by name where a grace date is asked for; see finding X6. |
| F14 | Art 7, Art 22, Annexes 1 and 3 | The crediting rate's period, and how a month's interest is computed | annual rate, /12; compound monthly; on the opening or the average balance | the rate is read as annual; the month's interest is an input (`interest on the basic account`). Annex 3 also subtracts an annual charge ("2%/năm") from a monthly yield ("hàng tháng"). |
| F15 | Arts 1, 2, 6 | Is the cancer-screening support a "Quyền lợi bảo hiểm Bệnh ung thư … đã được chi trả" to deduct? | not deducted; deducted | not deducted: it is credited to the top-up account, which the formula already adds. |
| F16 | Art 2(c), src 165-170; Art 24(a)(iii) | "trong giới hạn chi trả tương ứng": is there a cap on the early-stage advances in total? | (i) no aggregate cap: each paid in full, termination at ≥100%; (ii) the last payment is cut to the remainder of 100% | (i), as written; the policyowner's reading. Finding X2. |
| F17 | Art 3(a), src 190-191 | "cho tất cả các Hợp đồng bảo hiểm của Người được bảo" (for all the insured's contracts) | (i) a 500 million cap across all the insured's contracts with the Company; (ii) per contract | (i): what other contracts paid comes off. Which contracts count (this product only? any AIA product?) is an input. |
| F18 | Art 5, src 266-280 | conditions "trong Thời hạn hợp đồng" (during the term) for a payment at the end of year 5 | up to that day; the whole term | up to that day: a payment cannot depend on the future. |
| F19 | Art 8, src 344-352 | the bonus is computed "vào ngày cuối cùng của Năm hợp đồng" and allocated "tại Ngày kỷ niệm" | value on the last day, allocated next day; value on the anniversary | value on the last day of the year, as the first sentence says. |
| F20 | Art 9, src 354-357 | "của 4 Năm hợp đồng đầu tiên" (the premiums of the first 4 contract years) paid in full | premiums due so far paid; all four years paid | due so far: the literal reading empties the guarantee during the years it applies. |
| F21 | Art 22, src 637-689 | order of withdrawals and the deduction within a month | withdrawals first; deduction first | withdrawals first (both are subtracted in the formula; only the shortfall rule needs an order). |
| F22 | Art 23(a), src 703-725 | a beneficiary's fraud: the innocent beneficiaries' shares, or the account value of the last paragraph? | shares; account value; both | shares: (ii) provides for exactly that case; the last paragraph is read for a death not paid at all. Finding X10. |
| F23 | Art 26(b)(ii), src 871-884 | the impairment certificate, asked of every claim? | TPD claims only; every claim | TPD only (finding X11). |
| F24 | Art 29, src 956-975 | first premium over 100 million: refund as well as, or instead of, the benefit? | instead; as well; the refund belongs to a decline | instead: the only reading under which the third sentence ("no obligation to refund" when the cover is paid) also holds. Finding X15. |
| F25 | Art 12(c), src 434-437 | "điều chỉnh giảm tương ứng": reduced to what? | to the basic account value after; by the amount withdrawn from the basic account | not decided: refused by name. |
| F26 | Art 13(c), src 456-461 | "Ngày kỷ niệm hợp đồng gần nhất" (the nearest anniversary) | the next one; the nearer of the last and the next | the next one after approval: an effective date cannot precede the approval. |
| F27 | Art 25, src 860-863 | the day an ICU claim's 12 months run from | start of treatment; end; the 5th day | start of treatment (`ICU stay`'s `start date`). |
| F28 | Art 27, src 909-917 | how late-payment interest accrues | per day at an annual rate; per month | not decided: refused by name; the duty is a `DEONTIC`. |
| L1 | LAW Art 24, aid 588-591 | contra proferentem | — | recorded; each fork above says when its reading is not the policyowner's (F25, F28 are left undecided). |
| L2 | LAW Art 30, aid 706-714 vs Art 25 | the Law's 1-year claim period excludes force majeure and runs from knowledge where the claimant did not know | the document's 12 months stands as written; the Law adds tolling | encoded as written; the Law's tolling is not encoded. |
| L3 | LAW Art 31, aid 718-729 vs Art 27 | 15 days by default; the contract may agree otherwise; late interest by the Civil Code | the contract's 30 days | the contract's 30 days, which the Law permits. |
| L4 | LAW Art 35, aid 760-769 vs Art 11 | free look: Law allows deducting "reasonable costs" | the document deducts medical-examination costs only | as written (narrower than the Law allows, so in the policyowner's favour). |
| L5 | LAW Art 37(4), aid 787-791 vs Arts 9 and 37 | the Law forbids deducting unpaid premiums from the surrender value without consent | Article 37 lets the Company deduct premiums due before paying any benefit or on surrender | encoded as written; whether Article 37 survives the Law is for a lawyer. |
| L6 | LAW Art 37(2)-(3), aid 780-786 vs Arts 21, 34 | grace 60 days; reinstatement within 2 years | — | consistent; encoded as written. |
| L7 | LAW Art 40, aid 815-840 vs Art 23(a), (b) | the Law's own exclusions (death by the policyowner's or beneficiary's intent, execution, permanent injury by intent) and the payment of the surrender value or the premiums | the document's death list has two items | encoded as written; the Law's exclusions are not encoded. |
| L8 | LAW Art 28, aid 679-689 vs Art 39 | transfer of a life contract needs the insured's written consent and the Company's | the document asks only for an insurable interest | encoded as written. |
| L9 | LAW Art 32, aid 730-734 vs Art 41 | mediation and arbitration are also open by agreement | the document names courts | encoded as written. |
| L10 | LAW Art 41(2), aid 849-853 vs Art 23(a)(ii) | beneficiaries share equally where no shares are set | the shares are inputs | consistent: an equal split is supplied as equal shares. |
| L11 | LAW Art 22, aid 535-559 vs Art 30 | on the policyowner's intentional misstatement the Law lets the insurer cancel and refund premiums less reasonable costs | the document adds the options of (b)(ii) | encoded as written. |
| L12 | LAW Art 27(1)(b), aid 646-651 vs Art 21(c) | after termination for non-payment the insurer must pay for events before the termination | the document lapses the contract retroactively to the due date | encoded as written; the Law points to the policyowner's side of finding X5. |
| L13 | the aid itself | the Law's effective-date and transitional articles | — | not in the aid (it ends at Article 130, line 2905); whether the Law governs a contract on this 2021 form is not determined from the texts given. |

## 4. Findings

The hostile reading. Each finding names its source lines, a minimal scenario, and its evidence: an assertion in `ktv-tests-findings.l4` (or another tests module) that passes and shows the surprising answer, or "reading only".

| # | finding | source | scenario | evidence |
| --- | --- | --- | --- | --- |
| X1 | "Khách hàng" means the policyowner and/or the insured, so where they are different people the holder of each Part II right (free look, withdrawal, changes) is not determined. | src 43-45 | an employer owns the policy on an employee's life; the employee asks to withdraw. | reading only |
| X2 | The early-stage advances have no aggregate cap: four early-stage payments of 300 million on a 1 billion sum insured advance 1.2 billion before Article 24(a)(iii) ends the contract, and the termination refund is then paid on top. | src 71-80, 136-138, 165-170, 779-794 | sum insured 1 billion; early-stage cancer, carcinoma in situ, two early-stage illnesses | `X2` group: the fourth claim is `payable` 300 million; 1 200 million paid |
| X3 | The main benefit formula (major cancer, severe illness, TPD, death) has no floor: with advances and Article 9 debts it can go below zero, and the document does not say what is then paid. | src 85-108, 140-152, 307-327, 363-370 | basic 50 million, top-up 50 million, 900 million advanced, 250 million debts | `X3`: `#ASSERT REFUSED` |
| X4 | The 90-day waiting period runs from the Company's acceptance, not from the effective date on which the premium was paid; a slow underwriting stretches it. | src 755-757, 1384-1386 | effective 15 March, accepted 15 May; cancer diagnosed 10 August (148 days after payment) | `X4`: excluded |
| X5 | Article 21(b) keeps the benefits during the grace period, but 21(c) then lapses the contract from the due date, before the grace period began, if the premium is not paid; a death in the grace period is both covered and not. | src 600-620 | premium due 15 March 2023 never paid; death on 1 April 2023 | `X5`: benefits maintained TRUE, in force FALSE |
| X6 | From contract year 5 the grace period starts when the account value reaches zero, but the lapse still dates "từ ngày đến hạn đóng phí" (from the due date), which may be months earlier and which a flexible-premium year does not define. | src 594-595, 607-614 | year 6, account dry on 1 June 2027, last due date 15 March 2027 | `X6`: grace from 1 June, lapse from 15 March |
| X7 | The free-look refund has no time limit for the Company. | src 387-400 | notice on day 10; no refund date | reading only (the `DEONTIC` has no `WITHIN`) |
| X8 | The ICU, premium-support, screening, loyalty and maturity benefits have no exclusions at all; an ICU stay after a drink-driving crash or self-injury is paid while TPD from the same crash is excluded. | src 190-227, 691-762 | 7 days in ICU after a drink-driving crash | `X8`: ICU `payable` 300 million; TPD excluded |
| X9 | The cost of insurance, the largest charge, has no printed rate or basis ("căn cứ theo tuổi, giới tính"), and every charge may be changed during the contract with the Ministry's approval and 3 months' notice; the account values a policyowner relies on are therefore set by the insurer. | src 1719-1720, 1786-1788 | — | reading only; `#ASSERT REFUSED` on the rates |
| X10 | Article 23(a)'s last paragraph pays "Giá trị tài khoản hợp đồng" on an excluded death without saying to whom, and overlaps (ii)'s payment to innocent beneficiaries. | src 703-725 | a beneficiary forges a document | reading only (fork F22) |
| X11 | Article 26(b) lists an impairment certificate from the Medical Assessment Council without a condition: read literally, every claim (a cancer diagnosis, a death) needs one. | src 869-884 | a cancer claim | reading only (fork F23) |
| X12 | Late claims payments earn the rate for "các khoản tạm ứng từ giá trị hợp đồng" (advances from the contract value), but the document offers no such advances. | src 909-917 | a claim paid on day 45 | reading only |
| X13 | Annex 7(30) withholds the occupational-HIV benefit "nếu đã có phương pháp điều trị hiệu quả bệnh HIV". Outside knowledge, unverified: effective antiretroviral therapy exists; on that reading the cover is illusory. | src 3205-3206 | a nurse infected by a needle-stick | reading only |
| X14 | Article 28(b)(ii) sends the death benefit to the policyowner if "bất kỳ" (any) beneficiary died before or with the insured, so one predeceased beneficiary diverts the surviving beneficiaries' shares. | src 942-946 | two beneficiaries at 50%; one predeceased | `X14`: payee is the policyowner |
| X15 | Article 29's three sentences conflict when the first premium exceeds 100 million: refund it, pay the benefit, but no refund if the benefit is paid. As encoded (fork F24) the refund replaces the benefit. | src 956-975 | accidental death; first premium 101 million | `X15`: refund 101 million |
| X16 | Article 30(b)(ii) lets the Company choose among three outcomes at its own decision with no criteria; the third, paying "quyền lợi bảo hiểm nằm ngoài giới hạn", is unintelligible. | src 1028-1045 | a non-disclosure that would have meant an exclusion | reading only; the rule returns the three options |
| X17 | "Năm đóng phí" counts 12 months "từ Ngày kỷ niệm hợp đồng" in which the basic premium was paid in full; the first premium year starts on the effective date, not an anniversary, and a partly paid year's allocation rate is undefined. | src 1411-1413, 556-581 | year 5 paid in part | reading only; premium year is an input |
| X18 | Article 25's 12-month time-bar runs from "ngày được chẩn đoán"; definitions such as loss of speech (12 continuous months) and Kawasaki disease (echo no sooner than 12 months after onset) cannot be met until the bar runs out, unless the diagnosis date is the day the definition is met. | src 860-863, 3236, 3348-3354 | onset 10 January 2024 | `X18`: last day 10 January 2025 |
| X19 | Article 8 values the loyalty bonus on the last day of the year and allocates it on the anniversary; a lapse or claim between the two is unprovided for. | src 344-352 | death on the anniversary | reading only (fork F19) |
| X20 | Article 9 conditions the no-lapse guarantee of years 1-4 on the premiums "của 4 Năm hợp đồng đầu tiên" being paid in full: read literally it cannot apply until it has ended. | src 354-358 | year 2 | reading only (fork F20) |
| X21 | The three exclusion lists differ without reason: dangerous sports exclude TPD but not death; medicine without a prescription excludes cancer and CI but not TPD; fighting excludes TPD but not cancer or CI; only fraud and suicide exclude death. | src 691-762 | a fatal motor race | `X21`: TPD excluded, death paid; `ktv-tests-exclusions.l4` shows each list's near misses |
| X22 | Article 23(b)(vi) names dangerous activities only by example ("như") and never defines "nguy hiểm". | src 743-745 | a TPD in a trail run | `#ASSERT REFUSED` in `ktv-tests-benefits.l4` |
| X24 | A withdrawal from the basic account (allowed from the 2nd anniversary) removes the no-lapse guarantee in years 3-4, and no grace period exists for an account that cannot meet the deduction before year 5: the document does not say whether the contract then lapses. | src 354-370, 415, 584-595 | year 3, withdrawal made, account dry | `X24`: guarantee FALSE, still in force |
| X25 | After a withdrawal the sum insured is cut "tương ứng" without saying to what. | src 434-437 | 80 million withdrawal | `#ASSERT REFUSED` in `ktv-tests-general.l4` |
| X26 | A misstated age or sex is "adjusted" with no method. | src 1265-1268 | — | `#ASSERT REFUSED` in `ktv-tests-general.l4` |
| X29 | The termination refund at 100% advances (Article 24(a)(iii)) does not deduct debts; the surrender value (24(c)) does. | src 789-794, 843-845 | debts 10 million | `X29`: 50 million against 240 million |
| X30 | Article 3(a)(ii) needs an ICU in a hospital "tuyến tỉnh trở lên hoặc tương đương" (provincial tier or equivalent), a Vietnamese tier with no stated equivalent abroad, though Annex 1 covers foreign hospitals. | src 217-219, 1662-1670 | ICU abroad after an accident | reading only (an input) |
| X31 | Article 41's 3 years run from "ngày xảy ra tranh chấp" (the day the dispute arose), which nothing fixes. | src 1277-1278 | — | reading only |

(X23, X27 and X28 were merged into others while drafting: X27 into X9, X28 into fork L5.)

## 5. Answer table

For a sum insured of 1 billion, basic account 200 million, top-up account 50 million, no debts, annualised basic premium 20 million; each figure is asserted in `ktv-tests-benefits.l4`.

| benefit | provision | formula as encoded | worked figure |
| --- | --- | --- | --- |
| early-stage cancer; carcinoma in situ; each early-stage illness | Art 1(a)(i)-(ii), 2(a)(i) | min(30% × sum insured, 500 million) | 300 million (480 at 1.6 billion; 500 at 1.7 billion) |
| major cancer; severe-stage illness; TPD; death | Art 1(a)(iii), 2(a)(ii), 6(a) | max(sum insured, basic) + top-up − cancer/CI benefits paid − debts | 1 050 million; 750 after a 300 million advance |
| extended major cancer | Art 1(a)(iv) | 100% × sum insured | 1 000 million |
| ICU | Art 3(a) | min(30% × sum insured, 500 million − ICU paid on other contracts) | 300 million; 100 after 400 elsewhere |
| premium support | Art 4(a) | 200% × annualised basic premium | 40 million |
| cancer-screening support | Art 5 | 5 million each 5 years (sum insured ≥ 1 billion) | 5 million |
| loyalty bonus | Art 8 | 5% × basic account on the last day of years 5, 10, 15, 20 | 15 million on 300 million |
| maturity | Art 10 | contract account value | 250 million |
| termination at 100% advances | Art 24(a)(iii) | max(0, basic − sum insured) + top-up | 50 million |
| surrender | Art 24(c) | contract account value − debts | 250 million (240 with 10 million debts) |
| temporary cover | Art 29 | min(100 million, sum insured applied for) | 100 million |

## 6. What `check.sh` prints

```
module                                    errors satisfied  failed  refused  expected
ktv-annex1-definitions.l4                      0         0       0        0         0
ktv-annex2-charges.l4                          0         0       0        0         0
ktv-annex3-fund.l4                             0         0       0        0         0
ktv-annex4-coefficients.l4                     0         0       0        0         0
ktv-annex5-cancer.l4                           0         0       0        0         0
ktv-annex6-early-ci.l4                         0         0       0        0         0
ktv-annex7-severe-ci.l4                        0         0       0        0         0
ktv-assessment.l4                              0         0       0        0         0
ktv-nouns.l4                                   0         0       0        0         0
ktv-part1-benefits.l4                          0         0       0        0         0
ktv-part2-owner-rights.l4                      0         0       0        0         0
ktv-part3-exclusions-and-termination.l4        0         0       0        0         0
ktv-part3-premiums-and-account.l4              0         0       0        0         0
ktv-part4-claims.l4                            0         0       0        0         0
ktv-part5-general.l4                           0         0       0        0         0
ktv-tests-benefits.l4                          0        80       0        0         0
ktv-tests-cancer.l4                            0        31       0        0         0
ktv-tests-ci.l4                                0       182       0        0         0
ktv-tests-exclusions.l4                        0        17       0        0         0
ktv-tests-findings.l4                          0        21       0        0         0
ktv-tests-general.l4                           0       143       0        0         0
ktv-tests-tables.l4                            0       100       0        0         0
TOTAL (22 modules)                             0       574       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

Run on 2026-10-07 with the `l4` named in section 0; `check.sh` exited 0.
No module is listed in `expected_failed` and none fails: 0 failed and 0 refused assertions are expected and none occurs.
The rule modules carry no assertions of their own; every `#ASSERT` is in a `ktv-tests-*.l4` module.
`ktv-tests-general.l4` also runs four `#TRACE` directives (Articles 11 and 27), which `check.sh` does not count; their residuals are `FULFILLED`, `FULFILLED` and the Article 27 duty to pay with interest, as the comments above them say.
The tests were run one module at a time while being written, with the same totals per module.

## 7. `vnsrc check`

The gate (every `.l4` and every `.md` here except `BRIEF.md`, as the lead directed on 2026-10-07):

```
vnsrc check: 739 src: lines, 2963 Vietnamese runs, 0 problems
```

The literal command of the brief, `python3 -I tools/vnsrc.py check ../../source/raw/aia-khoe-tron-ven.txt *.l4 *.md`, also checks `BRIEF.md` (the lead's file) and reports one problem there, on line 23 of `BRIEF.md` (the cover's watermark word quoted with the title, which the rendering prints apart). Its last line:

```
vnsrc check: 739 src: lines, 2969 Vietnamese runs, 1 problems
```

The gate is the first command, as the lead directed.

## 8. Open questions for a domain expert

1. Does AIA read "Khách hàng" in Part II as the policyowner (fork F1)?
2. Is there an aggregate cap on the early-stage advances (fork F16, finding X2), and what is paid when the main formula is negative (finding X3)?
3. How is the cost of insurance computed (rate table, sum at risk or sum insured), and how is a month's interest computed from the declared rate (fork F14, finding X9)?
4. Does a death in the grace period with the premium never paid get the death benefit (finding X5, LAW fork L12)?
5. How is the sum insured reduced after a withdrawal (fork F25), and how is a misstated age adjusted (Article 40)?
6. Which contracts count towards the 500 million ICU cap (fork F17)?
7. Does Law 08/2022/QH15 govern contracts on this 2021 form, and if so, which of LAW forks L2, L5, L7, L8 and L12 override the document?
8. Is "ngày được chẩn đoán" in Article 25 the date of first diagnosis or the day the Annex definition is met (finding X18)?
