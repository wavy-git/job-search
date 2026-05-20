#!/usr/bin/env python3
"""Scan target companies' careers pages and collect roles that pass hard filters.

Collect-only by design. No scoring, no ranking. Strategy doc Rubric 1 screening
is applied later by a human reviewer over the snapshot file this script writes.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import pathlib
import random
import re
import sys
import time
from dataclasses import asdict, dataclass
from typing import Any, Callable
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

ROOT = pathlib.Path(__file__).resolve().parent
CACHE_DIR = ROOT / ".cache"
DEFAULT_OUT_DIR = ROOT / "outputs" / "scanner"
CACHE_TTL_SECONDS = 6 * 60 * 60
REQUEST_TIMEOUT = 30
POLITE_DELAY_RANGE = (2.0, 5.0)
USER_AGENT = "job-scanner/1.0 (personal use)"

MAX_POSTED_AGE_DAYS = 7
MAX_PLAYWRIGHT_DETAIL_FETCHES = 30

# Title keywords from job-search-strategy.md hard filters. Title must contain
# at least one of these (case-insensitive) to pass. Acceptable functions only.
TITLE_KEYWORDS = [
    # Product
    "product", "head of product", "vp product", "chief product", "cpo",
    # Strategy
    "strategy", "strategic initiatives", "chief strategy", "cso",
    # Operations
    "operations", " ops ", "operating officer", "coo", "chief operating",
    # Transformation
    "transformation", "business transformation", "digital transformation",
    # Innovation
    "innovation", "chief innovation",
    # Platform
    "platform", "technical platform", "platform engineering",
    # Program / Project Management
    "program management", "program manager", "project management", "pmo",
    "project management office",
    # Process
    "process excellence", "process improvement", "business process",
    "continuous improvement", "lean",
    # Delivery
    "delivery", "director of delivery", "head of delivery",
    # Implementation
    "implementation", "head of implementation",
    # General Mgmt
    "general manager", " gm ", "head of business", "business head",
    # Chief of Staff
    "chief of staff",
]

# Engineering / IC tracks to exclude even if they pass other keywords.
EXCLUDE_TITLE_TOKENS = [
    "engineer", "engineering manager", "tech lead", "technical lead",
    "architect", "developer", "designer", "scientist",
]

LOCATION_PATTERNS = [
    r"\bremote\b",
    r"\bphiladelphia\b", r"\bphila\b",
    r"\bnew york\b", r"\bnyc\b", r"\bny\b",
    r"\bseattle\b",
    r"\blos angeles\b", r"\bl\.?a\.?\b",
    r"\bsan francisco\b", r"\bbay area\b", r"\bsf\b",
    r"\bportugal\b", r"\blisbon\b",
    r"\bspain\b", r"\bmadrid\b", r"\bbarcelona\b",
]


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

@dataclass
class Job:
    company: str
    title: str
    location: str
    posted_date: str | None
    remote: bool
    jd_text: str
    apply_url: str
    source_ats: str


# ---------------------------------------------------------------------------
# Cache
# ---------------------------------------------------------------------------

def _cache_path(key: str) -> pathlib.Path:
    h = hashlib.sha256(key.encode()).hexdigest()[:16]
    return CACHE_DIR / f"{h}.json"


def cache_get(key: str) -> Any | None:
    p = _cache_path(key)
    if not p.exists():
        return None
    try:
        data = json.loads(p.read_text())
    except (json.JSONDecodeError, OSError):
        return None
    if time.time() - data.get("ts", 0) > CACHE_TTL_SECONDS:
        return None
    return data.get("value")


def cache_set(key: str, value: Any) -> None:
    CACHE_DIR.mkdir(exist_ok=True)
    _cache_path(key).write_text(json.dumps({"ts": time.time(), "value": value}))


# ---------------------------------------------------------------------------
# HTTP
# ---------------------------------------------------------------------------

_last_request_per_host: dict[str, float] = {}


def polite_get(url: str) -> requests.Response:
    host = urlparse(url).netloc
    delay = random.uniform(*POLITE_DELAY_RANGE)
    wait = max(0.0, _last_request_per_host.get(host, 0.0) + delay - time.time())
    if wait > 0:
        time.sleep(wait)
    _last_request_per_host[host] = time.time()
    resp = requests.get(url, timeout=REQUEST_TIMEOUT, headers={"User-Agent": USER_AGENT})
    resp.raise_for_status()
    return resp


def get_json(url: str) -> Any:
    cached = cache_get(url)
    if cached is not None:
        return cached
    data = polite_get(url).json()
    cache_set(url, data)
    return data


def html_to_text(html: str) -> str:
    return BeautifulSoup(html or "", "html.parser").get_text(" ", strip=True)


# ---------------------------------------------------------------------------
# ATS adapters
# ---------------------------------------------------------------------------

def fetch_greenhouse(company: str, slug: str) -> list[Job]:
    url = f"https://boards-api.greenhouse.io/v1/boards/{slug}/jobs?content=true"
    data = get_json(url)
    jobs: list[Job] = []
    for j in data.get("jobs", []):
        location = ((j.get("location") or {}).get("name") or "").strip()
        jd_text = html_to_text(j.get("content", ""))
        posted = j.get("updated_at") or j.get("first_published") or ""
        posted_date = posted.split("T")[0] if posted else None
        jobs.append(Job(
            company=company,
            title=j.get("title", ""),
            location=location,
            posted_date=posted_date,
            remote="remote" in location.lower(),
            jd_text=jd_text,
            apply_url=j.get("absolute_url", ""),
            source_ats="greenhouse",
        ))
    return jobs


def fetch_lever(company: str, slug: str) -> list[Job]:
    url = f"https://api.lever.co/v0/postings/{slug}?mode=json"
    data = get_json(url)
    jobs: list[Job] = []
    for j in data:
        cat = j.get("categories") or {}
        location = cat.get("location", "") or ""
        workplace = j.get("workplaceType", "") or ""
        parts = [html_to_text(j.get("description", ""))]
        for lst in j.get("lists") or []:
            parts.append(html_to_text(lst.get("content", "")))
        parts.append(html_to_text(j.get("additional", "")))
        jd_text = " ".join(p for p in parts if p)
        created_at = j.get("createdAt")
        posted_date = (
            dt.datetime.fromtimestamp(created_at / 1000, tz=dt.timezone.utc).date().isoformat()
            if created_at else None
        )
        is_remote = "remote" in (workplace + " " + location).lower()
        jobs.append(Job(
            company=company,
            title=j.get("text", ""),
            location=location,
            posted_date=posted_date,
            remote=is_remote,
            jd_text=jd_text,
            apply_url=j.get("hostedUrl") or j.get("applyUrl", ""),
            source_ats="lever",
        ))
    return jobs


def fetch_ashby(company: str, slug: str) -> list[Job]:
    url = f"https://api.ashbyhq.com/posting-api/job-board/{slug}?includeCompensation=true"
    data = get_json(url)
    jobs: list[Job] = []
    for j in data.get("jobs", []):
        location = j.get("locationName", "") or ""
        jd_text = j.get("descriptionPlain") or html_to_text(j.get("descriptionHtml", ""))
        published = j.get("publishedAt") or ""
        posted_date = published.split("T")[0] if published else None
        is_remote = bool(j.get("isRemote")) or "remote" in location.lower()
        jobs.append(Job(
            company=company,
            title=j.get("title", ""),
            location=location,
            posted_date=posted_date,
            remote=is_remote,
            jd_text=jd_text or "",
            apply_url=j.get("jobUrl") or j.get("applyUrl", ""),
            source_ats="ashby",
        ))
    return jobs


def fetch_smartrecruiters(company: str, slug: str) -> list[Job]:
    base = f"https://api.smartrecruiters.com/v1/companies/{slug}/postings"
    jobs: list[Job] = []
    offset, limit = 0, 100
    for _ in range(20):
        page_data = get_json(f"{base}?limit={limit}&offset={offset}")
        content = page_data.get("content", [])
        if not content:
            break
        for summary in content:
            posting_id = summary.get("id")
            detail = get_json(f"{base}/{posting_id}") if posting_id else summary
            loc = (summary.get("location") or detail.get("location") or {})
            location_str = ", ".join(
                filter(None, [loc.get("city"), loc.get("region"), loc.get("country")])
            )
            is_remote = bool(loc.get("remote")) or "remote" in location_str.lower()
            sections = ((detail.get("jobAd") or {}).get("sections") or {})
            jd_parts: list[str] = []
            for sec in sections.values():
                if isinstance(sec, dict):
                    jd_parts.append(html_to_text(sec.get("text", "")))
            jd_text = " ".join(p for p in jd_parts if p)
            posted = detail.get("releasedDate") or summary.get("releasedDate") or ""
            posted_date = posted.split("T")[0] if posted else None
            jobs.append(Job(
                company=company,
                title=summary.get("name", ""),
                location=location_str,
                posted_date=posted_date,
                remote=is_remote,
                jd_text=jd_text,
                apply_url=(
                    summary.get("applyUrl")
                    or f"https://jobs.smartrecruiters.com/{slug}/{posting_id}"
                ),
                source_ats="smartrecruiters",
            ))
        offset += limit
        if len(content) < limit:
            break
    return jobs


def fetch_workday(company: str, url: str) -> list[Job]:
    return _fetch_via_playwright(company, url, ats_label="workday")


def fetch_html(company: str, url: str) -> list[Job]:
    return _fetch_via_playwright(company, url, ats_label="html")


def _playwright_listing_html(url: str) -> str:
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(user_agent=USER_AGENT)
        page = context.new_page()
        page.goto(url, wait_until="networkidle", timeout=60_000)
        page.wait_for_timeout(3000)
        for _ in range(5):
            page.mouse.wheel(0, 10000)
            page.wait_for_timeout(800)
        html = page.content()
        browser.close()
    return html


def _extract_candidate_links(html: str, base_url: str) -> list[dict]:
    soup = BeautifulSoup(html, "html.parser")
    base_host = urlparse(base_url).netloc
    seen: set[tuple[str, str]] = set()
    results: list[dict] = []
    for a in soup.find_all("a"):
        href = (a.get("href") or "").strip()
        text = a.get_text(" ", strip=True)
        if not href or not text or len(text) < 4 or len(text) > 150:
            continue
        if href.startswith(("#", "mailto:", "javascript:")):
            continue
        abs_url = urljoin(base_url, href)
        host = urlparse(abs_url).netloc
        if host != base_host and "myworkdayjobs.com" not in host:
            continue
        key = (text, abs_url)
        if key in seen:
            continue
        seen.add(key)
        results.append({"title": text, "url": abs_url})
    return results


def _fetch_via_playwright(company: str, url: str, ats_label: str) -> list[Job]:
    listing_key = f"pw:list:{url}"
    candidates = cache_get(listing_key)
    if candidates is None:
        try:
            html = _playwright_listing_html(url)
        except Exception as e:
            raise RuntimeError(f"playwright listing fetch failed: {e}") from e
        candidates = _extract_candidate_links(html, url)
        cache_set(listing_key, candidates)

    filtered = [c for c in candidates if title_matches(c["title"])]
    filtered = filtered[:MAX_PLAYWRIGHT_DETAIL_FETCHES]

    jobs: list[Job] = []
    if not filtered:
        return jobs

    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(user_agent=USER_AGENT)
        page = context.new_page()
        for c in filtered:
            detail_key = f"pw:detail:{c['url']}"
            cached = cache_get(detail_key)
            if cached is not None:
                jobs.append(Job(**cached))
                continue
            try:
                page.goto(c["url"], wait_until="networkidle", timeout=60_000)
                page.wait_for_timeout(2000)
                dhtml = page.content()
            except Exception:
                dhtml = ""
            dsoup = BeautifulSoup(dhtml, "html.parser")
            for tag in dsoup(["script", "style", "nav", "header", "footer"]):
                tag.decompose()
            body = dsoup.find("main") or dsoup.body or dsoup
            jd_text = body.get_text(" ", strip=True)[:20000]
            job = Job(
                company=company,
                title=c["title"],
                location=_extract_location_hint(jd_text),
                posted_date=None,
                remote="remote" in jd_text.lower()[:3000],
                jd_text=jd_text,
                apply_url=c["url"],
                source_ats=ats_label,
            )
            jobs.append(job)
            cache_set(detail_key, asdict(job))
            time.sleep(random.uniform(*POLITE_DELAY_RANGE))
        browser.close()
    return jobs


def _extract_location_hint(jd: str) -> str:
    m = re.search(r"location[:\s]+([A-Za-z][A-Za-z0-9,\.\- ]{3,60})", jd, re.IGNORECASE)
    return m.group(1).strip() if m else ""


# ---------------------------------------------------------------------------
# Filtering
# ---------------------------------------------------------------------------

def title_matches(title: str) -> bool:
    """Title passes if it contains any wanted function keyword AND no excluded token."""
    t = " " + (title or "").lower() + " "
    if any(tok in t for tok in EXCLUDE_TITLE_TOKENS):
        return False
    return any(kw in t for kw in TITLE_KEYWORDS)


def location_matches(job: Job) -> bool:
    if job.remote:
        return True
    loc = (job.location or "").lower()
    if not loc:
        # Unknown location (common for Workday/HTML) — let it through; user
        # filters visually. Title + age filters still apply.
        return True
    return any(re.search(p, loc) for p in LOCATION_PATTERNS)


def within_age_window(job: Job) -> bool:
    if not job.posted_date:
        return True
    try:
        posted = dt.date.fromisoformat(job.posted_date)
    except ValueError:
        return True
    return (dt.date.today() - posted).days <= MAX_POSTED_AGE_DAYS


def passes_filters(job: Job) -> bool:
    return title_matches(job.title) and location_matches(job) and within_age_window(job)


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------

def write_markdown(jobs: list[Job], path: pathlib.Path, totals: dict[str, int]) -> None:
    """Write a flat snapshot, sorted by company. No scoring, no buckets."""
    today = dt.date.today().isoformat()
    sorted_jobs = sorted(jobs, key=lambda j: (j.company.lower(), j.title.lower()))

    lines: list[str] = [
        f"# Scanner Snapshot, {today}",
        "",
        "Collect-only output. No scoring, no ranking. Apply Rubric 1 screening manually.",
        "",
        "## Scan totals",
        "",
        f"- Companies scraped: {totals.get('scraped', 0)} / {totals.get('total', 0)}",
        f"- Total postings found: {totals.get('found', 0)}",
        f"- After hard filters (title keyword, location, recency): {len(jobs)}",
        "",
        "## Postings (sorted by company)",
        "",
        "| Company | Title | Location | Posted | Source | Apply Link |",
        "|---|---|---|---|---|---|",
    ]
    for j in sorted_jobs:
        location = j.location or "(unknown)"
        if j.remote and "remote" not in location.lower():
            location = f"{location} [remote]" if location != "(unknown)" else "Remote"
        posted = j.posted_date or "unknown"
        # Escape pipe characters in fields to keep table parseable
        company = j.company.replace("|", "\\|")
        title = j.title.replace("|", "\\|")
        location = location.replace("|", "\\|")
        lines.append(
            f"| {company} | {title} | {location} | {posted} | {j.source_ats} | {j.apply_url} |"
        )
    lines.append("")
    path.write_text("\n".join(lines))


def write_json(jobs: list[Job], path: pathlib.Path, totals: dict[str, int]) -> None:
    """Write JSON snapshot. Includes totals and sorted job list."""
    sorted_jobs = sorted(jobs, key=lambda j: (j.company.lower(), j.title.lower()))
    out = {
        "date": dt.date.today().isoformat(),
        "totals": totals,
        "jobs": [asdict(j) for j in sorted_jobs],
    }
    path.write_text(json.dumps(out, indent=2))


# ---------------------------------------------------------------------------
# Orchestration
# ---------------------------------------------------------------------------

FETCHERS: dict[str, Callable[..., list[Job]]] = {
    "greenhouse": fetch_greenhouse,
    "lever": fetch_lever,
    "ashby": fetch_ashby,
    "smartrecruiters": fetch_smartrecruiters,
    "workday": fetch_workday,
    "html": fetch_html,
}


def run(config_path: pathlib.Path, out_dir: pathlib.Path) -> int:
    companies = json.loads(config_path.read_text())
    all_jobs: list[Job] = []
    scraped = 0
    errors: list[str] = []

    for c in companies:
        name = c["name"]
        ats = c["ats"]
        fetcher = FETCHERS.get(ats)
        if not fetcher:
            errors.append(f"{name}: unknown ATS '{ats}'")
            continue
        arg = c.get("slug") or c.get("url")
        if not arg:
            errors.append(f"{name}: missing slug/url")
            continue
        print(f"[scrape] {name} via {ats} ({arg})", flush=True)
        try:
            jobs = fetcher(name, arg)
            all_jobs.extend(jobs)
            scraped += 1
            print(f"  -> {len(jobs)} postings", flush=True)
        except Exception as e:
            errors.append(f"{name}: {type(e).__name__}: {e}")
            print(f"  FAILED: {type(e).__name__}: {e}", flush=True)

    matched = [j for j in all_jobs if passes_filters(j)]

    today = dt.date.today().isoformat()
    out_dir.mkdir(parents=True, exist_ok=True)
    md_path = out_dir / f"jobs_{today}.md"
    json_path = out_dir / f"jobs_{today}.json"
    totals = {
        "scraped": scraped,
        "total": len(companies),
        "found": len(all_jobs),
        "matched": len(matched),
    }
    write_markdown(matched, md_path, totals)
    write_json(matched, json_path, totals)

    print()
    print("=== Summary ===")
    print(f"Companies scraped: {scraped}/{len(companies)}")
    print(f"Total postings found: {len(all_jobs)}")
    print(f"Matched after hard filters: {len(matched)}")
    print(f"Output: {md_path}, {json_path}")
    if errors:
        print(f"\nErrors ({len(errors)}):")
        for e in errors:
            print(f"  - {e}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", default=str(ROOT / "target_companies.json"))
    parser.add_argument("--out", default=str(DEFAULT_OUT_DIR))
    args = parser.parse_args()
    return run(pathlib.Path(args.config), pathlib.Path(args.out))


if __name__ == "__main__":
    sys.exit(main())
