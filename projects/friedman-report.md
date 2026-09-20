# The Friedman Report — Weekly Standing Procedure

This file documents Kyle Friedman's repeatable weekly Maryland market report
workflow. When Kyle drops in this week's numbers/context, follow the staged
workflow below without re-asking for the process, only ask for genuinely
missing data.

## Staged workflow (changed 2026-09-21 per Kyle)
Don't fan out to every channel immediately. Build in this order, with a real
stop for Kyle's sign-off after step 1:
1. Build `report-core.md` (the master narrative + all data/sections), then
   render it as a **PDF review draft** and hand that to Kyle first. This is
   the checkpoint: confirm the story, numbers, and angle are right before
   anything else gets built.
2. Once Kyle approves the PDF (or gives corrections and re-approves), build
   Substack, then the website SEO article, then the remaining social
   channels (LinkedIn, Instagram, GBP, YouTube).
   Order that ran smoothly the week of 9/14-9/20 (Kyle's call: video first):
   video script, PDF blueprint (sign-off), Substack, image prompts (Kyle
   generates, then I composite/fix), website article + push, then LinkedIn,
   GBP, Instagram Reel caption. Kyle said the PDF is "the blueprint" so the
   team is on the same page before everything else gets built.
3. **Do not build a Gamma deck by default.** Gamma is slow and not worth it
   most weeks, per Kyle. Only build one if Kyle explicitly asks for it that
   week. The PDF from step 1 is now the standard flagship visual document,
   not Gamma.

## What "this week's edition" contains — every time
1. **Narrative story** — buyer- or seller-focused, told through named fictional
   characters (not real clients)
2. **Statewide + county-level MLS stats** — sourced from Bright MLS
3. **Friedman Market Momentum Index (FMMI)** — with its four component scores
4. **County heat map**
5. **Friedman Signal**
6. **Weekly comparison table** (vs. prior week/period)
7. **A recipe** (closing lifestyle element)

## Story of the Week rules (confirmed with Kyle 2026-09-20)
- Fictional composite characters, **first names only, never a last name**
  (Kyle changed "Denise and Walt Holloway" to "Denise and Walt").
- Make it inspiring: it must end with a win, for example an offer in hand
  or a repriced listing that starts getting showings. The agent in the
  story reads the data and makes the right call early, so nobody in it
  "fails" (Kyle: make it seem like I don't fail). Never let the agent look
  slow or wrong.
- The story is reused in the video setup, PDF, Substack, website, LinkedIn, and
  GBP, so settle it once in `report-core.md` and copy it.
- Never fabricate a data point to fill a chart or a sentence. Chart series
  and "since we began tracking" claims use only weeks that exist in the log or
  in prior published articles (days to contract, rate, FMMI history are in the
  prior week's website article table). Unverifiable comparisons ("more than the
  previous three weeks combined") get cut or reworded to what the data shows.

## Standing data dependency
- Freddie Mac PMMS 30-year mortgage rate — query as:
  "Freddie Mac 30-year mortgage rate [specific date]" — pull this fresh every
  edition, don't reuse a stale figure.

## FMMI methodology (confirmed with Kyle 2026-08-30)
This report predates this vault — real prior editions exist (week of
8/10-8/16/2026 and 8/17-8/23/2026, logged in `friedman-report-log.md`).
Confirmed: there is **no separate algebraic formula** — the rendered
report *is* the template. Each week, set four component scores (0-100) by
editorial judgment, reading the direction and rough magnitude of that
week's underlying drivers against last week's log entry, then average them
for the headline FMMI:
1. **Demand Score** — driven by closed-sales and pending-contract momentum
   (both up = strong positive).
2. **Seller Strength Score** — driven by median sold price trend (up =
   positive) and price-reduction count trend (up = negative).
3. **Market Speed Score** — driven by days-on-market trend (down = faster =
   positive).
4. **Rate Environment Score** — driven by the mortgage-rate trend (down =
   positive).
Label each week's FMMI with a short descriptor in the same voice as prior
editions (e.g. "Balanced Market, Tightening") rather than a fixed
numeric-band label — don't invent buyer's/balanced/seller's cutoffs that
don't appear in the real prior editions.
**Days-on-market caveat:** prior editions' "Avg. Days on Market" appears to
be a blended statewide snapshot metric; this vault's weekly Bright MLS pull
(statewide + county) gives median/avg CDOM specifically for Closed sales
instead. Use that as the Speed driver and note the basis may not be
perfectly continuous with prior editions' figure, even though both
represent typical time-to-transact.

## Friedman Signal™
A single word/short phrase (e.g. "TIGHTENING", "STABILIZING") naming the
week's market direction, followed by a paragraph explaining why — distinct
from the FMMI score. Written fresh each edition; see the real prior
editions in `friedman-report-log.md` for tone and format.

## Other real-format elements confirmed from prior editions (not previously
## documented here — add to the edition checklist above)
- **Market Spotlight** — as of 2026-09-21, default to covering the largest
  8-11 counties by population/volume with their own paragraph (not just
  2), plus a 3-week trend table (rate/price/pace) and a new-listings vs.
  closings ratio per county, if the week's data supports it. This was a
  one-off expansion Kyle asked for on 9/14 that should now be the standing
  baseline depth, not something to rebuild from scratch only when asked.
- **Market Movers / Price Extremes** — most/least expensive listing this
  week, ideally a real specific address+price+beds/baths from Kyle (ask
  him for it, don't wait for him to volunteer it). **Also ask for the
  actual listing URL at the same time** (his expPortal link), not just the
  address/price/details — added 2026-09-21 after shipping a placeholder
  URL that had to be swapped out later. Only fall back to statewide
  aggregate min/max new-listing prices, with an explicit caveat, when no
  specific listing sheet is available.
- **Winners & Losers** — a short bulleted "winners this week" /
  "losing momentum" pair.
- **"One Thing I'd Do This Week"** — three short takes: If I Were Buying /
  Selling / Investing.
- **Deep Dive fact** — one surprising, sourced number (e.g. total sales
  volume, months-of-supply from a named third-party source with a
  methodology caveat, listings withdrawn/canceled).
- Ends with "Your Next Move Starts Here" (valuation + search-homes CTAs),
  then "Let's Talk" with Kyle's full signature block including "Why Choose
  Kyle" bullets. Brokerage is "The Friedman Team at eXp Realty"; office line
  888-860-7369 in addition to the cell 443-789-3101.

## Inputs needed from Kyle each week
- Before asking Kyle for anything, read `friedman-report-log.md` for the most
  recent entry — that's last week's data, needed for the comparison table.
- Then ask Kyle for: this week's Bright MLS stats (statewide + relevant
  counties). Do NOT ask him to re-supply last week's numbers — pull those
  from the log.
- Also ask: any specific story angle, county focus, or seasonal hook for the
  week, and anything unusual to flag (rate moves, local news, inventory
  shifts).
- Freddie Mac rate is NOT asked of Kyle — pull it yourself (see below).
- Once Kyle provides this week's numbers, append a new dated entry to
  `friedman-report-log.md` (format specified in that file) — don't overwrite
  prior entries.

## Real Substack format (confirmed from the 8/17-8/23 published post, 2026-08-31)
This is a DIFFERENT, shorter structure than the Gamma deck or website —
don't just paste the Gamma content into Substack, and don't embed images
via markdown `![]()` syntax pointing at raw CDN URLs (renders as broken
link clutter, not an image, when pasted into Substack's editor — Kyle
flagged this). If images are wanted, hand Kyle the image URLs/files
separately so he drops them into Substack's editor directly, or note
where they'd go without embedding a raw link inline.

Structure, top to bottom:
1. **Title** in the pattern `[Punchy hook] | Maryland Weekly Market
   Report, Week of [date range]` (changed 2026-09-14 per Kyle: title
   must contain "Maryland Weekly Market Report" and the date range, not
   just "The Friedman Report" branding).
2. **Subtitle**: one line, teases the story's turn.
3. Opens directly with the narrative (2-3 short paragraphs), no header
   before it.
4. Early callout, own line: `👉 [View the full interactive market report
   here](<gamma link>) — county by county data, the Friedman Signal, and
   this week's heat map.` Only include this line if a Gamma deck actually
   exists that week (it's no longer the default, see Staged workflow
   above); otherwise drop the line or point it at the PDF/website article
   instead.
5. A second link, own line: `[See This Week's Full Breakdown &
   More](<website article URL>)`.
6. Continue the narrative with the week's headline numbers woven in.
7. `## This Week's Price Extremes` — the real high/low listing (or
   aggregate fallback).
8. `## The Numbers, Fast` — bulleted, one emoji per line: 🏡 Homes Sold ·
   🆕 New Listings · ✍️ Pending Contracts · 💰 Median Sold Price · ⏱️
   Days on Market · 🏷️ Price Reductions · 📈 Mortgage Rate.
9. Fastest/slowest county as plain sentences (not a table).
10. FMMI as a short paragraph, not a full breakdown table (that level of
    detail lives in Gamma/website).
11. `## Deep Dive: <title>` — the one surprising number.
12. `## One Thing I'd Do This Week` — **Buying?** / **Selling?** /
    **Investing?** as inline bold questions, not H3 headers.
13. A personal engagement line inviting replies (e.g. "Just reply to this
    email, I read every one").
14. Sign-off: `Have Questions? Let's Talk.` + phone + **kyle@friedmanreteam.com**
    (canonical email — do not use any retired PenFed/CornerHouse domain)
    + Maple Lawn address.
15. Three separate link buttons, own lines: `Schedule a call` (Calendly),
    `Search Homes`, `Check Your Home's Value`. No "Why Choose Kyle"
    bullets on Substack — that block is Gamma/closing-slide only.
Everything after that (like count, "Discussion about this post", related
posts, the publication's own subscribe footer) is Substack's own
auto-generated UI — never hand-write it into the draft.

## Short-form video (added 2026-09-21)
A separate deliverable from the "Suggested talking points" in the YouTube
draft, that's for a longer talking-head video if Kyle wants one. The
**default weekly video is a 15-20 second short** (Reels/Shorts/TikTok),
NOT a 2-3 minute script, that was a real miss the first time this was
asked for. Structure, modeled on Kyle's own real examples:
1. A one-line setup naming the surprising thing that happened this week.
2. One or two concrete data points delivering the contrast (a county-vs-
   county gap, or a "you'd expect X, but Y happened" beat).
3. A short punchy "lesson" or reframe line.
4. A closing line that ties the lesson back to the viewer's own numbers or
   decision, varied week to week, don't reuse the same closing line
   multiple weeks running (Kyle flagged this after 5 similar closers in a
   row).
Total length: roughly 50-65 words, reads in 15-20 seconds. Write it as
plain spoken lines, no headers, easy to read straight off a phone while
recording. See `video-script.md` in a given week's drafts folder for the
exact format once one exists.

**Caption for the video post** is a separate, shorter piece of copy, not
the script repeated. It should tease the payoff and create a curiosity
gap rather than give away the "reveal," since a caption that summarizes
the whole video kills the reason to tap play. Match Kyle's own younger,
casual voice for Instagram/Reels captions specifically (see
`../notes/brand-guidelines.md` if that gets documented there), 5 hashtags
max, not a long tag block.

## Distribution — every edition goes to all of these (updated 2026-09-20)
- PDF review draft (see Staged workflow above, built first every week)
- Substack (real Substack format above)
- Website SEO article (must satisfy the homepage FMMI requirements below)
- LinkedIn (put the article link in the first comment, not the body)
- Short-form video script + Instagram Reel caption (see Short-form video
  section). The Instagram caption replaces the old YouTube description; Kyle
  said YouTube is not what he needs. Only write `youtube.md` if he asks.
- Google Business Profile: a **miniature of the Substack**, plain text, about
  1,400 to 1,480 characters (Kyle: "about 1500, no more, maybe a tad less").
  Order: standalone hook line, 3 to 4 sentence story ending with the win,
  THE NUMBERS, FAST (same emojis), fastest/slowest/tightest counties,
  Price Extremes line, FMMI line with the four scores, DEEP DIVE, ONE THING
  I'D DO (Buying/Selling/Investing one-liners), contact line + email +
  tagline. CTA button "Learn more" to the article. No separate short version.
- **No Instagram carousel for the weekly Friedman Report** (Kyle 2026-09-20).
  Carousels stay for standalone deep-dive pieces only.
- Gamma: **on request only**, not a default (changed 2026-09-21)

## Standing build rules
- Branding & tone: follow `../notes/brand-guidelines.md` — don't duplicate
  those rules here, check there.
- Deep-dive topic pieces (e.g. Zestimate accuracy, 1031 exchanges, closing
  costs) get the same Instagram carousel + Substack distribution as standard
  editions when produced as standalone content.
- **No em/en-dash punctuation anywhere** — every channel, not just the
  website article. See `../notes/brand-guidelines.md` "Writing style".
- **Before generating any branded image**, check how it will actually be
  displayed in the destination (the site's component code, the platform's
  aspect-ratio/crop rules) rather than assuming a format. Building the
  9/7-13 hero at a 3:1 banner without first checking that the site
  displays every hero in a fixed 16:9 `object-cover` box cost several
  redundant image generations. When in doubt, grep the consuming
  component before spending generation budget.
- **Website hero must be 16:9** (the site crops every hero to 16:9). This was
  already documented above and was missed again on 9/14-9/20: the hero
  went live as a 3:1 banner and got its text cut off at both ends, then had to
  be rebuilt. Check the aspect ratio of Kyle's image before it goes in the
  repo, and open the live blog card and article after deploy. Recipe in
  `report-images.md` ("Website hero must be 16:9").
- **Image prompts:** Kyle generates the images and drops them in chat. Check
  each one against the source numbers (heat map, supply, FMMI graphics had to
  be read digit by digit) and fix defects (e.g. a kicker fading into a cloud).
  Save finished files into the report folder's `images/` with the slug
  filenames, then copy the web ones into the website repo's
  `public/images/uploads/`.
- **Deliver files to Kyle with SendUserFile**; don't just cite paths.
- **Publishing the website article means commit + push to main in the website
  repo** (Kyle approves that step each week). The Substack links to it, so it
  goes live first.
- Reusable build kit lives in `scripts/report/` (see its README).
- **Before calling any edition "done," do a pre-publish pass**: grep the
  whole file (not just the section you touched) for every occurrence of
  anything you just fixed (an address, a link, a stat), and confirm every
  referenced image/asset path actually has a file behind it. A fix applied
  to one occurrence and missed on a duplicate elsewhere, and a broken
  `<img>` reference to a file that was never created, both shipped to the
  live site the week of 9/7-13 because this wasn't checked before calling
  it finished.

## Output format
Follow the Staged workflow above: PDF review draft first and wait for
Kyle's sign-off, then assemble the rest of the platform-specific versions
(Substack post, SEO article draft, LinkedIn post, GBP mini-Substack post,
Instagram Reel caption) ready to publish or lightly edit. Build a
Gamma deck only if Kyle asks for one that week.

## Homepage FMMI gauge depends on the website article (learned 2026-09-20)
The homepage gauge is rebuilt from each week's website article at deploy time (`scripts/generate-fmmi-data.mjs`). Every article MUST contain, inside the `## The Friedman Market Momentum Index` section: (1) the gauge image alt text "...Momentum Index at NN out of 100", (2) a `<p>` with the label (e.g. "Balanced Market, Cooling"), (3) a sub-score chart image whose alt is "...FMMI sub-scores: Demand NN%, Seller Strength NN%, Market Speed NN%, Rate Environment NN%" (the `%` signs are required), plus a `## The Friedman Signal: X` heading. Missing the label or sub-score alt blanks the bars and the "What's driving the score" panel on the homepage. `website-seo.md` generation template handles all of these.
