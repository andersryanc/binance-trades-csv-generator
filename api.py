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
    pass

client = Client(api_key, api_secret)

# PRELOAD BTC PRICE DATA in 30min klines
klines = client.get_klines(symbol='BTCUSDT', interval=KLINE_INTERVAL_30MINUTE)

# HEADERS
# 
print("SYMBOL", "\t", "QTY", "\t", "COST", "\t", "DATE", "\t", "BTC PRICE")

# TRADE DATA
# 
trades = client.get_my_trades(symbol='IOTABTC')
for trade in trades:
    btcAvgPrice = 0
    for kline in klines:
        if (kline[0] < trade['time'] and kline[6] > trade['time']):
            btcAvgPrice = ( float(kline[2]) + float(kline[3]) ) / 2

    print(trade['commissionAsset'], "\t", trade['qty'], "\t", trade['price'], "\t", ctime(trade['time']/1000), "\t", btcAvgPrice)
# print(trades)
