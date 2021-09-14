from src.domain.operation import Asset, Operation, Portfolio, SellOperationProfit
import unittest


class OpeationTest(unittest.TestCase):
    
    def test_should_calculate_total(self):
        quantity:int = 100
        price:int = 10
        buy_operation:Operation = Operation(quantity, price)
        self.assertEquals(1000, buy_operation.volume()) 

class OperationProfitTest(unittest.TestCase):
    def test_should_calculate_loss(self):
        sell_operation:Operation = Operation(10, 25)
        operation_profit = SellOperationProfit(50, sell_operation)
        self.assertEqual(-250, operation_profit.value())

class AssetTest(unittest.TestCase):

    def test_should_split_correctly(self):
        asset = Asset("TAEE11", 20, 10)
        asset.split(5)
        self.assertEquals(100, asset.quantity())
    
    def test_should_sell_correctly(self):
        asset = Asset("TAEE11", 30, 10.0)
        asset.sell(Operation(0,0))
        self.assertEquals(30, asset.quantity())
        self.assertEquals(10.0, asset.mean_price())

        asset.sell(Operation(10,5))
        self.assertEquals(20, asset.quantity())
        self.assertEquals(10.0, asset.mean_price())
        self.assertEquals(-50.0, asset.profit())

    def test_should_calculate_loss(self):
        asset = Asset("TAEE11", 10, 50)
        sell_operation:Operation = Operation(10, 25)
        operation_profit = asset.sell(sell_operation)
        self.assertEqual(-250, operation_profit.value())


    def test_should_buy_correctly(self):
        asset = Asset("TAEE11", 30, 10)
        asset.buy(Operation(0,0))
        self.assertEquals(30, asset.quantity())

        asset.buy(Operation(20,5))
        self.assertEquals(50, asset.quantity())
        self.assertEquals(8.0, asset.mean_price())
        self.assertEquals(0, asset.profit())

class PortfolioTest(unittest.TestCase):

    def test_should_add_asset(self):
        asset = Asset("TAEE11", 20, 10)
        portfolio = Portfolio()
        portfolio.add(asset)

        self.assertEqual(asset, portfolio.get("TAEE11"))
