from __future__ import annotations

import os
from functools import lru_cache
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()


class Settings:
    """Configurações centrais da aplicação carregadas via variáveis de ambiente."""

    def __init__(self) -> None:
        base_dir = Path(__file__).resolve().parent.parent
        self.base_dir = base_dir
        self.project_root = base_dir.parent
        self.app_port: int = int(os.getenv("APP_PORT", "8000"))
        self.headless_default: bool = (
            os.getenv("HEADLESS_DEFAULT", "true").lower() == "true"
        )
        self.login_timeout_ms: int = int(os.getenv("LOGIN_TIMEOUT", "30000"))
        self.vnc_password: str = os.getenv("VNC_PASSWORD", "vncpass")
        self.clientes_dir: Path = (self.project_root / "clientes").resolve()
        self.logs_dir: Path = (self.project_root / "logs").resolve()
        self.assets_dir: Path = (self.project_root / "assets").resolve()
        self.default_login_url: str = os.getenv(
            "PAGBANK_LOGIN_URL", "https://www.pagbank.com.br"
        )


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()
