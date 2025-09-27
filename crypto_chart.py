import requests
import matplotlib.pyplot as plt

url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
params = {"vs_currency": "usd", "days": 7}
data = requests.get(url, params=params).json()

prices = [p[1] for p in data["prices"]]
dates = [i for i in range(len(prices))]

plt.plot(dates, prices)
plt.title("Bitcoin Price (Last 7 Days)")
plt.xlabel("Time")
plt.ylabel("Price (USD)")
plt.show()
