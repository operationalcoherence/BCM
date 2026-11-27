"""v320: the lead's dashboard in three levels (Gregory, 26 Nov 19:55: "a smooth, clear UI that can be very condensed
(at a glance) or granular (each person)"; he chose mockup B, people as cards).
- Two tabs under the summary: People (default) and Project at a glance.
- People: the EVERY WORKBOOK table becomes cards in WORKING NOW, STILL GOING and FINISHED (all 7 answered). Each card:
  name, NOW, last change, voice, a seven-step bar (Q.1 to Q.4 dark, Q.5 to Q.7 grey), questions and notes, main emotion,
  Open, Remind, Delete. A group past 9 people shows 9 and "Show all N".
- One person (Open, or the name): back link, See their ground and their story (their workbook alone, opened as a copy for
  reading, like See everyone's ground together), Save as a file, Remind, Delete; progress by question; NEXT TO THE PROJECT
  (their emotion mix against the whole project, and the splits and agreements they are part of); their answers and
  notes, folded.
- Project at a glance: what READING THEM TOGETHER held, with HOW FAR THE PROJECT HAS GOT added and EMOTION ACROSS THE
  PROJECT (a whole-project row above the voices) moved up. "Patterns suggests; you decide." stays once, at the top.
- No new reads or writes: everything comes from the workbooks already read for the dashboard.
Run from the repository root:  python3 tools/patches/v320_lead_three_levels.py"""
P = 'gsm-readable.js'
s = open(P, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (c, old[:90]); s = s.replace(old, new)

rep('t && (t.textContent = "v319");', 't && (t.textContent = "v320");')

# state
rep('dash = { pid: "", rows: [], at: 0, busy: false, err: "", msg: "", open: "", ask: "", taking: true, voice: "" };',
    'dash = { pid: "", rows: [], at: 0, busy: false, err: "", msg: "", open: "", ask: "", taking: true, voice: "", tab: "people", who: "", more: {} };')
rep('if (dash.pid !== p.id) dash = { pid: p.id, rows: [], at: 0, busy: false, err: "", msg: "", open: "", ask: "", taking: true, voice: "" };',
    'if (dash.pid !== p.id) dash = { pid: p.id, rows: [], at: 0, busy: false, err: "", msg: "", open: "", ask: "", taking: true, voice: "", tab: "people", who: "", more: {} };')

# which questions each person has answered
rep('''    for (var i = 0; i < 7; i++) String(a[i] || "").trim() && r.answered++;''',
    '''    r.qa = [];
    for (var i = 0; i < 7; i++) (r.qa[i] = !!String(a[i] || "").trim()) && r.answered++;''')
rep('''var r = { uid: x.id, name: String(x.name || "").trim() || "No name", voice: String(x.voice || "").trim(), at: tms(x.saved), w: w, ok: !!(w && typeof w === "object"), answered: 0, notes: 0, emo: [], none: 0 };''',
    '''var r = { uid: x.id, name: String(x.name || "").trim() || "No name", voice: String(x.voice || "").trim(), at: tms(x.saved), w: w, ok: !!(w && typeof w === "object"), answered: 0, notes: 0, emo: [], none: 0, qa: [], list: [] };''')

# the person's answers and notes, without the old Save / Close row when shown inside the person view
rep('''  function viewWb(r) {
    var p = st.cur,''', '''  function viewWb(r, bare) {
    var p = st.cur,''')
rep('''    return (
      h +
      '<div class="lrow"><button type="button" class="btn alt" style="width:auto;flex:none" data-l="dfile" data-u="' + esc(r.uid) + '">Save as a file</button><button type="button" class="lnk sm" data-l="dclose">Close</button></div>' +''',
    '''    if (bare) return h + "</div>";
    return (
      h +
      '<div class="lrow"><button type="button" class="btn alt" style="width:auto;flex:none" data-l="dfile" data-u="' + esc(r.uid) + '">Save as a file</button><button type="button" class="lnk sm" data-l="dclose">Close</button></div>' +''')

# the table becomes the three levels
i0 = s.index('''    else {
      h += '<table class="ewb"><thead>''')
i1 = s.index('''      h += "</tbody></table>";
    }''', i0) + len('''      h += "</tbody></table>";
    }''')
s = s[:i0] + '''    else {
      var wr = dash.who ? rowOf(dash.who) : null;
      dash.who && !wr && (dash.who = "");
      h += wr ? personHtml(wr) : tabsHtml() + (dash.tab === "glance" ? readHtml() || '<div class="lh" style="margin-top:8px">Nothing to read yet: no workbook here could be read.</div>' : peopleHtml(rows));
    }''' + s[i1:]
rep('''    return h + readHtml() + "</div>";
  }
  function drawDash() {''', '''    return h + "</div>";
  }
  /* v320: the three levels. People (cards), one person, and Project at a glance (readHtml). */
  var GRPS = [["WORKING NOW", "saved in the last 5 minutes"], ["STILL GOING", "started, not finished"], ["FINISHED", "all 7 questions answered"]],
    GMAX = 9;
  function isNow(r) {
    return !!(r.at && Date.now() - r.at < NOWMS);
  }
  function tabsHtml() {
    return (
      '<div class="etabs" role="tablist" aria-label="Dashboard views">' +
      [["people", "People"], ["glance", "Project at a glance"]]
        .map(function (t) {
          var on = (dash.tab || "people") === t[0];
          return '<button type="button" role="tab" aria-selected="' + on + '"' + (on ? ' class="on"' : "") + ' data-l="dtab" data-v="' + t[0] + '">' + t[1] + "</button>";
        })
        .join("") +
      "</div>"
    );
  }
  function stepsHtml(r, lab) {
    var h = '<div class="estep' + (lab ? " elab" : "") + '" aria-hidden="true">';
    for (var i = 0; i < 7; i++) h += '<span class="' + (r.ok && r.qa[i] ? (i < 4 ? "s1" : "s2") : "") + '"><b></b>' + (lab ? "<i>Q." + (i + 1) + "</i>" : "") + "</span>";
    return h + "</div>";
  }
  function delAsk(r) {
    return (
      '<div class="warn">Delete ' + esc(r.name) + "’s workbook from this project? It can’t be undone. Their copy on their own device is kept" +
      (dash.taking ? ", and if they keep working it is sent again. To stop that, stop taking answers first." : ".") +
      '</div><div class="lrow"><button type="button" class="btn" data-l="ddelyes" data-u="' + esc(r.uid) + '">Delete for good</button><button type="button" class="btn alt" data-l="ddelno">Keep it</button></div>'
    );
  }
  function cardHtml(r) {
    var u = esc(r.uid),
      h =
        '<div class="ecard"><div class="ecth"><button type="button" class="ecn" data-l="dopen" data-u="' + u + '">' + esc(r.name) + "</button>" +
        (isNow(r) ? '<span class="enow">NOW</span>' : "") + '<span class="ect">' + esc(agoT(r.at)) + "</span></div>" +
        '<div class="ev">' + (r.voice ? esc(r.voice) : "No voice") + "</div>";
    h += r.ok
      ? stepsHtml(r) + '<div class="lh">' + r.answered + " of 7 questions answered · " + r.notes + (r.notes === 1 ? " note" : " notes") + '</div><div class="eemo"><span class="lh">Main emotion:</span> ' + emoCell(r) + "</div>"
      : '<div class="lh">This workbook couldn’t be read. It may have been saved by a newer or older version of the workbook.</div>';
    h +=
      '<div class="eact"><button type="button" class="lnk" data-l="dopen" data-u="' + u + '">Open</button><a class="lnk" href="' + esc(remindHref(r)) + '">Remind</a><button type="button" class="lnk" data-l="ddel" data-u="' + u + '">Delete</button></div>';
    dash.ask === r.uid && (h += delAsk(r));
    return h + "</div>";
  }
  function peopleHtml(rows) {
    var G = [[], [], []];
    rows.forEach(function (r) {
      G[isNow(r) ? 0 : r.ok && r.answered === 7 ? 2 : 1].push(r);
    });
    return G.map(function (g, i) {
      if (!g.length) return "";
      var show = dash.more[i] || g.length <= GMAX ? g : g.slice(0, GMAX);
      return (
        '<div class="egrp"><div class="egh"><b>' + GRPS[i][0] + "</b><span>" + g.length + (g.length === 1 ? " person" : " people") + " · " + GRPS[i][1] + "</span></div>" +
        '<div class="ecards">' + show.map(cardHtml).join("") + "</div>" +
        (show.length < g.length ? '<button type="button" class="lnk sm" data-l="dmore" data-g="' + i + '">Show all ' + g.length + "</button>" : "") +
        "</div>"
      );
    }).join("");
  }
  function mixOf(rows) {
    var c = [0, 0, 0, 0, 0],
      n = 0;
    rows.forEach(function (r) {
      (r.list || []).forEach(function (x) {
        x[5] != null && EMOS[x[5]] && (c[x[5]]++, n++);
      });
    });
    return { c: c, n: n };
  }
  function mixHtml(label, m) {
    var order = [1, 3, 2, 0, 4];
    if (!m.n) return '<div class="evr"><b>' + esc(label) + '</b> <span class="lh">no emotion marked yet</span></div>';
    return (
      '<div class="evr"><b>' + esc(label) + "</b>" +
      '<div class="ebar" aria-hidden="true">' + order.map(function (i) { return m.c[i] ? '<span style="width:' + (100 * m.c[i]) / m.n + "%;background:" + EMOS[i][1] + '"></span>' : ""; }).join("") + "</div>" +
      '<div class="lh">' + order.filter(function (i) { return m.c[i]; }).map(function (i) { return EMOS[i][0] + " " + Math.round((100 * m.c[i]) / m.n) + "%"; }).join(", ") + "</div></div>"
    );
  }
  function personHtml(r) {
    var p = st.cur,
      u = esc(r.uid),
      all = dash.rows.filter(function (x) { return x.ok; }),
      h = '<div class="eper"><button type="button" class="lnk sm" data-l="dback">← Everyone in ' + esc(p.name) + "</button>";
    h +=
      '<div class="eph"><b>' + esc(r.name) + "</b>" + (isNow(r) ? '<span class="enow">NOW</span>' : "") + "</div>" +
      '<div class="ev">' + (r.voice ? esc(r.voice) : "No voice") + " · last change " + esc(agoT(r.at)) + (r.ok ? " · " + r.notes + (r.notes === 1 ? " note" : " notes") : "") + "</div>";
    h +=
      '<div class="lrow">' +
      (r.ok ? '<button type="button" class="btn" style="width:auto;flex:none" data-l="rme" data-u="' + u + '">See their ground and their story →</button><button type="button" class="btn alt" style="width:auto;flex:none" data-l="dfile" data-u="' + u + '">Save as a file</button>' : "") +
      '<a class="lnk" href="' + esc(remindHref(r)) + '">Remind</a><button type="button" class="lnk" data-l="ddel" data-u="' + u + '">Delete</button></div>';
    dash.ask === r.uid && (h += delAsk(r));
    if (!r.ok) return h + '<div class="lh">This workbook couldn’t be read. It may have been saved by a newer or older version of the workbook.</div></div>';
    if (r.ok)
      h += '<div class="lh" style="margin:2px 0 0">Their workbook opens on its own as a copy for reading, with Pattern Analysis and Taking Action. Nothing there is sent or kept.</div>';
    var g = r.qa.slice(0, 4).filter(Boolean).length,
      d = r.qa.slice(4).filter(Boolean).length;
    h +=
      '<div class="rh">HOW FAR THEY HAVE GOT</div>' + stepsHtml(r, true) +
      '<div class="lh">' + r.answered + " of 7 answered. Grasping context (Q.1 to Q.4): " + g + " of 4. Designing for the context grasped (Q.5 to Q.7): " + d + " of 3.</div>";
    if (all.length >= 2) {
      h += '<div class="rh">NEXT TO THE PROJECT</div>' + mixHtml(r.name, mixOf([r])) + mixHtml("Whole project", mixOf(all));
      var S = shared(all),
        mine = function (x) { return x.r.uid === r.uid; },
        sp = S.split.filter(function (x) { return mine(x.pair[0]) || mine(x.pair[1]); }),
        ag = S.agree.filter(function (a) { return a.xs.some(mine); });
      sp.length && (h += '<div class="rsh">WHERE THEY SPLIT FROM OTHERS</div>' + sp.slice(0, 3).map(splitItem).join("") + (sp.length > 3 ? '<div class="lh">…and ' + (sp.length - 3) + " more.</div>" : ""));
      ag.length && (h += '<div class="rsh">WHERE THEY AGREE WITH OTHERS</div>' + ag.slice(0, 3).map(function (a) { return agreeItem(a); }).join("") + (ag.length > 3 ? '<div class="lh">…and ' + (ag.length - 3) + " more.</div>" : ""));
      sp.length || ag.length || (h += '<div class="lh">Nobody else names the same things in the same way yet.</div>');
    }
    h += '<details class="edet"><summary>THEIR ANSWERS AND NOTES</summary>' + viewWb(r, true) + "</details>";
    return h + "</div>";
  }
  function farHtml(rows) {
    var c = [0, 0, 0, 0, 0, 0, 0],
      n = rows.length,
      g = 0,
      d = 0;
    rows.forEach(function (r) {
      for (var i = 0; i < 7; i++) r.qa[i] && c[i]++;
      r.qa.slice(0, 4).every(Boolean) && g++;
      r.qa.slice(4).some(Boolean) && d++;
    });
    return (
      '<div class="efar" aria-hidden="true">' +
      c.map(function (v, i) {
        return '<div class="efq"><span class="efn">' + v + '</span><span class="efb"><b class="' + (i < 4 ? "s1" : "s2") + '" style="height:' + (n ? Math.round((100 * v) / n) : 0) + '%"></b></span><i>Q.' + (i + 1) + "</i></div>";
      }).join("") +
      "</div>" +
      '<div class="lh">How many of the ' + n + (n === 1 ? " person" : " people") + " have answered each question: " + c.map(function (v, i) { return "Q." + (i + 1) + " " + v; }).join(", ") + ". " +
      g + (g === 1 ? " has" : " have") + " answered all of Q.1 to Q.4 (grasping context); " + d + (d === 1 ? " has" : " have") + " started on Q.5 to Q.7 (designing for the context grasped).</div>"
    );
  }
  function drawDash() {''')

# the delete clears the person view too
rep('''        dash.open === u && (dash.open = "");
        dash.msg = r.name + "’s workbook was deleted.";''', '''        dash.open === u && (dash.open = "");
        dash.who === u && (dash.who = "");
        dash.msg = r.name + "’s workbook was deleted.";''')

# Project at a glance: readHtml without its old heading, with HOW FAR and EMOTION ACROSS THE PROJECT first
rep('''      h = '<div class="rdg"><div class="rh">READING THEM TOGETHER</div><div class="rpsd">Patterns suggests; you decide.</div>';''',
    '''      h = '<div class="rdg"><div class="rpsd">Patterns suggests; you decide.</div>';''')
rep('''    if (rows.length < 2) h += '<div class="lh" style="margin-top:8px">WHERE THEY AGREE and WHERE THEY SPLIT need''',
    '''    h += '<div class="rh">HOW FAR THE PROJECT HAS GOT</div>' + farHtml(rows);
    h += '<div class="rh">EMOTION ACROSS THE PROJECT</div>' + voiceHtml(rows);
    if (rows.length < 2) h += '<div class="lh" style="margin-top:8px">WHERE THEY AGREE and WHERE THEY SPLIT need''')
rep('''    h += '<div class="rh">EMOTION BY VOICE</div>' + voiceHtml(rows);
''', '')
rep('''    var h = V.map(function (v) {
      var order = [1, 3, 2, 0, 4];''', '''    var W = { k: "Whole project", ppl: 0, c: [0, 0, 0, 0, 0], n: 0 };
    V.forEach(function (v) {
      W.ppl += v.ppl;
      W.n += v.n;
      v.c.forEach(function (x, i) { W.c[i] += x; });
    });
    var h = (V.length >= 2 ? [W] : []).concat(V).map(function (v) {
      var order = [1, 3, 2, 0, 4];''')

# one person's workbook, opened as a copy for reading
rep('''  function openTogether() {
    var rows = vrows(),
      p = st.cur;''', '''  function openTogether(only) {
    var rows = only ? [only] : vrows(),
      p = st.cur;''')
rep('''JSON.stringify({ name: p.name, voice: dash.voice || "", n: rows.length, at: Date.now() })''',
    '''JSON.stringify({ name: p.name, voice: only ? "" : dash.voice || "", who: only ? only.name : "", n: rows.length, at: Date.now() })''')
rep('''      '<div class="jt">' + esc(String(M.name || "A shared project").toUpperCase()) + " · EVERYONE TOGETHER</div>" +
      "<div>" + (M.n || 0) + ((M.n || 0) === 1 ? " person" : " people") + (M.voice ? ", " + esc(M.voice) + " only" : ", every voice") + ". Their answers and notes are read here as one workbook.</div>" +''',
    '''      '<div class="jt">' + esc(String(M.name || "A shared project").toUpperCase()) + (M.who ? " · " + esc(String(M.who).toUpperCase()) : " · EVERYONE TOGETHER") + "</div>" +
      (M.who
        ? "<div>" + esc(M.who) + "’s answers and notes, read here on their own.</div>"
        : "<div>" + (M.n || 0) + ((M.n || 0) === 1 ? " person" : " people") + (M.voice ? ", " + esc(M.voice) + " only" : ", every voice") + ". Their answers and notes are read here as one workbook.</div>") +''')
rep('''". Nothing here is sent or kept. Pattern Analysis shows the ground they make together.</div>" +''',
    '''". Nothing here is sent or kept. " + (M.who ? "Pattern Analysis shows the ground their notes make." : "Pattern Analysis shows the ground they make together.") + "</div>" +''')

# clicks
rep('''    else if (k === "dopen") {
      var u = b.getAttribute("data-u");
      dash.open = dash.open === u ? "" : u;
      dash.ask = "";
      dash.msg = "";
      drawDash();
    }''', '''    else if (k === "dopen") {
      dash.who = b.getAttribute("data-u");
      dash.ask = "";
      dash.msg = "";
      drawDash();
      var de = document.getElementById("gsm-ldash");
      de && de.scrollIntoView && de.scrollIntoView({ block: "start" });
    } else if (k === "dback") ((dash.who = ""), (dash.ask = ""), (dash.msg = ""), drawDash());
    else if (k === "dtab") ((dash.tab = b.getAttribute("data-v") || "people"), (dash.who = ""), (dash.ask = ""), drawDash());
    else if (k === "dmore") ((dash.more[b.getAttribute("data-g")] = 1), drawDash());
    else if (k === "rme") {
      var mr = rowOf(b.getAttribute("data-u"));
      mr && mr.ok && openTogether(mr);
    }''')
rep('''    else if (k === "rtog") openTogether();''', '''    else if (k === "rtog") openTogether();''')

# styles
rep('''    "#gsm-lead .evr{margin:8px 0}''', '''    "#gsm-lead .etabs{display:flex;gap:2px;border-bottom:1.5px solid #222;margin:12px 0 10px}#gsm-lead .etabs button{border:0;background:none;font:inherit;font-size:14px;padding:9px 12px;min-height:44px;color:#555;cursor:pointer;border-bottom:3px solid transparent;margin-bottom:-1.5px}" +
    "#gsm-lead .etabs button.on{color:#111;font-weight:700;border-bottom-color:#222}" +
    "#gsm-lead .egrp{margin:6px 0 14px}#gsm-lead .egh{display:flex;flex-wrap:wrap;gap:4px 10px;align-items:baseline;border-bottom:1px solid #ccc;padding:0 0 4px;margin:0 0 8px}" +
    "#gsm-lead .egh b{letter-spacing:.12em;font-size:11.5px}#gsm-lead .egh span{color:#666;font-size:12.5px}" +
    "#gsm-lead .ecards{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:10px}" +
    "#gsm-lead .ecard{border:1px solid #bbb;background:#fff;padding:10px 12px;display:flex;flex-direction:column;gap:6px;min-width:0}" +
    "#gsm-lead .ecth{display:flex;align-items:baseline;gap:6px}#gsm-lead .ecn{border:0;background:none;padding:0;font:inherit;font-weight:700;font-size:15px;text-align:left;cursor:pointer;color:#111;overflow-wrap:anywhere}" +
    "#gsm-lead .ecn:hover{text-decoration:underline}#gsm-lead .ect{margin-left:auto;color:#666;font-size:12px;white-space:nowrap}#gsm-lead .ecard .ev,#gsm-lead .eper .ev{color:#666;font-size:12.5px}" +
    "#gsm-lead .estep{display:flex;gap:3px;margin:2px 0 0}#gsm-lead .estep span{flex:1;display:block}#gsm-lead .estep b{display:block;height:7px;background:#e4e1d9}" +
    "#gsm-lead .estep .s1 b{background:#222}#gsm-lead .estep .s2 b{background:#7a7a7a}#gsm-lead .estep i{display:block;font-style:normal;font-size:11px;color:#666;text-align:center;margin-top:3px}#gsm-lead .estep.elab b{height:10px}" +
    "#gsm-lead .eemo{font-size:13.5px}#gsm-lead .eact{display:flex;align-items:center;gap:16px;border-top:1px solid #e6e3dc;padding-top:6px;margin-top:2px}#gsm-lead .eact .lnk,#gsm-lead .eper>.lrow>.lnk{display:inline-flex;align-items:center;font-size:13.5px;min-height:32px;margin:0;padding:0;line-height:1.3;vertical-align:middle}#gsm-lead .eact .lnk:last-child{margin-left:auto}" +
    "#gsm-lead .eper{margin:8px 0 4px}#gsm-lead .eper .rh{font-weight:700;letter-spacing:.12em;font-size:11.5px;margin:16px 0 4px}#gsm-lead .eper .rsh{font-weight:700;letter-spacing:.1em;font-size:10.5px;color:#444;margin:12px 0 2px}" +
    "#gsm-lead .eph{display:flex;align-items:baseline;gap:6px;margin:10px 0 0}#gsm-lead .eph b{font-size:20px}" +
    "#gsm-lead .edet{margin:16px 0 0;border-top:1.5px solid #222;padding-top:8px}#gsm-lead .edet summary{cursor:pointer;font-weight:700;letter-spacing:.12em;font-size:11.5px;min-height:28px}" +
    "#gsm-lead .edet .ewv{margin:8px 0 0}#gsm-lead .etabs+.rdg{border-top:0;margin-top:0;padding-top:0}" +
    "#gsm-lead .efar{display:grid;grid-template-columns:repeat(7,minmax(0,1fr));gap:6px;max-width:460px;margin:6px 0 4px}#gsm-lead .efq{display:flex;flex-direction:column;align-items:stretch;gap:2px}" +
    "#gsm-lead .efn{font-size:12px;text-align:center}#gsm-lead .efb{height:64px;display:flex;align-items:flex-end;background:#f1efe9}#gsm-lead .efb b{display:block;width:100%;background:#222}#gsm-lead .efb b.s2{background:#7a7a7a}" +
    "#gsm-lead .efq i{font-style:normal;font-size:11px;color:#666;text-align:center}" +
    "#gsm-lead .evr{margin:8px 0}''')

open(P, 'w', encoding='utf-8').write(s)
print('v320 patched')
