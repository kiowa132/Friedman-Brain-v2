# Blog Article Maker — Standing Procedure

Generalized from the original Friday-only version. Handles two separate
request types — read which one applies before starting.

## What every finished article is — 5 deliverables
1. **Substack version** (`substack.md`) — conversational, first person,
   contractions, light headers. **Roughly 1,000-1,300 words, and always
   shorter than the website version.** Data woven into the narrative, not a
   formal H2 outline. **Vary the lead** — sometimes a named-client story
   (Dave & Michelle, Priya, Renee style), sometimes a scene, stat, or
   scenario hook. Don't open every edition with a client anecdote; it gets
   repetitive. Close with the contact block, then the signature:
   ```
   Have Questions? Let's Talk.
   📞 443-789-3101 | Kyle@friedmanreteam.com
   8115 Maple Lawn Blvd. #350 Fulton, MD 20759

   — Kyle Friedman, The Friedman Team
   ```
2. **Website version** (`website-seo.md`) — longer, structured for search,
   and **coded in the live website's format** (content markdown with YAML
   frontmatter + inline-styled HTML furniture; the site is Vite/React and
   runs the body through `marked`, so raw inline HTML in the markdown
   renders). Drop-in ready for
   `The-friedman-team-website/content/blog/<slug>.md`.
   **Roughly 1,300-1,800 words of prose, longer than the Substack version.**
   Reference files (match their conventions):
   - Market-report format:
     `.../content/blog/maryland-real-estate-market-report-week-of-august-17-23-2026.md`
   - Evergreen buyer/seller format:
     `.../content/blog/what-buying-above-500k-actually-looks-like-in-carroll-county-maryland.md`

   **YAML frontmatter** (top-level keys must start at column 0):
   - `title` — full H1 headline in quotes (house style: hook, colon,
     keyword clarifier — e.g. "What Zillow Doesn't Tell You: ...")
   - `metaDescription` — ≤155 chars, in quotes (also renders as the on-page
     dek under the H1)
   - `category` — exactly one of `Buy a Home`, `Sell Your Home`,
     `Market Reports` (drives the related-posts logic and the category link)
   - `publishDate` — `"YYYY-MM-DD"`
   - `heroImage` — `/images/uploads/<slug>-hero.png`. Actual file goes in
     `The-friedman-team-website/public/images/uploads/`. Recommend export
     at 1600×900, under 500KB; it's center-cropped to 16:9
   - `youtubeVideoId: ""` — set the real ID from deliverable 4 later. Only
     add `youtubeIsShort: true` when there's an actual short
   - `relatedAreaSlug` — optional, a real neighborhood id (e.g.
     `carroll-county`)
   - `carouselImages` — optional YAML list. **The page auto-interleaves
     these evenly through the body.** So use it ONLY for standalone
     lifestyle photos that can sit anywhere. Any graphic that must sit next
     to a specific section is a manual `<img>` in the body instead — and
     must NOT also appear in `carouselImages` (it would render twice).
   Track the target keyword in the brain draft only — no stray HTML comment
   in the shipped file. `blogManifest.json` and the sitemap regenerate
   automatically at build; never hand-edit them.

   **Body structure**, in order:
   - Open with a short illustrative buyer/seller scenario (first name only,
     e.g. "Marcus has been playing it patient all summer"), then a
     turn/stakes line. The first paragraph auto-gets larger "lead" styling
     — make it a strong standalone hook.
   - A bold **`Quick answer:`** paragraph (~60-100 words) OR a `>` pull
     quote near the top — the whole topic answered in one block
   - H2 sections built around real search queries, each grounded in
     concrete Maryland numbers/examples, not generalities
   - **Use the website content card system** (see
     `../notes/brand-guidelines.md` → "Website content card system" for the
     exact color/style tokens — don't reinvent them):
     - Stat-tile grid (inline-styled `<div>` grid) for any set of key
       figures — with ▲/▼ deltas where a comparison exists
     - Styled callout `<div>` for worked examples and any data note
     - For an options / trade-off comparison, use **stacked inline-styled
       cards** (one `<div>` per option), NOT a wide `<table>` — the site
       forces tables to `white-space:nowrap` + horizontal scroll, which
       mangles long cell text. Reserve markdown tables for short tabular
       data, the way the market reports use them.
     - Chart/diagram embeds where a visual explains it better:
       `<img src="/images/uploads/<slug>-<name>.png" alt="[takeaway]"
       style="width:100%;height:auto;margin:24px 0;" />` placed right after
       the paragraph it illustrates. List any asset that still needs to be
       produced in the delivery message; never hard-link a missing file
       without flagging it.
   - A "What to do before…" / "One thing I'd do" checklist section
   - A "The Bottom Line" section
   - A "Frequently Asked Questions" section — 4-5 Q&As, each a real search
     query as `**Question?**` followed by a tight answer paragraph
     (schema-friendly), matching the reference file's FAQ formatting
   - **Evergreen Buy/Sell posts END at the FAQ.** The page component
     auto-appends the valuation banner, subscribe cards, Meet-the-Author
     block, the "Have Questions? Let's Talk" contact block (phone / email /
     Maple Lawn address) and Kyle's signature image — so do NOT put a
     "Your Next Move" CTA section or a "— Kyle Friedman" text sign-off in
     the body. Weave 1-2 internal links (other posts, tool pages) into the
     body prose instead. (Only the market-report format ends with a short
     "Your Next Move Starts Here" + two links.)
   These two versions cover the same topic and points but are NOT the same
   text reformatted — write each for how it's actually consumed.
3. **Google Business Profile post** (`gbp-post.md`) — plain text, GBP
   renders no markdown. Reference: this folder's `gbp-post.md` for
   `2026-09-escalation-appraisal-gap`.
   - A **long version** ~1,200-1,450 chars (GBP hard limit is 1,500) and a
     **short version** ~140 words — Kyle picks which to post
   - First line is a standalone hook (GBP truncates to ~75 chars before
     "Read more")
   - Work in the county names (Carroll, Baltimore, Howard, Frederick) for
     local search; no hashtags
   - End with `📞 443-789-3101 — The Friedman Team | Numbers Over Guesswork`
   - CTA button: **Learn more** → the published post URL
     `https://www.friedmanreteam.com/blog/<slug>`
   - Note which image to attach (usually the hero or a body graphic)
   - Match the article's primary angle; a short seller-angle alt is a nice
     extra when the topic cuts both ways
4. **4 detailed image prompts** for a modern reference-image tool
   (ChatGPT / Midjourney / Nano Banana etc.). These are **not** one-line
   prompts. Each prompt block has four parts:
   - **Filename** — exact `slug-name.png` matching the article frontmatter
   - **Size** — an explicit line, e.g. `1792×1024 px — 16:9 horizontal
     landscape banner. Set this in the tool's aspect-ratio control.` Every
     block carries this; never leave size implied in prose only
   - **Reference assets to upload** — name which of Kyle's files to attach
     so the output isn't generic: his professional headshot (face/character
     reference), screenshots of the live friedmanreteam.com site (match
     type, layout, the stat-card system), the logo / wordmark PNG
     (transparent), a brand color swatch, and phone photos of Kyle's
     printed buyer/seller guides or existing collateral (paper stock,
     layout, brand feel)
   - **In-image text** — exact copy and placement. Text baked into the
     image is wanted now: kicker, serif headline, stat labels, and a
     `The Friedman Team` wordmark lockup. Always instruct the tool that
     spelling must be correct and text naturally integrated. **The negative
     list must forbid the string "REAL ESTATE" anywhere in the image** —
     tools keep inventing a "FRIEDMAN REAL ESTATE TEAM" logo, which
     violates the naming rule. Upload the real transparent LOGO every time
     and tell the tool to reproduce it exactly, not design its own
   - **The prompt** — spell out scene, subject, composition (explicitly
     reserve a side/third for the headline with a soft gradient scrim),
     lens / focal length / aperture, lighting, color grade citing the brand
     hex values (`#0F5C63` teal, `#C9A96A` gold, `#FAF8F5` cream, `#0D2226`
     ink, `#B5544A` loss-red), textures, post (grain, vignette), the style
     references being uploaded, aspect ratio, and a negative list
   **All prompts are banner / landscape (~16:9, crops cleanly to 3:1)**
   unless a specific prompt notes a different ratio. Tools ignore "16:9"
   written in prose — the prompt block must tell Kyle to set the ratio with
   the tool's own control (ChatGPT: "wide 16:9 landscape 1792×1024";
   Midjourney: `--ar 16:9`; others: the landscape preset; or upload a blank
   1920×1080 canvas as a reference frame). Consistent brand grading — see
   `../notes/brand-guidelines.md`. At least one of the four should use
   Kyle's uploaded headshot to put him in the frame.
5. **A 15–20 second social video script** (`video-script.md`) — an actual
   spoken script (the words Kyle says, ~45-55 words), plus a beat-by-beat
   "say this / show this" table and delivery notes. Story/hook-driven, NOT
   reciting data. Don't default every script to "a buyer I know…" — vary
   the opening device, and consider the seller's-agent POV.

## Mode 1 — On-demand ("I need an article about X")
Kyle names a topic directly, any day, any time.
1. Check `blog-article-log.md` — if this topic's already been covered,
   flag it to Kyle rather than silently duplicating; he may still want a
   fresh angle on it, but ask first.
2. Research it (web search — don't state Maryland-specific legal/tax/
   financing facts from memory alone).
3. Write all 5 deliverables: Substack version + website version + Google
   Business Profile post + 4 image prompts + video script.
4. Deliver directly to Kyle — no queue detour needed for an on-demand
   request.
5. Log it in `blog-article-log.md`.

## Mode 2 — Standing Friday queue (Kyle picks from ready options)
The queue should hold **multiple ready articles at once** (aim for at
least 3), so Kyle is choosing which one to run, not just accepting
whatever's next.

**Batch/refill session** (whenever the queue drops below ~3 ready items):
1. Check `blog-article-log.md` and `blog-article-queue.md` — never repeat
   a topic in either.
2. Propose new topic candidates to Kyle first — don't write on spec.
   Favor topics reinforcing brand positioning (see
   `../notes/brand-guidelines.md`), especially the farm/equestrian niche.
3. Once approved, research and fully write each one (all 5 deliverables:
   Substack + website + GBP post + image prompts + video script), save to
   `../drafts/blog-articles/<date-slug>/`, add to `blog-article-queue.md`
   as "ready" with a one-line summary — no fixed Friday date attached.

**Weekly Thursday check** (by Thursday, not Friday):
1. Read `blog-article-queue.md` — surface the full list of ready items
   with their one-line summaries to Kyle.
2. Kyle picks which one runs this week. Move that one from the queue to
   `blog-article-log.md`; the rest stay in the queue for a future week.
3. If fewer than 3 ready items remain after Kyle's pick, that's the
   trigger to run a refill batch session before next Thursday.

## Standing build rules
- Branding & tone: follow `../notes/brand-guidelines.md` — don't duplicate
  those rules here, check there.
- Putting Kyle in an image is fine when it's driven by his uploaded
  headshot as a face/character reference (not free-generated from a text
  description). For a hero where his face is the focus and must be exact, a
  real photo composited in Canva is still the safest route — but a
  reference-image tool is now acceptable.
- Baked-in image text is wanted (headline, kicker, stat labels, wordmark).
  Every prompt must specify exact copy and placement and tell the tool
  spelling must be correct. Canva is still fine for final text cleanup, but
  don't strip text out of the prompts.
- Every prompt should lean on uploaded reference assets (headshot, live
  site screenshots, logo, brand swatch, photos of Kyle's printed guides) so
  outputs match the brand instead of looking like generic stock.
