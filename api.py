from os import environ
from sys import exit
from time import ctime, strftime
from binance.client import Client
from binance.enums import *

try:
    api_key = environ['BINANCE_API_KEY']
    api_secret = environ['BINANCE_API_SECRET']
except KeyError:
    print("Missing API KEYS!")
    exit()

client = Client(api_key, api_secret)

# PRELOAD BTC PRICE DATA in 30min klines
klines = client.get_klines(symbol='BTCUSDT', interval=KLINE_INTERVAL_30MINUTE)

# HEADERS
# 
print(
    'DATE', ",",
    'SYMBOL', ",",
    'QTY', ",",
    'COST', ",",
    'BTC PRICE', ",",
    'USD PRICE', ",",
    'TOTAL'
)

symbols = ['IOTABTC', 'LTCBTC', 'ETHBTC']

# TRADE DATA
# 
for symbol in symbols:
    trades = client.get_my_trades(symbol=symbol)
    # print(trades)
    for trade in trades:
        btcAvgPrice = 0
        for kline in klines:
            if (kline[0] < trade['time'] and kline[6] > trade['time']):
                btcAvgPrice = ( float(kline[2]) + float(kline[3]) ) / 2

        price = -float(trade['price'])
        if trade['commissionAsset'] == "BTC":
            price = float(trade['price'])

        print(
            ctime(trade['time']/1000), ",",
            trade['commissionAsset'], ",",
            "%.2f" % float(trade['qty']), ",",
            price, ",",
            "%.2f" % btcAvgPrice, ",",
            ("%.2f" % (price * btcAvgPrice)), ",",
            "%.2f" % (float(trade['qty']) * price * btcAvgPrice)
        )
