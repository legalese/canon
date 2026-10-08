# NOTES — PTI Phúc An Sinh health care rules, encoding row `legalese-2026-10-vn-03`

Quy tắc bảo hiểm chăm sóc sức khoẻ Phúc An Sinh of Tổng công ty Cổ phần Bảo hiểm Bưu điện (PTI), issued by Decision 267/QĐ-PTI-BHCN of 26 September 2012, as published at <https://www.pti.com.vn/wp-content/uploads/2025/01/Quy-tac-BH-Phuc-An-Sinh.pdf> on the retrieval date, 2026-10-06.
Encoded in L4 by one agent in one session (run `VN-03-20261006`, agent `enc-vn-03`, finished 2026-10-07), from `BRIEF.md`.
Status: **draft**. No domain expert has read it against the source; HG1 has not been sought; no independent test pass has been run; every expected value was written by the session that wrote the rules.

Line numbers (`src:N`, "src N") are lines of `../../source/raw/pti-phuc-an-sinh.txt`, the `pdftotext -layout` rendering (760 lines) of the PDF whose sha256 is `f0a5d9fda7ea7393f74eb002ee22f99359900c0f91687471c3c3ff17a8ae0778` (checked before use).

## 0. Build and run

- `l4`: `/Users/mengwong/.local/bin/l4`, a symlink to `~/.cabal/bin/l4`, cabal store entry `jl4-0.1-0ee0100b`, built 2026-10-06 21:20, sha256 `64bbcb157dbef2ef1020a6a75589313bba0a2aeeb807c921c5e65e62e9eca118`. It has no `--version`. `JL4_LIBRARY_PATH` unset.
- Command, from this directory: `L4=/Users/mengwong/.local/bin/l4 ./check.sh`.
- The totals line, copied from the run recorded in section 6:

```
TOTAL (13 modules)                             0       405       0        0
```

- Every run also prints two warnings that differing copies of `prelude` and `daydate` exist under `~/.local/share/jl4/libraries/`; the binary uses its embedded copies. They are not errors.
- **Cost.** A module that imports the whole encoding takes about 70 seconds of CPU to typecheck on this binary (several minutes of wall time on a shared machine). `check.sh` runs the thirteen modules in sequence.
- **How the `.l4` files were made.** Each module was written as a template whose `{{src N M}}` lines were expanded by `tools/vnsrc.py quote` (so no `src:` line was typed) and whose short-period table and its tests were generated from src 583-589 by `tools/gen_shortrate.py`. The deposited `.l4` files are the expanded result and stand alone; the expander itself was a scratch script and is not deposited.

## 1. What is encoded and what is not

**Encoded: the whole document.**
Part 1, all 51 definitions (as predicates where a rule turns on them; 10 are inert, for the reasons in section 2).
Part 2, the insuring clauses of Programme I (death, total and partial permanent disablement, medical expenses, occupational disease) and Programme II (benefits 1-3 and the five "other benefits"), and optional benefits 1-6, each as (i) its own conditions, (ii) the heads of cost it pays, (iii) its amount before limits and the limits that apply.
Part 3, all 32 exclusions.
Part 4, all 11 clauses: who is insured, effect, renewal and the 65th birthday, cancellation with the short-period scale and refunds, waiting periods, other insurance, change of limits, examination, subrogation, medical arbitration, disputes.
Part 5, the time limits and forfeiture, every document list, the form of documents, and the direct-billing duties.
`pti-assessment.l4` puts the layers together: is the item within the cover; does an exclusion apply; does a waiting period bar it; how much is payable after co-payment, each limit (less what has been counted against it in the period) and other insurance; and is the claim filed late.

**Inputs, not gaps.** Everything the Rules leave to the certificate or the schedule: the period, the premium, every sum insured, limit and co-payment rate (the Rules print no money figure at all), whether optional benefits and the two unnamed extensions were bought, the contract's own waiting period for illness. Also the facts a witness states: diagnoses, treatments, places, doctors' orders, dates, the assessor's reasonable amount.

**Not in the published file.** Appendices 01 (benefit schedule), 03 (table of disablement rates) and 04 (hospital network) are said to be attached and are not in the PDF; page 16 is a back cover with no text. Their contents enter as inputs (section 2, last rows; finding X0).

**Declined by a named `REFUSE`** (each tested): a partial permanent disablement that Appendix 03 does not list (no rate); the renewal premium by age band (table not in the Rules); the day of last treatment for a claim with neither a hospital stay nor outpatient treatment (a death without treatment); a claim file not yet submitted; PTI's time to pay (the Rules state none); a medical disagreement with no arbitrator appointed at the outset; and, unreachably, a cover the schedule does not carry and a period the short-period scale has no row for.

**The Law.** The Law on Insurance Business 08/2022/QH15 (aid text) postdates the 2012 Rules. It was read only to tag forks `LAW` where it fills or overrides the Rules; it is not encoded. Its commencement date is not in the aid text given; "in force from 1 January 2023" is outside knowledge, unverified.

**Modules.**

| module | what |
| --- | --- |
| `pti-nouns.l4` | DECLARE only |
| `pti-part1-definitions.l4` | Part 1 |
| `pti-part4-conditions.l4` | Part 4 (imported by Parts 2, 3, 5) |
| `pti-part2-benefits.l4` | Part 2 |
| `pti-part3-exclusions.l4` | Part 3 |
| `pti-part5-claims.l4` | Part 5 |
| `pti-assessment.l4` | the layers together |
| `pti-tests-fixtures.l4` | fixtures (no assertions); every money figure hypothetical |
| `pti-tests-conditions.l4` | tests of Parts 1 and 4 (13 generated from the short-period scale) |
| `pti-tests-cover.l4` | tests of Part 2 and of the assessment |
| `pti-tests-exclusions.l4` | each exclusion: a trigger and a near miss |
| `pti-tests-claims.l4` | tests of Part 5 |
| `pti-findings.l4` | the literal readings behind the findings, with evidence |

## 2. Coverage table

Every provision in scope, in the document's order. "heading as written" is the Vietnamese heading, or for an unheaded provision its first words, copied from the raw text by script and checked to occur in it.

| provision | src lines | heading as written | English gloss | disposition | reason or fork | where in the L4 |
| --- | --- | --- | --- | --- | --- | --- |
| cover | 1-12 | QUY TẮC BẢO HIỂM CHĂM SÓC SỨC KHOẺ PHÚC AN SINH | title and the decision issuing the Rules | inert | identification only; the vintage is the published file (fork F1) | nouns header |
| Part 1 chapeau | 17-22 | ĐỊNH NGHĨA | the Rules, certificate and endorsements form the contract; terms mean as defined | inert | a reading instruction; every defined term below has its own row | pti-part1-definitions.l4 |
| def 1 | 23-24 | Công ty bảo hiểm | the insurer (PTI) | inert | names the party; no rule turns on it | party `PTI, the insurer` |
| def 2 | 25-26 | Người được bảo hiểm | the insured person | encoded | as the input record (the person the certificate names) | `The insured person` |
| def 3 | 27-30 | Hợp đồng bảo hiểm | the insurance contract | inert | lists the contract's papers; no rule turns on it | `The policy` |
| def 4 | 31-34 | Thời hạn bảo hiểm | the period of insurance | encoded |  | `the period of insurance of` |
| def 5 | 35-36 | Ngày bắt đầu bảo hiểm | the start date | encoded | fork F3 | `the first day of cover in the current period of` |
| def 6 | 37-38 | Ngày tái tục bảo hiểm | the renewal date | inert | a date of the policy (input) | `The renewal` |
| def 7 | 39-42 | Ngày gia nhập bảo hiểm | the date of joining | encoded | fork F3 | `the start date for waiting periods and exclusions, of` |
| def 8 | 43-47 | Thời gian chờ | waiting period | encoded |  | `a waiting period of` |
| def 9 | 48-50 | Phạm vi địa lý được bảo hiểm | geographical scope | encoded |  | `the geographical scope of` |
| def 10 | 51-52 | Phạm vi bảo hiểm | scope of cover | inert | restates that PTI considers paying covered risks; Part 2 says what is covered | pti-part1-definitions.l4 |
| def 11 | 53-55 | Quyền lợi bảo hiểm | benefit | inert | names what PTI pays; each benefit is encoded under Part 2 | `A benefit` |
| def 12 | 56-58 | Tổng giới hạn bồi thường | main limit | encoded |  | `the main limit of`; pti-assessment.l4 |
| def 13 | 70-72 | Giới hạn phụ | sub-limit | encoded | and the schedule check | `the schedule, checked against definition 13 and Part 2 B` |
| def 14 | 73-76 | Tai nạn | accident | encoded |  | `is an accident within definition 14, in the period of` |
| def 15 | 77-81 | Thương tật thân thể | bodily injury | encoded |  | `caused a bodily injury within definitions 15 and 50` |
| def 16 | 82-84 | Thương tật tạm thời | temporary injury | inert | defined and never used anywhere in the Rules | pti-part1-definitions.l4 |
| def 17 | 85-89 | Thương tật bộ phận vĩnh viễn | partial permanent disablement | encoded |  | `is a partial permanent disablement within definition 17, caused by an accident:` |
| def 18 | 90-94 | Thương tật toàn bộ vĩnh viễn | total permanent disablement | encoded |  | `is a total permanent disablement within definition 18` |
| def 19 | 95-99 | Bệnh đặc biệt | special diseases | encoded |  | `is a special disease within definition 19` |
| def 20 | 100-106 | Bệnh mãn tính | chronic illness | encoded |  | `is chronic within definition 20` |
| def 21 | 107-114 | Tình trạng có sẵn | pre-existing condition | encoded |  | `is pre-existing within definition 21, measured from` |
| def 22 | 127-128 | Tình trạng nguy kịch | critical condition | encoded | as a fact of the item, read by the transport benefit | field `the insured person was in a critical condition ...` |
| def 23 | 129-131 | Vận chuyển cấp cứu | emergency transport | encoded | through the transport benefit's ambulance limb (fork F14) | pti-part2-benefits.l4 |
| def 24 | 132-134 | Dị tật bẩm sinh | congenital defect | encoded | as the diagnosis exclusion 23 reads | condition `a congenital defect or disease` |
| def 25 | 135-139 | Bệnh nghề nghiệp | occupational disease | encoded | as the cause; its list is Vietnamese law at the start of cover (input) | cause `an occupational disease` |
| def 26 | 140-143 | Bác sỹ | doctor | encoded |  | `ordered by a doctor within definition 26` |
| def 27 | 144-147 | Cơ sở y tế | medical establishment | encoded |  | `a medical establishment within definition 27` |
| def 28 | 148-151 | Bệnh viện | hospital | encoded |  | `a hospital within definition 28` |
| def 29 | 152-154 | Khám sức khỏe | health check | encoded | as the treatment exclusion 15 reads | treatment `a health check, ...` |
| def 30 | 155-157 | Điều trị y tế | medical treatment | encoded |  | `is medical treatment within definition 30` |
| def 31 | 158-160 | Nằm viện | hospitalisation (24 hours) | encoded |  | `is a hospitalisation within definition 31` |
| def 32 | 161-163 | Điều trị nội trú | inpatient treatment | encoded |  | `is inpatient treatment within definition 32` |
| def 33 | 164-183 | Chi phí y tế | medical expenses (I)-(VII) | encoded | fork F16 | `is a medical expense within definition 33` |
| def 34 | 184-187 | Chi phí giường nằm | bed charge | encoded |  | `Programme II: the amount before limits for` |
| def 35 | 188-190 | Chi phí hợp lý | reasonable cost | encoded |  | `the reasonable cost of` |
| def 36 | 191-195 | Phẫu thuật | surgery | encoded | as the heads of benefit 2 | `the heads of benefit 2` |
| def 37 | 196-198 | Biến chứng thai sản | complication of pregnancy | encoded | as a head of benefit 4 | `the heads of maternity care` |
| def 38 | 199-202 | Bộ phận giả | prosthesis | encoded | as a head of benefit 2 and a treatment of exclusion 18 | head `a prosthesis to sustain life` |
| def 39 | 203-205 | Cấy ghép nội tạng | organ transplant | encoded | benefit 3 | `Programme II: the conditions are met by` |
| def 40 | 206-207 | Điều trị ngoại trú | outpatient treatment | encoded |  | `is outpatient treatment within definition 40, ...` |
| def 41 | 208-209 | Thuốc theo đơn kê của bác sĩ | prescription medicine | inert | the outpatient benefit's own words are read through the doctor's order | head `medicines prescribed by a doctor` |
| def 42 | 210-213 | Thương tật toàn bộ vĩnh viễn do ốm đau | total permanent disablement from illness | encoded |  | `is a total permanent disablement from illness within definition 42` |
| def 43 | 214-218 | Vật lý trị liệu | physiotherapy | encoded | in hospital, on a doctor's order (optional benefit 2) | `optional benefit 2: the conditions are met by` |
| def 44 | 219-221 | Vật tư thay thế | replacement material | inert | describes a kind of prosthesis; no rule turns on it | pti-part1-definitions.l4 |
| def 45 | 222-226 | Vật tư tiêu hao | consumable material | inert | describes the head `consumables`; no rule turns on its terms | pti-part1-definitions.l4 |
| def 46 | 238-240 | Ốm đau | illness | inert | the cause is the caller's statement | cause `an illness` |
| def 47 | 241-242 | Các hoạt động thể thao chuyên nghiệp | professional sport | encoded |  | `is a professional sport within definition 47` |
| def 48 | 243-246 | Các hoạt động thể thao nguy hiểm | dangerous sport | encoded | fork F17 | `is a dangerous sport within definition 48` |
| def 49 | 247-249 | Chi phí y tế thực tế | actual medical cost | encoded |  | `the reasonable cost of` |
| def 50 | 250-252 | Tổn thương thân thể | bodily injury (second term) | encoded |  | `caused a bodily injury within definitions 15 and 50` |
| def 51 | 253-254 | Người được bảo hiểm tự thanh toán | co-payment | encoded | fork F18 | `PTI's share, after a co-payment of` |
| Part 2 heading | 257-259 | PHẠM VI BẢO HIỂM | scope of cover | inert | heading | pti-part2-benefits.l4 |
| Part 2 A preamble | 260-265 | CÁC QUYỀN LỢI CHÍNH | main benefits: injury or illness in the period; main limit and sub-limits; actual, customary, necessary, reasonable cost | encoded |  | `Part 2: why this item is not covered, if it is not:`; pti-assessment.l4 |
| Part 2 A payees | 266-270 | Đại diện hợp pháp của Người được bảo hiểm | legal representative; to whom PTI may pay; independent adjuster | encoded |  | `Part 2 A: ...` (three rules) |
| Programme I | 272-274 | BẢO HIỂM TAI NẠN CÁ NHÂN | personal accident: accident in the period, consequences within 104 weeks | encoded | fork F9 | `Programme I: the conditions are met by` |
| Programme I death, TPD | 275 | Bồi thường 100% Số tiền bảo hiểm | 100% of the sum insured | encoded |  | `Programme I: the amount before limits for` |
| Programme I PPD | 276-277 | Bảng trả tiền tỷ lệ thương tật | by the Appendix 03 table | encoded | the table is an input (fork F10); an unlisted disablement is refused by name | `the Appendix 03 rate, applied to` |
| Programme I medical | 278-279 | chi phí cấp cứu | emergency, surgery, stay, medicines, tests, diagnostics | encoded |  | `the heads of Programme I's medical expenses` |
| Programme I occupational | 280 | bệnh nghề nghiệp | medical costs of occupational diseases | encoded | fork F24 | pti-part2-benefits.l4 |
| Programme II | 293-294 | BẢO HIỂM NẰM VIỆN VÀ PHẪU THUẬT DO ỐM ĐAU | hospitalisation and surgery for illness | encoded | fork F11 | `Programme II: the conditions are met by` |
| Programme II benefit 1 | 295-298 | Chi phí nằm viện do ốm đau | hospitalisation costs | encoded |  | pti-part2-benefits.l4 |
| Programme II benefit 2 | 299-304 | Chi phí phẫu thuật do ốm đau | surgery costs | encoded |  | `the heads of benefit 2` |
| Programme II benefit 3 | 305-310 | Cấy ghép nội tạng | organ transplant | encoded |  | `the heads of benefit 3` |
| other benefit: before admission | 311-314 | Chi phí trước khi nhập viện | 30 days before admission | encoded | fork F25 | pti-part2-benefits.l4 |
| other benefit: after discharge | 315-317 | Chi phí điều trị sau khi xuất viện | 45 days after discharge | encoded |  | pti-part2-benefits.l4 |
| other benefit: home nursing | 318-320 | Chi phí y tá chăm sóc tại nhà | 15 days after a 7-day stay | encoded |  | pti-part2-benefits.l4 |
| other benefit: daily allowance | 321-322 | Trợ cấp ngày nằm viện | per day in hospital | encoded |  | pti-part2-benefits.l4 |
| other benefit: transport | 323-331 | Chi phí vận chuyển | ambulance, taxi, transfer; within benefits 1-3 | encoded |  | `the heads of transport` |
| Part 2 B | 333 | CÁC QUYỀN LỢI LỰA CHỌN | optional benefits only with Programme II | encoded |  | `was bought in`; schedule check |
| optional benefit 1 | 334-336 | Mở rộng phạm vi lãnh thổ | extension to Asia | encoded | fork F26 | `the geographical scope of` |
| optional benefit 2 (a) | 349-357 | Điều trị ngoại trú do ốm đau | outpatient benefit | encoded |  | `optional benefit 2: the conditions are met by` |
| optional benefit 2 (*) | 358-361 | Lần khám, điều trị trong điều trị ngoại trú do bệnh | what one visit is | encoded | as a fact of the item (`the visit`, the visit flag) | pti-part2-benefits.l4 |
| optional benefit 2 (b) | 362-373 | Hướng dẫn chứng từ yêu cầu trả tiền bảo hiểm | its documents | encoded |  | pti-part5-claims.l4 |
| benefit 3 (a) | 374-379 | Điều trị răng | dental, with co-payment | encoded |  | `the heads of benefit 3, dental` |
| benefit 3 (b) | 380-383 | Hướng dẫn hồ sơ yêu cầu trả tiền bảo hiểm | its documents | encoded |  | pti-part5-claims.l4 |
| benefit 4 (a) | 384-393 | Thai sản, sinh đẻ | maternity, with co-payment | encoded |  | `the heads of maternity care` |
| benefit 4 (**) | 404-407 | Chăm sóc trẻ mới sinh | newborn care | encoded | fork F27 | `the heads of newborn care` |
| benefit 4 (b) | 408-411 | Thời gian chờ | 90 and 365 days | encoded | fork F28 | `benefit 4(b): the waiting period, in days, for` |
| benefit 4 (c) | 412-416 | Giấy chứng nhận phẫu thuật | its documents | encoded |  | pti-part5-claims.l4 |
| optional benefit 5 (a) | 417-421 | Trợ cấp thu nhập | income allowance; not under 18; not maternity | encoded | fork F29 | pti-part2-benefits.l4 |
| optional benefit 5 (b) | 422-431 | Trường hợp ốm đau, bệnh tật | its documents | encoded |  | pti-part5-claims.l4 |
| benefit 6 (a) | 432-441 | Tử vong, thương tật toàn bộ vĩnh viễn do ốm đau | death and disablement from illness | encoded | fork F30 | `the optional benefits: the conditions are met by` |
| benefit 6 (b) | 442-445 | Giấy chứng tử | its documents | encoded |  | pti-part5-claims.l4 |
| Part 3 chapeau | 458-461 | ĐIỂM LOẠI TRỪ | exclusions for all programmes, causing injury or illness | encoded |  | `the exclusions of Part 3 that apply to` |
| exclusion 1 | 462 | Hành động cố ý | exclusion 1 | encoded |  | `exclusion 1 applies to` |
| exclusion 2 | 463-464 | vi phạm pháp luật | exclusion 2 | encoded | fork F31 | `exclusion 2 applies to` |
| exclusion 3 | 465 | ảnh hưởng của rượu | exclusion 3 | encoded |  | `exclusion 3 applies to` |
| exclusion 4 | 466 | đánh nhau | exclusion 4 | encoded |  | `exclusion 4 applies to` |
| exclusion 5 | 467 | Động đất | exclusion 5 | encoded |  | `exclusion 5 applies to` |
| exclusion 6 | 468 | Chiến tranh | exclusion 6 | encoded |  | `exclusion 6 applies to` |
| exclusion 7 | 469-470 | hoạt động hàng không | exclusion 7 | encoded |  | `exclusion 7 applies to` |
| exclusion 8 | 471-472 | Bệnh giang mai | exclusion 8 | encoded |  | `exclusion 8 applies to` |
| exclusion 9 | 473-476 | Điều trị y tế hoặc sử dụng thuốc không có chỉ định | exclusion 9 | encoded | fork F32 | `exclusion 9 applies to` |
| exclusion 10 | 477-478 | Điều trị tại nhà | exclusion 10 | encoded |  | `exclusion 10 applies to` |
| exclusion 11 | 479-482 | Điều trị các bệnh lý về tâm thần | exclusion 11 | encoded |  | `exclusion 11 applies to` |
| exclusion 12 | 483-484 | Những chỉ định phẫu thuật có từ trước | exclusion 12 | encoded | fork F33 | `exclusion 12 applies to` |
| exclusion 13 | 485-487 | điều trị vô sinh | exclusion 13 | encoded |  | `exclusion 13 applies to` |
| exclusion 14 | 488 | Thai sản và sinh đẻ | exclusion 14 | encoded |  | `exclusion 14 applies to` |
| exclusion 15 | 489-491 | Khám sức khoẻ | exclusion 15 | encoded |  | `exclusion 15 applies to` |
| exclusion 16 | 492-494 | theo yêu cầu của Người được bảo hiểm | exclusion 16 | encoded |  | `exclusion 16 applies to` |
| exclusion 17 | 495 | Chỉnh hình | exclusion 17 | encoded |  | `exclusion 17 applies to` |
| exclusion 18 | 496-498 | bộ phận giả | exclusion 18 | encoded | fork F34 | `exclusion 18 applies to` |
| exclusion 19 | 499-500 | Các chất bổ sung | exclusion 19 | encoded |  | `exclusion 19 applies to` |
| exclusion 20 | 501-502 | Phẫu thuật phục hồi thị giác | exclusion 20 | encoded |  | `exclusion 20 applies to` |
| exclusion 21 | 513-514 | phẫu thuật thẩm mỹ | exclusion 21 | encoded |  | `exclusion 21 applies to` |
| exclusion 22 | 515 | kiểm soát trọng lượng cơ thể | exclusion 22 | encoded |  | `exclusion 22 applies to` |
| exclusion 23 | 516 | dị tật và bệnh bẩm sinh | exclusion 23 | encoded |  | `exclusion 23 applies to` |
| exclusion 24 | 517 | thể thao chuyên nghiệp | exclusion 24 | encoded |  | `exclusion 24 applies to` |
| exclusion 25 | 518-519 | nhổ răng sữa | exclusion 25 | encoded |  | `exclusion 25 applies to` |
| exclusion 26 | 520 | Bệnh đặc biệt và bệnh có sẵn | exclusion 26 | encoded | fork F44 | `exclusion 26 applies to` |
| exclusion 27 | 521 | Điều trị ngoại trú | exclusion 27 | encoded | fork F35 | `exclusion 27 applies to` |
| exclusion 28 | 522 | Điều trị ở những nước | exclusion 28 | encoded |  | `exclusion 28 applies to` |
| exclusion 29 | 523 | đại dịch | exclusion 29 | encoded |  | `exclusion 29 applies to` |
| exclusion 30 | 524 | dao mổ | exclusion 30 | encoded |  | `exclusion 30 applies to` |
| exclusion 31 | 525-526 | bất thường về sinh hoá | exclusion 31 | encoded |  | `exclusion 31 applies to` |
| exclusion 32 | 527 | Tử vong không rõ nguyên nhân | exclusion 32 | encoded |  | `exclusion 32 applies to` |
| Part 4 heading | 531-533 | ĐIỀU KIỆN BẢO HIỂM CHUNG | general conditions | inert | heading | pti-part4-conditions.l4 |
| Part 4 cl 1 | 534-542 | Điều kiện của Bên tham gia bảo hiểm | who PTI insures | encoded | forks F4-F6 | `is a person PTI insures under` |
| Part 4 cl 2 | 543-546 | Thời hạn bảo hiểm và hiệu lực bảo hiểm | period and effect | encoded | fork F2 | `Part 4 clause 2: cover in the current period takes effect on` |
| Part 4 cl 3 | 547-550 | Đảm bảo tái tục hợp đồng | guaranteed renewal | encoded |  | `clause 3 renews the policy of` |
| Part 4 cl 3 premium by age band | 551 | Phí bảo hiểm khi tái tục sẽ tăng lên | premium rises with a new age band | reached-and-refused | the premium table and its bands are not in the Rules | `Part 4 clause 3: the age bands of the premium table are not in the Rules` |
| Part 4 cl 3 higher option | 552-553 | lựa chọn cao hơn | waiting period on the higher part | encoded |  | `the size of` l `for` i (pti-assessment.l4) |
| Part 4 cl 3 age 65 | 554-555 | sau ngày sinh nhật thứ 65 | continuous cover ends after the 65th birthday | encoded |  | `continuous cover of` p `goes on at` r |
| Part 4 cl 4 notice | 567-569 | Hủy Hợp đồng bảo hiểm | cancellation on 30 days' notice | encoded | fork F19 | `the notice was sent at least 30 days ahead, for` |
| Part 4 cl 4 refunds | 570-574 | hoàn trả lại 100% phí bảo hiểm | 100% on PTI's cancellation; 80% on the insured's, if no claim paid | encoded |  | `the refund on` |
| Part 4 cl 4 method | 575 | biểu phí ngắn hạn | unexpired premium by the short-period scale | encoded | fork F20 | `the premium for the period not yet in effect, on` |
| Part 4 cl 4 fraud | 576-579 | gian lận | fraud: cancelled at once, no refund | encoded |  | `the refund on` |
| Part 4 cl 4 return of certificate | 580-581 | hoàn trả Giấy chứng nhận bảo hiểm | return the certificate and card within 30 days | encoded |  | deontic, `Part 4 clause 4: ...` |
| Part 4 cl 4 scale | 582-589 | Biểu phí bảo hiểm ngắn hạn | the short-period scale (7 rows) | encoded | generated by tools/gen_shortrate.py | `the short-period scale` |
| Part 4 cl 5 | 590-596 | Thời gian chờ | waiting periods | encoded | forks F3, F7, F8 | `the waiting period for illness, in days, under`; pti-assessment.l4 |
| Part 4 cl 6 | 597-600 | Đồng bảo hiểm | other insurance | encoded | forks F21, F22 | `clause 6: PTI pays, of` |
| Part 4 cl 7 | 601-603 | Thay đổi quyền lợi | limits change only at renewal | encoded |  | `clause 7 accepts a change of limits on` |
| Part 4 cl 8 | 604-607 | Kiểm tra | examination and autopsy | encoded |  | deontic permissions |
| Part 4 cl 9 | 608-611 | Thế quyền đòi bồi thường | subrogation | encoded | fork F23 (LAW) | `clause 9: the rights passed to PTI, on a payment of` |
| Part 4 cl 10 | 623-628 | Trọng tài | medical arbitration | encoded | no arbitrator: refused by name | `clause 10: the medical dispute is settled` |
| Part 4 cl 11 | 629-631 | Giải quyết tranh chấp | disputes | encoded |  | `clause 11: the dispute is decided by` |
| Part 5 heading | 635-636 | THỦ TỤC YÊU CẦU BỒI THƯỜNG | claims procedure | inert | heading | pti-part5-claims.l4 |
| Part 5 general (free documents) | 637-640 | Các thông tin chung về thủ tục yêu cầu trả tiền bảo hiểm | documents free of charge to PTI | inert | no rule turns on it | pti-part5-claims.l4 |
| Part 5 general (further information) | 641-643 | thu thập các thông tin đó từ bác sĩ điều trị bằng chi phí của mình | the insured gathers further information at own cost | encoded | fork F39 | deontic |
| Part 5 general (originals) | 644-645 | Các chứng từ tài chính phải nộp bản gốc | originals and certified copies | encoded | fork F36 | `is in an acceptable form` |
| Part 5 cl 1 notice | 646-648 | Thời hạn nộp hồ sơ yêu cầu bồi thường | notice within 30 days of last treatment | encoded | fork F37 | `the last day to notify PTI of`; deontic |
| Part 5 cl 1 filing | 649-651 | trong vòng 180 ngày | file within 180 days; the day of last treatment | encoded | a death without treatment: refused by name | `the last day to submit the claim file for` |
| Part 5 cl 1 further documents | 652-653 | 120 ngày kể từ ngày gửi đề nghị bổ sung | further documents within 120 days | encoded |  | `the last day to submit further documents asked for on` |
| Part 5 cl 1 forfeiture | 654-655 | trừ trường hợp bất khả kháng | late claims refused in full, save force majeure | encoded | forks F40, F41 (LAW) | `clause 1 refuses in full, for lateness,` |
| Part 5: PTI's time to pay | - | (not stated) | the Rules give PTI no time to assess or pay | reached-and-refused | nothing to encode; LAW fork F42 | `Part 5 states no time within which PTI must assess or pay a claim` |
| Part 5 cl 2 chapeau | 656-657 | Yêu cầu về hồ sơ yêu cầu trả tiền bảo hiểm | the documents | encoded |  | `the documents Part 5 asks for, for` |
| Part 5 cl 2 Programme I | 659-686 | Bản tường trình tai nạn | Programme I documents | encoded |  | `Programme I: the documents for` |
| Part 5 cl 2 stamp note | 687-688 | Dấu hợp lệ của cơ sở y tế là dấu tròn | a valid stamp | encoded |  | `bears a valid stamp of the medical establishment` |
| Part 5 cl 2 Programme II out of network | 692-716 | ĐIỀU TRỊ NỘI TRÚ NGOÀI HỆ THỐNG BỆNH VIỆN BẢO LÃNH VIỆN PHÍ | Programme II documents | encoded | fork F38 | `Programme II: the documents for` |
| Part 5 cl 2 network (a) | 718-723, 733-734 | ĐIỀU TRỊ NỘI TRÚ TRONG HỆ THỐNG BỆNH VIỆN BẢO LÃNH VIỆN PHÍ | direct billing; insured pays the excess | encoded | network membership is an input (Appendix 04) | `the part of a bill of` |
| Part 5 cl 2 network (b) | 735-741 | Trách nhiệm của người được bảo hiểm | insured person's duties | encoded |  | deontic `direct billing: the insured person's duties, ...` |
| Part 5 cl 2 network (c) | 742-744 | Trách nhiệm của PTI | PTI's duties | encoded |  | deontic `direct billing: PTI's duties` |
| signature | 746-755 | PHÓ TỔNG GIÁM ĐỐC | signed for the General Director | inert | signature block | pti-part5-claims.l4 |
| page 16 | (PDF p. 16) | (no text) | back cover | inert | an image page with no text | - |
| Appendix 01 | 261 | Phụ lục 01 | the benefit schedule | out-of-scope | not in the published file; its figures (limits, rates) enter as inputs of `The schedule` | `The schedule` |
| Appendix 03 | 277, 436 | Phụ lục 03 | the table of disablement rates | out-of-scope | not in the published file; the rate for a listed disablement is an input; an unlisted one is refused by name | field `the rate the table gives ...` |
| Appendix 04 | 723 | Phụ lục 04 | PTI's direct-billing hospital network | out-of-scope | not in the published file; membership is an input on the place | field `in PTI's direct-billing hospital network (Appendix 04)` |

Totals: 136 encoded, 18 inert, 3 out-of-scope, 2 reached-and-refused, 0 deferred (159 rows).

## 3. Fork register

Each ambiguity met, the readings seen, the one taken and the text for it. `LAW` marks a fork where Law 08/2022/QH15 (aid lines cited) fills or overrides the Rules; there the Rules are encoded as written unless the fork says otherwise. Where a fork is decided in the insured person's favour "by art 24", that is Law 08/2022/QH15 art 24 (aid lines 588-591): an unclear term of an insurance contract is read in favour of the buyer.

| # | where (src) | question | readings | taken, and why |
| --- | --- | --- | --- | --- |
| F1 | cover, src 8; URL path 2025/01 | Which text? | (i) the published file as retrieved; (ii) a later amended version | (i), as the brief pins. The Law of 2022 postdates the Rules; conflicts are LAW forks, not silent edits. |
| F2 | def 5 src 35-36; Part 4 cl 2 src 546 | When does cover begin if the premium arrives after the certificate's first day? | (i) the later of the two; (ii) the certificate's day | (i): the note says effect begins at 00:00 the day after full premium. |
| F3 | def 5 src 35-36; def 7 src 39-42; Part 4 cl 5 src 595-596 | From which date are waiting periods, pre-existing conditions (def 21), exclusion 12 and exclusion 26's "first year" measured on a contract renewed continuously? | (i) the first day of the current period (def 5 read alone); (ii) the date of joining | (ii): def 7's second sentence makes the latest effective date the start date only for contracts NOT renewed continuously, and clause 5 says continuous renewals take effect at once. (i) is finding X3. |
| F4 | Part 4 cl 1 src 537 | "từ đủ 15 ngày tuổi đến 65 tuổi": does 65 include the whole 65th year? | (i) up to age 65 in completed years; (ii) up to the 65th birthday | (i), the ordinary meaning of an age in years, and by art 24. It sits oddly with clause 3's end of continuous cover after the 65th birthday (finding X22). |
| F5 | Part 4 cl 1 src 534-542 | When are the bars tested? | (i) at each period's start; (ii) at joining only | (i): the cancer bar's proviso for continuous participation would be pointless if bars were tested only at joining. |
| F6 | Part 4 cl 1 src 540 | Epilepsy "applies only to those who take Programme I" | (i) bars Programme I cover; (ii) bars the person entirely if they take Programme I | (i), by art 24. |
| F7 | def 8 src 44; Part 4 cl 5 src 591 | Is the first day of cover day 1 of a waiting period, and does the treatment date or the onset govern? | first day: day 1 or day 0; date: treatment or onset | Day 1 (def 8 counts "kể từ ngày đầu tiên của thời hạn bảo hiểm"); the treatment date (def 8: benefits are not paid during the period). Both by art 24 as well. |
| F8 | Part 4 cl 5 src 593; def 25 | Is an occupational disease an "illness" for the 30-day wait (and for Programme II)? | yes; no | Yes: def 25 calls them diseases. |
| F9 | Programme I src 273-274; def 18 src 90-94 | What must fall within "104 weeks of the accident" for a disablement? | (i) its onset; (ii) its establishment | (i); (ii) makes the benefit unreachable (finding X1). |
| F10 | Programme I src 276-277; benefit 6 src 436-437 | What does Appendix 03 give? | (i) a percentage of the sum insured; (ii) an amount | (i), the usual form of such a table (outside knowledge, unverified); the table is absent. |
| F11 | Programme II src 293, 313-330 | Do Programme II's "other benefits" reach accidents, since they mention injury and accidents? | (i) illness only, the programme's heading; (ii) also accidents | (i); art 24 would argue for (ii): open question 3. |
| F12 | def 17 src 89 | "kéo dài trong vòng 52 tuần liên tục" | (i) has lasted at least 52 weeks; (ii) lasting up to 52 weeks | (i), parallel to def 18's 104 weeks and def 42's 52 weeks. |
| F13 | def 21 src 110 | The "3 years" of def 21(a) end when? | (i) at the start date; (ii) at the claim | (i): the definition is about what existed before the start date. |
| F14 | def 23 src 129-131; transport src 324-326 | Ambulance to the "nearest" adequate place (def 23) or an "appropriate" one (benefit)? | nearest; appropriate | appropriate: the benefit's own words; def 23 is not cited by it. |
| F15 | other benefits src 319-321; benefit 5 src 419 | How are days in hospital counted? | (i) calendar days, both ends; (ii) nights | (i), by art 24. |
| F16 | def 33 src 164-171 | Is the list (I)-(VII) closed? | closed; open | Closed: defs 36, 38, 43 say "bao gồm nhưng không giới hạn" when they mean open; def 33 says only "bao gồm". |
| F17 | def 48 src 245 | "bơi thuyền buồm cách xa bờ 5 km": at 5 km or beyond? | at least 5; more than 5 | More than 5, by art 24. |
| F18 | def 51; benefits 3, 4 | Co-payment before or after the limit? | before; after | Before: def 51 is a percentage "of the cost". |
| F19 | Part 4 cl 4 src 568-569 | "trước 30 ngày kể từ ngày hủy" | notice sent at least 30 days before the day of cancellation; received | Sent, at least 30 days before, inclusive. |
| F20 | Part 4 cl 4 src 575, 582-589 | How is "the premium for the period not yet in effect" computed from the short-period scale, and what is a month? | (i) annual premium less the scale's charge for the time run; (ii) the scale applied to the time left | (i); (ii) would refund more than the premium for the time left. Months are calendar months from the first day of cover, day of the month kept (`add months`, clamping at month end). |
| F21 | Part 4 cl 6 src 598-600 | Two methods joined by "hoặc"; which applies? | the insurer chooses; the larger; the excess where the other insurer has paid | The larger, by art 24 (LAW). Finding X12. |
| F22 | Part 4 cl 6 src 600 | "số tiền bảo hiểm của Quy tắc bảo hiểm này" in the ratio | the benefit's limit; the main limit | The benefit's limit. |
| F23 | Part 4 cl 9 src 608-611 | LAW: Law art 16(4) (aid 402-406) says subrogation does not apply to health insurance; art 38 (aid 792-802) bars the insurer's recourse | clause valid; clause overridden | Encoded as written; flagged as finding X14. Not resolved. |
| F24 | Programme I src 280 | Occupational-disease costs: which heads, which limit? | the accident heads and the medical-expense limit; none stated | The same heads and limit. |
| F25 | other benefits src 314 | "tối đa trong vòng 30 ngày ngay trước ngày nhập viện" | the 30 days before the day of admission; including it | The 30 days before; the day of admission belongs to the stay. |
| F26 | optional benefit 1 src 334-336 | Does the Asia extension reach Programme I? | the whole contract; Programme II only | The whole contract: it widens "the territory insured". |
| F27 | benefit 4 src 386-407 | Newborn care: co-payment? which limit? | its own limit and benefit 4's; its own only | Co-payment applies (benefit 4's first sentence); both limits. |
| F28 | benefit 4(b) src 408-411 | Do the 90/365-day periods govern claims under other benefits (an ovary removed for illness), and newborn care? | benefit 4 only; all | Benefit 4 only; none for newborn care. |
| F29 | benefit 5 src 417 | "trẻ em dưới 18 tuổi" on which day? | admission; claim | The day of admission. |
| F30 | benefit 6 src 438 | "Không nhận bảo hiểm cho người bị bệnh ung thư" | (i) no benefit-6 cover for a person who has cancer when the period begins; (ii) no benefit for a death from cancer | (i); (ii) would exclude the commonest cause of death from illness (open question 5). No continuity proviso, unlike Part 4 cl 1. |
| F31 | exclusion 2 src 463-464 | Does limb 1 ("vi phạm pháp luật") reach traffic offences? | yes; no | No: otherwise limb 2's age 14 does nothing (finding X7). |
| F32 | exclusion 9 src 473-476 | Does the proviso for a vaccination after an accident or bite limit the vaccination limb? | yes; no | Yes, else it never applies (finding X8). |
| F33 | exclusion 12 src 483-484 | Does the proviso for contracts extended to pre-existing conditions govern both limbs? | both; the second | Both. |
| F34 | benefit 2 src 301; exclusion 18 src 496 | A life-sustaining prosthesis bought for surgery: paid (benefit 2) or excluded (exclusion 18)? | paid; excluded | Paid: the specific grant prevails over the general exclusion, and by art 24 (finding X4). |
| F35 | exclusion 27 src 521 | Does it reach the benefits granted in terms for treatment outside a stay? | no; yes | No (finding X5). |
| F36 | Part 5 src 644-645 | Which documents are financial (original) and which medical (certified copy)? | by what each is | Receipts, invoices and itemised bills financial; records, orders, results, prescriptions, discharge papers medical; the rest (accident reports, licences, certificates of death and inheritance, nurse's diploma) no form stated. |
| F37 | Part 5 cl 1 src 647-653 | "trong vòng 30 ngày kể từ" a day X (and the 180 and 120 days): which is the last day? | X + N; X + N - 1 | X + N (day X not counted), by art 24. |
| F38 | Part 5 cl 2 src 692-744 | Network stays; the daily allowance; a taxi | network: no documents from the insured; allowance: the discharge paper; taxi: none listed | as stated. |
| F39 | Part 5 src 641-643 | Time to gather further medical information | the 120 days of cl 1; none | 120 days. |
| F40 | Part 5 cl 1 src 646-655 | "Quá thời hạn trên" forfeits for which time limits? | (i) the claim-file and further-document limits; (ii) also the 30-day notice | (i): the clause is headed as the time limit for submitting the claim file. (ii) is finding X2. |
| F41 | Part 5 cl 1 src 649-651 | LAW: Law art 30(1) (aid 707-710) makes the time to claim one year from the insured event | Rules' 180 days; Law's year | Encoded as written (180 days from last treatment); not resolved. |
| F42 | Part 5 | LAW: the Rules give PTI no time to pay; Law art 31(1) (aid 719-724): 15 days from a complete file | — | Refused by name; the Law's figure is not encoded. |
| F43 | Part 4 cl 4 src 568 | LAW: PTI may cancel on 30 days' notice for any reason; Law art 26 (aid 623-635) lists the grounds for unilateral termination | — | Encoded as written; finding X21. |
| F44 | exclusion 26 src 520 | "năm bảo hiểm đầu tiên" | the year from the start date of F3 | as stated. |
| F45 | Programme I; benefit 6 | Do death, total and partial disablement share one sum insured? | one; separate | One, with each programme's main limit over all. |
| F46 | defs 12-13 | Is there one main limit for the contract or one per programme? Do optional benefits count against Programme II's? | per programme; optional benefits only against their own limits | as stated; Appendix 01 would settle it. |
| F47 | Part 2 A src 261-262 | For illness, must the illness begin in the period or the treatment be in it? | treatment in the period; onset | Treatment (for Programme II, the admission): otherwise a pre-existing condition could never be covered and exclusion 26's "first year" would do nothing. |
| F48 | defs 27-28 src 144-151 | They exclude different kinds of place | literal; harmonised | Literal: a mental-disorder establishment is a medical establishment but not a hospital. |
| F49 | exclusion 25 src 518-519 | Does buying the dental benefit lift the whole exclusion (milk teeth too)? | whole; dental treatment only | Whole. |
| F50 | Part 5 cl 2 src 663 | When is a traffic accident "serious"? | death, a third party, or another serious accident (the list says "như", such as) | as stated; seriousness otherwise is an input. |

Where the encoding looked and found the Rules unambiguous enough to take as they stand: the 7 short-period rows, the 80% and 100% refunds, the age 14 and 18 thresholds, the 50% disablement bar, the 24-hour definition, the 7-day stay for home nursing.

## 4. Findings

The hostile reading. Each finding names the source lines, a minimal scenario and the evidence: an assertion in `pti-findings.l4` (or the tests module named) that shows the surprising answer, or "reading only". All the assertions cited are satisfied in the run of section 6.

**X0. The appendices are missing.** src 261, 277, 436, 723. The Rules pay partial disablement "by the table of Appendix 03 attached to these Rules" and define both permanent disablements by it; they list benefits in Appendix 01 and the hospital network in Appendix 04. The published file has none (16 pages, the last a back cover). A reader cannot learn what a lost finger pays. Reading only (the encoding takes the rates as inputs).

**X1. Total permanent disablement from an accident cannot be shown in time, read literally.** src 273-274, 90-94. Programme I covers consequences "within 104 weeks" of the accident; a disablement not in the table is total and permanent only once it "has lasted 104 weeks without a break". If it must be established within the 104 weeks, only one that began on the day of the accident qualifies. Scenario: accident 1 March 2026, disablement from 5 March. Evidence: `read literally, the disablement ... is established within 104 weeks of` is FALSE for onset on 5 March and TRUE only for onset on 1 March (`pti-findings.l4`). The encoding takes onset (fork F9).

**X19. The claim file is due 18 months before a total disablement can exist.** src 649-651 with 90-94. The claim file is due 180 days after the last treatment. Accident 1 March 2026, discharged 10 March: due 6 September 2026. A disablement from 5 March that is not in the table meets definition 18 only on 2 March 2028. Evidence: `the last day to submit the claim file for` = 2026-09-06, LESS THAN 2028-03-02 (`pti-findings.l4`). Unless the claimant files a claim for something that does not yet exist, the forfeiture clause (src 654-655) bars it. The same holds for partial disablement (52 weeks) and for benefit 6's total disablement from illness (52 weeks). LAW: art 30(1) gives a year from the insured event (fork F41), which is still shorter than 104 weeks.

**X26. A death claim has no day from which its time limits run.** src 650-651. The day of last treatment is defined only for a hospital stay (discharge) and outpatient treatment (diagnosis). A death without treatment has neither, so whether the claim is late cannot be said. Evidence: `#ASSERT REFUSED the total payable on the claim a death claim` (`pti-findings.l4`).

**X2. A late notice may forfeit a claim that is filed in time.** src 646-655. Notice is due within 30 days of the last treatment and the claim file within 180; "past the above time limit" the claim is refused in full. If "the above time limit" includes the notice, a claim notified on day 31 is lost although it could be filed until day 180. Evidence: `read literally, clause 1 refuses in full` is TRUE for notice on day 31 and filing on day 38; the reading taken (F40) is FALSE. LAW: art 19(3) bars relying on late notice caused by force majeure (aid 441-444), which the clause also exempts.

**X3. Definition 5's start date moves every year, and takes cover away at renewal.** src 35-36, 483-484, 520. Read alone, the start date is the first day of each period. Then a surgery ordered in 2025 on a contract held since 2023 is a "surgical indication from before the start date" in 2026 (exclusion 12), and a special disease in 2026 is in "the first year" again (exclusion 26). Evidence: `exclusion 12, with definition 5's start date, applies to` and `exclusion 26, with definition 5's start date, applies to` are TRUE where the encoded exclusions (fork F3) are FALSE (`pti-findings.l4`).

**X4. Benefit 2 pays for a life-sustaining prosthesis that exclusion 18 excludes.** src 301, 496-498. Exclusions apply "to the main programmes and the optional benefits alike" (src 460). Scenario: a pacemaker bought for heart surgery. Evidence: `exclusion 18, read literally, applies to` is TRUE; the encoding (fork F34) pays 5,000,000.

**X5. Exclusion 27, read literally, takes away what other benefits give.** src 521 with 278-279, 312-317. "Outpatient treatment, unless the insured person has the outpatient benefit" would exclude Programme I's emergency care when the person is not admitted (and Programme I alone cannot buy the outpatient option: optional benefits need Programme II, src 333), Programme II's costs before admission and treatment after discharge, and dental and maternity care outside a stay. Evidence: `exclusion 27, read literally, applies to` is TRUE for an examination before admission on Programme II alone and for emergency care after an accident on Programme I alone; the encoding (F35) pays 500,000 and 800,000.

**X6. "Hospitalisation" (24 hours) and "inpatient treatment" (a night) part company.** src 158-163. Benefit 1 needs a hospitalisation (def 31); the income allowance needs inpatient treatment (def 32), and calls it "điều trị nội trú (nằm viện)" as though they were one. Evidence: a 20-hour admitted overnight stay pays the income allowance (600,000) and not benefit 1; a 26-hour stay without admission is a hospitalisation but outpatient treatment, so exclusion 27 takes it away without the outpatient option (`pti-findings.l4`, `pti-tests-exclusions.l4`).

**X7. Exclusion 2's age limit does nothing if traffic law is law.** src 463-464. Limb 1 excludes any breach of the law; limb 2 excludes traffic offences by people aged 14 or more. A 13-year-old's traffic offence is a breach of the law. Evidence: `exclusion 2, read literally, applies to` TRUE; encoded (F31) FALSE.

**X8. Exclusion 9's proviso for a vaccination after an accident or bite never applies, read literally.** src 473-476. Vaccination is excluded (save newborn care); the proviso is attached to "preventive medicine". A rabies shot after a dog bite is a vaccination. Evidence: `exclusion 9, read literally, applies to` TRUE; encoded (F32) FALSE.

**X9. A partial disablement from illness is paid only if an injury table lists it.** src 436-437, 85-89. Benefit 6 pays partial permanent disablement from illness by Appendix 03, but definition 17's descriptive limb needs an accident. Evidence: benefit 6 partial disablement with no table rate is `not covered` (`pti-findings.l4`).

**X10. Definition 13 leaves the main limit nothing to do.** src 56-58, 70-72. If the sub-limits of a programme may not add up to more than its maximum, payments within the sub-limits never reach the maximum. Reading only (the fixtures' arithmetic is asserted).

**X11. Two extensions are named and never offered or defined.** src 484 ("hợp đồng mở rộng bảo hiểm cho tình trạng có sẵn"), src 502 (extension "cho bệnh đặc biệt"). No part of the Rules offers or prices them. Reading only; they are inputs.

**X12. Other insurance: two methods, no rule for choosing.** src 598-600. Evidence: on the same facts the excess method pays 7,000,000 and the ratio method 4,000,000 (`pti-tests-conditions.l4`). The encoding pays the larger (F21).

**X13. Examination at PTI's discretion.** src 604-607. PTI may have the insured person examined "at any time when necessary" during a claim; no criterion, no consequence of refusal. Reading only.

**X14. Subrogation in a health contract.** src 608-611; LAW art 16(4), art 38. Reading only (F23).

**X15. "Routine treatment as regulated by the Ministry of Health" is excluded.** src 492-494. Read literally, standard-of-care treatment is excluded. Evidence: an item so described is excluded by exclusion 16 (`pti-findings.l4`); what the words reach is not said.

**X16. A pedestrian cannot complete a traffic-accident claim.** src 662-665. A copy of the driving licence and vehicle registration is required for every traffic accident. Evidence: a pedestrian who files every other document has `the documents missing from` = the licence copy (`pti-findings.l4`).

**X17. Benefit 6 asks a living claimant for a death certificate.** src 442-445. The list for benefit 6 (death and disablement) is a death certificate, medical documents and an inheritance certificate. Evidence: the documents for a total disablement from illness include the death certificate (`pti-tests-claims.l4`).

**X18. No time for PTI to pay.** Part 5. Evidence: `#ASSERT REFUSED the last day for PTI to pay` (`pti-findings.l4`, `pti-tests-claims.l4`). LAW fork F42.

**X20. "100% of the premium" on PTI's cancellation is three quarters of it after one month.** src 570-571, 575, 583. The refund is of the unexpired premium computed on the short-period scale, which keeps 1/4 for one month. Evidence: PTI cancels after one month of a 12,000,000 premium: refund 9,000,000, less than the 11,000,000 pro rata (`pti-findings.l4`).

**X21. The renewal guarantee does not survive PTI's right to cancel.** src 547-550 with 568-569. PTI "guarantees" renewal but may cancel on 30 days' notice for any reason. LAW: art 26 limits unilateral termination to listed grounds (F43). Reading only.

**X22. A new applicant aged 65 is accepted; a renewing one is not.** src 537, 554-555. Born 1 November 1960: on 1 January 2026 a first policy is accepted (age 65), but a continuous renewal due that day falls after the 65th birthday and ends cover. Evidence: both assertions in `pti-findings.l4`.

**X25. Day-case surgery falls between benefit 2 and the outpatient benefit.** src 299-302, 351-357. Benefit 2 needs a hospitalisation (24 hours); the outpatient benefit pays examinations, tests, medicine and therapies but not surgery. Evidence: a 6-hour surgical stay is not covered under either (`pti-findings.l4`).

**X27. Defined terms missing or doubled.** "Số tiền bảo hiểm" (sum insured) carries the death benefit and is never defined; "Bên tham gia bảo hiểm" (policyholder) and "Đơn bảo hiểm" (policy) are used and not defined; definitions 15 and 50 define two terms for the same bodily injury; definition 16 (temporary injury) is never used. Reading only.

**X28. Numbering.** The optional benefits are numbered "Quyền lợi bổ sung" 1, 2 and 5 but "Quyền lợi" 3, 4 and 6, so "Quyền lợi 3" names both Programme II's organ transplant and dental treatment; the pre-admission documents ask for invoices "trước khi xuất viện" (before discharge, src 697) where "before admission" is meant. Reading only.

## 5. Answer table

Figures are the Rules' own; money is the fixtures' hypothetical money and is marked so.

| question | answer | src |
| --- | --- | --- |
| who may be insured | living and working in Vietnam, from 15 full days old to 65 (F4); not mental illness, leprosy, epilepsy (Programme I), cancer (unless continuous), disablement over 50% | 534-542 |
| cover takes effect | 00:00 the day after full premium, not before the certificate's day | 546 |
| continuous cover ends | the first due date after the 65th birthday | 554-555 |
| waiting periods | illness 30 days (or the contract's); accident none; complications, miscarriage, abortion, ovary removal 90 days; childbirth 365 days; special diseases and pre-existing conditions excluded in the first year | 590-596, 408-411, 520 |
| windows | before admission 30 days; after discharge 45 days; home nursing 15 days after a stay of at least 7 days; accident consequences 104 weeks | 312-320, 273-274 |
| death or total disablement | 100% of the sum insured | 275, 434-435 |
| partial disablement | the Appendix 03 rate (not in the file) | 276-277, 436-437 |
| co-payment (dental, maternity) | the contract's rate, applied before the limit (F18) | 376, 386 |
| notice / file / further documents | 30 / 180 days from the last treatment / 120 days from the request; late filing forfeits, save force majeure | 646-655 |
| PTI's time to pay | not stated | — |
| cancellation notice | 30 days, either party | 568-569 |
| refund | PTI cancels: 100% of the unexpired premium; insured cancels: 80% if no claim paid, else nothing; fraud: nothing | 570-579 |

The short-period scale (src 583-589), with the refund it gives on an annual premium of 12,000,000 (hypothetical) when PTI cancels, and when the insured person cancels with no claim:

| cover has run | the scale keeps | PTI cancels: refund | insured cancels: refund |
| --- | --- | --- | --- |
| up to 1 month | 1/4 | 9,000,000 | 7,200,000 |
| up to 2 months | 3/8 | 7,500,000 | 6,000,000 |
| up to 3 months | 1/2 | 6,000,000 | 4,800,000 |
| up to 4 months | 5/8 | 4,500,000 | 3,600,000 |
| up to 6 months | 3/4 | 3,000,000 | 2,400,000 |
| up to 8 months | 7/8 | 1,500,000 | 1,200,000 |
| over 8 months | 100% | 0 | 0 |

## 6. What `check.sh` prints

Run on 2026-10-07, from this directory, `L4=/Users/mengwong/.local/bin/l4 ./check.sh`:

```
module                                    errors satisfied  failed  refused  expected
pti-assessment.l4                              0         0       0        0         0
pti-findings.l4                                0        36       0        0         0
pti-nouns.l4                                   0         0       0        0         0
pti-part1-definitions.l4                       0         0       0        0         0
pti-part2-benefits.l4                          0         0       0        0         0
pti-part3-exclusions.l4                        0         0       0        0         0
pti-part4-conditions.l4                        0         0       0        0         0
pti-part5-claims.l4                            0         0       0        0         0
pti-tests-claims.l4                            0        54       0        0         0
pti-tests-conditions.l4                        0       141       0        0         0
pti-tests-cover.l4                             0        96       0        0         0
pti-tests-exclusions.l4                        0        78       0        0         0
pti-tests-fixtures.l4                          0         0       0        0         0
TOTAL (13 modules)                             0       405       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

`check.sh` exited 0.

No failure and no refusal is expected, and `check.sh`'s `expected_failed` table lists none.
The seven rule modules and the fixtures module carry no assertions.
`check.sh` does not count `#TRACE` directives; the nine in the tests of Parts 4 and 5 were read in the run output, and each fulfils or breaches as the comment above it says.
Every `#ASSERT REFUSED` names the refusal it expects (`BECAUSE`), so a refusal for another reason would fail.
Not done: a deliberately broken copy to show the harness can fail, and an independent test pass.

## 7. The quotation check

The gate (the lead's clarification of 2026-10-07): `python3 -I tools/vnsrc.py check ../../source/raw/pti-phuc-an-sinh.txt` over every `.l4` file and every `.md` file in this directory except `BRIEF.md`. Its last line:

```
vnsrc check: 973 src: lines, 600 Vietnamese runs, 0 problems
```

The literal command of the brief (`*.l4 *.md`, which includes the lead's `BRIEF.md`) printed:

```
vnsrc check: 973 src: lines, 607 Vietnamese runs, 0 problems
```

## 8. Open questions for a domain expert

1. What are Appendices 01, 03 and 04 for this product, and is a later version of these Rules in force (the file is hosted under a 2025 path but states a 2012 decision)?
2. Does PTI measure waiting periods, pre-existing conditions and exclusions 12 and 26 from the date of joining on continuous renewals (F3), or from each renewal (X3)?
3. Do Programme II's "other benefits" (costs before admission, after discharge, nursing, allowance, transport) apply after an accident (F11)?
4. How does PTI read exclusion 27 against the benefits for treatment outside a stay (X5), and exclusion 18 against benefit 2's prosthesis (X4)?
5. Does "Không nhận bảo hiểm cho người bị bệnh ung thư" in benefit 6 bar insuring a person with cancer, or a claim for a death from cancer (F30)?
6. How are total and partial permanent disablement claimed within the 180-day filing limit (X19), and does a late notice alone forfeit a claim (X2)?
7. Which of the two methods of Part 4 clause 6 does PTI apply, and who chooses (X12)?
8. Is clause 9 (subrogation) applied to health claims after Law 08/2022/QH15 art 16(4) and art 38 (F23)? Is the 180-day limit read subject to art 30, and PTI's time to pay to art 31 (F41, F42)?
9. What is "routine treatment as regulated by the Ministry of Health" in exclusion 16 (X15)?
10. For the age limit "đến 65 tuổi", may a person aged 65 years and some months take out a new policy (F4, X22)?
