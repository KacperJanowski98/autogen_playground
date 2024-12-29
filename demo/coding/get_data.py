# filename: get_data.py

import yfinance as yf
from datetime import datetime, timedelta

# Get the current date in YYYY-MM-DD format
today = datetime.today().strftime('%Y-%m-%d')

# Start of year (2024-01-01)
start_date = '2024-01-01'

stocks = ['NVDA', 'TSLA']
dataframes = []

for stock in stocks:
    # Download the historical data for each stock since start date to current date
    df = yf.download(stock, start=start_date, end=today)
    dataframes.append(df)

print("Downloaded history for: ", ', '.join(stocks))