#!/bin/bash

# Start Xvfb
Xvfb :1 -screen 0 ${GEOMETRY}x24 &

# Start Fluxbox
fluxbox &

# Start VNC server
x11vnc -display :1 -nopw -listen 0.0.0.0 -forever -xkb &

# Start noVNC
/usr/share/novnc/utils/launch.sh --vnc localhost:5900 --listen 8080 &

# Start the Node.js application
node /app/server.js
