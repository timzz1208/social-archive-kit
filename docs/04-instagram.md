# 04 · Instagram

> IG Reels/IGTV scraping **needs cookies**. The classic failure is `Instagram sent an empty media response` — 99% of the time it means no/stale cookies.

> IG Reels／IGTV 爬取**需要 cookies**。最經典的失敗是 `Instagram sent an empty media response`——99% 是沒有 cookies 或 cookies 過期。

## 4.1 Prerequisites / 前置

1. Export cookies for `instagram.com`（docs/01）— **the account must be logged in** in the browser.
2. Verify the file has a `sessionid`:

```bash
grep -c sessionid www.instagram.com_cookies.txt   # expect ≥ 1
```

## 4.2 Usage / 用法

```bash
python scripts/download_video.py "https://www.instagram.com/reel/XXX/" \
       --cookies "C:\...\www.instagram.com_cookies.txt"
```

Or raw:

```bash
yt-dlp --cookies "FILE" -f "bv*[ext=mp4]+ba[ext=m4a]/b" -o "reel.%(ext)s" "IG_URL"
```

## 4.3 Profile / carousel archive / 帳號／多圖存檔

```bash
# All posts of a profile (pictures + videos)
gallery-dl --cookies "FILE" "https://www.instagram.com/username/"
```

`gallery-dl` complements `yt-dlp` for image galleries; it has no Threads extractor (see docs/05).

## 4.4 Pitfalls / 陷阱

- **`challenge_required`** = Instagram suspects automated access. Causes: old cookies, new IP, high frequency. Fix: log in via browser again, re-export, and **slow down** (this kit is low-frequency by design).
- **Empty media response** = cookies missing/stale → re-export (docs/01 §1.5).
- **Don't hit `i.instagram.com/api/v1/` directly** with exported cookies — that private API route triggers challenges fast.
- IG is the platform most likely to lock a session; keep volume tiny and human-paced.
