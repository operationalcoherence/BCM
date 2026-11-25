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

**Since v171, `gsm-readable.js` is the source.** Edit it, then build the file the page
runs:

    npx esbuild@0.24 gsm-readable.js --minify --outfile=gsm-preview.js

(Tested on unchanged v170: the esbuild output rendered byte-identical text on every tab.
Exact-string patching of the minified file, used v95 to v170, is retired, and so are the
`tools/terrain` rebuild scripts, which start from an old v150 engine.)

From v266 to v268 the Pattern Synthesis graph modules were bundled ahead of the engine. Since v269 (Pattern
Synthesis retired) they are not: `tools/graph/` stays in the repository, unwired, and the one-file build above is
the build.

The 3D relief module `gsm-relief.js` is built from `tools/relief/relief.js` with
three@0.187.0:

    npx esbuild tools/relief/relief.js --bundle --minify --format=iife --outfile=gsm-relief.js

Each version's batch of edits is kept as a script in `tools/patches/`.

Project memory (architecture, current state, task queue, concept registry) is in
`docs/bcm/`.

## Documents

`docs/` holds the design and audit documents that go with the code. The
per-version notes (`groundsmith_web_vNN_update.md`) and the handoffs live in
the Claude project "Wildfire Design Industry".
