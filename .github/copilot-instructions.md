# xPagBank - Lista de Tarefas e Melhorias

## Funcionalidades Implementadas ✅
- [x] API FastAPI para automação de login no PagBank
- [x] Automação com Playwright Python e múltiplas estratégias de fallback
- [x] Salvamento de cookies e screenshots em `clientes/<username>/`
- [x] Suporte a Docker (headless e com VNC/noVNC)
- [x] Script externo `inicia.py` para chamada da API
- [x] Endpoint `/health` para health check
- [x] Configuração via variáveis de ambiente (.env)
- [x] Tratamento de banners de cookies e seletores dinâmicos

## Melhorias e Features Pendentes 🚧

### Alta Prioridade
- [x] Adicionar arquivo LICENSE ao repositório (ex: MIT)
- [x] Configurar pipeline de CI/CD com GitHub Actions
  - [x] Workflow de testes automatizados
  - [x] Workflow de lint (ruff, black, mypy)
  - [x] Workflow de build e validação Docker
  - [ ] Workflow de deploy (opcional)

### Média Prioridade
- [ ] Adicionar canal WebSocket para streaming de status dos passos da automação
  - [ ] Endpoint WebSocket `/ws/login/{session_id}`
  - [ ] Emitir eventos durante o fluxo (navegação, preenchimento, submit, etc)
  - [ ] Atualizar cliente `inicia.py` para suportar WebSocket (opcional)
- [ ] Melhorar tratamento de seletores dinâmicos no fluxo de login
  - [ ] Adicionar sistema de retry com backoff exponencial
  - [ ] Implementar detecção inteligente de mudanças no DOM
  - [ ] Adicionar fallbacks adicionais para elementos críticos

### Baixa Prioridade (Future)
- [ ] Integrar com @microsoft/playwright-mcp (bridge Node) para usar MCP em vez da biblioteca Playwright Python
  - [ ] Avaliar viabilidade e benefícios da migração
  - [ ] Criar bridge Node.js se necessário
  - [ ] Manter compatibilidade com implementação atual
- [ ] Adicionar logs estruturados em JSON
- [ ] Suporte a múltiplos navegadores (Firefox, WebKit)
- [ ] Persistir sessão entre requests (context reuse)
- [ ] Sistema de cache de sessões
- [ ] Adicionar criptografia para cookies em produção
- [ ] Implementar rate limiting e proteção contra abuse
- [ ] Adicionar testes unitários e de integração
- [ ] Documentação API com Swagger/OpenAPI melhorada
- [ ] Métricas e observabilidade (Prometheus/Grafana)

## Notas Técnicas
- O projeto usa Playwright Python (versão 1.46.0)
- FastAPI com uvicorn como servidor ASGI
- Docker com suporte VNC para debugging visual
- Seletores com múltiplas estratégias de fallback já implementados
