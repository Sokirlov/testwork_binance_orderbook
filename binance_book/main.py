import asyncio
import json
import subprocess
import redis
from binance import AsyncClient, BinanceSocketManager

bids = []
ask = []
r = redis.StrictRedis('redis', 6379, decode_responses=True)

async def wright_db(id, a, b):
    data = json.dumps(dict(_id=id, ask=a, bids=b))
    r.set(id, data)
    print('get')

async def main():
    client = await AsyncClient.create()
    bm = BinanceSocketManager(client)
    ts = bm.depth_socket('BTCUSDT')

    ids = None
    async with ts as tscm:
        while True:
            res = await tscm.recv()
            if res.get('E', 0) == ids:
                bids.append(res.get('b'))
                ask.append(res.get('a'))
            else:
                if ids:
                    await wright_db(id=ids, a=ask, b=bids)
                ids = res.get('E')
                bids = res.get('b')
                ask = res.get('a')

    await client.close_connection()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())


