"""v230: Taking Action speaks about the situation, not the workbook (his 11-18 21:53 wording review).
Logic and scoring unchanged; only user-facing text.
- THE SYSTEM THAT HOLDS -> WHAT HOLDS THE SITUATION IN PLACE (Analysis's card, the seeded card's title and source,
  THE TEST).
- THE TEST's lines: "What holds the situation in place", "What the goal needs, and people fear", "What keeps
  reinforcing the situation", "The alternative that already exists", "What already helps".
- "Not yet answered: N18 ..." -> "Tradition, ... remain unresolved." "Answered." -> what the proposed actions
  address (per line). "Not yet built on" -> "... already help the goal, but the proposed actions don't use them yet."
  Note numbers follow in small gray, as links, for auditing.
- The ridge line, the card test sentence, and the constraint summary in the same language.
Usage: python3 v230_situation_language.py gsm-readable.js"""
import sys
P = sys.argv[1]
s = open(P).read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:90]); s = s.replace(a, b)

rep('''        "THE SYSTEM THAT HOLDS",''', '''        "WHAT HOLDS THE SITUATION IN PLACE",''')
rep('''                from: "THE SYSTEM THAT HOLDS (Pattern Analysis)",''', '''                from: "WHAT HOLDS THE SITUATION IN PLACE (Pattern Analysis)",''')
rep('''                title: "What holds it: " + gsmMeanList(SS.sys.slice(0, 3)),''', '''                title: "What holds the situation in place: " + gsmMeanList(SS.sys.slice(0, 3)),''')
rep('''              ROWS.hold.push({ lab: "The system that holds", t: tS, title: "What holds it: " + gsmMeanList(SS.sys.slice(0, 3)) });''', '''              ROWS.hold.push({ lab: "What holds the situation in place", t: tS });''')
rep('''                ROWS.hold.push({ lab: "The key tension", t: tT, title: "The key tension: " + gs });''', '''                ROWS.hold.push({ lab: "What the goal needs, and people fear", t: tT });''')
rep('''                ROWS.hold.push({ lab: "The loop", t: tL, title: "The loop: " + lt });''', '''                ROWS.hold.push({ lab: "What keeps reinforcing the situation", t: tL });''')
rep('''              ROWS.move.push({ lab: "The opportunity", t: tO, title: "The opportunity" });''', '''              ROWS.move.push({ lab: "The alternative that already exists", t: tO });''')
rep('''              ROWS.move.push({ lab: "What is already helping", t: tH, title: "What is already helping" });''', '''              ROWS.move.push({ lab: "What already helps", t: tH });''')
# the test's kind, for what "yes" means
rep('''                test: tS,
                why: "it works in the low ground"''', '''                test: SAYK(tS, "sys"),
                why: "it works in the low ground"''')
rep('''                  test: tT,''', '''                  test: SAYK(tT, "ten"),''')
rep('''                  test: tL,''', '''                  test: SAYK(tL, "loop"),''')
rep('''                test: tO,''', '''                test: SAYK(tO, "help"),''')
rep('''                test: tH,''', '''                test: SAYK(tH, "help"),''')
rep('''                test: TEST(snr, 1),''', '''                test: SAYK(TEST(snr, 1), "help"),''')
rep('''              ROWS.hold.push({ lab: "What holds the situation in place", t: tS });''', '''              ROWS.hold.push({ lab: "What holds the situation in place", t: SAYK(tS, "sys") });''')
rep('''                ROWS.hold.push({ lab: "What the goal needs, and people fear", t: tT });''', '''                ROWS.hold.push({ lab: "What the goal needs, and people fear", t: SAYK(tT, "ten") });''')
rep('''                ROWS.hold.push({ lab: "What keeps reinforcing the situation", t: tL });''', '''                ROWS.hold.push({ lab: "What keeps reinforcing the situation", t: SAYK(tL, "loop") });''')
rep('''              ROWS.move.push({ lab: "The alternative that already exists", t: tO });''', '''              ROWS.move.push({ lab: "The alternative that already exists", t: SAYK(tO, "help") });''')
rep('''              ROWS.move.push({ lab: "What already helps", t: tH });''', '''              ROWS.move.push({ lab: "What already helps", t: SAYK(tH, "help") });''')
# the sentences themselves
rep('''              var h = "";
              met.length && (h += "What you would design reaches " + LS(met) + (by.length ? " (through " + phList(by.slice(0, 3)) + ")" : "") + ". ");
              not.length
                ? (h += "Nothing you would design " + (help ? "builds on " : "answers ") + LS(not) + " yet, so " + (help ? (1 === not.length ? "it" : "they") + " can slip." : (1 === not.length ? "it keeps" : "they keep") + " holding."))
                : (h += help ? "All of it is built on." : "All of it is answered somewhere.");
              return {
                h: h,
                met: met,
                not: not,
                v: not.length ? (met.length ? "partly" : "not yet") : "yes",
                s: not.length ? (help ? "Not yet built on: " : "Not yet answered: ") + NLS(not) + "." : help ? "Built on." : "Answered.",
              };''', '''              return { met: met, not: not, by: by, help: help, v: not.length ? (met.length ? "partly" : "not yet") : "yes" };''')
rep('''            function ME(x) {''', '''            function NAMES(xs, k) {
              k = k || 3;
              var b = xs.slice(0, k).map(function (x) {
                return Gt(NM(x));
              });
              xs.length > k && b.push(xs.length - k + " more");
              return phList(b).replace(/^./, function (c) {
                return c.toUpperCase();
              });
            }
            function IDS(xs, link) {
              return (
                ' <span class="stn">(' +
                xs
                  .map(function (x) {
                    var n = String(x.id).replace(/\\D/g, "");
                    return link ? x.id : (/^P/.test(x.id) ? "P" : "N") + n;
                  })
                  .join(", ") +
                ")</span>"
              );
            }
            var YES = {
              sys: "The proposed actions address every part holding it in place.",
              ten: "The proposed actions address the fear the goal runs into.",
              loop: "The proposed actions address the reinforcing cycle identified in Pattern Analysis.",
              help: "The proposed actions use all of it.",
            };
            function SAYK(t, kind) {
              if (!t || t.said) return t;
              var one = 1 === t.not.length,
                gap = function (link) {
                  return t.help
                    ? NAMES(t.not) + (one ? " already helps" : " already help") + " the goal, but the proposed actions don\\u2019t use " + (one ? "it" : "them") + " yet." + IDS(t.not, link)
                    : NAMES(t.not) + (one ? " remains" : " remain") + " unresolved." + IDS(t.not, link);
                };
              t.s = t.not.length ? gap(0) : YES[kind] || YES.help;
              t.r = t.not.length ? gap(1) : YES[kind] || YES.help;
              t.h =
                (t.met.length
                  ? "The proposed actions reach " +
                    NAMES(t.met, 4).replace(/^./, function (c) {
                      return c.toLowerCase();
                    }) +
                    IDS(t.met, 1) +
                    (t.by.length ? ' <span class="stn">(through ' + phList(t.by.slice(0, 3)) + ")</span>" : "") +
                    ". "
                  : "") +
                (t.not.length
                  ? t.help
                    ? NAMES(t.not, 4) + (one ? " already helps" : " already help") + " the goal, but nothing proposed uses " + (one ? "it" : "them") + " yet, so " + (one ? "it" : "they") + " can slip." + IDS(t.not, 1)
                    : NAMES(t.not, 4) + (one ? " remains" : " remain") + " unresolved, so " + (one ? "it keeps" : "they keep") + " holding the situation in place." + IDS(t.not, 1)
                  : YES[kind] || YES.help);
              t.said = 1;
              return t;
            }
            function ME(x) {''')
rep('''                  return "<div><i>" + r.lab + "</i> " + VL(r.t) + ' <span class="tev">' + (r.t.not.length ? "Not yet answered: " + LS(r.t.not, 3) + "." : "Answered.") + "</span></div>";''', '''                  return "<div><i>" + r.lab + "</i> " + VL(r.t) + " " + r.t.r + "</div>";''')
rep('''                  return "<div><i>" + r.lab + "</i> " + VL(r.t) + ' <span class="tev">' + (r.t.not.length ? "Not yet built on: " + LS(r.t.not, 3) + "." : "Built on.") + "</span></div>";''', '''                  return "<div><i>" + r.lab + "</i> " + VL(r.t) + " " + r.t.r + "</div>";''')
rep('''                  " The ridge of indifference runs through " +
                  LS(RIDGE, 4) +
                  ": " +
                  (tR.met.length ? "what you would design reaches " + LS(tR.met, 3) + (tR.not.length ? ", not yet " + LS(tR.not, 3) : "") + "." : "nothing you would design reaches it yet, and most crossings go through it.") +''', '''                  " People who are for nothing yet, the ridge of indifference, are where most shifts happen: " +
                  NAMES(RIDGE, 4).replace(/^./, function (c) {
                    return c.toLowerCase();
                  }) +
                  IDS(RIDGE, 1) +
                  ". " +
                  (tR.met.length
                    ? tR.not.length
                      ? "The proposed actions reach " + NAMES(tR.met).replace(/^./, function (c) { return c.toLowerCase(); }) + ", but not yet " + NAMES(tR.not).replace(/^./, function (c) { return c.toLowerCase(); }) + "."
                      : "The proposed actions reach all of them."
                    : "The proposed actions don\\u2019t reach them yet.") +''')
rep('''" No note carries indifference, so there is no ridge on this ground yet: every crossing is a climb over bare rock. Ask who is for nothing yet.</div>"''', '''" No one is mapped as for nothing yet, so there is no ridge of indifference: every shift is a climb over bare rock. Ask who is for nothing yet.</div>"''')
rep('''                      (1 === cons.length ? "One constraint named" : cons.length + " constraints named") +
                      "; " +
                      cons.filter(function (x) {
                        return x.indexOf("tav-yes") >= 0;
                      }).length +
                      " already in Q.4, Q.6, or Q.7.</div>" +''', '''                      (1 === cons.length ? "One thing holding the situation has been named" : cons.length + " things holding the situation have been named") +
                      "; " +
                      (function (n) {
                        return 0 === n ? "none is yet" : n === cons.length ? (1 === n ? "it is" : "all are") : n + " are";
                      })(
                        cons.filter(function (x) {
                          return x.indexOf("tav-yes") >= 0;
                        }).length,
                      ) +
                      " among the conditions to establish, redesigns, or reinforcements.</div>" +''')
rep('''                ["DOES WHAT YOU WOULD DESIGN MEET IT?", "The test on this card’s notes: which ones Q.5–Q.7 already reach, and which nothing reaches yet."],''', '''                ["DOES WHAT YOU WOULD DESIGN MEET IT?", "The test on this card: what the proposed actions already address, and what remains unresolved."],''')
# short check fixes
rep(r'''              return gsmStName({ txt: String(x.txt).replace(/^\s*(reinforce|continue to|support|scale|grow|keep)\s+/i, "") }) || x.id;''', r'''              return gsmStName({ txt: String(x.txt).replace(/^\s*(reinforce|continue to|support|scale|grow|keep)\s+/i, "").replace(/^\s*(for|to|in|on|with|by)\s+/i, "") }) || x.id;''')
rep('''" People who are for nothing yet, the ridge of indifference, are where most shifts happen: " +''', '''" Most shifts happen where people are for nothing yet, the ridge of indifference: " +''')
rep('''<div class="tatsub">Read against your workbook. Each line points to the cards below that take it up.</div>''', '''<div class="tatsub">Read against the situation you have mapped. The cards below take up each line.</div>''')
rep('''    if ("PLACED ONE WAY, TIED THE OTHER" === s.lab) return Gt(String((k.notes || [])[0] || "").replace(/^(?:place )?note (\\d+)/, "N$1")) + "\\u2019s place and ties disagree.";''', '''    if ("PLACED ONE WAY, TIED THE OTHER" === s.lab) {
      var nid = String((k.notes || [])[0] || ""),
        mm = /^(place )?note (\\d+)/.exec(nid),
        row = mm ? (mm[1] ? (C.p && C.p.m) || [] : C.m)[+mm[2] - 1] : null,
        nm = row ? gsmStName({ txt: String(row[3] || "") }) : "",
        lb = mm ? "N" + mm[2] : nid,
        who = (nm ? "\\u201c" + Gt(nm) + "\\u201d" : Gt(lb)),
        pe = null != k.pe ? k.pe : -1,
        pt = null != k.pt ? k.pt : -1,
        tail = nm ? \' <span class="stn">(\' + Gt(lb) + ")</span>" : "";
      return (!k.up && [0, 2, 4].indexOf(pe) >= 0 && (1 === pt || 3 === pt)
        ? who + " could be a foothold for the crossing."
        : pe >= 0 && pe === pt
          ? who + " carries energy that could be turned toward the goal."
          : k.up && [0, 2, 4].indexOf(pt) >= 0
            ? who + " looks like help but may give way under pressure."
            : who + " may not be where it seems.") + tail;
    }''')
rep('''t.textContent = "v229"''', '''t.textContent = "v230"''')
open(P, "w").write(s)
print("ok")
