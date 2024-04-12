from tradingview_ta import TA_Handler, Interval

# Define the symbol and exchange
symbol = "SOLUSDT"
exchange = "BINANCE"

# Create a TA_Handler instance with symbol and exchange parameters
ta_handler_15min = TA_Handler(symbol=symbol, exchange=exchange, screener="crypto", interval=Interval.INTERVAL_15_MINUTES)
ta_handler_30min = TA_Handler(symbol=symbol, exchange=exchange, screener="crypto", interval=Interval.INTERVAL_30_MINUTES)
ta_handler_1hour = TA_Handler(symbol=symbol, exchange=exchange, screener="crypto", interval=Interval.INTERVAL_1_HOUR)
ta_handler_4hour = TA_Handler(symbol=symbol, exchange=exchange, screener="crypto", interval=Interval.INTERVAL_4_HOURS)

# Get technical analysis data for the symbol at different intervals
ta_data_15min = ta_handler_15min.get_analysis()
ta_data_30min = ta_handler_30min.get_analysis()
ta_data_1hour = ta_handler_1hour.get_analysis()
ta_data_4hour = ta_handler_4hour.get_analysis()

# Extract buy/sell signals from the technical analysis data for each interval
buy_signal_15min = ta_data_15min.summary['RECOMMENDATION']
sell_signal_15min = ta_data_15min.summary['RECOMMENDATION']

buy_signal_30min = ta_data_30min.summary['RECOMMENDATION']
sell_signal_30min = ta_data_30min.summary['RECOMMENDATION']

buy_signal_1hour = ta_data_1hour.summary['RECOMMENDATION']
sell_signal_1hour = ta_data_1hour.summary['RECOMMENDATION']


buy_signal_4hour = ta_data_4hour.summary['RECOMMENDATION']
sell_signal_4hour = ta_data_4hour.summary['RECOMMENDATION']
# Print the buy and sell signals for each interval
print("15 Minutes Interval:")
print(f"Buy Signal: {buy_signal_15min}")
print(f"Sell Signal: {sell_signal_15min}")

print("\n30 Minutes Interval:")
print(f"Buy Signal: {buy_signal_30min}")
print(f"Sell Signal: {sell_signal_30min}")

print("\n1 Hour Interval:")
print(f"Buy Signal: {buy_signal_1hour}")
print(f"Sell Signal: {sell_signal_1hour}")

print("\n4 Hour Interval:")
print(f"Buy Signal: {buy_signal_4hour}")
print(f"Sell Signal: {sell_signal_4hour}")
