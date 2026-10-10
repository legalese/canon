# Dental Registration Act 1999 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2022 Revised Edition, informal consolidation, with amendments to
S 583/2026 (in force 3 September 2026, the Schedule) and Act 19 of 2025 (in force
5 December 2025, service of documents) shown.

**Checks:** one case file, 117 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**13 of the 527 Singapore Acts** deposited here cite it. This row takes what a
dentist, an oral health therapist, an employer or a patient meets: who may practise
and charge for dentistry, the titles, the offences and their penalty, the
practising certificate, the Disciplinary Committee's sanctions and when they take
effect, and composition: ss 14B(2), 17, 29-36, 38, 39, 50(2), 51, 73, 74 and 76. The
Council, the registers and registration entitlements, the Accreditation Board,
complaints, the Health Committee, interim orders, funds, inspectors, regulations,
savings and the Schedule of qualifications are not encoded.

## What the Act turns out to say

### 1. An appeal holds back even an "immediate" removal

s 51(9): a removal or suspension order takes effect only after 30 days. s 51(10)
lets the Committee order immediate effect "for the protection of members of the
public". But s 51(14) begins "Despite anything in this section": once the
practitioner appeals, the order "does not take effect unless" confirmed, or the
appeal is dismissed or withdrawn. Read literally, an appeal suspends even the order
made immediate for public protection. Asserted.

### 2. Read literally, a therapist may not describe herself as able to treat teeth

s 33(1)(c) bars anyone "other than a registered dentist who has in force a
practising certificate" from a description implying the person "is qualified to
heal or treat dental disorders". s 33(2)(b) bars the same description to anyone but
an oral health therapist with a certificate. Taken literally, each bars the other
profession, and only someone registered as both may use such a description. The
encoding follows the words; whether the title "oral health therapist" is itself
such a description is not decided. Asserted.

### 3. A first-division dentist needs approval to call himself "dentist"; a second-division one does not

s 38(2): a dentist in the first division may use only the designation "approved by
the Council for his or her use" or a listed prescribed title. s 38(3): a
second-division dentist may use "registered dentist" or "dentist" without approval,
but nothing else — Council approval does not widen (3). Breach is a disciplinary
matter, "deemed" to bring disrepute (s 38(4)), not an offence. Asserted.

### 4. Claiming to be a specialist is discipline only; misusing "dentist" is a crime

s 39 (holding out as a specialist without s 14C registration) and s 38 lead only to
disciplinary proceedings. s 35's penalty — $25,000, or $50,000 and/or 6 months on a
second conviction — covers ss 29 to 34 only. Asserted.

### 5. Fees follow registration and a certificate, not the therapist's scope

s 36(1) lets a registered dentist or oral health therapist "with a practising
certificate" recover fees. The scope of practice that limits a therapist's lawful
practice under s 29(2) is not a condition of s 36, so a therapist who practises
outside scope (an offence) is not on the face of s 36 barred from the fee. Medical
practitioners are carved out (s 36(2)); a supervised student under s 74 is not.
Asserted.

### 6. Defences differ by offence, and one offence has none

s 30(2) (employer) requires proof of both lack of knowledge and due diligence.
s 31(3) gives a mistake-plus-due-diligence defence only to s 31(1) and (2); s 31(4)
(practising on premises alongside an unlawful practitioner, knowing it) has none.
Asserted.

### 7. Smaller points

- The Disciplinary Committee may suspend for 3 months to 3 years (s 50(2)(b)), but
  for breach of conditions for "any period not exceeding 12 months" with no minimum
  (s 51(1)(b)). Asserted.
- Composition is capped at the lower of half the maximum fine and $500 (s 76(1)), so
  even a $25,000 offence compounds for at most $500. Asserted.
- A practising certificate lasts at most 2 years; renewing later than one month
  before expiry attracts a late fee (s 17(3)-(5)). Temporary registration is for at
  most 3 years, renewable (s 14B(2)). Asserted.

## What would need doing before this is worth anything

- s 73 (medical practitioners) is encoded as a flag "practising medicine or surgery";
  whether a doctor doing dental work is always within it is an inference the text
  does not settle.
- "The expiry of 30 days after the order is made" (s 51(9)) is read as 30 whole days
  elapsed; the boundary is an inference.
- The oral health therapists' scope of practice, the prescribed titles, the
  compoundable offences and the fees are left to regulations, none of which was read.
- No case law or Council guidance was searched.
