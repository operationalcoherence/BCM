# v245 (preview only) — 2026-11-19

Fix for v244. His report (11-19 12:18), a screenshot of Broadview's Synthesis showing the old flat drawing with HELP, HINDER, PRESENT, and the line-map legend: "you have reverted back: I have no idea what this is."

**Cause (Claude's bug in v244):** the place tour's stop "Notes with no emotion yet" has no spot on the map. The 3D reads a spot for every Synthesis stop, so on any place map with a note that has no emotion (Broadview has 6), the 3D failed to start and the page fell back to the flat line-map drawing. The v244 test workbook had an emotion on every note, so the test missed it.

**Fix:** that stop now goes in the tour's opening, which allows a stop with no spot. The fix is in v244's patch script (amended); this version only bumps the label.

**Checked on Broadview** (rebuilt from the project copy as tests/broadview.json, which stays out of git): the 3D starts on Analysis, Synthesis, and Taking Action, and the flat drawing shows nowhere. Both tours play through, opening with "Notes with no emotion yet: 6 notes have no emotion marked yet (the white pins)". There are no errors. Matrix clean on all workbooks plus Broadview. Keys: none.

**Rule for next time:** test every place change on Broadview (notes with no emotion, drawn areas, repeated notes), not only on synthetic place maps.
