# Buyer Feasibility Analysis — Standing Procedure

For a buyer client (usually a couple) weighing whether a purchase in a target
area actually works **before** they sink time into house-hunting. Output is a
decision tool: the monthly math at real price points, tested against what has
actually sold and what's on the market.

First run: Syed Imam, move-up from 8303 Bellona to Sparks vs. Ellicott City
(Aug 2026). Files: `clients/syed-imam-move-up-feasibility.md`,
`clients/syed-imam-feasibility-email.md`, Gamma `79gwm5p1a9z7urt`. That one took
~5 rebuilds; the "don't repeat" box below is why.

## Lock the scope in one line (say this to the client, put it in the report)
> A decision tool, not a loan pre-qualification. It assumes you're approved for
> the purchase. It lays out the monthly cost at a few price points against real
> inventory, so you can decide if it pencils.

Do **not** chase DTI, income, or a pre-qual. That's the lender's job.

## Pick the flavor (most are A or C, often + E)
- **A — Move-up with a home to sell:** equity → down payment; how much does the
  payment jump; does it still work.
- **B — Move-up that needs rental income:** A + the ADU / basement-suite / house-
  hack sections (rent, legal cost).
- **C — Straight affordability ("can we afford [area]?"):** down payment from
  savings; payment at 3 price points vs. their comfortable number; inventory reality.
- **D — Buy now vs. wait / rent-then-buy:** timing and rate/price sensitivity.
- **E — Two-area or two-price-band side-by-side:** when they're torn. Runs as a
  second column on every table.

## Inputs to collect BEFORE building (ideally on the consult call)
- Buyer name(s); married / filing status.
- **Current housing:** own (value, payoff, monthly P&I *and* whether it's PITI or
  P&I-only, is it being sold) or rent (current rent = the "vs. today" number).
- **Cash for the purchase:** from sale equity and/or savings; how much they want
  to keep back.
- **Target area(s):** 1–3 specific towns/zips. Are we comparing (flavor E)?
- **Price ceiling** + a **"comfortable monthly payment"** number.
- Must-haves: beds/baths/sqft, min school rating (if any), lot, commute, timeline;
  deal-breakers; would they take a fixer.
- **Rental income part of the plan?** If yes: basement suite / detached ADU /
  house-hack — and **does the unit already exist or need building?** (Default:
  exists, just needs legalizing. A full build estimate is a separate, bigger job.)

> Rebuilding because the area or price ceiling changed after the first draft was
> the #1 time sink last time. Nail these two before writing anything.

## Standing assumptions (use the same ones every run)
- **Rate:** current Freddie Mac 30-yr weekly PMMS. Cite the week.
- **Down payment:** 20%+ (no PMI) unless the client says otherwise. Note the
  effect of less down: **≈ +$320/mo per $50K not put down** at ~6.7%.
- **Property tax (% of price, reassessed near the sale price):** Baltimore County
  ~1.15% · Howard County ~1.35% · Carroll County ~1.0% · Frederick County ~1.1%.
- **Insurance:** ~$150–200/mo (higher on acreage / older / well+septic).
- **Seller sale costs (if selling):** ~6% commission + ~1% transfer/misc ≈ 7%.
- **Section 121:** first $250K gain (single) / $500K (MFJ) excluded, federal + MD,
  if it was their primary home 2 of the last 5 years. Preserved if sold within
  ~3 years of moving out.
- **Rental income from a unit that doesn't exist yet does NOT help them qualify.**
  Only an existing, leased unit with history counts, partially. Lender confirms.

## Report structure (Gamma `format: document`)
0. **Scope box** — 3 lines: what this is, what it assumes, rate + date.
1. **Where you start** — one clean number: "$X toward the purchase." If selling:
   value − payoff − ~7% costs = net, plus the Section 121 "it's tax-free" line.
2. **The new monthly payment** — table. 3 price points (comfortable / stretch /
   ceiling). One column per area (flavor E). Rows: price, loan, P&I, taxes,
   insurance, **PITI**, **vs. today / vs. comfort number**. Assumptions footnote.
3. **The number that matters** — the gap, isolated and bold: *"At $X you're paying
   about $Y/month more than today."* This is the headline output.
4. *(B only)* **What a rental unit brings in** — net rent by unit type, area-
   specific (net = gross − ~20–25% for vacancy, upkeep, license, higher insurance).
5. *(B only)* **Cost to legally rent** — DEFAULT: the space exists, so it's just
   fees to place a tenant: **basement in-law suite ≈ $300–1,500 one-time**;
   **detached structure w/ utilities ≈ $1,000–8,000**. (Rental license, any
   accessory-apartment registration, lead reg. for pre-1978, septic capacity
   review $250–750.) Full build breakdown only if they confirm it needs building →
   `scripts/pdf/adu-cost-breakdown-pdf.py`.
6. **Does it pencil?** — one-line verdict per scenario: **pencils / close / over**,
   with the net monthly after any rental income.
7. **Schools** *(only if they set a bar)* — table: zone → ES / MS / HS ratings →
   meets the bar? Call out where it fails (usually the middle school). GreatSchools
   ratings; confirm each specific address on the district's school locator.
8. **What's actually out there** — Redfin, target area(s), last ~6 months sold +
   current active, in their band. Group: **fits the brief · active in range · sold
   above budget (calibration)**. Note inventory depth and how fast the right one goes.
9. **Bottom line** — 3–5 bullets: the price range that works, the trade-offs, the
   recommended path, the next step.
+ Standing disclaimer (planning only; not tax/legal/lending advice; rates and
  rules change; confirm ADU rules with the county).

## Deliverables (one pass)
- Working analysis `clients/<name>-feasibility.md` (internal; dashes fine here).
- Client **Gamma document** — `format: document`, `textMode: preserve`,
  `themeId: m6zymtbkauah9qd` (Friedman brand), `imageOptions: {"source":"noImages"}`,
  `cardSplit: inputTextBreaks`. **Bake the full content in one shot** — Gamma
  credits are limited and every regen costs ~30–40.
  - If Gamma credits are out: (1) branded 2-page PDF via
    `scripts/pdf/feasibility-pdf.py` (copy + edit the DATA block), and (2) save
    the full paste-ready Gamma source to `clients/<name>-feasibility-gamma.md`
    (with the settings header) so it generates in one paste when credits refill.
    First use: Jose Salas — `clients/Jose-Salas-Feasibility.pdf`,
    `clients/jose-salas-feasibility-gamma.md`.
  - When the client gave Kyle a Bright MLS one-line export, build Section 2 (and
    the "what's out there" read) straight off that, not off web comps. Group
    sold / active / pending, and read the withdrawn+canceled rows for the price
    ceiling signal (a home that failed at $X and sold at $X-minus tells you where
    the ceiling is).
- **Summary email** (plain text, **no em/en dashes**) + a short **text**, in
  `clients/<name>-feasibility-email.md`.
- `people/<name>.md` card with the links.

## Don't repeat (from the Syed run)
1. Assume approved. No DTI/income math.
2. Confirm target area(s) + price ceiling before building. Rebuilding for a new
   area is the biggest time sink.
3. Ask if a rental unit is in the plan AND whether it exists. Default = legalize
   an existing space, not a construction estimate.
4. Client-facing copy: no em/en dashes (Kyle's rule).
5. Bake the Gamma fully on the first generate — credits run out mid-revision.
6. Lead with the gap number; it's what the client actually wants to know.
7. If the listing price for their current home hasn't been set with Kyle yet,
   give the sale proceeds as a WIDE range in client copy (e.g. "$200K to $325K"),
   never a single figure. Keep the point-estimate brackets in the working .md
   only. Model the payment table at two down-payment amounts that span the range.
8. Sale proceeds not used for the down payment can be applied to the new loan as
   a principal curtailment, then the loan recast (one-time re-amortization,
   ~$250, same rate/term) to drop the payment. Explain this wherever "buy before
   you sell" comes up. Bridge loan / HELOC covers the overlap.
