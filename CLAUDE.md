# The Friedman Team — Brain (Root Map)

This is Kyle Friedman's knowledge base for The Friedman Team real estate
business. If you are an AI agent (Claude Code or otherwise) working from this
folder, read this file first — it tells you where everything lives and how to
use it.

## Folder structure
- `projects/` — standing procedures and status for recurring/ongoing work.
  Each file documents a repeatable workflow end-to-end: what to build, what
  inputs are needed, and any templates. When Kyle drops in raw inputs for one
  of these, follow the file's procedure rather than asking him to re-explain
  it from scratch.
- `notes/` — durable reference facts: brand guidelines, naming rules, tool
  configuration. One topic per file.
- `people/` — cards for key contacts (clients, mentor, vendors). Not
  pre-populated — add as needed.
- `clients/` — deeper per-client working analyses that outgrow a `people/`
  card (e.g. move-up feasibility studies). The `people/` card stays the
  index; the detail lives here.
- `listings/` — per-listing packages (CMA data, pricing, net-proceeds,
  paperwork field-maps). `listings/_forms/` holds the blank form templates.
- `properties/` — hero-image generation staging for the weekly report, one
  folder per property (`photos/` raw drops, `generated/` scratch AI
  attempts, `final/` shipped compressed images, `image-log.md`). See
  `properties/README.md` and [[projects/report-images.md]]. Not the same
  thing as `listings/` — this is image production, not deal data.
- `marketing/` — physical/print marketing assets and reusable copy: the
  Avery mailing labels, the monthly-card mail-merge list (feeds
  [[projects/mailing-list.md]]), and
  [[marketing/listing-process-roadmap.md]] — the 10-step "WE ARE HERE"
  listing roadmap card, **reusable for every listing presentation**.
  [[projects/listing-presentation.md]] doesn't currently call this out as
  a required deliverable component, confirm with Kyle whether it should.
- `brand-assets/` — logo, headshot, and lockup image files referenced by
  the PDF generator scripts and Gamma decks.
- `scripts/` — reusable generators: `scripts/pdf/` (net-proceeds and
  listing-presentation PDF/Excel builders, one script per past listing,
  copy the closest match for a new one), `gen-image.ps1` / `keep-image.ps1`
  (report hero images, see `properties/`), `compress-photos.py`.
- `drafts/` — staging for in-progress content: `friedman-report/` (weekly
  report drafts), `blog-articles/`, plus occasional one-off client email
  drafts.
- `decisions.md` — running log of open decisions and resolved calls, so
  nothing gets re-litigated or forgotten.

## Sibling repos (same parent folder, not inside this one)
- `friedman-crm/` — the Friedman CRM app itself. See
  [[projects/crm-app.md]] here for the model/plan; the repo's own
  `README.md` / `ARCHITECTURE.md` have the current build status.
- `The-friedman-team-website/` — friedmanreteam.com. See
  [[projects/friedmanreteam-website.md]] and [[projects/sign-listing-page.md]].
- `Vendtrack/` — **a separate business**, a vending-machine inventory/cash
  tracker, unrelated to real estate. Not part of The Friedman Team brain's
  scope, listed here only so an agent poking around the parent folder
  doesn't mistake it for a Friedman Team project.

## Standing procedures — start here for recurring work
- [[projects/crm-app.md]] — **Friedman CRM**, the custom $0/mo Follow Up
  Boss replacement (data model, cascade automations, screen list, build
  phases). The actual app lives in the sibling folder `friedman-crm/` (its
  own repo, nested inside this one on disk, see its `README.md` /
  `ARCHITECTURE.md` for current build status, already well past planning:
  Today screen, People, Person detail, Deals pipeline, Templates,
  Settings, FUB import, Gmail send, 2-way Google Calendar sync, and AI
  drafting/briefs are already built. Cutover off FUB targeted for
  Oct 31, 2026.
- [[projects/listing-presentation.md]] — seller listing presentation package
- [[projects/listing-scripts.md]] — vetting-call script (qualify before booking)
  + listing-presentation close + objection handlers
- [[projects/friedman-report.md]] — weekly Friedman Report
- [[projects/friedman-report-log.md]] — weekly MLS data log (feeds the
  comparison table — check this before asking Kyle for data)
- [[projects/blog-article.md]] — blog article maker (on-demand articles +
  standing Friday queue with multiple ready options)
- [[projects/blog-article-queue.md]] — ready articles Kyle can pick from
- [[projects/blog-article-log.md]] — topics already published
- [[projects/sell-vs-rent-analysis.md]] — client sell vs. rent vs. HELOC
  comparison (framework, expense model, Section 121 rule)
- [[projects/feasibility-analysis.md]] — buyer feasibility analysis (can a
  move/purchase in a target area pencil): scope, inputs, section skeleton,
  standing assumptions, Syed-run lessons
- [[projects/report-images.md]] — free auto image generation for reports
  (`scripts/gen-image.ps1` + Gemini free tier); prompt templates + slot maps
- [[projects/friedmanreteam-website.md]] — friedmanreteam.com build status
- [[projects/prospecting-ledger-app.md]] — Ledger prospecting tracker app
- [[projects/sign-listing-page.md]] — For Sale sign QR → /listings/active
  (one permanent QR, editable current-listing page via Decap CMS)
- [[projects/mailing-list.md]] — /mailing-list signup + sports-schedule /
  monthly-card freebie funnel; how to pull the mail-merge list from FUB

## Reference
- [[notes/accounts.md]] — logins/2FA recovery codes for business tools (not
  git-tracked, local only)
- [[notes/brand-guidelines.md]] — visual identity, naming rules, brand voice
- [[notes/ai-video-tools.md]] — AI avatar / digital-twin video options
  (paid SaaS + free open-source stack) for realistic video of Kyle
- [[notes/seo-kyle-friedman.md]] — plan to rank the site + GBP for
  "Kyle Friedman"; what's done in code, what Kyle owes off-site
- [[decisions.md]] — open questions and resolved decisions

## Rules for any agent working in this folder
- Team name is always "The Friedman Team" — never "Friedman Real Estate Team"
  or any "real estate"-inclusive variant.
- Before building anything branded (decks, emails, social posts), check
  `notes/brand-guidelines.md` for current visual identity and voice — don't
  assume, check.
- If a procedure file and a live conversation disagree about current process,
  ask Kyle which is current rather than silently picking one — then update
  this brain to match.

## A note on scope
This folder is the source of truth for *procedures and durable facts* about
Kyle's business. It does not run anything on its own — scheduled tasks, live
data pulls (MLS, mortgage rates, CRM), and posting automation are separate
tools that should read their instructions from here rather than duplicating
them internally.
