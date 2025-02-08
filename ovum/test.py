import asyncio
import logging

from client import OvumClient


async def main():
    logging.basicConfig(level=logging.INFO)
    client = OvumClient('10.10.20.35')
    # value = await client.get_by_address(505)
    logging.info(f'{await client.get_by_address(5)}')
    logging.info(f'{await client.get_by_address(450)}')
    logging.info(f'{await client.get_by_address(456)}')
    logging.info(f'{await client.get_by_address(500)}')
    logging.info(f'{await client.get_by_address(503)}')
    logging.info(f'{await client.get_by_address(504)}')
    logging.info(f'{await client.get_by_address(505)}')
    logging.info(f'{await client.get_by_address(506)}')
    logging.info(f'{await client.get_by_address(524)}')
    logging.info(f'{await client.get_all()}')
    logging.info(f'{await client.get_multiple_by_address([450, 456, 500, 503, 504, 505, 506, 524])}')


asyncio.run(main())
