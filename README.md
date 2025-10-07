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