# Encoding brief: National Insurance Law, ss 1 (as needed), 334 and 337 and Schedule J (the contribution rates), in L4

Row IL-04, run id `IL-04-20261006`, encoder `enc-il-04` (one session, no sub-agents).
This brief is the whole specification.
It restates the lead's task in the template of `l4-ide/skills/encoding-a-subject/assets/brief-template.md`, so that a reviewer or an independent test author can work from it alone.

## The subject

**חוק הביטוח הלאומי [נוסח משולב], התשנ״ה–1995** — the National Insurance Law [Consolidated Version], 5755-1995, ס״ח תשנ״ה, 210 (further publication at 327), as amended into 5786 (2026).
It is a Knesset Law in consolidated-version form and carries both sides of Israeli social insurance: the benefit branches and the insurance contributions (דמי ביטוח) that fund them.
This row covers the core of the contributions arithmetic:

- **s 334 (פרשנות, interpretation for Chapter 15)**: the terms "payment period", "payment date" and "reduced collection threshold" (מדרגת גבייה מופחתת), the sum below which contributions are charged at the reduced rates, and the rule that a person whose wage is fixed by a Law or a Knesset resolution is an employee for the Chapter;
- **s 337 (שיעור דמי ביטוח, rate of insurance contributions)**: an employee's monthly contributions, and another insured person's annual contributions, are the percentages in Schedule J of their income; the Minister may change the rates by order; a change carries through proportionally to the deduction from an employee's wage;
- **Schedule J (לוח י׳)**: the rates, per branch of insurance, per column of insured person (employee, self-employed, neither), on the part of income above and up to the reduced collection threshold, with the employee's wage deduction and the Treasury allocation beside them; printed twice, as a temporary provision for 2025-2026 and as the permanent text, with further temporary figures for 2024-2027 in item 4;
- **s 1 (הגדרות)**, only as far as the three provisions above use it: "employee", "employer", "self-employed person", "the average wage" (with "compensation" and "the compensation rate"), "the index", "tax year", "the Minister".

There is one vintage in the sources:

| vintage | source | where |
| --- | --- | --- |
| AS AMENDED AT RETRIEVAL | Hebrew Wikisource consolidation, raw MediaWiki, retrieved 2026-10-06, sha256 `78bf47ee29a300d51c5c7646cf85992d7de78aa1380bd8460a4a18265f552a97` | `../../registers/source-bundle/national-insurance-law-consolidated-version-5755-1995.he.wiki.txt` |

Hebrew is authoritative.
The file is an **unofficial consolidation**; the official version is the publication in Reshumot plus every amending Law.
Its `{{ח:הערה|…}}` notes are the editors' additions: some carry figures for a year ("(נקוב לשנת 2025; בשנת 2026, 7,703 ש״ח)"), and some carry the periods of temporary provisions ("(הוראת שעה לשנים 2025–2026)", "(הוראת שעה בשנים 2024 עד 2027: 2.06)").
They are **aids**, and the encoding says which of them it relies on and why (NOTES.md, assumptions).
Earlier vintages of these provisions are not in the sources: **what they do not show, you do not know.**

## Scope — pinned, do not widen or narrow

- s 334, every part: (a) chapeau, its three definitions and paragraphs (1)-(2) of the third; (b).
- s 337, every part: (a)(1), (a)(2), (b), (c).
- Schedule J, every part: the headings and references, both tables (temporary 2025-2026 and permanent), all ten items and the totals row of each, all nine figure columns, and the temporary figures noted in item 4 and the totals.
- s 1: every defined term is listed in the coverage table; those the provisions above use are encoded.

Out of scope, with the reason recorded in NOTES.md: s 335 (who pays which branch), s 336 (payment periods), s 340 (work-injury and maternity rates), s 342 and s 348 and Schedule K (row IL-05), ss 66-68 (row IL-06), Schedule A, s 2 (exceptional pay months in the average wage), s 32 (the Treasury allocation), and everything else in the Law.
Where a provision in scope refers to one of these, its result is an **input**, with a citation, never an encoding.

## Deliverables, all in this directory

1. `.l4` modules with ASCII filenames, each starting `@lang en`: a nouns module (`DECLARE` only), a module for s 1, one for s 334, a generated data module for Schedule J's two tables, one for the Schedule J rules, one for s 337, a module of figures published by the National Insurance Institute (with provenance), a tests module, and a tests module that is expected to fail by an exact count.
   Identifiers are English backtick names; Hebrew appears only in `-- src:N |` comments copied mechanically from the source and in short runs checked to occur in it verbatim.
2. Tests asserting what the SOURCE says, and what the regulator prints: the composite rates the National Insurance Institute publishes for each column, its worked example for a person who is neither employee nor self-employed, both sides of the reduced collection threshold, each dated arm of Schedule J and the years either side of it, each limb of the "self-employed" definition at its boundary, and the printed totals of Schedule J against the sum of its items.
3. `NOTES.md`: scope, a coverage table with no row left `deferred`, a fork register, an answer table per year, what `check.sh` prints, open questions, nouns to reconcile at IL-07.
4. `check.sh` (the skill's template), `encoding.json`, `SOURCE-LICENSE.md`, and the `tools/` that quote the source and generate the Schedule J tables.

## Rules that matter

- **Encode isomorphically.** One source provision, one recognisable place, with an `@ref` naming the provision and the line of the source file.
- **The year of the contribution month is the vintage selector.** The encoding answers contribution months from January 2026, the date from which the deposited text of s 334 and Schedule J is in force, and declines (`REFUSE`) earlier months rather than borrowing the amended text.
- **Do not invent a number.** The consumer price index, the average wage, and the reduced collection threshold for any year after 2026 are inputs, or are taken from a fetched official publication with its URL, retrieval time and sha256.
- **A dash in Schedule J is not a zero.** Where the schedule prints "–" for a branch a person pays, the encoding declines.
- **Where the sources do not answer, `REFUSE "…"`**; never `FALSE`, `0` or a plausible default.
- **A failing assertion is a finding.** Never edit an expected value to match what the code computed.
- **Read the diagnostics, not the exit code**: run `check.sh` and report the numbers it prints.
- Money is new Israeli shekels (NIS), as a bare `NUMBER`; contributions are per month; Schedule J's figures are stored as the schedule prints them (percentages) and divided by 100 only where they are applied.
- Semi-cleanroom (ruled 2026-10-06): nothing from the Axiom Foundation or any RuleSpec encoding may be read.

## Toolchain

`/Users/mengwong/.local/bin/l4` (it has no `--version`; NOTES.md section 0 identifies the build used), with `JL4_LIBRARY_PATH` unset.
`l4 check FILE` type-checks; `l4 run FILE` also evaluates every `#EVAL` and `#ASSERT`.
