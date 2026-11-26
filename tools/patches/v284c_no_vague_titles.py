p='gsm-readable.js'
s=open(p,encoding='utf-8').read()
def r(a,b):
    global s
    assert s.count(a)==1,a[:90]
    s=s.replace(a,b)

r('''  function gsmTAAction(c, bd) {''','''  /* v284: what a note is about, in its own words: the longest run of content words (joined by "and" or "of" at
     most) in its first sentence. Used to name what a card builds on, so no title says only "what already helps". */
  var GSM_AUX = { is: 1, are: 1, was: 1, were: 1, be: 1, been: 1, being: 1, has: 1, have: 1, had: 1, will: 1, would: 1, could: 1, can: 1, may: 1, might: 1, should: 1, must: 1, do: 1, does: 1, did: 1, not: 1, no: 1, yet: 1, just: 1, even: 1, only: 1, already: 1, still: 1, one: 1, other: 1, way: 1, ways: 1 };
  function gsmTAGist(t) {
    var sen = String(t || "").split(/(?<=[.!?])\\s/)[0],
      w = sen.split(/\\s+/).slice(0, 24),
      lw = function (x) {
        return String(x || "").toLowerCase().replace(/[^a-z0-9'-]/g, "");
      },
      ct = function (x) {
        var l = lw(x);
        return l.length > 2 && !GSM_EDGE[l] && !GSM_AUX[l];
      },
      best = [],
      cur = [];
    for (var i = 0; i <= w.length; i++) {
      var x = w[i],
        l = lw(x),
        brk = i === w.length || /[,;:()]/.test(String(w[i - 1] || "").slice(-1));
      if (!brk && ct(x)) cur.push(x.replace(/[,;:.!?()"\\u201c\\u201d]+/g, ""));
      else if (!brk && cur.length && ("and" === l || "of" === l) && ct(w[i + 1])) cur.push(l);
      else {
        while (cur.length && !ct(cur[cur.length - 1])) cur.pop();
        cur.length > best.length && (best = cur);
        cur = !brk || !ct(x) ? [] : [x.replace(/[,;:.!?()"\\u201c\\u201d]+/g, "")];
      }
    }
    return best.length >= 2 ? best.slice(0, 5).join(" ").toLowerCase() : "";
  }
  function gsmTAGists(ids, n) {
    var d = window.gsmData ? window.gsmData() : { m: [] },
      out = [];
    (ids || []).forEach(function (id) {
      var m = /^note (\\d+)$/.exec(String(id).trim()),
        row = m ? (d.m || [])[+m[1] - 1] : null,
        g = row ? gsmTAGist(row[3]) : "";
      g &&
        out.length < (n || 3) &&
        !out.some(function (o) {
          return o === g || o.indexOf(g) >= 0 || g.indexOf(o) >= 0;
        }) &&
        out.push(g);
    });
    return out;
  }
  /* v284: a single word (not an emotion) widened by the list it stands in: "leadership" -> "leadership,
     management, and supervision"; otherwise by the run of words around it */
  function gsmTAWiden(word, sent) {
    var S = String(sent || ""),
      lw = String(word).toLowerCase();
    if (!S) {
      var d = window.gsmData ? window.gsmData() : { a: [], m: [] },
        all = [d.goal || ""].concat(d.a || []).concat(
          (d.m || []).map(function (x) {
            return (x && x[3]) || "";
          }),
        );
      all.some(function (t) {
        return String(t)
          .split(/(?<=[.!?])\\s+|\\n+/)
          .some(function (z) {
            return new RegExp("\\\\b" + lw.replace(/[^a-z0-9]/g, "") + "\\\\b", "i").test(z) && ((S = z), 1);
          });
      });
    }
    if (!S) return "";
    var items = S.split(/,\\s*/).map(function (x) {
        return x.replace(/^(and|or|including|such as)\\s+/i, "").replace(/[.;:]+$/, "").trim();
      }),
      k = -1;
    items.forEach(function (x, i) {
      k < 0 && x.toLowerCase() === lw && (k = i);
    });
    if (k >= 0 && items.length >= k + 3) {
      var L = items.slice(k, k + 3).filter(function (x) {
        return x && x.split(" ").length <= 3;
      });
      if (L.length === 3) return L[0] + ", " + L[1] + ", and " + L[2];
    }
    var g = gsmTAGist(S);
    return g && g.indexOf(lw) >= 0 ? g : "";
  }
  /* v284: is the user's own sentence an instruction? Then it is the title. */
  var GSM_IMP = /^(create|design|redesign|begin|start|offer|provide|send|allow|introduce|perform|build|spread|train|hold|give|set|make|bring|support|scale|engage|encourage|develop|establish|increase|reduce|simplify|continue|use|add|invite|ask|host|fund|hire|run|test|pilot|share|publish|teach|reinforce|keep|remove|replace|change|connect|partner|meet|map|measure|monitor|protect|restore)$/i;
  function gsmTAOwnAction(sent) {
    var S = String(sent || "").replace(/\\s+/g, " ").trim(),
      w = S.split(" ");
    if (!GSM_IMP.test(String(w[0] || "").replace(/[^a-z]/gi, ""))) return "";
    var h = S.split(/,|;|\\.\\s|\\s(?:by|so that|so|which|because|while|in order to)\\s/i)[0].replace(/[.]+$/, "").split(" ");
    h.length > 10 && (h = h.slice(0, 10));
    while (h.length > 2 && GSM_EDGE[String(h[h.length - 1]).toLowerCase()]) h.pop();
    return h.length >= 3 ? h.join(" ") : "";
  }
  function gsmTAAction(c, bd) {''')

# seeds: name what they build on
r('''    if (seed)
      return {''','''    var sids = String(c.getAttribute("data-seedids") || "").split(","),
      gl = !sub && /^(opp|help|snr)$/.test(seed || "") ? gsmTAGists(sids, 3) : [];
    gl.length && (sub = gsmMeanList(gl));
    if (seed)
      return {''')

# phrase cards: own instruction first, then widen single words
r('''      ph = q(GSM_EMO_RE.test(t.toLowerCase()) ? t : gsmTAPhrase(t, sent) || t),''','''      p0 = GSM_EMO_RE.test(t.toLowerCase()) ? t : gsmTAPhrase(t, sent) || t,
      own = gsmTAOwnAction(sent);
    if (own) return own;
    p0.indexOf(" ") < 0 && !GSM_EMO_RE.test(p0.toLowerCase()) && (p0 = gsmTAWiden(p0, sent) || p0);
    var ph = q(p0),''')
open(p,'w',encoding='utf-8').write(s)
print('ok')
