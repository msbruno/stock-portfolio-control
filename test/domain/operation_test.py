from src.domain.operation import SellOperationProfit, SellOperation
from src.domain.asset import Asset
import unittest

class AssetTest(unittest.TestCase):

    def test_should_be_create_correctly(self):
        asset = Asset("TAEE11", 20, 10)
        self.assertEquals(20, asset.shares())
        self.assertEqual(200, asset.value())

class SellOperationTest(unittest.TestCase):
    def test_should_sell_correctly(self):
        asset = Asset("TAEE11", 30, 10.0)
        sell_operation = SellOperation(0,0) 
        sell_operation.execute_on(asset) 
        self.assertEquals(30, asset.shares())
        self.assertEquals(10.0, asset.mean_price())

        sell_operation = SellOperation(10,5) 
        sell_operation.execute_on(asset)
        self.assertEquals(20, asset.shares())
        self.assertEquals(10.0, asset.mean_price())
        self.assertEquals(-50.0, asset.profit())

    def test_should_raise_exception_when_try_to_sell_more_shares_than_have(self):
        asset = Asset("TAEE11", 30, 10.0)
        sell_operation = SellOperation(50,1) 
        with self.assertRaises(Exception) as context:
            sell_operation.execute_on(asset)
        self.assertTrue("You are trying to sell more TAEE11 than you have." in str(context.exception))

class OperationProfitTest(unittest.TestCase):
    def test_should_calculate_loss(self):
        asset = Asset("TAEE11", 30, 20.0)
        operation_profit = SellOperationProfit(asset, 25, 10) 
        self.assertEqual(-250, operation_profit.value())
