# v246 (preview only) — 2026-11-19

His ask (11-19 14:13): "for the tours in both place mapping ... and the line map tour in analysis and synthesis - i would like a forward and backward buttons but more importantly, I would like what is being talked about to be illuminated somehow, with a spot light, a white glow or outline that doesn't occlude the color, something so that its very easy for people to tell what and where the focus is."

Every tour, line map and place map, on Analysis and Synthesis:

1. **The focus glows.** A white ring sits on the ground around the spot each stop talks about: a thin bright line inside a soft, wide glow, gently pulsing. It is an outline, so the colors inside stay visible. It's drawn over the land, so a hill never hides it. Stops with no spot (the opening, What a move costs) show no ring.
2. **The notes the caption names light up** (N5, P3, and so on): each gets a white glowing badge while its stop is on.
3. **Back and Next** sit beside Play/Pause while the tour runs. They jump to the stop before or after and play on from there. Next on the last stop ends the tour. End tour and Escape still end it and clear the glow.

**Checked:** tour.py on the clinic line map and on Broadview (place): Next moves on, Back goes back, pause and resume, and Escape ends and clears the glow, with no errors. Screenshot on the clinic map: ring around stop 2, with N5, N6, and N7 glowing. tour_an.py clean. Matrix clean. Keys: none. tour.py now reads the Play button by its class (.tpb), since Back is the bar's first button, and checks Back, Next, and the glow.

**Possible confusion:** the ring is white, like the goal's rings. It's a single ring that pulses, and it moves with the tour. Say if it should be another color.
