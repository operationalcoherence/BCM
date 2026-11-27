"""v319: a privacy screen for each role, not one general one (Gregory, 26 Nov 19:35: "it doesnt have any
uniqueness to each function").
- WORKING ON YOUR OWN: what stays on the device, and the file you choose to send.
- ANSWERING an invite: names the project and its lead ("Test Lead sees everything you write here"), what is sent and
  how often, who else can and can't see it, what the lead can do with it, and what stays in the person's hands.
  Waits behind a blocking "Opening the project..." screen until the invite has been read.
- LEADING a project: the lead holds other people's words; what that asks of them; deleting the project deletes
  everyone's workbooks; copies they save are theirs to look after; who holds the invite link can answer.
- Each role is acknowledged on its own (solo, join, lead). Records: data.privacy = join, project privacy = lead.
- The full page has a section for each role.
Run from the repository root:  python3 tools/patches/v319_privacy_by_role.py"""
P = 'gsm-readable.js'
s = open(P, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (c, old[:80]); s = s.replace(old, new)

rep('t && (t.textContent = "v318");', 't && (t.textContent = "v319");')
rep('json: s, privacy: window.gsmPrivacy ? window.gsmPrivacy.rec("live") : null }', 'json: s, privacy: window.gsmPrivacy ? window.gsmPrivacy.rec("join") : null }')
rep('privacy: window.gsmPrivacy ? window.gsmPrivacy.rec("live") : null', 'privacy: window.gsmPrivacy ? window.gsmPrivacy.rec("lead") : null', 2)
rep('''          if (window.gsmPrivacy && window.gsmPrivacy.need("live"))
            return window.gsmPrivacy.show("live", function () {''', '''          if (window.gsmPrivacy && window.gsmPrivacy.need("lead"))
            return window.gsmPrivacy.show("lead", function () {''')

# the invite, once read, tells the privacy screen whose project this is
rep('''        inv = x;
        if (me && inv.goal != null) {''', '''        inv = x;
        window.gsmJoinInfo = { name: inv.name || "", lead: inv.leadName || "", due: inv.due || "" };
        if (me && inv.goal != null) {''')
rep('''          st.msg = "This invite link doesn’t work. Ask the lead for a new one.";
          inv = null;''', '''          st.msg = "This invite link doesn’t work. Ask the lead for a new one.";
          window.gsmJoinInfo = { gone: true };
          inv = null;''')

i = s.index('/* v318: the privacy screen.')
s = s[:i] + r'''/* v318, v319: the privacy screen, one for each role. Nobody works until they have pressed "I understand".
   Roles: solo (working on your own), join (answering an invite), lead (leading a project). Each is asked again
   only when its version changes. Recorded in groundsmith-web-privacy. */
!(function () {
  var V = "2026-11-26.2",
    DATE = "2026-11-26",
    KEY = "groundsmith-web-privacy",
    ADMIN = /[?&#]bcmadmin\b/.test(location.search + location.hash),
    gate = null,
    lastFocus = null;
  function get() {
    try {
      return JSON.parse(localStorage.getItem(KEY) || "null") || {};
    } catch (e) {
      return {};
    }
  }
  function need(kind) {
    var r = get()[kind];
    return !(r && String(r.v) >= V);
  }
  function rec(kind) {
    var r = get()[kind];
    return r && r.v ? { v: String(r.v), at: r.at || null } : null;
  }
  function mark(kind) {
    var all = get();
    all[kind] = { v: V, at: new Date().toISOString() };
    try {
      localStorage.setItem(KEY, JSON.stringify(all));
    } catch (e) {}
  }
  function esc(t) {
    return String(t == null ? "" : t).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }
  var SERVICES =
    "Place search, maps, terrain, fonts, and code come from outside services: Esri, OpenStreetMap, Photon, Amazon Web Services, Google Fonts, cdnjs, and jsDelivr. They see your device’s internet address, as any website does, and a place search sends the words you type. None of them receive your goal, answers, or notes.";
  function solo() {
    return {
      h: "WORKING ON YOUR OWN: YOUR PRIVACY",
      d: "Please read this before you start your workbook.",
      L: [
        ["Your workbook stays on this device.", "Your goal, answers, notes, and maps are saved only in this browser. Nothing is sent to Operational Coherence or anyone else, and nobody signs in. We cannot see your work."],
        ["Only a file you choose leaves it.", "Save workbook downloads a file. You decide whether to keep it, send it to someone, or combine it with theirs. Once you send it, it is in the hands of whoever you send it to."],
        ["Clearing your browser erases it.", "Clearing this browser’s data, or using a private window, removes the copy kept here. Save a file to keep your work."],
        ["Some outside services are used.", SERVICES]
      ]
    };
  }
  function join(I) {
    var P = I && I.name ? "“" + I.name + "”" : "this project",
      Ld = I && I.lead ? I.lead : "The lead",
      ld = I && I.lead ? I.lead : "the lead";
    return {
      h: "BEFORE YOU ANSWER " + (I && I.name ? "“" + I.name.toUpperCase() + "”" : "THIS PROJECT"),
      d: "You were invited to answer in a shared project. Here is what happens to what you write.",
      L: [
        [Ld + " sees everything you write here.", "Your name, your voice, your answers, notes, and maps go to " + ld + " as you work, about every 30 seconds. " + Ld + " can read your workbook, read it together with everyone else’s, and save a copy of it as a file."],
        ["It is saved online.", "In Google Firebase, a database service, in the United States. It stays there until " + ld + " deletes " + P + ", or you delete it yourself."],
        ["Who else can see it.", "The BCM administrator at Operational Coherence, who can read it to look after the service. The other people invited to " + P + " cannot see your workbook."],
        ["You stay in control.", "You need no account. Pause sharing stops sending at any time. Delete my workbook removes it from " + P + " and from this device, for good. A copy " + ld + " has already saved as a file is theirs, and BCM can’t delete it."],
        ["Your own workbook stays apart.", "If you have a workbook of your own on this device, it is never sent. It comes back when you open the page without the invite link."]
      ],
      x: "Don’t write anything you wouldn’t want " + ld + " to read."
    };
  }
  function lead() {
    return {
      h: "BEFORE YOU LEAD A PROJECT",
      d: "Leading a project means holding other people’s words. Here is what that involves.",
      L: [
        ["You sign in with Google.", "Your Google name (or your email, if there is no name) is kept on the project and shown to everyone you invite."],
        ["People send you what they write.", "Everyone who answers through your invite link sends you their name, their voice, and their answers, notes, and maps, as they work. Use them for this project only, and tell people before they start what you will do with them."],
        ["It is saved online until you delete the project.", "In Google Firebase, in the United States. Deleting the project deletes every workbook in it, for good. You can also delete any one workbook."],
        ["Copies you make are yours to look after.", "Save as a file puts a person’s workbook on your device. BCM can’t delete those copies; you are responsible for them."],
        ["Your invite link lets people in.", "Anyone holding it can answer. Share it only with the people you mean to ask. Stop taking answers closes it."],
        ["Who else can see it.", "The BCM administrator at Operational Coherence, who can read projects and workbooks to look after the service. The people you invite can’t see each other’s workbooks, and each of them can pause or delete their own at any time."]
      ]
    };
  }
  function list(L) {
    return L.map(function (x) {
      return "<p><b>" + esc(x[0]) + "</b> " + esc(x[1]) + "</p>";
    }).join("");
  }
  function full() {
    var j = join(null),
      l = lead(),
      o = solo();
    return (
      '<div class="pvh" id="gsm-privh">THE BEAR CANYON METHOD · PRIVACY</div><div class="pvd">Last changed ' + esc(new Date(DATE + "T12:00:00").toLocaleDateString(undefined, { month: "long", day: "numeric", year: "numeric" })) + ".</div>" +
      '<div class="pvs">WORKING ON YOUR OWN</div>' + list(o.L.slice(0, 3)) +
      '<div class="pvs">ANSWERING AN INVITE</div>' + list(j.L) + "<p>" + esc(j.x) + "</p>" +
      '<div class="pvs">LEADING A PROJECT</div>' + list(l.L) +
      '<div class="pvs">OUTSIDE SERVICES</div><p>' + esc(SERVICES) + "</p>" +
      '<div class="pvs">WHAT WE DON’T DO</div><p>We don’t sell or share what you write, show advertising, or use what you write for anything but running BCM.</p>' +
      '<div class="pvs">WHEN THIS CHANGES</div><p>You are asked to read it again before you can carry on.</p>' +
      '<div class="pvs">QUESTIONS</div><p>Write to <a href="mailto:greg@operationalcoherence.com">greg@operationalcoherence.com</a>.</p>'
    );
  }
  var CSS =
    "#gsm-priv{position:fixed;inset:0;z-index:2147483600;background:rgba(20,20,20,.55);display:flex;align-items:center;justify-content:center;padding:14px;box-sizing:border-box;font-family:'Questrial',sans-serif;color:#222}" +
    "#gsm-priv .pvb{background:#fff;border:1.5px solid #222;max-width:600px;width:100%;max-height:100%;overflow:auto;padding:18px 20px 16px;box-sizing:border-box;font-size:15px;line-height:1.5;-webkit-overflow-scrolling:touch}" +
    "#gsm-priv .pvh{font-weight:700;letter-spacing:.14em;font-size:12.5px;margin:0 0 4px}#gsm-priv .pvd{font-size:13.5px;color:#555;margin:0 0 12px}" +
    "#gsm-priv .pvs{font-weight:700;letter-spacing:.12em;font-size:11.5px;margin:16px 0 4px}#gsm-priv p{margin:0 0 10px}#gsm-priv a{color:#222}" +
    "#gsm-priv .pvx{border-left:3px solid #222;padding-left:10px}" +
    "#gsm-priv .pvr{display:flex;flex-wrap:wrap;gap:10px 16px;align-items:center;margin:14px 0 0}" +
    "#gsm-priv .pvok{border:1px solid #111;background:#111;color:#fff;font:16px 'Questrial',sans-serif;padding:12px 22px;min-height:44px;cursor:pointer;letter-spacing:.03em}" +
    "#gsm-priv .pvlnk{background:none;border:0;padding:0;font:13.5px 'Questrial',sans-serif;color:#222;text-decoration:underline;cursor:pointer}" +
    "html.gsm-privon,html.gsm-privon body{overflow:hidden!important}@media print{#gsm-priv{display:none}}";
  function ensureCss() {
    if (document.getElementById("gsm-privcss")) return;
    var c = document.createElement("style");
    c.id = "gsm-privcss";
    c.textContent = CSS;
    document.head.appendChild(c);
  }
  function close() {
    if (!gate) return;
    gate.remove();
    gate = null;
    document.documentElement.classList.remove("gsm-privon");
    var w = document.getElementById("gsm");
    w && (w.inert = false);
    lastFocus && lastFocus.focus && lastFocus.focus();
  }
  function trap(e) {
    if (!gate) return;
    if (e.key === "Escape") return void (e.preventDefault(), e.stopPropagation());
    if (e.key !== "Tab") return;
    var f = gate.querySelectorAll("button,a[href]");
    if (!f.length) return void e.preventDefault();
    var a = f[0],
      z = f[f.length - 1];
    if (e.shiftKey && document.activeElement === a) (e.preventDefault(), z.focus());
    else if (!e.shiftKey && document.activeElement === z) (e.preventDefault(), a.focus());
    else if (!gate.contains(document.activeElement)) (e.preventDefault(), a.focus());
  }
  function screen(kind) {
    var T = kind === "lead" ? lead() : kind === "join" ? join(window.gsmJoinInfo) : solo();
    return (
      '<div class="pvh" id="gsm-privh">' + esc(T.h) + '</div><div class="pvd">' + esc(T.d) + "</div>" + list(T.L) +
      (T.x ? '<p class="pvx">' + esc(T.x) + "</p>" : "") +
      '<div class="pvr"><button type="button" class="pvok" data-pv="ok">I understand</button><button type="button" class="pvlnk" data-pv="full">Read the full privacy page</button></div>'
    );
  }
  /* kind: "solo", "join" or "lead" asks for "I understand"; "full" is the full page, closed with Close;
     "wait" holds the page while the invite is read */
  function show(kind, done) {
    ensureCss();
    close();
    lastFocus = document.activeElement;
    gate = document.createElement("div");
    gate.id = "gsm-priv";
    gate.setAttribute("role", "dialog");
    gate.setAttribute("aria-modal", "true");
    gate.setAttribute("aria-labelledby", "gsm-privh");
    var body =
      kind === "full"
        ? full() + '<div class="pvr"><button type="button" class="pvok" data-pv="close">Close</button></div>'
        : kind === "wait"
          ? '<div class="pvh" id="gsm-privh">OPENING THE PROJECT…</div><div class="pvd">What happens to what you write comes up here in a moment.</div>'
          : screen(kind);
    gate.innerHTML = '<div class="pvb" tabindex="-1">' + body + "</div>";
    gate.addEventListener("click", function (e) {
      var b = e.target.closest && e.target.closest("[data-pv]");
      if (!b) return;
      var k = b.getAttribute("data-pv");
      if (k === "ok") {
        mark(kind);
        close();
        done && done();
      } else if (k === "full") {
        var bx = gate.querySelector(".pvb");
        bx.innerHTML = full() + '<div class="pvr"><button type="button" class="pvok" data-pv="ok">I understand</button></div>';
        bx.scrollTop = 0;
        bx.querySelector("[data-pv=ok]").focus();
      } else if (k === "close") close();
    });
    document.body.appendChild(gate);
    document.documentElement.classList.add("gsm-privon");
    var w = document.getElementById("gsm");
    w && (w.inert = true);
    var ok = gate.querySelector(".pvok") || gate.querySelector(".pvb");
    ok && ok.focus();
  }
  document.addEventListener("keydown", trap, true);
  window.gsmPrivacy = { V: V, need: need, rec: rec, show: show };
  function start() {
    var w = document.getElementById("gsm");
    if (!w) return false;
    var a = document.getElementById("gsm-privlink");
    a &&
      a.addEventListener("click", function (e) {
        e.preventDefault();
        gate || show("full");
      });
    if (ADMIN) return true;
    if (window.gsmJoin) {
      if (!need("join")) return true;
      /* wait for the invite, so the screen can name the project and its lead */
      show("wait");
      var n = 0,
        t = setInterval(function () {
          var I = window.gsmJoinInfo;
          if (I || ++n > 80) {
            clearInterval(t);
            I && I.gone ? close() : show("join");
          }
        }, 100);
      return true;
    }
    var kind = window.gsmRead ? "lead" : "solo";
    need(kind) && show(kind);
    return true;
  }
  var n = 0,
    t = setInterval(function () {
      (start() || ++n > 120) && clearInterval(t);
    }, 100);
})();
'''
open(P, 'w', encoding='utf-8').write(s)
print('ok')
