import yfinance as yf
import pandas as pd
import datetime
msft = yf.Ticker("MSFT")
print(msft)
start = pd.to_datetime('2004-08-01')
stock = ["MSFT"]
data = yf.download(stock, start=start, end=datetime.date.today())
print(data)
#data = yf.dwonload("SPY AAPL", start = [2017-01-01], end = [2017-02-07])
