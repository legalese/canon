# Choice of Court Agreements Act 2016 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill conventions and nothing else. No pipeline, no coverage table, no independent
test pass, no human gate.

**Edition:** 2020 Revised Edition, which "incorporates all amendments up to and
including 1 December 2021", as deposited at
`../../registers/source-bundle/CCAA2016.txt` (SSO version current as at 1 October
2026). The latest amendment annotated is Act 40 of 2019 (Supreme Court of
Judicature (Amendment) Act 2019, in force 2 January 2021).

**Checks:** one case file, 54 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0044**: tier 2 of the remaining Singapore Acts, ordered by
everyday-life relevance. It asks what the Act decides for a person or business it
applies to; no scenario has asked a sharper question yet. The Act is short (24
sections) and matters to any business that signs a cross-border contract with a
clause choosing a court. This row takes what the clause is (s 3), when the Act
applies (ss 4, 6, 8, 9, 10, 24), what a Singapore court must do with it (ss 11, 12),
and recognition and enforcement of foreign judgments and judicial settlements
(ss 2(1), 13 to 16, 20), plus the High Court and SICC designation rule (s 2(2), (3))
and the independence of the clause (s 5). Not encoded: regulations (none retrieved,
so every "prescribed" ground is absent), s 2(4), s 11(3) to (5), s 15(3), ss 17 to 19
(beyond a comment), ss 21 to 23, and the list of Contracting States, which is taken
as a fact.

## What the Act turns out to say

### 1. A Singapore court must send the case abroad, "despite any other written law or rule of law"

Where the exclusive clause chooses a foreign court, a Singapore court "must stay or
dismiss" the case (s 12(1)) unless one of five narrow exceptions is shown: the clause
is void under the chosen State's law, a party lacked capacity under Singapore law,
giving effect to it would be a manifest injustice or manifestly contrary to public
policy, it cannot reasonably be performed for exceptional reasons, or the chosen
court has declined the case. The mirror rule in s 11(2): a chosen Singapore court
"cannot decline to exercise jurisdiction on the ground that the dispute should be
decided in a court of another State". Asserted.

### 2. Silence makes a clause exclusive

A written clause choosing the courts of one Contracting State is "deemed" exclusive
"unless the parties to the agreement expressly provide otherwise" (s 3(2)). A clause
that says nothing about exclusivity therefore brings in the whole Act; a clause the
parties expressly make non-exclusive falls outside it (left to regulations under
s 22(2), none retrieved). An oral clause is not covered: s 3 requires writing or an
accessible record. Asserted.

### 3. Consumers and employees are out; so are injuries, tenancies and patents

s 9(1) excludes any agreement where a party "acts primarily in the capacity of a
consumer", and employment contracts. s 9(2) excludes family, succession, insolvency,
carriage of passengers and goods, competition, personal injury, non-contractual
property damage, tenancies, and the validity and infringement of IP "(other than
copyright and related rights)". But a patent claim for breach of a licence between
the parties stays in (s 9(2)(n)), copyright validity stays in, and an excluded matter
raised only "as a preliminary question or defence" does not take the case out
(s 9(5)) -- except that s 9(5) reaches only s 9(2) matters, so a consumer contract is
out regardless. Asserted.

### 4. Must refuse, may refuse, and the court cannot look at the merits

The General Division "must not review the merits" (s 13(3)) and, if the
requirements are met, "must recognise, or recognise and enforce" (s 13(4)). It MUST
refuse for late notice to the defendant (unless the origin law allowed a challenge
and the defendant defended without making one), procedural fraud, or manifest
incompatibility with public policy (s 14). It MAY refuse for a void clause (unless
the chosen court upheld it), lack of capacity, defective service, inconsistent
judgments, a pending appeal (s 15) or damages beyond actual loss (s 16). A judgment
with effect but not enforceable at origin is recognised but not enforced (s 13(2)).
The encoding reports s 16 as "may refuse" though the text says "to the extent that".
Asserted.

### 5. A consent order is a judgment, not a settlement

"judgment" includes "a consent order, a consent judgment"; "judicial settlement"
expressly "does not include a consent order or consent judgment" (s 2(1)). So the
same compromise goes down different routes depending on whether the foreign court
made an order or merely recorded a contract. Settlements are only ever "enforced"
(s 20), on the same must/may grounds as judgments (s 20(3), (4)). Asserted.

### 6. The 1 October 2016 cut-off applies only to Singapore clauses

s 24(1) excludes agreements choosing a Singapore court concluded before 1 October
2016; s 24(2) excludes agreements choosing another Contracting State's court only if
concluded before the Convention entered into force in that State. A 2015 clause
choosing a court of a State already bound by the Convention is therefore within the
Act. Asserted.

### 7. "High Court" means the SICC too

A clause naming "the High Court" or its General Division is read as including the
Singapore International Commercial Court "unless a contrary intention appears"
(s 2(2), (3)). Asserted.

## What would need doing before this is worth anything

- Retrieve the regulations under s 22 (prescribed grounds, non-exclusive clauses,
  excluded matters) and the Rules of Court under s 23.
- Model ss 17 to 19 (preliminary-question rulings, insurance judgments, severable
  parts) and the "to the extent" operation of s 16.
- Supply the list of Contracting States and their Convention dates (an input here).
- No case law on s 12 or ss 14 to 16 was searched.
