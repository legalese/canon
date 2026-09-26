# state-public — coverage

Penal Code 1871 (2020 RE, SSO as at 09 Sep 2026), Chapters 6, 6A, 6B, 7, 8, 9 and 10: ss 121–190, 82 sections.
Encoder: the state-public agent, 2026-09-26.
Status: **draft** — no domain expert has read it against the source.

## What is where

| module | covers |
| --- | --- |
| `deposit/pc-state-public-common.l4` | one shared helper (`the to-wit clause`), no section |
| `deposit/pc-state-public-state.l4` | Chapter 6 (ss 121–130A), 6A (ss 130B–130C), 6B (ss 130D–130E), 7 (ss 131–140B) |
| `deposit/pc-state-public-assembly.l4` | Chapter 8 (ss 141–160) |
| `deposit/pc-state-public-servants.l4` | Chapter 9 (ss 161–171) |
| `deposit/pc-state-public-contempts.l4` | Chapter 10 (ss 172–190) |
| `deposit/pc-state-public-tests.l4` | tests for all of the above |

**The `.l4` files are generated.** `python3 notes/state-public-gen/build.py` writes them from the hand-written ladders, leaves, recitals and tests in `notes/state-public-gen/part_*.py`; `lib.py` does only the mechanical layout (quoting each section's text from `inputs/PC1871.txt`, the `Punishment` records, the charge builders, the fixtures).
Edit the part files and rebuild — a hand-edit to a `.l4` is lost on the next build.
`python3 notes/state-public-gen/notes_gen.py` regenerates this file's table and catalogue block.
The build refuses a rule named like a field of any facts record (FORK SP-0).

## Numbers

`deposit/check.sh` over a copy of the group's modules plus `pc-domain.l4` and `pc-general.l4` (toolchain `l4-unstable-20260926-c76e6b0`, `JL4_LIBRARY_PATH` unset): **0 errors, 0 warnings, 151 assertions satisfied, 0 failed**, in `pc-state-public-tests.l4`; every other module 0 / 0.

- 79 sections encoded — 70 punishing sections carrying 76 punishing provisions, each with a facts record, an `offence under s N` and a `charge under s N`, and 9 definition / deeming / saving / application sections with no charge (said so in the table) — plus 3 repealed and **0 deferred**.
- **Defining predicates.** 52 of the 76 offence ladders call a separate `@export`ed defining predicate (the catalogue's `definitionFns`). The other 24 — ss 121A-121D, 122-130, 130C, 131-133, 135-138, 140, 168, 169 — are sections that define and punish in one clause and give the offence no verb of its own; their `offence under s N` ladder IS the defining ladder, and `definitionFns` is empty (FORK SP-2).
- Every Illustration in these chapters is an `#ASSERT`, cited: ss 121, 144 (and as applied to 148, 158), 161 (a)–(c), 163, 164, 165 (a)–(c), 166, 174 (a)–(b), 177, 182 (a)–(d), 186, 188.
  Explanations are encoded as leaf `@desc`s (ss 130, 141, 161, 177 for 176, 186(2), 188) or tested (s 130's parole Explanation; s 161's "expecting" and "legal remuneration" Explanations).
- Charges asserted as full text: ss 121, 147, 152, 161, 170, 177(2), 182, 186; refusals asserted as full text: ss 121, 147, 170, 174(1), 186.
- Thresholds: s 141 / s 151's "5 or more persons" through the helper `5 or more persons` (4 / 5 / 6). No other number is an element in these chapters; the fines and terms are punishment data, checked through pc-general's readers (s 41 on ss 147, 186(1)(a); `punishable with death or imprisonment for life` on s 121; `fixed by law or carries a minimum sentence` on ss 130B(2), 169).

## Cross-module joins owed (PLAN section 1)

Leaves standing for another group's section, each saying so in its `@desc`:

| leaf | record | section | owner | edge on PLAN's list? |
| --- | --- | --- | --- | --- |
| `abets the waging of such war`, `abets the commission of any of the offences punishable by section 121A or 121B`, `abets the committing of mutiny ...`, `abets an assault ...`, `abets the desertion ...`, `abets what he knows to be an act of insubordination ...`, `abets the offence` (s 164) | Waging War, Plot against the President, War against an Allied Power, Armed Forces, Gratification to Influence | s 107 | general-part | yes |
| `assaults` (ss 124, 152), `uses criminal force to such public servant`, `threatens or attempts to use criminal force to such public servant` | Assaulting the President, Obstructing Riot Suppression | ss 350, 351 | body-a | **no — state-public → body-a is not on the list** |
| `wrongfully restrains`, `attempts wrongfully to restrain` | Assaulting the President | s 339 | body-a | **no** |
| `while committing or attempting to commit piracy, murders or attempts to murder ...` | Piracy | s 300 | body-a | **no** (it chooses the punishment only) |
| `steals a Singapore ship`, `steals or without lawful authority throws overboard ...` | Piratical Acts | s 378 | property | **no — state-public → property is not on the list** |

The two missing edges (state-public → body-a, state-public → property) are proposed; neither creates a cycle with the listed edges (no listed edge leads from body-a or property back to state-public).
Chapter 2 words (s 21 public servant, s 26A voluntarily, ss 26C–26F, s 43 illegal / legally bound, s 44 injury) are flat leaves drilling into pc-general, as PLAN section 3.3 directs.

## `DEFINITION_LADDERS` entries

```ts
  { fn: 'public servant within section 21', leaf: 'public servant', section: '21' },
  { fn: 'public servant within section 21, for sections 175, 178, 179, 180 and 228', leaf: 'public servant', section: '21(2)' }, // Omission to Produce, Refusing Oath, Refusing to Answer, Refusing to Sign Facts only
  { fn: 'voluntarily within section 26A', leaf: 'voluntarily', section: '26A' },
  { fn: 'does the act intentionally within section 26C(1)', leaf: 'intentionally', section: '26C' },
  { fn: 'knowingly in respect of a circumstance within section 26D(1)', leaf: 'knowingly', section: '26D' },
  { fn: 'rashly in respect of a circumstance within section 26E(1)', leaf: 'rashly', section: '26E' },
  { fn: 'negligently within section 26F', leaf: 'negligently', section: '26F' },
  { fn: 'injury within section 44', leaf: 'injury to any person', section: '44' },
  { fn: 'unlawful assembly within section 141', leaf: 'unlawful assembly', section: '141' },   // Hiring for Unlawful Assembly Facts (s 150)
  { fn: 'harbours within section 130A', leaf: 'harbours or conceals any such prisoner who has escaped from lawful custody', section: '130A' },
  { fn: 'harbours within section 140A', leaf: 'harbours such officer or serviceman', section: '140A' },
```

The `public servant` leaf is keyed by record: the same leaf name drills into s 21(2)'s ladder for the four records s 21(2) names, and into s 21(1)'s for every other record.
The harbour ladders take their own `Harbour Facts`, not the offence record, so the drill-down is a separate card, not a toggle.

## Proposed shared nouns

None required. Candidates another group will want: a **vessel** (s 48; ss 130B–130C "Singapore ship", s 137 "merchant vessel" — here STRING particulars), a **weapon** (ss 144, 148, 158 — here a leaf plus a STRING; body-a's s 324 and property's s 397 need the same "deadly weapon / weapon of offence likely to cause death" test), and a **summons / order / process** (ss 172–174, 188 — here STRING particulars; justice-order will meet the same).

## The table

"offence" rows carry, in order, the defining predicate(s) the offence ladder calls (the catalogue's `definitionFns`), then each `offence under s N` and `charge under s N`.
Where a section punishes in (a) "in the case of an individual" / (b) "in any other case", one charge serves both and cites the paragraph from the leaf `the accused is an individual` (FORK SP-1).
