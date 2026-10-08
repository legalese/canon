# Encoding brief: Decree 67/2023/NĐ-CP — compulsory motor vehicle owners' civil liability insurance (Chapter II), with Decree 220/2026/NĐ-CP, in L4

Row VN-10, row id `legalese-2026-10-vn-10`, run id `VN-10-20261006`, encoder `enc-vn-10` (one session, no sub-agents).
This brief is the whole specification. Read it fully before you open a source. It restates the lead's task in the template of `/Users/mengwong/src/legalese/l4-ide/skills/encoding-a-subject/assets/brief-template.md`.

## What this is for

A prototype of an insurance analytics product for Vietnam: Vietnamese consumer and business insurance documents found on the open web are encoded into L4, a language for rules as code, so that a person can ask what a policy covers, what it would pay, and where it has gaps, with every answer traceable to a clause. The encodings are deposited in a public repository (`legalese/commons`).
The deliverable is a faithful, reviewable, bilingual (Vietnamese source, English encoding) formalisation, plus an honest account of what is ambiguous or defective in the source.

## Where everything is

- SUBJECT = `/Users/mengwong/src/legalese/commonswt/vn-insurance/subjects/vn/decree-67-2023`
- DEPOSIT = `/Users/mengwong/src/legalese/commonswt/vn-insurance/subjects/vn/decree-67-2023/encodings/legalese-2026-10-vn-10` (**write only here**; `BRIEF.md`, `tools/vnsrc.py` and `check.sh` are already in it)
- Sources, as plain text with line numbers (the checkable form):
- `nd67-congbao-1017-1018`: `/Users/mengwong/src/legalese/commonswt/vn-insurance/subjects/vn/decree-67-2023/source/raw/nd67-congbao-1017-1018.txt` (the text rendering; the PDF is beside it as `nd67-congbao-1017-1018.pdf`), 95 pages, sha256 `19a1de3a974866c90498f3478597798a08892ed6f73d4c461c3f1ef5f41253c8`, from <https://congbaocdn.chinhphu.vn/CongBaoCP/VanBan/2023/9/40096/46430-1-20231017-101867-2023-nd-cp.pdf>. congbaocdn.chinhphu.vn, the Government gazette (Công báo) issue 1017+1018, 20 September 2023: the decree's body and Phụ lục I-III. The server wants a Referer..
- `nd67-congbao-1019-1020`: `/Users/mengwong/src/legalese/commonswt/vn-insurance/subjects/vn/decree-67-2023/source/raw/nd67-congbao-1019-1020.txt` (the text rendering; the PDF is beside it as `nd67-congbao-1019-1020.pdf`), 85 pages, sha256 `456cbc7d4cbf8a0eeb3db989ac2edadd0ac9bb3a1fcd024ef4359dcd73b79d59`, from <https://congbaocdn.chinhphu.vn/CongBaoCP/VanBan/2023/9/40096/46433-1-20231019-102067-2023-nd-cp.pdf>. congbaocdn.chinhphu.vn, the Government gazette (Công báo) issue 1019+1020: the decree's remaining annexes (Phụ lục III continued to X, including Phụ lục VI). The server wants a Referer..
- `nd220-2026-congbao-367`: `/Users/mengwong/src/legalese/commonswt/vn-insurance/subjects/vn/decree-67-2023/source/raw/nd220-2026-congbao-367.txt` (the text rendering; the PDF is beside it as `nd220-2026-congbao-367.pdf`), 37 pages, sha256 `ab0e75cdd5de3b3bc0e0ebc6d3fb03b87b9a4eebfe2658b57b0b16b3c11f3a52`, from <https://congbaocdn.chinhphu.vn/180507251028987904/2026/7/3/469840-1782964220_v1_1783040868_signed.pdf>. congbaocdn.chinhphu.vn, the Government gazette (Công báo) no. 367, 3 July 2026: Decree 220/2026/NĐ-CP, which amends Decree 67/2023. The server wants a Referer..
- `/Users/mengwong/src/legalese/commonswt/vn-insurance/subjects/vn/decree-67-2023/subject.json` records the provenance of each source; `/Users/mengwong/src/legalese/commonswt/vn-insurance/subjects/vn/decree-67-2023/SOURCE-LICENSE.md` its licence position.
- Read-only aid, Law on Insurance Business 08/2022/QH15 (text): `/Users/mengwong/src/legalese/commonswt/vn-insurance/.aids/law-08-2022-qh15.txt`
- `l4`: `/Users/mengwong/.local/bin/l4`

## The subject

**Nghị định 67/2023/NĐ-CP** — the Government's decree on compulsory insurance of motor vehicle owners' civil liability, compulsory fire and explosion insurance, and compulsory insurance in construction investment. This row covers the **compulsory motor vehicle owners' civil liability insurance** (bảo hiểm bắt buộc trách nhiệm dân sự của chủ xe cơ giới): the rules every Vietnamese car and motorbike owner is legally required to insure under. It is made under the Law on Insurance Business of 16 June 2022 and (as the preamble says) the Road Traffic Law of 13 November 2008. The motor chapter fixes the liability limits (Điều 6), the exclusions (Điều 7), the premium (Điều 8 with Phụ lục I), the term (Điều 9), the certificate (Điều 10), termination and refund (Điều 11), the claims principles with their deadlines and advance-payment percentages (Điều 12), the claims documents (Điều 13), and the bodily-injury payment table (Phụ lục VI).

## Scope: pinned, do not widen or narrow

**Encoded: the compulsory motor vehicle owners' civil liability insurance of Decree 67/2023/NĐ-CP, in both of its vintages.**

- Chương I, only as far as the motor chapter needs it: Điều 1 (phạm vi điều chỉnh), Điều 2 (đối tượng áp dụng), Điều 3 (giải thích từ ngữ: only the terms the motor provisions use) and Điều 4 (nguyên tắc chung: only the paragraphs that govern motor insurance). Read each in full; say in the coverage table which paragraphs you encoded and which you left, with a reason.
- Chương II Mục 1, every paragraph: Điều 5 to Điều 13.
- Every annex that Điều 5 to 13 names: at least Phụ lục I (mức phí bảo hiểm, the premium table, with its special cases in Section VII) and Phụ lục VI (bảng quy định trả tiền bồi thường thiệt hại về sức khỏe, tính mạng, the bodily-injury payment table). Find every annex reference in those Articles yourself and list them.
- Decree 220/2026/NĐ-CP, to the extent it reaches any of the above.

**Reached and not encoded, to be recorded in the coverage table with a reason:** Chương II Mục 2 (the Quỹ bảo hiểm xe cơ giới, the motor vehicle insurance fund, Điều 14-22) except as Điều 12 refers to it; Chương III (fire and explosion); Chương IV (construction investment); Chương V (the responsibilities of ministries and bodies, Điều 61 onward) and the annexes that belong only to those chapters. Where a motor provision depends on one of these, its result is an input with a citation, or a `REFUSE`.

## The two vintages

| vintage | source | in force |
| --- | --- | --- |
| AS MADE | Decree 67/2023/NĐ-CP of 6 September 2023, gazette issues 1017+1018 and 1019+1020 | from 6 September 2023 (the gazette page says so; confirm in the text) |
| AS AMENDED | the same, as amended by Decree 220/2026/NĐ-CP of 22 June 2026, gazette no. 367 of 3 July 2026 | from 1 July 2026 (Điều 10 of Decree 220: confirm) |

Read all of Decree 220/2026 (it is short) and establish **from its text** which of its changes reach the motor provisions. The search results that led to this brief suggested only the construction provisions and Phụ lục III change, plus phrase substitutions in Điều 9 of Decree 220 (such as `người thứ ba` to `bên thứ ba`) that do touch Articles 5, 7, 10, 12 and 13; that is **unverified**, so check it and state the exact list in NOTES.md.
Also establish what Điều 10(2) of Decree 220 does to a contract made before 1 July 2026, and which date decides the vintage (the accident date? the contract date? the claim date?). If the text does not say, that is a fork and the encoding takes the date as an input and `REFUSE`s where it matters.
Use the rule-effective-time mechanism (`writing-l4-rules`, `references/source-patterns/04-dates-and-periods.md`) or take the vintage as an explicit input, as that page directs. Each vintage is its own answer; a vintage silent on something answers with silence. Run every scenario against both vintages and say which answers differ.
Two things the decree's preamble names deserve a fork-register entry each: it is made under the **Road Traffic Law of 13 November 2008** (check whether that is still the law in force; if the answer depends on something outside your sources, say it is unverified, do not assume), and Điều 5-13 define the vehicle classes and driver conditions by reference to that Law.

## Deliverable specifics

- The **answer tables** (NOTES.md §5): the premium for every vehicle class in Phụ lục I (including the 120%, 170% and 120% special cases and the `trên 25 chỗ` formula, and the 15% adjustment cap of Điều 8(2)); the limit of liability per person and per accident for each vehicle class (Điều 6); the advance payment percentages of Điều 12(3).
- **Phụ lục VI** is long. Encode it as a table-driven lookup: each source row becomes one L4 row, and a script (kept in DEPOSIT/tools/, run with `python3 -I`) generates one test per row from the raw text. State in NOTES.md how many rows the table has and how many tests were generated, and where the table's layout in `pdftotext` was ambiguous (look at the PDF page itself with the Read tool, using `pages`, to settle a doubtful cell, and say that you did).
- The deadlines and percentages of Điều 12 (1 hour, 24 hours, 3 working days, 5 working days, 70%, 50%, 30%, 10%, 5%) and the one-contract-first rule of Điều 12(9): a test on both sides of each.
- The premium arithmetic is money: VND, with the VAT carve-out the annex states ("chưa bao gồm thuế giá trị gia tăng"): do not add VAT unless the source does.

**Watch for.** Not a private contract but secondary legislation: the 'policy' every motor third-party-liability certificate in Vietnam is bound by. Decree 220/2026/NĐ-CP amends Decree 67/2023; from its Điều 1-8 and Điều 9, read for yourself which of its changes reach the motor provisions (the search results suggested only construction provisions and Phụ lục III change, plus phrase substitutions such as `người thứ ba` -> `bên thứ ba`; that is UNVERIFIED, so verify it from the text of Decree 220 itself).

## Bilingual convention (Vietnamese source, English encoding)

This follows the Hebrew rows IL-01 to IL-03 of the Income Tax Ordinance: English identifiers, the source language quoted mechanically from the deposited text and checked by a script.
Read `/Users/mengwong/src/legalese/commons/subjects/il/income-tax-ordinance-new-version/encodings/legalese-2026-10-il-03/NOTES.md` and its nouns module `ito-il03-nouns.l4` to see the shape.
The rules:

1. Every module starts with `@lang en`. Identifiers are English backtick names (`` `the sum insured` ``). Filenames are ASCII.
2. Before each definition or rule you encode, put the Vietnamese it encodes on `-- src:N | …` comment lines. **Generate those lines, never type them**:
   `python3 -I tools/vnsrc.py quote ../../source/raw/nd67-congbao-1017-1018.txt N [M]`
   prints `-- src:N | <line N>` for lines N to M of the raw text. `src:N` always means line N of the raw `.txt` rendering listed under "Where everything is".
3. Vietnamese may also appear in short verbatim runs elsewhere (a defined term in a comment or a string, in NOTES.md, in GLOSSARY.md). Every such run must occur verbatim in the raw text. Plain English paraphrase needs no marker.
4. Your own Vietnamese, if any (a translation of English text), is allowed only on a line that carries the marker `[translator]`; the checker exempts those lines, and the marker says out loud that it is not the source's.
5. **GLOSSARY.md** is the bilingual deliverable: a table with the columns
   `Vietnamese term (verbatim)` | `English identifier in the L4` | `English meaning, one line` | `where defined or used (Điều / clause, src line)` | `translation risk`.
   One row for every term the document defines, and for every type, field or constant you DECLARE that renders a Vietnamese concept. The `translation risk` column is where the bilingual work shows: where a Vietnamese term has more than one plausible English rendering, or where an English word you chose carries a legal sense the Vietnamese does not, say so.
6. In NOTES.md's coverage table give each heading as the document writes it (Vietnamese) beside your English gloss.
7. Before you finish, from DEPOSIT run `python3 -I tools/vnsrc.py check ../../source/raw/nd67-congbao-1017-1018.txt *.l4 *.md` . It must end `0 problems`. Put its last line in NOTES.md.
8. Money is Vietnamese đồng (VND), a bare `NUMBER`. Vietnamese number format writes `1.270.000` for one million two hundred seventy thousand (the dot groups thousands) and `,` for a decimal point: read every figure with that in mind and test the ones whose layout is at all ambiguous.

## Deliverables, all in DEPOSIT

1. `.l4` modules, ASCII filenames, each starting `@lang en`: **one nouns module** (`DECLARE` only; the entities, their fields and enumerations; a witness of ordinary competence could testify to each fact), one rules module per Part or topic of the document, and tests modules. A 2,000-line single module is not reviewable.
2. A **tests module** whose expected values come from the source.
3. `NOTES.md`, in this order: §0 build and run (which `l4`, its sha256, the command, the `check.sh` totals); §1 what is encoded and what is not; §2 the **coverage table** (every provision in scope, its heading as written plus an English gloss, a disposition `encoded` / `inert` / `out-of-scope` with a reason of real length / `reached-and-refused`, and where in the L4; no row left `deferred`); §3 the **fork register**; §4 `Findings` (the hostile reading); §5 an **answer table** where the subject has one; §6 what `check.sh` prints and which failures are expected, if any; §7 the `vnsrc check` line; §8 open questions for a domain expert.
4. `GLOSSARY.md` (see the bilingual section), `COMPARABLES.md` (see above).
5. `check.sh` (already here: do not edit it), `encoding.json`, `SOURCE-LICENSE.md` (short: it points at the subject-level one and says how many `src:` lines the encoding quotes).
6. `encoding.json`: follow `/Users/mengwong/src/legalese/commons/subjects/il/income-tax-ordinance-new-version/encodings/legalese-2026-10-il-03/encoding.json`; `id` is the row id above, `run.id` and `run.agent` as above, `status` `draft`, `version` `0.1.0`, `license` `Apache-2.0`; `language` has `source_text`, `module_body: "en"` and a note; `source` lists each source document with its url and sha256 from `SUBJECT/subject.json`; `modules`; `scope`; `forks`; `self_check` with the command, the date, the `l4` sha256 and the totals; and `not_reviewed`: gate HG1 not sought, no domain expert has read it against the source, no independent test pass has been run, and every expected value was written by the same session that wrote the rules.

## How to model an insurance document

Three layers, kept apart:

1. **Is the event covered?** The insuring clause, the exclusions, the conditions precedent, the waiting periods, the eligibility and age rules. The incident and the insured are input records. Where a fact the answer turns on is not in the record, `REFUSE` naming it; do not assume it.
2. **How much is payable?** The sum insured or limit, valuation basis, deductible, depreciation, co-payment, sub-limits, per-event and per-period caps, benefit schedules. Encode every table the document contains as data that maps one source row to one L4 row, and test every row (generate long test lists from the raw text with a script, rather than retyping figures, and say so).
3. **What must each party do, and by when?** Notice, documents, assessment, payment, renewal, cancellation. Where the source is deontic with a deadline, use the regulative rules in `writing-l4-rules` (`references/regulative.md`); where it is a bare time-bar, a function returning the date is enough.

Tests, from the document and never from your code:
worked examples the document prints; both sides of every threshold, period and limit; for every exclusion, one fact pattern that triggers it and one near miss that does not; and one scenario that makes several layers interact (cover, then deductible, then limit).

## The hostile reading (this is the point of the exercise)

The research thesis is that a policy is code, and that a loophole is an exploit. Once the encoding is green, spend a dedicated pass attacking it as a policyholder's lawyer and as the insurer's, looking for:
events that fall between the cover and the exclusions; contradictions between clauses; defined terms that carry weight but are never defined or are used inconsistently; discretion given to the insurer with no criteria; cover that is illusory on a literal reading; deadlines that cannot all be met; arithmetic that does not close (a sub-limit above its limit, percentages that sum past 100); a time-bar shorter than the time the same document allows for another step.
Record each in NOTES.md under `## Findings`: the source lines, a minimal scenario, and the evidence from the L4 (an `#EVAL` or `#ASSERT` showing the surprising answer) or the words `reading only`. A finding that the encoding cannot demonstrate is allowed but must say so. Separate these from forks: a fork is an ambiguity you resolved; a finding is a defect in the instrument as written.

## Comparables (for the later cross-insurer analysis)

Write `COMPARABLES.md`: one table, at most 25 rows, `parameter | value as written (Vietnamese verbatim or "not stated") | English rendering | clause | src line`.
Use these parameters where the document has them, and add others the document makes prominent: policy term; who may be insured and age limits; geographic scope; waiting periods; sum insured or limit basis; deductible or excess; co-payment; valuation or depreciation basis; sub-limits; number of exclusions and their headings; insured's notice deadline; claim documents required; insurer's assessment and payment deadline; time-bar for claims or suit; cancellation and refund; renewal; dispute forum or governing law.
Where the document does not state a parameter, write `not stated`; do not fill it from outside knowledge.

## Rules that matter

- **Encode isomorphically.** A reader holding the source beside your module checks it line by line. One source provision, one recognisable place in the L4, with the provision's number and its `src:` lines on it.
- **Inputs, never defaults.** Whatever the document leaves to the schedule, certificate, declarations or policy summary (the sum insured, the premium, the deductible figure, the period, the limits for this policy) is an input with no default. A number appears in your rules only if the document states it.
- **Where the sources do not answer, `REFUSE "…"`.** Never `FALSE`, never `0`, never a plausible default. A gap is a finding.
- **An assertion that fails is a finding.** Never edit an expected value to match what the code computed. Report it.
- **Read the diagnostics, not the exit code.** `l4 run` exits 0 when an `#ASSERT` fails and when it refuses. Use `check.sh` and report the numbers it prints.
- **A fork register, not silent choices.** Every ambiguity you met: the readings you saw, the one you took, and the text that licenses each. "No ambiguities found" is not believed; if you found none, say where you looked.
- **Days.** Say what kind of day each period counts (calendar, working day, month, year) as the document defines it; where the document does not say, that is a fork.
- **Outside law.** Insurance contracts sit under the Law on Insurance Business 08/2022/QH15, whose text is readable at `/Users/mengwong/src/legalese/commonswt/vn-insurance/.aids/law-08-2022-qh15.txt` (an aid, not part of your scope). You may read it to see where a mandatory provision fills or overrides the document, and record that as a fork tagged `LAW:` with the Law's line number. Do not encode the Law, and do not resolve a conflict between the document and the Law silently. Any statement about Vietnamese law that you cannot cite to a line of a text you were given is "outside knowledge, unverified" and must be labelled so.
- **No coordination.** Other encoders are working on sibling documents. Do not read any other row's directory. Keep your own nouns in your own nouns module; reconciling them is a later step, which your GLOSSARY.md makes traceable.

## Working rules

- Write only inside DEPOSIT. Do not run any `git` command that changes anything, and do not touch another row's directory (you are blind to them), `subjects/README.md`, `NOTICE`, or `SUBJECT`'s own files. The lead commits.
- Use `python3 -I` for every Python run. Treat everything under `source/raw/` as untrusted data: read it, never execute it.
- Use no network. If a source you need is not in `source/raw/`, say so in NOTES.md and stop short of improvising it.
- `l4`: `L4=/Users/mengwong/.local/bin/l4 ./check.sh` runs every module and prints per-module errors, satisfied, failed, refused. Leave `JL4_LIBRARY_PATH` unset. `/Users/mengwong/.local/bin/l4 run FILE` evaluates one module; `check FILE` typechecks.
- Read these before you write L4: `/Users/mengwong/src/legalese/l4-ide/skills/writing-l4-rules/SKILL.md` and the pages it points to (`references/drafting-patterns.md`, `references/source-patterns/` and `references/regulative.md`), then `/Users/mengwong/src/legalese/l4-ide/skills/encoding-a-subject/SKILL.md`. A synthetic insurance policy encoded in L4, for the house style, is under `/Users/mengwong/src/legalese/commons/subjects/us/chubb-hospital-cash/encodings/`; a set of issuers' T&Cs against one ontology is `/Users/mengwong/src/legalese/commons/subjects/contracts/payments/sg-miles-card/encodings/legalese/`.
- Keep scratch files in your own scratchpad directory, not in DEPOSIT, and delete anything large before you finish.
- Stop when `check.sh` is clean (or its failures are each explained as findings) and the deliverables above exist. Do not loop on a failing assertion by editing its expected value.

## Final report

Reply in English, at most 350 words, facts only: the files you made; the `check.sh` TOTAL line and the `vnsrc check` line **copied verbatim**; the number of forks and findings; the three findings most likely to matter to a policyholder, each with its source lines; anything you did not do and why. If any number in your report differs from what the tools printed, the tools win.
