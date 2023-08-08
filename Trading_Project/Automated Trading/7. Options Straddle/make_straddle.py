import angel_file as taf


angel = taf.angel


name = 'BANKNIFTY'
straddle_script_names = taf.make_straddle(name=name, exipry='10AUG23', gap=100)
call_script = straddle_script_names[0]
put_script = straddle_script_names[1]

# short straddle
orderparams = {'variety': 'NORMAL', 'tradingsymbol': call_script, 'symboltoken': taf.get_token_and_exchange(call_script)[0], 'transactiontype': 'SELL', 'exchange': taf.get_token_and_exchange(call_script)[1], 'ordertype': 'MARKET', 'producttype': 'INTRADAY', 'duration': 'DAY',	'price': 0.0, 'squareoff': 0.0,	'stoploss': 0.0, 'triggerprice': 0.0, 'trailingstoploss': 0.0, 'quantity': 1}
call_orderId = taf.place_order(orderparams)

orderparams = {'variety': 'NORMAL', 'tradingsymbol': put_script, 'symboltoken': taf.get_token_and_exchange(put_script)[0], 'transactiontype': 'SELL', 'exchange': taf.get_token_and_exchange(put_script)[1], 'ordertype': 'MARKET', 'producttype': 'INTRADAY', 'duration': 'DAY', 'price': 0.0, 'squareoff': 0.0, 'stoploss': 0.0, 'triggerprice': 0.0, 'trailingstoploss': 0.0, 'quantity': 1}
put_orderId = taf.place_order(orderparams)


executed_combined_premium = taf.get_combined_premium(call_orderId, put_orderId)


while True:
    current_combined_premium = taf.get_current_premium(call_script, put_script)

    if current_combined_premium >= (executed_combined_premium * 1.1):
        orderparams = {'variety': 'NORMAL', 'tradingsymbol': call_script, 'symboltoken': taf.get_token_and_exchange(call_script)[0],	'transactiontype': 'BUY', 'exchange': taf.get_token_and_exchange(call_script)[1], 'ordertype': 'MARKET', 'producttype': 'INTRADAY', 'duration': 'DAY',	'price': 0.0, 'squareoff': 0.0,	'stoploss': 0.0, 'triggerprice': 0.0, 'trailingstoploss': 0.0, 'quantity': 1}
        taf.place_order(orderparams)

        orderparams = {'variety': 'NORMAL', 'tradingsymbol': put_script, 'symboltoken': taf.get_token_and_exchange(put_script)[0], 'transactiontype': 'BUY', 'exchange': taf.get_token_and_exchange(put_script)[1], 'ordertype': 'MARKET', 'producttype': 'INTRADAY', 'duration': 'DAY', 'price': 0.0, 'squareoff': 0.0, 'stoploss': 0.0, 'triggerprice': 0.0, 'trailingstoploss': 0.0, 'quantity': 1}
        taf.place_order(orderparams)

        print('Stoploss hit, straddle exited ')
        break

    # target .. 1:2 risk reward
    if current_combined_premium <= (executed_combined_premium * 0.8):
        orderparams = {'variety': 'NORMAL', 'tradingsymbol': call_script, 'symboltoken': taf.get_token_and_exchange(call_script)[0],	'transactiontype': 'BUY', 'exchange': taf.get_token_and_exchange(call_script)[1], 'ordertype': 'MARKET', 'producttype': 'INTRADAY', 'duration': 'DAY',	'price': 0.0, 'squareoff': 0.0,	'stoploss': 0.0, 'triggerprice': 0.0, 'trailingstoploss': 0.0, 'quantity': 50}
        taf.place_order(orderparams)

        orderparams = {'variety': 'NORMAL', 'tradingsymbol': put_script, 'symboltoken': taf.get_token_and_exchange(put_script)[0], 'transactiontype': 'BUY', 'exchange': taf.get_token_and_exchange(put_script)[1], 'ordertype': 'MARKET', 'producttype': 'INTRADAY', 'duration': 'DAY', 'price': 0.0, 'squareoff': 0.0, 'stoploss': 0.0, 'triggerprice': 0.0, 'trailingstoploss': 0.0, 'quantity': 50}
        taf.place_order(orderparams)

        print('target hit, straddle exited ')
        break
