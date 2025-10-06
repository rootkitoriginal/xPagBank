# Setup Guide - Pre-commit Hooks

## Instalação e Configuração do Pre-commit

Pre-commit é uma ferramenta que executa verificações automáticas antes de cada commit, garantindo qualidade de código.

### 1. Instalar dependências

```bash
pip install -r requirements-dev.txt
```

### 2. Instalar os hooks do pre-commit

```bash
pre-commit install
```

Isso irá configurar os git hooks automaticamente.

### 3. Executar manualmente (opcional)

Para testar os hooks sem fazer commit:

```bash
# Executar em todos os arquivos
pre-commit run --all-files

# Executar em arquivos específicos
pre-commit run --files app/schemas/usuario.py
```

### 4. Atualizar hooks

```bash
pre-commit autoupdate
```

## O que os hooks fazem

### 1. **Black** - Formatação automática
- Formata código Python automaticamente
- Linha máxima: 100 caracteres
- Estilo consistente em todo projeto

### 2. **Flake8** - Linting
- Verifica erros de sintaxe
- Detecta código não utilizado
- Verifica complexidade de código
- Identifica problemas de estilo

### 3. **isort** - Organização de imports
- Organiza imports alfabeticamente
- Agrupa imports por categoria
- Remove imports duplicados

### 4. **mypy** - Type checking
- Verifica tipos estáticos
- Detecta erros de tipo antes da execução
- Melhora documentação do código

### 5. **Pre-commit hooks básicos**
- Remove espaços em branco no final das linhas
- Adiciona newline no final dos arquivos
- Verifica sintaxe de YAML e JSON
- Detecta conflitos de merge
- Previne commits de arquivos grandes

## Workflow com Pre-commit

```bash
# 1. Fazer mudanças no código
vim app/schemas/usuario.py

# 2. Adicionar ao staging
git add app/schemas/usuario.py

# 3. Tentar fazer commit
git commit -m "feat: adiciona validação de CPF"

# Os hooks serão executados automaticamente:
# ✓ black................Passed
# ✓ flake8...............Passed
# ✓ isort................Passed
# ✓ mypy.................Passed

# 4. Se algum hook falhar, corrija e tente novamente
```

## Configuração no arquivo .pre-commit-config.yaml

O arquivo está em: `.pre-commit-config.yaml`

Para desabilitar um hook temporariamente:

```bash
SKIP=black git commit -m "mensagem"
```

Para ignorar todos os hooks (NÃO RECOMENDADO):

```bash
git commit --no-verify -m "mensagem"
```

## Integração com CI/CD

Os mesmos checks rodam no GitHub Actions:
- Veja `.github/workflows/ci-cd.yml`
- Executado automaticamente em PRs
- Previne merge de código com problemas

## Comandos úteis

```bash
# Ver configuração atual
pre-commit sample-config

# Limpar cache
pre-commit clean

# Desinstalar hooks
pre-commit uninstall

# Reinstalar hooks
pre-commit install
```

## Personalização

Edite `.pre-commit-config.yaml` para:
- Adicionar/remover hooks
- Alterar argumentos
- Mudar versões das ferramentas

## Dicas

1. **Execute localmente antes de push**
   ```bash
   pre-commit run --all-files
   ```

2. **Configure seu editor** para usar black e isort automaticamente

3. **Documente exceções** quando usar `# noqa` ou `# type: ignore`

4. **Mantenha atualizado**
   ```bash
   pre-commit autoupdate
   ```

## Troubleshooting

### Hook está falhando mas o código está correto?

```bash
# Limpar cache
pre-commit clean
pre-commit install --install-hooks
```

### Erro de versão do Python?

```bash
# Usar versão específica
pre-commit run --hook-stage manual --all-files
```

### Hook muito lento?

```bash
# Desabilitar temporariamente
SKIP=mypy git commit -m "mensagem"
```
