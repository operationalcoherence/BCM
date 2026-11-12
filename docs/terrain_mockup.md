# Terrain mock-up for Pattern Synthesis (2026-11-12)

`mockups/terrain.html` is a standalone page, separate from `gsm-preview.js`. It does not change the workbook or the live site.

It draws a raised-relief model from a workbook's line-map notes:

- **Ground:** colored by emotion. Acceptance raises it; aggression, distrust and defiance sink it; indifference makes it roll.
- **Trail:** runs from the present to the goal. The goal sits on a flat pad.
- **Questions:** signposts for Q.1–Q.7, placed at the middle of each question's notes.
- **Phrase loops:** shown when you tap a note or signpost.
- **Cause and effect:** arcs that use the engine's layer 26 rule.
- **What the ground says:** the page ranks what stands out (where a cause loop is fed, stuck places, contested or firm phrases, firm ground) and puts a numbered marker on the ground for each, with the reading listed under the model. Nothing has to be found by clicking. Each stuck place, firm place, phrase, cause loop and tapped note gets a plain sentence, read against the ground, the trail and the goal. Every sentence comes from fixed rules, with no AI. When a reading depends on whether a note is for or against a phrase ("away from aggressive suppression"), the page asks with one tap.

- **Legend:** a map legend in the corner of the model (the Legend button hides it).
- **Courses of action:** pick any Taking Action card and the model draws its way forward on the ground. A program gets one way, through its notes, and a reading of whether the ground holds for a program. A strategy gets its own way plus up to two others drawn from the same card: through its notes on firm ground only, and starting from the support its first move names. Each way says how much of it is on raised or sunk ground, which stuck places it passes through, and how it compares with the others. The cards are taken from the engine's own output. In this mock-up they are built in for the clinic sample only. Inside the workbook they would come from Taking Action directly.

Open it in a browser and use "Load your saved workbook…" to see your own data. Only made-up sample workbooks are built in. Real workbooks are kept out of this public repository.

Rules, decisions and open questions are in the project doc `claude/terrain_model.md`.
