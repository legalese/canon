# Food Safety and Security Act 2025 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. Not for public use.

**Edition:** "Informal Consolidation – version in force from 1/7/2026", deposited at
`../../registers/source-bundle/FSSA2025.txt`. The latest amendment annotated is Act 15
of 2026 wef 01/07/2026 (Act 9 of 2026 and Act 5 of 2026 are also annotated). Section 1
says the Act comes into operation on a date the Minister appoints by Gazette
notification. The deposit does not say which Parts are in force. Section numbers
follow the body of the deposit. The arrangement at its head is shifted by one line in
places: it lists "Meaning of 'food business'" against 4, but the body numbers it 5.

**Checks:** one case file, 53 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

It was chosen because ordinary people in Singapore meet it in everyday life: anyone
who sells food, cooks or bakes at home for money, grows vegetables for sale or brings
food back from a trip. The Act runs to more than 400 pages, so this row covers only
those situations: what a food business is and which ones need a licence (ss 5, 6, and
First Schedule Part 1 items 1, 4, 8 and 11, and Part 2 items 1 and 4), the
private-consumption allowance and reselling food brought in under it (ss 44, 160,
161), what "unsafe" means (s 11), the maximum fines for supplying unsafe or unsuitable
food, running unlicensed premises and disallowed conduct (ss 102, 104, 146, 147, 150,
151, 161), the repeat-offender rule, and two defences (ss 164, 166(2)).

Not encoded: food security and minimum stockholding (Part 2); import, export and
transhipment licensing and the offences other than s 44 (Part 3); licence grant,
conditions and regulatory action; traceability; food workers (s 103); defined food
and pre-market approval (Part 5); drinking water (Part 6); directions and recalls
(Part 7); the handling offences (ss 144, 145, 148, 149); food contact articles; food
and health promotion (Part 9); misleading conduct and labelling (Part 10); animal feed
and pesticides (Part 11); enforcement, appeals and the transitional Second Schedule.
The regulations that s 104 depends on were not retrieved.

## What the Act turns out to say

### 1. A home kitchen is excluded from some licensable classes but not others

First Schedule Part 1 items 1 (eating places), 4 (takeaway and ready-to-eat food) and
6 (meat, fish and perishables) each apply to "premises (but not a home)". Item 8
(catering, where food is "prepared and served to consumers of the food away from the
food premises" to a predetermined type, number, time and cost) has no such exclusion.
Neither has Part 2 item 4 (manufacturing, kneading, mixing, forming and so on "for the
purpose of sale to any other food business"). On the words alone, then, a home baker
selling cakes to the public falls outside the classes read here. A home cook catering
a party at the client's venue, or a home baker supplying a café for resale, falls
inside them. This is a reading of the Schedule's text only. It does not account for
exemptions under ss 320 and 321 or for any regulations. Asserted.

### 2. Bring it back for yourself, and you may not sell it

s 44 treats food as imported "for private consumption" only if one individual brings
it in, not for a food business, as a trade sample or to donate, and the total is "not
more than 15 kilograms (inclusive of any eggs)" with no more than 30 eggs. s 161 makes
it a strict liability offence to supply food imported on that basis: up to $5,000 or 3
months for an individual. s 160 is the knowing version: $15,000 or 6 months, rising
to $30,000 or 12 months for a repeat offender. Asserted (boundaries at 15 kg and 30
eggs).

### 3. Chewing gum and crocodile meat never count as private consumption

s 44(3) says the allowance "does not extend to any food of higher regulatory concern".
s 44(4) lists ANY chewing gum, raw or unpasteurised milk, blood products "such as
blood curd", puffer fish, fertilised eggs, defined food, and every meat other than
pork, beef, lamb, mutton, venison, chicken, duck, turkey, goose, quail or domesticated
pigeon. Those foods are also carved out of the ss 160 and 161 reselling offences. The
reason is presumably that they cannot come in as private consumption at all, but that
is an inference: the Act does not say so. Asserted.

### 4. A food business can be charitable, a one-off, or run from home, but a platform is not one

s 5(1) applies "regardless of whether ... of a commercial, charitable or community
nature or whether it involves the handling or the supply of food on one occasion only".
s 5(2) includes home businesses. s 5(3) excludes intermediaries "(such as an internet
service provider or an online auction location)" and event or market organisers.
Asserted.

### 5. Allergies and religion do not make food "unsafe"

s 11(2): food is not unsafe merely because of personal preference, a moral or
religious objection, harm only "in inappropriate quantities", or because it is
unhealthy for "any individual who has an allergy or other personal health condition".
Asserted.

### 6. Due diligence fails if the food was your own import or the fault was your staff's

s 164 gives a defence where the offence was due to another person or an outside cause
and all reasonable precautions were taken. "Another person" excludes the accused's
employee or agent (s 164(2)), and the defence "does not apply if the person charged
imported the food" (s 164(3)). A retailer who resold a sealed package in the condition
in which it was bought has a separate defence under s 166(2). Asserted.

### 7. Fines double for a repeat within five years; the strict liability versions have no repeat tier

Supplying unsafe food knowingly (s 146) carries up to $25,000 or 12 months for an
individual, and $50,000 or 24 months for a repeat offender, meaning one convicted
before "within the period of 5 years immediately before". For a non-individual it is
$50,000, or $100,000 on a repeat. The strict liability version (s 147) is $10,000 or 6
months, or $20,000, with no repeat tier. An owner or occupier who lets premises be
used for an unlicensed licensable food business (s 102) has a defence only if they
could not have known AND took all reasonable steps to stop the use once aware.
Asserted.

### 8. Growing more than 200 kg a month for sale needs a licence

First Schedule Part 2 item 1 excludes cultivating "not more than 200 kilograms in a
single month of fruits or vegetables" grown without excreta or a regulated plant
pesticide, and anything not for sale. Above 200 kg, or using either input, growing for
sale is licensable. Asserted.

## What would need doing before this is worth anything

- Find out which Parts are in force. The deposit does not say, and some provisions
  replace the Sale of Food Act 1973 and other Acts only on commencement.
- Retrieve the regulations (s 104's prohibited conduct, prescribed weights under
  s 44(5)) and any exemption orders under ss 320 and 321. Without them the
  home-business reading in finding 1 is incomplete.
- Read the rest of the First Schedule properly. Only the items named were encoded.
- The repeat-offender rule also counts convictions under the repealed Acts; that is
  not modelled.
