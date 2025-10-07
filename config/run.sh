#!/bin/bash
# config/run.sh

# Garante que os arquivos de lock antigos do Xvfb sejam removidos
rm -f /tmp/.X99-lock

# Inicia o Supervisor, que por sua vez inicia todos os serviços (Xvfb, VNC, FastAPI)
echo "Iniciando todos os serviços com Supervisor..."
exec /usr/bin/supervisord -c /config/supervisord.conf