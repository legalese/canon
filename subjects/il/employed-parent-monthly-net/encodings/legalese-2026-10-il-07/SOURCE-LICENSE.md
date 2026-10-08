# Source license

This row composes encodings of two Israeli statutes and quotes them only in short runs, copied from the deposited texts.
The terms those texts carry are recorded where the texts are deposited, and this file adds nothing to them:

- **Income Tax Ordinance [New Version]**: `../../../income-tax-ordinance-new-version/SOURCE-LICENSE.md`.
- **National Insurance Law [Consolidated Version], 5755-1995**: `../../../national-insurance-law-consolidated-version-5755-1995/SOURCE-LICENSE.md`.

Both say: no copyright in the statute text (Copyright Act 5768-2007, s 6); the deposited files are unofficial Hebrew Wikisource consolidations, with Wikisource's editorial additions, where any survive, under CC BY-SA 4.0.

## The vendored modules

The `.l4` files this directory's `vendor.sh` copies in are the six composed rows' own modules, under those rows' licence (Apache-2.0, each row's `encoding.json`).
(Version 0.2.0: and the modules of row IL-08's two halves, under the same licence, each half's `encoding.json`. Row IL-08's Income Tax Ordinance half quotes the Tax Authority's 2026 withholding booklet and Amendment 262, as its own `SOURCE-LICENSE.md` records; nothing more is quoted here.)
They are not committed here (`.gitignore`); `VENDORED.sha256` records which bytes were composed.

## Other material quoted

- **Israel Tax Authority, monthly withholding booklet for 2026** (one sentence, PDF p. 8, in `il07-published-figures.l4`).
  A government publication, not among the classes s 6 of the Copyright Act excludes from copyright; so, as row IL-01 does for the same booklet, only a short quotation is carried, and the file is not deposited.
- **Economic Efficiency Law (Budget Year 2026), 5786-2026** (cited by section and page in `NOTES.md` and `RECONCILE.md`, not quoted at length): a statute, no copyright (s 6). Not deposited; its URL, capture and sha256 are in `NOTES.md` section 7.
- **National Insurance Institute** rates pages: no text quoted; the employee health rates the tests apply are cited from row IL-04's `NOTES.md` section 7.

## Status

No source's terms are undetermined: each is recorded above or in the file it points to.
