# Provenance of the source text

| file | what it is | sha256 |
| --- | --- | --- |
| `EA1893.pdf` | Singapore Statutes Online PDF of the Evidence Act 1893, footer "Current version as at 01 Oct 2026 / PDF created date on: 01 Oct 2026"; supplied from the user's folder `SG Acts/Evidence Act 1893.pdf` on 2026-10-01 | `c49f71d5b3e3d497a643cfa4c89f2f8cd64bb9048ecaf24b34b7801dcb7cf7a0` |
| `EA1893.txt` | `pdftotext -layout` of the PDF (5,508 lines), in a single-byte (Latin-1) encoding and **not UTF-8**: read it with that encoding. Line references in the modules' comments are to this file | `25b13c324a9c91a79daa4f227d8664e91f4262499723f6c22e7b94840e2c0851` |

- **Act**: Evidence Act 1893, Singapore.
- **URL**: https://sso.agc.gov.sg/Act/EA1893
- **Retrieved**: 2026-10-01 (the PDF's own created date). How it was fetched is not known to the encoder.
- **Status**: unofficial consolidation (SSO Terms of Use cl.8). Not authoritative. **A current (revised) version**: the "2020 Revised Edition", which "incorporates all amendments up to and including 1 December 2021 and comes into operation on 31 December 2021", with marginal amendments after that date.
- **Legislative history**: the PDF ends with SSO's Legislative History ("not part of the Act"). The Act's own commencement line reads "[1 July 1893]". Repealed sections are printed as "[Repealed by ...]": ss 24 to 30 (Act 15 of 2010), 35 and 36 (Act 4 of 2012), 115 (Act 8 of 1996).
- **Instrument it is made under**: none; it is a primary Act. Acts it points at (the Criminal Procedure Code 2010, Penal Code 1871 and many others) were **not** fetched here. The Criminal Procedure Code has its own subject, `sg/criminal-procedure-code-2010`.
- **Extraction artefacts**: the layout text prints the apostrophe and some dashes as single non-UTF-8 bytes, repeats the page footer on every page, and in s 32(1) interleaves the paragraph headings ("when it relates to cause of death;") before the paragraphs they head.
