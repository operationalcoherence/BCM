# v284: Taking Action cards scannable in 15 seconds (his review, 25 Nov 2026 17:17).
# Order on every card: action title, FIRST MOVE, WHY, COST, SPLIT (or the obstacle), the map (stays visible),
# then the reasoning and the evidence, folded. The old title stays, in small gray, after the action title.
# Also: DOES THIS ANSWER IT? is now DOES THIS ANSWER THE GOAL?
p = 'gsm-readable.js'
s = open(p, encoding='utf-8').read()

def rep(old, new, n=1):
    global s
    c = s.count(old)
    assert c == n, (c, old[:100])
    s = s.replace(old, new)

# 1. the heading
rep("'<div class=\"rule open\"><div class=\"rl\">DOES THIS ANSWER IT?</div>' +",
    "'<div class=\"rule open\"><div class=\"rl\">DOES THIS ANSWER THE GOAL?</div>' +")
rep('if ("DOES THIS ANSWER IT?" === rt && tst)', 'if ("DOES THIS ANSWER THE GOAL?" === rt && tst)')

# 2. the card layer
old_start = '''      tv = c.getAttribute("data-tv"),
      ts = c.getAttribute("data-ts"),
      ws = c.getAttribute("data-ws"),
      h = "";'''
i0 = s.index(old_start)
old_end = '''      w.parentNode.insertBefore(e, w.nextSibling);
    }
  }
  /* v269: Pattern Synthesis retired.'''
i1 = s.index(old_end, i0)
new = r'''      tv = c.getAttribute("data-tv"),
      ts = c.getAttribute("data-ts"),
      ws = c.getAttribute("data-ws"),
      h = "";
    /* v284: the card reads in 15 seconds: action title, FIRST MOVE, WHY, COST, SPLIT, then the map, then the folds */
    var txt = function (el) {
        return el ? el.textContent.replace(/\s+/g, " ").trim() : "";
      },
      sec = function (r) {
        var x = L2.filter(function (y) {
          return y[0] === r;
        })[0];
        return x ? x[1] : null;
      },
      mapSec = sec(8),
      act = gsmTAAction(c, bd),
      why = txt(sec(1)).replace(/^IN SERVICE OF THE GOAL\s*/, ""),
      why2 = txt(sec(3)).replace(/^Why:\s*/, ""),
      cost = ws || "",
      mcsn = mapSec && mapSec.querySelector(":scope > .gterr-card .csn, .csn");
    /* a card whose purpose only names its source gives its reason instead */
    (!why || /^It is (what you would|already working)/.test(why) || c.hasAttribute("data-ground")) && why2 && (why = why2.charAt(0).toUpperCase() + why2.slice(1));
    if (!cost && mcsn) {
      var mm = /^Crosses the help and hinder line .*?goal\./.exec(mcsn.textContent.trim());
      mm && ((cost = mm[0]), (mcsn.textContent = mcsn.textContent.trim().slice(mm[0].length).trim()));
    }
    if (act) {
      var hd = c.querySelector(".hd"),
        hdt = hd && hd.querySelector(".hdt");
      if (hd && !hd.querySelector(".taact")) {
        var at = document.createElement("div");
        at.className = "taact";
        at.textContent = act;
        hd.insertBefore(at, hd.firstChild);
        hdt && hdt.classList.add("tactx");
      }
    }
    li && (h += '<div class="tafmr"><span class="tsl">FIRST MOVE</span> ' + li.innerHTML + "</div>");
    why && (h += '<div><span class="tsl">WHY</span> ' + Gt(why) + "</div>");
    cost && (h += '<div><span class="tsl">COST</span> ' + (ws ? cost : Gt(cost)) + "</div>");
    (c._tsp || []).length
      ? (h += '<div><span class="tsl">SPLIT</span> ' + c._tsp.join(" ") + "</div>")
      : tv && "yes" !== tv && ts && (h += '<div><span class="tsl">IN THE WAY</span> ' + ts + "</div>");
    var sp = document.createElement("div");
    sp.className = "tastrip";
    sp.innerHTML = h;
    var w = document.createElement("details");
    w.className = "tawhy";
    open && (w.open = !0);
    w.innerHTML = "<summary>Why this action, in full</summary>";
    L2.forEach(function (x) {
      x[1] !== mapSec && w.appendChild(x[1]);
    });
    bd.insertBefore(sp, bd.firstChild);
    var at0 = h ? sp : (sp.parentNode.removeChild(sp), null);
    /* the map stays visible, straight under the strip */
    mapSec && (mapSec.classList.add("tamap"), at0 ? bd.insertBefore(mapSec, at0.nextSibling) : bd.insertBefore(mapSec, bd.firstChild));
    var after = mapSec || at0;
    after ? bd.insertBefore(w, after.nextSibling) : bd.insertBefore(w, bd.firstChild);
    if (L3.length) {
      var e = document.createElement("details");
      e.className = "taev";
      e.innerHTML = "<summary>Evidence</summary>";
      L3.forEach(function (x) {
        e.appendChild(x);
      });
      w.parentNode.insertBefore(e, w.nextSibling);
    }
  }
  /* v284: a card's title as an action, from what the card is (its seed, its ground, or why it is a program or a
     strategy). The old title stays beside it, in small gray. Null when nothing accurate can be said. */
  function gsmTAAction(c, bd) {
    var tx = function (el) {
        return el ? el.textContent.replace(/\s+/g, " ").trim() : "";
      },
      b = c.querySelector(".hd .hdt b") || c.querySelector(".hd b"),
      t = tx(b),
      sub = t.indexOf(": ") >= 0 ? t.slice(t.indexOf(": ") + 2) : "",
      seed = c.getAttribute("data-seed"),
      strat = /STRATEGY/.test(tx(c.querySelector(".hd .mode"))),
      call = tx(bd.querySelector(":scope > .coacall")),
      why = tx(bd.querySelector(":scope > .why")),
      src = (/\((Q\.\d|N\d+|the goal)\)\s*$/.exec(tx(c.querySelector(".hd .phctx"))) || [])[1] || "",
      q = function (x) {
        return "“" + x + "”";
      };
    if (seed)
      return {
        sys: sub ? "Change what keeps " + sub + " in place" : "Change what holds the situation in place",
        ten: sub ? "Work the key tension: " + sub : "Work the key tension",
        loop: sub ? "Change one link in the loop: " + sub : "Change one link in the loop",
        opp: "Scale the alternative that already exists" + (sub ? ": " + sub : ""),
        help: "Build on what already helps" + (sub ? ": " + sub : ""),
        snr: "Reinforce the support you have not backed yet" + (sub ? ": " + sub : ""),
      }[seed] || null;
    if (c.hasAttribute("data-ground")) {
      var gm = /^(\w+) among acceptance/.exec(t),
        ids = tx(c.querySelector(".hd .gids"));
      return gm ? "Keep the " + gm[1].toLowerCase() + (ids ? " in " + ids : "") + " from spreading into the acceptance around it" : null;
    }
    if (!t) return null;
    var ph = q(t),
      qn = (/named (?:in|as something to \w+) \(?(Q\.\d)/.exec(why) || [])[1] || (/^Q\.\d$/.test(src) ? src : ""),
      vb = { "Q.3": "Reinforce", "Q.5": "Design", "Q.6": "Redesign", "Q.7": "Reinforce" }[qn];
    if (/already working/.test(call)) return "Reinforce " + ph;
    if (/\bis pulled both ways/.test(call)) return "Bring both sides of " + ph + " toward the goal";
    if (/strong emotion/.test(call)) return "Answer the resistance around " + ph;
    if (/Q\.5–Q\.7 do not reach it/.test(call)) return "Design something that answers " + ph;
    if (vb && strat) return vb + " " + ph + ": try two or three ways, small";
    if ("Reinforce" === vb) return "Reinforce " + ph;
    return strat ? "Try two or three small ways forward on " + ph : "Set a sequence for " + ph;
  }
  /* v269: Pattern Synthesis retired.'''
s = s[:i0] + new + s[i1 + len(old_end):]

# the old "var mapSec = null; ... " assignments inside the removed block are gone; check none left behind
assert s.count('w.innerHTML = "<summary>Why this action</summary>";') == 0

# 3. styles: action title dominant, old title small gray, FIRST MOVE larger than the other rows
rep('#gsm .tsl{font-size:10.5px;font-weight:700;letter-spacing:.14em;color:#555;margin-right:4px}',
    '#gsm .tsl{font-size:10.5px;font-weight:700;letter-spacing:.14em;color:#555;margin-right:4px}'
    '#gsm .coa .hd{flex-wrap:wrap}#gsm .coa .taact{flex:1 0 100%;font-size:19px;font-weight:700;line-height:1.35;color:#111;margin:0}#gsm .coa .hdt.tactx{flex:1 1 0;min-width:0}'
    '#gsm .coa .hdt.tactx{font-size:12.5px;color:#888;line-height:1.4}#gsm .coa .hdt.tactx b{font-weight:400;color:#888}'
    '#gsm .coa .hdt.tactx .phctx{color:#999}#gsm .tastrip .tafmr{font-size:18px;line-height:1.45;margin-bottom:6px}')

# 4. version
rep('t && (t.textContent = "v283");', 't && (t.textContent = "v284");')
open(p, 'w', encoding='utf-8').write(s)
print('ok')
