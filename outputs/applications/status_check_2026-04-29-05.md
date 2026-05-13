# Application Status Check, 2026-04-29 05:31 ET

Folders searched: ALL (search_emails spans all Fastmail folders)

Window scanned: last 12 hours (2026-04-28 17:31 ET through 2026-04-29 05:31 ET, i.e. 2026-04-28 21:31 UTC through 2026-04-29 09:31 UTC).

Active applications in scope (Funnel Status not in `offer`/`rejected-by-employer`/`withdrawn`/`ghosted`):
- ElectronX, Head of Product (LinkedIn 4392197135)
- Wheel, Senior Product Manager Operational Intelligence (656c9648-9e9d-4884-95bf-d83f1f127798)
- Sourgum, Head of Product (a8720ec5-99e8-4aa8-b8da-07aa0afa5be6)
- Liberty Personnel Services, Director Product Management (LinkedIn 4366542359) — outreach: Brian Patrick Feeley
- Customer.io, Director Product Management (Greenhouse 7775708) — outreach: Matthew Wensing
- Nava, Director of Product (Greenhouse 4210653009) — outreach: Leanna Miller

Search profiles applied per app: company name, job ID, role title, sender domain matches (`*@<company-domain>`), known ATS senders (`no-reply@ashbyhq.com`, `*@us.greenhouse-mail.io`, `*@myworkday.com`), recruiter/HM names from outreach.md, plus LinkedIn message senders (`messaging-noreply@linkedin.com`, `inmail-hit-reply@linkedin.com`). Body keyword sweeps for "interview", "next steps", "schedule", "phone screen", "recruiter", "unfortunately", "regret", "application update".

## Potential transitions

None within the 12-hour window.

No company-domain emails, no ATS notifications, no LinkedIn messages from Brian Patrick Feeley, Matthew Wensing, or Leanna Miller landed during the window. The most recent app-related correspondence is the ATS application acknowledgments, all dated 2026-04-26 / 2026-04-27 (outside this window).

## No new emails for these applications

- ElectronX, Head of Product — last app-related email: ATS ack from `no-reply@ashbyhq.com` 2026-04-26 (outside window)
- Wheel, Senior PM Operational Intelligence — last app-related email: ATS ack from `no-reply@ashbyhq.com` 2026-04-26 (outside window)
- Sourgum, Head of Product — last app-related email: ATS ack from `no-reply@ashbyhq.com` 2026-04-27 (outside window)
- Liberty Personnel Services, Director PM — last app-related email: outbound from `mmavvaj@gmail.com` to `bf@libertyjobs.com` 2026-04-27 (outside window); no inbound reply yet
- Customer.io, Director PM — last app-related email: ATS ack from `no-reply@us.greenhouse-mail.io` 2026-04-27 (outside window)
- Nava, Director of Product — last app-related email: ATS ack + security code from `no-reply@us.greenhouse-mail.io` 2026-04-27 (outside window)

## Outreach replies detected

None within the window. No new messages from Brian Patrick Feeley, Matthew Wensing, or Leanna Miller via email or LinkedIn relay (`messaging-noreply@linkedin.com`).

## Notes / errors during scan

- `search_emails` operator `after:` returned no results for any company-scoped query, while bare-keyword queries returned full hit lists across all dates. Treating the operator as unsupported for this MCP and relying on returned `date` field for window filtering.
- Hits inside the window that were not application-related (excluded as noise): LinkedIn weekly newsletter `newsletters-noreply@linkedin.com` 2026-04-28 21:45 UTC; multiple `jobalerts-noreply@linkedin.com` job-alert digests for unrelated postings (ACI Worldwide, Storm2, Hiya, Deloitte, Sabert, Ripple, Amazon, Denali, Oura, Jack & Jill); Interview Cake newsletter; Glassdoor Bowl Buzz; Prosper marketing; Volvo dealer marketing; Saucey marketing.
- One within-window LinkedIn job alert that mentions Nava (`director product: Nava - Director of Product posted on 4/27/26` 2026-04-28 13:06 UTC) is from the JYMBII alert system mirroring the existing posting; it is *outside* the 12-hour window (13:06 UTC = 09:06 ET, before the 17:31 ET cutoff) and is not a status signal regardless. Flagged here only because the search hit on the company name.
- No knock-out / disqualification / interview / schedule keywords surfaced against any active application's domain or ATS sender within the window.
- Pablo Gutiérrez Povero and José Boaventura Rodrigues (Mastercard outreach, R-275592 closed `rejected-by-employer`) were intentionally not searched per task spec (search profiles built only for non-closed apps).
