import re
from typing import Any, Dict

from app.schemas.acesso import AcessoRequest
from app.services.http_client import PagBankHttpClient


class AcessoController:
    """Controller for authentication operations"""

    @staticmethod
    def validar_cpf(cpf: str) -> bool:
        """
        Valida um CPF brasileiro

        Args:
            cpf: CPF com ou sem formatação

        Returns:
            True se válido, False caso contrário
        """
        # Remove caracteres não numéricos
        cpf = re.sub(r"\D", "", cpf)

        # Verifica se tem 11 dígitos
        if len(cpf) != 11:
            return False

        # Verifica se todos os dígitos são iguais
        if cpf == cpf[0] * 11:
            return False

        # Valida primeiro dígito verificador
        soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
        digito1 = (soma * 10 % 11) % 10

        if int(cpf[9]) != digito1:
            return False

        # Valida segundo dígito verificador
        soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
        digito2 = (soma * 10 % 11) % 10

        return int(cpf[10]) == digito2

    @staticmethod
    def validar_cnpj(cnpj: str) -> bool:
        """
        Valida um CNPJ brasileiro

        Args:
            cnpj: CNPJ com ou sem formatação

        Returns:
            True se válido, False caso contrário
        """
        # Remove caracteres não numéricos
        cnpj = re.sub(r"\D", "", cnpj)

        # Verifica se tem 14 dígitos
        if len(cnpj) != 14:
            return False

        # Verifica se todos os dígitos são iguais
        if cnpj == cnpj[0] * 14:
            return False

        # Valida primeiro dígito verificador
        multiplicadores1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        soma = sum(int(cnpj[i]) * multiplicadores1[i] for i in range(12))
        digito1 = 11 - (soma % 11)
        digito1 = 0 if digito1 > 9 else digito1

        if int(cnpj[12]) != digito1:
            return False

        # Valida segundo dígito verificador
        multiplicadores2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        soma = sum(int(cnpj[i]) * multiplicadores2[i] for i in range(13))
        digito2 = 11 - (soma % 11)
        digito2 = 0 if digito2 > 9 else digito2

        return int(cnpj[13]) == digito2

    @staticmethod
    def validar_email(email: str) -> bool:
        """
        Valida um endereço de email

        Args:
            email: Email a ser validado

        Returns:
            True se válido, False caso contrário
        """
        padrao = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return bool(re.match(padrao, email))

    @staticmethod
    def validar_username(username: str) -> bool:
        """
        Valida se o username é CPF, CNPJ ou Email válido

        Args:
            username: CPF, CNPJ ou Email

        Returns:
            True se válido, False caso contrário
        """
        # Remove espaços em branco
        username = username.strip()

        # Verifica se é email
        if "@" in username:
            return AcessoController.validar_email(username)

        # Remove caracteres não numéricos para testar CPF/CNPJ
        apenas_numeros = re.sub(r"\D", "", username)

        # Verifica se é CPF (11 dígitos)
        if len(apenas_numeros) == 11:
            return AcessoController.validar_cpf(username)

        # Verifica se é CNPJ (14 dígitos)
        if len(apenas_numeros) == 14:
            return AcessoController.validar_cnpj(username)

        return False

    @staticmethod
    async def fazer_login(acesso_data: AcessoRequest) -> Dict[str, Any]:
        """
        Authenticate user via PagBank API

        Args:
            acesso_data: Login credentials (CPF, CNPJ ou Email)

        Returns:
            Dict com a resposta da API ou erro
        """
        # Valida o username
        if not AcessoController.validar_username(acesso_data.username):
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
