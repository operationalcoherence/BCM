/* Shape detection for Pattern Synthesis (first build, 2026-11-24).
 *
 * Graph in (tools/graph/graph.js), ranked shapes out. Nothing here draws or picks a question.
 *
 * The three shapes (claude/pattern_synthesis_loop_audit_2026-11-24.md):
 *   loop        a cycle: the parts change each other round and back again
 *   settlement  several chains end in one state (a convergence that holds the state in place)
 *   chain       an open chain: where the situation is heading
 *
 * Rules taken from the frozen design, and how they are read here:
 *   - A shape is only as strong as its weakest arrow. Its grade IS that arrow's grade, and the
 *     arrow is named (weakest).
 *   - Only arrows in the graph are used. Candidates (lone inferred pairs) never are: they wait
 *     for the question step, which can call detectShapes on withArrow(...) / withoutArrow(...).
 *   - No shape stands on inference alone (amendment 6).
 *   - Shared parts are counted once (merged notes are already one part in the graph).
 *   - Ranking (amendment 8): grade of the weakest arrow, then distinct parts reached, then
 *     loop > settlement > chain, then fewer arrows, then earliest on the way, then id.
 *   - Novelty (amendment 9): a loop stated inside one note is the person's, given not found.
 *     It is handed back only with the arrows the person didn't state that join it (joins).
 *     With nothing joining it, it yields to every found shape.
 *
 * Calls made here that the frozen docs leave open (each is a general rule, none names a note):
 *   L1 A loop needs direction somewhere. Couplings alone (shared words on one stretch) make a
 *      cluster, not a loop. The one exception is two notes that name each other: each direction
 *      has its own evidence, so that pair is a two-part loop by itself.
 *   L2 A two-part loop otherwise needs two directed arrows, one each way. A shared-word tie read
 *      once as coupling and once as carry is one tie, not a loop.
 *   L3 Loops are at most 4 arrows, the same bound the graph uses for "closes".
 *   L4 The two arrows of a two-part loop must rest on different words. The same shared words
 *      read once as an expectation and once as order are still one tie.
 *   S1 A settlement is at least 3 different parts whose directed arrows end in one part.
 *   S2 The reasons are different: no two of its sources are joined by an arrow of their own
 *      (otherwise it is one chain reaching the state twice).
 *   S3 Nothing feeds back: the state doesn't reach any of its sources within 3 steps.
 *   S4 At least 2 of its arrows are stated or placed. The goal is never a settlement's state.
 *   S5 Each of its arrows is directed by the text (a cue) or by the person (a drawn link or an
 *      answer), never by order alone. The epistemology counts "configurations of stated
 *      conditions" as reliable and direction read from order as weak; a convergence read from
 *      order alone is only the later note that echoes the most earlier words (a hub).
 *   C1 A chain is at least 2 directed arrows (3 parts) and at most 5 arrows.
 *   C2 A chain made only of one theme's links is the theme (already in graph.themes), not a chain.
 *   C3 A chain inside a loop, or inside a longer chain of the same grade, isn't listed again.
 *   C4 A chain has at least one arrow directed by the text or the person. A run of shared words
 *      ordered only by position is a sequence of echoes, not a heading.
 *   A6 A shape holds at most one inferred arrow: amendment 6 lets an inferred arrow be the
 *      closing or bridging step of an OTHERWISE supported chain, so two cannot share one shape.
 *   G1 "Given" means stated inside one note. A chain or cycle across notes is BCM's joining of
 *      stated arrows, so it is found, even when every arrow in it is stated.
 */
(function (root) {
  "use strict";

  var RANK = { inferred: 1, placed: 2, stated: 3 };
  var TYPE_RANK = { loop: 0, settlement: 1, chain: 2 };
  var MAX_LOOP = 4,
    MAX_CHAIN = 5,
    BACK = 3,
    BUDGET = 4000000; // DFS steps across the whole run; past it the result says truncated

  function detectShapes(g, opts) {
    opts = opts || {};
    var budget = opts.budget || BUDGET,
      truncated = false,
      cut = [];
    var nodes = g.nodes || [],
      nodeById = {},
      order = {};
    nodes.forEach(function (n, i) {
      nodeById[n.id] = n;
      order[n.id] = i;
    });
    var arrows = (g.arrows || []).map(function (r, i) {
      return { i: i, r: r };
    });

    /* steps: for each part, the arrows that leave it (undirected arrows leave both ends) */
    var steps = {},
      dsteps = {},
      inD = {},
      touch = {};
    function push(o, k, v) {
      (o[k] = o[k] || []).push(v);
    }
    arrows.forEach(function (a) {
      var r = a.r;
      if (r.from === r.to) return;
      push(touch, r.from, a);
      push(touch, r.to, a);
      if (r.undirected) {
        push(steps, r.from, { to: r.to, a: a });
        push(steps, r.to, { to: r.from, a: a });
      } else {
        push(steps, r.from, { to: r.to, a: a });
        push(dsteps, r.from, { to: r.to, a: a });
        push(inD, r.to, a);
      }
    });
    var linked = {}; // any arrow between two parts
    arrows.forEach(function (a) {
      if (a.r.from === a.r.to) return;
      linked[a.r.from + "|" + a.r.to] = linked[a.r.to + "|" + a.r.from] = 1;
    });
    var ids = Object.keys(steps).sort(function (x, y) {
      return (order[x] == null ? 1e9 : order[x]) - (order[y] == null ? 1e9 : order[y]) || (x < y ? -1 : 1);
    });
    var idx = {};
    ids.forEach(function (id, i) {
      idx[id] = i;
    });

    var shapes = [];
    function textDirected(a) {
      return (a.r.evidence || []).some((e) => e.type === "cue" || e.type === "user-link" || e.type === "answer" || e.type === "names-each-other");
    }
    function tieWords(a) {
      var o = {};
      (a.r.evidence || []).forEach(function (e) {
        (e.words || []).concat(e.phrases || []).forEach((w) => (o[w] = 1));
      });
      return o;
    }
    function minGrade(list) {
      var m = 3;
      list.forEach(function (a) {
        m = Math.min(m, RANK[a.r.grade]);
      });
      return m;
    }
    var GRADE = { 1: "inferred", 2: "placed", 3: "stated" };
    function make(type, parts, list, extra) {
      var gmin = minGrade(list);
      if (list.every((a) => a.r.grade === "inferred")) return null; // amendment 6
      if (list.filter((a) => a.r.grade === "inferred").length > 1) return null; // A6
      var weakest = list.filter((a) => RANK[a.r.grade] === gmin);
      // the closing step of a loop, when BCM supplied it, is the one to name
      var closing = list.find((a) => a.r.grade === "inferred" && a.r.role === "closes");
      var s = {
        type: type,
        parts: parts,
        arrows: list.map((a) => a.r),
        grade: GRADE[gmin],
        weakest: weakest.map((a) => a.r),
        burden: (closing || weakest[0]).r,
        given: false,
        reached: parts.filter((id) => !nodeById[id] || nodeById[id].kind !== "goal").length,
        _ai: list.map((a) => a.i),
      };
      for (var k in extra || {}) s[k] = extra[k];
      s.key = type + ":" + parts.join(">");
      return s;
    }

    /* ---------- loops ---------- */
    // stated inside one note: given (amendment 9)
    var inNote = {};
    arrows.forEach(function (a) {
      if (a.r.from === a.r.to && a.r.kind === "loop") push(inNote, a.r.from, a);
    });
    Object.keys(inNote).forEach(function (id) {
      var s = make("loop", [id], inNote[id], { given: true });
      if (!s) return;
      // what the person didn't state that joins it
      s.joins = (touch[id] || []).filter((a) => a.r.grade !== "stated").map((a) => a.r);
      shapes.push(s);
    });
    // two notes that name each other (L1)
    arrows.forEach(function (a) {
      if (a.r.from !== a.r.to && (a.r.evidence || []).some((e) => e.type === "names-each-other")) {
        var p = [a.r.from, a.r.to].sort((x, y) => idx[x] - idx[y]);
        var s = make("loop", p, [a], { mutual: true });
        if (s) shapes.push(s);
      }
    });
    // cycles of 2 to MAX_LOOP arrows, each found once from its earliest part
    var cycles = {};
    ids.forEach(function (s0) {
      var i0 = idx[s0];
      var path = [s0],
        used = [],
        onPath = {};
      onPath[s0] = 1;
      (function dfs(u) {
        if (truncated) return;
        (steps[u] || []).forEach(function (st) {
          if (truncated) return;
          if (--budget <= 0) return void (truncated = true);
          if (used.indexOf(st.a) >= 0) return;
          var v = st.to;
          if (v === s0 && used.length + 1 >= 2) {
            var list = used.concat([st.a]);
            var directed = list.filter((a) => !a.r.undirected).length;
            if (!directed) return; // L1
            if (list.length === 2 && directed < 2) return; // L2
            if (list.length === 2) {
              var w0 = tieWords(list[0]),
                w1 = tieWords(list[1]);
              if (Object.keys(w0).some((w) => w1[w])) return; // L4
            }
            var key = path.join(">");
            var gr = minGrade(list);
            var prev = cycles[key];
            if (!prev || gr > prev.g) cycles[key] = { g: gr, parts: path.slice(), list: list };
            return;
          }
          if (onPath[v] || idx[v] == null || idx[v] < i0 || used.length + 1 >= MAX_LOOP) return;
          onPath[v] = 1;
          path.push(v);
          used.push(st.a);
          dfs(v);
          used.pop();
          path.pop();
          onPath[v] = 0;
        });
      })(s0);
    });
    // a cycle run the other way round (through couplings) is the same cycle
    var seenRing = {};
    Object.keys(cycles)
      .sort()
      .forEach(function (k) {
        var c = cycles[k];
        var ring = c.parts.slice().sort().join("|");
        var dirKey = ring + "#" + c.list.map((a) => a.i).sort((x, y) => x - y).join(",");
        if (seenRing[dirKey]) return;
        seenRing[dirKey] = 1;
        var s = make("loop", c.parts, c.list);
        if (s) shapes.push(s);
      });
    // keep the best-graded reading of each set of parts
    var bestLoop = {};
    shapes = shapes.filter(function (s) {
      if (s.type !== "loop" || s.given) return true;
      var k = s.parts.slice().sort().join("|");
      var b = bestLoop[k];
      if (!b || RANK[s.grade] > RANK[b.grade] || (RANK[s.grade] === RANK[b.grade] && s.mutual && !b.mutual)) {
        if (b) b._drop = true;
        bestLoop[k] = s;
        return true;
      }
      return false;
    });
    shapes = shapes.filter((s) => !s._drop);

    if (truncated) cut.push("loops");
    truncated = false;
    budget = opts.budget || BUDGET; // each phase gets its own budget, so one can't starve another
    /* ---------- settlements ---------- */
    function reachesAny(from, targets, n) {
      var frontier = [from],
        seen = {};
      seen[from] = 1;
      for (var k = 0; k < n; k++) {
        var next = [];
        for (var f = 0; f < frontier.length; f++) {
          var out = dsteps[frontier[f]] || [];
          for (var j = 0; j < out.length; j++) {
            var y = out[j].to;
            if (targets[y]) return true;
            if (!seen[y]) {
              seen[y] = 1;
              next.push(y);
            }
          }
        }
        frontier = next;
      }
      return false;
    }
    Object.keys(inD)
      .sort((x, y) => (idx[x] || 0) - (idx[y] || 0))
      .forEach(function (t) {
        if (nodeById[t] && nodeById[t].kind === "goal") return; // S4
        var bySrc = {};
        inD[t].forEach(function (a) {
          if (!textDirected(a)) return; // S5
          var b = bySrc[a.r.from];
          if (!b || RANK[a.r.grade] > RANK[b.r.grade]) bySrc[a.r.from] = a;
        });
        var srcs = Object.keys(bySrc).filter(function (s) {
          var o = {};
          o[s] = 1;
          return !reachesAny(t, o, BACK); // S3
        });
        srcs.sort((x, y) => RANK[bySrc[y].r.grade] - RANK[bySrc[x].r.grade] || idx[x] - idx[y]);
        var chosen = [];
        srcs.forEach(function (s) {
          if (chosen.every((c) => !linked[c + "|" + s])) chosen.push(s); // S2
        });
        if (chosen.length < 3) return; // S1
        var list = chosen.map((s) => bySrc[s]);
        if (list.filter((a) => a.r.grade !== "inferred").length < 2) return; // S4
        chosen.sort((x, y) => idx[x] - idx[y]);
        var s = make("settlement", chosen.concat([t]), chosen.map((c) => bySrc[c]), { target: t, sources: chosen });
        if (s) shapes.push(s);
      });

    /* ---------- open chains ---------- */
    var loopArrowSets = shapes.filter((s) => s.type === "loop").map((s) => new Set(s._ai));
    var paths = [];
    ids.forEach(function (s0) {
      var path = [s0],
        used = [],
        onPath = {};
      onPath[s0] = 1;
      (function dfs(u) {
        if (truncated) return;
        var ext = false;
        (dsteps[u] || []).forEach(function (st) {
          if (truncated || onPath[st.to] || used.length >= MAX_CHAIN) return;
          if (--budget <= 0) return void (truncated = true);
          ext = true;
          onPath[st.to] = 1;
          path.push(st.to);
          used.push(st.a);
          if (used.length >= 2) paths.push({ parts: path.slice(), list: used.slice() });
          dfs(st.to);
          used.pop();
          path.pop();
          onPath[st.to] = 0;
        });
      })(s0);
    });
    if (truncated) cut.push("chains");
    // C3: drop a chain that sits inside a longer one of the same or better grade
    var cover = {};
    paths.forEach(function (p) {
      p.g = minGrade(p.list);
      p.k = p.list.map((a) => a.i).join(",");
    });
    paths.forEach(function (p) {
      var L = p.list.length;
      for (var a = 0; a < L; a++)
        for (var b = a + 2; b <= L; b++) {
          if (a === 0 && b === L) continue;
          var sub = p.list
            .slice(a, b)
            .map((x) => x.i)
            .join(",");
          if (!cover[sub] || cover[sub] < p.g) cover[sub] = p.g;
        }
    });
    var seenPath = {};
    paths.forEach(function (p) {
      if (seenPath[p.k]) return;
      seenPath[p.k] = 1;
      if (cover[p.k] && cover[p.k] >= p.g) return;
      // C2: one theme's links only
      var ph = {};
      var allTheme = p.list.every(function (a) {
        return (a.r.evidence || []).every(function (e) {
          if (e.type !== "theme") return false;
          ph[e.phrases[0]] = 1;
          return true;
        });
      });
      if (allTheme && Object.keys(ph).length === 1) return;
      if (!p.list.some(textDirected)) return; // C4
      // C3: inside a loop
      if (loopArrowSets.some((set) => p.list.every((a) => set.has(a.i)))) return;
      var s = make("chain", p.parts, p.list);
      if (s) shapes.push(s);
    });

    /* ---------- containment, for the question step (a shape that holds another) ---------- */
    if (shapes.length <= 2000) {
      var sets = shapes.map((s) => new Set(s.parts));
      shapes.forEach(function (s, i) {
        s.contains = [];
        shapes.forEach(function (o, j) {
          if (i === j || o.parts.length >= s.parts.length) return;
          if (o.parts.every((id) => sets[i].has(id))) s.contains.push(o.key);
        });
      });
    }

    /* ---------- ranking (amendments 8 and 9) ---------- */
    function earliest(s) {
      var m = Infinity;
      s.parts.forEach(function (id) {
        var n = nodeById[id];
        var x = n && n.stretch != null && g.view !== "place" ? (n.x != null ? n.x : n.stretch * 100) : null;
        m = Math.min(m, x == null ? 1e6 + (order[id] || 0) : x * 1e3 + (order[id] || 0));
      });
      return m;
    }
    shapes.forEach(function (s) {
      s.yields = s.given && !(s.joins || []).length;
      s._e = earliest(s);
      delete s._ai;
    });
    shapes.sort(function (a, b) {
      return (
        a.yields - b.yields ||
        RANK[b.grade] - RANK[a.grade] ||
        b.reached - a.reached ||
        TYPE_RANK[a.type] - TYPE_RANK[b.type] ||
        a.arrows.length - b.arrows.length ||
        a._e - b._e ||
        (a.key < b.key ? -1 : a.key > b.key ? 1 : 0)
      );
    });
    shapes.forEach((s, i) => {
      s.rank = i + 1;
      delete s._e;
    });
    return { shapes: shapes, strongest: shapes[0] || null, truncated: cut.length ? cut : false };
  }

  /* The Yes and No pages of a question: the graph with one arrow confirmed by the person, or
     with it taken away. The graph itself is never changed. */
  function same(a, b) {
    return a.from === b.from && a.to === b.to && a.kind === b.kind;
  }
  function withArrow(g, arrow, grade) {
    var c = {};
    for (var k in g) c[k] = g[k];
    var r = {
      from: arrow.from,
      to: arrow.to,
      kind: arrow.kind,
      grade: grade || "stated",
      undirected: !!arrow.undirected,
      evidence: (arrow.evidence || []).concat([{ type: "answer" }]),
    };
    c.arrows = g.arrows.filter((a) => !same(a, r)).concat([r]);
    c.candidates = (g.candidates || []).filter((a) => !same(a, r));
    return c;
  }
  function withoutArrow(g, arrow) {
    var c = {};
    for (var k in g) c[k] = g[k];
    c.arrows = g.arrows.filter((a) => !same(a, arrow));
    c.candidates = (g.candidates || []).filter((a) => !same(a, arrow));
    return c;
  }

  var api = { detectShapes: detectShapes, withArrow: withArrow, withoutArrow: withoutArrow };
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  else root.gsmShapes = api;
})(typeof window !== "undefined" ? window : globalThis);
