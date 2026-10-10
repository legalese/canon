# High Court (Admiralty Jurisdiction) Act 1961 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, which says it incorporates
amendments up to 1 December 2021; the latest amendment annotated in the text is Act 25
of 2021, with effect from 1 April 2022 (s 5(2), (3)).

**Checks:** one case file, 49 assertions satisfied, 0 errors.

## Why this Act, and why scoped

**5 of the 527 Singapore Acts** deposited here cite it. This row takes the decisions a
shipping practitioner meets: whether a claim is an admiralty claim (s 3(1)), whether
the ship, a sister ship or an aircraft can be proceeded against in rem (s 4(2)-(6),
(8)), whether a collision claim can be brought in personam (s 5), the foreign-ship
wages saving (s 6), the Rhine Convention exclusion (s 7) and the Government saving
(s 8(2)). Not encoded: co-owners' accounts and sale (s 3(2)), the content of salvage
claims (s 3(3), (3A)), s 3(5), title to sale proceeds (s 4(7)), the Rules of Court
direction (s 5(6)), the receiver of wreck saving (s 8(1)), and the carve-out in
s 3(1)(i) for District Court salvage under section 168 of the Merchant Shipping Act
1995.

## What the Act turns out to say

### 1. A demise charter lets you arrest the ship, but not a sister ship

Under s 4(4)(c) the ship itself can be arrested if, when the action is brought, the
relevant person is the beneficial owner of all its shares "or the charterer of that ship
under a charter by demise". Under s 4(4)(d) another ship can be arrested only if the
relevant person is "the beneficial owner as respects all the shares in it". A demise
charterer's other chartered ships are out of reach. Asserted.

### 2. Once the owner has sold the ship, only a lien or a proprietary claim follows it

s 4(4) looks at who owns or demise-charters the ship "at the time when the action is
brought". A bunker supplier whose debtor has sold the ship has no action in rem against
it; a collision victim with a maritime lien still does (s 4(3)), and so does a mortgagee
(s 4(2)). Asserted.

### 3. A crew claim goes in rem only if it touches wages, even with a lien

s 4(6) operates "Notwithstanding anything in subsections (1) to (5)": a s 3(1)(n) claim
cannot be brought in rem "unless the claim relates wholly or partly to wages". The
encoding applies this even where a maritime lien is pleaded. Asserted.

### 4. The jurisdiction ignores flag, registration and place

s 3(4) applies the heads to all ships "whether of Singapore or not and whether
registered or not", to claims "wheresoever arising", and to mortgages "created under
foreign law". s 4(8) assumes the liable person resides in Singapore when testing
liability in personam for in rem purposes. Asserted for a foreign unregistered ship.

### 5. Collision claims in personam need a Singapore connection, and foreign suits must end first

s 5 confines actions in personam for collisions to defendants resident or doing business
in Singapore, causes of action arising in inland waters or the port, or incidents
already litigated here (s 5(1)); and none may proceed while the claimant's earlier
foreign proceedings against the same defendant are on foot (s 5(2)). Submission to the
jurisdiction disapplies both (s 5(4)), and counterclaims on the same incident are
outside them (s 5(3)). Other admiralty claims face no such limit (s 4(1)). Asserted.

### 6. Government ships, Government claims and Rhine Convention claims are out

s 8(2) authorises no proceedings in rem against the Government, nor the arrest of a ship
beneficially vested in or demised to it, or a Government aircraft. s 7 removes claims
the Minister certifies under the Rhine Navigation Convention, and proceedings on them
"shall be set aside". Asserted.

### 7. Section 6 is a saving, not a rule

s 6 only says the Act does not limit the court's jurisdiction "to refuse to entertain an
action for wages" by the crew of a ship "not being a Singapore ship". The encoding says
where the saving operates; it does not infer that no discretion exists for Singapore
ships. Asserted.

## What would need doing before this is worth anything

- None of the cross-referenced Acts (Merchant Shipping Act 1995, Air Navigation Act
  1966, Maritime and Port Authority of Singapore Act 1996) was read; "maritime lien",
  "Singapore ship", the port limits and the collision regulations are taken as given
  facts.
- Which claims carry a maritime lien is not stated in this Act, so the encoding asks
  the user rather than deciding.
- The s 3(1) heads are encoded as a list of example claims, one per head, not as tests
  of the head's wording; borderline characterisation is not modelled.
- No case law on beneficial ownership, "in connection with a ship" or "relevant person"
  was searched.
