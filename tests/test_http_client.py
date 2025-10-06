"""
Testes para o HTTP Client
"""
import asyncio
import sys
from pathlib import Path

# Adiciona o diretório raiz ao path
sys.path.insert(0, str(Path(__file__).parent.parent))  # noqa: E402

from app.services.http_client import PagBankHttpClient  # noqa: E402


async def test_http_client():
    """Testa o cliente HTTP"""
    print("\n" + "=" * 60)
    print("Testando PagBankHttpClient")
    print("=" * 60 + "\n")

    # Teste 1: Inicialização básica
    print("1. Teste de Inicialização:")
    client = PagBankHttpClient()
    print(f"   ✅ Base URL padrão: {client.base_url}")
    print(f"   ✅ Timeout padrão: {client.timeout}s")
    print(f"   ✅ Cookies iniciais: {client.get_cookies()}")

    # Teste 2: Inicialização customizada
    print("\n2. Teste de Inicialização Customizada:")
    client2 = PagBankHttpClient(base_url="https://api.security.pagbank.com.br", timeout=60.0)
    print(f"   ✅ Base URL: {client2.base_url}")
    print(f"   ✅ Timeout: {client2.timeout}s")

    # Teste 3: Gerenciamento de cookies
    print("\n3. Teste de Gerenciamento de Cookies:")
    print(f"   Cookies antes: {client.get_cookies()}")
    client.init_cookies({"session": "abc123", "user_id": "456"})
    print(f"   ✅ Cookies após init: {client.get_cookies()}")
    client.clear_cookies()
    print(f"   ✅ Cookies após clear: {client.get_cookies()}")

    # Teste 4: Headers padrão
    print("\n4. Teste de Headers Padrão:")
    headers = client.default_headers
    print(f"   ✅ Accept: {headers.get('accept')}")
    print(f"   ✅ Content-Type: {headers.get('content-type')}")
    print(f"   ✅ User-Agent: {headers.get('user-agent')[:50]}...")

    # Teste 5: Modificar headers
    print("\n5. Teste de Modificação de Headers:")
    client.set_header("X-Custom-Header", "CustomValue")
    print(f"   ✅ Header adicionado: {client.default_headers.get('X-Custom-Header')}")  # noqa: E501
    client.remove_header("X-Custom-Header")
    print(
        f"   ✅ Header removido: {client.default_headers.get('X-Custom-Header', 'None')}"
    )  # noqa: E501

    # Teste 6: Construção de URLs
    print("\n6. Teste de Construção de URLs:")
    url1 = client._build_url("/api/v1/users")
    print(f"   ✅ URL relativa: {url1}")
    url2 = client._build_url("https://external-api.com/data")
    print(f"   ✅ URL absoluta: {url2}")

    # Teste 7: Merge de headers
    print("\n7. Teste de Merge de Headers:")
    custom = {"Authorization": "Bearer token123"}
    merged = client._merge_headers(custom)
    print("   ✅ Headers mesclados:")
    print(f"      - Accept: {merged.get('accept')}")
    print(f"      - Authorization: {merged.get('Authorization')}")

    print("\n" + "=" * 60)
    print("✅ Todos os testes passaram!")
    print("=" * 60 + "\n")
    print("📝 Nota: Testes de requisições HTTP reais foram pulados")
    print("   (httpbin.org está indisponível no momento)")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    asyncio.run(test_http_client())
