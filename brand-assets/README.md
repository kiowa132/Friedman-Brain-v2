# brand-assets/

Reference images for the image pipeline (`scripts/gen-image.ps1`).
**Committed to the repo.** Pass the relevant ones with `-Ref` on a
generation.

| File | What | Use as `-Ref` for |
|---|---|---|
| `swatch.png` | brand colors: `#0F5C63` teal · `#C9A96A` gold · `#FAF8F5` cream · `#0D2226` ink · `#B5544A` red | every generation (palette lock) |
| `logo.png` | "FRIEDMAN" wordmark, teal + gold swoosh, transparent | every branded graphic (wordmark repro) |
| `logo-exp.png` | eXp Realty logo, black | when the eXp mark is needed |
| `lockup.png` | headshot + FRIEDMAN + eXp stacked lockup | reference for a full brand lockup |
| `headshot.jpg` | Kyle, cream suit, textured wall — cleanest face | "with Kyle" face reference |
| `kyle-portrait.png` | Kyle full-body **cutout**, transparent bg | compositing Kyle into a scene |
| `kyle-in-home.jpg` | Kyle standing in a staged room | "Kyle at a property" reference |

## Naming caution
Older lockups / flyers say **"Friedman Real Estate Team"** — NOT the
canonical name (see `../notes/brand-guidelines.md`: it's "The Friedman
Team by Kyle Friedman", never any "real estate" variant). `logo.png` is
just "FRIEDMAN" and is safe to reproduce. Never have the tool render
"Friedman Real Estate Team".

## Faces
Real faces from a single photo are still inconsistent on every engine.
For a hero where Kyle's face must be exact, composite a real photo in
Canva rather than trusting the generator.
