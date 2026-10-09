# Encoding brief: Income Tax Ordinance ss 39A, 39B, 40A to 40F, 41, 44, 45, 46 to 46C, 47A; s 35(e) and the rules of 5738-1977; s 47(d) and the Regulations of 5740-1980; the Retirement Age Law 5764-2004, in L4 (row IL-27)

Row IL-27, run id `IL-27-20261008`, encoder `enc-il-27` (one session, no sub-agents).
This brief restates the lead's task in the shape of `l4-ide/skills/encoding-a-subject/assets/brief-template.md`, so that a reviewer or an independent test author can work from it and the sources alone.
The lead's task is `l4-pipeline/BACKLOG.md`, row IL-27, and the brief for rows IL-25 to IL-35.
The gaps this row closes were recorded at `l4-pipeline/findings/il-2026-10-08/not-encoded.txt` (ITO ss 39A, 39B: IL-08/NOTES.md and IL-01/NOTES.md; ss 40A to 40F; ss 44, 45, 46 to 46C; s 47A; the retirement age taken as an input; ss 35(e) and 47(d) refused in row IL-08).

## The subject

**פקודת מס הכנסה [נוסח חדש]**, the Income Tax Ordinance [New Version], as consolidated on Hebrew Wikisource and deposited at `../../registers/source-bundle/income-tax-ordinance-new-version.he.wiki.txt` (retrieved 2026-10-06, sha256 `b87f2cf4…94b81b6`).
Beside it, two instruments made under it, in `../../registers/source-bundle/regulations/`: **כללי מס הכנסה (זיכוי לעולים במקרים מיוחדים), תשל״ח–1977** (sha256 `260b2b8b…186c3`), made under s 35(e), and **תקנות מס הכנסה (ניכוי תשלומים בעד תגמולים או קיצבה), תש״ם–1980** (sha256 `1de85699…34240`), made under s 47(d).
And the **חוק גיל פרישה, התשס״ד–2004**, at `../../../retirement-age-law-5764-2004/registers/source-bundle/retirement-age-law-5764-2004.he.wiki.txt` (sha256 `633aa70f…1dfa1bd`), which defines the retirement age that ITO s 1 and s 37 take.
Hebrew is authoritative; each file is an unofficial consolidation stated as amended at retrieval.

## Scope, as pinned from the text and the row

**Encoded, each section as its own module with its own tests and its own coverage row:**
ss 39A (discharged soldier), 39B (reserve service as a fighter), 40A (divorcee who has married again), 40B (youth), 40C (academic degree), 40D (vocational studies), 40E (no double credit; 40F repealed), 41 (spouse married for part of the year), 44 (relative kept in an institution), 45 (disabled child), 46 (donations), 46A (overall ceiling), 46B (base for advance payments; 46C repealed), 47A (National Insurance contributions); s 35(e) with the rules of 5738-1977 (rules 2 and 3); s 47(d) with the Regulations of 5740-1980 (regulations 1 and 2); the Retirement Age Law, ss 3 and 6 and the Schedule's Parts A and B.
The order is the order the capstone (row IL-07) is likeliest to need them: ss 39A, 39B, 40A to 40F, 41, 44 to 46C, 47A, then the rules and the Retirement Age Law.

**Out of this row, with a reason (NOTES.md has the table):** the Retirement Age Law's compulsory and early retirement ages (nothing in the Ordinance in scope turns on them); the Law of Return, the Discharged Soldiers Absorption Law, the Reserve Service Law and the Military Jurisdiction Law, whose definitions the caller states as facts; the regulations of 5756-1996 under ss 44 and 45 and of 5751-1991 under s 47A(c), which are not in the source bundle; the National Insurance Law and the Parallel Tax Law, whose contributions are inputs.

**Refused by name where a provision needs a text we do not hold ("needs a source"):** the commencement of s 39B (an amending Law of 5786 not in the bundle); the text of ss 40C and 40D for studies that ended before 2014 and 2018; Part B of the Schedule for a woman born before May 1947 (the deposited table has no row); the regulations of 5756-1996.

Not edited: the capstone, and every existing row.
Rows IL-01, IL-03 and IL-08 are vendored beside this row (sha256 in NOTES.md) and never edited.
Integrating this row into the capstone is a later version of IL-07.

## Deliverables, all in this directory

1. `.l4` modules: a nouns module (`DECLARE` only); a tax-years module (with the gates every section asks); a published-figures module (the consolidation's own notes, not law); one rule module per section or instrument; fourteen tests modules; the vendored modules.
2. `NOTES.md`: coverage table (every provision in scope: encoded, inert, out-of-scope with a reason, or needs a source), fork register, assumptions, answer table, what `check.sh` prints, open questions, inputs the capstone does not supply, nouns to reconcile.
3. `check.sh` (the skill's), `encoding.json` (status draft, HG1 not sought), `SOURCE-LICENSE.md`, and `tools/` (the quotation generator and checker; one script does both).

## Rules that matter

- Isomorphic: one source provision, one recognisable place, its line number in an `@ref` or a `src:` comment.
- Hebrew is quoted only mechanically: `src:N` lines are generated from the Ordinance by `tools/srcquote.py`, `ext:[TAG:N]` lines from the other three sources, and every other run of Hebrew is checked by `tools/srcquote.py --check` against the union of the four.
- Where the text does not decide, `REFUSE "…"` with a name; never a guessed 0 or FALSE.
- POLICY (Meng, SHRUG, 2026-10-08): where the text is silent or two readings are arguable and give different answers to a question someone would ask, ONE named switch, default DECLINE, the other readings kept by name and tested; the default declines only where the readings differ.
- Never invent a number: a figure that is only published goes in a clearly marked module with its source and hash; a credit point's value is an input, taken in the tests from row IL-01's published figures.
- Tests come from the source; a failing assertion is a finding; every expected value is worked by hand before the run.
- Imports resolve only beside the importing file, so the minimum of rows IL-01 and IL-08 is vendored with a recorded sha256.
- Semi-cleanroom with respect to the Axiom Foundation: nothing of theirs read, and no row's "Comparison with Axiom" section read.
