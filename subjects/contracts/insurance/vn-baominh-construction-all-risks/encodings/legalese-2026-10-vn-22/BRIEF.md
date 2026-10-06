# Encoding brief: Bảo Minh construction all risks insurance rules (Quy tắc bảo hiểm mọi rủi ro xây dựng), in L4

Row VN-22, row id `legalese-2026-10-vn-22`, run id `VN-22-20261006`, encoder `enc-vn-22` (one session, no sub-agents).
This brief is the whole specification. Read it fully before you open a source. It restates the lead's task in the template of `/Users/mengwong/src/legalese/l4-ide/skills/encoding-a-subject/assets/brief-template.md`.

## What this is for

A prototype of an insurance analytics product for Vietnam: Vietnamese consumer and business insurance documents found on the open web are encoded into L4, a language for rules as code, so that a person can ask what a policy covers, what it would pay, and where it has gaps, with every answer traceable to a clause. The encodings are deposited in a public repository (`legalese/commons`).
The deliverable is a faithful, reviewable, bilingual (Vietnamese source, English encoding) formalisation, plus an honest account of what is ambiguous or defective in the source.

## Where everything is

- SUBJECT = `/Users/mengwong/src/legalese/commonswt/vn-insurance/subjects/contracts/insurance/vn-baominh-construction-all-risks`
- DEPOSIT = `/Users/mengwong/src/legalese/commonswt/vn-insurance/subjects/contracts/insurance/vn-baominh-construction-all-risks/encodings/legalese-2026-10-vn-22` (**write only here**; `BRIEF.md`, `tools/vnsrc.py` and `check.sh` are already in it)
- Sources, as plain text with line numbers (the checkable form):
- `baominh-car`: `/Users/mengwong/src/legalese/commonswt/vn-insurance/subjects/contracts/insurance/vn-baominh-construction-all-risks/source/raw/baominh-car.txt` (the text rendering, made with `pdftotext -layout`; the PDF is beside it as `baominh-car.pdf`), 6 pages, sha256 `5dbef555b6fd4132dd6b55c0ebb7200e7f03071bd0867e5644c3085d8ea2bcce`, from <https://www.baominh.com.vn/uploads/source/File%20t%C3%A0i%20li%E1%BB%87u/tai%20san/03-Quytacbaohiemxaydung-MunicRe-TV.pdf>. baominh.com.vn, the insurer's own website (the server refuses a request with no Referer header: fetch.sh sends one).
- `/Users/mengwong/src/legalese/commonswt/vn-insurance/subjects/contracts/insurance/vn-baominh-construction-all-risks/subject.json` records the provenance of each source; `/Users/mengwong/src/legalese/commonswt/vn-insurance/subjects/contracts/insurance/vn-baominh-construction-all-risks/SOURCE-LICENSE.md` its licence position.
- Read-only aid, Law on Insurance Business 08/2022/QH15 (text): `/Users/mengwong/src/legalese/commonswt/vn-insurance/.aids/law-08-2022-qh15.txt`
- `l4`: `/Users/mengwong/.local/bin/l4`

## The subject

**Quy tắc bảo hiểm mọi rủi ro xây dựng** — Bảo Minh's contractors / construction all risks (CAR) wording, an **engineering** product, 6 pages. Like the installation wording it rests on a proposal form and a questionnaire. The URL's file name carries `MunicRe`; read the text for any attribution rather than assume one.

## Scope: pinned, do not widen or narrow

**The whole document**: every Part, Article, clause, definition, schedule, table and annex it contains. Nothing is deliberately left out.
What the document leaves to a schedule, certificate, declarations page or policy summary that is not in the document is an **input** (see the rules), not a gap.
The vintage is "the document as published at its URL on the retrieval date, 2026-10-06". What it does not show (a later amendment, a newer decision), you do not know.

**Watch for.** A sibling of Bảo Minh's installation all risks wording (another encoder, blind to you). Compulsory construction-investment insurance under Decree 67/2023 is a different regime; do not confuse them.

## Bilingual convention (Vietnamese source, English encoding)

This follows the Hebrew rows IL-01 to IL-03 of the Income Tax Ordinance: English identifiers, the source language quoted mechanically from the deposited text and checked by a script.
Read `/Users/mengwong/src/legalese/commons/subjects/il/income-tax-ordinance-new-version/encodings/legalese-2026-10-il-03/NOTES.md` and its nouns module `ito-il03-nouns.l4` to see the shape.
The rules:

1. Every module starts with `@lang en`. Identifiers are English backtick names (`` `the sum insured` ``). Filenames are ASCII.
2. Before each definition or rule you encode, put the Vietnamese it encodes on `-- src:N | …` comment lines. **Generate those lines, never type them**:
   `python3 -I tools/vnsrc.py quote ../../source/raw/baominh-car.txt N [M]`
   prints `-- src:N | <line N>` for lines N to M of the raw text. `src:N` always means line N of the raw `.txt` rendering listed under "Where everything is".
3. Vietnamese may also appear in short verbatim runs elsewhere (a defined term in a comment or a string, in NOTES.md, in GLOSSARY.md). Every such run must occur verbatim in the raw text. Plain English paraphrase needs no marker.
4. Your own Vietnamese, if any (a translation of English text), is allowed only on a line that carries the marker `[translator]`; the checker exempts those lines, and the marker says out loud that it is not the source's.
5. **GLOSSARY.md** is the bilingual deliverable: a table with the columns
   `Vietnamese term (verbatim)` | `English identifier in the L4` | `English meaning, one line` | `where defined or used (Điều / clause, src line)` | `translation risk`.
   One row for every term the document defines, and for every type, field or constant you DECLARE that renders a Vietnamese concept. The `translation risk` column is where the bilingual work shows: where a Vietnamese term has more than one plausible English rendering, or where an English word you chose carries a legal sense the Vietnamese does not, say so.
6. In NOTES.md's coverage table give each heading as the document writes it (Vietnamese) beside your English gloss.
7. Before you finish, from DEPOSIT run `python3 -I tools/vnsrc.py check ../../source/raw/baominh-car.txt *.l4 *.md` . It must end `0 problems`. Put its last line in NOTES.md.
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
- Keep scratch files under `/Users/mengwong/.claude/tmp/claude-502/-Users-mengwong-src-legalese-l4-pipeline/9efa11ae-1dd6-427f-9147-a0be56160d6d/scratchpad/vn22/` (make that directory first), not in DEPOSIT and **not** anywhere else in the scratchpad: the scratchpad is shared by every encoder, and a file written at its root can overwrite another encoder's. Delete anything large before you finish.
- Stop when `check.sh` is clean (or its failures are each explained as findings) and the deliverables above exist. Do not loop on a failing assertion by editing its expected value.

## Final report

Reply in English, at most 350 words, facts only: the files you made; the `check.sh` TOTAL line and the `vnsrc check` line **copied verbatim**; the number of forks and findings; the three findings most likely to matter to a policyholder, each with its source lines; anything you did not do and why. If any number in your report differs from what the tools printed, the tools win.
