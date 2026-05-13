# Job Scanner

Scrapes target companies' public careers pages, applies the strategy doc's hard filters (title keyword, location, recency), and writes a flat snapshot to `outputs/scanner/`. Collect-only by design. No scoring or ranking. Screening (per `screening_criteria.md`) is applied later by a human reviewer reading the snapshot.

## Install

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium
```

## Run

```
python job_scanner.py
```

Outputs `outputs/scanner/jobs_YYYY-MM-DD.md` and `outputs/scanner/jobs_YYYY-MM-DD.json`. Prints a one-line summary.

Flags:

- `--config PATH` — path to companies JSON (default: `target_companies.json`)
- `--out DIR` — output directory (default: `outputs/scanner/`)

## Hard filters (the only mechanical gates)

1. **Title keyword match.** Title must contain at least one of: product, head of product, vp product, chief product, cpo, strategy, strategic initiatives, chief strategy, cso, operations, ops, operating officer, coo, chief operating, transformation, business transformation, digital transformation, innovation, chief innovation, platform, technical platform, platform engineering, program management, program manager, project management, pmo, project management office, process excellence, process improvement, business process, continuous improvement, lean, delivery, director of delivery, head of delivery, implementation, head of implementation, general manager, gm, head of business, business head, chief of staff. AND must NOT contain: engineer, engineering manager, tech lead, technical lead, architect, developer, designer, scientist.
2. **Location match.** Remote, Philly, NYC, Seattle, SF Bay, LA, Portugal, Spain. Unknown location passes through (Workday/HTML often have no location metadata).
3. **Posted within last 7 days.** If `posted_date` is unknown (common for Workday/HTML), the role passes through and the snapshot shows `unknown`.

Anything else (comp, visa, function-fit nuance, IC scope, broken-to-fix language, tier label) is a screening input handled by judgment, not by the scanner.

## Adding companies

Edit `target_companies.json`. Each entry needs:

- `name` — display name
- `ats` — one of `greenhouse`, `lever`, `ashby`, `smartrecruiters`, `workday`, `html`
- For `greenhouse` / `lever` / `ashby` / `smartrecruiters`: `slug` is the company identifier in the board URL. Examples:
  - `boards.greenhouse.io/stripe` → slug `stripe`
  - `jobs.lever.co/plaid` → slug `plaid`
  - `jobs.ashbyhq.com/ramp` → slug `ramp`
  - `jobs.smartrecruiters.com/Gusto` → slug `Gusto` (case matters)
- For `workday` / `html`: `url` is the full listing page URL.

If a company fails to scrape, check the ATS assignment. Many companies change providers; verify by visiting the careers page and checking the URL host.

## Cache

Responses are cached to `.cache/` for 6 hours. Delete the directory to force a fresh fetch.

## Output schema

Each row has: Company, Title, Location, Posted, Source ATS, Apply Link. Sorted by company name, ascending. JSON output also includes scan totals (companies scraped, total postings found, matched after filters).

## Known limits

- Workday and generic HTML pages don't expose posted dates reliably; those roles pass the 7-day filter with `posted_date: unknown`.
- Workday and HTML JD fetches are capped at 30 postings per company to keep run time bounded.
- LinkedIn is intentionally not supported (use the `daily-job-alert-scan` scheduled task in Cowork for LinkedIn alert email collection).
