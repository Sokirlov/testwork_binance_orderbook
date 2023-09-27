import datetime
import os
import pymongo
import asyncio
from flask import Flask, render_template

DB_USER = os.getenv('MONGO_USERNAME')
DB_PASSWORD = os.getenv('MONGO_PASSWORD')
DB_HOST = os.getenv('MONGO_HOSTNAME')

app = Flask(__name__)

def get_data():
    try:
        dbclient = pymongo.MongoClient(f"mongodb://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:27017")
        db = dbclient["binance"]
        orderbook = db["orderbook"]
        data = orderbook.find().limit(1).sort([('$natural', -1)])[0]
        dbclient.close()
    except:
        data = dict(bids=list(), ask=list())
    return data

@app.route('/')
def index():
    bids = ask = list()
    data = get_data()
    bids += data.get('bids')
    ask += data.get('ask')
    tm = str(data.get('_id'))[:-3]
    ids = datetime.datetime.fromtimestamp(int(tm))
    return render_template("tmpl.html", bids=bids, ask=ask, ids=ids)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)