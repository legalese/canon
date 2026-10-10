# Air Navigation Act 1966 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, with amendments to Act 3
of 2021 (in force 1 July 2025) and Act 36 of 2018 (in force 1 January 2024) shown.
The arrangement of sections at the head of the deposit is out of step with the
body; the body's section numbers are used.

**Checks:** one case file, 136 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**10 of the 527 Singapore Acts** deposited here cite it. This row takes the
offences and liabilities that a drone operator, an airline passenger, a visitor
to an aerodrome, an aircraft owner or a pilot actually meets: ss 32 to 35
(unmanned aircraft), 38 (unruly passengers), 41 (aerodrome trespass), 42
(trespass, nuisance and damage), 43 (dangerous flying) and 82 (compounding).
The aviation safety instrument regime, enforcement powers, reportable safety
matters (s 29, which works only through subsidiary legislation), aviation
security, and control of obstructions near aerodromes are not encoded.

## What the Act turns out to say

### 1. The person who takes the drone photograph is guilty even if someone else flies it

s 32(2): when a photograph of a protected area is taken from an unmanned aircraft,
"the operator of the unmanned aircraft, and the person taking the photograph if the
person is not the operator, shall each be guilty". Taking a photograph includes
video and live-streaming (s 32(7)). The prosecution need not prove the accused knew
the area was protected or that the drone carried a camera (s 32(5)(a)). The only
defences are an unintended photograph caused by weather or an unavoidable cause,
or a security officer's permit. Asserted.

### 2. A careful but deliberate overflight is still an offence; a careless accidental one is too

The s 33(5)(b)(i) defence needs BOTH that the accused did not intend the overflight
AND that it was not due to want of reasonable care. An operator who meant to fly
over, however carefully, and one who drifted over through carelessness, are both
guilty; only the careful accidental overflight escapes. Asserted.

### 3. "Nobody was hurt" is expressly no defence to dropping something from a drone

s 35(5): it is not a defence that no one died or was hurt, no property was damaged,
or no hazard was caused. An intentional drop with no harm is an offence. Exhaust is
excluded from "discharge" (s 35(8)). A careful operator whose drone leaked
accidentally has a defence only if they also took all reasonably practicable steps
to stop further discharge (s 35(4)(a)(ii)). Asserted.

### 4. The repeat-offender tier for drones counts only the same subsection

ss 32(4), 33(4), 35(3): a repeat offender has an earlier conviction "of an offence
under subsection (2)" (or (1) for s 35) of that same section. The maximum rises from
$50,000 / 2 years to $100,000 / 5 years. Carrying a prohibited item (s 34) is
$100,000 / 5 years from the first offence. Asserted (as numbers of earlier
convictions for the same offence; cross-section priors are not modelled).

### 5. Contributory negligence defeats strict liability for ground damage entirely

s 42(2): damages for material damage caused on the ground by an aircraft, or by
something falling from it, are recoverable from the owner without proof of
negligence, "except where the damage or loss was caused by or contributed to by the
negligence of the person by whom the damage or loss was suffered". Read on its words,
any contributory negligence is a complete bar to this route, not an apportionment
(an inference from the text; the general law of contribution was not consulted).
Liability shifts to the hirer only where the aircraft was hired out for MORE than
14 days and none of the operative crew is employed by the owner (s 42(4)). Asserted.

### 6. The owner and the hirer answer for dangerous flying unless they prove no fault

s 43(1): the pilot is guilty, "and also the owner ... unless he, she or it proves
... that the aircraft was so flown without his, her or its actual fault or privity";
"owner" includes the hirer at the time (s 43(2)). The burden is on the owner.
Asserted.

### 7. Unruly-passenger penalties fall into three tiers, and "in flight" ends when a door opens

Interfering with or abusing crew, endangering the aircraft, or disobeying the
pilot-in-command: $100,000 / 5 years. Dangerous intoxication: $20,000 / 12 months,
with defences for involuntary intoxication and authorised prescription medication
(s 38(5)). Device use and smoking: $5,000 / 12 months. An aircraft is in flight
from the closing of all external doors after embarkation until a door is opened for
disembarkation, or after a forced landing until the police arrive (Singapore) or the
local authorities take over (abroad) (s 38(6)). Asserted.

### 8. Compounding is capped at the lower of half the maximum fine and $5,000

s 82(1). Which offences are compoundable is left to Ministerial rules, which were
not retrieved. Asserted.

## What would need doing before this is worth anything

- The protected-area orders (s 32(1)), the compoundable-offences rules (s 82(3)) and
  the aviation safety subsidiary legislation (device use, reportable matters) were
  not retrieved; several offences cannot be applied without them.
- s 38(2) (disobeying commands) and s 38(4) were encoded as not requiring the
  aircraft to be in flight, since their words do not say so; s 38(1) and (3)(b)
  were encoded as requiring it. That reading is untested.
- s 39(5) (10 years for reckless endangerment involving an unmanned aircraft) and
  the general offences in ss 37, 39 and 40 are not encoded.
- No case law or CAAS guidance was searched.
