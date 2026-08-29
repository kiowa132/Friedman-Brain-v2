# scripts/

PowerShell tools for the report-image pipeline. Windows PowerShell 5.1 —
nothing to install. Run from the repo root (`Friedman Brain/`).

## Setup (once)
1. `copy scripts\.env.example scripts\.env`
2. Paste keys into `scripts\.env`:
   - `OPENAI_API_KEY` — the engine we use. platform.openai.com → Billing →
     load $5 + set a **monthly budget cap** in Limits. ~$0.04/image.
   - `GEMINI_API_KEY` — optional; image gen needs billing on (free tier is
     `limit:0`).
3. `scripts/.env` is gitignored — keys never commit.

## gen-image.ps1 — generate an image
```
powershell -File "Friedman Brain/scripts/gen-image.ps1" -Engine openai `
  -Prompt "Wide 16:9 editorial banner ..." `
  -Ref "brand-assets/logo.png" `           # optional; logo/photo/face only, NOT the swatch
  -CropAspect "3:1" `                       # optional thin-banner crop
  -Out "properties/8303-bellona/generated/hero.png"
```
- `-Engine` : `openai` (use this) · `pollinations` (free, weak) · `gemini`
- `-Quality`: `low` ~$0.01 · `medium` (default) ~$0.04 · `high` ~$0.17
- `-Ref`    : up to 4 local images. Put **hex colors in the prompt text**,
  not a swatch ref (tested: swatch-as-ref muddies the grade).
- Output → `properties/<addr>/generated/` (gitignored scratch).

## keep-image.ps1 — promote a keeper
Run only for an image that actually shipped.
```
powershell -File "Friedman Brain/scripts/keep-image.ps1" `
  -From "properties/8303-bellona/generated/hero.png" `
  -Property "8303-bellona" -As "sell-vs-rent-cover" `
  -Prompt "<the prompt used>" -Note "<what it's for>"
```
Writes a ~120 KB jpg to `properties/<addr>/final/` (committed) and logs
the prompt to `properties/<addr>/image-log.md`.

## Full guide
`../projects/report-images.md` — prompt templates, slot maps per report
type, the generated/final workflow.
