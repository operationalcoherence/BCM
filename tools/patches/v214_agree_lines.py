"""v214: THE TWO PICTURES, SIDE BY SIDE drawn with lines (his call, 11-18 14:09: "use lines"), as on the chosen
artboard ("Chosen: lines (11-18)").
1. One thin line from each word to every note that carries it: solid black where the ground agrees with Analysis,
   dashed red where the ground raises a question. No hoses.
2. The box shows what Analysis found: black = contested; dashed outline = a gap that what you would design does
   not reach; teal outline = support nothing uses yet; grey outline = in what you would design with no cause behind
   it (and the two other ask kinds).
3. A key under the figure for the boxes and the lines (it replaces the key in the column).
4. On the 3D map above, a tapped word's lines are thin too: solid black, or dashed red.
Usage: python3 v214_agree_lines.py tools/relief/relief.js --relief   and   python3 v214_agree_lines.py gsm-readable.js"""
import sys

P = sys.argv[1]
RELIEF = "--relief" in sys.argv
s = open(P).read()


def rep(a, b, n=1):
    global s
    c = s.count(a)
    assert c == n, (c, a[:90])
    s = s.replace(a, b)


if RELIEF:
    rep(
        """        const c = new THREE.CatmullRomCurve3(pts), tube = new THREE.Mesh(new THREE.TubeGeometry(c, n * 4, 1.5, 8), new THREE.MeshStandardMaterial({ color: white ? '#f4f4f4' : '#111111', roughness: 0.45, emissive: white ? '#ffffff' : '#000000', emissiveIntensity: white ? 0.35 : 0 }));
        tube.castShadow = true; HOSES.add(tube); hoseN++;
        if (white) HOSES.add(new THREE.Mesh(new THREE.TubeGeometry(c, n * 4, 1.9, 8), new THREE.MeshStandardMaterial({ color: '#222', side: THREE.BackSide }))); } }""",
        """        /* v214: thin lines; a question is dashed red */
        const c = new THREE.CatmullRomCurve3(pts), segs = white ? Math.max(4, Math.round(c.getLength() / 6)) : 1;
        for (let q = 0; q < segs; q += white ? 2 : 1) { const sp = []; for (let k = 0; k <= 8; k++) sp.push(c.getPoint((q + k / 8) / segs));
          HOSES.add(new THREE.Mesh(new THREE.TubeGeometry(new THREE.CatmullRomCurve3(sp), white ? 8 : n * 4, 0.85, 6), new THREE.MeshStandardMaterial({ color: white ? '#b3261e' : '#111111', roughness: 0.5, emissive: white ? '#5a0d08' : '#000000', emissiveIntensity: white ? 0.35 : 0 }))); }
        hoseN++; } }""",
    )
else:
    rep(
        """        mk("path", { d: d, transform: "translate(2 3)", stroke: "#000", "stroke-opacity": 0.22, "stroke-width": 6, fill: "none", "stroke-linecap": "round" }, o.g);
        o.ok
          ? mk("path", { d: d, stroke: "#1a1a1a", "stroke-width": 4.2, fill: "none", "stroke-linecap": "round" }, o.g)
          : (mk("path", { d: d, stroke: "#222", "stroke-width": 6, fill: "none", "stroke-linecap": "round" }, o.g),
            mk("path", { d: d, stroke: "#f4f4f4", "stroke-width": 3.8, fill: "none", "stroke-linecap": "round" }, o.g));
        mk("path", { d: d, transform: "translate(-.8 -1.2)", stroke: "#fff", "stroke-opacity": o.ok ? 0.3 : 0.9, "stroke-width": 1.2, fill: "none", "stroke-linecap": "round" }, o.g);""",
        """        o.ok
          ? mk("path", { d: d, stroke: "#111", "stroke-width": 1.4, fill: "none" }, o.g)
          : mk("path", { d: d, stroke: "#b3261e", "stroke-width": 1.6, "stroke-dasharray": "5 4", fill: "none" }, o.g);""",
    )
    rep(
        """    mk("rect", { x: 10, y: VH - 30, width: 12, height: 9, fill: "#111" }, svg);
    mk("text", { x: 27, y: VH - 22, "font-size": 10, fill: "#333" }, svg).textContent = "the ground agrees";
    mk("rect", { x: 10, y: VH - 16, width: 12, height: 9, fill: "#fff", stroke: "#111" }, svg);
    mk("text", { x: 27, y: VH - 8, "font-size": 10, fill: "#333" }, svg).textContent = "the ground asks";""",
        "",
    )
    rep(
        """      o.box = mk("rect", { x: 8, y: o.y - bh / 2, width: 160, height: bh, rx: 2, fill: o.ok ? "#111" : "#fff", stroke: "#111", "stroke-width": 1.5 }, gw);
      L.forEach(function (l, k) {
        var t = mk("text", { x: 16, y: o.y - bh / 2 + 17 + 14 * k, "font-size": 12.5, fill: o.ok ? "#fff" : "#111" }, gw);""",
        """      var BX = { c: ["#111", "#111", "", "#fff"], g: ["#fff", "#111", "5 3", "#111"], u: ["#fff", "#1f6f66", "", "#1f6f66"] }[o.kind] || ["#fff", "#777", "", "#444"];
      o.box = mk("rect", { x: 8, y: o.y - bh / 2, width: 160, height: bh, rx: 2, fill: BX[0], stroke: BX[1], "stroke-width": 1.5, "stroke-dasharray": BX[2] }, gw);
      L.forEach(function (l, k) {
        var t = mk("text", { x: 16, y: o.y - bh / 2 + 17 + 14 * k, "font-size": 12.5, fill: BX[3] }, gw);""",
    )
    rep(
        """'<div class="agsub">Pattern Analysis keeps its own column; the hoses carry each of its words onto the Synthesis ground, to the notes that use it. A <b>black hose</b>: the ground agrees with what Analysis found. A <b>white hose</b>: the ground raises a question about it. Tap a word to follow it here and on the 3D map above.</div>';""",
        """'<div class="agsub">Pattern Analysis keeps its own column; a line runs from each of its words to every note on the Synthesis ground that carries it. A <b>solid black line</b>: the ground agrees with what Analysis found. A <b>dashed red line</b>: the ground raises a question about it. Tap a word to follow it here and on the 3D map above.</div>';""",
    )
    rep(
        """    rd.textContent = "Tap a word to read what both pictures say about it.";
    wrap.appendChild(rd);""",
        """    rd.textContent = "Tap a word to read what both pictures say about it.";
    var ky = document.createElement("div");
    ky.className = "agkey";
    ky.innerHTML =
      '<span><i style="background:#111;border-color:#111"></i>contested: resisted and supported</span><span><i style="border-style:dashed"></i>a gap: what you would design does not reach it</span><span><i style="border-color:#1f6f66"></i>support nothing uses yet</span><span><i style="border-color:#777"></i>designed with no cause behind it, or read differently by the two pictures</span><span><b style="border-top:1.5px solid #111"></b>the ground agrees</span><span><b style="border-top:1.6px dashed #b3261e"></b>the ground raises a question</span>';
    wrap.appendChild(ky);
    wrap.appendChild(rd);""",
    )
    rep(
        """#gsm .agread .lnk{margin-left:4px}";""",
        """#gsm .agread .lnk{margin-left:4px}#gsm .agkey{display:flex;flex-wrap:wrap;gap:4px 16px;font-size:12.5px;color:#333;margin:8px 0 0}#gsm .agkey span{display:inline-flex;align-items:center;gap:6px}#gsm .agkey i{display:inline-block;width:20px;height:11px;border:1.5px solid #111;background:#fff}#gsm .agkey b{display:inline-block;width:24px;height:0}";""",
    )
    s = s.replace('t.textContent = "v213"', 't.textContent = "v214"')
    assert 't.textContent = "v214"' in s
open(P, "w").write(s)
