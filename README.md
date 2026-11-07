# BCM — The Bear Canyon Method web workbook

Operational Coherence. The workbook lives on
[operationalcoherence.com/gsmlive](https://operationalcoherence.com/gsmlive).

## What is in here

| file | what it is |
|---|---|
| `gsm-preview.js` | the preview workbook. Every new version lands here first. |
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

The readable source and the per-version notes live in the Claude project
"Wildfire Design Industry", as `claude/groundsmith_web_vNN_update.md`.
