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

## Editing (Decap CMS) — the fast workflow
`friedmanreteam.com/admin` → **"Sign Listings (For Sale Sign QR)"** collection.
Per listing, Kyle only needs to set:
1. **active** toggle (ON for the one the sign points at).
2. **MLS #** — address, price, beds, baths, sq ft, year, status, and the
   description all pull in **live from Lofty** by that number.
3. **Photos** — drop them all into `public/images/listings/<slug>/` via
   GitHub's "Add file → Upload files" (drag a whole folder at once). Sorted
   by filename; name one `hero.*` to force the main image.

Every other CMS field is an optional **override** (only if Lofty is wrong,
or there's no MLS # yet). Saving commits to GitHub → Vercel rebuilds
(~1 min) → live.

### Data precedence (per field)
CMS override → live Lofty lookup → photo folder. Blank everywhere = field
just doesn't show.

### Requires (one-time, Kyle's action)
Lofty auto-fill needs **`LOFTY_API_KEY`** set in Vercel project env vars
(Lofty: Settings → Integrations → API). Until then the page still works
with manual override fields. Same key would also switch on the site's
whole IDX `/listings` search, which is currently dormant for the same reason.

Rule: only ONE listing should have `active: true` at a time. Turn it off on
the old one when switching.

Multiple active listings at once: add `listing-2.md`, `listing-3.md`, print a
QR for each `/listings/listing-2` etc. (or number sign riders). `/listings/active`
still points at the single flagged one.

## Build details (The-friedman-team-website repo)
- Content: `content/listings/*.md` (frontmatter: `active`, `mlsId`, + optional
  overrides; markdown body = optional highlights override).
- Loader: `SIGN_LISTINGS` in `src/lib/content.ts` — merges in the photo
  folder from `listingsManifest.json`.
- Type: `SignListing` in `src/types.ts`.
- Page: `src/pages/SignListingPage.tsx` — runtime Lofty lookup by MLS # via
  `fetchMlsListings({q: mlsId})` (`/api/mls/search`, existing IDX plumbing);
  merges CMS → Lofty → folder photos. Status badge, stats, hero, gallery,
  highlights, Text/Call/Email CTAs, map link, JSON-LD.
- Router: `src/pages/ListingRouteSwitch.tsx` — the `/listings/:mlsNumber`
  route dispatches: curated slug → SignListingPage, `active` → redirect to
  the `active: true` listing, anything else → the existing IDX
  `ListingDetailPage` (lazy).
- Photos: `public/images/listings/<slug>/` (batch upload), scanned by
  `scripts/generate-listings-manifest.mjs` → `src/data/listingsManifest.json`
  (`hero` + `photos` fields). That manifest also feeds `middleware.ts`
  (crawler `/listings/<slug>` previews, `/listings/:slug*` matcher) and
  `content.ts`. Script is in `prebuild`.
- Sitemap: `generate-sitemap.mjs` lists `/listings/<slug>` (not
  `/listings/active`, which is a redirect).

## Deploy history
- Batch 1 (base feature): `b43fd72` — LIVE.
- Batch 2 (MLS auto-fill + folder photos): `02b0e91 "launch"` — LIVE.
- Batch 3 (2026-09-01, fixes after Kyle tested):
  - **Sveltia CMS** swapped in for Decap (`public/admin/index.html`, one
    `<script>` line) — for real multi-select photo upload. Same config.yml,
    same GitHub OAuth (`api/decap-auth`). Revert = swap the line back.
  - `SignListingPage` now also calls `fetchMlsListingDetails(hit.id)` for
    the **full Lofty photo gallery + remarks**, not just the 1 preview pic.
  - Re-added the `photos` list field to the CMS (manual fallback).
  - Config hints: compress photos < 400KB before upload.

## Batch 4 (2026-09-02) — resumed, items 1 & 2 done, 3 staged

- **1. Build-time Lofty pull — DONE.** New `scripts/fetch-sign-listing-data.mjs`
  runs first in `prebuild`; for each `content/listings/*.md` with an `mlsId` it
  calls Lofty once and bakes address/price/beds/baths/sqft/status/gallery/
  remarks into `src/data/signListingsData.json`. `content.ts` + the manifest
  generator merge it UNDER any CMS override. `SignListingPage.tsx` no longer
  does any runtime fetch — removed the `useEffect`, the `mls*` state, the
  `fetchMls*` imports, and the "Pulling the latest details…" line. Page is now
  static + instant. New helper `fetchListingByMls()` in `server/mlsClient.js`.
- **2. MDWC2023688 lookup — improved + made graceful.** `fetchListingByMls`
  first tries a direct server-side MLS-number filter (a few field-name guesses),
  then falls back to the keyword scan widened to 40 pages (`__maxPages`) since
  build time can afford it. If it still finds nothing (Wicomico/Eastern Shore
  is very likely outside Kyle's Lofty feed), the build **logs a clear warning
  and does not fail** — the CMS override fields carry the page. `listing-1.md`
  now has the 315 Park Ave values filled back in as overrides so it works today.
- **3. Batch photo upload — STAGED, needs Kyle's action.** `public/admin/
  config.yml` has a commented `media_library: { name: cloudinary }` block with
  a 4-step setup (free Cloudinary account → cloud name + API key → uncomment →
  commit). That switches the media picker to multi-select + auto-compress. The
  GitHub folder-upload route (`public/images/listings/<slug>/`) still works as
  the zero-dependency option.
- Stray `public/images/uploads/img_0172.jpg` (13.8 MB) — **deleted** (`git rm`).

**PAUSED AGAIN 2026-09-02.** Batch 4 code is written and `git add`-ed in the
website repo but NOT committed or pushed — working tree has all 11 files staged.
To resume: `cd ~/Documents/GitHub/The-friedman-team-website`, review `git diff
--cached`, then commit + push. First real test is the Vercel build log
(`[sign-listings]` line) since there's no local Node to build with.
Still open: item 3 (Cloudinary account — Kyle's action, config block staged
commented in `public/admin/config.yml`).

## (historical) PAUSED 2026-09-01 — 3 things to fix when resumed

Kyle tested batch 3 and stopped here. Admin is working (Decap, Sveltia
reverted). Three open problems, in priority order:

### 1. Re-architect the Lofty pull: fetch once, not per visitor
Kyle's call, and he's right: `SignListingPage` currently does a **runtime**
`fetchMlsListings` + `fetchMlsListingDetails` on every page load — slow first
paint ("pulling listing details…" then blank), and dependent on Lofty being
up. Instead: pull the MLS data **ahead of time** and store it, so the page
is instant + static.
- Option A (best fit): a prebuild step. New script
  `scripts/fetch-sign-listing-data.mjs` — for each `content/listings/*.md`
  with an `mlsId`, call Lofty (reuse `server/mlsClient.js`), write
  address/price/beds/baths/sqft/status/gallery/remarks into
  `src/data/listingsManifest.json` (or a sibling `listingsData.json`).
  `SIGN_LISTINGS` in `content.ts` then merges: CMS override → baked Lofty
  data → folder photos. No runtime fetch at all. Refreshes every deploy;
  add a daily Vercel cron rebuild if staleness matters (status/price change).
  Needs `LOFTY_API_KEY` available at build time (it's a Vercel env var —
  confirm it's exposed to the build, not just serverless runtime).
- Option B: keep runtime but cache the first successful response into the
  markdown on load via a serverless write-back. More moving parts; skip.
- Remove the runtime `useEffect` fetch from `SignListingPage` once A is in.

### 2. Lofty returned nothing for MDWC2023688
Blanked `listing-1` (active + `mlsId: MDWC2023688` only) rendered fully
blank — the live fetch found nothing. Likely causes to check with the
Network tab (F12 → `api/mls/search` response) or `DEBUG_MLS=true`:
- The keyword scan in `searchListings` is depth-limited and Wicomico
  County / Salisbury (Eastern Shore) sits outside the site's usual
  Carroll/Baltimore/Howard/Frederick focus — may not be in the scanned
  pages.
- Lofty feed may not index by that exact Bright `mlsListingId`, or the feed
  is scoped to certain counties.
- **Fix path:** add a real "get one listing by MLS number" call to
  `server/mlsClient.js` if Lofty's API supports it (check their docs /
  support), rather than the brute-force keyword scan. That also makes
  Option A above reliable.
- Until then: Kyle fills the override text fields manually (the fields are
  all still in the CMS).

### 3. Batch photo upload still not solved
The CMS `photos` list widget only adds one slot at a time — that's what
Kyle keeps hitting. The GitHub-folder route
(`public/images/listings/<slug>/` + `generate-listings-manifest.mjs` scan)
IS built and works, but Kyle wants it inside `/admin`, not a separate
GitHub trip. Real options:
- **Cloudinary or Uploadcare media library for Decap** — official Decap
  integrations, true multi-select upload AND automatic image compression
  (solves the 13.8 MB phone-photo problem too). Needs a free account + one
  key in `config.yml` `media_library:`. Best fix.
- **Sveltia CMS, done properly** — it has native multi-upload, but the
  migration needs every config incompatibility fixed in one pass (first
  one hit: blog `publishDate` `widget: "date"` → `widget: "datetime"` +
  `time_format: false`; there may be more in the `fmmi` object / markdown
  widgets). Do it on a branch, click through the whole `/admin` before
  merging.
- Leftover: delete unreferenced `public/images/uploads/img_0172.jpg`
  (13.8 MB) from the repo.

---

## KNOWN BLOCKER — Lofty not connected
`fdd4ced`: Kyle entered `mlsId: MDWC2023688` and it pulled **nothing**,
because:
1. **`LOFTY_API_KEY` is almost certainly not set in Vercel.** Without it
   every `/api/mls/*` call returns 501 and no auto-fill can work. This is
   step one. (Lofty → Settings → Integrations → API → key → Vercel env var
   → redeploy.) Same key lights up the whole dormant `/listings` IDX search.
2. Even with the key, `listing-1.md` currently has every field filled in as
   an override, which masks whatever Lofty would return. To test/use pure
   auto-fill, clear the override fields in the CMS (leave only `active` +
   `mlsId`); they repopulate from Lofty if it's connected.
- Also: a 13.8 MB uncompressed phone photo got committed to
  `public/images/uploads/img_0172.jpg` (unreferenced). Delete it; compress
  to < 400 KB before any upload.

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
