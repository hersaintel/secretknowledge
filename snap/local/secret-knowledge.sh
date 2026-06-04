#!/bin/bash
export SECRET_KNOWLEDGE_DATA="$SNAP/share/secret-knowledge/data"
exec python3 "$SNAP/lib/python3/dist-packages/secret_knowledge/main.py" "$@"
