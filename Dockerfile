<<<<<<< HEAD
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
=======
# Dockerfile
# Usando a imagem Playwright base, mas adicionando os pacotes Linux necessários
FROM mcr.microsoft.com/playwright/python:v1.55.0-jammy
ENV DEBIAN_FRONTEND="noninteractive"
ENV TZ="Etc/UTC"
# 1. Instalação da Stack VNC/Supervisor/X11
RUN apt-get update && \
    # Instala os componentes gráficos, VNC, Websockify e Supervisor
    apt-get install -y --no-install-recommends \
        x11vnc \
        xvfb \
        fluxbox \
        supervisor \
        websockify \
        wget \
        novnc \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# 2. Configuração e Dependências Python
WORKDIR /app
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 3. Copia o código e as configurações
COPY app/ /app/app/
COPY config/ /config/

# Configura o noVNC
RUN mkdir -p /opt/novnc && \
    wget -qO /opt/novnc.tar.gz https://github.com/novnc/noVNC/archive/v1.3.0.tar.gz && \
    tar xzf /opt/novnc.tar.gz --strip-components=1 -C /opt/novnc && \
    rm /opt/novnc.tar.gz && \
    ln -s /opt/novnc/vnc.html /opt/novnc/index.html

# Configurações de Permissão
RUN chmod +x /config/run.sh

# Expõe as portas: 8000 (FastAPI) e 6080 (Websockify/noVNC)
EXPOSE 8000
EXPOSE 6080

# Define o comando de entrada
CMD ["/config/run.sh"]
>>>>>>> 2731bda82163ce02500b423bb5e3d145657354c6
