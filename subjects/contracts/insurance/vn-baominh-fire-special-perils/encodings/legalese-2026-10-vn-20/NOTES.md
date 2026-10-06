# NOTES — Bao Minh fire and special perils rules, encoding row `legalese-2026-10-vn-20`

"Quy tắc bảo hiểm hỏa hoạn và các rủi ro đặc biệt" of Tổng Công Ty Cổ Phần Bảo Minh, the whole document (10 pages), encoded in L4 by one agent in one session (run `VN-20-20261006`, agent `enc-vn-20`, 6-7 October 2026) from `BRIEF.md`.
Status: **draft**. No domain expert has read it against the source; HG1 has not been sought.

## 0. Build and run

- `l4`: `/Users/mengwong/.local/bin/l4`, a symlink to `~/.cabal/bin/l4`, cabal store entry `jl4-0.1-0ee0100b`, sha256 `64bbcb157dbef2ef1020a6a75589313bba0a2aeeb807c921c5e65e62e9eca118`. It has no `--version`. `JL4_LIBRARY_PATH` unset.
- Command, from this directory: `L4=/Users/mengwong/.local/bin/l4 ./check.sh`.
- Totals: `TOTAL (12 modules) 0 errors, 285 satisfied, 0 failed, 0 refused`, exit 0 (section 6).
- The `.l4` files are generated. Their sources are templates kept outside the deposit (`scratchpad/vn20/tmpl/*.l4.tmpl`); `expand.py` replaces each `--@src N M` line with `tools/vnsrc.py quote` output, `genfix.py` writes `bmfire-fixtures.l4` from the nouns so its enumerations mirror the records, and `gentable.py` writes the short-period tests from source lines 251-254. No `src:` line was typed.

Modules:

| module | what it holds |
| --- | --- |
| `bmfire-nouns.l4` | DECLARE only: risks A-J, the Policy Summary, items, heads of loss, claimed losses, locations, the facts of the incident, the Insured's conduct, warranties, VI.3 changes, premium, endorsements, the claim, a pending sale |
| `bmfire-insuring-clause.l4` | the preamble (insuring clause and proviso) and Part I (DAMAGE, Fire, Terrorism) |
| `bmfire-perils.l4` | Section II, risks A to J with their own exclusions |
| `bmfire-exclusions.l4` | Section III; VIII.1(a); VIII.2 |
| `bmfire-indemnity.l4` | the measure (preamble, VII.3, VIII.1(b)), III.2(b), VII.5, VII.6, the caps, Section IV and the deductible paragraphs of E-J |
| `bmfire-conditions.l4` | IV's warranty, V, VI, VII.1-4 and 7-9, VIII.3, the closing note; the regulative rules |
| `bmfire-claim.l4` | the top-level decision: named reasons, per claim and per loss; the amount payable; `@export` |
| `bmfire-fixtures.l4` | test scaffolding (generated), and the standard case |
| `bmfire-tests-cover.l4` | layer 1: cover, every exclusion triggered and missed |
| `bmfire-tests-amount.l4` | layer 2: measure, average, contribution, marine, deductible counting, caps, the layers together |
| `bmfire-tests-conditions.l4` | layer 3: conditions, periods on both sides, the short-period scale, refusals, `#TRACE`s |
| `bmfire-findings.l4` | evidence for the findings: assertions that show what the text gives |

## 1. What is encoded and what is not

**Encoded:** everything in the document. The insuring clause and its proviso; the three definitions; risks A to J with every limb, exclusion and deductible paragraph; the general exclusions III.1-4; Section IV (deductible and its warranty); Section V; the general conditions VI.1-6, including the cancellation clause and its short-period table; the claims conditions VII.1-9; the special endorsements VIII.1-3; the closing note.
Three provisions are inert because they decide nothing: VI.1 (the three documents are one contract), VIII.2 Part 3 (a date change is not an event), and the title, blank contract number and running footer.
Nothing is out of scope.

**Inputs, never defaults.** What the Policy Summary or property list fixes (the period, the risks taken, the sums insured, the deductibles, the premium, the locations, any warranty) is a field of `The Policy Summary` or of an item, with no default. The Rules print no figure except the short-period scale and the periods (7 days, 30 days, 30 days empty, 2 months, 12 months); those are the only numbers in the rules modules.

**Where the Rules give no answer**, the encoding refuses by name: the number of days "ngay lập tức" allows (VII.1(a)), and what happens where the short-period premium exceeds the premium for the period (VI.4). No outside figure is used.

**The source** was read only from the deposited text (sha256 of the PDF `3a74940c…ae77`, verified against `subject.json`; the `.txt` rendering is `466beac8…ccf`). The document carries no date. Its running footer reads "_03.06" and the file name ends "032006"; the PDF's metadata gives a creation date of 16 September 2008. Neither the text nor the footer says what "03.06" means (fork F1).

**Outside law.** The aid, Law on Insurance Business 08/2022/QH15, was read for the provisions a fire policy touches (arts. 15-32, 43-56). Where the Law would fill a gap or conflict with the Rules, a fork is tagged `LAW:` with the aid's line number. Nothing from the Law is encoded. Whether the 2022 Law governs a contract made on this wording depends on when the contract is made (outside knowledge, unverified: that Law took effect on 1 January 2023). The aid as deposited ends at art. 130, so its transitional provisions could not be read.

## 2. Coverage table

Line numbers are of `../../source/raw/baominh-fire.txt`.
Totals: **54 rows: 51 encoded, 3 inert, 0 out-of-scope, 0 reached-and-refused, 0 deferred.** Two encoded rows (43, 46) include a named refusal for the part the Rules do not answer; row 53 contains one inert part (VIII.2 Part 3), and the running footer is inert with row 1.

| # | heading as written | English gloss | lines | disposition | where in the L4 |
| --- | --- | --- | --- | --- | --- |
| 1 | QUY TẮC BẢO HIỂM HỎA HOẠN VÀ CÁC RỦI RO ĐẶC BIỆT | title | 1-2 | inert: a title | nouns header |
| 2 | Hợp đồng bảo hiểm số | contract number, a blank | 3 | inert: a blank for the issued policy; identifies, decides nothing | nouns header |
| 3 | (preamble) | insuring clause | 6-13 | encoded (the premium limb encoded and overridden by VIII.3, fork F27) | `preamble — …` in insuring-clause; claim |
| 4 | VỚI ĐIỀU KIỆN LÀ (i) | proviso: the sum insured | 14-16 | encoded | `proviso (i) …`, `proviso — the most Bao Minh pays …` |
| 5 | VỚI ĐIỀU KIỆN LÀ (ii) | proviso: the sum insured remaining | 17-18 | encoded | `proviso (ii) …` |
| 6 | I. ĐỊNH NGHĨA: TỔN HẠI | DAMAGE | 19-21 | encoded | `I — the loss is DAMAGE`; claim reasons |
| 7 | I. ĐỊNH NGHĨA: Cháy | Fire | 22-23 | encoded | `I — Fire` |
| 8 | I. ĐỊNH NGHĨA: Khủng bố | Terrorism | 24-27 | encoded | `I — Terrorism`; `B(b) and D.1(a) — …` |
| 9 | II. RỦI RO, A. CHÁY | risk A, fire, with (a), (b)(i)-(iv), (c) | 28-37 | encoded | perils `II.A …` |
| 10 | SÉT ĐÁNH | risk A, lightning | 38-40 | encoded | `II.A — direct lightning …` |
| 11 | NỔ (a) Nồi hơi (b) Hơi đốt | risk A, domestic boiler or gas explosion | 41-46 | encoded | `II.A — explosion of a boiler or of gas …` |
| 12 | B. NỔ | risk B, explosion, (a)-(b) | 48-54 | encoded | `II.B …` |
| 13 | C. MÁY BAY | risk C, aircraft | 55-56 | encoded | `II.C …` |
| 14 | D. GÂY RỐI, ĐÌNH CÔNG, BẾ XƯỞNG | risk D, (a)-(d) | 57-66 | encoded | `II.D …` |
| 15 | D, Loại trừ 1 | D's exclusions 1(a)-(d) | 67-77 | encoded | `II.D.1(a)` … `II.D.1(d)` |
| 16 | D, Loại trừ 2 and its proviso | D's exclusions 2(a)-(d) | 78-89 | encoded | `II.D.2(a)` … `II.D.2(d)` |
| 17 | E. TỔN HẠI DO HÀNH ĐỘNG ÁC Ý | risk E, malicious damage | 92-96 | encoded | `II.E …` |
| 18 | E, deductible paragraph | E's deductible, per location | 98-100 | encoded | `how the deductible is counted under` |
| 19 | E, closing sentence | E only with D; D's exclusions except 1(c) | 101-102 | encoded | `II.E — risk E is insured only together with risk D`; claim |
| 20 | F. ĐỘNG ĐẤT HOẶC NÚI LỬA PHUN | risk F | 103-104 | encoded | `II.F …` |
| 21 | F, deductible paragraph | F's deductible, non-fire losses, per location | 105-108 | encoded | `F — the amount at the location …` |
| 22 | G. GIÔNG VÀ BÃO | risk G, (i)-(v) | 109-122 | encoded | `II.G …` |
| 23 | G, deductible paragraph | per location | 123-125 | encoded | indemnity |
| 24 | H. GIÔNG, BÃO VÀ LỤT | risk H, (i)-(v) | 126-135 | encoded | `II.H …` |
| 25 | H, deductible paragraph | per location | 136-138 | encoded | indemnity |
| 26 | I. NƯỚC TRÀN TỪ CÁC BỂ … | risk I, (i)-(ii) | 139-142 | encoded | `II.I …` |
| 27 | I, deductible paragraph | per location | 147-149 | encoded | indemnity |
| 28 | J. ĐÂM VA DO XE CỘ HOẶC SÚC VẬT | risk J and its deductible sentence | 150-155 | encoded | `II.J …`; indemnity |
| 29 | III. NHỮNG ĐIỀU KHOẢN LOẠI TRỪ ÁP DỤNG CHUNG CHO TẤT CẢ CÁC RỦI RO, 1(a) | riot unless D, war, rebellion | 156-166 | encoded | `III.1(a)(i)`-`(iii)` |
| 30 | III.1(b) | nuclear | 167-174 | encoded | `III.1(b)(i)`-`(ii)` |
| 31 | III.1(c) | electrical machinery | 175-181 | encoded | `III.1(c) …` |
| 32 | III.1(d) | pollution | 182-185 | encoded | `III.1(d) …` |
| 33 | III.2(a) | named categories of property | 186-189 | encoded | `III.2(a) …` |
| 34 | III.2(b) | marine insurance: the excess only | 190-194 | encoded (a measure) | `III.2(b) …` |
| 35 | III.3 | consequential loss, rent written back | 195-196 | encoded | `III.3 …` |
| 36 | III.4 | theft during or after a fire | 198 | encoded | `III.4 …` |
| 37 | IV. MỨC MIỄN THƯỜNG | the deductible, after average | 199-202 | encoded | `IV — the deductible …`; `the amount payable on the covered losses` |
| 38 | IV, the warranty | not to insure the deductible | 203-204 | encoded | `IV — the Insured must not insure the deductible`; VI.5 |
| 39 | V. QUY ĐỊNH CHUNG, THAY ĐỔI QUYỀN LỢI BẢO HIỂM | change of interest on a pending sale | 205-212 | encoded | `V — the buyer takes the benefit …` |
| 40 | VI. ĐIỀU KIỆN CHUNG, 1. Sự đồng nhất | one contract | 213-219 | inert: a rule of construction with nothing to decide; applied in reading the Summary as part of the policy (fork F11) | conditions, comment |
| 41 | 2. Hợp đồng bảo hiểm bị vô hiệu | void policy | 220-223 | encoded | `VI.2 …` |
| 42 | 3. Thay đổi và di chuyển | alteration and removal | 224-237 | encoded | `VI.3 …` |
| 43 | 4. Hủy bỏ hợp đồng bảo hiểm, and Tỷ lệ phí ngắn hạn | cancellation; the short-period scale | 240-254 | encoded (with a named refusal) | `VI.4 …` |
| 44 | 5. Đoan kết | warranties | 255-261 | encoded | `VI.5 …` |
| 45 | 6. Đề phòng tổn thất | loss prevention | 262-265 | encoded | `VI.6 …` |
| 46 | VII. ĐIỀU KIỆN KHIẾU NẠI ĐÒI BỒI THƯỜNG, 1. Trách nhiệm của người được bảo hiểm | the Insured's duties after a loss | 266-288 | encoded (with a named refusal) | `VII.1 …` |
| 47 | 2. Mất quyền lợi | forfeiture; the twelve-month bars | 289-300 | encoded | `VII.2(a)`, `VII.2(b)…` |
| 48 | 3. Phục hồi tài sản | reinstatement | 301-319 | encoded | `VII.3 …` (indemnity and conditions) |
| 49 | 4. Quyền của Bảo Minh khi có tổn thất xảy ra | Bao Minh's rights; no abandonment | 320-329 | encoded | `VII.4 …` |
| 50 | 5. Luật tỷ lệ (bảo hiểm dưới giá trị) | average | 330-334 | encoded | `VII.5 …` |
| 51 | 6. Đóng góp bồi thường tổn thất | contribution | 339-347 | encoded | `VII.6 …` |
| 52 | 7. Thế quyền; 8. Trọng tài; 9. Thông báo và giao dịch bằng văn bản | subrogation; arbitration; notices in writing | 348-370 | encoded | `VII.7 …`, `VII.8 …`, `VII.9 …` |
| 53 | VIII. SỬA ĐỔI BỔ SUNG ĐẶC BIỆT, 1. Dữ liệu điện tử; 2. Nhận biết ngày điện tử | electronic data; date recognition | 371-443 | encoded, except VIII.2 Part 3 inert: it makes no event of a date change and decides nothing | `VIII.1(a)(i)`, `VIII.1(b)`, `VIII.2 Part 1`, `Part 2` |
| 54 | 3. Cam kết thanh toán phí; GHI CHÚ QUAN TRỌNG | premium payment warranty; closing note on disclosure | 446-494 | encoded | `VIII.3 …`; `closing note — the Insured must disclose` |

The running footer on every page ("Bảo Minh – BH Hỏa hoạn và các rủi ro đặc biệt_03.06", src 47, 97, 146, 197, 248, 297, 351, 405, 458, 499) is inert and counted with row 1.

## 3. Fork register

Each fork: the question, the readings, the one taken and why. `LAW:` marks a fork where the aid would fill or override the Rules, with its line; nothing from the Law is encoded. Where a reading was taken because it favours the Insured, that is the Law's own rule for an unclear term (art. 24, aid lines 588-591).

| # | where (src) | the question | readings | taken, and why |
| --- | --- | --- | --- | --- |
| F1 | title, footer (1-3, 47) | Is the document dated? | (i) March 2006 (footer "_03.06", file name "032006"); (ii) a version number "03.06"; (iii) undated | **(iii)**: the text states no date; the vintage is "as published on 2026-10-06" (BRIEF). PDF metadata says created 16 September 2008, which fits neither reading closely. |
| F2 | all | Which law governs? | (i) Law 08/2022/QH15; (ii) the law in force when the wording was written | **not decided**: nothing from the Law is encoded; conflicts are recorded as `LAW:` forks. |
| F3 | I, Cháy (22-23) | "điều kiện bất thường", "nguồn lửa chuyên dùng trong sinh hoạt" | (i) facts for the adjuster; (ii) categories the encoding defines | **(i)**: inputs. The Rules give no test. |
| F4 | II.A NỔ (41-46) | Does "được sử dụng cho mục đích sinh hoạt" qualify the boiler as well as the gas? | (i) both; (ii) gas only | **(i)**: the qualifier stands on its own line under both limbs. |
| F5 | II.A(b)(i)-(iii) (31-34) | Whose fermentation, drying or burning by order? | (i) the item it happened to; (ii) all DAMAGE from a fire it started | **(i)**: "tài sản" names the property, the market wording reads so, and it is the narrower exclusion (art. 24). |
| F6 | II.E (101-102) | "các loại trừ cho rủi ro này … trừ điểm 1(c)": which exclusions? | (i) D's; (ii) E's own | **(i)**: only D's list has a point 1(c). |
| F7 | II.I(ii) (142) | "TỔN HẠI của ngôi nhà bị bỏ trống": contents? how long empty? | (i) the building only, any time empty; (ii) contents too; (iii) 30 days as in VI.3(b) | **(i)**: "của ngôi nhà" (of the building); no period is stated (finding X8). |
| F8 | II.J (150-155) | J's only sentence names the Insured's own vehicles in a deductible sentence. | (i) a deductible sentence: own vehicles covered, with the deductible; (ii) the market exclusion of own vehicles | **(i)**: the words are about the deductible; no exclusion is stated (finding X1). |
| F9 | II.D(c), D.1(c) (63-64, 72-75) | D.1(c) carves out demonstrators ("biểu tình"); D(c) names only strikers and locked-out workers. | (i) as written: demonstrators' wilful acts are not excluded, and are within D only through limb (a); (ii) demonstrators within (c) | **(i)**. |
| F10 | III.1(d) (182) | "(trừ khi đã bị loại trừ)" after the main limb | (i) "unless otherwise excluded", adding nothing; (ii) the exclusion applies only where pollution is not excluded elsewhere | **(i)**: the market wording's "unless otherwise excluded"; either way no other exclusion is displaced. |
| F11 | III.2(a) (186-189) | "trừ khi được ghi nhận là được bảo hiểm": does an item in a wider class (contents) count as recorded? | (i) only if specifically recorded; (ii) any item the Summary covers | **(i)**: otherwise the exclusion could never apply to insured property (VI.1 makes the Summary part of the policy). |
| F12 | preamble, III.3, VII.5 (12, 195-196, 331) | Which heads are consequential; is rent averaged? | (i) D.2(a)-(b) heads are consequential; rent insured by the Summary, no average; (ii) other splits | **(i)**: the Rules name those heads; average speaks of property with an actual value. |
| F13 | proviso (ii) (17-18) | Remaining sum insured per item or for the policy? | (i) both; (ii) item; (iii) policy | **(i)**: (i) names both caps; both are applied. |
| F14 | VIII.1(a)(i) (376-380) | Does the exclusion reach physical damage to tangible property caused by a data matter? | (i) no: its objects are the data and loss of use, functionality and cost; (ii) yes, (ii) is a write-back | **(i)**: the words; (ii) is then declaratory. On (ii), a virus that opens a valve and floods the store would be excluded. |
| F15 | VIII.2 Part 1 (428-432) | Mapping the write-back's perils to facts | — | Matched: fire, lightning, explosion, aircraft, vehicle, storm, D's acts, riot/commotion/strike, malicious act, earthquake, tsunami (sea flood from earthquake). Not matched: freezing (it shares a field with subsidence and landslip), hail, whirlwind, falling objects (no fields). |
| F16 | VII.3 (315-319) | The measure where local rules prevent reinstatement | (i) the cost of a lawful repair to the former condition, supplied as the restoring cost; (ii) the value at the time of loss | **(i)**: the words. |
| F17 | IV (199-202) | The deductible's form | (i) an amount per risk in the Summary; (ii) a percentage; (iii) one figure for all risks | **(i)**: the caller converts (ii) and repeats (iii). |
| F18 | IV (201-202) and the measures | Order of the steps | (i) measure, marine excess, average, contribution, item cap, deductible, claim cap; (ii) others | **(i)**: IV fixes the deductible after all conditions, average included; the rest follows a loss adjuster's order. Average-then-contribution is finding X5. |
| F19 | VII.6 (342-343) | "phân bổ theo tỉ lệ": the ratio | (i) sums insured; (ii) independent liability | **(i)**. `LAW:` art. 49(2), aid lines 969-973, apportions double insurance by sums insured. |
| F20 | VII.1(a) (270) | "ngay lập tức" in days | (i) a fact; (ii) a number of days | **(i)**: a finding of fact; asking for the number refuses by name. `LAW:` art. 19(3), aid lines 441-444: a late notice caused by force majeure cannot be relied on. |
| F21 | preamble (11), VII.1(b) (275) | Are the period's ends inside it? From when do the 30 days run? | (i) both ends inside; from the day of the DAMAGE (the "sự cố"); (ii) other anchors | **(i)**: VII.1 opens "Nếu có bất kỳ sự cố nào". |
| F22 | 233, 275, 296, 361 | Kind of day and month | (i) calendar days, counted as days elapsed; calendar months by `add months`, clamped; (ii) working days | **(i)**: the Rules say "ngày" and "tháng" only. |
| F23 | VI.4 (241-244) | When does Bao Minh's cancellation take effect; how is the refund counted? | (i) 7 days after the notice is issued; refund pro rata by days from the notice day; (ii) from receipt | **(i)**: the refund is "tính từ ngày ra thông báo hủy bỏ" (from the day the notice is issued) (finding X13). |
| F24 | VI.4 table (251-254) | 3 and 6 months fall in two rows each | (i) to the lower row; (ii) to the higher | **(i)**: "Trên 9 tháng" (more than 9) shows a row reaches up to its upper figure, and the lower rate favours the Insured (finding X12). |
| F25 | VI.5 (258-261) | "nếu có TỔN HẠI xảy ra trong thời gian tái tục hợp đồng" | (i) literally, renewal periods only; (ii) any period (a slip) | **(i)**: as written (finding X6). |
| F26 | VI.3 (225-226) | "đối với những tài sản bị tổn thất": which property? | (i) the changes listed on a claim concern the property claimed; (ii) per item | **(i)**: a simplification; a change affecting other property is not listed. |
| F27 | preamble (11), VIII.3 (446-484) | Must the premium be paid before the DAMAGE? | (i) yes, the preamble; (ii) clause 1 alone: no liability unless paid in 30 days; (iii) clause 1 subject to clause 2: unpaid premium cancels cover after the deadline, DAMAGE before it covered | **(iii)**: VIII.3 overrides "anything to the contrary", and clause 1 is "subject to … clause 2". `LAW:` art. 27(1)(c), aid lines 652-657, says the same of property insurance terminated for unpaid premium (finding X9). |
| F28 | VIII.3.1 (453-470) | "ngày chấp nhận bảo hiểm"; the first instalment | (i) an input date; the first instalment's deadline is 30 days from it, whatever date the schedule gives it; (ii) its scheduled date | **(i)**: (b)(i) says so. |
| F29 | preamble (6-8) | Which conditions are conditions precedent, and is causation needed? | (i) every duty-condition of VI and VII, no causation; (ii) only those that say so | **(i)**: "các điều kiện quy định trong Quy tắc này … được coi là điều kiện tiên quyết". `LAW:` art. 46(1)-(2), aid lines 917-932: for late notice an insurer may only reduce by the damage it suffered; art. 54(1)(b), aid lines 1034-1037: refusal to transfer subrogation rights allows only a deduction by fault (finding X14). |
| F30 | V (209-212) | "nếu điều đó không làm phương hại …" | (i) a judgment, an input; (ii) a test the encoding defines | **(i)**: the Rules give no criteria. |
| F31 | VI.2 (220-223) | Intent; materiality; who decides | (i) no intent; "quan trọng" qualifies non-disclosure only; "Bảo Minh cho là vô hiệu" lets Bao Minh treat the policy as void; (ii) intent or materiality required | **(i)**: the words. `LAW:` art. 22(2), aid lines 543-553, gives a right to rescind only for intentional misinformation, and art. 25, aid lines 592-618, lists the grounds of voidness (finding X15). |
| F32 | preamble (12-13), II.E (95-96), III.4 (198) | Is a loss by theft caused by a risk? | (i) no risk names theft: out under every risk, with E and III.4 saying so for E and A; (ii) theft following a peril is caused by it | **(i)**: III.4 is then needed only for A, which is what it addresses. |
| F33 | VI.4 (241-247) | The refund on the Insured's termination | (i) the balance after the short-period premium is returned (implied by "giữ lại"); (ii) nothing is returned | **(i)**; where the short-period premium exceeds the premium for the period, the Rules do not say whether the Insured owes the difference: refused by name. No period is given for either refund. |
| F34 | VIII.3.1(c) (476-478) | "khi thời hạn thanh toán phí bảo hiểm dưới 30 ngày" | (i) literally, an agreed payment term under 30 days; (ii) a period of insurance under 30 days | **(i)**: as written (finding X17). |
| F35 | VII.1(b) (275) | A period Bao Minh allows that is shorter than 30 days | (i) ignored, "dài hơn" (longer) only; (ii) applied | **(i)**. |
| F36 | II.D (57) and III.1(a) (160, 164) | D's and III's words for riot and strike differ | (i) kept apart, as separate facts the caller states; (ii) treated as synonyms | **(i)**: the source's words; which word fits an event is the adjuster's call (finding X3). |
| F37 | VII.1(b) (275), VII.2(b) (294-300) | `LAW:` the period to claim and to be paid | — | **not encoded**: art. 30(1), aid lines 707-710, gives one year from the insured event to submit a claim file; art. 31(1), aid lines 719-724, requires payment within 15 days of a complete file where the contract states no period, which these Rules do not (findings X4, X19). |
| F38 | VI.4 (240-244) | `LAW:` Bao Minh's cancellation without cause | — | **not encoded**: art. 26, aid lines 623-635, lists the cases in which either party may terminate unilaterally; VI.4 gives Bao Minh a power with no ground (finding X16). |

Where else it was looked for and none found: the definitions of "ngôi nhà", "địa điểm được bảo hiểm" and "tài sản di động" are not given and were read in their ordinary sense; the arithmetic of the scale was checked (30, 60, 90, 100 rise and never exceed 100).

## 4. Findings

A finding is a defect of the instrument as written. Evidence is an assertion in `bmfire-findings.l4` (all pass: they show what the text gives) or the words "reading only".

| # | finding | source lines | minimal scenario | evidence |
| --- | --- | --- | --- | --- |
| X1 | **Risk J covers the Insured's own vehicles and animals.** Its only sentence about them is a deductible sentence; the market exclusion of own vehicles is absent. | 150-155 | The Insured's own lorry reverses into its warehouse: 200 m damage, deductible 10 m. | `the reasons` … EMPTY; `the amount payable` … 190,000,000 (`X1`) |
| X2 | **Terrorism by a person acting alone, or for a government, is not excluded** from B or D. The definition covers both; the exclusions add "nhân danh hoặc có liên quan đến bất kỳ tổ chức nào". | 24-27, 53-54, 69-70 | A lone bomber with a political aim destroys the building. | `I — Terrorism` holds; B and D claims have no reason (`X2`) |
| X3 | **Riot cover under D is illusory on a literal reading.** III.1(a)(i) gives "Nổi loạn" back where D is insured; III.1(a)(iii) excludes "Nổi loạn" and "bạo động" with no carve-back. D's own words ("GÂY RỐI", "ĐÌNH CÔNG") are not III's. | 57, 160-166 | A riot damages the shop; D is insured. Called "civil commotion": paid. Called "Nổi loạn": excluded. | `X3`: three assertions |
| X4 | **The 30-day claim period is far shorter than the Law's one year** for submitting a claim file; a late particular takes the whole claim away as a condition precedent. | 275-280, 6-8 | Particulars delivered on day 31. | `bmfire-tests-conditions.l4`: 2 July gives `VII.1(b)`; reading only for the Law (aid 707-710) |
| X5 | **Average and contribution reduce twice.** Average is measured against this policy's sum insured alone, then contribution takes a rateable share again. | 330-334, 339-347 | Value 1,000; insured 600 here and 600 elsewhere; damage 200. Each insurer pays 60: 120 in all. | `over-insured with two policies` = 60,000,000 (`X5`) |
| X6 | **A warranty bites only in a renewal period.** Non-compliance takes away a claim "nếu có TỔN HẠI xảy ra trong thời gian tái tục hợp đồng". | 255-261, 203-204 | First-year policy; sprinkler warranty broken and the deductible insured; fire. | warranty breach recorded, `the amount payable` 200,000,000 (`X6`) |
| X7 | **The twelve months to sue run while the arbitration on the amount is still being formed.** Either bar suffices; the arbitration has two two-month appointment periods and no period for the umpire or the award. | 294-300, 357-367 | Rejection and request to arbitrate on 15 March 2026; no award; 16 March 2027. | benefit lost (`X7`) |
| X8 | **An empty building's water damage is excluded at once; the policy ends only after 30 days empty.** | 142, 233 | Building empty since 31 May; pipe bursts 1 June. | VI.3 not triggered, I(ii) excludes (`X8`) |
| X9 | **Three answers to whether the premium must be paid first:** the preamble (yes), VIII.3.1 alone (no liability unless paid in 30 days), VIII.3.2 (liable for the period in force). | 11, 446-484 | Fire 15 January; premium paid 20 January, or never. | preamble limb FALSE, clause-1 reading FALSE, encoded answer pays 200,000,000 (`X9`) |
| X10 | **The electrical exclusion takes out lightning damage to the machine struck**, "do bất kỳ nguyên nhân nào (kể cả sét đánh)", although A covers direct lightning. | 38-40, 175-181 | Direct lightning burns out the printing press. | reason `III.1(c)` (`X10`) |
| X11 | **The date-change write-back omits flood, water from tanks, sprinklers, animals and subsidence**, and lists perils the policy does not insure (hail, whirlwind, falling objects, the weight of snow) and freezing, which G and H exclude. | 428-432, 116, 128 | A date fault lets a river flood the site under H. | flood excluded, storm not (`X11`) |
| X12 | **The short-period scale claims 3 and 6 months twice** ("Đến 3 tháng" and "Từ 3 đến 6 tháng"). | 251-253 | Termination effective exactly 3 months in: 30% or 60%? | 30% encoded (`X12`); the other row is a reading |
| X13 | **The refund on Bao Minh's cancellation counts from the notice day, though cover runs 7 more days.** | 241-244 | Notice 2 July; cover to 9 July; refund for 182 of 364 days. | 6,000,000 and 9 July (`X13`) |
| X14 | **Any condition defeats any claim, connected to the loss or not**, because the preamble makes the conditions conditions precedent and VI.6 is open-ended ("mọi biện pháp thích hợp"). | 6-8, 262-265 | Storm takes the roof; the gutters had been neglected. | `the amount payable` 0 (`X14`); `LAW:` art. 46 for notice |
| X15 | **An innocent misstatement voids the policy** at Bao Minh's option: VI.2 has no intent and, for misstatement, no materiality. | 220-223 | A wrong construction year, given in good faith. | reading only (`LAW:` art. 22(2), aid 543-553) |
| X16 | **Bao Minh may cancel on 7 days' notice for any reason**, by a registered letter to the last known address, without proof of receipt. | 240-244 | Cancellation sent as a typhoon approaches. | reading only (`LAW:` art. 26, aid 623-635) |
| X17 | **VIII.3.1(c) lengthens the time to pay where the agreed term is short**: an agreed 15-day term gives until the end of the period, a 30-day default gives 30 days. | 476-478 | Payment term 15 days agreed. | deadline 31 December vs 31 January (`X17`) |
| X18 | **After winning an arbitration on the amount the Insured must still sue within 12 months or lose the benefit.** | 298-300 | Award for the Insured; Bao Minh does not pay; no suit for a year. | reading only |
| X19 | **Bao Minh has no period to assess or pay, and a choice to reinstate with no criteria**; the Insured's periods are "at once", 30 days and 12 months. | 9-10, 301-314 | Any claim. | reading only (`LAW:` art. 31(1), aid 719-724) |

The three most likely to matter to a policyholder: **X3** (riot cover taken back), **X14** (any condition defeats any claim), **X9** (when cover starts against the premium).

## 5. Answer table

The Rules print one table, the short-period scale (src 249-254). With an annual premium of 12,000,000 and a period from 1 January 2026:

| termination effective | row (as written) | rate of annual premium | kept | returned (premium 12,000,000) |
| --- | --- | --- | --- | --- |
| up to 1 April 2026 | Đến 3 tháng | 30% | 3,600,000 | 8,400,000 |
| 2 April to 1 July | Từ 3 đến 6 tháng | 60% | 7,200,000 | 4,800,000 |
| 2 July to 1 October | Từ 6 đến 9 tháng | 90% | 10,800,000 | 1,200,000 |
| from 2 October | Trên 9 tháng | 100% | 12,000,000 | 0 |

How the deductible is counted, by risk (IV and the closing paragraphs of E-J):

| risk | counted | src |
| --- | --- | --- |
| A, B, C, D | once for each loss (Section IV) | 199-202 |
| E | for each loss at each separate location | 98-100 |
| F | for each loss at each location, on losses not caused by fire | 105-108 |
| G, H, I | for each and every loss at the different locations | 123-125, 136-138, 147-149 |
| J | for each loss caused by a vehicle or animal of the Insured, the occupier, or their employees (F8) | 151-155 |

## 6. What `check.sh` prints

Run on 2026-10-07 from this directory with `L4=/Users/mengwong/.local/bin/l4 ./check.sh`, `JL4_LIBRARY_PATH` unset; the machine was shared with about twenty other encoders' runs (load average near 190), which made the run slow but does not change its result:

```
module                                    errors satisfied  failed  refused  expected
bmfire-claim.l4                                0         0       0        0         0
bmfire-conditions.l4                           0         0       0        0         0
bmfire-exclusions.l4                           0         0       0        0         0
bmfire-findings.l4                             0        28       0        0         0
bmfire-fixtures.l4                             0         0       0        0         0
bmfire-indemnity.l4                            0         0       0        0         0
bmfire-insuring-clause.l4                      0         0       0        0         0
bmfire-nouns.l4                                0         0       0        0         0
bmfire-perils.l4                               0         0       0        0         0
bmfire-tests-amount.l4                         0        40       0        0         0
bmfire-tests-conditions.l4                     0        93       0        0         0
bmfire-tests-cover.l4                          0       124       0        0         0
TOTAL (12 modules)                             0       285       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

`check.sh` exit 0. No failing assertion is expected and none occurs; the rule modules carry no assertions of their own.
The 28 assertions in `bmfire-findings.l4` pass because they state what the text gives; each is evidence for a finding, not a sign the instrument is sound.
The conditions module also runs eleven `#TRACE`s (no assertions); their results were read and match the comments beside them (VII.1 performed: `FULFILLED`; written claim on day 31: `BREACH … VII.1(b)`; premium on day 30: `FULFILLED`, none by day 31: `BREACH … VIII.3.2`; deductible insured on day 100: `BREACH … Section IV`; Bao Minh's notice: the refund duty stands; arbitration: the Insured may appoint a sole arbitrator; the disclosure and loss-prevention duties stand).
Every run also prints two Warnings that differing copies of `prelude` and `daydate` exist under `~/.local/share/jl4/libraries/`; the binary uses its embedded copies, and the warnings are not errors.
Not done: a deliberate-failure run to show the harness can fail, and the independent test pass (skill step 8); the brief is one session with no sub-agents.

## 7. The `vnsrc check` line

The gate, over every `.l4` and every `.md` in this directory except `BRIEF.md` (the lead's file), run last on 2026-10-07:

```
vnsrc check: 489 src: lines, 494 Vietnamese runs, 0 problems
```

The brief's literal command, `python3 -I tools/vnsrc.py check ../../source/raw/baominh-fire.txt *.l4 *.md`, which also reads `BRIEF.md`, prints `vnsrc check: 489 src: lines, 503 Vietnamese runs, 0 problems`. The line above is the gate.

## 8. Open questions for a domain expert

1. X3 and F36: in Vietnamese claims practice, how are "Nổi loạn", "bạo động", "GÂY RỐI" and "bạo động dân sự" told apart? Is a street riot "Nổi loạn"?
2. F8 and X1: is impact by the Insured's own vehicle covered under J in Bao Minh's practice, or is the market exclusion read in?
3. F25 and X6: is "thời gian tái tục hợp đồng" in VI.5 understood as any period of the contract?
4. F27 and X9: when does Bao Minh treat cover as attaching where the premium is paid within 30 days?
5. F29 and X14: does Bao Minh rely on unrelated breaches of conditions to decline, and how do courts read the preamble's "điều kiện tiên quyết" against art. 46 of the Law?
6. F1: what does "_03.06" denote, and is a later version of these Rules in use?
7. F34 and X17: is VIII.3.1(c) a translation of "where the period of insurance is less than 30 days"?
8. Is the deductible stated in practice per risk, per location, or as a percentage of the loss?
