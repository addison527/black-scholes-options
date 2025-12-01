import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime
import pandas as pd
import os

def load_spy_data():
    """
    Fetches SPY historical data, cleans it, calculates log returns and annualized volatility,
    and saves the cleaned data to a CSV file.

    Returns:
        tuple: A tuple containing:
            - pandas.DataFrame: Cleaned SPY historical data.
            - pandas.Series: Cleaned logarithmic daily returns.
            - float: Annualized volatility (calculated from cleaned log returns).
    """
    # Fetch SPY data
    spy = yf.Ticker("SPY")
    spy_data = spy.history(period="1y") # Get 1 year of historical data

    # Data Cleaning
    # Sort index
    spy_data = spy_data.sort_index()
    # Drop NaNs from spy_data
    spy_data = spy_data.dropna()

    # Calculate log returns *after* cleaning spy_data
    log_returns = np.log(spy_data['Close'] / spy_data['Close'].shift(1))
    # Drop NaNs from log_returns (the first value will be NaN)
    log_returns = log_returns.dropna()

    # Annualize volatility using the cleaned log returns
    annualized_volatility = log_returns.std() * np.sqrt(252)

    # Save cleaned data to /data/spy_clean.csv
    os.makedirs('data', exist_ok=True)
    spy_data.to_csv('data/spy_clean.csv')
    print("Cleaned SPY data saved to data/spy_clean.csv from within load_spy_data().")

    return spy_data, log_returns, annualized_volatility

# --- Input Parameters for SPY Option ---
spy_data, log_returns, annualized_volatility = load_spy_data()


print("--- Data Validation ---")

# Check spy_data DataFrame
print(f"SPY Data Shape: {spy_data.shape}")
assert spy_data.shape[0] > 0, "spy_data should have more than 0 rows"
assert 'Close' in spy_data.columns, "'Close' column missing from spy_data"
print(f"SPY Data Columns: {spy_data.columns.tolist()}")

# Check annualized_volatility type
print(f"Annualized Volatility Type: {type(annualized_volatility)}")
assert isinstance(annualized_volatility, float), "annualized_volatility should be a float"
print(f"Annualized Volatility Value: {annualized_volatility:.4f}")

print("Data validation passed successfully!")