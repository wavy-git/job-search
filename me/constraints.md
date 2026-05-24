# Maz Mavvaj — Constraints

Source of truth for what defines Maz's career zone. Used by `skills/sourcing/` to filter raw collections into the in-zone pool. A JD that fails any constraint here is out of zone — `skills/sourcing/` rejects it, regardless of any other strength.

This file answers ONE question only: **is this kind of job in my career zone?**

It does NOT score fit, evaluate chances, or rank in-zone candidates. That's `skills/screening/`.

---

## Inclusion test

> **PASSES IF:** it's a hard parameter that defines Maz's career zone — comp floor, locations, wanted title families, function knock-outs, domain knock-outs, posting state, recruiter-Boolean credentials he can't carry.
>
> **FAILS IF:** screening fit/chances logic (pillar match scoring, JD red-flag verbs, score bands → `skills/screening/`); fact about Maz (→ `me/background.md`); representation rule (→ `me/voice.md`); workflow (→ a skill); operational state (→ pipeline files); current-cycle strategic objectives (→ `pending.md`).

---

## Compensation

- **Base hard floor:** $180K USD (or local-currency equivalent). If the JD lists a comp range and the entire range is below this floor → out of zone. If the range straddles the floor, in-zone. If unlisted, in-zone.

---

## Locations

### In zone
- Remote-first (priority).
- Greater Philadelphia (60-mile radius from Marlton, NJ).
- NYC.
- Seattle.
- SF Bay Area.
- LA.
- Lisbon (Portugal).
- Madrid (Spain).
- Barcelona (Spain).

### Soft friction (in zone but inconvenient)
- Western suburbs of Philly (Berwyn / Malvern / Radnor) — friction, not knock-out.

### Out of zone
- Canada (CAD comp typically below floor).
- Onsite outside the acceptable metros.

---

## Wanted role titles (in zone)

In-zone title requires an acceptable seniority signal AND a function matching one of the wanted families (either by title string or by responsibilities described in the JD body).

### Acceptable seniority prefixes (IN)
Manager, Senior Manager, Lead, Principal, Director, Head, Senior Director, VP, Group, Staff, Founding. No-prefix titles like "Product Manager" also qualify.

### Excluded seniority prefixes (OUT)
Associate, Junior, Entry-Level, Intern, Coordinator, Assistant.

### Acceptable functional families (with responsibility definitions)
- **Product** — owns product strategy, roadmap, what gets built and why.
- **Innovation** — owns 0-to-1 initiatives or new bets outside the BAU portfolio.
- **Operations** — owns operational systems, throughput, or process performance for the business or a function. Excludes Sales / Revenue / People-Ops variants (see § Function knock-outs).
- **Strategy / Strategic Initiatives** — owns multi-year direction or cross-org initiatives.
- **Transformation (Business / Digital)** — owns large-scale change programs reshaping how the org works.
- **Process Excellence / Process Improvement / Continuous Improvement / Lean** — owns process design, flow, quality, throughput improvements.
- **Platform** — owns shared infrastructure or capability serving multiple downstream teams.
- **Program Management / PMO / Project Management / TPM** — owns multi-program or portfolio-level delivery (Director+ floor; or Senior Manager / Principal where comp meets the $180K floor).
- **Product Operations** — owns the operational layer enabling product teams.
- **Growth** — owns cross-functional growth ownership (acquisition, retention, monetization) as a distinct function.
- **Business Operations / BizOps** — owns cross-functional operational leverage (planning, analytics, strategic execution) for a business or function.
- **Delivery / Implementation** (Director+ only) — owns customer-facing delivery of a product/program at scale.
- **General Manager / Chief of Staff** — owns a P&L or executes on behalf of an executive.
- **Head of Business / Business Head** — owns a business unit or line of business.

---

## Function knock-outs (auto-drop, out of zone)

- Marketing.
- Agency PMO / adtech-pipeline PMO.
- Engineering Management.
- Customer Success.
- People Operations / HR Operations.
- Revenue Operations.
- Sales Operations.

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

## Posting state

- Posting must be **open** at evaluation time. LinkedIn "No longer accepting applications" red badge → out of zone (mark as `stale`).
- Posting must be **within the last 14 days**. Older = out of zone unless explicitly flagged for retroactive interest.

---

## Recruiter-Boolean credentials Maz cannot carry

Required credentials in a JD that Maz does not hold and cannot honestly claim. If a JD requires any of these as a hard gate, it's out of zone. The list lives in `me/voice.md` § Recruiter-Boolean filters. **This file references it; the canonical list is voice.**
