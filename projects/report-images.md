# Report Images — Auto-Generation Pipeline

`scripts/gen-image.ps1` generates report images from a prompt. **Two
engines** — because genuinely-free API image generation has a real quality
ceiling (verified 2026-08).

## Engines

| | `pollinations` (DEFAULT) | `gemini` |
|---|---|---|
| Cost | **100% free**, no key, no billing | ~$0.03-0.04/image — **needs a billing-enabled Google key** (free tier is `limit: 0` for the image model) |
| Quality | Flux-schnell — good for atmospheric backgrounds / concept art; **weak on baked-in text + logos; ~1000px output** | Top tier — clean text, logos, precise composition |
| Reference photos (`-Ref`) | No (text-to-image only) | Yes — up to 4 local photos sent inline |
| Use for | section/background art in Gamma reports | hero banners, infographics, "my real listing look" |

Kyle's call (2026-08): **stay free.** So: use `pollinations` for
decorative/section art, and keep making the polished headline banners in
the **ChatGPT / Gemini web app** (free there, ~2 min each) using the
prompt templates below. `gemini` engine is wired and ready if billing is
ever switched on.

## Run it
```
# free
powershell -File "Friedman Brain/scripts/gen-image.ps1" `
  -Prompt "Wide editorial concept image, ..." `
  -Out "properties/8303-bellona/generated/section-tax.png"

# gemini (only if billing enabled)
powershell -File "Friedman Brain/scripts/gen-image.ps1" -Engine gemini `
  -Prompt "..." -Ref "brand-assets/logo.png","properties/8303-bellona/photos/front.jpg" `
  -Out "properties/8303-bellona/generated/hero.png"
```
Output → `../properties/<addr>/generated/` (gitignored) or straight to the
website repo's `public/images/uploads/` for blog posts.

## Known limits
- Pollinations caps resolution (~1000px) and is loose on specific
  composition — don't expect it to nail "a house model AND a cash stack on
  a scale"; expect a vibe, not a diagram.
- No free option does baked-in headline text or a clean logo. Those slots
  = ChatGPT/Gemini web, or the `gemini` engine with billing.
- Real faces from the headshot are inconsistent everywhere. "With Kyle"
  slot = real photo + Canva.

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

**Legend:** 🆓 = fine on the free `pollinations` engine · ✋ = do in
ChatGPT/Gemini web (needs headline text / logo / precision).

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
