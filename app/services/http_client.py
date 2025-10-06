"""
HTTP Client para integração com APIs do PagBank
Gerencia cookies, headers e requisições HTTP
"""
from typing import Any, Dict, Optional

import httpx


class PagBankHttpClient:
    """Cliente HTTP para APIs do PagBank com gerenciamento de sessão"""

    def __init__(
        self,
        base_url: str = "https://pagbank.com.br",
        timeout: float = 30.0,
    ):
        """
        Inicializa o cliente HTTP

        Args:
            base_url: URL base da API
            timeout: Timeout para requisições em segundos
        """
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.cookies: Dict[str, str] = {}
        self.default_headers = self._get_default_headers()

    def _get_default_headers(self) -> Dict[str, str]:
        """
        Retorna headers padrão para requisições

        Returns:
            Dict com headers padrão
        """
        return {
            "accept": "application/json",
            "accept-language": "pt-BR",
            "content-type": "application/json",
            "user-agent": (
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
            ),
            "x-requested-with": "XMLHttpRequest",
        }

    def init_cookies(self, cookies: Dict[str, str]) -> None:
        """
        Inicializa cookies para reutilização

        Args:
            cookies: Dicionário com cookies
        """
        self.cookies.update(cookies)

    def _build_url(self, path: str) -> str:
        """
        Constrói URL completa

        Args:
            path: Caminho da API (ex: /api/v1/users)

        Returns:
            URL completa
        """
        if path.startswith("http"):
            return path
        path = path.lstrip("/")
        return f"{self.base_url}/{path}"

    def _merge_headers(self, custom_headers: Optional[Dict[str, str]] = None) -> Dict[str, str]:
        """
        Mescla headers customizados com os padrão

        Args:
            custom_headers: Headers customizados

        Returns:
            Dict com todos os headers
        """
        headers = self.default_headers.copy()
        if custom_headers:
            headers.update(custom_headers)
        return headers

    async def get(
        self,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        use_cookies: bool = True,
    ) -> httpx.Response:
        """
        Faz requisição GET

        Args:
            path: Caminho da API
            params: Query parameters
            headers: Headers customizados
            use_cookies: Se True, usa cookies armazenados

        Returns:
            Response da requisição
        """
        url = self._build_url(path)
        merged_headers = self._merge_headers(headers)
        cookies = self.cookies if use_cookies else None

        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.get(
                url,
                params=params,
                headers=merged_headers,
                cookies=cookies,
            )
            # Atualiza cookies se houver novos
            if use_cookies and response.cookies:
                self.cookies.update(dict(response.cookies))
            return response

    async def post(
        self,
        path: str,
        data: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        use_cookies: bool = True,
    ) -> httpx.Response:
        """
        Faz requisição POST

        Args:
            path: Caminho da API
            data: Dados form-encoded
            json: Dados JSON
            headers: Headers customizados
            use_cookies: Se True, usa cookies armazenados

        Returns:
            Response da requisição
        """
        url = self._build_url(path)
        merged_headers = self._merge_headers(headers)
        cookies = self.cookies if use_cookies else None

        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.post(
                url,
                data=data,
                json=json,
                headers=merged_headers,
                cookies=cookies,
            )
            # Atualiza cookies se houver novos
            if use_cookies and response.cookies:
                self.cookies.update(dict(response.cookies))
            return response

    async def put(
        self,
        path: str,
        data: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        use_cookies: bool = True,
    ) -> httpx.Response:
        """
        Faz requisição PUT

        Args:
            path: Caminho da API
            data: Dados form-encoded
            json: Dados JSON
            headers: Headers customizados
            use_cookies: Se True, usa cookies armazenados

        Returns:
            Response da requisição
        """
        url = self._build_url(path)
        merged_headers = self._merge_headers(headers)
        cookies = self.cookies if use_cookies else None

        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.put(
                url,
                data=data,
                json=json,
                headers=merged_headers,
                cookies=cookies,
            )
            # Atualiza cookies se houver novos
            if use_cookies and response.cookies:
                self.cookies.update(dict(response.cookies))
            return response

    async def delete(
        self,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        use_cookies: bool = True,
    ) -> httpx.Response:
        """
        Faz requisição DELETE

        Args:
            path: Caminho da API
            params: Query parameters
            headers: Headers customizados
            use_cookies: Se True, usa cookies armazenados

        Returns:
            Response da requisição
        """
        url = self._build_url(path)
        merged_headers = self._merge_headers(headers)
        cookies = self.cookies if use_cookies else None

        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.delete(
                url,
                params=params,
                headers=merged_headers,
                cookies=cookies,
            )
            # Atualiza cookies se houver novos
            if use_cookies and response.cookies:
                self.cookies.update(dict(response.cookies))
            return response

    async def head(
        self,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        use_cookies: bool = True,
    ) -> httpx.Response:
        """
        Faz requisição HEAD

        Args:
            path: Caminho da API
            params: Query parameters
            headers: Headers customizados
            use_cookies: Se True, usa cookies armazenados

        Returns:
            Response da requisição
        """
        url = self._build_url(path)
        merged_headers = self._merge_headers(headers)
        cookies = self.cookies if use_cookies else None

        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.head(
                url,
                params=params,
                headers=merged_headers,
                cookies=cookies,
            )
            # Atualiza cookies se houver novos
            if use_cookies and response.cookies:
                self.cookies.update(dict(response.cookies))
            return response

    def clear_cookies(self) -> None:
        """Limpa todos os cookies armazenados"""
        self.cookies.clear()

    def get_cookies(self) -> Dict[str, str]:
        """
        Retorna cookies atuais

        Returns:
            Dict com cookies
        """
        return self.cookies.copy()

    def set_header(self, key: str, value: str) -> None:
        """
        Define um header padrão

        Args:
            key: Nome do header
            value: Valor do header
        """
        self.default_headers[key] = value

    def remove_header(self, key: str) -> None:
        """
        Remove um header padrão

        Args:
            key: Nome do header
        """
        self.default_headers.pop(key, None)
