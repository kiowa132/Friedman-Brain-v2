# Blog Article Maker — Standing Procedure

Generalized from the original Friday-only version. Handles two separate
request types — read which one applies before starting.

## What every finished article is — 4 deliverables
1. **Substack version** (`substack.md`) — shorter, punchier, conversational.
   Roughly 500-700 words. This is what actually gets read start-to-finish in
   an email/feed — get to the point fast, less structural scaffolding.
2. **Website SEO version** (`website-seo.md`) — longer and structured for
   search. Roughly 900-1300 words, clear H2s built around what someone
   would actually search, natural keyword usage (don't force it). Include
   at the top:
   - **Meta title** (≤60 characters)
   - **Meta description** (≤155 characters)
   - **Target keyword/phrase** it's written around
   These two versions cover the same topic and points but are NOT the same
   text reformatted — write each for how it's actually consumed.
3. **4 detailed image prompts** for use in ChatGPT/DALL-E/Midjourney
4. **A 15–20 second social video script** — story/hook-driven, NOT Kyle
   reciting data to camera. Hook in first 2-3s, a turn/twist, short payoff.
   Time-coded table (time / visual+edit direction / audio or on-screen
   text).

## Mode 1 — On-demand ("I need an article about X")
Kyle names a topic directly, any day, any time.
1. Check `blog-article-log.md` — if this topic's already been covered,
   flag it to Kyle rather than silently duplicating; he may still want a
   fresh angle on it, but ask first.
2. Research it (web search — don't state Maryland-specific legal/tax/
   financing facts from memory alone).
3. Write the Substack version + website SEO version + 4 image prompts +
   video script.
4. Deliver directly to Kyle — no queue detour needed for an on-demand
   request.
5. Log it in `blog-article-log.md`.

## Mode 2 — Standing Friday queue (Kyle picks from ready options)
The queue should hold **multiple ready articles at once** (aim for at
least 3), so Kyle is choosing which one to run, not just accepting
whatever's next.

**Batch/refill session** (whenever the queue drops below ~3 ready items):
1. Check `blog-article-log.md` and `blog-article-queue.md` — never repeat
   a topic in either.
2. Propose new topic candidates to Kyle first — don't write on spec.
   Favor topics reinforcing brand positioning (see
   `../notes/brand-guidelines.md`), especially the farm/equestrian niche.
3. Once approved, research and fully write each one (Substack version +
   website SEO version + 4 image prompts + video script), save to
   `../drafts/blog-articles/<date-slug>/`, add to `blog-article-queue.md`
   as "ready" with a one-line summary — no fixed Friday date attached.

**Weekly Thursday check** (by Thursday, not Friday):
1. Read `blog-article-queue.md` — surface the full list of ready items
   with their one-line summaries to Kyle.
2. Kyle picks which one runs this week. Move that one from the queue to
   `blog-article-log.md`; the rest stay in the queue for a future week.
3. If fewer than 3 ready items remain after Kyle's pick, that's the
   trigger to run a refill batch session before next Thursday.

## Standing build rules
- Branding & tone: follow `../notes/brand-guidelines.md` — don't duplicate
  those rules here, check there.
- Never generate Kyle's actual face via AI image tools — text-to-image
  tools can't reliably reproduce a specific real person anyway. If Kyle
  wants himself in a graphic: use a real photo + add text/graphics in
  Canva, not AI generation.
- Don't rely on AI tools for legible on-image text — recommend adding text
  as a post-process step (Canva) instead.
