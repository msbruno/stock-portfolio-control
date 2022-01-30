
from src.use_cases.generate_portfolio_market_to_market.mark_to_market import MarkToMarket
from src.use_cases.interfaces.mappers import ColumnMapper
import yfinance as yf
import pandas_datareader.data as web
import datetime
import pandas as pd
yf.pdr_override()


class MarkToMarketUsingYahoo(MarkToMarket):

    def __init__(self, column_mapper:ColumnMapper) -> None:
        self.__column_mapper = column_mapper

    def load_market_values(self, dt: pd.DataFrame,date:datetime=None)->pd.DataFrame:
        if date is None:
            date = datetime.datetime.now()
        date_filter = date + datetime.timedelta(days=1)
        tickers = dt[self.__column_mapper.ticker()].unique().tolist()
        
        if len(tickers) == 0:
            raise Exception("There are no tickers to mark portfolio to market. Insert a new date or operation table.")
        last_market_value = web.get_data_yahoo(tickers, end=date_filter)['Close']
        self.__last_market_value = last_market_value.fillna(method='ffill')


    def last_market_value(self, ticker:str):
        return self.__last_market_value[ticker].tail(1)[0]