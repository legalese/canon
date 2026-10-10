# Prisons Act 1933 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, with amendments to Act 21
of 2025 (in force 17 August 2026) and S 561/2026 (in force 17 August 2026) shown. The
arrangement of sections at the top of the deposit is out of step with the body; the
body's numbering is followed (unauthorised articles is s 66 in the body).

**Checks:** one case file, 109 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**19 of the 527 Singapore Acts** deposited here cite it. This row takes what a
prisoner, a prisoner's family or a defence practitioner meets: who is entitled to
remission and when the remission order must be made (ss 50E, 50G-50J, 50ZA, 50ZB),
how the unserved remainder is split (s 50K(3)), extension while unlawfully at large
(s 50N), the basic condition and the enhanced sentence for breaking it (ss 50S, 50T),
home-detention eligibility (ss 52, 53 and the Second Schedule), and the offence of
bringing unauthorised articles into or out of a prison (s 66). Not encoded: prisons
and officers, committees of inquiry, custody and removal, the mandatory aftercare
scheme and its First Schedule, life-sentence remission beyond the review, the
transitional Division 7, release on licence (Part 5C), Parts 6A and 6B, prison
offences and punishments, and Part 8.

## What the Act turns out to say

### 1. Time added for breaking a remission order earns no remission

s 50I(1)(b): where a prisoner is serving an enhanced sentence (s 50T(1)(a) or 50ZN)
or a term for a s 50Y(1) offence alongside other terms, the order is made only after
**all** of the enhanced time plus two-thirds of the rest. The Act's illustration (b):
one year for theft and two years enhanced gives two years and eight months. And s
50H(3) denies remission altogether where the sentence consists wholly of such terms.
Asserted.

### 2. Misbehaviour in prison is counted at one-third, forfeiture in full

s 50I(2): one-third of time in a punishment cell and one-third of time in hospital
"through his or her own fault or malingering" are not reckonable as served; forfeited
remission (unless restored) and any Presidential deferment are not reckonable at all.
Illustration (c), one year with three months in hospital by own fault, moves the
order from 1 September to 1 October 2013. Asserted (in days).

### 3. A fine does not break the basic condition; corrective or reformative training does

s 50S(1)(b): the basic condition is broken only by an offence while the order is in
effect **and** a sentence of imprisonment "(not including a default sentence)",
corrective training, reformative training, preventive detention, an SPP or an SEPP
(items (iv) to (vi) each annotated "Act 5 of 2024 wef 31/07/2026"). A fine, or
imprisonment in default of paying one, does not. Offences under s 50Y(1) are excluded.
Asserted.

### 4. The cap on an enhanced sentence is frozen at the date of the offence

s 50T(1)(a), (2)(b), (4): an enhanced sentence cannot exceed what remained of the
order on the date of the offence; later extensions are disregarded; several enhanced
sentences together are capped by the remainder at the earliest offence. The Act's own
illustration (offence A capped at 1 August 2013 to 7 January 2014; B at 21 October
2013 to 17 January 2014; together at A's cap) is reproduced. The day count is an
inference: the text says "the length of the period from" one date "to" another, and
this row counts both days (160 and 89). Asserted.

### 5. Short sentences get nothing: 14 days is a floor and a bar

s 50H(2): an aggregate term of 14 days or less earns no remission; s 50I(1)(a)(ii):
for anyone else the order cannot come before 14 days are served, so a 15- or 21-day
term is served for 14 days, not two-thirds. Asserted.

### 6. Home detention: four weeks, fourteen days, and a long disqualification list

s 53(1): the term must be at least 4 weeks and 14 days must have been served. The
Second Schedule disqualifies a lifer, a commuted capital prisoner, anyone "liable to
be removed from Singapore" on completion of sentence, anyone previously released on
home detention for the same sentence, and anyone convicted of a long list of
offences, among them Misuse of Drugs Act s 5, 7, 11F, 11H, many Penal Code offences
(rioting, outraging modesty, voyeurism and other sexual offences, s 224 escape),
Moneylenders Act s 19, 47, 49, and, from 3 August 2026 (S 525/2026), Tobacco and
Vaporisers Control Act s 19B and 19C. The Minister may lift a disqualification (s
53(2)). Theft and cheating, the offences in the Act's own illustrations, are not
listed. The period may not exceed 12 months (s 52). Asserted.

### 7. Almost anything is an unauthorised article

s 66(4): a letter, a document, an electronic storage device, drugs, food, drink,
clothing and money are unauthorised outright, and (g) "any article not specifically
authorised by the Commissioner" catches everything else. Conveying one to a prisoner,
bringing one in or out, or making a recording in a prison without authority is an
offence: up to $3,000, 12 months, or both (s 66(3)). Asserted.

## What would need doing before this is worth anything

- Days are used throughout; the Act counts in days for s 50K but does not say how a
  two-thirds fraction of a day is handled. The cases choose terms divisible by 3.
- The Act's illustrations are in calendar dates; the cases restate them as day
  numbers (1 January 2013 = day 1) and approximate illustration (b) and (c) with
  360-day years.
- s 50I(2)(e) (prescribed periods), the Gazette substitutions in ss 52 and 53, and
  the mandatory aftercare First Schedule were not read into the encoding.
- The Second Schedule Penal Code list is represented by a handful of entries, not
  all forty-odd.
- No regulations, Prison Standing Orders or case law were retrieved.
