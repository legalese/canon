# Maintenance of Religious Harmony Act 1990 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. Not for public use.

**Edition:** 2020 Revised Edition, informal consolidation (version in force from
15 September 2026), as deposited at `../../registers/source-bundle/MRHA1990.txt`. The
cover says the revised edition incorporates amendments up to 1 December 2021; the
latest amendment annotated in the body is Act 10 of 2025 wef 15/09/2026, which deleted
Part 2 and re-points "Council" to the Presidential Council for Racial and Religious
Harmony established by the Maintenance of Racial Harmony Act 2025.

**Checks:** one case file, 51 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is requirement **REQ-0056** in `subjects/sg/requirements.jsonl`: Tier 2 of the
remaining Singapore Acts, ordered by everyday-life relevance. The requirement asks what
the Act decides for a person or business it applies to; no scenario has asked a sharper
question yet.

The row takes what a religious group, its officers, a donor or a speaker actually meets:
reportable donations and the report deadline (s 2, s 16A), who is a foreign principal
(s 2), the nationality rules for responsible officers and governing bodies (ss 16D,
16E), the life of a restraining order (ss 8(3), 9(3), 11(1B), 12(4)), the s 17F offence
and its defences, maximum penalties (ss 16, 17E, 17F, 17H, 17J) and composition (s 17D).
Not encoded: the grounds and contents of restraining orders, the foreign affiliations and
key management reports, the information powers (ss 16G, 16GA), the s 17E offence beyond
its penalty, officers' liability (ss 17A, 17B), community remedial programmes (s 17GA),
s 17I, and ss 18 to 21.

## What the Act turns out to say

### 1. A religious leader's private remark is an offence where a layperson's is not

s 17F(1) and (2) make inciting hatred against a religious group, or insulting another's
religion, an offence for a **religious leader** with no further condition; (3) and (4)
reach anyone else only where the result "would threaten the public peace or public
order". The defences differ too: for the leader limbs, (7) needs the conduct to be
"domestic in nature"; for the public-order limbs, (8) accepts "private or domestic". So
a religious leader's remark at a private club meeting, heard only by members, has no
defence; the same remark at a family dinner does. Asserted.

### 2. The private defence fails where the target is in the room, or others may overhear

For the insult limbs the accused must also show they "could not reasonably have expected
that the conduct would be perceived by the target person" (s 17F(7)(c), (8)(c)); and
s 17F(9) removes both defences where the parties "ought reasonably to expect that it may
be heard or seen by someone else". Pointing out offensive matters "in good faith ... in
order to bring about a removal of those matters" is a separate defence ((10)). Asserted.

### 3. $10,000 from one foreign donor is reportable; three gifts of $5,000 are not

s 2 "reportable donation" counts a relevant donor's religious donation of $10,000 or more
"on any one occasion, without aggregating any earlier donation". An anonymous donation of
$10,000 or more is reportable even if not shown to be a religious donation, but cash in a
place-of-worship box, an authorised street collection, or cash collected during worship
is not "anonymous" at all. A donation spent on a mission overseas is not a religious
donation (it must serve a purpose "wholly or partly in Singapore"). Zakat and fitrah are
excluded from "gift"; the encoding treats them as not donations, which is an inference.
The report is due by 1 April of the following year (s 16A(3)). Asserted.

### 4. "Relevant donor" and "foreign principal" are different tests

A resident prescribed as a permissible donor is not a relevant donor but is a foreign
principal (not a citizen or PR). A company registered in Singapore but run from abroad
is not a relevant donor (registration suffices) but is a foreign principal ("principal
place of business in a foreign country, even if incorporated or registered in
Singapore"). Asserted.

### 5. With vacant seats a governing body can break s 16E(2) without triggering s 16E(3)

s 16E(2) requires citizens in "more than half of the total number of seats"; the removal
power in (3) arises only where non-citizens hold "half or more". Ten seats, five citizens,
two non-citizens and three vacancies fail (2) and do not trigger (3). Both ss 16D and 16E
apply only from a date the Minister declares by gazetted order; the deposit does not say
whether that has happened. Asserted (the encoding assumes s 16E is in force and takes
s 16D's commencement as an input).

### 6. A restraining order lasts at most 2 years, and lapses without timely confirmation

ss 8(3), 9(3): not exceeding 2 years. Representations to the Council must be written and
within 14 days (s 11(1B)). Where the Cabinet follows the Council, the order lapses unless
the President confirms it within 30 days of the recommendation (s 12(4)(b)); where the
Cabinet's advice is contrary, no such day limit appears in (4)(a). Breach: $10,000 or 2
years, then $20,000 or 3 years (s 16). Asserted.

### 7. No fine ceiling for the serious offences, and composition is capped at $5,000

s 17E carries up to 10 years and s 17F up to 5, each "or to a fine", with no fine maximum
stated. s 17D caps composition at the lower of half the maximum fine and $5,000. A missing
report costs each responsible officer up to $2,000 plus $200 a day after conviction
(s 17H(1)); ignoring a removal direction, $5,000 plus $1,000 a day (s 17J(3A)). Asserted.

## What would need doing before this is worth anything

- The commencement orders under ss 16D(1) and 16E(1), and the regulations (prescribed
  permissible donors, compoundable offences, any longer reporting periods), were not
  retrieved.
- Whether zakat or fitrah can be a donation under paragraphs (b) or (c) of "donation" was
  not settled.
- No decided case or ministerial practice was searched.
