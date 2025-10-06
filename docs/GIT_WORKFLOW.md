# Git Workflow com GitHub CLI (gh)

Este documento descreve o fluxo de trabalho Git para o projeto xPagBank usando GitHub CLI.

## Pré-requisitos

Instalar GitHub CLI:
```bash
# Ubuntu/Debian
sudo apt install gh

# Verificar instalação
gh --version
```

## Autenticação

```bash
# Fazer login no GitHub
gh auth login

# Verificar autenticação
gh auth status
```

## Workflow Completo

### 1. Inicializar Repositório

```bash
# Se ainda não foi inicializado
git init

# Adicionar arquivos
git add .

# Primeiro commit
git commit -m "feat: estrutura inicial do projeto xPagBank API"

# Criar repositório no GitHub
gh repo create xPagBank --public --source=. --remote=origin --push
```

### 2. Desenvolvimento de Feature

```bash
# Criar e mudar para nova branch
git checkout -b feature/nome-da-feature

# Fazer alterações...
# Adicionar arquivos modificados
git add .

# Commit com mensagem descritiva
git commit -m "feat: adiciona nova funcionalidade X"

# Push para o GitHub
git push -u origin feature/nome-da-feature

# Criar Pull Request
gh pr create --title "Feature: Nome da Feature" \
  --body "Descrição detalhada da feature" \
  --label enhancement

# Ou interativamente
gh pr create
```

### 3. Revisar Pull Requests

```bash
# Listar PRs abertos
gh pr list

# Ver detalhes de um PR
gh pr view <número-do-pr>

# Checkout de um PR para revisar localmente
gh pr checkout <número-do-pr>

# Adicionar comentário ao PR
gh pr comment <número-do-pr> --body "Comentário de revisão"

# Aprovar PR
gh pr review <número-do-pr> --approve

# Solicitar mudanças
gh pr review <número-do-pr> --request-changes --body "Sugestões de mudança"
```

### 4. Merge de Pull Request

```bash
# Merge via CLI
gh pr merge <número-do-pr> --merge

# Ou com squash
gh pr merge <número-do-pr> --squash

# Ou com rebase
gh pr merge <número-do-pr> --rebase

# Deletar branch após merge
git branch -d feature/nome-da-feature
git push origin --delete feature/nome-da-feature
```

### 5. Hotfix (Correção Urgente)

```bash
# Criar branch de hotfix a partir da main
git checkout main
git pull origin main
git checkout -b hotfix/descricao-bug

# Fazer correção...
git add .
git commit -m "fix: corrige bug crítico X"

# Push e criar PR urgente
git push -u origin hotfix/descricao-bug
gh pr create --title "Hotfix: Bug Crítico" \
  --body "Correção urgente de bug em produção" \
  --label bug,priority-high

# Merge rápido após revisão
gh pr merge <número-do-pr> --merge
```

### 6. Release

```bash
# Criar tag de versão
git tag -a v1.0.0 -m "Release v1.0.0"

# Push da tag
git push origin v1.0.0

# Criar release no GitHub
gh release create v1.0.0 \
  --title "Release v1.0.0" \
  --notes "Descrição das mudanças nesta versão"
```

## Comandos Úteis

```bash
# Ver status do repositório
gh repo view

# Clonar repositório
gh repo clone usuario/xPagBank

# Ver issues
gh issue list

# Criar issue
gh issue create --title "Bug: Descrição" --body "Detalhes do bug"

# Fechar issue
gh issue close <número-da-issue>

# Ver workflows (CI/CD)
gh workflow list

# Ver execuções do workflow
gh run list

# Ver logs de um workflow
gh run view <run-id> --log
```

## Convenção de Commits

Use mensagens de commit descritivas seguindo o padrão:

- `feat:` Nova funcionalidade
- `fix:` Correção de bug
- `docs:` Alterações na documentação
- `style:` Formatação, ponto e vírgula faltando, etc
- `refactor:` Refatoração de código
- `test:` Adição ou correção de testes
- `chore:` Tarefas de manutenção

Exemplos:
```bash
git commit -m "feat: adiciona endpoint de consulta de saldo"
git commit -m "fix: corrige validação de CPF no cadastro"
git commit -m "docs: atualiza README com instruções de deploy"
```

## Boas Práticas

1. **Sempre trabalhe em branches separadas**
   - Nunca commit direto na `main`
   - Use nomes descritivos para branches

2. **Faça commits pequenos e frequentes**
   - Commits menores são mais fáceis de revisar
   - Facilita o rollback se necessário

3. **Escreva mensagens de commit claras**
   - Use o padrão de convenção
   - Descreva o "o quê" e "por quê"

4. **Sempre faça pull antes de push**
   ```bash
   git pull origin main
   git push origin feature/minha-feature
   ```

5. **Use Pull Requests para todas as mudanças**
   - Facilita code review
   - Mantém histórico organizado

6. **Mantenha a branch main sempre estável**
   - Só merge código testado
   - Use CI/CD para validação automática

## Troubleshooting

### Conflito de merge
```bash
# Atualizar sua branch com a main
git checkout feature/minha-feature
git pull origin main

# Resolver conflitos manualmente
# Após resolver:
git add .
git commit -m "fix: resolve conflitos de merge"
git push origin feature/minha-feature
```

### Desfazer último commit (local)
```bash
# Manter mudanças
git reset --soft HEAD~1

# Descartar mudanças
git reset --hard HEAD~1
```

### Reverter commit (já no remote)
```bash
git revert <commit-hash>
git push origin main
```
