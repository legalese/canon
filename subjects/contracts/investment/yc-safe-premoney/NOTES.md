# NOTES — contracts/investment/yc-safe-premoney

**Status: `draft`, and this row is SOURCES ONLY.** There is no `encodings/` directory, no
`templates/`, no `cases/`, no `projections/`, no `report/` and no `gates/`. This row exists
so the original safe's text has a home with a path, a digest and a licence note. It makes no
claim about the instrument beyond what the deposited bytes say.

## What this row is, and why it is a separate leaf

The **pre-money SAFE**, which Y Combinator's own User Guide calls "the original safe": the
form introduced in late 2013 and superseded on 2018-09-28 by the post-money SAFE. Canon's
directory conventions §3 settle the filing directly — "distinct instruments in a family
(pre-money vs post-money SAFE) are distinct leaves" — so this is a sibling of
[`yc-safe-postmoney`](../yc-safe-postmoney), not a version of it. (That document,
`docs/directory-conventions.md`, is on the `docs/directory-conventions` branch and not on
this one; `git show docs/directory-conventions:docs/directory-conventions.md`.) The relationship is
recorded as `superseded_by` metadata in `subject.json`, because a path may not carry a
version (§5) and because these are two instruments, not two vintages of one.

Four US variants were published: valuation cap only (the Primer's "Standard Safe"), discount
only, **valuation cap and discount**, and MFN. The third has no post-money successor — it
was withdrawn at post-money v1.1 on 2021-08-28, and the User Guide's Appendix III explains
why. There were no non-US forms.

## Why there is no encoding here

The pre-money arithmetic belongs to the **paper track**, not to the generator this corpus
row was deposited alongside. These are the texts **Ron van der Meyden** (UNSW Sydney) and
**Michael J. Maher** (Reasoning Research Institute) analysed, in the project that produced
*Simple Agreements for Future Equity — not so simple?* (April 2023) and the 2025 Springer
book *Simple Agreements for Future Equity (SAFE), Smart Contracts for Venture Finance*. Their
analysis is of the pre-money valuation-cap form with a single SAFE outstanding, and its
concluding paragraph names automated analysis over a formal description of the contract as
future work. Encoding these forms is therefore a piece of work with a specific interlocutor
and a specific comparison to make, and doing it as a by-product of the post-money build would
serve neither. Deferred deliberately; ruled **R8** in `specs/todo/yc-safe/SPEC.md`
(`legalese/l4-ide`) and set out in that file's `SPEC-NOTES.md` §2.

The post-money row's own encoding will also need these texts for a different reason. The User
Guide's Appendix II carries a worked example headed "EXAMPLE 2 – combination of pre-money and
post-money safes", so half of that example cannot be asserted against a post-money encoding
until this leaf is encoded too.

## Provenance: everything came from the archive

Y Combinator no longer hosts these forms — `https://www.ycombinator.com/documents` offers
only the post-money set — so every document here is `retrieval_method: "archive"` with its
capture URL and 14-digit timestamp in
[`registers/source-bundle.json`](registers/source-bundle.json). All five were re-fetched from
the Internet Archive on 2026-09-04 and every sha256 matched the deposited copy, from both the
plain capture URL and the byte-exact `id_` form.

**The captures are not a single vintage.** The four forms are 2014-10-06, taken within about
ten minutes of one another; the SAFE Primer is 2017-09-10, nearly three years later. They are
deposited together because they are one product line, not because they were published
together, and nothing here establishes that the Primer describes exactly these four files.

**A Wayback lookup quirk, recorded so the next person does not conclude "not archived".** The
availability API at `http://archive.org/wayback/available` normalises the queried URL in a way
that is case-sensitive in the first path token. These return the capture:

```
?url=ycombinator.com/docs/SAFE_cap.docx
?url=ycombinator.com/docs/SAFE_discount.docx
?url=ycombinator.com/docs/SAFE_Primer.rtf
?url=ycombinator.com/docs/safe_cap_discount.docx
?url=ycombinator.com/docs/safe_MFN.docx
```

while `SAFE_cap_discount.docx` and `SAFE_MFN.docx` — the spellings the real URLs use —
return an **empty** `archived_snapshots` object. The captures exist in every case; only the
lookup differs. The `archive_url` on each document in the source bundle was fetched directly
and is what should be used.

## Two derivations

- **`source/md/`** — `pandoc <file>.docx -t gfm --wrap=none`. Checked 2026-09-04 under
  **pandoc 2.9.2.1**: re-running the command regenerates all four deposited `.md`
  byte-for-byte. A different pandoc will not.
- **`source/docx/SAFE_Primer.txt`** — **pandoc cannot read RTF**, so the Primer was rendered
  with macOS `textutil -convert txt` instead. The `.rtf` is the deposit; the `.txt` is a
  convenience rendering of it, and it is the only file in either row produced by a
  platform-specific tool.

Both derivations are digested in `source/SHA256SUMS` alongside the retrieved bytes
(`shasum -a 256 -c SHA256SUMS` from `source/`).

## What the documents say about themselves: nothing

`source/footers.json` is the same extraction the post-money row carries, run over these four
files to answer one question. **Every `word/header*.xml` and `word/footer*.xml` part of all
four `.docx` is empty except a page-number field.** No version stamp, no copyright notice, no
licence line, and the string "Y Combinator" appears nowhere in any of the four forms.

That is the material difference from the sibling row, and it has two consequences:

1. **Source terms are UNDETERMINED**, not permissive. The CC BY-ND footer was added at
   post-money v1.0 in 2018; these 2014 captures predate the licensing decision.
   [`SOURCE-LICENSE.md`](SOURCE-LICENSE.md) sets out the measurement and what does and does
   not follow from it. Silence is not a grant.
2. **There is no edition axis to read off the instruments.** `subject.json` records "late
   2013" because that is what the User Guide says — "In late 2013, Y Combinator introduced
   the original safe" — and it says no more. **Do not sharpen that to a month.** What is
   actually pinned is the capture: this row speaks for the 2014-10-06 state of four URLs, and
   whether the text moved between introduction and capture has not been checked.

## Drafting details that will matter to whoever encodes this

- **Governing law is a bracketed default, not a blank.** §5(f) reads "the laws of the State of
  `[California]`" — the form suggests an answer rather than leaving a hole. The post-money US
  forms replaced this with `[Governing Law Jurisdiction]`.
- **The incorporation state is not a hole at all.** The preamble reads "a Delaware
  corporation" as fixed text. The original form assumed a Delaware company under California
  law and invited the parties to overtype.
- **The "unmodified except to fill in blanks" representation is absent.** That sentence is a
  post-money v1.0 addition (Appendix III, first entry). The sentence that makes the
  post-money form's fill-in surface a closed set does not constrain this one, which is worth
  knowing before treating a pre-money hole map as authoritative in the same way.
- **The placeholders are styled differently.** Where the post-money forms print
  `[Investor Name]` and `[Date of Safe]`, these print the italic `[*investor name*]`,
  `[*amount*]`, `[*date*]`, `[*company name*]`. No `templates/holes.json` is deposited for
  this row, since nothing here is generating from it yet.

## Validator verdict, 2026-09-04

`register-validate.mjs source-bundle` on `registers/source-bundle.json` reports
`11 rule(s) checked, 2 skipped … ok`. The two skips are `assembled-digest-matches` (no single
assembled artifact is declared — this row has five source documents) and `peer-subjects-agree`
(no peer register was given; there is no fork register). The `digest-matches-local-file` rule
**did** run against the deposited files and passed for all five.
