# Provenance of the source text

| file | what it is | sha256 |
| --- | --- | --- |
| *(not in the repository)* | Singapore Statutes Online PDF of the Metrication Act 1970, footer "Current version as at 07 Oct 2026"; 7 pages; supplied by the user as an upload on 2026-10-07. Its text is identical to the 05 Oct 2026 PDF below | `b864e3eb60650153c7a25d0de1cb1c815d4fae8520b17e44f61c0b9e440c68a1` |
| *(removed 2026-10-07)* | the 05 Oct 2026 PDF ("Current version as at 05 Oct 2026 / PDF created date on: 05 Oct 2026"), uploaded 2026-10-05, from which `MA1970.txt` was extracted; it was committed as `MA1970.pdf` in 8be1b30e and removed, as PDFs are not kept in this repository | `ec7a5ce000bedb306d436ee6574945a880fbedb55a7a76c1c1884840361b7660` |
| `MA1970.txt` | the PDF's text layer, extracted with `pypdf` 6.19.0 in layout mode (the script reproduced below; 341 lines). The encoding's line references are to this file | `a998f36eff1b5acbe76cd594f13699a845e37100ccd95073332f488f5ab6d4d0` |

- **Status**: unofficial consolidation (SSO Terms of Use cl.8). Not authoritative.
- **In force as at**: 7 Oct 2026 (the banner of the later upload; the text is unchanged from 5 Oct 2026). The text states itself as the 2020 Revised Edition, which "incorporates all amendments up to and including 1 December 2021 and comes into operation on 31 December 2021".
- **History**: Legislative History: Act 52 of 1970 (commenced 15 February 1971), the 1985 Revised Edition, G.N. No. S 22/1989 (rectification, operating 30 March 1987, which the Fourth Schedule marks "[S 22/89]"), and the 2020 Revised Edition. The 2020 edition renumbered Schedules A-D as the First to Fourth Schedules (Comparative Table). The Legislative History "is not part of the Act".
- **How it was retrieved**: uploaded to the session by the user on 2026-10-05. How the PDF was obtained from SSO was not stated.
- **Extraction artefacts**: repeated page footers and the Table of Contents are in the text, which is not part of the Act. s 6 is extracted as "by notification in the , add to, vary or Gazette amend": the italicised word "Gazette" is displaced in the PDF's text layer. pypdf's plain (non-layout) extraction of the same PDF reads "by notification in the Gazette, add to, vary or amend", which is the reading encoded.
- **Instrument it is made under**: none; it is a primary Act.
- **Earlier deposit**: `../registers/source-bundle/MA1970.txt` was fetched by the bulk ingestion on an earlier date and is kept as it was; this `source/` copy is the one the encoding cites.

## Extraction script

```python
import sys, pypdf
r=pypdf.PdfReader(sys.argv[1])
out=[]
for i,p in enumerate(r.pages):
    out.append(p.extract_text(extraction_mode="layout"))
sys.stdout.write("\n\f\n".join(out))
```
