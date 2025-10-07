"""
CLI client for testing PagBank login locally
"""
import asyncio
import sys
from app.models import AcessoRequest
from app.controllers import AcessoController


async def main():
    """Main CLI function"""
    if len(sys.argv) < 2:
        print("Uso: python -m app.cli <usuario> [senha]")
        print("\nExemplos:")
        print("  python -m app.cli usuario@email.com")
        print("  python -m app.cli 12345678900 senha123")
        sys.exit(1)
    
    username = sys.argv[1]
    password = sys.argv[2] if len(sys.argv) > 2 else None
    
    acesso_data = AcessoRequest(username=username, password=password)
    
    print(f"\n🔐 Testando login no PagBank")
    print(f"👤 Usuário: {username}")
    print("-" * 60)
    
    result = await AcessoController.fazer_login(acesso_data)
    
    print("\n📋 Resultado:")
    print("-" * 60)
    import json
    print(json.dumps(result, indent=2, ensure_ascii=False))
    print("-" * 60)


if __name__ == "__main__":
    asyncio.run(main())
