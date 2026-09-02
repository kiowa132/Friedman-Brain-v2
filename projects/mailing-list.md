# Mailing List + Freebie Funnel

Kyle's stay-in-touch system: physical mail (Baltimore sports schedule magnets +
a monthly "3% Smarter" trivia card) plus a monthly market-update email. The
freebies are the hook to grow the list.

## Signup page (live on the website)
`friedmanreteam.com/mailing-list` — `src/pages/MailingListPage.tsx`.
- Fields: name, email, phone (optional), **full mailing address** (needed to
  send the magnets/cards), and checkboxes for which freebies they want.
- Submits through the existing lead pipeline (`src/lib/leads.ts` →
  `api/leads.js` → Follow Up Boss `/v1/events`).
- Extended the pipeline: it now also forwards a structured `addresses` entry
  and `tags` to the FUB person. Event `type` "Mailing List" is sent to FUB as
  "Registration" (FUB only allows fixed event types); segmentation is by tag.

## Pulling the mail-merge list out of Follow Up Boss
Filter FUB people by tag:
- `Mailing List` — everyone who signed up
- `Baltimore Football Schedule` / `Baltimore Baseball Schedule` — who wants which magnet
- `Monthly Card` — who gets the monthly AM card
Export those with the address field → mail merge / print vendor.

## Trademark note
Never use "Ravens" / "Orioles" or team logos on the site or the print pieces.
Use "Baltimore Football / Baseball Schedule" + the disclaimer "Team names are
the trademarks of their respective owners, who do not sponsor or endorse this."
(matches how the physical magnets are already worded).

## The print pieces (Kyle's existing assets, Aug 2026)
- Baltimore football schedule magnet — QR currently → home valuation; footer
  QR → "team trivia"
- Baltimore baseball schedule magnet — same QR treatment
- "AM Card" / "This Card Makes You 3% Smarter" — monthly card: this-day-in-
  history, life hack, astonishing fact, riddle, a quote
- The IG promo for the list uses headline "RELATIONSHIPS OVER ALGORITHMS."
  (see the image-prompt work, Sept 2026)

## Ideas / next
- Point the QR codes on future magnet reprints at `/mailing-list` instead of
  (or alongside) the valuation page, so the schedule itself grows the list.
- Add a promo block for `/mailing-list` on the homepage and blog post footer.
- Auto-tag by county / neighborhood from the address for targeted mailings.
