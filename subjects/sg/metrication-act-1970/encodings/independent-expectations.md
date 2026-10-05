# Independent expectations — Metrication Act 1970 (2020 RevEd)

Written from `BRIEF.md`, `../source/MA1970.txt` and `../source/PROVENANCE.md` only, before any
`.l4`, `NOTES.md` or `encoding.json` was opened.

## Readings taken where the text is silent or ambiguous

- **R1 s 3(1) date.** "On and after 15 February 1971": 14 Feb 1971 → no legal force under s 3(1);
  15 Feb 1971 and later → legal force.
- **R2 s 5 "in accordance with the Third Schedule".** Only the seven units the Third Schedule names
  (yard, pound, gallon, tahil, kati, chhun, chhek) are convertible under s 5. A unit not listed
  (foot, ounce, mile, picul, chupak...) is not answered by the Act: I expect the encoding to
  refuse, not to derive (e.g. foot = yard ÷ 3). Ambiguous — s 5 is permissive ("may be
  converted"), and derivation is arithmetic not the Act.
- **R3 Conversion is linear**: n units × factor. "exactly" / "approximately" is carried with the
  row.
- **R4 gallon** has two rows: 4.54609 litres approximately and 4.54609 cubic decimetres
  approximately. Both factors 4.54609; both approximate.
- **R5 s 2(1)(b) / s 3(2)(c) Fourth Schedule.** The Fourth Schedule units are part of SI unless the
  subject or context is inconsistent or it is otherwise expressly provided. Default: included.
- **R6 s 4(2) "must be published in the Gazette".** An order not published in the Gazette is not
  a valid order under s 4. A s 4 order may only replace non-metric references with SI references
  that are (a) equivalent or (b) approximations the Minister thinks desirable for convenient terms.
- **R7 s 7(1)** bars a challenge only where (i) the act was done *before* the making of a s 4
  order, and (ii) the *only* ground is that a non-SI unit was used. An act done on/after the order,
  or a challenge with another ground, is not saved by s 7(1). Whether "before the making of any
  order" means the order relevant to that subject or any order at all is ambiguous; I take "the
  relevant order". The day of the order itself: "before" → an act on the day of making is not saved.
- **R8 s 7(2).** Any other system of units lawfully used keeps its legal force.

## Scenarios

### s 2 / s 3 — what SI is, and when it has force

| # | scenario | expected | provision |
|---|---|---|---|
| S1 | use of SI on 14 Feb 1971 | no legal force under s 3(1) | s 3(1) |
| S2 | use of SI on 15 Feb 1971 | legal force and validity | s 3(1) |
| S3 | use of SI on 5 Oct 2026 | legal force | s 3(1) |
| S4 | "SI" abbreviation | recognised legal reference to SI | s 2(2) |
| S5 | each First Schedule unit (metre m length; kilogram kg mass; second s time; ampere A electric current; kelvin K thermodynamic temperature; candela cd luminous intensity) | is a basic SI unit; 6 in total | s 3(2)(a), Sch 1 |
| S6 | each Second Schedule unit (hertz Hz; newton N; joule J; watt W; coulomb C; volt V; farad F; ohm Ω; weber Wb; tesla T; henry H; lumen lm; lux lx; radian rad; steradian sr) | SI supplementary/derived unit; 15 in total | s 3(2)(b), Sch 2 |
| S7 | each Fourth Schedule unit (hectare ha area; metric tonne t mass; litre L volume; centigrade or Celsius °C temperature, temperature interval) | part of SI unless context inconsistent / expressly otherwise | s 2(1)(b), s 3(2)(c), Sch 4 |
| S8 | Fourth Schedule unit where context is inconsistent | NOT included | s 2(1)(b) |
| S9 | Fourth Schedule unit where expressly otherwise provided | NOT included | s 2(1)(b) |
| S10 | a unit in no Schedule (e.g. mole, yard, foot) | not a unit of SI as defined | s 2(1), s 3(2) |

### s 5 / Third Schedule — every row, and arithmetic

| # | unit | factor | exact? | worked example |
|---|---|---|---|---|
| T1 | 1 yard | 0.9144 metre | exactly | 100 yd = 91.44 m |
| T2 | 1 pound | 0.45359237 kilogram | exactly | 10 lb = 4.5359237 kg |
| T3 | 1 gallon | 4.54609 litres | approximately | 2 gal = 9.09218 L |
| T4 | 1 gallon | 4.54609 cubic decimetres | approximately | 1 gal = 4.54609 dm³ |
| T5 | 1 tahil | 37.799364 grams | approximately | 16 tahil = 604.789824 g |
| T6 | 1 kati | 0.604790 kilogram | approximately | 100 kati = 60.479 kg |
| T7 | 1 chhun | 37.465 millimetres | exactly | 10 chhun = 374.65 mm |
| T8 | 1 chhek | 0.37465 metre | exactly | 2 chhek = 0.7493 m |
| T9 | 0 of any unit | 0 | — | |
| T10 | foot / ounce / picul (not in Sch 3) | not answered — refuse (R2) | — | |
| T11 | yard, pound, gallon are imperial standard units (s 5(a)); tahil, kati, chhun, chhek are local customary (s 5(b)) | | | |

### s 4 — orders

| # | scenario | expected | provision |
|---|---|---|---|
| O1 | order replacing non-metric references with equivalent SI units, published in Gazette | valid | s 4(1)(a), 4(2) |
| O2 | order using approximations Minister thinks desirable for convenient terms, published | valid | s 4(1)(b), 4(2) |
| O3 | either, not published in Gazette | not valid / non-compliant | s 4(2) |
| O4 | order replacing with something neither equivalent nor a desirable approximation | not within s 4(1) | s 4(1) |

### s 6 — inert power (Minister, by Gazette notification, may add to, vary or amend the Schedules).

### s 7 — saving

| # | scenario | expected | provision |
|---|---|---|---|
| V1 | act done 1 Jan 1980, relevant order made 1 Jun 1980, challenged solely because done in a non-SI unit | challenge barred | s 7(1) |
| V2 | same act, challenged on another ground as well | not barred by s 7(1) | s 7(1) "only" |
| V3 | act done 1 Jul 1980 (after the order), sole ground non-SI unit | not saved by s 7(1) | s 7(1) |
| V4 | act done on the day the order is made | not "before" → not saved (boundary) | s 7(1) (R7) |
| V5 | act done with no order yet made | barred (before the making of any order) | s 7(1) |
| V6 | another system of units lawfully used | legal force unaffected | s 7(2) |
