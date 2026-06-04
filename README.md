# 🛡️ Book of Secret Knowledge

---

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Platform](https://img.shields.io/badge/Platform-Linux-orange.svg)](https://github.com/hersaintel/secretknowledge)
[![Tools](https://img.shields.io/badge/Tools-1657-58a6ff.svg)](https://github.com/hersaintel/secretknowledge)
[![Maintained](https://img.shields.io/badge/Maintained-yes-green.svg)](https://github.com/hersaintel/secretknowledge)
[![GitHub Stars](https://img.shields.io/github/stars/hersaintel/secretknowledge?style=social)](https://github.com/hersaintel/secretknowledge)

---

Hi, I'm **Hersa** — a cyber intelligence analyst. I built this app because I got tired of jumping between tabs looking for the right security tool. This is a free, offline Linux desktop app that puts **1,657 security tools and resources** into one clean, searchable interface — pentest frameworks, OSINT tools, AI security, cryptography, networking, cloud security, and more, all with embedded documentation.

> **Disclaimer:** I don't own any of the tools or resources listed here. Everything remains the intellectual property of its respective authors. This is simply a more convenient way to access publicly available security resources. If you're a tool author with concerns, reach out — I'll address it promptly.
>
> 📸 Instagram: [@hersaintel](https://instagram.com/hersaintel) · Discord: **@ers49**



## Install via Flatpak (Recommended)

This app runs best via Flatpak. Follow these steps to install and run it locally on any Linux distro.

### Step 1 — Install Flatpak

```bash
# Debian / Ubuntu / Mint / Kali / Parrot
sudo apt install flatpak

# Fedora
sudo dnf install flatpak

# Arch
sudo pacman -S flatpak
```

### Step 2 — Add the GNOME SDK (one-time setup)

```bash
flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
flatpak install flathub org.gnome.Platform//50 org.gnome.Sdk//50
```

### Step 3 — Clone the Repository

```bash
git clone https://github.com/hersaintel/secretknowledge.git
cd secretknowledge
```

### Step 4 — Build and Install

```bash
flatpak-builder --user --install --force-clean build-dir \
    io.github.hersaintel.secretknowledge.json
```

### Step 5 — Run

```bash
flatpak run io.github.hersaintel.secretknowledge
```

That's it — the app runs fully offline with no internet required after setup.

---

## Updating

When a new version is released, pull the latest changes and rebuild:

```bash
cd secretknowledge
git pull origin master
flatpak-builder --user --install --force-clean build-dir \
    io.github.hersaintel.secretknowledge.json
```

---

## Uninstall

```bash
flatpak uninstall io.github.hersaintel.secretknowledge
```

---

## Run Without Installing (Dev Mode)

If you just want to test or contribute without a full install:

```bash
# Install Python dependencies
sudo apt install python3-gi python3-gi-cairo gir1.2-gtk-4.0 \
    gir1.2-adw-1 gir1.2-webkit-6.0

# Run directly
python3 src/secret_knowledge/main.py
```

---

## What's Inside

| Category | Examples |
|---|---|
| CLI Tools | Shells, editors, terminal utilities, network tools |
| Hacking / Pentest | Offensive, defensive, OSINT, web app security, cloud |
| AI Security | ART, Garak, PyRIT, Promptfoo, PurpleLlama |
| Cryptography | libsodium, libtomcrypt, and more |
| Networks | Scanners, analyzers, proxies |
| Systems | Containers, orchestration, monitoring |

---

## Keyboard Shortcuts

| Shortcut | Action |
|---|---|
| `Ctrl+R` | Reload |
| `Ctrl++` / `Ctrl+-` | Zoom in / out |
| `Ctrl+0` | Reset zoom |
| `Ctrl+Q` | Quit |
| `Escape` | Close panel |

---

## Contributing

Found a tool that should be listed? Open an issue or pull request on GitHub. All suggestions welcome.

---

## Contact

Built and maintained by **Hersa** — Cyber Intelligence Analyst.
Reach out for tool removal requests, feedback, or collaboration.

- Instagram: [@hersaintel](https://instagram.com/hersaintel)
- Discord: **@ers49**