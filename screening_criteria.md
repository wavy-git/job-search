# Screening Criteria

Last updated: 2026-05-16

**Single source of truth for screening JDs.** Read this at the start of any screening session. Other docs (`job-search-strategy.md`, `Maz_Career_Background_Comprehensive.md`, `tailor-checklist.md`) defer to this file for screening rules.

This file is a living document. Items are added, removed, or moved between High and Low as the user revises preferences.

---

## Score bands (1-5)

- **5** — Top fit. Strong on most High items, no knock-outs. Pursue immediately.
- **4** — Good fit. Strong on most High items, minor friction. Pursue.
- **3** — Moderate fit. Mixed Highs, real friction. Hold or pursue with warm path.
- **2** — Weak fit. Multiple Highs missing or stacked friction. Archive-review.
- **1** — Poor fit. Hard knock-out OR multiple disqualifiers. Drop.

A single hard knock-out caps the score at 1 regardless of other strengths.

---

## Constraints (the user's hard parameters)

### Compensation
- US Director / Head base **target**: $200K+ (aspirational, not a gate)
- US Director / Head base **hard floor**: **$180K**. If JD lists a comp range and the entire range is below $180K → drop. If the range straddles $180K, pass through. If unlisted, pass through and verify at apply time.
- Portugal / Spain Director base floor: €120K-€140K (local market rate)
- Total comp matters more than base alone.

### Locations
- Remote-first US (priority)
- Acceptable metros: Greater Philadelphia (60-mi radius from Marlton NJ), NYC, Seattle, SF Bay, LA
- Portugal (Lisbon) if extraordinary
- Spain (Madrid, Barcelona) if extraordinary
- **Not** Canada (CAD comp typically below floor)
- Within Greater Philly: Western suburbs (Berwyn / Malvern / Radnor) carry soft friction (inconvenient commute)

### Wanted role titles (at the right altitude / comp)
**Manager, Senior Manager, Lead, Principal, Director, Head, Senior, VP** of:
- Product
- Innovation
- Operations
- Strategy / Strategic Initiatives
- Transformation / Business Transformation / Digital Transformation
- Process Excellence / Process Improvement / Continuous Improvement / Lean
- Platform
- Program Management / PMO / Project Management
- Product Operations
- Delivery / Implementation (at Director+ altitude)
- General Manager / Chief of Staff
- Head of Business / Business Head

### Function knock-outs (drop)
- Marketing / Agency PMO / Adtech-pipeline-PMO
- Engineering Management
- Customer Success
- Pure coordinator IC roles regardless of title (JD reads "support / facilitate / chair sync" and altitude is IC at small co with comp at floor)

### 11 background pillars
The user activates a JD when at least 2 of these match (direct or adjacent). Full descriptions in `Maz_Career_Background_Comprehensive.md`.
1. Payments and financial services infrastructure
2. Regulated industry operations
3. B2B2C platform architecture
4. Operational turnaround and scaling under pressure
5. 0-to-1 product creation, first-to-market
6. Operational intelligence and executive translation
7. Process and program transformation (PMO creation, Lean flow, Kanban)
8. Cross-functional leadership at scale
9. Technical depth and architecture credibility
10. Strategic partnership and vendor negotiation
11. Founder/builder identity and AI-augmented automation

---

## High impact (these decide fit)

1. **Domain match** — payments / fintech / regulated infra / B2B SaaS at scale. JD primary domain language.
2. **Function match** — title is in the Wanted list above; function is not in the Function knock-outs list.
3. **Altitude** — Sr PM / Sr Manager / Principal / Director / Head / Sr Director / VP / MD. Below Sr PM = drop. For Program Management / PMO / Project Management: altitude floor is Director / Head / VP at any size, OR Sr Manager / Principal at big-tech (Amazon / Apple / Microsoft / Google / Meta) where comp is typically $200-300K.
4. **Comp** — $180K base floor (US). If listed range entirely below floor → drop.
5. **Domain knock-outs (auto-drop):**
   - Security / cybersec (Defender / MDR / MSSP / PTaaS / SASE / SIEM / threat detection)
   - Tax / accounting (tax tech / revenue accounting / ASC 606 / financial accounting / audit)
   - FP&A / financial planning / finance PMO specialty
   - Q2C / NetSuite / AR automation / billing-systems specialty
   - Biotech / pharma R&D
   - Healthcare-product / telehealth domain expertise required
   - Waste-industry domain expertise required
6. **Direct-reports clause** — JD says "must currently manage X PMs" or "5+ years recent direct PM management required, no flex" → drop. Soft mentor / coach language → friction, not knock-out. (User's last direct people management ended 2015.)
7. **Location** — must be in the Acceptable list above. Onsite outside acceptable metros → drop.
8. **Posting status** — must be open. LinkedIn "No longer accepting applications" red badge → drop as `stale`.
9. **Posted recency** — within last 7 days. Older = drop unless flagged for retroactive interest.
10. **Pillar match** — JD activates ≥2 of the 11 background pillars.
11. **JD red-flag verbs** — primary verbs that signal coordinator / order-taker function: "gathering requirements," "facilitate meetings," "support PMs," "translate business asks into requirements." Distinct from regulatory translation (acceptable, e.g., "translate regulatory requirements into product requirements").
12. **Recruiter-Boolean filters** — keyword gates the user cannot honestly carry: FAANG-internal pedigree, NetSuite / Q2C deep specialist, Tamarac, ASC 606 deep specialist, Bedrock / Vertex AI 3+ yrs, MSSP / MDR / SASE deep specialist, active Secret/Top Secret clearance, biotech/pharma PM history, federal CMS/CDC contract PM history, gaming dev mgmt, real-estate MLS. (Note: user holds PMP — "PMP required" is a credential match, not a friction.)
13. **Domain bridge** — if pillar match is partial, is there a defensible bridge story without fabrication? If no defensible story exists, score drops 1-2 bands.

---

## Low impact (background context, not decision drivers)

1. Tier label (Tier A/B/C…) — organizational tagging only, see `target-companies.md`.
2. Specific tech stack mentioned (AWS / GCP / Salesforce / Snowflake) — cosmetic.
3. Source tag (linkedin / scanner / manual / recruiter-fronted) — provenance, not fit.
4. Company size bucket S/M/L — already absorbed into altitude judgment.
5. Score number itself when looking at an entry retroactively.
6. Direct ATS vs LinkedIn aggregator — matters for application URL, not fit.
7. Hidden-employer aggregator (Jobgether, RemoteHunter, recruiter-fronted) — flag at apply time.
8. Soft mgmt language without explicit no-flex.
9. Applicant count on LinkedIn — apply-time competition, not fit.
10. Western Philly suburbs (within radius but inconvenient) — soft friction.
11. Company stage survival risk (pre-seed / seed) — apply-time concern.
12. Domain bridge complexity (vs no bridge at all) — tailoring concern.

---

## Procedure

1. **Read the JD.** Fetch and save canonical body to `outputs/jds/{date}-{company-shorthand}-{role-shorthand}.md` for offline access. Header block: url, company, title, location, fetched_at, posting_status.
2. **Read source materials** if not already loaded: `resumes/Maz_Mavvaj_Director_Resume_FINAL5_5.md` (current canonical master) and `Maz_Career_Background_Comprehensive.md`. FINAL5_4 archived as previous canonical version.
3. **Walk the High items.** Identify which trigger as knock-outs, which are clean fits, which carry friction.
4. **Note any Low items** surfacing in this specific JD (rare).
5. **Write a 1-2 sentence judgment note**: dominant fit signal + dominant friction signal.
6. **Assign 1-5 score** per the bands above.
7. **Place in `candidates.json`**:
   - **List A — Realistic Baby Step:** Manager / Sr Manager / Principal at any size; Director / Head at S (<500).
   - **List B — Realistic Stretched:** Director / Head at M (500-5K) or L (5K+); Sr Director / VP / MD at any size.

---

## Maintenance

When the user adds, removes, or reweights a rule, update this file first. Other docs reference this file rather than duplicating its content. If a rule appears here AND in another doc, this file is authoritative.
