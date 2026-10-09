# Encoding brief: Income Tax Ordinance special rates and other regimes, and the Rounding Order 5746-1986, in L4

Row IL-30, run id `IL-30-20261008`, encoder `enc-il-30` (one session, no sub-agents).
This brief is the whole specification.
It restates the lead's task in the template of `l4-ide/skills/encoding-a-subject/assets/brief-template.md`, so that a reviewer or an independent test author can work from it alone.

## The subjects

**פקודת מס הכנסה [נוסח חדש]**, the Income Tax Ordinance [New Version] (the Ordinance), in the Hebrew Wikisource consolidation deposited at `../../registers/source-bundle/income-tax-ordinance-new-version.he.wiki.txt` (sha256 `b87f2cf437ccfed35c3164681f4fc7ee015a111633454622751930c8894b81b6`).
**צו מס הכנסה (כללים לעיגול סכומים), התשמ״ו–1986**, the Income Tax (Rules for Rounding Amounts) Order 5746-1986 (the Order), deposited at `../../registers/source-bundle/regulations/income-tax-rules-for-rounding-amounts-order-5746-1986.he.wiki.txt` (sha256 `3418c9bdc4ae0c18ddc947425f6a7bf690282cdc317320521f12707db39c293b`).
**חוק מיסוי מקרקעין (שבח ורכישה), התשכ״ג–1963**, the Real Estate Taxation (Appreciation and Purchase) Law (the RE Tax Law), deposited at `../../../real-estate-taxation-law-5723-1963/registers/source-bundle/real-estate-taxation-law-5723-1963.he.wiki.txt` (sha256 `aa4217b3b917a48356d8069b9e9510694b456506ec77c9b4527a99c6c16dd1ca`).
All three are unofficial consolidations of the text as amended at retrieval (2026-10-06 to 2026-10-08).
Hebrew is authoritative.
There is one vintage per source, and nothing here is vintage-merged: a date earlier than the text's own change date is declined (NOTES.md, assumption A6).

## Scope, pinned from the row and the gap records

The row (BACKLOG IL-30) names: Ordinance ss 91, 122, 125B, 125C; s 8(c); s 88; the RE Tax Law's rates; ss 64A1, 64A2; s 57; ss 55(b), 60A(2); s 120B(d) with the Order.
It records gaps at IL-03/NOTES.md:39 and :56, IL-02/NOTES.md:71, IL-01/NOTES.md:90 and :95.
In priority order, which the lead set because IL-03 depends on the first:

1. s 120B(d) and the Order, ss 1 to 17.
2. ss 122, 125B, 125C, 91 (with s 88, which the three rate sections use).
3. s 8(c).
4. ss 64A1, 64A2.
5. ss 55(b), 60A(2), 57.
6. the RE Tax Law's rates (ss 6, 9 and 48A).

The coverage table in NOTES.md lists every provision of each, with a disposition and, for anything not encoded, the reason.

## Deliverables, all in this directory

1. `.l4` modules with ASCII filenames, each starting `@lang en`: nouns modules (`DECLARE` only), one rules module per provision, one tests module per rules module, and a small module of the shared "highest layer" arithmetic.
2. `NOTES.md`: scope, the coverage table, the fork register, the assumptions, an answer table, what `check.sh` prints, findings, the inputs the capstone does not supply, open questions.
3. `check.sh` (the skill's template), `encoding.json`, `SOURCE-LICENSE.md`, `tools/` (the mechanical quoter and the Hebrew checker).

## Rules that matter

- **Isomorphic.** One source provision, one recognisable place, with an `@ref` naming the section and the source line.
  The Hebrew in a `-- src:N |` comment is generated mechanically from line N of the one source file the module names.
- **Never invent a number.**
  A figure that is only published (an index reading, an order, a figure the Tax Authority publishes) is an input with no default.
  The s 126(a) rate, the highest rate of s 121, the scale of s 121, the credit points and deductions of a kibbutz member, the s 94B profits and the housing-services index are all inputs.
- **Where the text is silent or two readings are arguable and give different answers, one named switch, declined by default.**
  Ruled by Meng on 2026-10-08 (SHRUG).
  The default declines only where the readings give different answers to the question asked; where they agree, the rule answers.
  The fork register in NOTES.md lists every one.
- **A failing assertion is a finding.**
  Every expected value was worked out by hand from the Hebrew text before it was run.
- **Read the diagnostics, not the exit code.**
  `check.sh` counts failed, refused and satisfied assertions per module.
- Semi-cleanroom (ruled 2026-10-06): nothing from the Axiom Foundation or any RuleSpec encoding was read.
- Git is read-only for this row; the lead commits.

## Toolchain

`l4` is `~/.local/bin/l4`, the cabal-store build `jl4-0.1-6df1397b`, sha256 `f0759b2ef2f1d1b2a577c68f059c54f487de9d913553fc9f0d9bf0f7f5dab0d8`.
Money is new Israeli shekels as a bare `NUMBER`; rates are percent literals as printed; a percent literal that is an argument of a mixfix call is parenthesised, because `10% \`keyword\`` otherwise parses as a postfix operator.
