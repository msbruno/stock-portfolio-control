from src.domain.portfolio_manager import OperationData, OperationType, PortfolioManager
from src.domain.portfolio import Portfolio
import unittest

class OpeationDataTest(unittest.TestCase):
    
    def test_should_calculate_total(self):
        quantity:int = 100
        price:int = 10
        operation:OperationData = OperationData(quantity, price, OperationType.BUY)
        self.assertEquals(1000, operation.volume()) 

class PortfolioManagerTest(unittest.TestCase):

    def test_should_add_asset_to_portfolio(self):
        portfolio = Portfolio()
        portfolio_mng = PortfolioManager(portfolio)
        portfolio_mng.execute_operation('TAEE11', OperationData(10, 1, OperationType.BUY))