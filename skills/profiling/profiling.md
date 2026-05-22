# Profiling

Workflow for maintaining the `me/` files — creating new content when info surfaces, updating existing content, auditing, and refreshing derived files (`me/resume.md`, `me/linkedin.md`) when `me/background.md` changes.

This is the skill Maz uses on himself. When new career facts surface in conversation, this skill routes them to the right `me/` file under the right discipline.

---

## Inclusion test

> **PASSES IF:** workflow for updating `me/background.md` with new career facts; workflow for updating `me/voice.md` with new preferences / representation rules; workflow for updating `me/constraints.md` with new screening parameters; workflow for refreshing `me/resume.md` and `me/linkedin.md` when background changes; routing logic (new content → which file → which section); audit procedure post-update.
>
> **FAILS IF:** the `me/` content itself (→ `me/<file>`); operational state updates (→ `skills/maintenance/`); JD evaluation (→ `skills/sourcing/` or `skills/screening/`); tailored artifacts (→ `skills/tailoring/`); outreach (→ `skills/outreach/`); interview material (→ `skills/interviewing/`); cross-cutting authoring rules that apply to all files in the repo (→ `discipline.md`).

---

## Inputs

- The new info, preference, or constraint surfaced in conversation.
- Existing `me/` files for context.
- `discipline.md` for authoring rules (re-derive, audit, source triangulation).

## Outputs

- Updated `me/<file>.md`
- Audit report (per `discipline.md` Rule 5)

---

## Routing — which file does new content belong in?

Apply the receiving file's inclusion test from the top of each `me/` file. Quick router:

| New content shape | Destination | Test |
|---|---|---|
| Positive fact about Maz (career, project, achievement, vendor, number) | `me/background.md` | "True independent of any artifact / role / audience?" |
| Universal writing-style preference (tone, punctuation, words to never use) | `me/voice.md` | "Applies in every artifact?" |
| Claim or don't-claim rule (universal OR conditional / bridge) | `me/voice.md` | "Rule about what to claim / not claim?" |
| Identity, brand, belief Maz expresses | `me/voice.md` | "Expressed across channels?" |
| Hard-lock representation rule | `me/voice.md` | "Never bend rule about how Maz is represented?" |
| Screening parameter (comp, location, knockout, recruiter-Boolean) | `me/constraints.md` | "Defines career zone?" |
| Resume content (header, summary, bullet, skim zone) change | `me/resume.md` | "Goes in master `.docx`?" |
| LinkedIn profile content (headline, About, one-liner) change | `me/linkedin.md` | "Goes in LinkedIn UI?" |

If content fits multiple destinations, apply all destination FAILS IF clauses to narrow.

---

## Workflow — updating an existing `me/` file

1. **Identify destination.** Apply the router table above + the destination file's inclusion test.
2. **Read all relevant sources.** Per `discipline.md` Rule 3 + Rule 9: if the new content relates to a rule that appears elsewhere, find every appearance and check for drift.
3. **Re-derive, don't lift.** Per Rule 2: write the new content fresh; don't copy-paste from chat or source.
4. **Apply the inclusion test sentence by sentence** as you write. Per Rule 4.
5. **Run mechanical consistency checks** post-write. Per Rule 6: headings vs body, internal redundancy, cross-refs resolve.
6. **Produce completion report.** Per Rule 5: which file changed, what was added/removed, sources cross-checked, mechanical checks performed, any items flagged for `pending.md`.

---

## Workflow — adding new info to background that affects resume / linkedin

When `me/background.md` gets a new fact that's significant enough to surface in the master resume or LinkedIn profile:

1. Update `me/background.md` first (per workflow above).
2. Decide if the new fact warrants a master resume update:
   - Yes if: it's a quantified achievement that strengthens an existing bullet, or a new role/credential/certification, or it changes a hard number already used in the resume.
   - No if: it's interview-only material, or it's already covered by an existing bullet, or it's a soft fact (no quantified outcome).
3. If yes, propose the resume update (which bullet to modify, which section to extend) — apply `skills/tailoring/` workflow to the master, treating "the master itself" as the JD's worth-tailoring-for.
4. Update `me/resume.md`. Regenerate master `.docx`.
5. Decide if LinkedIn needs a corresponding update (one-liner per role; About if it's a tone/role shift).
6. Update `me/linkedin.md` if so. Sync LinkedIn UI.
7. Audit report covers all touched files.

---

## Workflow — when user shares a new preference / voice rule

1. Confirm the rule applies universally (cross-channel) OR is conditional (e.g., a new bridge framing). If channel-specific, it's not voice — it's the channel's skill (`skills/outreach/`, etc.).
2. Identify any existing rule it modifies or contradicts. Per Rule 9: if there's drift between current `me/voice.md` and the new preference, surface to user before applying.
3. Update `me/voice.md` per workflow above.

---

## Audit procedure (after any `me/` file update)

- Read the file you just changed end-to-end.
- For each section, ask: does this still pass the file's inclusion test (PASSES IF)?
- For each section, ask: does any content here violate the file's FAILS IF clauses?
- If anything fails — surface and route to correct file.
- Cross-check against other `me/` files: did this update create drift with any cross-reference?
- Produce completion report.
