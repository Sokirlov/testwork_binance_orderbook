import json
import time
import os
import redis
import requests
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient


class DBmongoworker:
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "uk-UA,uk;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6",
        "cache-control": "max-age=0",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    }

    @property
    def db_username(self):
        return os.getenv("MONGO_USERNAME")
    @property
    def db_password(self):
        return os.getenv('MONGO_PASSWORD')
    @property
    def db_host(self):
        return os.getenv('MONGO_HOSTNAME')

    def write_to_db(self, data):
        try:
            self.orderbook.insert_one({**data})
        except:
            ...

    def get_hystory(self):
        resp = requests.get('https://api.binance.com/api/v3/depth?limit=5000&symbol=BTCUSDT')
        if resp.status_code == 200:
            data = resp.json()
            data["_id"] = data.pop("lastUpdateId")
            self.write_to_db(data)
    def __del__(self):
        self.__dbclient__.close()

    def __init__(self):
        self.__dbclient__ = AsyncIOMotorClient(f"mongodb://{self.db_username}:{self.db_password}@{self.db_host}:27017")
        self.__db__ = self.__dbclient__["binance"]
        self.orderbook = self.__db__["orderbook"]


async def main():
    m = DBmongoworker()
    r = redis.StrictRedis('redis', 6379, decode_responses=True)
    while True:
        try:
            # print('write', r.keys())
            for n in r.keys():
                print('key', n)
                data = json.loads(r.get(n))
                print('data is', data)
                if data:
                    m.write_to_db(data)
                    print('write')
                    r.delete(n)
        except:
            time.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())

