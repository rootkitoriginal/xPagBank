# Dockerfile
# Using Playwright Python base image with necessary Linux packages
FROM mcr.microsoft.com/playwright/python:v1.48.0-jammy

ENV DEBIAN_FRONTEND="noninteractive"
ENV TZ="Etc/UTC"
ENV DISPLAY=:1
ENV GEOMETRY="1920x1080"

# 1. Install VNC/Supervisor/X11 Stack
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        x11vnc \
        xvfb \
        fluxbox \
        supervisor \
        websockify \
        wget \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# 2. Configure noVNC
RUN mkdir -p /opt/novnc && \
    wget -qO /opt/novnc.tar.gz https://github.com/novnc/noVNC/archive/v1.3.0.tar.gz && \
    tar xzf /opt/novnc.tar.gz --strip-components=1 -C /opt/novnc && \
    rm /opt/novnc.tar.gz && \
    ln -s /opt/novnc/vnc.html /opt/novnc/index.html

# 3. Setup Python dependencies
WORKDIR /app
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && \
    playwright install chromium

# 4. Copy application code and configurations
COPY app/ /app/app/
COPY config/ /config/
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# 5. Set permissions
RUN chmod +x /config/run.sh

# 6. Create log directories
RUN mkdir -p /var/log/supervisor

# Expose ports: 8000 (FastAPI) and 6080 (noVNC)
EXPOSE 8000
EXPOSE 6080

# Start supervisor
CMD ["/config/run.sh"]
