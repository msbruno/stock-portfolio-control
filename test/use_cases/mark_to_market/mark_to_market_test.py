from src.external.use_cases.datatable_loader import FactoryOperationsDataTablePandas
from src.use_cases.process_operations.process_operations import ProcessOperations
from src.external.datatable.mappers import OPERATION_MAPPER
from src.external.datatable.datatable_pandas import FactoryRowDataTablePandas
from src.use_cases.interfaces.mappers import ColumnMapper
from src.use_cases.interfaces.mark_to_market import MarkToMarket
import unittest

import yfinance as yf
import pandas_datareader.data as web
from src.use_cases.interfaces.datatable import OperationsDataTable
yf.pdr_override()


class MarkToMarketFake(MarkToMarket):

    def load_market_values(self, dt: OperationsDataTable):
        starting_day = dt.first_date()
        tickers = dt.get_all_tickes()
        last_market_value = web.get_data_yahoo(tickers, start=starting_day)['Close']
        self.__last_market_value = last_market_value.fillna(method='ffill')
        print(last_market_value)

    
    def mark(self, dt: OperationsDataTable):
        result = dt.copy()
        self.load_market_values(result)
        #dt.update()



class MarkToMarketTest(unittest.TestCase):
    
    def test(self):

        path = r'D:\carreira\Python\controle\stock-portfolio-control\src\main\portfolio.csv'
        path2 = r'D:\carreira\Python\controle\stock-portfolio-control\src\main\portfolio_type.csv'
        column_mapper =  ColumnMapper('data', 'ticker', 'operação', 'qtd', 'pm')
        row_factory = FactoryRowDataTablePandas(OPERATION_MAPPER, column_mapper)
        loader = FactoryOperationsDataTablePandas(row_factory)
        df = loader.load(path, path2)

        sut = ProcessOperations(column_mapper)
        df_result:OperationsDataTable = sut.process_operations(df)

        marker = MarkToMarketFake()
        marker.mark(df_result)