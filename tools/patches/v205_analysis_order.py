"""v205: Pattern Analysis reordered, first half (review plan Phase 2, step 6).
1. WHAT YOUR USE OF THE METHOD PRODUCED moves to the top, right under AT A GLANCE (3d).
2. THE SAME THING? becomes a prompt at the top of the page while it is unanswered, with a sentence
   from the workbook for each word, so the user sees both in context before answering (3h).
3. WORDS THAT MAKE THE WORLD gets its own heading that opens and closes (3j); the "Test each one"
   sentence is rewritten so a user knows what to do (3k, Claude's wording).
4. YOUR LANDSCAPE, ONE QUESTION AT A TIME: hovering (or focusing) a question shows the question
   and its notes (3b).
5. Bug fix: the THE SAME THING? buttons did nothing (a local name hid the save function).
Usage: python3 v205_analysis_order.py gsm-readable.js"""
import sys

P = sys.argv[1]
s = open(P).read()


def rep(a, b, n=1):
    global s
    c = s.count(a)
    assert c == n, (c, a[:90])
    s = s.replace(a, b)


# 1 + 2: WHAT IT PRODUCED and the SAME THING? prompt open the page
rep(
    """        ((Ot =
          '<div class="part">1 · LOOKING IN<span>Analysis: the pieces, one at a time.</span></div>' +""",
    """        ((Ot =
          (function () {
            var x = window.gsmSameAsk || "";
            window.gsmSameAsk = "";
            return x;
          })() +
          we +
          '<div class="part">1 · LOOKING IN<span>Analysis: the pieces, one at a time.</span></div>' +""",
)
rep(
    """          })() +
          we +
          Ot +
          (C.m.some(function (t) {""",
    """          })() +
          Ot +
          (C.m.some(function (t) {""",
)

# 2: THE SAME THING? as an opening prompt, each word shown in a sentence of the user's own
rep(
    """            pr &&
              c(
                "THE SAME THING?",""",
    """            function sameCtx(a, b) {
              var T = [];
              (C.m || []).forEach(function (r, i) {
                T.push([String(r[3] || ""), "N" + (i + 1)]);
              });
              ((C.p && C.p.m) || []).forEach(function (r, i) {
                T.push([String(r[3] || ""), "N" + (i + 1) + " (place)"]);
              });
              (C.a || []).forEach(function (t, i) {
                T.push([String(t || ""), "Q." + (i + 1)]);
              });
              function rx(w) {
                return new RegExp("\\\\b" + w.replace(/[.*+?^${}()|[\\]\\\\]/g, "\\\\$&") + "\\\\b", "i");
              }
              var used = "";
              function one(w, o) {
                var R = rx(w),
                  Ro = rx(o),
                  best = null,
                  any = null;
                T.forEach(function (x) {
                  x[0]
                    .replace(/\\s+/g, " ")
                    .split(/(?<=[.!?])\\s+(?=[A-Z0-9“"(])/)
                    .forEach(function (z) {
                      var n = z.split(" ").length;
                      if (!R.test(z) || n < 5) return;
                      any || (any = [z, x[1]]);
                      !best && !Ro.test(z) && n <= 40 && x[1] !== used && (best = [z, x[1]]);
                    });
                });
                var p = best || any;
                if (!p) return "";
                used = p[1];
                var z = p[0].trim(),
                  m = z.search(R);
                z.length > 200 &&
                  ((z = z.slice(Math.max(0, m - 90), m + 110)),
                  (z = (m > 90 ? "…" : "") + z.replace(/^\\S*\\s/, "").replace(/\\s\\S*$/, "") + "…"));
                return (
                  '<div style="margin:3px 0">“' +
                  Gt(z).replace(rx(Gt(w)), function (q) {
                    return "<b>" + q + "</b>";
                  }) +
                  "” (" +
                  p[1] +
                  ")</div>"
                );
              }
              var x = one(a, b) + one(b, a);
              return x ? '<div class="samectx">Where you write each:' + x + "</div>" : "";
            }
            function sameAsk(h, body) {
              var k = body.indexOf('<div class="emo">');
              window.gsmSameAsk =
                '<div class="sameask"><div class="rl">' +
                h +
                "</div><div>" +
                (k > 0 ? body.slice(0, k) + sameCtx(pr[0], pr[1]) + body.slice(k) : body) +
                "</div></div>";
            }
            window.gsmSameAsk = "";
            pr &&
              sameAsk(
                "THE SAME THING?",""",
)
rep(
    """                  "','n')\\">No, different</button></div>",
                [],
                null,
              );
            done.length &&""",
    """                  "','n')\\">No, different</button></div>",
              );
            done.length &&""",
)
rep(
    "#gsm .glance{border:1.5px solid #222;padding:12px 14px;margin:14px 0 6px}",
    "#gsm .glance{border:1.5px solid #222;padding:12px 14px;margin:14px 0 6px}"
    "#gsm .sameask{border:2px solid #111;padding:12px 14px;margin:12px 0 14px;background:#faf8f3}"
    "#gsm .sameask .rl{font-weight:700;letter-spacing:.12em;font-size:12px;margin-bottom:6px}"
    "#gsm .samectx{margin:8px 0 4px;font-size:14px;color:#333}",
)

# 3: WORDS THAT MAKE THE WORLD under its own heading, folded like every other section
rep(
    """                  ". Test each one: what would have to be true for both to hold? If it holds up, change the map; if not, keep it as a voice.</p>",""",
    """                  ". For each, ask what would have to be true for both views to hold. If something would, change your map. If not, keep the note as a voice you have heard, and let your map stand.</p>",""",
)
rep(
    """            parts.length &&
              c(
                "WORDS THAT MAKE THE WORLD",
                '<details class="f7"><summary style="cursor:pointer;text-decoration:underline">Which words, and whose voices, shape this map (' +
                  parts.length +
                  ")</summary>" +
                  parts.join("") +
                  '<p style="color:#666;font-size:13px">Language brings forth the world it speaks of (Winograd &amp; Flores, 1986, p. 174). Nothing here rewrites your words.</p></details>',
                [],
                null,
              );""",
    """            window.gsmWMW = parts.length
              ? '<div class="plab">WORDS THAT MAKE THE WORLD</div><div class="rule"><div class="rl">WHICH WORDS, AND WHOSE VOICES, SHAPE THIS MAP</div><div>' +
                parts.join("") +
                '<p style="color:#666;font-size:13px">Language brings forth the world it speaks of (Winograd &amp; Flores, 1986, p. 174). Nothing here rewrites your words.</p></div></div>'
              : "";""",
)
rep(
    """                  .map(yo)
                  .join("")
              : ""
          );
        })()),""",
    """                  .map(yo)
                  .join("") +
                (function () {
                  var x = window.gsmWMW || "";
                  window.gsmWMW = "";
                  return x;
                })()
              : ""
          );
        })()),""",
)

# 4: hovering a question above YOUR LANDSCAPE shows the question and its notes
rep(
    """      function qbtn(q, label) {
        var b = document.createElement("button");
        b.type = "button";
        b.textContent = label;""",
    """      var qpop = document.createElement("div");
      qpop.className = "gtqpop";
      qpop.style.cssText =
        "display:none;border:1px solid #222;background:#fff;padding:8px 10px;margin:0 0 8px;font:13px/1.4 'Questrial',sans-serif;max-width:760px";
      function qshow(q) {
        if (!q) return void (qpop.style.display = "none");
        qpop.textContent = "";
        var h = document.createElement("div"),
          hb = document.createElement("b");
        hb.textContent = "Q." + q + " ";
        h.appendChild(hb);
        h.appendChild(document.createTextNode(QT[q - 1]));
        qpop.appendChild(h);
        var L = rows.filter(function (o) {
          return o.r[0] === q;
        });
        L.slice(0, 6).forEach(function (o) {
          var d = document.createElement("div"),
            t = String(o.r[3]).replace(/\\s+/g, " ").trim(),
            nb = document.createElement("b");
          t.length > 110 && (t = t.slice(0, 110).replace(/\\s+\\S*$/, "") + "…");
          d.style.margin = "3px 0 0 10px";
          nb.textContent = o.id;
          d.appendChild(nb);
          d.appendChild(document.createTextNode((null != o.r[5] ? " (" + EN[o.r[5]] + ")" : "") + " " + t));
          qpop.appendChild(d);
        });
        if (L.length > 6) {
          var m = document.createElement("div");
          m.style.cssText = "margin:3px 0 0 10px;color:#666";
          m.textContent = "…and " + (L.length - 6) + " more. Tap the question to see them all on the ground.";
          qpop.appendChild(m);
        }
        qpop.style.display = "block";
      }
      function qbtn(q, label) {
        var b = document.createElement("button");
        b.type = "button";
        b.textContent = label;
        b.onmouseenter = b.onfocus = function () {
          qshow(q);
        };
        b.onmouseleave = b.onblur = function () {
          qshow(0);
        };""",
)
rep(
    """      $("stage").parentNode.insertBefore(qb, $("stage"));
      function ids(L) {""",
    """      $("stage").parentNode.insertBefore(qb, $("stage"));
      $("stage").parentNode.insertBefore(qpop, $("stage"));
      function ids(L) {""",
)

# 5: THE SAME THING? buttons never saved (a local list named P hid the save function); call it by name
rep("  function P() {\n    (B(), gsmEHrec(),", "  window.gsmSaveP = P;\n  function P() {\n    (B(), gsmEHrec(),")
rep(
    """(C.asks["same|" + a + "|" + b] = v), P());""",
    """(C.asks["same|" + a + "|" + b] = v), window.gsmSaveP());""",
)

s = s.replace('t.textContent = "v204"', 't.textContent = "v205"')
assert 't.textContent = "v205"' in s
open(P, "w").write(s)
