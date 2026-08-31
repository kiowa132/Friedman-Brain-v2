# Decisions Log

## Open
- [ ] Should listing-presentation Gamma decks (currently Aurum theme) move to
      the new teal/gold brand identity used on the website? — raised
      2026-08-26
- [ ] IDX data approach for the website — not yet decided. Lofty API returns
      only 1 photo and no description per listing; IDX Broker identified as
      the likely upgrade path.

## Resolved
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
