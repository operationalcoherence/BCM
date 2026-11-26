p='gsm-readable.js'
s=open(p,encoding='utf-8').read()
def r(a,b):
    global s
    assert s.count(a)==1,a[:90]
    s=s.replace(a,b)

# 1. a gist with meaning: the note's first clause, in its own words, short; never just the goal's phrase
r('''  function gsmTAGists(ids, n) {''','''  /* v284: what a note says, as a short clause in its own words (who does what, to what), not a bare noun:
     "Sending supporters of the transformation to conferences where like ideas are discussed." -> "sending
     supporters of the transformation to conferences". Rejected when it says no more than the goal does. */
  function gsmTAClause(t) {
    var d = window.gsmData ? window.gsmData() : { goal: "" },
      G = {};
    String(d.goal || "")
      .toLowerCase()
      .replace(/[^a-z0-9\\s-]/g, " ")
      .split(/\\s+/)
      .forEach(function (x) {
        x && (G[x] = 1);
      });
    var c = String(t || "")
      .replace(/\\s+/g, " ")
      .trim()
      .split(/(?<=[.!?])\\s/)[0]
      .split(/[,;:\\u2014(]|\\s-\\s|\\s(?:but|where|which|whereas|because|while|although|though|so that|in order to|as well as)\\s/i)[0]
      .replace(/[.!?]+$/, "")
      .trim();
    c = c
      .replace(/^(\\w+ing) and (?:even |also )?(\\w+ing)\\b/i, "$2")
      .replace(/\\b(?:is|are|was|were) being (\\w+ed) (to|on|in|at|by|into)\\b/i, "$2")
      .replace(/\\b(?:has|have|had) been (\\w+ed)\\b/i, "$1")
      .replace(/^(?:there (?:is|are)|it is|this is|that is)\\s+/i, "")
      .replace(/^(?:the|a|an|this|that|these|those)\\s+/i, "");
    var w = c.split(" ");
    if (w.length > 12) {
      w = w.slice(0, 12);
    }
    while (w.length > 2 && (GSM_EDGE[w[w.length - 1].toLowerCase()] || GSM_AUX[w[w.length - 1].toLowerCase()])) w.pop();
    var own = w.filter(function (x) {
      var l = x.toLowerCase().replace(/[^a-z0-9-]/g, "");
      return l.length > 2 && !GSM_EDGE[l] && !GSM_AUX[l] && !G[l];
    }).length;
    if (w.length < 3 || own < 2) return "";
    var out = w.join(" ");
    return /^[A-Z][a-z]/.test(out) && !/^[A-Z][a-z]+ [A-Z]/.test(out) ? out.charAt(0).toLowerCase() + out.slice(1) : out;
  }
  function gsmTAGists(ids, n) {''')
r('''        g = row ? gsmTAGist(row[3]) : "";''','''        g = row ? gsmTAClause(row[3]) : "";''')
r('''        out.push(g);
    });
    return out;''','''        out.push({ g: g, id: "N" + m[1] });
    });
    return out;''')
r('''        !out.some(function (o) {
          return o === g || o.indexOf(g) >= 0 || g.indexOf(o) >= 0;
        }) &&''','''        !out.some(function (o) {
          return o.g === g || o.g.indexOf(g) >= 0 || g.indexOf(o.g) >= 0;
        }) &&''')

# 2. seed titles: lead with the first thing, the rest go into WHY
r('''    gl.length && (sub = gsmMeanList(gl));
    if (seed)
      return {
        sys: sub ? "Change what keeps " + sub + " in place" : "Change what holds the situation in place",
        ten: sub ? "Work the key tension: " + sub : "Work the key tension",
        loop: sub ? "Change one link in the loop: " + sub : "Change one link in the loop",
        opp: "Scale the alternative that already exists" + (sub ? ": " + sub : ""),
        help: "Build on what already helps" + (sub ? ": " + sub : ""),
        snr: "Reinforce the support you have not backed yet" + (sub ? ": " + sub : ""),
      }[seed] || null;''','''    if (gl.length) {
      c._tagist = gl.slice(1);
      var g0 = gl[0].g + " (" + gl[0].id + ")",
        more = gl.length > 1 ? ", and " + (gl.length - 1) + " more" : "";
      return {
        opp: "Scale what already works, starting with " + g0 + more,
        help: "Build on what already helps, starting with " + g0 + more,
        snr: "Back the support no one has reinforced yet, starting with " + g0 + more,
      }[seed];
    }
    if (seed)
      return {
        sys: sub ? "Change what keeps " + sub + " in place" : "Change what holds the situation in place",
        ten: sub ? "Work the key tension: " + sub : "Work the key tension",
        loop: sub ? "Change one link in the loop: " + sub : "Change one link in the loop",
        opp: "Scale the alternative that already exists" + (sub ? ": " + sub : ""),
        help: "Build on what already helps" + (sub ? ": " + sub : ""),
        snr: "Reinforce the support you have not backed yet" + (sub ? ": " + sub : ""),
      }[seed] || null;''')
r('''gl = !sub && /^(opp|help|snr)$/.test(seed || "") ? gsmTAGists(sids, 3) : [];''','''gl = !sub && /^(opp|help|snr)$/.test(seed || "") ? gsmTAGists(sids, 4) : [];''')

# the rest named in WHY
r('''    also && (why += " " + also);''','''    also && (why += " " + also);
    (c._tagist || []).length &&
      (why +=
        " Also already in place: " +
        c._tagist
          .map(function (x) {
            return x.g + " (" + x.id + ")";
          })
          .join("; ") +
        ".");''')

# 3. a card titled by the goal's own phrase says nothing the goal does not: it goes
r('''        return t && !GSM_EMO_RE.test(t) ? " " + t.replace(/[^a-z0-9 -]/g, "") + " " : "";
      },
      gone = [];''','''        return t && !GSM_EMO_RE.test(t) ? " " + t.replace(/[^a-z0-9 -]/g, "") + " " : "";
      },
      gd = window.gsmData ? " " + String(window.gsmData().goal || "").toLowerCase().replace(/[^a-z0-9 -]/g, " ").replace(/\\s+/g, " ") + " " : "",
      gone = [];
    /* v284: a card titled by the goal's own phrase ("complex adaptive system") says nothing every card does not */
    cards.forEach(function (c) {
      var p0 = ph(c);
      p0 && p0.trim().indexOf(" ") > 0 && gd.indexOf(p0) >= 0 && gone.push(c);
    });''')
open(p,'w',encoding='utf-8').write(s)
print('ok')
