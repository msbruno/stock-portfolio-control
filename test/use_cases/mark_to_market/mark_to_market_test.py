import datetime
from src.external.datatable.datatable_loader import FactoryDataTablePandas
from test.resources.load_file import path_resource
from src.use_cases.process_operations.process_operations import ProcessOperations
from src.external.datatable.mappers import DEFAULT_COLUMN_MAPPER, OPERATION_MAPPER
from src.external.datatable.datatable_pandas import FactoryRowDataTablePandas
from src.use_cases.interfaces.mark_to_market import MarkToMarket

import unittest

import yfinance as yf
import pandas_datareader.data as web
from src.use_cases.interfaces.datatable import DataTable
yf.pdr_override()


class MarkToMarketUsingYahoo(MarkToMarket):

    def _load_market_values(self, dt: DataTable, date:datetime):
        if date is None:
            date = datetime.datetime.now()
        date_filter = date + datetime.timedelta(days=1)
        tickers = dt.get_all_tickes()
        if len(tickers) == 0:
            raise Exception("There are no tickers to mark portfolio to market. Insert a new date or operation table.")
        last_market_value = web.get_data_yahoo(tickers, end=date_filter)['Close']
        self.__last_market_value = last_market_value.fillna(method='ffill')

    
    def mark_to_market(self, dt: DataTable, date:datetime=None):
        result = dt.last_positions(date)
        self._load_market_values(result, date)

        for row in result:
            market_value_per_share = self.__market_value(row.ticker)
            market_value = market_value_per_share * row.shares
            result.update(row.index, "market_value", market_value)
        return result

    def __market_value(self, ticker:str):
        return self.__last_market_value[ticker].tail(1)[0]



class MarkToMarketUsingYahooTest(unittest.TestCase):
    
    def test_mark_to_market(self):

        path = path_resource('portfolio.csv')
        path2 = path_resource('portfolio_type.csv')
        
        row_factory = FactoryRowDataTablePandas(OPERATION_MAPPER, DEFAULT_COLUMN_MAPPER)
        loader = FactoryDataTablePandas(row_factory)
        df = loader.load(path, path2)

        sut = ProcessOperations(DEFAULT_COLUMN_MAPPER)
        df_processed:DataTable = sut.process_operations(df)

        marker = MarkToMarketUsingYahoo()
        filter = datetime.datetime.strptime('12/10/2020', '%d/%m/%Y')
        result = marker.mark_to_market(df_processed, filter)
        result.print()