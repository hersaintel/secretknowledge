#!/usr/bin/env python3
"""
The Book of Secret Knowledge — GTK4/Libadwaita Desktop App
Curated by Hersa — Cyber Intelligence Analyst
Serves the tool browser over local HTTP with a built-in RSS proxy endpoint.
"""
import sys, os, threading, http.server, socketserver, socket, json
import urllib.request, urllib.error, urllib.parse
import gi

from gi.repository import GLib
GLib.set_prgname("io.hersaintel.secretknowledge")
GLib.set_application_name("Book of Secret Knowledge")

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
for wk in ("6.0", "4.1", "4.0"):
    try:
        gi.require_version("WebKit", wk)
        break
    except ValueError:
        continue

from gi.repository import Gtk, Adw, WebKit, Gio, Gdk

APP_ID   = "io.hersaintel.secretknowledge"
APP_NAME = "Book of Secret Knowledge"
VERSION  = "2.0.0"

RSS_UA = "Mozilla/5.0 (X11; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0"


# ── RSS Proxy Handler ─────────────────────────────────────────────────────────
class AppHandler(http.server.SimpleHTTPRequestHandler):

    def __init__(self, *args, data_dir=None, **kwargs):
        self._data_dir = data_dir
        super().__init__(*args, directory=data_dir, **kwargs)

    def log_message(self, *_):
        pass

    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.send_header("Cache-Control", "no-cache")
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path == "/rss-proxy":
            self._handle_rss_proxy(parsed)
        else:
            super().do_GET()

    def _handle_rss_proxy(self, parsed):
        params = urllib.parse.parse_qs(parsed.query)
        url    = params.get("url", [""])[0]

        if not url or not url.startswith("http"):
            self._json_error(400, "Missing or invalid url parameter")
            return

        try:
            req = urllib.request.Request(
                url,
                headers={
                    "User-Agent":      RSS_UA,
                    "Accept":          "application/rss+xml, application/xml, text/xml, */*",
                    "Accept-Language": "en-US,en;q=0.9",
                    "Accept-Encoding": "gzip, deflate",
                    "Cache-Control":   "no-cache",
                },
            )
            with urllib.request.urlopen(req, timeout=15) as resp:
                raw = resp.read()
                enc = resp.headers.get("Content-Encoding", "")
                if enc == "gzip":
                    import gzip
                    raw = gzip.decompress(raw)
                content = raw.decode("utf-8", errors="replace")

            response       = json.dumps({"content": content, "status": 200, "url": url})
            response_bytes = response.encode("utf-8")

            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(response_bytes)))
            self.end_headers()
            self.wfile.write(response_bytes)

        except urllib.error.HTTPError as e:
            self._json_error(e.code, f"Upstream HTTP {e.code}: {e.reason}")
        except urllib.error.URLError as e:
            self._json_error(502, f"Cannot reach feed: {e.reason}")
        except Exception as e:
            self._json_error(500, str(e))

    def _json_error(self, code, msg):
        body = json.dumps({"error": msg, "status": code}).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


# ── HTTP Server ───────────────────────────────────────────────────────────────
def find_free_port():
    with socket.socket() as s:
        s.bind(("", 0))
        return s.getsockname()[1]


def start_http_server(data_dir: str) -> int:
    port = find_free_port()

    def make_handler(*args, **kwargs):
        return AppHandler(*args, data_dir=data_dir, **kwargs)

    server = socketserver.ThreadingTCPServer(("127.0.0.1", port), make_handler)
    server.allow_reuse_address = True
    threading.Thread(target=server.serve_forever, daemon=True).start()
    print(f"HTTP server on http://127.0.0.1:{port}", file=sys.stderr)
    return port


# ── Main Window ───────────────────────────────────────────────────────────────
class SecretKnowledgeWindow(Adw.ApplicationWindow):
    def __init__(self, app, port: int):
        super().__init__(application=app)
        self.port = port

        self.set_title(APP_NAME)
        self.set_default_size(1280, 820)
        self.set_size_request(900, 600)

        # ── Header ──────────────────────────────────────────────────────────
        hdr = Adw.HeaderBar()
        hdr.set_centering_policy(Adw.CenteringPolicy.STRICT)

        title = Gtk.Label(label=APP_NAME)
        title.add_css_class("heading")
        hdr.set_title_widget(title)

        self.back_btn = Gtk.Button(icon_name="go-previous-symbolic")
        self.fwd_btn  = Gtk.Button(icon_name="go-next-symbolic")
        self.back_btn.set_tooltip_text("Back")
        self.fwd_btn.set_tooltip_text("Forward")
        self.back_btn.set_sensitive(False)
        self.fwd_btn.set_sensitive(False)
        self.back_btn.connect("clicked", lambda _: self.webview.go_back())
        self.fwd_btn.connect("clicked",  lambda _: self.webview.go_forward())
        hdr.pack_start(self.back_btn)
        hdr.pack_start(self.fwd_btn)

        reload_btn = Gtk.Button(icon_name="view-refresh-symbolic")
        reload_btn.set_tooltip_text("Reload")
        reload_btn.connect("clicked", lambda _: self.webview.reload())

        menu = Gio.Menu()
        menu.append("About", "app.about")
        menu.append("Quit",  "app.quit")
        menu_btn = Gtk.MenuButton(icon_name="open-menu-symbolic", menu_model=menu)

        hdr.pack_end(menu_btn)
        hdr.pack_end(reload_btn)

        # ── WebKit settings ──────────────────────────────────────────────────
        ws = WebKit.Settings()
        ws.set_enable_javascript(True)
        ws.set_enable_developer_extras(True)
        ws.set_enable_smooth_scrolling(True)
        ws.set_allow_universal_access_from_file_urls(True)
        ws.set_javascript_can_access_clipboard(True)
        ws.set_media_playback_requires_user_gesture(False)
        try:
            ws.set_hardware_acceleration_policy(WebKit.HardwareAccelerationPolicy.ALWAYS)
        except Exception:
            pass

        # ── WebView ──────────────────────────────────────────────────────────
        try:
            ns = WebKit.NetworkSession.new_ephemeral()
            self.webview = WebKit.WebView(settings=ws, network_session=ns)
        except Exception:
            self.webview = WebKit.WebView(settings=ws)

        self.webview.set_vexpand(True)

        try:
            cm = self.webview.get_user_content_manager()
            cm.register_script_message_handler("openExternal")
            cm.connect("script-message-received::openExternal", self._on_open_external)
        except Exception as e:
            print(f"Message handler error: {e}", file=sys.stderr)

        self.webview.connect("load-changed",  self._on_load_changed)
        self.webview.connect("decide-policy", self._on_decide_policy)

        # ── Spinner overlay ──────────────────────────────────────────────────
        try:
            spinner = Adw.Spinner()
        except Exception:
            spinner = Gtk.Spinner()
        spinner.set_size_request(48, 48)
        spin_box = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL,
            valign=Gtk.Align.CENTER, halign=Gtk.Align.CENTER, spacing=12)
        spin_box.append(spinner)
        lbl = Gtk.Label(label="Loading…")
        lbl.add_css_class("dim-label")
        spin_box.append(lbl)
        self._spinner = spin_box

        overlay = Gtk.Overlay()
        overlay.set_child(self.webview)
        overlay.add_overlay(spin_box)

        root = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        root.append(hdr)
        root.append(overlay)
        self.set_content(root)

        self.webview.load_uri(f"http://127.0.0.1:{port}/secret-knowledge-v2.html")

    def _on_open_external(self, cm, result):
        try:
            url = result.get_js_value().to_string()
            if url and url.startswith("http"):
                Gio.AppInfo.launch_default_for_uri(url, None)
        except Exception as e:
            print(f"openExternal error: {e}", file=sys.stderr)

    def _on_load_changed(self, wv, event):
        loading = event in (WebKit.LoadEvent.STARTED, WebKit.LoadEvent.COMMITTED)
        self._spinner.set_visible(loading)
        self.back_btn.set_sensitive(wv.can_go_back())
        self.fwd_btn.set_sensitive(wv.can_go_forward())

    def _on_decide_policy(self, wv, decision, dtype):
        if dtype in (
            WebKit.PolicyDecisionType.NAVIGATION_ACTION,
            WebKit.PolicyDecisionType.NEW_WINDOW_ACTION,
        ):
            uri = decision.get_navigation_action().get_request().get_uri()
            if uri and not uri.startswith(f"http://127.0.0.1:{self.port}"):
                try:
                    Gio.AppInfo.launch_default_for_uri(uri, None)
                except Exception as e:
                    print(f"launch_default_for_uri: {e}", file=sys.stderr)
                decision.ignore()
                return True
        return False


# ── Application ───────────────────────────────────────────────────────────────
class SecretKnowledgeApp(Adw.Application):
    def __init__(self, port: int):
        super().__init__(
            application_id=APP_ID,
            # NON_UNIQUE: skip D-Bus single-instance registration entirely.
            # Fixes "ServiceUnknown" crash inside Flatpak sandboxes where the
            # session bus isn't always reachable during first launch.
            flags=Gio.ApplicationFlags.NON_UNIQUE,
        )
        self.port   = port
        self.window = None

    def do_startup(self):
        Adw.Application.do_startup(self)
        Gtk.Window.set_default_icon_name(APP_ID)

        for name, cb in [("about", self._on_about), ("quit", lambda *_: self.quit())]:
            a = Gio.SimpleAction.new(name, None)
            a.connect("activate", cb)
            self.add_action(a)

        self.set_accels_for_action("app.quit", ["<Ctrl>q"])

        reload_a = Gio.SimpleAction.new("reload", None)
        reload_a.connect("activate", lambda *_: self.window and self.window.webview.reload())
        self.add_action(reload_a)
        self.set_accels_for_action("app.reload", ["<Ctrl>r"])

    def do_activate(self):
        if not self.window:
            self.window = SecretKnowledgeWindow(self, self.port)
        self.window.present()

    def _on_about(self, *_):
        try:
            d = Adw.AboutDialog(
                application_name=APP_NAME,
                application_icon=APP_ID,
                version=VERSION,
                developer_name="Hersa",
                license_type=Gtk.License.MIT_X11,
                website="https://instagram.com/hersaintel",
                comments=(
                    "A free offline browser for 1,657 security tools and resources — "
                    "curated by Hersa, Cyber Intelligence Analyst.\n\n"
                    "Tools listed remain the property of their respective authors. "
                    "This app is a convenient interface for publicly available security resources.\n\n"
                    "Contact: @hersaintel (Instagram) · @ers49 (Discord)"
                ),
                developers=["Hersa — Cyber Intelligence Analyst"],
            )
            d.present(self.window)
        except Exception:
            d = Gtk.MessageDialog(
                transient_for=self.window,
                message_type=Gtk.MessageType.INFO,
                buttons=Gtk.ButtonsType.OK,
                text=f"{APP_NAME} v{VERSION}",
                secondary_text=(
                    "Curated by Hersa — Cyber Intelligence Analyst\n"
                    "@hersaintel · @ers49"
                ),
            )
            d.connect("response", lambda x, _: x.destroy())
            d.show()


# ── Entry point ───────────────────────────────────────────────────────────────
def main():
    data_dir = os.environ.get(
        "SECRET_KNOWLEDGE_DATA",
        os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "data"))
    )
    html = os.path.join(data_dir, "secret-knowledge-v2.html")
    if not os.path.exists(html):
        print(f"Error: {html} not found", file=sys.stderr)
        sys.exit(1)

    port = start_http_server(data_dir)
    return SecretKnowledgeApp(port).run(sys.argv)


if __name__ == "__main__":
    sys.exit(main())
