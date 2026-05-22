# Maintenance

Workflow for maintaining operational state — pipeline transitions, status updates, weekly hygiene, sender-domain mappings, periodic system audit.

The skill that keeps the operational state (pipeline files, status snapshots) clean and current.

---

## Inclusion test

> **PASSES IF:** workflow for maintaining operational state — pipeline transitions (candidates → applications; active → archive); funnel status definitions; status check processing (parse `outputs/applications/status_check_*.md` → update applications pipeline file); weekly hygiene checklist; pivot triggers; sender-domain mappings for ATS notifications; daily review procedure.
>
> **FAILS IF:** personal data (→ `me/`); other skills' workflows (sourcing / screening / tailoring / outreach / interviewing / profiling / composing); the operational state files themselves (→ pipeline files); facts about Maz (→ `me/background.md`); JD bodies (→ `outputs/jds/`); cross-cutting authoring rules (→ `discipline.md`).

---

## Inputs

- Pipeline state files (candidates pool, applications, outreach log, archive, weekly metrics)
- `outputs/applications/status_check_*.md` (daily status check snapshots)
- Sender-domain mappings (ATS notification senders per company)
- Pivot triggers (cycle-level signals)

## Outputs

- Updated pipeline state files
- Audit reports

---

## Funnel status definitions

A submitted application moves through these states. Maintenance owns the transition rules.

- `submitted` — ATS submission confirmed (and ideally three-touch executed: ATS + HM DM + referral hunt).
- `recruiter-screen` — recruiter has reached out for first screening conversation.
- `phone-screen` — initial phone or video screen with recruiter or HM.
- `hm-conversation` — substantive conversation with hiring manager (beyond initial screen).
- `interview-loop` — formal interview process underway (multiple stakeholders).
- `onsite-loop` — final-stage interview loop (in-person or extended virtual).
- `offer` — written offer extended.
- `rejected-by-employer` — formal rejection received.
- `withdrawn` — Maz pulled out.
- `ghosted` — no response 25+ days post-submit, no rejection email; effectively dead.

Funnel-end states (`offer`, `rejected-by-employer`, `withdrawn`, `ghosted`) stay in the applications file as funnel record. They do not move to archive (archive is for candidates that never got submitted).

---

## Pre-application state definitions (candidates pool)

- `on-deck` — scored 4-5, in queue to tailor and submit.
- `screened` — scored, awaiting decision on whether to pursue.
- `archive-review` — scored 2, holding for re-review.

Archive states (for non-submitted, closed-out rows):
- `rejected` — failed sourcing in-zone filter, or screening dropped to 1.
- `stale` — posting closed before Maz applied.

---

## Pipeline transition rules

| From | To | Trigger |
|---|---|---|
| Sourcing in-zone filter pass | candidates pool (`on-deck` or `screened`) | Sourcing pass + initial score |
| candidates `screened` 4-5 | applications `submitted` | User decides to apply + tailor complete + submission confirmed |
| candidates 1-2 | archive `rejected` | Score finalized |
| candidates `stale` (posting closed before apply) | archive `stale` | Posting close detected |
| applications `submitted` | applications `recruiter-screen` | Recruiter reaches out (detected via status check) |
| applications `recruiter-screen` | applications `phone-screen` | Phone screen scheduled or held |
| ... etc through funnel | | |
| applications any-state | applications `rejected-by-employer` | Rejection email |
| applications any-state | applications `ghosted` | 25+ days no response, no rejection |
| applications any-state | applications `withdrawn` | Maz pulls out |

**Transition rule:** a row moves between files (sourcing → applications; either → archive). No duplication across files.

---

## Status check processing workflow

Daily scheduled task (`daily-application-status-check`, runs 5:30 AM + 1:30 PM ET) writes a snapshot to `outputs/applications/status_check_YYYY-MM-DD-HH.md`. This snapshot lists potential transitions detected from Fastmail (rejection emails, recruiter outreach, HM scheduling).

Workflow per snapshot:

1. Read the snapshot file.
2. For each potential transition flagged:
   - Verify the email content (rejection vs. interview invite vs. scheduling).
   - Match to the application in the applications pipeline file (by company, role, job ID, or applicant ID).
   - Apply the transition rule.
   - Update applications row with new funnel status + last status update date + next action.
3. Surface anything ambiguous to user (e.g., recruiter email that's neither rejection nor interview invite).
4. Don't auto-update unless the transition is unambiguous.

---

## Sender-domain mappings (ATS notification senders per company)

ATS systems send notifications from third-party domains, not the company's own domain. Maintain a discovered mapping list so status checks can match emails to applications correctly.

Common ATS sender patterns:
- `*@myworkday.com` — Workday
- `*@greenhouse-mail.io` — Greenhouse
- `*@ashbyhq.com` — Ashby
- `*@lever.co` — Lever
- `*@smartrecruiters.com` — SmartRecruiters
- `*@workable.com`, `*@candidates.workablemail.com` — Workable

Discovered company-specific mappings (extend as observed):
- Mastercard → `mastercard@myworkday.com`

For each application: search profile includes both `*@<company-domain>` AND known ATS sender patterns matching the company's posting source.

---

## Weekly hygiene checklist

Run weekly (or on-demand). Update `weekly-metrics.md` (or its successor).

1. **Counts:** applications submitted this week + cumulative; rejections received; active applications; HM outreach sent; LinkedIn connection accepts; recruiter screens; HM conversations; onsite/loops; offers.
2. **Three-touch completion check** for each app submitted this week. Flag gaps (ATS-only submissions where HM DM + referral hunt weren't done).
3. **Stale watch:** flag applications submitted 21+ days ago with no response → consider moving to `ghosted`.
4. **Outreach follow-up watch:** flag connection accepts 5-7 days old with no DM follow-up.
5. **Pipeline pivot check:** apply pivot triggers (below).

---

## Pivot triggers

Cycle-level signals that the strategy isn't working and needs reassessment.

- **3-week mark with zero recruiter screens:** audit funnel — resume, outreach, or targeting? Consider adjusting alert keywords and target tiers; consider LinkedIn profile overhaul.
- **7-week mark with no offers / final rounds:** deeper reassessment. Possibly bring in recruiter relationships directly.

When a pivot trigger fires, surface to user with diagnostic data (current counts vs. expected; conversion rates per funnel stage; which apps stalled where).

---

## System audit (periodic)

Run on user request or post-rebuild. For each pipeline file, check:
- Row counts match expected (no orphans, no duplicates across files).
- Status definitions used correctly.
- Sender-domain mappings updated when new ones surface.
- Stale-watch and three-touch-completion gaps surfaced.
- Cross-references between files resolve (e.g., outreach.md row references valid applications.md row).

---

## Open / parked items

- Pipeline file format and placement TBD — current archived versions use mixed formats (candidates.json vs applications.md vs outreach.md vs archive.json vs weekly-metrics.md). New rebuild needs a single coherent format decision. See `pending.md`.
