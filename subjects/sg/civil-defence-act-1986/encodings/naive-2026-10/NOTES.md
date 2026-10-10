# Civil Defence Act 1986 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, with amendments to Act 16
of 2026 (in force 30 September 2026) shown.

**Checks:** one case file, 100 assertions satisfied, 0 errors.

## Why this Act, and why scoped

**11 of the 527 Singapore Acts** deposited here cite it. Most of the Act governs the
Force itself: enlistment, service offences, arrest, trial and punishment of members.
This row takes only what a member of the public, a building owner, a business or an
employer meets: day-to-day operational powers and who may use them (ss 101A, 101B),
protection from liability (ss 101C, 105, 112), the state of civil defence emergency
and its powers (ss 102, 103), the public warning system on private premises
(ss 103A to 103D), obstruction (s 106), SCDF uniforms and insignia (s 106A), company
officers (s 107), employment protection (s 108) and compensation for injury (s 111).

## What the Act turns out to say

### 1. Tampering with a public warning siren carries ten times the fine for assaulting an officer

s 103D: anyone who "wilfully removes, relocates, destroys, damages or tampers with" a
prescribed civil defence emergency device faces up to $50,000 or 3 years. Assaulting,
obstructing or insulting a person performing duties under the Act (s 106) is up to
$5,000 or 6 months. Asserted.

### 2. A building owner must host the device at their own expense, contracts notwithstanding

s 103B: the Commissioner may direct the owner of "relevant premises" to provide space,
facilities and access "at the owner's expense", even where this prejudices the owner's
or occupier's contracts. A party who breaches a contract is not liable where the
breach is "solely attributable" to compliance. Defying the direction: $10,000 or 3
years, plus up to $1,000 a day after conviction. Residential buildings up to a
prescribed height are excluded; the height is in regulations not retrieved, and is a
parameter. Asserted.

### 3. Entry for assessment always needs 5 working days' notice; only urgent repairs may skip it

s 103C(2) requires notice to the owner "not less than 5 working days" before entry. The
s 103C(3) exception, which also permits breaking doors and demolishing fixtures,
applies only to urgent repairs, when an emergency is likely and entry has been refused
or consent cannot be obtained. An assessment visit has no urgent route. Asserted.

### 4. Ambulance contractors share most, but not all, of the Force's day-to-day powers

s 101B lets employees of a contracted emergency ambulance provider, and SAF servicemen
attached to the Force, exercise s 101A(1)(a) to (e) and (2): entering premises,
removing obstructions, closing roads, cutting off utilities, and taking an
unidentified unconscious person's fingerprints. They cannot require a medical
examination after hazardous exposure or seize contaminated things ((f), (g)). A
member needs the Commissioner's authorisation for s 101A; under s 103 in an emergency
any member, and any police officer, may act. Reading the necessity condition as
carried to s 101B persons is an inference. Asserted.

### 5. Three different liability shields, with three different tests

s 101C protects the Commissioner, members and s 101B persons personally only if they
acted "in good faith and with reasonable care". s 105(2) protects a civil defence
volunteer on good faith alone. s 112 bars any action, even against the Government
itself, for things done in good faith during a state of emergency or civil defence
emergency. Asserted.

### 6. Property loss is compensated only for two of the five emergency powers

s 103(3) compensates loss or damage caused by removing impeding things (s 103(1)(c))
and entering or breaking into premises (s 103(1)(d)). Loss from an evacuation or
exclusion order, or from a road or public-place closure, is not mentioned. A person
directed to help save life is entitled to "fair and reasonable remuneration"
(s 103(2)). Defying a direction: $2,000 or 3 months. Asserted.

### 7. Employment protection applies only during a declared emergency

s 108 protects a person absent from work on civil defence duties from dismissal or
loss of leave and benefits "whether or not his or her usual employer has consented",
but only during a state of emergency or state of civil defence emergency. By contrast,
s 111 compensation for death or injury covers civil defence measures and training
under the Commissioner's authority at any time. Asserted.

### 8. A state of civil defence emergency lapses after seven days

s 102(3): it terminates on the expiry of the seventh day; extension requires the
President's approval (s 102(4)). Counting elapsed days from the declaration is an
inference. Asserted.

### 9. The uniform offences have defences that do not all reach each other

The s 106A(3) defences (Commissioner's express permission; a public entertainment
licensed under the Public Entertainments Act 1958) cover only impersonation under
(1)(a) and a member's off-duty wear under (2). They do not cover the commercial
false-endorsement offence in (1)(d). A member wearing uniform outside duty without
written authorisation commits an offence. Supplying uniform or insignia to an
unauthorised person (s 106A(4)) has a reasonable-inquiry defence; manufacturing
without a Government agreement has none. Company officers are deemed to commit the
company's offences unless they prove both no consent or connivance and due diligence
(s 107). Asserted.

## What would need doing before this is worth anything

- The regulations (prescribed height and excluded building types for s 103A, the
  prescribed devices, claims procedure under s 103(2), (3), compensation rates under
  s 111) were not retrieved.
- s 106A(1)(b) and (c) (using a rank designation in business; representing oneself as
  a member) are not separately encoded.
- No case law was searched.
