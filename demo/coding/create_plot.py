# filename: create_plot.py

import pandas as pd
import matplotlib.pyplot as plt

# Calculate cumulative daily return from closing price (approximation of stock gain)
# Cumulative daily returns can be used to represent YTD growth for visualization purposes.
cumulative_gains = {}
for stock in dataframes:
    # Reset index to convert date column back to index and drop the old index
    gains_df = stock['Close'].reset_index(drop=True)
    gains_df.fillna(method='ffill', inplace=True)  # Replace NaN values with forward fill (last valid observation)

    cumulative_gains[stock.columns.name] = ((gains_df.pct_change() + 1).cumprod()) * 100

# Plot
plt.figure(figsize=(8,6))
for stock in stocks:
    plt.plot(cumulative_gains[stock], label=stock)
    
plt.title('YTD Stock Gains')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns (%)')
plt.legend()
plt.tight_layout()

plt.savefig('ytd_stock_gains.png')
print("Saved YTD stock gains chart to file ytd_stock_gains.png")