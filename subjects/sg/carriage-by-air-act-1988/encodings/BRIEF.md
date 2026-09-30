# Encoding brief: Carriage by Air Act 1988, in L4

You are producing an L4 encoding of the Carriage by Air Act 1988 (Singapore) from its source.
This brief is the whole specification.

## The subject

**Carriage by Air Act 1988** (2020 Revised Edition; Act 20 of 1988, in force 16 September 1988), as shown on Singapore Statutes Online "Current version as at 30 Sep 2026".

The Act gives the force of law in Singapore to the Warsaw Convention on international carriage by air in three texts, and adds rules of its own (ss 5 to 11). The three texts are set out in the Schedules: the original Warsaw Convention (Second Schedule), the Convention as amended by the Hague Protocol (First Schedule), and as further amended by Montreal Protocol No. 4 (Third Schedule). It is a primary Act. It delegates to the Minister in ss 6(4), 10(1) and 12; no order or regulation is among the inputs.

| vintage | source | where |
| ------- | ------ | ----- |
| the original Warsaw Convention | Second Schedule | `source/CAA1988.txt` lines 824 to 1392 |
| Warsaw as amended by the Hague Protocol | First Schedule | lines 246 to 823 |
| Warsaw (Hague) as amended by Montreal Protocol No. 4 | Third Schedule | lines 1393 to 2040 |

All three are in force in Singapore at once and apply to different carriage, depending on which instruments the States concerned have ratified. **Each is its own answer, and the version is an input.** Where a text is silent on a point, the answer is that it is silent; never a number borrowed from another text.

The text is Singapore Statutes Online's point-in-time PDF, which SSO's terms (cl.8) call an **unofficial** consolidation. The PDF was downloaded by hand from the SSO website.

## Scope: the whole Act

ss 1 to 13 and the three Schedules, every Article and the Additional Protocol of each. The Legislative History, Abbreviations and Comparative Table are not part of the Act and are out of scope.

## Deliverables, all under `encodings/`

1. `.l4` modules, English identifiers, ASCII filenames, the shared nouns in `caa-types.l4`.
2. Test modules asserting what the SOURCE says: both sides of every threshold, and each rule that differs between the texts asserted against each text.
3. `NOTES.md` with the coverage table (every Article of every Schedule), the fork register and the answer tables.
4. `check.sh`, `encoding.json`, `SOURCE-LICENSE.md`.

## Rules that matter

- **Isomorphic.** One source provision, one recognisable place, a citation on every rule naming the Schedule.
- **Versions are inputs, never merged.** A text that says nothing on a point answers `REFUSE`.
- **Amounts stay in the Convention's own units** (francs, Special Drawing Rights); converting them is the Minister's order under s 6(4), which is not an input, so it is a named `REFUSE`.
- **A failing assertion is a finding.** Never edit an expected value to match the code.
- **Read diagnostics, not exit codes.**

## Toolchain

`l4` from `legalese/prereleases` tag `unstable-20260926-c76e6b0`. `JL4_LIBRARY_PATH` unset.
