# Encoding brief: Income Tax Ordinance ss 33A, 34, 36 and 36A (credit points), in L4

This brief is the whole specification for row IL-01 (run `IL-01-20261006`).
It was written by the encoder, `enc-il-01`, from the lead's task statement, before any L4 was written.
An independent test author should be able to work from this file and the source alone.

## The subject

**פקודת מס הכנסה [נוסח חדש]** — Income Tax Ordinance [New Version] (דמ״י תשכ״א, 120; 5721-1961), as amended.
A Mandate-era ordinance in a Hebrew New Version, amended by ordinary Knesset amending Laws.

This row encodes the **credit points** (נקודות זיכוי) that open Chapter Three of Part C (פרק שלישי: ניכויים, זיכויים וקיצבאות ילדים):
the definitions of a credit point and of an allowance point (s 33A), and the three unconditional personal credits — two points for an Israeli resident individual (s 34), a quarter point "travel credit" for an Israeli resident individual (s 36), and half a point for a woman (s 36A).

There is one vintage.

| vintage            | source                                                                                     | where                                                                                       |
| ------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------- |
| AS AMENDED (2026)  | Hebrew Wikisource consolidation, raw MediaWiki, retrieved 2026-10-06, sha256 `b87f2cf4…b81b6` | `../../registers/source-bundle/income-tax-ordinance-new-version.he.wiki.txt` (read-only)     |

Hebrew is authoritative.
The file is an **unofficial consolidation** stated as amended at retrieval (the amendment list runs into תשפ״ו, 2026); it is not a historical vintage.
Israel publishes no free official consolidated text; the official version is the 1961 New Version plus every amending Act.
Editorial notes inside `{{ח:הערה|…}}` templates are Wikisource's, not the Knesset's, and are never law.

Line numbers in that file are the pinpoint citations used throughout: s 33A at 1561–1567, s 34 at 1569–1570, s 36 at 1593–1594, s 36A at 1596–1597; s 1 (definitions) from 106.

**Numbers that are not statutory constants** — the indexed value of a credit point for a tax year — are fixed by s 120B, which row IL-03 owns.
This row takes that value as a `GIVEN` input with no default.
Where an official Israel Tax Authority publication states the value for a year, the row may cite it (URL, retrieval date, sha256) and use it in tests, labelled as a published figure and not as encoded law.

## Scope — pinned, do not widen or narrow

**Encode:** s 33A (both definitions), s 34, s 36, s 36A.

**Read, do not encode:** the s 1 definitions these sections use ("תושב ישראל", "שנת מס", "אדם", "חבר בני אדם"); s 120B (the indexation that fixes a credit point's value — IL-03's).

**Out of scope, but a rule in scope can reach it:** s 48 (the Minister's power, exercised by an order of 5755-1995 per a Wikisource note, to apply ss 34, 36 and 37 to Area residents who are not Israeli citizens) and s 48A (the power, exercised by regulations of 5775-2014, to disapply the chapter's credits to a foreign worker).
Where an answer turns on either, the rule must `REFUSE` with a named reason, never answer.

**Out of scope (IL-08 and others):** ss 35, 35A, 37, 38, 39, 39A, 39B, 40–40F, 41, 41A, 42–48A and every other credit section; s 66 (IL-02); ss 120B, 121, 121B (IL-03).

## Deliverables, all in this directory

1. `.l4` modules with ASCII filenames, `@lang en`, English identifiers that read like the statute, Hebrew quoted as inert strings copied mechanically from the source (checked by `render_source.py --check`).
   A nouns module (`DECLARE`s only) that every other module imports; one rule module for s 33A and one for ss 34, 36, 36A; a module of published figures (not law); a tests module.
2. A tests module whose expected values come from the source text and from the Israel Tax Authority's own published statement of how a credit point is applied — never from the code.
   Cover each section on both sides of every condition, the refusals, and the aggregate the Ordinance itself names elsewhere ("נקודות הזיכוי שעל פי סעיפים 34 ו־36", s 134A(2)).
3. `NOTES.md`: scope, a coverage table (every provision met, with a disposition), a fork register, an answer table (points per section per kind of person; the credit-point amount per tax year as published), what `check.sh` prints, open questions, and "Nouns to reconcile at IL-07".
4. `check.sh` from the `encoding-a-subject` skill, run as `L4=/Users/mengwong/.local/bin/l4 ./check.sh`.
5. `encoding.json` (status `draft`, HG1 not sought) and `SOURCE-LICENSE.md`.

## Rules that matter

- **Encode isomorphically.** One section, one `§§` heading, the source's own limbs in the source's order, an `@ref` with the source line on every rule.
- **Where the sources do not answer, `REFUSE "…"`** — never `FALSE`, never `0`, never a plausible default. A refusal goes in return position, and the limbs the model can answer come first.
  "The section does not apply to this person" is the law's own answer and is an ordinary value (no points), not a refusal.
- **No invented numbers.** The credit-point value is an input. The editorial figures in the Wikisource notes (2,820; 2,904; 235; 242) are not law and are not used as values.
- **An assertion that fails is a finding.** Never edit an expected value to match what the code computed.
- **Read the diagnostics, not the exit code.** Report the numbers `check.sh` prints.
- Amounts are new Israeli shekels (NIS), as bare `NUMBER`s.
- Fractions are written as the source writes them: `1/4`, `1/2`.

## Toolchain

The binary is `/Users/mengwong/.local/bin/l4` (a symlink into a cabal store build `jl4-0.1-0ee0100b`; it has no `--version`, so `NOTES.md` records its sha256 at the time of each run).
Leave `JL4_LIBRARY_PATH` unset.
`l4 check FILE` typechecks; `l4 run FILE` also evaluates every `#EVAL` and `#ASSERT`.

## Semi-cleanroom rule (ruled by Meng, 2026-10-06)

Nothing from the Axiom Foundation may be read: not `/Volumes/transcend/src/Axiom/`, not any `rulespec-*` repository or directory, not github.com/TheAxiomFoundation, not axiom.org encodings, not any `docs/ENCODING-GAPS.md`, `.axiom/` directory or `data/coverage/tax-benefit-source-map.json`, not `l4-ide/specs/research/AXIOM-*`, and no web search for RuleSpec or Axiom encodings of Israeli tax law.
Their encoding of these sections is the comparison oracle.
Everything else is allowed: the source, official Israeli government publications, Legalese's own corpus, and the L4 skills.
