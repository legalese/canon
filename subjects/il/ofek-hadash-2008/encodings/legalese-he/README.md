# `ofek hadash` — an L4 encoding written in Hebrew

This directory holds a seven-module L4 encoding of the Israeli teachers' collective agreement known
as **אופק חדש** ("Ofek Hadash") — the 25.12.2008 base agreement, its 2012 completion agreement, the
September 2013 and 19.3.2017 amendments, the 19.10.2022 agreement that replaced the salary tables,
the annual circulars that price recuperation, jubilee and clothing allowances, and the 27.3.2025 law
and 29.6.2026 agreement that reduce public-sector pay. It answers, for a named teacher in a named
month, what the instruments say they are owed and why: which appendix, darga and seniority row they
stand in; how large a post their week of frontal, individual and presence hours amounts to; which
role supplements they draw and on what base; what the hour-priced work is worth; and what joins or
leaves the payslip in June, July and a reduction year. **The encoding is written in Hebrew** — every
type, field, parameter, rule and refusal name is a Hebrew phrase, and every declaration carries an
`@ref` naming its instrument and article, so the code can be read against the text it encodes. It is
not a payroll system and does not try to be one: it is the law, written down in a form that can be
executed, argued with, and shown to be wrong.

What the encoding will not do is guess. Where the corpus is missing the instrument a rule depends on
— the 31.8.2008 agreement on the pension-determining salary, the Ministry letter that conditions
every promotion, a trip-escort table whose column headings were transcribed as `[לא קריא]` — the
rules **refuse**, by name and with a citation, rather than returning a zero or a neighbouring value.
Thirty-eight such refusals are written into the code. `NOTES.md` is the companion document: it records
what is encoded and what is not, the three-form Hebrew naming convention, all eleven forks with both
readings and the one taken, the gaps in the corpus, the toolchain facts worth knowing before you
debug them, and the eight questions a reviewer still has to settle.

## Running it

The binary is `../l4-vinyl`. Run from **this directory**, so that `IMPORT` resolves
importer-relative:

```sh
cd deposit
../l4-vinyl check he-cases.l4      # typechecks he-cases and everything it imports
../l4-vinyl run   he-cases.l4      # also evaluates every #ASSERT and #EVAL
```

`he-cases.l4` sits at the bottom of the import graph, so checking it checks all seven modules. To run
one module on its own, name it instead — the dependency order is `he-domain`, `he-tavlaot`,
`he-mishra`, `he-sachar-meshulav`, `he-gmulim`, `he-brutto`, `he-cases`.

**Read the diagnostics, not the exit code.** `l4 run` exits 0 even when an assertion fails, printing
`DiagnosticSeverity_Error`. The current state is 457 assertions across the seven modules, all
satisfied, with zero errors; each satisfied assertion is logged twice, so a raw
`grep -c 'assertion satisfied'` reports 914. A refusal is a `DiagnosticSeverity_Warning` and is the
intended answer wherever the corpus is silent.

`he-tavlaot.l4` is **generated** from the corpus HTML by `../work/gen.py`, which parses the printed
tables directly. Edit the generator, not the module: a hand edit is reverted on the next run.
