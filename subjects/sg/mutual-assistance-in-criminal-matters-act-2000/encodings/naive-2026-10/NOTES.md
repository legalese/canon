# Mutual Assistance in Criminal Matters Act 2000 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, with amendments to Act 10
of 2025 (in force 15 September 2026, a Second Schedule entry) and Act 42 of 2024 (in
force 28 March 2025) shown. The arrangement of sections at the top of the deposit is
out of step with the body; the body's section numbers are used.

**Checks:** one case file, 205 assertions satisfied, 0 errors, 0 warnings. Most of
them (140) are a grid of seven refusal rules run over twenty requests.

## Why this Act, and why scoped

**9 of the 527 Singapore Acts** deposited here cite it. This row takes the
decision the Attorney-General makes on a foreign request (ss 16 and 20, with the
s 2 meaning of "Singapore offence"), and what the Act asks of people in Singapore
caught up in one: production orders and the offence of not complying (ss 22, 25),
what a witness must answer and how the evidence may be used (ss 21, 21A), travel
abroad to assist (s 26), safe conduct (s 11), no penalty for refusing to attend
(ss 10, 26(4), 40), and the maximum penalties (ss 25, 28, 35(4)). Requests by
Singapore, the content of a request (s 19), foreign confiscation orders (ss 29 to
32), transit, locating persons and service of process (beyond s 40), and the
First and Second Schedules are not encoded.

## What the Act turns out to say

### 1. Statements taken for a foreign investigation cannot be used here even for perjury

s 21(9) bars evidence taken by a Magistrate from any Singapore proceedings "except
a prosecution of the person who gave that evidence for the offence of perjury, or
contempt of court". s 21A(5), added by Act 42 of 2024 for statements taken by an
authorised officer, has the same bar with no exception at all. Asserted.

### 2. Dual criminality covers evidence, confiscation and search, but not locating people, serving process or sending witnesses abroad

s 20(3) requires refusal where the conduct would not be a Singapore offence here,
but only for Divisions 2, 5 and 6. A request to locate a person (Division 7),
serve process (Division 8) or arrange a person's attendance abroad (Division 3)
is not refused on that ground. Asserted.

### 3. Foreign tax evasion escapes dual criminality, more easily for evidence than for search

s 20(4) lifts the dual-criminality bar for any Division 2 request about a foreign
tax evasion offence. s 20(5) lifts it for Divisions 5 and 6 only if there is also
an Income Tax Act 1947 arrangement (s 49 or 105BA) or an international tax
compliance agreement with that country. Asserted.

### 4. A non-treaty country can get some help without promising anything, and other help not at all

s 16(1)(a) lets any foreign country have Magistrate-taken evidence (s 21),
location of persons and service of process; refusal for want of a reciprocity
undertaking is only discretionary (s 20(2)(d)). Production orders, statements,
search and seizure, attendance abroad and confiscation go only to prescribed
countries, or to others that give the reciprocity undertaking (s 16(2)), which
are then deemed prescribed (s 16(3)). Asserted.

### 5. Nine grounds oblige refusal, including "insufficient gravity" and "public interest"

s 20(1) says a request "must be refused" if, in the Attorney-General's opinion,
any of nine grounds holds: treaty breach, political offence, military-only
offence, persecution, double jeopardy, insufficient gravity, a thing of
insufficient importance or obtainable otherwise, public interest, or prejudice to
a Singapore criminal matter. Since each turns on the AG's opinion, "mandatory" is
less binding than it reads. A further mandatory ground (s 20(2A), Act 42 of 2024)
applies to production orders and search: the country must undertake to limit use
and to return or dispose of the thing. Asserted.

### 6. Refusing to help carries no penalty, but a production order does

s 10, s 26(4) and s 40 each say a person is not "subject to any penalty or
liability or otherwise prejudiced in law" only for refusing to attend, or for
ignoring a foreign witness summons "despite any contrary statement in the
summons". By contrast, not complying with a s 22 production order without
reasonable excuse is an offence (s 25), as are escaping transit custody (s 28) and
obstructing a search warrant (s 35(4)), each up to $10,000 or 2 years. A prisoner
cannot be sent abroad to assist even with consent (s 26(2)(d)). Asserted.

### 7. The person under investigation abroad need not testify here

s 21(6): that person is "competent, but not compellable". s 21(7): no witness
must answer a question they could not be compelled to answer in the foreign
proceedings. Asserted.

## What would need doing before this is worth anything

- s 25(b) says false material is an offence if produced "without (i) indicating
  ... or (ii) providing correct information". This row reads it as: an offence
  only if neither was done. That is an inference; the other reading (both needed
  where correct information is available) is open.
- s 16 and s 20 are encoded as yes/no facts about the AG's opinion; none of the
  opinion-based grounds is decided.
- The First and Second Schedules (which offences count) were not encoded;
  whether an offence is listed is taken as given.
- No prescribed-country orders under s 17, regulations or case law were read.
