/* The console scheme for the LQA run of the Residential Tenancies Act 1987 (WA), consolidated
   version 07-a0-00 (currency start 29 April 2026), with the Residential Tenancies Regulations 1989
   (WA) 05-ad0-00 so far as the in-scope provisions read them. Subject residential-tenancies-act-lqa.

   Drafted at step 4A (5 October 2026) from this subject's L4: part-1-definitions.l4,
   part-3-div-3-retaliatory-action.l4, part-4-div-1-rent-and-bonds.l4, part-5-termination.l4,
   part-6-boundary.l4, part-7-transitional-2024.l4, regulations-1989.l4, the two Interpretation Act
   modules, and the cases in cases.l4 and cases-consecutive.l4 (scenarios A to K). It follows the
   encoding's reading, including reading A of every fork in registers/fork-register.json (FK-01 to
   FK-26); where a fork decides what happens on screen, the log says what reading B would do.
   Observations name, in plain words, the encoding notes (N-01 to N-28 in ENCODING-NOTES.md) they
   correspond to. Nothing here is a finding and no observation carries a finding ID: findings are
   assigned at 7A-11A.

   Added at 8A (Demonstrate), 5 October 2026, by Claude (agent), for Legalese: `ref` on the
   observations that a candidate in incidents.json cites as scenario or simulation evidence (the LQA
   checker requires a scenario cited as evidence to record the candidate's ID); five observations,
   with the rules that record them ("mixed-tenants", "relet-new-tenant", "notice-under-replaced",
   "s65-later-proceedings", "demand-unlawful-increase"), each marked "added at 8A"; and five
   scenarios at the end of the list. The rules added only log and count, and set temporary facts and
   one relationship (reletAfter) that no other rule reads; they change nothing an existing rule
   decides. Candidates are not findings until challenged at 9A; `foundBy`, tiers and labels are 11A's.

   Day 0 is Monday 1 January 2024, so a run can cross 29 July 2024 (day 210), the day the
   Residential Tenancies Amendment Act 2024 s 25 came into operation, and show the transitional
   provisions (ss 99, 100) at work.

   How the console counts time, as the L4 does:
   - months by Interpretation Act ss 61(1)(a)-(b) and 62. The rules carry a calendar (the same
     day-number algorithm as the jurisdiction library module) so that "12 months after" day r ends
     on the last day of the 12 months beginning on r + 1, and an increase may take effect on that
     last day (FK-15 A). The engine's own month count (ageMonths) is a day out at the end of
     February, so it is not used;
   - "not less than 60 days after" (ss 30(1)(a), 31A(2)(b)(i), 64(2)) by s 61(1)(f): 60 clear days
     (FK-06 A); "earlier than 60 days after" (s 31(1B)(a)) by s 61(1)(b);
   - the last day for doing a thing moves off a Saturday or Sunday to the next weekday
     (s 61(1)(e), (h); FK-08 A).

   Where the console is coarser than the L4 (ENCODING-NOTES.md, "Console scheme"):
   - excluded days are Saturdays and Sundays only; no public holiday is listed (the cases list none);
   - an agreement holds one pending notice of each kind (s 30, s 31A, s 31, s 64, and one s 70A
     notice from each party). A second notice of increase is treated as withdrawing the first;
   - the regulations' status facts (r 5B exemptions, r 5CA, r 7D, r 7F, s 84 orders) are not
     offered: every agreement is an ordinary one for premises south of the 26th parallel;
   - s 31A is applied in its present form to every change of method (so is it in the L4, which does
     not encode the former s 31A);
   - a notice under s 70A given after the fixed term has ended (when s 76C already continues the
     agreement) is not applied as one. The L4 tests s 70A(1), (3) and (4) without regard to when
     the notice is given;
   - who is party to an agreement is two tenant places (a tenant and one co-tenant);
   - a tenancy commences on the day its agreement is entered in the console (a renewal agreed in
     advance is entered on its first day); a scenario may say it commenced earlier.

   The simulation keeps counts it reads to choose whom to let to (people with no tenancy, premises
   with none) in day rules marked "simulation bookkeeping (no provision)"; they run only for the
   people, premises and agreements a generated run made. Every generated event happens through an
   act or a spawn, so a run counts as Nature mode. */
(function (global) {
  "use strict";

  var COMMENCEMENT = 210;   /* 29 July 2024: RTAA 2024 s 25 in operation (SL 2024/143 cl. 2(f); REF-41) */
  var EPOCH = 19723;        /* day 0, 1 January 2024, is day 19 723 after 1 January 1970 */

  /* ---- expression builders (they return data; the scheme holds no functions) ---- */
  function max(a, b) { return ["if", [">=", a, b], a, b]; }
  function min(a, b) { return ["if", ["<=", a, b], a, b]; }
  /* a number typed into an action's form arrives as text: read it as a number, or take a default */
  function num(x, dflt) { return ["if", [">", ["*", x, 1], 0], ["*", x, 1], dflt]; }
  function dateOf(x) { return ["if", ["exists", x], ["date", x], null]; }
  /* 0 Sunday ... 6 Saturday; day 0 was a Monday */
  function weekday(d) { return ["-", ["+", d, 1], ["*", 7, ["floor", ["/", ["+", d, 1], 7]]]]; }
  /* IA s 61(1)(e), (h): a last day that is a Saturday or Sunday moves to the Monday */
  function openDay(d) { return ["if", ["=", weekday(d), 6], ["+", d, 2], ["if", ["=", weekday(d), 0], ["+", d, 1], d]]; }
  function at(h) { return function (k) { return h + ".attrs." + k; }; }
  var S = at("$self"), T = at("$target");

  /* IA ss 61(1)(a), 62: the last day of a period of `months` months beginning on `day`, written to
     `out`. Day numbers become calendar dates by the algorithm in the library module
     (wa-interpretation-act-1984.l4: `the date of day number`, `the day number of`, and `s 62 -- the
     last day of a period of n months beginning on d`). "n months after day r" (s 61(1)(b)) is the
     period beginning on r + 1. The workings are temporary facts on `h`, removed at the end. */
  function lastDayOfMonths(h, day, months, out) {
    var t = function (k) { return h + ".attrs._cal" + k; };
    var fl = function (x, n) { return ["floor", ["/", x, n]]; };
    var mod = function (x, n) { return ["-", x, ["*", n, fl(x, n)]]; };
    var steps = [
      ["Z",    ["+", day, EPOCH + 719468]],
      ["Era",  fl(t("Z"), 146097)],
      ["Doe",  ["-", t("Z"), ["*", t("Era"), 146097]]],
      ["Yoe",  fl(["-", ["+", ["-", t("Doe"), fl(t("Doe"), 1460)], fl(t("Doe"), 36524)], fl(t("Doe"), 146096)], 365)],
      ["Doy",  ["-", t("Doe"), ["-", ["+", ["*", 365, t("Yoe")], fl(t("Yoe"), 4)], fl(t("Yoe"), 100)]]],
      ["Mp",   fl(["+", ["*", 5, t("Doy")], 2], 153)],
      ["D",    ["+", ["-", t("Doy"), fl(["+", ["*", 153, t("Mp")], 2], 5)], 1]],
      ["M",    ["if", ["<", t("Mp"), 10], ["+", t("Mp"), 3], ["-", t("Mp"), 9]]],
      ["Y",    ["+", t("Yoe"), ["*", t("Era"), 400], ["if", ["<=", t("M"), 2], 1, 0]]],
      ["N",    ["+", ["*", t("Y"), 12], ["-", t("M"), 1], months]],
      ["TY",   fl(t("N"), 12)],
      ["TM",   ["+", ["-", t("N"), ["*", t("TY"), 12]], 1]],
      ["Leap", ["or", ["=", mod(t("TY"), 400), 0], ["and", ["=", mod(t("TY"), 4), 0], ["!=", mod(t("TY"), 100), 0]]]],
      ["Dim",  ["if", ["=", t("TM"), 2], ["if", t("Leap"), 29, 28],
                 ["if", ["or", ["=", t("TM"), 4], ["=", t("TM"), 6], ["=", t("TM"), 9], ["=", t("TM"), 11]], 30, 31]]],
      ["TD",   ["if", ["<=", t("D"), t("Dim")], t("D"), ["+", t("Dim"), 1]]],
      ["FY",   ["if", ["<=", t("TM"), 2], ["-", t("TY"), 1], t("TY")]],
      ["FEra", fl(t("FY"), 400)],
      ["FYoe", ["-", t("FY"), ["*", t("FEra"), 400]]],
      ["FMp",  ["if", [">", t("TM"), 2], ["-", t("TM"), 3], ["+", t("TM"), 9]]],
      ["FDoy", ["-", ["+", fl(["+", ["*", 153, t("FMp")], 2], 5), t("TD")], 1]],
      ["FDoe", ["+", ["*", t("FYoe"), 365], fl(t("FYoe"), 4), ["-", t("FDoy"), fl(t("FYoe"), 100)]]]
    ];
    var effects = steps.map(function (s) { return ["set", t(s[0]), s[1]]; });
    effects.push(["set", out, ["-", ["+", ["*", t("FEra"), 146097], t("FDoe")], 719468 + EPOCH + 1]]);
    steps.forEach(function (s) { effects.push(["set", t(s[0]), null]); });
    return effects;
  }

  /* ss 99(2), 100(3) with FK-22 A: does s 30 as in force before 29 July 2024 govern an increase
     taking effect on day x under the agreement h? */
  function formerGoverns(h, x) {
    return ["if", h + ".attrs.s99", ["<=", x, h + ".attrs.expiryDay"], ["<", x, COMMENCEMENT]];
  }

  /* s 31B(1): the increases (and changes of method) under the agreement h continues count for h.
     They are copied when h commences; this refreshes them from the agreement it continues, in case
     that agreement (continued beside h under s 76C) was varied afterwards. */
  function refresh(h) {
    var a = at(h), P = ["rel", h, "continues"];
    var pi = ["attrOf", P, "lastIncDay"], pc = ["attrOf", P, "lastChgDay"];
    var e = [["set", a("_adopt"), ["and", ["exists", pi], ["or", ["not", ["exists", a("lastIncDay")]], [">", pi, a("lastIncDay")]]]]];
    ["lastIncDay", "lastIncL12", "lastIncL6", "lastIncUnder", "lastIncNoticeDay", "lastIncNoticeL12"].forEach(function (k) {
      e.push(["set", a(k), ["if", a("_adopt"), ["attrOf", P, k], a(k)]]);
    });
    e.push(["set", a("_adopt"), ["and", ["exists", pc], ["or", ["not", ["exists", a("lastChgDay")]], [">", pc, a("lastChgDay")]]]]);
    ["lastChgDay", "lastChgL12"].forEach(function (k) {
      e.push(["set", a(k), ["if", a("_adopt"), ["attrOf", P, k], a(k)]]);
    });
    e.push(["set", a("_adopt"), null]);
    return e;
  }

  /* s 30(1)(a), (b), (2)(a), with ss 99-100: the first day an increase noticed on day g could take
     effect under the agreement h, on the readings taken. Written to h's incEarliest. */
  function s30Earliest(h, g) {
    var a = at(h);
    var bar = ["and", ["=", a("kind"), "fixed"], ["not", a("setOut")], ["not", a("periodic76C")]];
    var LF = ["if", ["exists", a("lastIncDay")], a("lastIncL6"), a("startL6")];
    var LP = ["if", ["exists", a("lastIncDay")], a("lastIncL12"), a("startL12")];
    return [
      ["set", a("_e1"), ["+", g, 61]],
      ["set", a("_cF"), max(a("_e1"), LF)],
      ["set", a("_cF"), ["if", bar, max(a("_cF"), ["+", a("fixedLastDay"), 1]), a("_cF")]],
      ["set", a("_cP"), max(a("_e1"), LP)],
      ["set", a("_cP"), ["if", bar, max(a("_cP"), ["+", a("fixedLastDay"), 1]), a("_cP")]],
      ["set", a("incEarliest"), ["if", formerGoverns(h, a("_cF")), a("_cF"), a("_cP")]],
      ["set", a("incEarliestDate"), ["date", a("incEarliest")]],
      ["set", a("_e1"), null], ["set", a("_cF"), null], ["set", a("_cP"), null]
    ];
  }

  /* s 60(1): the agreement h terminates today. An order under s 32 in force lapses with the tenancy
     (s 32(5), FK-23 A); pending notices are spent. */
  function terminate(h, how) {
    var a = at(h);
    return [
      ["set", a("_justEnded"), true],
      ["set", a("_lapseNote"), ["and", ["exists", a("orderMade")], ["not", a("orderLapsed")], ["<=", "$day", a("orderEnd")]]],
      ["set", a("_fk09Note"), ["and", ["=", a("kind"), "fixed"], ["=", "$day", a("expiryDay")], ["exists", a("possDay70A")]]],
      ["set", a("orderLapsedWithTenancy"), ["if", a("_lapseNote"), true, a("orderLapsedWithTenancy")]],
      ["set", a("orderLapsed"), ["if", a("_lapseNote"), true, a("orderLapsed")]],
      ["set", a("orderLapsedDay"), ["if", a("_lapseNote"), "$day", a("orderLapsedDay")]],
      ["set", a("ended"), true],
      ["set", a("endedDay"), "$day"],
      ["set", a("endedDate"), ["date", "$day"]],
      ["set", a("endedHow"), how],
      ["set", a("fixedLastDay"), ["if", ["and", ["=", a("kind"), "fixed"], ["not", a("periodic76C")], ["<", "$day", a("fixedLastDay")]], "$day", a("fixedLastDay")]],
      ["set", a("fixedLastDate"), dateOf(a("fixedLastDay"))],
      ["set", a("incPending"), false], ["set", a("chgPending"), false], ["set", a("n64Pending"), false],
      ["set", a("bondPending"), false]
    ];
  }

  /* the notes that follow a termination, for whichever trigger caused it (terminate() sets the flags) */
  function afterTermination(on, h, forType, suffix) {
    var a = at(h);
    var r = [
      { id: "s32-lapses-with-tenancy" + suffix, on: on, cite: "s 32(5); FK-23", "if": a("_lapseNote"),
        then: [
          ["log", "<b>The order under s 32 made on {" + h.slice(1) + ".attrs.orderMadeDate} lapses with the tenancy.</b> It has effect 'until the expiration of the tenancy of the person who applied for the order or of such period ... as is fixed by the court ..., whichever is the earlier' (s 32(5)). The tenancy is the right of occupancy under this agreement, and it has ended (FK-23 reading A), though the period fixed ran to {" + h.slice(1) + ".attrs.orderEndDate}. On reading B the order would run on while the applicant occupies under this or a continuing agreement (encoding note N-10).",
            { cite: "ss 3 'tenancy', 32(5); FK-23", sev: "warn" }],
          ["observe", "s32-lapse-tenancy"]
        ] },
      { id: "s76c-not-after-expiry-day" + suffix, on: on, cite: "s 76C(1); FK-09", "if": a("_fk09Note"),
        then: [
          ["log", "{" + h.slice(1) + "} terminated on its expiry day, after a notice under s 70A, so s 76C does not continue it: 'continues' presupposes an agreement in force (FK-09 reading A). Read word for word, s 76C(1) applies 'unless the agreement is terminated before the expiry day', and would continue an agreement s 60(1)(b)(i) has just ended (reading B; encoding note N-18).",
            { cite: "ss 60(1)(b)(i), 76C(1); FK-09", sev: "ok" }],
          ["observe", "fk09"]
        ] },
      { id: "after-termination-tidy" + suffix, on: on, cite: "s 60(1)", "if": a("_justEnded"),
        then: [["set", a("_justEnded"), null], ["set", a("_lapseNote"), null], ["set", a("_fk09Note"), null]] }
    ];
    if (forType) r.forEach(function (x) { x["for"] = forType; });
    return r;
  }

  /* who may act on an agreement ($target) */
  var IS_LESSOR = ["=", "$self.id", "$target.rels.lessor"];
  var IS_TENANT = ["or", ["=", "$self.id", "$target.rels.tenant"], ["and", ["exists", "$target.rels.cotenant"], ["=", "$self.id", "$target.rels.cotenant"]]];
  var LIVE = ["not", "$target.attrs.ended"];

  /* s 26A, s 26B(2): a lessor's action listed in s 26A(a), taken after a matter in s 26B(2) arose */
  function retaliation(actionId, kind, what, para) {
    var matter = ["and", ["exists", T("matterDay")], ["<=", T("matterDay"), "$day"]];
    var base = ["and", IS_LESSOR, LIVE];
    return [
      { id: actionId + "-26a-listed", on: "action:" + actionId, cite: "ss 26A(a)" + para + ", 26B(2)", "if": ["and", base, matter],
        then: [["set", T("listedKind"), kind], ["set", T("listedDay"), "$day"], ["set", T("listedDate"), ["date", "$day"]],
               ["set", T("listedWhat"), what], ["set", T("listedMotivated"), ["if", "$p.motivated", true, false]]] },
      { id: actionId + "-26a-retaliatory", on: "action:" + actionId, cite: "s 26A(a)" + para + ", (b)", "if": ["and", base, matter, "$p.motivated"],
        then: [
          ["log", "<b>Retaliatory action.</b> A matter in s 26B(2) arose on {target.attrs.matterDate} ({target.attrs.matterWhat}), and {self} " + what + ", motivated wholly or partly by it (a fact). That is retaliatory action (s 26A(a)" + para + ", (b)). The tenant may apply to a competent court for relief (s 26B(3)).",
            { cite: "ss 26A, 26B(2), (3)", sev: "stop" }],
          ["observe", "retaliatory"]
        ] },
      { id: actionId + "-26a-no-matter", on: "action:" + actionId, cite: "s 26A", "if": ["and", base, ["not", matter], "$p.motivated"],
        then: [["log", "{self}'s motive is not retaliation under s 26A: no matter in s 26B(2) (a request to enforce the tenant's rights, a complaint, a court order) has arisen under {target}.", { cite: "ss 26A, 26B(2)", sev: "ok" }]] }
    ];
  }

  /* s 85, r 12I, FK-12 A: an in-scope notice sent by email is not given */
  function emailed(actionId, which) {
    return { id: actionId + "-email", on: "action:" + actionId, cite: "s 85(1)(c); r 12I; FK-12",
      "if": ["and", IS_LESSOR_OR_TENANT_FOR(actionId), LIVE, ["or", "$p.email", ["=", "$p.how", "email"]]],
      then: [
        ["log", "<b>The " + which + " is sent by email, and is not given.</b> Section 85(1)(c) allows electronic service only 'by prescribed electronic means', and r 12I(2)(b) prescribes email only for an 'authorised notice' (r 12I(1)), which this is not. Consent alone is not enough (FK-12 reading A; encoding note N-20). On reading B it would be given today. The Act fixes no other time at which it is given, so nothing runs from it.",
          { cite: "s 85(1)(c); r 12I(1), (2); FK-12", sev: "warn" }],
        ["observe", "email-notice"]
      ] };
  }
  function IS_LESSOR_OR_TENANT_FOR(actionId) { return actionId === "give70A" ? ["or", IS_LESSOR, IS_TENANT] : IS_LESSOR; }

  /* ---- the s 31B search, for an agreement $self that commences today; $it is a candidate ---- */
  var S1 = ["-", "$self.attrs.startDay", 1];
  var NOT_ME = ["!=", "$it.id", "$self.id"];
  var SAME_PREMISES = ["=", "$it.rels.premises", "$self.rels.premises"];
  var SAME_LESSOR = ["=", "$it.rels.lessor", "$self.rels.lessor"];
  var SHARES = ["or",
    ["and", ["exists", "$it.rels.tenant"], ["=", "$it.rels.tenant", "$self.rels.tenant"]],
    ["and", ["exists", "$it.rels.tenant"], ["exists", "$self.rels.cotenant"], ["=", "$it.rels.tenant", "$self.rels.cotenant"]],
    ["and", ["exists", "$it.rels.cotenant"], ["=", "$it.rels.cotenant", "$self.rels.tenant"]],
    ["and", ["exists", "$it.rels.cotenant"], ["exists", "$self.rels.cotenant"], ["=", "$it.rels.cotenant", "$self.rels.cotenant"]]];
  /* FK-16 A, FK-17 A: the term of a fixed-term agreement ends on the last day of its fixed term
     (whether or not s 76C then continues it); any agreement's term also ends when it terminates */
  function termEndedOn(d) {
    return ["or", ["and", ["=", "$it.attrs.kind", "fixed"], ["=", "$it.attrs.fixedLastDay", d]],
                  ["and", "$it.attrs.ended", ["=", "$it.attrs.endedDay", d]]];
  }
  var W_CONT = ["and", NOT_ME, "$it.attrs.commenced", SAME_PREMISES, SAME_LESSOR, SHARES, termEndedOn(S1)];
  var W_GAP = ["and", NOT_ME, "$it.attrs.commenced", SAME_PREMISES, SAME_LESSOR, SHARES, "$it.attrs.ended", ["<", "$it.attrs.endedDay", S1]];
  var W_NEW_TENANT = ["and", NOT_ME, "$it.attrs.commenced", SAME_PREMISES, SAME_LESSOR, ["not", SHARES], termEndedOn(S1)];
  var W_NEW_LESSOR = ["and", NOT_ME, "$it.attrs.commenced", SAME_PREMISES, ["not", SAME_LESSOR], SHARES, termEndedOn(S1)];
  var W_IN_FORCE = ["and", NOT_ME, "$it.attrs.commenced", ["not", "$it.attrs.ended"], SAME_PREMISES, SAME_LESSOR, SHARES];
  /* added at 8A: an earlier agreement for the premises that ended within 92 days before this one starts
     and shares no tenant with it (any lessor) */
  var W_RELET = ["and", NOT_ME, "$it.attrs.commenced", SAME_PREMISES, "$it.attrs.ended", ["not", SHARES],
    ["<=", ["-", "$self.attrs.startDay", "$it.attrs.endedDay"], 92]];
  /* added at 8A: for an agreement $target, a later agreement in force between the same parties for the
     same premises (the one the parties made to replace it, s 60(1); N-05) */
  var SHARES_T = ["or",
    ["and", ["exists", "$it.rels.tenant"], ["=", "$it.rels.tenant", "$target.rels.tenant"]],
    ["and", ["exists", "$it.rels.tenant"], ["exists", "$target.rels.cotenant"], ["=", "$it.rels.tenant", "$target.rels.cotenant"]],
    ["and", ["exists", "$it.rels.cotenant"], ["=", "$it.rels.cotenant", "$target.rels.tenant"]],
    ["and", ["exists", "$it.rels.cotenant"], ["exists", "$target.rels.cotenant"], ["=", "$it.rels.cotenant", "$target.rels.cotenant"]]];
  var W_NEWER_T = ["and", ["!=", "$it.id", "$target.id"], "$it.attrs.commenced", ["not", "$it.attrs.ended"],
    ["=", "$it.rels.premises", "$target.rels.premises"], ["=", "$it.rels.lessor", "$target.rels.lessor"], SHARES_T,
    [">", "$it.attrs.startDay", "$target.attrs.startDay"]];

  function pred(k) { return ["attrOf", ["rel", "$self", "continues"], k]; }
  function fol(k) { return ["attrOf", ["rel", "$self", "follows"], k]; }
  /* the agreement before this one for the premises: the one it continues, or else the one it follows */
  function before(k) { return ["if", ["exists", "$self.rels.continues"], pred(k), fol(k)]; }

  /* The rules that run when an agreement's tenancy commences. In the console a tenancy commences on
     the day the agreement is entered into (a renewal agreed in advance is entered on its first day);
     a scenario may say it commenced earlier, and the simulation enters a renewal a day or two late
     with its tenancy commencing on the day the offer named. */
  function commencement() {
    var sfx = "", on = "create:agreement";
    var base = ["and", ["exists", S("startDay")], ["<=", S("startDay"), "$day"], ["not", S("commenced")], ["not", S("ended")]];
    var starting = S("_starting");
    var cont = ["exists", "$self.rels.continues"];
    var rules = [
      { id: "commence" + sfx, cite: "s 3 'tenancy'; s 31B(2)", "if": base, then: [
        ["set", S("commenced"), true],
        ["set", starting, true],
        ["set", "$self.rels.continues", ["attrOf", ["any", "agreement", W_CONT], "uid"]]
      ] },
      { id: "commenced-before" + sfx, cite: "s 3 'tenancy'", "if": ["and", starting, ["<", S("startDay"), S("enteredDay")]], then: [
        ["log", "The tenancy under {self} commenced on {self.attrs.startDate}, before it was entered in the console.", { cite: "s 3 'tenancy'" }]
      ] },
      { id: "s76c-already" + sfx, cite: "s 76C(2)", "if": ["and", starting, ["=", S("kind"), "fixed"], ["<", S("expiryDay"), "$day"]], then: [].concat([
        ["set", S("periodic76C"), true],
        ["set", S("periodicFrom"), ["+", S("expiryDay"), 1]],
        ["set", S("periodicFromDate"), ["date", S("periodicFrom")]]
      ], lastDayOfMonths("$self", ["+", S("periodicFrom"), 1], 12, S("p76L12")), [
        ["set", S("p76L12Date"), ["date", S("p76L12")]],
        ["log", "{self}'s fixed term ended on {self.attrs.expiryDate}, and it has continued since then as a periodic tenancy (s 76C(2)).", { cite: "s 76C(2)" }]
      ]) },

      /* ---- s 31B: a continuation ---- */
      { id: "s31b-continuation" + sfx, cite: "s 31B(1)-(3)", "if": ["and", starting, cont], then: [
        ["set", S("contName"), pred("name")],
        ["set", S("contRent"), pred("rentNow")],
        ["set", S("chainStartDay"), ["if", ["exists", pred("chainStartDay")], pred("chainStartDay"), pred("startDay")]],
        ["set", S("chainStartDate"), ["date", S("chainStartDay")]],
        ["set", S("lastIncDay"), pred("lastIncDay")],
        ["set", S("lastIncL12"), pred("lastIncL12")],
        ["set", S("lastIncL6"), pred("lastIncL6")],
        ["set", S("lastIncUnder"), pred("lastIncUnder")],
        ["set", S("lastIncNoticeDay"), pred("lastIncNoticeDay")],
        ["set", S("lastIncNoticeL12"), pred("lastIncNoticeL12")],
        ["set", S("lastChgDay"), pred("lastChgDay")],
        ["set", S("lastChgL12"), pred("lastChgL12")],
        ["set", S("lastIncDate"), dateOf(S("lastIncDay"))],
        ["set", S("lastIncL12Date"), dateOf(S("lastIncL12"))],
        ["set", S("lastChgDate"), dateOf(S("lastChgDay"))],
        ["set", S("lastChgL12Date"), dateOf(S("lastChgL12"))],
        ["log", "<b>{self} is taken to be a continuation of {self.attrs.contName}</b> (s 31B(2)): it is between the same parties (the same lessor, and at least one tenant in common, s 31B(3)), for the same premises, and it starts immediately after the end of the term of {self.attrs.contName}. For working out when the rent was last increased under s 30, or the method of calculating it last changed under s 31A, the two are one (s 31B(1)).",
          { cite: "s 31B(1)-(3)", sev: "ok" }],
        ["observe", "continuation"]
      ] },
      { id: "s31b-beside" + sfx, cite: "s 60(1); s 76C; N-05", "if": ["and", starting, cont, ["not", pred("ended")]], then: [
        ["log", "{self.attrs.contName} has not terminated. No circumstance in s 60(1) ends an agreement when the parties make a further one and the tenant stays: (g) needs vacant possession, and the opening words exclude the general law. So {self.attrs.contName} remains in force beside {self} (for a fixed term, as the periodic tenancy s 76C continues). Encoding note N-05.",
          { cite: "ss 60(1), 76C", sev: "warn" }],
        ["observe", "two-in-force"]
      ] },
      { id: "s31b-fk16" + sfx, cite: "s 31B(2)(c); s 70A(2); FK-16", "if": ["and", starting, cont, ["=", pred("kind"), "fixed"], ["not", ["and", pred("ended"), ["=", pred("endedDay"), S1]]]], then: [
        ["log", "This turns on FK-16. On reading A (taken) the term of {self.attrs.contName} ended on the last day of its fixed term, whether or not s 76C then continued it. On reading B the term of a fixed term ends only when the agreement terminates (s 70A(2): it 'does not end on the expiry day' unless a notice under s 70A is given); {self.attrs.contName} has not terminated, so {self} would not be a continuation. Read so, the commonest renewal, made without a notice, is never one (encoding note N-04).",
          { cite: "ss 31B(2)(c), 70A(2), 76C; FK-16", sev: "warn" }],
        ["observe", "fk16"]
      ] },
      { id: "s31b-fk17" + sfx, cite: "s 31B(2)(c); FK-17", "if": ["and", starting, cont, ["or", ["=", pred("kind"), "periodic"], ["!=", pred("fixedLastDay"), S1]]], then: [
        ["log", "This turns on FK-17. {self.attrs.contName}'s term ended the day it terminated, as a periodic tenancy (reading A, taken). On reading B 'term' means a fixed term, a periodic tenancy has no 'end of the term', and {self} would not be a continuation (encoding note N-06).",
          { cite: "s 31B(2)(c); FK-17", sev: "warn" }],
        ["observe", "fk17"]
      ] },
      { id: "s31b-fk13" + sfx, cite: "s 31B(3)(a); s 3 'lessor'; FK-13", "if": ["and", starting, cont, ["!=", pred("lessorId"), pred("grantedById")]], then: [
        ["log", "This turns on FK-13. {self.attrs.contName} was granted by another lessor; the lessor under it at its end is {self.attrs.lessorName}, who bought the premises, since 'lessor' includes a successor or assignee (s 3; reading A, taken). On reading B the lessor 'under' {self.attrs.contName} is the one who granted it, {self} is not between the same parties, and it starts a fresh 12 months.",
          { cite: "ss 3 'lessor', 31B(3)(a); FK-13", sev: "warn" }],
        ["observe", "fk13"]
      ] },
      { id: "s31b-fk01" + sfx, cite: "s 30(1); s 31B(1); FK-01", "if": ["and", starting, cont, [">", S("rent"), S("contRent")]], then: [
        ["log", "<b>The rent rises from ${self.attrs.contRent} to ${self.attrs.rent} a week, by agreement.</b> A rent a new agreement fixes is not an increase under s 30: no notice is needed, and neither the 60 days nor the 12 months limit it (FK-01 reading A). Section 31B carries across only increases under s 30 and changes under s 31A. On reading B this rise is an increase made otherwise than under s 30, which 'shall not' happen (s 30(1)), and s 82(1)(a) would avoid the term so far as it exceeds the old rent (encoding note N-01).",
          { cite: "ss 30(1), 31B(1); FK-01", sev: "warn" }],
        ["observe", "rent-by-agreement"]
      ] },
      { id: "s31b-clock" + sfx, cite: "ss 30(1)(b), 31B(1)(a)", "if": ["and", starting, cont, ["exists", S("lastIncDay")]], then: [
        ["log", "For the next increase by notice under {self}, the 12 months run from the last increase under s 30, on {self.attrs.lastIncDate} under an agreement it continues (s 31B(1)(a)), not from {self}'s own start: an increase may take effect from {self.attrs.lastIncL12Date} (encoding note N-02).",
          { cite: "ss 30(1)(b), 31B(1)(a)", sev: "warn" }],
        ["observe", "clock-carried"]
      ] },
      { id: "s31b-clock-31a" + sfx, cite: "ss 31A(2)(b)(ii), 31B(1)(b)", "if": ["and", starting, cont, ["exists", S("lastChgDay")]], then: [
        ["log", "For a change of method under {self}, the 12 months run from the last change under s 31A, on {self.attrs.lastChgDate} (s 31B(1)(b)): a change may take effect from {self.attrs.lastChgL12Date}.",
          { cite: "ss 31A(2)(b)(ii), 31B(1)(b)", sev: "warn" }],
        ["observe", "clock-carried"]
      ] },
      { id: "s31b-fk18" + sfx, cite: "s 30(1)(b); FK-18", "if": ["and", starting, cont, ["not", ["exists", S("lastIncDay")]], ["not", S("incomeBased")]], then: [
        ["log", "No rent in the chain was ever increased under s 30, so the 12 months run from 'the day on which the tenancy commenced': {self}'s own commencement, {self.attrs.startDate} (FK-18 reading A). On reading B they would run from the first commencement in the chain, {self.attrs.chainStartDate}.",
          { cite: "s 30(1)(b); FK-18", sev: "ok" }],
        ["observe", "fk18"]
      ] },
      /* added at 8A: one side has a single tenant and the other co-tenants (s 31B(3)(b)) */
      { id: "s31b-mixed-tenants" + sfx, cite: "s 31B(3)(b); s 3 'party' (a)", "if": ["and", starting, cont,
          ["or", ["and", ["exists", "$self.rels.cotenant"], ["not", ["exists", pred("cotenantId")]]],
                 ["and", ["not", ["exists", "$self.rels.cotenant"]], ["exists", pred("cotenantId")]]]], then: [
        ["log", "This turns on the words of s 31B(3)(b): the two agreements are between the same parties if 'the tenant, or at least 1 co-tenant, is the same under both agreements'. One of {self} and {self.attrs.contName} has a single tenant and the other has co-tenants (s 3 'party' (a)(ii), (iii)). Read word for word, neither 'the tenant' nor 'at least 1 co-tenant' is the same under both, and {self} would not be a continuation. The console, like the encoding, counts any tenant in common.",
          { cite: "s 31B(3)(b); s 3 'party' (a)", sev: "warn" }],
        ["observe", "mixed-tenants"]
      ] },

      /* ---- no continuation: say why, where there was an agreement before ---- */
      { id: "s31b-find-gap" + sfx, cite: "s 31B(2)(c)", "if": ["and", starting, ["not", cont]], then: [
        ["set", "$self.rels.follows", ["attrOf", ["any", "agreement", W_GAP], "uid"]],
        ["set", S("followsWhy"), ["if", ["exists", "$self.rels.follows"], "gap", null]]
      ] },
      { id: "s31b-find-new-tenant" + sfx, cite: "s 31B(3)(b)", "if": ["and", starting, ["not", cont], ["not", ["exists", "$self.rels.follows"]]], then: [
        ["set", "$self.rels.follows", ["attrOf", ["any", "agreement", W_NEW_TENANT], "uid"]],
        ["set", S("followsWhy"), ["if", ["exists", "$self.rels.follows"], "tenant", null]]
      ] },
      { id: "s31b-find-new-lessor" + sfx, cite: "s 31B(3)(a)", "if": ["and", starting, ["not", cont], ["not", ["exists", "$self.rels.follows"]]], then: [
        ["set", "$self.rels.follows", ["attrOf", ["any", "agreement", W_NEW_LESSOR], "uid"]],
        ["set", S("followsWhy"), ["if", ["exists", "$self.rels.follows"], "lessor", null]]
      ] },
      { id: "s31b-find-in-force" + sfx, cite: "s 31B(2)(c); s 60(1)", "if": ["and", starting, ["not", cont], ["not", ["exists", "$self.rels.follows"]]], then: [
        ["set", "$self.rels.follows", ["attrOf", ["any", "agreement", W_IN_FORCE], "uid"]],
        ["set", S("followsWhy"), ["if", ["exists", "$self.rels.follows"], "inforce", null]]
      ] },
      { id: "s31b-follows" + sfx, cite: "s 31B(2)", "if": ["and", starting, ["exists", "$self.rels.follows"]], then: [
        ["set", S("folName"), fol("name")],
        ["set", S("folRent"), fol("rentNow")],
        ["set", S("folEndedDate"), fol("endedDate")],
        ["set", S("gapDays"), ["if", ["=", S("followsWhy"), "gap"], ["-", S1, fol("endedDay")], null]]
      ] },
      { id: "s31b-gap" + sfx, cite: "s 31B(2)(c); N-03", "if": ["and", starting, ["=", S("followsWhy"), "gap"]], then: [
        ["log", "<b>{self} is not a continuation of {self.attrs.folName}.</b> {self.attrs.folName} terminated on {self.attrs.folEndedDate}, and {self} does not start 'immediately after the end of the term' (s 31B(2)(c)): {self.attrs.gapDays} day(s) lie between. Encoding note N-03.",
          { cite: "s 31B(2)(c)", sev: "warn" }],
        ["observe", "gap"]
      ] },
      { id: "s31b-new-tenant" + sfx, cite: "s 31B(3)(b); N-07", "if": ["and", starting, ["=", S("followsWhy"), "tenant"]], then: [
        ["log", "<b>{self} is not a continuation of {self.attrs.folName}.</b> No tenant under {self} was a tenant under {self.attrs.folName}, so they are not 'between the same parties' (s 31B(3)(b)), though the premises and the lessor are the same. The limit attaches to the parties, not the premises (encoding note N-07).",
          { cite: "s 31B(2)(a), (3)(b)", sev: "warn" }],
        ["observe", "new-tenant"]
      ] },
      { id: "s31b-new-lessor" + sfx, cite: "s 31B(3)(a)", "if": ["and", starting, ["=", S("followsWhy"), "lessor"]], then: [
        ["log", "<b>{self} is not a continuation of {self.attrs.folName}.</b> The lessor under {self} is not the lessor under {self.attrs.folName} at its end, so they are not 'between the same parties' (s 31B(3)(a)).",
          { cite: "s 31B(2)(a), (3)(a)", sev: "warn" }],
        ["observe", "new-lessor"]
      ] },
      { id: "s31b-in-force" + sfx, cite: "ss 31B(2)(c), 60(1); N-05", "if": ["and", starting, ["=", S("followsWhy"), "inforce"]], then: [
        ["log", "<b>{self} is not a continuation of {self.attrs.folName}.</b> {self.attrs.folName}, between the same parties for the same premises, has not terminated and its term did not end yesterday, so {self} does not start 'immediately after the end of the term' (s 31B(2)(c); FK-17 reading A for a periodic tenancy). No circumstance in s 60(1) ends it while the tenant stays, and it remains in force beside {self} (encoding note N-05).",
          { cite: "ss 31B(2)(c), 60(1)", sev: "warn" }],
        ["observe", "not-ended"]
      ] },
      { id: "s31b-fk10" + sfx, cite: "s 70A(5); s 76C(2); FK-10", "if": ["and", starting, ["=", S("followsWhy"), "inforce"], ["=", fol("kind"), "fixed"], ["=", fol("expiryDay"), S1], [">", fol("fixedLastDay"), S1]], then: [
        ["log", "This turns on FK-10. A notice under s 70A put {self.attrs.folName}'s possession day after its expiry day, so its term expires on the possession day and it is a fixed term until then (s 70A(5); reading A, taken). On reading B it became a periodic tenancy after the expiry day (s 76C(2)), its fixed term ended yesterday, and {self} would be a continuation.",
          { cite: "ss 70A(5), 76C(2); FK-10", sev: "ok" }],
        ["observe", "fk10"]
      ] },
      { id: "s31b-fresh" + sfx, cite: "s 30(1)(b)", "if": ["and", starting, ["exists", "$self.rels.follows"], ["not", S("incomeBased")]], then: [
        ["log", "Under {self} the 12 months run afresh from its own commencement, {self.attrs.startDate}: its first increase by notice may take effect from {self.attrs.startL12Date}. The rent it fixes (${self.attrs.rent} a week, against ${self.attrs.folRent} under {self.attrs.folName}) was not limited by s 30.",
          { cite: "s 30(1)(b)", sev: "ok" }],
        ["observe", "fresh-clock"]
      ] },
      { id: "s31b-first" + sfx, cite: "s 30(1)(b)", "if": ["and", starting, ["not", cont], ["not", ["exists", "$self.rels.follows"]], ["not", S("incomeBased")]], then: [
        ["log", "Under {self} the rent may first be increased by notice from {self.attrs.startL12Date}, 12 months after the tenancy commenced (s 30(1)(b); IA ss 61(1)(b), 62).", { cite: "s 30(1)(b)" }]
      ] },
      /* added at 8A: the premises are let again to a new tenant within 92 days of an earlier tenancy's end */
      { id: "s31b-relet" + sfx, cite: "ss 30(1)(b), 31B(3)(b)", "if": ["and", starting, ["not", cont], ["not", S("incomeBased")],
          [">", ["count", "agreement", W_RELET], 0]], then: [
        ["set", "$self.rels.reletAfter", ["attrOf", ["any", "agreement", W_RELET], "uid"]],
        ["set", S("reletName"), ["attrOf", ["rel", "$self", "reletAfter"], "name"]],
        ["set", S("reletRent"), ["attrOf", ["rel", "$self", "reletAfter"], "rentNow"]],
        ["set", S("reletEnded"), ["attrOf", ["rel", "$self", "reletAfter"], "endedDate"]]
      ] },
      { id: "s31b-relet-higher" + sfx, cite: "ss 30(1)(b), 31B(2), (3)", "if": ["and", starting, ["exists", "$self.rels.reletAfter"], [">", S("rent"), S("reletRent")]], then: [
        ["log", "<b>The premises are let again, to a new tenant, at more rent:</b> ${self.attrs.rent} a week under {self}, against ${self.attrs.reletRent} under {self.attrs.reletName}, which ended on {self.attrs.reletEnded}. No tenant is the same, so {self} continues nothing (s 31B(3)(b)): the rent it fixes is not limited by s 30, and its 12 months run afresh. Had the earlier tenancy run on, its rent could have risen only by notice, once in 12 months. The limit attaches to the tenancy, not to the premises.",
          { cite: "ss 30(1)(b), 31B(2), (3)", sev: "warn" }],
        ["observe", "relet-new-tenant"]
      ] },

      /* ---- an order under s 32 made under the agreement before (FK-23) ---- */
      { id: "s32-fk23-carry" + sfx, cite: "s 32(5); FK-23", "if": ["and", starting, ["or", cont, ["exists", "$self.rels.follows"]], before("orderLapsedWithTenancy"), [">=", before("orderEnd"), S("startDay")]], then: [
        ["set", S("prevOrderMax"), before("orderMax")],
        ["set", S("prevOrderEnd"), before("orderEnd")],
        ["set", S("prevOrderEndDate"), before("orderEndDate")],
        ["set", S("prevOrderFrom"), before("name")],
        ["log", "The order under s 32 that fixed the rent of {self.attrs.prevOrderFrom} at ${self.attrs.prevOrderMax} lapsed when that tenancy ended (FK-23 reading A), so {self}'s rent (${self.attrs.rent}) is not limited by it. On reading B the applicant's tenancy continues under {self}, and the order would be in force until {self.attrs.prevOrderEndDate} (encoding note N-10).",
          { cite: "s 32(5); FK-23", sev: "warn" }],
        ["observe", "fk23"]
      ] },
      { id: "commence-done" + sfx, cite: "s 3 'tenancy'", "if": starting, then: [["set", starting, null]] }
    ];
    rules.forEach(function (r) { r.on = on; });
    return rules;
  }

  /* ---- the evaluation of a notice of increase on the day it names (ss 30, 99, 100) ----
     The first rule works out every test on the due day and sets a flag (_w...) for each thing to
     say; the rules after it read only their flag, so on other days they cost one lookup. */
  function when(k) { return S("_w" + k); }
  var INC_FLAGS = {
    Income: ["not", S("_applies")],
    NotGiven: ["and", S("_applies"), ["not", S("_given")]],
    Form: ["and", S("_applies"), S("_given"), ["not", S("_formOk")]],
    Sixty: ["and", S("_applies"), S("_given"), ["not", S("_ok60")]],
    Fk06: ["and", S("_given"), ["=", "$day", ["+", S("incGiven"), 60]]],
    TwelveFromStart: ["and", S("_applies"), ["not", S("_ok12")], ["not", S("_hasInc")]],
    TwelveFromIncrease: ["and", S("_applies"), ["not", S("_ok12")], S("_hasInc")],
    Fk02: ["and", ["not", S("_ok12")], S("_hasInc"), ["exists", S("lastIncNoticeL12")], ["not", S("_former")], [">=", "$day", S("lastIncNoticeL12")]],
    Fk04: ["and", ["not", S("_former")], S("_hasInc"), ["=", S("lastIncUnder"), "former"]],
    Bar: ["and", S("_applies"), S("_bar")],
    Excluded: ["and", S("_applies"), S("excluded")],
    S1004: ["and", S("_reach"), ["not", S("_ok")]],
    S1004Ok: ["and", S("_reach"), S("_ok")],
    Ok: S("_ok"),
    Former: ["and", S("_ok"), S("_former")],
    Fk15: ["and", S("_ok"), ["=", "$day", S("_L")]],
    Fk03: ["and", S("_ok"), ["=", S("kind"), "fixed"], ["not", S("setOut")], [">=", S("incGiven"), S("startDay")], ["<=", S("incGiven"), S("fixedLastDay")], [">", "$day", S("fixedLastDay")]],
    Fk19: ["and", S("_ok"), S("periodic76C"), [">", "$day", S("periodicFrom")], ["not", S("_hasInc")], ["not", S("_former")], ["<", "$day", S("p76L12")]],
    Fk22: ["and", S("s99"), S("_given"), ["<=", S("incGiven"), S("expiryDay")], [">", "$day", S("expiryDay")]],
    Fk21: ["and", S("_ok"), ["not", S("s99")], ["<=", S("startDay"), COMMENCEMENT], S("_given"), ["<", S("incGiven"), COMMENCEMENT], ["<", "$day", COMMENCEMENT]],
    Fk26: ["and", S("_ok"), ["or", ["and", S("_former"), ["=", S("incForm"), "s88c"]], ["and", ["not", S("_former")], ["=", S("incForm"), "minister"]]]],
    Carried: ["and", S("_ok"), ["exists", "$self.rels.continues"], S("_hasInc"), ["<", S("lastIncDay"), S("startDay")], ["<", "$day", S("startL12")]],
    Order: ["and", S("_ok"), ["exists", S("orderMade")], ["not", S("orderLapsed")], ["<=", "$day", S("orderEnd")], [">", S("incRent"), S("orderMax")]],
    No: ["not", S("_ok")]
  };
  var INC_TEMPS = ["_former", "_hasInc", "_r", "_L", "_given", "_ok60", "_ok12", "_bar", "_formOk", "_applies", "_ok", "_reach", "_months", "_version",
                   "_rDate", "_LDate", "_e61Date"];
  var increaseRules = [
    { id: "s30-due", on: "day", "for": "agreement", cite: "ss 30(1)-(3), 99(3), 100(3), (4)",
      "if": ["and", S("incPending"), ["=", "$day", S("incEffect")], ["not", S("ended")]],
      then: [].concat(refresh("$self"), [
        ["set", S("_former"), formerGoverns("$self", "$day")],
        ["set", S("_hasInc"), ["exists", S("lastIncDay")]],
        ["set", S("_r"), ["if", S("_hasInc"), S("lastIncDay"), S("startDay")]],
        ["set", S("_L"), ["if", S("_former"), ["if", S("_hasInc"), S("lastIncL6"), S("startL6")], ["if", S("_hasInc"), S("lastIncL12"), S("startL12")]]],
        ["set", S("_given"), ["exists", S("incGiven")]],
        ["set", S("_ok60"), ["and", S("_given"), [">=", "$day", ["+", S("incGiven"), 61]]]],
        ["set", S("_ok12"), [">=", "$day", S("_L")]],
        ["set", S("_bar"), ["and", ["=", S("kind"), "fixed"], ["not", S("setOut")], [">=", "$day", S("startDay")], ["<=", "$day", S("fixedLastDay")]]],
        ["set", S("_formOk"), ["!=", S("incForm"), "none"]],
        ["set", S("_applies"), ["not", S("incomeBased")]],
        ["set", S("_ok"), ["and", S("_applies"), S("_given"), S("_formOk"), S("_ok60"), S("_ok12"), ["not", S("_bar")], ["not", S("excluded")]]],
        ["set", S("_reach"), ["and", ["not", S("s99")], ["<=", S("startDay"), COMMENCEMENT], S("_given"), ["<", S("incGiven"), COMMENCEMENT], [">=", "$day", COMMENCEMENT]]],
        ["set", S("_months"), ["if", S("_former"), 6, 12]],
        ["set", S("_version"), ["if", S("_former"), "s 30 as in force before 29 July 2024 (6 months)", "s 30 as in force from 29 July 2024 (12 months)"]],
        ["set", S("_rDate"), ["date", S("_r")]],
        ["set", S("_LDate"), ["date", S("_L")]],
        ["set", S("_e61Date"), ["if", S("_given"), ["date", ["+", S("incGiven"), 61]], null]]
      ], Object.keys(INC_FLAGS).map(function (k) { return ["set", when(k), INC_FLAGS[k]]; }), [
        ["set", when("Done"), true]
      ]) },
    { id: "s30-due-income", on: "day", "for": "agreement", cite: "ss 30(1), 31A(1)", "if": when("Income"), then: [
      ["log", "<b>No increase under {self}:</b> its rent is calculated by reference to the tenant's income, and s 30(1) does not apply to it. The method may be changed only under s 31A, 'but otherwise the rent must not increase or be increased' (s 31A(1)).",
        { cite: "ss 30(1), 31A(1)", sev: "warn" }],
      ["observe", "inc-income-based"]
    ] },
    { id: "s30-due-not-given", on: "day", "for": "agreement", cite: "ss 30(3), 85; FK-12", "if": when("NotGiven"), then: [
      ["log", "<b>No increase under {self}:</b> the notice was sent by email and never given under s 85 (FK-12 reading A), so it is not a notice 'given in accordance with this section' (s 30(3)).",
        { cite: "ss 30(3), 85(1)(c); FK-12", sev: "warn" }]
    ] },
    { id: "s30-due-form", on: "day", "for": "agreement", cite: "s 30(1) 'in the approved form'", "if": when("Form"), then: [
      ["log", "s 30(1): the notice is not in an approved form, so it is not a notice under s 30.", { cite: "s 30(1); s 3 'approved form'", sev: "warn" }],
      ["observe", "inc-form"]
    ] },
    { id: "s30-due-60", on: "day", "for": "agreement", cite: "s 30(1)(a); IA s 61(1)(f); FK-06", "if": when("Sixty"), then: [
      ["log", "s 30(1)(a): the day must be 'not less than 60 days after the day on which the notice is given', which is 60 clear days (IA s 61(1)(f); FK-06 reading A). For a notice given on {self.attrs.incGivenDate}, {self.attrs._e61Date} at the earliest.",
        { cite: "s 30(1)(a); IA s 61(1)(f); FK-06", sev: "warn" }],
      ["observe", "inc-60-days"]
    ] },
    { id: "s30-due-12-from-start", on: "day", "for": "agreement", cite: "s 30(1)(b); IA ss 61(1)(b), 62", "if": when("TwelveFromStart"), then: [
      ["log", "s 30(1)(b), under {self.attrs._version}: the day must be not less than {self.attrs._months} months after the day the tenancy commenced, {self.attrs._rDate}. Those months end on {self.attrs._LDate}, the first day an increase can take effect (IA ss 61(1)(b), 62; FK-15 reading A).",
        { cite: "s 30(1)(b); IA ss 61(1)(b), 62", sev: "warn" }],
      ["observe", "inc-12-months"]
    ] },
    { id: "s30-due-12-from-increase", on: "day", "for": "agreement", cite: "ss 30(1)(b), 31B(1)(a); IA ss 61(1)(b), 62", "if": when("TwelveFromIncrease"), then: [
      ["log", "s 30(1)(b), under {self.attrs._version}: the rent has been increased under s 30, last on {self.attrs._rDate} (under this agreement or one it continues, s 31B), and the day must be not less than {self.attrs._months} months after that. They end on {self.attrs._LDate}, the first day an increase can take effect (IA ss 61(1)(b), 62; FK-02 A, FK-15 A).",
        { cite: "ss 30(1)(b), 31B(1)(a)", sev: "warn" }],
      ["observe", "inc-12-months"]
    ] },
    { id: "s30-due-bar", on: "day", "for": "agreement", cite: "s 30(2)(a); FK-03; FK-10", "if": when("Bar"), then: [
      ["log", "s 30(2)(a): the increase would take effect during the currency of the fixed term, which runs to {self.attrs.fixedLastDate}, and the agreement does not set out the amount of an increase or how to calculate it. The right to increase 'is not exercisable' (FK-03 reading A: the bar is on increases taking effect during the term).",
        { cite: "s 30(2)(a); FK-03", sev: "warn" }],
      ["observe", "inc-fixed-term"]
    ] },
    { id: "s30-due-excluded", on: "day", "for": "agreement", cite: "s 30(2)(b)", "if": when("Excluded"), then: [
      ["log", "s 30(2)(b): the agreement excludes rent increases.", { cite: "s 30(2)(b)", sev: "warn" }],
      ["observe", "inc-excluded"]
    ] },
    { id: "s30-due-s100-4", on: "day", "for": "agreement", cite: "s 100(4); FK-21", "if": when("S1004"), then: [
      ["log", "<b>s 100(4):</b> the notice was given before 29 July 2024 under an agreement in force on that day, for an increase on or after it, and it does not comply with s 30 as in force from then. It 'has no effect' (FK-21 reading A: s 100(4) reaches notices whose increase is to take effect from 29 July 2024).",
        { cite: "s 100(2), (4); FK-21", sev: "warn" }],
      ["observe", "inc-s100-4"]
    ] },
    { id: "s30-due-no", on: "day", "for": "agreement", cite: "s 30(1) closing words", "if": when("No"), then: [
      ["log", "<b>The notice of increase under {self} has no effect.</b> The rent stays at ${self.attrs.rentNow} a week: 'otherwise the rent shall not increase or be increased' (s 30(1)).",
        { cite: "s 30(1), (3)", sev: "warn" }],
      ["observe", "increase-no-effect"]
    ] },
    { id: "s30-due-ok", on: "day", "for": "agreement", cite: "s 30(1), (3)", "if": when("Ok"), then: [].concat([
      ["set", S("prevRent"), S("rentNow")],
      ["set", S("rentNow"), S("incRent")],
      ["set", S("lastIncNoticeDay"), S("incGiven")],
      ["set", S("lastIncDay"), "$day"],
      ["set", S("lastIncUnder"), ["if", S("_former"), "former", "present"]],
      ["set", S("lastIncDate"), ["date", "$day"]]
    ], lastDayOfMonths("$self", ["+", "$day", 1], 12, S("lastIncL12")),
       lastDayOfMonths("$self", ["+", "$day", 1], 6, S("lastIncL6")),
       lastDayOfMonths("$self", ["+", S("incGiven"), 1], 12, S("lastIncNoticeL12")), [
      ["set", S("lastIncL12Date"), ["date", S("lastIncL12")]],
      ["log", "<b>The rent under {self} rises from ${self.attrs.prevRent} to ${self.attrs.rentNow} a week today</b> (s 30(3)). Under {self.attrs._version}: the notice was given on {self.attrs.incGivenDate}, not less than 60 clear days before; and today is not less than {self.attrs._months} months after {self.attrs._rDate}. The next increase may take effect from {self.attrs.lastIncL12Date}.",
        { cite: "s 30(1), (3)", sev: "ok" }],
      ["observe", "increase-effect"]
    ]) },
    { id: "s30-due-s100-4-complies", on: "day", "for": "agreement", cite: "s 100(4)", "if": when("S1004Ok"), then: [
      ["log", "s 100(4) reaches the notice (given before 29 July 2024, for an increase after it) and it complies with s 30 as in force from 29 July 2024, so it has effect.", { cite: "s 100(4)", sev: "ok" }]
    ] },
    { id: "s30-due-former", on: "day", "for": "agreement", cite: "ss 99(3), 100(3)", "if": when("Former"), then: [
      ["log", "The increase is governed by s 30 as in force before 29 July 2024 ({self.attrs._months} months; a form approved by the Minister).", { cite: "ss 99(3), 100(3)", sev: "ok" }],
      ["observe", "inc-former-s30"]
    ] },
    { id: "s30-due-former-s99", on: "day", "for": "agreement", cite: "s 99(2), (3); FK-22", "if": ["and", when("Former"), S("s99")], then: [
      ["log", "Section 99(3) continues the former s 30 for {self}, a fixed term entered into before 29 July 2024, until the end of its current term, {self.attrs.expiryDate}.", { cite: "s 99(2), (3); FK-22", sev: "ok" }]
    ] },
    { id: "s30-due-former-before", on: "day", "for": "agreement", cite: "RTAA 2024 s 25; SL 2024/143 cl. 2(f)", "if": ["and", when("Former"), ["not", S("s99")]], then: [
      ["log", "The increase takes effect before 29 July 2024, when the amendment (RTAA 2024 s 25) came into operation.", { cite: "ss 99, 100; SL 2024/143", sev: "ok" }]
    ] },
    { id: "s30-due-fk06", on: "day", "for": "agreement", cite: "s 30(1)(a); FK-06", "if": when("Fk06"), then: [
      ["log", "This turns on FK-06: today is the 60th day after the notice was given. Counted under IA s 61(1)(b) alone (reading B), that is 'not less than 60 days after'; counted under s 61(1)(f) (reading A, taken), it is a day short (encoding note N-14).",
        { cite: "s 30(1)(a); IA s 61(1)(b), (f); FK-06", sev: "warn" }],
      ["observe", "fk06"]
    ] },
    { id: "s30-due-fk02", on: "day", "for": "agreement", cite: "s 30(1)(b); FK-02", "if": when("Fk02"), then: [
      ["log", "This turns on FK-02. The rent was 'last so increased' on the day the increase took effect (reading A, taken). On reading B it was the day that notice was given, and the 12 months would already have run.",
        { cite: "s 30(1)(b); FK-02", sev: "ok" }],
      ["observe", "fk02"]
    ] },
    { id: "s30-due-fk04", on: "day", "for": "agreement", cite: "s 30(1)(b); IA s 16(2); FK-04", "if": when("Fk04"), then: [
      ["log", "This turns on FK-04. The last increase was under s 30 as in force before 29 July 2024; it is an increase 'under this section', the section as amended from time to time (IA s 16(2); reading A, taken). On reading B only increases under the present s 30 count, and the 12 months would run from the commencement of the tenancy on {self.attrs.startDate}.",
        { cite: "s 30(1)(b); IA s 16(2); FK-04", sev: "warn" }],
      ["observe", "fk04"]
    ] },
    { id: "s30-due-fk15", on: "day", "for": "agreement", cite: "s 30(1)(b); FK-15", "if": when("Fk15"), then: [
      ["log", "This turns on FK-15: today is the last day of the {self.attrs._months} months after {self.attrs._rDate} (IA ss 61(1)(b), 62), and that day is itself 'not less than' {self.attrs._months} months after (reading A, taken). On reading B the months must have run in full, and tomorrow would be the first good day.",
        { cite: "s 30(1)(b); IA s 62; FK-15", sev: "ok" }],
      ["observe", "fk15"]
    ] },
    { id: "s30-due-fk03", on: "day", "for": "agreement", cite: "s 30(2)(a); FK-03", "if": when("Fk03"), then: [
      ["log", "This turns on FK-03. The notice was given during the fixed term, for an increase after it: s 30(2)(a) bars an increase taking effect during the term, not a notice given in it (reading A, taken). On reading B the right was 'not exercisable' when the notice was given, and the increase would have no effect (encoding note N-25).",
        { cite: "s 30(2)(a); FK-03", sev: "ok" }],
      ["observe", "fk03"]
    ] },
    { id: "s30-due-fk19", on: "day", "for": "agreement", cite: "s 30(1)(b); s 76C(2); FK-19", "if": when("Fk19"), then: [
      ["log", "This turns on FK-19. {self} continues as a periodic tenancy under s 76C, and the tenancy it continues commenced on {self.attrs.startDate} (reading A, taken). On reading B s 76C created a new periodic tenancy on {self.attrs.periodicFromDate}, and the 12 months would not end until {self.attrs.p76L12Date} (encoding note N-26).",
        { cite: "ss 30(1)(b), 76C(2); FK-19", sev: "ok" }],
      ["observe", "fk19"]
    ] },
    { id: "s30-due-fk22", on: "day", "for": "agreement", cite: "s 99(3); FK-22", "if": when("Fk22"), then: [
      ["log", "This turns on FK-22. Section 99(3) continued the former s 30 for {self} 'until the end of the current term' ({self.attrs.expiryDate}); the notice was given in that term for an increase after it. Reading A (taken) applies the version in force for the day of the increase, the present s 30; on reading B the version for the day the notice was given (6 months) would govern (encoding note N-13).",
        { cite: "s 99(3); FK-22", sev: "warn" }],
      ["observe", "fk22"]
    ] },
    { id: "s30-due-fk21", on: "day", "for": "agreement", cite: "s 100(4); IA ss 5, 37(1)(b); FK-21", "if": when("Fk21"), then: [
      ["log", "This turns on FK-21. The notice was given before 29 July 2024 and its increase takes effect before then, under the former s 30; s 100(4) does not reach it (reading A, taken: IA s 37(1)(b) saves what was duly done before the repeal of '6 months'). Read alone (reading B), s 100(4) reaches every notice given before 29 July 2024, and this one, judged by the present s 30, would have no effect (encoding note N-11).",
        { cite: "s 100(4); IA ss 5, 37(1)(b); FK-21", sev: "ok" }],
      ["observe", "fk21"]
    ] },
    { id: "s30-due-fk26", on: "day", "for": "agreement", cite: "s 30(1); IA s 74; FK-26", "if": when("Fk26"), then: [
      ["log", "This turns on FK-26. The notice is in an approved form, but not the one the governing version names (the present s 30 asks for the form approved under s 88C; the former, a form approved by the Minister). Reading A (taken): IA s 74 saves a form whose deviations are immaterial and not misleading, taken here to be so. On reading B the notice would fail for its form (encoding note N-12).",
        { cite: "s 30(1); s 88C; IA s 74; FK-26", sev: "ok" }],
      ["observe", "fk26"]
    ] },
    { id: "s30-due-carried", on: "day", "for": "agreement", cite: "ss 30(1)(b), 31B; FK-13; FK-16; FK-17", "if": when("Carried"), then: [
      ["log", "<b>An increase by notice less than 12 months after {self} began</b>, on top of the rent it fixed: s 31B carries the last increase under the agreement it continues, and the 12 months ran from that (encoding note N-02). Were {self} not a continuation (as on reading B of FK-16, FK-17 or FK-13, where one of them decides it), they would run from its own start and end on {self.attrs.startL12Date}.",
        { cite: "ss 30(1)(b), 31B(1)(a); FK-16; FK-17; FK-13", sev: "warn" }],
      ["observe", "clock-carried-used"]
    ] },
    { id: "s30-due-order", on: "day", "for": "agreement", cite: "s 32(4), (7)", "if": when("Order"), then: [
      ["log", "An order under s 32 is in force until {self.attrs.orderEndDate}: the rent payable may not exceed ${self.attrs.orderMax} a week while it is (s 32(4)), and demanding more is an offence (s 32(7)).", { cite: "s 32(4), (7)", sev: "warn" }]
    ] },
    { id: "s30-due-done", on: "day", "for": "agreement", cite: "s 30(3)", "if": when("Done"), then: [["set", S("incPending"), false]]
      .concat(INC_TEMPS.map(function (k) { return ["set", S(k), null]; }))
      .concat(Object.keys(INC_FLAGS).concat(["Done"]).map(function (k) { return ["set", when(k), null]; })) }
  ];

  /* ---- s 31A: a change of method, evaluated on the day it names ---- */
  var CHG_FLAGS = {
    CFixed: ["not", S("incomeBased")],
    CSixty: ["and", S("incomeBased"), S("_given"), ["not", S("_ok60")]],
    CTwelve: ["and", S("incomeBased"), ["not", S("_ok12")]],
    COk: S("_ok"),
    CNo: ["not", S("_ok")]
  };
  var CHG_TEMPS = ["_hasChg", "_r", "_L", "_given", "_ok60", "_ok12", "_ok", "_rDate", "_LDate", "_e61Date"];
  var changeRules = [
    { id: "s31a-due", on: "day", "for": "agreement", cite: "s 31A(1), (2); s 31B(1)(b)",
      "if": ["and", S("chgPending"), ["=", "$day", S("chgEffect")], ["not", S("ended")]],
      then: [].concat(refresh("$self"), [
        ["set", S("_hasChg"), ["exists", S("lastChgDay")]],
        ["set", S("_r"), ["if", S("_hasChg"), S("lastChgDay"), S("startDay")]],
        ["set", S("_L"), ["if", S("_hasChg"), S("lastChgL12"), S("startL12")]],
        ["set", S("_given"), ["exists", S("chgGiven")]],
        ["set", S("_ok60"), ["and", S("_given"), [">=", "$day", ["+", S("chgGiven"), 61]]]],
        ["set", S("_ok12"), [">=", "$day", S("_L")]],
        ["set", S("_ok"), ["and", S("incomeBased"), S("_given"), S("_ok60"), S("_ok12")]],
        ["set", S("_rDate"), ["date", S("_r")]],
        ["set", S("_LDate"), ["date", S("_L")]],
        ["set", S("_e61Date"), ["if", S("_given"), ["date", ["+", S("chgGiven"), 61]], null]]
      ], Object.keys(CHG_FLAGS).map(function (k) { return ["set", when(k), CHG_FLAGS[k]]; }), [
        ["set", when("CDone"), true]
      ]) },
    { id: "s31a-due-fixed-rent", on: "day", "for": "agreement", cite: "s 31A(1)", "if": when("CFixed"), then: [
      ["log", "s 31A applies only where the rent is calculated by reference to the tenant's income; {self}'s rent is a fixed amount (s 30 governs it).", { cite: "ss 30(1), 31A(1)", sev: "warn" }]
    ] },
    { id: "s31a-due-60", on: "day", "for": "agreement", cite: "s 31A(2)(b)(i); IA s 61(1)(f); FK-06", "if": when("CSixty"), then: [
      ["log", "s 31A(2)(b)(i): the change must take effect not less than 60 clear days after the notice is given (IA s 61(1)(f); FK-06 A): {self.attrs._e61Date} at the earliest.", { cite: "s 31A(2)(b)(i); FK-06", sev: "warn" }]
    ] },
    { id: "s31a-due-12", on: "day", "for": "agreement", cite: "ss 31A(2)(b)(ii), 31B(1)(b)", "if": when("CTwelve"), then: [
      ["log", "s 31A(2)(b)(ii): the change must take effect not less than 12 months after {self.attrs._rDate} (the commencement of the tenancy, or the last change under s 31A in this agreement or one it continues, s 31B(1)(b)). Those 12 months end on {self.attrs._LDate}.",
        { cite: "ss 31A(2)(b)(ii), 31B(1)(b); IA ss 61(1)(b), 62", sev: "warn" }]
    ] },
    { id: "s31a-due-ok", on: "day", "for": "agreement", cite: "s 31A(1), (2)", "if": when("COk"), then: [].concat([
      ["set", S("prevRent"), S("rentNow")],
      ["set", S("rentNow"), S("chgRent")],
      ["set", S("lastChgDay"), "$day"],
      ["set", S("lastChgDate"), ["date", "$day"]]
    ], lastDayOfMonths("$self", ["+", "$day", 1], 12, S("lastChgL12")), [
      ["set", S("lastChgL12Date"), ["date", S("lastChgL12")]],
      ["log", "<b>The method of calculating the rent under {self} changes today</b> (s 31A(2)): the rent is now ${self.attrs.rentNow} a week. The next change may take effect from {self.attrs.lastChgL12Date}.",
        { cite: "s 31A(1), (2)", sev: "ok" }],
      ["observe", "change-effect"]
    ]) },
    { id: "s31a-due-no", on: "day", "for": "agreement", cite: "s 31A(1)", "if": when("CNo"), then: [
      ["log", "<b>The change of method under {self} has no effect</b>: 'otherwise the rent must not increase or be increased' (s 31A(1)). The rent stays at ${self.attrs.rentNow} a week.", { cite: "s 31A(1)", sev: "warn" }],
      ["observe", "change-no-effect"]
    ] },
    { id: "s31a-due-done", on: "day", "for": "agreement", cite: "s 31A(2)", "if": when("CDone"), then: [["set", S("chgPending"), false]]
      .concat(CHG_TEMPS.map(function (k) { return ["set", S(k), null]; }))
      .concat(Object.keys(CHG_FLAGS).concat(["CDone"]).map(function (k) { return ["set", when(k), null]; })) }
  ];

  /* ---- coming into existence ---- */
  var OFFER = ["any", "agreement", ["=", "$it.attrs.uid", "$self.attrs.renewalOf"]];
  function offered(k) { return ["attrOf", OFFER, k]; }
  var createRules = [
    { id: "person-arrives", on: "create:person", cite: "s 3 'party'", then: [
      ["set", S("name"), "$self.label"],
      ["set", S("tenancies"), ["if", ["exists", S("tenancies")], S("tenancies"), 0]]
    ] },
    { id: "premises-built", on: "create:premises", cite: "s 3 'residential premises'", then: [
      ["set", S("name"), "$self.label"],
      ["set", S("ownerId"), "$self.rels.owner"],
      ["set", S("occupied"), 0]
    ] },
    /* the simulation enters into a further agreement on an open offer: the parties, rent and start
       come from the offer (offerFurther) */
    { id: "enter-on-offer", on: "create:agreement", cite: "s 3 'residential tenancy agreement'", "if": S("renewal"), then: [
      ["set", S("renewalOf"), ["attrOf", ["any", "agreement", ["and", "$it.attrs.offerOpen", ["not", "$it.attrs.offerTaken"], ["<=", "$it.attrs.offerStart", "$day"]]], "uid"]],
      ["set", "$self.rels.premises", offered("premisesId")],
      ["set", "$self.rels.lessor", offered("lessorId")],
      ["set", "$self.rels.tenant", offered("tenantId")],
      ["set", "$self.rels.cotenant", offered("cotenantId")],
      ["set", S("kind"), offered("offerKind")],
      ["set", S("termMonths"), offered("offerMonths")],
      ["set", S("rent"), offered("offerRent")],
      ["set", S("bond"), ["*", 4, offered("offerRent")]],
      ["set", S("startsIn"), ["-", offered("offerStart"), "$day"]],
      ["set", S("motivatedByMatter"), offered("offerMotivated")],
      ["set", S("setOut"), false]
    ] },
    { id: "enter", on: "create:agreement", cite: "s 3 'residential tenancy agreement', 'expiry day'; s 3A; IA ss 61(1)(a), 62", then: [].concat([
      ["set", S("uid"), "$self.id"],
      ["set", S("name"), "$self.label"],
      ["set", "$self.rels.lessor", ["if", ["exists", "$self.rels.lessor"], "$self.rels.lessor", ["attrOf", ["rel", "$self", "premises"], "ownerId"]]],
      ["set", S("lessorId"), "$self.rels.lessor"],
      ["set", S("grantedById"), "$self.rels.lessor"],
      ["set", S("tenantId"), "$self.rels.tenant"],
      ["set", S("cotenantId"), "$self.rels.cotenant"],
      ["set", S("premisesId"), "$self.rels.premises"],
      ["set", S("lessorName"), ["attrOf", ["rel", "$self", "lessor"], "name"]],
      ["set", S("tenantName"), ["attrOf", ["rel", "$self", "tenant"], "name"]],
      ["set", S("cotenantName"), ["attrOf", ["rel", "$self", "cotenant"], "name"]],
      ["set", S("premisesName"), ["attrOf", ["rel", "$self", "premises"], "name"]],
      ["set", S("lessorSeenSale"), ["attrOf", ["rel", "$self", "premises"], "soldDay"]],
      ["set", S("kind"), ["if", ["=", S("kind"), "periodic"], "periodic", "fixed"]],
      ["set", S("termMonths"), num(S("termMonths"), 12)],
      ["set", S("rent"), num(S("rent"), 500)],
      ["set", S("rentNow"), S("rent")],
      ["set", S("bond"), ["if", ["exists", S("bond")], ["*", S("bond"), 1], ["*", 4, S("rent")]]],
      ["set", S("enteredDay"), "$day"],
      ["set", S("startDay"), ["+", "$day", ["if", ["exists", S("startsIn")], min(["*", S("startsIn"), 1], 0), 0]]],
      ["set", S("startDate"), ["date", S("startDay")]],
      ["set", S("chainStartDay"), S("startDay")],
      ["set", S("chainStartDate"), S("startDate")]
    ], lastDayOfMonths("$self", S("startDay"), S("termMonths"), S("_exp")), [
      ["set", S("expiryDay"), ["if", ["=", S("kind"), "fixed"], S("_exp"), null]],
      ["set", S("_exp"), null],
      ["set", S("fixedLastDay"), S("expiryDay")],
      ["set", S("expiryDate"), dateOf(S("expiryDay"))],
      ["set", S("fixedLastDate"), dateOf(S("fixedLastDay"))],
      ["set", S("s99"), ["and", ["=", S("kind"), "fixed"], ["<", S("enteredDay"), COMMENCEMENT], [">", S("expiryDay"), COMMENCEMENT]]]
    ], lastDayOfMonths("$self", ["+", S("startDay"), 1], 12, S("startL12")),
       lastDayOfMonths("$self", ["+", S("startDay"), 1], 6, S("startL6")), [
      ["set", S("startL12Date"), ["date", S("startL12")]],
      ["observe", "agreement-entered"]
    ]) },
    { id: "enter-fixed", on: "create:agreement", cite: "s 3 'expiry day'; IA ss 61(1)(a), 62", "if": ["=", S("kind"), "fixed"], then: [
      ["log", "<b>{self} is entered into</b>: {self.attrs.lessorName} lets {self.attrs.premisesName} to {self.attrs.tenantName} for a fixed term of {self.attrs.termMonths} months, from {self.attrs.startDate} to the expiry day, {self.attrs.expiryDate} (IA ss 61(1)(a), 62), at ${self.attrs.rent} a week.",
        { cite: "s 3 'residential tenancy agreement', 'expiry day'", sev: "ok" }]
    ] },
    { id: "enter-periodic", on: "create:agreement", cite: "s 3 'tenancy period'", "if": ["=", S("kind"), "periodic"], then: [
      ["log", "<b>{self} is entered into</b>: {self.attrs.lessorName} lets {self.attrs.premisesName} to {self.attrs.tenantName} as a periodic tenancy from {self.attrs.startDate}, at ${self.attrs.rent} a week.",
        { cite: "s 3 'residential tenancy agreement', 'tenancy period'", sev: "ok" }]
    ] },
    { id: "enter-cotenant", on: "create:agreement", cite: "s 3 'party' (a)", "if": ["exists", "$self.rels.cotenant"], then: [
      ["log", "{self.attrs.cotenantName} is a co-tenant (s 3 'party' (a)).", { cite: "s 3 'party'" }]
    ] },
    { id: "enter-income", on: "create:agreement", cite: "ss 30(1), 31A(1)", "if": S("incomeBased"), then: [
      ["log", "The rent under {self} is calculated by reference to the tenant's income: s 31A, not s 30, governs how it may change.", { cite: "ss 30(1), 31A(1)" }]
    ] },
    { id: "enter-s99", on: "create:agreement", cite: "s 99(2), (3)", "if": S("s99"), then: [
      ["log", "<b>s 99 applies to {self}</b>: a fixed term entered into before 29 July 2024 whose current term ends after that day. Section 30 as in force before 29 July 2024 (6 months; a form approved by the Minister) continues to apply to it until the end of the current term, {self.attrs.expiryDate} (s 99(3)).",
        { cite: "s 99(2), (3)", sev: "ok" }],
      ["observe", "s99-applies"]
    ] },
    { id: "enter-bond", on: "create:agreement", cite: "s 29(1)(b), (2); rr 10A, 11",
      "if": ["and", ["<=", S("rent"), 1200], [">", S("bond"), ["+", ["*", 4, S("rent")], ["if", S("petPermitted"), 350, 0]]]], then: [
      ["set", S("_bondMax"), ["+", ["*", 4, S("rent")], ["if", S("petPermitted"), 350, 0]]],
      ["log", "<b>s 29(1)(b): the bond is too large.</b> A security bond may not exceed 4 weeks' rent, plus $350 if a pet is permitted (r 10A): ${self.attrs._bondMax} here. {self} requires ${self.attrs.bond}, and requiring or receiving it is an offence. (The limit does not apply above $1,200 a week, s 29(2), r 11.)",
        { cite: "s 29(1)(b), (2); rr 10A, 11", sev: "stop" }],
      ["observe", "bond-over-limit"],
      ["set", S("_bondMax"), null]
    ] },
    { id: "enter-s82", on: "create:agreement", cite: "s 82(1)(a), (2); FK-01", "if": S("intentToEvade"), then: [
      ["log", "<b>s 82(2): an offence.</b> {self} was entered into with intent to defeat, evade or prevent the operation of the Act (a fact): maximum fine $10,000. It is not void under s 82(1)(a): on FK-01 reading A a rent fixed by a new agreement is not inconsistent with s 30 (encoding note N-28).",
        { cite: "s 82(1)(a), (2); FK-01", sev: "stop" }],
      ["observe", "s82-offence"]
    ] },
    { id: "enter-fk11", on: "create:agreement", cite: "s 26A(a)(ii), (iv); FK-11", "if": S("motivatedByMatter"), then: [
      ["log", "The lessor fixed {self}'s rent higher because of a matter in s 26B(2) (a fact). That is not retaliatory action on FK-11 reading A (taken): s 26A(a)(ii) speaks of increasing 'the rent payable under the residential tenancy agreement' the tenant holds, and (iv) reaches only a refusal of a further agreement, not an offer of one on harder terms. On reading B it is an increase within (ii) (encoding note N-08).",
        { cite: "s 26A(a)(ii), (iv); FK-11", sev: "warn" }],
      ["observe", "renewal-not-retaliatory"]
    ] }
  ];

  /* ---- every day: bookkeeping the simulation reads (no provision), and the clock's own rules ----
     The counts are kept only for the people, premises and agreements a generated run made
     (`simulated`), so that a scenario does not pay for them. */
  var bookkeeping = [
    { id: "count-tenancies", on: "day", "for": "person", cite: "simulation bookkeeping (no provision)", "if": S("seeker"), then: [
      ["set", S("tenancies"), ["count", "agreement", ["and", ["not", "$it.attrs.ended"], ["not", "$it.attrs.superseded"],
        ["or", ["=", "$it.rels.tenant", "$self.id"], ["=", "$it.rels.cotenant", "$self.id"]]]]]
    ] },
    { id: "count-occupation", on: "day", "for": "premises", cite: "simulation bookkeeping (no provision)", "if": S("simulated"), then: [
      ["set", S("occupied"), ["count", "agreement", ["and", ["=", "$it.rels.premises", "$self.id"],
        ["or", ["and", ["not", "$it.attrs.ended"], ["not", "$it.attrs.superseded"]], ["and", "$it.attrs.offerOpen", ["not", "$it.attrs.offerTaken"]]]]]]
    ] },
    { id: "note-superseded", on: "day", "for": "agreement", cite: "simulation bookkeeping (no provision)",
      "if": ["and", S("simulated"), S("commenced"), ["not", S("ended")], ["not", S("superseded")]], then: [
      ["set", S("superseded"), [">", ["count", "agreement", ["and", ["!=", "$it.id", "$self.id"], "$it.attrs.commenced",
        ["=", "$it.rels.premises", "$self.rels.premises"], [">", "$it.attrs.startDay", "$self.attrs.startDay"]]], 0]]
    ] },
    { id: "note-offer-taken", on: "day", "for": "agreement", cite: "simulation bookkeeping (no provision)",
      "if": ["and", S("offerOpen"), ["not", S("offerTaken")]], then: [
      ["set", S("offerTaken"), [">", ["count", "agreement", ["=", "$it.attrs.renewalOf", "$self.attrs.uid"]], 0]]
    ] },
    { id: "s3-successor-lessor", on: "day", "for": "agreement", cite: "s 3 'lessor'; FK-13",
      "if": ["and", ["not", S("ended")], ["exists", ["attrOf", ["rel", "$self", "premises"], "soldDay"]],
             ["!=", S("lessorSeenSale"), ["attrOf", ["rel", "$self", "premises"], "soldDay"]]], then: [
      ["set", S("lessorSeenSale"), ["attrOf", ["rel", "$self", "premises"], "soldDay"]],
      ["set", S("_oldName"), S("lessorName")],
      ["set", "$self.rels.lessor", ["attrOf", ["rel", "$self", "premises"], "ownerId"]],
      ["set", S("lessorId"), "$self.rels.lessor"],
      ["set", S("lessorName"), ["attrOf", ["rel", "$self", "lessor"], "name"]],
      ["log", "<b>{self.attrs.lessorName} becomes the lessor under {self}</b>, having bought the premises from {self.attrs._oldName}: 'lessor' includes a successor or assignee of a lessor (s 3). The agreement continues. For s 31B(3)(a), the lessor under {self} at its end is now {self.attrs.lessorName} (FK-13 reading A).",
        { cite: "s 3 'lessor'; FK-13", sev: "ok" }],
      ["observe", "successor-lessor"],
      ["set", S("_oldName"), null]
    ] }
  ];

  var clockRules = [
    { id: "s76c", on: "day", "for": "agreement", cite: "s 76C(1), (2); FK-09; FK-19",
      "if": ["and", ["=", S("kind"), "fixed"], S("commenced"), ["not", S("ended")], ["not", S("periodic76C")], ["=", "$day", ["+", S("fixedLastDay"), 1]]],
      then: [].concat([
        ["set", S("periodic76C"), true],
        ["set", S("periodicFrom"), "$day"],
        ["set", S("periodicFromDate"), ["date", "$day"]]
      ], lastDayOfMonths("$self", ["+", "$day", 1], 12, S("p76L12")), [
        ["set", S("p76L12Date"), ["date", S("p76L12")]],
        ["log", "<b>{self} continues as a periodic tenancy</b> from today, on the same terms (s 76C(2)): its fixed term ended on {self.attrs.fixedLastDate} and it had not terminated (s 76C(1); FK-09 reading A). It is the same agreement, and its parties, rent and rent history carry on (FK-19 reading A).",
          { cite: "s 76C(1), (2); FK-09; FK-19", sev: "ok" }],
        ["observe", "s76c"]
      ]) },
    { id: "s76c-holding-over", on: "day", "for": "agreement", cite: "ss 60(1)(b), 70A(5), 76C(1); FK-09",
      "if": ["and", S("periodic76C"), ["=", S("periodicFrom"), "$day"], ["exists", S("possDay70A")]], then: [
      ["log", "A notice under s 70A named {self.attrs.possDate70A} as the possession day, and the tenant has not delivered up possession. The agreement has not terminated (s 60(1)(b) needs possession delivered up, or an order under s 72, which is outside this run's scope), so on the encoding's reading s 76C continues it: FK-09 A asks only whether it terminated by the end of the fixed term.",
        { cite: "ss 60(1)(b), 70A, 76C(1); FK-09", sev: "warn" }],
      ["observe", "holding-over"]
    ] }
  ];

  var laterDayRules = [
    { id: "s31-bond-payable", on: "day", "for": "agreement", cite: "s 31(3)", "if": ["and", S("bondPending"), ["=", "$day", S("bondPayDay")], ["not", S("ended")]], then: [
      ["set", S("bond"), ["+", S("bond"), S("bondAdd")]],
      ["set", S("bondPending"), false],
      ["log", "The additional ${self.attrs.bondAdd} of security bond under {self} is payable today (s 31(3)): the bond is now ${self.attrs.bond}.", { cite: "s 31(1A), (3)", sev: "ok" }],
      ["observe", "bond-increase"]
    ] },
    { id: "s32-period-ends", on: "day", "for": "agreement", cite: "s 32(5)",
      "if": ["and", ["exists", S("orderMade")], ["not", S("orderLapsed")], ["not", S("ended")], ["=", "$day", ["+", S("orderEnd"), 1]]], then: [
      ["set", S("orderLapsed"), true],
      ["log", "The period of the order under s 32 for {self} ended yesterday, {self.attrs.orderEndDate} (6 months at most, beginning on the day it was made: IA ss 61(1)(a), 62). It no longer has effect (s 32(5)); the rent payable is again ${self.attrs.rentNow} a week.",
        { cite: "s 32(5); IA ss 61(1)(a), 62", sev: "ok" }],
      ["observe", "s32-lapse"]
    ] },
    { id: "s71-order-operates", on: "day", "for": "agreement", cite: "ss 60(1)(a)(ii), 64(4)(c)",
      "if": ["and", ["exists", S("courtTermDay")], ["=", "$day", S("courtTermDay")], ["not", S("ended")]], then: [].concat(terminate("$self", "an order for possession (s 60(1)(a)(ii))"), [
      ["log", "<b>{self} terminates today</b>: the court's order for possession operates (ss 60(1)(a)(ii), 64(4)(c)).", { cite: "ss 60(1)(a)(ii), 64(4)(c), 71", sev: "ok" }],
      ["observe", "terminated"]
    ]) },
    { id: "s60-no-tenant-left", on: "day", "for": "agreement", cite: "s 60(1)(i)",
      "if": ["and", S("commenced"), ["not", S("ended")], ["not", ["exists", "$self.rels.tenant"]], ["not", ["exists", "$self.rels.cotenant"]]], then: [].concat(terminate("$self", "no tenant left (s 60(1)(i))"), [
      ["log", "<b>{self} terminates</b>: it has no tenant left (every tenant has died, s 60(1)(i), or has been taken out of the cast).", { cite: "s 60(1)(i)", sev: "ok" }],
      ["observe", "terminated"]
    ]) }
  ];

  /* ---- what people do ---- */
  function voidRule(id, action, cond, text, cite) {
    return { id: id, on: "action:" + action, cite: cite, "if": cond, then: [
      ["log", "<b>Nothing has happened.</b> " + text, { cite: cite, sev: "ok" }],
      ["observe", "void-act"]
    ] };
  }
  var ENDED_T = ["and", T("ended")];

  var actionRules = [].concat(
    /* s 30: notice of increase */
    [
      voidRule("s30-not-lessor", "noticeIncrease", ["not", IS_LESSOR], "Section 30(1) lets the lessor increase the rent by notice to the tenant (or a property manager acting for the lessor, s 86B). {self} is not the lessor under {target}.", "s 30(1); s 86B"),
      voidRule("s30-ended", "noticeIncrease", ["and", IS_LESSOR, T("ended")], "{target} terminated on {target.attrs.endedDate}: there is no agreement left for a notice to vary (s 30(3)).", "ss 30(3), 60"),
      { id: "s30-replaces", on: "action:noticeIncrease", cite: "s 30(3)", "if": ["and", IS_LESSOR, LIVE, T("incPending")], then: [
        ["log", "A notice of increase under {target}, for {target.attrs.incEffectDate}, is still pending. The console holds one notice of increase at a time, so the lessor is taken to withdraw it (s 30(3)).", { cite: "s 30(3)" }]
      ] },
      { id: "s30-give", on: "action:noticeIncrease", cite: "ss 30(1), 85", "if": ["and", IS_LESSOR, LIVE], then: [].concat(refresh("$target"), [
        ["set", T("incPending"), true],
        ["set", T("incSent"), "$day"],
        ["set", T("incHow"), ["if", ["exists", "$p.how"], "$p.how", "personally"]],
        ["set", T("incGiven"), ["if", ["=", T("incHow"), "email"], null, ["if", ["=", T("incHow"), "post"], ["+", "$day", num("$p.postDays", 0)], "$day"]]],
        ["set", T("incGivenDate"), dateOf(T("incGiven"))],
        ["set", T("incForm"), ["if", ["exists", "$p.form"], "$p.form", "s88c"]],
        ["set", T("incRent"), num("$p.rent", ["+", T("rentNow"), 50])],
        ["set", T("incMotivated"), ["if", "$p.motivated", true, false]]
      ], s30Earliest("$target", ["if", ["exists", T("incGiven")], T("incGiven"), "$day"]), [
        ["set", T("incEffect"), ["if", [">", ["*", "$p.inDays", 1], 0], ["+", "$day", ["*", "$p.inDays", 1]], T("incEarliest")]],
        ["set", T("incEffectDate"), ["date", T("incEffect")]],
        ["set", T("noticeReceivedDay"), T("incGiven")],
        ["set", T("rentNoticeDay"), T("incGiven")],
        ["set", T("rentNoticeKind"), "s30"],
        ["set", T("rentNoticeUp"), true],
        ["set", T("rentNoticeEffect"), T("incEffect")],
        ["observe", "inc-notice"]
      ]) },
      { id: "s30-give-log", on: "action:noticeIncrease", cite: "ss 30(1), 85; IA s 61(1)(f)", "if": ["and", IS_LESSOR, LIVE, ["exists", T("incGiven")]], then: [
        ["log", "The notice says the rent is to be ${target.attrs.incRent} a week from {target.attrs.incEffectDate}. It is given on {target.attrs.incGivenDate} (s 85), and for a notice given that day the earliest day s 30(1) allows is {target.attrs.incEarliestDate}. Whether the increase takes effect is decided on the day it names.",
          { cite: "ss 30(1), 85; IA s 61(1)(f)" }]
      ] },
      emailed("noticeIncrease", "notice of increase")
    ],
    retaliation("noticeIncrease", "increase", "gave notice increasing the rent payable under the agreement", "(ii)"),
    [
      voidRule("s30-withdraw-nothing", "withdrawIncrease", ["not", ["and", IS_LESSOR, LIVE, T("incPending")]], "There is no pending notice of increase by {self} under {target} to withdraw.", "s 30(3)"),
      { id: "s30-withdraw", on: "action:withdrawIncrease", cite: "s 30(3)", "if": ["and", IS_LESSOR, LIVE, T("incPending")], then: [
        ["set", T("incPending"), false],
        ["log", "The notice of increase under {target}, for {target.attrs.incEffectDate}, is withdrawn: a withdrawn notice does not vary the agreement (s 30(3)).", { cite: "s 30(3)", sev: "ok" }],
        ["observe", "inc-withdrawn"]
      ] }
    ],
    /* s 31A: change of method */
    [
      voidRule("s31a-not-lessor", "noticeChange", ["not", IS_LESSOR], "Section 31A(1) lets the lessor change the method of calculating income-based rent. {self} is not the lessor under {target}.", "s 31A(1)"),
      voidRule("s31a-ended", "noticeChange", ["and", IS_LESSOR, T("ended")], "{target} terminated on {target.attrs.endedDate}.", "ss 31A, 60"),
      { id: "s31a-give", on: "action:noticeChange", cite: "s 31A(2); s 85", "if": ["and", IS_LESSOR, LIVE], then: [].concat(refresh("$target"), [
        ["set", T("chgPending"), true],
        ["set", T("chgGiven"), ["if", "$p.email", null, "$day"]],
        ["set", T("chgGivenDate"), dateOf(T("chgGiven"))],
        ["set", T("chgRent"), num("$p.rent", ["+", T("rentNow"), 20])],
        ["set", T("_L"), ["if", ["exists", T("lastChgDay")], T("lastChgL12"), T("startL12")]],
        ["set", T("chgEarliest"), max(["+", "$day", 61], T("_L"))],
        ["set", T("_L"), null],
        ["set", T("chgEffect"), ["if", [">", ["*", "$p.inDays", 1], 0], ["+", "$day", ["*", "$p.inDays", 1]], T("chgEarliest")]],
        ["set", T("chgEffectDate"), ["date", T("chgEffect")]],
        ["set", T("chgEarliestDate"), ["date", T("chgEarliest")]],
        ["set", T("chgUpReceivedDay"), ["if", [">", T("chgRent"), T("rentNow")], T("chgGiven"), null]],
        ["set", T("rentNoticeKind"), "s31A"],
        ["set", T("rentNoticeUp"), [">", T("chgRent"), T("rentNow")]],
        ["set", T("rentNoticeDay"), T("chgGiven")],
        ["set", T("rentNoticeEffect"), T("chgEffect")],
        ["observe", "change-notice"]
      ]) },
      { id: "s31a-give-log", on: "action:noticeChange", cite: "s 31A(2)", "if": ["and", IS_LESSOR, LIVE, ["exists", T("chgGiven")]], then: [
        ["log", "The notice specifies a change to the method, giving ${target.attrs.chgRent} a week, from {target.attrs.chgEffectDate}. For a notice given today the earliest day s 31A(2)(b) allows is {target.attrs.chgEarliestDate}.",
          { cite: "s 31A(2)(b); IA ss 61, 62" }]
      ] },
      { id: "s31a-fixed-rent", on: "action:noticeChange", cite: "ss 30(1), 31A(1)", "if": ["and", IS_LESSOR, LIVE, ["not", T("incomeBased")]], then: [
        ["log", "{target}'s rent is a fixed amount, not calculated by reference to the tenant's income: s 31A does not apply to it.", { cite: "s 31A(1)", sev: "warn" }]
      ] },
      emailed("noticeChange", "notice of a change of method")
    ],
    /* s 31: security bond */
    [
      voidRule("s31-not-lessor", "increaseBond", ["not", IS_LESSOR], "Section 31(1A) lets the lessor increase the bond. {self} is not the lessor under {target}.", "s 31(1A)"),
      voidRule("s31-ended", "increaseBond", ["and", IS_LESSOR, T("ended")], "{target} terminated on {target.attrs.endedDate}.", "ss 31, 60"),
      { id: "s31-prepare", on: "action:increaseBond", cite: "s 31(1A), (1B), (2); r 5CB; FK-25", "if": ["and", IS_LESSOR, LIVE], then: [
        ["set", T("_ev"), ["exists", T("rentNoticeDay")]],
        ["set", T("_pay"), ["if", [">", ["*", "$p.inDays", 1], 0], ["+", "$day", ["*", "$p.inDays", 1]],
                           max(["+", "$day", 60], ["if", ["exists", T("rentNoticeEffect")], T("rentNoticeEffect"), 0])]],
        ["set", T("_rentThen"), ["if", ["and", T("incPending"), ["<=", T("incEffect"), T("_pay")]], T("incRent"),
                                ["if", ["and", T("chgPending"), ["<=", T("chgEffect"), T("_pay")]], T("chgRent"), T("rentNow")]]],
        ["set", T("_cap"), ["+", ["*", 4, T("_rentThen")], ["if", T("petPermitted"), 350, 0]]],
        ["set", T("_add"), num("$p.amount", ["-", T("_cap"), T("bond")])],
        ["set", T("_ok1a"), [">=", T("_pay"), ["+", "$day", 60]]],
        ["set", T("_ok1b"), ["or", ["not", ["exists", T("rentNoticeEffect")]], [">=", T("_pay"), T("rentNoticeEffect")]]],
        ["set", T("_ok2"), ["<=", ["+", T("bond"), T("_add")], T("_cap")]],
        ["set", T("_payDate"), ["date", T("_pay")]],
        ["set", T("_bondOk"), ["and", T("_ev"), T("_ok1a"), T("_ok1b"), T("_ok2"), [">", T("_add"), 0]]]
      ] },
      { id: "s31-no-event", on: "action:increaseBond", cite: "s 31(1), (1A); r 5CB; s 29(1)(b)", "if": ["and", IS_LESSOR, LIVE, ["not", T("_ev")]], then: [
        ["log", "<b>The bond cannot be increased.</b> It 'can only be increased in accordance with' s 31 (s 31(1)), which needs a notice of increase of rent under s 30 or 31A (or, under r 5CB, a pet approved). None has been given under {target}. A rent fixed by a new agreement is no such notice; a new agreement takes its own bond under s 29 at its own rent (encoding note N-01).",
          { cite: "s 31(1), (1A); r 5CB; s 29(1)(b)", sev: "warn" }],
        ["observe", "bond-no-event"]
      ] },
      { id: "s31-too-early", on: "action:increaseBond", cite: "s 31(1B)(a); IA s 61(1)(b)", "if": ["and", IS_LESSOR, LIVE, T("_ev"), ["not", T("_ok1a")]], then: [
        ["log", "s 31(1B)(a): the additional amount cannot be payable 'earlier than 60 days after' the bond notice is given; {target.attrs._payDate} is too early.", { cite: "s 31(1B)(a)", sev: "warn" }]
      ] },
      { id: "s31-before-rent", on: "action:increaseBond", cite: "s 31(1B)(b); r 5CB(c)", "if": ["and", IS_LESSOR, LIVE, T("_ev"), ["not", T("_ok1b")]], then: [
        ["log", "s 31(1B)(b), as r 5CB(c) modifies it: the additional amount cannot be payable before the rent increase that is the subject of the rent notice takes effect.", { cite: "s 31(1B)(b); r 5CB", sev: "warn" }]
      ] },
      { id: "s31-over-cap", on: "action:increaseBond", cite: "s 31(2); r 10A", "if": ["and", IS_LESSOR, LIVE, T("_ev"), ["not", T("_ok2")]], then: [
        ["log", "s 31(2): the bond may not be increased past 4 weeks' rent at the time the additional amount is payable (${target.attrs._rentThen} a week), plus $350 if a pet is permitted: ${target.attrs._cap} in all.", { cite: "s 31(2)", sev: "warn" }]
      ] },
      { id: "s31-no-effect", on: "action:increaseBond", cite: "s 31(1)", "if": ["and", IS_LESSOR, LIVE, T("_ev"), ["not", T("_bondOk")]], then: [
        ["log", "The bond notice is not one given in accordance with s 31, and does not vary the agreement (s 31(3)).", { cite: "s 31(1), (3)", sev: "warn" }],
        ["observe", "bond-no-effect"]
      ] },
      { id: "s31-given", on: "action:increaseBond", cite: "s 31(1A), (3); FK-25", "if": ["and", IS_LESSOR, LIVE, T("_bondOk")], then: [
        ["set", T("bondPending"), true],
        ["set", T("bondAdd"), T("_add")],
        ["set", T("bondPayDay"), T("_pay")],
        ["log", "The bond notice is good: ${target.attrs.bondAdd} more, payable on {target.attrs._payDate} (s 31(1A), (1B), (2)).",
          { cite: "s 31(1A), (1B), (2)", sev: "ok" }]
      ] },
      { id: "s31-fk25", on: "action:increaseBond", cite: "s 31(1A); r 5CB; FK-25", "if": ["and", IS_LESSOR, LIVE, T("_bondOk"), ["=", T("rentNoticeKind"), "s31A"], ["not", T("rentNoticeUp")]], then: [
        ["log", "This turns on FK-25. The rent notice behind the bond increase is a notice under s 31A whose change does not raise the rent. Reading A (taken): every notice under s 31A is a 'notice of increase in rent' for s 31(1A), so the bond may rise (within s 31(2)). On reading B only a change that raises the rent is one, and the bond could not rise (encoding note N-23).",
          { cite: "s 31(1A); r 5CB(1AA)(a); FK-25", sev: "ok" }],
        ["observe", "fk25"]
      ] },
      { id: "s31-sixtieth-day", on: "action:increaseBond", cite: "s 31(1B)(a); s 30(1)(a); IA s 61(1)(b), (f); FK-06", "if": ["and", IS_LESSOR, LIVE, T("_bondOk"), ["=", T("_pay"), ["+", "$day", 60]]], then: [
        ["log", "The additional amount is payable on the 60th day after the bond notice: s 31(1B)(a) says 'earlier than 60 days after', counted under IA s 61(1)(b), so that day is allowed. A rent increase noticed the same day could take effect no earlier than the day after, s 30(1)(a)'s 'not less than 60 days' being counted under s 61(1)(f) (FK-06 reading A; encoding note N-14).",
          { cite: "ss 30(1)(a), 31(1B)(a); IA s 61(1)(b), (f); FK-06", sev: "warn" }],
        ["observe", "bond-60th-day"]
      ] },
      { id: "s31-tidy", on: "action:increaseBond", cite: "s 31", "if": ["and", IS_LESSOR, LIVE], then:
        ["_ev", "_pay", "_rentThen", "_cap", "_add", "_ok1a", "_ok1b", "_ok2", "_payDate", "_bondOk"].map(function (k) { return ["set", T(k), null]; }) }
    ],
    /* s 64: notice of termination without a ground */
    [
      voidRule("s64-not-lessor", "give64", ["not", IS_LESSOR], "Section 64(1) lets the lessor give notice of termination without a ground. {self} is not the lessor under {target}.", "s 64(1)"),
      voidRule("s64-ended", "give64", ["and", IS_LESSOR, T("ended")], "{target} terminated on {target.attrs.endedDate}.", "ss 60, 64"),
      emailed("give64", "notice of termination"),
      { id: "s64-prepare", on: "action:give64", cite: "s 64(2), (5); s 65(1)(a)", "if": ["and", IS_LESSOR, LIVE, ["not", "$p.email"]], then: [
        ["set", T("_p"), ["+", "$day", num("$p.inDays", 61)]],
        ["set", T("_pDate"), ["date", T("_p")]],
        ["set", T("_inFixed"), ["def", "inFixedTerm"]],
        ["set", T("_short"), ["<", T("_p"), ["+", "$day", 61]]],
        ["set", T("_ineff"), ["def", "s65Bites"]],
        ["set", T("_ok64"), ["and", ["not", T("_inFixed")], ["not", T("_short")], ["not", T("_ineff")]]]
      ] },
      { id: "s64-fixed-term", on: "action:give64", cite: "s 64(5); FK-10", "if": ["and", IS_LESSOR, LIVE, ["not", "$p.email"], T("_inFixed")], then: [
        ["log", "<b>Not a notice under s 64.</b> The section 'does not apply in relation to a residential tenancy agreement that creates a tenancy for a fixed term during the currency of that term' (s 64(5)), and {target}'s fixed term runs to {target.attrs.fixedLastDate} (FK-10 reading A where a notice under s 70A moved it).",
          { cite: "s 64(5); FK-10", sev: "warn" }],
        ["observe", "s64-fixed-term"]
      ] },
      { id: "s64-short", on: "action:give64", cite: "s 64(2); IA s 61(1)(f); FK-06", "if": ["and", IS_LESSOR, LIVE, ["not", "$p.email"], ["not", T("_inFixed")], T("_short")], then: [
        ["log", "<b>Not a notice under s 64.</b> The period of notice must be not less than 60 days before the possession day (s 64(2)): 60 clear days (IA s 61(1)(f); FK-06 reading A). {target.attrs._pDate} is too soon.",
          { cite: "s 64(2); IA s 61(1)(f); FK-06", sev: "warn" }],
        ["observe", "s64-short"]
      ] },
      { id: "s64-fk06", on: "action:give64", cite: "s 64(2); FK-06", "if": ["and", IS_LESSOR, LIVE, ["not", "$p.email"], ["not", T("_inFixed")], ["=", T("_p"), ["+", "$day", 60]]], then: [
        ["log", "This turns on FK-06: the possession day is the 60th day after the notice. Counted under IA s 61(1)(b) alone (reading B) that is enough.", { cite: "s 64(2); FK-06", sev: "warn" }],
        ["observe", "fk06"]
      ] },
      { id: "s64-s65", on: "action:give64", cite: "s 65(1)(a)", "if": ["and", IS_LESSOR, LIVE, ["not", "$p.email"], ["not", T("_inFixed")], ["not", T("_short")], T("_ineff")], then: [
        ["log", "<b>The notice is ineffectual.</b> Proceedings for an order under s 32 fixing the maximum rent are pending, or such an order is in force, and 'any notice of termination of the agreement given by the lessor under section 64 is ineffectual' (s 65(1)(a)).",
          { cite: "s 65(1)(a)", sev: "warn" }],
        ["observe", "s64-ineffectual"]
      ] },
      { id: "s64-given", on: "action:give64", cite: "s 64(1)-(3)", "if": ["and", IS_LESSOR, LIVE, ["not", "$p.email"], T("_ok64")], then: [
        ["set", T("n64Pending"), true],
        ["set", T("n64Given"), "$day"],
        ["set", T("n64Received"), "$day"],
        ["set", T("n64Day"), T("_p")],
        ["set", T("n64Date"), T("_pDate")],
        ["set", T("n64ApplyBy"), openDay(["+", "$day", 7])],
        ["set", T("n64ApplyByDate"), ["date", T("n64ApplyBy")]],
        ["log", "A notice of termination under s 64: the tenant is to give possession on {target.attrs.n64Date}. The tenant may, within 7 days after receiving it (to {target.attrs.n64ApplyByDate}, IA s 61(1)(e)), apply to a competent court for a further period of up to 60 days (s 64(3)), and may also apply under s 26B if the tenant believes it was retaliatory action (the note to s 64(3)).",
          { cite: "s 64(1)-(3)", sev: "ok" }],
        ["observe", "s64-notice"]
      ] },
      { id: "s64-tidy", on: "action:give64", cite: "s 64", "if": ["and", IS_LESSOR, LIVE], then:
        ["_p", "_pDate", "_inFixed", "_short", "_ineff", "_ok64"].map(function (k) { return ["set", T(k), null]; }) }
    ],
    retaliation("give64", "s64", "gave notice of termination without a ground (action to terminate the agreement)", "(iii)"),
    /* s 70A: notice at the end of a fixed term */
    [
      voidRule("s70a-not-party", "give70A", ["not", ["or", IS_LESSOR, IS_TENANT]], "Section 70A(2) speaks of a notice given by 'the lessor or tenant' to the other. {self} is neither under {target}.", "s 70A(2)"),
      voidRule("s70a-ended", "give70A", ["and", ["or", IS_LESSOR, IS_TENANT], T("ended")], "{target} terminated on {target.attrs.endedDate}.", "ss 60, 70A"),
      voidRule("s70a-periodic", "give70A", ["and", ["or", IS_LESSOR, IS_TENANT], LIVE, ["=", T("kind"), "periodic"]], "Section 70A applies only to 'a residential tenancy agreement that creates a tenancy for a fixed term' (s 70A(1)); {target} is a periodic tenancy, which the lessor ends under s 64 and the tenant under s 68.", "s 70A(1)"),
      { id: "s70a-after-term", on: "action:give70A", cite: "ss 70A(2), 76C(2)", "if": ["and", ["or", IS_LESSOR, IS_TENANT], LIVE, ["=", T("kind"), "fixed"], T("periodic76C")], then: [
        ["log", "{target}'s fixed term ended on {target.attrs.fixedLastDate}, and it continues as a periodic tenancy (s 76C(2)). Section 70A(2) speaks of whether the term ends on the expiry day, which has passed, so the console does not apply this as a notice under s 70A. The encoding tests only s 70A(1), (3) and (4), which do not say when the notice must be given, and would accept it.",
          { cite: "ss 70A(1)-(4), 76C(2)", sev: "warn" }],
        ["observe", "s70a-after-term"]
      ] },
      emailed("give70A", "notice under s 70A"),
      { id: "s70a-prepare", on: "action:give70A", cite: "s 70A(3), (4); IA s 61(1)(h); FK-08", "if": ["and", ["or", IS_LESSOR, IS_TENANT], LIVE, ["=", T("kind"), "fixed"], ["not", T("periodic76C")], ["not", "$p.email"]], then: [
        ["set", T("_p"), ["if", [">", ["*", "$p.inDays", 1], 0], ["+", "$day", ["*", "$p.inDays", 1]], T("expiryDay")]],
        ["set", T("_pDate"), ["date", T("_p")]],
        ["set", T("_last"), openDay(["-", T("_p"), 30])],
        ["set", T("_lastDate"), ["date", T("_last")]],
        ["set", T("_late"), [">", "$day", T("_last")]],
        ["set", T("_early"), ["<", T("_p"), T("expiryDay")]],
        ["set", T("_byLessor"), IS_LESSOR],
        ["set", T("_ineff"), ["and", T("_byLessor"), ["def", "s65Bites"], ["not", T("s65Authorised")]]],
        ["set", T("_ok70"), ["and", ["not", T("_late")], ["not", T("_early")], ["not", T("_ineff")]]],
        ["set", T("_live70"), true]
      ] },
      { id: "s70a-early", on: "action:give70A", cite: "s 70A(4)", "if": ["and", T("_live70"), T("_early")], then: [
        ["log", "<b>Not a notice under s 70A.</b> 'The possession day must not be a day earlier than the expiry day' (s 70A(4)); {target.attrs._pDate} is before {target.attrs.expiryDate}.", { cite: "s 70A(4)", sev: "warn" }],
        ["observe", "s70a-invalid"]
      ] },
      { id: "s70a-late", on: "action:give70A", cite: "s 70A(3); FK-07; IA s 61(1)(c), (h)", "if": ["and", T("_live70"), ["not", T("_early")], T("_late")], then: [
        ["log", "<b>Given too late.</b> 'The notice must be given not later than 30 days before the possession day' (s 70A(3)): by {target.attrs._lastDate} for possession on {target.attrs._pDate}. A late notice is not a notice under s 70A at all (FK-07 reading A), so the term does not end on the expiry day (s 70A(2)) and s 76C will continue the agreement. On reading B the notice would operate from the first day for which it was in time. The section states no consequence (encoding note N-17).",
          { cite: "s 70A(2), (3); FK-07", sev: "warn" }],
        ["observe", "s70a-late"]
      ] },
      { id: "s70a-excluded-day", on: "action:give70A", cite: "s 70A(3); IA s 61(1)(h); FK-08", "if": ["and", T("_live70"), T("_ok70"), [">", "$day", ["-", T("_p"), 30]]], then: [
        ["log", "In time only because the 30th day before the possession day was a Saturday or Sunday: IA s 61(1)(h) lets an act directed to be done on or before an excluded day be done on the next day that is not (FK-08 reading A). The tenant gets fewer than 30 days' notice. On reading B s 70A(3) shows a contrary intention and the notice is late (encoding note N-16).",
          { cite: "s 70A(3); IA s 61(1)(h); FK-08", sev: "warn" }],
        ["observe", "s70a-excluded-day"]
      ] },
      { id: "s70a-form-30", on: "action:give70A", cite: "s 70A(3); r 18, Sch 4 Form 1C; IA s 61(1)(f)", "if": ["and", T("_live70"), T("_ok70"), ["=", "$day", ["-", T("_p"), 30]]], then: [
        ["log", "Given exactly 30 days before the possession day, the last day s 70A(3) allows. The prescribed form (Form 1C, item 5) calls the notice one 'of NOT LESS THAN 30 DAYS', which counted under IA s 61(1)(f) needs 30 clear days: one day more than the section asks (encoding note N-15).",
          { cite: "s 70A(3); Form 1C; IA s 61(1)(f)", sev: "warn" }],
        ["observe", "s70a-form-30"]
      ] },
      { id: "s70a-s65", on: "action:give70A", cite: "s 65(1)(b), (2)", "if": ["and", T("_live70"), ["not", T("_late")], ["not", T("_early")], T("_ineff")], then: [
        ["log", "<b>The notice is ineffectual.</b> While proceedings under s 32 are pending or an order is in force, any notice of termination by the lessor other than under s 64 is ineffectual unless first authorised by a competent court (s 65(1)(b), (2)).",
          { cite: "s 65(1)(b), (2)", sev: "warn" }],
        ["observe", "s65-other-notice"]
      ] },
      { id: "s70a-given", on: "action:give70A", cite: "s 70A(1)-(6)", "if": ["and", T("_live70"), T("_ok70")], then: [
        ["set", T("n70L"), ["if", T("_byLessor"), T("_p"), T("n70L")]],
        ["set", T("n70T"), ["if", T("_byLessor"), T("n70T"), T("_p")]],
        ["set", T("possDay70A"), ["if", ["and", ["exists", T("n70L")], ["exists", T("n70T")]], min(T("n70L"), T("n70T")), ["if", ["exists", T("n70L")], T("n70L"), T("n70T")]]],
        ["set", T("possBy"), ["if", ["and", ["exists", T("n70L")], ["=", T("possDay70A"), T("n70L")]], "lessor", "tenant"]],
        ["set", T("possDate70A"), ["date", T("possDay70A")]],
        ["set", T("fixedLastDay"), max(T("expiryDay"), T("possDay70A"))],
        ["set", T("fixedLastDate"), ["date", T("fixedLastDay")]],
        ["log", "A notice under s 70A, with {target.attrs._pDate} as the possession day. The term of {target} ends on the expiry day only because of such a notice (s 70A(2)); the possession day is {target.attrs.possDate70A} (s 70A(1), (6)). If the tenant delivers up possession on or after it, the agreement terminates (s 60(1)(b)(i)).",
          { cite: "s 70A(1)-(6); s 60(1)(b)", sev: "ok" }],
        ["observe", "s70a-notice"]
      ] },
      { id: "s70a-extends", on: "action:give70A", cite: "s 70A(5); FK-10", "if": ["and", T("_live70"), T("_ok70"), [">", T("possDay70A"), T("expiryDay")]], then: [
        ["log", "The possession day is later than the expiry day ({target.attrs.expiryDate}), so 'the term of the agreement expires on the possession day' and its terms are varied 'for all purposes' (s 70A(5)): {target} is a fixed term until {target.attrs.fixedLastDate} (FK-10 reading A). On reading B it would become a periodic tenancy after the expiry day (s 76C(2)), which the notice ends on the possession day (encoding note N-18).",
          { cite: "s 70A(5); s 76C(2); FK-10", sev: "ok" }],
        ["observe", "s70a-extends"]
      ] },
      { id: "s70a-tidy", on: "action:give70A", cite: "s 70A", "if": T("_live70"), then:
        ["_p", "_pDate", "_last", "_lastDate", "_late", "_early", "_byLessor", "_ineff", "_ok70", "_live70"].map(function (k) { return ["set", T(k), null]; }) }
    ],
    retaliation("give70A", "s70a", "gave notice under s 70A ending the fixed term (action to terminate the agreement)", "(iii)"),
    /* further agreements */
    [
      voidRule("offer-not-lessor", "offerFurther", ["not", IS_LESSOR], "Only the lessor under {target} can offer its tenant a further agreement as lessor; {self} is not.", "s 3 'lessor'"),
      voidRule("offer-ended", "offerFurther", ["and", IS_LESSOR, T("ended")], "{target} terminated on {target.attrs.endedDate}.", "s 60"),
      { id: "offer-made", on: "action:offerFurther", cite: "s 26A(a)(iv); FK-11", "if": ["and", IS_LESSOR, LIVE], then: [
        ["set", T("offerOpen"), true],
        ["set", T("offerTaken"), false],
        ["set", T("offerRent"), num("$p.rent", T("rentNow"))],
        ["set", T("offerMonths"), num("$p.months", 12)],
        ["set", T("offerKind"), ["if", ["=", "$p.kind", "periodic"], "periodic", "fixed"]],
        ["set", T("offerGap"), num("$p.gapDays", 0)],
        ["set", T("offerStart"), ["+", ["if", ["and", ["=", T("kind"), "fixed"], ["not", T("periodic76C")], [">=", T("fixedLastDay"), "$day"]], T("fixedLastDay"), "$day"], 1, T("offerGap")]],
        ["set", T("offerStartDate"), ["date", T("offerStart")]],
        ["set", T("offerMotivated"), ["if", "$p.motivated", true, false]],
        ["log", "{self} offers the tenant under {target} a further agreement at ${target.attrs.offerRent} a week, to start on {target.attrs.offerStartDate}. A further agreement is a new agreement: if the tenant enters into it, the rent it fixes is not an increase under s 30 (FK-01 reading A).",
          { cite: "s 30(1); FK-01", sev: "ok" }],
        ["observe", "offer-made"]
      ] },
      { id: "offer-fk11", on: "action:offerFurther", cite: "s 26A(a)(ii), (iv); FK-11",
        "if": ["and", IS_LESSOR, LIVE, "$p.motivated", [">", T("offerRent"), T("rentNow")], ["exists", T("matterDay")]], then: [
        ["log", "The higher rent is motivated by the matter that arose on {target.attrs.matterDate} ({target.attrs.matterWhat}). Offering a further agreement on harder terms is not retaliatory action on FK-11 reading A: s 26A(a)(ii) reaches an increase of 'the rent payable under the residential tenancy agreement', and (iv) only a refusal of a further agreement. On reading B it is within (ii) (encoding note N-08).",
          { cite: "s 26A(a)(ii), (iv); FK-11", sev: "warn" }],
        ["observe", "renewal-not-retaliatory"]
      ] },
      voidRule("refuse-not-lessor", "refuseFurther", ["not", IS_LESSOR], "{self} is not the lessor under {target}, and has no further agreement to refuse.", "s 26A(a)(iv)"),
      { id: "refuse-further", on: "action:refuseFurther", cite: "s 26A(a)(iv)", "if": ["and", IS_LESSOR, LIVE], then: [
        ["set", T("offerOpen"), false],
        ["log", "{self} refuses to enter into a further agreement with the tenant under {target}. That is lawful in itself; it is retaliatory action only if a matter in s 26B(2) has arisen and motivated it (s 26A(a)(iv), (b)).", { cite: "s 26A(a)(iv), (b)", sev: "ok" }],
        ["observe", "refusal"]
      ] }
    ],
    retaliation("refuseFurther", "refusal", "refused to enter into a further agreement with the tenant", "(iv)"),
    /* s 32(7): demanding rent */
    [
      voidRule("demand-not-lessor", "demandRent", ["not", IS_LESSOR], "{self} is not the lessor under {target}.", "s 32(7)"),
      { id: "demand-prepare", on: "action:demandRent", cite: "s 32(7)", "if": IS_LESSOR, then: [
        ["set", T("_amt"), num("$p.amount", T("rentNow"))],
        ["set", T("_inForce"), ["def", "orderInForce"]]
      ] },
      { id: "demand-offence", on: "action:demandRent", cite: "s 32(7)", "if": ["and", IS_LESSOR, T("_inForce"), [">", T("_amt"), T("orderMax")]], then: [
        ["log", "<b>s 32(7): an offence.</b> {self} demands ${target.attrs._amt} a week; an order under s 32 in force until {target.attrs.orderEndDate} fixes the most at ${target.attrs.orderMax}. Maximum fine $5,000.",
          { cite: "s 32(7)", sev: "stop" }],
        ["observe", "s32-offence"]
      ] },
      { id: "demand-within-order", on: "action:demandRent", cite: "s 32(7)", "if": ["and", IS_LESSOR, T("_inForce"), ["<=", T("_amt"), T("orderMax")]], then: [
        ["log", "${target.attrs._amt} a week is within the order under s 32 (${target.attrs.orderMax}).", { cite: "s 32(4), (7)", sev: "ok" }]
      ] },
      { id: "demand-no-order", on: "action:demandRent", cite: "s 32(7)", "if": ["and", IS_LESSOR, ["not", T("_inForce")]], then: [
        ["log", "No order under s 32 is in force for {target}: demanding ${target.attrs._amt} a week is not an offence under s 32(7).", { cite: "s 32(5), (7)", sev: "ok" }]
      ] },
      { id: "demand-fk23", on: "action:demandRent", cite: "s 32(5), (7); FK-23",
        "if": ["and", IS_LESSOR, ["not", T("_inForce")], ["exists", T("prevOrderMax")], ["<=", "$day", T("prevOrderEnd")], [">", T("_amt"), T("prevOrderMax")]], then: [
        ["log", "This turns on FK-23. The order made in respect of {target.attrs.prevOrderFrom} fixed ${target.attrs.prevOrderMax} for a period running to {target.attrs.prevOrderEndDate}, and lapsed when that tenancy ended (reading A, taken). On reading B the applicant's tenancy continues under {target}, the order is still in force, and this demand is an offence under s 32(7) (encoding note N-10).",
          { cite: "s 32(5), (7); FK-23", sev: "warn" }],
        ["observe", "fk23"]
      ] },
      { id: "demand-tidy", on: "action:demandRent", cite: "s 32(7)", "if": IS_LESSOR, then: [["set", T("_amt"), null], ["set", T("_inForce"), null]] }
    ],
    /* the premises change hands */
    [
      voidRule("buy-own", "buyPremises", ["=", "$target.rels.owner", "$self.id"], "{self} already holds {target}.", "s 3 'lessor'"),
      { id: "buy-premises", on: "action:buyPremises", cite: "s 3 'lessor'; FK-13", "if": ["!=", "$target.rels.owner", "$self.id"], then: [
        ["set", T("_oldOwner"), ["attrOf", ["rel", "$target", "owner"], "name"]],
        ["set", "$target.rels.owner", "$self.id"],
        ["set", T("ownerId"), "$self.id"],
        ["set", T("soldDay"), "$day"],
        ["log", "{self} buys {target} from {target.attrs._oldOwner}. Each agreement for the premises still in force passes to {self} as a successor or assignee of the lessor (s 3 'lessor'); the console records it on each agreement the next day.",
          { cite: "s 3 'lessor'", sev: "ok" }],
        ["observe", "premises-sold"],
        ["set", T("_oldOwner"), null]
      ] }
    ],
    /* the tenant */
    [
      voidRule("repairs-not-tenant", "askRepairs", ["not", IS_TENANT], "{self} is not a tenant under {target}.", "s 26B(2)(a)"),
      { id: "repairs-asked", on: "action:askRepairs", cite: "s 26B(2)(a)(i)", "if": ["and", IS_TENANT, LIVE], then: [
        ["set", T("matterDay"), ["if", ["exists", T("matterDay")], T("matterDay"), "$day"]],
        ["set", T("matterDate"), ["date", T("matterDay")]],
        ["set", T("matterWhat"), ["if", ["exists", T("matterWhat")], T("matterWhat"), "the tenant asked for repairs, s 26B(2)(a)(i)"]],
        ["log", "{self} asks for repairs: the tenant 'takes action to enforce the tenant's rights' (s 26B(2)(a)(i)). If the lessor now takes an action s 26A(a) lists, motivated by it, that is retaliatory action.", { cite: "ss 26A, 26B(2)(a)(i)", sev: "ok" }],
        ["observe", "matter-arises"]
      ] },

      voidRule("vacate-not-tenant", "vacate", ["not", IS_TENANT], "{self} is not a tenant under {target}.", "s 60(1)"),
      voidRule("vacate-ended", "vacate", ["and", IS_TENANT, T("ended")], "{target} terminated on {target.attrs.endedDate}.", "s 60(1)"),
      voidRule("vacate-not-begun", "vacate", ["and", IS_TENANT, LIVE, ["not", T("commenced")]], "The tenancy under {target} has not commenced.", "s 60(1)"),
      { id: "vacate-how", on: "action:vacate", cite: "s 60(1)", "if": ["and", IS_TENANT, LIVE, T("commenced")], then: [
        ["set", T("_how"),
          ["if", "$p.written", "g",
          ["if", "$p.abandon", "f",
          ["if", ["and", T("n64Pending"), [">=", "$day", T("n64Day")]], "a",
          ["if", ["and", ["exists", T("possDay70A")], [">=", "$day", T("possDay70A")]], "b",
          ["if", ["and", ["=", T("possBy"), "lessor"], [">", T("possDay70A"), T("expiryDay")], [">", "$day", T("expiryDay")], ["<", "$day", T("possDay70A")]], "b7", "none"]]]]]]
      ] },
      { id: "vacate-written", on: "action:vacate", cite: "s 60(1)(g)", "if": ["=", T("_how"), "g"], then: [].concat(terminate("$target", "vacant possession under a written agreement (s 60(1)(g))"), [
        ["log", "<b>{target} terminates today</b>: the tenant delivers up vacant possession under a written agreement with the lessor to terminate it (s 60(1)(g)).", { cite: "s 60(1)(g)", sev: "ok" }],
        ["observe", "terminated"]
      ]) },
      { id: "vacate-abandon", on: "action:vacate", cite: "s 60(1)(f)", "if": ["=", T("_how"), "f"], then: [].concat(terminate("$target", "abandonment (s 60(1)(f))"), [
        ["log", "<b>{target} terminates today</b>: the tenant abandons the premises (s 60(1)(f)).", { cite: "s 60(1)(f)", sev: "ok" }],
        ["observe", "terminated"]
      ]) },
      { id: "vacate-after-64", on: "action:vacate", cite: "s 60(1)(a)(i)", "if": ["=", T("_how"), "a"], then: [].concat(terminate("$target", "notice and vacant possession (s 60(1)(a)(i))"), [
        ["log", "<b>{target} terminates today</b>: notice of termination was given under the Act and the tenant delivers up vacant possession on or after the end of the period of notice, {target.attrs.n64Date} (s 60(1)(a)(i)).", { cite: "s 60(1)(a)(i)", sev: "ok" }],
        ["observe", "terminated"]
      ]) },
      { id: "vacate-after-70a", on: "action:vacate", cite: "s 60(1)(b)(i)", "if": ["=", T("_how"), "b"], then: [].concat(terminate("$target", "a notice under s 70A and possession (s 60(1)(b)(i))"), [
        ["log", "<b>{target} terminates today</b>: a notice under s 70A was given and the tenant delivers up possession on or after the day the term expired under that section, {target.attrs.possDate70A} (s 60(1)(b)(i)).", { cite: "s 60(1)(b)(i)", sev: "ok" }],
        ["observe", "terminated"]
      ]) },
      { id: "vacate-70a-7", on: "action:vacate", cite: "s 70A(7); s 60(1)(b)(i)", "if": ["=", T("_how"), "b7"], then: [].concat([
        ["set", T("possDay70A"), "$day"], ["set", T("possDate70A"), ["date", "$day"]]
      ], terminate("$target", "a notice under s 70A and possession (s 60(1)(b)(i), s 70A(7))"), [
        ["log", "<b>{target} terminates today</b>: the lessor's notice put the possession day after the expiry day, and the tenant delivers up possession after the expiry day but before it, so today is taken to be the possession day (s 70A(7)) and the term ends today (s 60(1)(b)(i)).", { cite: "s 70A(7); s 60(1)(b)(i)", sev: "ok" }],
        ["observe", "terminated"]
      ]) },
      { id: "vacate-no-termination", on: "action:vacate", cite: "s 60(1)", "if": ["=", T("_how"), "none"], then: [
        ["set", T("vacatedDay"), "$day"],
        ["log", "<b>{target} does not terminate.</b> 'A residential tenancy agreement shall not terminate or be terminated except in one of the following circumstances' (s 60(1)): no notice period has run out and there is no written agreement to terminate, so moving out is not one of them (unless the premises are abandoned, a fact). The agreement, and the rent, run on.",
          { cite: "s 60(1)", sev: "warn" }],
        ["observe", "vacated-no-termination"]
      ] }
    ],
    afterTermination("action:vacate", "$target", null, "-on-vacating"),
    [
      { id: "vacate-tidy", on: "action:vacate", cite: "s 60(1)", "if": ["exists", T("_how")], then: [["set", T("_how"), null]] },

      voidRule("agree-not-party", "agreeToEnd", ["not", ["or", IS_LESSOR, IS_TENANT]], "{self} is not a party to {target}.", "s 60(1)(g)"),
      { id: "agree-to-end", on: "action:agreeToEnd", cite: "s 60(1)(g); N-05", "if": ["and", ["or", IS_LESSOR, IS_TENANT], LIVE], then: [
        ["log", "<b>{target} does not terminate.</b> Section 60(1)(g) ends an agreement where 'the tenant delivers up vacant possession of the premises pursuant to an agreement in writing ... to terminate'; while the tenant stays, no circumstance in s 60(1) applies, and its opening words ('Despite any Act or law to the contrary') shut out surrender by operation of law (encoding note N-05).",
          { cite: "s 60(1), (1)(g)", sev: "warn" }],
        ["observe", "agreed-end-no-termination"]
      ] },

      voidRule("s32-not-tenant", "apply32", ["not", IS_TENANT], "Only 'a tenant under a residential tenancy agreement' may apply under s 32(1); {self} is not a tenant under {target}.", "s 32(1)"),
      { id: "s32-prepare", on: "action:apply32", cite: "s 32(2); IA s 61(1)(b), (e)", "if": ["and", IS_TENANT, LIVE], then: [
        ["set", T("_t30"), ["and", ["exists", T("noticeReceivedDay")], [">=", "$day", T("noticeReceivedDay")], ["<=", "$day", openDay(["+", T("noticeReceivedDay"), 30])]]],
        ["set", T("_t31a"), ["and", ["exists", T("chgUpReceivedDay")], [">=", "$day", T("chgUpReceivedDay")], ["<=", "$day", openDay(["+", T("chgUpReceivedDay"), 30])]]],
        ["set", T("_trigger"), ["or", ["exists", T("noticeReceivedDay")], ["exists", T("chgUpReceivedDay")], "$p.reduction"]],
        ["set", T("_inTime"), ["or", T("_t30"), T("_t31a"), "$p.reduction"]],
        ["set", T("_s32"), true]
      ] },
      { id: "s32-in-time", on: "action:apply32", cite: "s 32(1), (2)", "if": ["and", T("_s32"), T("_inTime")], then: [
        ["set", T("s32Pending"), true], ["set", T("s32Late"), false],
        ["log", "{self} applies within 30 days after the trigger s 32(2) names (IA s 61(1)(b), (e)). Proceedings for an order fixing the maximum rent are now pending, so s 65 bites: a notice under s 64 is ineffectual, and any other notice of termination by the lessor needs the court's authority.",
          { cite: "ss 32(2), 65(1)", sev: "ok" }],
        ["observe", "s32-applied"]
      ] },
      { id: "s32-late", on: "action:apply32", cite: "s 32(2)", "if": ["and", T("_s32"), ["not", T("_inTime")], T("_trigger")], then: [
        ["set", T("s32Pending"), true], ["set", T("s32Late"), true],
        ["log", "The application is made more than 30 days after the tenant received notice of the increase: it is out of time unless the court allows a greater period 'having regard to the justice and merits of the case' (s 32(2)).", { cite: "s 32(2)", sev: "warn" }],
        ["observe", "s32-late"]
      ] },
      { id: "s32-no-trigger", on: "action:apply32", cite: "s 32(2); N-09", "if": ["and", T("_s32"), ["not", T("_trigger")]], then: [
        ["log", "<b>No application can be made.</b> Section 32(2) requires it within 30 days (or a greater period the court allows) after the tenant receives notice of an increase in the rent payable or of a change of method that raises it, or after a significant reduction in chattels or facilities. {self} has received no such notice under {target}: a rent fixed by a new agreement, even a first agreement with a new tenant, is not 'notice of an increase in the rent payable' (encoding note N-09).",
          { cite: "s 32(1), (2)", sev: "warn" }],
        ["observe", "s32-no-trigger"]
      ] },
      { id: "s32-tidy", on: "action:apply32", cite: "s 32(2)", "if": T("_s32"), then:
        ["_t30", "_t31a", "_trigger", "_inTime", "_s32"].map(function (k) { return ["set", T(k), null]; }) },

      voidRule("s26b-not-tenant", "apply26B", ["not", IS_TENANT], "{self} is not a tenant under {target}.", "s 26B(3)"),
      { id: "s26b-applies", on: "action:apply26B", cite: "s 26B(2), (3)", "if": ["and", IS_TENANT, ["exists", T("listedKind")]], then: [
        ["set", T("s26bApplied"), true],
        ["log", "Section 26B applies: the tenant believes the lessor's action on {target.attrs.listedDate} (the lessor {target.attrs.listedWhat}) was retaliatory action, and it was taken after a matter in s 26B(2) arose on {target.attrs.matterDate}. {self} applies to a competent court for relief (s 26B(3)).",
          { cite: "s 26B(2), (3)", sev: "ok" }],
        ["observe", "s26b-applies"]
      ] },
      { id: "s26b-none", on: "action:apply26B", cite: "ss 26A(a), 26B(2); FK-11", "if": ["and", IS_TENANT, ["not", ["exists", T("listedKind")]]], then: [
        ["log", "<b>Section 26B does not apply.</b> Under {target} the lessor has taken none of the actions s 26A(a) lists after a matter in s 26B(2) arose. A higher rent fixed by a further agreement is not one of them (FK-11 reading A; encoding note N-08).",
          { cite: "ss 26A(a), 26B(2); FK-11", sev: "warn" }],
        ["observe", "s26b-no-application"]
      ] },

      voidRule("s64-apply-not-tenant", "apply64", ["not", IS_TENANT], "{self} is not a tenant under {target}.", "s 64(3)"),
      voidRule("s64-apply-nothing", "apply64", ["and", IS_TENANT, ["not", T("n64Pending")]], "No notice of termination under s 64 is pending under {target}.", "s 64(3)"),
      { id: "s64-apply", on: "action:apply64", cite: "s 64(3); IA s 61(1)(b), (e)", "if": ["and", IS_TENANT, T("n64Pending"), ["<=", "$day", T("n64ApplyBy")]], then: [
        ["set", T("n64Applied"), true],
        ["log", "{self} applies within 7 days after receiving the notice (s 64(3)) for an order that the period of notice be extended.", { cite: "s 64(3)", sev: "ok" }],
        ["observe", "s64-application"]
      ] },
      { id: "s64-apply-late", on: "action:apply64", cite: "s 64(3)", "if": ["and", IS_TENANT, T("n64Pending"), [">", "$day", T("n64ApplyBy")]], then: [
        ["log", "Too late: s 64(3) allows an application 'within 7 days after receiving' the notice, here to {target.attrs.n64ApplyByDate}.", { cite: "s 64(3)", sev: "warn" }],
        ["observe", "s64-application-late"]
      ] },

      voidRule("join-already", "joinAsCotenant", IS_TENANT, "{self} is already a tenant under {target}.", "s 3 'party'"),
      voidRule("join-ended", "joinAsCotenant", ["and", ["not", IS_TENANT], T("ended")], "{target} terminated on {target.attrs.endedDate}.", "s 60"),
      voidRule("join-full", "joinAsCotenant", ["and", ["not", IS_TENANT], LIVE, ["exists", "$target.rels.cotenant"]], "The console models a tenant and one co-tenant, and {target} has both.", "s 3 'party'"),
      { id: "join", on: "action:joinAsCotenant", cite: "s 3 'party' (a)", "if": ["and", ["not", IS_TENANT], LIVE, ["not", ["exists", "$target.rels.cotenant"]]], then: [
        ["set", "$target.rels.cotenant", "$self.id"],
        ["set", T("cotenantId"), "$self.id"],
        ["set", T("cotenantName"), ["attrOf", ["rel", "$target", "cotenant"], "name"]],
        ["log", "{self} becomes a co-tenant under {target}, by agreement with the lessor and the tenant (how is a matter for Part IV Division 2, outside this scope). A later agreement with {self} as tenant shares a tenant with {target} (s 31B(3)(b)).",
          { cite: "s 3 'party' (a); s 31B(3)(b)", sev: "ok" }],
        ["observe", "cotenant-joins"]
      ] },

      voidRule("leave-not-tenant", "leaveAgreement", ["not", IS_TENANT], "{self} is not a tenant under {target}.", "s 60(2)"),
      voidRule("leave-ended", "leaveAgreement", ["and", IS_TENANT, T("ended")], "{target} terminated on {target.attrs.endedDate}.", "s 60(2)"),
      voidRule("leave-alone", "leaveAgreement", ["and", IS_TENANT, LIVE, ["not", ["exists", "$target.rels.cotenant"]]], "{self} is the only tenant under {target}. Section 60(2) keeps an agreement alive for the other tenants when one tenant's interest ends; with none left, the agreement ends only in a circumstance s 60(1) lists.", "s 60(1), (2)"),
      { id: "leave-as-tenant", on: "action:leaveAgreement", cite: "s 60(2)", "if": ["and", ["=", "$self.id", "$target.rels.tenant"], LIVE, ["exists", "$target.rels.cotenant"]], then: [
        ["set", "$target.rels.tenant", "$target.rels.cotenant"],
        ["set", "$target.rels.cotenant", null],
        ["set", T("tenantId"), "$target.rels.tenant"], ["set", T("cotenantId"), null],
        ["set", T("tenantName"), ["attrOf", ["rel", "$target", "tenant"], "name"]], ["set", T("cotenantName"), null],
        ["log", "{self}'s interest in {target} ends. 'The termination of a tenant's interest ... does not terminate the agreement in respect of any other tenant' (s 60(2)): {target.attrs.tenantName} remains the tenant. (How a tenant's interest ends is outside this scope.)",
          { cite: "s 60(2)", sev: "ok" }],
        ["observe", "cotenant-leaves"]
      ] },
      { id: "leave-as-cotenant", on: "action:leaveAgreement", cite: "s 60(2)", "if": ["and", ["=", "$self.id", "$target.rels.cotenant"], LIVE], then: [
        ["set", "$target.rels.cotenant", null],
        ["set", T("cotenantId"), null], ["set", T("cotenantName"), null],
        ["log", "{self}'s interest in {target} ends; the agreement continues for {target.attrs.tenantName} (s 60(2)).", { cite: "s 60(2)", sev: "ok" }],
        ["observe", "cotenant-leaves"]
      ] },

      { id: "income-rises", on: "action:incomeRises", cite: "s 31A(1); FK-20", "if": ["and", S("incomeBased"), ["not", S("ended")]], then: [
        ["set", S("prevRent"), S("rentNow")],
        ["set", S("rentNow"), num("$p.rent", ["+", S("rentNow"), 20])],
        ["log", "The unchanged method, applied to the tenant's higher income, gives ${self.attrs.rentNow} a week (from ${self.attrs.prevRent}). That is the method operating, not the rent increasing 'otherwise' than by a change of method (s 31A(1); FK-20 reading A). Read word for word (reading B), 'otherwise the rent must not increase' would bar it (encoding note N-22).",
          { cite: "s 31A(1); FK-20", sev: "ok" }],
        ["observe", "income-rise"]
      ] },
      { id: "income-rises-fixed", on: "action:incomeRises", cite: "s 30(1)", "if": ["or", ["not", S("incomeBased")], S("ended")], then: [
        ["log", "<b>Nothing has happened.</b> {self}'s rent is not calculated by reference to the tenant's income (or the agreement has ended); the tenant's income does not change it.", { cite: "ss 30(1), 31A(1)", sev: "ok" }],
        ["observe", "void-act"]
      ] }
    ],
    /* the court */
    [
      voidRule("s32-nothing-before-court", "order32", ["not", T("s32Pending")], "No application under s 32 about {target} is before the court.", "s 32(1)"),
      { id: "s32-decide", on: "action:order32", cite: "s 32(2)-(5)", "if": T("s32Pending"), then: [
        ["set", T("_decision"), ["if", ["and", T("s32Late"), ["not", "$p.allowLate"]], "late", ["if", "$p.refuse", "refuse", "order"]]],
        ["set", T("s32Pending"), false]
      ] },
      { id: "s32-out-of-time", on: "action:order32", cite: "s 32(2)", "if": ["=", T("_decision"), "late"], then: [
        ["log", "The court does not allow a greater period: the application, out of time under s 32(2), fails.", { cite: "s 32(2)", sev: "warn" }],
        ["observe", "s32-refused"]
      ] },
      { id: "s32-not-excessive", on: "action:order32", cite: "s 32(3), (4)", "if": ["=", T("_decision"), "refuse"], then: [
        ["log", "The court determines, having regard to the matters in s 32(3), that the rent is not excessive: no order.", { cite: "s 32(3), (4)", sev: "ok" }],
        ["observe", "s32-refused"]
      ] },
      { id: "s32-order", on: "action:order32", cite: "s 32(4), (5); IA ss 61(1)(a), 62", "if": ["=", T("_decision"), "order"], then: [].concat([
        ["set", T("_m"), num("$p.months", 6)],
        ["set", T("_m6"), min(T("_m"), 6)],
        ["set", T("orderMade"), "$day"],
        ["set", T("orderMadeDate"), ["date", "$day"]],
        ["set", T("orderMax"), num("$p.max", ["-", T("rentNow"), 50])],
        ["set", T("orderLapsed"), false],
        ["set", T("orderLapsedWithTenancy"), false]
      ], lastDayOfMonths("$target", "$day", T("_m6"), T("orderEnd")), [
        ["set", T("orderEndDate"), ["date", T("orderEnd")]],
        ["set", T("matterDay"), ["if", ["exists", T("matterDay")], T("matterDay"), "$day"]],
        ["set", T("matterDate"), ["date", T("matterDay")]],
        ["set", T("matterWhat"), ["if", ["exists", T("matterWhat")], T("matterWhat"), "an order of a competent court is in force, s 26B(2)(c)"]],
        ["log", "<b>Order under s 32(4):</b> from today the rent payable under {target} shall not exceed ${target.attrs.orderMax} a week. It has effect until the expiration of the applicant's tenancy or the end of the period fixed, {target.attrs.orderEndDate} (the period begins on the day the order is made), whichever is earlier (s 32(5)). While it is in force s 65 bites, and demanding more is an offence (s 32(7)).",
          { cite: "s 32(4), (5), (7); s 65", sev: "ok" }],
        ["observe", "s32-order"]
      ]) },
      { id: "s32-order-cap", on: "action:order32", cite: "s 32(5)", "if": ["and", ["=", T("_decision"), "order"], [">", T("_m"), 6]], then: [
        ["log", "The court fixed {target.attrs._m} months, but the period may not exceed 6 months (s 32(5)): it ends on {target.attrs.orderEndDate}.", { cite: "s 32(5)", sev: "ok" }]
      ] },
      { id: "s32-decide-tidy", on: "action:order32", cite: "s 32", "if": ["exists", T("_decision")], then: [["set", T("_decision"), null], ["set", T("_m"), null], ["set", T("_m6"), null]] },

      voidRule("s26b-nothing-before-court", "decide26B", ["not", T("s26bApplied")], "No application under s 26B about {target} is before the court.", "s 26B(3)"),
      { id: "s26b-dismissed", on: "action:decide26B", cite: "s 26B(4)", "if": ["and", T("s26bApplied"), ["not", "$p.satisfied"]], then: [
        ["set", T("s26bApplied"), false], ["set", T("s26bDecided"), true],
        ["log", "The court is not satisfied that the lessor's action was likely to have been retaliatory action: no order (s 26B(4)).", { cite: "s 26B(4)", sev: "ok" }],
        ["observe", "s26b-dismissed"]
      ] },
      { id: "s26b-set-aside", on: "action:decide26B", cite: "s 26B(4)(a)", "if": ["and", T("s26bApplied"), "$p.satisfied"], then: [
        ["set", T("s26bApplied"), false], ["set", T("s26bDecided"), true],
        ["set", T("n64Pending"), ["if", ["=", T("listedKind"), "s64"], false, T("n64Pending")]],
        ["set", T("incPending"), ["if", ["=", T("listedKind"), "increase"], false, T("incPending")]],
        ["set", T("n70L"), ["if", ["=", T("listedKind"), "s70a"], null, T("n70L")]],
        ["set", T("possDay70A"), ["if", ["=", T("listedKind"), "s70a"], T("n70T"), T("possDay70A")]],
        ["set", T("fixedLastDay"), ["if", ["and", ["=", T("listedKind"), "s70a"], ["not", T("periodic76C")]], ["if", ["exists", T("possDay70A")], max(T("expiryDay"), T("possDay70A")), T("expiryDay")], T("fixedLastDay")]],
        ["set", T("fixedLastDate"), dateOf(T("fixedLastDay"))],
        ["log", "<b>The court sets aside the lessor's action</b> (the lessor {target.attrs.listedWhat}), being satisfied it was likely to have been retaliatory action (s 26B(4)(a)). It may also order compensation for loss or injury other than personal injury (s 26B(4)(b)).",
          { cite: "s 26B(4)", sev: "ok" }],
        ["observe", "s26b-set-aside"]
      ] },

      voidRule("s64-nothing-before-court", "decide64", ["not", T("n64Applied")], "No application under s 64(3) about {target} is before the court.", "s 64(3)"),
      { id: "s64-decide", on: "action:decide64", cite: "s 64(4)", "if": T("n64Applied"), then: [
        ["set", T("n64Applied"), false],
        ["set", T("_ext"), num("$p.extendDays", 0)],
        ["set", T("_pos"), num("$p.possessionInDays", 0)],
        ["set", T("_d"), ["+", "$day", T("_pos")]],
        ["set", T("_lo"), max(["+", T("n64Received"), 61], ["+", "$day", 1])],
        ["set", T("_hi"), max(["+", T("n64Received"), 61], ["+", "$day", 7])],
        ["set", T("_dDate"), ["date", T("_d")]], ["set", T("_loDate"), ["date", T("_lo")]], ["set", T("_hiDate"), ["date", T("_hi")]],
        ["set", T("_s64d"), ["if", "$p.notTerminated", "b", ["if", [">", T("_ext"), 0], "a", ["if", [">", T("_pos"), 0], "c", "none"]]]]
      ] },
      { id: "s64-not-terminated", on: "action:decide64", cite: "s 64(4)(b)", "if": ["=", T("_s64d"), "b"], then: [
        ["set", T("n64Pending"), false],
        ["log", "The court orders that {target} is not terminated as a consequence of the notice (s 64(4)(b)).", { cite: "s 64(4)(b)", sev: "ok" }],
        ["observe", "s64-court"]
      ] },
      { id: "s64-extended", on: "action:decide64", cite: "s 64(4)(a); IA s 61(1)(g)", "if": ["=", T("_s64d"), "a"], then: [
        ["set", T("n64Day"), ["+", T("n64Day"), min(T("_ext"), 60)]],
        ["set", T("n64Date"), ["date", T("n64Day")]],
        ["log", "The court extends the period of notice, by up to 60 days (s 64(4)(a)): possession is now to be given on {target.attrs.n64Date}.", { cite: "s 64(4)(a)", sev: "ok" }],
        ["observe", "s64-court"]
      ] },
      { id: "s64-possession", on: "action:decide64", cite: "s 64(4)(c); FK-05", "if": ["and", ["=", T("_s64d"), "c"], [">=", T("_d"), T("_lo")], ["<=", T("_d"), T("_hi")]], then: [
        ["set", T("courtTermDay"), T("_d")],
        ["log", "The court makes an order for possession under s 71(2), operating from {target.attrs._dDate}: the later of a day not less than 60 days after the notice was received and a day within 7 days after the order (s 64(4)(c); FK-05 reading A allows {target.attrs._loDate} to {target.attrs._hiDate}).",
          { cite: "s 64(4)(c); FK-05", sev: "ok" }],
        ["observe", "s64-court"]
      ] },
      { id: "s64-possession-fk05", on: "action:decide64", cite: "s 64(4)(c); FK-05", "if": ["and", ["=", T("_s64d"), "c"], ["or", ["<", T("_d"), T("_lo")], [">", T("_d"), T("_hi")]]], then: [
        ["log", "The court cannot make the order operate from {target.attrs._dDate}. Section 64(4)(c) asks for 'a day that is the later of (i) a day not less than 60 days after the day on which the notice ... was received; or (ii) a day within 7 days after the day on which the order was made'. On FK-05 reading A (taken) that is a day from {target.attrs._loDate} to {target.attrs._hiDate}. Read literally (reading B), the words name two ranges and any day from {target.attrs._loDate} would do (encoding note N-19).",
          { cite: "s 64(4)(c); FK-05", sev: "warn" }],
        ["observe", "fk05"]
      ] },
      { id: "s64-decide-tidy", on: "action:decide64", cite: "s 64(4)", "if": ["exists", T("_s64d")], then:
        ["_ext", "_pos", "_d", "_lo", "_hi", "_dDate", "_loDate", "_hiDate", "_s64d"].map(function (k) { return ["set", T(k), null]; }) },

      voidRule("s65-not-biting", "authorise65", ["not", ["def", "s65Bites"]], "No proceedings under s 32 are pending about {target} and no order is in force: s 65 does not apply, and there is nothing to authorise.", "s 65(1)"),
      { id: "s65-refused", on: "action:authorise65", cite: "s 65(2)", "if": ["and", ["def", "s65Bites"], "$p.motivated"], then: [
        ["log", "The court is not satisfied that neither the proceedings nor the order motivated the lessor: it does not authorise a notice of termination (s 65(2)).", { cite: "s 65(2)", sev: "ok" }]
      ] },
      { id: "s65-authorised", on: "action:authorise65", cite: "s 65(2)", "if": ["and", ["def", "s65Bites"], ["not", "$p.motivated"]], then: [
        ["set", T("s65Authorised"), true],
        ["log", "The court authorises the lessor to give notice of termination of {target} (s 65(2)): a notice other than under s 64 is no longer ineffectual (s 65(1)(b)). A notice under s 64 still is (s 65(1)(a)).", { cite: "s 65(1), (2)", sev: "ok" }],
        ["observe", "s65-authorised"]
      ] }
    ],
    /* ---- added at 8A (5 Oct 2026): rules that only log and count, for LQA candidates ---- */
    [
      /* a notice without a ground under an agreement the parties replaced in place (s 60(1); N-05) */
      { id: "s64-under-replaced", on: "action:give64", cite: "ss 60(1), 64(1), (5); N-05",
        "if": ["and", IS_LESSOR, LIVE, T("n64Pending"), ["=", T("n64Given"), "$day"], [">", ["count", "agreement", W_NEWER_T], 0]], then: [
        ["set", T("_newer"), ["attrOf", ["any", "agreement", W_NEWER_T], "name"]],
        ["log", "<b>{target} is still in force</b>, though the parties made {target.attrs._newer} to replace it: no circumstance in s 60(1) ended it while the tenant stayed. It is a periodic tenancy, so this notice without a ground is good under s 64. To end {target} the tenant must deliver up vacant possession (s 60(1)(a)(i)), and with it goes the tenant's occupation under {target.attrs._newer}, during a fixed term in which s 64(5) bars such a notice under {target.attrs._newer} itself (encoding note N-05).",
          { cite: "ss 60(1), 64(1), (5)", sev: "warn" }],
        ["observe", "notice-under-replaced"],
        ["set", T("_newer"), null]
      ] },
      /* proceedings under s 32 begun after a notice under s 64 was given (s 65(1)(a)) */
      { id: "s65-after-notice", on: "action:apply32", cite: "s 65(1)(a); s 32(2)",
        "if": ["and", IS_TENANT, LIVE, T("s32Pending"), T("n64Pending"), ["<", T("n64Given"), "$day"]], then: [
        ["set", T("_n64g"), ["date", T("n64Given")]],
        ["log", "Proceedings for an order under s 32 are now pending, and a notice without a ground given on {target.attrs._n64g} is running. Section 65(1)(a) says that where such proceedings are pending 'any notice of termination of the agreement given by the lessor under section 64 is ineffectual'. It does not say whether that reaches a notice given before the proceedings began, or whether such a notice revives if the application fails. The console, like the encoding's cases, tests s 65 when a notice is given, so it lets this notice run on.",
          { cite: "s 65(1)(a), (2); s 32(2)", sev: "warn" }],
        ["observe", "s65-later-proceedings"],
        ["set", T("_n64g"), null]
      ] },
      /* a demand for more rent than the rent payable, with no order under s 32 in force */
      { id: "demand-above-rent", on: "action:demandRent", cite: "ss 27(1), 30(1), 31A(1), 32(7)",
        "if": ["and", IS_LESSOR, LIVE, ["not", ["def", "orderInForce"]], [">", num("$p.amount", T("rentNow")), T("rentNow")]], then: [
        ["set", T("_dem"), num("$p.amount", T("rentNow"))],
        ["log", "{self} demands ${target.attrs._dem} a week. The rent payable under {target} is ${target.attrs.rentNow}: no notice under s 30 (or change of method under s 31A) has raised it, and 'otherwise the rent shall not increase or be increased' (s 30(1)). The Act states no consequence for the demand: s 32(7) punishes only a demand above an order under s 32, and whether s 27(1) reaches the excess turns on whether it is 'rent'.",
          { cite: "ss 27(1), 30(1), 32(7)", sev: "warn" }],
        ["observe", "demand-unlawful-increase"],
        ["set", T("_dem"), null]
      ] }
    ]
  );

  var RULES = [].concat(
    createRules,
    commencement(),
    bookkeeping,
    clockRules,
    increaseRules,
    changeRules,
    laterDayRules,
    afterTermination("day", "$self", "agreement", "-on-the-day"),
    actionRules
  );

  var OBSERVATIONS = [
    /* agreements: beginning, carrying on, ending */
    { id: "agreement-entered", sev: "ok", label: "An agreement is entered into", cite: "s 3 'residential tenancy agreement'",
      what: "A residential tenancy agreement comes into existence.", why: "Counted." },
    { id: "continuation", sev: "ok", label: "A new agreement is a continuation of the one before", cite: "s 31B(2), (3)",
      what: "A further agreement between the same parties, for the same premises, starts the day after the end of the term of the existing one.",
      why: "For working out when rent was last increased under s 30 or the method last changed under s 31A, the two are one (s 31B(1))." },
    { id: "rent-by-agreement", ref: "M-01", sev: "warn", label: "The rent rises by a new agreement, not by notice", cite: "ss 30(1), 31B(1); FK-01",
      what: "A continuing agreement fixes a higher rent than the one it continues.",
      why: "On FK-01 reading A the rent a new agreement fixes is not an increase under s 30: no notice, no 60 days, no 12 months, at every renewal. Encoding note N-01." },
    { id: "clock-carried", sev: "warn", label: "A new agreement inherits the 12 months from the last rise by notice", cite: "ss 30(1)(b), 31B(1)",
      what: "A continuing agreement starts with a rent increase (or change of method) in the chain behind it.",
      why: "Section 31B carries the last increase across, so the 12 months for the next one run from it, not from the new agreement's start. Encoding note N-02." },
    { id: "clock-carried-used", ref: "L-03", sev: "warn", label: "A rise by notice soon after a new agreement's higher rent", cite: "ss 30(1)(b), 31B; FK-16; FK-17; FK-13",
      what: "An increase by notice takes effect less than 12 months after the agreement it varies began.",
      why: "The rent has risen twice within the year, once by agreement and once by notice; without the continuation the second could not take effect so soon. Encoding note N-02." },
    { id: "fresh-clock", sev: "ok", label: "A new agreement starts a fresh 12 months", cite: "s 30(1)(b)",
      what: "An agreement that follows another for the same premises is not a continuation of it.",
      why: "Its rent was set freely, and the 12 months run from its own commencement." },
    { id: "gap", ref: "L-06", sev: "warn", label: "A gap between agreements ends the continuation", cite: "s 31B(2)(c)",
      what: "A further agreement between the same parties starts a day or more after the earlier one terminated.",
      why: "'Starts immediately after the end of the term' (s 31B(2)(c)): one day is enough to break it. Encoding note N-03." },
    { id: "new-tenant", ref: "L-05", sev: "warn", label: "A new tenant starts a fresh 12 months", cite: "s 31B(3)(b)",
      what: "A new agreement for the same premises and lessor shares no tenant with the one before.",
      why: "The limit attaches to the parties, not the premises (Queensland's 2024 text attaches it to the premises). Encoding note N-07." },
    { id: "new-lessor", ref: "L-05", sev: "warn", label: "A different lessor starts a fresh 12 months", cite: "s 31B(3)(a)",
      what: "A new agreement with a tenant in common is made by a lessor who was not the lessor under the earlier one at its end.",
      why: "Not 'between the same parties' (s 31B(3)(a))." },
    { id: "not-ended", ref: "L-04", sev: "warn", label: "The earlier agreement has not ended, so the new one continues nothing", cite: "ss 31B(2)(c), 60(1)",
      what: "A new agreement between the same parties starts while the earlier one, not having terminated, is still running.",
      why: "No circumstance in s 60(1) ends an agreement the parties replace while the tenant stays. Encoding note N-05." },
    { id: "two-in-force", ref: "L-04", sev: "warn", label: "Two agreements for the same premises and parties are in force at once", cite: "ss 60(1), 76C",
      what: "A renewal is made and the old agreement does not terminate; s 76C continues it as a periodic tenancy beside the new one.",
      why: "Encoding note N-05." },
    { id: "s76c", sev: "ok", label: "A fixed term continues as a periodic tenancy", cite: "s 76C(1), (2)",
      what: "A fixed term passes its last day without terminating.", why: "Same agreement, same terms, now periodic." },
    { id: "holding-over", ref: "L-25", sev: "warn", label: "The tenant stays after the possession day, and s 76C continues the agreement", cite: "ss 60(1)(b), 70A, 76C; FK-09",
      what: "A notice under s 70A named a possession day and the tenant did not leave.",
      why: "On the encoding's reading s 76C asks only whether the agreement terminated by the end of the fixed term." },
    { id: "fk09", ref: "L-25", sev: "ok", label: "An agreement ended on its expiry day is not continued by s 76C", cite: "s 76C(1); FK-09",
      what: "A fixed term terminates on its expiry day after a notice under s 70A.",
      why: "FK-09 reading A; read word for word, s 76C(1) ('unless the agreement is terminated before the expiry day') would continue it. Encoding note N-18." },
    { id: "terminated", sev: "ok", label: "An agreement terminates", cite: "s 60(1)",
      what: "An agreement ends in a circumstance s 60(1) lists.", why: "Counted." },
    { id: "vacated-no-termination", sev: "warn", label: "The tenant moves out, but the agreement does not end", cite: "s 60(1)",
      what: "Vacant possession is given up before any notice period has run, without a written agreement to end.",
      why: "Section 60(1) lists the only ways an agreement terminates." },
    { id: "agreed-end-no-termination", ref: "L-04", sev: "warn", label: "The parties agree to end an agreement and the tenant stays: it does not end", cite: "s 60(1)(g)",
      what: "The lessor and tenant agree to end an agreement (to replace it, say) and the tenant does not move out.",
      why: "Section 60(1)(g) needs vacant possession delivered up under the written agreement. Encoding note N-05." },
    { id: "successor-lessor", sev: "ok", label: "A buyer of the premises becomes the lessor", cite: "s 3 'lessor'; FK-13",
      what: "Premises let under an agreement in force are sold.", why: "'Lessor' includes a successor or assignee of a lessor (s 3)." },
    { id: "premises-sold", sev: "ok", label: "Premises are sold", cite: "s 3 'lessor'", what: "Someone buys residential premises.", why: "Counted." },
    { id: "cotenant-joins", sev: "ok", label: "A co-tenant joins an agreement", cite: "s 3 'party' (a); s 31B(3)(b)", what: "A person becomes a co-tenant.", why: "Counted." },
    { id: "cotenant-leaves", sev: "ok", label: "A tenant leaves; the agreement continues for the other", cite: "s 60(2)",
      what: "One tenant's interest ends while another stays.", why: "Section 60(2)." },
    { id: "void-act", sev: "ok", label: "An act with no legal effect", cite: "ss 26B, 30, 31, 31A, 32, 60, 64, 65, 70A",
      what: "Someone does something the Act gives them no power to do, or that has nothing to act on.",
      why: "Shown, not prevented: the console reports the nullity." },

    /* s 30 */
    { id: "inc-notice", sev: "ok", label: "A notice of rent increase is given", cite: "s 30(1)", what: "A lessor gives notice of an increase.", why: "Counted." },
    { id: "increase-effect", sev: "ok", label: "A rent increase takes effect", cite: "s 30(1), (3)", what: "A notice of increase given in accordance with s 30 varies the agreement.", why: "Counted." },
    { id: "increase-no-effect", sev: "warn", label: "A notice of rent increase has no effect", cite: "s 30(1) closing words",
      what: "A notice of increase reaches the day it names without meeting s 30.", why: "'Otherwise the rent shall not increase or be increased.' The log gives the reason." },
    { id: "inc-12-months", sev: "warn", label: "No increase: the 12 months had not passed", cite: "s 30(1)(b); IA ss 61(1)(b), 62",
      what: "The day named is earlier than the last day of the 12 months after the tenancy commenced or the rent was last increased.",
      why: "Counted in calendar months, with the last day of the 12 months a good day (FK-15 A)." },
    { id: "inc-60-days", sev: "warn", label: "No increase: fewer than 60 clear days' notice", cite: "s 30(1)(a); IA s 61(1)(f); FK-06",
      what: "The day named is less than 60 clear days after the notice was given.", why: "FK-06 reading A." },
    { id: "inc-fixed-term", sev: "warn", label: "No increase: it would take effect during a fixed term that sets out no increase", cite: "s 30(2)(a); FK-03",
      what: "The day named falls in the fixed term, and the agreement sets out no amount or method of increase.", why: "FK-03 reading A: the bar is on increases taking effect in the term." },
    { id: "inc-form", sev: "warn", label: "No increase: not in an approved form", cite: "s 30(1); s 3 'approved form'", what: "A notice not in an approved form.", why: "Counted." },
    { id: "inc-income-based", sev: "warn", label: "No increase: the rent is income-based, so s 30 does not apply", cite: "ss 30(1), 31A(1)",
      what: "A notice under s 30 for an agreement whose rent is calculated by reference to income.", why: "Only a change of method under s 31A can raise such a rent." },
    { id: "inc-excluded", sev: "warn", label: "No increase: the agreement excludes increases", cite: "s 30(2)(b)", what: "A notice under an agreement that excludes increases.", why: "Counted." },
    { id: "inc-withdrawn", sev: "ok", label: "A notice of increase is withdrawn", cite: "s 30(3)", what: "The lessor withdraws a pending notice.", why: "Counted." },
    { id: "email-notice", ref: "U-17", sev: "warn", label: "A notice sent by email is not given", cite: "s 85(1)(c); r 12I; FK-12",
      what: "A notice under s 30, 31A, 64 or 70A is sent by email, even with the recipient's consent.",
      why: "No electronic means is prescribed for these notices (r 12I prescribes email only for an 'authorised notice'), so on FK-12 reading A the notice is never given. Encoding note N-20." },
    { id: "inc-s100-4", sev: "warn", label: "A notice given before 29 July 2024 has no effect under s 100(4)", cite: "s 100(4); FK-21",
      what: "A notice given before 29 July 2024, for an increase on or after it, fails the present s 30.",
      why: "Section 100(4). Encoding notes N-11 and N-12 (no notice given before then could be in the form approved under s 88C)." },
    { id: "inc-former-s30", sev: "ok", label: "An increase under s 30 as in force before 29 July 2024", cite: "ss 99, 100",
      what: "An increase takes effect under the former s 30 (6 months).", why: "Section 99(3), or an increase before the amendment came into operation." },
    { id: "s99-applies", sev: "ok", label: "A fixed term keeps the former s 30 to the end of its current term", cite: "s 99(2), (3)",
      what: "A fixed term entered into before 29 July 2024 runs past it.", why: "Section 99(3)." },
    { id: "fk02", ref: "U-36", sev: "ok", label: "When was rent 'last so increased': the day it took effect (FK-02)", cite: "s 30(1)(b); FK-02",
      what: "An increase fails because the 12 months from the last increase taking effect have not run, though 12 months from its notice have.", why: "FK-02 reading A." },
    { id: "fk03", ref: "U-18", sev: "ok", label: "A notice given in a fixed term for an increase after it (FK-03)", cite: "s 30(2)(a); FK-03",
      what: "An increase takes effect the day after a fixed term, under a notice given during it.", why: "FK-03 reading A; on reading B it would fail. Encoding note N-25." },
    { id: "fk04", ref: "U-23", sev: "warn", label: "An increase under the former s 30 counts as the last increase (FK-04)", cite: "s 30(1)(b); IA s 16(2); FK-04",
      what: "The 12 months under the present s 30 run from an increase made under the former one.", why: "FK-04 reading A (IA s 16(2))." },
    { id: "fk06", ref: "T-35", sev: "warn", label: "A notice on the 60th day: enough or a day short (FK-06)", cite: "ss 30(1)(a), 64(2); IA s 61(1)(b), (f); FK-06",
      what: "A notice names the 60th day after it is given.", why: "A day short on reading A (60 clear days); enough on reading B. Encoding note N-14." },
    { id: "fk15", ref: "U-37", sev: "ok", label: "An increase on the last day of the 12 months (FK-15)", cite: "s 30(1)(b); IA s 62; FK-15",
      what: "An increase takes effect on the numerically corresponding day a year after the last.", why: "FK-15 reading A; on reading B the next day." },
    { id: "fk19", ref: "U-12", sev: "ok", label: "After s 76C, the 12 months still run from the first commencement (FK-19)", cite: "ss 30(1)(b), 76C(2); FK-19",
      what: "An increase under an agreement s 76C continued takes effect less than 12 months after the periodic tenancy began.", why: "FK-19 reading A. Encoding note N-26." },
    { id: "fk21", ref: "U-22", sev: "ok", label: "s 100(4) does not reach an increase that took effect before 29 July 2024 (FK-21)", cite: "s 100(4); IA s 37(1)(b); FK-21",
      what: "An increase noticed and taking effect before 29 July 2024 stands.", why: "FK-21 reading A. Encoding note N-11." },
    { id: "fk22", ref: "U-19", sev: "warn", label: "Which s 30 governs a notice spanning the end of a s 99 term (FK-22)", cite: "s 99(3); FK-22",
      what: "A notice given in the current term of a s 99 agreement for an increase after it.", why: "FK-22 reading A: the version for the day of the increase. Encoding note N-13." },
    { id: "fk26", ref: "M-20", sev: "ok", label: "A notice in the other approved form is saved by IA s 74 (FK-26)", cite: "s 30(1); s 88C; IA s 74; FK-26",
      what: "A notice in the Minister's form where the s 88C form is required, or the reverse.", why: "FK-26 reading A. Encoding note N-12." },

    /* s 31A */
    { id: "change-notice", sev: "ok", label: "A notice of change of method is given", cite: "s 31A(2)", what: "A lessor gives notice of a change to how income-based rent is calculated.", why: "Counted." },
    { id: "change-effect", sev: "ok", label: "A change of method takes effect", cite: "s 31A(1), (2)", what: "A change of method under s 31A takes effect.", why: "Counted." },
    { id: "change-no-effect", sev: "warn", label: "A change of method has no effect", cite: "s 31A(1), (2)", what: "A notice of change reaches its day without meeting s 31A(2).", why: "'Otherwise the rent must not increase or be increased.'" },
    { id: "income-rise", ref: "U-29", sev: "ok", label: "Income-based rent rises with income, the method unchanged (FK-20)", cite: "s 31A(1); FK-20",
      what: "The tenant's income rises and the unchanged method gives a higher rent.", why: "FK-20 reading A; read word for word, s 31A(1) bars it. Encoding note N-22." },

    /* s 31B forks */
    { id: "fk13", ref: "U-10", sev: "warn", label: "A buyer who renews continues the old agreement (FK-13)", cite: "ss 3 'lessor', 31B(3)(a); FK-13",
      what: "A continuation where the lessor at the end of the existing agreement is not the lessor who granted it.", why: "FK-13 reading A; on reading B a fresh 12 months." },
    { id: "fk16", ref: "U-08", sev: "warn", label: "A renewal made without a notice under s 70A continues the old term (FK-16)", cite: "ss 31B(2)(c), 70A(2), 76C; FK-16",
      what: "A continuation of a fixed term that did not terminate (no notice under s 70A, or the tenant stayed).",
      why: "FK-16 reading A; on reading B the commonest renewal is never a continuation. Encoding note N-04." },
    { id: "fk17", ref: "U-09", sev: "warn", label: "A continuation of a periodic tenancy (FK-17)", cite: "s 31B(2)(c); FK-17",
      what: "A continuation whose existing agreement ended as a periodic tenancy.", why: "FK-17 reading A; on reading B 'term' means a fixed term. Encoding note N-06." },
    { id: "fk18", ref: "U-11", sev: "ok", label: "No rise by notice in the chain: the 12 months run from the new agreement's start (FK-18)", cite: "s 30(1)(b); FK-18",
      what: "A continuation with no increase under s 30 anywhere in the chain.", why: "FK-18 reading A; on reading B from the chain's first commencement." },
    { id: "fk10", ref: "U-26", sev: "ok", label: "A possession day after the expiry day keeps the fixed term running (FK-10)", cite: "ss 70A(5), 76C(2); FK-10",
      what: "A new agreement starts the day after the expiry day of one whose possession day is later.", why: "FK-10 reading A; on reading B it would be a continuation." },

    /* s 31, s 29 */
    { id: "bond-increase", sev: "ok", label: "A bond increase becomes payable", cite: "s 31(1A), (3)", what: "An additional amount of bond is payable.", why: "Counted." },
    { id: "fk25", ref: "D-42", sev: "ok", label: "A notice under s 31A that lowers the rent supports a bond increase (FK-25)", cite: "s 31(1A); r 5CB; FK-25",
      what: "A bond increase rests on a notice under s 31A whose change does not raise the rent.", why: "FK-25 reading A: the phrase names the notice. Encoding note N-23." },
    { id: "bond-no-event", ref: "M-01", sev: "warn", label: "No bond increase without a notice of rent increase", cite: "s 31(1), (1A); r 5CB",
      what: "A lessor tries to increase the bond with no notice under s 30 or 31A given.", why: "A rent set by a new agreement supports no bond increase under s 31. Encoding note N-01." },
    { id: "bond-no-effect", sev: "warn", label: "A bond notice that does not meet s 31", cite: "s 31(1B), (2)", what: "A bond notice payable too soon, or too large.", why: "Counted." },
    { id: "bond-60th-day", ref: "T-35", sev: "warn", label: "Bond payable on the 60th day; rent could not rise till the 61st", cite: "ss 30(1)(a), 31(1B)(a); IA s 61; FK-06",
      what: "An additional amount of bond is payable on the 60th day after its notice.",
      why: "'Earlier than 60 days after' and 'not less than 60 days after' count to days one apart. Encoding note N-14." },
    { id: "bond-over-limit", sev: "stop", label: "s 29(1)(b): a bond larger than the law allows", cite: "s 29(1)(b), (2); rr 10A, 11",
      what: "An agreement requires a bond above 4 weeks' rent (plus $350 for a pet).", why: "An offence." },

    /* s 64, s 65 */
    { id: "s64-notice", sev: "ok", label: "A notice of termination without a ground", cite: "s 64", what: "A lessor gives a valid notice under s 64.", why: "Counted." },
    { id: "s64-fixed-term", sev: "warn", label: "No s 64 notice during a fixed term", cite: "s 64(5); FK-10",
      what: "A notice without ground is given while a fixed term runs (to its expiry day, or a later s 70A possession day).", why: "Section 64(5)." },
    { id: "s64-short", sev: "warn", label: "A s 64 notice with fewer than 60 clear days is no notice", cite: "s 64(2); FK-06",
      what: "A notice names a possession day less than 60 clear days away.", why: "FK-06 reading A." },
    { id: "s64-ineffectual", sev: "warn", label: "A s 64 notice is ineffectual while s 32 proceedings or an order stand", cite: "s 65(1)(a)",
      what: "A lessor gives notice without ground while an application under s 32 is pending or an order is in force.", why: "Section 65(1)(a)." },
    { id: "s64-application", sev: "ok", label: "The tenant applies for more time under s 64(3)", cite: "s 64(3)", what: "An application within 7 days.", why: "Counted." },
    { id: "s64-application-late", sev: "warn", label: "A s 64(3) application out of time", cite: "s 64(3)", what: "An application more than 7 days after the notice.", why: "Counted." },
    { id: "s64-court", sev: "ok", label: "The court decides a s 64(3) application", cite: "s 64(4)", what: "An extension, an order that the agreement is not terminated, or an order for possession.", why: "Counted." },
    { id: "fk05", ref: "U-34", sev: "warn", label: "When an order for possession may operate (FK-05)", cite: "s 64(4)(c); FK-05",
      what: "A court is asked to make an order for possession operate outside the days FK-05 reading A allows.", why: "Reading B leaves the day at large. Encoding note N-19." },
    { id: "s65-other-notice", sev: "warn", label: "A lessor's other notice is ineffectual without the court's authority", cite: "s 65(1)(b)",
      what: "A notice under s 70A while s 32 proceedings or an order stand, not authorised.", why: "Section 65(1)(b), (2)." },
    { id: "s65-authorised", sev: "ok", label: "The court authorises a notice of termination", cite: "s 65(2)", what: "Authorisation under s 65(2).", why: "Counted." },

    /* s 70A */
    { id: "s70a-notice", sev: "ok", label: "A notice under s 70A", cite: "s 70A", what: "A valid notice ending a fixed term.", why: "Counted." },
    { id: "s70a-invalid", sev: "warn", label: "A s 70A notice naming a day before the expiry day", cite: "s 70A(4)", what: "A possession day earlier than the expiry day.", why: "Section 70A(4)." },
    { id: "s70a-late", ref: "U-27", sev: "warn", label: "A s 70A notice given too late is no notice", cite: "s 70A(3); FK-07",
      what: "A notice given less than 30 days before its possession day.", why: "FK-07 reading A: the term does not end and s 76C continues the agreement. Encoding note N-17." },
    { id: "s70a-excluded-day", ref: "U-28", sev: "warn", label: "A s 70A notice in time only because of a weekend", cite: "s 70A(3); IA s 61(1)(h); FK-08",
      what: "The 30th day before the possession day was a Saturday or Sunday, and the notice is given on the Monday.", why: "FK-08 reading A. Encoding note N-16." },
    { id: "s70a-form-30", ref: "X-39", sev: "warn", label: "A s 70A notice on the last day: the prescribed form asks a day more", cite: "s 70A(3); Form 1C; IA s 61(1)(f)",
      what: "A notice given exactly 30 days before its possession day.", why: "Encoding note N-15." },
    { id: "s70a-extends", ref: "U-26", sev: "ok", label: "A possession day after the expiry day extends the fixed term", cite: "s 70A(5); FK-10",
      what: "A notice under s 70A names a possession day after the expiry day.", why: "FK-10 reading A. Encoding note N-18." },
    { id: "s70a-after-term", ref: "L-24", sev: "warn", label: "A s 70A notice after the fixed term has ended", cite: "ss 70A, 76C(2)",
      what: "A notice under s 70A is given when s 76C already continues the agreement.",
      why: "The console does not apply it; the encoding's test of s 70A(1), (3) and (4) would accept it." },

    /* ss 26A, 26B */
    { id: "matter-arises", sev: "ok", label: "A matter in s 26B(2) arises", cite: "s 26B(2)", what: "The tenant asks for repairs, or a court order comes into force.", why: "Counted." },
    { id: "retaliatory", sev: "stop", label: "Retaliatory action", cite: "s 26A",
      what: "The lessor takes an action s 26A(a) lists, motivated by a matter in s 26B(2).", why: "The tenant may apply to a competent court for relief (s 26B(3))." },
    { id: "renewal-not-retaliatory", ref: "U-13", sev: "warn", label: "A higher rent by a further agreement is not retaliatory action", cite: "s 26A(a)(ii), (iv); FK-11",
      what: "A lessor, motivated by a repair request, offers or makes a further agreement at a higher rent.", why: "FK-11 reading A. Encoding note N-08." },
    { id: "s26b-applies", sev: "ok", label: "The tenant applies under s 26B", cite: "s 26B(2), (3)", what: "An application for relief against retaliatory action.", why: "Counted." },
    { id: "s26b-no-application", ref: "U-13", sev: "warn", label: "No s 26B application lies", cite: "ss 26A(a), 26B(2); FK-11",
      what: "A tenant seeks relief where the lessor has taken no listed action after a matter arose.", why: "Section 26B(2)." },
    { id: "s26b-set-aside", sev: "ok", label: "The court sets aside a retaliatory action", cite: "s 26B(4)(a)", what: "An order setting aside the lessor's action.", why: "Counted." },
    { id: "s26b-dismissed", sev: "ok", label: "The court is not satisfied an action was retaliatory", cite: "s 26B(4)", what: "No order under s 26B(4).", why: "Counted." },
    { id: "offer-made", sev: "ok", label: "The lessor offers a further agreement", cite: "s 26A(a)(iv)", what: "An offer of a further agreement.", why: "Counted." },
    { id: "refusal", sev: "ok", label: "The lessor refuses a further agreement", cite: "s 26A(a)(iv)", what: "A refusal to enter into a further agreement.", why: "Counted." },

    /* s 32 */
    { id: "s32-applied", sev: "ok", label: "The tenant applies under s 32 in time", cite: "s 32(1), (2)", what: "An application within 30 days of a trigger.", why: "Counted." },
    { id: "s32-no-trigger", ref: "L-14", sev: "warn", label: "No s 32 application: no notice of an increase was received", cite: "s 32(2)",
      what: "A tenant whose rent was set by a new agreement seeks to challenge it.", why: "Section 32(2) has no trigger for it. Encoding note N-09." },
    { id: "s32-late", sev: "warn", label: "A s 32 application out of time", cite: "s 32(2)", what: "An application more than 30 days after the trigger.", why: "Counted." },
    { id: "s32-refused", sev: "ok", label: "No order under s 32", cite: "s 32(2)-(4)", what: "The court refuses, or the application is out of time.", why: "Counted." },
    { id: "s32-order", sev: "ok", label: "An order under s 32 fixes the most rent", cite: "s 32(4), (5)", what: "An order that the rent shall not exceed an amount.", why: "Counted." },
    { id: "s32-lapse", sev: "ok", label: "An order under s 32 runs its period", cite: "s 32(5)", what: "The period fixed (6 months at most) ends.", why: "Counted." },
    { id: "s32-lapse-tenancy", ref: "U-15", sev: "warn", label: "An order under s 32 lapses when the tenancy ends", cite: "s 32(5); FK-23",
      what: "The agreement the order was made under terminates before the order's period ends.", why: "FK-23 reading A. Encoding note N-10." },
    { id: "s32-offence", sev: "stop", label: "s 32(7): rent demanded above an order", cite: "s 32(7)", what: "A lessor demands more than an order in force allows.", why: "An offence." },
    { id: "fk23", ref: "U-15", sev: "warn", label: "A new agreement after an order under s 32 (FK-23)", cite: "s 32(5); FK-23",
      what: "The tenant stays on under a new agreement after an order made under the old one.", why: "On FK-23 reading A the order is gone and the new rent may exceed it; on reading B it runs on. Encoding note N-10." },

    /* s 82 */
    { id: "s82-offence", ref: "E-16", sev: "stop", label: "s 82(2): an agreement made to evade the Act", cite: "s 82(2)",
      what: "An agreement entered into with intent to defeat, evade or prevent the operation of the Act.", why: "An offence; whether that was the intent is a fact. Encoding note N-28." },

    /* added at 8A (5 Oct 2026), for LQA candidates */
    { id: "mixed-tenants", ref: "L-07", sev: "warn", label: "A continuation between one tenant and co-tenants", cite: "s 31B(3)(b); s 3 'party' (a)",
      what: "A continuing agreement has co-tenants where the existing one had a single tenant, or the reverse.",
      why: "Read word for word, s 31B(3)(b) ('the tenant, or at least 1 co-tenant, is the same under both agreements') is met by neither limb; the encoding and the console count any tenant in common." },
    { id: "relet-new-tenant", ref: "L-05", sev: "warn", label: "Premises let again to a new tenant at more rent", cite: "ss 30(1)(b), 31B(2), (3)",
      what: "Within 92 days after a tenancy ends, the premises are let to a tenant who was not a party to it, at a higher rent.",
      why: "No tenant is the same, so the new agreement continues nothing: its rent is not limited and its 12 months run afresh. The limit attaches to the tenancy, not the premises (encoding note N-07)." },
    { id: "notice-under-replaced", ref: "L-04", sev: "warn", label: "A notice without a ground under an agreement the parties replaced", cite: "ss 60(1), 64(1), (5)",
      what: "The lessor gives notice under s 64 under a periodic agreement that the parties replaced in place with a fixed term, the tenant staying.",
      why: "The replaced agreement never ended (s 60(1)), so it can be ended without a ground during the new agreement's fixed term (encoding note N-05)." },
    { id: "s65-later-proceedings", ref: "T-33", sev: "warn", label: "Proceedings under s 32 begun after a notice under s 64", cite: "s 65(1)(a)",
      what: "A tenant applies under s 32 while a notice without a ground, given earlier, is running.",
      why: "Section 65(1)(a) does not say whether a notice given before the proceedings is 'ineffectual', or whether it revives if they fail." },
    { id: "demand-unlawful-increase", ref: "E-32", sev: "warn", label: "The lessor demands more rent than is payable", cite: "ss 27(1), 30(1), 32(7)",
      what: "A lessor demands a higher rent than the agreement, as varied under ss 30 and 31A, makes payable, with no order under s 32 in force.",
      why: "The Act states no consequence for it; s 32(7) reaches only a demand above an order." }
  ];

  /* scenario helpers: an agreement for 1 Example St with Lena and Tom unless said otherwise */
  function agreement(as, label, attrs, rels) {
    var r = { lessor: "l1", tenant: "t1", premises: "pr1" }, k;
    for (k in (rels || {})) if (rels.hasOwnProperty(k)) r[k] = rels[k];
    return { spawn: "agreement", as: as, label: label, attrs: attrs, rels: r };
  }
  function lena(action, target, params) { return { actor: "l1", action: action, target: target, params: params || {} }; }
  function tom(action, target, params) { return { actor: "t1", action: action, target: target, params: params || {} }; }
  function court(action, target, params) { return { actor: "ct", action: action, target: target, params: params || {} }; }
  var FIXED = function (months, rent, more) { var a = { kind: "fixed", termMonths: months, startsIn: 0, rent: rent, bond: 4 * rent }, k; for (k in (more || {})) a[k] = more[k]; return a; };
  var PERIODIC = function (rent, more) { var a = { kind: "periodic", startsIn: 0, rent: rent, bond: 4 * rent }, k; for (k in (more || {})) a[k] = more[k]; return a; };

  /* the first part of several of the brief's scenarios: an agreement from 1 Jan 2025 whose rent rose
     by notice on 1 Jan 2026 (notice of 1 Oct 2025), then ended on 30 Jun 2026 */
  function fromJanuary2025(as, label, attrs, rels, rent) {
    return [
      { tick: 366 },
      agreement(as, label, attrs, rels),
      { tick: 273 },
      lena("noticeIncrease", "@" + as, { rent: rent, inDays: 92 })
    ];
  }

  var SCENARIOS = [
    /* ---- one per key rule ---- */
    { label: "s 30: a periodic tenancy's rent rises by notice 12 months after it began", focus: "@p", mode: "nature",
      description: "cases.l4, s 30 under one agreement: tenancy from 1 Mar 2025; a notice of 1 Dec 2025 for $550 from 1 Mar 2026 increases the rent (1 Mar 2026 is the last day of the 12 months: FK-15 A).",
      steps: [ { tick: 425 }, agreement("p", "P", PERIODIC(500)), { tick: 275 }, lena("noticeIncrease", "@p", { rent: 550, inDays: 90 }), { tick: 90 } ] },
    { label: "s 30(1)(b): an increase a day short of 12 months has no effect", focus: "@p", mode: "nature",
      description: "cases.l4: the same notice for 28 Feb 2026 fails s 30(1)(b).",
      steps: [ { tick: 425 }, agreement("p", "P", PERIODIC(500)), { tick: 275 }, lena("noticeIncrease", "@p", { rent: 550, inDays: 89 }), { tick: 89 } ] },
    { label: "s 30(1)(a): 60 days are 60 clear days", focus: "@p", mode: "nature",
      description: "cases.l4, FK-06: a notice given 1 Jan 2026 for 2 Mar 2026 (the 60th day after) fails on reading A; the earliest day it could name is 3 Mar 2026.",
      steps: [ { tick: 425 }, agreement("p", "P", PERIODIC(500)), { tick: 306 }, lena("noticeIncrease", "@p", { rent: 550, inDays: 60 }), { tick: 60 } ] },
    { label: "s 30(1)(b): the 12 months run from the day the last increase took effect", focus: "@p", mode: "nature",
      description: "cases.l4, FK-02: after an increase on 1 Mar 2026 (noticed 1 Dec 2025), a notice for 1 Jan 2027 fails on reading A; on reading B (from the notice day) it would succeed.",
      steps: [ { tick: 425 }, agreement("p", "P", PERIODIC(500)), { tick: 275 }, lena("noticeIncrease", "@p", { rent: 550, inDays: 90 }),
               { tick: 304 }, lena("noticeIncrease", "@p", { rent: 600, inDays: 92 }), { tick: 92 } ] },
    { label: "s 85: a notice of increase sent by email is not given", focus: "@p", mode: "nature",
      description: "cases.l4, FK-12: P's notice emailed with the tenant's consent does not increase the rent.",
      steps: [ { tick: 425 }, agreement("p", "P", PERIODIC(500)), { tick: 275 }, lena("noticeIncrease", "@p", { rent: 550, inDays: 90, how: "email" }), { tick: 90 } ] },
    { label: "s 31: the bond rises with the rent", focus: "@p", mode: "nature",
      description: "cases.l4, s 31: rent to $550 from 1 Mar 2026; a bond notice handed over 1 Dec 2025 for $200 payable 1 Mar 2026 takes the $2,000 bond to $2,200, 4 weeks of $550.",
      steps: [ { tick: 425 }, agreement("p", "P", PERIODIC(500, { bond: 2000 })), { tick: 275 },
               lena("noticeIncrease", "@p", { rent: 550, inDays: 90 }), lena("increaseBond", "@p", { amount: 200, inDays: 90 }), { tick: 90 } ] },
    { label: "s 31(1B)(a): bond payable on the 60th day, a day before rent could rise", focus: "@p", mode: "nature",
      description: "cases.l4 and encoding note N-14: a bond notice handed over 5 Jan 2026 may make $200 payable on 6 Mar 2026, the 60th day after.",
      steps: [ { tick: 425 }, agreement("p", "P", PERIODIC(500, { bond: 2000 })), { tick: 275 },
               lena("noticeIncrease", "@p", { rent: 550, inDays: 90 }), { tick: 35 }, lena("increaseBond", "@p", { amount: 200, inDays: 60 }), { tick: 60 } ] },
    { label: "s 64(2): 60 clear days' notice without a ground", focus: "@p", mode: "nature",
      description: "cases.l4: a notice of 1 Mar 2026 for 30 Apr 2026 is not a notice under s 64 (FK-06 A); one for 1 May 2026 is.",
      steps: [ { tick: 425 }, agreement("p", "P", PERIODIC(500)), { tick: 365 },
               lena("give64", "@p", { inDays: 60 }), lena("give64", "@p", { inDays: 61 }) ] },
    { label: "s 65(1)(a): no notice without a ground while s 32 proceedings are pending", focus: "@p", mode: "nature",
      description: "cases.l4, s 65: the tenant applies under s 32 (a reduction in facilities); the lessor's s 64 notice is ineffectual.",
      steps: [ { tick: 425 }, agreement("p", "P", PERIODIC(500)), { tick: 365 },
               tom("apply32", "@p", { reduction: true }), lena("give64", "@p", { inDays: 61 }) ] },
    { label: "s 64(4)(a): the court extends the notice; the tenant leaves at its end", focus: "@p", mode: "nature",
      description: "s 64(3), (4)(a): a notice for 1 May 2026, an application the same day, 30 more days; vacant possession on 31 May 2026 ends the agreement (s 60(1)(a)(i)).",
      steps: [ { tick: 425 }, agreement("p", "P", PERIODIC(500)), { tick: 365 },
               lena("give64", "@p", { inDays: 61 }), tom("apply64", "@p"), court("decide64", "@p", { extendDays: 30 }),
               { tick: 91 }, tom("vacate", "@p") ] },
    { label: "s 64(4)(c): an order for possession from 3 May, made on 20 April (FK-05)", focus: "@p", mode: "nature",
      description: "cases.l4, FK-05: notice received 1 Mar 2026; on an order made 20 Apr 2026, reading A allows 1 May only; 3 May fails on A and would do on B.",
      steps: [ { tick: 425 }, agreement("p", "P", PERIODIC(500)), { tick: 365 },
               lena("give64", "@p", { inDays: 61 }), tom("apply64", "@p"), { tick: 50 }, court("decide64", "@p", { possessionInDays: 13 }) ] },
    { label: "s 70A(3): a notice 29 days before the possession day is no notice (FK-07)", focus: "@f", mode: "nature",
      description: "cases.l4: for possession on 31 Dec 2026 the notice must be given by 1 Dec; one given 2 Dec is not a notice under s 70A (FK-07 A), and s 76C continues the agreement from 1 Jan 2027.",
      steps: [ { tick: 731 }, agreement("f", "F", FIXED(12, 500)), { tick: 335 }, lena("give70A", "@f", { inDays: 29 }), { tick: 30 } ] },
    { label: "s 70A(3), (5): a notice in time because of a weekend, for a day after the expiry day (FK-08, FK-10)", focus: "@f", mode: "nature",
      description: "cases.l4: for possession on Mon 4 Jan 2027 the 30th day before is Sat 5 Dec 2026; a notice given Mon 7 Dec is in time on FK-08 A. The term runs to 4 Jan 2027 (s 70A(5); FK-10 A), when the tenant leaves.",
      steps: [ { tick: 731 }, agreement("f", "F", FIXED(12, 500)), { tick: 340 }, lena("give70A", "@f", { inDays: 28 }), { tick: 28 }, tom("vacate", "@f") ] },
    { label: "s 70A: the tenant's notice for the expiry day, and the tenant leaves on it (FK-09)", focus: "@f", mode: "nature",
      description: "cases.l4, FK-09: an agreement terminated on its expiry day after a notice under s 70A is not continued by s 76C on reading A. The notice is given exactly 30 days before (encoding note N-15).",
      steps: [ { tick: 731 }, agreement("f", "F", FIXED(12, 500)), { tick: 334 }, tom("give70A", "@f"), { tick: 30 }, tom("vacate", "@f") ] },
    { label: "s 32: an order, a demand above it, and the end of its period", focus: "@p", mode: "nature",
      description: "cases.l4, s 32(5), (7): an order made 1 Mar 2026 for 7 months is cut to 6 (to 31 Aug 2026); demanding more on 1 Jun is an offence; on 1 Sep it has lapsed.",
      steps: [ { tick: 425 }, agreement("p", "P", PERIODIC(500)), { tick: 365 },
               tom("apply32", "@p", { reduction: true }), court("order32", "@p", { max: 450, months: 7 }),
               { tick: 92 }, lena("demandRent", "@p", { amount: 500 }), { tick: 92 } ] },
    { label: "s 31A(1): income-based rent rises with income, the method unchanged (FK-20)", focus: "@j1", mode: "nature",
      description: "cases.l4, FK-20: a rise from the unchanged method applied to a higher income is permitted on reading A.",
      steps: [ { tick: 366 }, agreement("j1", "J1", PERIODIC(300, { incomeBased: true })), { tick: 30 }, { actor: "@j1", action: "incomeRises", params: { rent: 320 } } ] },
    { label: "s 60(2): a co-tenant leaves and another joins", focus: "@c1", mode: "nature",
      description: "cases.l4, s 60(2): one co-tenant's interest ending does not end the agreement for the other.",
      steps: [ { tick: 366 }, agreement("c1", "C1", PERIODIC(500), { cotenant: "t2" }), { tick: 30 },
               { actor: "t2", action: "leaveAgreement", target: "@c1" }, { actor: "t3", action: "joinAsCotenant", target: "@c1" } ] },
    { label: "s 60(1): moving out early does not end the agreement", focus: "@p", mode: "nature",
      description: "s 60(1): vacant possession with no notice period run and no written agreement is not a circumstance that ends it.",
      steps: [ { tick: 425 }, agreement("p", "P", PERIODIC(500)), { tick: 30 }, tom("vacate", "@p") ] },
    { label: "s 100(4): a notice given before 29 July 2024 for an increase after it", focus: "@pa",
      description: "cases.l4, Part 7 (scenario mode: a tenancy from 1 Sep 2023 and a notice of 1 Dec 2023 are set by hand). The increase of 1 Mar 2024 stands (FK-21 A). A notice of 1 Jun 2024 for 1 Sep 2024 is reached by s 100(4) and fails the present s 30.",
      steps: [ agreement("pa", "PA", PERIODIC(500, { startsIn: -122 }), { premises: "pr1" }),
               { set: "@pa", attrs: { incPending: true, incSent: -31, incGiven: -31, incGivenDate: "1 Dec 2023", incEffect: 60, incEffectDate: "1 Mar 2024", incRent: 520, incForm: "minister", incHow: "personally" } },
               { tick: 60 }, { tick: 92 }, lena("noticeIncrease", "@pa", { rent: 540, inDays: 92, form: "minister" }), { tick: 92 } ] },
    { label: "s 100(4) and IA s 74: a notice in the Minister's form that complies (FK-26)", focus: "@pa",
      description: "cases.l4, Part 7 (scenario mode): the same tenancy; a notice of 1 Jun 2024 for 1 Mar 2025 complies with the present s 30, its Minister's form saved by IA s 74 (FK-26 A).",
      steps: [ agreement("pa", "PA", PERIODIC(500, { startsIn: -122 }), { premises: "pr1" }),
               { set: "@pa", attrs: { incPending: true, incSent: -31, incGiven: -31, incGivenDate: "1 Dec 2023", incEffect: 60, incEffectDate: "1 Mar 2024", incRent: 520, incForm: "minister", incHow: "personally" } },
               { tick: 152 }, lena("noticeIncrease", "@pa", { rent: 540, inDays: 273, form: "minister" }), { tick: 273 } ] },
    { label: "s 99: a two-year term keeps the 6-month rule to its end, then the 12-month rule (FK-22, FK-04)", focus: "@fa", mode: "nature",
      description: "cases.l4, Part 7: FA from 1 Jan 2024 to 31 Dec 2025. Increases on 1 Jul 2024, 1 Jan 2025 and 1 Jul 2025 under the former s 30; a notice of 1 Oct 2025 for 1 Jan 2026 is governed by the present s 30 (FK-22 A) and fails, the 12 months running from 1 Jul 2025 (FK-04 A).",
      steps: [ agreement("fa", "FA", FIXED(24, 500, { setOut: true })),
               { tick: 91 }, lena("noticeIncrease", "@fa", { rent: 520, inDays: 91, form: "minister" }),
               { tick: 183 }, lena("noticeIncrease", "@fa", { rent: 540, inDays: 92, form: "minister" }),
               { tick: 182 }, lena("noticeIncrease", "@fa", { rent: 560, inDays: 91, form: "minister" }),
               { tick: 183 }, lena("noticeIncrease", "@fa", { rent: 580, inDays: 92 }), { tick: 92 } ] },
    { label: "s 30: notices that do not raise the rent (not the lessor, no approved form, excluded, withdrawn)", focus: "@p", mode: "nature",
      description: "cases.l4, s 30(1)-(3): Theo, not the lessor, achieves nothing; a notice in no approved form fails; under X, which excludes increases, a notice fails (s 30(2)(b)); a withdrawn notice does not vary the agreement (s 30(3)).",
      steps: [ { tick: 425 }, agreement("p", "P", PERIODIC(500)), agreement("x", "X", PERIODIC(500, { excluded: true }), { premises: "pr2", tenant: "t2" }),
               { tick: 275 }, { actor: "t3", action: "noticeIncrease", target: "@p", params: { rent: 550 } },
               lena("noticeIncrease", "@p", { rent: 550, inDays: 90, form: "none" }), lena("noticeIncrease", "@x", { rent: 550, inDays: 90 }),
               { tick: 90 }, lena("noticeIncrease", "@p", { rent: 550, inDays: 92 }), lena("withdrawIncrease", "@p") ] },
    { label: "s 29(1)(b), s 31(2): bonds above the limits", focus: "@p", mode: "nature",
      description: "cases.l4, ss 29 and 31: at $500 a week with a pet the bond may be $2,350, so $2,400 is an offence; with the rent rising to $550, a further $250 on a $2,000 bond (no pet) passes 4 weeks' rent.",
      steps: [ { tick: 425 }, agreement("p", "P", PERIODIC(500, { bond: 2000 })), agreement("q", "Q", PERIODIC(500, { bond: 2400, petPermitted: true }), { premises: "pr2", tenant: "t2" }),
               { tick: 275 }, lena("noticeIncrease", "@p", { rent: 550, inDays: 90 }), lena("increaseBond", "@p", { amount: 250, inDays: 90 }) ] },
    { label: "s 31(1A): a change of method that lowers the rent still supports a bond increase (FK-25)", focus: "@j1", mode: "nature",
      description: "cases.l4, FK-25: a notice under s 31A whose change lowers the rent is a 'notice of increase in rent' on reading A, so the bond may rise within s 31(2).",
      steps: [ { tick: 366 }, agreement("j1", "J1", PERIODIC(300, { incomeBased: true, bond: 1000 })), { tick: 273 },
               lena("noticeChange", "@j1", { rent: 280, inDays: 92 }), lena("increaseBond", "@j1", { amount: 100, inDays: 92 }), { tick: 92 } ] },
    { label: "s 32(2): an application more than 30 days after the notice", focus: "@p", mode: "nature",
      description: "cases.l4, s 32(2): notice of an increase received 1 Dec 2025; an application on 10 Jan 2026 is out of time unless the court allows a greater period, and here it does not.",
      steps: [ { tick: 425 }, agreement("p", "P", PERIODIC(500)), { tick: 275 }, lena("noticeIncrease", "@p", { rent: 550, inDays: 90 }),
               { tick: 40 }, tom("apply32", "@p"), court("order32", "@p", {}) ] },
    { label: "s 64(3): an application more than 7 days after the notice", focus: "@p", mode: "nature",
      description: "s 64(3): received Sun 1 Mar 2026, so the 7 days end on Mon 9 Mar (IA s 61(1)(e)); an application on 11 Mar is too late.",
      steps: [ { tick: 425 }, agreement("p", "P", PERIODIC(500)), { tick: 365 }, lena("give64", "@p", { inDays: 61 }), { tick: 10 }, tom("apply64", "@p") ] },
    { label: "s 65(1)(b), (2): a notice under s 70A while s 32 proceedings are pending, then authorised", focus: "@f", mode: "nature",
      description: "cases.l4, s 65: with proceedings pending, Lena's notice under s 70A is ineffectual unless first authorised; the court authorises it, and a fresh notice is good.",
      steps: [ { tick: 731 }, agreement("f", "F", FIXED(12, 500)), { tick: 273 }, tom("apply32", "@f", { reduction: true }),
               lena("give70A", "@f"), court("authorise65", "@f"), lena("give70A", "@f") ] },
    { label: "s 70A(4), and a notice after the fixed term has ended", focus: "@f", mode: "nature",
      description: "cases.l4: a possession day before the expiry day is no notice under s 70A (s 70A(4)). After s 76C has continued the agreement, the console does not apply a notice under s 70A (see ENCODING-NOTES.md).",
      steps: [ { tick: 731 }, agreement("f", "F", FIXED(12, 500)), { tick: 273 }, lena("give70A", "@f", { inDays: 60 }),
               { tick: 92 }, lena("give70A", "@f", { inDays: 60 }) ] },
    { label: "s 26B(4): the tenant believes it was retaliation; the court is not satisfied", focus: "@i1", mode: "nature",
      description: "cases.l4, s 26B(2)-(4): a s 64 notice after a repair request lets the tenant apply (s 26B(2) turns on the tenant's belief), but the lessor was not motivated by it and the court is not satisfied.",
      steps: [ { tick: 731 }, agreement("i1", "I1", PERIODIC(500)), { tick: 59 }, tom("askRepairs", "@i1"),
               { tick: 9 }, lena("give64", "@i1", { inDays: 66 }), tom("apply26B", "@i1"), court("decide26B", "@i1", { satisfied: false }) ] },
    { label: "s 26A(a)(iv): offering a further agreement at more rent, then refusing one, after a repair request (FK-11)", focus: "@i1", mode: "nature",
      description: "cases.l4, s 26A and FK-11: an offer of a further agreement at a higher rent, motivated by the repair request, is not retaliatory action on reading A; a refusal to enter into one, so motivated, is (s 26A(a)(iv)).",
      steps: [ { tick: 731 }, agreement("i1", "I1", PERIODIC(500)), { tick: 59 }, tom("askRepairs", "@i1"),
               { tick: 30 }, lena("offerFurther", "@i1", { rent: 560, months: 12, motivated: true }), lena("refuseFurther", "@i1", { motivated: true }) ] },
    { label: "C: a buyer who makes a new agreement after the old one ended", focus: "@c5", mode: "nature",
      description: "Section C: Pat buys 1 Example St on 1 Jul 2026, after C1 ended on 30 Jun, and lets it to Tom and Tia from that day at $640. The lessor under C1 at its end was Lena, so C5 is not between the same parties (s 31B(3)(a)) and starts a fresh 12 months.",
      steps: fromJanuary2025("c1", "C1", PERIODIC(500), { cotenant: "t2" }, 550).concat([
               { tick: 272 }, tom("vacate", "@c1", { written: true }),
               { tick: 1 }, { actor: "pb", action: "buyPremises", target: "pr1" }, agreement("c5", "C5", PERIODIC(640), { lessor: "pb", cotenant: "t2" }) ]) },

    /* ---- the brief's scenarios, cases-consecutive.l4 sections A to K ---- */
    { label: "A: a fixed term renewed by a new fixed term between the same parties, no notice under s 70A", focus: "@a2", mode: "nature",
      description: "Section A. A1 (1 Jan 2025 to 31 Dec 2026, $500, increases set out) rises by notice to $530 on 1 Jan 2026; a second notice for 4 Mar 2026 fails s 30(1)(b). A2 from 1 Jan 2027 at $600 continues A1 (FK-16 A), and s 76C continues A1 beside it (N-05). A2's notice given 1 Jan 2027 takes the rent to $650 from 3 Mar 2027, the earliest day: the 12 months ran from 1 Jan 2026 (N-02).",
      steps: [ { tick: 366 }, agreement("a1", "A1", FIXED(24, 500, { setOut: true })), { tick: 273 },
               lena("noticeIncrease", "@a1", { rent: 530, inDays: 92 }), { tick: 93 },
               lena("noticeIncrease", "@a1", { rent: 600, inDays: 61 }), { tick: 364 },
               agreement("a2", "A2", FIXED(12, 600, { setOut: true })),
               lena("noticeIncrease", "@a2", { rent: 650 }), { tick: 61 } ] },
    { label: "B: a gap of one day between agreements", focus: "@b2", mode: "nature",
      description: "Section B. B1 (periodic from 1 Jan 2025) rises to $540 on 1 Jan 2026 and ends on 30 Jun 2026 after a notice under s 64. B2 starts on 2 Jul 2026 at $620: not a continuation (N-03). A notice for 1 Jan 2027 fails; one for 2 Jul 2027 succeeds.",
      steps: fromJanuary2025("b1", "B1", PERIODIC(500), null, 540).concat([
               { tick: 182 }, lena("give64", "@b1", { inDays: 90 }), { tick: 90 }, tom("vacate", "@b1"),
               { tick: 2 }, agreement("b2", "B2", PERIODIC(620)),
               { tick: 91 }, lena("noticeIncrease", "@b2", { rent: 660, inDays: 92 }),
               { tick: 182 }, lena("noticeIncrease", "@b2", { rent: 660, inDays: 92 }), { tick: 92 } ]) },
    { label: "B: with no gap, the new agreement continues the old", focus: "@b2x", mode: "nature",
      description: "Section B, B2x: from 1 Jul 2026 it continues B1 (FK-17 A), so a notice for 1 Jan 2027 succeeds: the 12 months ran from B1's increase on 1 Jan 2026. The $620 it fixed was not limited (FK-01 A).",
      steps: fromJanuary2025("b1", "B1", PERIODIC(500), null, 540).concat([
               { tick: 182 }, lena("give64", "@b1", { inDays: 90 }), { tick: 90 }, tom("vacate", "@b1"),
               { tick: 1 }, agreement("b2x", "B2x", PERIODIC(620)),
               { tick: 92 }, lena("noticeIncrease", "@b2x", { rent: 660, inDays: 92 }), { tick: 92 } ]) },
    { label: "C: one co-tenant in common is enough to continue", focus: "@c2", mode: "nature",
      description: "Section C. C1 (Tom and Tia, periodic from 1 Jan 2025) rises to $550 on 1 Jan 2026 and ends 30 Jun 2026. C2 (Tia and Theo) from 1 Jul 2026 at $620 continues it; its notice for 1 Jan 2027 succeeds.",
      steps: fromJanuary2025("c1", "C1", PERIODIC(500), { cotenant: "t2" }, 550).concat([
               { tick: 272 }, tom("vacate", "@c1", { written: true }),
               { tick: 1 }, agreement("c2", "C2", PERIODIC(620), { tenant: "t2", cotenant: "t3" }),
               { tick: 92 }, lena("noticeIncrease", "@c2", { rent: 650, inDays: 92 }), { tick: 92 } ]) },
    { label: "C: a new tenant, a rent set at will and a fresh 12 months", focus: "@c3", mode: "nature",
      description: "Section C, C3: Theo alone from 1 Jul 2026 at $700 shares no tenant with C1 (N-07). A notice for 1 Jan 2027 fails; one given 1 Apr 2027 for 1 Jul 2027 succeeds.",
      steps: fromJanuary2025("c1", "C1", PERIODIC(500), { cotenant: "t2" }, 550).concat([
               { tick: 272 }, tom("vacate", "@c1", { written: true }),
               { tick: 1 }, agreement("c3", "C3", PERIODIC(700), { tenant: "t3" }),
               { tick: 92 }, lena("noticeIncrease", "@c3", { rent: 730, inDays: 92 }),
               { tick: 182 }, lena("noticeIncrease", "@c3", { rent: 730, inDays: 91 }), { tick: 91 } ]) },
    { label: "C: a buyer of the premises renews with the same tenants (FK-13)", focus: "@c4", mode: "nature",
      description: "Section C, C4: Pat buys 1 Example St on 1 Jun 2026 and becomes C1's lessor (s 3 'lessor'); C1 ends 30 Jun; C4 (Pat; Tom and Tia) from 1 Jul 2026 at $640 continues C1 on FK-13 A, not on reading B.",
      steps: fromJanuary2025("c1", "C1", PERIODIC(500), { cotenant: "t2" }, 550).concat([
               { tick: 243 }, { actor: "pb", action: "buyPremises", target: "pr1" },
               { tick: 29 }, tom("vacate", "@c1", { written: true }),
               { tick: 1 }, agreement("c4", "C4", PERIODIC(640), { lessor: "pb", cotenant: "t2" }) ]) },
    { label: "D: a notice in the fixed term for the day after it; s 76C continues the agreement", focus: "@d1", mode: "nature",
      description: "Section D. D1 (fixed term for 2025, nothing set out): a notice of 1 Oct 2025 for 1 Jan 2026 succeeds (FK-03 A, the 12 months from 1 Jan 2025); D1 continues as a periodic tenancy from 1 Jan 2026 (s 76C).",
      steps: [ { tick: 366 }, agreement("d1", "D1", FIXED(12, 500)), { tick: 273 }, lena("noticeIncrease", "@d1", { rent: 540, inDays: 92 }), { tick: 92 } ] },
    { label: "D: an increase during the fixed term, nothing set out", focus: "@d1", mode: "nature",
      description: "Section D: the same notice for 31 Dec 2025 is not exercisable (s 30(2)(a)).",
      steps: [ { tick: 366 }, agreement("d1", "D1", FIXED(12, 500)), { tick: 273 }, lena("noticeIncrease", "@d1", { rent: 540, inDays: 91 }), { tick: 91 } ] },
    { label: "D: after s 76C, the 12 months run from the first commencement (FK-19)", focus: "@d1", mode: "nature",
      description: "Section D: with no increase before, a notice of 1 Mar 2026 for 1 Jun 2026 succeeds on FK-19 A (12 months from 1 Jan 2025); on reading B it would fail.",
      steps: [ { tick: 366 }, agreement("d1", "D1", FIXED(12, 500)), { tick: 424 }, lena("noticeIncrease", "@d1", { rent: 540, inDays: 92 }), { tick: 92 } ] },
    { label: "E: periodic to fixed term, the tenant staying on", focus: "@e2", mode: "nature",
      description: "Section E(i). E1 (periodic from 1 Jan 2025, $540 from 1 Jan 2026): the parties agree to replace it and the tenant stays, so it does not end (N-05). E2 (fixed, from 1 Jul 2026, $600) continues nothing; its notice for 1 Jan 2027 fails.",
      steps: fromJanuary2025("e1", "E1", PERIODIC(500), null, 540).concat([
               { tick: 272 }, lena("agreeToEnd", "@e1"),
               { tick: 1 }, agreement("e2", "E2", FIXED(12, 600, { setOut: true })),
               { tick: 92 }, lena("noticeIncrease", "@e2", { rent: 630, inDays: 92 }), { tick: 92 } ]) },
    { label: "E: periodic to fixed term after vacant possession", focus: "@e2", mode: "nature",
      description: "Section E(ii). E1 ends 30 Jun 2026 with vacant possession under a written agreement (s 60(1)(g)); E2 from 1 Jul 2026 continues it (FK-17 A), and its notice for 1 Jan 2027 succeeds.",
      steps: fromJanuary2025("e1", "E1", PERIODIC(500), null, 540).concat([
               { tick: 272 }, tom("vacate", "@e1", { written: true }),
               { tick: 1 }, agreement("e2", "E2", FIXED(12, 600, { setOut: true })),
               { tick: 92 }, lena("noticeIncrease", "@e2", { rent: 630, inDays: 92 }), { tick: 92 } ]) },
    { label: "F: six-monthly fixed terms at $500, $550 and $600", focus: "@f3", mode: "nature",
      description: "Section F. Each term continues the last (FK-16 A) and s 76C continues each beside the next (N-05). Each rise is by agreement, not under s 30 (FK-01 A; N-01). F2 follows a repair request and was made to evade the Act: not retaliatory action (FK-11 A; N-08), but an offence under s 82(2) (N-28). Its tenant cannot apply under s 32 (N-09) or s 26B, and the bond cannot rise under s 31. For F3 the 12 months run from 1 Jan 2027 (FK-18 A).",
      steps: [ { tick: 731 }, agreement("f1", "F1", FIXED(6, 500)), { tick: 120 }, tom("askRepairs", "@f1"),
               { tick: 61 }, agreement("f2", "F2", FIXED(6, 550, { motivatedByMatter: true, intentToEvade: true })),
               tom("apply26B", "@f2"), { tick: 9 }, tom("apply32", "@f2"), lena("increaseBond", "@f2", { amount: 100 }),
               { tick: 175 }, agreement("f3", "F3", FIXED(6, 600)) ] },
    { label: "F: the same rise by notice under one agreement fails", focus: "@g", mode: "nature",
      description: "Section F, agreement G: periodic from 1 Jan 2026; a notice of 1 Apr 2026 for $550 from 1 Jul 2026 fails s 30(1)(b).",
      steps: [ { tick: 731 }, agreement("g", "G", PERIODIC(500)), { tick: 90 }, lena("noticeIncrease", "@g", { rent: 550, inDays: 91 }), { tick: 91 } ] },
    { label: "G: from the former s 30 to the present one across a renewal (FK-04)", focus: "@g2", mode: "nature",
      description: "Section G. G1 (1 Feb 2024 to 31 Jan 2025, s 99) rises to $520 on 1 Aug 2024 under the former s 30 (6 months). G2 from 1 Feb 2025 continues it; its notice for 1 Aug 2025 succeeds, 12 months after G1's increase (FK-04 A); on reading B it would fail.",
      steps: [ { tick: 31 }, agreement("g1", "G1", FIXED(12, 500, { setOut: true })), { tick: 90 },
               lena("noticeIncrease", "@g1", { rent: 520, inDays: 92, form: "minister" }), { tick: 276 },
               agreement("g2", "G2", FIXED(12, 560, { setOut: true })), { tick: 89 },
               lena("noticeIncrease", "@g2", { rent: 580, inDays: 92 }), { tick: 92 } ] },
    { label: "H: an order under s 32, then a new agreement (FK-23)", focus: "@h2", mode: "nature",
      description: "Section H. H1 (periodic from 1 Jan 2026, $600): order of 1 Mar 2026 fixing $500 to 31 Aug 2026; a s 64 notice on 15 Apr is ineffectual (s 65(1)(a)). H1 ends 30 Apr and the order lapses with it (FK-23 A; N-10). H2 from 1 May at $650; demanding $650 on 15 May is not an offence (on reading B it would be).",
      steps: [ { tick: 731 }, agreement("h1", "H1", PERIODIC(600)), { tick: 59 },
               tom("apply32", "@h1", { reduction: true }), court("order32", "@h1", { max: 500, months: 6 }),
               { tick: 45 }, lena("give64", "@h1", { inDays: 61 }),
               { tick: 15 }, tom("vacate", "@h1", { written: true }),
               { tick: 1 }, agreement("h2", "H2", PERIODIC(650)),
               { tick: 14 }, lena("demandRent", "@h2", { amount: 650 }) ] },
    { label: "I: ending a periodic tenancy without a ground after a repair request", focus: "@i1", mode: "nature",
      description: "Section I. Tom asks for repairs on 1 Mar 2026; on 10 Mar Lena gives a s 64 notice for 15 May, motivated by it. It is a notice under s 64 (60 clear days) and retaliatory action (s 26A(a)(iii)); Tom applies under s 26B and the court sets it aside.",
      steps: [ { tick: 731 }, agreement("i1", "I1", PERIODIC(500)), { tick: 59 }, tom("askRepairs", "@i1"),
               { tick: 9 }, lena("give64", "@i1", { inDays: 66, motivated: true }),
               tom("apply26B", "@i1"), court("decide26B", "@i1", { satisfied: true }) ] },
    { label: "J: income-based rent across agreements (s 31A, s 31B(1)(b))", focus: "@j2", mode: "nature",
      description: "Section J. J1's method changed from 1 Jan 2026; J1 ends 30 Jun 2026 and J2 continues it from 1 Jul. A change for 1 Oct 2026 fails, and a notice under s 30 is no way round it; a change for 1 Jan 2027 succeeds.",
      steps: [ { tick: 366 }, agreement("j1", "J1", PERIODIC(300, { incomeBased: true })), { tick: 273 },
               lena("noticeChange", "@j1", { rent: 310, inDays: 92 }), { tick: 272 }, tom("vacate", "@j1", { written: true }),
               { tick: 1 }, agreement("j2", "J2", PERIODIC(310, { incomeBased: true })),
               lena("noticeChange", "@j2", { rent: 320, inDays: 92 }), lena("noticeIncrease", "@j2", { rent: 330, inDays: 92 }),
               { tick: 92 }, lena("noticeChange", "@j2", { rent: 320, inDays: 92 }), { tick: 92 } ] },
    { label: "J: income-based rent after a gap", focus: "@j3", mode: "nature",
      description: "Section J, J3 from 3 Jul 2026: not a continuation, so a change for 1 Jan 2027 fails and one for 3 Jul 2027 succeeds.",
      steps: [ { tick: 366 }, agreement("j1", "J1", PERIODIC(300, { incomeBased: true })), { tick: 273 },
               lena("noticeChange", "@j1", { rent: 310, inDays: 92 }), { tick: 272 }, tom("vacate", "@j1", { written: true }),
               { tick: 3 }, agreement("j3", "J3", PERIODIC(310, { incomeBased: true })),
               lena("noticeChange", "@j3", { rent: 320, inDays: 182 }), { tick: 182 },
               lena("noticeChange", "@j3", { rent: 320, inDays: 183 }), { tick: 183 } ] },
    { label: "K: a notice under s 70A moves the end of the term, and the renewal follows it", focus: "@k2", mode: "nature",
      description: "Section K. K1 (fixed term for 2025): Lena's notice of 1 Nov 2025 for 31 Jan 2026 moves the end of the term (s 70A(5); FK-10 A); a s 64 notice on 10 Jan 2026 is no notice (s 64(5)). K2 from 1 Feb 2026 continues K1; K1, not having ended, runs on under s 76C.",
      steps: [ { tick: 366 }, agreement("k1", "K1", FIXED(12, 500)), { tick: 304 }, lena("give70A", "@k1", { inDays: 91 }),
               { tick: 70 }, lena("give64", "@k1", { inDays: 68 }),
               { tick: 22 }, agreement("k2", "K2", FIXED(12, 580)) ] },
    { label: "K: a renewal from the old expiry day is not a continuation", focus: "@k2x", mode: "nature",
      description: "Section K, K2x from 1 Jan 2026: K1's term runs to 31 Jan 2026, so K2x does not start immediately after it (FK-10 A); on reading B it would.",
      steps: [ { tick: 366 }, agreement("k1", "K1", FIXED(12, 500)), { tick: 304 }, lena("give70A", "@k1", { inDays: 91 }),
               { tick: 61 }, agreement("k2x", "K2x", FIXED(12, 580)) ] },

    /* ---- added at 8A (5 Oct 2026), to demonstrate LQA candidates ---- */
    { label: "s 31B(3)(b): a sole tenant renews with a co-tenant added", focus: "@y2", mode: "nature",
      description: "Y1 (Tom alone, periodic from 1 Jan 2025) rises by notice to $550 on 1 Jan 2026 and ends 30 Jun 2026 with vacant possession under a written agreement. Y2 (Tom and Tia) from 1 Jul 2026 at $620 is a continuation on the reading the encoding and the console take (any tenant in common), so its notice for 1 Jan 2027 succeeds. Read word for word, s 31B(3)(b) is met by neither limb.",
      steps: fromJanuary2025("y1", "Y1", PERIODIC(500), null, 550).concat([
               { tick: 272 }, tom("vacate", "@y1", { written: true }),
               { tick: 1 }, agreement("y2", "Y2", PERIODIC(620), { cotenant: "t2" }),
               { tick: 92 }, lena("noticeIncrease", "@y2", { rent: 650, inDays: 92 }), { tick: 92 } ]) },
    { label: "Ending a periodic tenancy without a ground, and letting to a new tenant at more rent", focus: "@z2", mode: "nature",
      description: "Z1 (Tom, periodic from 1 Jan 2025) rises by notice to $550 on 1 Jan 2026. On 1 Mar 2026 Lena gives notice without a ground for 1 May 2026 (s 64), and Tom leaves that day. On 2 May she lets the premises to Theo at $700: not a continuation (s 31B(3)(b)), so the $700 is not limited and a fresh 12 months begin. Under Z1 the rent could not have risen again before 1 Jan 2027.",
      steps: fromJanuary2025("z1", "Z1", PERIODIC(500), null, 550).concat([
               { tick: 151 }, lena("give64", "@z1", { inDays: 61 }), { tick: 61 }, tom("vacate", "@z1"),
               { tick: 1 }, agreement("z2", "Z2", PERIODIC(700), { tenant: "t3" }) ]) },
    { label: "E: the replaced periodic agreement is ended without a ground during the new fixed term", focus: "@e1", mode: "nature",
      description: "Section E(i) continued. E1 (periodic) is replaced in place by E2, a fixed term from 1 Jul 2026, and the tenant stays, so E1 does not end (s 60(1); N-05). On 1 Sep 2026 Lena gives notice without a ground under E1, for 2 Nov 2026: it is good under s 64. The same notice under E2 is no notice (s 64(5)).",
      steps: fromJanuary2025("e1", "E1", PERIODIC(500), null, 540).concat([
               { tick: 272 }, lena("agreeToEnd", "@e1"),
               { tick: 1 }, agreement("e2", "E2", FIXED(12, 600, { setOut: true })),
               { tick: 62 }, lena("give64", "@e1", { inDays: 62 }), lena("give64", "@e2", { inDays: 62 }) ]) },
    { label: "s 65(1)(a): a notice without a ground, then proceedings under s 32", focus: "@p", mode: "nature",
      description: "P (periodic from 1 Mar 2025): on 1 Dec 2025 Lena gives notice raising the rent to $600 from 1 Mar 2026, and on 6 Dec a notice without a ground for 5 Feb 2026. On 11 Dec Tom applies under s 32, in time (within 30 days of the rent notice). Section 65(1)(a) makes 'any notice ... under section 64' ineffectual while the proceedings are pending; whether that reaches a notice given before them is not said.",
      steps: [ { tick: 425 }, agreement("p", "P", PERIODIC(500)), { tick: 275 },
               lena("noticeIncrease", "@p", { rent: 600, inDays: 90 }), { tick: 5 }, lena("give64", "@p", { inDays: 61 }),
               { tick: 5 }, tom("apply32", "@p") ] },
    { label: "s 30(1): the lessor demands an increase that did not take effect", focus: "@p", mode: "nature",
      description: "P (periodic from 1 Mar 2025): a notice of 1 Dec 2025 for $550 from 28 Feb 2026 fails s 30(1)(b), a day short of 12 months. On 28 Feb 2026 Lena demands $550 anyway. The rent payable is still $500; the Act states no consequence for the demand (s 32(7) reaches only a demand above an order under s 32).",
      steps: [ { tick: 425 }, agreement("p", "P", PERIODIC(500)), { tick: 275 }, lena("noticeIncrease", "@p", { rent: 550, inDays: 89 }), { tick: 89 },
               lena("demandRent", "@p", { amount: 550 }) ] }
  ];

  var SIMULATION = {
    params: [
      { key: "owners", label: "Owners letting premises, besides Lena and Pat", def: 3, min: 0, max: 20, step: 1 },
      { key: "homes", label: "Residential premises, besides 1 and 2 Example St", def: 8, min: 1, max: 60, step: 1 },
      { key: "tenants", label: "People looking for a home", def: 12, min: 1, max: 120, step: 1 },
      { key: "startLets", label: "Of those premises, let on day 0 under tenancies that began in the year before", def: 6, min: 0, max: 60, step: 1 },
      { key: "letsPerMonth", label: "Vacant premises let to a new tenant, per month", def: 6, min: 0, max: 60, step: 0.5 },
      { key: "pFixed", label: "New agreements for a fixed term (the rest periodic)", unit: "%", def: 60, min: 0, max: 100, step: 5 },
      { key: "pIncrease", label: "Lessors who give notice of a rent increase, per month, once one could take effect within about 10 weeks", unit: "%", def: 40, min: 0, max: 100, step: 1 },
      { key: "pCompliant", label: "Notices of increase naming the earliest day the Act allows (the rest name a day at random)", unit: "%", def: 70, min: 0, max: 100, step: 5 },
      { key: "pRenew", label: "Fixed terms the lessor offers to renew, 40 days before they end", unit: "%", def: 60, min: 0, max: 100, step: 5 },
      { key: "pGap", label: "Renewals that start after a gap of a few days", unit: "%", def: 15, min: 0, max: 100, step: 5 },
      { key: "pEndNotice", label: "Fixed terms not renewed that are ended by a notice under s 70A", unit: "%", def: 50, min: 0, max: 100, step: 5 },
      { key: "pS64", label: "Periodic tenancies the lessor ends without a ground, per month", unit: "%", def: 2, min: 0, max: 50, step: 0.5 },
      { key: "pLeave", label: "Periodic tenancies ended by agreement, the tenant moving out, per month", unit: "%", def: 3, min: 0, max: 50, step: 0.5 },
      { key: "pRepair", label: "Tenants who ask for repairs, per month", unit: "%", def: 4, min: 0, max: 50, step: 0.5 },
      { key: "pSale", label: "Premises sold, per year", unit: "%", def: 5, min: 0, max: 100, step: 1 }
    ],
    generators: [
      { id: "owners", start: "$param.owners",
        spawn: { type: "person", label: "{name}", names: ["Omar", "Rosa", "Ivan", "Mei", "Ken", "Ada", "Noor", "Raj"], attrs: { isOwner: true, tenancies: 0, simulated: true } } },
      { id: "homes", start: "$param.homes",
        spawn: { type: "premises", label: "{n} Sample Rd", attrs: { occupied: 0, simulated: true, idx: ["count", "premises", "$it.attrs.simulated"] },
                 rels: { owner: ["any", "person", "$it.attrs.isOwner"] } } },
      { id: "people", start: "$param.tenants",
        spawn: { type: "person", label: "{name}", names: ["Ali", "Bea", "Cal", "Dee", "Eli", "Fay", "Gus", "Hana", "Ira", "Joy", "Kit", "Lou", "Max", "Nell"],
                 attrs: { isOwner: false, tenancies: 0, simulated: true, seeker: true, idx: ["count", "person", "$it.attrs.seeker"] } } },
      /* the k-th tenancy running on day 0 is of the k-th premises, to the k-th person */
      { id: "running", start: min(min("$param.startLets", "$param.homes"), "$param.tenants"),
        spawn: { type: "agreement", label: "Lease E{n}",
          attrs: { kind: ["if", ["chance", ["/", "$param.pFixed", 100]], "fixed", "periodic"], termMonths: ["oneOf", 6, 12, 12], startsIn: ["-", 0, ["randInt", 20, 330]],
                   rent: ["*", 10, ["randInt", 42, 78]], incomeBased: ["chance", 0.08], setOut: ["chance", 0.15], excluded: false, petPermitted: ["chance", 0.3], simulated: true },
          rels: { premises: ["any", "premises", ["and", "$it.attrs.simulated", ["=", "$it.attrs.idx", ["count", "agreement", "$it.attrs.simulated"]]]],
                  tenant: ["any", "person", ["and", "$it.attrs.seeker", ["=", "$it.attrs.idx", ["count", "agreement", "$it.attrs.simulated"]]]] } } },
      { id: "let", rate: ["/", "$param.letsPerMonth", 30],
        when: ["and", ["exists", ["any", "premises", ["and", "$it.attrs.simulated", ["=", "$it.attrs.occupied", 0]]]],
                      ["exists", ["any", "person", ["and", "$it.attrs.seeker", ["=", "$it.attrs.tenancies", 0]]]]],
        spawn: { type: "agreement", label: "Lease N{n}",
          attrs: { kind: ["if", ["chance", ["/", "$param.pFixed", 100]], "fixed", "periodic"], termMonths: ["oneOf", 6, 12, 12], startsIn: 0,
                   rent: ["*", 10, ["randInt", 42, 78]], incomeBased: ["chance", 0.08], setOut: ["chance", 0.15], excluded: false, petPermitted: ["chance", 0.3], simulated: true },
          rels: { premises: ["any", "premises", ["and", "$it.attrs.simulated", ["=", "$it.attrs.occupied", 0]]],
                  tenant: ["any", "person", ["and", "$it.attrs.seeker", ["=", "$it.attrs.tenancies", 0]]] } } },
      { id: "increase", per: "agreement",
        when: ["and", "$self.attrs.commenced", ["not", "$self.attrs.ended"], ["not", "$self.attrs.superseded"], ["not", "$self.attrs.incomeBased"], ["not", "$self.attrs.incPending"],
               ["<=", ["if", ["exists", "$self.attrs.lastIncDay"], "$self.attrs.lastIncL12", "$self.attrs.startL12"], ["+", "$day", 75]]],
        chance: ["/", "$param.pIncrease", 3000],
        act: { action: "noticeIncrease", actor: ["rel", "$self", "lessor"], target: "$self",
               params: { rent: ["+", "$target.attrs.rentNow", ["*", 5, ["randInt", 2, 12]]],
                         inDays: ["if", ["chance", ["/", "$param.pCompliant", 100]], 0, ["randInt", 40, 100]],
                         form: ["if", ["<", "$day", 210], "minister", "s88c"],
                         motivated: ["and", ["exists", "$target.attrs.matterDay"], ["chance", 0.3]] } } },
      { id: "change", per: "agreement",
        when: ["and", "$self.attrs.commenced", ["not", "$self.attrs.ended"], ["not", "$self.attrs.superseded"], "$self.attrs.incomeBased", ["not", "$self.attrs.chgPending"],
               ["<=", ["if", ["exists", "$self.attrs.lastChgDay"], "$self.attrs.lastChgL12", "$self.attrs.startL12"], ["+", "$day", 75]]],
        chance: ["/", "$param.pIncrease", 3000],
        act: { action: "noticeChange", actor: ["rel", "$self", "lessor"], target: "$self",
               params: { rent: ["+", "$target.attrs.rentNow", ["randInt", 5, 25]], inDays: ["if", ["chance", ["/", "$param.pCompliant", 100]], 0, ["randInt", 40, 100]] } } },
      { id: "offer", per: "agreement",
        when: ["and", "$self.attrs.commenced", ["not", "$self.attrs.ended"], ["not", "$self.attrs.superseded"], ["=", "$self.attrs.kind", "fixed"],
               ["not", "$self.attrs.periodic76C"], ["not", "$self.attrs.offerOpen"], ["=", "$day", ["-", "$self.attrs.fixedLastDay", 40]]],
        chance: ["/", "$param.pRenew", 100],
        act: { action: "offerFurther", actor: ["rel", "$self", "lessor"], target: "$self",
               params: { rent: ["+", "$target.attrs.rentNow", ["*", 10, ["randInt", 2, 10]]], months: ["oneOf", 6, 12, 12],
                         kind: ["if", ["chance", ["/", "$param.pFixed", 100]], "fixed", "periodic"],
                         gapDays: ["if", ["chance", ["/", "$param.pGap", 100]], ["randInt", 1, 10], 0],
                         motivated: ["and", ["exists", "$target.attrs.matterDay"], ["chance", 0.3]] } } },
      /* a further agreement on an open offer is entered on the day it is to start (or, if two start
         the same day, the next), and its tenancy commences on that day */
      { id: "renew", rate: 1,
        when: ["exists", ["any", "agreement", ["and", "$it.attrs.offerOpen", ["not", "$it.attrs.offerTaken"], ["<=", "$it.attrs.offerStart", "$day"]]]],
        spawn: { type: "agreement", label: "Lease R{n}", attrs: { renewal: true, simulated: true } } },
      { id: "end-by-notice", per: "agreement",
        when: ["and", "$self.attrs.commenced", ["not", "$self.attrs.ended"], ["not", "$self.attrs.superseded"], ["=", "$self.attrs.kind", "fixed"],
               ["not", "$self.attrs.periodic76C"], ["not", ["exists", "$self.attrs.possDay70A"]], ["=", "$day", ["-", "$self.attrs.fixedLastDay", 35]]],
        chance: ["if", ["and", "$self.attrs.offerOpen", [">", "$self.attrs.offerGap", 0]], 1, ["if", "$self.attrs.offerOpen", 0, ["/", "$param.pEndNotice", 100]]],
        act: { action: "give70A", actor: ["oneOf", ["rel", "$self", "lessor"], ["rel", "$self", "tenant"]], target: "$self", params: { inDays: 0 } } },
      { id: "move-out", per: "agreement",
        when: ["and", "$self.attrs.commenced", ["not", "$self.attrs.ended"],
               ["or", ["and", "$self.attrs.n64Pending", [">=", "$day", "$self.attrs.n64Day"]], ["and", ["exists", "$self.attrs.possDay70A"], [">=", "$day", "$self.attrs.possDay70A"]]]],
        chance: 0.6,
        act: { action: "vacate", actor: ["rel", "$self", "tenant"], target: "$self" } },
      { id: "end-without-ground", per: "agreement",
        when: ["and", "$self.attrs.commenced", ["not", "$self.attrs.ended"], ["not", "$self.attrs.superseded"], ["not", "$self.attrs.n64Pending"],
               ["or", ["=", "$self.attrs.kind", "periodic"], "$self.attrs.periodic76C"]],
        chance: ["/", "$param.pS64", 3000],
        act: { action: "give64", actor: ["rel", "$self", "lessor"], target: "$self",
               params: { inDays: ["randInt", 56, 90], motivated: ["and", ["exists", "$target.attrs.matterDay"], ["chance", 0.3]] } } },
      { id: "leave-by-agreement", per: "agreement",
        when: ["and", "$self.attrs.commenced", ["not", "$self.attrs.ended"], ["not", "$self.attrs.superseded"], ["or", ["=", "$self.attrs.kind", "periodic"], "$self.attrs.periodic76C"]],
        chance: ["/", "$param.pLeave", 3000],
        act: { action: "vacate", actor: ["rel", "$self", "tenant"], target: "$self", params: { written: true } } },
      { id: "repairs", per: "agreement",
        when: ["and", "$self.attrs.commenced", ["not", "$self.attrs.ended"], ["not", "$self.attrs.superseded"], ["not", ["exists", "$self.attrs.matterDay"]]],
        chance: ["/", "$param.pRepair", 3000],
        act: { action: "askRepairs", actor: ["rel", "$self", "tenant"], target: "$self" } },
      { id: "excessive-rent", per: "agreement",
        when: ["and", "$self.attrs.commenced", ["not", "$self.attrs.ended"], ["not", "$self.attrs.s32Pending"], ["not", ["exists", "$self.attrs.orderMade"]],
               ["exists", "$self.attrs.noticeReceivedDay"], ["<=", "$day", ["+", "$self.attrs.noticeReceivedDay", 30]]],
        chance: 0.004,
        act: { action: "apply32", actor: ["rel", "$self", "tenant"], target: "$self" } },
      { id: "court-s32", per: "agreement", when: "$self.attrs.s32Pending", chance: 0.05,
        act: { action: "order32", actor: ["any", "court"], target: "$self",
               params: { max: ["-", "$target.attrs.rentNow", ["*", 10, ["randInt", 2, 6]]], months: ["oneOf", 3, 6], refuse: ["chance", 0.4] } } },
      { id: "rent-demanded", per: "agreement",
        when: ["and", ["exists", "$self.attrs.orderMade"], ["not", "$self.attrs.orderLapsed"], ["not", "$self.attrs.ended"]], chance: 0.02,
        act: { action: "demandRent", actor: ["rel", "$self", "lessor"], target: "$self",
               params: { amount: ["if", ["chance", 0.3], "$target.attrs.rentNow", "$target.attrs.orderMax"] } } },
      { id: "retaliation-claims", per: "agreement",
        when: ["and", ["exists", "$self.attrs.listedKind"], ["not", "$self.attrs.s26bApplied"], ["not", "$self.attrs.s26bDecided"], ["not", "$self.attrs.ended"]], chance: 0.05,
        act: { action: "apply26B", actor: ["rel", "$self", "tenant"], target: "$self" } },
      { id: "court-s26b", per: "agreement", when: "$self.attrs.s26bApplied", chance: 0.05,
        act: { action: "decide26B", actor: ["any", "court"], target: "$self", params: { satisfied: "$target.attrs.listedMotivated" } } },
      { id: "sales", per: "premises", chance: ["/", "$param.pSale", 36500],
        act: { action: "buyPremises", actor: ["any", "person", ["and", "$it.attrs.isOwner", ["!=", "$it.id", "$self.attrs.ownerId"]]], target: "$self" } },
      { id: "cotenants", per: "agreement",
        when: ["and", "$self.attrs.commenced", ["not", "$self.attrs.ended"], ["not", "$self.attrs.superseded"], ["not", ["exists", "$self.rels.cotenant"]]], chance: 0.0006,
        act: { action: "joinAsCotenant", actor: ["any", "person", ["and", "$it.attrs.seeker", ["=", "$it.attrs.tenancies", 0]]], target: "$self" } },
      { id: "cotenant-leaves", per: "agreement",
        when: ["and", "$self.attrs.commenced", ["not", "$self.attrs.ended"], ["exists", "$self.rels.cotenant"]], chance: 0.001,
        act: { action: "leaveAgreement", actor: ["rel", "$self", "cotenant"], target: "$self" } }
    ]
  };

  var RTA_LQA = {
    id: "residential-tenancies-act-lqa",
    title: "Residential Tenancies Act 1987 (LQA run)",
    jurisdiction: "Western Australia",
    status: "Consolidated version 07-a0-00 (currency start 29 Apr 2026), with the Residential Tenancies Regulations 1989 05-ad0-00 · encoded at 4A and 5A, 4-5 Oct 2026 · fidelity certified at 6H, 5 Oct 2026 · candidate findings recorded at 7A-8A, 5 Oct 2026, not yet challenged (9A)",
    scope: "How rent is set and varied under a residential tenancy agreement, and how one tenancy ends and the next begins: ss 30, 31A, 31B and 31 (the bond so far as it follows the rent, with s 29(1)(b)); s 32 (excessive rent) and s 65; ss 60, 64, 70A and 76C; ss 26A and 26B (retaliatory action); s 82(2); s 85 so far as it fixes the day a notice is given; and ss 99 and 100 for agreements in force on 29 July 2024. Day 0 is 1 January 2024. Coarser than the L4 in the ways listed in ENCODING-NOTES.md ('Console scheme'): weekends are the only excluded days, one pending notice of each kind, no regulation status facts, the present s 31A throughout, no s 70A notice after a fixed term has ended, two tenant places, and a tenancy commences on the day its agreement is entered.",
    startDate: "2024-01-01",
    dayLabel: "Day",

    types: [
      { id: "court", label: "Competent court", band: 0, shape: "rect" },
      { id: "person", label: "Person", band: 1, shape: "rect",
        create: { nameHint: "Sam", fields: [
          { key: "isOwner", type: "bool", origin: "exogenous", cite: "s 3 'lessor'",
            label: "Owns residential premises and lets them",
            note: "Ownership is settled by property law, not by this Act. The simulation chooses lessors and buyers from these people." }
        ], rels: [] } },
      { id: "premises", label: "Residential premises", band: 2, shape: "rect",
        create: { nameHint: "3 Example St", bornVerb: "Built", fields: [], rels: [
          { key: "owner", label: "Held by (the owner, who lets them)", target: "person", origin: "exogenous", cite: "s 3 'lessor'",
            note: "Settled by property law. A sale moves it: 'Buy the premises'." }
        ] } },
      { id: "agreement", label: "Residential tenancy agreement", band: 2, shape: "round",
        create: { nameHint: "A1", bornVerb: "Entered into", fields: [
          { key: "kind", type: "choice", origin: "innate", def: "fixed", cite: "s 3 'tenancy period'; s 70A(1)", label: "Kind of tenancy",
            options: [ { v: "fixed", label: "for a fixed term" }, { v: "periodic", label: "a periodic tenancy" } ] },
          { key: "termMonths", type: "number", origin: "innate", def: 12, min: 1, max: 60, cite: "s 3 'expiry day'; IA ss 61(1)(a), 62",
            label: "Fixed term, in months (not read for a periodic tenancy)",
            note: "The expiry day is the last day of that many calendar months beginning on the day the tenancy commences." },
          { key: "rent", type: "number", origin: "innate", def: 500, min: 1, cite: "s 3 'rent'; s 27AA; FK-01", label: "Weekly rent the agreement fixes" },
          { key: "incomeBased", type: "bool", origin: "innate", cite: "ss 30(1), 31A(1)", label: "The rent is calculated by reference to the tenant's income" },
          { key: "setOut", type: "bool", origin: "innate", cite: "s 30(2)(a)", label: "The agreement sets out the amount of an increase, or how to calculate it" },
          { key: "excluded", type: "bool", origin: "innate", cite: "s 30(2)(b)", label: "The agreement excludes rent increases" },
          { key: "bond", type: "number", origin: "innate", def: 2000, min: 0, cite: "s 29(1)(b), (2); r 11", label: "Security bond required, in dollars" },
          { key: "petPermitted", type: "bool", origin: "innate", cite: "s 29(1)(b)(ii); r 10A", label: "The tenant is permitted to keep a pet" },
          { key: "motivatedByMatter", type: "bool", origin: "exogenous", cite: "s 26A(b); FK-11",
            label: "The lessor fixed this rent higher because of a matter in s 26B(2) (a repair request, a complaint, a court order)",
            note: "The lessor's motive is a fact (REF-20)." },
          { key: "intentToEvade", type: "bool", origin: "exogenous", cite: "s 82(2)",
            label: "Entered into with intent to defeat, evade or prevent the operation of the Act", note: "Intent is a fact." },
          { key: "ended", type: "bool", origin: "conferred", by: "vacate", cite: "s 60(1)", label: "Has terminated" }
        ], rels: [
          { key: "lessor", label: "Lessor", target: "person", required: true, origin: "innate", cite: "s 3 'lessor', 'party' (a)" },
          { key: "tenant", label: "Tenant", target: "person", required: true, origin: "innate", cite: "s 3 'tenant', 'party' (a)" },
          { key: "cotenant", label: "Co-tenant", target: "person", origin: "innate", cite: "s 3 'party' (a); s 31B(3)(b)" },
          { key: "premises", label: "For the premises", target: "premises", required: true, origin: "innate", cite: "s 3A" }
        ] } }
    ],

    relLabels: { lessor: "lessor", tenant: "tenant", cotenant: "co-tenant", premises: "for", owner: "held by",
                 continues: "continues (s 31B)", follows: "follows", reletAfter: "let again after" },

    entities: [
      { id: "ct", type: "court", label: "Magistrates Court", note: "a competent court (s 3; REF-02)" },
      { id: "l1", type: "person", label: "Lena", note: "owns 1 and 2 Example St", attrs: { name: "Lena", isOwner: true, tenancies: 0 } },
      { id: "t1", type: "person", label: "Tom", attrs: { name: "Tom", isOwner: false, tenancies: 0 } },
      { id: "t2", type: "person", label: "Tia", attrs: { name: "Tia", isOwner: false, tenancies: 0 } },
      { id: "t3", type: "person", label: "Theo", attrs: { name: "Theo", isOwner: false, tenancies: 0 } },
      { id: "pb", type: "person", label: "Pat", note: "buys houses to let", attrs: { name: "Pat", isOwner: true, tenancies: 0 } },
      { id: "pr1", type: "premises", label: "1 Example St", attrs: { name: "1 Example St", ownerId: "l1", occupied: 0 }, rels: { owner: "l1" } },
      { id: "pr2", type: "premises", label: "2 Example St", attrs: { name: "2 Example St", ownerId: "l1", occupied: 0 }, rels: { owner: "l1" } }
    ],

    defs: {
      orderInForce: ["and", ["exists", T("orderMade")], ["not", T("orderLapsed")], ["<=", "$day", T("orderEnd")], ["not", T("ended")]],
      s65Bites: ["or", T("s32Pending"), ["def", "orderInForce"]],
      inFixedTerm: ["and", ["=", T("kind"), "fixed"], ["not", T("periodic76C")], [">=", "$day", T("startDay")], ["<=", "$day", T("fixedLastDay")]]
    },

    actions: [
      /* the lessor */
      { id: "noticeIncrease", actor: "person", target: "agreement", label: "Give the tenant notice of a rent increase", cite: "s 30(1)",
        log: "<b>{self}</b> gives notice of a rent increase under <b>{target}</b>.",
        params: [
          { key: "rent", type: "number", label: "The increased weekly rent (empty: $50 more)" },
          { key: "inDays", type: "number", label: "Days from today to the day it becomes payable (empty: the earliest day s 30(1) allows)" },
          { key: "how", type: "choice", label: "How it is given", options: [
            { v: "personally", label: "handed to the tenant (s 85(1)(a))" },
            { v: "post", label: "posted (s 85(1)(b))" },
            { v: "email", label: "emailed, the tenant having consented (s 85(1)(c))" } ] },
          { key: "postDays", type: "number", label: "If posted: days until it would be delivered in the ordinary course of post (s 85(2))" },
          { key: "form", type: "choice", label: "Form", options: [
            { v: "s88c", label: "the approved form (Form 10, approved under s 88C)" },
            { v: "minister", label: "the form the Minister approved before 29 July 2024" },
            { v: "none", label: "no approved form" } ] },
          { key: "motivated", label: "motivated by a matter in s 26B(2) (s 26A(b))" } ] },
      { id: "withdrawIncrease", actor: "person", target: "agreement", label: "Withdraw the notice of increase", cite: "s 30(3)",
        log: "<b>{self}</b> withdraws the notice of increase under <b>{target}</b>." },
      { id: "noticeChange", actor: "person", target: "agreement", label: "Give notice of a change to how income-based rent is calculated", cite: "s 31A(2)",
        log: "<b>{self}</b> gives notice of a change to the method of calculating the rent under <b>{target}</b>.",
        params: [
          { key: "rent", type: "number", label: "The weekly rent the changed method gives (empty: $20 more)" },
          { key: "inDays", type: "number", label: "Days from today to the day the change takes effect (empty: the earliest day s 31A allows)" },
          { key: "email", label: "sent by email, the tenant having consented (s 85(1)(c))" } ] },
      { id: "increaseBond", actor: "person", target: "agreement", label: "Give notice of an increase in the security bond", cite: "s 31(1A), (1B), (2)",
        log: "<b>{self}</b> gives notice increasing the security bond under <b>{target}</b>.",
        params: [
          { key: "amount", type: "number", label: "The additional amount, in dollars (empty: up to 4 weeks' rent)" },
          { key: "inDays", type: "number", label: "Days from today to the day it is payable (empty: the earliest allowed)" } ] },
      { id: "give64", actor: "person", target: "agreement", label: "Give notice of termination without a ground", cite: "s 64",
        log: "<b>{self}</b> gives notice of termination of <b>{target}</b> without specifying a ground.",
        params: [
          { key: "inDays", type: "number", label: "Days from today to the day possession is to be given (empty: 61)" },
          { key: "email", label: "sent by email, the tenant having consented (s 85(1)(c))" },
          { key: "motivated", label: "motivated by a matter in s 26B(2) (s 26A(b))" } ] },
      { id: "give70A", actor: "person", target: "agreement", label: "Give notice ending the fixed term", cite: "s 70A",
        log: "<b>{self}</b> gives notice under s 70A for <b>{target}</b>.",
        params: [
          { key: "inDays", type: "number", label: "Days from today to the possession day (empty: the expiry day)" },
          { key: "email", label: "sent by email, the other party having consented (s 85(1)(c))" },
          { key: "motivated", label: "(lessor) motivated by a matter in s 26B(2) (s 26A(b))" } ] },
      { id: "offerFurther", actor: "person", target: "agreement", label: "Offer the tenant a further agreement", cite: "s 26A(a)(ii), (iv); FK-11",
        log: "<b>{self}</b> offers the tenant under <b>{target}</b> a further agreement.",
        params: [
          { key: "rent", type: "number", label: "Weekly rent of the further agreement (empty: the present rent)" },
          { key: "months", type: "number", label: "Its fixed term, in months (empty: 12)" },
          { key: "kind", type: "choice", label: "Kind", options: [ { v: "fixed", label: "for a fixed term" }, { v: "periodic", label: "a periodic tenancy" } ] },
          { key: "gapDays", type: "number", label: "Days between the end of this term and the start of the next (empty: none)" },
          { key: "motivated", label: "the higher rent is motivated by a matter in s 26B(2)" } ] },
      { id: "refuseFurther", actor: "person", target: "agreement", label: "Refuse to enter into a further agreement", cite: "s 26A(a)(iv)",
        log: "<b>{self}</b> refuses to enter into a further agreement with the tenant under <b>{target}</b>.",
        params: [ { key: "motivated", label: "motivated by a matter in s 26B(2) (s 26A(b))" } ] },
      { id: "demandRent", actor: "person", target: "agreement", label: "Demand rent", cite: "s 32(7)",
        log: "<b>{self}</b> demands rent under <b>{target}</b>.",
        params: [ { key: "amount", type: "number", label: "Weekly rent demanded (empty: the rent under the agreement)" } ] },
      { id: "buyPremises", actor: "person", target: "premises", label: "Buy the premises", cite: "s 3 'lessor'; FK-13",
        log: "<b>{self}</b> buys <b>{target}</b>." },
      /* the tenant */
      { id: "askRepairs", actor: "person", target: "agreement", label: "Ask the lessor for repairs", cite: "s 26B(2)(a)(i)",
        log: "<b>{self}</b> asks the lessor for repairs to the premises under <b>{target}</b>." },
      { id: "vacate", actor: "person", target: "agreement", label: "Deliver up vacant possession", cite: "s 60(1)",
        log: "<b>{self}</b> moves out and delivers up vacant possession under <b>{target}</b>.",
        params: [
          { key: "written", label: "under a written agreement with the lessor to end the agreement (s 60(1)(g))" },
          { key: "abandon", label: "abandoning the premises (s 60(1)(f))" } ] },
      { id: "agreeToEnd", actor: "person", target: "agreement", label: "Agree with the other party to end the agreement, the tenant staying on", cite: "s 60(1)",
        log: "<b>{self}</b> agrees with the other party to end <b>{target}</b>; the tenant stays in the premises." },
      { id: "apply32", actor: "person", target: "agreement", label: "Apply to the court: the rent is excessive", cite: "s 32(1), (2)",
        log: "<b>{self}</b> applies to the court for an order that the rent under <b>{target}</b> is excessive.",
        params: [ { key: "reduction", label: "there has been a significant reduction in the chattels or facilities, through no default of the tenant (s 32(2)(b))" } ] },
      { id: "apply26B", actor: "person", target: "agreement", label: "Apply to the court: the lessor's action was retaliatory", cite: "s 26B(3)",
        log: "<b>{self}</b> applies to the court for relief against retaliatory action under <b>{target}</b>." },
      { id: "apply64", actor: "person", target: "agreement", label: "Apply to the court for a longer period of notice", cite: "s 64(3)",
        log: "<b>{self}</b> applies to the court about the notice of termination under <b>{target}</b>." },
      { id: "joinAsCotenant", actor: "person", target: "agreement", label: "Join the agreement as a co-tenant", cite: "s 3 'party' (a)",
        log: "<b>{self}</b> joins <b>{target}</b> as a co-tenant." },
      { id: "leaveAgreement", actor: "person", target: "agreement", label: "Leave the agreement, the other tenant staying", cite: "s 60(2)",
        log: "<b>{self}</b>'s interest in <b>{target}</b> ends; the other tenant stays." },
      /* the agreement itself */
      { id: "incomeRises", actor: "agreement", label: "The tenant's income rises", cite: "s 31A(1); FK-20",
        log: "The tenant's income under <b>{self}</b> rises.",
        params: [ { key: "rent", type: "number", label: "The weekly rent the unchanged method now gives (empty: $20 more)" } ] },
      /* the court */
      { id: "order32", actor: "court", target: "agreement", label: "Decide the application under s 32", cite: "s 32(2)-(5)",
        log: "<b>{self}</b> decides the application under s 32 about <b>{target}</b>.",
        params: [
          { key: "max", type: "number", label: "The most the weekly rent may be (empty: $50 less than now)" },
          { key: "months", type: "number", label: "The period of the order, in months (empty: 6)" },
          { key: "refuse", label: "the rent is not excessive: no order" },
          { key: "allowLate", label: "allow a greater period for a late application (s 32(2))" } ] },
      { id: "decide26B", actor: "court", target: "agreement", label: "Decide the application under s 26B", cite: "s 26B(4)",
        log: "<b>{self}</b> decides the tenant's application under s 26B about <b>{target}</b>.",
        params: [ { key: "satisfied", label: "satisfied the lessor's action was likely to have been retaliatory action" } ] },
      { id: "decide64", actor: "court", target: "agreement", label: "Decide the application under s 64(3)", cite: "s 64(4)",
        log: "<b>{self}</b> decides the tenant's application under s 64(3) about <b>{target}</b>.",
        params: [
          { key: "extendDays", type: "number", label: "Extend the period of notice by this many days (s 64(4)(a))" },
          { key: "notTerminated", label: "order that the agreement is not terminated by the notice (s 64(4)(b))" },
          { key: "possessionInDays", type: "number", label: "Or order possession, operating this many days from today (s 64(4)(c))" } ] },
      { id: "authorise65", actor: "court", target: "agreement", label: "Decide the lessor's application to give notice", cite: "s 65(2)",
        log: "<b>{self}</b> decides whether to authorise the lessor to give notice of termination of <b>{target}</b>.",
        params: [ { key: "motivated", label: "the s 32 proceedings or order wholly or partly motivated the lessor" } ] }
    ],

    rules: RULES,
    observations: OBSERVATIONS,
    scenarios: SCENARIOS,
    simulation: SIMULATION
  };

  global.SCHEMES = (global.SCHEMES || []).concat([RTA_LQA]);
})(window);
