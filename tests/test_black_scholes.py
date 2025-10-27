import unittest
from src.black_scholes import black_scholes_price

class TestBlackScholes(unittest.TestCase):
    def test_call_option(self):
        price = black_scholes_price(100, 100, 1, 0.05, 0.2, "call")
        self.assertAlmostEqual(price, 10.4506, places=4)

    def test_put_option(self):
        price = black_scholes_price(100, 100, 1, 0.05, 0.2, "put")
        self.assertAlmostEqual(price, 5.5735, places=4)

if __name__ == "__main__":
    unittest.main()
