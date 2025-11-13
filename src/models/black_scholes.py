import numpy as np
import scipy.stats as si

def black_scholes(S, K, T, r, sigma, option_type):
    """
    Calculates the Black-Scholes option price.

    Args:
        S (float): Current stock price.
        K (float): Option strike price.
        T (float): Time to expiration (in years).
        r (float): Risk-free interest rate (annualized).
        sigma (float): Volatility of the underlying asset (annualized).
        option_type (str): 'call' or 'put'.

    Returns:
        float: Option price.
    """
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == 'call':
        price = (S * si.norm.cdf(d1, 0.0, 1.0) - K * np.exp(-r * T) * si.norm.cdf(d2, 0.0, 1.0))
    elif option_type == 'put':
        price = (K * np.exp(-r * T) * si.norm.cdf(-d2, 0.0, 1.0) - S * si.norm.cdf(-d1, 0.0, 1.0))
    else:
        raise ValueError("option_type must be 'call' or 'put'")

    return price