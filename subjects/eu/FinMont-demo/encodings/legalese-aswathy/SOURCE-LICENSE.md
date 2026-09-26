# Source license

The quoted text of **Commission Delegated Regulation (EU) 2018/389** is sourced from
[EUR-Lex](https://eur-lex.europa.eu/), operated by the Publications Office of the
European Union.

- **Copyright owner**: European Union.
- **License**: reuse authorised under
  [Commission Decision 2011/833/EU of 12 December 2011 on the reuse of Commission documents](https://eur-lex.europa.eu/eli/dec/2011/833/oj)
  (OJ L 330, 14.12.2011, p. 39) — free of charge, including for commercial purposes,
  provided the source is acknowledged and the original meaning is not distorted.
- **Retrieved**: 2026-09-09, from https://eur-lex.europa.eu/eli/reg_del/2018/389/oj
- **Excluded from the license**: the European Union emblem and any logos or trade marks
  appearing on the source site, and any third-party material identified as such.

## Required attribution

Sourced from EUR-Lex at 2026-09-09: "Commission Delegated Regulation (EU) 2018/389 of
27 November 2017 supplementing Directive (EU) 2015/2366 of the European Parliament and of
the Council with regard to regulatory technical standards for strong customer
authentication and common and secure open standards of communication", OJ L 69,
13.3.2018, p. 23, © European Union, reused under Commission Decision 2011/833/EU.

This encoding **adapts** the quoted text rather than reproducing it verbatim: it restates
the Regulation's rules as L4 definitions. The attribution must therefore read "Based on
content from EUR-Lex at 2026-09-09 ...".

## Secondary source — not deposited

`psd2-refunds-and-liability.l4`, and three of the five scope gates in
`finmont-sca-orchestration.l4`, are derived from

> Directive (EU) 2015/2366 of the European Parliament and of the Council of 25 November
> 2015 on payment services in the internal market, OJ L 337, 23.12.2015, p. 35.
> ELI: <https://eur-lex.europa.eu/eli/dir/2015/2366/oj>

carrying the same licence terms. ⚠ **That text was not supplied with this encoding job
and is not in `registers/source-bundle/`.** Every rule derived from it is marked
`UNVERIFIED` at its `@ref`. See `NOTES.md` §3.

## Authenticity

Only the electronic edition of the *Official Journal of the European Union* published on
EUR-Lex is authentic and produces legal effects, under
[Council Regulation (EU) No 216/2013](https://eur-lex.europa.eu/eli/reg/2013/216/oj) of
7 March 2013 on the electronic publication of the Official Journal.

**Nothing in this directory is authentic legal text.** `registers/source-bundle/` holds a
text extraction of a PDF copy; the `.l4` modules are an encoding of that extraction. Where
this encoding and the Official Journal differ, the Official Journal governs, and the
difference is a defect here to be reported and fixed.

## The encoding itself

Everything authored in this directory — the `.l4` modules, the scenario cases, the
ambiguity register, the notes and the conversion report — is licensed under
[Apache-2.0](../../../LICENSE), the repository's licence for authored work.

The prose artifacts (`NOTES.md`, `registers/ambiguity-register.md`,
`report/conversion-report.md`) are additionally offered under
[CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/).

## No legal advice

This encoding is a machine-readable construction of a legal text, produced to support
engineering and compliance work. It is not legal advice, and it carries no fidelity claim:
`subject.json` declares `status: "draft"` and no human gate has been granted. The
one-leg-out reading in particular (`registers/ambiguity-register.md`, AR-07) is contested
and jurisdiction-sensitive and should not be relied on without local advice.
