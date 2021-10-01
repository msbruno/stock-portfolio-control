
from src.use_cases.interfaces.mappers import ColumnMapper
from src.use_cases.interfaces.mark_to_market import MarkToMarket
import yfinance as yf
import pandas_datareader.data as web
from src.use_cases.interfaces.datatable import DataTable
import datetime
yf.pdr_override()


class MarkToMarketUsingYahoo(MarkToMarket):

    def __init__(self, column_mapper:ColumnMapper) -> None:
        self.__column_mapper = column_mapper

    def load_market_values(self, dt: DataTable,date:datetime=None)->DataTable:
        if date is None:
            date = datetime.datetime.now()
        date_filter = date + datetime.timedelta(days=1)
        tickers = dt.unique(self.__column_mapper.ticker_column())
        if len(tickers) == 0:
            raise Exception("There are no tickers to mark portfolio to market. Insert a new date or operation table.")
        last_market_value = web.get_data_yahoo(tickers, end=date_filter)['Close']
        self.__last_market_value = last_market_value.fillna(method='ffill')


    def last_market_value(self, ticker:str):
        return self.__last_market_value[ticker].tail(1)[0]