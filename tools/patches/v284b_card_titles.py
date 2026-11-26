p='gsm-readable.js'
s=open(p,encoding='utf-8').read()
def r(a,b):
    global s
    assert s.count(a)==1,a[:90]
    s=s.replace(a,b)

# A. tidy before grouping: fragment cards and look-alike ground cards
r('''    SP = SP || [];
    // split readings onto the cards they touch''','''    SP = SP || [];
    cards = gsmTATidy(cards);
    // split readings onto the cards they touch''')

# B. panel at the top uses the action titles
r('''    !opened && !ft && cards[0] && cards[0].querySelector(".tawhy")''','''    if (fe) {
      var fm = fe.querySelector(".tafm");
      fm &&
        cards.forEach(function (c) {
          var a = c.querySelector(".taact"),
            o = tl(c);
          a && o && (fm.innerHTML = fm.innerHTML.split("\\u201c" + Gt(o) + "\\u201d").join("\\u201c" + Gt(a.textContent) + "\\u201d"));
        });
    }
    !opened && !ft && cards[0] && cards[0].querySelector(".tawhy")''')

# C. helpers + better action titles
r('''  function gsmTAAction(c, bd) {''','''  var GSM_EMO_RE = /^(accept|indiffer|distrust|aggress|defian)/,
    GSM_EDGE = { a: 1, an: 1, the: 1, and: 1, or: 1, but: 1, of: 1, to: 1, in: 1, on: 1, at: 1, by: 1, for: 1, with: 1, from: 1, as: 1, is: 1, are: 1, be: 1, being: 1, been: 1, was: 1, were: 1, it: 1, its: 1, this: 1, that: 1, these: 1, those: 1, while: 1, also: 1, including: 1, such: 1, any: 1, some: 1, more: 1, most: 1, very: 1, not: 1, so: 1, than: 1, then: 1, which: 1, who: 1, whether: 1, into: 1, about: 1, both: 1, all: 1, each: 1, their: 1, they: 1, them: 1, there: 1, how: 1, what: 1, when: 1, where: 1 };
  /* v284: the shortest whole phrase the user wrote: no edge words, never cut inside what they wrote, at most five words */
  function gsmTAPhrase(ph, sent) {
    ph = String(ph || "").replace(/[\\u2026.]+$/, "").replace(/\\s+/g, " ").trim();
    var w = ph.split(" "),
      lw = function (x) {
        return String(x || "").toLowerCase().replace(/[^a-z0-9'-]/g, "");
      };
    /* a word cut off at the end, where the sentence carries on with a word of its own: "changing work" -> "changing work life" */
    var S = String(sent || "").replace(/\\s+/g, " "),
      sw = S.split(" "),
      at = -1;
    for (var i = 0; i + w.length <= sw.length; i++) {
      var ok = 1;
      for (var j = 0; j < w.length; j++) lw(sw[i + j]) !== lw(w[j]) && (ok = 0);
      if (ok) {
        at = i;
        break;
      }
    }
    if (at >= 0 && w.length < 5) {
      var nx = sw[at + w.length];
      nx && !GSM_EDGE[lw(nx)] && !/[,;:.]$/.test(w[w.length - 1]) && /^[a-z]/i.test(nx) && w.push(nx.replace(/[,;:.!?)]+$/, ""));
    }
    while (w.length > 1 && GSM_EDGE[lw(w[0])]) w.shift();
    while (w.length > 1 && GSM_EDGE[lw(w[w.length - 1])]) w.pop();
    if (w.length > 5) {
      w = w.slice(0, 5);
      while (w.length > 1 && GSM_EDGE[lw(w[w.length - 1])]) w.pop();
    }
    return w.join(" ").replace(/[,;:]+$/, "");
  }
  /* v284: before cards are grouped, a card titled by a fragment of another card's phrase goes (the fuller one
     stays), and cards that read the same off the ground (same emotion among acceptance) become one card */
  function gsmTATidy(cards) {
    var tx = function (el) {
        return el ? el.textContent.replace(/\\s+/g, " ").trim() : "";
      },
      ph = function (c) {
        if (c.hasAttribute("data-seed") || c.hasAttribute("data-ground")) return "";
        var b = c.querySelector(".hd .hdt b") || c.querySelector(".hd b"),
          t = tx(b).toLowerCase();
        return t && !GSM_EMO_RE.test(t) ? " " + t.replace(/[^a-z0-9 -]/g, "") + " " : "";
      },
      gone = [];
    cards.forEach(function (c) {
      var p0 = ph(c);
      if (!p0) return;
      cards.some(function (d) {
        var p1 = d !== c && gone.indexOf(d) < 0 ? ph(d) : "";
        return p1 && p1.length > p0.length && p1.indexOf(p0) >= 0;
      }) && gone.push(c);
    });
    var gk = {};
    cards.forEach(function (c) {
      if (!c.hasAttribute("data-ground")) return;
      var k = tx(c.querySelector(".hd b")) + "|" + tx(c.querySelector(".hd .mode"));
      if (!gk[k]) return void (gk[k] = { c: c, more: [] });
      gk[k].more.push(c);
      gone.push(c);
    });
    Object.keys(gk).forEach(function (k) {
      var g = gk[k];
      if (!g.more.length) return;
      var ids = [tx(g.c.querySelector(".hd .gids"))].concat(
        g.more.map(function (c) {
          return tx(c.querySelector(".hd .gids"));
        }),
      );
      g.c.setAttribute("data-gall", ids.join("|"));
      var bd = g.c.querySelector(".bd"),
        al = document.createElement("div");
      al.className = "why tagalso";
      al.innerHTML =
        "Also here: " +
        g.more
          .map(function (c) {
            var w = tx(c.querySelector(".bd > .why")).replace(/^Why:\\s*/, ""),
              nb = (/among acceptance \\(([^)]*)\\)/.exec(w) || [])[1];
            return Gt(tx(c.querySelector(".hd .gids"))) + (nb ? ", among " + Gt(nb) : "");
          })
          .join("; ") +
        ". Each sits in the same kind of ground, so the same moves apply.";
      var w0 = bd && bd.querySelector(":scope > .why");
      w0 ? w0.parentNode.insertBefore(al, w0.nextSibling) : bd && bd.appendChild(al);
    });
    gone.forEach(function (c) {
      c.parentNode && c.parentNode.removeChild(c);
    });
    return cards.filter(function (c) {
      return gone.indexOf(c) < 0;
    });
  }
  function gsmTAAction(c, bd) {''')

# ground: name every note merged in
r('''      var gm = /^(\\w+) among acceptance/.exec(t),
        ids = tx(c.querySelector(".hd .gids"));''','''      var gm = /^(\\w+) among acceptance/.exec(t),
        ga = (c.getAttribute("data-gall") || "").split("|").filter(Boolean),
        ids = ga.length > 1 ? gsmMeanList(ga) : tx(c.querySelector(".hd .gids"));''')

# phrase cards: clean phrase, verb from the first move
r('''    if (!t) return null;
    var ph = q(t),''','''    if (!t) return null;
    var sent = (/^:\\s*\\u201C(.*)\\u201D/.exec(tx(c.querySelector(".hd .phctx"))) || [])[1] || "",
      ph = q(GSM_EMO_RE.test(t.toLowerCase()) ? t : gsmTAPhrase(t, sent) || t),
      fm = tx(bd.querySelector(".csec .csn li") || null),
      both = /\\bis pulled both ways/.test(call),
      FM = [
        [/^Start from the support/, both ? "Build on the support for " + ph + ", then reach the other side" : "Build on the support for " + ph],
        [/^Sketch two or three designs/, "Design " + ph + ": sketch two or three, test them small"],
        [/^Redesign it with those who oppose it/, "Redesign " + ph + " with those who oppose it"],
        [/^Ask those doing it what they need/, "Keep " + ph + " going: ask those doing it what they need"],
        [/^Carry out what Q\\.5 designs/, "Carry out what you designed for " + ph],
        [/^Reinforce what Q\\.\\d describes/, "Reinforce " + ph],
        [/^Build on what/, "Build on " + ph],
        [/^Check back if circumstances change/, "Keep " + ph + " running, and check back if circumstances change"],
      ];
    for (var fi = 0; fi < FM.length; fi++) if (FM[fi][0].test(fm)) return FM[fi][1];
    var''')
open(p,'w',encoding='utf-8').write(s)
print('ok')
