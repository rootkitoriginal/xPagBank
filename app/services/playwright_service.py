"""
Playwright Browser Automation Service
Gerencia navegador headless para automação
"""
from typing import Any, Dict, Optional

from playwright.async_api import Browser, Page, Playwright, async_playwright


class PlaywrightService:
    """Serviço para automação com Playwright"""

    def __init__(
        self,
        headless: bool = True,
        timeout: float = 30000,  # 30 segundos
        viewport: Optional[Dict[str, int]] = None,
    ):
        """
        Inicializa o serviço Playwright

        Args:
            headless: Se True, roda sem interface gráfica
            timeout: Timeout padrão em milissegundos
            viewport: Tamanho da viewport {width, height}
        """
        self.headless = headless
        self.timeout = timeout
        self.viewport = viewport or {"width": 1920, "height": 1080}
        self.playwright: Optional[Playwright] = None
        self.browser: Optional[Browser] = None
        self.page: Optional[Page] = None

    async def start(self) -> None:
        """Inicia o navegador"""
        if self.playwright is None:
            self.playwright = await async_playwright().start()
            self.browser = await self.playwright.chromium.launch(headless=self.headless)

    async def new_page(self) -> Page:
        """
        Cria uma nova página/aba

        Returns:
            Page instance
        """
        if self.browser is None:
            await self.start()

        self.page = await self.browser.new_page(viewport=self.viewport)
        self.page.set_default_timeout(self.timeout)
        return self.page

    async def goto(self, url: str, wait_until: str = "networkidle") -> None:
        """
        Navega para uma URL

        Args:
            url: URL de destino
            wait_until: Quando considerar carregamento completo
                       (load, domcontentloaded, networkidle)
        """
        if self.page is None:
            await self.new_page()

        await self.page.goto(url, wait_until=wait_until)

    async def fill_input(self, selector: str, value: str, delay: int = 100) -> None:
        """
        Preenche um campo de input

        Args:
            selector: Seletor CSS do campo
            value: Valor a preencher
            delay: Delay entre teclas em ms (simula digitação)
        """
        if self.page is None:
            raise RuntimeError("Page não inicializada")

        await self.page.wait_for_selector(selector, state="visible")
        await self.page.fill(selector, value)
        # Simula digitação mais natural se delay > 0
        if delay > 0:
            await self.page.type(selector, "", delay=delay)

    async def click(self, selector: str) -> None:
        """
        Clica em um elemento

        Args:
            selector: Seletor CSS do elemento
        """
        if self.page is None:
            raise RuntimeError("Page não inicializada")

        await self.page.wait_for_selector(selector, state="visible")
        await self.page.click(selector)

    async def wait_for_selector(
        self, selector: str, state: str = "visible", timeout: Optional[float] = None
    ) -> None:
        """
        Aguarda um seletor aparecer

        Args:
            selector: Seletor CSS
            state: Estado esperado (visible, hidden, attached, detached)
            timeout: Timeout em ms (usa padrão se None)
        """
        if self.page is None:
            raise RuntimeError("Page não inicializada")

        await self.page.wait_for_selector(selector, state=state, timeout=timeout or self.timeout)

    async def get_content(self) -> str:
        """
        Obtém HTML da página atual

        Returns:
            HTML content
        """
        if self.page is None:
            raise RuntimeError("Page não inicializada")

        return await self.page.content()

    async def get_cookies(self) -> list:
        """
        Obtém cookies da página atual

        Returns:
            Lista de cookies
        """
        if self.page is None:
            raise RuntimeError("Page não inicializada")

        return await self.page.context.cookies()

    async def screenshot(self, path: str, full_page: bool = False) -> bytes:
        """
        Tira screenshot da página

        Args:
            path: Caminho para salvar
            full_page: Se True, captura página inteira

        Returns:
            Bytes da imagem
        """
        if self.page is None:
            raise RuntimeError("Page não inicializada")

        return await self.page.screenshot(path=path, full_page=full_page)

    async def evaluate(self, script: str) -> Any:
        """
        Executa JavaScript na página

        Args:
            script: Código JavaScript

        Returns:
            Resultado da execução
        """
        if self.page is None:
            raise RuntimeError("Page não inicializada")

        return await self.page.evaluate(script)

    async def close_page(self) -> None:
        """Fecha a página atual"""
        if self.page is not None:
            await self.page.close()
            self.page = None

    async def close(self) -> None:
        """Fecha o navegador e limpa recursos"""
        if self.page is not None:
            await self.page.close()
            self.page = None

        if self.browser is not None:
            await self.browser.close()
            self.browser = None

        if self.playwright is not None:
            await self.playwright.stop()
            self.playwright = None

    async def __aenter__(self):
        """Context manager entry"""
        await self.start()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit"""
        await self.close()
