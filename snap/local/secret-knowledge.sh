#!/bin/bash
export SECRET_KNOWLEDGE_DATA="$SNAP/share/secret-knowledge/data"
export GI_TYPELIB_PATH="$SNAP/usr/lib/x86_64-linux-gnu/girepository-1.0:${GI_TYPELIB_PATH}"
export LD_LIBRARY_PATH="$SNAP/usr/lib/x86_64-linux-gnu:$SNAP/usr/lib:${LD_LIBRARY_PATH}"
export PYTHONPATH="$SNAP/usr/lib/python3/dist-packages:$SNAP/usr/lib/python3.12:${PYTHONPATH}"

# Find main.py wherever it landed
MAIN=$(find $SNAP -name "main.py" -path "*/secret_knowledge/*" 2>/dev/null | head -1)

if [ -z "$MAIN" ]; then
    echo "Error: main.py not found in $SNAP" >&2
    exit 1
fi

exec python3 "$MAIN" "$@"
