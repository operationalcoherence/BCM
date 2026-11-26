# v292: the loop and two-ways questions are back

His note (25 Nov 2026 21:41): "We just added these! Nooko." v291 removed the A LOOP BETWEEN GROUPS question ("Does the aggression in N38 come from …?") and the TWO WAYS OF RUNNING question ("Is the goal two ways of running, each for its own conditions?"). Both are features he asked for, not questions covering the engine's limits, so both are restored exactly as in v290. The rest of v291 stays. Patch: tools/patches/v292_restore_loop_twoways.py.

Lesson for the rule "no one-tap questions to cover the engine's limits": it applies to questions that admit the engine can't tell (e.g. "Patterns cannot tell which, so it asks"), not to questions he designed into a finding. Ask before removing any question that came from his own request.

Checks: fulldump on 11-20 shows both questions with their buttons; matrix.py on 11-20, 11-13, Broadview, clinic, empty: no errors.
