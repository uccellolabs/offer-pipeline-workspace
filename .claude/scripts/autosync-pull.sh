#!/usr/bin/env bash
# SessionStart hook: pull remote changes (e.g. from phone via Working Copy / GitHub Mobile)
# before Claude starts working. Silent on failure, never blocks the session.

set +e
SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
WORKSPACE="$( cd "$SCRIPT_DIR/../.." && pwd )"
LOG="$HOME/Library/Logs/$(basename "$WORKSPACE")-autosync.log"
mkdir -p "$(dirname "$LOG")"

cd "$WORKSPACE" || exit 0

TS=$(date '+%Y-%m-%d %H:%M:%S')
{
  echo "[$TS] SessionStart pull"
  git pull --rebase --autostash origin main 2>&1
  echo "[$TS] pull exit=$?"
  echo "---"
} >> "$LOG" 2>&1

exit 0
