# 03 · Facebook

> Facebook public video/Reel scraping **needs cookies** — without them you get empty or partial results.

> FB 公開影片／Reels 爬取**需要 cookies**——沒有會拿到空的或不完整的結果。

## 3.1 Prerequisites / 前置

1. Export cookies for `facebook.com`（docs/01）— Netscape format.
2. Make sure you are **logged in** in the browser before exporting.

## 3.2 Usage / 用法

```bash
python scripts/download_video.py "https://www.facebook.com/..." \
       --cookies "C:\...\www.facebook.com_cookies.txt"
```

Or raw yt-dlp:

```bash
yt-dlp --cookies "C:\...\www.facebook.com_cookies.txt" -o "%(title)s.%(ext)s" "FB_URL"
```

## 3.3 Metadata first / 先看 metadata（省流量）

```bash
yt-dlp --cookies "FILE" --skip-download --print "%(title)s" --print "%(duration)s" \
       --print "%(uploader)s" "FB_URL"
```

## 3.4 Pitfalls / 陷阱

- **Cookies must match the video's country/account access.** If the video is friends-only or region-restricted for your account, scraping fails — that's access control working as intended; don't try to bypass it.
- Facebook sometimes serves content only to the browser session, not the API — if `yt-dlp` returns empty, open the video in your logged-in browser first to "warm" it, then retry.
- Reels and Watch links may need different URL forms: prefer the canonical `/videos/` or `/reel/` URL from the browser address bar.
