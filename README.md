# PagBank Login Automation (FastAPI + Playwright + VNC opcional)

Este projeto implementa:
- API FastAPI para iniciar fluxo de login no PagBank
- Automação Playwright com múltiplas estratégias de fallback
- Salvamento de cookies + screenshot em `clientes/<username>`
- Execução via Docker (com ou sem interface)
- Suporte opcional a VNC/noVNC para visualizar e interagir com o navegador em modo headful

## Endpoints

### POST /login
Body JSON:
```json
{
  "username": "seu_usuario",
  "password": "sua_senha",
  "headless": false
}
```

Resposta:
```json
{
  "success": true,
  "username": "seu_usuario",
  "screenshot": "clientes/seu_usuario/screenshot.png",
  "cookies_count": 12,
  "cookies_file": "clientes/seu_usuario/cookies.json",
  "error": null
}
```

### GET /health
Health check simples.

## Rodando local (sem Docker)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium
uvicorn app.main:app --reload
```

## Docker (modo básico headless)

```bash
docker build -t pagbank-app .
docker run --rm -p 8000:8000 pagbank-app
```

## Docker + VNC/noVNC

```bash
docker compose up --build
```

Acessos:
- API: http://localhost:8000
- noVNC: http://localhost:7900  (senha padrão: `vncpass` se não alterar)

## Script externo (inicia.py)

Você pode chamar:
```bash
python scripts/inicia.py <usuario> <senha> --host http://localhost:8000
```

## Fluxo de Login (Resumo)
1. Abre https://www.pagbank.com.br
2. Fecha banner de consentimento se presente
3. Tenta clicar "Entrar" por:
   - Texto exato / locator de texto
   - get_by_text
   - link com `href` coerente
4. Localiza campo de usuário (label, role, placeholder ou heurística fallback)
5. Digita usuário (atraso simulando humano)
6. Clica "Continuar" ou aperta Enter
7. Localiza campos de senha (inputs fracionados ou único input password)
8. Digita senha
9. Submete (botão Entrar ou Enter)
10. Aguarda pós-login, coleta cookies e captura screenshot
11. Salva em `clientes/<username>/`
12. Retorna JSON

## Variáveis (.env)

Copie `.env.example` para `.env` e ajuste se necessário.

## Segurança

- Não comitar `.env` real
- Armazenar cookies com cuidado
- Possível adicionar criptografia se for produção

## Roadmap

- [ ] Adicionar retries com backoff
- [ ] Logs estruturados (JSON)
- [ ] WebSocket streaming de eventos
- [ ] Suporte a múltiplos navegadores
- [ ] Persistir sessão (context reuse)

## Licença

Defina uma licença (ex: MIT).