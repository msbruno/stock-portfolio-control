

from datetime import datetime
from test.resources.load_file import path_resource
from src.use_cases.report.generate_report_positions.generate_report_positions import GeneratePositionsReport, PrinterPortfolioPositionPlotly
from test.use_cases.mark_to_market.mark_to_market_test import MarkToMarketUsingYahoo
from src.use_cases.generate_portfolio_market_to_market.generate_portfolio_market_to_market import GeneratePortfolioMarkedToMarket
from src.external.datatable.datatable_loader import FactoryDataTablePandas
from src.use_cases.process_operations.process_operations import ProcessOperations
from src.external.datatable.mappers import DEFAULT_COLUMN_MAPPER


def run(path:str, path2:str, date:datetime=None):
    process_ops = ProcessOperations(DEFAULT_COLUMN_MAPPER)
    dt_loader = FactoryDataTablePandas(DEFAULT_COLUMN_MAPPER)
    generate_portfolio = GeneratePortfolioMarkedToMarket(process_ops, dt_loader, MarkToMarketUsingYahoo())
    data = generate_portfolio.load(path, path2).portfolio_marked_to_market(date)
    printer = PrinterPortfolioPositionPlotly(DEFAULT_COLUMN_MAPPER)
    #printer.print_positions(data)
    printer.print_type(data,'type3' )


path_operations = path_resource('portfolio.csv')
path_types = path_resource('portfolio_type.csv')

run(path_operations, path_types)
    