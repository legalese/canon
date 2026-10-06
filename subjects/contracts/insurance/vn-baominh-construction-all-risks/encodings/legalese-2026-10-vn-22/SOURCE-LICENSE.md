# Source licence — encoding row `legalese-2026-10-vn-22`

The source is Bảo Minh's standard-form wording, "Quy tắc bảo hiểm mọi rủi ro xây dựng", published by Tổng Công ty Cổ Phần Bảo Minh at baominh.com.vn (PDF sha256 `5dbef555b6fd4132dd6b55c0ebb7200e7f03071bd0867e5644c3085d8ea2bcce`).
Its terms are **undetermined**; the subject's own record is `../../SOURCE-LICENSE.md`, which governs where this file is silent, including the ruling of 2026-10-06 that quoting encoded clauses as short `-- src:N |` comment lines is acceptable for private insurers' text, and the path for removing them if the issuer objects.

**How much this encoding quotes.**
The `.l4` modules carry **256** `-- src:N |` lines, quoting **226 distinct lines** of the 233 non-empty lines of `../../source/raw/baominh-car.txt`, each before the rule that encodes it.
That is because the brief pinned the scope to the whole document, and every clause is encoded with its text beside it: the quotation is clause by clause, but taken together it covers nearly all of the text.
The lead should weigh this against the ruling, which covers clause-level quotation and not reproduction of the document.
The other 30 quotation lines are repeats (26 source lines quoted twice, lines 19 and 20 three times), each before a second rule that encodes the same clause; the findings and tests modules cite line numbers instead of quoting.
`NOTES.md`, `GLOSSARY.md` and `COMPARABLES.md` quote short runs only.
Removing every `src:` line leaves the rules and tests intact.

The encoding itself (the `.l4` modules and the Markdown files) is Apache-2.0; that does not extend to the quoted source text.
