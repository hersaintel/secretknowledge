# 🛡️ Book of Secret Knowledge
# 🛡️ Book of Secret Knowledge

[![Snap Store](https://snapcraft.io/secret-knowledge/badge.svg)](https://snapcraft.io/secret-knowledge)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Platform](https://img.shields.io/badge/Platform-Linux-orange.svg)](https://snapcraft.io/secret-knowledge)
[![Tools](https://img.shields.io/badge/Tools-1657-58a6ff.svg)](https://github.com/hersaintel/secretknowledge)
[![Maintained](https://img.shields.io/badge/Maintained-yes-green.svg)](https://github.com/hersaintel/secretknowledge)
[![GitHub Stars](https://img.shields.io/github/stars/hersaintel/secretknowledge?style=social)](https://github.com/hersaintel/secretknowledge)

Hi, I'm **Hersa** — a cyber intelligence analyst. I built this app because I got tired of jumping between tabs looking for the right security tool. This is a free, offline Linux desktop app that puts **1,657 security tools and resources** into one clean, searchable interface — pentest frameworks, OSINT tools, AI security, cryptography, networking, cloud security, and more, all with embedded documentation.

> **Disclaimer:** I don't own any of the tools or resources listed here. Everything remains the intellectual property of its respective authors. This is simply a more convenient way to access publicly available security resources. If you're a tool author with concerns, reach out — I'll address it promptly.
>
> 📸 Instagram: [@hersaintel](https://instagram.com/hersaintel) · Discord: **@ers49**

---

## Install via Snap *(Recommended)*

```bash
sudo snap install secret-knowledge
```

---

## Install from Source

### Prerequisites

```bash
# Debian / Ubuntu / Mint / Kali / Parrot
sudo apt install git python3 python3-gi python3-gi-cairo \
    gir1.2-gtk-4.0 gir1.2-adw-1 gir1.2-webkit2-6.0 \
    meson ninja-build gettext

# Fedora
sudo dnf install git python3 python3-gobject gtk4 libadwaita \
    webkitgtk6.0 meson ninja-build gettext

# Arch
sudo pacman -S git python python-gobject gtk4 libadwaita \
    webkit2gtk-6.0 meson ninja gettext
```

### Clone and Build

```bash
git clone https://github.com/hersaintel/secretknowledge.git
cd secretknowledge

# Set up build
meson setup build --prefix=/usr

# Compile
ninja -C build

# Install system-wide
sudo ninja -C build install

# Run
secret-knowledge
```

### Run Without Installing (Dev Mode)

```bash
git clone https://github.com/hersaintel/secretknowledge.git
cd secretknowledge
python3 src/secret_knowledge/main.py
```

---

## Uninstall

```bash
# If installed via Snap
sudo snap remove secret-knowledge

# If installed from source
sudo ninja -C build uninstall
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
| `/` | Focus search |
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
