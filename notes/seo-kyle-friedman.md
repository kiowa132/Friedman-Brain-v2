# SEO — Rank for "Kyle Friedman" (website + Google Business Profile)

Goal: when someone searches **Kyle Friedman**, the friedmanreteam.com site
ranks #1 and the Google Business Profile shows in the map pack / knowledge
panel. Plus general SEO via internal linking.

## The bigger picture (what actually moves rankings)
Technical SEO here is done — it's hygiene, not a growth lever. After ~1
month of flat rankings, the gaps are **backlinks** and **review velocity**,
in priority order:
1. **Google Business Profile / reviews** — fastest local win. A review
   *system* (every closing → same-day request, 2-4/mo, reply to all,
   reviewers name the town + buy/sell). Also collect on Zillow /
   Realtor.com / Facebook. Weekly GBP posts, monthly photos, all fields
   filled, service areas trimmed to the 4 counties.
2. **Links** — new site + ~zero backlinks = no rank. Over 60 days:
   citations (Yelp, BBB, Chamber, Realtor.com, Homes.com, Nextdoor, Bright
   MLS, eXp team page); the Maryland Professional Network (mutual links —
   currently unused); local partners (lender/title/inspector/stager
   preferred-partner links); local sponsorships ($200-500, listed with a
   link); HARO/Qwoted/Featured for press mentions; pitch the weekly
   Friedman Report to Carroll County Times / Baltimore Sun / Patch / local
   FB groups as a data source.
3. **Striking-distance keywords** — Search Console → queries at position
   8-20 → add internal links w/ that anchor, expand that section, get one
   link. 12 → 6 roughly doubles clicks.
4. **Deep neighborhood pages + topical clusters** — thin town pages don't
   rank; "Living in <Town>, MD" with local data/schools/commute/photos
   does. Pillar page + 8-10 interlinked supporting posts.
5. **YouTube** — @SimplyFriedman is underused. Town tour + market-update
   videos titled "<Town> MD Real Estate", embedded on the matching
   neighborhood/blog page (`youtubeVideoId` field already wired).

Timeline: name/branded = days once indexed; map pack for "<town> realtor" =
1-3 mo with the review push; blog long-tail = 2-4 mo/post; head terms
("carroll county homes for sale") = 6-18 mo and needs link authority.

## The internal-linking tactic (from the video Kyle shared)
1. Google `site:friedmanreteam.com "keyword"` — shows which of your pages
   already rank for that keyword.
2. From each of those pages, add an internal link to the page you *want*
   ranking for that keyword, using the keyword as the anchor text.
3. That's it — it concentrates internal relevance/authority on the target
   page for that term.

Applied here: the blog posts are the crawlable, topic-rich pages. Every
post now links "Kyle Friedman" → `/about` (byline + author block), and
each post should also weave 1-2 keyword-anchored links to the money pages
(`/buy`, `/sell`, relevant `/neighborhoods/*`). Keep doing that in every
new post (already in `../projects/blog-article.md` deliverable 2).

## Done in code this session (The-friedman-team-website repo)
- **`src/pages/AboutPage.tsx`** — added a standalone `Person` JSON-LD block
  with `mainEntityOfPage` → `/about` (Google keys a person entity off
  this; index.html only had Kyle nested as `founder`). Also retitled the
  page to lead with the exact name: "Kyle Friedman | Realtor, The Friedman
  Team | Carroll County, MD".
- **`src/pages/BlogPostPage.tsx`** — the byline name + photo and the
  "Meet the Author" heading now link to `/about` with "Kyle Friedman"
  anchor text (was plain text). ~20+ internal links with exact-match
  anchor pointing at the page we want ranking for the name.

## Canonical name decision (2026-08)
Business name = **"The Friedman Team by Kyle Friedman"** (matches the live
Google Business Profile; the name containing "Kyle Friedman" also helps
that branded search). Done in code: `index.html` schema `name` +
`founder.worksFor.name`, `AboutPage.tsx` `personSchema.worksFor.name`, and
the `/about` title in `usePageMeta` + `middleware.ts` all updated to this;
`streetAddress` changed `#350` → `Suite 350` to match GBP; the GBP share
link `https://share.google/q91ZdJrdKqZ3o5NUd` added to both `sameAs`
blocks. Kyle is updating Zillow / Realtor.com / Homes.com / Bright MLS /
Facebook Page to the same name + address.

MD real estate license **673223** (exp 2028-02-05) is now in the Person
schema as `hasCredential`. Bright MLS agent ID: 3264576.

## Still needed from Kyle to finish the code
- **Realtor.com / Homes.com agent-profile URLs** (if they exist) → add to
  `sameAs`.
- Ideally swap the `share.google/q91Zd…` short link for the full
  `google.com/maps/place/…` URL once Kyle grabs it.

## Zillow profile cleanup (Kyle, 2026-08)
- Professional title: "Real Estate **Proffesional**" → "Professional"
- "In business since 2016" contradicts the bio's "since 2020" — pick the
  true year, make both match
- Service areas were full of DC-metro / PG / Anne Arundel towns (Silver
  Spring, College Park, Bowie, Annapolis, Capitol Heights…) — trim to the
  real footprint: Carroll, Baltimore, Howard, Frederick county towns only
- Specialties list is broad (Property Management, Foreclosure specialist) —
  prune to what's true and on-brand ($400K+ direction)
- Bio: add Frederick County to the "throughout … communities" line; fix
  "transaction it is about" → "transaction — it's about"
- Name field (General info) stays "Kyle Friedman"; the /about link + full
  business name are in the bio ✓

## Nav crawlability — DONE (2026-08)
`Footer.tsx` and `Navbar.tsx` now render real react-router `<Link>` (=
`<a href>`) for every navigation item instead of `<button onClick>`.
Crawlers can follow the internal link graph. Modal/toggle triggers
(Home Valuation, dropdown open/close, menu open) correctly stay `<button>`.
Deployed with the schema/redirect batch.

**Follow-up done (2026-08):** footer "Key Markets" now deep-links to real
town pages (Westminster, Hunt Valley, Clarksville, Downtown Frederick,
Fulton, Eldersburg, Mount Airy). Footer "Navigation" now also links the 6
pages that had zero crawlable inbound links (`/guides`, `/videos`,
`/financing-options`, `/calculators`, `/past-transactions`, `/network`).
`/network*` routes added to `generate-sitemap.mjs`.

## Search Console index issues (reviewed 2026-08)
- **Fixed in code** (`vercel.json` redirects): `/sell-your-home` → `/sell`,
  `/market-reports` → `/blog` (genuinely old URLs; cleared 2 of 4
  "duplicate, no canonical" flags).
- **5xx on `/transactions/803-c-st-ne-washington-dc`** — it IS a real page
  (slug is in `mentorTransactions.ts`). Site is a static SPA (always 200),
  so the 5xx came from the Vercel Edge Middleware — most likely a transient
  cold-start on one crawl. Click "Validate Fix" in GSC and monitor; if it
  recurs, the middleware bundles ALL transaction/town/network data and is
  probably too heavy — trim it then.
- **2 `/transactions/*` pages flagged "duplicate, no canonical"** — real
  pages, near-identical template. Google routinely skips near-dup template
  pages; not worth chasing (not money pages). Add unique per-transaction
  copy later if it matters.
- "Page with redirect" (http / non-www) and "?price=" calculator variant —
  working as intended, ignore.

## Off-site checklist (Kyle — can't be done in code)
**Google Search Console**
- Verify `friedmanreteam.com`, submit `sitemap.xml`
- URL Inspection → Request Indexing on `/` and `/about` after this deploy

**Google Business Profile**
- Business name **exactly "The Friedman Team"** — never "Friedman Real
  Estate Team" (matches the site; the naming rule in
  `brand-guidelines.md`)
- Primary category: Real Estate Agent (secondary: Real Estate Agency)
- Address identical to the site: 8115 Maple Lawn Blvd #350, Fulton, MD
  20759 — or set up as a service-area business, but pick one and be
  consistent everywhere
- Phone (443) 789-3101; website field → https://www.friedmanreteam.com
- Fill every field: hours, services, the 4 service-area counties,
  description with "Kyle Friedman" in the first sentence
- Photos: logo, cover, 10+ real photos
- Weekly Google Posts (use the blog GBP deliverable)
- Reviews: steady flow, reply to every one, nudge reviewers to name
  "Kyle Friedman" and their county
- Seed 3-4 real Q&A entries

**NAP consistency** — identical address / phone everywhere. For the
*business name* field: use "The Friedman Team by Kyle Friedman" on
Realtor.com, Homes.com, Yelp, the Facebook business Page, BBB, local
chamber, Bright MLS. **Zillow is a personal agent profile** — keep the
name field as "Kyle Friedman" (person), brokerage "eXp Realty", team field
(if any) "The Friedman Team by Kyle Friedman", website field →
`friedmanreteam.com/about`. Google links the Zillow person node to the GBP
business node via `sameAs`; they don't need matching names.

**Entity links** — every social bio (LinkedIn contact info, FB page About,
IG link, YouTube channel links, Zillow profile website field) should link
to `friedmanreteam.com/about` specifically, not just the homepage.

**A few real inbound links** to `/about` with "Kyle Friedman" anchor —
chamber, partner vendors, Maryland Professional Network members.

The website lives in a separate repo:
`C:\Users\kylej\Documents\GitHub\The-friedman-team-website` (Vite/React,
auto-deploys on push). See [[friedmanreteam-website]] for build status.
