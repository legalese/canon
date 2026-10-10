# Registers of Law 08/2022/QH15

`source-bundle.json` is the P1 source bundle: the three gazette documents (the Law in two files and the amending Law), each pinned by URL and sha256, and the official consolidated text held as corroboration only.
`external-modifications.json` is the P2 sweep: seven searches with what each does not cover, and three entries (the amending Law in two effective dates, and the implementing instruments, which were reported by search summaries and not read).
It was written after the encoding landed so that its routing names real arms.
The roadmaps are under the encoding row, `encodings/legalese-2026-10-vn-29/registers/`, because scope is a decision of the job: one per source document, every unit of each with a disposition.
There is no fork register in the pipeline's JSON format.
The fork register is `NOTES.md` section 3 of the encoding row, and `encoding.json` lists each fork in one line.
Validate the files with the `register-validate.mjs` of `legalese/l4-pipeline`.
