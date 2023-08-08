import angel_file as taf
import talib
import pdb

angel = taf.angel
watchlist = ['COALINDIA-EQ', 'TATAMOTORS-EQ', 'SBIN-EQ', 'NATIONALUM-EQ', 'RECLTD-EQ', 'TATAPOWER-EQ', 'TATAMOTORS-EQ', 'NTPC-EQ', 'ASHOKLEY-EQ','CANBK-EQ']


for name in watchlist:
	candle_data = taf.get_historical_data(name = name, interval = "5min", timeperiod = 5)

	candle_data['rsi_30'] =  talib.RSI(candle_data['close'], timeperiod = 30)
	candle_data['ma_30'] = talib.MA(candle_data['close'] , timeperiod = 30 ,matype =0)
	candle_data['ema_14'] = talib.EMA(candle_data['close'], timeperiod=14)
	candle_data['atr_14'] = talib.ATR(candle_data['high'], candle_data['low'], candle_data['close'], timeperiod=14)
	candle_data['bollinger_14'] = talib.BBANDS(candle_data['close'], timeperiod = 14, nbdevup=2, nbdevdn=2, matype=0)[1]

	indicators = candle_data.iloc[-1]
	print(indicators, "\n\n\n\n")
	#print(candle_data)




