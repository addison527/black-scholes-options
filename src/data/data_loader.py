import yfinance as yf
import pandas as pd

ticker="SPY"
stock = yf.Ticker(ticker)

expirations=stock.options
print(f"Expiration dates: {expirations}")

expiry = expirations[0]
option_chain = stock.option_chain(expiry)

calls = option_chain.calls
puts = option_chain.puts

print(calls.head())

#spot price
S=stock.history(period="1d")["Close"].iloc[-1]

#risk free rate (using 3-month T-bill rate)
r=0.05

#time to maturity
from datetime import datetime

expiry_datetime = datetime.strptime(expiry, "%Y-%m-%d")
T=(expiry_datetime-datetime.now()).days / 365

#strike price
K=calls.loc[10, "strike"]
sigma = calls.loc[10, "impliedVolatility"]



# stock data from yfinance, strike prices, etc
#    S: Spot price
#    K: Strike price
#    T: Time to maturity (in years)
#    r: Risk-free rate
#    sigma: Volatility