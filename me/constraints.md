# Maz Mavvaj — Constraints

Source of truth for what defines Maz's career zone. Used by `skills/sourcing/` to filter raw collections into the in-zone pool. A JD that fails any constraint here is out of zone — `skills/sourcing/` rejects it, regardless of any other strength.

This file answers ONE question only: **is this kind of job in my career zone?**

It does NOT score fit, evaluate chances, or rank in-zone candidates. That's `skills/screening/`.

---

## Inclusion test

> **PASSES IF:** it's a hard parameter that defines Maz's career zone — comp floor, locations, wanted title families, function knock-outs, domain knock-outs, direct-reports clause, posting state, recruiter-Boolean credentials he can't carry.
>
> **FAILS IF:** screening fit/chances logic (pillar match scoring, JD red-flag verbs, score bands → `skills/screening/`); fact about Maz (→ `me/background.md`); representation rule (→ `me/voice.md`); workflow (→ a skill); operational state (→ pipeline files); current-cycle strategic objectives (→ `pending.md`).

---

## Compensation

- **US base hard floor:** $180K. If the JD lists a comp range and the entire range is below $180K → out of zone. If the range straddles $180K, in-zone (verify at apply time). If unlisted, in-zone (verify at apply time).
- **US base target (aspirational, not a gate):** $200K+.
- **Portugal / Spain Director base floor:** €120K-€140K (local market rate).
- **Total comp** matters more than base alone at offer stage. For sourcing/screening, base floor governs.

---

## Locations

### In zone (US)
- Remote-first US (priority).
- Greater Philadelphia (60-mile radius from Marlton, NJ).
- NYC.
- Seattle.
- SF Bay Area.
- LA.

### In zone (EU, only if extraordinary)
- Portugal (Lisbon).
- Spain (Madrid, Barcelona).

### Soft friction (in zone but inconvenient)
- Western suburbs of Philly (Berwyn / Malvern / Radnor) — friction, not knock-out.

### Out of zone
- Canada (CAD comp typically below floor).
- Onsite outside the acceptable metros.

---

## Wanted role titles (in zone)

A JD's title must combine an acceptable seniority prefix with an acceptable functional family.

**Acceptable seniority prefixes:** Manager, Senior Manager, Lead, Principal, Director, Head, Senior Director, VP.

**Acceptable functional families:**
- Product
- Innovation
- Operations
- Strategy / Strategic Initiatives
- Transformation / Business Transformation / Digital Transformation
- Process Excellence / Process Improvement / Continuous Improvement / Lean
- Platform
- Program Management / PMO / Project Management
- Product Operations
- Delivery / Implementation (at Director+ altitude only)
- General Manager / Chief of Staff
- Head of Business / Business Head

### Altitude floor
- Below Senior Product Manager → out of zone.
- For Program Management / PMO / Project Management specifically: floor is Director / Head / VP at any company size, OR Senior Manager / Principal at big-tech (Amazon / Apple / Microsoft / Google / Meta) where comp typically lands $200-300K.

---

## Function knock-outs (auto-drop, out of zone)

- Marketing.
- Agency PMO / adtech-pipeline PMO.
- Engineering Management.
- Customer Success.
- Pure coordinator IC roles regardless of title (JD reads "support / facilitate / chair sync" and altitude is IC at small co with comp at floor).

---

## Domain knock-outs (auto-drop, out of zone)

- Security / cybersecurity products (Defender / MDR / MSSP / PTaaS / SASE / SIEM / threat detection).
- Tax / accounting (tax tech / revenue accounting / ASC 606 / financial accounting / audit).
- FP&A / financial planning / finance PMO specialty.
- Quote-to-Cash / NetSuite / AR automation / billing-systems specialty.
- Biotech / pharma R&D.
- Healthcare-product / telehealth domain expertise required.
- Waste-industry domain expertise required.

---

## Direct-reports clause

- JD says "must currently manage X PMs" or "5+ years recent direct PM management required, no flex" → **out of zone.**
- Soft mentor / coach / guide language → **in zone with friction** (pursue with the people-management story front-loaded).

(Maz's last direct people management ended 2015. He has 12 direct reports + 50+ employees + 700+ field technicians at Infotech VP as the defensible team-build evidence. Recent management at NG is matrixed, not HR-direct.)

---

## Posting state

- Posting must be **open** at evaluation time. LinkedIn "No longer accepting applications" red badge → out of zone (mark as `stale`).
- Posted **within last 7 days** preferred. Older = out of zone unless explicitly flagged for retroactive interest.

---

## Recruiter-Boolean credentials Maz cannot carry

Required credentials in a JD that Maz does not hold and cannot honestly claim. If a JD requires any of these as a hard gate, it's out of zone. The list lives in `me/voice.md` § Recruiter-Boolean filters. **This file references it; the canonical list is voice.**

PMP (which Maz holds) is the inverse: a credential MATCH, not a knock-out. Treat "PMP required" as a positive signal.
