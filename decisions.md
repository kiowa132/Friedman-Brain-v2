# Decisions Log

## Open
- [ ] Should listing-presentation Gamma decks (now "friedman v2 test" theme,
      switched from Aurum 2026-09-15) move to the new teal/gold brand
      identity used on the website? — raised 2026-08-26, still open
- [ ] IDX data approach for the website — not yet decided. Lofty API returns
      only 1 photo and no description per listing; IDX Broker identified as
      the likely upgrade path.

## Resolved
- Gamma deck review + AI providers (2026-09-18): the Presentation page now
  has a Step 4 that builds the whole Gamma deck as reviewable cards (numbers
  from the same data as the net sheet, static copy from the approved Beall
  deck), lets Kyle edit any card or ask AI to reword one (AI can't change a
  number; the client discards an edit that introduces one), then "Copy for
  Gamma" / "Copy for chat". Still NO Gamma API (paid plan), so it ends in a
  paste. Code: `friedman-crm/src/lib/gammaDeck.ts`. Same day the `ai` edge
  function gained OpenAI as a provider and an automatic fallback chain
  (Claude, OpenAI, Gemini, or `AI_PROVIDER` first) because Gemini's free tier
  kept returning "high demand"; OpenAI needs an API key with billing, a
  ChatGPT Plus plan doesn't include it. See `friedman-crm/SETUP-AI.md`.
- CRM auto-generating Gamma decks (2026-09-16): confirmed with Kyle he's
  not upgrading Gamma to a Pro/Ultra/Team/Business plan right now, which
  is required for API access no matter how it's called (direct API,
  Zapier/Make/n8n — the gate is on Gamma's side, unrelated to which AI
  or automation tool is calling it, and separately unrelated to paying
  for Claude/ChatGPT credits, which don't touch Gamma at all). So the
  CRM does NOT auto-generate decks — it organizes the data (comps,
  market stats, property facts) and Kyle hands a "deck brief" to Claude
  in chat to generate the deck manually, same as this session's own
  workflow. Revisit if Kyle upgrades Gamma later — see crm-app.md item
  10 for what the smaller follow-up build would look like.
- Friedman Report FMMI methodology confirmed with Kyle 2026-08-30: no
  separate formula exists — four component scores (Demand, Seller
  Strength, Market Speed, Rate Environment) are set by editorial judgment
  each week from that week's data vs. the log, then averaged. Documented
  in `projects/friedman-report.md`, alongside the full real section
  checklist (Market Spotlight, Market Movers, Winners & Losers, One Thing
  I'd Do, Deep Dive, etc.) recovered from two real prior editions Kyle
  shared (8/10-8/16 and 8/17-8/23/2026) that predate this vault.
- Prospecting Ledger app: deploy on a free Netlify subdomain, not a custom
  domain.
- Prospecting Ledger app: no login — private, hard-to-guess URL instead of a
  password.
- Website stack: custom React/TS/Vite chosen over WordPress + IDX.
- Team name is "The Friedman Team" — "Friedman Real Estate Team" and any
  "real estate"-inclusive variant retired.
- Friedman Report workflow retro (2026-09-20, week of 9/14-9/20, went smoothly): story uses first names only and ends with a win (offer in hand); GBP is a mini Substack of about 1,450 characters; Instagram Reel caption replaces the YouTube description; no Instagram carousel for the weekly report; website hero must be 16:9 (site crops); homepage FMMI gauge needs the label `<p>` and the sub-score alt text with `%` signs in each week's article; chart data uses verified weeks only; reusable generators saved in `scripts/report/`. Details in `projects/friedman-report.md`.
