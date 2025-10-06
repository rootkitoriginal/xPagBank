from typing import Any, Dict

from app.schemas.acesso import AcessoRequest
from app.services.http_client import PagBankHttpClient
from app.utils.validators import Validators


class AcessoController:
    """Controller for authentication operations"""

    @staticmethod
    async def fazer_login(acesso_data: AcessoRequest) -> Dict[str, Any]:
        """
        Authenticate user via PagBank API

        Args:
            acesso_data: Login credentials (CPF, CNPJ ou Email)

        Returns:
            Dict com a resposta da API ou erro
        """
        # Valida o username usando Validators
        if not Validators.validar_username(acesso_data.username):
            return {
                "success": False,
                "message": "Username inválido. Forneça um CPF, CNPJ ou Email válido.",
                "data": None,
            }

        # Inicializa o cliente HTTP
        client = PagBankHttpClient(
            base_url="https://acesso.pagbank.com.br",
            timeout=30.0,
        )

        try:
            # PASSO 1: Acessa a página de login para obter cookies de sessão
            print("\n" + "=" * 60)
            print("PASSO 1: Obtendo cookies de sessão...")
            print("=" * 60)

            initial_headers = {
                "accept": (
                    "text/html,application/xhtml+xml,application/xml;q=0.9,"
                    "image/avif,image/webp,image/apng,*/*;q=0.8,"
                    "application/signed-exchange;v=b3;q=0.7"
                ),
                "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
                "cache-control": "max-age=0",
                "referer": "https://pagbank.com.br/",
                "sec-ch-ua": (
                    '"Google Chrome";v="141", "Not?A_Brand";v="8", ' '"Chromium";v="141"'
                ),
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"Linux"',
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "same-origin",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requests": "1",
            }

            # Acessa a página inicial para obter cookies
            initial_response = await client.get(
                path="/",
                headers=initial_headers,
                use_cookies=True,
            )

            print(f"Status: {initial_response.status_code}")
            print(f"Cookies obtidos: {len(client.get_cookies())} cookies")
            for cookie_name in client.get_cookies().keys():
                print(f"  - {cookie_name}")
            print("=" * 60 + "\n")

            # PASSO 2: Faz a requisição para a API usando os cookies
            print("=" * 60)
            print("PASSO 2: Validando username na API...")
            print("=" * 60)

            # Muda a base URL para a API
            client.base_url = "https://api.security.pagbank.com.br"

            # Headers customizados para a API
            api_headers = {
                "origin": "https://acesso.pagbank.com.br",
                "referer": "https://acesso.pagbank.com.br/",
                "x-user-type": "primary",
            }

            payload = {"username": acesso_data.username}

            response = await client.post(
                path="/usernames",
                json=payload,
                headers=api_headers,
                use_cookies=True,  # Reutiliza os cookies obtidos no passo 1
            )

            print(f"Status Code: {response.status_code}")
            print("=" * 60)
            print("Response Headers:")
            for key, value in response.headers.items():
                print(f"  {key}: {value}")
            print("=" * 60)
            print("Response Body:")
            body = response.text
            print(body[:500] if len(body) > 500 else body)
            print("=" * 60)
            print("Cookies finais:")
            print(client.get_cookies())
            print("=" * 60 + "\n")

            # Verifica se é bloqueio do Cloudflare
            is_cloudflare_block = response.status_code == 403 and (
                "cloudflare" in response.text.lower()
                or "cf-ray" in response.headers.get("server", "").lower()
                or response.headers.get("server", "").lower() == "cloudflare"
            )

            if is_cloudflare_block:
                msg = (
                    "Bloqueado pelo Cloudflare. A API do PagBank "
                    "está protegida e requer autenticação adicional."
                )
                detail = (
                    "A requisição foi bloqueada pelo sistema de " "proteção Cloudflare do PagBank"
                )
                return {
                    "success": False,
                    "status_code": response.status_code,
                    "message": msg,
                    "data": {
                        "error": "cloudflare_protection",
                        "detail": detail,
                    },
                }

            # Tenta parsear o JSON
            try:
                response_data = response.json()
            except Exception:
                response_data = {"raw": response.text}

            success = response.status_code == 200
            msg = "Requisição realizada com sucesso" if success else "Erro na requisição"
            return {
                "success": success,
                "status_code": response.status_code,
                "message": msg,
                "data": response_data,
                "cookies": client.get_cookies(),  # Retorna cookies para reutilização
            }

        except Exception as e:
            error_type = type(e).__name__
            if "timeout" in error_type.lower() or "timeout" in str(e).lower():
                return {
                    "success": False,
                    "message": "Timeout ao conectar com a API do PagBank",
                    "data": None,
                }
            return {
                "success": False,
                "message": f"Erro ao fazer requisição: {str(e)}",
                "data": None,
            }
