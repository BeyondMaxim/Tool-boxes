import requests

api_key = "P1KIEEBOYPZK5DYV"
from_currency = "BTC"  # Replace with the desired cryptocurrency symbol
to_currency = "USD"
base_url = "https://www.alphavantage.co/query"

# Function to retrieve historical data for a cryptocurrency pair
def get_historical_data(symbol):
    function = "DIGITAL_CURRENCY_DAILY"
    market = "USD"
    page_size = 100

    # Parameters for the API request
    params = {
        "function": function,
        "symbol": symbol,
        "market": market,
        "apikey": api_key,
        "outputsize": "full",
    }

    try:
        # Sending the initial request
        response = requests.get(base_url, params=params)
        data = response.json()

        # Extracting the historical data
        time_series = data["Time Series (Digital Currency Daily)"]

        # Iterate over all pages of data
        while "has_more_pages" in data and data["has_more_pages"]:
            # Get the last timestamp in the current data set
            last_timestamp = max(time_series.keys())

            # Set the new parameter for the next request with pagination
            params["outputsize"] = "compact"
            params["end_date"] = last_timestamp

            # Send the next request
            response = requests.get(base_url, params=params)
            data = response.json()

            # Extend the time series with the new data
            time_series.update(data["Time Series (Digital Currency Daily)"])

        # Print the data for the latest date
        latest_date = max(time_series.keys())
        print(f"Latest date: {latest_date}")
        print(f"Open price: {time_series[latest_date]['1a. open ({market})']}")
        print(f"High price: {time_series[latest_date]['2a. high ({market})']}")
        print(f"Low price: {time_series[latest_date]['3a. low ({market})']}")
        print(f"Close price: {time_series[latest_date]['4a. close ({market})']}")
        print(f"Volume: {time_series[latest_date]['5. volume']}")

    except KeyError:
        print("Error in retrieving data. Please check the symbol and API key.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Call the function with the desired cryptocurrency symbol
get_historical_data(symbol)