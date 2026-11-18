# v216 update (2026-11-18)

His note at 14:52, with screenshots from v214: the figure belongs on In Parallel, not Pattern Synthesis, and "the In Parallel page is very wrong still." v215 (pushed 14:41) had already moved the figure and deleted the grid; his page was still on v214, held in GitHub's cache. v216 cuts the text under the figure (review 5c–5e). Patch: `tools/patches/v216_in_parallel_cut.py` (engine only).

## In Parallel now reads
1. THE TWO PICTURES, SIDE BY SIDE (the figure).
2. **Where to start**, in one line.
3. **MORE FROM BOTH PICTURES**, closed: Read together, Closest and farthest from the goal, Emotion, Voices, Patterns worth a second look, What might relate to what. Nothing is deleted; it's out of the way.
4. **THE EARLIER 3D VIEW**, closed, now last.

"Where both pictures agree" and "Where they differ" are removed when the figure is shown, because the figure says the same thing word by word (tap a word). That includes "wildfire risk", the word 5c asked to explain: "the threads keep it in the context you have grasped, though Analysis does not list it as a gap … The ground asks: is it answered in other words?" On place maps, where the figure can't be drawn (Broadview), the two paragraphs stay as before.

## Tests
- Page check on 11-18: the figure shows; Where to start is the only text left open; MORE FROM BOTH PICTURES holds its six parts, closed. Broadview: no figure, so agree and differ stay open; the rest is folded the same way.
- `tests/agree.py` on 11-18 with the 3D: no grid; a tapped word's 8 line segments on the Synthesis 3D; no page errors. Screenshot checked.
- `tests/matrix.py` on 11-18, 11-13, Broadview, and every mkwb workbook: no page errors.
- Both builds reproduce from source; `grep -c 'AAPK\|AIza'` = 0.
