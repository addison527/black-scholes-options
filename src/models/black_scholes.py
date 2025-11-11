"""Main module for Black-Scholes option pricing functions."""
# Import a helper to fetch market data. Prefer the helper function so callers
# can explicitly fetch values where needed (and tests/mocks can replace it).
try:
    from ..data.data_loader import get_market_data
except Exception:
    try:
        from data.data_loader import get_market_data
    except Exception:
        get_market_data = None

# If available, populate module-level defaults for convenience. Callers can
# still pass explicit values to the pricing function.
if get_market_data is not None:
    try:
        S, K, T, r, sigma = get_market_data()
    except Exception:
        S = K = T = r = sigma = None
else:
    S = K = T = r = sigma = None

import numpy as np
from scipy.stats import norm


def black_scholes_price(S, K, T, r, sigma, option_type="call"):
    """
    Calculate Black-Scholes option price.

    Parameters
    - S: Spot price
    - K: Strike price
    - T: Time to maturity (in years)
    - r: Risk-free rate
    - sigma: Volatility
    - option_type: 'call' or 'put'

    Returns
    - price: Black-Scholes price for the option
    """
    # Basic validation: T and sigma must be positive to avoid division by zero
    if T is None or sigma is None:
        raise ValueError("T and sigma must be provided (not None)")
    if T <= 0 or sigma <= 0:
        raise ValueError("T and sigma must be > 0")

    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    if option_type == "call":
        price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    else:
        price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    return price
