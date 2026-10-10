# Corrosive and Explosive Substances and Offensive Weapons Act 1958 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation ("version in force from
17/8/2026"), deposited as `CESOWA1958.txt`. The latest amendment annotated is Act 21
of 2025 wef 17/08/2026 (ss 3, 6(1), 7(1)); the earlier one is Act 3 of 2021 wef
01/07/2025. The deposit shows the amended wording only, not what it replaced.

**Checks:** one case file, 55 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**REQ-0054:** tier 2 of the remaining Singapore Acts, ordered by everyday-life
relevance. The requirement asks what the Act decides for a person or business it
applies to; no scenario has asked a sharper question yet. The Act is short, so nearly
all of it is here: the definition of a corrosive substance (s 2, First Schedule), the
offences in ss 3 to 8 and their punishments, the s 9(3) limit on searching women, and
the presumptions in s 11. Not encoded: the search powers in s 9(1) and (2) beyond that
limit, disposal of seized property (s 10), the power to amend the First Schedule
(s 12), and the meaning of "scheduled weapon" and "prohibited weapon", which come from
the Guns, Explosives and Weapons Control Act 2021 (not read).

## What the Act turns out to say

### 1. Every offence in the Act carries caning, and two make it mandatory

s 3 (up to 10 years), s 6(1) (up to 3 years) and s 7(1) (up to 5 years; 2 to 8 years
for a repeat) each say the offender "shall also be liable to caning". s 4 (using a
corrosive substance or offensive weapon to cause hurt, up to life) and s 6(1A)
(carrying a prohibited weapon in public, up to 5 years) say the offender "shall also be
punished with caning with not less than 6 strokes". s 4 applies "whether any hurt has
actually been caused or not". Asserted.

### 2. Acetic acid, ammonia and sodium hydroxide are corrosive substances, and the occupier is presumed to possess them

The First Schedule lists acetic acid, ammonia and sodium hydroxide among its nine
items, and s 2 deems "all substances which are capable on application to the human
body of causing hurt through corrosive action" to be included. Under s 11(1) the
occupier of premises where one is found is deemed to possess it unless they prove
someone else did, or prove both that they had no knowledge or means of knowledge
**and** that they took all reasonable precautions. (That these substances are found in
households is an inference, not something the Act says.) Asserted.

### 3. Keeping it in the wrong bottle raises the presumption of intent to hurt

s 11(2): in a prosecution under s 3 or 5, intent to cause hurt is "presumed until the
contrary is proved" if the quantity exceeded ordinary household or business needs,
it was concealed or kept somewhere unexpected, or it was kept in a container of a kind
it is not ordinarily kept in. Any one of the three is enough. Asserted.

### 4. Carrying a weapon in public: the purpose is the carrier's to prove

s 6(2) puts "the onus of proving the existence of a lawful purpose" on the accused. The
s 6(1B) list (work, religion, theatre or film, ornamental display, authorised hunting or
slaughter, gardening, animal husbandry or primary production) is open ("includes") and
applies to s 6(1) only. Lawful authority is presumed for the armed forces, the police, a
lawfully present visiting force, and ceremonial dress — but only "on any official or
ceremonial occasion" (s 6(3)). Asserted.

### 5. The scheduled-weapon test in s 7(1A)(b) joins its three limbs with "and"

The act is "otherwise than for a lawful purpose" if the person intends injury, fear
or damage and the possession is "(i) not authorised by a licence ...; (ii) not in
accordance with the conditions of a licence ...; and (iii) not exempt". Read literally,
a licence holder who breaches the conditions meets (ii) but not (i), so (1A) does not
apply to them, and the case falls back on s 7(2)'s onus of proving a lawful purpose.
The encoding takes the "and" at its word; how a court reads it is not attempted.
Asserted.

### 6. A repeat s 7 offence counts convictions, not offences, within 5 years

s 7(4): the earlier conviction must be "within the period of 5 years immediately before
the date on which the person is convicted" of the current offence, and be for the same
offence or an offence under s 7(1) "as in force before" s 94(g) of the Guns, Explosives
and Weapons Control Act 2021 commenced "and that involved a scheduled weapon". Asserted (4
years yes, 6 years no; the boundary at exactly 5 years is not asserted).

### 7. Consorting carries the carrier's punishment

ss 5 and 8: a person who "consorts with, or is found in the company of" someone carrying
in contravention of s 3 or s 6 is liable to "the like punishment", unless they prove
reasonable grounds for believing the purpose was lawful. Guilt is asserted; the
punishment transfer is in a comment only. ss 6, 7 and 8 are deemed arrestable and
non-bailable by the Act; ss 3, 4 and 5 are not so deemed here (the Criminal Procedure
Code 2010 was not read). Asserted.

## What would need doing before this is worth anything

- The Guns, Explosives and Weapons Control Act 2021 definitions of "scheduled weapon",
  "prohibited weapon" and "explosive device" were not read.
- What Act 21 of 2025 changed in ss 3, 6(1) and 7(1) is not visible in the deposit.
- No case law on "offensive weapon", "lawful purpose" or the s 11 presumptions was
  searched.
