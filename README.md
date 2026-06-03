# 🛡️ Book of Secret Knowledge

Hi, I'm **Hersa** — a cyber intelligence analyst. I built this app because I got tired of jumping between tabs looking for the right security tool. This is a free, offline Linux desktop app that puts **1,657 security tools and resources** into one clean, searchable interface — pentest frameworks, OSINT tools, AI security, cryptography, networking, cloud security, and more, all with embedded documentation.

> **Disclaimer:** I don't own any of the tools or resources listed here. Everything remains the intellectual property of its respective authors. This is simply a more convenient way to access publicly available security resources. If you're a tool author with concerns, reach out — I'll address it promptly.
>
> 📸 Instagram: [@hersaintel](https://instagram.com/hersaintel) · Discord: **@ers49**

---

## Install via Flatpak

```bash
flatpak install flathub io.hersaintel.secretknowledge
flatpak run io.hersaintel.secretknowledge
```

---

## Build from Source

**Prerequisites:**

```bash
# Add Flathub remote
flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo

# Install GNOME SDK (one-time)
flatpak install flathub org.gnome.Platform//46 org.gnome.Sdk//46
```

**Build & install:**

```bash
cd secret-knowledge-app
flatpak-builder --user --install --force-clean build-dir io.hersaintel.secretknowledge.json
flatpak run io.hersaintel.secretknowledge
```

**Without Flatpak (dev mode)** — requires Python 3.10+, GTK4, Libadwaita, WebKitGTK 6.0:

```bash
sudo apt install python3-gi gir1.2-gtk-4.0 gir1.2-adw-1 gir1.2-webkit-6.0  # Debian/Ubuntu
python3 src/main.py
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

## Contact

Built and maintained by **Hersa** — Cyber Intelligence Analyst.
Reach out for tool removal requests, feedback, or collaboration.

- Instagram: [@hersaintel](https://instagram.com/hersaintel)
- Discord: **@ers49**
