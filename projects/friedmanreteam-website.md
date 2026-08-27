# friedmanreteam.com — Build Status

## Stack
React/TypeScript/Vite SPA on Vercel, Decap CMS, Tailwind CSS, Framer Motion,
Recharts.

## Completed
- Sitewide interactivity: scroll-reveal, page transitions, animated Market
  Pulse card with FMMI gauge
- Full lead capture system: gated calculator results, blog scroll gate,
  TCPA-compliant forms across 8 touchpoints
- Maryland Professional Network section at `/network/*`
- Luxury section expansion
- Sitewide OG/social preview meta via Vercel Edge Middleware
- RealEstateAgent JSON-LD schema; sitemap.xml + robots.txt via prebuild
  script; Place+BreadcrumbList schema on all 30 neighborhood town pages
- All 30 neighborhood town pages have real written content
- Master copy bank: brand mission, homepage, buyer/seller/luxury pages,
  detailed Seller Process page

## Open items
- [ ] Test all lead capture forms into Follow Up Boss
- [ ] Decide on IDX data approach (see `../decisions.md`)
- [ ] Add Privacy Policy / Terms pages
- [ ] Supply real neighborhood photos as available
- [ ] Google Business Profile has zero reviews — building initial reviews is
      the top local SEO priority

## Notes
- Explored WordPress + IDX before committing to the custom React stack.
- Lofty MLS API confirmed to return only one photo and no description per
  listing — full data only via Lofty's hosted site or WordPress plugin; IDX
  Broker identified as the likely upgrade path.
- Visual identity: see `../notes/brand-guidelines.md`.
