#!/usr/bin/env python3
"""Fetch a Threads post + full comment section.

Usage:
    python fetch_threads.py "<THREADS_URL>" --cookies "<NETSCAPE_COOKIES_FILE>"

Requirements:
    pip install playwright
    python -m playwright install chromium

The cookies file must be Netscape format and contain a `sessionid` line
(export with Get cookies.txt LOCALLY — see docs/01-cookies-setup.md).
"""
import argparse
import asyncio
from playwright.async_api import async_playwright

def parse_netscape(path):
    """Parse a Netscape-format cookies file into Playwright cookie dicts."""
    cookies = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split("\t")
            if len(parts) < 7:
                continue
            domain, _, path_c, secure, expires, name, value = parts[:7]
            cookies.append({
                "name": name,
                "value": value,
                "domain": domain,
                "path": path_c,
                "secure": secure == "TRUE",
                "expires": int(expires),
            })
    names = {c["name"] for c in cookies}
    assert "sessionid" in names, (
        "Invalid cookies file: no 'sessionid' found. "
        "Re-export from a logged-in browser (see docs/01)."
    )
    return cookies

async def fetch(post_url: str, cookie_file: str) -> None:
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent=("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                        "AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/126.0.0.0 Safari/537.36"),
            locale="zh-TW",
        )
        await context.add_cookies(parse_netscape(cookie_file))
        page = await context.new_page()
        await page.goto(post_url, wait_until="domcontentloaded", timeout=60000)
        await page.wait_for_timeout(6000)          # let JS render

        # Scroll to trigger comment lazy-loading
        for _ in range(8):
            await page.mouse.wheel(0, 2000)
            await page.wait_for_timeout(1200)

        # Expand collapsed comments ("顯示更多 / Show more")
        try:
            more = page.locator("text=顯示更多")
            n = await more.count()
            for i in range(min(n, 5)):
                try:
                    await more.nth(i).click(timeout=3000)
                    await page.wait_for_timeout(1500)
                except Exception:
                    pass
        except Exception:
            pass

        text = await page.evaluate("document.body.innerText")
        print(text)
        await browser.close()

def main():
    ap = argparse.ArgumentParser(description="Fetch Threads post + comments")
    ap.add_argument("url", help="https://www.threads.net/@user/post/XXX")
    ap.add_argument("--cookies", required=True,
                    help="Netscape cookies file for threads.net")
    args = ap.parse_args()
    asyncio.run(fetch(args.url, args.cookies))

if __name__ == "__main__":
    main()
