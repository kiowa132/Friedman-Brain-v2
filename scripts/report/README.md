# Weekly Friedman Report generators (saved 2026-09-20)

Reusable build kit from the Sept 14-20 edition. Copy the week's numbers into `week_data.py` once and everything else derives from it, so text, tables, and channels can't drift.

Order (see `projects/friedman-report.md` for the full procedure):
1. `week_data.py`: type the week's Bright MLS numbers (CT county tuples, ST statewide, LAST, PREV, TREND). Run `verify.py` to print every derived number (% changes, ratios, payment math, fastest/slowest counties) and check the narrative against it.
2. `report-core.template.md` + `gen_core.py`: narrative template with `{{TABLE}}` placeholders. The story, FMMI scores, Signal, spotlights, and recipe are written fresh each week; the tables are generated. Output is `drafts/friedman-report/<week>/report-core.md`. Has a dash guard.
3. `scripts/pdf/friedman-report-pdf.py`: renders report-core.md to the PDF review draft. Update the WEEK block (headline, tiles, FMMI, chart series). Chart series use ONLY verified weeks (see the rule in friedman-report.md).
4. `substack_html.py`: turns `substack.md` into the paste-ready `substack-formatted.html`.
5. `web.template.md` + `gen_web.py`: builds the website SEO article (`website-seo.md`) from the template, pulling tables, spotlights, heat map, supply, recipe, and story out of report-core.md. Includes the FMMI label and sub-score alt text the homepage gauge needs.
6. `h169.py` + `comp169.py`: hero helper. Removes baked text from a wide banner, stretches sky and lawn to 16:9, then re-composites the text. Only needed when the source is a 3:1 banner; the site needs 16:9.

These scripts hardcode Windows paths to the scratchpad and the Sept 14-20 folder. Change the paths at the top of each before running. Nothing here publishes anything.
