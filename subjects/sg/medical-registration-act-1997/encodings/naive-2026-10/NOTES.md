# Medical Registration Act 1997 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation.

**Checks:** two case files, 92 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**48 of the 527 Singapore Acts** deposited here name it, mostly without citing a
section: they rely on it to say who is a registered medical practitioner. s 16
settles that for every written law. This row takes who may practise, what an
unregistered practitioner loses, the offences, and the Disciplinary Tribunal's
powers as they reach a doctor or a patient.

**Not encoded:** the Medical Council, the registers and registration routes, the
accreditation boards, and the complaint, investigation, health and interim-order
machinery of Part 7.

## What the Act turns out to say

### 1. A registered doctor's false specialist title is no offence; an unregistered "doctor" is $100,000

s 17: an unregistered person who practises under the title "physician, surgeon,
**doctor**" or implies a medical degree commits an offence: $100,000 or 12 months.
ss 64 and 65: a **registered** doctor who uses an unapproved title, or falsely
claims to be a specialist or family physician, "may be subject to disciplinary
proceedings". No offence. Asserted.

### 2. A medical certificate from a doctor whose practising certificate has lapsed is not valid

s 15: a certificate required by any written law to be signed by a duly qualified
practitioner "is not valid unless signed by a person who is registered under this
Act **and** has a valid practising certificate". Registration alone is not enough.
A statutory sick-leave certificate signed during a lapse is invalid on the text,
and nothing saves the patient or employee who relied on it. s 14: the doctor cannot
recover fees for that period either. Asserted.

### 3. The traditional-medicine defence names three traditions

s 17(2): it is a defence to prove the person "practised a system of therapeutics
according to **Malay, Chinese or Indian** method" and did not represent themselves
as a qualified practitioner. A Thai, Japanese or Western herbalist, or a homeopath,
is outside the defence on the text, however modest their claims. Asserted.

### 4. A suspended doctor who practises is caught twice

s 63: practising during suspension is $10,000 or **2 years**. And s 59F(3): a
suspended practitioner "is not regarded as being registered", so they are an
unauthorised person under s 13, and s 17 applies: $100,000 or **12 months**. The two
offences have inverted maxima -- the specific one has the lower fine and the higher
term. Asserted.

### 5. Discipline reaches poor quality, not only misconduct

s 59D(1)(d): the Disciplinary Tribunal may act where a doctor "failed to provide
professional services of the quality that is reasonable to expect of him", alongside
professional misconduct and disgraceful conduct. The same orders follow: removal,
suspension up to **3 years**, a penalty up to **$100,000**, censure. Asserted.

### 6. A penalty bites at once; a suspension waits 30 days

s 59F(1): removal and suspension do not take effect for 30 days. s 59F(2): every other
order -- a penalty, censure, conditions -- "takes effect from the date the order is
made". An appeal stops both (s 59G(4)), unless the Tribunal orders immediate effect in
the public interest or the doctor's own interest (s 59E(6), 59G(5)). Asserted.

### 7. Six years, then a public-interest gate

s 41: a complaint made more than six years after the conduct, and more than six years
after the complainant knew or could have discovered it, is not referred. But s 42
sends it to the President of the Disciplinary Commission, who may send it on in the
public interest. A late complaint is diverted, not barred. Asserted.

### 8. Smaller things worth recording

- **s 67:** only the doctor **treating** a colleague must report that colleague's
  unfitness; a co-worker who sees the same thing has no statutory duty. Failure is
  disciplinary only.
- **s 66:** a ship's surgeon treating crew and passengers on board needs neither
  registration nor a practising certificate.
- **s 59G:** both the doctor and the Medical Council may appeal, within 30 days, to
  three Judges, with no further appeal; findings on ethics and standards stand
  unless "unsafe, unreasonable or contrary to the evidence".
- **s 59F(3):** rights revive after suspension only if every term of the order was
  complied with.

## What would need doing before this is worth anything

- **No case law was searched.** The Court of Three Judges' sentencing framework for
  medical discipline is extensive.
- The Medical Registration Regulations and the Council's Ethical Code were not
  retrieved; the approved titles in s 64 live there.
- Whether a practice is "according to Malay, Chinese or Indian method" is a supplied
  fact; the Traditional Chinese Medicine Practitioners Act 2000, which regulates
  TCM separately, is not followed.
