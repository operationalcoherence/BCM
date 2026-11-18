# v203 update (2026-11-18)

Phase 1, step 5 of the review plan, second half (P3; review 6c; decision E9). Patch: `tools/patches/v203_moves_follow_way.py` (terrain module in the engine file; no relief change).

## FIRST MOVES follows the selected way
On a Taking Action card, choosing a way (its button over the map, its row in THE WAYS FORWARD, or on the 3D) adds a line under FIRST MOVES, or THE SEQUENCE on a program. The line says which acceptance the way runs through, which indifference it passes (win it over before it tips the other way), and whether it meets what resists the goal (bring something to do, not an argument) or goes around it, leaving it as it is. "All ways" takes the line away. On 11-13, wildfire management:

- Way A: runs through acceptance at N3, N4, and N6, through the indifference at N26, and meets what resists the goal at N2, N9, and N16.
- Way B: runs through acceptance at N3, N5, and N6, through the indifference at N31, and goes around what resists the goal, which stays as it is.

## A call made differently from E9 (his to redirect)
E9 said way A would follow FIRST MOVES. I built and measured two versions of that:
1. Way A starts at the notes FIRST MOVES says to start from, then goes left to right. On 11-13 the crossings didn't change (wildfire management stayed at 5), and two cards got longer (1.4× to 2.0×, 2.1× to 4.0× a straight run). On the 200-note workbook ways got far longer (6.2× to 38.2×).
2. The nearest next note, with a cost for crossing the line and for going back. Crossings fell (5 to 3 on wildfire management; 13 to 2 on the 200-note workbook), but lengths rose (up to 29.6×), and on good fire both got worse (1 to 3 crossings, 1.4× to 3.3×).

Neither made the drawing better, so the drawing is unchanged and **the words follow the way instead**. Way A's left-to-right zigzag is still there; it needs its own fix later.

## Wording that is Claude's (flagged)
"Following way A: it runs through acceptance at …, through the indifference at … (win it over before it tips the other way), and meets what resists the goal at … (bring something to do, not an argument)" / "and goes around what resists the goal, which stays as it is."

## Tests
- `tests/waymoves.py` (new): with the 3D loaded, clicks every way on every card and prints the line. 11-13, the 11-13 + aggression copy, and Broadview's place map.
- `tests/matrix.py` on 11-13, Broadview, that copy, and every mkwb workbook: no page errors, no script injection.
- `grep -c 'AAPK\|AIza'` = 0.
