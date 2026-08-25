#!/usr/bin/env bash
# plane-assign-when-accepted.sh: assign the showcase issues the moment Ezekiel accepts.
#
# WHY THIS EXISTS
#   Plane cannot assign an issue to a pending invitee: an invited user has no member uuid
#   until they accept. So the nine CONTENT issues were created unassigned, and "he can see
#   what is assigned to him" is not true until someone runs the assign step after acceptance.
#   Leaving that as a manual step means it gets forgotten and he logs in to an empty queue.
#
#   This closes the gap: it polls hourly, assigns when he appears in the member list, then
#   REMOVES ITS OWN CRON LINE so it does not linger as permanent cruft.
set -uo pipefail
export PATH="/home/jeremy/bin:/usr/local/bin:/usr/bin:/bin"
export LC_ALL=C.UTF-8

REPO=/home/jeremy/000-projects/omarchy
LOG_DIR=/home/jeremy/.local/state/omarchy-plane-assign
mkdir -p "$LOG_DIR"
LOG="$LOG_DIR/assign.log"
exec >>"$LOG" 2>&1
echo "[$(date -Is)] poll"

OUT="$(python3 "$REPO/scripts/plane-sync-packets.py" --assign-only 2>&1)"
echo "$OUT"

if echo "$OUT" | grep -q "has NOT accepted"; then
  echo "[$(date -Is)] still pending, will retry"
  exit 0
fi

ASSIGNED=$(echo "$OUT" | grep -c '^assigned ')
echo "[$(date -Is)] assigned=$ASSIGNED"
if [ "$ASSIGNED" -lt 1 ]; then
  echo "[$(date -Is)] member exists but nothing assigned, leaving cron in place"
  exit 0
fi

# Self-remove: the job has done the one thing it was for.
crontab -l 2>/dev/null | grep -v 'plane-assign-when-accepted.sh' | crontab -
echo "[$(date -Is)] assigned $ASSIGNED issues and removed own cron entry"

if [ -f /home/jeremy/bin/lib/notify-lib.sh ]; then
  # shellcheck disable=SC1091
  . /home/jeremy/bin/lib/notify-lib.sh 2>/dev/null || true
  if command -v slack_post >/dev/null 2>&1; then
    slack_post "Ezekiel accepted the Plane invite. Assigned $ASSIGNED Omarchy showcase issues in CONTENT and removed the polling cron." || true
  fi
fi
