from test.resources.load_file import path_resource
from test.use_cases.mark_to_market.mark_to_market_test import MarkToMarketUsingYahoo
from src.external.datatable.datatable_loader import FactoryDataTablePandas
from src.external.datatable.mappers import DEFAULT_COLUMN_MAPPER_BR, OPERATION_MAPPER
from src.use_cases.process_operations.process_operations import ProcessOperations
from src.use_cases.generate_portfolio_market_to_market.generate_portfolio_market_to_market import GeneratePortfolioMarkedToMarket
from src.use_cases.report.generate_report_positions.generate_report_positions import GeneratePositionsReport, PrinterPortfolioPositionPlotly
import unittest


class GeneratePositionsReportTest(unittest.TestCase):

    def test(self):
        process_ops = ProcessOperations(DEFAULT_COLUMN_MAPPER_BR)
        df_loader = FactoryDataTablePandas(DEFAULT_COLUMN_MAPPER_BR)
        generate_portfolio = GeneratePortfolioMarkedToMarket(MarkToMarketUsingYahoo(DEFAULT_COLUMN_MAPPER_BR), DEFAULT_COLUMN_MAPPER_BR)
        generate_report = GeneratePositionsReport(process_ops, generate_portfolio, PrinterPortfolioPositionPlotly())

        path_operations = path_resource('portfolio.csv')
        path_types = path_resource('portfolio_type.csv')
        operations = df_loader.load(path_operations, path_types)
        generate_report.generate_report(operations)
        
    
        #self.assertEqual(0,0)
    