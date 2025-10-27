"""
Utility functions for Black-Scholes project.
"""
import numpy as np

def annualize_volatility(daily_vol, trading_days=252):
    """
    Convert daily volatility to annual volatility.
    """
    return daily_vol * np.sqrt(trading_days)
