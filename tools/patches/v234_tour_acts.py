"""v234: the Synthesis tour opens each of his four acts with what that act means (review plan item 4c, E8).
The first stop of THE HIGH GROUND, THE LOW GROUND, BETWEEN THEM, and WHAT KEEPS IT THIS WAY gets one line under
the act's name, written from his confirmed meanings of the ground (emotions are not good or bad in themselves;
acceptance the highest ground; indifference a narrow ridge most moves cross, where people can stay precariously;
defiance the lowest ground and the longest road back) and counted from the workbook's own notes. Tour captions
never cite the paper. Built for every workbook; the stop holds a little longer to be read.
Usage: python3 v234_tour_acts.py gsm-readable.js tools/relief/relief.js"""
import sys
P, R = sys.argv[1], sys.argv[2]
s = open(P).read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:90]); s = s.replace(a, b)
rep('''          D.groups = GROUPS;''', '''          D.groups = GROUPS;
          /* v234: what each act of the tour means, from his confirmed meanings, counted from this workbook */
          D.actMean = (function () {
            var c = [0, 0, 0, 0, 0];
            ((terr && terr.notes) || []).forEach(function (n) {
              null != n.e && c[n.e]++;
            });
            var nn = function (k, w) {
                return k + " " + (1 === k ? "note" : "notes") + " " + w;
              },
              low = c[0] + c[2] + c[4];
            return [
              "Acceptance: where the goal already has people with it. It takes care to keep, and it is the place to start from. " +
                (c[1] ? nn(c[1], "of yours stand" + (1 === c[1] ? "s" : "") + " here.") : "None of your notes stand here yet."),
              "Distrust, aggression, and defiance. They are not bad in themselves; what matters is what they are attached to. The deeper the ground, the longer the road back to acceptance, and defiance is the longest. " +
                (low ? nn(low, "of yours sit" + (1 === low ? "s" : "") + " here.") : "None of your notes sit here yet."),
              "Indifference: a narrow ridge where people are not yet for or against. Most moves between emotions cross it, and people can stay on it, precariously. " +
                (c[3] ? nn(c[3], "of yours carr" + (1 === c[3] ? "ies" : "y") + " it.") : "None of your notes carry it yet, so there is no ridge to cross by."),
              "What holds the situation in place: patterns in your answers and notes that keep the ground as it is until something changes them.",
            ];
          })();''')
rep('t && (t.textContent = "v233");', 't && (t.textContent = "v234");')
open(P, "w").write(s)

r = open(R).read()
def rr(a, b):
    global r
    assert r.count(a) == 1, (r.count(a), a[:80]); r = r.replace(a, b)
rr('''cap.innerHTML = '<div class="ta"></div><div class="tt"></div><div class="tx"></div><div class="tp"><i></i></div>';''',
   '''cap.innerHTML = '<div class="ta"></div><div class="tm"></div><div class="tt"></div><div class="tx"></div><div class="tp"><i></i></div>'; const am = actOpen(i); cap.querySelector('.tm').textContent = am; cap.querySelector('.tm').style.display = am ? '' : 'none';''')
rr('''  function capFor(i) {''', '''  /* v234: the first stop of each act opens with what the act means */
  function actOpen(i) { const r = TL[i]; if (i < NI || !r || r.grp == null || !D.actMean) return ''; const p = TL[i - 1]; return (i === NI || !p || p.grp !== r.grp) ? (D.actMean[r.grp] || '') : ''; }
  function capFor(i) {''')
rr('''    const hold = r => Math.max(2.4, Math.min(6, String((r.title || '') + ' ' + (r.cap || r.text || '')).split(/\\s+/).length / 3.3)) * SL;''',
   '''    const hold = (r, i) => (Math.max(2.4, Math.min(6, String((r.title || '') + ' ' + (r.cap || r.text || '')).split(/\\s+/).length / 3.3)) + Math.min(5, actOpen(i).split(/\\s+/).filter(Boolean).length / 3.6)) * SL;''')
rr('''legs.push({ i, a: from, b: [hp.clone(), ht.clone()], fly, hold: hold(r) });''', '''legs.push({ i, a: from, b: [hp.clone(), ht.clone()], fly, hold: hold(r, i) });''')
rr('''legs.push({ i, a: from, b: [p, lk], fly, hold: hold(r) });''', '''legs.push({ i, a: from, b: [p, lk], fly, hold: hold(r, i) });''')
rr('''.grel .tourcap .ta{font-size:12.5px;letter-spacing:.14em;font-weight:700;color:#555}''',
   '''.grel .tourcap .ta{font-size:12.5px;letter-spacing:.14em;font-weight:700;color:#555}.grel .tourcap .tm{font-size:15px;line-height:1.45;color:#333;margin:4px 0 8px;padding:0 0 8px;border-bottom:1px solid #ddd}''')
open(R, "w").write(r)
print("ok")
