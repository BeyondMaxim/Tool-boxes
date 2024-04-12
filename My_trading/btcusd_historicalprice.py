# Import necessary libraries
import yfinance as yf

# Define the stock symbol and timeframe for BTCUSD
stock_symbol = 'btc-usd'  # Bitcoin to USD
start_date = '2022-01-01'
end_date = '2022-12-31'

# Fetch historical BTCUSD price data using yfinance
btcusd_data = yf.download(tickers = stock_symbol, start=start_date, end=end_date)

# Display the historical BTCUSD price data
print(btcusd_data)
