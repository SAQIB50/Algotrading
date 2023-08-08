import angel_file as taf

angel = taf.angel


ohlc1 = taf.get_ohlc(name='ACC-EQ', exchange='NSE')
ohlc2 = taf.get_ohlc(name="ASHOKLEY",exchange="BSE")
# ohlc3 = taf.get_ohlc(name="ACC28OCT23FUT",exchange="NFO")
# ohlc4 = taf.get_ohlc(name="BANKNIFTY07OCT2139000PE",exchange="NFO")
# ohlc5 = taf.get_ohlc(name="ALUMINIUM21OCTFUT",exchange="MCX")
# ohlc6 = taf.get_ohlc(name="EURINR21O2982PE",exchange="CDS")


print(ohlc1)
print(ohlc2)
# print(ohlc3)
# print(ohlc4)
# print(ohlc5)
# print(ohlc6)