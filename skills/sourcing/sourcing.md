# Sourcing

The skill that takes raw external job postings (from any channel) and produces a pool of JDs that are in Maz's career zone — using `me/constraints.md` as the filter.

Answers ONE question: **should I consider this kind of job?** (Yes → in-zone pool. No → rejected, archived.)

Does NOT evaluate fit, chances, or rank in-zone candidates. That's `skills/screening/`.

---

## Inclusion test

> **PASSES IF:** channel definition, collection procedure, or in-zone filter logic that turns external job postings into a pool of in-zone JDs (using `me/constraints.md`).
>
> **FAILS IF:** Maz's career-zone parameters themselves (→ `me/constraints.md`); evaluation of fit/chances for in-zone JDs (→ `skills/screening/`); per-JD tailoring decisions (→ `skills/tailoring/`); outreach drafts (→ `skills/outreach/`); interview prep (→ `skills/interviewing/`); operational state (→ pipeline files); fact about Maz (→ `me/background.md`).

---

## Inputs

- `me/constraints.md` (career-zone filter)
- Raw output from each channel (see below)

## Outputs

- Per-channel raw collection files in `outputs/<channel>/`
- In-zone pool entry (logged to pipeline file — see pipeline section in CLAUDE.md routing)
- Out-of-zone rejection logged to archive

---

## Channels

### 1. LinkedIn alerts
- LinkedIn sends alert emails to `mmavvaj@gmail.com`. Fastmail IMAP-fetches from Gmail (re-enabled 2026-04-25 after Fastmail's auto-disable in early April).
- Scheduled task (Cowork): `daily-job-alert-scan`, runs 5:00 AM ET daily.
- Senders scanned: `jobs-listings@linkedin.com`, `jobalerts-noreply@linkedin.com`, `jobs-noreply@linkedin.com`.
- Folder search spans ALL Fastmail folders (Fastmail sieve filter routes List-Unsubscribe emails including LinkedIn to `Ignore` folder; `search_emails` MCP tool spans all folders).
- Output: `outputs/linkedin/linkedin_alerts_YYYY-MM-DD.md` (snapshot of postings extracted from that day's alerts).
- Volume scales by adding more LinkedIn alert keywords/metros, not by expanding any single alert (the "See all jobs" link requires auth and can't be scraped).
- 16 active alerts as of 2026-05-04 across keywords (director product, head of product, director PMO, payments-specific) and metros (US Remote, NYC, SF Bay, Seattle, Philly).

### 2. Python scanner (currently archived — was a channel)
- Script `job_scanner.py` archived in `_archive/2026-05-20-rebuild/`.
- Scraped 108 target companies' careers pages via ATS APIs (Greenhouse, Lever, Ashby, SmartRecruiters JSON endpoints) and HTML (Workday + generic).
- Hard filters: title-keyword match (Product / Strategy / Operations / Transformation / Innovation / Platform / PMO / Process / Delivery / GM / Chief of Staff families), location (Remote / Philly / NYC / Seattle / SF Bay / LA / Portugal / Spain), posted within last 7 days. Unknown location/date passes through.
- Cache: 6-hour HTTP response cache (was in `.cache/`).
- Output: `outputs/scanner/jobs_YYYY-MM-DD.md` + `.json` (one snapshot per run).
- **Status:** archived. Reactivation requires resetting up the venv + scheduled run. Listed here as a channel that can be re-enabled.

### 3. Manual paste
- User pastes a JD URL or full text in chat.
- Workflow: fetch canonical body from company ATS (preferred over LinkedIn body — LinkedIn truncates), save to `outputs/jds/YYYY-MM-DD-<co-shorthand>-<role-shorthand>.md` with header (URL, company, title, location, fetched_at, posting_status).
- ATS preferred sources: Greenhouse / Lever / Ashby / Workday / SmartRecruiters / Workable / company careers page.
- Sender-domain note for ATS notifications: third-party domains (`*@myworkday.com`, `*@greenhouse-mail.io`, `*@ashbyhq.com`, `*@lever.co`, `*@smartrecruiters.com`, `*@workable.com`, `*@candidates.workablemail.com`).

### 4. Recruiter inbound
- Recruiter emails Maz directly (or DMs on LinkedIn) about a specific role.
- User forwards the email to chat, or pastes the LinkedIn message.
- Same workflow as manual paste: extract JD details, fetch canonical body if available, save to `outputs/jds/`.
- Flag as `source: recruiter-inbound` so screening can weight warm-path differently (recruiter-fronted roles often hide the actual employer).

### 5. Direct browsing
- User finds a JD via web browsing (e.g., on a company's careers page) and pastes URL/text.
- Variant of #3 (manual paste). Treat identically.

---

## In-zone filter workflow

For every JD collected from any channel, apply `me/constraints.md` as the filter. The constraint values themselves (title families, knockout lists, comp floor, locations, etc.) live in `me/constraints.md` — this file references that file for the values; it does not duplicate them.

The JD is in-zone if and only if ALL of these checks pass against `me/constraints.md`:

1. **Title match** — title contains an acceptable seniority prefix AND an acceptable functional family. *(Lists in `me/constraints.md` § Wanted role titles.)*
2. **Altitude floor** — at or above the role-specific floor. *(In `me/constraints.md` § Wanted role titles § Altitude floor.)*
3. **Function NOT in knock-out list.** *(In `me/constraints.md` § Function knock-outs.)*
4. **Domain NOT in knock-out list.** *(In `me/constraints.md` § Domain knock-outs.)*
5. **Comp NOT entirely below floor.** If listed range is fully below the floor → out of zone. Straddles or unlisted → in-zone (verify at apply). *(Floor in `me/constraints.md` § Compensation.)*
6. **Location in acceptable set.** *(In `me/constraints.md` § Locations.)*
7. **Direct-reports clause not hard-no.** *(Rule in `me/constraints.md` § Direct-reports clause.)*
8. **Posting state.** Must be open; posted within recency window. *(In `me/constraints.md` § Posting state.)*
9. **Recruiter-Boolean credentials.** If JD hard-requires any credential Maz doesn't carry → out of zone. *(List in `me/voice.md` § Recruiter-Boolean filters, referenced by `me/constraints.md`.)*

**ALL must pass.** Any single failure → out of zone, JD goes to archive.

If any constraint value seems wrong or out of date, fix it in `me/constraints.md` (via `skills/profiling/`), not here. Sourcing only applies the constraints; it does not define them.

---

## Sourcing procedure (per JD)

1. Receive JD from a channel (per channel-specific intake above).
2. If channel = LinkedIn or scanner, JD is already extracted from a snapshot file. If manual paste / recruiter inbound, fetch canonical JD body and save to `outputs/jds/<date>-<co>-<role>.md`.
3. Apply in-zone filter (9 checks above).
4. If in-zone: log to pipeline file (the holding area for screening). Include source channel, JD location, link.
5. If out-of-zone: log to archive with reason (which constraint failed). Don't re-evaluate this URL if it surfaces again in another channel.
6. Sourcing's job ends here. Screening picks up the in-zone pool.

---

## Notes on channel hygiene

- **LinkedIn email delivery failure mode:** LinkedIn sends to gmail, not directly to Fastmail. Fastmail IMAP-fetches from gmail. If that pipeline breaks (as it did 2026-04-07), no LinkedIn alerts arrive. Watch for "last-seen receipt" dates per sender to detect breakage early.
- **Sieve filter routing:** Fastmail sieve filter routes List-Unsubscribe emails (including LinkedIn alerts) to `Ignore` folder. The `search_emails` MCP tool spans all folders, so this isn't a problem. If routing ever changes or alerts need to land in Inbox, add an exception above the List-Unsubscribe fallback rule.
- **Keyword altitude:** "senior product manager" alert keyword returns IC roles. Consider replacing with "director of product," "head of product," "principal product manager" for better signal-to-noise.

---

## Open / parked items

- Add more LinkedIn alerts: fintech, payments director, head of product, principal product manager, director of platform, director of transformation; metros: LA, Portugal/Lisbon.
- Research safe web-scraping paths (public ATS APIs, RSS, ToS-friendly aggregators) for richer job data beyond the email digest.
- Reactivate or replace Python scanner (currently archived).
