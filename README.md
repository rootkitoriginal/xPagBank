# xPagBank - Automação PagBank com Playwright

Sistema de automação para PagBank usando Playwright e FastAPI em container Docker com interface VNC.

## 🚀 Funcionalidades

- **Automação PagBank**: Acesso automatizado ao portal do PagBank com validação de CPF, CNPJ e Email
- **API FastAPI**: API RESTful para automação programática
- **Interface VNC**: Visualização remota do browser via web
- **CLI Integrada**: Comando `login` para facilitar testes
- **Container Docker**: Ambiente isolado e portável
- **Gerenciamento Fácil**: Script utilitário para controle do servidor

## 🔧 Requisitos

- Docker
- Python 3.11+ (para desenvolvimento local)

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
./pagbank.sh login    # Realiza login no PagBank
```

### Login no PagBank

Para realizar login usando o comando CLI:

```bash
# Com email
./pagbank.sh login pagbank usuario@email.com senha123

# Com CPF
./pagbank.sh login pagbank 12345678900 senha123

# Com CNPJ
./pagbank.sh login pagbank 12345678000100 senha123
```

O comando irá:
1. Validar o formato do username (CPF, CNPJ ou Email)
2. Iniciar o navegador automatizado
3. Preencher os campos de login
4. Retornar o status da operação

### API REST

Você também pode usar a API diretamente:

```bash
# Fazer login via API
curl -X POST http://localhost:8000/api/v1/login \
  -H "Content-Type: application/json" \
  -d '{"username":"usuario@email.com","password":"senha123"}'
```

Endpoints disponíveis:
- `GET /` - Health check
- `GET /health` - Status da API
- `POST /api/v1/login` - Realizar login
- `GET /docs` - Documentação Swagger
- `GET /redoc` - Documentação ReDoc

### Acessos

- **API FastAPI**: http://localhost:8000
- **Interface VNC**: http://localhost:6080
- **Documentação API**: http://localhost:8000/docs

## 🏗️ Arquitetura

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────────┐
│   Web Client    │────│   Docker Host    │────│   Container         │
│                 │    │                  │    │                     │
│                 │    │ Port Forwarding  │    │ ┌─────────────────┐ │
│                 │    │ 8000 -> 8000     │    │ │   FastAPI       │ │
│                 │    │ 6080 -> 6080     │    │ │   :8000         │ │
└─────────────────┘    │                  │    │ └─────────────────┘ │
                       │                  │    │ ┌─────────────────┐ │
┌─────────────────┐    │                  │    │ │   noVNC         │ │
│   VNC Client    │────│                  │    │ │   :6080         │ │
│ (Web Browser)   │    │                  │    │ └─────────────────┘ │
└─────────────────┘    └──────────────────┘    │ ┌─────────────────┐ │
                                               │ │   Playwright    │ │
                                               │ │   + Chromium    │ │
                                               │ └─────────────────┘ │
                                               └─────────────────────┘
```

### Fluxo de Operação

1. **CLI**: `./pagbank.sh login pagbank <usuario> <senha>`
2. **API Request**: POST para `/api/v1/login`
3. **Validação**: Validators verificam formato do username
4. **Browser Automation**: Playwright inicia navegador
5. **Interação**: Preenche formulários do PagBank
6. **Resposta**: Retorna status e cookies da sessão

## 🔧 Configuração

### Variáveis de Ambiente

- `DISPLAY`: Display do X11 (padrão: :1)
- `GEOMETRY`: Resolução da tela (padrão: 1920x1080)
- `PYTHONUNBUFFERED`: Logs Python em tempo real (padrão: 1)

### Portas Expostas

- `8000`: API FastAPI
- `6080`: Interface VNC via noVNC

## 📁 Estrutura do Projeto

```
xPagBank/
├── app/
│   ├── controllers/           # Controllers da aplicação
│   │   └── acesso_controller.py  # Controller de autenticação
│   ├── models/                # Modelos Pydantic
│   │   └── acesso.py          # Modelo de requisição
│   ├── routes/                # Rotas FastAPI
│   │   └── acesso.py          # Rotas de autenticação
│   ├── services/              # Serviços
│   │   └── playwright_service.py  # Serviço de automação
│   ├── utils/                 # Utilitários
│   │   ├── validators.py      # Validadores (CPF, CNPJ, Email)
│   │   └── response_parser.py # Parser de respostas
│   ├── main.py                # Aplicação FastAPI principal
│   ├── cli.py                 # CLI para testes locais
│   ├── requirements.txt       # Dependências Python
│   └── server.js              # (Legacy) Servidor Chrome
├── config/
│   └── run.sh                 # Script de inicialização
├── Dockerfile                 # Configuração do container
├── supervisord.conf           # Configuração do supervisor
├── pagbank.sh                 # Script de gerenciamento
└── README.md                  # Este arquivo
```

## 🐛 Resolução de Problemas

### Container não inicia
```bash
./pagbank.sh logs
```

### API não acessível
- Verifique se a porta 8000 está livre
- Confirme se o container está rodando: `./pagbank.sh status`
- Aguarde alguns segundos após iniciar o container

### VNC não acessível
- Verifique se a porta 6080 está livre
- Confirme se o container está rodando: `./pagbank.sh status`

### Erro de validação de username
- Certifique-se de que o CPF/CNPJ está no formato correto
- Para CPF: 11 dígitos numéricos
- Para CNPJ: 14 dígitos numéricos
- Para Email: formato válido (exemplo@dominio.com)

## 📝 Desenvolvimento

Para desenvolvimento local sem Docker:

```bash
# Instalar dependências
pip install -r app/requirements.txt
playwright install chromium

# Iniciar servidor FastAPI
cd app
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Ou usar o CLI para testes
python -m app.cli usuario@email.com senha123
```

### Testes com cURL

```bash
# Health check
curl http://localhost:8000/health

# Login
curl -X POST http://localhost:8000/api/v1/login \
  -H "Content-Type: application/json" \
  -d '{"username":"test@email.com","password":"senha"}'
```

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença ISC.