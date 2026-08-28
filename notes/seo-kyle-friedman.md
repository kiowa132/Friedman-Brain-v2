# SEO — Rank for "Kyle Friedman" (website + Google Business Profile)

Goal: when someone searches **Kyle Friedman**, the friedmanreteam.com site
ranks #1 and the Google Business Profile shows in the map pack / knowledge
panel. Plus general SEO via internal linking.

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

## Still needed from Kyle to finish the code
- **Google Business Profile public URL** (maps place link or g.page short
  link) → add to `sameAs` in `index.html` and the `personSchema` in
  `AboutPage.tsx`, so Google binds site ↔ GBP.
- **REALTOR license number** → add as a `hasCredential` block on the
  Person schema.
- **Realtor.com / Homes.com agent-profile URLs** (if they exist) → add to
  `sameAs`.

## Known bigger issue (not yet fixed)
`src/components/Footer.tsx` (and likely `Navbar.tsx`) build navigation with
`<button onClick={goTo(...)}>` instead of `<a href>` / react-router
`<Link>`. Crawlers don't follow buttons as links, so the site's internal
link graph is much thinner than it looks. Converting primary nav + footer
to real `<Link>`/`<a href>` is a worthwhile, larger change.

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

**NAP consistency** — identical name / address / phone on Zillow,
Realtor.com, Homes.com, Yelp, the Facebook business Page, BBB, local
chamber, Bright MLS agent profile. "The Friedman Team" everywhere.

**Entity links** — every social bio (LinkedIn contact info, FB page About,
IG link, YouTube channel links, Zillow profile website field) should link
to `friedmanreteam.com/about` specifically, not just the homepage.

**A few real inbound links** to `/about` with "Kyle Friedman" anchor —
chamber, partner vendors, Maryland Professional Network members.

See [[friedman-website-repo]] for the repo/deploy setup.
