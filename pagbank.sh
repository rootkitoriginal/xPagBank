#!/bin/bash

# Script para gerenciar o PagBank Server
PROJECT_NAME="pagbank-server"
IMAGE_NAME="xpagbank:latest"

case "$1" in
    "start")
        echo "🚀 Iniciando PagBank Server..."
        docker stop $PROJECT_NAME 2>/dev/null || true
        docker rm $PROJECT_NAME 2>/dev/null || true
        docker run -d -p 8000:8000 -p 6080:6080 --name $PROJECT_NAME $IMAGE_NAME
        echo "✅ Servidor iniciado!"
        echo "🌐 API: http://localhost:8000"
        echo "🔗 VNC Interface: http://localhost:6080"
        ;;
    "stop")
        echo "🛑 Parando PagBank Server..."
        docker stop $PROJECT_NAME
        docker rm $PROJECT_NAME
        echo "✅ Servidor parado!"
        ;;
    "restart")
        echo "🔄 Reiniciando PagBank Server..."
        $0 stop
        sleep 2
        $0 start
        ;;
    "logs")
        echo "📋 Logs do PagBank Server:"
        docker logs -f $PROJECT_NAME
        ;;
    "status")
        echo "📊 Status do PagBank Server:"
        docker ps | grep $PROJECT_NAME || echo "❌ Servidor não está rodando"
        ;;
    "pull"|"build")
        echo "� Baixando imagem do PagBank Server..."
        docker pull $IMAGE_NAME
        echo "✅ Imagem baixada!"
        ;;
    "rebuild")
        echo "� Baixando nova versão e reiniciando PagBank Server..."
        $0 stop 2>/dev/null || true
        docker pull $IMAGE_NAME
        $0 start
        ;;
    "login")
        if [ "$2" != "pagbank" ]; then
            echo "❌ Uso: $0 login pagbank <usuario> <senha>"
            exit 1
        fi
        
        if [ -z "$3" ]; then
            echo "❌ Erro: Usuário não fornecido"
            echo "Uso: $0 login pagbank <usuario> <senha>"
            exit 1
        fi
        
        USERNAME="$3"
        PASSWORD="${4:-}"
        
        echo "🔐 Realizando login no PagBank..."
        echo "👤 Usuário: $USERNAME"
        
        # Verifica se o servidor está rodando
        if ! docker ps | grep -q $PROJECT_NAME; then
            echo "⚠️  Servidor não está rodando. Iniciando..."
            $0 start
            echo "⏳ Aguardando servidor iniciar..."
            sleep 5
        fi
        
        # Cria JSON payload
        if [ -n "$PASSWORD" ]; then
            JSON_PAYLOAD="{\"username\":\"$USERNAME\",\"password\":\"$PASSWORD\"}"
        else
            JSON_PAYLOAD="{\"username\":\"$USERNAME\"}"
        fi
        
        # Faz requisição para a API
        echo "📡 Enviando requisição para API..."
        RESPONSE=$(curl -s -X POST \
            -H "Content-Type: application/json" \
            -d "$JSON_PAYLOAD" \
            http://localhost:8000/api/v1/login)
        
        # Exibe resposta formatada
        echo ""
        echo "📋 Resposta:"
        echo "$RESPONSE" | python3 -m json.tool 2>/dev/null || echo "$RESPONSE"
        echo ""
        ;;
    *)
        echo "🤖 PagBank Server Manager"
        echo ""
        echo "Uso: $0 {start|stop|restart|logs|status|pull|rebuild|login}"
        echo ""
        echo "Comandos:"
        echo "  start    - Inicia o servidor"
        echo "  stop     - Para o servidor"
        echo "  restart  - Reinicia o servidor"
        echo "  logs     - Mostra os logs do servidor"
        echo "  status   - Mostra o status do servidor"
        echo "  pull     - Baixa a imagem Docker mais recente"
        echo "  rebuild  - Baixa nova versão e reinicia o servidor"
        echo "  login    - Realiza login no PagBank"
        echo ""
        echo "Exemplos de uso do login:"
        echo "  $0 login pagbank usuario@email.com senha123"
        echo "  $0 login pagbank 12345678900 senha123"
        echo ""
        echo "Acessos:"
        echo "  API: http://localhost:8000"
        echo "  VNC Interface: http://localhost:6080"
        ;;
esac