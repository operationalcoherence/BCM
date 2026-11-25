# v280 · A LOOP BETWEEN GROUPS

Item 6 in his order of the second generation of insight types (BCM_TASK_QUEUE.md, 11-20 20:06). His call: "#6, Loops Between Groups", then "push access granted", 25 Nov 2026 16:22. Patch: tools/patches/v280_loops_between_groups.py.

## What it does
**A LOOP BETWEEN GROUPS** (LOOPS BETWEEN GROUPS when there are two), a card under WHY IT BEHAVES THIS WAY on Pattern Analysis, right after WHO STANDS WHERE. It looks for two groups whose emotions are aimed at each other: group A holds an emotion toward group B, and B holds one toward A.

- **Both holders named:** it states the loop. Both emotions low (aggression, distrust, defiance): each side's emotion is the other side's evidence, so the two harden together, and it weakens only when one side stops answering in kind or something they share comes to matter more. Both acceptance: a tie that strengthens itself and can shut others out. Mixed: the tie runs differently each way.
- **The note aimed back doesn't say whose emotion it is:** it asks one tap. "Does the aggression in N38 come from those who are defiant, aggressive, or distrustful?" Yes states the loop, marked "(you said … comes from them)". No drops it. Stored in C.asks as `loop|<note id>|<group>`.

Up to two loops; stated ones first. `gsmStructSum.loops` keeps them for later use (Taking Action, not wired yet).

## How it reads holder and target (general words only)
- **Target:** v279's reader (the emotion word, then toward, against, in, of, at, over, or about). The target counts as people when it is a v276 group word, or people named by their emotions ("those who are defiant, aggressive, or distrustful"), read as the set of those emotions.
- **Holder:** a group word that opens the note ("The council holds distrust…"), owns the emotion ("Residents' distrust…"), or follows among, amongst, from, by, or within ("Aggression amongst supporters…"). A word inside the target is never the holder.
- **Matching:** the same group word, or two emotion-named groups that share an emotion. When the target is named by emotions, the note aimed back must carry one of them before it is asked about. Words are never merged.

## WHO STANDS WHERE
A group the loop card covers is left out of WHO STANDS WHERE, and so is one in a loop the person said No to, except for the reading "the plan relies on the people it distrusts", which stays because v278's first move on Taking Action reads it. Its v276 readings of that group were the loop half seen: "runs both ways around supporters" claimed a loop from one group's notes. With that reading gone, the next one ("Supporters is not one block") counted N38, aggression *at* supporters, as supporters hindering, which is wrong.

## Inactive unless it applies
Silent unless one note names a group holding an emotion aimed at another group, and another note aims an emotion back at the first.

## Results
- His 11-20 workbook: supporters hold aggression toward those who are defiant, aggressive, or distrustful (N16); aggression is aimed at supporters (N38) with no holder named, so it asks. This is the 11-20 review's mutual aggression loop and the loop audit's best-supported link (L3). WHO STANDS WHERE keeps leadership only.
- A clinic test workbook with four added notes: "The council and residents hold distrust toward each other" (N9, N10), both holders named, stated without asking.
- Every other test workbook: word counts on every tab equal v279. Taking Action unchanged everywhere.

## Limits
Words only. A group named in other words, or an emotion the note doesn't name, is missed. A target found only through the verb form ("Nurses accept the new rota and the doctors…") reads the first object, so the doctors are missed. Note order on the map is not used to say which emotion answers which.

## Checks
matrix.py (15 workbooks, including 11-20 with its note text, kept local): no page errors, no injection. ta_flow.py on 11-20: pass. The Yes tap was clicked in the page: saved to C.asks and the card re-rendered as stated. No keys in the built file.

## His reaction
On the stated 11-20 card (after Yes): "brilliant" (25 Nov 2026 16:38).

## Wording to flag (Claude's)
The title and every sentence of the card: the question, "each side's … is the other side's evidence, so it grows on its own", "the two harden together", "It weakens only when one side stops answering in kind, or when something the two share comes to matter more than what divides them", the acceptance and mixed sentences, "(you said the … in N… comes from them)".
