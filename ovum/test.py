import asyncio
import logging

from client import OvumClient

async def main():
    logging.basicConfig(level=logging.INFO)
    client = OvumClient()
    value = await client.get_address(8)
    logging.info(f'{value}')

asyncio.run(main())
