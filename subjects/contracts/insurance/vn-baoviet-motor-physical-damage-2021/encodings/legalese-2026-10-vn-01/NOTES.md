# NOTES — vn-baoviet-motor-physical-damage-2021, encoding row `legalese-2026-10-vn-01`

Bao Viet's motor vehicle physical damage insurance rules (Quy tắc bảo hiểm vật chất xe ô tô), issued with Decision 5688/QĐ-BHBV of 9 December 2021, encoded whole in L4 by one agent (`enc-vn-01`, run `VN-01-20261006`, 2026-10-06 to 07) from `BRIEF.md`.
Status: **draft**.
No domain expert has read it against the source; HG1 has not been sought; no independent test pass has been run.

## 0. Build and run

- `l4`: `/Users/mengwong/.local/bin/l4`, a symlink to `~/.cabal/bin/l4`, the cabal store build `jl4-0.1-0ee0100b`, modified 2026-10-06 21:20, sha256 `64bbcb157dbef2ef1020a6a75589313bba0a2aeeb807c921c5e65e62e9eca118`. It has no `--version`; no record beside it names its commit. `JL4_LIBRARY_PATH` unset.
- Command, from this directory: `L4=/Users/mengwong/.local/bin/l4 ./check.sh`.
- Every run prints two Warnings that differing copies of `prelude` and `daydate` exist under `~/.local/share/jl4/libraries/`; the binary uses its embedded copies. They are not errors.
- The runs were slow: the machine carried a load average near 200 while a dozen encoders ran `l4` at once, and a tests module took up to ~10 minutes of wall time.

What `check.sh` printed, verbatim (check.sh exit 0):

```
module                                    errors satisfied  failed  refused  expected
bvvcx-claim.l4                                 0         0       0        0         0
bvvcx-nouns.l4                                 0         0       0        0         0
bvvcx-p1-definitions.l4                        0         0       0        0         0
bvvcx-p2-claims.l4                             0         0       0        0         0
bvvcx-p2-contract.l4                           0         0       0        0         0
bvvcx-p2-duties.l4                             0         0       0        0         0
bvvcx-p3-cover.l4                              0         0       0        0         0
bvvcx-p3-settlement.l4                         0         0       0        0         0
bvvcx-p4-supplementary.l4                      0         0       0        0         0
bvvcx-tests-contract.l4                        0        74       0        0         0
bvvcx-tests-cover.l4                           0        74       0        0         0
bvvcx-tests-findings.l4                        0        20       0        0         0
bvvcx-tests-fixtures.l4                        0         0       0        0         0
bvvcx-tests-generated.l4                       0        54       0        0         0
bvvcx-tests-limits.l4                          0         5       0        0         0
bvvcx-tests-settlement.l4                      0        80       0        0         0
TOTAL (16 modules)                             0       307       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

**Generated files.** The `.l4` modules are expanded from templates kept in the session scratchpad (`scratchpad/enc-vn-01/tmpl/`): every `-- src:N | …` line is printed by `tools/vnsrc.py quote` from a `-- @@SRC N M` marker, never typed (script `expand-vn01.py`). `bvvcx-tests-generated.l4` is written by `gen-tests-vn01.py`, which reads each printed figure off the raw text with a regular expression and the Vietnamese number format (a dot groups thousands, a comma is the decimal point), and computes deadline dates with Python's `datetime`, not with the L4 library. The coverage table below is cut from the raw text by `gen-coverage-vn01.py`. The scripts live in the scratchpad, not here; the deposited files stand on their own.

**A process incident, recorded because the rows are meant to be blind to one another.** The session scratchpad turned out to be shared by all the encoders. My first expander read the shared `scratchpad/tmpl/`, found there VN-08's template `baominh-par-nouns.l4` (Bao Minh property all risks), and wrote an expanded copy of it into this deposit. I saw its first five lines (the header naming VN-08), deleted it from this deposit, and moved all my work to `scratchpad/enc-vn-01/`. My nouns module had already been written before that, and no name or structure from that file entered this encoding. I also overwrote, once, another encoder's root-level `scratchpad/expand.py` before I knew the directory was shared; its owner rewrote it. I reported both to the lead at the time.

## 1. What is encoded and what is not

**Encoded, the whole document**: the important notice; Part I (all 14 definitions, as rules where they decide something and as nouns where they name something); Part II, Articles 1-9 (the contract and its documents, the period and the premium conditions, every way the contract ends and every refund, the insurer's and the purchaser's rights and duties as regulative rules and date functions, the assessment, the claim file, double insurance, the time limits and the forum); Part III, Articles 10-15 (the heads of cover and the 10.2 costs, all 17 exclusions, the sum insured and value, partial and total loss with the depreciation table, salvage, the order of deductions, the deductible, all reductions); Part IV, Articles 16-23 (BVVC01-BVVC07 as changes to the Part III rules, and Article 23 declined by name).

Three layers, as the brief asks: **cover** (`bvvcx-claim.l4` `the cover decision for`), **amount** (`the settlement of`, `the amount payable on`), **duties and deadlines** (the regulative rules and date functions of Articles 3-6, 9 and 19).

**Inputs, never defaults.** Everything the Rules leave to the certificate is a field of `The policy` with no default: the period, the sum insured, the deductible (14.3's 500,000 applies only where the certificate states none), the supplementary clauses, the car-hire sums, the premium arrangements. Market values, repair costs, the insurer's 15.1.3 rate and its wreck valuation are inputs; a rule that needs a missing one declines by name.

**Declined by name (`REFUSE`)**: a certificate carrying an Article 23 clause; a certificate that sets its own reduction rates (4.1.6) where a reduction applies; a sum insured above the value (12.1); a 15.1.3 ground with no rate fixed, or a rate outside 0-100%; a 15.1.5 ground with no premium due recorded; a kept wreck with no valuation; a missing 12.3 value; BVVC05 without its sums; 4.2.3 when the authority has not concluded (the Rules set no time); 9.2 and 9.3 without their start dates; a negative time in use.

**Not encoded**: the Law on Insurance Business (read only, for `LAW:` forks); the TCVN vehicle standard (whether a kind is listed is the caller's input); Vietnam's public holidays (an input list); the Civil Code's rule for counting periods (assumed, labelled as outside knowledge). The cap in Article 8's chapeau on what ALL insurers together pay is not computed, because the encoding computes only this insurer's share.

## 2. Coverage table

Each heading is cut from the raw text by script (the first words of the line after its number).

| provision | src | heading or opening words as written | English gloss | disposition | where in the L4 |
| --- | --- | --- | --- | --- | --- |
| title | 1 | QUY TẮC BẢO HIỂM VẬT CHẤT XE Ô TÔ | Motor vehicle physical damage insurance rules (Decision 5688/QĐ-BHBV) | inert | comment, bvvcx-p2-contract.l4 |
| notice | 7 | LƯU Ý QUAN TRỌNG | Important notice: signing the request is evidence of understanding | encoded | bvvcx-p2-contract.l4 `the notice — …` |
| contents | 15 | MỤC LỤC | Table of contents | inert | comment, bvvcx-p2-contract.l4 |
| Part I | 48 | PHẦN I: GIẢI THÍCH TỪ NGỮ | Definitions (the bold terms) | inert | bvvcx-p1-definitions.l4 |
| def 1 | 50 | “BẢO VIỆT” | the insurer | inert | `A party`; bvvcx-p1-definitions.l4 |
| def 2 | 52 | “Bên mua bảo hiểm” | the purchaser: owner or lawful holder, who concluded and paid | encoded | bvvcx-p1-definitions.l4 `a purchaser within definition 2` |
| def 3 | 56 | “Cháy” | fire: chemical combustion with heat and light | encoded | bvvcx-p1-definitions.l4 `a fire within definition 3` |
| def 4 | 58 | “Giá thị trường” | market value: price of a like vehicle offered at the time | inert | input; bvvcx-p1-definitions.l4 comment (fork F2) |
| def 5 | 61 | “Giấy chứng nhận kiểm định” | inspection certificate | inert | noun; bvvcx-p1-definitions.l4 |
| def 6 | 63 | “Giấy yêu cầu bảo hiểm” | request form, paper or electronic; OTP equals a signature | encoded | bvvcx-p1-definitions.l4 `the request counts as signed …` |
| def 7 | 69 | “Hợp đồng bảo hiểm” | insurance contract: see Article 1 | inert | bvvcx-p1-definitions.l4 comment |
| def 8 | 71 | “Người điều khiển xe” | the driver: drives with the purchaser's or the insured's consent | encoded | bvvcx-p1-definitions.l4 `the driver within definition 8` |
| def 9 | 73 | “Người được bảo hiểm” | the insured: named on the certificate | inert | `The claimant`; bvvcx-p1-definitions.l4 |
| def 10 | 75 | “Nổ” | explosion, not a physical (pressure) explosion | encoded | bvvcx-p1-definitions.l4 `an explosion within definition 10` |
| def 11 | 78 | “Phí bảo hiểm” | premium | inert | `The premium arrangements` |
| def 12 | 80 | “Thời gian sử dụng xe” | time in use, in months, from first registration (or June of the year made) | encoded | bvvcx-p1-definitions.l4 `the time in use, in months, …` |
| def 13 | 84 | “Trọng tải” | load, per the inspection certificate | inert | `permitted load`; bvvcx-p1-definitions.l4 |
| def 14 | 92 | “Xe ô tô/Xe” | car: self-propelled road vehicle, not a motorcycle, moped, e-bike | encoded | bvvcx-p1-definitions.l4 `a car within definition 14` |
| Part II | 97 | PHẦN II: QUY ĐỊNH CHUNG | General provisions | inert | bvvcx-p2-contract.l4 |
| Art 1 chapeau | 98 | Hợp đồng bảo hiểm | the insurance contract and its documents | encoded | bvvcx-p2-contract.l4 `Article 1 — the documents …` |
| 1.1 | 103 | Giấy yêu cầu bảo hiểm | request form; unsigned but paid is agreement | encoded | bvvcx-p2-contract.l4 `1.1 — the requester is taken to agree …` |
| 1.2-1.5 | 109 | Quy tắc bảo hiểm này | these Rules; certificate; other agreements; amendments | encoded | bvvcx-p2-contract.l4 `Article 1 — the documents …` |
| Art 2 heading | 117 | Thời hạn bảo hiểm và quy định về thanh | period of insurance and premium payment | inert | bvvcx-p2-contract.l4 |
| 2.1 | 118 | Thời hạn bảo hiểm | period stated on the certificate | encoded | bvvcx-p2-contract.l4 `2.1 — within the period of insurance` |
| 2.2 | 120 | Hợp đồng bảo hiểm chỉ có | in effect only once the premium is paid, unless a time is agreed in writing | encoded | bvvcx-p2-contract.l4 `2.2 — the premium condition is met on` |
| 2.3 | 123 | Trường hợp Bên mua bảo hiểm | unpaid with no agreement: the contract ends | encoded | bvvcx-p2-contract.l4 `3.1.1 — the date the contract ends …` |
| 2.4 | 126 | Trong Thời hạn bảo hiểm, trường | transfer of ownership: runs for the new owner | encoded | bvvcx-p2-contract.l4 `2.4 — the standing on …` |
| Art 3 chapeau | 131 | Hợp đồng bảo hiểm chấm dứt | the contract ends in these cases | inert | bvvcx-p2-contract.l4 |
| 3.1 | 132 | Chấm dứt Hợp đồng bảo hiểm | end for late payment | inert | heading; bvvcx-p2-contract.l4 |
| 3.1.1 | 137 | Hợp đồng bảo hiểm sẽ chấm | ends the day after the due date | encoded | bvvcx-p2-contract.l4 `3.1.1 — the date the contract ends …` |
| 3.1.2 | 142 | Bên mua bảo hiểm phải có | within 5 days refund or ask for premium; no refund once liability arises | encoded | bvvcx-p2-contract.l4 `3.1.2 — …` |
| 3.1.3 | 149 | Hợp đồng bảo hiểm tiếp tục | continues on payment and written acceptance | encoded | bvvcx-p2-contract.l4 `3.1.3 — …` |
| 3.2 | 152 | Đơn phương chấm dứt thực hiện | unilateral termination | inert | heading; bvvcx-p2-contract.l4 |
| 3.2.1 | 153 | Trong thời hạn bảo hiểm, một | either party, by written notice; on the notice date if none stated | encoded | bvvcx-p2-contract.l4 `3.2.1 — the date the contract ends under` |
| 3.2.2 | 159 | Trường hợp Bên mua bảo hiểm | purchaser ends: 70% of the rest, within 15 days | encoded | bvvcx-p2-contract.l4 `3.2.2 — …` |
| 3.2.3 | 167 | Đối với Hợp đồng bảo hiểm | group contracts: vehicle by vehicle | encoded | bvvcx-p2-contract.l4 `3.2.3 — …` |
| 3.2.4 | 170 | Trường hợp BẢO VIỆT đơn phương | insurer ends: 100% of the rest, within 15 days | encoded | bvvcx-p2-contract.l4 `3.2.4 — …` |
| Art 4 heading | 175 | Quyền và nghĩa vụ của BẢO | the insurer's rights and duties | inert | bvvcx-p2-duties.l4 |
| 4.1.1 | 177 | Thu Phí bảo hiểm theo | collect the premium | inert | bvvcx-p2-duties.l4 comment |
| 4.1.2 | 178 | Kiểm tra, đánh giá tình | inspect the vehicle; ask for information | inert | bvvcx-p2-duties.l4 comment |
| 4.1.3 | 183 | Từ chối bồi thường cho | refuse claims outside cover or excluded | encoded | bvvcx-claim.l4 `the cover decision for` |
| 4.1.4 | 186 | Yêu cầu Bên mua bảo | require loss prevention | inert | bvvcx-p2-duties.l4 comment |
| 4.1.5 | 189 | Yêu cầu người thứ ba | recover from third parties | inert | bvvcx-p2-duties.l4 comment; consequence in 15.1.3(a) |
| 4.1.6 | 192 | Giảm trừ số tiền bồi | reduce compensation for breaches of 5.2, at rates in the Rules or the certificate | encoded | bvvcx-claim.l4 `the reduction rate for` (certificate rates declined) |
| 4.1.7 | 196 | Các quyền khác theo quy | other rights under law | inert | bvvcx-p2-duties.l4 comment |
| 4.2.1-4.2.2 | 198 | Giải thích cho Bên mua | explain the terms; issue the certificate | inert | bvvcx-p2-duties.l4 comment |
| 4.2.3 | 202 | Trả tiền bồi thường bảo hiểm | pay within 15 days (30 with verification); 90-day rule | encoded | bvvcx-p2-duties.l4 `4.2.3 — …` (no-time case refused: X7) |
| 4.2.4 | 213 | Trường hợp từ chối bồi thường | written refusal with reasons within 15 days | encoded | bvvcx-p2-duties.l4 `4.2.4 — …` |
| 4.2.5 | 216 | Đối với những vụ tai nạn | advance on serious accidents (may) | encoded | bvvcx-p2-duties.l4 `4.2.5 — …` (MAY) |
| 4.2.6 | 220 | BẢO VIỆT có trách nhiệm hướng | guide the claimant on the file | inert | bvvcx-p2-duties.l4 comment |
| 4.2.7 | 223 | BẢO VIỆT có trách nhiệm đánh | re-rate within 5 working days; pro-rata adjustment | encoded | bvvcx-p2-duties.l4 `4.2.7 — …` |
| 4.2.8 | 231 | Các nghĩa vụ khác theo | other duties under law | inert | bvvcx-p2-duties.l4 comment |
| Art 5 heading | 232 | Quyền và nghĩa vụ của Bên | the purchaser's and the insured's rights and duties | inert | bvvcx-p2-duties.l4 |
| 5.1.1-5.1.4 | 234 | Yêu cầu BẢO VIỆT giải | rights: explanation, claim, assignment, others | inert | bvvcx-p2-duties.l4 comment |
| 5.2.1 | 242 | Đóng Phí bảo hiểm đầy | pay the premium | inert | enforced by bvvcx-p2-contract.l4 (Arts 2-3) |
| 5.2.2 | 244 | Khi yêu cầu bảo hiểm | declare fully and honestly | inert | enforced by 15.1.5(a) |
| 5.2.3 | 246 | Tạo điều kiện thuận lợi | let the insurer inspect the vehicle | inert | bvvcx-p2-duties.l4 comment |
| 5.2.4 | 248 | Trường hợp thay đổi mức độ | notify a change in risk within 15 working days; (a) and (b) | encoded | bvvcx-p2-duties.l4 `5.2.4 — …`, `5.2.4(a) — …`, `5.2.4(b) — …` |
| 5.2.5 | 268 | Tuân thủ các quy định | obey road safety rules | inert | bvvcx-p2-duties.l4 comment |
| 5.2.6 | 274 | Khi xảy ra thiệt hại, Bên | on damage: notify at once; do not move or repair; written notice in 5 days | encoded | bvvcx-p2-duties.l4 `5.2.6(a)`, `5.2.6(c)`; 15.1.1-15.1.2 |
| 5.2.7 | 288 | Bên mua bảo hiểm, Người được | be honest in the claim file | encoded | bvvcx-p3-settlement.l4 15.1.3(b)-(c) |
| 5.2.8 | 292 | Trường hợp thiệt hại xảy ra | preserve and transfer rights against third parties | encoded | bvvcx-p3-settlement.l4 15.1.3(a) |
| 5.2.9 | 298 | Đối với các thiệt hại dẫn | hand over replaced parts | encoded | bvvcx-p2-duties.l4 `5.2.9 — …` |
| 5.2.10 | 301 | Khi xe ô tô bị mất | theft of the vehicle: notify police and insurer within 24 hours | encoded | bvvcx-p2-duties.l4 `5.2.10 — …` |
| 5.2.11 | 305 | Các nghĩa vụ khác theo | other duties under law | inert | bvvcx-p2-duties.l4 comment |
| Art 6 heading | 306 | Giám định thiệt hại | assessment of the damage | inert | bvvcx-p2-duties.l4 |
| 6.1 | 307 | Khi xảy ra tai nạn, BẢO | the insurer assesses and bears the cost | inert | bvvcx-p2-duties.l4 comment; cost used in 6.3 |
| 6.2 | 313 | Trường hợp các bên không thống | independent assessor; courts that may appoint | encoded | bvvcx-p2-duties.l4 `6.2 — …` |
| 6.3 | 322 | Trường hợp kết luận của giám | who pays the independent assessor | encoded | bvvcx-p2-duties.l4 `6.3 — …` |
| 6.4 | 326 | Trong trường hợp đặc biệt, BẢO | special cases: the insurer guides the insured | inert | bvvcx-p2-duties.l4 comment |
| Art 7 | 331 | Hồ sơ bồi thường | the claim file | encoded | bvvcx-p2-claims.l4 `Article 7 — the documents …` |
| 7.1.1-7.1.6 | 334 | Tài liệu do Bên mua bảo | documents from the purchaser and the insured | encoded | bvvcx-p2-claims.l4 `A claim document` |
| 7.2.1-7.2.3 | 364 | Tài liệu do BẢO VIỆT phối | documents gathered with the insurer | encoded | bvvcx-p2-claims.l4 |
| 7.3 | 378 | Các tài liệu khác có liên | other relevant documents | encoded | bvvcx-p2-claims.l4 |
| 7.4.1-7.4.4 | 379 | Trường hợp xe bị mất trộm | theft of the whole vehicle: police documents | encoded | bvvcx-p2-claims.l4 |
| Art 8 chapeau | 390 | Hợp đồng bảo hiểm trùng là | double insurance; total not above the actual loss | encoded | bvvcx-p2-claims.l4 (the across-insurer cap is about other insurers' payments and is not computed) |
| 8.1 | 394 | Đối với những điều kiện bảo | overlapping conditions: pro rata by sum insured | encoded | bvvcx-p2-claims.l4 `8.1 — …` |
| 8.2 | 398 | Đối với những điều kiện bảo | different conditions: each under its own contract | encoded | bvvcx-p2-claims.l4 `8.1 — …` (share 1) |
| 9.1 | 407 | Thời hạn yêu cầu bồi thường | claim within 1 year of the event | encoded | bvvcx-p2-claims.l4 `9.1 — …` |
| 9.2 | 411 | Thời hạn khiếu nại về quyết | complaint within 90 days of the settlement notice | encoded | bvvcx-p2-claims.l4 `9.2 — …` |
| 9.3 | 417 | Thời hiệu khởi kiện về Hợp | suit within 3 years of the dispute | encoded | bvvcx-p2-claims.l4 `9.3 — …` (no date: refused) |
| 9.4 | 419 | Mọi tranh chấp phát sinh từ | negotiation, then arbitration or a court in Vietnam | encoded | bvvcx-p2-claims.l4 `9.4 — …` |
| Part III | 422 | PHẦN III: QUY ĐỊNH CỤ | Specific provisions | inert | bvvcx-p3-cover.l4 |
| 10.1 chapeau | 424 | BẢO VIỆT chịu trách nhiệm bồi | material damage from sudden accidents and natural disasters, in these cases | encoded | bvvcx-p3-cover.l4 `10.1 — the head of cover for the event` |
| 10.1.1 | 427 | Đâm va, lật, đổ, lệch trọng | collision, overturning, toppling, sinking, falling, struck from outside | encoded | bvvcx-p3-cover.l4 |
| 10.1.2 | 429 | Hỏa hoạn, cháy | conflagration, fire, explosion | encoded | bvvcx-p3-cover.l4 |
| 10.1.3 | 430 | Những tai họa bất khả kháng | natural catastrophes | encoded | bvvcx-p3-cover.l4 |
| 10.1.4 | 431 | Mất toàn bộ xe do trộm | loss of the whole vehicle by theft or robbery | encoded | bvvcx-p3-cover.l4 |
| 10.2 | 432 | Ngoài số tiền bồi thường, BẢO | costs at the insurer's request, on top | encoded | bvvcx-p3-cover.l4 `10.2 — the expenses payable …` |
| 10.2.1-10.2.2 | 435 | Chi phí ngăn ngừa hạn chế | preventing further damage; rescue and towing, at most 10% of the sum insured | encoded | bvvcx-p3-cover.l4 |
| 10 closing | 438 | BẢO VIỆT không chịu trách nhiệm | nothing outside 10.1 | encoded | bvvcx-claim.l4 `outside the cover of Article 10` |
| Art 11 chapeau | 441 | BẢO VIỆT không bồi thường thiệt | exclusions | encoded | bvvcx-p3-cover.l4 `An exclusion of Article 11` |
| 11.1 | 442 | Hành động cố ý gây thiệt | deliberate damage | encoded | bvvcx-p3-cover.l4 `11.1 — …` |
| 11.2 | 449 | Tại thời điểm xe ô tô | no valid inspection certificate (new-vehicle grace 30 days) | encoded | bvvcx-p3-cover.l4 `11.2 — …` |
| 11.3 | 452 | Người điều khiển xe không có | no proper licence | encoded | bvvcx-p3-cover.l4 `11.3 — …` |
| 11.4 | 459 | Người điều khiển xe lái xe | alcohol over 50 mg/100 ml or 0.25 mg/l; drugs | encoded | bvvcx-p3-cover.l4 `11.4 — …` |
| 11.5 | 462 | Điều khiển xe vào đường ngược | wrong way, prohibited turn, signals, no lights | encoded | bvvcx-p3-cover.l4 `11.5 — …` |
| 11.6 | 467 | Đua xe (hợp pháp hoặc | racing; unlawful towing | encoded | bvvcx-p3-cover.l4 `11.6 — …` |
| 11.7 | 469 | Chở hàng hóa nguy hiểm không | dangerous goods without permit | encoded | bvvcx-p3-cover.l4 `11.7 — …` |
| 11.8 | 471 | Thiệt hại xảy ra ngoài | outside Vietnam | encoded | bvvcx-p3-cover.l4 `11.8 — …` |
| 11.9 | 472 | Thiệt hại xảy ra trong những | war, terrorism | encoded | bvvcx-p3-cover.l4 `11.9 — …` |
| 11.10 | 473 | Thiệt hại do hao mòn tự | wear, inherent nature, loss of value, defect, repair | encoded | bvvcx-p3-cover.l4 `11.10 — …` |
| 11.11 | 476 | Thiệt hại xảy ra đối với | electrical equipment: overload, short circuit | encoded | bvvcx-p3-cover.l4 `11.11 — …` |
| 11.12 | 479 | Thiệt hại hệ thống điện, động | engine and electrical system while operating in flood | encoded | bvvcx-p3-cover.l4 `11.12 — …` |
| 11.13 | 481 | Thiệt hại đối với săm lốp | tyres, tarpaulins, labels damaged alone | encoded | bvvcx-p3-cover.l4 `11.13 — …` |
| 11.14 | 484 | Mất bộ phận của xe do | theft of parts | encoded | bvvcx-p3-cover.l4 `11.14 — …` |
| 11.15 | 485 | Mất toàn bộ xe trong trường | whole vehicle lost by fraud or breach of trust | encoded | bvvcx-p3-cover.l4 `11.15 — …` |
| 11.16 | 487 | Xe chở/kéo theo quá trọng tải | overloading by 50% or more | encoded | bvvcx-p3-cover.l4 `11.16 — …` |
| 11.17 | 496 | Thiệt hại đối với các thiết | added equipment | encoded | bvvcx-p3-cover.l4 `11.17 — …` |
| Art 12 heading | 501 | Số tiền bảo hiểm và giá | sum insured and value | inert | bvvcx-p3-settlement.l4 |
| 12.1 | 502 | Số tiền bảo hiểm là số | sum insured, not above market value at conclusion | encoded | bvvcx-p3-settlement.l4 `12.2 — insured below value` (above: refused) |
| 12.2 | 506 | Bên mua bảo hiểm có thể | may insure at or below value | encoded | bvvcx-p3-settlement.l4 `12.2 — insured below value` |
| 12.3 | 508 | BẢO VIỆT xác định giá trị | how the insurer values the vehicle | encoded | bvvcx-p3-settlement.l4 `12.3 — the value of` |
| 12.3.1 | 509 | Đối với xe mới một trăm | new: published or import price with taxes | encoded | bvvcx-p3-settlement.l4 |
| 12.3.2 | 512 | Đối với xe đã qua sử | used: market value at conclusion | encoded | bvvcx-p3-settlement.l4 |
| 12.4 | 514 | Trong mọi trường hợp số tiền | never above the sum insured | encoded | bvvcx-p3-settlement.l4 `12.4 — …` |
| 13.1.1 | 517 | BẢO VIỆT chịu trách nhiệm thanh | partial loss: reasonable repair or replacement; cash; repairer paid | encoded | bvvcx-p3-settlement.l4 `13.1 — the reasonable cost of`, `13.1.1 — who is paid …` |
| 13.1.2(a) | 526 | a) Trường hợp xe được bảo | below value: pro rata | encoded | bvvcx-p3-settlement.l4 `13.1.2(a) — …`; bvvcx-claim.l4 |
| 13.1.2(b) | 529 | b) Trường hợp xe được bảo | at value: reasonable cost; depreciation on new parts | encoded | bvvcx-p3-settlement.l4 `13.1.2(b) — the depreciation scale` |
| 13.1.2(b) table | 534 | Xe sử dụng dưới ba (03) | depreciation 0/15/25/35/50% by years in use | encoded | bvvcx-p3-settlement.l4 (5 rows; generated tests) |
| 13.1.3 | 547 | BẢO VIỆT bồi thường chi phí | whole-vehicle repaint if over 50% damaged | encoded | bvvcx-p3-settlement.l4 `13.1.3 — …` |
| 13.2.1 | 551 | BẢO VIỆT bồi thường thiệt hại | total loss: cost over 75% of market value; theft with police suspension | encoded | bvvcx-p3-settlement.l4 `13.2.1(a)`, `13.2.1(b)` |
| 13.2.2 | 557 | Số tiền bồi thường thiệt hại | total loss: market value at the loss, capped by the sum insured | encoded | bvvcx-p3-settlement.l4 `13.2.2 — …` |
| 13.3 | 560 | Thu hồi tài sản sau bồi | recovery after payment | inert | heading; bvvcx-p3-settlement.l4 |
| 13.3.1 | 563 | Đối với trường hợp bồi thường | replaced parts to the insurer | encoded | bvvcx-p3-settlement.l4 `13.3.1 — …` |
| 13.3.2 | 566 | Đối với trường hợp bồi thường | wreck to the insurer; kept wreck deducted | encoded | bvvcx-p3-settlement.l4 `13.3.2 — …` |
| 13.3.3 | 572 | Đối với trường hợp bồi thường | stolen vehicle found: the insurer owns it | encoded | bvvcx-p3-settlement.l4 `13.3.3 — …` |
| 13.4 | 574 | Nguyên tắc áp dụng giảm trừ | order: clause deductible, reduction, general deductible | encoded | bvvcx-p3-settlement.l4 `13.4 — …`; bvvcx-claim.l4 |
| 14.1 | 584 | Mức khấu trừ là số tiền | deductible per partial loss, on the certificate | encoded | bvvcx-p3-settlement.l4 `14 — the deductible …` |
| 14.2 | 587 | Khi xảy ra thiệt hại thuộc | at or below the deductible nothing; above, the excess | encoded | bvvcx-p3-settlement.l4 `14.2 — …` |
| 14.3 | 593 | BẢO VIỆT áp dụng Mức khấu | minimum 500,000 VND per loss | encoded | bvvcx-p3-settlement.l4 `14.3 — …` |
| 15.1 chapeau | 597 | BẢO VIỆT thực hiện giảm mức | reductions by a rate | encoded | bvvcx-p3-settlement.l4 `15.1 — the reductions …` |
| 15.1.1 | 599 | Giảm mười phần trăm (10%) số | 10%: late notice, no mitigation, scene, parking or lane offence | encoded | bvvcx-p3-settlement.l4 `15.1.1 — …` |
| 15.1.2 | 616 | Giảm 25% số tiền bồi thường | 25%: repair without consent; speed 20% over | encoded | bvvcx-p3-settlement.l4 `15.1.2 — …` |
| 15.1.3 | 628 | Giảm tối đa đến một trăm | up to 100% by fault: subrogation, dishonesty, verification | encoded | bvvcx-p3-settlement.l4 `15.1.3 — …` (no rate: refused) |
| 15.1.4 | 640 | Giảm số tiền bồi thường tương | overloading over 20% and under 50%: by the percentage | encoded | bvvcx-p3-settlement.l4 `15.1.4 — …` |
| 15.1.5 | 643 | Giảm số tiền bồi thường theo | premium paid over premium due | encoded | bvvcx-p3-settlement.l4 `15.1.5 — …` (no due premium: refused) |
| 15.2 | 651 | Nguyên tắc giảm trừ số tiền | one reduction only, the highest | encoded | bvvcx-p3-settlement.l4 `15.2 — …` |
| Part IV preamble | 657 | Ngoài các quy định trong Phần | supplementary clauses: with base cover, if on the certificate | encoded | bvvcx-p4-supplementary.l4 `Part IV — the clause … is in effect …` |
| Art 16 BVVC01 | 673 | Bảo hiểm không khấu hao thay | no depreciation on new parts | encoded | bvvcx-p4-supplementary.l4 `Article 16 — …` |
| Art 17 BVVC02 | 682 | Bảo hiểm sửa chữa xe tại | repair at an authorised garage; not over 10 years in use | encoded | bvvcx-p4-supplementary.l4 `Article 17 — …` |
| Art 18 BVVC03 | 690 | Bảo hiểm xe bị ngập nước | flood damage; deductible 10%, at least 3,000,000 | encoded | bvvcx-p4-supplementary.l4 `Article 18 — …` |
| Art 19 BVVC04 | 700 | Bảo hiểm mất cắp bộ phận | theft of parts; 2 or 3 thefts; deductible 20%, at least 2,000,000; 24 hours | encoded | bvvcx-p4-supplementary.l4 `Article 19 — …` |
| Art 20 BVVC05 | 726 | Bảo hiểm thanh toán chi phí | car hire during repair; per day and per event; 3-day deductible | encoded | bvvcx-p4-supplementary.l4 `Article 20 — …` |
| Art 21 BVVC06 | 740 | Bảo hiểm bồi thường theo giới | settlement up to the limit of liability | encoded | bvvcx-p4-supplementary.l4 `Article 21 — …` |
| Art 22 BVVC07 | 753 | Bảo hiểm thiệt hại xảy ra | damage in China, Laos, Cambodia, Thailand | encoded | bvvcx-p4-supplementary.l4 `Article 22 — …` |
| Art 23 | 766 | Điều 23.Các điều khoản bổ sung | other clauses agreed in writing | reached-and-refused | bvvcx-p4-supplementary.l4 `the certificate carries an Article 23 clause …` |
| signature | 772 | TỔNG GIÁM ĐỐC | General Director | inert | bvvcx-p4-supplementary.l4 comment |

Totals: 109 encoded, 38 inert, 1 reached-and-refused (148 rows, 0 deferred).

## 3. Fork register

`LAW:` marks a fork that turns on the Law on Insurance Business 08/2022/QH15 (the aid at `.aids/law-08-2022-qh15.txt`; line numbers are its lines).
The aid's text stops at Article 130 and does not show the Law's commencement or transitional articles; that the Law took effect on 1 January 2023, after these Rules were issued, is outside knowledge, unverified.
A general rule sits under all of them: LAW: Article 24 (aid lines 588-591) construes an unclear term "in the purchaser's favour". Where two readings are evenly balanced the encoding takes the purchaser's; where one is the more natural reading of the words it takes that one and records the other.

| # | where | the question | readings | taken, and why |
| --- | --- | --- | --- | --- |
| F1 | def 8, src 71 | "Người lái xe được bảo hiểm": the person driving the insured vehicle, or the insured driver? | (i) the person driving the insured vehicle; (ii) a driver who is insured | (i): the definition's point is consent ("với sự đồng ý"), which (ii) would make redundant. |
| F2 | def 4, src 58; 12.2, 13.2 | "Giá trị thị trường" (12.2, 13.2.1, 13.2.2) is not the defined "Giá thị trường"; and is 12.3's "value" the market value? | (i) the same term; (ii) an undefined term | (i): the Article 12 heading writes "giá trị bảo hiểm (giá thị trường)", equating them. |
| F3 | notice, src 7-12 | Is the signed request evidence that the purchaser understood every term, exclusions included? | (i) yes, as the notice says; (ii) LAW: Article 19(2) (aid 435-440) requires the insurer to explain exclusions and hold evidence of it | Encoded as the notice says (`the notice — …`); whether that satisfies Article 19(2) is not decided (finding X12). |
| F4 | 10.1, src 424-426 | Does "sudden, unforeseeable" qualify every listed case, or accidents only? | (i) every case; (ii) accidents only | (i): consistent with LAW: Article 16(5) (aid 407-408), which requires every insured risk to be sudden and unforeseeable. |
| F5 | 11.3-11.7, 15.1.3(b) | Limbs that name "Người điều khiển xe" need the definition-8 driver; limbs with no subject? | (i) subjectless limbs reach whoever drove; (ii) all limbs need the defined driver | (i): the text names the defined term in some limbs and not others. So 11.4's drugs limb, 11.5's wrong-way, turn and lights limbs, 11.6 and 11.7 reach anyone driving; 11.3, 11.4's alcohol limb and 11.5's signals limb only a consenting driver. |
| F6 | passim | "ngày" (day): calendar or working? | (i) calendar; (ii) working | (i): the Rules say "ngày làm việc" where they mean working days (4.2.7, 5.2.4). |
| F7 | passim | Is the day of the event counted in "N ngày kể từ ngày X"? | (i) not counted: the last day is X + N; (ii) counted: X + N − 1 | (i): the Civil Code's rule as this encoder understands it (outside knowledge, unverified); it is also the purchaser-favourable reading for the purchaser's deadlines. |
| F8 | 2.1, src 118 | Are the first and last days on the certificate inside the period? | (i) both inside; (ii) end exclusive | (i). It also decides that a 1 January-31 December contract runs 12 months for BVVC04. |
| F9 | 3.1.2, 3.2.2, 3.2.4, 4.2.7 | "Tương ứng với thời gian còn lại": pro rata by what? | (i) calendar days; (ii) months; (iii) a short-period scale | (i): nothing in the Rules prints a scale. |
| F10 | 2.2, 3.1.1 | Is an agreement allowing the premium to be owed (3.1.1) a written agreement on the time for payment (2.2)? | (i) yes; (ii) no | (i): both postpone payment by agreement. |
| F11 | 10.1.3, 11.12, Art 18 | Is a flooded street a "natural catastrophe"? Is a parked car "operating" (hoạt động) in a flooded area? | flood: the caller's classification; parked: (i) not operating; (ii) operating | Flood: an input (`a natural catastrophe beyond human control` against `flooding in rain, storm or flood`). Parked: (i), so a parked car's drowned engine is covered by 10.1.3 without BVVC03 (finding X18). |
| F12 | 2.4, src 126-129 | When does a contract ended at the former owner's request end? | (i) at the transfer; (ii) at the request | (i): the request is made "on" the transfer and the Rules give no other date. |
| F13 | 3.1.1, 3.2.1 | "Chấm dứt vào ngày X": in effect on X or not? | (i) not in effect on X; (ii) in effect through X | (i): 3.1.1's "the day after the due date" only makes sense if the contract is not in effect on that day; 3.2.1 uses the same words. |
| F14 | def 12, 13.1.2(b) | Is depreciation measured at the start of cover or at the loss? | (i) at the start, as def 12 says; (ii) at the loss | (i): def 12 counts "to the month the insurance takes effect". |
| F15 | 4.2.7, 5.2.4 | What is a working day? | (i) Monday-Friday less public holidays; (ii) Monday-Saturday | (i), with the holidays supplied by the caller. |
| F16 | 4.2.3, src 206-208 | After the authority concludes, how long to pay? | (i) 15 days; (ii) 30 days | (i): the file is "complete and valid" from the conclusion, and the insurer itself verifies nothing more. |
| F17 | 4.2.7, src 229-230 | Pro rata from when? | (i) the date of the change; (ii) the date of re-rating | (i). |
| F18 | 6.2, src 316-320 | Who may appoint an independent assessor? | (i) the court of the place of damage or of the insured's residence; (ii) LAW: Article 53(2) (aid 1022-1025) also lets an arbitrator | (i) as written; the Law's wider route is recorded, not encoded. |
| F19 | Art 8, src 390-400 | What is double insurance? | (i) the Rules: two or more contracts on the same subject and conditions; (ii) LAW: Article 49(1) (aid 965-968): only where the sums insured together exceed the market value | (i) as written; the difference is finding X4. |
| F20 | 9.1, src 407-410 | From when does the year run if the insured did not know of the event? | (i) the event, as written; (ii) LAW: Article 30(2) (aid 711-714): from when the insured learned of it, if proved | (i) as written; the Law adds (ii). |
| F21 | 15.1.4, src 640-642 | Do children under 7 count for 15.1.4's overload? | (i) not counted, as 11.16; (ii) counted | (i): the same measure as the exclusion it adjoins, and the purchaser-favourable reading. |
| F22 | 9.4, src 419-421 | Does "tại Việt Nam" qualify arbitration as well as the courts? | (i) both; (ii) courts only | (i). |
| F23 | 11.13, src 481-483 | "Các bộ phận khác": does another tyre count? | (i) only parts that are not tyres, tarpaulins or labels; (ii) any other part | (i): (ii) would let two tyres save each other and empty the exclusion. |
| F24 | 11.17, src 496-500 | Does "trừ các thiết bị lắp thêm theo quy định" lift both limbs? | (i) both; (ii) the second only | (i), purchaser-favourable. |
| F25 | 10.1.4, 11.15 | Is taking by fraud or abuse of trust "trộm, cướp"? | (i) no; (ii) yes | (i): 11.15 names fraud separately (finding X21). |
| F26 | 11.15, src 485-486 | Is the parenthesis (hired, lent, debt, dispute) a limit? | (i) a limit; (ii) examples | (i), purchaser-favourable; under F25 it changes no answer. |
| F27 | 10.2, 12.4, Art 15 | Are the 10.2 costs inside the 12.4 cap, the deductible, the reduction and Article 8's share? | (i) outside all four; (ii) inside | (i): 10.2 pays them "ngoài số tiền bồi thường" (besides the compensation), and the other provisions speak of the compensation. |
| F28 | 15.1.1(c), src 606-610 | "Không giữ nguyên hiện trường thiệt hại, tự ý di chuyển …": one limb or two? | (i) one: not keeping the scene by moving without consent, with the safety exception; (ii) two | (i): under (ii) the safety exception would never save someone who moved the car for safety. |
| F29 | 12.1, src 502-505 | A sum insured above the value? | (i) declined; (ii) LAW: Article 47 (aid 933-952) | Declined by name; the Law settles it. |
| F30 | 13.1.2(a), src 526-533 | Does depreciation apply to a vehicle insured below value? | (i) yes: (a) pro-rates the "reasonable cost" that (b) defines; (ii) no: the depreciation sentence sits in (b) | (i), the more natural reading of the term. Under LAW: Article 24, (ii) is arguable and would pay more. |
| F31 | 13.2.1(a), src 552-553 | Which "reasonable cost" is compared with 75%? | (i) the cost 13.1.2(b) defines, depreciation included, of the parts the cover pays for; (ii) the undepreciated cost of all damage | (i): the same words as 13.1.2(b). |
| F32 | 13.3.2, src 566-571 | A kept wreck below value: deduct the whole valuation or the insurer's share? | (i) the insurer's share; (ii) the whole | (i): "giá trị thu hồi" is the value the insurer would recover. |
| F33 | 13.4 with 8, 12.4, 13.1.2(a), 13.3.2 | Where do the steps 13.4 does not order go? | as taken: pro-rating, then 13.4's three steps, then the 12.4 cap, then Article 8's share; a kept wreck inside the total-loss figure; 10.2 and BVVC05 added last | A choice; each step is in `bvvcx-claim.l4` and can be moved. |
| F34 | 14.1, src 584-586 | Does the deductible apply to a total loss? | (i) no: "mỗi và mọi vụ tổn thất bộ phận"; (ii) yes: 14.2 says "mỗi vụ tổn thất" | (i): the definition governs, and it is purchaser-favourable. |
| F35 | 14.3, src 593-595 | A certificate deductible below 500,000? | (i) as stated; (ii) raised to 500,000 | (i): 14.3 says another figure "will be stated on the certificate". |
| F36 | 15.1.1, src 599-602 | Is a theft (or a natural catastrophe) a "tai nạn"? | (i) yes, any loss event; (ii) collisions and fires only | (i): the Rules use "tai nạn" for every loss (6.1, 7.1.1). Under LAW: Article 24, (ii) is arguable; it would remove finding X3. |
| F37 | Part IV, src 661-662 | "Một trong các Điều khoản": one clause only? | (i) any number, as the certificate states; (ii) one | (i). |
| F38 | Art 20, src 735-736 | "Tổng số tiền bồi thường không vượt quá số tiền bảo hiểm trên ngày": a cap on each day or on the total? | (i) each day; (ii) the total | (i): (ii) would make the per-event sum unreachable (finding X16). |
| F39 | Art 21, src 745-749 | "Bồi thường theo số tiền bảo hiểm (đối với thiệt hại toàn bộ)": pay the sum insured, or up to it? | (i) pay it; (ii) up to it | (i): 13.2.2 already caps at the sum insured, so (ii) would add nothing (finding X20). |
| F40 | Arts 18-19, 13.4 | On what does a clause deductible ("10% số tiền bồi thường") fall? | (i) the part of the compensation paid under that clause, after pro-rating and before the deductible; (ii) the whole compensation | (i). |
| F41 | 11.4, src 459-460 | No alcohol reading taken? | (i) the exclusion is not shown; (ii) the claim cannot be decided | (i); refusing a test is 15.1.3(b). |
| F42 | 11.3, src 453-454 | "Đối với loại xe ô tô bắt buộc phải có Giấy phép lái xe": which cars need a licence? | (i) every car | (i); the traffic law is not in the sources. |
| F43 | 13.1.3, src 547-549 | Damage to half or less of the paint? | (i) the damaged area is paid (13.1.1); (ii) nothing | (i). |
| F44 | 2.2, src 120-122 | Paid in full when? | (i) on or before the date asked about, and by the due date unless continued under 3.1.3 | (i). |
| F45 | 1.1, src 106-108 | "Đã nộp phí bảo hiểm": any premium, or all of it? | (i) any | (i). |
| F46 | 5.2.4(b), 15.1.5(b) | Is a change in risk "not notified" before the 15 working days have run? | (i) yes, if the insurer has not been told when the loss happens; (ii) no | (i), as written (finding X24). |
| F47 | 3.2.1, src 153-158 | May a notice name a date before the notice? | (i) yes, nothing forbids it; (ii) no | (i) as written (finding X23). LAW: Article 26 (aid 623-635) limits the grounds for unilateral termination; the Rules' "theo quy định pháp luật" defers to it, and the encoding does not test grounds. |
| F48 | 15.1.1(a), src 601-602 | Is a late call excused by force majeure? | (i) no, as written; (ii) LAW: Articles 19(3) and 46(1) (aid 441-444, 917-927) bar reductions for late notice caused by force majeure and limit them to the insurer's loss | (i) as written (finding X17). |
| F49 | Art 7, 4.2.3 | When is a file "đầy đủ, hợp lệ"? | — | Not decided: the caller supplies the date the complete file was received (finding X6). |
| F50 | Art 19 with 11.13 | Is a stolen tyre alone a tyre "damaged alone"? | (i) yes: BVVC04 cancels only 11.14 | (i). |

Where I looked and found nothing to fork: the money figures (500.000, 3.000.000, 2.000.000 read with the dot as a thousands separator, confirmed by the generated tests); the depreciation table's edges (each row's lower bound is the previous row's upper bound); the 15.1.4/11.16 band (over 20% and under 50% reduce, 50% and over exclude, 20% and under do nothing: no gap and no overlap); the alcohol figures (exceeding, strict).

## 4. Findings

A finding is a defect or a surprise in the instrument as written, separate from the forks.
"Evidence" names the assertion that shows it; each such assertion passes, showing the surprising answer.

**X1. "The driver" is defined by consent, so exclusions about the driver miss a thief or a joyrider.** Source: def 8 (src 71-72); 11.1, 11.3, 11.4, 11.5 (src 442-466); 15.1.3(b) (src 636-637). Scenario: an unlicensed person drives the car without the owner's consent with 80 mg of alcohol per 100 ml and crashes. The owner's friend in the same state, driving with consent, is excluded by 11.3 and 11.4; the thief is not "the driver", so the loss is paid in full. Evidence: `bvvcx-tests-findings.l4` §X1 (`excluded by (LIST 11.3, 11.4)` against `16_000_000`). Favours the policyholder; an insurer's lawyer would read "Người điều khiển xe" loosely, against its own definition.

**X2. The exclusions ask for no causal link.** Source: 11 chapeau (src 441), 11.2 (src 449-451). Scenario: hail damages a parked car whose inspection certificate lapsed last week; nothing about the lapse caused the damage. 11.2 excludes the whole loss. The same holds for 11.3 (a lapsed licence on a driver rear-ended at a red light). Evidence: `bvvcx-tests-findings.l4` §X2 (`excluded by (LIST 11.2 …)`, payable 0).

**X3. A theft reported within the 24 hours 5.2.10 allows still loses 10% under 15.1.1(a)'s six hours.** Source: 5.2.10 (src 301-304); 15.1.1(a) (src 599-602); Article 19 (src 720-722) gives 24 hours for a theft of parts too. Scenario: the car is stolen; the owner tells the police and the insurer 20 hours later. 5.2.10 is met (its trace is FULFILLED), and the total-loss compensation falls from 580,000,000 to 522,000,000. Both clocks run from the event, not from its discovery, so an owner who finds the car gone in the morning may be out of time for both before knowing of the loss. Rests on fork F36 (a theft is a "tai nạn"). Evidence: `bvvcx-tests-findings.l4` §X3 (`#TRACE` FULFILLED; payable 522,000,000).

**X4. Double insurance and under-insurance reduce the same loss twice, and the Rules' "double insurance" is wider than the Law's.** Source: Article 8 (src 389-400); 13.1.2(a) (src 526-528); LAW: Article 49(1) (aid 965-968). Scenario: a car worth 600,000,000 insured for 300,000,000 with each of two insurers on the same conditions, which together insure exactly its value. Each insurer pro-rates by 0.5 for under-insurance and then pays half as its Article 8 share: a 16,500,000 loss yields 3,875,000 from each, 7,750,000 in all. Under the Law's Article 49 this is not double insurance at all. Evidence: `bvvcx-tests-findings.l4` §X4.

**X5. The claim file and the exclusion disagree about inspection.** Source: 7.1.2(d) (src 345-348); 11.2 (src 449-451). 7.1.2(d) excuses the inspection certificate for a vehicle circulating temporarily with written approval or being registered and inspected for the first time; 11.2 excuses only a new vehicle awaiting inspection, for 30 days. Scenario: a vehicle circulating temporarily with approval is damaged on day 165: the file need not include a certificate, and the loss is excluded for want of one. Evidence: `bvvcx-tests-findings.l4` §X5.

**X6. "A complete and valid file" starts the insurer's clocks and is never defined.** Source: 4.2.3, 4.2.4 (src 202-215); the Article 7 chapeau ("one or more" documents) and 7.3 ("other relevant documents, if any") (src 332-333, 378). The 15-day payment and 15-day refusal clocks run from receipt of a complete, valid file; Article 7 lists what a file may contain, leaves the choice open, and ends with other relevant documents. The insurer decides when its own clock starts. Reading only: the encoding takes the date of the complete file as an input (`The claim file`).

**X7. After 90 days without the authorities' conclusion the insurer must "proceed to consider" the claim, with no deadline.** Source: 4.2.3 (src 206-212). Evidence: `bvvcx-tests-contract.l4`, `#ASSERT REFUSED` on `4.2.3 — the last day for the insurer to pay on` with the message "4.2.3 sets no time for paying a claim the competent authority has not concluded on".

**X8. One notice of a change in risk starts two "5-day" clocks with different units.** Source: 4.2.7 (src 223-224: five working days to re-rate); 5.2.4(a) (src 254-257: five days to answer a request to reduce the premium). Scenario: a notice received Thursday 8 October 2026: the answer is due 13 October, the re-rating 15 October, so the insurer may have to say whether it reduces the premium before it has re-rated the risk. Evidence: `bvvcx-tests-findings.l4` §X8.

**X9. The premium is demanded for a period in which, under 2.2, there was no cover; and 3.1 mis-points at 2.3.** Source: 2.2-2.3 (src 120-125); 3.1, 3.1.1-3.1.2 (src 132-148). With no written agreement on time and nothing paid, 2.2 says the contract has no effect, yet 3.1.2 asks for the premium from the start of cover to the end of the contract. 3.1 says it applies to 2.3 (no agreement on time), while 3.1.1 speaks of the date agreed in the contract. Evidence: `bvvcx-tests-contract.l4`: the standing on 1 January is `not in effect, the premium not having been paid (2.2)` and `3.1.2 — the premium the insurer asks for …` is 10,000.

**X10. The definition of the purchaser requires full payment, which 2.2's deferred payment contradicts.** Source: def 2 (src 52-55); 2.2 (src 120-122). A person who agreed in writing to pay by 31 January is not "the purchaser" on 20 January, though the contract they concluded is in effect. Every duty and right the Rules give "the purchaser" is, on a literal reading, unowned until payment. Evidence: `bvvcx-tests-findings.l4` §X9 and X10.

**X11. When a dispute "arises" is undefined, and the complaint period is called both a time limit and a limitation period.** Source: 9.2-9.3 (src 411-418). The three-year time-bar runs from an undefined moment. Evidence: `bvvcx-tests-contract.l4`, `#ASSERT REFUSED` on `9.3 — the last day to sue` without a date. Otherwise reading only.

**X12. A signature on the request form is made evidence that the purchaser understood every term.** Source: the important notice (src 7-12); def 6 (src 63-68). LAW: Article 19(2) (aid 435-440) requires the insurer to explain the exclusions and to hold evidence that the purchaser was fully told and understood. A form recital that the signer understood everything is weaker evidence than the Law asks for. Reading only.

**X13. Discretion and undefined standards with weight on them.** 15.1.3 (src 628-630): a reduction up to 100% "by degree of fault", with no scale; 13.3.2 (src 569-571): the kept wreck at the insurer's own valuation; 4.2.5 (src 216): "serious or especially serious" accidents undefined; 6.4 (src 326): "special cases" undefined; 11.17 (src 499-500): "as the regulations provide" with no regulation named; def 2 (src 55): "Người thụ hưởng" capitalised and never defined. Evidence for the first: `bvvcx-tests-settlement.l4`, `#ASSERT REFUSED` with "a ground of 15.1.3 applies and the insurer has fixed no rate for it". The rest reading only.

**X14. A non-party is made to pay.** Source: 6.3 (src 322-325): where the independent assessment agrees with the insurer's, the insured AND the driver pay its cost. The driver (def 8) is not a party to the contract. Evidence: `bvvcx-tests-contract.l4`, `6.3 — who pays for the independent assessment … EQUALS LIST the insured, the driver`.

**X15. BVVC01 literally cancels the whole of 13.1.2(b), including the at-value rule for repairs.** Source: Article 16 (src 677-680). It cancels "the partial-loss provision in sub-point b of 13.1.2" and then restores only new parts at actual cost. Repairs survive under 13.1.1's general promise; a literal reader could argue otherwise. Reading only; the encoding keeps repairs paid.

**X16. BVVC05, read literally, caps the whole car-hire benefit at one day's sum insured.** Source: Article 20 (src 735-738): "the total compensation does not exceed the sum insured per day and the sum insured per event". With 800,000 a day and 8,000,000 an event, ten days at 1,000,000 pay 800,000 on the literal reading against 5,600,000 on the reading taken (F38). Evidence: `bvvcx-tests-findings.l4` §X16.

**X17. The six-hour rule has no force-majeure exception and is not tied to the insurer's prejudice.** Source: 15.1.1(a) (src 601-602), against (b)'s exception (src 604-605); LAW: Articles 19(3) (aid 441-444) and 46(1) (aid 917-927). Scenario: the insurer is told after 10 hours because of force majeure: still 10% off. Evidence: `bvvcx-tests-findings.l4` §X17 (14,350,000).

**X18. The same drowned engine is paid in full or not at all, depending on whether the car was "operating".** Source: 10.1.3 (src 430); 11.12 (src 479-480); Article 18 (src 690-699). A car parked when a flood reaches it: 10.1.3 pays the engine (39,500,000 on a 40,000,000 repair) without BVVC03. Driven into the same water: 11.12 excludes it (0) unless BVVC03, which then charges its own 10% deductible (35,500,000). "Operating" is undefined (F11). Evidence: `bvvcx-tests-settlement.l4` §BVVC03.

**X19. Either party may end the contract with immediate effect.** Source: 3.2.1 (src 153-158). A notice that states no time ends the contract on its own date; there is no notice period, so a purchaser may be uninsured from the day the insurer's letter is dated, before receiving it. LAW: Article 26 (aid 623-635) allows unilateral termination only on listed grounds; the Rules defer to the law without listing them. Evidence: `bvvcx-tests-contract.l4` §3.2.1 (ended on 20 June by a notice of 20 June).

**X20. BVVC06 pays the sum insured on a total loss even above the vehicle's market value at the loss.** Source: Article 21 (src 745-751); 13.2.2 (src 557-559). Scenario: insured at 600,000,000; market value at the loss 580,000,000: 580,000,000 without BVVC06, 600,000,000 with it. LAW: Article 16(3) (aid 399-401) allows indemnity above the actual loss only by agreement, which this is. Rests on F39. Evidence: `bvvcx-tests-findings.l4` §X20.

**X21. Exclusion 11.15 has nothing to exclude on the reading taken.** Source: 10.1.4 (src 431); 11.15 (src 485-486). If fraud and abuse of trust are not theft or robbery (F25), a vehicle so taken is outside 10.1 anyway and 11.15 is declaratory; if they are, 11.15's parenthesis leaves fraud on a vehicle that was not hired, lent or disputed covered. Either way the drafting suggests a broader 10.1.4 than its words. Evidence: `bvvcx-tests-cover.l4` (fraud: `outside the cover of Article 10`; `11.15 — …` TRUE only for a hired vehicle).

**X22. A purchaser who ends the contract because the insurer refused to cut the premium for a lower risk loses 30%.** Source: 5.2.4(a) (src 258-261) gives the right to end the contract under 3.2; 3.2.2 (src 159-163) refunds only 70%. LAW: Article 27(2) (aid 658-665) refunds "as agreed in the contract". Reading only; the 70% figure is tested in `bvvcx-tests-contract.l4`.

**X23. A notice may end the contract on a date already past.** Source: 3.2.1 (src 153-156): the notice must state clearly when the contract ends, and nothing requires that time to be after the notice. Scenario: an insurer's notice dated 20 June names 1 June; a loss on 15 June finds the contract ended. Evidence: `bvvcx-tests-findings.l4` §X23.

**X24. A change in risk is penalised inside the time the Rules allow for reporting it.** Source: 5.2.4 (src 248-251: 15 working days to notify); 15.1.5(b) (src 647-650). Scenario: the car is converted on Wednesday 10 June 2026; the purchaser has until 1 July to report it; the loss on 15 June is reduced by the premium shortfall (3,650,000 of 4,380,000: to 13,250,000), although no deadline was missed. Rests on F46. Evidence: `bvvcx-tests-findings.l4` §X24.

The three most likely to matter to a policyholder: X3 (theft: 6 hours against 24, both running from the event), X2 (exclusions without a causal link, so an expired inspection certificate defeats an unrelated claim), and X6 with X7 (the insurer controls when its payment clock starts, and after 90 days has none).

## 5. Answer table

The document prints no worked example, so every figure below is a scenario the tests module builds and works by hand from the text.

Worked figures the tests assert (VND). The standard case: a car first registered January 2022 (48 months in use when cover began: 15% depreciation), insured at value for 600,000,000; market value at the loss 580,000,000; a door repaired for 8,000,000 and a bumper replaced for 10,000,000 (8,500,000 after depreciation).

| case | what applies | payable | test |
| --- | --- | --- | --- |
| standard collision | 16,500,000 − 500,000 deductible | 16,000,000 | tests-settlement |
| registered Feb 2023 (35 months) | 0% depreciation | 17,500,000 | tests-settlement |
| registered Jan 2020 / 2016 / 2011 | 25% / 35% / 50% | 15,000,000 / 14,000,000 / 12,500,000 | tests-settlement |
| sum insured 480,000,000 of 600,000,000 | pro rata 0.8 | 12,700,000 | tests-settlement |
| the same with BVVC06 | no pro rata | 16,000,000 | tests-settlement |
| BVVC01 | no depreciation | 17,500,000 | tests-settlement |
| certificate deductible 2,000,000 | | 14,500,000 | tests-settlement |
| insurer told after 7 hours | 10% off | 14,350,000 | tests-settlement |
| repaired without consent; or speed 20% over | 25% off | 11,875,000 | tests-settlement |
| 7 hours and repaired without consent | the higher only | 11,875,000 | tests-settlement |
| dishonest, insurer fixes 40% | | 9,400,000 | tests-settlement |
| goods vehicle 30% / 49.9% / 50% overloaded | 30% off / 49.9% off / excluded | 11,050,000 / 7,766,500 / 0 | tests-settlement |
| premium 9,000,000 paid of 12,000,000 due | 25% off | 11,875,000 | tests-settlement |
| paint over half damaged (whole repaint 30,000,000) | | 46,000,000 | tests-settlement |
| repair 455,000,000 > 75% of 580,000,000 | total loss | 580,000,000 | tests-settlement |
| repair exactly 435,000,000 | partial | 434,500,000 | tests-settlement |
| total loss, wreck kept at 50,000,000 | | 530,000,000 | tests-settlement |
| total loss, sum insured 480,000,000 | no pro rata on a total loss | 480,000,000 | tests-settlement |
| theft, police suspended the case | | 580,000,000 | tests-settlement |
| flood under BVVC03, engine 40,000,000 | 10% clause deductible, then 500,000 | 35,500,000 | tests-settlement |
| catastrophe while parked, engine 40,000,000, no BVVC03 | base cover | 39,500,000 | tests-settlement |
| theft of a mirror (6,000,000 new) under BVVC04 | 2,000,000 floor, then 500,000 | 2,600,000 | tests-settlement |
| BVVC05, 10 days at 1,000,000 (800,000 a day) | 8,000,000 − 2,400,000 | + 5,600,000 | tests-settlement |
| 10.2 costs at the insurer's request, towing 70,000,000 | towing capped at 60,000,000 | + 62,000,000 | tests-settlement |
| 200,000,000 repair, sum insured 100,000,000 of 600,000,000, BVVC06 | capped at the sum insured (12.4) | 100,000,000 | tests-limits |
| another insurer, 400,000,000 on the same conditions | 600/1000 | 9,600,000 | tests-settlement |
| the layered case (below value, BVVC03, late call, 1,000,000 deductible, 2,000,000 costs) | | 38,800,000 | tests-settlement |

Refunds on a premium of 3,650,000 for 2026, ended 2 July (183 of 365 days left): purchaser 1,281,000; insurer 1,830,000; nothing to the purchaser once liability has arisen.

## 6. What `check.sh` prints

`TOTAL (16 modules)`: 0 errors, 307 assertions satisfied, 0 failed, 0 refused. No failure or refusal is expected and none is listed in `check.sh`'s `expected_failed`. The nine rule modules carry no assertions; the six `bvvcx-tests-*` modules other than `bvvcx-tests-fixtures.l4` (named cases only) carry them all: generated 54, contract 74, cover 74, settlement 80, limits 5, findings 20. `#ASSERT REFUSED` directives count as satisfied when the expression refuses with the stated message; they are how the declined cases are tested. The `#TRACE` directives (Articles 3.2.2, 4.2.3, 4.2.4, 5.2.6(a) and 5.2.10) print their outcome (FULFILLED or a named BREACH) and are not counted by `check.sh`.

## 7. The quote check

The gate (every `.l4` and every `.md` here except `BRIEF.md`, which is the lead's file):

```
vnsrc check: 1031 src: lines, 345 Vietnamese runs, 0 problems
```

The brief's literal command (`*.l4 *.md`, which includes `BRIEF.md`):

```
vnsrc check: 1031 src: lines, 361 Vietnamese runs, 2 problems
```

Both problems the literal command reports are on line 31 of `BRIEF.md`, the lead's file, which mixes English and Vietnamese and is not edited here. The gate is the first line.

## 8. Open questions for a domain expert

1. F30: does Bao Viet apply depreciation to a vehicle insured below value (13.1.2(a)), and pro rata after it?
2. F36 and X3: is a theft a "tai nạn" for 15.1.1(a)'s six hours, given 5.2.10's twenty-four?
3. F11 and X18: how does Bao Viet tell a "natural catastrophe" from ordinary flooding, and is a parked car "operating" for 11.12?
4. X2: does Bao Viet in practice apply 11.2 (no inspection certificate) to a loss the lapse did not cause, such as hail on a parked car?
5. X4 and F19: does Bao Viet apply Article 8 where the contracts together insure no more than the value (outside the Law's Article 49)?
6. X6: what makes a claim file "complete and valid" in practice, and who decides when it is?
7. F38: is BVVC05's per-day sum a cap on each day or on the total?
8. F39 and X20: does BVVC06 pay the sum insured on a total loss when the market value at the loss is lower?
9. Do the Rules issued under Decision 5688/QĐ-BHBV still apply after the Law on Insurance Business 08/2022/QH15 took effect, or has a newer decision replaced them? The document as retrieved shows no amendment.
10. F35: may a certificate set a deductible below 14.3's 500,000?
