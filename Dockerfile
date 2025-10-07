# Dockerfile
# Usando a imagem Playwright base, mas adicionando os pacotes Linux necessários
FROM mcr.microsoft.com/playwright/python:v1.44.0-jammy
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