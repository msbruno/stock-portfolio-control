from src.external.datatable.mappers import OPERATION_MAPPER, DEFAULT_COLUMN_MAPPER
from src.use_cases.process_operations.portfolio_manager import OperationType
from src.use_cases.interfaces.datatable import Row
from src.external.datatable.datatable_pandas import DataTablePandas, RowPandas
import unittest
import pandas as pd


class FactoryRowdateFramePandasTest(unittest.TestCase):

    def test_should_create_correctly(self):
        date = ['NET', 'BUY', '10/10/2020', 1, 100, 1]
        row = self._create_row(date)

        row:Row = RowPandas(1, row)
        self.assertEqual('NET', row['ticker'])
        self.assertEqual('BUY', row['operation'])
        self.assertEqual('10/10/2020', row['date'])
        self.assertEqual(1, row['qtd'])
        self.assertEqual(100, row['pm'])

    def _create_row(self, date):
        columns = ['ticker', 'operation', 'date', 'qtd', 'pm', 'fees']
        date = [date]
        df = pd.DataFrame(data=date, columns=columns)
        row = df.iloc[0]
        return row

class dateFramePandasTest(unittest.TestCase):

    def test_should_be_iterable(self):
        columns = ['ticker', 'operation', 'date', 'qtd', 'pm', 'fees']
        date = [['NET', 'BUY', '10/10/2020', 1, 100, 1], 
                ['NET', 'BUY', '10/10/2020', 1, 300, 0], 
        ]
        df = pd.DataFrame(data=date, columns=columns)
        sut = DataTablePandas(df)

        for x in sut:
            pass

    def test_should_create_correctly(self):

        columns = ['ticker', 'operation', 'date', 'qtd', 'pm', 'fees']
        date = [['NET', 'BUY', '10/10/2020', 1, 100, 1], 
                ['NET', 'SELL', '10/10/2020', 1, 300, 0], 
        ]
        df = pd.DataFrame(data=date, columns=columns)
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