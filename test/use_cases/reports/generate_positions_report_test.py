from test.resources.load_file import path_resource
from test.use_cases.mark_to_market.mark_to_market_test import MarkToMarketUsingYahoo
from src.external.datatable.pandas_loader import PandasLoader
from src.external.datatable.mappers import DEFAULT_COLUMN_MAPPER_BR
from src.use_cases.process_operations.process_operations import ProcessOperations
from src.use_cases.generate_portfolio_market_to_market.generate_portfolio_market_to_market import GeneratePortfolio
import unittest


class GeneratePositionsReportTest(unittest.TestCase):

    def test(self):
        column_mapper =  DEFAULT_COLUMN_MAPPER_BR
        process_ops = ProcessOperations(column_mapper)
        df_loader = PandasLoader(column_mapper)
        marker = MarkToMarketUsingYahoo(column_mapper)
        generate_portfolio = GeneratePortfolio(column_mapper)


        path_operations = path_resource('portfolio.csv')
        path_types = path_resource('portfolio_type.csv')
        operations = df_loader.load(path_operations, path_types)

        processed_operations = process_ops.process_operations(operations)
        portfolio = generate_portfolio.generate_portfolio(processed_operations)
        #portfolio_marked_to_market = 
        portfolio_marked_to_market_with_currency = generate_portfolio.mark_to_currency(portfolio_marked_to_market)
        
        

        
     
        #self.assertEqual(0,0)
    