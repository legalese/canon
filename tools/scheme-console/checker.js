/* ===========================================================================
   The checker, for the browser. The same checks check.js runs from the command
   line, as one function the console can apply to a scheme it has just been
   given — in practice, a scheme Claude has just written from a Bill.

     var problems = checkScheme(scheme);   // [] when it holds together

   It checks that the scheme hangs together: every reference resolves, every
   conferred fact has an act that confers it, every observation can be
   recorded, and every scenario runs. It cannot check that the scheme reads
   the Bill correctly. Nothing here can.
   =========================================================================== */
(function (global) {
  "use strict";

  function arr(x) { return Array.isArray(x) ? x : []; }

  function playScenario(eng, sc, bad) {
    return eng.play(sc, function (e) { bad((sc.label || "a scenario") + ": " + e.message); })(sc.focus);
  }

  function checkScheme(s, opts) {
    opts = opts || {};
    var problems = [];
    function bad(m) { if (problems.indexOf(m) < 0) problems.push(m); }
    var Engine = global.Engine;

    ["types", "entities", "actions", "rules", "observations", "scenarios"].forEach(function (k) {
      if (s[k] !== undefined && !Array.isArray(s[k])) bad(k + " must be a list");
    });
    var typeIds = arr(s.types).map(function (t) { return t.id; });
    var actionIds = arr(s.actions).map(function (a) { return a.id; });
    var obsIds = arr(s.observations).map(function (o) { return o.id; });
    var ruleIds = arr(s.rules).map(function (r) { return r.id; });
    var entIds = arr(s.entities).map(function (e) { return e.id; });

    [["type", typeIds], ["action", actionIds], ["observation", obsIds], ["rule", ruleIds], ["actor", entIds]]
      .forEach(function (p) {
        var seen = {};
        p[1].forEach(function (id) {
          if (!id) bad("a " + p[0] + " has no id");
          else if (seen[id]) bad("two " + p[0] + "s share the id " + id);
          seen[id] = 1;
        });
      });

    arr(s.entities).forEach(function (e) {
      if (typeIds.indexOf(e.type) < 0) bad("actor " + e.id + " has unknown type " + e.type);
      Object.keys(e.rels || {}).forEach(function (k) {
        if (entIds.indexOf(e.rels[k]) < 0) bad("actor " + e.id + "." + k + " points at a missing actor " + e.rels[k]);
      });
    });

    /* provenance: a conferred fact must have an act that confers it */
    arr(s.types).forEach(function (t) {
      var cr = t.create || {};
      arr(cr.fields).concat(arr(cr.rels)).forEach(function (f) {
        if (f.origin !== "conferred") return;
        if (!f.by) { bad(t.id + "." + f.key + " is conferred by nothing named"); return; }
        if (actionIds.indexOf(f.by) < 0) { bad(t.id + "." + f.key + " names a missing act " + f.by); return; }
        var sets = arr(s.rules).some(function (r) {
          return r.on === "action:" + f.by && arr(r.then).some(function (e) {
            return e[0] === "set" && String(e[1]).indexOf("." + f.key) >= 0; });
        });
        if (!sets) bad("no rule on " + f.by + " ever sets " + f.key);
      });
      arr(cr.fields).forEach(function (f) {
        if (["birth", "innate", "conferred", "exogenous"].indexOf(f.origin || "innate") < 0) {
          bad(t.id + "." + f.key + " has an unknown origin " + f.origin);
        }
      });
      arr(cr.rels).forEach(function (r) {
        if (typeIds.indexOf(r.target) < 0) bad(t.id + "." + r.key + " targets a missing type " + r.target);
      });
    });

    var observedBy = {};
    arr(s.rules).forEach(function (r) {
      var on = String(r.on || "");
      if (!on) bad("rule " + r.id + " has no trigger");
      if (on.indexOf("action:") === 0 && actionIds.indexOf(on.slice(7)) < 0) bad("rule " + r.id + " is on a missing action " + on.slice(7));
      if (on.indexOf("create:") === 0 && typeIds.indexOf(on.slice(7)) < 0) bad("rule " + r.id + " is on a missing type");
      if (on.indexOf("death:") === 0 && typeIds.indexOf(on.slice(6)) < 0) bad("rule " + r.id + " is on a missing type");
      if (on === "day" && r["for"] && typeIds.indexOf(r["for"]) < 0) bad("day rule " + r.id + " binds a missing type");
      if (!Array.isArray(r.then)) bad("rule " + r.id + " has no list of effects");
      arr(r.then).forEach(function (e) {
        if (!Array.isArray(e)) { bad("rule " + r.id + " has an effect that is not a list"); return; }
        if (["set", "log", "observe", "after"].indexOf(e[0]) < 0) bad("rule " + r.id + " uses unknown effect " + e[0]);
        if (e[0] === "observe") {
          observedBy[e[1]] = true;
          if (obsIds.indexOf(e[1]) < 0) bad("rule " + r.id + " observes undeclared " + e[1]);
        }
        if (e[0] === "after" && ruleIds.indexOf(e[2]) < 0) bad("rule " + r.id + " schedules a missing rule " + e[2]);
      });
    });
    /* a static observation is a finding no run can show (Style, Form): it is listed, never recorded */
    arr(s.observations).forEach(function (o) { if (o.static) observedBy[o.id] = true; });
    obsIds.forEach(function (id) {
      if (!observedBy[id]) bad("observation " + id + " is declared but no rule records it");
    });
    arr(s.actions).forEach(function (a) {
      if (typeIds.indexOf(a.actor) < 0) bad("action " + a.id + " has unknown actor type " + a.actor);
      if (a.target && typeIds.indexOf(a.target) < 0) bad("action " + a.id + " has unknown target type " + a.target);
    });

    /* the simulation section: required when opts.requireSimulation is set */
    var sim = s.simulation;
    if (!sim) { if (opts.requireSimulation) bad("there is no simulation section: parameters with defaults, and generators that use them"); }
    else {
      var pkeys = arr(sim.params).map(function (q) { return q.key; });
      if (!pkeys.length) bad("the simulation section has no parameters");
      if (!arr(sim.generators).length) bad("the simulation section has no generators");
      arr(sim.params).forEach(function (q) {
        if (typeof q.def !== "number" || isNaN(q.def)) bad("simulation parameter " + q.key + " has no numeric default");
      });
      var gseen = {};
      arr(sim.generators).forEach(function (g) {
        var name = "generator " + (g.id || "(no id)");
        if (!g.id) bad("a generator has no id"); else if (gseen[g.id]) bad("two generators share the id " + g.id);
        gseen[g.id] = 1;
        if (g.start === undefined && g.rate === undefined && !g.per) bad(name + " has no start, rate or per");
        if (g.per && typeIds.indexOf(g.per) < 0) bad(name + " runs per a missing type " + g.per);
        if (!g.spawn && !g.act && !g.remove) bad(name + " neither spawns, acts nor removes");
        if (g.spawn && typeIds.indexOf(g.spawn.type) < 0) bad(name + " spawns a missing type " + g.spawn.type);
        if (g.act && actionIds.indexOf(g.act.action) < 0) bad(name + " performs a missing action " + g.act.action);
        (JSON.stringify(g).match(/\$param\.[A-Za-z0-9_]+/g) || []).forEach(function (m) {
          if (pkeys.indexOf(m.slice(7)) < 0) bad(name + " reads a parameter that is not declared: " + m.slice(7));
        });
      });
    }

    if (!Engine) return problems;
    var probe;
    try { probe = new Engine(s); } catch (e) { bad("the engine cannot load it: " + e.message); return problems; }

    /* every scenario runs, and its focus exists */
    arr(s.scenarios).forEach(function (sc) {
      if (!Array.isArray(sc.steps) || !sc.steps.length) { bad((sc.label || "a scenario") + " has no steps"); return; }
      var eng = new Engine(s);
      var focus = playScenario(eng, sc, bad);
      if (sc.focus && !eng.get(focus)) bad(sc.label + ": focus resolves to nothing");
      eng.log.forEach(function (l) {
        if (/could not be applied|Could not apply/.test(l.text)) bad(sc.label + ": " + l.text.replace(/<[^>]+>/g, ""));
      });
    });

    /* every creatable type can be brought into existence */
    probe.creatableTypes().forEach(function (t) {
      try {
        var fi = probe.settableAtBirth(t.id, false), ri = probe.settableRels(t.id, false), attrs = {}, rels = {};
        fi.fields.forEach(function (f) {
          attrs[f.key] = f.def !== undefined ? f.def : (f.type === "bool" ? false : (f.type === "number" ? 0 : "x"));
        });
        if (fi.birth) attrs.bornDay = probe.dayForYearsAgo(1);
        ri.rels.forEach(function (r) {
          var c = probe.ofType(r.target)[0];
          if (r.required && !c) bad(t.id + " needs a " + r.target + " and none exists in the cast");
          if (c) rels[r.key] = c.id;
        });
        probe.spawn(t.id, "Test " + t.id, attrs, rels);
      } catch (e) { bad("creating a " + t.id + " fails: " + e.message); }
    });

    /* a trial run: ninety generated days at the defaults, from the starting cast */
    if (sim && arr(sim.generators).length) {
      try {
        var run = new Engine(s), param = {}, d;
        arr(sim.params).forEach(function (q) { param[q.key] = q.def; });
        run.seed(1);
        run.startRun(sim, param);
        for (d = 0; d < 90; d++) { run.tick(); run.generate(sim); }
        run.log.filter(function (l) { return /Generator .* failed|could not be applied/.test(l.text); })
          .slice(0, 4).forEach(function (l) { bad("simulation: " + l.text.replace(/<[^>]+>/g, "")); });
        if (run.order.length > 3000) bad("simulation: the population grows past 3,000 in ninety days; add a ceiling");
        var acted = run.log.filter(function (l) { return l.sev === "act" && /^action:/.test(l.rule || ""); }).length;
        if (!acted && run.order.length === probe.order.length) bad("simulation: ninety days at the defaults and nothing happens");
      } catch (e) { bad("simulation: the trial run fails: " + e.message); }
    }

    return problems;
  }

  global.checkScheme = checkScheme;
})(window);
