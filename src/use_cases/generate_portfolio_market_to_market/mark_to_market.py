import abc
from datetime import datetime
import pandas as pd


class MarkToMarket(abc.ABC):

    @abc.abstractmethod
    def load_market_values(self, dt:pd.DataFrame,date:datetime=None)->pd.DataFrame:
        pass
    
    @abc.abstractmethod
    def last_market_value(self, ticker:str):
        pass