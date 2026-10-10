# Maritime and Port Authority of Singapore Act 1996 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, with amendments to Act 17
of 2025 (in force 1 February 2026) shown.

**Checks:** one case file, 109 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**15 of the 527 Singapore Acts** deposited here cite it. Most of the Act sets up the
Authority and its finances. This row takes the parts a shipowner, agent, master,
pilot, salvor or investor meets: port clearance and its return (ss 46, 47), the appeal
against a direction to leave (s 49), compulsory pilotage (ss 60-64), who answers for a
piloted vessel (ss 71, 72, 74), the Authority's own liability (ss 90, 91), the salvage
licence (s 80), the 5% controller notice (ss 86E, 86I), the maximum penalties for the
offences in ss 39, 44-47, 50, 61, 64, 73, 80 and 92-99, and the ceiling on composition
(s 102). Not encoded: the Authority's constitution, functions and finances, seamen's and
port regulations, wreck removal, the Pilotage Committee, seaward works, public licences,
the 25%/50%/75% controller approvals (s 86F onward), special administration (Part 13) and
Part 16. Dues and fees are set by regulations, which were not retrieved.

## What the Act turns out to say

### 1. Compulsory pilotage does not move liability off the owner

s 71: under compulsory pilotage the master or owner is answerable for loss or damage
"in the same manner as the master or owner would if pilotage were not compulsory". s
74(2) deems the pilot "the employee only of the master or owner" and says the Authority
"shall not be liable". The pilot's own liability, once the $1,000 bond is given, stops at
the bond plus the pilotage payable for the voyage (s 72(1), (2)). A $500,000 collision
claim against a bonded pilot on an $800 pilotage job is capped at $1,800. Asserted.

### 2. The Authority caps its liability for damage to a vessel by gold francs

s 91: unless at "actual fault or privity", the Authority is not liable beyond "1,000
gold francs for each ton of the vessel's tonnage", converted at the rate gazetted under
the Merchant Shipping Act 1995 "as in force before 1 May 2005". The rate is not in this
Act, so it is a parameter. s 90 separately says the Authority is never liable for a public
licensee's default. Asserted.

### 3. An unused port clearance has a 6-hour return window

s 47: a vessel that does not leave within 48 hours of clearance, or any shorter period the
Port Master sets, must return the clearance within 6 hours after that period. That is hour
54 by default, or the shorter period plus 6. Fine up to $5,000, and the vessel may be
detained. Asserted.

### 4. Two penalties carry double dues, and paying up later does not help

Failing to take a pilot when required (s 61) and evading dues (s 94) each carry a fine
plus "as penalty double the amount" of the dues. s 94(2): later payment or acceptance of
evaded dues "does not release or discharge" the person. Asserted.

### 5. The 5% controller offence is strict, with two narrow defences

s 86E: notice is due within 7 days of becoming a 5% controller of a designated entity.
The only defences are being unaware and notifying within 14 days of finding out, or an
associate's increase with no arrangement between you and notice within 7 days "after the
contravention". s 86E(5) rules out any other lack-of-intent defence. The penalty in s 86I
is up to $500,000 for an individual and $1 million otherwise. Counting "after the
contravention" from day 7 is an inference: the Act does not say when the contravention
happens. Asserted.

### 6. Port clearance exemptions turn on freight or fares, not on ownership

s 46(3): warships and Government vessels are exempt "unless the vessel is carrying or
habitually carries cargo or passengers for freight or fares". A Government ferry carrying
fare-paying passengers needs clearance. s 46(5) lists when clearance must be refused
(import or export law not complied with, or the flag not declared), and s 46(6)-(8) when
it may be. Asserted.

### 7. Composition is capped at the lower of half the maximum fine or $2,000

s 102(1). So $1,000 for a $2,000 offence, and $2,000 for anything with a fine of $4,000 or
more. Which offences can be compounded is left to regulations. Asserted.

## What would need doing before this is worth anything

- The regulations (port dues, pilotage, compoundable offences) were not retrieved. The
  fees and dues that feed ss 61 and 94 are therefore inputs.
- The gazetted value of 1,000 gold francs (s 91(2)) was not found.
- The 25%/50%/75% controller approvals (s 86F) and remedial directions are not encoded.
- s 64(4) (acting as pilot of a vessel in distress) is encoded as excusing the s 64(1)
  offence only. Whether it reaches the s 61 or s 64(2) offences was not settled.
- No case law was searched.
