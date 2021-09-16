import pandas
from src.use_cases.process_operations import ProcessOperation
import unittest
import pandas as pd

class ProcessOperationTest(unittest.TestCase):

    def test_should_process_buy_operation(self):


        pandas_df = None#PandasDataFrame(df)
        sut = ProcessOperation(pandas_df)
        sut.process_operations()