# v300 — place-map Taking Action cards stop talking about ground that isn't there

His go-ahead, 26 Nov 2026 07:10 ("Yes fix that next"), on what v299 found on Broadview's "holds" card:
WHAT IT WILL TAKE read "the ridge at has heard many stories of homes", spoke of a ridge on a place map, and
showed P1/P3/P5 where the rest of the card shows N1.

His rule (19 Nov 2026): on a place map the hills, hollows, and ridges are the real land and have nothing to do with
the notes. So on a place-only workbook the cards now name emotions, not ground:

- WHAT IT WILL TAKE / THE WAY ACROSS: "indifference at …" not "the ridge at …"; "a big jump" not "a climb over bare
  rock"; "Short of indifference, behaviors first; from indifference on, emotions first".
- FIRST MOVES: "through the indifference at N3"; "Where people hold defiance, bring the behavior before its label…".
- Strategy or program: "it works with the emotions slowest to move" / "it already stands in acceptance".
- PWAY: "Already in acceptance: no crossing"; "close by in indifference" not "at its edge on the ridge".
- The card section WHAT HOLDS IT IN THE LOW GROUND is WHAT HOLDS IT WHERE IT IS on place-only workbooks, and its
  question reads "What constraint or rule keeps this note where it is…" (reworded, not removed). Help list matches.

Everywhere (line maps too): the user's words in WHAT IT WILL TAKE are in quotes, so the sentence reads
("the ridge at “hospital board sees the satellite clinic” N1"). Grey labels on the card strip show what the page
shows: N5, or "N5 (place)" on a both-maps workbook.

Checks: no ridge/rock/low ground/high ground/P-label text on any Broadview card or on a made-up place-only storefront
workbook (tests/wb_store_place.json, kept local). Line-map and both-maps workbooks: Taking Action text identical to
v299 except the added quotes (wb_cause). vague_titles.py passes. No page errors.
