# Listing Presentation Package — Standing Procedure

This file documents Kyle Friedman's repeatable seller listing presentation workflow.
When Kyle provides the inputs below for a new listing, produce the full package
without re-asking for the process — only ask for genuinely missing inputs.

## What to build, every time
A complete seller presentation package = **4 deliverables**:
1. **Interactive comps Gamma presentation** — built from the RPR comp data
   Kyle provides. Cover all comp categories present in the data (active,
   pending, sold) as an interactive deck, not a static PDF-style export.
2. **Listing strategy Gamma presentation** — the seller-facing listing
   strategy/pitch deck.
3. **Net proceeds** — two forms:
   - **Branded client PDF** (the deliverable Kyle attaches to the seller email):
     one page, FRIEDMAN wordmark + teal/gold, scenario columns, tax note,
     assumptions, contact footer. Generator: `../scripts/pdf/net-proceeds-pdf.py`
     (copy + edit the model block per listing). Requires the real Python.
   - **Formula-driven Excel workbook** as the working model for changing
     assumptions (openpyxl, scenario columns, editable yellow cells).
4. **Pre-appointment confirmation email** to the seller (template below)

## Pre-appointment confirmation email — standing template
Sent once all 4 deliverables above (minus listing paperwork, drafted
separately) are ready, to confirm the listing strategy consultation and give
the seller everything to review beforehand.

> Subject: Your Listing Strategy Consultation — [Day], [Date] at [Time]
>
> Hi [Seller Name],
>
> Looking forward to our listing strategy consultation on [Day] at [Time] to
> go over everything for [Property Address].
>
> Ahead of our meeting, I've put together the following for you to review:
> - Listing Strategy
> - Interactive Comps Presentation
> - Listing Paperwork
> - Net Proceeds Estimate
>
> Take a look through these when you get a chance — happy to answer any
> questions before we sit down.
>
> After we meet, if you feel we're a good fit to work together, we'll go over
> the listing paperwork and get started on marketing your property to find
> the right buyer.
>
> Talk soon,
> Kyle Friedman
> The Friedman Team

Fill in seller name, appointment day/date/time, and property address per
listing. Keep the "if good fit → paperwork → marketing" framing — it's the
standing next-steps logic, not appointment-specific.

## Inputs needed from Kyle for each new listing
- Property address, county, and basic details (beds/baths/sqft/lot, list price target)
- Seller name(s) and contact context
- Any comps already pulled, or note to source via RPR/NarrPR
- Target list price and any known seller motivations/timeline
- Estimated payoff/liens if known (for net proceeds accuracy)

## Standing build rules — do not deviate without asking
- **Comp data**: source via RPR/NarrPR unless Kyle supplies comps directly.
- **Gamma deck**: use theme `aurum` (`themeId: aurum`), `textMode: preserve`,
  `cardSplit: inputTextBreaks`. See `../notes/brand-guidelines.md` and
  `../decisions.md` — the Aurum-vs-teal/gold question is an open decision;
  don't switch themes without confirming with Kyle.
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
