# 💍 Mudae Waifu Auto-Marry Bot

A Python automation bot that identifies your favorite waifus in the **Mudae Discord game** and automatically reacts to marry them.

## ⚙️ How it Works

The bot:
- Uses screenshots to identify waifu names on screen.
- Types `$wa` to roll waifus.
- If a match is found (based on images in the `waifus/` folder), it reacts automatically using your selected emoji.

---

## 📁 Setup Instructions

### 1. Add your waifus

To let the bot identify your favorite waifus:

- Search the waifu in Mudae using `$im WaifuName`.
- Take a **screenshot of the waifu's name only** (don't include the image or description).
- Save it in the `waifus/` folder.

**Example:**

1. `$im Rei Ayanami`  
2. Take a screenshot of just her name  
3. Save as `Rei_waifu.png` inside the `waifus/` folder

> Make sure the screenshot is clear and exactly as it appears on your screen!

---

### 2. Set up the reaction emoji

The bot reacts with a specific emoji to marry.

To configure this:
- Favorite the emoji `:index_pointing_at_the_viewer:` in Discord
- OR take a screenshot of the emoji you want to use and save it as:
reactsemote/react_emote.png

yaml
Copiar
Editar

Optional: You can also replace the `react_button.png` if the UI button changes.

---

## ⚠️ MEGA IMPORTANT WARNING

This project **can stop working at any time** if Discord updates its UI, changes colors, fonts, or structure.

> It’s entirely based on screen recognition and is not officially supported by Discord or Mudae.

---
