# The Friedman Report — Weekly Standing Procedure

This file documents Kyle Friedman's repeatable weekly Maryland market report
workflow. When Kyle drops in this week's numbers/context, produce the full
edition and its full distribution set without re-asking for the process —
only ask for genuinely missing data.

## What "this week's edition" contains — every time
1. **Narrative story** — buyer- or seller-focused, told through named fictional
   characters (not real clients)
2. **Statewide + county-level MLS stats** — sourced from Bright MLS
3. **Friedman Market Momentum Index (FMMI)** — with its four component scores
4. **County heat map**
5. **Friedman Signal**
6. **Weekly comparison table** (vs. prior week/period)
7. **A recipe** (closing lifestyle element)

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
- **Market Spotlight** — two counties profiled with active/closed/avg-DOM
  stats and a short editorial note.
- **Market Movers** — most/least expensive listing this week. If individual
  listing sheets aren't available (as with the 8/17-8/23 edition), fall
  back to statewide aggregate min/max new-listing prices and the priciest
  closing, with an explicit caveat — don't invent a specific address.
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

## Distribution — every edition goes to all of these
- Gamma (custom theme ID `m6zymtbkauah9qd`)
- Substack
- Website SEO article
- LinkedIn
- Instagram (carousel format — standard for every edition)
- Google Business Profile
- YouTube

## Standing build rules
- Branding & tone: follow `../notes/brand-guidelines.md` — don't duplicate
  those rules here, check there.
- Deep-dive topic pieces (e.g. Zestimate accuracy, 1031 exchanges, closing
  costs) get the same Instagram carousel + Substack distribution as standard
  editions when produced as standalone content.

## Output format
Deliver the full edition as a complete package: narrative + all data
components assembled, plus platform-specific versions (Gamma deck, Substack
post, SEO article draft, LinkedIn post, Instagram carousel copy, GBP post,
YouTube description) ready to publish or lightly edit.
