import asyncio
import logging

from client import OvumClient

async def main():
    logging.basicConfig(level=logging.INFO)
    client = OvumClient()
    # value = await client.get_address(505)
    logging.info(f'{await client.get_address(5)}')
    logging.info(f'{await client.get_address(450)}')
    logging.info(f'{await client.get_address(456)}')
    logging.info(f'{await client.get_address(500)}')
    logging.info(f'{await client.get_address(503)}')
    logging.info(f'{await client.get_address(504)}')
    logging.info(f'{await client.get_address(505)}')
    logging.info(f'{await client.get_address(506)}')
    logging.info(f'{await client.get_address(524)}')

asyncio.run(main())
