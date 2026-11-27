# v316: no old figures on Pattern Analysis, ever

Gregory, 26 Nov 19:04, after the live test showed the old petal figure: "lets make sure that never happens again."

- AROUND THE GOAL and HOW IT HANGS TOGETHER never show, whatever the workbook holds. They stay in the page, hidden, for any code that still looks for them.
- Before, they showed whenever no line-map note had words: workbooks with only symbols, with answers only, or with notes on the place map only.
- When no note has words, Pattern Analysis opens with **NO GROUND YET**: it says how many symbols are waiting for words, that what follows reads the answers only, and has a Go to Mapping Landscape button.
- Everything else on Pattern Analysis is unchanged (matrix word counts identical to v315).

Patch: tools/patches/v316_no_old_figures.py.
