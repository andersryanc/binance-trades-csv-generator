This script uses the [Binance API](https://www.binance.com/restapipub.html) via [python-binance](https://github.com/sammchardy/python-binance) to generate a tab based CSV file containing your trade history with the 30 min average BTC/USDT price for each trade.

# Using the script

First of all, initialize and activate the virtual environment:

```
virtualenv -p python3 .env
source .env/bin/activate
```

Then make sure you have the dependencies installed:

```
pip install -r requirements.txt
```

Modify the `generate-csv.sample.sh` and add your own `BINANCE_API_KEY` + `BINANCE_API_SECRET` keys. Then you can run the following to generate a CSV containing your trade history along with the most recent 30 min average price of BTC/USDT:

```
./generate-csv.sh > data.csv
```

> You may need to make the file executable with `chmod +x generate-csv.sh`.

When your all done using this script, you can exit out of the virtual environment with:

```
deactivate
```
