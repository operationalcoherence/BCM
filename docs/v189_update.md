# v189 (preview only) — 2026-11-17

From his note: Esri imagery shows no elevation on its own. He chose real terrain, true to scale.

1. **On a place map the ground is now the real terrain, true to scale.** Heights are meters divided by the map's meters per unit, so the land is neither stretched nor flattened. Emotion no longer raises or lowers the ground on a place; it shows only as color. This replaces v186's gentle emotion relief.
2. **Elevation comes from AWS Terrain Tiles** (Terrarium PNG, free and open; in the US the data is USGS 3DEP), at zoom 15 or less. Up to 36 tiles are fetched once per place, before the 3D scene is built, and shared by every map of that place.
   - If they cannot be loaded within 12 seconds, the ground is flat.
   - Esri's own elevation (Terrain3D) was not used: its tiles need a separate decoder (LERC/WebAssembly), and it may need a key.
3. **The place legend drops the heights.** The emotion rows read just "Acceptance", "Indifference", and so on. A new row reads: "The ground is the real terrain, true to scale. Emotion shows only as color." (Claude's wording, for his review.)
4. Line maps are unchanged: there, emotion is still the terrain.

**Checked:**
- Broadview with stand-in elevation tiles (synthetic hills around 2,300 m): the ground shows the slopes. With tiles failing: flat ground, imagery and color still there, no errors.
- His 11-13 workbook: cards, legends and full screen as in v185.
- 13 workbooks: matrix clean. Keys: none.

**Not checked:** real elevation tiles. The sandbox cannot reach AWS or Esri, so look at the preview.

**Open for him:**
- On a place map, the written readings (WHAT THE GROUND SAYS, the T5 "low ground" section, the high/low ground popovers) still speak of high and low ground. There it means the emotion ground, which now shows only as color. Should a place map say it differently (for example "the acceptance ground", "where distrust gathers")?
