

from datetime import datetime
from src.use_cases.convert_currency.convert_currency import ConvertCurrency
from src.use_cases.interfaces.datatable import DataTable
from test.resources.load_file import path_resource
from src.use_cases.report.generate_report_positions.generate_report_positions import PrinterPortfolioPositionPlotly
from test.use_cases.mark_to_market.mark_to_market_test import MarkToMarketUsingYahoo
from src.use_cases.generate_portfolio_market_to_market.generate_portfolio_market_to_market import GeneratePortfolioMarkedToMarket
from src.external.datatable.datatable_loader import FactoryDataTablePandas
from src.use_cases.process_operations.process_operations import ProcessOperations
from src.external.datatable.mappers import DEFAULT_COLUMN_MAPPER_BR


def process_operations(path_operations:str, path_types:str, separator:str=None, data_format:str=None)->DataTable:
    factory = FactoryDataTablePandas(DEFAULT_COLUMN_MAPPER_BR, separator, data_format)
    data = factory.load(path_operations, path_types)
    processor = ProcessOperations(DEFAULT_COLUMN_MAPPER_BR)
    return processor.process_operations(data)

def generate_portfolio_marked_to_market(operations:DataTable, date_filter:datetime=None):
    generate_portfolio = GeneratePortfolioMarkedToMarket(MarkToMarketUsingYahoo(DEFAULT_COLUMN_MAPPER_BR), DEFAULT_COLUMN_MAPPER_BR)
    return generate_portfolio.portfolio_marked_to_market(operations, date_filter)

def generate_portfolio_marked_to_market_adjusted_by_currency(data:DataTable):
    currency_converter = ConvertCurrency(DEFAULT_COLUMN_MAPPER_BR)
    return currency_converter.convert(data)

def print_portfolio_positions(data:DataTable):
    printer = PrinterPortfolioPositionPlotly()
    printer.print_type(data, DEFAULT_COLUMN_MAPPER_BR.ticker_column(), DEFAULT_COLUMN_MAPPER_BR.acc_value())




path_operations = path_resource('portfolio.csv')
path_types = path_resource('portfolio_type.csv')
data_operations = process_operations(path_operations, path_types)
data_porfolio = generate_portfolio_marked_to_market(data_operations)
print_portfolio_positions(data_operations)
data_porfolio = generate_portfolio_marked_to_market_adjusted_by_currency(data_operations)
print_portfolio_positions(data_porfolio)

'''
data = LoadOperations(x,y)
a = markToMarket(LoadOperations)
b = markToMarketUsingCurrency()

'''


    