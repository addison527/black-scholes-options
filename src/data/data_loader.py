import yfinance as yf
import pandas as pd

import yfinance as yf
import pandas as pd
from datetime import datetime


def get_market_data(ticker: str = "SPY", expiry_index: int = 0, risk_free_rate: float = 0.05):
	"""Fetch market data needed for option pricing.

	Parameters
	- ticker: ticker symbol to fetch (default: 'SPY')
	- expiry_index: which expiry to use from the chain (0 = nearest)
	- risk_free_rate: fallback / assumed risk-free rate

	Returns
	(S, K, T, r, sigma)
	"""
	stock = yf.Ticker(ticker)

	expirations = stock.options
	if not expirations:
		raise ValueError(f"No option expirations found for ticker {ticker}")

	expiry = expirations[expiry_index]
	option_chain = stock.option_chain(expiry)

	calls = option_chain.calls
	puts = option_chain.puts

	# Spot price
	S = stock.history(period="1d")["Close"].iloc[-1]

	# Risk-free rate (simple fallback)
	r = risk_free_rate

	# Time to maturity (in years)
	expiry_datetime = datetime.strptime(expiry, "%Y-%m-%d")
	T = (expiry_datetime - datetime.now()).days / 365

	# Choose a strike and implied vol — use a safe fallback if table shorter
	if len(calls) > 10:
		K = calls.loc[10, "strike"]
		sigma = calls.loc[10, "impliedVolatility"]
	elif len(calls) > 0:
		K = calls.iloc[0]["strike"]
		sigma = calls.iloc[0]["impliedVolatility"]
	else:
		raise ValueError("No call option data available to determine strike/vol")

	return S, K, T, r, sigma


# Maintain backwards compatibility: populate module-level names when imported
try:
	S, K, T, r, sigma = get_market_data()
except Exception:
	# If fetching fails (network/offline), leave variables as None so callers
	# can still call functions by passing explicit arguments.
	S = K = T = r = sigma = None