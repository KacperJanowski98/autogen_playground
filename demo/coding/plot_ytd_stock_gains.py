# filename: plot_ytd_stock_gains.py

import yfinance as yf
from datetime import datetime

# Start and end dates
today = '2024-12-29'
start_date = '2024-01-01'

stocks = ['NVDA', 'TSLA']
dataframes = {}

for stock in stocks:
    # Download the historical data for each stock since start date to current date
    df = yf.download(stock, start=start_date, end=today)
    dataframes[stock] = df

# Calculate cumulative daily return from closing price (approximation of stock gain)
cumulative_gains_dict = {}
for symbol, df in dataframes.items():
    # Reset index to convert date column back to index and drop the old index
    gains_df = df['Close'].reset_index(drop=True)
    gains_df.fillna(method='ffill', inplace=True)  # Replace NaN values with forward fill (last valid observation)

    cumulative_gains_dict[symbol] = ((gains_df.pct_change() + 1).cumprod()) * 100

# Plot
plt.figure(figsize=(8,6))
for stock in stocks:
    plt.plot(cumulative_gains_dict[stock], label=stock)
    
plt.title('YTD Stock Gains')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns (%)')
plt.legend()
plt.tight_layout()

plt.savefig('ytd_stock_gains.png')
print("Saved YTD stock gains chart to file ytd_stock_gains.png")