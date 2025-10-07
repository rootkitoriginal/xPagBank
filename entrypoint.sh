#!/bin/bash

# Start Xvfb
Xvfb :1 -screen 0 ${GEOMETRY}x24 &
sleep 2

# Start Fluxbox
fluxbox &
sleep 2

# Start VNC server
x11vnc -display :1 -nopw -listen 0.0.0.0 -forever -xkb &
sleep 2

# Start noVNC
/usr/share/novnc/utils/launch.sh --vnc localhost:5900 --listen 8080 &
sleep 2

echo "Starting supervisord..."
exec /usr/bin/supervisord -n -c /etc/supervisor/conf.d/supervisord.conf
