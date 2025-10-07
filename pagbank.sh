#!/bin/bash

# Script para gerenciar o PagBank Server
PROJECT_NAME="pagbank-server"
IMAGE_NAME="xpagbank"

case "$1" in
    "start")
        echo "🚀 Iniciando PagBank Server..."
        docker stop $PROJECT_NAME 2>/dev/null || true
        docker rm $PROJECT_NAME 2>/dev/null || true
        docker run -d -p 8080:8080 -p 3001:3001 --name $PROJECT_NAME $IMAGE_NAME
        echo "✅ Servidor iniciado!"
        echo "🌐 VNC Interface: http://localhost:8080"
        echo "🔗 CDP Server: ws://localhost:3001"
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
    "build")
        echo "🔨 Construindo imagem do PagBank Server..."
        docker build -t $IMAGE_NAME .
        echo "✅ Imagem construída!"
        ;;
    "rebuild")
        echo "🔨 Reconstruindo e reiniciando PagBank Server..."
        $0 stop 2>/dev/null || true
        docker build -t $IMAGE_NAME .
        $0 start
        ;;
    *)
        echo "🤖 PagBank Server Manager"
        echo ""
        echo "Uso: $0 {start|stop|restart|logs|status|build|rebuild}"
        echo ""
        echo "Comandos:"
        echo "  start    - Inicia o servidor"
        echo "  stop     - Para o servidor"
        echo "  restart  - Reinicia o servidor"
        echo "  logs     - Mostra os logs do servidor"
        echo "  status   - Mostra o status do servidor"
        echo "  build    - Constrói a imagem Docker"
        echo "  rebuild  - Reconstrói e reinicia o servidor"
        echo ""
        echo "Acessos:"
        echo "  VNC Interface: http://localhost:8080"
        echo "  CDP Server: ws://localhost:3001"
        ;;
esac