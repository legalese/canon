# Visiting Forces Act 1960 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, as deposited at
`../../registers/source-bundle/VFA1960.txt`. The deposit says it incorporates all
amendments up to and including 1 December 2021 and came into operation on
31 December 2021. No later amendment is annotated in the text.

**Checks:** one case file, 54 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**6 of the 527 Singapore Acts** deposited here cite it. This row takes the rules
with decision content for a person, a police officer, a prosecutor, a coroner or a
court: who is connected with a visiting force (ss 2, 4, 5), whose service courts may
act in Singapore (s 6), when a Singapore prosecution may proceed (s 7), custody after
arrest (s 9), claims the courts will not hear (s 10), death inquiries and removal of
bodies (s 11), the weight of certificates (ss 14, 16, 18(1)(a)), deserters (s 15) and
lending Singapore personnel (s 17(1), (5)). Not encoded: the President's orders
designating countries and modifying the Act (s 3), extending Singapore-forces law to
visiting forces (s 12), claims settlement (s 13), the passport presumptions (s 14(3)),
mutual powers of command (s 17(2)-(4)) and the identity presumptions of s 18(2), (3).

Which countries have been designated, and what any treaty says about who holds
primary jurisdiction over an offence, is not in the deposit. The encoding takes both
as inputs.

## What the Act turns out to say

### 1. A Singapore court cannot even start a prosecution of a visiting serviceman without the Public Prosecutor's certificate

s 7(1): no prosecution of a member of a visiting force "shall be instituted" unless
the Public Prosecutor certifies that Singapore holds exclusive or primary jurisdiction
under a treaty and has not waived it, or that the service authorities held the primary
right and waived it. The certificate is conclusive (s 14(6)). Arrest and remand may
still go ahead without it, but the case "shall not be further prosecuted" until it is
given (s 7(4)). A person already tried by the service court for the same offence cannot
be tried again here (s 7(2)). The President may extend s 7(1) by order to other
associated persons (s 7(3)). Asserted.

### 2. A Singapore citizen serving in a visiting force falls under its service courts

s 6(2)(b) and (c) exclude Singapore citizens (and, in (c), ordinary residents), but
s 6(2)(a), "members of any visiting force", carries no such condition. The one
exception is the proviso: someone who joined the force while in Singapore is not
treated as a member unless it is shown he joined with his consent. Asserted.

### 3. Police must hand an apparently associated arrestee to the service authority; otherwise they get 24 hours

s 9(2): if a relevant association is apparent, the person "shall as soon as
practicable" be delivered to a service authority. If it is not apparent but there are
reasonable grounds to believe he is subject to the service courts, he may be held for
up to 24 hours; if not delivered within that period he must be bailed or brought
before a Magistrate. Asserted (the encoding treats hour 24 as within the period).

### 4. Coroners stand down, and the body may leave Singapore, unless the Minister intervenes

s 11(1): a Magistrate or Coroner satisfied that the deceased had a relevant association
"shall not hold the inquiry", or must adjourn it, unless the Minister otherwise
directs; s 11(2) does the same where someone subject to the service courts has been
charged there with causing the death, or is detained to be charged. s 11(4): laws
restricting removal of a body from Singapore do not apply to such a body, unless the
Minister has required the inquiry to be held or resumed (s 11(5)). Asserted.

### 5. Dependants and civilians are defined by residence and by passport entries

A dependant must be "not ordinarily resident in Singapore" (s 2(1)), and time spent
here as a member, civilian or dependant does not count towards ordinary residence
(s 2(5)). A member of a civilian component, for Part 2, is defined by three
passport conditions: a non-Singapore passport, an uncancelled sending-country entry,
and an uncancelled, unwithdrawn note of recognition by the Minister for immigration
(s 4(1)). Reservists count as members only while called into actual service or out for
training (s 2(2)). Asserted.

### 6. Some certificates are conclusive, others yield to contrary proof

Conclusive: a service court sentence, detention or trial (s 14(2)); the Public
Prosecutor's s 7 certificate (s 14(6)); presence of a force in Singapore (s 18(1)(a)).
Sufficient unless the contrary is proved: membership of a visiting force (s 14(1)), a
dependant passport entry (s 14(4)), an offence arising in the course of duty (s 14(5)),
and a commanding officer's deserter certificate (s 16(b)). Five of these are
asserted; the dependant entry and deserter certificate are encoded but not asserted.

### 7. Smaller rules

- No Singapore court will hear a claim about pay, terms of service or discharge from
  service in a visiting force or its civilian component (s 10). Asserted.
- A service court death sentence may be carried out in Singapore only if Singapore
  law could have imposed death in a similar case (s 6(4)). Asserted.
- Deserters from a designated country's forces may be apprehended under the Singapore
  Armed Forces Act 1972 powers only at the request of that country's appropriate
  authority (s 15(2)). Asserted.
- A Singapore serviceman may be placed at a foreign force's disposal only with his
  consent (s 17(1)); forces count as serving together "if and only if" the President
  so declares by order (s 17(5)). Asserted.

## What would need doing before this is worth anything

- The President's designation orders under s 3, and the treaties that allocate primary
  jurisdiction, were not retrieved; every rule here takes them as inputs.
- s 11(2) is expressed "subject to subsection (1)"; the encoding simply ORs the two
  grounds for not proceeding, which is an inference about how they combine.
- s 9(2)(b)'s "within that period" is read as allowing the full 24 hours; whether
  bail or a Magistrate is due at, or only after, the 24th hour is not tested by case law.
- No case law or subsidiary legislation was searched.
