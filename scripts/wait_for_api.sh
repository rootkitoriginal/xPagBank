#!/usr/bin/env bash
set -euo pipefail

HOST="${1:-http://localhost:8000/health}"
RETRIES=${RETRIES:-30}
SLEEP_SECONDS=${SLEEP_SECONDS:-2}

echo "Aguardando API em $HOST ..."

for ((i = 1; i <= RETRIES; i++)); do
  if curl -sf "$HOST" >/dev/null; then
    echo "API disponível após $i tentativa(s)."
    exit 0
  fi
  sleep "$SLEEP_SECONDS"
  echo "Tentativa $i falhou, tentando novamente..."
done

echo "Timeout aguardando API em $HOST" >&2
exit 1
