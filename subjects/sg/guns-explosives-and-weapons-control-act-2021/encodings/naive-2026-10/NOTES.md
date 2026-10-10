# Guns, Explosives and Weapons Control Act 2021 — naive encoding

**Method: naive.** Straight from the deposited text, following the conventions
of the `writing-l4-rules` skill as shown in the finished naive rows (the skill
itself could not be loaded in this session). No pipeline, no coverage table,
no independent test pass, no human gate.

**Edition:** Act No. 3 of 2021, informal consolidation, version in force from
1 July 2025, as deposited at `../../registers/source-bundle/GEWCA2021.txt`.
The latest amendments annotated are S 354/2025 and S 355/2025, both with effect
from 1 July 2025 (First Schedule items 2, 23 and 24; Third Schedule paragraphs 7
to 11). Act 31 of 2022 is annotated once, at s 97(5). The deposit has no
legislative history and does not say when s 29 came into operation.

**Checks:** one case file, 58 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is requirement **REQ-0053** in `subjects/sg/requirements.jsonl`: Tier 2
of the remaining Singapore Acts, ordered by everyday-life relevance. The
requirement asks what the Act decides for a person or business it applies to.
No scenario has asked a sharper question yet.

The Act runs to some 160 pages. This row covers what an ordinary person
meets. Is the thing I own controlled? Is having it an offence? What is the
most I can be fined or jailed? What must I do if it is lost, inherited or no
longer licensed? The sections are ss 3, 4, 5(3), 11, 17(1), 22, 27, 29, 34, 36,
38, 39, 74 and 85, the First and Second Schedules, and paragraph 11 of the
Third Schedule.

Not encoded:

- the manufacture, trade, supply, conveyance and acquisition offences, except where they share the penalty sections
- digital blueprints (s 13)
- shooting and paintball ranges
- breaches of licence conditions
- security clearance
- licensing procedure and class licences
- business requirements, enforcement powers and appeals
- the defence exemption (s 88)
- the meaning of "store"

No Regulations or class-licence orders were retrieved. So which guns, weapons
and explosives are "prohibited", and which offences can be compounded, are
taken as given.

## What the Act turns out to say

### 1. A longbow, a parang, a diving knife and an axe are all "weapons" needing a licence

The First Schedule lists "A bow regardless of its draw weight, and includes a
longbow" (item 5), swords "including ... a machete, parang, bolo, kukri" (item
7), and stabbing instruments that include "a diving knife, hunting knife, kris,
karambit, kirpan or dirk" (item 8). It also lists "An axe" (item 22).

Possessing any of these at a place without a licence, class licence or
exemption is an offence under s 29(1). Section 29(2) applies it "regardless"
that the thing is not held for business. A pepper spray is a "noxious
substance" under s 2(1), and the same offence applies.

The text sets these out without qualification. Whether a class-licence order
lifts the licence requirement for household items cannot be seen from the
Act. Asserted.

### 2. A crossbow is not a gun, but it is a weapon. A slingshot is neither

Section 3(4)(a) takes "a longbow, crossbow, slingshot or shanghai" out of
"gun". Crossbows and longbows come back in through the First Schedule. A
slingshot does not: it is in no Schedule, so on the deposited text the Act does
not control it.

An imitation gun is excluded by s 3(4)(c). A toy replica bomb is excluded
because "imitation explosive device" in s 4(1) includes any object "produced
and identified as a toy or replica".

By contrast, airguns, tasers, starting pistols and paintball markers are
listed examples of guns. Fireworks, sand crackers and "A nail gun cartridge"
are explosives. Asserted.

### 3. Guns, explosives and weapons carry jail AND a fine. Precursors carry jail OR a fine

For a gun, an explosive or a weapon, the penalty sections say an individual
"shall be punished on conviction with imprisonment ... and a fine" (ss 17(1),
27(a), (b), 34). For an explosive precursor, s 27(c) uses a different form: an
individual is "liable ... to a fine ... or to imprisonment ... or to both".

This row reads the first form as requiring both penalties. That is an
inference from the contrast between the two forms. Non-individuals face only
fines, and they are generally twice the individual figure.

The maximum terms are 5 years for a prohibited gun, a major part of one, or a
prohibited explosive. They are 36 months for an ordinary gun or explosive, and
24 months for an ordinary gun accessory, an ordinary weapon or a precursor.
Asserted.

### 4. The fine for unlicensed guns is set per gun, then capped

Section 17(1)(a) and (b) set the fine at "$10,000 for each fully assembled
prohibited gun involved or $100,000 in total, whichever is the lower". For an
ordinary gun the figures are $5,000 and $50,000. A non-individual's cap is
$200,000 or $100,000.

So three prohibited guns carry at most $30,000 and twelve carry $100,000. A
company with fifteen faces $150,000.

Where no fully assembled gun is involved, the alternative "(B)" cap applies.
That reading of "whichever is applicable" is an inference. Asserted.

### 5. Anyone holding a controlled item must report a loss, and anyone who inherits one must surrender it

Section 36(2) applies to any person who "possesses or stores" the thing, not
only licensees. That person must tell the Licensing Officer "without delay"
once aware of a loss, theft or destruction. The maximum is $10,000 or 12
months.

Section 39 requires a person who comes into possession without authority to
surrender the thing without delay. The illustrations are inheriting a
licensee's gun and unearthing "an undetonated bomb from the time of the
Japanese Occupation". The same applies to a person whose licence expires or is
revoked or suspended. The maximum for an individual is $10,000 or 6 months,
doubled for a repeat offender. A repeat offender is someone with an earlier
conviction within 5 years (s 2(1)).

A transferor must ask to see and inspect the acquirer's licence (s 38). That
duty does not apply to a surrender to the police. Asserted.

### 6. Owning the premises is possession, unless the occupier did not and could not know

Under s 5(1)(e), a thing on premises a person owns, leases or occupies is in
that person's possession. Section 5(3) displaces this if the court is
satisfied, on a balance of probabilities, of either of two things. One is that
the person "did not know and could not reasonably be expected to have known"
the thing was there. The other is that an authorised person is there or
controls it. The defendant "has the evidential burden" (s 5(6)). Asserted.

### 7. The 2025 grace period protects ornamental swords but not a sword kept for use

Paragraph 11 of the Third Schedule, as substituted by S 355/2025, lets a
person keep a weapon they already possessed when s 29 began. The grace period
is 6 months. It runs longer if the person applied for a licence within that
time, ending when the application is decided or withdrawn.

"Weapon" here covers a sword "kept in a dwelling house as a curio or for
ornamental purposes". It excludes a sword not so kept, arrows with broadhead
and similar tips, arbalests, crossbows, and "a bow with a draw weight of more
than 27.215 kilograms". A bow of exactly 27.215 kg is covered.

The deposit does not give the commencement date of s 29. How limbs (a) and (b)
interact when a s 56 order is made is an inference. Asserted.

### 8. Composition is capped at half the maximum fine or $5,000

Section 74 allows a prescribed compoundable offence to be settled for "the
lower of" half the maximum fine and $5,000. A surrendered item becomes
unclaimed 30 days after surrender if no owner has claimed it (s 85(1)). It may
then be sold, and the buyer "acquires good title" (s 85(5)). Asserted.

## What would need doing before this is worth anything

- The Regulations and class-licence orders were not retrieved. They say which guns, weapons and explosives are "prohibited", which offences are compoundable, and whether everyday items (kitchen axes, diving knives, archery bows) are licensed by class. Without them, finding 1 overstates what an individual must do.
- The commencement dates of ss 11, 22 and 29 are not in the deposit. They are needed to place the Third Schedule grace periods.
- The two readings flagged as inferences need checking against case law or official guidance: "imprisonment ... and a fine" as mandatory, and "whichever is applicable".
- The meaning of "store" (12 or more guns; explosives held over 24 hours) and the trade and manufacture offences are not encoded.
