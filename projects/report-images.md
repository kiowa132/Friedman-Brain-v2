# Report Images — Auto-Generation Pipeline

`scripts/gen-image.ps1` generates report images from a prompt. **Two
engines** — because genuinely-free API image generation has a real quality
ceiling (verified 2026-08).

## Engines

| | `openai` (USE THIS) | `pollinations` (default) | `gemini` |
|---|---|---|---|
| Cost | **~$0.04/image** (medium) — needs `OPENAI_API_KEY` + billing | **free**, no key | ~$0.03/image, needs billing (free tier = `limit:0` for images) |
| Text / logos / infographics | best-in-class | can't | good |
| Reference photos (`-Ref`) | yes (up to 4) | no | yes |
| Use for | **everything** — heroes, infographics, section art | throwaway background art only | reference-heavy shots / faces |

Kyle's call (2026-08): pay ~$0.04/image on **`openai`** and drop the
"do it in the web app" step. `pollinations` stays as the zero-cost
fallback; `gemini` stays wired for reference-heavy work if wanted.

## Run it
```
# openai — the normal path
powershell -File "Friedman Brain/scripts/gen-image.ps1" -Engine openai `
  -Prompt "Wide 16:9 editorial banner ..." `
  -Ref "brand-assets/logo.png","brand-assets/swatch.png" `
  -Out "properties/8303-bellona/generated/hero.png"

# add -Quality high for a hero that must be crisp (~$0.17); -Quality low for scratch (~$0.01)
# free fallback:
powershell -File "Friedman Brain/scripts/gen-image.ps1" -Prompt "..." -Out "...png"
```
Output → `../properties/<addr>/generated/` (gitignored scratch) or
straight to `The-friedman-team-website/public/images/uploads/` for blog
posts.

**Keeping a final:** when an image actually ships in a deliverable, run
`scripts/keep-image.ps1 -From <generated png> -Property <addr> -Name <slug>
-Prompt "<prompt used>" -Note "<what it's for>"`. It writes a compressed
~300 KB jpg into `properties/<addr>/final/` (committed) and appends the
prompt to `properties/<addr>/image-log.md`. `generated/` stays disposable.

## Notes
- `openai` size is `1536x1024` landscape by default (`-Size`). For a thin
  banner add **`-CropAspect "3:1"`** (also `21:9`, `16:9`) — center-crops
  after generation. Downscale to 1600x900 for blog heroes.
- **Left-edge text clip fix:** gpt-image-1 ignores "leave a margin" but
  respects a concrete visual anchor. Put in the prompt: *"a thin warm-gold
  vertical hairline runs top-to-bottom ~12% in from the left edge; every
  letter sits to the right of it, nothing touches the left edge."*
- For a thin banner, also tell it the **top third is empty sky, bottom
  third is empty road** (blank trim margin) so the crop only removes
  emptiness.
- **Refs are "content to blend," not "settings."** Tested 2026-08:
  passing `swatch.png` as a `-Ref` muddies the grade instead of matching
  it. So: put the **hex values in the prompt text** (`deep teal #0F5C63`
  …), and reserve `-Ref` for things that should literally appear —
  `logo.png` (wordmark repro), a property photo (match its look), a
  headshot (face). Often the cleanest banner has **no refs at all**, just
  a detailed prompt.
- Real faces from the headshot are still inconsistent on any engine.
  "With Kyle" hero = real photo + Canva unless a test proves otherwise.
- Set an OpenAI **budget cap** so a loop can't run away.

## Spend tally (rough)
- 2026-08: pipeline build + 8303 Bellona test images (~8 medium generations) ≈ **$0.35**

## Brand constants for every prompt
Deep teal `#0F5C63`, warm gold `#C9A96A`, cream `#FAF8F5`, ink `#0D2226`,
loss-red `#B5544A`. Editorial real-estate / finance photography, restrained
and premium. Baked-in text is wanted; spelling must be correct. Wordmark
reads **"The Friedman Team"** — never "Friedman Real Estate Team". Negative
list: no extra logos, no watermark, no warped text.

---

## Prompt templates by report slot

Placeholders: `{HEADLINE}`, `{KICKER}`, `{SUBJECT_PHOTO}`, `{ADDRESS}`.
Always pass `brand-assets/logo.png` + `brand-assets/swatch.png` as refs,
plus any look/photo refs noted.

### blog-hero (16:9) — `<slug>-hero.png`
> Wide cinematic hero banner for a real-estate strategy article. {SCENE — a
> tasteful, on-topic editorial photo}. Golden-hour light, restrained grade
> in deep teal shadows / warm gold highlights / soft cream mid-tones, fine
> grain, gentle vignette. Left two-thirds is open, with a soft
> teal-to-transparent scrim for text. Lay in: gold letter-spaced kicker
> "{KICKER}" upper-left; large serif headline "{HEADLINE}" in warm white; a
> thin gold rule; "The Friedman Team" wordmark lower-left (reproduce the
> uploaded logo). Match colors to the uploaded swatch. No people, no
> misspelled text.
Refs: logo, swatch.

### blog-infographic (16:9) — `<slug>-<name>.png`
> Wide branded explainer graphic, clean financial-editorial infographic
> style. {DESCRIBE the cards / bars / diagram and the exact figures}. Cream
> cards with thin gold borders and soft shadows; labels in small uppercase
> letter-spaced teal; figures in a Georgia-style serif in near-black.
> Kicker "{KICKER}" upper-left; small teal footer "The Friedman Team ·
> Numbers Over Guesswork" lower-right. Crisp, correctly spelled text. No
> people, no photoreal clutter.
Refs: logo, swatch, a site stat-card screenshot if available.

### listing-hero (16:9) — `properties/<addr>/generated/listing-hero.png`
> Wide cinematic hero banner for a home listing at {ADDRESS}. Generate an
> upscale exterior in the style and character of the uploaded property
> photo — same architecture, materials, and setting — at golden hour,
> restrained premium grade. Right two-thirds is the house; left third is a
> soft teal scrim for text. Kicker "JUST LISTED" in gold; address
> "{ADDRESS}" in serif; "The Friedman Team" wordmark lower-left. No people,
> no misspelled text, no extra signage.
Refs: `properties/<addr>/photos/<front>.jpg`, logo, swatch.

### report-section-art (16:9) — concept art for a Gamma section
> Wide editorial concept image for the "{SECTION}" section of a client
> report. {METAPHOR — e.g. a balance scale of a house model vs. a stack of
> cash; a set of keys on a contract; a fork in a suburban road}. Minimalist
> finance-magazine style, cream background, teal/gold palette from the
> uploaded swatch, soft studio light. Optional small kicker "{KICKER}" in
> gold uppercase. No people, no clutter, no text beyond the kicker.
Refs: swatch (logo optional).

### agent-portrait (16:9) — `with-kyle.png` (expect re-runs)
> Wide editorial banner. A real-estate advisor — use the uploaded headshot
> as an exact face reference — at the right edge in a charcoal blazer, calm
> confident half-smile, blurred bright office behind. Left two-thirds is a
> teal-graded wall with a scrim for text: kicker "{KICKER}", serif line
> "{HEADLINE}". "The Friedman Team" wordmark lower-left. Face must match the
> reference with no distortion. No other people, no warped features.
Refs: `brand-assets/headshot.jpg`, logo, swatch.

---

## Slot maps by report type

All slots below run on `-Engine openai`. The 🆓 ones are also acceptable on
the free `pollinations` engine if avoiding spend; ✋ ones need `openai`
(headline text / logo / precision).

### Blog article (see `blog-article.md`)
Blog markdown already has the `<img src>` slots wired. Files go in
`The-friedman-team-website/public/images/uploads/` with the exact
frontmatter filenames:
- ✋ `<slug>-hero.png` → blog-hero template (headline + logo)
- ✋ `<slug>-<name>.png` (stepup / gap / etc.) → blog-infographic template
- ✋ `<slug>-two-numbers.png` / "with Kyle" → agent-portrait template

### Sell-vs-Rent client report (see `sell-vs-rent-analysis.md`)
Gamma document. Section art can be free:
- ✋ **Cover** → listing-hero (needs address text; web or gemini engine)
- 🆓 **The tax picture** → section art, metaphor: a balance scale, a house
  model vs. a stack of cash
- 🆓 **Rent — risks** → section art: a wrench and a calendar on an older
  kitchen counter
- 🆓 **HELOC option** → section art: a house with a faucet drawing coins
- **Side-by-side / 5-year** → skip art; the tables carry it

Generated 8303 Bellona example: `properties/8303-bellona/generated/section-tax.png`

### Listing presentation (see `listing-presentation.md`)
- Cover → listing-hero
- Any "our marketing" section → blog-infographic style stat cards

---

## Adding a new report type
1. Add its slot map above.
2. Reuse a template, or add a new one with the brand constants block.
3. Kyle drops photos → name the report → generate + wire in.
