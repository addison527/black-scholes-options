import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime

# --- Input Parameters for SPY Option ---
# Fetch SPY data
spy = yf.Ticker("SPY")
spy_data = spy.history(period="1y") # Get 1 year of historical data

# Calculate implied volatility from historical data (simple annualized standard deviation of daily returns)
# This is a simplification; actual implied volatility is derived from market prices.
log_returns = np.log(spy_data['Close'] / spy_data['Close'].shift(1))
# Annualize volatility assuming 252 trading days in a year
annualized_volatility = log_returns.std() * np.sqrt(252)