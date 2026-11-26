# v284 — Taking Action cards you can read in 15 seconds

His review, 25 Nov 2026 (17:17–18:22). Pushed to main.

## Every card, in this order
1. **An action as the title.** The old title stays beside it in small gray.
2. **FIRST MOVE**, in larger type.
3. **WHY THIS HELPS THE GOAL**
4. **WHAT IT WILL TAKE**: the effort first ("Moderate effort."), then the order of the crossings; or, in words, how often the way switches between helping and hindering and how much longer it is than a straight line.
5. **WHAT TO WATCH FOR** (where the reading splits), or **WHAT STILL STANDS IN THE WAY** when there is no split.
6. **The map**, always visible.
7. Folded: **Why this action, in full**, then **Evidence**.

DOES THIS ANSWER IT? is now **DOES THIS ANSWER THE GOAL?**

## Rules built into the engine (every workbook)
- **Splits name only phrases the user wrote.** A single word is widened to the phrase it sits in; pieces of one phrase ("complex adaptive", "adaptive system", "system") become that phrase once; a single word with no phrase around it is not stated. **Emotion names (acceptance, indifference, distrust, aggression, defiance) always stand alone**, never widened ("Your plans take the distrust more lightly than your notes do.").
- **Titles come from what the card is**: its seed, its ground, or its first move, so title and first move agree.
- **No vague titles.** Cards that build on what already helps or already works name the notes by a short clause in the notes' own words, with the note id ("starting with … (N13), and 3 more"; the rest on the WHY line). A single word in a title is widened by the list it stands in, from the question the card came from. A note written as an instruction ("Create conditions …") becomes the title, once.
- **The goal's own words say nothing here**: dropped from those clauses, and a card titled only by the goal's phrase is removed.
- **Fragment cards go** (a card whose phrase is part of another card's phrase); **look-alike ground cards merge** (same emotion among acceptance), naming every note on WHY.
- The panel at the top (THE CHEAPEST FIRST MOVE) uses the new titles.

## Tests
`tests/vague_titles.py` fails any card title that names a single non-emotion word, nothing at all, or only the goal's words. All pass on nine workbooks; `matrix.py` (no page errors, no injection), `ta_flow.py` and `switch.py` pass.

## Still weak
- The phrase picker itself gives verb-ending phrases on some workbooks (clinic: "clinic open", "residents drive"). A bigger change.
- A merged ground card's map draws only the first note's ways.
- All wording is Claude's, for his final wording pass.
