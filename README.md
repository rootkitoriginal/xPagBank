<<<<<<< HEAD
# xPagBank - Automação PagBank com Playwright

Sistema de automação para PagBank usando Playwright em container Docker com interface VNC.

## 🚀 Funcionalidades

- **Automação PagBank**: Acesso automatizado ao portal do PagBank
- **Interface VNC**: Visualização remota do browser via web
- **CDP Server**: Acesso programático via Chrome DevTools Protocol
- **Container Docker**: Ambiente isolado e portável
- **Gerenciamento Fácil**: Script utilitário para controle do servidor

## 🔧 Requisitos

- Docker
- Node.js 18+ (para desenvolvimento local)

## 📦 Instalação

1. Clone o repositório:
```bash
git clone <url-do-repo>
cd xPagBank
```

2. Construa a imagem Docker:
```bash
./pagbank.sh build
```

## 🎯 Uso

### Scripts Disponíveis

```bash
./pagbank.sh start    # Inicia o servidor
./pagbank.sh stop     # Para o servidor  
./pagbank.sh restart  # Reinicia o servidor
./pagbank.sh logs     # Visualiza os logs
./pagbank.sh status   # Verifica o status
./pagbank.sh build    # Constrói a imagem
./pagbank.sh rebuild  # Reconstrói e reinicia
```

### Acessos

- **Interface VNC**: http://localhost:8080
- **CDP Server**: ws://localhost:3001

## 🏗️ Arquitetura

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   VNC Client    │────│   Docker Host    │────│   Container     │
│ (Web Browser)   │    │                  │    │                 │
│ :8080           │    │ Port Forwarding  │    │ ┌─────────────┐ │
└─────────────────┘    │ 8080 -> 8080     │    │ │   noVNC     │ │
                       │ 3001 -> 3001     │    │ │   :8080     │ │
┌─────────────────┐    │                  │    │ └─────────────┘ │
│   CDP Client    │────│                  │    │ ┌─────────────┐ │
│ (Automation)    │    │                  │    │ │ Playwright  │ │
│ :3001           │    │                  │    │ │   :3001     │ │
└─────────────────┘    └──────────────────┘    │ └─────────────┘ │
                                               │ ┌─────────────┐ │
                                               │ │   Chrome    │ │
                                               │ │ + PagBank   │ │
                                               │ └─────────────┘ │
                                               └─────────────────┘
```

## 🔧 Configuração

### Variáveis de Ambiente

- `DISPLAY`: Display do X11 (padrão: :1)
- `GEOMETRYTRY`: Resolução da tela (padrão: 1920x1080)

### Portas Expostas

- `8080`: Interface VNC via noVNC
- `3001`: Chrome DevTools Protocol

## 📁 Estrutura do Projeto

```
xPagBank/
├── app/
│   └── server.js          # Servidor Chrome simples
├── Dockerfile             # Configuração do container
├── entrypoint.sh          # Script de inicialização
├── server.js              # Servidor principal Playwright
├── supervisord.conf       # Configuração do supervisor
├── pagbank.sh            # Script de gerenciamento
├── package.json          # Dependências Node.js
└── README.md             # Este arquivo
```

## 🐛 Resolução de Problemas

### Container não inicia
```bash
./pagbank.sh logs
```

### VNC não acessível
- Verifique se a porta 8080 está livre
- Confirme se o container está rodando: `./pagbank.sh status`

### CDP não conecta
- Verifique se a porta 3001 está livre
- Aguarde alguns segundos após iniciar o container

## 📝 Desenvolvimento

Para desenvolvimento local:

```bash
npm install
npm start
```

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença ISC.
=======
# xPagBank - Automação Web com Playwright e FastAPI

Uma solução robusta para automação web com interface VNC integrada, usando Python, Playwright, FastAPI e Docker.

## 🌟 Características

- Interface Web VNC para visualização e interação com a automação
- API RESTful com FastAPI para controle da automação
- Persistência de sessões por usuário (cookies e estados)
- Docker container com ambiente completo
- Suporte a múltiplos usuários/sessões
- Interface gráfica integrada via noVNC

## 🔧 Tecnologias

- **Backend**: Python, FastAPI
- **Automação**: Playwright
- **Interface Gráfica**: Xvfb, x11vnc, noVNC
- **Containerização**: Docker
- **Processo**: Supervisord

## 🚀 Como Usar

### Usando Docker (Recomendado)

1. Construa e execute o container:

```bash
docker build -t xpagbank .
docker run -p 8000:8000 -p 6080:6080 -v "$(pwd)/clientes:/data/clientes" xpagbank
```

Ou use o script automatizado:

```bash
./test_and_run.sh
```

2. Acesse:
   - API: [http://localhost:8000/docs](http://localhost:8000/docs)
   - Interface VNC: [http://localhost:6080](http://localhost:6080)

### Desenvolvimento Local

1. Instale as dependências:

```bash
cd app
pip install -r requirements.txt
```

2. Execute a API:

```bash
uvicorn app.main:app --reload --host 0.0.0.0
```

3. Para testar:

```bash
python3 inicia.py
```

## 📁 Estrutura do Projeto

```plaintext
.
├── app/
│   ├── main.py             # API FastAPI
│   ├── browser_logic.py    # Lógica de automação Playwright
│   ├── sessao_interativa.py# Sessão interativa do navegador
│   └── requirements.txt    # Dependências Python
├── config/
│   ├── run.sh             # Script de inicialização
│   └── supervisord.conf    # Configuração do Supervisor
├── clientes/              # Dados persistentes dos usuários
├── Dockerfile            
├── inicia.py             # Script cliente de teste
└── test_and_run.sh       # Script de build e teste
```

## 🔄 API Endpoints

- `GET /health` - Verificação de saúde da API
- `POST /login` - Endpoint de login/automação

```json
{
    "username": "string",
    "password": "string"
}
```

## 💾 Persistência

Os dados dos usuários são armazenados em:

- `/data/clientes/<username>/state.json` - Cookies e estado da sessão
- `/data/clientes/<username>/screenshot_final.png` - Screenshot da última execução

## 🖥️ Interface VNC

A interface VNC permite:

- Visualização em tempo real da automação
- Interação manual quando necessário
- Debugging visual
- Acesso via navegador em [http://localhost:6080](http://localhost:6080)

## 🛡️ Características de Robustez

- Estratégias de fallback para seletores
- Tratamento de erros amigável
- Persistência de sessão
- Timeouts configuráveis
- Logs detalhados

## 🐳 Variáveis de Ambiente

- `HEADLESS`: Controla modo headless do navegador (default: "true")
- `API_VERSION`: Versão da API (default: "1.0")
- `USER_SESSION`: Nome do usuário para sessão interativa

## 📝 Licença

[Incluir sua licença aqui]

## 👥 Contribuição

[Incluir instruções para contribuição aqui]
>>>>>>> 2731bda82163ce02500b423bb5e3d145657354c6
