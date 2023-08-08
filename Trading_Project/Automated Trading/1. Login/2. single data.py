import angel_file as taf
angel = taf.angel


ltp = taf.get_ltp(name='ZEEL-EQ', exchange='NSE')
print('ZEEL' , ltp)



ohlc = taf.get_ohlc(name='ACC-EQ', exchange='NSE')
print('ACC' , ohlc)