# Terrain mock-up for Pattern Synthesis (2026-11-12)

`mockups/terrain.html` is a standalone page, separate from `gsm-preview.js`. It does not change the workbook or the live site.

It draws a raised-relief model from a workbook's line-map notes:

- **Ground:** colored by emotion. Acceptance raises it; aggression, distrust and defiance sink it; indifference makes it roll.
- **Trail:** runs from the present to the goal. The goal sits on a flat pad.
- **Questions:** signposts for Q.1–Q.7, placed at the middle of each question's notes.
- **Phrase loops:** shown when you tap a note or signpost.
- **Cause and effect:** arcs that use the engine's layer 26 rule.
- **What it means:** each stuck place, firm place, phrase, cause loop and tapped note gets a plain sentence, read against the ground, the trail and the goal. Every sentence comes from fixed rules, with no AI. When a reading depends on whether a note is for or against a phrase ("away from aggressive suppression"), the page asks with one tap.

Open it in a browser and use "Load your saved workbook…" to see your own data. Only made-up sample workbooks are built in. Real workbooks are kept out of this public repository.

Rules, decisions and open questions are in the project doc `claude/terrain_model.md`.
