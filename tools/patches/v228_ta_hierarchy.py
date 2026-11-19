"""v228: Taking Action in three layers (his 11-18 21:37 "do it" on the hierarchy review).
Nothing is removed; sections are reordered and opened on demand.
Page:
- THE CHEAPEST FIRST MOVE leads THE TEST, in larger type; the old "Where to start" note joins it as "Carries furthest".
- THE TEST: each line keeps its verdict; the notes behind it are small and gray. Split readings: a one-line summary
  of the kinds found, each split and its cards under it (closed). Constraints named: a summary, the texts under it.
- DOES THIS ANSWER IT? moves right under THE TEST. NOTHING YOU WOULD DO ANSWERS THESE YET folds (the audit trail).
- The opening note is set small; each group's long explanation moves behind "Why a strategy?" / "Why a program?".
Each card:
- Layer 1, a decision strip: MEETS THE TEST (verdict + short phrase), FIRST MOVE, THE WAY ACROSS (one line),
  READING SPLITS (one line, when there are any).
- Layer 2, "Why this action" (closed, except on the card named in the cheapest first move): in service of the goal,
  strategy or program with the switch, why, the full test, THE WAY ACROSS, WHERE THE READING SPLITS, FIRST MOVES or
  THE SEQUENCE, THE WAY THROUGH IT (3D and chart), WHAT HOLDS IT IN THE LOW GROUND.
- Layer 3, "Evidence" (closed): the note lists, what this rests on, the Morin line.
- Empty constraint boxes collapse to "Name what holds it"; written ones always show. YOUR DECISION and WHAT YOU DID
  stay visible at the foot.
- Type tiers: the strip in black with a heavy rule; the rest normal; evidence gray.
Usage: python3 v228_ta_hierarchy.py gsm-readable.js"""
import sys
P = sys.argv[1]
s = open(P).read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:90]); s = s.replace(a, b)

# ---- builder: short forms for the strip
rep('''            function ME(x) {''', '''            function NL(x) {
              var n = String(x.id).replace(/\\D/g, "");
              return Gt(NM(x)) + ' <span class="stn">' + (/^P/.test(x.id) ? "P" : "N") + n + "</span>";
            }
            function NLS(xs, k) {
              k = k || 3;
              var b = xs.slice(0, k).map(NL);
              xs.length > k && b.push(xs.length - k + " more");
              return phList(b);
            }
            function ME(x) {''')
rep('''              return { h: h, met: met, not: not, v: not.length ? (met.length ? "partly" : "not yet") : "yes" };''', '''              return {
                h: h,
                met: met,
                not: not,
                v: not.length ? (met.length ? "partly" : "not yet") : "yes",
                s: not.length ? (help ? "Not yet built on: " : "Not yet answered: ") + NLS(not) + "." : help ? "Built on." : "Answered.",
              };''')
rep('''              return { h: out.join(" "), ids: ids, e0: ems[0], s0: s0, rg: rg };''', '''              var st0 = Math.abs(RK[ems[0]] - 2),
                sh = rg
                  ? E[ems[0]] + " (" + NL(s0) + ") \\u2192 the ridge at " + NL(rg) + " \\u2192 acceptance" + (tg ? " at " + NL(tg) : "") + " \\u00b7 " + COST(st0 + 1) + " cost"
                  : E[ems[0]] + " \\u2192 acceptance: a climb over bare rock \\u00b7 high cost";
              ems.length > 1 && 4 === ems[ems.length - 1] && 4 !== ems[0] && (sh += "; defiance last");
              return { h: out.join(" "), ids: ids, e0: ems[0], s0: s0, rg: rg, s: sh };''')
rep('''              return { h: h, ids: xs.slice(0, 6).concat(ie.slice(0, 1)) };''', '''              return { h: h, ids: xs.slice(0, 6).concat(ie.slice(0, 1)), s: "already on the high ground \\u00b7 low cost" + (ie.length ? "; bring in " + NL(ie[0]) + " before it tips" : "") };''')
rep('''                '<div class="coa" data-seed="' +
                  o.seed +''', '''                '<div class="coa" data-seed="' +
                  o.seed +
                  '" data-tv="' +
                  (o.test ? o.test.v : "") +
                  '" data-ts="' +
                  Gt(o.test ? o.test.s : "") +
                  '" data-ws="' +
                  Gt(o.way && o.way.s ? o.way.s : "") +''')
# THE TEST: first move on top, quieter notes, constraint summary
rep('''                  return "<div><i>" + r.lab + "</i> " + VL(r.t) + " " + (r.t.not.length ? "Not yet answered: " + LS(r.t.not, 3) + "." : "Answered.") + "</div>";''', '''                  return "<div><i>" + r.lab + "</i> " + VL(r.t) + ' <span class="tev">' + (r.t.not.length ? "Not yet answered: " + LS(r.t.not, 3) + "." : "Answered.") + "</span></div>";''')
rep('''                  return "<div><i>" + r.lab + "</i> " + VL(r.t) + " " + (r.t.not.length ? "Not yet built on: " + LS(r.t.not, 3) + "." : "Built on.") + "</div>";''', '''                  return "<div><i>" + r.lab + "</i> " + VL(r.t) + ' <span class="tev">' + (r.t.not.length ? "Not yet built on: " + LS(r.t.not, 3) + "." : "Built on.") + "</span></div>";''')
rep('''              first = (function () {''', '''              FT = "",
              first = (function () {''')
rep('''                  st = CARDS.filter(function (c) {
                    return c.S;
                  })[0];
                return pr && st''', '''                  st = CARDS.filter(function (c) {
                    return c.S;
                  })[0];
                FT = (pr || st || {}).title || "";
                return pr && st''')
rep('''              '<div class="tatst"><div class="tatq">THE TEST</div>''', '''              '<div class="tatst">' +
              (first ? '<div class="tafirst" data-ft="' + Gt(FT) + '"><div class="tatl">THE CHEAPEST FIRST MOVE</div><div class="tafm">' + first + "</div></div>" : "") +
              '<div class="tatq">THE TEST</div>''')
rep('''              (cons.length ? row("What holds it, as you named it", cons.join("")) : "") +
              (first ? row("The cheapest first move", "<div>" + first + "</div>") : "") +''', '''              (cons.length
                ? row(
                    "What holds it, as you named it",
                    "<div>" +
                      (1 === cons.length ? "One constraint named" : cons.length + " constraints named") +
                      "; " +
                      cons.filter(function (x) {
                        return x.indexOf("tav-yes") >= 0;
                      }).length +
                      " already in Q.4, Q.6, or Q.7.</div>" +
                      '<details class="more"><summary>The constraints</summary>' +
                      cons.join("") +
                      "</details>",
                  )
                : "") +''')

# ---- post-pass: short split lines, layered cards, page order
rep('''  function gsmTAPass(Rt, tries) {''', '''  function gsmTAShort(s) {
    var k = s.k || {},
      w = s.names || [],
      q = function (x) {
        return "\\u201c" + Gt(x) + "\\u201d";
      },
      TR = [3, 0, 2, 1, 4];
    if ("TWO PEOPLE, TWO SIDES" === s.lab) return "Two groups read " + q(w[0]) + " two ways.";
    if ("THE EMOTION CHANGES" === s.lab && k.emo) return q(w[0]) + (TR[k.emo[1]] < TR[k.emo[0]] ? " reads easier in your plans than on the ground." : " reads harder in your plans than on the ground.");
    if ("ONE IDEA UNDER TWO NAMES" === s.lab) return q(w[0]) + " and " + q(w[1] || "") + " act as one idea.";
    if ("PLACED ONE WAY, TIED THE OTHER" === s.lab) return Gt(String((k.notes || [])[0] || "").replace(/^(?:place )?note (\\d+)/, "N$1")) + "\\u2019s place and ties disagree.";
    return "";
  }
  document.addEventListener("click", function (ev) {
    var b = ev.target.closest && ev.target.closest("#gsm .tanb");
    if (!b) return;
    ev.preventDefault();
    var c = b.closest(".ccons");
    c && c.classList.remove("cempty");
    var t = c && c.querySelector("textarea");
    t && t.focus();
  });
  function gsmTALayer(c, open) {
    var bd = c.querySelector(".bd");
    if (!bd || bd.querySelector(":scope > .tastrip")) return;
    var lab = function (el) {
        var l = el.querySelector && el.querySelector(":scope > .csl");
        return l ? l.textContent.trim() : "";
      },
      dec = bd.querySelector(":scope > .dec"),
      act = bd.querySelector(":scope > .acted"),
      rank = function (el) {
        if (el === dec || el === act) return -1;
        var cl = el.classList,
          l = lab(el);
        return cl.contains("purp") ? 1 : cl.contains("coacall") ? 2 : cl.contains("why") ? 3 : cl.contains("tatest") ? 4 : cl.contains("taway") ? 5 : cl.contains("tasplit") ? 6 : /^(FIRST MOVES|THE SEQUENCE)$/.test(l) ? 7 : "THE WAY THROUGH IT" === l ? 8 : "WHAT HOLDS IT IN THE LOW GROUND" === l ? 9 : 0;
      },
      L2 = [],
      L3 = [];
    [].slice.call(bd.children).forEach(function (el) {
      var r = rank(el);
      r > 0 ? L2.push([r, el]) : 0 === r && L3.push(el);
    });
    L2.sort(function (x, y) {
      return x[0] - y[0];
    });
    var fmS = L2.filter(function (x) {
        return 7 === x[0];
      })[0],
      li = fmS && fmS[1].querySelector("li"),
      tv = c.getAttribute("data-tv"),
      ts = c.getAttribute("data-ts"),
      ws = c.getAttribute("data-ws"),
      h = "";
    tv && (h += '<div><span class="tsl">MEETS THE TEST</span> <span class="tav tav-' + tv.replace(" ", "") + '">' + Gt(tv.toUpperCase()) + "</span> " + (ts || "") + "</div>");
    li && (h += '<div><span class="tsl">FIRST MOVE</span> ' + li.innerHTML + "</div>");
    ws && (h += '<div><span class="tsl">THE WAY ACROSS</span> ' + ws + "</div>");
    (c._tsp || []).length && (h += '<div><span class="tsl">READING SPLITS</span> ' + c._tsp.join(" ") + "</div>");
    var sp = document.createElement("div");
    sp.className = "tastrip";
    sp.innerHTML = h;
    var w = document.createElement("details");
    w.className = "tawhy";
    open && (w.open = !0);
    w.innerHTML = "<summary>Why this action</summary>";
    L2.forEach(function (x) {
      w.appendChild(x[1]);
    });
    w.querySelectorAll(".ccons").forEach(function (cc) {
      var t = cc.querySelector("textarea");
      if (!t || t.value.trim() || cc.querySelector(".tanb")) return;
      cc.classList.add("cempty");
      var q = cc.querySelector(".cq"),
        b = document.createElement("button");
      b.type = "button";
      b.className = "lnk sm tanb";
      b.textContent = "Name what holds it";
      q ? q.parentNode.insertBefore(b, q.nextSibling) : cc.insertBefore(b, cc.firstChild);
    });
    bd.insertBefore(sp, bd.firstChild);
    h ? sp.parentNode.insertBefore(w, sp.nextSibling) : (sp.parentNode.removeChild(sp), bd.insertBefore(w, bd.firstChild));
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
  function gsmTAPass(Rt, tries) {''')
rep('''      if (!bd || !h) return;
      var d = document.createElement("div");''', '''      if (!bd || !h) return;
      c._tsp = perC[ci]
        .map(function (si) {
          return gsmTAShort(SP[si]);
        })
        .filter(Boolean);
      var d = document.createElement("div");''')
rep('''    sr &&
      SP.length &&
      (sr.outerHTML = SP.slice(0, 6)''', '''    var kinds = SP.map(function (sp) {
      return sp.lab;
    }).filter(function (x, i, a) {
      return a.indexOf(x) === i;
    });
    sr &&
      SP.length &&
      (sr.outerHTML =
        "<div>" +
        kinds
          .map(function (x) {
            return '<span class="tsk">' + x + "</span>";
          })
          .join(" \\u00b7 ") +
        '</div><details class="more"><summary>Each split, and the cards it lands on</summary>' +
        SP.slice(0, 6)''')
rep('''            (on.length ? ": carried onto " + gsmMeanList(on) + "." : ": no card takes it up yet. " + gsmTASay(sp)) +
            "</div>"
          );
        })
        .join(""));''', '''            (on.length ? ": carried onto " + gsmMeanList(on) + "." : ": no card takes it up yet. " + gsmTASay(sp)) +
            "</div>"
          );
        })
        .join("") +
        "</details>");''')
# group explanations behind a fold
rep('''      meta && d.appendChild(meta);
      ph.parentNode.insertBefore(d, ph);''', '''      if (meta) {
        var mf = document.createElement("details");
        mf.className = "more tameta";
        mf.innerHTML = "<summary>Why a " + ("STRATEGIES" === lab ? "strategy" : "program") + "?</summary>";
        mf.appendChild(meta);
        d.appendChild(mf);
      }
      ph.parentNode.insertBefore(d, ph);''')
rep('''    ph.parentNode.removeChild(ph);
    window.gsmTAV = (window.gsmTAV || 0) + 1;''', '''    ph.parentNode.removeChild(ph);
    // layers on every card; the card named in the cheapest first move opens
    var fe = Rt.querySelector(".tafirst"),
      ft = fe ? fe.getAttribute("data-ft") : "",
      opened = 0;
    cards.forEach(function (c) {
      var o = !!ft && ft === tl(c);
      o && opened++;
      gsmTALayer(c, o);
    });
    !opened && !ft && cards[0] && cards[0].querySelector(".tawhy") && !cards[0].closest("details.tamore") && (cards[0].querySelector(".tawhy").open = !0);
    // page order: the test, then what it asks of you, then the audit trail
    var tst = Rt.querySelector(".tatst");
    region.forEach(function (el) {
      if (el.classList.contains("pnote") && /^Where to start\\./.test(el.textContent.trim()) && fe) {
        var b = el.querySelector("b");
        b && (b.textContent = "Carries furthest:");
        var dw = document.createElement("div");
        dw.className = "tafws";
        while (el.firstChild) dw.appendChild(el.firstChild);
        fe.appendChild(dw);
        el.parentNode.removeChild(el);
      } else if (el.classList.contains("pnote") && /^Prompts, not findings/.test(el.textContent.trim())) el.classList.add("tapn");
      else if (el.classList.contains("rule")) {
        var rl = el.querySelector(".rl"),
          rt = rl ? rl.textContent.trim() : "";
        if ("DOES THIS ANSWER IT?" === rt && tst) tst.parentNode.insertBefore(el, tst.nextSibling);
        else if ("NOTHING YOU WOULD DO ANSWERS THESE YET" === rt) {
          var f = document.createElement("details");
          f.className = "fold";
          f.innerHTML = "<summary>NOTHING YOU WOULD DO ANSWERS THESE YET</summary>";
          el.parentNode.insertBefore(f, el);
          rl.parentNode.removeChild(rl);
          f.appendChild(el);
        }
      }
    });
    window.gsmTAV = (window.gsmTAV || 0) + 1;''')
# type tiers
rep('''#gsm .coa[data-seed] .phctx{color:#888}''', '''#gsm .coa[data-seed] .phctx{color:#888}#gsm .tafirst{border-left:5px solid #111;padding:2px 0 4px 12px;margin:2px 0 14px}#gsm .tafm{font-size:18px;line-height:1.5;color:#111}#gsm .tafws{font-size:13.5px;color:#555;margin-top:4px}#gsm .tatst .tev{font-size:13.5px;color:#666}#gsm .tapn{font-size:13px;color:#666;background:none;border:0;padding:0}#gsm .tastrip{border-left:4px solid #111;padding:2px 0 2px 12px;margin:8px 0 10px;font-size:16px;line-height:1.5;color:#111}#gsm .tastrip>div{margin:3px 0}#gsm .tsl{font-size:10.5px;font-weight:700;letter-spacing:.14em;color:#555;margin-right:4px}#gsm .tawhy>summary,#gsm .taev>summary{cursor:pointer;font-size:12.5px;letter-spacing:.1em;text-decoration:underline;margin:6px 0}#gsm .tawhy[open]{border-left:1px solid #ddd;padding-left:10px}#gsm .taev{font-size:13px;color:#666}#gsm .taev>summary{color:#666}#gsm .taev[open]{border-left:1px solid #eee;padding-left:10px}#gsm .ccons.cempty .ccq,#gsm .ccons.cempty .consq{display:none}#gsm .ccons:not(.cempty) .tanb{display:none}#gsm .tameta>summary{font-size:13px;cursor:pointer;text-decoration:underline;color:#444}''')
rep('''t.textContent = "v227"''', '''t.textContent = "v228"''')
open(P, "w").write(s)
print("ok")
