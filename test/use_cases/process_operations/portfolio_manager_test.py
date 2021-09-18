from src.use_cases.process_operations.portfolio_manager import OperationData, OperationType, PortfolioManager
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
        sut = PortfolioManager(portfolio)
        profit = sut.execute_operation('TAEE11', OperationData(10, 1, OperationType.BUY))
        self.assertEqual(0, profit.value())
        self.assertEqual(10, portfolio.get("TAEE11").shares())

    def test_should_sell_asset_from_portfolio(self):
        portfolio, sut = self._make_sut()
        profit = sut.execute_operation('TAEE11', OperationData(5, 5, OperationType.SELL))
        self.assertEqual(-25, profit.value())
        self.assertEqual(5, portfolio.get("TAEE11").shares())

    def test_should_sell_asset_from_portfolio(self):
        portfolio, sut = self._make_sut()
        profit = sut.execute_operation('TAEE11', OperationData(5, 5, OperationType.SELL))
        self.assertEqual(-25, profit.value())
        self.assertEqual(5, portfolio.get("TAEE11").shares())

    def _make_sut(self):
        portfolio = Portfolio()
        portfolio_mng = PortfolioManager(portfolio)
        profit = portfolio_mng.execute_operation('TAEE11', OperationData(10, 10, OperationType.BUY))
        self.assertTrue(portfolio.has("TAEE11"))
        return portfolio,portfolio_mng