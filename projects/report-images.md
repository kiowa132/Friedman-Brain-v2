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
- **Left-edge text clip fix (superseded for report heroes — see below):**
  gpt-image-1 ignores "leave a margin" but respects a concrete visual
  anchor somewhat better than nothing. Put in the prompt: *"a thin
  warm-gold vertical hairline runs top-to-bottom ~12% in from the left
  edge; every letter sits to the right of it, nothing touches the left
  edge."* Still unreliable on its own — see the plate+composite method
  below, which is now the standard for Friedman Report hero banners.
- For a thin banner, also tell it the **top third is empty sky, bottom
  third is empty road** (blank trim margin) so the crop only removes
  emptiness.

## Friedman Report hero banner — proven method (confirmed 2026-09-13)
Baking title text into the AI image is unreliable no matter how the
prompt is worded — gpt-image-1 clips the first letter of left-aligned
lines often enough that it's not worth fighting. **Standard method now:
generate a completely text-free background plate, then composite the
title text on top with Python/Pillow for pixel-exact placement.**

1. **Generate a text-free plate.** Same brand-palette prompt as usual,
   but explicitly instruct *no text, no letters, no words, no numbers,
   no logos, no watermark anywhere in the image*. `-Quality high`
   (~$0.17), no `-Ref` needed (refs muddy the grade — see note above).
2. **Vary the scene/angle every week.** Don't reuse the same eye-level
   suburban-street-with-a-For-Sale-sign shot two weeks running — Kyle
   flagged this as "too basic" the second time. Good alternatives:
   an elevated three-quarter **aerial/drone view** over a neighborhood
   with several small signs scattered across different lawns (reads as
   "a wave of listings," ties to supply-surge stories), a different
   season/time-of-day treatment, a different property type/density.
   Pick something that matches that week's actual story angle.
3. **Crop to a 3:1 banner** (long and skinny, not square-ish) with
   Pillow — pick the vertical band that keeps the most interesting
   content (signage, rooflines), not a blind center-crop.
4. **Composite text with Pillow**, fonts substituted from what's on the
   Windows box (brand fonts Avenir Next / Mrs Eaves aren't installed
   locally):
   - Kicker: `C:\Windows\Fonts\ArialNova-Bold.ttf`, ~30px, gold
     `#C9A96A`, tracking +4px, uppercase
   - Headline: `C:\Windows\Fonts\georgiab.ttf` (Georgia Bold), **92px**
     — go big, this is the number one thing to get right — cream
     `#FAF8F5`
   - Subhead: `C:\Windows\Fonts\georgiai.ttf` (Georgia Italic), ~32px,
     gold
   - Wordmark ("THE FRIEDMAN TEAM"): `ArialNova-Bold.ttf`, ~32px, cream,
     tracking +2px
   - Vertically **center the whole text block** in the banner (compute
     total block height, center it, don't just top-align with a big gap
     before the wordmark)
   - Left margin: **5% of image width**, not less — this is what
     guarantees nothing clips, since it's real math now, not a model
     guess
   - Draw each text line with a **soft drop shadow** (offset ~2-3px,
     black at ~120 alpha) — this alone does most of the legibility work
   - **Left-side gradient scrim, but light:** a dark teal-black gradient
     (`~(6,16,18)`) from the left edge, peak alpha **~150** (not higher —
     215 read as "too dark" and killed the photo), fading out over
     **~50% of the image width**. Do **not** add a full-frame darken
     layer on top of the scrim — that flattened the whole photo and was
     the main complaint the first time; the scrim + drop shadow alone is
     enough contrast.
5. Save the composited PNG, then re-encode to a ~1600px-wide JPG
   (quality ~85-88) for web use, and copy it into
   `The-friedman-team-website/public/images/uploads/` with the exact
   frontmatter filename.

This fully sidesteps gpt-image-1's unreliable text rendering — nothing
can clip because placement is exact math, not a model guess. Use this
method by default for every future Friedman Report hero; don't go back
to baked-in AI text for this slot.
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
