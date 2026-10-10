# Inheritance (Family Provision) Act 1966 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/IFPA1966.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021" and comes into operation on
31 December 2021. The last amendment in its Legislative History is Act 40 of 2019
(commencement 2 January 2021). The arrangement of sections at the top of the `.txt`
is one line out of step with the body; the body's numbering is followed.

**Checks:** one case file, 55 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Chosen for its **everyday-life relevance** (Tier 1 of the remaining Acts), not by
citation count. It is the only route this Act offers a spouse or child left out of a
will, or left short by intestacy, to ask a court for maintenance from the estate.

The Act is six sections long, so the whole of it is covered: ss 1 to 6. The court's
discretionary weighing (s 3(5) to (8)), the effect of an order on the will or
intestacy (s 5(1)) and the filing of orders (s 5(3)) are quoted in comments but not
decided. The Intestate Succession Act, the Probate and Administration Act, CPF
nominations and Muslim law were not read.

## What the Act turns out to say

### 1. An adult daughter qualifies only if she has never married; an adult son, never (unless disabled)

s 3(1) lists the dependants: a spouse; "a daughter who has not been married or who is,
by reason of some mental or physical disability, incapable of maintaining herself";
"an infant son"; and a son disabled in the same way. So an unmarried daughter of 45
may apply, but a divorced or widowed daughter of 40 may not unless she is disabled,
and an able son of 25 may not at all. "Infant" is not defined; the encoding reads it
as under 21 because s 3(2)(c) ends an infant son's payments at 21 (an inference).
Asserted.

### 2. Parents, siblings, former spouses and stepchildren are outside the Act

No one else is in the s 3(1) list. s 2 extends "son" and "daughter" to children
adopted by order (in Singapore, Malaysia or Brunei Darussalam) and to a child
"en ventre sa mere" at the death, but says nothing of stepchildren. The encoding
treats a dependent parent, a disabled sibling, a divorced wife and an unadopted
stepchild as not dependants (an inference from the closed list). Asserted.

### 3. A spouse taking two-thirds of the income shuts everyone out, unless there is a child of another relationship

The proviso to s 3(1): "no application shall be made ... by or on behalf of any person"
where the surviving spouse is entitled to "not less than two-thirds of the income of
the net estate" and the only other dependants are "a child or children of the
surviving spouse". A spouse on 70% with only their own children bars every
application; the same 70% with a dependant child of an earlier marriage does not.
Asserted.

### 4. Six months from the first grant, extendable only on three grounds

s 4(1): the application must be made within 6 months of representation "first taken
out". s 4(2) lets the court extend only if the limit "would operate unfairly" because
of a later-discovered will or codicil, an undetermined question about an interest in
the estate, or "some other circumstances affecting the administration or distribution
of the estate". s 4(4): a grant limited to trust property does not start the clock
unless a grant for the remainder was made before or with it. s 4(3) protects personal
representatives who distribute after six months from liability for not foreseeing an
extension (recorded, not asserted). Asserted (except s 4(3)).

### 5. Periodical payments, capped at the estate's income; a lump sum only up to $50,000

s 3(2): provision is "by way of periodical payments". s 3(3): neither one dependant's
annual rate nor the aggregate for all may exceed the "annual income of the net
estate". s 3(4): only where the net estate "does not exceed $50,000" may the court
order a lump sum. s 5(2): no more of the estate may be set aside than will produce
the provision by its income ($12,000 a year at 4% is $300,000). Asserted.

### 6. Payments end no later than remarriage, marriage, 21 or recovery, and always on death

s 3(2): a spouse's on remarriage; a daughter's on "her marriage or the cesser of her
disability, whichever is the later"; an infant son's at 21; a disabled son's when the
disability ceases; and anyone's on earlier death. The encoding reads "whichever is
the later" as requiring both events for an unmarried disabled daughter (an
inference). For a son who is both an infant and disabled the Act does not say which
rule governs; no case asserts it. Asserted (except that case).

### 7. After the period, an order can still be varied, but only over income already applied to maintenance

s 6(1): a late application may vary an order for non-disclosure of a material fact or
a substantial change in circumstances, or add provision for another dependant, "but
only as respects property the income of which is at that date applicable for the
maintenance of a dependant". s 6(2) lets a dependant, the trustees, or a beneficiary
apply under (1)(a). The encoding treats a creditor of the estate as not entitled
(inference from the list). Asserted.

## What would need doing before this is worth anything

- No case law was read: how "reasonable provision", "maintenance" and "infant" have
  been interpreted, and how s 3(6) and (7) are weighed, decide most real claims.
- The interaction with the Intestate Succession Act (what intestacy actually gives a
  spouse and children) and with assets outside the will, such as CPF nominations, was
  not read; the s 2 "net estate" is only the property disposable "by his will".
- The six-month boundary and the infant-and-disabled son are left unasserted.
- No independent test pass, no human gate.
