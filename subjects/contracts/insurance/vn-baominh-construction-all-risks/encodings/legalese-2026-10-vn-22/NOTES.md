# NOTES — vn-baominh-construction-all-risks, encoding row `legalese-2026-10-vn-22`

Bảo Minh's construction all risks wording, "Quy tắc bảo hiểm mọi rủi ro xây dựng", encoded in L4 by one agent in one session (run `VN-22-20261006`, agent `enc-vn-22`, 2026-10-06 to 2026-10-07), from the brief in `BRIEF.md`.
Status: **draft**.
No domain expert has read it against the source; HG1 has not been sought; no independent test pass has been run; every expected value was written by the session that wrote the rules.

Source: `../../source/raw/baominh-car.txt`, the `pdftotext -layout` rendering (330 lines, sha256 `38fa3915e19d4b97094f1e4e7f0c9754c19715348fba0c3e3e5d36feb383ce17`) of the 6-page PDF (sha256 `5dbef555b6fd4132dd6b55c0ebb7200e7f03071bd0867e5644c3085d8ea2bcce`) published on baominh.com.vn and retrieved on 2026-10-06.
Every "line N" below, and every `src:N` in the modules, is line N of the `.txt` rendering.

## 0. Build and run

`l4` is `/Users/mengwong/.local/bin/l4`, a symlink to `~/.cabal/bin/l4`, which resolves to the cabal store entry `jl4-0.1-0ee0100b` (`/Volumes/transcend/caches/cabal/store/ghc-9.10.3-fe9c/jl4-0.1-0ee0100b/bin/l4`, modified 2026-10-06 21:20 local), sha256 `64bbcb157dbef2ef1020a6a75589313bba0a2aeeb807c921c5e65e62e9eca118`.
The binary has no `--version`.
`JL4_LIBRARY_PATH` was unset for every run.
Every run prints two Warnings that differing copies of `prelude` and `daydate` are visible under `~/.local/share/jl4/libraries/`; the binary uses its embedded copies, and the warnings are not errors.

The command, from this directory:

```
L4=/Users/mengwong/.local/bin/l4 ./check.sh
```

What it printed is in §6.

**How the modules were made.**
The `.l4` files were written as templates in the session's scratch directory and expanded by a small script that replaces each placeholder line with the output of `python3 -I tools/vnsrc.py quote ../../source/raw/baominh-car.txt N M`; so every `-- src:N |` line is the tool's output, not typed.
The 53 `A loss to an item` literals and the 23 `A claim under Section II` literals in `bmcar-fixtures.l4` were written by a script from one set of defaults plus each fixture's stated differences, because L4 has no record-update operator and each literal has 19 to 22 fields; the script computes no expected value.
Neither script is deposited (the brief keeps scratch files out of the deposit); the `.l4` files are complete without them, and `tools/vnsrc.py check` re-verifies every quotation.

**Modules.**

| module | what it holds |
| --- | --- |
| `bmcar-nouns.l4` | DECLARE only: the parties, the Schedule, the policy in force, the Insured's conduct, notices, causes, kinds of property, a loss to an item, claim histories, the two claim records, outcomes, acts |
| `bmcar-insuring-and-period.l4` | title, recital (inert), insuring agreement, period of insurance (lines 1-52) |
| `bmcar-general-exclusions.l4` | General Exclusions (a)-(d) and the burden of proof (lines 17-39) |
| `bmcar-general-conditions.l4` | General Conditions 1-9, with regulative rules for General Conditions 5 and 7 (lines 55-145) |
| `bmcar-section-1.l4` | Section I: insuring clause, debris, exclusions (a)-(i), Articles I, 2 and 3, the occurrence, the outcome (lines 148-253) |
| `bmcar-section-2.l4` | Section II: insuring clause, costs, limit, exclusions 1-4, Conditions 1-2, the outcome (lines 256-325) |
| `bmcar-fixtures.l4` | named cases; no directives |
| `bmcar-tests.l4` | 189 `#ASSERT` and 8 `#TRACE`, expected values from the text |
| `bmcar-findings.l4` | 21 `#ASSERT` and 1 `#TRACE` demonstrating the findings of §4 |

## 1. What is encoded and what is not

**Encoded: the whole document.**
Every clause of the 6 pages is in the coverage table (§2) with a disposition, and none is `deferred`.
The three layers the brief asks for are kept apart.
Cover: the insuring agreement's premium condition, the period of insurance, the General Exclusions, the Section I and Section II insuring clauses and their exclusions.
Amount: Article 2's two bases with its total-loss switch, the "actually incurred" and "included in the sum insured" limits, Article 3, exclusion (d)'s carve-out, Article I's average for items 1, 2 and 3, the item's sum insured, the deductible, debris clearance, the per-occurrence limit, the Section's total sum insured, and Section II's damages, costs, deductible and limit.
Duties: General Conditions 1 and 3-6 as the conditions precedent the claim stands on; General Condition 5's 14-day bar as a date function and as a regulative rule; the inspection-before-repair rule as a regulative rule; General Condition 7's one-month appointment as a regulative rule; General Condition 8's three months as a date function; Section II Condition 1 as a prohibition and a permission.
`Section I — the outcome of the claim` and `Section II — the outcome of the claim` gather everything and say why nothing is payable when nothing is.

**Inputs, not encoded figures.**
The document prints no money figure.
The premium, the period dates, the items and their sums insured, the total sum insured, any per-occurrence limit, the debris sum, the deductibles and the Section II limit are in the Schedule ("Phụ lục"), which is not in the document; each is a field of `The Schedule` with no default.
Facts that need a judgement the document does not make (whether a notice was "immediate", a period "reasonable in the circumstances" for inspection, "the sum for which the claims can be settled") are inputs too, each named in the fork register.

**Declined by name (`REFUSE`), because the document does not answer:** who bears the burden of proof where Bảo Minh contends that General Exclusion (a) applies; the adjustment of cover or premium after a material change (General Condition 4(b)); Bảo Minh's rateable proportion where another insurance covers the loss (General Condition 9); the sum required to be insured for an item other than 1, 2 and 3 (Article I); a measure of value that has not been established; and the time within which Bảo Minh must pay (Sections I and II).

**Not encoded:** the Law on Insurance Business 08/2022/QH15 (an aid; where it bears on a clause it is a fork tagged `LAW:` in §3), the Civil Code, and compulsory construction-investment insurance under Decree 67/2023, which is a different regime (fork F47).
No sibling wording was read.

## 2. Coverage table

Headings are as the document writes them; a paragraph with no heading is identified by its first words.
Totals: **63 rows: 55 encoded, 6 inert, 2 reached-and-refused, 0 out-of-scope, 0 deferred.**
Four encoded rows (9, 52, 57, 63) also carry a limb that is reached and refused; each is named in its row.

| # | lines | heading or first words, as written | English gloss | disposition | where in the L4 |
| --- | --- | --- | --- | --- | --- |
| 1 | 1-2 | "QUY TẮC" / "BẢO HIỂM MỌI RỦI RO XÂY DỰNG" | title: rules for construction all risks insurance | inert: a title | `bmcar-insuring-and-period.l4` header |
| 2 | 5-9 | "Trên cơ sở Người được bảo hiểm có tên trong phụ lục" | recital: the proposal and questionnaire form part of the Policy | inert: its operative effect is General Condition 1 (row 22) | comment; X1 |
| 3 | 11-14 | "Đơn bảo hiểm này xác nhận với điều kiện là" | insuring agreement: on payment of the premium Bảo Minh indemnifies as provided | encoded | `the insuring agreement — the premium stated in the Schedule has been paid` |
| 4 | 17-20 | "CÁC ĐIỂM LOẠI TRỪ CHUNG" | General Exclusions, chapeau: loss directly or indirectly caused by | encoded | `a General Exclusion applies to a loss caused by` |
| 5 | 22-28 | "a)" "Chiến tranh, xâm lược" | (a) war, rebellion, strike, riot, usurped power, political violence, confiscation | encoded | `General Exclusion (a) applies to a loss caused by` |
| 6 | 30 | "b)" "Phản ứng hạt nhân" | (b) nuclear | encoded | `General Exclusion (b) …` |
| 7 | 32 | "c)" "Hành động cố ý hay cố tình sơ xuất" | (c) wilful act or wilful negligence of the Insured | encoded | `General Exclusion (c) …` |
| 8 | 34 | "d)" "Ngừng công việc" | (d) cessation of work | encoded | `General Exclusion (d) …` |
| 9 | 36-39 | "Trong các trường hợp khiếu tố, kiện tụng hay kiện cáo" | burden of proof under exclusion (a) | encoded (the Insured-contends case); the Bảo Minh-contends case reached-and-refused | `the party who must prove …` |
| 10 | 42-45 | "THỜI HẠN BẢO HIỂM" — "Trách nhiệm của Bảo Minh sẽ bắt đầu" | period: commencement on the works or unloading | encoded | `the date Bao Minh's liability commences` |
| 11 | 47-48 | "Sau khi từng phần của công trình" | period: ends for a part handed over and put into use | encoded | `cover had ended for the damaged part …` |
| 12 | 51-52 | "Chậm nhất thì bảo hiểm này sẽ chấm dứt" | period: ends on the Schedule date; extensions in writing | encoded | `the date the insurance ends at the latest` |
| 13 | 50, 109, 168, 222, 277, 330 | page footer "(Munich Re)_03.06" | the footer names Munich Re and "03.06" | inert: page furniture | §4 X22 |
| 14 | 55 | "ĐIỀU KIỆN CHUNG" | General Conditions, heading | inert: a heading | section heading |
| 15 | 57-60 | "1." | compliance and true answers are a condition precedent | encoded | `General Condition 1 — the conditions precedent to liability are met` |
| 16 | 62-66 | "2." | the Schedule is part of the Policy; a term keeps its meaning | inert: an interpretive rule with no defined term to act on | comment; forks F22, F15; X20 |
| 17 | 68-70 | "3." | reasonable precautions at the Insured's expense | encoded | `General Condition 3 — …` (two rules) |
| 18 | 72-74 | "4. a)" | inspection; information to assess the risk | encoded | `General Condition 4(a) — …` |
| 19 | 76-78 | "b)" "Người được bảo hiểm phải lập tức thông báo" | notify a material change by telegram and in writing; additional precautions | encoded | `General Condition 4(b) — a material change was notified and provided for` |
| 20 | 79-80 | "nếu cần thì phạm vi bảo hiểm và/hoặc phí bảo hiểm sẽ được điều chỉnh" | adjustment of cover or premium | reached-and-refused: no criteria | `General Condition 4(b) gives no criteria …` |
| 21 | 82-84 | "Người được bảo hiểm không được tự ý tiến hành" | no unapproved material change increasing the risk | encoded | `General Condition 4 — no material change …` |
| 22 | 86-90 | "5." "a) Lập tức thông báo ngay" | notice of an occurrence | encoded | `General Condition 5(a) — notice was given as required`; regulative `General Condition 5 — the duty to notify an occurrence` |
| 23 | 92-93 | "b) Thực hiện mọi biện pháp" | minimise the loss | encoded | `General Condition 5(a)-(e) — …` |
| 24 | 95-96 | "c) Bảo quản các bộ phận bị tổn thất" | preserve the damaged parts | encoded | same |
| 25 | 98 | "d) Cung cấp mọi thông tin" | furnish information and documents | encoded | same |
| 26 | 100 | "e) Thông báo cho cơ quan Công an" | inform the police of theft | encoded | same |
| 27 | 102-104 | "Trong mọi trường hợp, Bảo Minh sẽ không chịu trách nhiệm" | 14-day bar on notice | encoded | `General Condition 5 — Bao Minh received notice within 14 days …` |
| 28 | 106-112 | "Sau khi thông báo cho Bảo Minh theo điều kiện này" | minor repairs; inspection before other repairs | encoded | regulative `General Condition 5 — the inspection before repair, within`; `… no damage that was not minor was repaired before an inspection` |
| 29 | 114-115 | "Trách nhiệm của Bảo Minh theo Đơn bảo hiểm này đối với bất kỳ hạng mục" | cover ends on an item not repaired properly without delay | encoded | `General Condition 5 — cover on the item had ceased …` |
| 30 | 117-124 | "6." | subrogation, at Bảo Minh's expense | encoded | `General Condition 6 — …` (two rules) |
| 31 | 126-127 | "7." "Nếu có sự tranh chấp về số tiền bồi thường" | arbitration of the amount, liability admitted | encoded | `General Condition 7 — the difference must be referred to arbitration` |
| 32 | 127-132 | "Trọng tài này do hai bên chỉ định" | appointment: one arbitrator, or two within one month, and an umpire | encoded | `the last day to appoint an arbitrator …`; regulative `General Condition 7 — the duty of …` |
| 33 | 132-134 | "Trọng tài chung sẽ ngồi với hai trọng tài kia" | the umpire presides; the award is a condition precedent to an action | encoded | `General Condition 7 — an action against Bao Minh is barred for want of an award` |
| 34 | 136-138 | "8." "Nếu có sự khiếu nại gian lận hay khai báo sai" | forfeiture for fraud or a false declaration | encoded | `General Condition 8 — the claim is tainted by fraud …` |
| 35 | 138-141 | "hoặc nếu khiếu nại đòi bồi thường bị khước từ" | forfeiture: no proceedings within three months of an award | encoded | `General Condition 8 — the time-bar after an award has run` |
| 36 | 143-145 | "9." | other insurance: rateable proportion | reached-and-refused: the proportion is not defined | `General Condition 9 limits Bao Minh to a rateable proportion …`; the cap given a proportion is encoded |
| 37 | 148 | "PHẠM VI BẢO HIỂM" | scope of cover, heading | inert: a heading | section heading |
| 38 | 150-155 | "PHẦN I - TỔN THẤT VẬT CHẤT" — "Trong phần này Bảo Minh thoả thuận" | Section I insuring clause | encoded | `Section I — the insuring clause reaches the loss to the item` |
| 39 | 156-157 | "bằng tiền, bằng cách sửa chữa, thay thế (tùy Bảo Minh lựa chọn)" | cash, repair or replacement at Bảo Minh's option | encoded | `Section I — the party who chooses …` |
| 40 | 157-160 | "mức bồi thường đối với từng hạng mục" | caps: the item's sum, the per-occurrence limit, the Section total | encoded | `Section I — the indemnity for the loss to the item`; `… the per-occurrence limit applied to`; `… what remains of the total sum insured` |
| 41 | 162-164 | "Bảo Minh cũng sẽ bồi thường cho Người được bảo hiểm chi phí dọn dẹp hiện trường" | debris clearance, if a separate sum is entered | encoded | `Section I — the reimbursement of the cost of clearing debris` |
| 42 | 169-171 | "Điều khoản loại trừ chỉ áp dụng riêng cho Phần I" | Section I exclusions, chapeau | encoded | `a Section I exclusion takes the whole loss …` |
| 43 | 173-174 | "a)" "Mức khấu trừ" | (a) the deductible, each occurrence | encoded | `Section I exclusion (a) — the losses to items, less the deductible` |
| 44 | 176-177 | "b)" "Tất cả các loại tổn thất có tính chất hậu quả" | (b) consequential loss | encoded | `Section I exclusion (b) — …` |
| 45 | 179 | "c)" "Những tổn thất do thiết kế sai" | (c) faulty design | encoded | `Section I exclusion (c) — …` |
| 46 | 181-184 | "d)" "Những chi phí thay thế, sửa chữa, chỉnh lý khuyết tật" | (d) defective material or workmanship, limited to the items affected | encoded | `Section I exclusion (d) — …`; alternative reading in `bmcar-findings.l4` |
| 47 | 186-187 | "e)" "Ăn mòn, mài mòn, ô xy hoá, mục rữa" | (e) corrosion, wear, oxidation, deterioration | encoded | `Section I exclusion (e) — …` |
| 48 | 189-190 | "f)" "Đổ vỡ cơ học" | (f) breakdown of construction plant | encoded | `Section I exclusion (f) — …` |
| 49 | 192-193 | "g)" "Mất mát hay thiệt hại đối với xe cơ giới" | (g) licensed vehicles, ships, barges | encoded | `Section I exclusion (g) — …` |
| 50 | 195-196 | "h)" "Mất mát hay thiệt hại đối với hồ sơ, sơ đồ" | (h) records, cash and instruments | encoded | `Section I exclusion (h) — …` |
| 51 | 198 | "i)" "Mất mát hay thiệt hại chỉ phát hiện được vào thời điểm kiểm kê" | (i) loss found only at an inventory | encoded | `Section I exclusion (i) — …` |
| 52 | 200-211 | "Điều khoản áp dụng cho phần I" — "Điều I - Số tiền bảo hiểm:" | Article I: the sum insured required for items 1, 2 and 3 | encoded (items 1-3); another item reached-and-refused | `Article I — the sum for which the item should have been insured` |
| 53 | 213-215 | "và Người được bảo hiểm cam kết sẽ tăng hay giảm số tiền" | sums adjusted for price movements, effective once recorded | encoded as an input convention: the item's sum insured is the one recorded | `bmcar-nouns.l4`, `An item entered in the Schedule` |
| 54 | 217-220 | "Trong trường hợp có tổn thất, nếu phát hiện thấy số tiền bảo hiểm thấp hơn" | the average, item by item | encoded | `Article I — the average applied to … for the loss` |
| 55 | 223-232 | "Điều 2 - Cơ sở giải quyết bồi thường:" | Article 2: (a) repairable, (b) total loss | encoded | `Article 2(a) …`, `Article 2(b) …`, `Article 2 — the basis of indemnity for the loss` |
| 56 | 234-236 | "Tuy nhiên chỉ bồi thường ở mức độ chi phí mà Người được bảo hiểm thực tế phải gánh chịu" | only what was actually incurred, and what the sum insured includes | encoded | `Article 2 — the cost actually incurred …`; `Article 2 — the loss to the item, before Article I and the limits` |
| 57 | 238-242 | "Bảo Minh sẽ chỉ bồi thường sau khi thoả mãn" | payment after invoices; repairable losses repaired; repair at or above value settled as total loss | encoded (the time for payment reached-and-refused, row 63) | `Article 2 — Bao Minh is not yet bound to pay …`; `Article 2 — the loss is settled as a total loss` |
| 58 | 244-245 | "Chi phí sửa chữa tạm thời" | provisional repairs | encoded | `Article 2 — the cost actually incurred …` |
| 59 | 247-248 | "Mọi chi phí nhằm sửa đổi, bổ sung và/hoặc hoàn thiện thêm" | alterations and improvements not paid | encoded | same |
| 60 | 250-253 | "Điều 3 - Mở rộng phạm vi bảo hiểm:" | Article 3: overtime, night and holiday work, express freight | encoded | `Article 3 — …` |
| 61 | 256-279 | "PHẦN II – TRÁCH NHIỆM ĐỐI VỚI BÊN THỨ BA" | Section II: insuring clause; costs; limit | encoded | `Section II — the insuring clause reaches the claim`; `… the damages Bao Minh pays`; `… the costs Bao Minh pays`; `… the indemnity for the claim` |
| 62 | 281-308 | "Những loại trừ áp dụng riêng cho phần II" — "1." to "4. d)" | Section II exclusions 1, 2, 3, 4(a)-(d) | encoded | `Section II exclusion 2 …` to `… 4(d) …`; deductible in `Section II — the indemnity for the claim` |
| 63 | 310-325 | "Các điều kiện áp dụng riêng cho Phần II" — "1." and "2." | Condition 1: no admission; Bảo Minh may take over. Condition 2: pay the limit or a settlement sum and be discharged | encoded; the time for payment (Sections I and II) reached-and-refused | `Section II Condition 1 — …` (three rules); `Section II Condition 2 — …` (two rules); `the policy states no time within which Bao Minh must pay …` |

Rows 9, 52, 57 and 63 are counted as encoded; the refusals inside them (row 9's Bảo Minh-contends case, row 52's other items, row 63's time for payment, which row 57 points to) are named in the row.

## 3. Fork register

A fork is an ambiguity resolved; a defect in the instrument is a finding (§4).
Rows tagged `LAW:` record where the Law on Insurance Business 08/2022/QH15 (`.aids/law-08-2022-qh15.txt` at the root of the vn-insurance worktree, "Law line N") bears on a clause; the Law is not encoded, and no conflict is resolved by it.
Contra proferentem (F36) is noted where it would point one way.

| # | where | the question | readings | taken, and why |
| --- | --- | --- | --- | --- |
| F1 | recital, lines 5-9 | "(giấy yêu cầu bảo hiểm này được xem như)" never says what the proposal is deemed to be, and the next parenthesis never closes | (i) the proposal and questionnaire are incorporated into the Policy; (ii) the deeming is void for incompleteness | (i), and inert: General Condition 1 gives the questionnaire answers their effect independently. |
| F2 | insuring agreement, lines 11-12 | When must the premium have been paid? | (i) by the time the claim is decided; (ii) before the occurrence; (iii) by a due date in the Schedule | (i): the clause states no time; the fact is a BOOLEAN on the policy. See F49. |
| F3 | General Exclusions, lines 19-20 | "trực tiếp hay gián tiếp gây nên bởi" with several causes | (i) any listed risk among the causes excludes; (ii) only a proximate or dominant cause | (i): "or indirectly" reaches remote causes; the causes are a list on the loss. Contra proferentem would favour (ii). Finding X24. |
| F4 | lines 36-39 | Who bears the burden where Bảo Minh contends exclusion (a) applies? | (i) as written, the clause speaks only of the Insured contending ("Người được bảo hiểm cho là"); (ii) read as the insurer contending | (i): the case written is encoded; the case not written is a REFUSE. Finding X2. |
| F5 | lines 44-45 | "từ lúc khởi công công trình hoặc sau khi dỡ xong các hạng mục" | (i) the earlier of the two events, for the whole policy; (ii) each item from its own event; (iii) the later of the two | (i): the disjunction names two triggers and the first to happen starts liability; the text gives no per-item rule. Unloading counts from the day it is completed. |
| F6 | line 45 | "dù ngày quy định trong phụ lục có thể khác" | (i) the Schedule's start date does not govern either way, so cover can begin before it; (ii) cover never begins before the Schedule date | (i), as the Vietnamese reads; it has no "only". A statement that the insurer's English original reads "only after" would be outside knowledge, unverified. Finding X3. |
| F7 | lines 47-48 | "đã được bàn giao và đưa vào sử dụng" | (i) both, handed over AND put into use; (ii) either | (i): "và". Finding X4. |
| F8 | line 51 | Is the Schedule's end date inside the period? | (i) inclusive; (ii) exclusive | (i): "chấm dứt hiệu lực vào ngày" ends cover on that date, read as at its end. |
| F9 | General Condition 1, lines 57-60 | Does any breach of any duty defeat the claim? | (i) yes, no materiality or causation test; (ii) only a material breach connected with the loss | (i), as written. See F38 and F46 for the Law. Findings X5, X6. |
| F10 | General Condition 4(b), lines 76-80 | "bằng điện tín và bằng văn bản"; and the adjustment | (i) telegram AND writing, both required; (ii) either | (i): "và". The adjustment of cover or premium has no criteria and is refused. Findings X6, X23. |
| F11 | General Condition 5(a), lines 89-90 | "Lập tức" (immediately) has no period; "bằng điện thoại hay điện tín cũng như bằng văn bản" | (i) "immediately" is a fact to be found, the medium is (telephone or telegram) and writing; (ii) "immediately" means within the 14 days of lines 102-104 | (i): the two sentences are separate duties; reading (ii) would make the first redundant. Finding X5. |
| F12 | lines 102-104 | "trong vòng 14 ngày kể từ ngày xảy ra sự cố" | (i) 14 calendar days, the day of the occurrence not counted, receipt on day 14 in time; (ii) the day of the occurrence is day 1; (iii) working days | (i): "ngày" undefined; (i) is the longer of the calendar readings and so the one contra proferentem favours. That the Civil Code excludes the first day is outside knowledge, unverified. Tested both sides. |
| F13 | lines 106-112 | "hư hỏng nhỏ" (minor damage) and "một thời gian được xem là hợp lý xét theo tình hình thực tế" | — | Neither has criteria: whether damage was minor and the reasonable period are inputs. Finding X7. |
| F14 | lines 114-115 | Liability for an item "chấm dứt" if not repaired properly without delay: for this loss, or for later ones? | (i) later occurrences only; (ii) this loss too | (i): Article 2 already pays only what was actually spent on this loss; reading (ii) would add a forfeiture the clause does not name. |
| F15 | General Condition 7, lines 126-134 | Scope; "một tháng"; "Trọng tài chung" | (i) only a difference on the amount, liability admitted, is arbitrable; one calendar month from the day the request is sent, the last day inclusive; (ii) any difference | (i): "(trách nhiệm được chấp nhận theo cách khác)". "gửi" (sends) fixes the start. "Trọng tài chung" is the sole arbitrator at line 128 and the umpire at lines 131-132 (finding X9). |
| F16 | General Condition 8, lines 138-141 | The time-bar limb | (i) as the Vietnamese has it: a rejected claim, AND no proceedings within three calendar months of an award, where there was an arbitration; "bị khước từ" includes a rejection of the amount; an award by any of the three makers starts the clock; (ii) a bar running from the rejection itself | (i): the Vietnamese has no clock from the rejection. Proceedings on the last day are in time. Findings X9, X10. |
| F17 | General Condition 9, lines 143-145 | "tỷ lệ của họ" | (i) by sums insured; (ii) by independent liability; (iii) other | **not answered**: refused by name; a caller with a proportion can apply it. See F43. Finding X12. |
| F18 | Section I, lines 158-159 | "hạn mức trách nhiệm bồi thường đó" has no antecedent | (i) a per-occurrence limit where the Schedule stipulates one; (ii) the item's sum insured again | (i): an optional Schedule figure (`MAYBE`); none stipulated means no per-occurrence cap. Finding X13. |
| F19 | lines 159-160 | The Section total | — | The total sum insured for Section I less what was paid earlier in the period caps each occurrence. |
| F20 | lines 162-164 | Debris clearance | (i) payable only where the occurrence gives rise to a covered Section I loss, up to the separate sum, not averaged, outside the deductible, inside the per-occurrence and total caps; (ii) any claim under the Policy | (i): "sự cố dẫn đến khiếu nại theo Đơn bảo hiểm này"; the separate sum has no "required" value to average against. No sum entered means no debris cover. |
| F21 | exclusion (a), lines 173-174 | "trong mọi sự cố" | (i) one deductible per occurrence, after the per-item average; (ii) per item; (iii) before the average | (i): the deductible is per occurrence and the average is per item ("một cách riêng biệt"), so the average is applied first. On a single underinsured item, (iii) would pay the Insured deductible x (1 - ratio) more, so contra proferentem favours it; but on several items (iii) needs the one deductible apportioned among them, which the text does not do. |
| F22 | exclusion (d), lines 181-184 | "hạng mục" in "chỉ hạn chế trong chính những hạng mục bị ảnh hưởng trực tiếp" | (i) a component of the works; (ii) an item of the Schedule, as at lines 153 and 206 | (i): the encoding takes out only the cost of rectifying the defect itself. (ii) is demonstrated in `bmcar-findings.l4`. Finding X14. |
| F23 | exclusion (e), lines 186-187 | Does "do ít sử dụng hay do điều kiện áp suất, nhiệt độ bình thường" qualify all four, or "mục rữa" only? | (i) all four; (ii) only deterioration | (i): one list, one qualifier; the cause is one constructor carrying the qualifier. Under (ii), corrosion from an abnormal event (a chemical spill) would be excluded too. LAW: Art 50 (Law lines 974-978) excludes wear and inherent vice unless otherwise agreed. |
| F24 | exclusion (f), lines 189-190 | Breakdown "của các trang thiết bị và máy móc xây dựng" | (i) the plant's own breakdown only; (ii) any loss caused by a plant breakdown | (i): the item is "Đổ vỡ cơ học" itself, not loss "do" it; contrast (c) "tổn thất do thiết kế sai". Near misses are tested. |
| F25 | Article I, lines 206-208 | The principal's materials | (i) added to the contract value where the contract price does not contain them; (ii) already inside the contract value | (i): "bao gồm … nguyên vật liệu hay các hạng mục do chủ công trình (bên A) cung cấp" names them as part of the required sum; the record has two fields to avoid counting them twice. |
| F26 | Article I, lines 217-220 | The order of the average, and items other than 1-3 | (i) per item, on the Article 2 amount, before the item's sum insured caps it and before the deductible; (ii) on the final indemnity | (i), with F21. An item other than 1, 2 and 3 has no required sum stated and is refused. LAW: see F42. |
| F27 | Article 2, lines 234-236 | Does "chỉ bồi thường ở mức độ chi phí mà Người được bảo hiểm thực tế phải gánh chịu" reach basis (b)? | (i) both bases; (ii) repairs only | (i): "Tuy nhiên" follows (a) and (b) together, and lines 238-240 speak of repair "or replacement". Contra proferentem would favour (ii). Finding X17. |
| F28 | Article 2, lines 240-242 | "tương đương hay vượt quá" | — | At least equal (`AT LEAST`); tested at, above and one VND below. |
| F29 | Section II, lines 258-264 | "bên thứ ba" | — | Not defined: anyone other than the Insured, subject to exclusions 4(a) and 4(b). Whether one named Insured is a third party to another is not answered by the text (open question 4). |
| F30 | Section II, lines 258, 278-279, 285 | Limit and deductible | (i) the limit applies per occurrence, costs inside it, the deductible on damages and costs together; (ii) an aggregate for the period | (i): Condition 2 speaks of "hạn mức bồi thường với mỗi sự cố". No aggregate is modelled. LAW: F45. |
| F31 | Section II, lines 269-273 | Costs of a claim the Insured successfully defends | (i) the costs incurred with written consent are paid if the claim is within the cover; (ii) only when the Insured is held liable | (i): "được giải quyết theo các quy định" covers a claim resolved under the Policy, and contra proferentem and Law Art 59.3 (Law lines 1098-1103) point the same way. |
| F32 | exclusion 3, lines 290-292 | The second limb | (i) harm caused by the damaged property, land or buildings; (ii) any harm caused by vibration | (i): "do bất kỳ tổn thất nào nêu trên gây ra". Injury caused directly by vibration is covered (tested). |
| F33 | Condition 2, lines 321-325 | "số tiền mà khiếu nại … có thể được giải quyết" | — | Bảo Minh's figure; an input. Finding X19. |
| F34 | lines 238-240 | When must Bảo Minh pay? | — | **not answered**: refused by name for both Sections. LAW: F40. |
| F35 | Sections I and II | Does Section II Condition 1 bind a Section I claim through General Condition 1? | (i) no; (ii) yes | (i): an admission to a third party has no bearing on a material-damage claim; reading (ii) is literal but empty in practice. |
| F36 | LAW: Art 24, Law lines 588-591 | Contra proferentem | — | An unclear term is read for the policyholder. Not applied by the encoding; noted per fork. |
| F37 | LAW: Art 19.2, Law lines 435-440 | Exclusions must be explained, with evidence the buyer understood them | — | Whether each exclusion binds depends on facts outside the document; not modelled. |
| F38 | LAW: Art 19.3, Law lines 441-444; Art 46, Law lines 917-932 | Late notice | — | The Law bars a late-notice exclusion where force majeure or an objective obstacle caused the delay, and Art 46.1 lets the insurer reduce the payment by the damage the delay caused it. General Condition 5's bar is total. Not resolved; the document is encoded as written. |
| F39 | LAW: Art 30, Law lines 706-717 | Time to submit claim documents | — | One year from the insured event, or from the third party's demand. The document states none. |
| F40 | LAW: Art 31, Law lines 718-729 | Time to pay | — | 15 days from receipt of complete, valid claim documents where the contract agrees none; interest on late payment. The document agrees none (F34). |
| F41 | LAW: Art 32, Law lines 730-734 | Disputes | — | Negotiation, then mediation, arbitration or court. The document provides a forum only for the amount (finding X11). |
| F42 | LAW: Art 48, Law lines 955-963 | Underinsurance | — | Proportion of the sum insured to market value at contracting, or as the contract agrees (Law line 962). Article I's completion value is a contractual basis; whether the Law permits a basis measured at a future date is open (question 5). |
| F43 | LAW: Art 49, Law lines 964-973 | Double insurance | — | Each insurer pays sum insured over total sums insured, where the total exceeds the market value. Would fill F17 in that case only. |
| F44 | LAW: Art 52, Law lines 997-1010 | Form of indemnity | — | Agreed by the parties, failing which in money. Section I gives the choice to Bảo Minh. |
| F45 | LAW: Art 59, Law lines 1090-1115 | Costs and the limit | — | Costs are paid on top of the limit unless otherwise agreed; Section II agrees otherwise (lines 278-279). |
| F46 | LAW: Art 22.2, Law lines 543-553 | Untrue answers | — | Avoidance needs an intentional untruth; General Condition 1 and General Condition 8's "khai báo sai" state no intent. Finding X18. |
| F47 | LAW: Art 8, Law line 231 | Compulsory construction insurance | — | Compulsory insurance in construction investment (Law line 231) is a separate regime; nothing in this wording says it is a compulsory policy. Not mixed in. |
| F48 | LAW: Art 53, Law lines 1011-1025 | Survey costs and disputes about the loss | — | The insurer pays for the survey; an independent assessor where the parties disagree. The document is silent on survey cost. |
| F49 | LAW: Arts 26-27, Law lines 623-678 | Non-payment of premium | — | A right to terminate, and liability for events before termination (Art 27.1(c)); the insuring agreement makes payment a condition (F2). Not resolved. |

## 4. Findings

The hostile reading: defects in the instrument as written, attacked as the policyholder's lawyer and as the insurer's.
"Evidence" names the assertion in `bmcar-findings.l4` (by its `§§` heading) or `bmcar-tests.l4` that shows the answer, or says `reading only`.

**X1. The recital never finishes its sentence.**
Lines 6-9: "(giấy yêu cầu bảo hiểm này được xem như)" deems the proposal to be nothing named, and "(Bản câu hỏi này …" never closes.
Scenario: the Insured argues a proposal statement is not a term because the deeming is incomplete.
Evidence: reading only.

**X2. The burden-of-proof clause names the wrong party.**
Lines 36-39 shift the burden of proving cover to the Insured where it is the Insured ("Người được bảo hiểm cho là") who contends exclusion (a) applies.
An Insured never contends that its own loss is excluded, so read as written the clause never operates, and the case that matters (Bảo Minh contends a riot or strike caused the loss) is not addressed.
Evidence: `bmcar-tests.l4`, `General Exclusions`: the Insured-contends case returns `the Insured`; the Bảo Minh-contends case is `#ASSERT REFUSED`.

**X3. Cover can begin before the Schedule's date.**
Lines 44-45 start liability on the site events "dù ngày quy định trong phụ lục có thể khác".
Scenario: Schedule from 1 March 2026; work began 15 February; a loss on 20 February is in the period.
Evidence: `bmcar-findings.l4`, `X3`.

**X4. Handed over but not in use, or in use but not handed over, stays on cover.**
Lines 47-48 need both ("bàn giao và đưa vào sử dụng").
Scenario: a floor occupied by the owner for months without a formal handover is still at the contractor's insurer's risk.
Evidence: `bmcar-findings.l4`, `X4` (payable 350 million in both cases).

**X5. A notice in time can still defeat the claim.**
General Condition 5(a) (line 89) requires notice "lập tức"; lines 102-104 allow 14 days before the bar; General Condition 1 (lines 57-60) makes every duty a condition precedent.
Scenario: notice received on day 2, found not to be immediate: within the 14 days, yet the claim fails.
Evidence: `bmcar-findings.l4`, `X5`.

**X6. A telegram is a condition precedent, and no causal link is needed.**
General Condition 4(b) (lines 76-77) requires a material change to be notified "bằng điện tín và bằng văn bản"; General Condition 5(a) requires a telephone call or a telegram as well as writing.
Scenario: a material change notified promptly in writing, every precaution taken; a later storm loss unconnected with the change fails under General Condition 1.
Whether a public telegram service still exists in Vietnam is outside knowledge, unverified; if it does not, the duty in 4(b) cannot be performed.
Evidence: `bmcar-findings.l4`, `X6` (both the 4(b) and the 5(a) cases).

**X7. The Insured must wait for an inspection and also repair without delay, and Bảo Minh controls the first clock.**
Lines 106-112 forbid repairing non-minor damage before an inspection or until a period "được xem là hợp lý" has passed, with no criteria; lines 114-115 end liability on an item not repaired "kịp thời".
A repair made early breaches a condition precedent; a repair made late loses the item's cover.
Evidence: reading only; the period is an input to the regulative rule (`bmcar-tests.l4`, two traces).

**X8. Arbitration can be stalled indefinitely.**
Lines 128-131 give each party one month to appoint, with no consequence for failing and no other way to constitute the tribunal; lines 133-134 make the award a condition precedent to any action.
Scenario: Bảo Minh does not appoint; 400 days later the duty is breached and the action is still barred.
Evidence: `bmcar-findings.l4`, `X8` (the trace ends `BREACH BY Bao Minh`; the bar asserts TRUE with no date input).

**X9. "Trọng tài chung" means two different people.**
Line 128 uses it for the single arbitrator the parties agree; lines 131-132 for the umpire the two arbitrators appoint; line 133's condition precedent is the award "của cuộc họp", which presupposes a meeting of three; line 140 starts General Condition 8's clock on an award of "hai Trọng tài viên hay Trọng tài chung".
General Condition 2 says a term keeps one meaning throughout.
Evidence: reading only (fork F16 takes an award by any of the three).

**X10. The General Condition 8 time-bar never reaches an outright rejection.**
Lines 138-141, as the Vietnamese has it, run three months only from an award; a claim rejected outright is a liability dispute, which General Condition 7 does not send to arbitration, so there is never an award and never a bar.
Scenario: rejected in 2026, no proceedings by 2031: not forfeited.
Evidence: `bmcar-findings.l4`, `X10`.

**X11. Liability disputes have no forum in the document.**
General Condition 7 (lines 126-127) sends only the amount to arbitration; nothing says where a dispute about liability goes.
Evidence: reading only (LAW F41).

**X12. "Rateable proportion" is undefined.**
Lines 143-145.
Evidence: `bmcar-tests.l4`, `General Condition 9`: the outcome of a claim with other insurance is `#ASSERT REFUSED`.

**X13. A limit referred to as "that" with nothing before it.**
Lines 158-159: "đối với mỗi sự cố sẽ không vượt quá hạn mức trách nhiệm bồi thường đó".
Evidence: reading only (F18 makes it an optional Schedule figure).

**X14. Exclusion (d) can swallow the works.**
The insuring clause (lines 153-154) distinguishes "hạng mục" (a Schedule item) from "bộ phận" (a part); exclusion (d) (lines 181-184) is limited to "những hạng mục bị ảnh hưởng trực tiếp"; General Condition 2 (lines 64-66) keeps a term's meaning.
Read so, a defect anywhere in the works makes item 1 "directly affected" and only other Schedule items are saved by the carve-back.
Scenario: a 20 million defective beam brings down 400 million of the works: 380 million on the component reading taken, nothing on the Schedule-item reading.
Evidence: `bmcar-findings.l4`, `X14`.

**X15. Insured at the new price, paid at the depreciated value.**
Article I (lines 210-211) requires plant to be insured at its replacement value new; Article 2(b) (lines 231-232) pays a total loss at actual value before the loss.
Scenario: plant worth 1.2 billion, 2 billion new, destroyed and replaced new: 1.2 billion paid on a premium charged on 2 billion; insured at 1.2 billion instead, the average cuts it to 720 million.
Evidence: `bmcar-findings.l4`, `X15`.

**X16. The average bites a small early loss.**
Item 1 must be insured at the full contract value "tại thời điểm hoàn thành việc xây dựng" (lines 206-208), and the average compares the sum insured with that (lines 217-220), whatever was at risk when the loss happened.
Scenario: works insured for 10 billion, completion value 12.5 billion, 1 billion built when 400 million is damaged: 320 million paid.
Evidence: `bmcar-findings.l4`, `X16`.

**X17. Nothing is paid until the Insured has paid for the repair or the replacement.**
Lines 234-236 pay only costs "thực tế phải gánh chịu"; lines 238-240 pay only after invoices show the work done; lines 114-115 end cover on an item not repaired promptly.
A contractor that cannot fund the repair receives nothing, and may then lose the item's cover.
Evidence: `bmcar-findings.l4`, `X17`.

**X18. A false declaration forfeits everything, with no intent stated.**
Line 136: "khai báo sai (được đưa ra hay hỗ trợ cho khiếu nại đó)"; "tất cả các quyền lợi" are lost (line 141).
An innocent mistake in a supporting document reads as a forfeiture.
Evidence: `bmcar-tests.l4`, `General Condition 8` (`a history with a false declaration` forfeits); LAW F46.

**X19. Bảo Minh may buy its way out of a third-party claim, with full discretion.**
Section II Condition 1 (lines 314-317) gives Bảo Minh "toàn quyền" over the defence and settlement; Condition 2 (lines 321-325) lets it pay "a lesser sum for which the claims can be settled" and be discharged.
Scenario: limit leaves 4 billion, Bảo Minh pays 2.5 billion; the claimant recovers more, or the defence costs more: the Insured's problem.
Evidence: `bmcar-findings.l4`, `X19`.

**X20. Terms that carry weight are never defined.**
General Condition 2 (lines 64-66) presupposes definitions, but the document defines nothing.
"sự cố" (occurrence: the unit of the deductible and the limits), "thay đổi quan trọng" (material change), "hư hỏng nhỏ" (minor damage), "bên thứ ba" (third party) and "công trường" (the site) are undefined; "hạng mục" and "Trọng tài chung" are used in two senses (X14, X9).
Evidence: reading only.

**X21. Drafting slips.**
"Điều I" (line 202) is followed by "Điều 2" and "Điều 3"; "dđòi hỏi" (line 204), "luơng bổng" (line 207), "băng" for "bằng" (lines 128, 211), "khôngg" (line 139), "khoảnmục" (line 220), "thoả thận" (line 306), "khởi nghiã" (line 23); line 302 reads "được bảo hiểm toàn bộ hay chỉ một theo Phần I", missing a word, which leaves exclusion 4(b)'s qualifier unclear.
Evidence: reading only.

**X22. Borrowed wording.**
Section II's insuring clause speaks of "xây dựng hay lắp đặt" (construction or erection, line 266), erection being the installation wording's subject; every page footer reads "(Munich Re)_03.06", which attributes the text to Munich Re and suggests a version "03.06" (its meaning is not stated).
Evidence: reading only; harmless to the Insured.

**X23. Discretion with no criteria over cover and premium.**
General Condition 4(b) (lines 79-80): after a material change "phạm vi bảo hiểm và/hoặc phí bảo hiểm sẽ được điều chỉnh một cách thích hợp".
Evidence: `bmcar-tests.l4`: `#ASSERT REFUSED` on the adjustment.

**X24. A stoppage anywhere in the chain of causes excludes the loss.**
General Exclusion (d) (line 34) with "trực tiếp hay gián tiếp" (lines 19-20).
Scenario: a storm damages a site idle during a suspension of work: excluded, because the stoppage is among the causes.
Evidence: `bmcar-findings.l4`, `X24`.

## 5. Answer table

The document states only these figures; everything else is the Schedule's.

| parameter | value | clause | src line | tested |
| --- | --- | --- | --- | --- |
| notice to reach Bảo Minh | 14 days from the day of the occurrence (calendar, day of occurrence not counted; F12) | General Condition 5 | 102-104 | day 14 in time, day 15 barred; across a month end and a year end |
| appointment of each arbitrator | one month from the day the written request is sent (F15) | General Condition 7 | 129-131 | 15 July → 15 August (31 days); 31 January → 28 February (28 days) |
| proceedings after an award | three months from the award (F16) | General Condition 8 | 139-140 | 30 September → 30 December; proceedings on 30 December in time, 31 December late |
| deductible | once per occurrence, Section I and Section II | Section I (a); Section II 1 | 173-174, 285 | below, at and above |
| total-loss switch | repair at or above the item's value before the loss | Article 2 | 240-242 | at, above, one VND below |
| average | sum insured / sum required, item by item | Article I | 217-220 | item 1 (with and without the principal's materials), item 2; at equality no average |

The order of the Section I arithmetic taken (F19-F21, F26): for each covered item, Article 2 basis (plus agreed Article 3 extras), limited to the cost actually incurred as recognised; less what the sum insured does not include and what exclusion (d) takes out; times the Article I ratio; capped at the item's sum insured.
Then for the occurrence: the sum of the items, less the deductible, plus debris clearance up to its separate sum, capped at any per-occurrence limit, capped at what remains of the Section's total sum insured.

## 6. What `check.sh` prints

Run on 2026-10-07, the last run, after every module was in its final form:

```
module                                    errors satisfied  failed  refused  expected
bmcar-findings.l4                              0        21       0        0         0
bmcar-fixtures.l4                              0         0       0        0         0
bmcar-general-conditions.l4                    0         0       0        0         0
bmcar-general-exclusions.l4                    0         0       0        0         0
bmcar-insuring-and-period.l4                   0         0       0        0         0
bmcar-nouns.l4                                 0         0       0        0         0
bmcar-section-1.l4                             0         0       0        0         0
bmcar-section-2.l4                             0         0       0        0         0
bmcar-tests.l4                                 0       189       0        0         0
TOTAL (9 modules)                              0       210       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

`check.sh` exit 0.

No failure or refusal is expected and none occurs.
The rule modules and the fixtures carry no assertions; the tests module carries 189 and the findings module 21, which matches the `#ASSERT` directives in each (`grep -c '^#ASSERT'`).
The 9 `#TRACE` directives are not counted by `check.sh`; each was read: the four General Condition 5 traces end `FULFILLED`, `BREACH BY the Insured`, `FULFILLED`, `FULFILLED`; the two General Condition 7 traces `FULFILLED` and `BREACH BY Bao Minh`; the two Section II Condition 1 traces `BREACH BY the Insured` and `FULFILLED`; the finding X8 trace `BREACH BY Bao Minh`.
To show the harness can fail, a scratch copy of the modules (without the findings module) with three expected values in `bmcar-tests.l4` deliberately altered (400,000,000 to 400,000,001; 320,000,000 to 400,000,000; 330,000,000 to 350,000,000) was run through the same `check.sh`.
It printed, for `bmcar-tests.l4`, `3 errors, 186 satisfied, 3 failed`, the line `TOTAL (8 modules) 3 186 3 0`, and exited 1.
The scratch copy was then deleted.
Twice during the session a run was killed by the host (exit 144) partway through `bmcar-tests.l4`, which takes several minutes; the runs recorded here were made in the background and completed.

## 7. The quotation check

The gate (the lead's clarification of 2026-10-07): the brief's command over every `.l4` and every `.md` in this directory except `BRIEF.md`, the lead's own file:

```
python3 -I tools/vnsrc.py check ../../source/raw/baominh-car.txt $(ls *.l4 *.md | grep -v '^BRIEF.md$')
vnsrc check: 256 src: lines, 584 Vietnamese runs, 0 problems
```

The brief's literal command, which also reads `BRIEF.md`, was run too:

```
python3 -I tools/vnsrc.py check ../../source/raw/baominh-car.txt *.l4 *.md
vnsrc check: 256 src: lines, 591 Vietnamese runs, 0 problems
```

The first is the gate.

## 8. Open questions for a domain expert

1. General Exclusions, lines 36-39: is "Người được bảo hiểm cho là" a translation slip for the insurer (X2), and if so, does a court read the clause as intended or as written?
2. General Condition 5: how are "lập tức" and "hư hỏng nhỏ" read in Vietnamese practice, and does Art 19.3 or Art 46 of the Law cut down the 14-day bar or General Condition 1's effect on it (F38)?
3. General Condition 8: is a rejected claim subject to any contractual time-bar, given the Vietnamese wording (X10), and does the Civil Code's limitation period then govern?
4. Section II: is one named Insured (the principal) a third party to another (the contractor)? The document has no cross-liability clause (F29).
5. Article I: does Law Art 48 permit an underinsurance basis measured at the completion of the works rather than at contracting (F42, X16)?
6. Exclusion (d): which meaning of "hạng mục" does Vietnamese practice give it (F22, X14)?
7. What "03.06" in the footer refers to, and whether a later edition of this wording exists (X22).
8. Whether the Schedule commonly entered with this wording states per-item deductibles, a per-occurrence limit, a debris sum and a Section II aggregate, which would settle F18, F21 and F30.
