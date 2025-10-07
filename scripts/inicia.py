#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
from typing import Any, Dict

DEFAULT_HOST = "http://localhost:8000"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Dispara o fluxo de login PagBank via API FastAPI"
    )
    parser.add_argument("username", help="Usuário/cpf do PagBank")
    parser.add_argument("password", help="Senha do PagBank")
    parser.add_argument(
        "--host",
        default=DEFAULT_HOST,
        help=f"URL base da API (padrão: {DEFAULT_HOST})",
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--headless",
        dest="headless",
        action="store_true",
        help="Força execução headless",
    )
    group.add_argument(
        "--no-headless",
        dest="headless",
        action="store_false",
        help="Força execução com navegador visível (headful)",
    )
    parser.set_defaults(headless=None)
    parser.add_argument(
        "--timeout",
        type=int,
        default=120,
        help="Timeout da requisição em segundos",
    )
    return parser


def call_login(host: str, payload: Dict[str, Any], *, timeout: int) -> Dict[str, Any]:
    url = host.rstrip("/") + "/login"
    data = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        url=url,
        data=data,
        method="POST",
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        body = response.read().decode("utf-8")
        return json.loads(body)


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    payload: Dict[str, Any] = {
        "username": args.username,
        "password": args.password,
    }
    if args.headless is not None:
        payload["headless"] = args.headless

    try:
        result = call_login(args.host, payload, timeout=args.timeout)
    except urllib.error.HTTPError as http_error:
        error_body = http_error.read().decode("utf-8")
        print(f"Falha HTTP {http_error.code}: {error_body}", file=sys.stderr)
        return 2
    except urllib.error.URLError as url_error:
        print(f"Erro de conexão: {url_error}", file=sys.stderr)
        return 3

    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
