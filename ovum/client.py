from __future__ import annotations

import logging
from itertools import count
from typing import Any, Union
import httpx

from dto.ovum_dto import OvumAddressDTO
from const.address_mapping import address_map


class OvumClient:
    def __init__(self, ip: str):
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

    async def __read(self, addresses: Union[list[int], int] = -1) -> Any:
        query = addresses
        if addresses == -1:
            query = 'all'
        if type(addresses) is list:
            query = ','.join(map(str, addresses))
        path = f'ODJET_CGI?pread={query}'
        json = await self.__read_json_from_webserver(path)
        json = json['tab_param']
        for index, item in enumerate(json):  # rename fields
            json[index]['address'] = int(json[index].pop('addr'))
            json[index]['default'] = json[index].pop('def')
        return json

    @staticmethod
    def __convert_to_dto(json: Any) -> OvumAddressDTO | None:
        if json['address'] in address_map:
            json['label'] = address_map[json['address']]['label']
            json['unit'] = address_map[json['address']]['unit']
            for key in ['value', 'min', 'max', 'default']:
                json[key] = float(json[key]) * address_map[json['address']]['factor']
            addr_dto = OvumAddressDTO.from_dict(json)
            return addr_dto
        return None

    async def get_by_address(self, addr: int) -> OvumAddressDTO | None:
        json = await self.__read(addr)
        return self.__convert_to_dto(json[0])

    async def get_multiple_by_address(self, addresses: list[int]) -> list[OvumAddressDTO | None]:
        json = await self.__read(addresses)
        result = []
        for item in json:
            if item['address'] in address_map:
                result.append(self.__convert_to_dto(item))
        return result

    async def get_all(self) -> list[OvumAddressDTO | None]:
        json = await self.__read()
        result = []
        for item in json:
            if item['address'] in address_map:
                result.append(self.__convert_to_dto(item))
        return result
