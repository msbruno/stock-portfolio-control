from src.domain.operation import BuyOperation, ReverseSplitOperation, SellOperationProfit, SellOperation,SplitOperation
from src.domain.asset import Asset
import unittest

class SellOperationProfitTest(unittest.TestCase):
    def test_should_calculate_loss(self):
        asset = Asset("TAEE11", 30, 5000)
        operation_profit = SellOperationProfit(asset, 30, 2500) 
        self.assertEqual(-2500, operation_profit.value())

class SellOperationTest(unittest.TestCase):
    def test_should_sell_correctly(self):
        asset = Asset("TAEE11", 20, 1000.0)
        sell_operation = SellOperation(0,0) 
        sell_operation.execute_on(asset) 
        self.assertEquals(20, asset.shares())
        self.assertEquals(50.0, asset.mean_price())

        sell_operation = SellOperation(10, 250.0) 
        sell_operation.execute_on(asset)
        self.assertEquals(10, asset.shares())
        self.assertEquals(50.0, asset.mean_price())
        self.assertEquals(-250.0, asset.profit())

    def test_should_raise_exception_when_try_to_sell_more_shares_than_have(self):
        asset = Asset("TAEE11", 30, 10.0)
        sell_operation = SellOperation(50,1) 
        with self.assertRaises(Exception) as context:
            sell_operation.execute_on(asset)
        self.assertTrue("You are trying to sell more value of TAEE11 than you have." in str(context.exception))

class BuyOperationTest(unittest.TestCase):

    def test_should_buy_correctly(self):
        asset = Asset("TAEE11", 30, 9000.0)
        buy_operation = BuyOperation(30, 3000.0) 
        profit = buy_operation.execute_on(asset) 
        self.assertEqual(0, profit.value())
        self.assertEquals(60, asset.shares())
        self.assertEquals(12000, asset.value())
        self.assertEquals(200.0, asset.mean_price())

class SplitOperationTest(unittest.TestCase):
    
    def test_should_split_correctly(self):
        asset = Asset("TAEE11", 30, 30000.0)
        split_operation = SplitOperation(2)
        split_operation.execute_on(asset)
        self.assertEqual(60, asset.shares())
        self.assertEqual(30000.0, asset.value())
        self.assertEqual(30000.0, asset.mean_price())

class ReverseSplitOperationTest(unittest.TestCase):
    def test_should_group_corretly(self):
        asset = Asset("TAEE11", 30, 30000.0)
        split_operation = ReverseSplitOperation(2)
        split_operation.execute_on(asset)
        self.assertEqual(15, asset.shares())
        self.assertEqual(30000.0, asset.value())