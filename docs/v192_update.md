# v192 (preview only) — 2026-11-17

F3 (action friction field) and F5 (synthetic bridging across bare rock faces), his pick after A2.

**How the ways forward now weigh the ground they cross** (route stats, `routeStats` in the terrain module):
- **Friction (F3):** each step of a way costs by the emotion holding the ground there, weighted by how strongly the notes hold it: acceptance 0.2, indifference 0.5, distrust 1.0, aggression 1.4, defiance 1.8. Ground no note reaches counts 0.3. The total is divided by the straight run from START to the goal.
- **Boomerang risk (F3):** the way enters aggression or defiance ground directly, without passing indifference first.
- **Rock faces (F5):** each crossing of a bare rock face (two emotions two or more steps apart, with no indifference between them; the same test that paints the rock on the map) adds the distance between the two emotions. A face crossed back and forth counts each time and is named once.
- **Effort** = climb + 0.15 × length ratio + 0.6 × friction + 0.5 × rock faces. Return on effort follows.

**On the cards (every strategy card's ways, on line and place maps alike):**
- Each "X: why choose it" adds, when it applies:
  - "It crosses [a bare rock face / N bare rock faces] (N2, aggression, against N6, acceptance; …), where two distant emotions meet with no indifference between them. That is the costliest ground to act on. A bridge there would be something both sides can first be indifferent to."
  - "Boomerang risk: it goes straight into defiance at N29 without passing indifference first, so pushing there can turn people further against the goal."
- COMPARE THE WAYS IN A CHART:
  - two new rows: "Friction: How hard the emotional ground is to act on along the way: acceptance costs least, defiance most." and "Rock faces: Bare rock faces the way crosses, weighted by how far apart the two emotions are.";
  - Effort now reads "The energy it takes: climbing, friction and rock faces together."

All of the above wording is Claude's, for his review. The weights are a first setting, relative to his own map, not a standard measure.

**Checked:**
- 11-13: every strategy card. On one card, way A crosses 3 faces and has boomerang risk at N29; way B crosses 1 face and has boomerang risk at N9.
- Broadview: the strategy card shows the same.
- 13 workbooks: matrix clean. 3D cards and full screen, Broadview terrain, T5 boxes: unchanged.

**For his call:**
- The weights (friction per emotion; 0.6 and 0.5 in effort).
- Should boomerang risk also lower Impact?
- On a place map, "climbs" in these readings means the emotion ground, not the real hills (same open question as v189).
