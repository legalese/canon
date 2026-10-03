# Incident register: Residential Tenancies Amendment (Rent Cap) Bill 2026 (WA)

Bill No. 70, a private member's Bill (Hon Tim Clifford MLC), introduced in the Legislative Council
on 7 May 2026. At 2026-09-30 it is still at Legislative Council second reading. The text we hold
is the Bill **as introduced**: `Bill+70-1+(2026).pdf`, sha256
`35266e07ea3164ad9107c06a5b71ecfc40015c9cde89e979a201de4c02f30e12`. The Act text is
`../registers/source-bundle/mrdoc_49316.txt`, retrieved 2026-09-07.

Extrinsic material, read on 2026-09-30 (text in `sources/`):

| file | what | sha256 |
|---|---|---|
| `EM.pdf` → `sources/em.txt` | Explanatory Memorandum, tabled 7 May 2026 (paper 1154) | `30019b93…2374b` |
| `Debate.pdf` → `sources/debate.txt` | LC Hansard, 7 May 2026: introduction and second reading speech | `6498365d…72fa6` |
| `sources/act-rta-1997-r84-part5-excerpt.txt` | Residential Tenancies Act 1997 (ACT), Republication 84, Part 5: the model the EM names | recorded in the file |

This register uses the same classes and discipline as
`../../retail-barring-orders-bill-2025/INCIDENTS.md`:

- **B-nn**: a finding about the Bill, including how it fits the Act it amends.
- **F-n**: a fork, where the Bill supports more than one reading.
- **V-nn**: something checked and found sound.

Every B-nn is reproduced by an `#ASSERT` in `rent-cap-bill-rent.l4` or
`rent-cap-bill-termination.l4`, and each assertion is marked with the finding's number in the
comment above it. There are 43 assertions and all of them pass. Points that could not be
reproduced that way are kept separately under **Observations**, because by our own rule they are
opinions, not findings.

Statuses: `OPEN`, `FIXED`, `WAIVED`, `VERIFIED-NO-DEFECT`. Every item below is `OPEN` unless it
says otherwise.

## Summary

| id | severity | where | in one line |
|---|---|---|---|
| B-01 | high | s.31AA(2)(a) × s.30(2)(a), s.82; ACT s.64B(1)(a) | The cap never applies to a fixed-term increase, and any agreement term switches it off. The ACT model limits this exception to leases signed before its own reform |
| B-03 | high | s.31AA × s.31A | The cap cannot operate on income-based rent |
| B-05 | high | s.64(4)(c) unamended; s.71BA(4)(c) | The court may order possession at day 60, before the new 3-month, 6-month or 90-day notice periods run |
| B-09 | high | ss.106, 107 × s.72(1) | s.107 relies on a tenant's s.72(1) application, which cannot exist; lessors' pending s.71/72 applications are left unresolved |
| B-02 | medium | s.31AA "under section 30 or 31A"; ACT s.64AE | Rent raised through a renewal agreement is not capped. The ACT model caps it |
| B-14 | medium | s.31AB(6) × EM | The EM says a s.31AB order lasts "up to 1 year"; the Bill fixes it at 1 year |
| B-04 | medium | s.31AA(1) formula | Index numbers "published most recently before" two different days may be on different reference bases |
| B-06 | medium | s.31AB(5), (6), (8) | The offence covers rent "from the residential premises" for a year, including under a later tenancy the order does not govern |
| B-07 | medium | s.70A(2) as amended | Social housing tenants lose s.70A: the fixed term can end on its expiry day and the tenant's end-of-term notice disappears |
| B-08 | medium | s.71BA | The Bill does not say whether s.71BA can end a social housing fixed term during its currency |
| B-11 | medium | s.31AA(2), (3) × s.30(3) | No stated consequence when a notice breaches the cap or omits the required statements (see F-1) |
| B-10 | low | s.65 × s.31AB | s.65 protects a tenant during s.32 proceedings but not during s.31AB proceedings |
| B-12 | low | cl.2(b)(i) | The 1 July 2026 commencement limb can no longer operate |
| B-13 | low | ss.64, 71BA | Clerical: cross-reference form, grammar, an undefined term |

---

## What the Explanatory Memorandum and second reading speech add

Neither document is law, but under s.19 of the Interpretation Act 1984 both may be used to confirm
a provision's ordinary meaning, or to resolve ambiguity or a manifestly absurd result. Four things
matter here.

1. **The cap is modelled on the ACT.** The EM says it "corresponds with the system currently in
   place in the ACT". The speech calls it "a system that is aligned with the Australian Capital
   Territory", and later says "We only have to look to the ACT". s.31AA(2) and (3) do follow ACT
   s.64B(1) and (2) almost word for word. The places where they depart from it are B-01 and B-02.
2. **The stated purpose is to take above-cap increases out of the lessor's unilateral hands.** The
   speech says a higher increase "will be made transparently, based on evidence and with regard to
   fairness. It is not made unilaterally or behind closed doors." B-01's exception lets it be made
   by a clause in the lessor's standard lease.
3. **Transitional intent.** The EM says of both s.106 and s.107: "If proceedings relating to such
   a notice are pending, they are taken to be dismissed." That covers all proceedings, not only a
   tenant's. The speech says: "to ensure that nobody is disadvantaged by timing". This confirms
   B-09 is a drafting error, not a policy choice.
4. **Social housing.** The speech says the Bill "still requires that terminations occur on
   specified grounds and with appropriate notice". Neither document gives a reason for removing
   s.70A(2) from social housing (B-07) or addresses fixed terms under s.71BA (B-08).

Nothing in either document settles **F-1** (the effect of a non-compliant notice), **F-2** (fixed
term or periodic after the expiry day) or **B-03** (income-based rent). Neither mentions s.31A,
s.76C or what happens to a notice that breaches s.31AA.

Context from the speech: the member refers to government announcements that "the end of no-fault
evictions" is coming, and says "we do not know exactly what approach will be taken". A government
Bill on the same sections may overtake this one. Any finding here about ss.64, 70A and 72 should be
re-checked against that Bill if it appears.

---

## B-01: The cap never reaches fixed-term tenancies, and any agreement term switches it off

- **Provisions:** proposed s.31AA(2)(a); s.30(2)(a); s.82(1).
- **Demonstrated:** `rent-cap-bill-rent.l4`, fixtures *fixed term, 25 percent written into the
  lease* and *periodic, 10 percent annual clause*.

Under s.30(2)(a), a lessor can raise rent during a fixed term **only if** "the amount of the
increase, or the method of calculating the amount of the increase, is set out in the agreement".
Proposed s.31AA(2)(a) lifts the cap in exactly that case. So every lawful mid-term increase under
a fixed-term lease meets the exception, and the cap never applies to one. The encoding allows a
25% increase that is written into the lease, even though the limit works out at $33 on $600 a
week.

The same exception works for periodic agreements: a standard clause such as "rent increases by
10% each year" takes the tenancy outside the cap. s.82 does not rescue the position. It voids
terms inconsistent with the Act "except as provided under this Act", and s.31AA(2)(a) *is*
provision under the Act.

**Against the model.** ACT s.64B(1)(a) exempts only "a fixed term agreement to which section 64A
applies". Under ACT s.64A(1) that is a fixed-term agreement entered into before A2024-29 s.76
commenced, on 10 December 2024. In the ACT, then, the exception is a closing transitional
provision for leases already signed. In transplanting it, the WA Bill dropped the qualifier and
made it permanent and general.

This is demonstrated in the §§ *ACT comparison -- illustrations* of `rent-cap-bill-rent.l4`: for
a lease signed after the reform, the ACT exception does not apply and the WA exception does.

**Against the stated intent.** See item 2 above: the speech presents court approval as the route
for any above-cap increase.

**Repair options:**
- Follow the ACT: confine (a) to a fixed-term agreement entered into before commencement day,
  which s.105 would then complement.
- Or remove (a) altogether.

## B-02: Rent raised through a new agreement is not capped

- **Provisions:** proposed s.31AA(2) ("increase the rent … under section 30 or 31A"); s.31B.
- **Demonstrated:** fixture *renewal at 20 percent more*.

Renewing with the same tenant at a higher rent creates a new residential tenancy agreement. That
is not an increase under s.30 or s.31A, so s.31AA does not govern it. s.31B treats a renewal as a
continuation only "for the purposes of working out" when rent was last increased, so it does not
bring the new rent within s.31AA either.

Clause 7 limits the damage, because a tenant who refuses the renewal now stays on as a periodic
tenant at the old rent. The cap still falls away wherever a tenant agrees to a new lease, and
s.31AA(2)(b)'s requirement that the tenant's agreement be written and come after a notice does
not apply to a renewal.

The cap also does not follow the premises between tenants. That is a policy choice, not a
defect.

**Against the model.** ACT s.64AE defines "rental rate increase" to include an increase "under a
residential tenancy agreement (including an existing consecutive tenancy agreement)", and one that
"will take effect under a proposed consecutive tenancy agreement". ACT s.64AAA(2) carries the
12-month clock across renewals. The WA Bill has neither provision. The speech's aim is to limit
increases "during a tenancy", which a same-tenant renewal is in substance.

This is demonstrated in the §§ *ACT comparison -- illustrations*.

**Repair:** follow ACT s.64AE, using WA s.31B(2) as the definition of a continuing agreement.

## B-03: The cap is unworkable for income-based rent (s.31A)

- **Provisions:** proposed s.31AA(1) ("initial CPI" (b)), (2) and (3)(a); s.31A.
- **Demonstrated:** fixture *income-based method change*.

A s.31A notice does not increase rent. It changes "the method by which the rent is calculated by
reference to [the tenant's] income". s.31AA treats that notice as an increase of a stated amount.
Under s.31AA(3)(a) the notice must state "the amount of the proposed increase", and under (3)(b)
whether that amount exceeds the limit. Where the rent depends on income that is not yet known,
neither statement can truthfully be made.

On reading A of F-1, no s.31A change can then take effect at all. Most income-based rents are
social housing rents.

**Repair:** exclude s.31A, or define the increase for s.31A as the change in rent that would
result on the tenant's income at the date of the notice.

## B-04: CPI reference-base changes are not dealt with

- **Provisions:** proposed s.31AA(1), "CPI" and the L formula.
- **Demonstrated:** fixture *CPI re-referenced between notices*.

The formula divides one published index number by another, taken before two dates that may be
years apart. The ABS periodically re-references its index series (the current base is
2011–12 = 100) and revises published numbers. If that happens between the two dates, the numbers
are on different scales. In the fixture, rents actually rose 5%, but the re-referenced current
figure (105) is below the old-base initial figure (200). It is therefore floored to 200, and the
limit becomes $0.

**Repair:** use the index numbers for both periods as they appear in the latest publication, or
the percentage change the ABS publishes.

## B-05: The court can order possession before the statutory notice period has run

- **Provisions:** s.64(3)–(4)(c), unamended; proposed s.64(2A); proposed s.71BA(2) and (4)(c).
- **Demonstrated:** `rent-cap-bill-termination.l4`, the §§ *Section 64(4)(c) unamended* rules
  and the s.71BA illustration.

The Bill lengthens notice periods: 3 months for renovation (s.64(2A)(a)), 6 months for another
lawful use ((2A)(b)), and 90 days for s.71BA. It keeps s.64(4)(c), and copies it into
s.71BA(4)(c). That provision lets the court, **on the tenant's own application to extend**, order
possession from "a day not less than 60 days after the day on which the notice … was received".
The 60 days matched the old s.64(2), and it now undercuts every new period except the plain
60-day one.

A tenant who applies to extend a 6-month notice can therefore be ordered out about four months
early. The encoding compares against the shortest calendar length of 3 and 6 months (89 and 181
days), so the result holds in any year.

**Repair:** in s.64(4)(c)(i) and s.71BA(4)(c)(i), replace "60 days" with "the period of notice
required for the ground".

## B-06: The s.31AB(8) offence outlives the order it enforces

- **Provisions:** proposed s.31AB(5), (6), (7) and (8); compare s.32(5) and (7).
- **Demonstrated:** fixture *demand from a new tenant*.

Under s.31AB(5), the court may order that the rent payable "under the residential tenancy
agreement" not exceed an amount. Subsection (6) keeps that order in force for a fixed year.
Subsection (8), however, makes it an offence to demand rent "from the residential premises" above
that amount.

If the tenant leaves, the order no longer limits any agreement, but charging a new tenant more
remains an offence until the year is up. Its sibling provision, s.32(5), ends the order "on the
expiration of the tenancy of the person who applied".

A related point: under s.31AB(7) only the tenant may apply to vary the order, whereas under s.32(6)
it is the lessor.

**Repair:** have the order end at the earlier of one year and the end of the tenancy, and align
(8) with (5).

## B-14: The EM and the Bill disagree on how long a s.31AB order lasts

- **Provisions:** proposed s.31AB(6); EM, notes on clause 4.
- **Shown by:** a direct comparison of the two texts. This is not an assertion, because the EM is
  not encoded. `rent-cap-bill-rent.l4` follows the Bill: a fixed 365 days, in
  `the section 31AB(5) order is in effect`. The EM says: "The court may make an order specifying
  the maximum rent payable for a period of up to 1 year."

The Bill reads: "An order made under subsection (5) has effect for the period of 1 year". The
court has no discretion over duration. On the EM's account it would have one, as it does under
s.32(5) ("such period not exceeding 6 months as is fixed by the court").

Whichever the drafter meant, B-06 remains: a fixed year that survives the tenancy is the cause of
it.

**Repair:** "has effect for the period, not exceeding 1 year, specified in the order, or until
the tenancy ends, whichever is earlier."

## B-07: Social housing tenants lose the protection of s.70A

- **Provisions:** amended s.70A(2) ("other than a social housing tenancy agreement"); s.60(1)(b);
  s.76C.
- **Demonstrated:** fixture *social housing fixed term, tenant gives end-of-term notice*.

The current s.70A(2) stops *every* fixed term ending on its expiry day unless someone gives
notice. The replacement text excludes social housing agreements, so for those nothing in s.70A
prevents the term ending on the expiry day any more. Because s.70A(1) defines "notice" as one
"referred to in subsection (2)", a social housing tenant's end-of-term notice is no longer a s.70A
notice either, and s.60(1)(b) is closed to them.

The Bill carves social housing out of s.64 and gives it s.71BA instead. For s.70A, though, the
carve-out removes a protection and puts nothing in its place.

**Repair:** keep the current wording of s.70A(2) for social housing agreements, or drop the
carve-out.

## B-08: s.71BA does not say whether it reaches a fixed term during its currency

- **Provisions:** proposed s.71BA; compare s.63(4), s.64(5) (current), s.71G(1)(a) and s.71J(5).
- **Demonstrated:** fixture *social housing sale, mid fixed term*. The encoding follows the text,
  so the notice is effectual.

Wherever the Act lets a lessor's notice interact with a fixed term, it says so expressly, one way
or the other. s.71BA is silent. If it applies, a social housing lessor can end a fixed term
mid-term to sell, on 90 days' notice, which private lessors cannot do. If it does not apply, the
Bill should say so.

## B-09: The transitional provisions miss the lessor's pending applications, and s.107 relies on an application that cannot exist

- **Provisions:** proposed ss.106 and 107; s.72(1) (current and amended); s.71(1).
- **Demonstrated:** fixtures *lessor's section 72 application pending*, *lessor's section 71
  application pending* and *tenant's section 64(3) application pending*.

s.107(2)(b), (4)(b) and (5)(b) refer to "an application by the tenant under previous section
72(1)". s.72(1) has only ever allowed **the lessor** to apply. As a result:

- s.107(4)–(5) can never operate;
- (2)(b) is always true, so every lessor's s.70A notice becomes ineffectual.

The application that actually exists, the lessor's s.72 application for possession, is not
dealt with. The same gap appears in s.106: the tenant's s.64(3) application is dismissed, but the
lessor's s.71 application on the same notice is not mentioned.

This leaves proceedings on foot whose notice is now void. It also leaves open what happens to a
possession order already made but not yet executed (F-3).

**Intent confirmed.** The EM says that for both sections "If proceedings relating to such a notice
are pending, they are taken to be dismissed". That describes all proceedings. The text reaches
only a tenant's, and in s.107 only one that cannot exist.

**Repair:** in s.107, read "an application by the lessor under previous section 72(1)". Deal
expressly with a lessor's s.71 or s.72 application pending on commencement day, and with orders
already made.

## B-10: s.65 is not extended to s.31AB

- **Provisions:** s.65(1); proposed s.31AB.
- **Demonstrated:** fixture *sale notice while a section 31AB order is in force*.

While s.32 excessive-rent proceedings or orders are on foot, s.65 makes a s.64 notice
ineffectual, and makes other lessor notices subject to court authorisation. s.31AB proceedings
and orders get no equivalent protection.

A lessor refused an above-cap increase can give a 60-day "sell" notice straight away. The tenant
is left with a retaliatory-action application under s.26B, or the court testing the ground under
s.71(2)(b) or refusing relief under s.71(3)(b)(i).

## B-11: No consequence for a notice that breaches s.31AA (fork F-1)

- **Provisions:** proposed s.31AA(2) ("cannot increase") and (3) ("must state"); s.30(3); s.27;
  s.83.
- **Demonstrated:** §§ *Interaction with section 30 (fork F-1)*, under reading A.

The Bill does not amend s.30(3). That subsection makes any notice "given in accordance with this
section" (that is, s.30) vary the agreement. s.31AA is a different section. There is no offence
for demanding rent above the cap. Compare s.31AB(8) and s.32(7), which each carry a $5,000 fine.

**Repair:** make s.30(3) and s.31A subject to s.31AA, and state what happens to the notice.

## B-12: A commencement limb that can no longer operate

- **Provision:** cl.2(b)(i). **Demonstrated:** the §§ *Clause 2 -- illustrations* assertions.

The Bill has not passed either House, so assent cannot now come before 1 July 2026. The rest of
the Act will commence on the day after assent.

## B-13: Clerical

- s.64(2A)(a) and (b) say "subsection 1(e)" and "subsection 1(f)". They should read "(1)(e)" and
  "(1)(f)".
- s.64(1)(c) reads "that another person … **to** live in the premises", which is ungrammatical.
  Compare (b), "that the lessor's immediate relative live".
- s.64(1)(b): "immediate relative" is not defined in the Act or the Bill.
- s.64(1) says "other than a social housing tenancy", but the defined term is "social housing
  tenancy agreement" (s.3, s.71A). The phrase also duplicates new s.64(5).
- s.71BA(4)(c)(ii): "a day within 7 days after **which** the day on which the order was made".
  Compare s.64(4)(c)(ii).

---

## Forks

### F-1: Effect of a rent-increase notice that breaches s.31AA(2) or (3)

- **Reading A** (encoded): the notice is ineffective in whole. "Cannot increase" and "must state"
  are treated as conditions on s.30(3).
- **Reading B:** the notice takes effect up to the increase limit.
- **Reading C:** under s.30(3) the notice still varies the agreement, and the tenant's remedies
  are s.26B, s.32 or s.83.

The choice decides B-03 (reading A makes income-based rent changes impossible) and whether B-11
is a gap or a design choice.

The EM ("A lessor must not increase rent above the increase limit unless …") and the speech point
towards prohibition, but neither says what happens to the notice. The ACT model uses "must not be
more than" (s.64B(1)) and leaves the same question open. **Not resolved.**

### F-2: A fixed term the tenant has not ended: fixed term or periodic?

Amended s.70A(2) says the term "does not end on the expiry day". s.76C(2) says the agreement
"continues as a periodic tenancy after the expiry day". This tension was already in the Act, but
the Bill makes it decisive. On the fixed-term reading, s.63(4) and amended s.64(1) (periodic
tenancies only) leave the lessor **no** ground-based route at all, only breach or a court order
under ss.73–75.

Both readings are encoded as a parameter of `after the expiry day the lessor can give a notice
under amended section 64`.

The EM and the speech both say only that the agreement "does not … terminate at the end of a fixed
term unless the tenant gives notice". The speech presents s.64's grounds as the list of "genuine
reasons why a lessor might have to end a tenancy", which assumes the grounds reach former fixed
terms. That supports the periodic reading. **Leaning towards the periodic reading, not
resolved.**

### F-3: Pre-commencement notices and applications

It is unclear whether a notice is "in effect" (ss.106(1)(a) and 107(2)(a)) once its possession
day has passed and the tenant is holding over. It is also unclear what becomes of a possession
order already made on a notice that becomes ineffectual. s.71(2)(a) requires the notice to have
been "given in accordance with this Act" at the time it was given, so an order already made
arguably stands.

---

## Checked and found sound

- **V-01**, s.105: increases noticed before commencement are left alone. Demonstrated by
  *notice given before commencement*.
- **V-02**, numbering: the Act's Part 7 ends at s.103, so the new Division 4 (ss.104–107) follows
  on. There are no collisions.
- **V-03**, s.60(1)(b)(ii) still reads "upon application by the lessor … under section 72". That
  stays consistent with amended s.72(1), which is still the lessor's application.
- **V-04**, s.70A(1): deleting subsections (6) and (7) and the words "and has the meaning affected
  by subsection (6)" is consistent. Both subsections only dealt with a lessor's notice.
- **V-05**, s.64(1)(d) "sell" (60 days, with evidence) and s.63 "contract of sale" (30 days) sit
  together coherently. The stronger fact gets the shorter period.
- **V-06**, s.64(2) evidence: the Bill gives no sanction of its own, but s.71(2)(a) makes it
  effective, because the court orders possession only on a notice that "complied with … this
  Act".
- **V-07**, the "current CPI" floor keeps the limit from going negative. Demonstrated by *CPI
  fell*.
- **V-08**, CPI series: the ABS still publishes quarterly CPI, now the average of three monthly
  CPIs, after the move to a monthly CPI in November 2025. It has committed to do so for at least 18
  months. The definition therefore still points at a published series, but it depends on the ABS
  continuing it.

## In the scheme console

The Act as amended by the Bill is modelled as scheme `rta-rent-cap` in
`tools/scheme-console/schemes.js`. The model assumes the Bill commences on 1 January 2027 (assent
on 31 December 2026, cl.2(b)(ii)). That is day 92 on the console's clock, so the transitional
provisions can be run on the clock rather than asserted.

A console result is **demonstrated on stated facts, not by an `#ASSERT`**. It corroborates the
assertions above; it does not replace them. `node tools/scheme-console/check.js` reports no
problems. The one conferred fact is `tenancy.approvedAboveCap`, and it traces to the court's
approval.

| finding | console scenario | mode |
|---|---|---|
| B-01 | 25% written into a fixed-term lease | scenario |
| B-02 | Renewal with the same tenant at 20% more | **nature** |
| B-03 | An income-based social housing rent | scenario |
| B-04 | The ABS re-references the index | scenario |
| B-05 | Six months' notice, cut to 60 days by the tenant's own application; Social housing: 90 days under s.71BA, 60 by order | scenario |
| B-06 | Court caps the rent; the next tenant pays more | **nature** |
| B-07 | A social housing tenant tries to end the fixed term | scenario |
| B-08 | Social housing: 90 days under s.71BA, 60 by order | scenario |
| B-09 | Old s.70A notice / old no-grounds notice, lessor's case pending at commencement | scenario |
| B-10 | A 'sell' notice while the rent order is in force | scenario |
| F-1 | A 10% increase the tenant never agrees to (reading A) | scenario |
| F-2 | A fixed term runs out and nobody gives notice (s.76C reading) | scenario |
| V-01, V-06 | A rent notice given before commencement; … and where the tenant applied under s.64(3) instead | scenario |

B-02 and B-06 arise in Nature mode (called simulation mode when this was written; "Simulation"
now means a run the console generates itself), where the new agreement is created on the clock rather
than asserted. That is the stronger evidence, because it shows that a state the rules can
actually reach produces the finding.

In the other scenarios the cast's state is authored, and the Bill's rules then act on it as the
clock runs. For example, in B-05 the 60-day possession day comes from s.64(4)(c) and the
calendar, not from anything asserted. B-09 is reached by giving the old notices before day 92 and
letting commencement arrive, not by asserting that a notice is pending.

Modelling the Bill turned up **no new finding**. The one thing learned from the console is that
a fixed term expiring anywhere in the cast brings in B-07 or F-2, depending on the tenancy.
Every expiry of a fixed term after commencement engages one of the two.

## Observations (not reproduced by machine)

- The new s.64 grounds carry no offence for a false ground, unlike s.63(3) ($10,000), and there
  is no bar on re-letting after the tenant leaves. A ground is tested only if the tenant stays on
  and the lessor applies under s.71(2)(b).
- Amended s.72(3)(b), the refusal where the term was under 90 days, now applies only after a
  *tenant's* notice. Its limbs are about the lessor's purposes, so it is now effectively dead
  text.
- s.31AB(5): it is unclear whether, having refused the amount requested, the court may approve a
  smaller increase that is still above the limit.
- Timing: s.31AA(3)(c) implies notice first, then a court application. Nothing says what happens
  if approval comes after the day the s.30 notice set for the increase. The ACT model avoids this
  by requiring "the ACAT's **prior** approval" (s.64B(1)(c), (2)(d)). The WA Bill dropped the word
  "prior" from both places.
- The EM says a social housing lessor "may terminate … only on specified grounds" under s.71BA.
  That overstates the Bill: ss.62, 71C, 71H and 75A remain available (s.71B). "Only" is accurate
  only in the sense that s.71BA replaces no-grounds termination.
- The Bill copies ACT s.64B(2)'s notice content, but applies it to every notice, where ACT applies
  it "for subsection (1)(b)" (tenant agreement). This is a reasonable choice and is not counted as
  a finding.
- B-04 (CPI re-referencing) was not checked against the ACT's regulation, which prescribes the
  ACT formula. If the ACT has the same exposure, it is at least a known one.
