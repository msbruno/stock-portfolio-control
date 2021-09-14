from src.controller.result_entry import ResultEntry
from src.domain.operation import Operation
import unittest

class ResultTest(unittest.TestCase):

    def test_should_calculate_deltas_when_liquidated(self):
        buy = Operation(100, 10)
        sell = Operation(100, 10)
        result = ResultEntry(buy, sell)
        self.assertEquals(0, result.delta_value())
        self.assertEquals(0, result.delta_quantity())

    def test_should_calculate_mean_price(self):
        buy = Operation(100, 10)
        sell = Operation(50, 5)
        result = ResultEntry(buy, sell)
        self.assertEquals(50, result.delta_quantity())
        self.assertEquals(50, result.delta_value())