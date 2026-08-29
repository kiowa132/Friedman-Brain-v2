# properties/

One folder per property Kyle is working. Convention:

```
properties/
  8303-bellona/           <- kebab-case street + short name
    photos/               <- Kyle drops raw listing photos here (jpg/png)
    generated/            <- pipeline output (gitignored — regenerate anytime)
    notes.md              <- optional: address, quirks, which photos are which
```

**Workflow:** Kyle drops photos into `photos/`, names the report he wants,
and the pipeline (`scripts/gen-image.ps1` + the templates in
`../projects/report-images.md`) generates images into `generated/` and
wires them into the report.
