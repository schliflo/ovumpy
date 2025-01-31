from __future__ import annotations

import logging
import httpx


class OvumClient:
    def __init__(self, ip: str = '10.10.20.35'):
        self.__ip: str = ip
        self.__httpx_client = httpx.AsyncClient()

    async def get_value(self, addr: int) -> int | None:
        url = f'http://{self.__ip}/ODJET_CGI?pread={addr}'
        response = await self.__httpx_client.get(url=url)
        if response.status_code in (200, 201):
            return response.json()['tab_param'][0]['value'] or None
        else:
            logging.warning(f'URL {url} returned status code {response.status_code} for GET request')
            return None
