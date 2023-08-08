import talib
import angel_file as taf
import time


watchlist = ['NATIONALUM-EQ', 'SAIL-EQ', 'IOC-EQ', 'ASHOKLEY-EQ', 'PFC-EQ', 'NTPC-EQ', 'NMDC-EQ', 'RECLTD-EQ', 'GAIL-EQ', 'CUB-EQ', 'ONGC-EQ', 'CANBK-EQ', 'TATAPOWER-EQ', 'M&MFIN-EQ', 'EXIDEIND-EQ', 'POWERGRID-EQ', 'RBLBANK-EQ', 'COALINDIA-EQ', 'MANAPPURAM-EQ', 'INDIACEM-EQ', 'INDHOTEL-EQ', 'BEL-EQ', 'APOLLOTYRE-EQ', 'PETRONET-EQ', 'ITC-EQ', 'MOTHERSUMI-EQ', 'IBULHSGFIN-EQ', 'ABFRL-EQ', 'DELTACORP-EQ', 'VEDL-EQ', 'ZEEL-EQ', 'INDUSTOWER-EQ', 'HINDPETRO-EQ']
traded = []


while True:
	for name in watchlist:
		print(name)
		candle_data = taf.get_historical_data(name = name, interval = "5min", timeperiod = 5)
		candle_data['rsi_7'] = talib.RSI(candle_data['close'], timeperiod=7)
		candle_data['ma_30'] = talib.MA(candle_data['close'] , timeperiod = 30 ,matype =0)
		candle_data['ma_60'] = talib.MA(candle_data['close'] , timeperiod = 60 ,matype =0)

		candle_data = candle_data.iloc[-1]

		if (candle_data['rsi_7'] > 60) and (candle_data['ma_30'] > candle_data['ma_60']) and (name not in traded):

			orderparams={ "variety": 'NORMAL',
						"tradingsymbol": name,  
						"symboltoken": taf.get_token_and_exchange(name)[0],
						"transactiontype": 'BUY',
						"exchange": taf.get_token_and_exchange(name)[1],
						"ordertype": 'MARKET',
						"producttype": 'INTRADAY',
						"duration": 'DAY',
						"price": 0.0,
						"squareoff": 0.0,
						"stoploss": 0.0,
						"triggerprice": 0.0,
						"trailingstoploss": 0.0,
						"quantity": 1 }

			print("		Buy signal for ", name)
			traded.append(name)
			orderId = taf.place_order(orderparams)

		if (candle_data['rsi_7'] < 40) and (candle_data['ma_30'] < candle_data['ma_60']) and (name not in traded):
			orderparams={ "variety": 'NORMAL',
						"tradingsymbol": name,  
						"symboltoken": taf.get_token_and_exchange(name)[0],
						"transactiontype": 'SELL',
						"exchange": taf.get_token_and_exchange(name)[1],
						"ordertype": 'MARKET',
						"producttype": 'INTRADAY',
						"duration": 'DAY',
						"price": 0.0,
						"squareoff": 0.0,
						"stoploss": 0.0,
						"triggerprice": 0.0,
						"trailingstoploss": 0.0,
						"quantity": 1 }

			print("		Sell signal for ", name)
			traded.append(name)
			orderId = taf.place_order(orderparams)