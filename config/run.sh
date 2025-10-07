#!/bin/bash

# Script de inicialização do container

echo "🚀 Starting xPagBank services..."

# Start X11 virtual framebuffer
echo "Starting Xvfb..."
Xvfb :1 -screen 0 ${GEOMETRY}x24 &
sleep 2

# Start Fluxbox window manager
echo "Starting Fluxbox..."
fluxbox -display :1 &
sleep 2

# Start VNC server
echo "Starting VNC server..."
x11vnc -forever -shared -create -display :1 -nopw &
sleep 2

# Start noVNC
echo "Starting noVNC..."
websockify --web /opt/novnc 6080 localhost:5900 &
sleep 2

# Start FastAPI server
echo "Starting FastAPI server..."
cd /app
uvicorn app.main:app --host 0.0.0.0 --port 8000 &

echo "✅ All services started!"
echo "📊 Service URLs:"
echo "  - API: http://localhost:8000"
echo "  - VNC: http://localhost:6080"

# Keep container running
tail -f /dev/null
