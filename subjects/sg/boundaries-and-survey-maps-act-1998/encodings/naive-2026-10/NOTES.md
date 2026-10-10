# Boundaries and Survey Maps Act 1998 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, incorporating amendments up
to 1 December 2021, with Act 25 of 2024 (wef 1 October 2025) shown in the s 2
definitions. Deposited at `../../registers/source-bundle/BSMA1998.txt`.

**Checks:** one case file, 55 assertions satisfied, 0 errors.

## Why this Act, and why scoped

**6 of the 527 Singapore Acts** deposited here cite it. This row takes what a
landowner, a registered surveyor or a court meets: when a cadastral survey is complete
and what a certified plan proves (s 4), the notice to clear a boundary line (s 9),
boundary marks and the offence of obliterating one (ss 10, 11), surveyors' entry on
land (s 12), approval of survey plans and lodgment of assurance plans (s 15),
correction of survey errors (s 16), correction of the map (s 17), what is conclusive
evidence (ss 8, 18) and the continuing offence of non-compliance (s 20). The Chief
Surveyor's appointment, general powers and duties (ss 3, 5, 6), the coordinated
cadastre programme (s 7), inspection and deposit of records (ss 13, 14), the s 19
self-help power, rules and fees (ss 21, 22) and Mukim boundaries (s 17(6)) are not
encoded.

## What the Act turns out to say

### 1. The old map binds the courts more firmly than a new survey plan

s 18(1): every map published under the repealed Act is "conclusive evidence in all
courts of the boundaries", subject only to s 17 orders, until superseded by a s 7(f)
declaration. A certified plan, by contrast, is only "prima facie evidence" of
boundaries, marks, area and lot number (s 4(2)); so is a certified copy of a deposited
plan (s 14(4)). A map generated from the coordinated cadastre becomes conclusive only
"upon a declaration under section 7(f)" — which s 7(f) allows only once every parcel in
Singapore is within the coordinated cadastre. Before then, on the text, it has no
conclusive status (an inference from s 18(2) saying nothing else). Bench marks are
conclusive of height (s 8). Asserted.

### 2. Damaging a survey mark can cost three times the repair, on top of the fine

s 11(1): wilfully obliterating, removing or injuring, without reasonable excuse, a mark
made by or under the Chief Surveyor carries a fine up to $1,000, and a Magistrate's Court
may further require "3 times the cost of replacing and repairing" the mark and of any
survey made necessary. If the offender cannot be found, the Chief Surveyor may put the
cost on "the owners of the adjacent lands" (s 11(3)). The offence needs wilfulness and
a mark made under the Chief Surveyor; an accidental knock, or a private marker, is
outside it. Asserted. Separately, every owner "must preserve the boundary marks"
(s 10(1)), but no penalty is attached to that duty in s 10 itself. Not asserted.

### 3. The fine for ignoring an order only runs after conviction

s 20: wilful refusal, or neglect without reasonable excuse, to comply with an order or
notice under the Act is an offence, punishable by up to $100 "for every day or part of
every day during which the refusal or neglect continues after conviction". On the text
there is no fixed fine for the default itself; zero days after conviction gives a
maximum of $0. Note the reasonable-excuse qualifier attaches only to neglect, not to
wilful refusal. Asserted.

### 4. Surveyors may enter land only by daylight, and must warn the occupier unless it is a road

s 12: entry needs the Chief Surveyor's authority, a registered surveyor "who has in
force a practising certificate" (or the surveyor's assistant), and "any reasonable time
during the hours of daylight". Reasonable notice to the occupier is required "where
practicable" for land "that is not a road"; identity and authority must be produced on
first entry if practicable. s 12(4): the authority does not exempt the surveyor from
liability for damage. Asserted (except s 12(4)).

### 5. An approved plan does not shift responsibility from the surveyor

s 15(5): "Despite that a survey plan has been approved by the Chief Surveyor", the
signing surveyor must ensure it is correct. The Chief Surveyor may refuse approval for
missing subdivision permission, unpaid fees, or an unresolved encroachment by the owner
on adjoining land in a survey for a new State title, amalgamation or subdivision
(s 15(3), (6)). An assurance plan may be lodged only if signed, approved and bearing a
caution that its boundaries are "inconclusive" (s 15(2)), and the s 16 correction
directions do not apply to it (s 16(5)). Asserted.

### 6. Neighbours cannot move a boundary on the map by agreement alone

s 17(2)(d): the map may be altered on agreement of conterminous owners only "upon a deed
or instrument being presented" at the Registry. A survey error goes to notice and a
one-month objection window: no objection, the Chief Surveyor "must" order correction;
any objection, an inquiry (s 17(3), (4)). Asserted.

## What would need doing before this is worth anything

- The s 4(1)(b)(ii) floors-and-walls route is modelled as available only where marks or
  coordinates are impossible or impracticable; whether that is a factual or discretionary
  judgement was not explored.
- "Within one month" (s 17) and "every day or part of every day" (s 20) are left to the
  caller as a boolean and a day count.
- The rules made under s 21 (fees, inquiry procedure, survey practice) were not read.
- No case law on boundary disputes or the conclusiveness of maps was searched.
