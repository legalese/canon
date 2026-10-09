# Brief: Minimum Wage Law 5747-1987 (row IL-32, run IL-32-20261008, agent enc-il-32)

## Scope

The statutory rules for what an employee must be paid as a minimum, from the deposited Hebrew text (`../../registers/source-bundle/minimum-wage-law-5747-1987.he.wiki.txt`, sha256 `d74633b3e230f83e486642c2815a81fe98b3259450ee85f01bc6f1b972ef78f5`, an unofficial Wikisource consolidation whose amendments run to 5778).
Encoded: s 1 (the definitions of the monthly, daily and hourly minimum wage), s 2 (the right, part-time proportion, absence), s 3 (which pay counts), s 5 (no reduction on update), s 21 (the transitional amounts).
Taken as published inputs, clearly marked and with provenance: the shekel amounts in force since 1 April 2025, which come from the Minister's notices under s 6 and not from the Law.
Refused by name: the rates for those under 18 (s 16 regulations), for the disabled (s 17 regulations), the pay bases of s 18 regulations, and any date for which no figure is held.

## The two answers the capstone needs

1. The full adult monthly minimum wage on a given date.
2. The minimum for a part-time employee on given hours.
Where the Law's order or the figure is not held, each declines by name.

## What the text does not contain

The Law sets no youth rate, no apprentice rate and no age band as a fraction.
Section 16 lets the Minister fix them by regulations, which are not deposited, so the encoding refuses them by name.
The Law also contains no shekel figure except s 21's 525 and 551 (1987).

## Policy

Every ambiguity: one named switch, default DECLINE, the other readings kept by name and tested, and the default answers where the readings agree (Meng, SHRUG, 2026-10-08).
No figure is invented; a published figure is a clearly marked input with its source and hash.

## Deliverables

Nouns module; one rules module per section; a published-figures module; tests (expected values worked by hand first); NOTES.md; check.sh; encoding.json; SOURCE-LICENSE.md.

## Coverage table

See NOTES.md section 2; no row is left deferred.
