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

## 🇧🇷 Versão em Português

Um bot em Python que identifica suas waifus favoritas no **jogo Mudae do Discord** e reage automaticamente para se casar com elas.

---

## ⚙️ Como funciona

O bot:
- Usa screenshots para identificar nomes de waifus na tela.
- Digita `$wa` para rolar waifus.
- Se encontrar uma imagem correspondente (com base na pasta `waifus/`), ele reage automaticamente com o emoji configurado.

---

## 📁 Como configurar

### 1. Adicione suas waifus

Para o bot identificar as waifus certas:

- Pesquise a waifu no Mudae com `$im NomeDaWaifu`
- Tire uma **print SOMENTE do nome da waifu**
- Salve a print dentro da pasta `waifus/`

**Exemplo:**

1. `$im Rei Ayanami`  
2. Print do nome da waifu (somente o nome!)  
3. Salve como `Rei_waifu.png` dentro da pasta `waifus/`

> A imagem deve estar clara e exatamente como aparece no Discord.

---

### 2. Configure o emoji de reação

O bot usa um emoji favorito para reagir automaticamente.

Você pode:
- Favoritar o emoji `:index_pointing_at_the_viewer:` no Discord
- OU tirar uma print do emoji que quer usar e salvar como:
reactsemote/react_emote.png

yaml
Copiar
Editar

Opcionalmente, substitua também o `react_button.png` se o botão de reagir for diferente no seu Discord.

---

## ⚠️ AVISO MEGA IMPORTANTE

O projeto **pode parar de funcionar a qualquer momento** se o Discord mudar qualquer detalhe visual, como:
- Interface
- Cores
- Fontes

> O bot depende 100% de reconhecimento de tela e **não é oficial** do Discord ou Mudae.

---

## 🖥️ Requisitos

- Python 3.8 ou superior
- Biblioteca `pyautogui`
- Escala de tela recomendada: **100%**
- Interface do Discord em português ou inglês (igual às imagens salvas)
