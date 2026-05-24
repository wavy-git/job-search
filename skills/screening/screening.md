# Screening

The skill that takes in-zone JDs (already past `skills/sourcing/`) and evaluates fit + chances of getting the interview. Output: a ranked judgment of which are worth pursuing.

Answers: **given this is in my career zone, what are my chances?**

Does NOT re-check whether the JD is in zone — sourcing already answered. Does NOT collect from channels.

---

## Inclusion test

> **PASSES IF:** evaluation logic, scoring framework, or fit-assessment procedure for in-zone JDs — answers "how compatible is this with my background, and what are my chances?"
>
> **FAILS IF:** channel collection or the in-zone filter itself (→ `skills/sourcing/`); Maz's career-zone parameters (→ `me/constraints.md`); per-JD tailoring (→ `skills/tailoring/`); outreach drafts (→ `skills/outreach/`); interview prep (→ `skills/interviewing/`); operational state (→ pipeline files); fact about Maz (→ `me/background.md`).

---

## Inputs

- In-zone JD body (from `outputs/jds/`)
- `me/background.md` (for pillar match evidence)
- `me/voice.md` (for don't-claim list to evaluate domain bridge feasibility)
- The pillar framework (defined below)
- The JD red-flag verbs list (defined below)
- Score band definitions (defined below)

## Outputs

- A 1-5 score per JD
- A 1-2 sentence judgment note (dominant fit signal + dominant friction signal)
- Pipeline row updated with score, judgment, and List assignment (List A = realistic baby step; List B = realistic stretched)

---

## 11 background pillars (capability inventory used for fit matching)

Maz's career capabilities clustered into 11 pillars. A JD activates a pillar when its requirements/responsibilities map to the evidence for that pillar (direct match, adjacent, or via defensible bridge per `me/voice.md`).

1. **Payments and financial services infrastructure** — national card network, 30+ FI integrations, PCI-DSS championing, central bank seat, 1M+ terminals, 150M+ transactions, transaction routing/settlement/security frameworks.
2. **Regulated industry operations** — NG utility multi-state (NY/MA), Infotech national payments regulatory work, PCI-DSS championing. (Regulated = **Utilities + Fintech (PCI-DSS) only.** NOT Government, NOT Healthcare.)
3. **B2B2C platform architecture** — multi-bank terminal; AMI platform supporting 8 downstream teams; NCC routing across multiple banks; PSP serving merchants who serve consumers.
4. **Operational turnaround and scaling under pressure** — 10K → 120K merchants in 18 months; NCC 20 → 5,000+; Comcast 200% throughput at 50% fewer resources; culture transformation.
5. **0-to-1 product creation, first-to-market** — first remote terminal mgmt nationwide; first domestic POS on national switch; first config-driven payment platform; first bank-independent terminal; conceived B2C payment services venture.
6. **Operational intelligence and executive translation** — $2M vendor accountability framework reframing; Log4Shell crisis analytics; Comcast analytics platform; NG defect tracking; Tableau / Power BI / SQL fluency.
7. **Process and program transformation** — Comcast Lean flow / WIP / quality gates (not agile); CCRE change management; NG Feature Flow Kanban; lead/cycle time introduction; PMO creation at Infotech Director.
8. **Cross-functional leadership at scale** — 12 direct reports + 50+ employees + 700+ field techs at VP; 7 eng teams / 40+ engineers at Director; 30-person team supporting 8 downstream teams at NG.
9. **Technical depth and architecture credibility** — BS Software Engineering; started as developer; Python / PowerShell / Java / ANSI C / embedded fluency; holds architecture discussions with engineering.
10. **Strategic partnership and vendor negotiation** — Ingenico software-ownership negotiation (NCC); Gemalto / Thales / Temenos partnerships; L+G vendor accountability framework.
11. **Founder / builder identity and AI-augmented automation** — conceived B2C payment services venture at parent company before being asked to take charge; founded Seagull Cybernetics 2022; Project Lighthouse working app with PrioritEyes live; Jingle live on TestFlight; Libz under Liberté; MailFlow autonomous-agent system; AI-augmented PowerShell + Jira automation at NG (feature-documentation scope specifically); CCRE change management built unprompted; Log4Shell crisis analytics built without being asked.

### Context multipliers (signal-boosters when present)
- EMEA / international / multilingual (Farsi native; multi-region experience across Southwest Asia / N. Africa / W. Europe)
- Industry-shaping / regulatory framework work (drove PCI-DSS national adoption, formal central bank seat)

### Pillar match threshold
- A JD must activate **≥2 of the 11 pillars** (direct, adjacent, or via defensible bridge) to score above 2.
- If pillar match is partial (one direct hit + a defensible bridge for the other), apply bridge framing per `me/voice.md` § Don't-claim list + bridges.
- If no defensible bridge exists for a missing pillar, score drops 1-2 bands.

---

## JD red-flag verbs (signal coordinator / order-taker work, not decision-maker altitude)

If these verbs DOMINATE the JD's primary responsibilities, downgrade or drop:

- "Gathering requirements."
- "Facilitate meetings."
- "Support PMs."
- "Translate business asks into requirements."

**Exception:** regulatory translation is acceptable signal (e.g., "translate regulatory requirements into product requirements" — that's policy-to-product mapping, not coordinator work).

**[PLACEHOLDER from `me/constraints.md` audit 2026-05-24 — scrutinize during comprehensive screening audit, do not delete until reviewed.]** **Coordinator-IC multi-signal pattern:** if a JD has ALL of (a) red-flag verbs dominating responsibilities, AND (b) IC altitude (no team or scope ownership), AND (c) small company, AND (d) comp at the $180K floor (not significantly above), apply the cap rule (score 1, drop). This is stronger than the verb-dominance downgrade above and was moved here from constraints during the 2026-05-24 audit.

---

## Score bands (1-5)

After applying the pillar match + red-flag check + friction assessment:

- **5 — Top fit.** ≥3 pillars activated directly. No knock-outs. Strong domain fit. Pursue immediately.
- **4 — Good fit.** ≥2 pillars activated. Minor friction (e.g., applicant count high but warm path possible). Pursue.
- **3 — Moderate fit.** ≥2 pillars activated (one via bridge). Real friction (e.g., direct-reports soft preference, location friction, comp ambiguous). Hold or pursue with warm path.
- **2 — Weak fit.** Multiple High-impact items missing OR stacked friction (no warm path + high applicant count + bridged pillars). Archive-review.
- **1 — Poor fit.** Hard knock-out missed by sourcing OR multiple disqualifiers. Drop. (Should be rare since sourcing handles knock-outs; if a knock-out is found here, also surface to sourcing for filter tightening.)

### Cap rule
A single hard knock-out caps the score at 1, regardless of other strengths. (Hard knock-outs should already be caught at sourcing; this cap is a safety net.)

---

## Friction factors (lower the score within a band)

- **High applicant count** (200+ on LinkedIn at evaluation time): drop ~0.5 band unless a warm path exists.
- **Hidden employer** (recruiter-fronted: Forsyth Barnes, Wayoh, Ladders, RemoteHunter, Recruiting from Scratch): drop ~0.5 band unless the recruiter has placed Maz-adjacent roles before.
- **No HM identifiable** for warm-path DM: drop ~0.5 band.
- **Stale-employer-already-applied** (already applied to a role at this co recently): drop ~1 band.
- **Comp ambiguous and likely below floor** (no listed range, company stage suggests below-floor): drop ~0.5 band.
- **Location friction** (in-zone but inconvenient — Western Philly suburbs, hybrid requiring relocation): drop ~0.5 band.
- **[PLACEHOLDER from `me/constraints.md` audit 2026-05-24 — scrutinize during comprehensive screening audit, do not delete until reviewed.]** **Soft people-leadership language** (JD uses "mentor," "coach," or "guide" the team instead of hard direct-management language, no formal direct-report requirement): drop ~0.5 band. Friction is no recent direct reports since 2015.
- **[PLACEHOLDER from `me/constraints.md` audit 2026-05-24 — scrutinize during comprehensive screening audit, do not delete until reviewed.]** **Posting age 8-14 days:** drop ~0.5 band (older posting = more applicants already submitted, lower response odds).

---

## Boost factors (raise the score within a band)

- **Warm path available** (1st/2nd LinkedIn connection at company; mutual contact; known HM): raise ~0.5 band.
- **HM is identifiable AND has builder/founder pattern** (like Maz): raise ~0.5 band; HM-pass odds improve significantly.
- **JD explicitly weights Maz's strongest pillars** (e.g., payments infrastructure + regulated industry ops + operational turnaround = bullseye match): raise ~0.5 band.
- **Low applicant count** (under 50 at evaluation): raise ~0.5 band.
- **Recent posting, niche domain**: raise ~0.5 band.

---

## Screening procedure (per in-zone JD)

1. **Read the JD body** (from `outputs/jds/<file>`).
2. **Identify the top 6 key qualifications** the hiring team and recruiter are looking for. Rank by importance to recruiter screen.
3. **Map each qualification to Maz's pillars** — direct match, adjacent match, or via defensible bridge (per `me/voice.md`).
4. **Note gaps** where no pillar or bridge applies. These are the disqualifiers if too many.
5. **Apply pillar match threshold** — at least 2 pillars activated to score above 2.
6. **Scan for JD red-flag verbs** dominating responsibilities. Downgrade if found.
7. **Apply friction + boost factors** to the base band score.
8. **Write 1-2 sentence judgment note:** dominant fit signal + dominant friction signal.
9. **Assign 1-5 score.**
10. **Place in pipeline:**
    - **List A — Realistic Baby Step:** Manager / Sr Manager / Principal at any size; Director / Head at S (<500 employees).
    - **List B — Realistic Stretched:** Director / Head at M (500-5K) or L (5K+); Sr Director / VP / MD at any size.
11. **Decision:**
    - Score 5: pursue immediately, tailor + three-touch.
    - Score 4: pursue, tailor + three-touch.
    - Score 3: hold for warm path; tailor only if warm path materializes.
    - Score 2: archive-review.
    - Score 1: drop. If a hard knock-out was missed by sourcing, surface to sourcing skill for filter tightening.

---

## Open / parked items

- Warm-path scoring as a separate signal layer (conceptually relevant — strategy doc says cold ATS converts 2-5%, referrals 20-40%). Could surface roles where Maz has a 1st/2nd connection at the company as a separate boost.
- Tier-A target company list (108 companies in `_archive/2026-05-20-rebuild/target-companies.md`) — referenced for warm-path and prioritization. Reactivation TBD.
- **[PLACEHOLDER from `me/constraints.md` audit 2026-05-24 — scrutinize during comprehensive screening audit, do not delete until reviewed.]** **Altitude signals not captured by `me/constraints.md`.** Constraints handles altitude via title prefix list + comp floor + function knock-outs only. Six altitude signals are NOT in constraints and may need handling here: scope (team size, budget, geographic reach), reporting line (proximity to CEO/CTO/CPO), decision authority (decide vs recommend vs facilitate), strategic vs tactical orientation, time horizon (years vs days), stakeholder altitude (C-suite, board, regulators). Evaluate during the screening audit: pillar expansion vs new friction factor vs new dedicated section.
