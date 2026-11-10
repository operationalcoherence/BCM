# Bear Canyon Method v104 (preview) - update

Written 2026-11-10. Follows v103.

## What changed

**The hang figure is no longer cut off at the bottom.**

The figure's frame was fixed at one size for every workbook, while the loops
are drawn from wherever the dots sit. On his workbook the drawing reaches
y=349.5 and the frame stopped at 334, so the lowest loops were cut off.

Now the finished drawing is measured and the frame grows to hold it, with 6
units of margin. The frame never shrinks below the old size, so any workbook
that already fit looks the same.

| Workbook | Frame height before | After | Drawing bottom |
| --- | --- | --- | --- |
| His real workbook | 348 | 370 | 349.5 |
| Broadview | 348 | 353 | 333.0 (fit by zero before) |
| Clinic (non-wildfire) | 348 | 348 | 319.8 |

Both the line-map figure on Pattern Synthesis and the copy on In Parallel use
the same frame. Full screen reads the frame from the page, so it follows.

Sizing the frame from the dots does not work: loops and labels extend about 43
units past the lowest dot. The fix measures the drawing itself.

## Verified

- Measured with the page's own geometry: the drawing now sits inside the frame
  on his workbook, Broadview and the clinic workbook.
- Screenshot before and after on his workbook: the loops that ran off the
  bottom edge now close.
- All three reading pages rendered as text with every fold open, his workbook
  and Broadview, before and after: byte-identical text.
- tests/matrix.py over nine workbooks (real, Broadview, clinic, empty, one
  note, goal only, legacy, 200 notes, hostile): no page errors, no probe fired.
- The measurement runs in a hidden off-screen holder, so In Parallel works even
  when its tab is hidden (the risk flagged in the v103 handoff). If the
  measurement ever fails, the old frame is used.
- Key check: `grep -c 'AAPK\|AIza'` is 0.
- `gsm-readable.js` regenerated.

## Not verified

- Window sizes other than 1000 and 1400 wide; touch devices; PDF export.
- Fonts: the test harness blocks Questrial, so label widths came from the
  fallback font. The 6-unit margin is there to cover the difference.
- Whether the clipping he sees on screen matches the 15.5 units measured. This
  fix covers it either way.

## Wording

No new wording.

## Tests

`tests/measure.py` reports the frame and the drawn extent for both figures.
`tests/shot.py` screenshots the figure. `tests/matrix.py` now loads
`../gsm-preview.js` (it pointed at a file that no longer exists).
