import pandas as pd
import pdb


nifty50 = ['ADANIPORTS', 'ASIANPAINT', 'AXISBANK', 'BAJAJ-AUTO', 'BAJFINANCE', 'BAJAJFINSV', 'BPCL', 'BHARTIARTL', 'BRITANNIA', 'CIPLA', 'COALINDIA', 'DIVISLAB', 'DRREDDY', 'EICHERMOT', 'GAIL', 'GRASIM', 'HCLTECH', 'HDFCBANK', 'HDFCLIFE', 'HEROMOTOCO', 'HINDALCO', 'HINDUNILVR', 'HDFC', 'ICICIBANK', 'ITC', 'IOC', 'INDUSINDBK', 'INFY', 'JSWSTEEL', 'KOTAKBANK', 'LT', 'M&M', 'MARUTI', 'NTPC', 'NESTLEIND', 'ONGC', 'POWERGRID', 'RELIANCE', 'SBILIFE', 'SHREECEM', 'SBIN', 'SUNPHARMA', 'TCS', 'TATAMOTORS', 'TATASTEEL', 'TECHM', 'TITAN', 'UPL', 'ULTRACEMCO', 'WIPRO']

nse_file_link = 'https://www1.nseindia.com/archives/nsccl/volt/CMVOLT_15112021.CSV'
nse_file = pd.read_csv(nse_file_link)


nse_file = nse_file[nse_file['Symbol'].isin(nifty50)]

nse_file['nse_daily_pct'] = nse_file['Current Day Underlying Daily Volatility (E) = Sqrt(0.995*D*D + 0.005*C*C)']
nse_file['daily_volatality'] = pd.to_numeric(nse_file['nse_daily_pct'])*100
nse_file = nse_file.sort_values(by=['daily_volatality'], ascending=False)

nse_file.head(30).to_csv('Best_stocks_to_trade_today.csv')


