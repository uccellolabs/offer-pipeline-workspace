#!/usr/bin/env bash
# Stop hook: auto-commit + push dirty workspace to origin/main.
# Protections : skip si node_modules dans changements, skip si fichier > 10MB.
# Silent sur succès, tout log dans ~/Library/Logs/uccello-workspace-autosync.log

set +e
SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
WORKSPACE="$( cd "$SCRIPT_DIR/../.." && pwd )"
LOG="$HOME/Library/Logs/$(basename "$WORKSPACE")-autosync.log"
MAX_BYTES=10485760  # 10 MB
mkdir -p "$(dirname "$LOG")"

cd "$WORKSPACE" || exit 0

TS=$(date '+%Y-%m-%d %H:%M:%S')

# Quick exit if clean
if [ -z "$(git status --porcelain)" ]; then
  exit 0
fi

# Protection 1 : node_modules ne doit jamais passer (le .gitignore le bloque déjà,
# mais ceinture+bretelles si le .gitignore est cassé/modifié)
if git status --porcelain | grep -q "node_modules"; then
  echo "[$TS] SKIP push: node_modules detected in changes" >> "$LOG"
  echo "---" >> "$LOG"
  exit 0
fi

# Protection 2 : skip si un fichier > 10MB est en jeu
LARGE_FILE=""
while IFS= read -r line; do
  # Format porcelain : "XY path" — extract path after the 3 chars
  path="${line:3}"
  # Handle renames: "R old -> new"
  if [[ "$path" == *" -> "* ]]; then
    path="${path##* -> }"
  fi
  # Strip quotes if present
  path="${path%\"}"
  path="${path#\"}"
  if [ -f "$path" ]; then
    size=$(stat -f%z "$path" 2>/dev/null || echo 0)
    if [ "$size" -gt "$MAX_BYTES" ]; then
      LARGE_FILE="$path ($size bytes)"
      break
    fi
  fi
done < <(git status --porcelain)

if [ -n "$LARGE_FILE" ]; then
  echo "[$TS] SKIP push: large file detected: $LARGE_FILE" >> "$LOG"
  echo "---" >> "$LOG"
  exit 0
fi

# Tout OK : commit + push
COUNT=$(git status --porcelain | wc -l | tr -d ' ')
MSG="auto: ${TS} (${COUNT} files)"

{
  echo "[$TS] Stop push: $COUNT files"
  git add -A 2>&1
  git commit -m "$MSG" 2>&1
  git push origin main 2>&1
  echo "[$TS] push exit=$?"
  echo "---"
} >> "$LOG" 2>&1

exit 0
