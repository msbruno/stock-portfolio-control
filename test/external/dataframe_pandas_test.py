from src.external.datatable.mappers import OPERATION_MAPPER, DEFAULT_COLUMN_MAPPER
from src.use_cases.process_operations.portfolio_manager import OperationType
from src.use_cases.interfaces.datatable import DataTableRow
from src.external.datatable.datatable_pandas import OperationsDataTablePandas, FactoryRowDataTablePandas
import unittest
import pandas as pd


class FactoryRowDataFramePandasTest(unittest.TestCase):

    def test_should_create_correctly(self):
        data = ['NET', 'COMPRA', '10/10/2020', 1, 100]
        row = self._create_row(data)

        sut = FactoryRowDataTablePandas(OPERATION_MAPPER, DEFAULT_COLUMN_MAPPER)
        row:DataTableRow = sut.create(1, row)
        self.assertEqual('NET', row.ticker())
        self.assertEqual(OperationType.BUY, row.operation())
        self.assertEqual('10/10/2020', row.data())
        self.assertEqual(1, row.shares())
        self.assertEqual(100, row.mean_price())

    def _create_row(self, data):
        columns = ['ticker', 'operação', 'data', 'qtd', 'pm']
        data = [data]
        df = pd.DataFrame(data=data, columns=columns)
        row = df.iloc[0]
        return row

class DataFramePandasTest(unittest.TestCase):

    def test_should_be_iterable(self):
        columns = ['ticker', 'operação', 'data', 'qtd', 'pm']
        data = [['NET', 'COMPRA', '10/10/2020', 1, 100], 
                ['NET', 'COMPRA', '10/10/2020', 1, 300], 
        ]
        df = pd.DataFrame(data=data, columns=columns)
        factory = FactoryRowDataTablePandas(OPERATION_MAPPER, DEFAULT_COLUMN_MAPPER)
        sut = OperationsDataTablePandas(df, factory)

        for x in sut:
            pass

    def test_should_create_correctly(self):

        columns = ['ticker', 'operação', 'data', 'qtd', 'pm']
        data = [['NET', 'COMPRA', '10/10/2020', 1, 100], 
                ['NET', 'VENDA', '10/10/2020', 1, 300], 
        ]
        df = pd.DataFrame(data=data, columns=columns)
        factory = FactoryRowDataTablePandas(OPERATION_MAPPER, DEFAULT_COLUMN_MAPPER)
        sut = OperationsDataTablePandas(df, factory)

        row = next(sut)
        self.assertEqual('NET', row.ticker())
        self.assertEqual(OperationType.BUY, row.operation())
        self.assertEqual('10/10/2020', row.data())
        self.assertEqual(1, row.shares())
        self.assertEqual(100, row.mean_price())
        
        row = next(sut)
        self.assertEqual('NET', row.ticker())
        self.assertEqual(OperationType.SELL, row.operation())
        self.assertEqual('10/10/2020', row.data())
        self.assertEqual(1, row.shares())
        self.assertEqual(300, row.mean_price())