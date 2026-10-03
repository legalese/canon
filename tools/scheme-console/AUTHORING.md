# Writing a scheme

A scheme is the whole of what makes the console model one Act rather than another. It is
**data**: no functions, no statute-specific code. `engine.js` reads it and has never heard
of a dog or a barring order.

To add a statute, add one object to the array at the bottom of `schemes.js` and change
nothing else. Two worked examples are already in that file — the Dog Act 1976 exercises
every feature described here; the Retail Barring Orders Bill 2025 is leaner.

---

## The shape

```js
{
  id, title, jurisdiction, status, scope,   // labels for the reader
  startDate: "2026-01-01",                  // day 0. Ages are real calendar ages from here
  types:        [ ... ],   // kinds of actor, and what it takes to bring one into existence
  entities:     [ ... ],   // the cast the console opens with
  relLabels:    { ... },   // how a relationship reads on the canvas
  defs:         { ... },   // named expressions, so a test is written once
  actions:      [ ... ],   // what an actor can be told to do
  rules:        [ ... ],   // what the statute does about it
  observations: [ ... ],   // what is worth counting
  scenarios:    [ ... ]    // one-click demonstrations
}
```

---

## `types` — kinds of actor

```js
{ id: "dog", label: "Dog", band: 2, shape: "round", create: { ... } }
```

`band` places it on the canvas: `0` authorities, `1` people and organisations, `2` things
and places. `shape` is `"rect"` or `"round"`. **Omit `create` entirely** for a type nobody
can bring into existence — courts are the obvious case, and leaving it out is a statement,
not an oversight.

### `create` — what it takes to exist

```js
create: {
  nameHint: "Scout",        // what the form offers as a name
  bornVerb: "Whelped",      // the word for coming into existence; default "Born"
  fields: [ ... ],
  rels:   [ ... ]
}
```

**Every field declares where its value came from.** This is the part that matters, and the
part a new scheme most often gets wrong.

| `origin` | meaning | settable when creating? |
| --- | --- | --- |
| `"birth"` | the date of birth itself | scenario: as an age · simulation: today, always |
| `"innate"` | true from the start, conferred by nobody | both modes |
| `"conferred"` | becomes true only through an act | scenario only; `by` names the act |
| `"exogenous"` | settled outside this scheme, by other law | both modes, and say so in `note` |

```js
{ key: "restrictedBreed", type: "bool", origin: "innate", cite: "s. 3",
  label: "Is of a breed prescribed as restricted by the regulations",
  note: "The Act names no breeds — the regulations do — so this is a supplied fact." }

{ key: "declaredDangerous", type: "bool", origin: "conferred", by: "declare",
  cite: "s. 33E(1)", label: "Has been declared to be a dangerous dog" }

{ key: "bornDay", type: "age", origin: "birth", unit: "months",
  label: "Age in months", def: 12 }
```

Field `type` is `"bool"`, `"number"`, `"text"`, `"choice"` (with `options: [{v, label}]`),
or `"age"` (which must also be `origin: "birth"`, and takes `unit: "months" | "years"`).
Optional on any field: `cite`, `note`, `def`, `min`, `max`, `placeholder`, `emph`.

**Age is never stored.** A `"birth"` field writes `bornDay`, a day number, and age is worked
out from it against a real calendar whenever a rule asks. God mode works backwards from
the age you type to a date of birth, so the age still moves with the clock afterwards. Never
add an `ageMonths` or `ageYears` attribute — thirty-day months get "three months" and
"18 years" wrong, which is exactly the kind of error this console exists to find.

Relationships take the same `origin`:

```js
rels: [
  { key: "owner", label: "Owned by", target: "person", required: true, origin: "innate" },
  { key: "registeredWith", label: "Registered with", target: "localgov",
    origin: "conferred", by: "register", cite: "Pt III Div 1" }
]
```

`required: true` means the console refuses to create the actor without it, and says which
provision makes it necessary. Use it only where existence really is unintelligible without
the link.

---

## `entities` — the opening cast

```js
{ id: "d1", type: "dog", label: "Rex", note: "pit bull terrier",
  attrs: { breed: "Pit bull terrier", bornDate: "2023-07-01", restrictedBreed: true },
  rels:  { owner: "p1", registeredWith: "lg1" } }
```

Give a date of birth as `bornDate`, an ISO date. The engine converts it to `bornDay` on
reset. `id` is referenced by `rels` and by scenarios, so keep them short and stable.

---

## `defs` — named expressions

Write a test once, use it everywhere:

```js
defs: {
  dangerous: ["or", "$self.attrs.declaredDangerous",
                    "$self.attrs.restrictedBreed",
                    "$self.attrs.commercialSecurity"],
  ageMonths: ["ageMonths", "$self.attrs.bornDay"],
  isRestrictedPup: ["and", ["def", "parentRestricted"], ["<", ["def", "ageMonths"], 3]]
}
```

A def is evaluated in whatever environment invoked it, so `$self` means different actors in
different rules. That is deliberate and occasionally surprising: if a def is only ever right
for the target, name it so (`targetAge`, not `age`).

---

## Expressions

A literal, a `"$path"` into the environment, or `[operator, ...arguments]`. The environment
holds `$self`, `$target`, `$p` (the action's parameters) and `$day`.

| | |
| --- | --- |
| logic | `and` `or` `not` `if` |
| comparison | `=` `!=` `>` `>=` `<` `<=` |
| arithmetic | `+` `-` `*` `/` `floor` |
| presence | `exists` |
| time | `daysSince` · `ageMonths` · `ageYears` · `date` · `nextDate` |
| chance (simulation only) | `chance` · `randInt` · `oneOf` · `any` · `count` |
| reaching | `rel` (the actor a relationship points at) · `attrOf` (a fact of another actor) · `def` |

```js
["attrOf", ["rel", "$self", "parent"], "restrictedBreed"]
```

That is how "has at least one parent that is a dangerous dog (restricted breed)" gets said
without any code.

`["nextDate", 10, 31]` is the day number of the next 31 October on or after today, for
provisions that run "until the next 31 October". `set` it to an attribute when the period
starts; comparing `$day` to that attribute later is how the period ends.

---

## `actions` — what an actor can be told to do

```js
{ id: "attack", actor: "dog", target: "person",
  label: "Attack or chase a person", cite: "s. 33D",
  log: "An incident involving <b>{self}</b> and <b>{target}</b>.",
  params: [ { key: "bit", label: "bit, or otherwise caused physical injury" } ] }
```

`actor` is the type that may perform it — it appears in that actor's panel and nowhere else.
`target` is optional; with one, the console asks the user to click a target on the canvas.
`log` is optional narration written before any rule fires.

**Do not use `actor` to enforce the law.** It says who *can* do the thing in the world, not
who is *entitled* to. See the three categories below.

---

## `rules` — what the statute does about it

```js
{ id: "owner-is-victim", on: "action:attack",
  "if": ["and", ["def", "attackOrChase"], ["def", "ownerIsVictim"]],
  then: [
    ["log", "<b>The person attacked is {target}, who owns {self}.</b> …",
      { cite: "ss. 3, 33D(1)", sev: "stop" }],
    ["observe", "owner-victim"]
  ] }
```

Triggers:

| `on` | fires when |
| --- | --- |
| `"action:<id>"` | that action is performed |
| `"create:<type>"` | an actor of that type comes into existence |
| `"death:<type>"` | one is removed as an event, in Nature mode or a simulation |
| `"day"` | every day; add `"for": "<type>"` to bind `$self` to each actor of a type |

Effects:

| | |
| --- | --- |
| `["set", "$target.attrs.k", expr]` | write a fact; `null` removes it (a lapsed registration, a spent notice) |
| `["log", "template", {cite, sev}]` | say what happened, and under which provision |
| `["observe", "obsId"]` | count it |
| `["after", days, "ruleId"]` | fire a rule later |

`sev` is `"stop"`, `"warn"`, `"ok"` or omitted. `"ok"` is not "good" — it marks something
that looks wrong and is not, which is worth as much as a defect.

Log templates interpolate `{self}`, `{target}` and any path: `{target.attrs.offenceDay}`.
**A template cannot evaluate an expression.** To interpolate a computed number, `set` it to
an attribute first, then interpolate that attribute. `{daysSince}` renders as an em-dash and
is always a bug.

Rules fire in array order within a trigger, so a rule that records state must come before one
that reads it.

---

## The three categories

This is the distinction the whole design turns on, and it is the one thing a new scheme
should be checked against by hand.

**Naturally impossible** — a dog whelped aged ten. Handled by `origin`: Nature mode
simply does not offer the field. Nothing to write.

**Legally void** — a shopkeeper purporting to declare a dog dangerous. Give it an action, let
anyone perform it, and write a rule that changes nothing and says why:

```js
{ id: "purport-declare-void", on: "action:purportDeclare",
  then: [["log", "<b>Nothing has happened.</b> Section 33E(1) confers the power on the local
    government, and on nobody else. …", { cite: "s. 33E(1)", sev: "ok" }],
    ["observe", "void-act"]] }
```

Do **not** hide the button. A console that silently disables an ineffective act teaches the
drafter nothing; one that lets it happen and reports the nullity teaches them the provision.

**Prohibited but effective** — keeping a dog unsterilised past three months, transferring a
restricted breed pup. Fully available, and it produces an offence. **Never prevent these.** A
console that would not let you break the law could never show you an offence, which is most
of what an LQA job is looking for.

---

## `observations` — what is worth counting

```js
{ id: "owner-victim", ref: "A-01", sev: "stop", label: "The dog attacked its owner",
  cite: "ss. 3, 33D(1)",
  what: "A dog attacks or chases the person who owns it.",
  why: "Section 33D(1) makes every person liable for the control of the dog guilty …" }
```

Counters, not claims: one only moves when the simulation actually produces the situation.
Keep the ones that are *not* defects — a provision that looks wrong and is not is worth
recording, because knowing what was checked is part of the result.

`ref` is optional: the entry this observation corresponds to in the subject's `INCIDENTS.md`
(`B-01`, `V-01`) or fork register (`F-1`, `F-ATTACK-PROVOCATION-UNLESS`). The console's
Incidents panel shows `ref` where there is one and `id` where there is not. Leave it out rather
than guess. An observation with no register entry is still worth counting.

Two optional fields for subjects run through the LQA pipeline (`LQA-PIPELINE.md`):

- `foundBy`: how the finding was first found: `RD`, `CMP`, `ENC`, `CHK`, `TST`, `SIM` or `EXT`. It
  must match `found_by` in the subject's `incidents.json`; the LQA checker compares them. The
  console shows it as a tag on each incident and lets the reader filter by it.
- `static: true`: a Form or Style finding, which no run can show. No rule records it, and the
  checkers do not require one to.

The Incidents panel also lists, for each observation, the scenarios that produce it. Nobody
writes that list: the console runs every scenario headless when a scheme loads and records
what each one observes, so it cannot drift from the rules. "No scenario produces this yet"
means exactly that, and is a gap in the demonstrations rather than in the Act.

Each observation is stamped with the mode it arose in. **A finding a simulation arrives at is
better evidenced than one a scenario asserts**, because an asserted state may be one the rules
could never reach. Say so when reporting.

---

## `scenarios` — one-click demonstrations

```js
{ label: "… and reaches three months old", focus: "@pup", mode: "nature", steps: [
  { spawn: "dog", as: "pup", label: "Nipper",
    attrs: { bornDate: "2026-01-01", restrictedBreed: true, sterilised: false },
    rels: { owner: "p1", parent: "d1" } },
  { tick: 90 }
] }
```

Steps are `{ actor, action, target, params }`, `{ spawn, as, label, note, attrs, rels }`,
`{ tick: n }`, `{ set: actor, attrs, rels }` (a fact set by hand, God mode) or
`{ remove: actor, asEvent }`. `as` names an alias; `"@name"` refers back to it in later steps
and in `focus`. `mode: "nature"` runs the scenario in Nature mode; omit it for God mode.
`empty: true` starts it with nobody. Scenarios written in the console, and runs saved from a
simulation, are stored in the artifact's database in exactly this form.

---

## `simulation` — what happens of its own accord

```js
simulation: {
  params: [ { key: "dogsPerMonth", label: "Pups whelped per month", def: 4, min: 0, max: 60, step: 0.5 } ],
  generators: [
    { id: "residents", start: "$param.residents", spawn: { type: "person", label: "{name}", names: [...] } },
    { id: "whelp", rate: ["/", "$param.dogsPerMonth", 30], spawn: { type: "dog", attrs: {...}, rels: {...} } },
    { id: "register", per: "dog", when: [...], chance: 0.05,
      act: { action: "register", actor: ["any", "localgov"], target: "$self" } }
  ]
}
```

`params` are what the user sets in the Simulation panel; every default is illustrative, and
the panel says so. Rules and generators read them as `$param.key`. A parameter used only by
`start` generators is marked "at start".

A generator is one of: `{ start: n, spawn }` — n of these when a run begins; `{ rate: perDay,
spawn | act }` — about that many a day; `{ per: type, chance: p, act | remove }` — each actor of
the type, with chance p each day, bound as `$self`. `when` gates any of them. `act.actor`
and `act.target` are expressions: `"$self"`, `["rel", "$self", "owner"]`, or
`["any", "person", where]`, a random actor for which `where` holds with the candidate as
`$it`. Randomness comes only from `chance`, `randInt`, `oneOf` and `any`, all rolled from the
run's seed, so a seed replays its run.

**Generators may only act, spawn or remove — never set a fact.** That is what makes a
generated run count as Nature mode: a dog is registered because a local government
registers it. `check.js` generates a year for every scheme that has this section, checks the
seed replays it, and checks a saved run plays back to the same cast and day.

The Scenarios panel describes each scenario by outlining its steps (who does what to whom, and
how long the clock runs). Give it `description: "…"` to say something better in its place.

---

## Checking it

```bash
node tools/scheme-console/check.js
```

Runs every scenario of every scheme headless and reports:

- scenarios that throw, or whose `focus` resolves to nothing;
- observations tagged with the wrong mode;
- **conferred facts with no act that confers them**, and acts that never set what they claim to;
- **declared observations no rule can ever record** — usually a rule that got dropped;
- rules triggering on missing actions or types, actions with unknown actor or target types,
  relationships pointing at types that do not exist;
- creation exercised in both modes for every creatable type, aged 200 days and removed, with
  dangling relationships reported.

The provenance checks are the valuable ones, and they generalise past this console: a fact the
corpus reads but no provision can make true is a hole worth knowing about. `INCIDENTS.md` C-01
in the Dog Act subject is one found exactly this way.

Add a scheme, run the checker, and fix what it says before trusting anything the console tells
you.

`checker.js` is the same set of checks as one browser function, `checkScheme(scheme)`, which
returns a list of problems; with `{requireSimulation: true}` it also requires a `simulation`
section, checks each generator against the scheme, and gives it a ninety-day trial run at the
defaults.
Keep the two checkers in step when you add a check.

---

## No laws added from the page

The console once let a viewer upload a law and have Claude write a scheme from it. That route is
closed: the published console shows only laws encoded in L4 here, added by the five steps in
`README.md`. The upload code is still in `index.html` but nothing reaches it, and the
`laws` collection in the artifact's database is no longer read.
