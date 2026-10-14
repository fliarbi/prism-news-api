#!/usr/bin/env bash
# run.sh — gunicorn + uvicorn workers on :8800, logs under logs/.
#
#   ./run.sh            foreground (Ctrl-C stops it)
#   ./run.sh --bg       daemonise; pid in logs/gunicorn.pid
#   ./run.sh stop       stop the daemon started by --bg (pidfile only — never pkill)
#   ./run.sh status     is the daemon alive
#
# Env: PORT (8800), WORKERS (2), BIND (0.0.0.0), PRISM_* (see prism_news_api/config.py).
set -euo pipefail
cd "$(dirname "$(readlink -f "$0")")"
mkdir -p logs
PORT="${PORT:-8800}"
WORKERS="${WORKERS:-2}"
BIND="${BIND:-0.0.0.0}"
PIDFILE="logs/gunicorn.pid"
GUNICORN="${GUNICORN:-gunicorn}"
command -v "$GUNICORN" >/dev/null 2>&1 || GUNICORN="$HOME/.local/bin/gunicorn"

ARGS=( -k uvicorn.workers.UvicornWorker -w "$WORKERS" -b "$BIND:$PORT"
       --timeout 120 --graceful-timeout 20 --keep-alive 5
       --access-logfile logs/access.log --error-logfile logs/error.log
       --log-level info prism_news_api.main:app )

case "${1:-}" in
  --bg)
    if [[ -f "$PIDFILE" ]] && kill -0 "$(cat "$PIDFILE")" 2>/dev/null; then
      echo "already running (pid $(cat "$PIDFILE"))"; exit 0
    fi
    "$GUNICORN" "${ARGS[@]}" --daemon --pid "$PIDFILE"
    sleep 1; echo "started on :$PORT (pid $(cat "$PIDFILE" 2>/dev/null || echo ?)); logs in logs/" ;;
  stop)
    if [[ -f "$PIDFILE" ]]; then
      kill "$(cat "$PIDFILE")" && echo "stopped pid $(cat "$PIDFILE")"; rm -f "$PIDFILE"
    else echo "no pidfile"; fi ;;
  status)
    if [[ -f "$PIDFILE" ]] && kill -0 "$(cat "$PIDFILE")" 2>/dev/null; then echo "running (pid $(cat "$PIDFILE"))"
    else echo "not running"; exit 1; fi ;;
  *)
    exec "$GUNICORN" "${ARGS[@]}" ;;
esac
