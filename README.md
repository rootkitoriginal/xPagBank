# xPagBank API

Sistema REST API para pagamentos e transações bancárias usando FastAPI.

## 🎯 Duas Versões Disponíveis

| Versão | Tecnologia | Velocidade | Robustez | Recomendado para |
|--------|-----------|-----------|----------|------------------|
| **V1** | HTTP Client (httpx) | ⚡ Muito rápida | 🔸 Pode ser bloqueada | Velocidade e eficiência |
| **V2** | Browser Automation (Playwright) | 🐢 Mais lenta | ✅ Simula usuário real | Bypass de proteções |

## Estrutura do Projeto

```
xPagBank/
├── app/
│   ├── api/
│   │   ├── v1/                 # API V1 (HTTP Client)
│   │   │   └── routers/        # Endpoints V1
│   │   └── v2/                 # API V2 (Browser Automation)
│   │       └── routers/        # Endpoints V2
│   ├── controllers/
│   │   ├── v1/                 # Controllers V1 (HTTP)
│   │   ├── v2/                 # Controllers V2 (Browser)
│   │   └── health_controller.py # Compartilhado
│   ├── services/
│   │   ├── http_client.py      # 🌐 Cliente HTTP V1
│   │   └── playwright_service.py # 🎭 Browser Automation V2
│   ├── utils/
│   │   └── response_parser.py  # 🔧 Parser compartilhado
│   ├── models/                 # Database models
│   ├── schemas/                # Pydantic schemas
│   └── core/                   # Configuration
├── docs/                       # 📚 Documentação completa
│   ├── README.md               # 📖 Índice da documentação
│   ├── API_EXAMPLES.md         # Exemplos V1
│   ├── API_V2_GUIDE.md         # 🎭 Guia completo V2
│   ├── HTTP_CLIENT_EXAMPLES.md # 🌐 Guia do HTTP Client
│   ├── SETUP_GUIDE.md
│   ├── GIT_WORKFLOW.md
│   ├── PRE_COMMIT_GUIDE.md
│   └── DEPENDABOT_GUIDE.md
├── tests/                      # 🧪 Testes automatizados
├── main.py                     # Application entry point
└── requirements.txt            # Python dependencies
```

## Arquitetura MVC

- **Models**: Definições de dados e modelos de banco de dados
- **Views**: Endpoints da API (routers) - v1 e v2
- **Controllers**: Lógica de negócio - v1 (HTTP) e v2 (Browser)

## API Endpoints

### 🔵 V1 - HTTP Client (httpx)

Todos os endpoints estão sob o prefixo `/api/v1/`:

- `GET /api/v1/health` - Health check
- `POST /api/v1/usuario` - Criar usuário
- `POST /api/v1/acesso` - Autenticação/Login
- `POST /api/v1/qrcode` - Gerar QR Code
- `POST /api/v1/confirmaqrcode` - Confirmar QR Code
- `GET /api/v1/saldo` - Consultar saldo
- `POST /api/v1/pix` - Iniciar transação PIX
- `POST /api/v1/confirma_pix` - Confirmar transação PIX

### 🟢 V2 - Browser Automation (Playwright)

Todos os endpoints estão sob o prefixo `/api/v2/`:

- `POST /api/v2/acesso` - Autenticação/Login via navegador real

> 💡 **Dica**: Use V1 para velocidade, V2 para bypass de proteções Cloudflare

## Instalação

### Opção 1: V1 apenas (HTTP Client)

1. Instalar dependências:
```bash
pip install -r requirements.txt
```

2. Executar o servidor:
```bash
python main.py
```

Ou com uvicorn diretamente:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8874
```

## Documentação

📚 **Documentação completa disponível em [`docs/`](./docs/)**

Após iniciar o servidor, acesse:

- **Swagger UI**: http://localhost:8874/docs
- **ReDoc**: http://localhost:8874/redoc

### Guias disponíveis

- 🚀 [**SETUP_GUIDE.md**](./docs/SETUP_GUIDE.md) - Guia de instalação completo
- 🔌 [**API_EXAMPLES.md**](./docs/API_EXAMPLES.md) - Exemplos práticos de uso da API
- 🌐 [**HTTP_CLIENT_EXAMPLES.md**](./docs/HTTP_CLIENT_EXAMPLES.md) - Guia completo do HTTP Client
- 🔄 [**GIT_WORKFLOW.md**](./docs/GIT_WORKFLOW.md) - Workflow Git e boas práticas
- ✅ [**PRE_COMMIT_GUIDE.md**](./docs/PRE_COMMIT_GUIDE.md) - Configuração do pre-commit
- 🤖 [**DEPENDABOT_GUIDE.md**](./docs/DEPENDABOT_GUIDE.md) - Configuração do Dependabot

## HTTP Client

🌐 **Cliente HTTP reutilizável para integração com APIs**

O projeto inclui um cliente HTTP avançado (`PagBankHttpClient`) que facilita requisições:

- ✅ **Métodos HTTP**: GET, POST, PUT, DELETE, HEAD
- ✅ **Gerenciamento de Cookies**: Persistência automática entre requisições
- ✅ **Base URL Configurável**: Default `https://pagbank.com.br`
- ✅ **Headers Padrão**: User-Agent, Accept, Content-Type pré-configurados
- ✅ **Timeout Configurável**: Default 30 segundos

**Exemplo de uso:**

```python
from app.services.http_client import PagBankHttpClient

# Inicializa o cliente
client = PagBankHttpClient(base_url="https://api.pagbank.com.br")

# Faz login (cookies são salvos automaticamente)
response = await client.post(
    path="/api/v1/login",
    json={"username": "user@example.com"}
)

# Requisições seguintes reutilizam cookies automaticamente
profile = await client.get("/api/v1/profile")
```

📖 **[Ver documentação completa do HTTP Client](./docs/HTTP_CLIENT_EXAMPLES.md)**

## Configuração

As configurações estão em `app/core/config.py`. Você pode criar um arquivo `.env` para sobrescrever valores padrão:

```env
APP_NAME=xPagBank API
APP_VERSION=1.0.0
DEBUG=True
SECRET_KEY=your-secret-key-here
```

## Git Workflow

Integração com GitHub CLI (`gh`):

```bash
# Criar branch
gh repo clone <repo>
git checkout -b feature/nova-funcionalidade

# Commit e push
git add .
git commit -m "feat: nova funcionalidade"
git push origin feature/nova-funcionalidade

# Criar PR
gh pr create --title "Nova funcionalidade" --body "Descrição"

# Revisar e merge
gh pr merge <pr-number>
```

## Versionamento

A API suporta versionamento. Para criar uma nova versão:

1. Criar diretório `app/api/v2/`
2. Copiar estrutura de `v1` e fazer alterações
3. Atualizar `main.py` para incluir novo router
4. Endpoints ficarão disponíveis em `/api/v2/`

## Desenvolvimento

### Adicionar novo endpoint:

1. Criar schema em `app/schemas/`
2. Criar controller em `app/controllers/`
3. Criar router em `app/api/v1/routers/`
4. Registrar router em `app/api/v1/api.py`

## Tecnologias

- **FastAPI**: Framework web moderno e rápido
- **Pydantic**: Validação de dados
- **Uvicorn**: ASGI server
- **Python 3.10+**
