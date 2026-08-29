# brand-assets/

Reference images for the image pipeline (`scripts/gen-image.ps1`). Committed
to the repo. Pass the relevant ones with `-Ref` on every generation.

| File | What | Status |
|---|---|---|
| `swatch.png` | brand colors: `#0F5C63` teal · `#C9A96A` gold · `#FAF8F5` cream · `#0D2226` ink · `#B5544A` red | ✅ generated |
| `logo.png` | "FRIEDMAN" wordmark, teal + gold swoosh, transparent PNG | ⬜ Kyle to add |
| `logo-exp.png` | eXp Realty logo, black, transparent PNG | ⬜ Kyle to add |
| `headshot.jpg` | Kyle, cream suit, circular / head-and-shoulders | ⬜ Kyle to add |
| `kyle-portrait.jpg` | Kyle, full body, cream suit, textured teal/cream wall | ⬜ Kyle to add — best "with Kyle" reference |
| `lockup.png` | headshot + FRIEDMAN + eXp stacked lockup | ⬜ Kyle to add |
| `look-flyer.jpg` | the 2026 Home Seller's Guide flyer | ⬜ Kyle to add — **visual style reference only** |

## Naming caution
The `look-flyer.jpg` body copy and some older lockups say **"Friedman Real
Estate Team"**. That is NOT the canonical name (see
`../notes/brand-guidelines.md` — it's "The Friedman Team by Kyle Friedman",
never any "real estate" variant). Use the flyer for **layout / color /
type feel only**. For a wordmark the tool should reproduce, use `logo.png`
(just "FRIEDMAN") — never ask it to render "Friedman Real Estate Team".

## Adding the files
Save the images Kyle shared into this folder with the exact names above,
then commit. `.jpg` / `.png`, ~1024px on the long edge is plenty.
