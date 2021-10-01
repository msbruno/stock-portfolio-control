import abc
from datetime import datetime
from src.use_cases.interfaces.datatable import DataTable


class MarkToMarket(abc.ABC):

    @abc.abstractmethod
    def load_market_values(self, dt: DataTable,date:datetime=None)->DataTable:
        pass
    
    @abc.abstractmethod
    def last_market_value(self, ticker:str):
        pass