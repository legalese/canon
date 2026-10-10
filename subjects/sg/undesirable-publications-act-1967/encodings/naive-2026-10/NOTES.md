# Undesirable Publications Act 1967 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition (amendments up to 1 December 2021, in operation
31 December 2021), informal consolidation, version in force from 9/3/2025, as
deposited at `../../registers/source-bundle/UPA1967.txt`. The latest amendment
annotated is Act 5 of 2025 (wef 09/03/2025), to s 18.

**Checks:** one case file, 53 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is requirement **REQ-0055**: Tier 2 of the remaining Singapore Acts, ordered
by everyday-life relevance. The requirement asks what the Act decides for a person
or business it applies to; no scenario has asked a sharper question yet. The Act is
short (21 sections), so most of it is here: what counts as a publication and as
supply, obscene and objectionable, the offences and penalties, the delivery duty,
forfeiture, the return of seized items, border declarations, corporate officers,
detention, destruction and appeal, and exemptions. Not encoded: the Minister's
order-making power under s 5 beyond its effect, the s 4(2) list of matters to
consider, package examination (s 8), Magistrate's warrants (ss 10(1), 13(1)), the
court's disposal order (s 13(2)), arrest (s 14), appointments (s 18) and the bar to
legal proceedings (s 19). No prohibition order, register entry or regulation was
retrieved, so which publications are actually prohibited is not known to this row.

## What the Act turns out to say

### 1. Making an obscene publication for yourself is an offence; keeping or importing one for yourself is not

ss 11(a) and 12(a) catch anyone who "makes or reproduces, or makes or reproduces for
the purposes of sale, supply, exhibition or distribution to any other person". The
first alternative carries no purpose, so read literally it catches making or copying
for one's own use. Limb (b), importing or possessing, needs a purpose of passing it
on. So copying an obscene file for yourself is caught and importing or keeping one for
yourself is not. The literal reading is the encoding's; no case law was searched to
see whether courts read a purpose into limb (a). Asserted.

### 2. Whether a publication is "objectionable" is a controller's opinion, and evidence is not essential

s 4(1): objectionable "if, in the opinion of any controller", it deals with sex,
horror, crime, cruelty, violence or drugs in a manner likely to be injurious to the
public good, or with race or religion in a manner likely to cause enmity between
groups. The list in (a) is introduced by "matters such as", so it is illustrative.
s 4(3) makes the question "a matter for the expert judgment" of the decider, and
evidence "is not essential". Yet a s 12 offence turns on the publication being
objectionable. One part or item is enough (s 4(1)), as it is for obscenity (s 3).
Asserted (the opinion is an input).

### 3. A repeat offence under s 6 carries imprisonment only, with no fine

s 6(1) (importing, selling, supplying, reproducing and the rest): first offence up to
$10,000 or 3 years or both; subsequent offence "imprisonment for a term not exceeding
4 years". s 6(2) (possession without reasonable excuse): $2,000 or 12 months or both;
subsequent offence up to 2 years. No fine is mentioned for a subsequent offence. On a
possession charge the accused is presumed to have known the contents (s 6(3)). The
s 11 and s 12 offences have no repeat-offence uplift. Asserted.

### 4. Receiving a prohibited publication unasked is not a defence; it is a duty to hand it in

s 7: a person sent a prohibited publication without knowledge or privity, or who
ordered it before the prohibition, or who held it when the prohibition took effect,
must "forthwith" deliver it to a police station once its nature is known. Failure: up
to $1,000 or 12 months or both. Someone who orders it after the prohibition is not in
s 7 at all; that is the s 6 offence. Asserted.

### 5. Forfeiture follows even an acquittal

s 9: if satisfied a document is a prohibited publication, the court "shall, whether
the alleged offender is convicted or not", order it forfeited. s 13(2) gives a similar
power (a "may") for obscene and objectionable material. Asserted for s 9.

### 6. Detained items can be destroyed only after 3 months, and not while an appeal is open

ss 15(2)(b), 16(3): if no proceedings are instituted within 3 months of detention, the
controller may return the item or, if it is obscene or objectionable or return is
impracticable, destroy it "subject to section 20". s 20(5): no destruction unless the
detention was not appealed, or the appeal was dismissed or abandoned. The appeal goes
to the Minister in writing with reasons within 14 days of service of the notice, and
the Minister's decision is final (s 20(1), (2)). s 13(3), for items seized under a
warrant, says they "shall be returned" when no proceedings follow within 3 months.
s 19 bars any claim for loss, damage or delay to a seized item (not encoded). Asserted.

### 7. At the border, a declaration on demand, and an importer pays more for refusing

s 16(1): an importer or a person entering Singapore must, if required by a controller
or authorised officer, declare any publication and produce it. Failure is a fine of up
to $1,000 for a traveller and $5,000 for an importer, with no imprisonment (s 16(4)).
Asserted.

### 8. Smaller points

- A film is not a "publication" (s 2), "film" taking its meaning from the Films Act 1981
  (that films are regulated there instead is an inference). Asserted.
- Supply includes emailing or faxing the contents and lending or hiring (s 2).
  Broadcasting is excluded from "electronic transmission"; the encoding infers that
  broadcasting is outside supply. Asserted on that inference.
- Officers of companies, partners and officers of associations are guilty too where the
  offence was by their consent, connivance or neglect (s 17). Asserted.
- A sergeant or above may search without a warrant where delay would frustrate the
  search (s 10(2)). Asserted.
- Exemptions may be given to a person or limited class for educational, professional,
  scientific, artistic or technical reasons (s 21(3)), on application with a prescribed
  fee. Asserted.

## What would need doing before this is worth anything

- No prohibition order under s 5, entry in the Register of Objectionable Publications
  (s 4(4)) or exemption regulations were retrieved.
- No case law was searched, in particular on the literal reading of ss 11(a), 12(a)
  (finding 1) and on the obscenity test.
- "Within 3 months" and "within 14 days" are encoded as at most 3 months and at most 14
  days; the counting convention was not checked against the Interpretation Act.
