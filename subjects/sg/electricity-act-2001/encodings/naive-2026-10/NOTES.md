# Electricity Act 2001 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, with amendments to Act 27
of 2024 (in force 1 July 2025 and 1 September 2025) shown.

**Checks:** one case file, 155 assertions satisfied, 0 errors, 0 warnings. Most of
the count is three per-offence tables (maximum fine, maximum imprisonment, daily
fine) across 17 offences.

## Why this Act, and why scoped

**9 of the 527 Singapore Acts** deposited here cite it. This row takes what an
electrician, a contractor digging near cables, a building owner or a householder
meets: the s 2 voltage definitions, who needs an electricity licence (s 6), earthworks
near cables (ss 79, 80), who may do electrical work (s 82), the offences of Part 10
with s 92's default penalty, the s 87 fine formula and meter-tampering presumption,
officers' liability (s 91), composition (s 93) and serious accidents (s 94). Licensing
procedure, tariffs, special administration, Part 4A control, rationing, gas, the
wholesale market, competition and the Appeal Panel are not encoded.

## What the Act turns out to say

### 1. Stealing electricity has no ceiling on the fine

s 87(2): the fine is "the total of" up to $50,000 **and** "an amount equal to 3 times
the value of electricity" abstracted, plus $250 a day for a continuing offence. The
second limb is a fixed multiple, not a cap, so the maximum grows with the theft: on
$20,000 of electricity it is $110,000. Asserted.

### 2. Tampering is presumed from five physical signs plus custody

s 87(4): if a device or wire was attached, the cover had a hole "not a result of
ordinary wear and tear", a licensee's seal or paint was disturbed, or a test link was
moved, **and** the accused had custody or control of the meter, tampering is
"presumed, until the contrary is proved". A worn hole or a low bill alone does not
trigger it; nor does a sign without custody. Asserted.

### 3. Digging near a high-voltage cable carries 5 years; near a low-voltage one, 12 months

s 80(1) requires 7 days' written notice to the licensee, location information and
consultation, and licensed cable detection; breach carries $100,000 or 5 years
(s 80(7)). Near a low-voltage cable, s 79 requires only licensed cable detection,
at $10,000 or 12 months. Both yield to genuine safety emergencies (with notice to the
licensee not more than 7 days afterwards) and do not bind the licensee that owns the
cable. Asserted. Whether a late emergency notice is itself an offence is not said:
the penalty provisions name s 79(1) and s 80(1), and the notice duty sits in the
exceptions. Not asserted beyond whether the notice was in time.

### 4. The s 80(9) defence can be lost on paper

A person charged under s 80(7) who relies on information from the licensee or a
cable detection worker cannot, without the court's permission, use the due-diligence
defence unless written notice identifying the source was served on the prosecutor
"within 14 clear days before the hearing" (s 80(10), added by Act 27 of 2024). This
encoding reads "within 14 clear days before" as at least 14 clear days before; that
is an inference, and the words could be read the other way. Asserted on that reading.

### 5. A householder may change a lamp or a household fuse, and nothing else

s 82(1) bars any individual from electrical work unless licensed or supervised by a
licensed electrical worker. s 82(8) saves replacing a lamp or a household-type fuse
"in the person's own electrical installation", Authority staff on duty, appliance
technicians who keep off any circuit "connected to a source of electricity supply",
and a trained employee following the written instructions of the electrical worker
in charge. Adding a socket in one's own home is not saved. An owner who **knowingly**
engages an unpermitted person also commits an offence (s 82(5)). No penalty is
stated, so s 92 applies: $10,000 or 12 months, $250 a day. Asserted.

### 6. Two penalty shapes are lopsided

s 6(2) (unlicensed generation, retail, trading and the rest) carries a fine up to
$500,000 and $12,500 a day but **no imprisonment**. s 83(2) (wilful tampering with an
installation so as to endanger life or property) carries imprisonment up to 5 years
and **no fine**. Asserted. s 6(1A) relieves the Authority of the licence only for
generation, transmission, import/export and wholesale trading, not for retail, market
support or operating the market. Asserted.

### 7. "High voltage" and "low voltage" overlap

s 2 defines high voltage as exceeding 1000V a.c. or 1500V d.c. between conductors,
"or" 600V a.c. or 900V d.c. to Earth, and low voltage as **not** exceeding the same
figures joined by the same "or". A supply above one limit and below the other meets
both definitions as written. This encoding treats it as high voltage (an inference).
Asserted on that reading.

### 8. Accidents: report on any hurt, freeze the site only on death or grievous hurt

s 94(1) requires the premises owner and the Part 9 licensee to report any accident
causing loss of life, hurt or serious property damage. The site may not be altered
without the Authority's approval until investigations finish only on loss of life or
grievous hurt (s 94(3)), and never so as to stop rescue or safety work (s 94(4)). An
inquiry is mandatory where non-compliance is suspected or the accident was
preventable (s 94(5)). Asserted.

## What would need doing before this is worth anything

- The Authority may modify the 7-day notice period (s 80(3)) and exempt installations
  (s 71); neither is encoded.
- Which offences are compoundable is left to regulations (s 93(2)); none were read.
- The arrangement of sections in the deposit is column-shifted against the body
  (for example, the arrangement prints "79" beside the s 80 heading); the body's
  numbering was followed.
- No regulations, Authority directions, codes of practice or case law were read.
