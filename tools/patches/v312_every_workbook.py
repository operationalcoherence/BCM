"""v312: F8 step 5, the lead's dashboard core: EVERY WORKBOOK.
Opening a project you lead shows every workbook saved in it as a table (person and voice, questions answered,
notes, main emotion, last change), counts people started and working now, and offers Open (read the workbook,
save it as a file for Combine workbooks), Remind (an email with their link), and Delete. Also Stop / Start
taking answers (the invite key's open flag). Run from the repository root:  python3 tools/patches/v312_every_workbook.py"""
import re
P = 'gsm-readable.js'
s = open(P, encoding='utf-8').read()

def rep(old, new, n=1):
    global s
    c = s.count(old)
    assert c == n, (c, old[:80])
    s = s.replace(old, new)

rep('t && (t.textContent = "v311");', 't && (t.textContent = "v312");')

# --- CSS for the table, inside the lead block's CSS string
rep('''    "#gsm-lead label.rad{display:flex;gap:8px;align-items:flex-start;margin:5px 0;font-weight:400;letter-spacing:0;font-size:14px}";''',
'''    "#gsm-lead label.rad{display:flex;gap:8px;align-items:flex-start;margin:5px 0;font-weight:400;letter-spacing:0;font-size:14px}" +
    "#gsm-lead .dash{border:1.5px solid #222;padding:10px 12px;margin:4px 0 14px}" +
    "#gsm-lead .esum{display:flex;flex-wrap:wrap;gap:4px 14px;align-items:baseline;margin:2px 0 6px}#gsm-lead .esum b{font-size:15px}" +
    "#gsm-lead table.ewb{width:100%;border-collapse:collapse;font-size:13.5px;margin:6px 0 4px}" +
    "#gsm-lead .ewb th{text-align:left;font-size:10.5px;letter-spacing:.12em;font-weight:700;color:#444;border-bottom:1.5px solid #222;padding:5px 8px 5px 0;vertical-align:bottom}" +
    "#gsm-lead .ewb td{border-bottom:1px solid #ddd;padding:7px 8px 7px 0;vertical-align:top}#gsm-lead .ewb td.ea{white-space:nowrap}" +
    "#gsm-lead .ewb td.ea .lnk{display:block;margin:0 0 4px;font-size:13px}#gsm-lead .ewb .ev{display:block;color:#666;font-size:12.5px}" +
    "#gsm-lead .ewb tr.eon td{background:#faf8f3}#gsm-lead .enow{display:inline-block;font-size:10px;letter-spacing:.1em;font-weight:700;border:1px solid #2f5d2f;color:#2f5d2f;padding:0 4px;margin-left:5px;vertical-align:1px}" +
    "#gsm-lead .esw{display:inline-block;width:11px;height:11px;border-radius:50%;margin-right:4px;vertical-align:-1px;border:1px solid rgba(0,0,0,.15)}" +
    "#gsm-lead .egray{color:#888}#gsm-lead .ewv{background:#faf8f3;border:1px solid #bbb;padding:10px 12px;margin:0 0 10px}" +
    "#gsm-lead .ewv .eq{display:flex;gap:8px;padding:5px 0;border-top:1px solid #e6e3dc;white-space:pre-wrap;overflow-wrap:anywhere}#gsm-lead .ewv .eq>b{flex:0 0 34px}" +
    "#gsm-lead .ewv .ewh{font-weight:700;letter-spacing:.12em;font-size:11px;margin:10px 0 2px}" +
    "@media(max-width:620px){#gsm-lead .ewb thead{display:none}#gsm-lead .ewb,#gsm-lead .ewb tbody,#gsm-lead .ewb tr,#gsm-lead .ewb td{display:block;width:100%}" +
    "#gsm-lead .ewb tr{border-top:1.5px solid #222;padding:6px 0}#gsm-lead .ewb td{border:0;padding:2px 0;display:flex;gap:8px}" +
    "#gsm-lead .ewb td[data-h]:before{content:attr(data-h);flex:0 0 104px;font-size:10.5px;letter-spacing:.12em;font-weight:700;color:#555;padding-top:2px}" +
    "#gsm-lead .ewb td.ea{gap:18px;padding-top:6px}#gsm-lead .ewb td.ea .lnk{display:inline;margin:0}#gsm-lead .ewb td.ew{display:block}}";''')

# --- the dashboard functions, before draw()
rep('''  function draw() {
    if (!box) return;
    var b = st.view === "signin" ? viewSignin()''',
r'''  /* v312: F8 step 5 - EVERY WORKBOOK. The lead reads projects/{pid}/workbooks (the rules let only the lead list them)
     and the invite key (to show whether answers are being taken). One read per workbook, on opening the project,
     on Refresh, and once a minute while the project stays open on screen. */
  var EMOS = [["Aggression", "#c8352e"], ["Acceptance", "#2a9d8f"], ["Distrust", "#a48fd0"], ["Indifference", "#e6be4f"], ["Defiance", "#1b2a8f"]],
    NOWMS = 5 * 60000,
    NOTICE = "This document was generated using The Bear Canyon Method, a method developed by Operational Coherence. The Bear Canyon Method is provided free of charge; however, attribution to Operational Coherence is required. The Bear Canyon Method, including its architecture, framework design, and implementation, remains the intellectual property of Operational Coherence.",
    dash = { pid: "", rows: [], at: 0, busy: false, err: "", msg: "", open: "", ask: "", taking: true };
  function tms(t) {
    if (!t) return 0;
    if (typeof t.toMillis === "function") return t.toMillis();
    if (t.seconds != null) return t.seconds * 1000;
    return +new Date(t) || 0;
  }
  function agoT(t) {
    if (!t) return "not saved yet";
    var s = Math.max(0, Math.round((Date.now() - t) / 1000));
    if (s < 60) return "just now";
    var m = Math.round(s / 60);
    if (m < 60) return m + (m === 1 ? " minute ago" : " minutes ago");
    var h = Math.round(m / 60);
    if (h < 48) return h + (h === 1 ? " hour ago" : " hours ago");
    return new Date(t).toLocaleDateString(undefined, { month: "short", day: "numeric" });
  }
  function readWb(x) {
    var w = null;
    try {
      w = JSON.parse((x.data && x.data.json) || "null");
    } catch (e) {}
    if (w && w.app && w.data) w = w.data;
    var r = { uid: x.id, name: String(x.name || "").trim() || "No name", voice: String(x.voice || "").trim(), at: tms(x.saved), w: w, ok: !!(w && typeof w === "object"), answered: 0, notes: 0, emo: [], none: 0 };
    if (!r.ok) return r;
    var a = Array.isArray(w.a) ? w.a : [],
      c = [0, 0, 0, 0, 0];
    for (var i = 0; i < 7; i++) String(a[i] || "").trim() && r.answered++;
    r.list = (Array.isArray(w.m) ? w.m : []).concat(w.p && Array.isArray(w.p.m) ? w.p.m : []).filter(function (n) {
      return Array.isArray(n) && String(n[3] || "").trim();
    });
    r.list.forEach(function (n) {
      r.notes++;
      n[5] != null && EMOS[n[5]] ? c[n[5]]++ : r.none++;
    });
    var top = Math.max.apply(null, c);
    top > 0 &&
      c.forEach(function (v, i) {
        v === top && r.emo.push(i);
      });
    return r;
  }
  function loadDash(quiet) {
    var p = st.cur;
    if (!p || !p.id || dash.busy) return;
    if (dash.pid !== p.id) dash = { pid: p.id, rows: [], at: 0, busy: false, err: "", msg: "", open: "", ask: "", taking: true };
    dash.busy = true;
    quiet || drawDash();
    var pid = p.id;
    window.gsmF8
      .fs()
      .then(function (S) {
        var M = S.M;
        return Promise.all([
          M.getDocs(M.collection(S.db, "projects", pid, "workbooks")),
          p.key ? M.getDoc(M.doc(S.db, "projects", pid, "keys", p.key)).catch(function () { return null; }) : null,
        ]);
      })
      .then(function (res) {
        if (dash.pid !== pid) return;
        dash.rows = res[0].docs.map(function (d) {
          var x = d.data();
          x.id = d.id;
          return readWb(x);
        });
        dash.rows.sort(function (a, b) {
          return b.at - a.at;
        });
        var k = res[1];
        if (k && k.exists && k.exists()) dash.taking = k.data().open !== false;
        dash.at = Date.now();
        dash.busy = false;
        dash.err = "";
        drawDash();
      })
      .catch(function (e) {
        dash.busy = false;
        dash.err = errText(e);
        drawDash();
      });
  }
  function emoCell(r) {
    if (!r.ok) return '<span class="egray">—</span>';
    if (!r.notes) return '<span class="egray">No notes yet</span>';
    if (!r.emo.length) return '<span class="egray">No emotion marked</span>';
    if (r.emo.length > 2) return "Mixed: " + r.emo.map(function (i) { return '<span class="esw" style="background:' + EMOS[i][1] + '"></span>' + EMOS[i][0]; }).join(", ");
    return r.emo.map(function (i) { return '<span class="esw" style="background:' + EMOS[i][1] + '"></span>' + EMOS[i][0]; }).join(" and ");
  }
  function remindHref(r) {
    var p = st.cur,
      body =
        "Hi " + r.name + ",\n\nA reminder about \"" + p.name + "\"" + (p.due ? ", with answers due " + p.due : "") + ". " +
        (r.ok ? "So far you've answered " + r.answered + " of the 7 questions and written " + r.notes + (r.notes === 1 ? " note" : " notes") + ". " : "") +
        "To carry on, open the same link as before, on the device you used:\n" + link(p) + "\n";
    return "mailto:?subject=" + encodeURIComponent("Reminder: " + p.name) + "&body=" + encodeURIComponent(body);
  }
  function viewWb(r) {
    var p = st.cur,
      w = r.w,
      h = '<div class="ewv">';
    if (!r.ok) return h + "This workbook couldn’t be read. It may have been saved by a newer or older version of the workbook.</div>";
    if (String(w.goal || "").trim() && String(w.goal).trim() !== String(p.goal || "").trim())
      h += '<div class="ewh">THEIR GOAL</div><div class="lh" style="margin:0 0 4px">It differs from the shared goal. It may be from before you last changed the goal.</div><div class="eq">' + esc(w.goal) + "</div>";
    h += '<div class="ewh">ANSWERS</div>';
    for (var i = 0; i < 7; i++) {
      var t = String((w.a || [])[i] || "").trim();
      h += '<div class="eq"><b>Q.' + (i + 1) + "</b><span" + (t ? ">" + esc(t) : ' class="egray">Not answered yet') + "</span></div>";
    }
    h += '<div class="ewh">NOTES</div>';
    if (!r.list.length) h += '<div class="eq egray">No notes yet.</div>';
    r.list.forEach(function (n, j) {
      var e = n[5] != null && EMOS[n[5]] ? EMOS[n[5]] : null;
      h +=
        '<div class="eq"><b>' + (j + 1) + '.</b><span>' + esc(n[3]) +
        '<span class="ev">' + (e ? '<span class="esw" style="background:' + e[1] + '"></span>' + e[0] : "No emotion marked") + (n[7] ? " · " + esc(n[7]) : "") + "</span></span></div>";
    });
    return (
      h +
      '<div class="lrow"><button type="button" class="btn alt" style="width:auto;flex:none" data-l="dfile" data-u="' + esc(r.uid) + '">Save as a file</button><button type="button" class="lnk sm" data-l="dclose">Close</button></div>' +
      '<div class="lh">The file opens with Combine workbooks, to read their workbook together with yours.</div></div>'
    );
  }
  function dashHtml() {
    var p = st.cur,
      h = '<div class="dash" id="gsm-ldash"><div class="ll" style="font-weight:700;letter-spacing:.12em;font-size:11.5px">EVERY WORKBOOK</div>';
    if (!p || dash.pid !== p.id || (dash.busy && !dash.at)) return h + '<div class="lh">Loading…</div></div>';
    var rows = dash.rows,
      now = rows.filter(function (r) { return r.at && Date.now() - r.at < NOWMS; }).length;
    h +=
      '<div class="esum"><b>' + (rows.length ? rows.length + (rows.length === 1 ? " person" : " people") + " started" : "Nobody has started yet") + "</b>" +
      (rows.length ? "<span>" + now + " working now</span>" : "") +
      '<span class="lh">' + (dash.busy ? "Updating…" : "Updated " + agoT(dash.at)) + ' · <button type="button" class="lnk sm" data-l="dref">Refresh</button></span></div>';
    h += '<div class="lh">' + (dash.taking ? "Taking answers. Each person’s workbook is sent to you as they work. “Working now” means saved in the last 5 minutes." : "<b>Not taking answers.</b> People can still open their workbooks, but nothing new is sent to you.") + "</div>";
    if (dash.err) h += '<div class="lmsg" role="status">' + esc(dash.err) + "</div>";
    if (dash.msg) h += '<div class="lmsg lok" role="status">' + esc(dash.msg) + "</div>";
    if (!rows.length) h += '<div class="lh" style="margin-top:6px">Send the invite link below. Each person who opens it and chooses Begin shows up here.</div>';
    else {
      h += '<table class="ewb"><thead><tr><th>PERSON</th><th>QUESTIONS</th><th>NOTES</th><th>MAIN EMOTION</th><th>LAST CHANGE</th><th><span style="position:absolute;left:-9999px">Actions</span></th></tr></thead><tbody>';
      rows.forEach(function (r) {
        var on = dash.open === r.uid;
        h +=
          '<tr' + (on ? ' class="eon"' : "") + '><td data-h="PERSON"><span><b>' + esc(r.name) + "</b>" + (r.at && Date.now() - r.at < NOWMS ? '<span class="enow">NOW</span>' : "") + '<span class="ev">' + (r.voice ? esc(r.voice) : "No voice") + "</span></span></td>" +
          '<td data-h="QUESTIONS">' + (r.ok ? r.answered + " of 7" : '<span class="egray">—</span>') + "</td>" +
          '<td data-h="NOTES">' + (r.ok ? r.notes : '<span class="egray">—</span>') + "</td>" +
          '<td data-h="MAIN EMOTION"><span>' + emoCell(r) + "</span></td>" +
          '<td data-h="LAST CHANGE">' + esc(agoT(r.at)) + "</td>" +
          '<td class="ea"><button type="button" class="lnk" data-l="dopen" data-u="' + esc(r.uid) + '" aria-expanded="' + on + '">' + (on ? "Close" : "Open") + '</button><a class="lnk" href="' + esc(remindHref(r)) + '">Remind</a><button type="button" class="lnk" data-l="ddel" data-u="' + esc(r.uid) + '">Delete</button></td></tr>';
        if (dash.ask === r.uid)
          h +=
            '<tr><td colspan="6" class="ew"><div class="warn">Delete ' + esc(r.name) + "’s workbook from this project? It can’t be undone. Their copy on their own device is kept" +
            (dash.taking ? ", and if they keep working it is sent again. To stop that, stop taking answers first." : ".") +
            '</div><div class="lrow"><button type="button" class="btn" data-l="ddelyes" data-u="' + esc(r.uid) + '">Delete for good</button><button type="button" class="btn alt" data-l="ddelno">Keep it</button></div></td></tr>';
        if (on) h += '<tr><td colspan="6" class="ew">' + viewWb(r) + "</td></tr>";
      });
      h += "</tbody></table>";
    }
    h +=
      '<div class="lrow"><button type="button" class="lnk sm" data-l="dtake">' + (dash.taking ? "Stop taking answers" : "Start taking answers again") + "</button>" +
      '<span class="lh">' + (dash.taking ? "Stops new saves from everyone. You can start again at any time." : "People’s work is sent again on their next save.") + "</span></div>";
    return h + "</div>";
  }
  function drawDash() {
    var el = box && document.getElementById("gsm-ldash");
    if (el) el.outerHTML = dashHtml();
  }
  function rowOf(u) {
    for (var i = 0; i < dash.rows.length; i++) if (dash.rows[i].uid === u) return dash.rows[i];
    return null;
  }
  function saveFile(r) {
    var p = st.cur,
      d = new Date(),
      safe = function (t) {
        return String(t).replace(/[^A-Za-z0-9 _-]+/g, "").trim().replace(/\s+/g, "-").slice(0, 40) || "workbook";
      },
      w = Object.assign({}, r.w);
    w.who || (w.who = r.name);
    var blob = new Blob([JSON.stringify({ app: "groundsmith", v: 1, saved: new Date(r.at || d).toISOString(), notice: NOTICE, data: w }, null, 1)], { type: "application/json" }),
      a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = "bear-canyon-" + safe(p.name) + "-" + safe(r.name) + ".json";
    document.body.appendChild(a);
    a.click();
    setTimeout(function () {
      URL.revokeObjectURL(a.href);
      a.remove();
    }, 1000);
  }
  function delWb(u) {
    var p = st.cur,
      r = rowOf(u);
    if (!p || !r) return;
    dash.msg = "Deleting…";
    drawDash();
    window.gsmF8
      .fs()
      .then(function (S) {
        return S.M.deleteDoc(S.M.doc(S.db, "projects", p.id, "workbooks", u));
      })
      .then(function () {
        dash.rows = dash.rows.filter(function (x) { return x.uid !== u; });
        dash.ask = "";
        dash.open === u && (dash.open = "");
        dash.msg = r.name + "’s workbook was deleted.";
        drawDash();
      })
      .catch(function (e) {
        dash.msg = "";
        dash.err = errText(e);
        drawDash();
      });
  }
  function setTaking(on) {
    var p = st.cur;
    if (!p || !p.id || !p.key) return;
    dash.msg = "Saving…";
    drawDash();
    window.gsmF8
      .fs()
      .then(function (S) {
        return S.M.updateDoc(S.M.doc(S.db, "projects", p.id, "keys", p.key), { open: on });
      })
      .then(function () {
        dash.taking = on;
        dash.msg = on ? "Taking answers again." : "Stopped taking answers.";
        drawDash();
      })
      .catch(function (e) {
        dash.msg = "";
        dash.err = errText(e);
        drawDash();
      });
  }
  function draw() {
    if (!box) return;
    var b = st.view === "signin" ? viewSignin()''')

rep('    if (!isNew) h += inviteBox(p);\n', '    if (!isNew) h += dashHtml() + inviteBox(p);\n')

# load the table when a project opens, and after a new one is created
rep('''    else if (k === "open") ((st.cur = st.list[i]), (st.voices = (st.cur.voices || []).slice()), go("form"));''',
'''    else if (k === "open") ((st.cur = st.list[i]), (st.voices = (st.cur.voices || []).slice()), (dash.pid = ""), go("form"), loadDash());
    else if (k === "dref") ((dash.msg = ""), loadDash());
    else if (k === "dopen") {
      var u = b.getAttribute("data-u");
      dash.open = dash.open === u ? "" : u;
      dash.ask = "";
      dash.msg = "";
      drawDash();
    } else if (k === "dclose") ((dash.open = ""), drawDash());
    else if (k === "dfile") {
      var fr = rowOf(b.getAttribute("data-u"));
      fr && fr.ok && saveFile(fr);
    } else if (k === "ddel") ((dash.ask = b.getAttribute("data-u")), (dash.msg = ""), drawDash());
    else if (k === "ddelno") ((dash.ask = ""), drawDash());
    else if (k === "ddelyes") delWb(b.getAttribute("data-u"));
    else if (k === "dtake") setTaking(!dash.taking);''')

rep('''        st.msg = wasNew ? "Project created. Send the invite link below." : "Saved.";
        draw();''',
'''        st.msg = wasNew ? "Project created. Send the invite link below." : "Saved.";
        draw();
        wasNew && loadDash();''')

# keep the table fresh while the project is open on screen
rep('''    box = document.createElement("div");
    box.id = "gsm-lead";''',
'''    setInterval(function () {
      if (!box || !box.classList.contains("on") || st.view !== "form" || !st.cur || !st.cur.id) return;
      document.visibilityState === "visible" && !dash.ask ? loadDash(true) : drawDash();
    }, 60000);
    box = document.createElement("div");
    box.id = "gsm-lead";''')

open(P, 'w', encoding='utf-8').write(s)
print('ok')
