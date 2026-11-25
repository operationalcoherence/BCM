/* The relationship graph for Pattern Synthesis (first build, 2026-11-24).
 *
 * Workbook in, graded relationships out. Nothing here draws, ranks shapes, or
 * picks a question: those wait until this part is shown to work.
 *
 * Relationships (claude/pattern_synthesis_engine_2026-11-24.md):
 *   carry      earlier ground changes later ground
 *   reachback  what is expected later changes earlier ground
 *   coupling   parts on the same stretch change each other (undirected unless a cue gives direction)
 *   recoil     what you would design changes the ground it was designed for
 *   loop       a whole loop stated inside one note
 *   link       a relation with no kind yet (a user-drawn link, or no order to read)
 *
 * Grades (claude/pattern_synthesis_loop_audit_2026-11-24.md):
 *   stated    the text says it: a cause, "continued", "since", "reinforcing ... itself"
 *   placed    shown by position, a shared phrase, notes that name each other, or a user-drawn link
 *   inferred  one shared significant word, or nearness on a place map; kept ONLY as the closing
 *             or bridging step of an otherwise supported chain (amendment 6)
 *
 * The amendments in claude/pattern_synthesis_architecture_attack_2026-11-24.md are built in:
 *   1 relationships inside one note; 2 identical notes merged, across voices read as split
 *   readings; 3 order only within one voice; 4 user-drawn links are placed, links Patterns made
 *   are never evidence; 5 no order on place maps, nearness never above inferred; 6 inferred only
 *   closes or bridges; 7 shared terms use the engine's significance rules.
 *
 * Words use the engine's own tokenizer (the stopword list Lt, the -ly exceptions At, and the
 * stemmer Nt in gsm-readable.js), so the graph and the reading pages agree on what a word is.
 */
(function (root) {
  "use strict";

  /* ---------- the engine's lexicon ---------- */
  var LEX = null;
  function loadLexicon() {
    if (LEX) return LEX;
    if (root.gsmLexicon) return (LEX = root.gsmLexicon); // inside the page, the engine hands its own
    var fs = require("fs"),
      p = require("path");
    var src = fs.readFileSync(p.join(__dirname, "..", "..", "gsm-readable.js"), "utf8");
    var lt = src.match(/var Lt =\s*"([a-z' ]+)"/);
    var at = src.match(/var At = (\{[\s\S]*?\});/);
    if (!lt || !at) throw new Error("graph.js: engine lexicon not found in gsm-readable.js");
    var stop = {};
    lt[1].split(" ").forEach(function (w) {
      stop[w] = 1;
    });
    LEX = { stop: stop, ly: Function("return " + at[1])() };
    return LEX;
  }
  function Nt(t) {
    // identical to the engine's Nt
    var e = t;
    if (/ies$/.test(e) && e.length > 5) e = e.slice(0, -3) + "y";
    else if (/ing$/.test(e) && e.length > 5) e = e.slice(0, -3);
    else if ((/ed$/.test(e) && e.length > 5) || (/es$/.test(e) && e.length > 6)) e = e.slice(0, -2);
    else if (/s$/.test(e) && !/(ss|us|is)$/.test(e) && e.length > 3) e = e.slice(0, -1);
    return e.length > 6 ? e.slice(0, 6) : e;
  }

  /* Clauses with their kept words and where each word starts, as the engine's Ht keeps them:
     no stopwords, no proper nouns (capitals mid-sentence), nothing under 3 letters, no numbers,
     no -ly words outside the exceptions. */
  function clauses(text) {
    var L = loadLexicon();
    var t = String(text || "").replace(/[’']/g, "");
    t = t.replace(/((?:[.!?;:]\s+|^\s*|\n\s*)(?:["“”(\-–—]\s*)*)([A-Z])/g, function (m, a, b) {
      return a + b.toLowerCase();
    });
    var out = [];
    t.split(/[.!?;:\n]+/).forEach(function (raw) {
      if (!raw.trim()) return;
      var toks = [],
        re = /[A-Za-z][A-Za-z-]*/g,
        m;
      while ((m = re.exec(raw))) {
        var w = m[0].replace(/^-+|-+$/g, "");
        if (/^[A-Z]/.test(w) && w !== "I") continue;
        var low = w.toLowerCase();
        if (low.length < 3 || L.stop[low]) continue;
        if (/ly$/.test(low) && !L.ly[low]) continue;
        low.split("-").forEach(function (part) {
          if (part.length >= 3 && !L.stop[part]) toks.push({ s: Nt(part), at: m.index });
        });
      }
      out.push({ raw: raw.toLowerCase(), toks: toks });
    });
    return out;
  }
  function stemsOf(cl) {
    var o = {};
    cl.forEach(function (c) {
      c.toks.forEach(function (k) {
        o[k.s] = 1;
      });
    });
    return o;
  }
  function bigramsOf(cl) {
    var o = {};
    cl.forEach(function (c) {
      for (var i = 0; i + 1 < c.toks.length; i++) if (c.toks[i].s !== c.toks[i + 1].s) o[c.toks[i].s + " " + c.toks[i + 1].s] = 1;
    });
    return o;
  }
  function spanStems(c, from, to) {
    var o = {};
    c.toks.forEach(function (k) {
      if (k.at >= from && k.at < to) o[k.s] = 1;
    });
    return o;
  }
  function spanBigrams(c, from, to) {
    var o = {},
      t = c.toks.filter(function (k) {
        return k.at >= from && k.at < to;
      });
    for (var i = 0; i + 1 < t.length; i++) if (t[i].s !== t[i + 1].s) o[t[i].s + " " + t[i + 1].s] = 1;
    return o;
  }

  /* ---------- cue words (hand-made; listed here so they can be read and argued with) ---------- */
  // "A <cue> B": A acts on B
  // only verb forms that can't be nouns: "fuel loads" and "feeds" are not causes
  var FWD = /\b(leads? to|led to|results? in|resulting in|causes|causing|driving|fueling|feeding|reinforc\w*|forces|contributes? to(?:ward)?|in turn|prevents?|preventing|enabl\w*|promot\w*|so that)\b/g;
  // "A <cue> B": B acts on A
  var BWD = /\b(because of|because|due to|since|as a result of|driven by|caused by|founded on|supported by|in response to)\b/g;
  // "<cue> X": X persists from earlier ground
  var CONT = /\b(continued|continues|continuing|remains?)\b/g;
  // "<cue> X": X is expected
  // with their grammar, so "expectations of how work is done" and "fear" in a list don't count
  var EXPECT = /\b(likely to|expects?(?= that| to)|expected|expecting|fears?(?= that| of)|feared|worr(?:y|ied|ies)|waiting to see|to see what happens|anticipat\w*|forecast\w*|concern for how)\b/g;
  // the words a cue points at end at the next clause word or comma
  var SPAN_END = /,|\b(to|that|which|who|while|when|where|but|because|so|by|through|about|regarding|concerning|with|for|as|if|than|until|and then)\b/;
  // a whole loop in one note
  var LOOPWORDS = /\b(positive feedback|feedback loop|vicious (?:circle|cycle)|self-reinforc\w*|self-perpetuat\w*|reinforc\w* (?:itself|themselves|each other|one another))\b/;
  // "suppression reinforcing the need for more suppression": the same word before the cue and
  // again after it, marked as more of it
  var REINF = /\breinforc\w*|\bfueling\b|\bfeeding\b|\bdriving\b/g;
  var MORE = /\b(more|further|greater|higher|increased|increasing|even more)\s+(\w+\s+){0,2}$/;
  // what an emotion is aimed at, and who holds it
  var TARGET = /\b(toward|towards|against)\b/;
  var HOLDER = /\b(amongst|among)\b/;
  var PEOPLE = /\b(those|people|anyone|others|who|whoever)\b/;
  var EMO_STEM = { aggres: 0, accept: 1, distru: 2, indiff: 3, defian: 4 };

  var HELP_HINDER_Y = 118; // the help/hinder line on line maps (BCM_HANDOFF.md)
  var START_X = 10,
    GOAL_X = 305;
  var COMMON = 0.2; // a word or phrase in more than this share of the parts is too common to tie two of them
  var NEAR_M = 120;
  var PAIR_MAX = 3; // a phrase in more parts than this is a theme: its parts are chained in order, not tied pairwise // place maps: nearer than this, with no shared words, is a candidate (inferred only)

  /* ---------- the parts ---------- */
  function readParts(d) {
    var place = d.view === "place" || (!(d.m || []).length && ((d.p && d.p.m) || []).length > 0);
    var rows = place ? (d.p && d.p.m) || [] : d.m || [];
    var own = (d.voices && d.voices[0]) || "Mine";
    var parts = [];
    rows.forEach(function (r, i) {
      var n = {
        id: r[8] || "row" + i,
        label: place ? r[8] || "row" + i : "N" + (i + 1),
        kind: "note",
        q: r[0],
        text: r[3] || "",
        emo: r[5] == null ? null : r[5],
        voice: r[7] || own,
      };
      if (place) {
        n.lat = r[1];
        n.lng = r[2];
      } else {
        n.x = r[1];
        n.y = r[2];
        n.side = r[2] < HELP_HINDER_Y ? "help" : r[2] > HELP_HINDER_Y ? "hinder" : "line";
      }
      parts.push(n);
    });
    (d.a || []).forEach(function (t, i) {
      if (!String(t || "").trim()) return;
      var q = i + 1,
        mine = parts.filter(function (n) {
          return n.kind === "note" && n.q === q && n.x != null;
        });
      parts.push({
        id: "Q." + q,
        label: "Q." + q,
        kind: "answer",
        q: q,
        text: t,
        emo: null,
        voice: own,
        // an answer sits where its notes sit; with no notes it has no place in the order
        x: !place && mine.length ? mine.reduce((s, n) => s + n.x, 0) / mine.length : null,
      });
    });
    parts.forEach(function (n) {
      n.cl = clauses(n.text);
      n.stems = stemsOf(n.cl);
      n.bigrams = bigramsOf(n.cl);
      // Q.1-Q.4 grasp the context; Q.5-Q.7 design for it. A design note on the hinder side
      // is the situation's own plan, not the reader's, so it counts as context.
      n.role = n.q >= 5 && n.side !== "hinder" ? "design" : "context";
      if (n.x != null) n.stretch = n.x < START_X + (GOAL_X - START_X) / 3 ? 0 : n.x < START_X + (2 * (GOAL_X - START_X)) / 3 ? 1 : 2;
      n.marks = {};
    });
    return { place: place, parts: parts, own: own };
  }

  /* amendment 2: identical notes (same words in the same order) are one part; in two voices,
     a split reading */
  function mergeIdentical(parts) {
    var seen = {},
      keep = [],
      splits = [],
      allLabels = {};
    parts.forEach(function (n) {
      allLabels[n.label] = n.id;
      if (n.kind !== "note") return keep.push(n);
      var key = n.cl
        .map(function (c) {
          return c.toks.map((k) => k.s).join(" ");
        })
        .join("|");
      if (!key) return keep.push(n);
      var first = seen[key];
      if (!first) {
        seen[key] = n;
        n.aliases = [];
        n.voices = [n.voice];
        return keep.push(n);
      }
      first.aliases.push(n.id);
      allLabels[n.label] = first.id;
      if (first.voices.indexOf(n.voice) < 0) {
        first.voices.push(n.voice);
        var sp = splits.find((s) => s.id === first.id);
        if (!sp) splits.push((sp = { id: first.id, labels: [first.label], voices: [first.voice] }));
        sp.labels.push(n.label);
        sp.voices.push(n.voice);
      }
    });
    return { parts: keep, splits: splits, allLabels: allLabels };
  }

  /* ---------- significance (amendment 7) ---------- */
  function frequencies(parts, goal) {
    var df = {},
      bf = {},
      docs = parts.map((n) => [n.stems, n.bigrams]);
    var gcl = clauses(goal);
    docs.push([stemsOf(gcl), bigramsOf(gcl)]);
    docs.forEach(function (d) {
      Object.keys(d[0]).forEach((s) => (df[s] = (df[s] || 0) + 1));
      Object.keys(d[1]).forEach((b) => (bf[b] = (bf[b] || 0) + 1));
    });
    var N = docs.length;
    return {
      N: N,
      df: df,
      bf: bf,
      commonStem: (s) => (df[s] || 0) >= 3 && df[s] / N > COMMON,
      sigBigram: (b) => (bf[b] || 0) >= 2 && !((bf[b] || 0) >= 3 && bf[b] / N > COMMON),
      pairPhrase: (b) => (bf[b] || 0) <= PAIR_MAX,
    };
  }

  /* How strongly two sets of words tie: a shared phrase, two or more shared words, or one. */
  function tie(F, aStems, aBig, bStems, bBig, longText) {
    var ph = Object.keys(aBig).filter((b) => bBig[b] && F.sigBigram(b) && F.pairPhrase(b));
    var ws = Object.keys(aStems).filter((s) => bStems[s] && (F.df[s] || 0) >= 2 && !F.commonStem(s));
    if (ph.length) return { level: "phrase", phrases: ph, words: ws };
    // a long answer shares many words with everything, so it ties only by a phrase or one word
    if (ws.length >= 2 && !longText) return { level: "words", phrases: [], words: ws };
    if (ws.length >= 1) return { level: "word", phrases: [], words: ws };
    return null;
  }
  function isLong(n) {
    return n.kind === "answer";
  }

  function kindFor(a, b) {
    if (a.role === "design" && b.role === "context") return "recoil";
    if (a.stretch == null || b.stretch == null) return "link";
    if (a.stretch < b.stretch) return "carry";
    if (a.stretch > b.stretch) return "reachback";
    return "coupling";
  }
  function metres(a, b) {
    var R = 6371000,
      t = Math.PI / 180;
    var dl = (b.lat - a.lat) * t,
      dg = (b.lng - a.lng) * t;
    var h = Math.sin(dl / 2) ** 2 + Math.cos(a.lat * t) * Math.cos(b.lat * t) * Math.sin(dg / 2) ** 2;
    return 2 * R * Math.asin(Math.sqrt(h));
  }

  /* ---------- the graph ---------- */
  var RANK = { inferred: 1, placed: 2, stated: 3 };
  function buildGraph(d, opts) {
    opts = opts || {};
    var R = readParts(d || {});
    var M = mergeIdentical(R.parts);
    var parts = M.parts,
      place = R.place;
    var byId = {};
    parts.forEach((n) => (byId[n.id] = n));
    var F = frequencies(parts, d.goal || "");
    var A = {};
    function add(from, to, kind, grade, ev, undirected) {
      if (from === to && kind !== "loop") return;
      var f = from,
        t = to;
      if (undirected && f > t) (f = to), (t = from);
      var key = f + "|" + t + "|" + kind + (undirected ? "|u" : "");
      var r = A[key];
      if (!r) r = A[key] = { from: f, to: t, kind: kind, grade: grade, undirected: !!undirected, evidence: [] };
      if (RANK[grade] > RANK[r.grade]) r.grade = grade;
      r.evidence.push(ev);
    }
    var sameVoice = (a, b) => a.voice === b.voice || (a.kind === "answer") !== (b.kind === "answer");
    var notes = parts.filter((n) => n.kind === "note");

    /* 1. Stated: cues inside a note (amendment 1) */
    parts.forEach(function (n) {
      n.cl.forEach(function (c) {
        if (LOOPWORDS.test(c.raw)) add(n.id, n.id, "loop", "stated", { type: "cue", cue: c.raw.match(LOOPWORDS)[0] });
        var m;
        REINF.lastIndex = 0;
        while ((m = REINF.exec(c.raw))) {
          var L = spanStems(c, 0, m.index);
          var same = [];
          c.toks.forEach(function (k) {
            if (k.at > m.index && L[k.s] && MORE.test(c.raw.slice(Math.max(m.index, k.at - 40), k.at))) same.push(k.s);
          });
          if (same.length) add(n.id, n.id, "loop", "stated", { type: "cue", cue: m[0], words: same });
        }
        [
          [FWD, "fwd"],
          [BWD, "bwd"],
          [CONT, "cont"],
          [EXPECT, "expect"],
        ].forEach(function (pair) {
          var re = pair[0],
            dir = pair[1];
          re.lastIndex = 0;
          while ((m = re.exec(c.raw))) {
            var end = m.index + m[0].length;
            var rest = c.raw.slice(end),
              stop = rest.search(SPAN_END),
              stopAt = stop < 0 ? 1e9 : end + stop;
            // "since the announcement to the old ways": the cue points at "the announcement"
            if (stop >= 0 && !rest.slice(0, stop).trim()) {
              // the cue is followed straight by a clause word ("leads to"): skip it and read on
              var r2 = rest.slice(stop).replace(/^,?\s*\w+/, "");
              var s2 = r2.search(SPAN_END);
              stopAt = s2 < 0 ? 1e9 : c.raw.length - r2.length + s2;
            }
            var after = spanStems(c, end, stopAt),
              afterB = spanBigrams(c, end, stopAt);
            if (dir === "expect") n.marks.expects = (n.marks.expects ? n.marks.expects + "; " : "") + c.raw.slice(m.index).trim();
            // the other side of the cue, matched against the other parts
            var other = [after, afterB];
            var hits = [];
            parts.forEach(function (o) {
              if (o === n) return;
              if (n.kind === "answer" && o.kind === "answer") return; // two answers restating one fact
              var t = tie(F, other[0], other[1], o.stems, o.bigrams, isLong(o));
              if (!t) return;
              if (!place && !sameVoice(n, o) && t.level !== "phrase") return;
              if (dir === "cont" && !(o.x != null && n.x != null && o.x < n.x)) return; // "continued" looks back
              if (dir === "expect" && !(o.x != null && n.x != null && o.x > n.x)) return; // an expectation looks ahead
              if (place && (dir === "cont" || dir === "expect")) return; // amendment 5
              hits.push({ o: o, t: t, score: t.phrases.length * 2 + t.words.length });
            });
            hits.sort((a, b) => b.score - a.score);
            // one word points at one part only if exactly one part carries it; otherwise the
            // text doesn't say which, and choosing would be guessing
            var wordHits = hits.filter((h) => h.t.level === "word");
            if (wordHits.length > 1) hits = hits.filter((h) => h.t.level !== "word");
            hits.slice(0, 3).forEach(function (h) {
              var ev = { type: "cue", cue: m[0], phrases: h.t.phrases, words: h.t.words };
              // one word after a cue is still one word: the cause is stated, which part it
              // points at is only shown, so the arrow is placed, never stated
              var gr = h.t.level === "word" ? "placed" : "stated";
              if (dir === "fwd") add(n.id, h.o.id, place ? "link" : kindFor(n, h.o) === "reachback" ? "coupling" : kindFor(n, h.o), gr, ev);
              else if (dir === "bwd") add(h.o.id, n.id, place ? "link" : kindFor(h.o, n) === "reachback" ? "coupling" : kindFor(h.o, n), gr, ev);
              else if (dir === "cont") add(h.o.id, n.id, "carry", gr, ev);
              else add(h.o.id, n.id, "reachback", gr, ev);
              if (dir === "cont") ev.order = true;
            });
          }
        });
      });
    });

    /* 2. Placed: notes that name each other (an emotion aimed at the people another note describes) */
    function aim(n) {
      var t = null,
        h = null;
      n.cl.forEach(function (c) {
        var mt = c.raw.match(TARGET);
        if (!mt || t) return;
        var ti = c.raw.indexOf(mt[0]) + mt[0].length;
        t = spanStems(c, ti, 1e9);
        // emotion words in the target name people only after a word for people:
        // "towards those who are defiant" names the defiant; "towards indifference" names an emotion
        var pm = c.raw.slice(ti).match(PEOPLE);
        t.__people = pm ? ti + pm.index : 1e9;
        t.__emo = {};
        c.toks.forEach(function (k) {
          if (k.at >= t.__people && EMO_STEM[k.s] != null) t.__emo[EMO_STEM[k.s]] = 1;
        });
        var mh = c.raw.slice(0, ti).match(HOLDER);
        if (mh) h = spanStems(c, c.raw.indexOf(mh[0]) + mh[0].length, ti);
      });
      return { target: t, holder: h };
    }
    function names(a, b) {
      var at = a.aim.target;
      if (!at) return false;
      if (b.aim.holder && Object.keys(b.aim.holder).some((s) => at[s])) return true;
      return b.emo != null && !!at.__emo[b.emo];
    }
    notes.forEach((n) => (n.aim = aim(n)));
    for (var i = 0; i < notes.length; i++)
      for (var j = i + 1; j < notes.length; j++) {
        var a = notes[i],
          b = notes[j];
        if (names(a, b) && names(b, a)) add(a.id, b.id, "coupling", "placed", { type: "names-each-other" }, true);
      }

    /* 3. Placed and inferred: shared words, read with position */
    var cand = [];
    for (i = 0; i < parts.length; i++)
      for (j = i + 1; j < parts.length; j++) {
        a = parts[i];
        b = parts[j];
        if (a.kind === "answer" && b.kind === "answer") continue;
        var t = tie(F, a.stems, a.bigrams, b.stems, b.bigrams, isLong(a) || isLong(b));
        var near = place && a.lat != null && b.lat != null ? metres(a, b) : null;
        if (!t && !(near != null && near < NEAR_M)) continue;
        var crossVoice = !sameVoice(a, b);
        if (crossVoice && (!t || t.level !== "phrase")) continue; // amendment 3
        var grade = t && t.level !== "word" ? "placed" : "inferred";
        var ev = t ? { type: "shared", phrases: t.phrases, words: t.words } : { type: "proximity", metres: Math.round(near) };
        if (place || crossVoice) {
          // no order to read: a relation, kind unknown unless one side is design
          var k = a.role !== b.role ? "recoil" : "coupling";
          var from = a.role === "design" ? a : b.role === "design" ? b : a;
          var to = from === a ? b : a;
          cand.push([from.id, to.id, k, grade, ev, k !== "recoil"]);
          continue;
        }
        var first = a.x != null && b.x != null && b.x < a.x ? b : a,
          second = first === a ? b : a;
        if (a.role !== b.role) {
          var des = a.role === "design" ? a : b;
          cand.push([des.id, (des === a ? b : a).id, "recoil", grade, ev, false]);
        } else if (first.stretch == null || second.stretch == null) {
          cand.push([a.id, b.id, "link", grade, ev, true]);
        } else if (first.stretch === second.stretch) {
          cand.push([a.id, b.id, "coupling", grade, ev, true]);
        } else {
          ev.order = true; // kept so place maps can be checked never to use order
          cand.push([first.id, second.id, "carry", grade, ev, false]);
        }
      }
    cand.forEach(function (c) {
      if (c[3] !== "inferred") add(c[0], c[1], c[2], c[3], c[4], c[5]);
    });

    /* 3b. Themes: a significant phrase in more than PAIR_MAX parts. Within one voice on a line
       map its parts are chained along the way, each to the next (Carry: the same part on
       successive stretches). Elsewhere there is no order, so it is recorded as a theme only. */
    var themes = [];
    Object.keys(F.bf).forEach(function (b) {
      if (!F.sigBigram(b) || F.pairPhrase(b)) return;
      var mem = parts.filter((n) => n.bigrams[b]);
      if (mem.length < 2) return;
      themes.push({ phrase: b, parts: mem.map((n) => n.id) });
      if (place) return;
      var byVoice = {};
      mem.forEach((n) => {
        if (n.x == null) return;
        (byVoice[n.voice] = byVoice[n.voice] || []).push(n);
      });
      Object.keys(byVoice).forEach(function (v) {
        var ch = byVoice[v].sort((a, b) => a.x - b.x);
        for (var k = 0; k + 1 < ch.length; k++) {
          var a = ch[k],
            b2 = ch[k + 1],
            ev = { type: "theme", phrases: [b], order: true };
          if (a.role !== b2.role) {
            var des = a.role === "design" ? a : b2;
            add(des.id, (des === a ? b2 : a).id, "recoil", "placed", ev);
          } else if (a.stretch === b2.stretch) add(a.id, b2.id, "coupling", "placed", ev, true);
          else add(a.id, b2.id, "carry", "placed", ev);
        }
      });
    });

    /* 4. User-drawn links (amendment 4). Links Patterns made are skipped. */
    (d.links || []).forEach(function (l) {
      if (l.src === "patterns") return;
      var f = byId[l.f] ? l.f : M.allLabels[l.f],
        tt = l.t === "GOAL" ? "GOAL" : byId[l.t] ? l.t : M.allLabels[l.t];
      if (tt === "GOAL" && !byId.GOAL) {
        byId.GOAL = { id: "GOAL", label: "GOAL", kind: "goal", text: d.goal || "", marks: {} };
        parts.push(byId.GOAL);
      }
      if (!byId[f] || !byId[tt]) return;
      add(f, tt, "link", "placed", { type: "user-link", src: l.src || "user" });
    });

    /* 5. Inferred: kept only as the closing or bridging step of a supported chain (amendment 6) */
    var sup = Object.keys(A).map((k) => A[k]);
    var out = {},
      und = {};
    sup.forEach(function (r) {
      if (r.from === r.to) return;
      (out[r.from] = out[r.from] || []).push(r.to);
      (und[r.from] = und[r.from] || []).push(r.to);
      (und[r.to] = und[r.to] || []).push(r.from);
      if (r.undirected) (out[r.to] = out[r.to] || []).push(r.from);
    });
    var comp = {},
      cn = 0;
    Object.keys(und).forEach(function (s) {
      if (comp[s] != null) return;
      var st = [s];
      comp[s] = cn;
      while (st.length) {
        var x = st.pop();
        (und[x] || []).forEach(function (y) {
          if (comp[y] == null) {
            comp[y] = cn;
            st.push(y);
          }
        });
      }
      cn++;
    });
    // closing means finishing a short cycle: a supported way back of at most MAX_BACK steps,
    // so the loop has at most MAX_BACK + 1 arrows (every loop in the hand runs had 2 to 4).
    // In a dense graph nearly any pair "closes" some long cycle, which says nothing.
    var MAX_BACK = 3;
    function reaches(s, goal) {
      var frontier = [s],
        seen = {};
      seen[s] = 1;
      for (var step = 0; step < MAX_BACK; step++) {
        var next = [];
        frontier.forEach(function (x) {
          (out[x] || []).forEach(function (y) {
            if (y === goal) next.found = true;
            if (!seen[y]) {
              seen[y] = 1;
              next.push(y);
            }
          });
        });
        if (next.found) return true;
        frontier = next;
      }
      return false;
    }
    cand.forEach(function (c) {
      if (!c || c[3] !== "inferred") return;
      var f = c[0],
        to = c[1],
        role = null;
      if (reaches(to, f) || (c[5] && reaches(f, to))) role = "closes";
      else if (comp[f] != null && comp[to] != null && comp[f] !== comp[to]) role = "bridges";
      if (!role) return;
      add(f, to, c[2], "inferred", c[4], c[5]);
      var k = Object.keys(A).find((kk) => {
        var r = A[kk];
        return r.grade === "inferred" && ((r.from === f && r.to === to) || (r.from === to && r.to === f)) && r.kind === c[2];
      });
      if (k) A[k].role = role;
    });

    var arrows = Object.keys(A).map((k) => A[k]);
    var candidates = cand
      .filter((c) => c && c[3] === "inferred")
      .map((c) => ({ from: c[0], to: c[1], kind: c[2], grade: "inferred", undirected: c[5], evidence: [c[4]] }));
    var byLabel = {};
    parts.forEach((n) => (byLabel[n.label] = n.id));
    Object.keys(M.allLabels).forEach((l) => {
      if (!byLabel[l]) byLabel[l] = M.allLabels[l];
    });
    return {
      view: place ? "place" : "line",
      nodes: parts.map(function (n) {
        return {
          id: n.id,
          label: n.label,
          kind: n.kind,
          q: n.q,
          role: n.role,
          side: n.side,
          stretch: n.stretch,
          x: n.x,
          emo: n.emo,
          voice: n.voice,
          aliases: n.aliases,
          marks: n.marks,
        };
      }),
      arrows: arrows,
      candidates: candidates,
      themes: themes,
      splits: M.splits,
      byLabel: byLabel,
      allLabels: M.allLabels,
    };
  }

  var api = { buildGraph: buildGraph, _clauses: clauses };
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  else root.gsmGraph = api;
})(typeof window !== "undefined" ? window : globalThis);
