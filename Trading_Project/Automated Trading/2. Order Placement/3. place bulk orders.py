import angel_file as taf

angel = taf.angel

buy_watchlist = ['COALINDIA-EQ', 'ONGC-EQ', 'NMDC-EQ', 'NATIONALUM-EQ']


for name in buy_watchlist:

	token, exchange = taf.get_token_and_exchange(name)
	orderparams={ 
				"variety": 'NORMAL',
				"tradingsymbol": name,	
				"symboltoken": token,
				"transactiontype": 'BUY',
				"exchange": exchange,
				"ordertype": 'MARKET',
				"producttype": 'INTRADAY',
				"duration": 'DAY',
				"price": 0.0,
				"squareoff": 0.0,
				"stoploss": 0.0,
				"triggerprice": 0.0,
				"trailingstoploss": 0.0,
				"quantity": 1
				}
	order_id = taf.place_order(orderparams)
	print("Buy order is placed for = ", name)



sell_watchlist = ['GMRINFRA-EQ', 'BHEL-EQ', 'NTPC-EQ', 'ASHOKLEY-EQ']
for name in sell_watchlist:
	token, exchange = taf.get_token_exchange(name)
	orderparams={ 
				"variety": 'NORMAL',
				"tradingsymbol": name,	
				"symboltoken": token,
				"transactiontype": 'SELL',
				"exchange": exchange,
				"ordertype": 'MARKET',
				"producttype": 'INTRADAY',
				"duration": 'DAY',
				"price": 0.0,
				"squareoff": 0.0,
				"stoploss": 0.0,
				"triggerprice": 0.0,
				"trailingstoploss": 0.0,
				"quantity": 1
				}
	order_id = taf.place_order(orderparams)
	print("Sell order is placed for = ", name)
