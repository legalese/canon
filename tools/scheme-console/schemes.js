/* ===========================================================================
   Scheme definitions. Data, not code.

   Four statutes, one engine. Nothing below is executable on its own: it is read
   by engine.js, which has never heard of a dog or a barring order. To model a
   fifth scheme, add a fifth object here and change nothing else.

   Every fact a type can hold declares where it came from:

     origin: "birth"      the date of birth. Age is worked out from it, never stored.
     origin: "innate"     true from the start, conferred by nobody.
     origin: "conferred"  becomes true only through an act; `by` names which one.
     origin: "exogenous"  settled outside this scheme, by some other body of law.

   That is what lets a scenario be written two ways. In God mode you author a
   state of the world and may assert anything. In Nature mode only what nature
   gives at birth, and what another Act settles, can be asserted; the rest has
   to be done by somebody, and age is worked out rather than stated.

   A scheme may also carry a `simulation` section: parameters the user sets,
   and generators — the things that happen of their own accord, and how often.
   In Simulation the app writes the scenario itself, in Nature mode's terms.
   =========================================================================== */
(function (global) {
  "use strict";

  /* ======================= Dog Act 1976 (WA) ============================ */

  var DOG_ACT = {
    id: "dog-act",
    title: "Dog Act 1976",
    jurisdiction: "Western Australia",
    status: "In force · compilation 08-b0-00, 28 Nov 2024",
    scope: "s. 3 (terms used); s. 7 and Pt III Div 1 (registration, and its 31 October expiry); Pt III Div 2 (microchipping, and notices on transfer); s. 11A (authorised persons); s. 29 (seizure, impounding, notice, holding periods, reclaim and destruction); s. 31 (dogs in public places); s. 33D (dog attacks); s. 33E(1) (declaration); ss. 33GB–33GC (sterilisation and transfer); s. 38 (nuisance orders); ss. 39–40 (destruction orders); s. 46 (damages).",
    startDate: "2026-01-01",
    dayLabel: "Day",

    types: [
      { id: "localgov", label: "Local government", band: 0, shape: "rect",
        create: { nameHint: "Shire of Mundaring", fields: [], rels: [] } },

      { id: "court", label: "Court", band: 0, shape: "rect" },

      { id: "person", label: "Person", band: 1, shape: "rect",
        create: { nameHint: "Ada", bornVerb: "Born", fields: [
          { key: "bornDay", type: "age", origin: "birth", unit: "years",
            label: "Age in years", def: 34 },
          { key: "isVeterinarian", type: "bool", origin: "exogenous", cite: "s. 3",
            label: "Is a veterinarian, or acting on one’s behalf, in professional practice",
            note: "Settled by registration under another Act, so it is taken as given here." },
          { key: "isPoliceOfficer", type: "bool", origin: "exogenous", cite: "s. 3",
            label: "Is a police officer, or otherwise acting under a statutory duty",
            note: "Also settled elsewhere. A police officer may exercise an authorised person’s powers under s. 29 (s. 29(1a))." }
        ], rels: [
          { key: "authorisedBy", label: "Authorised person for", target: "localgov",
            origin: "conferred", by: "appoint", cite: "s. 11A",
            note: "Nobody is born an authorised person. The chief executive officer of a local government appoints them." }
        ] } },

      { id: "dog", label: "Dog", band: 2, shape: "round",
        create: { nameHint: "Scout", bornVerb: "Whelped", fields: [
          { key: "bornDay", type: "age", origin: "birth", unit: "months",
            label: "Age in months", def: 12 },
          { key: "breed", type: "choice", origin: "innate", label: "Breed", def: "Kelpie",
            cite: "Dog (Restricted Breeds) Regulations (No. 2) 2002 r. 3",
            note: "The first six are the breeds the Regulations list as restricted. The Act names none: it defers to the regulations (s. 3).",
            options: [
              { v: "Dogo Argentino", label: "Dogo Argentino — restricted, r. 3(a)" },
              { v: "Fila Brasileiro", label: "Fila Brasileiro — restricted, r. 3(b)" },
              { v: "Japanese tosa", label: "Japanese tosa — restricted, r. 3(c)" },
              { v: "American pit bull terrier", label: "American pit bull terrier — restricted, r. 3(d)" },
              { v: "Pit bull terrier", label: "Pit bull terrier — restricted, r. 3(e)" },
              { v: "Mix with a restricted breed", label: "A mix that includes one of these — s. 3, r. 3" },
              { v: "Kelpie", label: "Kelpie" },
              { v: "Labrador", label: "Labrador" },
              { v: "Poodle", label: "Poodle" },
              { v: "Another breed", label: "Another breed" } ] },
          { key: "restrictedBreed", type: "bool", origin: "innate", cite: "s. 3",
            label: "Is of a breed prescribed as restricted by the regulations",
            note: "Set automatically when the breed is one the Regulations list. Tick it yourself only for a breed caught by r. 3(f), whose import the Commonwealth prohibits absolutely." },
          { key: "commercialSecurity", type: "bool", origin: "exogenous", cite: "s. 3",
            label: "Is a commercial security dog",
            note: "A matter of how the dog is used and licensed, not of this Act." },
          { key: "declaredDangerous", type: "bool", origin: "conferred", by: "declare",
            cite: "s. 33E(1)", label: "Has been declared to be a dangerous dog" },
          { key: "sterilised", type: "bool", origin: "conferred", by: "sterilise",
            cite: "s. 33GB", label: "Is sterilised" },
          { key: "microchipped", type: "bool", origin: "conferred", by: "microchip",
            cite: "s. 21(2)", label: "Is microchipped" }
        ], rels: [
          { key: "owner", label: "Owned by", target: "person", required: true,
            origin: "innate", cite: "s. 3",
            note: "A dog has an owner from the moment it is whelped. Changing one afterwards is a transfer, which is an act." },
          { key: "registeredWith", label: "Registered with", target: "localgov",
            origin: "conferred", by: "register", cite: "Pt III Div 1" },
          { key: "parent", label: "Parent dog", target: "dog", origin: "innate", cite: "s. 33GC" }
        ] } }
    ],

    relLabels: { owner: "owned by", registeredWith: "registered with", parent: "parent",
                 authorisedBy: "authorised person for", previousOwner: "previously owned by" },

    /* ---------------------------------------------------------- simulation
       What happens in a district of its own accord. Every rate is a
       parameter the user sets, and every default is illustrative: there is
       no data behind them. Things happen only through acts — a dog is
       registered because a local government registers it — so a generated
       run obeys the same rules, and records the same way, as a scripted one. */
    simulation: {
      params: [
        { key: "residents", label: "People in the district at the start", def: 12, min: 1, max: 60, step: 1 },
        { key: "startDogs", label: "Dogs already in the district at the start", def: 25, min: 0, max: 200, step: 1,
          note: "Adult dogs of any age. Like the residents, they are simply there when the run begins; nothing about their registration or chipping is assumed." },
        { key: "maxDogs", label: "Most dogs alive at once", def: 60, min: 1, max: 400, step: 1,
          note: "A ceiling, so a long run cannot grow without limit." },
        { key: "dogsPerMonth", label: "Pups whelped per month", def: 4, min: 0, max: 60, step: 0.5 },
        { key: "pRestricted", label: "Pups of a restricted breed", unit: "%", def: 5, min: 0, max: 100, step: 1 },
        { key: "pCompliant", label: "Owners who keep up with registration, chipping and sterilisation", unit: "%", def: 80, min: 0, max: 100, step: 1 },
        { key: "pPupSold", label: "Pups sold before twelve weeks", unit: "%", def: 30, min: 0, max: 100, step: 1 },
        { key: "adultSalesPerYear", label: "Adult dogs sold, per dog per year", def: 0.05, min: 0, max: 1, step: 0.01 },
        { key: "pNotifyDb", label: "Sellers who tell the chip registry within 7 days", unit: "%", def: 60, min: 0, max: 100, step: 1 },
        { key: "pNotifyLg", label: "Sellers who tell the council within 28 days", unit: "%", def: 75, min: 0, max: 100, step: 1 },
        { key: "attacksPerYear", label: "Attacks per dog per year", def: 0.1, min: 0, max: 2, step: 0.01 },
        { key: "pOwnerVictim", label: "Attacks where the dog’s owner is the one attacked", unit: "%", def: 15, min: 0, max: 100, step: 1 },
        { key: "pInjury", label: "Attacks that cause injury", unit: "%", def: 40, min: 0, max: 100, step: 1 },
        { key: "atLargePerYear", label: "Times per dog per year it is found off the leash in public", def: 0.5, min: 0, max: 5, step: 0.05 },
        { key: "pEarlyDestruction", label: "Rangers who destroy an unclaimed dog before the holding period ends", unit: "%", def: 5, min: 0, max: 100, step: 1 },
        { key: "complaintsPerYear", label: "Barking complaints per dog per year", def: 0.15, min: 0, max: 2, step: 0.01 },
        { key: "pRelapse", label: "Dogs that bark again while a nuisance order runs", unit: "%", def: 30, min: 0, max: 100, step: 1 }
      ],
      generators: [
        /* ---- who is there when the run begins, if nobody is ---- */
        { id: "council", start: ["if", ["=", ["count", "localgov"], 0], 1, 0],
          spawn: { type: "localgov", label: "City of Belmont" } },
        { id: "court", start: ["if", ["=", ["count", "court"], 0], 1, 0],
          spawn: { type: "court", label: "Magistrates Court" } },
        { id: "vet", start: ["if", ["=", ["count", "person", "$it.attrs.isVeterinarian"], 0], 1, 0],
          spawn: { type: "person", label: "Dr {name}", names: ["Patel", "Okoro", "Lindqvist"], note: "veterinarian",
                   attrs: { bornDay: ["-", "$day", ["*", 365, ["randInt", 30, 60]]], isVeterinarian: true, isPoliceOfficer: false } } },
        { id: "ranger", start: ["if", ["=", ["count", "person", ["or", "$it.attrs.ranger", ["exists", "$it.rels.authorisedBy"]]], 0], 1, 0],
          spawn: { type: "person", label: "{name}", names: ["Sam Okafor", "Jess Tran"], note: "ranger",
                   attrs: { bornDay: ["-", "$day", ["*", 365, ["randInt", 25, 55]]], isVeterinarian: false, isPoliceOfficer: false, ranger: true } } },
        { id: "residents", start: "$param.residents",
          spawn: { type: "person", label: "{name}", note: "resident",
                   names: ["Ada", "Ben", "Chen", "Dee", "Eli", "Fay", "Gus", "Hana", "Ivo", "Jun", "Kai", "Lena",
                           "Mo", "Nia", "Omar", "Pia", "Quin", "Rui", "Sita", "Tom", "Uma", "Vic", "Wen", "Xan"],
                   attrs: { bornDay: ["-", "$day", ["*", 365, ["randInt", 20, 75]]], isVeterinarian: false,
                            isPoliceOfficer: false, resident: true } } },

        { id: "adult-dogs", start: "$param.startDogs",
          spawn: { type: "dog", label: "{name}",
                   names: ["Rex", "Betty", "Max", "Coco", "Buster", "Daisy", "Charlie", "Molly", "Toby", "Lola",
                           "Sam", "Rosie", "Harley", "Penny", "Zeus", "Ginger", "Ollie", "Holly", "Diesel", "Willow"],
                   attrs: { bornDay: ["-", "$day", ["randInt", 120, 3650]],
                            breed: ["if", ["chance", ["/", "$param.pRestricted", 100]], "Pit bull terrier",
                                    ["oneOf", "Kelpie", "Labrador", "Poodle", "Another breed"]],
                            restrictedBreed: false, commercialSecurity: false, declaredDangerous: false,
                            sterilised: false, microchipped: false,
                            compliant: ["chance", ["/", "$param.pCompliant", 100]] },
                   rels: { owner: ["any", "person", "$it.attrs.resident"] } } },

        /* a ranger is appointed by the local government — nobody is born one (s. 11A) */
        { id: "appoint", per: "person",
          when: ["and", "$self.attrs.ranger", ["not", ["exists", "$self.rels.authorisedBy"]]], chance: 1,
          act: { action: "appoint", actor: ["any", "localgov"], target: "$self" } },

        /* ---- pups ---- */
        { id: "whelp", rate: ["/", "$param.dogsPerMonth", 30],
          when: ["<", ["count", "dog"], "$param.maxDogs"],
          spawn: { type: "dog", label: "{name}",
                   names: ["Biscuit", "Nala", "Rusty", "Pepper", "Scout", "Milo", "Tilly", "Bear", "Ziggy", "Olive",
                           "Rocky", "Luna", "Bluey", "Maple", "Sox", "Ruby", "Duke", "Honey", "Jet", "Poppy"],
                   attrs: { bornDay: "$day",
                            breed: ["if", ["chance", ["/", "$param.pRestricted", 100]], "Pit bull terrier",
                                    ["oneOf", "Kelpie", "Labrador", "Poodle", "Another breed"]],
                            restrictedBreed: false, commercialSecurity: false, declaredDangerous: false,
                            sterilised: false, microchipped: false,
                            compliant: ["chance", ["/", "$param.pCompliant", 100]] },
                   rels: { owner: ["any", "person", "$it.attrs.resident"] } } },

        /* ---- a careful owner gets there, mostly in time ---- */
        { id: "chip", per: "dog",
          when: ["and", "$self.attrs.compliant", ["not", "$self.attrs.microchipped"], ["not", "$self.attrs.destroyed"],
                        [">=", ["daysSince", "$self.attrs.bornDay"], 45]], chance: 0.06,
          act: { action: "microchip", actor: ["any", "person", "$it.attrs.isVeterinarian"], target: "$self" } },
        { id: "register", per: "dog",
          when: ["and", "$self.attrs.compliant", ["not", ["exists", "$self.rels.registeredWith"]],
                        ["not", "$self.attrs.destroyed"], [">=", ["daysSince", "$self.attrs.bornDay"], 60]], chance: 0.05,
          act: { action: "register", actor: ["any", "localgov"], target: "$self", params: { period: "annual" } } },
        { id: "sterilise", per: "dog",
          when: ["and", "$self.attrs.compliant", "$self.attrs.restrictedBreed", ["not", "$self.attrs.sterilised"],
                        ["not", "$self.attrs.destroyed"], [">=", ["daysSince", "$self.attrs.bornDay"], 45]], chance: 0.06,
          act: { action: "sterilise", actor: ["any", "person", "$it.attrs.isVeterinarian"], target: "$self" } },

        /* ---- sales, and the notices that follow ---- */
        { id: "sell-pup", per: "dog",
          when: ["and", [">=", ["daysSince", "$self.attrs.bornDay"], 49], ["<", ["daysSince", "$self.attrs.bornDay"], 84],
                        ["not", ["exists", "$self.attrs.transferDay"]], ["not", "$self.attrs.destroyed"],
                        ["or", ["not", "$self.attrs.restrictedBreed"], ["not", "$self.attrs.compliant"]]],
          chance: ["/", "$param.pPupSold", 3500],
          act: { action: "takeOwnership",
                 actor: ["any", "person", ["and", "$it.attrs.resident", ["!=", "$it.id", "$self.rels.owner"]]], target: "$self" } },
        { id: "sell-adult", per: "dog",
          when: ["and", [">", ["daysSince", "$self.attrs.bornDay"], 365], ["not", "$self.attrs.destroyed"],
                        ["not", "$self.attrs.impounded"]],
          chance: ["/", "$param.adultSalesPerYear", 365],
          act: { action: "takeOwnership",
                 actor: ["any", "person", ["and", "$it.attrs.resident", ["!=", "$it.id", "$self.rels.owner"]]], target: "$self" } },
        { id: "notify-db", per: "dog",
          when: ["and", ["exists", "$self.attrs.transferDay"], ["=", ["daysSince", "$self.attrs.transferDay"], 3],
                        "$self.attrs.microchipped"],
          chance: ["/", "$param.pNotifyDb", 100],
          act: { action: "notifyDatabase", actor: ["rel", "$self", "previousOwner"], target: "$self" } },
        { id: "notify-db-late", per: "dog",
          when: ["and", ["exists", "$self.attrs.transferDay"], ["=", ["daysSince", "$self.attrs.transferDay"], 12],
                        "$self.attrs.microchipped", ["!=", "$self.attrs.dbNotifiedBy", "$self.rels.previousOwner"]],
          chance: 0.5,
          act: { action: "notifyDatabase", actor: ["rel", "$self", "previousOwner"], target: "$self" } },
        { id: "notify-lg", per: "dog",
          when: ["and", ["exists", "$self.attrs.transferDay"], ["=", ["daysSince", "$self.attrs.transferDay"], 14],
                        ["exists", "$self.rels.registeredWith"]],
          chance: ["/", "$param.pNotifyLg", 100],
          act: { action: "notifyLocalGov", actor: ["rel", "$self", "previousOwner"], target: "$self" } },

        /* ---- registration runs out on 31 October, and careful owners renew ---- */
        { id: "renew", per: "dog",
          when: ["and", "$self.attrs.compliant", ["exists", "$self.attrs.regExpiryDay"],
                        ["not", ["exists", "$self.rels.registeredWith"]], ["not", "$self.attrs.destroyed"]], chance: 0.08,
          act: { action: "register", actor: ["any", "localgov"], target: "$self", params: { period: "annual" } } },

        /* ---- attacks ---- */
        { id: "attack", per: "dog",
          when: ["and", [">", ["daysSince", "$self.attrs.bornDay"], 120], ["not", "$self.attrs.destroyed"],
                        ["not", "$self.attrs.impounded"]],
          chance: ["/", "$param.attacksPerYear", 365],
          act: { action: "attack", actor: "$self",
                 target: ["if", ["chance", ["/", "$param.pOwnerVictim", 100]], ["rel", "$self", "owner"],
                                ["any", "person", ["!=", "$it.id", "$self.rels.owner"]]],
                 params: { rushed: true, bit: ["chance", ["/", "$param.pInjury", 100]], injury: "$p.bit" } } },

        /* ---- the pound ---- */
        { id: "at-large", per: "dog",
          when: ["and", [">", ["daysSince", "$self.attrs.bornDay"], 120], ["not", "$self.attrs.destroyed"],
                        ["not", "$self.attrs.impounded"]],
          chance: ["/", "$param.atLargePerYear", 365],
          act: { action: "seize", actor: ["any", "person", ["exists", "$it.rels.authorisedBy"]], target: "$self",
                 params: { ground: "public" } } },
        { id: "notice", per: "dog",
          when: ["and", "$self.attrs.impounded", "$self.attrs.impoundIdentifiable", ["not", ["exists", "$self.attrs.noticeDay"]]],
          chance: 0.7,
          act: { action: "giveNotice", actor: ["any", "person", ["exists", "$it.rels.authorisedBy"]], target: "$self" } },
        { id: "reclaim", per: "dog",
          when: ["and", "$self.attrs.impounded", "$self.attrs.compliant"], chance: 0.4,
          act: { action: "reclaim", actor: ["rel", "$self", "owner"], target: "$self" } },
        { id: "destroy", per: "dog",
          when: ["and", "$self.attrs.impounded", ["def", "selfHoldRun"]], chance: 0.2,
          act: { action: "destroyImpounded", actor: ["any", "person", ["exists", "$it.rels.authorisedBy"]], target: "$self" } },
        { id: "destroy-early", per: "dog",
          when: ["and", "$self.attrs.impounded", ["not", ["def", "selfHoldRun"]], [">=", ["daysSince", "$self.attrs.impoundDay"], 1]],
          chance: ["/", "$param.pEarlyDestruction", 500],
          act: { action: "destroyImpounded", actor: ["any", "person", ["exists", "$it.rels.authorisedBy"]], target: "$self" } },
        { id: "gone", per: "dog", when: "$self.attrs.destroyed", chance: 1, remove: true },

        /* ---- barking ---- */
        { id: "complain", per: "dog",
          when: ["and", ["not", ["def", "nuisanceInForce"]], ["not", "$self.attrs.destroyed"],
                        [">", ["daysSince", "$self.attrs.bornDay"], 120]],
          chance: ["/", "$param.complaintsPerYear", 365],
          act: { action: "complain", actor: ["any", "person", ["and", "$it.attrs.resident", ["!=", "$it.id", "$self.rels.owner"]]],
                 target: "$self" } },
        { id: "nuisance-order", per: "dog",
          when: ["and", ["exists", "$self.attrs.complaintDay"],
                        ["or", ["not", ["exists", "$self.attrs.nuisanceOrderDay"]],
                               [">", "$self.attrs.complaintDay", "$self.attrs.nuisanceOrderDay"]]],
          chance: 0.3,
          act: { action: "nuisanceOrder", actor: ["any", "person", ["exists", "$it.rels.authorisedBy"]], target: "$self" } },
        { id: "quieten", per: "dog",
          when: ["and", ["def", "nuisanceInForce"], ["not", "$self.attrs.nuisanceStopped"],
                        [">=", ["daysSince", "$self.attrs.nuisanceOrderDay"], 7]],
          chance: 0.3,
          act: { action: "stopNuisance", actor: ["rel", "$self", "owner"], target: "$self" } },
        { id: "relapse", per: "dog",
          when: ["and", ["def", "nuisanceInForce"], "$self.attrs.nuisanceStopped"],
          chance: ["/", "$param.pRelapse", 15000],
          act: { action: "barkPersistently", actor: "$self" } }
      ]
    },

    scenarios: [
      { label: "Rex bites someone in the park", focus: "d1", steps: [
        { actor: "d1", action: "attack", target: "p2", params: { bit: true, injury: true } }
      ] },
      { label: "Rex bites John, who owns him", focus: "d1", steps: [
        { actor: "d1", action: "attack", target: "p1", params: { bit: true, injury: true } }
      ] },
      { label: "Betty rushes at someone teasing her", focus: "d2", steps: [
        { actor: "p2", action: "provoke", target: "d2" },
        { actor: "d2", action: "attack", target: "p2", params: { rushed: true } }
      ] },
      { label: "… and the same behaviour a day later", focus: "d2", steps: [
        { actor: "p2", action: "provoke", target: "d2" },
        { tick: 1 },
        { actor: "d2", action: "attack", target: "p2", params: { rushed: true } }
      ] },
      { label: "The bootstrapping attack", focus: "d2", steps: [
        { actor: "d2", action: "attack", target: "p2", params: { bit: true, injury: true } },
        { tick: 21 },
        { actor: "lg1", action: "declare", target: "d2" }
      ] },
      { label: "A shopkeeper tries to declare a dog dangerous", focus: "d2", steps: [
        { actor: "p2", action: "purportDeclare", target: "d2" }
      ] },
      { label: "A pup is whelped to a restricted-breed parent", focus: "@pup",
        mode: "nature", steps: [
        { spawn: "dog", as: "pup", label: "Nipper", note: "whelped today",
          attrs: { breed: "Pit bull terrier", bornDate: "2026-01-01", restrictedBreed: true,
                   commercialSecurity: false, declaredDangerous: false, sterilised: false },
          rels: { owner: "p1", parent: "d1" } }
      ] },
      { label: "… and reaches three months old", focus: "@pup",
        mode: "nature", steps: [
        { spawn: "dog", as: "pup", label: "Nipper", note: "whelped today",
          attrs: { breed: "Pit bull terrier", bornDate: "2026-01-01", restrictedBreed: true,
                   commercialSecurity: false, declaredDangerous: false, sterilised: false },
          rels: { owner: "p1", parent: "d1" } },
        { tick: 90 }
      ] },
      { label: "… unless someone registers and sterilises him", focus: "@pup",
        mode: "nature", steps: [
        { spawn: "dog", as: "pup", label: "Nipper", note: "whelped today",
          attrs: { breed: "Pit bull terrier", bornDate: "2026-01-01", restrictedBreed: true,
                   commercialSecurity: false, declaredDangerous: false, sterilised: false },
          rels: { owner: "p1", parent: "d1" } },
        { tick: 40 },
        { actor: "lg1", action: "register", target: "@pup" },
        { actor: "p3", action: "sterilise", target: "@pup" },
        { tick: 50 }
      ] },
      { label: "A puppy is sold at eight weeks, unchipped", focus: "@pup",
        mode: "nature", steps: [
        { spawn: "dog", as: "pup", label: "Biscuit", note: "kelpie pup",
          attrs: { breed: "Kelpie", bornDate: "2026-01-01", restrictedBreed: false,
                   commercialSecurity: false, declaredDangerous: false, sterilised: false, microchipped: false },
          rels: { owner: "p1" } },
        { tick: 56 },
        { actor: "p2", action: "takeOwnership", target: "@pup" }
      ] },
      { label: "Three months old, and nothing done", focus: "@pup",
        mode: "nature", steps: [
        { spawn: "dog", as: "pup", label: "Biscuit", note: "kelpie pup",
          attrs: { breed: "Kelpie", bornDate: "2026-01-01", restrictedBreed: false,
                   commercialSecurity: false, declaredDangerous: false, sterilised: false, microchipped: false },
          rels: { owner: "p1" } },
        { tick: 90 }
      ] },
      { label: "Betty is sold; the council is told, the chip registry is not", focus: "d2", steps: [
        { actor: "p2", action: "takeOwnership", target: "d2" },
        { tick: 5 },
        { actor: "p1", action: "notifyLocalGov", target: "d2" },
        { tick: 25 }
      ] },
      { label: "Registration runs out on 31 October", focus: "d2", steps: [
        { tick: 305 }
      ] },
      { label: "Seized in the park, destroyed two days after notice", focus: "d2", steps: [
        { actor: "p4", action: "seize", target: "d2", params: { ground: "public" } },
        { tick: 1 },
        { actor: "p4", action: "giveNotice", target: "d2" },
        { tick: 2 },
        { actor: "p4", action: "destroyImpounded", target: "d2" }
      ] },
      { label: "… or after a fortnight with no notice at all", focus: "d2", steps: [
        { actor: "p4", action: "seize", target: "d2", params: { ground: "public" } },
        { tick: 14 },
        { actor: "p4", action: "destroyImpounded", target: "d2" }
      ] },
      { label: "… or reclaimed by John", focus: "d2", steps: [
        { actor: "p4", action: "seize", target: "d2", params: { ground: "public" } },
        { actor: "p4", action: "giveNotice", target: "d2" },
        { tick: 2 },
        { actor: "p1", action: "reclaim", target: "d2" }
      ] },
      { label: "A ranger seizes a dog for being unregistered", focus: "@stray", steps: [
        { spawn: "dog", as: "stray", label: "Pepper", note: "labrador, never registered",
          attrs: { breed: "Labrador", bornDate: "2024-03-01", restrictedBreed: false,
                   commercialSecurity: false, declaredDangerous: false, sterilised: true, microchipped: true },
          rels: { owner: "p2" } },
        { actor: "p4", action: "seize", target: "@stray", params: { ground: "unregistered" } }
      ] },
      { label: "Barking again in month three of a nuisance order", focus: "d2", steps: [
        { actor: "p2", action: "complain", target: "d2" },
        { actor: "p4", action: "nuisanceOrder", target: "d2" },
        { tick: 14 },
        { actor: "p1", action: "stopNuisance", target: "d2" },
        { tick: 76 },
        { actor: "d2", action: "barkPersistently" }
      ] },
      { label: "A destruction order after the park bite", focus: "d1", steps: [
        { actor: "d1", action: "attack", target: "p2", params: { bit: true, injury: true } },
        { tick: 14 },
        { actor: "c1", action: "orderDestruction", target: "d1" }
      ] }
    ],

    entities: [
      { id: "lg1", type: "localgov", label: "City of Belmont" },
      { id: "c1", type: "court", label: "Magistrates Court" },
      { id: "p4", type: "person", label: "Sam Okafor", note: "ranger",
        attrs: { bornDate: "1988-08-14", isVeterinarian: false, isPoliceOfficer: false },
        rels: { authorisedBy: "lg1" } },
      { id: "p1", type: "person", label: "John", note: "owner",
        attrs: { bornDate: "1984-05-12", isVeterinarian: false, isPoliceOfficer: false } },
      { id: "p2", type: "person", label: "Mei", note: "in the park",
        attrs: { bornDate: "1991-11-03", isVeterinarian: false, isPoliceOfficer: false } },
      { id: "p3", type: "person", label: "Dr Patel", note: "veterinarian",
        attrs: { bornDate: "1979-02-20", isVeterinarian: true, isPoliceOfficer: false } },
      { id: "d1", type: "dog", label: "Rex", note: "pit bull terrier",
        attrs: { breed: "Pit bull terrier", bornDate: "2023-07-01", restrictedBreed: true,
                 declaredDangerous: false, commercialSecurity: false, sterilised: true,
                 microchipped: true, regExpiryDay: 303 },
        rels: { owner: "p1", registeredWith: "lg1" } },
      { id: "d2", type: "dog", label: "Betty", note: "poodle",
        attrs: { breed: "Poodle", bornDate: "2022-01-15", restrictedBreed: false,
                 declaredDangerous: false, commercialSecurity: false, sterilised: true,
                 microchipped: true, regExpiryDay: 303 },
        rels: { owner: "p1", registeredWith: "lg1" } }
    ],

    defs: {
      dangerous: ["or", "$self.attrs.declaredDangerous",
                        "$self.attrs.restrictedBreed",
                        "$self.attrs.commercialSecurity"],
      limb: ["or", "$p.rushed", "$p.bit", "$p.tore", "$p.feared"],
      provokedToday: ["and", ["exists", "$self.attrs.provokedDay"],
                             ["=", ["daysSince", "$self.attrs.provokedDay"], 0]],
      provocation: ["or", "$p.provoked", ["def", "provokedToday"]],
      isAttack: ["if", ["def", "provocation"], false,
                       ["and", ["def", "limb"], ["not", "$p.reasonableCause"]]],
      attackOrChase: ["or", ["def", "isAttack"], "$p.chased"],
      ownerIsVictim: ["=", "$target.id", "$self.rels.owner"],
      ageMonths: ["ageMonths", "$self.attrs.bornDay"],
      parentRestricted: ["attrOf", ["rel", "$self", "parent"], "restrictedBreed"],
      isRestrictedPup: ["and", ["def", "parentRestricted"], ["<", ["def", "ageMonths"], 3]],
      sterilisationDue: ["and", "$self.attrs.restrictedBreed",
                                ["not", "$self.attrs.sterilised"],
                                [">=", ["def", "ageMonths"], 3]],

      /* Dog (Restricted Breeds) Regulations (No. 2) 2002 r. 3(a)–(e), and a mix (s. 3(b) of the Act) */
      breedListed: ["or", ["=", "$self.attrs.breed", "Dogo Argentino"], ["=", "$self.attrs.breed", "Fila Brasileiro"],
                          ["=", "$self.attrs.breed", "Japanese tosa"], ["=", "$self.attrs.breed", "American pit bull terrier"],
                          ["=", "$self.attrs.breed", "Pit bull terrier"], ["=", "$self.attrs.breed", "Mix with a restricted breed"]],

      /* the dog as target — for acts done to a dog by a person, a court or a local government */
      tDangerous: ["or", "$target.attrs.declaredDangerous", "$target.attrs.restrictedBreed",
                         "$target.attrs.commercialSecurity"],
      tMonths: ["ageMonths", "$target.attrs.bornDay"],
      tRegistered: ["exists", "$target.rels.registeredWith"],
      tIdentifiable: ["or", ["def", "tRegistered"], "$target.attrs.microchipped"],

      /* s. 11A, s. 29(1a): who holds the seizure powers */
      selfAuthorised: ["or", ["exists", "$self.rels.authorisedBy"], "$self.attrs.isPoliceOfficer"],

      /* s. 29(8): at least 7 days after notice if identifiable, at least 72 hours after
         detention if not. A day counter reads 72 hours as three days. */
      tHoldRun: ["if", "$target.attrs.impoundIdentifiable",
                   ["and", ["exists", "$target.attrs.noticeDay"],
                           [">=", ["daysSince", "$target.attrs.noticeDay"], 7]],
                   [">=", ["daysSince", "$target.attrs.impoundDay"], 3]],
      selfHoldRun: ["if", "$self.attrs.impoundIdentifiable",
                   ["and", ["exists", "$self.attrs.noticeDay"],
                           [">=", ["daysSince", "$self.attrs.noticeDay"], 7]],
                   [">=", ["daysSince", "$self.attrs.impoundDay"], 3]],

      selfIsPreviousOwner: ["=", "$self.id", "$target.rels.previousOwner"],
      selfIsOwner: ["=", "$self.id", "$target.rels.owner"],

      /* s. 38(4): an order has effect for 6 months after the day it is issued */
      nuisanceInForce: ["and", ["exists", "$self.attrs.nuisanceOrderDay"],
                               ["<", ["ageMonths", "$self.attrs.nuisanceOrderDay"], 6]]
    },

    actions: [
      { id: "attack", actor: "dog", target: "person",
        label: "Attack or chase a person", cite: "s. 33D",
        log: "An incident involving <b>{self}</b> and <b>{target}</b>.",
        params: [
          { key: "rushed", label: "aggressively rushed at or harassed them" },
          { key: "bit", label: "bit, or otherwise caused physical injury" },
          { key: "tore", label: "tore clothing or damaged property" },
          { key: "feared", label: "attempted to attack, or would make a reasonable person fear injury" },
          { key: "chased", label: "chased them" },
          { key: "injury", label: "physical injury was caused", emph: true },
          { key: "provoked", label: "the behaviour was an immediate response to, and induced by, provocation" },
          { key: "reasonableCause", label: "the owner establishes the behaviour was justified by a reasonable cause" }
        ] },
      { id: "provoke", actor: "person", target: "dog",
        label: "Tease, torment or abuse the dog", cite: "s. 3 ‘provocation’",
        log: "<b>{self}</b> teases <b>{target}</b>." },
      { id: "declare", actor: "localgov", target: "dog",
        label: "Declare the dog to be dangerous", cite: "s. 33E(1)",
        log: "<b>{self}</b> declares <b>{target}</b> to be a dangerous dog." },
      { id: "purportDeclare", actor: "person", target: "dog",
        label: "Purport to declare the dog dangerous", cite: "s. 33E(1)",
        log: "<b>{self}</b> purports to declare <b>{target}</b> a dangerous dog." },
      { id: "register", actor: "localgov", target: "dog",
        label: "Register the dog", cite: "Pt III Div 1",
        log: "<b>{self}</b> registers <b>{target}</b>.",
        params: [
          { key: "period", type: "choice", label: "For how long?", options: [
            { v: "annual", label: "to the next 31 October — s. 15(2)(c)" },
            { v: "lifetime", label: "for the dog’s lifetime — s. 15(2)(b)" } ] }
        ] },
      { id: "microchip", actor: "person", target: "dog",
        label: "Implant a microchip", cite: "s. 21(2)",
        log: "<b>{self}</b> implants a microchip in <b>{target}</b>." },
      { id: "notifyDatabase", actor: "person", target: "dog",
        label: "Tell the microchip database of the new owner", cite: "s. 26C",
        log: "<b>{self}</b> notifies the microchip database company about <b>{target}</b>." },
      { id: "notifyLocalGov", actor: "person", target: "dog",
        label: "Tell the local government of the new owner", cite: "s. 16A(1)",
        log: "<b>{self}</b> notifies the local government of <b>{target}</b>’s new owner." },
      { id: "appoint", actor: "localgov", target: "person",
        label: "Appoint as an authorised person", cite: "s. 11A",
        log: "<b>{self}</b> appoints <b>{target}</b> as an authorised person." },
      { id: "seize", actor: "person", target: "dog",
        label: "Seize and impound the dog", cite: "s. 29(3)",
        log: "<b>{self}</b> seizes <b>{target}</b>.",
        params: [
          { key: "ground", type: "choice", label: "On what ground?", options: [
            { v: "public", label: "in a public place without being held on a leash — s. 29(3)(ca), s. 31" },
            { v: "attack", label: "an attack has occurred or is likely — s. 29(3)(a), (b)" },
            { v: "unregistered", label: "not registered — s. 29(3)(c)(ii)" } ] }
        ] },
      { id: "giveNotice", actor: "person", target: "dog",
        label: "Give the owner notice of the impounding", cite: "s. 29(8)(a)",
        log: "<b>{self}</b> gives notice to <b>{target}</b>’s owner." },
      { id: "reclaim", actor: "person", target: "dog",
        label: "Reclaim the dog from the pound", cite: "s. 29(8), (9)",
        log: "<b>{self}</b> comes to reclaim <b>{target}</b>." },
      { id: "destroyImpounded", actor: "person", target: "dog",
        label: "Cause the impounded dog to be destroyed", cite: "s. 29(10)",
        log: "<b>{self}</b> causes <b>{target}</b> to be destroyed." },
      { id: "complain", actor: "person", target: "dog",
        label: "Complain that the dog is a nuisance", cite: "s. 38(2)",
        log: "<b>{self}</b> lodges a complaint that <b>{target}</b> is a nuisance." },
      { id: "nuisanceOrder", actor: "person", target: "dog",
        label: "Issue a nuisance order", cite: "s. 38(3)",
        log: "<b>{self}</b> issues a nuisance order about <b>{target}</b>." },
      { id: "stopNuisance", actor: "person", target: "dog",
        label: "Stop the barking", cite: "s. 38(5)",
        log: "<b>{self}</b> stops <b>{target}</b>’s barking." },
      { id: "barkPersistently", actor: "dog",
        label: "Bark persistently", cite: "s. 38(1)(a)",
        log: "<b>{self}</b> barks, persistently, to a degree that unreasonably interferes with the neighbours’ peace." },
      { id: "orderDestruction", actor: "court", target: "dog",
        label: "Order the dog destroyed", cite: "ss. 39(1), 40",
        log: "<b>{self}</b> hears an application for an order that <b>{target}</b> be destroyed." },
      { id: "sterilise", actor: "person", target: "dog",
        label: "Sterilise the dog", cite: "s. 33GB" },
      { id: "takeOwnership", actor: "person", target: "dog",
        label: "Take ownership of the dog", cite: "s. 33GC" }
    ],

    rules: [
      /* ---------------------------------------------------------- attacks */
      { id: "provocation-carveout", on: "action:attack",
        "if": ["def", "provocation"],
        then: [
          ["log", "Not an attack. Section 3 excludes behaviour that was an immediate response to, and induced by, provocation, and on the reading this encoding takes that carve-out is categorical — it is not reopened by the ‘unless … reasonable cause’ words that close the definition.",
            { cite: "s. 3 ‘attack’", sev: "ok" }],
          ["observe", "fork-provocation"]
        ] },

      { id: "reasonable-cause", on: "action:attack",
        "if": ["and", ["not", ["def", "provocation"]], ["def", "limb"], "$p.reasonableCause"],
        then: [["log", "Not an attack. The owner establishes that the behaviour was justified by a reasonable cause, which takes it outside the (a)–(d) inclusions.",
          { cite: "s. 3 ‘attack’", sev: "ok" }]] },

      { id: "is-attack", on: "action:attack",
        "if": ["def", "isAttack"],
        then: [["log", "<b>{self} attacks {target}.</b>", { cite: "s. 3 ‘attack’" }]] },

      { id: "record-incident", on: "action:attack",
        "if": ["def", "attackOrChase"],
        then: [
          ["set", "$self.attrs.offenceDay", "$day"],
          ["set", "$self.attrs.offenceDangerous", ["def", "dangerous"]],
          ["set", "$self.attrs.offenceInjury", "$p.injury"]
        ] },

      { id: "s33D1", on: "action:attack",
        "if": ["and", ["def", "attackOrChase"], "$p.injury"],
        then: [["log", "Offence under s. 33D(1). The dog attacked or chased {target} and caused physical injury, so the owner and every other person liable for the control of the dog commits an offence.",
          { cite: "s. 33D(1)" }]] },

      { id: "s33D1-penalty-dangerous", on: "action:attack",
        "if": ["and", ["def", "attackOrChase"], "$p.injury", ["def", "dangerous"]],
        then: [["log", "{self} is a dangerous dog, so the penalty is a fine of not more than $20,000 and not less than $1,000.",
          { cite: "s. 33D(1) Penalty" }]] },

      { id: "s33D1-penalty-ordinary", on: "action:attack",
        "if": ["and", ["def", "attackOrChase"], "$p.injury", ["not", ["def", "dangerous"]]],
        then: [["log", "{self} is not a dangerous dog, so the penalty is a fine of not more than $10,000, with no minimum.",
          { cite: "s. 33D(1) Penalty" }]] },

      { id: "s33D2A", on: "action:attack",
        "if": ["and", ["def", "attackOrChase"], ["not", "$p.injury"]],
        then: [["log", "Offence under s. 33D(2A). The same conduct, without physical injury.",
          { cite: "s. 33D(2A)" }]] },

      { id: "s33D2A-penalty-dangerous", on: "action:attack",
        "if": ["and", ["def", "attackOrChase"], ["not", "$p.injury"], ["def", "dangerous"]],
        then: [["log", "Dangerous dog, no injury: a fine of not more than $10,000.",
          { cite: "s. 33D(2A) Penalty" }]] },

      { id: "s33D2A-penalty-ordinary", on: "action:attack",
        "if": ["and", ["def", "attackOrChase"], ["not", "$p.injury"], ["not", ["def", "dangerous"]]],
        then: [["log", "Not a dangerous dog, no injury: a fine of not more than $3,000.",
          { cite: "s. 33D(2A) Penalty" }]] },

      { id: "owner-is-victim", on: "action:attack",
        "if": ["and", ["def", "attackOrChase"], ["def", "ownerIsVictim"]],
        then: [
          ["log", "<b>The person attacked is {target}, who owns {self}.</b> Section 33D(1) makes every person liable for the control of the dog guilty, and s. 3 puts the registered owner squarely in that class. Nothing in either provision takes the owner out of it when the owner is the one who was bitten — so the owner commits the offence, and is liable to the fine, for being attacked by their own dog.",
            { cite: "ss. 3, 33D(1)", sev: "stop" }],
          ["observe", "owner-victim"]
        ] },

      { id: "victim-is-vet", on: "action:attack",
        "if": ["and", ["def", "attackOrChase"], "$target.attrs.isVeterinarian"],
        then: [["log", "{target} is a veterinarian acting in professional practice. That does not touch the offence — it takes them out of the class of persons <i>liable for the control of</i> the dog under s. 3, which is a different question from whether they were attacked.",
          { cite: "s. 3" }]] },

      { id: "destruction", on: "action:attack",
        "if": ["and", ["def", "attackOrChase"], "$p.injury", ["def", "dangerous"]],
        then: [
          ["log", "A dangerous dog has caused physical injury. Part VII allows a destruction order to be sought, and not only by the owner.",
            { cite: "Pt VII", sev: "warn" }],
          ["observe", "destruction"]
        ] },

      { id: "damages", on: "action:attack",
        "if": ["and", ["def", "attackOrChase"], "$p.injury", ["not", ["def", "ownerIsVictim"]]],
        then: [["log", "{self}’s owner is also liable to {target} in damages, subject to any contributory negligence. {target} does not have to show that {self} had a previous mischievous propensity, that the owner knew of one, or that the owner was negligent.",
          { cite: "s. 46(2), (3)" }]] },

      { id: "provoke-now", on: "action:provoke",
        then: [
          ["set", "$target.attrs.provokedDay", "$day"],
          ["log", "{target} has been provoked <b>today</b>. Behaviour that is an immediate response to this falls outside ‘attack’ — but only while it is immediate. Step the clock forward a day and the same behaviour is an attack again.",
            { cite: "s. 3 ‘provocation’", sev: "ok" }]
        ] },

      /* ---------------------------------------- conferring and purporting */
      { id: "declare-dangerous", on: "action:declare",
        then: [
          ["set", "$target.attrs.declaredDangerous", true],
          ["log", "{target} is a dangerous dog from now on, for every purpose in the Act.",
            { cite: "ss. 3, 33E(1)" }]
        ] },

      { id: "purport-declare-void", on: "action:purportDeclare",
        then: [
          ["log", "<b>Nothing has happened.</b> Section 33E(1) confers the power to declare a dog dangerous on the local government, and on nobody else. {self} is not a local government, so the purported declaration is a nullity — not an offence, not an irregularity, simply of no effect. {target} is exactly as dangerous, in law, as it was a moment ago.",
            { cite: "s. 33E(1)", sev: "ok" }],
          ["observe", "void-act"]
        ] },

      { id: "bootstrapping-attack", on: "action:declare",
        "if": ["and", ["exists", "$target.attrs.offenceDay"],
                      ["not", "$target.attrs.offenceDangerous"],
                      "$target.attrs.offenceInjury"],
        then: [
          ["log", "<b>The bootstrapping attack.</b> {target} committed a s. 33D(1) offence on day {target.attrs.offenceDay}, when it was not a dangerous dog \u2014 and today\u2019s declaration is the consequence of that very attack. Read the dog\u2019s status <i>at the time of the offence</i> and the maximum is $10,000 with no minimum. Read it <i>at the time of prosecution</i> and it is $20,000 with a $1,000 minimum. The section fixes the penalty by the dog\u2019s status without ever saying which moment to read it at.",
            { cite: "s. 33D(1) Penalty", sev: "stop" }],
          ["observe", "bootstrap"]
        ] },

      { id: "do-register", on: "action:register",
        then: [
          ["set", "$target.rels.registeredWith", "$self.id"],
          ["set", "$target.attrs.regLifetime", ["and", ["=", "$p.period", "lifetime"], ["not", ["def", "tDangerous"]]]],
          ["set", "$target.attrs.regExpiryDay", ["nextDate", 10, 31]],
          ["set", "$target.attrs.regExpiryDate", ["date", ["nextDate", 10, 31]]],
          ["log", "{target} is on the register, which is what ties it to a local government for the rest of the Act.",
            { cite: "Pt III Div 1", sev: "ok" }]
        ] },

      { id: "register-annual", on: "action:register", "if": ["not", "$target.attrs.regLifetime"],
        then: [["log", "The registration has effect until {target.attrs.regExpiryDate} — the next 31 October — unless cancelled sooner.",
          { cite: "s. 15(2)(c), (3A)" }]] },

      { id: "register-lifetime", on: "action:register", "if": "$target.attrs.regLifetime",
        then: [["log", "Registered for the dog’s lifetime: it has effect until {target}’s death, unless cancelled sooner.",
          { cite: "s. 15(2)(b)" }]] },

      { id: "register-dangerous-lifetime", on: "action:register",
        "if": ["and", ["=", "$p.period", "lifetime"], ["def", "tDangerous"]],
        then: [["log", "{target} is a dangerous dog, so it cannot be registered for its lifetime. A dangerous dog’s registration runs only to the next 31 October.",
          { cite: "s. 15(3A)", sev: "warn" }]] },

      { id: "register-unchipped", on: "action:register",
        "if": ["and", [">=", ["def", "tMonths"], 3], ["not", "$target.attrs.microchipped"]],
        then: [["log", "{target} is over three months old and not microchipped. That is a ground on which the local government may refuse or cancel registration; here it registers the dog anyway.",
          { cite: "s. 16(3)(da)", sev: "warn" }]] },

      { id: "do-sterilise-by-vet", on: "action:sterilise",
        "if": "$self.attrs.isVeterinarian",
        then: [
          ["set", "$target.attrs.sterilised", true],
          ["set", "$target.attrs.sterilisationFlagged", true],
          ["log", "{self} sterilises {target}, so the s. 33GB(1) duty is satisfied and cannot be broken later.",
            { cite: "s. 33GB(1)", sev: "ok" }]
        ] },

      { id: "do-sterilise-not-vet", on: "action:sterilise",
        "if": ["not", "$self.attrs.isVeterinarian"],
        then: [["log", "{self} is not a veterinarian. Section 33GB requires the dog to be sterilised and says nothing about who does it, but the procedure is regulated elsewhere — so nothing happens here.",
          { cite: "s. 33GB", sev: "warn" }]] },

      /* recorded first: every other transfer rule reads who the transferor was */
      { id: "transfer-record", on: "action:takeOwnership",
        then: [
          ["set", "$target.rels.previousOwner", "$target.rels.owner"],
          ["set", "$target.attrs.transferDay", "$day"],
          ["set", "$target.attrs.dbNotifiedBy", ""],
          ["set", "$target.attrs.lgNotifiedBy", ""],
          ["after", 8, "transfer-db-overdue"],
          ["after", 29, "transfer-lg-overdue"]
        ] },

      { id: "transfer-unchipped-pup", on: "action:takeOwnership",
        "if": ["and", ["not", "$target.attrs.microchipped"], ["<", ["def", "tMonths"], 3]],
        then: [
          ["log", "<b>{target} is not microchipped, so whoever transferred it commits an offence</b> — s. 26B(1), a fine of $5,000, unless satisfied that a vet’s exemption certificate applies. None can: a certificate “cannot apply in respect of a dog that is under 3 months of age” (s. 21(5)). Yet the duty to microchip does not arise until the dog “has reached 3 months of age” (s. 21(2)). So a pup can be sold lawfully only if it is chipped earlier than the Act requires.",
            { cite: "ss. 21(2), 21(5), 26B(1)", sev: "stop" }],
          ["observe", "unchipped-pup"]
        ] },

      { id: "transfer-unchipped", on: "action:takeOwnership",
        "if": ["and", ["not", "$target.attrs.microchipped"], [">=", ["def", "tMonths"], 3]],
        then: [["log", "{target} is not microchipped, so whoever transferred it commits an offence unless satisfied that a vet’s exemption certificate applies. A fine of $5,000.",
          { cite: "s. 26B(1)", sev: "stop" }]] },

      { id: "transfer-notices", on: "action:takeOwnership",
        "if": ["and", "$target.attrs.microchipped", ["not", ["def", "tDangerous"]], ["def", "tRegistered"]],
        then: [["log", "Two notices are now due from the person who transferred {target}: to the microchip database company within <b>7 days</b> (s. 26C), and to the local government within <b>28 days</b> (s. 16A(1)). Each carries a fine of $5,000.",
          { cite: "ss. 16A(1), 26C" }]] },

      { id: "transfer-db-overdue", on: "scheduled",
        "if": ["and", "$target.attrs.microchipped",
                      ["!=", "$target.attrs.dbNotifiedBy", "$target.rels.previousOwner"]],
        then: [
          ["log", "Seven days have passed since {target} changed hands and the person who transferred it has not told the microchip database company. Offence under s. 26C, a fine of $5,000 — whatever has been done about the local government’s 28 days.",
            { cite: "s. 26C", sev: "stop" }],
          ["observe", "two-clocks"]
        ] },

      { id: "transfer-lg-overdue", on: "scheduled",
        "if": ["and", ["not", ["def", "tDangerous"]], ["def", "tRegistered"],
                      ["!=", "$target.attrs.lgNotifiedBy", "$target.rels.previousOwner"]],
        then: [["log", "Twenty-eight days have passed and the registered owner has not told the local government who now owns {target}. Offence under s. 16A(1), a fine of $5,000.",
          { cite: "s. 16A(1)", sev: "stop" }]] },

      { id: "notify-db", on: "action:notifyDatabase",
        then: [
          ["set", "$target.attrs.dbNotifiedBy", "$self.id"],
          ["log", "The database company is told the new owner’s name and address.", { cite: "s. 26C" }]
        ] },

      { id: "notify-db-wrong-person", on: "action:notifyDatabase",
        "if": ["and", ["exists", "$target.rels.previousOwner"], ["not", ["def", "selfIsPreviousOwner"]]],
        then: [["log", "The duty is on “the person who effected the transfer”. {self} is not that person, so this notice does not discharge it.",
          { cite: "s. 26C", sev: "warn" }]] },

      { id: "notify-lg", on: "action:notifyLocalGov",
        then: [
          ["set", "$target.attrs.lgNotifiedBy", "$self.id"],
          ["log", "The local government is told the new owner’s name and residential address.", { cite: "s. 16A(1)" }]
        ] },

      { id: "transfer-pup", on: "action:takeOwnership",
        "if": "$target.attrs.isPup",
        then: [
          ["log", "{target} is a restricted breed pup, so transferring its ownership is an offence under s. 33GC unless this is a deceased estate passing through an executor, the previous owner has been certified by a medical practitioner as incapable of caring for it, or the Minister has formed the view that extraordinary conditions justify it. None of those is recorded.",
            { cite: "s. 33GC(3)", sev: "stop" }],
          ["observe", "unlawful-transfer"]
        ] },

      { id: "transfer-do", on: "action:takeOwnership",
        then: [
          ["set", "$target.rels.owner", "$self.id"],
          ["log", "The transfer is effective either way: {target} now belongs to {self}. An unlawful transfer is still a transfer — the Act makes it an offence, not a nullity.",
            { cite: "s. 33GC" }]
        ] },

      /* --------------------------------------------------- microchipping */
      { id: "do-microchip", on: "action:microchip",
        then: [
          ["set", "$target.attrs.microchipped", true],
          ["log", "{target} is microchipped. The implanter must tell the database company within 7 days (s. 24), and the owner must tell the local government within 7 days unless the details go with a registration application (s. 23).",
            { cite: "ss. 23, 24", sev: "ok" }]
        ] },

      /* ------------------------------------------ authorised persons, s. 11A */
      { id: "do-appoint", on: "action:appoint",
        then: [
          ["set", "$target.rels.authorisedBy", "$self.id"],
          ["log", "{target} is now an authorised person for {self}, and may exercise the powers the Act gives authorised persons — among them seizure under s. 29 and nuisance orders under s. 38.",
            { cite: "s. 11A", sev: "ok" }]
        ] },

      /* ----------------------------------------------- seizure, s. 29(3) */
      { id: "seize-no-power", on: "action:seize", "if": ["not", ["def", "selfAuthorised"]],
        then: [
          ["log", "<b>Nothing has happened.</b> The power to seize a dog belongs to an authorised person, and to a police officer. {self} is neither, so {target} has not been seized in law, however it may look.",
            { cite: "s. 29(1a), (3)", sev: "ok" }],
          ["observe", "void-act"]
        ] },

      { id: "seize-unregistered-ordinary", on: "action:seize",
        "if": ["and", ["def", "selfAuthorised"], ["=", "$p.ground", "unregistered"], ["not", ["def", "tDangerous"]]],
        then: [
          ["log", "<b>Nothing has happened.</b> Being unregistered is a ground for seizure only in the case of a dangerous dog. {target} is not one, so it may not be seized for that reason — although its owner is committing an offence under s. 7(1).",
            { cite: "s. 29(3)(c)(ii)", sev: "ok" }],
          ["observe", "no-seize-unregistered"]
        ] },

      { id: "seize-do", on: "action:seize",
        "if": ["and", ["def", "selfAuthorised"], ["not", "$target.attrs.impounded"],
                      ["or", ["!=", "$p.ground", "unregistered"], ["def", "tDangerous"]]],
        then: [
          ["set", "$target.attrs.impounded", true],
          ["set", "$target.attrs.impoundDay", "$day"],
          ["set", "$target.attrs.impoundIdentifiable", ["def", "tIdentifiable"]],
          ["set", "$target.attrs.noticeDay", null],
          ["set", "$target.attrs.holdRunLogged", false],
          ["log", "{target} is seized and detained in a dog management facility.",
            { cite: "s. 29(3)(d), (6)" }]
        ] },

      { id: "seize-public-offence", on: "action:seize",
        "if": ["and", ["=", "$target.attrs.impoundDay", "$day"], ["=", "$p.ground", "public"], "$target.attrs.impounded"],
        then: [["log", "A dog in a public place must be held by someone capable of controlling it, on a leash. Every person liable for the control of {target} commits an offence: a fine of $5,000.",
          { cite: "s. 31(3)", sev: "stop" }]] },

      { id: "seize-identifiable", on: "action:seize",
        "if": ["and", ["=", "$target.attrs.impoundDay", "$day"], "$target.attrs.impounded", "$target.attrs.impoundIdentifiable"],
        then: [["log", "{target} is registered or microchipped, so its owner must be given notice “as soon as is practicable”, and it must be kept for at least <b>7 days after the notice</b>. Nothing says how late “as soon as practicable” may be.",
          { cite: "s. 29(8)(a), (b)" }]] },

      { id: "seize-unidentifiable", on: "action:seize",
        "if": ["and", ["=", "$target.attrs.impoundDay", "$day"], "$target.attrs.impounded", ["not", "$target.attrs.impoundIdentifiable"]],
        then: [["log", "{target} carries no tag or microchip, so it must be kept for at least <b>72 hours</b> from when the detention began.",
          { cite: "s. 29(8)(c)" }]] },

      { id: "notice-no-power", on: "action:giveNotice", "if": ["not", ["def", "selfAuthorised"]],
        then: [["log", "<b>Nothing has happened.</b> The notice is for the authorised person causing the dog to be detained to give.",
          { cite: "s. 29(8)(a)", sev: "ok" }], ["observe", "void-act"]] },

      { id: "notice-do", on: "action:giveNotice",
        "if": ["and", ["def", "selfAuthorised"], "$target.attrs.impounded", "$target.attrs.impoundIdentifiable"],
        then: [
          ["set", "$target.attrs.noticeDay", "$day"],
          ["set", "$target.attrs.holdUntilDate", ["date", ["+", "$day", 7]]],
          ["log", "Notice is given. {target} must now be kept until at least {target.attrs.holdUntilDate}.",
            { cite: "s. 29(8)(b)" }]
        ] },

      /* ------------------------------------------ reclaim, s. 29(4), (8), (9) */
      { id: "reclaim-not-owner", on: "action:reclaim",
        "if": ["and", "$target.attrs.impounded", ["not", ["def", "selfIsOwner"]]],
        then: [["log", "{self} cannot show ownership of {target}, or authority to take it, so the pound does not release it.",
          { cite: "s. 29(8)", sev: "warn" }]] },

      { id: "reclaim-unregistered", on: "action:reclaim",
        "if": ["and", "$target.attrs.impounded", ["def", "selfIsOwner"], ["not", ["def", "tRegistered"]]],
        then: [["log", "{target} is not registered, so {self} may be required to register it before it is released.",
          { cite: "s. 29(9)", sev: "warn" }]] },

      { id: "reclaim-do", on: "action:reclaim",
        "if": ["and", "$target.attrs.impounded", ["def", "selfIsOwner"]],
        then: [
          ["set", "$target.attrs.impounded", false],
          ["log", "{target} is released to {self} — on payment, if the local government requires it, of the cost of return and maintenance, the seizure and impounding charges, any unpaid fees, <b>and any penalties imposed on the owner for an offence</b>. Had the money not been paid, that alone would be a ground on which {target} could be destroyed (s. 29(10)(c)).",
            { cite: "s. 29(4)", sev: "warn" }],
          ["observe", "pay-to-reclaim"]
        ] },

      { id: "reclaim-nothing", on: "action:reclaim", "if": ["not", "$target.attrs.impounded"],
        then: [["log", "{target} is not being detained.", { cite: "s. 29", sev: "ok" }]] },

      /* ------------------------------------------ destruction, s. 29(10) */
      { id: "destroy-no-power", on: "action:destroyImpounded", "if": ["not", ["def", "selfAuthorised"]],
        then: [["log", "<b>Nothing lawful has happened.</b> The power to cause an impounded dog to be destroyed is an authorised person’s.",
          { cite: "s. 29(10)", sev: "ok" }], ["observe", "void-act"]] },

      { id: "destroy-not-held", on: "action:destroyImpounded",
        "if": ["and", ["def", "selfAuthorised"], ["not", "$target.attrs.impounded"]],
        then: [["log", "{target} is not seized and detained, so s. 29(10) does not reach it.",
          { cite: "s. 29(10)", sev: "ok" }]] },

      { id: "destroy-no-notice", on: "action:destroyImpounded",
        "if": ["and", ["def", "selfAuthorised"], "$target.attrs.impounded", "$target.attrs.impoundIdentifiable",
                      ["not", ["exists", "$target.attrs.noticeDay"]]],
        then: [
          ["set", "$target.attrs.daysHeld", ["daysSince", "$target.attrs.impoundDay"]],
          ["log", "<b>{target} has been held {target.attrs.daysHeld} days and its owner was never given notice.</b> The 7-day minimum in s. 29(8)(b) runs from the notice, so it has not begun. Section 29(10) lets an authorised person destroy a dog that “is not claimed”, and does not say it must first wait out the s. 29(8) period. Read together, the destruction is premature; read alone, s. 29(10) permits it. The corpus’s L4 encoding of s. 29(10) does not wait either.",
            { cite: "s. 29(8)(b), (10)", sev: "stop" }],
          ["observe", "early-destruction"]
        ] },

      { id: "destroy-early", on: "action:destroyImpounded",
        "if": ["and", ["def", "selfAuthorised"], "$target.attrs.impounded", ["not", ["def", "tHoldRun"]],
                      ["or", ["not", "$target.attrs.impoundIdentifiable"], ["exists", "$target.attrs.noticeDay"]]],
        then: [
          ["log", "<b>{target} is destroyed before its minimum holding period has run.</b> Section 29(8) says the dog “is to be kept and maintained” for that period; s. 29(10) gives the power to destroy an unclaimed dog without referring to it. Whether (10) waits on (8) is a question of reading, and the Act does not answer it in terms.",
            { cite: "s. 29(8), (10)", sev: "stop" }],
          ["observe", "early-destruction"]
        ] },

      { id: "destroy-do", on: "action:destroyImpounded",
        "if": ["and", ["def", "selfAuthorised"], "$target.attrs.impounded"],
        then: [
          ["set", "$target.attrs.impounded", false],
          ["set", "$target.attrs.destroyed", true],
          ["log", "{target} is destroyed. It could instead have been sold or otherwise disposed of, the proceeds going to the local government (s. 29(11)). The owner is liable for the cost (s. 29(15)).",
            { cite: "s. 29(10), (11), (15)" }]
        ] },

      /* ------------------------------------------------- nuisance, s. 38 */
      { id: "do-complain", on: "action:complain",
        then: [
          ["set", "$target.attrs.complaintDay", "$day"],
          ["log", "A complaint in the prescribed form is lodged with an authorised person, alleging that {target} is a nuisance.",
            { cite: "s. 38(2)" }]
        ] },

      { id: "order-no-power", on: "action:nuisanceOrder", "if": ["not", ["exists", "$self.rels.authorisedBy"]],
        then: [["log", "<b>Nothing has happened.</b> Only an authorised person may issue a nuisance order.",
          { cite: "s. 38(3)", sev: "ok" }], ["observe", "void-act"]] },

      { id: "order-no-complaint", on: "action:nuisanceOrder",
        "if": ["and", ["exists", "$self.rels.authorisedBy"], ["not", ["exists", "$target.attrs.complaintDay"]]],
        then: [["log", "An order follows a complaint, and none has been lodged about {target}. No order issues.",
          { cite: "s. 38(2), (3)", sev: "warn" }]] },

      { id: "order-do", on: "action:nuisanceOrder",
        "if": ["and", ["exists", "$self.rels.authorisedBy"], ["exists", "$target.attrs.complaintDay"]],
        then: [
          ["set", "$target.attrs.nuisanceOrderDay", "$day"],
          ["set", "$target.attrs.nuisanceStopped", false],
          ["log", "A nuisance order issues to the person liable for the control of {target}, requiring them to prevent the barking by a time it specifies. The order has effect for <b>6 months</b>, and they must comply with it throughout that period.",
            { cite: "s. 38(3), (4), (5)" }]
        ] },

      { id: "do-stop-nuisance", on: "action:stopNuisance",
        then: [
          ["set", "$target.attrs.nuisanceStopped", true],
          ["log", "The barking stops. The order is complied with — for now.", { cite: "s. 38(5)", sev: "ok" }]
        ] },

      { id: "bark-no-order", on: "action:barkPersistently",
        "if": ["not", ["exists", "$self.attrs.nuisanceOrderDay"]],
        then: [["log", "Persistent barking can make {self} a nuisance, but it is not an offence in itself. The offence comes only after a complaint, an order, and a failure to comply with the order.",
          { cite: "s. 38(1)–(5)", sev: "ok" }]] },

      { id: "bark-breach", on: "action:barkPersistently",
        "if": ["and", ["def", "nuisanceInForce"], ["not", "$self.attrs.nuisanceStopped"]],
        then: [["log", "The nuisance order is in force and has not been complied with. Offence under s. 38(5): a fine of $5,000 — or, for a dangerous dog, $10,000 with a minimum of $500.",
          { cite: "s. 38(5)", sev: "stop" }]] },

      { id: "bark-relapse", on: "action:barkPersistently",
        "if": ["and", ["def", "nuisanceInForce"], "$self.attrs.nuisanceStopped"],
        then: [
          ["set", "$self.attrs.nuisanceStopped", false],
          ["log", "<b>The barking is back, and the order is still in force.</b> Section 38(5) requires compliance “during the period in which it has effect”, so this is an offence: a fine of $5,000. The corpus’s L4 encoding would record no breach — it treats the duty as discharged once the barking was first prevented by the time the order specified.",
            { cite: "s. 38(4), (5)", sev: "stop" }],
          ["observe", "nuisance-relapse"]
        ] },

      { id: "bark-order-lapsed", on: "action:barkPersistently",
        "if": ["and", ["exists", "$self.attrs.nuisanceOrderDay"], ["not", ["def", "nuisanceInForce"]]],
        then: [["log", "The nuisance order lapsed six months after it issued. A fresh complaint and a fresh order are needed before this barking can found an offence.",
          { cite: "s. 38(4)", sev: "ok" }]] },

      /* ----------------------------------------- destruction orders, s. 39 */
      { id: "destruction-no-attack", on: "action:orderDestruction",
        "if": ["not", ["and", ["exists", "$target.attrs.offenceDay"], "$target.attrs.offenceInjury"]],
        then: [["log", "No attack by {target} has been shown to have caused injury or damage, so there is nothing on which a destruction order can be made.",
          { cite: "s. 39(1)", sev: "ok" }]] },

      { id: "destruction-order", on: "action:orderDestruction",
        "if": ["and", ["exists", "$target.attrs.offenceDay"], "$target.attrs.offenceInjury"],
        then: [
          ["set", "$target.attrs.destructionOrdered", true],
          ["log", "The court orders {target} destroyed. It may also order it seized and detained, and require the owner to take preventive steps and pay the costs of detention and destruction.",
            { cite: "ss. 39(1), (3), 40(1)" }],
          ["log", "The order must state the period within which it is to be put into effect. The Act sets no period of its own, so everything turns on what the court writes.",
            { cite: "s. 40(2)", sev: "warn" }]
        ] },

      /* ------------------------------------------------ coming into being */
      /* first among the creation rules: every other one reads restrictedBreed */
      { id: "breed-prescribed", on: "create:dog",
        "if": ["and", ["def", "breedListed"], ["not", "$self.attrs.restrictedBreed"]],
        then: [
          ["set", "$self.attrs.restrictedBreed", true],
          ["log", "{self} is a {self.attrs.breed}, a breed the Regulations list, so it is a dangerous dog (restricted breed) from the moment it exists.",
            { cite: "s. 3; Dog (Restricted Breeds) Regulations (No. 2) 2002 r. 3" }]
        ] },

      { id: "new-dog-past-three-months", on: "create:dog",
        "if": [">=", ["def", "ageMonths"], 3],
        then: [["set", "$self.attrs.threeMonthsSeen", true]] },

      { id: "new-dog-unchipped", on: "create:dog",
        "if": ["and", [">=", ["def", "ageMonths"], 3], ["not", "$self.attrs.microchipped"]],
        then: [["log", "{self} is over three months old and not microchipped, so its owner is committing an offence.",
          { cite: "s. 21(2)", sev: "stop" }]] },

      { id: "new-dog-pup-exempt", on: "create:dog",
        "if": ["and", ["not", ["exists", "$self.rels.registeredWith"]], ["<", ["def", "ageMonths"], 3]],
        then: [["log", "{self} is under three months old, so it need not be registered or microchipped yet. Both duties arrive together on its three-month birthday.",
          { cite: "ss. 7(3)(a), 21(2)", sev: "ok" }]] },

      { id: "new-dog-unregistered", on: "create:dog",
        "if": ["and", ["not", ["exists", "$self.rels.registeredWith"]], [">=", ["def", "ageMonths"], 3]],
        then: [
          ["log", "No local government has registered {self}. Part III Division 1 requires a dog to be registered, and registration is what ties it to a local government for everything that follows — including who may declare it dangerous.",
            { cite: "Pt III Div 1", sev: "warn" }],
          ["observe", "unregistered"]
        ] },

      { id: "new-dog-restricted", on: "create:dog",
        "if": "$self.attrs.restrictedBreed",
        then: [["log", "{self} is of a restricted breed, so it is a <b>dangerous dog</b> from the moment it is whelped — with no declaration, no incident, and nothing it has done. Every penalty in s. 33D is already at the higher rate.",
          { cite: "s. 3", sev: "warn" }]] },

      { id: "new-dog-pup", on: "create:dog",
        "if": ["def", "isRestrictedPup"],
        then: [
          ["set", "$self.attrs.isPup", true],
          ["log", "{self} is under three months old and has at least one parent that is a dangerous dog (restricted breed), so it is a <b>restricted breed pup</b>. Its ownership cannot be transferred except in the narrow cases s. 33GC allows: a deceased estate passing through an executor, an owner certified by a medical practitioner as incapable of caring for it, or the Minister forming the view, in his absolute discretion, that extraordinary conditions justify the transfer.",
            { cite: "s. 33GC", sev: "warn" }],
          ["observe", "pup"]
        ] },

      { id: "new-dog-sterilise", on: "create:dog",
        "if": ["and", ["def", "sterilisationDue"],
                      ["not", "$self.attrs.sterilisationFlagged"]],
        then: [
          ["set", "$self.attrs.sterilisationFlagged", true],
          ["log", "{self} is a dangerous dog (restricted breed) already past three months and not sterilised. Section 33GB(1) makes that an offence for the owner from the moment it is true.",
            { cite: "s. 33GB(1)", sev: "stop" }],
          ["observe", "sterilise"]
        ] },

      { id: "new-person-note", on: "create:person",
        then: [["log", "{self} is now someone the Act can speak about — as an owner, an occupier, a person with a dog under control, or a person a dog attacks.",
          { cite: "s. 3" }]] },

      /* -------------------------------------------------------- the clock */
      { id: "sterilise-due", on: "day", "for": "dog",
        "if": ["and", ["def", "sterilisationDue"],
                      ["not", "$self.attrs.sterilisationFlagged"]],
        then: [
          ["set", "$self.attrs.sterilisationFlagged", true],
          ["log", "{self} reaches three months old today. Section 33GB(1) makes it an offence for the owner of a dangerous dog (restricted breed) that has reached 3 months of age to keep it unsterilised. Section 33GB(2) gives a defence if the dog is already sterile, or has a physical condition that makes sterilising it likely to cause death — neither of which anyone has to turn their mind to until the day arrives.",
            { cite: "s. 33GB(1), (2)", sev: "stop" }],
          ["observe", "sterilise"]
        ] },

      { id: "pup-grows-up", on: "day", "for": "dog",
        "if": ["and", "$self.attrs.isPup", [">=", ["def", "ageMonths"], 3]],
        then: [
          ["set", "$self.attrs.isPup", false],
          ["log", "{self} turns three months old, so it stops being a restricted breed pup and the s. 33GC transfer restriction stops applying <i>on that footing</i>. Whether {self} is itself of a restricted breed is a separate question, and s. 33GC reaches that too.",
            { cite: "s. 33GC", sev: "ok" }]
        ] },

      /* the three-month birthday: registration and microchipping fall due together */
      { id: "birthday-unregistered", on: "day", "for": "dog",
        "if": ["and", [">=", ["def", "ageMonths"], 3], ["not", "$self.attrs.threeMonthsSeen"],
                      ["not", ["exists", "$self.rels.registeredWith"]]],
        then: [["log", "{self} reaches three months today, so the exemption for a dog under 3 months ends. It is not registered: <b>its owner, and the occupier of the premises where it is kept, each commit an offence</b> from today — a fine of $5,000, or $10,000 for a dangerous dog. There is no period of grace.",
          { cite: "s. 7(1), (3)(a)", sev: "stop" }]] },

      { id: "birthday-unchipped", on: "day", "for": "dog",
        "if": ["and", [">=", ["def", "ageMonths"], 3], ["not", "$self.attrs.threeMonthsSeen"],
                      ["not", "$self.attrs.microchipped"]],
        then: [["log", "{self} is not microchipped, and it has reached 3 months of age. Its owner commits an offence from today: a fine of $5,000.",
          { cite: "s. 21(2)", sev: "stop" }]] },

      { id: "birthday-count", on: "day", "for": "dog",
        "if": ["and", [">=", ["def", "ageMonths"], 3], ["not", "$self.attrs.threeMonthsSeen"],
                      ["or", ["not", ["exists", "$self.rels.registeredWith"]], ["not", "$self.attrs.microchipped"]]],
        then: [["observe", "three-months"]] },

      { id: "birthday-seen", on: "day", "for": "dog",
        "if": ["and", [">=", ["def", "ageMonths"], 3], ["not", "$self.attrs.threeMonthsSeen"]],
        then: [["set", "$self.attrs.threeMonthsSeen", true]] },

      /* registration ends on 31 October */
      { id: "registration-lapses", on: "day", "for": "dog",
        "if": ["and", ["exists", "$self.rels.registeredWith"], ["not", "$self.attrs.regLifetime"],
                      ["exists", "$self.attrs.regExpiryDay"], [">", "$day", "$self.attrs.regExpiryDay"],
                      ["not", "$self.attrs.destroyed"]],
        then: [
          ["set", "$self.rels.registeredWith", null],
          ["log", "{self}’s registration ended yesterday, 31 October. From today {self} is an unregistered dog: <b>its owner and the occupier each commit an offence</b> under s. 7(1). The Act allows no period of grace for renewal.",
            { cite: "ss. 7(1), 15(2)(c)", sev: "warn" }],
          ["observe", "oct31"]
        ] },

      /* the end of the minimum holding period */
      { id: "hold-run", on: "day", "for": "dog",
        "if": ["and", "$self.attrs.impounded", ["not", "$self.attrs.holdRunLogged"], ["def", "selfHoldRun"]],
        then: [
          ["set", "$self.attrs.holdRunLogged", true],
          ["log", "{self}’s minimum holding period has run. If it is not claimed, an authorised person may now cause it to be destroyed, or it may be sold or otherwise disposed of.",
            { cite: "s. 29(8), (10), (11)", sev: "ok" }]
        ] },

      { id: "dog-dies", on: "death:dog",
        then: [["log", "Everything the Act attached to {self} — the registration, any declaration, the sterilisation duty — ends here. Nothing in the Act requires anyone to be told.",
          { cite: "Pt III Div 1", sev: "warn" }]] }
    ],

    observations: [
      { id: "owner-victim", ref: "A-01", sev: "stop", label: "The dog attacked its owner",
        cite: "ss. 3, 33D(1)",
        what: "A dog attacks or chases the person who owns it.",
        why: "Section 33D(1) makes every person liable for the control of the dog guilty, and the owner is in that class by definition. Being the victim does not remove them from it, so the owner is liable to a fine of up to $20,000 for being attacked by their own dog — and a destruction order can be sought by someone else." },
      { id: "bootstrap", ref: "F-DANGEROUS-DOG-STATUS-TIMING", sev: "stop", label: "Penalty turns on which clock you read",
        cite: "s. 33D(1) Penalty",
        what: "An attack that is itself the reason the dog is later declared dangerous.",
        why: "The penalty depends on whether the dog is a dangerous dog, and the section never says whether that is judged at the time of the offence or at the time of prosecution. The same facts give $10,000 or $20,000." },
      { id: "sterilise", ref: "A-02", sev: "stop", label: "Unsterilised restricted-breed dog at three months",
        cite: "s. 33GB(1)",
        what: "A dangerous dog (restricted breed) reaches three months old and is not sterilised.",
        why: "The offence attaches to the owner on a birthday, not on anything the dog or the owner does. Whelp one in Nature mode and step the clock, and it arrives by itself." },
      { id: "unlawful-transfer", sev: "stop", label: "Transfer of a restricted breed pup",
        cite: "s. 33GC(3)",
        what: "Ownership of a restricted breed pup passes to somebody else.",
        why: "Effective and criminal at the same time. The Act does not void the transfer, it prosecutes it — which is why the console lets the act succeed and records the offence rather than refusing the click." },
      { id: "pup", sev: "warn", label: "Restricted breed pup: transfer shut down",
        cite: "s. 33GC",
        what: "A dog under three months old with at least one restricted-breed parent.",
        why: "Ownership cannot be transferred except through a deceased estate, a medical certificate of incapacity, or the Minister’s absolute discretion — and it stops being true on the ninetieth day, which is the same day the sterilisation duty starts." },
      { id: "fork-provocation", ref: "F-ATTACK-PROVOCATION-UNLESS", sev: "warn", label: "Provocation carve-out: two readings",
        cite: "s. 3 ‘attack’",
        what: "Behaviour induced by provocation.",
        why: "The definition excludes provoked behaviour, then includes (a)–(d) ‘unless the owner establishes … reasonable cause’. Whether that closing qualifier reaches back over the provocation exclusion is a live fork; this model takes the categorical reading." },
      { id: "unregistered", sev: "warn", label: "A dog with no local government",
        cite: "Pt III Div 1",
        what: "A dog exists and no local government has registered it.",
        why: "Registration is the hook much of the rest of the Act hangs on. Recorded because it is the commonest real-world state and the easiest to leave out of a model." },
      { id: "destruction", sev: "warn", label: "Destruction order available",
        cite: "Pt VII",
        what: "A dangerous dog causes physical injury.",
        why: "Recorded because the consequence runs well past the fine, and can be set in motion by a person other than the owner." },
      { id: "unchipped-pup", ref: "A-03", sev: "warn", label: "A pup must be chipped before sale, earlier than the law requires",
        cite: "ss. 21(2), 21(5), 26B(1)",
        what: "An unchipped dog under three months old changes hands.",
        why: "Chipping is not required until three months (s. 21(2)), a vet’s exemption cannot apply below three months (s. 21(5)), and transferring an unchipped dog is an offence unless an exemption applies (s. 26B(1)). So every sale of an unchipped young pup is an offence. That may well be the policy — pups chipped before sale — but the Act reaches it only by combining three provisions, and a breeder reading s. 21 alone would not see it." },
      { id: "early-destruction", sev: "warn", label: "Destroyed before the holding period ran",
        cite: "s. 29(8), (10)",
        what: "An authorised person destroys an impounded dog before its s. 29(8) minimum period has run — including where notice was never given, so the period never began.",
        why: "Section 29(10) gives the power to destroy an unclaimed dog without saying it must wait for s. 29(8). Two readings survive. The corpus encoding takes neither expressly: its s. 29(10) rule does not wait on s. 29(8)." },
      { id: "two-clocks", sev: "warn", label: "A seller’s two notice clocks",
        cite: "ss. 16A(1), 26C",
        what: "A registered, microchipped dog is sold and the seller has not told the microchip database within 7 days.",
        why: "The seller has 28 days to tell the local government and 7 days to tell the database company, each on pain of $5,000. A seller who knows the 28 days is already late for the 7. Recorded as a trap for owners, not as a defect." },
      { id: "three-months", sev: "warn", label: "Everything falls due at three months",
        cite: "ss. 7(3)(a), 21(2), 33GB",
        what: "A dog reaches three months old unregistered or unchipped.",
        why: "Registration and microchipping — and, for a restricted breed, sterilisation — become offences on the same birthday, with no period of grace. Being unchipped is also a ground to refuse registration (s. 16(3)(da)), so in practice the chip has to come first." },
      { id: "oct31", sev: "warn", label: "Registration lapses on 31 October",
        cite: "ss. 7(1), 15(2)(c)",
        what: "An annual registration reaches the next 31 October.",
        why: "It ends on that day for every dog registered annually, and the owner and occupier commit an offence from 1 November. The Act has no renewal period of grace. A dangerous dog can only ever be registered this way (s. 15(3A))." },
      { id: "pay-to-reclaim", sev: "warn", label: "Release can wait on paying fines",
        cite: "s. 29(4), (10)(c)",
        what: "An owner reclaims an impounded dog.",
        why: "The local government may require payment not only of costs and fees but of “any penalties imposed on … the owner in respect of an offence” before release, and unpaid money is itself a ground for destruction. Recorded because it ties the dog’s life to the owner’s fines." },
      { id: "nuisance-relapse", ref: "C-02", sev: "warn", label: "Barking again while a nuisance order runs",
        cite: "s. 38(4), (5)",
        what: "A dog under a nuisance order stops barking, then starts again within the order’s six months.",
        why: "The Act makes that an offence: compliance is required “during the period in which it has effect”. The corpus’s L4 encodes the duty as discharged once the barking is first prevented, and has no six-month period, so it would miss this. A defect in our encoding, not in the Act." },
      { id: "no-seize-unregistered", sev: "ok", label: "An unregistered dog cannot be seized for that alone",
        cite: "s. 29(3)(c)(ii)",
        what: "An authorised person seizes an ordinary dog because it is not registered.",
        why: "Looks like a gap; is a choice. Being unregistered is a seizure ground only for a dangerous dog. For any other dog it is an offence by the owner (s. 7(1)), dealt with by prosecution, not by the pound." },
      { id: "void-act", sev: "ok", label: "An act of no effect",
        cite: "ss. 29, 33E(1), 38(3)",
        what: "Somebody without the power purports to exercise it.",
        why: "Not an offence and not an irregularity — simply nothing. Counted separately from prohibited acts, because a nullity and a crime are different failures, and a console that hid the button would teach neither." }
    ]
  };

  /* ============== Retail Barring Orders Bill 2025 (WA) ================== */

  var RBO_BILL = {
    id: "rbo-bill",
    title: "Retail Barring Orders Bill 2025",
    jurisdiction: "Western Australia",
    status: "Not law · before the Legislative Council",
    scope: "ss. 6, 8, 9, 19, 20, 21, 27, 29, 30, 34, 38, 39, 48, 54–57 and 63.",
    startDate: "2027-01-01",
    dayLabel: "Day",

    types: [
      { id: "court", label: "Court", band: 0, shape: "rect" },
      { id: "authority", label: "Authority", band: 0, shape: "rect" },
      { id: "business", label: "Eligible person", band: 1, shape: "rect",
        create: { nameHint: "Riverton Pharmacy", fields: [], rels: [] } },
      { id: "person", label: "Person", band: 1, shape: "rect",
        create: { nameHint: "Alex", bornVerb: "Born", fields: [
          { key: "bornDay", type: "age", origin: "birth", unit: "years",
            label: "Age in years", def: 19, cite: "s. 9(1)",
            note: "The Bill routes by age on the day each application is made, so this is the fact almost everything else turns on." },
          { key: "isWorker", type: "bool", origin: "exogenous", label: "Works in retail" }
        ], rels: [] } },
      { id: "premises", label: "Premises", band: 2, shape: "round",
        create: { nameHint: "Riverton Pharmacy, Shelley", fields: [
          { key: "inCentre", type: "bool", origin: "innate", cite: "s. 8(3)",
            label: "Is inside a shopping centre" }
        ], rels: [
          { key: "operator", label: "Operated by", target: "business", required: true,
            origin: "innate", cite: "s. 8(3)" }
        ] } }
    ],

    relLabels: { operator: "operated by" },

    scenarios: [
      { label: "Kirra turns 18 mid-application", focus: "r1", steps: [
        { actor: "r1", action: "violence", target: "s1", params: { threatened: true } },
        { tick: 5 },
        { actor: "e1", action: "apply", target: "r1" },
        { tick: 57 }
      ] },
      { label: "… and then applies to set it aside", focus: "r1", steps: [
        { actor: "r1", action: "violence", target: "s1", params: { threatened: true } },
        { tick: 3 },
        { actor: "e1", action: "apply", target: "r1" },
        { actor: "c2", action: "makeOrder", target: "r1", params: { inAbsence: true } },
        { tick: 2 },
        { actor: "c2", action: "serve", target: "r1", params: { route: "in-court" } },
        { tick: 57 },
        { tick: 10 },
        { actor: "r1", action: "setAside", target: "c1" }
      ] },
      { label: "The firearms order nobody was asked about", focus: "r2", steps: [
        { actor: "r2", action: "violence", target: "s1", params: { injured: true } },
        { tick: 3 },
        { actor: "e1", action: "apply", target: "r2" },
        { actor: "c1", action: "makeOrder", target: "r2", params: { firearms: true, inAbsence: true } },
        { tick: 4 },
        { actor: "c1", action: "serve", target: "r2", params: { route: "prison" } }
      ] },
      { label: "The application nobody can dismiss", focus: "r2", steps: [
        { actor: "r2", action: "violence", target: "s1", params: { threatened: true } },
        { tick: 3 },
        { actor: "e1", action: "apply", target: "r2" },
        { actor: "c1", action: "makeOrder", target: "r2", params: {} },
        { tick: 2 },
        { actor: "c1", action: "serve", target: "r2", params: { route: "police-personal" } },
        { tick: 180 },
        { actor: "e1", action: "applyCancel", target: "r2" },
        { tick: 21 },
        { actor: "c1", action: "refuseCancel", target: "r2" }
      ] },
      { label: "Twelve months too late", focus: "r2", steps: [
        { actor: "r2", action: "violence", target: "s1", params: { damaged: true } },
        { tick: 400 },
        { actor: "e1", action: "apply", target: "r2" }
      ] },
      { label: "A new shop, and a new 17-year-old", focus: "@kid",
        mode: "nature", steps: [
        { spawn: "business", as: "biz", label: "Riverton Pharmacy" },
        { spawn: "premises", as: "shop", label: "Riverton Pharmacy, Shelley",
          attrs: { inCentre: true }, rels: { operator: "@biz" } },
        { spawn: "person", as: "kid", label: "Tobi R.", note: "aged 17",
          attrs: { bornDate: "2009-02-05", isWorker: false } },
        { tick: 2 },
        { actor: "@kid", action: "violence", target: "@shop", params: { threatened: true } },
        { tick: 3 },
        { actor: "@biz", action: "apply", target: "@kid" },
        { tick: 31 }
      ] }
    ],

    entities: [
      { id: "c1", type: "court", label: "Magistrates Court" },
      { id: "c2", type: "court", label: "Children’s Court" },
      { id: "a1", type: "authority", label: "Commissioner of Police" },
      { id: "e1", type: "business", label: "Kingsway Fresh", note: "employer" },
      { id: "r1", type: "person", label: "Kirra T.", note: "aged 17",
        attrs: { bornDate: "2009-03-04", isWorker: false } },
      { id: "r2", type: "person", label: "Dane M.", note: "aged 24",
        attrs: { bornDate: "2002-06-15", isWorker: false } },
      { id: "w1", type: "person", label: "Sam O.", note: "retail worker",
        attrs: { bornDate: "1995-09-20", isWorker: true } },
      { id: "s1", type: "premises", label: "Kingsway Fresh, Belmont",
        attrs: { inCentre: false }, rels: { operator: "e1" } }
    ],

    defs: {
      targetAge: ["ageYears", "$target.attrs.bornDay"],
      selfAge: ["ageYears", "$self.attrs.bornDay"],
      targetIsChild: ["<", ["def", "targetAge"], 18],
      withinWindow: ["and", ["exists", "$target.attrs.incidentDay"],
                            ["<=", ["daysSince", "$target.attrs.incidentDay"], 365]],
      routeAsks: ["or", ["=", "$p.route", "police-personal"],
                        ["=", "$p.route", "police-oral"]]
    },

    actions: [
      { id: "violence", actor: "person", target: "premises",
        label: "Commit retail violence", cite: "s. 6",
        log: "<b>{self}</b> commits retail violence at <b>{target}</b>.",
        params: [
          { key: "threatened", label: "threatened a retail worker" },
          { key: "injured", label: "caused physical injury" },
          { key: "damaged", label: "damaged property" }
        ] },
      { id: "apply", actor: "business", target: "person",
        label: "Apply for a retail barring order", cite: "ss. 8, 9",
        log: "<b>{self}</b> applies for an RBO against <b>{target}</b>." },
      { id: "makeOrder", actor: "court", target: "person",
        label: "Make a retail barring order", cite: "ss. 10, 21",
        params: [
          { key: "firearms", label: "the order restrains possession of a firearm item", emph: true },
          { key: "inAbsence", label: "made in the person’s absence" }
        ] },
      { id: "serve", actor: "court", target: "person",
        label: "Serve the order", cite: "ss. 20, 54–57",
        params: [
          { key: "route", type: "choice", label: "How is it served?", options: [
            { v: "police-personal", label: "personally, by a police officer — s. 55(2)(c)" },
            { v: "police-oral", label: "substituted service, orally by police — s. 57(6)(a)" },
            { v: "registrar", label: "personally, by a registrar — s. 55(2)(a)" },
            { v: "authorised", label: "personally, by a person a registrar authorised — s. 55(2)(b)" },
            { v: "custodial", label: "personally, by a custodial officer — s. 55(2)(d)" },
            { v: "prison", label: "personally, by a prison officer — s. 55(2)(e)" },
            { v: "in-court", label: "taken to be served, the person was in court — s. 54(2)" },
            { v: "post", label: "substituted service, by post — s. 57(6)(b)" },
            { v: "electronic", label: "substituted service, electronically — s. 57(6)(c)" }
          ] }
        ] },
      { id: "applyCancel", actor: "business", target: "person",
        label: "Apply to cancel, heard in the person’s absence",
        cite: "ss. 34(3), 38(1)(a)",
        log: "<b>{self}</b> applies to cancel the order against <b>{target}</b>, and asks for it to be heard in their absence. A registrar fixes a hearing and does not summons them." },
      { id: "refuseCancel", actor: "court", target: "person",
        label: "Decline to cancel the order", cite: "s. 39(2)" },
      { id: "setAside", actor: "person", target: "court",
        label: "Apply to set the order aside", cite: "ss. 27, 29" }
    ],

    rules: [
      { id: "record-violence", on: "action:violence",
        then: [
          ["set", "$self.attrs.incidentDay", "$day"],
          ["log", "The twelve months in which an application may be made start running today.",
            { cite: "s. 8(2)" }]
        ] },

      { id: "no-incident", on: "action:apply",
        "if": ["not", ["exists", "$target.attrs.incidentDay"]],
        then: [["log", "Nothing is recorded against {target}. An RBO application must be founded on retail violence.",
          { cite: "s. 8(1)", sev: "warn" }]] },

      { id: "window-closed", on: "action:apply",
        "if": ["and", ["exists", "$target.attrs.incidentDay"], ["not", ["def", "withinWindow"]]],
        then: [
          ["set", "$target.attrs.daysSinceViolence", ["daysSince", "$target.attrs.incidentDay"]],
          ["log", "It is {target.attrs.daysSinceViolence} days since the retail violence. Section 8(2) bars an application more than twelve months after it, and the Bill provides no extension.",
            { cite: "s. 8(2)", sev: "warn" }],
          ["observe", "lapsed"]
        ] },

      { id: "apply-child", on: "action:apply",
        "if": ["and", ["def", "withinWindow"], ["def", "targetIsChild"]],
        then: [
          ["set", "$target.attrs.matterOpen", true],
          ["set", "$target.attrs.matterCourt", "Children’s Court"],
          ["log", "{target} is a child <b>today</b>, so the application goes to the <b>Children’s Court</b>. The Bill routes by age at the moment each application is made, not at the moment of the violence.",
            { cite: "s. 9(1)(a)" }]
        ] },

      { id: "apply-adult", on: "action:apply",
        "if": ["and", ["def", "withinWindow"], ["not", ["def", "targetIsChild"]]],
        then: [
          ["set", "$target.attrs.matterOpen", true],
          ["set", "$target.attrs.matterCourt", "Magistrates Court"],
          ["log", "{target} is an adult, so the application goes to the <b>Magistrates Court</b>.",
            { cite: "s. 9(1)(b)" }]
        ] },

      { id: "make-order", on: "action:makeOrder",
        "if": "$target.attrs.matterOpen",
        then: [
          ["set", "$target.attrs.orderMadeDay", "$day"],
          ["set", "$target.attrs.childAtMaking", ["def", "targetIsChild"]],
          ["set", "$target.attrs.firearms", "$p.firearms"],
          ["set", "$target.attrs.madeInAbsence", "$p.inAbsence"],
          ["log", "An RBO is made against <b>{target}</b> by {self}. It runs from service, for at most two years if they were an adult when it was made and one year if they were a child.",
            { cite: "ss. 10, 21(2), 21(3)" }],
          ["log", "Nothing in the Bill requires the Commissioner of Police to be told that an order has been <i>made</i>. That duty appears on variation, on cancellation and on a set aside, and not here — only the rules of court could fill it.",
            { cite: "ss. 19, 70(2)(i)", sev: "warn" }],
          ["observe", "no-commissioner"]
        ] },

      { id: "make-order-no-matter", on: "action:makeOrder",
        "if": ["not", "$target.attrs.matterOpen"],
        then: [["log", "There is no application on foot against {target}.",
          { cite: "s. 8(1)", sev: "warn" }]] },

      { id: "serve-order", on: "action:serve",
        "if": ["exists", "$target.attrs.orderMadeDay"],
        then: [
          ["set", "$target.attrs.servedDay", "$day"],
          ["log", "The order against {target} is served, and comes into force today.",
            { cite: "s. 20(a)" }]
        ] },

      { id: "firearms-asked", on: "action:serve",
        "if": ["and", "$target.attrs.firearms", ["def", "routeAsks"]],
        then: [["log", "A police officer puts the four firearms questions to {target} and completes the police copy, so the Commissioner can notify their employer and any co-licensee.",
          { cite: "s. 63(2), (4)", sev: "ok" }]] },

      { id: "firearms-not-asked", on: "action:serve",
        "if": ["and", "$target.attrs.firearms", ["not", ["def", "routeAsks"]]],
        then: [
          ["log", "This is a <b>firearms RBO</b>, and it was not served by a police officer acting personally or orally. Section 63(2) puts the duty to ask on those two routes and on no other, so no police copy is completed, the Commissioner’s duty under s. 63(4) never arises, and the offences in s. 63(5) and (6) cannot be committed by an employer or co-licensee who lets {target} near a firearm.",
            { cite: "s. 63(2), (4)", sev: "stop" }],
          ["observe", "b02"]
        ] },

      { id: "cancel-open", on: "action:applyCancel",
        then: [["set", "$target.attrs.cancelOpen", true]] },

      { id: "refuse-cancel", on: "action:refuseCancel",
        "if": "$target.attrs.cancelOpen",
        then: [
          ["log", "The court applies ss. 12 to 14 as though it were deciding whether to make the order, and is <b>not</b> satisfied that the order should be cancelled.",
            { cite: "s. 39(3)" }],
          ["log", "<b>Section 39(2) confers exactly one power at a hearing fixed under s. 38(1)(a): making an order cancelling the RBO.</b> It has no power to dismiss. Section 39(1)(a) has that power, but only for a hearing fixed under s. 37, and s. 41(1) supplies a dismissal only where the applicant fails to attend. So the application is not granted, not dismissed, and still on foot.",
            { cite: "s. 39(2)", sev: "stop" }],
          ["observe", "b01"]
        ] },

      { id: "refuse-cancel-none", on: "action:refuseCancel",
        "if": ["not", "$target.attrs.cancelOpen"],
        then: [["log", "There is no cancellation application before the court.",
          { cite: "s. 38", sev: "warn" }]] },

      { id: "set-aside-routing", on: "action:setAside",
        "if": ["and", ["exists", "$self.attrs.servedDay"],
                      ["=", "$self.attrs.matterCourt", "Children’s Court"],
                      [">=", ["def", "selfAge"], 18]],
        then: [
          ["log", "{self} was a child when the order was made and is an adult now, so s. 29(1)(b) sends the set aside application to the <b>Magistrates Court</b> — while the <b>Children’s Court</b> made the decision and holds the record. This looks like a routing error and is not one: s. 30 requires a registrar of the Children’s Court to provide the court record to the Magistrates Court.",
            { cite: "ss. 29(1)(b), 30", sev: "ok" }],
          ["observe", "s30"]
        ] },

      { id: "set-aside-late", on: "action:setAside",
        "if": ["and", ["exists", "$self.attrs.servedDay"],
                      [">", ["daysSince", "$self.attrs.servedDay"], 21]],
        then: [
          ["set", "$self.attrs.daysSinceService", ["daysSince", "$self.attrs.servedDay"]],
          ["log", "The application comes {self.attrs.daysSinceService} days after service, outside the 21 days s. 27 allows, so the court must be satisfied there was a reasonable excuse for the delay.",
            { cite: "ss. 27, 31(3)", sev: "warn" }]] },

      { id: "set-aside-none", on: "action:setAside",
        "if": ["not", ["exists", "$self.attrs.servedDay"]],
        then: [["log", "No order has been served on {self}, so there is nothing to set aside. The 21 days in s. 27 run from service.",
          { cite: "s. 27", sev: "warn" }]] },

      { id: "new-person-child", on: "create:person",
        "if": ["<", ["def", "selfAge"], 18],
        then: [["log", "{self} is a child. While that stays true an RBO application about them goes to the Children’s Court, and an order made while they are a child can run for at most one year rather than two.",
          { cite: "ss. 9(1)(a), 21(3)(b)" }]] },

      { id: "new-premises-operator", on: "create:premises",
        "if": ["not", ["exists", "$self.rels.operator"]],
        then: [["log", "Nobody is recorded as operating {self}. Section 8(3) limits who may apply for an RBO about a place — an employer, the operator of the business, the owner or operator of a shopping centre, or a union — so with no operator there may be nobody able to apply at all.",
          { cite: "s. 8(3)", sev: "warn" }]] },

      { id: "turns-18", on: "day", "for": "person",
        "if": ["and", ["=", ["def", "selfAge"], 18],
                      ["not", "$self.attrs.turned18"]],
        then: [
          ["set", "$self.attrs.turned18", true],
          ["log", "<b>{self} turns 18 today.</b> From now on every application about them is routed to the Magistrates Court, whatever court heard the last one.",
            { cite: "ss. 9(1), 29(1), 34(1)" }]
        ] },

      { id: "s48-transfer", on: "day", "for": "person",
        "if": ["and", ["=", ["def", "selfAge"], 18],
                      ["not", "$self.attrs.s48Done"],
                      "$self.attrs.matterOpen",
                      ["=", "$self.attrs.matterCourt", "Children’s Court"],
                      ["not", ["exists", "$self.attrs.orderMadeDay"]]],
        then: [
          ["set", "$self.attrs.s48Done", true],
          ["set", "$self.attrs.matterCourt", "Magistrates Court"],
          ["log", "A matter about {self} is still pending in the Children’s Court, so it must be transferred to the Magistrates Court. What has already been done is not invalidated and orders already made stand.",
            { cite: "s. 48", sev: "ok" }],
          ["observe", "s48"]
        ] }
    ],

    observations: [
      { id: "b01", ref: "B-01", sev: "stop", label: "Application left undetermined",
        cite: "s. 39(2)",
        what: "A cancellation heard in the person’s absence, which the court declines to grant.",
        why: "Section 39(2) gives the court one power at that hearing — cancelling. Declining leaves the application on foot with no order available to dispose of it." },
      { id: "b02", ref: "B-02", sev: "stop", label: "Firearms order served with no inquiry",
        cite: "s. 63(2)",
        what: "A firearms RBO served by anyone but a police officer acting personally or orally.",
        why: "Seven of the nine service routes the Bill provides produce this. The questions are never put, so the notification chain never starts and two offence provisions never become available." },
      { id: "s30", ref: "V-01", sev: "ok", label: "Set aside routed to the other court",
        cite: "ss. 29(1)(b), 30",
        what: "The respondent was a child when the order was made and an adult when they apply to set it aside.",
        why: "Not a defect. Section 30 sends the court record across. Worth watching precisely because it looks like one." },
      { id: "s48", sev: "ok", label: "Pending matter transferred on turning 18",
        cite: "s. 48",
        what: "The respondent turns 18 while a Children’s Court matter is still pending.",
        why: "Not a defect. The matter transfers, proceedings already taken are not invalidated, and orders already made stand." },
      { id: "no-commissioner", ref: "B-04", sev: "warn", label: "Order made, Commissioner not told",
        cite: "s. 19",
        what: "Every order.",
        why: "The Bill requires the Commissioner of Police to be notified on variation, on cancellation and on a set aside, and not on the making of an order. Only the rules of court can fill it." },
      { id: "lapsed", sev: "warn", label: "Twelve months ran out",
        cite: "s. 8(2)",
        what: "An application attempted more than twelve months after the violence.",
        why: "Not a defect — a deliberate bar with no extension. Recorded because it is the deadline retailers are most likely to miss." }
    ]
  };

  /* ===== Residential Tenancies Act 1987 (WA), as amended by the ======== */
  /* ===== Residential Tenancies Amendment (Rent Cap) Bill 2026 ========= */
  /* Encoding: subjects/western-australia/residential-tenancies-act/LQA/.
     Commencement is assumed: assent 31 Dec 2026, so cl. 2(b)(ii) brings the
     Bill into force on 1 Jan 2027, which is day 92 on this clock. Before that
     day the previous ss. 64 and 70A still operate, so the transitional
     provisions (ss. 105-107) can be run rather than asserted.            */

  var RTA_RENT_CAP = {
    id: "rta-rent-cap",
    title: "Residential Tenancies Act 1987, as amended by the Rent Cap Bill 2026",
    jurisdiction: "Western Australia",
    status: "Not law · Bill No. 70 at LC second reading · commencement assumed 1 Jan 2027 (day 92)",
    scope: "ss. 30, 31AA, 31AB (rent cap); s. 64 as amended and s. 64(3)–(4) unamended; s. 70A as amended; s. 71BA; s. 76C; transitional ss. 105–107.",
    startDate: "2026-10-01",
    dayLabel: "Day",

    types: [
      { id: "court", label: "Court", band: 0, shape: "rect" },

      { id: "party", label: "Person or body", band: 1, shape: "rect",
        create: { nameHint: "Robin", fields: [], rels: [] } },

      { id: "tenancy", label: "Tenancy agreement", band: 2, shape: "round",
        create: { nameHint: "Periodic tenancy, Bassendean", bornVerb: "Commenced", fields: [
          { key: "bornDay", type: "age", origin: "birth", unit: "months",
            label: "Months since the agreement commenced", def: 18, cite: "ss. 30(1)(b), 31AA(1)",
            note: "An agreement’s commencement is its birth: the 12-month gap between increases, the initial CPI and the end of a fixed term are all counted from it in calendar months." },
          { key: "rent", type: "number", origin: "innate", def: 600, cite: "s. 3 ‘rent’",
            label: "Weekly rent fixed by the agreement ($)" },
          { key: "fixedTerm", type: "bool", origin: "innate", cite: "s. 3",
            label: "Creates a tenancy for a fixed term" },
          { key: "termMonths", type: "number", origin: "innate", def: 0, cite: "s. 3 ‘expiry day’",
            label: "Length of the fixed term in months (0 if periodic)" },
          { key: "increaseClause", type: "bool", origin: "innate", cite: "ss. 30(2)(a), 31AA(2)(a)",
            label: "Sets out the amount of rent increases or the method of calculating them" },
          { key: "incomeBased", type: "bool", origin: "innate", cite: "s. 31A",
            label: "Rent is calculated by reference to the tenant’s income" },
          { key: "socialHousing", type: "bool", origin: "exogenous", cite: "ss. 3, 71A",
            label: "Is a social housing tenancy agreement",
            note: "Turns on whether the lessor is the Housing Authority or a prescribed provider, and on what regulations exclude, so it is settled outside this scheme." },
          { key: "approvedAboveCap", type: "bool", origin: "conferred", by: "approveIncrease",
            cite: "s. 31AA(2)(c)", label: "A competent court has approved an increase above the limit" }
        ], rels: [
          { key: "lessor", label: "Lessor", target: "party", required: true, origin: "innate", cite: "s. 3" },
          { key: "tenant", label: "Tenant", target: "party", required: true, origin: "innate", cite: "s. 3" },
          { key: "previousAgreement", label: "Follows, at the same premises", target: "tenancy",
            origin: "innate", cite: "s. 31B(2)",
            note: "The agreement this one replaced. Same lessor and tenant makes it a continuation under s. 31B; a different tenant makes it a new tenancy of the same premises." }
        ] } }
    ],

    relLabels: { lessor: "lessor", tenant: "tenant", previousAgreement: "follows" },

    scenarios: [
      { label: "A 3% increase inside the cap", focus: "a1", steps: [
        { tick: 92 },
        { actor: "l1", action: "rentNotice", target: "a1", params: { pct: "3", cpi: "4", statesCap: true } },
        { tick: 60 }
      ] },
      { label: "A 10% increase the tenant never agrees to", focus: "a1", steps: [
        { tick: 92 },
        { actor: "l1", action: "rentNotice", target: "a1", params: { pct: "10", cpi: "4", statesCap: true } },
        { tick: 60 }
      ] },
      { label: "… approved by the court on day 61", focus: "a1", steps: [
        { tick: 92 },
        { actor: "l1", action: "rentNotice", target: "a1", params: { pct: "10", cpi: "4", statesCap: true } },
        { actor: "l1", action: "applyAboveCap", target: "a1" },
        { tick: 61 },
        { actor: "c1", action: "approveIncrease", target: "a1" }
      ] },
      { label: "25% written into a fixed-term lease (B-01)", focus: "a2", steps: [
        { tick: 92 },
        { actor: "l1", action: "rentNotice", target: "a2", params: { pct: "25", cpi: "4", statesCap: true } },
        { tick: 60 }
      ] },
      { label: "An income-based social housing rent (B-03)", focus: "a3", steps: [
        { tick: 92 },
        { actor: "l2", action: "rentNotice", target: "a3", params: { pct: "5", cpi: "4", statesCap: true } }
      ] },
      { label: "The ABS re-references the index (B-04)", focus: "a1", steps: [
        { tick: 92 },
        { actor: "l1", action: "rentNotice", target: "a1", params: { pct: "3", cpi: "rebased", statesCap: true } },
        { tick: 60 }
      ] },
      { label: "Renewal with the same tenant at 20% more (B-02)", focus: "@renewal",
        mode: "nature", steps: [
        { tick: 92 },
        { spawn: "tenancy", as: "renewal", label: "Renewal, Victoria Park", note: "same lessor, same tenant",
          attrs: { bornDate: "2027-01-01", rent: 720, fixedTerm: true, termMonths: 12, increaseClause: false,
                   incomeBased: false, socialHousing: false, approvedAboveCap: false },
          rels: { lessor: "l1", tenant: "t1", previousAgreement: "a1" } }
      ] },
      { label: "Court caps the rent; the next tenant pays more (B-06)", focus: "@next",
        mode: "nature", steps: [
        { tick: 92 },
        { actor: "l1", action: "rentNotice", target: "a1", params: { pct: "10", cpi: "4", statesCap: true } },
        { actor: "l1", action: "applyAboveCap", target: "a1" },
        { tick: 3 },
        { actor: "c1", action: "refuseAndFix", target: "a1" },
        { tick: 90 },
        { spawn: "party", as: "morgan", label: "Morgan", note: "new tenant" },
        { spawn: "tenancy", as: "next", label: "New tenancy, Victoria Park", note: "different tenant",
          attrs: { bornDate: "2027-04-04", rent: 700, fixedTerm: false, termMonths: 0, increaseClause: false,
                   incomeBased: false, socialHousing: false, approvedAboveCap: false },
          rels: { lessor: "l1", tenant: "@morgan", previousAgreement: "a1" } },
        { actor: "l1", action: "demandRent", target: "@next" }
      ] },
      { label: "Six months’ notice, cut to 60 days by the tenant’s own application (B-05)", focus: "a1", steps: [
        { tick: 92 },
        { actor: "l1", action: "groundNotice", target: "a1",
          params: { ground: "otheruse", period: "184", evidence: true, genuine: true } },
        { tick: 3 },
        { actor: "t1", action: "applyExtend", target: "a1" },
        { tick: 10 },
        { actor: "c1", action: "courtPossession", target: "a1" },
        { tick: 60 }
      ] },
      { label: "Social housing: 90 days under s. 71BA, 60 by order (B-05, B-08)", focus: "a3", steps: [
        { tick: 92 },
        { actor: "l2", action: "sh71BA", target: "a3", params: { ground: "sell", period: "90" } },
        { tick: 2 },
        { actor: "t3", action: "applyExtend", target: "a3" },
        { tick: 5 },
        { actor: "c1", action: "courtPossession", target: "a3" },
        { tick: 60 }
      ] },
      { label: "A social housing tenant tries to end the fixed term (B-07)", focus: "a3", steps: [
        { tick: 100 },
        { actor: "t3", action: "tenantEndOfTerm", target: "a3" },
        { tick: 143 }
      ] },
      { label: "A fixed term runs out and nobody gives notice (F-2)", focus: "a5", steps: [
        { tick: 222 },
        { actor: "l1", action: "groundNotice", target: "a5",
          params: { ground: "sell", period: "60", evidence: true, genuine: true } }
      ] },
      { label: "A lessor’s end-of-term notice after commencement", focus: "a5", steps: [
        { tick: 95 },
        { actor: "l1", action: "lessorEndOfTerm", target: "a5" }
      ] },
      { label: "A ‘sell’ notice while the rent order is in force (B-10)", focus: "a1", steps: [
        { tick: 92 },
        { actor: "l1", action: "rentNotice", target: "a1", params: { pct: "10", cpi: "4", statesCap: true } },
        { actor: "l1", action: "applyAboveCap", target: "a1" },
        { tick: 3 },
        { actor: "c1", action: "refuseAndFix", target: "a1" },
        { tick: 7 },
        { actor: "l1", action: "groundNotice", target: "a1",
          params: { ground: "sell", period: "60", evidence: true, genuine: false } }
      ] },
      { label: "Old s. 70A notice, lessor’s s. 72 case pending at commencement (B-09)", focus: "a4", steps: [
        { actor: "l1", action: "lessorEndOfTerm", target: "a4" },
        { tick: 41 },
        { actor: "l1", action: "applyPossession", target: "a4" },
        { tick: 52 }
      ] },
      { label: "Old no-grounds notice, lessor’s s. 71 case pending at commencement (B-09)", focus: "a1", steps: [
        { actor: "l1", action: "oldNoGrounds", target: "a1" },
        { tick: 61 },
        { actor: "l1", action: "applyPossession", target: "a1" },
        { tick: 31 }
      ] },
      { label: "… and where the tenant applied under s. 64(3) instead", focus: "a1", steps: [
        { actor: "l1", action: "oldNoGrounds", target: "a1" },
        { tick: 3 },
        { actor: "t1", action: "applyExtend", target: "a1" },
        { tick: 89 }
      ] },
      { label: "A rent notice given before commencement (s. 105)", focus: "a1", steps: [
        { tick: 10 },
        { actor: "l1", action: "rentNotice", target: "a1", params: { pct: "10", cpi: "4", statesCap: false } },
        { tick: 60 }
      ] },
      { label: "The tenant’s neighbour gives a rent notice", focus: "a1", steps: [
        { tick: 92 },
        { actor: "t2", action: "rentNotice", target: "a1", params: { pct: "10", cpi: "4", statesCap: true } }
      ] }
    ],

    entities: [
      { id: "c1", type: "court", label: "Magistrates Court" },
      { id: "l1", type: "party", label: "Priya", note: "private lessor" },
      { id: "l2", type: "party", label: "Housing Authority", note: "social housing provider" },
      { id: "t1", type: "party", label: "Sam", note: "tenant, Victoria Park" },
      { id: "t2", type: "party", label: "Jordan", note: "tenant, Joondalup" },
      { id: "t3", type: "party", label: "Aroha", note: "tenant, Mirrabooka" },
      { id: "t4", type: "party", label: "Lee", note: "tenant, Fremantle" },
      { id: "t5", type: "party", label: "Kai", note: "tenant, Midland" },
      { id: "a1", type: "tenancy", label: "Periodic, Victoria Park", note: "$600 a week",
        attrs: { bornDate: "2025-03-01", rent: 600, fixedTerm: false, termMonths: 0, increaseClause: false,
                 incomeBased: false, socialHousing: false, approvedAboveCap: false },
        rels: { lessor: "l1", tenant: "t1" } },
      { id: "a2", type: "tenancy", label: "2-year lease, Joondalup", note: "25% increase clause",
        attrs: { bornDate: "2026-01-15", rent: 600, fixedTerm: true, termMonths: 24, increaseClause: true,
                 incomeBased: false, socialHousing: false, approvedAboveCap: false },
        rels: { lessor: "l1", tenant: "t2" } },
      { id: "a3", type: "tenancy", label: "Social housing, Mirrabooka", note: "1-year term to 1 Jun 2027, income-based rent",
        attrs: { bornDate: "2026-06-01", rent: 300, fixedTerm: true, termMonths: 12, increaseClause: false,
                 incomeBased: true, socialHousing: true, approvedAboveCap: false },
        rels: { lessor: "l2", tenant: "t3" } },
      { id: "a4", type: "tenancy", label: "1-year lease, Fremantle", note: "expires 10 Nov 2026",
        attrs: { bornDate: "2025-11-10", rent: 550, fixedTerm: true, termMonths: 12, increaseClause: false,
                 incomeBased: false, socialHousing: false, approvedAboveCap: false },
        rels: { lessor: "l1", tenant: "t4" } },
      { id: "a5", type: "tenancy", label: "1-year lease, Midland", note: "expires 10 May 2027",
        attrs: { bornDate: "2026-05-10", rent: 500, fixedTerm: true, termMonths: 12, increaseClause: false,
                 incomeBased: false, socialHousing: false, approvedAboveCap: false },
        rels: { lessor: "l1", tenant: "t5" } }
    ],

    defs: {
      inForce: [">=", "$day", 92],
      selfIsLessor: ["=", "$self", ["rel", "$target", "lessor"]],
      selfIsTenant: ["=", "$self", ["rel", "$target", "tenant"]],
      tMonths: ["ageMonths", "$target.attrs.bornDay"],
      tDuringFixedTerm: ["and", "$target.attrs.fixedTerm", ["not", "$target.attrs.expired"],
                                ["<", ["def", "tMonths"], "$target.attrs.termMonths"]],
      tMonthsSinceIncrease: ["if", ["exists", "$target.attrs.lastIncreaseDay"],
                                   ["ageMonths", "$target.attrs.lastIncreaseDay"], ["def", "tMonths"]],
      /* CPI growth since the initial CPI. "rebased" is the published current
         number on a new reference base (105) against an initial number on the
         old one (200): below it, so floored to it, so growth is nil. */
      growth: ["if", ["=", "$p.cpi", "rebased"], 0, ["/", ["floor", "$p.cpi"], 100]],
      limit: ["/", ["floor", ["*", "$target.attrs.rent", ["def", "growth"], 110]], 100],
      proposed: ["/", ["floor", ["*", "$target.attrs.rent", ["floor", "$p.pct"]]], 100],
      aboveCap: [">", ["def", "proposed"], ["def", "limit"]],
      amountAllowed: ["or", ["not", "$target.attrs.rentNoticeUnderNewLaw"], ["not", ["def", "aboveCap"]],
                            "$target.attrs.increaseClause", "$target.attrs.tenantAgreed",
                            "$target.attrs.approvedAboveCap"],
      contentAllowed: ["or", ["not", "$target.attrs.rentNoticeUnderNewLaw"], "$p.statesCap"],
      ownOrderInForce: ["and", ["exists", "$target.attrs.orderDay"],
                               ["<", ["ageMonths", "$target.attrs.orderDay"], 12]],
      prevOrderDay: ["attrOf", ["rel", "$target", "previousAgreement"], "orderDay"],
      prevOrderInForce: ["and", ["exists", ["def", "prevOrderDay"]],
                                ["<", ["ageMonths", ["def", "prevOrderDay"]], 12]],
      prevTenantDiffers: ["!=", ["rel", "$target", "tenant"],
                                ["rel", ["rel", "$target", "previousAgreement"], "tenant"]],
      requiredMonths: ["if", ["=", "$p.ground", "renovate"], 3, ["if", ["=", "$p.ground", "otheruse"], 6, 0]],
      s64Base: ["and", ["def", "selfIsLessor"], ["def", "inForce"],
                       ["not", "$target.attrs.socialHousing"], ["not", ["def", "tDuringFixedTerm"]]],
      earliestPossession: ["if", [">", ["+", "$day", 1], ["+", "$target.attrs.termNoticeDay", 60]],
                                 ["+", "$day", 1], ["+", "$target.attrs.termNoticeDay", 60]],
      selfExpiring: ["and", "$self.attrs.fixedTerm", ["not", "$self.attrs.expired"],
                            [">=", ["ageMonths", "$self.attrs.bornDay"], "$self.attrs.termMonths"]],
      selfInForce: [">=", "$day", 92],
      isCommencementDay: ["=", "$day", 92]
    },

    actions: [
      /* ---------------------------------------------------------- rent */
      { id: "rentNotice", actor: "party", target: "tenancy",
        label: "Give notice of a rent increase", cite: "ss. 30, 31AA",
        log: "<b>{self}</b> gives notice of a rent increase under <b>{target}</b>.",
        params: [
          { key: "pct", type: "choice", label: "Increase", options: [
            { v: "3", label: "3%" }, { v: "5", label: "5%" }, { v: "10", label: "10%" }, { v: "25", label: "25%" } ] },
          { key: "cpi", type: "choice", label: "Perth rents CPI since the initial CPI", options: [
            { v: "4", label: "up 4%" }, { v: "2", label: "up 2%" }, { v: "0", label: "unchanged" },
            { v: "rebased", label: "the ABS re-referenced the series in between" } ] },
          { key: "statesCap", label: "the notice states the amount, whether it exceeds the limit and, if it does, that court approval is needed (s. 31AA(3))" }
        ] },
      { id: "agreeInWriting", actor: "party", target: "tenancy",
        label: "Agree in writing to the proposed increase", cite: "s. 31AA(2)(b)" },
      { id: "applyAboveCap", actor: "party", target: "tenancy",
        label: "Apply to the court to increase rent above the limit", cite: "s. 31AB(2)" },
      { id: "approveIncrease", actor: "court", target: "tenancy",
        label: "Approve the increase above the limit", cite: "ss. 31AA(2)(c), 31AB" },
      { id: "refuseAndFix", actor: "court", target: "tenancy",
        label: "Refuse, and order that rent not exceed the current rent", cite: "s. 31AB(5)–(6)" },
      { id: "demandRent", actor: "party", target: "tenancy",
        label: "Demand the rent the agreement fixes", cite: "s. 31AB(8)" },

      /* --------------------------------------------------- termination */
      { id: "groundNotice", actor: "party", target: "tenancy",
        label: "Give notice of termination on a s. 64 ground", cite: "s. 64(1)–(2A)",
        log: "<b>{self}</b> gives notice of termination of <b>{target}</b> under amended s. 64.",
        params: [
          { key: "ground", type: "choice", label: "Ground (the lessor genuinely intends …)", options: [
            { v: "live", label: "to live in the premises — (a)" },
            { v: "relative", label: "that an immediate relative live there — (b)" },
            { v: "close", label: "that a person with a close relationship live there — (c)" },
            { v: "sell", label: "to sell the premises — (d)" },
            { v: "renovate", label: "to reconstruct, renovate or make major repairs — (e)" },
            { v: "otheruse", label: "to use the premises for another lawful use — (f)" } ] },
          { key: "period", type: "choice", label: "Period of notice", options: [
            { v: "60", label: "60 days" },
            { v: "92", label: "92 days (at least 3 months from any day)" },
            { v: "184", label: "184 days (at least 6 months from any day)" } ] },
          { key: "evidence", label: "accompanied by written evidence supporting the ground (s. 64(2))" },
          { key: "genuine", label: "the lessor genuinely holds the intention stated" }
        ] },
      { id: "sh71BA", actor: "party", target: "tenancy",
        label: "Give a social housing notice under s. 71BA", cite: "s. 71BA(1)–(2)",
        log: "<b>{self}</b> gives notice of termination of <b>{target}</b> under s. 71BA.",
        params: [
          { key: "ground", type: "choice", label: "Ground", options: [
            { v: "sell", label: "to sell the premises — (a)" },
            { v: "renovate", label: "to reconstruct, renovate or make major repairs — (b)" },
            { v: "otheruse", label: "to use them other than as social housing — (c)" } ] },
          { key: "period", type: "choice", label: "Period of notice", options: [
            { v: "90", label: "90 days" }, { v: "120", label: "120 days" } ] }
        ] },
      { id: "applyExtend", actor: "party", target: "tenancy",
        label: "Apply to the court to extend the notice period", cite: "ss. 64(3), 71BA(3)" },
      { id: "courtPossession", actor: "court", target: "tenancy",
        label: "Refuse the extension and order possession from the earliest day allowed",
        cite: "ss. 64(4)(c), 71BA(4)(c)" },
      { id: "tenantEndOfTerm", actor: "party", target: "tenancy",
        label: "Give notice ending the fixed term at its expiry", cite: "s. 70A(2)" },
      { id: "lessorEndOfTerm", actor: "party", target: "tenancy",
        label: "Give a lessor’s notice ending the fixed term at its expiry", cite: "previous s. 70A(2)" },
      { id: "oldNoGrounds", actor: "party", target: "tenancy",
        label: "Give notice of termination without any ground", cite: "previous s. 64(1)" },
      { id: "applyPossession", actor: "party", target: "tenancy",
        label: "Apply for termination and an order for possession", cite: "ss. 71, 72" }
    ],

    rules: [
      /* ============================ rent increases ============================ */
      { id: "rn-not-lessor", on: "action:rentNotice", "if": ["not", ["def", "selfIsLessor"]],
        then: [["log", "<b>Nothing has happened.</b> Sections 30 and 31A give the power to increase rent to the lessor. {self} is not the lessor under {target}, so the notice is of no effect.",
          { cite: "ss. 30(1), 31A(1)", sev: "ok" }], ["observe", "void-act"]] },

      { id: "rn-record", on: "action:rentNotice", "if": ["def", "selfIsLessor"],
        then: [
          ["set", "$target.attrs.rentNoticeDay", "$day"],
          ["set", "$target.attrs.rentNoticeUnderNewLaw", ["def", "inForce"]],
          ["set", "$target.attrs.rentNoticeVoid", false],
          ["set", "$target.attrs.tenantAgreed", false],
          ["set", "$target.attrs.approvedAboveCap", false],
          ["set", "$target.attrs.limitNow", ["def", "limit"]],
          ["set", "$target.attrs.proposedNow", ["def", "proposed"]],
          ["log", "Proposed increase ${target.attrs.proposedNow} a week on rent of ${target.attrs.rent}. Increase limit L = R × (current CPI − initial CPI) ÷ initial CPI × 1.1 = <b>${target.attrs.limitNow}</b>.",
            { cite: "s. 31AA(1)" }]
        ] },

      { id: "rn-s105", on: "action:rentNotice", "if": ["and", ["def", "selfIsLessor"], ["not", ["def", "inForce"]]],
        then: [["log", "This notice is given before commencement day, so s. 31AA does not apply to the increase, however large. The old s. 30 governs it to the end.",
          { cite: "s. 105", sev: "ok" }], ["observe", "s105"]] },

      { id: "rn-fixed-no-clause", on: "action:rentNotice",
        "if": ["and", ["def", "selfIsLessor"], ["def", "tDuringFixedTerm"], ["not", "$target.attrs.increaseClause"],
                      ["not", "$target.attrs.incomeBased"]],
        then: [
          ["set", "$target.attrs.rentNoticeVoid", true],
          ["log", "<b>Nothing has happened.</b> {target} is a fixed term during its currency, and s. 30(2)(a) makes the right to increase rent unexercisable unless the agreement sets out the amount or method. It does not.",
            { cite: "s. 30(2)(a)", sev: "ok" }], ["observe", "void-act"]] },

      { id: "rn-income", on: "action:rentNotice",
        "if": ["and", ["def", "selfIsLessor"], ["def", "inForce"], "$target.attrs.incomeBased"],
        then: [
          ["set", "$target.attrs.rentNoticeVoid", true],
          ["log", "<b>{target}’s rent is calculated by reference to the tenant’s income.</b> A s. 31A notice changes the <i>method</i>; the rent that results depends on income nobody yet knows. Section 31AA(3)(a) requires the notice to state “the amount of the proposed increase”, and (3)(b) whether it exceeds the limit. Neither can truthfully be stated, so on the reading the encoding takes no s. 31A change can ever take effect.",
            { cite: "ss. 31A, 31AA(3)", sev: "stop" }], ["observe", "b03"]] },

      { id: "rn-rebased", on: "action:rentNotice",
        "if": ["and", ["def", "selfIsLessor"], ["def", "inForce"], ["=", "$p.cpi", "rebased"]],
        then: [["log", "<b>The ABS re-referenced the index between the two dates.</b> The current number as published (105) is below the old-base initial number (200), so under the definition of “current CPI” it is floored to the initial CPI and the limit is nil — although rents in fact rose. The formula divides numbers “published most recently before” two different days and never says they must be on the same base.",
          { cite: "s. 31AA(1) ‘CPI’, L", sev: "stop" }], ["observe", "b04"]] },

      { id: "rn-clause", on: "action:rentNotice",
        "if": ["and", ["def", "selfIsLessor"], ["def", "inForce"], ["not", "$target.attrs.rentNoticeVoid"],
                      ["def", "aboveCap"], "$target.attrs.increaseClause"],
        then: [["log", "<b>The cap does not apply.</b> {target} sets out the amount or method of increase, and s. 31AA(2)(a) lifts the limit whenever it does. During a fixed term s. 30(2)(a) permits an increase <i>only</i> in that case, so no fixed-term increase is ever capped; and a clause in a periodic agreement works the same way. The ACT provision the Bill copies (s. 64B(1)(a)) confines this exception to fixed-term agreements signed before its own reform.",
          { cite: "ss. 30(2)(a), 31AA(2)(a)", sev: "stop" }], ["observe", "b01"]] },

      { id: "rn-above", on: "action:rentNotice",
        "if": ["and", ["def", "selfIsLessor"], ["def", "inForce"], ["not", "$target.attrs.rentNoticeVoid"],
                      ["def", "aboveCap"], ["not", "$target.attrs.increaseClause"]],
        then: [["log", "The increase is above the limit. It can take effect only if the tenant agrees in writing after this notice, or a competent court approves the amount.",
          { cite: "s. 31AA(2)(b), (c)", sev: "warn" }]] },

      { id: "rn-within", on: "action:rentNotice",
        "if": ["and", ["def", "selfIsLessor"], ["def", "inForce"], ["not", "$target.attrs.rentNoticeVoid"],
                      ["not", ["def", "aboveCap"]]],
        then: [["log", "The increase is within the limit.", { cite: "s. 31AA(2)", sev: "ok" }],
               ["observe", "within-cap"]] },

      { id: "rn-schedule", on: "action:rentNotice",
        "if": ["and", ["def", "selfIsLessor"], ["not", "$target.attrs.rentNoticeVoid"]],
        then: [
          ["log", "The increased rent can become payable no earlier than 60 days after the notice.", { cite: "s. 30(1)(a)" }],
          ["after", 60, "rid-too-soon"], ["after", 60, "rid-blocked"], ["after", 60, "rid-ok"]
        ] },

      { id: "rid-too-soon", on: "scheduled",
        "if": ["<", ["def", "tMonthsSinceIncrease"], 12],
        then: [
          ["set", "$target.attrs.rentNoticeVoid", true],
          ["log", "The day named in the notice is less than 12 months after the tenancy commenced or the rent was last increased, so the increase does not take effect.",
            { cite: "s. 30(1)(b)", sev: "warn" }]] },

      { id: "rid-blocked", on: "scheduled",
        "if": ["and", ["not", "$target.attrs.rentNoticeVoid"],
                      ["not", ["and", ["def", "amountAllowed"], ["def", "contentAllowed"]]]],
        then: [
          ["log", "<b>The day named in the notice has arrived, and the increase has neither the tenant’s written agreement nor the court’s approval.</b> What happens to the notice is fork F-1: the Bill does not amend s. 30(3), which varies the agreement by any notice “given in accordance with this section”. This model takes reading A — the notice has no effect at all.",
            { cite: "ss. 30(3), 31AA(2)", sev: "warn" }],
          ["observe", "f1"]] },

      { id: "rid-ok", on: "scheduled",
        "if": ["and", ["not", "$target.attrs.rentNoticeVoid"], ["def", "amountAllowed"], ["def", "contentAllowed"]],
        then: [
          ["set", "$target.attrs.rent", ["+", "$target.attrs.rent", ["def", "proposed"]]],
          ["set", "$target.attrs.lastIncreaseDay", "$day"],
          ["set", "$target.attrs.rentNoticeVoid", true],
          ["log", "The increase takes effect. Rent under {target} is now <b>${target.attrs.rent}</b> a week.",
            { cite: "s. 30(3)" }]] },

      { id: "agree", on: "action:agreeInWriting",
        "if": ["and", ["def", "selfIsTenant"], ["exists", "$target.attrs.rentNoticeDay"]],
        then: [["set", "$target.attrs.tenantAgreed", true],
               ["log", "{self} agrees to the increase in writing, after the notice.", { cite: "s. 31AA(2)(b)" }]] },

      { id: "agree-not-tenant", on: "action:agreeInWriting", "if": ["not", ["def", "selfIsTenant"]],
        then: [["log", "<b>Nothing has happened.</b> Only the tenant’s agreement counts.",
          { cite: "s. 31AA(2)(b)", sev: "ok" }], ["observe", "void-act"]] },

      { id: "apply-above", on: "action:applyAboveCap", "if": ["def", "selfIsLessor"],
        then: [["set", "$target.attrs.s31abPending", true],
               ["log", "{self} applies for an order approving an increase above the limit. The court must have regard to comparable rents, capital value, outgoings, services, chattels and the state of the premises.",
                 { cite: "s. 31AB(2)–(4)" }]] },

      { id: "approve", on: "action:approveIncrease",
        then: [["set", "$target.attrs.approvedAboveCap", true],
               ["set", "$target.attrs.s31abPending", false],
               ["log", "{self} approves the amount of the increase.", { cite: "s. 31AA(2)(c)" }]] },

      { id: "approve-late", on: "action:approveIncrease",
        "if": ["and", ["exists", "$target.attrs.rentNoticeDay"], [">", ["daysSince", "$target.attrs.rentNoticeDay"], 60]],
        then: [["log", "<b>The approval comes after the day the notice named.</b> On that day the increase had no approval and did not take effect. The Bill does not say whether a later approval revives the notice, needs a fresh one, or runs back. The ACT provision it copies avoids the question by requiring the tribunal’s <i>prior</i> approval; the Bill dropped “prior”.",
          { cite: "s. 31AA(2)(c), (3)(c)", sev: "warn" }], ["observe", "timing"]] },

      { id: "refuse-fix", on: "action:refuseAndFix",
        then: [
          ["set", "$target.attrs.orderDay", "$day"],
          ["set", "$target.attrs.orderMax", "$target.attrs.rent"],
          ["set", "$target.attrs.s31abPending", false],
          ["log", "{self} refuses the increase and orders that the rent payable under {target} not exceed <b>${target.attrs.orderMax}</b>. The order has effect for 1 year from today — fixed by the Bill, where the Explanatory Memorandum says “up to 1 year”.",
            { cite: "s. 31AB(5), (6)" }]] },

      { id: "demand-own", on: "action:demandRent",
        "if": ["and", ["def", "selfIsLessor"], ["def", "ownOrderInForce"], [">", "$target.attrs.rent", "$target.attrs.orderMax"]],
        then: [["log", "Offence: rent above the amount the court ordered. Fine up to $5,000.",
          { cite: "s. 31AB(8)" }], ["observe", "s31ab8"]] },

      { id: "demand-prev", on: "action:demandRent",
        "if": ["and", ["def", "selfIsLessor"], ["def", "prevOrderInForce"], ["def", "prevTenantDiffers"],
                      [">", "$target.attrs.rent", ["attrOf", ["rel", "$target", "previousAgreement"], "orderMax"]]],
        then: [
          ["log", "<b>{self} demands ${target.attrs.rent} under a new agreement with a new tenant.</b> The s. 31AB(5) order limited rent “under the residential tenancy agreement” it was made about, and that tenancy has ended. But s. 31AB(8) forbids demanding rent “from the residential premises” above the ordered amount, and s. 31AB(6) keeps the order alive for a fixed year. So this demand is an offence although no order governs this agreement. Compare s. 32(5), whose order ends with the tenancy.",
            { cite: "s. 31AB(5), (6), (8)", sev: "stop" }],
          ["observe", "b06"], ["observe", "s31ab8"]] },

      { id: "demand-not-lessor", on: "action:demandRent", "if": ["not", ["def", "selfIsLessor"]],
        then: [["log", "{self} is not the lessor under {target}. A demand for rent by a stranger is not a demand under the agreement.",
          { cite: "s. 31AB(8)", sev: "ok" }], ["observe", "void-act"]] },

      /* ================= s. 64 as amended, and s. 64(3)–(4) =================== */
      { id: "gn-not-lessor", on: "action:groundNotice", "if": ["not", ["def", "selfIsLessor"]],
        then: [["log", "<b>Nothing has happened.</b> Section 64 gives the power to the lessor.",
          { cite: "s. 64(1)", sev: "ok" }], ["observe", "void-act"]] },

      { id: "gn-not-in-force", on: "action:groundNotice",
        "if": ["and", ["def", "selfIsLessor"], ["not", ["def", "inForce"]]],
        then: [["log", "Amended s. 64 is not yet in force. Until commencement day a lessor may give notice without any ground under previous s. 64(1).",
          { cite: "cl. 2; previous s. 64", sev: "warn" }]] },

      { id: "gn-social", on: "action:groundNotice",
        "if": ["and", ["def", "selfIsLessor"], ["def", "inForce"], "$target.attrs.socialHousing"],
        then: [["log", "<b>Nothing has happened.</b> Section 64 does not apply to a social housing tenancy agreement. A social housing lessor uses s. 71BA.",
          { cite: "s. 64(5)", sev: "ok" }], ["observe", "void-act"]] },

      { id: "gn-fixed", on: "action:groundNotice",
        "if": ["and", ["def", "selfIsLessor"], ["def", "inForce"], ["not", "$target.attrs.socialHousing"], ["def", "tDuringFixedTerm"]],
        then: [["log", "<b>Nothing has happened.</b> Amended s. 64(1) reaches only an agreement that creates a periodic tenancy, and {target} is a fixed term during its currency.",
          { cite: "s. 64(1)", sev: "ok" }], ["observe", "void-act"]] },

      { id: "gn-fork", on: "action:groundNotice",
        "if": ["and", ["def", "s64Base"], "$target.attrs.fixedTerm", "$target.attrs.expired"],
        then: [["log", "{target}’s fixed term has run out without a tenant’s notice. Amended s. 70A(2) says the term “does not end”; s. 76C(2) says the agreement “continues as a periodic tenancy”. Only on the second reading can s. 64 reach it at all. This model takes the s. 76C reading, which the second reading speech leans towards (fork F-2).",
          { cite: "ss. 64(1), 70A(2), 76C(2)", sev: "warn" }], ["observe", "f2"]] },

      { id: "gn-record", on: "action:groundNotice", "if": ["def", "s64Base"],
        then: [
          ["set", "$target.attrs.termNoticeDay", "$day"],
          ["set", "$target.attrs.termNoticeKind", "s64"],
          ["set", "$target.attrs.requiredMonths", ["def", "requiredMonths"]],
          ["set", "$target.attrs.extendApplied", false],
          ["log", "Notice given on a s. 64(1) ground. Period required: 3 months for (e), 6 months for (f), 60 days otherwise.",
            { cite: "s. 64(2A)" }],
          ["after", ["floor", "$p.period"], "npe-short"], ["after", ["floor", "$p.period"], "npe-ok"]
        ] },

      { id: "gn-no-evidence", on: "action:groundNotice",
        "if": ["and", ["def", "s64Base"], ["not", "$p.evidence"]],
        then: [["log", "The notice is not accompanied by written evidence supporting the ground, so it was not given in accordance with the Act, and s. 71(2)(a) stops the court ordering possession on it.",
          { cite: "ss. 64(2), 71(2)(a)", sev: "warn" }]] },

      { id: "gn-not-genuine", on: "action:groundNotice",
        "if": ["and", ["def", "s64Base"], ["not", "$p.genuine"]],
        then: [["log", "The lessor does not genuinely hold the intention stated. If {target}’s tenant simply leaves, that is the end of it: amended s. 64 has no offence for a false ground (compare s. 63(3), $10,000), and the ground is tested only if the tenant stays and the lessor applies under s. 71.",
          { cite: "ss. 63(3), 64(1), 71(2)(b)", sev: "warn" }], ["observe", "no-false-offence"]] },

      { id: "gn-b10", on: "action:groundNotice",
        "if": ["and", ["def", "s64Base"], ["or", ["def", "ownOrderInForce"], "$target.attrs.s31abPending"]],
        then: [["log", "A s. 31AB application or order is on foot for {target}. While s. 32 proceedings or orders are on foot, s. 65 makes a s. 64 notice ineffectual; the Bill does not extend s. 65 to s. 31AB, so this notice stands.",
          { cite: "ss. 31AB, 65(1)", sev: "warn" }], ["observe", "b10"]] },

      { id: "npe-short", on: "scheduled",
        "if": ["and", ["not", "$target.attrs.terminated"], [">", "$target.attrs.requiredMonths", 0],
                      ["<", ["ageMonths", "$target.attrs.termNoticeDay"], "$target.attrs.requiredMonths"]],
        then: [["log", "The day for possession has come, but fewer than {target.attrs.requiredMonths} calendar months have run since the notice. It was not a valid notice under s. 64(2A).",
          { cite: "s. 64(2A)", sev: "warn" }]] },

      { id: "npe-ok", on: "scheduled",
        "if": ["and", ["not", "$target.attrs.terminated"],
                      ["or", ["=", "$target.attrs.requiredMonths", 0],
                             [">=", ["ageMonths", "$target.attrs.termNoticeDay"], "$target.attrs.requiredMonths"]]],
        then: [["log", "The period of notice has run. If the tenant stays, the lessor may apply under s. 71 within 30 days, and must establish the ground.",
          { cite: "ss. 60(1)(a), 71(1), 71(2)(b)", sev: "ok" }]] },

      /* ================================ s. 71BA ================================ */
      { id: "sh-not-lessor", on: "action:sh71BA", "if": ["not", ["def", "selfIsLessor"]],
        then: [["log", "<b>Nothing has happened.</b> Section 71BA gives the power to the lessor.",
          { cite: "s. 71BA(1)", sev: "ok" }], ["observe", "void-act"]] },

      { id: "sh-not-social", on: "action:sh71BA",
        "if": ["and", ["def", "selfIsLessor"], ["not", "$target.attrs.socialHousing"]],
        then: [["log", "<b>Nothing has happened.</b> Section 71BA applies only to a social housing tenancy agreement.",
          { cite: "s. 71BA(1)", sev: "ok" }], ["observe", "void-act"]] },

      { id: "sh-not-in-force", on: "action:sh71BA",
        "if": ["and", ["def", "selfIsLessor"], "$target.attrs.socialHousing", ["not", ["def", "inForce"]]],
        then: [["log", "Section 71BA is not yet in force.", { cite: "cl. 2", sev: "warn" }]] },

      { id: "sh-fixed", on: "action:sh71BA",
        "if": ["and", ["def", "selfIsLessor"], "$target.attrs.socialHousing", ["def", "inForce"], ["def", "tDuringFixedTerm"]],
        then: [["log", "<b>{target} is a fixed term during its currency.</b> Every other lessor’s notice in the Act says expressly whether it can end a fixed term early (ss. 63(4), 64(5) as it stood, 71G(1)(a), 71J(5)); s. 71BA says nothing. On its words, a social housing lessor can end the term mid-way to sell, which a private lessor cannot. The model follows the words.",
          { cite: "s. 71BA", sev: "warn" }], ["observe", "b08"]] },

      { id: "sh-record", on: "action:sh71BA",
        "if": ["and", ["def", "selfIsLessor"], "$target.attrs.socialHousing", ["def", "inForce"]],
        then: [
          ["set", "$target.attrs.termNoticeDay", "$day"],
          ["set", "$target.attrs.termNoticeKind", "s71BA"],
          ["set", "$target.attrs.requiredMonths", 0],
          ["set", "$target.attrs.extendApplied", false],
          ["log", "Notice given under s. 71BA. The period of notice must be at least 90 days.",
            { cite: "s. 71BA(2)" }]] },

      /* ================== the tenant's application, and the order ================== */
      { id: "ae-not-tenant", on: "action:applyExtend", "if": ["not", ["def", "selfIsTenant"]],
        then: [["log", "<b>Nothing has happened.</b> Only the tenant may apply.",
          { cite: "ss. 64(3), 71BA(3)", sev: "ok" }], ["observe", "void-act"]] },

      { id: "ae-none", on: "action:applyExtend",
        "if": ["and", ["def", "selfIsTenant"], ["not", ["exists", "$target.attrs.termNoticeDay"]]],
        then: [["log", "There is no notice of termination to extend.", { cite: "s. 64(3)", sev: "warn" }]] },

      { id: "ae-late", on: "action:applyExtend",
        "if": ["and", ["def", "selfIsTenant"], ["exists", "$target.attrs.termNoticeDay"],
                      [">", ["daysSince", "$target.attrs.termNoticeDay"], 7]],
        then: [["log", "Too late: the application must be made within 7 days after the notice was received.",
          { cite: "ss. 64(3), 71BA(3)", sev: "warn" }]] },

      { id: "ae-ok", on: "action:applyExtend",
        "if": ["and", ["def", "selfIsTenant"], ["exists", "$target.attrs.termNoticeDay"],
                      ["<=", ["daysSince", "$target.attrs.termNoticeDay"], 7]],
        then: [["set", "$target.attrs.extendApplied", true],
               ["log", "{self} applies for the period of notice to be extended by up to 60 days.",
                 { cite: "ss. 64(3), 71BA(3)" }]] },

      { id: "cp-none", on: "action:courtPossession", "if": ["not", "$target.attrs.extendApplied"],
        then: [["log", "No application under s. 64(3) or s. 71BA(3) is before the court.",
          { cite: "ss. 64(4), 71BA(4)", sev: "warn" }]] },

      { id: "cp-order", on: "action:courtPossession", "if": "$target.attrs.extendApplied",
        then: [
          ["set", "$target.attrs.possessionDay", ["def", "earliestPossession"]],
          ["set", "$target.attrs.possessionWait", ["-", ["def", "earliestPossession"], "$day"]],
          ["set", "$target.attrs.possessionDate", ["date", ["def", "earliestPossession"]]],
          ["set", "$target.attrs.extendApplied", false],
          ["log", "{self} refuses the extension, terminates {target} and orders possession from <b>{target.attrs.possessionDate}</b>: the later of a day not less than 60 days after the notice was received and a day within 7 days after the order.",
            { cite: "ss. 64(4)(c), 71BA(4)(c)" }],
          ["after", "$target.attrs.possessionWait", "cpd-b05-months"],
          ["after", "$target.attrs.possessionWait", "cpd-b05-days"],
          ["after", "$target.attrs.possessionWait", "cpd-terminate"]
        ] },

      { id: "cpd-b05-months", on: "scheduled",
        "if": ["and", ["=", "$target.attrs.termNoticeKind", "s64"], [">", "$target.attrs.requiredMonths", 0],
                      ["<", ["ageMonths", "$target.attrs.termNoticeDay"], "$target.attrs.requiredMonths"]],
        then: [["log", "<b>The tenant must give up possession today, before the notice period the lessor was required to give has run</b> — fewer than {target.attrs.requiredMonths} months since the notice. Section 64(4)(c) still uses the 60 days that matched the old s. 64(2); the Bill lengthened the notice periods in s. 64(2A) and left the formula alone. The tenant got here by applying for <i>more</i> time.",
          { cite: "ss. 64(2A), 64(4)(c)", sev: "stop" }], ["observe", "b05"]] },

      { id: "cpd-b05-days", on: "scheduled",
        "if": ["and", ["=", "$target.attrs.termNoticeKind", "s71BA"],
                      ["<", ["daysSince", "$target.attrs.termNoticeDay"], 90]],
        then: [["log", "<b>The tenant must give up possession today, {target.attrs.possessionWait} days after the order and short of the 90 days’ notice s. 71BA(2) requires.</b> Section 71BA(4)(c) copies the 60-day formula from s. 64(4)(c). The tenant got here by applying for more time.",
          { cite: "s. 71BA(2), (4)(c)", sev: "stop" }], ["observe", "b05"]] },

      { id: "cpd-terminate", on: "scheduled",
        then: [["set", "$target.attrs.terminated", true],
               ["log", "The order for possession takes effect, and {target} is terminated.",
                 { cite: "s. 60(1)(a)(ii)" }]] },

      /* ============================ s. 70A as amended ============================ */
      { id: "te-not-tenant", on: "action:tenantEndOfTerm", "if": ["not", ["def", "selfIsTenant"]],
        then: [["log", "<b>Nothing has happened.</b> After the Bill, only the tenant can give this notice.",
          { cite: "s. 70A(2)", sev: "ok" }], ["observe", "void-act"]] },

      { id: "te-periodic", on: "action:tenantEndOfTerm",
        "if": ["and", ["def", "selfIsTenant"], ["not", "$target.attrs.fixedTerm"]],
        then: [["log", "{target} is periodic; s. 70A is about fixed terms. A tenant ends a periodic tenancy with 21 days’ notice under s. 68.",
          { cite: "ss. 68, 70A", sev: "ok" }]] },

      { id: "te-social", on: "action:tenantEndOfTerm",
        "if": ["and", ["def", "selfIsTenant"], "$target.attrs.fixedTerm", "$target.attrs.socialHousing", ["def", "inForce"]],
        then: [["log", "<b>This is not a notice under s. 70A.</b> Amended s. 70A(2) excludes a social housing tenancy agreement, and s. 70A(1) defines “notice” as one “referred to in subsection (2)”. So s. 60(1)(b) is not open to {self}: a social housing tenant has lost the end-of-term notice every other tenant keeps. Neither the Explanatory Memorandum nor the speech gives a reason.",
          { cite: "ss. 60(1)(b), 70A(1), (2)", sev: "stop" }], ["observe", "b07"]] },

      { id: "te-ok", on: "action:tenantEndOfTerm",
        "if": ["and", ["def", "selfIsTenant"], "$target.attrs.fixedTerm",
                      ["or", ["not", "$target.attrs.socialHousing"], ["not", ["def", "inForce"]]]],
        then: [["set", "$target.attrs.tenantGaveNotice", true],
               ["log", "{self} gives notice that {target} ends at its expiry. It must be at least 30 days before the day named, and that day not before the expiry day.",
                 { cite: "s. 70A(2)–(4)" }]] },

      { id: "le-not-lessor", on: "action:lessorEndOfTerm", "if": ["not", ["def", "selfIsLessor"]],
        then: [["log", "<b>Nothing has happened.</b> {self} is not the lessor.",
          { cite: "previous s. 70A(2)", sev: "ok" }], ["observe", "void-act"]] },

      { id: "le-after", on: "action:lessorEndOfTerm",
        "if": ["and", ["def", "selfIsLessor"], ["def", "inForce"]],
        then: [["log", "<b>Nothing has happened.</b> Clause 7 took “lessor or” out of s. 70A(2): only a tenant’s notice ends a fixed term now. The lessor’s notice is not an offence and not an irregularity — it simply has no effect. {target} will run on past its expiry day.",
          { cite: "ss. 60(1)(b), 70A(2)", sev: "ok" }], ["observe", "void-act"]] },

      { id: "le-before", on: "action:lessorEndOfTerm",
        "if": ["and", ["def", "selfIsLessor"], ["not", ["def", "inForce"]], "$target.attrs.fixedTerm"],
        then: [["set", "$target.attrs.oldNotice70A", true],
               ["set", "$target.attrs.termNoticeDay", "$day"],
               ["log", "Before commencement, previous s. 70A(2) still lets the lessor end the fixed term at expiry.",
                 { cite: "previous s. 70A(2)" }]] },

      { id: "ong-not-lessor", on: "action:oldNoGrounds", "if": ["not", ["def", "selfIsLessor"]],
        then: [["log", "<b>Nothing has happened.</b> {self} is not the lessor.",
          { cite: "previous s. 64(1)", sev: "ok" }], ["observe", "void-act"]] },

      { id: "ong-after", on: "action:oldNoGrounds",
        "if": ["and", ["def", "selfIsLessor"], ["def", "inForce"]],
        then: [["log", "<b>Nothing has happened.</b> The power to give notice without any ground was replaced on commencement day; amended s. 64 needs a ground and supporting evidence.",
          { cite: "s. 64(1)–(2)", sev: "ok" }], ["observe", "void-act"]] },

      { id: "ong-before", on: "action:oldNoGrounds",
        "if": ["and", ["def", "selfIsLessor"], ["not", ["def", "inForce"]], ["not", ["def", "tDuringFixedTerm"]]],
        then: [["set", "$target.attrs.oldNotice64", true],
               ["set", "$target.attrs.termNoticeDay", "$day"],
               ["set", "$target.attrs.termNoticeKind", "old64"],
               ["log", "Notice without any ground, 60 days.", { cite: "previous s. 64(1), (2)" }]] },

      { id: "ap-lessor", on: "action:applyPossession",
        "if": ["and", ["def", "selfIsLessor"], ["exists", "$target.attrs.termNoticeDay"]],
        then: [["set", "$target.attrs.lessorApplied", true],
               ["log", "The tenant has not delivered up possession. {self} applies for an order terminating {target} and for possession.",
                 { cite: "ss. 71(1), 72(1)" }]] },

      { id: "ap-none", on: "action:applyPossession",
        "if": ["not", ["and", ["def", "selfIsLessor"], ["exists", "$target.attrs.termNoticeDay"]]],
        then: [["log", "There is no lessor’s notice for an application to rest on.",
          { cite: "ss. 71(1), 72(1)", sev: "warn" }]] },

      /* ================================ the clock ================================ */
      { id: "com-106", on: "day", "for": "tenancy",
        "if": ["and", ["def", "isCommencementDay"], "$self.attrs.oldNotice64", ["not", "$self.attrs.terminated"]],
        then: [["log", "<b>Commencement day.</b> {self}’s notice under previous s. 64(1) becomes ineffectual.",
          { cite: "s. 106(2), (4)(a)", sev: "ok" }]] },

      { id: "com-106-tenant", on: "day", "for": "tenancy",
        "if": ["and", ["def", "isCommencementDay"], "$self.attrs.oldNotice64", "$self.attrs.extendApplied"],
        then: [["set", "$self.attrs.extendApplied", false],
               ["log", "The tenant’s s. 64(3) application is taken to be dismissed.",
                 { cite: "s. 106(4)(b)", sev: "ok" }], ["observe", "v106"]] },

      { id: "com-106-lessor", on: "day", "for": "tenancy",
        "if": ["and", ["def", "isCommencementDay"], "$self.attrs.oldNotice64", "$self.attrs.lessorApplied"],
        then: [["log", "<b>The lessor’s s. 71 application is still pending, on a notice that is now ineffectual.</b> Section 106 dismisses the tenant’s s. 64(3) application and says nothing about the lessor’s. The Explanatory Memorandum says “If proceedings relating to such a notice are pending, they are taken to be dismissed.” The text does not do that.",
          { cite: "ss. 71, 106", sev: "stop" }], ["observe", "b09"]] },

      { id: "com-107", on: "day", "for": "tenancy",
        "if": ["and", ["def", "isCommencementDay"], "$self.attrs.oldNotice70A", ["not", "$self.attrs.terminated"]],
        then: [["log", "<b>Commencement day.</b> {self}’s notice under previous s. 70A(2) becomes ineffectual.",
          { cite: "s. 107(3)", sev: "ok" }]] },

      { id: "com-107-lessor", on: "day", "for": "tenancy",
        "if": ["and", ["def", "isCommencementDay"], "$self.attrs.oldNotice70A", "$self.attrs.lessorApplied"],
        then: [["log", "<b>The lessor’s s. 72 application is still pending, on a notice that is now ineffectual.</b> Section 107(5)(b) dismisses “an application by the tenant under previous section 72(1)” — but s. 72(1) has only ever let the <i>lessor</i> apply. Subsections (4) and (5) can never operate, and the application that actually exists is not dealt with. The Explanatory Memorandum says pending proceedings “are taken to be dismissed”.",
          { cite: "ss. 72(1), 107(4), (5)", sev: "stop" }], ["observe", "b09"]] },

      { id: "ex-tenant-notice", on: "day", "for": "tenancy",
        "if": ["and", ["def", "selfExpiring"], "$self.attrs.tenantGaveNotice"],
        then: [["set", "$self.attrs.terminated", true],
               ["log", "{self}’s fixed term expires on the tenant’s notice. The agreement ends when the tenant delivers up possession.",
                 { cite: "ss. 60(1)(b), 70A(2)" }]] },

      { id: "ex-old-lessor", on: "day", "for": "tenancy",
        "if": ["and", ["def", "selfExpiring"], ["not", "$self.attrs.tenantGaveNotice"], "$self.attrs.oldNotice70A",
                      ["not", ["def", "selfInForce"]]],
        then: [["log", "{self}’s fixed term expires on the lessor’s notice under previous s. 70A(2). If the tenant does not deliver up possession, the lessor may apply under s. 72 within 30 days.",
          { cite: "previous s. 70A(2); s. 72(1)" }]] },

      { id: "ex-social", on: "day", "for": "tenancy",
        "if": ["and", ["def", "selfExpiring"], ["not", "$self.attrs.tenantGaveNotice"], "$self.attrs.socialHousing",
                      ["def", "selfInForce"]],
        then: [["log", "<b>{self}’s fixed term reaches its expiry day, and amended s. 70A(2) does not apply to it.</b> Before the Bill, s. 70A(2) stopped <i>every</i> fixed term ending on its expiry day without a notice; now nothing in s. 70A stops a social housing term ending. Section 76C continues it as periodic, so the tenant is not out on the street — but the protection that was there has gone, and nothing replaced it.",
          { cite: "ss. 70A(2), 76C", sev: "stop" }], ["observe", "b07"]] },

      { id: "ex-f2", on: "day", "for": "tenancy",
        "if": ["and", ["def", "selfExpiring"], ["not", "$self.attrs.tenantGaveNotice"], ["not", "$self.attrs.socialHousing"],
                      ["def", "selfInForce"]],
        then: [["log", "{self}’s expiry day passes with no tenant’s notice. Amended s. 70A(2): the term “does not end”. Section 76C(2): the agreement “continues as a periodic tenancy”. If it is still a fixed term, s. 63(4) and amended s. 64(1) leave the lessor no ground-based route at all. This model takes the s. 76C reading (fork F-2).",
          { cite: "ss. 70A(2), 76C(2)", sev: "warn" }], ["observe", "f2"]] },

      { id: "ex-old-none", on: "day", "for": "tenancy",
        "if": ["and", ["def", "selfExpiring"], ["not", "$self.attrs.tenantGaveNotice"], ["not", "$self.attrs.oldNotice70A"],
                      ["not", ["def", "selfInForce"]]],
        then: [["log", "{self}’s expiry day passes with no notice from either side, so the term does not end and the agreement continues as periodic.",
          { cite: "previous s. 70A(2); s. 76C", sev: "ok" }]] },

      { id: "ex-set", on: "day", "for": "tenancy", "if": ["def", "selfExpiring"],
        then: [["set", "$self.attrs.expired", true]] },

      { id: "order-lapses", on: "day", "for": "tenancy",
        "if": ["and", ["exists", "$self.attrs.orderDay"], ["not", "$self.attrs.orderLapsed"],
                      [">=", ["ageMonths", "$self.attrs.orderDay"], 12]],
        then: [["set", "$self.attrs.orderLapsed", true],
               ["log", "The s. 31AB(5) order about {self} has run its year and lapses.",
                 { cite: "s. 31AB(6)", sev: "ok" }]] },

      /* ============================ coming into being ============================ */
      { id: "new-renewal", on: "create:tenancy",
        "if": ["and", ["exists", "$self.rels.previousAgreement"],
                      ["=", ["rel", "$self", "lessor"], ["rel", ["rel", "$self", "previousAgreement"], "lessor"]],
                      ["=", ["rel", "$self", "tenant"], ["rel", ["rel", "$self", "previousAgreement"], "tenant"]],
                      [">", "$self.attrs.rent", ["attrOf", ["rel", "$self", "previousAgreement"], "rent"]]],
        then: [
          ["set", "$self.attrs.risePct", ["floor", ["*", 100,
            ["/", ["-", "$self.attrs.rent", ["attrOf", ["rel", "$self", "previousAgreement"], "rent"]],
                  ["attrOf", ["rel", "$self", "previousAgreement"], "rent"]]]]],
          ["log", "<b>The rent rises {self.attrs.risePct}% by a new agreement with the same lessor and tenant.</b> Section 31B treats this as a continuation — but only “for the purposes of working out” when rent was last increased. Section 31AA governs increases “under section 30 or 31A”, and this is neither, so the cap does not reach it. The ACT provision the Bill copies does (s. 64AE, “consecutive tenancy agreement”).",
            { cite: "ss. 31AA(2), 31B", sev: "stop" }], ["observe", "b02"]] },

      { id: "new-after-order", on: "create:tenancy",
        "if": ["and", ["exists", "$self.rels.previousAgreement"],
                      ["exists", ["attrOf", ["rel", "$self", "previousAgreement"], "orderDay"]],
                      ["<", ["ageMonths", ["attrOf", ["rel", "$self", "previousAgreement"], "orderDay"]], 12],
                      [">", "$self.attrs.rent", ["attrOf", ["rel", "$self", "previousAgreement"], "orderMax"]]],
        then: [["log", "A s. 31AB(5) order about the previous agreement at these premises is still within its year, and {self}’s rent is above the amount it fixed.",
          { cite: "s. 31AB(6), (8)", sev: "warn" }]] }
    ],

    observations: [
      { id: "b01", ref: "B-01", sev: "stop", label: "Cap switched off by the agreement", cite: "ss. 30(2)(a), 31AA(2)(a)",
        what: "An above-limit increase under an agreement that sets out the amount or method.",
        why: "During a fixed term that is the only way rent can rise at all, so the cap never reaches a fixed term; in a periodic agreement a standard clause does the same. The ACT model confines the exception to leases signed before its reform." },
      { id: "b02", ref: "B-02", sev: "stop", label: "Renewal raises rent outside the cap", cite: "ss. 31AA(2), 31B",
        what: "A new agreement with the same lessor and tenant at a higher rent.",
        why: "Not an increase under s. 30 or s. 31A, so s. 31AA never engages. The ACT model reaches it." },
      { id: "b03", ref: "B-03", sev: "stop", label: "Income-based rent cannot comply", cite: "ss. 31A, 31AA(3)",
        what: "A rent-method change for income-based rent after commencement.",
        why: "The notice must state an amount that depends on income not yet known." },
      { id: "b04", ref: "B-04", sev: "stop", label: "Index re-referenced between the two dates", cite: "s. 31AA(1)",
        what: "An increase where the CPI series changed reference base between the initial and current CPI.",
        why: "Numbers on different bases are divided as if they were comparable; the limit collapses to nil." },
      { id: "b05", ref: "B-05", sev: "stop", label: "Possession before the notice period has run", cite: "ss. 64(4)(c), 71BA(4)(c)",
        what: "A court order for possession on the tenant’s own application to extend.",
        why: "The 60-day formula survives from old s. 64(2) and undercuts the new 3-month, 6-month and 90-day periods." },
      { id: "b06", ref: "B-06", sev: "stop", label: "Rent order outlives the tenancy it governs", cite: "s. 31AB(5), (6), (8)",
        what: "A demand from a new tenant within the year of an order about the previous agreement.",
        why: "The order speaks of the agreement; the offence speaks of the premises; the year is fixed." },
      { id: "b07", ref: "B-07", sev: "stop", label: "Social housing loses s. 70A", cite: "s. 70A(2)",
        what: "A social housing fixed term at its end: the tenant’s notice, or its expiry day.",
        why: "The carve-out removes the protection and the tenant’s notice without replacing either." },
      { id: "b08", ref: "B-08", sev: "warn", label: "s. 71BA silent on a fixed term", cite: "s. 71BA",
        what: "A s. 71BA notice during a social housing fixed term.",
        why: "Every comparable provision says whether it can end a fixed term early; this one does not." },
      { id: "b09", ref: "B-09", sev: "stop", label: "Lessor’s case survives its void notice", cite: "ss. 106, 107",
        what: "A lessor’s s. 71 or s. 72 application pending on commencement day.",
        why: "The transitional provisions dismiss only the tenant’s applications — in s. 107 one that cannot exist — though the EM says all pending proceedings are dismissed." },
      { id: "b10", ref: "B-10", sev: "warn", label: "s. 65 does not reach s. 31AB", cite: "ss. 31AB, 65",
        what: "A s. 64 notice while a s. 31AB application or order is on foot.",
        why: "The protection for s. 32 proceedings was not extended to the new ones." },
      { id: "f1", ref: "F-1", sev: "warn", label: "Non-compliant rent notice: effect unstated", cite: "ss. 30(3), 31AA",
        what: "An increase reaches its day without the limit being met or excused.",
        why: "Section 30(3) is unamended. The model takes reading A: no effect at all." },
      { id: "f2", ref: "F-2", sev: "warn", label: "Fixed term or periodic after expiry", cite: "ss. 70A(2), 76C",
        what: "A fixed term passes its expiry day with no tenant’s notice.",
        why: "Which one it is decides whether the lessor has any s. 64 route. The model takes the s. 76C reading." },
      { id: "timing", sev: "warn", label: "Court approval after the notice’s day", cite: "s. 31AA(2)(c)",
        what: "A court approves an above-limit increase after the day the notice named.",
        why: "The Bill dropped the ACT model’s word “prior” and says nothing about what a late approval does." },
      { id: "no-false-offence", sev: "warn", label: "False ground, no offence", cite: "ss. 63(3), 64",
        what: "A s. 64 notice on a ground the lessor does not genuinely hold.",
        why: "Tested only if the tenant stays; s. 63(3) punishes a false sale notice, s. 64 punishes nothing." },
      { id: "s31ab8", sev: "warn", label: "Rent above a court order", cite: "s. 31AB(8)",
        what: "A demand above the amount a s. 31AB(5) order fixed.",
        why: "Offence, fine up to $5,000. Counted so B-06 can be seen against the ordinary case." },
      { id: "within-cap", sev: "ok", label: "Increase within the limit", cite: "s. 31AA(2)",
        what: "An increase at or below the increase limit.",
        why: "The cap working as intended." },
      { id: "s105", ref: "V-01", sev: "ok", label: "Pre-commencement notice left alone", cite: "s. 105",
        what: "A rent notice given before commencement day.",
        why: "Sound: s. 31AA does not apply to it." },
      { id: "v106", sev: "ok", label: "Tenant’s s. 64(3) application dismissed", cite: "s. 106(4)(b)",
        what: "A tenant’s application pending on commencement day on an old no-grounds notice.",
        why: "Sound, and the contrast that makes B-09 visible." },
      { id: "void-act", sev: "ok", label: "An act of no effect", cite: "ss. 30, 64, 70A, 71BA",
        what: "Somebody without the power purports to exercise it, or uses a power the Bill removed.",
        why: "Not an offence — simply nothing. The lessor’s end-of-term notice after commencement is the one the Bill creates." }
    ]
  };

  /* ======================= Cat Act 2011 (WA) ============================ */
  /* Encoding: subjects/western-australia/cat-act-2011/. Part 2 Divisions 1-3
     of the Act and the Cat Regulations 2012 regs 9, 10, 12, 17, 18 and Sch. 3,
     as the L4 modules read them, with the readings they take at FORK-1
     (renewal: 11-31 October) and FORK-2-B (the six-month duties are breached
     only when the owner fails to act with all convenient speed, Interpretation
     Act 1984 s 63). Refs are to the subject's INCIDENTS.md and fork register;
     observations with no ref were raised here and are not yet in the register. */

  var CAT_ACT = {
    id: "cat-act",
    title: "Cat Act 2011",
    jurisdiction: "Western Australia",
    status: "In force · compilation 00-l0-01, 25 Sep 2025 · Cat Regulations 2012, 02-b0-00",
    scope: "Part 2, with the Interpretation Act 1984 s. 63 (all convenient speed): s. 5 (registration), s. 6 (tags) and reg. 10, s. 7 (tag interference), s. 9 (the decision on an application) and regs 9, 12 and Sch. 3, ss. 14–15 (microchipping) and reg. 17, ss. 18–21 (sterilisation) and reg. 18.",
    startDate: "2026-01-01",
    dayLabel: "Day",

    types: [
      { id: "localgov", label: "Local government", band: 0, shape: "rect",
        create: { nameHint: "City of Fremantle", fields: [], rels: [] } },

      { id: "person", label: "Person", band: 1, shape: "rect",
        create: { nameHint: "Anne", bornVerb: "Born", fields: [
          { key: "bornDay", type: "age", origin: "birth", unit: "years", label: "Age in years", def: 40,
            cite: "s. 9(2)(a)", note: "An applicant under 18 is refused registration outright." },
          { key: "isVeterinarian", type: "bool", origin: "exogenous", cite: "s. 3(1)",
            label: "Is a veterinarian", note: "Settled by the Veterinary Practice Act 2021, so it is taken as given." },
          { key: "isImplanter", type: "bool", origin: "exogenous", cite: "reg. 7",
            label: "Is a microchip implanter", note: "Authorised under other law; a veterinarian usually is one too." },
          { key: "isApprovedBreeder", type: "bool", origin: "exogenous", cite: "ss. 3(1), 37",
            label: "Is an approved cat breeder",
            note: "Approval to breed is granted under Part 3 Division 4, which is not encoded, so it is taken as given." },
          { key: "offences", type: "number", origin: "exogenous", def: 0, min: 0, cite: "s. 9(2)(e)",
            label: "Convictions in the last 3 years under this Act, the Dog Act or the Animal Welfare Act" }
        ], rels: [] } },

      { id: "cat", label: "Cat", band: 2, shape: "round",
        create: { nameHint: "Smudge", bornVerb: "Born", fields: [
          { key: "bornDay", type: "age", origin: "birth", unit: "months", label: "Age in months", def: 8,
            cite: "ss. 5(1), 14(1), 18(1)", note: "Every duty in Part 2 attaches at six months." },
          { key: "ownedForBreeding", type: "bool", origin: "exogenous", cite: "s. 18(2)(b)",
            label: "Is owned for the purpose of breeding",
            note: "A fact about the owner’s purpose, not the cat. It exempts the cat from sterilisation only if the owner is an approved breeder." },
          { key: "custody", type: "choice", origin: "exogenous", def: "none", cite: "reg. 9(2)",
            label: "In the custody of",
            options: [
              { v: "none", label: "nobody listed in reg. 9(2)" },
              { v: "Cat Haven", label: "Cat Haven — reg. 9(2)(a)" },
              { v: "RSPCA", label: "the RSPCA in WA — reg. 9(2)(b)" },
              { v: "cat management facility", label: "a cat management facility — reg. 9(2)(d)" },
              { v: "veterinary premises", label: "veterinary premises — reg. 9(2)(e)" } ] },
          { key: "microchipped", type: "bool", origin: "conferred", by: "microchip", cite: "s. 3(1)", label: "Is microchipped" },
          { key: "sterilised", type: "bool", origin: "conferred", by: "sterilise", cite: "s. 3(1)",
            label: "Is sterilised (made permanently infertile by a surgical procedure)" },
          { key: "sterilisedByVet", type: "bool", origin: "conferred", by: "sterilise", cite: "s. 18(1)",
            label: "Was sterilised by a veterinarian" },
          { key: "wearingTag", type: "bool", origin: "conferred", by: "register", cite: "ss. 6(1), 11(1)(c)",
            label: "Is wearing its registration tag" }
        ], rels: [
          { key: "owner", label: "Owned by", target: "person", required: true, origin: "innate", cite: "s. 4" },
          { key: "registeredWith", label: "Registered with", target: "localgov", origin: "conferred", by: "register", cite: "s. 9" }
        ] } }
    ],

    relLabels: { owner: "owned by", registeredWith: "registered with" },

    entities: [
      { id: "lg1", type: "localgov", label: "City of Perth" },
      { id: "p1", type: "person", label: "Anne", note: "owner",
        attrs: { bornDate: "1985-03-14", isVeterinarian: false, isImplanter: false, isApprovedBreeder: false, offences: 0 } },
      { id: "p2", type: "person", label: "Dr Singh", note: "veterinarian",
        attrs: { bornDate: "1979-09-02", isVeterinarian: true, isImplanter: true, isApprovedBreeder: false, offences: 0 } },
      { id: "p3", type: "person", label: "Ben", note: "approved breeder",
        attrs: { bornDate: "1970-06-21", isVeterinarian: false, isImplanter: false, isApprovedBreeder: true, offences: 0 } },
      { id: "p4", type: "person", label: "Jo", note: "neighbour",
        attrs: { bornDate: "1992-11-30", isVeterinarian: false, isImplanter: false, isApprovedBreeder: false, offences: 0 } },
      { id: "c1", type: "cat", label: "Mittens", note: "registered",
        attrs: { bornDate: "2024-05-01", ownedForBreeding: false, custody: "none", microchipped: true, sterilised: true,
                 sterilisedByVet: true, wearingTag: true, keptSinceDay: -400, regExpiryDay: 303, sixMonthsSeen: true },
        rels: { owner: "p1", registeredWith: "lg1" } },
      { id: "c2", type: "cat", label: "Smudge", note: "nothing done",
        attrs: { bornDate: "2025-05-01", ownedForBreeding: false, custody: "none", microchipped: false, sterilised: false,
                 sterilisedByVet: false, wearingTag: false, keptSinceDay: -200, sixMonthsSeen: true },
        rels: { owner: "p1" } }
    ],

    defs: {
      ageMonths: ["ageMonths", "$self.attrs.bornDay"],
      tMonths: ["ageMonths", "$target.attrs.bornDay"],
      tOwner: ["rel", "$target", "owner"],
      selfIsVet: ["=", "$self.attrs.isVeterinarian", true],
      selfMayImplant: ["or", "$self.attrs.isImplanter", "$self.attrs.isVeterinarian"],

      /* reg. 9: custody, or foster care placed by Cat Haven or the RSPCA, or by a SAFE entity for no more than 12 weeks */
      selfFosterExempt: ["and", ["exists", "$self.attrs.fosterDay"],
                          ["or", ["!=", "$self.attrs.fosterPlacer", "SAFE"], ["<=", ["daysSince", "$self.attrs.fosterDay"], 84]]],
      tFosterExempt: ["and", ["exists", "$target.attrs.fosterDay"],
                       ["or", ["!=", "$target.attrs.fosterPlacer", "SAFE"], ["<=", ["daysSince", "$target.attrs.fosterDay"], 84]]],
      selfClassExempt: ["or", ["!=", "$self.attrs.custody", "none"], ["def", "selfFosterExempt"]],
      tClassExempt: ["or", ["!=", "$target.attrs.custody", "none"], ["def", "tFosterExempt"]],

      /* ss. 14(2)-(3), 18(2)(a), (3), on the reading taken at FORK-2: a certificate works only if given at six months or older */
      tChipExempt: ["and", ["exists", "$target.attrs.certChipAge"], [">=", "$target.attrs.certChipAge", 6]],
      selfChipExempt: ["and", ["exists", "$self.attrs.certChipAge"], [">=", "$self.attrs.certChipAge", 6]],
      tSterExempt: ["or", ["and", ["exists", "$target.attrs.certSterAge"], [">=", "$target.attrs.certSterAge", 6]],
                          ["and", ["attrOf", ["def", "tOwner"], "isApprovedBreeder"], "$target.attrs.ownedForBreeding"]],
      selfSterExempt: ["or", ["and", ["exists", "$self.attrs.certSterAge"], [">=", "$self.attrs.certSterAge", 6]],
                             ["and", ["attrOf", ["rel", "$self", "owner"], "isApprovedBreeder"], "$self.attrs.ownedForBreeding"]],

      /* s. 9(2): the grounds on which refusal is mandatory — and, by "if, and only if", the only ones */
      gChild: ["<", ["ageYears", ["attrOf", ["def", "tOwner"], "bornDay"]], 18],
      gChip: ["and", ["not", "$target.attrs.microchipped"], ["not", ["def", "tChipExempt"]]],
      gSter: ["and", ["not", "$target.attrs.sterilised"], ["not", ["def", "tSterExempt"]]],
      gOffences: [">=", ["attrOf", ["def", "tOwner"], "offences"], 2],
      anyGround: ["or", ["def", "gChild"], ["def", "tClassExempt"], ["def", "gChip"], ["def", "gSter"], ["def", "gOffences"]],

      daysToOct31: ["-", ["nextDate", 10, 31], "$day"],
      selfDutyAge: [">=", ["def", "ageMonths"], 6]
    },

    actions: [
      { id: "register", actor: "localgov", target: "cat", label: "Decide an application to register the cat", cite: "s. 9(1), (2)",
        log: "<b>{self}</b> decides an application to register <b>{target}</b>.",
        params: [ { key: "period", type: "choice", label: "For how long?", options: [
          { v: "one", label: "one year, to the next 31 October — reg. 12(2)(a)(i)" },
          { v: "three", label: "3 years — reg. 12(2)(a)(ii)" },
          { v: "life", label: "the life of the cat — reg. 12(2)(a)(iii)" } ] } ] },
      { id: "renew", actor: "localgov", target: "cat", label: "Renew the registration", cite: "reg. 12(2)(b)",
        log: "<b>{self}</b> considers an application to renew <b>{target}</b>’s registration." },
      { id: "requireDocs", actor: "localgov", target: "cat", label: "Require documents for the application", cite: "s. 9(5)",
        params: [ { key: "days", type: "choice", label: "Within how many days?", options: [
          { v: "14", label: "14 days" }, { v: "21", label: "21 days" }, { v: "30", label: "30 days" } ] } ] },
      { id: "supplyDocs", actor: "person", target: "cat", label: "Supply the documents asked for", cite: "s. 9(5)" },
      { id: "refuseToConsider", actor: "localgov", target: "cat", label: "Refuse to consider the application", cite: "s. 9(6)",
        log: "<b>{self}</b> refuses to consider the application to register <b>{target}</b>." },
      { id: "microchip", actor: "person", target: "cat", label: "Implant a microchip", cite: "ss. 14, 15",
        log: "<b>{self}</b> implants a microchip in <b>{target}</b>." },
      { id: "sterilise", actor: "person", target: "cat", label: "Sterilise the cat", cite: "ss. 18, 20, 21",
        log: "<b>{self}</b> sterilises <b>{target}</b>." },
      { id: "certify", actor: "person", target: "cat", label: "Certify that a procedure may harm the cat", cite: "ss. 14(2), 18(2)(a)",
        params: [ { key: "about", type: "choice", label: "Which procedure?", options: [
          { v: "chip", label: "implanting a microchip — s. 14(2)" },
          { v: "ster", label: "sterilisation — s. 18(2)(a)" } ] } ] },
      { id: "placeFoster", actor: "person", target: "cat", label: "Place the cat in foster care", cite: "reg. 9(3)",
        params: [ { key: "placer", type: "choice", label: "Placed by", options: [
          { v: "SAFE", label: "a SAFE entity — exempt for 12 weeks, reg. 9(3)(b)" },
          { v: "Cat Haven", label: "Cat Haven — reg. 9(3)(a)(i)" },
          { v: "RSPCA", label: "the RSPCA in WA — reg. 9(3)(a)(ii)" } ] } ] },
      { id: "goOut", actor: "cat", label: "Go out into a public place", cite: "s. 6(1)",
        log: "<b>{self}</b> goes out into a public place." },
      { id: "comeHome", actor: "cat", label: "Come home", cite: "s. 6(1)", log: "<b>{self}</b> comes home." },
      { id: "loseTag", actor: "cat", label: "Lose its registration tag", cite: "s. 6(1)", log: "<b>{self}</b> loses its tag." },
      { id: "exhibit", actor: "person", target: "cat", label: "Exhibit the cat at a cat show", cite: "reg. 10",
        params: [ { key: "host", type: "choice", label: "Held by", options: [
          { v: "listed", label: "the Cat Owners’ Association of WA, or another body listed in reg. 10(1)" },
          { v: "unlisted", label: "a body not listed in reg. 10(1)" } ] } ] },
      { id: "removeTag", actor: "person", target: "cat", label: "Remove the cat’s registration tag", cite: "s. 7",
        params: [ { key: "excuse", label: "with a reasonable excuse" } ] },
      { id: "tattoo", actor: "person", target: "cat", label: "Tattoo the cat’s ear as sterilised", cite: "s. 19, reg. 18" },
      { id: "sitOnIt", actor: "person", target: "cat", label: "Fail to act with all convenient speed", cite: "Interpretation Act 1984 s. 63",
        log: "<b>{self}</b> has not acted with all convenient speed about <b>{target}</b>. Whether that is so is a judgment the Act leaves to a court; here it is supplied, as the encoding supplies it." }
    ],

    rules: [
      /* ------------------------------------------------ deciding an application */
      { id: "reg-child", on: "action:register", "if": ["def", "gChild"],
        then: [["log", "The applicant is under 18, so the application must be refused.", { cite: "s. 9(2)(a)", sev: "warn" }]] },
      { id: "reg-class", on: "action:register", "if": ["def", "tClassExempt"],
        then: [["log", "{target} belongs to a class prescribed as exempt from registration, so the application must be refused.",
          { cite: "s. 9(2)(b), reg. 9", sev: "warn" }]] },
      { id: "reg-chip", on: "action:register", "if": ["def", "gChip"],
        then: [["log", "{target} is not microchipped and not exempt, so the application must be refused.", { cite: "s. 9(2)(c), (3)", sev: "warn" }]] },
      { id: "reg-ster", on: "action:register", "if": ["def", "gSter"],
        then: [["log", "{target} is not sterilised and not exempt, so the application must be refused.", { cite: "s. 9(2)(d), (4)", sev: "warn" }]] },
      { id: "reg-offences", on: "action:register", "if": ["def", "gOffences"],
        then: [["log", "The applicant has two or more convictions in the last three years, so the application must be refused.",
          { cite: "s. 9(2)(e)", sev: "warn" }]] },
      { id: "reg-a04", on: "action:register", "if": ["def", "anyGround"],
        then: [
          ["log", "Refusal here is a duty, not a choice: s. 9(2) says the local government <i>must</i> refuse “if, and only if” a ground applies. The Explanatory Memorandum to the Cat Bill describes the same subclauses as ones on which a local government “<i>can</i> refuse”. A council that followed the memorandum would think it had a discretion it does not have.",
            { cite: "s. 9(2); EM cl. 9", sev: "warn" }],
          ["observe", "a04"]
        ] },
      { id: "reg-a02", on: "action:register",
        "if": ["and", ["not", ["def", "anyGround"]], "$target.attrs.sterilised", ["not", "$target.attrs.sterilisedByVet"]],
        then: [
          ["log", "<b>{target} was sterilised, but not by a veterinarian.</b> It is “sterilised” as s. 3(1) defines the word — “made permanently infertile by a surgical procedure” — so ground (d) does not apply and, by “if, and only if”, the local government may not refuse. Yet s. 18(1) requires the owner to ensure the cat is sterilised <i>by a veterinarian</i>, so the owner is in breach of the Act while the registration goes through.",
            { cite: "ss. 3(1), 9(2)(d), 18(1)", sev: "stop" }],
          ["observe", "a02"]
        ] },
      { id: "reg-grant", on: "action:register", "if": ["not", ["def", "anyGround"]],
        then: [
          ["set", "$target.rels.registeredWith", "$self.id"],
          ["set", "$target.attrs.wearingTag", true],
          ["set", "$target.attrs.regLife", ["=", "$p.period", "life"]],
          ["set", "$target.attrs.regExpiryDay", ["if", ["=", "$p.period", "three"], ["nextDate", 10, 31, 2], ["nextDate", 10, 31]]],
          ["set", "$target.attrs.regExpiryDate", ["date", ["if", ["=", "$p.period", "three"], ["nextDate", 10, 31, 2], ["nextDate", 10, 31]]]],
          ["set", "$target.attrs.docsDay", null],
          ["log", "No ground in s. 9(2) applies, so refusal is forbidden: {target} is registered, and its owner is given a registration tag.",
            { cite: "ss. 9(2), 11(1)(c)", sev: "ok" }]
        ] },
      { id: "reg-grant-fixed", on: "action:register", "if": ["and", ["not", ["def", "anyGround"]], ["!=", "$p.period", "life"]],
        then: [["log", "The registration has effect until {target.attrs.regExpiryDate}.", { cite: "reg. 12(2)(a)" }]] },
      { id: "reg-grant-life", on: "action:register", "if": ["and", ["not", ["def", "anyGround"]], ["=", "$p.period", "life"]],
        then: [["log", "Registered for life: it has effect until the cat dies. The fee is $100.", { cite: "reg. 12(2)(a)(iii), Sch. 3 item 3" }]] },
      { id: "reg-fee-half", on: "action:register",
        "if": ["and", ["not", ["def", "anyGround"]], ["=", "$p.period", "one"], ["<=", ["def", "daysToOct31"], 152]],
        then: [
          ["set", "$target.attrs.regWeeks", ["floor", ["/", ["def", "daysToOct31"], 7]]],
          ["log", "The registration will run only about {target.attrs.regWeeks} weeks, to 31 October — but a first grant after 31 May is charged $10, half the one-year fee. The short first period is priced in.",
            { cite: "reg. 12(2)(a)(i), Sch. 3 item 1(a)", sev: "ok" }],
          ["observe", "v01"]
        ] },
      { id: "reg-fee-full", on: "action:register",
        "if": ["and", ["not", ["def", "anyGround"]], ["=", "$p.period", "one"], [">", ["def", "daysToOct31"], 152]],
        then: [["log", "The fee for one year is $20.", { cite: "Sch. 3 item 1(b)" }]] },
      { id: "reg-fee-three", on: "action:register", "if": ["and", ["not", ["def", "anyGround"]], ["=", "$p.period", "three"]],
        then: [["log", "The fee for 3 years is $42.50.", { cite: "Sch. 3 item 2" }]] },

      /* ------------------------------------------------ renewal, and FORK-1 */
      { id: "renew-none", on: "action:renew", "if": ["not", ["exists", "$target.rels.registeredWith"]],
        then: [["log", "{target} is not registered, so there is nothing to renew. A lapsed registration is granted again, not renewed.",
          { cite: "s. 9(1)", sev: "warn" }]] },
      { id: "renew-early", on: "action:renew",
        "if": ["and", ["exists", "$target.rels.registeredWith"], [">", ["def", "daysToOct31"], 20]],
        then: [["log", "It is too early. A renewal takes effect from 1 November and may be applied for only within the preceding 21 days.",
          { cite: "reg. 12(2)(b)", sev: "warn" }]] },
      { id: "renew-fork", on: "action:renew",
        "if": ["and", ["exists", "$target.rels.registeredWith"], ["=", ["def", "daysToOct31"], 20]],
        then: [
          ["log", "<b>Today is 11 October.</b> “Within the preceding period of 21 days” before 1 November is either 11–31 October (21 days counted back including 31 October) or 12–31 October (21 clear days). The encoding takes 11–31 October, so the renewal is in time; on the other reading it is a day early.",
            { cite: "reg. 12(2)(b)", sev: "warn" }],
          ["observe", "f1"]
        ] },
      { id: "renew-do", on: "action:renew",
        "if": ["and", ["exists", "$target.rels.registeredWith"], ["<=", ["def", "daysToOct31"], 20], [">=", ["def", "daysToOct31"], 0]],
        then: [
          ["set", "$target.attrs.regExpiryDay", ["nextDate", 10, 31, 1]],
          ["set", "$target.attrs.regExpiryDate", ["date", ["nextDate", 10, 31, 1]]],
          ["log", "Renewed from 1 November, until {target.attrs.regExpiryDate}.", { cite: "reg. 12(2)(b)", sev: "ok" }]
        ] },

      /* ------------------------------------------ documents, and refusing to consider */
      { id: "docs-too-long", on: "action:requireDocs", "if": [">", ["floor", "$p.days"], 21],
        then: [["log", "<b>Nothing has happened.</b> A requirement under s. 9(5) may allow “not more than 21 days”. One that allows {p.days} is outside the power.",
          { cite: "s. 9(5)", sev: "ok" }], ["observe", "void-act"]] },
      { id: "docs-set", on: "action:requireDocs", "if": ["<=", ["floor", "$p.days"], 21],
        then: [
          ["set", "$target.attrs.docsDay", "$day"],
          ["set", "$target.attrs.docsDays", ["floor", "$p.days"]],
          ["set", "$target.attrs.docsSupplied", false],
          ["log", "The applicant must supply the documents within {target.attrs.docsDays} days.", { cite: "s. 9(5)" }]
        ] },
      { id: "docs-supplied", on: "action:supplyDocs", "if": ["exists", "$target.attrs.docsDay"],
        then: [["set", "$target.attrs.docsSupplied", true],
               ["log", "The documents are supplied.", { cite: "s. 9(5)", sev: "ok" }]] },
      { id: "rtc-no-requirement", on: "action:refuseToConsider", "if": ["not", ["exists", "$target.attrs.docsDay"]],
        then: [["log", "<b>Nothing has happened.</b> The power in s. 9(6) arises only when a requirement under s. 9(5) has not been met in time.",
          { cite: "s. 9(6)", sev: "ok" }], ["observe", "void-act"]] },
      { id: "rtc-too-soon", on: "action:refuseToConsider",
        "if": ["and", ["exists", "$target.attrs.docsDay"], ["not", "$target.attrs.docsSupplied"],
                      ["<=", ["daysSince", "$target.attrs.docsDay"], "$target.attrs.docsDays"]],
        then: [["log", "The time allowed has not run yet.", { cite: "s. 9(6)", sev: "warn" }]] },
      { id: "rtc-supplied", on: "action:refuseToConsider", "if": ["and", ["exists", "$target.attrs.docsDay"], "$target.attrs.docsSupplied"],
        then: [["log", "The documents were supplied, so the power to refuse to consider does not arise.", { cite: "s. 9(6)", sev: "ok" }]] },
      { id: "rtc-a04", on: "action:refuseToConsider",
        "if": ["and", ["exists", "$target.attrs.docsDay"], ["not", "$target.attrs.docsSupplied"],
                      [">", ["daysSince", "$target.attrs.docsDay"], "$target.attrs.docsDays"]],
        then: [
          ["log", "<b>The application is now neither granted nor refused.</b> Section 9(1) says that on receiving an application a local government “is to” grant or refuse it, and s. 9(2) allows refusal “if, and only if” a listed ground applies. Section 9(6) adds a third course — refusing to <i>consider</i> — that s. 9(1) does not offer and s. 9(2) does not list. Whether the application is then refused, or simply left undecided, the Act does not say.",
            { cite: "s. 9(1), (2), (6)", sev: "stop" }],
          ["observe", "rtc"]
        ] },

      /* ------------------------------------------------ microchipping */
      { id: "chip-not-implanter", on: "action:microchip", "if": ["not", ["def", "selfMayImplant"]],
        then: [["log", "<b>Nothing has happened.</b> {self} is not a microchip implanter, and “microchipped” means implanted in a prescribed manner.",
          { cite: "s. 3(1), reg. 7", sev: "ok" }], ["observe", "void-act"]] },
      { id: "chip-do", on: "action:microchip", "if": ["def", "selfMayImplant"],
        then: [
          ["set", "$target.attrs.microchipped", true],
          ["log", "{target} is microchipped. {self} must give the database company the prescribed information within 7 days — among it the cat’s age, breed, colour, gender and sterilisation status.",
            { cite: "s. 15, reg. 17", sev: "ok" }]
        ] },
      { id: "chip-a03", on: "action:microchip", "if": ["and", ["def", "selfMayImplant"], "$target.attrs.sterilised"],
        then: [
          ["log", "{target} was sterilised before it was microchipped, so no notice was owed under s. 20 at the time. It is not lost: the implanter reports the sterilisation status now.",
            { cite: "ss. 15, 20, reg. 17(m)", sev: "ok" }],
          ["observe", "a03"]
        ] },

      /* ------------------------------------------------ sterilisation */
      { id: "ster-vet", on: "action:sterilise", "if": ["def", "selfIsVet"],
        then: [
          ["set", "$target.attrs.sterilised", true],
          ["set", "$target.attrs.sterilisedByVet", true],
          ["log", "{target} is sterilised by a veterinarian, and {self} must give its owner a certificate of sterilisation.",
            { cite: "ss. 18(1), 21", sev: "ok" }]
        ] },
      { id: "ster-vet-chipped", on: "action:sterilise", "if": ["and", ["def", "selfIsVet"], "$target.attrs.microchipped"],
        then: [["log", "{target} is microchipped, so {self} must notify the database company of the sterilisation within 7 days.",
          { cite: "s. 20" }]] },
      { id: "ster-vet-unchipped", on: "action:sterilise", "if": ["and", ["def", "selfIsVet"], ["not", "$target.attrs.microchipped"]],
        then: [["log", "{target} has no microchip, so there is no database company to notify. Section 20 owes nothing.",
          { cite: "s. 20" }]] },
      { id: "ster-non-vet", on: "action:sterilise", "if": ["not", ["def", "selfIsVet"]],
        then: [
          ["set", "$target.attrs.sterilised", true],
          ["log", "{target} is made permanently infertile by {self}, who is not a veterinarian. It is “sterilised” for the purposes of the Act, but not in the way s. 18(1) requires, and no s. 21 certificate can issue.",
            { cite: "ss. 3(1), 18(1), 21", sev: "warn" }]
        ] },
      { id: "tattoo-false", on: "action:tattoo", "if": ["not", "$target.attrs.sterilised"],
        then: [["log", "{target} is not sterilised, and an ear tattoo is a prescribed way of identifying a cat as sterilised. Offence: a fine of $5,000.",
          { cite: "s. 19, reg. 18", sev: "stop" }]] },
      { id: "tattoo-ok", on: "action:tattoo", "if": "$target.attrs.sterilised",
        then: [["log", "{target} is sterilised, so marking it as sterilised is no offence.", { cite: "s. 19, reg. 18", sev: "ok" }]] },

      /* ------------------------------------------------ certificates, and FORK-2 */
      { id: "cert-not-vet", on: "action:certify", "if": ["not", ["def", "selfIsVet"]],
        then: [["log", "<b>Nothing has happened.</b> Only a certificate given by a veterinarian exempts a cat.",
          { cite: "ss. 14(2), 18(2)(a)", sev: "ok" }], ["observe", "void-act"]] },
      { id: "cert-chip", on: "action:certify", "if": ["and", ["def", "selfIsVet"], ["=", "$p.about", "chip"]],
        then: [["set", "$target.attrs.certChipAge", ["def", "tMonths"]],
               ["log", "{self} certifies that implanting a microchip may harm {target}, now {target.attrs.certChipAge} months old.",
                 { cite: "s. 14(2)" }]] },
      { id: "cert-ster", on: "action:certify", "if": ["and", ["def", "selfIsVet"], ["=", "$p.about", "ster"]],
        then: [["set", "$target.attrs.certSterAge", ["def", "tMonths"]],
               ["log", "{self} certifies that sterilising {target} may harm it, now {target.attrs.certSterAge} months old.",
                 { cite: "s. 18(2)(a)" }]] },
      { id: "cert-early", on: "action:certify", "if": ["and", ["def", "selfIsVet"], ["<", ["def", "tMonths"], 6]],
        then: [
          ["log", "The certificate is given before {target} is six months old, and a certificate “cannot apply in respect of a cat that is under 6 months of age”. On the encoding’s reading it is spent: it will have to be given again once {target} is six months old. Friction, not a trap — the owner is not in breach while getting a fresh one with all convenient speed.",
            { cite: "ss. 14(3), 18(3); Interpretation Act s. 63", sev: "ok" }],
          ["observe", "a01"]
        ] },

      /* ------------------------------------------------ foster care (reg. 9(3)) */
      { id: "foster", on: "action:placeFoster",
        then: [
          ["set", "$target.attrs.fosterDay", "$day"],
          ["set", "$target.attrs.fosterPlacer", "$p.placer"],
          ["set", "$target.attrs.fosterEndLogged", false],
          ["log", "{target} is placed in foster care by {p.placer}, and belongs for now to a class of cats exempt from registration.",
            { cite: "reg. 9(3)" }]
        ] },
      { id: "foster-safe", on: "action:placeFoster", "if": ["=", "$p.placer", "SAFE"],
        then: [["log", "A SAFE placement exempts the cat only while it has been in foster care for no more than 12 weeks in total. Cat Haven and RSPCA placements have no such limit.",
          { cite: "reg. 9(3)(b)", sev: "warn" }]] },

      /* ------------------------------------------------ out and about: tags */
      { id: "out", on: "action:goOut", then: [["set", "$self.attrs.inPublic", true]] },
      { id: "home", on: "action:comeHome", then: [["set", "$self.attrs.inPublic", false], ["set", "$self.attrs.exhibited", false]] },
      { id: "lose-tag", on: "action:loseTag", then: [["set", "$self.attrs.wearingTag", false]] },
      { id: "out-no-tag", on: "action:goOut",
        "if": ["and", ["exists", "$self.rels.registeredWith"], ["not", "$self.attrs.wearingTag"], ["not", "$self.attrs.exhibited"]],
        then: [["log", "{self} is registered and in a public place without its tag. Its owner commits an offence — a fine of $5,000 — unless the tag was lost by accident or another’s act despite reasonable precautions.",
          { cite: "s. 6(1), (3)", sev: "stop" }]] },
      { id: "out-unregistered", on: "action:goOut", "if": ["not", ["exists", "$self.rels.registeredWith"]],
        then: [["log", "{self} is not registered, so s. 6(1) cannot apply to it, tag or no tag. Its owner’s problem, if any, is s. 5(1).",
          { cite: "ss. 5(1), 6(1)", sev: "ok" }]] },
      { id: "exhibit-set", on: "action:exhibit",
        then: [["set", "$target.attrs.exhibited", ["=", "$p.host", "listed"]], ["set", "$target.attrs.inPublic", true]] },
      { id: "exhibit-listed", on: "action:exhibit",
        "if": ["and", ["=", "$p.host", "listed"], ["exists", "$target.rels.registeredWith"], ["not", "$target.attrs.wearingTag"]],
        then: [
          ["log", "{target} is at a listed cat show without its tag, and that is allowed. But look at how: s. 6(2) lets the regulations prescribe “a class of cats” exempt from the tag duty; reg. 10(2) instead exempts “the owner of a cat that is being exhibited … but only while that cat is being exhibited”. The effect is much the same, the form is not what s. 6(2) asks for.",
            { cite: "s. 6(2), reg. 10(2)", sev: "warn" }],
          ["observe", "a05"]
        ] },
      { id: "exhibit-unlisted", on: "action:exhibit",
        "if": ["and", ["=", "$p.host", "unlisted"], ["exists", "$target.rels.registeredWith"], ["not", "$target.attrs.wearingTag"]],
        then: [["log", "The show is not held by a body listed in reg. 10(1), so the exemption does not apply: {target} is in a public place without its tag. Offence under s. 6(1).",
          { cite: "s. 6(1), reg. 10(1)", sev: "stop" }]] },
      { id: "remove-tag", on: "action:removeTag", "if": ["not", "$p.excuse"],
        then: [["set", "$target.attrs.wearingTag", false],
               ["log", "{self} removes {target}’s registration tag without a reasonable excuse. Offence: a fine of $5,000.", { cite: "s. 7", sev: "stop" }]] },
      { id: "remove-tag-excused", on: "action:removeTag", "if": "$p.excuse",
        then: [["set", "$target.attrs.wearingTag", false],
               ["log", "{self} removes the tag with a reasonable excuse. No offence.", { cite: "s. 7", sev: "ok" }]] },

      /* ------------------------------------------------ coming into being */
      { id: "new-cat-kept", on: "create:cat",
        then: [["set", "$self.attrs.keptSinceDay", "$day"]] },
      { id: "new-cat-older", on: "create:cat", "if": ["def", "selfDutyAge"],
        then: [["set", "$self.attrs.sixMonthsSeen", true]] },

      /* ------------------------------------------------ the clock */
      { id: "six-months", on: "day", "for": "cat",
        "if": ["and", ["=", ["def", "ageMonths"], 6], ["not", "$self.attrs.sixMonthsSeen"]],
        then: [["log", "{self} is six months old today. Its owner must now ensure it is registered, microchipped and sterilised by a veterinarian, unless it is exempt — and, since the Act fixes no time, must do so with all convenient speed.",
          { cite: "ss. 5(1), 14(1), 18(1); Interpretation Act s. 63" }]] },
      { id: "six-months-cert", on: "day", "for": "cat",
        "if": ["and", ["=", ["def", "ageMonths"], 6], ["not", "$self.attrs.sixMonthsSeen"], ["not", "$self.attrs.microchipped"],
                      ["exists", "$self.attrs.certChipAge"], ["<", "$self.attrs.certChipAge", 6]],
        then: [["log", "{self}’s certificate against microchipping was given at {self.attrs.certChipAge} months, so it does not apply. The vet needs to give it again now.",
          { cite: "s. 14(3)", sev: "warn" }]] },
      { id: "six-months-seen", on: "day", "for": "cat",
        "if": ["and", ["def", "selfDutyAge"], ["not", "$self.attrs.sixMonthsSeen"]],
        then: [["set", "$self.attrs.sixMonthsSeen", true]] },

      /* a failure of all convenient speed: whichever of the three duties is still unmet is breached */
      { id: "slow-young", on: "action:sitOnIt", "if": ["<", ["def", "tMonths"], 6],
        then: [["log", "{target} is under six months old, so none of the three duties has arisen yet.", { cite: "ss. 5(1), 14(1), 18(1)", sev: "ok" }]] },
      { id: "slow-reg", on: "action:sitOnIt",
        "if": ["and", [">=", ["def", "tMonths"], 6], ["not", ["exists", "$target.rels.registeredWith"]], ["not", ["def", "tClassExempt"]],
                      [">=", ["daysSince", "$target.attrs.keptSinceDay"], 14]],
        then: [["log", "{target} is not registered. Its owner commits an offence under s. 5(1): a fine of $5,000.", { cite: "s. 5(1)", sev: "stop" }]] },
      { id: "slow-chip", on: "action:sitOnIt",
        "if": ["and", [">=", ["def", "tMonths"], 6], ["not", "$target.attrs.microchipped"], ["not", ["def", "tChipExempt"]]],
        then: [["log", "{target} is not microchipped and not exempt. Offence under s. 14(1): a fine of $5,000.", { cite: "s. 14(1)", sev: "stop" }]] },
      { id: "slow-ster", on: "action:sitOnIt",
        "if": ["and", [">=", ["def", "tMonths"], 6], ["not", "$target.attrs.sterilisedByVet"], ["not", ["def", "tSterExempt"]]],
        then: [["log", "{target} has not been sterilised by a veterinarian and is not exempt. Offence under s. 18(1): a fine of $5,000.", { cite: "s. 18(1)", sev: "stop" }]] },
      { id: "slow-mark", on: "action:sitOnIt", then: [["set", "$target.attrs.slowJudged", true]] },

      { id: "safe-lapse", on: "day", "for": "cat",
        "if": ["and", ["=", "$self.attrs.fosterPlacer", "SAFE"], ["exists", "$self.attrs.fosterDay"],
                      [">", ["daysSince", "$self.attrs.fosterDay"], 84], ["not", "$self.attrs.fosterEndLogged"]],
        then: [
          ["set", "$self.attrs.fosterEndLogged", true],
          ["set", "$self.attrs.slowJudged", false],
          ["log", "{self} has now been in SAFE foster care for more than 12 weeks, so the exemption from registration ends — on no change in the cat and none in the Act.",
            { cite: "reg. 9(3)(b)", sev: "ok" }],
          ["observe", "safe"]
        ] },

      { id: "reg-lapse", on: "day", "for": "cat",
        "if": ["and", ["exists", "$self.rels.registeredWith"], ["not", "$self.attrs.regLife"],
                      ["exists", "$self.attrs.regExpiryDay"], [">", "$day", "$self.attrs.regExpiryDay"]],
        then: [
          ["set", "$self.rels.registeredWith", null],
          ["set", "$self.attrs.wearingTag", false],
          ["set", "$self.attrs.slowJudged", false],
          ["log", "{self}’s registration ended yesterday, 31 October. Its owner must register it again with all convenient speed.", { cite: "reg. 12(2)(a)", sev: "warn" }]
        ] }
    ],

    observations: [
      { id: "a02", ref: "A-02", sev: "stop", label: "Sterilised, but not by a vet",
        cite: "ss. 3(1), 9(2)(d), 18(1)",
        what: "A cat made infertile by someone who is not a veterinarian is presented for registration.",
        why: "It is “sterilised” as defined, so s. 9(2)(d) cannot refuse it, while its owner is in breach of s. 18(1). The registration gate the Explanatory Memorandum calls the Act’s compliance mechanism does not catch this case. OPEN in the register." },
      { id: "a04", ref: "A-04", sev: "warn", label: "The memorandum describes a discretion the Act does not confer",
        cite: "s. 9(2); EM cl. 9",
        what: "An application is decided where a ground in s. 9(2) applies.",
        why: "The Act: must refuse “if, and only if” a ground applies. The Explanatory Memorandum: a local government “can” refuse. The enacted words prevail, but a council following the memorandum would misread its duty. OPEN in the register; demonstrated on stated facts, not by an #ASSERT." },
      { id: "a05", ref: "A-05", sev: "warn", label: "Reg. 10 exempts an owner, not a class of cats",
        cite: "s. 6(2), reg. 10(2)",
        what: "A registered cat is exhibited at a listed cat show without its tag.",
        why: "Section 6(2) authorises prescribing a class of cats; reg. 10(2) exempts the owner of a cat being exhibited. Same practical effect, different form. CANDIDATE: the register says a human who knows WA delegated-legislation practice should decide it." },
      { id: "rtc", sev: "warn", label: "Refusing to consider leaves the application undecided",
        cite: "s. 9(1), (2), (6)",
        what: "A local government refuses to consider an application because documents asked for under s. 9(5) did not arrive in time.",
        why: "Section 9(1) offers grant or refuse; s. 9(2) permits refusal “if, and only if” a listed ground applies; s. 9(6) adds refusal to consider. Either it is a refusal on an unlisted ground, or the application is left undetermined. Raised in the console; not yet in the subject’s register." },
      { id: "f1", ref: "FORK-1", sev: "warn", label: "Renewing on 11 October",
        cite: "reg. 12(2)(b)",
        what: "An application to renew is made on 11 October.",
        why: "“Within the preceding period of 21 days” before 1 November is 11–31 October or 12–31 October. The encoding takes the first (FORK-1-A); on the second the application is a day early." },
      { id: "a01", ref: "A-01", sev: "ok", label: "A certificate given before six months is spent",
        cite: "ss. 14(3), 18(3); Interpretation Act s. 63",
        what: "A veterinarian certifies, before a cat is six months old, that a procedure may harm it.",
        why: "Raised as a trap and retracted: the duties fix no time, so s. 63 gives the owner all convenient speed after six months (FORK-2-B), and an owner who gets a fresh certificate promptly is not in breach. The early certificate is still spent. VERIFIED-NO-DEFECT in the register." },
      { id: "a03", ref: "A-03", sev: "ok", label: "A sterilisation before microchipping is still recorded",
        cite: "ss. 15, 20, reg. 17(m)",
        what: "A cat sterilised before it was ever microchipped is microchipped later.",
        why: "Looks like a gap — s. 20 only reaches a cat already microchipped — and is not one: reg. 17(m) makes the implanter report the sterilisation status. VERIFIED-NO-DEFECT in the register." },
      { id: "v01", sev: "ok", label: "A short first registration, at half the fee",
        cite: "reg. 12(2)(a)(i), Sch. 3 item 1(a)",
        what: "A one-year registration is granted between 1 June and 31 October.",
        why: "Every one-year registration ends on 31 October, so one granted in September runs about six weeks; Sch. 3 halves the fee for a first grant after 31 May. Sound. Checked in the console; not yet in the subject’s register." },
      { id: "safe", sev: "ok", label: "A SAFE foster placement runs out at 12 weeks",
        cite: "reg. 9(3)(b)",
        what: "A cat placed in foster care by a SAFE entity passes 12 weeks there.",
        why: "Its exemption from registration ends, while one placed by Cat Haven or the RSPCA would keep it. Deliberate, and asserted in the encoding." },
      { id: "void-act", sev: "ok", label: "An act of no effect", cite: "ss. 3(1), 9(5), 9(6), 14(2)",
        what: "Somebody without the power purports to exercise it.",
        why: "Not an offence — simply nothing." }
    ],

    scenarios: [
      { label: "A kitten certified at five months, and certified again at six", focus: "@kit", mode: "nature", steps: [
        { spawn: "cat", as: "kit", label: "Pip", note: "vet says a chip may harm her",
          attrs: { bornDate: "2026-01-01", ownedForBreeding: false, custody: "none", microchipped: false, sterilised: false,
                   sterilisedByVet: false, wearingTag: false }, rels: { owner: "p1" } },
        { tick: 152 },
        { actor: "p2", action: "certify", target: "@kit", params: { about: "chip" } },
        { tick: 30 },
        { actor: "p2", action: "certify", target: "@kit", params: { about: "chip" } }
      ] },
      { label: "… or the owner sits on it", focus: "@kit", mode: "nature", steps: [
        { spawn: "cat", as: "kit", label: "Pip", note: "vet says a chip may harm her",
          attrs: { bornDate: "2026-01-01", ownedForBreeding: false, custody: "none", microchipped: false, sterilised: false,
                   sterilisedByVet: false, wearingTag: false }, rels: { owner: "p1" } },
        { tick: 152 },
        { actor: "p2", action: "certify", target: "@kit", params: { about: "chip" } },
        { tick: 90 },
        { actor: "p1", action: "sitOnIt", target: "@kit" }
      ] },
      { label: "Refused registration: the memorandum says “can”, the Act says “must”", focus: "c2", steps: [
        { actor: "lg1", action: "register", target: "c2", params: { period: "one" } }
      ] },
      { label: "Sterilised by a breeder, then registered", focus: "c2", steps: [
        { actor: "p3", action: "sterilise", target: "c2" },
        { actor: "p2", action: "microchip", target: "c2" },
        { actor: "lg1", action: "register", target: "c2", params: { period: "one" } }
      ] },
      { label: "Sterilised first, microchipped later", focus: "c2", steps: [
        { actor: "p2", action: "sterilise", target: "c2" },
        { tick: 30 },
        { actor: "p2", action: "microchip", target: "c2" }
      ] },
      { label: "Documents not supplied: refused consideration", focus: "c2", steps: [
        { actor: "lg1", action: "requireDocs", target: "c2", params: { days: "21" } },
        { tick: 22 },
        { actor: "lg1", action: "refuseToConsider", target: "c2" }
      ] },
      { label: "At a cat show without a tag", focus: "c1", steps: [
        { actor: "c1", action: "loseTag" },
        { actor: "p1", action: "exhibit", target: "c1", params: { host: "listed" } }
      ] },
      { label: "… at a show nobody lists", focus: "c1", steps: [
        { actor: "c1", action: "loseTag" },
        { actor: "p1", action: "exhibit", target: "c1", params: { host: "unlisted" } }
      ] },
      { label: "Registered in September, lapses in November", focus: "c2", steps: [
        { actor: "p2", action: "sterilise", target: "c2" },
        { actor: "p2", action: "microchip", target: "c2" },
        { tick: 257 },
        { actor: "lg1", action: "register", target: "c2", params: { period: "one" } },
        { tick: 50 }
      ] },
      { label: "Renewing Mittens on 11 October", focus: "c1", steps: [
        { tick: 283 },
        { actor: "lg1", action: "renew", target: "c1" }
      ] },
      { label: "Thirteen weeks in SAFE foster care", focus: "c2", steps: [
        { actor: "p4", action: "placeFoster", target: "c2", params: { placer: "SAFE" } },
        { tick: 92 }
      ] },
      { label: "A kitten grows up, and nothing is done", focus: "@kit", mode: "nature", steps: [
        { spawn: "cat", as: "kit", label: "Tigger", note: "born today",
          attrs: { bornDate: "2026-01-01", ownedForBreeding: false, custody: "none", microchipped: false, sterilised: false,
                   sterilisedByVet: false, wearingTag: false }, rels: { owner: "p4" } },
        { tick: 240 },
        { actor: "p4", action: "sitOnIt", target: "@kit" }
      ] }
    ],

    /* ---------------------------------------------------------- simulation
       Illustrative defaults throughout: there is no data behind them. */
    simulation: {
      params: [
        { key: "residents", label: "People in the district at the start", def: 12, min: 1, max: 60, step: 1 },
        { key: "startCats", label: "Cats already in the district at the start", def: 20, min: 0, max: 200, step: 1,
          note: "Adult cats of any age. Nothing about their registration, chip or sterilisation is assumed." },
        { key: "maxCats", label: "Most cats alive at once", def: 60, min: 1, max: 400, step: 1 },
        { key: "kittensPerMonth", label: "Kittens born per month", def: 3, min: 0, max: 60, step: 0.5 },
        { key: "pCompliant", label: "Owners who keep up with registration, chipping and sterilisation", unit: "%", def: 75, min: 0, max: 100, step: 1 },
        { key: "pNonVet", label: "Sterilisations not done by a veterinarian", unit: "%", def: 3, min: 0, max: 100, step: 1 },
        { key: "pSterFirst", label: "Careful owners who sterilise before microchipping", unit: "%", def: 40, min: 0, max: 100, step: 1 },
        { key: "pEarlyCert", label: "Kittens a vet certifies unfit for a procedure before six months", unit: "%", def: 3, min: 0, max: 100, step: 1 },
        { key: "pDocs", label: "Applications where the council asks for documents", unit: "%", def: 15, min: 0, max: 100, step: 1 },
        { key: "pNoDocs", label: "Applicants who never supply the documents", unit: "%", def: 25, min: 0, max: 100, step: 1 },
        { key: "tagLossPerYear", label: "Tags lost per cat per year", def: 0.3, min: 0, max: 5, step: 0.05 },
        { key: "outingsPerYear", label: "Times per cat per year it is seen in a public place", def: 6, min: 0, max: 60, step: 1 },
        { key: "showsPerYear", label: "Cat shows per cat per year", def: 0.1, min: 0, max: 5, step: 0.05 },
        { key: "pSafeFoster", label: "Cats placed in SAFE foster care per year", unit: "%", def: 3, min: 0, max: 100, step: 1 },
        { key: "slowDays", label: "Days after six months before a careless owner is treated as too slow", def: 60, min: 1, max: 365, step: 1,
          note: "“All convenient speed” is a judgment the Act leaves to a court. This is the simulation’s stand-in for it, not a rule of law." }
      ],
      generators: [
        { id: "council", start: ["if", ["=", ["count", "localgov"], 0], 1, 0], spawn: { type: "localgov", label: "City of Perth" } },
        { id: "vet", start: ["if", ["=", ["count", "person", "$it.attrs.isVeterinarian"], 0], 1, 0],
          spawn: { type: "person", label: "Dr {name}", names: ["Singh", "Walsh", "Nguyen"], note: "veterinarian",
                   attrs: { bornDay: ["-", "$day", ["*", 365, ["randInt", 30, 60]]], isVeterinarian: true, isImplanter: true,
                            isApprovedBreeder: false, offences: 0 } } },
        { id: "residents", start: "$param.residents",
          spawn: { type: "person", label: "{name}", note: "resident",
                   names: ["Ada", "Ben", "Cleo", "Dev", "Eve", "Finn", "Gia", "Hal", "Isla", "Jai", "Kit", "Lou",
                           "Mae", "Ned", "Ola", "Pat", "Ray", "Sal", "Tia", "Uri", "Val", "Wes", "Yan", "Zoe"],
                   attrs: { bornDay: ["-", "$day", ["*", 365, ["randInt", 19, 80]]], isVeterinarian: false, isImplanter: false,
                            isApprovedBreeder: false, offences: 0, resident: true } } },
        { id: "adult-cats", start: "$param.startCats",
          spawn: { type: "cat", label: "{name}",
                   names: ["Mittens", "Smudge", "Tiger", "Luna", "Oscar", "Bella", "Milo", "Cleo", "Simba", "Nala",
                           "Felix", "Willow", "Leo", "Coco", "Jasper", "Pepper", "Ziggy", "Maple", "Sooty", "Ginger"],
                   attrs: { bornDay: ["-", "$day", ["randInt", 200, 4000]], ownedForBreeding: false, custody: "none",
                            microchipped: false, sterilised: false, sterilisedByVet: false, wearingTag: false,
                            compliant: ["chance", ["/", "$param.pCompliant", 100]],
                            sterFirst: ["chance", ["/", "$param.pSterFirst", 100]] },
                   rels: { owner: ["any", "person", "$it.attrs.resident"] } } },
        { id: "kittens", rate: ["/", "$param.kittensPerMonth", 30],
          when: ["<", ["count", "cat"], "$param.maxCats"],
          spawn: { type: "cat", label: "{name}",
                   names: ["Pip", "Tigger", "Mochi", "Biscuit", "Sushi", "Pumpkin", "Pebbles", "Olive", "Mango", "Button",
                           "Dot", "Fudge", "Kiwi", "Noodle", "Peanut", "Rolo", "Taco", "Waffle", "Yoyo", "Zest"],
                   attrs: { bornDay: "$day", ownedForBreeding: false, custody: "none",
                            microchipped: false, sterilised: false, sterilisedByVet: false, wearingTag: false,
                            compliant: ["chance", ["/", "$param.pCompliant", 100]],
                            sterFirst: ["chance", ["/", "$param.pSterFirst", 100]],
                            earlyCert: ["chance", ["/", "$param.pEarlyCert", 100]] },
                   rels: { owner: ["any", "person", "$it.attrs.resident"] } } },

        /* a vet's early certificate, for the few kittens that need one */
        { id: "early-cert", per: "cat",
          when: ["and", "$self.attrs.earlyCert", ["not", ["exists", "$self.attrs.certChipAge"]],
                        [">=", ["daysSince", "$self.attrs.bornDay"], 120], ["<", ["daysSince", "$self.attrs.bornDay"], 170]],
          chance: 0.05,
          act: { action: "certify", actor: ["any", "person", "$it.attrs.isVeterinarian"], target: "$self", params: { about: "chip" } } },

        /* careful owners get there, in one order or the other */
        { id: "sterilise", per: "cat",
          when: ["and", "$self.attrs.compliant", ["not", "$self.attrs.sterilised"], [">=", ["daysSince", "$self.attrs.bornDay"], 110],
                        ["or", "$self.attrs.sterFirst", "$self.attrs.microchipped"]],
          chance: 0.06,
          act: { action: "sterilise",
                 actor: ["if", ["chance", ["/", "$param.pNonVet", 100]],
                               ["any", "person", ["and", "$it.attrs.resident", ["!=", "$it.id", "$self.rels.owner"]]],
                               ["any", "person", "$it.attrs.isVeterinarian"]],
                 target: "$self" } },
        { id: "microchip", per: "cat",
          when: ["and", "$self.attrs.compliant", ["not", "$self.attrs.microchipped"], [">=", ["daysSince", "$self.attrs.bornDay"], 90],
                        ["not", "$self.attrs.earlyCert"], ["or", ["not", "$self.attrs.sterFirst"], "$self.attrs.sterilised"]],
          chance: 0.06,
          act: { action: "microchip", actor: ["any", "person", "$it.attrs.isVeterinarian"], target: "$self" } },

        /* applications: some are asked for documents, a few never supply them */
        { id: "ask-docs", per: "cat",
          when: ["and", "$self.attrs.compliant", ["not", ["exists", "$self.rels.registeredWith"]], "$self.attrs.microchipped",
                        "$self.attrs.sterilised", ["not", ["exists", "$self.attrs.docsDay"]], ["not", "$self.attrs.docsDone"]],
          chance: ["/", "$param.pDocs", 1000],
          act: { action: "requireDocs", actor: ["any", "localgov"], target: "$self", params: { days: "21" } } },
        { id: "supply-docs", per: "cat",
          when: ["and", ["exists", "$self.attrs.docsDay"], ["not", "$self.attrs.docsSupplied"],
                        ["=", ["daysSince", "$self.attrs.docsDay"], 7]],
          chance: ["-", 1, ["/", "$param.pNoDocs", 100]],
          act: { action: "supplyDocs", actor: ["rel", "$self", "owner"], target: "$self" } },
        { id: "refuse-consider", per: "cat",
          when: ["and", ["exists", "$self.attrs.docsDay"], ["not", "$self.attrs.docsSupplied"],
                        ["=", ["daysSince", "$self.attrs.docsDay"], 25]],
          chance: 1,
          act: { action: "refuseToConsider", actor: ["any", "localgov"], target: "$self" } },
        { id: "register", per: "cat",
          when: ["and", "$self.attrs.compliant", ["not", ["exists", "$self.rels.registeredWith"]],
                        [">=", ["daysSince", "$self.attrs.bornDay"], 150],
                        ["or", "$self.attrs.microchipped", ["def", "selfChipExempt"]], "$self.attrs.sterilised",
                        ["or", ["not", ["exists", "$self.attrs.docsDay"]], "$self.attrs.docsSupplied"]],
          chance: 0.05,
          act: { action: "register", actor: ["any", "localgov"], target: "$self",
                 params: { period: ["oneOf", "one", "one", "three", "life"] } } },
        { id: "renew", per: "cat",
          when: ["and", ["exists", "$self.rels.registeredWith"], "$self.attrs.compliant",
                        ["<=", ["def", "daysToOct31"], 20], [">=", ["def", "daysToOct31"], 0],
                        ["<", "$self.attrs.regExpiryDay", ["+", "$day", 25]]],
          chance: 0.15,
          act: { action: "renew", actor: ["any", "localgov"], target: "$self" } },

        /* out in the world */
        { id: "go-out", per: "cat",
          when: ["and", ["not", "$self.attrs.inPublic"], [">", ["daysSince", "$self.attrs.bornDay"], 120]],
          chance: ["/", "$param.outingsPerYear", 365],
          act: { action: "goOut", actor: "$self" } },
        { id: "come-home", per: "cat", when: "$self.attrs.inPublic", chance: 0.8,
          act: { action: "comeHome", actor: "$self" } },
        { id: "lose-tag", per: "cat", when: "$self.attrs.wearingTag",
          chance: ["/", "$param.tagLossPerYear", 365],
          act: { action: "loseTag", actor: "$self" } },
        { id: "show", per: "cat",
          when: ["and", ["exists", "$self.rels.registeredWith"], ["not", "$self.attrs.inPublic"]],
          chance: ["/", "$param.showsPerYear", 365],
          act: { action: "exhibit", actor: ["rel", "$self", "owner"], target: "$self",
                 params: { host: ["oneOf", "listed", "listed", "listed", "unlisted"] } } },
        { id: "too-slow", per: "cat",
          when: ["and", ["not", "$self.attrs.compliant"], ["not", "$self.attrs.slowJudged"],
                        [">=", ["daysSince", "$self.attrs.bornDay"], ["+", 182, "$param.slowDays"]]],
          chance: 1,
          act: { action: "sitOnIt", actor: ["rel", "$self", "owner"], target: "$self" } },
        { id: "foster", per: "cat",
          when: ["and", ["not", ["exists", "$self.attrs.fosterDay"]], ["not", ["exists", "$self.rels.registeredWith"]]],
          chance: ["/", "$param.pSafeFoster", 36500],
          act: { action: "placeFoster", actor: ["any", "person", "$it.attrs.resident"], target: "$self", params: { placer: "SAFE" } } }
      ]
    }
  };

  global.SCHEMES = [DOG_ACT, CAT_ACT, RBO_BILL, RTA_RENT_CAP];
})(window);
