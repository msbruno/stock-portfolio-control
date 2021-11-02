

import abc
from datetime import datetime
import pandas
from pandas.io import json
from src.external.datatable.datatable_pandas import DataTablePandas
from src.external.datatable.mappers import DEFAULT_COLUMN_MAPPER_BR
from src.use_cases.generate_portfolio_market_to_market.generate_portfolio_market_to_market import GeneratePortfolioMarkedToMarket
from src.use_cases.interfaces.datatable import DataTable, DataTableLoader
import plotly.express as px

from src.use_cases.process_operations.process_operations import ProcessOperations

class PrinterPortfolioPosition(abc.ABC):
    
    @abc.abstractmethod
    def print_type(self, data:DataTable, column_type:str, values:str, title:str):
        pass

class PrinterPortfolioPositionPlotly(PrinterPortfolioPosition):

    def print_type(self, data:DataTable, column_type:str, values:str, title:str):
        data_json = data.to_json()
        parsed = json.loads(data_json)
        df =  pandas.DataFrame.from_dict(parsed, orient='index')
        fig = px.pie(df, 
             values=values,
             names=column_type,
             title=title,
             labels={'ticker':'ticker'}
            )
        fig.update_traces(textposition='inside', textinfo='label+percent')
        #fig.show()
        fig.write_html("./file.html")

class GeneratePositionsReport:

    def __init__(self, 
        process_ops:ProcessOperations, 
        generate_portfolio:GeneratePortfolioMarkedToMarket, 
        printer: PrinterPortfolioPosition):
        self.__process_ops = process_ops
        self.__generate_portfolio:GeneratePortfolioMarkedToMarket = generate_portfolio
        self.__portfolio_printer = printer
        
    def generate_report(self,operations_data:DataTable, date:datetime=None):
        processed_operations = self.__process_ops.process_operations(operations_data)
        portfolio_marked_to_market = self.__generate_portfolio.portfolio_marked_to_market(processed_operations, date)
        column_currency = DEFAULT_COLUMN_MAPPER_BR.currency()
        currencies = portfolio_marked_to_market.unique(column_currency)

        for currency in currencies:
            filtered_postions = DataTablePandas(portfolio_marked_to_market[portfolio_marked_to_market[column_currency]==currency])
            self.__portfolio_printer.print_type(filtered_postions, DEFAULT_COLUMN_MAPPER_BR.ticker(), DEFAULT_COLUMN_MAPPER_BR.market_value(), 'teste')


        
       
        
        

        
