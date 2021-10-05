from src.external.datatable.datatable_loader import FactoryDataTablePandas
from src.external.datatable.mappers import DEFAULT_COLUMN_MAPPER_EN, OPERATION_MAPPER, DEFAULT_COLUMN_MAPPER_BR
from src.use_cases.process_operations.portfolio_manager import OperationType
from src.use_cases.interfaces.datatable import Row
from src.external.datatable.datatable_pandas import DataTablePandas, RowPandas
import unittest
import pandas as pd

class FactoryDataTablePandasTest(unittest.TestCase):

    def test_should_convert_columns_correctly(self):
        columns = ['ticker', 'operation', 'date', 'qt', 'mp', 'fee']
        data = [['NET', 'BUY', '10/10/2020', 1, 100, 1], 
                ['NET', 'BUY', '10/10/2020', 1, 300, 0], 
        ]
        df = pd.DataFrame(data=data, columns=columns)
        sut = FactoryDataTablePandas(DEFAULT_COLUMN_MAPPER_EN, ';', '%d/%m/%Y')
        result = sut.wrap(df)
        print(result['mp'])
        


class RowPandasTest(unittest.TestCase):

    def test_should_create_correctly(self):
        data = ['NET', 'BUY', '10/10/2020', 1, 100, 1]
        row = self._create_row(data)

        row:Row = RowPandas(1, row)
        self.assertEqual('NET', row['ticker'])
        self.assertEqual('BUY', row['operation'])
        self.assertEqual('10/10/2020', row['date'])
        self.assertEqual(1, row['qtd'])
        self.assertEqual(100, row['pm'])

    def _create_row(self, data):
        columns = ['ticker', 'operation', 'date', 'qtd', 'pm', 'fees']
        data = [data]
        df = pd.DataFrame(data=data, columns=columns)
        row = df.iloc[0]
        return row

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