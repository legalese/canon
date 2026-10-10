# Good Samaritan Food Donation Act 2024 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** informal consolidation, version in force from 28/11/2025 (retrieved
1 October 2026). The only amendment annotated is Act 7 of 2025 wef 28/11/2025, which
repointed the definition of "food" to s 4 of the Food Safety and Security Act 2025.
The deposit does not give the date on which the Act, or s 4, came into operation.

**Checks:** one case file, 44 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Chosen for its everyday-life relevance: anyone who gives surplus food to a food bank,
soup kitchen or charity, whether a bakery, a hotel, a caterer or a home cook, is
the person this Act protects or leaves exposed. The Act has five sections, so the
whole operative part (ss 2, 4 and 5) is encoded. The borrowed meanings of "food",
"unsafe" and "unsuitable" (Food Safety and Security Act 2025; Sale of Food Act 1973
ss 2C, 2D) were not read and are a single input flag. s 4(2) is noted, not modelled.

## What the Act turns out to say

### 1. The warnings must go to whoever takes the food from you, not to the person who eats it

s 2 defines "recipient" as "the person directly receiving the food from a food donor",
and s 4(1)(b) and (c) require the donor to have told "the recipient" of any handling
requirements and any time limit. A caterer who labels the food for the end diners
but tells the charity nothing does not meet the condition on a literal reading. That
reading is the naive one; whether a court would take a label that travels with the food
as informing the charity is not answered here. Asserted.

### 2. The protection covers death and personal injury, and nothing else

s 4(1) waives liability "in respect of any death or personal injury that results from
the consumption of the food", in criminal or civil proceedings. A claim for damage to
property or for pure financial loss is not touched by the Act. And a failed s 4 does
not make anyone liable: s 4(2) says the section is "additional to any other defence".
Asserted (the scope of harm; s 4(2) is not modelled).

### 3. Anyone who donates food is a "food donor"; the business limb decides nothing

Limb (a) of "food donor" is an entity donating food "in the course of a business,
regardless if the entity is a charity"; limb (b) is "any other person who donates
food". Limb (b) takes in individuals and non-business entities alike, so the two limbs
together cover every donor. What does decide the matter is "donate": a gift "for a
charitable, benevolent, or philanthropic purpose without receiving any money or
money's worth". A discount sale of near-expiry food, or a corporate gift to a client,
is not a donation. Asserted.

### 4. Food banks passing food on are donors too, with their own duty to warn

Limb (b) of "donate" covers a person giving "any thing donated by another". A food
bank that hands donated food to a family is itself a food donor, and its own
"recipient" is the family, so it must pass on handling and time-limit warnings to
qualify. Asserted (the food bank is a food donor and is protected when it warns).

### 5. The donor answers for the food as it left, not for what happened after

s 4(1)(a) asks whether the food was "not unsafe and not unsuitable at the time it left
the possession or control of the food donor". Cakes that spoil later in the food
bank's fridge do not cost the bakery the waiver, provided the handling warning was
given. The hygiene condition in (d) is "all reasonably practicable measures", not
strict compliance. Asserted.

### 6. Sharing with friends, and live-in workers' meals, are outside the Act

s 5(2) excludes "any exchanging or giving of food between individuals as part of a
personal relationship" and food supplied with accommodation at a private residence "in
exchange for services or labour". It is an inference, not something the text says, that
(b) is aimed at live-in domestic workers. s 5(1) also keeps s 4 away from liability
arising before s 4 commenced. Asserted.

## What would need doing before this is worth anything

- Read the definitions of "unsafe" and "unsuitable" (Sale of Food Act 1973 ss 2C, 2D)
  and "food" (Food Safety and Security Act 2025 s 4) and encode them instead of one flag.
- Find the commencement notification for s 1 and s 5(1).
- Decide whether a label travelling with the food informs "the recipient" (finding 1),
  and what "personal relationship" covers between neighbours or colleagues.
- No case law or parliamentary material was searched.
