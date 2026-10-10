# Constitution of the Republic of Singapore — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, deposited as
`CONS1963.txt`; the deposit calls itself the "version in force from 15/9/2026".
The latest amendment annotated is Act 9 of 2025 (in force 15/09/2026).

**Checks:** one case file, 52 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Chosen for its **everyday-life relevance** to ordinary people in Singapore, not by
how often other Acts cite it. The Constitution is long, so this row takes the
provisions an individual meets: rights on arrest (Art 9), no retrospective
punishment or repeated trial (Art 11), the bar on some kinds of discrimination
(Arts 12, 16), who may stand for Parliament (Arts 44, 45), and how citizenship is
acquired by birth, descent and registration, kept, renounced and lost after a
sentence (Arts 121-123, 126, 128, 129(3)(b)(i) and (7)).

Not encoded: sovereignty and referendums, the President and the Executive, the
Council of Presidential Advisers, the rest of the Legislature (including vacation
of seats under Art 46), the Judiciary, the Public Service, finance, Arts 10, 13,
14 and 15, naturalisation (Art 127), the other deprivation grounds and the
committee-of-inquiry procedure (Arts 129(2), (4)-(6), 130, 133-135), Part 12
special powers, and the Schedules.

## What the Act turns out to say

### 1. A child born abroad is not a citizen by descent through a naturalised parent

Art 122(1)(b) names a father or mother who is a citizen "by birth, registration or
descent". Citizenship by naturalisation, listed separately in Art 120(2)(d), is not
among them. Read literally, a child born abroad to a naturalised-citizen father and
a non-citizen mother is not a citizen by descent. Asserted. (Whether a
naturalised parent's child has another route, such as registration of minors under
Art 124, was not encoded.)

### 2. One registered parent brings in the foreign-citizenship test, even if the other parent was born a citizen

For a birth on or after the 2004 amendment, Art 122(2)(b) denies citizenship by
descent to a child who acquires the birth country's citizenship where "either his
father or mother is a citizen of Singapore by registration". Read literally, a
child of a citizen-by-birth father and a citizen-by-registration mother, born in a
country that confers citizenship by birth, is not a citizen by descent. Art 122(3)
works the same way for a parent who is a citizen by descent. This is the literal
reading; the encoding does not try to find a purposive one. Asserted.

### 3. Before the 2004 amendment, only the father counted

Art 122(1)(a): for a birth before the commencement of s 7 of the 2004 Amendment
Act, a child born abroad is a citizen by descent only if "his father is a citizen".
A 1990 birth abroad to a citizen-by-birth mother does not qualify under Art 122.
The deposit does not give the commencement date; the encoding takes it as a flag.
Asserted.

### 4. Discrimination is barred on four grounds only, and only against citizens

Art 12(1) gives all persons equality before the law, but Art 12(2) bars
discrimination "against citizens of Singapore on the ground only of religion,
race, descent or place of birth", unless expressly authorised by the Constitution;
Art 12(3) saves personal law and religious offices. Art 16(1) repeats the four
grounds for public schools and student aid. Sex and age are not among them.
Asserted.

### 5. A $10,000 fine bars a parliamentary candidate for five years; $5,000 can cost a new citizen citizenship

Art 45(1)(e) disqualifies a person sentenced to at least a year's imprisonment or a
$10,000 fine (no free pardon; a foreign conviction counts only where the act would
be punishable in Singapore), and Art 45(2) ends the disqualification five years
after release or the fine, or earlier if the President removes it. Art 129(3)(b)(i)
lets the Government deprive a citizen by registration or naturalisation sentenced
within five years of becoming a citizen to at least a year or a $5,000 fine, but
Art 129(7) forbids it where the person would be left stateless and requires that
continued citizenship be "not conducive to the public good". Citizens by birth or
descent are outside Art 129. Asserted.

### 6. Registration as the spouse of a citizen is open to a wife only

Art 123(2) lets "any woman who is married to a citizen of Singapore" be registered
after two years' continuous residence. No clause for a husband was found in Part 10;
(inference) a husband would have to qualify under Art 123(1) like anyone else. Asserted.

### 7. Arrest: 48 hours to a Magistrate, but not for everyone

Art 9(4) requires an arrested person not released to be brought before a Magistrate
"without unreasonable delay, and in any case within 48 hours" (excluding necessary
journeys), and Art 9(3) gives a right to be told the grounds and to a lawyer of
choice. Art 9(5) excludes enemy aliens and people arrested for contempt of
Parliament on the Speaker's warrant. Only the 48-hour ceiling is encoded, not
"unreasonable delay", and the Art 9(6) saving for preventive-detention and
drug-rehabilitation laws is not. Asserted.

### 8. Minors who became citizens must take the oath at 21

Art 122(4) and Art 126(3): citizenship acquired as a minor by descent, or by
registration under Art 124, ends at 22 unless the Oath of Renunciation, Allegiance
and Loyalty is taken within 12 months after turning 21. Asserted. Renunciation
(Art 128) needs age 21 (or marriage, for a woman under 21), sound mind and another
citizenship, and may be withheld from a person subject to the Enlistment Act 1970 unless he has
done full-time service or 3 years of operationally ready service, or met conditions
the Government sets. Asserted.

## What would need doing before this is worth anything

- Every finding is a literal reading. None was checked against case law, the
  Singapore Citizenship Rules, ICA practice or the Parliamentary Elections Act.
- The commencement date of s 7 of the 2004 Amendment Act was not looked up.
- Arts 124, 127 and 130-135 (registration of minors, naturalisation, other
  deprivation grounds and the inquiry procedure) would complete the citizenship
  picture; the elected-President qualifications are a natural next scope.
- Art 9(4)'s "unreasonable delay" and the Art 9(6) saving need a judgment-based
  treatment that a boolean cannot give.
