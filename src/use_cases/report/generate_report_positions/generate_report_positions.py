

import abc
from datetime import datetime

import pandas
from pandas.io import json
from src.use_cases.interfaces.mappers import ColumnMapper
from src.use_cases.generate_portfolio_market_to_market.generate_portfolio_market_to_market import GeneratePortfolioMarkedToMarket
from src.use_cases.interfaces.datatable import DataTable
import plotly.express as px

class PrinterPortfolioPosition(abc.ABC):

    @abc.abstractmethod
    def print_positions(self, data:DataTable):
        pass
    
    @abc.abstractmethod
    def print_type(self, data:DataTable, column_type:str):
        pass

class PrinterPortfolioPositionPlotly(PrinterPortfolioPosition):

    def __init__(self, column_mapper: ColumnMapper) -> None:
        self.__column_mapper  = column_mapper

    def print_positions(self, data:DataTable):
        data_json = data.to_json()
        parsed = json.loads(data_json)
        df =  pandas.DataFrame.from_dict(parsed, orient='index')
        fig = px.pie(df, 
             values=self.__column_mapper.acc_value(),
             names=self.__column_mapper.ticker_column(),
             title='market_value',
             labels={'ticker':'ticker'}
            )
        fig.update_traces(textposition='inside', textinfo='label+percent')
        fig.show()

    def print_type(self, data:DataTable, column_type:str):
        data_json = data.to_json()
        parsed = json.loads(data_json)
        df =  pandas.DataFrame.from_dict(parsed, orient='index')
        fig = px.pie(df, 
             values=self.__column_mapper.acc_value(),
             names=column_type,
             title='market_value',
             labels={'ticker':'ticker'}
            )
        fig.update_traces(textposition='inside', textinfo='label+percent')
        fig.show()


class GeneratePositionsReport:

    def __init__(self, generate_portfolio:GeneratePortfolioMarkedToMarket, printer: PrinterPortfolioPosition):
        self.__generate_portfolio:GeneratePortfolioMarkedToMarket = generate_portfolio
        self.__portfolio_printer = printer
        
    def generate_report(self, path_datatable_operations:str, path_datatable_types:str, date:datetime=None):
        result = self.__generate_portfolio.load(path_datatable_operations, path_datatable_types)
        result = self.__generate_portfolio.portfolio_marked_to_market(date)
        
        self.__portfolio_printer.print_positions(result)
        self.__portfolio_printer.print_type(result, 'type3')
        
       
        
        

        
