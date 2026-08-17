# 05 · Threads（貼文＋留言區）

> The hardest platform. Threads has **no public API**, the page is a **JavaScript shell** (content loads only after login + client-side render), and `yt-dlp` / `gallery-dl` have **no Threads extractor**. The reliable path is **Playwright + valid cookies**.

> 最難的平台。Threads **沒有公開 API**、頁面是 **JS 空殼**（要登入＋前端渲染才有內容）、`yt-dlp`／`gallery-dl` **沒有 Threads extractor**。可靠路徑＝**Playwright＋有效 cookies**。

## 5.1 What works / 已驗證可行（2026-08 實測）

| 方法 | 結果 |
|---|---|
| Firecrawl / generic web extract | ❌ not supported |
| `yt-dlp` | ❌ no Threads extractor |
| `gallery-dl` | ❌ no Threads extractor |
| curl page HTML（even with cookies） | ❌ JS shell, ~256KB of CSS |
| IG official API with shortcode→media_id | ❌ `challenge_required` |
| **Playwright + cookies** | ✅ post + full comment section |

## 5.2 Usage / 用法

```bash
pip install playwright
python -m playwright install chromium

python scripts/fetch_threads.py "https://www.threads.net/@user/post/XXX" --cookies "C:\...\www.threads.com_cookies.txt"
```

The script:
1. Parses the Netscape cookie file（`sessionid` required — asserts it）
2. Launches headless Chromium with your cookies
3. Waits for render, scrolls to trigger comment loading
4. Clicks "顯示更多 / Show more" to expand collapsed comments
5. Prints post + full comment section to stdout

## 5.3 Output / 輸出

Plain text from `document.body.innerText` — post body, view/like/reply counts, then every comment with author labels. Pipe to a file for archiving:

```bash
python scripts/fetch_threads.py "<URL>" --cookies "<FILE>" > thread_archive.txt
```

## 5.4 Pitfalls / 陷阱（全部實測過）

1. **Domain must be `threads.net`** — `threads.com` redirects and breaks tools.
2. **`sessionid` = the key.** A cookie file without it is dead. Re-export when it expires.
3. **Comments need scrolling.** Without the scroll + "show more" steps you only get the post.
4. **Don't go through `i.instagram.com/api/v1/`** with old IG cookies — your account gets `challenge_required` and may be temporarily locked out of that route.
5. **GraphQL `/api/graphql` guessing is a dead end** — returns the HTML shell, not data.

## 5.5 Legal note / 注意

Threads has no official API and aggressive bot detection. Keep volume tiny and cadence human — this is for archiving posts you could read anyway.
