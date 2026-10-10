# Biological Agents and Toxins Act 2005 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. Not for public use.

**Edition:** 2020 Revised Edition, informal consolidation. The deposit's title page
says the revised edition "incorporates all amendments up to and including
1 December 2021 and comes into operation on 31 December 2021"; the running footer
says "Informal Consolidation – version in force from 9/10/2023". The latest
amendment annotated in the text is S 657/2023 (in force 9 October 2023); Act 11 of
2023 (in force 1 May 2023), which substituted the Director‑General of Health for the
former authority throughout, is annotated section by section. Deposited at
`../../registers/source-bundle/BATA2005.txt`.

**Checks:** one case file, 60 assertions satisfied, 0 errors, 0 warnings
(`l4 run bata-cases-approvals.l4`).

## Why this Act, and why scoped

Requirement **REQ-0086** in `../../../requirements.jsonl`: tier 2 of the remaining
Singapore Acts, ordered by everyday-life relevance. The requirement asks what the Act
decides for a person or business it applies to; no scenario has asked a sharper
question yet.

The Act's own content is two things: lists of organisms and toxins in five Schedules,
and a scheme of approvals, permits, duties and penalties built on top of those lists.
This row encodes the **scheme**, taking the class of the thing as given. It does not
reproduce the Schedules: which organism sits in which class is a factual lookup, it
changes by Gazette order every year or two (nineteen items of legislative history,
most of them Schedule amendment orders), and the encoding does not need it to answer
"what must I hold, by when, and what is the maximum if I get it wrong".

Not encoded: the Schedule contents; ss 5 and 30 (use for a non‑peaceful purpose)
beyond their penalty and their place in the Eighth Schedule; the Director‑General's
powers of entry, inspection and cessation orders (ss 52, 53) beyond the penalty for
disobeying an order; the application and revocation machinery in s 50 beyond
s 50(6); the detail of the operator's duties in ss 40 to 44 beyond the fact of them;
ss 56, 57 (officers and principals), 60 (appeal), 61, 62, 63.

## What the Act turns out to say

### 1. Unapproved large-scale production of a Third Schedule agent is not itself an offence

Section 23(1) says a person "must not carry out or procure any large-scale production"
of a Third Schedule biological agent without an approval. But s 23(2) gives only the
Director‑General's consequential order (cessation, destruction, decontamination,
closure, examination or quarantine of anyone exposed), and s 23(3) makes the offence
**contravening that order** — $10,000 or 12 months. On the words of the section the
production itself carries no penalty, where the same conduct with a First Schedule
agent carries $100,000 or 10 years (s 7(3)(a)). Asserted
(`the maximum fine for unlawful large-scale production`).

### 2. The heaviest penalty in the Act is for disobeying an order, not for the production

Large-scale production of a Second Schedule agent is flatly prohibited — s 16(1)
offers no approval to apply for — and is punishable by $100,000 or 10 years
(s 16(2)(a)). Contravening the Director‑General's order made because of it is
punishable by **$1 million or imprisonment "for a term which may extend to life"**
(s 16(3)), the same ceiling as using an agent or toxin for a non-peaceful purpose
(ss 5(2)(a), 30(2)(a)). Asserted only as to the production.

### 3. A s 16 offence a District Court may not try is still compoundable for $5,000

Section 58 withholds District Court jurisdiction over ss 5, 16 and 30. But the Eighth
Schedule, which lists the non-compoundable offences, names only ss 5 and 30. So
large-scale production of a Second Schedule agent must go to the High Court if it is
tried — yet the Director‑General may compound it under s 59(1) for "the lower of" half
the maximum fine and **$5,000**, against a $100,000 maximum. Asserted
(`a District Court may try the offence`, `the composition sum`).

### 4. Certification lasts a year, and a refit ends it — and with it the approval to possess

A certification ceases to be valid on the earlier of one year from its date or "any
design or structural change made to the facility" (s 51(2)). Where the Act requires
the facility to be certified, s 50(6)(b) then makes the **approval to possess** cease
to be valid too, automatically, with no decision by anyone. Asserted
(`the certification is still valid`, `the approval to possess is still valid`).

### 5. The protected-place requirement is not waivable; certification sometimes is

For a First Schedule agent the Director‑General may approve possession at an
*uncertified* facility if satisfied the work "will be carried out ... in a safe and
proper manner" (s 6(3)) — but the requirement that a Part 2 facility be a protected
place under the Infrastructure Protection Act 2017 (s 6(2)(b)) has no such escape. For
a Second Schedule agent the facility must be both certified and a protected place
(s 15(2)), with no waiver. For a Fifth Schedule toxin s 31(2) requires a protected
place but, on its words, **not** a certified facility. Asserted
(`an approval to possess may be granted`).

### 6. The transfer offence is narrower than the transfer prohibition

Sections 11(1), 20(1) and 35(1) forbid a transfer unless the transferor holds an
approval to possess and the transferee holds one or is outside Singapore. The offence
in ss 11(3), 20(3) and 35(3) is committed only by a transferor who transfers to a
transferee in Singapore "knowing or having reason to believe" the transferee has no
approval. A transferor with no approval of his own, transferring to someone who has
one, breaches the prohibition and commits no offence. Asserted
(`the transfer is permitted`, `the transfer is an offence`).

### 7. Couriers and warehouses are carved out of possession, and in at 10 litres

The possession offences do not reach a person engaged to transport the thing within
Singapore, or to store it pending delivery to the importer or pending export on
transhipment, whose possession is "merely incidental" to that engagement
(ss 6(8), 14(4), 15(7), 31(6)). Instead Part 5 Division 2 binds carriers: a flat
$10,000 for any breach (s 49), no imprisonment, and for a Third Schedule agent the
Division applies only at "quantities aggregating 10 litres or more ... at any one
time" (s 46(1)(c)). Packing and labelling stays the **transferor's** duty (s 48).
Asserted (`the possession is an offence`, `the carrier duties apply`).

### 8. The notification deadlines are 24 hours, 24 hours and 48 hours

A permit holder is deemed to have failed to receive a consignment if it does not
arrive within 24 hours of the holder's own reasonable estimate, and must then notify
the Director‑General *immediately* — $10,000 (ss 9, 18, 33). The duty falls on the
importer of a First Schedule (Part 2) agent, a Second Schedule agent or a Fifth
Schedule toxin, not of a Part 1 agent. A transferee is deemed to have failed to
receive a transfer 24 hours after the time the transferor estimated (ss 12, 21, 36). A
person aggrieved by a seizure has **48 hours** to complain to a Magistrate's Court,
after which the thing seized "becomes the property of the Government" (s 54). Asserted
(`a failed import must be notified`, `the consignment is deemed not received`,
`the seized matter becomes Government property`).

### 9. Diagnosis, autopsy and finished products are outside Parts 3 to 6 — except for one paragraph

Section 4(1) takes the whole scheme of Parts 3 to 6 off hazardous-waste disposal,
handling in the course of a diagnosis or an autopsy, public-health sampling of food
and the environment, and finished cosmetic or medicinal products containing a toxin —
"with the exception of section 41(e)", the duty not to discharge anything into the
environment without decontamination. The exclusion reverses under s 4(2) and (3) the
moment the thing is used, or passed on, for a purpose outside the excluded list.
Asserted (`the purpose is an excluded purpose`, `Parts 3 to 6 apply`).

### 10. "Large-scale" is about the equipment, not the batch

Section 2 defines large-scale production as production "using equipment at a facility
capable of producing in aggregate 10 or more litres of culture ... at any one time".
Capability, not output, is the trigger. Asserted (`the production is large-scale`).

## What would need doing before this is worth anything

- The First to Fifth Schedules are not encoded at all. Every answer this row gives
  presupposes someone has already classified the organism or toxin, which is the hard
  part in practice and the part that changes by Gazette order.
- The Biological Agents and Toxins Regulations and any other subsidiary legislation
  were not retrieved. Much of the Act's real content ("such requirements as may be
  prescribed" in ss 10, 19, 34, 39(1), 40(a), 41(b), 43, 48, 51(5)) lives there.
- Findings 1, 2 and 3 are readings of the deposited words only. No case law,
  parliamentary debate or MOH guidance was consulted, and each is the kind of gap a
  practitioner would check before relying on it.
- The penalty figures are maxima on conviction. Nothing here models the continuing
  daily fine beyond s 45(1)(a)'s $1,000 a day, the s 55 repeat-offence step, or
  sentencing practice.
- The appeal to the Minister (s 60) is "within such time as may be prescribed" — the
  deposit does not state the period, and the regulations were not retrieved.
