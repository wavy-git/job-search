# Resume Tailoring Instructions

Last updated: 2026-05-19

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
   - `resumes/Maz_Mavvaj_Director_Resume_FINAL5_5.md` (current canonical master, full body — every section). FINAL5_4 is archived as the previous canonical version.
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
   - Which sections of the resume highlight which JD qualification (e.g., Header positioning block carries #1-#2 industries/disciplines; Summary intro line reinforces #1-#2 with minor edits; new S2 sentence covers #3-#5; 3 Summary bullets carry hard-number punches; Bullet X in NG section covers #6; Core Competencies skim zone carries #2 and #6)
   - Which reserve material gets promoted, where, and why (cite (a)/(b)/(c) of promotion rule explicitly)
   - Which bridge framings are needed (cite domain-bridging playbook entries)
   - Which gaps stay as gaps (don't fabricate; document and accept)

7. **Full-resume audit before Phase 2.** Walk all 9 sections (Header positioning block, title, summary, scope lines, bullets, IV order, Core Competencies, Tools & Technologies, Certifications) and document which need changes per the strategy and which stay as master. Surface this list in the Phase 1 strategy output.

8. **Only after the strategy is written do you start Phase 2.**

---

## Phase 2: Tailor by section

Apply the strategy from Phase 1 to each section in the order below. Every change must be earned by the strategy — no edits without strategy backing.

**Zone discipline:**
- **Narrative zones** (Summary, scope lines, bullets): clean prose, hard numbers, demonstration over labeling. Do not stuff keywords.
- **Hybrid zone — Header positioning block** (Phase 2.1): compact prose surface that IS designed to carry keyword density for AI screening.
- **Skim zones** (Core Competencies, Tools & Technologies, Certifications): carry exact JD keyword surface. Stuffing acceptable here.

**Specificity in narrative zones (additional rule).** Every noun in narrative zones needs concrete grounding. Vague abstracts ("prototypes," "workflows," "platforms," "outcomes") without specification fail. Test: can the reader picture the work from the words alone? If they ask "what specifically?" the phrase is too vague.

### Phase 2.1: Header positioning block (NEW)

The 3-line block under Maz's contact info is fully tailorable per JD. No hard locks. Run BEFORE Summary.

Master (FINAL5_5):
- Line 1: `Business & Technology Leader`
- Line 2: `Product • Operations • Engineering • Monetization`
- Line 3: `AI-Augmented Ops • Regulated Platforms • FinTech • Telecom • Energy`

Rules:
- **Line 1 (role identity):** swap when JD calls for a different identity ("Product Leader," "Operations Executive," "Transformation Leader"). Defensible per comp doc.
- **Line 2 (disciplines):** reorder/swap to lead with JD's primary function. Drop irrelevant slots; replace with JD-relevant disciplines defensible per comp doc.
- **Line 3 (industries):** reorder/swap to lead with JD's primary industry. Drop irrelevant tags; add JD-relevant industry tags defensible per comp doc.

This block is a prime AI-screening keyword location — above the fold, high keyword density per square inch. Place JD's specific industry/discipline keywords here first.

### Phase 2.2: Summary (REVISED)

Master structure (FINAL5_5): intro line + S2 expansion sentence + 3 bullets + closing identity line. Do NOT rewrite the structure.

- **S1 (intro line):** minor edits only (not rewrite). Must carry the **#1 JD priority**; may carry more if the master sentence's structure allows natural minor edits. No upper cap.
- **S2 (expansion sentence):** write a single new sentence carrying whatever S1 didn't, up to **S1 + S2 combined = 4-5 of the top 5 priorities**. **Must read as a coherent sentence, not a comma-list.** If a priority can't fit naturally, drop it and let it land in a bullet, header, or skim zone.
- **3 bullets:** minor edits only (not rewrite), each stays ≤1 line. If a bullet is clearly off vs JD priorities, you MAY swap one for a promoted bullet from comprehensive background. **Limit: 1 promotion in Summary bullets per tailored resume** (independent of Phase 2.3 promotion).
- **Closing identity line:** do not change. Brand identity.

**Fluency protection:** never sacrifice the fluency or power of S1 or S2 to cram priorities in. If S2 reads stuffed, drop a priority and reposition it elsewhere on page 1. Per Phase 2.4, flag the trade-off rather than silently breaking fluency.

### Phase 2.3: Career progression — titles, scope, bullets (REVISED)

Applies to all body roles (NG, Comcast, Infotech VP/Director/Manager/Developer).

- **Role titles:** match JD's title verbatim where defensible (functional descriptor, no payroll inflation). Hard lock: never claim "Director" as NG payroll title.
- **Scope lines:** freely tailorable. Same facts, JD-relevant lens. Avoid keyword piles.
- **Bullets:** minor edits only (not rewrite). Strong reason required. Strong reasons include:
  - JD-cited tool/term not in current wording (swap a noun)
  - Verb-mode mismatch where the mismatch is **severe** (e.g., ownership-vs-collaboration). Skip when borderline (ownership-vs-execution).
  - Reordering bullet sequence within a role to lead with JD-relevant outcome
- **Bullet promotion (body):** AT MOST 1 promoted bullet across the entire body per tailored resume. Run detailed analysis first. **This is independent of Phase 2.2's Summary promotion — so up to 2 total promotions per tailored resume (1 Summary + 1 body).**

**Bullet count discipline (FINAL5_5):** NG=5, Comcast=4, Infotech VP=5, Director=3, Manager=2, Developer=2. Master is denser than FINAL5_4; most tailorings swap/reorder, rarely add. Flag any count change in the strategy and in the diff. No silent count changes.

Every modified bullet must pass the 10-point bullet framework (`resume-validation.md`).

### Phase 2.4: Flag when blind rule-following misses something important (NEW)

These rules are guardrails, not a script. If applying them mechanically would miss a key JD signal — **stop and flag to the user**. Examples:
- A JD priority that cannot be reinforced by Summary S1 edits OR a single new S2 sentence (might need a 2nd promotion — flag, don't silently break the limit).
- A JD verb mode that conflicts with multiple bullets across a role section (the pattern is wrong, not just one bullet — flag).
- A JD-cited domain/tool/term whose closest defensible bridge isn't in the playbook (flag, propose framing, get confirmation).

Surface conflicts in the Phase 1 strategy OR mid-Phase-2 when discovered.

### Phase 2.5: Independent Ventures (UPDATED)

Master has 3 ventures + 4-line builder-identity intro paragraph. Keep the intro intact for senior-leadership / Series A / founder JDs. Trim only for tactical IC tailorings (rare).

Ordering:
- **MailFlow first** when JD wants agentic AI / autonomous LLM systems / AI-augmented automation depth (defensible per Sonnet+Haiku tiered routing).
- **Jingle first** when JD wants player-coach / hands-on / live builder / cross-platform consumer.
- **Lighthouse first** when JD wants operational visibility / risk / governance / PMO.
- **Default** (no pull): Lighthouse → Jingle → MailFlow.

### Phase 2.6: Core Competencies (skim zone, UPDATED)

Master = 8 fixed slots (FINAL5_5). Nothing is strictly hard-locked, but each slot has a reason and isn't easily replaced. Tailoring allowed.

Master slots:
- Operational Turnaround & Transformation
- Executive Communication & Stakeholder Alignment
- Product Strategy, Roadmapping, Go-to-Market and P&L
- Vendor & Partnership Management
- Regulated Industry Ops (Energy, Utilities, FinTech, PCI-DSS)
- KPI/OKR-Driven Decision Making & Analytics
- Cross-Functional Team Leadership (50+ direct/indirect)
- AI-Augmented Operations & Process Automation

Rules:
- **Count stays at 8 slots.** Don't grow or shrink.
- Replace slots with JD's exact must-have keywords when needed. Source from `Maz_Career_Background_Comprehensive.md` § PROMOTIONAL RESERVE when keyword isn't on master but underlying capability is real per comp doc.
- `AI-Augmented Operations & Process Automation` is an identity slot anchored to MailFlow + Jingle in IV. Keep present unless JD has zero AI/automation surface.
- Document each replacement in Phase 1 strategy: which JD keyword drove it, where in the comp doc the capability is anchored.

### Phase 2.7: Tools & Technologies (skim zone, UPDATED)

Master = 6 categorized rows (FINAL5_5).

Master:
- `Agentic AI, LLMs & GenAI, Claude Code, Anthropic API, MCP`
- `Analytics & BI: Tableau, Power BI, eazyBI, SQL`
- `Jira & Jira Align, Confluence, Smartsheet, Excel, ServiceNow`
- `ANSI C, Java, Python, Swift, PowerShell, Embedded Systems`
- `GitHub/Git, GitHub Actions, REST APIs, Xcode, TestFlight`
- `Cloud Platforms: Cloudflare, AWS`

Rules:
- Reorder items WITHIN a row to lead with JD-relevant items.
- Reorder ROWS to lead with the JD-relevant category (AI JDs → row 1 [master default]; payments → rows 3-4; PMO/ops → row 3).
- Tools/vendor names not on master may be pulled from § PROMOTIONAL RESERVE (Ingenico, Gemalto, Thales, Temenos, "predictive analytics," "PCI-DSS," "payment switching") when JD references them or weights the underlying capability.
- Primary AI-screening keyword location alongside Header. Surface JD's specific tool names here, not in narrative.

### Phase 2.8: Certifications & Honors (LOCKED)

Master list (FINAL5_5):
- Beta Gamma Sigma Honors Society
- AWS Cloud Practitioner
- CPISI (Certified Card Payment Security Implementor, SISA)
- CSCIP/Payments (Certified Smart Card Industry Professional)
- PMP (Project Management Professional, PMI)
- CSPO (Certified Scrum Product Owner, Scrum Alliance)
- POPM (Product Owner / Product Manager, SAFe)
- SA (Scaled Agilist, SAFe)

Lock as-is. Do not tailor unless a major credential is genuinely missing OR JD knock-out requires reordering. Beta Gamma Sigma carries signal for F500 / consulting / MBA-pedigree JDs; deprioritize for builder-engineer JDs.

---

**Hard locks** (verify none violated; full list in `Maz_Career_Background_Comprehensive.md` § Hard Locks):
- Hard numbers preserved verbatim
- Companies, dates, employment facts unchanged (chronological structure)
- No "Director" payroll-title claim at NG
- Pillar identity respected (no claims of pillars Maz doesn't have)
- **Agentic AI:** defensible as a master claim anchored to MailFlow + Jingle in IV. Do NOT claim agentic AI as enterprise-scale production track record at NG or Comcast.

**Save** as `resumes/Maz_Mavvaj_[Title]_[Company].docx`. Then run `resume-validation.md`.

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

Current canonical master: `resumes/Maz_Mavvaj_Director_Resume_FINAL5_5.docx` (and `.md` markdown copy for fast reading during Phase 1). FINAL5_4 archived as previous canonical version.

After save, immediately open `resume-validation.md` and run every check.
