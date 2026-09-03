# SOURCE-LICENSE — Y Combinator pre-money SAFE (the "original safe")

**Status: UNDETERMINED.** This file records what the documents say, which is nothing, and
the question that leaves open. **Do not read the absence of a restriction here as a grant.**
The sibling row [`yc-safe-postmoney`](../yc-safe-postmoney/SOURCE-LICENSE.md) is
`DETERMINED`; the difference between the two is the whole point of this file.

## What the documents actually say

**Nothing.** Measured 2026-09-04 over all four `.docx` under `source/docx/`:

- **Headers and footers are empty.** Every `word/header*.xml` and `word/footer*.xml` part in
  all four files contains no text but a page-number field. The full extraction is in
  [`source/footers.json`](source/footers.json), and it is a table of empty lists.
- **The body carries no notice.** A case-insensitive search of `source/md/` for `copyright`,
  `©`, `licen[cs]e` and `creative commons` returns nine hits across the four files, and every
  one is ordinary contract language about the *company's* affairs, not about this document:
  the permits-and-licences limb of the §3(c) no-conflict representation, the
  patents-trademarks-copyrights-licenses list in the §3(e) intellectual-property
  representation, and — in the MFN form only — "technology license" inside the §2 definition
  of Subsequent Convertible Securities. There is no `©` character in any of the four.
- **The publisher is not named at all.** The string `Y Combinator` does not appear anywhere
  in any of the four forms.

So: no copyright notice, no licence reference, no attribution requirement, no permission.
The forms state no terms.

## Why they state none, which is a dated fact and not an oversight

The Creative Commons Attribution-NoDerivatives 4.0 footer that the post-money forms carry
was **added in 2018**, and the publisher says so. The SAFE User Guide's Appendix III lists
it among the Version 1.0 changes, released 9/28/2018:

> The safe is expressly copyrighted and made available under the Creative Commons
> Attribution-No Derivatives 4.0 License.
> Location: First page footer

These captures are from 2014-10-06, four years earlier. They predate the licensing decision.
A reader who knows the post-money forms and assumes the same terms apply here would be
wrong, and that is the specific mistake this file exists to prevent.

## What follows, and what does not

- **Silence is not a grant.** Absent terms, the default is ordinary copyright in whatever is
  copyrightable in the text. Nothing is asserted here about what that permits.
- **What this row does is deposit and cite.** The four forms and the Primer are held under
  `source/` as retrieved, unmodified, with their provenance in
  [`registers/source-bundle.json`](registers/source-bundle.json). There is **no `encodings/`
  row** under this subject, so no derived work exists here to license.
- **The question is open in a way the post-money row's is not.** For the post-money forms
  the open question is a characterisation question (is an L4 formalisation an "adaptation"
  under a licence we hold?). Here the prior question has not been answered: what terms apply
  at all. That must be settled before this row moves off `mengwong/drafts`, and before
  anything is derived from these texts.
- **A further point specific to an archive deposit.** The bytes came from the Internet
  Archive rather than from the publisher. The Archive's own terms govern how it serves them;
  they do not enlarge whatever rights subsist in the underlying documents, and no claim to
  the contrary is made here.

## Attribution

No entry has been added to the repository [`NOTICE`](../../../../NOTICE) claiming a licence,
because there is none to claim. An entry **is** added recording the deposit and stating that
the terms are undetermined — the same shape the `sg/pdpa-2012` and `sg/penal-code-1871` rows
use. The forms are Y Combinator's work and are credited as such as a matter of accuracy, not
because any instrument here requires it.
