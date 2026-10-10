# Poisons Act 1938 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, with amendments to Act 9
of 2026 (in force 1 May 2026) shown, and Schedule amendments to S 770/2025.
The deposit's arrangement of sections is shifted by one against the body (it
lists "19A. Prohibition of sale to persons below 18 years"). This row follows the
body: sale to under-18s is s 19, composition is s 19A.

**Checks:** one case file, 95 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**12 of the 527 Singapore Acts** deposited here cite it. This row takes what a
seller, pharmacist, doctor or holder of poisons meets: the licence requirement
(s 5), the conditions of every sale (s 6) and the exemptions from them (ss 7, 8),
keeping and storing poisons (s 9), doctors' licences (s 10(2)), penalties and
employer liability (s 16), the burden on a person found with poisons (s 18(2)),
sale to under-18s (s 19), composition (s 19A), the ceiling for offences under
rules (s 20(1)(o)), and a sample of the Poisons List. Licensing administration,
search powers, the Minister's exemption orders, forfeiture, fees and all rules
made under the Act are not encoded.

## What the Act turns out to say

### 1. Anyone keeping a poison outside its labelled container commits an offence carrying up to 5 years

s 9(1): "No person whether licensed under this Act or not" may knowingly keep a
poison except in the unbroken manufacturer's package or in a receptacle labelled
with the substance's name **and** a mark showing it is poison. Knowledge is
presumed unless the person proves otherwise (s 9(2)). The text has no household
or personal-use exception, and s 16(1) excepts only acts within ss 7 and 8. Since
Act 9 of 2026 the maximum is $50,000 or 5 years. Ibuprofen is on the List, so on
the text, decanting it into an unmarked pill box is caught. Asserted.

### 2. The export exemption excludes Malaysia

s 8(b) relaxes the pharmacist, labelling and poisons-book rules for sales "to be
exported from Singapore to a place other than Malaysia". A sale for export to
Malaysia gets no relaxation and must meet all of s 6. Asserted.

### 3. Section 8 relaxes only the paperwork, never the licence

s 8 disapplies s 6(1)(a)(v), (2) and (3) only. The licence, licensed premises and
named-person conditions (s 6(1)(a)(i)–(iv)) and the wholesale rule (s 6(1)(b))
still bind a sale to a hospital, a ministry or a research lab. Asserted.

### 4. A retail sale needs a signed poisons-book entry before delivery

s 6(3): the buyer must be known to the seller or introduced, and the seller
"shall not deliver" until the date, names, addresses, quantity and stated purpose
are entered in a book **and** signed by the buyer and any introducer. Rules may
relax this; none were retrieved. Asserted.

### 5. Possession is presumed to be for sale

s 18(2) puts on the accused "the burden of proving that any poison found in the
possession of the accused was not kept for sale". Combined with s 5, an
unlicensed person found with poisons must prove personal use. Asserted.

### 6. The medicines exemption is tight on timing and on who compounds

s 7: doctors, dentists, vets and licensed pharmacists escape s 6 only if the
medicine is labelled with supplier, address and an identification number, and
entered in a book that day, or the next day if same-day entry was "not reasonably
practicable". A licensed pharmacist supplying (not dispensing) a "patent or
proprietary medicine" is outside s 7(1)(e). s 7(5) requires compounding under
the personal supervision of a pharmacist or doctor; nothing similar is written
for dentists or vets. Treating s 7(5) as a condition of the exemption is an
inference: s 7(1) lists only subsections (2), (3) and (4). Asserted.

### 7. Composition is capped at $5,000 for every Act offence

s 19A (Act 9 of 2026): an offence prescribed as compoundable may be compounded for
no more than the lower of half the maximum fine and $5,000. With a $50,000 Act
maximum and a $20,000 rules maximum (s 20(1)(o)), the cap is $5,000 for both;
only an offence with a prescribed maximum under $10,000 would compound for less.
Which offences are compoundable is left to rules. Asserted.

### 8. Under-18 sales: no exemption for practitioners is written into s 19

s 19(1): "No poison shall be sold to any person below 18 years of age", with a
defence of reasonable cause to believe the buyer was above 18. The ss 7 and 8
exemptions are written for s 6 and s 16(1), not s 19. Whether a doctor's or
pharmacist's supply to a minor is a "sale" is not settled by the text (inference
only). The defence speaks of "above the age of 18"; a belief that the buyer was
exactly 18 falls in that gap on a literal reading. Partly asserted (the offence
and the defence, not the practitioner question).

### 9. Paracetamol and aspirin are not on the List

A search of the deposited Schedule finds neither paracetamol nor aspirin.
Ibuprofen, codeine, nicotine, warfarin and sildenafil are listed. Some entries are
conditional: xylometazoline only "when contained in eye preparations"; urea only
in preparations for human consumption, except external preparations of not more
than 10%. Asserted for this sample only.

### 10. A doctor may hold only a retail licence for an all-doctor practice

s 10(2): no licence to a medical practitioner except to import, possess and sell
by retail for his own practice or a practice or partnership "in which every
member is a medical practitioner". Asserted.

## What would need doing before this is worth anything

- The Poisons Rules were not retrieved. s 6(3) and s 7 are both "subject to" or
  "except as provided in" rules, so the encoded duties may be relaxed in practice.
- Only nine substances from the Poisons List are encoded; the List runs to nearly
  2,000 lines of the deposit and is amended frequently by subsidiary legislation.
- The interaction of s 19 with ss 7 and 8 (practitioner supply to minors) needs
  case law or the rules.
- The s 7(4) repeat-prescription entry rule and the s 8(g)(ii) employee-treatment
  limb are not separately modelled.
- No case law was searched.
