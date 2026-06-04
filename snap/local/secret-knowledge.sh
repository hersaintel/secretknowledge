#!/bin/bash
export SECRET_KNOWLEDGE_DATA="$SNAP/share/secret-knowledge/data"
export PYTHONPATH="$SNAP/usr/lib/python3/dist-packages:${PYTHONPATH}"
export GI_TYPELIB_PATH="$SNAP/gnome-platform/usr/lib/x86_64-linux-gnu/girepository-1.0:${GI_TYPELIB_PATH}"
export LD_LIBRARY_PATH="$SNAP/gnome-platform/usr/lib/x86_64-linux-gnu:${LD_LIBRARY_PATH}"
export WEBKIT_DISABLE_SANDBOX_THIS_IS_DANGEROUS="1"
export WEBKIT_DISABLE_COMPOSITING_MODE="1"

MAIN=$(find $SNAP -name "main.py" -path "*/secret_knowledge/*" 2>/dev/null | head -1)
exec python3 "$MAIN" "$@"
