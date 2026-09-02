# For-Sale-Sign Listing Page — friedmanreteam.com

Purpose: one QR code on the physical For Sale sign that never has to be
reprinted, always showing the current listing. Kyle's own version of the
paid "dynamic QR" his mentor buys from Bitly.

## How it works
- **QR target (print once, never change):** `https://www.friedmanreteam.com/listings/active`
- `/listings/active` is a redirect. It forwards to whichever sign listing
  has `active: true`.
- The real page lives at `/listings/<slug>` — currently `/listings/listing-1`.
- To point the sign at a new house: edit the listing (or add a new one) and
  flip the `active` checkbox. The printed QR is untouched.

## Editing (Decap CMS)
`friedmanreteam.com/admin` → **"Sign Listings (For Sale Sign QR)"** collection.
Fields: active toggle, status, address, city/state/zip, price, beds, baths,
sqft, lot, year, MLS#, tour URL, hero photo, photo gallery, highlights/description.
Only filled-in fields show on the page. Saving commits to GitHub → Vercel
rebuilds (~1 min) → live. No local build needed.

Rule: only ONE listing should have `active: true` at a time. Turn it off on
the old one when switching.

Multiple active listings at once: add `listing-2.md`, `listing-3.md`, print a
QR for each `/listings/listing-2` etc. (or number sign riders). `/listings/active`
still points at the single flagged one.

## Build details (The-friedman-team-website repo)
- Content: `content/listings/*.md` (YAML frontmatter + markdown body =
  highlights). Mirrors the blog pipeline exactly.
- Loader: `SIGN_LISTINGS` in `src/lib/content.ts`.
- Type: `SignListing` in `src/types.ts`.
- Page: `src/pages/SignListingPage.tsx` (status badge, address, price, stat
  row, hero, gallery, highlights, Text/Call/Email CTAs, map link, JSON-LD).
- Router: `src/pages/ListingRouteSwitch.tsx` — the `/listings/:mlsNumber`
  route now dispatches: curated slug → SignListingPage, `active` → redirect,
  anything else → the existing IDX `ListingDetailPage`.
- Crawler previews: `scripts/generate-listings-manifest.mjs` →
  `src/data/listingsManifest.json`, imported by `middleware.ts` (new
  `/listings/<slug>` branch + `/listings/:slug*` matcher). Added to `prebuild`.
- Sitemap: `generate-sitemap.mjs` now lists `/listings/<slug>` (not
  `/listings/active`, which is a redirect).

## First listing (set up 2026-09-01)
`content/listings/listing-1.md` — 315 Park Ave, Salisbury MD 21801 ·
Pending · $199,999 · 6 bd / 3 bath / 3,080 sq ft · active: true.
**Still needs:** hero photo, gallery photos, and a description — add via /admin.

## Notes / possible future changes
- The reusable-slot slug (`listing-1`) means page content rotates under a
  fixed URL — mild SEO wart. If Kyle later wants each listing permanently
  indexed, switch to address slugs (`/listings/315-park-ave`) and keep
  `/listings/active` as the only redirect. Page + router already support any
  slug; would just change the file naming + keep sold pages up.
- Alternative to building this: Dub.co / Short.io free tier (custom
  subdomain, editable destination, QR + analytics) — considered, not used.
