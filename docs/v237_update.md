# v237: Way A follows the path the data gives (his review note 6a)

His note (11-19): "Way A should reflect the strategy pathway or trajectory necessary to move towards the goal. This is not a decision made about appearance, but about making explicit what the data is telling the user to do. An accurate way is a good way."

## What the check found
Way A did **not** follow the data. It ran from START through the card's notes **left to right**, then to GOAL. In v203 it was measured but never changed (E9). So it said nothing about the ground, and it didn't match THE WAY ACROSS, which already reads the data's route in words.

## Now, on every strategy card
Way A is the route THE WAY ACROSS describes:
1. START.
2. The card's low-ground notes, beginning with the emotion nearest the ridge: distrust, then aggression, and defiance last. Within each emotion, left to right.
3. Over the ridge of indifference nearest the first of them.
4. Up to the acceptance on the help side nearest that ridge.
5. The goal.

Its name says so, for example: "The way the ground points: N19, N20, N17, and N1, over the ridge at N8, up to acceptance at N10." With no ridge on the map, it climbs straight to acceptance ("straight up over bare rock"). A strategy card with no low-ground notes keeps the old way. Programs, Way B (firm ground only), and Way C (from the support) are unchanged.

On 11-18, the first card's Way A now draws the same route its THE WAY ACROSS line names (distrust at N19 → the ridge at N8 → acceptance at N10). Way A is the costlier, higher-impact way, as the ways chart shows: it meets what holds the situation, while Way B goes around it.

## Checked
tests/waya.py (new; opens each card's folds and prints each way's name) on 11-18 and the 200-note workbook. Also matrix.py on all 14 workbooks (no errors), ta_flow.py on 11-18 and Broadview, and a screenshot of the first strategy card's 3D. The key check is 0.
Patch: tools/patches/v237_way_a_follows_data.py.
