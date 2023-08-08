import angel_file as taf

angel = taf.angel

orderparams={"variety": 'NORMAL', 
			"tradingsymbol": 'BANKNIFTY07OCT2136100CE',	
			"symboltoken": '40671', 
			"transactiontype": 'BUY', 
			"exchange": 'NFO', 
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

market_options_id = taf.place_order(orderparams)
print("buy order is placed with orderid = ", market_options_id)



orderparams={ "variety": 'NORMAL', 
			"tradingsymbol": 'BANKNIFTY07OCT2136100CE',	
			"symboltoken": '40671', 
			"transactiontype": 'BUY', 
			"exchange": 'NFO', 
			"ordertype": 'LIMIT', 
			"producttype": 'INTRADAY', 
			"duration": 'DAY', 
			"price": 1190, 
			"squareoff": 0.0, 
			"stoploss": 0.0, 
			"triggerprice": 0.0, 
			"trailingstoploss": 0.0, 
			"quantity": 1 }

limit_options_id = taf.place_order(orderparams)
print("buy order is placed with orderid= ", limit_options_id)

