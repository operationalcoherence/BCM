# v202 update (2026-11-18)

Phase 1, step 5 of the review plan, first half: cards that follow the ground (P3). Patch: `tools/patches/v202_cards_ground.py` (engine only, for every workbook).

## 1. Program or strategy (review 6o and 6q; decision E10)
A card whose notes go from acceptance into aggression, distrust, or defiance is now a strategy, because a program can't plan for a move that risky. The card's reason says so and names the notes. This is the seventh thing that tips a card to strategy (the line "the only one of the six things" now says seven).

Up to four strategies are shown (was three), so a card the rule turns into a strategy isn't pushed straight off the page. Programs stay at two.

On 11-13: "aggressive suppression" turns from program to strategy (N15 acceptance, N17 aggression). "social media" is a strategy now too, as he said it should be (N4, N10, N15 acceptance; N23 aggression), but it ranks fifth among strategies, so it isn't shown. **Flag for him:** raise the cap to five, or leave it.

## 2. A manual switch on every card (6q)
Every card's reason line ends with "Make it a program" or "Make it a strategy". The choice is saved in the workbook (`asks["mode|…"]`), and the card then says "because you set it as one. Without that, the method would read it as a …", with "Let the engine decide" to undo it. A card you switched always stays on the page, whatever the caps.

## 3. Cards from the ground (6d)
Aggression, distrust, or defiance written on the side of the line where things help, within reach of acceptance, now forms a card of its own, named by the ground: "Aggression among acceptance, where things help (N32)". Notes close to each other (within 70 map units) share one card. At most two of these cards; line maps only. Each is a strategy unless switched, and its reason cites the paper on what that emotion can become: aggression can tip toward defiance; distrust can turn more severe instead of more benevolent; defiance is the emotion most resistant to any strategy (Vigneaux, 2026). Its FIRST MOVES start from the acceptance around it.

That is the case from his review: aggression added among acceptance on the help side now changes the strategies, even when it shares no recurring word with anything.

## Wording that is Claude's (flagged)
"its notes go from acceptance (…) into … (…), a high-risk move that a program cannot plan for"; "Make it a program / strategy"; "Let the engine decide"; "because you set it as one. Without that, the method would read it as a …"; the ground card's title, IN SERVICE OF THE GOAL, Why, reason, and four FIRST MOVES.

## Not yet (v203)
FIRST MOVES following the selected way, and way A following FIRST MOVES. Grouping strategies and programs together on the page is Phase 2.

## Tests
- `tests/switch.py` (new): clicks the switch on a program card, checks it becomes a strategy, stays on the page, and is saved; then undoes it and checks every card is back as before. Passes on 11-13, the 11-13 + aggression test copy, and clinic.
- A test copy of 11-13 with two aggression notes added among acceptance (`wb_aggr.json`, local only, never committed): both form ground cards.
- `tests/matrix.py` on 11-13, Broadview, that copy, and every mkwb workbook: no page errors, no script injection.
- `tests/relief_text.py` with the 3D: the ground cards and the switch render.
- `grep -c 'AAPK\|AIza'` = 0.
