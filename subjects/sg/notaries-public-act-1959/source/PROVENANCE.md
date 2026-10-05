# Provenance of the source text

| file | what it is | sha256 |
| --- | --- | --- |
| `NPA1959.pdf` | Singapore Statutes Online PDF of the Notaries Public Act 1959, footer "Current version as at 05 Oct 2026 / PDF created date on: 05 Oct 2026"; supplied by the user as an upload on 2026-10-05 | `798adba96bb355c74216808372ea5cc613ad55f2d85292eaff915d5df798146c` |
| `NPA1959.txt` | the PDF's text layer, extracted with `pypdf` 6.19.0 in layout mode (the script reproduced below; 324 lines). The encoding's line references are to this file | `580b26225859607c5eff4c19ae5ddc81fdb6efbb4804c64e07dd1edcc0c7a281` |

- **Status**: unofficial consolidation (SSO Terms of Use cl.8). Not authoritative.
- **In force as at**: 5 Oct 2026 (the banner). The text states itself as the 2020 Revised Edition, which "incorporates all amendments up to and including 1 December 2021 and comes into operation on 31 December 2021".
- **History**: Legislative History: Federation of Malaya Ordinance 41 of 1959, extended to Singapore with modifications on 18 March 1965 (L.N. 98/1965); amended by Act 18 of 1983 (20 January 1984), Act 34 of 1995 s 11 (1 January 1996) and Act 20 of 2007 s 25 (1 June 2007, which s 7 marks "[20/2007]"); 2020 Revised Edition. The Legislative History "is not part of the Act".
- **How it was retrieved**: uploaded to the session by the user on 2026-10-05. How the PDF was obtained from SSO was not stated.
- **Extraction artefacts**: repeated page footers and the Table of Contents are in the text, which is not part of the Act. s 3(7) is extracted as "shall be published in the .Gazette": the italicised word is displaced in the text layer; pypdf's plain (non-layout) extraction of the same PDF reads "shall be published in the Gazette."
- **Instrument it is made under**: none; it is a primary Act.
- **Earlier deposit**: none; this subject was created on 2026-10-05.

## Extraction script

```python
import sys, pypdf
r=pypdf.PdfReader(sys.argv[1])
out=[]
for i,p in enumerate(r.pages):
    out.append(p.extract_text(extraction_mode="layout"))
sys.stdout.write("\n\f\n".join(out))
```
