# Encoding notes: Residential Tenancies Act 1987 (WA), LQA steps 4A and 5A

Subject `residential-tenancies-act-lqa`. Instrument: Residential Tenancies Act 1987 (WA), consolidated
version 07-a0-00 (currency start 29 April 2026), with the Residential Tenancies Regulations 1989 (WA)
05-ad0-00. Encoded by Claude (agent), for Legalese, on 4-5 October 2026, after 3H was signed on
4 October 2026. As written, nothing here had been through 6H; MICHAEL FAIRWEATHER certified 6H on
5 October 2026, and the two lines below that say 6H is not started describe the state at 5A.

This run was independent of the earlier subject `subjects/au/wa/residential-tenancies-act/`: nothing in
it was opened, read or listed. The only other material reused is the WA jurisdiction library module
`wa-interpretation-act-1984.l4`, copied byte for byte.

## The brief

The human commissioned this run to test whether Western Australia's once-in-12-months limit on rent
increases can be avoided by ending a tenancy and starting another, as Queensland's 2023 limit could
be until it was attached to the premises in 2024. The run was to pay particular attention to how
ss 30, 31A, 31B, 64, 70A and 76C fit together across consecutive agreements: the same parties,
different tenants, a gap between agreements, fixed term to periodic, periodic to fixed term, and a
rent set by a new agreement against an increase by notice under s 30. The encoding was to say what the
text says, with the forks it raises, and not decide whether anything is a defect (that is for 7A-9A).
Candidate issues are the numbered notes at the end, each with the provision, what the text forces and
how it surfaced: **ENC** (writing the encoding forced the question), **TST** (a written test surfaced
it), **RD** (a casual reader would have caught it) or **CMP** (found by setting two documents side by
side; the pipeline's method between RD and ENC).

The Queensland texts in `sources/` (the 2023 and 2026 reprints of ss 91-93B) were read for the
comparison the brief draws and are not encoded.

## What is encoded

| Module | Provisions | Lines |
|---|---|---|
| `part-1-definitions.l4` | s 3 (the terms the scope uses), s 3A; the nouns every module reads; day numbers and the Interpretation Act counts | 506 |
| `part-3-div-3-retaliatory-action.l4` | ss 26A, 26B | 123 |
| `part-4-div-1-rent-and-bonds.l4` | ss 27, 27AA, 28, 29(1)(b), (2), (3), 30, 31A, 31B, 31 (with r 5CB), 32(2), (5), (7) | 878 |
| `part-5-termination.l4` | ss 60, 64, 65, 70, 70A (with r 7D), 76C | 447 |
| `part-6-boundary.l4` | ss 82 (with r 7F), 85 (with rr 7FA, 12I): boundary modules REF-77, REF-82 | 137 |
| `part-7-transitional-2024.l4` | ss 99, 100; s 30 as in force before 29 July 2024 | 254 |
| `regulations-1989.l4` | rr 5B, 5CA, 5CB, 7D, 7F, 7FA, 10AD, 10A, 11, 12I | 210 |
| `wa-interpretation-act-1984.l4` | byte-identical copy of the jurisdiction library module (Interpretation Act ss 61, 62, 71, 72) | 338 |
| `wa-interpretation-act-extra.l4` | Interpretation Act ss 5 ("amend", "repeal"), 16(2), 37(1)(b), 74 | 69 |
| `cases.l4` | 320 assertions, rule by rule | 808 |
| `cases-consecutive.l4` | 99 assertions, the brief's scenarios A-K | 389 |

`coverage.json` lists each Part with its modules and provisions, and what is not encoded and why.
`registers/fork-register.json` holds 26 forks (FK-01 to FK-26). Every rule carries an `@ref`; helpers that
implement no provision (calendar conversions, list utilities, constructors for the cases) say so in a
comment.

The module names are those the reference register proposed at 2A, not the names suggested in the brief
(`definitions`, `part-iv-rent`, ...): the checker treats each module the register names as a file that
must exist, and the register is covered by the 3H signature, so it was not changed.

## How the encoding reads

**Nouns first.** `part-1-definitions.l4` declares the records every other module reads: a
`Residential tenancy agreement` (its name, lessor and the lessor who granted it, tenants, premises,
kind, rent basis, the day it was entered into, the day its tenancy commenced, expiry day, the rent it
fixes, whether increases are set out or excluded, its s 70A notices, the day possession was delivered
up, the day it terminated, and status facts the Regulations read); a `Rent history` (every agreement
for the premises and every increase or change of method that has taken effect); a
`Notice of increase of rent`; and the `Giving of a notice` that s 85 reads.

**Days.** Every date is a day number (days since 1 January 1970), made with `day number` y m d through
the jurisdiction library's calendar. Periods are counted under Interpretation Act s 61 (days) and s 62
(months), encoded in the library and wrapped in `part-1-definitions.l4`. Public holidays are an input
(a list of day numbers); Saturdays and Sundays are computed.

**Facts.** Whatever the reference register supplies as a fact is an input: whether a form is approved,
which court is competent, whether a notice of termination on a ground was given, whether a court made
an order and when it operates, abandonment, merger, whether the Act applies (s 5), the status facts the
Regulations read, the day a posted letter would be delivered in the ordinary course of post, motive
(ss 26A, 65(2)), intent (s 82(2)). The day an agreement terminated is an input decided by the s 60 rule
(or supplied).

**Readings.** The taken reading of each fork is the plain name; each rejected reading is encoded beside
it under a name beginning with the fork's id (`FK-16 reading B -- ...`), or reached through the reading
selectors `Reading of s 30(1)(b)` and `Reading of s 31B` (`on` k `, s 30 -- the notice ...`). The cases
assert both readings on the same facts.

## What the encoding says about the brief

On the readings taken (scenario letters are the sections of `cases-consecutive.l4`):

- **A rent fixed by a new agreement is not limited by s 30 at all** (FK-01 A). Section 31B carries across
  agreements only increases under s 30 and changes under s 31A; a further agreement between the same
  parties may fix any rent, at every renewal. Six-monthly fixed terms at $500, $550 and $600 are lawful
  (F), where the same rises by notice under one agreement are not. On FK-01 B each such rent is an
  increase made otherwise than under s 30, which "shall not" happen.
- **Where s 31B applies, the 12 months run from the last increase by notice, not from the new
  agreement** (A). A1's rent rose by notice to $530 on 1 January 2026; A2, the renewal, fixed $600 from
  1 January 2027; a notice under A2 may raise it to $650 from 3 March 2027. Without the continuation (a
  one-day gap, B, or FK-16 B) the next increase by notice could not take effect before the new
  agreement's first anniversary.
- **The limit attaches to the parties, not the premises** (C). A new tenant (or, on FK-13 B, a new
  lessor) means a fresh agreement, a rent set at will and a fresh 12 months; one co-tenant in common is
  enough to continue.
- **A gap of one day ends the continuation** (B, J), and so does any start that is not the day after the
  end of the existing term (K: a s 70A notice that moves the end of the term moves the day a new
  agreement must start).
- **Fixed term to periodic under s 76C is the same agreement** (D): its increases count, the 12 months
  run from its first commencement (FK-19 A), and a notice given during the fixed term may raise the rent
  from the day after it (FK-03 A).
- **Periodic to fixed term** (E): s 60(1) has no circumstance in which an agreement ends when the parties
  replace it and the tenant stays, so the periodic agreement does not end and the new one continues
  nothing; if the tenant gives up vacant possession under a written agreement and the new agreement
  begins the next day, it is a continuation (FK-17 A).
- **Renewing a fixed term without a s 70A notice** (A, F): no s 60 circumstance ends the old agreement
  either, and s 76C continues it as a periodic tenancy beside the new one.
- **Income-based rent** (J) behaves the same way under ss 31A and 31B(1)(b).
- **Ending a periodic tenancy without grounds** (I): a s 64 notice of 60 clear days ends it; s 26A treats
  that as retaliatory action only where a s 26B(2) matter motivated it, and offering a further agreement
  at a higher rent is not within s 26A (FK-11 A).

## Decisions recorded

- **The jurisdiction library module** is copied byte for byte into this folder (l4 imports only from its
  own folder) and not edited. Both copies are checked by the checker.
- **Interpretation Act provisions beyond the library** (ss 5, 16(2), 37(1)(b), 74) are encoded in the
  subject-level boundary module `wa-interpretation-act-extra.l4`. They are not in the reference register:
  they are one step deeper than depth 1, taken because forks FK-04, FK-21 and FK-26 turn on them.
- **s 30 as in force before 29 July 2024** is encoded in the Part 7 module, as the present text with the
  two changes the 2024 Act s 25 made reversed; s 30 as in force before 1 July 2013 is not encoded beyond
  r 5CA (see `coverage.json`).
- **Notices sent by email.** `s 85 -- the day the notice is given` gives no day for an in-scope notice sent
  by email, even with consent (FK-12 A). The Act fixes no time at which an electronic notice is given;
  where email is a prescribed means (an authorised notice) the encoding takes the day it is sent.
- **The console scheme is not drafted here.** The brief leaves it to another agent and asks for the
  scheme field to be null or omitted "as the schema allows". The schema
  (`tools/lqa/schemas/coverage.schema.json`) requires `scheme` and requires it to be an object with a
  `file` and an `id`, so neither is allowed: `coverage.json` names the file and id the scheme is to have
  (`scheme.js`, `residential-tenancies-act-lqa`). Until that file exists the checker reports
  "scheme: scheme.js does not load" under 4A, which keeps 4A OPEN and every later step WAITING.

## Limitations of the installed l4 (April 2026 build) worked around

1. Its `prelude` and `daydate` libraries provide nothing: list helpers (membership, latest, count) and
   the greater or lesser of two numbers are written out; dates use the library module's calendar.
2. No `REFUSE`: where the Act gives no answer the encoding returns `NOTHING` (e.g. no day of giving) and
   the case says so.
3. `NOT a OR b` parses as `NOT (a OR b)`: every negation is parenthesised.
4. No `verify` command; checking is `l4 check` and the cases are `#ASSERT`s run by `l4 run`.
5. `IMPORT` finds only modules in the same folder: hence the library copy.
6. A `GIVEN` with a `LIST OF` parameter followed by a comma and another parameter does not parse; such
   parameters are written one to a line.
7. The parameters on `GIVEN` must be in the order they appear in a mixfix name.
8. A one-argument mixfix name may not end with a keyword segment, and a plain function may not share its
   name with the head of a mixfix function of the same arity (a call is matched by arity and the mixfix
   wins): the date constructor became `day number`, and the mixfix heads that began with `day` were
   renamed (`is day` d `during the currency of ...`).
9. A parameter may not share a name with a top-level name in scope, including record fields and enum
   constructors (`given`, `way`, `on`); and a function head may not equal an enum constructor
   (`a periodic tenancy` became `the periodic agreement` for the constructor function).
10. Compound arguments of mixfix calls, and mixfix calls inside `AND`/`OR`, need parentheses; in a
    one-line record literal a `LIST` field needs parentheses before the next comma.
11. When a `...`/`..` chain puts its connectives at the same column as an `OR` or `AND`, the linter warns
    of a possible "precedence error"; the LQA checker fails 4A on the word "error" in `l4 check` output,
    so every chain keeps each label and its node on one line.

## Numbered notes

Candidate issues for 7A-9A. None is decided here to be a defect.

- **N-01 (ENC) ss 30(1), 31B(1).** A rent fixed by a further agreement is not an increase under s 30, and
  s 31B carries only increases under s 30 (and changes under s 31A) across agreements (FK-01). So the
  12-month limit does not reach a rise made by a new agreement between the same parties, at any interval
  (F); nor does s 31 (a bond increase needs a notice under s 30 or 31A, while a new agreement may take a
  new bond under s 29 at its own rent). This is the position Queensland's 2023 text stated in a note to
  its s 91. The explanatory memorandum for Bill 140 describes s 31B's purpose more widely than its text.
- **N-02 (TST) s 30(1)(b) with s 31B.** Because the "or, if the rent has been increased under this
  section" limb displaces the commencement limb, s 31B carries the last increase by notice into the
  continuing agreement and the 12 months run from it, not from the continuing agreement's own start: an
  increase by notice may follow the new agreement's higher rent within weeks (A: $530, then $600 by
  agreement on 1 January 2027, then $650 by notice on 3 March 2027). Without the continuation the
  interval would be at least 12 months.
- **N-03 (RD) s 31B(2)(c).** "starts immediately after the end of the term": a gap of one day takes a new
  agreement outside s 31B (B, J).
- **N-04 (ENC) s 31B(2)(c) with ss 70A(2), 76C.** For a fixed term renewed by a new agreement with no
  notice under s 70A, s 70A(2) says the term "does not end on the expiry day", and s 76C continues the
  agreement; read with them, the commonest renewal is never "immediately after the end of the term"
  (FK-16).
- **N-05 (ENC) s 60(1).** No circumstance in s 60(1) ends an agreement that the parties replace while the
  tenant stays: (g) requires vacant possession, and the opening words exclude the general law (surrender
  by operation of law). On the text the old agreement continues beside the new one (for a fixed term,
  under s 76C) in every renewal and every periodic-to-fixed change made in place (A, E(i), F).
- **N-06 (ENC) s 31B(2)(c).** "the end of the term" has no evident meaning for a periodic existing
  agreement; "term" elsewhere means a fixed term (FK-17). On one reading periodic-to-fixed changes are
  never continuations.
- **N-07 (TST) s 31B(3).** The limit follows the parties: a new tenant, or (on FK-13 B) a purchaser who
  makes a new agreement, starts a fresh 12 months at a rent set at will (C). Queensland's 2024 text
  attaches its limit to the premises.
- **N-08 (ENC) s 26A(a)(ii), (iv).** A rise made by offering a further agreement at a higher rent is not
  "increases the rent payable under the residential tenancy agreement", and (iv) reaches only a refusal
  of a further agreement (FK-11; F). A retaliatory rise by renewal is outside s 26A on the reading taken.
- **N-09 (ENC) s 32(2).** An application must be made within 30 days after the tenant receives notice of
  an increase or of a change of method, or after a reduction in chattels or facilities. A tenant whose
  rent was set by a new agreement (including a first agreement with a new tenant) has no such trigger,
  so s 32 is out of reach unless entering into an agreement is "notice of an increase in the rent
  payable" (F).
- **N-10 (ENC) s 32(5).** An order lapses at "the expiration of the tenancy of the person who applied";
  ending the agreement and making a new one with the same tenant ends the order, and the new rent may
  exceed it (FK-23; H).
- **N-11 (ENC) s 100(4).** Read literally it reaches notices given before 29 July 2024 whose increases had
  already taken effect, and gives them no effect if they did not meet the 12-month rule (FK-21).
- **N-12 (ENC) s 100(4), s 88C; s 99(3).** Compliance "with that section as in force from the
  commencement" includes "the approved form", a form approved under s 88C, which came into operation on
  29 July 2024: no notice given before then could be in such a form. Conversely a notice for an agreement
  within s 99 after 29 July 2024 must be "in a form approved by the Minister", while the published Form 10
  is approved by the Commissioner under s 88C (source bundle, `cp-form-10`). No transitional provision
  deals with forms (FK-26).
- **N-13 (ENC) s 99(3).** It does not say which version of s 30 governs a notice given during the current
  term for an increase to take effect after it (FK-22).
- **N-14 (ENC) ss 30(1)(a), 31A(2)(b)(i), 64(2) and 31(1B)(a).** "not less than 60 days after" is counted
  under Interpretation Act s 61(1)(f) (the 61st day), "earlier than 60 days after" under s 61(1)(b) (the
  60th): a bond notice and a rent notice given the same day yield days one apart (FK-06). Different words
  for what may be meant as the same period.
- **N-15 (CMP) s 70A(3) and Regulations Schedule 4 Form 1C, item 5.** The prescribed form calls the s 70A
  notice one "of NOT LESS THAN 30 DAYS"; s 70A(3) requires it "not later than 30 days before the
  possession day". Under Interpretation Act s 61 the form asks one day more than the section.
- **N-16 (ENC) s 70A(3) with Interpretation Act s 61(1)(h).** Where the 30th day before the possession
  day is an excluded day, the notice may be given on the next day that is not, shortening the notice
  below 30 days (FK-08).
- **N-17 (ENC) s 70A(3).** No consequence is stated for a notice given late (FK-07).
- **N-18 (ENC) s 76C(1) with s 70A(5).** "unless the agreement is terminated before the expiry day" does
  not provide for termination on the expiry day, or for a possession day later than it: read literally,
  s 76C continues an agreement that s 60(1)(b)(i) has ended, and makes periodic an agreement that
  s 70A(5) keeps as a fixed term (FK-09, FK-10).
- **N-19 (ENC) s 64(4)(c).** "the later of (i) a day not less than 60 days ... or (ii) a day within 7 days"
  names two ranges, not two days: the operative day is not fixed by the words (FK-05).
- **N-20 (ENC) s 85(1)(c), r 12I.** No electronic means is prescribed for any notice in scope, so a rent
  increase notice (or a notice under s 31A, 31, 64 or 70A) cannot be given by email under s 85, even with
  the tenant's consent (FK-12).
- **N-21 (RD) r 10AD.** Rows 2 and 3 of the Table overlap for premises south of the 26th parallel at $1 200
  or more a week (FK-14).
- **N-22 (RD) s 31A(1).** "otherwise the rent must not increase or be increased" literally bars a rise in
  income-based rent from a higher income under the unchanged method (FK-20).
- **N-23 (RD) ss 31(1A), 100(4), r 5CB; s 31A.** A notice under s 31A is called a "notice of increase in
  rent" even where its change lowers the rent (FK-25); s 31A(1) speaks of "the method by which the rent is
  calculated", s 31A(2)(b)(ii) and s 31B(1)(b) of "the means of calculating rent".
- **N-24 (RD) s 29(3).** The deeming is hard to read: "the amount (if any) allowed by subsection (1)(b)(ii)"
  is "deemed to have been paid as a security bond" (FK-24).
- **N-25 (ENC) s 30(2)(a).** "not exercisable ... during the currency of that term" does not say whether the
  bar is on notices given during the term or on increases that take effect in it (FK-03).
- **N-26 (ENC) s 30(1)(b).** "the day on which the tenancy commenced" is not settled for a continuing
  agreement under s 31B (FK-18) or an agreement continued under s 76C (FK-19).
- **N-27 (ENC) s 30(1), r 5B.** Where r 5B disapplies s 30(1), it disapplies its closing words too ("but
  otherwise the rent shall not increase or be increased"): for those agreements the Act sets no interval,
  notice period or form for increases at all.
- **N-28 (ENC) s 82.** An agreement made to avoid the 12-month limit is an offence under s 82(2) only if
  made "with intent ... to defeat, evade or prevent the operation of this Act", a fact; s 82(1)(a) does not
  avoid it, since on FK-01 A it is not inconsistent with s 30 (F).

## Running

From the subject folder, with the installed binary (`C:\Users\micha\AppData\Local\Programs\l4\l4.exe`):

```
l4 check part-4-div-1-rent-and-bonds.l4      # any module
l4 run cases.l4                              # 320 assertions
l4 run cases-consecutive.l4                  # 99 assertions
```

From the repository root: `node tools/lqa/check.js subjects/au/wa/residential-tenancies-act-lqa --l4`.

## Console scheme

`scheme.js` (id `residential-tenancies-act-lqa`, the file and id `coverage.json` names) was drafted at 4A on
5 October 2026 by a second agent, from the L4 modules and cases above, following reading A of every fork.
It replaces the bullet under "Decisions recorded" saying the scheme is not drafted here. Nothing in it is a
finding; observations name the numbered notes they correspond to.

**What it models.** People (lessors, tenants, co-tenants, buyers), residential premises, agreements (fixed
term or periodic, with their rent, bond, rent history and continuation chain) and a competent court. Acts:
entering into an agreement (a further one with the same parties, after a gap, or with a new tenant or
lessor), notices under ss 30, 31A, 31, 64 and 70A, withdrawal, offers and refusals of a further agreement,
sale of the premises (s 3 "lessor"), joining and leaving as co-tenant (s 60(2)), delivering up possession,
applications under ss 26B, 32 and 64(3), and the court's decisions under ss 26B(4), 32(4)-(5), 64(4) and
65(2). The clock runs s 30(1)(a)-(b), s 30(2)(a), ss 31A, 31B, 70A, 76C, 32(5) and ss 99-100. 51 scenarios:
one or more per key rule, and sections A to K of `cases-consecutive.l4`, each reproducing what the L4
asserts. A simulation section (15 parameters, 22 generators) generates lettings, renewals, increases,
terminations and re-lettings.

**Time.** Months are counted with the library module's day-number algorithm and IA s 62, so the 28 and
29 February edges agree with the L4; "not less than 60 days" is 60 clear days (FK-06 A); a last day on a
Saturday or Sunday moves to the Monday (FK-08 A). Day 0 is 1 January 2024, so a run crosses 29 July 2024.

**Coarser than the L4.** Weekends are the only excluded days; an agreement holds one pending notice of each
kind (a second notice of increase withdraws the first); the regulations' status facts (r 5B, r 5CA, r 7D,
r 7F, s 84 orders) are not offered; two tenant places; a tenancy commences on the day its agreement is
entered in the console. N-21 (r 10AD), N-24 (s 29(3)) and N-27 (r 5B) are not modelled.

**Where the scheme decides what the L4 leaves open.** (1) A notice under s 70A given after the fixed term has
ended is not applied: the L4 tests s 70A(1), (3), (4) with no regard to when the notice is given. (2) Section
65(1) is tested when the lessor's notice is given. (3) A notice of increase is decided on the day it names,
against the rent history then; an agreement re-reads the one it continues, one step back. (4) An application
under s 26B stands for the tenant's reasonable belief. (5) An order under s 32 runs from the day it is made.

**Checks.** The scheme console's checks (`checker.js` with a simulation required, and the steps of
`check.js`, run against this file): no problems; every observation is produced by at least one scenario;
seed 1 replays; a saved run plays back. `node tools/lqa/check.js subjects/au/wa/residential-tenancies-act-lqa --l4`:
4A and 5A DONE, 6H NOT STARTED. (State at 5A. 6H was certified on 5 October 2026; see registers/gates.json.)
