from src.domain.portfolio import Portfolio, PortfolioManager, OperationType, OperationData
from src.domain.asset import Asset
import unittest

class OpeationDataTest(unittest.TestCase):
    
    def test_should_calculate_total(self):
        quantity:int = 100
        price:int = 10
        operation:OperationData = OperationData(quantity, price, OperationType.BUY)
        self.assertEquals(1000, operation.volume()) 

class PortfolioTest(unittest.TestCase):

    def test_should_add_asset(self):
        asset = Asset("TAEE11", 20, 10)
        portfolio = Portfolio()
        portfolio.add(asset)
        self.assertEqual(asset, portfolio.get("TAEE11"))

class PortfolioManagerTest(unittest.TestCase):

    def test_should_add_asset_to_portfolio(self):
        portfolio = Portfolio()
        portfolio_mng = PortfolioManager(portfolio)
        portfolio_mng.execute_operation('TAEE11', OperationData(10, 1, OperationType.BUY))