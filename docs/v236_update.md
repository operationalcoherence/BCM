# v236: his answers to the pre-F8 review table (11-19 09:20)

Table: https://claude.ai/artifact/84H2tJCmJvqMcQoDDZdrit. Everything he approved or changed is applied in this one build.

## Applied
- **1b** Start here 05 ends "…especially as acting brings new information to light."
- **1e** Start here 03 opens with his text: "One through four are questions about grasping context. The remainder are questions about how to design for the context just grasped." He wrote "One and four". Claude used "One through four" so that it matches his Q.1–Q.4 / Q.5–Q.7 distinction. **Confirm with him.**
- **1g** WORDS USED HERE (both places): "The emotion a note carries, how you know it, and whose view it carries."
- **2i** Instruction 11: "Mapping Synthesis" is now "Pattern Synthesis".
- **2k** LOCATION help: "Add the place the goal is about, if it has one, and the place map opens below. Leave it blank for a goal with no place, such as a policy or a practice; the line map is built for those."
- **3g** The strip heading is now WHAT YOU WOULD DESIGN FOR THAT CONTEXT (his wording).
- **3s / 6t** Definitions in small gray text:
  - THE LOOP on Analysis: "A loop, in this method, is a reinforcing cycle: each turn of it makes the next turn more likely. Systems thinking calls this positive feedback, where positive means self-amplifying, not good. It is not a balancing loop that settles back on its own." (This is what the engine detects: each round calls for more of the same.)
  - WHERE IT CAN CROSS: "Crossing is a move from one emotion's ground to another's, such as from distrust toward acceptance. Distant emotions take the most energy to cross between, in either direction."
  - The Taking Action loop card now opens "A reinforcing loop: …".
- **4c** Tour openers (his wording): "where the goal already has people aligned with it"; "…what they are attached to and the present and future they create."
- **34** THE EMOTION CHANGES is now THE HIDDEN CHANNELS everywhere.
- **5f** In Parallel figure: a lone word becomes the opening words of the shortest note that carries it, in quotes. A lone word that no note carries is left out of the figure.
- **6f** "Decide good fire first. It touches more of the situation than anything else here, so what you decide about it reaches furthest."
- **6l** "What you would design breaks into the cycle that keeps the situation going."
- **6s** "Most shifts happen on the ridge of indifference, where people are not yet for or against…". "For nothing yet" is now "not yet for or against" everywhere on screen.
- **6g** Ground card titles: the note numbers sit behind the title, small and gray.
- **W1** "Prompts, not findings: talk them through with the people involved, and change or drop any that do not fit."
- **W2** THE TEST's subline is cut.
- **W3** The two help lines now appear once, under STRATEGIES, instead of on every card.

## Kept as they are (his call)
1a, 1c, 1d, 1f, 2d, 2f, 2j, 3c, the line under YOUR LANDSCAPE, 35 (PLACED ONE WAY, TIED THE OTHER), 5r, 6t titles, 6v, 6c, 6w (word cards stay folded, no merging), W4.

## His notes for later
- **6a, Way A:** "Way A should reflect the strategy pathway or trajectory necessary to move towards the goal… An accurate way is a good way." No smoothing. Way A already follows FIRST MOVES (E9), which comes from the data. Next session: check that Way A's route is exactly the order the data gives on each strategy card, and fix any card where it isn't.
- **F1/F2:** talk it through with him before F8.
- **D8:** voices stay equal; revisit with F8.
- **X1:** the WebM download and A1 come after F8, or are dropped.

## Checked
step9.py (updated for the new 03), ta_flow.py, tour.py (both act openers read his wording), agree.py (the figure's labels; no page errors), and matrix.py on all 14 workbooks (no errors). The key check is 0.
Patch: tools/patches/v236_review_answers.py.
