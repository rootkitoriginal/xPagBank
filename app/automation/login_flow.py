from __future__ import annotations

import asyncio
from datetime import datetime
from pathlib import Path
from typing import Iterable, Optional

from fastapi import HTTPException
from playwright.async_api import Page, TimeoutError as PlaywrightTimeoutError

from app.models.login import LoginResponse
from app.services.playwright_service import PlaywrightService
from app.utils.fs import ensure_dir, write_json

LOGIN_BUTTON_SELECTORS: tuple[str, ...] = (
    "text=Entrar",
    "role=button[name='Entrar']",
    "role=link[name='Entre']",
    "[data-testid='sign-in-button']",
    "a[href*='login']",
)

USERNAME_FIELD_SELECTORS: tuple[str, ...] = (
    "input[name='username']",
    "input[type='email']",
    "input[autocomplete='username']",
    "role=textbox[name='Seu CPF ou e-mail']",
)

PASSWORD_FIELD_SELECTORS: tuple[str, ...] = (
    "input[type='password']",
    "input[autocomplete='current-password']",
    "input[name='password']",
)

SUBMIT_BUTTON_SELECTORS: tuple[str, ...] = (
    "role=button[name='Continuar']",
    "role=button[name='Entrar']",
    "button[type='submit']",
)

COOKIE_BANNER_SELECTORS: tuple[str, ...] = (
    "text=Aceitar todos",
    "role=button[name='Aceitar']",
    "role=button[name='Aceito']",
)


async def run_login_flow(
    *,
    username: str,
    password: str,
    headless: bool,
    timeout_ms: int,
    output_dir: Path,
    login_url: str,
) -> LoginResponse:
    client_dir = ensure_dir(Path(output_dir) / username)
    timestamp = datetime.utcnow().strftime("%Y%m%d-%H%M%S")
    screenshot_path = client_dir / f"screenshot-{timestamp}.png"
    cookies_path = client_dir / "cookies.json"

    cookies_count = 0

    async with PlaywrightService(headless=headless, timeout_ms=timeout_ms) as service:
        page = await service.get_page()
        success = False
        error_message: Optional[str] = None

        try:
            await navigate_and_prepare(page, login_url)
            await close_cookie_banner(page)
            await open_login_modal(page)
            await fill_username(page, username)
            await submit_step(page)
            await fill_password(page, password)
            await submit_step(page)
            await wait_post_login(page)
            success = True
        except Exception as exc:  # pragma: no cover - salvaguarda
            error_message = str(exc)
        finally:
            await capture_screenshot(page, screenshot_path)
            cookies = await page.context.cookies()
            cookies_count = len(cookies)
            if cookies:
                write_json(cookies_path, cookies)
            elif cookies_path.exists():
                cookies_path.unlink()

    return LoginResponse(
        success=success,
        username=username,
        screenshot=str(relative_path(screenshot_path, output_dir)) if screenshot_path.exists() else None,
        cookies_count=cookies_count if success else 0,
        cookies_file=(
            str(relative_path(cookies_path, output_dir))
            if success and cookies_path.exists()
            else None
        ),
        error=error_message,
    )


async def navigate_and_prepare(page: Page, url: str) -> None:
    await page.goto(url, wait_until="networkidle")
    await asyncio.sleep(1)


async def close_cookie_banner(page: Page) -> None:
    await click_first_available(page, COOKIE_BANNER_SELECTORS, optional=True)


async def open_login_modal(page: Page) -> None:
    await click_first_available(page, LOGIN_BUTTON_SELECTORS)


async def fill_username(page: Page, username: str) -> None:
    await fill_first_available(page, USERNAME_FIELD_SELECTORS, username)


async def fill_password(page: Page, password: str) -> None:
    await fill_first_available(page, PASSWORD_FIELD_SELECTORS, password)


async def submit_step(page: Page) -> None:
    await click_first_available(page, SUBMIT_BUTTON_SELECTORS, optional=True)
    await page.keyboard.press("Enter")


async def wait_post_login(page: Page) -> None:
    try:
        await page.wait_for_load_state("networkidle")
        await asyncio.sleep(2)
    except PlaywrightTimeoutError as exc:  # pragma: no cover - fallback
        raise HTTPException(status_code=504, detail="Timeout aguardando pós-login") from exc


async def click_first_available(
    page: Page,
    selectors: Iterable[str],
    *,
    optional: bool = False,
) -> None:
    for selector in selectors:
        locator = page.locator(selector)
        try:
            await locator.first.click(timeout=1500)
            return
        except PlaywrightTimeoutError:
            continue
        except Exception:
            continue
    if not optional:
        raise HTTPException(status_code=422, detail=f"Elemento não encontrado: {selectors!r}")


async def fill_first_available(page: Page, selectors: Iterable[str], value: str) -> None:
    for selector in selectors:
        locator = page.locator(selector)
        try:
            await locator.first.fill(value, timeout=1500)
            return
        except PlaywrightTimeoutError:
            continue
        except Exception:
            continue
    raise HTTPException(status_code=422, detail=f"Campo não encontrado: {selectors!r}")


async def capture_screenshot(page: Page, destination: Path) -> None:
    ensure_dir(destination.parent)
    try:
        await page.screenshot(path=str(destination), full_page=True)
    except Exception:  # pragma: no cover - captura opcional
        if destination.exists():
            destination.unlink()


def relative_path(path: Path, base: Path) -> Path:
    try:
        return path.relative_to(base.parent)
    except ValueError:
        return path
