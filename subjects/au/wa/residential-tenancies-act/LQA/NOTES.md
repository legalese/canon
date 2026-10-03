# LQA notes: Residential Tenancies Amendment (Rent Cap) Bill 2026 (WA)

## This is a Bill, and it is not law

Bill No. 70 is a private member's Bill (Hon Tim Clifford MLC). It was introduced, read a first
time and had its second reading moved in the Legislative Council, all on 7 May 2026. At
2026-09-30 its status is still "Legislative Council Second Reading". No Supplementary Notice
Paper has been read. Nothing in this folder should be quoted as law.

## What is here

| file | contents |
|---|---|
| `Bill+70-1+(2026).pdf` | the Bill as introduced, deposited by the user. sha256 `35266e07…f30e12` |
| `sources/bill-70-1.txt` | `pdftotext -layout` extraction of the PDF |
| `EM.pdf`, `sources/em.txt` | Explanatory Memorandum (paper 1154) |
| `Debate.pdf`, `sources/debate.txt` | LC Hansard, 7 May 2026: second reading speech |
| `sources/act-rta-1997-r84-part5-excerpt.txt` | ACT Residential Tenancies Act 1997, Part 5: the model the EM names |
| `rent-cap-bill-rent.l4` | cl.2 commencement; proposed s.31AA, s.31AB and s.105 |
| `rent-cap-bill-termination.l4` | cl.5–9 (amended ss.60, 64, 70A, 72; new s.71BA); proposed ss.106–107 |
| `INCIDENTS.md` | the findings: B-01 to B-13, forks F-1 to F-3, V-01 to V-08 |

Each module encodes the Act **as it would read if the Bill passed unamended**. Neither module
edits or imports the Act's own encoding in `../`. The unamended provisions stay encoded there as
current law, and the Bill modules re-state only what they need.

## Running it

```bash
l4 run rent-cap-bill-rent.l4
l4 run rent-cap-bill-termination.l4
```

Both exit 0, with 23 and 20 `#ASSERT`s respectively, all satisfied and no error diagnostics
(checked 2026-09-30). As with the RBO Bill, this was run directly with `l4` rather than through
the pipeline driver. It is an inner loop, not a receipt, and nothing here has been through HG1.

## Scheme console

`tools/scheme-console/schemes.js` holds scheme `rta-rent-cap`: the Act as amended by the Bill.
Its scope is ss.30, 31AA and 31AB; s.64 as amended, with s.64(3)–(4) unamended; s.70A as
amended; s.71BA; s.76C; and ss.105–107. Commencement is assumed to be 1 January 2027, which is
day 92 on the console clock. At forks it takes the same readings as the L4: reading A for F-1 and
the s.76C reading for F-2.

To run the checker:

```bash
node tools/scheme-console/check.js
```

To view the scheme, serve `tools/scheme-console/` over HTTP. `index.html` declares no charset, so
under a bare `python -m http.server` every scheme's dashes and quotes display as mojibake. That
problem predates this scheme.

## Conventions forced by the local toolchain

- **No `IMPORT daydate`.** It still does not resolve (H-04 in the RBO register), so dates are day
  offsets. Calendar months in s.64(2A) are represented by their shortest possible day-counts
  (89 days and 181 days). A notice falling in the band just above those needs a calendar check.
- **No record update.** `value WITH …` works only on a type name, so every fixture is a full
  literal.

## Not done

- The EM and the second reading speech **were** read on 2026-09-30 (`EM.pdf` and `Debate.pdf`,
  with text in `sources/`). So was the ACT Act that both name as the model (excerpt in
  `sources/`). See "What the Explanatory Memorandum and second reading speech add" in
  `INCIDENTS.md`. They confirm B-09 is a drafting error, show that B-01 and B-02 depart from the
  ACT model, add B-14, and leave F-1 and F-2 open.
- Debate adjourned on 7 May 2026 after the mover's speech, so there is no further Hansard to read.
  Also not read: the Anglicare report tabled as paper 1155, which is policy context, not
  interpretation.
- Regulative (`MUST … WITHIN`) encodings of the new duties were not written.
- Findings have not been sent to anyone. Per `PIPELINE.md`, releasing them is an HG2 act.
