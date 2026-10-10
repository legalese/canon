# Public Order and Safety (Special Powers) Act 2018 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, as deposited at
`../../registers/source-bundle/POSSPA2018.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021"; the latest amendment annotated in
the text is Act 3 of 2021 wef 01/07/2025 (the definition of "dangerous article"). The
arrangement of sections at the head of the deposit is out of step with the body (its
first numbered entries are shifted); the body's numbering is followed throughout.

**Checks:** one case file, 56 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**6 of the 527 Singapore Acts** deposited here cite it. This row takes what a member
of the public, an occupier or a practitioner meets once the powers are switched on:
the time limits on activation orders and special authorisations (ss 8-11, 14), who may
exercise a special power (s 15), the 24-hour road-closure limit (s 19(3)), the
non-compliance offences (ss 16-20, 29) and the lifespan of a temporary restraining order
(ss 29, 49), the Part 6 offences and penalties (ss 37-44), and arrest, bail and detention
(s 48). The definitions of "serious incident" and "act of serious violence" (ss 3, 4)
are reduced to a flag. The search, seizure and drone-interception powers (ss 22-28),
communications stop orders and telecommunication directions (ss 30-34, except the s 44
offence), requisition (ss 35, 36), corporate liability (ss 45, 46), service and
regulations are not encoded.

## What the Act turns out to say

### 1. Penal Code ss 427, 435 and 436 in a target area are non-bailable, but are not on the s 48(1) arrestable list

s 48(1)(b) makes Penal Code ss 143 ... 382 committed in a target area arrestable. s 48(2)(b),
as amended by 15/2019, adds ss 427, 435 and 436 to the list for which an officer may use
force "including the use of lethal weapons" to arrest. s 48(6)(b) makes every offence
"mentioned in subsection (2)(b)" committed in a target area non-bailable — so it picks up
the three added sections, while s 48(1)(b) does not. Whether those offences are arrestable
under the Criminal Procedure Code anyway was not checked (inference: the gap may be
harmless). The s 42 doubling list also omits them. Asserted.

### 2. A civilian may be told to help police — but only with some powers, and never with lethal force

s 15(3)(b) lets "an individual (who is not a serviceman)" act as a civilian assistant on a
granted officer's direction. s 15(4) confines that to ss 18, 19(1) or (2), 20(1) or (2), 24
and 27(1)(a) or (b) — cordons, road closures, movement directions and dispersal, moving
vehicles, and directing occupiers to close premises or restrict entry — and bars "lethal
force". A civilian may not help search an individual (s 22), impose a curfew (s 21) or
demand an occupier's documents (s 27(1)(c)). A plain-clothes officer may act "only after he
or she produces a warrant". Asserted.

### 3. Knowledge is not an element of the publication, drone and stop-order offences

s 38(2): the prosecution need not prove that the accused knew or had reason to believe a
document contained prejudicial matter — and the offence covers mere possession. s 43(2)(a):
nor that the drone operator knew the area was a target area; the only defence is proving
the picture was taken unintentionally "because of weather conditions or other unavoidable
cause". s 44(3): the only defence is the Commissioner's prior approval. Asserted.

### 4. An occupier is taken to possess a weapon found on the premises, and a hoard is presumed hostile

s 41(6): the occupier is taken to possess an offensive weapon found there unless he proves
someone else had it, or proves both no knowledge and all reasonable precautions. s 41(7):
excess quantity, concealment or unusual containers raise a presumption of a purpose
prejudicial to public order. s 41(5) lets the accused prove a solely lawful purpose on a
balance of probabilities. Asserted.

### 5. Doubled sentences for ordinary crimes in a target area

s 42: offences under the listed Penal Code 1871 sections (143-158, 267B, 379-382),
committed or attempted within a target area (or abetted from anywhere in Singapore), carry
imprisonment up to "twice the longest term provided for that offence". The Part 6 offences
themselves run to 10 years and caning (s 39), 7 years and caning (s 40), 5 and 3 years with
caning (s 41), 3 years (ss 37, 38), and $20,000 or 2 years for drone photography, stop-order
breaches and non-compliance with special powers or restraining orders. Asserted. (The Act lists
the Penal Code offences by number only; their content was not read.)

### 6. Time limits: one month, one month, 24 hours, 48 hours

An activation order may last no longer than one month (s 10(2)) but may be renewed (s 10(3));
a special authorisation must sit inside the activation order (ss 11(1), 14(2)); a road
closure lapses after 24 hours unless the Commissioner confirms it in time (s 19(3)); an
arrested person must not be held beyond 48 hours, excluding the journey to the Magistrate's
Court (s 48(4)). A temporary restraining order runs despite an appeal (s 49(3)) and lapses
with the special authorisation (s 29(3)(b)). Failing to publish an activation order does not
invalidate it (s 8(3)). Asserted.

## What would need doing before this is worth anything

- "One month" is taken as a count of months supplied by the user; the Act does not say how
  it is reckoned.
- s 19(3) confirmation is one flag, not a chain of 24-hour confirmations.
- The ss 22-28 powers and the communications stop order regime (ss 30-34) are not encoded.
- The Criminal Procedure Code's own arrestability schedule was not read, so finding 1 is a
  reading of s 48 alone.
- No case law or subsidiary legislation (including any prescribed appeal time under s 49(2))
  was retrieved.
