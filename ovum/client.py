from __future__ import annotations

import logging
from typing import Any
import httpx

from dto.ovum_dto import OvumAddressDTO


class OvumClient:
    def __init__(self, ip: str = '10.10.20.35'):
        self.__ip: str = ip
        self.__httpx_client = httpx.AsyncClient()

    async def __read_json_from_webserver(self, path: str) -> Any | None:
        url = f'http://{self.__ip}/{path}'
        response = await self.__httpx_client.get(url=url)
        if response.status_code in (200, 201):
            return response.json() or None
        else:
            logging.warning(f'URL {url} returned status code {response.status_code} for GET request')
            return None

    async def __read_address(self, addr: int) -> Any:
        path = f'ODJET_CGI?pread={addr}'
        json = await self.__read_json_from_webserver(path)
        json = json['tab_param'][0]
        json['address'] = json.pop('addr')
        json['default'] = json.pop('def')
        return json

    async def get_address(self, addr: int) -> OvumAddressDTO | None:
        json = await self.__read_address(addr)
        addr_dto = OvumAddressDTO.from_dict(json)
        # TODO: map label to address
        return addr_dto or None
