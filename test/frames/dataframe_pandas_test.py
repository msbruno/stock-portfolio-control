from src.use_cases.interfaces.dataframe import DataFrameRow
from src.frames.dataframe_pandas import DataFramePandas, FactoryRowDataFramePandas
import unittest
import pandas as pd


class RowDataFramePandasTest(unittest.TestCase):

    def test_should_create_(self):
        data = ['NET', 'COMPRA', '10/10/2020', 1, 100]
        row = self._create_row(data)

        sut = FactoryRowDataFramePandas()
        row:DataFrameRow = sut.create(1, row)
        self.assertEqual('NET', row.ticker())
        self.assertEqual('COMPRA', row.operation())
        self.assertEqual('10/10/2020', row.data())
        self.assertEqual(1, row.quantity())
        self.assertEqual(100, row.mean_price())

    def _create_row(self, data):
        columns = ['ticker', 'operação', 'data', 'qtd', 'pm']
        data = [data]
        df = pd.DataFrame(data=data, columns=columns)
        row = df.iloc[0]
        return row

class DataFramePandasTest(unittest.TestCase):

    def test_should_create_correctly(self):

        columns = ['ticker', 'operação', 'data', 'qtd', 'pm']
        data = [['NET', 'COMPRA', '10/10/2020', 1, 100], 
                ['NET', 'COMPRA', '10/10/2020', 1, 300], 
                ['NET', 'COMPRA', '10/10/2020', 1, 150], 
        ]
        df = pd.DataFrame(data=data, columns=columns)
        factory = FactoryRowDataFramePandas()
        sut = DataFramePandas(df, factory)
        row = sut.next_row()

        self.assertEqual('NET', row.ticker())
        self.assertEqual('COMPRA', row.operation())
        self.assertEqual('10/10/2020', row.data())
        self.assertEqual(1, row.quantity())
        self.assertEqual(100, row.mean_price())
        
        pass