import angel_file as taf
from datetime import timedelta
import pandas as pd
import datetime
import pdb


angel = taf.angel

watchlist = ['IOC-EQ', 'NTPC-EQ', 'ONGC-EQ', 'POWERGRID-EQ', 'COALINDIA-EQ', 'ITC-EQ', 'TATAMOTORS-EQ', 'BPCL-EQ', 'SBIN-EQ', 'HINDALCO-EQ', 'WIPRO-EQ']

start_range = datetime.time(9, 15)
end_range = datetime.time(10, 50)
range_date = datetime.datetime.now().date()

start_time = str(range_date)+"T"+str(start_range)+"+05:30"
end_time = str(range_date)+"T"+str(end_range)+"+05:30"
traded = []

while True:
	for name in watchlist:
		symboltoken, exchange = taf.get_token_and_exchange(name)
		df = taf.get_historical_data(name=name, interval="5min", timeperiod=5)
		temp_df = df[start_time:end_time]

		range_high = temp_df["high"].max()
		range_low = temp_df["low"].max()
		ltp = taf.get_ltp(name=name, exchange=exchange)

		if (ltp > range_high) and (name not in traded):
			print("Buy order placed for", name)
			orderparams = {"variety": 'NORMAL', "tradingsymbol": name, "symboltoken": symboltoken, "transactiontype": 'BUY', "exchange": exchange, "ordertype": 'MARKET', "producttype": 'INTRADAY', "duration": 'DAY', "price": 0.0, "squareoff": 0.0, "stoploss": 0.0, "triggerprice": 0.0, "trailingstoploss": 0.0, "quantity": 1}
			orderId = taf.place_order(orderparams)
			traded.append(name)

		if (ltp < range_low) and (name not in traded):
			print("Sell order placed for", name)
			orderparams = {"variety": 'NORMAL', "tradingsymbol": name, "symboltoken": symboltoken, "transactiontype": 'SELL', "exchange": exchange, "ordertype": 'MARKET', "producttype": 'INTRADAY', "duration": 'DAY', "price": 0.0, "squareoff": 0.0, "stoploss": 0.0, "triggerprice": 0.0, "trailingstoploss": 0.0, "quantity": 1}
			orderId = taf.place_order(orderparams)
			traded.append(name)