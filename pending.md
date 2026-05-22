# Pending

Items that must survive across sessions but aren't active work right now. Active work for the current session belongs in the todo tool (volatile, lost when context compresses). Anything already documented in another file gets **referenced** here, not duplicated.

## Inclusion test

> Is this item (a) durable beyond a single session AND (b) not already documented in a more specific home? If yes → add here with enough detail to act on later. If no → put it where it belongs.

---

## Deferred personal-data files

### `me/interview-bank.md` (not yet built)

Built when the interview-prep use case is rebuilt. Will contain:

- **Core stories** (from old `interview-prep.md` and `Maz_Career_Background_Comprehensive.md`):
  - $2M vendor analysis reframing (National Grid)
  - Log4Shell crisis response (Comcast, Dec 2021)
  - NCC revival 20 → 5,000 units (Infotech Director)
  - Multi-bank terminal (Infotech VP)
  - Central bank seat / national card network (Infotech VP)
  - Cloud platform delivery 6 vs 12 months (Comcast)
  - Configuration-driven platform (Infotech Manager)
  - VP Infotech turnaround (the full toxic-culture-to-120K-merchants arc)
- **Anticipated questions and framed answers:**
  - "Why VP to TPM?" (deliberate, MBA, US enterprise entry — answer drafted in archived doc)
  - "Do you have direct reports?" at NG (platform-ownership framing — answer drafted)
  - "Tell me about a failure" — **not yet developed** (see fact-verification items below)
  - "What's your product vision at NG?" — **not yet developed**
- **Reusable answers:**
  - "What's a product you wish you built?" → scent technology answer (full text in archived `interview-prep.md`)
- **Behavioral interview mapping** (which story for which prompt):
  - Influence without authority → $2M vendor or Log4Shell
  - Initiative → Log4Shell or CCRE
  - Strategic product decision → NCC revival or multi-bank terminal
  - Cross-functional program → NG AMI or Infotech national card network
  - Turnaround → Infotech VP or Comcast deployment ops
- **Voice/brand to express:**
  - "The way most problems stay problems is that people stop questioning them."
  - Gap between exceptional and average teams is imagination, not ambition.
  - Leadership = understand vs. assume, build clarity, make decisions visible, reduce friction.
  - Technology should serve people, not constrain them.
- **Not to sound like:** consultant, generic product leader, apologetic about non-traditional path.

Source material: `_archive/2026-05-20-rebuild/interview-prep.md`, `_archive/2026-05-20-rebuild/Maz_Career_Background_Comprehensive.md` § Interview Preparation + Key Stories + Leadership Philosophy + Brand Identity.

### `me/linkedin.md` (not yet built)

Built when the LinkedIn workstream is activated. Will contain:

- **Headline:** Technology Leader, Educator, Builder
- **About** essay (full text in archived comp doc § LinkedIn Profile)
- **Experience one-liners** per role (Head of Products at NG; Senior TPM at Comcast; VP Payment Card Services; Director Products & PMO; Manager Software Dev; Software Developer; Founder Seagull Cybernetics; Innovation & Strategy Advisor; Adjunct Instructor) — all in archived comp doc.

Source: `_archive/2026-05-20-rebuild/Maz_Career_Background_Comprehensive.md` § LinkedIn Profile.

---

## Structural decisions deferred to the relevant skill rebuild

These are decisions that affect file placement / data flow. Each one waits for the skill that actually needs to use it, so we decide with full context instead of pre-committing.

### Pipeline state files — placement
The old system had `candidates.json`, `applications.md`, `outreach.md`, `archive.json`, `weekly-metrics.md`. They are operational state, updated frequently.
- Options: `me/pipeline/`, top-level `pipeline/`, split across owning skills.
- Decide when building the **maintenance** and **outreach** skills.

### Per-application research dossier files — placement
We agreed on one file per application as the dossier. Placement undecided.
- Options: `me/research/YYYY-MM-DD-company-role.md`, top-level `research/`, under `outputs/applications/`.
- Decide when building the **outreach** skill (which uses HM research most heavily) or **screening** (which produces the first sourcing-depth notes).

### `outputs/` folder convention going forward
Current `outputs/` has `applications/`, `jds/`, `linkedin/`, `scanner/`. Scanner is archived. Other three are live (LinkedIn alerts daily, JD bodies, application status checks).
- Decide what stays in `outputs/`, what moves, what's renamed when building the **sourcing** skill.

### Master resume canonical source — `.docx` or `.md` companion
The old system maintained both. They drift silently. Pick one canonical; the other becomes derived (or dropped).
- Decide when building the **tailoring** skill.

### Data flow between skills
Sourcing produces JDs → screening consumes them → tailoring uses screened candidates → outreach acts on submitted ones. Composition not documented anywhere yet.
- Each skill, when built, declares its inputs and outputs as part of its own workflow.

---

## Stale state to fix at end of rebuild

These are known-stale references that will keep firing every session until cleaned. Defer until the rebuild is far enough along to write the replacement.

### `CLAUDE.md`
Still the pre-rebuild version. Routes to files now in `_archive/2026-05-20-rebuild/`. Will be rewritten at the end of the rebuild as: project-level operating rules + routing to `me/` and `skills/`.

### `.claude/settings.json` SessionStart hook
Hook command currently prints:
```
=== Job Search Project — Canonical State ===
IMPORTANT: Read CLAUDE.md first for any career-related work.
Master resume (canonical): resumes/Maz_Mavvaj_Director_Resume_FINAL5_5.docx (and .md companion). FINAL5_4 is archived; do not use.
Source of truth: Maz_Career_Background_Comprehensive.md
...
```
The file references (`Maz_Career_Background_Comprehensive.md`) point at archived content. Update at end of rebuild to reflect the new structure.

---

## Open fact-verification items (referenced, not duplicated)

These live at the bottom of `me/background.md` § Open / pending facts to verify. Not duplicated here. Summary:
- E-voucher monthly volume (placeholder 2M+, needs exact figure).
- Failure story for interviews — not yet developed.
- NG product vision (forward-looking) — not yet developed.

---

## Placeholder names to replace

### Project Siesta
Working name for the umbrella under Seagull Cybernetics that houses MailFlow (philosophy: "the mundane shouldn't tax a meaningful life"). Marked as placeholder in `me/background.md`. Replace when a better name lands. One find/replace when done.

---

## Flagged borderline items in `me/background.md` (kept as-is per direction)

These were flagged during the v2 audit as borderline (could read as rule/framing rather than pure fact). User chose to leave them — noted here so future-Claude knows they were a conscious choice, not an oversight:
- MailFlow "**Defensible agentic AI credential**" label.
- Project Liberté philosophy text ("liberate users from platform lock-in...").
- Adjunct Instructor "**Dimension of identity, not definition**" framing line.

---

## Future-structure considerations (not blocking)

- **Future Independent Ventures beyond Seagull.** Current structure has Seagull Cybernetics as one venture under `## Independent Ventures` in `me/background.md`. Future ventures (new company, advisory, fund, etc.) sit at the same level as Seagull. Nothing to do until a new venture appears.
- **Skill self-containment.** Each skill in `skills/` will be its own folder, fully encapsulated, with its own inclusion rule, workflow, and inputs/outputs declaration. No shared "principles" or "discipline" file at the skill level — skills inherit pattern by reading each other.
- **Word lock files in `resumes/`.** Files like `resumes/~$z_Mavvaj_VP_Embedded_Payments_JPMC.docx` are Word temp files. Harmless. Could be cleaned up on a low-priority pass.
