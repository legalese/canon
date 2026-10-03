# Incident register — Cat Act 2011 (WA)

Findings from encoding the Cat Act 2011, its Regulations and its Explanatory Memorandum.
Classes are kept apart because they are claims about different things:

- **A-nn — the Act** (or its regulations): logical, clerical and drafting defects in the source.
- **B-nn — the Bill**: findings against the Cat Amendment (Local Laws) Bill 2026 (Bill 53), which
  is **not law**. It was before the Legislative Council at second reading on 16 September 2026, and
  the print read is the as-introduced print of 25 February 2026 — see the note under B-01 on why
  that is also the print now before the Council.
- **C-nn — the corpus**: defects in our own work — the deposits, the encoding, the provenance.
- **H-nn — the harness**: defects in the pipeline itself. None new here; the harness defects
  recorded at `../retail-barring-orders-bill-2025/INCIDENTS.md` (H-01 onward) still reproduce, and
  they are why no pipeline stage has run over this subject.

Status vocabulary: `OPEN`, `CANDIDATE`, `FIXED`, `WAIVED`, `VERIFIED-NO-DEFECT`.

**Every finding is traceable to a provision and reproducible by machine.** Where a finding rests on
stated facts rather than an `#ASSERT`, it says so. Interpretive forks are not defects and live in
[`registers/fork-register.json`](registers/fork-register.json).

**Two findings were retracted on review.** A-01 and A-03 were raised against the Act read alone and
did not survive the delegated legislation and the Interpretation Act. They are kept, marked
verified-no-defect, because knowing what was checked and found sound is part of the result — and
because the reason each dissolved is itself worth recording.

---

## A-01 — the exempting certificate cannot exist before the duty attaches

- **Status:** VERIFIED-NO-DEFECT (raised 2026-09-30; retracted the same day)
- **Provision:** ss 14(1), 14(3), 18(1), 18(3)
- **Severity when raised:** high · **Severity now:** none, beyond the drafting observation below

**What was raised.** The duty attaches to "a cat that has reached 6 months of age", and a vet
certificate excusing microchipping or sterilisation "cannot apply in respect of a cat that is under
6 months of age". So the exemption cannot exist until the duty already does, and an owner whose cat
cannot safely be chipped is in breach while the certificate is obtained.

**Why it does not stand.** The duty fixes no time, so the **Interpretation Act 1984 (WA) s 63**
supplies one: "Where no time is fixed or allowed within which an act or thing shall be done, such
act or thing shall be done with all convenient speed and as often as occasion arises." The owner
therefore has all convenient speed after the cat's sixth month, and an owner obtaining the
certificate within it is not in breach. The Explanatory Memorandum reads the same way, describing
the duty as to have the cat microchipped and sterilised "**by** 6 months of age". That reading is
recorded as **FORK-2** and is the one the encoding takes.

**What survives, as an observation rather than a defect.** ss 14(3) and 18(3) still spend a
certificate given before the cat turns 6 months. A vet who examines a five-month-old kitten, decides
the procedure would harm it, and issues a certificate has issued a document with no effect; it must
be re-issued once the cat is six months old. That is friction, not a trap, and it is what the
drafter wrote.

**Reproduced:** `cat-cases.l4` § `A-01`, the pair on `Anne and Smudge, certified at five months`
(in breach: sat on it) and `Anne, acting promptly, certified at five months` (not in breach). The
pair is also the boundary case for FORK-2.

---

## A-02 — sterilised, but not by a veterinarian

- **Status:** OPEN · **Class:** definitional mismatch · **Severity:** medium
- **Provisions:** s 3(1) definition of `sterilised`, s 18(1), s 9(2)(d)

s 3(1) defines `sterilised` as "made permanently infertile by a surgical procedure" and says nothing
about who performs it. s 18(1) requires the owner to ensure the cat is "sterilised **by a
veterinarian**". s 9(2)(d) makes refusal of registration mandatory where "the cat is not
sterilised" — the defined term, not the s 18(1) formula.

For a cat sterilised by someone who is not a veterinarian, both of these are true at once: the owner
is in breach of s 18(1), and the local government **must not** refuse registration on ground (d),
because the cat is `sterilised` as the Act defines it. The registration gate that the Explanatory
Memorandum describes as the Act's compliance mechanism — "Registration will be a key mechanism to
ensure compliance … through the requirement for cat owners to provide evidence … that the cat is
microchipped and sterilised" — does not catch this case.

The regulations do not close it: reg 18 prescribes how a cat is *identified* as sterilised (a s 21
certificate or an ear tattoo), and a s 21 certificate comes from a veterinarian, but s 9(2)(d) still
turns on the defined term rather than on the certificate.

**Reproduced:** `cat-cases.l4` § `A-02`, on `Anne and Smudge, sterilised by a breeder`: the owner
contravenes s 18(1), and no ground in s 9(2) applies.

---

## A-03 — the sterilisation of an unmicrochipped cat is recorded nowhere

- **Status:** VERIFIED-NO-DEFECT (raised 2026-09-30; retracted the same day)
- **Provisions:** s 20, and Cat Regulations 2012 reg 17

**What was raised.** s 20 obliges a veterinarian who sterilises a **microchipped** cat to notify the
microchip database company within 7 days. A cat sterilised before it is ever microchipped triggers
no notice, so its sterilisation appears in no database.

**Why it does not stand.** Reg 17 prescribes what a microchip implanter must give the database
company under s 15, and paragraph (m) is "the age, breed (if known), colour, gender **and
sterilisation status** of the cat". So when the cat is later microchipped — which s 14(1) requires
anyway — its sterilisation status is reported. Reg 16(k) separately requires the local government's
register to record "the cat's sterilisation status" at registration. The gap existed only in a
reading of the Act without its regulations.

**Method note.** This is the second finding in this subject retracted by reading the delegated
legislation. An incident raised against a WA Act before its regulations are read should be treated
as provisional until they are.

---

## A-04 — the Explanatory Memorandum describes a discretion the Act does not confer

- **Status:** OPEN · **Class:** extrinsic material at odds with the enacted words · **Severity:** low-medium
- **Provisions:** s 9(1)-(4); Explanatory Memorandum, Cat Bill 2011, clause 9

The Act: "A local government **must** refuse an application for the grant or renewal of the
registration of a cat **if, and only if**, the local government is satisfied that one or more of the
following apply". Mandatory when a ground applies, and forbidden when none does.

The Explanatory Memorandum: "Subclause (2), (3) and (4) provides that a local government **can**
refuse to grant or renew registration for the following reasons". Permissive, and silent on the
"only if" limb.

Under the **Interpretation Act 1984 (WA) s 19** an explanatory memorandum is extrinsic material that
may be considered, but it is not the law and the enacted words prevail. The finding is not that the
Act is ambiguous; it is that the document written to explain the Act to the people who administer it
describes a power where the Act imposes a duty. A local government that followed the memorandum
would believe it could register a cat that is not microchipped, which s 9(2)(c) forbids, and could
decline one on a ground outside the list, which "if, and only if" also forbids.

The same memorandum omits the second limb of s 18(2)(b), describing the breeder exemption as "the
cat is owned by an approved breeder" where the Act requires it to be "owned, **for the purpose of
breeding**, by an approved cat breeder".

**Demonstrated on stated facts, not by an `#ASSERT`:** the encoding implements the enacted words, so
no assertion can fail on the memorandum's account of them. `a ground in section 9(2) applies` is the
rule to read against clause 9 of the memorandum.

---

## A-05 — reg 10 exempts an owner where s 6(2) authorises exempting a class of cats

- **Status:** CANDIDATE · **Class:** possible excess of the regulation-making power · **Severity:** low
- **Provisions:** s 6(2), s 76; Cat Regulations 2012 reg 10(2)

s 6(2): "Subsection (1) does not apply if **the cat belongs to a class of cats prescribed** as
exempt from wearing registration tags when in a public place." The power is to prescribe a class of
**cats**.

Reg 10(2): "**The owner** of a cat that is being exhibited **is exempt from the requirement** to
ensure the cat wears its registration tag in a public place in section 6(1) of the Act." That
exempts a **person** from a duty, by reference to what is being done with the cat at the time, and
"a cat that is being exhibited" is a description of a temporary activity rather than obviously a
class of cats.

Whether that matters is genuinely arguable, and this is recorded as a candidate rather than a
finding. Against it: s 76 confers a general regulation power, "a class of cats" may fairly include
cats defined by what is presently being done with them, and the practical effect is identical
either way. For it: the two provisions are not saying the same thing, and the drafter of reg 10 had
s 6(2)'s words in front of them.

**A human should decide this one**, and it needs someone who knows WA delegated-legislation
practice, not a machine. The encoding implements reg 10 as written, because it is the regulation
that creates the exemption; see the note in `cat-regulations-2012.l4` § 10.

### Revised 2026-10-01: the Bill's Explanatory Memorandum supplies the practice this asked for

A-05 said it needed someone who knows WA delegated-legislation practice. The Explanatory Memorandum
to the Cat Amendment (Local Laws) Bill 2026 records what that practice is, on the neighbouring
subsection of the same Act:

> Prior to this Bill, several local governments had attempted to make cat containment local laws.
> The Joint Standing Committee on Delegated Legislation (JSCDL) has held the view that the existing
> powers of the Act did not permit these local laws to be made.

Three things follow, and they cut the same way as A-05:

1. **The empowering words are read strictly.** s 79(3)(f) said "specifying places where cats are
   prohibited absolutely". The JSCDL did not read that as reaching curfews or district-wide
   containment, even though the practical effect was within the Act's evident purpose. A-05's
   complaint is of the same shape: s 6(2) says "a class of **cats**", and reg 10(2) exempts an
   **owner**.
2. **Interpretation Act s 43 was not treated as curing the mismatch.** The Bill's new s 79(4) is
   expressed "[w]ithout limiting … the Interpretation Act 1984 section 43(7) or (8)", and the EM
   quotes s 43(7) in full. If s 43(7)-(8) had already supplied what the local laws needed, no
   amendment was required. They govern *how* a power may be exercised, not *what* it extends to —
   which is precisely the distinction A-05 turns on.
3. **The Government's chosen remedy was to amend the Act.** Not to argue that the regulations were
   valid, nor that s 43 saved them. That is the strongest available signal about how the question is
   actually resolved in this jurisdiction.

**Status unchanged at CANDIDATE**, deliberately. This is an argument by analogy from s 79(3)(f) to
s 6(2): a different provision, a different delegate (local government against the Governor), and
the JSCDL's view on the earlier local laws is reported by the EM rather than read in the Committee's
own report, which was not retrieved. It is now a supported candidate rather than an open question,
and the thing that would settle it is the JSCDL's report itself.

---

## B-01 — the Bill cannot decide whether it confers a power or clarifies one, and validates nothing

- **Status:** OPEN · **Class:** retrospective effect left unresolved · **Severity:** medium-high
- **Provisions:** Bill 53 cll 2, 4; Explanatory Memorandum, Overview; Interpretation Act 1984 (WA) s 43(1)

The Explanatory Memorandum says both of these things, two paragraphs apart:

> The Bill … amends the Cat Act 2011 … **to provide a head of power** in the Act to enable local
> governments to make local laws that … restrict cats to their owners' premises …

> The Bill is intended to **clarify the existing legislation** and ensure local governments have
> clearly expressed authority …

Those are different claims with opposite consequences, and the difference is not academic, because
the same Overview records that the question has already arisen in practice:

> Prior to this Bill, several local governments had attempted to make cat containment local laws.
> The Joint Standing Committee on Delegated Legislation (JSCDL) has held the view that the existing
> powers of the Act did not permit these local laws to be made.

If the Bill **confers** a power, then the containment local laws already made were beyond power, and
**Interpretation Act 1984 (WA) s 43(1)** — "subsidiary legislation shall be void to the extent of
any such inconsistency" — made them void from the start. If the Bill **clarifies**, they were valid
all along.

**The Bill resolves this neither way.** It has four clauses: short title, commencement, Act amended,
s 79 amended. There is **no transitional provision, no validating provision, and no declaratory
provision**, and cl 2 commences the operative clause "on the day after" Royal Assent — purely
prospectively. So on the JSCDL's view the affected local laws were void before commencement and stay
void after it, and every enforcement action taken under one was taken under a void instrument. A
single validating clause would have settled it; the Act's own s 79 is silent, and so is the Bill.

Which way this falls is the subject of **FORK-3**, and the fork is not the defect. The defect is that
a Bill whose own memorandum says the question has already been litigated before a parliamentary
committee leaves it open.

**Demonstrated on the Bill's text, not by an `#ASSERT`:** the absence of a provision cannot be
asserted. The claim is checkable by reading `sources/bill-53-1-cat-amendment-local-laws-2026.txt` —
four clauses, and cl 4 is the whole of the amendment.

**Note on the print.** The Bill page offers "Bill as Introduced" and "Bill as passed by originating
House" as separate downloads. Both return **byte-identical** PDFs (sha256
`032892c4c90977943f29668f4a8b218b4e1c1036768acece0d31feb7bae8d224`), so although the Assembly held
Consideration in Detail on 15 September 2026, the Bill reached the Council unamended — or the second
link is mislabelled. The digests are recorded in the source bundle so that a reader can tell which.

---

## B-02 — the Bill expands s 79(3)(f) and leaves s 79(1) untouched

- **Status:** OPEN · **Class:** observation on the scope of the repair · **Severity:** low
- **Provisions:** s 79(1), s 79(3); Bill 53 cl 4

s 79(3) opens "**Without limiting subsection (1)**", so its eleven paragraphs are illustrations of
the general power in s 79(1), not a closed list. A local law that fits no paragraph of (3) may still
be supported by (1) — "all matters that are … necessary or convenient to be so prescribed, for it to
perform any of its functions under this Act".

It follows that the Bill was thought necessary only because s 79(1) was **also** considered not to
support cat containment. If (1) had supported it, (3)(f) would not have needed amending, since (3)
cannot cut (1) down. The Bill amends (3)(f) and says nothing about (1).

That leaves the repair narrower than the problem it is aimed at. Any future local law of a kind
new s 79(4) does not name is back in the position the containment laws were in: arguing from
s 79(1), against a committee view that s 79(1) did not carry the earlier laws. The Bill's
"[w]ithout limiting … the Interpretation Act 1984 section 43(7) or (8)" does not help, because
s 43(7)-(8) govern how a power may be exercised, not what the power extends to.

**Reproduced:** `cat-part6-cases.l4` § `What the Bill does, and does not, change`, the pair on
`the night curfew` and `the night curfew, resting on section 79(1)`. The same local law, and the
Bill changes the answer for the first and not the second. The inference about what was *thought*
about s 79(1) is an inference, and no assertion makes it.

---

## B-03 — a containment local law can forbid the journey that Part 2 requires

- **Status:** VERIFIED-NO-DEFECT · **Class:** cross-Part interaction · **Severity:** none, as answered
- **Provisions:** new s 79(4)(a)(ii) and Example 3; ss 14(1), 18(1); Interpretation Act 1984 (WA) s 43(1)

New s 79(4)(a)(ii) lets a local law prohibit a cat from being in "any place other than the premises
at which the cat is ordinarily kept". ss 14(1) and 18(1) require the owner to ensure the cat is
microchipped and **sterilised by a veterinarian** — duties discharged only by taking the cat to
veterinary premises. A local law in the terms of (4)(a)(ii) forbids that journey.

Example 3 to s 79(4) carves it out:

> A local law may prohibit a cat from being in any place other than the premises at which the cat is
> ordinarily kept, unless — (a) the cat is being transported to, or is at, veterinary premises; and
> (b) the cat is contained, or under the effective control of a person.

But an **example is not a requirement**. Nothing in the Bill obliges a local government to include
it, and a local law that omits it makes compliance with ss 14(1) and 18(1) impossible.

**Why there is no defect.** Interpretation Act 1984 (WA) s 43(1) answers it without needing anything
in the Cat Act: such a local law is inconsistent with the Act under which it is made and is "void to
the extent of any such inconsistency". The cat may go to the vet. This is the third finding in this
subject answered by the Interpretation Act rather than by the instrument in front of us — see A-01
(s 63) and A-04 (s 19) — and the pattern is now worth stating as a method rule: in WA, read the
Interpretation Act before reporting a gap.

**Reproduced:** `cat-part6-cases.l4` § `Where Part 6 meets the Part 2 duties`, on
`the containment local law, no vet carve-out`: it obstructs a Part 2 duty, it is void to that
extent, **and** it is within the amended power — validity under s 79 and voidness under s 43(1)
being different questions. The paired case
`the containment local law, with the vet carve-out` does not obstruct.

---

## C-01 — what is deposited, and what is only cited

- **Status:** OPEN · **Class:** provenance · **Severity:** low

The Act, both regulations and the Assembly Explanatory Memorandum are deposited. Three things are
cited but not held:

1. **The second reading speeches** (Assembly p. 4260b, 15 June 2011; Council p. 7430b, 21 September
   2011). Their exact URLs are in the source bundle. `parliament.wa.gov.au` refuses scripted clients
   with HTTP 403, and unlike `/Bills.nsf/`, the `/Hansard/` path is refused even to a same-origin
   fetch from inside a real browser. Nothing was circumvented; the speeches are simply not held.
2. **The Council Explanatory Memorandum** (`EM - Bill197.002.pdf`), not extracted. The Assembly one
   was, and the two are usually identical, but that is an assumption and not a check.
3. **The Explanatory Memoranda and speeches for the five amending Acts.** Not retrieved. The Act's
   text as compiled is what the encoding reads, so nothing in the encoding depends on them, but any
   claim about *why* an amended provision reads as it does would.

The deposited EM is an **extract**, not the whole document: the clause notes for the Divisions this
subject encodes, with the full document's URL, byte count and sha256 recorded so the extract can be
checked against it.
