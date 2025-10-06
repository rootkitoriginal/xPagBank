# 📚 Documentação - xPagBank API

Este diretório contém toda a documentação do projeto xPagBank API.

## 📁 Estrutura da Documentação

```
docs/
├── README.md              # Este arquivo - Índice da documentação
├── API_EXAMPLES.md        # Exemplos de uso da API
├── SETUP_GUIDE.md         # Guia de instalação e configuração
├── GIT_WORKFLOW.md        # Workflow Git e boas práticas
├── PRE_COMMIT_GUIDE.md    # Guia de configuração do pre-commit
└── DEPENDABOT_GUIDE.md    # Guia de configuração do Dependabot
```

## 📖 Guias Disponíveis

### 🚀 [SETUP_GUIDE.md](./SETUP_GUIDE.md)
Guia completo de instalação e configuração do projeto.

**Conteúdo:**
- Pré-requisitos
- Instalação de dependências
- Configuração do ambiente
- Execução do projeto
- Troubleshooting

### 🔌 [API_EXAMPLES.md](./API_EXAMPLES.md)
Exemplos práticos de uso de todos os endpoints da API.

**Conteúdo:**
- Exemplos de requisições curl
- Exemplos de respostas
- Casos de uso comuns
- Códigos de erro

**Endpoints documentados:**
- `GET /api/v1/health` - Health check
- `POST /api/v1/usuario` - Criar usuário
- `POST /api/v1/acesso` - Validar CPF/CNPJ/Email
- `POST /api/v1/qrcode` - Gerar QR Code
- `POST /api/v1/confirmaqrcode` - Confirmar QR Code
- `GET /api/v1/saldo` - Consultar saldo
- `POST /api/v1/pix` - Realizar PIX
- `POST /api/v1/confirma_pix` - Confirmar PIX

### 🔄 [GIT_WORKFLOW.md](./GIT_WORKFLOW.md)
Workflow Git e boas práticas de versionamento.

**Conteúdo:**
- Convenções de commit
- Branch naming
- Pull Request guidelines
- Code review process
- Git hooks

### ✅ [PRE_COMMIT_GUIDE.md](./PRE_COMMIT_GUIDE.md)
Configuração e uso do pre-commit hooks.

**Conteúdo:**
- Instalação do pre-commit
- Configuração dos hooks
- Hooks disponíveis
- Troubleshooting
- Bypass (quando necessário)

### 🤖 [DEPENDABOT_GUIDE.md](./DEPENDABOT_GUIDE.md)
Configuração do Dependabot para atualizações automáticas.

**Conteúdo:**
- O que é Dependabot
- Configuração
- Como funciona
- Gerenciamento de PRs
- Boas práticas

## 🎯 Quick Start

### 1. Configurar Ambiente
```bash
# Siga o guia de setup
cat docs/SETUP_GUIDE.md
```

### 2. Ver Exemplos de API
```bash
# Veja exemplos práticos
cat docs/API_EXAMPLES.md
```

### 3. Configurar Git Workflow
```bash
# Configure pre-commit hooks
cat docs/PRE_COMMIT_GUIDE.md
```

## 📝 Documentação da API (Interativa)

Além desta documentação, você pode acessar a documentação interativa da API:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🔗 Links Úteis

- [README Principal](../README.md)
- [Tests](../tests/README.md)
- [PyProject](../pyproject.toml)
- [Requirements](../requirements.txt)

## ✨ Como Contribuir com a Documentação

1. Mantenha a documentação atualizada com o código
2. Use Markdown formatado corretamente
3. Adicione exemplos práticos sempre que possível
4. Inclua screenshots quando apropriado
5. Atualize este README ao adicionar novos documentos

## 📮 Estrutura de um Bom Documento

```markdown
# Título do Documento

## Visão Geral
Breve descrição do que o documento cobre

## Pré-requisitos
O que é necessário antes de começar

## Passo a Passo
Instruções detalhadas

## Exemplos
Exemplos práticos de uso

## Troubleshooting
Problemas comuns e soluções

## Referências
Links e recursos adicionais
```

## 🎨 Convenções de Markdown

- Use `#` para títulos principais
- Use `##` para seções
- Use `###` para subseções
- Use ` ``` ` para blocos de código
- Use emojis para melhor visualização 🎉
- Use links relativos para documentos internos

---

**Última atualização:** 6 de outubro de 2025
**Versão da API:** 1.0.0
