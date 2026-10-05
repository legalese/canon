# Encoding brief: the Notaries Public Act 1959 (Singapore), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Notaries Public Act 1959** — Singapore, 2020 Revised Edition, as printed by Singapore Statutes Online, "Current version as at 05 Oct 2026".

The Act lets the Senate of the Singapore Academy of Law appoint fit and proper practising advocates and solicitors of at least 7 years' standing as notaries public for up to 12 months, after consulting the Law Society's Council (s 3(1)-(4)), and appoint temporary notaries during another's absence of more than a month (s 3(5)-(6)). It gives notaries the powers of English notaries, but limits oaths for affidavits used in Singapore to three cases (s 4); requires revocation for bankruptcy, striking off or misconduct (s 5) and allows it on request (s 6); makes exercising notarial functions otherwise than in accordance with the Act an offence (s 7); and lets the Chief Justice make rules (s 8).

There is one vintage. The source is `../source/NPA1959.pdf` and its text, `../source/NPA1959.txt`; `../source/PROVENANCE.md` says where it came from. It is SSO's unofficial consolidation (SSO Terms of Use cl.8), not the authoritative text.

The Act was last amended by Act 20 of 2007 (in force 1 June 2007). Earlier texts were not supplied: every rule about a day refuses for a day before 1 June 2007.

## Scope — pinned

ss 1-8, the whole Act. A provision with nothing to compute (a short title, a power with no condition) is **inert**: carry its words and say so in the coverage table. Out of scope: any subsidiary legislation, and the other Acts this one refers to — what they decide is an input.

## Deliverables, all in this `encodings/` directory (no row subfolder)

1. `.l4` modules: one module of nouns only, the rules, and tests whose expected values come from the source.
2. `NOTES.md`: scope, a coverage table (every section and Schedule), a fork register, and anything a reviewer must know.
3. `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's own words beside each limb.
- Where the source does not answer, `REFUSE "…"` — never `FALSE` or `0`.
- A failing assertion is a finding: never edit an expected value to match the code.
- Read the diagnostics, not the exit code.
- The powers of notaries in England (s 4(1)) and anything prescribed by rules under s 8 are not in the source: where an answer turns on them, REFUSE.
- Maximum fines are ceilings, not amounts owed.

## Toolchain

`~/.local/bin/l4`, built from `legalese/l4-ide` `unstable` at `7768812fa`. Leave `JL4_LIBRARY_PATH` unset.
