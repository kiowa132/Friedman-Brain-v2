# Listing Presentation Package — Standing Procedure

This file documents Kyle Friedman's repeatable seller listing presentation workflow.
When Kyle provides the inputs below for a new listing, produce the full package
without re-asking for the process — only ask for genuinely missing inputs.

## What to build, every time
A complete seller presentation package = **3 deliverables**:
1. **One combined Gamma presentation** (changed 2026-09-14, was two separate
   decks, comps and strategy, Kyle corrected this: "why are you doing 2
   seprate gammas when it should just be 1 with all the info combined" —
   he presents one deck in the meeting, not two he has to juggle). Structure,
   in this order:
   - Cover
   - Subject property facts (don't repeat these later in a separate "Your
     Home" section, say it once)
   - Comps: cover all categories present in the data (active, pending,
     under contract, sold) as individual interactive cards, then a
     takeaways card
   - **Market-evidence pricing section** (added after the Wendy Fossen /
     8302 Woodmont run, Sept 2026): grouped **active / pending / closed
     (last ~6 mo) / withdrawn+expired+canceled (last ~12 mo)**, from a
     Bright MLS one-line pull or an RPR CMA export, plus the subject's own
     listing history and DOM/CDOM if it has one. Read failed listings for
     the price ceiling, read the price-cut history for what NOT to repeat.
     Land on one recommended list price with "one price, no cut-ladder"
     framing. This is what makes the number defensible instead of an
     opinion. Works especially for expired/withdrawn re-lists, frame those
     as a **relaunch** (go dark, new photos, coming-soon, new MLS #), not a
     price change on the dead listing.
   - Marketing strategy, launch plan, digital campaign
   - **Your Listing Roadmap** (added 2026-09-15, was being skipped
     entirely, `marketing/listing-process-roadmap.md` says it's "reusable
     for every listing presentation" and that file was never linked from
     here, real miss caught during a brain audit). This replaces any
     generic "path to success" process-overview card, it's the specific,
     branded 10-step roadmap: Plan (WE ARE HERE) → Prepare + Present →
     Coming Soon (Thursday) → Go Active (the next Thursday) → Open House +
     Brokers Open → Feedback + Adjust → Negotiate → Under Contract → Clear
     to Close → Settlement. Condense to one card, a compact numbered list,
     don't spell out all the sub-bullets from the source file, that's for
     Kyle's live talk track, not the slide. Always mark step 1 as "we are
     here" since that's the day of the listing appointment.
   - Why clients choose The Friedman Team, testimonials, team roles,
     stats, guarantees, agent bio
   - Next steps close
   One `generate` call, `cardSplit: inputTextBreaks` so the whole thing
   holds together as a single deck Kyle can present start to finish.
   **Target 10-20 cards total** (corrected same day after a 37-card first
   pass took so long to render it stalled, and Kyle called it "way to
   long"). Condense, don't enumerate: comps go on 1-2 summary cards (all
   closed comps listed together, all current active/pending/AUC comps
   together), not one card per property. One strong testimonial, not
   three. Team roles and guarantees each get one condensed card, not a
   card per role or per guarantee.
2. **Net proceeds** — two forms:
   - **Branded client PDF** (the deliverable Kyle attaches to the seller email):
     one page, FRIEDMAN wordmark + teal/gold, scenario columns, tax note,
     assumptions, contact footer. Generator: `../scripts/pdf/net-proceeds-pdf.py`
     (copy + edit the model block per listing). Requires the real Python.
   - **Formula-driven Excel workbook** as the working model for changing
     assumptions (openpyxl, scenario columns, editable yellow cells).
3. **Pre-appointment confirmation email** to the seller (template below)

## FUB calendar/appointment description — standing template (changed 2026-09-21)
The seller receives this directly (Follow Up Boss emails the calendar invite to
them), so it must be written **to** the seller, second person, personable, not
a third-person internal note describing them. Fixed after the first version
for Samuel Watson read like an agent's own case note ("Meet with Samuel
Watson to present...") even though Samuel was the one reading it.

> Looking forward to sitting down with you to go over a detailed listing
> strategy for your home, including a review of recent comparable sales,
> recommended pricing, positioning, marketing strategy, and the plan to
> generate the strongest possible offer.
>
> We'll also walk through your estimated net proceeds after commissions,
> closing costs, fees, and other anticipated expenses, so you have a clear
> picture of what you can expect to walk away with.
>
> If the strategy, the numbers, and the overall plan make sense, and we're
> a good fit to work together, we'll move forward with completing the
> listing paperwork and getting your property officially prepared for
> market.

The description body is fully generic, fill in nothing there. But the
title/time/location/attendee fields around it must be spelled out
explicitly every time, labeled (Title / Date / Time / Location / Attendee),
not left as a parenthetical note telling Kyle to fill them in himself.
Corrected 2026-09-14 after handing Kyle a FUB deliverable with only the
description text: "thanks for fub calalnder invite but there is no title
no time no location its not formatted correctly at all." See
`listings/1000-beall-dr/confirmation-email.md` for the corrected format.

## Pre-appointment confirmation email — standing template (final, 2026-09-14)
Sent once the deliverables above are ready, to confirm the appointment and
give the seller everything to review beforehand. This went through two
rewrites in one day, first from a short bullet list to a long numbered
market-narrative version (Kyle: "way better thanks"), then Kyle pasted the
actual Samuel Watson / 3070 Monroe St email he'd sent as the real target:
"email should look more like this i think moving forward." **Use that one.**
The long numbered-narrative version (market stats, comp-by-comp breakdown,
net proceeds dollar figures spelled out in the email body) is retired, the
market data lives in the attached Gamma deck and net proceeds PDF, not in
the email itself. Model: `listings/1000-beall-dr/confirmation-email.md`
(rewritten to match) and the Samuel Watson email below.

Structure, in order:
1. Subject: "Your Listing Strategy Consultation, [Day] [Date] at [Time]"
2. "Looking forward to our listing strategy consultation this [Day],
   [Date] at [Time] for [address]."
3. "Please take some time to review everything I've attached beforehand.
   This is important, it means we can spend our time together talking
   through your questions instead of me walking you through numbers for
   the first time in person." (verbatim, this line explains *why* he wants
   it reviewed ahead of time)
4. "Here's what I've put together for you:" then a short bullet list (not
   numbered sections): the interactive pricing/marketing plan, the
   Interactive Comps Presentation ("the real comparable [town] sales I
   priced this off of"), Estimated Net Proceeds ("what you can expect to
   walk away with, across three price scenarios"). No dollar figures, no
   market stats here, that's what the attachments are for.
5. The Gamma link on its own line right after the bullets.
6. "A couple of things I want to make sure you know about, both are
   already built into what I'm offering you:" then two call-outs:
   - **Complimentary cleaning service**, included at no cost, one less
     thing to coordinate before photos.
   - **Zillow Showcase**, framed as normally reserved for listings above
     $500,000 but extended to this seller at no additional cost (use this
     framing whenever the list price is under $500K, see the standing
     offering note above). Include the full stat pitch verbatim: 79% more
     page views, 76% more saves, 91% more shares, sells for about 2% more
     (roughly $7,000 on a home in this price range), same tool used on
     luxury listings.
7. "Take a look through everything, and let me know if you have any
   questions before [day]."
8. **Close with this exact line** (Kyle's own wording): "If after we sit
   down you feel I'm the right fit for the job, we'll fill out the listing
   paperwork right then, get your home in front of our exclusive
   off-market buyers list immediately, and start scheduling your
   complimentary cleaning service the same week." Not "if we're a good
   fit" or "if the numbers make sense."
9. Sign-off: Kyle Friedman / The Friedman Team, brokered by eXp Realty /
   (443) 789-3101 / kyle@friedmanreteam.com

No numbered market-story sections, no "please have ready" checklist, no
"what we'll do at the meeting" paragraph, those belonged to the retired
long version. Keep it to the structure above.

**Companion text-message version** (separate, sent alongside): confirm the
appointment, mention the email/attachments were sent, ask him to bring
whatever's needed to lock exact numbers, short version of the same
assumptive close. No stats or dollar figures in the text either (Kyle
corrected this explicitly: "shouldnt include numbers just assume sale and
tell him[to check the] email adn confirm appt").

The FUB calendar invite description stays separate and short, it is not
this email, don't merge them. Always spell out the FUB invite's title/
date/time/location/attendee as explicit labeled fields with real values,
never a parenthetical "fill this in" note (corrected 2026-09-14).

## Inputs needed from Kyle for each new listing
- Property address, county, and basic details (beds/baths/sqft/lot, list price target)
- Seller name(s) and contact context
- Any comps already pulled, or note to source via RPR/NarrPR
- **Bright MLS one-line export** for the subject's competitive set (active /
  pending / closed 6mo / withdrawn+expired+canceled 12mo) + Statistical Summary
  if the tool gives it — feeds the market-evidence pricing section
- Target list price and any known seller motivations/timeline
- Estimated payoff/liens if known (for net proceeds accuracy)
- Condo/HOA fee + what it covers (drives buyer affordability; put it in the analysis)
- If it's an expired/withdrawn re-list: the prior listing's full price-cut
  history and DOM, and whether Kyle knows of any building issue (reserves,
  special assessment, rental cap, FHA/VA) behind slow sales
- Comp data can also arrive as an **RPR CMA PDF export** (not just a Bright
  MLS one-line) — extract with pypdf (these are text-based, unlike scanned
  listing agreements). It already groups active/pending/closed, so it can
  feed the market-evidence section directly without a separate Bright MLS pull.
- County transfer/recordation tax rates vary a lot by county and aren't
  worth guessing, confirm via web search each time (Harford County: 1.0%
  county transfer + 0.5% MD state transfer + $6.60/$1,000 recordation,
  customarily split 50/50, seller share ≈1.08% combined — first run,
  1000 Beall Dr, Sept 2026).
- If Kyle attaches his own reused "Listing Strategy" template PDF (generic
  marketing/process/testimonial deck, not listing-specific), treat it as
  the base content for the strategy Gamma, not a finished deliverable. It's
  often stale: check for the wrong team name ("Friedman Real Estate Team"
  instead of "The Friedman Team"), leftover pages from a prior client's
  address, and any stat that conflicts with Kyle's actual current bio
  elsewhere in the same doc, fix quietly rather than perpetuate.
- If exact mortgage/HELOC payoff isn't known, public record sales/financing
  history (in the RPR CMA's "Sales and Financing Activity" section) gives
  origination amounts and dates, useful as a labeled placeholder, but flag
  to Kyle that it's not a current balance and should be confirmed with the
  seller before finalizing net proceeds.

## When there's no appointment booked (prospecting package)
Cold or warm-lead package to earn the meeting. Same deliverables, but:
- Cover email pitches a 30-min meeting instead of confirming one; references how
  Kyle connected (e.g. cold call off the expired list)
- Lead with the market-evidence pricing section + net proceeds; the "why me"
  marketing content comes after
- First run: Wendy Fossen / 8302 Woodmont Ave #203, Bethesda (Sept 2026) —
  `listings/8302-woodmont-ave-203/`. Reusable PDF generators:
  `scripts/pdf/listing-presentation-8302-woodmont.py` and
  `scripts/pdf/net-proceeds-8302-woodmont.py` (copy + edit per listing).

## Standing offerings (added 2026-09-21, weave into strategy content where relevant)
- **Free cleaning service** is included in every listing package, standard,
  not an upsell. Mention it as part of the prep/marketing story (fits
  naturally in the Home Prep Advisor section).
- **Zillow Showcase** is standard/included on every listing **$500K and
  up**. Below $500K, it's not automatic, Kyle offers it selectively as a
  closing incentive/promotional point when it helps close the deal, frame
  it as something being extended to this specific seller, not a standard
  perk everyone gets. When pitching it (especially as the special offer on
  a sub-$500K listing), the real stats to use:
  - Showcase listings average **79% more page views, 76% more saves, and
    91% more shares** than comparable non-Showcase listings.
  - Homes sell for roughly **2% more** (about $7,000 on an average-priced
    home).
  - Includes: professional 3D Home tour on every listing, interactive
    floor plans, priority placement in Zillow search/map results,
    dedicated email alerts to serious buyers, and (on select listings)
    SkyTour, a drone-like exterior/neighborhood flythrough.
  - Sources: [Zillow Showcase](https://www.zillow.com/agents/showcase/),
    [Zillow Media Room](https://zillow.mediaroom.com/2024-04-16-Showcase-listings-on-Zillow-are-more-than-just-cutting-edge-featured-homes-sell-faster-and-for-more-money),
    [Amplifiles ROI breakdown](https://www.amplifiles.ai/blog/zillow-showcase).

## Standing build rules — do not deviate without asking
- **Comp data**: source via RPR/NarrPR unless Kyle supplies comps directly.
- **Gamma deck**: use theme **"friedman v2 test"** (`themeId: dlup7kt5fa4f3r0`,
  a custom theme in Kyle's Gamma workspace), `textMode: preserve`,
  `cardSplit: inputTextBreaks`. Changed 2026-09-15, Kyle confirmed this
  explicitly ("also use this theme friedman v2 test") after it showed up
  by accident on the 261 Magothy deck (a workspace-default override) and
  he liked it better than `aurum`. `aurum` is retired for new decks. See
  `../notes/brand-guidelines.md` and `../decisions.md` for the older
  Aurum-vs-teal/gold history, now superseded by this pick.
- **Excel workbook**: build with openpyxl, formula-driven (not hardcoded values),
  include scenario modeling (multiple price/timeline scenarios where relevant).
- **Branding & tone**: follow `../notes/brand-guidelines.md` for naming,
  voice, and positioning — don't duplicate those rules here, check there.

## Known variants to watch for
- Investment property angle: if the property could be evaluated as a rental
  (sell vs. STR vs. long-term rental), check local jurisdiction rules first —
  e.g., PG County requires primary-residence occupancy for non-owner-occupied
  STRs, which rules STR out there.

## Output format
Deliver all three pieces in one pass unless Kyle says otherwise: Gamma deck
link/file, Excel workbook file, and drafted confirmation email text ready to
send.
