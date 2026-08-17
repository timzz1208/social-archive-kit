# 01 · Cookies Setup Guide / Cookies 安裝引導

> ⚠️ Skip this only if you already export cookies with a tool you trust.
> ⚠️ 如果你已經有可信的 cookies 匯出工具，可跳過本節。

## 1.1 Why cookies at all? / 為什麼需要 cookies

YouTube is mostly public. **Facebook, Instagram and Threads require login** to serve content to scrapers: without cookies you get empty responses, login walls, or `challenge_required`. Cookies prove "I am a logged-in user" to the site.

YouTube 大多公開。**FB／IG／Threads 需要登入狀態**才會把內容給爬蟲：沒有 cookies 會拿到空回應、登入牆或 `challenge_required`。Cookies 就是向網站證明「我是登入的使用者」。

## 1.2 Which tool — and which NOT / 用哪個、不要用哪個

### ✅ Use: Get cookies.txt LOCALLY
- Repo: https://github.com/kairi003/Get-cookies.txt-LOCALLY （open source, ~1.1k stars）
- **Processes everything locally** — nothing is uploaded
- Available: Chrome Web Store / Firefox Add-ons / install from source

### ❌ Avoid: the original "Get cookies.txt"
- **Reddit PSA (2023): the original extension was found sending your cookies (including login sessions) to its developer.** If an old tutorial told you to install "Get cookies.txt", uninstall it and use the LOCALLY version above.

### ❌ 不要用：原版「Get cookies.txt」
- **Reddit 警告（2023）：原版擴充被發現把 cookies（含登入 session）送給開發者。** 若舊教學叫你裝「Get cookies.txt」，請移除並改用上面的 LOCALLY 版。

## 1.3 Install / 安裝（Chrome 為例）

1. Open the Chrome Web Store page of [Get cookies.txt LOCALLY](https://chrome.google.com/webstore/detail/get-cookiestxt-locally/cclelndahbckbenkjhflpdbgdldlbecc) → **Add to Chrome**.
2. From source (offline): download the repo → `chrome://extensions` → enable **Developer mode** → **Load unpacked** → select `Get-cookies.txt-LOCALLY/src`.
3. Pin the extension icon (puzzle icon → pin).

## 1.4 Export / 匯出（每個要爬的網站各匯一次）

1. Log in to the site in the same browser (e.g. `threads.net`, `instagram.com`).
2. Click the extension icon → **Export Format: Netscape** (default).
3. Click **Export** → browser downloads `www.threads.com_cookies.txt` (or similar).
4. Move it to a safe local folder, e.g.:
   - Windows: `C:\Users\<you>\social-archive\cookies\`
   - macOS/Linux: `~/social-archive/cookies/`
5. **Record the path, not the content.** Never paste cookie values into chats or code.

**Verification** — a valid Netscape cookie file must contain a `sessionid` line (Threads/IG) or similar auth cookie. Without it, the file is useless:

```bash
grep -c "sessionid" www.threads.com_cookies.txt   # expect ≥ 1
```

## 1.5 Lifecycle / 生命週期

- Cookies **expire** (browser re-login, session rotation, site policy). If scraping starts failing with empty responses / `challenge_required`, re-export from the browser.
- Treat the folder like a keychain: keep it out of git (`echo "cookies/" >> .gitignore`).

---

## Troubleshooting quick links / 快速排障

| Symptom | Cause | Fix |
|---|---|---|
| `Instagram sent an empty media response` | No / stale cookies | Re-export cookies; pass `--cookies` |
| `challenge_required` | Account flagged / old session | Re-login in browser, re-export; slow down frequency |
| Antivirus warning when scraping | AV flags cookie-DB reads | Allow for your own profile (see docs/06) |
| Threads page renders but empty | JS shell, not logged in | Use Playwright + valid cookies (docs/05) |
