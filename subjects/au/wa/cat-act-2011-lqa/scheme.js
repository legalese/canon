/* The console scheme for the LQA run of the Cat Act 2011 (WA), Parts 1 and 2.
   Drafted at step 4A (2026-10-01) from this subject's L4 (part-1-preliminary.l4,
   part-2-div-*.l4, cat-regulations-2012.l4, and the Interpretation Act module), following its
   readings and the forks taken in registers/fork-register.json. Separate from any other Cat Act
   scheme.

   Steps 8A-11A (2026-10-02) added the findings: one observation per finding in incidents.json,
   with its ID as `ref` and its discovery method as `foundBy`; the rules that record each one; and
   the scenarios that show them. Findings verified sound are recorded with sev "ok". Form findings
   are `static` (no run can show a typographical slip). Every finding the console shows is the
   L4's reading (the forks taken at 5A, confirmed at 6H); where a finding turns on a fork, the log
   says what the other reading would do.

   Where the console is coarser than the L4, ENCODING-NOTES.md says so (the console's clocks do
   not move a deadline off an excluded day, which the L4 does under IA s 61(1)(e)). */
(function (global) {
  /* a registration's end under r 12(2)(a)(i), FORK-05 reading A: the first 31 October AFTER
     the day it takes effect (one taking effect on 31 October runs a year) */
  var NEXT_31_OCT = ["if", ["=", ["nextDate", 10, 31], "$day"], ["nextDate", 10, 31, 1], ["nextDate", 10, 31]];
  /* r 12(2)(a)(ii), FORK-06 reading A: the 31 October in the last 12 months of the 3-year period
     beginning today -- the next 31 October on or after today, two years on */
  var THREE_YEAR_END = ["nextDate", 10, 31, 2];

  var CAT_ACT_LQA = {
    id: "cat-act-lqa",
    title: "Cat Act 2011 (LQA run)",
    jurisdiction: "Western Australia",
    status: "Compilation 00-l0-01 (currency start 25 Sep 2025), with the Cat Regulations 2012 compilation 02-b0-00 · encoding certified at 6H on 1 Oct 2026 · findings at 8A-11A, 2 Oct 2026 · not released (12H)",
    scope: "Part 1 and Part 2 (ss. 2-25), with the Cat Regulations 2012 rr. 4-19 and Sch. 3, and Interpretation Act 1984 ss. 61, 62, 71, 72. Registration, tags, microchipping, sterilisation, transfer and notices. Modelled more coarsely than the L4: s. 25 changes of details, s. 10 cancellation, fees, r. 9 custody and foster care, cat management facilities and reclaiming, and the excluded-day rule (all exact in the L4).",
    startDate: "2026-01-01",
    dayLabel: "Day",

    types: [
      { id: "localgov", label: "Local government", band: 0, shape: "rect",
        create: { nameHint: "Shire of Kalamunda", fields: [], rels: [] } },
      { id: "company", label: "Microchip database company", band: 1, shape: "rect",
        create: { nameHint: "Central Animal Records", fields: [
          { key: "prescribed", type: "bool", origin: "innate", cite: "s. 3(1); r. 6",
            label: "Is prescribed as a microchip database company (r. 6)",
            note: "Only the four companies r. 6 names are microchip database companies." }
        ], rels: [] } },
      { id: "person", label: "Person", band: 1, shape: "rect",
        create: { nameHint: "Ana", fields: [
          { key: "bornDay", type: "age", origin: "birth", unit: "years", label: "Age in years", def: 35,
            cite: "ss. 4(1)(c), 9(2)(a)", note: "A child is under 18, reckoned in calendar months from the day of birth (FORK-01 reading A)." },
          { key: "vet", type: "bool", origin: "exogenous", cite: "s. 3(1) 'veterinarian'",
            label: "Is a veterinarian", note: "Registration under the Veterinary Practice Act 2021 is settled by that Act (REF-14). An interstate practitioner who does not practise in WA is not one (VPA s. 22(1)(c))." },
          { key: "interstateVet", type: "bool", origin: "exogenous", cite: "VPA 2021 ss. 3, 22",
            label: "Is a veterinarian registered only in another State, not practising in WA",
            note: "Such a person is not a 'veterinarian' for the Cat Act (D-05, D-22)." },
          { key: "microchipImplanter", type: "bool", origin: "exogenous", cite: "s. 3(1); r. 7",
            label: "Is a microchip implanter (a veterinarian, a veterinary nurse, or holds the r. 7(2) qualifications)",
            note: "Registration as a veterinary nurse and completion of the units and courses are facts settled elsewhere (REF-11, REF-12)." },
          { key: "approvedBreeder", type: "bool", origin: "exogenous", cite: "ss. 3(1), 37",
            label: "Is an approved cat breeder", note: "Approval is granted under Part 3 (s. 37), outside this run's scope (REF-01)." },
          { key: "convictions2in3", type: "bool", origin: "exogenous", cite: "s. 9(2)(e)",
            label: "Has 2 or more convictions against the Cat, Dog or Animal Welfare Acts in the last 3 years",
            note: "Counted together across the three Acts (FORK-10 reading A). Convictions are a court's business (REF-25)." },
          { key: "nonResident", type: "bool", origin: "exogenous", cite: "s. 5(2)(b)",
            label: "Is not resident in the State", note: "FORK-09: a person never resident is not within s. 5(2)(b) (reading A)." },
          { key: "pensioner", type: "bool", origin: "exogenous", cite: "Sch. 3 cl. 1(1), (3)",
            label: "Is an eligible pensioner", note: "Rates and Charges (Rebates and Deferments) Act 1992 s. 3(1) (REF-24)." }
        ], rels: [] } },
      { id: "cat", label: "Cat", band: 2, shape: "round",
        create: { nameHint: "Tom", bornVerb: "Born", fields: [
          { key: "bornDay", type: "age", origin: "birth", unit: "months", label: "Age in months", def: 8,
            cite: "ss. 5(1), 14(1), 18(1)", note: "The duties attach on the day the cat reaches 6 months (FORK-01 reading A)." },
          { key: "breeding", type: "bool", origin: "innate", cite: "s. 18(2)(b)",
            label: "Is owned for the purpose of breeding" },
          { key: "chipped", type: "bool", origin: "conferred", by: "implant", cite: "s. 3(1); r. 8",
            label: "Is microchipped (implanted with a microchip by a microchip implanter)" },
          { key: "sterilised", type: "bool", origin: "conferred", by: "sterilise", cite: "s. 3(1)",
            label: "Is sterilised (made permanently infertile by a surgical procedure)" },
          { key: "chipCert", type: "bool", origin: "conferred", by: "certifyChip", cite: "s. 14(2)",
            label: "Holds a veterinarian's certificate that microchipping may harm it" },
          { key: "sterCert", type: "bool", origin: "conferred", by: "certifySter", cite: "s. 18(2)(a)",
            label: "Holds a veterinarian's certificate that sterilising may harm it" },
          { key: "registered", type: "bool", origin: "conferred", by: "decide", cite: "ss. 3(1), 9",
            label: "Is registered" },
          { key: "wearingTag", type: "bool", origin: "conferred", by: "decide", cite: "s. 11(1)(c)",
            label: "Is wearing its registration tag" },
          { key: "earTattoo", type: "bool", origin: "conferred", by: "tattoo", cite: "r. 18",
            label: "Bears the sterilisation tattoo on its ear" }
        ], rels: [
          { key: "keptIn", label: "Ordinarily kept in the district of", target: "localgov", required: true, origin: "exogenous",
            cite: "s. 5(1)", note: "Which district a cat is kept in is geography (REF-17)." },
          { key: "keeper", label: "Kept and cared for by", target: "person", origin: "innate", cite: "s. 4(1)(b)" },
          { key: "registeredWith", label: "Registered with", target: "localgov", origin: "conferred", by: "decide", cite: "s. 9" },
          { key: "registeredOwner", label: "Registered in the name of", target: "person", origin: "conferred", by: "decide", cite: "s. 3(1) 'registered owner'" },
          { key: "company", label: "Microchip database company for the cat", target: "company", origin: "conferred", by: "implant", cite: "s. 3(1)" },
          { key: "implanter", label: "Microchipped by", target: "person", origin: "conferred", by: "implant", cite: "s. 15" }
        ] } }
    ],

    relLabels: { keptIn: "kept in", keeper: "kept by", registeredWith: "registered with", registeredOwner: "registered to",
                 company: "records with", implanter: "chipped by", sterilisedBy: "desexed by" },

    entities: [
      { id: "lg1", type: "localgov", label: "City of Perth" },
      { id: "lg2", type: "localgov", label: "Shire of Kalamunda" },
      { id: "co1", type: "company", label: "Petsafe", note: "prescribed by r. 6(c)", attrs: { prescribed: true } },
      { id: "p1", type: "person", label: "Ana", attrs: { bornDate: "1980-05-05", vet: false, microchipImplanter: false, approvedBreeder: false, convictions2in3: false } },
      { id: "p2", type: "person", label: "Ben", attrs: { bornDate: "1975-02-02", vet: false, microchipImplanter: false, approvedBreeder: false, convictions2in3: false } },
      { id: "p3", type: "person", label: "Kit", note: "Ana's daughter, a child", attrs: { bornDate: "2012-03-10", vet: false, microchipImplanter: false, approvedBreeder: false, convictions2in3: false, parent: "p1" } },
      { id: "v1", type: "person", label: "Dr Vu", note: "veterinarian", attrs: { bornDate: "1970-01-01", vet: true, microchipImplanter: true, approvedBreeder: false, convictions2in3: false } },
      { id: "p4", type: "person", label: "Dr Hart", note: "Melbourne veterinarian; does not practise in WA",
        attrs: { bornDate: "1972-04-04", vet: false, interstateVet: true, microchipImplanter: false, approvedBreeder: false, convictions2in3: false } },
      { id: "p5", type: "person", label: "Bree", note: "approved cat breeder", attrs: { bornDate: "1985-01-01", vet: false, microchipImplanter: false, approvedBreeder: true, convictions2in3: false } },
      { id: "p6", type: "person", label: "Vic", note: "lives in Darwin", attrs: { bornDate: "1985-01-01", vet: false, microchipImplanter: false, approvedBreeder: false, convictions2in3: false, nonResident: true } },
      { id: "p7", type: "person", label: "Pat", note: "pensioner", attrs: { bornDate: "1950-01-01", vet: false, microchipImplanter: false, approvedBreeder: false, convictions2in3: false, pensioner: true } },
      { id: "c1", type: "cat", label: "Tom", note: "a kitten, kept by Ana, unchipped and entire",
        attrs: { bornDate: "2025-11-01", keptSinceDay: -61, breeding: false, chipped: false, sterilised: false,
                 chipCert: false, sterCert: false, registered: false, wearingTag: false, earTattoo: false },
        rels: { keptIn: "lg1", keeper: "p1" } },
      { id: "c2", type: "cat", label: "Tess", note: "adult, chipped, desexed, registered to Ana until 31 October 2026",
        attrs: { bornDate: "2020-06-01", keptSinceDay: -400, breeding: false, chipped: true, sterilised: true, sterilisedByVet: true,
                 chipCert: false, sterCert: false, registered: true, everRegistered: true, regExpiryDay: 303, regExpiryDate: "31 Oct 2026",
                 wearingTag: true, earTattoo: false, s15Notified: true, s21Given: true },
        rels: { keptIn: "lg1", keeper: "p1", registeredWith: "lg1", registeredOwner: "p1", company: "co1", implanter: "v1" } }
    ],

    defs: {
      sixMonths: [">=", ["ageMonths", "$self.attrs.bornDay"], 6],
      /* ss. 14(2)-(3), 18(2)-(3): a certificate applies only once the cat is 6 months (FORK-13 reading A) */
      chipExempt: ["and", "$self.attrs.chipCert", ["def", "sixMonths"]],
      sterExempt: ["or", ["and", "$self.attrs.sterCert", ["def", "sixMonths"]],
                         ["and", "$self.attrs.breeding", ["attrOf", ["rel", "$self", "keeper"], "approvedBreeder"]]],
      /* s. 4(1): a registered cat's owner is its registered owner; otherwise its keeper */
      ownerId: ["if", "$self.attrs.registered", "$self.rels.registeredOwner", "$self.rels.keeper"],
      tChipExempt: ["and", "$target.attrs.chipCert", [">=", ["ageMonths", "$target.attrs.bornDay"], 6]],
      tSterExempt: ["or", ["and", "$target.attrs.sterCert", [">=", ["ageMonths", "$target.attrs.bornDay"], 6]],
                          ["and", "$target.attrs.breeding", ["attrOf", ["rel", "$target", "keeper"], "approvedBreeder"]]],
      tOwnerIsActor: ["if", "$target.attrs.registered", ["=", "$target.rels.registeredOwner", "$self.id"], ["=", "$target.rels.keeper", "$self.id"]],
      tUnderSix: ["<", ["ageMonths", "$target.attrs.bornDay"], 6],
      /* the purchaser of a registered cat: keeps it, but it is registered in someone else's name */
      tKeeperNotRegisteredOwner: ["and", "$target.attrs.registered", ["=", "$target.rels.keeper", "$self.id"],
                                  ["not", ["=", "$target.rels.registeredOwner", "$self.id"]]],
      /* the s. 5(1) test the s5 rule applies, for rules that annotate it */
      s5Due: ["and", ["def", "sixMonths"], ["exists", "$self.rels.keeper"], ["not", "$self.attrs.s5Flag"],
              [">=", ["daysSince", "$self.attrs.keptSinceDay"], 14],
              ["not", ["and", "$self.attrs.registered", ["=", "$self.rels.registeredWith", "$self.rels.keptIn"]]],
              ["not", "$self.attrs.atVet"]],
      daysTo31Oct: ["-", ["nextDate", 10, 31], "$day"]
    },

    actions: [
      { id: "apply", actor: "person", target: "cat", label: "Apply to the local government to register the cat", cite: "s. 8; r. 11",
        log: "<b>{self}</b> applies to register <b>{target}</b>.",
        params: [ { key: "threeYears", label: "for 3 years (r. 12(1)(a))" },
                  { key: "noFee", label: "without paying the fee (s. 8(2)(b))" } ] },
      { id: "decide", actor: "localgov", target: "cat", label: "Decide the application to register the cat", cite: "s. 9",
        log: "<b>{self}</b> decides the application to register <b>{target}</b>." },
      { id: "requireInfo", actor: "localgov", target: "cat", label: "Require the applicant to give information within a set time", cite: "s. 9(5)",
        log: "<b>{self}</b> requires the applicant for <b>{target}</b> to give it further information.",
        params: [ { key: "over21", label: "allowing more than 21 days" } ] },
      { id: "refuseToConsider", actor: "localgov", target: "cat", label: "Refuse to consider the application", cite: "s. 9(6)",
        log: "<b>{self}</b> refuses to consider the application to register <b>{target}</b>." },
      { id: "letNoticeLapse", actor: "localgov", target: "cat", label: "Let 7 days pass without giving notice of a refusal", cite: "s. 13",
        log: "<b>{self}</b> gives no notice of its refusal to register <b>{target}</b>." },
      { id: "implant", actor: "person", target: "cat", label: "Implant a microchip", cite: "s. 3(1) 'microchipped'; r. 8",
        log: "<b>{self}</b> implants a microchip in <b>{target}</b>.",
        params: [ { key: "noDatabase", label: "without arranging for any microchip database company to keep the records" } ] },
      { id: "notifyImplant", actor: "person", target: "cat", label: "Notify the microchip database company of the implant", cite: "s. 15; r. 17",
        log: "<b>{self}</b> gives the microchip database company written notice of the information about <b>{target}</b>." },
      { id: "changePracticeDetails", actor: "person", target: "cat", label: "Change the implanter's business contact details", cite: "s. 25(b); r. 17(e)",
        log: "<b>{self}</b>'s practice changes its telephone number and address." },
      { id: "certifyChip", actor: "person", target: "cat", label: "Certify that microchipping may harm the cat", cite: "s. 14(2)",
        log: "<b>{self}</b> certifies that implanting a microchip in <b>{target}</b> may adversely affect its health and welfare." },
      { id: "sterilise", actor: "person", target: "cat", label: "Sterilise the cat", cite: "s. 3(1) 'sterilised'",
        log: "<b>{self}</b> sterilises <b>{target}</b>." },
      { id: "notifySterilisation", actor: "person", target: "cat", label: "Notify the microchip database company of the sterilisation", cite: "s. 20",
        log: "<b>{self}</b> notifies the microchip database company that <b>{target}</b> has been sterilised." },
      { id: "giveCertificate", actor: "person", target: "cat", label: "Give the owner a certificate of sterilisation", cite: "s. 21",
        log: "<b>{self}</b> gives a certificate of sterilisation for <b>{target}</b>." },
      { id: "giveFalseCertificate", actor: "person", target: "cat", label: "Hand over a false certificate of sterilisation", cite: "s. 19; r. 18",
        log: "<b>{self}</b> hands over a document certifying that <b>{target}</b> has been sterilised." },
      { id: "certifySter", actor: "person", target: "cat", label: "Certify that sterilising may harm the cat", cite: "s. 18(2)(a)",
        log: "<b>{self}</b> certifies that sterilising <b>{target}</b> may adversely affect its health and welfare." },
      { id: "tattoo", actor: "person", target: "cat", label: "Tattoo the sterilisation mark on the cat's ear", cite: "s. 19; r. 18",
        log: "<b>{self}</b> tattoos a broken circle with a bisecting broken line on <b>{target}</b>'s ear." },
      { id: "acquire", actor: "person", target: "cat", label: "Take the cat over from its keeper (a sale or gift)", cite: "ss. 3(1) 'transfer', 22, 23",
        log: "<b>{self}</b> takes <b>{target}</b> over from its keeper.",
        params: [ { key: "voucher", label: "with a voucher for later sterilisation at no cost (s. 23(2)(b))" } ] },
      { id: "offerForSale", actor: "person", target: "cat", label: "Advertise the cat for sale", cite: "s. 3(1) 'transfer' (a); s. 24",
        log: "<b>{self}</b> advertises <b>{target}</b> for sale." },
      { id: "notifyTransfer", actor: "person", target: "cat", label: "Notify the transfer to the local government and database company", cite: "s. 24",
        log: "<b>{self}</b> gives written notice of the transfer of <b>{target}</b> and the purchaser's name and address." },
      { id: "surrenderToVet", actor: "person", target: "cat", label: "Give the cat up to a veterinary clinic", cite: "s. 23(3); rr. 9(2)(e), 19",
        log: "<b>{self}</b> gives <b>{target}</b> up to a registered veterinary clinic." },
      { id: "giveToSafe", actor: "person", target: "cat", label: "Give the cat to a SAFE rescue group", cite: "s. 23(3); rr. 9, 19",
        log: "<b>{self}</b> gives <b>{target}</b> to Saving Animals from Euthanasia Incorporated." },
      { id: "impound", actor: "localgov", target: "cat", label: "Impound the cat in the council pound", cite: "ss. 27, 28 (Part 3)",
        log: "<b>{self}</b> impounds <b>{target}</b> in its pound, a cat management facility." },
      { id: "reclaim", actor: "person", target: "cat", label: "Reclaim the cat from the pound", cite: "s. 3(1) 'transfer' (b); ss. 22-24",
        log: "<b>{self}</b> reclaims <b>{target}</b> from the pound." },
      { id: "leaveAtVet", actor: "person", target: "cat", label: "Leave the cat at a veterinary clinic for treatment", cite: "r. 9(2)(e)",
        log: "<b>{self}</b> leaves <b>{target}</b> at a registered veterinary clinic for a few days' treatment." },
      { id: "collectFromVet", actor: "person", target: "cat", label: "Collect the cat from the veterinary clinic", cite: "r. 9(2)(e)",
        log: "<b>{self}</b> collects <b>{target}</b> from the clinic." },
      { id: "placeInFoster", actor: "person", target: "cat", label: "Place the cat in foster care for a SAFE group", cite: "r. 9(3)(b)",
        log: "<b>{self}</b> takes <b>{target}</b> into foster care, placed by a SAFE entity." },
      { id: "moveDistrict", actor: "person", target: "cat", label: "Move house, with the cat, to the Shire of Kalamunda", cite: "s. 5(1); r. 13",
        log: "<b>{self}</b> moves house with <b>{target}</b> to the Shire of Kalamunda." },
      { id: "notifyMove", actor: "person", target: "cat", label: "Notify both local governments to continue the registration (r. 13)", cite: "r. 13",
        log: "<b>{self}</b> notifies the City of Perth and the Shire of Kalamunda to continue <b>{target}</b>'s registration with the Shire." },
      { id: "fakeTag", actor: "person", target: "cat", label: "Put a home-made registration tag on the cat", cite: "s. 7",
        log: "<b>{self}</b> fastens a home-made tag, made to look like a council registration tag, to <b>{target}</b>'s collar." },
      { id: "goOut", actor: "cat", label: "Go into a public place", cite: "s. 6(1)",
        log: "<b>{self}</b> is in a public place.",
        params: [ { key: "exhibited", label: "being exhibited at a show of a listed cat body (r. 10)" } ] },
      { id: "loseTag", actor: "cat", label: "Lose its registration tag", cite: "s. 11(2)",
        log: "<b>{self}</b> loses its registration tag." },
      { id: "replaceTag", actor: "localgov", target: "cat", label: "Give the owner a new registration tag", cite: "s. 11(2)",
        log: "<b>{self}</b> issues a new registration tag for <b>{target}</b>." }
    ],

    rules: [
      /* ---- s. 8: who may apply ---- */
      { id: "apply-purchaser", on: "action:apply", "if": ["def", "tKeeperNotRegisteredOwner"],
        then: [
          ["set", "$target.attrs.purchaserTried", true],
          ["log", "<b>{self} keeps and cares for {target}, but cannot register it.</b> {target} is registered in another person's name, so its owner is that registered owner (s. 4(1)(a)) and {self} is not an owner at all; only an owner may apply (s. 8(1)). Nothing in Part 2 moves a registration to a new keeper.",
            { cite: "ss. 4(1)(a), 8(1)", sev: "stop" }],
          ["observe", "d01"]
        ] },
      { id: "apply-not-owner", on: "action:apply", "if": ["not", ["def", "tOwnerIsActor"]],
        then: [
          ["log", "<b>Nothing has happened.</b> Section 8(1) lets the owner of a cat apply. {self} is not {target}'s owner (s. 4: the registered owner of a registered cat, otherwise the person who keeps and cares for it).",
            { cite: "ss. 4, 8(1)", sev: "ok" }],
          ["observe", "void-act"]
        ] },
      { id: "apply-child", on: "action:apply", "if": ["and", ["def", "tOwnerIsActor"], ["<", ["ageYears", "$self.attrs.bornDay"], 18]],
        then: [
          ["log", "{self} is a child. On FORK-02's reading A (taken) {self} is an owner under s. 4(1)(b) and {self}'s parent is an owner too under s. 4(1)(c): 'any of these persons'. Reading B would make the parent the only owner.",
            { cite: "s. 4(1)(b), (c)", sev: "ok" }],
          ["observe", "u04"]
        ] },
      { id: "apply-pensioner", on: "action:apply", "if": ["and", ["def", "tOwnerIsActor"], "$self.attrs.pensioner"],
        then: [
          ["log", "{self} is a pensioner, so the fee is halved: Sch. 3 cl. 1(3) applies 'if the owner of a cat is a pensioner'. The clause tests 'the owner'; where a cat has several owners (a child and parent, a business's owners, or a registered owner who no longer keeps it) and only some are pensioners, it does not say whose status counts.",
            { cite: "Sch. 3 cl. 1(3)", sev: "warn" }],
          ["observe", "d41"]
        ] },
      { id: "apply-nofee", on: "action:apply", "if": ["and", ["def", "tOwnerIsActor"], "$p.noFee"],
        then: [
          ["log", "No fee is paid, so the application is not made as s. 8(2)(b) requires. Section 9(2) says the local government must refuse 'if, and only if' one of five grounds applies, and a missing fee is not one; but s. 9 operates only on 'an application ... under section 8', and one without the fee is not such an application. Verified sound.",
            { cite: "ss. 8(2), 9(1), (2)", sev: "ok" }],
          ["observe", "l16"]
        ] },
      { id: "apply-renewal-window", on: "action:apply",
        "if": ["and", ["def", "tOwnerIsActor"], "$target.attrs.registered", [">", ["def", "daysTo31Oct"], 20]],
        then: [
          ["log", "<b>A renewal outside the 21 days.</b> Regulation 12(2)(b) lets a registration be renewed 'to take effect as from 1 November ... within the preceding period of 21 days' (11-31 October). It does not say whether a renewal may be made at any other time, or from when one made now would take effect.",
            { cite: "r. 12(2)(b); IA s. 61(1)(c)", sev: "warn" }],
          ["observe", "t39"]
        ] },
      { id: "apply-after-lapse", on: "action:apply",
        "if": ["and", ["def", "tOwnerIsActor"], ["not", "$target.attrs.registered"], "$target.attrs.everRegistered"],
        then: [
          ["log", "<b>Grant or renewal?</b> {target}'s registration has expired. Neither s. 8 nor r. 12 says whether this application is for a renewal or a fresh grant, and the fee differs: a one-year grant between June and October costs $10, a renewal $20 (Sch. 3 item 1).",
            { cite: "s. 8(1); r. 12(2)(b); Sch. 3 item 1", sev: "warn" }],
          ["observe", "t39"]
        ] },
      { id: "apply", on: "action:apply", "if": ["def", "tOwnerIsActor"],
        then: [
          ["set", "$target.attrs.applied", true],
          ["set", "$target.attrs.applicantId", "$self.id"],
          ["set", "$target.attrs.applicantChild", ["<", ["ageYears", "$self.attrs.bornDay"], 18]],
          ["set", "$target.attrs.applicantConvictions", "$self.attrs.convictions2in3"],
          ["set", "$target.attrs.applied3y", ["if", "$p.threeYears", true, false]],
          ["log", "The application is made by {target}'s owner (s. 8(1)). The local government must now grant it or refuse it (s. 9(1)). (The explanatory memorandum says s. 8 'requires' the owner to apply; s. 8 permits, and the duty is s. 5(1)'s.)", { cite: "ss. 5(1), 8", sev: "ok" }],
          ["observe", "x50"]
        ] },

      /* ---- s. 9: the decision ---- */
      { id: "decide-nothing", on: "action:decide", "if": ["not", "$target.attrs.applied"],
        then: [
          ["log", "<b>Nothing has happened.</b> There is no application under s. 8 for {target} before the local government, and s. 9 only operates on one.", { cite: "s. 9(1)", sev: "ok" }],
          ["observe", "void-act"]
        ] },
      { id: "decide-grounds", on: "action:decide", "if": "$target.attrs.applied",
        then: [
          ["set", "$target.attrs.gA", "$target.attrs.applicantChild"],
          ["set", "$target.attrs.gB", ["exists", "$target.attrs.atVet"]],
          ["set", "$target.attrs.gC", ["and", ["not", "$target.attrs.chipped"], ["not", ["def", "tChipExempt"]]]],
          ["set", "$target.attrs.gD", ["and", ["not", "$target.attrs.sterilised"], ["not", ["def", "tSterExempt"]]]],
          ["set", "$target.attrs.gE", "$target.attrs.applicantConvictions"],
          ["set", "$target.attrs.mustRefuse", ["or", "$target.attrs.gA", "$target.attrs.gB", "$target.attrs.gC", "$target.attrs.gD", "$target.attrs.gE"]],
          ["set", "$target.attrs.applied", false],
          ["set", "$target.attrs.deciding", true]
        ] },
      { id: "decide-ground-a", on: "action:decide", "if": ["and", "$target.attrs.deciding", "$target.attrs.mustRefuse", "$target.attrs.gA"],
        then: [["log", "Ground (a): the applicant is a child under 18.", { cite: "s. 9(2)(a)" }]] },
      { id: "decide-child-notice", on: "action:decide", "if": ["and", "$target.attrs.deciding", "$target.attrs.mustRefuse", "$target.attrs.gA"],
        then: [
          ["log", "<b>To whom does the notice go?</b> Section 13(1) requires notice to 'the owner of the cat'; the child and the parent are both owners (FORK-02), and the applicant is the child. It must state 'the person's rights' to object and seek review, but s. 13 has introduced no person, only the owner (compare s. 40(1), 'the person affected by the decision'). The objection and review rights belong to 'a person who has been given notice under section 13' (ss. 69(1), 71(1)).",
            { cite: "ss. 13(1), 40(1), 69(1), 71(1)", sev: "warn" }],
          ["observe", "r17"]
        ] },
      { id: "decide-ground-b", on: "action:decide", "if": ["and", "$target.attrs.deciding", "$target.attrs.mustRefuse", "$target.attrs.gB"],
        then: [
          ["log", "<b>Ground (b): {target} is 'in the custody of' veterinary premises today, so it belongs to a class of cats prescribed as exempt from registration (r. 9(2)(e)).</b> Section 9(2)(b) then obliges the local government to refuse -- an owned cat, at the vet for a few days, cannot be registered or renewed while it is there. The same follows for a cat boarding at any facility a local government has approved (r. 9(2)(d), s. 3(1) 'cat management facility' (c)).",
            { cite: "s. 9(2)(b); r. 9(2)(d), (e)", sev: "stop" }],
          ["observe", "d10"]
        ] },
      { id: "decide-ground-c", on: "action:decide", "if": ["and", "$target.attrs.deciding", "$target.attrs.mustRefuse", "$target.attrs.gC"],
        then: [["log", "Ground (c): {target} is not microchipped, and no veterinary certificate applies (s. 9(3) with s. 14(2)-(3)).", { cite: "s. 9(2)(c), (3)" }]] },
      { id: "decide-ground-d", on: "action:decide", "if": ["and", "$target.attrs.deciding", "$target.attrs.mustRefuse", "$target.attrs.gD"],
        then: [["log", "Ground (d): {target} is not sterilised and is not exempt under s. 18(2). A kitten under 6 months is never exempt, because a certificate cannot apply to it (s. 18(3)).", { cite: "s. 9(2)(d), (4)" }]] },
      { id: "decide-kitten", on: "action:decide", "if": ["and", "$target.attrs.deciding", "$target.attrs.mustRefuse", "$target.attrs.gD", ["def", "tUnderSix"]],
        then: [
          ["log", "A kitten under 6 months that is not yet sterilised must be refused registration (ss. 9(2)(d), (4), 18(3)). That costs the owner nothing: the duty to register attaches only at 6 months (s. 5(1)). Verified sound.",
            { cite: "ss. 5(1), 9(2)(d), (4), 18(3)", sev: "ok" }],
          ["observe", "l11"]
        ] },
      { id: "decide-ground-e", on: "action:decide", "if": ["and", "$target.attrs.deciding", "$target.attrs.mustRefuse", "$target.attrs.gE"],
        then: [
          ["log", "Ground (e): the applicant has 2 or more relevant convictions in the previous 3 years, counted together across the three Acts (FORK-10 reading A; the Council amended 'an offence against' to '2 or more offences against any of the following' in 2011). Verified sound.", { cite: "s. 9(2)(e)", sev: "ok" }],
          ["observe", "u12"],
          ["log", "<b>Three years before what?</b> 'Convicted within the previous 3 years': the encoding counts back from the day of decision (FORK-11 reading A). Counted from the application (as Form 1 Part F asks), a conviction that falls out of the window between application and decision would still count, and the result can turn on how quickly the local government decides.",
            { cite: "s. 9(2)(e); Form 1 Part F", sev: "warn" }],
          ["observe", "u13"],
          ["log", "The explanatory memorandum for the Cat Bill 2011 (cl. 9) describes refusal for a single conviction; that describes the Bill as introduced, before the Legislative Council's amendment. Verified sound.",
            { cite: "s. 9(2)(e); LC SNP 197-2", sev: "ok" }],
          ["observe", "x48"]
        ] },
      { id: "decide-refuse", on: "action:decide", "if": ["and", "$target.attrs.deciding", "$target.attrs.mustRefuse"],
        then: [
          ["set", "$target.attrs.deciding", false],
          ["set", "$target.attrs.refusedDay", "$day"],
          ["log", "<b>{self} must refuse</b> to register {target}, and must give the owner written notice of the decision, the reasons and the rights of objection and review within 7 days (s. 13).",
            { cite: "ss. 9(2), 13", sev: "warn" }],
          ["observe", "refused"]
        ] },
      { id: "decide-31-oct", on: "action:decide",
        "if": ["and", "$target.attrs.deciding", ["not", "$target.attrs.mustRefuse"], ["not", "$target.attrs.applied3y"], ["=", ["nextDate", 10, 31], "$day"]],
        then: [
          ["log", "Registered for one year on 31 October: 'the next 31 October' is read as 31 October next year (FORK-05 reading A). Read as today, a one-year registration would last one day; r. 12(1)(a) says it is for 'one year'. Verified sound.",
            { cite: "r. 12(1)(a), (2)(a)(i)", sev: "ok" }],
          ["observe", "u37"]
        ] },
      { id: "decide-nov-dec", on: "action:decide",
        "if": ["and", "$target.attrs.deciding", ["not", "$target.attrs.mustRefuse"], ["not", "$target.attrs.applied3y"], [">", ["def", "daysTo31Oct"], 303]],
        then: [
          ["log", "A one-year grant in November or December costs $20: the $10 rate is for applications 'made after 31 May for registration until the next 31 October', which ties the 31 May to the registration year (FORK-07 reading A). Verified sound.",
            { cite: "Sch. 3 item 1(a)", sev: "ok" }],
          ["observe", "u40"]
        ] },
      { id: "decide-grant", on: "action:decide", "if": ["and", "$target.attrs.deciding", ["not", "$target.attrs.mustRefuse"]],
        then: [
          ["set", "$target.attrs.deciding", false],
          ["set", "$target.attrs.registered", true],
          ["set", "$target.attrs.everRegistered", true],
          ["set", "$target.rels.registeredWith", "$self.id"],
          ["set", "$target.rels.registeredOwner", "$target.attrs.applicantId"],
          ["set", "$target.attrs.grantDay", "$day"],
          ["set", "$target.attrs.regExpiryDay", ["if", "$target.attrs.applied3y", THREE_YEAR_END, NEXT_31_OCT]],
          ["set", "$target.attrs.regExpiryDate", ["date", "$target.attrs.regExpiryDay"]],
          ["set", "$target.attrs.regDays", ["-", "$target.attrs.regExpiryDay", "$day"]],
          ["set", "$target.attrs.wearingTag", true],
          ["set", "$target.attrs.s5Flag", false],
          ["log", "{self} registers {target} until {target.attrs.regExpiryDate} (r. 12(2)(a), FORKS 05 and 06 reading A). It allots a number and gives the owner a certificate in Form 2 and a tag (s. 11(1)).",
            { cite: "ss. 9, 11; r. 12", sev: "ok" }],
          ["observe", "registered"],
          ["log", "<b>From when?</b> Regulation 12(2)(a) says a registration 'has effect from the period specified in the registration certificate'. A registration takes effect from a day, not a period, and the prescribed certificate (Form 2, r. 14) specifies neither: it has a field for the expiry date only.",
            { cite: "r. 12(2)(a); r. 14, Form 2", sev: "warn" }],
          ["observe", "r36"]
        ] },
      { id: "grant-short", on: "action:decide",
        "if": ["and", ["=", "$target.attrs.grantDay", "$day"], ["not", "$target.attrs.applied3y"], ["<", "$target.attrs.regDays", 31]],
        then: [
          ["log", "<b>The registration lasts {target.attrs.regDays} days.</b> A one-year registration runs only to the next 31 October (r. 12(2)(a)(i)), however late in October it is granted; the half fee for June-October grants (Sch. 3 item 1(a)) is the same for five months as for a few days, and a renewal follows almost at once.",
            { cite: "r. 12(2)(a)(i); Sch. 3 item 1", sev: "warn" }],
          ["observe", "t46"]
        ] },
      { id: "grant-3y-short", on: "action:decide",
        "if": ["and", ["=", "$target.attrs.grantDay", "$day"], "$target.attrs.applied3y", ["<", "$target.attrs.regDays", 1000]],
        then: [
          ["log", "<b>A '3-year' registration of {target.attrs.regDays} days.</b> It runs to '31 October in the final year of that period' (r. 12(2)(a)(ii)). On the reading taken (FORK-06 A) one taking effect on 31 October lasts two years and a day; on reading B (the calendar year in which the period ends) some last more than three years; reading C picks a 31 October outside the period.",
            { cite: "r. 12(2)(a)(ii)", sev: "warn" }],
          ["observe", "u38"]
        ] },
      { id: "decide-reset", on: "action:decide", then: [["set", "$target.attrs.applied3y", false]] },

      /* ---- s. 9(5)-(6) and s. 13 ---- */
      { id: "require-over21", on: "action:requireInfo", "if": "$p.over21",
        then: [
          ["log", "A requirement allowing more than 21 days is not one 'under subsection (5)', which allows 'a specified time of not more than 21 days'; s. 9(6) cannot rest on it, and the local government must decide the application. Verified sound: the limit is express.",
            { cite: "s. 9(5), (6)", sev: "ok" }],
          ["observe", "p14"]
        ] },
      { id: "require", on: "action:requireInfo", "if": ["not", "$p.over21"],
        then: [["set", "$target.attrs.infoRequired", true],
               ["log", "The applicant must answer within the time specified, not more than 21 days (s. 9(5)).", { cite: "s. 9(5)" }]] },
      { id: "refuse-to-consider", on: "action:refuseToConsider", "if": "$target.attrs.applied",
        then: [
          ["set", "$target.attrs.applied", false],
          ["set", "$target.attrs.unconsidered", true],
          ["log", "<b>The application is neither granted nor refused.</b> A refusal to consider (s. 9(6)) is not a decision s. 13(2) lists, so no notice, reasons or statement of rights is owed, and Part 4 Division 5 gives no objection or review (s. 68 lists the same decisions). The owner remains bound by s. 5(1) and cannot comply until a fresh application succeeds.",
            { cite: "ss. 9(6), 13(2), 68", sev: "stop" }],
          ["observe", "p15"],
          ["log", "Form 1 Part G tells the applicant that the local government 'may refuse an application' if information is not provided in time. The Act's power is to refuse to consider it, which -- unlike a refusal -- carries no notice and no review.",
            { cite: "s. 9(6); Sch. 1 Form 1 Part G", sev: "warn" }],
          ["observe", "x51"]
        ] },
      { id: "refuse-to-consider-void", on: "action:refuseToConsider", "if": ["not", "$target.attrs.applied"],
        then: [["log", "<b>Nothing has happened.</b> There is no application before the local government.", { cite: "s. 9(6)", sev: "ok" }],
               ["observe", "void-act"]] },
      { id: "notice-lapse", on: "action:letNoticeLapse", "if": ["exists", "$target.attrs.refusedDay"],
        then: [
          ["log", "<b>No notice is given.</b> Section 13 carries no penalty and no other consequence; but the owner's right to object (s. 69(1)) and to apply to the State Administrative Tribunal (s. 71(1)) belongs only to 'a person who has been given notice under section 13'. The local government's default takes away the owner's review.",
            { cite: "ss. 13, 69(1), 71(1)", sev: "stop" }],
          ["observe", "e18"]
        ] },
      { id: "notice-lapse-void", on: "action:letNoticeLapse", "if": ["not", ["exists", "$target.attrs.refusedDay"]],
        then: [["log", "<b>Nothing has happened.</b> No refusal has been made.", { cite: "s. 13", sev: "ok" }], ["observe", "void-act"]] },

      /* ---- r. 12: registration ends ---- */
      { id: "lapse", on: "day", "for": "cat",
        "if": ["and", "$self.attrs.registered", [">", "$day", "$self.attrs.regExpiryDay"]],
        then: [
          ["set", "$self.attrs.registered", false],
          ["set", "$self.rels.registeredWith", null],
          ["set", "$self.rels.registeredOwner", null],
          ["set", "$self.attrs.wearingTag", false],
          ["log", "{self}'s registration ended yesterday, 31 October. From today the owner is whoever keeps and cares for it (s. 4(1)(b)).", { cite: "r. 12(2)(a); s. 4(1)" }],
          ["observe", "lapsed"]
        ] },

      /* ---- the day a cat reaches 6 months ---- */
      { id: "six-months", on: "day", "for": "cat",
        "if": ["and", ["=", ["ageMonths", "$self.attrs.bornDay"], 6], ["not", "$self.attrs.sixSeen"]],
        then: [
          ["set", "$self.attrs.sixSeen", true],
          ["log", "{self} has reached 6 months of age today. The owner's duties to have it registered, microchipped and sterilised attach. The Act does not say how age is reckoned; the encoding uses the numerically corresponding day (FORK-01 reading A, following IA s. 62). Verified sound.",
            { cite: "ss. 5(1), 14(1), 18(1); IA s. 62", sev: "ok" }],
          ["observe", "six-months"],
          ["observe", "u03"]
        ] },
      { id: "breeder-queen", on: "day", "for": "cat",
        "if": ["and", ["def", "sixMonths"], "$self.attrs.breeding", ["attrOf", ["rel", "$self", "keeper"], "approvedBreeder"],
               ["not", "$self.attrs.sterilised"], ["not", "$self.attrs.d25Seen"]],
        then: [
          ["set", "$self.attrs.d25Seen", true],
          ["log", "{self} is owned for breeding by an approved cat breeder, so 'the cat is exempt from sterilisation' (s. 18(2)(b)). The exemption attaches to the cat, so every owner of it has the benefit. Verified sound.",
            { cite: "s. 18(2)(b)", sev: "ok" }],
          ["observe", "d25"]
        ] },

      /* ---- s. 5 ---- */
      { id: "s5-grace-ends", on: "day", "for": "cat",
        "if": ["and", ["def", "sixMonths"], ["exists", "$self.rels.keeper"], ["not", "$self.attrs.registered"],
               ["=", ["daysSince", "$self.attrs.keptSinceDay"], 14]],
        then: [
          ["log", "Today is the 14th day after {self} was taken in. The days are counted as IA s. 61(1)(b) and (g) count them, without the first day, so the s. 5(2)(a) grace ends today (FORK-04 reading A); counting both days it would have ended yesterday. Verified sound.",
            { cite: "s. 5(2)(a); IA s. 61(1)(b), (g)", sev: "ok" }],
          ["observe", "u07"]
        ] },
      { id: "s5-parent", on: "day", "for": "cat",
        "if": ["and", ["def", "s5Due"], ["<", ["ageYears", ["attrOf", ["rel", "$self", "keeper"], "bornDay"]], 18]],
        then: [
          ["log", "<b>Whose 14 days?</b> {self} is kept by a child, so the child's parent is an owner too (s. 4(1)(c)). Section 5(2)(a) exempts the owner while 'the cat has been kept by the person for less than 14 days' -- and the section has introduced no 'person', only 'the owner'. On reading A (taken) the parent is treated as having kept the cat since the child did, and is now in breach; on reading B the parent, who keeps nothing, is exempt for ever (FORK-03).",
            { cite: "ss. 4(1)(c), 5(2)(a)", sev: "warn" }],
          ["observe", "u06"]
        ] },
      { id: "s5-nonresident", on: "day", "for": "cat",
        "if": ["and", ["def", "s5Due"], ["attrOf", ["rel", "$self", "keeper"], "nonResident"]],
        then: [
          ["log", "{self}'s keeper has never been resident in the State. Section 5(2)(b) ('has been resident in the State for less than 14 days') is read as a period of grace for newcomers, not a permanent exemption for non-residents (FORK-09 reading A, preferred under IA s. 18). Verified sound.",
            { cite: "s. 5(2)(b); IA s. 18", sev: "ok" }],
          ["observe", "u08"]
        ] },
      { id: "s5-moved", on: "day", "for": "cat",
        "if": ["and", "$self.attrs.registered", ["not", ["=", "$self.rels.registeredWith", "$self.rels.keptIn"]], ["not", "$self.attrs.l09Seen"]],
        then: [
          ["set", "$self.attrs.l09Seen", true],
          ["log", "<b>{self} is registered, but with the local government of the district it has left.</b> Section 5(1) requires registration 'with the local government in whose district the cat is ordinarily kept', from the day of the move: there is no period of grace. Regulation 13 lets the owner 'notify both ... to continue that period of registration with the new local government' but nothing in the Act or the regulations says what the notice does.",
            { cite: "s. 5(1); r. 13; s. 10(a)(iii)", sev: "stop" }],
          ["observe", "l09"]
        ] },
      { id: "s5", on: "day", "for": "cat",
        "if": ["def", "s5Due"],
        then: [
          ["set", "$self.attrs.s5Flag", true],
          ["log", "<b>{self} is 6 months or older and is not registered with the local government of its district.</b> Its owner contravenes s. 5(1) (penalty $5 000). Whether the failure is a further offence each day after a conviction depends on whether IA s. 71(2) reaches a duty to 'ensure' a state of affairs (FORK-12; reading A, taken, says it does).",
            { cite: "s. 5(1); IA ss. 71, 72", sev: "stop" }],
          ["observe", "s5"],
          ["observe", "u44"]
        ] },
      { id: "move", on: "action:moveDistrict",
        then: [["set", "$target.rels.keptIn", "lg2"],
               ["log", "{target} is now ordinarily kept in the Shire of Kalamunda.", { cite: "s. 5(1)" }]] },
      { id: "notify-move", on: "action:notifyMove",
        then: [
          ["log", "<b>Nothing follows from the notice.</b> Regulation 13 permits it, but neither the Act nor the regulations make {target} 'registered with' the new local government, by any decision or with any number or tag; s. 9 registers only on an application under s. 8, and s. 10(a)(iii) lets the old local government cancel once the cat 'has been registered with another local government'.",
            { cite: "r. 13; ss. 5(1), 9, 10(a)(iii)", sev: "stop" }],
          ["observe", "l09"]
        ] },

      /* ---- r. 9: custody and foster care ---- */
      { id: "at-vet", on: "action:leaveAtVet", then: [["set", "$target.attrs.atVet", true]] },
      { id: "from-vet", on: "action:collectFromVet", then: [["set", "$target.attrs.atVet", null]] },
      { id: "foster", on: "action:placeInFoster", then: [["set", "$target.attrs.fosterDay", "$day"]] },
      { id: "foster-ends", on: "day", "for": "cat",
        "if": ["and", ["exists", "$self.attrs.fosterDay"], ["=", ["daysSince", "$self.attrs.fosterDay"], 85]],
        then: [
          ["log", "{self} has been in foster care placed by a SAFE entity for more than 12 weeks, so it is no longer exempt from registration (r. 9(3)(b): 'a total of 12 weeks', counted over all its time in foster care). Verified sound.",
            { cite: "r. 9(3)(b)", sev: "ok" }],
          ["observe", "t42"]
        ] },

      /* ---- Division 2: microchipping ---- */
      { id: "implant", on: "action:implant", "if": ["and", "$self.attrs.microchipImplanter", ["not", "$p.noDatabase"]],
        then: [
          ["set", "$target.attrs.chipped", true],
          ["set", "$target.rels.implanter", "$self.id"],
          ["set", "$target.rels.company", "co1"],
          ["set", "$target.attrs.s15Notified", false],
          ["set", "$target.attrs.s15DueDay", ["+", "$day", 7]],
          ["set", "$target.attrs.s15DueDate", ["date", ["+", "$day", 7]]],
          ["log", "{target} is microchipped. {self} must give the microchip database company the r. 17 information by {target.attrs.s15DueDate} (s. 15).",
            { cite: "ss. 3(1), 15; rr. 8, 17" }]
        ] },
      { id: "implant-nodb", on: "action:implant", "if": ["and", "$self.attrs.microchipImplanter", "$p.noDatabase"],
        then: [
          ["set", "$target.attrs.chipped", true],
          ["set", "$target.rels.implanter", "$self.id"],
          ["log", "<b>{target} is microchipped, and s. 15 has nobody to be told.</b> The implanter must notify 'the microchip database company for that cat', which is the company that 'keeps, or has agreed to keep' its records (s. 3(1)). No company has agreed, so there is none, and the duty has no addressee: the chip identifies nobody.",
            { cite: "ss. 3(1) 'microchip database company' (b), 15", sev: "stop" }],
          ["observe", "r20"]
        ] },
      { id: "implant-not-implanter", on: "action:implant", "if": ["not", "$self.attrs.microchipImplanter"],
        then: [
          ["set", "$target.attrs.chipByNonImplanter", true],
          ["log", "<b>{target} is not 'microchipped'.</b> A chip counts only if a microchip implanter implants it (r. 8), and {self} is not one (r. 7): a veterinarian registered only in another State who does not practise in WA is not a 'veterinarian' (VPA s. 22(1)(c)), and an overseas one never is. The owner's s. 14(1) duty is unmet, registration must be refused (s. 9(2)(c)), and s. 17 forbids removing the chip.",
            { cite: "s. 3(1); rr. 7, 8; VPA s. 22", sev: "warn" }],
          ["observe", "d05"]
        ] },
      { id: "s15-late", on: "day", "for": "cat",
        "if": ["and", "$self.attrs.chipped", ["exists", "$self.attrs.s15DueDay"], ["not", "$self.attrs.s15Notified"],
               [">", "$day", "$self.attrs.s15DueDay"], ["not", "$self.attrs.s15Flag"]],
        then: [
          ["set", "$self.attrs.s15Flag", true],
          ["log", "<b>The microchip implanter has not notified the database company within 7 days.</b> Contravention of s. 15; the obligation continues (IA s. 71(1)). The console does not move a deadline off a weekend or holiday; the L4 does (IA s. 61(1)(e)).",
            { cite: "s. 15; IA ss. 61, 71", sev: "stop" }],
          ["observe", "s15"],
          ["log", "<b>And the company is in breach of s. 16.</b> It 'must keep and maintain in its microchip database the information prescribed under section 15', which it has never been given. The Dog Amendment (Stop Puppy Farming) Act 2021 s. 53 would limit the duty to information 'that has been given to it'; that section has not commenced.",
            { cite: "s. 16", sev: "warn" }],
          ["observe", "w21"]
        ] },
      { id: "notify-implant", on: "action:notifyImplant", "if": ["=", "$target.rels.implanter", "$self.id"],
        then: [["set", "$target.attrs.s15Notified", true]] },
      { id: "notify-implant-presumed", on: "action:notifyImplant", "if": ["and", ["=", "$target.rels.implanter", "$self.id"], ["not", "$target.attrs.registered"]],
        then: [
          ["log", "{target} is unregistered and now microchipped, so the person the database records as owner 'is to be taken, in the absence of evidence to the contrary', to keep and care for it (s. 4(2)). The presumption gives no day on which that keeping began (s. 5(2)(a)); evidence of when it did is evidence to the contrary. Verified sound.",
            { cite: "ss. 4(2), 5(2)(a)", sev: "ok" }],
          ["observe", "d02"]
        ] },
      { id: "notify-implant-other", on: "action:notifyImplant", "if": ["not", ["=", "$target.rels.implanter", "$self.id"]],
        then: [
          ["log", "<b>That does not discharge s. 15.</b> The duty is the implanter's, and {self} did not implant {target}'s chip.", { cite: "s. 15", sev: "ok" }],
          ["observe", "void-act"]
        ] },
      { id: "practice-details", on: "action:changePracticeDetails", "if": ["=", "$target.rels.implanter", "$self.id"],
        then: [["set", "$target.attrs.implChangeDay", "$day"],
               ["log", "The implanter's business contact details are information prescribed under s. 15 (r. 17(e)).", { cite: "r. 17(e)" }]] },
      { id: "practice-details-late", on: "day", "for": "cat",
        "if": ["and", ["exists", "$self.attrs.implChangeDay"], [">", ["daysSince", "$self.attrs.implChangeDay"], 7], ["not", "$self.attrs.t35Seen"], ["exists", "$self.rels.company"]],
        then: [
          ["set", "$self.attrs.t35Seen", true],
          ["log", "<b>{self}'s owner contravenes s. 25.</b> There was 'a change to ... the information prescribed under section 15' (the implanter's contact details, r. 17(e)), and the owner had to tell the company 'within 7 days after the change'. The owner was never told of it. The clock runs from the change, not from the owner's knowledge; the Stop Puppy Farming Act 2021 s. 55 would run it from when the owner 'becomes aware', but has not commenced.",
            { cite: "s. 25(b); r. 17(c)-(e)", sev: "stop" }],
          ["observe", "t35"]
        ] },
      { id: "age-change", on: "day", "for": "cat",
        "if": ["and", "$self.attrs.chipped", ["exists", "$self.rels.company"], ["=", ["ageMonths", "$self.attrs.bornDay"], 12], ["not", "$self.attrs.u34Seen"]],
        then: [
          ["set", "$self.attrs.u34Seen", true],
          ["log", "<b>{self} is a year old.</b> 'The age' of the cat is information prescribed under s. 15 (r. 17(m)), and s. 25(b) requires notice of 'a change to any of' it within 7 days. On the reading taken (FORK-15 A) the age is fixed as at implanting and does not 'change'; read literally, every owner of a microchipped cat must notify the company every time the cat grows older.",
            { cite: "s. 25(b); r. 17(m)", sev: "warn" }],
          ["observe", "u34"]
        ] },
      { id: "certify-chip", on: "action:certifyChip", "if": "$self.attrs.vet",
        then: [
          ["set", "$target.attrs.chipCert", true],
          ["log", "The certificate exempts {target} from microchipping, but only once it is 6 months old (s. 14(3), read on the day in question: FORK-13). Sections 14(2)-(3) came into operation on 1 November 2012, a year before the duty in s. 14(1), because the registration rules in s. 9(3) needed them from then (s. 2(b), (c)); verified sound.", { cite: "ss. 2, 9(3), 14(2), (3)", sev: "ok" }],
          ["observe", "t45"]
        ] },
      { id: "certify-chip-young", on: "action:certifyChip", "if": ["and", "$self.attrs.vet", ["def", "tUnderSix"]],
        then: [
          ["log", "<b>{target} is under 6 months.</b> 'A certificate ... cannot apply in respect of a cat that is under 6 months of age' (s. 14(3)). On reading A (taken) this certificate starts to apply when {target} turns 6 months; on reading B it never applies and a new one must be obtained, or the owner is in breach of s. 14(1) from that day (FORK-13).",
            { cite: "s. 14(2), (3)", sev: "warn" }],
          ["observe", "u19"]
        ] },
      { id: "certify-chip-void", on: "action:certifyChip", "if": ["not", "$self.attrs.vet"],
        then: [
          ["log", "<b>Nothing has happened.</b> Only a certificate given by a veterinarian counts (s. 14(2)).", { cite: "s. 14(2)", sev: "ok" }],
          ["observe", "void-act"]
        ] },
      { id: "s14", on: "day", "for": "cat",
        "if": ["and", ["def", "sixMonths"], ["not", "$self.attrs.chipped"], ["not", ["def", "chipExempt"]],
               ["exists", "$self.rels.keeper"], ["not", "$self.attrs.s14Flag"]],
        then: [
          ["set", "$self.attrs.s14Flag", true],
          ["log", "<b>{self} is 6 months or older and is not microchipped.</b> Its owner contravenes s. 14(1) (penalty $5 000).", { cite: "s. 14(1)", sev: "stop" }],
          ["observe", "s14"]
        ] },

      /* ---- Division 3: sterilisation ---- */
      { id: "sterilise-vet", on: "action:sterilise", "if": "$self.attrs.vet",
        then: [
          ["set", "$target.attrs.sterilised", true],
          ["set", "$target.attrs.sterilisedByVet", true],
          ["set", "$target.rels.sterilisedBy", "$self.id"],
          ["set", "$target.attrs.s21Given", false],
          ["set", "$target.attrs.s20Applies", ["and", "$target.attrs.chipped", ["exists", "$target.rels.company"]]],
          ["set", "$target.attrs.s20Notified", false],
          ["set", "$target.attrs.s20DueDay", ["+", "$day", 7]],
          ["log", "{target} is sterilised by a veterinarian. {self} must give the owner a certificate of sterilisation (s. 21) and, if the cat is microchipped, notify the database company within 7 days (s. 20).",
            { cite: "ss. 18(1), 20, 21" }],
          ["log", "Section 21 fixes no time for the certificate: it must be given 'with all convenient speed' (IA s. 63). Verified sound.", { cite: "s. 21; IA s. 63", sev: "ok" }],
          ["observe", "t23"]
        ] },
      { id: "sterilise-nonvet", on: "action:sterilise", "if": ["not", "$self.attrs.vet"],
        then: [
          ["set", "$target.attrs.sterilised", true],
          ["log", "<b>{target} is sterilised, but not by a veterinarian.</b> Section 18(1) requires the owner to ensure the cat is sterilised 'by a veterinarian'. A veterinarian registered only in another State who does not practise in WA is not one (VPA s. 22(1)(c)); nor is any overseas veterinarian. The owner can never comply short of a second operation -- yet registration may not be refused, because s. 9(2)(d) asks only whether the cat is sterilised.",
            { cite: "ss. 3(1), 9(2)(d), 18(1); VPA ss. 3, 22", sev: "warn" }],
          ["observe", "d22"]
        ] },
      { id: "s20-late", on: "day", "for": "cat",
        "if": ["and", "$self.attrs.s20Applies", ["not", "$self.attrs.s20Notified"], [">", "$day", "$self.attrs.s20DueDay"], ["not", "$self.attrs.s20Flag"]],
        then: [
          ["set", "$self.attrs.s20Flag", true],
          ["log", "<b>The veterinarian has not notified the database company of the sterilisation within 7 days.</b> Contravention of s. 20.", { cite: "s. 20", sev: "stop" }],
          ["observe", "s20"]
        ] },
      { id: "notify-ster", on: "action:notifySterilisation", "if": ["=", "$target.rels.sterilisedBy", "$self.id"],
        then: [["set", "$target.attrs.s20Notified", true]] },
      { id: "give-cert", on: "action:giveCertificate", "if": ["=", "$target.rels.sterilisedBy", "$self.id"],
        then: [["set", "$target.attrs.s21Given", true], ["log", "Section 21 is complied with.", { cite: "s. 21", sev: "ok" }]] },
      { id: "false-cert", on: "action:giveFalseCertificate", "if": ["not", "$target.attrs.sterilised"],
        then: [
          ["log", "<b>No offence under s. 19.</b> Section 19 forbids identifying an unsterilised cat as sterilised 'in the manner prescribed'; r. 18(1) prescribes 'a sterilisation certificate given ... under section 21' or the ear tattoo. A certificate under s. 21 is one a veterinarian gives after sterilising the cat, so a false one is never 'given under section 21': s. 19 reaches only the tattoo.",
            { cite: "s. 19; r. 18(1); s. 21", sev: "stop" }],
          ["observe", "r24"]
        ] },
      { id: "certify-ster", on: "action:certifySter", "if": "$self.attrs.vet",
        then: [
          ["set", "$target.attrs.sterCert", true],
          ["log", "The certificate exempts {target} from sterilisation once it is 6 months old (s. 18(3), FORK-13).", { cite: "s. 18(2)(a), (3)" }]
        ] },
      { id: "certify-ster-void", on: "action:certifySter", "if": ["not", "$self.attrs.vet"],
        then: [
          ["log", "<b>Nothing has happened.</b> Only a certificate given by a veterinarian counts (s. 18(2)(a)).", { cite: "s. 18(2)(a)", sev: "ok" }],
          ["observe", "void-act"]
        ] },
      { id: "s18", on: "day", "for": "cat",
        "if": ["and", ["def", "sixMonths"], ["not", "$self.attrs.sterilisedByVet"], ["not", ["def", "sterExempt"]],
               ["exists", "$self.rels.keeper"], ["not", "$self.attrs.s18Flag"]],
        then: [
          ["set", "$self.attrs.s18Flag", true],
          ["log", "<b>{self} is 6 months or older and has not been sterilised by a veterinarian.</b> Its owner contravenes s. 18(1) (penalty $5 000).", { cite: "s. 18(1)", sev: "stop" }],
          ["observe", "s18"]
        ] },
      { id: "tattoo", on: "action:tattoo",
        then: [["set", "$target.attrs.earTattoo", true]] },
      { id: "tattoo-unsterilised", on: "action:tattoo", "if": ["not", "$target.attrs.sterilised"],
        then: [
          ["log", "<b>{target} is not sterilised.</b> Identifying it as sterilised by the r. 18 tattoo contravenes s. 19 (penalty $5 000).", { cite: "s. 19; r. 18", sev: "stop" }],
          ["observe", "s19"]
        ] },

      /* ---- Division 4: transfer ---- */
      { id: "acquire-own", on: "action:acquire", "if": ["=", "$target.rels.keeper", "$self.id"],
        then: [
          ["log", "<b>Nothing has happened.</b> {self} already keeps {target}.", { cite: "s. 3(1) 'transfer'", sev: "ok" }],
          ["observe", "void-act"]
        ] },
      { id: "acquire-s23-1", on: "action:acquire",
        "if": ["and", ["not", ["=", "$target.rels.keeper", "$self.id"]], ["not", "$target.attrs.chipped"], ["not", ["def", "tChipExempt"]]],
        then: [
          ["log", "<b>{target} is transferred though not microchipped.</b> The seller contravenes s. 23(1) (penalty $5 000), unless satisfied a s. 14(2) certificate applies; for a kitten under 6 months none can (s. 14(3)).",
            { cite: "s. 23(1)", sev: "stop" }],
          ["observe", "s23"]
        ] },
      { id: "acquire-kitten-unchipped", on: "action:acquire",
        "if": ["and", ["not", ["=", "$target.rels.keeper", "$self.id"]], ["not", "$target.attrs.chipped"], ["def", "tUnderSix"]],
        then: [
          ["log", "An unchipped kitten under 6 months can be transferred lawfully only to a body set out in r. 9 (r. 19): no veterinary certificate can apply to it (s. 14(3)), and s. 23(1) has no voucher route. That is the scheme the Cat Bill 2011 described: every cat microchipped before transfer. Verified sound.",
            { cite: "ss. 14(3), 23(1); r. 19", sev: "ok" }],
          ["observe", "l28"]
        ] },
      { id: "acquire-s23-2", on: "action:acquire",
        "if": ["and", ["not", ["=", "$target.rels.keeper", "$self.id"]], ["not", "$target.attrs.sterilised"], ["not", ["def", "tSterExempt"]], ["not", "$p.voucher"],
               ["not", ["and", "$self.attrs.approvedBreeder", "$target.attrs.breeding"]]],
        then: [
          ["log", "<b>{target} is transferred unsterilised, with no voucher.</b> The seller contravenes s. 23(2) (penalty $5 000).", { cite: "s. 23(2)", sev: "stop" }],
          ["observe", "s23"],
          ["log", "Section 23(2)(a)(iii) would excuse a seller satisfied that the cat 'belongs to a class of cats prescribed as exempt from sterilisation', and s. 18(2)(c) exempts such a class; no regulation prescribes one, so neither limb can apply. The Act permits a class to be prescribed; it does not require one. Verified sound.",
            { cite: "ss. 18(2)(c), 23(2)(a)(iii), 76(1)", sev: "ok" }],
          ["observe", "l26"]
        ] },
      { id: "acquire-voucher-adult", on: "action:acquire",
        "if": ["and", ["not", ["=", "$target.rels.keeper", "$self.id"]], ["not", "$target.attrs.sterilised"], "$p.voucher", ["not", ["def", "tUnderSix"]]],
        then: [
          ["log", "An adult cat is transferred entire with a sterilisation voucher. The explanatory memorandum says the voucher is 'only intended' for cats too young to be sterilised; s. 23(2)(b) has no such limit, and a Council amendment that would have imposed one was not made. The words are clear, so the memorandum cannot change them (IA s. 19). Verified sound.",
            { cite: "s. 23(2)(b); IA s. 19", sev: "ok" }],
          ["observe", "x49"]
        ] },
      { id: "acquire-registered", on: "action:acquire",
        "if": ["and", ["not", ["=", "$target.rels.keeper", "$self.id"]], "$target.attrs.registered"],
        then: [
          ["log", "<b>{target} stays registered in the seller's name, so the seller stays its owner.</b> For a registered cat 'owner' means only 'the registered owner' (s. 4(1)(a)), and nothing in Part 2 moves the registration to the purchaser: s. 24 requires notice of the purchaser's name, but no provision then registers the cat in it, and s. 12(4) corrects only errors. Until the registration ends -- for a lifetime registration, never -- the seller bears ss. 5, 6(1), 14, 18 and 25 for a cat it no longer has, and the purchaser bears none of them and may not apply to register it (s. 8(1)).",
            { cite: "ss. 3(1), 4(1)(a), 8(1), 12(4), 24", sev: "stop" }],
          ["observe", "d01"],
          ["log", "<b>Two duties for one change.</b> The seller must notify the local government and the company of the purchaser's name and address under s. 24; and, still the registered owner, must also notify the same change to 'the cat owner's full name' under s. 25 (rr. 16(a), 17(g)), on the same 7-day clock -- two offences for one omission.",
            { cite: "ss. 24, 25; rr. 16, 17", sev: "warn" }],
          ["observe", "l33"]
        ] },
      { id: "acquire-unnotifiable", on: "action:acquire",
        "if": ["and", ["not", ["=", "$target.rels.keeper", "$self.id"]], ["not", "$target.attrs.registered"], ["not", ["exists", "$target.rels.company"]]],
        then: [
          ["log", "{target} is neither registered nor recorded with a database company, so neither paragraph of s. 24 has an addressee ('the local government with which the cat is registered'; 'the microchip database company for that cat'), and there is nothing to notify. Verified sound.",
            { cite: "s. 24(a), (b)", sev: "ok" }],
          ["observe", "r32"]
        ] },
      { id: "acquire", on: "action:acquire", "if": ["not", ["=", "$target.rels.keeper", "$self.id"]],
        then: [
          ["set", "$target.attrs.sellerId", "$target.rels.keeper"],
          ["set", "$target.attrs.s24Pending", ["or", "$target.attrs.registered", ["exists", "$target.rels.company"]]],
          ["set", "$target.attrs.s24Notified", false],
          ["set", "$target.attrs.s24Flag", false],
          ["set", "$target.attrs.s24DueDay", ["+", "$day", 7]],
          ["set", "$target.rels.keeper", "$self.id"],
          ["set", "$target.attrs.keptSinceDay", "$day"],
          ["set", "$target.attrs.s5Flag", false],
          ["log", "{self} now keeps and cares for {target}.", { cite: "ss. 4(1), 22" }]
        ] },
      { id: "offer", on: "action:offerForSale",
        then: [
          ["log", "<b>An offer for sale is a 'transfer'</b> (s. 3(1) 'transfer' (a)), so s. 24 requires the seller, within 7 days, to give notice of 'the name and address of the purchaser of the cat' -- and there is no purchaser. (Section 23 also applies to the offer, which is its point.) The Stop Puppy Farming Act 2021 s. 50(4) would delete 'offer for sale' from the definition; it has not commenced.",
            { cite: "ss. 3(1), 22, 24", sev: "warn" }],
          ["observe", "d31"]
        ] },
      { id: "surrender-vet", on: "action:surrenderToVet",
        then: [
          ["log", "<b>Section 23 does not apply.</b> Regulation 19 disapplies s. 23(1) and (2) for a transfer 'to an organisation or person set out in regulation 9', and r. 9 now sets out veterinary premises and any cat management facility -- including a private facility a local government has approved (s. 3(1)). When r. 19 was made, r. 9 listed no such places; it was replaced in 2018 and amended in 2022, and r. 19 was not revisited (IA s. 16(2) makes the reference ambulatory). Premises are not an 'organisation or person' at all.",
            { cite: "s. 23(3); rr. 9(2)(d), (e), 19; IA s. 16", sev: "warn" }],
          ["observe", "r29"]
        ] },
      { id: "give-safe", on: "action:giveToSafe",
        then: [
          ["log", "<b>Is a SAFE group 'set out in regulation 9'?</b> Regulation 9 names the SAFE entities only as bodies that place cats into foster care (r. 9(1), (3)(b)), not as custodians whose custody exempts a cat. On reading A (taken) the gift is outside s. 23; on reading B the giver of an unchipped or entire cat commits an offence (FORK-08).",
            { cite: "r. 19; r. 9(1), (3)(b); s. 23", sev: "warn" }],
          ["observe", "u30"]
        ] },
      { id: "impound", on: "action:impound", then: [["set", "$target.attrs.impounded", true], ["set", "$target.attrs.impoundedBy", "$self.id"]] },
      { id: "reclaim", on: "action:reclaim", "if": "$target.attrs.impounded",
        then: [
          ["set", "$target.attrs.impounded", false],
          ["log", "<b>Who transferred {target}?</b> 'Transfer' includes 'to reclaim from a cat management facility' (s. 3(1)), and s. 22 defines the seller as 'the person by whom the cat is transferred'. On reading A (taken) the pound's operator is the seller, and -- the cat being unchipped or entire -- the operator contravenes s. 23 and owes the s. 24 notice of a 'purchaser' who was the owner all along; on reading B the owner who reclaims is the seller, and there is then no purchaser at all (FORK-14).",
            { cite: "ss. 3(1), 22-24, 33", sev: "warn" }],
          ["observe", "u27"]
        ] },
      { id: "reclaim-void", on: "action:reclaim", "if": ["not", "$target.attrs.impounded"],
        then: [["log", "<b>Nothing has happened.</b> {target} is not impounded.", { cite: "s. 3(1)", sev: "ok" }], ["observe", "void-act"]] },
      { id: "s24-late", on: "day", "for": "cat",
        "if": ["and", "$self.attrs.s24Pending", ["not", "$self.attrs.s24Notified"], [">", "$day", "$self.attrs.s24DueDay"], ["not", "$self.attrs.s24Flag"]],
        then: [
          ["set", "$self.attrs.s24Flag", true],
          ["log", "<b>The seller has not given notice of the transfer within 7 days.</b> Contravention of s. 24 (penalty $5 000).", { cite: "s. 24", sev: "stop" }],
          ["observe", "s24"]
        ] },
      { id: "notify-transfer", on: "action:notifyTransfer", "if": ["=", "$target.attrs.sellerId", "$self.id"],
        then: [["set", "$target.attrs.s24Notified", true]] },
      { id: "notify-transfer-other", on: "action:notifyTransfer", "if": ["not", ["=", "$target.attrs.sellerId", "$self.id"]],
        then: [
          ["log", "<b>That does not discharge s. 24.</b> The duty is the seller's.", { cite: "s. 24", sev: "ok" }],
          ["observe", "void-act"]
        ] },

      /* ---- s. 6, s. 7 and s. 11(2): tags ---- */
      { id: "go-out-untagged", on: "action:goOut", "if": ["and", "$self.attrs.registered", ["not", "$self.attrs.wearingTag"], ["not", "$p.exhibited"]],
        then: [
          ["log", "<b>{self} is in a public place without its registration tag.</b> Its registered owner contravenes s. 6(1) (penalty $5 000), subject to the s. 6(3) defence and the r. 10 show exemption.",
            { cite: "s. 6; r. 10", sev: "stop" }],
          ["observe", "s6"]
        ] },
      { id: "go-out-exhibited", on: "action:goOut", "if": ["and", "$self.attrs.registered", ["not", "$self.attrs.wearingTag"], "$p.exhibited"],
        then: [
          ["log", "{self} is being exhibited at a show, untagged. Regulation 10(2) exempts 'the owner of a cat that is being exhibited' rather than prescribing 'a class of cats' as s. 6(2) contemplates; but the exemption is defined entirely by the cats being exhibited, so in substance it is the s. 6(2) class. Verified sound.",
            { cite: "s. 6(2); r. 10", sev: "ok" }],
          ["observe", "p43"]
        ] },
      { id: "fake-tag", on: "action:fakeTag",
        then: [
          ["log", "<b>No offence.</b> Section 7 forbids removing or interfering with 'a registration tag worn by a cat', and a registration tag is 'the registration tag given to the owner ... under section 11(1)(c)' (s. 3(1)). A home-made tag is not one. The Cat Bill 2011 explanatory memorandum (cl. 7) presents s. 7 as mainly about forged tags and tags put on unregistered cats; its words reach neither.",
            { cite: "ss. 3(1), 7", sev: "warn" }],
          ["observe", "x47"]
        ] },
      { id: "lose-tag", on: "action:loseTag", then: [["set", "$self.attrs.wearingTag", false]] },
      { id: "replace-tag", on: "action:replaceTag", "if": ["=", "$target.rels.registeredWith", "$self.id"],
        then: [["set", "$target.attrs.wearingTag", true]] },
      { id: "replace-tag-void", on: "action:replaceTag", "if": ["not", ["=", "$target.rels.registeredWith", "$self.id"]],
        then: [
          ["log", "<b>Nothing has happened.</b> Only the local government that registered {target} may give a new tag (s. 11(2)).", { cite: "s. 11(2)", sev: "ok" }],
          ["observe", "void-act"]
        ] }
    ],

    observations: [
      /* neutral counters */
      { id: "six-months", sev: "ok", label: "A cat reaches 6 months", cite: "ss. 5(1), 14(1), 18(1)",
        what: "A cat reaches 6 months of age.", why: "The day the owner's three duties attach." },
      { id: "registered", sev: "ok", label: "A cat is registered", cite: "s. 9", what: "A local government grants registration.", why: "Counted." },
      { id: "refused", sev: "warn", label: "An application is refused", cite: "s. 9(2)", what: "A local government must refuse an application.", why: "Counted." },
      { id: "lapsed", sev: "ok", label: "A registration ends on 31 October", cite: "r. 12(2)(a)", what: "A registration expires.", why: "Counted." },
      { id: "s5", sev: "stop", label: "s. 5(1): a cat 6 months or older is unregistered", cite: "s. 5(1)", what: "The owner's duty to register is unmet.", why: "Counted." },
      { id: "s6", sev: "stop", label: "s. 6(1): a registered cat in public without its tag", cite: "s. 6(1)", what: "A registered cat is in a public place untagged.", why: "Counted." },
      { id: "s14", sev: "stop", label: "s. 14(1): a cat 6 months or older is not microchipped", cite: "s. 14(1)", what: "The owner's duty to microchip is unmet.", why: "Counted." },
      { id: "s15", sev: "stop", label: "s. 15: implant not notified within 7 days", cite: "s. 15", what: "The implanter's notice is late.", why: "Counted." },
      { id: "s18", sev: "stop", label: "s. 18(1): a cat 6 months or older is not sterilised by a veterinarian", cite: "s. 18(1)", what: "The owner's duty to sterilise is unmet.", why: "Counted." },
      { id: "s19", sev: "stop", label: "s. 19: an unsterilised cat identified as sterilised", cite: "s. 19", what: "The r. 18 tattoo on an entire cat.", why: "Counted." },
      { id: "s20", sev: "stop", label: "s. 20: sterilisation not notified within 7 days", cite: "s. 20", what: "The veterinarian's notice is late.", why: "Counted." },
      { id: "s23", sev: "stop", label: "s. 23: a cat transferred unchipped or unsterilised", cite: "s. 23", what: "A transfer contravenes s. 23(1) or (2).", why: "Counted." },
      { id: "s24", sev: "stop", label: "s. 24: transfer not notified within 7 days", cite: "s. 24", what: "The seller's notice is late.", why: "Counted." },
      { id: "void-act", sev: "ok", label: "An act with no legal effect", cite: "ss. 8, 9, 11(2), 13, 14(2), 15, 18(2), 24",
        what: "Someone does something the Act gives them no power or duty to do.", why: "Shown, not prevented: the console reports the nullity." },

      /* findings: incidents.json, by severity */
      { id: "d01", ref: "D-01", foundBy: "ENC", sev: "stop", label: "After a sale the seller stays the owner; the buyer cannot register the cat",
        cite: "s. 4(1)(a); ss. 5, 6, 8(1), 24, 25", what: "A registered cat is sold or given away.",
        why: "For a registered cat 'owner' means only the registered owner, and nothing moves a registration to the purchaser. The seller keeps every owner's duty for a cat it no longer has (for life, under a lifetime registration); the purchaser has none and may not apply. OPEN, high." },
      { id: "d05", ref: "D-05", foundBy: "ENC", sev: "warn", label: "A chip implanted interstate or overseas does not make a cat 'microchipped'",
        cite: "s. 3(1) 'microchipped'; rr. 7, 8; VPA s. 22", what: "A cat is chipped by someone who is not a 'microchip implanter', such as a vet registered only in another State.",
        why: "Only an implant by a WA-registered or WA-practising veterinarian, a WA veterinary nurse or a qualified implanter counts. A cat brought to WA from another State or overseas is 'not microchipped': its owner is in breach of s. 14(1), its registration must be refused, and the only cure is a second chip. OPEN, medium-high." },
      { id: "d22", ref: "D-22", foundBy: "ENC", sev: "warn", label: "A cat desexed interstate or overseas is never 'sterilised by a veterinarian'",
        cite: "s. 18(1); s. 3(1) 'veterinarian'; VPA ss. 3, 22", what: "A cat is desexed by someone who is not a 'veterinarian' as the Cat Act defines it.",
        why: "Since 2022 'veterinarian' means a WA veterinarian or an interstate one who practises in WA. The owner of a cat desexed elsewhere can never comply with s. 18(1), though s. 9(2)(d) lets the cat be registered. OPEN, medium-high." },
      { id: "l09", ref: "L-09", foundBy: "ENC", sev: "stop", label: "An owner who moves district is in breach at once, and r. 13's notice does nothing",
        cite: "s. 5(1); r. 13; s. 10(a)(iii)", what: "The owner of a registered cat moves to another district.",
        why: "Section 5(1) requires registration where the cat is kept, from the day of the move. Regulation 13 lets the owner notify both councils 'to continue that period of registration', but no provision gives the notice an effect. OPEN, medium." },
      { id: "d10", ref: "D-10", foundBy: "CMP", sev: "stop", label: "An owned cat at the vet, or boarding at an approved facility, must be refused registration",
        cite: "s. 9(2)(b); r. 9(2)(d), (e)", what: "A registration or renewal is decided while the cat is at a veterinary clinic or approved cattery.",
        why: "Regulation 9(2) exempts from registration any cat 'in the custody of' veterinary premises or a cat management facility, and s. 9(2)(b) then requires the local government to refuse. The class was meant for shelter cats. OPEN, medium." },
      { id: "p15", ref: "P-15", foundBy: "ENC", sev: "stop", label: "A refusal to consider has no notice, no reasons and no review",
        cite: "ss. 9(6), 13(2), 68", what: "A local government refuses to consider an application under s. 9(6).",
        why: "The application is never decided, the owner is owed nothing under s. 13 and has no objection or review under Part 4 Division 5, and remains in breach of s. 5(1). OPEN, medium." },
      { id: "e18", ref: "E-18", foundBy: "ENC", sev: "stop", label: "If the council gives no s. 13 notice, the owner loses the right of review",
        cite: "ss. 13, 69(1), 71(1)", what: "A local government refuses registration and gives no notice.",
        why: "Section 13 has no penalty, and objection and review are open only to 'a person who has been given notice under section 13'. The council's default removes the owner's remedy. OPEN, medium." },
      { id: "r20", ref: "R-20", foundBy: "ENC", sev: "stop", label: "If no database company has agreed, s. 15 has nobody to notify",
        cite: "s. 15; s. 3(1) 'microchip database company' (b)", what: "An implanter chips a cat without arranging a database.",
        why: "The implanter must notify 'the microchip database company for that cat', which exists only once a company keeps or has agreed to keep the records. Until then the duty has no addressee and the implanter commits no offence. OPEN, medium." },
      { id: "u06", ref: "U-06", foundBy: "ENC", sev: "warn", label: "'The person' in s. 5(2)(a): has a parent or business owner kept the cat?",
        cite: "s. 5(2)(a); s. 4(1)(b), (c); FORK-03", what: "A cat is kept by a child, or by a business.",
        why: "Section 5(2)(a) introduces no person, and an owner through someone else's keeping has kept nothing. Reading A (taken) attributes the keeping; reading B exempts such owners for ever. OPEN, low-medium." },
      { id: "u27", ref: "U-27", foundBy: "ENC", sev: "warn", label: "On a reclaim from the pound, who is the 'seller'?",
        cite: "s. 3(1) 'transfer' (b); ss. 22-24; FORK-14", what: "An owner reclaims an impounded cat.",
        why: "Reading A (taken) makes the pound's operator the seller, liable under s. 23 and owing a s. 24 notice of the owner's name; reading B makes the owner the seller with no purchaser. OPEN, low-medium." },
      { id: "r24", ref: "R-24", foundBy: "ENC", sev: "stop", label: "s. 19 does not reach a false sterilisation certificate",
        cite: "s. 19; r. 18(1)", what: "A false certificate of sterilisation is given for an entire cat.",
        why: "The prescribed manner is a certificate 'given ... under section 21', which a false one never is, so s. 19 catches only the ear tattoo. OPEN, low-medium." },
      { id: "r29", ref: "R-29", foundBy: "RD", sev: "warn", label: "r. 19's reference to r. 9 now exempts transfers to vets and approved facilities",
        cite: "r. 19; r. 9(2)(d), (e); s. 23(3)", what: "An unchipped or entire cat is given to a vet clinic or an approved private facility.",
        why: "Regulation 19 exempts transfers to 'an organisation or person set out in regulation 9'. Since 2018 r. 9 sets out facilities and premises as well, so s. 23 no longer applies to transfers to them, by a change nobody appears to have made on purpose. OPEN, low-medium." },
      { id: "d31", ref: "D-31", foundBy: "TST", sev: "warn", label: "An offer for sale is a 'transfer', so s. 24 demands notice of a purchaser who does not exist",
        cite: "s. 3(1) 'transfer' (a); s. 24", what: "A registered or chipped cat is advertised for sale.",
        why: "The seller must name 'the purchaser' within 7 days of the offer; there is none. A repair was enacted in 2021 (SPF Act s. 50(4)) and has not commenced. OPEN, low-medium." },
      { id: "u34", ref: "U-34", foundBy: "ENC", sev: "warn", label: "Is a cat growing older a 'change' the owner must notify?",
        cite: "s. 25(b); r. 17(m); FORK-15", what: "A microchipped cat has a birthday.",
        why: "'The age' is information prescribed under s. 15. Read literally, s. 25(b) requires notice within 7 days of every change of age. Reading A (taken) fixes the age at implanting. OPEN, low-medium." },
      { id: "t35", ref: "T-35", foundBy: "ENC", sev: "stop", label: "s. 25's 7 days run from a change the owner may never learn of",
        cite: "s. 25; r. 17(c)-(e); r. 16(g)", what: "The implanter's contact details change, unknown to the owner.",
        why: "The owner must notify 'within 7 days after the change', and some prescribed items are about other people. A repair (SPF Act s. 55: 'becomes aware') was enacted in 2021 and has not commenced. OPEN, low-medium." },
      { id: "u38", ref: "U-38", foundBy: "ENC", sev: "warn", label: "A '3-year' registration can last two years and a day",
        cite: "r. 12(2)(a)(ii); FORK-06", what: "A 3-year registration is granted on or near 31 October.",
        why: "'31 October in the final year of that period' gives two years and a day on reading A (taken), more than three years on B, a date outside the period on C. OPEN, low-medium." },
      { id: "w21", ref: "W-21", foundBy: "ENC", sev: "warn", label: "The company must keep information it was never given",
        cite: "s. 16; s. 15", what: "An implanter does not notify the company.",
        why: "Section 16 requires the company for the cat to keep 'the information prescribed under section 15', whether or not it was given. A repair (SPF Act s. 53) was enacted in 2021 and has not commenced. OPEN, low-medium." },
      { id: "u13", ref: "U-13", foundBy: "ENC", sev: "warn", label: "'Within the previous 3 years' -- of the application or the decision?",
        cite: "s. 9(2)(e); FORK-11", what: "An applicant has an old conviction near the 3-year line.",
        why: "Counted from the decision (reading A, taken) or from the application (B), the result can turn on how fast the local government decides. OPEN, low." },
      { id: "r17", ref: "R-17", foundBy: "RD", sev: "warn", label: "s. 13: notice goes to 'the owner', and 'the person's rights' has no antecedent",
        cite: "s. 13(1)", what: "A refusal where the applicant is not the only owner (a child and parent).",
        why: "Section 13(1)(c) speaks of 'the person's rights' after naming only 'the owner'; s. 40, its twin, says 'the person affected'. Which owner is owed the notice, and so the review rights, is not said. OPEN, low." },
      { id: "u19", ref: "U-19", foundBy: "ENC", sev: "warn", label: "Does a certificate given before 6 months start to apply at 6 months?",
        cite: "ss. 14(2), (3), 18(2)(a), (3); FORK-13", what: "A veterinarian certifies a kitten under 6 months.",
        why: "Reading A (taken): yes. Reading B: never, and the owner is in breach at 6 months without a fresh certificate. OPEN, low." },
      { id: "u30", ref: "U-30", foundBy: "ENC", sev: "warn", label: "Are the SAFE groups 'set out in regulation 9' for r. 19?",
        cite: "r. 19; r. 9(1), (3)(b); FORK-08", what: "A cat is given to a SAFE rescue group.",
        why: "Regulation 9 names SAFE entities only as placers of foster care. Reading A (taken) exempts transfers to them from s. 23; reading B does not. OPEN, low." },
      { id: "l33", ref: "L-33", foundBy: "ENC", sev: "warn", label: "ss. 24 and 25 both require the seller to report the same change",
        cite: "ss. 24, 25; rr. 16(a), 17(g)", what: "A registered cat is sold.",
        why: "The seller, still the registered owner (D-01), owes s. 24 and s. 25 notices of the same change on the same clock: two offences for one omission. OPEN, low." },
      { id: "t39", ref: "T-39", foundBy: "ENC", sev: "warn", label: "Renewal outside the 21 days, and an application after expiry",
        cite: "r. 12(2)(b); Sch. 3 item 1", what: "A renewal is sought outside 11-31 October, or after the registration has lapsed.",
        why: "Regulation 12(2)(b) allows renewal within 21 days before 1 November and says nothing of other times, or whether a late application is a renewal or a grant (which changes the fee). OPEN, low." },
      { id: "t46", ref: "T-46", foundBy: "CMP", sev: "warn", label: "A one-year registration granted in late October lasts days",
        cite: "r. 12(2)(a)(i); Sch. 3 item 1(a)", what: "A one-year registration is granted in October.",
        why: "Every one-year registration ends on the next 31 October; one granted on 25 October lasts six days and must be renewed at once. OPEN, low." },
      { id: "r36", ref: "R-36", foundBy: "RD", sev: "warn", label: "'Has effect from the period specified in the registration certificate'",
        cite: "r. 12(2)(a); r. 14, Form 2", what: "A registration is granted.",
        why: "A registration takes effect from a day, and the prescribed certificate specifies only its expiry date. OPEN, low." },
      { id: "d41", ref: "D-41", foundBy: "ENC", sev: "warn", label: "The pensioner rate turns on 'the owner', who may be several people",
        cite: "Sch. 3 cl. 1(3)", what: "A pensioner applies, or a cat has owners of whom only some are pensioners.",
        why: "The fee is halved 'if the owner of a cat is a pensioner'; with several owners the clause does not say whose status counts. OPEN, low." },
      { id: "u44", ref: "U-44", foundBy: "ENC", sev: "warn", label: "Does IA s. 71(2) make a continuing failure to 'ensure' a daily offence?",
        cite: "ss. 5(1), 14(1), 18(1); IA s. 71(2); FORK-12", what: "An owner is in breach of s. 5(1), 14(1) or 18(1).",
        why: "Section 71(2) reaches 'an act or thing ... required ... to be done'; whether a duty to ensure a state of affairs is one decides whether each day after conviction is a further $50 offence. OPEN, low." },
      { id: "x47", ref: "X-47", foundBy: "CMP", sev: "warn", label: "The EM says s. 7 deals with forged tags; its words do not",
        cite: "ss. 3(1), 7; EM Cat Bill 2011 cl. 7", what: "A home-made tag is put on an unregistered cat.",
        why: "Section 7 protects only 'a registration tag worn by a cat', which is the tag a council issued. OPEN, low." },
      { id: "x51", ref: "X-51", foundBy: "CMP", sev: "warn", label: "Form 1 Part G says the council 'may refuse'; the Act says 'refuse to consider'",
        cite: "s. 9(6); Sch. 1 Form 1 Part G", what: "A council refuses to consider an application.",
        why: "A refusal carries s. 13 notice and review; a refusal to consider carries neither. The prescribed form tells applicants the former. OPEN, low." },

      /* verified sound */
      { id: "d02", ref: "D-02", foundBy: "ENC", sev: "ok", label: "The s. 4(2) presumption gives no start day for s. 5(2)(a)",
        cite: "ss. 4(2), 5(2)(a)", what: "An unregistered cat is recorded in a microchip database.",
        why: "The presumption operates only 'in the absence of evidence to the contrary'; evidence of when keeping began answers s. 5(2)(a). VERIFIED-NO-DEFECT." },
      { id: "u03", ref: "U-03", foundBy: "ENC", sev: "ok", label: "The day a cat reaches 6 months",
        cite: "ss. 5(1), 14(1), 18(1); IA s. 62; FORK-01", what: "A cat reaches 6 months.",
        why: "Reckoned in calendar months by IA s. 62, which the reading taken follows. VERIFIED-NO-DEFECT." },
      { id: "u04", ref: "U-04", foundBy: "ENC", sev: "ok", label: "A child keeper and her parent are both owners",
        cite: "s. 4(1); FORK-02", what: "A child keeps a cat.",
        why: "'Any of these persons': the parent is added, not substituted. VERIFIED-NO-DEFECT." },
      { id: "u07", ref: "U-07", foundBy: "ENC", sev: "ok", label: "Counting the 14 days in s. 5(2)",
        cite: "s. 5(2)(a), (b); IA s. 61(1)(b), (g); FORK-04", what: "The 14th day after a cat is taken in.",
        why: "IA s. 61 excludes the first day. VERIFIED-NO-DEFECT." },
      { id: "u08", ref: "U-08", foundBy: "ENC", sev: "ok", label: "A person never resident in the State and s. 5(2)(b)",
        cite: "s. 5(2)(b); IA s. 18; FORK-09", what: "A non-resident keeps a cat in WA.",
        why: "The purposive reading (IA s. 18) treats the paragraph as grace for newcomers. VERIFIED-NO-DEFECT." },
      { id: "l11", ref: "L-11", foundBy: "TST", sev: "ok", label: "An entire kitten under 6 months must be refused registration",
        cite: "ss. 9(2)(d), (4), 18(3); s. 5(1)", what: "An owner applies early for an unsterilised kitten.",
        why: "No duty to register arises until 6 months. VERIFIED-NO-DEFECT." },
      { id: "u12", ref: "U-12", foundBy: "ENC", sev: "ok", label: "'2 or more offences against any of' three Acts are counted together",
        cite: "s. 9(2)(e), s. 10(b); FORK-10", what: "An applicant has one Dog Act and one Animal Welfare Act conviction.",
        why: "The Council's 2011 amendment replaced 'an offence against' any of the Acts with '2 or more offences against any of the following'. VERIFIED-NO-DEFECT." },
      { id: "p14", ref: "P-14", foundBy: "ENC", sev: "ok", label: "A requirement allowing more than 21 days",
        cite: "s. 9(5), (6)", what: "A council allows more than 21 days for information.",
        why: "The limit is express; such a requirement is not one under s. 9(5). VERIFIED-NO-DEFECT." },
      { id: "l16", ref: "L-16", foundBy: "ENC", sev: "ok", label: "'If, and only if', and an application without the fee",
        cite: "ss. 8(2), 9(1), (2)", what: "An application is made without the fee.",
        why: "Section 9 operates only on an application under s. 8, made as s. 8(2) requires. VERIFIED-NO-DEFECT." },
      { id: "t23", ref: "T-23", foundBy: "ENC", sev: "ok", label: "s. 21 fixes no time for the sterilisation certificate",
        cite: "s. 21; IA s. 63", what: "A veterinarian sterilises a cat.",
        why: "IA s. 63: with all convenient speed. VERIFIED-NO-DEFECT." },
      { id: "d25", ref: "D-25", foundBy: "ENC", sev: "ok", label: "s. 18(2)(b) where a cat has several owners",
        cite: "s. 18(2)(b)", what: "An approved breeder's breeding queen reaches 6 months entire.",
        why: "'A cat is exempt': the exemption attaches to the cat, for every owner. VERIFIED-NO-DEFECT." },
      { id: "l26", ref: "L-26", foundBy: "CMP", sev: "ok", label: "No class of cats is prescribed as exempt from sterilisation",
        cite: "ss. 18(2)(c), 23(2)(a)(iii), 76(1)", what: "An entire cat is transferred.",
        why: "The Act permits a class to be prescribed and does not require one. VERIFIED-NO-DEFECT." },
      { id: "l28", ref: "L-28", foundBy: "ENC", sev: "ok", label: "An unchipped kitten under 6 months cannot lawfully be transferred",
        cite: "ss. 14(3), 23(1)", what: "An unchipped kitten changes hands.",
        why: "The Cat Bill 2011's stated scheme: every cat microchipped before transfer. VERIFIED-NO-DEFECT." },
      { id: "r32", ref: "R-32", foundBy: "ENC", sev: "ok", label: "s. 24 for a cat neither registered nor recorded",
        cite: "s. 24(a), (b)", what: "An unregistered, unrecorded cat changes hands.",
        why: "Each paragraph names its addressee by the registration or record; with neither there is nothing to notify. VERIFIED-NO-DEFECT." },
      { id: "u37", ref: "U-37", foundBy: "ENC", sev: "ok", label: "'The next 31 October' for a registration taking effect on 31 October",
        cite: "r. 12(1)(a), (2)(a)(i); FORK-05", what: "A one-year registration is granted on 31 October.",
        why: "Registration is for 'one year' (r. 12(1)(a)). VERIFIED-NO-DEFECT." },
      { id: "u40", ref: "U-40", foundBy: "ENC", sev: "ok", label: "The $10 fee 'after 31 May'",
        cite: "Sch. 3 item 1(a); FORK-07", what: "A one-year registration is granted in November or December.",
        why: "The words tie 31 May to 'registration until the next 31 October'. VERIFIED-NO-DEFECT." },
      { id: "t42", ref: "T-42", foundBy: "ENC", sev: "ok", label: "Foster care for 'a total of 12 weeks'",
        cite: "r. 9(3)(b)", what: "A SAFE foster placement passes 12 weeks.",
        why: "The total is of the cat's time in foster care. VERIFIED-NO-DEFECT." },
      { id: "p43", ref: "P-43", foundBy: "RD", sev: "ok", label: "r. 10 exempts an owner where s. 6(2) speaks of a class of cats",
        cite: "s. 6(2); r. 10", what: "A registered cat is exhibited untagged.",
        why: "The exemption is defined entirely by the class of cats being exhibited. VERIFIED-NO-DEFECT." },
      { id: "t45", ref: "T-45", foundBy: "ENC", sev: "ok", label: "ss. 14(2)-(3), 18(2)-(3) commenced a year before the duties",
        cite: "s. 2(b), (c); s. 9(3), (4)", what: "A veterinary exemption certificate is given.",
        why: "Section 9(3)-(4), in operation from 1 November 2012, needed the exemptions then. VERIFIED-NO-DEFECT." },
      { id: "x48", ref: "X-48", foundBy: "CMP", sev: "ok", label: "The EM describes refusal for a single conviction",
        cite: "s. 9(2)(e); EM Cat Bill 2011 cl. 9; LC SNP 197-2", what: "An applicant has convictions.",
        why: "The EM describes the Bill as introduced; the Council amended the clause. VERIFIED-NO-DEFECT." },
      { id: "x49", ref: "X-49", foundBy: "CMP", sev: "ok", label: "The EM limits the sterilisation voucher to young cats; s. 23(2)(b) does not",
        cite: "s. 23(2)(b); EM Cat Bill 2011 cl. 23; IA s. 19", what: "An adult cat is transferred entire with a voucher.",
        why: "The words are clear; extrinsic material cannot displace them. VERIFIED-NO-DEFECT." },
      { id: "x50", ref: "X-50", foundBy: "CMP", sev: "ok", label: "The EM says s. 8 'requires' an application; s. 8 permits one",
        cite: "ss. 5(1), 8(1); EM Cat Bill 2011 cl. 8", what: "An owner applies to register a cat.",
        why: "The duty the EM describes is s. 5(1)'s. VERIFIED-NO-DEFECT." },

      /* form: static */
      { id: "f52", ref: "F-52", foundBy: "RD", sev: "warn", static: true, label: "r. 12(1): 'may be for — ... (b) for the life of the cat'",
        cite: "r. 12(1)", what: "Read for form.", why: "The chapeau's 'for' is repeated in paragraph (b). OPEN, low." },
      { id: "f53", ref: "F-53", foundBy: "RD", sev: "warn", static: true, label: "r. 4: 'each of the following bodies are prescribed'",
        cite: "r. 4", what: "Read for form.", why: "'Each ... are'; r. 6 has 'each ... is'. OPEN, low." },
      { id: "f54", ref: "F-54", foundBy: "RD", sev: "warn", static: true, label: "Form 1 labels dates of birth 'Age (dd/mm/yy)'",
        cite: "Sch. 1 Form 1 Parts A, B", what: "Read for form.",
        why: "The fields ask for a date, labelled as an age, with a two-digit year; r. 16(d) records the owner's 'date of birth'. OPEN, low." }
    ],

    scenarios: [
      /* neutral demonstrations of the encoding's reading */
      { label: "Tom reaches 6 months unchipped, entire and unregistered", focus: "c1", steps: [ { tick: 125 } ] },
      { label: "Ana applies to register Tom as he is; the council must refuse", focus: "c1", steps: [
        { actor: "p1", action: "apply", target: "c1" },
        { actor: "lg1", action: "decide", target: "c1" }
      ] },
      { label: "Dr Vu chips and desexes Tom; Ana applies; the council registers him", focus: "c1", steps: [
        { tick: 130 },
        { actor: "v1", action: "implant", target: "c1" },
        { actor: "v1", action: "notifyImplant", target: "c1" },
        { actor: "v1", action: "sterilise", target: "c1" },
        { actor: "v1", action: "notifySterilisation", target: "c1" },
        { actor: "v1", action: "giveCertificate", target: "c1" },
        { actor: "p1", action: "apply", target: "c1" },
        { actor: "lg1", action: "decide", target: "c1" }
      ] },
      { label: "Ben takes Tess over from Ana and nobody tells anyone", focus: "c2", steps: [
        { actor: "p2", action: "acquire", target: "c2" },
        { tick: 10 }
      ] },
      { label: "Tess's registration runs out on 31 October", focus: "c2", steps: [ { tick: 305 } ] },

      /* the findings */
      { label: "Ben buys Tess, then applies to register her in his own name", focus: "c2",
        description: "D-01, L-33: the seller stays the owner; the buyer may not apply.", steps: [
        { actor: "p2", action: "acquire", target: "c2" },
        { tick: 3 },
        { actor: "p2", action: "apply", target: "c2" }
      ] },
      { label: "Lulu, chipped and desexed by a Melbourne vet, comes to Perth", focus: "@lulu",
        description: "D-05, D-22: neither the chip nor the desexing counts in WA.", steps: [
        { spawn: "cat", as: "lulu", label: "Lulu", note: "came from Melbourne",
          attrs: { bornDate: "2022-06-01", keptSinceDay: -30, breeding: false, chipped: false, sterilised: false, chipCert: false, sterCert: false, registered: false, wearingTag: false, earTattoo: false },
          rels: { keptIn: "lg1", keeper: "p1" } },
        { actor: "p4", action: "implant", target: "@lulu" },
        { actor: "p4", action: "sterilise", target: "@lulu" },
        { tick: 1 },
        { actor: "p1", action: "apply", target: "@lulu" },
        { actor: "lg1", action: "decide", target: "@lulu" }
      ] },
      { label: "Ana moves with Tess to Kalamunda and notifies both councils", focus: "c2",
        description: "L-09.", steps: [
        { actor: "p1", action: "moveDistrict", target: "c2" },
        { actor: "p1", action: "notifyMove", target: "c2" },
        { tick: 2 }
      ] },
      { label: "Tess is at the vet when her renewal is decided", focus: "c2",
        description: "D-10.", steps: [
        { tick: 290 },
        { actor: "p1", action: "leaveAtVet", target: "c2" },
        { actor: "p1", action: "apply", target: "c2" },
        { actor: "lg1", action: "decide", target: "c2" }
      ] },
      { label: "The council refuses to consider Ana's application for Tom", focus: "c1",
        description: "P-15, X-51.", steps: [
        { tick: 130 },
        { actor: "p1", action: "apply", target: "c1" },
        { actor: "lg1", action: "requireInfo", target: "c1" },
        { tick: 22 },
        { actor: "lg1", action: "refuseToConsider", target: "c1" },
        { tick: 3 }
      ] },
      { label: "The council refuses Tom and gives no notice", focus: "c1",
        description: "E-18.", steps: [
        { actor: "p1", action: "apply", target: "c1" },
        { actor: "lg1", action: "decide", target: "c1" },
        { tick: 8 },
        { actor: "lg1", action: "letNoticeLapse", target: "c1" }
      ] },
      { label: "Dr Vu chips Tom but arranges no database", focus: "c1",
        description: "R-20.", steps: [
        { actor: "v1", action: "implant", target: "c1", params: { noDatabase: true } }
      ] },
      { label: "Dr Vu chips Tom and never tells the database company", focus: "c1",
        description: "W-21.", steps: [
        { actor: "v1", action: "implant", target: "c1" },
        { tick: 9 }
      ] },
      { label: "Kit, a child, takes in Mo and applies to register him", focus: "@mo",
        description: "U-04, R-17, U-06.", steps: [
        { spawn: "cat", as: "mo", label: "Mo", note: "kept by Kit",
          attrs: { bornDate: "2021-06-01", keptSinceDay: 0, breeding: false, chipped: true, sterilised: true, sterilisedByVet: true, chipCert: false, sterCert: false, registered: false, wearingTag: false, earTattoo: false },
          rels: { keptIn: "lg1", keeper: "p3" } },
        { actor: "p3", action: "apply", target: "@mo" },
        { actor: "lg1", action: "decide", target: "@mo" },
        { tick: 15 }
      ] },
      { label: "Ben sells Tom with a false certificate of sterilisation", focus: "c1",
        description: "R-24.", steps: [
        { actor: "p2", action: "giveFalseCertificate", target: "c1" }
      ] },
      { label: "The council impounds Tom; Ana reclaims him unchipped", focus: "c1",
        description: "U-27.", steps: [
        { actor: "lg1", action: "impound", target: "c1" },
        { actor: "p1", action: "reclaim", target: "c1" }
      ] },
      { label: "Ana gives unchipped Tom up to her vet clinic", focus: "c1",
        description: "R-29.", steps: [
        { actor: "p1", action: "surrenderToVet", target: "c1" }
      ] },
      { label: "Ana gives Tom to a SAFE rescue group", focus: "c1",
        description: "U-30.", steps: [
        { actor: "p1", action: "giveToSafe", target: "c1" }
      ] },
      { label: "Ana advertises Tess for sale", focus: "c2",
        description: "D-31.", steps: [
        { actor: "p1", action: "offerForSale", target: "c2" }
      ] },
      { label: "Chipped Tom turns one", focus: "c1",
        description: "U-34.", steps: [
        { actor: "v1", action: "implant", target: "c1" },
        { actor: "v1", action: "notifyImplant", target: "c1" },
        { tick: 305 }
      ] },
      { label: "Dr Vu's practice changes its phone number and nobody tells Ana", focus: "c2",
        description: "T-35.", steps: [
        { actor: "v1", action: "changePracticeDetails", target: "c2" },
        { tick: 9 }
      ] },
      { label: "A 3-year registration granted on 31 October", focus: "@max",
        description: "U-38.", steps: [
        { spawn: "cat", as: "max", label: "Max", attrs: { bornDate: "2020-06-01", keptSinceDay: -100, breeding: false, chipped: true, sterilised: true, sterilisedByVet: true, chipCert: false, sterCert: false, registered: false, wearingTag: false, earTattoo: false }, rels: { keptIn: "lg1", keeper: "p1" } },
        { tick: 303 },
        { actor: "p1", action: "apply", target: "@max", params: { threeYears: true } },
        { actor: "lg1", action: "decide", target: "@max" }
      ] },
      { label: "A one-year registration granted on 31 October", focus: "@max",
        description: "U-37.", steps: [
        { spawn: "cat", as: "max", label: "Max", attrs: { bornDate: "2020-06-01", keptSinceDay: -100, breeding: false, chipped: true, sterilised: true, sterilisedByVet: true, chipCert: false, sterCert: false, registered: false, wearingTag: false, earTattoo: false }, rels: { keptIn: "lg1", keeper: "p1" } },
        { tick: 303 },
        { actor: "p1", action: "apply", target: "@max" },
        { actor: "lg1", action: "decide", target: "@max" }
      ] },
      { label: "A one-year registration granted on 25 October", focus: "@max",
        description: "T-46, R-36.", steps: [
        { spawn: "cat", as: "max", label: "Max", attrs: { bornDate: "2020-06-01", keptSinceDay: -100, breeding: false, chipped: true, sterilised: true, sterilisedByVet: true, chipCert: false, sterCert: false, registered: false, wearingTag: false, earTattoo: false }, rels: { keptIn: "lg1", keeper: "p1" } },
        { tick: 297 },
        { actor: "p1", action: "apply", target: "@max" },
        { actor: "lg1", action: "decide", target: "@max" }
      ] },
      { label: "A one-year registration granted in November", focus: "@max",
        description: "U-40.", steps: [
        { spawn: "cat", as: "max", label: "Max", attrs: { bornDate: "2020-06-01", keptSinceDay: -100, breeding: false, chipped: true, sterilised: true, sterilisedByVet: true, chipCert: false, sterCert: false, registered: false, wearingTag: false, earTattoo: false }, rels: { keptIn: "lg1", keeper: "p1" } },
        { tick: 320 },
        { actor: "p1", action: "apply", target: "@max" },
        { actor: "lg1", action: "decide", target: "@max" }
      ] },
      { label: "Ana renews Tess in July, and again after she lapses", focus: "c2",
        description: "T-39.", steps: [
        { tick: 190 },
        { actor: "p1", action: "apply", target: "c2" },
        { tick: 125 },
        { actor: "p1", action: "apply", target: "c2" }
      ] },
      { label: "Ben, with two recent convictions, applies to register his cat", focus: "@bo",
        description: "U-12, U-13, X-48.", steps: [
        { set: "p2", attrs: { convictions2in3: true } },
        { spawn: "cat", as: "bo", label: "Bo", attrs: { bornDate: "2020-06-01", keptSinceDay: -100, breeding: false, chipped: true, sterilised: true, sterilisedByVet: true, chipCert: false, sterCert: false, registered: false, wearingTag: false, earTattoo: false }, rels: { keptIn: "lg1", keeper: "p2" } },
        { actor: "p2", action: "apply", target: "@bo" },
        { actor: "lg1", action: "decide", target: "@bo" }
      ] },
      { label: "Pat, a pensioner, registers his cat", focus: "@puss",
        description: "D-41.", steps: [
        { spawn: "cat", as: "puss", label: "Puss", attrs: { bornDate: "2020-06-01", keptSinceDay: -100, breeding: false, chipped: true, sterilised: true, sterilisedByVet: true, chipCert: false, sterCert: false, registered: false, wearingTag: false, earTattoo: false }, rels: { keptIn: "lg1", keeper: "p7" } },
        { actor: "p7", action: "apply", target: "@puss" },
        { actor: "lg1", action: "decide", target: "@puss" }
      ] },
      { label: "Ana applies for Max without paying the fee", focus: "@max",
        description: "L-16.", steps: [
        { spawn: "cat", as: "max", label: "Max", attrs: { bornDate: "2020-06-01", keptSinceDay: -100, breeding: false, chipped: true, sterilised: true, sterilisedByVet: true, chipCert: false, sterCert: false, registered: false, wearingTag: false, earTattoo: false }, rels: { keptIn: "lg1", keeper: "p1" } },
        { actor: "p1", action: "apply", target: "@max", params: { noFee: true } }
      ] },
      { label: "The council allows 30 days to answer", focus: "c1",
        description: "P-14.", steps: [
        { actor: "p1", action: "apply", target: "c1" },
        { actor: "lg1", action: "requireInfo", target: "c1", params: { over21: true } }
      ] },
      { label: "Ana takes in Max; the 14-day grace ends", focus: "@max",
        description: "U-07, U-44.", steps: [
        { spawn: "cat", as: "max", label: "Max", attrs: { bornDate: "2020-06-01", keptSinceDay: 0, breeding: false, chipped: true, sterilised: true, sterilisedByVet: true, chipCert: false, sterCert: false, registered: false, wearingTag: false, earTattoo: false }, rels: { keptIn: "lg1", keeper: "p1" } },
        { tick: 15 }
      ] },
      { label: "Vic, who lives in Darwin, keeps Vito in Perth", focus: "@vito",
        description: "U-08.", steps: [
        { spawn: "cat", as: "vito", label: "Vito", attrs: { bornDate: "2020-06-01", keptSinceDay: -100, breeding: false, chipped: true, sterilised: true, sterilisedByVet: true, chipCert: false, sterCert: false, registered: false, wearingTag: false, earTattoo: false }, rels: { keptIn: "lg1", keeper: "p6" } },
        { tick: 1 }
      ] },
      { label: "Bree's breeding queen reaches 6 months entire", focus: "@queen",
        description: "D-25.", steps: [
        { spawn: "cat", as: "queen", label: "Queen", attrs: { bornDate: "2025-07-10", keptSinceDay: -150, breeding: true, chipped: true, sterilised: false, chipCert: false, sterCert: false, registered: false, wearingTag: false, earTattoo: false }, rels: { keptIn: "lg1", keeper: "p5" } },
        { tick: 15 }
      ] },
      { label: "A SAFE group places a stray in foster care for 13 weeks", focus: "@stray",
        description: "T-42.", steps: [
        { spawn: "cat", as: "stray", label: "Stray", attrs: { bornDate: "2024-01-01", breeding: false, chipped: false, sterilised: false, chipCert: false, sterCert: false, registered: false, wearingTag: false, earTattoo: false }, rels: { keptIn: "lg1" } },
        { actor: "p2", action: "placeInFoster", target: "@stray" },
        { tick: 86 }
      ] },
      { label: "Dr Vu certifies that chipping may harm 2-month-old Tom", focus: "c1",
        description: "U-19, T-45.", steps: [
        { actor: "v1", action: "certifyChip", target: "c1" }
      ] },
      { label: "Tess is exhibited untagged at a Cats United show", focus: "c2",
        description: "P-43.", steps: [
        { actor: "c2", action: "loseTag" },
        { actor: "c2", action: "goOut", params: { exhibited: true } }
      ] },
      { label: "Ben puts a home-made tag on unregistered Tom", focus: "c1",
        description: "X-47.", steps: [
        { actor: "p2", action: "fakeTag", target: "c1" }
      ] },
      { label: "Ana sells adult Max entire, with a sterilisation voucher", focus: "@max",
        description: "X-49.", steps: [
        { spawn: "cat", as: "max", label: "Max", attrs: { bornDate: "2020-06-01", keptSinceDay: -100, breeding: false, chipped: true, sterilised: false, chipCert: false, sterCert: false, registered: false, wearingTag: false, earTattoo: false }, rels: { keptIn: "lg1", keeper: "p1", company: "co1" } },
        { actor: "p2", action: "acquire", target: "@max", params: { voucher: true } }
      ] },
      { label: "Ana sells Tom unchipped and entire, with no voucher", focus: "c1",
        description: "L-26, L-28, R-32.", steps: [
        { actor: "p2", action: "acquire", target: "c1" }
      ] }
    ],

    simulation: {
      params: [
        { key: "residents", label: "People at the start", def: 20, min: 1, max: 80, step: 1 },
        { key: "startCats", label: "Cats at the start", def: 15, min: 0, max: 200, step: 1 },
        { key: "maxCats", label: "Most cats alive at once", def: 120, min: 1, max: 600, step: 1 },
        { key: "catsPerMonth", label: "Kittens born per month", def: 3, min: 0, max: 40, step: 0.5 },
        { key: "pChip", label: "Unchipped cats over 2 months chipped per month", unit: "%", def: 30, min: 0, max: 100, step: 1 },
        { key: "pSterilise", label: "Entire cats over 4 months sterilised per month", unit: "%", def: 25, min: 0, max: 100, step: 1 },
        { key: "pApply", label: "Unregistered cats over 5 months whose owner applies, per month", unit: "%", def: 20, min: 0, max: 100, step: 1 },
        { key: "pNotify", label: "Notices given, of those due, per week", unit: "%", def: 85, min: 0, max: 100, step: 1 },
        { key: "pTransfer", label: "Cats changing hands per month", unit: "%", def: 2, min: 0, max: 50, step: 0.5 },
        { key: "pPurchaserApplies", label: "Buyers of registered cats who try to register them, per month", unit: "%", def: 50, min: 0, max: 100, step: 1 }
      ],
      generators: [
        { id: "residents", start: "$param.residents",
          spawn: { type: "person", label: "{name}", names: ["Ada", "Bo", "Cleo", "Dev", "Eve", "Finn", "Gia", "Hal", "Isla", "Jai", "Kai", "Lou"],
                   attrs: { bornDay: ["-", "$day", ["randInt", 6600, 25000]], vet: false, microchipImplanter: false, approvedBreeder: false, convictions2in3: false, resident: true } } },
        { id: "vets", start: 2,
          spawn: { type: "person", label: "Dr {name}", names: ["Ito", "Moss"],
                   attrs: { bornDay: ["-", "$day", ["randInt", 10000, 20000]], vet: true, microchipImplanter: true, approvedBreeder: false, convictions2in3: false } } },
        { id: "adult-cats", start: "$param.startCats",
          spawn: { type: "cat", label: "{name}", names: ["Luna", "Milo", "Bella", "Oscar", "Coco", "Simba", "Nala", "Leo"],
                   attrs: { bornDay: ["-", "$day", ["randInt", 200, 3000]], keptSinceDay: ["-", "$day", ["randInt", 20, 1000]], breeding: false,
                            chipped: false, sterilised: false, chipCert: false, sterCert: false, registered: false, wearingTag: false, earTattoo: false },
                   rels: { keeper: ["any", "person", "$it.attrs.resident"], keptIn: ["any", "localgov"] } } },
        { id: "births", rate: ["/", "$param.catsPerMonth", 30], when: ["<", ["count", "cat"], "$param.maxCats"],
          spawn: { type: "cat", label: "{name}", names: ["Pip", "Mochi", "Kiwi", "Dot", "Fudge", "Taco", "Socks", "Ziggy"],
                   attrs: { bornDay: "$day", keptSinceDay: "$day", breeding: false,
                            chipped: false, sterilised: false, chipCert: false, sterCert: false, registered: false, wearingTag: false, earTattoo: false },
                   rels: { keeper: ["any", "person", "$it.attrs.resident"], keptIn: ["any", "localgov"] } } },
        { id: "chip", per: "cat", when: ["and", ["not", "$self.attrs.chipped"], [">=", ["ageMonths", "$self.attrs.bornDay"], 2]],
          chance: ["/", "$param.pChip", 3000],
          act: { action: "implant", actor: ["any", "person", "$it.attrs.microchipImplanter"], target: "$self" } },
        { id: "notify-chip", per: "cat", when: ["and", "$self.attrs.chipped", ["not", "$self.attrs.s15Notified"], ["exists", "$self.rels.implanter"]],
          chance: ["/", "$param.pNotify", 700],
          act: { action: "notifyImplant", actor: ["rel", "$self", "implanter"], target: "$self" } },
        { id: "desex", per: "cat", when: ["and", ["not", "$self.attrs.sterilised"], [">=", ["ageMonths", "$self.attrs.bornDay"], 4]],
          chance: ["/", "$param.pSterilise", 3000],
          act: { action: "sterilise", actor: ["any", "person", "$it.attrs.vet"], target: "$self" } },
        { id: "notify-desex", per: "cat", when: ["and", "$self.attrs.s20Applies", ["not", "$self.attrs.s20Notified"]],
          chance: ["/", "$param.pNotify", 700],
          act: { action: "notifySterilisation", actor: ["rel", "$self", "sterilisedBy"], target: "$self" } },
        { id: "certificate", per: "cat", when: ["and", "$self.attrs.sterilisedByVet", ["not", "$self.attrs.s21Given"]],
          chance: 0.5,
          act: { action: "giveCertificate", actor: ["rel", "$self", "sterilisedBy"], target: "$self" } },
        { id: "apply", per: "cat", when: ["and", ["not", "$self.attrs.registered"], ["not", "$self.attrs.applied"], [">=", ["ageMonths", "$self.attrs.bornDay"], 5], ["exists", "$self.rels.keeper"]],
          chance: ["/", "$param.pApply", 3000],
          act: { action: "apply", actor: ["rel", "$self", "keeper"], target: "$self" } },
        { id: "purchaser-applies", per: "cat",
          when: ["and", "$self.attrs.registered", ["exists", "$self.rels.keeper"], ["not", ["=", "$self.rels.keeper", "$self.rels.registeredOwner"]], ["not", "$self.attrs.purchaserTried"]],
          chance: ["/", "$param.pPurchaserApplies", 3000],
          act: { action: "apply", actor: ["rel", "$self", "keeper"], target: "$self" } },
        { id: "decide", per: "cat", when: "$self.attrs.applied", chance: 0.3,
          act: { action: "decide", actor: ["rel", "$self", "keptIn"], target: "$self" } },
        { id: "transfer", per: "cat", when: ["exists", "$self.rels.keeper"], chance: ["/", "$param.pTransfer", 3000],
          act: { action: "acquire", actor: ["any", "person", ["and", "$it.attrs.resident", ["!=", "$it.id", "$self.rels.keeper"]]], target: "$self",
                 params: { voucher: ["chance", 0.3] } } },
        { id: "notify-transfer", per: "cat", when: ["and", "$self.attrs.s24Pending", ["not", "$self.attrs.s24Notified"]],
          chance: ["/", "$param.pNotify", 700],
          act: { action: "notifyTransfer", actor: ["any", "person", ["=", "$it.id", "$self.attrs.sellerId"]], target: "$self" } },
        { id: "outings", per: "cat", when: "$self.attrs.registered", chance: 0.03,
          act: { action: "goOut", actor: "$self" } },
        { id: "lost-tags", per: "cat", when: "$self.attrs.wearingTag", chance: 0.002,
          act: { action: "loseTag", actor: "$self" } },
        { id: "new-tags", per: "cat", when: ["and", "$self.attrs.registered", ["not", "$self.attrs.wearingTag"]], chance: 0.05,
          act: { action: "replaceTag", actor: ["rel", "$self", "registeredWith"], target: "$self" } },
        { id: "deaths", per: "cat", chance: 0.0002, remove: true }
      ]
    }
  };

  global.SCHEMES = (global.SCHEMES || []).concat([CAT_ACT_LQA]);
})(window);
