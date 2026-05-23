# Pending

Items that must survive across sessions but aren't already documented in a more specific home. Active session work belongs in the volatile todo tool, not here.

---

## Inclusion test

> **PASSES IF:** durable item beyond a single session AND not already documented in a more specific home — deferred files / features to build later, structural decisions parked for the relevant skill's build-out, stale state to fix, placeholder names to replace, drift event log, cross-session reminders.
>
> **FAILS IF:** anything documented in another file (reference instead of duplicate); active-session work (→ todo tool); domain content (→ `me/` or skill); authoring rules (→ `discipline.md`); routing or operating rules (→ `CLAUDE.md`); operational state (→ pipeline files).

---

## Structural decisions parked for the relevant skill build-out

These were surfaced during the rebuild but deferred because the deciding context only becomes clear when the relevant feature is actively in use.

### Pipeline state file format + placement
The maintenance skill (`skills/maintenance/`) references "pipeline state files" — candidates pool, applications funnel, outreach log, archive, weekly metrics. The OLD system had these as: `candidates.json` (structured), `applications.md` (markdown table with 500-word blob notes), `outreach.md` (markdown table), `archive.json` (structured), `weekly-metrics.md` (free-form log).

**Decide when:** maintenance skill is being actively operated for the first time (next time a sourced JD lands in the pool).

**Considerations:**
- Top-level `pipeline/` folder vs distributed per skill vs `me/pipeline/`.
- Markdown table vs JSON vs JSONL.
- The applications.md "Next Action" blob problem (500-word notes per row) is the main thing to avoid — research dossiers should split out (see next item).

### Per-application research dossiers — placement and format
When researching HM info, company facts, comp band research for a specific application, where does that go? OLD system buried it in `applications.md` row notes (500-word blobs).

**Decide when:** outreach skill is actively producing a warm DM that needs HM research (next time a score-4-or-5 application requires it).

**Options:**
- Top-level `research/<jd>.md` (one file per application, applications row references it)
- `outputs/research/<jd>.md` (consistent with `outputs/` folder for collected data)
- `pipeline/research/<jd>.md` (with operational pipeline)

### Per-JD interview artifact location
`skills/interviewing/` produces per-JD interview plans. Output location TBD until first interview prep is generated.

**Recommendation (not decided):** top-level `interviews/<jd>.md` (parallel to `resumes/<jd>.docx`).

**Decide when:** first interview screen lands and interview prep is generated.

---

## Deferred features / files

### Cover letters / application essays — `skills/composing/`
Placeholder folder exists with stub. Real workflow + templates get built when a JD requires a cover letter or essay. Two prior examples to draw from: Customer.io ("Why this position" 3-part essay) and ElectronX ("Why ElectronX?" + scent product reuse). Captured in `_archive/2026-05-20-rebuild/applications.md` notes.

### Failure story (interview prep)
`skills/interviewing/` flags this as a pending answer. Needs a real story with: real stakes, ownership of failure, clear learning, evidence the learning changed behavior. Candidates (need user input): major program at NG / Comcast / Infotech that didn't go as planned; any investment / hire / product bet / strategic decision that backfired; any time turnaround tactics didn't work.

### NG product vision (interview prep)
`skills/interviewing/` flags this as a pending answer. Forward-looking answer about platform evolution beyond ops. Options to develop: platform beyond AMI; AI-augmented utility operations; customer-facing extensibility; cross-state consolidation.

### Negotiation skill
Not built. Skill scope: workflow for offer negotiation, decline scripts, accept patterns. Build when first offer arrives.

### Hardlock enforcement for stable files (Rule 11 teeth)
Rule 11 in `discipline.md` defines the hardlock for stable files (me/, skills/, CLAUDE.md, design.md, discipline.md, pending.md) — edits require user approval, Rule 5 audit report, Rule 4 sentence-level test pass, and Read-after-edit. Currently the enforcement is discipline-level. To add real teeth:

- **PreToolUse hook on Write/Edit** that blocks edits to any stable file unless a "validated" marker is present in the recent conversation (e.g., user said "apply fixes" or similar approval phrase). If absent, hook prints "edit to stable file blocked — requires user approval marker" and aborts.
- **Per-file marker at the top of each stable file:** *"STABLE — changes require user approval + Rule 4 audit + completion report per Rule 5."* Reminds anyone (or any Claude session) reading the file that direct edits aren't free.

**Decide when:** after the current validation pass completes for all `me/` files and skills, when the system is stable enough to bolt on enforcement. Avoid implementing during a validation pass since validation requires many legitimate edits.

### LinkedIn profile audit
`me/linkedin.md` exists as master content. The actual LinkedIn profile may not be in sync. User flagged earlier the LinkedIn headline was invisible to recruiter Boolean — needs an audit pass. Defer until LinkedIn workstream is activated.

---

## Placeholder names to replace

### Project Siesta
Working name for the umbrella under Seagull Cybernetics that houses MailFlow (philosophy: "the mundane shouldn't tax a meaningful life"). Marked as placeholder in `me/background.md` § Independent Ventures. Replace when a better name lands. One find/replace covers it.

---

## Open / pending facts to verify

These live at the bottom of `me/background.md` § Open / pending. Referenced here for cross-session awareness:
- E-voucher monthly volume (placeholder 2M+, needs exact figure).
- Failure story (also listed under deferred features above).
- NG product vision (also listed under deferred features above).

---

## Stale-state items resolved during 2026-05-22 rebuild

These were stale before the rebuild and have been fixed:
- CLAUDE.md — was pointing at archived files (Maz_Career_Background_Comprehensive.md). Now rewritten as index + router + gatekeeper.
- `.claude/settings.json` SessionStart hook — was printing archived file paths. Now reflects new structure.
- `resumes/Maz_Mavvaj_Director_Resume_FINAL5_5.md` — was redundant with `me/resume.md`. Deleted from `resumes/` (master .md lives in `me/`; .docx + .pdf stay in `resumes/`).

---

## Stale-state items not yet addressed

### `resumes/Maz_Mavvaj_Director_Resume_FINAL5_4.*` (3 files: .docx, .md, .pdf)
Previous canonical version, archived per comp doc. Still occupying space in `resumes/`. Could move to `_archive/` or delete. Defer.

### Old tailored resume `.docx` files in `resumes/`
Tailored versions for prior applications (ElectronX, Wheel, Sourgum, Liberty, Customer_io, Forsyth_Barnes, Nava, Toast, Leap, Mastercard, JPMC). Most applications are closed (rejected or ghosted). Could be archived. Defer unless space matters.

### Word lock files (`resumes/~$*.docx`)
Word temp files created when a .docx is open. Harmless. Could be cleaned up on a low-priority pass.

### Nava-related operational records
User direction was to delete Nava data. Nava is still in `_archive/2026-05-20-rebuild/applications.md` and `outreach.md` as historical record. The pipeline state files for the new rebuild won't carry Nava forward. The .docx (`resumes/Maz_Mavvaj_Director_of_Product_Nava.docx`) is historical artifact — could be deleted.

---

## Drift event log

Drift events found during 2026-05-22 rebuild (per discipline.md Rule 9). Canonical versions per user calls are now in the rebuilt files. This log exists so older framings don't slip back in.

| Item | Old version (stale) | Canonical (current) |
|---|---|---|
| Log4Shell framing | "Walked in unbidden / NOT assigned" | "Invited based on reputation" |
| Em-dash rule | Variants of "never" vs "sparingly" | **Sparingly** (per user) |
| En-dash rule | Absent from job-search archives; "never" in global CLAUDE.md | **Sparingly** (per user) |
| Agentic AI rule | "Don't claim agentic AI track record" | **Defensible per Jingle + MailFlow; not at enterprise scale** |
| AI-augmented PowerShell scope | Inflated to "feature planning and delivery operations" in some tailoring | **Feature documentation specifically** (per Nava overclaim correction) |
| Libz | Dropped in current archive comp doc | **Present** under Liberté (per user) |
| MailFlow + The Cat | Absent in pre-rework | **Present** in IV |
| Tailoring workflow | RT 8-step vs JSS 5-phase Rubric 2 | **RT 8-step** canonical; JSS Rubric 2 dead |
| Validation gates | RV 11 gates vs JSS 7-step QA | **RV 11 gates** canonical; JSS Phase 4 dead |
| Interview story count | Comp doc had 7; interview-prep had 8 | **8 stories** including VP Infotech turnaround |
| Scent product reusable | Only in interview-prep.md | **Canonical reusable** in `skills/interviewing/` |
| Pillar definitions wording | SC terse vs JSS richer | **Merged**: richer JSS text trimmed where redundant (now in `skills/screening/` § 11 background pillars) |
| Resume content (summary, bullets, scope, header, certs, IV ventures count, Core Comp wording, Tools format) | Mixed FINAL5_4 / FINAL5_5 references with drift | **FINAL5_5 across all** (per master `me/resume.md`) |
| CCRE "on resume" status | Tracked as drift between comp doc versions | **Cut**: master resume IS authoritative for what's on it; not tracked elsewhere |
| Don't-claim Nava additions (Government, Design, Agile-Comcast) | Surfaced from Nava overclaim notes | **Cut**: general overclaim principle covers; specific enumeration unnecessary |

---

## Cross-session reminders

### Periodic audit
Per `discipline.md` Rule 5 + Rule 8: periodically run an audit pass across all `me/` files and skill files to catch drift, leaked content, broken cross-references. Recommend after any significant change set.

### When extending the system
- New content → apply destination file's inclusion test (top of each file).
- If content fits multiple destinations, apply each destination's FAILS IF to narrow.
- If still ambiguous, surface to user.
- Apply `discipline.md` Rules 1-9 throughout.

### Pipeline activation
Many skills reference pipeline state files (candidates pool, applications, outreach, archive, weekly metrics) but the format + placement is deferred per "Structural decisions parked" above. The first time any skill needs to write to one, settle the decision then.

### Content inventory + drift triangulation work
`_archive/content-inventory-2026-05-21.md` contains the systematic content inventory + 23 drift events found during the rebuild. Reference if questions arise about how a rule landed where it did, or what was in the pre-rebuild system.
