# Interviewing

Workflow + framework + reusable answers for producing a per-JD interview plan. Scans `me/background.md` + `me/voice.md` + the JD + the tailored resume to generate prep.

Per-JD interview plans are artifacts (live in `interviews/<jd>.md` when built, generated fresh per interview). This skill is the workflow that produces them.

---

## Inclusion test

> **PASSES IF:** workflow for producing per-JD interview plan; behavioral interview mapping framework (which story for which prompt); reusable answers (scent product, "Why VP→TPM," "Direct reports at NG"); interview-specific tone rules (don't apologize for the path; specific stories carry more weight than principles); pending answer slots (failure story, NG product vision — when developed).
>
> **FAILS IF:** facts about Maz the answers cite (→ `me/background.md`); voice/brand/belief content (→ `me/voice.md`); per-JD generated interview plan output (→ `interviews/<jd>.md`); resume content (→ `me/resume.md`); outreach messages (→ `skills/outreach/`); cover letters (→ `skills/composing/`); workflow for tailoring (→ `skills/tailoring/`); cross-cutting authoring (→ `discipline.md`).

---

## Inputs

- `me/background.md` (career facts + stories)
- `me/voice.md` (brand identity, core beliefs, don't-claim, bridges)
- The JD body (`outputs/jds/<file>`)
- The tailored resume for this JD (`resumes/<jd>.docx` + tailoring strategy from `skills/tailoring/`)
- Interview context (recruiter screen vs. HM convo vs. loop vs. onsite)

## Outputs

- Per-JD interview plan in `interviews/<jd>.md` (artifact)
- Behavioral mapping for this JD's likely prompts
- Selected stories to lead with
- Anticipated tough questions + drafted answers

---

## Core stories (ready to use, mapped to behavioral prompts)

These live here because they're INTERVIEW MATERIAL (answers Maz would give), not facts (which are in background) or representation rules (voice). They're stories pre-selected and pre-framed for interview use, drawn from the facts in background.

### Story 1: $2M vendor analysis reframing (National Grid)
- **Context:** built defect tracking system across all AMI teams' QA operations. Translated technical issues into financial impact. Showed leadership that fixing one issue could prevent $2M+/month in losses from manual technician dispatches.
- **Result:** reframed vendor accountability from technical escalations to financial decisions executives could act on. Changed how the org prioritizes vendor issues.
- **Use for:** executive influence, analytics translation, stakeholder management, operational turnaround, "tell me about a time you influenced without authority."

### Story 2: Log4Shell crisis response (Comcast, December 2021)
- **Context:** CISA called Log4Shell "one of the most serious" cybersecurity vulnerabilities ever. Maz was on the Network team; **invited into the response taskforce based on prior reputation** (leadership knew his work and brought him in across org lines).
- **Result:** built crisis reporting that surfaced every vulnerability across the company and tracked remediation to closure. The dashboard became the operational backbone the taskforce ran on (taskforce did the fixing; Maz's build was the visibility/tracking layer).
- **Use for:** initiative, operator pattern, seeing gaps, crisis leadership, analytics rigor, cross-functional/cross-org boundary crossing, "tell me about taking initiative."

### Story 3: NCC revival (Infotech Director, 20 to 5,000 units)
- **Context:** NCC = Network Communication Concentrator (payment transaction router). Obsolete Ingenico product, 20 units deployed. Maz negotiated directly with Ingenico to secure software ownership while Ingenico kept hardware. Rebuilt with capabilities outside the original product's intended purpose (gas station distribution, smart card processing, transaction monitoring, blacklist/whitelist).
- **Result:** 20 units → 5,000+ (250x). No competitor could replicate (no source code access).
- **Use for:** strategic thinking, partnership negotiation, building what others abandoned, creative reframing, "tell me about a strategic product decision."

### Story 4: Multi-bank terminal (Infotech VP)
- **Context:** market's first bank-independent terminal. Merchants with multiple bank accounts previously needed a separate terminal per bank. Created one device consolidating all accounts.
- **Result:** three outcomes from one product decision — attracted merchants (convenience), multiplied transaction volume (per-terminal density 20 → 90), made every competitor terminal obsolete.
- **Use for:** product strategy, customer-centric thinking, competitive positioning, payments expertise.

### Story 5: Central bank seat / national card network (Infotech VP)
- **Context:** co-architected the national card network at the central bank's table. Held a formal seat, one of the key decision-makers. Built national interbank payment switching network (equivalent in function to VisaNet or Mastercard's network at country scale). Unified transaction routing, authorization, settlement, security frameworks. Included PCI-DSS as part of broader reform.
- **Result:** covered 30+ financial institutions. 99.5/100 comprehensive score. Maz's company ranked #1 of all national payment service providers. Maz championed PCI-DSS until nationally regulated.
- **Use for:** industry-shaping work, gravitas, regulatory expertise, payments credibility at network scale, "tell me about a cross-functional program."

### Story 6: Cloud platform delivery (Comcast)
- **Context:** data center network portion of Comcast's strategic in-house cloud platform. Unplanned mid-cycle, tapped by leadership.
- **Result:** delivered in 6 months vs. 12-month estimate. Zero impact on parallel initiatives.
- **Use for:** delivery speed, resource efficiency, complex program execution under pressure.

### Story 7: Configuration-driven platform (Infotech Manager)
- **Context:** built the market's first configuration-driven payment application platform. Replaced hardcoded apps with configurable code.
- **Result:** release cycles 6-8 weeks → 3-5 days. Terminal deployments 5-6 months → 2-3 weeks. Customer base 2 → 8 major FIs. Terminal network 10K → 100K+. "The market was in shock."
- **Use for:** technical innovation, market-making, speed as strategy, early-career credibility.

### Story 8: VP Infotech turnaround (2013-2015)
- **Context:** company was in bad shape. Toxic culture, trust at lowest, customers (banks) losing confidence, losing contracts, bleeding money. Critical 60K terminal contract with only 10K deployed.
- **Result:** 10K → 120K merchants, 150M+ annual transactions, 54x volume growth in 18 months. Four first-to-market innovations (predictive merchant targeting, pull-based logistics, automated remote configuration, multi-bank terminal).
- **Use for:** turnaround experience, scaling under pressure, operational leadership, payments at merchant scale, "tell me about a turnaround."

---

## Behavioral interview mapping (which story for which prompt)

| Prompt | Lead story | Backup |
|---|---|---|
| Tell me about a time you influenced without authority | Story 1 ($2M vendor) | Story 2 (Log4Shell) |
| Tell me about taking initiative | Story 2 (Log4Shell) | CCRE change mgmt (in background.md, can promote to story) |
| Tell me about a strategic product decision | Story 3 (NCC revival) | Story 4 (multi-bank terminal) |
| Tell me about a cross-functional program | Story 5 (central bank seat) | NG AMI platform leadership (background) |
| Tell me about a turnaround | Story 8 (Infotech VP) | Comcast deployment transformation (in background) |
| Tell me about a time you built something under pressure | Story 6 (cloud platform 6 vs 12) | Story 2 (Log4Shell) |
| Tell me about technical innovation | Story 7 (config-driven platform) | Story 3 (NCC software ownership) |

---

## Reusable answers (canonical wording, drawn from voice + background)

### "Why VP to TPM?" (career trajectory question)

```
Deliberate move. I left a VP role to relocate to the US, earn an MBA,
and enter the American market. Comcast wasn't a step down, it was a
strategic entry point into Fortune 50 enterprise scale. The outcomes
prove it: I tripled deployment throughput, built analytics that
powered a national cybersecurity crisis response, and was recruited
to replicate my model across a larger division.
```

### "Do you have direct reports?" (asked at NG)

```
At National Grid, I lead through platform ownership. 30 people work
on my platform day to day. Eight teams deliver on my platform. It's
leadership through influence, not org chart authority. My earlier
roles at Infotech prove I can build and manage large direct teams:
12 direct reports, 50+ employees, 700+ field technicians. At NG, the
challenge is different: making an entire program succeed through the
platform I own.
```

### "What's a product you wish you built?" (reusable scent answer)

```
A technology that captures, stores, and transmits scent. Smell is
the only sense that bypasses the brain's processing centers and goes
straight to memory and emotion. It's why the smell of a specific
bakery can pull you back twenty years before you've even named the
feeling. And yet every digital product we've ever built is silent on
this entire dimension. Sound, sight, sometimes touch, but never
smell. There's a whole language of presence we haven't been able to
write.

I want to build the infrastructure that closes that gap. Imagine a
photo of yourself as a child in the kitchen returning the scent of
the cookies your grandmother was baking that evening. A video call
with someone overseas carrying the smell of their morning coffee. A
history lesson about an ancient marketplace landing the spice and
smoke of the actual place. A horror game where the sewer you're
hiding in smells like a sewer. Once it works, the question isn't
what we'd use it for. It's what we couldn't. It would add a
dimension to digital experience that has never existed before, and
the parts of the brain it would reach are the ones that make us
feel something is real.
```

**Use for:** any "product you wish you built," "favorite product idea," "blue-sky problem" question. Shows product imagination, taste, range, humanity.

---

## Interview-specific tone rules

These are interview-channel-specific applications of voice rules. Universal voice rules (em dash, no melodrama, etc.) apply too — these add on for the interview channel:

- **Direct, factual, leader-altitude.** No hedging. Land the story.
- **Don't apologize for the path.** VP → TPM transition was deliberate; own it. Don't preface stories with "well, this was a long time ago but..." — leadership-altitude framing.
- **Use breadth as evidence, not as defense.** "I've operated as B2B Director, B2C VP, Fortune 50 TPM, and platform owner — same builder pattern at every scale." Breadth proves range, not lack of focus.
- **Specific stories carry more weight than principles.** When asked about influence, lead with the $2M vendor story (specific, quantified). Don't lead with "I believe in data-driven decision-making."
- **Numbers anchor every story.** 250x, 54x, 10K→120K, 6 months vs 12. These do the work of credibility.

---

## Per-JD interview plan generation workflow

When a recruiter screen lands (or earlier, when preparing for an anticipated interview):

1. **Read inputs:** the JD body, the tailored resume for this JD, `me/background.md`, `me/voice.md`.
2. **Identify likely behavioral prompts** based on the JD's primary responsibilities and the interviewer's role (recruiter vs HM vs peer vs cross-functional).
3. **Map each likely prompt to the best lead story** from the core stories above. Note backups.
4. **Identify JD-specific stories to prepare:** anything in the JD that requires a story not in the core 8 → flag and develop or escalate.
5. **Draft answers to the standard hard questions** (Why VP→TPM, direct reports, failure story if developed, product vision if developed).
6. **Identify don't-claim risks for THIS interview:** what topics might the interviewer push on that overlap with Maz's don't-claim list (healthcare, MSSP, etc.)? Pre-draft bridge framings from `me/voice.md` § Don't-claim + bridges.
7. **Note questions Maz should ask the interviewer:** at recruiter screen (process, timeline), at HM convo (team, success metrics, what's broken), at onsite (org strategy, where to make impact in first 90 days).
8. **Save to `interviews/<jd>.md`.** Format: behavioral mapping + selected stories + drafted hard answers + don't-claim bridges for this domain + questions to ask.
9. **Audit:** does the plan violate any voice rule? Does it claim anything from the don't-claim list?

---

## Pending answers (to develop when triggered)

These are anticipated questions Maz doesn't yet have strong answers for. Develop when next interview triggers them.

### "Tell me about a failure"
- Needs a specific real story.
- Strong failure stories for Director-level interviews show: real stakes (not trivial); ownership of the failure; clear learning; evidence the learning changed behavior.
- Candidates to consider (need user input): any major program at NG / Comcast / Infotech that didn't go as planned? Any investment / hire / product bet / strategic decision that backfired? Any time the turnaround tactics didn't work?

### "What's your product vision at NG?" (forward-looking)
- Needs a forward-looking answer about platform evolution beyond ops.
- Options to develop: platform beyond AMI (data platform for the whole utility?); AI-augmented utility operations; customer-facing extensibility; cross-state consolidation.

---

## Open / parked items

- Scent product answer is currently a one-shot reusable. Consider variants for different audience tones (more technical for engineering interviewers; more narrative for product interviewers).
- Per-company interview prep notes (e.g., Mastercard-specific, Customer.io-specific) live in the per-JD `interviews/<jd>.md` file, not here.
