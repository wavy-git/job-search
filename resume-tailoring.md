# Resume Tailoring Instructions

Last updated: 2026-05-12

This file contains the resume tailoring framework. **Resume tailoring is the activity of customizing the master resume for one specific JD so it passes AI + recruiter screens by mapping the JD's key competencies to Maz's background.**

Related files (each has a single, distinct purpose; no duplication):
- `screening_criteria.md` — screening (decide if a JD is worth pursuing). Run before any tailoring decision.
- `resume-validation.md` — validation checklist for the tailored resume. Run after Phase 2, before ship.
- `Maz_Career_Background_Comprehensive.md` — career facts: hard locks, reserve material, pillars.

---

## Top-of-file principles (apply throughout)

**Honesty / non-fabrication.** If evidence doesn't exist in Maz's background, don't invent. Use bridge framing or ask the user. Never claim what isn't real. The pillar-identity hard locks and don't-claim list in the comprehensive doc are the operational manifestation.

**Hard-lock vs user-feedback precedence.** When user feedback during tailoring contradicts a hard lock (e.g., asks for a pillar Maz doesn't have, modifies a hard number, claims a domain that's on the don't-claim list), the hard lock wins. Surface the conflict to the user explicitly; do not silently apply the conflicting feedback.

---

## Workflow

The tailoring activity follows a strict sequence. Do not skip steps. Do not present the tailored resume to the user until validation passes.

1. **Phase 1 — JD analysis + tailoring strategy.** Produce written strategy. (See Phase 1 below.)
2. **Phase 2 — Tailor by section.** Apply the strategy. Save `resumes/Maz_Mavvaj_[Title]_[Company].docx`. (See Phase 2 below.)
3. **Validation — run every check in `resume-validation.md`.** Identify any failures.
4. **Adjust — fix every validation failure.** Re-edit the tailored resume.
5. **Re-run validation if any material change was made in step 4.** Repeat until all checks pass.
6. **Present** the side-by-side diff and the validation-pass summary to the user.
7. **Apply user feedback** if any. Re-run validation on changed sections.
8. **Ship** (per `resume-validation.md` post-ship section: ATS submit + outreach + logging).

The order is not optional. Presenting an un-validated resume to the user is a process failure.

---

## Phase 1: JD analysis + tailoring strategy (do NOT touch the resume yet)

This is the gate that prevents producing a tailored resume that misses key JD priorities. **If Phase 1 isn't done in writing, do not start Phase 2.**

1. **Pull JD body from canonical source** (company ATS like Ashby HQ / Greenhouse / Lever / Workday, NOT LinkedIn abbreviations). Save to `outputs/jds/YYYY-MM-DD-{company}-{role}.md` with header (url, company, title, location, fetched_at, posting_status).

2. **Identify the top 6 key qualifications the hiring team and recruiter are looking for.** Read the JD comprehensively. Rank by importance to the recruiter screen. **Distinguish verb mode** for each priority — ownership ("own the roadmap," "lead," "drive"), discovery ("investigate," "analyze," "research"), execution ("ship," "deliver"), collaboration ("work closely with," "partner"). Anchor each priority with the matching verb mode in the resume.

3. **Deep-read the career sources before mapping:**
   - `resumes/Maz_Mavvaj_Director_Resume_FINAL5_4.md` (current canonical master, full body — every section). Note: `FINAL5_5.docx` is a draft candidate being built; not yet promoted to canonical master.
   - `Maz_Career_Background_Comprehensive.md` (career history, hard locks, reserve material list, 11 pillars)
   - Memory files at `/Users/mmavvaj/.claude/projects/-Users-mmavvaj-Projects-dev-wavygull-job-search/memory/`

   Don't rely on memory or summary. The master resume is a SUBSET of the full background; reserve material in the comprehensive doc is promotable to a tailored resume bullet when the JD weights it.

4. **Map each of the top 6 against background:**
   - Which background items hit each qualification (direct match, adjacent, or via bridge framing)
   - **Look for career patterns across multiple roles**, not just single items. If a priority shows up at Infotech AND Comcast AND National Grid as the same kind of work, that pattern is stronger evidence than any single bullet. Anchor on the pattern, not a single instance.
   - **Credential check before flagging a gap.** Before flagging any JD-required credential (PMP, AWS, CSPO, etc.) as friction, check Maz's actual credentials in the master resume Certifications + comprehensive doc + memory files. Required credentials Maz holds are credential matches, not gaps.
   - Note gaps where no defensible match exists.
   - Identify which gaps need a bridge framing (per the domain-bridging playbook below).
   - Identify which reserve material is a promotion candidate (per the promotion rule below).

5. **If any priority's evidence is thin or ambiguous, ask the user clarifying questions about background before tailoring.** Don't fabricate. Don't guess. Examples: "Was X built using AI tooling?" "Does this pattern appear in roles I haven't surfaced?"

6. **Produce the tailoring strategy IN WRITING before touching the resume:**
   - Top 6 JD priorities, ranked, with verb mode noted
   - Each priority's mapping to background (direct / adjacent / pattern / bridge)
   - Which sections of the resume highlight which JD qualification (e.g., Summary lands #1-#4 in S1-S2; Bullet X in NG section covers #5; Core Competencies skim zone carries #2 and #6)
   - Which reserve material gets promoted, where, and why (cite (a)/(b)/(c) of promotion rule explicitly)
   - Which bridge framings are needed (cite domain-bridging playbook entries)
   - Which gaps stay as gaps (don't fabricate; document and accept)

7. **Full-resume audit before Phase 2.** Walk all 8 sections (title, summary, scope lines, bullets, IV order, Core Competencies, Tools & Technologies, Certifications) and document which need changes per the strategy and which stay as master. Surface this list in the Phase 1 strategy output.

8. **Only after the strategy is written do you start Phase 2.**

---

## Phase 2: Tailor by section

Apply the strategy from Phase 1 to each section in order. Every change must be earned by the strategy — no edits without strategy backing.

**Zone discipline:**
- **Narrative zones** (Summary, scope lines, bullets): clean prose, hard numbers, demonstration over labeling. NEVER stuff keywords.
- **Skim zones** (Core Competencies, Tools & Technologies, Certifications): carry exact JD keyword surface. Stuffing acceptable here.

**Specificity in narrative zones (additional rule).** Every noun in narrative zones needs concrete grounding. Vague abstracts ("prototypes," "workflows," "platforms," "outcomes") without specification fail. Test: can the reader picture the work from the words alone? If they ask "what specifically?" the phrase is too vague.

**Section-by-section work:**
1. **Title alignment**: match JD's title verbatim where defensible (functional descriptor, no payroll inflation). Per the hard locks (see comprehensive doc), never claim "Director" as the current NG payroll title.
2. **Summary**: every word earns premium real estate. Land the top JD priorities in S1-S2 of the summary so the recruiter sees them in 6 seconds (specific threshold in `resume-validation.md` Gate 1). Each sentence does work; reader effort matters more than sentence count rules.
3. **Scope lines** (under each role): JD-relevant lens, same facts. Avoid keyword piles.
4. **Bullets**: reorder, replace, or promote reserve material per the promotion rule.
   - **Bullet count discipline.**
     - **Master (FINAL5_4, current canonical):** NG=4, Comcast=4, Infotech VP=3, Director=3, Manager=2, Developer=2.
     - **Draft (FINAL5_5, not yet canonical):** NG=5, Comcast=4, Infotech VP=5, Director=3, Manager=2, Developer=2.
     - Default to whichever version is the active master at tailoring time. When promotion of reserve material adds a bullet vs the active master (e.g., NG 4→5), flag the count change explicitly in the strategy and in the diff. No silent count changes.
   - Every modified bullet must pass the 10-point bullet framework (see `resume-validation.md`).
5. **Independent Ventures order**:
   - Jingle first when JD wants player-coach / hands-on / live builder
   - Lighthouse first when JD wants operational visibility / risk / governance / PMO
6. **Core Competencies** (skim zone): swap to JD's exact must-have keywords. Drop master entries that don't fit. Add JD-aligned slots. **Sourcing:** keywords may be pulled from `Maz_Career_Background_Comprehensive.md` § PROMOTIONAL RESERVE table (e.g., "Lean operations," "Data-driven decision-making," "Regulatory shaping") when the underlying capability is real per the comp doc but not currently on the master.
7. **Tools & Technologies** (skim zone): reorder to lead with JD-relevant tools. **Sourcing:** Tools/vendor names not currently in master may be pulled from the PROMOTIONAL RESERVE table (e.g., Ingenico, Gemalto, Thales, Temenos for payments JDs; "predictive analytics," "PCI-DSS," "payment switching") when JD references them or weights the underlying capability.
8. **Certifications** (skim zone): reorder to lead with JD-relevant certs.

**Hard locks** (verify none violated; full list in `Maz_Career_Background_Comprehensive.md` § Hard Locks):
- Hard numbers preserved verbatim
- Companies, dates, employment facts unchanged (chronological structure)
- No "Director" payroll-title claim at NG
- Pillar identity respected (no claims of pillars Maz doesn't have)

**Save** as `resumes/Maz_Mavvaj_[Title]_[Company].docx`.

After Phase 2, open `resume-validation.md` and run every check before ship.

---

## Promotion rule (for reserve material)

**Reserve material** = career facts (stories, tools, techniques, vendors, methodologies, descriptors) that are real and verifiable but kept OFF the master resume by default. Holding them back keeps the master tight; surfacing them is a tailoring move when a specific JD weights them.

**Two reserve sources in the comprehensive doc:**

1. **§ Promotion rule for interview-only material** — narrative reserve (story-level material). Originally NG-only:
   - AI-augmented PowerShell + Jira/Jira Align API automation (NG)
   - CCRE change management with Jira Kanban + Power BI dashboards (NG)
   - L+G deployment gap analysis (NG)
   - ServiceNow migration (NG)

2. **§ PROMOTIONAL RESERVE — Multi-Surface Tailoring Candidates** — tools, techniques, vendors, keywords, methodologies. Covers Infotech VP innovations (predictive merchant targeting, pull-based logistics, automated remote config, multi-bank device, transaction routing/settlement/security frameworks, PCI-DSS), vendor partners (Ingenico, Gemalto, Thales, Temenos), Comcast operational philosophy (Lean flow, WIP limits, quality gates, ownership-based accountability, etc.), and interview-only inherited-state descriptors.

### Bullet-level promotion (highest bar)

Promote a reserve item to a resume bullet only if all three conditions:

(a) **Strengthens match to JD must-have OR nice-to-have.** Cite the specific JD line.
(b) **Passes the 10-point bullet framework.** (See `resume-validation.md`.)
(c) **Doesn't displace a stronger master bullet for THIS JD.** Run the displacement test.

### Skim-zone promotion (lower bar)

For Tools & Technologies / Core Competencies / Certifications, promote a reserve item when:

(a) **JD references the keyword explicitly** OR weights the underlying capability.
(b) The keyword is **defensible per the comp doc** (don't fabricate; check the role-section it lives under).

Skim-zone promotions don't require the 10-point bullet framework — they're keywords, not stories.

### Interview-only items

Some reserve items (e.g., cultural transformation specifics, CISA Log4Shell severity context, inherited toxic culture / bleeding finances at Infotech VP) are flagged interview-only in the PROMOTIONAL RESERVE table. **Never surface to resume.** They're behavioral / narrative material.

### Citation discipline (no silent promotions)

For every **bullet-level** promotion, cite in the Phase 1 strategy output:
(a) the specific JD line that drove the promotion
(b) the 10-point bullet check explicitly run
(c) the displaced bullet OR documentation of why no displacement

For every **skim-zone** promotion, note in the strategy which keyword(s) came from the PROMOTIONAL RESERVE (vs. the master) so the choice is auditable.

The "Used at" annotation in the comprehensive doc reserve tables tracks which items have been promoted at which company. Update it on every promotion.

---

## Hidden-employer handling

For recruiter-fronted roles where the actual employer is hidden (Forsyth Barnes, Wayoh, aggregator listings like Ladders / RemoteHunter / Recruiting from Scratch):

1. **Infer the industry from JD content.** Use responsibilities, tech stack, comp range, regulatory references, problem domain to judge the industry.
2. **Apply industry-appropriate framing in the tailored resume.** If the JD reads fintech, frame fintech. If the JD reads enterprise SaaS, frame enterprise SaaS.
3. **Fall back to generic-industry framing only when JD content is too thin to infer.**
4. **Document the hidden-employer flag in the candidates.json / applications.md notes.** Verify employer reveal at apply time. Update the resume framing if the revealed employer changes the industry inference.

---

## Domain-bridging playbook

When Maz's pillars don't directly match the JD's industry, use these defensible framings (no fabrication):

| Target industry | Bridge framing | Justification |
|---|---|---|
| Marketplace SaaS (Sourgum, etc.) | "B2B SaaS marketplace" | Infotech B2C PSP serving merchants is a multi-sided platform; multi-bank terminal is consolidation in fragmented market |
| Telehealth / healthcare ops (Wheel, etc.) | "Regulated infrastructure at national scale" | NG is regulated; HIPAA isn't claimed but regulatory operating muscle transfers |
| Energy / commodities exchange (ElectronX, etc.) | "Regulated payments + energy intersection" | NG energy + Infotech payments + central bank seat |
| Cybersecurity SaaS (Cobalt, Microsoft Defender, etc.) | "Operational intelligence in cybersecurity" — Comcast Log4Shell pattern, NOT MDR/MSSP product claim | Adjacent expertise only; don't claim MSSP/MDR specialty |
| AI/automation product (Wheel, Ladders client, etc.) | "AI-augmented operations + automation builder" | NG PowerShell+Jira automation, Jingle stack; do NOT claim agentic AI track record |
| Energy / grid / VPP / DER (Leap, etc.) | "Regulated grid infrastructure + AI-augmented operations" | NG AMI smart meter platform + AI-augmented automation; bridge to grid-flexibility / DER orchestration is adjacent, not direct VPP product experience |
| Payments infrastructure / interbank networks | "Co-architect of national interbank payment network at central bank's table — equivalent in function to Visa BankNet / Mastercard's network at country scale" | Infotech VP national card network work; defensible per comp doc. Decodes "national card network" for non-payments readers and signals magnitude. |

Document the bridge used in the Phase 1 strategy. Validation verifies the bridge appears in every section it should.

---

## Modern ATS reality (validated 2026)

- Modern ATS (Workday, Greenhouse, Ashby, Lever, plus AI-screening layers like Eightfold/HireVue) generate vector embeddings of resume + JD and compute semantic similarity — not exact keyword matching. ~78% of initial screenings now use NLP-based semantic matching.
- Keyword stuffing is actively penalized — repeating terms unnaturally lowers the score.
- What wins: contextual demonstration of skills through achievement bullets, not labels in a list.
- Knock-out filters (location, citizenship, YOE, direct-reports) fire before the AI score is even calculated. Missing a knock-out = automatic reject.
- Older parsers still scan skim zones for exact-string keywords. Recruiter Boolean searches still hit on exact strings.

The two screens we must clear:
1. **AI/ATS screen** (automated parsing + scoring against the JD before any human sees the resume)
2. **Recruiter 6-second scan** (human eyepath across page 1 to decide click-into vs discard)

Both must pass or no interview.

---

## Skim zones vs narrative zones (the core conflict resolution)

The conflict between ATS keyword surface and 6-second scan readability is resolved by zone:

- **Narrative zones (Summary, role scope lines, bullets):** clean prose, achievement-driven, concrete numbers, max 1-2 keywords per natural construction. Demonstration over labeling. NEVER stuff keywords here.
- **Skim zones (Core Competencies, Tools & Technologies, Certifications):** carry exact JD keyword surface. Stuffing acceptable here. Recruiter Boolean and older ATS parsers scan these.

This zone discipline alone resolves most ATS-vs-scan trade-offs.

---

## Tailor flavor by company stage (use as a check, NOT as the starting point)

After the Phase 1 strategy is written, this table sanity-checks that the tailoring emphasis matches the recruiter type at the company stage:

| Stage | Recruiter type | What dominates the tailoring |
|---|---|---|
| Series A (≤100 ppl) | Founder review | Cover letter + summary punch + Independent Ventures lead with Jingle/Lighthouse working apps; mission fit |
| Mid-stage SaaS (100-1K) | Hiring manager review | Bullets + Core Competencies with agile/B2B SaaS keywords; platform thinking; KPIs |
| F500 corporate (5K+) | ATS keyword surface + recruiter scan | Skim zones heavy; narrative tight; scale signals; regulated-industry credibility |
| FAANG / Big Tech | Bar-raiser interview prep | Bullets must mirror leadership principles; technical depth surfaced; data rigor |

Note: this flavor table is a sanity check applied AFTER the JD-priority strategy. It is NOT the starting point. Starting from flavor produces a stage-template tailoring that may miss the actual JD priorities.

---

## Save format and naming convention

Filename: `resumes/Maz_Mavvaj_[Title]_[Company].docx`

Examples currently in use: `Maz_Mavvaj_Sr_PM_Leap.docx`, `Maz_Mavvaj_Director_PM_Customer_io.docx`, etc.

Current canonical master: `resumes/Maz_Mavvaj_Director_Resume_FINAL5_4.docx` (and `.md` markdown copy for fast reading during Phase 1). Draft candidate `FINAL5_5.docx` exists and is being built up — when promoted to canonical master, references here will switch and a `.md` companion will be needed.

After save, immediately open `resume-validation.md` and run every check.
