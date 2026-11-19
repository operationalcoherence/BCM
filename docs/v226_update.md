# v226 — Taking Action rebuilt around the central test (Phase 2, step 8)

2026-11-18. Patch: `tools/patches/v226_taking_action.py`. Tests: `tests/ta_flow.py` (new), `matrix.py`, `relief_text.py`, `dump2.py`.

Taking Action now answers BCM_ARCHITECTURE.md §0.3, the central test: **"Does what you would design change the conditions and invite the transitions the goal needs?"** Its cards grow from what Pattern Analysis, Pattern Synthesis, and In Parallel found, not from recurring words alone.

## What changed on the page (top to bottom)
1. **THE TEST** (open panel under the opening note). It reads the workbook against the test, one line per part, with a verdict (YES, PARTLY, NOT YET):
   - *What holds it*: the system that holds, the key tension, the loop. It names the notes nothing in Q.5–Q.7 answers yet.
   - *What already moves*: the opportunity and what is already helping. It names the support nothing builds on yet.
   - *Where it can shift*: whether what you would design reaches the ridge of indifference.
   - *Where the reading splits*: each split reading from In Parallel, and which cards carry it, or what it means if no card does.
   - *What holds it, as you named it*: every constraint written so far, and whether it is in Q.4, Q.6, or Q.7.
   - *The cheapest first move*: the program on high ground first, then the strategy through the ridge.
   - **WHAT EACH PART OF A CARD DOES** (closed): one line per field.
2. **STRATEGIES**, then **PROGRAMS**, each under its own heading with its explanation (his text, moved, not changed). Cards seeded from the structure come first. Cards built only from recurring words fold under **MORE STRATEGIES / MORE PROGRAMS, FROM THE WORDS YOU USE**. A word card stays visible if it has a decision, a WHAT YOU DID entry, a manual program/strategy switch, or is the "Where to start" card. Ground cards (hostile emotion among acceptance) stay visible.
3. The rest is unchanged: NOTHING YOU WOULD DO ANSWERS THESE YET, DOES THIS ANSWER IT?, GOAL NUMBERS, Where to start, WHERE THE CARDS MEET, MORE INFORMATION NEEDED, WHAT YOU DECIDED AND WHY, REFERENCES.

## Seeded cards
| Seed (Pattern Analysis) | Card | Mode |
|---|---|---|
| THE SYSTEM THAT HOLDS | What holds it: … | strategy |
| THE KEY TENSION | The key tension: … (the goal's own clause) | strategy |
| THE LOOP | The loop: … | strategy |
| THE OPPORTUNITY | The opportunity: … | program (strategy if its notes mix acceptance and low ground) |
| WHAT IS ALREADY HELPING (Q.1–Q.4 notes above the line, not in the opportunity) | What is already helping: … | program |
| SUPPORT NOT YET REINFORCED (the engine's "unused" support, or support nothing in Q.5–Q.7 reaches) | its own card only if under half of it already sits in another program card; otherwise it shows in that card's test and sequence ("Add N3, N6 to Q.7") | program |

Each seeded card has the switch (key `seed|sys`, `seed|ten`, …); a switched card moves to the other group.

Each seeded card carries:
- **DOES WHAT YOU WOULD DESIGN MEET IT?** The test on its own notes. "Answers" uses the same rule as NOTHING YOU WOULD DO (`gsmNR`, now also exposing `rw`, `cm`, `ri`). "Builds on" also counts the engine's unused-support reading, so it agrees with Analysis's WHAT IS ALREADY HELPING. Q.5–Q.7 notes count as built on.
- **THE WAY ACROSS.** The low-ground emotions are ordered by cost to the ridge (distrust one step, aggression two, defiance three and always last). Each gets "to the ridge at Nx, then up to acceptance at Ny". The cost reads low, moderate, or high. Straight across reads as a climb over bare rock that costs more. With no ridge, the way says to find the people who are for nothing yet. Entrenched notes (`gsmHy` > 1.05) cost more. The way ends "behaviors first below the ridge, emotions first above it (Vigneaux, 2026)". Program cards say they stand on high ground and name their edge: indifference that could tip and low ground nearby that could pull them down.
- **FIRST MOVES / THE SEQUENCE**, **THE WAY THROUGH IT** (3D ways A/B/C, with the ridge and acceptance notes included so the ways can pass them), and the constraint fields. These come from the engine's own `Un()`.

## Split readings carried into action
In Parallel keeps its double readings in `window.gsmSplit`: label, notes, words, and the data each needs (`vi/va/eu/ed`, `emo`, `pe/pt/up`, `su/sd`). After render, `gsmTAPass()` matches each split to cards by shared notes, or by the word in the card's title. Each split goes onto at most two cards, and each card takes at most two splits. A matched card gets **WHERE THE READING SPLITS** with what it means for acting:
- TWO PEOPLE, TWO SIDES: a way in for each group; test the wording with both. Same emotion: agree on the direction first. Far-apart emotions: no single message carries both.
- THE EMOTION CHANGES: plans harder than the situation: reword what the actions ask of people. Plans easier: try them small on the ground they will land on.
- ONE IDEA UNDER TWO NAMES: act on them as one. Both sides claim them: lead with them. Only hindering: answer them directly.
- PLACED ONE WAY, TIED THE OTHER: a foothold for the crossing, something to redirect, a borrowed foothold to check, or a place to check.

## Constraint → card → WHAT YOU DID → re-map
- Once a constraint is written, buttons appear under it: **Q.4 · a condition to establish**, **Q.6 · something to redesign**, **Q.7 · something to reinforce**. A tap appends the text to that answer (once), updates Mapping Context, and re-reads the workbook. The button then reads "In Q.4 ✓" on every card that holds the note.
- WHAT YOU DID lists **WHAT HOLDS IT, AS YOU NAMED IT** for the card's notes. Logging saves them on the entry (`acts[].c = [{id, lab, x}]`) and flags those notes to re-map, along with the card's Q.1–Q.4 notes.
- SINCE YOU ACTED on Mapping Landscape shows each flagged note's constraint.

## Smaller
- The chart comparing the ways is open by default; the summary reads THE WAYS COMPARED.
- One-line help under each field: the constraint field, YOUR DECISION, and WHAT YOU DID.
- The opening note: "Each card grows from what Pattern Analysis, Pattern Synthesis, and In Parallel found, or from the words you used."
- Ground cards carry `data-ground="1"`.

## Code
- `gsmStructBuild()` keeps its notes in `gsmStructSum.D` (`sys`, `ten {gc, f, h}`, `loop {s, t, k, n}`, `opp`, `oppN`, `ind`).
- Seeded cards and THE TEST are built in the Taking Action builder, right after the ground cards, as `In = seeded + In` and `TAT`.
- Post-render: `gsmTAPass(Rt)`, run from the card wiring. It places the splits, fills the test's split row, groups, and folds. It waits for `gsmSplit` for up to about 1.2 s.
- New helpers next to `gsmActUI`: `gsmConsQ`, `gsmTANorm`, `gsmTAIds`, `gsmCardCons`, `gsmTACss`, `gsmTASay`, `gsmTAPass`. A document listener handles `button[data-cq]`.

## Checked
- `matrix.py` on 11-18, Broadview, and all mkwb workbooks: no errors, no injection.
- `ta_flow.py` on 11-18 and Broadview: all pass (constraint → Q.4 → Mapping Context → In Q.4 → WHAT YOU DID → acts[].c → remap → SINCE YOU ACTED; switch moves a seeded card).
- `relief_text.py`: 3D ways, THE WAY ACROSS, splits, and the open chart on 11-18 and Broadview. On clinic, the only open card has one way, so it has no chart, and the folded word cards mount their maps when opened.
- Pattern Analysis, Pattern Synthesis, and In Parallel read word for word as v225 on 11-18.
- Visible length of Taking Action: 11-18 about 5,100 words (v225: 4,700); Broadview 1,700 (2,300); clinic 1,200 (2,600).
- `grep -c 'AAPK\|AIza'` = 0 on both built files.

## For his redlines (all wording is Claude's)
- Card titles "What holds it: …", "The key tension: …", "The loop: …", "The opportunity: …", "What is already helping: …", "Support not yet reinforced: …", and the gray "grown from …".
- THE TEST's labels, the verdict words YES / PARTLY / NOT YET, and THE CHEAPEST FIRST MOVE.
- THE WAY ACROSS: the cost words (low, moderate, high: one or fewer steps is low, three or fewer is moderate, more or bare rock is high).
- The split implications, the field help lines, and the fold names MORE STRATEGIES / PROGRAMS, FROM THE WORDS YOU USE.
- Folding the word cards was Claude's call, to keep the page from doubling. Say if he wants them open.
