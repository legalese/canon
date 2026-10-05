# Encoding brief: the Metrication Act 1970 (Singapore), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Metrication Act 1970** — Singapore, 2020 Revised Edition, as printed by Singapore Statutes Online, "Current version as at 05 Oct 2026".

The Act gives the International System of Units (SI) legal force in Singapore from 15 February 1971 (s 3), defines it by the units in the First, Second and Fourth Schedules (ss 2, 3(2)), lets the Minister adapt written law to SI by Gazetted order (s 4), allows imperial and local customary values to be converted by the Third Schedule's factors (s 5), lets the Minister vary the Schedules (s 6), and saves acts done before an order and other lawful systems (s 7).

There is one vintage. The source is `../source/MA1970.pdf` and its text, `../source/MA1970.txt`; `../source/PROVENANCE.md` says where it came from. It is SSO's unofficial consolidation (SSO Terms of Use cl.8), not the authoritative text.

No date gate beyond s 3(1)'s own date: the only change since 1971 is the 1989 rectification of the Fourth Schedule, operating from 30 March 1987. The Schedules are as printed on 05 Oct 2026.

## Scope — pinned

ss 1-7 and the First to Fourth Schedules, the whole Act. A provision with nothing to compute (a short title, a power with no condition) is **inert**: carry its words and say so in the coverage table. Out of scope: any subsidiary legislation, and the other Acts this one refers to — what they decide is an input.

## Deliverables, all in this `encodings/` directory (no row subfolder)

1. `.l4` modules: one module of nouns only, the rules, and tests whose expected values come from the source.
2. `NOTES.md`: scope, a coverage table (every section and Schedule), a fork register, and anything a reviewer must know.
3. `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's own words beside each limb.
- Where the source does not answer, `REFUSE "…"` — never `FALSE` or `0`.
- A failing assertion is a finding: never edit an expected value to match the code.
- Read the diagnostics, not the exit code.
- Encode every row of every Schedule, copied from the source; the Third Schedule's "exactly" and "approximately" are part of each row.
- The text layer displaces the word "Gazette" in s 6; see ../source/PROVENANCE.md.

## Toolchain

`~/.local/bin/l4`, built from `legalese/l4-ide` `unstable` at `7768812fa`. Leave `JL4_LIBRARY_PATH` unset.
