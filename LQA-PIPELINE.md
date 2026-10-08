# The LQA pipeline

Legislative quality assurance: finding, evidencing and reporting defects in a Bill, an Act or a
piece of delegated legislation. This pipeline is Legalese's own, built for that job. It is not the
`l4-ide` conversion pipeline (P0-P10, described in [`PIPELINE.md`](PIPELINE.md)), which exists to
turn law into checked executable artifacts and has no stage that finds a defect.

**Status: first version, 1 October 2026.** The steps, the defect categories, the discovery methods
and the handover are settled. Each category's probe procedure is in
[`LQA-CATEGORIES.md`](LQA-CATEGORIES.md). The register formats are JSON Schemas in
[`tools/lqa/schemas/`](tools/lqa/schemas/), and [`tools/lqa/check.js`](tools/lqa/check.js) reports
each step's status from a subject's files. No real subject has been run through it yet. Paths
assume the current repository layout, which is itself provisional.

---

## What it keeps, and why

Four things carry over from the conversion pipeline because they are what make a finding
trustworthy, whoever runs the work:

1. **Every source is pinned.** Each document is fingerprinted (sha256) and recorded with where it
   came from, so every finding is tied to one exact print.
2. **Forks are recorded, and a fork is not a defect.** Where the text supports two readings, the
   register records the reading taken and the reading rejected, and the encoding asserts both
   where it can.
3. **A step reads only what an earlier step produced.** Each step names what it leaves behind, and
   a later step may rely on nothing else. When a later step needs something an earlier one did
   not produce, that is a gap in the earlier step, recorded and repaired there.
4. **Release needs a human signature and cannot be waived.**

And one rule from the corpus: **every finding is traceable to a provision and reproducible by
machine.** A finding with no assertion, scenario or simulation behind it is labelled opinion.

---

## Who runs it

A **legal engineer** (LE) runs the pipeline from 0H to 11A. The output is handed to a **legal
drafter** (LD):

- the written report; and
- the scheme for the LQA Console, complete with incidents, scenarios and simulation parameters,
  in which the LD can replay each finding, run simulations, build scenarios of their own and
  discuss the law with Claude.

The handover is final: the pipeline ends when the LD has the report and the console. (Where both
can work in one hosted environment, this may later become an ongoing collaboration; that is not
part of this design.)

The console is the LD's tool, not the LE's workbench. No step of the pipeline needs anyone to open
it: the scheme's scenarios and simulation runs are played headless by the console engine.

---

## The steps

Steps are numbered 0 to 13. The letter says who does the step: **A** for the agent, **H** for a
human. An agent may help with an H step, but cannot complete one.

| Step | Name | Who | Leaves behind |
|---|---|---|---|
| **0H** | Jurisdiction | Human | the jurisdiction's reference set and library |
| **1A** | Pin | Agent | the instrument, at its exact print, fingerprinted |
| **2A** | Gather | Agent | the subject's surroundings, the search log and the reference register |
| **3H** | Confirm | Human | a signed statement that the reference set is complete, or what is knowingly missing |
| **4A** | Encode | Agent | the L4 modules and the coverage record |
| **5A** | Fork | Agent | the fork register |
| **6H** | Fidelity | Human | a certification that the encoding says what the law says, or a recorded waiver |
| **7A** | Probe | Agent | candidate findings, and a record of which categories ran over which Parts |
| **8A** | Demonstrate | Agent | the evidence for each candidate |
| **9A** | Challenge | Agent | each candidate either OPEN or VERIFIED-NO-DEFECT, and each OPEN finding a headline, a drafting note, or merged |
| **10A** | Re-pin | Agent | each surviving finding stamped with the current print |
| **11A** | Report | Agent | the LQA report |
| **12H** | Release | Human | a signature for one release to one recipient |
| **13A** | Publish | Agent | the release log |

### 0H — Jurisdiction

Done once per jurisdiction, shared by every subject in it, and re-confirmed when any item changes.
The first subject in a jurisdiction will usually show what else belongs (a local-government Act for
a law that local laws are made under, say); add it then and re-confirm.
A human chooses what belongs here, because which manual is authoritative, and whether the set is
complete, is a judgment no search can make.

The reference set holds four kinds of material:

- **drafting manuals, style guides and plain-language guidelines** issued by the drafting office;
- **interpretation legislation**: the Interpretation Act, and whatever governs commencement,
  citation, amendment, repeal, publication and official versions. In some jurisdictions that is a
  separate Legislation or Publication Act; look for one;
- **other meta-legislation** that governs how legislation operates: the making, publication and
  disallowance of delegated legislation, general penalty and infringement-notice regimes, general
  principles of criminal responsibility, limitation periods for prosecutions, and the constitution
  for limits on power;
- **the jurisdiction library** (below), as it grows.

Every item is pinned and versioned like a subject's sources. Manuals are revised, so a Style finding
records which version of the manual it was checked against. Pin the file you actually read from:
the official file, or a text converted from it, with the conversion recorded in the item's `why`.
Where a site-wide licence and a document's own notice conflict, do not hold a copy; record the
conflict in `licence` and give a `no_copy_reason`.

**Where the drafting office publishes no manual.** Some do not (Western Australia's Parliamentary
Counsel's Office publishes none). Then Style (S) has nothing to cite, and the human at 0H decides
one of two things, recorded in the confirmation:

- **S does not run** for this jurisdiction. Each probe of S is recorded with the note "not run: no
  0H manual", and the report says so.
- **A named stand-in** (another jurisdiction's manual) is added with kind `drafting-manual` and a
  `why` saying it is not the jurisdiction's own and why it was chosen. S findings against it say so.

To check a reference set before any subject in the jurisdiction exists:
`node tools/lqa/check.js --jurisdiction subjects/<jurisdiction>/_jurisdiction`.

### 1A — Pin

The instrument at its exact print: the compilation of an Act, the print of a Bill (as introduced,
as amended in a House, as passed), or the version of a piece of delegated legislation. A human may
supply the file; the agent fingerprints it, records its source and licence, and says which print it
is. For a Bill, it also records the Bill's stage in each House.

### 2A — Gather

The agent's attempt at everything around this instrument:

- the Act a Bill amends, and the regulations and other delegated legislation made under the Act;
- explanatory memoranda, second-reading speeches and debates, and committee reports;
- **every provision the instrument cross-references** (see *The reference register*).

Every search is logged, including the routes that failed and why. A log of what was searched is
as much a deliverable as what was found, because it is what lets 3H judge completeness.

### 3H — Confirm

Agents are poor at fetching parliamentary and secondary material, and cannot know when a set is
complete. A human checks the pinned print and the gathered set, supplies what the agent could not
reach, confirms the reference register, and signs a statement of what the set is and what is
knowingly missing, with the reason for each gap. A later finding that turns on a missing document
then points back to a recorded gap, not a silent one.

### 4A — Encode

L4 in the instrument's own terms, one module per Part or Division, with an `@ref` citation on every
rule and `l4 check` clean. Referenced provisions marked *encoded* in the reference register are
encoded too, or reused from the jurisdiction library. The coverage record says which provisions
are encoded and which are not, and why.

The console scheme is drafted here too, from the L4: its actors, acts, rules and clocks follow the
encoding's reading, including the forks taken at 5A. Writing it is itself a way of finding
defects (method `ENC`).

### 5A — Fork

Every point where the text supports two readings goes into the fork register: the readings, the
reading taken, the reading rejected and the reason. Where the encoding can, it asserts both ways, so
a change to the reading taken cannot pass silently.

### 6H — Fidelity

A domain expert reviews the encoding section by section against the source, including any boundary
modules not already certified in the jurisdiction library, and certifies that it says what the law
says. This gate may be waived, but a waiver is a decision with a reason, recorded and printed in the
report, never an absence.

It comes before Probe so that no defect is hunted in an encoding nobody has vouched for. A
"defect" found in a misencoding is a defect in our own work.

### 7A — Probe

Run every defect category (below) over every encoded Part, following its procedure in
[`LQA-CATEGORIES.md`](LQA-CATEGORIES.md), the probe record says which categories ran over which Parts, so a report can state what was
checked rather than imply it. Style findings are checked against the 0H manuals and must cite the
paragraph breached. Each candidate enters the incident register as `CANDIDATE`.

### 8A — Demonstrate

Each candidate gets evidence of one or more of four kinds:

- **assert**: an `#ASSERT` in the encoding, cited by its text;
- **scenario**: a scenario in the console scheme, cited by its label, which must record the finding
  when played;
- **simulation**: a generated run, cited by its seed, its length and any parameters changed from
  the defaults, which must record the finding;
- **quote**: words from a pinned document, which must appear in its pinned copy. This is how Form,
  Style and Extrinsic findings are evidenced.

Scenarios and simulation runs are written into the scheme as data and played headless by the
console engine, so this step needs no one at a screen. A finding with no evidence is labelled
opinion and stays one until it gets some. A simulation run is stronger evidence than a scenario,
because a scenario can assert a state the rules could never reach.

Demonstration comes before Challenge on purpose: a finding made precise is easier to test.

### 9A — Challenge

Try to kill each finding. Read the instrument against the 0H meta-legislation, the delegated
legislation, the extrinsic material and the case law. Each candidate ends either `OPEN`, with a
category and severity, or `VERIFIED-NO-DEFECT`, naming the provision that answered it. Findings
answered as sound are kept, because knowing what was checked is part of the result.

**Challenge may answer a finding only from the 0H and 3H sets.** If something outside them answers
it, the answer still stands, but its absence from the set is recorded as a gap and repaired at 0H or
3H.

**Then triage what survives.** A thorough probe finds many things, and a reader given all of them at
once cannot tell which matter. Each `OPEN` finding gets a `tier`:

- **headline**: a real person (an owner, an applicant, a council, a court) gets a wrong, unfair or
  uncertain result in a situation that could plausibly happen. A headline also gets a `plain_title`,
  saying what happens to whom in words a non-lawyer understands, a `story` of about three sentences
  (who, what happens, why it matters), and a `rank`, 1 being the most consequential.
- **note**: a drafting note. Wording, form and style, cross-references that mislead without changing
  an outcome, and questions of reading on which little turns in practice.
- **merged**: the finding shares its cause or its fix with another, and is reported under it
  (`merged_into`).

At most ten findings are headlines. If more pass the test, the weakest become notes, and the report
says how many did. Nothing is discarded: notes and merged findings keep their evidence and appear in
full in the report and the console.

### 10A — Re-pin

Check every surviving finding against the current print of the instrument, and of every referenced
provision it turns on, which may have been amended on its own timetable. A finding already repaired
becomes `FIXED`. Each finding is stamped with the print it was last checked against.

### 11A — Report

Two outputs from one incident register, which must agree: no finding in one that is not in the
other.

**The console scheme**, finalised: every incident as an observation with its ID as `ref` and its
method as `foundBy`; every `OPEN` finding shown by at least one scenario, except Form and Style
findings, which no run can show and which appear as `static` observations; findings verified sound shown as
such; the simulation parameters with their defaults; and the text and L4 bundled where licences
allow.

**Both open on the headline findings.** The console's incident list opens on them, ranked, each under
its plain title with its story first and the technical detail behind a fold; drafting notes and
findings checked sound are one click away. The written report begins with a section of headline
findings in plain words, before any technical material.

**The written report**: each finding with its provision, evidence, category, severity, status and a
suggested repair; the forks and the readings taken; the findings checked and found sound; the probe
record; the coverage record; the state of every gate, including any waiver and its reason; and what
the reference set knowingly lacks.

### 12H — Release

Any act others will see — handing the report and console to the LD, sending findings to a ministry,
a regulator, a drafting office or a client, or publishing them — needs a named person's signature for that specific release to that specific
recipient. It cannot be waived. Handing over the console means publishing a copy for that
recipient, not sharing a demonstration link other people also hold. Before signing, the signer confirms that 10A has been run recently
enough that the findings are against the current print.

### 13A — Publish

The release is sent, and the release log records what went to whom, when, and against which print.

---

## Defect categories

A finding's ID is its category letter and a number: `D-01`, `M-02`. Numbers run in one sequence per
subject across all letters, so the number alone identifies a finding. If Challenge changes a
finding's category, the number stays and the old ID is kept as an alias. A finding
that spans two categories takes its primary letter and lists the other.

The letters avoid A and H, which mark the steps.

| Letter | Category | Covers |
|---|---|---|
| **D** | Definition | a defined term used inconsistently with its definition; a key term left undefined; circular or overlapping definitions |
| **R** | Reference | a cross-reference to the wrong, a missing or a repealed provision; a reference whose target does not do what the citing provision assumes; a pronoun or "the person" with no antecedent |
| **L** | Logic | contradiction; a gap (a case no rule decides); an overlap where two rules give different answers; an unreachable condition; a fact the law reads that no provision can make true |
| **T** | Time | commencement; deadlines and how time is counted; calendar arithmetic; a duty arising before it can be met; expiry and renewal |
| **U** | Uncertainty | ambiguity or vagueness that changes outcomes. The readings go in the fork register; the defect is that the drafter left the choice open |
| **P** | Power | delegated legislation beyond its power; a power with no holder; a discretion without criteria; a decision with no procedure, notice or review |
| **E** | Enforcement | an obligation with no consequence; an offence with no penalty or the wrong one; nobody able to enforce; a defence that defeats the offence |
| **M** | Amendment | an amending instruction that fails to apply; a repair that stops short; a missed consequential amendment; missing savings, transitional or validating provisions |
| **I** | Interaction | conflict between Parts, with the parent Act, with other Acts, or with a higher level of government |
| **X** | Extrinsic | an explanatory memorandum, heading, note or example at odds with the enacted words |
| **W** | Workability | a duty that cannot practically be complied with; a scheme that depends on something that does not exist. Reported only where the impossibility is demonstrated |
| **F** | Form | mechanical errors: typographical errors, numbering, grammar, broken formatting |
| **S** | Style | non-compliance with the jurisdiction's drafting manual, style guide or plain-language guidelines. Every S finding cites the paragraph of the 0H manual it breaches |

F and S are kept apart because "the drafter slipped" and "the drafter departed from the rules"
call for different responses. Both are reported after the substantive categories so they do not
crowd them out.

**Status** is one of `CANDIDATE`, `OPEN`, `FIXED`, `WAIVED`, `VERIFIED-NO-DEFECT`.

**Severity** is one of `none`, `low`, `medium`, `high`, with a combined value such as `low-medium`
where the case is between two.

**Each finding records the instrument and print it was made against** — the Act's compilation, or
the Bill's print. The instrument is a field, not part of the ID.

### How it was found

Each finding records **one** discovery method in its `found_by` field. It is not part of the ID.
Apply the tests in this order; the first that fits is the method:

| Method | Test |
|---|---|
| `RD` read | a **casual** reader of the provision would have caught it |
| `CMP` compare | found by setting documents side by side (the explanatory memorandum, the parent Act, the drafting manual, a referenced provision read as text), not through the L4 |
| `ENC` encode | writing the L4 or the console scheme forced the question |
| `CHK` check | a tool reported it without running the law: the L4 compiler, `l4 verify`, the console checker |
| `TST` test | a written case surfaced it: an `#ASSERT` or a scenario |
| `SIM` simulate | a generated run surfaced it |
| `EXT` external | someone else found it first, such as a committee, a court or a commentator. It is attributed, and still demonstrated and challenged like any other finding |

The test is a casual reader, not a careful one, on purpose: it credits the L4 with what a careful
reader might have caught but a casual one would not. The report states the test, so its numbers
can be read for what they are. `CMP` exists so that deliberate cross-reading is not credited to the
L4.

`found_by` is recorded at first record and does not change. **Evidence** (8A) is recorded
separately and may be several things: a finding found by `RD` and demonstrated by `TST` stays `RD`.

### Not defects in the law

Problems with our own encoding, or with our tools, are not findings about the law and do not go in
the incident register. "The Act is wrong", "we encoded it wrongly" and "the tool is wrong" have
different repairs. Corpus problems go in the subject's corpus register, and tool problems in the
tool's own register.

---

## The reference register

Every cross-reference the instrument makes is entered in the subject's reference register in 2A and
given one disposition:

- **encoded**: as a small boundary module, or reused from the jurisdiction library;
- **supplied as a fact**: the encoding takes its result as an input, with the reason;
- **out of scope**: with the reason.

**Depth.** By default, encode the referenced provision itself, plus what makes it readable: the
provisions it cannot be read without and the definitions it uses. Go no further. Go one step
further only when a candidate finding turns on it, and record why. Depth follows the findings, not
curiosity.

This replaces the corpus's older scope discipline, under which every cross-reference was
automatically a fact-supplied input. A cross-reference may still be supplied as a fact, but now
because someone decided so, with a reason.

Encoded references are where Reference and Interaction findings come from: the defects that
appear only when the citing Act and the cited Act are read side by side.

## The jurisdiction library

Boundary modules and the encoded parts of the meta-legislation live at jurisdiction level, not
inside a subject, so the next subject that cites the same provision finds it done and already
through 6H. Meta-legislation is encoded selectively: a provision joins the library when it answers
or decides a finding, not before. Over time each jurisdiction builds a library of the provisions
that matter in practice, chosen by use.

---

## Where things live

Under the current layout. Each JSON file has a schema in `tools/lqa/schemas/`; `source-bundle.json`
and `fork-register.json` keep the formats the corpus already uses.

```
subjects/<jurisdiction>/_jurisdiction/
    reference-set.json       0H: manuals, guides, meta-legislation, each pinned; its "confirmed"
                             block is the 0H signature
    sources/                 the pinned texts, where their licence allows
    library/*.l4             boundary modules and encoded meta-legislation

subjects/<jurisdiction>/<subject>/
    lqa.json                          the instrument, its current print, and who runs the subject
    registers/source-bundle.json      1A, 2A: every source, pinned
    registers/search-log.json         2A: every search, including failed routes
    registers/reference-register.json 2A: every cross-reference and its disposition
    *.l4, coverage.json               4A: the encoding, what it covers, where its scheme is
    registers/fork-register.json      5A
    registers/gates.json              3H, 6H, 12H: signatures and waivers
    registers/probe-record.json       7A: categories run over Parts
    incidents.json, INCIDENTS.md      7A-10A: findings, machine-readable and prose
    REPORT.md                         11A
    registers/release-log.json        13A
```

## Checking a subject

```bash
node tools/lqa/check.js subjects/<jurisdiction>/<subject>          # every step's status
node tools/lqa/check.js subjects/<jurisdiction>/<subject> --l4     # also run l4 check and l4 run
node tools/lqa/check.js subjects/<jurisdiction>/<subject> --digest 6H
node tools/lqa/test.js                                              # the checker's own tests
```

Each step is `DONE`, `OPEN` (with what is missing), `NOT STARTED`, `STALE`, `WAITING` (for an earlier
step) or, for 6H only, `WAIVED`.

**Strict order.** Every step waits for the one before it to be complete. A step whose predecessor
is not complete reports `WAITING`, whatever its own files say.

**How a human step is approved.** In the conversation. When the agent reaches an H step it stops,
shows the human what the step covers (the files, what they say, what is knowingly missing) and asks
whether to proceed. The human answers by typing their full name; a waiver of 6H also needs a
reason. The agent then records it:

```bash
node tools/lqa/check.js subjects/<jurisdiction>/<subject> --sign 6H --by "Full Name"
node tools/lqa/check.js --jurisdiction subjects/<jurisdiction>/_jurisdiction --sign 0H --by "Full Name" --statement "..."
```

`--sign` refuses if any earlier step is incomplete or the step's own files have problems. It writes
the name, the date and a digest of what was approved: into `reference-set.json` for 0H, into
`registers/gates.json` for the others. Nothing more: no keys, no certificates. The digest covers
the files the step vouches for:

| Step | Covers |
|---|---|
| 0H | the reference set's items and library, and the library modules |
| 3H | `source-bundle.json`, `search-log.json`, `reference-register.json` |
| 6H | every L4 module, `fork-register.json` (the console scheme gains findings after 6H, so 12H covers it) |
| 12H | `incidents.json`, `REPORT.md`, the console scheme |

Change any of them and the step reports `STALE` until it is approved again. The checker cannot tell
who typed a name: that an H step was done by a human is a matter of honesty, not of software. An
agent never records an approval the human did not type in the conversation.

**The worked example** at `tools/lqa/example/exampleland/` is a fictional Bill with five findings,
run through every step with fictional signatures. `test.js` breaks it twenty ways and checks that
the right step fails each time.

## Not yet done

- Whether 6H must be done by someone other than the encoder. The checker notes when it was, but
  does not fail.
- Generating the report and the scheme's incident list from `incidents.json`, rather than writing
  them by hand and letting 11A check that they agree.
- Running a real subject through the pipeline.
- Moving existing subjects off the older A/B/C/H incident IDs, which mark the instrument (Act, Bill),
  the corpus or the tool rather than the defect.
