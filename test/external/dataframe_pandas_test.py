from src.external.datatable.datatable_pandas import DataTablePandas
import unittest
import pandas as pd

class DataTablePandasTest(unittest.TestCase):

    def test_should_be_iterable(self):
        columns = ['ticker', 'operation', 'date', 'qtd', 'pm', 'fees']
        data = [['NET', 'BUY', '10/10/2020', 1, 100, 1], 
                ['NET', 'BUY', '10/10/2020', 1, 300, 0], 
        ]
        df = pd.DataFrame(data=data, columns=columns)
        sut = DataTablePandas(df)

        for x in sut:
            pass

    def test_should_create_correctly(self):

        columns = ['ticker', 'operation', 'date', 'qtd', 'pm', 'fees']
        data = [['NET', 'BUY', '10/10/2020', 1, 100, 1], 
                ['NET', 'SELL', '10/10/2020', 1, 300, 0], 
        ]
        df = pd.DataFrame(data=data, columns=columns)
        sut = DataTablePandas(df)

        row = next(sut)
        self.assertEqual('NET', row['ticker'])
        self.assertEqual('BUY', row['operation'])
        self.assertEqual('10/10/2020', row['date'])
        self.assertEqual(1, row['qtd'])
        self.assertEqual(100, row['pm'])
        
        row = next(sut)
        self.assertEqual('NET', row['ticker'])
        self.assertEqual('SELL', row['operation'])
        self.assertEqual('10/10/2020', row['date'])
        self.assertEqual(1, row['qtd'])
        self.assertEqual(300, row['pm'])