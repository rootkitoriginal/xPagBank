from __future__ import annotations

from typing import Optional

from playwright.async_api import (
    Browser,
    BrowserContext,
    Page,
    Playwright,
    async_playwright,
)


class PlaywrightService:
    """Pequeno helper para gerenciar o ciclo de vida do Playwright."""

    def __init__(self, *, headless: bool = True, timeout_ms: int = 30_000) -> None:
        self.headless = headless
        self.timeout_ms = timeout_ms
        self._playwright: Optional[Playwright] = None
        self._browser: Optional[Browser] = None
        self._context: Optional[BrowserContext] = None

    async def __aenter__(self) -> "PlaywrightService":
        await self.start()
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:  # type: ignore[override]
        await self.stop()

    async def start(self) -> None:
        if self._playwright:
            return
        playwright = await async_playwright().start()
        browser = await playwright.chromium.launch(headless=self.headless)
        context = await browser.new_context()
        context.set_default_timeout(self.timeout_ms)
        context.set_default_navigation_timeout(self.timeout_ms)

        self._playwright = playwright
        self._browser = browser
        self._context = context

    async def stop(self) -> None:
        if self._context:
            await self._context.close()
            self._context = None
        if self._browser:
            await self._browser.close()
            self._browser = None
        if self._playwright:
            await self._playwright.stop()
            self._playwright = None

    @property
    def context(self) -> BrowserContext:
        if not self._context:
            raise RuntimeError("O contexto do navegador ainda não foi inicializado.")
        return self._context

    async def new_page(self) -> Page:
        return await self.context.new_page()

    async def reset_context(self) -> None:
        """Reinicia o contexto do navegador (útil para fluxos com múltiplas tentativas)."""
        browser = self._browser
        if not browser:
            raise RuntimeError("O navegador ainda não foi inicializado.")
        if self._context:
            await self._context.close()
        context = await browser.new_context()
        context.set_default_timeout(self.timeout_ms)
        context.set_default_navigation_timeout(self.timeout_ms)
        self._context = context

    async def get_page(self) -> Page:
        """Atalho para reutilizar uma única page por tentativa."""
        if self.context.pages:
            return self.context.pages[0]
        return await self.new_page()
