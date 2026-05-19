# Tailored Resume Validation

Last updated: 2026-05-16

This file contains the validation checklist for a tailored resume. Run every gate after Phase 2 of `resume-tailoring.md`. **Do not present an un-validated resume to the user.**

If any gate fails, fix it before continuing. Re-run any gate whose section was modified by a fix.

---

## Gate 0: Strategy exists in writing

- [ ] Phase 1 of `resume-tailoring.md` produced a **written strategy** mapping the top 6 JD qualifications to background, with explicit highlights, gaps, bridges, and reserve-material promotions. The strategy includes the verb-mode mapping (ownership / discovery / execution / collaboration) for each priority and the full-resume audit (which sections need changes, which stay as master).

If no written strategy exists, **stop and return to Phase 1.** A tailored resume without a strategy is a process failure.

---

## Gate 1: JD priority coverage

- [ ] **Top 5 of top 6 JD priorities: coverage table.** Strategy identifies top 6; validation confirms top 5 land. Threshold:
  - **Top priority lands in S1 of summary**
  - **At least 2 of the top 5 land in S1-S2 of summary**
  - **All 5 covered somewhere in summary (S1-S4)**

| # | JD priority | Verb mode | Where in summary | Where in body | Pass? |
|---|---|---|---|---|---|
| 1 | ... | ownership/discovery/execution/collab | S? | bullet/scope/skim | |
| 2 | ... | ... | ... | ... | |
| 3 | ... | ... | ... | ... | |
| 4 | ... | ... | ... | ... | |
| 5 | ... | ... | ... | ... | |

- [ ] **Body reinforces summary, not contradicts.** For each top-5 priority, body sections (bullets, scope lines, skim zones) reinforce what the summary claims. No contradiction between summary and body.

- [ ] Bridge framings from Phase 1 strategy appear in every section of the resume where they should (per the bridge-sweep list in the strategy).

---

## Gate 2: Hard locks

Full hard locks list lives in `Maz_Career_Background_Comprehensive.md` § Hard Locks. Verify each below.

- [ ] **Hard numbers preserved verbatim.** Cross-check the tailored version against the master: 10K to 120K, 150M+ transactions, 30+ FIs, $1.4B program, 99.5/100, 12 direct reports, 50+ employees, 700+ field technicians, 1M+ terminals, $250M+, 2M+ vouchers monthly, 200% throughput, 6-8 weeks to 3-5 days, 5-6 months to 2-3 weeks, 2 to 8 FIs, 10K to 100K+ terminals, 60K terminal contract, 20 to 5,000+ NCC, 50% market share, 80+ features per PI, **#1 of all national payment service providers (Infotech VP)**, **4 national data centers + 100+ regional facilities (Comcast)**, **20 to 90 monthly per-terminal transactions (Infotech VP)**, **54x volume growth in 18 months (Infotech VP)**.
- [ ] **Companies, dates, employment facts unchanged.** Chronological structure not reordered.
- [ ] **No "Director" payroll-title claim at NG.** Functional descriptors only.
- [ ] **Log4Shell framing (Comcast):** invited into response taskforce based on prior reputation while on Network team (cross-functional move). Build did reporting + visibility + tracking of vulnerabilities, NOT the fixing. Never revert to "walked in unbidden" framing.
- [ ] **Pillar identity respected.** No claims of pillars Maz doesn't have:
  - Not claiming agentic AI track record (it's AI-augmented automation, not agentic LLM workflow design in production)
  - Not claiming healthcare-product or telehealth domain expertise
  - Not claiming waste-industry domain expertise
  - Not claiming MSSP/MDR/PTaaS specialty
  - Not claiming Quote-to-Cash or Oracle NetSuite specialty
  - Not claiming cybersecurity-product specialty (Comcast cyber work was org-level analytics, not product)
- [ ] **Bullet count discipline (FINAL5_5, current canonical):** NG=5, Comcast=4, Infotech VP=5, Director=3, Manager=2, Developer=2. Any count change vs the master must be documented in the strategy.

---

## Gate 3: 10-point bullet framework (every modified bullet)

Each modified bullet must pass all 10:

1. **Outcome first** — leads with what changed
2. **Scale signal** — shows the size of impact
3. **So what** — recruiter would care
4. **One idea** — says one thing clearly
5. **Scannable** — 1.5 lines max
6. **Executive tone** — sounds like a leader wrote it
7. **Decision-maker signal** — shows Maz made a choice
8. **Altitude** — right level of abstraction
9. **Defensible** — can be backed up in interview
10. **Pattern reinforcement** — supports career thesis

A bullet that fails any of the 10 must be fixed before ship.

---

## Gate 4: Recruiter-shoe test on summary

Read the summary as a recruiter who has 6 seconds and zero domain context.

- [ ] **Every term decodes in 2 seconds by a non-domain reader.** No company-specific abbreviations the reader can't expand (e.g., "NG", "PI"); no industry-internal jargon ("FIs", "DDI", etc.) without context; no unexplained product/app names ("Lighthouse", "Jingle" without description). If an abbreviation must appear, expand it on first use.
- [ ] **Every word earns premium real estate.** No filler, no cliché verbs ("synergize", "leverage", "streamline"), no padding clauses.
- [ ] **Specificity check.** No vague abstract nouns in narrative zones without concrete grounding. "Prototypes," "workflows," "platforms," "outcomes" must be specified — what kind, what scope, who. Test: can the reader picture the work from the words alone?
- [ ] **Each sentence is clear and readable.** Compound clauses are fine if they aid clarity. If a sentence requires the reader to re-parse, simplify. Reader effort matters more than sentence-count rules.
- [ ] **Each fact attributed to its real role.** No verb-stacking that conflates two roles. Example failure mode: "Built X and tripled Y at a Fortune 50" when X happened at NG and Y at Comcast.
- [ ] **Each number anchored to a JD priority with context.** No isolated stats floating without a clear "why the recruiter cares." Numbers without context are distraction, not evidence.
- [ ] **JD verbatim language echoed where defensible.** If the JD says "workflows and prototypes," the resume should use both words, not paraphrase ("AI-built apps"). Use JD's exact terminology in skim zones and where it lands naturally in narrative.
- [ ] **Pattern vs one-off.** Each priority is anchored on a career pattern (stronger evidence) or a single item (weaker). Pattern preferred when available. If anchored on a one-off, document why no pattern applies.
- [ ] **Phrase-level reinforcement audit.** Walk the summary phrase by phrase. Each phrase must strongly and clearly reinforce a specific top-5 JD qualification. Build a phrase → priority map. Anything that does NOT tie to a top-5 priority is flagged: either cut, or rework so it earns. Common failure: subject-matter details (e.g., "music app" for a non-music JD) that describe instead of reinforce — cut. Generic enough to grounded prototype framing ("AI-built prototypes live to real users") is preferred over specific subject matter when the subject is irrelevant to the JD.
- [ ] **Test-by-deletion.** Read each word and phrase. Mentally delete it. If the JD priority reinforcement still holds without it, the word didn't earn — delete it. Apply to: redundant modifiers ("deployment throughput" → "throughput"; "vendor defect data" → "vendor data"), location anchors after first mention (don't repeat "at National Grid" in every sentence once S1 establishes it), HOW-context that doesn't reinforce a top-5 priority ("via Lean flow"), tenure double-counts ("a decade" if brand line already says "20+ years"), parallel-structure connectors that don't add meaning, and over-explanation when the reader can infer (e.g., "workflows automating feature documentation" — "AI-augmented workflows" already implies the function). Over-explanation is a signal of unconfidence; trim it.

---

## Gate 5: 6-second mock scan

- [ ] Read only the top of page 1 (name, title, current company, top 3 bullets) in 6 seconds. State the punchline. **Does the punchline match the JD's #1 priority?** If the recruiter's hottest button isn't visible in 6 seconds, S1 of the summary needs to lead with it.

---

## Gate 6: JD must-have coverage

- [ ] Every JD must-have (from Phase 1 extraction) is demonstrated somewhere in the resume — bullet, scope line, or skim zone. List each must-have and where it lands.

---

## Gate 7: Knock-out check

- [ ] Location: meets JD's stated requirement.
- [ ] Citizenship: meets JD's stated requirement (or no requirement listed).
- [ ] YOE: meets or exceeds JD's stated minimum.
- [ ] Direct-reports: meets JD's stated requirement OR JD has soft mentor/coach language only.

---

## Gate 8: Length and trim

- [ ] Length: 1-2 pages.
- [ ] **Trim 10%.** Read every sentence and every bullet. Cut what doesn't earn its place.

---

## Gate 9: Verify file state, then side-by-side diff to user

When Gates 0-8 all pass:

- [ ] **Read the current docx state** before composing the diff. Don't rely on memory of what was "applied" — verify what's actually saved.
- [ ] Compose the side-by-side diff using the canonical format below.
- [ ] **Restate the change set in plain words** before applying. "I'm about to do X, Y, Z. Confirm?" Forces sanity check between user understanding and Claude's intended changes.

**Canonical side-by-side format (locked 2026-04-27, validated to render correctly in Maz's Claude Code desktop renderer):**

- **Removed text:** wrap in `~~***[...]***~~` — produces strikethrough + bold-italic + square brackets
- **Added text:** wrap in `***[...]***` — produces bold-italic + square brackets
- **Table structure:** 5 columns — `# | Section | Master | [Tailored Company] | Why`
- **Cell content:** show only the sections that changed; drop unchanged rows. Within each cell, show enough surrounding context for the reader to locate the change, but trim aggressively (`...` is fine for unchanged middle).
- **Do not use:** monospace/code style (changes the font, dilutes signal); HTML tags (`<u>`, `<mark>`, `<span>` — none render in Maz's viewer); yellow background (renderer doesn't support it).

Example row:

```
| 1 | Summary | ...stalled ~~***[fintech startup]***~~; scaled it from 10K... | ...stalled ***[payments venture]***; scaled it from 10K... | Generalizes industry framing for hidden employer. |
```

**Present the diff WITH the validation-pass summary** so the user knows every gate has been cleared. If a gate could not be passed (rare), surface the specific failure with the diff.

---

## Gate 10: Apply user feedback

- [ ] User feedback applied to changed sections.
- [ ] **Re-run Gates 1-8 on any sections that changed in response to feedback.** A summary edit may break Gate 1; a bullet edit may break Gate 4. Don't assume one section is independent of others.
- [ ] **If user feedback contradicts a hard lock, hard lock wins.** Surface the conflict; don't silently apply the conflicting feedback.

---

## SHIP

After all gates pass and user approves the diff:

- [ ] Final save of the tailored resume.
- [ ] Confirm the user is ready to submit.

---

## Post-ship: three-touch and logging

After the user submits the application:

- [ ] **ATS submit** — confirmed completed by user.
- [ ] **HM / founder LinkedIn DM** — use HM identification from leadership lookup. Draft per the user's preferred tone (warm, casual, asks for perspective, not pitchy).
- [ ] **Referral hunt** — 1st/2nd degree connection at the company.
- [ ] Move row from `candidates.json` to `applications.md` with full notes (tailoring decisions, three-touch status, recruiter-pass / HM-pass odds estimate).
- [ ] Add outreach touches to `outreach.md`.
- [ ] Update `weekly-metrics.md`.
