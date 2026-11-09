# Asking rather than telling: questions the engine can already ask

Written 2026-11-08, from Gregory's request for "the engine that gives us the
ability to ask better questions about user data they provide." All wording here
is Claude's. Designed, not built, and not scheduled.

Companion to `vocabulary_architecture.md` and `vocabulary_funnel.md`. The
vocabulary feature is one instance of what follows; this note generalizes it.

## The rule

**A finding becomes a question when the engine has found a discrepancy it
cannot resolve and the person can. Everything else stays a statement.**

That is the whole design. It needs no new understanding of meaning, no new
data, and no network. Every question below comes from structure the engine
already computes and today prints as a sentence.

## Why this fits the standard

Measured against power and simplicity: no new machinery, nothing leaves the
device, still deterministic, still private. It is more power out of what is
already computed, which is the trade the elegance standard asks for.

It is also more faithful to his own standing rule, "Patterns suggests; you
decide." A question suggests. A statement asserts. Several of the lines on the
reading pages today assert something the engine cannot actually know, and a
question is the honest form of exactly those.

## The catalogue

Each class below is paired with a real instance measured on his workbooks at
v101, so none of this is hypothetical.

**1. Contradiction between placement and language.** In Parallel already prints:
*note 20 sits below the line, but 2 of the 3 places it shares words with sit on
the other side. Where you put it and what it ties to may not agree.* As a
question: you put this on the hinder side, but it talks like the help side —
which is right? Only he can settle it, and settling it corrects the data.

**2. Two judgements that never disagree.** On his workbook every note above the
line is marked acceptance (11 of 11) and none below it is (aggression 7,
distrust 2, indifference 2, defiance 1). The engine can ask whether the emotion
mark and the placement are two judgements or the same one made twice. This is a
question about how he is using the method, and nothing else in the workbook
will ever raise it. It is the same measurement as item 5 in the week's plan,
asked instead of reported.

**3. A gap that may be deliberate.** Fifteen recurring terms are in Q.1–Q.4 and
reach nothing in Q.5–Q.7 — tradition, urban sprawl, unplanned ignitions,
eradicated among them. Today the page states the gap. The useful form is: is
this deliberate, or missing? The engine cannot tell those apart. He can, in one
tap per term, and only for the two or three that carry a top finding.

**4. Grounding, asked where it matters.** Fifteen of his 24 notes have no voice
and fifteen have no source. Asking about all fifteen is a chore. Asking about
the one or two that carry the strongest thread is a real question: this note is
doing a lot of work here and is unattributed — who said it?

**5. Dots that tie to nothing.** Six share no thread (N5, N7, N18, N20, N22,
N24). The engine cannot read them, but it can ask whether they are new ground
or the same ideas in different words. That second branch is a vocabulary
question, which is why this class feeds the funnel.

**6. Repeated text in different places.** On Broadview the same sentence,
"Design educational and emotional transformation program.", is three separate
notes at three coordinates. The engine can ask whether that is one thing in
three places or three things that happen to share wording. On a place map that
distinction changes what the map means, and nothing today notices it.

**7. A missing name, now that it matters.** Broadview's `who` is empty. Since
v100 and v101 the map hover shows the author or falls back to the workbook
name, so on Broadview it shows nothing. Worth one prompt before a combine
rather than a silent blank.

**8. Vocabulary.** The funnel, already designed. Five to eight pairs, one tap
each.

Note that N20 appears in both class 1 and class 5. A single dot can raise more
than one question, so questions need de-duplicating per dot before any are
shown.

## Where the answers live

`C.decisions` is taken — it holds the Keep/Change/Drop choices on
course-of-action cards, keyed by `mode|heading`. Answers to these questions
need their own key on `C`, and it has to survive combine.

When two people answer the same question differently, that is the same conflict
the vocabulary architecture already resolves per group rather than per file, so
the resolution pattern exists and should be reused rather than reinvented.

## Rationing

A method that asks twenty questions has replaced one kind of clutter with
another, and would fail the same standard this note is written under. The
funnel's cap is the right model for all eight classes together, not for each:
five to eight questions total, one tap each, and only where the answer would
change what a top finding says.

Which questions those are depends on the ranking, so this leans on item 6 like
everything else.

## What it cannot ask

It cannot ask about claims, only about structure. "Your Q.5 designs tools and
media while your Q.2 says the obstacle is an occupational complex" is still
above the ceiling and still needs claim extraction or a language model, which
the elegance standard argues against.

Everything in the catalogue is a disagreement between two things the engine can
already see. That is the boundary.
