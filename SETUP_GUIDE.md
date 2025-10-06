# xPagBank API - Guia Completo de Setup e Desenvolvimento

## 🚀 Status do Projeto

✅ **Projeto completamente configurado e funcional!**

O servidor FastAPI está rodando em: **http://localhost:8000**

## 📋 O que foi criado

### 1. Estrutura MVC Completa

```
xPagBank/
├── .github/
│   ├── workflows/
│   │   └── ci-cd.yml           # GitHub Actions CI/CD
│   └── copilot-instructions.md # Instruções do projeto
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── routers/        # 8 endpoints implementados
│   │       │   ├── health.py
│   │       │   ├── usuario.py
│   │       │   ├── acesso.py
│   │       │   ├── qrcode.py
│   │       │   ├── confirmaqrcode.py
│   │       │   ├── saldo.py
│   │       │   ├── pix.py
│   │       │   └── confirma_pix.py
│   │       └── api.py          # Router aggregator
│   ├── controllers/            # Business logic (8 controllers)
│   ├── schemas/                # Pydantic models (8 schemas)
│   ├── models/                 # Database models (para futuro)
│   ├── services/               # External services (para futuro)
│   └── core/
│       └── config.py           # Configurações da aplicação
├── tests/
│   ├── test_health.py
│   └── test_usuario.py
├── main.py                     # Application entry point
├── requirements.txt            # Production dependencies
├── requirements-dev.txt        # Development dependencies
├── pyproject.toml             # Pytest configuration
├── README.md                   # Documentação completa
├── GIT_WORKFLOW.md            # Workflow Git com gh CLI
└── .gitignore                 # Git ignore rules
```

### 2. API Endpoints (v1)

Todos os endpoints estão sob `/api/v1/`:

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/api/v1/health` | Health check |
| POST | `/api/v1/usuario` | Criar usuário |
| POST | `/api/v1/acesso` | Login/Autenticação |
| POST | `/api/v1/qrcode` | Gerar QR Code |
| POST | `/api/v1/confirmaqrcode` | Confirmar QR Code |
| GET | `/api/v1/saldo` | Consultar saldo |
| POST | `/api/v1/pix` | Iniciar PIX |
| POST | `/api/v1/confirma_pix` | Confirmar PIX |

### 3. Arquitetura MVC

- **Models** (`app/models/`): Definições de dados e banco
- **Views** (`app/api/v1/routers/`): Endpoints da API
- **Controllers** (`app/controllers/`): Lógica de negócio

### 4. Schemas Pydantic

Todos os endpoints possuem schemas de request e response com validação automática:
- Validação de tipos
- Validação de formato (email, CPF, etc)
- Valores opcionais e obrigatórios
- Valores mínimos/máximos

## 🏃 Como executar

### Opção 1: Diretamente com Python

```bash
python3 main.py
```

### Opção 2: Com Uvicorn

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Opção 3: Usando a Task do VS Code

1. Pressione `Ctrl+Shift+P`
2. Digite "Tasks: Run Task"
3. Selecione "Run xPagBank API Server"

## 📚 Documentação da API

Após iniciar o servidor, acesse:

- **Swagger UI (interativa)**: http://localhost:8000/docs
- **ReDoc (documentação)**: http://localhost:8000/redoc
- **Root endpoint**: http://localhost:8000/

## 🧪 Testes

### Executar testes

```bash
# Instalar dependências de desenvolvimento
pip install -r requirements-dev.txt

# Executar todos os testes
pytest

# Executar com cobertura
pytest --cov=app

# Executar teste específico
pytest tests/test_health.py
```

### Estrutura de testes

- `tests/test_health.py` - Testes do endpoint de health
- `tests/test_usuario.py` - Testes do endpoint de usuário

## 🔧 Configuração

### Variáveis de Ambiente

Crie um arquivo `.env` baseado no `.env.example`:

```env
APP_NAME=xPagBank API
APP_VERSION=1.0.0
DEBUG=True
SECRET_KEY=sua-chave-secreta-aqui
DATABASE_URL=sqlite:///./xpagbank.db
```

### Configurações principais

Arquivo: `app/core/config.py`

- `API_V1_PREFIX`: Prefixo dos endpoints v1
- `SECRET_KEY`: Chave para JWT
- `ACCESS_TOKEN_EXPIRE_MINUTES`: Tempo de expiração do token

## 🔄 Git Workflow

### Configuração inicial

```bash
# Instalar GitHub CLI
sudo apt install gh

# Login
gh auth login

# Criar repositório
gh repo create xPagBank --public --source=. --remote=origin --push
```

### Workflow de desenvolvimento

```bash
# 1. Criar feature branch
git checkout -b feature/nova-funcionalidade

# 2. Fazer mudanças e commit
git add .
git commit -m "feat: adiciona nova funcionalidade"

# 3. Push e criar PR
git push -u origin feature/nova-funcionalidade
gh pr create --title "Feature: Nova Funcionalidade" --body "Descrição"

# 4. Após aprovação, fazer merge
gh pr merge <número-pr> --squash
```

Veja `GIT_WORKFLOW.md` para mais detalhes.

## 📦 Versionamento da API

### Criar nova versão (v2)

1. Copiar estrutura v1:
```bash
cp -r app/api/v1 app/api/v2
```

2. Atualizar `app/core/config.py`:
```python
API_V2_PREFIX: str = "/api/v2"
```

3. Criar novo router em `app/api/v2/api.py`

4. Registrar no `main.py`:
```python
app.include_router(api_router_v2, prefix=settings.API_V2_PREFIX)
```

5. Endpoints estarão disponíveis em `/api/v2/`

## 🚀 Próximos Passos

### 1. Implementar Banco de Dados

- [ ] Adicionar SQLAlchemy models em `app/models/`
- [ ] Configurar conexão com banco
- [ ] Criar migrations com Alembic
- [ ] Implementar CRUD operations

### 2. Implementar Autenticação

- [ ] JWT token generation
- [ ] Middleware de autenticação
- [ ] Proteção de rotas
- [ ] Refresh tokens

### 3. Adicionar Validações

- [ ] Validação de CPF
- [ ] Validação de chave PIX
- [ ] Validação de saldo
- [ ] Rate limiting

### 4. Melhorar Testes

- [ ] Aumentar cobertura de testes
- [ ] Testes de integração
- [ ] Testes de carga
- [ ] Mock de serviços externos

### 5. Deploy

- [ ] Docker e docker-compose
- [ ] Configuração de produção
- [ ] CI/CD completo
- [ ] Monitoramento e logs

## 📖 Recursos Adicionais

### Documentação FastAPI
- https://fastapi.tiangolo.com/

### Pydantic
- https://docs.pydantic.dev/

### GitHub CLI
- https://cli.github.com/manual/

### Python Best Practices
- https://docs.python-guide.org/

## 🤝 Contribuindo

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'feat: Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Convenção de Commits

- `feat:` Nova funcionalidade
- `fix:` Correção de bug
- `docs:` Mudanças na documentação
- `style:` Formatação de código
- `refactor:` Refatoração de código
- `test:` Adição ou correção de testes
- `chore:` Tarefas de manutenção

## 📄 Licença

Este projeto está sob a licença MIT.

## 👥 Autores

- Desenvolvido com FastAPI e ❤️

---

**Status Atual**: ✅ Pronto para desenvolvimento

**Servidor**: 🟢 Rodando em http://localhost:8000

**Documentação**: 📚 http://localhost:8000/docs
