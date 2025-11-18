"""Simple runner to print Black-Scholes price for SPY using local project code.

Run from the repository root with:
    python run_price.py

This script ensures `src` is on sys.path so imports work whether or not the
package is installed.
"""
import sys
import os

# Add src directory to sys.path so imports like `data.data_loader` and
# `models.black_scholes` resolve when running this script from the repo root.
repo_root = os.path.dirname(__file__)
src_path = os.path.join(repo_root, "src")
if src_path not in sys.path:
    sys.path.insert(0, src_path)

try:
    from data.data_loader import get_market_data
except Exception:
    # Try the src package style as a fallback
    try:
        from src.data.data_loader import get_market_data
    except Exception as e:
        raise RuntimeError("Could not import get_market_data from data_loader") from e

from models.black_scholes import black_scholes_price


def main():
    S, K, T, r, sigma = get_market_data()
    price = black_scholes_price(S, K, T, r, sigma, option_type="call")
    print(f"SPY Black-Scholes call price (S={S}, K={K}, T={T:.4f}, r={r}, sigma={sigma}): {price:.4f}")


if __name__ == "__main__":
    main()
