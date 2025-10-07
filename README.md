# PagBank Login Automation (FastAPI + Playwright + VNC opcional)

Este projeto implementa uma solução completa para automação de login no PagBank:

## Funcionalidades

- ✅ **API REST FastAPI** - Endpoint `/login` para automação de login
- ✅ **Automação Robusta** - Playwright com múltiplas estratégias de fallback para seletores
- ✅ **Persistência** - Salvamento automático de cookies e screenshot em `clientes/<username>/`
- ✅ **Docker Support** - Execução containerizada com ou sem interface gráfica
- ✅ **VNC/noVNC** - Visualização e interação com o navegador em tempo real
- ✅ **Script Cliente** - `inicia.py` para facilitar chamadas à API
- ✅ **Health Check** - Endpoint `/health` para monitoramento
- ✅ **Configurável** - Variáveis de ambiente para personalização
- ✅ **Tratamento de Erros** - Captura e retorno de erros amigáveis

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

## Estrutura do Projeto

```
xPagBank/
├── app/
│   ├── api/              # Rotas da API
│   ├── automation/       # Lógica de automação Playwright
│   ├── core/            # Configurações centrais
│   ├── models/          # Modelos Pydantic
│   ├── services/        # Serviços (Playwright)
│   └── utils/           # Utilitários (filesystem, etc)
├── scripts/
│   └── inicia.py        # Script cliente para chamar a API
├── clientes/            # Diretório para cookies e screenshots
├── .env.example         # Exemplo de variáveis de ambiente
├── Dockerfile           # Container com VNC/noVNC
├── docker-compose.yml   # Orquestração dos serviços
└── requirements.txt     # Dependências Python
```

## Segurança

- **Não comitar `.env` real** - Mantenha suas credenciais fora do controle de versão
- **Armazenar cookies com cuidado** - Os cookies salvos podem conter tokens de sessão
- **Ambiente de produção** - Considere adicionar criptografia para cookies
- **VNC** - Altere a senha padrão do VNC (`VNC_PASSWORD` no `.env`)
- **Validação** - A API valida entrada com Pydantic
- **Rate limiting** - Planejado para evitar abuso

## Roadmap

### Em Desenvolvimento
- [ ] Adicionar arquivo LICENSE ao repositório (MIT)
- [ ] Configurar pipeline de CI/CD com GitHub Actions (testes, lint, build)
- [ ] Canal WebSocket para streaming de status dos passos da automação
- [ ] Melhorar tratamento de seletores dinâmicos com retry e backoff exponencial

### Planejado
- [ ] Integração com @microsoft/playwright-mcp (bridge Node.js)
- [ ] Logs estruturados (JSON)
- [ ] Suporte a múltiplos navegadores (Firefox, WebKit)
- [ ] Persistir sessão entre requests (context reuse)
- [ ] Testes unitários e de integração
- [ ] Métricas e observabilidade

## Contribuindo

Contribuições são bem-vindas! Por favor:
1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um Pull Request

## Licença

Este projeto será licenciado sob a licença MIT. O arquivo LICENSE será adicionado em breve.

Para mais detalhes sobre melhorias planejadas, consulte `.github/copilot-instructions.md`.