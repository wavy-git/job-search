# Application Status Check, 2026-04-28 10:23 ET

Folders searched: ALL (search_emails spans all Fastmail folders)

Lookback window: 2026-04-27 22:23 ET to 2026-04-28 10:23 ET (12 hours)

Note: Off-schedule on-demand run (scheduled slots are 05:30 and 13:30 ET); HH=10 used in filename to distinguish from scheduled snapshots.

Search profiles built and queried:

- ElectronX (Head of Product, LinkedIn 4392197135): from:electronx.com, from:ashbyhq.com (Ashby ATS), keyword "ElectronX"
- Wheel (Sr PM Operational Intelligence, Ashby 656c9648): from:wheel.com, from:ashbyhq.com, keyword "Wheel"
- Sourgum (Head of Product, Ashby a8720ec5): from:sourgum.com, from:ashbyhq.com, keyword "Sourgum"
- Liberty Personnel Services (Director PM, LinkedIn 4366542359): from:libertyjobs.com, keywords "Liberty Personnel" and "Brian Feeley"
- Customer.io (Director PM, Greenhouse 7775708): from:customer.io, from:greenhouse-mail.io, keyword "Customer.io"
- Nava (Director of Product, Greenhouse 4210653009): from:navapbc.com, from:greenhouse-mail.io, keyword "Nava"

Cross-cutting searches: from:myworkday.com, from:lever.co, from:messaging-noreply@linkedin.com, body keywords "phone screen", "next steps", "unfortunately decided", "your application", outreach contact names (Pablo, Boaventura, Jessica Dobie, Matthew Wensing, Leanna Miller, Brian Feeley).

## Potential transitions

None detected within the 12-hour window.

No company-domain emails, no ATS provider emails (Ashby, Greenhouse, Workday, Lever, SmartRecruiters, Workable), and no recruiter or HM emails were received in the window for any of the six active applications. The only application-adjacent inbound during the window is one LinkedIn job-alert digest that lists the Nava posting (a generic aggregator alert, not a status signal).

### Nava - Director of Product (Greenhouse 4210653009)
- Current Funnel Status: submitted
- Email matched: jobalerts-noreply@linkedin.com - "director product: Nava - Director of Product posted on 4/27/26" - received 2026-04-28 09:06 EDT
- Confidence: low
- Suggested transition: none (no transition; this is a LinkedIn keyword-alert digest, not a recruiter or ATS communication)
- Email body excerpt (first 200 chars):
  > (subject only; LinkedIn alert digest body not retrieved)

## No new emails for these applications

- ElectronX - Head of Product - last in-window check 2026-04-28 10:23 ET
- Wheel - Senior Product Manager, Operational Intelligence - last in-window check 2026-04-28 10:23 ET
- Sourgum - Head of Product - last in-window check 2026-04-28 10:23 ET
- Liberty Personnel Services - Director Product Management - last in-window check 2026-04-28 10:23 ET
- Customer.io - Director, Product Management - last in-window check 2026-04-28 10:23 ET
- Nava - Director of Product - last in-window check 2026-04-28 10:23 ET (one low-confidence LinkedIn alert match logged above; no recruiter or HM communication)

## Outreach replies detected

None detected within the 12-hour window.

Searched contacts: Pablo Gutiérrez Povero, José Boaventura Rodrigues, Jessica Dobie, Brian Patrick Feeley, Matthew Wensing, Leanna Miller. No emails from these senders, no LinkedIn-message notifications (`messaging-noreply@linkedin.com`) referencing any of these names.

## Notes / errors during scan

- The body keyword `ElectronX` returns expansive fuzzy matches (Hyundai/Volvo dealer mail, etc.) on Fastmail's search backend. Domain-scoped and ATS-scoped searches are the reliable path; ignoring noise from broad keyword fan-out.
- Customer.io application receipt (no-reply@us.greenhouse-mail.io, 2026-04-27 13:04 ET, "Thank you for applying to Customer.io") and Nava application receipts (no-reply@us.greenhouse-mail.io, 2026-04-27 18:04 ET) sit just outside the 12-hour window and are already reflected in applications.md as `submitted`. No action.
- Liberty Personnel LinkedIn application-viewed notification (jobs-noreply@linkedin.com, 2026-04-27 14:04 ET) is also outside the window. No action.
- Run executed off-schedule (10:23 ET) rather than at the scheduled 05:30 or 13:30 ET slots. The next scheduled snapshot at 13:30 ET will cover any inbound between approximately 01:30 ET and 13:30 ET, which overlaps but does not duplicate this 22:23 ET to 10:23 ET window.
- No errors during scan.
