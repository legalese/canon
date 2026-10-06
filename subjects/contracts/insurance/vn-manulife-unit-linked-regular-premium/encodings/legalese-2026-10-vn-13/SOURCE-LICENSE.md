# Source licence — encoding row `legalese-2026-10-vn-13`

The source is Manulife Vietnam's contract terms for its regular-premium unit-linked product (`manulife-maxx`), whose licence position is recorded at the subject level: `../../SOURCE-LICENSE.md`.
In short, the terms are **undetermined**: no copyright or reproduction notice was found, the PDF and its text rendering are not held in this repository, and quotation as short `-- src:N |` comment lines rests on Meng's ruling of 2026-10-06 recorded there, not on the issuer's terms.

**How much this encoding quotes.** The `.l4` modules carry **782** `-- src:N |` lines, quoting **770** distinct lines of the 983 non-blank lines of `../../source/raw/manulife-maxx.txt` (about 78%).
The brief scoped the whole document, and each encoded clause is quoted once, before the rule that encodes it, one source line per comment line; inert passages (marketing prose, the Annex 1 fund descriptions, definitions of documents) are quoted by their first line only, ending "…".
That is most of the document, because most of the document is operative. The subject-level ruling covers clause-level quotation and not reproduction of the document, so the lead should weigh this figure; removing every `src:` line leaves the rules and the tests standing.

The `tools/gen_tables.py` output also quotes the 36 lines of the Article 13.9 a table and the six lines of the Annex 1 equity bands; they are included in the counts above.
Short Vietnamese terms also appear in `NOTES.md`, `GLOSSARY.md` and `COMPARABLES.md`, each checked verbatim against the source by `tools/vnsrc.py`.

The encoding itself (the `.l4` modules, the tools, `check.sh` and the notes) is Apache-2.0, the licence of this repository. That does not extend to the quoted source text.
