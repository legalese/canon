# Fisheries Act 1966 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation. The deposit says it
"incorporates all amendments up to and including 1 December 2021"; the latest
amending Acts annotated in the text are Act 11 of 2019 (Singapore Food Agency Act
2019) and Act 15 of 2019 (Criminal Law Reform Act 2019). The arrangement of sections
at the top of the deposit is misaligned with the body around ss 19 to 22; the body's
numbering is followed.

**Checks:** one case file, 53 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**5 of the 527 Singapore Acts** deposited here cite it. This row takes what a
fisherman, fish farmer or fish dealer meets in the Act itself: who is a fish dealer
(s 2), the officer who will not identify himself (s 5(2)), licence validity (ss 7,
8), the poison and explosives offences (s 10), trawl-nets (s 12), penalties (s 13),
proceeds of seized fish (s 15), liability of partners, employers and officers (ss 17,
19, 20), composition (s 18), offences abroad (s 22) and exemptions (s 25).

Not encoded: administration (ss 3, 4), the licensing discretion and appeal (s 6),
forfeiture and confiscation (ss 14, 16), jurisdiction (s 21), officers' powers
(s 23), service (s 24), fees (s 26) and the rule-making power (s 27). The Act is
mostly a frame: the actual fishing controls (net sizes, closed areas, licensing of
vessels, stakes and farms) are all left to rules under s 27, and none were retrieved.

## What the Act turns out to say

### 1. Trawling carries mandatory jail, and the gear goes even if nobody is convicted

s 12(2): using, operating or assisting with a trawl-net in territorial waters is
punishable by imprisonment "for a presumptive minimum term of not less than 3 months
and not exceeding 3 years" (inserted by Act 15 of 2019). No fine is mentioned.
s 12(3): on the Public Prosecutor's written application the court "shall" forfeit
the vessel or gear used and seized, "notwithstanding that no person may have been
convicted". Asserted.

### 2. Partners escape on either proof; employers and officers need both

s 17: a licensed partner is liable for the others' acts unless he proves he had no
knowledge **or** in no way contributed. s 19 (employer) and s 20 (director, manager,
partner, secretary, or one purporting to act as such) require proof of **both** due
diligence and no knowledge, consent or connivance. So a partner is easier to clear
under s 17 than under s 20, which also names partners. Asserted (the overlap between
ss 17 and 20 is noted, not resolved).

### 3. Being near the water with poison is presumed use; on a fishing boat it is an offence outright

s 10(3): a person found with a poisonous or explosive substance "in the neighbourhood
of any waters shortly after the use of such a substance" is "presumed until the
contrary is proved" to have used it to stupefy, poison or kill fish. s 10(4): anyone
in a fishing boat found with such a substance without a licence commits an offence,
with no intent required. s 10(2): possessing fish caught that way is an offence
unless one gives "a satisfactory account". Asserted.

### 4. You may refuse an officer only if he both fails to declare himself and refuses his card

s 5(2) protects a person who refuses an authorised officer, or a police officer not
in uniform, "who fails to declare his office **and** refuses to produce his
identification card on demand". Either one alone does not suffice. Asserted;
limiting the excuse to officers not in uniform is an inference from s 5(1)(a).

### 5. Continuing offences: $50 a day, and jail once it runs past 10 days

s 13(1), (2): the general maximum is $10,000 or 12 months or both. s 13(3): after
conviction, a fine not exceeding $50 for every day the offence continues, and if it
continues "for a period exceeding 10 days after conviction", imprisonment up to 6
months. Asserted.

### 6. Smaller points

- Licences expire on 31 December of the year of issue unless they say otherwise, are
  not transferable (s 7), and a partnership licence survives a partner's death or
  retirement (s 8(4)). Asserted (s 7(3) not asserted).
- A "fish dealer" includes anyone buying fish except for personal consumption, and
  anyone processing fish (s 2). Asserted.
- Seized fish may be sold at once (s 15). The proceeds are held pending any
  prosecution or claim; if there is none, they go to the person the fish was seized
  from, or to the Agency if that person cannot be ascertained. Asserted.
- Composition is capped at $1,000 and only for offences prescribed by rules (s 18).
  Asserted.
- Offences abroad are triable in Singapore when committed by citizens, ordinary
  residents, or crew or owners of Singapore-registered fishing vessels, but not for
  offences under subsidiary legislation (s 22). Asserted.
- Exemption under s 25(1) needs the Minister's approval and covers only researchers
  fishing "only" for research and people fishing for personal consumption. Asserted.

## What would need doing before this is worth anything

- The rules under s 27 (where the real fishing controls and the list of compoundable
  offences live) were not retrieved.
- "Presumptive minimum term" in s 12(2) is encoded as a plain 3-month floor; what a
  court may do below a presumptive minimum is a question for the Criminal Procedure
  Code or Penal Code, not read here.
- Whether s 12(2) excludes a fine, and how ss 17 and 20 interact for partners, are
  left open.
- No case law was searched.
