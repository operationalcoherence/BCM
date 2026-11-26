# v282 · the color wash at 45%

His call, 25 Nov 2026 17:07, after a side-by-side of the 11-20 workbook at 60%, 45%, and 30% (same camera): "give me 45% (b)". Patch: tools/patches/v282_color_wash_45.py.

## What changed
- The emotion color over the rock, grass, and soil on line maps goes from 60% to 45% (`ALPHA` in tools/relief/relief.js). More of the rock and its bedding shows through; the five emotions stay easy to tell apart.
- Applies to every line-map 3D view: Pattern Analysis, the Taking Action card maps, and full screen.
- Place maps keep their own wash (0.42), unchanged.

## Lighting
Left as v255. He was shown three lightings (v255, a lower sun, softer and even) and said "the lighting levels all look the same to me". This closes the v255 lighting check.

## Checks
The v282 build renders pixel-identical to the 45% mockup he chose (11-20 workbook, tests/reliefshot.py, tab 3). No keys in either built file.
