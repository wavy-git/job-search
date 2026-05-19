# Job Search System — Entry Point

This directory is Maz Mavvaj's job search system. It contains the master resume, all career-background facts, and the operational docs that govern screening, tailoring, validation, and outreach.

**Read this file first in every session.** It tells you which files to load for which kind of request.

---

## Canonical state (as of 2026-05-16)

- **Master resume:** `resumes/Maz_Mavvaj_Director_Resume_FINAL5_5.docx` (and `.md` companion for fast reading). **FINAL5_5 is canonical.** FINAL5_4 is archived; do not use.
- **Source of truth for career facts:** `Maz_Career_Background_Comprehensive.md`. If a fact isn't in this doc, it isn't defensible. Update this doc whenever new career information surfaces.
- **Tailored resumes:** live in `resumes/` with naming pattern `Maz_Mavvaj_[Title]_[Company].docx`.

---

## Doc hierarchy (load only what you need)

| Doc | Purpose | When to load |
|---|---|---|
| `Maz_Career_Background_Comprehensive.md` | Source of truth: career history, hard locks, voice rules, promotional reserve, brand identity, communication preferences, 10-point bullet framework | **Always** — for any career-related request |
| `resume-tailoring.md` | Tailoring workflow (Phase 1 strategy → Phase 2 section work), promotion rule for reserve material, domain-bridging playbook | When user asks to tailor a resume for a specific JD |
| `resume-validation.md` | 11 validation gates (0-10) — strategy check, hard-lock check, 10-point bullet check, 6-second scan, etc. | After tailoring, before showing to user |
| `screening_criteria.md` | Compensation floor, location, wanted titles, function knock-outs, 11 background pillars, 1-5 scoring | When user asks whether a JD is worth pursuing |
| `job-search-strategy.md` | Overall job-search rubric, target altitude bands, channel strategy | Background context; rarely needed standalone |
| `interview-prep.md` | Anticipated questions + framed answers, key stories to prep | When user asks about interview prep |
| `applications.md` | Log of submitted applications with three-touch status | When user asks about a specific application or wants outreach context |
| `outreach.md` | DM templates, referral hunt log | When user asks about outreach touches |
| `target-companies.md` / `target_companies.json` | Company watch list with ATS metadata | Scanner-related work; usually background |
| `candidates.json` | Pre-application JD pipeline | When user asks about JDs in the pipeline |
| `README.md` | Documents `job_scanner.py` only — NOT the resume system | Only for scanner work |

---

## Workflow entry points

### Workflow A — Screen a JD (decide if it's worth pursuing)
**Load:** `screening_criteria.md` first; `Maz_Career_Background_Comprehensive.md` for pillar matching.

Run the procedure in `screening_criteria.md` § Procedure. Output: 1-5 score + 1-2 sentence judgment. Place in `candidates.json`.

### Workflow B — Tailor a resume for a specific JD
**Load:** `Maz_Career_Background_Comprehensive.md` (full), `resumes/Maz_Mavvaj_Director_Resume_FINAL5_5.md` (full), `resume-tailoring.md`, `resume-validation.md`.

Follow `resume-tailoring.md` Phase 1 → Phase 2 → run every gate in `resume-validation.md` → present diff to user. **Do not present an un-validated resume.**

### Workflow C — Rebuild / refine a resume bullet
**Load:** `Maz_Career_Background_Comprehensive.md` (role section + Hard Locks + PROMOTIONAL RESERVE + Communication Preferences + 10-point framework), `resumes/Maz_Mavvaj_Director_Resume_FINAL5_5.md`.

Apply the bullet-by-bullet approach: ask theme → propose 2-3 options → wait for user feedback. Hold all voice rules and hard locks throughout. When a bullet is locked, update the comp doc's "Resume Bullets — current canonical (FINAL5_5)" section for that role.

### Workflow D — Interview prep
**Load:** `interview-prep.md`, `Maz_Career_Background_Comprehensive.md` § Interview Preparation + Key Stories.

### Workflow E — Outreach / DMs / referral hunts
**Load:** `outreach.md`, `applications.md` (for context on which application this connects to), `Maz_Career_Background_Comprehensive.md` § Brand Identity + Communication Preferences.

### Workflow F — Update the comp doc with new career facts
**Load:** `Maz_Career_Background_Comprehensive.md`.

Add new facts under the relevant role section. Cross-check against Hard Locks (add new defensible numbers there too). Update Last Updated header.

---

## Rules that govern all sessions

### Hard locks (full list in `Maz_Career_Background_Comprehensive.md` § Hard Locks)
- All hard numbers verbatim (no rounding, no edits)
- Companies, dates, employment facts unchanged
- No "Director" payroll-title claim at NG (functional descriptors only)
- Log4Shell framing: invited based on reputation while on Network team (NOT "walked in unbidden")
- Pillar identity respected (don't claim agentic AI at enterprise scale outside independent projects; don't claim healthcare-product, waste-industry, MSSP/MDR, Quote-to-Cash, cybersecurity-product specialties)

### Voice rules (in `Maz_Career_Background_Comprehensive.md` § Communication Preferences + INSTRUCTIONS FOR CLAUDE)
- Plain English, no buzzwords ("operational picture," "strategic product call," etc.)
- Outcome-led with hard numbers
- Decision-maker signal in every bullet
- Senior leadership altitude — director and above
- Em dashes used sparingly (acceptable in rare occasions that aid clarity)
- Agentic AI is defensible (per Jingle + MailFlow)
- Brand identity: quiet confidence, sees gaps, builds without being asked, authority through facts not performance

### Process discipline
- **Discuss before coding** — don't edit files without discussing the approach first
- **Never assume** — confirm with evidence (read code/data/docs); no "likely," "probably," "maybe"
- **Verify your work** — read the file back; check against hard locks; run validation gates
- **Fix before build** — never build new features while existing issues are broken
- **Maintain docs** — update the relevant docs in the same commit as the change

---

## Promotional reserve (for tailoring)

When a JD weights tools / techniques / keywords that aren't currently in the master resume, source them from `Maz_Career_Background_Comprehensive.md` § PROMOTIONAL RESERVE table. Bullet-level promotion requires the 3-condition promotion rule (in `resume-tailoring.md`). Skim-zone promotion (Tools & Tech / Core Comp / Certs) has a lower bar — just verify the keyword is defensible per comp doc and the JD references it.

---

## Project structure quick reference

```
/                          ← you are here
├── CLAUDE.md              ← this file (entry point)
├── README.md              ← scanner docs only
├── Maz_Career_Background_Comprehensive.md  ← source of truth
├── resume-tailoring.md    ← tailoring workflow
├── resume-validation.md   ← validation gates
├── screening_criteria.md  ← JD screening
├── job-search-strategy.md ← overall strategy
├── interview-prep.md
├── applications.md
├── outreach.md
├── candidates.json        ← JD pipeline
├── target_companies.json  ← scanner config
├── archive.json           ← screened-out JDs
├── job_scanner.py         ← scraper
├── resumes/               ← master + tailored versions
└── outputs/               ← scanner output + saved JDs
```

---

## When in doubt

1. Read this file
2. Read `Maz_Career_Background_Comprehensive.md` if the request touches career facts at all
3. Ask the user before editing files
4. Don't silently violate hard locks or voice rules — surface conflicts explicitly
