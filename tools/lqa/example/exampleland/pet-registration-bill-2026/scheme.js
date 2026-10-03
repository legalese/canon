/* The console scheme for the LQA checker's worked example.
   FICTIONAL: Exampleland and its Pet Registration Bill do not exist. */
(function (global) {
  var PET_BILL = {
    id: "pet-bill",
    title: "Pet Registration Bill 2026",
    jurisdiction: "Exampleland (fictional)",
    status: "Print 1, as introduced · a fictional worked example",
    scope: "ss. 3–5, with the Interpretation Act 1990 ss. 12 and 20.",
    startDate: "2026-01-01",
    dayLabel: "Day",

    types: [
      { id: "council", label: "Council", band: 0, shape: "rect",
        create: { nameHint: "Exampleland Council", fields: [], rels: [] } },
      { id: "person", label: "Person", band: 1, shape: "rect",
        create: { nameHint: "Ana", fields: [], rels: [] } },
      { id: "pet", label: "Pet", band: 2, shape: "round",
        create: { nameHint: "Rex", bornVerb: "Born", fields: [
          { key: "bornDay", type: "age", origin: "birth", unit: "months", label: "Age in months", def: 6,
            cite: "s. 3(1)", note: "The duty attaches at three complete calendar months." },
          { key: "registered", type: "bool", origin: "conferred", by: "register", cite: "s. 4(1)", label: "Is registered" }
        ], rels: [
          { key: "owner", label: "Owned by", target: "person", required: true, origin: "innate", cite: "s. 2" },
          { key: "minder", label: "Minded by", target: "person", origin: "conferred", by: "mind", cite: "s. 3(2)" }
        ] } }
    ],

    relLabels: { owner: "owned by", minder: "minded by" },

    entities: [
      { id: "c1", type: "council", label: "Exampleland Council" },
      { id: "p1", type: "person", label: "Ana", note: "owner" },
      { id: "p2", type: "person", label: "Ben", note: "neighbour" },
      { id: "d1", type: "pet", label: "Rex", note: "unregistered",
        attrs: { bornDate: "2025-06-01", registered: false }, rels: { owner: "p1" } }
    ],

    defs: {
      toJune30: ["-", ["nextDate", 6, 30], "$day"]
    },

    actions: [
      { id: "register", actor: "council", target: "pet", label: "Grant the application to register the pet", cite: "s. 4(1)",
        log: "<b>{self}</b> grants the application to register <b>{target}</b>." },
      { id: "refuseToConsider", actor: "council", target: "pet", label: "Refuse to consider the application", cite: "s. 4(2)",
        log: "<b>{self}</b> refuses to consider the application to register <b>{target}</b>." },
      { id: "mind", actor: "person", target: "pet", label: "Take the pet in to mind it", cite: "s. 3(2)",
        log: "<b>{self}</b> takes <b>{target}</b> in to mind it." }
    ],

    rules: [
      { id: "grant", on: "action:register",
        then: [
          ["set", "$target.attrs.registered", true],
          ["set", "$target.attrs.regExpiryDay", ["nextDate", 6, 30]],
          ["set", "$target.attrs.regExpiryDate", ["date", ["nextDate", 6, 30]]],
          ["log", "{target} is registered until {target.attrs.regExpiryDate}, the next 30 June.", { cite: "ss. 4(1), 5", sev: "ok" }]
        ] },
      { id: "grant-short", on: "action:register", "if": ["<", ["def", "toJune30"], 31],
        then: [
          ["log", "<b>The registration lasts less than a month.</b> Section 5 ends every registration on the next 30 June, however late in the year it was granted, and nothing in the Bill reduces the fee.",
            { cite: "s. 5", sev: "warn" }],
          ["observe", "t02"]
        ] },
      { id: "rtc", on: "action:refuseToConsider",
        then: [
          ["log", "Section 4(2) lets the council refuse to consider an application, with no ground, no time and no consequence. Section 4(1) requires a grant only of an application the council considers, so the owner is left unable to comply with s. 3(1).",
            { cite: "s. 4", sev: "stop" }],
          ["observe", "p03"]
        ] },
      { id: "minded", on: "action:mind",
        then: [
          ["set", "$target.rels.minder", "$self.id"],
          ["log", "Section 3(2) speaks of “the person” who has kept the pet, and no person is introduced. Read as the owner, the duty to register {target} is unaffected; read as whoever has the pet now, it is suspended for 14 days.",
            { cite: "s. 3(2)", sev: "warn" }],
          ["observe", "r01"]
        ] },
      { id: "lapse", on: "day", "for": "pet",
        "if": ["and", "$self.attrs.registered", ["=", "$day", "$self.attrs.regExpiryDay"]],
        then: [
          ["set", "$self.attrs.registered", false],
          ["log", "{self}’s registration ends today.", { cite: "s. 5" }]
        ] },
      { id: "three-months", on: "day", "for": "pet",
        "if": ["and", ["=", ["ageMonths", "$self.attrs.bornDay"], 3], ["not", "$self.attrs.threeSeen"]],
        then: [
          ["set", "$self.attrs.threeSeen", true],
          ["log", "{self} has reached three complete calendar months, so the duty to register attaches today.",
            { cite: "s. 3(1); Interpretation Act 1990 s. 12", sev: "ok" }],
          ["observe", "t04"]
        ] }
    ],

    observations: [
      { id: "r01", ref: "R-01", foundBy: "ENC", sev: "warn", label: "“The person” in s. 3(2) has no antecedent",
        cite: "s. 3(2)", what: "A pet is minded by someone other than its owner.",
        why: "The exemption turns on how long “the person” has kept the pet. Nothing says whether that is the owner or whoever has the pet. OPEN." },
      { id: "t02", ref: "T-02", foundBy: "SIM", sev: "warn", label: "A registration granted in June lasts days",
        cite: "s. 5", what: "A pet is registered in the month before 30 June.",
        why: "Every registration ends on the next 30 June, so one granted on 20 June lasts ten days at a full fee. OPEN." },
      { id: "p03", ref: "P-03", foundBy: "ENC", sev: "stop", label: "The council may refuse to consider, without limit",
        cite: "s. 4(2)", what: "The council refuses to consider an application.",
        why: "No ground, no time, no consequence; the owner cannot then comply with s. 3(1). OPEN." },
      { id: "t04", ref: "T-04", foundBy: "ENC", sev: "ok", label: "When a pet reaches three months",
        cite: "s. 3(1); Interpretation Act 1990 s. 12", what: "A pet reaches three months of age.",
        why: "Whether “3 months” is calendar months or 90 days looked open. The Interpretation Act s. 12 answers it: complete calendar months. VERIFIED-NO-DEFECT." },
      { id: "s05", ref: "S-05", foundBy: "CMP", sev: "warn", static: true, label: "Section 5 uses “shall”",
        cite: "s. 5; Drafting Manual 3.1", what: "Read against the Drafting Manual.",
        why: "The Manual, para. 3.1: use “must”, never “shall”. OPEN, low." }
    ],

    scenarios: [
      { label: "Ben minds Rex for a week", focus: "d1", steps: [
        { actor: "p2", action: "mind", target: "d1" }
      ] },
      { label: "Rex is registered on 20 June", focus: "d1", steps: [
        { tick: 170 },
        { actor: "c1", action: "register", target: "d1" }
      ] },
      { label: "The council refuses to consider Rex’s application", focus: "d1", steps: [
        { actor: "c1", action: "refuseToConsider", target: "d1" }
      ] },
      { label: "Pip reaches three months", focus: "@pip", mode: "nature", steps: [
        { spawn: "pet", as: "pip", label: "Pip", attrs: { bornDate: "2026-01-01", registered: false }, rels: { owner: "p1" } },
        { tick: 90 }
      ] }
    ],

    simulation: {
      params: [
        { key: "residents", label: "People at the start", def: 10, min: 1, max: 60, step: 1 },
        { key: "startPets", label: "Pets at the start", def: 12, min: 0, max: 200, step: 1 },
        { key: "maxPets", label: "Most pets alive at once", def: 80, min: 1, max: 400, step: 1 },
        { key: "petsPerMonth", label: "Pets born per month", def: 2, min: 0, max: 40, step: 0.5 },
        { key: "pRegister", label: "Unregistered pets over three months registered per month", unit: "%", def: 30, min: 0, max: 100, step: 1 }
      ],
      generators: [
        { id: "council", start: ["if", ["=", ["count", "council"], 0], 1, 0], spawn: { type: "council", label: "Exampleland Council" } },
        { id: "residents", start: "$param.residents",
          spawn: { type: "person", label: "{name}", names: ["Ada", "Ben", "Cleo", "Dev", "Eve", "Finn", "Gia", "Hal", "Isla", "Jai"],
                   attrs: { resident: true } } },
        { id: "adult-pets", start: "$param.startPets",
          spawn: { type: "pet", label: "{name}", names: ["Rex", "Luna", "Milo", "Bella", "Oscar", "Coco"],
                   attrs: { bornDay: ["-", "$day", ["randInt", 100, 3000]], registered: false },
                   rels: { owner: ["any", "person", "$it.attrs.resident"] } } },
        { id: "births", rate: ["/", "$param.petsPerMonth", 30], when: ["<", ["count", "pet"], "$param.maxPets"],
          spawn: { type: "pet", label: "{name}", names: ["Pip", "Mochi", "Kiwi", "Dot", "Fudge", "Taco"],
                   attrs: { bornDay: "$day", registered: false },
                   rels: { owner: ["any", "person", "$it.attrs.resident"] } } },
        { id: "register", per: "pet",
          when: ["and", ["not", "$self.attrs.registered"], [">=", ["ageMonths", "$self.attrs.bornDay"], 3]],
          chance: ["/", "$param.pRegister", 3000],
          act: { action: "register", actor: ["any", "council"], target: "$self" } }
      ]
    }
  };

  global.SCHEMES = (global.SCHEMES || []).concat([PET_BILL]);
})(window);
