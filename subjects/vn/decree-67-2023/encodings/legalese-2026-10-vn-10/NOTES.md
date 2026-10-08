# NOTES — vn/decree-67-2023, encoding row `legalese-2026-10-vn-10`

Decree 67/2023/NĐ-CP of 6 September 2023, Chapter II Section 1: the compulsory insurance of motor vehicle owners' civil liability ("bảo hiểm bắt buộc trách nhiệm dân sự của chủ xe cơ giới"), with Chapter I as far as it needs, Annex I (the premium) and Annex VI (the bodily-injury payment table), in two vintages: as made, and as amended by Decree 220/2026/NĐ-CP of 22 June 2026.
Encoded in L4 by one agent, `enc-vn-10`, in one session (run `VN-10-20261006`, 2026-10-06), from `BRIEF.md`.
Status: **draft**.
No domain expert has read it against the source; HG1 has not been sought.

## 0. Build and run

Run on 2026-10-06 with `/Users/mengwong/.local/bin/l4`, `JL4_LIBRARY_PATH` unset.
That path is a symlink to `~/.cabal/bin/l4`, which resolves to the cabal store entry `jl4-0.1-0ee0100b` (`/Volumes/transcend/caches/cabal/store/ghc-9.10.3-fe9c/jl4-0.1-0ee0100b/bin/l4`, modified 2026-10-06 21:20 local), sha256 `64bbcb157dbef2ef1020a6a75589313bba0a2aeeb807c921c5e65e62e9eca118`.
The binary has no `--version`.
Every run prints two Warnings that differing copies of `prelude` and `daydate` exist under `~/.local/share/jl4/libraries/`; the binary uses its embedded copies, and the warnings are not errors.

The command, from this directory:

```
L4=/Users/mengwong/.local/bin/l4 ./check.sh
```

It takes about four minutes, most of it in the 1,235 generated Annex VI tests.
Totals: **14 modules, 0 errors, 1,487 assertions satisfied, 0 failed, 0 refused**; `check.sh` exit 0 (the table is in §6; last run 2026-10-07, after the last change to any module).

The three gazette PDFs were hashed before use and match `../../subject.json`: `nd67-congbao-1017-1018.pdf` `19a1de3a…1253c8`, `nd67-congbao-1019-1020.pdf` `456cbc7d…d79d59`, `nd220-2026-congbao-367.pdf` `ab0e75cd…1f3a52`.
No network was used.

Three scripts in `tools/` (run with `python3 -I`, from this directory):

- `tools/annex6.py ../../source/raw/nd67-congbao-1019-1020.txt` generates `nd67-annex6-table.l4` (the rows of Annex VI) and `nd67-annex6-tests.l4` (one test per row and per cell of the acuity table); §5.4.
- `tools/annex1.py ../../source/raw/nd67-congbao-1017-1018.txt` generates `nd67-annex1-tests.l4` (one test per row and band edge of Annex I) and prints the table of §5.1.
- `tools/vnsrc.py`, the row's quotation tool, **extended** in this row (§7): it now also checks quotations of the two other raw files.

Every `-- src:` line in the hand-written modules was printed by `tools/vnsrc.py quote` or `quoteid`, through a template expander kept outside the deposit; none was typed.

The modules, in import order:

| module | what it holds | lines |
| --- | --- | --- |
| `nd67-vn10-nouns.l4` | every `DECLARE`: vintages, vehicle classes, the contract, certificate, accident, person, injury, claim file, results and problems | 401 |
| `nd67-ch1-general.l4` | Chapter I (Articles 1-4) and which vintage governs a contract (Articles 76(1), 77(1); Decree 220 Articles 9-10) | 321 |
| `nd67-art5-7-cover.l4` | Articles 5-7: object, limits, scope, exclusions, the answer on cover | 317 |
| `nd67-art8-premium.l4` | Article 8 and Annex I | 354 |
| `nd67-art9-11-term.l4` | Articles 9-11: term, certificate, termination and refund | 173 |
| `nd67-annex6-table.l4` | GENERATED: the 1,135 rows of Annex VI and the 10 rows of its acuity table, each under its source lines | 2,734 |
| `nd67-annex6.l4` | Annex VI lookups, formula, two notes, special cases | 274 |
| `nd67-art12-13-claims.l4` | Articles 12-13: advance, payee, amounts, reduction, limit, one-contract rule, claim file | 434 |
| `nd67-art12-duties-hours.l4` | Article 12(2) as regulative rules, clock in hours | 84 |
| `nd67-art12-duties-workdays.l4` | Articles 10(1), 12(1), (3), (4), (7), (10), (11) as regulative rules, clock in working days; working-day dates | 247 |
| `nd67-tests.l4` | 180 hand-written tests from the source | 596 |
| `nd67-annex1-tests.l4` | GENERATED: 55 premium tests | 124 |
| `nd67-annex6-tests.l4` | GENERATED: 1,235 Annex VI tests | 2,397 |
| `nd67-findings.l4` | 17 assertions that state the findings' surprising answers | 156 |

The generated table module is long because the table is: one L4 row per source row, each beside the source line it encodes, so a reviewer checks it row by row against the gazette.

To show that the harness can fail, a scratch copy of the modules with three expected values in `nd67-tests.l4` deliberately altered was run through `check.sh` (§6).

## 1. What is encoded and what is not

**Encoded.**
Chapter II Section 1 in full, Articles 5 to 13.
Chapter I as the motor chapter uses it: Article 2(1); Article 3(1), (2), (3) and (5)(a); Article 4(1), (3), (4) (with Article 12(9)), (5)(a), (7) (the outer bound), (8).
The annexes Articles 5 to 13 name, which are exactly two (Article 8(1) and (2) name Annex I, src lines 233-238; Article 12(6)(a) names Annex VI five times, src lines 353, 358, 361, 367-368, 372-373; no other annex is named in Articles 5-13): **Annex I** in full (sections A, A.VII and B) and **Annex VI** in full (Parts A and B, 1,135 rows, the 10 × 10 acuity table, two of its seventeen notes, and its special cases 1, 3, 4, 5 and 6).
The transitional and commencement provisions that decide the vintage: Decree 67 Articles 76(1) and 77(1); Decree 220 Articles 9(1) and 10(1)-(2).

**Inputs, with their citations, not encoded:** whatever the Road Traffic Law decides (the vehicle kinds of Article 6(2) and Annex I, the driver's age, which vehicles need a licence); the Ministry of Health's alcohol level; the facts of the accident and the persons harmed; the medical assessment's rate within a band of Annex VI; the estimated compensation for the advance; the working-day calendar's days off; agreed and court-fixed sums.

**Declined by a named `REFUSE`:** a contract concluded before Decree 67, which Article 76(1) leaves under rules not in the sources; the premium payment deadline the Minister of Finance sets (Article 4(7)); a refund on a change of owner (Article 9(3) with Article 11); a band of Annex VI with no assessed rate; a row whose "cộng lùi" addition applies; an unlisted injury with no rate (special case 5); a number of seats Annex I does not list; two contracts concluded on the same first day (Article 12(9)).

**Not encoded (out of scope, §2):** Chapter II Section 2 (the Motor Vehicle Insurance Fund, Articles 14-22) except the insurer's right in Article 12(3) to ask it for repayment; Chapters III and IV (fire, construction); Chapter V (Articles 61-75); Chapter VI beyond the vintage; the annexes that belong only to those (II, III, IV, V, VII, VIII, IX, X); Decree 220 Articles 1-8.

### 1.2 What Decree 220/2026 does to the motor provisions

Read from its text: the body in full (220 src lines 1-211), and the two annexes it substitutes (220 src lines 212-1550: Annex III, the construction premium and deductible rates, and Form 3 of Annex X, a construction reporting form), scanned for any mention of the motor insurance, of which there is none beyond the decree's title and its Article 9:

- **Articles 1-7** amend Articles 32, 33, 34(2)(m)-(n), 37, 38, 45 and 58: all Chapter IV, construction insurance (220 src lines 31-163).
- **Article 8** replaces Annex III and Form 3 of Annex X (construction; reporting) (220 src lines 166-171). Annex I and Annex VI are untouched.
- **Article 9(1)** replaces "người thứ ba" with "bên thứ ba" in, among others, **Article 3(5), Article 5, Article 7(1)(a), Article 10(2)(đ), Article 12(2) and (6)(a), and Article 13(5)** (220 src lines 172-178). Checked against Decree 67: every occurrence of "người thứ ba" in Articles 3 to 13 is at one of those places (src lines 84-86, 185, 200-201, 274, 314, 366-367, 438-439), so the substitution is complete for the motor chapter, and Annex VI has no occurrence.
- **Article 9(2)** replaces "hoạt động đầu tư xây dựng" with "hoạt động xây dựng" in Articles 1(1), 1(3), 2(3), 2(5), 3(5)(b), 4(5)(c), 4(6)(b) and others: the construction limbs, not the motor ones (220 src lines 179-183).
- **Article 9(3)-(4)** change wording in the construction provisions (the consultants' insurance; a reference to Decree 06/2021) (220 src lines 184-193).
- **Article 10(1)**: in force from 1 July 2026; **10(2)**: a contract concluded before that and still running continues as agreed, unless the parties amend it to apply Decree 220; **10(3)**: government-guaranteed projects (220 src lines 194-205).

So the search results' suggestion stands on the text: the only change Decree 220 makes to the motor chapter is the word for the third party, in exactly the places listed.
The definition's words are otherwise unchanged, so both vintages name the same persons (fork F2), and **no answer in this encoding differs between the vintages**: every scenario of `nd67-tests.l4` that turns on the vintage was run under both and gives the same answer (§5.5).

### 1.2a Two further amending decrees (read 2026-10-07, at the lead's request)

Their numbers are written "ND-CP" here because their Vietnamese text is not among this row's checked sources.

The lead passed on, unverified, that Decree 67/2023 is also amended by Decree 105/2025/ND-CP and, through it, by Decree 347/2026/ND-CP.
Both were fetched from the government's servers on 2026-10-07 into scratch only (not deposited; untrusted data, deleted after reading), converted with `pdftotext -layout`, and read where they touch Decree 67:

- **Decree 105/2025/ND-CP** of 15 May 2025 (fire prevention and rescue), gazette issue 717+718 of 31 May 2025, `https://congbaocdn.chinhphu.vn/CongBaoCP/VanBan/2025/5/44912/56374-1-2025717-718105-2025-nd-cp.pdf`, sha256 `9f80546df6c9e4c8162e0d321f4f2297808cb69e39262b7e7e51bde752f38e11`, with its second issue 719+720 (`…/56377-1-2025719-720105-2025-nd-cp.pdf`, sha256 `64c8d534a90e8123a25700524f60090c28540b92b0bc41d9e076892af502097f`), which does not mention Decree 67. Its **Article 44(1)** amends Decree 67 at points (a)-(h): Article 4(5)(b) (the insurer's right to refuse, fire limb), 23(1)(a), 24(1), 26(1)-(2), 28(3), 29(3), repeals 30(1) and 31(2), and replaces **Annex II** (the fire premium annex). Every one is a fire-insurance provision. In force 1 July 2025 (its Article 45(1)). The other mentions of Decree 67 in it (its Article 35(3) and its own Annex VI) concern the fire levy and fire premiums.
- **Decree 347/2026/ND-CP** of 8 September 2026, `https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/9/347_2026_nd-cp_08092026_7-signed.signed.pdf`, sha256 `9559542193426a0f7ab7f3bacb133cd37c810c418ad68616d6f349820bc3f550` (20 pages). Its only reference to Decree 67 is **Article 28**, which rewrites the title and points (a)-(c) of Article 44(1) of Decree 105: again Decree 67's Article 4(5)(b), 23(1)(a) and 24(1), all fire. Its Article 30(2) repeals clause 3 of Decree 105's Article 44, which amends Decree 175/2024 (construction management), not Decree 67. In force 15 September 2026 (its Article 41(1)).

**Neither reaches Articles 5 to 13, Article 1-3 or the motor limbs of Article 4, Annex I or Annex VI.**
So the motor chapter has the two vintages this encoding already holds: the text as made (unchanged in its motor provisions by Decree 105 from 1 July 2025 and by Decree 347 from 15 September 2026) and the text as amended by Decree 220 from 1 July 2026. "As made" in the identifiers means the motor provisions as made.
Also reported by the lead's catalogue and **not verified here**: Law 08/2022/QH15 is amended by Law 139/2025/QH15 from 1 January 2026, and Resolution 32/NQ-CP keeps Decree 67/2023 in force from that day. The LAW forks of §3 cite the Law's 2022 text (the only text in this row's aids); the 2025 amendment may change what they say.

### 1.3 Which date decides the vintage

Decree 67 Article 77(1) puts it in force from signature, 6 September 2023 (src line 2009, with the date at src line 16).
Article 76(1) keeps a contract concluded before then and still running under the earlier rules, unless the parties amend it (src lines 1978-1997).
Decree 220 Article 10(2) does the same for a contract concluded before 1 July 2026 (220 src lines 196-200).
Both speak of the date the contract was **concluded** ("đã giao kết trước ngày"); neither mentions the accident or the claim.
So the encoding selects the vintage from the contract's conclusion date and any agreed amendment, as an explicit derived input (`the rules that govern`, `the vintage that governs`), not from the rule-effective-time axis: the date that decides is a fact of the contract, not the date of evaluation (fork F1).

## 2. Coverage table

Every provision in scope, with its heading as the decree writes it.
Dispositions: `encoded`, `inert` (quoted, decides no case), `out-of-scope`, `reached-and-refused`.
Totals: **78 rows: 61 encoded (one of them in part), 9 inert, 5 out-of-scope, 3 reached-and-refused, 0 deferred**.

| provision | heading as written | English gloss | src | disposition | where in the L4 |
| --- | --- | --- | --- | --- | --- |
| Chương I | QUY ĐỊNH CHUNG | general provisions | 39-40 | inert: a chapter heading | `nd67-ch1-general.l4` |
| Điều 1 | Phạm vi điều chỉnh | scope of regulation | 42-55 | inert: it lists what the decree covers and decides no case; clause 2's fund is Section 2, out of scope | comment |
| Điều 2(1) | Đối tượng áp dụng | subjects of application: owners in traffic in Vietnam | 56-60 | encoded | `Article 2(1) — the decree applies, for the motor insurance, to the person` |
| Điều 2(2)-(3) | (same) | fire and construction insurance | 61-64 | out-of-scope: they apply the decree to fire and construction insurance, which Chapters III and IV govern and this row does not encode | — |
| Điều 2(4)-(5) | (same) | insurers; other persons concerned | 65-71 | inert: (4) names the insurers and gives the short name "doanh nghiệp bảo hiểm"; (5) reaches everyone else concerned; neither decides a case | comment |
| Điều 3 chapeau | Giải thích từ ngữ | definitions | 72-73 | inert | comment |
| Điều 3(1) | Chủ xe cơ giới | vehicle owner | 76-77 | encoded | `Article 3(1) — a vehicle owner` |
| Điều 3(2) | Xe cơ giới hoạt động | operating vehicle | 78-79 | encoded | `Article 3(2) — the vehicle was operating` |
| Điều 3(3) | Xe cơ giới tham gia giao thông | vehicle in traffic | 80-81 | encoded | `Article 3(3) — the vehicle was participating in traffic` |
| Điều 3(5)(a) | Người thứ ba | third party (motor) | 84-89; 220: 172-178 | encoded, per vintage | `Article 3(5)(a) — a third party`, `the term for the third party in` |
| Điều 3(4), (5)(b), (6)-(10) | Nhà thầu tư vấn; Mức khấu trừ bảo hiểm; Đưa vào sử dụng; ... | consultant; deductible; putting into use; occupational terms | 82-83, 90-101 | out-of-scope: (4), (5)(b), (7)-(10) define construction and labour terms; (6), the deductible, is never used by Articles 5-13 or Annexes I and VI (the compulsory motor insurance has no deductible) | GLOSSARY.md |
| Điều 4(1) | Nguyên tắc chung | general principles: who must buy | 103-106 | encoded | `Article 4(1) — the person must buy the compulsory motor insurance` |
| Điều 4(2) | (same) | conditions, premium, sums as the decree sets | 109-111 | encoded through Article 8 and Annexes I and VI | `nd67-art8-premium.l4` |
| Điều 4(3) | (same) | wider cover allowed; compulsory part separated | 112-121 | encoded | `Article 4(3) — the insurer has separated the compulsory part as required` |
| Điều 4(4) | (same) | one contract per vehicle | 122-124 | encoded with Article 12(9) | `Article 12(9) — what becomes of` |
| Điều 4(5)(a) | (same) | insurer may refuse a vehicle past its service life | 125-128 | encoded | `Article 4(5)(a) — the insurer may refuse to sell the insurance for` |
| Điều 4(5)(b)-(c), 4(6)(b), 4(9) | (same) | fire; construction; reinsurers' ratings | 129-139, 149-150, 163-169 | out-of-scope: fire, construction and reinsurance rules, not the motor insurance | — |
| Điều 4(6)(a) | Chi phí mua bảo hiểm bắt buộc | the cost of the insurance in the accounts | 142-148 | inert: an accounting permission that decides no question of cover, premium or claim | comment |
| Điều 4(7) | (same) | premium payment deadline | 151-159 | encoded (the bound: not past the term) | `Article 4(7) — the premium payment deadline is within the term` |
| Điều 4(7), first sentence | (same) | deadline set by the Minister of Finance | 151-152 | reached-and-refused: the Minister's rule is not in the sources | `the premium payment deadline the Minister of Finance sets is not encoded in this model` |
| Điều 4(8) | (same) | nothing for amounts fraud added | 160-162 | encoded | `Article 4(8) — the compensation without what fraud added` |
| Điều 4(10) | (same) | other matters by the insurance business law | 170-172 | inert: a pointer to the Law; LAW forks L1-L9 record where it fills a gap | §3 |
| Chương II, Mục 1 | QUY ĐỊNH VỀ BẢO HIỂM BẮT BUỘC TRÁCH NHIỆM DÂN SỰ CỦA CHỦ XE CƠ GIỚI; ĐIỀU KIỆN BẢO HIỂM, MỨC PHÍ BẢO HIỂM, GIỚI HẠN TRÁCH NHIỆM BẢO HIỂM | the motor insurance: conditions, premium, limits | 175-181 | inert: a chapter and section heading | `nd67-art5-7-cover.l4` onward |
| Điều 5 | Đối tượng bảo hiểm | the object of the insurance | 183-186 | encoded | `Article 5 — the owner's insured liability is owed to` |
| Điều 6(1) | Giới hạn trách nhiệm bảo hiểm | limit, health and life | 187-189 | encoded | `Article 6(1) — the limit for health and life, per person per accident` |
| Điều 6(2)(a) | (same) | limit, property, motorcycles and mopeds | 190-193 | encoded | `Article 6(2)(a) — ...`, `Article 6(2) — the limit for property, per accident, for a vehicle of class` |
| Điều 6(2)(b) | (same) | limit, property, cars, tractors, trailers | 194-196 | encoded | `Article 6(2)(b) — ...` |
| Điều 7(1)(a) | Phạm vi bảo hiểm | third parties' health, life, property | 198-201 | encoded | `Article 7(1) — the harm ...`, `... property is within the scope` |
| Điều 7(1)(b) | (same) | passengers' health and life | 202-203 | encoded | same |
| Điều 7(2)(a) | Các trường hợp loại trừ trách nhiệm bảo hiểm | intentional act | 209-210 | encoded | `Article 7(2)(a) — ...`; `Article 7 — the answer on cover ...` |
| Điều 7(2)(b) | (same) | hit and run | 211-214 | encoded | `Article 7(2)(b) — ...` |
| Điều 7(2)(c) | (same) | driver's age, licence | 215-222 | encoded (reading ii of F5; the literal reading kept for R3) | `Article 7(2)(c) — ...` |
| Điều 7(2)(d) | (same) | indirect consequences | 223-224 | encoded | `Article 7 — the answer on cover for an item of property of` |
| Điều 7(2)(đ) | (same) | alcohol, drugs (property) | 225-227 | encoded | `Article 7(2)(dd) — alcohol or drugs` |
| Điều 7(2)(e) | (same) | property stolen or robbed | 228 | encoded | `Article 7 — the answer on cover for an item of property of` |
| Điều 7(2)(g) | (same) | special property | 229-230 | encoded | same |
| Điều 7(2)(h) | (same) | war, terrorism, earthquake | 231 | encoded | both answers on cover |
| Điều 8(1) | Mức phí bảo hiểm | premium by class, Annex I | 232-234 | encoded | `Annex I section A — the premium for a 1-year term, VAT not included, for` |
| Điều 8(2) | (same) | insurer's adjustment, at most 15% | 235-238 | encoded | `Article 8(2) — the premium after an adjustment of` |
| Phụ lục I, A.I-A.VI | MỨC PHÍ BẢO HIỂM BẮT BUỘC TRÁCH NHIỆM DÂN SỰ CỦA CHỦ XE CƠ GIỚI | the premium for a 1-year term, by class | 2041-2099 | encoded, one constant per row | `Annex I A.I.1 — ...` to `Annex I A.VI.4 — ...` |
| Phụ lục I, A.VII.1-6 | Phí bảo hiểm trong một số trường hợp khác | special cases: driving school, taxi, special-purpose, tractor unit, tractor, bus | 2100-2127 | encoded | `Annex I section A — ...` |
| Phụ lục I, B | Phí bảo hiểm cho thời hạn bảo hiểm khác 1 năm | a term other than 1 year | 2128-2139 | encoded | `Annex I section B — the premium for a term of`, `Annex I — the premium for the term of` |
| Điều 9(1) | Thời hạn bảo hiểm | 1 to 3 years; three cases under 1 year | 241-249 | encoded | `Article 9 — the term is permitted for` |
| Điều 9(2) | (same) | aligning a fleet's renewal date | 250-256 | encoded | `Article 9 — a term under 1 year is permitted for` |
| Điều 9(3) | (same) | former owner may terminate | 257-259 | encoded | `Article 9(3) — the former owner may terminate the contract` |
| Điều 9(3), the refund | (same) | the refund on that termination | 257-259, 285-291 | reached-and-refused: Article 11 provides none (finding R9) | `Article 11 states no refund for a termination on a change of owner, ...` |
| Điều 10(1) | Giấy chứng nhận bảo hiểm | one certificate per vehicle; a lost one | 260-265 | encoded | `Article 10(1) — one certificate for the vehicle`; `Article 10(1) — an owner who loses the certificate must ask in writing for a new one` |
| Điều 10(2) | (same) | particulars (a)-(i) | 266-280 | encoded | `Article 10(2) — the certificate carries every particular it must` |
| Điều 10(3) | (same) | electronic certificate | 281-284 | encoded | `Article 10(3) — the electronic certificate is valid` |
| Điều 11 | Chấm dứt thực hiện hợp đồng bảo hiểm và hậu quả pháp lý của việc chấm dứt thực hiện hợp đồng bảo hiểm | termination on revocation of registration; refund | 285-291 | encoded | `Article 11 — the refund on the revocation of the registration on` |
| Điều 12 chapeau | Nguyên tắc bồi thường bảo hiểm | claims principles, under the insurance business law | 292-294 | inert: a pointer to the Law and a heading for the clauses below | comment; LAW forks |
| Điều 12(1)(a)-(d) | (same) | the buyer's duties when an accident happens | 295-309 | encoded (regulative; no period) | `Article 12(1) — the duties of the buyer and the insured when an accident happens` |
| Điều 12(2) | (same) | 1 hour; 24 hours | 310-316 | encoded (regulative, hours) | `nd67-art12-duties-hours.l4` |
| Điều 12(3)(a)-(b) | (same) | the advance: 70%, 50%; 30%, 10% | 317-330 | encoded | `Article 12(3) — the advance for` |
| Điều 12(3), 3 working days | (same) | the advance's deadline | 317-319 | encoded (regulative and dates) | `Article 12(3) — the insurer must pay the advance`; `... the last day for the advance ...` |
| Điều 12(3), last paragraph | (same) | repayment by the Fund | 331-334 | encoded (the right to ask; R10) | `Article 12(3) — the insurer may ask the Fund to repay the advance` |
| Điều 12(4) | (same) | written notice within 5 working days | 335-338 | encoded (regulative and dates) | `Article 12(4) and (7) — the written notice of the accident`; `... the last day for the written notice ...` |
| Điều 12(5) | (same) | who is paid | 341-349 | encoded | `Article 12(5) — the insurer pays` |
| Điều 12(6)(a), first paragraph | Mức bồi thường bảo hiểm | Annex VI, agreement, court | 350-361 | encoded | `Article 12(6)(a) — the compensation for the health and life of` |
| Điều 12(6)(a), second paragraph | (same) | several vehicles, by fault | 362-364 | encoded (fork F17) | same |
| Điều 12(6)(a), third paragraph | (same) | entirely a third party's fault: 50% | 365-373 | encoded (finding R4) | same |
| Điều 12(6)(b) | (same) | property: actual damage by fault, within the limit | 376-378 | encoded | `Article 12(6)(b) — the compensation for property in the accident` |
| Điều 12(7) | (same) | reduction up to 5% | 379-385 | encoded (amount; regulative permission in 12(4)) | `Article 12(7) — the compensation for property after a reduction of` |
| Điều 12(8) | (same) | nothing above the limit | 386-388 | encoded | `Article 12(8) — the compensation within the limit` |
| Điều 12(9) | (same) | the first contract pays; refunds | 389-392 | encoded | `Article 12(9) — what becomes of` |
| Điều 12(9), same-day contracts | (same) | which of two same-day contracts is first | 389-391 | reached-and-refused: a date cannot order them (fork F19) | `two contracts were concluded on the same first day, ...` |
| Điều 12(10)-(11) | (same) | telling the injured person; notifying and paying | 393-400 | encoded (regulative; no period) | `Article 12(10) — ...`, `Article 12(11) — ...` |
| Điều 13(1)-(7) and last paragraph | Hồ sơ bồi thường bảo hiểm | the claim file and who gathers what | 401-450 | encoded | `Article 13 — the documents the buyer or insured has still to gather`; `... the insurer has still to gather` |
| Phụ lục VI, Part A and B formula | BẢNG QUY ĐỊNH TRẢ TIỀN BỒI THƯỜNG THIỆT HẠI VỀ SỨC KHỎE, TÍNH MẠNG | 100% cases; rate × limit | 1019-1020: 591-602 | encoded | `Annex VI — the payment for an injury rate of`; `the Annex VI amount for` |
| Phụ lục VI, Part B sections I-X | Tỷ lệ tổn thương cơ thể do tổn thương ... | 1,133 rows by body system | 1019-1020: 603-2176 | encoded, one L4 row per source row (generated) | `nd67-annex6-table.l4`; `the payment band in Annex VI for` |
| Phụ lục VI, acuity table | TỶ LỆ TỔN THƯƠNG CƠ THỂ DO GIẢM THỊ LỰC VÌ TỔN THƯƠNG CƠ QUAN THỊ GIÁC | 10 × 10 visual acuity table | 1019-1020: 1990-2010 | encoded (generated) | `the acuity table rate for` |
| Phụ lục VI, notes | Ghi chú | 17 notes and instructions | 1019-1020: 622, 670, 763, 869, 930, 1129, 1425, 1641, 1774, 1816, 1832, 1845, 1860, 1985, 2041, 2123, 2169 | encoded in part: 2 encoded (limb; sex); 15 inert: they direct "cộng lùi" combinations the sources do not define, or describe how to apply other rows (R7) | `the point a note of Annex VI fixes for`; quoted as NOTE |
| Phụ lục VI, special cases 1-6 | Những trường hợp đặc biệt | stiffness; loss of function; one eye; several injuries; unlisted; unidentified dead | 1019-1020: 2177-2195 | encoded: 1, 3, 4, 5, 6; case 2 is an input convention (the caller names the loss row) | `Annex VI — the rate in percent for the injury`; `the Annex VI amount for` |
| Mục 2, Điều 14-22 | CƠ CHẾ QUẢN LÝ, SỬ DỤNG QUỸ BẢO HIỂM XE CƠ GIỚI | the Motor Vehicle Insurance Fund | 453-723 | out-of-scope: the brief excludes it; it governs the Fund and its contributors, not the contract; Article 17(1)(a) is quoted for finding R10 | `nd67-art12-13-claims.l4` comment |
| Chương III-IV, V, VI; Phụ lục II-V, VII-X | (fire; construction; organisation of implementation; final provisions; their annexes) | other insurances and other addressees | 725-2040; 2142-3199; 1019-1020: 1-590, 2198-2810 | out-of-scope: fire and construction insurance and the duties of ministries and bodies are other rows' or nobody's; Articles 76(1) and 77(1) are encoded for the vintage, 75(1) and 75(10) quoted for R12 and the comparables | — |
| Decree 220, Điều 1-8, 9(2)-(4), 10(3) | (amendments to Chapter IV, Annex III, Form 3 of Annex X, wording) | construction amendments | 220: 31-193, 203-205 | inert for this row: they reach only construction provisions and annexes (§1.2) | — |
| Decree 220, Điều 9(1), 10(1)-(2) | Thay thế một số cụm từ; Điều khoản thi hành | "bên thứ ba"; commencement; existing contracts | 220: 172-178, 194-200 | encoded | `the term for the third party in`; `the rules that govern` |
| Decree 67, Điều 76(1), 77(1) | Điều khoản chuyển tiếp; Hiệu lực thi hành | transitional; commencement | 1978-1997, 2008-2009 | encoded | `the rules that govern` |

## 3. Fork register

A fork is an ambiguity this encoding resolved; the readings it saw, the one it took, and why.
Places looked at where no fork was found are named at the end.

| # | where | the question | readings | taken, and why |
| --- | --- | --- | --- | --- |
| F1 | Art 76(1); 220 Art 10(2) | Which date decides the vintage? | (i) the date the contract was concluded; (ii) the accident date; (iii) the claim date | **(i)**: both clauses speak of contracts "đã giao kết trước ngày" the decree took effect; neither names the accident or the claim. An agreed amendment moves a contract to the later text. |
| F2 | Art 3(5)(a); 220 Art 9(1) | Does "bên thứ ba" name the same persons as "người thứ ba"? | (i) yes, a rename; (ii) "bên" (party) widens it to organisations | **(i)**: Decree 220 changes the word only; the definition's body (the injured person and the exceptions) is untouched. Both vintages are encoded from their own text and agree. |
| F3 | preamble (src 29); Art 6(2); Annex I | The vehicle kinds and the driver's conditions are "theo quy định của Luật Giao thông đường bộ", the Law of 13 November 2008 by the preamble. Is that Law still in force, and does Annex I's row "Dưới 50 cc" under "Mô tô 2 bánh" overlap its "Xe gắn máy"? | — | **unverified**: nothing in the sources says whether the 2008 Law is still in force; Art 77(3) (src 2026-2028) says a replaced law is read as its replacement. Outside knowledge, unverified: the 2008 Law was replaced from 1 January 2025 by the Law on Road Traffic Order and Safety and the Law on Roads. So the class of a vehicle and whether it needs a licence are **inputs**; the mapping of Annex I classes to Art 6(2)(a)/(b) is the encoder's (I-III → (a); IV-VII → (b)). |
| F4 | Art 3(2) | Does "có sự điều khiển" (under control) govern moving and stopping as well as parking? | (i) all three; (ii) parking only | **(i)**: it closes the list "đang vận hành gồm di chuyển, dừng xe, đỗ xe". On (ii) a vehicle moving with nobody at the controls would be "operating"; it is anyway "in traffic" only if driven. Finding R2 follows. |
| F5 | Art 7(2)(c) | Does "đối với xe cơ giới bắt buộc phải có Giấy phép lái xe" qualify every licence limb or only the last? | (i) the last only (last antecedent); (ii) every licence limb | **(ii)**: on (i) the cover of every vehicle that needs no licence is illusory for any driver without one, which the clause cannot mean; but (i) is the grammatical reading. The age limb bites always. Both readings are encoded; finding R3. |
| F6 | Art 7(2)(a) | Whose damage does the injured person's intentional act exclude? | (i) that person's own; (ii) the whole accident's | **(i)**: the owner's or driver's intent excludes the accident; the victim's own intent cannot reasonably defeat another victim's claim. |
| F7 | Art 7(2)(đ) | Is the drug limb, after the semicolon, also confined to damage to property? | (i) yes; (ii) drugs exclude all damage | **(i)**: the limb continues "do lái xe điều khiển xe cơ giới mà ..."; bodily injury stays covered under both alcohol and drugs. |
| F8 | Art 9(1) | Are 1 year and 3 years inclusive, and what is a year? | — | **inclusive**; a year ends on the same day and month a year on (`add years`), whatever the days in it. |
| F9 | Annex I B | How are the days of a term counted? | — | the day count from the first day to the last, the first excluded (`Day end - Day begin`): a term from 1 January 2026 to 1 January 2027 is 365 days. |
| F10 | Annex I B; Art 11 | Are premiums and refunds rounded? | — | **no rounding**: the decree states none; amounts are kept exact. |
| F11 | Art 8(2) | Does the 15% adjust the annual figure or the premium of the contract's own term? | — | the Annex I premium of the contract's term (after section B); the clause says "tính trên mức phí bảo hiểm quy định tại Phụ lục I". |
| F12 | Art 11 | How is "tương ứng với thời hạn còn lại" measured? | — | pro rata by days, from the day of revocation (counted as used) to the end of the term. |
| F13 | special case 3 | Which row is "mất hoàn toàn hai mắt"? | (i) B.VIII 1.4, total blindness of both eyes, 87%; (ii) enucleation of both eyes, 91% or 95% | **(i)**, which is also the acuity table's cell for no light perception in both eyes (87); enucleation, where it happened, has its own rows. |
| F14 | Art 12(3)-(4) | Which days are "ngày làm việc"? | — | Monday to Friday, less the days off the caller supplies (public holidays). The decree does not say; whether Saturday is a working day for an insurer is not settled by any text here. |
| F15 | Art 12(3)(b) | "tử vong và ước tính tỷ lệ tổn thương từ 81% trở lên": both at once, or two cases? | (i) two cases; (ii) both | **(i)**: a death has no injury rate to estimate; Art 17(1)(a) uses the same words for the same two cases. |
| F16 | Art 12(3)(a); Annex VI A.2, B.I 4.1 | Is a persistent vegetative state a "tổn thương bộ phận" (partial injury)? | (i) yes; (ii) no, it is Part A, apart from Part B's partial injuries | **(i)**: the same injury is also Part B section I item 4.1 (100), so it is a partial injury; on (ii) point (a) would give no advance for it while (b) gives 30%. |
| F17 | Art 12(6)(a) second paragraph; (b) | How does "theo mức độ lỗi của chủ xe cơ giới" fix the amount? | — | the owner's share of the fault, a fraction, multiplies the amount (for health and life only where several vehicles caused the accident). |
| F18 | Art 12(6)(a) third paragraph | Is a court's figure held to the 50% ceiling? | — | **yes**: the paragraph caps an agreement at 50% and is silent on courts; the first paragraph caps a court's figure at the Annex VI amount, here read as the halved amount. |
| F19 | Art 12(9) | Which of two contracts concluded on the same day is "giao kết đầu tiên"? | — | **declined** by name: a date cannot order them. |
| F20 | Art 13(3) | "có thể bao gồm một hoặc một số": which documents must an injury or a death file have? | — | an injury: at least one of (3)(a) and (3)(b); a death: (3)(c). |
| F21 | Art 13(2)(b), (6) | Is a licence needed where the vehicle needs none? Is the assessment record always needed? | — | the licence only where one is required; the insurer's record always. |
| F22 | Art 12(3)-(4) | Is the day of the anchor counted? | — | **no**: day 1 is the next working day. Outside knowledge, unverified: the Civil Code counts a period in days from the day after the event. |
| F23 | Art 12(3) | Which notice starts the 3 working days? | (i) the first notice (the hotline call of 12(1)(a)); (ii) the written notice of 12(4) | **(i)**: "kể từ ngày nhận được thông báo ... về vụ tai nạn" names no form, and (ii) could delay the advance by up to 5 working days. |
| F24 | Art 12(4) | Does force majeure suspend the 5 days or lift them? | — | **lifts** them for that notice ("trừ trường hợp"); LAW L4 agrees on its effect. |
| F25 | Art 3(5)(a), 7(1)(b) | Who is a "hành khách" (passenger)? | (i) anyone carried; (ii) a person carried under a contract of carriage | **an input**: undefined in the sources; the encoding takes the classification as a fact and shows both outcomes (finding R1). |
| F26 | Art 12(2) | From when do the 24 hours run? | — | from receipt of the notice, like the 1 hour: the sentence opens "Khi nhận được thông báo về tai nạn". |
| F27 | Art 12(5) with (6) | Is the insurer's payment the insured's civil liability (12(5)) or the table's amount (12(6))? | — | the amount of 12(6), which 12(6)(a) itself caps; 12(5) is encoded as who is paid. |
| F28 | Art 12(6)(a); Annex VI | What is "mức bồi thường quy định tại Phụ lục VI" where the row gives a band? | (i) the assessed point; (ii) the top of the band; (iii) the bottom | **(i)**: the assessed rate is an input; without it the encoding declines (finding R6). |
| F29 | Art 6(2) | Is the property limit per accident across all the injured? | — | **yes**: "trong một vụ tai nạn"; every person's covered property counts towards it. |
| F30 | Art 3(5)(a) | Can a company be a "người thứ ba"? | — | yes: the encoding does not distinguish natural and legal persons; a person record may be either. |
| F31 | Art 9(1)(b) | "niên hạn sử dụng nhỏ hơn 1 năm": the whole service life, or what remains of it? | — | what remains: no road vehicle has a service life under 1 year. |
| F32 | 220 Art 10(2) | "tiếp tục thực hiện theo các quy định đã thỏa thuận tại hợp đồng": which rules? | — | for a compulsory contract, the decree as made, whose terms Art 4(2) obliges the parties to use. |
| F33 | Annex VI rows with "cộng lùi" | Encode the addition? | — | **no**: "cộng lùi" is not defined in the sources; such a row is answered without the addition, and with it the encoding declines (R7). |
| F34 | Art 7(1)(a) | "Thiệt hại ngoài hợp đồng": which third-party damage is contractual? | — | none is distinguished: every third party's damage is taken as non-contractual. A third party's goods carried under a contract with the owner are a case this does not model. |
| F35 | Art 12(6)(a) third paragraph | Does the 50% reach passengers? | — | **no**: "đối với các đối tượng thuộc người thứ ba". |
| F36 | Art 12(1)(b) | How is the exception for safety, harm and authority demands applied? | — | as a fact about the act: where it holds, the prohibition does not bind. |

**LAW forks** (Law on Insurance Business 08/2022/QH15, `.aids/law-08-2022-qh15.txt`, an aid; not encoded; quoted here in English):

| # | the Law | aid lines | what it does here |
| --- | --- | --- | --- |
| L1 | Art 31(1): pay within the agreed period, or within 15 days of a complete, valid claim file | 719-724 | fills the decree's silence on the deadline for paying the compensation (12(11)); not encoded |
| L2 | Art 30(1): file a claim within 1 year of the insured event | 707-710 | fills the decree's silence on a time-bar; not encoded |
| L3 | Art 46(1): reduce for late notice only by the damage the insurer itself suffered, and not after force majeure | 917-927 | possible conflict with Art 12(7)'s flat "up to 5%"; **not resolved**: the decree's figure is encoded as written |
| L4 | Art 19(3): force majeure or an objective obstacle that delayed the notice bars an exclusion for late notice | 441-444 | agrees with F24 |
| L5 | Art 8(4): an insurer may not refuse to sell compulsory insurance to a person who meets the conditions | 240-243 | consistent with Art 4(5)(a) (a vehicle past its service life does not meet them) |
| L6 | Art 24: an unclear clause of an insurance contract is read for the buyer | 588-591 | whether it reaches the decree's own text is not settled here; several forks (F5, F16, F25) were resolved in the direction it points, but on their own reasons |
| L7 | Art 58(2): a third party has no direct claim against the insurer unless law provides | 1087-1089 | Art 12(5) is such a provision (direct payment where the insured has died or lost capacity) |
| L8 | Art 59(3)-(4): the insurer also pays dispute costs and interest, within the limit | 1098-1107 | the decree is silent; not encoded |
| L9 | Arts 26-27: unilateral termination and its consequences | 623-678 | the decree's Art 11 covers only revocation of the registration; termination on other grounds follows the Law; not encoded |

Places looked at with no fork found: Article 6 (figures and units plain); Article 10(2) points (a)-(i); Article 12(8); Article 13(1), (2)(a), (2)(c), (2)(d), (4), (6), (7); Annex I sections IV and VI (the bands meet with no gap and no overlap); every row of Annex VI's acuity table (symmetric, checked by the generated tests).

## 4. Findings

A finding is a defect or a surprise in the decree as written, not an ambiguity resolved.
Each gives the source lines, a minimal scenario, and the evidence (an assertion in `nd67-findings.l4` or `nd67-tests.l4`), or the words "reading only".

**R1. A person on the vehicle who is not a passenger is covered by neither limb of Article 7(1).**
Article 3(5)(a) excludes from the third parties "Người lái xe, người trên xe, hành khách trên chính chiếc xe đó" (src 86-87); Article 7(1)(b) covers only "hành khách trên chiếc xe đó" (src 202).
Scenario: a family member riding pillion on a private motorbike, if not a "hành khách" (undefined, F25), is killed: no compensation.
Evidence: `nd67-findings.l4`, R1, `outside the scope: the person is neither a third party nor a passenger`, in both vintages.

**R2. Damage done by a vehicle parked with nobody at its controls is outside the cover.**
Article 3(2) (src 78-79) needs "sự điều khiển"; Article 3(3) (src 80-81) needs driving in road traffic.
Scenario: a parked car whose handbrake fails rolls into a pedestrian.
Evidence: `nd67-findings.l4`, R2; and `nd67-tests.l4` (the same car with its driver at the wheel is covered).

**R3. On its grammatical reading, Article 7(2)(c) makes the cover illusory for every unlicensed driver of a vehicle that needs no licence.**
Src 215-222; fork F5.
Scenario: an electric moped needing no licence, ridden by its owner who holds none, injures a pedestrian: excluded on the literal reading.
Evidence: `nd67-findings.l4`, R3: the encoded reading does not exclude; the last-antecedent reading does.

**R4. "Lỗi hoàn toàn của người thứ ba" halves the compensation of an innocent third party.**
Article 12(6)(a), third paragraph (src 365-373), keys the 50% on the accident being entirely "a third party's" fault, and applies it to "các đối tượng thuộc người thứ ba", whoever was at fault.
Scenario: a cyclist swerves and causes the accident; a pedestrian is killed: 75,000,000 instead of 150,000,000; the car's passenger killed in the same accident receives 150,000,000.
Evidence: `nd67-findings.l4`, R4.

**R5. Annex I charges a 16-seat business vehicle more than a 17-seat one.**
Src 2081-2082: 16 seats 3.054.000; 17 seats 2.718.000; every other step of section V rises. The gazette PDF page (gazette page 65) prints the same figures (§5.4).
Evidence: `nd67-findings.l4`, R5.

**R6. A band of Annex VI is a range of money, and nothing says who picks the point or how.**
821 of the 1,135 rows give a rate: 650 a band and 171 a single figure; 589 of the bands are 4 points wide, which on the 150,000,000 limit is 6,000,000 between the least and the most.
Article 12(6)(a) (src 350-361) applies the table "theo từng loại thương tật" and names no assessor or criterion; only two notes of the table fix a point, for 10 items.
Scenario: B.I 1.1 pays anything from 9,000,000 to 15,000,000.
Evidence: `nd67-findings.l4`, R6; `nd67-tests.l4` declines a band with no assessed rate.

**R7. "Cộng lùi" carries weight and is never defined; special case 4 combines by a different rule.**
The phrase occurs on 28 lines of Annex VI (rows and notes), e.g. src 1019-1020 lines 2086-2088, 2103-2104, 1774-1776; neither the decree nor Decree 220 defines it.
Special case 4 (1019-1020 src 2185-2187) adds several injuries' payments plainly, capped at the limit, so two methods coexist with no rule for which governs.
Evidence: reading only; the encoding declines a row whose addition applies (`nd67-tests.l4`).

**R8. Annex VI has gaps and overlaps at its boundaries.**
Reading only, the rows encoded as printed:
V 11.1 "Trên 50 tuổi" / 11.2 "Dưới 50 tuổi" (1019-1020 src 1222-1223): a victim of exactly 50 is in neither;
VI 6.5.2 "chi ngắn dưới 4 cm" / 6.5.3 "chi ngắn trên 4 cm" (src 1525-1527), and 6.7.3 / 6.7.4 (src 1540-1541): exactly 4 cm is in neither;
VI 2.4.3 "chi ngắn dưới 3 cm" / 2.4.4 "chi ngắn trên 3 cm" (src 1321-1322): exactly 3 cm;
VI 7.4.1 "Khớp giả hai xương chặt, chi ngắn dưới 5 cm" / 7.4.2 "Khớp giả hai xương lỏng, chi ngắn trên 5 cm" (src 1582-1583): a loose joint under 5 cm, a tight one over 5 cm, and exactly 5 cm are in neither;
IX 2.2 "Mất từ 2 đến 8 răng" / 2.3 "Mất từ 8 đến 19 răng" (src 2040, 2043): 8 teeth are in both (checked on the PDF, gazette page 63);
VI 2.3.1 "trên 5° đến 145°" / 2.3.4 "trên 100° đến 150°" (src 1311, 1314): the elbow arcs overlap, at 11-15% and 51-55%;
VI 10.4.1 "Nam giới ..." / 10.4.3 "Người ở độ tuổi vị thành niên ..." (src 1729-1731): a boy is in both, at 31-35% and 41-45%;
VI 6.12.3 "Cứng ba khớp lớn (háng, gối)" names two joints and pays 66-70%, more than 6.12.4 "Cứng ba khớp háng, gối và cổ chân" at 61-65% (src 1561-1562).

**R9. Article 9(3) sends a former owner to Article 11, which says nothing about a change of owner.**
Src 257-259; Article 11 (src 285-291) provides only for revocation of the registration certificate and plates.
Scenario: the vehicle is sold mid-term; the seller terminates: the decree states no refund.
Evidence: `nd67-findings.l4`, R9 (a named refusal).

**R10. Article 12(3) lets the insurer ask the Fund to repay any advance; Article 17(1)(a) binds the Fund to repay only advances under point (b).**
Src 331-334 against src 503-507.
Scenario: an advance under point (a) (cover found at the time) for an accident later found excluded: a right to ask with no duty to pay.
Evidence: reading only (Article 17 is out of scope).

**R11. Annex I section B prices a short term on the premium "do Bộ Tài chính quy định" (set by the Ministry of Finance), though Annex I is set by this Government decree.**
Src 2130-2132.
Evidence: reading only; the encoding applies section B to the Annex I premium.

**R12. The insurer's discretion has a ceiling and no criterion.**
Article 8(2) (src 235-238): raise or lower by up to 15% on claims or accident history; Article 12(7) (src 379-385): reduce property compensation by up to 5%.
Neither says how much, and a 15% reduction sits uneasily with Article 75(1) (src 1909-1910): "Không khuyến mại, chiết khấu thanh toán dưới mọi hình thức" (no promotion or discount in any form).
Evidence: `nd67-findings.l4`, R12 (both ends lawful on the same facts).

**R13. The decree sets no deadline for paying the compensation itself, and no time-bar.**
Article 12(11) (src 397-400) requires notification and payment with no period; Article 13 sets no claims deadline.
Evidence: reading only; LAW forks L1 (15 days) and L2 (1 year) fill both.

**R14. Special case 1 can halve what the table's own stiffness rows pay.**
Special case 1 (1019-1020 src 2178-2180): "dính các khớp ngón tay (trừ ngón cái và ngón trỏ)" pays 50% of the loss of the finger. The table's own rows for stiffness ("Cứng ... khớp") of the same fingers pay more: the middle finger's interphalangeal joints, B.VI 4.5.3.3, 7-9% (src 1448), against 50% of B.VI 4.5.3.6's 8-10% (src 1451), 4-5%.
Whether "dính khớp" (ankylosis) and "cứng khớp" (stiffness) are the same condition is the open question.
Evidence: `nd67-findings.l4`, R14.

**R15. Section B's arithmetic.**
A 1-day contract costs a twelfth of the year, the same as a 30-day one (src 2138-2139); a two-year term that spans 29 February costs 731/365 of a year's premium, more than two years' (875,197.26 against 874,000 for 437,000).
Evidence: `nd67-findings.l4`, R15.

**R16. Annex VI rates vary with sex, age, marital status and occupation.**
The note after B.I 6.3.8 (1019-1020 src 763) gives women the top of the band and men the bottom; the note in section VII (src 1816-1818) adds 5-10% for "nam, nữ thanh niên chưa lập gia đình"; others add for singers, teachers, perfumers (src 2123-2124, 2169-2171).
Evidence: the sex note is encoded and tested (`nd67-tests.l4`); the rest reading only (R7).

## 5. Answer tables

### 5.1 The premium, Annex I (VND a year, VAT not included; both vintages)

Generated by `tools/annex1.py` from the raw text; each line is also a test in `nd67-annex1-tests.l4`.

| Annex I row | vehicle tested | premium, VND, VAT not included | src line |
| --- | --- | --- | --- |
| I.1 | under 50 cc (49 cc) | 55,000 | 2052 |
| I.2 | 50 cc or more (50 cc) | 60,000 | 2053 |
| II | three-wheeled motorcycle | 290,000 | 2054 |
| III.1 | electric moped | 55,000 | 2058 |
| III.2 | other mopeds | 290,000 | 2059 |
| IV.1 | non-business car, 5 seats | 437,000 | 2061 |
| IV.2 | non-business car, 6 seats | 794,000 | 2062 |
| IV.2 | non-business car, 11 seats | 794,000 | 2062 |
| IV.3 | non-business car, 12 seats | 1,270,000 | 2063 |
| IV.3 | non-business car, 24 seats | 1,270,000 | 2063 |
| IV.4 | non-business car, 25 seats | 1,825,000 | 2064 |
| IV.4 | non-business car, 45 seats | 1,825,000 | 2064 |
| IV.5 | pickup or minivan, non-business | 437,000 | 2065 |
| V.1 | business car, under 6 seats (5) | 756,000 | 2067 |
| V.2 | business car, 6 seats | 929,000 | 2068 |
| V.3 | business car, 7 seats | 1,080,000 | 2069 |
| V.4 | business car, 8 seats | 1,253,000 | 2070 |
| V.5 | business car, 9 seats | 1,404,000 | 2071 |
| V.6 | business car, 10 seats | 1,512,000 | 2072 |
| V.7 | business car, 11 seats | 1,656,000 | 2073 |
| V.8 | business car, 12 seats | 1,822,000 | 2077 |
| V.9 | business car, 13 seats | 2,049,000 | 2078 |
| V.10 | business car, 14 seats | 2,221,000 | 2079 |
| V.11 | business car, 15 seats | 2,394,000 | 2080 |
| V.12 | business car, 16 seats | 3,054,000 | 2081 |
| V.13 | business car, 17 seats | 2,718,000 | 2082 |
| V.14 | business car, 18 seats | 2,869,000 | 2083 |
| V.15 | business car, 19 seats | 3,041,000 | 2084 |
| V.16 | business car, 20 seats | 3,191,000 | 2085 |
| V.17 | business car, 21 seats | 3,364,000 | 2086 |
| V.18 | business car, 22 seats | 3,515,000 | 2087 |
| V.19 | business car, 23 seats | 3,688,000 | 2088 |
| V.20 | business car, 24 seats | 4,632,000 | 2089 |
| V.21 | business car, 25 seats | 4,813,000 | 2090 |
| V.22 | business car, 26 seats: 4,813,000 + 30,000 × (26 − 25) | 4,843,000 | 2092 |
| V.22 | business car, 45 seats: 4,813,000 + 30,000 × 20 | 5,413,000 | 2092 |
| V.23 | pickup or minivan, business | 933,000 | 2094 |
| VI.1 | truck, 2.9 t | 853,000 | 2096 |
| VI.2 | truck, 3 t | 1,660,000 | 2097 |
| VI.2 | truck, 8 t | 1,660,000 | 2097 |
| VI.3 | truck, 8.1 t | 2,746,000 | 2098 |
| VI.3 | truck, 15 t | 2,746,000 | 2098 |
| VI.4 | truck, 15.1 t | 3,200,000 | 2099 |
| VII.1 | driving-school car: 120% of IV.1 | 524,400 | 2102 |
| VII.1 | driving-school truck: 120% of VI.2 | 1,992,000 | 2102 |
| VII.2 | taxi, 5 seats: 170% of V.1 | 1,285,200 | 2105 |
| VII.2 | taxi, 7 seats: 170% of V.3 | 1,836,000 | 2105 |
| VII.3(a) | ambulance: 120% of V.23 | 1,119,600 | 2110 |
| VII.3(b) | cash-in-transit: 120% of IV.1 | 524,400 | 2112 |
| VII.3(c) | special-purpose, 10 t: 120% of VI.3 | 3,295,200 | 2115 |
| VII.3(c) | special-purpose, no designed payload: 120% of VI.1 | 1,023,600 | 2117 |
| VII.4 | tractor unit and trailer: 150% of VI.4 | 4,800,000 | 2119 |
| VII.5 | tractor and trailer: 120% of VI.1 | 1,023,600 | 2123 |
| VII.6 | bus, 16 seats: as IV.3 | 1,270,000 | 2126 |
| VII.6 | bus, 30 seats: as IV.4 | 1,825,000 | 2126 |

Article 8(2): any premium may be raised or lowered by at most 15%: for 437,000, from 371,450 to 502,550; 16% either way is rejected (`nd67-tests.l4`).
Section B: a term of 30 days or less pays the annual premium / 12 (437,000 → 36,416.67); a longer one pays annual / 365 × days (31 days → 37,115.07; 730 days → 874,000).

### 5.2 The limits of liability (Article 6; both vintages)

| vehicle (Annex I sections) | health and life, per person per accident | property, per accident | src |
| --- | --- | --- | --- |
| two- and three-wheeled motorcycles, mopeds, similar (I-III) | 150,000,000 | 50,000,000 | 188-193 |
| cars, goods vehicles, tractors, tractor units, towed trailers, buses, taxis, special-purpose (IV-VII) | 150,000,000 | 100,000,000 | 188-189, 194-196 |

### 5.3 The advance on compensation (Article 12(3); both vintages; src 317-330)

| the accident | the harm | the advance | on the 150,000,000 limit |
| --- | --- | --- | --- |
| found within the scope | death | 70% of the estimated compensation | 105,000,000 on an estimate of 150,000,000 |
| found within the scope | a partial injury (incl. a vegetative state, F16) | 50% of the estimated compensation | 15,000,000 on an estimate of 30,000,000 |
| not yet found | death, or an estimated rate of 81% or more | 30% of the limit | 45,000,000 |
| not yet found | an estimated rate from 31% to under 81% | 10% of the limit | 15,000,000 |
| not yet found | an estimated rate under 31% | none of the cases listed | — |

Deadline: 3 working days from the notice (a notice on Monday 5 October 2026: Thursday 8 October; the 9th is late).
The written notice of the accident: 5 working days (an accident on Monday 5 October 2026: Monday 12 October).
The insurer's guidance: 1 hour; the loss assessment organised: 24 hours.
Each is tested on both sides in `nd67-tests.l4`.

### 5.4 Annex VI: rows, tests, and the layout settled against the PDF

`tools/annex6.py` reads lines 591-2197 of `nd67-congbao-1019-1020.txt` and writes:

- **1,135 rows**: 2 in Part A and 1,133 in Part B (section I 176, II 53, III 47, IV 114, V 59, VI 442, VII 48, VIII 71, IX 32, X 91); 821 with a rate (650 bands, 171 single figures), 314 with no rate of their own (257 headings with rows under them, 57 rows whose text sends the assessor elsewhere);
- the **acuity table**: 10 rows × 10 cells;
- **17 notes**, quoted inert after the row they follow;
- **1,235 tests** in `nd67-annex6-tests.l4`: one per row (the payment band, or the absence of a rate) and one per cell of the acuity table. Their expected values are extracted from the raw text a second time, by a different routine from the one that writes the table; the two extractions agree on every row (0 disagreements), and the script checks that every item number is unique in its section and that every parent item comes before its children (0 problems).

Where `pdftotext -layout` was ambiguous, the PDF page itself was read with the Read tool (`pages`), on 2026-10-06, and the reading recorded in the script's `LAYOUT` table:

| raw line | the doubt | settled on the PDF (gazette page) |
| --- | --- | --- |
| 1746 | a line ending "từ 0" looks like a cell | text: "xoay từ 0 đến 20°" (page 54) |
| 2021 | one space before "31 - 35" | the cell is 31-35; "từ cành cao trở xuống" is the text (page 62) |
| 2047 | an uncoded line under heading IX 3 carries 51-55 | the row is IX 3, its text in an unnumbered cell (page 63) |
| 2132, 2133, 2148, 2150, 2151 | one space before the range | each is the cell (page 66) |
| 841, 1895 | the cell on the middle line of a multi-line row | the cell belongs to the row (pages 26, 59) |
| 1165 | a line starting "1.3.2 cộng lùi" looks like an item | a continuation of V 1.3.3 (page 36) |
| 2076 | "1.1.10.2" with no final dot | a row (page 64) |
| 1990-2010 | the acuity table's header is scrambled | columns 8/10-10/10, 6/10-7/10, 5/10, 4/10, 3/10, 2/10, 1/10, 1/20, below 1/20, ST(-), as printed (page 62) |

The Annex I figure at R5 (16 seats, 3.054.000) and the rows of section A were also checked on the PDF (gazette pages 64-66 of issue 1017+1018).

### 5.5 The two vintages compared

Run under both vintages (contracts concluded 30 June 2026 and 1 July 2026, or the vintage given directly): the third-party test (5 cases), the term for the third party (the only difference: "người thứ ba" / "bên thứ ba"), the premium, the compensation for health and life (including the third-party-fault halving), the compensation for property, and the cover answer for R1.
**No answer differs.**
A contract concluded on 5 September 2023 is declined (`a contract concluded before Decree 67/2023 is governed by earlier rules not encoded in this model`).

## 6. What `check.sh` prints

```
module                                    errors satisfied  failed  refused  expected
nd67-annex1-tests.l4                           0        55       0        0         0
nd67-annex6-table.l4                           0         0       0        0         0
nd67-annex6-tests.l4                           0      1235       0        0         0
nd67-annex6.l4                                 0         0       0        0         0
nd67-art12-13-claims.l4                        0         0       0        0         0
nd67-art12-duties-hours.l4                     0         0       0        0         0
nd67-art12-duties-workdays.l4                  0         0       0        0         0
nd67-art5-7-cover.l4                           0         0       0        0         0
nd67-art8-premium.l4                           0         0       0        0         0
nd67-art9-11-term.l4                           0         0       0        0         0
nd67-ch1-general.l4                            0         0       0        0         0
nd67-findings.l4                               0        17       0        0         0
nd67-tests.l4                                  0       180       0        0         0
nd67-vn10-nouns.l4                             0         0       0        0         0
TOTAL (14 modules)                             0      1487       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

`check.sh` exit 0 (run 2026-10-07). No failure is expected and none occurs; `expected_failed` is unchanged (0 for every module).
The regulative modules carry `#TRACE`s rather than assertions (a `DEONTIC` cannot be compared); their breaches print at Information severity and are not errors. Their deadlines are also asserted, on both sides, through the date and hour functions in `nd67-tests.l4`.

The harness can fail. A scratch copy of the eleven modules `nd67-tests.l4` needs, with three expected values in `nd67-tests.l4` altered by one unit (105,000,000 → 105,000,001; 8 → 9 October; 874,000 → 874,001), run through the same `check.sh` on 2026-10-06, printed:

```
module                                    errors satisfied  failed  refused  expected
nd67-annex6-table.l4                           0         0       0        0         0
nd67-annex6.l4                                 0         0       0        0         0
nd67-art12-13-claims.l4                        0         0       0        0         0
nd67-art12-duties-hours.l4                     0         0       0        0         0
nd67-art12-duties-workdays.l4                  0         0       0        0         0
nd67-art5-7-cover.l4                           0         0       0        0         0
nd67-art8-premium.l4                           0         0       0        0         0
nd67-art9-11-term.l4                           0         0       0        0         0
nd67-ch1-general.l4                            0         0       0        0         0
nd67-tests.l4                                  3       172       3        0         0
nd67-vn10-nouns.l4                             0         0       0        0         0
TOTAL (11 modules)                             3       172       3        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
exit 1
```

Three failures, each counted as an error, and exit 1.

## 7. The `vnsrc check` line

`tools/vnsrc.py` was extended in this row, because the brief's checker takes one raw file and this row quotes three (Annex VI is in `nd67-congbao-1019-1020.txt`, Decree 220 in `nd220-2026-congbao-367.txt`).
The extension, described in the script's docstring: a quotation `-- src:ID:N | …` is checked as a slice of lines N of `ID.txt` beside the named raw, exactly as `-- src:N` is checked against it; an unknown ID is a problem; and a Vietnamese run elsewhere must occur in the named raw or in a raw that some `src:ID:` line names. A file with no qualified marker is checked exactly as before (original sha256 `664590f4…6e38e1`). The lead approved the change on 2026-10-06, for this row's copy only.
It was shown to fail on planted errors: an altered quotation of a 1019-1020 line, an unknown ID, and a made-up Vietnamese run each produced a problem.

Two runs, on 2026-10-07, both with the extended `tools/vnsrc.py`, copied verbatim.

The brief's literal command, `python3 -I tools/vnsrc.py check ../../source/raw/nd67-congbao-1017-1018.txt *.l4 *.md`, which includes the lead's `BRIEF.md`, ends:

```
vnsrc check: 2062 src: lines, 723 Vietnamese runs, 6 problems
```

Its six problem lines all name `BRIEF.md` (lines 25 twice, 32 twice, 36 and 57), whose mixed English and Vietnamese phrases are not verbatim runs; `BRIEF.md` is the lead's and not this row's to edit. The six lines are not copied here because their quoted phrases would themselves fail the check in this file.

**The gate**, approved by the lead: the same command over every `.l4` and every `.md` of this directory except `BRIEF.md` (`*.l4 COMPARABLES.md GLOSSARY.md NOTES.md PROGRESS.md SOURCE-LICENSE.md`):

```
vnsrc check: 2062 src: lines, 651 Vietnamese runs, 0 problems
```

No qualified `src:ID:N` line fails either run.

**How this `tools/vnsrc.py` differs from the shared one**, in one sentence: `SRC_LINE` accepts an optional qualifier, `src:ID:N[-M]`, where ID names `ID.txt` beside RAW.txt and the quotation is checked as a slice of that file (an ID with no file is a problem); the rule-2 haystack is RAW.txt plus every raw a `src:ID:` line in the checked files names; and a new subcommand `quoteid` prints quotations in the qualified form (plain `src:N` and every other behaviour are unchanged).

## 8. Open questions for a domain expert

1. R1 / F25: is a person riding free on a private vehicle (a pillion rider, a relative) a "hành khách" for Article 7(1)(b)? If not, is such a person covered anywhere?
2. F5 / R3: do insurers apply Article 7(2)(c) to a rider of a vehicle for which no licence is required?
3. R4: is the 50% of Article 12(6)(a) applied to an injured third party who was not the one at fault?
4. R6 / F28: who fixes the point within a band of Annex VI in practice, the insurer's assessor or a medical assessment council, and on what criterion?
5. R7: what does "cộng lùi" mean in this table? Is it the Ministry of Health's method of combining impairment rates (outside knowledge, unverified), and does it override special case 4's plain sum?
6. R14: are "dính khớp" in special case 1 and "cứng khớp" in the table's rows the same condition?
7. F3: what law now defines the vehicle kinds and the driver's age and licence conditions that Articles 6 and 7 refer to the Road Traffic Law of 2008 for?
8. F14 / F22: what is a working day for Article 12(3)-(4), and is the day of the notice counted?
9. R5: is the 16-seat figure of 3.054.000 an error in the gazette, and if so what is the intended figure?
10. L3: does Article 46(1) of the Law on Insurance Business limit the 5% reduction of Article 12(7)?
11. R10: does the Fund in practice repay an advance made under point (a)?
