# Source licence — encoding row `legalese-2026-10-vn-08`

The source is Bảo Minh's "Quy tắc bảo hiểm mọi rủi ro cho tài sản", a standard-form document published by Tổng Công ty Cổ phần Bảo Minh on its own website: private contract terms, not law.
Its licence position is recorded in the subject's own file, `../../SOURCE-LICENSE.md`, which governs here: **terms undetermined**, no licence claimed, and the source itself is not held in this repository (`source/fetch.sh` fetches it and checks its sha256).

What this encoding takes from it:

- **455 `-- src:N |` quotation lines** across the `.l4` modules (the count `tools/vnsrc.py check` reports over `*.l4`), each one line of the `pdftotext` rendering, generated mechanically so that a reviewer can check each rule against its words;
- short verbatim runs in `NOTES.md`, `GLOSSARY.md`, `COMPARABLES.md`, `encoding.json` and in comments and strings, each checked by `tools/vnsrc.py check` to occur in the source.

If the issuer objects to the quotation, delete the `src:` lines and the quoted runs; the rules and the tests stand without them.

The encoding itself (the `.l4` modules, `check.sh`, `tools/`, and the notes) is Apache-2.0, the licence of this repository; that does not extend to the quoted source text.
