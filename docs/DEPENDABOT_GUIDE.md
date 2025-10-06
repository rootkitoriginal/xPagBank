# 🤖 Guia do Dependabot

## O que é o Dependabot?

O Dependabot é uma ferramenta integrada ao GitHub que mantém suas dependências atualizadas automaticamente. Ele:
- 🔍 Verifica vulnerabilidades de segurança
- 📦 Cria Pull Requests para atualizar dependências
- 🛡️ Protege seu projeto contra falhas de segurança
- ⏰ Executa verificações semanalmente

## Configuração

O arquivo `.github/dependabot.yml` configura como o Dependabot funciona:

### 📅 Agendamento
- **Frequência**: Toda segunda-feira às 09:00 (horário de São Paulo)
- **Limite de PRs**: Até 10 PRs de dependências Python e 5 de GitHub Actions

### 📦 Ecossistemas Monitorados

#### 1. **Python (pip)**
Monitora `requirements.txt` e `requirements-dev.txt`:
- Dependências do FastAPI (fastapi, uvicorn, pydantic)
- Ferramentas de desenvolvimento (pytest, black, flake8, isort)
- Bibliotecas de segurança (cryptography, python-jose, passlib)

#### 2. **GitHub Actions**
Monitora `.github/workflows/*.yml`:
- Ações do CI/CD
- Runners e ferramentas de automação

### 🏷️ Labels Aplicadas
Cada PR criado recebe labels:
- `dependencies` - Indica atualização de dependência
- `python` ou `github-actions` - Indica o ecossistema
- `security` - Para atualizações de segurança (Python)

### 📝 Formato de Commits
- **Python**: `chore(deps): update <package>`
- **GitHub Actions**: `chore(ci): update <action>`

### 👤 Atribuição
- PRs são automaticamente atribuídos ao usuário `rootkitoriginal`

## Grupos de Dependências

O Dependabot agrupa atualizações relacionadas em um único PR:

### 🚀 FastAPI Dependencies
```yaml
- fastapi
- uvicorn
- pydantic
- pydantic-settings
```

### 🛠️ Dev Dependencies
```yaml
- pytest
- black
- flake8
- isort
- mypy
- pre-commit
```

### 🔒 Security Dependencies
```yaml
- cryptography
- python-jose
- passlib
```

## Como Funciona?

### 1️⃣ Verificação Semanal
Toda segunda-feira às 09h, o Dependabot:
1. Verifica todas as dependências
2. Compara com as versões mais recentes
3. Identifica vulnerabilidades de segurança

### 2️⃣ Criação de PRs
Para cada atualização necessária:
1. Cria um branch `dependabot/<ecosystem>/<package>-<version>`
2. Atualiza o arquivo de dependências
3. Cria um PR com descrição detalhada
4. Aplica labels e atribui ao responsável

### 3️⃣ Revisão e Merge
Você deve:
1. Revisar o PR criado
2. Verificar os testes no CI/CD
3. Fazer merge se tudo estiver OK
4. Fechar o PR se não quiser a atualização

## Alertas de Segurança

### 🚨 Vulnerabilidades Detectadas
O GitHub detectou **6 vulnerabilidades** no projeto:
- 2 críticas
- 2 altas
- 2 moderadas

### Onde Ver os Alertas
1. Acesse: https://github.com/rootkitoriginal/xPagBank/security/dependabot
2. Clique em "Dependabot alerts"
3. Revise cada alerta
4. Aceite os PRs de correção ou atualize manualmente

### Priorização
1. **Críticas**: Merge imediato (exploração remota)
2. **Altas**: Merge em 24-48h (dados sensíveis)
3. **Moderadas**: Merge na próxima sprint (impacto limitado)
4. **Baixas**: Avaliar custo-benefício

## Comandos do Dependabot

Você pode controlar o Dependabot via comentários nos PRs:

### Comandos Básicos
```
@dependabot rebase
```
Rebase o PR com a branch master

```
@dependabot recreate
```
Recria o PR do zero

```
@dependabot merge
```
Faz merge do PR (se os testes passarem)

```
@dependabot squash and merge
```
Faz squash dos commits e merge

```
@dependabot cancel merge
```
Cancela um merge automático agendado

```
@dependabot close
```
Fecha o PR sem fazer merge

```
@dependabot ignore this dependency
```
Ignora atualizações futuras dessa dependência

```
@dependabot ignore this major version
```
Ignora apenas atualizações de major version

```
@dependabot ignore this minor version
```
Ignora apenas atualizações de minor version

## Boas Práticas

### ✅ Fazer
- ✅ Revisar PRs de segurança imediatamente
- ✅ Testar localmente antes do merge
- ✅ Ler o changelog das dependências
- ✅ Manter dependências agrupadas quando possível
- ✅ Configurar branch protection rules

### ❌ Evitar
- ❌ Ignorar alertas de segurança
- ❌ Fazer merge sem revisar
- ❌ Desabilitar o Dependabot
- ❌ Ignorar todas as atualizações
- ❌ Atualizar manualmente sem avisar o Dependabot

## Integração com CI/CD

O Dependabot funciona perfeitamente com o GitHub Actions:

1. **PR criado** → Triggers CI/CD workflow
2. **Testes executados** → pytest, black, flake8, isort
3. **Testes passaram** → ✅ Safe to merge
4. **Testes falharam** → ❌ Needs investigation

## Monitoramento

### Status do Dependabot
Verifique em: https://github.com/rootkitoriginal/xPagBank/network/updates

### Estatísticas
- Total de PRs abertos
- PRs merged
- Vulnerabilidades corrigidas
- Tempo médio de merge

## Troubleshooting

### PRs não estão sendo criados
1. Verifique o arquivo `.github/dependabot.yml`
2. Confirme que está na branch master
3. Verifique se atingiu o limite de PRs abertos
4. Veja logs em Settings → Dependabot

### Merge conflicts
```bash
# Rebase manualmente
git checkout dependabot/pip/package-version
git rebase origin/master
git push --force-with-lease
```

### Desabilitar temporariamente
Comente a seção no `.github/dependabot.yml`:
```yaml
# updates:
#   - package-ecosystem: "pip"
#     ...
```

## Recursos Adicionais

- 📚 [Documentação oficial](https://docs.github.com/en/code-security/dependabot)
- 🔧 [Configuration options](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/configuration-options-for-the-dependabot.yml-file)
- 🛡️ [Security advisories](https://github.com/advisories)
- 💬 [Dependabot commands](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/managing-pull-requests-for-dependency-updates#managing-dependabot-pull-requests-with-comment-commands)

---

**Configurado em**: 06/10/2025
**Última atualização**: 06/10/2025
**Status**: ✅ Ativo
