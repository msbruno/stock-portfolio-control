

from datetime import datetime
from src.use_cases.interfaces.datatable import DataTable
from test.resources.load_file import path_resource
from src.use_cases.report.generate_report_positions.generate_report_positions import PrinterPortfolioPositionPlotly
from test.use_cases.mark_to_market.mark_to_market_test import MarkToMarketUsingYahoo
from src.use_cases.generate_portfolio_market_to_market.generate_portfolio_market_to_market import GeneratePortfolioMarkedToMarket
from src.external.datatable.datatable_loader import FactoryDataTablePandas
from src.use_cases.process_operations.process_operations import ProcessOperations
from src.external.datatable.mappers import DEFAULT_COLUMN_MAPPER


def load_operations(path:str, path_types:str, separator:str=None, data_format:str=None):
    factory = FactoryDataTablePandas(DEFAULT_COLUMN_MAPPER, separator, data_format)
    return factory.load(path_operations, path_types)

def generate_portfolio_marked_to_market(path:str, path_types:str):
    process_ops = ProcessOperations(DEFAULT_COLUMN_MAPPER)
    dt_loader = FactoryDataTablePandas(DEFAULT_COLUMN_MAPPER)
    generate_portfolio = GeneratePortfolioMarkedToMarket(process_ops, dt_loader, MarkToMarketUsingYahoo())
    return generate_portfolio.load(path, path_types).portfolio_marked_to_market()

def print_portfolio_positions(data:DataTable):
    printer = PrinterPortfolioPositionPlotly(DEFAULT_COLUMN_MAPPER)
    printer.print_positions(data)



path_operations = path_resource('portfolio.csv')
path_types = path_resource('portfolio_type.csv')
data = load_operations(path_operations, path_types)

data = generate_portfolio_marked_to_market(path_operations, path_types)
print_portfolio_positions(data)


'''
data = LoadOperations(x,y)
a = markToMarket(LoadOperations)
b = markToMarketUsingCurrency()

'''


    