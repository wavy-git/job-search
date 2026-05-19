# Application Status Check, 2026-05-14 05:31 ET

Folders searched: ALL (search_emails spans all Fastmail folders)

Window: 2026-05-13 21:31 UTC to 2026-05-14 09:31 UTC (last 12 hours)

## Potential transitions

None. No emails in the 12-hour window match any active application search profile (company domain, ATS sender pattern, outreach contact name, or Job ID / role / company keyword).

## No new emails for these applications

- Liberty Personnel Services (LinkedIn 4366542359) — Director Product Management — last checked 2026-05-14 05:31 ET
- Customer.io (Greenhouse 7775708) — Director, Product Management — last checked 2026-05-14 05:31 ET
- Toast (LinkedIn 4345032625) — Senior Product Manager, Core Payments — last checked 2026-05-14 05:31 ET
- Forsyth Barnes (LinkedIn 4405363504) — Senior / Principal Forward Deployed PM — last checked 2026-05-14 05:31 ET
- Nava (Greenhouse 4210653009) — Director of Product — last checked 2026-05-14 05:31 ET
- Mastercard (LinkedIn 4404123247) — Director, AI Product Definition & Execution — last checked 2026-05-14 05:31 ET
- Leap / Leapfrog Power (LinkedIn 4383181854) — Senior Product Manager — last checked 2026-05-14 05:31 ET

## Outreach replies detected

None in the 12-hour window. No new LinkedIn messages from outreach contacts (Brian Patrick Feeley, Jessica Dobie, Matthew Wensing, Leanna Miller, Pablo Gutiérrez Povero, José Boaventura Rodrigues) and no `messaging-noreply@linkedin.com` traffic matching any contact name.

## Notes / errors during scan

- Inbox traffic in the 12-hour window is non-application: HBR Management Tip (2026-05-14 08:21 UTC), IFTTT marketing (2026-05-14 00:50 UTC), LinkedIn job alert digests (`jobalerts-noreply@linkedin.com` 2026-05-13 23:49 UTC for "director product" → Thrively, and 2026-05-13 22:49 UTC for "head of product" → Remitly), Orangetheory marketing (2026-05-13 20:49 UTC). None map to an active application company or outreach contact.
- Fastmail `search_emails` quirk: queries using `from:linkedin.com` return zero results even when keyword "linkedin" surfaces LinkedIn senders. The `from:` operator appears to require the exact sender address, not a domain. Workaround in use: layered keyword + name probes per profile.
- Carried over from prior check, NOT in 12-hour scope but still pending manual reconciliation in `applications.md` (surface only, no auto-update):
  - Customer.io: email from `no-reply@customerio.com` on 2026-05-05 18:15 UTC, subject "Customer.io: Director, Product Management Application Update". Preview language is ambiguous (thank-you or soft rejection). Current Funnel Status = `submitted`. Recommend fetching full body and reconciling.
  - Leap / Leapfrog Power: email from `noreply@candidates.workablemail.com` on 2026-05-07 15:29 UTC, subject "Sr. Product Manager - Leapfrog Power, Inc.". Preview ("we regret to inform you that you have not been selected for further consideration") is a clear rejection. Current Funnel Status = `submitted`. Recommend updating to `rejected-by-employer` dated 2026-05-07.
