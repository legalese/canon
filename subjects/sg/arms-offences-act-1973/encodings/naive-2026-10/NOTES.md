# Arms Offences Act 1973 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation (version in force from
1 July 2025), with amendments to Act 3 of 2021 (in force 1 July 2025) shown.

**Checks:** one case file, 103 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**12 of the 527 Singapore Acts** deposited here cite it. The Act is short, so this
row takes almost all of it: the definitions in s 2, the offences and punishments in
ss 3 to 8, the occupier's presumption in s 9, and the Schedule of scheduled offences.
Not encoded: ss 1, 11 and 12; the content of the Penal Code Chapter 4 exceptions and
of the Guns, Explosives and Weapons Control Act 2021, which the definitions of "gun",
"unlawful possession" and "trafficking in guns" point to; and Penal Code s 458A in
the Schedule, which is not a whole-number section.

The arrangement of sections at the top of the deposit is one line out of step with
the body (it calls "Unlawful possession of gun with criminal intent" s 3A, which is
s 3 in the body). The encoding follows the body.

## What the Act turns out to say

### 1. Using a gun carries a mandatory death sentence, and the intent is presumed

s 4(1): whoever "uses or attempts to use any gun" intending to injure, endanger,
cause reasonable fear of injury or damage property "shall on conviction be punished
with death". s 4(2) presumes that intent "until the contrary is proved". "Use"
includes holding a gun "so as to cause a reasonable belief that it will be fired,
whether or not it is capable of being fired" (s 2). The only escapes are proving
the contrary or a Penal Code Chapter 4 exception, and s 95 of the Penal Code is
expressly excluded from those exceptions. What s 95 says was not read. Asserted.

### 2. In a scheduled offence, intent does not matter at all

s 4A: using or attempting to use a gun while committing or attempting a scheduled
offence is punished with death "whether or not the person has any intention to cause
physical injury to any individual or property". Asserted.

### 3. Accomplices die too, for a gun used in "any offence"

s 5: where a gun is used in committing or attempting "any offence" (not only a
scheduled one) or an s 4A offence is committed, each accomplice present who "may
reasonably be presumed to have known" of the gun is punished with death unless the
accomplice proves "all reasonable steps to prevent the use of the gun". The burden
is the accomplice's. Asserted.

### 4. A licensee in breach of conditions is not in "unlawful possession", read literally

s 2 defines "unlawful possession" by three limbs joined by **and**: (a) not
authorised by a licence or class licence, (b) not in accordance with the licence's
conditions, and (c) not exempt. A licensee breaching the conditions is still
authorised by a licence, so limb (a) fails; the possession is then not "unlawful
possession", and ss 3, 3A and 7 do not bite. The encoding follows this literal
reading. That it may not be what was intended is an inference; the text does not
say. Asserted.

### 5. Carrying at the moment of arrest is enough for mandatory life

s 3A: a person convicted of a scheduled offence who, at the time of committing it
**or at the time of apprehension** for it, carries a gun in unlawful possession is
punished with life imprisonment and at least 6 strokes. No intent is required.
Asserted.

### 6. Trafficking needs two guns and an intent to harm

s 2 defines "trafficking in guns" as importing, supplying or transferring "2 or more
guns" in contravention of the 2021 Act intending to injure, cause fear of injury or
damage property. One gun is never trafficking; nor is a bulk transfer without one of
those intentions. The punishment (s 6) is death, or life and at least 6 strokes.
Asserted.

### 7. Smaller points

- s 3: carrying with criminal intent: 5 to 10 years and at least 6 strokes; with a
  previous scheduled-offence conviction the maximum doubles to 20, but the minimum
  stays at 5. Asserted.
- s 7: consorting with a person unlawfully carrying a gun attracts "the like
  punishment as that other person"; the defence of reasonable belief is the
  consorter's to prove. Asserted for liability only.
- s 8: exhibiting an imitation gun during a scheduled offence: up to 10 years and at
  least 3 strokes. A real gun is not an imitation gun. Asserted.
- s 9: the occupier of premises where a gun is found is deemed to possess it unless
  the occupier proves another person possessed it, or proves BOTH no knowledge (or
  means of knowing) AND all reasonable precautions. Asserted.
- The Schedule's marginal note cites "Sections 2, 3(3) and (4), 4A, 8 and 12". There
  is no s 3(4) in the body, and s 3A, which turns on a scheduled offence, is not cited.
  Not asserted.
- Theft (Penal Code s 379) and cheating (s 420) are not scheduled; robbery and
  extortion are. Asserted by section number.

## What would need doing before this is worth anything

- The Guns, Explosives and Weapons Control Act 2021 (meaning of "gun", licences,
  exemptions) and the Penal Code Chapter 4 exceptions, including s 95, were not read.
- The literal reading of "unlawful possession" (finding 4) needs checking against
  case law or the 2021 amending Act's debates; none were retrieved.
- s 7's borrowed punishment is not computed.
- Penal Code s 458A and the Kidnapping Act and Vandalism Act items of the Schedule
  are not encoded.
- No cases on ss 4, 4A or 5 were searched.
