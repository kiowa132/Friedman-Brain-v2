# CRM App — data model + screen list (planning)

Replacement for Follow Up Boss ($70/mo). Same stack as VendTrack: React +
Vite + TypeScript + Tailwind, Supabase (Postgres + Auth + Storage), deploys
on Vercel. Phone-first PWA. Single user (Kyle) but modeled so a second seat
is a config change, not a rebuild.

**Hard cutover: Oct 31, 2026** (before the next FUB charge). Phase 1 below is
what has to be working by then.

---

## Design principles

1. **Multi-axis contacts.** Lead status, attempt progression, temperature,
   type, and source are *separate* fields you can sort or board by in any
   combination — the Podio flexibility FUB doesn't give you.
2. **One status change does the bookkeeping.** Moving a contact or a deal
   between stages cascades: creates the deal, spawns the task set, pauses
   nurture, converts to past client, etc. You never re-type an address.
3. **Dates drive tasks.** Milestone dates (appointment, settlement, closing)
   anchor task templates. Change the date → incomplete tasks recompute;
   completed ones don't move.
4. **The activity timeline is append-only.** Everything that happened to a
   contact is a permanent row. Corrections are new rows, not edits.
5. **AI assists, human sends.** Drafts, extraction, clustering, search —
   Kyle approves outbound. (Exception you may opt into: an after-hours
   first-touch auto-reply.)
6. **Client-facing copy never self-blames** (per brain memory) — applies to
   every AI-drafted message.

---

## Enums

- **lead_status:** `new`, `attempting`, `contacted`, `discovery`,
  `interested`, `appt_set`, `active_buyer`, `active_seller`,
  `under_contract`, `closed`, `nurture`, `past_client`, `sphere`, `dead`
  — *confirm this list against your Podio one*
- **dead_reason** (required when status = dead): `not_interested`,
  `wrong_number`, `cant_afford`, `wants_too_much`, `no_response`,
  `using_another_agent`, `unqualified`, `duplicate`, `do_not_contact`,
  `other`
- **temperature:** `hot`, `warm`, `cold`
- **contact_type:** `buyer`, `seller`, `both`, `investor`, `renter`,
  `agent`, `vendor`, `sphere`, `past_client`, `recruit`, `other`
- **activity_type:** `call`, `text`, `email`, `note`, `meeting`,
  `stage_change`, `task_completed`, `appointment`, `lead_created`,
  `presentation_sent`, `review_requested`, `system`
- **activity_direction:** `inbound`, `outbound`
- **call_outcome:** `connected`, `no_answer`, `left_voicemail`, `busy`,
  `wrong_number`, `not_interested`, `appointment_set`, `callback_requested`
- **task_type:** `follow_up`, `call`, `text`, `email`, `presentation_prep`,
  `gift_order`, `showing`, `admin`, `other`
- **task_status:** `open`, `done`, `cancelled`
- **appointment_type:** `listing_appt`, `buyer_consult`, `showing`,
  `phone_call`, `closing`, `open_house`, `other`
- **appointment_outcome:** `none`, `met`, `no_show`, `rescheduled`,
  `cancelled`, `completed`
- **rsvp_status:** `needs_action`, `accepted`, `declined`, `tentative`
- **deal_type:** `listing`, `buyer`
- **deal_stage_listing:** `potential`, `appt_set`, `signed`, `coming_soon`,
  `active`, `under_contract`, `pending`, `closed`, `fell_through`,
  `withdrawn`, `expired`
- **deal_stage_buyer:** `potential`, `consult_set`, `agreement_signed`,
  `active_search`, `offer_out`, `under_contract`, `pending`, `closed`,
  `fell_through`, `lost`
- **milestone_type:** `inspection`, `inspection_resolution`,
  `appraisal_ordered`, `appraisal_deadline`, `financing_contingency`,
  `title_commitment`, `walkthrough`, `settlement`, `possession`
- **objection_category:** `price`, `timing`, `commission`, `market_fear`,
  `spouse`, `another_agent`, `trust`, `wants_too_much`, `other`

---

## Data model

### people
The contact record. One row per person.

- `id`, `created_at`, `updated_at`
- `first_name`, `last_name`, `full_name` (maintained)
- `company`, `job_title` — *company doubles as the caller-ID label; the
  "Add to iPhone" button writes `FRIEDMAN CRM · <label>` here*
- `lead_status` (enum), `stage_entered_at` — when they entered current status
- `dead_reason` (enum, null unless dead)
- `temperature` (enum, null)
- `contact_type` (enum)
- `source_id` → lead_sources, `source_detail` (e.g. which Zillow listing)
- `referred_by_person_id` → people (null) — referral loop
- `owner_id` → operators (default Kyle)
- **attempt tracking:**
  - `attempt_count` int — attempts *since last connect* (resets on connect)
  - `attempt_count_lifetime` int — never resets, for analytics
  - `last_attempt_at` — any outbound call/text/email
  - `last_connected_at` — a real two-way (answered call, reply, met)
  - `last_activity_at` — anything incl. inbound + notes
- `next_action_at` — derived: earliest open task due date; `snooze_until` (manual)
- **preferences / compliance:** `do_not_call`, `do_not_text`, `do_not_email`
  (bool), `unsubscribed_at`
- **home / equity:** `home_address`, `home_city`, `home_state`, `home_zip`,
  `home_purchase_date`, `home_purchase_price`, `birthday`
- **buyer criteria (null for non-buyers):** `buyer_price_min`,
  `buyer_price_max`, `buyer_areas` text[], `buyer_beds`, `buyer_timeline`
- `about` text — freeform bio (dated notes live in activities)
- **sync flags:** `synced_to_phone` bool, `synced_to_google_contacts` bool,
  `google_contact_resource` text
- `tags` — via contact_tags

### contact_methods
Multiple phones/emails per person, typed (for vCard + caller-ID + search).

- `id`, `person_id`, `kind` (`phone` | `email` | `other`), `value`,
  `label` (`mobile` | `home` | `work` | `other`), `is_primary` bool
- index on `value` (inbound-call lookup, dedupe)

### tags, contact_tags
- `tags`: `id`, `name`, `color`
- `contact_tags`: `person_id`, `tag_id`

### activities  *(append-only)*
The unified timeline.

- `id`, `person_id`, `deal_id` (null), `occurred_at`, `created_at`, `created_by`
- `type` (enum), `direction` (enum, null)
- `outcome` (call_outcome, null) — for calls
- `subject`, `body` — emails / notes / meeting notes
- `duration_seconds` (null) — calls
- `channel_ref` — provider message id, google event id, etc.
- `meta` jsonb
- Written via the `log_activity()` RPC, which also updates the person's
  `last_attempt_at` / `last_connected_at` / `attempt_count` / `last_activity_at`.

### tasks
- `id`, `person_id` (null), `deal_id` (null), `title`, `description`
- `type` (enum), `status` (enum), `priority` (`low`|`normal`|`high`)
- `due_at`, `done_at`
- **anchoring:** `anchor_type` (`appointment`|`milestone`|`manual`),
  `anchor_id` (uuid, null), `anchor_offset_days` int (e.g. `-10`)
- `template_step_id` (null) — which sequence step created it
- `created_by`, `assigned_to`
- Recompute rule: on anchor date change, for `status='open'` tasks with that
  `anchor_id`, `due_at = anchor_date + offset`, then `due_at = max(due_at, today)`.

### sequences, sequence_steps
Reusable task bundles ("New Seller Prep", "Buyer Under Contract",
"Pre-Close", "Post-Close", plus nurture cadences).

- `sequences`: `id`, `name`, `trigger` (text — e.g. `deal_created_listing`,
  `settlement_date_set`, `deal_closed`, `manual`), `is_active`
- `sequence_steps`: `sequence_id`, `order`, `title`, `task_type`,
  `anchor` (`sequence_start` | `appointment_date` | `list_date` |
  `settlement_date` | `closing_date`), `offset_days`,
  `message_template_id` (null)

### appointments
- `id`, `person_id`, `deal_id` (null)
- `title`, `description`, `location`
- `starts_at`, `ends_at`, `timezone`, `all_day` bool
- `type` (enum), `outcome` (enum, default `none`)
- `rsvp_status` (enum, null) — synced from Google
- `google_event_id`, `google_calendar_id`
- `send_invite` bool
- `reminder_text` text — the pre-drafted copy/paste reminder
- `created_at`, `updated_at`, `created_by`
- On create with `send_invite` + person has email → Google event with the
  person as attendee, `sendUpdates: all`. A `The Friedman Team · 443-789-3101
  · friedmanreteam.com` line is appended to `description` automatically.
- `outcome = no_show` → auto follow-up task + nurture bump.
  `outcome = met` on `listing_appt` → prompt stage move / presentation.

### deals
- `id`, `person_id` (primary contact), `type` (enum), `name`
- `stage` (enum — listing or buyer set), `stage_entered_at`
- **property:** `property_address`, `city`, `state`, `zip`, `mls_number`
- **money:** `original_list_price`, `list_price`, `current_price`,
  `contract_price`, `sale_price`, `loan_payoff`, `concessions`,
  `commission_rate`, `commission_amount`, `est_net_proceeds`
- **dates:** `signed_date`, `list_date` *(DOM anchors here, not signed_date)*,
  `contract_date`, `settlement_date`, `actual_close_date`
- **parties:** `lender`, `title_company`, `other_agent`, `other_agent_brokerage`
- `source_presentation_id` (null)
- `nurture_pause_snapshot` jsonb — what got paused, so nothing wrongly resumes
- `created_at`, `updated_at`, `created_by`

### deal_contacts
- `deal_id`, `person_id`, `role` (`seller`|`co_seller`|`buyer`|`co_buyer`)

### deal_milestones
- `id`, `deal_id`, `type` (milestone_type), `due_date`, `completed` bool,
  `completed_at`
- Each can spawn tasks via a template; each is an anchor for `tasks`.

### message_templates
- `id`, `name`, `channel` (`email`|`text`), `category`
- `subject` (email only), `body` — merge tokens `{{first_name}}`,
  `{{property_address}}`, `{{appt_time}}`, `{{appt_type}}`, `{{net_proceeds}}`, …
- `is_active`, `created_at`, `updated_at`

### email_messages
- `id`, `person_id` (null — matched by from/to), `deal_id` (null)
- `direction`, `provider_message_id`, `thread_id`, `in_reply_to`
- `from_email`, `to_email`, `cc`, `subject`, `body_text`, `body_html`
- `sent_at`, `received_at`
- `status` (`queued`|`sent`|`delivered`|`bounced`|`opened`|`failed`)
- `template_id` (null), `sequence_step_id` (null)
- Every row also produces an `activities` row (`type='email'`).

### saved_views  *(smart lists + kanban configs)*
- `id`, `name`, `owner_id`, `entity` (`people`|`deals`|`tasks`)
- `filter` jsonb — `[{field, op, value}]`
- `sort` jsonb, `group_by` text (null), `is_pinned` bool, `color`
- A kanban board is just a saved_view with `group_by` set.

### lead_sources
- `id`, `name`, `category` (`portal`|`referral`|`sphere`|`organic`|`paid`|
  `event`|`other`), `cost_monthly` (null — for ROI)
- `parse_config` jsonb — inbound address / from-pattern → this source, plus
  field-extraction hints for the lead parser

### inbound_leads  *(raw intake log)*
- `id`, `received_at`, `raw_from`, `raw_subject`, `raw_body`, `parsed` jsonb
- `source_id` (null), `person_id` (null — set after create/merge)
- `status` (`parsed`|`needs_review`|`merged`|`created`|`ignored`)
- `dedupe_match_person_id` (null)

### presentations
- `id`, `deal_id` (null), `person_id`, `property_address`
- `status` (`draft`|`generated`|`sent`|`signed`)
- `target_list_price`, `suggested_range_low`, `suggested_range_high`
- `loan_payoff`, `est_net_proceeds`, `net_sheet` jsonb
- `valuations` jsonb — `[{source, value, entered_via: pdf|image|manual}]`
  (CMA, RPR RVM, Realist AVM 1, Realist AVM 2, Remine, Zestimate, Redfin)
- `comps` jsonb — `[{address, status, price, beds, baths, sqft, dom, ppsf,
  distance, is_selected}]`
- `market_stats` jsonb — parsed from the MLS stat screenshots (by-status
  activity + closed metrics within 2 mi)
- `zillow_url` text
- `source_files` jsonb — `[{kind: rpr_pdf|mls_image|avm_image, storage_path}]`
- `output_web_url`, `output_pdf_path`, `sent_at`, `opened_at`
- Uploaded files live in Supabase Storage.

### market_data  *(shared spine)*
- `id`, `week_ending` date, `scope` (`statewide` or county name)
- `median_sold_price`, `median_dom`, `avg_dom`, `months_supply`,
  `closed_sales`, `new_listings`, `pending`, `price_reductions`,
  `mortgage_rate_30yr`, `sold_to_orig_pct`
- `source_url` (the blog post), `pulled_at`
- Unique on `(week_ending, scope)`. Auto-upserted weekly from the newest
  market-report post on friedmanreteam.com; manual paste fallback.
- Read by presentations, nurture drafts, equity nudges.

### content_ideas
- `id`, `created_at`, `title`, `angle`, `theme`
- `evidence` jsonb — `[{person_id, activity_id, snippet}]`
- `status` (`new`|`queued`|`drafted`|`published`|`dismissed`)
- `source_run_id`
- "Send to blog queue" action feeds the brain's `blog-article-queue.md`.

### objections
- `id`, `person_id`, `activity_id`, `category` (enum), `verbatim`,
  `created_at` — aggregated into a report + `content_ideas`.

### queue_drafts  *(the daily follow-up queue, cached)*
- `id`, `person_id`, `generated_at`, `reason` (which rule fired),
  `channel` (`email`|`text`|`call`), `draft_subject`, `draft_body`
- `status` (`pending`|`sent`|`edited`|`dismissed`|`snoozed`)
- `snoozed_until`, `sent_activity_id`
- One row per person per day (deduped — highest-priority reason wins).

### operators / profile
- `user_id` (auth), `name`, `email`, `phone`, `google_calendar_id`
- `signature_block` text, `brand` jsonb (colors, logo url — for
  presentations + emails)
- `goals` jsonb (`annual_gci_target`, `annual_transactions_target`)
- `business_hours` jsonb, `after_hours_autoreply` text (null = off)

### audit_log  *(generic, like VendTrack)*
- `table_name`, `row_id`, `action`, `actor`, `old_data`, `new_data`, `ts`

---

## Automations (RPCs / triggers — the cascade spine)

1. **`log_activity(person, type, direction, outcome, subject, body,
   occurred_at, deal)`** — insert the activity, then update the person:
   `last_attempt_at` if outbound; `last_connected_at` + reset
   `attempt_count` to 0 if `outcome ∈ {connected, replied, met}`; increment
   `attempt_count` + `attempt_count_lifetime` if outbound and no connect;
   `last_activity_at` always.
2. **`set_lead_status(person, new_status, dead_reason)`** — update + stamp
   `stage_entered_at` + write a `stage_change` activity, then:
   - → `appt_set` on a seller: create the **presentation-prep task now**
     (booklet lead time) linked to the appointment.
   - → `active_seller` / "Listing Signed": call
     `create_deal_from_contact(person, 'listing')`.
   - → `active_buyer` / buyer-rep signed: `create_deal_from_contact(person,
     'buyer')`.
   - → `dead`: require `dead_reason`; if `do_not_contact`, set the
     `do_not_*` flags; cancel open tasks + pending queue drafts; drop from
     sequences.
   - → `past_client`: ensure in the sphere/equity pool.
3. **`create_deal_from_contact(person, type)`** — create the deal, copy
   address / price / contacts from the person (+ latest presentation if
   listing), set stage (`signed` / `agreement_signed`), instantiate the
   matching prep sequence, **pause nurture** (snapshot), link back on the
   contact card.
4. **`set_deal_stage(deal, new_stage)`**
   - → `active` (listing): stamp `list_date` if null (DOM anchor);
     instantiate active-listing tasks.
   - → `under_contract`: stamp `contract_date`; prompt for milestone dates.
   - → `closed`: stamp `actual_close_date`; instantiate the **post-close
     sequence** anchored to close date (review request +5 days, then 30 /
     90 / 365); move primary + co-contacts to `past_client`; add to SOI +
     equity pool.
   - → `fell_through`: cancel *incomplete* pre-close tasks; if the gift task
     was already done, surface "you already ordered a gift for this one";
     move the contact back to a sane status.
5. **`set_settlement_date(deal, date)`** — instantiate the **pre-close prep
   sequence** anchored to the settlement date: gift order at
   `max(today, settlement − 10d)`, walkthrough scheduling, "what to expect"
   client message, closing-day photo/post, prep (don't send) the review
   request, calendar the settlement.
6. **`reschedule_anchor(anchor_type, anchor_id, new_date)`** — recompute
   `due_at` for `status='open'` anchored tasks only; clamp negative offsets
   to `>= today`.
7. **`instantiate_sequence(sequence_id, context)`** — create tasks from
   steps with computed dates.
8. **`add_to_phone(person)`** — build a vCard (later: Google Contacts API
   `createContact`) with `Company = FRIEDMAN CRM · <label>`; set
   `synced_to_phone`.
9. **`parse_inbound_lead(raw_email)`** *(webhook, event-driven — not a
   poll)* — parse, dedupe on phone/email, create or merge the person, set
   source, log an activity, generate the speed-to-lead draft (or auto-send
   the after-hours first-touch if `after_hours_autoreply` is set and it's
   outside business hours).
10. **`generate_presentation(deal/person, files, fields)`** — AI reads the
    uploaded RPR PDF + pasted MLS-stat images + pasted AVM images →
    structured comps / valuations / market stats → Kyle reviews & edits →
    on confirm, render the branded web page + PDF, store, attach, set
    status.

### Cron jobs
- `sync_google_calendar` — pull changed events, push local changes,
  reconcile RSVP (webhook + periodic sync-token catch-up; renew the push
  channel before it expires).
- `pull_market_data` — weekly: fetch the newest market-report post, parse,
  upsert `market_data`.
- `run_followup_queue` — daily AM: evaluate rules
  (`next_action_at` hit · no `last_connected_at` in 30/90d ·
  birthday/home-anniversary · life-event flags — **not** a market-report
  blast), dedupe to one `queue_draft` per person, generate the AI draft.
- `run_blog_idea_miner` — weekly: scan activities since the watermark,
  cluster themes, insert `content_ideas`.
- `send_scheduled_emails` — the auto pre-appointment email reminder, any
  sequence email steps.

---

## Screen list

1. **Today** — the morning screen.
   - Follow-up queue: each card = person + reason + AI-drafted message;
     actions Approve / Edit / Send / Call / Snooze.
   - Tasks due today, overdue count.
   - Today's appointments + one-tap "confirm" (copy reminder text) and
     RSVP status.
   - Contract deadlines this week (from `deal_milestones`).
   - "Leads gone cold" count → link to that smart list.
   - Goal pace bar (transactions / GCI vs target).
   - New leads awaiting first touch.

2. **People** — the main list.
   - Table view / Kanban view (grouped by any axis via a saved view:
     lead status, attempt count, temperature, source, type).
   - Left rail: pinned smart lists (New Leads, Hot, No-connect 30d,
     Sellers, Buyers, Sphere, Past Clients, By Source, By Attempt…).
   - Filter bar, full-text search (name / phone / email / address).
   - Bulk: tag, set status, add to sequence, add-to-phone, export.

3. **Person detail**
   - Header: name, status, temperature, type, tags; quick actions
     Call (`tel:`) / Text (copy or `sms:`) / Email / Log / Add to iPhone.
   - Tabs/panels: **Timeline** (all activities, filterable) · **Tasks** ·
     **Appointments** · **Deals** · **Notes** · **Details** (every field,
     editable) · **Files** · **Referrals** (referred by / referred).
   - AI **meeting-prep brief** (one paragraph: last contact, what they
     want, the sticking point, sensitivities).
   - "Log call / text / email" quick forms (feed `log_activity`).

4. **Deals** — pipeline board.
   - Columns = deal stages; toggle Listing / Buyer (or combined).
   - Card: address, price, contact, days in stage, next milestone, health
     flag (past its area's median DOM).
   - List view with the same filters.

5. **Deal detail**
   - Property info, contacts + roles, stage, key dates.
   - **Transaction timeline** — milestones with dates + their tasks;
     editing a date recomputes tasks.
   - Net sheet, linked presentation, tasks, activity, files (contract,
     disclosures), other-party info.

6. **Calendar / Appointments**
   - Week / month view synced with Google.
   - Create-appointment modal: title, time, type, guest(s), location,
     **Send calendar invite** toggle, reminder-text field, copy button.
   - Outcome logging (met / no-show / rescheduled…).

7. **Tasks** — all tasks; filters (today / overdue / this week, by type, by
   deal, anchored vs manual); quick complete.

8. **Templates** — email + text templates by category; merge-token helper;
   live preview against a sample contact.

9. **Sequences** — the prep / post-close / nurture bundles: steps, anchors,
   offsets, attached templates. Mostly set-once.

10. **Listing Presentation Builder**
    - Guided form: property address · upload RPR PDF · paste MLS stat
      screenshot(s) · paste AVM screenshots (Remine, Realist ×2,
      Zestimate/Redfin) · Zillow URL · target list price · loan payoff.
    - Review step: extracted comps / valuations / market stats in editable
      tables (with the AI's confidence flags).
    - Generate → preview the branded web page + PDF → Send to seller /
      Mark signed (mark-signed fires `create_deal_from_contact`).
    - Standalone **Net Sheet** mode (Maryland closing costs + county
      transfer/recordation tax).

11. **Content Ideas** — miner output with evidence; status
    (new / queued / dismissed); "send to blog queue". Tab: **Objection
    report** (categorized, with verbatims and counts).

12. **Reports**
    - Source ROI (which sources close, cost per closing).
    - Conversion funnel by status; average days in each stage.
    - Activity (calls / texts / emails / appts per week).
    - Pipeline value, goal pace.
    - "Who am I losing" (sphere + past clients, no connect 90/180d, ranked).
    - Equity-nudge candidates (home anniversary + area movement).

13. **Settings**
    - Profile, signature, brand (logo + colors for presentations/emails).
    - Goals; business hours; after-hours auto-reply (on/off + text).
    - Lead sources + monthly cost + parse config.
    - Connections: Google (Calendar now, Contacts later), email sending
      domain.
    - **Import / Migration** tool: FUB CSV upload → column-map → dedupe →
      dry-run preview → commit.

14. **Login** — Supabase email + password.

*(Optional, may fold into panels rather than their own screens: "Ask the
CRM" natural-language search; the AI meeting-prep brief.)*

---

## Build phases

### Phase 1 — by Oct 31 (cut over, cancel FUB)
Auth · People (list + kanban + saved views) · Person detail + timeline +
`log_activity` · Tasks + date-anchored recompute · Calendar with **2-way
Google sync** + client invites · Templates · Deals + full forward/back
cascade + transaction timeline + pre/post-close sequences ·
Add-to-iPhone (vCard) · Import/Migration · **Today** screen (tasks + appts +
rule-based follow-ups, no AI draft yet) · Settings · Email **sending**
(Resend) + logging + inbound parse for your top 1–2 lead sources ·
market_data table (manual paste ok to start).

### Phase 2 — November
AI follow-up queue with drafts · speed-to-lead auto-draft + after-hours ·
Listing Presentation Builder (RPR/image ingestion + generate) · Net Sheet ·
market_data auto-pull · "Ask the CRM" · meeting-prep briefs · email reply
capture.

### Phase 3 — later
Content-idea miner + objection tracker · equity-nudge engine · "who am I
losing" · full Reports/ROI · Google Contacts API upgrade (silent sync) ·
review-request tracking · goal pace · deal file management ·
*(optional)* Twilio texting · *(optional)* native iOS Call Directory app
for true caller-ID on unsaved numbers.

---

## Infrastructure

- **Supabase** — Postgres + Auth + Storage (presentation files, email
  attachments). Free tier to start; Pro ($25/mo) if rows/storage grow.
- **Vercel** — Pro ($20/mo, commercial) or Netlify free.
- **Google Cloud project** — OAuth for Calendar API (Contacts API in
  Phase 3). Calendar push needs a public webhook + a channel-renewal cron.
- **Email** — Resend or Postmark for sending; requires SPF/DKIM/DMARC on a
  `friedmanreteam.com` subdomain (e.g. `mail.friedmanreteam.com`). Inbound
  lead parsing via Resend inbound or Cloudflare Email Routing → webhook.
- **Cron** — Supabase `pg_cron` or Vercel Cron.
- **AI** — Claude API for drafts, PDF/image extraction (vision), theme
  clustering, NL search, briefs. Small per-use cost at a solo agent's
  volume (~$5–30/mo).
- **Running cost:** ~$0–70/mo depending on how many paid tiers you need —
  at or below FUB, and it never scales per seat.

---

## Mojo Dialer connection — DEFERRED (decided 2026-09-09)

Mojo's public API is **push-in only** (how Vulcan7/Redx/Landvoice feed it).
There is **no free way to pull data out of Mojo or webhook on "marked Lead"**
— outbound sync is Zapier or API Nation by design, both paid.

Current lead flow: Kyle dials expireds in Mojo, marks keepers as **Lead**,
FUB pulls them via Mojo's native FUB integration.

Options for the new CRM, when we get to it:
- **Browser extension (free, instant):** a Chrome extension on the Mojo tab
  that posts a contact to the CRM webhook when Kyle marks it Lead (reads
  Mojo's internal data calls, not DOM scraping). Custom, can break on a
  Mojo redesign, runs only on his laptop.
- **Zapier free tier:** 100 automations/mo, ~15-min delay, "contact added
  to a group" trigger. Works only if keeper volume stays under ~3/day.
- **API Nation ~$5/mo** or **Zapier paid ~$20/mo** — supported, reliable.

**For now:** the Phase-1 CSV import/migration tool covers it — export the
Mojo "Lead" group and import. Revisit the auto-connect (likely the browser
extension) after the core CRM is running.

Free bonus the other direction: Mojo's push-in API lets the CRM *load*
calling lists into Mojo (website leads, a sphere segment) at no cost.

## Open decisions (need Kyle)

**Blocking the schema — need before build starts:**
1. Final **lead_status** list — confirm/adjust vs your Podio stages.
2. Final **dead_reason** list.
3. **Deal boards:** one combined board, or separate Listing / Buyer?

**Can come during the build:**
4. Which **lead sources** feed you now (Mojo expireds, website — anything
   else?) — determines the Phase-1 parsers.
5. **Email sending:** from `kyle@friedmanreteam.com` (keeps replies in your
   Gmail; needs Gmail API) or a `mail.friedmanreteam.com` subdomain via
   Resend?
6. **After-hours:** auto-send a first-touch, or wait for you? *(Phase 2)*
7. **Presentation output:** web page + PDF both, or one? Printed booklet —
   manual order with the PDF, or integrate a print API? *(Phase 2)*
8. Your **annual GCI + transaction targets** for the pace tracker. *(Phase 3)*

**Resolved:**
- FUB export (8,486 contacts, 81 cols) **includes** Birthday, Closing
  Anniversary, tags, stage, source, 5 phones, spouse/co-contact, property
  fields, and Deal Stage/Close Date/Price. Granular call/text/email
  timeline does **not** export — new activity starts fresh; pull history
  for ~50–100 active contacts via the FUB API pre-cutover if wanted.
