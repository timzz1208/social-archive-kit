#!/usr/bin/env python3
"""yt-dlp wrapper with cookie-file support for FB / IG / YT.

Usage:
    python download_video.py "<URL>" [--cookies "<FILE>"] [--audio] [-o "<NAME>"]

Platforms: YouTube (cookies optional), Facebook (cookies required),
Instagram (cookies required). For Threads use fetch_threads.py instead.
"""
import argparse
import shutil
import subprocess
import sys


def main():
    ap = argparse.ArgumentParser(description="Download a video via yt-dlp")
    ap.add_argument("url", help="Video URL (YT/FB/IG)")
    ap.add_argument("--cookies", help="Netscape cookies file (required for FB/IG)")
    ap.add_argument("--audio", action="store_true",
                    help="Extract audio only (wav)")
    ap.add_argument("-o", "--output", default="%(title)s.%(ext)s",
                    help="Output template")
    args = ap.parse_args()

    yt = shutil.which("yt-dlp")
    if not yt:
        sys.exit("yt-dlp not found. Install: pip install yt-dlp")

    cmd = [yt]
    if args.cookies:
        cmd += ["--cookies", args.cookies]
    if args.audio:
        cmd += ["-x", "--audio-format", "wav", "--audio-quality", "0"]
    cmd += ["-o", args.output, args.url]

    print(" ".join(cmd))
    raise SystemExit(subprocess.call(cmd))


if __name__ == "__main__":
    main()
