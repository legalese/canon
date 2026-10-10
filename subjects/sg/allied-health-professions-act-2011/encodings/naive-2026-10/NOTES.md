# Allied Health Professions Act 2011 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition (incorporating amendments up to 1 December 2021,
in operation 31 December 2021), informal consolidation, version in force from
5 December 2025. The latest amendment annotated is Act 19 of 2025 (Statutes
(Miscellaneous Amendments) Act 2025), wef 5 December 2025. Deposited at
`../../registers/source-bundle/AHPA2011.txt`.

**Checks:** one case file, 54 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This row answers **REQ-0020** in `subjects/sg/requirements.jsonl`: Tier 2 of the
remaining Singapore Acts, ordered by everyday-life relevance. The requirement asks
what the Act decides for a person or business it applies to; no scenario has asked a
sharper question yet. So the row takes what a patient, a practitioner, a student or an
employing clinic meets: which professions are regulated and which titles reserved
(s 4 and the Schedules), who is "duly qualified" (s 3), temporary registration
periods (s 19(3)), appeals (ss 21(7), 26(3), 55(1)), practising certificates
(s 23), the title offences and who else they catch (ss 29 to 34), the Part 4
penalty (s 36), Tribunal and voluntary suspension (ss 37(1)(d), 53(2)) and
composition (s 73). The Council and its committees, the eligibility tests for full,
restricted and conditional registration, the complaints and inquiry procedure, the
Third Column descriptions of each profession's acts, regulations and the s 76
transitional deeming are not encoded.

## What the Act turns out to say

### 1. Half the listed professions are not regulated by it at all

The First Schedule lists ten allied health professions, but s 4 says the Act
"applies only in relation to allied health professions set out in the Second
Schedule", and the Second Schedule has five: occupational therapy, physiotherapy,
speech-language pathology, radiation therapy and radiography. Audiologists, clinical
psychologists, dietitians, podiatrists and prosthetists/orthotists are named in the
Act but not registered under it, so calling oneself "Dietitian" or "Clinical
Psychologist" is not an offence under s 29. Asserted.

### 2. Registration is not enough: without a practising certificate you may not use your own title

s 3 defines a "duly qualified allied health professional" as one who is registered
**and** has a valid practising certificate, and s 29 makes title offences turn on not
being duly qualified. On the encoding, a registered physiotherapist whose certificate
has lapsed commits an offence by calling herself "Physiotherapist" (unless she proves
no intent to deceive or gain). Asserted. Whether prosecutions are brought on that
basis was not checked.

### 3. A duly qualified professional may use only the titles of the authorised profession

s 30 mirrors s 29 for duly qualified professionals using another profession's titles.
A registered radiation therapist may call herself "Therapeutic Radiographer" (a
second-column title of radiation therapy) but not "Radiographer", which belongs to
radiography. Asserted.

### 4. The training exemption covers uniforms, not titles

s 29(2) exempts supervised training at an approved establishment from s 29(1)(d)
(name, title, sign, uniform or badge implying qualification) only. A student who uses
a Second Schedule title is caught by (c) unless the (3) defence of no intent to
deceive or gain is proved; and the (3) defence is lost for advertising "in the
prescribed circumstances" (s 29(4)). Asserted.

### 5. Employers are guilty with their staff, and must prove a double defence

s 31(3): where an employee, agent or partner commits a s 29 or 30 offence, the
employer "shall also be guilty". The s 31(4) defence needs both lack of knowledge
**and** all reasonable precautions and due diligence. A registered professional who
knowingly enables an assistant to assume a title is guilty too (s 33). Asserted.

### 6. Penalties, suspension and the composition cap

Part 4 offences: up to $25,000 or 6 months, $50,000 or 12 months on a repeat
conviction (s 36). Failing to surrender a practising certificate within 14 days: up
to $5,000 (s 23(10)). A Disciplinary Tribunal suspension must be at least 3 months
and at most 3 years, and its penalty at most $50,000 (s 53(2)); a voluntary
suspension (s 37(1)(d)) has the 3-year cap but no minimum. Composition is capped at
the lower of half the maximum fine and $2,000 (s 73), so for any Part 4 offence the
cap is $2,000; which offences are compoundable is left to regulations not read.
Appeals against refusal or removal go to the Minister, whose decision is final;
against a Tribunal order, to the General Division of the High Court; all within
30 days. Asserted.

## What would need doing before this is worth anything

- The regulations (fees, late fee, prescribed circumstances under s 29(4),
  compoundable offences, practising certificate conditions) were not retrieved.
- Foreign-language equivalents of the titles (s 29(1)(c)) and the Third Column
  descriptions of each profession's acts are not modelled.
- The mapping of the First Schedule's "Speech Therapist" to the Second Schedule's
  Speech-Language Pathology is by name (an inference).
- No decided case was searched.
