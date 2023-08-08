import angel_file as taf

angel = taf.angel

watchlist = ['COALINDIA-EQ', 'TATAMOTORS-EQ', 'SBIN-EQ', 'NATIONALUM-EQ', 'RECLTD-EQ', 'TATAPOWER-EQ', 'TATAMOTORS-EQ', 'NTPC-EQ', 'ASHOKLEY-EQ','CANBK-EQ']

for name in watchlist:
    token, exchange = taf.get_token_and_exchange(name)
    ltp = taf.get_ltp(name, exchange)

    rsi = taf.get_ltp(name, exchange)
    st = taf.get_ltp(name, exchange)


    if (rsi > 60) and (st == 'Green') and (lgt > s1 ) and  (ma30 > ma60):
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
        print("Sell order is placed for = ", name)


    if (rsi < 40) and (st == 'red'):
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
        print("Buy order is placed for = ", name)