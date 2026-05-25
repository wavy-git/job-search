# Tailoring

Workflow + frameworks + quality tools for producing a tailored resume `.docx` from `me/resume.md` + the JD. Validation is a phase within this skill (not a separate skill).

Tailoring assumes the JD has already passed sourcing (in-zone) and screening (score 4-5). Tailoring is the production step.

---

## Inclusion test

> **PASSES IF:** generic, reusable tailoring workflow content — process steps (Phase 1 / Phase 2 / validation gates / ship / post-ship); decision criteria (10-point bullet framework, promotion rule, tailor flavor by company stage, skim vs narrative zone discipline); tailoring-specific edge-case handling (hidden employer, fluency protection, count-change documentation); references to required inputs and produced outputs; structural requirements tailoring imposes on the master (line counts, slot counts, row counts, expected sections); output format conventions (save format, naming, side-by-side diff format, validation summary); the modern ATS reality that shapes how tailoring works; illustrative examples using concrete profile content to clarify a workflow, format, or convention (kept minimal; the rule/convention itself stays generic).
>
> **FAILS IF:** any fact about Maz — credentials, employers, projects, vendors, dates, numbers, honors, IV projects, anywhere in the file in any form (→ `me/background.md` or `me/linkedin.md`); master resume content (→ `me/resume.md`); voice rules or hard-lock restatements (→ `me/voice.md`); constraint parameters (→ `me/constraints.md`); the JD body (→ `outputs/jds/`); the tailored output (→ `resumes/`); per-application strategy / research / status (→ `outputs/applications/<jd>.md`); other skills' workflows (sourcing / screening / outreach / interviewing / composing / profiling / maintenance — each owns its own); cross-cutting authoring discipline (→ `discipline.md`).

---

## Inputs

- The JD body (`outputs/jds/<jd>.md`)
- `me/resume.md` (master to derive from)
- `me/background.md` (full source of facts — for surfacing what's relevant to this JD and for promotional reserve)
- `me/voice.md` (writing-style + claim rules + bridges + hard locks)
- `me/constraints.md` (verify JD passed screening — if pursuing for any reason, sanity check)
- This file (workflow + frameworks)

## Outputs

- Tailored resume `.docx` in `resumes/Maz_Mavvaj_<Title>_<Company>.docx`
- Phase 1 written strategy (saved alongside or in the per-application research dossier)
- Side-by-side diff presented to user for review before ship

---

## Two screens we must clear

1. **AI/ATS screen** — automated parsing + scoring against the JD before any human sees the resume.
2. **Recruiter 6-second scan** — human eyepath across page 1 to decide click-into vs discard.

Both must pass or no interview.

---

## Modern ATS reality (validated 2026)

- Modern ATS (Workday, Greenhouse, Ashby, Lever, plus AI-screening layers like Eightfold / HireVue) generate vector embeddings of resume + JD and compute semantic similarity. ~78% of initial screenings use NLP-based semantic matching.
- Keyword stuffing is actively penalized. Repeating terms unnaturally lowers the score.
- What wins: contextual demonstration of skills through achievement bullets, not labels in a list.
- Knock-out filters (location, citizenship, YOE, direct-reports) fire before the AI score is calculated. Missing a knock-out = automatic reject.
- Older parsers still scan skim zones for exact-string keywords. Recruiter Boolean searches still hit on exact strings.

---

## Skim vs narrative zones (the core conflict resolution)

The conflict between ATS keyword surface and 6-second scan readability is resolved by zone discipline.

- **Narrative zones** (Summary, role scope lines, bullets): clean prose, hard numbers, demonstration over labeling. Max 1-2 keywords per natural construction. **NEVER stuff keywords here.**
- **Hybrid zone — Header positioning block:** compact prose surface designed to carry keyword density for AI screening AND scan well as a 3-line header for human eyes.
- **Skim zones** (Core Competencies, Tools & Technologies, Certifications): carry exact JD keyword surface. Stuffing acceptable here. Recruiter Boolean and older ATS parsers scan these.

Zone discipline alone resolves most ATS-vs-scan trade-offs.

---

## The 8-step workflow

Strict sequence. Do not skip steps. Do not present the tailored resume to the user until validation passes.

1. **Phase 1 — JD analysis + tailoring strategy.** Produce written strategy. (See Phase 1 detail below.)
2. **Phase 2 — Tailor by section.** Apply the strategy. (See Phase 2.1-2.8 detail below.)
3. **Validation — run every gate.** (See Validation Gates 0-10 below.)
4. **Adjust — fix every validation failure.** Re-edit the tailored resume.
5. **Re-run validation if any material change was made in step 4.** Repeat until all gates pass.
6. **Present** the side-by-side diff + validation-pass summary to the user.
7. **Apply user feedback** if any. Re-run validation on changed sections.
8. **Ship** (per post-ship section: ATS submit + outreach via `skills/outreach/` + log via `skills/maintenance/`).

The order is not optional. Presenting an un-validated resume to the user is a process failure.

---

## Phase 1 — JD analysis + tailoring strategy (do NOT touch the resume yet)

This is the gate that prevents producing a tailored resume that misses key JD priorities. **If Phase 1 isn't done in writing, do not start Phase 2.**

### Phase 1 steps

1. **Verify JD body is canonical.** Pulled from company ATS (Ashby / Greenhouse / Lever / Workday), not LinkedIn abbreviations. Saved to `outputs/jds/<date>-<co>-<role>.md` with header.

2. **Identify the top 6 key qualifications.** Read the JD comprehensively. Rank by importance to recruiter screen.

3. **Distinguish verb mode for each priority** — ownership ("own the roadmap," "lead," "drive"), discovery ("investigate," "analyze," "research"), execution ("ship," "deliver"), collaboration ("work closely with," "partner"). Anchor each priority with the matching verb mode in the resume.

4. **Deep-read the career sources before mapping:**
   - `me/resume.md` (current master, full body — every section)
   - `me/background.md` (full facts, promotional reserve)
   - `me/voice.md` (hard locks, don't-claim, bridges)

5. **Map each of the top 6 against background:**
   - Which background items hit each qualification (direct match, adjacent, or via bridge framing)
   - **Look for patterns across multiple roles**, not just single items
   - **Credential check (both directions).** Open and read `me/background.md` § Certifications & Honors AND `me/linkedin.md` § Licenses & Certifications now. (a) **Forward:** for any credential the JD requires, verify it's already held (don't flag as gap if held). (b) **Reverse:** scan all held credentials — regardless of whether the JD explicitly mentions specific certs — for any that would strengthen the resume for this JD. Held credentials not yet on the master resume are candidates for the tailored resume's Certifications section (Phase 2.8) or Core Competencies (Phase 2.6) — both skim zones designed to carry exact keyword surface.
   - Note gaps where no defensible match exists
   - Identify which bridge framings are needed (per `me/voice.md` § Don't-claim list + bridges)
   - Identify which reserve material is a promotion candidate (per promotion rule below)

6. **If any priority's evidence is thin or ambiguous, ask the user clarifying questions before tailoring.** Don't fabricate. Don't guess.

7. **Produce the tailoring strategy IN WRITING:**
   - Top 6 JD priorities, ranked, with verb mode noted
   - Each priority's mapping to background (direct / adjacent / pattern / bridge)
   - Which sections of the resume highlight which JD qualification (e.g., Header carries #1-#2 industries/disciplines; Summary intro reinforces #1-#2; new S2 sentence covers #3-#5; 3 Summary bullets carry hard-number punches; Bullet X in NG section covers #6; Core Competencies skim zone carries #2 and #6)
   - Which reserve material gets promoted, where, and why (cite (a)/(b)/(c) of promotion rule explicitly)
   - Which bridge framings are needed (cite the specific bridge from voice.md)
   - Which gaps stay as gaps (don't fabricate; document and accept)

8. **Full-resume audit before Phase 2.** Walk all 9 sections (Header positioning block, title, summary, scope lines, bullets, IV order, Core Competencies, Tools & Technologies, Certifications) and document which need changes per the strategy and which stay as master.

9. **Only after the written strategy is produced do you start Phase 2.**

---

## Phase 2 — Tailor by section

Apply the strategy from Phase 1 to each section in the order below. Every change must be earned by the strategy — no edits without strategy backing.

**Specificity in narrative zones.** Every noun in narrative zones needs concrete grounding. Vague abstracts ("prototypes," "workflows," "platforms," "outcomes") without specification fail. Test: can the reader picture the work from the words alone?

### Phase 2.1 — Header positioning block

The 3-line block under contact info is fully tailorable per JD. No hard locks. Run BEFORE Summary.

Master 3-line block lives in `me/resume.md` § Header. Read from there for the current master values; do not duplicate here.

Rules:
- **Line 1 (role identity):** swap when JD calls for a different identity ("Product Leader," "Operations Executive," "Transformation Leader"). Must be defensible per `me/background.md`.
- **Line 2 (disciplines):** reorder/swap to lead with JD's primary function. Drop irrelevant slots; replace with JD-relevant disciplines defensible per background.
- **Line 3 (industries):** reorder/swap to lead with JD's primary industry. Drop irrelevant tags; add JD-relevant industry tags defensible per background.

This block is a prime AI-screening keyword location — above the fold, high keyword density per square inch. Place JD's specific industry/discipline keywords here first.

### Phase 2.2 — Summary

Master structure: prose opener + 3 quantified bullets + closing identity line. Do NOT rewrite the structure.

- **S1 (prose opener):** minor edits only (not rewrite). Must carry the **#1 JD priority**. May carry more if the master sentence allows natural minor edits.
- **3 quantified bullets:** minor edits only (not rewrite), each stays ≤1 line. If a bullet is clearly off vs JD priorities, you MAY swap one for a promoted bullet from background. **Limit: 1 promotion in Summary bullets per tailored resume** (independent of Phase 2.3 promotion).
- **Closing identity line:** do not change. Brand identity.

**Fluency protection:** never sacrifice the fluency or power of S1 to cram priorities in. If S1 reads stuffed, drop a priority and reposition it elsewhere on page 1.

### Phase 2.3 — Career progression — titles, scope, bullets

Applies to all body roles in the career progression section of the master.

- **Role titles:** match JD's title verbatim where defensible (functional descriptor, no payroll inflation). Apply all hard locks per `me/voice.md` § Hard locks — open and read voice.md now.
- **Scope lines:** freely tailorable. Same facts, JD-relevant lens. Avoid keyword piles.
- **Bullets:** minor edits only (not rewrite). Strong reason required:
  - JD-cited tool/term not in current wording (swap a noun)
  - Verb-mode mismatch where the mismatch is **severe** (e.g., ownership vs collaboration). Skip when borderline (ownership vs execution).
  - Reordering bullet sequence within a role to lead with JD-relevant outcome
- **Bullet promotion (body):** AT MOST 1 promoted bullet across the entire body per tailored resume. Run detailed analysis first. Independent of Phase 2.2's Summary promotion (so up to 2 total promotions per tailored resume).

**Bullet count discipline:** match the per-role bullet counts in the current master (`me/resume.md`). Most tailorings swap/reorder, rarely add. Flag any count change in the strategy and the diff. No silent count changes.

Every modified bullet must pass the 10-point bullet framework (below).

### Phase 2.4 — Flag when blind rule-following misses something important

These rules are guardrails, not a script. If applying them mechanically would miss a key JD signal — **stop and flag to the user**:
- A JD priority that cannot be reinforced by Summary S1 edits OR a single promoted bullet (might need a 2nd promotion — flag, don't silently break the limit).
- A JD verb mode that conflicts with multiple bullets across a role section (the pattern is wrong, not just one bullet — flag).
- A JD-cited domain/tool/term whose closest defensible bridge isn't in `me/voice.md` (flag, propose framing, get confirmation).

### Phase 2.5 — Independent Ventures

Master has 3 ventures + builder-identity intro paragraph. Keep the intro intact for senior-leadership / Series A / founder JDs.

Ordering: reorder ventures to lead with whichever best matches the JD's primary signal. Capability per venture is in `me/background.md` § Independent Ventures. Default (no clear pull): master order from `me/resume.md` § Independent Ventures.

### Phase 2.6 — Core Competencies (skim zone)

Master = 8 fixed slots (per `me/resume.md`). Tailoring allowed.

Rules:
- **Count stays at 8 slots.** Don't grow or shrink.
- Replace slots with JD's exact must-have keywords when needed. Source from `me/background.md` when keyword isn't on master but underlying capability is real.
- Identity-anchored slots in Core Competencies represent capabilities present in the candidate's background — could anchor to career roles, Independent Ventures, credentials, honors, or any combination. Keep an identity-anchored slot present unless the JD has zero surface for the underlying capability.
- Document each replacement in Phase 1 strategy: which JD keyword drove it, where in background the capability is anchored.

### Phase 2.7 — Tools & Technologies (skim zone)

Master = 6 categorized rows (per `me/resume.md`).

Rules:
- Reorder items WITHIN a row to lead with JD-relevant items.
- Reorder ROWS to lead with the JD-relevant category.
- Tools/vendor names not on master may be pulled from `me/background.md` or `me/linkedin.md` when the JD references them or weights the underlying capability.
- Primary AI-screening keyword location alongside Header. Surface JD's specific tool names here, not in narrative.

### Phase 2.8 — Certifications & Honors (LOCKED)

Master list (per `me/resume.md`): 8 items in order.

Lock as-is. Do not tailor unless a major credential is genuinely missing OR JD knock-out requires reordering. If academic / pedigree honors are present in the master, surface them for JDs where pedigree signals positively; deprioritize for JDs that prioritize practical builder capability over credentials.

---

## Validation gates (Gates 0-10)

Run every gate after Phase 2. **Do not present an un-validated resume to the user.** If any gate fails, fix it before continuing. Re-run any gate whose section was modified by a fix.

### Gate 0 — Strategy exists in writing
Phase 1 produced a written strategy mapping top 6 JD qualifications with verb modes, sections needing changes, promotions cited, bridges cited. **If no written strategy, return to Phase 1.**

### Gate 1 — JD priority coverage
- #1 priority lands in Summary S1.
- 4-5 of top 5 priorities covered in Summary (S1 + bullets).
- 5th lands somewhere on page 1 (Header / Summary bullet / scope line / skim zone).
- Closing identity line untouched.
- Summary bullets: ≤1 line each; max 1 promoted bullet.
- Bridge framings appear in every section they should.
- Coverage table filled in (priority / verb mode / where on page 1 / pass).

### Gate 2 — Hard locks
Open and read `me/voice.md` § Hard locks now. Apply every hard lock to the tailored resume. Bullet count discipline: counts match the current master (`me/resume.md`) unless a count change is documented per Phase 2.3.

### Gate 3 — 10-point bullet framework (every modified bullet)
Each modified bullet passes all 10 (see 10-point framework below).

### Gate 4 — Recruiter-shoe test on summary
Read the summary as a recruiter with 6 seconds and zero domain context.
- Every term decodes in 2 seconds by a non-domain reader (no internal abbreviations without expansion; no unexplained product or project names).
- Every word earns premium real estate.
- Specificity check (no vague nouns without grounding).
- Each sentence clear; no compound clauses requiring re-parse.
- Each fact attributed to its real role (no verb-stacking conflating roles).
- Each number anchored to a JD priority with context.
- JD verbatim language echoed where defensible.
- Pattern vs one-off (each priority anchored on pattern preferred).
- Phrase-level reinforcement audit (each phrase ties to a top-5 priority).
- Test-by-deletion (mentally delete each word; if priority reinforcement still holds, delete it).

### Gate 5 — 6-second mock scan
Read only the top of page 1 in 6 seconds. State the punchline. **Does it match the JD's #1 priority?**

### Gate 6 — JD must-have coverage
Every JD must-have demonstrated somewhere (bullet / scope line / skim zone). List each + where it lands.

### Gate 7 — Knock-out check
- Location: meets JD requirement.
- Citizenship: meets (or no requirement).
- YOE: meets or exceeds JD minimum.
- Direct-reports: meets JD requirement OR JD has soft mentor/coach language only.

### Gate 8 — Length and trim
- 1-2 pages.
- **Trim 10%.** Read every sentence; cut what doesn't earn.

### Gate 9 — Verify file state, then side-by-side diff
- **Read the current `.docx` state** before composing the diff. Don't rely on memory of what was "applied."
- Compose side-by-side diff using canonical format (below).
- **Restate the change set in plain words** before applying.

### Gate 10 — Apply user feedback
- User feedback applied to changed sections.
- **Re-run Gates 1-8 on any sections changed in response.** A Summary edit may break Gate 1; a bullet edit may break Gate 4.
- **If user feedback contradicts a hard lock from voice.md, hard lock wins.** Surface conflict; do not silently apply.

---

## 10-point bullet framework

Every modified bullet must pass all 10:

1. **Outcome first** — leads with what changed.
2. **Scale signal** — shows the size of impact.
3. **So what** — recruiter would care.
4. **One idea** — says one thing clearly.
5. **Scannable** — 1.5 lines max.
6. **Executive tone** — sounds like a leader wrote it.
7. **Decision-maker signal** — shows Maz made a choice.
8. **Altitude** — right level of abstraction.
9. **Defensible** — can be backed up in interview.
10. **Pattern reinforcement** — supports the career thesis.

A bullet that fails any of the 10 must be fixed before ship.

---

## Promotion rule (for reserve material)

**Reserve material** = career facts (stories, tools, techniques, vendors, methodologies, descriptors) that are real and defensible but kept OFF the master resume by default. Holding them back keeps the master tight; surfacing them is a tailoring move when a specific JD weights them.

Reserve material lives in `me/background.md` (the full facts; what's NOT in `me/resume.md` is the reserve).

### Bullet-level promotion (highest bar)

Promote a reserve item to a resume bullet only if all three conditions:

(a) **Strengthens match to JD must-have OR nice-to-have.** Cite the specific JD line.
(b) **Passes the 10-point bullet framework.**
(c) **Doesn't displace a stronger master bullet for THIS JD.** Run the displacement test.

### Skim-zone promotion (lower bar)

For Tools & Technologies / Core Competencies / Certifications, promote a reserve item when:

(a) **JD references the keyword explicitly** OR weights the underlying capability.
(b) The keyword is **defensible per `me/background.md`** (don't fabricate; check the role section it lives under).

Skim-zone promotions don't require the 10-point framework — they're keywords, not stories.

### Citation discipline (no silent promotions)

For every **bullet-level** promotion, cite in the Phase 1 strategy output:
(a) the specific JD line that drove the promotion
(b) the 10-point check explicitly run
(c) the displaced bullet OR documentation of why no displacement

For every **skim-zone** promotion, note in the strategy which keyword(s) came from background reserve (vs. master) so the choice is auditable.

---

## Promotional reserve — where to find candidates

The full reserve is `me/background.md` content NOT already in `me/resume.md`. For each JD, open and read background; scan for items that strengthen JD match per the promotion rule above. Document selections in the strategy with citations to background sections. Also check `me/linkedin.md` for additional reserve content (Projects, Recommendations, Honors) not already in resume or background.

---

## Tailor flavor by company stage

Sanity-check AFTER the Phase 1 strategy is written. Not the starting point.

Company stage determines who reads the tailored resume first and how they read it. For the JD's stage: identify the likely first reader, read the tailored resume through that reader's lens, and surface relevant prior experience by matching the JD stage to role stage tags in `me/background.md`. Adjust emphasis where the read doesn't match what they value seeing.

| JD Stage | Likely first reader | How they read | What they value seeing | Where to find in background |
|---|---|---|---|---|
| Series A (≤100 ppl) | Founder / co-founder | End-to-end, fast, gut-check | Builder credibility, mission fit, concrete shipped work, low-ceremony | Roles whose stage tag contains "Series A" |
| Mid-stage (100-1K) | Hiring manager | Selective, scanning for domain fit | Domain depth, KPI ownership, platform thinking, scaling track record | Roles whose stage tag contains "Mid-stage" |
| F500 corporate (5K+) | ATS + recruiter 6-second scan, then HM | Keyword match first, then narrative | Skim-zone keyword surface, scale signals, regulated/enterprise credibility | Roles whose stage tag contains "F500 / Large-corporate" |
| FAANG / Big Tech | Bar-raiser + leveling team | Bullets as behavioral prompts | Leadership-principle behaviors, technical depth, data rigor | Roles whose stage tag contains "FAANG / Big Tech" |

If the candidate has no roles directly tagged at the JD's stage, surface roles whose work content best fits "what they value seeing" — read role descriptions in `me/background.md` and select on substance.

Starting from flavor produces a stage-template tailoring that may miss actual JD priorities. Strategy first; flavor checks alignment.

---

## Hidden-employer handling

For recruiter-fronted roles where the actual employer is hidden:

1. **Infer the industry from JD content.** Use responsibilities, tech stack, comp range, regulatory references, problem domain.
2. **Apply industry-appropriate framing** in the tailored resume. Fintech reads → fintech frame; enterprise SaaS reads → enterprise SaaS frame.
3. **Fall back to generic-industry framing** only when JD content is too thin to infer.
4. **Document the hidden-employer flag** in the application research and tailoring strategy. Verify employer reveal at apply time. Update framing if revealed employer changes the industry inference.

---

## Side-by-side diff — canonical format

When presenting the tailored resume to the user, use this exact format. Locked because it's the only format that renders correctly in the Claude Code desktop renderer.

- **Removed text:** wrap in `~~***[...]***~~` — produces strikethrough + bold-italic + square brackets
- **Added text:** wrap in `***[...]***` — produces bold-italic + square brackets
- **Table structure:** 5 columns — `# | Section | Master | [Tailored Company] | Why`
- **Cell content:** show only sections that changed; drop unchanged rows. Within each cell, show enough surrounding context to locate the change, but trim aggressively (`...` is fine for unchanged middle).
- **Do not use:** monospace/code style (changes font, dilutes signal); HTML tags (`<u>`, `<mark>`, `<span>` — renderer strips them); yellow background (unsupported).

Example row:

```
| 1 | Summary | ...stalled ~~***[fintech startup]***~~; scaled it from 10K... | ...stalled ***[payments venture]***; scaled it from 10K... | Generalizes industry framing for hidden employer. |
```

Present the diff **with the validation-pass summary** so the user knows every gate has cleared. If a gate could not be passed (rare), surface the specific failure with the diff.

---

## Save format and naming convention

Filename: `resumes/<Candidate_Name>_<Title>_<Company>.docx`

Examples: `Maz_Mavvaj_Sr_PM_Leap.docx`, `Maz_Mavvaj_Director_PM_Customer_io.docx`, `Maz_Mavvaj_Director_AI_Product_Definition_Mastercard.docx`.

Master canonical: per `me/resume.md`.

After save, immediately run validation gates and prepare the side-by-side diff.

---

## Post-ship

After user approves the diff and confirms submit:

1. Final save of the tailored resume.
2. ATS submit (user confirms completed).
3. Trigger `skills/outreach/` three-touch (HM DM + referral hunt).
4. Trigger `skills/maintenance/` to move pipeline row from candidates → applications.

---

## Open / parked items

- Per-application tailoring strategy file placement (currently buried in application notes; could move to a per-application research dossier or `me/research/` style location) — see `pending.md`.
- "Used at" promotion log — when reserve material gets promoted for a specific role, track which item was promoted at which company so it's reusable next time. Placement TBD.
