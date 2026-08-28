# Brand Guidelines

## Naming
- Everyday brand / short form: **The Friedman Team** — always. Never
  "Friedman Real Estate Team" or any variant containing "real estate."
- **Canonical business name for citations / NAP / schema:**
  **"The Friedman Team by Kyle Friedman"** — this is the Google Business
  Profile name (decided 2026-08). Use this exact string wherever a business
  name is a structured field: JSON-LD `name`, Zillow / Realtor.com /
  Homes.com / Bright MLS profiles, directory listings. Prose/headings still
  use the short "The Friedman Team".
- Canonical address (match GBP exactly): 8115 Maple Lawn Blvd Suite 350,
  Fulton, MD 20759. Phone: (443) 789-3101.
- Professional email: kyle@friedmanreteam.com (not PenFedRealty or
  CornerHouseRealty — both retired addresses).

## Visual identity — website (current)
- Deep teal `#0F5C63`, warm gold `#C9A96A`
- Avenir Next for headings, Mrs Eaves Italic for editorial accents
- Supersedes the older Aurum/Gold Leaf Gamma theme

### Website content card system (blog posts & reports)
Reference implementation:
`The-friedman-team-website/content/blog/maryland-real-estate-market-report-week-of-august-17-23-2026.md`
Every coded website article (see `../projects/blog-article.md` deliverable 2)
uses this same inline-styled system — no external CSS, safe for the Hugo
markdown pipeline.
- Card background `#FAF8F5`, border `#C9A96A55` (gold at ~33% alpha)
- Card label: `#0D222699`, 11px, 700, uppercase, `letter-spacing:0.06em`
- Figure/value: `font-family:Georgia,serif`, 24px, 800, color `#0D2226`
- Positive / good delta: `#0F5C63` with `&#9650;` (▲)
- Negative / bad delta: `#B5544A` with `&#9660;` (▼)
- Stat-tile grid wrapper:
  `display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,1fr));gap:10px;margin:24px 0;`
- Section-label caption: centered, `#0F5C63`, uppercase,
  `letter-spacing:0.08em`, 13px, 700
- Pull quotes: markdown `>` blockquote
- Charts/diagrams: SVG assets at
  `/images/uploads/charts/<post-slug>/<name>.svg`, embedded as
  `<img src="…" alt="[describe the takeaway]" style="width:100%;height:auto;margin:20px 0;" />`

## Visual identity — Gamma decks (open question — see decisions.md)
- Listing presentation decks currently use Gamma theme `aurum`
  (`themeId: aurum`, `textMode: preserve`, `cardSplit: inputTextBreaks`)
- Friedman Report uses a separate custom Gamma theme
  (`themeId: m6zymtbkauah9qd`)
- Neither has been confirmed to move to the new teal/gold identity yet.

## Brand direction
- Shifting toward $400K+ and luxury clientele — away from investor-grade /
  wholesaler voice. Applies across all content: report, listing materials,
  social, email tone.

## Positioning
- Core brand mission: "Numbers Over Guesswork"
- Core values: honesty, empowerment over pressure
- Farm, equestrian, and country estate niche in Carroll County — identified
  as an authentic, unclaimed positioning opportunity
