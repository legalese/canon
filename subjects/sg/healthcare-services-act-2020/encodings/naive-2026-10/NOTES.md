# Healthcare Services Act 2020 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** Act 3 of 2020 (the deposit's page headers read "NO. 3 OF 2020"),
informal consolidation, with amendments by Act 11 of 2023 (in force 1 May and
26 June 2023), Act 31 of 2022, S 1/2022, S 387/2023 and S 800/2023 (in force
18 December 2023) shown. The deposit does not say it is a Revised Edition text.

**Checks:** one case file, 93 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**10 of the 527 Singapore Acts** deposited here cite it. This row takes what a
clinic, a practitioner or an advertiser meets: what a healthcare service and a
clinical procedure are (s 3), which services need a licence (First Schedule
para 1), the ambulatory surgical centre service, unlicensed provision and its
penalties (ss 5, 8, 9, 9A), transfer and lapse of a licence (ss 16, 18),
employee-record retention (s 28(4)), names and titles (s 29), advertising
(ss 31, 31A, 31B), and obstruction and false statements (ss 42, 43). The
application procedure, licence conditions, regulatory action, key appointment
holders, step-in orders, most enforcement powers, appeals, and the Second
Schedule are not encoded.

## What the Act turns out to say

### 1. On its face, s 31A forbids almost anyone without a licence from advertising treatment

s 31A(1): a person "must not advertise, or cause to be advertised, any skill or
service relating to the treatment of any ailment, disease, injury, infirmity or
condition affecting the human body so as to induce any person to seek the
advice of or treatment from the advertiser". The only carve-out in s 31A(2) is
a licensable service advertised by or for its licensee. So a provider of a
service NOT in the First Schedule (the row's examples are traditional Chinese
medicine and psychological counselling, which the Schedule does not name) has
no carve-out in s 31A, whatever the practitioner's own registration. The
defence in s 31A(4) is for a technical publication circulating mainly among
doctors, dentists, nurses and midwives, pharmacists, poisons licence holders
and their trainees. Allied health professionals, optometrists and TCM
practitioners are not on that list, so a technical journal for physiotherapists
does not qualify. Exemption orders under s 53 or regulations may change this
and were not retrieved. Asserted.

### 2. "Doctor" in an advertisement: anyone without a practising certificate must say so

s 31B applies to anyone called "Doctor" (or any abbreviation or derivative, in
any language) in an advertisement of a healthcare service unless they are a
"specified person": a registered allied health professional, dentist or oral
health therapist, doctor, nurse or midwife, optometrist or optician,
pharmacist or TCM practitioner who holds a valid practising certificate. Anyone
else must have their qualification stated "whenever the protected title is
used"; a disclaimer if it is not medical or dental; and, if they hold ANY
medical or dental qualification, a disclaimer that they have no practising
certificate. So a PhD who also holds an unused medical degree needs both
disclaimers, and a registered TCM practitioner or pharmacist with a
certificate needs neither. Asserted.

### 3. A licensee's misleading name is not an offence; a non-licensee's is

s 29 bars a licensee from using "Singapore" or "National" in its name or logo
without approval (s 29(1)(b)), or a speciality term without engaging a
relevant specialist (s 29(2A)), but creates an offence only for a person "that
is not a licensee" using a prescribed term (s 29(3), (4): $10,000 or 12 months,
plus $1,000 a day continuing). A licensee's breach is instead a ground for
regulatory action under s 20(1)(b)(iii), which covers "any other provision of
this Act, the contravention of which is not an offence". Asserted (the
breach and the offence; the s 20 route is in a comment only).

### 4. Penalties escalate on different triggers

s 8 (unlicensed provision) and s 9 (unapproved premises, conveyance or mode)
double the maximum fine for a person with a "previous qualifying conviction",
which reaches back to convictions under the repealed Private Hospitals and
Medical Clinics Act. s 9A (a specified service without s 11D approval) doubles
it "in the case of a second or subsequent offence", with no reference to the
repealed Act. Maximums: s 8 $100,000 / $200,000 and 2 years; s 9 $50,000 /
$100,000 and 12 months; s 9A $100,000 / $200,000 and 2 years. The Government is
outside the Act altogether (s 5). Asserted.

### 5. The 12-hour line for an ambulatory surgical centre

A surgical procedure, or one performed with anaesthetics, is a "relevant
procedure" unless the patient is assessed at the start to need accommodation
for more than 12 hours; exactly 12 is still within it. An outpatient medical
or dental clinic, community hospital, contingency care or renal dialysis
licensee needs no ambulatory surgical centre licence for it unless it
"require[s] general anaesthesia". An acute hospital is excluded only for
inpatients. Asserted.

### 6. Smaller rules

A healthcare service is one "whether or not provided for reward" (s 3(1)).
Body piercing, tattooing and intense pulsed light are never clinical
procedures (s 3(2)(b)). A licence transfer needs both a licence condition
allowing it and the Director-General's written consent, and is otherwise void
(s 16). A licence lapses on the licensee's death or dissolution or when the
last approval is cancelled, with no refund (s 18). Employee records must be
kept for 2 years after employment ends (s 28(4)). Self-incrimination is a
reasonable excuse for refusing information (s 42(2)). Asserted.

## What would need doing before this is worth anything

- The Second Schedule (appointed days) is column-shifted in the .txt deposit:
  the dates 3 January 2022, 26 June 2023 and 18 December 2023 and the two
  lettered lists of services cannot be matched to each other reliably from
  the text, so it was not encoded. As deposited, the emergency ambulance and
  medical transport services do not appear by name in it (an observation of
  the deposit, not checked against the PDF).
- s 18's "last valid approval" is modelled as a count of approvals cancelled
  against approvals held, an inference about how the condition is met.
- The prescribed terms (s 29(3)), specified services (s 9A), section 28
  licensees and prescribed advertising requirements (s 31(2)) all live in
  regulations, none retrieved. Nor were any s 53 exemption orders.
- No case law or MOH guidance was searched.
