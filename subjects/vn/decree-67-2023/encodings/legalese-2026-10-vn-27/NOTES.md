# NOTES — vn/decree-67-2023, encoding row `legalese-2026-10-vn-27`

Decree 67/2023/NĐ-CP of 6 September 2023, the second row on this decree: Chapter II Section 2, the Motor Vehicle Insurance Fund ("Quỹ bảo hiểm xe cơ giới", Articles 14 to 22), and Chapter V as it bears on the compulsory motor insurance, chiefly Article 75 (the insurer's responsibilities), in two vintages: as made, and as amended by Decree 220/2026/NĐ-CP of 22 June 2026.
Row VN-10 encoded the motor chapter's core (Articles 5 to 13, Annexes I and VI); this row encodes what it left out.
Encoded in L4 by one agent, `enc-vn-27`, in one session (run `VN-27-20261007`, 2026-10-07), from `BRIEF.md`.
Status: **draft**.
No domain expert has read it against the source; HG1 has not been sought.

## 0. Build and run

Run on 2026-10-07 with `/Users/mengwong/.local/bin/l4`, `JL4_LIBRARY_PATH` unset.
That path is a symlink to `~/.cabal/bin/l4`, which resolves to the cabal store entry `jl4-0.1-ff13a0ea` (`/Volumes/transcend/caches/cabal/store/ghc-9.10.3-fe9c/jl4-0.1-ff13a0ea/bin/l4`, modified 2026-10-07 06:41 local), sha256 `f65015688970231681a024ceb9ff3a58abba1f5280837cc955c2bba56dbfa8bc`.
This is a newer build than the one row VN-10 recorded (`jl4-0.1-0ee0100b`).
The binary has no `--version`.
Every run prints two Warnings that differing copies of `prelude` and `daydate` exist under `~/.local/share/jl4/libraries/`; the binary uses its embedded copies, and the warnings are not errors.

The command, from this directory:

```
L4=/Users/mengwong/.local/bin/l4 ./check.sh
```

It takes under a minute.
Totals: **10 modules, 0 errors, 445 assertions satisfied, 0 failed, 0 refused**; `check.sh` exit 0 (the table is in §6).

The three gazette PDFs were hashed before use and match `../../subject.json`: `nd67-congbao-1017-1018.pdf` `19a1de3a…1253c8`, `nd67-congbao-1019-1020.pdf` `456cbc7d…d79d59`, `nd220-2026-congbao-367.pdf` `ab0e75cd…1f3a52`.
No network was used.
The figures of Article 17 and the text of Article 75 were checked against the gazette page images (issue 1017+1018, gazette pages 16-18 and 59-61, PDF pages 15-17 and 58-60): the text layer agrees with the page on every figure and phrase used.

Two scripts in `tools/` (run with `python3 -I`, from this directory):

- `tools/art17.py ../../source/raw/nd67-congbao-1017-1018.txt > nd67-vn27-art17-tests.l4` generates the answer table of Article 17 as 316 tests. Its expected values are computed from figures it extracts from the raw text by regular expressions (the limit of Article 6(1), the percentages and thresholds of Articles 12(3)(b) and 17(1)(a), the eight ceilings and their bases, the points of Article 17(1)(i)); it stops if an extraction does not find exactly the shape it expects. Only the mapping from a point letter to this row's L4 names is written by hand.
- `tools/vnsrc.py`, the quotation tool as the brief supplied it (identical to row VN-10's extended copy, sha256 `06a2605b…2453ae`): `quote`, `quoteid` and `check`.

Every `-- src:` line in the hand-written modules was printed by `tools/vnsrc.py quote` or `quoteid`, through a template expander kept outside the deposit (a `--@ 67|6719|220 N [M]` marker becomes the tool's output, gazette running heads dropped); none was typed.

The modules, in import order (each imports only the one before it; the three test modules import only `nd67-vn27-art75.l4`):

| module | what it holds | lines |
| --- | --- | --- |
| `nd67-vn27-nouns.l4` | every `DECLARE`: the vintage, the working-day calendar, the person harmed and the vehicles, an advance, the Fund's money, a contribution year, an offer, the hotline, look-up and explanation, Form 1 of Annex X, parties and acts, results and problems | 444 |
| `nd67-vn27-general.l4` | which vintage answers (Article 77(1); Decree 220 Articles 8-10), the rule that forces the vintage, "the day before", working days, Article 6(1)'s limit | 148 |
| `nd67-vn27-fund-art14-16.l4` | Articles 14-16 (principles, sources, contributions) with Article 20(2)(c) | 191 |
| `nd67-vn27-fund-art17.l4` | Article 17: humanitarian support, repaying advances (with Article 12(3)(b) and its last paragraph), the ceilings, the carry-over, the emergency | 350 |
| `nd67-vn27-fund-art18-22.l4` | Articles 18(2), 21(1)(b) and (d); the rest of Articles 18-22 recorded | 138 |
| `nd67-vn27-ch5-authorities.l4` | Chapter V, Articles 61-74: Article 62(5) encoded; 62, 65 and 73 read in full and recorded | 137 |
| `nd67-vn27-art75.l4` | Article 75, all fourteen clauses, with Article 8(2) and Form 1 of Annex X | 491 |
| `nd67-vn27-tests.l4` | 106 hand-written tests and 18 traces from the source | 484 |
| `nd67-vn27-art17-tests.l4` | GENERATED: 316 tests of Article 17's answer table | 427 |
| `nd67-vn27-findings.l4` | 23 assertions that state the findings' surprising answers | 211 |

To show that the harness can fail, a scratch copy of the modules with three expected values in `nd67-vn27-tests.l4` deliberately altered was run through the same `check.sh` (§6).

## 1. What is encoded and what is not

**Encoded.**
Chapter II Section 2 as far as it decides who is paid what from the Fund, by whom, and when, and every right or duty it gives a policyholder, a person harmed or an insurer: Article 15 (the sources, as the base of the ceilings); Article 16 in full (the amount of an insurer's contribution, the Council's rate and its deadline, the two instalments and their deadlines) with Article 20(2)(c) (the Executive Board's recourse) as the consequence of a late or short payment; Article 17 in full (humanitarian support in its four cases, the repayment of an insurer's advance, the eight ceilings and their two bases, the carry-over of support files, the emergency use of the balance); Article 18(2) (the audited settlement report, owed to the insurers); Article 21(1)(b) and (d) (the budget, notified to the insurers).
Chapter V: Article 62(5) (the police copies of the accident documents, within 5 working days) and Article 75 read in full: (1) as a decision over an offer, with Article 8(2) beside it, and as a standing prohibition; (2)(a) the motor report, its period, deadline and ways of sending, with Form 1 of Annex X as a record and a check that its total adds up; (3) the hotline, (4) the certificate look-up and (5) the explanation as decisions over the insurer's facts; (5), (7), (8), (9), (10), (11), (12), (13) as regulative rules, (10) with its window of dates.
From outside the row's own Articles, repeated under this row's names because Article 17 refers to them: Article 6(1) (the limit per person), Article 12(3)(b) and the last paragraph of Article 12(3) (the advance and the insurer's right to ask for repayment), Article 13's last paragraph (the documents the insurer gathers), Article 8(2) (the premium adjustment); and Article 77(1) of Decree 67 with Article 10(1) of Decree 220 for the vintage.

**Inputs, with their citations, not encoded:** the insurer's answer on cover for the person's harm (row VN-10 computes it; §1.3); whether a vehicle was identified and insured; the assessed injury rate; the Council's contribution rate; the premiums an insurer collected; the Fund's receipts, balance and spending; the facts of an offer, a hotline, a look-up, an explanation; the dates of an investigation result, a notice, the end of a term; the days off of the working-day calendar.

**Declined by a named `REFUSE`:** an event before Decree 67 was in force (Article 77(1)); the contributions for the financial year 2023 and before (Article 76(2), outside the brief's pin on Chapter VI, or earlier rules); an amount of contribution where the Council has decided no rate (Article 16(2)); who receives humanitarian support and the file to submit (left by Article 20(1)(k) to the Council's rules, not in the sources).

**Not encoded (out of scope, §2):** Articles 14, 18(1), 19, 20 (but for (1)(d), (1)(k), (2)(c)), 21 (but for (1)(b), (d)), 22; Articles 61, 62 (but for (5)), 63-74; Article 75(2)(a)'s fire and construction reports and 75(2)(b); Chapters III and IV; Chapter II Section 1 (row VN-10's, except the clauses repeated above); Chapter VI beyond Article 77(1) (Article 76(2) is reached and declined); the annexes no provision in scope names (all but Form 1 of Annex X).

### 1.2 What Decree 220/2026 does to this row's provisions

Read from its text, the body in full (220 src lines 1-211):

- **Articles 1-7** amend Articles 32, 33, 34(2)(m)-(n), 37, 38, 45 and 58: Chapter IV, construction insurance (220 src lines 31-163). None is in this row.
- **Article 8** replaces Annex III and **Form 3 of Annex X**, the construction report (220 src lines 166-171). Form 1, the motor report this row encodes, is untouched.
- **Article 9(1)** replaces "người thứ ba" with "bên thứ ba" in Articles 3(5), 5, 7(1)(a), 10(2)(đ), 12(2), 12(6)(a), 13(5), 41, 43, 46, 47, 54-60 and the title of Chapter IV Section 4 (220 src lines 172-178). None of Articles 14-22 or 61-75 uses the phrase (checked by search: no occurrence in src lines 453-724 or 1779-2032). Article 17(1)(a) refers to Article 7(2), which the substitution does not reach.
- **Article 9(2)** replaces "hoạt động đầu tư xây dựng" with "hoạt động xây dựng" in, among others, **Article 63** and **point (a) of Article 75(2)** (220 src lines 179-183). In Article 75(2)(a) the phrase is in the name of the construction report (Form 3), outside this row's subject; Article 63 is construction.
- **Article 9(3)-(4)** change construction wording (220 src lines 184-193).
- **Article 10(1)**: in force from 1 July 2026; **10(2)**: a contract concluded before then continues as agreed; **10(3)**: government-guaranteed projects (220 src lines 194-205).

So **no provision this row encodes reads differently in the two vintages**, and no answer differs: every scenario of the three test modules that could turn on the vintage was asserted under both (§5.6).
Decree 220's preamble records that the Law on Insurance Business 08/2022/QH15 has been amended by Law 139/2025/QH15 (220 src lines 24-25); this row's aid is the Law's 2022 text, so the LAW forks of §3 may be out of date.
Row VN-10 also read Decrees 105/2025 and 347/2026 at its lead's request and found that they amend only fire-insurance provisions of Decree 67; that was not re-read here (no source of this row holds them).

### 1.3 How this row joins row VN-10

This row does not import VN-10, so a customer-facing answer calls VN-10 first and passes what it found into this row's inputs.

**After VN-10's cover decision for health and life** (`Article 7 — the answer on cover for the health and life of`), where the answer is anything but `covered`, call `Article 17(1)(a) — the humanitarian support, in the vintage in force on the day of the accident, for` with a `A person harmed in a road accident` whose vehicle is `an identified, insured vehicle, whose insurer answers` and the answer mapped one to one:

| VN-10 `The answer on cover` | this row's `The insurer's answer on the person's harm` |
| --- | --- |
| `covered` | `the insurer covers the harm` |
| `outside the scope: the vehicle was neither in road traffic nor operating` | `the harm is outside the scope of Article 7(1)` |
| `outside the scope: the person is neither a third party nor a passenger` | `the harm is outside the scope of Article 7(1)` |
| `excluded: an intentional act of the owner or the driver` | `Article 7(2)(a): an intentional act of the owner or the driver` |
| `excluded: an intentional act of the injured person` | `Article 7(2)(a): an intentional act of the injured person` |
| `excluded: the driver fled without performing the owner's civil liability` | `Article 7(2)(b): the driver fled without performing the owner's civil liability` |
| `excluded: the driver's age or licence` | `Article 7(2)(c): the driver's age or driving licence` |
| `excluded: war, terrorism or an earthquake` | `Article 7(2)(h): war, terrorism or an earthquake` |
| the property answers (`a passenger's property`, `an indirect consequence`, `alcohol or drugs, for damage to property`, `property stolen or robbed`, `special property`) | not used: the support pays only for death and injury |

Where there is no contract for the vehicle, the vehicle is `an identified vehicle with no compulsory insurance in force`; where it was never identified, `a vehicle that was not identified`.
So VN-10's finding R1 (a pillion rider who is not a passenger has no cover) and R2 (a car parked with nobody at the controls) end, in this row, in humanitarian support of 30% or 10% of the limit (finding R2 here).

**After VN-10's advance** (`Article 12(3) — the advance for`): where the insurer later finds the accident excluded or outside the scope, call `Article 17(1)(a) — under` v `, what the Fund owes the insurer for` with the point of Article 12(3) the advance was paid under.

**Before a sale**: VN-10's `Annex I — the premium for the term of` gives `the premium of Annex I for the vehicle and the term`; call `Article 75(1) — under` v `, the offer carries a promotion or a payment discount in some form:` and `Articles 75(1) and 8(2) — under` v `, the defects of`.

**Before expiry**: VN-10's contract field `insurance ends on` is `the insurance ends on` of `Article 75(10) — under` v `, a notice sent on` … `is in time for insurance ending on`.

**During a claim**: VN-10's Article 12(3) deadline for the advance (3 working days) and this row's `Article 62(5) — the last day for the police copies, the investigation result being of`, with the documents of `Article 75(7) with Article 13 — the documents that are the insurer's to gather, …`.

## 2. Coverage table

Every provision in scope, with its heading as the decree writes it.
Dispositions: `encoded`, `inert` (quoted, decides no case), `out-of-scope` (with its reason), `reached-and-refused`.
Totals: **69 rows: 34 encoded, 7 inert, 25 out-of-scope, 3 reached-and-refused, 0 deferred**.

| provision | heading as written | English gloss | src | disposition | where in the L4 |
| --- | --- | --- | --- | --- | --- |
| Chương II, Mục 2 | CƠ CHẾ QUẢN LÝ, SỬ DỤNG QUỸ BẢO HIỂM XE CƠ GIỚI | the Motor Vehicle Insurance Fund | 453-454 | inert: a section heading | `nd67-vn27-fund-art14-16.l4` |
| Điều 14(1)-(3) | Nguyên tắc quản lý, sử dụng Quỹ bảo hiểm xe cơ giới | principles: purposes; contributed by insurers, managed at the Association; transparent use | 457-468 | inert: purposes and a manner of management; the duty to contribute is Article 16's and what the money is for is Article 17's | comment, `§§ Article 14` |
| Điều 15 | Nguồn hình thành Quỹ bảo hiểm xe cơ giới | the four sources of the Fund | 469-474 | encoded | `Article 15 — the Fund's receipts from`; base of the ceilings (fork V12) |
| Điều 16(1) | Đóng góp Quỹ bảo hiểm xe cơ giới | at most 1% of the preceding year's premiums | 477-481 | encoded (fork V18) | `Article 16(1)-(2) — the insurer's contribution for` |
| Điều 16(2) | (same) | the Council decides the rate before 30 April | 482-484 | encoded | `Article 16(2) — the last day for the Council to decide the rate for`; `Article 16(2) — the Council must decide the rate and notify it, for` |
| Điều 16(2), no rate decided | (same) | the amount when no rate exists | 482-484 | reached-and-refused: the amount cannot be computed | `the Fund's Management Council has decided no contribution rate for the year, …` |
| Điều 16(3)(a)-(b) | (same) | 50% before 30 June; the rest before 31 December | 485-491 | encoded (regulative, dates) | `Article 16(3) — the insurer must pay its contribution for`; the two date functions |
| Điều 17(1)(a), first paragraph | Nội dung và tỷ lệ chi của Quỹ bảo hiểm xe cơ giới | humanitarian support: four cases, 30% and 10% of the limit | 494-502 | encoded (forks V6-V10) | `Article 17(1)(a) — under` … `, the humanitarian support for`; generated tests |
| Điều 17(1)(a), second paragraph | (same) | the Fund repays a point (b) advance | 503-507 | encoded (fork V11) | `Article 17(1)(a) — under` … `, what the Fund owes the insurer for` |
| Điều 17(1)(a), third paragraph | (same) | 30% ceiling; unpaid support files carried over | 510-514 | encoded (fork V24) | ceilings table; `Article 17(1)(a) — when a file of` |
| Điều 17(1)(b)-(h) | (same) | the other heads and their ceilings | 515-550 | encoded | `Article 17(1) — the ceilings`; `… the most the Fund may spend …`; `… the heads overspent by` |
| Điều 17(1)(i) | (same) | an emergency: the balance for points (d)-(h) | 551-559 | encoded (fork V13) | `Article 17(1)(i) — …` (two rules) |
| Điều 17(2) | (same) | the Association's priorities | 560-563 | inert: names no measure of priority | comment |
| Điều 18(1) | Quản trị, điều hành hoạt động của Quỹ bảo hiểm xe cơ giới | the organs of the Fund | 564-571 | out-of-scope: who governs the Fund; gives no person harmed, policyholder or insurer a right | comment |
| Điều 18(2) | (same) | the audited settlement report to the Ministry and the insurers; publication | 572-576 | encoded (forks V2, V17) | `Article 18(2) — the settlement report for`; `… the last day to send …` |
| Điều 19 | Cơ cấu tổ chức, quản trị điều hành của Quỹ bảo hiểm xe cơ giới | the composition of the organs | 579-605 | out-of-scope: membership of the Council and Boards; the insurers' seats are an organisational rule, not a right a claim turns on | comment |
| Điều 20(1)(d) | Nhiệm vụ, quyền hạn của tổ chức, bộ máy Quỹ bảo hiểm xe cơ giới | the Council decides the contribution rate | 616-617 | encoded with Article 16(2) | `Article 16(2) — the Council must decide …` |
| Điều 20(1)(k) | (same) | the Council issues the process and file for support and repayment | 633-634 | reached-and-refused: the Council's rules are not in the sources | `the Fund's Management Council's process, procedure and file …`; `Article 17(1)(a) — who receives the support, and the file to submit, for` |
| Điều 20(2)(c) | (same) | the Executive Board urges or recovers late or short contributions | 649-650 | encoded as the consequence of Article 16(3) | `Article 20(2)(c) — the Executive Board must urge the insurer or recover the contribution` |
| Điều 20, the rest | (same) | the organs' other tasks | 606-657 | out-of-scope: internal responsibility, regulations, the database's management, supervision; no right of a claimant or duty of an insurer | comment |
| Điều 21(1)(b) | Công tác lập dự toán, kế toán, quyết toán của Quỹ bảo hiểm xe cơ giới | the approved budget notified to the insurers | 665-668 | encoded (forks V17, V22) | `Article 21(1)(b) — the approved budget must be notified to the insurers` |
| Điều 21(1)(d) | (same) | an adjusted budget notified to the insurers | 674-676 | encoded (fork V22) | `Article 21(1)(d) — an adjusted budget must be notified to the insurers` |
| Điều 21, the rest | (same) | preparing the budget; carrying plans over; accounts; quarterly report; settlement | 660-664, 669-671, 677-695 | out-of-scope: the Fund's internal accounting and its reports to the Ministry; no right or duty of a claimant or an insurer (21(3) is read for fork V17) | comment |
| Điều 22 | Thành lập Hội đồng quản lý Quỹ bảo hiểm xe cơ giới, thay đổi thành viên Hội đồng quản lý Quỹ bảo hiểm xe cơ giới | setting up the Council; changing its members | 696-723 | out-of-scope: an application between the Association and the Ministry, with Annexes VIII and IX | comment |
| Chương V | TỔ CHỨC THỰC HIỆN | organisation of implementation | 1779-1780 | inert: a chapter heading | `nd67-vn27-ch5-authorities.l4` |
| Điều 61 | Trách nhiệm của Bộ Tài chính | the Ministry of Finance | 1782-1795 | out-of-scope: the regulator's powers (propaganda, supervision, inspection, sanctions, the ASEAN body); no right enforceable under this decree | comment |
| Điều 62(5) | Trách nhiệm của Bộ Công an | police copies of the Article 13(5) documents within 5 working days | 1810-1812 | encoded (forks V5, V20) | `Article 62(5) — the last day for the police copies, …`; `Article 62(5) — the police must provide copies of the accident documents` |
| Điều 62, the rest | (same) | propaganda; inspection; fire; data sharing; rewards | 1797-1809, 1813-1818 | out-of-scope: read in full; none gives a period or right a motor claim turns on (62(6) feeds the database) | comment |
| Điều 63 | Trách nhiệm của Bộ Xây dựng | the Ministry of Construction | 1819-1826 | out-of-scope: construction insurance (Decree 220 Article 9(2) rewords it) | comment |
| Điều 64 | Trách nhiệm của Bộ Giao thông vận tải | the Ministry of Transport | 1827-1833 | out-of-scope: coordination and supervision; no claimant's right | comment |
| Điều 65 | Trách nhiệm của Bộ Y tế | the Ministry of Health | 1834-1839 | out-of-scope: read in full; the Ministry directs facilities to provide medical copies, with no period and no right against a facility; it holds no guidance on the alcohol level of Article 7(2)(đ) (finding R16) | comment |
| Điều 66 | Trách nhiệm của Bộ Thông tin và Truyền thông | the Ministry of Information | 1840-1842 | out-of-scope: propaganda | comment |
| Điều 67 | Trách nhiệm của bộ, cơ quan ngang bộ, cơ quan thuộc Chính phủ | ministries and agencies | 1843-1853 | out-of-scope: coordination and propaganda | comment |
| Điều 68 | Trách nhiệm của Ủy ban nhân dân tỉnh, thành phố trực thuộc Trung ương | provincial People's Committees | 1856-1866 | out-of-scope: enforcement against uninsured owners (68(3)) sets no sanction of its own; the owner's duty to buy is Article 4(1), row VN-10 | comment |
| Điều 69 | Trách nhiệm của Bộ Tư lệnh Bộ đội Biên phòng | the Border Guard | 1867-1872 | out-of-scope: border checks on transiting vehicles | comment |
| Điều 70 | Trách nhiệm của Ủy ban An toàn Giao thông Quốc gia | the National Traffic Safety Committee | 1873-1878 | out-of-scope: coordinates with the Fund on support; adds nothing to who is paid | comment |
| Điều 71 | Trách nhiệm của Cơ quan Quốc gia Việt Nam thực hiện Nghị định thư số 5 về Chương trình bảo hiểm bắt buộc xe cơ giới ASEAN | the national body for ASEAN Protocol 5 | 1879-1890 | out-of-scope: a standing body and its proposals | comment |
| Điều 72 | Trách nhiệm của Hiệp hội Vận tải ô tô Việt Nam | the Vietnam Automobile Transport Association | 1891-1896 | out-of-scope: propaganda | comment |
| Điều 73 | Trách nhiệm của Hiệp hội Bảo hiểm Việt Nam | the Vietnam Insurance Association | 1897-1902 | out-of-scope: read in full; a report between public bodies, propaganda, and a publicity duty naming no information or audience; no certificate look-up (that is Article 75(4)) | comment |
| Điều 74 | Trách nhiệm của cơ quan, tổ chức và cá nhân có cơ sở có nguy hiểm về cháy, nổ | fire-risk establishments | 1903-1907 | out-of-scope: fire insurance | comment |
| Điều 75(1) | Trách nhiệm của doanh nghiệp bảo hiểm | no promotion, no payment discount | 1909-1910 | encoded: a decision over an offer (with Article 8(2)) and a prohibition (forks V14, V15) | `Article 75(1) — under` … `, the offer carries …`; `Articles 75(1) and 8(2) — under` … `, the defects of`; `Article 75(1) — the insurer shall not offer …` |
| Điều 75(2)(a), the motor report | (same) | Form 1 to the Ministry of Finance by 31 March | 1911-1925 | encoded | `Article 75(2)(a) — …` (five rules) |
| Điều 75(2)(a), Forms 2 and 3; 75(2)(b) | (same) | fire and construction reports | 1914-1917, 1926-1934 | out-of-scope: fire and construction insurance | comment |
| Điều 75(3) | (same) | the 24/7 hotline, calls recorded | 1935-1939 | encoded (fork V23) | `Article 75(3) — what the hotline lacks:`; `… the hotline meets the clause:` |
| Điều 75(4) | (same) | online certificate look-up | 1940-1944 | encoded | `Article 75(4) — under` … `, the look-up meets the clause:` |
| Điều 75(5) | (same) | explaining the cover; compulsory against voluntary | 1945-1947 | encoded (fork V16) | `Article 75(5) — under` … `, the explanation meets the clause:`; `Article 75(5) — the insurer must explain the cover` |
| Điều 75(6) | (same) | more use of information technology | 1948-1949 | inert: sets no measure an act could meet or miss | comment |
| Điều 75(7) | (same) | one claim file; gather the insurer's documents | 1952-1956 | encoded | `Article 75(7) with Article 13 — the documents …`; `Article 75(7) — the insurer must gather its own claim documents` |
| Điều 75(8) | (same) | advance and pay promptly and accurately | 1957-1958 | encoded (no period; finding R11) | `Article 75(8) — the insurer must advance and pay promptly and accurately` |
| Điều 75(9) | (same) | pay the police's copying costs; confidentiality | 1959-1961 | encoded | `Article 75(9) — the insurer must pay for the copies and keep the investigation secret` |
| Điều 75(10) | (same) | notify expiry within 15 days before the end | 1962-1963 | encoded (forks V4, V19) | `Article 75(10) — …` (four rules) |
| Điều 75(11) | (same) | contribute to the Fund under Article 16 | 1964-1967 | encoded through Article 16(3); its fire limb out-of-scope | `Article 75(11) — the insurer must contribute to the Fund for` |
| Điều 75(12) | (same) | separate accounts | 1968-1969 | encoded | `Article 75(12) — …` |
| Điều 75(13) | (same) | information into the database | 1970-1972 | encoded | `Article 75(13) — …` |
| Điều 75(14) | (same) | other duties by law | 1973 | inert: a pointer outside the decree; LAW forks of §3 | comment |
| Phụ lục X, Mẫu số 1 | BÁO CÁO VỀ TÌNH HÌNH THỰC HIỆN BẢO HIỂM BẮT BUỘC TRÁCH NHIỆM DÂN SỰ CỦA CHỦ XE CƠ GIỚI | Form 1, the motor report | 1019-1020: 2642-2700 | encoded: a record and a check that its total adds up | `A report on Form 1`; `Annex X, Form 1 — …` |
| Phụ lục X, Mẫu số 2-4 | (fire and construction reports) | other forms | 1019-1020: 2700-2810 | out-of-scope: fire and construction insurance; Decree 220 replaces Form 3 | — |
| Phụ lục VIII, IX | (applications to set up the Council or change its members) | forms of Article 22 | 1019-1020: 2580-2641 | out-of-scope: named only by Article 22, out of scope | — |
| Điều 6(1) | Giới hạn trách nhiệm bảo hiểm | the limit per person, as Article 17(1)(a) uses it | 187-189 | encoded, repeated from row VN-10's scope | `Article 6(1) — the limit per person per accident, for health and life` |
| Điều 12(3)(b) and last paragraph | Nguyên tắc bồi thường bảo hiểm | the point (b) advance; the insurer may ask the Fund | 317-319, 325-334 | encoded, repeated from row VN-10's scope, as Article 17(1)(a) names them | `Article 12(3)(b) — the advance for`; `Article 12(3) — the insurer may ask the Fund to repay` |
| Điều 8(2) | Mức phí bảo hiểm | the 15% adjustment, beside Article 75(1) | 235-238 | encoded, repeated from row VN-10's scope | `Article 8(2) — a ground the clause gives:`; `Article 8(2) — the adjustment is within 15% in` |
| Điều 76(2) | Điều khoản chuyển tiếp | the Fund mechanism from 2023; the 2023 contributions | 1998-2004 | reached-and-refused: the brief pins Chapter VI to what row VN-10 encoded, which does not include it | `the contributions for the financial year 2023 and before are governed by Article 76(2) …` |
| Điều 76(1), (3) | (same) | existing contracts; tendered contracts | 1979-1997, 2005-2007 | out-of-scope: contracts (row VN-10 encodes 76(1)); nothing in this row is a term of a contract (fork V1) | — |
| Điều 77(1) | Hiệu lực thi hành | in force from signature | 2008-2009 | encoded | `the vintage in force on` |
| Điều 77(2)-(3), 78 | Hiệu lực thi hành; Trách nhiệm thi hành | decrees replaced; references; who implements | 2010-2032 | inert: 77(2) is named in the refusal of an event before Decree 67; 77(3) and 78 decide no case here | comment |
| Decree 220, Điều 8-9 | Thay thế một số Phụ lục và mẫu …; Thay thế một số cụm từ tại Nghị định số 67/2023/NĐ-CP | annex, form and phrase substitutions | 220: 166-193 | encoded as their effect on this row: none (§1.2) | `Decree 220/2026 changes a provision this row encodes, in`; `the answer in` … `, unamended by Decree 220/2026:` |
| Decree 220, Điều 10(1) | Điều khoản thi hành | in force 1 July 2026 | 220: 194-195 | encoded | `the vintage in force on` |
| Decree 220, Điều 1-7, 10(2)-(3) | (amendments to Chapter IV; transition) | construction; contracts | 220: 31-163, 196-205 | out-of-scope: construction insurance, and the contract transition, which no rule of this row turns on (fork V1) | — |
| Chương III, IV; Chapter II Section 1 (Mục 1); Phụ lục I-VII | (fire; construction; row VN-10's motor core; their annexes) | other rows' subject | 725-1778; 175-452; 2041-3199; 1019-1020: 1-2579 | out-of-scope: reached, not encoded, per the brief; the motor core is row VN-10's | — |

## 3. Fork register

A fork is an ambiguity this encoding resolved: the readings it saw, the one it took, and why.
Places looked at where no fork was found are named at the end.

| # | where | the question | readings | taken, and why |
| --- | --- | --- | --- | --- |
| V1 | Art 77(1); 220 Art 10(1)-(2) | Which date decides the vintage for this row's rules? | (i) the date of the event the rule turns on (accident, offer, notice, year); (ii) a contract's conclusion date (row VN-10's F1) | **(i)**: Article 76(1) and Decree 220 Article 10(2) speak only of contracts; the Fund's support reaches people with no contract at all, and the insurer's duties are the decree's, not the contract's. Moot in outcome: no provision in scope differs (§1.2). |
| V2 | Arts 16(2), 16(3), 18(2) | "Trước ngày D": is D included? | (i) strictly before D; (ii) on or before D | **(i)**: the decree writes "chậm nhất là ngày D" where it includes D (Art 75(2), src 1922) and "đã giao kết trước ngày" in Art 76(1), which cannot include the day of commencement. Last days: 29 April, 29 June, 30 December, 30 March. |
| V3 | Arts 16(1), 75(2)(a) | What is "năm tài chính" (financial year)? | (i) the calendar year; (ii) another accounting year | **an input** (the caller names the year); Art 75(2)(a)'s data period "từ ngày 01 tháng 01 đến ngày 31 tháng 12" is the calendar year, and the deadlines are computed on it. Outside knowledge, unverified: Vietnamese accounting years are usually calendar years. |
| V4 | Art 75(10) | "trong vòng 15 ngày trước khi hết thời hạn bảo hiểm": what window, what days? | (i) the 15 calendar days before the end date, end excluded; (ii) the same, end date included; (iii) at least 15 days before (any earlier day counts) | **(i)**: "ngày" is a calendar day (the decree writes "ngày làm việc" for working days, Arts 12(3), 12(4), 62(5)); "trong vòng" (within) makes a window, not a minimum; on the end date the term is no longer "before" its end. Window: end − 15 to end − 1 (finding R13). |
| V5 | Art 62(5) | Which days are "ngày làm việc", and is the anchor day counted? | — | row VN-10's F14 and F22, followed: Monday to Friday less the caller's days off; day 1 is the next working day. |
| V6 | Art 17(1)(a) | "tử vong và tỷ lệ tổn thương từ 81% trở lên": both, or two cases? | (i) two cases; (ii) both | **(i)**: a death has no injury rate; row VN-10 read the same words of Art 12(3)(b) the same way (its F15). |
| V7 | Art 17(1)(a) | Does "(trừ hành động cố ý gây thiệt hại của người bị thiệt hại)" limit every case, or only the exclusions of Art 7(2)? | (i) the Art 7(2) case only; (ii) all four cases | **(i)**: it sits inside the fourth case, right after "khoản 2 Điều 7", and carves the victim's limb out of Art 7(2)(a). Finding R4 shows the consequence. |
| V8 | Art 17(1)(a) | Several vehicles caused the harm, one insured and covering it, one uninsured: is the person in a case? | (i) yes, if any vehicle puts the harm in a case; (ii) only if all do | **(i)**: "xe không tham gia bảo hiểm" is true of the uninsured vehicle whatever the other did. Finding R5. |
| V9 | Art 17(1)(a) | Which injury rate, assessed by whom? | — | **an input**: the rate assessed for the person; the decree names no assessor for the Fund (Art 12(3)(b) speaks of an estimate, Art 17(1)(a) does not). |
| V10 | Art 17(1)(a) | "không thuộc phạm vi bảo hiểm": of the accident, or of the person's harm? | (i) the person's harm; (ii) the accident as a whole | **(i)**: the support is "cho một người"; an accident can be within the scope for one person and not for another (the driver, a non-passenger on the vehicle). Finding R2. |
| V11 | Art 17(1)(a), second paragraph | How much does the Fund repay, and does the victim's-intent exception apply? | (i) the amount advanced, up to what Art 12(3)(b) prescribes for the estimated harm, for every exclusion; (ii) whatever was advanced; (iii) as (i), less the victim's intent | **(i)**: the paragraph names "tạm ứng bồi thường quy định tại điểm b khoản 3 Điều 12" and "loại trừ trách nhiệm bảo hiểm" with no exception. Finding R4. |
| V12 | Arts 15, 17(1) | "tổng số tiền đóng vào Quỹ bảo hiểm xe cơ giới hàng năm": which receipts? | (i) the insurers' contributions of the year; (ii) every receipt of Art 15 | **(i)**: "đóng" (pay in as a contribution) is the verb of Art 16; interest, sponsorship and other receipts are "thu", "tài trợ", "hỗ trợ". They reach spending through the balance. |
| V13 | Art 17(1)(i) | "tổng mức chi không vượt quá tỷ lệ quy định tại điểm d, …, h … tương ứng với mức đóng góp tối đa 1%" | (i) the sum of those rates, of the contributions at 1% of the premiums; (ii) the same rates, of the actual contributions; (iii) each rate separately | **(i)**: "tổng mức chi" is one total, and "tương ứng với mức đóng góp tối đa 1%" names the base. Finding R8. |
| V14 | Arts 75(1), 8(2) | Is an Art 8(2) reduction a "chiết khấu" (discount) Art 75(1) forbids? | (i) no, within 15% on an Art 8(2) ground; any other reduction is a discount in some form; (ii) every reduction is forbidden; (iii) only discounts at payment are forbidden | **(i)**: Art 8(2) expressly allows "giảm" (reductions) on two grounds, so (ii) empties it; "dưới mọi hình thức" (in any form) defeats (iii). Finding R9. |
| V15 | Art 75(1) | Does the ban reach voluntary cover sold with the compulsory, or an agent's rebate? | (i) no: it binds the insurer, "đối với bảo hiểm bắt buộc trách nhiệm dân sự của chủ xe cơ giới"; (ii) yes, by its purpose | **(i)** on its words. Finding R10. |
| V16 | Art 75(5) | "số tiền bảo hiểm tối thiểu" for the motor insurance, which has none | (i) read as the limit of liability (Art 6); (ii) inapplicable to motor | **(i)**: Art 4(3) pairs the two, "số tiền bảo hiểm tối thiểu hoặc giới hạn trách nhiệm bảo hiểm" (src 112-113). |
| V17 | Arts 18(2), 21(1)(b) | Who sends the settlement report and the approved budget? (passive voice) | (i) the Executive Board; (ii) the Council; (iii) the Association | **(i)**: Art 21(3) makes the Board prepare the settlement report, and Art 21(1)(b) makes it report the budget. Art 18(2)'s date is read with the sending only; publication has no period. Finding R15. |
| V18 | Art 16(1)-(2) | "trích tối đa 1%" and the Council's rate | (i) the insurer owes the Council's rate, capped at 1%; (ii) the insurer may pay any amount up to 1% | **(i)**: (2) gives the rate to the Council; (1) caps it. A rate above 1% is rejected as a defect in the facts. |
| V19 | Art 75(10) | Notify the buyer AND the insured, or either? | — | both (the clause lists them with a comma, as "bên mua bảo hiểm, người được bảo hiểm" throughout); one notice where they are one person. |
| V20 | Art 62(5) | Whose duty, to whom, from when? | — | the police directed (the Ministry's duty is to direct them); to the insurer, who gathers the Art 13(5) documents (Art 13 last paragraph); from "ngày có kết quả điều tra". |
| V21 | Art 16(3)(b) | "số tiền còn lại" (the remaining amount) | — | the amount of (1) and (2) less what was paid under (a); nothing more is due where the first payment was the whole. |
| V22 | Art 21(1)(b) | "ngay sau khi phê duyệt" (immediately after approval) | — | no period in days: none invented (as row VN-10 did with "ngay" in Art 12(1)(a)). |
| V23 | Art 75(3) | "24 giờ/7 ngày"; "ghi âm các cuộc gọi" | — | continuous operation; every call recorded. |
| V24 | Art 17(1)(a), third paragraph | A support file larger than what is left under the 30% ceiling | (i) carried whole; (ii) paid in part now, the rest next year | **(i)**: the paragraph carries "hồ sơ" (files), not amounts. |

**LAW forks** (Law on Insurance Business 08/2022/QH15, `.aids/law-08-2022-qh15.txt`, an aid, in its 2022 text; not encoded; quoted here in English):

| # | the Law | aid lines | what it does here |
| --- | --- | --- | --- |
| L1 | Art 31(1): pay within the agreed period, or within 15 days of receiving a complete, valid claim file | 718-724 | fills Art 75(8)'s silence on a period; but Art 75(7) makes the insurer answer for the file's completeness (finding R11); not encoded |
| L2 | Art 30(1): a claim file within 1 year of the insured event | 706-710 | a contract claim; it does not obviously reach humanitarian support, which is not paid under a contract: the support has no time-bar in the sources (finding R6) |
| L3 | Art 20(2)(b): explain clearly the benefits, the exclusions, the buyer's rights and duties | 471-473 | wider than Art 75(5) (it names the exclusions); not encoded |
| L4 | Art 89(3): the Fund is formed from insurers' contributions and other lawful sources for humanitarian support and other activities; its mechanism is the Government's | 1838-1846 | the authority for Articles 14-22; consistent with them |
| L5 | Art 8(4): an insurer may not refuse to sell compulsory insurance to one who meets the conditions | 240-243 | consistent with Art 75(1): price competition is closed, so is refusal |
| L6 | Art 24: an unclear term of an insurance contract is read for the buyer | 588-591 | reaches contracts, not the Fund's rules; forks V7, V10 and V14 were not resolved by it |

Places looked at with no fork found: Article 15 (four sources, a closed list but for "khác (nếu có)"); Article 16(3)'s percentages (50%, the rest); the eight ceilings' figures and bases (unambiguous in the text and on the page images); Article 18(2)'s list of recipients; Article 75(4)'s list of who may look up; Article 75(9) (two plain duties); Article 75(12)-(13); Form 1's columns.

## 4. Findings

A finding is a defect or a surprise in the decree as written, not an ambiguity resolved.
Each gives the source lines, a minimal scenario, and the evidence (an assertion in `nd67-vn27-findings.l4` or `nd67-vn27-tests.l4`), or the words "reading only".

**R1. Article 12(3) lets the insurer ask the Fund to repay any advance; Article 17(1)(a) binds the Fund to repay only a point (b) advance.**
Src 331-334 against 503-507; row VN-10's R10, now with the Fund's side encoded.
Scenario: the accident is found within the scope, the insurer advances 70% for a death (105,000,000), then finds it excluded: it may ask, and the Fund owes nothing.
Evidence: `nd67-vn27-findings.l4`, R1.

**R2. The Fund's support reaches the driver who caused the accident, including an owner who never bought the insurance.**
Src 495-502; Article 4(1), src 103-106 (the duty to buy).
The cases are "xe không tham gia bảo hiểm" and "không thuộc phạm vi bảo hiểm" with no condition on who the injured person is (fork V10).
Scenario: the owner of an uninsured motorbike, in breach of Article 4(1), crashes alone and dies: 45,000,000 to his estate from a Fund the insurers pay for; a driver of an insured car crashes alone and is injured at 85%: 45,000,000.
It also means row VN-10's uncovered pillion rider (its R1) and the person hit by a car parked with nobody at the controls (its R2) are each paid 30% or 10% of the limit here.
Evidence: `nd67-vn27-findings.l4`, R2.

**R3. One death can be paid twice by the Fund.**
Src 327-328, 498-500, 503-507.
Scenario: an unlicensed driver kills a pedestrian; the scope not yet found, the insurer advances 45,000,000 under Article 12(3)(b); the accident is then found excluded under Article 7(2)(c): the Fund repays the insurer 45,000,000, and the pedestrian's death is in case (4) for 45,000,000 of humanitarian support.
Nothing nets the support against the advance, or asks the family to return the advance.
Evidence: `nd67-vn27-findings.l4`, R3.

**R4. The injured person's own intent bars support only where the vehicle was identified and insured, and never bars the repayment.**
Src 496-498, 503-507 (fork V7, V11).
Scenario: a person deliberately steps in front of a vehicle and dies: nothing if the vehicle was insured; 45,000,000 if it was uninsured or drove off unidentified; and an advance paid to that person's family under point (b) is repaid to the insurer when the intent is found.
Evidence: `nd67-vn27-findings.l4`, R4.

**R5. Support is paid on top of compensation where one of two vehicles was uninsured.**
Src 495-502 (fork V8).
Scenario: a pedestrian is killed by two vehicles, one insured (whose insurer pays its share by degree of fault, Article 12(6)(a), row VN-10), one uninsured: 45,000,000 of support besides.
Evidence: `nd67-vn27-findings.l4`, R5.

**R6. The support has no named recipient, procedure, deadline or time-bar.**
Src 494-502; Article 20(1)(k), src 633-634.
Compensation has a payee (Article 12(5)) and a file (Article 13); the support has neither, and Article 20(1)(k) leaves "quy trình, thủ tục và hồ sơ chi hỗ trợ nhân đạo" to the Council, whose rules are not in the sources. The Law's 1-year limit (LAW L2) is for contract claims.
Scenario: the family of a person killed by an unidentified vehicle asks who may claim, with what, by when: the decree does not say.
Evidence: `nd67-vn27-findings.l4`, R6 (a named refusal).

**R7. Point (a)'s ceiling is shared by support and repayments, only support files carry over, and the Council may leave the Fund empty.**
Src 478-479 ("trích tối đa 1%": a ceiling, no floor), 510-514.
The 30% ceiling covers both paragraphs of point (a), but the carry-over names only "các hồ sơ chi hỗ trợ nhân đạo"; the repayment to insurers has no deadline and no carry-over, and nothing says which is paid first when the ceiling binds.
A rate of 0% is lawful; with no contributions and no balance, point (a) may spend nothing, and every support file is carried to the next year, indefinitely.
Evidence: `nd67-vn27-findings.l4`, R7 (a contribution of 0 at a 0% rate; a 15,000,000 file carried).

**R8. In an emergency the balance is released to the police, rewards, the database, ASEAN and administration, not to humanitarian support.**
Src 551-559 (fork V13).
Point (i) lets the Council spend earlier years' balance in a declared natural-disaster emergency or group A epidemic, but only on points (d), (đ), (e), (g), (h); points (a)-(c) get nothing from it, and its ceiling is computed on a 1% contribution the insurers may not have made.
Scenario: premiums of 10,000,000,000,000 and a Council rate of 0.5%: points (d)-(h) may normally spend 19,000,000,000; in the emergency, 38,000,000,000 more from the balance.
Evidence: `nd67-vn27-findings.l4`, R8.

**R9. Articles 75(1) and 8(2) meet at the label.**
Src 1909-1910 against 235-238 (fork V14); row VN-10's R12 (no criterion).
The same price for the same car is lawful pricing or a prohibited discount according to the ground the offer states, and nothing in the decree tests whether the stated history supports it.
Scenario: 371,450 for a car whose Annex I premium is 437,000: lawful if the offer says "claims history", prohibited if it says "for buying online".
Evidence: `nd67-vn27-findings.l4`, R9; both sides of the 15% in `nd67-vn27-tests.l4`.

**R10. A discount moved onto voluntary cover sold alongside escapes Article 75(1).**
Src 1909-1910; Article 4(3), src 112-118 (fork V15).
Article 4(3) lets the parties add voluntary cover and requires only that the compulsory part be separated; the ban reaches the compulsory cover alone, and Article 75 binds the insurer, not an agent or a platform.
Scenario: the compulsory cover at the full 437,000 and the voluntary cover sold with it 200,000 cheaper: no defect under Article 75(1).
Evidence: `nd67-vn27-findings.l4`, R10 (the bundle); the agent's rebate is reading only.

**R11. Nothing in the decree sets an outer time for paying the compensation.**
Src 1952-1958 (Article 75(7)-(8)), 1810-1812 (Article 62(5)), 437-450 (Article 13(5)-(6), last paragraph).
Article 75(8) says "nhanh chóng và chính xác" (promptly and accurately) and gives no period (row VN-10's R13: Article 12(11) gives none either).
The Law's 15 days (LAW L1) run from a complete and valid file, but Article 75(7) makes the insurer answer for the file's completeness and gather its own assessment record (13(6)) with no period, and for a death the file needs the police documents of 13(5), due 5 working days after an investigation result that no text times.
So the clock the Law would start is controlled by the insurer and by an investigation without a deadline.
Evidence: reading only; the dates of Article 62(5) are tested in `nd67-vn27-tests.l4`.

**R12. Article 75(5) asks for a result no one can check, about a figure the motor insurance does not have.**
Src 1945-1947 (fork V16).
"bảo đảm bên mua bảo hiểm, người được bảo hiểm phân biệt rõ" is a duty of result on the buyer's understanding; "số tiền bảo hiểm tối thiểu" has no motor counterpart but the limit of liability.
Evidence: reading only; the encoding takes the buyer's understanding as a fact.

**R13. An early expiry notice does not count, and one on the last day of cover is late.**
Src 1962-1963 (fork V4).
"trong vòng 15 ngày trước khi hết thời hạn" is a window: a notice a month ahead is outside it, and the insurer must notify again within the last 15 days.
Scenario: insurance ending 1 January 2027: a notice on 1 December 2026 does not meet the clause; nor does one on 1 January 2027.
Evidence: `nd67-vn27-findings.l4`, R13; both edges in `nd67-vn27-tests.l4`.

**R14. The insurer's first instalment can fall due before its amount exists.**
Src 482-491.
The Council must decide the rate before 30 April, but nothing follows if it does not; the insurer's 50% still falls due before 30 June, and a missed instalment sends the Executive Board after the insurer (Article 20(2)(c)), not after the Council.
Scenario: no rate decided by 29 June 2026: the amount cannot be computed, the instalment is due that day.
Evidence: `nd67-vn27-findings.l4`, R14.

**R15. Duties with no named party.**
Src 572-576 (Article 18(2): "phải được gửi", passive, no sender; the publication has no period), 665-668 (Article 21(1)(b): "phải được thông báo", passive), 1810-1812 (Article 62(5): the Ministry directs, the police provide, to no named recipient) (forks V17, V20).
Evidence: reading only; the encoding names the parties it took.

**R16. The alcohol threshold of Article 7(2)(đ) is in no text of the sources, and Article 17(1)(a) refers to exclusions that cannot apply to it.**
Src 225-227, 1834-1839.
Article 7(2)(đ) refers to "nồng độ cồn vượt quá mức trị số bình thường theo hướng dẫn của Bộ Y tế"; Article 65, the Ministry of Health's article, holds no such guidance, and nothing else in the sources does (row VN-10 takes it as an input).
Article 17(1)(a) refers to all of Article 7(2), but points (d), (đ), (e) and (g) exclude only damage to property (row VN-10's F7 for (đ)), which the support never pays: four of its eight references cannot produce a case.
Evidence: reading only.

## 5. Answer tables

### 5.1 Humanitarian support (Article 17(1)(a); both vintages; src 494-502)

The limit per person per accident is 150,000,000 (Article 6(1), src 188-189).

| the harm | the support | on the limit |
| --- | --- | --- |
| death | 30% of the limit | 45,000,000 |
| an injury rate of 81% or more | 30% of the limit | 45,000,000 |
| an injury rate from 31% to under 81% | 10% of the limit | 15,000,000 |
| an injury rate under 31% | none | — |

In the cases: the vehicle not identified; the vehicle not insured; the harm outside the scope of Article 7(1); an exclusion of Article 7(2) other than the injured person's own intent.
Not in a case: the insurer covers the harm; the insured vehicle's insurer excludes it for the injured person's own intent.
`nd67-vn27-art17-tests.l4` tests every case at a death and at the rates 100, 81, 80.5, 80, 31, 30.5, 30 and 0, in both vintages (234 assertions).

### 5.2 Repaying an insurer's advance (Article 17(1)(a), second paragraph; src 503-507)

| the advance was paid under | later found | the Fund owes |
| --- | --- | --- |
| Article 12(3)(a) | anything | nothing (but the insurer may ask, Article 12(3); R1) |
| Article 12(3)(b) | within the scope and not excluded | nothing |
| Article 12(3)(b) | excluded, or outside the scope | the amount advanced, up to 30% of the limit for a death or an estimated rate of 81% or more, 10% for 31% to under 81% (fork V11) |

### 5.3 The ceilings of Article 17(1) (src 510-550)

| point | head | ceiling | base | on contributions of 100,000,000,000 and a balance of 20,000,000,000 |
| --- | --- | --- | --- | --- |
| (a) | humanitarian support and repaying advances | 30% | contributions and balance | 36,000,000,000 |
| (b) | works and equipment to prevent losses and accidents | 15% | contributions and balance | 18,000,000,000 |
| (c) | propaganda and education | 17% | contributions and balance | 20,400,000,000 |
| (d) | support for the police | 10% | contributions | 10,000,000,000 |
| (đ) | rewards | 5% | contributions | 5,000,000,000 |
| (e) | the database | 10% | contributions | 10,000,000,000 |
| (g) | the ASEAN programme | 5% | contributions | 5,000,000,000 |
| (h) | managing the Fund | 8% | contributions | 8,000,000,000 |
| | total | 100% | | 112,400,000,000 |

The percentages add up to 100, on two bases: a year may spend at most the contributions plus 62% of the balance.
Point (i), in a declared emergency: points (d)-(h), 38% of a 1% contribution, from the balance (on premiums of 10,000,000,000,000: 38,000,000,000).
Each row is tested at its ceiling and one đồng above in `nd67-vn27-art17-tests.l4`.

### 5.4 Deadlines

| duty | deadline | kind of day | src |
| --- | --- | --- | --- |
| the Council decides the contribution rate (16(2)) | before 30 April: last day 29 April | calendar (fork V2) | 482-484 |
| the insurer pays 50% (16(3)(a)) | before 30 June: last day 29 June | calendar | 488-489 |
| the insurer pays the rest (16(3)(b)) | before 31 December: last day 30 December | calendar | 490-491 |
| the audited settlement report to the insurers (18(2)) | before 31 March of the next year: last day 30 March | calendar | 572-576 |
| the motor report to the Ministry (75(2)(a)) | at the latest 31 March of the next financial year | calendar | 1922 |
| the police copies of the accident documents (62(5)) | 5 working days from the investigation result (31 August 2026: 7 September, or 8 September with 2 September off) | working (fork V5) | 1810-1812 |
| the expiry notice (75(10)) | from the end date less 15 to the end date less 1 (ending 1 January 2027: 17 to 31 December 2026) | calendar (fork V4) | 1962-1963 |
| the budget to the insurers (21(1)(b), (d)); the claim documents (75(7)); payment (75(8)); copying costs (75(9)); accounts, database (75(12)-(13)) | none given | — | — |

### 5.5 Offers under Article 75(1) with Article 8(2) (a car whose Annex I premium is 437,000; src 1909-1910, 235-238, 2061)

| the offer | defects | a promotion or payment discount in some form? |
| --- | --- | --- |
| 437,000, nothing else | none | no |
| 371,450 on the vehicle's claims history (−15%) | none | no |
| 371,449 on the vehicle's claims history | adjusted by more than 15% | yes |
| 502,550 on the owner's accident history (+15%) | none | no |
| 502,551 on the owner's accident history | adjusted by more than 15% | no |
| 393,300 "for buying online" (−10%) | reduced on a ground Article 8(2) does not give | yes |
| 400,000 with no ground stated | reduced on a ground Article 8(2) does not give | yes |
| 450,000 for "peak season" | raised on a ground Article 8(2) does not give | no |
| 437,000 with a free helmet | a promotion | yes |
| 437,000 with 20,000 back on payment | a payment discount | yes |
| 437,000, voluntary cover 200,000 cheaper | none (R10) | no |

### 5.6 The two vintages compared

Run under both vintages (the vintage passed directly, and through the date of the accident: 30 June 2026 and 1 July 2026): every case of the humanitarian support, the repayments, the offers, the hotline, look-up and explanation, the expiry notice.
**No answer differs.**
An accident on 5 September 2023 is declined (`Decree 67/2023 was not yet in force on that day: …`).
The encoding found one encoding error this way: the answer functions first took the vintage without looking at it, so a date before Decree 67 was ignored rather than refused (L4 is lazy); every answer function now passes through `the answer in` v `, unamended by Decree 220/2026:`, which forces it, and the test that caught it passes.

## 6. What `check.sh` prints

```
module                                    errors satisfied  failed  refused  expected
nd67-vn27-art17-tests.l4                       0       316       0        0         0
nd67-vn27-art75.l4                             0         0       0        0         0
nd67-vn27-ch5-authorities.l4                   0         0       0        0         0
nd67-vn27-findings.l4                          0        23       0        0         0
nd67-vn27-fund-art14-16.l4                     0         0       0        0         0
nd67-vn27-fund-art17.l4                        0         0       0        0         0
nd67-vn27-fund-art18-22.l4                     0         0       0        0         0
nd67-vn27-general.l4                           0         0       0        0         0
nd67-vn27-nouns.l4                             0         0       0        0         0
nd67-vn27-tests.l4                             0       106       0        0         0
TOTAL (10 modules)                             0       445       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

`check.sh` exit 0 (run 2026-10-07, after the last change to any module). No failure is expected and none occurs; `expected_failed` is unchanged (0 for every module).
The regulative rules carry `#TRACE`s rather than assertions (a `DEONTIC` cannot be compared); 18 traces in `nd67-vn27-tests.l4`, each with the outcome its comment states (fulfilled, a breach with its reason, or the Executive Board's recourse). Their deadlines are also asserted, on both sides, through the date functions.

The harness can fail. A scratch copy of the ten modules, with three expected values in `nd67-vn27-tests.l4` altered by one unit (the last day for the first instalment 29 → 30 June; the emergency ceiling 38,000,000,000 → 38,000,000,001; a death's support 45,000,000 → 45,000,001), run through the same `check.sh` on 2026-10-07, printed:

```
nd67-vn27-tests.l4                             3       103       3        0         0
TOTAL (10 modules)                             3       442       3        0
```

with every other module as above, and exit 1: three failures, each counted as an error.

## 7. The `vnsrc check` line

The brief's command, over every `.l4` and every `.md` of this directory except `BRIEF.md`, run from this directory on 2026-10-07:

```
python3 -I tools/vnsrc.py check ../../source/raw/nd67-congbao-1017-1018.txt *.l4 $(ls *.md | grep -v '^BRIEF.md$')
vnsrc check: 715 src: lines, 536 Vietnamese runs, 0 problems
```

`tools/vnsrc.py` is the brief's copy, unchanged (sha256 `06a2605b…2453ae`, the same file as row VN-10's extended tool).

## 8. Open questions for a domain expert

1. R2 / V10: does the Fund in practice pay humanitarian support to the driver who caused a single-vehicle accident, or to an owner who had not bought the compulsory insurance?
2. R3: when the Fund repays an insurer's point (b) advance, is the advance counted against the family's humanitarian support, or recovered from them?
3. R4 / V7: is the exception for the injured person's own intent applied to accidents with uninsured or unidentified vehicles?
4. R6: what are the Council's procedures under Article 20(1)(k): who claims the support, with what documents, by when, and is there a time-bar?
5. R7: when the 30% ceiling of point (a) binds, which is paid first, support or repayments, and do repayments carry over?
6. R9 / V14: how do insurers and the Ministry draw the line between an Article 8(2) reduction and an Article 75(1) discount; is a vehicle with no claims history eligible for a reduction on its "claims history"?
7. R10 / V15: is a discount on voluntary cover sold with the compulsory cover, or an agent's rebate from commission, treated as a breach of Article 75(1)?
8. R13 / V4: do insurers read Article 75(10) as a window (the last 15 days) or as a minimum notice (at least 15 days ahead)?
9. V2: is "trước ngày 30 tháng 6" read as "by 29 June" or "by 30 June" in practice?
10. R11: what period does the Ministry hold an insurer to for paying motor compensation where the police investigation is still open?
11. R16: which Ministry of Health guidance fixes the alcohol level of Article 7(2)(đ)?
12. LAW: does Law 139/2025/QH15, which amends the Law on Insurance Business (Decree 220's preamble), change any of LAW L1-L6?
