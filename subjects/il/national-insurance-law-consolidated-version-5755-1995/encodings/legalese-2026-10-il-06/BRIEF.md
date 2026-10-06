# Encoding brief: National Insurance Law, ss 66-68 (the child allowance: entitlement, the count of children, the amount), in L4

Row IL-06, run id `IL-06-20261006`, encoder `enc-il-06` (one session, no sub-agents).
This brief is the whole specification.
It restates the lead's task in the template of `l4-ide/skills/encoding-a-subject/assets/brief-template.md`, so that a reviewer or an independent test author can work from it alone.

## The subject

**חוק הביטוח הלאומי [נוסח משולב], התשנ״ה–1995** — the National Insurance Law [Consolidated Version], 5755-1995 (Sefer HaChukim 5755 p. 210), as amended.
It is the central Israeli social-security statute: it imposes insurance contributions and creates the benefit branches.
This row covers the core of Chapter 4 (פרק ד׳: ביטוח ילדים, children's insurance), Mark B (סימן ב׳: קצבת ילדים, the child allowance):

- **s 66 (זכות לקצבת ילדים, right to a child allowance)**: an insured parent is entitled to a monthly child allowance for each child, except an insured parent who has income chargeable to additional tax within the meaning of s 121B of the Income Tax Ordinance;
- **s 67 (מנין ילדים, counting children)**: a child is counted with one insured parent only, and the rule for choosing which;
- **s 68 (סכום הקצבה, the amount of the allowance)**: the monthly allowance for each child in the parent's count equals the basic amount fixed for that child; a higher amount for a fourth or later child born before 1 June 2003; and a supplement for the third and fourth child of a parent paid an Income Support benefit or a maintenance payment.

Read with them, and encoded only as far as they need:

- **s 65 (פרשנות)**, the Chapter's definitions of "מבוטח" (insured) and "ילד" (child), and s 65(b) on a child abroad;
- **s 1**, the definitions of "ילד" (child) and of "הסכום הבסיסי" (the basic amount), paragraph (2), whose limbs (a), (b) and (c) fix the basic amount for the child allowance by the child's place in the count.

There is one vintage of the text in the sources:

| vintage | source | where |
| --- | --- | --- |
| AS AMENDED AT RETRIEVAL | Hebrew Wikisource consolidation, raw MediaWiki, retrieved 2026-10-06, sha256 `78bf47ee29a300d51c5c7646cf85992d7de78aa1380bd8460a4a18265f552a97` | `../../registers/source-bundle/national-insurance-law-consolidated-version-5755-1995.he.wiki.txt` |

Hebrew is authoritative.
The file is an **unofficial consolidation**; the consolidation's `{{ח:הערה|…}}` notes (for instance the indexed amounts printed beside the basic amounts) are **aids, not law**.

**When that text took effect.** s 68 and s 1 paragraph (2) have their present wording from the Economic Efficiency Law (Legislative Amendments for Achieving the Budget Targets for Budget Years 2015 and 2016), 5776-2015, s 28, which s 29(a) of that Law commences on 1 May 2015.
None of ss 65-68 carries an amendment tag later than that Law (תשע״ו־3) in the deposited text.
So the deposited text answers days **from 1 May 2015**; earlier days are declined by name.

**The figures.** The basic amounts are printed in s 1 as 150, 188 and 140 shekels and updated each 1 January by the consumer price index under s 1's updating clause, which is row IL-04's.
The figure in force on a day is therefore not in the text.
It is taken from the National Insurance Institute's published table of basic amounts, fetched on 2026-10-06 and cited by URL and sha256, and kept in its own module, which says on its face that it is not encoded law.
The rules themselves take the three basic amounts as an input.

## Scope — pinned, do not widen or narrow

- s 66; s 67(a), (b); s 68(a), (b) (with (b)(1) deleted), (b)(2), (b)(3), (c), and (d)-(יא) (repealed).
- s 65(a) "מבוטח" and "ילד", and s 65(b), as far as ss 66-68 need them.
- s 1 "ילד", and s 1 "הסכום הבסיסי" paragraph (2)(a)-(c), as far as ss 65-68 need them.

Out of scope, with the reason recorded in NOTES.md: s 69 onward (in particular s 69A, which displaces ss 67-68 for an insured man with children by more than one woman, and s 71, a parent who died or ceased to be insured, both of which are reachable and are declined by name); s 72 (the months for which the allowance is paid); s 238 ("housewife"); s 381 and the rounding regulations; s 1's updating clause (row IL-04); the Income Tax Ordinance s 121B (row IL-03); the Income Support Law; the Maintenance (Assurance of Payment) Law; and the regulations under s 65.
Where one of these feeds a provision in scope, its result is an **input**, with a citation, never an encoding.

## Deliverables, all in this directory

1. `.l4` modules with ASCII filenames, each starting `@lang en`: a nouns module (`DECLARE` only); one rules module per section (s 1 paragraph (2), s 65, s 66, s 67, s 68); a module for the period the text answers; a module of the Institute's published figures; a module that answers for a family on a day; and a tests module.
   Identifiers are English backtick names; Hebrew is quoted in `-- src:N |` comments generated mechanically from line N of the source file.
2. A tests module asserting what the SOURCES say: both sides of the 18th birthday, of 1 June 2003, of the three-month absence, of 1 May 2015 and of each 1 January in the figures table; every place in the count from first to sixth; each limb of s 67(b) and each case it does not answer; s 66's exception; s 68(c) for two, three and four children; and the Institute's own published per-child amounts for 2018, 2020, 2024, 2025 and 2026.
3. `NOTES.md`: scope, a coverage table with no row left `deferred`, a fork register, an answer table, what `check.sh` prints, open questions.
4. `check.sh` (the skill's template), `encoding.json`, `SOURCE-LICENSE.md`.

## Rules that matter

- **Encode isomorphically.** One source provision, one recognisable place, with an `@ref` naming the section and the line of the source file.
- **Do not invent a number.** A basic amount in force is an input; the Institute's published figures are a separate module with their provenance; a figure found only in a consolidation note is not encoded.
- **Where the sources do not answer, `REFUSE "…"`**; never `FALSE`, `0` or a plausible default.
- **A failing assertion is a finding.** Never edit an expected value to match what the code computed.
- **Read the diagnostics, not the exit code**: run `check.sh` and report the numbers it prints.
- Money is new Israeli shekels (NIS) per month, as a bare `NUMBER`. Amounts are **before rounding** under s 381, which is not encoded.
- Semi-cleanroom (ruled 2026-10-06): nothing from the Axiom Foundation or any RuleSpec encoding may be read.

## Toolchain

`/Users/mengwong/.local/bin/l4` (it has no `--version`; NOTES.md section 0 identifies the build used), with `JL4_LIBRARY_PATH` unset.
`l4 check FILE` type-checks; `l4 run FILE` also evaluates every `#EVAL` and `#ASSERT`.
