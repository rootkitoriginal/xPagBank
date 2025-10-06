"""
Controller v2 for authentication operations using Playwright
"""
import re
from typing import Any, Dict

from app.schemas.acesso import AcessoRequest
from app.services.playwright_service import PlaywrightService
from app.utils.response_parser import ResponseParser


class AcessoController:
    """Controller v2 using browser automation"""

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
        Authenticate user via PagBank using browser automation

        Args:
            acesso_data: Login credentials (CPF, CNPJ ou Email)

        Returns:
            Dict com a resposta normalizada
        """
        # Valida o username
        if not AcessoController.validar_username(acesso_data.username):
            return ResponseParser.validation_error(
                "Username inválido. Forneça um CPF, CNPJ ou Email válido."
            )

        browser = None
        try:
            # Inicializa o navegador
            browser = PlaywrightService(headless=True, timeout=30000)
            await browser.start()

            print("\n" + "=" * 60)
            print("V2: Iniciando automação do navegador...")
            print("=" * 60)

            # PASSO 1: Acessa a página de login
            print("\nPASSO 1: Acessando página de login...")
            await browser.goto("https://acesso.pagbank.com.br/")
            print("✅ Página carregada")

            # PASSO 2: Aguarda e preenche o campo de username
            print("\nPASSO 2: Preenchendo username...")
            username_selector = 'input[name="username"]'

            try:
                await browser.wait_for_selector(username_selector, timeout=10000)
                await browser.fill_input(username_selector, acesso_data.username, delay=50)
                print(f"✅ Username preenchido: {acesso_data.username}")
            except Exception as e:
                print(f"⚠️  Erro ao preencher username: {str(e)}")
                # Tenta seletores alternativos
                alt_selectors = [
                    'input[type="text"]',
                    'input[placeholder*="CPF"]',
                    'input[placeholder*="Email"]',
                    "#username",
                ]
                for selector in alt_selectors:
                    try:
                        await browser.wait_for_selector(selector, timeout=5000)
                        await browser.fill_input(selector, acesso_data.username, delay=50)
                        print(f"✅ Username preenchido com seletor: {selector}")
                        break
                    except Exception:
                        continue

            # PASSO 3: Aguarda resposta/redirecionamento
            print("\nPASSO 3: Aguardando resposta...")
            await browser.page.wait_for_timeout(2000)  # Aguarda 2 segundos

            # PASSO 4: Captura estado da página
            print("\nPASSO 4: Capturando estado da página...")
            current_url = browser.page.url
            page_content = await browser.get_content()
            cookies = await browser.get_cookies()

            print(f"URL atual: {current_url}")
            print(f"Cookies: {len(cookies)} encontrados")

            # Verifica se há mensagens de erro ou sucesso
            has_error = "erro" in page_content.lower() or "error" in page_content.lower()
            has_password_field = (
                "password" in page_content.lower() or "senha" in page_content.lower()
            )

            print("=" * 60 + "\n")

            # Determina o resultado
            if has_error:
                return ResponseParser.normalize_response(
                    success=False,
                    message="Erro detectado na página",
                    data={
                        "url": current_url,
                        "cookies_count": len(cookies),
                        "error_detected": True,
                    },
                    source="browser",
                )
            elif has_password_field:
                return ResponseParser.normalize_response(
                    success=True,
                    message="Username validado. Campo de senha disponível.",
                    data={
                        "url": current_url,
                        "cookies_count": len(cookies),
                        "next_step": "password",
                        "cookies": {c["name"]: c["value"] for c in cookies},
                    },
                    source="browser",
                )
            else:
                return ResponseParser.normalize_response(
                    success=True,
                    message="Página carregada com sucesso",
                    data={
                        "url": current_url,
                        "cookies_count": len(cookies),
                        "content_length": len(page_content),
                    },
                    source="browser",
                )

        except Exception as e:
            error_type = type(e).__name__
            if "timeout" in error_type.lower() or "timeout" in str(e).lower():
                return ResponseParser.timeout_error(source="browser")
            return ResponseParser.generic_error(e, source="browser")

        finally:
            # Fecha o navegador
            if browser is not None:
                await browser.close()
                print("🔒 Navegador fechado\n")
