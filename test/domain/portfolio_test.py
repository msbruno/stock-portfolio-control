from src.domain.portfolio import Portfolio
from src.domain.asset import Asset
import unittest

class PortfolioTest(unittest.TestCase):

    def test_should_add_asset(self):
        asset = Asset("TAEE11", 20, 10)
        portfolio = Portfolio()
        portfolio.add(asset)
        self.assertEqual(asset, portfolio.get("TAEE11"))