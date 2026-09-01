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
- `decisions.md` — running log of open decisions and resolved calls, so
  nothing gets re-litigated or forgotten.

## Standing procedures — start here for recurring work
- [[projects/listing-presentation.md]] — seller listing presentation package
- [[projects/friedman-report.md]] — weekly Friedman Report
- [[projects/friedman-report-log.md]] — weekly MLS data log (feeds the
  comparison table — check this before asking Kyle for data)
- [[projects/blog-article.md]] — blog article maker (on-demand articles +
  standing Friday queue with multiple ready options)
- [[projects/blog-article-queue.md]] — ready articles Kyle can pick from
- [[projects/blog-article-log.md]] — topics already published
- [[projects/sell-vs-rent-analysis.md]] — client sell vs. rent vs. HELOC
  comparison (framework, expense model, Section 121 rule)
- [[projects/report-images.md]] — free auto image generation for reports
  (`scripts/gen-image.ps1` + Gemini free tier); prompt templates + slot maps
- [[projects/friedmanreteam-website.md]] — friedmanreteam.com build status
- [[projects/prospecting-ledger-app.md]] — Ledger prospecting tracker app

## Reference
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
