# v230: Taking Action describes the situation, not the workbook; the short check of Taking Action

2026-11-18. Patch: `tools/patches/v230_situation_language.py`. User-facing text only: no logic, scoring, or architecture changes.

## His wording review (21:53)
- **THE SYSTEM THAT HOLDS → WHAT HOLDS THE SITUATION IN PLACE:** on Analysis's WHY IT BEHAVES THIS WAY card, on the seeded card's title and its "grown from" line, and in THE TEST.
- **THE TEST's line names:**

  | Before | After |
  |---|---|
  | The system that holds | What holds the situation in place |
  | The key tension | What the goal needs, and people fear |
  | The loop | What keeps reinforcing the situation |
  | The opportunity | The alternative that already exists |
  | What is already helping | What already helps |
- **Unresolved:** "Not yet answered: N18, N26, and N19" becomes "Tradition, indifference toward the subject of wildfire, and justified fear of intentionally burning remain unresolved." The note numbers follow in small gray, as links.
- **YES lines say what the proposed actions address:**
  - What holds the situation in place: "…every part holding it in place."
  - What the goal needs, and people fear: "…the fear the goal runs into."
  - What keeps reinforcing the situation: "…the reinforcing cycle identified in Pattern Analysis."
  - Help lines: "…use all of it."
- **Not used yet:** "Not yet built on" becomes "… already help the goal, but the proposed actions don't use them yet."
- **The same language** in each card's strip and its full test sentence ("The proposed actions reach …; … remain unresolved, so they keep holding the situation in place"), in the ridge line, and in the constraints summary.

## The short check of Taking Action (fixes made here)
1. **A broken name:** names taken from a note's opening words kept a leading preposition ("For good fire already helps…"). Leading for, to, in, on, with, and by are now dropped.
2. **The ridge line** reads as the situation: "Most shifts happen where people are for nothing yet, the ridge of indifference: …"
3. **THE TEST's subtitle** said it was read against "your workbook" and that each line "points to" cards (it doesn't). It now reads: "Read against the situation you have mapped. The cards below take up each line."
4. **PLACED ONE WAY, TIED THE OTHER on card strips** said "N8's place and ties disagree" (map language). It now names the note and says what it means for acting, with the number in gray. One of:
   - "could be a foothold for the crossing";
   - "carries energy that could be turned toward the goal";
   - "looks like help but may give way under pressure";
   - "may not be where it seems".

## Left as they are (noted by the check, outside this change)
- "Carries furthest: good fire shares notes with 3 of the other cards…" is the engine's older wording and still workbook language.
- Ground card titles carry note numbers: "Aggression among acceptance, where things help (N32 and N33)".
- The loop card keeps its title "The loop: …", because it names Pattern Analysis's section THE LOOP. Only THE TEST was asked to change.
- BCM_CONCEPT_REGISTRY.md and the architecture still say "the system that holds", as the analytical name; the screen now says WHAT HOLDS THE SITUATION IN PLACE.

## Checked
- `ta_flow.py` passes on 11-18 and Broadview; `matrix.py` shows no errors on any workbook; the key check is 0.

Wording is Claude's except the two phrases he gave.
