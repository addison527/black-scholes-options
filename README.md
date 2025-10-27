# Black-Scholes Option Pricing

A quantitative Python implementation of the Black-Scholes option pricing algorithm.

## Features
- European call and put option pricing
- Utility functions for volatility conversion
- Unit tests for core pricing logic

## Usage
Install dependencies:
```
pip install -r requirements.txt  # do this first!
```
Run tests:
```
python -m unittest discover tests
```
Example usage:
```python
from src.black_scholes import black_scholes_price
price = black_scholes_price(100, 100, 1, 0.05, 0.2, "call")
print(price)
```

## Struc
quant-options-pricing/
├── README.md
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── data/
│   │   ├── data_loader.py        # Get market data for testing
│   ├── models/
│   │   ├── black_scholes.py      # Core pricing model
│   │   ├── greeks.py             # Delta, Gamma, Vega, etc.
│   │   ├── implied_volatility.py # Optional later feature
│   └── main.py                   # Runs the model end-to-end
├── notebooks/
│   ├── bs_pricing_examples.ipynb
│   └── volatility_surface.ipynb
└── docs/
    └── project_plan.md

## Background

Greeks measure how sensitive an option’s price is to changes in market variables:
Delta (Δ) Change in the underlying asset’s price (S)
Gamma (Γ) Change in Delta when the stock price changes
Vega (ν) Change in price due to volatility (σ)
Theta (Θ) Change in price with time decay
Rho (ρ) Change in price with interest rate (r)

## .gitignore

# Python cache files
__pycache__/
*.pyc
*.pyo

# Jupyter Notebook checkpoints
.ipynb_checkpoints/

# Data files (optional, if you don’t want to commit)
data/

# Environment / config files
.env

# OS files
.DS_Store
Thumbs.db


## -------
