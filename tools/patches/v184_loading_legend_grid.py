"""v184: maps load once, without the old flat chart or the blurry canvas showing first; a legend stays with
every strategy card's map (also while parked); program cards show none."""
import sys
P = sys.argv[1]
s = open(P).read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:80]); s = s.replace(a, b)

# 1) before a card's map mounts, show a quiet placeholder, not the old flat chart; the chart returns only if the map fails
rep("#gsm .copy a{color:#555}", "#gsm .copy a{color:#555}#gsm .gterr-card:not(.gterr):not([data-fail]) .cpath{visibility:hidden}#gsm .gterr-card:not(.gterr):not([data-fail]){position:relative;min-height:260px}#gsm .gterr-card:not(.gterr):not([data-fail])::before{content:'Building the land\\2026';position:absolute;left:0;right:0;top:110px;text-align:center;color:#999;font-size:13px}")
rep("""          h.innerHTML = fb;""", """          h.innerHTML = fb;
          h.setAttribute("data-fail", "1");""")

# 2) the canvas map stays hidden while the 3D model loads; it shows only if 3D cannot be drawn
rep("""    (function () {
      var stg = $("stage"),
        box = document.createElement("div");
      stg.parentNode.insertBefore(box, stg);
      var snapImg = null;""", """    (function () {
      var stg = $("stage"),
        box = document.createElement("div");
      stg.parentNode.insertBefore(box, stg);
      var snapImg = null,
        wait = document.createElement("div");
      wait.className = "gtwait";
      wait.style.cssText = "text-align:center;color:#999;font-size:13px;padding:110px 0;border:1px solid #e4e4e4";
      wait.textContent = "Building the land\\u2026";
      stg.style.display = "none";
      stg.parentNode.insertBefore(wait, stg);
      function fallBack() {
        wait.remove();
        host._rel || (stg.style.display = "");
        try {
          resize();
          render();
        } catch (e) {}
      }""")
rep("""            if (!host.isConnected || host._rel) return;
            var c = document.createElement("canvas");
            if (!(c.getContext("webgl2") || c.getContext("webgl"))) return;""", """            if (!host.isConnected || host._rel) return;
            var c = document.createElement("canvas");
            if (!(c.getContext("webgl2") || c.getContext("webgl"))) return fallBack();""")
rep("""            } catch (e) {
              box.innerHTML = "";
              host._rel = null;
              if (window.console) console.warn("relief", e);
              return;
            }
            stg.style.display = "none";""", """            } catch (e) {
              box.innerHTML = "";
              host._rel = null;
              if (window.console) console.warn("relief", e);
              return fallBack();
            }
            wait.remove();
            stg.style.display = "none";
            /* legend: kept outside the 3D box on strategy cards, so it stays while the map is parked; none on programs */
            (function () {
              var lg = box.querySelector(".grleg");
              if (!lg || !CARDH) return;
              var cm = CARDS && null != COURSE && CARDS[COURSE] ? CARDS[COURSE].mode : "";
              lg.style.display = "none";
              if ("PROGRAM" === cm) return;
              host._legKeep && host._legKeep.remove();
              host._legKeep = lg.cloneNode(!0);
              host._legKeep.style.display = "";
              box.parentNode.insertBefore(host._legKeep, box.nextSibling);
            })();""")
rep("""          .catch(function () {});
      }
      function park() {""", """          .catch(function () {
            fallBack();
          });
      }
      function park() {""")
a = s.index("                  function gsmGrid() {")
b = s.index("                  var st = function (t) {", a)
NEW = r'''                  function gsmGrid() {
                    var M = (window.gsmData ? window.gsmData().m || [] : [])
                        .map(function (r, i) {
                          return { r: r, id: "N" + (i + 1), k: i + 1, t: Ht(r[3] || "") };
                        })
                        .filter(function (o) {
                          return String(o.r[3] || "").trim();
                        });
                    if (M.filter(function (o) {
                        return o.r[0] >= 5;
                      }).length < 2) return "";
                    var HARD = [3, 0, 2, 1, 4],
                      MED = window.gsmMED || {},
                      pts = M.map(function (o) {
                        var e = o.r[5],
                          d = (null == e ? 2 : HARD[e]) + (o.r[2] >= 118 ? 1 : 0),
                          emo = {},
                          shared = 0;
                        M.forEach(function (p) {
                          if (p === o) return;
                          var hit = Object.keys(o.t.k).some(function (k) {
                            return !MED[k] && p.t.k[k];
                          });
                          hit && (shared++, null != p.r[5] && (emo[p.r[5]] = 1));
                        });
                        return { id: o.id, k: o.k, q: o.r[0], act: o.r[0] >= 5, d: d / 5, reach: Object.keys(emo).length, shared: shared, e: e };
                      }),
                      mr = Math.max.apply(null, pts.map(function (p) { return p.reach; }).concat([1])),
                      ms = Math.max.apply(null, pts.map(function (p) { return p.shared; }).concat([1]));
                    pts.forEach(function (p) {
                      p.any = p.reach / mr;
                    });
                    window.gsmGridPts = pts.filter(function (p) {
                      return p.act;
                    });
                    var W = 620,
                      H = 440,
                      L = 60,
                      R = W - 60,
                      T = 44,
                      B = H - 44,
                      cx = (L + R) / 2,
                      cy = (T + B) / 2,
                      col = ["#c8352e", "#2a9d8f", "#a48fd0", "#e6be4f", "#1b2a8f"],
                      used = {},
                      jit = function (k) {
                        return ((k * 2654435761) % 1000) / 1000 - 0.5;
                      },
                      quad =
                        '<rect x="' + L + '" y="' + T + '" width="' + (cx - L) + '" height="' + (cy - T) + '" fill="#f4f8f6"/>' +
                        '<rect x="' + cx + '" y="' + T + '" width="' + (R - cx) + '" height="' + (cy - T) + '" fill="#fbf3f2"/>' +
                        '<rect x="' + L + '" y="' + cy + '" width="' + (cx - L) + '" height="' + (B - cy) + '" fill="#eef6f3"/>' +
                        '<rect x="' + cx + '" y="' + cy + '" width="' + (R - cx) + '" height="' + (B - cy) + '" fill="#f7f3fa"/>' +
                        '<g font-family="Questrial,Helvetica,Arial,sans-serif" font-size="11" fill="#777" letter-spacing=".08em">' +
                        '<text x="' + (L + 8) + '" y="' + (T + 16) + '">FIRST STEPS, LOCALLY</text>' +
                        '<text x="' + (R - 8) + '" y="' + (T + 16) + '" text-anchor="end">ONLY WHERE IT BLOCKS</text>' +
                        '<text x="' + (L + 8) + '" y="' + (B - 8) + '">START HERE: THEY TRAVEL</text>' +
                        '<text x="' + (R - 8) + '" y="' + (B - 8) + '" text-anchor="end">WORTH IT ONCE MOVING</text></g>',
                      dots = pts
                        .slice()
                        .sort(function (a, b) {
                          return a.act - b.act;
                        })
                        .map(function (p) {
                          var x = L + 14 + p.d * (R - L - 28) + jit(p.k) * 26,
                            y = T + 24 + p.any * (B - T - 48) + jit(p.k * 7) * 18,
                            kk = Math.round(x / 16) + "," + Math.round(y / 16);
                          while (used[kk]) {
                            x += 14;
                            kk = Math.round(x / 16) + "," + Math.round(y / 16);
                          }
                          used[kk] = 1;
                          var r = p.act ? 7 + 5 * (p.shared / ms) : 5 + 3 * (p.shared / ms),
                            c = null == p.e ? "#888" : col[p.e];
                          return (
                            '<g class="gdot"><circle data-ref="note ' + p.k + '" cx="' + x.toFixed(1) + '" cy="' + y.toFixed(1) + '" r="' + r.toFixed(1) +
                            '" fill="' + (p.act ? c : "#fff") + '" stroke="' + (p.act ? "#111" : c) + '" stroke-width="' + (p.act ? 1.4 : 2.6) +
                            '" style="cursor:help"><title>' + p.id + " · Q." + p.q + "</title></circle>" +
                            '<text x="' + (x + r + 3).toFixed(1) + '" y="' + (y + 4).toFixed(1) + '" font-size="' + (p.act ? 12.5 : 10.5) +
                            '" font-weight="' + (p.act ? 700 : 400) + '" font-family="Questrial,Helvetica,Arial,sans-serif" fill="' + (p.act ? "#111" : "#666") + '" pointer-events="none">' + p.id + "</text></g>"
                          );
                        })
                        .join(""),
                      svg =
                        '<svg viewBox="0 0 ' + W + " " + H + '" style="display:block;width:100%;max-width:660px;height:auto;margin:6px auto;background:#fff" role="img" aria-label="Actions by ease and reach">' +
                        quad +
                        '<line x1="' + cx + '" y1="' + T + '" x2="' + cx + '" y2="' + B + '" stroke="#111" stroke-width="1.2"/>' +
                        '<line x1="' + L + '" y1="' + cy + '" x2="' + R + '" y2="' + cy + '" stroke="#111" stroke-width="1.2"/>' +
                        '<g font-family="Questrial,Helvetica,Arial,sans-serif" font-size="16" fill="#111" text-anchor="middle">' +
                        '<text x="' + cx + '" y="' + (T - 14) + '">Act Here</text><text x="' + cx + '" y="' + (B + 28) + '">Act Anywhere</text>' +
                        '<text x="' + (L - 6) + '" y="' + (cy + 5) + '" text-anchor="end" font-size="14">Easy</text><text x="' + (R + 6) + '" y="' + (cy + 5) + '" text-anchor="start" font-size="14">Difficult</text></g>' +
                        dots +
                        "</svg>",
                      A = pts.filter(function (p) {
                        return p.act;
                      }),
                      q4 = function (f) {
                        return A.filter(f).map(function (p) {
                          return p.id;
                        });
                      },
                      li = function (a) {
                        return a.length > 1 ? a.slice(0, -1).join(", ") + " and " + a[a.length - 1] : a[0];
                      },
                      ea = q4(function (p) { return p.d < 0.5 && p.any >= 0.5; }),
                      eh = q4(function (p) { return p.d < 0.5 && p.any < 0.5; }),
                      da = q4(function (p) { return p.d >= 0.5 && p.any >= 0.5; }),
                      dh = q4(function (p) { return p.d >= 0.5 && p.any < 0.5; }),
                      others = pts.filter(function (p) { return !p.act && p.d < 0.5 && p.any >= 0.5; }).map(function (p) { return p.id; }),
                      tx = [];
                    ea.length && tx.push("<b>Easy, and they act anywhere:</b> " + li(ea) + ". Little energy, and their words run through notes in many emotions, so they travel. Start here.");
                    eh.length && tx.push("<b>Easy, but they act here:</b> " + li(eh) + ". Cheap to take, but tied to one kind of ground. Good first steps in that place, not everywhere.");
                    da.length && tx.push("<b>Difficult, but they act anywhere:</b> " + li(da) + ". They cost energy, yet what they touch runs through the whole workbook. Worth the effort once something is moving.");
                    dh.length && tx.push("<b>Difficult, and they act here:</b> " + li(dh) + ". Costly and local. Take them only where that ground is what stands between you and the goal, and watch them closely.");
                    others.length &&
                      tx.push("<b>Not yet actions, but easy and far-reaching:</b> " + li(others.slice(0, 6)) + (others.length > 6 ? " and more" : "") + ". These notes sit where acting would be cheap and would travel. Nothing you would do is placed on them yet; each is a candidate for a Q.5–Q.7 note.");
                    return (
                      '<div class="intl"><b>Actions by ease and reach.</b> Every note on your map, placed by how hard it would be to act on it (left to right: the emotion it sits in, and whether it is above or below the line) and how far acting on it would reach (top to bottom: from here, where its words meet notes in few emotions, to anywhere, where they run through many). <b>Filled dots</b> are things you would do (Q.5–Q.7); <b>rings</b> are every other note. Bigger dots share words with more notes. Colors are the emotions. Hover or tap a dot to read its note.</div>' +
                      svg +
                      '<div class="intl">' + tx.join("<br>") + "</div>"
                    );
                  }
'''
s = s[:a] + NEW + s[b:]
rep('t && (t.textContent = "v183");', 't && (t.textContent = "v184");')
open(P, "w").write(s); print("v184 ok")
