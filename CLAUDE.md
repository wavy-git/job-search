# Job Search System — Entry Point

This file is the index, router, and gatekeeper for the job search system. It tells Claude WHERE everything lives, WHICH skill handles WHICH request, and WHERE content does NOT belong. It does not contain workflow content, personal data, or authoring discipline — those live elsewhere.

**Read this file first in every session.**

---

## Inclusion test for this file

> **PASSES IF:** (a) index — what lives where; (b) routing — which skill handles which request; (c) update / access pointers — how to update each file; (d) gatekeeping guardrails — anti-overlap rules preventing skill/feature duplication; (e) project-level operating context that doesn't fit a specific skill or `me/` file (e.g., voice-dictation interpretation, hard-lock-wins-over-user-input conflict resolution).
>
> **FAILS IF:** any actual workflow content (→ the skill that owns it); any domain content — facts (→ `me/background.md`), voice rules (→ `me/voice.md`), constraints (→ `me/constraints.md`); any authoring discipline (re-derive, audit, source triangulation) (→ `discipline.md`); deferred items (→ `pending.md`); operational state (→ pipeline files); ANY duplication of skill instructions (the whole point of CLAUDE.md is to prevent duplication, not be a source of it).

---

## Index — what lives where

### Personal data (source of truth about Maz)
- `me/background.md` — facts about Maz (career history, achievements, projects, tech stacks, vendors, personal info, education, certifications)
- `me/voice.md` — how Maz communicates and is represented (universal writing-style, claim / don't-claim rules, bridges, brand identity, core beliefs, hard locks)
- `me/constraints.md` — what defines Maz's career zone (comp, locations, wanted titles, function knock-outs, domain knock-outs, direct-reports clause, posting state, recruiter-Boolean credentials)
- `me/resume.md` — master resume content in markdown (mirror of master `.docx`)
- `me/linkedin.md` — master LinkedIn profile content (headline, About, experience one-liners)

### Skills (workflows)
- `skills/profiling/` — maintain `me/` files when new info surfaces; refresh resume/linkedin from background changes
- `skills/sourcing/` — collect JDs from channels; filter to in-zone pool using `me/constraints.md`
- `skills/screening/` — evaluate in-zone JDs for fit/chances; score 1-5
- `skills/tailoring/` — produce tailored resume `.docx` from `me/resume.md` + JD; validation is a phase within this skill
- `skills/outreach/` — produce DMs, emails, invites, follow-ups; three-touch model
- `skills/interviewing/` — produce per-JD interview plans; behavioral mapping; reusable answers
- `skills/maintenance/` — pipeline transitions; status check processing; weekly hygiene; sender-domain mappings
- `skills/composing/` — placeholder for cover letters and application essays (built when needed)

### Artifacts (outputs)
- `resumes/` — master resume `.docx` + per-JD tailored `.docx` files
- `interviews/` — per-JD interview plans (when generated)
- `outputs/` — collected sourcing data (`linkedin/`, `jds/`, `applications/`, `scanner/`)

### Project-level
- `discipline.md` — authoring rules (re-derive, sentence audit, source triangulation, etc.)
- `pending.md` — deferred items, drift log, structural decisions parked, placeholder names
- `CLAUDE.md` — this file

### System
- `.claude/settings.json` — SessionStart hook, permissions
- `.git/`, `.venv/`, `.cache/` — system folders

### Archive
- `_archive/2026-05-20-rebuild/` — old system (pre-rebuild). Reference only; do not modify or use as source of truth.

---

## Routing — which skill for which request

| Request | Skill |
|---|---|
| "Look at this JD" / "Score this role" / "Is this worth pursuing?" | `skills/screening/` (preceded by `skills/sourcing/` for in-zone check if not already done) |
| "Collect today's LinkedIn alerts" / "Add this JD I found" | `skills/sourcing/` |
| "Tailor my resume for this JD" | `skills/tailoring/` |
| "Draft a DM to this hiring manager" / "Write a cold email to this recruiter" / "Send a follow-up" | `skills/outreach/` |
| "Prep me for this interview" / "What stories should I use for this role?" | `skills/interviewing/` |
| "I have new info to add to my background" / "Update my voice rule for X" / "Add to constraints" | `skills/profiling/` |
| "Update status on this application" / "Process today's status check" / "Weekly review" | `skills/maintenance/` |
| "Write a cover letter for this role" | `skills/composing/` (placeholder — content not yet built) |

---

## Update / access pointers

| To update this | Use |
|---|---|
| `me/background.md` (new fact) | `skills/profiling/` workflow |
| `me/voice.md` (new preference / rule) | `skills/profiling/` workflow |
| `me/constraints.md` (new screening param) | `skills/profiling/` workflow |
| `me/resume.md` (curated master) | `skills/profiling/` workflow + `skills/tailoring/` for the curation logic |
| `me/linkedin.md` (master profile) | `skills/profiling/` workflow |
| `resumes/<jd>.docx` (tailored) | `skills/tailoring/` workflow |
| `interviews/<jd>.md` (interview plan) | `skills/interviewing/` workflow |
| Pipeline state files | `skills/maintenance/` workflow |
| `pending.md` (deferred item) | Direct edit per the file's inclusion test |
| `discipline.md` (new authoring rule) | Direct edit per discipline rules |
| `CLAUDE.md` (this file) | Direct edit per the inclusion test above |

---

## Gatekeeping guardrails — anti-overlap rules

These prevent skill/feature duplication and drift. Apply BEFORE writing any new content to any file.

1. **Voice rules NEVER go in skills.** A skill might APPLY voice rules but doesn't OWN them. Voice rules live in `me/voice.md` only.
2. **Channel-specific format NEVER goes in voice.** Cold email format, DM tone, interview answer structure — all live in the respective channel's skill. Voice handles cross-channel rules only.
3. **Facts NEVER go in `me/resume.md` unless they're already in `me/background.md`.** Resume is a curated subset of background. If a fact isn't in background, it shouldn't appear in resume.
4. **Constraints NEVER drift into skills.** Career-zone parameters live in `me/constraints.md` only. Skills reference; they don't duplicate.
5. **Recruiter-Boolean filter list is canonical in `me/voice.md`** (as don't-claim list). `me/constraints.md` references it for screening knock-outs. Don't duplicate the list.
6. **Pipeline state files contain operational state only.** No personal data, no workflow content, no authoring rules.
7. **Per-JD content lives in artifact files**, not in skills. `resumes/<jd>.docx`, `interviews/<jd>.md`, per-application research dossiers (location TBD per `pending.md`) — not in skill folders.
8. **Authoring discipline lives in `discipline.md`** (re-derive, sentence audit, source triangulation, mechanical consistency checks). Skills follow the discipline; they don't redefine it.
9. **Deferred items live in `pending.md`.** Not duplicated in skill files or `me/` files.
10. **When in doubt about where content belongs, apply the destination file's inclusion test** (PASSES IF / FAILS IF at top of each file). If the test fails for that destination, route to the test that passes.

---

## Project-level operating context

These aren't workflow content but apply across every interaction:

- **Voice dictation interpretation.** Maz often uses voice dictation in chat. Transcription artifacts (extra words, missing punctuation, homophones) appear in source material. Don't pattern-match those into voice rules or facts — interpret intent.
- **Hard-lock-wins-over-user-input.** If user input contradicts a hard lock in `me/voice.md` (e.g., asks to claim "Director" as NG payroll title, asks to use the old "walked in unbidden" Log4Shell framing), surface the conflict and ask before applying. The hard lock wins by default.
- **Time zone.** Present times in Eastern Standard Time unless otherwise specified.
- **Push back rather than ship subpar.** If a draft isn't exceptional, name what's missing and fix it before showing. Don't smooth over a real gap.

---

## When in doubt

1. Read this file (you're here).
2. Read the relevant skill's `.md` for workflow.
3. Read the relevant `me/` file for content.
4. Read `discipline.md` for authoring rules.
5. Check `pending.md` for known deferred items related to your task.
6. If still unclear, ask Maz before editing.
