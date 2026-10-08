# NOTES — OPES O-Car motor vehicle physical damage rules, encoding row `legalese-2026-10-vn-15`

OPES's "Quy tắc điều khoản sản phẩm bảo hiểm vật chất xe ô tô" (Decision 124/2019/QĐ-TGĐ, amended by the supplementary clauses of Decision 17/2022/QĐ-TGĐ), encoded in L4 by one agent in one session (run `VN-15-20261006`, agent `enc-vn-15`, 6-7 October 2026) from `BRIEF.md`.
Status: **draft**. No domain expert has read it against the source; HG1 has not been sought.

## 0. Build and run

Run on 2026-10-07 with `/Users/mengwong/.local/bin/l4` (a symlink to `~/.cabal/bin/l4`; no `--version`), sha256 `64bbcb157dbef2ef1020a6a75589313bba0a2aeeb807c921c5e65e62e9eca118`, `JL4_LIBRARY_PATH` unset.
Command, from this directory: `L4=/Users/mengwong/.local/bin/l4 ./check.sh`.

Totals: **18 modules, 0 errors, 349 satisfied, 0 failed, 0 refused** (the full output is in §6); `check.sh` exited 0.
`check.sh` counts `#ASSERT` outcomes only; the `#TRACE` directives in `ocar-tests-process.l4` were read by eye (§6).

## 1. What is encoded and what is not

**The file.** 27 PDF pages. Page 1 is the cover, page 2 the table of contents, pages 3-20 Articles 1-17 (src:55-986), pages 21-24 the supplementary clauses BS01-BS07 under their own heading (src:998-1129), pages 25-26 an undated clause on personal data (src:1141-1249), and page 27 a back cover that is an image with no text layer (the company's address, hotline and website, read from a rendering of the page; nothing on it is a rule).

**The two versions.** The heading names the 2019 rules and the 2022 supplementary clauses that amend them. The file holds them **side by side, not folded together**: Articles 1-17 are one body, the supplementary clauses another, and each supplementary clause says itself which base provision it cancels (BS03 cancels 12.12, BS04 cancels 14.1.2(a), BS05 cancels 12.15). The base text and the supplement are therefore separable, and are treated as two versions, chosen by an explicit input: the date the contract was concluded (forks F1, F2). What the file cannot show is whether Decision 17/2022 also edited the wording of Articles 1-17; no 2019 text is in the sources, so Articles 1-17 as printed are taken as the 2019 text. The personal data clause is a third, undated layer that cites a Decree of 17/04/2023, which the heading does not mention (fork F3).

**Encoded:** every Article of 1-17 that decides something, every supplementary clause BS01-BS07 and its general conditions, and clauses 7(b), 9 and 10 of the personal data clause. In summary: the vehicle definition (1.1), the sum-insured cap (1.10), time in use (1.15); the insurance period, transfer of ownership, termination and every refund (2-3); the parties' deadlines as regulative rules (3.1.3, 3.2.2, 3.2.3, 4.2, 5.2, 6, data clause 7(b)); assessment costs (7); the claim file (8); double insurance (9); the time limits (10); the perils, the costs and the cap (11); all 24 exclusions (12); valuation with its table (13); partial loss, depreciation in all four of its rules, replacement, repainting, total loss and salvage (14); the deductible (15); the reductions and the one-reduction rule (16); when a supplementary clause is in effect (17); and one module, `ocar-claim.l4`, that composes them into the amount payable.

**Not encoded, and why** (each a row of §2): the table of contents and the running headers; the back cover; the rights and duties in Articles 4 and 5 that restate another article or name conduct with no consequence of its own; the descriptions of how a market value is found (13.1), which are a valuation the caller supplies; the lists of data, purposes, recipients and risks in the personal data clause. **No figure in the encoding comes from anywhere but the text**; everything the rules leave to the contract or the certificate is an input with no default.

**Inputs.** `ocar-nouns.l4` declares them. The contract and certificate (`The policy`: period, sum insured, market value, deductible, premium, supplementary clauses with their figures, other policies), the vehicle (`The vehicle`), the loss as assessed (`The loss`, with `The circumstances of the loss`, `The load and speed`, `The conduct after the loss` and a list of `A damaged item`), earlier payments in the period, and, for the deadlines, a calendar of non-working days.

**Where the rules do not answer, the encoding declines** (`REFUSE`), by name: a contract before Decision 124/2019; a 2019 contract listing a supplementary clause other than BS01; 13.2 for a new or imported-new vehicle, or without the customs rate; tyre depreciation with no agreed rate; BS04 with no sub-limit, or beyond it; BS05's limit for a contract under 12 months; BS06 with no limit; a contract that states its own Article 16 reduction level; 3.2.2's refund when the premium was not paid in full; a pre-2023 contract said to carry the personal data clause.

## 2. Coverage table

Headings are as the document writes them. Totals: **68 encoded, 30 inert, 1 out-of-scope, 0 deferred (99 rows; a row may group several provisions, as its first cell says)**.

| provision | heading as written | English gloss | disposition | reason (for inert / out-of-scope) | where in the L4 |
| --- | --- | --- | --- | --- | --- |
| heading | Quy tắc điều khoản sản phẩm được ban hành theo Quyết định số 124/2019/QĐ-TGĐ | the rules and the two Decisions | encoded | — | `ocar-01-definitions.l4`: `the version of the rules governing` |
| contents | MỤC LỤC | table of contents | inert | a list of headings and page numbers; nothing in it is a rule | — |
| page headers | QUY TẮC ĐIỀU KHOẢN SẢN PHẨM | running header and page numbers on every page | inert | layout, repeated on each page | — |
| back cover | (image, no text layer) | address, hotline, website | out-of-scope | PDF page 27 is an image with no text layer, so nothing on it can be quoted or checked; it carries contact details only, and the hotline number the rules rely on is "ghi trên Hợp Đồng Bảo Hiểm/Giấy Chứng Nhận Bảo Hiểm" (src:319-320), not on this page | — |
| 1 chapeau | Các định nghĩa | definitions | inert | introduces 1.1-1.15 | `ocar-01-definitions.l4` |
| 1.1 | “Xe Ô Tô” | the motor car | encoded | — | `1.1 — a motor car within the definition`; used by `11 — the policy was in force for the loss` |
| 1.2 | “Chủ Xe” | the vehicle owner | inert | names a role; declared as `the Vehicle Owner` (`A party`) | `ocar-nouns.l4` |
| 1.3 | “Bên Mua Bảo Hiểm” | the policyholder | inert | names a role (`the Policyholder`) | `ocar-nouns.l4` |
| 1.4 | “Người Được Bảo Hiểm” | the insured | inert | names a role (`the Insured`) | `ocar-nouns.l4` |
| 1.5 | “Lái Xe” | the driver | inert | names a role (`the Driver`) | `ocar-nouns.l4` |
| 1.6 | “Xe Được Bảo Hiểm” | the insured vehicle | inert | the vehicle named in the certificate: `vehicle` of `The policy` | `ocar-nouns.l4` |
| 1.7 | “Phí Bảo Hiểm” | the premium | inert | an amount the contract fixes: `premium` | `ocar-nouns.l4` |
| 1.8 | “Mức khấu trừ” | the deductible | encoded | — | `1.8 — the amount after a deductible of` (`ocar-15-16-deductible-reductions.l4`) |
| 1.9 | “Giá Thị Trường” | market value | encoded | — | inputs `market value when insured`, `market value immediately before the loss`; 13.2 when not determined |
| 1.10 | “Số Tiền Bảo Hiểm” | the sum insured | encoded | — | `1.10 — the sum insured is not greater than the market value when insured` |
| 1.11 | “Hợp Đồng Bảo Hiểm” | the insurance contract | inert | names the contract; its terms are `The policy` | `ocar-nouns.l4` |
| 1.12 | “Giấy Chứng Nhận Bảo Hiểm” | the certificate | inert | names the document the inputs come from | `ocar-nouns.l4` |
| 1.13 | “Điều Khoản Bảo Hiểm Bổ Sung” | supplementary clause | inert | names the clauses BS01-BS07 encode | `ocar-17-supplementary.l4` |
| 1.14 | “Công Ty Bảo Hiểm” | the Insurer | inert | names a party (`the Insurer`) | `ocar-nouns.l4` |
| 1.15 | “Thời Gian Sử Dụng Xe Ô Tô” | time in use | encoded | — | `1.15 — the time in use of the vehicle, in months` |
| 2.1 | Thời hạn bảo hiểm | the insurance period | encoded | — | `2.1 — the date falls within the insurance period of`, `2.1 — the insurance period lasts at least` / `more than` |
| 2.2 | Phí bảo hiểm | the premium is paid as agreed | inert | states that the contract fixes payment; the consequences are 3.1 | — |
| 2.3 | Kê khai thông tin khi yêu cầu bảo hiểm | (heading) declaration when applying; (text) transfer of ownership | encoded | — | `2.3 — the benefits pass to the transferee`, `2.3 — the refund on a transfer without the benefits` |
| 3.1.1 | Chấm dứt Hợp Đồng Bảo Hiểm do vi phạm thời hạn thanh toán | termination for late premium | encoded | — | `3.1.1 — the date the contract terminates for late premium` |
| 3.1.2 | (3.1.2) | premium owed to termination | encoded | — | `3.1.2 — the premium owed up to termination` |
| 3.1.3 | (3.1.3) | 70% refund of overpayment, within 5 working days | encoded | — | `3.1.3 — the refund after termination for late premium`, `3.1.3 — the Insurer's duty to refund` |
| 3.2.1 | Đơn phương chấm dứt Hợp Đồng Bảo Hiểm trước thời hạn | unilateral termination on 5 working days' notice | encoded | — | `3.2.1 — the earliest date a termination noticed on` |
| 3.2.2 | (3.2.2) | the Policyholder terminates: 70% | encoded | — | `3.2.2 — the refund on the Policyholder's termination`, `3.2.2 — the date the contract ends ...`, `3.2.2 — the Insurer's duty to refund` |
| 3.2.3 | (3.2.3) | the Insurer terminates: 100% | encoded | — | `3.2.3 — the refund on the Insurer's termination`, `3.2.3 — the Insurer's duty to refund` |
| 3.2.3 last paragraph | Mọi khoản chi phí phát sinh liên quan đến việc hoàn trả | refund costs borne by the Policyholder (3.1.3, 3.2.2) | encoded | — | `the cost of making the refund` in 3.1.3 and 3.2.2 |
| 4.1 | Công Ty Bảo Hiểm có quyền | the Insurer's rights | inert | each restates a rule encoded where it has effect (2.2, 3.1, 11-12, 16) or the right of recourse against a third party, which pays the Policyholder nothing; quoted with pointers | `ocar-04-05-06-duties.l4` |
| 4.2, bullets 1-2 | Công Ty Bảo Hiểm có nghĩa vụ | explain the terms; issue the certificate | inert | no deadline and no amount turn on them | `ocar-04-05-06-duties.l4` |
| 4.2, bullet 3 | Trả tiền bồi thường bảo hiểm trong vòng 15 ngày làm việc | pay within 15 / 30 working days | encoded | — | `4.2 — the Insurer's duty to pay`, `4.2 — the working days to pay` |
| 4.2, bullet 4 | Trong trường hợp Công Ty Bảo Hiểm không đủ thẩm quyền để xác minh | file complete on the authority's conclusion; refusal explained in 15 working days; 90 days | encoded | — | `4.2 — the date the file counts as complete`, `4.2 — the Insurer's duty to explain a refusal`, `4.2 — the Insurer verifies by itself and may consider settling` |
| 4.2, bullets 5-7 | Phối hợp chặt chẽ | cooperate; advance costs of serious losses; guide on documents | inert | cooperation and guidance have no measurable content; the advance is a permission ("có thể") with no amount, deadline or criterion, so nothing turns on it | `ocar-04-05-06-duties.l4` |
| 4.2, bullet 8 | Trong vòng 05 ngày làm việc | re-assess within 5 working days of a change | encoded | — | `4.2 — the Insurer's duty to re-assess after notice of a change on` |
| 4.2, bullet 9 | Các nghĩa vụ khác | other duties under law | inert | points outside the rules | — |
| 5.1 | Bên Mua Bảo hiểm, Người Được Bảo Hiểm có quyền | the Policyholder's rights | inert | each is the counterpart of a duty in 4.2 or a right in 2.3 and 3.2 | `ocar-04-05-06-duties.l4` |
| 5.2, bullets 1-4 | Bên Mua Bảo hiểm, Người Được Bảo Hiểm có nghĩa vụ | declare, pay, allow inspection, obey traffic law | inert | their consequences are set by 3.1, 12, 16.1.6; inspection before issue has no consequence stated | `ocar-04-05-06-duties.l4` |
| 5.2, bullet 5, first + | Thông báo ngay cho Công Ty Bảo Hiểm | tell the Insurer at once, mitigate, protect the scene, tell the police | encoded | — | through 16.1.1 bullet 2 and 12.23 |
| 5.2, bullet 5, second + | Không được di chuyển xe | do not move or repair before consent; deemed consent after 5 working days | encoded | — | `5.2 — the duty not to move, dismantle or repair before the Insurer agrees` |
| 5.2, bullet 5, third + | Trong thời hạn năm (5) ngày làm việc kể từ ngày xảy ra tổn thất | notify within 5 working days | encoded | — | `5.2 — the duty to notify the loss`, `5.2 — the loss was notified in time` |
| 5.2, bullets 6-9 | Cung cấp các tài liệu trong hồ sơ bồi thường | documents; truthfulness; the third-party claim; hand over parts | inert | their effect is set by 8, 12.22, 16.1.4 and 14.3.1, where they are encoded | `ocar-04-05-06-duties.l4` |
| 5.2, bullet 10 | trong vòng 24 giờ phải thông báo cho Công Ty Bảo Hiểm | theft or disaster loss: 24 hours | encoded | — | `5.2 — the duty to notify the Insurer of a theft or a disaster loss within 24 hours` |
| 5.2, bullet 11 | Thực hiện các các nghĩa vụ khác | other duties under law | inert | points outside the rules | — |
| 6 | Thay đổi yếu tố làm cơ sở tính phí bảo hiểm | changes in the rating factors | encoded | — | `6 — the duty to notify a change ...`, `6 — the Insurer's duty to answer ...`, `6 — the Policyholder may terminate under 3.2.2`, `6 — the Insurer may terminate under 3.2.3` |
| 7 | Giám định tổn thất | loss assessment | encoded | — | `7 — the party who pays for the Insurer's assessment`, `7 — the party who pays for the independent assessment and the court fees` |
| 8 chapeau | Hồ sơ bồi thường | the claim file: "one or more" of | encoded | — | `8 — the documents the claim file may include, for` |
| 8.1 | Tài liệu do Bên Mua Bảo Hiểm/ Người Được Bảo Hiểm cung cấp | documents the Policyholder provides | encoded | — | same |
| 8.2 | Tài liệu do Công Ty Bảo Hiểm phối hợp | documents the Insurer helps collect | encoded | — | same |
| 8.3 | Trường hợp xe bị mất trộm, mất cướp toàn bộ | theft of the whole vehicle | encoded | — | same |
| 9 | Bảo hiểm trùng | double insurance | encoded | — | `9 — the Insurer's share under double insurance, on` |
| 10, claims | Thời hạn yêu cầu bồi thường | one year to claim | encoded | — | `10 — the last day to claim, for an event on` |
| 10, complaints | Thời hạn khiếu nại | 90 days to complain | encoded | — | `10 — the last day to complain, notice received on` |
| 10, suit | Thời hiệu khởi kiện | 3 years to sue | encoded | — | `10 — the last day to sue, the dispute having arisen on` |
| 10, forum | Mọi tranh chấp phát sinh từ Hợp Đồng Bảo Hiểm | a competent court in Vietnam | inert | a forum with no condition; quoted | `ocar-07-10-claims-process.l4` |
| 11.1 | Phạm vi bảo hiểm và Quyền lợi bảo hiểm | the perils | encoded | — | `11.1 — the peril is one the cover lists, on`, `11 — the policy was in force for the loss, on` |
| 11.2 | Ngoài ra, Công Ty Bảo Hiểm còn thanh toán | costs besides the indemnity | encoded | — | `11.2 — the costs payable besides the indemnity, for` |
| 11.2, last bullet | Trong mọi trường hợp | not more than the sum insured | encoded | — | `11.2 — capped at the sum insured of` |
| 12 chapeau | Loại trừ trách nhiệm bảo hiểm | exclusions, save where a supplementary clause extends cover | encoded | — | `12 — the supplementary clause ... extends the cover on` |
| 12.1-12.10 | (12.1) to (12.10) | deliberate act; inspection; licence; alcohol and drugs; prohibited manoeuvres; prohibited parking; practice, racing, towing; goods; outside Vietnam; war and riot | encoded | — | `12.1 — applies to` ... `12.10 — applies to`; `12 — the exclusions of the event, on` |
| 12.11-12.15 | (12.11) to (12.15) | wear and defects; water in the engine; electrical and mechanical breakdown; tyres, keys and the like; loss of parts | encoded | — | `12.11 — applies to the item` ... `12.15 — applies on`; `12 — the exclusions of the item, on` |
| 12.16-12.18 | (12.16) to (12.18) | fraud; own special equipment; overload of 50% or more | encoded | — | `12.16`, `12.17`, `12.18 — applies to` |
| 12.19 | (12.19) | added equipment | encoded | — | `12.19 — applies on` |
| 12.20 | (12.20) | at or below the deductible | encoded | — | `12.20 — applies to an amount of` |
| 12.21-12.24 | (12.21) to (12.24) | speeding over 50%; untruthful claim; consequential loss; unreinspected conversion | encoded | — | `12.21`, `12.22`, `12.23 — applies to the item`, `12.24` |
| 13.1 | Nguyên tắc xác định số tiền bảo hiểm | insuring at or below value; how the market value is found | inert | describes a valuation the caller supplies as `market value when insured`; the "at or below" rule is 1.10, encoded there | `ocar-13-valuation.l4` |
| 13.2 (i)-(ii) and table | Trường hợp Bên Mua Bảo Hiểm và Công Ty Bảo Hiểm không xác định được Giá Thị Trường | value by formula | encoded | — | `13.2 — the value of the vehicle when insured, by formula, on`, `13.2 — the minimum remaining-quality rate ...` |
| 13.2 last bullet | Giá trị khai báo | declared value; under- and over-insurance | encoded | — | `13 — insured below value, on`, `13 — insured above value, on` |
| 14.1.1 | Đối với tổn thất bộ phận | what is paid for a partial loss | encoded | — | `14.1 — the cost allowed, on`; (b) through 11.2 |
| 14.1.2(a)-(b) | Cách xác định số tiền bồi thường | under-insurance; depreciation; listed uses; used parts | encoded | — | `14.1.2 — the indemnity for the partial loss on`, `14.1.2(b) — ...` |
| 14.1.2(c) | (c) | with the no-depreciation clause | encoded | — | `14.1.2(c) — the no-depreciation clause relieves, on` |
| 14.1.2(d) | (d) | always depreciated; glass never | encoded | — | `14.1.2 — the depreciation rate, on`, `14.1.2(d) — ...` |
| 14.1.2(e) | (e) | other cases as agreed | inert | refers to agreements outside the rules; none is an input | `ocar-14-settlement.l4` |
| 14.1.3 | (14.1.3) | replacement only if irreparable or over 50% | encoded | — | `14.1.3 — replacement with a new part is accepted for` |
| 14.1.4 | (14.1.4) | repainting over 50% | encoded | — | `14.1.4 — the cost of repainting allowed for` |
| 14.2.1-14.2.3 | Đối với tổn thất toàn bộ | total loss | encoded | — | `14.2.1 — ...`, `14.2.2 — ...`, `14.2.3 — the indemnity for a total loss, on` |
| 14.3 chapeau, 14.3.1, 14.3.3 | Thu hồi tài sản sau bồi thường | the Insurer owns replaced parts and recovered stolen vehicles | inert | who owns the salvage; no amount turns on it | `ocar-14-settlement.l4` |
| 14.3.2 | (14.3.2) | the wreck after a total loss | encoded | — | `14.3.2 — the share of the wreck the Insurer takes, on`, `14.2 and 14.3.2 — the indemnity for the total loss, on` |
| 15.1-15.2 | Mức khấu trừ | the deductible | encoded | — | `15 — the deductible on`, `15 — the deductible for a partial loss, on` |
| 16 chapeau | Giảm trừ bồi thường | reductions; a contract-stated level | encoded | — | `16.1 lets the contract state a reduction level, but its comparative is incomplete` |
| 16.1.1-16.1.6 | (16.1.1) to (16.1.6) | the six grounds of reduction | encoded | — | `16.1 — the reductions open to the Insurer, on` and the rule per ground |
| 16.2 | Nguyên tắc giảm trừ số tiền bồi thường | one reduction, the highest | encoded | — | `16.2 — the highest rate the Insurer may apply, on`, `16 — the Insurer may apply a reduction, on` |
| 17 | Điều khoản bảo hiểm bổ sung | supplementary clauses: in effect when paid and accepted | encoded | — | `17 — the supplementary clause ... is in effect on` |
| BS heading | Điều khoản bảo hiểm bổ sung | general conditions of the supplementary clauses | encoded | — | same; the two conditions hold by construction |
| BS01 | Bảo hiểm không tính khấu hao phụ tùng | no depreciation | encoded | — | `BS01 — the clause leaves this kind of part to depreciation` |
| BS02 | Bảo hiểm lựa chọn cơ sở sửa chữa | choice of repair shop | encoded | — | `BS02 — the Insured may choose the repair shop`, `BS02 — the repair cost OPES accepts` |
| BS03 | Bảo hiểm xe bị ngập nước | flood damage | encoded | — | `BS03 — the deductible on`; 11.1, 12.12, 12.13 |
| BS04 | Bảo hiểm bồi thường theo giới hạn trách | settlement up to a limit of liability | encoded | — | `BS04 — the partial-loss indemnity on` |
| BS05 | Bảo hiểm mất bộ phận | loss of parts | encoded | — | `BS05 — the number of parts losses covered on`, `BS05 — the deductible on`; 11.1, 12.15 |
| BS06 | Hành trình bình an | safe journey | encoded | — | `BS06 — the safe-journey benefit on` |
| BS07 | Bảo hiểm cho thiết bị được cải tạo, cơi nới | added equipment | encoded | — | `BS07 — covers the added item` |
| data clause, opening | Điều khoản bổ sung về thu thập và bảo vệ dữ | who collects whose data, for what | inert | a statement of practice; no rule of the contract turns on it | `ocar-personal-data.l4` |
| data clause 1-6 | Nội dung Dữ liệu cá nhân cơ bản | data collected, purposes, methods, recipients, risks | inert | lists that describe the processing; nothing in the contract turns on them; quoted by heading only | `ocar-personal-data.l4` |
| data clause 7(a) | Thời gian bắt đầu | processing starts with consent | inert | a starting point with no consequence in the contract | `ocar-personal-data.l4` |
| data clause 7(b) | Thời gian kết thúc | processing ends within 72 hours of a request to delete | encoded | — | `data clause 7(b) — the Insurer's duty to stop processing ...` |
| data clause 8 | Chủ thể dữ liệu có các quyền | rights under Decree 13/2023 | inert | the rights are the Decree's, which is not in the sources | `ocar-personal-data.l4` |
| data clause 9 | Trường hợp Chủ thể dữ liệu không đồng ý | no consent, no contract | encoded | — | `data clause 9 — the contract stands, on` |
| data clause 10 | Trường hợp Chủ thể dữ liệu đã đồng ý | exercising a right ends the contract as 3.2.2 | encoded | — | `data clause 10 — the contract ends, on`, `data clause 10 — the refund, on` |

**Layout artefacts of the text layer** (the PDF has a text layer; this is `pdftotext -layout`, not OCR, so there are no character errors to correct): the headings of Articles 2, 5 and 10 are split across lines with "Điều N:" between their halves (src:131-134, 281-284, 529-532); the 13.2 table has its bullet marks moved to the ends of lines ("85% o", src:748-750); 1.6 and 1.12 wrap mid-word ("Bảo / Hiểm"); BS03 and BS05 cite "Khoản 12. 12" and "Khoản 12. 15" with a space. None changes a reading; every `src:` line quotes the rendering as it is.

## 3. Fork register

Each ambiguity met, the readings seen, the one taken and the text that licenses it. "LAW" marks a fork where the Law on Insurance Business 08/2022/QH15 (the aid, `.aids/law-08-2022-qh15.txt`) fills or conflicts with the rules; its line numbers are that file's. Statements about Vietnamese law not cited to it are outside knowledge, unverified.

| # | where (src) | the question | readings | taken, and why |
| --- | --- | --- | --- | --- |
| F1 | heading, src:5-7 | Which version governs a policy? | (i) the one in force when the contract was concluded; (ii) at the date of the loss; (iii) at the start of the period | **(i)**: the contract incorporates the rules issued with it; 1.15 already makes the contract month operative. An explicit input, `date the contract was concluded`. |
| F2 | heading, src:5-7 | From when is each Decision in force, and did 17/2022 edit Articles 1-17? | (i) from its date; Articles 1-17 unedited; (ii) a later commencement; edits folded in | **(i)**: the dates are the only ones the file gives; the 2022 instrument is described as amending "theo Điều khoản bảo hiểm bổ sung" (by the supplementary clauses), and the clauses state their own overrides. No 2019 text is in the sources to compare. |
| F3 | data clause, src:1141-1249 | When does the undated personal data clause apply? | (i) when the contract says it is part of it, never before 17/04/2023; (ii) to every contract | **(i)**: it cites Decree 13/2023 of 17/04/2023 (src:1234-1235), so it cannot be older; the heading does not name it. An input; an earlier contract that claims it is declined. |
| F4 | 9 with 14.1.2(a), src:517-523, 785-787 | Under double insurance, is the share applied on top of the under-insurance ratio? | (i) both; (ii) only one | **(i)**: each is stated without regard to the other. Finding X22 shows the result. |
| F5 | 14.1.2(c), src:823-827; 17 | A 2019 contract listing BS01, or another clause? | (i) BS01 is the clause 14.1.2(c) names, with (c)'s effect; the others' 2019 text is missing; (ii) apply the 2022 text | **(i)**: (c) is part of the base text; the 2022 texts may not be borrowed for 2019. Others declined. |
| F6 | 3.1.3, 3.2.2, src:176, 189 | What is a "sự kiện bảo hiểm" (insured event)? | (i) any event within the scope of cover, paid or not; (ii) only one giving rise to payment | **(i)**: 3.2.2 lists "or liability to pay has arisen" as a separate limb, so the event alone suffices. An input. Finding X25. |
| F7 | 3.1.3, 5.2, 10 | Is day X counted in "kể từ ngày X"? | (i) no; (ii) yes | **(i)**: the period runs from the day after. Outside knowledge, unverified: Vietnam's Civil Code is said to count this way. |
| F8 | 3.1.3, 3.2.1, 4.2, 5.2, 6 | What is a working day? | — | **an input**: the rules do not define it; the caller supplies the non-working days, weekends and holidays alike. The tests use a hypothetical calendar. |
| F9 | 1.15, src:126-129 | Months "from month A to month B": B-A or B-A+1? | (i) B-A; (ii) inclusive | **(i)**: a car registered in January 2025 and insured in January 2026 has one year's use, not thirteen months. |
| F10 | 13.2, 14.1.2(b), src:747, 795 | "Thời gian đã sử dụng" and "Xe sử dụng" are not the defined term. Measured to when? | (i) as 1.15, to the contract month; (ii) to the loss | **(i)**: 1.15 is the only definition. Finding X11. |
| F11 | 3.1.2, 3.2.2, 3.2.3 | How is "the premium for the remaining period" computed? | (i) pro rata by calendar days, the day of termination used; (ii) by months; (iii) short-period scale | **(i)**: the period is stated in dates; nothing names a scale. |
| F12 | 2.3, src:139-148 | Do the benefits pass automatically, and which Article 3 refund applies? | (i) by default, unless the Policyholder asks for a refund, which is 3.2.2's; (ii) 3.2.3's 100% | **(i)**: it is the Policyholder's request. |
| F13 | 3.1.3, src:170-175 | 70% of (paid less owed), or 70% of paid less owed? | (i), (ii) | **(i)**: "70% phần Phí Bảo Hiểm ... đã đóng thừa" is the overpaid part, after deducting what 3.1.2 says is owed. |
| F14 | 3.2.2, src:184-190 | 70% of which premium, when it has not all been paid? | — | **declined**: not addressed. |
| F15 | BS03, BS05, src:1054-1057, 1100-1103 | Do their deductibles replace 15.2's, and on which losses? | (i) replace, on any loss resting on the clause (its peril, or an item only its cancellation lets in); (ii) add | **(i)**: "áp dụng riêng cho Điều Khoản ... này" (applied specifically to this clause). |
| F16 | 12 chapeau, src:591-592 | Must an excluded circumstance cause the loss? | (i) no more than each limb's words ask ("khi", while; "do", caused by); (ii) always causation | **(i)**: the chapeau reaches losses "có liên quan tới" (connected with) the matters. Finding X29. |
| F17 | 11.1, src:553-554 | Must every peril be "sudden and unforeseeable"? | (i) yes, except the natural catastrophe; (ii) only accidents | **(i)**: the chapeau qualifies the cases that follow; a catastrophe of nature is "thiên tai" in the same phrase. |
| F18 | 11.2, 14.1.1(b) | Are 11.2's costs reduced by under-insurance, the deductible or Article 16? | (i) no; (ii) yes | **(i)**: "Ngoài ra" (besides); the Law's Article 51(3) (lines 991-996) pays such costs in addition to the indemnity. Only the cap reaches them. |
| F19 | 11.2 last bullet, src:583-584 | Per loss or in aggregate? | (i) per loss; (ii) aggregate | **(i)**: BS04 says "tổng số tiền bồi thường" (total) where it means an aggregate. |
| F20 | 12.2(iii), src:603-605 | Count children under 7 for "không chở quá số người quy định"? | (i) no, as 12.18; (ii) yes | **(i)**: the same document counts persons that way for the same certificate. |
| F21 | 12.13, BS03, src:652-656, 1051-1053 | BS03 covers flood electrical damage; 12.13 excludes short-circuit damage "whatever the cause" and is not cancelled. | (i) BS03 prevails for a flood-water loss; (ii) 12.13 prevails | **(i)**: specific over general, and LAW L1 (Article 24, line 588: an unclear term favours the Policyholder). Finding X9. |
| F22 | 13.2, src:742-751 | Does the table apply to (ii)? | (i) no, (ii) uses the customs rate; (ii) yes | **(i)**: (ii) names its own source of the rate. |
| F23 | 13.2(ii), src:742 | "Nhập khẩu đã qua sử dụng": used abroad, or imported and used since? | (i) used abroad; (ii) either | **(i)**: as 1.15 (src:127-128); only a used import has a customs remaining-quality rate. Finding X10. |
| F24 | 15.2, src:897-900 | A contract deductible below 500,000? | (i) raised to 500,000; (ii) as written | **(i)**: "tối thiểu và bắt buộc" (minimum and mandatory). |
| F25 | 1.8, 15.1, 15.2 | A deductible on a total loss? | (i) no; (ii) yes | **(i)**: 15.1 limits it to partial losses, and LAW L1. Finding X15. |
| F26 | 16.1.3, 5.2 | Does five working days' silence count as approval for 16.1.3? | (i) yes; (ii) no | **(i)**: 5.2 permits the repair then; a reduction for a permitted act would be a trap. Finding X17. |
| F27 | 16.1.5, src:962-964 | Overload of a mixed vehicle; counting children? | (i) the higher of load and persons; children counted; (ii) other | **(i)**: the text gives no rule for mixed vehicles; it does not leave children out. Finding X4. |
| F28 | 14.1.2(d), src:832-833 | "Năm sử dụng đầu tiên (từ năm đăng ký lần đầu)" | (i) the calendar year of first registration; (ii) twelve months | **(i)**: "from the YEAR of first registration". |
| F29 | 14.1.2(c), (d), BS01 | A battery with the no-depreciation clause? | (i) depreciated, (d) "in every case"; (ii) not | **(i)**. Finding X2. |
| F30 | 14.3.2, src:882-888 | Under-insured, Owner keeps the wreck: reduce by the whole wreck value or the Insurer's share? | (i) the share; (ii) the whole | **(i)**: the same sentence limits the Insurer's recovery to the insured share. |
| F31 | 9, 11.2, 14, 15, 16 | In what order are the layers applied? | (i) Article 14, then the Article 9 share, then the deductible (partial losses), then the one reduction, then 11.2 costs, then the cap; (ii) other orders | **(i)**: 1.8 takes the deductible from the amount "thuộc trách nhiệm bảo hiểm" (within the Insurer's liability), which the share and the ratio define; Article 16 reduces "số tiền bồi thường" (the indemnity). |
| F32 | 5.2, src:351-356 | 24 hours from when? | (i) from learning of it; (ii) from the event | **(i)**: one cannot report what one does not know. The rule's clock starts at that moment; the encoding takes no position on when that is. |
| F33 | 10, src:533-535 | One year, and excused delay | (i) the calendar anniversary, delay added day for day | **(i)**. LAW L5. |
| F34 | 10, src:543-545 | When does a dispute "arise"? | — | **an input**. |
| F35 | BS06 | Is the BS06 benefit inside the sum-insured cap? | (i) no; (ii) yes | **(i)**: 11.2's cap names the costs of 11.1 and 11.2 only. |
| F36 | 16.2, src:973-976 | "Theo tỷ lệ cao nhất" when the grounds are ranges | (i) the ground with the highest ceiling, at a rate within its range, or none; (ii) the highest rate of every ground's lower bound | **(i)**. |
| F37 | 14.2.2, src:853-856 | A theft without a judgment or decision | (i) nothing payable yet (0); (ii) declined | **(i)**: the rule states the condition; until it holds the answer is "not yet". |
| F38 | Article 7, src:410-424 | "Khác với" (differs) | (i) any difference in cause or extent; (ii) a material one | **(i)**: no threshold is stated. Finding X23. |
| F39 | 16.1.1, src:919-920 | "Năm (5) ngày" | (i) calendar days; (ii) working days as in 5.2 | **(i)**: the words differ from 5.2's. Finding X3. |
| F40 | 3.1.1, src:162-166 | Is the last day for paying covered? | (i) yes: the contract ends "ngay khi kết thúc thời hạn thanh toán", at the end of that day | **(i)**. |
| L1 | Law Art 24, line 588 | Ambiguity | — | An unclear term is construed for the Policyholder. Used as a tie-break in F21, F25; not encoded. |
| L2 | Law Art 31(1), lines 719-724 | Payment period | — | The Law's 15 days applies only where the contract agrees none; 4.2 agrees 15 working days, so 4.2 governs. |
| L3 | Law Art 26, lines 623-635; rules 3.2.1 | Unilateral termination "theo quy định pháp luật" | (i) the contract's own free right (3.2.2, 3.2.3); (ii) only the Law's grounds | **(i)**, with the conflict recorded: the Law lists grounds; the rules grant the right without them. |
| L4 | Law Art 52(2), lines 1004-1006; rules 14.1.1(a) | Who chooses the form of settlement? | — | The rules give it to the Insurer; the Law settles in cash where the parties do not agree. Recorded; no amount turns on it. |
| L5 | Law Art 30(2), lines 711-714; rules 10 | Claim period where the Insured did not know of the event | — | The Law runs the year from knowledge; the rules do not say so. Recorded, not encoded. |
| L6 | Law Art 49(1), lines 964-968; rules 9 | Definition of double insurance | — | The Law requires the total sums insured to exceed the market value; Article 9 does not. Encoded as the rules say; finding X22. |
| L7 | Law Art 53(2), lines 1020-1025; rules 7 | Binding effect of an independent assessment | — | The Law binds the parties to any independent assessor's conclusion; the rules state it only for a court-appointed one. Recorded. |
| L8 | Law Art 26(1), lines 627-628; rules 3.1.1 | A grace period for premium | — | The Law contemplates termination after a grace period for paying the premium (line 628); 3.1.1 ends the contract at once. Recorded; finding X28. |

## 4. Findings

A finding is a defect in the instrument as written. Each has its source lines, a minimal scenario and the evidence (the assertion in `ocar-tests-findings.l4`, or "reading only").

| # | finding | source | scenario | evidence |
| --- | --- | --- | --- | --- |
| X1 | **Exercising a statutory data right ends the cover at a 30% loss.** If any data subject (the Policyholder, but also the Insured or a beneficiary) exercises a right under clause 4, 5, 6 or 8 of Article 9 of Decree 13/2023, the contract ends from the request and is treated as the Policyholder's own termination: 70% of the unexpired premium, and nothing at all if an insured event has happened. | data clause 10, src:1242-1249; 3.2.2, src:184-190 | Premium 12,000,000 for 2026; the Insured asks on 1 July under clause 5. | `ocar-tests-findings.l4` §X1: refund 70% x 12,000,000 x 183/365; 0 after a loss. |
| X2 | **The battery is both relieved of and subject to depreciation.** 14.1.2(c) and BS01 list what the no-depreciation clause still depreciates and leave the battery out; 14.1.2(d) depreciates the battery "in every case". | src:823-833, 1017-1023 | BS01 in force; battery replaced new for 10,000,000. | §X2: 5,000,000 under fork F29; the two lists asserted not to contain it. |
| X3 | **A notice that meets 5.2 is still late under 16.1.1.** 5.2 allows five WORKING days; 16.1.1 reduces the indemnity by 5-10% where notice is not sent within five DAYS. A loss on a Wednesday notified the next Wednesday is in time for one and late for the other. | src:330-332, 917-923 | Loss 10 June 2026, notice 17 June. | §X3: 5.2 met; 16.1.1 applies; least payable 8,550,000 of 9,500,000. |
| X4 | **One more passenger, a child, removes the reduction.** 12.18 does not count children under 7; 16.1.5 does. Seven adults in a five-seat car: 40% over by either count, no exclusion, a 40% reduction. Add a child: 12.18 still sees 40% (no exclusion), 16.1.5 sees 60%, which is not "under 50%", so no reduction. The more overloaded car is paid in full. | src:683-688, 962-964 | Collision repaired for 10,000,000. | §X4: 5,700,000 with 7 adults; 9,500,000 with 7 adults and a child. |
| X5 | **Termination on notice, or on receipt.** 3.2.1 requires notice at least five working days before the termination; 3.2.2 ends the contract when the Insurer receives the notice. | src:179-183, 190-192 | Notice received Monday 5 October 2026. | §X5: 12 October under 3.2.1; 5 October under 3.2.2. |
| X6 | **Untruthful claim documents: the whole claim, or at most 30%.** 12.22 excludes the loss where the Insurer PROVES the information untruthful or forged; 16.1.4 reduces by up to 30% where the Owner was untruthful, with no proof required. The same conduct has two consequences and the Insurer can choose its burden. | src:698-701, 950-951 | Collision repaired for 10,000,000. | §X6: 0 under 12.22; 6,650,000 at least under 16.1.4. |
| X7 | **BS04 cancels the under-insurance rule and leaves a hole beyond its sub-limit.** It settles at full value "until" the sub-limit is reached; it cancels 14.1.2(a) without condition; nothing says how a partial loss is settled after that, or the part of a loss above what remains. | src:1063-1076 | Sub-limit 100,000,000, 90,000,000 paid, a 20,000,000 loss. | §X7: declined. |
| X8 | **BS05 has no limit for a contract under 12 months.** 2 losses for 12-18 months, 3 for over 18, nothing for less. | src:1097-1099 | A six-month contract with BS05. | §X8: declined. |
| X9 | **BS03's electrical cover against 12.13's "whatever the cause".** BS03 extends the cover to electrical damage from driving into flood water and cancels only 12.12; 12.13 excludes electrical damage from a short circuit "do bất kỳ nguyên nhân nào". Read literally, the extension is largely empty; the encoding lets BS03 prevail (F21). Without BS03, a natural-catastrophe flood that shorts the electrics is excluded although the flood is an insured peril. | src:652-656, 1049-1053 | Flood-shorted electrics repaired for 8,000,000. | §X9: excluded by 12.13 on the plain policy; not excluded with BS03 (fork). |
| X10 | **No value for a vehicle imported new.** 13.2 values a used car made in Vietnam (i) and one imported after use abroad (ii); a new car, or one imported new and used here since, whose market value cannot be determined has no rule. | src:736-744 | An imported-new car, market value not determined. | §X10: declined. |
| X11 | **The defined "time in use" is never used, and fixes the age at the contract month.** 13.2 and 14.1.2(b) use other words; read as 1.15 (F10), depreciation on an 18-month BS05 contract, or a loss late in the year, uses the age at inception. | src:126-129, 747, 795 | — | reading only |
| X12 | **"Người Thụ Hưởng" is used as a defined term and never defined.** | src:111, 1146 | — | reading only |
| X13 | **2.3's heading does not match its text, and its two sentences pull apart.** Headed "declaring information when applying", it deals with transfer of ownership; it says benefits pass "mặc nhiên" (automatically) and then that the Policyholder may decline to pass them. | src:139-148 | — | reading only (fork F12) |
| X14 | **Article 16 is a discretion without criteria.** Each ground gives a range ("từ 05% đến 10%", "tối đa 80%"); nothing says where in it the Insurer should be. | src:913-976 | Repaired without approval, 10,000,000. | §X14: 9,500,000 or 1,900,000, both open to the Insurer. |
| X15 | **The deductible applies to every loss, or to partial losses only.** 1.8 and 15.2 say each loss; 15.1 says each partial loss. | src:87-91, 894-900 | — | reading only (fork F25) |
| X16 | **The 16.1 chapeau's comparative has lost its adjective.** "trừ trường hợp Công Ty Bảo Hiểm quy định mức giảm trừ hơn trong Hợp Đồng" — a reduction level "more ..." than what, higher or lower, is not said. | src:913-915 | A contract stating a reduction level of 10%. | §X16: declined. |
| X17 | **16.1.3 does not know 5.2's deemed consent.** 5.2 lets the Policyholder repair after five working days of the Insurer's silence; 16.1.3 reduces by up to 80% for repairing "without the Insurer's approval". | src:326-329, 936-940 | — | reading only (fork F26) |
| X18 | **The two total-loss limbs draw the line differently**: damage "trên 75%" (over), repair cost "bằng hoặc trên 75%" (75% or more). | src:849-852 | — | reading only; both edges are tested in `ocar-tests-amounts.l4` |
| X19 | **4.1 calls the amount paid out the "Số Tiền Bảo Hiểm"** (the defined sum insured). | src:228-230 | — | reading only |
| X20 | **The payment period may never start.** The Insurer pays within 15 or 30 working days of a "complete and valid" file; Article 8's file is "one or more" of a list ending with "other relevant papers (if any)", chosen by no stated rule; where the Insurer cannot verify, the file is complete only on the authority's conclusion; after 90 days the Insurer "may consider" settling. A theft is payable only on a judgment or decision (14.2.2) with no time for it. | src:238-252, 427-429, 488, 853-856 | The Insurer cannot verify; the authority has not concluded. | §X20: the date the file counts as complete is NOTHING. |
| X21 | **A lower risk, refused, costs 30% to leave.** Article 6 lets the Insurer refuse to cut the premium after a fall in risk; the Policyholder's remedy is 3.2.2, at 70%, or nothing after a loss. | src:376-385, 184-190 | Risk falls, request refused, terminate 1 July. | §X21 |
| X22 | **Double insurance the Law would not call double, stacked on under-insurance.** Article 9 shares a loss whatever the total sum insured; the Law's Article 49(1) only where the total exceeds the value. On a 600,000,000 car insured twice at 300,000,000, OPES pays half of half. | src:503-523; Law lines 964-968 | A 10,000,000 loss. | §X22: 2,000,000 after the deductible. |
| X23 | **One dong moves the whole cost of the independent assessment.** If its conclusion "differs" from the Insurer's, the Insurer pays it and the court fees; if it is the same, the Policyholder pays. | src:410-424 | Insurer 10,000,000; independent 10,000,001. | §X23 |
| X24 | **Article 10 names different parties for the same complaint**: the period runs from the Owner's receipt of the notice, and is extended where the Policyholder could not complain. | src:536-542 | — | reading only |
| X25 | **Any insured event forfeits the refund, even one that paid nothing.** 3.1.3 and 3.2.2 refund nothing "trong trường hợp đã xảy ra sự kiện bảo hiểm"; a scrape below the deductible is such an event, pays nothing (12.20), and still wipes out the refund. | src:176-177, 188-190, 694-695 | A 400,000 scrape, then termination on 1 July. | §X25: claim 0; refund 0 instead of 70% x 12,000,000 x 183/365. |
| X26 | **12.13 excludes electrical damage from a short circuit "by any cause"**, including one caused by a collision or fire the cover insures. | src:652-656 | A collision that shorts the wiring. | `ocar-tests-cover.l4`: the item is excluded |
| X27 | **1.10 forbids over-insurance by definition; 13.2 and 14.1.2(b) provide for it.** | src:96-98, 754-756, 788 | — | reading only |
| X28 | **No grace period for the premium.** 3.1.1 ends the contract the moment the payment period ends; the Law speaks of termination after a grace period (L8). | src:162-166 | — | reading only |
| X29 | **Several exclusions need no causal link.** 12.4 and 12.5 exclude a loss "khi" (while) the driver is over the limit or making a prohibited turn; a tree falling on the car during a prohibited U-turn is excluded. | src:587-592, 622-629 | — | reading only (fork F16) |

The three that most matter to a policyholder: **X3** (a notice in time under one clause is late under another, at a cost of up to 10%), **X25** (a refund lost to a claim that paid nothing), and **X1** (exercising a data-protection right ends the cover and forfeits 30% of the premium, or all of it).

## 5. Answer table

From the text (src lines in brackets); "input" means the contract or certificate states it.

| question | answer |
| --- | --- |
| minimum deductible [897] | 500,000 VND a loss; higher if the contract says |
| BS03 deductible [1054-1057] | 10% of the indemnity, at least 3,000,000 (or as agreed) |
| BS05 deductible [1100-1103] | 20% of the indemnity, at least 2,000,000 (or as agreed) |
| BS05 number of losses [1097-1099] | 2 for 12-18 months; 3 over 18; under 12 declined |
| depreciation, ordinary [795-802] | up to 3 years 0%; to 6: 15%; to 10: 25%; to 15: 35%; over 15: 50% |
| depreciation, bus / transport / rental / taxi [803-818] | up to 3 years 15%; to 6: 22.5%; to 10: 37.5%; to 15: 52.5%; over 15: 75% |
| depreciation, gas, coolant, oil, battery, canvas [830-833] | 30% in the first year of use, 50% after |
| depreciation, tyres, tubes, labels [834-837] | agreed at assessment, at least 30% |
| depreciation, glass and mirrors [838-839] | none |
| remaining-quality rate (13.2(i)) [747-751] | up to 1 year 100%; to 3: 85%; to 6: 70%; to 10: 55%; over 10: 40% |
| replacement threshold [842-844] | repair over 50% of the new part's value |
| whole repaint [845] | over 50% of the painted area |
| total loss [849-852] | damage over 75%, or repair 75% or more, of the market value before the loss |
| reductions [916-972] | 5-10%; up to 25%; up to 80%; up to 30%; by the overload (over 20%, under 50%); by the premium shortfall; one only, the highest |
| refunds [170-201] | late premium: 70% of the overpayment, in 5 working days; Policyholder ends it: 70% of the unexpired premium, in 15 days; Insurer ends it: 100%, in 15 days; none after an insured event (first two) |
| deadlines [238-332, 354, 371-381] | notify a loss 5 working days; a theft 24 hours; notify a change 15 days; Insurer pays 15 / 30 working days; answers a premium request 5 working days |
| time limits [533-545] | claim 1 year; complaint 90 days; suit 3 years |

## 6. What `check.sh` prints

```
module                                    errors satisfied  failed  refused  expected
ocar-01-definitions.l4                         0         0       0        0         0
ocar-02-03-term-termination.l4                 0         0       0        0         0
ocar-04-05-06-duties.l4                        0         0       0        0         0
ocar-07-10-claims-process.l4                   0         0       0        0         0
ocar-11-12-cover.l4                            0         0       0        0         0
ocar-13-valuation.l4                           0         0       0        0         0
ocar-14-settlement.l4                          0         0       0        0         0
ocar-15-16-deductible-reductions.l4            0         0       0        0         0
ocar-17-supplementary.l4                       0         0       0        0         0
ocar-claim.l4                                  0         0       0        0         0
ocar-nouns.l4                                  0         0       0        0         0
ocar-personal-data.l4                          0         0       0        0         0
ocar-tests-amounts.l4                          0       119       0        0         0
ocar-tests-cover.l4                            0        92       0        0         0
ocar-tests-findings.l4                         0        32       0        0         0
ocar-tests-fixtures.l4                         0         0       0        0         0
ocar-tests-process.l4                          0        56       0        0         0
ocar-tests-tables.l4                           0        50       0        0         0
TOTAL (18 modules)                             0       349       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

No failed or refused assertion is expected: `check.sh`'s `expected_failed` table is unchanged (0 for every module), and every declined case is asserted with `#ASSERT REFUSED ... BECAUSE "..."`, which counts as satisfied.
The rule modules and `ocar-tests-fixtures.l4` carry no directives, so they show zeros.
On the separate runs before this one, one assertion in `ocar-tests-amounts.l4` failed: a test written for a total loss gave damage of 500,000,000 against a market value of 700,000,000, which is not over 75% (525,000,000), so the encoding rightly treated it as a partial loss with no items and paid 0. The scenario's facts were corrected to 600,000,000; the expected value (600,000,000, the sum insured) was not changed. Every other assertion passed on its first complete run.
`ocar-tests-process.l4` also runs 20 `#TRACE` directives, which `check.sh` does not count; each pair shows the duty kept (`FULFILLED`) and broken (`DEONTIC BREACHED`), and the 5.2 no-repair rule shows the breach on an early repair and `FULFILLED` for a repair after five working days' silence.
Each run also begins with two `Warning | [Import Resolution]` notices: the binary's embedded `prelude` and `daydate` are chosen over differing copies under `~/.local/share/jl4/libraries/`. They are not diagnostics, and `check.sh` does not count them.
A run takes many minutes on a loaded machine: l4 re-checks an imported module once per import path, which is why the rule modules import each other in a single chain.

## 7. The `vnsrc check` line

The gate, as the lead ruled on 7 October: every `.l4` and every `.md` in this directory except `BRIEF.md` (the lead's file), from this directory:
`python3 -I tools/vnsrc.py check ../../source/raw/opes-ocar.txt *.l4 $(ls *.md | grep -v '^BRIEF.md$')`. Its last line:

```
vnsrc check: 769 src: lines, 492 Vietnamese runs, 0 problems
```

The brief's literal command (`... *.l4 *.md`) also reads `BRIEF.md`, and its one problem is there (line 31, the name of a sibling row's insurer, which is not in this source). Its last line:

```
vnsrc check: 769 src: lines, 502 Vietnamese runs, 1 problems
```

## 8. Open questions for a domain expert

1. Did Decision 17/2022 change the wording of Articles 1-17, and from when was each Decision in force (F2)? Was there a 2019 text of the no-depreciation clause, and of other supplementary clauses?
2. Under which instrument, and from when, was the personal data clause added (F3)? Do OPES certificates say which version of the rules they incorporate?
3. Is "sự kiện bảo hiểm" in 3.1.3 and 3.2.2 read in practice as any event within the cover, or only one that is paid (F6, X25)?
4. How does OPES apply 16.1.1's five days against 5.2's five working days (X3), and how does it choose a rate within the Article 16 ranges (X14)?
5. Is the battery depreciated under BS01 (X2)? Does 12.13 bite on flood damage under BS03 (X9)?
6. How is a partial loss settled under BS04 once the sub-limit is used (X7), and what is BS05's limit for a contract under 12 months (X8)?
7. In what order does OPES apply the under-insurance ratio, the double-insurance share, the deductible and the reduction (F31, F4)?
8. Does the Law on Insurance Business override 3.2.1's "in accordance with law" (L3), Article 9's definition (L6), and Article 7's binding-effect rule (L7)? Is there a premium grace period in practice (L8)?
