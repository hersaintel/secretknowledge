#!/bin/bash
# Book of Secret Knowledge — Flatpak launcher
# Curated by Hersa — Cyber Intelligence Analyst

export SECRET_KNOWLEDGE_DATA="/app/share/secret-knowledge/data"
export GI_TYPELIB_PATH="/app/lib/girepository-1.0:/usr/lib/girepository-1.0:${GI_TYPELIB_PATH}"
export LD_LIBRARY_PATH="/app/lib:/usr/lib:${LD_LIBRARY_PATH}"

echo "Starting Book of Secret Knowledge..." >&2

# If no D-Bus session bus is available, start a temporary one.
# This prevents the "ServiceUnknown" GDBus error on first launch.
if [ -z "$DBUS_SESSION_BUS_ADDRESS" ]; then
    echo "No session bus found — launching with dbus-run-session" >&2
    exec dbus-run-session /usr/bin/python3 /app/share/secret-knowledge/src/main.py "$@"
else
    exec /usr/bin/python3 /app/share/secret-knowledge/src/main.py "$@"
fi
