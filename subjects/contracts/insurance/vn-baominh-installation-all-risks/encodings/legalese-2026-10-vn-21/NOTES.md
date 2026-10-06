# NOTES — Bảo Minh erection all risks rules, encoding row `legalese-2026-10-vn-21`

"Quy tắc bảo hiểm mọi rủi ro lắp đặt", Tổng Công Ty Cổ Phần Bảo Minh, 6 pages, encoded in L4 by one agent in one session (run `VN-21-20261006`, encoder `enc-vn-21`, worked 2026-10-06 to 2026-10-07) from `BRIEF.md`.
Status: **draft**. No domain expert has read it against the source; HG1 has not been sought.
`src:N` everywhere means line N of `../../source/raw/baominh-ear.txt` (the `pdftotext -layout` rendering of the PDF with sha256 `ae94994e3a5eabe428ea4bdef129b8dda8243aae32ead2b58422f2d5455d163a`).

## 0. Build and run

- `l4`: `/Users/mengwong/.local/bin/l4`, a symlink to `~/.cabal/bin/l4`, sha256 `64bbcb157dbef2ef1020a6a75589313bba0a2aeeb807c921c5e65e62e9eca118`. It has no `--version`; no record beside it names its commit. `JL4_LIBRARY_PATH` unset; every run prints two Warnings that differing copies of `prelude` and `daydate` exist under `~/.local/share/jl4/libraries/` and that the embedded copies are used. They are not errors.
- Command: `L4=/Users/mengwong/.local/bin/l4 ./check.sh` from this directory.
- The `.l4` files are generated from templates by a script that replaces each `{{src N M}}` placeholder with the output of `python3 -I tools/vnsrc.py quote ../../source/raw/baominh-ear.txt N M`; no `src:` line was typed. The templates and the script are in the session scratchpad (`scratchpad/vn21/tpl/`, `build.sh`, `expand.py`); the deposited `.l4` files are the outputs and stand alone.
- `check.sh` totals: see section 6.

Modules (`@lang en`, ASCII names):

| module | what it holds |
| --- | --- |
| `bm-ear-nouns.l4` | every DECLARE: parties, causes, kinds of property, the works, schedule items, the schedule, the questionnaire answers, the policy, the Insured's duties and conduct, the occurrence, Part I losses, Part II liabilities, the dispute, the claim; and the vocabulary of the answers (grounds of non-liability) and of the regulative rules (acts) |
| `bm-ear-period.l4` | the period of insurance, src:40-57 |
| `bm-ear-general-exclusions.l4` | general exclusions (a)-(d) and the burden-of-proof clause, src:16-37 |
| `bm-ear-general-conditions.l4` | the preamble, src:5-13, and General Conditions 1-9, src:60-150; the grounds that defeat a whole claim |
| `bm-ear-part1-material-damage.l4` | Part I, src:153-242: insuring clause, debris, exclusions 1-6, Articles 1-4, the amount |
| `bm-ear-part2-third-party.l4` | Part II, src:245-314: insuring clause, costs, exclusions 1-3, conditions 1-2, the amount |
| `bm-ear-duties.l4` | regulative rules for the duties with a deadline or a sequence (GC4(b), GC5, GC7, Part II conditions 1-2) |
| `bm-ear-fixtures.l4` | named test cases and builders; no directives |
| `bm-ear-tests-period.l4`, `-general.l4`, `-part1.l4`, `-part2.l4`, `-duties.l4`, `-findings.l4` | tests; `-duties` holds the traces; `-findings` demonstrates section 4 |

## 1. What is encoded and what is not

**Encoded: the whole document.** The preamble, the four general exclusions and the burden-of-proof clause, the period of insurance, General Conditions 1-9, Part I (insuring clause, debris clearance, six exclusions, Articles 1-4) and Part II (insuring clause, costs, three exclusions with four limbs, two conditions).
Layer 1 (is it covered?) is a list of grounds of non-liability, each naming its clause, for each Part I loss and each Part II liability; covered means the list is empty.
Layer 2 (how much?) computes Bao Minh's liability for one occurrence under each Part.
Layer 3 (who must do what, by when?) is the duties as facts read by General Condition 1, the two time-bars as date functions, and seven regulative rules exercised by traces.

**Inputs, not gaps.** The schedule ("Phụ lục") is not in the document. Every sum insured, full value, limit, deductible, debris sum and the end date of cover is therefore an input with no default; the document prints no money figure at all. The questionnaire's questions are not in the document either; the record holds only whether the answers were given and whether they were true and complete.

**Not encoded:** nothing in scope. Inert text: the title (src:1-2), the page footers (src:49, 108, 167, 226, 286, 319), the headings, and General Condition 2 (src:67-71), whose only work is to bring the schedule into the policy (which is why its figures are inputs) and to give defined words their meaning throughout, when the document defines none. The Law on Insurance Business is not encoded; where it would fill or override a clause, the fork register says so with the Law's line number.

**What the encoding declines, by name (`REFUSE`):** an occurrence on the same day as an event that starts or ends cover (F07); the burden of proof where Bao Minh alleges exclusion (a) (F03); the adjustment of cover or premium after a material change (GC4(b)); the 14-day bar before 14 days have run with no notice; Article 1 average on an item other than 1, 2 and 4 (F23); Bao Minh's proportion under GC9 when none is determined (F20); Part II damages before liability is established.

## 2. Coverage table

Totals: **56 rows: 52 encoded, 4 inert, 0 out-of-scope, 0 reached-and-refused as a whole provision** (four encoded provisions also refuse in one case each; see section 1). No row is `deferred`.
Headings are as the document writes them; a clause with no heading is identified by its number and opening words.

| # | heading as written | English gloss | src | disposition | where in the L4 |
| --- | --- | --- | --- | --- | --- |
| 1 | "QUY TẮC" / "BẢO HIỂM MỌI RỦI RO LẮP ĐẶT" | title | 1-2 | inert: a title decides nothing | nouns header comment |
| 2 | preamble, "Trên cơ sở" | the proposal, questionnaire and declarations form part of the policy | 5-8 | encoded | `the answers that form part of` (general-conditions); `The answers in the questionnaire and the proposal form` (nouns) |
| 3 | preamble, "Đơn bảo hiểm này xác nhận với điều kiện" | premium condition; Bao Minh's promise to indemnify | 10-13 | encoded | `the premium condition in the preamble is met for`; ground `preamble: ...` |
| 4 | "CÁC ĐIỂM LOẠI TRỪ CHUNG", chapeau | general exclusions, directly or indirectly | 16-19 | encoded | `was caused, directly or indirectly, by one of` |
| 5 | general exclusion "a)" | war, strikes, riot, confiscation and the rest | 21-26 | encoded | `the risks general exclusion (a) lists` |
| 6 | general exclusion "b)" | nuclear risks | 28 | encoded | `the risks general exclusion (b) lists` |
| 7 | general exclusion "c)" | wilful act or wilful negligence of the Insured | 30 | encoded | `the risks general exclusion (c) lists` |
| 8 | general exclusion "d)" | cessation of work | 32 | encoded | `the risks general exclusion (d) lists` |
| 9 | burden clause, "Trong các trường hợp khiếu tố" | burden of proof under exclusion (a) | 34-37 | encoded (refuses Bao Minh's allegation, F03) | `the burden of proof where exclusion (a) is alleged by` |
| 10 | "THỜI HẠN BẢO HIỂM", commencement | cover begins | 42-43 | encoded | `the day cover on the item began`; `the day cover under the policy began` |
| 11 | same, end | handover, first test operation, four weeks | 43-46 | encoded | `the events that end cover on the works`; `the last day of the testing period` |
| 12 | same, "Tuy nhiên, nếu một bộ phận" | partial termination, with liabilities arising from the part | 46-51 | encoded | `the events that end cover on the item as a part`; Part II period |
| 13 | same, second-hand items | second-hand items off cover when testing begins | 53-54 | encoded | `the events that end cover on a second-hand item` |
| 14 | same, "Chậm nhất" | latest end; extension needs prior written consent | 56-57 | encoded | `the last day of cover under the schedule` |
| 15 | "ĐIỀU KIỆN CHUNG" 1 | conditions precedent: duties and answers | 62-65 | encoded | `General Condition 1: the duties breached in`; `under ... , General Condition 1 is met by` |
| 16 | "ĐIỀU KIỆN CHUNG" 2 | schedule part of the policy; defined words | 67-71 | inert: no case turns on it; the document defines nothing for it to carry | comment in general-conditions |
| 17 | "ĐIỀU KIỆN CHUNG" 3 | precautions, recommendations, manufacturer's rules | 73-75 | encoded | `the duties General Condition 3 imposes` |
| 18 | "ĐIỀU KIỆN CHUNG" 4 a) | inspection; information to assess the risk | 77-79 | encoded | `the duties General Condition 4(a) imposes` |
| 19 | "ĐIỀU KIỆN CHUNG" 4 b), notice of change | notify material change by telegram and in writing; precautions | 81-85 | encoded | `the duties General Condition 4(b) imposes`; `General Condition 4(b): notify a material change` (duties) |
| 20 | same, adjustment | cover or premium adjusted "if necessary" | 84-85 | encoded (refuses: no criterion) | `General Condition 4(b) gives no criterion for adjusting ...` |
| 21 | same, last paragraph | no material change increasing risk without approval | 87-89 | encoded | duty in list; `General Condition 4(b): no material change increasing the risk without written approval` (SHANT) |
| 22 | "ĐIỀU KIỆN CHUNG" 5 a)-e) | claims duties | 91-105 | encoded | `the duties General Condition 5(a)-(e) imposes`; GC5 and GC5(e) regulative rules |
| 23 | same, "Trong mọi trường hợp" | 14-day receipt bar | 109-111 | encoded | `General Condition 5: Bao Minh received notice in time of`; ground |
| 24 | same, "Sau khi thông báo" | minor repairs; inspection; reasonable time | 113-117 | encoded | `General Condition 5: after notice` (MAY chain); implied duty (F11) |
| 25 | same, last sentence | liability ceases for an item not repaired promptly and properly | 119-120 | encoded | `General Condition 5: liability for the item had ceased before` |
| 26 | "ĐIỀU KIỆN CHUNG" 6 | subrogation | 122-129 | encoded | `the duties General Condition 6 imposes` |
| 27 | "ĐIỀU KIỆN CHUNG" 7 | arbitration of the amount; award a condition precedent | 131-139 | encoded | `General Condition 7: the last day to appoint ...`; `General Condition 7 does not bar an action ...`; appointment rule (duties) |
| 28 | "ĐIỀU KIỆN CHUNG" 8, fraud | forfeiture for fraud or false declaration | 141-143, 146 | encoded | `General Condition 8: all benefit is forfeited for` |
| 29 | same, rejection | three months after an award | 143-146 | encoded | `General Condition 8: the rejected claim is barred` |
| 30 | "ĐIỀU KIỆN CHUNG" 9 | other insurance, rateable proportion | 148-150 | encoded | `General Condition 9: Bao Minh's share, in` |
| 31 | "PHẦN I - TỔN THẤT VẬT CHẤT", insuring clause | sudden and unforeseen physical loss; option; limits | 155-163 | encoded | `the Part I insuring clause does not reach`; `the period of insurance covers`; amount rules |
| 32 | same, debris | clearance of debris if a sum is stated | 168-170 | encoded | `Part I: the clearance of debris covered in` |
| 33 | "Điều Khoản Loại Trừ Chỉ Áp Dụng Riêng Cho Phần I" 1 | deductible | 176 | encoded | `Part I exclusion 1: the deductible for the occurrence in` |
| 34 | same 2 | consequential loss | 178-179 | encoded | `Part I exclusion 2: the consequential losses excluded from` |
| 35 | same 3 | faulty design, material, casting, workmanship (not erection) | 181-182 | encoded | `the causes Part I exclusion 3 lists` |
| 36 | same 4 | corrosion, wear, oxidation, scaling | 184 | encoded | `the causes Part I exclusion 4 lists` |
| 37 | same 5 | documents, money, securities, packaging | 186-187 | encoded | `the kinds of property Part I exclusion 5 lists` |
| 38 | same 6 | discovered only at inventory | 189 | encoded | `the Part I exclusions that apply to` |
| 39 | "Điều 1 - Số tiền bảo hiểm", first paragraph | sum insured not less than full value; undertaking to adjust | 193-198 | encoded | `Article 1: the sum insured is not less than the full value of`; duty in list |
| 40 | same, second paragraph | average | 200-203 | encoded (refuses for items other than 1, 2, 4) | `Article 1: the proportion of the loss recoverable on` |
| 41 | "Điều 2 - Cơ sở giải quyết bồi thường" a), b) | repair basis; total-loss basis | 205-212 | encoded | `Article 2(a): the repair basis for`; `Article 2(b): the total-loss basis for` |
| 42 | same, "Tuy nhiên" | actually incurred; included in the sum insured; compliance | 214-216 | encoded | `Article 2: the basis of settlement for` |
| 43 | same, invoices; constructive total loss | pay after invoices; repair at or above value goes to (b) | 218-222 | encoded | `Article 2: payment may now be made for`; basis choice |
| 44 | same, temporary repairs | temporary repairs if part of permanent, not increasing cost | 227-228 | encoded | `Article 2: the temporary repairs borne by Bao Minh in` |
| 45 | same, alterations | no alterations, additions, improvements | 230-231 | encoded | alterations subtracted from costs incurred |
| 46 | "Điều 3 - Mở rộng phạm vi bảo hiểm" | overtime, night, holiday work, express freight only if agreed | 233-235 | encoded | `Article 3: the extra charges covered in` |
| 47 | "Điều 4 - Tài sản xung quanh" | surrounding property | 237-242 | encoded | `Article 4 does not reach` |
| 48 | "PHẦN II – TRÁCH NHIỆM ĐỐI VỚI BÊN THỨ BA", insuring clause | third-party injury and property damage | 247-256 | encoded | `the Part II insuring clause does not reach` |
| 49 | same, costs | claimant's costs; costs with written consent; within the limit | 258-266 | encoded | `Part II: the costs covered on`; amount rule |
| 50 | "Những Loại Trừ Áp Dụng Riêng Cho Phần II" 1 | deductible | 272 | encoded | `Part II exclusion 1: the deductible for the occurrence in` |
| 51 | same 2 | redoing what Part I covers | 274-275 | encoded | `the Part II exclusions that apply to` |
| 52 | same 3 a)-d) | employees, connected firms' property, vehicles and craft, contractual liability | 277-297 | encoded | `the Part II exclusions that apply to`; `the causes Part II exclusion 3(c) lists` |
| 53 | "Các Điều Kiện Áp Dụng Riêng Cho Phần II" 1 | no admission without consent; Bao Minh may take over | 301-308 | encoded | `the duties Part II condition 1 imposes`; two regulative rules |
| 54 | same 2 | Bao Minh may pay the limit or a settlement sum | 310-314 | encoded | `Part II condition 2: Bao Minh may pay ...`; amount rule |
| 55 | page footers, "BảoMinh - Mọi rủi ro lắp đặt ( Munich Re)" | footer: product name, Munich Re, document number 1782/2004-BM/BHTS, page | 49, 108, 167, 226, 286, 319 | inert: page furniture; the attribution is reported in COMPARABLES.md | none |
| 56 | headings ("Điều Khoản Áp Dụng Cho Phần I" and the others above) | headings | 60, 153, 172, 191, 245, 268, 299 | inert: headings are carried as `§` titles | `§` sections |

## 3. Fork register

Every ambiguity met, the readings seen, the one taken, and the text for each.
"Điều 24" is the Law on Insurance Business, Article 24 (Law lines 588-591): an unclear clause is read in favour of the purchaser. It is noted where it would choose differently; it was not used to choose. `LAW:` marks a mandatory provision that may fill or override the document.

| # | where (src) | question | readings | taken, and why |
| --- | --- | --- | --- | --- |
| F01 | preamble 5-8; GC1 62-65 | Who owes disclosure? | (i) the Insured named in the schedule; (ii) a separate purchaser | **(i)**: the document names no other party. `LAW:` the Law puts the duty to declare on the purchaser (Law 512-515, 537-542); for a policy where purchaser and insured differ, the Law's party governs. |
| F02 | GC1 62-65 | Does a breach of ANY duty defeat EVERY claim? | (i) yes, literally; (ii) only a breach connected with the claim; (iii) only material breaches | **(i)**, the words: "điều kiện tiên quyết" with no qualifier. Điều 24 would favour (ii). `LAW:` Law 46 (917-932) lets an insurer reduce a payment only in proportion to the harm a late notice caused, and not at all where no sanction is agreed or there is force majeure; Law 19(3) (441-444) forbids applying a late-notice exclusion after force majeure. Findings 3, 20. |
| F03 | burden clause 34-37 | Whose allegation shifts the burden? | (i) the Insured's, as written; (ii) Bao Minh's, the evident purpose | **(i)**, the words; Bao Minh's allegation is refused by name. Điều 24 agrees with (i). Finding 5. |
| F04 | GC1 63-64 | Is the condition that the questions were answered, or that the answers were true? | (i) answered; (ii) true and complete ("chấp hành đúng" carrying over) | **(ii)**: the grammar allows it and the clause has no work to do under (i). Both readings are encoded as named values. Điều 24 would favour (i). `LAW:` Law 22(2) (543-553) lets the insurer avoid only for INTENTIONAL non-disclosure or falsehood made to obtain payment. Findings 2, 21. |
| F05 | preamble 10-11 | By when must the premium be paid? | (i) before the occurrence; (ii) at any time before payment of the claim; (iii) by a date in the schedule | **(i)**, recorded as a fact at the occurrence; the document gives no date. `LAW:` Law 26(1), 27(1)(c) (627-657): for non-payment the insurer may terminate, but remains liable for events before termination, with a right to deduct premium. |
| F06 | 42-43 | When does cover on an item begin? | (i) the earlier of works commencement and the item's unloading; (ii) the later; (iii) unloading only (the item-specific trigger) | **(i)**: "hoặc" offers alternatives; the first to happen starts cover. Điều 24 agrees. |
| F07 | 42-54 | An occurrence on the same DAY as an event that starts or ends cover | (i) inside; (ii) outside; (iii) undecidable from a date | **(iii)**: the events are instants ("from the moment", "after unloading is completed", "until after handover"); a date cannot order them. The rule refuses by name. |
| F08 | 45-46 | "4 tuần ... kể từ ngày bắt đầu chạy thử" | (i) 28 calendar days from the day the WORKS' testing began; (ii) from each item's own testing | **(i)**: the sentence is about cover as a whole; the item-level limb is the partial-termination sentence. |
| F09 | 45, 56 | Is the last day of a date limit inside? | (i) yes; (ii) no | **(i)**: "không chậm quá" (not later than) and "vào ngày" (on the date) read inclusively; day 28 and the schedule date are covered. Điều 24 agrees. |
| F10 | 46-47 | "đã được chạy thử" for a part | (i) its test run completed; (ii) its testing begun | **(i)**: under (ii) the four-week allowance would never reach a part, contradicting the sentence before. |
| F11 | 113-117 | Is repairing before inspection a breach? | (i) an implied duty, a condition precedent under GC1; (ii) no duty, only Bao Minh's opportunity | **(i)**, recorded as a duty in the list, flagged as implied; the trace models the permission sequence only. |
| F12 | 119-120 | "liability for any damaged item ceases" | (i) for later occurrences on that item; (ii) also for the loss in hand | **(i)**: the loss in hand is governed by Article 2's invoices condition; (ii) would make the sentence and Article 2 duplicate each other. Điều 24 agrees. |
| F13 | 109-111 | Counting the 14 days | (i) calendar days, day of occurrence not counted, RECEIPT on day 14 in time; (ii) the day of occurrence counted; (iii) working days | **(i)**: "ngày" unqualified; receipt because the text says "không nhận được". Outside knowledge, unverified: the Civil Code's rules for computing periods may differ. `LAW:` Law 19(3) and 46 (see F02). |
| F14 | 161-162 | "hạn mức trách nhiệm bồi thường đó" — which limit? | (i) a per-occurrence limit stated in the schedule, if one is; (ii) the item's sum; (iii) none | **(i)**: a MAYBE input; NOTHING means no per-occurrence limit. |
| F15 | 160-163, 176, 200-203, 214 | The order of the Part I arithmetic; whether the per-item cap is per occurrence or cumulative | order: basis, average, item cap, debris, deductible, occurrence limit, aggregate, GC9; per-item cap per occurrence | taken as listed (module header). The document gives no order. A cumulative per-item cap would need each item's earlier payments, which the aggregate already tracks in total. |
| F16 | 160 | Cash, repair or replacement "at Bao Minh's option" | (i) the amount is computed in money; (ii) model the choice | **(i)**: the option is a mode of settlement, not a measure. It conflicts with Article 2 (Finding 9). |
| F17 | 19; 181-184; 277, 292 | "directly or indirectly" / "due to" with several causes | (i) any listed cause on the record excludes; (ii) the dominant cause only | **(i)** for the general exclusions (their words); applied alike to Part I exclusions 3-4 and Part II 3(c). Exclusion 4 lists conditions without "due to"; read as causes. Điều 24 would favour (ii) for the Part I and Part II lists. |
| F18 | 134-135, 144 | "một tháng", "ba tháng" | (i) calendar months, same day of the month, clamped to the month's last day; (ii) 30 or 90 days | **(i)**, via `add months`. |
| F19 | 143-146 | GC8's three-month bar: from what? | (i) from an arbitral award only, as translated; (ii) from the rejection, or from the award where there is arbitration (the evident source wording) | **(i)**, the words: there is no anchor at the rejection. Điều 24 agrees. Finding 6. |
| F20 | 148-150 | Basis of Bao Minh's proportion | (i) sum-insured basis; (ii) independent-liability basis; (iii) not stated | **(iii)**: an input when determined, a named refusal otherwise. `LAW:` Law 49 (964-973) fixes a sum-insured basis for double insurance where the total sums insured exceed market value. |
| F21 | 168-170 | Debris clearance: when, and inside which limits? | (i) only with a covered Part I loss, inside the deductible, occurrence limit and aggregate; (ii) separately | **(i)**: "after an occurrence giving rise to a claim under this Policy"; the separate sum caps it. |
| F22 | 181-182 | Carve-back "nhưng không phải do lỗi trong lắp đặt" | (i) qualifies bad workmanship only; (ii) the whole exclusion | **(i)**: an erection fault is a kind of workmanship. A loss also caused by faulty design is excluded. Điều 24 would favour (ii). |
| F23 | 193-203, 241 | Average for items other than 1 and 2 | (i) item 4 against the value of the surrounding property, other items refused; (ii) no average outside 1 and 2; (iii) refuse all | **(i)**: Article 4 requires "the value of that property" to be stated; for any other item the text gives no measure, so refused (Finding 8). |
| F24 | 227-228 | Temporary repairs that increase cost | (i) none borne; (ii) only the increase disallowed | **(i)**, the words: borne "if" both conditions hold. Điều 24 would favour (ii). |
| F25 | 56-57 | Does an extension move the four-week testing limit? | (i) no, only the schedule date; (ii) yes | **(i)**: the four weeks have their own "unless otherwise agreed in writing". |
| F26 | 214-215 | "to the extent included in the sum insured" | (i) subtract the part of the repair cost of a kind not in the sum insured, in basis (a); (ii) also in (b) | **(i)**: for a total loss the actual value is the measure and has no separable "kind". |
| F27 | 220-222 | "chi phí sửa chữa" for the constructive-total-loss test | (i) the gross restoration cost; (ii) net of salvage | **(i)**. |
| F28 | 279-281, 287-290 | "được bảo hiểm toàn bộ hay chỉ một phần theo Phần I" | (i) describes the works; (ii) describes the property (only property insured under Part I excluded) | **(i)**: in 3(a) it cannot describe injured people, and the two limbs are parallel. |
| F29 | 258-266, 272, 310-311 | Part II arithmetic | deductible on damages plus costs; limit per occurrence; no aggregate | taken as listed; condition 2 calls the limit "per occurrence", and no aggregate is stated. |
| F30 | 258-260 | Costs where the Insured is held not liable | (i) covered if the claim is within Part II's scope; (ii) covered only with a liability indemnified | **(i)**: "claims ... resolved under the provisions of this Policy" include a claim defended under Part II condition 1. Điều 24 agrees. |
| F31 | 148-150 | GC9 for Part I and Part II | (i) one record of other insurance for the claim; (ii) separate per Part | **(i)**, a simplification; a claim with other insurance on one Part only needs two runs. |
| F32 | 81-82, 94-95 | Notice "by telegram" | (i) the record says whether the duty was complied with; (ii) decide which channels count | **(i)**: not decided here (Finding 14). |
| F33 | 155-163 | Where must a Part I loss happen? | (i) nowhere stated; (ii) at the site | **(i)**: Part I has no location limb, unlike Part II and Article 4. |
| F34 | 233-235 | Article 3 extra charges, when agreed | (i) added to the basis, inside the item and occurrence limits; (ii) a separate limit | **(i)**: no separate figure is mentioned. |
| F35 | 114, 116 | "hư hỏng nhỏ", "thời gian ... hợp lý" | inputs (a fact found and a number of days found) | inputs; the document gives no measure (Finding 12). |

Where I looked for more and found none: the units of every period (14 days, 4 weeks, one month, three months), every "and/or" (src:47, 84, 230), every "hay"/"hoặc" in a list of conditions, every cross-reference (the general exclusions "above" and "below", Article 4's "Part I item 4", Article 1's "items 1 and 2").

## 4. Findings

The hostile reading. Each finding gives the source lines, a minimal scenario, and the evidence (an assertion in `bm-ear-tests-findings.l4` unless stated) or the words `reading only`. A finding is a defect or a surprise in the instrument as written; a fork (section 3) is an ambiguity resolved.

1. **The 14-day notice bar runs from the occurrence, counts receipt, and cannot be met for latent damage.** src:109-111. Damage occurs 1 June, hidden; found 20 June; notice received 21 June: Bao Minh is not liable under either Part (`a latent loss, notified the day after it was found`: grounds `GC5: ...`, Part I 0, Part II 0). The duty itself is "immediately" (src:94); the bar is absolute ("Trong mọi trường hợp"). `LAW:` Law 46 (917-932) and 19(3) (441-444) allow only a proportionate reduction and exclude force majeure (fork F02); a policyholder may rely on them, but the policy as written gives nothing.
2. **One innocent, immaterial wrong answer in the questionnaire defeats every claim.** src:62-65 with src:5-8. Under reading (ii) of GC1, an incomplete answer, however trivial and however unrelated, leaves Part I 0 and Part II 0 where the same claim otherwise pays 900,000,000 and 330,000,000 (`a claim after an incomplete answer`). The policy asks nothing about intent, materiality or connection, and provides no proportionate remedy.
3. **Every duty is a condition precedent, with no connection test.** src:62-65. An unrelated breach of a manufacturer's recommendation (GC3) leaves Part I at 0; a late police report of an unrelated theft (GC5(e)) leaves a Part II injury claim at 0.
4. **General Condition 1 makes Article 1's average redundant.** src:193-203 with 62-65. Article 1's undertaking to adjust the sum insured is something the Insured "must do", so its breach is a condition precedent failure: an underinsured item pays 0 instead of the average figure 710,000,000 (`an underinsured claim` against `the same claim, with the undertaking recorded as broken`).
5. **The burden-of-proof clause names the wrong party.** src:34-37. It shifts the burden when THE INSURED contends exclusion (a) applies, which an insured never does, and is silent when Bao Minh does. Evidence: `#ASSERT REFUSED ... alleged by Bao Minh`. A Vietnamese court may read it purposively; as written it never helps the insurer.
6. **The three-month bar on suit, as translated, never reaches a claim that was simply rejected.** src:143-146 with 131-132. The bar runs only "from when the arbitrators made their award"; but arbitration takes only disputes about the amount with liability admitted. A claim rejected outright cannot be arbitrated, so no bar starts (`NOT ... the rejected claim is barred` in 2030). The evident source wording also ran from the rejection; that limb is missing.
7. **No award, no action; and nothing makes a party appoint.** src:131-139. An award is a condition precedent to any action on the amount; a party who ignores the written request to appoint within one month suffers nothing, because the clause states no consequence and appoints no one in default. Evidence: `NOT General Condition 7 does not bar an action ...` with no award; the trace in `bm-ear-tests-duties.l4` ends in a breach by Bao Minh with no consequence attached.
8. **Average has no measure for most of the schedule.** src:193-203. "Every item ... separately" is subject to average, but the amount that ought to have been insured is stated only for items 1 and 2 (and, on fork F23, item 4). Evidence: `#ASSERT REFUSED Article 1: the proportion ... item 3`.
9. **A total loss pays nothing until the Insured has paid for the replacement itself.** src:155-160, 211-222. The insuring clause promises indemnity "in cash, or by repair or replacement, at Bao Minh's option", but Article 2 pays only "costs actually incurred" and only after invoices showing the replacement was made. An Insured who cannot fund replacement recovers 0 on a destroyed item worth 8,000,000,000 (`a total loss not yet replaced`: no ground of non-liability, amount 0).
10. **Surrounding property damaged by construction work falls between the Parts.** src:237-242, 255, 287-290. Article 4 requires a direct connection with ERECTION OR TESTING; Part II names construction, but exclusion 3(b) excludes the principal's property. The principal's building next to the site, damaged by the civil works: Part I 0, Part II 0 (`the gap claim`).
11. **Repair is both a precondition of payment and a condition of continuing cover.** src:119-120, 218-222. Bao Minh pays only after repair invoices, and its liability for an item ends if the item is not repaired "promptly and properly". An Insured short of cash loses the payment for the first loss and the cover for the next. Reading only (the second limb is encoded as fork F12 and tested in `bm-ear-tests-part1.l4`).
12. **Words that carry weight are never defined.** General Condition 2 says defined words keep their meaning throughout, but the document defines only the insurer's short name. Undefined: "sự cố" (occurrence, by which every deductible and limit counts), "thay đổi quan trọng" (material change), "hư hỏng nhỏ" (minor damage), "một thời gian được xem là hợp lý" (a reasonable time), "kịp thời chu đáo", "đại diện" (representative), "bên thứ ba" (third party), "hạng mục sử dụng lại". The two deductibles carry two different words, "mức khấu trừ" and "mức miễn thường". Reading only.
13. **"Cessation of work, whole or partial" excludes losses during an ordinary stoppage.** src:32. No minimum duration: a theft over a weekend when work had stopped is excluded (`Part I ... (LIST theft, cessation of work ...)` gives 0).
14. **Notices must go by telegram.** src:81-82 (telegram AND in writing), 94-95 (telephone or telegram AS WELL AS in writing). If no telegram service is available to the Insured, a question of fact outside the document, General Condition 4(b) cannot be complied with as written, and under General Condition 1 that defeats every claim. Reading only.
15. **Bao Minh may adjust cover or premium after a material change with no criterion.** src:84-85. Evidence: `#ASSERT REFUSED the premium as adjusted after a material change` in `bm-ear-tests-general.l4`.
16. **A false declaration in one claim forfeits every claim.** src:141-146. "All benefits under this Policy" lose their value: an honest claim after a false declaration in an earlier one pays 0 under both Parts (`a record of a false declaration in an earlier claim`).
17. **Part II condition 2 lets Bao Minh pay what it judges the claim can be settled for and walk away.** src:310-314. Who judges "can be settled" is not said; afterwards the Insured's further defence costs are its own. Evidence: Part II 0 after a condition 2 payment.
18. **General Condition 9 has no basis for the proportion.** src:148-150. Evidence: `#ASSERT REFUSED` on a Part II claim with other insurance and no proportion determined.
19. **Translation and typesetting defects.** "khôngg" (src:144), "băng văn bản" for "bằng" (src:133), "vật liệu vật liệu" (src:187), "khởi nghiã" (src:22), an unclosed parenthesis in the preamble (src:7-8), "hạn mức trách nhiệm bồi thường đó" with no antecedent (src:162), the burden clause's subject (Finding 5) and GC8's missing anchor (Finding 6). Reading only.
20. **The notice bar is stricter than the Law allows.** src:109-111 against Law 46 (917-932) and 19(3) (441-444). Reading only; the Law is not encoded (fork F02).
21. **The disclosure condition is stricter than the Law allows.** src:62-65 against Law 22(2) (543-553), which requires intent. Reading only (fork F04).

The three most likely to matter to a policyholder: **Finding 1** (src:109-111), **Findings 2 and 3** (src:62-65), **Finding 9** (src:211-222).

## 5. Answer table

The document has no benefit table, schedule of rates or other table; every figure is in the schedule, which is an input. Its own numbers are periods, collected here:

| what | value | kind of day | src |
| --- | --- | --- | --- |
| notice must reach Bao Minh | within 14 days of the occurrence | calendar days, receipt (F13) | 109-111 |
| testing limit | 4 weeks from the start of testing, unless otherwise agreed in writing | 28 calendar days, last day inside (F08, F09) | 45-46 |
| appoint an arbitrator | within one month of the written request being sent | calendar month (F18) | 134-136 |
| commence proceedings | within three months of the award | calendar months (F18, F19) | 143-146 |
| notify a material change; notify a loss | immediately | none stated | 81, 94 |
| inspection before repair | a reasonable time | none stated; input | 116 |

Worked amounts the tests assert (scenario figures, not the document's; `bm-ear-fixtures.l4`):

| scenario | Part I | Part II |
| --- | --- | --- |
| standard repair (1,000,000,000 to restore, salvage 50,000,000), deductible 50,000,000 | 900,000,000 | — |
| same, item insured at 80% | 710,000,000 | — |
| constructive total loss (repair 9,000,000,000 ≥ value 8,000,000,000), replaced | 7,450,000,000 | — |
| total loss, not yet replaced | 0 | — |
| standard repair plus debris 300,000,000 (separate sum 200,000,000) | 1,100,000,000 | — |
| 80% item, temporary repairs, occurrence limit 700,000,000; then other insurance at one half | 700,000,000; 350,000,000 | — |
| injured passer-by: damages 300,000,000, costs 30,000,000 + 20,000,000, deductible 20,000,000 | — | 330,000,000 |
| damages 6,000,000,000 | — | 5,000,000,000 (limit) |

## 6. What `check.sh` prints

Run on 2026-10-07 with the `l4` named in section 0:

```
module                                    errors satisfied  failed  refused  expected
bm-ear-duties.l4                               0         0       0        0         0
bm-ear-fixtures.l4                             0         0       0        0         0
bm-ear-general-conditions.l4                   0         0       0        0         0
bm-ear-general-exclusions.l4                   0         0       0        0         0
bm-ear-nouns.l4                                0         0       0        0         0
bm-ear-part1-material-damage.l4                0         0       0        0         0
bm-ear-part2-third-party.l4                    0         0       0        0         0
bm-ear-period.l4                               0         0       0        0         0
bm-ear-tests-duties.l4                         0         2       0        0         0
bm-ear-tests-findings.l4                       0        25       0        0         0
bm-ear-tests-general.l4                        0        49       0        0         0
bm-ear-tests-part1.l4                          0        51       0        0         0
bm-ear-tests-part2.l4                          0        29       0        0         0
bm-ear-tests-period.l4                         0        32       0        0         0
TOTAL (14 modules)                             0       188       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

`check.sh` exit 0.

No failure or refusal is expected and none occurs: `expected_failed` lists no module.
Each `#ASSERT REFUSED` that is satisfied counts as satisfied. The traces in `bm-ear-tests-duties.l4` are not assertions; what they printed, checked by eye against the expectation written above each:
GC5 notice on day 14, inspection, repair: `FULFILLED`; no notice by day 15: `DEONTIC BREACHED ... BY the Insured BECAUSE "General Condition 5: Bao Minh received no notice within 14 days of the occurrence, and is not liable for the loss"`; no inspection within the reasonable time, then repair: `FULFILLED`; minor damage: `FULFILLED`; police duty with no event: the residual obligation; GC4(b) change with approval: the residual prohibition; without approval: `DEONTIC BREACHED ... BY the Insured`; notice of change: `FULFILLED`; GC7 appointment on day 28: `FULFILLED`; none by day 29: `DEONTIC BREACHED ... BY Bao Minh BECAUSE "... the policy states no consequence"`; Part II condition 1 admission with consent: residual; without: `DEONTIC BREACHED ... BY the Insured`; Bao Minh takes over: `FULFILLED`; condition 2 payment: `FULFILLED`.

## 7. The `vnsrc check` line

The gate (the lead's clarification of 2026-10-07): every `.l4` and every `.md` in this directory except `BRIEF.md`, i.e. `python3 -I tools/vnsrc.py check ../../source/raw/baominh-ear.txt $(ls *.l4 *.md | grep -v '^BRIEF.md$')`. Last line:

```
vnsrc check: 214 src: lines, 389 Vietnamese runs, 0 problems
```

The literal command of the brief, `python3 -I tools/vnsrc.py check ../../source/raw/baominh-ear.txt *.l4 *.md` (which also reads `BRIEF.md`), printed:

```
vnsrc check: 214 src: lines, 397 Vietnamese runs, 0 problems
```

## 8. Open questions for a domain expert

1. F04 / Finding 2: do Vietnamese courts read "điều kiện tiên quyết" in an insurer's rules as an all-or-nothing condition, or through Law 22's intent test?
2. Finding 1: is a 14-day receipt bar on notice enforceable against Law 46, which allows only a proportionate reduction?
3. F06: in Bảo Minh's practice, does erection cover start for an item at works commencement or only on its unloading at site?
4. F19 / Finding 6: does Bảo Minh's English or reinsurance wording (the footer names Munich Re) run the three-month bar from a rejection? Is the Vietnamese text the governing version?
5. F20: on what basis does Bảo Minh compute its "proportion" under General Condition 9 in practice?
6. Finding 9: does Bảo Minh in practice pay a total loss in cash before replacement, despite Article 2?
7. Finding 14: what does Bảo Minh accept in place of a telegram?
8. Outside knowledge, unverified: the document number 1782/2004-BM/BHTS suggests a 2004 approval; is this wording still the one Bảo Minh issues, and has the Law of 2022 (in force from 2023, outside knowledge, unverified) required a revision?

## 9. What was not done

- No independent test pass (encoding-a-subject step 8): the brief is one session with no sub-agents. Every expected value was worked by hand from the text before it was asserted, by the same session that wrote the rules.
- HG1 not sought.
- No network was used; the only source read is the deposited text, plus the Law as an aid.
- Quotation volume: the encoding quotes nearly every line of the document once, because its scope is the whole document and the brief asks for the Vietnamese before each rule; see `SOURCE-LICENSE.md` for the count, for the lead to weigh against the 2026-10-06 ruling.
