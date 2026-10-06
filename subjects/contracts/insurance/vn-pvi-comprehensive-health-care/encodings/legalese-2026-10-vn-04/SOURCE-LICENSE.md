# Source licence — encoding row `legalese-2026-10-vn-04`

The source is PVI's comprehensive health care insurance rules, private contract terms and the issuer's text, as mirrored on an insurance agent's website (`../../source/raw/pvi-health.pdf`, sha256 `89ce0df496b51b87d7f7a5d80ad419942ec035a61999526c9391a0bb3fb49860`; its text rendering `pvi-health.txt` is what is quoted).
The subject's own record of the terms, `../../SOURCE-LICENSE.md`, governs: **terms undetermined**, no reproduction notice found, no licence claimed, the source fetched rather than held.

What this encoding quotes: **842 `-- src:N |` lines** in its `.l4` modules (counted by `tools/vnsrc.py check` over the `.l4` files on 2026-10-07), each one line of the rendering, generated mechanically and placed beside the rule it supports; and short verbatim runs (defined terms, clause headings) in NOTES.md, GLOSSARY.md and COMPARABLES.md. The encoding does not reproduce the document wholesale.
If the issuer objects, delete the `src:` lines and the quoted runs; the rules and tests stand without them.

The encoding itself (the `.l4` modules, `check.sh`, the notes and tables) is Apache-2.0. That does not extend to the quoted source text.
