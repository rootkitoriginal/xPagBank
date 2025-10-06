#!/bin/bash

echo "=========================================="
echo "Testando endpoint /api/v1/acesso"
echo "=========================================="
echo ""

# Teste 1: CPF válido
echo "🧪 Teste 1: CPF válido (123.456.789-09)"
curl -X POST http://localhost:8000/api/v1/acesso \
  -H 'Content-Type: application/json' \
  -d '{"username": "123.456.789-09"}' \
  -s | python3 -m json.tool
echo ""
echo ""

# Teste 2: CNPJ válido
echo "🧪 Teste 2: CNPJ válido (15.053.434/0001-27)"
curl -X POST http://localhost:8000/api/v1/acesso \
  -H 'Content-Type: application/json' \
  -d '{"username": "15.053.434/0001-27"}' \
  -s | python3 -m json.tool
echo ""
echo ""

# Teste 3: Email válido
echo "🧪 Teste 3: Email válido (usuario@exemplo.com)"
curl -X POST http://localhost:8000/api/v1/acesso \
  -H 'Content-Type: application/json' \
  -d '{"username": "usuario@exemplo.com"}' \
  -s | python3 -m json.tool
echo ""
echo ""

# Teste 4: Username inválido
echo "🧪 Teste 4: Username inválido (texto-invalido)"
curl -X POST http://localhost:8000/api/v1/acesso \
  -H 'Content-Type: application/json' \
  -d '{"username": "texto-invalido"}' \
  -s | python3 -m json.tool
echo ""
echo ""

# Teste 5: CPF inválido
echo "🧪 Teste 5: CPF inválido (111.111.111-11)"
curl -X POST http://localhost:8000/api/v1/acesso \
  -H 'Content-Type: application/json' \
  -d '{"username": "111.111.111-11"}' \
  -s | python3 -m json.tool
echo ""
echo ""

echo "=========================================="
echo "Testes concluídos!"
echo "=========================================="
