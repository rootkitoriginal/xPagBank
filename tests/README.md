# Tests - xPagBank API

Este diretório contém todos os testes da aplicação xPagBank API.

## 📁 Estrutura

```
tests/
├── __init__.py                 # Módulo Python
├── README.md                   # Este arquivo
├── test_health.py              # Testes do endpoint /health
├── test_usuario.py             # Testes do endpoint /usuario
├── test_validacao.py           # Testes de validação CPF/CNPJ/Email
└── test_api_acesso.sh          # Testes de integração do endpoint /acesso
```

## 🧪 Tipos de Testes

### Testes Unitários (Python)

#### test_validacao.py
Testa as funções de validação de documentos e email.

**Execução:**
```bash
cd tests/
python3 test_validacao.py
```

**O que testa:**
- ✅ Validação de CPF (válidos e inválidos)
- ✅ Validação de CNPJ (válidos e inválidos)
- ✅ Validação de Email (válidos e inválidos)
- ✅ Validação geral de username (CPF/CNPJ/Email)

#### test_health.py
Testes do endpoint de health check.

**Execução:**
```bash
pytest test_health.py -v
```

#### test_usuario.py
Testes do endpoint de usuário.

**Execução:**
```bash
pytest test_usuario.py -v
```

### Testes de Integração (Shell Script)

#### test_api_acesso.sh
Testa o endpoint `/api/v1/acesso` com diferentes cenários.

**Execução:**
```bash
cd tests/
./test_api_acesso.sh
```

**Pré-requisitos:**
- Servidor deve estar rodando em `http://localhost:8874`
- Comando `curl` instalado
- Python 3 com módulo `json.tool`

**O que testa:**
1. ✅ CPF válido (123.456.789-09)
2. ✅ CNPJ válido (15.053.434/0001-27)
3. ✅ Email válido (usuario@exemplo.com)
4. ❌ Username inválido (texto-invalido)
5. ❌ CPF inválido (111.111.111-11)

## 🚀 Execução Rápida

### Todos os testes unitários com pytest
```bash
cd /home/rootkit/Apps/xPagBank
pytest tests/ -v
```

### Teste específico
```bash
# Validação de documentos
python3 tests/test_validacao.py

# Teste de integração do endpoint /acesso
bash tests/test_api_acesso.sh
```

### Com cobertura
```bash
pytest tests/ --cov=app --cov-report=html
```

## 📝 Notas

- Os testes de integração requerem que o servidor esteja rodando
- Para iniciar o servidor: `python3 main.py` na raiz do projeto
- Testes unitários não requerem o servidor rodando
- Use `pytest -v` para saída verbose
- Use `pytest -s` para ver prints durante os testes

## ✨ Adicionar Novos Testes

1. Crie um arquivo `test_*.py` neste diretório
2. Use pytest para estruturar os testes
3. Documente o propósito do teste no início do arquivo
4. Atualize este README

## 🔍 Exemplo de Teste com Pytest

```python
import pytest
from app.controllers.acesso_controller import AcessoController

def test_validar_cpf_valido():
    """Testa validação de CPF válido"""
    assert AcessoController.validar_cpf("123.456.789-09") == True

def test_validar_cpf_invalido():
    """Testa validação de CPF inválido"""
    assert AcessoController.validar_cpf("111.111.111-11") == False
```
