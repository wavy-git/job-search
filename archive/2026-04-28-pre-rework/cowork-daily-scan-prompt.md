# Cowork Daily Job Alert Scan Prompt (HISTORICAL)

**Status**: This file is a historical snapshot of the original full-Rubric-1 prompt. The live scheduled task `daily-job-alert-scan` was simplified to collect-only on 2026-04-25. The live prompt is stored in the task itself. The current design separates collection (this task + the Python scanner) from screening (a human reviewer applying Rubric 1 over the snapshot files).

For the live prompt, see the scheduled task in Cowork settings or the `mcp__scheduled-tasks__list_scheduled_tasks` output.

The content below is preserved for reference only.

---

```
DAILY JOB ALERT SCAN

STEP 1 - Read context

Read these files from my project folder:
- job-search-strategy.md (Rubric 1 scoring rules, working rules)
- job-applications-log.md (what I've already applied to, avoid duplicates)
- target-companies.md (my 110 target companies, Tier A through O)
- Maz_Career_Background_Comprehensive.md (my full background for matching)

STEP 2 - Scan Fastmail

Use the Fastmail MCP. Search for emails received in the last 24 hours from jobs-listings@linkedin.com. Pull the full body of each email with get_email. Extract every job posting (company, title, location, posted date, apply link).

My 16 active LinkedIn alerts cover:
- director product (US Remote, Philly, Seattle, NYC, SF Bay)
- head of product (US Remote, Philly, Seattle, NYC, SF Bay)
- director pmo (US Remote, Philly, Seattle, NYC, SF Bay)
- director program management office (US Remote)
- senior product manager (US Remote)
- director product payments (US Remote, past week)

Each daily LinkedIn email contains 5-10 jobs in the body. Parse them all.

STEP 3 - Apply hard filters

Drop any role that fails:
- Posted more than 7 days ago
- Location not in: Remote US, Philly, NYC, Seattle, SF Bay, LA (allow Portugal/Spain only if it looks extraordinary at the Director level)
- Comp listed below $200K (unlisted = pass)
- Visa blocker for US citizens

STEP 4 - Stage 1: Score every passing role and keep top 200

Use Rubric 1 from job-search-strategy.md. Base 5. Apply modifiers. Clamp 1-10.

Background pillars (all equally weighted, no domain bias):
1. Payments / fintech / financial services
2. Platform / infrastructure / regulated industry
3. Operational turnaround / scaling
4. 0-to-1 builder / founding product
5. Analytics + executive translation
6. Cross-functional leadership at scale
7. B2B and B2C product depth

Acceptable role types: Director, Head, Principal, Senior of Product, Innovation, Operations, Strategy, Transformation, Process Excellence, Platform, Program Management.

Positive signals:
+3 if JD's primary domain matches any one pillar
+2 if JD's secondary requirements match other pillars
+2 for "broken-to-fix" pattern signals (turnaround, transformation, fix, scale, rescue, build-from-zero, founding hire)
+2 if Tier A or C target company (cross-check against target-companies.md)
+2 for title altitude in acceptable range, flexible on role type
+1 if posted in last 3 days
+1 hot-hiring signal (recent funding, expansion, leadership announcement)
+1 EMEA-relevant role (Farsi multilingual advantage)
+1 quiet-substance culture (engineering-led, enterprise SaaS, payments network, regulated industry)

Negative signals:
-2 narrow domain explicitly required outside stack ("10+ years at Stripe specifically")
-3 pure senior IC with no leadership scope
-2 strict payroll title required (background check risk)

Keep top 200.

STEP 5 - Stage 2: Deep analysis on the 200

For each, read full JD against full background. Re-score with judgment:
- Does the "what you'll do" actually match what candidate has done?
- Hidden hard requirements not flagged in stage 1?
- What's the realistic story candidate would tell to land?
- Yellow/red flags missed in stage 1?
- Classify each as: Match / Stretch-up / Stretch-sideways

Re-rank.

STEP 6 - Stage 3: Tag each role

Two binary labels per role:
- Domain: Payments OR Non-Payments
- Company size (by application volume / brand recognition): Large OR Small

Four buckets:
- Payments + Large
- Payments + Small
- Non-Payments + Large
- Non-Payments + Small

STEP 7 - Stage 4: Hand-pick top 20

4-6 roles per bucket = 20 total. Strongest by stage 2 + judgment. If a bucket can't yield 4 from 200, flag this as a signal that the input or rubric needs adjustment.

Cross-check against job-applications-log.md to flag anything I've already applied to.

STEP 8 - Output

Produce a ranked table with these columns:
Rank | Bucket | Company | Role | Location | Posted | Score | Match/Stretch | Reasoning (one line) | Apply link

Below the table:
- Total jobs scanned today
- Total passing hard filters
- Total in top 200
- Top 3 picks with 2-3 sentence analysis each (why these specifically, what the pivot story is, what the three-touch approach would look like)
- Urgent flags: score 9+ roles, posted-today roles, roles from Tier A or C companies
- Bucket distribution: how many roles came from each bucket originally, was anything underrepresented

STEP 9 - Update memory files

If new information emerged that should live in the memory files, update them:
- New role posted at a target company? Note it in target-companies.md
- Discovered a new company worth adding? Add to target-companies.md under appropriate tier
- Any new context that changes scoring? Update job-search-strategy.md
- Always update weekly-metrics.md with today's scan count

STEP 10 - Daily hygiene review

Quickly scan all 5 memory files plus the career background for:
- Inconsistencies between files
- Stale data (applications marked "waiting" for more than 2 weeks, etc.)
- Missing context that came up in recent sessions
- Out-of-date information

Fix what's found. Report what you changed.

WORKING RULES

- Never use em dashes or en dashes. Use commas, colons, periods, parentheses.
- Never assume time of day.
- Verify before claiming. If you can't verify a link, flag it as unverified.
- Be efficient. No preamble, no narration. Deliver the output.
- Do what's asked, nothing more.
```

---

## Setup notes

1. Schedule this task to run once daily, 30 minutes after your first LinkedIn alert email typically arrives (usually 7am ET for US-targeted alerts).

2. Make sure Cowork has Fastmail MCP enabled (same as your Claude.ai chat).

3. Make sure all 5 memory files plus `Maz_Career_Background_Comprehensive.md` are accessible from Cowork's project context.

4. The output is a daily ranked top 20. You review, pick which to pursue, and bring those JDs into a Claude.ai chat for tailoring and outreach.

5. Stage 2 (deep analysis on 200) is the heavy work. Expect 100-200 minutes of compute per run. Schedule accordingly.
