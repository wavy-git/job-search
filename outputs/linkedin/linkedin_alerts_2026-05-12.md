# LinkedIn Alerts Snapshot, 2026-05-12

Senders scanned: jobs-listings@linkedin.com, jobalerts-noreply@linkedin.com, jobs-noreply@linkedin.com
Time window: last 24 hours (2026-05-11T09:07Z to 2026-05-12T09:07Z)
Folders searched: ALL (search_emails spans all Fastmail folders, including Ignore)

## Scan totals

| Sender | Emails parsed | Postings extracted | Last-seen receipt |
|---|---|---|---|
| jobs-listings@linkedin.com | 1 | 6 | 2026-05-11 |
| jobalerts-noreply@linkedin.com | 1 | 6 | 2026-05-11 |
| jobs-noreply@linkedin.com | 0 | 0 | 2026-05-10 (outside 24h window) |
| TOTAL | 2 | 12 (after dedup) | |

After hard filters: 12 roles passed.

## Postings (sorted by company)

| Company | Title | Location | Posted Date | Apply Link | Source Sender | Source Subject |
|---|---|---|---|---|---|---|
| Chubb | VP, Global Transformation Programs | Jersey City, NJ | 2026-05-11 (email receipt proxy) | https://www.linkedin.com/jobs/view/4409624691/ | jobs-listings@linkedin.com | Chubb is hiring a VP, Global Transformation Programs |
| Guild | Principal Technical Program Manager | United States | 2026-05-11 (email receipt proxy) | https://www.linkedin.com/jobs/view/4380144940/ | jobs-listings@linkedin.com | Chubb is hiring a VP, Global Transformation Programs |
| Iopa Solutions | Head of Product (Treasury & Cash Management Software) | United States | 2026-05-11 (email receipt proxy) | https://www.linkedin.com/jobs/view/4409911755/ | jobs-listings@linkedin.com | Chubb is hiring a VP, Global Transformation Programs |
| JPMorganChase | Point-of-Sale Product Manager, Payments, Vice President | Jersey City, NJ | 2026-05-11 (email receipt proxy) | https://www.linkedin.com/jobs/view/4403572595/ | jobalerts-noreply@linkedin.com | "product manager": Plaid - Product Lead - Money Movement posted on 5/9/26 |
| Mediavine | Sr. Director, Product Delivery | New York, NY | 2026-05-11 (email receipt proxy) | https://www.linkedin.com/jobs/view/4411643807/ | jobs-listings@linkedin.com | Chubb is hiring a VP, Global Transformation Programs |
| Otter | Product Manager, Money Platform | New York, NY | 2026-05-11 (email receipt proxy) | https://www.linkedin.com/jobs/view/4371708110/ | jobalerts-noreply@linkedin.com | "product manager": Plaid - Product Lead - Money Movement posted on 5/9/26 |
| Plaid | Product Lead, Money Movement | New York, NY | 2026-05-09 | https://www.linkedin.com/jobs/view/4336913856/ | jobalerts-noreply@linkedin.com | "product manager": Plaid - Product Lead - Money Movement posted on 5/9/26 |
| Smarsh | Senior Director, Product Management | New York, NY | 2026-05-11 (email receipt proxy) | https://www.linkedin.com/jobs/view/4411881278/ | jobs-listings@linkedin.com | Chubb is hiring a VP, Global Transformation Programs |
| third | VP of Delivery | United States | 2026-05-11 (email receipt proxy) | https://www.linkedin.com/jobs/view/4411712743/ | jobs-listings@linkedin.com | Chubb is hiring a VP, Global Transformation Programs |
| Toppan Merrill | Principal Product Manager | Middlesex County, NJ | 2026-05-11 (email receipt proxy) | https://www.linkedin.com/jobs/view/4402748949/ | jobalerts-noreply@linkedin.com | "product manager": Plaid - Product Lead - Money Movement posted on 5/9/26 |
| Toppan Merrill | Principal Product Manager | Queens County, NY | 2026-05-11 (email receipt proxy) | https://www.linkedin.com/jobs/view/4402753190/ | jobalerts-noreply@linkedin.com | "product manager": Plaid - Product Lead - Money Movement posted on 5/9/26 |
| Weedmaps | Staff Product Manager, Enterprise Business Applications (Remote) | New York, NY (Remote) | 2026-05-11 (email receipt proxy) | https://www.linkedin.com/jobs/view/4396166609/ | jobalerts-noreply@linkedin.com | "product manager": Plaid - Product Lead - Money Movement posted on 5/9/26 |

## Filter notes

No rows dropped at hard filters. All 12 extracted postings passed title-keyword, location, and 7-day-recency checks.

Filter interpretation notes:

- Title keywords matched as case-insensitive substrings. Examples that passed: "Transformation Programs" (transformation), "Principal Technical Program Manager" (program manager; "technical" is not on the exclusion list - only "tech lead" / "technical lead" are), "VP of Delivery" (delivery), "Money Platform" (product, platform).
- Location interpretation: "Jersey City, NJ" passed as Greater NYC / NJ (Hoboken/Jersey City are NYC-metro). "Middlesex County, NJ" passed as NJ city (NJ cities allowed per rules). "Queens County, NY" passed as NYC borough. "United States" passed through as USA-without-explicit-indicator.
- Posted dates: Only Plaid's posting carried an explicit date in the email subject (5/9/26). All other rows use the email receipt date (2026-05-11) as a proxy, per task instructions.
- Volume note: today's snapshot is unusually small because only one JYMBII digest and one keyword-alert email arrived in the 24-hour window. The other 6 saved keyword alerts ("head of product", "director product", "director pmo", "director product payments remote", etc.) and the jobs-noreply similarity digest did not deliver in the last 24 hours. Previous snapshots typically see 8 to 9 alert emails per day.

## Reminders

- Add more LinkedIn alerts in the interim while web-scraping path is unresolved. Target keywords: fintech, payments director, head of product, principal product manager, director of platform, senior manager product, principal product manager, manager strategy. Target metros to add: LA, Portugal/Lisbon.
- Only 2 of 3 senders delivered today. jobs-noreply@linkedin.com last delivered 2026-05-10 (similar-jobs digest cadence is normally daily). Worth a check next run if pattern persists.
- Most saved alerts (head of product, director product, director pmo, etc.) did not fire in the last 24 hours despite firing daily in prior weeks. May indicate a LinkedIn-side cadence change, a quiet candidate-pool day, or a sieve/filter issue. Re-check at next run before raising.
