# Discipline

Authoring rules for this repository. These rules govern **how** files in this system are written, extended, audited, and reviewed. They do not contain domain logic. They do not contain personal data. They do not contain skill workflows.

Loaded by `CLAUDE.md` every session so the discipline survives between conversations.

---

## Inclusion test (for this file)

> **Is this content a rule about HOW a file in this repo is authored, extended, audited, or reviewed — independent of the file's domain? If yes → belongs here. If no — if it's domain logic (sourcing, tailoring, etc.) it belongs in that skill; if it's personal data it belongs in `me/`; if it's an operating instruction for the project as a whole it belongs in `CLAUDE.md`.**

Examples:
- "Re-derive each sentence from sources rather than lifting blocks." → authoring rule. Keep.
- "Run inclusion test sentence-by-sentence before declaring a file done." → authoring rule. Keep.
- "Comp floor is $180K." → domain rule (screening). Goes to constraints.
- "Don't claim agentic AI at enterprise scale." → voice/representation rule. Goes to voice.md.
- "Hard locks list lives in voice.md." → routing/operating rule. Goes to CLAUDE.md.

---

## Rule 1 — Each file declares its own inclusion test at the top

Every file in this repo (in `me/`, in any `skills/<skill>/`, in `pending.md`, etc.) opens with a one-statement inclusion test specific to that file: what belongs in it, what doesn't, where the things that don't belong should go instead.

The test must be **operational**: applying it to a candidate sentence should yield a yes/no answer without further interpretation. Vague principles ("only the important stuff") fail this rule.

Why this matters: without a stated inclusion rule, files accumulate content based on whoever was writing them at the moment. That's how the old comp doc grew to 859 lines of mixed facts, voice rules, tailoring decisions, and instructions for Claude. The rebuild exists because that drift happened. Don't recreate it.

---

## Rule 2 — Re-derive, don't lift

When writing a new file from existing source material (archived docs, other files), do not copy blocks and lightly edit them. Read the source, set it aside, then write each sentence in the new file from scratch.

Reason: lifting preserves the source's content shape. When the source mixed concerns (facts with rules with decisions), lifted blocks carry that mix into the new file. The act of re-deriving forces a fresh decision per sentence about whether it belongs.

Concrete: when writing `me/background.md`, the OLD comp doc's "Resume title: Head of AMI Products (functional descriptor, not inflated)" was lifted and relabeled as a "fact." The original framing said "Resume title" — a presentation decision. The relabeling didn't change what it was. Strict re-derive would have caught it.

---

## Rule 3 — Read all relevant sources, not just the most convenient one

When extracting content for a file, identify every archived source that contains related material and cross-check across all of them. Don't read one source and ship.

Example: the same hard-locks list appears in `_archive/2026-05-20-rebuild/Maz_Career_Background_Comprehensive.md` AND `screening_criteria.md` AND `job-search-strategy.md` AND `resume-tailoring.md` AND `resume-validation.md`. Reading only one means missing variants the others contain, or duplicating drift the others corrected.

The completion report (Rule 5) must list which sources were cross-checked.

---

## Rule 4 — Audit sentence-by-sentence before declaring done

After writing or modifying a file, walk it sentence by sentence and apply the file's inclusion test to each sentence. Each sentence either passes (keep) or fails (cut, with a note where the content should live instead).

This is not a keyword search. Keyword stop-lists catch words, not concepts. The test is the test — applied to meaning, not to surface form.

The audit pass is non-optional. A file isn't done until every sentence has been tested against the inclusion rule.

---

## Rule 5 — The completion report is part of completion

When declaring a file done (whether newly written or modified), the report must include:

- **Inclusion test results:** number of sentences walked, kept, cut. The cuts listed individually with destination (where they went instead).
- **Sources cross-checked:** list every archived source consulted for this file's content.
- **Mechanical consistency checks performed:** heading vs body agreement; internal redundancy scan; cross-file references resolved; claim-vs-source verification.
- **Open items flagged:** anything noticed during writing that doesn't belong in this file but isn't yet placed elsewhere → logged in `pending.md`.

Without the report, the work isn't done.

---

## Rule 6 — Run mechanical consistency checks before narrative analysis

When reviewing or analyzing a file, the first pass is mechanical:

- Does each section heading agree with its body's claims (e.g., title in the heading matches title in the bullets)?
- Are any sentences saying the same thing in two places (internal redundancy)?
- Do cross-file references resolve (e.g., "list in X" — does X actually contain the list)?
- Do quoted claims match the source (e.g., wording from background.md cited in voice.md — is it actually that wording)?

Cheap mechanical checks first. Then narrative analysis. Not the reverse.

Reason: narrative analysis can produce structured-looking output that masks shallow checking. Mechanical checks are unambiguous and either pass or fail.

---

## Rule 7 — When user feedback contradicts an authoring rule, surface the conflict

If the user asks for something that violates one of these rules (e.g., "just copy this section from the old doc"), do not silently apply it. Surface the conflict: "this would violate Rule 2 — re-derive, don't lift. Want me to lift anyway, or re-derive?" Then act on the user's explicit decision.

The user can override any of these rules. The point is not silent violation.

---

## Rule 8 — Don't trust filenames in archived or legacy source systems

Content in pre-rebuild systems is scattered with no enforced discipline. Career facts may live in interview-prep files. Voice rules may live in application notes. User-caught overclaims (real voice signal) may live buried in tailoring decision logs. Real voice exemplars may live in sent DMs.

When extracting content from archived sources:

1. Read every relevant file **end-to-end**. Don't assume a file's filename predicts its content.
2. For every piece of content in every file, categorize by **actual nature**, not by the file it appears in: fact about the user → background; voice/representation rule → voice; screening parameter → constraints; tailoring decision → tailoring skill; etc.
3. Where the same content appears in multiple files with variations, **document the drift** and pick the canonical version.
4. Read derived artifacts too (interview answers, tailored resumes, sent DMs, application notes). The system that produced them may have leaked content there that doesn't exist anywhere else, or that contradicts the supposed "source of truth."

This rule applies most aggressively during a rebuild but also when extending the system later. If the system grew without Rule 1 enforced, content drifts; periodic comprehensive re-reads catch it.

---

## Maintenance

This file is itself subject to its own rules. To add a new rule:

1. Apply the inclusion test above — is this a cross-cutting authoring rule, or does it belong elsewhere?
2. Verify the rule isn't a duplicate of an existing one.
3. Add the rule with a concrete example or anti-example.
4. Update CLAUDE.md routing if needed.
