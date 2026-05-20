# Tailor Checklist

Last updated: 2026-04-27

The 1-page operational runbook for tailoring a resume to a JD. Open this file at the start of every tailor and follow each phase in order. Target: complete the full sequence in 60 minutes per role.

The full framework lives in `job-search-strategy.md` Rubric 2. The career-history constraints (hard locks, promotion rule, interview-only material table) live in `Maz_Career_Background_Comprehensive.md`. This file is the executable checklist.

---

## Phase 1 — JD reconnaissance (15 min)

- [ ] Pull JD body from canonical source (company ATS like Ashby HQ / Greenhouse / Lever / Workday). LinkedIn abbreviations are not enough.
- [ ] Extract **must-haves** (hard requirements: years, skills, scope, domain)
- [ ] Extract **nice-to-haves** (preferred qualifications)
- [ ] Extract **knock-outs** (location, citizenship, recent direct-reports, hard YOE bar)
- [ ] Extract **culture cues** (founder language, mission framing, brand vibe)
- [ ] Detect company stage: Series A (≤100 ppl) / Mid-stage SaaS (100-1K) / F500 (5K+) / FAANG
- [ ] Detect application volume signal (45 applicants vs 200+)
- [ ] Map each must-have to one of the 11 pillars (1:1 where possible)
- [ ] Flag must-haves with **no pillar match** — these determine pursue-or-skip judgment
- [ ] **Identify domain-bridging framing needed** (per the bridging playbook in `job-search-strategy.md` Rubric 2). Example: waste tech → "B2B SaaS marketplace"; telehealth → "regulated infrastructure"; energy exchange → "regulated payments + energy intersection."
- [ ] **Bridge sweep — list every resume section the bridge framing applies to.** Typically: Summary, VP/Director scope lines, relevant bullets where the underlying story is the same multi-sided / regulated / consolidation pattern. Write the list down so Phase 4 can verify consistency.

## Phase 2 — Tailor flavor (5 min)

Pick by stage:

| Stage | Optimize for | What dominates |
|---|---|---|
| Series A (≤100 ppl) | Founder review, narrative quality, mission fit, builder identity | Cover letter + summary punch + Independent Ventures lead with Jingle/Lighthouse working apps |
| Mid-stage SaaS (100-1K) | Hiring manager review, platform thinking, agile delivery, KPIs | Bullets + Core Competencies with agile/B2B SaaS keywords |
| F500 corporate (5K+) | ATS keyword surface + recruiter scan, scale signals, regulated-industry credibility | Skim zones heavy; narrative tight |
| FAANG / Big Tech | Bar-raiser interview prep, principles match (Amazon LP / Meta XFN), data rigor | Bullets must mirror leadership principles, technical depth surfaced |

- [ ] Flavor selected: ____________

## Phase 3 — Tailor (30 min)

Zone discipline:
- **Narrative zones (Summary, scope lines, bullets):** clean prose, hard numbers, max 1-2 keywords per natural construction. Demonstration over labeling. NEVER stuff keywords here.
- **Skim zones (Core Competencies, Tools & Technologies, Certifications):** carry exact JD keyword surface. Stuffing acceptable here.

Section work:
- [ ] **Title alignment:** match JD's title verbatim where defensible (functional descriptor, no payroll inflation)
- [ ] **Summary:** 3-4 clean sentences, hard numbers, brand line at end intact
- [ ] **Scope lines:** tight, JD-relevant lens, same facts, no kitchen-sink keyword piles
- [ ] **Bullets:** reorder, replace, or promote interview-only material per the promotion rule (see comprehensive doc). Every modified bullet must pass 10-point framework (Phase 4).
- [ ] **Independent Ventures order:**
  - Jingle first when JD wants player-coach / hands-on / live builder
  - Lighthouse first when JD wants operational visibility / risk / governance / PMO
- [ ] **Core Competencies:** stuff with JD's exact must-have keywords. Drop master entries that don't fit. Add JD-aligned slots.
- [ ] **Tools & Technologies:** reorder to lead with JD-relevant tools. Stuffing acceptable.
- [ ] **Certifications:** reorder to lead with JD-relevant certs.

Hard locks (verify none violated):
- [ ] Hard numbers preserved verbatim
- [ ] Companies, dates, chronology unchanged
- [ ] No "Director" payroll-title claim at NG
- [ ] Pillar identity respected — no claims of pillars Maz doesn't have

Promotion check (if any interview-only material promoted):
- [ ] (a) Strengthens match to JD must-have OR nice-to-have
- [ ] (b) Passes 10-point bullet framework
- [ ] (c) Doesn't displace a stronger bullet for THIS JD (displacement test)

Domain-bridging (if applied, document the framing used):
- [ ] Bridge framing: ____________ → ____________

Save:
- [ ] Filename: `resumes/Maz_Mavvaj_[Title]_[Company].docx`

## Phase 4 — QA gate (15 min, ship-or-don't)

Resume-level checks. Run in order. If all pass, ship. Do not iterate further on phrasing after this gate.

- [ ] **6-second mock scan:** read top of page 1 (name, title, current company, top 3 bullets) in 6 seconds. Can you state the punchline?
- [ ] **JD must-have coverage check:** every must-have demonstrated somewhere (bullet, scope line, or skim zone)
- [ ] **Bridge consistency check:** the domain-bridging framing identified in Phase 1 appears in every section on the bridge sweep list (not just one spot). Catches the failure mode where the bridge lands in the summary but not in scope lines or bullets where the same story lives.
- [ ] **Knock-out check:** location, citizenship, YOE, direct-reports — all met
- [ ] **10-point bullet framework on every modified bullet:**
  1. Outcome first
  2. Scale signal
  3. So what
  4. One idea
  5. Scannable (1.5 lines max)
  6. Executive tone
  7. Decision-maker signal
  8. Altitude
  9. Defensible
  10. Pattern reinforcement
- [ ] **Length:** 1-2 pages
- [ ] **Trim 10%:** every word earns its place
- [ ] **Side-by-side diff with reasoning** presented to user (master vs tailored). **Use the canonical format below — no exceptions, no font experiments.**

  **Canonical side-by-side format** (locked 2026-04-27, validated to render correctly in Maz's Claude Code desktop renderer):
  - **Removed text:** wrap in `~~***[...]***~~` — produces strikethrough + bold-italic + square brackets
  - **Added text:** wrap in `***[...]***` — produces bold-italic + square brackets
  - **Table structure:** 5 columns — `# | Section | Master | [Tailored Company] | Why`
  - **Cell content:** show only the sections that changed; drop unchanged rows. Within each cell, show enough surrounding context for the reader to locate the change, but trim aggressively (`...` is fine for unchanged middle).
  - **No monospace/code style** (changes the font, dilutes signal). **No HTML tags** (`<u>`, `<mark>`, `<span>` — none render in Maz's viewer). **No yellow background** (renderer doesn't support it).

  Example row that demonstrates the format:

  ```
  | 1 | Summary | ...stalled ~~***[fintech startup]***~~; scaled it from 10K... | ...stalled ***[payments venture]***; scaled it from 10K... | Generalizes industry framing for hidden employer. |
  ```
- [ ] **Apply user feedback if any.**
- [ ] **SHIP.** Do not iterate further on phrasing after this point.

## Phase 5 — Three-touch (post-submit)

- [ ] ATS submit
- [ ] HM/founder LinkedIn DM (use HM identification from leadership lookup)
- [ ] Referral hunt (1st/2nd degree connection at company)
- [ ] Move row from `candidates.md` to `applications.md`
- [ ] Add outreach touches to `outreach.md`
- [ ] Update `weekly-metrics.md`

---

## Notes for self

- The two screens we must clear: AI/ATS (semantic NLP, not exact keywords; ~78% use semantic matching as of 2026) and human recruiter 6-second scan. Both must pass.
- Modern ATS penalizes keyword stuffing. Skim zones (not narrative zones) are where keyword surface lives.
- Knock-out filters fire before the AI score. Missing a knock-out = automatic reject.
- The "ship gate" is real. If Phase 4 passes, do not keep tweaking summary phrasings. Move to Phase 5.
