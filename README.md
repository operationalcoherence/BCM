# BCM — The Bear Canyon Method web workbook

Operational Coherence. The workbook lives on
[operationalcoherence.com/gsmlive](https://operationalcoherence.com/gsmlive).

## What is in here

| file | what it is |
|---|---|
| `gsm-preview.js` | the preview workbook. Every new version lands here first. |
| `gsm-readable.js` | the same file, prettified, as a readable reference. Not loaded by any page. |
| `gsm.js` | the live workbook. Only ever a copy of a preview that was approved. |
| `webador_stub_PREVIEW.html` | paste once into the Webador block of the preview page |
| `webador_stub_LIVE.html` | paste once into the Webador block of the live page |

## How a version goes out

1. A new version is committed to `gsm-preview.js`. The preview page picks it up
   within a minute.
2. It gets looked at there.
3. If it is approved, `gsm-preview.js` is copied over `gsm.js`. That, and only
   that, changes the live page.

Nothing reaches `gsm.js` without someone deciding it should.

## The Esri key is not in this repository

The map's Esri key lives in the Webador block on the page, not here, and must
stay that way — this repository is public. The code reads it from
`window.GSM_ESRI_KEY`, which the stub sets.

The key should also be restricted by referrer in the ArcGIS developer dashboard
so it only works from operationalcoherence.com.

## Source

`gsm-preview.js` is the only thing the page runs, and it is minified. Since the
sandbox that held the readable source was lost, the repository is the source of
truth, so `gsm-readable.js` is kept here as the readable copy of it: the same
program, prettified to about 12,700 lines, verified to render identical output
across Pattern Analysis, Pattern Synthesis, In Parallel and Taking Action.

Nothing loads `gsm-readable.js`. It is for reading and for working out a change
before it is made. **Whenever `gsm-preview.js` changes, regenerate it**, or the
two drift apart and the next person reads a version that is no longer running:

    prettier --parser babel --print-width 110 gsm-preview.js > gsm-readable.js

## Documents

`docs/` holds the design and audit documents that go with the code. The
per-version notes (`groundsmith_web_vNN_update.md`) and the handoffs live in
the Claude project "Wildfire Design Industry".
