# ATS Resolution Notes

Companies that could not be resolved to a supported ATS (greenhouse, lever, ashby, smartrecruiters, workday with direct listing URL). Fallback: ats="html" with best careers URL. Scanner will Playwright-scrape these.

## html fallbacks

Moov Financial: careers page moov.io/careers has no detectable ATS embed.
Stax Payments: careers page uses Paylocity recruiting (recruiting.paylocity.com/recruiting/jobs/.../Stax), which this scanner does not support.
Checkout.com: careers page loads jobs dynamically via JS, no static ATS link detected.
Unit: careers page loads jobs dynamically, no static ATS link detected.
Vagaro: careers page uses Breezy HR (vagaro.breezy.hr), not a supported ATS.
Housecall Pro: no ATS detected in page HTML.
Procore: careers page uses internal /jobs/search path; no static ATS link.
Rippling: careers page has no static ATS link; jobs loaded dynamically.
Apple: uses proprietary jobs.apple.com portal.
Amazon: uses proprietary amazon.jobs portal.
Google: uses proprietary Google Careers portal.
Microsoft: uses proprietary careers.microsoft.com portal.
Meta: uses proprietary metacareers.com portal.
Uber: jobs.uber.com is proprietary; legacy SmartRecruiters/Uber has only 1 posting, not authoritative.
DoorDash: careersatdoordash.com is proprietary (Phenom People) portal.
Mastercard: careers.mastercard.com is an Oracle HCM portal, not supported.
PayPal: careers.pypl.com is proprietary (Phenom People).
Fiserv: careers.fiserv.com is an Oracle HCM portal.
FIS: careers.fisglobal.com is a proprietary portal.
Global Payments: company.globalpayments.com is a proprietary portal.
American Express: careers.americanexpress.com is an Oracle HCM portal.
GE Vernova: careers.gevernova.com is a proprietary portal.
VertexOne: no supported ATS found.
Itron: na.itron.com/careers is a SuccessFactors portal, not supported.
Enverus: enverus.com/careers has no supported ATS embed.
Uplight: uplight.com/careers has no supported ATS embed.
AutoGrid: auto-grid.com careers page has no supported ATS embed.
Kraken Technologies: kraken.tech/careers has no supported ATS embed.
Athenahealth: careers.athenahealth.com is an Oracle HCM portal.
Datavant: datavant.com/careers has no supported ATS embed.
Splunk: careers page redirects to careers.cisco.com (Cisco acquisition), not a supported ATS.
HashiCorp: careers redirect to ibm.com/careers (IBM acquisition), not a supported ATS.
Atlassian: atlassian.com/company/careers uses proprietary portal.
CrowdStrike: careers page uses proprietary portal.
Palo Alto Networks: jobs.paloaltonetworks.com uses proprietary portal.
SentinelOne: careers page mentions Greenhouse in footer but no exposed slug via API; falling back to html.
Salesforce: careers uses proprietary portal (also hiring at Salesforce Career Connect).
Retool: retool.com/careers shows "0 roles across all locations"; no ATS link exposed.
Census: getcensus.com/careers redirects to fivetran.com/careers (Fivetran acquired Census). Keeping original URL for now.
Workhuman: careers page content is minimal; no ATS link exposed.
Granicus: careers page returns SVG content; no ATS link found.
iCIMS: icims.com/about-icims/careers uses iCIMS talent cloud (self-hosted), not supported as a distinct ATS here.
Kajabi: kajabi.com/careers has no supported ATS embed.
Mercoa: mercoa.com/careers has no supported ATS embed.
Puzzle: puzzle.io/careers has no supported ATS embed.
Default: default.com/careers has no supported ATS embed.
Clay: clay.com/careers has no supported ATS embed.
