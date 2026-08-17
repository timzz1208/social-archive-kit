#!/usr/bin/env python3
"""Optional local cookie extractor — no browser extension needed.

Extracts cookies for a given domain from your browser's cookie store and
writes them to a Netscape-format file that yt-dlp / Playwright can use.

Usage:
    python cookie_extract.py threads      # domain substring filter
    python cookie_extract.py instagram -b edge -o out.txt

⚠️ Reading a browser cookie DB may trigger antivirus prompts (credential-like
access). This is expected; allow for your own profile only. If AV blocks it,
fall back to the extension route (docs/01) — the exported file is identical.
"""
import argparse
import sys


def main():
    ap = argparse.ArgumentParser(description="Extract cookies from browser")
    ap.add_argument("domain",
                    help="Domain substring to keep (e.g. threads, instagram)")
    ap.add_argument("-b", "--browser", default="chrome",
                    help="chrome / edge / firefox (default: chrome)")
    ap.add_argument("-o", "--output", default="cookies.txt",
                    help="Output Netscape file")
    args = ap.parse_args()

    try:
        from yt_dlp.cookies import extract_cookies_from_browser
    except ImportError:
        sys.exit("yt-dlp required: pip install yt-dlp")

    try:
        jar = extract_cookies_from_browser(args.browser)
    except Exception as e:
        sys.exit(f"Failed to read browser cookies ({args.browser}): {e}\n"
                 "If your browser is running, close it and retry, or use the "
                 "extension export route (docs/01).")

    kept = [c for c in jar if args.domain.lower() in c.domain.lower()]
    if not kept:
        sys.exit(f"No cookies found for domain containing '{args.domain}' "
                 f"in {args.browser}. Are you logged in to that site?")

    with open(args.output, "w", encoding="utf-8") as f:
        f.write("# Netscape HTTP Cookie File\n")
        for c in kept:
            f.write("\t".join([
                c.domain, "TRUE", c.path,
                "TRUE" if c.secure else "FALSE",
                str(int(c.expires)) if c.expires else "0",
                c.name, c.value,
            ]) + "\n")

    print(f"Wrote {len(kept)} cookies -> {args.output}")
    print("Security: this file is your account key. Keep it local, never "
          "commit it, never paste it into chats.")


if __name__ == "__main__":
    main()
