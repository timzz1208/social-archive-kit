---
name: social-archive-kit
description: 少量自帳號爬取 YT/FB/IG/Threads 的整包工作流（含安全 cookies 安裝引導）。觸發：彥廷要抓社群內容、要重新匯出 cookies、要讀 Threads 貼文/留言、要爬 FB/IG 影片、或要把本工作流分享/上架時。本 repo 是公開版；本機延伸細節（IG cookies 位置、whisper 轉錄）見 video-note-processing 與 threads-fetch。
---

# Social Archive Kit（操作版）

Repo：`C:\彥廷資料庫\social-archive-kit\`（公開 GitHub 版：Hao0321/social-archive-kit）
定位：輕量、個人帳號、少量低頻存檔。**不做大量爬取**。

## 平台速查

| 平台 | 工具 | cookies | 文件 |
|---|---|---|---|
| YouTube | yt-dlp | 免（公開） | docs/02 |
| Facebook | yt-dlp | 要 | docs/03 |
| Instagram | yt-dlp / gallery-dl | 要 | docs/04 |
| Threads | Playwright | 要 | docs/05 |

## cookies 鐵則（docs/01）
1. 只用 **Get cookies.txt LOCALLY**（開源、本地處理）；原版 Get cookies.txt 是 malware（2023 PSA），**禁止推薦**
2. cookies 有效檔必須含 `sessionid`；過期就重匯（瀏覽器重新登入 → 擴充 → 放回原位）
3. 只存路徑不存值；永不 commit、永不貼進對話
4. 防毒可能擋「讀瀏覽器 cookie DB」（--cookies-from-browser／cookie_extract.py）——用匯出檔路線避開；真被擋就允許自己的 profile，不要全域關防毒

## 執行流程
1. 確認目標平台＋URL
2. cookies 存在？→ 驗證 `grep -c sessionid`；不存在 → 引導 docs/01 流程（使用者手動匯出，我只記路徑）
3. YT → `download_video.py`；FB/IG → `download_video.py --cookies`；Threads → `fetch_threads.py --cookies`
4. 產出存檔（暫存筆記／指定資料夾）

## 已知坑（docs/06 完整版）
- IG `empty media response`＝cookies 缺/舊
- `challenge_required`＝換 IP/舊 session/太頻繁→重登入＋重匯＋降頻，**不要重試私 API**
- Threads 頁面空＝cookies 無 sessionid；yt-dlp/gallery-dl 對 Threads 一律 Unsupported（正常）
- 中文路徑會壞 Python 工具→cookies 資料夾用純 ASCII

## 分享/上架
- 公開版已上架；改 repo 後同步 push（git add/commit/push）
- 公開版**不含**使用者本機 cookies 路徑與個人資料——新內容進公開版前先除敏
