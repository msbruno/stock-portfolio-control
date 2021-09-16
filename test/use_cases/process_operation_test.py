from src.frames.dataframe_pandas import DataFramePandas, FactoryRowDataFramePandas
import pandas
from src.use_cases.process_operations import ProcessOperation
import unittest
import pandas as pd

class ProcessOperationTest(unittest.TestCase):

    def test_should_process_buy_operation(self):
        columns = ['ticker', 'operação', 'data', 'qtd', 'pm']
        data = [['NET', 'COMPRA', '10/10/2020', 1, 100], 
                ['NET', 'COMPRA', '10/10/2020', 1, 300], 
        ]
        df = pd.DataFrame(data=data, columns=columns)
        factory = FactoryRowDataFramePandas()
        pandas_df = DataFramePandas(df, factory)
        sut = ProcessOperation(pandas_df)
        sut.process_operations()

        asset = sut.portfolio_mg()._portfolio.get('NET')
        