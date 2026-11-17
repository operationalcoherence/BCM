# v185 (preview only) — 2026-11-17

From his note on v184: "put the legends back as they were in Taking Action; put the legend in full-screen mode, exactly as in Pattern Synthesis."

1. **Taking Action legends are back as they were before v184.** Each card's legend sits under its map again, on strategy and program cards alike. The v184 copy kept outside the 3D box is gone.
2. **Full screen on a strategy or program card now shows the legend the way full-screen Pattern Synthesis does:** a drawer on the left with Hide legend / Legend, the map beside it, and THE BEAR CANYON METHOD · BY OPERATIONAL COHERENCE at the bottom right. The legend under the map hides while the card is full screen (the drawer has it) and returns on Close full screen.

Files: `tools/patches/v185_legends_back_fullscreen_drawer.py` (engine), `tools/relief/relief.js` (drawer in card full screen) → `gsm-preview.js`, `gsm-relief.js`.

Checked: matrix on the 11 synthetic workbooks (the 2 built from his real workbook need it attached); with 3D loaded (swiftshader), all 7 clinic cards show their legend under the map; card full screen opens the drawer (legend text present, map shifted 340px), Hide legend closes it, Close full screen restores the inline legend; Pattern Synthesis full screen unchanged. Also run on his 11-13 workbook: matrix clean; all 8 card maps show their legend; card full screen opens the drawer.

No new wording.
