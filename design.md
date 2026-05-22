# Job Search System — Design Document

High-level architecture, design rationale, and history of this system. Read this first when picking up the project cold, then `CLAUDE.md` for the operational index.

---

## What this system is

A personal job search system for Maz Mavvaj. Helps Maz find his next director-level role by:
- Discovering relevant job postings (sourcing)
- Evaluating them for fit and chances (screening)
- Producing tailored resumes per job (tailoring)
- Producing outreach artifacts — cold emails, LinkedIn invites, warm DMs to hiring managers, follow-ups (outreach)
- Preparing for interviews when they land (interviewing)
- Maintaining the operational state — pipeline transitions, status updates, weekly hygiene (maintenance)
- Keeping the personal-data files (background, voice, constraints, master resume, master LinkedIn) accurate and current (profiling)
- A placeholder for cover letters / application essays (composing)

Built to be reusable as skills by anyone — Maz first, others later. Personal data is separated from system logic.

---

## Why this rebuild exists

Before the 2026-05-20 rebuild, the system was an accumulation of patches on top of patches. Symptoms included:
- The same rule (hard locks, em dash rule, agentic AI claim, Log4Shell framing) in 4-5 different files with different wordings.
- A 859-line "comprehensive" career background doc that mixed facts, voice rules, tailoring decisions, interview prep, LinkedIn content, and instructions to Claude all together.
- A validation framework with 11 gates that were rubber-stampable (no forcing function; Claude could self-attest "yes I checked" without actually checking).
- Stale references everywhere (one doc pointed at a file that had been archived; another doc duplicated content the first one was supposed to own).
- Content in the wrong files (career facts buried in interview prep notes; voice rules hiding in application notes where user caught overclaims).

These weren't bugs — they were the design failing. Patches on top of patches don't fix a structural problem; they accelerate the drift. The rebuild was a fundamental redesign.

The OLD system lives in `_archive/2026-05-20-rebuild/` as historical record (never modify; reference only).

---

## Three-layer architecture

The core insight that drove the rebuild: there are three distinct kinds of content in this system, and the OLD system was mixing them.

**1. Personal data (`me/`)** — source of truth about WHO Maz is. Stable, infrequently updated. Five files:
- `me/background.md` — facts about Maz (career, projects, numbers, education, certs)
- `me/voice.md` — rules about how Maz communicates and is represented (universal writing-style, claim/don't-claim, bridges, brand identity, hard locks)
- `me/constraints.md` — what defines Maz's career zone (comp floor, locations, wanted titles, function/domain knock-outs, recruiter-Boolean credentials)
- `me/resume.md` — master resume content in markdown (source the master `.docx` is generated from)
- `me/linkedin.md` — master LinkedIn profile content (headline, About, experience one-liners)

**2. Skills (`skills/`)** — workflows that produce artifacts from personal data + situational inputs (JD, target role, etc.). Eight skills:
- `skills/profiling/` — maintain `me/` files when new info surfaces
- `skills/sourcing/` — collect JDs from channels; filter to in-zone pool using `me/constraints.md`
- `skills/screening/` — evaluate in-zone JDs for fit and chances; score 1-5
- `skills/tailoring/` — produce tailored resume `.docx` from `me/resume.md` + JD (validation is a phase within this skill)
- `skills/outreach/` — produce DMs, emails, invites, follow-ups; three-touch model
- `skills/interviewing/` — produce per-JD interview plans; behavioral mapping; reusable answers
- `skills/maintenance/` — pipeline transitions, status check processing, weekly hygiene, sender-domain mappings
- `skills/composing/` — placeholder for cover letters and application essays (built when needed)

**3. Artifacts (outputs from skills)** — external-facing deliverables. Live in folders parallel to the skills that produce them:
- `resumes/` — master `.docx` + per-JD tailored `.docx` files
- `interviews/` — per-JD interview plans (when generated)
- `outputs/` — collected sourcing data per channel (`linkedin/`, `jds/`, `applications/`, `scanner/`)
- LinkedIn (the actual profile on linkedin.com) — synced from `me/linkedin.md` manually

Plus project-level files:
- `CLAUDE.md` — index, router, gatekeeper (loaded at session start)
- `discipline.md` — authoring rules (how files in this repo are written and extended)
- `pending.md` — deferred items, drift log, structural decisions parked, placeholder names

---

## Why the three layers stay separate

Each layer has a different lifecycle, different update cadence, different consumers.

- **Personal data changes when Maz's career evolves** (new role, new project, new credential, new preference). Update via `skills/profiling/`.
- **Skills change when the workflow itself needs to improve** (better tailoring framework, new outreach channel). Update directly; review carefully.
- **Artifacts are produced per use case** (per-JD tailored resume, per-interview prep). Don't outlive their use case.

The OLD system mixed these: the "comprehensive" comp doc had personal data, voice rules, the 10-point bullet framework, the promotion rule, instructions to Claude, and interview prep all in one file. That meant updating any one of them risked drift on the others, and the file became unmaintainable.

Three layers means three distinct update mechanisms and no cross-contamination.

---

## Inclusion tests — the discipline that keeps the layers clean

Every file in the system has its own **inclusion test** at the top — a PASSES IF / FAILS IF rule that says exactly what content belongs in this file and where misplaced content should go.

Example for `me/voice.md`:
> PASSES IF: universal writing-style rule, claim/don't-claim rule, identity/brand/belief expressed across channels, or hard-lock representation rule.
> FAILS IF: fact about Maz (→ background); channel-specific format (→ that skill); per-JD tailoring decision (→ tailoring); etc.

These tests are the gates that prevent the OLD drift problem. When new content needs a home, apply the test. When auditing a file, walk every section against the test.

The 16 files in the system each have their own test. They're hardened with explicit FAILS IF clauses so content can't claim multiple homes.

---

## Authoring discipline (`discipline.md`)

Nine rules that govern HOW any file in the repo is written and extended. These are domain-agnostic — they apply to writing voice rules, writing skill workflows, updating background, anything.

1. **Each file declares its own inclusion test at the top.**
2. **Re-derive, don't lift.** Don't copy-paste from sources; read sources, set them aside, write fresh.
3. **Read all relevant sources, not just the most convenient one.**
4. **Audit sentence-by-sentence** against the inclusion test before declaring done.
5. **The completion report is part of completion.** Report what was done, what was cut, what sources were checked.
6. **Run mechanical consistency checks before narrative analysis** (heading vs body, internal redundancy, cross-references resolve).
7. **When user feedback contradicts an authoring rule, surface the conflict** (don't silently apply).
8. **Don't trust filenames in archived or legacy source systems** — content is scattered; categorize by actual nature, not filename.
9. **Triangulate at the item level, not the file level** — for every rule/fact, find every appearance across sources, compare versions, pick canonical with reasoning.

Discipline lives in `discipline.md` (not duplicated anywhere else). Skills follow the discipline; they don't redefine it.

---

## CLAUDE.md as index + router + gatekeeper

`CLAUDE.md` is the entry point loaded at session start. Three jobs:
1. **Index** — what lives where (one-line per destination).
2. **Routing** — which skill handles which request (table mapping user requests to skills).
3. **Gatekeeper** — anti-overlap rules (10 guardrails that prevent content from drifting to the wrong file).

CLAUDE.md does NOT contain workflow content (that's in skills), domain content (that's in `me/`), or authoring discipline (that's in `discipline.md`). It's pure routing.

---

## Skill composition — how skills compose for a typical job pursuit

A typical end-to-end pursuit of a job:

```
1. Sourcing      (LinkedIn alert → outputs/linkedin/<date>.md → filter in-zone using me/constraints.md → candidates pool)
2. Screening     (read candidates pool entry → score 1-5 using pillars + friction/boost → if 4-5, mark on-deck)
3. Tailoring     (Phase 1 strategy from me/resume + me/voice + me/background + JD → Phase 2 by section → validation gates → side-by-side diff to user → ship as resumes/<jd>.docx)
4. Outreach      (three-touch: ATS submit + HM DM + referral hunt; produce drafts using me/voice + me/background + JD + HM research)
5. Maintenance   (log application; transition pipeline state; process status check snapshots over time)
6. Interviewing  (when recruiter screen lands: generate per-JD interview plan in interviews/<jd>.md from me/background + me/voice + JD + tailored resume)
```

Each skill is self-contained but composes naturally with the others through standard inputs (`me/` files) and outputs (artifact folders or pipeline state).

`skills/profiling/` is invoked OUT OF BAND when new personal data surfaces during a conversation — independent of any active job pursuit.

---

## Pipeline state files (deferred)

The maintenance skill references pipeline state files — operational state that tracks where things are in the funnel:
- **candidates pool** — pre-application JDs with screening scores
- **applications funnel** — submitted apps with status (submitted → recruiter-screen → phone-screen → hm-conversation → interview-loop → onsite-loop → offer / rejected / withdrawn / ghosted)
- **outreach log** — touches per application
- **archive** — closed-out non-submitted
- **weekly metrics** — weekly review log

The OLD system had these as `candidates.json` (structured), `applications.md` (markdown table with 500-word blob notes), `outreach.md`, `archive.json`, `weekly-metrics.md`.

Their format and placement in the NEW system is deferred per `pending.md` — to be settled when the maintenance skill is first operated. The 500-word-blob problem (research dossiers buried in row notes) needs to be addressed at the same time, with research dossiers likely splitting out into their own per-application files.

---

## Gatekeeping principles (anti-overlap)

The hardest part of keeping this system clean is preventing content from drifting to the wrong file. Ten guardrails in `CLAUDE.md` enforce this — examples:
- Voice rules NEVER go in skills (skills APPLY voice rules; they don't OWN them).
- Channel-specific format NEVER goes in voice (voice is cross-channel only).
- Facts NEVER appear in `me/resume.md` unless they're already in `me/background.md` (resume is a curated subset).
- Constraints NEVER drift into skills (skills reference; they don't duplicate).
- Recruiter-Boolean filter list is canonical in `me/voice.md` (don't-claim list); `me/constraints.md` references it for screening knock-outs.

The audit pass at the end of any rebuild applies these guardrails systematically to catch leakage.

---

## Rebuild history (2026-05-20 through 2026-05-22)

The rebuild took place over three days of intensive work. Key phases:

1. **Audit + problem framing.** Mapped the old system's structural problems (duplication, drift, rubber-stampable validation, content in wrong files). Confirmed the right approach was rebuild, not patch.
2. **Archive everything.** Moved the old system to `_archive/2026-05-20-rebuild/`. Started from a near-blank slate.
3. **Multiple rebuild attempts on `me/` files.** Repeatedly built and rebuilt as drilling questions surfaced structural issues (lift-with-edit, inclusion tests with edge-case rescues, voice file with channel-specific tone leaks, don't-claim list as enumeration vs principle).
4. **Comprehensive content inventory.** Catalogued every distinct piece of content across all archived sources (`_archive/content-inventory-2026-05-21.md`). 23 drift events surfaced where the same rule appeared in 2-5 sources with different wordings.
5. **User canonical calls on every drift.** Each drift event got a user decision (em dash sparingly; Log4Shell invited-based-on-reputation; agentic AI defensible per Jingle+MailFlow; etc.).
6. **Hardened inclusion tests with PASSES IF + FAILS IF for all 16 destinations.**
7. **Rebuilt every file from scratch** under the finalized tests, using the canonical resolutions from the drift work.
8. **Audit pass against the inclusion tests** caught 3 violations (sourcing duplicating constraints; interviewing duplicating voice; tailoring duplicating master resume header) and 3 borderline items (MailFlow agentic-AI label; AI-augmented scope rule; Comcast Lean-not-agile parenthetical). All fixed.

The HTML side-by-side diff of the old comp doc vs the new background.md is preserved at `_archive/comparison.html`.

---

## Open / deferred items

Tracked in `pending.md`. Highest-priority deferred:
- **Pipeline state file format + placement** (decide when maintenance skill is first operated)
- **Per-application research dossier placement** (decide when outreach first needs HM research)
- **Per-JD interview artifact folder** (`interviews/<jd>.md` recommended; decide when first interview prep generated)
- **Project Siesta placeholder name** (replace when better name lands)
- **Failure story + NG product vision** (interview prep — need user input to develop)
- **`skills/composing/` content** (placeholder until first cover letter / essay needed)
- **Negotiation skill** (not built; create when first offer arrives)

---

## How to extend this system going forward

When new content surfaces:
1. Apply the destination file's inclusion test (top of each file). Where does it pass?
2. If it passes one destination's test → write there.
3. If it could fit multiple → apply each destination's FAILS IF clauses. The one where no FAILS IF triggers is correct.
4. If still ambiguous → surface to user. Don't decide silently.
5. Apply `discipline.md` Rules 1-9 throughout. Especially Rule 2 (re-derive, don't lift) and Rule 9 (item-level source triangulation if the new content relates to a rule that already exists elsewhere).

When extending a skill (e.g., adding a new outreach channel to `skills/outreach/`):
1. Apply the skill's inclusion test — does the new content fit?
2. If yes, write under the skill's existing sections. Maintain internal structure for clarity.
3. Run the audit (sentence-by-sentence inclusion test) before declaring done.
4. Update `CLAUDE.md` routing table if the addition changes which skill handles which request.

When the rebuild appears to be drifting (which it will, eventually):
1. Don't patch. Patches accelerate drift.
2. Run the content inventory + triangulation process (per `discipline.md` Rule 8 + Rule 9).
3. Resolve drift events with the user.
4. Rebuild the affected files under finalized tests.

---

## What success looks like

- A new session can pick up this system cold by reading `design.md` → `CLAUDE.md` → the relevant skill → relevant `me/` files.
- Every piece of content has exactly one home.
- The inclusion tests catch attempts to place content in the wrong file.
- The discipline rules catch attempts to write files in lift-with-edit fashion.
- Drift across files is caught early via Rule 9 (per-item triangulation) rather than discovered late.
- The system continues to produce high-quality tailored resumes, outreach, and interview prep for Maz's job search without requiring another full rebuild.
