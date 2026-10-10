# Veterinary Practice Act 2026 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** the Act as enacted (No. 11 of 2026), informal consolidation, "version
in force from 1/8/2026", retrieved 1 October 2026, deposited at
`../../registers/source-bundle/VPA2026.txt`. The deposit annotates no amending Act.
s 1 leaves commencement to a Gazette notification, and the deposit does not say
which sections are in force. s 89 amends the Act itself (deleting s 4(5) and
s 7(1)(k)), but the consolidation still prints s 4(5). That suggests s 89 had not
commenced by 1 August 2026, but this is an inference.

**Checks:** one case file, 56 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is requirement **REQ-0023**: Tier 2 of the remaining Singapore Acts, ordered by
everyday-life relevance. The requirement asks what the Act decides for a person or
business it applies to. No scenario has asked a sharper question yet. The people
it applies to are pet owners, animal-care businesses, vets and vet students. This
row covers the provisions they meet:

- what counts as an animal and as veterinary practice (s 2)
- who is a duly qualified veterinarian, including existing licensees deemed qualified (ss 3, 90)
- renewing a practising certificate (s 23)
- the offences of unqualified practice and false titles (ss 29 to 36)
- bringing a disciplinary case and its limitation period (ss 40, 42, 43)
- what a Disciplinary Committee can order, and the appeal (ss 56, 62)

Not encoded: the Council (Part 2); the registers and the tests for full, restricted
and specialist registration (ss 15 to 22); cancellation and restoration (ss 26, 27);
voluntary cancellation (ss 37, 38); the Registrar's review, Complaints Assessment
Committees, mediation, Interim Orders Committees and investigations; composition
and exemption (ss 83, 86); and anything left to regulations ("prescribed"), because
no regulations were read.

## What the Act turns out to say

### 1. A supervised layperson may anaesthetise an animal, but may not diagnose or operate

s 29(1) bars anyone but a duly qualified veterinarian from practising veterinary
medicine. s 29(5) then lets anyone who is not suspended do any act "not being an
excluded act" if they work under a duly qualified vet's supervision. The excluded
acts (s 29(7)) are diagnosis, "treatment (of a surgical nature)", prescribing,
certificates that need professional judgment, and anything prescribed. That
leaves administering anaesthetics, non-surgical treatment and advice on a diagnosis
open to a supervised vet nurse, even though s 2 lists them as veterinary practice.
A suspended vet working under supervision gets no benefit from s 29(5). Asserted.

### 2. Calling yourself a vet need not be an offence; pretending to be one always is

s 30(1) makes five kinds of holding out an offence for anyone who is not duly
qualified. For three of them, taking the title (c), implying qualification (d) and
advertising (e), s 30(4) gives a defence if the person proves they acted "without the
intention to deceive or to gain any advantage". That defence is not open for
wilful pretence (a) or practising under the title (b). For advertising it is also
lost "in the prescribed circumstances" (s 30(5)). A vet student in supervised
training is outside limb (d) altogether (s 30(2)). Asserted.

### 3. A false specialist title is a disciplinary matter, not a crime

ss 29 to 33 and 36 are offences carrying up to $50,000 or 12 months or both. A
registered vet who falsely claims to be a specialist (s 34), represents another
vet as one (s 35), or uses unregistered qualifications or unapproved titles (s 25)
commits no offence. The text says only that a disciplinary case "may be brought".
Asserted.

### 4. "Animal" includes a prawn, a snail and an egg, but not an insect

s 2 covers mammals other than humans, birds, reptiles, amphibians, and "a fish
(including a crustacean, mollusc or other aquatic invertebrate)", together with the
young or egg of any animal. Insects and spiders are not on the list. This row reads
"mollusc" literally, so a land snail counts. That is an inference: the parenthesis
may be meant only for aquatic species. Asserted for a prawn, a land snail, a
butterfly and a human being; the egg is encoded but not asserted.

### 5. Existing licensees are vets for twelve months, unless refused sooner

s 90 deems the holder of an unsuspended licence under s 53(1) of the Animals and
Birds Act 1965 to be duly qualified from the day s 29 commences. This lasts until
the earliest of: 12 months (or a longer prescribed period), the grant of a practising
certificate, or the final refusal or withdrawal of their application. Asserted
(12 months taken, since no longer period was found prescribed).

### 6. A complaint has a 3-year window, measured from the later of two dates

s 42(1): the Council must not refer a case brought after "the later of" 3 years from
the conduct and 3 years from when the complainant knew of it or could with
reasonable diligence have discovered it. s 43 lets a late case go forward anyway if
an appointed Council member assesses it to be in the public interest. A complaint
must be in writing and supported by a statutory declaration, unless a public
officer, public authority or the Council brings it (s 40(2)). Asserted.

### 7. Discipline: up to $50,000 and 3 years' suspension; one appeal only

s 56(2) allows cancellation, suspension "not exceeding 3 years", and "a penalty not
exceeding $50,000", among other orders. s 62 allows an appeal to the General Division
of the High Court within 30 days. "there is no appeal" beyond it. Practising-
certificate refusals go to the Minister within 30 days, "whose decision is final"
(s 23(11)). A renewal must be filed at least 30 days before expiry, or the prescribed late
application fee, "if any", is payable (s 23(3), (4)). Asserted.

## What would need doing before this is worth anything

- The Veterinary Practice regulations (prescribed acts, conditions, fees, the s 30(5)
  "prescribed circumstances" and any longer s 90 period) were not retrieved.
- Which sections have commenced was not established. s 89 appears not to have
  commenced (an inference, from s 4(5) still being printed).
- Whether dental treatment that is not surgical is an excluded act is left open by
  the text. This row treats it as not excluded, and does not test it.
- No cases, Council guidance or Animals and Birds Act provisions were read.
