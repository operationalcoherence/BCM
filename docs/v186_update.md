# v186 (preview only) — 2026-11-17

From the handoff's next step (D1, his question 3 on 11-17): the Esri place map as the ground.

1. **A place-map workbook now gets the 3D map.** Before, a workbook with only place-map notes (Broadview) had no 3D map anywhere. Now Pattern Analysis, Pattern Synthesis, In Parallel and every Taking Action card show one.
   - Each place note stands where you put it. North is at the back.
   - The goal stands at the location you found on Mapping Context.
   - The relief is gentle: the emotions still raise and lower the ground, but only a little.
2. **The ground is the Esri satellite image**, with roads and place names on top, and the emotion color laid over it translucently. Where no notes are near, the image shows plain.
3. **Areas you drew on the place map are shaded patches** in their emotion's color, with a white edge (on Broadview, N13 and N14).
4. **On a place there is no help/hinder line**, so:
   - the HELP, HINDER, PRESENT and FUTURE labels are off;
   - the green flag (START) is the note farthest from the goal, and the ways run from there to the goal;
   - a note counts as hindering when it answers Q.1 or Q.2.
5. A workbook with line-map notes is unchanged; it still uses the line map.

**New wording (Claude's), for his review:**
- START tip: "The note farthest from the goal. The ways run from here to the goal."
- Legend: "Shaded patches: areas you drew on the place map, in their emotion's color."
- Legend: "Satellite image without color: no notes nearby, so no information here."
- Legend: "Pins are notes in their emotion's color, where you placed them; black flags are questions. The green flag (START) is the note farthest from the goal; the checkered flag is the goal, at [location]. North is at the back."

**Credit:** "Imagery © Esri, Maxar, Earthstar Geographics, and the GIS User Community · Powered by Esri" sits at the bottom left of the map once the imagery has loaded.

**How:**
- `gsmData()` projects the place notes (Web Mercator) into the module's 340 × 230 frame when no line note has text. The frame is fitted to the notes, their areas and the location, at least 250 m across, with a margin.
- The relief loads Esri tiles at zoom 17–18 (up to 64 tiles per layer): World_Imagery, plus the Reference/World_Transportation and Reference/World_Boundaries_and_Places layers. It sends no key; the place map already loads the same tiles this way.
- If the tiles fail, the old painted ground stays and the credit is hidden.

**Checked:**
- Broadview, with stand-in tiles: maps on all four places, patches visible, credit shown. With failing tiles: painted ground, no errors.
- His 11-13 workbook: identical word counts on every tab; legends and card full screen as in v185.
- 11 synthetic workbooks: matrix clean. Keys: none.

**Not checked:** real Esri tiles. The sandbox cannot reach Esri, so look at the preview. If the ground stays painted there, the tiles were refused, and the browser console will say why.

**Not done:** the canvas fallback (no WebGL) still draws the line-map trail and labels on a place workbook.
