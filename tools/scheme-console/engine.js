/* ===========================================================================
   Scheme engine.

   Nothing in this file names a statute, a court, a dog or a shop. Every
   statute-specific thing — the actors, what they can do to each other, the
   consequences, the clocks and the things worth counting — arrives as a
   scheme definition. See schemes.js for three of them.

   The engine is: a fact base of entities, a tiny expression language, a
   forward-chaining rule pass, a calendar, and — for generated runs — a
   seeded dice and a list of things that happen of their own accord.
   =========================================================================== */
(function (global) {
  "use strict";

  function clone(x) { return JSON.parse(JSON.stringify(x)); }

  /* the actors a log line is about: whoever acted, and whoever it was done to */
  function whoOf(env) {
    var w = [];
    if (env && env.self && env.self.id) w.push(env.self.id);
    if (env && env.target && env.target.id && w.indexOf(env.target.id) < 0) w.push(env.target.id);
    return w;
  }

  function Engine(scheme) {
    this.scheme = scheme;
    this.reset();
  }

  Engine.prototype.reset = function () {
    var sc = this.scheme, self = this;
    this.day = 0;
    this.log = [];
    this.counts = {};
    this.observed = [];
    this.context = "god";
    this.pending = [];
    this.recorder = null;
    this.param = {};
    this.genCount = {};
    this.entities = {};
    this.order = [];
    var d = (sc.startDate || "2026-01-01").split("-");
    this.start = Date.UTC(+d[0], +d[1] - 1, +d[2]);
    (sc.observations || []).forEach(function (o) { self.counts[o.id] = 0; });
    (sc.entities || []).forEach(function (e) {
      var ent = {
        id: e.id, type: e.type, label: e.label, note: e.note || "",
        attrs: clone(e.attrs || {}),
        rels: clone(e.rels || {})
      };
      /* a date of birth in the scheme becomes a day number the rules can read */
      if (ent.attrs.bornDate) ent.attrs.bornDay = self.dayForDate(ent.attrs.bornDate);
      self.entities[ent.id] = ent;
      self.order.push(ent.id);
    });
  };

  /* --------------------------------- calendar ---------------------------------
     Age is never stored. It is worked out from a date of birth and the clock,
     against a real calendar, because "three months" and "18 years" are calendar
     facts and thirty-day months get them wrong.                                */

  Engine.prototype.dateOf = function (day) {
    return new Date(this.start + (day === undefined ? this.day : day) * 86400000);
  };
  Engine.prototype.dayForDate = function (iso) {
    var d = String(iso).split("-");
    return Math.round((Date.UTC(+d[0], +d[1] - 1, +d[2]) - this.start) / 86400000);
  };
  Engine.prototype.dayForMonthsAgo = function (months) {
    var now = this.dateOf(this.day);
    var b = new Date(Date.UTC(now.getUTCFullYear(), now.getUTCMonth() - months, now.getUTCDate()));
    return Math.round((b.getTime() - this.start) / 86400000);
  };
  Engine.prototype.dayForYearsAgo = function (years) {
    return this.dayForMonthsAgo(years * 12);
  };
  function monthsBetween(a, b) {
    var m = (b.getUTCFullYear() - a.getUTCFullYear()) * 12 + (b.getUTCMonth() - a.getUTCMonth());
    if (b.getUTCDate() < a.getUTCDate()) m--;
    return m;
  }
  Engine.prototype.monthsSince = function (bornDay) {
    if (bornDay === undefined || bornDay === null) return null;
    return monthsBetween(this.dateOf(bornDay), this.dateOf(this.day));
  };
  Engine.prototype.formatDate = function (day) {
    var MO = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];
    var d = this.dateOf(day);
    return d.getUTCDate() + " " + MO[d.getUTCMonth()] + " " + d.getUTCFullYear();
  };

  /* The console labels what it is doing; the engine only records the label,
     so a finding can say which way of working produced it. */
  Engine.prototype.setContext = function (label) { this.context = label; };

  Engine.prototype.get = function (id) { return this.entities[id]; };

  Engine.prototype.ofType = function (t) {
    var self = this;
    return this.order.map(function (i) { return self.entities[i]; })
      .filter(function (e) { return e.type === t; });
  };

  Engine.prototype.typeDef = function (t) {
    return (this.scheme.types || []).filter(function (x) { return x.id === t; })[0] ||
      { id: t, label: t, band: 1 };
  };

  /* ----------------------------- expressions -----------------------------
     An expression is a literal, a "$path" reference into the environment,
     or [operator, ...arguments]. That is the entire language.             */

  function resolve(ref, env) {
    var parts = ref.slice(1).split("."), cur = env[parts[0]], i;
    for (i = 1; i < parts.length; i++) {
      if (cur === null || cur === undefined) return undefined;
      cur = cur[parts[i]];
    }
    return cur;
  }

  Engine.prototype.evaluate = function (x, env) {
    var self = this, i, v;
    if (x === null || x === undefined) return x;
    if (typeof x === "string") return x.charAt(0) === "$" ? resolve(x, env) : x;
    if (typeof x === "number" || typeof x === "boolean") return x;
    if (!Array.isArray(x)) return x;

    var op = x[0], a = x.slice(1);
    function ev(y) { return self.evaluate(y, env); }

    switch (op) {
      case "and": for (i = 0; i < a.length; i++) { if (!ev(a[i])) return false; } return true;
      case "or":  for (i = 0; i < a.length; i++) { if (ev(a[i])) return true; } return false;
      case "not": return !ev(a[0]);
      case "=":   return ev(a[0]) === ev(a[1]);
      case "!=":  return ev(a[0]) !== ev(a[1]);
      case ">":   return ev(a[0]) > ev(a[1]);
      case ">=":  return ev(a[0]) >= ev(a[1]);
      case "<":   return ev(a[0]) < ev(a[1]);
      case "<=":  return ev(a[0]) <= ev(a[1]);
      case "+":   return a.reduce(function (s, y) { return s + (ev(y) || 0); }, 0);
      case "-":   return ev(a[0]) - ev(a[1]);
      case "*":   return a.reduce(function (s, y) { return s * ev(y); }, 1);
      case "/":   return ev(a[0]) / ev(a[1]);
      case "floor": return Math.floor(ev(a[0]));
      case "if":  return ev(a[0]) ? ev(a[1]) : ev(a[2]);
      case "rel":
        /* ["rel", "$self", "parent"] -> the entity that relation points at */
        v = ev(a[0]);
        return (v && v.rels) ? this.get(v.rels[a[1]]) : undefined;
      case "attrOf":
        /* ["attrOf", ["rel","$self","parent"], "restrictedBreed"] */
        v = ev(a[0]);
        return (v && v.attrs) ? v.attrs[a[1]] : undefined;
      case "ageMonths":
        return this.monthsSince(ev(a[0]));
      case "ageYears":
        v = this.monthsSince(ev(a[0]));
        return v === null ? null : Math.floor(v / 12);
      case "date":
        return this.formatDate(ev(a[0]));
      case "nextDate":
        /* ["nextDate", 10, 31] -> the day number of the next 31 October on or
           after today. Statutes fix periods by the calendar ("until the next
           31 October"), which a day counter cannot say on its own. */
        v = this.dateOf(this.day);
        i = Date.UTC(v.getUTCFullYear(), ev(a[0]) - 1, ev(a[1]));
        if (i < v.getTime()) i = Date.UTC(v.getUTCFullYear() + 1, ev(a[0]) - 1, ev(a[1]));
        /* an optional third argument counts that many years further on:
           ["nextDate", 10, 31, 2] is 31 October in the final year of a 3-year period */
        if (a[2] !== undefined) {
          v = new Date(i);
          i = Date.UTC(v.getUTCFullYear() + Math.floor(Number(ev(a[2])) || 0), ev(a[0]) - 1, ev(a[1]));
        }
        return Math.round((i - this.start) / 86400000);
      case "exists":
        v = ev(a[0]);
        return v !== undefined && v !== null && v !== false;
      case "daysSince":
        v = ev(a[0]);
        return (v === undefined || v === null) ? null : this.day - v;
      case "chance":
        /* ["chance", 0.3] -> true three times in ten, from the run's seeded dice */
        return this.random() < Number(ev(a[0]));
      case "randInt":
        v = Math.floor(Number(ev(a[0])));
        return v + Math.floor(this.random() * (Math.floor(Number(ev(a[1]))) - v + 1));
      case "oneOf":
        return ev(a[Math.floor(this.random() * a.length)]);
      case "any":
      case "count":
        /* ["any", "person", where] -> a random actor of that type for which `where`
           holds with the candidate as $it; ["count", ...] -> how many there are */
        v = this.ofType(a[0]).filter(function (e) {
          if (a[1] === undefined) return true;
          var e2 = {}, k;
          for (k in env) if (env.hasOwnProperty(k)) e2[k] = env[k];
          e2.it = e;
          return !!self.evaluate(a[1], e2);
        });
        if (op === "count") return v.length;
        return v.length ? v[Math.floor(this.random() * v.length)] : null;
      case "def":
        if (!this.scheme.defs || this.scheme.defs[a[0]] === undefined) {
          throw new Error("no such definition: " + a[0]);
        }
        return this.evaluate(this.scheme.defs[a[0]], env);
      default:
        throw new Error("unknown operator: " + op);
    }
  };

  /* ------------------------------ templates ------------------------------ */

  Engine.prototype.fill = function (tpl, env) {
    var self = this;
    return String(tpl).replace(/\{([^{}]+)\}/g, function (whole, ref) {
      var v;
      try { v = self.evaluate(ref.charAt(0) === "$" ? ref : "$" + ref, env); }
      catch (e) { return whole; }
      if (v === undefined || v === null) return "—";
      if (typeof v === "object" && v.label) return v.label;
      if (typeof v === "number") return v.toLocaleString("en-AU");
      if (typeof v === "boolean") return v ? "yes" : "no";
      return String(v);
    });
  };

  /* ------------------------------- effects ------------------------------- */

  function writePath(ref, value, env) {
    var parts = ref.slice(1).split("."), cur = env[parts[0]], i;
    if (!cur) return;
    for (i = 1; i < parts.length - 1; i++) {
      if (cur[parts[i]] === undefined || cur[parts[i]] === null) cur[parts[i]] = {};
      cur = cur[parts[i]];
    }
    /* setting a fact to null removes it: a lapsed registration leaves no
       relationship behind, rather than one that points at nothing */
    if (value === null || value === undefined) delete cur[parts[parts.length - 1]];
    else cur[parts[parts.length - 1]] = value;
  }

  Engine.prototype.applyEffect = function (eff, env, ruleId) {
    var op = eff[0], a = eff.slice(1);
    switch (op) {
      case "set":
        writePath(a[0], this.evaluate(a[1], env), env);
        break;
      case "log":
        this.log.push({
          day: this.day,
          text: this.fill(a[0], env),
          cite: (a[1] && a[1].cite) || "",
          sev: (a[1] && a[1].sev) || "",
          rule: ruleId || "",
          who: whoOf(env)
        });
        break;
      case "observe":
        this.counts[a[0]] = (this.counts[a[0]] || 0) + 1;
        this.observed.push({ id: a[0], day: this.day, context: this.context });
        break;
      case "after":
        this.pending.push({
          day: this.day + this.evaluate(a[0], env),
          rule: a[1],
          selfId: env.self ? env.self.id : null,
          targetId: env.target ? env.target.id : null,
          p: env.p
        });
        break;
      default:
        throw new Error("unknown effect: " + op);
    }
  };

  /* ---------------------------- rule firing ------------------------------ */

  Engine.prototype.fireRule = function (rule, env) {
    var self = this;
    try {
      if (rule["if"] !== undefined && !this.evaluate(rule["if"], env)) return false;
    } catch (e) { return false; }
    (rule.then || []).forEach(function (eff) {
      try { self.applyEffect(eff, env, rule.id); }
      catch (e) {
        self.log.push({ day: self.day, sev: "stop", cite: rule.cite || "",
          text: "Rule <b>" + rule.id + "</b> could not be applied: " + e.message, rule: rule.id, who: whoOf(env) });
      }
    });
    return true;
  };

  Engine.prototype.rulesOn = function (trigger) {
    return (this.scheme.rules || []).filter(function (r) { return r.on === trigger; });
  };

  /* An action is what a click on the canvas performs. */
  Engine.prototype.act = function (actorId, actionId, targetId, params) {
    var action = (this.scheme.actions || []).filter(function (x) { return x.id === actionId; })[0];
    if (!action) throw new Error("no such action: " + actionId);
    var self = this;
    var env = {
      self: this.get(actorId),
      target: targetId ? this.get(targetId) : null,
      p: params || {},
      day: this.day
    };
    this.record({ actor: this.recRef(actorId), action: actionId,
                  target: targetId ? this.recRef(targetId) : undefined, params: clone(params || {}) });
    var before = this.log.length;
    if (action.log) {
      this.log.push({ day: this.day, text: this.fill(action.log, env),
        cite: action.cite || "", sev: "act", rule: "action:" + actionId, who: whoOf(env) });
    }
    this.rulesOn("action:" + actionId).forEach(function (r) { self.fireRule(r, env); });
    return this.log.slice(before);
  };

  /* One day: scheduled rules that have come due, then every day-rule. */
  Engine.prototype.tick = function () {
    if (this.recorder) {
      var last = this.recorder.steps[this.recorder.steps.length - 1];
      if (last && last.tick) last.tick++; else this.recorder.steps.push({ tick: 1 });
    }
    this.day++;
    var self = this, due = [], keep = [];
    this.pending.forEach(function (p) { (p.day <= self.day ? due : keep).push(p); });
    this.pending = keep;

    due.forEach(function (p) {
      var rule = (self.scheme.rules || []).filter(function (r) { return r.id === p.rule; })[0];
      if (!rule) return;
      self.fireRule(rule, {
        self: p.selfId ? self.get(p.selfId) : null,
        target: p.targetId ? self.get(p.targetId) : null,
        p: p.p || {}, day: self.day
      });
    });

    this.rulesOn("day").forEach(function (rule) {
      var subjects = rule["for"] ? self.ofType(rule["for"]) : [null];
      subjects.forEach(function (s) {
        self.fireRule(rule, { self: s, target: null, p: {}, day: self.day });
      });
    });
  };

  /* ------------------------ creating and removing ------------------------
     A scheme says which types can be brought into existence and what has to
     be settled when one is. The engine does not care what they are.        */

  Engine.prototype.creatableTypes = function () {
    return (this.scheme.types || []).filter(function (t) { return !!t.create; });
  };

  Engine.prototype.spawn = function (typeId, label, attrs, rels, note) {
    var td = this.typeDef(typeId), n = 1, id, self = this, given = clone(attrs || {}), k;
    do { id = typeId + "-" + (n++); } while (this.entities[id]);
    if (this.recorder) {
      var rrels = {};
      for (k in (rels || {})) if (rels.hasOwnProperty(k)) rrels[k] = this.recRef(rels[k]);
      this.recorder.made[id] = 1;
      this.record({ spawn: typeId, as: id, label: label, note: note || "", attrs: given, rels: rrels });
    }
    var ent = {
      id: id, type: typeId, label: label || (td.label + " " + n),
      note: note || "", attrs: attrs || {}, rels: rels || {}, made: true
    };
    if (ent.attrs.bornDate) ent.attrs.bornDay = this.dayForDate(ent.attrs.bornDate);
    this.entities[id] = ent;
    this.order.push(id);
    var born = ent.attrs.bornDay;
    this.log.push({
      day: this.day, sev: "act", cite: "",
      text: "<b>" + ent.label + "</b> comes into existence as a " + td.label.toLowerCase() +
        (born === this.day ? ", born today — " + this.formatDate(this.day) + "."
         : born !== undefined && born !== null
           ? ", born " + this.formatDate(born) + "." : "."),
      rule: "create:" + typeId,
      who: [ent.id]
    });
    this.rulesOn("create:" + typeId).forEach(function (r) {
      self.fireRule(r, { self: ent, target: null, p: {}, day: self.day });
    });
    return ent;
  };

  Engine.prototype.remove = function (id, asEvent) {
    var self = this, e = this.entities[id], orphaned = [];
    if (!e) return;
    this.record({ remove: this.recRef(id), asEvent: !!asEvent });
    /* A death is an event the scheme may have something to say about. A removal
       in scenario mode is not: it is the author changing the cast. */
    if (asEvent) {
      this.rulesOn("death:" + e.type).forEach(function (r) {
        self.fireRule(r, { self: e, target: null, p: {}, day: self.day });
      });
    }
    this.order = this.order.filter(function (x) { return x !== id; });
    delete this.entities[id];
    this.order.forEach(function (oid) {
      var o = self.entities[oid];
      Object.keys(o.rels || {}).forEach(function (k) {
        if (o.rels[k] === id) { delete o.rels[k]; orphaned.push(o.label); }
      });
    });
    this.log.push({
      day: this.day, sev: "act", cite: "",
      text: "<b>" + e.label + "</b> " + (asEvent ? "dies" : "is removed from the cast") + "." +
        (orphaned.length
          ? " That leaves " + orphaned.join(", ") + " with a relationship pointing at nothing — " +
            "which is its own kind of fact about the scheme."
          : ""),
      who: [id]
    });
  };

  /* Which fields a scheme will let you assert directly, given how you are working.
     In scenario mode you are authoring a state of the world and may assert
     anything. In simulation mode only what nature gives at birth, and what some
     other body of law settles, can be asserted; the rest has to be conferred by
     an act, and age is worked out rather than stated. */
  Engine.prototype.settableAtBirth = function (typeId, simulation) {
    var td = this.typeDef(typeId), out = { fields: [], locked: [], birth: null };
    ((td.create && td.create.fields) || []).forEach(function (f) {
      var o = f.origin || "innate";
      if (o === "birth") { out.birth = f; return; }
      if (!simulation || o === "innate" || o === "exogenous") out.fields.push(f);
      else out.locked.push(f);
    });
    return out;
  };
  Engine.prototype.settableRels = function (typeId, simulation) {
    var td = this.typeDef(typeId), out = { rels: [], locked: [] };
    ((td.create && td.create.rels) || []).forEach(function (r) {
      var o = r.origin || "innate";
      if (!simulation || o === "innate" || o === "exogenous") out.rels.push(r);
      else out.locked.push(r);
    });
    return out;
  };
  Engine.prototype.actionLabel = function (actionId) {
    var a = (this.scheme.actions || []).filter(function (x) { return x.id === actionId; })[0];
    return a ? a.label : actionId;
  };

  Engine.prototype.setRel = function (id, key, targetId) {
    var e = this.get(id), t = targetId ? this.get(targetId) : null;
    if (!e) return;
    var td = this.typeDef(e.type);
    var def = ((td.create && td.create.rels) || []).filter(function (r) { return r.key === key; })[0];
    var label = (def && def.label) || (this.scheme.relLabels || {})[key] || key;
    if ((e.rels[key] || null) === (targetId || null)) return;
    var rr = {}; rr[key] = targetId ? this.recRef(targetId) : null;
    this.record({ set: this.recRef(id), rels: rr });
    if (t) { e.rels[key] = targetId; } else { delete e.rels[key]; }
    this.log.push({
      day: this.day, sev: "", cite: (def && def.cite) || "",
      text: "<b>" + e.label + "</b> — " + label.toLowerCase() + ": " +
            (t ? "<b>" + t.label + "</b>" : "nobody"),
      who: t ? [id, targetId] : [id]
    });
  };

  Engine.prototype.setAttr = function (id, key, value) {
    var e = this.get(id);
    if (!e) return;
    if (e.attrs[key] === value) return;
    var ra = {}; ra[key] = value;
    this.record({ set: this.recRef(id), attrs: ra });
    e.attrs[key] = value;
  };

  Engine.prototype.actionsFor = function (entity) {
    return (this.scheme.actions || []).filter(function (a) { return a.actor === entity.type; });
  };

  Engine.prototype.targetsFor = function (action, actorId) {
    if (!action.target) return [];
    return this.ofType(action.target).filter(function (e) { return e.id !== actorId; });
  };

  /* ------------------------ an empty world ------------------------ */
  Engine.prototype.clearCast = function () {
    this.entities = {};
    this.order = [];
    if (this.recorder) this.recorder.empty = true;
  };

  /* ---------------------------- recording ----------------------------
     While a recorder is on, everything that happens — actors created, acts,
     days passing, facts set by hand, removals — is written down as scenario
     steps, so a run authored by hand or generated by the dice can be saved and
     played again. Actors created during the recording are referred to by alias. */
  Engine.prototype.startRecording = function () {
    this.recorder = { steps: [], made: {}, empty: false };
  };
  Engine.prototype.recRef = function (id) {
    return this.recorder && this.recorder.made[id] ? "@" + id : id;
  };
  Engine.prototype.record = function (step) {
    if (this.recorder && !this.replaying) this.recorder.steps.push(step);
  };

  /* ------------------------ playing a scenario ------------------------
     One player for the console, the checkers and generated runs alike. Steps are
     { actor, action, target, params } · { tick } · { spawn, as, label, attrs, rels }
     · { set, attrs, rels } · { remove, asEvent }. "@alias" names an actor
     created earlier in the same scenario. Returns the alias resolver. */
  Engine.prototype.play = function (sc, onError) {
    var self = this, alias = {};
    function deref(x) {
      if (typeof x === "string" && x.charAt(0) === "@") return alias[x.slice(1)];
      return x;
    }
    if (sc.empty) this.clearCast();
    this.setContext(sc.mode === "nature" ? "nature" : "god");
    (sc.steps || []).forEach(function (st) {
      try {
        var i, k;
        if (st.tick) { for (i = 0; i < Math.min(+st.tick || 0, 3660); i++) self.tick(); return; }
        if (st.spawn) {
          var rels = {};
          for (k in (st.rels || {})) if (st.rels.hasOwnProperty(k)) rels[k] = deref(st.rels[k]);
          var ent = self.spawn(st.spawn, st.label, clone(st.attrs || {}), rels, st.note || "");
          if (st.as) alias[st.as] = ent.id;
          return;
        }
        if (st.set) {
          var who = deref(st.set);
          if (!self.get(who)) throw new Error("no actor " + st.set + " to set");
          for (k in (st.attrs || {})) if (st.attrs.hasOwnProperty(k)) self.setAttr(who, k, st.attrs[k]);
          for (k in (st.rels || {})) if (st.rels.hasOwnProperty(k)) self.setRel(who, k, deref(st.rels[k]));
          return;
        }
        if (st.remove) { self.remove(deref(st.remove), !!st.asEvent); return; }
        if (!self.get(deref(st.actor))) throw new Error("step names an actor that does not exist (" + st.actor + ")");
        self.act(deref(st.actor), st.action, deref(st.target) || null, st.params || {});
      } catch (e) {
        if (onError) onError(e, st);
        else self.log.push({ day: self.day, sev: "stop", cite: "", text: "Scenario step failed: " + e.message });
      }
    });
    return deref;
  };

  /* ---------------------------- the dice ----------------------------
     Generated runs roll from a seed, so the same seed replays the same run. */
  Engine.prototype.seed = function (n) {
    var a = (Math.floor(Number(n)) >>> 0) || 1;
    this.rng = function () {
      a = (a + 0x6D2B79F5) | 0;
      var t = Math.imul(a ^ (a >>> 15), 1 | a);
      t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  };
  Engine.prototype.random = function () { return this.rng ? this.rng() : Math.random(); };

  /* -------------------------- generated runs --------------------------
     A scheme's `simulation.generators` say what happens of its own accord, and
     how often. Each happens through the ordinary doors — spawn, act, remove — so
     a generated run obeys every rule a scripted one does, and records as one.
       { start: n, spawn: {...} }           n of these when the run begins
       { rate: perDay, spawn|act: {...} }    about `perDay` a day
       { per: type, chance: p, act|remove }  each actor of the type, chance p a day
     `when` gates any of them. $param holds the user's parameters. */
  Engine.prototype.genEnv = function (ent) {
    return { self: ent, target: null, p: {}, day: this.day, param: this.param || {} };
  };
  Engine.prototype.startRun = function (sim, param) {
    var self = this;
    this.param = param || {};
    this.genCount = {};
    this.setContext("simulation");
    (sim.generators || []).forEach(function (g) {
      if (g.start === undefined) return;
      var n = Math.max(0, Math.floor(Number(self.evaluate(g.start, self.genEnv(null))) || 0)), i;
      for (i = 0; i < Math.min(n, 1000); i++) self.fireGenerator(g, null);
    });
  };
  Engine.prototype.generate = function (sim) {
    var self = this;
    (sim.generators || []).forEach(function (g) {
      if (g.start !== undefined) return;
      try {
        if (g.per) {
          self.ofType(g.per).forEach(function (ent) {
            if (!self.entities[ent.id]) return;
            var env = self.genEnv(ent);
            if (g.when !== undefined && !self.evaluate(g.when, env)) return;
            if (self.random() < Number(self.evaluate(g.chance === undefined ? 1 : g.chance, env))) self.fireGenerator(g, ent);
          });
          return;
        }
        var rate = Number(self.evaluate(g.rate, self.genEnv(null))) || 0, i;
        var n = Math.floor(rate) + (self.random() < rate - Math.floor(rate) ? 1 : 0);
        for (i = 0; i < n; i++) {
          if (g.when !== undefined && !self.evaluate(g.when, self.genEnv(null))) break;
          self.fireGenerator(g, null);
        }
      } catch (e) {
        self.log.push({ day: self.day, sev: "stop", cite: "", text: "Generator " + g.id + " failed: " + e.message });
      }
    });
  };
  Engine.prototype.fireGenerator = function (g, ent) {
    var env = this.genEnv(ent), k;
    function idOf(x) { return x && typeof x === "object" ? x.id : x; }
    if (g.remove) { if (ent) this.remove(ent.id, true); return; }
    if (g.spawn) {
      var sp = g.spawn, n = this.genCount[g.id] = (this.genCount[g.id] || 0) + 1;
      var attrs = {}, rels = {}, names = sp.names || [], name;
      for (k in (sp.attrs || {})) if (sp.attrs.hasOwnProperty(k)) attrs[k] = this.evaluate(sp.attrs[k], env);
      for (k in (sp.rels || {})) if (sp.rels.hasOwnProperty(k)) {
        var r = idOf(this.evaluate(sp.rels[k], env));
        if (r && this.get(r)) rels[k] = r;
      }
      name = names.length ? names[(n - 1) % names.length] +
        (n > names.length ? " " + (Math.floor((n - 1) / names.length) + 1) : "") : String(n);
      this.spawn(sp.type, String(sp.label || "{name}").replace("{n}", n).replace("{name}", name),
                 attrs, rels, sp.note || "");
      return;
    }
    if (g.act) {
      var a = g.act, actor = idOf(this.evaluate(a.actor, env));
      var target = a.target === undefined ? null : idOf(this.evaluate(a.target, env));
      if (!actor || !this.get(actor)) return;
      if (a.target !== undefined && (!target || !this.get(target))) return;
      env.self = this.get(actor); env.target = target ? this.get(target) : null;
      var p = {};
      env.p = p;
      for (k in (a.params || {})) if (a.params.hasOwnProperty(k)) p[k] = this.evaluate(a.params[k], env);
      this.act(actor, a.action, target, p);
    }
  };

  Engine.prototype.size = function () {
    var sc = this.scheme;
    return {
      types: (sc.types || []).length,
      entities: (sc.entities || []).length,
      actions: (sc.actions || []).length,
      rules: (sc.rules || []).length,
      defs: Object.keys(sc.defs || {}).length,
      observations: (sc.observations || []).length
    };
  };

  global.Engine = Engine;
})(window);
