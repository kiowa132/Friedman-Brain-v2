# properties/

One folder per property Kyle is working. Convention:

```
properties/
  8303-bellona/           <- kebab-case street + short name
    photos/               <- Kyle drops raw listing photos here (jpg/png)
    generated/            <- all AI image attempts — GITIGNORED scratch
    final/                <- only images that shipped, compressed jpg — COMMITTED
    image-log.md          <- auto-written: what prompt made each final
    notes.md              <- optional: address, quirks, which photos are which
```

**Workflow:**
1. Kyle drops photos into `photos/`, names the report he wants
2. `scripts/gen-image.ps1` generates candidates into `generated/` (scratch)
3. Kyle picks the keeper → `scripts/keep-image.ps1` compresses it into
   `final/` (~300 KB jpg) and logs the prompt in `image-log.md`
4. `generated/` can be wiped anytime; `final/` + `image-log.md` are the
   permanent record

Blog images skip this — they go straight to
`The-friedman-team-website/public/images/uploads/` and commit in that repo.
