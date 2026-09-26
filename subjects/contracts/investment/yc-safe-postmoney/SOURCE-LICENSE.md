# SOURCE-LICENSE — Y Combinator post-money SAFE

**Status: DETERMINED.** Unlike the `sg/` rows, whose source terms are an open question, this
subject's terms are stated on the face of every document and are reproduced below. Read this
file before reproducing anything under `source/`: **attribution here discharges a licence
CONDITION and must not be removed.**

This is the **subject-level** file, and it governs the source text, which is shared by every
encoding row (directory conventions §6). Each row under `encodings/` carries its own
`SOURCE-LICENSE.md` saying what that row does under these terms; those files state the row's
own conduct and defer to this one for the terms themselves.

## The grant, verbatim

Every one of the ten `.docx` under `source/docx/` carries this sentence in its first-page
footer. Extracted 2026-09-04 by reading each file's `word/footer*.xml` parts; the per-file
strings are in [`source/footers.json`](source/footers.json). This is the US valuation-cap
form's copy:

> © 2023 Y Combinator Management, LLC.  This form is made available under a Creative Commons Attribution-NoDerivatives 4.0 License (International): https://creativecommons.org/licenses/by-nd/4.0/legalcode.  You may modify this form so you can use it in transactions, but please do not publicly disseminate a modified version of the form without asking us first.

The other nine are **identical modulo the year**, checked by normalising the year out and
comparing all ten: the four Pro Rata Side Letters read `© 2018` (United States) or `© 2021`
(Singapore, Canada, Cayman Islands) in place of `© 2023`. Nothing else differs. One
typographic aside: in the Canadian SAFE the footer paragraph begins with a space before the
`©`, so the raw paragraph in `word/footer3.xml` and the trimmed
`copyright_and_license_line` differ by that character; both are in `source/footers.json`,
under `parts` and at the top level respectively.

Two characters that do not survive casual copying: the string contains **non-breaking spaces**
(U+00A0) after `LLC.` and after the URL, and `source/footers.json` holds it byte-exact.

The licence is [Creative Commons Attribution-NoDerivatives 4.0
International](https://creativecommons.org/licenses/by-nd/4.0/legalcode) — the URL the
footer itself gives. The publisher's reason for adopting it is on the record in the SAFE
User Guide, Appendix III, as a Version 1.0 change:

> The safe is expressly copyrighted and made available under the Creative Commons
> Attribution-No Derivatives 4.0 License.
> Location: First page footer
> Notes: … People have periodically asked us if they could re-publish the safe documents in
> educational or reference materials, and our replies typically tracked the terms of the
> Creative Commons license mentioned, i.e. provide attribution and please do not change the
> form without asking us first. We also wanted to make sure that if other people publish the
> safe documents in other public-facing channels (e.g. other websites, circulars, etc.), they
> publish the actual safe documents, rather than modified versions that might confuse people
> into thinking that they are viewing or using the "standard" versions.

That paragraph is the interpretive key to everything below: the concern the publisher names
is a **modified form circulating as the standard one**.

## What is done here under it

- **Verbatim deposit with attribution.** `source/docx/` holds the ten forms and the User
  Guide byte-exact, and `source/md/` holds a mechanical Markdown rendering of each, verbatim
  in its text. Attribution is recorded in the repository [`NOTICE`](../../../../NOTICE) and
  the licence line is preserved in `source/footers.json` — pandoc drops footers, so without
  that file the Markdown would silently lose the notice.
- **Transaction fills.** Filling the blanks and bracketed terms to make an instrument for a
  transaction is what the form is for, and the form says so in its own preamble: the parties
  represent that neither "has modified the form, except to fill in blanks and bracketed
  terms". A filled SAFE is a use of the form, not a modified form.
- **Derived templates, proven to round-trip.** `templates/holes.json` maps each bracketed
  placeholder and each underlined blank, by position, to a hole name. A template derived
  from it must reproduce the deposited Markdown byte-for-byte when rendered with every hole
  set back to its original placeholder text. That check is the mechanical form of "unmodified
  except to fill in blanks": a template that passes it differs from the published form in no
  character outside a blank.
- **Refusing unpublished cells.** Y Combinator publishes six SAFEs — three US variants and
  one each for Singapore, Canada and the Cayman Islands, all cap-only. The five cells off
  that diagonal (a Singapore discount SAFE, an MFN SAFE for Canada, and so on) **are not
  synthesised here and must not be**. Synthesising one would produce precisely the modified
  version circulating as standard that the Appendix III note asks people not to disseminate.

## What is not done here

- **No modified form is publicly disseminated.** Nothing in this tree publishes an altered
  SAFE. Where the encoding needs to quote the form, it quotes it as a quotation with
  attribution, in comments, and never re-issues the document with the text changed.
- **No YC branding or endorsement is claimed.** CC BY-ND requires attribution and forbids
  distributing an adaptation; it grants no trademark rights and implies no approval. Nothing
  here is a Y Combinator product or is endorsed by Y Combinator.
- **No permission is sought or assumed for a variant.** The footer says to ask first. Nothing
  in this row has been asked, so nothing in this row relies on having been granted anything
  beyond the licence text.

## The open question, recorded and not resolved

**Is an L4 formalisation of the form an "adaptation" under CC BY-ND 4.0?** The licence
forbids distributing "Adapted Material" — material derived from the licensed work "in which
the Licensed Material is translated, altered, arranged, transformed, or otherwise modified in
a manner requiring permission under the Copyright rights held by the Licensor". Two readings
are available and this file takes neither:

1. **Not an adaptation.** The encoding is a new work expressing propositions, in a different
   language, for a different purpose; it is closer to a summary, an index or a piece of
   software about the form than to a translation of it, and its expressive choices are the
   encoder's own.
2. **An adaptation.** "Translated … or otherwise modified" is broad, and a
   clause-by-clause formalisation that tracks the form's structure section by section is at
   least arguably a translation of it into another notation.

Nothing here decides between them, because deciding it takes legal advice this repository
does not have, and because the question is more interesting than any answer that could be
asserted in a corpus note. It is recorded as **R9** in the subject's specification
(`specs/todo/yc-safe/SPEC.md` §2 and §11 in `legalese/l4-ide`), which answers the licence
question **as to conduct** — the four practices listed above — and leaves the
adaptation characterisation open. Two practical consequences hold either way and are
observed here regardless of the answer: attribution is given, and no modified form is
disseminated.

*(This section states two readings of a licence. It is not legal advice, and nothing in this
tree checks it.)*

## Attribution for NOTICE

The [`NOTICE`](../../../../NOTICE) entry for this subject reads, and must continue to read,
that the SAFE documents under `source/` are © Y Combinator Management, LLC, made available
under CC BY-ND 4.0 International, with a link to the licence. That attribution is a
**condition** of the grant, not a courtesy: removing it removes the permission.
