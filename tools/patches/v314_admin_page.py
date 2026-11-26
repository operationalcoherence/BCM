"""v314: F8 step 5b, the admin page for Gregory. Open the page with #bcmadmin (or ?bcmadmin) and sign in with
operationalcoherence@gmail.com. Counts across all F8 projects: projects, leads, people, saved workbooks, complete
(7 of 7), working now, notes, and exports (a lead's Save as a file), with one row per project. Counts only: no
names of people answering and no content are shown. The solo version is not counted (its workbooks never leave the
device); traffic comes from Webador's own statistics. Firebase loads only on this address.
Run from the repository root:  python3 tools/patches/v314_admin_page.py"""
P = 'gsm-readable.js'
s = open(P, encoding='utf-8').read()

def rep(old, new, n=1):
    global s
    c = s.count(old)
    assert c == n, (c, old[:80])
    s = s.replace(old, new)

rep('t && (t.textContent = "v313");', 't && (t.textContent = "v314");')

# a lead's Save as a file is counted on the project record (exports), for the admin page
rep('''    else if (k === "dfile") {
      var fr = rowOf(b.getAttribute("data-u"));
      fr && fr.ok && saveFile(fr);''',
'''    else if (k === "dfile") {
      var fr = rowOf(b.getAttribute("data-u"));
      fr && fr.ok && saveFile(fr);
      /* v314: count it, for the admin page; one write, and nothing is lost if it fails */
      fr && fr.ok && st.cur && st.cur.id &&
        window.gsmF8
          .fs()
          .then(function (S) {
            return S.M.increment && S.M.updateDoc(S.M.doc(S.db, "projects", st.cur.id), { exports: S.M.increment(1) });
          })
          .catch(function () {});''')

rep('''/* v313: F8 step 6 - reading everyone together (#bcmread=pid).''',
r'''/* v314: F8 step 5b - the admin page (#bcmadmin). Only operationalcoherence@gmail.com can read across projects
   (the rules check the signed-in Google email). Counts only, read on opening and on Refresh. */
!(function () {
  if (!/[?&#]bcmadmin\b/.test(location.search + location.hash)) return;
  var ADMIN = "operationalcoherence@gmail.com",
    NOWMS = 5 * 60000,
    box = null,
    st = { busy: false, msg: "", at: 0, P: [], W: [] };
  function esc(t) {
    return String(t == null ? "" : t).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }
  function tms(t) {
    if (!t) return 0;
    if (typeof t.toMillis === "function") return t.toMillis();
    if (t.seconds != null) return t.seconds * 1000;
    return +new Date(t) || 0;
  }
  function ago(t) {
    if (!t) return "—";
    var s = Math.max(0, Math.round((Date.now() - t) / 1000));
    if (s < 60) return "just now";
    var m = Math.round(s / 60);
    if (m < 60) return m + (m === 1 ? " minute ago" : " minutes ago");
    var h = Math.round(m / 60);
    if (h < 48) return h + (h === 1 ? " hour ago" : " hours ago");
    return new Date(t).toLocaleDateString(undefined, { month: "short", day: "numeric", year: "numeric" });
  }
  function errText(e) {
    var c = (e && e.code) || "";
    if (/permission-denied/.test(c)) return "The database refused this. Either this account is not the admin, or the admin rules are not published yet.";
    if (/popup-closed|cancelled-popup/.test(c)) return "Sign-in was closed before it finished.";
    if (/unavailable|network/.test(c)) return "No connection. Try again when you are online.";
    return "Something went wrong: " + (c || (e && e.message) || e);
  }
  function count(x) {
    var w = null,
      r = { answered: 0, notes: 0 };
    try {
      w = JSON.parse((x.data && x.data.json) || "null");
    } catch (e) {}
    w && w.app && w.data && (w = w.data);
    if (!w || typeof w !== "object") return r;
    for (var i = 0; i < 7; i++) String((w.a || [])[i] || "").trim() && r.answered++;
    (Array.isArray(w.m) ? w.m : []).concat(w.p && Array.isArray(w.p.m) ? w.p.m : []).forEach(function (n) {
      Array.isArray(n) && String(n[3] || "").trim() && r.notes++;
    });
    return r;
  }
  function me() {
    return window.gsmF8 && window.gsmF8.user();
  }
  function isAdmin() {
    var u = me();
    return !!(u && !u.anon && String(u.email || "").toLowerCase() === ADMIN);
  }
  function load() {
    st.busy = true;
    st.msg = "";
    draw();
    window.gsmF8
      .fs()
      .then(function (S) {
        var M = S.M;
        return Promise.all([M.getDocs(M.collection(S.db, "projects")), M.getDocs(M.collectionGroup(S.db, "workbooks"))]);
      })
      .then(function (res) {
        st.P = res[0].docs.map(function (d) {
          var x = d.data();
          return { id: d.id, name: x.name || "Untitled", lead: x.lead || "", leadName: x.leadName || "", created: tms(x.created), updated: tms(x.updated), exports: +x.exports || 0 };
        });
        st.W = res[1].docs.map(function (d) {
          var x = d.data(),
            c = count(x),
            pp = d.ref && d.ref.parent && d.ref.parent.parent;
          return { pid: pp ? pp.id : String((d.ref && d.ref.path) || "").split("/")[1], uid: d.id, at: tms(x.saved), answered: c.answered, notes: c.notes };
        });
        st.busy = false;
        st.at = Date.now();
        draw();
      })
      .catch(function (e) {
        st.busy = false;
        st.msg = errText(e);
        draw();
      });
  }
  function stat(n, l) {
    return '<div class="ast"><b>' + n + "</b><span>" + l + "</span></div>";
  }
  function viewData() {
    var P = st.P,
      W = st.W,
      now = Date.now(),
      wk = now - 7 * 86400000,
      leads = {},
      ppl = {},
      done = 0,
      on = 0,
      notes = 0,
      ex = 0;
    P.forEach(function (p) {
      p.lead && (leads[p.lead] = 1);
      ex += p.exports;
    });
    W.forEach(function (w) {
      ppl[w.uid] = 1;
      w.answered === 7 && done++;
      w.at && now - w.at < NOWMS && on++;
      notes += w.notes;
    });
    var h =
      '<div class="agrid">' +
      stat(P.length, P.length === 1 ? "project" : "projects") +
      stat(Object.keys(leads).length, Object.keys(leads).length === 1 ? "lead" : "leads") +
      stat(Object.keys(ppl).length, "people answering") +
      stat(W.length, W.length === 1 ? "saved workbook" : "saved workbooks") +
      stat(done, "complete (7 of 7)") +
      stat(on, "working now") +
      stat(notes, notes === 1 ? "note" : "notes") +
      stat(ex, ex === 1 ? "export" : "exports") +
      "</div>" +
      '<div class="lh">In the last 7 days: ' +
      (function (a, b) {
        return a + (a === 1 ? " new project, " : " new projects, ") + b + (b === 1 ? " workbook" : " workbooks") + " saved to. ";
      })(P.filter(function (p) { return p.created > wk; }).length, W.filter(function (w) { return w.at > wk; }).length) + "“Working now” means saved in the last 5 minutes. Exports are a lead’s Save as a file.</div>";
    if (!P.length) return h + '<div class="lh" style="margin-top:8px">No projects yet.</div>';
    var rows = P.map(function (p) {
      var ws = W.filter(function (w) { return w.pid === p.id; }),
        last = Math.max.apply(null, [p.updated || p.created || 0].concat(ws.map(function (w) { return w.at; })));
      return { p: p, ws: ws, last: last };
    }).sort(function (a, b) { return b.last - a.last; });
    h +=
      '<table class="ewb"><thead><tr><th>PROJECT</th><th>STARTED</th><th>PEOPLE</th><th>COMPLETE</th><th>NOTES</th><th>EXPORTS</th><th>LAST CHANGE</th></tr></thead><tbody>' +
      rows.map(function (r) {
        var live = r.ws.some(function (w) { return w.at && now - w.at < NOWMS; });
        return (
          '<tr><td data-h="PROJECT"><span><b>' + esc(r.p.name) + "</b>" + (live ? '<span class="enow">NOW</span>' : "") + '<span class="ev">Lead: ' + esc(r.p.leadName || "no name") + "</span></span></td>" +
          '<td data-h="STARTED">' + esc(r.p.created ? new Date(r.p.created).toLocaleDateString(undefined, { month: "short", day: "numeric", year: "numeric" }) : "—") + "</td>" +
          '<td data-h="PEOPLE">' + r.ws.length + "</td>" +
          '<td data-h="COMPLETE">' + r.ws.filter(function (w) { return w.answered === 7; }).length + "</td>" +
          '<td data-h="NOTES">' + r.ws.reduce(function (a, w) { return a + w.notes; }, 0) + "</td>" +
          '<td data-h="EXPORTS">' + r.p.exports + "</td>" +
          '<td data-h="LAST CHANGE">' + esc(ago(r.last)) + "</td></tr>"
        );
      }).join("") +
      "</tbody></table>";
    return h;
  }
  function draw() {
    if (!box) return;
    var u = me(),
      h = '<div class="lt">BCM ADMIN</div>';
    if (u && !u.anon) h += '<div class="lh">Signed in as ' + esc(u.email || u.name) + ' · <button type="button" class="lnk sm" data-a="out">Sign out</button></div>';
    if (!u || u.anon)
      h += "<p>Sign in with " + ADMIN + " to see how BCM’s live projects are used.</p>" + '<div class="lrow"><button type="button" class="btn" data-a="in">Sign in with Google</button></div>';
    else if (!isAdmin()) h += "<p>This page is only for the BCM administrator. Sign out, then sign in with " + ADMIN + ".</p>";
    else {
      h +=
        '<div class="lrow" style="margin:4px 0 10px"><span class="lh">' + (st.busy ? "Reading…" : st.at ? "Updated " + ago(st.at) : "") +
        ' · <button type="button" class="lnk sm" data-a="ref">Refresh</button></span></div>';
      st.at && (h += viewData());
      h +=
        '<div class="lh" style="margin-top:12px">Counts only. Nobody answering is named, and no answers or notes are shown here. ' +
        "The solo version is not counted: those workbooks stay on each person’s device. For visits to the page, use Webador’s own statistics.</div>";
    }
    st.msg && (h += '<div class="lmsg" role="status">' + esc(st.msg) + "</div>");
    box.innerHTML = h;
  }
  function onClick(ev) {
    var b = ev.target.closest("[data-a]");
    if (!b) return;
    var k = b.getAttribute("data-a");
    if (k === "in")
      window.gsmF8
        .signInLead()
        .then(function () {
          draw();
          isAdmin() && load();
        })
        .catch(function (e) {
          st.msg = errText(e);
          draw();
        });
    else if (k === "out") window.gsmF8.signOut().then(function () { st.at = 0; st.P = []; st.W = []; draw(); });
    else if (k === "ref") load();
  }
  var CSS =
    "#gsm-admin{border:1.5px solid #222;padding:14px 16px;margin:14px 0 4px;font-size:14.5px;line-height:1.45;background:#fff}" +
    "#gsm-admin .lt{font-weight:700;letter-spacing:.14em;font-size:12px;margin:0 0 8px}#gsm-admin .lh{font-size:12.5px;color:#666;margin:3px 0 0}" +
    "#gsm-admin .lrow{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin:8px 0}#gsm-admin .lmsg{color:#a33;margin:8px 0;font-size:13.5px}" +
    "#gsm-admin .agrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(120px,1fr));gap:8px;margin:4px 0 8px}" +
    "#gsm-admin .ast{border:1px solid #bbb;padding:8px 10px}#gsm-admin .ast b{display:block;font-size:22px;line-height:1.1}#gsm-admin .ast span{font-size:12px;color:#555}" +
    "#gsm-admin table.ewb{width:100%;border-collapse:collapse;font-size:13.5px;margin:12px 0 4px}" +
    "#gsm-admin .ewb th{text-align:left;font-size:10.5px;letter-spacing:.12em;font-weight:700;color:#444;border-bottom:1.5px solid #222;padding:5px 8px 5px 0;vertical-align:bottom}" +
    "#gsm-admin .ewb td{border-bottom:1px solid #ddd;padding:7px 8px 7px 0;vertical-align:top}#gsm-admin .ewb .ev{display:block;color:#666;font-size:12.5px}" +
    "#gsm-admin .enow{display:inline-block;font-size:10px;letter-spacing:.1em;font-weight:700;border:1px solid #2f5d2f;color:#2f5d2f;padding:0 4px;margin-left:5px;vertical-align:1px}" +
    "@media(max-width:620px){#gsm-admin .ewb thead{display:none}#gsm-admin .ewb,#gsm-admin .ewb tbody,#gsm-admin .ewb tr,#gsm-admin .ewb td{display:block;width:100%}" +
    "#gsm-admin .ewb tr{border-top:1.5px solid #222;padding:6px 0}#gsm-admin .ewb td{border:0;padding:2px 0;display:flex;gap:8px}" +
    "#gsm-admin .ewb td[data-h]:before{content:attr(data-h);flex:0 0 104px;font-size:10.5px;letter-spacing:.12em;font-weight:700;color:#555;padding-top:2px}}" +
    "@media print{#gsm-admin{display:none}}";
  function start() {
    var host = document.getElementById("gsm"),
      after = host && host.querySelector(".dsc");
    if (!after || !window.gsmF8 || !document.getElementById("gsm-ways")) return false;
    var css = document.createElement("style");
    css.textContent = CSS;
    document.head.appendChild(css);
    box = document.createElement("div");
    box.id = "gsm-admin";
    after.parentNode.insertBefore(box, after.nextSibling);
    box.addEventListener("click", onClick);
    try {
      window.gsmTab && window.gsmTab(5);
    } catch (e) {}
    st.msg = "";
    box.innerHTML = '<div class="lt">BCM ADMIN</div><div class="lh">Opening…</div>';
    window.gsmF8
      .load()
      .then(function () {
        draw();
        isAdmin() && load();
      })
      .catch(function (e) {
        st.msg = errText(e);
        draw();
      });
    return true;
  }
  var n = 0,
    t = setInterval(function () {
      (start() || ++n > 120) && clearInterval(t);
    }, 250);
})();

/* v313: F8 step 6 - reading everyone together (#bcmread=pid).''')

open(P, 'w', encoding='utf-8').write(s)
print('ok')
