FROM mcr.microsoft.com/playwright/python:v1.46.0-jammy

# Instala pacotes para VNC/noVNC (opcional)
RUN apt-get update && apt-get install -y --no-install-recommends \
    x11vnc xvfb fluxbox supervisor websockify wget novnc python3-netifaces \
    && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir -r requirements.txt

# Copia app
COPY app ./app
COPY scripts ./scripts
COPY supervisord.conf .
COPY .env.example ./

ENV PYTHONUNBUFFERED=1
ENV PLAYWRIGHT_BROWSERS_PATH=/ms-playwright
ENV UVICORN_HOST=0.0.0.0
ENV UVICORN_PORT=8000

# Instala browsers (já vem, mas garantimos)
RUN playwright install --with-deps chromium

EXPOSE 8000 5900 7900

CMD ["/usr/bin/supervisord","-c","/app/supervisord.conf"]