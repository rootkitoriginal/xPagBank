"""
Playwright service for browser automation
"""
from playwright.async_api import async_playwright, Browser, BrowserContext, Page
from typing import Optional, List, Dict, Any


class PlaywrightService:
    """Service for browser automation using Playwright"""

    def __init__(self, headless: bool = False, timeout: int = 30000):
        """
        Initialize PlaywrightService
        
        Args:
            headless: Whether to run browser in headless mode
            timeout: Default timeout in milliseconds
        """
        self.headless = headless
        self.timeout = timeout
        self.playwright = None
        self.browser: Optional[Browser] = None
        self.context: Optional[BrowserContext] = None
        self.page: Optional[Page] = None

    async def start(self):
        """Start the browser"""
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(
            headless=self.headless,
            args=[
                '--no-sandbox',
                '--disable-setuid-sandbox',
                '--disable-dev-shm-usage',
                '--disable-accelerated-2d-canvas',
                '--no-first-run',
                '--no-zygote',
                '--disable-gpu'
            ]
        )
        self.context = await self.browser.new_context(
            viewport={'width': 1920, 'height': 1080}
        )
        self.page = await self.context.new_page()
        self.page.set_default_timeout(self.timeout)

    async def goto(self, url: str, wait_until: str = "networkidle") -> None:
        """
        Navigate to URL
        
        Args:
            url: URL to navigate to
            wait_until: When to consider navigation succeeded
        """
        if not self.page:
            raise RuntimeError("Browser not started. Call start() first.")
        await self.page.goto(url, wait_until=wait_until)

    async def wait_for_selector(self, selector: str, timeout: Optional[int] = None) -> None:
        """
        Wait for selector to appear
        
        Args:
            selector: CSS selector to wait for
            timeout: Timeout in milliseconds
        """
        if not self.page:
            raise RuntimeError("Browser not started. Call start() first.")
        
        wait_timeout = timeout if timeout is not None else self.timeout
        await self.page.wait_for_selector(selector, timeout=wait_timeout)

    async def fill_input(self, selector: str, value: str, delay: int = 0) -> None:
        """
        Fill input field
        
        Args:
            selector: CSS selector for the input field
            value: Value to fill
            delay: Delay between key presses in milliseconds
        """
        if not self.page:
            raise RuntimeError("Browser not started. Call start() first.")
        
        await self.page.fill(selector, value)
        if delay > 0:
            # Type with delay for more natural interaction
            await self.page.locator(selector).clear()
            await self.page.type(selector, value, delay=delay)

    async def click(self, selector: str) -> None:
        """
        Click on element
        
        Args:
            selector: CSS selector for the element
        """
        if not self.page:
            raise RuntimeError("Browser not started. Call start() first.")
        await self.page.click(selector)

    async def get_content(self) -> str:
        """
        Get page content
        
        Returns:
            Page HTML content
        """
        if not self.page:
            raise RuntimeError("Browser not started. Call start() first.")
        return await self.page.content()

    async def get_cookies(self) -> List[Dict[str, Any]]:
        """
        Get browser cookies
        
        Returns:
            List of cookies
        """
        if not self.context:
            raise RuntimeError("Browser not started. Call start() first.")
        return await self.context.cookies()

    async def close(self) -> None:
        """Close the browser"""
        if self.page:
            await self.page.close()
            self.page = None
        if self.context:
            await self.context.close()
            self.context = None
        if self.browser:
            await self.browser.close()
            self.browser = None
        if self.playwright:
            await self.playwright.stop()
            self.playwright = None
