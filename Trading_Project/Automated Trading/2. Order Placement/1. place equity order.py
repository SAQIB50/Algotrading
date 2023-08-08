import angel_file as taf

angel = taf.angel


orderparams={ "variety": 'NORMAL', 
			  "tradingsymbol": 'ASHOKLEY-EQ',	
			  "symboltoken": taf.get_token_and_exchange("ASHOKLEY-EQ")[0],
			  "transactiontype": 'BUY', 
			  "exchange": 'NSE', 
			  "ordertype": 'MARKET', 
			  "producttype": 'INTRADAY', 
			  "duration": 'DAY', 
			  "price": 0.0, 
			  "squareoff": 0.0, 
			  "stoploss": 0.0, 
			  "triggerprice": 0.0, 
			  "trailingstoploss": 0.0, 
			  "quantity": 1 }


market_equity_id = taf.place_order(orderparams)
print("buy market order is placed with orderid = ", market_equity_id)




orderparams={ "variety": 'NORMAL', 
				"tradingsymbol": 'ASHOKLEY-EQ',
				"symboltoken": taf.get_token_and_exchange("ASHOKLEY-EQ")[0],
				"transactiontype": 'BUY', 
				"exchange": 'NSE', 
				"ordertype": 'LIMIT', 
				"producttype": 'INTRADAY', 
				"duration": 'DAY', 
				"price": 125, 
				"squareoff": 0.0, 
				"stoploss": 0.0, 
				"triggerprice": 0.0, 
				"trailingstoploss": 0.0, 
				"quantity": 1 }

limit_equity_id = taf.place_order(orderparams)
print("buy limit order is placed with orderid = ", limit_equity_id)
