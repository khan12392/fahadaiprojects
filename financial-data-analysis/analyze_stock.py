import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('sample_stock_data.csv')
df['Date'] = pd.to_datetime(df['Date'])

# Calculate daily returns
df['Daily_Return'] = df['Close'].pct_change() * 100

# Print summary statistics
print("=== Stock Data Summary ===")
print(df[['Open', 'High', 'Low', 'Close']].describe())
print("\n=== Daily Returns ===")
print(df[['Date', 'Close', 'Daily_Return']])

# Plot closing price
plt.figure(figsize=(10, 5))
plt.plot(df['Date'], df['Close'], marker='o', color='blue')
plt.title('AAPL Closing Price')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.grid(True)
plt.tight_layout()
plt.savefig('closing_price_chart.png')
print("\nChart saved as closing_price_chart.png")
