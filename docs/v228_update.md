# v228: Taking Action in three layers

2026-11-18. Patch: `tools/patches/v228_ta_hierarchy.py`. Test: `tests/ta_flow.py`, extended.

His 21:37 "do it" on the hierarchy review: a user should answer "What should I do?" in under 30 seconds, and "Why?" by opening more. **Nothing is removed.** Sections are reordered, summarized first, or opened on demand.

## The page
- **THE CHEAPEST FIRST MOVE** leads the test panel in larger type. The old "Where to start" note joins it as "Carries furthest", so the page no longer gives two starts.
- **THE TEST**: each line keeps its verdict; the notes behind it are smaller and gray.
  - Split readings: a one-line list of the kinds found, with "Each split, and the cards it lands on" closed under it.
  - Constraints named: a one-line summary, with the texts closed under it.
- **DOES THIS ANSWER IT?** sits right under THE TEST (it asks him to decide).
- **NOTHING YOU WOULD DO ANSWERS THESE YET** is folded. THE TEST already says it; the fold keeps the audit trail.
- The opening note is set small. Each group's long explanation (his text) sits behind "Why a strategy?" / "Why a program?".

## Each card
- **Layer 1, the decision strip (always visible):**
  - MEETS THE TEST: verdict and a short phrase, in the notes' own words with the number in gray.
  - FIRST MOVE: the first line of FIRST MOVES or THE SEQUENCE.
  - THE WAY ACROSS, in one line, e.g. "distrust (…) → the ridge at … → acceptance at … · moderate cost; defiance last".
  - READING SPLITS, in one line, when there are any.

  Word cards show only the lines they have.
- **Layer 2, "Why this action":** in service of the goal; strategy or program, with the switch; why; the full test; THE WAY ACROSS in full; WHERE THE READING SPLITS in full; all first moves; THE WAY THROUGH IT (3D and the open chart); WHAT HOLDS IT IN THE LOW GROUND. It is closed, except on the card named in the cheapest first move.
- **Layer 3, "Evidence" (closed):** the note lists, What this rests on, and the Morin line.
- **Constraint boxes:**
  - An empty box shows as "Name what holds it"; one tap opens it.
  - A written constraint always shows, with its Q.4 / Q.6 / Q.7 buttons.
- YOUR DECISION and WHAT YOU DID stay visible at the foot of each card.

## Not layered yet
The way's written readings that the 3D adds after it loads (A: why choose it, comparing the ways, moves in order, when to stop) stay inside THE WAY THROUGH IT in layer 2. They are drawn by the terrain module after the card opens; moving them to Evidence would need a change there.

## Checked
- Visible words on first load, before and after:

  | Workbook | Before | After |
  |---|---|---|
  | 11-18 | ~5,100 | ~1,800 |
  | Broadview | ~1,700 | ~1,100 |
  | Clinic | ~1,200 | ~760 |

  Everything is still in the page, closed.
- `ta_flow.py` passes on 11-18 and Broadview; clinic has no seeded card with a constraint field, so that part skips.
- `matrix.py`: no errors on any workbook.
- Analysis, Synthesis, and In Parallel read word for word as before.
- The key check is 0.

Wording is Claude's, for his redlines: "Why this action", "Evidence", "MEETS THE TEST", "Carries furthest:", "Name what holds it", "Why a strategy?", "Why a program?", and the short split lines.
