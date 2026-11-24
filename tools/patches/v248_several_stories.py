"""v248: Pattern Analysis, several stories (the Several Systems capability, first on Analysis).

Finds the separate low grounds on a line map from what the workbook already holds
(each note's place, side, and emotion, with the same height rule the terrain uses),
and when there is more than one, YOUR STORY SO FAR opens with one story for each
(cap 3): what holds it, what helps, and where it can cross. The one-line story is kept,
folded under it. A workbook with one structure, a place map, or fewer than 12 placed
notes is unchanged.
"""
import re, sys
F = "gsm-readable.js"
s = open(F).read()

JS = r'''
  /* v248: several systems. The low grounds are found the way the terrain makes them:
     height = acceptance - (1.5 x aggression + distrust + 3.4 x defiance), smoothed by each
     note's reach; hollows that meet at a shallow saddle are one hollow. Line maps only. */
  function gsmSystems() {
    var pts = [],
      E = GSMEMO;
    (C.m || []).forEach(function (t, i) {
      if (!t || !String(t[3] || "").trim() || "number" != typeof t[1] || "number" != typeof t[2]) return;
      pts.push({
        x: t[1],
        y: t[2],
        e: "number" == typeof t[5] && t[5] >= 0 && t[5] < 5 ? t[5] : null,
        em: "number" == typeof t[5] && t[5] >= 0 && t[5] < 5 ? t[5] : null,
        side: t[2] < 118 ? 1 : t[2] > 118 ? -1 : 0,
        ref: "note " + (i + 1),
        lab: "N" + (i + 1),
        txt: t[3],
        k: t[0],
      });
    });
    var res = { low: [], high: [], pts: pts };
    var ep = pts.filter(function (p) {
      return null != p.e;
    });
    if (pts.length < 12 || ep.length < 8) return res;
    var CX = 4,
      VX = 86,
      VY = 58,
      n = VX * VY,
      sig = 22;
    var nn = ep
      .map(function (p) {
        var m = 1e9;
        ep.forEach(function (q) {
          q !== p && (m = Math.min(m, Math.hypot(p.x - q.x, p.y - q.y)));
        });
        return m;
      })
      .sort(function (a, b) {
        return a - b;
      });
    sig = Math.max(13, Math.min(30, 0.9 * nn[Math.floor(nn.length / 2)]));
    var H = new Float32Array(n),
      s2 = 2 * sig * sig,
      cut = 16 * sig * sig,
      hmin = 1e9,
      hmax = -1e9;
    for (var j = 0; j < VY; j++)
      for (var i = 0; i < VX; i++) {
        var x = i * CX,
          y = j * CX,
          w = [0, 0, 0, 0, 0];
        ep.forEach(function (p) {
          var d2 = (x - p.x) * (x - p.x) + (y - p.y) * (y - p.y);
          d2 < cut && (w[p.e] += Math.exp(-d2 / s2));
        });
        var h = w[1] - (1.5 * w[0] + w[2] + 3.4 * w[4]);
        H[j * VX + i] = h;
        h < hmin && (hmin = h);
        h > hmax && (hmax = h);
      }
    var span = Math.max(1e-6, hmax - hmin);
    function cellOf(p) {
      var ci = Math.max(0, Math.min(VX - 1, Math.round(p.x / CX))),
        cj = Math.max(0, Math.min(VY - 1, Math.round(p.y / CX)));
      return cj * VX + ci;
    }
    /* merge-by-depth watershed: a hollow shallower than 12% of the map's height at its
       saddle joins its neighbor */
    function sheds(sign) {
      var ord = [],
        par = new Int32Array(n).fill(-1),
        floor = {};
      for (var q = 0; q < n; q++) ord.push(q);
      ord.sort(function (a, b) {
        return sign * H[a] - sign * H[b];
      });
      function find(a) {
        while (par[a] !== a) (par[a] = par[par[a]]), (a = par[a]);
        return a;
      }
      ord.forEach(function (c) {
        var ci = c % VX,
          cj = (c / VX) | 0,
          roots = [];
        for (var dj = -1; dj <= 1; dj++)
          for (var di = -1; di <= 1; di++) {
            if (!di && !dj) continue;
            var ni = ci + di,
              nj = cj + dj;
            if (ni < 0 || nj < 0 || ni >= VX || nj >= VY) continue;
            var u = nj * VX + ni;
            if (par[u] < 0) continue;
            var r = find(u);
            roots.indexOf(r) < 0 && roots.push(r);
          }
        if (!roots.length) {
          par[c] = c;
          floor[c] = sign * H[c];
          return;
        }
        roots.sort(function (a, b) {
          return floor[a] - floor[b];
        });
        var lv = sign * H[c],
          keep = roots[0];
        par[c] = keep;
        roots.slice(1).forEach(function (r) {
          if (lv - floor[r] < 0.12 * span) par[r] = keep;
        });
      });
      return find;
    }
    function groups(sign, ok) {
      var find = sheds(sign),
        G = {};
      pts.forEach(function (p) {
        if (!ok(p)) return;
        var r = find(cellOf(p));
        (G[r] = G[r] || []).push(p);
      });
      return Object.keys(G)
        .map(function (r) {
          var L = G[r],
            cx = 0,
            cy = 0;
          L.forEach(function (p) {
            cx += p.x;
            cy += p.y;
          });
          return { n: L, x: cx / L.length, y: cy / L.length, depth: sign * H[+r] };
        })
        .filter(function (g) {
          return g.n.length >= 3;
        });
    }
    res.low = groups(1, function (p) {
      return 3 !== p.e && (p.side < 0 || (null != p.e && [0, 2, 4].indexOf(p.e) >= 0 && p.side <= 0));
    })
      .filter(function (g) {
        var lowE = g.n.filter(function (p) {
          return [0, 2, 4].indexOf(p.e) >= 0;
        }).length;
        return g.y > 118 && lowE >= 2 && g.depth < -0.15 * span;
      })
      .sort(function (a, b) {
        return b.n.length - a.n.length || a.depth - b.depth;
      });
    res.high = groups(-1, function (p) {
      return p.side > 0;
    }).sort(function (a, b) {
      return b.n.length - a.n.length;
    });
    var tot = res.low.reduce(function (a, g) {
      return a + g.n.length;
    }, 0);
    res.several = res.low.length >= 2 && res.low[0].n.length < 0.75 * tot && res.low[1].n.length >= 3;
    return res;
  }
  window.gsmSystems = gsmSystems;
  function gsmStories(mt) {
    if (!mt || mt.querySelector(".stories")) return;
    var Y = gsmSystems();
    window.gsmSys = Y;
    if (!Y.several) return;
    var E = GSMEMO,
      ST = Y.low.slice(0, 3),
      ind = Y.pts.filter(function (p) {
        return 3 === p.e;
      }),
      usedInd = {},
      usedHelp = {};
    function where(g) {
      return g.x < 115 ? "start" : g.x > 225 ? "goal" : "mid";
    }
    function lowEm(g) {
      return gsmStEm(
        g.n.filter(function (p) {
          return [0, 2, 4].indexOf(p.e) >= 0;
        }),
      ).o;
    }
    var GW = { 0: "the lower ground of aggression", 2: "the low ground of distrust", 4: "defiance, the lowest ground" };
    function dsq(a, b) {
      return Math.hypot(a.x - b.x, a.y - b.y);
    }
    function segD(p, a, b) {
      var vx = b.x - a.x,
        vy = b.y - a.y,
        L = vx * vx + vy * vy || 1,
        t = Math.max(0, Math.min(1, ((p.x - a.x) * vx + (p.y - a.y) * vy) / L));
      return Math.hypot(p.x - a.x - t * vx, p.y - a.y - t * vy);
    }
    function pickHold(g) {
      var R = { 4: 5, 0: 4, 2: 3, 3: 1, 1: 2 };
      return g.n
        .slice()
        .sort(function (a, b) {
          return (
            (b.txt.split(/\s+/).length >= 4) - (a.txt.split(/\s+/).length >= 4) ||
            (R[b.e] || 0) - (R[a.e] || 0) ||
            dsq(a, g) - dsq(b, g)
          );
        })
        .slice(0, 2);
    }
    var seenWhere = {},
      out = [];
    ST.forEach(function (g, k) {
      var wh = where(g),
        o = lowEm(g),
        acc = g.n.filter(function (p) {
          return 1 === p.e;
        }),
        hc = Y.high
          .slice()
          .sort(function (a, b) {
            return dsq(a, g) - dsq(b, g);
          })[0],
        help = hc
          ? hc.n
              .filter(function (p) {
                return (1 === p.e || null == p.e) && !usedHelp[p.ref];
              })
              .sort(function (a, b) {
                return dsq(a, g) - dsq(b, g);
              })
              .slice(0, 2)
          : [],
        tgt = hc || { x: g.x, y: 60 },
        cr = ind
          .filter(function (p) {
            return !usedInd[p.ref] && segD(p, g, tgt) < 40;
          })
          .sort(function (a, b) {
            return dsq(a, g) - dsq(b, g);
          })
          .slice(0, 3)
          .sort(function (a, b) {
            return +a.lab.slice(1) - +b.lab.slice(1);
          });
      cr.forEach(function (p) {
        usedInd[p.ref] = 1;
      });
      help.forEach(function (p) {
        usedHelp[p.ref] = 1;
      });
      var em2 = o.length > 1 && gsmStEm(g.n).c[o[1]] * 2 >= gsmStEm(g.n).c[o[0]];
      /* the verse: where it is, how deep, what sits inside, how it gets out */
      var V = [];
      V.push(
        "start" === wh
          ? seenWhere.start
            ? "Here at the start, a second hollow:"
            : "Here, at the start,"
          : "goal" === wh
            ? "Close to the goal,"
            : "Halfway to the goal,",
      );
      seenWhere[wh] = 1;
      V.push(
        (4 === o[0]
          ? "the ground drops to defiance"
          : 0 === o[0]
            ? "the ground falls into aggression"
            : "the ground sinks into distrust") +
          (em2 ? " and " + E[o[1]] : "") +
          ",",
      );
      acc.length
        ? V.push("and acceptance of what holds it sits down here too,")
        : "goal" === wh
          ? V.push("just where the work could look finished,")
          : V.push(help.length ? "below the help that stands across the line," : "with nothing yet across the line from it,");
      V.push(cr.length ? "and a ridge of indifference runs out of it." : "and no ridge leads out, only a climb.");
      /* the prose: what holds it, what helps, where it can cross */
      var hold = pickHold(g),
        P = [];
      P.push(
        "<b>What holds it:</b> " +
          gsmMeanList(
            hold.map(function (p) {
              return gsmStQ(p);
            }),
          ) +
          ". " +
          (g.n.length > hold.length ? g.n.length + " notes sit in this hollow, most of them on " + GW[o[0]] + "." : "") +
          (acc.length
            ? " " +
              gsmMeanList(acc.map(gsmStRef)) +
              (acc.length > 1 ? " carry" : " carries") +
              " acceptance here, acceptance of what holds the goal back: it keeps this hollow in place, not open."
            : "") +
          ("goal" === wh ? " Because it lies close to the goal, it can take hold after the change seems done." : ""),
      );
      P.push(
        "<b>What helps:</b> " +
          (help.length
            ? gsmMeanList(
                help.map(function (p) {
                  return gsmStQ(p);
                }),
              ) + ", the nearest higher ground across the line."
            : "nothing yet stands on the side that helps near this hollow."),
      );
      P.push(
        "<b>Where it can cross:</b> " +
          (cr.length
            ? gsmMeanList(cr.map(gsmStRef)) +
              (cr.length > 1 ? " carry" : " carries") +
              " indifference between this hollow and that help, the ridge most crossings go through."
            : "no indifference lies between this hollow and the help, so getting across is a climb over bare rock, and it takes the most energy."),
      );
      out.push(
        '<div class="story1"><div class="s1h">STORY ' +
          (k + 1) +
          '</div><div class="s1v">' +
          V.map(Gt).join("<br>") +
          '</div><div class="s1p">' +
          P.join("<br>") +
          '</div><details class="more"><summary>The notes in this hollow</summary><div class="srev">' +
          g.n
            .map(function (p) {
              return "<div>" + gsmStRef(p) + " <i>" + (null != p.em ? E[p.em] : "no emotion marked") + "</i>: " + gsmStQ(p).replace(/ \(<a[^)]*<\/a>\)$/, "") + "</div>";
            })
            .join("") +
          "</div></details></div>",
      );
    });
    var more = Y.low.length > 3 ? " These are the three largest; " + (Y.low.length - 3) + (Y.low.length - 3 > 1 ? " smaller hollows are" : " smaller hollow is") + " left out." : "";
    var box = document.createElement("div");
    box.className = "stories";
    box.innerHTML =
      '<p class="stsn">Your workbook holds ' +
      ["", "one story", "two stories", "three stories"][ST.length] +
      ". Each is its own low ground, held by its own notes, with its own way out. Read them apart before reading them as one." +
      more +
      "</p>" +
      out.join("");
    var rest = [].slice.call(mt.children).filter(function (c) {
        return !c.classList.contains("owm");
      }),
      fd = document.createElement("details");
    fd.className = "more onel";
    fd.innerHTML = "<summary>The whole workbook read as one story</summary>";
    rest.forEach(function (c) {
      fd.appendChild(c);
    });
    mt.prepend(fd);
    mt.prepend(box);
  }
'''

CSS = '#gsm .stories{margin:6px 0 10px}#gsm .stories .stsn{font-size:17.5px;line-height:1.6;color:#111}#gsm .story1{border-left:3px solid #111;padding:4px 0 6px 14px;margin:16px 0}#gsm .story1 .s1h{font-size:11px;font-weight:700;letter-spacing:.16em;color:#444;margin-bottom:6px}#gsm .story1 .s1v{font-size:18px;line-height:1.55;font-style:italic;color:#111;margin:0 0 10px}#gsm .story1 .s1p{font-size:15.5px;line-height:1.6;color:#222}#gsm .story1 .s1p b{font-weight:700;color:#111}#gsm details.onel{margin-top:14px}'

a = "  window.gsmStruct = gsmStruct;\n"
assert s.count(a) == 1
s = s.replace(a, a + JS, 1)

b = """        p1 ? (p1.after(h), h.after(p)) : (mt.prepend(p), mt.prepend(h));
      }
    }
"""
assert s.count(b) == 1
s = s.replace(b, b + """    try {
      gsmStories(fd.querySelector(".mtext"));
    } catch (e) {}
""", 1)

c = '#gsm .stn{color:#888;font-size:13px}";'
assert s.count(c) == 1
s = s.replace(c, '#gsm .stn{color:#888;font-size:13px}' + CSS + '";', 1)

d = 't.textContent = "v247"'
assert s.count(d) == 1
s = s.replace(d, 't.textContent = "v248"', 1)
open(F, "w").write(s)
print("v248 applied")
