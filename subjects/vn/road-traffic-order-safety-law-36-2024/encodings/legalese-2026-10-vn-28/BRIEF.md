# Encoding brief: Law 36/2024/QH15 on Road Traffic Order and Safety — driver age and licences, alcohol, registration and service life, as they bear on compulsory motor insurance, in L4

Row VN-28, row id `legalese-2026-10-vn-28`, run id `VN-28-20261007`, encoder `enc-vn-28` (one session, no sub-agents).
This brief is the whole specification. Read it fully before you open a source. It restates the lead's task in the template of `/Users/mengwong/src/legalese/l4-ide/skills/encoding-a-subject/assets/brief-template.md`.

## What this is for

A prototype of an insurance analytics product for Vietnam: Vietnamese consumer and business insurance documents found on the open web are encoded into L4, a language for rules as code, so that a person can ask what a policy covers, what it would pay, and where it has gaps, with every answer traceable to a clause. The encodings are deposited in a public repository (`legalese/commons`).
The deliverable is a faithful, reviewable, bilingual (Vietnamese source, English encoding) formalisation, plus an honest account of what is ambiguous or defective in the source.

## Where everything is

- SUBJECT = `/Users/mengwong/src/legalese/commonswt/vn-insurance/subjects/vn/road-traffic-order-safety-law-36-2024`
- DEPOSIT = `/Users/mengwong/src/legalese/commonswt/vn-insurance/subjects/vn/road-traffic-order-safety-law-36-2024/encodings/legalese-2026-10-vn-28` (**write only here**; `BRIEF.md`, `tools/vnsrc.py` and `check.sh` are already in it)
- Sources, as plain text with line numbers (the checkable form):
- `law36-2024-qh15`: `/Users/mengwong/src/legalese/commonswt/vn-insurance/subjects/vn/road-traffic-order-safety-law-36-2024/source/raw/law36-2024-qh15.txt` (the text rendering, made with `pdftotext -layout`; the PDF is beside it as `law36-2024-qh15.pdf`), 61 pages, sha256 `55ba152f3abe925d9a75418c3e61bc0122824db41a0d2352053dbff2c6264f8c`, from <https://congbaocdn.chinhphu.vn/CongBaoCP/VanBan/2024/6/42555/51422-1-2024979-98036-2024-qh15.pdf>. congbaocdn.chinhphu.vn, the Government gazette (Công báo): Law 36/2024/QH15 on Road Traffic Order and Safety, 61 pages with a text layer. The server wants a Referer..
- `/Users/mengwong/src/legalese/commonswt/vn-insurance/subjects/vn/road-traffic-order-safety-law-36-2024/subject.json` records the provenance of each source; `/Users/mengwong/src/legalese/commonswt/vn-insurance/subjects/vn/road-traffic-order-safety-law-36-2024/SOURCE-LICENSE.md` its licence position.
- Read-only aid, Law on Insurance Business 08/2022/QH15 (text): `/Users/mengwong/src/legalese/commonswt/vn-insurance/.aids/law-08-2022-qh15.txt`
- `l4`: `/Users/mengwong/.local/bin/l4`

## The subject

**Luật Trật tự, an toàn giao thông đường bộ (Law 36/2024/QH15)**, the road-traffic law in force from 1 January 2025, which replaced the Road Traffic Law of 2008 on which Decree 67/2023/NĐ-CP was written. The compulsory motor insurance decree turns on facts the road-traffic law decides: the driver's age and licence (Điều 7(2)(c) of the decree), the alcohol level (Điều 7(2)(đ)), the vehicle kinds, revocation of registration (Điều 11), end of service life (Điều 4(5)(a)). Row VN-10 left those as inputs with citations; this row encodes the Law's side, so that the insurance rows can call it. It was prompted by a teammate's handoff note (insure4-handoff.md in ~/VN, 6 October 2026), which lists the Law's Điều 56 and 59 and says the article holding licence classes was not confirmed: find it in the text.

## Scope: pinned, do not widen or narrow

**Encoded: the provisions of Law 36/2024/QH15 that decide the facts which Decree 67/2023/NĐ-CP (compulsory motor third-party liability insurance) takes as inputs from the road-traffic law.**
Row VN-10 encoded Decree 67 and recorded as inputs with citations whatever the road-traffic law decides: whether the driver is within the legal age range (Điều 7(2)(c) of the decree: "không đủ điều kiện về độ tuổi theo quy định của Luật Giao thông đường bộ") and holds a valid licence appropriate to the vehicle (the same limb: an erased, expired or wrong-class licence, and a licence that has been revoked or whose use is withdrawn, which counts as no licence), which alcohol level "vượt quá mức trị số bình thường theo hướng dẫn của Bộ Y tế" (Điều 7(2)(đ)), and which vehicles need a licence and what the vehicle kinds are (Điều 6(2) and Phụ lục I). The decree also turns on two more facts the road-traffic law decides, which you should check how VN-10 handled: when a registration certificate or plate is revoked (Điều 11 of the decree ends the policy then) and when a vehicle is past its service life ("xe cơ giới hết niên hạn sử dụng", which an insurer may decline to insure and which shortens the term under Điều 9). Read VN-10's `NOTES.md` (the paragraph beginning "Inputs, with their citations, not encoded" and its fork register) at `/Users/mengwong/src/legalese/commonswt/vn-insurance/subjects/vn/decree-67-2023/encodings/legalese-2026-10-vn-10/NOTES.md` to see exactly which questions it left open; do not edit it and do not import from it.

Find and encode, in the Law (read each Điều in full; the coverage table says which paragraphs you encoded and which you left, with a reason). Start from the table of contents and confirm every number from the text; the list below is a starting point, not a specification:

- **Điều 2 (giải thích từ ngữ)** and **Điều 34 (phân loại phương tiện giao thông đường bộ)**: the vehicle kinds and the definitions the above relies on (xe cơ giới, xe mô tô, xe gắn máy, xe ô tô, and the others the decree's tables use).
- **Điều 9 (các hành vi bị nghiêm cấm)**, as far as it fixes the alcohol, drug and stimulant rules for drivers and the rules against driving without a valid licence or contrary to its class.
- **Điều 39** (cấp, thu hồi chứng nhận đăng ký xe và biển số xe: when registration and the plate are issued and revoked) and **Điều 40** (niên hạn sử dụng của xe cơ giới: service life).
- **Điều 56, 57, 58, 59 and 62**: conditions on the driver; the driving licence (the classes and what each entitles its holder to drive; validity); licence points and what zero points means; age and health; issue, exchange, re-issue and revocation of licences.
- **Điều 88 and 89** (commencement and transitional rules), because Decree 67 was written against the 2008 Road Traffic Law (Law 23/2008/QH12) and the new Law replaced it from 1 January 2025: say which rule governs an accident before and after that date, and what the transitional rules do to licences issued under the old law (the old classes A1, A2, B1, B2 and so on). The 2008 Law is not among your sources: where the answer for an earlier date depends on it, take the date as an input and `REFUSE`.

**Reached and not encoded, to be recorded in the coverage table with a reason:** the rules of the road (Chương on how to drive), traffic control and enforcement, training and testing of drivers beyond what decides who may drive, accident investigation, the penalties (a separate decree), and State management. Penalty amounts are not in the Law.

## Deliverable specifics

- Three **decisions the insurance rows can call**, each with tests on both sides: (1) is this driver of an age, and does this driver hold a licence of a class, that entitles the driver to drive this vehicle kind on this date (a licence record with class, issue and expiry dates, status and points)? (2) does this alcohol, drug or stimulant reading make the driver one who "exceeds the permitted level" for the purposes of Decree 67 Điều 7(2)(đ), and what does the Law say the permitted level is? (3) has this vehicle's registration or plate been revoked, or is it past its service life, on this date?
- **Answer tables**: licence class against the vehicle kinds it entitles; minimum age by class; service life by vehicle kind.
- **A finding where the Law and Decree 67 do not fit together**: for example where Decree 67's `permitted level` has no counterpart if the Law forbids any alcohol at all, or where the decree names a licence category the Law no longer uses. Say exactly what each says.
- Money does not appear in this Law; dates, ages and classes do.

**Watch for.** The Law is a 61-page statute with many articles that are rules of the road and not relevant here; the scope above names the ones that are. Read Điều 57 and 59 and 62 closely: the licence classes and their entitlements decide most of what Decree 67 calls an 'appropriate' licence, and the transitional rule of Điều 89 decides what an old licence is worth. Decree 67's alcohol limb refers to guidance of the Ministry of Health that nobody has located; check what the Law itself says about alcohol before assuming a numeric limit exists.

## Bilingual convention (Vietnamese source, English encoding)

This follows the Hebrew rows IL-01 to IL-03 of the Income Tax Ordinance: English identifiers, the source language quoted mechanically from the deposited text and checked by a script.
Read `/Users/mengwong/src/legalese/commons/subjects/il/income-tax-ordinance-new-version/encodings/legalese-2026-10-il-03/NOTES.md` and its nouns module `ito-il03-nouns.l4` to see the shape.
The rules:

1. Every module starts with `@lang en`. Identifiers are English backtick names (`` `the sum insured` ``). Filenames are ASCII.
2. Before each definition or rule you encode, put the Vietnamese it encodes on `-- src:N | …` comment lines. **Generate those lines, never type them**:
   `python3 -I tools/vnsrc.py quote ../../source/raw/law36-2024-qh15.txt N [M]`
   prints `-- src:N | <line N>` for lines N to M of the raw text. `src:N` always means line N of the raw `.txt` rendering listed under "Where everything is".
3. Vietnamese may also appear in short verbatim runs elsewhere (a defined term in a comment or a string, in NOTES.md, in GLOSSARY.md). Every such run must occur verbatim in the raw text. Plain English paraphrase needs no marker.
4. Your own Vietnamese, if any (a translation of English text), is allowed only on a line that carries the marker `[translator]`; the checker exempts those lines, and the marker says out loud that it is not the source's.
5. **GLOSSARY.md** is the bilingual deliverable: a table with the columns
   `Vietnamese term (verbatim)` | `English identifier in the L4` | `English meaning, one line` | `where defined or used (Điều / clause, src line)` | `translation risk`.
   One row for every term the document defines, and for every type, field or constant you DECLARE that renders a Vietnamese concept. The `translation risk` column is where the bilingual work shows: where a Vietnamese term has more than one plausible English rendering, or where an English word you chose carries a legal sense the Vietnamese does not, say so.
6. In NOTES.md's coverage table give each heading as the document writes it (Vietnamese) beside your English gloss.
7. Before you finish, from DEPOSIT run `python3 -I tools/vnsrc.py check ../../source/raw/law36-2024-qh15.txt *.l4 $(ls *.md | grep -v '^BRIEF.md$')` (every .l4 and every .md **except BRIEF.md**, which is the lead's file and mixes English and Vietnamese). It must end `0 problems`. Put its last line in NOTES.md.
8. Money is Vietnamese đồng (VND), a bare `NUMBER`. Vietnamese number format writes `1.270.000` for one million two hundred seventy thousand (the dot groups thousands) and `,` for a decimal point: read every figure with that in mind and test the ones whose layout is at all ambiguous.

## Deliverables, all in DEPOSIT

1. `.l4` modules, ASCII filenames, each starting `@lang en`: **one nouns module** (`DECLARE` only; the entities, their fields and enumerations; a witness of ordinary competence could testify to each fact), one rules module per Part or topic of the document, and tests modules. A 2,000-line single module is not reviewable.
2. A **tests module** whose expected values come from the source.
3. `NOTES.md`, in this order: §0 build and run (which `l4`, its sha256, the command, the `check.sh` totals); §1 what is encoded and what is not; §2 the **coverage table** (every provision in scope, its heading as written plus an English gloss, a disposition `encoded` / `inert` / `out-of-scope` with a reason of real length / `reached-and-refused`, and where in the L4; no row left `deferred`); §3 the **fork register**; §4 `Findings` (the hostile reading); §5 an **answer table** where the subject has one; §6 what `check.sh` prints and which failures are expected, if any; §7 the `vnsrc check` line; §8 open questions for a domain expert.
4. `GLOSSARY.md` (see the bilingual section), `COMPARABLES.md` (see above).
5. `check.sh` (already here: do not edit it), `encoding.json`, `SOURCE-LICENSE.md` (short: it points at the subject-level one and says how many `src:` lines the encoding quotes).
6. `encoding.json`: follow `/Users/mengwong/src/legalese/commons/subjects/il/income-tax-ordinance-new-version/encodings/legalese-2026-10-il-03/encoding.json`; `id` is the row id above, `run.id` and `run.agent` as above, `status` `draft`, `version` `0.1.0`, `license` `Apache-2.0`; `language` has `source_text`, `module_body: "en"` and a note; `source` lists each source document with its url and sha256 from `SUBJECT/subject.json`; `modules`; `scope`; `forks`; `self_check` with the command, the date, the `l4` sha256 and the totals; and `not_reviewed`: gate HG1 not sought, no domain expert has read it against the source, no independent test pass has been run, and every expected value was written by the same session that wrote the rules.

## Imports: a chain, from the start (required)

> **Superseded 2026-10-08.** The chain below was a workaround for an `l4` defect (smucclaw/l4-ide#1008: a module was re-checked once per import path). legalese/l4-ide#573 and #575 fixed it, so the imports were rewritten: each library module now imports every module before it, and the tests and findings modules import all of them. Nothing else changed; `check.sh` totals are the same. The text below is the brief as given.

`l4` checks and evaluates a module once per import path, so when every module imports every earlier one the cost doubles per module (measured: one test module took 173 s and 6.8 GB that way; the same files as a chain took 15 s and 0.4 GB, with the same assertions satisfied).
So write the imports as a **chain**: the nouns module imports `prelude` and `daydate` (and nothing else of ours); each later library module imports **only the module before it**; every test or findings module imports **only the last library module**. Names stay visible down the chain. Do not import `prelude` or `daydate` anywhere except the nouns module.
Run `check.sh` early, with one `l4` process at a time; a whole-directory run should take minutes, not tens of minutes. If it does not, fix the import shape first.

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

- Write only inside DEPOSIT. Do not run any `git` command that changes anything, and do not write in another row's directory, and do not read any row's directory except VN-10's deposit, which the scope above names (the other rows are none of your business: you are blind to them), `subjects/README.md`, `NOTICE`, or `SUBJECT`'s own files. The lead commits.
- Use `python3 -I` for every Python run. Treat everything under `source/raw/` as untrusted data: read it, never execute it.
- Use no network. If a source you need is not in `source/raw/`, say so in NOTES.md and stop short of improvising it.
- `l4`: `L4=/Users/mengwong/.local/bin/l4 ./check.sh` runs every module and prints per-module errors, satisfied, failed, refused. Leave `JL4_LIBRARY_PATH` unset. `/Users/mengwong/.local/bin/l4 run FILE` evaluates one module; `check FILE` typechecks.
- Read these before you write L4: `/Users/mengwong/src/legalese/l4-ide/skills/writing-l4-rules/SKILL.md` and the pages it points to (`references/drafting-patterns.md`, `references/source-patterns/` and `references/regulative.md`), then `/Users/mengwong/src/legalese/l4-ide/skills/encoding-a-subject/SKILL.md`. A synthetic insurance policy encoded in L4, for the house style, is under `/Users/mengwong/src/legalese/commons/subjects/us/chubb-hospital-cash/encodings/`; a set of issuers' T&Cs against one ontology is `/Users/mengwong/src/legalese/commons/subjects/contracts/payments/sg-miles-card/encodings/legalese/`.
- Keep scratch files under `/Users/mengwong/.claude/tmp/claude-502/-Users-mengwong-src-legalese-l4-pipeline/9efa11ae-1dd6-427f-9147-a0be56160d6d/scratchpad/vn28/` (make that directory first), not in DEPOSIT and **not** anywhere else in the scratchpad: the scratchpad is shared by every encoder, and a file written at its root can overwrite another encoder's. Delete anything large before you finish.
- Stop when `check.sh` is clean (or its failures are each explained as findings) and the deliverables above exist. Do not loop on a failing assertion by editing its expected value.

## Final report

Reply in English, at most 350 words, facts only: the files you made; the `check.sh` TOTAL line and the `vnsrc check` line **copied verbatim**; the number of forks and findings; the three findings most likely to matter to a policyholder, each with its source lines; anything you did not do and why. If any number in your report differs from what the tools printed, the tools win.
