#!/usr/bin/env python3
"""
Script de teste para validação de CPF, CNPJ e Email
"""
import sys

sys.path.insert(0, "/home/rootkit/Apps/xPagBank")

from app.controllers.acesso_controller import AcessoController  # noqa: E402

# Testes
print("=" * 60)
print("TESTE DE VALIDAÇÃO")
print("=" * 60)

# Testes de CPF
cpfs = [
    "123.456.789-00",  # Inválido
    "111.111.111-11",  # Inválido (todos iguais)
    "123.456.789-09",  # Válido (exemplo)
    "12345678909",  # Válido sem formatação
]

print("\n--- Testando CPFs ---")
for cpf in cpfs:
    valido = AcessoController.validar_cpf(cpf)
    print(f"CPF: {cpf:20} -> {'VÁLIDO' if valido else 'INVÁLIDO'}")

# Testes de CNPJ
cnpjs = [
    "15.053.434/0001-27",  # CNPJ do exemplo
    "11.111.111/1111-11",  # Inválido (todos iguais)
    "15053434000127",  # Mesmo CNPJ sem formatação
]

print("\n--- Testando CNPJs ---")
for cnpj in cnpjs:
    valido = AcessoController.validar_cnpj(cnpj)
    print(f"CNPJ: {cnpj:20} -> {'VÁLIDO' if valido else 'INVÁLIDO'}")

# Testes de Email
emails = [
    "usuario@exemplo.com",
    "invalido@",
    "teste.usuario@dominio.com.br",
    "semdominio",
]

print("\n--- Testando Emails ---")
for email in emails:
    valido = AcessoController.validar_email(email)
    print(f"Email: {email:30} -> {'VÁLIDO' if valido else 'INVÁLIDO'}")

# Teste da validação geral
usernames = [
    "123.456.789-09",
    "15.053.434/0001-27",
    "usuario@exemplo.com",
    "invalido",
]

print("\n--- Testando Username Geral ---")
for username in usernames:
    valido = AcessoController.validar_username(username)
    print(f"Username: {username:30} -> {'VÁLIDO' if valido else 'INVÁLIDO'}")

print("\n" + "=" * 60)
