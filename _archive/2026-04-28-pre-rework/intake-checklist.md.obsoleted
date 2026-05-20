# Intake Checklist

Last updated: 2026-04-27

The 1-page operational runbook for screening new JDs entering the pipeline. Open this file every time a new JD needs to be evaluated. Target: 5-10 minutes per JD.

The full framework lives in `job-search-strategy.md` Rubric 1. Career constraints (11 pillars, hard locks, payroll-title risk) live in `Maz_Career_Background_Comprehensive.md`. This file is the executable checklist.

---

## Phase 1 — Hard gates (binary; fail any → log to archive.md, never enter candidates.md)

The URL is logged in archive.md with the hard-gate failure reason in Notes, so future daily runs do not re-screen the same role.

- [ ] **Title-keyword match.** Title contains at least one wanted keyword AND none of the excluded keywords (engineer, engineering manager, tech lead, technical lead, architect, developer, designer, scientist). Full keyword list in strategy doc Rubric 1.
- [ ] **Location pass.** Remote US / NYC / Philly metro / SF Bay / Seattle / LA / Portugal / Spain. Greater Philly tri-state region (NJ + Eastern PA + Northern DE within ~60 mi of Philly) all pass. Lenient default for ambiguous "United States" labels.
- [ ] **Posted recency.** Within last 7 days. Unknown date passes through.
- [ ] **Citizenship knock-out.** Drop if non-US country requires local citizenship and won't sponsor.
- [ ] **Comp floor.** Drop if comp listed below floor (US Director $200K base; PT/ES Director €120-140K base).
- [ ] **Hard knock-out keyword.** Drop if explicit must-have Maz cannot honestly claim (PMP REQUIRED, active Secret clearance REQUIRED, biotech-only, single specialty no defensible bridge).

If all gates pass, proceed to Phase 2. If any gate fails, write to archive.md with the failure reason and stop.

## Phase 2 — Pull the JD body

- [ ] Fetch from canonical source (company ATS like Ashby HQ / Greenhouse / Lever / Workday) when possible. LinkedIn abbreviations are not enough.
- [ ] If canonical not accessible, use LinkedIn body. Note the source.
- [ ] If JD body cannot be fetched, score conservatively and flag in Notes: "JD-fetch incomplete."

## Phase 3 — Seven screening dimensions (expert-judgment, not rigid scoring)

Evaluate each lens, capture the read mentally:

- [ ] **Pillar match map.** Which of the 11 background pillars activate? Direct / adjacent / stretch.
- [ ] **Altitude alignment.** JD altitude × company size per the table in strategy doc Rubric 1.
- [ ] **Recent-direct-reports gap.** Maz's last direct people management ended 2015. JDs requiring "currently managing X direct reports" or "5+ years recent direct PM management" carry friction. Surface as a flag in the score; pair with no-flexibility language and treat as hard knock-out (Phase 1, retroactive).
- [ ] **Domain bridging.** Direct fit / adjacent / cross-bridge / no defensible bridge. Bridge framings playbook lives in Rubric 2; reference it.
- [ ] **Friction signals.** Recruiter-Boolean filter risks (NetSuite/Q2C/MSSP/MDR/biotech/Oracle ERP/IWMS/specific certifications/FAANG-pipeline pedigree).
- [ ] **Function fit.** Product / Strategy / Operations / Transformation / Platform / Program Management / Innovation / Process — wanted. Marketing / Design / Legal / Engineering Mgmt / Customer Success — wrong function, retroactively treat as hard knock-out.
- [ ] **Realistic story.** What story would Maz tell to land this role? If no defensible story exists, the surface signals overstate the fit.

Voice during this phase: senior career coach reviewing one last time. Not a checklist tick exercise.

## Phase 4 — Output

- [ ] **Score** (1-10). Single composite, honestly reflecting ALL factors including knock-outs and friction. A role with strong pillar fit but a single hard knock-out gets a low score, not a high score with a flag. Top of list = next to apply; bottom = consider archiving.
- [ ] **Notes** (1-2 sentences). Honest read capturing the dominant fit signal and the dominant friction signal. No bullet lists, no buzzwords, just the verdict-worthy summary in the voice of a career coach.
- [ ] **Status.** Set to `screened` if Maz should consider it, `archive-review` if the screener thinks it should be archived but wants user confirmation first.

There is no separate Verdict column. Score is the verdict; Status drives action state.

## Phase 5 — Write to candidates.md

- [ ] **Insert row** with: Rank (placeholder; resorted next), Score, URL, Company, Title, Size (S < 500 / M 500-5K / L 5K+), Source (linkedin / scanner / manual / recruiter-fronted / etc.), Posted, First Seen = today, Last Seen = today, Status (`screened` or `archive-review`), Notes.
- [ ] **Resort** the table:
  1. Status: `on-deck` first (active work floats to top), then `screened`, then `archive-review` (sinks to bottom for user confirmation).
  2. Score descending within each Status group.
  3. Re-number Rank.
- [ ] If existing URL: only update `last_seen`, do not re-score. Re-scoring happens at apply-time per Rubric 1 two-screen design.

## Phase 6 — Volume handling (independent of source)

- [ ] If processing many JDs at once (any daily snapshot — LinkedIn alerts, Python scanner, target-company alert, batch paste), batch the survivors through a subagent with this checklist as the spec. Volume is the trigger, not source.
- [ ] If processing a single JD (opportunistic add, one-off paste, one role at a time), run inline.
- [ ] After any batch completes, single resort + Rank renumbering pass on candidates.md.

---

## Notes for self

- The two screens (intake here, apply-time deep validation in tailor-checklist Phase 1) do the same JD-vs-candidate evaluation at different depths. Apply-time catches anything intake missed.
- The screen is intentionally not a rubric-as-formula. The structure ensures comprehensive coverage; the final score comes from honest expert judgment.
- `archive-review` Status entries stay at the bottom of candidates.md until user confirms move to archive.md. The screener flags; the user decides.
- Hard-gate failures go directly to archive.md (Phase 1). They never appear in candidates.md.
