# NOTES: Manulife term life product terms, encoding row `legalese-2026-10-vn-11`

Manulife Vietnam's term life product terms, "Điều khoản sản phẩm bảo hiểm tử kỳ có thời hạn" ("Bảo hiểm nhân thọ có thời hạn"), encoded in L4 by one agent in one session (run `VN-11-20261006`, agent `enc-vn-11`, 2026-10-06), from `BRIEF.md`.
Status: **draft**.
No domain expert has read it against the source; HG1 has not been sought; no independent test pass has been run.

The source is `../../source/raw/manulife-term-life.txt`, the `pdftotext` rendering (reading order, no `-layout`) of `manulife-term-life.pdf`, 5 pages (page 5 is blank), sha256 `145e8c27775d6bc71c942c796505df7ecc6c3bc5501c560cb9f7faef33ee626c`, from the insurer's website, retrieved 2026-10-06.
`src:N` is line N of that rendering.
The PDF is two columns, so the rendering interleaves them: Art 5's text is at src:212-213, then src:147-169, then src:175-179; the refund sentence that closes Art 3(c) is at src:171-173; Art 4's text is at src:185-195 under its heading at src:181; Art 6 is src:183 and src:197-199; Art 18(i)'s text is at src:403-404 with its numeral at src:409.
Each was checked against the rendered PDF page.

## 0. Build and run

`l4` is `/Users/mengwong/.local/bin/l4`, a link to `~/.cabal/bin/l4`, itself a link into cabal store entry `jl4-0.1-0ee0100b`, modified 2026-10-06 21:20 (local), sha256 `64bbcb157dbef2ef1020a6a75589313bba0a2aeeb807c921c5e65e62e9eca118`.
The binary has no `--version` and no record beside it names the commit it was built from.
`JL4_LIBRARY_PATH` was unset.

Command, from this directory:

```
L4=/Users/mengwong/.local/bin/l4 ./check.sh
```

```
module                                    errors satisfied  failed  refused  expected
vn11-art01-02-definitions.l4                   0         0       0        0         0
vn11-art03-benefits.l4                         0         0       0        0         0
vn11-art04-07-premiums.l4                      0         0       0        0         0
vn11-art08-13-conditions.l4                    0         0       0        0         0
vn11-art14-18-administration.l4                0         0       0        0         0
vn11-death-claim.l4                            0         0       0        0         0
vn11-findings.l4                               0        16       0        0         0
vn11-nouns.l4                                  0         0       0        0         0
vn11-tests.l4                                  0       128       0        0         0
TOTAL (9 modules)                              0       144       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

`check.sh` exit 0, run on 2026-10-06 after the last change to any `.l4` file, and run again at 00:06 on 2026-10-07, after the stray file below was removed, with output identical to the table above.

**A stray file, now removed.** For a while this directory also held `vn13-nouns.l4`. It was **not part of VN-11**: it was row VN-13's nouns template, expanded into this deposit by this row's build script on 2026-10-06 at about 22:51. The session's scratchpad directory is shared by all the encoders, and VN-11 and VN-13 had both put templates in `scratchpad/tpl/`; the same collision then overwrote both rows' templates with VN-13's raw text. Its `src:` lines were quoted from **this** row's source, by this row's line numbers, so they meant nothing for VN-13. This row's own attempt to delete it was refused by the permission classifier; the lead removed it at about 23:05 on the user's instruction. No VN-11 module imported or referred to it. Every `check.sh` total in this file was taken after its removal: each per-module table lists 9 modules, none of them it.

**What this row saw of VN-13's material, against the blind rule.** In finding and reporting the collision, this session read: the first three lines of the expanded `vn13-nouns.l4` (`@lang en`, `IMPORT prelude`, `IMPORT daydate`); VN-13's `scratchpad/build.sh` (its deposit path and the name of its raw text, `manulife-maxx.txt`); and about fifty-five lines (lines 1-5 and 20-69) of that raw text, which had been written over this row's template, including its title and its definitions of "Ngày hiệu lực Hợp đồng" and "Ngày cấp Hợp đồng". A process listing taken to find a slow run of this row's own also showed fragments of other encoders' commands (a few lines of VN-01's test generator, and other rows' file names). It did not see VN-13's encoding: no rule, no identifier beyond those three lines, no fork, no test. So far as this session can tell, nothing from any of this reached this row's modules. The nouns module, including the `issue date` field, and the reading behind fork F3 (the issue date is undefined in this document) had been written, built and type-checked before the collision was found. The overwritten templates were rewritten from this session's own copies. All of this row's later scratch work is under `scratchpad/enc-vn-11/` only.

## 1. What is encoded and what is not

**The whole document is in scope and every provision is reached** (coverage table, section 2): the definitions of Art 1, the contract and amendments of Art 2, the death benefit with its child table and exclusions (Art 3), the free-look period (Art 4), premiums, grace and lapse (Art 5), the currency (Art 6), residence (Art 7), beneficiaries (Art 8), misstated Age or sex (Art 9), incontestability (Art 10), suicide (Art 11), the two "no" clauses (Arts 12, 13), reinstatement (Art 14), assignment (Art 15), claims and payment (Art 16), disputes (Art 17) and termination (Art 18).
Nothing is out of scope.

**Modules.**
`vn11-nouns.l4` declares the facts, and nothing else.
`vn11-art01-02-definitions.l4`, `vn11-art03-benefits.l4`, `vn11-art04-07-premiums.l4`, `vn11-art08-13-conditions.l4` and `vn11-art14-18-administration.l4` follow the document's Articles.
`vn11-death-claim.l4` puts a death claim together in three layers: whether the contract was in force and whether a limitation bites; how much is payable; and the claim's time, evidence and the Company's duty to pay.
`vn11-tests.l4` holds the tests; `vn11-findings.l4` holds the evidence for the findings in section 4.

**Inputs, not defaults.**
Everything the document leaves to the contract page ("Trang Hợp đồng") is an input with no default: the sum insured, the effective, issue and maturity dates, the premium plan, and the premiums paid.
So are the facts of a claim, the Company's own decisions (to treat the contract as void, to approve a change, to reinstate), judgements the document leaves to someone (materiality, whether a death was "related to" HIV), the riders' benefits (their terms are not in this document) and the Company's figure for "reasonable costs".
The figures in the rules are the document's: 0 and 60 (Art 1.3), 20/40/60/80/100% (Art 3(b)), 100% (Arts 3(c), 9, 11), 14 days (Art 4), 60 days (Art 5), 2 years (Arts 10, 11, 14), 1 year and 2 months (Art 16), 3 years (Art 17).
Two more are readings, each recorded: 0, the floor of a refund (fork F10), and 1, for "the day after" the grace period on which Art 18(i) ends the contract.

**Where the document is silent the encoding refuses**, with a named `REFUSE` whose message is the gap: before the first premium is paid (Art 5); an insured not resident on the issue date, or issued at an Age outside 0-60 that was not misstated (Arts 1.3, 7); an application not signed by both (Art 1.5); no beneficiary, shares stated for some only, or shares not making up the whole (Art 8); what is returned when the Company avoids the contract (Art 10); the amount of late-payment interest (Art 16).
Each is reached by a test (`#ASSERT REFUSED … BECAUSE "…"`).

**Days.** Calendar days throughout (the document never says working days); the day a period counts from is day 0 and the period includes its last day; months and years are calendar months and years, with a 29 February or 31st clamped to the end of a shorter month (fork F2).
The regulative rules' clock (Arts 4, 5, 16) is calendar days, stated in each module's header.

**Not done.** No independent test pass (the brief allows one session and no sub-agents).
No `@export` annotations: the brief asks for none, and adding them would be a deployment decision.

## 2. Coverage table

Headings are as the document writes them, then an English gloss.
Totals: **48 rows: 37 encoded (3 of them with a gap reached and refused), 8 inert, 3 reached-and-refused, 0 out-of-scope, 0 deferred**.

| provision | heading as written / English gloss | src | disposition | where in the L4 |
| --- | --- | --- | --- | --- |
| title | Điều khoản sản phẩm bảo hiểm tử kỳ có thời hạn / term life product terms; attached to a 2002 letter of the Ministry of Finance whose number and date are blank | 1-5, 50-52 | inert: names the document and its vintage, decides nothing | header of `vn11-art01-02-definitions.l4` |
| Art 1 | Điều 1: Định nghĩa / Definitions | 7 | inert (chapeau) | § `Article 1` |
| Art 1.1 | Công ty / the Company | 8-12 | encoded | `the Company` in `A party` (nouns) |
| Art 1.2 | Bên mua bảo hiểm / the policyholder | 13-20 | encoded | `the policyholder` in `A party` (nouns) |
| Art 1.3 | Người được bảo hiểm / the insured: residence and Age 0-60 at issue | 21-31 | encoded | `The insured`; `Art 1.3 — an Age from 0 to 60`; `Art 1.3 — the insured met the residence and Age conditions …` |
| Art 1.3, consequence | (none written) / what follows when a condition fails | 26-31 | reached-and-refused | `Arts 1.3 and 7 do not say …`; `Art 1.3 does not say …` |
| Art 1.4 | Tuổi / Age, at the last birthday | 32-33 | encoded | `the Age of` … `on` … |
| Art 1.5, first paragraph | Năm Hợp đồng và Ngày kỷ niệm Hợp đồng / contract years, anniversaries, the effective date | 34-43 | encoded | `The contract page`; `contract anniversary number` … `of` … |
| Art 1.5, valid application | (same heading) / the application signed by both | 43-45 | encoded; its consequence reached-and-refused | `Art 1.5 — the application is valid`; `Art 1.5 does not say …` |
| Art 1.5, second paragraph | (same heading) / the maturity date | 46-48 | encoded | `maturity date` (nouns); `Art 1.6 — the day falls in the contract term` |
| Art 1.6 | Thời hạn Hợp đồng bảo hiểm / the contract term | 54-56 | encoded | `Art 1.6 — the day falls in the contract term` |
| Art 2, first paragraph | Điều 2: Hợp đồng bảo hiểm / the documents forming the complete contract | 57-69 | inert: lists documents, decides nothing | `Art 2 — the documents that together form the complete contract` |
| Art 2, second paragraph | (same heading) / amendments in writing, signed by the General Director or a Deputy, with the policyholder's consent | 70-74 | encoded | `Art 2 — the amendment is validly made` |
| Art 3 | Điều 3: Quyền lợi bảo hiểm / benefits | 75 | inert (chapeau) | § `Article 3` |
| Art 3(a) | a. Quyền lợi khi tử vong / the death benefit: (i) the sum insured, plus (ii) rider benefits, less (iii) unpaid premiums | 76-93 | encoded | `Art 3(a) — the death benefit` |
| Art 3(b) | b. Giới hạn Quyền lợi khi tử vong / a child's benefit reduced by a table of five rows | 94-126 | encoded, one arm per row | `Art 3(b) — the percentage of the sum insured for an Age at death of` |
| Art 3(c) | C. Loại trừ đối với Quyền lợi khi tử vong / exclusions: (i) crime, (ii) AIDS, ARC or HIV | 128-145 | encoded | `Art 3(c) — the death benefit is excluded for` |
| Art 3(c), last sentence | (same heading) / the premium refunded, less reasonable costs | 171-173 | encoded | `the premium refunded, without interest, after the reasonable costs` |
| Art 4 | Điều 4: Từ chối tham gia bảo hiểm / the 14-day free look, refund less medical expenses, receipts | 181, 185-195 | encoded | `Art 4 — the result of the request to cancel`; `Art 4 — the policyholder may cancel …` (DEONTIC) |
| Art 5, duty | Điều 5: Đóng phí bảo hiểm và Gia hạn đóng phí bảo hiểm / the policyholder pays each premium by its due date | 207-213, 147-150, 175-179 | encoded | `Art 5 — the policyholder must pay each premium …` (DEONTIC) |
| Art 5, deemed non-payment | (same heading) / payment to the Company or its agent on or before the due date | 151-154 | encoded | `Art 5 — the instalment is deemed not paid`; `Art 5 — paid to the Company or to its agent` |
| Art 5, first premium | (same heading) / the rule begins after the first premium | 151 | reached-and-refused | `Art 5 does not say whether the contract is in force before the first premium is paid` |
| Art 5, grace | (same heading) / 60 days, in force throughout | 155-158 | encoded | `Art 5 — the last day of the grace period for` |
| Art 5, lapse | (same heading) / unpaid at the end of grace: lapse and termination | 159-161 | encoded | `Art 5 — the contract had lapsed by` … `for non-payment of` … |
| Art 5, annual basis | (same heading) / premiums not yet due are not required on a death claim | 162-169 | encoded | `Art 5 — the premiums deducted from the death benefit as unpaid` |
| Art 6 | Điều 6: Loại tiền thanh toán / payment in Vietnamese dong | 183, 197-199 | inert: fixes the unit of every NUMBER, decides nothing | `Art 6 — the currency of every payment …` |
| Art 7 | Điều 7: Cư trú, đi lại và nghề nghiệp / residence in Vietnam at issue; no other restriction | 200-205 | encoded (the second sentence by absence: no rule reads travel or occupation) | `Art 7 — the insured resided in Vietnam …`; test "Articles 6 and 7" |
| Art 8, first and second paragraphs | Điều 8: Người thụ hưởng / beneficiaries, equal shares unless stated | 210-227 | encoded; three gaps reached-and-refused | `Art 8 — the amounts paid to the beneficiaries, in the order they are named`; three `Art 8 does not say …` |
| Art 8, third paragraph | (same heading) / changing the beneficiary | 228-232 | encoded | `Art 8 — the change of beneficiary takes effect` |
| Art 8, fourth paragraph | (same heading) / the Company not responsible for a designation's validity | 233-235 | inert: a disclaimer that decides no question asked here | `Art 8 — the Company's responsibility for the validity of a designation` |
| Art 9, first paragraph | Điều 9: Tuổi và giới tính / a misstated Age or sex corrected | 236-248 | encoded | `Art 9 — the sum insured after the misstatement is corrected`; `Art 9 — the excess premium refunded, without interest` |
| Art 9, second paragraph | (same heading) / a true Age outside 0-60: premium refunded | 249-254 | encoded | `Art 9 — a misstated Age, and the true Age at issue outside Art 1.3` |
| Art 10 | Điều 10: Mặc nhiên thừa nhận Hợp đồng bảo hiểm / the Company's right to avoid for non-disclosure, and its end after 2 years | 255-276 | encoded | `Art 10 — the Company may treat the contract as void`; `Art 10 — the last day of the two years` |
| Art 10, consequence | (same heading) / what is returned on avoidance | 257-267 | reached-and-refused | `Art 10 — the premium returned when the Company treats the contract as void` |
| Art 11 | Điều 11: Tự tử / suicide within 2 years | 277-288 | encoded | `Art 11 — a suicide within 2 years of the issue date or of a reinstatement` |
| Art 12 | Điều 12: Không tham gia chia lãi / no participation in profits | 289-291 | encoded | `Art 12 — the contract shares in the Company's profits` (FALSE) |
| Art 13 | Điều 13: Giá trị hoàn lại và quyền lợi không bị tước đoạt / no surrender value, no non-forfeiture benefits | 292-296 | encoded | `Art 13 — the contract has a surrender value` (FALSE); `… non-forfeiture benefits` (FALSE) |
| Art 14 | Điều 14: Khôi phục hiệu lực Hợp đồng / reinstatement within 2 years, at the Company's discretion | 297-311 | encoded | `Art 14 — the contract may be reinstated`; `Art 14 — the contract is reinstated` |
| Art 15, first to third paragraphs | Điều 15: Chuyển nhượng / assignment while the insured is alive and the contract in force | 312-324 | encoded | `Art 15 — the policyholder may assign the contract`; `Art 15 — the assignee takes the policyholder's rights` |
| Art 15, fourth paragraph | (same heading) / notice, original instrument, written approval; no responsibility for validity | 325-334 | encoded (the disclaimer inert) | `Art 15 — the Company is treated as knowing of the assignment` |
| Art 16, evidence | Điều 16: Giải quyết Quyền lợi bảo hiểm khi tử vong / proof of death and items (i)-(v) | 335-362 | encoded | `Art 16 — the Company has received the evidence it requires` |
| Art 16, time to claim | (same heading) / one year, force majeure, the policyholder's ignorance | 364-375 | encoded | `Art 16 — the last day to claim`; `Art 16 — the claim was made in time` |
| Art 16, payment and interest | (same heading) / interest after 2 months at the State Bank's overdue-debt rate | 376-383 | encoded; the interest amount reached-and-refused | `Art 16 — the Company must pay the death benefit, with interest …` (DEONTIC); `Art 16 — the interest on a death benefit …` |
| Art 16, last sentence | (same heading) / the contract ends once the claim is settled | 383-385 | inert: a second end beside Art 18(ii), which decides the cover questions (finding 11) | comment at Art 18 |
| Art 17, first paragraph | Điều 17: Giải quyết mâu thuẫn và tranh chấp / Vietnamese law governs | 386-389 | inert: the encoding is already the chosen law's reading | `Art 17 — the governing law` |
| Art 17, second paragraph | (same heading) / negotiation, then the nearest court or an agreed court | 390-394 | encoded | `Art 17 — the courts the dispute may be taken to` |
| Art 17, third paragraph | (same heading) / 3 years to sue | 395-398 | encoded | `Art 17 — the last day to bring proceedings` |
| Art 18 | Điều 18: Chấm dứt Hợp đồng / termination at the earliest of (i)-(iv) | 399-409 | encoded | `Art 18 — the termination of the contract`; and in `vn11-death-claim.l4` |

## 3. Fork register

Every ambiguity met, the readings seen, the one taken and the text that licenses it.
`LAW:` forks are where Law 08/2022/QH15 (the aid at `.aids/law-08-2022-qh15.txt`, cited by its line numbers there) fills or overrides the document; none is resolved silently, and the encoding encodes the document, not the Law.
Whether the Law of 2022 governs a contract made on this template at all depends on its transitional provisions, which are not in the aid (its text stops at Điều 130): outside knowledge, unverified.

| # | where | the question | readings | taken, and why |
| --- | --- | --- | --- | --- |
| F1 | Art 1.5, src:38-42 | Is the effective date the day the application is signed, or the day the Company accepts it? | (i) the signing day, once accepted; (ii) the acceptance day | **neither decided**: the effective date is "ghi trong Trang Hợp đồng" (written on the contract page), so it is an input. |
| F2 | Arts 4, 5, 10, 11, 14, 16, 17 | How are "ngày", "tháng", "năm" counted, and is the first day in? | (i) calendar units, the start day is day 0, the last day is start + N, inclusive; (ii) the start day is day 1, so the last day is start + N - 1; (iii) working days | **(i)**. The document never says working days. "Kể từ" (counting from) and "sau khi" (after) read most naturally as starting the day after. The Civil Code is said to count the same way (outside knowledge, unverified). Months and years are calendar ones, clamped at a month's end (29 Feb → 28 Feb). Ages use the same rule for birthdays. |
| F3 | Arts 1.3, 7, 10, 11 | What is "ngày cấp Hợp đồng bảo hiểm" (the issue date)? It is used four times and never defined. | (i) a date of its own, usually after the effective date; (ii) the effective date | **(i)**, an input distinct from the effective date: the document uses two different words. The difference is finding 4. |
| F4 | Art 1.3, src:29-31 | "từ 0 (không) Tuổi đến 60 (sáu mươi) Tuổi": is 60 included? | (i) inclusive; (ii) up to but not including 60 | **(i)**: "từ … đến" (from … to) names both ends, and Law Art 24 (aid lines 588-591) reads an unclear term for the policyholder. |
| F5 | Arts 1.5, 1.6, 18(iii) | Is a death on the maturity date covered? | (i) yes, the term runs "đến" (to) the maturity date; (ii) no, the contract ends as that day begins | **(i)**, for the same reasons as F4. |
| F6 | Art 3(c)(i), src:137 | "Phạm tội hoặc cố tình phạm tội hình sự": whose crime? | (i) the insured's own; (ii) anyone's, so a murdered insured is excluded | **(i)**: the exclusion is a list of causes for which the insured's conduct is the usual subject, and Law Art 24 reads the gap for the policyholder; Law Art 38 (lines 793-802) has the insurer pay when a third party causes the death. Reading (ii) is the text's literal reach (finding 1). |
| F7 | Art 3(a)(iii), src:93, with Art 5, src:162-169 | Which premiums does "Tất cả các khoản phí bảo hiểm chưa đóng" (all premiums not paid) deduct? | (i) those due and unpaid at the death; (ii) also the rest of the year's premium under a modal plan, not yet due | **(i)**: Art 5 says that on a death claim the Company "will not require" the year's premiums not yet due, which would be empty if (iii) deducted them anyway. Finding 13 shows (ii). |
| F8 | Art 3(b), src:108-126 | The rows "Dưới 1 tuổi", "Dưới 2 tuổi" overlap. Which row governs Age 0? | (i) the first row that fits, read down the table; (ii) the last | **(i)**: each row only makes sense for the Ages the row above leaves. With Age at the last birthday (Art 1.4), each "under N" row covers exactly Age N-1: "Dưới 2 tuổi" covers Age 1. |
| F9 | Art 3(b), src:95-100 | What does the percentage reduce? | (i) the sum insured, limb (i) only, then (ii) added and (iii) deducted; (ii) the whole of (i) less (iii) | **(i)**: "tỷ lệ phần trăm của số tiền bảo hiểm (không bao gồm quyền lợi của các điều khoản bảo hiểm bổ trợ)" (a percentage of the sum insured, excluding the riders). |
| F10 | Arts 3(c), 9, 11; Art 4 | "hoàn lại 100% số phí bảo hiểm … sau khi khấu trừ các chi phí": 100% of which premium, and what if the costs exceed it? Likewise Art 4's refund less medical expenses. | (i) all premium paid, not below nil; (ii) the current year's premium; (iii) a negative refund, owed by the policyholder | **(i)**: "hoàn lại" (refund) cannot be negative, and nothing limits the premium to one year. |
| F11 | Arts 9 and 10 | A misstated Age or sex is also a misstatement of "thông tin nào có tầm quan trọng". Which Article governs it? | (i) Art 9 alone; (ii) Art 10 too, so the Company may avoid within two years | **(i)**: Art 9 is the specific rule with its own remedy. The disclosure record is about other information. |
| F12 | Art 4, src:185-188 | Is "yêu cầu bằng văn bản gửi tới Công ty" within 14 days met on the day the request is sent or the day it arrives? And does a request after the death cancel? | (i) sent; (ii) received | **(i)**: "gửi" is "send". A request sent after the death is not dealt with; only a request sent in time on or before the death defeats cover. |
| F13 | Art 11, src:278-280 | Is a suicide before the issue date (between the effective and issue dates) "trong thời gian 2 (hai) năm kể từ ngày cấp"? | (i) no: the period runs from the issue date; (ii) yes: any time up to two years after issue | **(i)**, on the words and Law Art 24 (finding 4). |
| F14 | Art 9, src:245-248 | "điều chỉnh giảm số tiền bảo hiểm xuống phù hợp với khoản phí bảo hiểm đã đóng": by how much? | (i) in proportion, sum insured × paid / payable; (ii) whatever the premium paid buys on the insurer's rate table | **(i)**: the rate table is not in the document. The two agree when the premium is proportional to the sum insured, and differ by any fixed policy fee. |
| F15 | Art 18(iv), src:407-408 | When does a termination "Khi Bên mua bảo hiểm yêu cầu" take effect, and is a death that day covered? | (i) on the day of the request, a death that day covered; (ii) on the Company's receipt or processing | **(i)**: the clause names the request, not the Company's act; covered on the day, as for maturity (F5). |
| F16 | Art 14, src:298-303 | Which day must fall within the two years: the application to reinstate, or the reinstatement? | (i) the application; (ii) the reinstatement | **(i)**, because the reinstatement's timing is the Company's ("tùy theo sự xem xét của Công ty"), and a policyholder can only act within the window. |
| F17 | Art 16, src:376-383 | Is there a payment deadline, and when is interest owed? | (i) "cố gắng giải quyết ngay" sets none; the two months after the claim is the only deadline, and interest is owed "vì bất kỳ lý do gì" (for whatever reason) after it; (ii) interest only where the Company caused the delay | **(i)** on the words. From when interest runs, on what and at what day count is not said: refused. |
| F18 | the composition, `vn11-death-claim.l4` | In what order do the Articles decide a claim, and does the claim's time bar apply to refunds? | — | Term, first premium, cancellation, lapse, termination, Art 10, Art 9, then the refusing gates (Arts 1.5, 7, 1.3), then Art 11, Art 3(c), the time bar, and the benefit. The time bar (Art 16) speaks of "quyền lợi bảo hiểm" (benefits) and is applied to the death benefit only, not to the refunds of Arts 3(c), 9 and 11. |
| F19 | Art 5, src:151-161 | What counts as payment? | — | Payment in full ("đóng đủ") to the Company or its agent ("cho Công ty hoặc cho đại lý của Công ty"); a part payment, or payment to anyone else, does not count. |
| F20 | Art 10, src:264-267 | "và Người được bảo hiểm hoặc Bên mua bảo hiểm có liên quan cũng không khai báo việc không khai báo hoặc khai báo sai nói trên": a condition, or a restatement? | (i) a further condition: the omission was not itself declared (corrected) later; (ii) a restatement | **(i)**: read as a restatement it would add nothing. |
| F21 | Art 16, src:364-375 | From when does the year to claim run, and who can extend it? | (i) the death; extended only where the policyholder proves ignorance; (ii) also the beneficiary | **(i)** on the words, "Bên mua bảo hiểm chứng minh". Finding 3. |
| F22 | Art 16, src:337-362 | Do missing documents defeat the claim, or delay it? | (i) delay: the Company must settle once they are in; (ii) defeat | **(i)**: "sẽ được giải quyết … khi Công ty nhận được" (will be settled when the Company receives). |
| F23 | Art 3(c), Arts 9, 11 | Who is paid a refund? | — | **not stated**: the encoding computes the amount and names no payee. |
| F24 | Art 8, src:222-227 | One beneficiary; shares stated as fractions | — | One beneficiary takes the whole; stated shares are fractions of the death benefit. |
| F25 | Art 5, src:151 | Is the contract in force before the first premium is paid? | (i) yes, from the effective date; (ii) no | **refused**: the non-payment rules start "Sau khi đóng phí bảo hiểm lần đầu" (after the first premium) and nothing says what applies before (finding 15). |
| F26 | Art 1.4, with Arts 1.3, 3(b), 9 | At which day is Age measured? | — | Art 1.3: the issue date ("Tuổi cấp Hợp đồng bảo hiểm"); Art 3(b): the day of death; Art 9: the true Age at the issue date. |
| L1 | LAW: Art 4 | Free-look period. | The document gives 14 days from receipt. Law Art 35 (lines 760-769) gives 21 days for a contract longer than one year. | Encoded: **14 days**, the document's. Not resolved: if the Law governs and the term exceeds a year, the Law's 21 days would prevail (outside knowledge, unverified, as to precedence). |
| L2 | LAW: Art 11 | When the suicide period starts. | The document counts from the issue date. Law Art 40(1)(a) (lines 818-820) counts from the payment of the first premium or the reinstatement. | Encoded: **the issue date**. Law Art 40(3) (lines 835-840): premium paid less reasonable costs, or surrender value, which agrees with the document's refund. |
| L3 | LAW: Art 16 | The time to claim. | The document gives "một năm hoặc một thời hạn khác theo quy định hiện hành của luật pháp". Law Art 30(1) (lines 707-710) also gives one year with force majeure excluded, and Art 30(2) (lines 711-714) gives the discovery rule to the insured or the beneficiary. | Encoded: **one year**, with the discovery rule for the policyholder only, as the document writes it (finding 3). |
| L4 | LAW: Art 16 | The payment deadline. | The document has no deadline, only interest after 2 months. Law Art 31(1) (lines 719-724) gives 15 days from a complete, valid claim where none is agreed, and Art 31(2) (lines 725-729) gives interest on late payment. | Encoded: **two months** as the deadline whose miss triggers the interest duty. Whether "2 months" is an "agreed period" under Art 31(1) is open. |
| L5 | LAW: Art 5 | Grace, reinstatement, premium suits. | Law Art 37(2) (lines 780-782): 60 days of grace, the same; 37(3) (783-786): reinstatement within 2 years, the same; 37(4) (787-791): the insurer may not sue for unpaid premium. | Encoded as the document; the duty's only reported consequence is lapse. |
| L6 | LAW: Art 15 | Assignment. | The document needs the Company's written approval. Law Art 28(1) (lines 680-682) also needs, for life insurance, the insured's written consent; 28(3) (685-689) the insurer's written consent. | Encoded: **the document's conditions**; the insured's consent is not a field. |
| L7 | LAW: Art 8 | Changing the beneficiary. | The document needs the Company's approval and no beneficiary's consent. Law Art 41(3) (lines 854-865) needs the insured's written consent and a written notice to the insurer, which confirms. | Encoded: **the document's conditions**. |
| L8 | LAW: Art 17 | The limitation period. | The document gives "3 (ba) năm hoặc một thời hạn khác theo quy định hiện hành của luật pháp". The Law, as given in the aid, has no limitation provision. | Encoded: **3 years**. What "current law" provides is outside knowledge, unverified. |
| L9 | LAW: Art 10 | What is returned on avoidance. | The document is silent. Law Art 22(2) (lines 543-553): on the policyholder's intentional false information the insurer may rescind and refunds the premium less reasonable costs; Art 25(2) (lines 619-622): a void contract is unwound both ways. | **Refused** (finding 5). |
| L10 | LAW: Art 3(c) | The exclusions. | Law Art 40(1) (lines 815-829) lists cases with no payment: suicide within 2 years; death by an intentional act of the policyholder or a beneficiary; death by execution; and others agreed. Art 19(2) (lines 435-440) requires exclusions to be explained, with evidence that they were. | Encoded: **the document's two**. The statutory cases the document does not repeat are not encoded. |
| L11 | LAW: Arts 1.3, 1.5 | Insuring a child. | The document admits Age 0 and requires the insured to sign. Law Art 39(2)(a) (lines 808-811) allows death cover on a minor only with a parent's or guardian's written consent. | Encoded: **the document's requirement**, which refuses for a child who did not sign (finding 10). |
| L12 | LAW: generally | Unclear terms. | Law Art 24 (lines 588-591) reads an unclear term in the policyholder's favour. | Used to choose readings F4, F5, F6, F13. |

## 4. Findings

The hostile reading: defects in the instrument as written, as a policyholder's lawyer and as the insurer's would use them.
A fork is an ambiguity the encoding resolved; a finding is a defect it found.
"L4:" names the evidence in `vn11-findings.l4` (or `vn11-tests.l4`); every one of those assertions passes, which is the point.

1. **The crime exclusion has no criminal.** src:132-137.
   "Công ty sẽ không thanh toán Quyền lợi khi tử vong nếu tử vong xảy ra do kết quả trực tiếp hay gián tiếp của … Phạm tội hoặc cố tình phạm tội hình sự".
   No subject is named, so on its words any death resulting, even indirectly, from anyone's crime is excluded: the insured murdered in a robbery, killed by a drunk driver, or killed by a beneficiary.
   Minimal scenario: the insured is killed in a robbery on 10 May 2023.
   L4: `Finding 1`, the taken reading `NOT … excluded` and the literal reading `… excluded`, both satisfied.
   The taken reading (F6) is the insured's own crime; the Law points the same way (L10, L12) but only if it governs.
2. **"Phạm tội" needs no intent.** src:137.
   The second limb says "cố tình" (intentionally); the first does not, so it swallows the second and reaches a crime of negligence. An insured who dies in a crash the insured caused, where that is a crime, is excluded, and the family receives the premium back less costs.
   L4: `Finding 2`, 19 million refunded instead of 1 billion. Whether careless driving is a crime is outside the document.
3. **Only the policyholder can stop the claim year running.** src:364-375.
   "Trong trường hợp Bên mua bảo hiểm chứng minh được rằng Bên mua bảo hiểm không biết …".
   In a death claim the claimant is the beneficiary, and when the insured is also the policyholder, the only person who can invoke the rule is dead. A beneficiary who learns of the death after a year is out of time. Law Art 30(2) gives the rule to the beneficiary (L3).
   L4: `Finding 3`, a claim 19 months after the death, `the claim for the death benefit is out of time`.
4. **The suicide and contest years run from an undefined date.** src:271-272, 278-280.
   Both count from "ngày cấp Hợp đồng bảo hiểm" (the issue date), which is not defined (F3) and is not the effective date from which cover runs (Art 1.5).
   Insurer's side: if issue follows the effective date, the two years end later than two years of cover; a suicide two years and 17 days into cover is still excluded.
   Policyholder's side: a suicide after the effective date but before issue is not "within 2 years from" the issue date, so the full benefit is payable.
   The Law counts the suicide period from the first premium (L2).
   L4: `Finding 4`, both cases.
5. **Avoidance with no stated consequence.** src:257-267.
   The Company "có quyền xem Hợp đồng bảo hiểm là vô hiệu" (may regard the contract as void), and the document never says what is returned: the premiums, the premiums less costs, or nothing.
   L4: `Finding 5`, `#ASSERT REFUSED`. The Law has answers (L9).
6. **No beneficiary, no payee.** src:215-227.
   The document says how to split among beneficiaries but not who is paid when none was designated or all have died, and not who receives a refund (F23).
   L4: `Finding 6`, refused.
7. **Discretion with no criteria.** src:172-173, 230-231, 260, 301, 307-311, 329.
   "Các chi phí và phí tổn phát sinh hợp lý" (reasonable costs, deducted from every refund) has no definition; the Company's approval of a beneficiary change (Art 8), of an assignment (Art 15) and of a reinstatement (Art 14, "tùy theo sự xem xét của Công ty") has no standard; the reinstatement interest is "ở mức và theo cách thức do Công ty quyết định" (at a rate and in a manner the Company decides), capped only by the State Bank's maximum; "có tầm quan trọng" (material) in Art 10 has no test.
   Reading only: each is an input recording the Company's decision.
8. **A misstated Age undoes cover at any time.** src:249-254 with 268-276.
   Art 10's two-year limit protects the policyholder against non-disclosure, but Art 9's last paragraph has no limit: a misstated Age whose true value was outside 0-60 ends in a refund of premium less costs fifteen years on.
   L4: `Finding 8`, a death in 2035, refund under Art 9.
9. **HIV: "related to", directly or indirectly.** src:132-134, 141-145.
   "Bất kỳ sự tử vong nào do liên quan đến … nhiễm vi rút (virus) gây suy giảm miễn dịch ở người (HIV)", within a chapeau reaching causes "trực tiếp hay gián tiếp". An insurer can argue that any death of an HIV-positive insured is indirectly related to the infection, whatever its proximate cause. No carve-out for infection by transfusion or at work.
   Reading only: the encoding records the relation as found.
10. **Conditions with no consequence, one of which a child cannot meet.** src:26-31, 43-45, 201-203.
    Arts 1.3 and 7 require residence in Vietnam and an issue Age of 0 to 60, and Art 1.5 requires the insured to sign the application, but none says what follows when a condition fails (Art 9 answers only a misstated Age).
    Art 1.3 admits an insured of Age 0, and Art 3(b) exists for young children, yet nobody can sign for the child under Art 1.5. On a truthful record a child's claim cannot be answered.
    L4: `Finding 10`, refused; the tests refuse the residence and issue-Age cases too.
11. **The contract ends twice.** src:383-385, 405.
    Art 18(ii) ends the contract on the day of death; Art 16 ends it "sau khi đã giải quyết xong quyền lợi bảo hiểm" (once the claim is settled). Between the two, it is unclear whether premiums falling due are owed or the Company's other duties survive.
    Reading only.
12. **A short free look, and a refund lost for want of receipts.** src:185-195.
    14 days against the Law's 21 (L1). A policyholder who cancels in time but does not return the premium receipts gets "không hoàn trả lại bất cứ một khoản tiền nào" (nothing at all), and no period is set for returning them, so the forfeiture never becomes final and never lapses.
    L4: `Finding 12`, a request on day 20 is late; a timely request without the receipts refunds nothing.
13. **"All premiums unpaid" against "will not require".** src:93 with 162-169.
    Read literally, Art 3(a)(iii) deducts the rest of the year's modal premiums that Art 5 says the Company will not require. The two clauses conflict unless (iii) means "due and unpaid" (F7).
    L4: `Finding 13`, 1 billion on the reading taken, 992.5 million on the literal one.
14. **No deadline to pay, and interest that cannot be computed.** src:376-383.
    "Sẽ cố gắng giải quyết ngay" (will try to settle promptly) binds the Company to nothing; the only bite is interest after two months "vì bất kỳ lý do gì" (for whatever reason, so even where the claimant delayed). The rate is named ("lãi suất nợ quá hạn do Ngân hàng Nhà nước Việt Nam quy định") but not the period, the day count or the base. The Law gives 15 days (L4).
    L4: `#ASSERT REFUSED` on the interest, in `vn11-tests.l4`.
15. **Before the first premium, no rule.** src:151.
    The non-payment, grace and lapse rules apply "Sau khi đóng phí bảo hiểm lần đầu"; the effective date runs from the application, so a death between the effective date and the first premium is in force on Art 1.5 and unaddressed by Art 5.
    L4: `Finding 15`, refused.
16. **The death benefit has no floor.** src:83-93.
    (i) plus (ii) less (iii) has no lower bound, so with Art 3(b)'s 20% for a child of Age 0 and a large overdue premium the formula goes negative. Theoretical: premiums that large against the sum insured are not realistic.
    L4: `Finding 16`, -5 million.

## 5. Answer table

The death benefit on a sum insured of 1,000,000,000 dong with no rider benefit and nothing unpaid, by Age at death (Art 3(b), src:108-126; generated from the raw text in `vn11-tests.l4`):

| Age at death (Art 1.4) | row as written | percentage | death benefit (VND) |
| --- | --- | --- | --- |
| 0 | Dưới 1 tuổi | 20% | 200,000,000 |
| 1 | Dưới 2 tuổi | 40% | 400,000,000 |
| 2 | Dưới 3 tuổi | 60% | 600,000,000 |
| 3 | Dưới 4 tuổi | 80% | 800,000,000 |
| 4 and over | Từ 4 tuổi trở lên | 100% | 1,000,000,000 |

The periods, each with both its edges tested (fork F2: the start day is day 0; the last day is inside):

| period | from | last day inside (example) | Article |
| --- | --- | --- | --- |
| 14 days to cancel | receipt of the contract, 5 Feb 2020 | 19 Feb 2020 | Art 4, src:185-188 |
| 60 days of grace | due date, 15 Jan 2023 | 16 Mar 2023 | Art 5, src:155-156 |
| 2 years, contest | issue or latest reinstatement, 1 Feb 2020 | 1 Feb 2022 | Art 10, src:268-276 |
| 2 years, suicide | issue or reinstatement, 1 Feb 2020 | 1 Feb 2022 | Art 11, src:278-288 |
| 2 years to reinstate | termination, 17 Mar 2023 | 17 Mar 2025 | Art 14, src:298-303 |
| 1 year to claim | the death, 10 May 2023 | 10 May 2024 (plus days of force majeure) | Art 16, src:364-370 |
| 2 months before interest | the claim, 10 Jan 2024 | 10 Mar 2024 (day 60) | Art 16, src:376-383 |
| 3 years to sue | the dispute, 1 Jun 2024 | 1 Jun 2027 | Art 17, src:395-398 |

## 6. What `check.sh` prints

```
module                                    errors satisfied  failed  refused  expected
vn11-art01-02-definitions.l4                   0         0       0        0         0
vn11-art03-benefits.l4                         0         0       0        0         0
vn11-art04-07-premiums.l4                      0         0       0        0         0
vn11-art08-13-conditions.l4                    0         0       0        0         0
vn11-art14-18-administration.l4                0         0       0        0         0
vn11-death-claim.l4                            0         0       0        0         0
vn11-findings.l4                               0        16       0        0         0
vn11-nouns.l4                                  0         0       0        0         0
vn11-tests.l4                                  0       128       0        0         0
TOTAL (9 modules)                              0       144       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

`check.sh` exit 0, run on 2026-10-06 after the last change to any `.l4` file, and run again at 00:06 on 2026-10-07, after the stray file below was removed, with output identical to the table above.

No failure and no refusal is expected, and none occurs; `check.sh`'s `expected_failed` table is unchanged (every module 0).
`vn11-tests.l4` has 128 `#ASSERT` directives, 10 of them `#ASSERT REFUSED … BECAUSE "…"` (each of the document's silences is reached by one), and 8 `#TRACE` directives for the regulative rules of Arts 4, 5 and 16, which `check.sh` does not count; their results were read by hand: the premium paid on day 0 or day 60 is `FULFILLED`, on day 61 or never it is `BREACH` with the lapse reason; a death benefit paid on day 60 is `FULFILLED`, on day 61 it leaves the duty to pay with interest standing, and paid with interest it is `FULFILLED`.
`vn11-findings.l4` has 16 `#ASSERT` directives, 4 of them `REFUSED`, each pinning a defect as the instrument has it (section 4).
The rule modules carry no assertions of their own.

To show the harness can fail, a scratch copy of the modules (outside this directory) with three expected values in `vn11-tests.l4` deliberately altered (995,000,000 to 990,000,000; 3,000,000 to 4,000,000; the insurable Age 60 to 61) was run with `l4 run`: 3 assertions failed, 125 satisfied, 3 `DiagnosticSeverity_Error` lines, and `l4 run` still exited 0, which is why the totals above come from `check.sh` and not from an exit code.

Every run prints two Warnings that differing copies of `prelude` and `daydate` exist under `~/.local/share/jl4/libraries/`; the binary uses its embedded copies, and the warnings are not errors.
The machine was heavily loaded during the run (load average about 300, from the other encoders), so `l4 run` on the tests module took minutes; that affects time, not results.

## 7. The `vnsrc check` line

**The gate**, as the lead set it on 2026-10-06, is the brief's command over every `.l4` and every `.md` file in this directory except `BRIEF.md` (the lead's file). Run from this directory:

```
$ python3 -I tools/vnsrc.py check ../../source/raw/manulife-term-life.txt *.l4 COMPARABLES.md GLOSSARY.md NOTES.md PROGRESS.md SOURCE-LICENSE.md
vnsrc check: 162 src: lines, 457 Vietnamese runs, 0 problems
```

The brief's literal command, `python3 -I tools/vnsrc.py check ../../source/raw/manulife-term-life.txt *.l4 *.md`, also checks `BRIEF.md`, and ends:

```
vnsrc check: 162 src: lines, 467 Vietnamese runs, 1 problems
```

Its one problem is reported at `BRIEF.md:23`: the brief quotes the heading's letter reference ("Kèm theo Công văn số …") as one continuous phrase, but the two-column rendering splits it across src:3, 5, 50 and 52 with other lines between, so the phrase is not a verbatim run of the source.
(The problem line itself is not reproduced here, because quoting it would make this file fail the check.)

## 8. Open questions for a domain expert

1. Does Law 08/2022/QH15 govern contracts written on this 2002 template, and if so do its Arts 30, 31, 35, 40 and 41 displace Arts 4, 11, 16 and 8 here (L1-L7)?
2. Is "Phạm tội" in Art 3(c)(i) read in practice as the insured's own crime, and does it include crimes of negligence (findings 1, 2)?
3. What is the issue date ("ngày cấp Hợp đồng bảo hiểm") in Manulife's practice, and how far after the effective date does it fall (F3, finding 4)?
4. How is a child insured's application signed in practice, given Art 1.5 (finding 10)?
5. Which published rate is "lãi suất nợ quá hạn do Ngân hàng Nhà nước Việt Nam quy định", and how is late-payment interest computed (finding 14)?
6. On avoidance under Art 10, what does the Company return (finding 5)?
7. Is the Art 9 reduction of the sum insured proportional, or read off the rate table (F14)?
8. Who receives a refund under Arts 3(c), 9 and 11 when the policyholder is the insured and has died (F23)?
9. What counts as "chi phí và phí tổn phát sinh hợp lý" (finding 7)?
10. Has this template been amended since 2002? The document shows no later version, and the vintage encoded is the PDF at its URL on 2026-10-06 (created 20 September 2023 by its metadata).
