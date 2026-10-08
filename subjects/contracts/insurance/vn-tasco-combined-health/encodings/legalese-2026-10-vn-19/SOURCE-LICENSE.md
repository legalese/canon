# Source licence — encoding row `legalese-2026-10-vn-19`

The subject's own record governs: `../../SOURCE-LICENSE.md` (terms **undetermined**; issuer's text; the PDFs and their renderings are not held in the repository, and `../../source/fetch.sh` fetches them).
Meng's ruling of 2026-10-06, recorded there, permits quoting the encoded clauses as short `-- src:N |` comment lines for private insurers' text; it is a ruling to quote, not a finding that the terms permit it.

What this encoding quotes, counted on 2026-10-07 by `grep` over the `.l4` modules:

- **516** `-- src:N |` lines from the rules (`tasco-combined-health.txt`, 843 lines, 633 of them non-blank), one clause at a time, each placed before the rule that encodes it. The scope is the whole document, so most operative clauses are quoted once.
- **5** qualified lines (`-- src:tasco-guarantee-hospitals:N`, `-- src:tasco-excluded-facilities:N`): the two lists' titles and column headings.
- The two lists' rows (160 and 38) are carried as **data**, not as comments: facility names, addresses and regions, which are needed to use the lists at all.
- The Article 2.11 list (46 names) is carried as data in the same way.
- `NOTES.md`, `GLOSSARY.md` and `COMPARABLES.md` quote short terms and phrases.

If the issuer objects, remove the `src:` lines and the quoted phrases; the rules and tests stand without them. The list data is the content of the lists and would go with them.

The encoding itself (the `.l4` modules, `tools/`, `check.sh` and the notes) is Apache-2.0, like the rest of the repository. That does not extend to the quoted source text.
