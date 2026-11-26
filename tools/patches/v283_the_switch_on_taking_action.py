# v283: TWO WAYS OF RUNNING reaches Taking Action (his "1. go", 25 Nov 2026 17:11): after a Yes, a row in
# THE TEST, "The switch", tested like the rest: YES when what you would design says how the switch is made,
# PARTLY when it only reaches the conditions, NOT YET otherwise. Silent before a Yes and after a No.
p = 'gsm-readable.js'
s = open(p, encoding='utf-8').read()

def rep(old, new, n=1):
    global s
    c = s.count(old)
    assert c == n, (c, old[:100])
    s = s.replace(old, new)

# 1. the reader keeps what Taking Action needs
rep('''    return { say: say, ev: ev.join(""), ask: 0, key: key, conds: [c1.show, c2.show], refs: tied.map(function (n) { return n.ref; }) };''',
'''    return {
      say: say,
      ev: ev.join(""),
      ask: 0,
      key: key,
      conds: [c1.show, c2.show],
      refs: tied.map(function (n) {
        return n.ref;
      }),
      sw: sw.map(function (n) {
        return n.lab;
      }),
      reach: reach.map(function (n) {
        return n.lab;
      }),
    };''')

# 2. Taking Action: a row in THE TEST, after "After the goal"
rep('''                    " Count the goal reached by how people work, not by what is announced.</div>",
                );
              })() +''',
'''                    " Count the goal reached by how people work, not by what is announced.</div>",
                );
              })() +
              (function () {
                /* v283: TWO WAYS OF RUNNING, tested like the rest (only after a Yes) */
                var MD = SS.modes;
                if (!MD || MD.ask || !MD.conds) return "";
                var tM = { v: MD.sw.length ? "yes" : MD.reach.length ? "partly" : "not yet" },
                  L = function (a) {
                    return " (" + Gt(gsmMeanList(a.slice(0, 4))) + ")";
                  };
                return row(
                  "The switch",
                  "<div>" +
                    VL(tM) +
                    " You said the goal runs two ways: one <b>" +
                    Gt(MD.conds[0]) +
                    "</b>, the other <b>" +
                    Gt(MD.conds[1]) +
                    "</b>. " +
                    (MD.sw.length
                      ? "What you would do says how the switch is made" + L(MD.sw) + "."
                      : (MD.reach.length
                          ? "What you would do reaches part of it" + L(MD.reach) + ", but not who calls the switch, or what tells them conditions have changed."
                          : "Nothing you would do yet says who calls the switch, or what tells them conditions have changed.") +
                        " Decide both, so no one is working one way while others work the other.") +
                    "</div>",
                );
              })() +''')

rep('t && (t.textContent = "v282");', 't && (t.textContent = "v283");')
open(p, 'w', encoding='utf-8').write(s)
print('ok')
