# Encoding brief: Law 08/2022/QH15 on Insurance Business, the whole Act in three vintages, in L4

> Note added when the row was filed: the paths in this brief are those of the working tree the encoder ran in, an isolated copy of this subject directory in which `../../../../../refs/il-03/` held read-only copies of three files of the row `legalese-2026-10-il-03` of this repository.
> The brief is otherwise as it was given.

Row id `legalese-2026-10-vn-29`, run id `VN-29-20261010`, encoder `enc-vn-29` (one session, one encoder, no sub-agents).
This brief is the whole specification. Read it fully before you open a source.
It restates the lead's task in the template of `encoding-a-subject/assets/brief-template.md`, with the coverage discipline of the `running-the-l4-pipeline` deposit runbook (a roadmap of every unit of the source, every unit starting `deferred`).

## What this is for

A public, reviewable, bilingual (Vietnamese source, English encoding) formalisation of the statute that governs insurance business in Vietnam, filed in the public repository `legalese/commons`.
The deliverable is a faithful encoding, a complete account of what was encoded and what was not, and an honest account of the ambiguities and defects in the instrument as written.
Nothing in this deposit is legal advice, and no Vietnamese-qualified lawyer has read it.

## Where everything is

All paths are relative to DEPOSIT, which is your working directory. Write only inside it.

- Sources, as plain text with line numbers (the checkable form), each the `pdftotext -layout` rendering of a gazette PDF that sits beside it:
  - `../../source/raw/law08-2022-qh15.txt` (2,905 lines): Law 08/2022/QH15, **Điều 1 to Điều 130**, Công báo số 575 + 576 of 17 July 2022. PDF sha256 `1790a7788738008ffd2574f1248aedcfd485e5966647b9f29be07335b17194c4`. It ends with "(Xem tiếp Công báo số 577 + 578)".
  - `../../source/raw/law08-2022-qh15-577-578.txt` (570 lines): the rest of Law 08/2022/QH15, **Điều 131 to Điều 157**, Công báo số 577 + 578 of 17 July 2022. PDF sha256 `f2310ab382393a9b4845a9bf09880d80b1e845e5261c07743181fc8c6a4ed58c`.
  - `../../source/raw/law139-2025-qh15.txt` (356 lines): Law 139/2025/QH15 amending the Law, Công báo số 39 of 22 January 2026, 3 articles. PDF sha256 `81c81bf4f77ed68f0fbaa4967c6573aa6ff81831960a742de14e8933287ad665`.
- `../../subject.json` records the provenance of each source (URLs, hashes); `../../SOURCE-LICENSE.md` the licence position; `../../registers/source-bundle.json` the P1 source bundle.
- `registers/roadmap-law08-2022-qh15.json` (130 units, Điều 1 to 130), `registers/roadmap-law08-2022-qh15-577-578.json` (27 units, Điều 131 to 157) and `registers/roadmap-law139-2025-qh15.json` (25 units, the numbered clauses of Law 139/2025). **Every unit starts `deferred`.** You move each one as it lands, with `tools/roadmap.py` (see "The roadmap").
- `tools/vnsrc.py`: quotes the Vietnamese source mechanically and checks that every quotation is verbatim.
- `check.sh` (already here: do not edit it) runs every `.l4` module in DEPOSIT and prints errors, assertions satisfied, failed and refused per module.
- `l4`: on `PATH`. Leave `JL4_LIBRARY_PATH` unset.
- Skills to read before you write L4, read-only: `/Users/mengwong/src/legalese/l4-ide/skills/writing-l4-rules/SKILL.md` and the pages it points to (`references/drafting-patterns.md`, `references/source-patterns/` including `04-dates-and-periods.md` section 4.7 on the rule-version axis, `references/regulative.md`), then `/Users/mengwong/src/legalese/l4-ide/skills/encoding-a-subject/SKILL.md`.
- A worked example of the bilingual convention, read-only: `../../../../../refs/il-03/` (a copy of the Hebrew-source row `legalese-2026-10-il-03` of the Income Tax Ordinance in `legalese/commons`: its `encoding.json`, its nouns module and its `NOTES.md`).

## The subject

**Luật Kinh doanh bảo hiểm số 08/2022/QH15**, the Law on Insurance Business, passed by the National Assembly on 16 June 2022, in force from 1 January 2023 (Điều 156), 157 articles in seven chapters:

| Chương | Heading | Điều |
| --- | --- | --- |
| I | Những quy định chung | 1 to 14 |
| II | Hợp đồng bảo hiểm | 15 to 61 |
| III | Doanh nghiệp bảo hiểm, doanh nghiệp tái bảo hiểm, chi nhánh nước ngoài tại Việt Nam | 62 to 123 |
| IV | Đại lý bảo hiểm, doanh nghiệp môi giới bảo hiểm, dịch vụ phụ trợ bảo hiểm | 124 to 143 |
| V | Bảo hiểm vi mô | 144 to 150 |
| VI | Quản lý nhà nước về hoạt động kinh doanh bảo hiểm | 151 to 154 |
| VII | Điều khoản thi hành | 155 to 157 |

(The chapter headings are abbreviated; confirm each from the text.)
The Law is a statute of the National Assembly; it is made directly under the Constitution and has no empowering instrument above it to fetch. It delegates detail to the Government and to the Minister of Finance in many places, and those instruments are **not** among your sources: where an article hands a matter to them, encode the delegation (who may regulate what, as the article writes it), never the unseen content.

### Vintages

The Law exists in three vintages, and all three are in scope, each as its own answer.

| vintage | in force | what it is | where |
| --- | --- | --- | --- |
| **V1, as made** | 1 January 2023 to 31 December 2025 | Law 08/2022/QH15 as passed | the two `law08-2022-qh15*.txt` files |
| **V2** | from 1 January 2026 | V1 with Law 139/2025/QH15 Điều 1 and Điều 2 applied, except Điều 2(6) and Điều 2(8) of that Law | `law139-2025-qh15.txt`, applied to V1 |
| **V3** | from 1 July 2026 | V2 with Điều 2(6) and Điều 2(8) of Law 139/2025/QH15 also applied (Điều 3(2) of that Law) | `law139-2025-qh15.txt` |

There is no separate file of the amended text: **you apply the amending Law to V1 yourself, and say so.**
The amending Law is 3 articles; its Điều 1 has 15 numbered clauses that amend, add or replace provisions (Điều 3, 63, 73, 74, 81, 82, 87, 101, 127, 134, 138, 151, 154, 156 and 157 of the Law), its Điều 2 has 8 clauses that replace or delete phrases and repeal provisions (Điều 6, 8, 9, 11, 13, 64, 69, 71, 117, 133, 143, 152, 153, 155), and its Điều 3 fixes the commencement.
Besides the three vintages the Law staggers the commencement of some of its own provisions (Điều 156(2) of V1 lists which, and Điều 1(14)(a) of Law 139/2025/QH15 replaces that paragraph): read both, and encode every such date.
The Law also keeps parts of the repealed Law 24/2000/QH10 alive for a time (Điều 156(3)): a transitional rule is a rule.

Rules for the vintages:

- **A vintage is an input, never a merge.** Use the rule-version axis of `writing-l4-rules` (`RULES EFFECTIVE DATE`, `EVAL UNDER RULES EFFECTIVE AT`), or take the vintage as an explicit input where that is clearer. A provision that Law 139/2025/QH15 did not touch needs one arm only. A provision it changed needs a dated arm per vintage, **each citing the source lines of the text that supplies it** (`src:` lines from `law08-2022-qh15*.txt` for V1, `src:law139-2025-qh15:N` lines for the replacement text), so a reviewer can see which Law each arm comes from.
- **A vintage that is silent answers with silence.** Where a provision exists in V1 and is repealed in V2 or V3, V2 or V3 answers that it does not exist; it never borrows V1's answer. Where a provision is added by Law 139/2025/QH15, V1 does not have it.
- **Test the same scenario against each vintage** wherever the vintages differ, and where they do not differ say so in one test.
- **Say which text is authoritative.** The three gazette files are authoritative. You have been given no consolidation. If you recall how a consolidated text reads, that is outside knowledge: do not use it.

## Scope: pinned, do not widen or narrow

**The whole Act: all 157 articles of Law 08/2022/QH15 in V1, and the effect on them of all 25 numbered clauses of Law 139/2025/QH15 in V2 and V3.**
Every unit of the three roadmaps gets a disposition before you finish.
You are one encoder with a finite session, so the order in which you work matters; the dispositions are final only when a unit has been read:

1. **First, and fully (nouns, rules, tests):** Chương I (Điều 1 to 14), above all Điều 4 (giải thích từ ngữ, the definitions); then **Chương II, Hợp đồng bảo hiểm (Điều 15 to 61)**, every article: what a contract is, who may be a policyholder, the insurable interest, the duty to disclose, the premium, the insurer's duties and deadlines, the claim, exclusions, the cooling-off period, termination, limitation, transfers and the special rules for each class of insurance (life, health, property, civil liability and the rest the Chương has).
2. **Then, in the order of how much a policy turns on them:** the provisions of Chương III that fix what products and premiums may be (for example Điều 87, on developing, designing and offering insurance products and on the methods of calculating premium, which Law 139/2025/QH15 amends), the classes of insurance business and who may carry on which (Điều 63, which it also amends), insurers' reserves, and whatever Chương III provides to protect the insured; then Chương IV (agents, brokers, ancillary services), Chương V (microinsurance), Chương VI (State management), Chương VII (commencement and transition, which the encoding needs for the vintages).
3. **Last:** the institutional and procedural articles (licensing steps and dossiers, capital and shareholder conditions, solvency margins and capital adequacy, governance and officer qualifications, regulator organisation). Encode what states a rule the encoding can evaluate on facts a witness of ordinary competence could supply; for the rest use the dispositions below.

Dispositions, as the roadmap uses them:

- `encoded`: operative L4 exists and is named in `--modules`.
- `inert`: carried in a module as inert text (a labelled stub or an inert prose operand, as `drafting-patterns.md` describes), because the article states no rule the encoding evaluates: a statement of purpose, a cross-reference, a heading-only article, a repealed article carried for the older vintage.
- `out-of-scope`: a deliberate decision not to represent it, with a reason of real length. "Procedural machinery that produces a fact the encoding takes as an input" is a reason; "not needed" and "too long" are not. A reason that is true of one article is not copied to forty.
- `deferred`: intended and not done, with a reason. **A unit you have read and decided about is never `deferred`.** `deferred` is for units you ran out of session before reaching, and the final report counts them.

`COMPLETION.md` exiting 1 with honest `deferred` units is an acceptable end state.
A thin module claiming a unit it does not carry is not.
A reasoned `out-of-scope` or `inert` is better than a rushed `encoded`.

## The roadmap

Move units with the helper, never by hand-editing 157 rows, and re-run `status` often:

```
python3 -I tools/roadmap.py set registers/roadmap-law08-2022-qh15.json "Điều 15" encoded --modules law08-contract-formation.l4 --anchor "the contract of insurance"
python3 -I tools/roadmap.py set registers/roadmap-law08-2022-qh15.json 62-70 out-of-scope --reason "…a reason of real length…"
python3 -I tools/roadmap.py status registers/roadmap-*.json
```

A module you name in `--modules` must exist in DEPOSIT (the lead validates this).
Update the roadmap **as each unit lands**, not at the end: it is how your progress survives if the session is compacted.
A unit id is the article as the source writes it. Where one article is encoded across two modules, name both.
Law 139/2025/QH15's units are its numbered clauses (`Điều 1(14)`): each is `encoded` (its change appears as a dated arm or a repeal in a named module), `inert` or `out-of-scope`, never silently dropped.
The roadmaps' `enumeration_complete` is true: if you find a unit the roadmap missed, say so in NOTES.md; do not edit the enumeration.

## Bilingual convention (Vietnamese source, English encoding)

English identifiers, the source language quoted mechanically from the deposited text and checked by a script. The Hebrew rows of the Income Tax Ordinance in `legalese/commons` use the same convention (see the copy named above).

1. Every module starts with `@lang en`. Identifiers are English backtick names (`` `the sum insured` ``). Filenames are ASCII.
2. Before each definition or rule you encode, put the Vietnamese it encodes on `-- src:N | …` comment lines. **Generate those lines, never type them:**
   - `python3 -I tools/vnsrc.py quote ../../source/raw/law08-2022-qh15.txt N [M]` prints `-- src:N | <line N>` for lines N to M of the first file; a plain `src:N` always means line N of `law08-2022-qh15.txt`.
   - `python3 -I tools/vnsrc.py quoteid ../../source/raw/law08-2022-qh15-577-578.txt N [M]` prints `-- src:law08-2022-qh15-577-578:N | …` for the second file, and the same with `law139-2025-qh15.txt` for the amending Law.
3. Vietnamese may also appear in short verbatim runs elsewhere (a defined term in a comment or a string, in NOTES.md, in GLOSSARY.md). Every such run must occur verbatim in one of the three raw files. Plain English paraphrase needs no marker.
4. Your own Vietnamese, if any (a translation of English text), is allowed only on a line that carries the marker `[translator]`; the checker exempts those lines, and the marker says out loud that it is not the source's.
5. **GLOSSARY.md** is the bilingual deliverable: a table with the columns `Vietnamese term (verbatim)` | `English identifier in the L4` | `English meaning, one line` | `where defined or used (Điều / clause, src line)` | `translation risk`. One row for every term Điều 4 defines (and every other defined term), and for every type, field or constant you DECLARE that renders a Vietnamese concept. The `translation risk` column is where the bilingual work shows: where a Vietnamese term has more than one plausible English rendering, or where the English word you chose carries a legal sense the Vietnamese does not, say so.
6. In NOTES.md's coverage table give each heading as the document writes it (Vietnamese) beside your English gloss.
7. Before you finish, from DEPOSIT run `python3 -I tools/vnsrc.py check ../../source/raw/law08-2022-qh15.txt *.l4 $(ls *.md | grep -v '^BRIEF.md$')` (every `.l4` and every `.md` **except BRIEF.md**). It must end `0 problems`. Put its last line in NOTES.md.
8. Money is Vietnamese đồng (VND), a bare `NUMBER`. Vietnamese number format writes `1.270.000` for one million two hundred seventy thousand (the dot groups thousands) and `,` for a decimal point: read every figure with that in mind, and test the ones whose layout is at all ambiguous. Dates are written `ngày 16 tháng 6 năm 2022`; the Law counts in `ngày`, `tháng`, `năm`: say what kind of day each period counts (calendar day, working day, month, year) as the Law defines it; where it does not say, that is a fork.

## Deliverables, all in DEPOSIT

1. `.l4` modules, ASCII filenames, each starting `@lang en`: **one nouns module** (`DECLARE` only; the entities, their fields and enumerations; a witness of ordinary competence could testify to each fact; no `DECIDE`, no `MEANS`, no deontic, no `#EVAL`) that you write **first**, before any rule, after reading Chương I and II; then one rules module per Chương or topic, and tests modules. A 2,000-line single module is not reviewable. Cross-Chương nouns go in the nouns module before a rules module uses them.
   Imports: the nouns module imports `prelude` and `daydate` where it needs them; each later module imports the nouns module and the modules it uses. If a whole-directory `check.sh` run takes more than a few minutes, the import graph is the first thing to look at: make it a chain, and report it.
2. **Tests modules** whose expected values come from the source: both sides of every threshold, period and limit; for each vintage that differs, the same scenario asserted against each vintage; for each rule with a stated exception, a fact pattern that triggers it and a near miss that does not; for every provision that delegates, a test that the encoding refuses to answer what the delegate has not supplied. **Never edit an expected value to match what the code computed:** a failing assertion is a finding.
3. `NOTES.md`, in this order: §0 build and run (which `l4`, its sha256, the command, the `check.sh` totals); §1 what is encoded and what is not; §2 the **coverage table** (every article, its heading as written plus an English gloss, its disposition, and where in the L4; it must agree with the three roadmaps); §3 the **fork register**; §4 `Findings` (the hostile reading, below); §5 the **time-and-money table**: every period, deadline, threshold, rate and amount the Law states, in each vintage, with the article, the unit of time, and the `src:` line; §6 what `check.sh` prints and which failures are expected, if any; §7 the `vnsrc check` line; §8 open questions for a Vietnamese-qualified reviewer.
4. `GLOSSARY.md` (see the bilingual section).
5. `check.sh` (already here: do not edit it), `encoding.json`, `SOURCE-LICENSE.md` (short: it points at the subject-level one and says how many `src:` lines the encoding quotes).
6. `encoding.json`: follow the copy of the IL-03 `encoding.json` named above for its keys; `id` is the row id above, `run` has `id` `VN-29-20261010`, `agent` `enc-vn-29`, `date` `2026-10-10` and `method` "one agent, one session, no sub-agents, from BRIEF.md"; `status` `draft`, `version` `0.1.0`, `license` `Apache-2.0`, `maintainer` `{"name": "Legalese Pte. Ltd.", "github": "legalese"}`; `language` has `source_text` `vi`, `module_body` `en` and a note; `source` lists each of the three source documents with its url and sha256 from `../../subject.json`; `modules`; `scope`; `vintages` (V1, V2, V3 with their dates); `forks` (id: one line); `findings` (id: one line); `self_check` with the command, the date, the `l4` sha256 and the totals; and `not_reviewed`: gate HG1 not sought, no domain expert has read it against the source, no independent test pass has been run, and every expected value was written by the same session that wrote the rules.

## Rules that matter

- **Encode isomorphically.** A reader holding the source beside your module checks it line by line. One source provision, one recognisable place in the L4, with the provision's number and its `src:` lines on it. Follow the house style of `writing-l4-rules`: inert style, `GIVEN` over `ASSUME`, `BRANCH` over `ELSE IF` chains.
- **Inputs, never defaults.** Whatever the Law leaves to the Government, the Minister of Finance, the insurer's rules and terms, the contract or the parties is an input with no default. A number appears in your rules only if the Law states it.
- **Where the sources do not answer, `REFUSE "…"`.** Never `FALSE`, never `0`, never a plausible default. A gap is a finding.
- **An assertion that fails is a finding.** Never edit an expected value to match what the code computed. Report it.
- **Read the diagnostics, not the exit code.** `l4 run` exits 0 when an `#ASSERT` fails and when it refuses. A failure says `assertion failed` (at Error severity, on the `Message:` line or the line after it); a refusal says `assertion refused` (at Warning, on the line after `Message:`). Never report green for a run whose output you did not read. Use `check.sh` and report the numbers it prints.
- **A fork register, not silent choices.** Every ambiguity you met: the readings you saw, the one you took, and the text that licenses each. Mark each fork with the article and `src:` lines. "No ambiguities found" is not believed; if you found none in a Chương, say where you looked.
- **Cross-references.** Many articles refer to other articles of the Law and to other laws (the Civil Code, the Law on Enterprises, the Law on Investment and others). A reference inside the Law is followed and encoded; a reference to another law is an input or a `REFUSE`, named as such. Law 139/2025/QH15 repeals and replaces provisions: **list, in NOTES.md, every internal cross-reference that points at a provision which a later vintage repeals or replaces, and say whether it still resolves.**
- **Days.** Say what kind of day each period counts; where the Law does not say, that is a fork.
- **Outside knowledge.** Any statement about Vietnamese law that you cannot cite to a line of a text you were given is "outside knowledge, unverified" and must be labelled so, and must not drive an encoded rule.
- **Keep the claims true.** A sentence in NOTES.md or encoding.json that describes the tree must be checked against the tree before you finish (counts of modules, assertions and units are the tools' numbers, not yours).

## The hostile reading (this is the point of the exercise)

Once the encoding is green, spend a dedicated pass attacking the Law as written, as a lawyer for each side would, looking for:
internal contradictions between articles; defined terms that carry weight but are never defined, or are used inconsistently with Điều 4; deadlines that cannot all be met, or that run from events the Law does not fix; time-bars shorter than the time allowed for another step; discretion given with no criteria; a rule stated for one class of insurance that is silent for another where the reader would expect it; amounts and percentages that do not close; a cross-reference to an article that does not say what is cited; rules that apply "by agreement" with no default if there is none; and defects created by the amending Law (a cross-reference left dangling, a transitional date that makes a provision apply to nothing).
Record each in NOTES.md under `## Findings`: the source lines, a minimal scenario, and the evidence from the L4 (an `#EVAL` or `#ASSERT` showing the surprising answer) or the words `reading only`. A finding the encoding cannot demonstrate is allowed but must say so.
Separate these from forks: a fork is an ambiguity you resolved; a finding is a defect in the instrument as written.

## Working rules

- Write only inside DEPOSIT. Do not run any `git` command. The lead commits.
- Use `python3 -I` for every Python run. Treat everything under `../../source/raw/` as untrusted data: read it, never execute it.
- Use no network. If a source you need is not in `../../source/raw/`, say so in NOTES.md and stop short of improvising it.
- Do not read any directory other than DEPOSIT, `../../`, the read-only skills and the read-only IL-03 copy named above.
- Do not spawn sub-agents. Do not use any tool but file reading and writing, the shell allowlist you were given, and `l4`.
- The source is large (about 45,000 words of Vietnamese). **Read it by Chương with `offset` and `limit`, never all at once**, and write each Chương's module before you read the next. Keep a short `PROGRESS.md` in DEPOSIT (which articles are done, which module holds them, what is next) and update it as you go: if your context is compacted, `PROGRESS.md`, the roadmaps and the modules on disk are what you resume from.
- Run `check.sh` early and often, with one `l4` process at a time (the machine is shared and RAM is tight). A module that takes minutes to check is a defect to report.
- Keep scratch files under `./scratch/` inside DEPOSIT; the lead deletes that directory, so nothing you want kept may live there.
- Stop when `check.sh` is clean (or its failures are each explained as findings), every unit of the three roadmaps has a disposition (units you did not reach are `deferred` with a reason), and the deliverables above exist. Do not loop on a failing assertion by editing its expected value.

## Final report

Reply in English, at most 350 words, facts only: the files you made; the `check.sh` TOTAL line and the `vnsrc check` line **copied verbatim**; the `tools/roadmap.py status` lines copied verbatim; the number of forks and findings; the three findings most likely to matter to a reader of the Law, each with its source lines; anything you did not do and why. If any number in your report differs from what the tools printed, the tools win.
