# v241 (preview only) — 2026-11-19

His note (11-19 10:52), with a screenshot of a way that doubles back on itself: "in instances like this, its still impossible to tell what the order is."

1. **Numbered stops on the selected way.** Each way now carries its stops in order: the points it is built through, which are its notes and, for way A on a strategy, the ridge and the acceptance it climbs to (v237). The 3D numbers them 1, 2, 3, and so on, in small badges in the way's color, at the point where the way passes each stop. START and GOAL keep their flags. Stops less than 3 map units apart get one number.
2. **Only one way's numbers show at a time:** the selected way's, or way A's when All ways is on. Hovering a way shows its numbers.
3. The arrows (v240) stay. Together they give direction on each stretch (arrows) and the order of the stretches (numbers).

**How:** `viaPts()` and `legs()` keep `out.stops`; way C joins `first.stops` with the goal; `data()` passes `routes[].stops`. relief.js adds `.wn` labels per way (`WAYS[k].nums`), hidden through `o.hid` in `place()` and set in `showWays()`.

**Checked:** all four reading tabs, every fold open, identical to v240 on six workbooks. Cause workbook: 1 to 4 follow A down to N9 and N2, back up past N1, to N3. 200-note workbook: A shows 59 numbers; selecting B shows only B's, and All ways shows A's again. That card is an extreme case (49 notes), so it is busy but still readable in order. waymoves.py and the matrix are clean. Keys: none.

**Next:** v242, bare rock on place maps shown as color (his yes, 11-19 10:06).
