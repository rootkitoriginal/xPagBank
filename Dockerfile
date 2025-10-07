# Use an official Node.js runtime as a parent image
FROM node:18

# Set environment variables
ENV DISPLAY=:1
ENV GEOMETRY="1920x1080"
ENV CHROME_FLAGS="--no-sandbox --disable-gpu --user-data-dir=/tmp/user-data"

# Install dependencies
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    xvfb \
    fluxbox \
    x11vnc \
    novnc \
    supervisor \
    --no-install-recommends \
    && wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

# Create app directory
WORKDIR /app

# Copy all files
COPY . .

# Install dependencies
RUN npm install && npx playwright install chromium
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Create necessary directories
RUN mkdir -p /var/log/supervisor

# Expose ports
EXPOSE 8080 3001

# Start supervisor
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
