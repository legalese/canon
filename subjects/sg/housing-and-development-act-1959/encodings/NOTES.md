# Housing and Development Act 1959 (Singapore) — encoding notes

Read this first. `BRIEF.md` is the specification; `../source/PROVENANCE.md` says where the text came from.

## 1. What is encoded

**The whole Act** (Parts 1-6 and the two Schedules), as printed in SSO's informal consolidation of the version in force from 15 July 2026. It is encoded from the text already deposited in this repository; no PDF was supplied.

**Inputs.** These are taken as given rather than worked out:
- the Board's and the Minister's discretions and opinions;
- prescribed matters: minimum occupation periods, rules under s 74, prescribed persons;
- the court's findings and convictions;
- commencement dates the Act does not state (the "appointed date" in s 63(1)(o)).

**Carried as text.** The Schedules list the lands vested in the Board on 1 May 1982. In the deposited text their lot tables have interleaved columns: the text is all there, but row-to-column alignment cannot be relied on. They are carried as text and nothing turns on them.

### The top-level goal

`the flat position for` a `Flat case` (`hda-goal.l4`) answers: *for this HDB flat and its owner (or would-be owner), may the person buy it; is this dealing lawful; is the flat safe from creditors; and may the Board re-enter, compulsorily acquire it, or impose a financial penalty instead?*

| goal | question | main functions | provisions | module |
| --- | --- | --- | --- | --- |
| 1 | May this person buy a flat from the Board? | `entitled to purchase a flat from the Board`, `the Board may cancel the application on`, `eligible to buy a DBSS flat…` | ss 50(1), (10), (12), 57, 92 | `hda-flats.l4` |
| 2 | Is this dealing lawful, and is the flat safe from creditors? | `the effect of`, `does not vest in the Official Assignee on bankruptcy…`, `may not be attached in execution…`, `the Board may vest a deceased owner's flat…` | ss 52, 55, 56, 58, 59 | `hda-flats.l4` |
| 3 | May the Board re-enter, acquire, or penalise instead, and when may it act? | `the Board may re-enter and determine the lease`, `the Board may compulsorily acquire the flat on`, `the most financial penalty instead of ss 50, 62 or 63…`, `the earliest the Board may act on`, `the last day to object or appeal for` | ss 50(3A)-(4), 59(5A)-(6), 62, 63, 66, 68, 69, 74, 15, 28(14), 29(9) | `hda-flats.l4` |
| 4 | Does an upgrading poll carry; may works go ahead; when is a contribution due, charged and enforced? | `the poll carries`, `specified upgrading works may be carried out…`, `special upgrading works may be carried out…`, `the improvement contribution is due by…`, `…becomes a charge on…`, `the earliest the Board may sell the flat…`, `the s 82(8) application of proceeds` | ss 77, 80, 82 | `hda-upgrading-board.l4` |
| 5 | Is the Board validly constituted and quorate; when is its budget due? | `the Board's constitution is within s 6…`, `the member's office is vacant or barred`, `the meeting is quorate…`, `the budget is due by…`, `a temporary appointment … is within 2 months` | ss 6, 7, 9, 45, 98 | `hda-upgrading-board.l4` |
| 6 | Offences, penalties, composition, financial penalties, parking liability, service and entry | `the maximum penalty for`, `the most that may be collected to compound`, `the most financial penalty for`, `the vehicle owner is liable for the parking offence…`, `service takes effect on…`, `may be served by email…`, `hours of notice needed to enter for` | ss 13, 14, 28-33, 70, 72, 84, 107, 108, 111 | `hda-upgrading-board.l4` |

## 2. Coverage table

| provision | disposition |
| --- | --- |
| long title, ss 1-5 | carried as text |
| ss 6, 7, 9 | Goal 5 |
| ss 8, 10-12 | carried as text |
| ss 13, 14 | Goal 6 (offences) |
| s 15 | Goal 3 (mortgage rate notice) |
| ss 16-27 | carried as text (functions and powers) |
| ss 28, 29 | Goal 6 (entry notice); Goal 3 (repair-cost date) |
| ss 30-33 | Goal 6 |
| ss 34-48 | carried as text, except s 44 and s 45(4) (Goal 5) |
| ss 49, 51, 53, 54, 60, 61, 64, 65, 67, 71, 73 | carried as text |
| ss 50, 57 | Goals 1 and 3 |
| ss 52, 55, 56, 58, 59 | Goal 2; the periods in s 59 are in Goal 3 |
| ss 62, 63, 66, 68, 69, 74 | Goal 3 |
| ss 70, 72 | Goal 6 |
| ss 75, 76, 78, 79, 81, 83, 85, 86 | carried as text |
| ss 77, 80, 82 | Goal 4 |
| s 84 | Goal 6 (entry notice and offence); the s 84(3) warrant and s 84(8) acquisition are carried as text |
| ss 87-91, 93, 94 | carried as text |
| s 92 | Goal 1 |
| ss 95-97, 99-106 | carried as text |
| s 98 | Goal 5 |
| ss 107, 108 | Goal 6 |
| ss 109, 110 | carried as text |
| s 111 | Goal 6 |
| First and Second Schedules | carried as text (see §1) |

Repealed sections are marked in the source and not encoded.

## 3. Fork register

| id | provision | question | reading taken | why |
| --- | --- | --- | --- | --- |
| F1 | s 50(1)(b) "at any time within 30 months immediately prior to the date of making an application" | Is a disposal exactly 30 months before the application inside the window? | Yes, it is barred | The window is inclusive of its far edge; the independent pass read it the same way (E07) |
| F2 | s 62(1)(c) "within 2 weeks after a written notice" | On which day may the Board re-enter? | From day 15 after the notice. The input counts days after the notice day | The notice day is excluded, so the 2 weeks end at the close of day 14 |
| F3 | ss 50(3A), 59(5A), 66(1), 68(1) "until the expiry of a period of N days after the service" | When may the Board act? | served + N + 1 | The period expires at the close of served + N |
| F4 | s 63(2) "$250,000 or such higher value as the Minister may allow" | How is the cap set? | The Minister's higher figure if one is given, otherwise $250,000 | The text |
| F5 | s 63(1)(o) "the appointed date" | When is it? | An input: the Act does not state it | Commencement is outside the text |
| F6 | s 107 | Fine or imprisonment, or both? | Either, not both | The section has no "or both" |

## 4. Tests

- **`hda-tests.l4`: 117 assertions.** Expected values are worked from the source. They cover:
  - every s 50 window edge;
  - each dealing's effect;
  - the s 58 protections;
  - each s 59 limb;
  - the re-entry and acquisition grounds, with their edges;
  - the Board-step periods;
  - poll thresholds, contributions and the s 82(8) waterfall;
  - the Board's quorum, constitution and budget date;
  - every penalty, composition, parking, service and entry rule;
  - whole cases through the top-level goal.
- **The independent pass.** The files are `tests-independent.l4` (164 assertions), `independent-expectations.md` and `INDEPENDENT-TEST-REPORT.md`. A separate session wrote its expectations from the source before reading the encoding.
  - **Result:** 162 pass and 2 fail. Both failures (E60, E91) are off-by-one-day expectations; the report itself concludes the encoding is right (forks F2 and F3). They are **expected failures**, and the expected values are left as written.
- **Changed after the independent pass:**
  - **s 50(1)(b):** every disposal date is now an input (a list), so an earlier disposal inside the window is no longer hidden by a later one.
  - **s 58(6)-(7):** these are now separate rules. A consented mortgagee or statutory chargee defeats only the attachment protection, not the protection from vesting in the Official Assignee. The top-level goal reports both.
  - **s 59(3)(a):** representation taken out more than 12 months after death still satisfies limb (a).
  - **s 63(1)(m):** the "above 14" age now limits only an authorised occupier, not the owner or spouse, and the 1 March 1984 limit is an input.
  - **s 63(1)(o):** the related-person-or-above-18 condition and the appointed date are inputs.
  - **Top-level penalty:** this was hard-coded at $50,000. It now follows the breach date under s 74, and gives NOTHING when no breach is put.

  The independent file was changed only in plumbing: the purchase helper turns its date into a list, and the (m) and (o) constructors and the `Flat case` constructor take their new arguments. Each value is set so that the expected answer is unchanged.
- **Simplifications the report lists, kept as they are:**
  - the s 111 email exclusions are an input;
  - s 111(9) is carried as text;
  - email service takes effect on the day sent;
  - s 33(3)(b)-(c) are merged;
  - the warrants in ss 28, 29, 64, 84 and the s 84(8) acquisition are carried as text;
  - s 59(4) rescission is carried as text;
  - the s 50(12)(b) age and Penal Code list are an input (ground (b) made out);
  - the s 55(3) 20 November 1998 edge is an input.

## 5. Open questions

- s 74 limits the financial penalty to breaches on or after 20 July 2015, and allows it only "instead of" proceeding under ss 50, 62 or 63. The encoding reports the ceiling and leaves the election to the Board.
- The Schedules' lot tables: if they are ever needed, they should be re-extracted from the PDF.

## 6. Checks

`L4=~/.local/bin/l4 ./check.sh` prints 0 errors for every module except `tests-independent.l4`: 279 satisfied and 2 failed (the expected failures E60 and E91). See `encoding.json` → `checks`.
