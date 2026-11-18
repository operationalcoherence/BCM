# v212 update (2026-11-18)

Review Phase 2 step 7: Pattern Synthesis reordered. Patch: `tools/patches/v212_synthesis_order.py` (engine only).

## What changes
1. **Patterns above the figure (4f).** A row of the patterns sits right above the map: tap one to draw it on the 3D (or the canvas) without scrolling to the list; tap again to clear it. The row and the list's tick boxes stay in step.
2. **Questions moved to PATTERNS THAT RUN THROUGH IT (4e).** "Does N15 support 'aggressive suppression'?" and the like were asked inside WHAT THE GROUND SAYS and again under PATTERNS. They are now asked only under PATTERNS, where the phrase is. The reading says so: "Until you answer the question about it under PATTERNS THAT RUN THROUGH IT, N15 counts as supporting it."
3. **The match in bold (4g).** Under PATTERNS THAT RUN THROUGH IT, read more now shows the sentence from each note and answer with the phrase in bold (up to 8). The note numbers link back to the note. CAUSE AND EFFECT bolds the word in its quoted sentences.
4. **Links back to the map (4i).** In WHAT IT MIGHT MEAN, a finding that no note carries now names the answers it comes from ("allowing unplanned (Q.3 and Q.4)"), and those link back to the answer, as note numbers already link back to the note.

Already in place: the legend (4d), and IN YOUR ANSWERS, NOT ON THE MAP in phrases (4h, v201).

Still open in WHAT IT MIGHT MEAN: a few findings there are still lone words ("tradition (N1, N18, and N23)"). The v211 rule (quote the shortest note that uses the word) could apply here too; left for his call, since it makes the list longer.

## Wording that is Claude's (flagged)
The row's help line and the new sentence for the readings.

## Tests
- Screenshot with the 3D on 11-18: the row sits above the map; tapping "good fire" draws its loop and ticks its box below; unticking the box clears the button.
- `tests/dump2.py` Synthesis on 11-18: the questions appear only under PATTERNS.
- `tests/matrix.py` on 11-18, 11-13, Broadview, and every mkwb workbook: no page errors.
- Both builds reproduce from source; `grep -c 'AAPK\|AIza'` = 0.
