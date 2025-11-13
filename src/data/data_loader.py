import yfinance as yf
import pandas as pd
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

S = spy_data['Close'].iloc[-1] # Current SPY price
K = 550 # Example Strike Price
expiration_date = datetime(2025, 12, 19) # Example Expiration Date
valuation_date = datetime.now()
T = (expiration_date - valuation_date).days / 365.0 # Time to expiration in years
r = 0.04 # Risk-free rate (e.g., current U.S. 10-year treasury yield)
sigma = annualized_volatility # Volatility of SPY
option_type = 'call' # Type of option (call or put)

print(f"Current SPY Price (S): {S:.2f}")
print(f"Strike Price (K): {K:.2f}")
print(f"Time to Expiration (T): {T:.2f} years")
print(f"Risk-free Rate (r): {r:.4f}")
print(f"Estimated Annualized Volatility (sigma): {sigma:.4f}")
print(f"Option Type: {option_type.capitalize()}")

# Calculate option price
option_price = black_scholes(S, K, T, r, sigma, option_type)

print(f"\nBlack-Scholes {option_type.capitalize()} Option Price: {option_price:.2f}")
