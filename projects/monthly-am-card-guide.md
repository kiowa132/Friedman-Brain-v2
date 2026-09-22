# Monthly AM Card Guide (standing process, set 2026-09-21)

Each month's AM card carries a QR code that opens a new guide on friedmanreteam.com/guides. September was the Relocation Survival Guide; October is the Carroll County Town by Town Buyer's Guide. Plan: county buyer guides on rotation (Carroll, then Baltimore County, then Howard County, then others), so each month has a new reason to mail the card.

## Steps that worked (October 2026)
1. Pick the topic (Kyle's positioning: direct buyer questions for a specific area, plus his existing guides are broad, so area guides fill the gap).
2. Research and outline in `marketing/<month>-guide-<topic>/research-and-outline.md`. Numbers come from Kyle's Bright MLS pull (Stats button, closed sales by city, about 6 months, Residential): closed count, median sold price, median days to contract, sold vs. original list, active listings. Compute months of supply. Tax rates from the Maryland Dept. of Assessments and Taxation rate sheet (real property = municipal + county + state per $100).
3. Write `chatgpt-prompts.md`: one master style prompt (exact hex colors, type sizes, layout copied from the relocation guide) plus one prompt per page with every word. Rules learned: no bracketed notes in page prompts (ChatGPT prints them), no hyphens or dashes in page copy except the phone number, keep cards short so pages are not crowded, shrink photos to make room for text, tell ChatGPT not to zoom on Kyle's headshot.
4. Kyle generates pages in ChatGPT, checks numbers and spelling (send me pages to review). If a table page garbles, I build it in code.
5. Kyle exports a PDF and a zip of page PNGs (zip filenames may be stale; open every image and check the order).
6. I add it to the site: page images resized to 1000x1414 JPG in `public/images/guides/<slug>/` (page-01-cover.jpg, page-02.jpg ... page-NN-cta.jpg), a compressed PDF in `public/guides/` (a 30 MB PDF rebuilt from the page images to about 4 MB), a data file in `src/data/guides/`, and a line in `src/data/guides/index.ts`. Commit and push to main.
7. Kyle makes the QR code from the live URL (`/guides/<slug>`), puts it on the AM card. Card copy is separate.

## Not yet done for October
- AM card copy for the October card.
- Sitemap: the sitemap script only reads `content/guides` markdown, so the handbook-style guides are not in the sitemap.
- The guide's rate (6.95 percent, Sept 17) and figures are as of the pull; the 2026-2027 Maryland tax sheet was not yet posted, so re-check tax rates.
