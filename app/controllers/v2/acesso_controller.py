"""
Controller v2 for authentication operations using Playwright
"""
from typing import Any, Dict

from app.schemas.acesso import AcessoRequest
from app.services.playwright_service import PlaywrightService
from app.utils.response_parser import ResponseParser
from app.utils.validators import Validators


class AcessoController:
    """Controller v2 using browser automation"""

    @staticmethod
    async def fazer_login(acesso_data: AcessoRequest) -> Dict[str, Any]:
        """
        Authenticate user via PagBank using browser automation

        Args:
            acesso_data: Login credentials (CPF, CNPJ ou Email)

        Returns:
            Dict com a resposta normalizada
        """
        # Valida o username usando Validators
        if not Validators.validar_username(acesso_data.username):
            return ResponseParser.validation_error(
                "Username inválido. Forneça um CPF, CNPJ ou Email válido."
            )

        browser = None
        try:
            # Inicializa o navegador (modo visível para debug)
            browser = PlaywrightService(headless=False, timeout=30000)
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
