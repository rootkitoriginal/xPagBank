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
- `GEOMETRY`: Resolução da tela (padrão: 1920x1080)

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