from test.use_cases.mark_to_market.mark_to_market_test import MarkToMarketUsingYahoo
from test.resources.load_file import path_resource
from src.external.datatable.datatable_loader import FactoryOperationsDataPandas
from src.external.datatable.mappers import OPERATION_MAPPER
from src.external.datatable.datatable_pandas import FactoryRowDataTablePandas
from src.use_cases.interfaces.mappers import ColumnMapper
from src.use_cases.process_operations.process_operations import ProcessOperations
from src.use_cases.generate_portfolio_market_to_market.generate_portfolio_market_to_market import GeneratePortfolioMarkedToMarket
import unittest

class TreatDataframe(unittest.TestCase):

    def test(self):

        column_mapper = ColumnMapper('data', 'ticker', 'operação', 'qtd', 'pm')
        process_ops = ProcessOperations(column_mapper)
        row_factory = FactoryRowDataTablePandas(OPERATION_MAPPER ,column_mapper)
        dt_loader = FactoryOperationsDataPandas(row_factory)
        generate = GeneratePortfolioMarkedToMarket(process_ops, dt_loader, MarkToMarketUsingYahoo())
        
        path_operations = path_resource('portfolio.csv')
        path_types = path_resource('portfolio_type.csv')
        generate.load(path_operations, path_types)
        data = generate.portfolio_marked_to_market()
        data.print()
