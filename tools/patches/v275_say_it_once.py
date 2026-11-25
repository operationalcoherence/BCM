# v275: Pattern Analysis says each thing once (his go-ahead 25 Nov 2026 14:58, "fix all", on
# claude/pattern_analysis_repeats_review_2026-11-25.md in the Claude project), plus three fixes found in that read.
p = 'gsm-readable.js'
s = open(p, encoding='utf-8').read()

def rep(old, new, n=1):
    global s
    c = s.count(old)
    assert c == n, (c, old[:100])
    s = s.replace(old, new)

# ---- 5. chapter boilerplate: a sentence already said in an earlier chapter is not said again ----
rep('''      seenWhere = {},
      chap = [],
      out = [];''', '''      seenWhere = {},
      chap = [],
      said = {},
      out = [];''')
rep('''          : "For it to lose its influence, a ridge has to be made first. Nothing between this low ground and the help yet carries indifference, so going straight across is a climb over bare rock, and it takes the most energy in either direction.") +
          (acc ? " The acceptance that holds the present in place has to loosen too: until the current arrangement stops looking like the only legitimate one, every case for the goal will be heard as an attack on it." : "") +
          ("goal" === wh ? " Near the goal, the way out also means judging the change by what people do, not by what has been declared." : ""),
      );''', '''          : "For it to lose its influence, a ridge has to be made first. Nothing between this low ground and the help yet carries indifference, so going straight across is a climb over bare rock, and it takes the most energy in either direction."),
      );
      acc && S.push("The acceptance that holds the present in place has to loosen too: until the current arrangement stops looking like the only legitimate one, every case for the goal will be heard as an attack on it.");
      "goal" === wh && S.push("Near the goal, the way out also means judging the change by what people do, not by what has been declared.");
      /* v275: say once. A sentence an earlier chapter already said is left out here. */
      var S1 = S.slice(0, 3).filter(function (x) {
          return x && !said[x] && (said[x] = 1);
        }),
        S2 = S.slice(3).filter(function (x) {
          return x && !said[x] && (said[x] = 1);
        });''')
rep('''          S.slice(0, 3).join(" ") +
          "</p><p>" +
          S.slice(3).join(" ") +''', '''          S1.join(" ") +
          "</p><p>" +
          S2.join(" ") +''')

# ---- 3. the story no longer repeats AT A GLANCE's heading ----
rep('''      '<div class="evo"><div class="s1h">WHAT THE SYSTEM IS DOING</div>' +''', '''      '<div class="evo">' +''')

# ---- 4. WHAT HOLDS THE SITUATION IN PLACE goes when the story already says it ----
rep('''        var gh = gp.querySelector("h4");
        gh ? gh.after(grow) : gp.prepend(grow);
      }
    } catch (e) {}''', '''        var gh = gp.querySelector("h4");
        gh ? gh.after(grow) : gp.prepend(grow);
      }
      /* v275: the story says why the present holds, so the card that says it again goes */
      if (anyAcc && groot)
        [].slice.call(groot.querySelectorAll('[data-pv="2"] .sread')).forEach(function (r) {
          var l = r.querySelector(".srl");
          if (!l || "WHAT HOLDS THE SITUATION IN PLACE" !== l.textContent.trim() || !/taken as the right one/.test(r.textContent)) return;
          var box = r.parentNode;
          box.removeChild(r);
          if (!box.querySelector(".sread")) gsmDropSec(box);
        });
    } catch (e) {}''')
# a section left empty takes its heading with it
rep('''  function gsmStructBuild() {''', '''  function gsmDropSec(box) {
    /* the section body may already sit in its fold (.secb after a .plab.pfold) */
    var w = box.closest(".secb") || box;
    if (w !== box && w.textContent.replace(/\\s+/g, "") !== box.textContent.replace(/\\s+/g, "")) return box.parentNode.removeChild(box);
    var h = w.previousElementSibling;
    h && h.classList && h.classList.contains("plab") && h.parentNode.removeChild(h);
    w.parentNode && w.parentNode.removeChild(w);
  }
  function gsmStructBuild() {''')

# ---- 6. WHERE IT CAN CROSS is not shown (Taking Action still gets SS.cross) ----
rep('''    function card(lab, html, ev) {
      R.push(''', '''    function card(lab, html, ev) {
      if ("WHERE IT CAN CROSS" === lab) return; /* v275: the ground and the story say it */
      R.push(''')

# ---- 8. WHERE THIS LEAVES THE WORK goes: THE OPPORTUNITY says it ----
rep('''    if (P.length >= 3) {
      var mt = fd.querySelector(".mtext"),''', '''    if (0 && P.length >= 3) {
      /* v275: retired; THE OPPORTUNITY and WHAT HOLDS say the same */
      var mt = fd.querySelector(".mtext"),''')

# ---- 1, 2. WHAT STANDS OUT: the gap and the unused support are said elsewhere; both-sides cards merge ----
rep('''          })(
            b.filter(function (t) {
              return !t[2];
            }),
          ),''', '''          })(
            gsmAnOnce(b).filter(function (t) {
              return !t[2];
            }),
          ),''')
rep('''  function gsmStructBuild() {''', '''  /* v275: findings said elsewhere on the page are not cards. OPPOSITION NOT YET ENGAGED is BIGGEST GAP and the
     list under WHAT SHAPE; SUPPORT NOT YET REINFORCED and READY TO REINFORCE are THE OPPORTUNITY and the unused
     support list. FOR AND AGAINST ON THE MAP and OTHER SIDE OF THE LINE join CROSSES THE GROUND LINE. */
  function gsmAnOnce(b) {
    var cut = { "OPPOSITION NOT YET ENGAGED": 1, "SUPPORT NOT YET REINFORCED": 1, "READY TO REINFORCE": 1 },
      cr = null;
    b.forEach(function (t) {
      "CROSSES THE GROUND LINE" === t[0] && !cr && (cr = t);
    });
    cr &&
      b.forEach(function (t) {
        if ("FOR AND AGAINST ON THE MAP" === t[0]) cut[t[0]] = 1;
        if ("OTHER SIDE OF THE LINE" === t[0] && !cr.os) {
          cr.os = 1;
          cr[1] += "<p>Placed on the other side of the line from where its question usually sits: " + t[1].replace(/ sits where you might not expect it\\. Worth a second look\\.$/, ".") + "</p>";
          cut[t[0]] = 1;
        }
      });
    for (var i = b.length - 1; i >= 0; i--) cut[b[i][0]] && b.splice(i, 1);
    return b;
  }
  function gsmStructBuild() {''')

# POSSIBLE PATTERNS: drop the pairs that only restate the gap
rep('''                (r = r
                  .sort(function (t, e) {
                    return e.s - t.s;
                  })
                  .filter(function (t) {
                    return !a[t.k] && (a[t.k] = 1);
                  })),''', '''                (r = r
                  .sort(function (t, e) {
                    return e.s - t.s;
                  })
                  .filter(function (t) {
                    /* v275: the gap is said under BIGGEST GAP and WHAT SHAPE THE LINE MAP MAKES */
                    return !/comes up often, but nothing you would design|only ever appears[^]*none of your actions/.test(t.t);
                  })
                  .filter(function (t) {
                    return !a[t.k] && (a[t.k] = 1);
                  })),''')

# WHAT SHAPE THE LINE MAP MAKES: no "Areas to reinforce", no disposition count, no indifference list, no aside
rep('''              "plan",
              "strength",
            ].forEach(function (t) {''', '''              "plan",
            ].forEach(function (t) {''')
rep('''          ((lt +=
            "<p><b>Emotional disposition (" +''', '''          (0 &&
            (lt +=
            "<p><b>Emotional disposition (" +''')
rep('''              : o[pt[0]][0] + " leads.") +
            "</p>"),
            gt[3] &&''', '''              : o[pt[0]][0] + " leads.") +
            "</p>"),
            0 &&
            gt[3] &&''')
rep(''' then tie it to what needs doing to reach the goal. (The other way, <b>behaviors first</b>, suits aggression, distrust, and defiance: introduce the behavior itself, without its label, and let the emotion shift after it.)</p>");''',
    ''' then tie it to what needs doing to reach the goal.</p>");''')

# ---- story (whole workbook): no unused-support sentence, no NOT YET ANSWERED, no "Read them in full" ----
rep('''                (FR.unused || []).length &&
                  (s2 +=''', '''                0 &&
                  (FR.unused || []).length &&
                  (s2 +=''')
rep('''              var U = NR.u;
              out += P0(
                "NOT YET ANSWERED",''', '''              var U = [];
              /* v275: NOT YET ANSWERED is said under WHAT YOU WOULD DO and in WHAT SHAPE THE LINE MAP MAKES */
              out += P0(
                "NOT YET ANSWERED",''')
rep('''              gsmOwnStrip() +
              '<details class="more"><summary>Read them in full</summary><p>This only puts them in order; it does not say what they mean. A note is shown as answered only where you said so or drew the link.</p>' +
              sec("THE GOAL", '<div style="margin:4px 0">“' + Gt(g1) + "”</div>") +
              sec("WHAT STANDS IN THE WAY", h2) +
              sec("WHAT IS ALREADY HELPING", h3) +
              sec("WHAT HAS TO BE TRUE", h4) +
              sec("WHAT YOU WOULD DO", h5) +
              sec("WHERE TO START", h6) +
              sec("NOT YET ANSWERED", h7) +
              "</details></details></div></details>"''', '''              gsmOwnStrip() +
              "</details></div></details>"''')

# ---- fix a: the story's present/later reading is about the context grasped, and splits where NOW AND LATER does ----
rep('''                    now = function (o) {
                      return o.r[1] < 157;
                    },''', '''                    now = function (o) {
                      return o.r[1] < 146;
                    },''')
rep('''                        ? "Most of what hinders sits in the present, and most of what helps lies further on: the help is still ahead of the trouble."
                        : hl.length * 2 > H && pn.length * 2 > U
                          ? "Most of what helps is already here, and most of what hinders lies further on: the trouble is still ahead, which leaves time to meet it."
                          : hn.length * 2 > H && pn.length * 2 > U
                            ? "Most of what hinders and most of what helps sit in the present, so little of the context you have grasped yet reaches toward the goal."
                            : "What hinders and what helps are spread from the present toward the goal, so the work meets both all the way along."),''',
    '''                        ? "In the context you have grasped, most of what hinders sits in the present, and most of what helps lies further on: the help is still ahead of the trouble."
                        : hl.length * 2 > H && pn.length * 2 > U
                          ? "In the context you have grasped, most of what helps is already here, and most of what hinders lies further on: the trouble is still ahead, which leaves time to meet it."
                          : hn.length * 2 > H && pn.length * 2 > U
                            ? "In the context you have grasped, most of what hinders and most of what helps sit in the present, so little of it yet reaches toward the goal."
                            : "In the context you have grasped, what hinders and what helps are spread from the present toward the goal, so the work meets both all the way along."),''')
rep('''            '<div class="plab">NOW AND LATER</div><div class="mean"><p>You placed ' +''',
    '''            '<div class="plab">NOW AND LATER</div><div class="mean"><p>Counting what you would design too, you placed ' +''')

# ---- fix b: RUNS TOGETHER reads a note's side from where it sits on the line, not from its symbol ----
rep('''              var n = { id: t.id, side: Wt[t.k - 1], lead: 4 === t.k, act: t.k >= 5, ks: t.t.k };''',
    '''              var n = { id: t.id, side: Wt[t.k - 1], ls: t.line ? (t.line[2] < 118 ? 1 : -1) : null, lead: 4 === t.k, act: t.k >= 5, ks: t.t.k };''')
rep('''            var e = t.us.map(function (t) {
                return T[t];
              }),
              n = e.some(function (t) {
                return t.side > 0;
              }),
              o = e.some(function (t) {
                return t.side < 0;
              }),''', '''            var e = t.us.map(function (t) {
                return T[t];
              }),
              /* v275: a note's side is where it sits; an answer counts only for opposition or support */
              sd = function (t) {
                return null != t.ls ? t.ls : "Q.2" === t.id ? -1 : "Q.3" === t.id ? 1 : 0;
              },
              n = e.some(function (t) {
                return sd(t) > 0;
              }),
              o = e.some(function (t) {
                return sd(t) < 0;
              }),''')

# ---- 10. WHAT THIS SUGGESTS: the answers with no note are NOT ON THE MAP's to say ----
rep('''        miss.length &&
          (t +=
            " " +
            miss.join(", ") +''', '''        0 &&
          miss.length &&
          (t +=
            " " +
            miss.join(", ") +''')

# ---- 7. THE BARE LANDSCAPE: the table repeated the paragraphs above it ----
rep('''          R.join("") +
          '</div><details class="brm"><summary>Each ground, side by side</summary><table class="brt">' +
          tb +
          "</table></details>";''', '''          R.join("") +
          "</div>";''')
rep('''<p class="em">Tap the ground, a color in the bar, or a row in the table to read it.</p>''',
    '''<p class="em">Tap the ground or a color in the bar to read it.</p>''')

# ---- fix c: WHAT THE NUMBERS ON THE MAP SAY was built but hidden on Pattern Analysis (v273) ----
rep('''      ["crshead", "courses", "coursebox", "rdhead", "readings", "selnote", "msg"].forEach(function (id) {
        var e = $(id);
        if (e) e.style.display = "none";
      });
      LEGON = false;''', '''      ["crshead", "courses", "coursebox", "rdhead", "readings", "selnote", "msg"].forEach(function (id) {
        var e = $(id);
        if (e) e.style.display = "none";
      });
      /* v275: the list of the numbers is the one fold that stays */
      host._rdf && ((host._rdf.style.display = ""), ($("readings").style.display = ""));
      LEGON = false;''')

# Taking Action names where the unused support is now read on Analysis
rep('''                from: "SUPPORT NOT YET REINFORCED (Pattern Analysis)",''',
    '''                from: "Unused support, WHAT SHAPE THE LINE MAP MAKES (Pattern Analysis)",''')

rep('t.textContent = "v274"', 't.textContent = "v275"')
open(p, 'w', encoding='utf-8').write(s)
print('ok')
