# v323 · project clusters on the lead's project map (preview)

Lead's combined copy only (window.gsmRead), Pattern Analysis, YOUR LANDSCAPE, ONE QUESTION AT A TIME:
- Notes in a cluster: dots on short stems, in the emotion's colour with a white rim; a dashed ring on the ground around them; a tag
  (number, what it is about, how many people). Every other note: a faint dot. No note labels.
- Under the map: HOW GATHERED THE PROJECT IS (share of notes in clusters, each emotion gathered or spread), CLUSTERS (tap one: its
  notes open and the others fade on the map; tapping a tag on the map does the same), Early threads (folded), HOW NOTES ARE MATCHED.
- Engine: tools/clusters/clusters.js, copied into gsm-readable.js as window.gsmClusters (keep the two the same).
- Solo workbooks: unchanged (screenshot pixel-identical to v322). gsm-relief.js changes do nothing unless the page sends clusters,
  so the live page is unaffected.
- Not in this version: voice and question filters for clusters, WHERE PEOPLE FALL TOGETHER, the AI match, the 2D fallback map.
Test: tests/clustershot.py PREVIEW.js RELIEF.js tests/fuel_break_20.json OUT [width] [solo]
