# Encoding brief: National Insurance Law ss 342, 348 and Schedule K, in L4 (row IL-05)

You are producing an L4 encoding of three provisions of the National Insurance Law from its sources.
This brief is the whole specification.
Read it fully before opening any source.

## The subject

**חוק הביטוח הלאומי [נוסח משולב], התשנ״ה–1995** — National Insurance Law [Consolidated Version], 5755-1995.

Chapter 15 of the Law (insurance contributions) makes residents and employers pay contributions to the National Insurance Institute on income.
This row encodes three of its provisions:

- **s 342** (החייבים בתשלום דמי ביטוח, who is liable to pay contributions): the self-employed and those who are neither employee nor self-employed pay for themselves; an employer pays for its employee and deducts the employee's share from the wage; the coordination of an employee with several employers; and the reduced rate for an employee who is also self-employed.
- **s 348** (סכום מרבי, סכום מזערי וסכום שלא יובא בחשבון): the income above a maximum is disregarded, non-work income up to 25% of the average wage is disregarded, and income below a minimum is raised to it; with two deeming rules for the unemployed and for volunteers and yeshiva students.
- **Schedule K** (לוח י״א, maximum and minimum income for contributions): the figures s 348 reads, per month, quarter and year, for four kinds of insured person.

The row depends on row IL-04 of the same subject (s 1 definitions, s 334, s 337, Schedule J), which encodes the rates these provisions apply.

| vintage | source | where |
| --- | --- | --- |
| as amended at retrieval (into 5786, 2026) | Hebrew Wikisource consolidation, retrieved 2026-10-06, sha256 `78bf47ee…2a97` | `../../registers/source-bundle/national-insurance-law-consolidated-version-5755-1995.he.wiki.txt` |

The Hebrew text is authoritative; the file is an unofficial consolidation, an aid.
Its editors' notes (`{{ח:הערה|…}}`) are aids too, and each use of one is cited.
Line numbers of that file are the pinpoint citations.

## Scope — pinned, do not widen or narrow

s 342 in full (lines 3658-3675); s 348 in full (lines 3762-3769); Schedule K in full, with its definitions (lines 4751-4773).
Schedule K1 (line 4775) only if s 342 or s 348 refers to it.
The s 1 definitions these provisions use, as far as they use them.
Everything else is out of scope; where these provisions refer to another provision, take its result as an input with a citation, or import row IL-04's encoding of it.

## Deliverables, all in this directory

1. `.l4` modules with ASCII filenames, identifiers in English, `@lang en`, Hebrew only in mechanically generated `-- src:N |` comments.
   The nouns in one module; rules split along the source (Schedule K, s 348, s 342); tests in their own module.
2. A tests module asserting what the SOURCE says, and what the National Insurance Institute's published figures say where the Law computes a figure it does not print.
3. `NOTES.md`: scope, a coverage table, a fork register, an answer table, open questions, nouns to reconcile with other rows.
4. `check.sh`, `encoding.json`, `SOURCE-LICENSE.md`.

## Rules that matter

- **Isomorphic**: one source provision, one recognisable place in the L4, with its line cited.
- **Vintages are inputs, never merged.** The row answers contribution periods from January 2026 (say why in NOTES.md); s 348(e) carries a permanent text and a temporary text, which are dated arms.
- **Where the sources do not answer, `REFUSE "…"`**, never `FALSE` or `0`.
- **Figures the Law does not print** (the basic amount, the average wage, the minimum wage) come from an official publication with URL, retrieval time and sha256, or are inputs with no default.
- **A failing assertion is a finding.** Never edit an expected value to match the code. Checks that fail because the SOURCE is inconsistent go in their own module, counted in `check.sh` and `encoding.json`.
- **Read the diagnostics, not the exit code.**
- Money is new Israeli shekels (NIS), a bare `NUMBER`. Nothing is rounded unless the source says so.
- **Semi-cleanroom** (ruled 2026-10-06): nothing from the Axiom Foundation or any RuleSpec encoding is read.

## Toolchain

`/Users/mengwong/.local/bin/l4` (cabal store `jl4-0.1-0ee0100b`, sha256 `64bbcb15…e9eca118`), `JL4_LIBRARY_PATH` unset.
`l4 run FILE` typechecks and evaluates every `#EVAL` and `#ASSERT`; `check.sh` reads the diagnostics.
