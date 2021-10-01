import datetime
from src.external.market_value.mark_to_market_yahoo import MarkToMarketUsingYahoo
from src.use_cases.interfaces.datatable import DataTable
from src.external.datatable.datatable_loader import FactoryDataTablePandas
from test.resources.load_file import path_resource
from src.use_cases.process_operations.process_operations import ProcessOperations
from src.external.datatable.mappers import DEFAULT_COLUMN_MAPPER

import unittest

class MarkToMarketUsingYahooTest(unittest.TestCase):
    
    def test_mark_to_market(self):

        path = path_resource('portfolio.csv')
        path2 = path_resource('portfolio_type.csv')
        loader = FactoryDataTablePandas(DEFAULT_COLUMN_MAPPER)
        df = loader.load(path, path2)

        sut = ProcessOperations(DEFAULT_COLUMN_MAPPER)
        df_processed:DataTable = sut.process_operations(df)

        marker = MarkToMarketUsingYahoo(DEFAULT_COLUMN_MAPPER)
        filter = datetime.datetime.strptime('12/10/2020', '%d/%m/%Y')
        marker.load_market_values(df_processed, filter)
        assert marker.last_market_value('FB') == 275.75