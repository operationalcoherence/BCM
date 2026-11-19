"""v235: plan item 3g. YOUR STORY SO FAR's "Your own words, in the order the method asks for them" opens with a strip:
Q.1 to Q.7 left to right, under THE CONTEXT YOU HAVE GRASPED (Q.1-Q.4) and WHAT YOU WOULD DESIGN (Q.5-Q.7),
with the key phrases of each answer and its notes under it. Phrases only, never a lone word (his rule); a phrase
another question also uses says so in small gray text (no hover needed). The full text folds under the strip.
Usage: python3 v235_own_words_strip.py gsm-readable.js"""
import sys
P = sys.argv[1]
s = open(P).read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:90]); s = s.replace(a, b)

FN = r'''
  /* v235: YOUR OWN WORDS as a strip (plan 3g). Two- and three-word phrases, as written, per question. */
  function gsmOwnStrip() {
    var D = window.gsmData ? window.gsmData() : null;
    if (!D) return "";
    var A = D.a || [],
      M = (D.m || []).concat((D.p && D.p.m) || []),
      SW = {},
      LAB = ["why it has not taken root", "opposition", "support", "conditions", "design", "redesign", "reinforce"];
    "the a an and or but of to in on at by for with from as is are was were be been being it its this that these those there their they them we our you your i my me he she his her not no nor so than then too very can could would should will shall may might must do does did done have has had having also only just more most much many some such each every other into onto over under about above below when what which while where whose who whom how why all any both either neither same own off out up down again further once here because since until though although whether if yet still even like well upon within without between through across around toward towards being way ways thing things lot lots get gets got make makes made need needs needed use used using one two way's it's"
      .split(" ")
      .forEach(function (w) {
        SW[w] = 1;
      });
    var esc = function (t) {
        t = String(t);
        t.length > 48 && (t = t.slice(0, 46) + "\u2026");
        return t.replace(/[&<>"]/g, function (c) {
          return "&#" + c.charCodeAt(0) + ";";
        });
      },
      key = function (w) {
        return w.toLowerCase().replace(/'s$/, "").replace(/(?:ies)$/, "y").replace(/([^s])s$/, "$1");
      };
    function grams(t) {
      var out = {};
      String(t || "")
        .split(/[.;:!?()\[\]{}"“”,\n—–]+|\s-\s/)
        .forEach(function (ch) {
          var ws = ch.split(/\s+/).filter(Boolean).map(function (w) {
            return w.replace(/^[^A-Za-z0-9]+|[^A-Za-z0-9']+$/g, "");
          });
          for (var i = 0; i < ws.length; i++)
            for (var n = 2; n <= 3 && i + n <= ws.length; n++) {
              var seg = ws.slice(i, i + n);
              if (
                seg.some(function (w) {
                  return !w || w.length < 3 && !/^[A-Z0-9]/.test(w);
                }) ||
                SW[seg[0].toLowerCase()] ||
                SW[seg[n - 1].toLowerCase()] ||
                (3 === n && SW[seg[1].toLowerCase()] && !/^(of|and|for|to)$/i.test(seg[1]))
              )
                continue;
              if (2 === n && SW[seg[1].toLowerCase()]) continue;
              var k = seg.map(key).join(" ");
              out[k] || (out[k] = seg.join(" "));
            }
        });
      return out;
    }
    var per = [];
    for (var q = 1; q <= 7; q++) {
      var txt = [A[q - 1] || ""].concat(
          M.filter(function (r) {
            return Array.isArray(r) && r[0] === q && String(r[3] || "").trim();
          }).map(function (r) {
            return r[3];
          }),
        ),
        cnt = {},
        surf = {};
      txt.forEach(function (t) {
        var g = grams(t);
        Object.keys(g).forEach(function (k) {
          cnt[k] = (cnt[k] || 0) + 1;
          surf[k] || (surf[k] = g[k]);
        });
      });
      per.push({ q: q, cnt: cnt, surf: surf, has: !!String(A[q - 1] || "").trim(), n: txt.length - 1 });
    }
    var inQ = {};
    per.forEach(function (P) {
      Object.keys(P.cnt).forEach(function (k) {
        (inQ[k] = inQ[k] || []).push(P.q);
      });
    });
    var goalG = grams(D.goal || ""),
      nq = per.filter(function (P) {
        return P.has || P.n;
      }).length,
      wide = Object.keys(inQ)
        .filter(function (k) {
          return nq >= 4 && inQ[k].length >= Math.max(4, nq - 2) && !/^\d+ /.test(k);
        })
        .sort(function (a, b) {
          return inQ[b].length - inQ[a].length || (a < b ? -1 : 1);
        })
        .slice(0, 3),
      wideS = {};
    wide.forEach(function (k) {
      wideS[k] = 1;
      per.some(function (P) {
        return P.surf[k] && (wideS[k] = P.surf[k]);
      });
    });
    function top(P) {
      var ks = Object.keys(P.cnt).filter(function (k) {
        return !/^\d+ /.test(k) && !wideS[k];
      });
      /* what sets this question apart: used often here, shared with few others */
      var sc = function (k) {
        return P.cnt[k] * 2 + (inQ[k].length > 1 && inQ[k].length <= 3 ? 1.5 : 0) - (inQ[k].length > 3 ? 1 : 0) + (goalG[k] ? 1 : 0) + (k.split(" ").length > 2 ? 0.3 : 0);
      };
      ks.sort(function (a, b) {
        return sc(b) - sc(a) || (a < b ? -1 : 1);
      });
      var out = [];
      ks.forEach(function (k) {
        if (out.length >= 3) return;
        if (1 === P.cnt[k] && 1 === inQ[k].length && !goalG[k] && out.length >= 2) return;
        if (
          out.some(function (o) {
            var ow = o.split(" ");
            return (
              o.indexOf(k) >= 0 ||
              k.indexOf(o) >= 0 ||
              k.split(" ").filter(function (w) {
                return ow.indexOf(w) >= 0;
              }).length >= 2
            );
          })
        )
          return;
        out.push(k);
      });
      return out;
    }
    var col = function (P) {
      var ks = P.has || P.n ? top(P) : [];
      return (
        '<div class="ows' +
        (P.q >= 5 ? " owd" : "") +
        '"><div class="owh"><b>Q.' +
        P.q +
        "</b><span>" +
        LAB[P.q - 1] +
        "</span></div>" +
        (ks.length
          ? ks
              .map(function (k) {
                var o = inQ[k].filter(function (x) {
                  return x !== P.q;
                });
                return (
                  '<div class="owp">“' +
                  esc(P.surf[k]) +
                  "”" +
                  (o.length || goalG[k]
                    ? '<span class="owx">also ' +
                      (goalG[k] ? "the goal" + (o.length ? ", " : "") : "") +
                      o
                        .map(function (x) {
                          return "Q." + x;
                        })
                        .join(", ") +
                      "</span>"
                    : "") +
                  "</div>"
                );
              })
              .join("")
          : '<div class="owe">' + (P.has || P.n ? "No phrase repeats or stands out yet." : "Not answered yet.") + "</div>") +
        "</div>"
      );
    };
    return (
      (wide.length
        ? '<div class="owrun"><b>RUNS THROUGH NEARLY EVERY ANSWER</b> ' +
          wide
            .map(function (k) {
              return "\u201c" + esc(wideS[k]) + "\u201d";
            })
            .join(", ") +
          "</div>"
        : "") +
      '<div class="owstrip"><div class="owg"><div class="owgl">THE CONTEXT YOU HAVE GRASPED</div><div class="owc">' +
      per.slice(0, 4).map(col).join("") +
      '</div></div><div class="owg owgd"><div class="owgl">WHAT YOU WOULD DESIGN</div><div class="owc">' +
      per.slice(4).map(col).join("") +
      '</div></div></div><div class="ownote">Under each question: the phrases that set its answer and notes apart, and where else they appear. Phrases only; a single word is never a theme here.</div>'
    );
  }
  window.gsmOwnStrip = gsmOwnStrip;
'''
rep('''  var EDQ = [''', FN + '''  var EDQ = [''')
rep('''              '<details class="more"><summary>Your own words, in the order the method asks for them</summary><p>''',
    '''              '<details class="more owm"><summary>Your own words, in the order the method asks for them</summary>' +
              gsmOwnStrip() +
              '<details class="more"><summary>Read them in full</summary><p>''')
rep('''              sec("NOT YET ANSWERED", h7) +
              "</details></div></details>"''', '''              sec("NOT YET ANSWERED", h7) +
              "</details></details></div></details>"''')
rep('''"#gsm .emodef{''', '''"#gsm .owstrip{display:flex;gap:10px;margin:10px 0 6px;overflow-x:auto;padding-bottom:4px}#gsm details.more.owm{text-decoration:none;color:#222}#gsm details.more.owm>summary{color:#7a1d12;text-decoration:underline}#gsm .owg{flex:none}#gsm .owgd{border-left:2px solid #222;padding-left:10px}#gsm .owgl{font-size:10.5px;letter-spacing:.14em;font-weight:700;color:#444;margin-bottom:6px}#gsm .owc{display:flex;gap:5px}#gsm .ows{flex:0 0 76px;border-top:3px solid #222;padding-top:5px}#gsm .ows.owd{border-top-color:#2a9d8f}#gsm .owh b{display:block;font-size:13px}#gsm .owh span{display:block;font-size:11px;color:#666;line-height:1.3;margin-bottom:5px}#gsm .owp{font-size:12px;line-height:1.35;margin:0 0 6px;color:#111}#gsm .owx{display:block;font-size:10.5px;color:#888;margin-top:1px}#gsm .owe{font-size:11.5px;color:#999;font-style:italic}#gsm .owrun{font-size:13px;margin:10px 0 2px}#gsm .owrun b{font-size:10.5px;letter-spacing:.14em;color:#444;margin-right:6px}#gsm .owp{overflow-wrap:anywhere}#gsm .ownote{font-size:11.5px;color:#777;margin:2px 0 8px}@media(max-width:620px){#gsm .owstrip{flex-direction:column}#gsm .owgd{border-left:0;padding-left:0;border-top:2px solid #222;padding-top:6px}#gsm .owc{overflow-x:auto}#gsm .ows{flex-basis:67px}#gsm .owp{font-size:11.5px}}#gsm .emodef{''')
rep('t && (t.textContent = "v234");', 't && (t.textContent = "v235");')
open(P, "w").write(s)
print("ok")
