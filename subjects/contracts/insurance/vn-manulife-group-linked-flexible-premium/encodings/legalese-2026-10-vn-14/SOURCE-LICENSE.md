# Source licence — encoding row `legalese-2026-10-vn-14`

The source is Công ty TNHH Manulife (Việt Nam)'s rules and terms for its group universal-linked flexible-premium product, cited by URL and sha256 in `../../subject.json`.
Its licence position is recorded in the subject-level file, `../../SOURCE-LICENSE.md`, which governs: **terms undetermined**; the PDF and its text rendering are not held in the repository; quotation follows Meng's ruling of 2026-10-06 ("quoting the encoded clauses as short -- src:N | comment lines is acceptable for private insurers' text").

How much this encoding quotes, counted on 2026-10-07:

- the `.l4` modules carry **693** `-- src:` lines (518 single-line quotations and 175 range citations, each of which quotes one line and stands for a range);
- together they quote **620 distinct lines** of the 1,422 non-blank lines of the rendering (44%), one clause at a time, each beside the rule that encodes it;
- the Markdown files quote short verbatim terms and phrases only (GLOSSARY.md, COMPARABLES.md, NOTES.md), checked by `tools/vnsrc.py`.

If the issuer objects, remove the `src:` lines; the rules and tests stand without them.
The encoding itself (the `.l4` modules, the tools, `check.sh` and the notes) is Apache-2.0; that does not extend to the quoted source text.
