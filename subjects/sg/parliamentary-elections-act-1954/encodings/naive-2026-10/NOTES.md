# Parliamentary Elections Act 1954 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, as deposited at
`../../registers/source-bundle/PEA1954.txt`. The deposit labels itself "version in
force from 28/3/2025". The latest amendment annotated is S 200/2025 (wef 28 March
2025, Third Schedule), and the latest Act annotated is Act 34 of 2024 (wef 22 January 2025).

**Checks:** one case file, 55 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**7 of the 527 Singapore Acts** deposited here cite it. This row takes the rules a
voter, candidate, employer or publisher actually meets:

- who may be on the register (ss 5, 6)
- forfeiture of the deposit (s 28)
- compulsory voting and restoration (s 43)
- punishment and incapacity for corrupt and illegal practices (ss 61, 79)
- the expenses cap (s 69, Third Schedule)
- the employer's polling-day duty (s 76)
- the survey blackout, the exit-poll ban, the cooling-off ban and the canvassing ban
  (ss 61C, 61D, 78C to 78E, 80)

Not encoded:

- electoral divisions and GRCs
- registration, nomination, polling and counting procedure
- DRE voting, and overseas and postal voting
- the definitions of treating, undue influence and bribery (ss 58 to 60)
- the rest of the election advertising regime (ss 61B, 61E to 61S)
- election agents and returns (ss 62 to 75A)
- election petitions (Part 4) and the Fourth Schedule Rules

The deposit amount itself is not computed: s 28(1AA) sets it at an MP's monthly
allowance, rounded to the nearest $500.

## What the Act turns out to say

### 1. Not voting takes you off the register, and $50 puts you back

s 43(1) says "Every elector must record his or her vote", but s 43 attaches no fine to failing to vote. Instead,
s 43(5) expunges every non-voter from the register. s 43(8) restores a name "without
penalty" on "a good and sufficient reason", and s 43(8A) otherwise restores it "on
payment of the sum of $50". A person who is expunged and not restored is disqualified
under s 6(1)(g). Voting at a special polling station counts as voting (s 43(1A)). So
does an overseas postal voter applying for voting papers (s 43(1B)). Asserted.

### 2. A citizen abroad keeps the vote by keeping a contact address, but then loses it in a foreign jail even where Singapore would not have punished the offence

s 5(1A) deems a citizen ordinarily resident if they keep a contact address, "even
though the person is not resident". s 6(2) says a foreign conviction does not
disqualify under s 6(1)(b) unless the act would also be punishable in Singapore.
However, s 6(1A)(a) separately disqualifies a person who is deemed resident and is
serving a sentence "in any prison ... outside Singapore". That provision has no
requirement that the act be punishable in Singapore. Treating a person who relies on
s 5(1A) as one who is not actually resident is an inference. Asserted.

### 3. The fine for lying about a candidate has no stated cap

Under s 61(1)(g) and (h), personation, treating, undue influence and bribery are
punishable by up to $5,000 or 3 years. A knowingly false statement about a candidate's
character, or about another candidate's withdrawal (s 61(1)(d) and (e)), is
punishable by "a fine or ... imprisonment for a term not exceeding 12 months". No
maximum fine is stated. These are also the only corrupt practices that do not need
the Public Prosecutor's consent to prosecute (s 61(3)). Any corrupt-practice
conviction brings 7 years' incapacity to register, vote or be elected (s 61(2)). An
illegal practice brings 3 years (s 79(1)). Asserted.

### 4. A candidate on exactly one-eighth loses the deposit

s 28(4A) forfeits the deposit only where the votes polled "does not exceed one-eighth"
of the total. On that wording, exactly one-eighth is not more than one-eighth, so the
deposit is lost. One vote more and it is returned. In a GRC the test is applied to the
group's votes. Asserted.

### 5. The employer offence does not cover docking pay

s 76(1A) forbids deducting pay for the time taken to vote. But the offence in s 76(3)
covers only refusing a reasonable period for voting, or interfering with one. The row
therefore separates breaching s 76 from committing the s 76(3) offence. Railway train
crew who cannot be spared are excepted (s 76(2)). Asserted.

### 6. The expenses cap is $5 an elector, shared out in a GRC

The Third Schedule, as amended by S 200/2025, sets the cap at $5 for each elector. In
a GRC that sum is divided by the number of candidates in the group. Personal expenses
are excluded, and so is an election agent's fee "not exceeding $500" (s 69(1A)).
**Reading:** a fee above $500 is counted in full, not just the amount over $500. The
text supports either reading. Exceeding the cap knowingly is an illegal practice
(s 69(2)). Asserted, including one case that depends on the reading.

### 7. Three bans end at different times

- **Survey results** may not be published from the day the writ issues until the
  close of all polling stations (s 78C).
- **Exit polls** may not be published on polling day before the close (s 78D).
- **Election advertising** is banned from the eve of polling day until the close of
  polling (s 61C). Clothing and badges with permissible electoral matter, news by an
  authorised news agency, private messages, and unaltered posters put up earlier are
  excepted (s 61D).
- **Canvassing** is banned for the whole of polling day and its eve, not just until
  the polls close (s 80). This includes visiting an elector at home or at work.

For ss 78C and 78D, s 78E gives a defence: the person must prove both that the breach
was beyond their control and that they took all reasonable steps. Asserted.

## What would need doing before this is worth anything

- Days are modelled as whole numbers relative to polling day, and "before the close
  of polling" as a flag. No real calendar is used.
- The deemed-resident reading in finding 2 and the agent-fee reading in finding 6
  need checking against case law or practice. None was searched.
- The disqualifications in s 6(1)(a)(iii) (foreign allegiance), (b) (sentence of
  death), (e) (foreign armed forces) and (h) (expunged under the Presidential
  Elections Act), and those in s 6(1A)(b) and (c) (outstanding warrants), are not
  encoded.
- The election advertising regulations, which s 61D(1)(a)(iii) and (2)(d) rely on,
  were not retrieved.
