

from datetime import datetime
from src.use_cases.generate_portfolio_market_to_market.generate_portfolio_market_to_market import GeneratePortfolioMarkedToMarket
from src.use_cases.interfaces.mark_to_market import MarkToMarket
from src.use_cases.process_operations.process_operations import ProcessOperations
from src.use_cases.interfaces.datatable import DataTable, DataTableLoader
import plotly.express as px

class GenerateReportPositions:

    def __init__(self, generate_portfolio:GeneratePortfolioMarkedToMarket, printer):
        self.__generate_portfolio:GeneratePortfolioMarkedToMarket = generate_portfolio
        self.__portfolio_printer = printer
        
    def generate_report(self, path_datatable_operations:str, path_datatable_types:str, date:datetime=None):
        result = self.__generate_portfolio.load(path_datatable_operations, path_datatable_types)
        result = self.__generate_portfolio.portfolio_marked_to_market(date)
        self.__portfolio_printer.print(result)
        
        

        
