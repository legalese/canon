# NOTES — PVI comprehensive health care rules, encoding row `legalese-2026-10-vn-04`

PVI's "Quy tắc bảo hiểm chăm sóc sức khỏe toàn diện" for individual customers, encoded in L4 by one agent in one session (run `VN-04-20261006`, agent `enc-vn-04`, 2026-10-06 to 2026-10-07), from `BRIEF.md`.
Status: **draft**. No domain expert has read it against the source; HG1 has not been sought; no independent test pass has been run; every expected value was written by the same session that wrote the rules.

## 0. Build and run

- `l4`: `/Users/mengwong/.local/bin/l4`, a symlink to `~/.cabal/bin/l4`, which resolves to the cabal store entry `jl4-0.1-0ee0100b`; sha256 `64bbcb157dbef2ef1020a6a75589313bba0a2aeeb807c921c5e65e62e9eca118`. It has no `--version`. `JL4_LIBRARY_PATH` unset; every run prints two Warnings that other copies of `prelude` and `daydate` exist under `~/.local/share/jl4/libraries/` and that the embedded copies are chosen. Those are not errors.
- Command, from this directory: `L4=/Users/mengwong/.local/bin/l4 ./check.sh`.
- The `check.sh` totals are in section 6.
- How the files are made. Every `.l4` file and GLOSSARY.md and COMPARABLES.md are expanded from templates by a script that replaces each `-- @@src N M` placeholder with the output of `python3 -I tools/vnsrc.py quote ../../source/raw/pvi-health.txt N M`, so no `src:` line was typed. `pvi-health-tests-exclusions.l4` is generated from a table (item, fact pattern, expected items). The coverage table below is generated with its Vietnamese headings cut from the raw text by line. The two list-length assertions in `pvi-health-tests-part2.l4` rest on a script count of the raw text's lists (27 comma-separated special diseases, one pair joined without a comma, so 28; 8 deemed pre-existing diseases). The scripts are in the encoder's scratch directory (`scratchpad/enc-vn-04/`), not deposited.

Modules (`@lang en`, English identifiers, Vietnamese only in `src:` comments and short checked runs):

| module | what it holds |
| --- | --- |
| `pvi-health-nouns.l4` | DECLARE only: parties, benefits, causes, the insured person, certificate periods and the schedule, facilities, treatment, costs, dental items, maternity events, death or injury, the named conditions and circumstances, the claim, notices, documents, grounds of refusal |
| `pvi-health-part1-general.l4` | Part I: ages, geography, eligibility (2.1, 2.2), other insurance, premium, termination and refund, renewal, changes, term, law, examination, PVI's liability, dishonesty |
| `pvi-health-part2-definitions.l4` | Part II: every definition, as a predicate, a function, a list or an inert comment |
| `pvi-health-part3-benefits.l4` | Part III: per benefit, scope, waiting periods (with the continuous-renewal chain), own exclusions, amounts |
| `pvi-health-part4-exclusions.l4` | Part IV: one predicate per item, and the list of items a claim engages |
| `pvi-health-assessment.l4` | the three layers together: grounds of refusal, cover, amount payable |
| `pvi-health-part5-claims.l4` | Part V (documents, time limits, PVI's payment duty, regulative rules) and Part VI |
| `pvi-health-fixtures.l4` | named hypothetical people, certificates, facilities, treatments, claims; no directives |
| `pvi-health-tests-part1.l4`, `-part2`, `-part3`, `-part5`, `-exclusions` | tests from the source |
| `pvi-health-findings.l4` | evidence for the findings (section 4); these assertions are expected to pass |

## 1. What is encoded and what is not

**Encoded: the whole document**, Parts I to VI, every clause, definition and list it contains, as the coverage table shows.
The three layers the brief asks for are kept apart: whether the event is covered (`the grounds of refusal of`, `the claim is covered`), how much is payable (`the amount PVI pays on`, built from each benefit's amount rule), and what each party must do and by when (Part V's deadlines and two regulative rules, Part I's notice, refund and permissions).

**Not in the document, so inputs or refusals, not gaps:**
- The schedule of benefits ("Bảng quyền lợi bảo hiểm Chăm sóc Sức khỏe Toàn diện"): every sum insured and limit, the premiums, and the definition of the "chương trình" (programmes) are inputs with no default (`The schedule of benefits`, `programme`, `premium`). A.2.3(c), the "other benefits" that exist only in that schedule, is out of scope for that reason.
- The annex "Bảng tỷ lệ trả tiền bảo hiểm thương tật", which the Rules call attached, is not in the published copy. The rate it gives for an injury is an input (`rate the annex gives for the injury`, `MAYBE NUMBER`, NOTHING meaning not listed).
- "Các trường hợp chấm dứt Hợp đồng bảo hiểm khác thực hiện theo quy định pháp luật hiện hành": the refund in those other cases of termination is declined by a named `REFUSE`, since the law of termination is not encoded.
- The Law on Insurance Business is read as an aid only and is not encoded; where it fills or overrides the Rules the fork register says so (`LAW:`).

**Provenance.** The copy is a mirror on an insurance agent's website, not PVI's own. **No decision number and no date appear anywhere in the document**: I searched the text rendering for the words for decision, number, a day-month-year date and "issued", and found only the Ministry of Health's surgery list ("do Bộ Y tế Việt Nam ban hành", src:365).
The search strings, which are my own and not quotations [translator]: Quyết định, số:, ngày tháng năm, ban hành. The front cover (PDF page 1) and the back cover (PDF page 23) are images with no number or date (rendered and looked at). The PDF's own metadata names the agent's website as author and gives a creation date of 2024-12-20; that is an aid about the mirror, not about the Rules. The printed page numbers run 2 to 23 and then jump to 27 on the back cover: printed pages 24 to 26 are not in the mirror (finding X18).

## 2. Coverage table

Every provision of the document, in its order. The heading column is cut from the raw text by a script (line and word count), so it is the document's own words, sometimes the first words of a clause that has no heading. Dispositions: `encoded` (a rule, a predicate or data in the L4), `inert` (quoted or described, not operative, with the reason), `out-of-scope` (with the reason), `reached-and-refused` (a named `REFUSE` a rule reaches).

| provision | heading as the document writes it | English gloss | disposition | where in the L4, or why |
| --- | --- | --- | --- | --- |
| cover, contents (src:1-32) | QUY TẮC | title and table of contents | inert | headings only; the TOC lists Parts I-VI and no annex |
| preamble (src:33-40) | QUY TẮC | these are PVI's comprehensive health care rules for individual customers | inert | an invitation to read; no rule |
| Part I chapeau (src:44-48) | NGUYÊN TẮC CHUNG | the Rules are an agreement between PVI and the insured person named on the certificate | inert | pvi-health-part1-general.l4 § Part I (quoted); the parties are `A party` in the nouns |
| I.1 (src:50-54) | Phạm vi địa lý được bảo hiểm | geographic scope: personal accident worldwide, other benefits Vietnam | encoded | pvi-health-part1-general.l4 `clause 1 — the geographic scope of`; item 1 in pvi-health-part4-exclusions.l4 |
| I.2.1 para 1 (src:58-64) | Điều kiện tham gia bảo hiểm | who may be insured: citizens or resident foreigners, 15 days to 60, to 65 if continuously insured; 130% loading 61-65 | encoded | pvi-health-part1-general.l4 `clause 2.1 — ...` (residence, age, 61-65 loading) |
| I.2.1 para 2 (src:66-71) | Người được bảo hiểm dưới 18 | under 18 only with a parent and for no more than the parent; under 1 only on programme 1 or 2, 130% loading | encoded | pvi-health-part1-general.l4 `clause 2.1 — a person under 18 ...`, `... under 1 year ...`, infant loading |
| I.2.2 (src:73-79) | Bảo hiểm PVI không nhận bảo hiểm đối | PVI does not accept persons with mental illness, leprosy, cancer, 50%+ disability, or under treatment | encoded | pvi-health-part1-general.l4 `clause 2.2 — PVI does not accept ...`; read through item 34 |
| I.3 (src:85-94) | Hợp đồng bảo hiểm khác | other insurance: PVI pays only what another contract did not | encoded | pvi-health-part1-general.l4 `clause 3 — the costs left for PVI ...`; used in every medical-expense amount |
| I.4 (src:96-103) | Phí bảo hiểm | premium: set on the certificate; no liability unless paid in full and on time | encoded | pvi-health-part1-general.l4 `clause 4 — PVI is not liable ...`; a ground in pvi-health-assessment.l4 |
| I.5.1 (src:105-112) | Ký kết, chấm dứt và tái tục Hợp đồng bảo hiểm | the application form and certificate evidence the contract | inert | evidence of formation; no rule here asks for proof |
| I.5.2 notice (src:114-117) | Hai bên đều có quyền đơn | either party may end the contract on 30 days' written notice; the insured may not postpone | encoded | pvi-health-part1-general.l4 `clause 5.2 — the notice ... is valid`, `... the termination date that takes effect ...` |
| I.5.2 refunds (src:119-127) | Trường hợp Người được bảo hiểm | refund 80% (insured ends, no claim paid) or 100% (PVI ends, not for non-payment, paid in full) of the remaining premium | encoded | pvi-health-part1-general.l4 `clause 5.2 — the premium refunded on early termination` |
| I.5.2 remaining period (src:133-135) | Thời gian còn lại | the remaining period runs from termination to the end of the term | encoded | pvi-health-part1-general.l4 `clause 5.2 — the days remaining ...`, `... the premium for the remaining period ...` |
| I.5.2 other cases (src:137-138) | Các trường hợp chấm dứt Hợp | other cases of termination follow the law in force | reached-and-refused | pvi-health-part1-general.l4 named REFUSE `clause 5.2 leaves the refund for any other case ... to the law in force`: the law of termination is not encoded |
| I.5.3 (src:140-142) | Khi kết thúc thời hạn bảo | at expiry PVI may refuse to renew or change terms | encoded | pvi-health-part1-general.l4 DEONTIC `clause 5.3 — PVI may refuse to renew ...` |
| I.6 (src:144-149) | Thay đổi quyền lợi bảo hiểm | no change of benefits during the term; only at renewal | encoded | pvi-health-part1-general.l4 `clause 6 — a change of benefits can take effect on` |
| I.7 (src:151-154) | Thời hạn bảo hiểm | term: one year (12 months) | encoded | pvi-health-part1-general.l4 `clause 7 — the term is one year` |
| I.8 (src:156-158) | Luật áp dụng | governing law: Vietnamese law | encoded | pvi-health-part1-general.l4 `clause 8 — the governing law` |
| I.9 (src:160-165) | Kiểm tra y tế | PVI may have the insured examined at any time, at its cost | encoded | pvi-health-part1-general.l4 DEONTIC `clause 9 — PVI may ...`; `clause 9 — who bears the cost ...` |
| I.10 limb 1 (src:169-174) | Trường hợp chấm dứt bảo hiểm | on early termination liability ends at once, costs after it not paid | encoded | pvi-health-part1-general.l4 `clause 10 — the last day of PVI's liability under`; pvi-health-assessment.l4 ground; A.2 day-by-day |
| I.10 limb 2 (src:176-189) | Trường hợp bảo hiểm hết hiệu | on expiry liability ends, but events in the term are still handled, except costs after it | encoded | same; with A.1.4 (iv) prevailing for a death within a year (fork F21) |
| I.11 limbs 1-4 (src:191-204) | Kê khai trung thực, đầy đủ | duties to declare honestly, pay, comply, mitigate, notify as early as possible | inert | duties with no stated period or consequence of their own; carried as comments in pvi-health-part1-general.l4 |
| I.11 limb 5 (src:206-210) | Nếu Người được bảo hiểm hoặc | dishonesty: PVI may cancel and/or refuse part or all; premium not refunded | encoded | pvi-health-part1-general.l4 DEONTIC `clause 11 — PVI may refuse part or all ...`; refund 0 |
| I.11 limb 6 (src:212-214) | Trong trường hợp Người được bảo | PVI may refer apparent breaches of law to the authorities | inert | a power to report, with no effect on the claim |
| Part II chapeau (src:219-221) | Một số thuật ngữ trong Quy | terms in these Rules are understood as follows | inert | pvi-health-part2-definitions.l4 |
| II Sự kiện bảo hiểm (src:223-225) | Sự kiện bảo hiểm | insured event | encoded | the whole assessment, pvi-health-assessment.l4 `the claim is covered` |
| II Tai nạn (src:227-234) | Tai nạn | accident | encoded | pvi-health-part2-definitions.l4 `an accident as the Rules define it` |
| II Thương tật thân thể (src:236-237) | Thương tật thân thể | bodily injury | inert | the same test as an accident; no rule reads it apart |
| II Thương tật toàn bộ vĩnh viễn (src:239-245) | Thương tật toàn bộ vĩnh viễn | total permanent injury | encoded | pvi-health-part2-definitions.l4 `a total permanent injury as the Rules define it` |
| II Thương tật bộ phận vĩnh viễn (src:247-254) | Thương tật bộ phận vĩnh viễn | partial permanent injury | encoded | pvi-health-part2-definitions.l4 `a partial permanent injury ...` (fork F15) |
| II Thương tật tạm thời (src:256-258) | Thương tật tạm thời | temporary injury | inert | defined, used by no clause (finding X9) |
| II Ốm đau, bệnh tật (src:260-261) | Ốm đau, bệnh tật | sickness, illness | inert | the caller's classification, `the cause` is `an illness` |
| II Bệnh mãn tính (src:263-264) | Bệnh mãn tính | chronic disease | encoded | pvi-health-part2-definitions.l4 `a chronic disease as the Rules define it` |
| II Bệnh có sẵn (src:266-285) | Bệnh có sẵn | pre-existing disease, with 8 deemed | encoded | pvi-health-part2-definitions.l4 `a pre-existing disease, cover having begun on`, `the diseases deemed pre-existing` |
| II Bệnh đặc biệt (src:287-293) | Bệnh đặc biệt | special disease (closed list of 28) | encoded | pvi-health-part2-definitions.l4 `the special diseases`, `a special disease as the Rules define it` |
| II Bệnh nghề nghiệp (src:295-299) | Bệnh nghề nghiệp | occupational disease | inert | the list is the Ministries'; recorded as a condition, read by item 14 |
| II Bệnh / dị tật bẩm sinh (src:301-304) | Bệnh / dị tật bẩm sinh | congenital disease or defect | inert | recorded as a condition, read by item 17 |
| II Bệnh Di truyền (src:306-310) | Bệnh Di truyền | genetic disease | inert | recorded as a condition, read by item 17 |
| II Bệnh viện (src:312-323) | Bệnh viện | hospital | encoded | pvi-health-part2-definitions.l4 `a hospital as the Rules define it` |
| II Bệnh viện công lập (src:325-332) | Bệnh viện công lập | public hospital | inert | the caller's classification, `kind` is `a public hospital` |
| II Phòng khám (src:334-339) | Phòng khám | clinic | encoded | pvi-health-part2-definitions.l4 `a clinic as the Rules define it` |
| II Người hành nghề khám bệnh, chữa bệnh (src:341-347) | Người hành nghề khám bệnh, chữa bệnh | medical practitioner; relatives are not doctors | encoded | pvi-health-part2-definitions.l4 `indicated by a doctor as the Rules define one` |
| II Nằm viện (src:349-351) | Nằm viện | hospitalisation (24 hours) | encoded | pvi-health-part2-definitions.l4 `a hospitalisation as the Rules define it` (fork F17) |
| II Điều trị nội trú (src:353-355) | Điều trị nội trú | inpatient treatment | encoded | pvi-health-part2-definitions.l4 `inpatient treatment as the Rules define it` |
| II Điều trị trong ngày (src:357-359) | Điều trị trong ngày | day treatment | encoded | pvi-health-part2-definitions.l4 `day treatment as the Rules define it` |
| II Phẫu thuật (src:361-365) | Phẫu thuật | surgery | encoded | pvi-health-part2-definitions.l4 `a surgery as the Rules define it, at` |
| II Phẫu thuật trong ngày (src:367-368) | Phẫu thuật trong ngày | day surgery | encoded | pvi-health-part2-definitions.l4 `a day surgery as the Rules define it, at` |
| II Điều trị ngoại trú (src:370-372) | Điều trị ngoại trú | outpatient treatment | encoded | pvi-health-part2-definitions.l4 `outpatient treatment as the Rules define it, at` |
| II Chi phí thông lệ và hợp lý (src:374-384) | Chi phí thông lệ và hợp lý | customary and reasonable costs | inert | defined, used by no operative clause (finding X9) |
| II Tiền giường điều trị (src:386-388) | Tiền giường điều trị | bed charges; non-medical costs not paid | encoded | pvi-health-part2-definitions.l4 `the covered cost of a day in hospital at` |
| II Phòng tiêu chuẩn (src:390-392) | Phòng tiêu chuẩn | standard room | encoded | same rule, as a price cap (fork F18) |
| II Thuốc kê theo đơn của bác sỹ (src:394-395) | Thuốc kê theo đơn của bác sỹ | prescribed medicine | inert | read into B.1.1 |
| II Lần khám/điều trị (src:397-406) | Lần khám/điều trị | a visit; counting joint consultations | encoded | pvi-health-part2-definitions.l4 `the number of visits counted when` |
| II Chăm sóc y tế tại nhà (src:408-411) | Chăm sóc y tế tại nhà | home medical care | encoded | pvi-health-part2-definitions.l4 `home medical care as the Rules define it`; item 29 |
| II Chi phí trước khi nhập viện (src:413-416) | Chi phí trước khi nhập viện | pre-admission costs (30 days) | encoded | pvi-health-part2-definitions.l4 `a pre-admission cost on` |
| II Chi phí điều trị sau khi xuất viện (src:418-421) | Chi phí điều trị sau khi xuất viện | post-discharge costs (30 days) | encoded | pvi-health-part2-definitions.l4 `a post-discharge cost on` |
| II Thai kỳ (src:423-424) | Thai kỳ | pregnancy | inert | defined, used by no clause (finding X9) |
| II Bộ phận / Dụng cụ giả (src:426-431) | Bộ phận / Dụng cụ giả | prosthesis | inert | recorded as a circumstance, read by item 23 |
| II Dụng cụ/ thiết bị y tế hỗ trợ điều trị (src:433-444) | Dụng cụ/ thiết bị y tế hỗ trợ điều trị | medical devices supporting treatment | encoded | pvi-health-part2-definitions.l4 `a medical device supporting treatment as the Rules define it` |
| II Điều trị phục hồi chức năng (src:446-451) | Điều trị phục hồi chức năng | rehabilitation | inert | recorded as a circumstance, read by item 23 |
| II Vật lý trị liệu (src:453-456) | Vật lý trị liệu | physiotherapy | inert | read into B.1.1 |
| II Dịch bệnh (src:458) | Dịch bệnh | epidemic, as a central authority announces | inert | recorded as a circumstance, read by item 7 |
| II Số tiền bảo hiểm (src:460-463) | Số tiền bảo hiểm | sum insured per insurance year | encoded | pvi-health-part2-definitions.l4 `the sum insured left in the insurance year for` |
| II Giới hạn trách nhiệm chi tiết (src:465-468) | Giới hạn trách nhiệm chi tiết (Giới hạn phụ) | sub-limits, together not above the sum insured | encoded | pvi-health-part2-definitions.l4 `the schedule, checked against the sum insured` |
| II Người được bảo hiểm (src:470-473) | Người được bảo hiểm | insured person | inert | the claim names the insured person |
| II Thời gian chờ (src:480-485) | Thời gian chờ | waiting period; must be shown on the certificate | encoded | pvi-health-part2-definitions.l4 `the waiting periods apply under`; pvi-health-part3-benefits.l4 |
| II Tái tục liên tục (src:487-492) | Tái tục liên tục | continuous renewal | encoded | pvi-health-part2-definitions.l4 `a continuous renewal:` |
| II Đồng chi trả (src:494-500) | Đồng chi trả | co-payment | encoded | pvi-health-part2-definitions.l4 `PVI's part under co-payment of` |
| Part III chapeau (src:505-507) | QUYỀN LỢI BẢO HIỂM | benefits | inert | pvi-health-part3-benefits.l4 |
| III A.1.1 (src:508-512) | Phạm vi bảo hiểm: Bảo hiểm | personal accident: scope | encoded | pvi-health-part3-benefits.l4 `A.1.1 — what the claim lacks ...` |
| III A.1.2 (src:514-515) | Hiệu lực bảo hiểm: Quyền lợi | in force at once | encoded | pvi-health-part3-benefits.l4 `A.1.2 — the waiting period ...` (0) |
| III A.1.3(a) (src:519-522) | Quyền lợi 1 - Tử | Benefit 1: death or total permanent injury, the whole sum insured | encoded | pvi-health-part3-benefits.l4 `A.1 — the amount payable on` |
| III A.1.3(b) (src:527-530) | Quyền lợi 2 - Thương | Benefit 2: partial permanent injury, the annex percentage | encoded | same; the annex rate is an input (annex absent: finding X18) |
| III A.1.4 (src:532-548) | Quy định chung | one sum insured per accident; Benefit 2 at most 100%; no interest; difference on death within one year | encoded | same; `A.1.4 — the interest ...`; pvi-health-assessment.l4 `A.1.4 (iv) ...` |
| III A.2.1 scope (src:550-555) | Phạm vi bảo hiểm: Bảo hiểm | inpatient: illness or accident needing hospitalisation or surgery, no dental | encoded | pvi-health-part3-benefits.l4 `A.2.1 — what the claim lacks ...` (fork F26) |
| III A.2.1 co-payment (src:557-560) | Đối với Người được bảo hiểm | 30/70 for a child under 10 except at public hospitals | encoded | pvi-health-part3-benefits.l4 `the co-payment for a child under 10 applies to` (fork F24) |
| III A.2.2 (src:562-583) | Hiệu lực bảo hiểm: Quyền lợi | waiting periods 0/30/180/365; continuous renewal | encoded | pvi-health-part3-benefits.l4 `the waiting period in days under A.2 or B.1 for`, `the date the waiting periods for ...` |
| III A.2.3(a) (src:587-593) | Trường hợp nằm viện | hospitalisation costs, up to the limit and 60 days a year | encoded | pvi-health-part3-benefits.l4 `A.2.3(a) — ...`, `A.2 — the amount payable on` |
| III A.2.3(b) (src:595-599) | Trường hợp phẫu thuật | surgery costs, up to the limit | encoded | pvi-health-part3-benefits.l4 `A.2.3(b) — ...` |
| III A.2.3(c) (src:601-602) | Các quyền lợi bảo hiểm khác | other benefits, in the schedule | out-of-scope | the benefits are named and limited only in the schedule of benefits, which is not part of the published document; nothing in the document says what they cover, so there is no rule to encode and no claim the nouns can describe for them |
| III B.1.1 (src:605-631) | Quyền lợi bổ sung 1: Điều | outpatient: costs covered; day treatment and day surgery routed here; co-payment | encoded | pvi-health-part3-benefits.l4 `B.1.1 — ...`, `B.1 — the amount payable on` |
| III B.1.2 (src:633-650) | Hiệu lực bảo hiểm: Quyền lợi | waiting periods as A.2 | encoded | pvi-health-part3-benefits.l4 (shared with A.2.2) |
| III B.1.3 (src:652-660) | Loại trừ bảo hiểm: Ngoài quy | outpatient's own exclusions | encoded | pvi-health-part3-benefits.l4 `B.1.3 — the outpatient benefit's own exclusions engaged by` |
| III B.2 heading (src:662-664) | Quyền lợi bổ sung 2: Bảo hiểm | dental care, only with outpatient | encoded | pvi-health-part3-benefits.l4 `B.2 — taken with supplementary benefit 1` |
| III B.2.1 services (src:666-688) | Phạm vi bảo hiểm: Bảo hiểm | dental services covered; scaling once a year; emergency within 24 hours up to 10% | encoded | pvi-health-part3-benefits.l4 `B.2 — the amount payable on` |
| III B.2.1 geography (src:690-698) | Phạm vi bảo hiểm quyền lợi bảo | where dental care is covered | encoded | pvi-health-part3-benefits.l4 `B.2.1 — a facility where dental care is covered` |
| III B.2.2 (src:700-702) | Hiệu lực bảo hiểm: Quyền lợi | dental waiting period 30 days | encoded | pvi-health-part3-benefits.l4 `B.2.2 — ...` |
| III B.2.3 (src:704-710) | Loại trừ bảo hiểm | dentures; cosmetic or orthodontic | encoded | dropped item by item in the B.2 amount |
| III B.3 heading (src:712-715) | Quyền lợi bổ sung 3: Bảo | maternity: women 18-45 on programme 1 or 2 | encoded | pvi-health-part3-benefits.l4 `B.3 — a woman aged 18 to 45 on programme 1 or 2` |
| III B.3.1 (src:717-753) | Phạm vi bảo hiểm: Bảo hiểm | complications, necessary caesarean, normal delivery, up to the limit | encoded | pvi-health-part3-benefits.l4 `B.3.1 — a maternity event the benefit covers`, `B.3 — the amount payable on` |
| III B.3.2 (src:755-767) | Hiệu lực bảo hiểm: Quyền lợi | waiting periods 60 / 365 | encoded | pvi-health-part3-benefits.l4 `B.3.2 — the waiting period in days for` (fork F28) |
| III B.4.1 (src:769-774) | Phạm vi bảo hiểm: Bảo hiểm | death from illness: the whole sum insured | encoded | pvi-health-part3-benefits.l4 `B.4.1 — ...`, `B.4 — the amount payable on` |
| III B.4.2 (src:776-788) | Hiệu lực bảo hiểm: Quyền lợi | waiting periods 30 / 730 | encoded | pvi-health-part3-benefits.l4 `B.4.2 — the waiting period in days for` |
| Part IV chapeau (src:796-801) | (Áp dụng cho quyền lợi chính và tất | exclusions, for every benefit | encoded | pvi-health-part4-exclusions.l4 `the Part IV items engaged by`; pvi-health-assessment.l4 |
| IV item 1 (src:803) | Điều trị ngoài phạm vi địa | exclusion item 1 | encoded | pvi-health-part4-exclusions.l4 `Part IV item 1 — ...` |
| IV item 2 (src:805) | Hành động cố ý của Người | exclusion item 2 | encoded | pvi-health-part4-exclusions.l4 `Part IV item 2 — ...` |
| IV item 3 (src:811) | Tử vong hoặc bất kỳ ốm | exclusion item 3 | encoded | pvi-health-part4-exclusions.l4 `Part IV item 3 — ...` |
| IV item 4 (src:815) | Điều trị và/hoặc chăm sóc cai | exclusion item 4 | encoded | pvi-health-part4-exclusions.l4 `Part IV item 4 — ...` |
| IV item 5 (src:818) | Điều trị hoặc phẫu thuật theo | exclusion item 5 | encoded | pvi-health-part4-exclusions.l4 `Part IV item 5 — ...` |
| IV item 6 (src:821) | Tử vong hoặc bất kỳ ốm | exclusion item 6 | encoded | pvi-health-part4-exclusions.l4 `Part IV item 6 — ...` |
| IV item 7 (src:824) | Tử vong hoặc bất kỳ ốm | exclusion item 7 | encoded | pvi-health-part4-exclusions.l4 `Part IV item 7 — ...` |
| IV item 8 (src:828) | Người được bảo hiểm có ý | exclusion item 8 | encoded | pvi-health-part4-exclusions.l4 `Part IV item 8 — ...` |
| IV item 9 (src:831) | Người được bảo hiểm từ 14 | exclusion item 9 | encoded | pvi-health-part4-exclusions.l4 `Part IV item 9 — ...` |
| IV item 10 (src:835) | Thương tật của Người được bảo | exclusion item 10 | encoded | pvi-health-part4-exclusions.l4 `Part IV item 10 — ...` |
| IV item 11 (src:838) | Tham gia vào các hoạt động | exclusion item 11 | encoded | pvi-health-part4-exclusions.l4 `Part IV item 11 — ...` |
| IV item 12 (src:842) | Tham gia tập luyện hoặc thi | exclusion item 12 | encoded | pvi-health-part4-exclusions.l4 `Part IV item 12 — ...` |
| IV item 13 (src:848) | Bất kỳ việc điều trị hoặc | exclusion item 13 | encoded | pvi-health-part4-exclusions.l4 `Part IV item 13 — ...` |
| IV item 14 (src:853) | Bệnh sốt rét, phong, lao, bệnh | exclusion item 14 | encoded | pvi-health-part4-exclusions.l4 `Part IV item 14 — ...` |
| IV item 15 (src:855) | Điều trị bệnh ung thư, u | exclusion item 15 | encoded | pvi-health-part4-exclusions.l4 `Part IV item 15 — ...` |
| IV item 16 (src:858) | Các bệnh suy tủy, bạch cầu | exclusion item 16 | encoded | pvi-health-part4-exclusions.l4 `Part IV item 16 — ...` |
| IV item 17 (src:861) | Điều trị và/hoặc phẫu thuật cho | exclusion item 17 | encoded | pvi-health-part4-exclusions.l4 `Part IV item 17 — ...` |
| IV item 18 (src:867) | Điều trị và hậu quả của | exclusion item 18 | encoded | pvi-health-part4-exclusions.l4 `Part IV item 18 — ...` |
| IV item 19 (src:870) | Điều trị các chứng ngủ ngáy | exclusion item 19 | encoded | pvi-health-part4-exclusions.l4 `Part IV item 19 — ...` |
| IV item 20 (src:874) | Khám sức khoẻ định kỳ/thông lệ | exclusion item 20 | encoded | pvi-health-part4-exclusions.l4 `Part IV item 20 — ...` |
| IV item 21 (src:883) | Điều trị thẩm mỹ hoặc phẫu | exclusion item 21 | encoded | pvi-health-part4-exclusions.l4 `Part IV item 21 — ...` |
| IV item 22 (src:887) | Điều trị kiểm soát trọng lượng | exclusion item 22 | encoded | pvi-health-part4-exclusions.l4 `Part IV item 22 — ...` |
| IV item 23 (src:891) | Chi phí điều trị phục hồi | exclusion item 23 | encoded | pvi-health-part4-exclusions.l4 `Part IV item 23 — ...` |
| IV item 24 (src:900) | Kế hoạch hoá gia đình, điều | exclusion item 24 | encoded | pvi-health-part4-exclusions.l4 `Part IV item 24 — ...` |
| IV item 25 (src:904) | Các chi phí liên quan đến | exclusion item 25 | encoded | pvi-health-part4-exclusions.l4 `Part IV item 25 — ...` |
| IV item 26 (src:907) | Chăm sóc trước và sau khi | exclusion item 26 | encoded | pvi-health-part4-exclusions.l4 `Part IV item 26 — ...` |
| IV item 27 (src:909) | Các sản phẩm Vitamin hoặc khoáng | exclusion item 27 | encoded | pvi-health-part4-exclusions.l4 `Part IV item 27 — ...` |
| IV item 28 (src:916) | Các điều trị liên quan đến | exclusion item 28 | encoded | pvi-health-part4-exclusions.l4 `Part IV item 28 — ...` |
| IV item 29 (src:918) | Dịch vụ khám hoặc điều trị | exclusion item 29 | encoded | pvi-health-part4-exclusions.l4 `Part IV item 29 — ...` |
| IV item 30 (src:925) | Điều trị và hậu quả của | exclusion item 30 | encoded | pvi-health-part4-exclusions.l4 `Part IV item 30 — ...` |
| IV item 31 (src:928) | Các chi phí điều trị ngoại | exclusion item 31 | encoded | pvi-health-part4-exclusions.l4 `Part IV item 31 — ...` |
| IV item 32 (src:931) | Các chi phí điều trị răng | exclusion item 32 | encoded | pvi-health-part4-exclusions.l4 `Part IV item 32 — ...` |
| IV item 33 (src:934) | Điều trị tại các phòng khám | exclusion item 33 | encoded | pvi-health-part4-exclusions.l4 `Part IV item 33 — ...` |
| IV item 34 (src:940) | Các chi phí và điều trị | exclusion item 34 | encoded | pvi-health-part4-exclusions.l4 `Part IV item 34 — ...` |
| IV item 35 (src:942) | Việc điều trị thử nghiệm, điều | exclusion item 35 | encoded | pvi-health-part4-exclusions.l4 `Part IV item 35 — ...` |
| Part V chapeau (src:948-949) | THỦ TỤC THANH TOÁN BỒI THƯỜNG | claims procedure | inert | pvi-health-part5-claims.l4 |
| V.1 documents (src:950-976) | Hồ sơ yêu cầu bồi thường | the claim dossier | encoded | pvi-health-part5-claims.l4 `clause 1 — the documents required for` (fork F34) |
| V.1 last paragraph (src:978-981) | Tất cả các thông tin, bằng | documents free and in PVI's form; examination on request at PVI's cost | inert | no period; the examination is Part I 9 |
| V.2 (src:(none)) | (none) | there is no clause 2 in Part V | inert | numbering gap (finding X12) |
| V.3 (src:983-988) | Thời hạn yêu cầu trả tiền bồi thường | claim within 6 months, else the right is lost except force majeure | encoded | pvi-health-part5-claims.l4 `clause 3 — the last day ...`, `clause 3 alone — ...` (fork F35) |
| V.4 (src:990-994) | Thời hạn giải quyết yêu cầu trả tiền bảo hiểm | PVI pays within 15 working days of a complete dossier unless agreed otherwise | encoded | pvi-health-part5-claims.l4 `clause 4 — the last day for PVI to pay ...`, DEONTIC `clause 4 — PVI must pay ...` |
| V.5 claim limit (src:1000-1003) | Thời hạn khiếu nại và thời hiệu khởi kiện | claim within 12 months | encoded | pvi-health-part5-claims.l4 `clause 5 — the last day to request payment ...`, DEONTIC `clause 5 — the claimant must send ...` |
| V.5 limitation (src:1005-1006) | Thời hiệu khởi kiện về | suit within 3 years | encoded | pvi-health-part5-claims.l4 `clause 5 — the last day to sue ...` |
| Part VI (src:1011-1016) | GIẢI QUYẾT TRANH CHẤP | negotiation, then the competent court | encoded | pvi-health-part5-claims.l4 `Part VI — the forum ...` |
| back cover (src:1021-1022) | www.pvi.com.vn | page numbers; the back cover is numbered 27 | inert | printed pages 24-26 are absent (finding X18) |

Totals: 110 encoded, 27 inert, 1 out-of-scope, 1 reached-and-refused, 0 deferred (139 rows).

## 3. Fork register

Every ambiguity met, the readings, the one taken and the text for each.
Where no textual argument decides and the reading changes the answer for the policyholder, the reading taken is the one LAW: Art. 24 of the Law on Insurance Business requires (aid lines 588-591: an unclear clause is construed in favour of the policyholder); where the text points one way, the text is followed and Art. 24 is noted.
Rows tagged `LAW:` are where the Law fills or overrides the Rules; none of those conflicts is resolved silently, and none changes the encoded answer (the Law is not encoded), except where the row says so.

**Days.** Waiting periods: calendar days from the date the benefit was first taken up (F22). The 60 days of A.2.3(a): days of a stay, one per day record, counted in the insurance year (the certificate's term). Notice of termination: 30 calendar days (F7). Claim limits: calendar months, by `add months`, which clamps to the end of a short month (F35). Suit: 3 years by `add years`. A.1.4 (iv): one year by `add years`, anniversary included. Pre-existing look-back: 3 years by `add years`, inclusive (F16). Pre-admission and post-discharge windows: 30 calendar days, day 30 included. Dental emergency: 24 hours, the 24th included. PVI's payment: 15 working days (F36). The Rules define none of these units; each reading is recorded here.

| # | where | the question | readings | taken, and why |
| --- | --- | --- | --- | --- |
| F1 | Part I 1, src:52 | Which benefit is "quyền lợi Bảo hiểm Tai nạn", worldwide? | (i) main benefit A.1 only; (ii) any benefit claimed for an accident (A.2 or B.1 treatment of an injury abroad) | **(i)**: A.1 is titled "Bảo hiểm Tai nạn cá nhân" (src:508); A.2 and B.1 treat an accident as one cause among others. Art. 24 could favour (ii); the text points to (i). |
| F2 | Part I 2.1 src:70; B.3 src:714 | What are "chương trình 1 hoặc 2"? | defined only in the schedule | **input** (`programme`, a NUMBER); the document does not define the programmes. |
| F3 | Part I 2.1 src:61-62; every age in the Rules | How is age counted, and are the end ages included? | (i) completed years by the last birthday, ends included; (ii) nearest birthday; (iii) exclusive ends | **(i)** for every age (15 days, 60, 65, 18, 1, 6, 10, 14, 18-45): 2.1 says "tính theo lần sinh nhật gần nhất" and no other clause says otherwise. "đến 60 (sáu mươi) tuổi" read as up to and including age 60. |
| F4 | Part I 2.1 | On what date is eligibility by age tested? | (i) the certificate's start date; (ii) each claim date | **(i)**: the conditions are "điều kiện tham gia bảo hiểm" (conditions for joining). Ages for the co-payment (under 10) are taken on the date of treatment, for the 180-day period and item 9 on the date of the event, for B.3 (18-45) on the start date. |
| F5 | Part I 2.2, src:73-79; item 34, src:940 | When is "đang bị", "đang trong thời gian điều trị" (currently ill, currently under treatment) tested? | (i) when the insurance is taken out; (ii) when a claim is made | **(i)**. (ii) refuses every claimant, since a claimant is under treatment (finding X4). |
| F6 | Part I 3, src:91-94 | Is "các khoản không được thanh toán" item by item or an amount? | (i) amount; (ii) item | **(i)**: the costs claimed are not itemised by payer. |
| F7 | Part I 5.2, src:114-116 | Is 30 days' notice measured inclusively? | (i) a notice exactly 30 days before is valid; (ii) 31 needed | **(i)**, calendar days. |
| F8 | Part I 5.2, 10 | Is the date of early termination itself covered? | (i) no: cover ends at the start of that date; (ii) yes | **(i)**: the remaining period is "tính từ ngày chấm dứt" (counted from the date of termination), so that date is in the remaining period; it is counted, with the end date, in the refund. |
| F9 | Part I 5.2, src:120, 126 | How is "phí bảo hiểm của thời gian còn lại" worked out? | (i) pro rata by days; (ii) a short-period scale | **(i)**: the Rules print no scale. |
| F10 | Part I 5.2, src:119-127 | What is refunded when the limb's condition fails (a claim was paid; the premium not paid in full)? | (i) nothing; (ii) unknown | **(i)**: the clause gives a refund only on its condition and nothing else in the Rules gives one. |
| F11 | Part II "Thời gian chờ", src:480-485 | What is "the date the event arose" for an illness? | onset, diagnosis, first treatment | **input** (`the date the event arose`): the date the medical record gives for the onset; the Rules do not say. |
| F12 | Part I 7, src:153 | When does a one-year term end? | (i) the day before the first anniversary; (ii) on the anniversary | **(i)**: `clause 7 — the term is one year` checks it; a certificate states its own end date in any case. |
| F13 | Part I 11, src:209-210 | Premium on cancellation for dishonesty. | Rules: not refunded. | **Rules followed** (0). LAW: Art. 22(2) (aid lines 543-551) requires the insurer who cancels for intentionally false information to refund the premium less reasonable costs. Not encoded; flagged. |
| F14 | Part II "Số tiền bảo hiểm", "Giới hạn phụ"; A.1.3, B.4.1 | (a) Is "toàn bộ Số tiền bảo hiểm" in A.1 and B.4 the overall sum insured or the benefit's own? (b) Which limits are the sub-limits that may not exceed it? (c) Are the limits per event or per year? | (a) overall / per benefit; (b) all / the medical ones; (c) either | **(a) per benefit** (inputs `sum insured for personal accident`, `... for death from illness`), and the annual cap is applied to the medical-expense benefits only; **(b)** the five medical limits; **(c)** each limit is the amount the schedule allows for the claim in hand. |
| F15 | Part II, src:251-254 | The definition of PARTIAL permanent injury says "Thương tật toàn bộ vĩnh viễn chỉ bao gồm những mục được liệt kê trong Phụ lục". | (i) a slip for partial; (ii) as written, total injury limited to the annex too | **(i)**, finding X7. |
| F16 | Part II "Bệnh có sẵn", src:266-285 | (a) Are the 8 listed diseases pre-existing whenever they arise? (b) Is "trong vòng 3 năm" inclusive? (c) Before which start date? | (a) yes / only if before cover; (b) yes / no; (c) the first certificate of a continuous chain / the current one | **(a) yes** ("ngoài các bệnh có sẵn theo định nghĩa trên", besides the defined ones: a deeming, finding X6); **(b) inclusive**; **(c) the date the benefit's waiting periods run from**. |
| F17 | Part II "Nằm viện", src:349-351 | Does "ít nhất 24 giờ liên tục" qualify day treatment too? | (i) the inpatient limb only; (ii) both | **(i)**: under (ii) day treatment, which ends the same day, could never count, and A.2.3(a)'s carve-out of day treatment would be pointless. Either way an overnight stay under 24 hours is not a hospitalisation (finding X5). |
| F18 | Part II "Phòng tiêu chuẩn", src:390-392 | A patient in a VIP room: is the bed charge capped at the cheapest single room, or not paid? | (i) cap; (ii) nothing | **(i)**: "được giới hạn tới" (is limited to) reads as a cap; LAW: Art. 24. |
| F19 | Part II "Thời gian chờ", src:484-485 | The waiting period "phải được thể hiện trên Hợp đồng / Giấy chứng nhận". If the certificate does not show it? | (i) no waiting period; (ii) the Rules' periods apply anyway | **(i)**, with the certificate's showing an input (`shows the waiting periods of its benefits`): the definition makes showing a condition. |
| F20 | Part II "Đồng chi trả", src:494-500 | Is the percentage applied to the lower of cost and sub-limit, or is the lower of (percentage of cost) and sub-limit taken? | (i) % x min(cost, sub-limit); (ii) min(% x cost, sub-limit) | **(i)**: "theo tỷ lệ phần trăm (%) trên tổng số tiền ... hoặc trên các mức giới hạn phụ ... tùy theo mức nào thấp hơn" puts the percentage on the lower base. (ii) pays more when costs exceed the sub-limit. |
| F21 | Part I 10 vs A.1.4 (iv), src:176-189, 544-548 | A death after the term but within a year of the accident, after a Benefit 2 payment; a death more than a year after; a permanent injury determined after the term. | clause 10 bars consequences after the term; A.1.4 (iv) pays the difference within a year | **A.1.4 (iv) prevails** for a death within the year (the specific rule; Art. 24). A death more than a year after a Benefit 2 payment: nothing (A.1.4 (iv) is the only route). A permanent injury is a consequence that arose with the accident, so clause 10 does not bar its later determination. Finding X1. |
| F22 | Part III waiting periods | When does an N-day waiting period end? | (i) cover from start + N (the start day is day 1); (ii) from start + N + 1 | **(i)**, LAW: Art. 24. Outside knowledge, unverified: the Civil Code's rule that the first day of a period is not counted would support (ii). Both sides of each period are tested. |
| F23 | A.1.4, src:542 | No interest on any amount. | Rules: none. | **Rules followed** (0). LAW: Art. 31(2) (aid lines 725-729) requires interest on a late payment. Finding X8. |
| F24 | A.2.1 src:557-560; B.1.1 src:624-631 | "trừ Bệnh viện công lập nhưng không bao gồm khoa quốc tế tại Bệnh viện công lập" | (i) the public-hospital exception does not extend to its international department (co-payment applies there); (ii) the co-payment does not apply in international departments either | **(i)**: "nhưng" (but) qualifies the exception. |
| F25 | A.2.2, B.1.2 | More than one waiting period describes the illness (a chronic bronchitis in a child of 5). | longest / most specific | **the longest**. |
| F26 | A.2.1, src:553-555 | "phải nằm viện phẫu thuật": hospitalisation AND surgery, or either? A pregnancy hospitalisation under A.2? | either / both; A.2 / B.3 only | **either** (2.3 pays (a) and (b) separately). A pregnancy event is outside A.2's scope (illness or accident); it is claimed under B.3, whose own exclusion item 25 lifts only for B.3. |
| F27 | A.2, B.1, B.2, B.3 amounts | In what order do the co-payment, the sub-limit, another insurer's payment and the annual sum insured apply? | several | % x min(cost, sub-limit) per part; then no more than the costs another contract left unpaid; then no more than the sum insured left in the year. |
| F28 | B.3.2, src:759-761 | Which waiting period for a medically necessary caesarean, listed under "a. Biến chứng thai sản và sinh mổ"? | 60 (complication) / 365 (childbirth) | **365**: a caesarean is a childbirth ("sinh đẻ"); the 60-day line names complications only. Art. 24 would argue 60. |
| F29 | Part IV item 2, src:805-809 | Does the proviso for "những người thụ hưởng hợp pháp khác" save the insured person's own claim where a beneficiary acted? | no / yes | **no**: the Rules name the insured person and the lawful beneficiary as different persons (src:225, 462). LAW: Art. 40(1)(c), (2) (aid lines 823-834) also refuses a permanent injury caused by a beneficiary's intent and saves only other beneficiaries. Finding X11. |
| F30 | item 8, src:828-829 | Does "trừ khi để cứu người, cứu tài sản" qualify suicide too? | danger limb only / both | **danger limb only**. |
| F31 | items 9 (src:831-833) and 33 (src:936-938) | "vi phạm pháp luật và vi phạm quy định an toàn lao động"; "không có giấy phép hoạt động hợp pháp và không cung cấp được chứng từ" | conjunctive / disjunctive | **conjunctive**, as written; Art. 24 points the same way. |
| F32 | item 22, src:887-889 | The list ends "…". | open / closed | **only the named conditions** are encoded; a similar unnamed condition is not excluded. |
| F33 | item 27, src:911-914 | Does "với điều kiện chi phí ... không lớn hơn chi phí thuốc điều trị" attach to both exceptions or the second? | second only / both | **second only** (the support limb), the nearer antecedent. |
| F34 | Part V 1, src:957-973 | (a) Accident report for every accident or only a traffic accident? (b) "(trường hợp điều trị nội trú)" on the discharge paper too? (c) Payment documents for a lump-sum benefit? | | **(a)** every accident, vehicle papers only when driving; **(b)** both papers for inpatient treatment; **(c)** payment documents only for the benefits that pay costs. |
| F35 | Part V 3 (src:985-988) vs 5 (src:1002-1003) | 6 months or 12 months to claim? | 6 / 12 | **12 months** operative: LAW: Art. 30(1) (aid lines 707-710) fixes one year and does not count force majeure; Art. 24. Clause 3 is encoded alone for the finding (X13). |
| F36 | Part V 4, src:993 | What is a working day? | not defined | **Monday to Friday, not a public holiday**, the holidays an input (no calendar ships with L4). Outside knowledge, unverified, which days Vietnam treats as working days. |
| F37 | Part II "Bệnh đặc biệt", src:287 | "các loại u bướu lành tính bệnh huyết áp" has no comma. | two items (benign tumours; hypertension) / one | **two**: "bệnh huyết áp" is a disease in its own right; 28 rows. |
| F38 | Part I 5.2, src:114-117 | May either party end the contract early for any reason? | Rules: yes, on 30 days' notice. | **Rules followed**. LAW: Art. 26 (aid lines 623-635) lists the cases in which a party may unilaterally terminate; whether the Rules may add an at-will right is a question for the Law and the Civil Code (outside knowledge, unverified). Art. 27(1)(b) (aid lines 646-651) keeps the insurer liable for events before termination. Finding X17. |
| F39 | B.2.1, src:672, 683-688 | Is the 10% emergency cap and "1 lần/năm" (once a year) per claim or per year? | | scaling: per insurance year, with the scalings already paid an input; the 10% cap: per claim (the Rules do not say "a year"). |
| F40 | item 20, src:876-877 | A follow-up test with no discharge before it. "quá 30 ngày" at exactly 30? | | not caught by the follow-up limb; "quá" (more than) is strict, so day 30 is not excluded. |
| F41 | item 17 with B.3.1(a), src:744-746, 861-865 | A therapeutic abortion because of a congenital defect of the FOETUS. | item 17 applies to the foetus's condition / to the insured person's | **the insured person's**: the claim lists the insured person's conditions; B.3.1(a) names this case expressly (finding X19). |

## 4. Findings

Defects in the instrument as written, from a hostile reading as policyholder's and as insurer's lawyer: events between cover and exclusion, contradictions, terms that carry weight undefined, discretion without criteria, illusory cover, deadlines that cannot all be met.
Evidence is an `#ASSERT` in `pvi-health-findings.l4` (all satisfied: they assert the surprising answer) or in a test module, or the words **reading only**.

**X1. Clause 10 and A.1.4 (iv) disagree; and the disagreement favours the family that was already paid.**
src:176-189, 544-548. An accident on 1 November 2026, a certificate ending 31 December 2026, death from the accident on 1 February 2027. Clause 10: no liability for a consequence after the term. A.1.4 (iv): where Benefit 2 has been paid, the difference is paid on death within one year. Taking (iv) as the specific rule (F21), the family that had received 30,000,000 for a partial injury receives 70,000,000 more; the family of a person who died of the same accident on the same date without an earlier partial payment receives nothing.
Evidence: `pvi-health-findings.l4` § X1, four assertions (70,000,000 against 0).

**X2. Part IV item 26 swallows the maternity care that B.3 sells.**
src:717-721, 907, 874-877. B.3.1 covers "chi phí y tế chăm sóc thai sản và sinh đẻ" (the medical costs of maternity care and childbirth). Item 26 excludes "Chăm sóc trước và sau khi sinh" (care before and after childbirth), with no exception for B.3, under a Part that "applies to the main benefits and all supplementary benefits"; item 20 excludes routine antenatal check-ups. What is left of "maternity care" is the complications, the caesarean and the delivery.
Evidence: § X2, a pre-natal care claim under B.3 is refused by item 26.

**X3. Raising the benefits at renewal restarts every waiting period, the main benefit's included.**
src:487-492, 575-583. "Tái tục liên tục" is a new certificate with benefits "thấp hơn hoặc bằng" (lower than or equal to) the old. An insured person with PVI since 2024 who adds a rider in 2026 is not continuously renewed at all, so the 365-day period for a chronic, special or pre-existing disease under A.2, whose terms did not change, runs again from 1 January 2026.
Evidence: § X3 (hypertension on 1 June 2026: refused when upgraded, covered when renewed unchanged); `pvi-health-tests-part3.l4` "continuous renewal".

**X4. Part I 2.2(c), read through item 34 at the time of a claim, refuses every claimant.**
src:79, 940. Item 34 excludes costs for a person "không đủ điều kiện tham gia bảo hiểm"; 2.2(c) refuses a person "đang trong thời gian điều trị bệnh hoặc thương tật". A claimant is under treatment. The encoding reads 2.2 at enrolment (F5); the insurer's reading makes the cover illusory.
Evidence: § X4 (the 2.2 test on a claimant's status answers TRUE).

**X5. An overnight stay of less than 24 hours falls between the benefits.**
src:349-355, 370-372, 587-588, 620-622, 928-929. Admitted at 18:00, discharged at 10:00: inpatient treatment (overnight in a bed), but not a hospitalisation (24 continuous hours), so A.2.3(a) does not pay it; not being a hospitalisation, it is "outpatient treatment" by definition, which item 31 excludes without supplementary benefit 1.
Evidence: § X5 (grounds: the A.2.3 scope and item 31).

**X6. The eight deemed pre-existing diseases are pre-existing whenever they arise.**
src:276-285. Asthma, a herniated disc, a vestibular disorder, joint or spinal degeneration and the rest are "được hiểu là Bệnh có sẵn" besides the defined pre-existing diseases, with no reference to when they arose. Asthma first diagnosed in month 6 of a first certificate waits 365 days, against 30 for an ordinary illness.
Evidence: § X6.

**X7. The definition of partial permanent injury restricts TOTAL permanent injury.**
src:251-254. The sentence "Theo quy định của Quy tắc bảo hiểm này, Thương tật toàn bộ vĩnh viễn chỉ bao gồm những mục được liệt kê trong Phụ lục" sits in the definition of "Thương tật bộ phận vĩnh viễn". As written, a total permanent injury of 81% or more is paid only if the annex (not published) lists it. Read as a slip (F15). **Reading only.**

**X8. No interest on any amount, against the Law.**
src:542. A.1.4 says no amount paid under the Rules bears interest. LAW: Art. 31(2) (aid lines 725-729) requires interest on a late payment. Evidence: § X8 (the encoded interest is 0); the conflict itself is reading only.

**X9. Terms defined and never used; a benefit cited and never stated.**
"Thương tật tạm thời" (src:256), "Chi phí thông lệ và hợp lý" (src:374), "Thai kỳ" (src:423), "Chi phí trước khi nhập viện" (src:413) and "Chi phí điều trị sau khi xuất viện" (src:418) are defined and read by no operative clause; "Lần khám/điều trị" (src:397) only by the schedule. Item 29 excepts a main benefit "Chi phí y tế chăm sóc tại nhà theo chỉ định của bác sĩ" (src:918-919) that Part III does not contain. "Chủ hợp đồng" (src:480) and "STBH" (src:688) are used and never defined. The definition of customary and reasonable costs, in particular, would cap payments, and nothing applies it. **Reading only.**

**X10. Discretion with no criterion.**
PVI may refuse renewal or change terms at renewal (5.3, src:140-142); may end the certificate for any reason on 30 days' notice (5.2, src:114-116); may refuse "một phần hoặc toàn bộ" (part or all) of the money for dishonesty "tùy theo mức độ vi phạm" (src:208-209); and excludes dental care at facilities "trong danh sách từ chối bồi thường của Bảo hiểm PVI" (src:698), a list the document does not publish. Evidence: the permissions are encoded unconditionally (`pvi-health-tests-part1.l4` traces); the refusal list is an input. Otherwise **reading only**.

**X11. Item 2 refuses the insured person injured by a beneficiary.**
src:805-809. The insured person is assaulted by her husband, a named beneficiary, and claims her hospital costs. The proviso saves only "những người thụ hưởng hợp pháp khác"; the Rules distinguish the insured person from a beneficiary (F29). Evidence: § X11.

**X12. Part V has no clause 2.**
src:950, 983. The clauses are numbered 1, 3, 4, 5. Whether a clause was dropped (in the mirror or in the original) cannot be told from the copy. **Reading only.**

**X13. Six months or twelve months to claim.**
src:985-988, 1002-1003. Clause 3: the dossier must be sent within 6 months of the event, after which the right is lost except for force majeure. Clause 5: the time limit to request payment is 12 months from the event. A dossier sent after 8 months is lost under one and in time under the other. Clause 3 also names the "người thừa kế hợp pháp" (lawful heir) as the one who loses the right, where clause 1 and clause 5 say "người thụ hưởng hợp pháp". The encoding takes 12 months (F35; LAW: Art. 30(1) fixes one year).
Evidence: § X13.

**X14. 365-day waiting periods inside a one-year term: illusory first-year cover.**
src:153-154, 573, 644, 761, 782. A chronic, special or pre-existing disease under A.2 and B.1 (hypertension, diabetes, heart disease, haemorrhoids, sinusitis, stroke and the rest of the 28, and the 8 deemed diseases) and childbirth under B.3 wait 365 days; the term is one year. On a first certificate starting 1 January 2026, an event on its last day is still in the waiting period; in a term containing 29 February, cover exists on the last day only. Death from such a disease under B.4 waits 730 days, which no event before the first day of a third consecutive certificate can satisfy. The premium for these benefits in the first year buys nothing for these diseases unless the certificate is continuously renewed (and X3 shows how easily that breaks).
Evidence: § X14 (diabetes and a delivery on 31 December 2026 refused; diabetes on 29 February 2028 covered, on 28 February 2028 refused; 730).

**X15. Emergency dental care after an accident waits 30 days.**
src:683-688, 700-702. B.2 covers emergency care only within 24 hours of an accident, and makes the whole benefit wait 30 days with no exception for accidents (A.2 and B.1 have one). An accident in the first 30 days of the certificate can never be followed by covered emergency dental care. Evidence: § X15.

**X16. The same dental clinic is covered in Da Nang and not in Hanoi.**
src:690-698. In Hanoi and Ho Chi Minh City dental care is covered only at state hospitals and medical centres, private and international hospitals, and facilities with a PVI agreement; elsewhere at any licensed facility that issues proper invoices. A licensed private dental clinic in Hanoi without a PVI agreement is outside the cover. Evidence: § X16; `pvi-health-tests-part3.l4` "Scope — B.2 dental".

**X17. Termination at will cuts off treatment already under way.**
src:114-116, 169-174. PVI may end the certificate for any reason on 30 days' written notice, and on early termination its liability ends at once, including for costs arising after termination of an event that arose while the certificate was in force. An insured person admitted on 29 June 2026 for four nights, under a certificate PVI terminated with effect from 1 July 2026, is paid for two nights of four. LAW: Arts. 26 and 27 (F38).
Evidence: § X17 (6,000,000 of 12,000,000).

**X18. The annex and the schedule are not in the published copy.**
src:252-253, 529-530, 460-466, 601-602; printed page numbers (src:1021-1022). The annex of injury percentages that Benefit 2 pays by, "đính kèm Quy tắc" (attached to the Rules), and the schedule of benefits that sets every sum insured and limit and defines the programmes, are absent. The printed pages run 2 to 23 and then 27; pages 24 to 26 are missing from the mirror, and may have held the annex. Benefit 2 cannot be computed from the document. **Reading only.**

**X19. Item 17 against the maternity benefit's therapeutic abortion.**
src:744-746, 861-865. B.3.1(a) covers a therapeutic abortion "do các bệnh lý di truyền/dị tật bẩm sinh của thai nhi" (because of a genetic disease or congenital defect of the foetus); item 17 excludes treatment of congenital and genetic diseases "và mọi biến chứng, hậu quả liên quan" for every benefit. The insurer can argue the abortion is a consequence of a congenital defect. Read for the insured (F41). **Reading only.**

**X20. Special diseases that the exclusions take back.**
src:287-293, 858-859, 867-868. Alzheimer's disease and "hội chứng mất trí nhớ" (dementia) are special diseases (covered after 365 days), while item 18 excludes mental and behavioural disorders; whether dementia is a mental disorder is a medical classification the Rules do not make (outside knowledge, unverified: international classifications put dementia among mental disorders). "bệnh liên quan đến hệ thống tạo máu" (diseases of the blood-forming system) is a special disease, while item 16 excludes bone marrow failure and leukaemia, which are such diseases. **Reading only**; the encoding treats each named condition as named.

**X21. Item 9 and item 33 read conjunctively leave little.**
src:831-838, 934-938. Item 9 bites only on a breach of the law AND of workplace safety rules, recorded by an authority; a road-traffic offence alone is not caught. Item 33's last limb bites only on a facility that is both unlicensed AND unable to issue invoices. The insurer's disjunctive reading would exclude far more (F31). Evidence: `pvi-health-tests-exclusions.l4`, items 9 and 33 near misses.

**X22. Any illness arising from an announced epidemic.**
src:458, 824-826. Item 7 excludes death, illness or injury arising "trực tiếp hoặc gián tiếp" (directly or indirectly) from an epidemic a central authority has announced, for every benefit. During an announced epidemic, a pneumonia linked to it is excluded however it was treated. Evidence: § X22.

## 5. Answer table

Waiting periods, in days from the date the benefit was first taken up (continuous renewal keeps the first date):

| benefit | accident | ordinary illness | child 15 days-6 years with bronchitis, bronchiolitis, pneumonia | chronic, special or pre-existing disease | maternity complication | childbirth (caesarean included) | src |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A.1 personal accident | 0 | — | — | — | — | — | 514-515 |
| A.2 inpatient | 0 | 30 | 180 | 365 | — | — | 562-573 |
| B.1 outpatient | 0 | 30 | 180 | 365 | — | — | 633-644 |
| B.2 dental | 30 | 30 | 30 | 30 | — | — | 700-702 |
| B.3 maternity | — | — | — | — | 60 | 365 | 755-761 |
| B.4 death from illness | — | 30 | 30 | 730 | — | — | 776-782 |

Ages and limits the document states: insured from 15 days to 60, to 65 if continuously insured since 60 (2.1); under 18 only with a parent; under 1 only on programme 1 or 2; 130% loading for 61-65 and under 1; not accepted with a disability of 50% or more (2.2); co-payment 30/70 under 10 outside public hospitals; maternity for women 18 to 45 on programme 1 or 2; total permanent injury from 81%; 60 hospital days a year; scaling once a year; dental emergency within 24 hours, up to 10% of the dental sum insured; refund 80% / 100% of the remaining premium; notice 30 days; claim 6 or 12 months; payment 15 working days; suit 3 years.

## 6. What `check.sh` prints

Run on 2026-10-07, 01:27-01:31 SGT, with the binary in section 0 (`L4=/Users/mengwong/.local/bin/l4 ./check.sh`):

```
module                                    errors satisfied  failed  refused  expected
pvi-health-assessment.l4                       0         0       0        0         0
pvi-health-findings.l4                         0        27       0        0         0
pvi-health-fixtures.l4                         0         0       0        0         0
pvi-health-nouns.l4                            0         0       0        0         0
pvi-health-part1-general.l4                    0         0       0        0         0
pvi-health-part2-definitions.l4                0         0       0        0         0
pvi-health-part3-benefits.l4                   0         0       0        0         0
pvi-health-part4-exclusions.l4                 0         0       0        0         0
pvi-health-part5-claims.l4                     0         0       0        0         0
pvi-health-tests-exclusions.l4                 0        92       0        0         0
pvi-health-tests-part1.l4                      0        57       0        0         0
pvi-health-tests-part2.l4                      0        72       0        0         0
pvi-health-tests-part3.l4                      0       101       0        0         0
pvi-health-tests-part5.l4                      0        18       0        0         0
TOTAL (14 modules)                             0       367       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

- `check.sh` exit status 0, from a second complete run (01:31-01:35 SGT) that printed the same table.
- The 367 satisfied assertions are every `#ASSERT` in the six modules that carry them (findings 27, tests-exclusions 92, tests-part1 57, tests-part2 72, tests-part3 101, tests-part5 18; counted with `grep -c '^#ASSERT'`). No assertion fails or refuses, and none is expected to: `expected_failed` is 0 for every module and encoding.json names no `expected_red`.
- The rule modules, the nouns and the fixtures carry no assertions.
- The six `#TRACE` directives are not counted by `check.sh`; their results, read from the run output: the two Part I permissions exercised, FULFILLED; the claimant who sends the dossier on day 100, FULFILLED, and who sends nothing by day 366, BREACH BY `the insured person` with the clause 5 reason; PVI paying on day 21, FULFILLED, and paying nothing by day 22, BREACH BY PVI with the clause 4 reason.
- `pvi-health-findings.l4` passing does not mean the findings are resolved: its assertions state the surprising answers of section 4.
- History, because a failing assertion is a finding and no expected value was edited: during development the Part IV tests failed twice (items 9, a 13- and a 14-year-old), because the fact pattern put a minor on a contract without a parent, which also engaged item 34; the fixture was moved onto a parent's contract and the expected item lists were left as they were. One Part III assertion (an event before the term) failed because the clause 10 ground also fired for a cost BEFORE the start date, which clause 10 does not say; the rule was narrowed to costs after the last day of liability and the expected value was left as it was. Two earlier full runs of `check.sh` on this machine were killed by the environment part-way (exit 144) while the machine's load average was above 200; the run above is complete.

## 7. The quote check

The gate is the brief's command over every `.l4` and every `.md` in this directory except BRIEF.md (the lead's file), run from this directory after this file was completed:

```
vnsrc check: 842 src: lines, 733 Vietnamese runs, 0 problems
```

The literal command of the brief, `python3 -I tools/vnsrc.py check ../../source/raw/pvi-health.txt *.l4 *.md`, also reads BRIEF.md and reports one problem there, at BRIEF.md line 31: the first word of the sibling PTI product's name, which is not in this source. Its last line:

```
vnsrc check: 842 src: lines, 746 Vietnamese runs, 1 problems
```

## 8. Open questions for a domain expert

1. Which of Part V clause 3 (6 months) and clause 5 (12 months) does PVI apply, and does Art. 30 of the Law settle it?
2. Is the at-will early termination in Part I 5.2 valid against Art. 26 of the Law, and does Art. 27(1)(b) keep PVI liable for the rest of a hospital stay that began before termination?
3. Is the 365-day waiting period counted so that day 365 is covered (F22), and does PVI regard first-year cover for the special diseases and for childbirth as available at all?
4. Does a certificate that does not print the waiting periods carry them (F19)?
5. What does the annex of injury percentages say, and are printed pages 24 to 26 that annex?
6. Is the sentence in the definition of partial permanent injury that names "toàn bộ" a slip (F15)?
7. Does item 26 apply to a policyholder who bought B.3 (X2)? Does item 17 apply to a therapeutic abortion for a foetal defect (X19)?
8. Does item 2's proviso protect the insured person's own claim (F29, X11)?
9. Is Alzheimer's disease or dementia excluded by item 18 despite being a special disease (X20)?
10. How are the "other benefits" of A.2.3(c), the pre-admission and post-discharge costs and home medical care limited in the schedules in use?
11. Is a working day Monday to Friday for PVI, and which holidays count (F36)?
12. Does Art. 31(2) of the Law (interest on late payment) override A.1.4's "no interest" (X8), and Art. 22(2) the no-refund rule of Part I 11 (F13)?
