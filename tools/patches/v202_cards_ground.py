"""v202: cards that follow the ground (review plan, Phase 1 step 5, first half; P3).
1. The program or strategy rule (review 6o, 6q; decision E10): a card whose notes go from acceptance into aggression,
   distrust, or defiance is a strategy. Programs don't dip from acceptance into those emotions; that is a high-risk
   move. The card says so in its reason. This joins the six things that already tip a card to strategy.
2. A manual switch on every card (6q): "Make it a program" / "Make it a strategy", saved in the workbook
   (asks["mode|…"]), with "Let the engine decide" to undo it. The switch works in both directions.
   Up to four strategies are shown (was three), so a card the rule turns into a strategy isn't pushed off the page;
   a card switched by hand always stays.
3. Cards from the ground (6d): aggression, distrust, or defiance written on the side of the line where things help,
   among acceptance, forms a card of its own even when it shares no recurring word with anything. So a patch of
   aggression added among acceptance changes the strategies. Line maps only.
Engine only, for every workbook.
Usage: python3 v202_cards_ground.py gsm-readable.js"""
import sys

P = sys.argv[1]
s = open(P).read()


def rep(a, b, n=1):
    global s
    c = s.count(a)
    assert c == n, (c, a[:90])
    s = s.replace(a, b)


# the switch: saved in the workbook, read on every pass
rep(
    "  window.gsmData = function () {\n",
    """  document.addEventListener("click", function (ev) {
    var b = ev.target.closest && ev.target.closest("#gsm .gsmmode");
    if (!b) return;
    ev.preventDefault();
    (C.asks && "object" == typeof C.asks) || (C.asks = {});
    var k = "mode|" + b.getAttribute("data-mk"),
      v = b.getAttribute("data-mv");
    v ? (C.asks[k] = v) : delete C.asks[k];
    P();
  });
  function gsmModeOv(k) {
    var v = C.asks && C.asks["mode|" + k];
    return "s" === v ? 1 : "p" === v ? 0 : null;
  }
  function gsmModeBtn(k, isS) {
    var at = String(k).replace(/&/g, "&amp;").replace(/"/g, "&quot;").replace(/</g, "&lt;");
    return (
      ' <button type="button" class="ech gsmmode" data-mk="' +
      at +
      '" data-mv="' +
      (isS ? "p" : "s") +
      '">Make it a ' +
      (isS ? "program" : "strategy") +
      "</button>" +
      (null != gsmModeOv(k) ? ' <button type="button" class="ech gsmmode" data-mk="' + at + '" data-mv="">Let the engine decide</button>' : "")
    );
  }
  window.gsmData = function () {
""",
)
rep("#gsm .coa .purq{", "#gsm .coacall .gsmmode{margin:6px 6px 0 0;font-size:12px}#gsm .coa .purq{")

# 1. the rule, and the switch, for cards that grow from a recurring word
rep(
    "          function Fn(t) {\n            var e = ge[t],",
    """          var EMN = ["aggression", "acceptance", "distrust", "indifference", "defiance"];
          function MixE(t) {
            var acc = [],
              hos = [],
              hn = null;
            xo(t).forEach(function (x) {
              var id = String(x.id).replace(/^note\\s*/, "N");
              if (!/^N\\d+$/.test(id)) return;
              var e = $t(x);
              1 === e ? acc.push(id) : (0 === e || 2 === e || 4 === e) && (hos.push(id), null == hn && (hn = e));
            });
            return acc.length && hos.length ? { acc: acc, hos: hos, e: hn } : null;
          }
          function Fn(t) {
            var OV = gsmModeOv(t);
            if (null != OV) return !!OV;
            if (MixE(t)) return !0;
            var e = ge[t],""",
)
rep(
    '                "condition" === e.c && r.push("it is a condition with nothing behind it yet"),\n',
    """                "condition" === e.c && r.push("it is a condition with nothing behind it yet"),
                (function (mx) {
                  mx &&
                    r.push(
                      "its notes go from acceptance (" +
                        phList(mx.acc.slice(0, 3)) +
                        ") into " +
                        EMN[mx.e] +
                        " (" +
                        phList(mx.hos.slice(0, 3)) +
                        "), a high-risk move that a program cannot plan for",
                    );
                })(MixE(t)),
""",
)
rep("That is the only one of the six things that tips it", "That is the only one of the seven things that tips it")
# the reason line carries the switch; a card the user set says so
rep(
    "            return e\n              ? n.length\n                ? '<div class=\"coacall\">A <b>strategy</b>, because ' +",
    """            var OVr = gsmModeOv(t);
            if (null != OVr)
              return (
                '<div class="coacall">A <b>' +
                (OVr ? "strategy" : "program") +
                "</b>, because you set it as one. Without that, the method would read it as a " +
                (OVr ? "program" : "strategy") +
                "." +
                gsmModeBtn(t, OVr) +
                "</div>"
              );
            return e
              ? n.length
                ? '<div class="coacall">A <b>strategy</b>, because ' +""",
)
rep(
    """                  })() +
                  "</div>"
                : ""
              : '<div class="coacall">A <b>program</b>, because none of the things""",
    """                  })() +
                  gsmModeBtn(t, 1) +
                  "</div>"
                : ""
              : '<div class="coacall">A <b>program</b>, because none of the things""",
)
rep(
    """                    : "helps the goal rather than hindering it") +
                  ".</div>";
          }""",
    """                    : "helps the goal rather than hindering it") +
                  "." +
                  gsmModeBtn(t, 0) +
                  "</div>";
          }""",
)

# a card you switched by hand always stays on the page
rep(
    """          de.forEach(function (t) {
            Fn(t)
              ? zn.length < 3 && !Yn(t, zn.concat(Vn)) && zn.push(t)
              : Vn.length < 2 && !Yn(t, zn.concat(Vn)) && Vn.push(t);
          });""",
    """          de.forEach(function (t) {
            var hand = null != gsmModeOv(t);
            Fn(t)
              ? (hand || zn.length < 4) && !Yn(t, zn.concat(Vn)) && zn.push(t)
              : (hand || Vn.length < 2) && !Yn(t, zn.concat(Vn)) && Vn.push(t);
          });""",
)

# 2. the switch on cards built from what Q.5–Q.7 name
rep(
    "                  h = c || d.length > 0 || (5 === t && s[1] && !u.length);\n",
    "                  h = c || d.length > 0 || (5 === t && s[1] && !u.length),\n"
    "                  OVd = gsmModeOv(r);\n"
    "                null != OVd && (h = !!OVd);\n",
)
rep(
    """                    "</b>, because what it names is " +
                    (h ? "not concrete enough to plan yet" : "concrete enough to plan") +
                    ".</div>" +""",
    """                    (null != OVd
                      ? "</b>, because you set it as one."
                      : "</b>, because what it names is " + (h ? "not concrete enough to plan yet" : "concrete enough to plan") + ".") +
                    gsmModeBtn(r, h) +
                    "</div>" +""",
)

# 3. cards from the ground, after the cards from Q.3 and Q.7
GROUND = r"""              }).join("") +
              (function () {
                if (!Hn()) return "";
                var NS = a.filter(function (x) {
                    return x.txt.trim() && x.line && /^(?:N|note\s*)\d+$/.test(x.id);
                  }),
                  hos = NS.filter(function (x) {
                    var e = $t(x);
                    return x.line[2] < 118 && (0 === e || 2 === e || 4 === e);
                  }),
                  acc = NS.filter(function (x) {
                    return 1 === $t(x);
                  }),
                  dd = function (p, q) {
                    return Math.hypot(p.line[1] - q.line[1], p.line[2] - q.line[2]);
                  },
                  G = [],
                  used = {},
                  idf = function (x) {
                    return String(x.id).replace(/^note\s*/, "N");
                  },
                  open = function (x) {
                    var w = String(x.txt).replace(/\s+/g, " ").trim().split(" ");
                    return Gt(w.slice(0, 14).join(" ").replace(/[.,;:]$/, "")) + (w.length > 14 ? "…" : "");
                  },
                  WHY = [
                    "aggression can tip toward defiance, the most severe emotion",
                    "",
                    "distrust can turn more severe instead of more benevolent",
                    "",
                    "defiance is the emotion most resistant to any strategy",
                  ];
                hos.forEach(function (x) {
                  if (used[x.id]) return;
                  var g = [x];
                  used[x.id] = 1;
                  for (var i = 0; i < g.length; i++)
                    hos.forEach(function (y) {
                      !used[y.id] && dd(g[i], y) <= 70 && ((used[y.id] = 1), g.push(y));
                    });
                  var nb = acc.filter(function (z) {
                    return g.some(function (y) {
                      return dd(y, z) <= 70;
                    });
                  });
                  nb.length && G.push({ g: g, nb: nb });
                });
                return G.slice(0, 2)
                  .map(function (Q0) {
                    var ids = Q0.g.map(idf),
                      nbi = Q0.nb.map(idf).slice(0, 3),
                      e0 = $t(Q0.g[0]),
                      em = EMN[e0],
                      key = "ground|" + ids.join(","),
                      OV = gsmModeOv(key),
                      S = null == OV ? 1 : OV,
                      mv = [
                        "Start from the acceptance around it (" + phList(nbi) + "): ask the people there what they see in " + phList(ids) + ".",
                        "Find out what the " + em + " in " + phList(ids) + " answers before you act on it.",
                        "Bring something to do that fits what people there already value, not an argument, and keep it small.",
                        "Watch whether the acceptance around it holds.",
                      ];
                    return (
                      '<div class="coa"><div class="hd"><b>' +
                      Gt(em.charAt(0).toUpperCase() + em.slice(1) + " among acceptance, where things help (" + phList(ids) + ")") +
                      '</b><span class="mode' +
                      (S ? " s" : "") +
                      '">' +
                      (S ? "STRATEGY" : "PROGRAM") +
                      '</span></div><div class="bd"><div class="purp"><b>IN SERVICE OF THE GOAL</b> ' +
                      Q0.g
                        .slice(0, 2)
                        .map(function (x) {
                          return "“" + open(x) + "” (" + idf(x) + ")";
                        })
                        .join("; ") +
                      ". It stands in the goal’s way inside ground that otherwise helps it. Turning it keeps the acceptance around it (" +
                      phList(nbi) +
                      ") working for the goal.</div><div class=\"why\">Why: " +
                      em +
                      " on the side of the line where things help, among acceptance (" +
                      phList(nbi) +
                      "). The ground itself puts it here, whatever words it shares with other cards.</div>" +
                      '<div class="coacall">A <b>' +
                      (S ? "strategy" : "program") +
                      "</b>, because " +
                      (null != OV
                        ? "you set it as one."
                        : "going from acceptance into " + em + " is a high-risk move: " + WHY[e0] + " (Vigneaux, 2026).") +
                      gsmModeBtn(key, S) +
                      "</div>" +
                      Un(S, mv, Q0.nb, [], [], Q0.g, [], Q0.g.concat(Q0.nb)) +
                      '<div class="q">' +
                      (S ? Mn : jn) +
                      "</div></div></div>"
                    );
                  })
                  .join("");
              })()));
          var Xn = _n.concat("""
rep('              }).join("")));\n          var Xn = _n.concat(', GROUND)

s = s.replace('t.textContent = "v201"', 't.textContent = "v202"')
assert 't.textContent = "v202"' in s
open(P, "w").write(s)
