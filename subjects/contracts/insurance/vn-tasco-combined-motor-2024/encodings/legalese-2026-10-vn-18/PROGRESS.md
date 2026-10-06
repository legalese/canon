# PROGRESS — row VN-18 (enc-vn-18)

State on disk, in case the session is killed. Read this and BRIEF.md first, then re-run `L4=/Users/mengwong/.local/bin/l4 ./check.sh`.

## How the modules are made

Every `.l4` here is GENERATED from a template in the scratch directory
`/Users/mengwong/.claude/tmp/claude-502/-Users-mengwong-src-legalese-l4-pipeline/9efa11ae-1dd6-427f-9147-a0be56160d6d/scratchpad/vn18/tmpl/*.l4.tmpl`
by `python3 -I scratchpad/vn18/expand.py DEPOSIT TEMPLATE...`, which replaces each `{{Q N M}}` line with the output of `tools/vnsrc.py quote` for lines N-M.
Edit the template, never the `.l4`, then re-expand.
If the scratch directory is lost, the `.l4` files are the source: edit them directly.

## Done (typecheck clean)

- tasco-nouns.l4 (all DECLAREs, outcome types at the end)
- tasco-p0-definitions.l4 (decision page, opening paragraph, definitions 1-19)
- tasco-ch1-contract.l4 (Điều 1, 2, 3, 6, 12)
- tasco-ch1-duties.l4 (Điều 4, 5, 7)
- tasco-ch1-claims.l4 (Điều 8, 9, 10)
- tasco-ch1-exclusions.l4 (Điều 11, 13)
- tasco-ch2-physical-damage.l4 (Điều 14-19, depreciation table)
- tasco-ch3-personal-accident.l4 (Điều 20-25)
- tasco-ch4-goods-liability.l4 (Điều 26-29)
- tasco-ch5-voluntary-liability.l4 (Điều 30-34)

- tasco-ch6-additional-clauses.l4 (Chương VI, BS01-BS15, Điều 35, 36) — done 2026-10-07
- tasco-claims.l4 (assembly of the Chương II answer with the BS clauses) — done 2026-10-07

## Remaining, in order

3. tests modules (expected values from the source; Điều 35 rows generated from OCR lines 1427-1432; depreciation rows from the page-read lines)
4. findings demonstrations (#ASSERT showing the literal answer)
5. NOTES.md, GLOSSARY.md, COMPARABLES.md, encoding.json, SOURCE-LICENSE.md
6. vnsrc gate: every .l4 and .md EXCEPT BRIEF.md, must end `0 problems`

## Pages viewed as images

All 25 pages at 100 dpi (scratch `pages/p-NN.png`). Zoomed: p.1 (number and date, 300 dpi), p.11 (150 dpi, Điều 11-13 figures), p.15 table (200 dpi), p.16 (500.000), p.18 (0,5%, 1.000.000), p.21 (BS03 3.000.000), p.22 (BS04 02/03 vụ, 1.000.000), p.23 (BS07 100%, 500.000, 30 ngày, 04 ngày), p.24 (BS15 heading), p.25 (BS15 3.000.000, Điều 35 table).

## OCR corrections found so far (page: OCR -> page)

- p.1 l.4: "Sề: 3⁄2024/QĐ-BH Tasco Hà Nội, ngày9,Ù tháng" -> "Số: 53/2024/QĐ-BH Tasco", "ngày 22 tháng 05 năm 2024" (handwritten) [page-read]
- p.3 l.114: "18;" -> "19." (definition 19)
- p.9 l.530: "(chương II)" -> "(chương III)"; l.537 "M)" -> "IV)"
- p.10 l.596: "LẺ" -> "1."; l.665 "TẾ." -> "11."; l.619-622 numerals "¡", "1iI" -> i, iii
- p.11 l.676: "+" -> "1."; l.679 "ñ." -> "a."; l.689 "L4" -> "c."
- p.13 l.787: "-" -> "3." (15.3)
- p.14 l.800: "ri" -> "7."; l.806 "ẩ." -> "8."; l.811 "9," -> "9."; l.829 "ch" -> "3."; l.831 "hấng" -> "hãng"
- p.15 l.869-905: table scrambled; every cell read from the page (see ch2 module page-read lines); l.873 "linh doanh" -> "kinh doanh"
- p.16 l.972: "Z" -> "2."
- p.17 l.1002 "1L" -> "1."; l.1005 "xà" -> "2."; l.1009 "&" -> "3."
- p.18 l.1040 "k" -> "1."; l.1045 "5%" -> "3."; l.1049 "VÀ" -> "5."; l.1058 "k" -> "1."; l.1067 "phóng xa" -> "phóng xạ" [page-read]
- p.21 l.1151 "CHƯƠNG VỊ" -> "CHƯƠNG VI"; l.1173 "%" -> "1."; l.1179 "%" -> "2."; l.1198 "LỆ" -> "a."
- p.25 l.1426 "lu CÓ KHÁU TRỪ" -> "STT | MỨC MIỄN THƯỜNG CÓ KHẤU TRỪ"

## Forks so far (numbering used in module comments)

F1 signing date = 22 May 2024; F2 months of use = difference of months; F3 period of use ends at the contract month; F4 definition 15 "và/hoặc" = OR; F5 when "paid in full" is tested (day by day); F6 pro rata by days; F7 bare "ngày" = calendar day; F8 period inclusive at both ends; F9 "ngay" has no number; F10 Điều 6.2 prevails over 6.1 on a late notice; F11 which Điều 3 limb 6.2 refunds by; F12 when a file Tasco cannot verify is complete; F13 Điều 9.1 share applied to what Tasco would pay alone; F14 "kinh doanh" (Điều 18) = "KDVT" (Điều 35); F15 10.1 last day by add years + obstacle days; F16 11.4 drug limb also property-only; F17 overload "hoặc" = larger excess; F18 13.1.1(a) conjunction; F19 Điều 11 not applied to Chương V; F20 "sudden, unforeseen" applied to all 14.1 cases but natural catastrophe; F21 consumables "first year" = 12 months of use or less; F22 deductible compared with the amount after depreciation and ratio; F23 Điều 13 reduction not applied to 14.2 costs; F24 BS deductible replaces Điều 19's; F25 ratio of 18.1.2(a) applied to the depreciated cost; F26 accident sum insured per person; F27 table percentage applied to the sum insured; F28 child under 7 = half of an adult's benefit; F29 child and overcrowding adjustments both apply; F30 goods: deductible then reduction then cap; F31 Chương V bodily = lesser of 34.1 and Điều 32; F32 34.2 property reading; F33 33.3 without 11.1's spared causes; F34 BS07 day of loss = day 1; F35 BS15 standalone; F36 Điều 35 deductible on partial losses only.

## Findings so far (X numbers used in comments)

X1 Điều 11.4 alcohol/drugs excludes only damage to property: a drunk driver's own injury under Chương III is not excluded.
X2 opening paragraph calls the buyer "chủ xe"; definition 5 defines "Chủ xe" as owner.
X3 "Tổn thất" defined as sudden damage, yet 15.1 excludes wear and tear as a "tổn thất".
X4 definition 19 is circular.
X5 Điều 3.2 Tasco-termination refund has no insured-event exception.
X6 Điều 6.1 and 6.2 conflict on a late notice where the old owner agreed.
X7 Điều 6 silent where notice was in time and the old owner neither agreed nor asked to end it.
X8 Điều 4.1.6 refers to "khoản 2, Điều 6" (transfer); duties are Điều 5.2.
X9 Điều 4.2.6 refers to "Điều 7" for the claim file; it is Điều 8.
X10 Điều 8: "one or more" documents, Tasco's choice; the 15-day payment clock runs from a "complete" file.
X11 10.1 one-year bar voids "mọi khiếu nại"; 10.2 allows a complaint 90 days after the decision, possibly after the one-year mark.
X13 13.1.2(a): Tasco's 3-working-day opinion has no consequence when missed.
X14 11.1 has two exclusions under one number.
X15 13.1.2/13.1.3 rates left to Tasco within wide ranges, no criteria.
X16 18.2.1 total-loss limbs part at exactly 75%.
X17 Điều 24 does not name permanent partial disability.
X18 27.2 exception for theft with the whole vehicle gives no cover; Điều 26 does not name theft.
X19 Điều 32 vs 34.1 formula.
To add with Chương VI: BS03 does not buy back the electric-motor limb of 15.2; BS04 has no count limit for contracts under 12 months; BS09 benefit sites narrower than eligibility sites; BS15 deductible heavier than Điều 19; Chương VI refers to "Quy tắc bảo hiểm vật chất xe ô tô" and BS14 to "Quy tắc bảo hiểm tự nguyện xe ôtô", documents not this one.

## Last check

No check.sh run yet (no tests). vnsrc over *.l4: 724 src lines, 2 problems (being fixed: "phóng xạ" line in ch4 lacks the page-read marker; a comment in ch5 naming two articles). [page-read]

## 2026-10-07 progress

- Tests are generated by `scratchpad/vn18/gen.py DEPOSIT`, which runs `scratchpad/vn18/tests/t*.py`; fixtures are full literals checked against the record declarations.
- tasco-tests-fixtures.l4, tasco-tests-ch1.l4 (119 asserts), tasco-tests-ch2.l4 (111 asserts) written; ch2 ran: 111 satisfied, 0 errors. ch1 had one fixture error (fixed: the combined-reductions case lacked the move-without-consent fact), rerun pending.
- Type checking is slow when a module imports many others (the assembly 73 s, a module importing all 270 s): test modules import only what they test.
- 2026-10-07: tests ch1 120/120, ch2 111/111, ch3-5 45/45 satisfied (before the finding additions); ch6-claims written (104 asserts), running. Finding demonstrations added to ch1 (X11, X13), ch3-5 (X19), ch6 (X24). Next: NOTES.md, GLOSSARY.md, COMPARABLES.md, encoding.json, SOURCE-LICENSE.md, then check.sh and the vnsrc gate.
- 2026-10-07: all four test modules ran clean one by one: ch1 123/123, ch2 111/111, ch3-5 46/46, ch6-claims 104/104 satisfied, 0 errors. NOTES.md, GLOSSARY.md, COMPARABLES.md, encoding.json, SOURCE-LICENSE.md written. Remaining: the full check.sh run (running), then fill NOTES §0/§6/§7 and encoding.json self_check placeholders (@@...@@), run the vnsrc gate, send the final report.
- 2026-10-07 DONE: check.sh TOTAL (17 modules) 0 errors, 384 satisfied, 0 failed, 0 refused, exit 0. vnsrc gate (all .l4 and .md except BRIEF.md): 908 src lines, 1272 Vietnamese runs, 0 problems. All deliverables written. Page images deleted from scratch (re-render with pdftoppm if needed).
