from src.controller.result_entry import ResultEntry
from src.domain.operation import OperationData
import unittest 

class ResultTest(unittest.TestCase):

    def test_should_calculate_deltas_when_liquidated(self):
        buy = OperationData(100, 10)
        sell = OperationData(100, 10)
        result = ResultEntry(buy, sell)
        self.assertEquals(0, result.delta_value())
        self.assertEquals(0, result.delta_quantity())
