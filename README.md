# Social Archive Kit

> Lightweight, personal-account scraping recipes for **YouTube / Facebook / Instagram / Threads** — with a complete, safe **cookies setup guide** baked in. Built for small-scale, low-frequency archiving by real humans with real accounts.

> 輕量、個人帳號少量爬取的實戰食譜：**YouTube / Facebook / Instagram / Threads** 四平台，內建完整且安全的 **cookies 安裝引導**。給「真的有帳號、少量低頻存檔」的一般人用。

---

## Why this exists / 為什麼有這個專案

Most scrapers on GitHub assume you already know how to obtain cookies, or they silently rely on a browser extension that may be **malware** (the original "Get cookies.txt" extension was found exfiltrating cookies to its developer — see [Reddit PSA](https://www.reddit.com/r/youtubedl/comments/11i5vyq/psa_the_get_cookiestxt_extension_is_now_actively/)). This kit closes that gap: it tells you exactly **which safe tool to install**, **how to export**, **where to put the file**, and then how to scrape each platform.

GitHub 上多數爬蟲教學都假設你「已經知道 cookies 怎麼來」，或默默叫你裝一個可能是**惡意軟體**的擴充（原版「Get cookies.txt」曾被發現把 cookies 外傳給開發者——見 [Reddit 警告](https://www.reddit.com/r/youtubedl/comments/11i5vyq/psa_the_get_cookiestxt_extension_is_now_actively/)）。這個專案補上缺口：**裝哪個安全工具、怎麼匯出、檔放哪、然後怎麼爬**，一次講完。

## Platform coverage / 平台支援

| Platform | Method | Cookies needed? | Notes |
|---|---|---|---|
| YouTube | `yt-dlp` | No (public) | Subtitles, playlists, channels |
| Facebook | `yt-dlp` | Yes | Public videos/Reels need login cookies |
| Instagram | `yt-dlp` | Yes | Reels/IGTV; empty-response = missing cookies |
| Threads | Playwright + cookies | Yes | Full post + comment section; JS-rendered, no public API |

## Quick start / 快速開始

```bash
# 1. Install the two engines
pip install yt-dlp playwright
python -m playwright install chromium

# 2. Set up cookies (see docs/01-cookies-setup.md — 5 minutes)
#    → Get cookies.txt LOCALLY (safe, open-source) → export threads.com & instagram.com → save paths

# 3. Scrape
python scripts/download_video.py "https://www.facebook.com/..." --cookies "path/to/cookies.txt"
python scripts/fetch_threads.py "https://www.threads.net/@user/post/XXX" --cookies "path/to/cookies.txt"
```

## Security principles / 安全原則

1. **Cookies are your account keys.** Store paths, never values. Never paste cookies into chats, tickets, or public code.
2. **Use the safe extension only**: [Get cookies.txt LOCALLY](https://github.com/kairi003/Get-cookies.txt-LOCALLY) (open-source, processes locally). Avoid the original "Get cookies.txt".
3. **Antivirus false positives**: tools that read browser cookie databases may trigger AV prompts. This is expected; grant access for your own profile only.
4. **Low frequency.** This kit is for occasional personal archiving — not bulk scraping. Respect each platform's ToS and rate limits; excessive requests can get your account challenged.

---

## Structure / 結構

```
social-archive-kit/
├── README.md                 ← you are here
├── LICENSE                   ← MIT
├── SKILL.md                  ← Hermes-agent skill version of this kit
├── docs/
│   ├── 01-cookies-setup.md       安全 cookies 工具安裝＋匯出引導（含惡意版警告）
│   ├── 02-youtube.md             yt-dlp 免登入食譜
│   ├── 03-facebook.md            FB 影片＋Reels（需 cookies）
│   ├── 04-instagram.md           IG Reels＋圖庫（需 cookies；登入牆陷阱）
│   ├── 05-threads.md             Threads 貼文＋留言區（Playwright）
│   └── 06-troubleshooting.md     防毒誤報／cookies 過期／challenge_required
└── scripts/
    ├── fetch_threads.py          Playwright 抓 Threads 貼文＋留言
    ├── download_video.py         yt-dlp wrapper（--cookies 參數化）
    └── cookie_extract.py         （可選）本機抽 cookies 小工具，不需瀏覽器擴充
```

## Requirements / 需求

- Python 3.10+
- `yt-dlp`, `playwright`（`pip install yt-dlp playwright`）
- A real browser account (Chrome/Edge/Firefox) for cookie export
- Windows / macOS / Linux (scripts are cross-platform; tested on Windows git-bash)

## Credits / 致謝

This kit is a thin wrapper and cookbook around battle-tested open-source tools. All credit goes to their authors; we only wrote the glue scripts and the docs (all pitfalls tested by us in real usage, 2026).

本套件只是圍繞成熟開源工具的「薄包裝＋實戰食譜」。功勞屬於原作者們；我們只寫了膠水腳本與文件（所有坑都是我們 2026 年實測踩過的）。

| Tool | Author | License | Used for |
|---|---|---|---|
| [yt-dlp](https://github.com/yt-dlp/yt-dlp) | yt-dlp team | Unlicense | YT / FB / IG video download |
| [gallery-dl](https://github.com/mikf/gallery-dl) | [mikf](https://github.com/mikf) | GPLv2 | IG image galleries |
| [Playwright](https://github.com/microsoft/playwright) | Microsoft | Apache-2.0 | Threads rendering (no public API) |
| [Get cookies.txt LOCALLY](https://github.com/kairi003/Get-cookies.txt-LOCALLY) | [kairi003](https://github.com/kairi003) | MIT | Safe cookie export |

Our `scripts/` are original glue code (subprocess/Playwright wrappers, ~100 lines each); we did not copy code from the projects above. The docs are our own field notes.

我們的 `scripts/` 是原創膠水碼（subprocess／Playwright 包裝，每支約百行）；沒有複製上述專案的程式碼。文件是我們自己的實戰筆記。

## License / 授權

MIT © 2026 Hao0321 Studio. Cookbook-style documentation; scripts are minimal wrappers around `yt-dlp` / `playwright`.

## Disclaimer / 免責聲明

This kit is for archiving content you are allowed to access with your own account. You are responsible for complying with each platform's Terms of Service and your local laws. The author is not affiliated with Meta / Google.

本專案僅供「以自己帳號存取你本來就能看的內容」之少量存檔用途。請自行遵守各平台服務條款與當地法令；作者與 Meta／Google 無任何關聯。
