# 📚 Documentação - xPagBank API# 📚 Documentação - xPagBank API



<div align="center">Este diretório contém toda a documentação do projeto xPagBank API.



[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)## 📁 Estrutura da Documentação

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg?style=for-the-badge&logo=python)](https://www.python.org/)

[![Playwright](https://img.shields.io/badge/Playwright-2EAD33?style=for-the-badge&logo=playwright)](https://playwright.dev/)```

docs/

</div>├── README.md              # Este arquivo - Índice da documentação

├── API_EXAMPLES.md        # Exemplos de uso da API

---├── SETUP_GUIDE.md         # Guia de instalação e configuração

├── GIT_WORKFLOW.md        # Workflow Git e boas práticas

## 🎯 Visão Geral├── PRE_COMMIT_GUIDE.md    # Guia de configuração do pre-commit

└── DEPENDABOT_GUIDE.md    # Guia de configuração do Dependabot

A **xPagBank API** oferece duas versões com abordagens diferentes:```



| Versão | Tecnologia | Velocidade | Robustez | Uso |## 📖 Guias Disponíveis

|--------|-----------|-----------|----------|-----|

| **V1** | HTTP Client (httpx) | ⚡ Muito rápida | 🔸 Pode ser bloqueada | Requisições diretas |### 🚀 [SETUP_GUIDE.md](./SETUP_GUIDE.md)

| **V2** | Browser Automation (Playwright) | 🐢 Mais lenta | ✅ Simula usuário real | Bypass de proteções |Guia completo de instalação e configuração do projeto.



---**Conteúdo:**

- Pré-requisitos

## 📑 Índice da Documentação- Instalação de dependências

- Configuração do ambiente

### 🚀 Início Rápido- Execução do projeto

- Troubleshooting

<table>

<tr>### 🔌 [API_EXAMPLES.md](./API_EXAMPLES.md)

<td width="50%">Exemplos práticos de uso de todos os endpoints da API.



#### 📘 [SETUP_GUIDE.md](./SETUP_GUIDE.md)**Conteúdo:**

**Guia de Instalação e Configuração**- Exemplos de requisições curl

- Exemplos de respostas

- ✅ Pré-requisitos- Casos de uso comuns

- 📦 Instalação de dependências- Códigos de erro

- ⚙️ Configuração do ambiente

- 🚀 Execução do projeto**Endpoints documentados:**

- 🔧 Troubleshooting- `GET /api/v1/health` - Health check

- `POST /api/v1/usuario` - Criar usuário

</td>- `POST /api/v1/acesso` - Validar CPF/CNPJ/Email

<td width="50%">- `POST /api/v1/qrcode` - Gerar QR Code

- `POST /api/v1/confirmaqrcode` - Confirmar QR Code

#### 📗 [API_EXAMPLES.md](./API_EXAMPLES.md)- `GET /api/v1/saldo` - Consultar saldo

**Exemplos Práticos de Uso**- `POST /api/v1/pix` - Realizar PIX

- `POST /api/v1/confirma_pix` - Confirmar PIX

- 🔌 Exemplos de requisições curl

- 📤 Exemplos de respostas### 🔄 [GIT_WORKFLOW.md](./GIT_WORKFLOW.md)

- 💡 Casos de uso comunsWorkflow Git e boas práticas de versionamento.

- ⚠️ Códigos de erro

**Conteúdo:**

</td>- Convenções de commit

</tr>- Branch naming

</table>- Pull Request guidelines

- Code review process

---- Git hooks



### 🎭 Documentação por Versão### ✅ [PRE_COMMIT_GUIDE.md](./PRE_COMMIT_GUIDE.md)

Configuração e uso do pre-commit hooks.

<table>

<tr>**Conteúdo:**

<td width="50%">- Instalação do pre-commit

- Configuração dos hooks

#### 🔵 Versão 1 - HTTP Client- Hooks disponíveis

- Troubleshooting

##### 📘 [HTTP_CLIENT_EXAMPLES.md](./HTTP_CLIENT_EXAMPLES.md)- Bypass (quando necessário)

**Cliente HTTP com httpx**

### 🤖 [DEPENDABOT_GUIDE.md](./DEPENDABOT_GUIDE.md)

- ⚡ Requisições rápidasConfiguração do Dependabot para atualizações automáticas.

- 🍪 Gerenciamento de cookies

- 🔑 Headers customizados**Conteúdo:**

- 🔄 Reutilização de sessão- O que é Dependabot

- Configuração

**Endpoints V1:**- Como funciona

- `GET /api/v1/health`- Gerenciamento de PRs

- `POST /api/v1/usuario`- Boas práticas

- `POST /api/v1/acesso`

- `POST /api/v1/qrcode`## 🎯 Quick Start

- `POST /api/v1/confirmaqrcode`

- `GET /api/v1/saldo`### 1. Configurar Ambiente

- `POST /api/v1/pix````bash

- `POST /api/v1/confirma_pix`# Siga o guia de setup

cat docs/SETUP_GUIDE.md

</td>```

<td width="50%">

### 2. Ver Exemplos de API

#### 🟢 Versão 2 - Browser Automation```bash

# Veja exemplos práticos

##### 📗 [API_V2_GUIDE.md](./API_V2_GUIDE.md)cat docs/API_EXAMPLES.md

**Automação com Playwright**```



- 🌐 Navegador real (Chromium)### 3. Configurar Git Workflow

- 🎭 Simula usuário humano```bash

- 🖼️ Screenshots de debug# Configure pre-commit hooks

- 🍪 Cookies automáticoscat docs/PRE_COMMIT_GUIDE.md

```

**Endpoints V2:**

- `POST /api/v2/acesso`## 📝 Documentação da API (Interativa)

- *(Em desenvolvimento)*

Além desta documentação, você pode acessar a documentação interativa da API:

</td>

</tr>- **Swagger UI**: http://localhost:8874/docs

</table>- **ReDoc**: http://localhost:8874/redoc



---## 🔗 Links Úteis



### ⚙️ Desenvolvimento- [README Principal](../README.md)

- [Tests](../tests/README.md)

<table>- [PyProject](../pyproject.toml)

<tr>- [Requirements](../requirements.txt)

<td width="33%">

## ✨ Como Contribuir com a Documentação

#### 🔄 [GIT_WORKFLOW.md](./GIT_WORKFLOW.md)

**Workflow Git**1. Mantenha a documentação atualizada com o código

2. Use Markdown formatado corretamente

- 📝 Convenções de commit3. Adicione exemplos práticos sempre que possível

- 🌳 Branch naming4. Inclua screenshots quando apropriado

- 🔀 Pull Request guidelines5. Atualize este README ao adicionar novos documentos

- 👀 Code review process

- 🪝 Git hooks## 📮 Estrutura de um Bom Documento



</td>```markdown

<td width="33%"># Título do Documento



#### ✅ [PRE_COMMIT_GUIDE.md](./PRE_COMMIT_GUIDE.md)## Visão Geral

**Pre-commit Hooks**Breve descrição do que o documento cobre



- 🔧 Instalação## Pré-requisitos

- ⚙️ ConfiguraçãoO que é necessário antes de começar

- 🛠️ Hooks disponíveis

- 🔧 Troubleshooting## Passo a Passo

- ⏭️ BypassInstruções detalhadas



</td>## Exemplos

<td width="33%">Exemplos práticos de uso



#### 🤖 [DEPENDABOT_GUIDE.md](./DEPENDABOT_GUIDE.md)## Troubleshooting

**Dependabot**Problemas comuns e soluções



- 📦 O que é Dependabot## Referências

- ⚙️ ConfiguraçãoLinks e recursos adicionais

- ⚡ Como funciona```

- 🔀 Gerenciamento de PRs

- ✅ Boas práticas## 🎨 Convenções de Markdown



</td>- Use `#` para títulos principais

</tr>- Use `##` para seções

</table>- Use `###` para subseções

- Use ` ``` ` para blocos de código

---- Use emojis para melhor visualização 🎉

- Use links relativos para documentos internos

## 🎯 Quick Start

---

### 1️⃣ Escolha sua versão

**Última atualização:** 6 de outubro de 2025

<details>**Versão da API:** 1.0.0

<summary><b>📘 Usar V1 (HTTP Client)</b> - Recomendado para velocidade</summary>

```bash
# 1. Instalar dependências
pip install -r requirements.txt

# 2. Iniciar servidor
python3 main.py

# 3. Testar endpoint
curl -X POST http://localhost:8874/api/v1/acesso \
  -H 'Content-Type: application/json' \
  -d '{"username": "123.456.789-09"}'
```

**✅ Vantagens:**
- ⚡ Muito rápido
- 💚 Baixo consumo de recursos
- 🔄 Múltiplas requisições simultâneas

**⚠️ Limitações:**
- Pode ser bloqueado por Cloudflare
- Não executa JavaScript

</details>

<details>
<summary><b>📗 Usar V2 (Browser Automation)</b> - Recomendado para robustez</summary>

```bash
# 1. Instalar dependências
pip install -r requirements.txt

# 2. Instalar navegador Chromium
python3 -m playwright install chromium

# 3. (Opcional) Instalar deps do sistema
sudo playwright install-deps chromium

# 4. Iniciar servidor
python3 main.py

# 5. Testar endpoint
curl -X POST http://localhost:8874/api/v2/acesso \
  -H 'Content-Type: application/json' \
  -d '{"username": "test@example.com"}'
```

**✅ Vantagens:**
- ✅ Simula usuário real
- 🛡️ Bypass de Cloudflare
- 🖼️ Screenshots de debug
- ✅ Executa JavaScript

**⚠️ Limitações:**
- 🐢 Mais lento
- 🔴 Alto consumo de recursos

</details>

---

### 2️⃣ Documentação Interativa

Após iniciar o servidor, acesse:

- 📖 **Swagger UI**: http://localhost:8874/docs
- 📘 **ReDoc**: http://localhost:8874/redoc

---

## 🔀 Quando usar cada versão?

### Use V1 quando:
- ✅ Velocidade é prioridade
- ✅ Consumo de recursos é limitado
- ✅ Fazer muitas requisições simultâneas
- ✅ API não tem proteção JavaScript complexa

### Use V2 quando:
- ✅ V1 está sendo bloqueado
- ✅ Precisa executar JavaScript
- ✅ Precisa simular comportamento real
- ✅ Precisa capturar screenshots
- ✅ Debug visual é importante

---

## 📊 Comparação Detalhada

| Característica | V1 (HTTP) | V2 (Browser) |
|----------------|-----------|--------------|
| **Velocidade** | ⚡⚡⚡⚡⚡ | ⚡⚡ |
| **Consumo RAM** | ~50MB | ~300MB |
| **Cloudflare** | ❌ Bloqueado | ✅ Bypass |
| **JavaScript** | ❌ Não executa | ✅ Executa |
| **Screenshots** | ❌ Não | ✅ Sim |
| **Debug** | 📝 Logs HTTP | 🖼️ Visual |
| **Paralelismo** | ✅ Alto | ⚠️ Limitado |
| **Setup** | ✅ Simples | ⚠️ Requer browser |

---

## 🏗️ Estrutura do Projeto

```
xPagBank/
├── app/
│   ├── api/
│   │   ├── v1/           # API V1 (HTTP Client)
│   │   │   └── routers/
│   │   └── v2/           # API V2 (Browser)
│   │       └── routers/
│   ├── controllers/
│   │   ├── v1/           # Controllers V1
│   │   ├── v2/           # Controllers V2
│   │   └── health_controller.py  # Compartilhado
│   ├── services/
│   │   ├── http_client.py        # Cliente HTTP V1
│   │   └── playwright_service.py # Browser V2
│   ├── utils/
│   │   └── response_parser.py    # Parser compartilhado
│   ├── schemas/          # Pydantic models
│   └── models/           # Database models
├── docs/                 # Esta documentação
├── tests/                # Testes
└── main.py               # Entry point
```

---

## 📚 Documentação Adicional

### 📖 Guias Completos

| Documento | Descrição |
|-----------|-----------|
| [SETUP_GUIDE.md](./SETUP_GUIDE.md) | Guia completo de instalação |
| [API_EXAMPLES.md](./API_EXAMPLES.md) | Exemplos de uso da API V1 |
| [API_V2_GUIDE.md](./API_V2_GUIDE.md) | Guia completo da API V2 |
| [HTTP_CLIENT_EXAMPLES.md](./HTTP_CLIENT_EXAMPLES.md) | Exemplos do cliente HTTP |
| [GIT_WORKFLOW.md](./GIT_WORKFLOW.md) | Workflow Git e convenções |
| [PRE_COMMIT_GUIDE.md](./PRE_COMMIT_GUIDE.md) | Configuração de hooks |
| [DEPENDABOT_GUIDE.md](./DEPENDABOT_GUIDE.md) | Atualizações automáticas |

---

## 🆘 Suporte

### 📝 Logs e Debug

**V1 (HTTP Client):**
```python
# Logs automáticos em app/services/http_client.py
# Verifique o console para ver requisições e respostas
```

**V2 (Browser):**
```python
# Screenshots automáticos em caso de erro
# Arquivos salvos em: /tmp/pagbank-error-*.png
```

### 🔧 Troubleshooting

Consulte a seção de troubleshooting em:
- [SETUP_GUIDE.md](./SETUP_GUIDE.md#troubleshooting)
- [API_V2_GUIDE.md](./API_V2_GUIDE.md#troubleshooting)

---

## 📞 Contato

Para dúvidas ou sugestões, abra uma issue no GitHub.

---

<div align="center">

**Feito com ❤️ usando FastAPI + Playwright**

[⬆ Voltar ao topo](#-documentação---xpagbank-api)

</div>
