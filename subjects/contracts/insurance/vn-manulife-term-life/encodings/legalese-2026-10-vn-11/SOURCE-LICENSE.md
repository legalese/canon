# Source licence: row VN-11

The source is Manulife Vietnam's term life product terms; its licence position is in the subject's own `../../SOURCE-LICENSE.md`.
In short: the terms are **undetermined**, no licence is claimed, the PDF and its text rendering are not held in this repository, and quoting encoded clauses as short `-- src:N |` comment lines rests on Meng's ruling of 2026-10-06 recorded there.

What this encoding quotes, counted on 2026-10-06 with `grep -hE -- "--\s*src:[0-9]+\s*\|" *.l4 | sed -E 's/.*src:([0-9]+).*/\1/' | sort -u | wc -l` (and `tools/vnsrc.py check` agrees: 162 `src:` lines):
**162 distinct lines of the rendering, each quoted once**, out of 410 lines, 361 of them non-blank (45% of the non-blank lines).
Each rule carries the one to three lines that hold its operative words (the condition, the figure, the consequence), not the whole provision; its `@ref` gives the provision's full line range.
The quotations are concentrated where the words matter most: the five rows of the Art 3(b) table are quoted in full (10 lines).
Headings are not quoted in the modules; `NOTES.md` section 2 gives each heading as the document writes it.

Short Vietnamese terms also appear in `GLOSSARY.md`, `COMPARABLES.md`, `NOTES.md` and the modules' comments, each checked to occur verbatim in the source by `tools/vnsrc.py check`.

If the issuer objects to the quotation, delete the `-- src:N |` lines: the rules and the tests stand without them.
The encoding itself is Apache-2.0, which does not extend to the quoted source text.
