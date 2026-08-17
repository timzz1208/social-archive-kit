# 02 · YouTube

> The only platform in this kit that mostly works **without cookies** for public content.

> 本套件中唯一「公開內容大多不需要 cookies」的平台。

## 2.1 Install / 安裝

```bash
pip install yt-dlp
```

## 2.2 Single video / 單支影片

```bash
yt-dlp -o "%(title)s.%(ext)s" "https://www.youtube.com/watch?v=XXX"
```

## 2.3 Subtitles / 字幕

```bash
# Chinese traditional subtitles (write to .srt/.vtt)
yt-dlp --write-subs --sub-langs "zh-Hant,zh-TW" --sub-format srt --skip-download \
       -o "%(title)s.%(ext)s" "https://www.youtube.com/watch?v=XXX"

# List available subtitle languages first
yt-dlp --list-subs "https://www.youtube.com/watch?v=XXX"
```

## 2.4 Playlist / 播放清單

```bash
yt-dlp -o "%(playlist_title)s/%(playlist_index)s - %(title)s.%(ext)s" \
       "https://www.youtube.com/playlist?list=XXX"
```

## 2.5 Audio only / 只要音訊

```bash
yt-dlp -x --audio-format wav --audio-quality 0 -o "audio.%(ext)s" "URL"
```

## 2.6 Age-restricted / 年齡限制

Some videos need login cookies even on YouTube:

```bash
yt-dlp --cookies "path/to/cookies.txt" "URL"
```

## 2.7 Pitfalls / 陷阱

- **Channels without public playlists**: use `https://www.youtube.com/@handle/videos` with `--flat-playlist`.
- **`--cookies-from-browser chrome`** may trigger antivirus prompts (reads your browser profile) — the exported-file approach avoids this (see docs/01).
- If "Sign in to confirm you're not a bot" appears, you need cookies for that IP.
