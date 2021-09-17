from src.frames.dataframe_pandas import DataFramePandas, FactoryRowDataFramePandas
from src.use_cases.process_operations import ProcessOperation
import unittest
import pandas as pd

class ProcessOperationTest(unittest.TestCase):

    def test_should_process_buy_operation(self):
        columns = ['data', 'ticker', 'operação', 'qtd', 'pm']
        data = [['10/10/2020', 'NET', 'COMPRA', 5, 100], 
                ['10/10/2020', 'NET', 'COMPRA', 5, 300], 
                ['10/10/2020', 'NET', 'VENDA', 2, 100], 
        ]
        df = pd.DataFrame(data=data, columns=columns)
        factory = FactoryRowDataFramePandas()
        pandas_df = DataFramePandas(df, factory)
        sut = ProcessOperation(pandas_df)
        sut.process_operations()

        asset = sut.portfolio_mg()._portfolio.get('NET')
        self.assertEqual('NET', asset.ticker())
        self.assertEqual(8, asset.shares())
        self.assertEqual(200, asset.mean_price())
        self.assertEqual(-200, asset.profit())