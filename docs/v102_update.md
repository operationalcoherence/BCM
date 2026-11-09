# Bear Canyon Method v102 (preview) - update

Written 2026-11-09. Follows v101. The first of the "free parts" from
`week_of_11_09_plan.md`.

## What changed

The stopword list only. 362 entries to 352, with no change in behavior.

- **Eight duplicates removed:** could, get, got, much, other, same, taken, way.
  Each appeared twice; the lookup only ever saw the first.
- **Two dead entries removed:** `place's` and `time's`. The tokenizer strips
  apostrophes before the lookup, so neither could ever match anything.

Nothing else was touched. The six subject words (community, communities,
people, person, area, areas) stay suppressed — they are decided, batched with
item 2, and wait on the Layer 1 scoring.

## Verified

Pattern Analysis, Pattern Synthesis and In Parallel rendered with every fold
open, on his real workbook and on Broadview, before and after. All six pages
are byte-identical except the version label, which reads v102.

Key check: `grep -c 'AAPK\|AIza'` is 0 in both files.

## Wording

No on-screen wording changed.
