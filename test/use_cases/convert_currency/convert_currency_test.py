import unittest
from src.external.datatable.pandas_loader import PandasLoader
from src.external.datatable.datatable_pandas import DataTablePandas
from src.external.datatable.mappers import DEFAULT_COLUMN_MAPPER_BR
from src.use_cases.convert_currency.convert_currency import ConvertCurrency

from test.resources.load_file import path_resource



class ConvertCurrencyTest(unittest.TestCase):

    def test_convert_currency(self):
        data_operations = self.operations()
        sut = ConvertCurrency(DEFAULT_COLUMN_MAPPER_BR)
        result = sut.convert(data_operations)
        print(result['pm'])
        
    
    def operations(self)->DataTablePandas:
        path_operations = path_resource('portfolio.csv')
        path_types = path_resource('portfolio_type.csv')
        factory = PandasLoader(DEFAULT_COLUMN_MAPPER_BR)
        return factory.load(path_operations, path_types)
