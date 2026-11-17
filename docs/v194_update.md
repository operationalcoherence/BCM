# v194 (preview only) — 2026-11-17

F4, the reflexive loop: map, act, re-map (Maturana & Varela; Morin's ecology of action).

1. **WHAT YOU DID**, on every Taking Action card, under YOUR DECISION.
   - Write what you did and what happened, then press **Log it**. Entries stay on the card with the date and your name.
   - Logging flags the card's Q.1–Q.4 notes (why it has not taken root, opposition, support, conditions), the ones in the card's map, for re-mapping.
2. **SINCE YOU ACTED**, at the top of Mapping Landscape:
   - It quotes your last entry and lists the flagged notes, each with a **Done** button.
   - A note leaves the list once you edit it on the map or press Done.
   - It shows only on Mapping Landscape.
3. **In the workbook:**
   - `acts: [{k: card, t, w, x: text, n: note ids, l: labels}]`
   - `remap: {noteId: time}`
   - The edit log gets an "act" entry.
   - It works for line and place notes alike.

**New wording (Claude's), for his review:**
- Section label "WHAT YOU DID"; the box placeholder "What you did, and what happened"; the button "Log it"; "Flagged to check on the map: …".
- After logging: "Logged. N3, N8, N14 (Q.1–Q.4) are flagged on Mapping Landscape: check whether their emotion or place has changed, then read Pattern Synthesis again."
- "SINCE YOU ACTED … Check these notes on the map: has their emotion or place changed? Edit a note and it leaves this list. Then read Pattern Synthesis again."

**Checked, on both workbooks:**
- 11-13, "good fire": flags N3, N6, N11, N27, N30.
- Broadview, "mitigation": flags N3, N8, N14.
- On both, the list shows on Mapping Landscape only; Done removes a note; editing a note removes it; everything survives a reload.
- 13 workbooks: matrix clean. T5 boxes, Open workbook and the 3D cards are unchanged.

**For his call:**
- Should Combine merge `acts` and `remap` from coworkers? Today it doesn't.
- Should the PDF include WHAT YOU DID?
