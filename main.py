

from datetime import datetime
from src.use_cases.interfaces.datatable import DataTable
from test.resources.load_file import path_resource
from src.use_cases.report.generate_report_positions.generate_report_positions import PrinterPortfolioPositionPlotly
from test.use_cases.mark_to_market.mark_to_market_test import MarkToMarketUsingYahoo
from src.use_cases.generate_portfolio_market_to_market.generate_portfolio_market_to_market import GeneratePortfolioMarkedToMarket
from src.external.datatable.datatable_loader import FactoryDataTablePandas
from src.use_cases.process_operations.process_operations import ProcessOperations
from src.external.datatable.mappers import DEFAULT_COLUMN_MAPPER


def process_operations(path_operations:str, path_types:str, separator:str=None, data_format:str=None)->DataTable:
    factory = FactoryDataTablePandas(DEFAULT_COLUMN_MAPPER, separator, data_format)
    data = factory.load(path_operations, path_types)
    processor = ProcessOperations(DEFAULT_COLUMN_MAPPER)
    return processor.process_operations(data)

def generate_portfolio_marked_to_market(operations:DataTable, date_filter:datetime=None):
    generate_portfolio = GeneratePortfolioMarkedToMarket(MarkToMarketUsingYahoo(DEFAULT_COLUMN_MAPPER), DEFAULT_COLUMN_MAPPER)
    return generate_portfolio.portfolio_marked_to_market(operations, date_filter)

def print_portfolio_positions(data:DataTable):
    printer = PrinterPortfolioPositionPlotly()
    printer.print_type(data, DEFAULT_COLUMN_MAPPER.ticker_column(), DEFAULT_COLUMN_MAPPER.acc_value())


path_operations = path_resource('portfolio.csv')
path_types = path_resource('portfolio_type.csv')
data = process_operations(path_operations, path_types)
data = generate_portfolio_marked_to_market(data)
print_portfolio_positions(data)


'''
data = LoadOperations(x,y)
a = markToMarket(LoadOperations)
b = markToMarketUsingCurrency()

'''


    