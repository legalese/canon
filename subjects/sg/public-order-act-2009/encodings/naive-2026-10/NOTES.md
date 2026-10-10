# Public Order Act 2009 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, incorporating amendments
up to 1 December 2021. The latest annotations in the body are 26/2018 and "Act 12 of
2020 wef 01/10/2025", the latter in Part 3, which is not encoded.

**Checks:** one case file, 122 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**9 of the 527 Singapore Acts** deposited here cite it. This row covers what an
organiser, a participant, someone filming the police, or an owner of premises
runs into: when notice and a permit are needed (ss 2, 3, 5, 14, 46), the
foreign-participation ground for refusal (s 7(2)(h), (4)), permit duration and
appeals (ss 9, 11), the offences and defences (ss 15 to 18), immunity (s 19),
special notice of large events (s 6A), move-on directions (ss 34 to 37), film
deletion directions (s 38), owners and occupiers (s 42), and the penalty and
composition figures (s 41).

Not encoded: the contents of the notice (s 6(3)), the Commissioner's general
grounds for refusal (s 7(2)(a) to (g)), conditions (s 8), prohibited-area and
prohibition orders (ss 12, 13) beyond their effect, all of Part 3 (special events
security), arrest, bodies corporate, service and regulations. The prescribed
notice periods and the prescribed crowd size for s 6A sit in regulations, which
were not retrieved.

## What the Act turns out to say

### 1. One person with a placard needs a permit

An "assembly" includes "a demonstration by a person alone" for any of the three
listed purposes (support or opposition, publicising a cause, commemorating an
event), and a "procession" includes a march by one person (s 2(1)). So s 5 applies
to a lone demonstrator in a public place in the same way as to a crowd. The
demonstrator must give the notice in person (s 6(3)(b)(i)). Asserted.

### 2. A lone demonstrator is never an "organiser", so faces the lower fine

s 3(1) excludes "a person carrying on a demonstration by himself or herself or
marching alone" from organising, and s 3(2) counts that person as *taking part*.
Without a permit the maximum is the participant's $3,000 (s 16(2)), not the
organiser's $5,000. A person who only "assists or promotes", or who will receive
ticket revenue, *is* an organiser. Asserted.

### 3. A crowd notice for a big event carries four times the fine for an unpermitted rally

s 6A requires special notice from the organiser of *any* event, "whether or not
comprising or involving an assembly or a procession", if more than a prescribed
number are expected at any one time. Failing to give it carries $20,000 or 12
months (s 6A(5)). Organising a public assembly without a permit carries $5,000
(s 16(1)), or $10,000 or 6 months for a repeat offender (s 16(3)). The prescribed
number is not in the Act. Asserted.

### 4. Move-on powers do not reach a lawful assembly at all

Part 4 "does not apply to any assembly or procession that is not unlawful under
Part 2" (s 34(2)). Where it does apply, a move-on direction must come from a
sergeant or above, be written, last no more than 24 hours, and, if it interferes
with peaceful assembly, be reasonably necessary for public safety, public order or
others' rights (s 36). Contravening one carries $20,000 or 12 months (s 37). The
encoding treats s 34(2) as excluding the power over a person who is part of such an
assembly. That is a reading of "does not apply", not something the text spells out.
Asserted.

### 5. A deviation is excused by a sergeant's agreement, not by a corporal's

s 17(2)(b)(iii) excuses a different date, time or route that was agreed with "a
police officer not below the rank of sergeant" or directed by the senior police
officer at the scene. A corporal's or constable's agreement does not count unless
that officer is the senior officer present and gives a s 8(4) direction. Asserted.

### 6. Filming the police: who may order deletion

s 38 lets a police sergeant or above, or a CPIB, narcotics, intelligence or
immigration officer, order a person to stop and to delete or surrender a film or
picture of law enforcement activities. The officer must reasonably believe that
showing it would prejudice an ongoing operation or investigation, or endanger an
officer. A constable cannot, and nor can an auxiliary police officer (not listed).
Non-compliance carries $20,000 or 12 months (s 38(4)). Asserted.

### 7. Political end plus one non-citizen is a ground for refusal

s 7(2)(h) lets the Commissioner refuse a permit for an assembly "directed towards a
political end" if it is organised by, or involves the participation of, a
non-Singapore entity or "an individual who is not a citizen of Singapore". The
definition of "political end" in s 7(4) is wide: it includes influencing public
opinion on "a matter of public controversy". The encoding does not model that
definition. Asserted for the ground and the corporation test.

### 8. Appeals: 7 days, three decisions only

s 11 allows an appeal to the Minister, "whose decision is final", against a
refusal, a cancellation or a condition, within 7 days of notification or a longer
period the Minister allows. It does not apply to a cancellation caused by a special
authorisation (s 11(4)). A refusal to accept shorter notice (s 6(4), (5)) is not
in the list; treating it as unappealable under s 11 is an inference. Asserted.

### 9. Composition is capped at the lower of half the fine and $5,000

s 41: so $1,500 for taking part without a permit, $2,500 for organising without
one, and $5,000 for anything with a fine of $10,000 or more. Which offences are
prescribed as compoundable is in regulations, which were not retrieved. Asserted.

## What would need doing before this is worth anything

- The regulations: prescribed notice periods (s 6(2)), the s 6A crowd size, and the
  list of compoundable offences.
- The orders in force under ss 12, 13, 14 and 46: which places are prohibited or
  unrestricted (the encoding takes "unrestricted area" as an input), and which
  assemblies are exempt.
- Whether "within the period of 5 years" (s 16(5)) includes exactly 5 years: the
  encoding assumes it does, and no assertion sits on the boundary.
- Whether a march on private land that the public is invited to is a public
  assembly (the procession definition needs a public place, and the assembly
  definition takes invited publics). The encoding says it is not; that is a
  reading.
- No case law was searched.
