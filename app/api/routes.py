from __future__ import annotations

from fastapi import APIRouter, HTTPException

from app.automation.login_flow import run_login_flow
from app.core.config import get_settings
from app.models.login import LoginRequest, LoginResponse

router = APIRouter()


@router.post("/login", response_model=LoginResponse)
async def trigger_login(payload: LoginRequest) -> LoginResponse:
    settings = get_settings()
    headless = payload.headless if payload.headless is not None else settings.headless_default

    try:
        result = await run_login_flow(
            username=payload.username,
            password=payload.password,
            headless=headless,
            timeout_ms=settings.login_timeout_ms,
            output_dir=settings.clientes_dir,
            login_url=settings.default_login_url,
        )
    except HTTPException:
        raise
    except Exception as exc:  # pragma: no cover - proteção extra
        raise HTTPException(status_code=500, detail=str(exc)) from exc

    return result
