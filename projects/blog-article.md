# Blog Article Maker — Standing Procedure

Generalized from the original Friday-only version. Handles two separate
request types — read which one applies before starting.

## What every finished article is — 4 deliverables
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
   and **coded in the live website's format** (Hugo content markdown with
   YAML frontmatter + inline-styled HTML furniture). This file should be
   drop-in ready for `The-friedman-team-website/content/blog/<slug>.md`.
   **Roughly 1,300-1,800 words of prose, longer than the Substack version.**
   Reference file (match its conventions):
   `The-friedman-team-website/content/blog/maryland-real-estate-market-report-week-of-august-17-23-2026.md`

   **YAML frontmatter** (top of file, between `---` fences):
   - `title` — full H1 headline in quotes
   - `metaDescription` — ≤155 chars, in quotes
   - `category` — e.g. `Buyer Strategy`, `Seller Strategy`, `Market Reports`
   - `publishDate` — `"YYYY-MM-DD"`
   - `heroImage` — `/images/uploads/...` (leave a clearly-marked TODO path
     if the asset doesn't exist yet)
   - `carouselImages` — optional YAML list
   - `youtubeVideoId` / `youtubeIsShort` — from deliverable 4; leave
     `youtubeVideoId: ""` with a TODO if not filmed yet
   Also keep a plain-text **Target keyword/phrase** line as an HTML comment
   just under the frontmatter so it's not lost.

   **Body structure**, in order:
   - Open with a short illustrative buyer/seller scenario (first name only,
     e.g. "Marcus has been playing it patient all summer"), then a
     turn/stakes line
   - A bold **`Quick answer:`** paragraph (~60-100 words) OR a `>` pull
     quote near the top — the whole topic answered in one block
   - H2 sections built around real search queries, each grounded in
     concrete Maryland numbers/examples, not generalities
   - **Use the website content card system** (see
     `../notes/brand-guidelines.md` → "Website content card system" for the
     exact color/style tokens — don't reinvent them):
     - Stat-tile grid (inline-styled `<div>` grid) for any set of key
       figures — with ▲/▼ deltas where a comparison exists
     - Inline-styled HTML `<table>` for options / trade-off comparisons
     - Styled callout `<div>` for worked examples and any data-transparency
       note
     - SVG chart/diagram embeds where a visual explains it better:
       `<img src="/images/uploads/charts/<slug>/<name>.svg" alt="[takeaway]"
       style="width:100%;height:auto;margin:20px 0;" />` — list the SVGs
       that need to be produced in the delivery message; never hard-link a
       missing asset without flagging it
     - Centered uppercase section-label caption where it adds a beat
   - A "What to do before…" / "One thing I'd do" checklist section
   - A "The Bottom Line" section
   - A "Frequently Asked Questions" section — 4-5 Q&As, each a real search
     query as `**Question?**` followed by a tight answer paragraph
     (schema-friendly), matching the reference file's FAQ formatting
   - Close with a "Your Next Move Starts Here" CTA section: internal links
     to friedmanreteam.com articles / neighborhood / tool pages (valuation,
     calculators) worked in naturally, county mention (Carroll, Baltimore,
     Howard, Frederick), signature "— Kyle Friedman, The Friedman Team"
   These two versions cover the same topic and points but are NOT the same
   text reformatted — write each for how it's actually consumed.
3. **4 detailed image prompts** for use in ChatGPT/DALL-E/Midjourney
4. **A 15–20 second social video script** — story/hook-driven, NOT Kyle
   reciting data to camera. Hook in first 2-3s, a turn/twist, short payoff.
   Time-coded table (time / visual+edit direction / audio or on-screen
   text).

## Mode 1 — On-demand ("I need an article about X")
Kyle names a topic directly, any day, any time.
1. Check `blog-article-log.md` — if this topic's already been covered,
   flag it to Kyle rather than silently duplicating; he may still want a
   fresh angle on it, but ask first.
2. Research it (web search — don't state Maryland-specific legal/tax/
   financing facts from memory alone).
3. Write the Substack version + website SEO version + 4 image prompts +
   video script.
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
3. Once approved, research and fully write each one (Substack version +
   website SEO version + 4 image prompts + video script), save to
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
- Never generate Kyle's actual face via AI image tools — text-to-image
  tools can't reliably reproduce a specific real person anyway. If Kyle
  wants himself in a graphic: use a real photo + add text/graphics in
  Canva, not AI generation.
- Don't rely on AI tools for legible on-image text — recommend adding text
  as a post-process step (Canva) instead.
