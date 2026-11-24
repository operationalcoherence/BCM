# v265: attribution drawn into the 3D picture itself (BCM_TASK_QUEUE.md, "Attribution on every full-screen view";
# his words 11-23 12:20: "The Bear Canyon Method by Operational Coherence", "in a spot that cannot be snipped by
# screenshots but does not interfere with using the tool").
# The line is lettered on the front face of the block, under the ground, like the label on a physical relief model.
# It is part of the 3D scene, so any picture of the block carries it, in every 3D view (Analysis, Synthesis, In Parallel,
# Taking Action card maps, the tour, full screen or not) and on place maps. It sits below the lowest point of the front
# edge, so it never covers a note, a label, the goal, or a button. The page's own brand line stays as it was.
p = "tools/relief/relief.js"
s = open(p, encoding="utf-8").read()
old = "  Object.values(ed).forEach(p => { const m = new THREE.Mesh(wallStrip(p), sideMat); m.receiveShadow = true; scene.add(m); });"
assert s.count(old) == 1
s = s.replace(old, old + """
  /* v265: the attribution, lettered on the front face of the block, below the lowest point of its top edge */
  { let top = 1e9; ed.s.forEach(p => { top = Math.min(top, gH(p[0], p[1])); }); const room = top - BASE;
    if (room > 1.5) { const cv = document.createElement('canvas'); cv.width = 2048; cv.height = 96; const g = cv.getContext('2d');
      g.fillStyle = '#d8d4cc'; g.textAlign = 'center'; g.textBaseline = 'middle'; g.font = '600 52px Helvetica, Arial, sans-serif';
      const T = 'The Bear Canyon Method by Operational Coherence'; if ('letterSpacing' in g) g.letterSpacing = '4px'; g.fillText(T, 1024, 50);
      const tw = Math.min(2040, g.measureText(T).width + 40), th = Math.min(room * 0.42, 9), pw = th * cv.width / cv.height * 0.98;
      const tt = new THREE.CanvasTexture(cv); tt.colorSpace = THREE.SRGBColorSpace; tt.anisotropy = 8;
      const sign = new THREE.Mesh(new THREE.PlaneGeometry(Math.min(pw, W * 0.9), th), new THREE.MeshBasicMaterial({ map: tt, transparent: true, opacity: 0.85, depthWrite: false }));
      if (pw > W * 0.9) sign.scale.y = W * 0.9 / pw; sign.position.set(0, BASE + room * 0.5, H / 2 + 0.25); if (th >= 4) scene.add(sign); }
    /* where the front face is too low to letter (flat or gentle ground, as on many place maps), the line lies on the base in front of it */
    if (!(room > 1.5) || Math.min(room * 0.42, 9) < 4) { const cv = document.createElement('canvas'); cv.width = 2048; cv.height = 96; const g = cv.getContext('2d');
      g.fillStyle = '#55524c'; g.textAlign = 'center'; g.textBaseline = 'middle'; g.font = '600 52px Helvetica, Arial, sans-serif'; if ('letterSpacing' in g) g.letterSpacing = '4px';
      g.fillText('The Bear Canyon Method by Operational Coherence', 1024, 50); const tt = new THREE.CanvasTexture(cv); tt.colorSpace = THREE.SRGBColorSpace; tt.anisotropy = 8;
      const th = 7, pw = Math.min(th * cv.width / cv.height * 0.98, W * 0.9), mat = new THREE.MeshBasicMaterial({ map: tt, transparent: true, opacity: 0.85, depthWrite: false });
      const flat = new THREE.Mesh(new THREE.PlaneGeometry(pw, th * pw / (th * cv.width / cv.height * 0.98)), mat); flat.rotation.x = -Math.PI / 2; flat.position.set(0, BASE + 0.05, H / 2 + 8); scene.add(flat); } }""", 1)
open(p, "w", encoding="utf-8").write(s)
p = "gsm-readable.js"; s = open(p, encoding="utf-8").read()
assert s.count('t.textContent = "v264"') == 1
s = s.replace('t.textContent = "v264"', 't.textContent = "v265"'); open(p, "w", encoding="utf-8").write(s)
