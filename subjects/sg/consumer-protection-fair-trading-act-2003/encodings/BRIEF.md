# Encoding brief: Consumer Protection (Fair Trading) Act 2003, in L4

You are producing an L4 encoding of the Consumer Protection (Fair Trading) Act 2003 (Singapore) from its source.
This brief is the whole specification.

## The subject

**Consumer Protection (Fair Trading) Act 2003** (2020 Revised Edition; Act 27 of 2003, in force 1 March 2004; revised edition in operation 31 December 2021), as shown on Singapore Statutes Online "Current version as at 30 Sep 2026".

The Act protects individual consumers against unfair practices by suppliers (Part 2), gives consumers additional rights where goods do not conform to the contract (Part 3), gives the Competition and Consumer Commission of Singapore investigation powers (Part 3A), creates offences of obstructing those investigations (Part 3B), and closes with general provisions and five Schedules (Part 4).
It is a primary Act. It is not made under another instrument, but it delegates: ss 6(6), 9(7), 9(10), 11, 41(2), 42 and 43 let the Minister prescribe by regulation or order, and no such instrument is among the inputs.

| vintage | source | where |
| ------- | ------ | ----- |
| Current consolidation, 30 Sep 2026 | Singapore Statutes Online PDF, "PDF created date on: 30 Sep 2026"; banner: "2020 Revised Edition ... incorporates all amendments up to and including 1 December 2021 ... comes into operation on 31 December 2021", with the marginal `[Act 5 of 2025 wef 09/03/2025]` and `[Act 31 of 2022 wef 01/11/2022]` amendments visible in the text | `source/CPFTA2003.pdf` (text: `source/CPFTA2003.txt`) |

One vintage. The text is Singapore Statutes Online's point-in-time PDF, which SSO's own terms (cl.8) call an **unofficial** consolidation: it is not the authoritative text, and no authoritative source (the printed 2020 Revised Edition, the Gazette) is among the inputs. The banner's "Current version as at 30 Sep 2026" is the in-force statement used throughout.
No earlier or later text is an input, so no vintage axis is encoded: the Act's own dated rules (s 14(1)(c), contracts on or after 1 September 2012; s 44, before 2 April 2018) are encoded as ordinary date tests on the facts of the case.

All inputs are under `source/`. Read them there and nowhere else.

## Scope: the whole Act

Every provision: ss 1 to 44, the First, Second, Fourth and Fifth Schedules, and the Third Schedule (repealed).
The Legislative History, Abbreviations and Comparative Table are not part of the Act (the Legislative History says so) and are out of scope.
Definitions the Act takes from other Acts (Sale of Goods Act 1979, Supply of Goods Act 1982, Hire-Purchase Act 1969, Unfair Contract Terms Act 1977, Small Claims Tribunals Act 1984, Road Traffic Act 1961, Limitation Act 1959) are **inputs**: the encoding takes their answers as facts and does not encode those Acts.

## Deliverables, all under `encodings/`

1. `.l4` modules, English identifiers, ASCII filenames, the shared nouns in one module (`cpfta-types.l4`) that every other module imports.
2. A tests module asserting what the SOURCE says: both sides of every threshold ($30,000; 6 months; 2 working days; 14 days; 5 and 10 years; $10,000 and 12 months; the lower of half the maximum fine and $5,000; 15% of voting power) and one scenario per Second Schedule paragraph.
3. `NOTES.md` with the coverage table, the fork register and the answer tables.
4. `check.sh` and `encoding.json`, `SOURCE-LICENSE.md`.

## Rules that matter

- **Isomorphic.** One source provision, one recognisable place, section numbering in `§` headings, a citation on every rule.
- **Where the Act delegates and no instrument is an input, `REFUSE`.** The prescribed limit in s 6 is different: s 6(6) fixes $30,000 and lets the Minister prescribe another, so $30,000 is the default and the amount is also an input.
- **Where the Act is a power, not a duty** (a court "may"), the encoding answers whether the power is *available*, never whether it will be exercised.
- **A failing assertion is a finding.** Never edit an expected value to match the code.
- **Read diagnostics, not exit codes.** `check.sh` prints errors, satisfied and failed.

## Toolchain

`l4` from `legalese/prereleases` tag `unstable-20260926-c76e6b0` (commit `c76e6b041f0b297cadad0ea535a4894d9b6fdef7`). `JL4_LIBRARY_PATH` unset.
