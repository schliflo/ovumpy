import asyncio
import logging

from client import OvumClient

async def main():
    logging.basicConfig(level=logging.INFO)
    client = OvumClient()
    # value = await client.get_address(505)
    logging.info(f'{await client.get_address(5)}')
    logging.info(f'{await client.get_address(505)}')

asyncio.run(main())
