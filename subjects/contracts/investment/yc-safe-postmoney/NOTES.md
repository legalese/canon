# NOTES — contracts/investment/yc-safe-postmoney

**Status: `draft`.** This file documents the **source deposit** — everything under `source/`,
`registers/source-bundle.json`, `templates/holes.json`, and the subject descriptor. All of it
is the publisher's text and facts measured from it.

An encoding row, `encodings/legalese-2026-09/`, and `registers/fork-register.json` landed in
the same change **from another hand**, after this file was first written. Nothing here
authored them and nothing here makes any claim about them: for what that encoding is, what it
covers and what it does not, read its own `encoding.json`, `NOTES.md` and `SOURCE-LICENSE.md`.
The two halves of the change are described in two places on purpose, and this half is the
source deposit.

This is the **first row filed under `subjects/contracts/`**, so it also seeds
[`../../GENRES.md`](../../GENRES.md) with the four genres the directory conventions name.
Read `docs/directory-conventions.md` §3 for why
the contracts tree is keyed on genre rather than jurisdiction; §8.4 of that document names
this exact subject as its worked example of a standard form. It is **not on this branch** —
`git show docs/directory-conventions:docs/directory-conventions.md`.

## What this row is

The Y Combinator post-money SAFE — Simple Agreement for Future Equity — is a **standard
form**, so `form_kind` is `"standard-form"` and there is no citation, no extent and no
enacting authority. It has a publisher (Y Combinator Management, LLC), editions, and a
licence printed in its own footer.

The instrument is unusual among the subjects in this corpus, and the reason is one sentence
of its own preamble:

> This Safe is one of the forms available at http://ycombinator.com/documents and the Company
> and the Investor agree that neither one has modified the form, except to fill in blanks and
> bracketed terms.

That sentence makes the form's fill-in surface a closed set. The blanks are the parameter
set, the bracketed terms are the variation points, and every other character is invariant.
`templates/holes.json` is the measurement of that surface — see below.

## The product matrix: six SAFEs, not twelve

```
{us} × {cap, discount, mfn}  ∪  {sg, ca, ky} × {cap}
```

Three economic variants exist for the United States; Singapore, Canada and the Cayman
Islands get **valuation-cap only**. The five off-diagonal cells — a Singapore discount SAFE,
an MFN SAFE for Canada, and so on — are not published, and this row deliberately does not
contain them. Anything built on this subject must **refuse** those cells rather than
synthesise one, because a synthesised cell is exactly the "modified version" the licence
footer asks people not to disseminate. See [`SOURCE-LICENSE.md`](SOURCE-LICENSE.md).

The four Pro Rata Side Letters are a separate instrument, one per jurisdiction, optional per
investor. They became separate at post-money v1.0: Appendix III records "Deletion of the
post-conversion round pro rata right; addition of optional conversion round pro rata side
letter."

## What the sidecar does NOT have

Recorded plainly so no reader infers more than is here. This list is about the subject as a
whole, and it was written for a tree with no encoding row in it; where the encoding row
supplies something, that row's own `NOTES.md` is what speaks for it.

- **No `projections/`.** Nothing has been projected to DMN, BPMN, AKN or anything else, at
  either level.
- **No `report/` and no `gates/`.** There is no conversion report and **no human review**:
  HG1 has not been sought and no signature exists for this subject.
- **No `templates/*.mustache`.** `templates/` holds only `holes.json`, the measured map. The
  templates are derived from it by a tool that lives in `legalese/l4-ide`, not here.
- **No fidelity claim from this deposit.** The source half of this change asserts provenance
  and digests, and nothing else. It does not assert that any encoding matches the form.

**Any golden in this tree is point-in-time.** canon has no CI: nothing in this repository
re-runs `l4`, re-derives a projection or re-checks a golden. A golden deposited here records
what the tools produced on the day it was written, against the compiler of that day, and it
will silently rot. That is a property of the repository, not of this subject; say what
version produced it, or the file is not evidence.

## Two derivations, and the one thing the derived layer loses

`source/md/` holds one Markdown file per `.docx`, produced by:

```
pandoc <file>.docx -t gfm --wrap=none
```

Checked 2026-09-04 under **pandoc 2.9.2.1**: re-running that command over all ten forms
regenerates the deposited `.md` **byte-for-byte**. (The same check covers the four pre-money
forms in the sibling row — fourteen files, fourteen identical.) A different pandoc will
almost certainly produce different output; the version is part of the claim.

**pandoc drops headers and footers entirely**, and that is where the licence line and the
version stamp live. `source/footers.json` is the repair: every `word/header*.xml` and
`word/footer*.xml` part of every file, per paragraph, reconstructed from the OOXML runs in
document order. Reconstruction is necessary because Word splits these strings across runs —
`"Version 1."` + `"2"` — so no single run holds the value. Word fields are emitted once as
`{FIELD <instruction>}` and their **cached results are discarded**, because the page number
Word last rendered is a rendering artifact and not text of the form.

Anything that reproduces a form from `source/md/` **must put the footer back**. Attribution
is a condition of the CC BY-ND grant, not a courtesy.

## `templates/holes.json`: measured, not authored

The file lists, per form, in document order:

- **`brackets`** — every bracketed placeholder, exactly as it appears in the Markdown
  (pandoc escapes the form's square brackets, so the literals read `\[Company Name\]`,
  `$\[\_\_\_\_\_\_\_\_\_\_\_\_\_\]`, `\[*100 minus the discount*\]`, `\[**COMPANY\]`), plus
  the one brace placeholder described below — merged into one list by byte offset.
- **`blanks`** — every `<u>…</u>` whose content is whitespace only. The forms also use `<u>`
  to underline sub-headings ("Equity Financing", "excluding"), and the whitespace test is
  what separates a blank from a heading.

Bracket accounting is complete in every file: the count of `\[` equals the count of `\]`
equals the number of matches, and no unescaped `[…]` survives the conversion, so nothing was
skipped. Hole names come from the placeholder literal where it is self-describing, from the
enclosing sentence where an underscore run is not (`THIS CERTIFIES THAT` → `purchaseAmount`,
`Post-Money Valuation Cap` → `valuationCap`, `Province of` / `Courts of` →
`governingProvince`), and from the printed label for blanks (`By:` / `Name:` / `Title:` /
`Address:` / `Email:`, an empty label meaning a continuation of the line above).

**Five hole names were added beyond the vocabulary this deposit was given**, each because
the measurement found a fill-in position the list did not cover:

| added                                             | why                                                                                                                |
| ------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `companyRegistrationNumber`                       | Singapore only, and **not a bracket**: the form prints `Company Registration number {. . .}`. The only brace-delimited hole in the corpus. |
| `companySignatureLine`, `investorSignatureLine`   | the manuscript signature blanks after `By:`. Not for a generator to fill, but listing them keeps the positional map complete. |
| `companyAddressLine2`, `investorAddressLine2`     | the unlabelled continuation blank under each `Address:` line. The form gives two physical lines for one address.       |

**A hole name may repeat within a form**, and the `index` is the identity. `companyName`
appears twice on most SAFEs; `governingProvince` appears twice on a single Canadian line
("laws of the Province of `[_______]`" and "Courts of `[_______]`"), one value filled twice.

**The placeholder casing is not consistent across the forms**, which a generator has to
decide about, so it is recorded rather than normalised. The cover title reads
`[Company Name]` on the US cap form, `[**COMPANY NAME**]` on the discount and MFN forms,
`[COMPANY NAME]` on the Singapore form, `[Company Name]` on the Cayman form, and
`[company name]` — lower case — on the Canadian form. Each entry carries a
`placeholder_case` field; `companyName` versus `companyNameCaps` follows it.

## Findings worth knowing before you rely on something

**1. The MFN form is stamped Version 1.3, and no changelog describes a 1.3.** The User
Guide's Appendix III stops at Version 1.2 (February 2023), and Appendix III itself says
"Version numbers are stamped on the upper right-hand corner of each form of the post-money
safe" — so the stamp is the publisher's own authority on which edition you hold. The
deposited MFN form's header reads `Version 1.3`. The guide's own Q7 quotes that form's
header as "MFN ONLY Version 1.1". So the MFN instrument has moved at least twice since the
guide's text was written and at least once since the last published changelog entry, with no
note of what changed. **Nothing here reconstructs the diff — only the stamp is evidence.**
Do not treat the 1.2 changelog as covering the MFN form deposited here. The specification
that commissioned this deposit states "The fetched US forms are v1.2"; that is right for the
cap and discount forms and wrong for MFN, and this note is the correction.

The other stamps, all measured: `Version 1.2` (US cap, US discount), `Singapore Version
1.2`, `Canada Version 1.2`, `Cayman Version 1.2`, `Version 1.0` (US Pro Rata Side Letter),
and **no stamp at all** on the three non-US side letters.

**2. The deposited filenames depart from the naming rule, deliberately.** Directory
conventions §7 rule 1 requires every path component to match `^[a-z0-9][a-z0-9-]*$`, and
these files are named `Postmoney Safe - Valuation Cap Only - FINAL.docx` — spaces, capitals,
parentheses. The publisher's filename is the last path segment of the asset URL and is how
the form is identified on the publisher's own page, so slugging it would break the identity
between the deposited bytes and the URL that served them, and would silently rename a
document that other people cite by name. The names are kept and the departure is recorded
here rather than left for a linter to discover. If the rule is enforced later, the fix is a
mapping table, not a rename.

**3. Singapore §5(f) reads "the laws of the Singapore".** Quoted verbatim in `subject.json`;
it is the publisher's text, not a transcription slip on our side.

**4. The Canadian form carries a law firm's document-management stamp.** `word/footer4.xml`
holds `LEGAL_1:65957856.2` beside a `DOCPROPERTY "DocsID"` field — residue from the drafting
firm's DMS that the publisher did not strip. It is in `source/footers.json` because the
extraction is complete, not because it is part of the form.

**5. The Singapore form's one brace hole is easy to miss.** `Company Registration number
{. . .}` is the only fill-in in the whole corpus that is not a square bracket or an
underlined blank. A bracket-only scan will silently drop it.

## What the schema asked that a form cannot answer

`registers/source-bundle.json` validates against the l4-ide source-bundle schema, which was
written for **enacted law**. Two of its required sweeps have no referent here, and both are
answered with a stated reason rather than an invented value:

| rule                    | what it wanted                         | what was written, and why                                                                                                          |
| ----------------------- | -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `in-force-or-absent-reason` | the publisher's currency banner, verbatim | `in_force_absent_reason`. **No in-force date is asserted and none was invented.** A form has editions, not commencement; the publisher's own way of telling you which text you hold is the version stamp, and those are recorded per file. |
| `covers-or-absent-reason`   | the date range of law each document states | `covers_absent_reason` on all eleven documents, for the same reason: an edition is a publication event, not a period of legal force, and the release dates come from the changelog rather than from the instruments. |

Two further shapes, recorded so a reader does not read an absence as an oversight:

- **No document carries role `instrument`.** That role is for the text a subject is *made
  under*. A privately published contract form is made under nothing; naming one would be a
  fabrication. The ten forms are `current`; the User Guide is `guidance`, on the reasoning
  the `us/chubb-hospital-cash` bundle uses for an answer key — the issuing body's own
  non-binding reading of its own instrument.
- **`annotations` is `[]` on every document, and that is a finding.** There is no publisher
  apparatus over a `.docx`: no amendment markers, no modification list, no commencement or
  extent notes. The schema cannot express "the inventory is complete and it is empty" — an
  `annotation_group` requires at least one marker — so the explicit empty array plus this
  sentence is the whole record.

**Validator verdict, 2026-09-04.** Run as
`register-validate.mjs source-bundle registers/source-bundle.json registers/fork-register.json`,
which validates the peer in its own right and then joins on it:

```
register-validate: fork-register …/registers/fork-register.json
  18 rule(s) checked, 1 skipped
  skip cross-refs-resolve — no external-modifications file was given
register-validate: source-bundle …/registers/source-bundle.json
  12 rule(s) checked, 1 skipped
  skip assembled-digest-matches — no assembled artifact is declared
register-validate: ok
```

The one skip on the bundle is `assembled-digest-matches`: this subject declares no single
assembled artifact, because it has eleven source documents rather than one assembled text.
`digest-matches-local-file` **did** run against the deposited files and passed for all
eleven, and `peer-subjects-agree` passed — both registers name subject `yc-safe-postmoney`.
Without the peer argument the bundle alone reports `11 rule(s) checked, 2 skipped … ok`, the
second skip being `peer-subjects-agree` with nothing to join on. The fork register is not
this deposit's file; its verdict is reported here only because the join needs it.

## The licence question, recorded and not resolved

The forms are © Y Combinator Management, LLC under CC BY-ND 4.0 International, and the
attribution is a **condition**, recorded in the repository `NOTICE`. Whether an **L4
formalisation** of the form counts as an "adaptation" under a NoDerivatives licence is a real
question that this deposit **records and does not answer** — it is ruling **R9** in
`specs/todo/yc-safe/SPEC.md` (`legalese/l4-ide`), answered as to conduct and open as to
characterisation. [`SOURCE-LICENSE.md`](SOURCE-LICENSE.md) sets out both readings and the
four practices that hold either way. Anyone about to derive something from this row should
read that file first.

## Provenance in one paragraph

The ten forms and the User Guide were fetched from `https://www.ycombinator.com/documents`
and re-verified on 2026-09-04 by re-fetching all eleven assets and comparing sha256 against
the deposited copy: **all eleven matched**, from both `https://www.ycombinator.com/assets/ycdc/`
and the `//bookface-static.ycombinator.com` host the page's own links point at. Digests for
every deposited file, source and derived, are in `source/SHA256SUMS`
(`shasum -a 256 -c SHA256SUMS` from `source/`).
