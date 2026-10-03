# Incident register — Dog Act 1976 (WA)

Findings about this subject. Two classes, kept apart because they are findings about
different things:

- **A-nn — the Act.** Logical, clerical and drafting defects in the source text.
  Every finding is traceable to a provision and demonstrable on stated facts: an
  incident that cannot be demonstrated by an assertion or a worked scenario is an
  opinion, not a finding. Findings that turn out to be sound drafting are kept and
  marked verified-no-defect, because knowing what was checked is part of the result.
- **C-nn — the corpus.** Defects in our own work on this subject — the deposits, the
  encoding, the provenance. Kept separate from A-nn because "the Act is wrong" and
  "we encoded it wrongly" are not the same claim and do not have the same repair.

No harness (H-nn) findings arose in this pass; the work that produced these entries
ran outside the pipeline, in the scheme console described under **Method** below.

Status vocabulary for this register: `OPEN`, `CANDIDATE`, `FIXED`, `WAIVED`,
`VERIFIED-NO-DEFECT`. `CANDIDATE` means raised and stated, but not yet demonstrated
to be a defect rather than deliberate policy — it is **not** a finding until promoted.

**Interpretive forks are not recorded here.** Where two readings of a provision both
survive, the entry belongs in [`registers/fork-register.json`](registers/fork-register.json).
Two forks in that register bear directly on the entries below and are cross-referenced
at the end rather than duplicated.

---

## A-01 — ss. 3, 33D(1): the owner commits the offence when the dog attacks the owner

- **Status:** OPEN · **Class:** substantive gap · **Severity:** medium ·
  **DEMONSTRATED** — worked scenario, scheme console, 2026-09-30
- **Not discovered here.** Michael Fairweather raised this at the Commonwealth
  Association of Legislative Counsel conference, Perth, February 2025, in the
  Greenfoot simulation segment of *Legislative Quality Assurance by Computer
  Simulation*. It arose there because a dog in a randomised population attacked its
  own owner, which nobody had thought to ask about. This entry records the finding,
  its reasoning and its reproduction; it does not claim the discovery.

**Provisions.** s. 3 "person liable for the control of the dog"; s. 33D(1), (2A); Pt VII.

Section 33D(1) makes the offence one committed by *every* person liable for the
control of the dog. Section 3 defines that class as the registered owner, the owner,
the occupier of premises where the dog is ordinarily kept, or a person who has the
dog in possession or under control — less two express exclusions: a veterinarian (or
someone acting on a veterinarian's behalf) in professional practice, and a police
officer or other person acting under a statutory duty or administering the Act.

The owner is in the class by definition. **Nothing in either provision takes the
owner out of it when the owner is the person attacked.**

**Worked scenario.** John owns Rex, a dog of a prescribed restricted breed. Rex bites
John, causing physical injury. There was no provocation and no reasonable cause.
The behaviour is an attack within s. 3; the attack caused physical injury, so s.
33D(1) is engaged; John is a person liable for the control of the dog; Rex is a
dangerous dog by breed alone. John commits an offence carrying a fine of not more
than $20,000 and not less than $1,000 — for being bitten by his own dog.

**Why this is not answered elsewhere.** Section 3 shows the drafter carving classes
out of the liable-person definition deliberately, and twice — for veterinarians and
for police. Neither carve-out is about who was attacked; both are about who was
handling the dog and why. The victim is not among them. Nor is there a s. 33D(2B)
defence on point: the defences there do not turn on the identity of the person
injured.

**Aggravation.** The consequence is not confined to the fine. A dangerous dog that
has caused physical injury attracts the Part VII destruction provisions, which may
be set in motion by a person other than the owner. So the owner-as-victim is exposed
to a penalty *and* to losing the dog, on facts where they are the only person harmed.

**Why it may never be seen.** An owner bitten by their own dog has no incentive to
report it, and every incentive not to. That makes this a defect that is unlikely to
surface in enforcement statistics and correspondingly unlikely to be found by
reading complaint records — which is the argument for finding it by simulation.

**Not yet settled.** Whether this is a defect or a deliberate choice — the Act may
intend the owner's liability to be strict and personal, precisely so that ownership
of a dangerous dog carries the risk — has not been tested against the second reading
speech or the explanatory memorandum. Recorded as OPEN on the drafting point, not as
a settled criticism of the policy.

---

## A-02 — s. 33GB(1): the offence attaches by the calendar alone, with no grace period

- **Status:** CANDIDATE · **Class:** question of policy or oversight · **Severity:** low
- **Raised:** 2026-09-30, scheme console, by stepping a created dog's age past three months.

**Provisions.** s. 33GB(1), (2); s. 33GC; s. 3 "dangerous dog".

Section 33GB(1) makes it an offence for the owner of a dangerous dog (restricted
breed) *that has reached 3 months of age* to keep it unsterilised. Section 33GB(2)
supplies two defences, both about the dog: that it is already sterile, or that it has
a physical condition making sterilisation likely to cause death.

The offence is therefore complete on a birthday. No act or omission by the owner on
that day is required, and neither defence is available to an owner whose difficulty
is one of timing rather than of the dog's physiology — an owner who acquired the dog
days before it turned three months, or who has a sterilisation appointment booked for
the following week.

**The interaction that makes it sharper.** While the dog is under three months and has
at least one restricted-breed parent it is a *restricted breed pup*, and s. 33GC shuts
down transfer of its ownership save in three narrow cases: a deceased estate passing
through an executor, an owner certified by a medical practitioner as incapable of
caring for it, and the Minister forming the view in his absolute discretion that
extraordinary conditions justify the transfer. So for the whole of the period before
the duty bites, the owner cannot lawfully hand the problem to someone else.

**Why this is only a candidate.** Both provisions may be doing exactly what they are
meant to do. Restricting the transfer and forcing sterilisation of restricted-breed
dogs is a coherent policy, and a grace period would blunt it. The candidate is not
that the scheme is wrong; it is that **no provision addresses the owner who is
willing and has simply not got there yet**, and that the absence looks unconsidered
rather than chosen. Promoting it would require the extrinsic material. Until then it
is a question, not a finding.

---

## A-03 — ss. 21(2), 21(5), 26B(1): an unchipped pup cannot be sold, though it need not yet be chipped

- **Status:** CANDIDATE · **Class:** question of policy or oversight · **Severity:** low
- **Raised:** 2026-09-30, while extending the scheme console to Part III Div 2. First
  noticed by a subagent reading the encoding; checked here against the compilation text
  (`registers/source-bundle/mrdoc_47983.txt`, compilation 08-b0-00).

**Provisions.** s. 21(2), (4), (5); s. 26B(1), (2).

Three provisions, each unremarkable on its own:

- s. 21(2): the owner of a dog "that has reached 3 months of age must ensure that the dog
  is microchipped". Nothing requires a younger dog to be chipped.
- s. 26B(1): "A person must not transfer the ownership of a dog that is not microchipped
  unless … the person is satisfied that a certificate referred to in section 21(4) or
  22(4) applies". A fine of $5,000. s. 26B(2): this applies "regardless of when or
  whether the dog was registered".
- s. 21(5): a vet's exemption certificate "cannot apply in respect of a dog that is under
  3 months of age".

Together: every transfer of an unchipped dog under three months is an offence, because
the only exemption s. 26B(1) recognises cannot exist for such a dog. A breeder who sells
an eight-week-old pup must have chipped it, although s. 21 — the provision headed
"Microchipping of dogs other than dangerous dogs" — would tell them there is no duty yet.

**Demonstrated** on stated facts in the scheme console, in Nature mode (called simulation
mode when this entry was written): "A puppy is
sold at eight weeks, unchipped". The pup is whelped on day 0, the clock runs 56 days,
and the transfer produces the s. 26B(1) offence. Not demonstrated by an `#ASSERT`.

**Why this is only a candidate.** It is very likely the policy: pups chipped before
sale. If so, the drafting achieves it. The candidate is that the Act reaches the result
only by combining three provisions, one of which (s. 21(5)) reads as a limit on
exemptions rather than as a sale rule. Promoting it needs the extrinsic material for the
2013 amendments.

---

## C-01 — the encoding gives `declared dangerous` no route to becoming true

- **Status:** OPEN · **Class:** corpus, modelling · **Severity:** low
- **Raised:** 2026-09-30, while giving each fact in a simulation a lawful provenance.

`dog-act-domain.l4` declares `DogProfile` with
`declared to be a dangerous dog (declared) under s 33E(1)` as a supplied BOOLEAN, and
`dog-act-1976.l4` encodes s. 33E itself. The two are not connected: nothing in the
corpus derives the boolean from an exercise of the s. 33E(1) power. The same is true
of `is a dangerous dog (restricted breed)`, though that one is defensible — the
breeds are prescribed by regulation, outside the Act's text, so treating it as a
supplied fact is correct.

`declared` is different. The Act supplies the power, the corpus encodes the power,
and the fact the rest of the corpus reads is still an input that any caller may
assert at will. Nothing is *wrong* in the sense of giving a bad answer, and for
isomorphic encoding of individual sections this is the right shape. But it means the
corpus cannot answer "could this state have been arrived at lawfully?", which is a
different and useful question.

**Why it was not visible before.** Reading section by section, a supplied fact is
unremarkable — every module treats cross-references outside its own text as
scoped-out inputs, by design and by the scope discipline in `NOTES.md`. It only
becomes visible when you try to run the scheme forward in time, because then every
fact has to have got its value from somewhere.

**Suggested repair.** None yet, and possibly none wanted: this may be a property of
the corpus worth keeping. Recorded so the decision is a decision.

---

## C-02 — s. 38(5) is encoded as a one-off duty, so a relapse during a nuisance order is missed

- **Status:** OPEN · **Class:** corpus, encoding · **Severity:** medium
- **Raised:** 2026-09-30, while extending the scheme console to s. 38. First noticed by
  a subagent reading the encoding; checked here against the text and the module.

**Provisions.** s. 38(3), (4), (5).

The Act: an authorised person may issue an order requiring the person liable for control
"to prevent the behaviour … by a time specified in the order" (s. 38(3)). "An order has
effect for 6 months after the day on which it is issued" (s. 38(4)). "A person to whom an
order is issued must comply with the order during the period in which it has effect"
(s. 38(5)).

The encoding (`dog-act-part6-div3-4-livestock-nuisance.l4`, the `s 38(5) compliance duty`
DEONTIC, around lines 227-236): `MUST prevent the behaviour … WITHIN` the time specified,
`HENCE FULFILLED`. The duty is discharged the first time the behaviour is prevented by the
specified time, and the six-month period in s. 38(4) does not appear. A dog that stops
barking by the deadline and starts again in month three breaches s. 38(5), and the
encoding records nothing.

**Demonstrated** on stated facts in the scheme console: "Barking again in month three of a
nuisance order". Complaint, order, compliance on day 14, persistent barking on day 90, and
the console records the s. 38(5) offence. The console follows the Act, not the encoding.
Not demonstrated by an `#ASSERT` against the module, which is the next step.

**Suggested repair.** Model the obligation as holding throughout the six months from the
day of issue — a duty to keep the behaviour prevented until the order lapses, not a
one-off deadline — and add an assertion for the relapse case. The fix belongs in
`legalese/l4-ide`, whose copy of the module is the authoritative one (`NOTES.md`).

---

## Method

The entries above came from building a scheme console — a day-stepped simulation in
which actors are laid out, acted on, and the consequences applied by rule with each
one traced to its provision. A-01 was reproduced there; A-02 and C-01 were raised
there; A-03 and C-02 were raised while extending it to Part III Div 2 and s. 38, and are
demonstrated there. The console is a demonstration artifact, not part of the pipeline, and
**nothing here has been through a machine check in this corpus**: A-01 is
demonstrated on stated facts, not by an `#ASSERT`. Turning it into an assertion in
`dog-act-1976.l4` is the obvious next step and has not been done.

## Related forks

These are recorded in [`registers/fork-register.json`](registers/fork-register.json)
and are not repeated here:

- **`F-ATTACK-PROVOCATION-UNLESS`** — whether the closing "unless the owner
  establishes … reasonable cause" in the s. 3 definition of *attack* reaches back over
  the provocation exclusion, or qualifies only the (a)–(d) inclusions. The corpus takes
  the categorical reading: provoked behaviour is not an attack, full stop.
- **`F-DANGEROUS-DOG-STATUS-TIMING`** — whether the dog's status as a dangerous dog is
  read at the time of the offence or at the time of prosecution, where the attack is
  itself the reason for a later declaration. The corpus takes status at the time of the
  offence. The two readings give $10,000 with no minimum, and $20,000 with a $1,000
  minimum, on identical facts. Asserted both ways at `dog-act-1976.l4:817-818`.
