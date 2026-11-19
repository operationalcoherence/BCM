# v231: the constraint boxes on Taking Action show again

His report (11-18 22:29): the grayed questions under the constraint fields had disappeared.

Cause: v228 folded every empty constraint box into a "Name what holds it" link to cut the page's word count. That hid the field and the Q.4 / Q.6 / Q.7 buttons he approved in v227 (always shown, grayed out until something is written).

Fix: the fold is removed. Every box shows its field, its one-line help, and its grayed buttons; the buttons turn on as you type, as in v227. The layering from v228 is otherwise unchanged.

Checked: on 11-18, all 28 fields and 84 buttons are visible, and the buttons are disabled until text is written. `ta_flow.py` passes on 11-18 and Broadview. `matrix.py` has no errors. The key check is 0.

Patch: tools/patches/v231_constraints_shown.py.
