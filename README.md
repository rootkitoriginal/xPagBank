# xPagBank API

Sistema REST API para pagamentos e transações bancárias usando FastAPI.

## Estrutura do Projeto

```
xPagBank/
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── routers/        # Endpoints (Views)
│   │       └── api.py          # Router aggregator
│   ├── controllers/            # Business logic (Controllers)
│   ├── models/                 # Database models
│   ├── schemas/                # Pydantic schemas
│   ├── services/               # External services
│   └── core/                   # Configuration
├── docs/                       # 📚 Documentação completa
│   ├── API_EXAMPLES.md
│   ├── SETUP_GUIDE.md
│   ├── GIT_WORKFLOW.md
│   ├── PRE_COMMIT_GUIDE.md
│   └── DEPENDABOT_GUIDE.md
├── tests/                      # 🧪 Testes automatizados
│   ├── test_validacao.py
│   ├── test_api_acesso.sh
│   ├── test_health.py
│   └── test_usuario.py
├── main.py                     # Application entry point
└── requirements.txt            # Python dependencies
```

## Arquitetura MVC

- **Models**: Definições de dados e modelos de banco de dados
- **Views**: Endpoints da API (routers)
- **Controllers**: Lógica de negócio

## API Endpoints (v1)

Todos os endpoints estão sob o prefixo `/api/v1/`:

- `GET /api/v1/health` - Health check
- `POST /api/v1/usuario` - Criar usuário
- `POST /api/v1/acesso` - Autenticação/Login
- `POST /api/v1/qrcode` - Gerar QR Code
- `POST /api/v1/confirmaqrcode` - Confirmar QR Code
- `GET /api/v1/saldo` - Consultar saldo
- `POST /api/v1/pix` - Iniciar transação PIX
- `POST /api/v1/confirma_pix` - Confirmar transação PIX

## Instalação

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
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Documentação

📚 **Documentação completa disponível em [`docs/`](./docs/)**

Após iniciar o servidor, acesse:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Guias disponíveis:

- 🚀 [**SETUP_GUIDE.md**](./docs/SETUP_GUIDE.md) - Guia de instalação completo
- 🔌 [**API_EXAMPLES.md**](./docs/API_EXAMPLES.md) - Exemplos práticos de uso da API
- 🔄 [**GIT_WORKFLOW.md**](./docs/GIT_WORKFLOW.md) - Workflow Git e boas práticas
- ✅ [**PRE_COMMIT_GUIDE.md**](./docs/PRE_COMMIT_GUIDE.md) - Configuração do pre-commit
- 🤖 [**DEPENDABOT_GUIDE.md**](./docs/DEPENDABOT_GUIDE.md) - Configuração do Dependabot

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
