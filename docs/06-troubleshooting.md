# 06 · Troubleshooting / 排障手冊

> Every pitfall below was hit and fixed in real usage (2026). Read before opening an issue.

> 以下每個坑都是實際踩過並解決的（2026）。發 issue 前先讀。

## 6.1 Antivirus blocks the scraper / 防毒擋爬蟲

**Symptom**: AV popup when running `yt-dlp --cookies-from-browser` or Playwright; command exits with no output.

**Cause**: reading browser cookie databases (SQLite/DPAPI) looks like credential theft to AV heuristics.

**Fix**:
1. Prefer the **exported cookie file** route (docs/01) over `--cookies-from-browser` — no browser DB access.
2. If AV still flags it, allow the specific Python/yt-dlp executable for your own profile only.
3. Never disable AV globally to "make it work".

## 6.2 Cookies expired / cookies 過期

**Symptom**: was working, now `empty media response` / `challenge_required` / Threads renders nothing.

**Fix**: log in to the site in your browser → re-export cookies (docs/01) → replace the file. Cookies have lifetimes (weeks to months); this is normal.

## 6.3 `challenge_required`（IG／Threads）

**Symptom**: IG API returns `{"message":"challenge_required",...}`.

**Cause**: old session, new IP, or automation suspicion.

**Fix**:
1. Log in via browser, solve any challenge there.
2. Re-export cookies.
3. Slow down frequency — this kit is for occasional archiving.
4. Do **not** retry the private API route repeatedly; it escalates the challenge.

## 6.4 Threads: page loads but empty text / Threads 頁面有載入但沒內容

**Cause**: JS shell rendered, but you're not logged in (cookie file missing `sessionid`).

**Check**:

```bash
grep -c sessionid www.threads.com_cookies.txt   # must be ≥ 1
```

## 6.5 Threads: `Unsupported URL` from yt-dlp / gallery-dl

**Expected.** Neither tool has a Threads extractor. Use `scripts/fetch_threads.py` (Playwright) — see docs/05.

## 6.6 FB video returns empty

**Fix**: open the video in your logged-in browser first, then retry. Some content is only served to the active session.

## 6.7 Windows git-bash path issues / Windows 路徑問題

- Use forward slashes in cookie paths: `--cookies "C:/Users/you/cookies.txt"`.
- Chinese-character paths break some Python tools — keep the cookies folder ASCII-only.

## 6.8 `sessionid` missing after export / 匯出後沒有 sessionid

**Cause**: you exported from a page where you weren't logged in, or the extension exported the wrong tab's domain.

**Fix**: navigate to the target site first (e.g. open `threads.net`), confirm you're logged in, then export.
